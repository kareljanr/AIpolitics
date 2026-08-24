# -*- coding: utf-8 -*-
from pathlib import Path
import csv
import re
import ssl
import urllib.request

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent

mined = set()
for path in [
    "docs/doge/data/entities.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
]:
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
            for m in re.findall(r"\d{10}", blob):
                mined.add(m)

CANDS = [
    ("0446506836", "avondvrede"),
    # Anima / Anima Group holding guesses - search via known
    ("0460123987", "skip"),
    # Try Anima Zorggroep / Anima NV common
    ("0470123456", "skip2"),
]


def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            data = r.read()
        path.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, type(e).__name__, str(e)[:80])
        return None


# Resolve Anima group KBO
for label, url in [
    ("anima_search", "https://www.companyweb.be/nl/anima"),
    ("anima_en", "https://www.companyweb.be/en/anima"),
]:
    t = fetch(url, out / f"{label}.html")
    if t:
        kbos = re.findall(r"/(?:nl|en)/(\d{10})", t)
        print(label, list(dict.fromkeys(kbos))[:20])
        for k in list(dict.fromkeys(kbos))[:12]:
            CANDS.append((k, f"anima_{k}"))

for kbo, label in CANDS:
    if "skip" in label:
        continue
    status = "MINED" if kbo in mined else "FREE"
    print("---", label, kbo, status)
    if status == "MINED" and label != "avondvrede":
        continue
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_en.html")
    if not t:
        continue
    # also NL/FR/KBO for avondvrede if strong
    title = re.search(r"<title>([^<]+)", t)
    if not title or "Error 404" in title.group(1):
        print(" 404")
        continue
    yblocks = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):

        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yblocks[y] = {
            k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]
        }
    fte = re.search(r"([\d.,]+)\s*FTE", t)
    filed = re.search(r"filed on ([0-9-]{10})", t)
    nace = list(dict.fromkeys(re.findall(r"(87\.\d{3}|88\.\d{3})", t)))[:5]
    print(" title", title.group(1)[:110])
    print(
        " fte",
        fte.group(1) if fte else "-",
        "filed",
        filed.group(1) if filed else "-",
        "nace",
        nace,
    )
    for y in sorted(yblocks, reverse=True)[:2]:
        print(" ", y, yblocks[y])
    y5 = yblocks.get("2025", {})
    if any(y5.get(k) for k in ("omzet", "bruto_marge", "winst")):
        omzet = (y5.get("omzet") or "").replace(",", "")
        if status == "FREE" and (omzet.isdigit() or y5.get("bruto_marge")):
            print(" >>> LIVE FREE YE2025")

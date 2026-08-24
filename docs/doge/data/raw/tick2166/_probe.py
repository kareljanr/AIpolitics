# -*- coding: utf-8 -*-
import csv
import re
import ssl
import urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent
out.mkdir(parents=True, exist_ok=True)

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
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    ("0877556624", "agb_bornem"),
    ("0446506836", "avondvrede"),
    ("0469969453", "anima_hold"),
    ("0755822317", "lork_hoeselt"),
]


def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            data = r.read()
        path.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", path.name, type(e).__name__, str(e)[:70])
        return None


for kbo, label in CANDS:
    status = "MINED" if kbo in mined else "FREE"
    print("===", label, kbo, status)
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_en.html")
    if not t:
        continue
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
    print(" ", title.group(1)[:95])
    print(
        "  fte",
        fte.group(1) if fte else "-",
        "filed",
        filed.group(1) if filed else "-",
    )
    for y in sorted(yblocks, reverse=True)[:2]:
        print(" ", y, yblocks[y])
    y5 = yblocks.get("2025", {})
    if status == "FREE" and any(
        y5.get(k) for k in ("omzet", "bruto_marge", "winst", "eigen_vermogen")
    ):
        omzet = (y5.get("omzet") or "").replace(",", "")
        if omzet.isdigit() and int(omzet) >= 500_000:
            print(" >>> STRONG")

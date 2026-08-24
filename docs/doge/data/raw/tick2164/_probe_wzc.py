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

mined = set()
for path in [
    "docs/doge/data/entities.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
]:
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
            for m in re.findall(r"0\d{9}", blob):
                mined.add(m)

CANDS = [
    ("0410219433", "haagwinde"),
    ("0459770496", "sint_augustinus_halle"),
    ("0422152314", "sint_barbara_herselt"),
    ("0414678562", "vander_stokken"),
    ("0410142031", "olv_lourdes"),
    ("0430882809", "ter_engelen"),
    ("0410509443", "kanunnik_triest"),
    ("0449507205", "veilige_have"),
    ("0452865383", "sint_jozef_ninove"),
    ("0425678912", "skip"),
    # more from search variants
    ("0461511449", "st_vincentius_lendelede"),
    ("0418016550", "st_vincentius_antwerpen"),
    ("0473762450", "zusterhof"),
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


for kbo, label in CANDS:
    if label == "skip":
        continue
    status = "MINED" if kbo in mined else "FREE"
    print("---", label, kbo, status)
    if status == "MINED":
        continue
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
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    filed = re.search(r"filed on ([0-9-]{10})", t)
    nace = list(dict.fromkeys(re.findall(r"(87\.\d{3}|88\.\d{3})", t)))[:4]
    print(" title", title.group(1)[:100])
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
    omzet = (y5.get("omzet") or "").replace(",", "")
    if omzet.isdigit() and int(omzet) >= 1_000_000:
        print(" >>> STRONG")

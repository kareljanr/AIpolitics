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
    "docs/doge/data/budgets.csv",
]:
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
            for m in re.findall(r"0\d{9}", blob):
                mined.add(m)
print("mined count", len(mined))


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


def detail(label, t, kbo):
    title = re.search(r"<title>([^<]+)", t)
    year = None
    for pat in [
        r"Last balance sheet year[^0-9N]{0,120}(20\d\d|N/A)",
        r"Last financial year[^0-9N]{0,120}(20\d\d|N/A)",
        r"Laatste balansjaar[^0-9N]{0,120}(20\d\d|N/A)",
    ]:
        m = re.search(pat, t, re.I)
        if m:
            year = m.group(1)
            break
    yblocks = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):

        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yblocks[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    filed = re.search(r"filed on ([0-9-]{10})", t) or re.search(
        r"neergelegd op ([0-9-]{10})", t
    )
    nace = list(dict.fromkeys(re.findall(r"(87\.\d{3}|88\.\d{3}|86\.\d{3})", t)))[:6]
    free = kbo not in mined
    print("=" * 50)
    print(
        label,
        kbo,
        "FREE" if free else "MINED",
        "year",
        year,
        "fte",
        fte.group(1) if fte else "-",
        "filed",
        filed.group(1) if filed else "-",
        "nace",
        nace,
    )
    print(" title", (title.group(1)[:100] if title else "?"))
    for y in sorted(yblocks, reverse=True)[:3]:
        print(" ", y, yblocks[y])
    return free, year, yblocks


CANDS = [
    ("0450755634", "residentie_oudenburg"),
    ("0755822317", "lork_hoeselt"),
    ("0823488131", "thofke"),
    ("0415653116", "maria_boodschap_niel"),
    ("0413055989", "sint_jozef_aarschot"),
    ("0416337262", "home_vrijzicht_ieper"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    ("0893863017", "faro"),
    # extra unused care guesses / known from prior notes
    ("0421.479.153".replace(".", ""), "le_hanois_check"),  # mined expect
    ("0473694748", "ruggeveld_check"),
    ("0432582485", "bernardus_check"),
    ("0404415728", "wzc_de_meers"),
    ("0428674121", "huis_ter_meulen"),
    ("0460462814", "residentie_sonneweelde"),
    ("0478.642.519".replace(".", ""), "wzc_zonnige_ruste"),
    ("0403546879", "rusthuis_ter_veste"),
    ("0439.082.156".replace(".", ""), "wzc_de_wingerd"),
    ("0414.497.710".replace(".", ""), "olvf_kortrijk"),
    ("0425.306.478".replace(".", ""), "sint_anna_brugge"),
]

for kbo, label in CANDS:
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_en.html")
    if t:
        detail(label, t, kbo)

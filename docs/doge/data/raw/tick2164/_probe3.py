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
    if not title or "Error 404" in title.group(1):
        print(label, kbo, "404")
        return False
    yblocks = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):

        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yblocks[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    filed = re.search(r"filed on ([0-9-]{10})", t)
    nace = list(dict.fromkeys(re.findall(r"(87\.\d{3}|88\.\d{3})", t)))[:6]
    free = kbo not in mined
    y5 = yblocks.get("2025", {})
    live = any(y5.get(k) for k in ("omzet", "bruto_marge", "winst", "eigen_vermogen"))
    print("=" * 50)
    print(
        label,
        kbo,
        "FREE" if free else "MINED",
        "YE2025" if live else "noYE2025",
        "fte",
        fte.group(1) if fte else "-",
        "filed",
        filed.group(1) if filed else "-",
        "nace",
        nace,
    )
    print(" title", title.group(1)[:110])
    for y in sorted(yblocks, reverse=True)[:2]:
        print(" ", y, yblocks[y])
    return free and live


CANDS = [
    ("0475400760", "famifamenne"),
    ("0411515075", "emmaus"),
    ("0470673890", "zorg_saam"),
    ("0428692191", "de_medemens"),  # likely mined
    ("0408041271", "huize_ter_linde"),
    ("0416934425", "sint_anna"),
    ("0422540661", "de_meerssen"),
    ("0427301819", "olvf"),
    # Oase / Witte Meren / De Meers Waregem / Avondvrede - try search via companyweb name URLs hard; use known
    ("0435440123", "oase_guess"),
    ("0460123456", "witte_guess"),
    # From staatsblad Avondvrede - search
    ("0400123456", "avond_guess"),
    # Probe companyweb search pages?
]

# Try Upswitch / Pappers search is better. Web: companyweb avondvrede
for kbo, label in CANDS:
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_en.html")
    if t:
        detail(label, t, kbo)

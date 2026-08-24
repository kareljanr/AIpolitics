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
    if title and "Error 404" in title.group(1):
        print(label, kbo, "404")
        return
    yblocks = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):

        def g(k, b=body):
            m = re.search(rf'{k}:\s*"([^"]*)"', b)
            return m.group(1) if m else None

        yblocks[y] = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    filed = re.search(r"filed on ([0-9-]{10})", t)
    nace = list(
        dict.fromkeys(re.findall(r"(87\.\d{3}|88\.\d{3}|86\.\d{3})", t))
    )[:8]
    free = kbo not in mined
    y2025 = yblocks.get("2025")
    has_live = bool(y2025 and (y2025.get("omzet") or y2025.get("bruto_marge") or y2025.get("winst")))
    print("=" * 50)
    print(
        label,
        kbo,
        "FREE" if free else "MINED",
        "LIVE2025" if has_live else "no2025",
        "fte",
        fte.group(1) if fte else "-",
        "filed",
        filed.group(1) if filed else "-",
        "nace",
        nace,
    )
    print(" title", (title.group(1)[:110] if title else "?"))
    for y in sorted(yblocks, reverse=True)[:2]:
        print(" ", y, yblocks[y])


# Lork Hoeselt deep + more WZC/MRS candidates (known care names / nearby KBOs)
CANDS = [
    ("0755822317", "lork_hoeselt"),
    ("0823488131", "thofke"),
    # Flemish WZC candidates often unused
    ("0400387582", "wzc_zonnebloem"),
    ("0412187654", "dummy"),
    ("0420.555.123".replace(".", ""), "dummy2"),
    ("0431.222.111".replace(".", ""), "dummy3"),
    ("0440.123.456".replace(".", ""), "dummy4"),
    ("0455.789.012".replace(".", ""), "dummy5"),
    # From common WZC lists
    ("0408.041.271".replace(".", ""), "huize_ter_linde"),
    ("0416.934.425".replace(".", ""), "sint_anna"),
    ("0422.540.661".replace(".", ""), "de_meerssen"),
    ("0427.301.819".replace(".", ""), "olvf"),
    ("0435.678.901".replace(".", ""), "x"),
    ("0441.789.123".replace(".", ""), "y"),
    ("0465.320.147".replace(".", ""), "z"),
    ("0472.111.333".replace(".", ""), "a"),
    ("0480.555.777".replace(".", ""), "b"),
    ("0508.123.456".replace(".", ""), "c"),
    ("0535.987.654".replace(".", ""), "d"),
    ("0558.111.222".replace(".", ""), "e"),
    ("0600.111.222".replace(".", ""), "f"),
    ("0628.333.444".replace(".", ""), "g"),
    ("0645.555.666".replace(".", ""), "h"),
    ("0678.777.888".replace(".", ""), "i"),
    ("0700.111.222".replace(".", ""), "j"),
    ("0725.333.444".replace(".", ""), "k"),
    ("0740.555.666".replace(".", ""), "l"),
    ("0765.777.888".replace(".", ""), "m"),
    ("0780.999.000".replace(".", ""), "n"),
    ("0800.111.222".replace(".", ""), "o"),
    # better: search via known unused from tick notes / adjacent
    ("0415.653.116".replace(".", ""), "maria_boodschap"),  # YE2024
    ("0425.852.147".replace(".", ""), "wzc_cand1"),
    ("0438.741.258".replace(".", ""), "wzc_cand2"),
    ("0449.852.369".replace(".", ""), "wzc_cand3"),
    ("0456.963.147".replace(".", ""), "wzc_cand4"),
    ("0467.159.258".replace(".", ""), "wzc_cand5"),
    ("0475.268.369".replace(".", ""), "wzc_cand6"),
    ("0488.377.159".replace(".", ""), "wzc_cand7"),
    ("0402.147.258".replace(".", ""), "wzc_cand8"),
    ("0405.369.147".replace(".", ""), "wzc_cand9"),
    ("0410.258.369".replace(".", ""), "wzc_cand10"),
    ("0412.369.147".replace(".", ""), "wzc_cand11"),
    ("0418.147.258".replace(".", ""), "wzc_cand12"),
    ("0423.258.369".replace(".", ""), "wzc_cand13"),
    ("0428.369.147".replace(".", ""), "wzc_cand14"),
    ("0433.147.258".replace(".", ""), "wzc_cand15"),
    ("0436.258.369".replace(".", ""), "wzc_cand16"),
    ("0442.369.147".replace(".", ""), "wzc_cand17"),
    ("0446.147.258".replace(".", ""), "wzc_cand18"),
    ("0451.258.369".replace(".", ""), "wzc_cand19"),
    ("0458.369.147".replace(".", ""), "wzc_cand20"),
]

# Smarter: web search companyweb for woonzorgcentrum + unused
# Also probe Lork Hoeselt KBO fully + search staatsbladmonitor / known lists

# Focused known WZC names via companyweb slug search is hard; use KBO from open data?
# Try a short curated list from Flemish care sector names not in do-not-redo
CURATED = [
    ("0755822317", "lork_hoeselt"),
    ("0823488131", "thofke"),
    ("0400387582", "probe_0400387582"),
    ("0416934425", "sint_anna_probe"),
    ("0422540661", "de_meerssen"),
    ("0427301819", "olvf_probe"),
    ("0408041271", "huize_ter_linde"),
    ("0412187654", "probe_0412187654"),
    # Walloon MRS unused
    ("0400.111.222".replace(".", ""), "w1"),
    ("0421.111.222".replace(".", ""), "w2"),
    ("0432.111.222".replace(".", ""), "w3"),
    ("0443.111.222".replace(".", ""), "w4"),
    ("0454.111.222".replace(".", ""), "w5"),
    ("0465.111.222".replace(".", ""), "w6"),
    ("0476.111.222".replace(".", ""), "w7"),
    ("0487.111.222".replace(".", ""), "w8"),
    ("0498.111.222".replace(".", ""), "w9"),
    ("0501.111.222".replace(".", ""), "w10"),
]

# Instead: parse companyweb search? Or use bing/web for "woonzorgcentrum companyweb 2025"
# Practical: take Lork Hoeselt (named WZC, YE2025, FREE) OR find via web_search

for kbo, label in CURATED[:8]:
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_en.html")
    if t:
        detail(label, t, kbo)

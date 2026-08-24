# -*- coding: utf-8 -*-
from pathlib import Path
import re
import csv
import ssl
import urllib.request

csv.field_size_limit(10**7)
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
out = Path(__file__).resolve().parent

mined = set()
with open(Path(r"docs/doge/data/entities.csv"), newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        blob = re.sub(r"[.\s]", "", " ".join(str(v) for v in row.values()))
        for m in re.findall(r"0\d{9}", blob):
            mined.add(m)


def fetch(url, path):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as r:
            data = r.read()
        path.write_bytes(data)
        return data.decode("utf-8", "ignore")
    except Exception as e:
        print("FAIL", url, e)
        return None


def summarize(label, t):
    title = re.search(r"<title>([^<]+)", t)
    year = re.search(r"Last balance sheet year[^0-9N]{0,80}(20\d\d|N/A)", t)
    if not year:
        year = re.search(r"Laatste balansjaar[^0-9N]{0,80}(20\d\d|N/A)", t)
    nums = re.findall(r"/en/(0\d{9})", t) or re.findall(r"BE0(\d{9})", t) or re.findall(r"BE(\d{10})", t)
    nums = [n[-10:] if len(n) >= 10 else n for n in nums]
    nums = list(dict.fromkeys(nums))
    y25 = None
    for y, body in re.findall(r'(20\d\d)\s*:\s*\{([^{}]+)\}', t):
        if y in ("2025", "2026"):
            def g(k, b=body):
                m = re.search(rf'{k}:\s*"([^"]*)"', b)
                return m.group(1) if m else None
            y25 = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
            break
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    free = [n for n in nums if n not in mined]
    print(
        label,
        (title.group(1)[:55] if title else "?"),
        "Y",
        year.group(1) if year else "-",
        "data",
        y25,
        "fte",
        fte.group(1) if fte else "-",
        "nums",
        nums[:3],
        "FREE",
        free[:3],
    )
    return free, y25, year.group(1) if year else "-"


# From tick2153 filenames that looked like MRS probes
prior = Path(r"docs/doge/data/raw/tick2153")
for name in [
    "hestalie_en.html",
    "niraye_en.html",
    "ambleve_en.html",
    "fac_similiter_search.html",
    "bremdael_search.html",
    "zottegem_jr2025",
]:
    p = prior / name
    if p.exists() and p.is_file():
        summarize(name, p.read_text(encoding="utf-8", errors="ignore"))

# Fresh candidates - Walloon/Flemish MRS likely unused (from directories / siblings)
URLS = [
    # Résidence Les Tilleuls / common Walloon names via KBO guesses won't work
    # Use companyweb pages found via name search patterns from known public lists
    ("https://www.companyweb.be/en/0464.558.219", "cand1"),  # may fail
]

# Better public pages: search staatsbladmonitor / companyweb for specific unused
# Try entities mentioned in Apricusa news + LNA Santé Belgian homes
MORE = [
    "https://www.companyweb.be/en/0466778899",  # skip
]

# Known LNA Santé BE / other chains - look up via web results KBOs
# From prior deferred notes in loop: try "Résidence Les Acacias", "Home Saint-Joseph" etc.
NAME_PAGES = [
    ("https://www.companyweb.be/nl/0428551234", "x"),
]

# Practical approach: open Northdata/CW for entities from tick2153 z*.html which may be zone list
for f in sorted(prior.glob("z*_en.html"))[:20]:
    t = f.read_text(encoding="utf-8", errors="ignore")
    title = re.search(r"<title>([^<]+)", t)
    year = re.search(r"Last balance sheet year[^0-9N]{0,80}(20\d\d|N/A)", t)
    if year and year.group(1) in ("2025", "2026"):
        summarize(f.name, t)

# Probe concrete public care KBOs from directories
CONCRETE = [
    # Maison de repos Notre-Dame / various
    ("0471.234.890", "https://www.companyweb.be/en/0471234890"),
    # Try KBOs extracted from hestalie/niraye if present in HTML as links
]

for f in ["hestalie_en.html", "niraye_en.html", "ambleve_en.html"]:
    p = prior / f
    if not p.exists():
        continue
    t = p.read_text(encoding="utf-8", errors="ignore")
    print("FILE", f, "len", len(t), "title", (re.search(r"<title>([^<]+)", t) or type("x", (), {"group": lambda *_: "?"})()).group(1)[:80])
    # print year snippets
    for pat in ["Last balance", "Laatste balans", "omzet", "Turnover", "2025", "2024"]:
        i = t.find(pat)
        if i >= 0:
            snippet = re.sub(r"<[^>]+>", " ", t[i : i + 120])
            snippet = re.sub(r"\s+", " ", snippet)
            print(" ", pat, snippet[:100])

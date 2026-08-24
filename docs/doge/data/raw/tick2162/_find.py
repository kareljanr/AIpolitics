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
        print("FAIL", path.name, e)
        return None


def summarize(label, t):
    title = re.search(r"<title>([^<]+)", t)
    year = re.search(r"Last balance sheet year[^0-9N]{0,80}(20\d\d|N/A)", t)
    if not year:
        year = re.search(r"Laatste balansjaar[^0-9N]{0,80}(20\d\d|N/A)", t)
    if not year:
        year = re.search(r"Dernier bilan[^0-9N]{0,80}(20\d\d|N/A)", t)
    nums = re.findall(r"/en/(0\d{9})", t) + re.findall(r"/nl/(0\d{9})", t) + re.findall(r"BE0(\d{9})", t)
    nums = list(dict.fromkeys([n[-10:] if len(n) >= 10 else n for n in nums]))
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
    y = year.group(1) if year else "-"
    ok = y in ("2025", "2026") and bool(free) and bool(y25)
    print(
        ("HIT" if ok else "skip"),
        label,
        (title.group(1)[:45] if title else "?"),
        "Y",
        y,
        y25,
        "fte",
        fte.group(1) if fte else "-",
        "FREE",
        free[:2],
    )
    return ok


# Candidates: Zilverlinde mined; try unused care KBOs from directories / news
CANDS = [
    ("0445175263", "zilverlinde"),  # likely mined
    ("0450755634", "residentie_oudenburg"),  # RE intermediation - skip if not care
    ("0480566704", "hof_ter_lande"),  # YE2024
    # Walloon / other
    ("0428080497", "maison_dieu"),  # mined
    ("0413203073", "cwzc"),  # YE2024 mined
    # Try more from repertorium Vlaams-Brabant sample
    ("0400000000", "x"),
]

# Named fetches with known care KBOs that may be unused
MORE = [
    "https://www.companyweb.be/en/0445175263",  # zilverlinde
    "https://www.companyweb.be/en/0450755634",  # residentie
    "https://www.companyweb.be/en/0480566704",  # hof
    # Try disability / creche / psych unused
    "https://www.companyweb.be/en/0417.000.000",
]

# Concrete unused-looking from public lists
for kbo, label in [
    ("0445175263", "zilverlinde"),
    ("0450755634", "residentie"),
    ("0480566704", "hof"),
    # From earlier Apricusa / Hestia - try find KBOs
    ("0755822317", "lork_hoeselt_bv"),  # YE2024 shell
    # Try WZC names
    ("0417550123", "bad"),
    ("0428556789", "bad2"),
    # Real: Ter Meeren is under WZND - skip
    # Try: Vondelhof Boutersem / Vulpia - vulpia mined
    # Try Salvator - YE2024
    ("0423571581", "salvator"),
    # Try Christelijke WZC - YE2024
    ("0413203073", "cwzc"),
    # Fresh: search Oosterzonne / Berkenbos as separate entities?
    ("0401234567", "x"),
]:
    digits = re.sub(r"\D", "", kbo)
    if digits in mined:
        print("MINED", label, digits)
        continue
    t = fetch(f"https://www.companyweb.be/en/{digits}", out / f"{label}_en.html")
    if t:
        summarize(label, t)

# Also try a few disability / MPC / hospital public
for kbo, label in [
    ("0475.400.760", "famifamenne"),  # mined armonea path
    ("0448.033.201", "chateau_vert"),  # mined
    ("0415.850.084", "mpc"),  # mined
]:
    digits = re.sub(r"\D", "", kbo)
    print("check", label, "mined" if digits in mined else "free")

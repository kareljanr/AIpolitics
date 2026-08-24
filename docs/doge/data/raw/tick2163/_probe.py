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
        print("FAIL", path.name, type(e).__name__, str(e)[:70])
        return None


def summarize(label, t):
    title = re.search(r"<title>([^<]+)", t)
    year = re.search(r"Last balance sheet year[^0-9N]{0,80}(20\d\d|N/A)", t)
    if not year:
        year = re.search(r"Laatste balansjaar[^0-9N]{0,80}(20\d\d|N/A)", t)
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
        (title.group(1)[:48] if title else "?"),
        "Y",
        y,
        y25,
        "fte",
        fte.group(1) if fte else "-",
        "FREE",
        free[:2],
    )
    return ok


# Prefer path
for kbo, label in [
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    ("0755822317", "lork_hoeselt"),  # YE2025 empty omzet NEG equity optional
    ("0480566704", "hof_ter_lande"),  # YE2024
]:
    digits = re.sub(r"\D", "", kbo)
    if digits in mined:
        print("MINED", label)
        continue
    t = fetch(f"https://www.companyweb.be/en/{digits}", out / f"{label}_en.html")
    if t:
        summarize(label, t)

# More unused care candidates
for kbo, label in [
    ("0412886636", "boterlaar_check"),  # should be mined
    ("0429.123.456", "bad"),
    # Try Zorgfamilie siblings / Antwerp belt
    ("0460.111.222", "bad2"),
    ("0438.765.432", "bad3"),
    # Real candidates from directories
    ("0405.311.530", "elisabeth_zee"),  # maybe mined
    ("0417.958.152", "camillus"),  # maybe mined
    ("0445.175.263", "zilverlinde"),  # mined
    ("0428.080.497", "maison_dieu"),  # mined
    # Fresh Walloon / VL
    ("0466.961.859", "buissons"),  # mined
    ("0479.984.011", "peupliers"),  # mined
    # Try new
    ("0408.123.789", "x"),
    ("0441.567.890", "y"),
    ("0455.234.567", "z"),
    ("0462.316.153", "castel"),  # mined residence le castel?
    ("0459.540.765", "rsw"),  # mined
    ("0475.400.760", "famifamenne"),  # mined
]:
    digits = re.sub(r"\D", "", kbo)
    if digits in mined:
        print("MINED", label)
        continue
    t = fetch(f"https://www.companyweb.be/en/{digits}", out / f"{label}_en.html")
    if t:
        summarize(label, t)

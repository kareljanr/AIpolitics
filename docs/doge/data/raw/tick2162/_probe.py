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
    nums = re.findall(r"/en/(0\d{9})", t) + re.findall(r"BE0(\d{9})", t)
    nums = list(dict.fromkeys([n[-10:] if len(n) >= 10 else n for n in nums]))
    y25 = None
    yy = None
    for y, body in re.findall(r'(20\d\d)\s*:\s*\{([^{}]+)\}', t):
        if y in ("2025", "2026"):
            yy = y

            def g(k, b=body):
                m = re.search(rf'{k}:\s*"([^"]*)"', b)
                return m.group(1) if m else None

            y25 = {k: g(k) for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]}
            break
    fte = re.search(r"(\d[\d.,]*)\s*FTE", t)
    free = [n for n in nums if n not in mined]
    y = year.group(1) if year else "-"
    print(
        label,
        (title.group(1)[:50] if title else "?"),
        "Y",
        y,
        "ye",
        yy,
        y25,
        "fte",
        fte.group(1) if fte else "-",
        "FREE",
        free[:2],
    )
    return y in ("2025", "2026") and bool(free) and bool(y25)


# Prefer path + prior tick2160 probes
CANDS = [
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
    # Hof ter Lande from tick2160 raw
    ("0400000000", "skip"),
]

# Parse prior hof_ter_lande / other FREE from tick2160
prior = Path(r"docs/doge/data/raw/tick2160")
for name in ["hof_ter_lande_en.html", "hof_ter_lande_nl.html", "aiesh_en_full.html", "faro_en.html" if False else ""]:
    p = prior / name
    if name and p.exists():
        summarize(name, p.read_text(encoding="utf-8", errors="ignore"))

# Discover Hof ter Lande KBO from prior HTML
p = prior / "hof_ter_lande_en.html"
if p.exists():
    t = p.read_text(encoding="utf-8", errors="ignore")
    nums = re.findall(r"BE0?(\d{9,10})", t) + re.findall(r"/en/(0\d{9})", t)
    print("hof nums", nums[:5])

# Fresh fetches
for kbo, label in [
    ("0893863017", "faro"),
    ("0201712587", "aiesh"),
    ("0644638937", "rew"),
]:
    if kbo in mined and label != "faro":
        # still check year
        pass
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_en.html")
    if t:
        summarize(label, t)

# Try Hof ter Lande via companyweb slug search from prior files
for name in ["hof_ter_lande_kbo.html", "hof_ter_lande_kbo.txt"]:
    p = prior / name
    if p.exists():
        t = p.read_text(encoding="utf-8", errors="ignore")
        print("===", name, "len", len(t))
        m = re.search(r"0\d{3}[.\s]?\d{3}[.\s]?\d{3}", t)
        print("kbo?", m.group(0) if m else None)
        print(t[:400])

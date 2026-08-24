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
root = Path(r"C:\Users\karel\dev\AIpolitics")

mined = set()
with open(root / "docs/doge/data/entities.csv", newline="", encoding="utf-8") as f:
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
        print("FAIL", path.name, type(e).__name__, str(e)[:60])
        return None


def parse(label, kbo, t):
    title = re.search(r"<title>([^<]+)", t)
    year = re.search(r"Last balance sheet year[^0-9N]{0,80}(20\d\d|N/A)", t)
    if not year:
        year = re.search(r"Laatste balansjaar[^0-9N]{0,80}(20\d\d|N/A)", t)
    rows = {}
    for y, body in re.findall(r"(20\d\d)\s*:\s*\{([^{}]+)\}", t):
        if y >= "2023":

            def g(k, b=body):
                m = re.search(rf'{k}:\s*"([^"]*)"', b)
                return m.group(1) if m else None

            rows[y] = {
                k: g(k)
                for k in ["omzet", "winst", "bruto_marge", "eigen_vermogen"]
            }
    fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t)
    filed = re.search(r"filed on ([0-9-]{10})", t)
    free = kbo not in mined
    print(
        "===",
        label,
        kbo,
        "FREE" if free else "MINED",
        (title.group(1)[:50] if title else "?"),
        "Y",
        year.group(1) if year else "-",
        "fte",
        fte.group(1) if fte else "-",
        "filed",
        filed.group(1) if filed else "-",
    )
    for y in sorted(rows):
        if y >= "2024":
            print(" ", y, rows[y])
    return free and (year.group(1) if year else "") in ("2025", "2026") and bool(rows)


cands = [
    ("0411600692", "marias_rustoord"),
    ("0428692191", "de_medemens"),
    ("0418016550", "st_vincentius"),
    ("0409724238", "heilig_hart_grimbergen"),
    ("0410142031", "olv_lourdes"),
    ("0412886636", "boterlaarhof"),
    ("0422152314", "sint_barbara"),
    ("0644984078", "zilverbos"),
    ("0445106274", "sint_bernardus"),
    ("0424830108", "stuyvenberg"),
    ("0823488131", "thofke"),
    ("0409970203", "sint_carolus"),  # likely mined Ternat
    ("0413055989", "sint_jozef_rillaar"),  # likely mined
    ("0456528719", "skip_bad"),
]

hits = []
for kbo, label in cands:
    t = fetch(f"https://www.companyweb.be/en/{kbo}", out / f"{label}_en.html")
    if t and parse(label, kbo, t):
        hits.append(label)
print("HIT_LABELS", hits)

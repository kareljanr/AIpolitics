import re
from pathlib import Path
from collections import Counter

base = Path(r"docs/doge/data/raw/tick2075")
for fname in ["kuurne_en.html", "kuurne_nl.html"]:
    t = (base / fname).read_text(encoding="utf-8", errors="replace")
    print("====", fname)
    cats = re.findall(r"categories:\s*(\[[^\]]+\])", t)
    print("categories", cats[:5])
    series = re.findall(r"name:\s*'([^']+)'[^}]{0,300}data:\s*(\[[^\]]+\])", t)
    print("series", len(series))
    for n, d in series[:20]:
        print(" ", n, "=>", d[:160])
    # numeric fields
    for key in ["omzet", "winst", "bruto_marge", "eigen_vermogen", "fte"]:
        vals = re.findall(rf'{key}:\s*"([^"]+)"', t)
        print(key, vals[:6])
    # also double-quoted name series
    series2 = re.findall(r'name:\s*"([^"]+)"[^}]{0,300}data:\s*(\[[^\]]+\])', t)
    print("series2", len(series2))
    for n, d in series2[:20]:
        print(" ", n, "=>", d[:160])
    # equity English
    for key in ["equity", "gross_margin", "profit", "turnover", "workforce", "employees"]:
        vals = re.findall(rf'{key}[^:]*:\s*"([^"]+)"', t, re.I)
        if vals:
            print("alt", key, vals[:6])

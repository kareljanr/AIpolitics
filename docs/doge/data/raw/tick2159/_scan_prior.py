# -*- coding: utf-8 -*-
from pathlib import Path
import re
import csv

csv.field_size_limit(10**7)

# Parse prior probe HTMLs for YE2025 care entities
roots = [
    Path(r"docs/doge/data/raw/tick2153"),
    Path(r"docs/doge/data/raw/tick2144"),
    Path(r"docs/doge/data/raw/tick2151"),
]

mined = set()
with open(Path(r"docs/doge/data/entities.csv"), newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        blob = " ".join(str(v) for v in row.values())
        for m in re.findall(r"0\d{9}", re.sub(r"[.\s]", "", blob)):
            mined.add(m)
        for m in re.findall(r"0\d{3}\.\d{3}\.\d{3}", blob):
            mined.add(re.sub(r"\D", "", m))

print("mined", len(mined))

for root in roots:
    if not root.exists():
        continue
    for f in sorted(root.glob("*.html")):
        t = f.read_text(encoding="utf-8", errors="ignore")
        title = re.search(r"<title>([^<]+)", t)
        year = re.search(r"Last balance sheet year[^0-9N]{0,80}(20\d\d|N/A)", t)
        if not year:
            year = re.search(r"Laatste balansjaar[^0-9N]{0,80}(20\d\d|N/A)", t)
        y = year.group(1) if year else "-"
        if y != "2025" and y != "2026":
            continue
        nums = re.findall(r"BE0?(\d{9,10})", t)
        nums += re.findall(r"/en/(0\d{9})", t)
        nums = [n[-10:] if len(n) > 10 else n for n in nums]
        nums = list(dict.fromkeys(nums))
        objs = re.findall(r'(20\d\d)\s*:\s*\{([^{}]+)\}', t)
        omzet = winst = None
        for yy, body in objs:
            if yy in ("2025", "2026"):
                m = re.search(r'omzet:\s*"([^"]*)"', body)
                w = re.search(r'winst:\s*"([^"]*)"', body)
                omzet = m.group(1) if m else None
                winst = w.group(1) if w else None
                break
        status = []
        for n in nums[:3]:
            status.append(f"{n}:{'MINED' if n in mined else 'FREE'}")
        print(
            f.name,
            (title.group(1)[:50] if title else "?"),
            "Y",
            y,
            "omzet",
            omzet,
            "winst",
            winst,
            status,
        )

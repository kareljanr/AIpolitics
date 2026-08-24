# -*- coding: utf-8 -*-
import csv
import re
import shutil
from pathlib import Path

csv.field_size_limit(10**7)
src = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2146")
dst = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2147")
dst.mkdir(parents=True, exist_ok=True)
for name in [
    "hesbaye_en.html",
    "hesbaye_nl.html",
    "hesbaye_fr.html",
    "hesbaye_kbo.html",
]:
    p = src / name
    if p.exists():
        shutil.copy2(p, dst / name)

kbo = (dst / "hesbaye_kbo.html").read_text(encoding="utf-8", errors="replace")
text = re.sub(r"<[^>]+>", "\n", kbo)
lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
for i, ln in enumerate(lines):
    if any(
        k in ln.lower()
        for k in [
            "status",
            "actief",
            "adres",
            "nace",
            "hannut",
            "vestiging",
            "naam",
            "rechtsvorm",
            "email",
            "web",
            "hesbaye",
            "84.250",
            "aanbested",
        ]
    ):
        print("KBO", " | ".join(lines[i : i + 3])[:230])

en = (dst / "hesbaye_en.html").read_text(encoding="utf-8", errors="replace")
m = re.search(r'Employees\s*=\s*"([^"]+)"', en)
print("fte", m.group(1) if m else None)
m = re.search(r'window\.cw\.startDate\s*=\s*"([^"]+)"', en)
print("start", m.group(1) if m else None)
print("title", re.search(r"<title>([^<]+)", en).group(1)[:100])

ents = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\entities.csv").read_text(
    encoding="utf-8", errors="replace"
).lower()
print(
    "mined",
    "0500.916.512" in ents
    or "0500916512" in ents
    or "zs_hesbaye" in ents
    or "hesbaye" in ents,
)

with open(
    r"C:\Users\karel\dev\AIpolitics\docs\doge\data\research_queue.csv",
    encoding="utf-8",
    newline="",
) as f:
    rows = list(csv.DictReader(f))
for x in rows:
    if x.get("task_id") == "rq_2147":
        print("2147", x.get("status"))

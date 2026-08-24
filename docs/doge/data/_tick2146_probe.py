# -*- coding: utf-8 -*-
import csv
import re
import shutil
from pathlib import Path

csv.field_size_limit(10**7)
ents = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\entities.csv").read_text(
    encoding="utf-8", errors="replace"
).lower()
src2144 = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2144")
src2145 = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2145")
dst = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2146")
dst.mkdir(parents=True, exist_ok=True)

for name in [
    "zonnelied_en.html",
    "zonnelied_nl.html",
    "zonnelied_fr.html",
    "zonnelied_kbo.html",
    "zonnelied_site.html",
    "rew_en.html",
    "hesbaye_en.html",
    "hesbaye_nl.html",
    "hesbaye_fr.html",
    "hesbaye_kbo.html",
]:
    p = src2144 / name if (src2144 / name).exists() else src2145 / name
    if not p.exists():
        print("MISSING", name)
        continue
    shutil.copy2(p, dst / name)
    t = p.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)", t)
    years = re.findall(r"\n(202[0-9])\s*:", t)
    print("===", name, "years", years[:6])
    print(" title", title.group(1)[:110] if title else None)
    for y in ["2025", "2024"]:
        mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", t)
        if mm:
            print(" ", y, re.sub(r"\s+", " ", mm.group(1))[:300])
    m = re.search(r'Employees\s*=\s*"([^"]+)"', t)
    if m:
        print(" fte", m.group(1))
    m = re.search(r"BE(\d{10})", title.group(1) if title else "")
    if m:
        k = m.group(1)
        print(" mined", k in ents.replace(".", ""), k)

print("zonnelied in ents", "zonnelied" in ents)
print(
    "hesbaye in ents",
    "hesbaye" in ents or "0500916512" in ents or "0500.916.512" in ents,
)

with open(
    r"C:\Users\karel\dev\AIpolitics\docs\doge\data\research_queue.csv",
    encoding="utf-8",
    newline="",
) as f:
    rows = list(csv.DictReader(f))
for x in rows:
    if x.get("task_id") == "rq_2146":
        print("2146", x.get("status"))

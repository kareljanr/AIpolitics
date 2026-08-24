# -*- coding: utf-8 -*-
import csv
import re
from pathlib import Path

csv.field_size_limit(10**7)
base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2139")
for name in ["moisson_en.html", "bornem_en.html", "faro_en.html", "aiesh_en.html", "rew_en.html"]:
    t = (base / name).read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    years = re.findall(r"\n(202[0-9])\s*:", t)
    print("===", name, "years", years[:6], "title", title.group(1)[:90] if title else None)
    for y in ["2025", "2024"]:
        mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", t)
        if mm:
            print(" ", y, re.sub(r"\s+", " ", mm.group(1))[:300])

# already mined?
data = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
needles = [
    "0413.796.456",
    "0413796456",
    "de foyer",
    "0436.595.020",
    "0436595020",
    "seniorencentrum onze lieve",
    "0434.384.014",
    "0434384014",
    "la moisson",
]
for fn in ["entities.csv", "leaderboard.csv", "sources.csv"]:
    text = (data / fn).read_text(encoding="utf-8", errors="replace").lower()
    for n in needles:
        if n.lower() in text:
            print("HIT", fn, n)

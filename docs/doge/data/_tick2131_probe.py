# -*- coding: utf-8 -*-
import re
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2131")
for name in [
    "bornem_en.html",
    "faro_en.html",
    "aiesh_en.html",
    "rew_en.html",
    "orchidee_search.html",
]:
    p = base / name
    if not p.exists():
        print(name, "MISSING")
        continue
    t = p.read_text(encoding="utf-8", errors="replace")
    years = re.findall(r"\n(202[0-9])\s*:", t)
    print(name, "years", years[:8])
    for y in ["2025", "2024"]:
        mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", t)
        if mm:
            print(" ", y, re.sub(r"\s+", " ", mm.group(1))[:280])
    if "search" in name:
        for m in re.finditer(r"/en/(\d{10})/([a-z0-9\-]+)", t):
            slug = m.group(2)
            if "orchid" in slug or "orchide" in slug:
                print(" link", m.group(0))
        for m in re.finditer(r"Orchid.{0,100}", t, re.I):
            print(" hit", re.sub(r"\s+", " ", m.group(0))[:140])

# -*- coding: utf-8 -*-
import re
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw")
# check both tick2137 prestige and tick2138
paths = []
for d in ["tick2138", "tick2137"]:
    p = base / d
    if p.exists():
        paths.extend(sorted(p.glob("*prestige*")))
        paths.extend(sorted(p.glob("*bornem*")))
        paths.extend(sorted(p.glob("*faro*")))
        paths.extend(sorted(p.glob("*aiesh*")))
        paths.extend(sorted(p.glob("*rew*")))

seen = set()
for p in paths:
    if p.name in seen:
        continue
    seen.add(p.name)
    t = p.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    years = re.findall(r"\n(202[0-9])\s*:", t)
    print("===", p.parent.name + "/" + p.name, "len", len(t))
    print(" title:", title.group(1)[:120] if title else None)
    print(" years:", years[:8])
    for y in ["2025", "2024"]:
        mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", t)
        if mm:
            print(" ", y, re.sub(r"\s+", " ", mm.group(1))[:320])
    for pat in [
        r'Employees\s*=\s*"([^"]+)"',
        r"filed on ([0-9\-]+)",
        r'rel="canonical" href="([^"]+)"',
        r"Principal activity[^<]{0,120}",
    ]:
        m = re.search(pat, t, re.I)
        if m:
            print(" ", re.sub(r"\s+", " ", m.group(0))[:180])

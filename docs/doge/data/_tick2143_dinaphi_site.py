# -*- coding: utf-8 -*-
import re
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2143")
for name in ["dinaphi_site.html", "dinaphi_dinaphi.html"]:
    p = base / name
    if not p.exists():
        print(name, "missing")
        continue
    t = p.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)", t)
    print(name, "len", len(t), "title", title.group(1)[:80] if title else None)
    for m in re.finditer(r'href="([^"]+\.pdf)"', t, re.I):
        print(" pdf", m.group(1)[:160])
    for m in re.finditer(
        r"(budget|jaarrekening|comptes|dotation|million|€|EUR).{0,80}", t, re.I
    ):
        print(" hit", re.sub(r"\s+", " ", m.group(0))[:140])
    for m in re.finditer(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t):
        print(" email", m.group(0))

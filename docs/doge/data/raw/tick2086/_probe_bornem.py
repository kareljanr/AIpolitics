# -*- coding: utf-8 -*-
import re
from pathlib import Path

t = Path("docs/doge/data/raw/tick2086/bornem_jr.html").read_text(encoding="utf-8", errors="replace")
for m in re.finditer(r'href="([^"]+)"[^>]*>([^<]{0,120})', t, re.I):
    href, txt = m.group(1), m.group(2)
    blob = (href + " " + txt).lower()
    if any(k in blob for k in ["jaarrekening", "agb", "2025", "pdf", "bbc"]):
        print(txt.strip()[:80], "->", href[:140])
print("--- snippets ---")
for m in re.finditer(r"(jaarrekening[^<\n]{0,80}|AGB[^<\n]{0,60})", t, re.I):
    s = re.sub(r"\s+", " ", m.group(0))[:120]
    print(s)

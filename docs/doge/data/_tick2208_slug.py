# -*- coding: utf-8 -*-
import re
from pathlib import Path

for name in ["arcor_en.html", "noordheuvel_en.html"]:
    p = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2207") / name
    t = p.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"companyweb\.be/(?:en|nl|fr)/(\d+)/([^\"'?\s]+)", t)
    print(name, m.groups() if m else None)
    title = re.search(r"<title>([^<]+)", t, re.I)
    print(" title", title.group(1)[:120] if title else None)

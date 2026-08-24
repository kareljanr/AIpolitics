# -*- coding: utf-8 -*-
import re
from pathlib import Path

for name in ["faro_en.html", "aiesh_en.html", "rew_en.html", "bornem_en.html"]:
    html = (Path("docs/doge/data/raw/tick2131") / name).read_text(
        encoding="utf-8", errors="replace"
    )
    years = re.findall(r"(202[0-9])\s*:\s*\{\s*winst", html)
    print(name, "year keys", years[:12])
    m = re.search(r"<title>([^<]+)", html)
    print(" title", m.group(1) if m else None)
    for label in [
        "Last balance sheet year",
        "lastJaar",
        "Employees =",
        "turnover of €",
        "Profit/Loss",
    ]:
        i = html.lower().find(label.lower())
        if i >= 0:
            snippet = html[i : i + 160].replace("\n", " ")
            print(" ", label, "->", snippet[:160])

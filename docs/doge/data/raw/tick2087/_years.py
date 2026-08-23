# -*- coding: utf-8 -*-
import re
from pathlib import Path

te = Path("docs/doge/data/raw/tick2087/lindelo_en.html").read_text(encoding="utf-8", errors="replace")
# find thead years in financial table
m = re.search(r"<thead>[\s\S]{0,800}?</thead>", te)
print("first thead", re.sub(r"\s+", " ", m.group(0)) if m else "none")
# all year headers near Turnover
idx = te.find("Turnover")
print("around turnover header", re.sub(r"\s+", " ", te[idx - 500 : idx + 200])[:700])
idx2 = te.find("Employees")
print("years before employees section:")
print(re.findall(r">\s*(20\d\d)\s*<", te[max(0, idx2 - 2500) : idx2]))

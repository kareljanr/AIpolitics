# -*- coding: utf-8 -*-
import re
from pathlib import Path
for lang in ["en","nl","fr"]:
    t=Path(f"docs/doge/data/raw/tick2143/careion_cw_{lang}.html").read_text(encoding="utf-8",errors="replace")
    m=re.search(r'Employees\s*=\s*"([^"]+)"', t)
    print(lang, "Employees=", m.group(1) if m else None)
    # try personnel in year blocks - sometimes separate
    # look near "924" and "873"
    for n in ["873,8","873.8","924,9","924.9","1712"]:
        print(" ", n, t.count(n))

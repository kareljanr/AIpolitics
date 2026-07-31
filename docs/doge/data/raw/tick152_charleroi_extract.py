# -*- coding: utf-8 -*-
"""Extract named L5 lines from Charleroi BI2026 ordinary cahier."""
from pypdf import PdfReader
import re
from pathlib import Path

PDF = Path("docs/doge/data/raw/charleroi_cahier_ord_2026.pdf")
r = PdfReader(str(PDF))

# dump key pages raw
for i in [20, 21, 22, 100, 101, 104, 105, 202, 203, 232, 233, 234, 235]:
    t = " ".join((r.pages[i].extract_text() or "").split())
    out = Path(f"docs/doge/data/raw/charl_key_p{i+1}.txt")
    out.write_text(t, encoding="utf-8")
    # large amounts
    for m in re.finditer(
        r"(\d[\d\.]*,\d{2})\s+(\d[\d\.]*,\d{2})\s+(\d[\d\.]*,\d{2})\s+(\d[\d\.]*,\d{2})",
        t,
    ):
        vals = [float(m.group(j).replace(".", "").replace(",", ".")) for j in range(1, 5)]
        if vals[3] < 200_000:
            continue
        start = max(0, m.start() - 90)
        ctx = t[start : m.start()].strip()[-90:]
        print(f"P{i+1}|ctx={ctx}|BI2026={vals[3]:.0f}|BI2025={vals[1]:.0f}|2024={vals[0]:.0f}")

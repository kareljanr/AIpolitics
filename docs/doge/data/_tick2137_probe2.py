# -*- coding: utf-8 -*-
from pathlib import Path
import re

base = Path("docs/doge/data/raw/tick2137")
for name in [
    "faro_cw_en.html",
    "aiesh_cw_en.html",
    "corolles_cw_en.html",
    "corolles_cw_nl.html",
]:
    html = (base / name).read_text(encoding="utf-8", errors="replace")
    m = re.search(
        r"Last balance sheet year\s*</div>\s*<div[^>]*>\s*(\d{4})", html
    )
    m2 = re.search(r"Laatste balansjaar\s*</div>\s*<div[^>]*>\s*(\d{4})", html)
    fte = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
    filed = re.search(r"filed on ([0-9-]{10})", html) or re.search(
        r"neergelegd op ([0-9-]{10})", html
    )
    bal = (m or m2).group(1) if (m or m2) else "?"
    print(
        name,
        "balance",
        bal,
        "fte",
        fte.group(1) if fte else "?",
        "filed",
        filed.group(1) if filed else "?",
    )

html = (base / "corolles_cw_en.html").read_text(encoding="utf-8", errors="replace")
for year in ("2025", "2024"):
    m = re.search(rf"{year}\s*:{{([^}}]+)}}", html)
    print(year, m.group(1).strip() if m else None)

# prior FTE unknown OK
print("yoy calc:")
o25, o24 = 9741365, 9385583
b25, b24 = 10263326, 9813565
p25, p24 = 467552, 424611
e25, e24 = 9934798, 9613283


def yoy(a, b):
    return f"{(a - b) / b * 100:+.2f}%"


print("omzet", yoy(o25, o24), "bruto", yoy(b25, b24), "pnl", yoy(p25, p24), "eq", yoy(e25, e24))
# pi rough: size ~9.7m → cost_score ~5.5; absurdity merger absorptions + public MRS ~6.5; difficulty 3
# pi = 0.55*6.5 + 0.35*5.5 + 0.10*(11-3) = 3.575+1.925+0.8 = 6.3
print("pi~6.3")

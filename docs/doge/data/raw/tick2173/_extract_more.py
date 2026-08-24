# -*- coding: utf-8 -*-
import re
from pathlib import Path

t = Path("docs/doge/data/raw/tick2173/langerheide_en.html").read_text(
    encoding="utf-8", errors="ignore"
)
# FTE series if present
for m in re.finditer(r"FTE[^<{]{0,40}|Employees[^<{]{0,80}|Personnel[^<{]{0,80}", t, re.I):
    print("FTECTX", m.group(0)[:100])
# look for year FTE pairs in JS
for m in re.finditer(r"fte[^:]*:\s*[\"']?([\d.,]+)", t, re.I):
    print("fteval", m.group(1))
# address / website / phone snippets
for pat in [
    r"www\.[a-zA-Z0-9.\-/]+",
    r"Langerheide[^<{]{0,80}",
    r"Haacht[^<{]{0,40}",
    r"\+32[^<{]{0,30}",
    r"0\d[\d/\s.]{6,}",
]:
    ms = re.findall(pat, t)
    if ms:
        print(pat, "->", list(dict.fromkeys(ms))[:8])

# YoY calcs
om25, om24 = 1842966, 1873019
br25, br24 = 3143509, 3089043
pnl25, pnl24 = 106076, 66122
eq25, eq24 = 931790, 825714
print("omzet pct", round((om25 - om24) / om24 * 100, 2))
print("bruto pct", round((br25 - br24) / br24 * 100, 2))
print("pnl pct", round((pnl25 - pnl24) / pnl24 * 100, 2))
print("equity pct", round((eq25 - eq24) / eq24 * 100, 2))

# pi heuristic: modest care WZC ~1.8m omzet, pnl JUMP, thin equity vs bruto
# cost_score ~4.0 (small), absurdity ~4.5 (public ROB opacity assets), difficulty 3.0
# pi = 0.55*4.0 + 0.35*4.5 + 0.10*5.0 = 2.2+1.575+0.5 = 4.275 ≈ 4.3
print("suggested pi ~4.3")

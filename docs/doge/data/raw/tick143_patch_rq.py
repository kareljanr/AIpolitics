# -*- coding: utf-8 -*-
from pathlib import Path

p = Path("docs/doge/data/research_queue.csv")
text = p.read_text(encoding="utf-8")
old = (
    'rq_118,IEFH Institute women-men funding map,continuous,6,open,L2,iefh,'
    '"Parallel Unia method: federal Institute for Equality of Women and Men budget 2024-2026 primary.",'
    ",2026-07-27T12:00:00Z,2026-07-27T12:00:00Z,Equality dual architecture next after Unia"
)
new = (
    'rq_118,IEFH Institute women-men funding map,continuous,6,done,L2,iefh,'
    '"Parallel Unia method: federal Institute for Equality of Women and Men budget 2024-2026 primary.",'
    "gap_iefh_funding_detail,2026-07-27T12:00:00Z,2026-07-27T21:10:00Z,"
    '"tick143: RA2024 strong exp 24.8m CPVS 10.9m dotation 33.9m protocols 223k Flanders0 FOI residual"'
)
if old not in text:
    raise SystemExit("OLD NOT FOUND")
p.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")
print("OK")

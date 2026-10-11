# -*- coding: utf-8 -*-
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/loop_state.csv")
text = p.read_text(encoding="utf-8")
lines = text.splitlines()
header = lines[0]
row = "main,continuous,hole_fill,2026-08-19T06:40:00Z,rq_1403,1403,no,tick1403 VERKO leftover waste IGS residual; KBO 0218.426.974; live JR2025 NBB WVV PDF; sourced euros assets 38416495 omzet 26146600 diensten 12448633 pers 11760008 debt 28727165 voorzieningen 5233600 pnl 6578 equity 4455729 cash 3529851 capex 2165409; FOI ready omzet 26.15m / diensten 12.45m / debt 28.73m / commissaris fee unpublished; next rq_1404 residual dual L5 VL; continuous hole_fill"
p.write_text(header + "\n" + row + "\n", encoding="utf-8")
print("loop_state ok")

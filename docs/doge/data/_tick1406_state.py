# -*- coding: utf-8 -*-
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/loop_state.csv")
text = p.read_text(encoding="utf-8")
lines = text.splitlines()
header = lines[0]
row = "main,continuous,hole_fill,2026-08-19T07:30:00Z,rq_1406,1406,no,tick1406 MLSO leftover IGS residual; KBO 0223.944.690; live JR2025 NBB WVV PDF; sourced euros assets 227277417 omzet 24044090 diensten 7752488 interwaas 3762956 nrec 4415758 debt 13594288 pnl 7699101 equity 213683129 cash 24924839 capex 259767 dividend 2910456; FOI ready diensten split / Interwaas 3.76m / nrec 4.42m / vennoten unpublished; next rq_1407 residual dual L5 VL; continuous hole_fill"
p.write_text(header + "\n" + row + "\n", encoding="utf-8")
print("loop_state ok")

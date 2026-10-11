# -*- coding: utf-8 -*-
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/loop_state.csv")
text = p.read_text(encoding="utf-8")
lines = text.splitlines()
header = lines[0]
row = "main,continuous,hole_fill,2026-08-19T06:15:00Z,rq_1402,1402,no,tick1402 DDS leftover streek IGS residual; KBO 0207.087.872; live JR2025 NBB WVV PDF; sourced euros assets 48501395 omzet 1262519 othops 5219038 diensten 1359141 pers 3875923 inventory 12793375 voorzieningen 7847265 pnl -287310 equity 38109541 cash 5533236 capex 789825; FOI ready othops 5.22m / inventory 12.79m / voorzieningen 7.85m / commissaris fee unpublished; next rq_1403 residual dual L5 VL; continuous hole_fill"
p.write_text(header + "\n" + row + "\n", encoding="utf-8")
print("loop_state ok")

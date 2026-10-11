# -*- coding: utf-8 -*-
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/loop_state.csv")
text = p.read_text(encoding="utf-8")
lines = text.splitlines()
header = lines[0]
row = "main,continuous,hole_fill,2026-08-19T06:50:00Z,rq_1404,1404,no,tick1404 Psilon leftover crematorium IGS residual; KBO 0874.649.790; live JR2025 NBB WVV PDF; sourced euros assets 8627377 brutomarge 1935397 pers 877307 debt 2186709 pnl 498832 equity 6113421 cash 776217 capex 170092; FOI ready omzet empty / diensten unpublished / debt 2.19m / vennoten 6.20m guarantee; next rq_1405 residual dual L5 VL; continuous hole_fill"
p.write_text(header + "\n" + row + "\n", encoding="utf-8")
print("loop_state ok")

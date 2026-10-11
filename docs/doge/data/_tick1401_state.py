# -*- coding: utf-8 -*-
import csv
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/loop_state.csv")
UTC = "2026-08-19T05:50:00Z"
fields = ["state_id","mode","current_sprint","last_tick_utc","last_unit_id","ticks_completed","paused","notes"]
with p.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\r\n")
    w.writeheader()
    w.writerow({
        "state_id": "main",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1401",
        "ticks_completed": "1401",
        "paused": "no",
        "notes": "tick1401 OVCO leftover crematorium IGS residual; KBO 0845.064.493; live JR2025 NBB WVV PDF; sourced euros assets 9368744 brutomarge 1163024 pers 459819 debt 6313967 pnl 385548 equity 3054777 cash 83941 invest 973616 cip 975949 capsub 1743380; FOI ready omzet empty / 6.31m debt / 0.98m CIP / vennoten unpublished; next rq_1402 residual dual L5 VL; continuous hole_fill",
    })
print("loop_state ok")

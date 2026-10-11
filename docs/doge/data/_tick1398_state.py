# -*- coding: utf-8 -*-
import csv
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/loop_state.csv")
UTC = "2026-08-19T05:05:00Z"
fields = ["state_id","mode","current_sprint","last_tick_utc","last_unit_id","ticks_completed","paused","notes"]
with p.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\r\n")
    w.writeheader()
    w.writerow({
        "state_id": "main",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1398",
        "ticks_completed": "1398",
        "paused": "no",
        "notes": "tick1398 IGS IBEG leftover IGS energy holding residual; KBO 0202.082.078; live JR2025 NBB WVV PDF; sourced euros assets 100488193 omzet empty diensten 809703 debt 1450184 pnl 1283311 equity 99038008 div 3500000 fva 96372430; FOI ready omzet-empty/3.50m dividend/96.37m FVA/9.00m Fluvius HV loan; next rq_1399 residual dual L5 VL; continuous hole_fill",
    })
print("loop_state ok")

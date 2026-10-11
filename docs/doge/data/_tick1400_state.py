# -*- coding: utf-8 -*-
import csv
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/loop_state.csv")
UTC = "2026-08-19T05:40:00Z"
fields = ["state_id","mode","current_sprint","last_tick_utc","last_unit_id","ticks_completed","paused","notes"]
with p.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\r\n")
    w.writeheader()
    w.writerow({
        "state_id": "main",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1400",
        "ticks_completed": "1400",
        "paused": "no",
        "notes": "tick1400 IGL leftover zorg IGS residual + every-10; KBO 0201.310.929; live JR2025 NBB WVV PDF; sourced euros assets 65298610 omzet 48156858 pers 40508243 diensten 5366617 debt 31766387 pnl 2298043 equity 33288549 cash 5894254 invest 9500000 capsub 8217525; FOI ready VL 40.23m / 40.51m pers / 31.77m debt / vennoten unpublished; next rq_1401 residual dual L5 VL leftover OVCO; continuous hole_fill",
    })
print("loop_state ok")

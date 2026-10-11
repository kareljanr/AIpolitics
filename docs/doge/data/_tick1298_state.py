# -*- coding: utf-8 -*-
import csv
from pathlib import Path
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC="2026-08-17T13:20:00Z"
with (DATA/"loop_state.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["state_id","mode","current_sprint","last_tick_utc","last_unit_id","ticks_completed","paused","notes"])
    w.writeheader()
    w.writerow({
        "state_id":"main","mode":"continuous","current_sprint":"hole_fill",
        "last_tick_utc":UTC,"last_unit_id":"rq_1298","ticks_completed":"1298","paused":"no",
        "notes":"tick1298 Stad+OCMW Steenokkerzeel JR2025 GE residual; KBO 0206.561.993/0212.173.345; assets 95.073m fin debt 2.492m IGS reval 9.510m AFM -0.051m OCMW cum -1.428m NEG; FOI ready; next rq_1299 residual dual L5 VL; continuous hole_fill",
    })
print("loop_state ok")
log_src = DATA/"_tick1298_log.md"
txt = log_src.read_text(encoding="utf-8")
txt = txt.replace("budgets+36","budgets+40")
log_src.write_text(txt, encoding="utf-8")
log = ROOT/"loop_log.md"
entry = txt if txt.startswith("\n") else "\n"+txt
tail = log.read_text(encoding="utf-8")[-400:]
if "Tick 1298" in tail:
    print("loop_log already has 1298")
else:
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")

# -*- coding: utf-8 -*-
import csv
from pathlib import Path
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC="2026-08-17T12:50:00Z"
with (DATA/"loop_state.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["state_id","mode","current_sprint","last_tick_utc","last_unit_id","ticks_completed","paused","notes"])
    w.writeheader()
    w.writerow({
        "state_id":"main","mode":"continuous","current_sprint":"hole_fill",
        "last_tick_utc":UTC,"last_unit_id":"rq_1297","ticks_completed":"1297","paused":"no",
        "notes":"tick1297 Stad+OCMW Diepenbeek JR2025 GE residual; KBO 0207.465.974/0212.246.787; assets 190.496m fin debt 13.592m IGS reval 19.425m OCMW equity -0.708m NEG; FOI ready; next rq_1298 residual dual L5 VL; continuous hole_fill",
    })
print("loop_state ok")
# fix log budgets count then append
log_src = DATA/"_tick1297_log.md"
txt = log_src.read_text(encoding="utf-8")
txt = txt.replace("budgets+36","budgets+39")
log_src.write_text(txt, encoding="utf-8")
log = ROOT/"loop_log.md"
entry = txt if txt.startswith("\n") else "\n"+txt
# avoid double-append
tail = log.read_text(encoding="utf-8")[-400:]
if "Tick 1297" in tail:
    print("loop_log already has 1297")
else:
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")

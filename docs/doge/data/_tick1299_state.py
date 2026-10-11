# -*- coding: utf-8 -*-
import csv
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent
UTC="2026-08-17T13:50:00Z"
with (DATA/"loop_state.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["state_id","mode","current_sprint","last_tick_utc","last_unit_id","ticks_completed","paused","notes"])
    w.writeheader()
    w.writerow({
        "state_id":"main","mode":"continuous","current_sprint":"hole_fill",
        "last_tick_utc":UTC,"last_unit_id":"rq_1299","ticks_completed":"1299","paused":"no",
        "notes":"tick1299 AGB Kortenaken JR2025 Entity II residual; KBO 0535.811.469; assets 3.479m fin debt 3.281m leasing 3.216m city prijssub 0.157m gecorr AFM -0.209m; FOI ready; next rq_1300 residual dual L5 VL + every-10; continuous hole_fill",
    })
print("loop_state ok")
log = ROOT/"loop_log.md"
txt = (DATA/"_tick1299_log.md").read_text(encoding="utf-8")
entry = txt if txt.startswith("\n") else "\n"+txt
tail = log.read_text(encoding="utf-8")[-400:]
if "Tick 1299" in tail:
    print("loop_log already has 1299")
else:
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")

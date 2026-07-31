# tick 350 — progress@350 close queues
import csv
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T13:45:00Z"
unit = "rq_341"

rq_path = base / "research_queue.csv"
with open(rq_path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for r in rows:
    if r["task_id"] == "rq_341":
        r["status"] = "done"
        r["updated_utc"] = now
        r["notes"] = (
            "tick350: progress@350 coverage A-E + waste top10 stable fossil/cars/cheque/EIWT; "
            "spawn rq_342 hole-fill"
        )

rows.append(
    {
        "task_id": "rq_342",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.",
        "blocked_gap_id": "",
        "created_utc": now,
        "updated_utc": "",
        "notes": "Spawned tick350 after progress@350; rq_116 SWA deferred",
    }
)
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

with open(base / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    f.write(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    )
    f.write(
        f"main,continuous,hole_fill,{now},{unit},350,no,"
        "Scheduler 60s. Next prio5 rq_342; rq_116 SWA deferred. FOI ready. "
        "tick350 progress coverage % + waste top10.\n"
    )

print("queues OK")

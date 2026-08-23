import csv
from pathlib import Path

path = Path("docs/doge/data/research_queue.csv")
csv.field_size_limit(10**7)
with path.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row["task_id"] == "rq_2079":
        st = (row.get("status") or "").lower()
        if st not in ("open", "in_progress"):
            raise SystemExit(f"RACE status={row.get('status')}")
        row["status"] = "in_progress"
        row["updated_utc"] = "2026-08-25T00:45:00Z"
        row["notes"] = "CLAIM tick2079 probing AGB/FARO/AIESH/REW then unused WZC Vander Stokken"
with path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("claimed rq_2079")

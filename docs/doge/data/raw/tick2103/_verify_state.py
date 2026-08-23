import csv
from pathlib import Path

csv.field_size_limit(10**7)
print(Path("docs/doge/data/loop_state.csv").read_text(encoding="utf-8"))
with open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    print("fields", r.fieldnames)
    key = r.fieldnames[0]
    for row in r:
        tid = row[key]
        if tid in ("rq_2102", "rq_2103", "rq_2104"):
            print(tid, row["status"], (row.get("title") or "")[:80])

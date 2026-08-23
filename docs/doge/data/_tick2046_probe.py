import csv
csv.field_size_limit(10_000_000)

with open("docs/doge/data/loop_state.csv", newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        print("STATE:", dict(r))

with open("docs/doge/data/research_queue.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print("RQ cols:", list(rows[0].keys()) if rows else None)
inprog = [r for r in rows if r.get("status") == "in_progress"]
print("IN_PROGRESS:", len(inprog))
for r in inprog[:5]:
    print(
        r.get("id"),
        r.get("priority"),
        (r.get("title") or r.get("unit") or r.get("topic") or "")[:100],
    )

open_rows = [r for r in rows if r.get("status") == "open"]


def pri(r):
    try:
        return float(r.get("priority") or 0)
    except Exception:
        return 0


open_rows.sort(key=lambda r: (-pri(r), r.get("id", "")))
print("OPEN count:", len(open_rows))
print("TOP OPEN:")
for r in open_rows[:20]:
    title = (
        r.get("title") or r.get("unit") or r.get("topic") or r.get("description", "")
    )[:100]
    print(f"  {r.get('id')} pri={r.get('priority')} {title}")

for r in rows:
    rid = r.get("id", "")
    if rid.startswith("rq_204") or rid.startswith("rq_205"):
        title = (r.get("title") or r.get("unit") or "")[:100]
        print("NEAR:", rid, r.get("status"), r.get("priority"), title)

for kw in ["FARO", "AIESH", "REW", "YE2025", "WZC", "psych", "IGS", "dual"]:
    hits = [
        r
        for r in rows
        if kw.lower() in str(r).lower()
        and r.get("status") in ("open", "in_progress", "blocked_foi")
    ]
    print(f"KW {kw}: {len(hits)} open/ip/foi")
    for r in hits[:10]:
        title = (r.get("title") or r.get("unit") or "")[:90]
        print(f"  {r.get('id')} {r.get('status')} pri={r.get('priority')} {title}")

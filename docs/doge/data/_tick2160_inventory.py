import csv
from collections import Counter

csv.field_size_limit(10**7)
base = r"C:\Users\karel\dev\AIpolitics\docs\doge\data"
for name in ["budgets", "commitments", "leaderboard", "entities", "sources", "foi_queue", "research_queue"]:
    with open(f"{base}\\{name}.csv", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    print(name, len(rows))
    if name == "foi_queue":
        c = Counter((r.get("status") or "").strip().lower() for r in rows)
        print("  statuses", dict(c))
    if name == "research_queue":
        c = Counter((r.get("status") or "").strip().lower() for r in rows)
        print("  statuses", dict(c))

with open(f"{base}\\leaderboard.csv", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
print("lb cols", list(rows[0].keys()))


def pi(r):
    try:
        return float(r.get("priority_index") or 0)
    except Exception:
        return 0


rows.sort(key=pi, reverse=True)
print("TOP 25 raw:")
for r in rows[:25]:
    tid = r.get("item_id") or r.get("id") or r.get("leaderboard_id")
    title = (r.get("title") or r.get("name") or r.get("short_name") or "")[:70]
    amt = r.get("amount_eur") or r.get("annual_eur") or r.get("amount")
    print(f"  {pi(r):.3f} {tid} | {title} | amt={amt} conf={r.get('confidence')}")

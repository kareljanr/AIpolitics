# ephemeral inventory for tick2060 every-10
import csv

csv.field_size_limit(10_000_000)


def n(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


print("budgets", len(n("docs/doge/data/budgets.csv")))
print("commitments", len(n("docs/doge/data/commitments.csv")))
print("leaderboard", len(n("docs/doge/data/leaderboard.csv")))
print("entities", len(n("docs/doge/data/entities.csv")))
print("sources", len(n("docs/doge/data/sources.csv")))
foi = n("docs/doge/data/foi_queue.csv")
from collections import Counter

c = Counter((r.get("status") or "").lower() for r in foi)
print("foi", dict(c), "total", len(foi))

rows = []
for r in n("docs/doge/data/leaderboard.csv"):
    try:
        pi = float(r.get("priority_index") or 0)
    except ValueError:
        pi = 0
    try:
        ann = float(r.get("annual_cost_eur") or 0)
    except ValueError:
        ann = 0
    rows.append((pi, ann, r))
rows.sort(key=lambda x: (-x[0], -x[1]))
shown = 0
for pi, ann, r in rows:
    if pi > 10:
        continue
    iid = (r.get("item_id") or "").lower()
    if any(s in iid for s in ["metro3", "owv_snowball", "hedera_cap"]):
        continue
    shown += 1
    print(f"{shown:2d} pi={pi} ann={ann:.0f} {r.get('item_id')} | {(r.get('name') or '')[:70]}")
    if shown >= 12:
        break

print("--- 2051-2060 ---")
for r in n("docs/doge/data/research_queue.csv"):
    tid = r.get("task_id") or ""
    if tid in [f"rq_{i}" for i in range(2051, 2061)]:
        print(tid, r.get("status"), (r.get("entity_id") or "")[:45], (r.get("title") or "")[:95])

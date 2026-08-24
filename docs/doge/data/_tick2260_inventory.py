import csv
from collections import Counter
from pathlib import Path
csv.field_size_limit(10**7)
DATA = Path("docs/doge/data")
for fn in ["budgets.csv","commitments.csv","leaderboard.csv","entities.csv","sources.csv","foi_queue.csv","research_queue.csv"]:
    with open(DATA/fn, encoding="utf-8") as f:
        n = sum(1 for _ in csv.DictReader(f))
    print(fn, n)
with open(DATA/"foi_queue.csv", encoding="utf-8") as f:
    c = Counter((r.get("status") or "") for r in csv.DictReader(f))
print("foi", dict(c))
rows=[]
with open(DATA/"leaderboard.csv", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        try:
            pi=float(r.get("priority_index") or 0)
        except Exception:
            continue
        rows.append((pi,r))
rows.sort(key=lambda x: -x[0])
print("COLS", list(rows[0][1].keys())[:25])
print("---TOP20---")
for pi,r in rows[:20]:
    name=(r.get("name") or "")[:60]
    print("%.2f|%s|%s|%s" % (pi, r.get("item_id"), name, r.get("annual_cost_eur")))
# recent residual dual items 2251-2259
print("---RECENT DUAL---")
for pi,r in rows:
    notes=r.get("notes") or ""
    if any(x in notes for x in ["tick225","tick224"]):
        if "tick225" in notes or "tick224" in notes:
            print("%.2f|%s|%s" % (pi, r.get("item_id"), (r.get("name") or "")[:70]))

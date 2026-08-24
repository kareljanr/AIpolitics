import csv
from pathlib import Path
csv.field_size_limit(10**7)
DATA = Path("docs/doge/data")

def count(name):
    with open(DATA/name, newline="", encoding="utf-8") as f:
        return sum(1 for _ in csv.DictReader(f))

counts = {n: count(n) for n in ["budgets.csv","commitments.csv","leaderboard.csv","entities.csv","sources.csv"]}
foi = list(csv.DictReader(open(DATA/"foi_queue.csv", newline="", encoding="utf-8")))
foi_ready = sum(1 for r in foi if r.get("status")=="ready")
foi_ans = sum(1 for r in foi if r.get("status")=="answered")
foi_part = sum(1 for r in foi if r.get("status")=="partial")
print("COUNTS", counts)
print("FOI", len(foi), "ready", foi_ready, "ans", foi_ans, "partial", foi_part)

# top10 by priority_index
rows = list(csv.DictReader(open(DATA/"leaderboard.csv", newline="", encoding="utf-8")))
def pi(r):
    try: return float(r.get("priority_index") or 0)
    except: return 0
def ann(r):
    try: return float(r.get("annual_cost_eur") or 0)
    except: return 0
# filter corrupt pi>10 and stock-like
cands = [r for r in rows if pi(r) <= 10 and r.get("status")!="struck"]
cands.sort(key=lambda r: (-pi(r), -ann(r)))
print("TOP15 candidates:")
for i,r in enumerate(cands[:15],1):
    print(i, f"{pi(r):.2f}", r.get("item_id","")[:50], (r.get("name") or "")[:70], ann(r))
# recent residual items
recent = [r for r in rows if any(x in (r.get("notes") or "")+(r.get("item_id") or "") for x in ["tick213","tick214"])]
print("recent tick213x lbs", len(recent))
for r in recent[-12:]:
    print(" ", r.get("item_id"), pi(r), (r.get("name") or "")[:60])

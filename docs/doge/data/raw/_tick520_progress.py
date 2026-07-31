import csv
from pathlib import Path
from collections import Counter

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

def open_csv(fn):
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            with open(base / fn, encoding=enc, newline="") as f:
                rows = list(csv.DictReader(f))
            return rows, enc
        except Exception:
            continue
    raise RuntimeError(fn)

for fn in [
    "budgets.csv",
    "commitments.csv",
    "leaderboard.csv",
    "entities.csv",
    "sources.csv",
    "foi_queue.csv",
    "research_queue.csv",
]:
    rows, enc = open_csv(fn)
    print(fn, len(rows), enc)

foi, _ = open_csv("foi_queue.csv")
print("foi status", Counter(r.get("status", "") for r in foi))
rq, _ = open_csv("research_queue.csv")
print("rq open", [(r["task_id"], r["priority"]) for r in rq if r.get("status") == "open"])
print("rq total", len(rq))

lb, _ = open_csv("leaderboard.csv")

def pi(r):
    try:
        return float(r.get("priority_index") or 0)
    except Exception:
        return 0

def ann(r):
    try:
        return float(r.get("annual_cost_eur") or 0)
    except Exception:
        return 0

cands = [r for r in lb if ann(r) > 0]
cands.sort(key=lambda r: (-pi(r), -ann(r)))
print("=== TOP 15 ===")
for i, r in enumerate(cands[:15], 1):
    print(
        "|".join(
            [
                str(i),
                r["item_id"],
                (r.get("name") or "")[:50],
                f"{ann(r):.0f}",
                str(r.get("absurdity_score")),
                str(r.get("cost_score")),
                str(r.get("difficulty")),
                f"{pi(r):.3f}",
            ]
        )
    )

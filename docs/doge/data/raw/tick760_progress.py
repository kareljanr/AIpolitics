# tick760 progress@760 coverage + waste top10
import csv
from collections import Counter
from pathlib import Path

base = Path("docs/doge/data")

foi = list(csv.DictReader((base / "foi_queue.csv").open(encoding="utf-8")))
print("FOI", dict(Counter(r.get("status", "").strip() for r in foi)), "total", len(foi))

rows = list(csv.DictReader((base / "leaderboard.csv").open(encoding="utf-8")))


def pi(r):
    try:
        return float(r.get("priority_index") or 0)
    except Exception:
        return 0.0


def annual(r):
    try:
        return float(r.get("annual_cost_eur") or 0)
    except Exception:
        return 0.0


sorted_rows = sorted(rows, key=lambda r: (-pi(r), -annual(r)))
print("lb total", len(rows))
print("TOP 30 by pi:")
for i, r in enumerate(sorted_rows[:30], 1):
    iid = (r.get("item_id") or "")[:55]
    name = (r.get("name") or "")[:55]
    print(f"{i:2} pi={pi(r):5.2f} ann={annual(r)/1e6:10.1f}m  {iid} | {name}")

print("--- high abs >=9 ---")
for r in sorted_rows:
    try:
        a = float(r.get("absurdity_score") or 0)
    except Exception:
        a = 0
    if a >= 9.0:
        print(f"abs={a:4.1f} pi={pi(r):5.2f} {annual(r)/1e6:8.1f}m {(r.get('item_id') or '')[:50]}")

# inventory
for f in ["budgets.csv", "commitments.csv", "leaderboard.csv", "entities.csv", "sources.csv"]:
    n = sum(1 for _ in open(base / f, encoding="utf-8")) - 1
    print(f"count {f}={n}")

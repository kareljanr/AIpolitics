import csv
import sys
from collections import Counter

csv.field_size_limit(sys.maxsize)
base = "docs/doge/data/"


def n(p):
    with open(p, encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


for f in [
    "budgets.csv",
    "commitments.csv",
    "leaderboard.csv",
    "entities.csv",
    "sources.csv",
    "foi_queue.csv",
    "research_queue.csv",
]:
    print(f, n(base + f))

with open(base + "foi_queue.csv", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
print("foi status", dict(Counter((r.get("status") or "").lower() for r in rows)))

with open(base + "research_queue.csv", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
print("rq status", dict(Counter((r.get("status") or "").lower() for r in rows)))

with open(base + "leaderboard.csv", encoding="utf-8", newline="") as f:
    lb = list(csv.DictReader(f))


def pi(x):
    try:
        return float(x.get("priority_index") or 0)
    except Exception:
        return 0


cands = []
for x in lb:
    p = pi(x)
    if p > 10:
        continue
    ann = (x.get("annual_cost_eur") or "").replace(",", "")
    try:
        a = float(ann) if ann else 0
    except Exception:
        a = 0
    name = (x.get("name") or "") + (x.get("notes") or "") + (x.get("item_id") or "")
    low = name.lower()
    if any(
        k in low
        for k in [
            "snowball",
            "metro3",
            "hedera",
            "debt stock",
            "owv",
            "safe loan",
            "mff",
            "gni",
        ]
    ):
        continue
    cands.append((p, a, x))
cands.sort(key=lambda t: (-t[0], -t[1]))
print("TOP12 candidates:")
for p, a, x in cands[:12]:
    print(
        f"{p:.2f} {a/1e6:.1f}m {x.get('item_id')} | {(x.get('name') or '')[:70]}"
    )

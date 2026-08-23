# ephemeral inventory for every-10 tick2030
import csv
import sys
from collections import Counter
from pathlib import Path

csv.field_size_limit(sys.maxsize)


def n(p):
    with Path(p).open(encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


def foi_stats():
    with Path("docs/doge/data/foi_queue.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    c = Counter((r.get("status") or "").lower() for r in rows)
    return len(rows), c


b = n("docs/doge/data/budgets.csv")
c = n("docs/doge/data/commitments.csv")
l = n("docs/doge/data/leaderboard.csv")
e = n("docs/doge/data/entities.csv")
s = n("docs/doge/data/sources.csv")
ftot, fc = foi_stats()
print("budgets", b, "commitments", c, "leaderboard", l, "entities", e, "sources", s)
print(
    "foi_total",
    ftot,
    "ready",
    fc.get("ready", 0),
    "answered",
    fc.get("answered", 0),
    "partial",
    fc.get("partial", 0),
    "draft",
    fc.get("draft", 0),
)

rows = list(csv.DictReader(Path("docs/doge/data/leaderboard.csv").open(encoding="utf-8", newline="")))


def pi(r):
    try:
        return float(r.get("priority_index") or 0)
    except ValueError:
        return 0.0


def ann(r):
    try:
        return float(r.get("annual_cost_eur") or 0)
    except ValueError:
        return 0.0


ranked = sorted(
    [r for r in rows if (r.get("status") or "").lower() == "active" and pi(r) <= 10],
    key=lambda r: (-pi(r), -ann(r)),
)
print("TOP15 candidates:")
for i, r in enumerate(ranked[:15], 1):
    print(i, f"{pi(r):.2f}", r.get("item_id"), r.get("annual_cost_eur"), (r.get("name") or "")[:70])

# recent residual duals 2021-2029
print("RECENT duals:")
for r in rows:
    notes = r.get("notes") or ""
    iid = r.get("item_id") or ""
    if any(x in notes or x in iid for x in ("tick202", "tick 202")):
        if any(str(t) in notes or str(t) in iid for t in range(2021, 2030)):
            print("-", iid, r.get("annual_cost_eur"), (r.get("name") or "")[:80])

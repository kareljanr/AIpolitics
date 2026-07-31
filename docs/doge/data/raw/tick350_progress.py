# tick 350 — progress@350 inventory + top10
import csv
from collections import Counter
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")


def count_rows(name: str) -> int:
    with open(base / name, encoding="utf-8-sig", newline="") as f:
        return sum(1 for _ in csv.reader(f)) - 1


print("=== COUNTS ===")
for n in [
    "budgets.csv",
    "commitments.csv",
    "leaderboard.csv",
    "entities.csv",
    "sources.csv",
    "foi_queue.csv",
    "research_queue.csv",
]:
    print(n, count_rows(n))

with open(base / "foi_queue.csv", encoding="utf-8-sig", newline="") as f:
    foi = list(csv.DictReader(f))
print("foi_status", dict(Counter(r.get("status", "").strip() for r in foi)))

with open(base / "research_queue.csv", encoding="utf-8-sig", newline="") as f:
    rq = list(csv.DictReader(f))
print("rq_open", sum(1 for r in rq if r.get("status") == "open"))
print("rq_done", sum(1 for r in rq if r.get("status") == "done"))
print("rq_blocked", sum(1 for r in rq if r.get("status") == "blocked_foi"))
print("rq_total", len(rq))

with open(base / "leaderboard.csv", encoding="utf-8-sig", newline="") as f:
    lb = list(csv.DictReader(f))


def pi(r):
    try:
        return float(r.get("priority_index") or 0)
    except Exception:
        return 0


def fnum(r, k):
    try:
        return float(r.get(k) or 0)
    except Exception:
        return 0


lb_active = [
    r for r in lb if (r.get("status") or "seed") not in ("cancelled", "struck")
]
lb_sorted = sorted(
    lb_active,
    key=lambda r: (-pi(r), -fnum(r, "absurdity_score"), -fnum(r, "annual_cost_eur")),
)
print("lb_active", len(lb_active))
print("=== TOP15 ===")
for i, r in enumerate(lb_sorted[:15], 1):
    name = (r.get("name") or "")[:70]
    print(
        "|".join(
            [
                str(i),
                r.get("item_id") or "",
                name,
                r.get("annual_cost_eur") or "",
                r.get("absurdity_score") or "",
                r.get("cost_score") or "",
                r.get("difficulty") or "",
                r.get("priority_index") or "",
            ]
        )
    )

print("=== HIGH_ABS ===")
lb_abs = sorted(
    lb_active,
    key=lambda r: (-fnum(r, "absurdity_score"), -fnum(r, "annual_cost_eur")),
)
for i, r in enumerate(lb_abs[:8], 1):
    name = (r.get("name") or "")[:55]
    print(
        "|".join(
            [
                str(i),
                r.get("item_id") or "",
                r.get("absurdity_score") or "",
                r.get("annual_cost_eur") or "",
                name,
            ]
        )
    )

# recent dual material for progress notes (ticks 341-349)
print("=== RECENT LB (tick34x keywords) ===")
keys = (
    "vaf",
    "cca",
    "taxshelter",
    "wallimage",
    "screen",
    "sport",
    "adeps",
    "fwo",
    "fnrs",
    "awv",
    "sofico",
    "oe_",
    "erfgoed",
    "av_",
)
for r in lb:
    iid = (r.get("item_id") or "").lower()
    if any(k in iid for k in keys) and "tick34" in (r.get("notes") or ""):
        print(r.get("item_id"), r.get("annual_cost_eur"), (r.get("notes") or "")[:40])

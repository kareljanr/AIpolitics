# tick 530 progress helper
import csv
from pathlib import Path
from collections import Counter

base = Path("docs/doge/data")

def open_csv(name):
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            path = base / name
            with open(path, encoding=enc, newline="") as f:
                f.read()
            return open(path, encoding=enc, newline="")
        except UnicodeDecodeError:
            continue
    return open(base / name, encoding="utf-8", errors="replace", newline="")


def count_rows(name):
    with open_csv(name) as f:
        return sum(1 for _ in csv.reader(f)) - 1

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

with open_csv("foi_queue.csv") as f:
    rows = list(csv.DictReader(f))
st = Counter((r.get("status") or "").strip() for r in rows)
print("FOI status", dict(st))
print(
    "ready",
    st.get("ready", 0),
    "draft",
    st.get("draft", 0),
    "answered",
    st.get("answered", 0),
    "sent",
    st.get("sent", 0),
)

with open_csv("research_queue.csv") as f:
    rq = list(csv.DictReader(f))
print("rq open", sum(1 for r in rq if r.get("status") == "open"))
print("rq total", len(rq))
print("open ids", [r["task_id"] for r in rq if r.get("status") == "open"][:15])

with open_csv("leaderboard.csv") as f:
    lb = list(csv.DictReader(f))


def fnum(x):
    try:
        return float(x or 0)
    except Exception:
        return 0.0


scored = []
for r in lb:
    ann = fnum(r.get("annual_cost_eur"))
    pi = fnum(r.get("priority_index"))
    if ann <= 0:
        continue
    scored.append((pi, ann, r))
scored.sort(key=lambda t: (-t[0], -t[1]))
print("lb rows", len(lb), "with annual>0", len(scored))
print("TOP20:")
for i, (pi, ann, r) in enumerate(scored[:20], 1):
    name = (r.get("name") or "")[:70]
    notes = (r.get("notes") or "")[:50]
    print(
        i,
        r.get("item_id"),
        name,
        int(ann),
        "abs",
        r.get("absurdity_score"),
        "cost",
        r.get("cost_score"),
        "diff",
        r.get("difficulty"),
        "pi",
        pi,
        notes,
    )

# high absurdity regardless of annual
abs_scored = sorted(lb, key=lambda r: (-fnum(r.get("absurdity_score")), -fnum(r.get("priority_index"))))
print("HIGH_ABSURDITY:")
for r in abs_scored[:12]:
    print(
        r.get("item_id"),
        (r.get("name") or "")[:60],
        "abs",
        r.get("absurdity_score"),
        "ann",
        r.get("annual_cost_eur"),
        "pi",
        r.get("priority_index"),
    )

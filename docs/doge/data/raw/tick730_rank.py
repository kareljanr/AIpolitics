# tick730 — rank leaderboard for progress refresh
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
D = Path(__file__).resolve().parents[1]

rows = []
with open(D / "leaderboard.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        def fnum(k, default=0.0):
            v = row.get(k)
            if v is None or v == "":
                return default
            try:
                return float(v)
            except Exception:
                return default

        rows.append(
            {
                "pi": fnum("priority_index"),
                "abs": fnum("absurdity_score"),
                "cost": fnum("cost_score"),
                "diff": fnum("difficulty"),
                "ann": fnum("annual_cost_eur"),
                "tot": fnum("total_cost_eur"),
                "id": (row.get("item_id") or "").strip(),
                "name": (row.get("name") or "")[:110],
                "notes": (row.get("notes") or "")[:100],
            }
        )

flow = [r for r in rows if r["ann"] > 0]
flow.sort(key=lambda x: (-x["pi"], -x["ann"]))
print("=== TOP 25 annual>0 by priority_index ===")
for i, r in enumerate(flow[:25], 1):
    print(
        f"{i}. pi={r['pi']:.2f} abs={r['abs']:.1f} cost={r['cost']:.1f} "
        f"ann={r['ann']/1e6:.2f}m id={r['id']} name={r['name']}"
    )

print("\n=== NEW residual keys top ===")
for key in ["owv_", "tv_", "intsec", "antifraud", "otw_", "gip_", "dbfm", "sub_snow"]:
    hits = [r for r in rows if key in r["id"].lower()]
    hits.sort(key=lambda x: -x["pi"])
    print(key, "n=", len(hits))
    for h in hits[:4]:
        print(f"  pi={h['pi']:.2f} abs={h['abs']:.1f} ann={h['ann']/1e6:.1f}m {h['id']}")

print("\n=== HIGH ABS >=8.5 ===")
ha = sorted(rows, key=lambda x: (-x["abs"], -x["pi"]))
n = 0
for r in ha:
    if r["abs"] >= 8.5:
        n += 1
        print(
            f"{n}. abs={r['abs']:.1f} pi={r['pi']:.2f} ann={r['ann']/1e6:.1f}m "
            f"{r['id']} | {r['name'][:75]}"
        )
        if n >= 25:
            break

# counts
for name in [
    "budgets.csv",
    "commitments.csv",
    "leaderboard.csv",
    "entities.csv",
    "sources.csv",
    "foi_queue.csv",
    "research_queue.csv",
]:
    with open(D / name, encoding="utf-8") as f:
        print(name, sum(1 for _ in f) - 1)

from collections import Counter

st = Counter()
with open(D / "foi_queue.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        s = (row.get("status") or "").strip()
        if s in ("ready", "answered", "sent", "draft", "cancelled"):
            st[s] += 1
        elif "ready" in s:
            st["ready"] += 1
print("foi_status_clean", dict(st))

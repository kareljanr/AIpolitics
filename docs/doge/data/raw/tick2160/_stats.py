# -*- coding: utf-8 -*-
import csv
from collections import Counter
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"docs/doge/data")


def n(p):
    with (ROOT / p).open(newline="", encoding="utf-8") as f:
        return sum(1 for _ in csv.DictReader(f))


print("budgets", n("budgets.csv"))
print("commitments", n("commitments.csv"))
print("leaderboard", n("leaderboard.csv"))
print("entities", n("entities.csv"))
print("sources", n("sources.csv"))
with (ROOT / "foi_queue.csv").open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print("foi", dict(Counter(r.get("status") for r in rows)), "total", len(rows))

with (ROOT / "leaderboard.csv").open(newline="", encoding="utf-8") as f:
    lbs = list(csv.DictReader(f))


def pi(r):
    try:
        return float(r.get("priority_index") or 0)
    except Exception:
        return 0


# Prefer TE-adjacent / open; exclude absurd pi>10
cands = [r for r in lbs if 0 < pi(r) <= 10]
cands.sort(key=pi, reverse=True)
print("TOP15:")
for r in cands[:15]:
    print(
        f"{pi(r):.2f}\t{(r.get('item_id') or '')[:60]}\tann={(r.get('annual_cost_eur') or '')[:14]}\tabs={(r.get('absurdity_score') or '')}"
    )

# recent dual items 2151-2159
print("RECENT:")
for r in lbs:
    notes = r.get("notes") or ""
    if any(f"tick{t}" in notes for t in range(2151, 2160)):
        print((r.get("item_id") or "")[:70], notes[:80])

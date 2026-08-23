# -*- coding: utf-8 -*-
import csv

csv.field_size_limit(10**7)


def count_rows(path: str) -> int:
    with open(path, encoding="utf-8-sig", newline="") as f:
        return sum(1 for _ in csv.reader(f)) - 1


print("budgets", count_rows("docs/doge/data/budgets.csv"))
print("commitments", count_rows("docs/doge/data/commitments.csv"))
print("leaderboard", count_rows("docs/doge/data/leaderboard.csv"))
print("entities", count_rows("docs/doge/data/entities.csv"))
print("sources", count_rows("docs/doge/data/sources.csv"))

foi_ready = foi_ans = foi_part = foi_tot = 0
with open("docs/doge/data/foi_queue.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        foi_tot += 1
        st = (r.get("status") or "").lower()
        if st == "ready":
            foi_ready += 1
        elif st == "answered":
            foi_ans += 1
        elif st == "partial":
            foi_part += 1
print("foi", foi_ready, foi_ans, foi_part, foi_tot)

rows = []
with open("docs/doge/data/leaderboard.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        try:
            pi = float(r.get("priority_index") or 0)
        except Exception:
            continue
        if pi > 10:
            continue
        try:
            annual = float(str(r.get("annual_cost_eur") or "0").replace(",", ""))
        except Exception:
            annual = 0
        rows.append((pi, annual, r))
rows.sort(key=lambda x: (-x[0], -x[1]))
print("TOP candidates:")
for pi, annual, r in rows[:12]:
    name = (r.get("name") or "")[:70]
    print(f"{pi:.2f} {annual/1e6:.2f}m {r.get('item_id')} | {name}")

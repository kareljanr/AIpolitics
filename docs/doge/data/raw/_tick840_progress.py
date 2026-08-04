# tick840 progress inventory
import csv
import re
from collections import Counter
from pathlib import Path

root = Path("docs/doge/data")

rows = []
with open(root / "leaderboard.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        st = (row.get("status") or "active").strip()
        if st and st not in ("active",):
            continue
        try:
            pi = float(row.get("priority_index") or 0)
        except ValueError:
            pi = 0
        rows.append((pi, row))
rows.sort(key=lambda x: -x[0])

print("=== TOP 12 by priority_index (active) ===")
for i, (pi, row) in enumerate(rows[:12], 1):
    name = (row.get("name") or "")[:75]
    ann = row.get("annual_cost_eur")
    print(f"{i}. pi={pi} {row.get('item_id')} | {name} | ann={ann}")

c = Counter()
with open(root / "foi_queue.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        c[row.get("status", "?")] += 1
print("FOI", dict(c), "total", sum(c.values()))

# inventory counts
for name in ["budgets", "commitments", "leaderboard", "entities", "sources"]:
    path = root / f"{name}.csv"
    n = sum(1 for _ in open(path, encoding="utf-8", errors="replace")) - 1
    print(f"{name}: {n}")

ticks = Counter()
with open(root / "budgets.csv", encoding="utf-8", errors="replace") as f:
    for line in f:
        m = re.search(r"tick(83[0-9]|84[0-9])", line)
        if m:
            ticks[m.group(1)] += 1
print("budget ticks", dict(sorted(ticks.items())))

# sum recent city assets for notes
keys = [
    "bud_kortrijk_assets_2025",
    "bud_genk_assets_2025",
    "bud_aalst_assets_2025",
    "bud_brugge_assets_2025",
    "bud_tielt_assets_2025",
    "bud_mechelen_assets",
]
with open(root / "budgets.csv", encoding="utf-8", errors="replace") as f:
    for line in f:
        for k in keys:
            if line.startswith(k + ","):
                parts = line.split(",")
                print(k, parts[3] if len(parts) > 3 else "?")

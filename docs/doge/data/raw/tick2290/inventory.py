import csv
from collections import Counter

csv.field_size_limit(10**7)


def count(path):
    with open(path, encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


def foi_stats():
    with open("docs/doge/data/foi_queue.csv", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    c = Counter(r.get("status") for r in rows)
    return len(rows), c


b = count("docs/doge/data/budgets.csv")
c = count("docs/doge/data/commitments.csv")
l = count("docs/doge/data/leaderboard.csv")
e = count("docs/doge/data/entities.csv")
s = count("docs/doge/data/sources.csv")
ft, fc = foi_stats()
print("budgets", b)
print("commitments", c)
print("leaderboard", l)
print("entities", e)
print("sources", s)
print("foi_total", ft)
print("foi_status", dict(fc))

with open("docs/doge/data/leaderboard.csv", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))


def pi(r):
    try:
        return float(r.get("priority_index") or 0)
    except Exception:
        return 0.0


rows = sorted(rows, key=pi, reverse=True)
for r in rows[:12]:
    print(f"{pi(r):.2f}|{(r.get('name') or '')[:75]}|{r.get('annual_cost_eur')}|{r.get('item_id')}")

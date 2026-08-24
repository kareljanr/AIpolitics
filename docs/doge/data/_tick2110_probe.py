import csv
from collections import Counter

csv.field_size_limit(10**7)


def n(p):
    with open(p, encoding="utf-8-sig", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


print("budgets", n("docs/doge/data/budgets.csv"))
print("commitments", n("docs/doge/data/commitments.csv"))
print("leaderboard", n("docs/doge/data/leaderboard.csv"))
print("entities", n("docs/doge/data/entities.csv"))
print("sources", n("docs/doge/data/sources.csv"))
with open("docs/doge/data/foi_queue.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
c = Counter((r.get("status") or "").strip() for r in rows)
print("foi_ready", c.get("ready", 0), "answered", c.get("answered", 0), "partial", c.get("partial", 0), "total", len(rows))

with open("docs/doge/data/leaderboard.csv", encoding="utf-8-sig") as f:
    lbs = list(csv.DictReader(f))


def pi(r):
    try:
        return float(r.get("priority_index") or 0)
    except Exception:
        return 0


filt = [
    r
    for r in lbs
    if pi(r) <= 10
    and r.get("status") != "struck"
    and "Metro3" not in str(r)
    and "snowball" not in str(r).lower()
]
filt.sort(key=pi, reverse=True)
for r in filt[:10]:
    print(f"{pi(r):.2f}|{(r.get('item_id') or '')[:42]}|{(r.get('name') or '')[:50]}")

# check sint jozef ninove unused
blob = ""
with open("docs/doge/data/entities.csv", encoding="utf-8-sig") as f:
    for e in csv.DictReader(f):
        blob += " ".join(str(v or "") for v in e.values())
print("0452865383", "FOUND" if "0452865383" in blob.replace(".", "") else "MISSING")

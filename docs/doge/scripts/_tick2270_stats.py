import csv
from collections import Counter

csv.field_size_limit(10**7)

with open("docs/doge/data/leaderboard.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))


def pi(r):
    try:
        return float(r.get("priority_index") or 0)
    except Exception:
        return 0


def annual(r):
    try:
        return float(r.get("annual_cost_eur") or 0)
    except Exception:
        return 0


rows.sort(key=lambda r: (-pi(r), -annual(r)))
print("LB count", len(rows))
print("TOP20 raw by pi")
for r in rows[:20]:
    iid = (r.get("item_id") or "")[:65]
    name = (r.get("name") or "")[:65]
    print(
        "%.2f | %s | %s | %s | %s"
        % (pi(r), iid, r.get("annual_cost_eur"), r.get("confidence"), name)
    )

filtered = []
for r in rows:
    p = pi(r)
    if p > 10:
        continue
    blob = ((r.get("item_id") or "") + " " + (r.get("name") or "")).lower()
    if any(m in blob for m in ("owv_snowball", "metro3_overrun", "metro3_gap", "metro3")):
        continue
    filtered.append(r)

print("\nFILTERED top15")
for r in filtered[:15]:
    print(
        "%.2f | %s | %s | %s"
        % (pi(r), (r.get("item_id") or "")[:70], r.get("annual_cost_eur"), (r.get("name") or "")[:60])
    )

for n in [
    "entities",
    "sources",
    "budgets",
    "commitments",
    "leaderboard",
    "foi_queue",
    "research_queue",
]:
    with open("docs/doge/data/%s.csv" % n, newline="", encoding="utf-8") as f:
        rr = list(csv.DictReader(f))
    print(n, len(rr))
    if n == "foi_queue":
        print("FOI", Counter(x.get("status") for x in rr))
    if n == "research_queue":
        print("RQ", Counter(x.get("status") for x in rr))

print("\nRecent LB 2261-2269")
for r in rows:
    notes = r.get("notes") or ""
    if any(("tick%d" % t) in notes for t in range(2261, 2270)):
        print(
            (r.get("item_id") or "")[:60],
            r.get("priority_index"),
            r.get("annual_cost_eur"),
            notes[:40],
        )

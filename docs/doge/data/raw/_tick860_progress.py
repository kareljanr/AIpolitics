import csv
from pathlib import Path
from collections import Counter

csv.field_size_limit(10_000_000)


def count(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


for name in ["budgets", "commitments", "leaderboard", "entities", "sources", "foi_queue", "research_queue"]:
    print(name, count(f"docs/doge/data/{name}.csv"))

with Path("docs/doge/data/foi_queue.csv").open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
print("foi status", dict(Counter(r.get("status") for r in rows)))

with Path("docs/doge/data/leaderboard.csv").open(encoding="utf-8", newline="") as f:
    lbs = list(csv.DictReader(f))


def pi(r):
    try:
        return float(r.get("priority_index") or 0)
    except Exception:
        return 0


def ann(r):
    try:
        return float(r.get("annual_cost_eur") or 0)
    except Exception:
        return 0


active = [r for r in lbs if (r.get("status") or "active") == "active"]
# pure annual: type not debt_stock, annual > 0
pure = []
for r in active:
    t = (r.get("type") or "").lower()
    a = ann(r)
    name = (r.get("name") or "").lower()
    notes = ((r.get("notes") or "") + " " + (r.get("tco_notes") or "")).lower()
    if t in ("debt_stock",):
        continue
    if a <= 0:
        continue
    if "stock" in t and a < 10_000_000:
        continue
    # skip multi-bn steered governance without true annual waste identity for ranking stability
    pure.append(r)

pure.sort(key=lambda r: (-pi(r), -ann(r)))
print("\nTOP PURE ANNUAL:")
for i, r in enumerate(pure[:15], 1):
    print(i, r["item_id"], "pi", r.get("priority_index"), "ann", r.get("annual_cost_eur"), "abs", r.get("absurdity_score"), r.get("name", "")[:70])

overall = sorted(active, key=lambda r: (-pi(r), -ann(r)))
print("\nTOP OVERALL PI:")
for i, r in enumerate(overall[:15], 1):
    print(i, r["item_id"], "pi", r.get("priority_index"), "ann", r.get("annual_cost_eur"), "type", r.get("type"), r.get("name", "")[:60])

# high absurdity city FOI-adjacent 851-859
print("\nCITY TICK 851-859:")
with Path("docs/doge/data/entities.csv").open(encoding="utf-8", newline="") as f:
    for e in csv.DictReader(f):
        n = e.get("notes") or ""
        if any(f"tick85{x}" in n for x in "123456789") or "tick859" in n:
            if e.get("entity_id", "").startswith("city_"):
                print(e["entity_id"], n[:120])

# recent leaderboard FOI-adjacent high pi from cities
print("\nRECENT CITY LB HIGH PI:")
city_lbs = [r for r in active if any(x in (r.get("item_id") or "") for x in ("_ie_", "_ld_", "_iz_", "_wg_", "_dd_", "_lm_", "_hb_", "_gb_", "_aa_", "ieper", "landen", "izegem", "waregem", "dendermonde", "lommel", "heist", "geraards", "aarschot", "dual_"))]
city_lbs = [r for r in active if (r.get("item_id") or "").startswith(("lb_ie_", "lb_ld_", "lb_iz_", "lb_wg_", "lb_dd_", "lb_lm_", "lb_hb_", "lb_gb_", "lb_aa_", "lb_dual_"))]
city_lbs.sort(key=lambda r: -pi(r))
for r in city_lbs[:20]:
    print(r["item_id"], "pi", r.get("priority_index"), r.get("name", "")[:70])

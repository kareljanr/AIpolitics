# ephemeral inventory for every-10 tick2040
import csv
import sys
from collections import Counter
from pathlib import Path

csv.field_size_limit(sys.maxsize)


def n(p):
    with Path(p).open(encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


def foi_stats():
    with Path("docs/doge/data/foi_queue.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    c = Counter((r.get("status") or "").lower() for r in rows)
    return len(rows), c


b = n("docs/doge/data/budgets.csv")
c = n("docs/doge/data/commitments.csv")
l = n("docs/doge/data/leaderboard.csv")
e = n("docs/doge/data/entities.csv")
s = n("docs/doge/data/sources.csv")
ftot, fc = foi_stats()
print("budgets", b, "commitments", c, "leaderboard", l, "entities", e, "sources", s)
print(
    "foi_total",
    ftot,
    "ready",
    fc.get("ready", 0),
    "answered",
    fc.get("answered", 0),
    "partial",
    fc.get("partial", 0),
    "draft",
    fc.get("draft", 0),
)

rows = list(csv.DictReader(Path("docs/doge/data/leaderboard.csv").open(encoding="utf-8", newline="")))


def pi(r):
    try:
        return float(r.get("priority_index") or 0)
    except ValueError:
        return 0.0


def ann(r):
    try:
        return float(r.get("annual_cost_eur") or 0)
    except ValueError:
        return 0.0


# Match prior every-10: active, pi<=10, exclude obvious stocks / snowballs / corrupt AGB
STOCK_MARKERS = (
    "snowball",
    "stock",
    "debt stock",
    "metro3",
    "owv",
    "hedera",
    "safe loan",
    "mff",
    "hermreg",
    "illness",
    "riziv",
    "balance sheet",
)
corrupt = [r for r in rows if pi(r) > 10]
print("corrupt_pi_gt10", len(corrupt))

ranked = sorted(
    [
        r
        for r in rows
        if (r.get("status") or "").lower() == "active"
        and 0 < pi(r) <= 10
        and ann(r) >= 1e6
    ],
    key=lambda r: (-pi(r), -ann(r)),
)

# Prefer known TE/FFS annual flow ids from prior top10 first if still present
prior_ids = [
    "lb_vl_gip_monitor_fail_2_5bn",
    "lb_fed_fossil_direct_13_3bn",
    "lb_fed_fossil_accises_10_5bn",
    "lb_company_cars_fpb",
    "lb_exc_heatoil",
    "lb_cheque_economy",
    "lb_co2_vs_ordinary_ssc_gap_1bn",
    "lb_oaa_consol_reporte_300_6m",
    "lb_bcr_annexe2_reporte_wave",
    "lb_dual_cars_ssc_taxex",
]
by_id = {r.get("item_id"): r for r in rows}
print("PRIOR top10 still present?")
for iid in prior_ids:
    r = by_id.get(iid)
    if r:
        print(
            "-",
            iid,
            "pi",
            r.get("priority_index"),
            "ann",
            r.get("annual_cost_eur"),
            "status",
            r.get("status"),
        )
    else:
        print("- MISSING", iid)

print("TOP15 by pi (ann>=1m, pi<=10):")
for i, r in enumerate(ranked[:15], 1):
    print(
        i,
        f"{pi(r):.2f}",
        r.get("item_id"),
        r.get("annual_cost_eur"),
        (r.get("name") or "")[:70],
    )

# recent residual duals 2031-2039
print("RECENT duals 2031-2039:")
for r in rows:
    notes = r.get("notes") or ""
    iid = r.get("item_id") or ""
    if any(f"tick{t}" in notes or f"tick{t}" in iid for t in range(2031, 2040)):
        print("-", iid, r.get("annual_cost_eur"), (r.get("name") or "")[:80])

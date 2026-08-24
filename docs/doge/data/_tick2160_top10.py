import csv

csv.field_size_limit(10**7)
base = r"C:\Users\karel\dev\AIpolitics\docs\doge\data"
with open(f"{base}\\leaderboard.csv", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

# Known pure annual top10 IDs from prior every-10
keep_ids = [
    "lb_vl_gip_monitor_fail_2_5bn",
    "lb_fed_fossil_direct_13_3bn",
    "lb_company_cars_fpb",
    "lb_fed_fossil_accises_10_5bn",
    "lb_exc_heatoil",
    "lb_cheque_economy",
    "lb_co2_vs_ordinary_ssc_gap_1bn",
    "lb_dual_cars_ssc_taxex",
    "lb_oaa_consol_reporte_300_6m",
    "lb_bcr_annexe2_reporte_wave",
]
by_id = {r["item_id"]: r for r in rows}
print("verify keep_ids:")
for i, iid in enumerate(keep_ids, 1):
    r = by_id.get(iid)
    if not r:
        print(i, iid, "MISSING")
        continue
    print(
        i,
        iid,
        "pi=",
        r.get("priority_index"),
        "ann=",
        r.get("annual_cost_eur"),
        "abs=",
        r.get("absurdity_score"),
        "cost=",
        r.get("cost_score"),
        "diff=",
        r.get("difficulty"),
        "name=",
        (r.get("name") or "")[:50],
    )

# Also find rows with pi between 7 and 10 sorted
cands = []
for r in rows:
    try:
        p = float(r.get("priority_index") or 0)
    except Exception:
        continue
    if 7.0 <= p <= 10.0:
        cands.append((p, r))
cands.sort(key=lambda x: -x[0])
print("\npi 7-10 top 15:")
for p, r in cands[:15]:
    print(p, r["item_id"], (r.get("name") or "")[:55], r.get("annual_cost_eur"))

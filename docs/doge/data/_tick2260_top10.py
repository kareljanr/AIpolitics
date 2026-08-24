import csv
from pathlib import Path
csv.field_size_limit(10**7)
DATA = Path("docs/doge/data")
# known pure annual top10 ids from 2250
ids = [
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
want=set(ids)
found={}
rows=[]
with open(DATA/"leaderboard.csv", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        try: pi=float(r.get("priority_index") or 0)
        except: continue
        rows.append((pi,r))
        if r.get("item_id") in want:
            found[r["item_id"]]=r
print("found", len(found))
for i in ids:
    r=found.get(i)
    if not r:
        print("MISSING", i); continue
    print("%.2f|%s|%s|abs=%s cost=%s diff=%s" % (
        float(r["priority_index"]), r["item_id"], r.get("annual_cost_eur"),
        r.get("absurdity_score"), r.get("cost_score"), r.get("difficulty")))

# also find pure annual candidates with pi between 8 and 10, annual >= 100m
print("---PURE CANDIDATES pi 8-10 annual>=100m---")
for pi,r in sorted(rows, key=lambda x:-x[0]):
    if pi>10 or pi<8: continue
    try:
        a=float(str(r.get("annual_cost_eur") or "0").replace(" ","").replace(",",""))
    except: continue
    if a < 1e8: continue
    print("%.2f|%s|%.0f|%s" % (pi, r.get("item_id"), a, (r.get("name") or "")[:50]))

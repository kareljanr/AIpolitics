# -*- coding: utf-8 -*-
import csv
csv.field_size_limit(10**7)

def budgets_for(eid):
    with open("docs/doge/data/budgets.csv", encoding="utf-8-sig", newline="") as f:
        return [x for x in csv.DictReader(f) if x.get("entity_id") == eid]

for eid in [
    "vzw_zorg_en_welzijn_kuurne",
    "vzw_wzc_huize_vincent",
    "vzw_groep_zorg_h_familie",
    "vzw_woonzorgcentra_ocura_beringen",
    "vzw_wzc_ter_burg",
]:
    b = budgets_for(eid)
    years = sorted({x.get("year") for x in b})
    print(eid, "n=", len(b), "years=", years)
    for x in b[:3]:
        print(" ", x.get("year"), x.get("amount_eur"), (x.get("metric") or x.get("line_item") or "")[:70])

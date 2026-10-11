# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/commitments.csv")
row = {
    "commitment_id": "comm_ptri_jr2025_pnl",
    "title": "AGB Patri JR2025 leftover AGB dual (assets 9.69m / brutomarge 0.57m / debt 4.57m / recv 1.57m / PnL +0.08m)",
    "entity_id": "agb_ptri",
    "beneficiary": "AGB Patri / Stad Sint-Truiden / cultuurcentra",
    "legal_basis": "WVV autonoom gemeentebedrijf; Decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
    "decision_date": "2026-06-22",
    "start_year": "2015",
    "end_year": "",
    "total_envelope_eur": "574007",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00258861.pdf",
    "stated_goal": "Local leftover AGB map VL Sint-Truiden cultuurcentra — 0.57m brutomarge / 4.57m debt / 1.57m recv / PnL +0.08m",
    "cut_option": "Publish omzet 70 + 60/61 split + pers 62/VTE + ST recv 1.57m counterpart + LT bank 3.40m terms + overige ST 0.22m + commissaris unpublished; do not keep leftover AGB as dual unpublished vehicle",
    "source_id": "src_ptri_jr2025_nbb",
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Limburg>Sint-Truiden>AGB_Patri>JR2025_L5",
    "notes": "tick1407; assets 9688747 brutomarge 574007 omzet empty diensten empty pers empty debt 4566935 recv 1565883 pnl 84930 equity 5017317 cash 380295 capex 127844 dividend 16986; FOI ready not sent; not TE-additive of 348bn; double_count vs Stad Sint-Truiden / AGOST possible",
}
with p.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    seen = {x[fields[0]] for x in r}
added = 0
with p.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    if row[fields[0]] not in seen:
        w.writerow({k: row.get(k, "") for k in fields})
        added = 1
print("commitments", added)

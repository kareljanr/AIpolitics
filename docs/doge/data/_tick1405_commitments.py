# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/commitments.csv")
row = {
    "commitment_id": "comm_tlt_jr2025_pnl",
    "title": "AGB Tielt JR2025 leftover AGB dual (assets 19.95m / brutomarge 0.68m / lease 9.30m / debt 11.90m / PnL +0.32m)",
    "entity_id": "agb_tlt",
    "beneficiary": "AGB Tielt / Stad Tielt / sportaccommodaties + monumenten",
    "legal_basis": "WVV autonoom gemeentebedrijf; Decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
    "decision_date": "2026-07-02",
    "start_year": "2011",
    "end_year": "",
    "total_envelope_eur": "679356",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00316168.pdf",
    "stated_goal": "Local leftover AGB map VL sport+monumenten — 0.68m brutomarge / omzet empty / 9.30m lease / 11.90m debt / PnL +0.32m",
    "cut_option": "Publish omzet 70 + 60/61 diensten split + 9.30m lease counterpart + 1.99m overige leningen + pers 62/VTE + commissaris; do not keep AGB as dual unpublished vehicle",
    "source_id": "src_tlt_jr2025_nbb",
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Tielt>AGB_Tielt>JR2025_L5",
    "notes": "tick1405; assets 19953810 brutomarge 679356 debt 11899035 lease 9303045 pnl 321320 equity 5586840 cash 1132461 capex 388010 dividend 160660; FOI ready not sent; not TE-additive of 348bn; double_count vs gemeente sport fees possible",
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

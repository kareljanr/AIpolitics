# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/commitments.csv")
row = {
    "commitment_id": "comm_ibeg_jr2025_pnl",
    "title": "IGS IBEG JR2025 leftover IGS dual (assets 100.49m / omzet empty / FVA 96.37m / dividend 3.50m / PnL +1.28m)",
    "entity_id": "igs_ibeg",
    "beneficiary": "IGS IBEG / Grimbergen + Machelen + Meise + Vilvoorde + Wemmel (ibeg.be; leftover IGS energy holding HV)",
    "legal_basis": "WVV OV; Decreet Lokaal Bestuur; NBB neerlegging",
    "decision_date": "2026-06-23",
    "start_year": "1968",
    "end_year": "",
    "total_envelope_eur": "3500000",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00238388.pdf",
    "stated_goal": "Local leftover IGS map VL energy holding HV 5 gemeenten — omzet unpublished / 3.50m dividend / 96.37m FVA / PnL +1.28m",
    "cut_option": "Publish omzet + 809k diensten split + 3.50m dividend per vennoot + 96.37m FVA counterparts + 9.00m Fluvius HV loan terms + statutory audit oordeel; do not keep energy holding IGS as dual unpublished vehicle",
    "source_id": "src_ibeg_jr2025_nbb",
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>IGS>IBEG>JR2025_L5",
    "notes": "tick1398; assets 100488193 omzet empty diensten 809703 debt 1450184 pnl 1283311 equity 99038008 div 3500000 fva 96372430; FOI ready not sent; not TE-additive of 348bn; double_count vs Fluvius HV 1387 possible",
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

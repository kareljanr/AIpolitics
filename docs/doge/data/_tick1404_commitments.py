# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/commitments.csv")
row = {
    "commitment_id": "comm_psln_jr2025_pnl",
    "title": "Psilon JR2025 leftover crematorium IGS dual (assets 8.63m / brutomarge 1.94m / debt 2.19m / PnL +0.50m)",
    "entity_id": "igs_psln",
    "beneficiary": "Psilon / 22 West-Vlaanderen vennoten / crematorium Uitzicht Kortrijk",
    "legal_basis": "WVV opdrachthoudende vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
    "decision_date": "2026-06-17",
    "start_year": "2005",
    "end_year": "",
    "total_envelope_eur": "1935397",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00258944.pdf",
    "stated_goal": "Local leftover crematorium IGS map VL funeral — 1.94m brutomarge / omzet empty / 2.19m debt / PnL +0.50m",
    "cut_option": "Publish omzet 70 + 60/61 diensten split + 2.19m bank counterpart + 6.20m vennoten guarantee named share + 5-6.8m energy-transit reserve plan; do not keep crematorium IGS as dual unpublished vehicle",
    "source_id": "src_psln_jr2025_nbb",
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>IGS>Psilon>JR2025_L5",
    "notes": "tick1404; assets 8627377 brutomarge 1935397 pers 877307 debt 2186709 voorzieningen 327247 pnl 498832 equity 6113421 cash 776217 capex 170092; FOI ready not sent; not TE-additive of 348bn; double_count vs gemeente funeral fees possible",
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

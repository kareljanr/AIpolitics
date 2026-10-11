# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/commitments.csv")
row = {
    "commitment_id": "comm_ovco_jr2025_pnl",
    "title": "OVCO JR2025 leftover crematorium IGS dual (assets 9.37m / debt 6.31m / CIP 0.98m / brutomarge 1.16m / PnL +0.39m)",
    "entity_id": "igs_ovco",
    "beneficiary": "OVCO / Oostende+Bredene+Middelkerke+Oudenburg vennoten / Crematorium Polderbos",
    "legal_basis": "WVV opdrachthoudende vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
    "decision_date": "2026-06-25",
    "start_year": "2011",
    "end_year": "",
    "total_envelope_eur": "6313967",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00287142.pdf",
    "stated_goal": "Local leftover crematorium IGS map VL funeral — 6.31m debt / 0.98m CIP / unpublished omzet / PnL +0.39m",
    "cut_option": "Publish omzet 70 + 60/61 split + 6.31m debt counterpart/rate/waarborg + 0.98m CIP dossier + 0.97m beleggingen bank + 1.74m capsub dossier + named vennoten share; do not keep crematorium IGS as dual unpublished vehicle",
    "source_id": "src_ovco_jr2025_nbb",
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>IGS>OVCO>JR2025_L5",
    "notes": "tick1401; assets 9368744 brutomarge 1163024 pers 459819 debt 6313967 pnl 385548 equity 3054777 cash 83941 invest 973616 cip 975949 capsub 1743380; FOI ready not sent; not TE-additive of 348bn; double_count vs gemeente funeral fees possible",
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

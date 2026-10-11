# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/commitments.csv")
row = {
    "commitment_id": "comm_mlso_jr2025_pnl",
    "title": "MLSO JR2025 leftover IGS dual (assets 227.28m / omzet 24.04m / diensten 7.75m / Interwaas 3.76m / PnL +7.70m)",
    "entity_id": "igs_mlso",
    "beneficiary": "MLSO / Vlaams Gewest / Haven Antwerpen-Brugge / Interwaas / Waaslandhaven concessionarissen",
    "legal_basis": "WVV opdrachthoudende vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging; wet Chabert",
    "decision_date": "2026-06-03",
    "start_year": "1982",
    "end_year": "",
    "total_envelope_eur": "24044090",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00247733.pdf",
    "stated_goal": "Local leftover IGS map VL Waaslandhaven — 24.04m omzet / 7.75m diensten / 3.76m Interwaas / 4.42m nrec / PnL +7.70m",
    "cut_option": "Publish 7.75m diensten split + 3.76m Interwaas booking + 4.42m nrec split + 6.82m overige schulden + named vennoten/dividend; do not keep IGS as dual unpublished vehicle",
    "source_id": "src_mlso_jr2025_nbb",
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Waaslandhaven>MLSO>JR2025_L5",
    "notes": "tick1406; assets 227277417 omzet 24044090 diensten 7752488 interwaas 3762956 nrec 4415758 debt 13594288 pnl 7699101 equity 213683129 cash 24924839 capex 259767 dividend 2910456; FOI ready not sent; not TE-additive of 348bn; double_count vs Interwaas / PoAB / Vlaams Gewest possible",
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

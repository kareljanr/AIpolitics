# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/commitments.csv")
row = {
    "commitment_id": "comm_vrko_jr2025_pnl",
    "title": "VERKO JR2025 leftover waste IGS dual (assets 38.42m / omzet 26.15m / diensten 12.45m / debt 28.73m / PnL +6.6k)",
    "entity_id": "igs_vrko",
    "beneficiary": "VERKO / Berlare+Buggenhout+Dendermonde+Hamme+Laarne+Lebbeke+Melle+Wetteren+Wichelen vennoten",
    "legal_basis": "WVV opdrachthoudende vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
    "decision_date": "2026-06-09",
    "start_year": "1978",
    "end_year": "",
    "total_envelope_eur": "26146600",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00195553.pdf",
    "stated_goal": "Local leftover waste IGS map VL waste — 26.15m omzet / 12.45m diensten / 28.73m debt / PnL +6.6k",
    "cut_option": "Publish 18.55m per-gemeente omzet + 12.45m diensten split + 28.73m bank/lease counterpart + 5.22m herstel dossier + commissaris fee + named gemeente share; do not keep waste IGS as dual unpublished vehicle",
    "source_id": "src_vrko_jr2025_nbb",
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>IGS>VERKO>JR2025_L5",
    "notes": "tick1403; assets 38416495 omzet 26146600 diensten 12448633 pers 11760008 debt 28727165 voorzieningen 5233600 pnl 6578 equity 4455729 cash 3529851 capex 2165409; FOI ready not sent; not TE-additive of 348bn; double_count vs gemeente waste fees possible",
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

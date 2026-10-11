# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/commitments.csv")
row = {
    "commitment_id": "comm_iglg_jr2025_pnl",
    "title": "IGL JR2025 leftover zorg IGS dual (assets 65.30m / omzet 48.16m / pers 40.51m / debt 31.77m / PnL +2.30m)",
    "entity_id": "igs_iglg",
    "beneficiary": "IGL / Limburg municipalities + provincie vennoten / Ter Heide + LIV + Secretariaat",
    "legal_basis": "WVV opdrachthoudende vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
    "decision_date": "2026-06-25",
    "start_year": "1967",
    "end_year": "",
    "total_envelope_eur": "40508243",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00270170.pdf",
    "stated_goal": "Local leftover zorg IGS map VL disability-care — 48.16m omzet / 40.51m pers / 31.77m debt / PnL +2.30m",
    "cut_option": "Publish 6.10 geo + 40.23m VL werkingsopbrengsten per gemeente/centrum + 40.51m pers split + 31.77m debt counterpart/rate + 5.37m diensten + 8.22m capsub dossier + 9.50m deposito bank + named vennoten; do not keep zorg IGS as dual unpublished vehicle",
    "source_id": "src_iglg_jr2025_nbb",
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Limburg>IGS>IGL>JR2025_L5",
    "notes": "tick1400; assets 65298610 omzet 48156858 diensten 5366617 pers 40508243 debt 31766387 pnl 2298043 equity 33288549 cash 5894254 invest 9500000 capsub 8217525; FOI ready not sent; not TE-additive of 348bn; double_count vs gemeente/VAPH fees possible",
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

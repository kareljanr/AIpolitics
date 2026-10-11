# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/commitments.csv")
row = {
    "commitment_id": "comm_dds_jr2025_pnl",
    "title": "DDS JR2025 leftover streek IGS dual (assets 48.50m / othops 5.22m / inventory 12.79m / voorzieningen 7.85m / PnL -0.29m)",
    "entity_id": "igs_dds",
    "beneficiary": "DDS / Berlare+Buggenhout+Dendermonde+Hamme+Lebbeke+Wetteren+Wichelen+Zele vennoten + OV Verko + 2 politiezones",
    "legal_basis": "WVV dienstverlenende vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
    "decision_date": "2026-06-09",
    "start_year": "1970",
    "end_year": "",
    "total_envelope_eur": "5219038",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00188846.pdf",
    "stated_goal": "Local leftover streek IGS map VL development — 5.22m othops / 12.79m land bank / 7.85m voorzieningen / PnL -0.29m",
    "cut_option": "Publish 5.22m othops split + 12.79m inventory dossier + 7.85m voorzieningen dossier + 2.56m prepaid counterpart + commissaris fee + named gemeente share; do not keep streek IGS as dual unpublished vehicle",
    "source_id": "src_dds_jr2025_nbb",
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>IGS>DDS>JR2025_L5",
    "notes": "tick1402; assets 48501395 omzet 1262519 othops 5219038 diensten 1359141 pers 3875923 inventory 12793375 voorzieningen 7847265 pnl -287310 equity 38109541 cash 5533236 capex 789825; FOI ready not sent; not TE-additive of 348bn; double_count vs gemeente development/woon fees possible",
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

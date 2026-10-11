# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/commitments.csv")
row = {
    "commitment_id": "comm_otar_jr2025_pnl",
    "title": "Otary RS JR2025 leftover NV dual (assets 95.63m / omzet 12.43m / FVA 82.86m / dividend 14.47m / PnL +17.24m)",
    "entity_id": "nv_otar",
    "beneficiary": "Otary RS NV / 8x12.5pct aandeelhouders (Z-Kracht + Aspiravi + DEME + Elicio + Green Offshore + Power@Sea + Socofe + WE Environnement)",
    "legal_basis": "WVV NV publiek recht; Bestuursdecreet openbaarheid; NBB neerlegging",
    "decision_date": "2026-05-15",
    "start_year": "2011",
    "end_year": "",
    "total_envelope_eur": "14471000",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00254280.pdf",
    "stated_goal": "Local leftover NV map VL offshore-wind holding — 12.43m omzet / 14.47m dividend / 82.86m FVA / PnL +17.24m",
    "cut_option": "Publish 6.10 omzet split + 10.24m diensten + 14.47m dividend per 12.5pct aandeelhouder + Seastar/Mermaid FVA path + 11.00m achtergesteld counterpart/rate + 19.12m FVA income DROP; do not keep public-law NV as dual unpublished vehicle after PEZ/tender stop",
    "source_id": "src_otar_jr2025_nbb",
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>NV>OtaryRS>JR2025_L5",
    "notes": "tick1399; assets 95625285 omzet 12426978 diensten 10235828 debt 14121330 pnl 17237470 equity 81503955 div 14471000 fva 82864237 cash 10999623; FOI ready not sent; not TE-additive of 348bn; double_count vs ECO2050 1360 11m Otary loan possible",
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

# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/leaderboard.csv")
row = {
    "item_id": "lb_otar_omzet_12_43m_diensten_10_24m_div_14_47m",
    "name": "Otary RS JR2025 leftover NV: assets 95.63m / omzet 12.43m / diensten 10.24m / dividend 14.47m / 42.7 VTE",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>NV>OtaryRS>JR2025_L5",
    "annual_cost_eur": "14471000",
    "total_cost_eur": "95625285",
    "tco_notes": "Leftover dual Nuhma-adjacent public-law NV (offshore-wind holding Rentel/Seastar/Mermaid): assets 95.63m / equity 81.50m / pnl +17.24m DROP vs +62.77m / omzet 12.43m / diensten 10.24m / pers 5.15m / expl -1.69m / FVA 82.86m (Otary BIS 51pct + Rentel 52pct + verbonden vordering 10.25m) / LT achtergesteld 11.00m / cash JUMP 11.00m / dividend 14.47m DROP vs 63.01m / 42.7 VTE; 6.10 omzet category/geo empty; Seastar/Mermaid FVA path unpublished; official NBB WVV live; do not treat 95.63m as TE-additive of 348bn; double_count vs ECO2050 1360 11m possible",
    "confidence": "strong",
    "source_id": "src_otar_jr2025_nbb",
    "beneficiaries": "Otary RS NV / 8x12.5pct aandeelhouders incl Z-Kracht (Nuhma zetel) + Aspiravi + DEME + Elicio + Green Offshore + Power@Sea + Socofe + WE Environnement",
    "stated_goal": "Local leftover NV map VL offshore-wind holding — JR2025 live; dual omzet/diensten/dividend/FVA FOI",
    "measured_outcome": "Official NBB WVV 2026-08-19: assets 95.63m / omzet 12.43m / FVA 82.86m / dividend 14.47m / pnl +17.24m / 42.7 VTE",
    "absurdity_score": "7.4",
    "cost_score": "7.8",
    "difficulty": "2.8",
    "priority_index": "6.8",
    "cut_proposal": "Publish 6.10 omzet split + 10.24m diensten + 14.47m dividend per 12.5pct aandeelhouder + Seastar/Mermaid FVA path + 11.00m achtergesteld counterpart/rate + 19.12m FVA income DROP; do not keep public-law NV as dual unpublished vehicle after PEZ/tender stop",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1399; leftover Nuhma-adjacent public-law NV after leftover AGB/IGS hunt; FOI ready not sent; not TE-additive of 348bn; distinct from ECO2050 1360 and Nuhma cv 1356",
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
print("leaderboard", added)

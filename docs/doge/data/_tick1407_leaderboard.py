# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/leaderboard.csv")
row = {
    "item_id": "lb_ptri_omzet_empty_debt_4_57m_recv_1_57m",
    "name": "AGB Patri JR2025 leftover AGB: assets 9.69m / omzet empty / brutomarge 0.57m / debt 4.57m / recv 1.57m",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Vlaanderen>Limburg>Sint-Truiden>AGB_Patri>JR2025_L5",
    "annual_cost_eur": "574007",
    "total_cost_eur": "9688747",
    "tco_notes": "Leftover dual AGB (mined city Sint-Truiden cultuurcentra): assets 9.69m / equity 5.02m / pnl +0.08m / omzet empty / brutomarge 0.57m / diensten unpublished / pers empty / expl +0.12m / debt 4.57m / cash 0.38m / capex 0.13m / dividend 0.02m / commissaris unpublished; official NBB WVV live; do not treat 9.69m as TE-additive of 348bn; double_count vs Stad Sint-Truiden / AGOST possible",
    "confidence": "strong",
    "source_id": "src_ptri_jr2025_nbb",
    "beneficiaries": "AGB Patri / Stad Sint-Truiden / cultuurcentra",
    "stated_goal": "Local leftover AGB map VL Sint-Truiden — JR2025 live; dual omzet/diensten/recv/debt FOI",
    "measured_outcome": "Official NBB WVV 2026-08-19: assets 9.69m / omzet empty / brutomarge 0.57m / debt 4.57m / recv 1.57m / pnl +0.08m",
    "absurdity_score": "6.2",
    "cost_score": "5.4",
    "difficulty": "2.0",
    "priority_index": "5.8",
    "cut_proposal": "Publish omzet 70 + 60/61 split + pers 62/VTE + ST recv 1.57m counterpart + LT bank 3.40m terms + overige ST 0.22m + commissaris unpublished; do not keep leftover AGB as dual unpublished vehicle",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1407; leftover AGB of mined city Sint-Truiden after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined AGOST / Trupark / AGB Tielt 1405 / MLSO 1406",
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

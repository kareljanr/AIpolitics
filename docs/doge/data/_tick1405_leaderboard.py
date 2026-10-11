# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/leaderboard.csv")
row = {
    "item_id": "lb_tlt_omzet_empty_lease_9_30m_debt_11_90m",
    "name": "AGB Tielt JR2025 leftover AGB: assets 19.95m / brutomarge 0.68m / omzet empty / lease 9.30m / debt 11.90m",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Tielt>AGB_Tielt>JR2025_L5",
    "annual_cost_eur": "679356",
    "total_cost_eur": "19953810",
    "tco_notes": "Leftover dual AGB (mined city Tielt / sport+monumenten): assets 19.95m / equity 5.59m / pnl +0.32m / brutomarge 0.68m / omzet 70 empty / 60/61 empty / pers 62 empty / expl +0.31m / debt 11.90m / lease 9.30m / cash 1.13m / capex 0.39m / dividend 0.16m / commissaris unpublished; official NBB WVV live; do not treat 19.95m as TE-additive of 348bn; double_count vs gemeente sport fees possible",
    "confidence": "strong",
    "source_id": "src_tlt_jr2025_nbb",
    "beneficiaries": "AGB Tielt / Stad Tielt / sportaccommodaties + monumenten",
    "stated_goal": "Local leftover AGB map VL sport+monumenten — JR2025 live; dual omzet-empty/lease/debt FOI",
    "measured_outcome": "Official NBB WVV 2026-08-19: assets 19.95m / brutomarge 0.68m / omzet empty / lease 9.30m / debt 11.90m / pnl +0.32m",
    "absurdity_score": "6.5",
    "cost_score": "6.6",
    "difficulty": "2.5",
    "priority_index": "6.5",
    "cut_proposal": "Publish omzet 70 + 60/61 diensten split + 9.30m lease counterpart + 1.99m overige leningen + pers 62/VTE + commissaris; do not keep AGB as dual unpublished vehicle",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1405; leftover AGB of mined city Tielt after leftover AGB/IGS hunt; FOI ready not sent; not TE-additive of 348bn; distinct from WAGSO / AGB Oostkamp / AGB Sport Hulshout",
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

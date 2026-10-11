# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/leaderboard.csv")
row = {
    "item_id": "lb_ovco_omzet_empty_debt_6_31m_cip_0_98m",
    "name": "OVCO JR2025 leftover crematorium IGS: assets 9.37m / debt 6.31m / CIP 0.98m / omzet unpublished / 4.8 VTE",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>IGS>OVCO>JR2025_L5",
    "annual_cost_eur": "6313967",
    "total_cost_eur": "9368744",
    "tco_notes": "Leftover dual crematorium IGS (Polderbos of Oostende+Bredene+Middelkerke+Oudenburg): assets 9.37m / equity 3.05m / pnl +0.39m / omzet unpublished / brutomarge 1.16m / diensten unpublished / pers 0.46m / 4.8 VTE / YE 5.7 / expl +0.41m / debt 6.31m (LT bank/lease 5.61m; gov-guaranteed 5.99m) / cash 0.08m / invest 0.97m / CIP 0.98m / capsub 1.74m / dividend 0; official NBB WVV live; do not treat 9.37m as TE-additive of 348bn; double_count vs gemeente funeral fees possible",
    "confidence": "strong",
    "source_id": "src_ovco_jr2025_nbb",
    "beneficiaries": "OVCO / Oostende+Bredene+Middelkerke+Oudenburg vennoten / Crematorium Polderbos",
    "stated_goal": "Local leftover crematorium IGS map VL funeral — JR2025 live; dual omzet/debt/CIP FOI",
    "measured_outcome": "Official NBB WVV 2026-08-19: assets 9.37m / debt 6.31m / CIP 0.98m / omzet unpublished / pnl +0.39m / 4.8 VTE",
    "absurdity_score": "6.5",
    "cost_score": "6.4",
    "difficulty": "2.5",
    "priority_index": "6.3",
    "cut_proposal": "Publish omzet 70 + 60/61 split + 6.31m debt counterpart/rate/waarborg + 0.98m CIP dossier + 0.97m beleggingen bank + 1.74m capsub dossier + named vennoten share; do not keep crematorium IGS as dual unpublished vehicle",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1401; leftover crematorium IGS after leftover AGB/IGS hunt; FOI ready not sent; not TE-additive of 348bn; distinct from HAVICREM 1393 / Westlede 1394 / Hofheide 1395 / Pontes 1396 / IGL 1400",
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

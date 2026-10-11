# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/leaderboard.csv")
row = {
    "item_id": "lb_psln_omzet_empty_brutomarge_1_94m_debt_2_19m",
    "name": "Psilon JR2025 leftover crematorium IGS: assets 8.63m / brutomarge 1.94m / omzet empty / debt 2.19m / 9 VTE",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>IGS>Psilon>JR2025_L5",
    "annual_cost_eur": "1935397",
    "total_cost_eur": "8627377",
    "tco_notes": "Leftover dual crematorium IGS (22 West-Vlaanderen gemeenten / Uitzicht Kortrijk): assets 8.63m / equity 6.11m / pnl +0.50m / brutomarge 1.94m / omzet 70 empty / 60/61 empty / pers 0.88m / 9 VTE / expl +0.52m / debt 2.19m / cash 0.78m / voorzieningen 0.33m / capex 0.17m / dividend 0 / vennoten guarantee 6.20m; official NBB WVV live; do not treat 8.63m as TE-additive of 348bn; double_count vs gemeente funeral fees possible",
    "confidence": "strong",
    "source_id": "src_psln_jr2025_nbb",
    "beneficiaries": "Psilon / 22 West-Vlaanderen vennoten / crematorium Uitzicht",
    "stated_goal": "Local leftover crematorium IGS map VL funeral — JR2025 live; dual omzet-empty/diensten/debt FOI",
    "measured_outcome": "Official NBB WVV 2026-08-19: assets 8.63m / brutomarge 1.94m / omzet empty / debt 2.19m / pnl +0.50m / 9 VTE",
    "absurdity_score": "6.4",
    "cost_score": "6.2",
    "difficulty": "2.5",
    "priority_index": "6.3",
    "cut_proposal": "Publish omzet 70 + 60/61 diensten split + 2.19m bank counterpart + 6.20m vennoten guarantee named share + 0.33m herstel dossier + 5-6.8m energy-transit reserve plan; do not keep crematorium IGS as dual unpublished vehicle",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1404; leftover crematorium IGS after leftover AGB/IGS hunt; FOI ready not sent; not TE-additive of 348bn; distinct from HAVICREM 1393 / Westlede 1394 / Hofheide 1395 / Pontes 1396 / OVCO 1401",
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

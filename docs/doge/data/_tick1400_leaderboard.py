# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/leaderboard.csv")
row = {
    "item_id": "lb_iglg_omzet_48_16m_pers_40_51m_debt_31_77m",
    "name": "IGL JR2025 leftover zorg IGS: assets 65.30m / omzet 48.16m / pers 40.51m / debt 31.77m / 529.5 VTE",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Vlaanderen>Limburg>IGS>IGL>JR2025_L5",
    "annual_cost_eur": "40508243",
    "total_cost_eur": "65298610",
    "tco_notes": "Leftover dual zorg IGS (disability-care of Limburg municipalities + provincie): assets 65.30m / equity 33.29m / pnl +2.30m / omzet 48.16m (VL werkingsopbrengsten 40.23m) / diensten 5.37m / pers 40.51m / 529.5 VTE / YE 680 / expl +2.27m / debt 31.77m (LT bank 20.04m) / cash 5.89m / invest 9.50m / capsub 8.22m / hypotheekmandaat 28.72m / dividend 0; 6.10 geo empty; official NBB WVV live; do not treat 65.30m as TE-additive of 348bn; double_count vs gemeente/VAPH fees possible",
    "confidence": "strong",
    "source_id": "src_iglg_jr2025_nbb",
    "beneficiaries": "IGL / Limburg municipalities + provincie vennoten / Ter Heide + LIV + Secretariaat",
    "stated_goal": "Local leftover zorg IGS map VL disability-care — JR2025 live; dual omzet/pers/debt FOI",
    "measured_outcome": "Official NBB WVV 2026-08-19: assets 65.30m / omzet 48.16m / pers 40.51m / debt 31.77m / pnl +2.30m / 529.5 VTE",
    "absurdity_score": "6.8",
    "cost_score": "7.2",
    "difficulty": "2.6",
    "priority_index": "6.7",
    "cut_proposal": "Publish 6.10 geo + 40.23m VL werkingsopbrengsten per gemeente/centrum + 40.51m pers split + 31.77m debt counterpart/rate + 5.37m diensten + 8.22m capsub dossier + 9.50m deposito bank + named vennoten; do not keep zorg IGS as dual unpublished vehicle",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1400; leftover zorg IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from Fluvius Limburg 1388 / Nuhma / Otary RS 1399",
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

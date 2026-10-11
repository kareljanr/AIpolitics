# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/leaderboard.csv")
row = {
    "item_id": "lb_vrko_omzet_26_15m_diensten_12_45m_debt_28_73m",
    "name": "VERKO JR2025 leftover waste IGS: assets 38.42m / omzet 26.15m / diensten 12.45m / debt 28.73m / 191.5 VTE",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>IGS>VERKO>JR2025_L5",
    "annual_cost_eur": "26146600",
    "total_cost_eur": "38416495",
    "tco_notes": "Leftover dual waste IGS (9 Oost-Vlaanderen gemeenten): assets 38.42m / equity 4.46m thin / pnl +6.6k / omzet 26.15m / diensten 12.45m / pers 11.76m / 191.5 VTE / YE 190 / expl +0.69m / debt 28.73m / cash 3.53m JUMP / voorzieningen 5.23m / capex 2.17m / dividend 0; official NBB WVV live; do not treat 38.42m as TE-additive of 348bn; double_count vs gemeente waste fees possible",
    "confidence": "strong",
    "source_id": "src_vrko_jr2025_nbb",
    "beneficiaries": "VERKO / Berlare+Buggenhout+Dendermonde+Hamme+Laarne+Lebbeke+Melle+Wetteren+Wichelen",
    "stated_goal": "Local leftover waste IGS map VL waste — JR2025 live; dual omzet/diensten/debt FOI",
    "measured_outcome": "Official NBB WVV 2026-08-19: assets 38.42m / omzet 26.15m / diensten 12.45m / debt 28.73m / pnl +6.6k / 191.5 VTE",
    "absurdity_score": "6.8",
    "cost_score": "7.6",
    "difficulty": "2.5",
    "priority_index": "6.8",
    "cut_proposal": "Publish 18.55m per-gemeente omzet + 12.45m diensten split + 28.73m bank/lease counterpart + 5.22m herstel dossier + commissaris fee + named gemeente share; do not keep waste IGS as dual unpublished vehicle",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1403; leftover waste IGS after leftover AGB/IGS hunt; FOI ready not sent; not TE-additive of 348bn; distinct from DDS 1402 / IDM / IVM / ILvA / IVLA / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO",
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

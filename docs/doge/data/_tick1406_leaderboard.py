# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/leaderboard.csv")
row = {
    "item_id": "lb_mlso_omzet_24_04m_diensten_7_75m_interwaas_3_76m",
    "name": "MLSO JR2025 leftover IGS: assets 227.28m / omzet 24.04m / diensten 7.75m / Interwaas 3.76m / nrec 4.42m",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Waaslandhaven>MLSO>JR2025_L5",
    "annual_cost_eur": "24044090",
    "total_cost_eur": "227277417",
    "tco_notes": "Leftover dual IGS (mined Waasland / Vlaams Gewest / PoAB / haven-grond): assets 227.28m / equity 213.68m / pnl +7.70m / omzet 24.04m / diensten 7.75m / Interwaas 3.76m / nrec 4.42m / expl +7.32m / debt 13.59m / cash 24.92m / capex 0.26m / dividend 2.91m / commissaris 11635; official NBB WVV live; do not treat 227.28m as TE-additive of 348bn; double_count vs Interwaas / PoAB / Vlaams Gewest possible",
    "confidence": "strong",
    "source_id": "src_mlso_jr2025_nbb",
    "beneficiaries": "MLSO / Vlaams Gewest / Haven Antwerpen-Brugge / Interwaas / Waaslandhaven concessionarissen",
    "stated_goal": "Local leftover IGS map VL Waaslandhaven — JR2025 live; dual diensten/Interwaas/nrec FOI",
    "measured_outcome": "Official NBB WVV 2026-08-19: assets 227.28m / omzet 24.04m / diensten 7.75m / Interwaas 3.76m / nrec 4.42m / pnl +7.70m",
    "absurdity_score": "6.8",
    "cost_score": "7.4",
    "difficulty": "2.5",
    "priority_index": "6.8",
    "cut_proposal": "Publish 7.75m diensten split + 3.76m Interwaas booking + 4.42m nrec split + 6.82m overige schulden + named vennoten/dividend; do not keep IGS as dual unpublished vehicle",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1406; leftover IGS of mined Waasland after leftover AGB/IGS hunt; FOI ready not sent; not TE-additive of 348bn; distinct from Interwaas / IDM / Water-Link / Farys / Port of Antwerp-Bruges",
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

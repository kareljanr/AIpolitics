# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/leaderboard.csv")
row = {
    "item_id": "lb_dds_othops_5_22m_inv_12_79m_prov_7_85m",
    "name": "DDS JR2025 leftover streek IGS: assets 48.50m / othops 5.22m / inventory 12.79m / voorzieningen 7.85m / 40.6 VTE",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>IGS>DDS>JR2025_L5",
    "annual_cost_eur": "5219038",
    "total_cost_eur": "48501395",
    "tco_notes": "Leftover dual streek IGS (8 Oost-Vlaanderen gemeenten + OV Verko + 2 politiezones): assets 48.50m / equity 38.11m / pnl -0.29m / omzet 1.26m / othops 5.22m / diensten 1.36m / pers 3.88m / 40.6 VTE / YE 46 / expl -0.51m / debt 2.54m (no LT) / cash 5.53m DROP / inventory 12.79m land bank / voorzieningen 7.85m / prepaid 2.56m / capex 0.79m / dividend 0; official NBB WVV live; do not treat 48.50m as TE-additive of 348bn; double_count vs gemeente development/woon fees possible",
    "confidence": "strong",
    "source_id": "src_dds_jr2025_nbb",
    "beneficiaries": "DDS / Berlare+Buggenhout+Dendermonde+Hamme+Lebbeke+Wetteren+Wichelen+Zele / OV Verko / 2 politiezones",
    "stated_goal": "Local leftover streek IGS map VL development — JR2025 live; dual othops/inventory/voorzieningen FOI",
    "measured_outcome": "Official NBB WVV 2026-08-19: assets 48.50m / othops 5.22m / inventory 12.79m / voorzieningen 7.85m / pnl -0.29m / 40.6 VTE",
    "absurdity_score": "6.6",
    "cost_score": "7.2",
    "difficulty": "2.5",
    "priority_index": "6.5",
    "cut_proposal": "Publish 5.22m othops split + 12.79m inventory dossier + 7.85m voorzieningen dossier + 2.56m prepaid counterpart + commissaris fee + named gemeente share; do not keep streek IGS as dual unpublished vehicle",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1402; leftover streek IGS after leftover AGB/IGS hunt; FOI ready not sent; not TE-additive of 348bn; distinct from SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / OVCO 1401",
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

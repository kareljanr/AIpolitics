# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/leaderboard.csv")
row = {
    "item_id": "lb_ibeg_omzet_empty_div_3_50m_fva_96_37m",
    "name": "IGS IBEG JR2025 leftover IGS: assets 100.49m / omzet empty / FVA 96.37m / dividend 3.50m / 0 VTE",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>IGS>IBEG>JR2025_L5",
    "annual_cost_eur": "3500000",
    "total_cost_eur": "100488193",
    "tco_notes": "Leftover dual IGS energy holding 5 HV municipalities (Grimbergen/Machelen/Meise/Vilvoorde/Wemmel): assets 100.49m / equity 99.04m / pnl +1.28m / omzet unpublished / diensten 0.81m JUMP / FVA 96.37m (Fluvius HV 64.83m 21.48pct + VENTUM 9.26m 92.55pct + Publigas/Publi-T 13.29m) / loan to Fluvius HV 9.00m (facility 30m) / dividend 3.50m / debt 1.45m (no LT) / cash 1.84m / 0 VTE / statutory audit oordeel unpublished (6:116 only); official NBB WVV live; do not treat 100.49m as TE-additive of 348bn; double_count vs Fluvius HV 1387 possible",
    "confidence": "strong",
    "source_id": "src_ibeg_jr2025_nbb",
    "beneficiaries": "IGS IBEG / Grimbergen + Machelen + Meise + Vilvoorde + Wemmel (ibeg.be; leftover IGS energy holding HV)",
    "stated_goal": "Local leftover IGS map VL energy holding HV 5 gemeenten — JR2025 live; dual omzet/dividend/FVA FOI",
    "measured_outcome": "Official NBB WVV 2026-08-19: assets 100.49m / omzet empty / FVA 96.37m / dividend 3.50m / pnl +1.28m / 0 VTE",
    "absurdity_score": "7.0",
    "cost_score": "7.5",
    "difficulty": "3.0",
    "priority_index": "6.4",
    "cut_proposal": "Publish omzet + 809k diensten split + 3.50m dividend per vennoot + 96.37m FVA counterparts + 9.00m Fluvius HV loan terms + statutory audit oordeel; do not keep energy holding IGS as dual unpublished vehicle",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1398; leftover IGS IBEG energy holding IGS; FOI ready not sent; not TE-additive of 348bn; distinct from Fluvius HV 1387 and IGS IVEBICA 1397 / Pontes 1396 / Fluvius stack 1382-1391",
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

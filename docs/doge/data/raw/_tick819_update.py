# -*- coding: utf-8 -*-
"""Tick 819 — UGent Jaarverslag 2025 finance dual KU Leuven."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
utc = "2026-08-05T06:30:00Z"
ROOT = Path(__file__).resolve().parents[1]


def load_csv(name):
    p = ROOT / name
    with p.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r), r.fieldnames, p


def save_csv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def prio(a, c, d):
    return round((float(a) + float(c) + float(d)) / 3, 2)


ent_rows, ent_fields, ent_path = load_csv("entities.csv")
if not any(e.get("entity_id") == "ugent" for e in ent_rows):
    ent_rows.append(
        {
            "entity_id": "ugent",
            "name_nl": "Universiteit Gent",
            "name_fr": "Universite de Gand",
            "name_en": "Ghent University",
            "level": "L2",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.ugent.be",
            "foi_email": "openbaarheid@vlaanderen.be",
            "foi_postal": "https://www.vlaanderen.be/openbaarheid-van-bestuur",
            "notes": "Flemish university; dual KU Leuven tick819",
        }
    )
    save_csv(ent_path, ent_fields, ent_rows)
    print("entity ugent added")
else:
    print("entity ugent exists")

src_rows, src_fields, src_path = load_csv("sources.csv")
new_sources = [
    {
        "source_id": "src_ugent_jv2025",
        "title": "UGent Jaarverslag 2025 Balans en jaarrekening executive summary",
        "url": "https://secretariaat.rvb.ugent.be/jaarverslag/jaarverslag-2025/Jaarverslag2025-volledig.pdf",
        "publisher": "Universiteit Gent",
        "accessed_date": "2026-08-05",
        "source_class": "entity_accounts",
        "notes": "Strong tick819 primary 691p finance section: assets 1.376bn (2024 1.271bn); equity 901.8m solvency 65.6pct; provisions 104.3m; debt 369.6m; net cash ~643m; WC 473.1m; result +61.9m te bestemmen; analytical +35.9m cum surplus 652.6m; personnel ~667m; depreciation 62.9m; werkings share 29.7pct VL; index 8.4m klik 11.3m; IOF rev 22.4m (18.14+4 prior); dual KU Leuven 3.4bn",
    },
    {
        "source_id": "src_dual_ugent_kuleuven_tick819",
        "title": "Dual UGent 1.376bn vs KU Leuven 3.4bn university residual tick819",
        "url": "docs/doge/data/raw/ugent_jaarverslag_2025.pdf",
        "publisher": "DOGE synthesis",
        "accessed_date": "2026-08-05",
        "source_class": "synthesis",
        "notes": "Strong dual not TE-additive: UGent assets 1.376bn equity 902m result +62m vs KU Leuven 3.4bn equity 2.52bn research 782m",
    },
]
existing = {s["source_id"] for s in src_rows}
for s in new_sources:
    if s["source_id"] not in existing:
        src_rows.append(s)
save_csv(src_path, src_fields, src_rows)
print("sources ok")

bud_rows, bud_fields, bud_path = load_csv("budgets.csv")
new_buds = [
    ("bud_ugent_assets_2025", "ugent", 2025, 1376000000, "", "", "outturn", "src_ugent_jv2025", "strong", "Total assets YE2025 1.376bn (2024 1.271bn); tick819"),
    ("bud_ugent_assets_2024", "ugent", 2024, 1271000000, "", "", "outturn", "src_ugent_jv2025", "strong", "Total assets YE2024 1.271bn; tick819"),
    ("bud_ugent_fixed_assets_2025", "ugent", 2025, 558500000, "", "", "outturn", "src_ugent_jv2025", "strong", "Fixed assets 558.5m (+14.1m); tick819"),
    ("bud_ugent_auc_2025", "ugent", 2025, 51500000, "", "", "outturn", "src_ugent_jv2025", "strong", "Assets under construction 51.5m (+21.2m); tick819"),
    ("bud_ugent_current_assets_2025", "ugent", 2025, 817300000, "", "", "outturn", "src_ugent_jv2025", "strong", "Current assets 817.3m (+82.3m); tick819"),
    ("bud_ugent_investments_2025", "ugent", 2025, 572200000, "", "", "outturn", "src_ugent_jv2025", "strong", "Geldbeleggingen 572.2m (+30.4m); tick819"),
    ("bud_ugent_cash_2025", "ugent", 2025, 130600000, "", "", "outturn", "src_ugent_jv2025", "strong", "Liquide middelen 130.6m (+43.7m); tick819"),
    ("bud_ugent_equity_2025", "ugent", 2025, 901800000, "", "", "outturn", "src_ugent_jv2025", "strong", "Eigen vermogen 901.8m (+54.4m); solvency 65.6pct; tick819"),
    ("bud_ugent_provisions_2025", "ugent", 2025, 104300000, "", "", "outturn", "src_ugent_jv2025", "strong", "Provisions 104.3m (pensions ~60.8 + other ~43.5); tick819"),
    ("bud_ugent_debt_2025", "ugent", 2025, 369600000, "", "", "outturn", "src_ugent_jv2025", "strong", "Schulden 369.6m (+45.6m); ST 344.2 LT 25.5; tick819"),
    ("bud_ugent_project_prepayments_2025", "ugent", 2025, 189600000, "", "", "outturn", "src_ugent_jv2025", "strong", "Ontvangen vooruitbetalingen projecten 189.6m; tick819"),
    ("bud_ugent_net_cash_2025", "ugent", 2025, 643000000, "", "", "outturn", "src_ugent_jv2025", "strong", "Netto kaspositie ~643m (2024 577.5m); cash+invest-fin debt; tick819"),
    ("bud_ugent_working_capital_2025", "ugent", 2025, 473100000, "", "", "outturn", "src_ugent_jv2025", "strong", "Werkkapitaal 473.1m (2024 421m); tick819"),
    ("bud_ugent_result_2025", "ugent", 2025, 61900000, "", "", "outturn", "src_ugent_jv2025", "strong", "Resultaat boekjaar +61.9m te bestemmen overschot; tick819"),
    ("bud_ugent_analytical_result_2025", "ugent", 2025, 35900000, "", "", "outturn", "src_ugent_jv2025", "strong", "Analytisch resultaat +35.9m; cum surplus 652.6m; tick819"),
    ("bud_ugent_cum_surplus_2025", "ugent", 2025, 652600000, "", "", "outturn", "src_ugent_jv2025", "strong", "Gecumuleerd saldo 652.6m; tick819"),
    ("bud_ugent_personnel_costs_2025", "ugent", 2025, 667000000, "", "", "outturn", "src_ugent_jv2025", "strong", "Personeelskosten ca 667m largest cost; tick819"),
    ("bud_ugent_depreciation_2025", "ugent", 2025, 62900000, "", "", "outturn", "src_ugent_jv2025", "strong", "Afschrijvingen 62.9m; tick819"),
    ("bud_ugent_indexatie_effect_2025", "ugent", 2025, 8400000, "", "", "outturn", "src_ugent_jv2025", "strong", "Indexatie effect werkings 8.4m; tick819"),
    ("bud_ugent_klik_effect_2025", "ugent", 2025, 11300000, "", "", "outturn", "src_ugent_jv2025", "strong", "Klik 2pct VOW+VOZ effect 11.3m; tick819"),
    ("bud_ugent_iof_revenue_2025", "ugent", 2025, 22400000, "", "", "outturn", "src_ugent_jv2025", "strong", "IOF total revenue 22.4m (toelage 18.14 + 4m prior year book); tick819"),
    ("bud_ugent_werkings_share_pct_2025", "ugent", 2025, 297, "", "", "outturn", "src_ugent_jv2025", "strong", "UGent share of VL werkingsmiddelen 29.7pct (amount stores bps 297); tick819"),
    ("bud_dual_ugent_kuleuven_assets_2025", "gg_belgium", 2025, 1376000000, 1376000000, 3400000000, "synthesis", "src_dual_ugent_kuleuven_tick819", "strong", "Dual UGent 1.376bn vs KU Leuven 3.4bn assets; not TE-additive; tick819"),
]
existing_b = {b["budget_id"] for b in bud_rows}
for row in new_buds:
    d = dict(
        zip(
            [
                "budget_id",
                "entity_id",
                "year",
                "amount_eur",
                "amount_min_eur",
                "amount_max_eur",
                "basis",
                "source_id",
                "confidence",
                "notes",
            ],
            row,
        )
    )
    for k in ["year", "amount_eur", "amount_min_eur", "amount_max_eur"]:
        if d[k] != "" and d[k] is not None:
            d[k] = str(d[k])
    if d["budget_id"] not in existing_b:
        bud_rows.append(d)
save_csv(bud_path, bud_fields, bud_rows)
print("budgets", len(new_buds))

cmt_rows, cmt_fields, cmt_path = load_csv("commitments.csv")
new_cmts = [
    {
        "commitment_id": "cmt_ugent_balance_1_376bn_2025",
        "title": "UGent balance sheet 1.376bn YE2025 (equity 902m)",
        "entity_id": "ugent",
        "beneficiary": "University operations",
        "legal_basis": "UGent Jaarverslag 2025 finance executive summary",
        "decision_date": "2025-12-31",
        "start_year": "2024",
        "end_year": "2025",
        "total_envelope_eur": "1376000000",
        "cash_by_year": '{"assets_bn": 1.376, "equity_m": 901.8, "debt_m": 369.6, "net_cash_m": 643, "result_m": 61.9, "personnel_m": 667}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://secretariaat.rvb.ugent.be/jaarverslag/jaarverslag-2025/Jaarverslag2025-volledig.pdf",
        "stated_goal": "Solvent public research university",
        "cut_option": "Publish first-stream public grant FOI dual KU Leuven",
        "source_id": "src_ugent_jv2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Onderwijs>UGent",
        "notes": "tick819 dual KU Leuven 3.4bn",
    },
    {
        "commitment_id": "cmt_ugent_result_61_9m_2025",
        "title": "UGent book result +61.9m 2025 (analytical +35.9m)",
        "entity_id": "ugent",
        "beneficiary": "Destined reserves / operations",
        "legal_basis": "UGent JV2025",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "61900000",
        "cash_by_year": '{"book_m": 61.9, "analytical_m": 35.9, "cum_surplus_m": 652.6, "wedge_m": 26}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/ugent_jv2025_finance.txt",
        "stated_goal": "Positive operating performance",
        "cut_option": "Explain 26m bedrijfseconomisch vs analytisch wedge FOI",
        "source_id": "src_ugent_jv2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Onderwijs>UGent>result",
        "notes": "tick819 surplus not waste; transparency FOI",
    },
    {
        "commitment_id": "cmt_dual_ugent_kuleuven_tick819",
        "title": "Dual UGent 1.376bn vs KU Leuven 3.4bn residual",
        "entity_id": "gg_belgium",
        "beneficiary": "dual map",
        "legal_basis": "UGent JV + KU Leuven JV dual",
        "decision_date": "2026-08-05",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "1376000000",
        "cash_by_year": '{"ugent_bn": 1.376, "kul_bn": 3.4, "ugent_result_m": 61.9, "kul_research_m": 781.88}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/ugent_jaarverslag_2025.pdf",
        "stated_goal": "Dual residual map tick819",
        "cut_option": "Cross FOI public grant matrices",
        "source_id": "src_dual_ugent_kuleuven_tick819",
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>ugent_kuleuven",
        "notes": "tick819 not TE-additive",
    },
]
existing_c = {c["commitment_id"] for c in cmt_rows}
for c in new_cmts:
    if c["commitment_id"] not in existing_c:
        cmt_rows.append(c)
save_csv(cmt_path, cmt_fields, cmt_rows)
print("cmt", len(new_cmts))

lb_rows, lb_fields, lb_path = load_csv("leaderboard.csv")
new_lbs = [
    {
        "item_id": "lb_ugent_balance_1_376bn_2025",
        "name": "UGent balance sheet 1.376bn YE2025",
        "level": "L2",
        "type": "finance",
        "hierarchy_path": "Vlaanderen>Onderwijs>UGent",
        "annual_cost_eur": "0",
        "total_cost_eur": "1376000000",
        "tco_notes": "Strong JV2025; equity 902m solvency 65.6pct net cash 643m; FILTER pure annual stock; dual KU Leuven 3.4bn",
        "confidence": "strong",
        "source_id": "src_ugent_jv2025",
        "beneficiaries": "university system",
        "stated_goal": "Solvent public research university",
        "measured_outcome": "+105m assets YoY",
        "absurdity_score": "3.0",
        "cost_score": "8.5",
        "difficulty": "7.0",
        "priority_index": str(prio(3.0, 8.5, 7.0)),
        "cut_proposal": "First-stream grant FOI; dual KU Leuven matrix",
        "status": "active",
        "struck_reason": "",
        "notes": "tick819 stock",
    },
    {
        "item_id": "lb_ugent_personnel_667m_2025",
        "name": "UGent personnel costs ~667m 2025",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>Onderwijs>UGent>personnel",
        "annual_cost_eur": "667000000",
        "total_cost_eur": "0",
        "tco_notes": "Strong largest cost post; dual KU Leuven research 782m different perimeter",
        "confidence": "strong",
        "source_id": "src_ugent_jv2025",
        "beneficiaries": "staff",
        "stated_goal": "Deliver teaching and research",
        "measured_outcome": "ca 667m stated",
        "absurdity_score": "3.5",
        "cost_score": "8.5",
        "difficulty": "6.5",
        "priority_index": str(prio(3.5, 8.5, 6.5)),
        "cut_proposal": "FTE+grade FOI; public vs third-stream funded posts",
        "status": "active",
        "struck_reason": "",
        "notes": "tick819",
    },
    {
        "item_id": "lb_ugent_result_61_9m_surplus",
        "name": "UGent book surplus +61.9m 2025 (analytical +35.9m)",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>Onderwijs>UGent>result",
        "annual_cost_eur": "0",
        "total_cost_eur": "61900000",
        "tco_notes": "Strong positive result; 26m wedge bedrijfseconomisch vs analytisch FOI; cum surplus 652.6m; not pure waste",
        "confidence": "strong",
        "source_id": "src_ugent_jv2025",
        "beneficiaries": "reserves",
        "stated_goal": "Financial sustainability",
        "measured_outcome": "+61.9m book / +35.9m analytical",
        "absurdity_score": "4.0",
        "cost_score": "5.5",
        "difficulty": "4.0",
        "priority_index": str(prio(4.0, 5.5, 4.0)),
        "cut_proposal": "Explain wedge and destined surplus use FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick819 surplus transparency",
    },
    {
        "item_id": "lb_ugent_net_cash_643m",
        "name": "UGent net cash position ~643m YE2025",
        "level": "L5",
        "type": "finance",
        "hierarchy_path": "Vlaanderen>Onderwijs>UGent>liquidity",
        "annual_cost_eur": "0",
        "total_cost_eur": "643000000",
        "tco_notes": "Strong cash 130.6 + invest 572.2 - fin debt 59.35 ~643; opportunity cost of large liquidity vs teaching",
        "confidence": "strong",
        "source_id": "src_ugent_jv2025",
        "beneficiaries": "treasury buffer",
        "stated_goal": "Liquidity and investment buffer",
        "measured_outcome": "+65.5m vs 2024 577.5m",
        "absurdity_score": "5.0",
        "cost_score": "7.5",
        "difficulty": "5.0",
        "priority_index": str(prio(5.0, 7.5, 5.0)),
        "cut_proposal": "Policy on excess cash vs tuition/staffing FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick819 liquidity L5",
    },
    {
        "item_id": "lb_dual_ugent_kuleuven_tick819",
        "name": "Dual UGent 1.376bn vs KU Leuven 3.4bn residual",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Belgium>dual>ugent_kuleuven",
        "annual_cost_eur": "0",
        "total_cost_eur": "1376000000",
        "tco_notes": "Strong dual not TE-additive; primary both JV2025",
        "confidence": "strong",
        "source_id": "src_dual_ugent_kuleuven_tick819",
        "beneficiaries": "multi-channel",
        "stated_goal": "Dual residual map",
        "measured_outcome": "primary",
        "absurdity_score": "3.5",
        "cost_score": "8.5",
        "difficulty": "5.0",
        "priority_index": str(prio(3.5, 8.5, 5.0)),
        "cut_proposal": "Cross FOI public grant matrices",
        "status": "active",
        "struck_reason": "",
        "notes": "tick819",
    },
]
existing_l = {x["item_id"] for x in lb_rows}
for lb in new_lbs:
    if lb["item_id"] not in existing_l:
        lb_rows.append(lb)
save_csv(lb_path, lb_fields, lb_rows)
print("lb", [x["priority_index"] for x in new_lbs])

foi_rows, foi_fields, foi_path = load_csv("foi_queue.csv")
new_gap = {
    "gap_id": "gap_ugent_public_grant_matrix_l5",
    "hierarchy_path": "Vlaanderen>Onderwijs>UGent_L5",
    "entity_id": "ugent",
    "what_is_missing": (
        "Full statutory P&L 2025 with first-stream werkingsuitkering EUR; "
        "research spend total and public/private split; "
        "26m wedge between book result 61.9m and analytical 35.9m; "
        "policy on net cash 643m; personnel 667m FTE matrix; "
        "IOF/BOF detailed grants; dual KU Leuven comparable public-euro table"
    ),
    "why_it_matters": "1.376bn university book without clear public-euro matrix dual KU Leuven blocks HE waste ranking",
    "priority": "7",
    "recipient_body": "Universiteit Gent / Departement Onderwijs en Vorming",
    "recipient_email": "openbaarheid@vlaanderen.be",
    "recipient_postal": "https://www.vlaanderen.be/openbaarheid-van-bestuur",
    "draft_letter_path": "docs/doge/foi/drafts/gap_ugent_public_grant_matrix_l5.md",
    "status": "ready",
    "date_ready": "2026-08-05",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_ugent_balance_1_376bn_2025|cmt_ugent_result_61_9m_2025",
    "linked_leaderboard_id": "lb_ugent_balance_1_376bn_2025|lb_ugent_personnel_667m_2025|lb_ugent_net_cash_643m",
    "created_utc": utc,
    "updated_utc": utc,
    "notes": "tick819 primary JV2025; ready draft; do not send",
}
if not any(x.get("gap_id") == "gap_ugent_public_grant_matrix_l5" for x in foi_rows):
    foi_rows.append(new_gap)
save_csv(foi_path, foi_fields, foi_rows)
print("foi ok")

rq_rows, rq_fields, rq_path = load_csv("research_queue.csv")
for row in rq_rows:
    if row.get("task_id") == "rq_810":
        row["status"] = "done"
        row["updated_utc"] = utc
        row["notes"] = (
            "tick819 UGent JV2025 assets 1.376bn equity 902m result +61.9m personnel ~667m "
            "net cash 643m dual KU Leuven; FOI gap_ugent_public_grant_matrix_l5 ready"
        )
# spawn rq_811 as MANDATORY progress@820 next
if not any(x.get("task_id") == "rq_811" for x in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_811",
            "title": "MANDATORY progress@820 coverage % + waste top10 refresh",
            "sprint": "hole_fill",
            "priority": "10",
            "status": "open",
            "hierarchy_target": "L0",
            "entity_id": "gg_belgium",
            "instructions": (
                "MANDATORY at tick 820: refresh docs/doge/data/progress_every_10_ticks.md "
                "(layers A-E % of 347.956bn TE) and doge_waste_top10_current.md (top10 by priority_index); "
                "append log; no invent euros"
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": "spawned tick819 — progress@820 next tick",
        }
    )
if not any(x.get("task_id") == "rq_812" for x in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_812",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "After progress@820: dual L5 or unmined primary (local city, CoA residual, Entity II dual); "
                "prefer FOI-adjacent L5; skip rq_116; UGent+KU Leuven dual filled tick818-819"
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": "spawned tick819 after UGent dual",
        }
    )
save_csv(rq_path, rq_fields, rq_rows)
print("rq ok")

ls_rows, ls_fields, ls_path = load_csv("loop_state.csv")
ls_rows[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": utc,
    "last_unit_id": "rq_810",
    "ticks_completed": "819",
    "paused": "no",
    "notes": (
        "tick819 UGent 1.376bn equity902 result+62 personnel667 dual KU Leuven FOI; "
        "next rq_811 MANDATORY progress@820; rq_116 deferred"
    ),
}
save_csv(ls_path, ls_fields, ls_rows)
print("loop_state 819 OK")

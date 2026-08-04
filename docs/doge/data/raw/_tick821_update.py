# -*- coding: utf-8 -*-
"""Tick 821 — SOWAER comptes YE2025 residual dual BSCA/BAC airports."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
utc = "2026-08-05T07:30:00Z"
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


src_rows, src_fields, src_path = load_csv("sources.csv")
new_sources = [
    {
        "source_id": "src_sowaer_comptes_ye2025",
        "title": "SOWAER compte de resultats et bilan YE2025 (extract 07/07/2026)",
        "url": "docs/doge/data/raw/sowaer_comptes_2025.pdf",
        "publisher": "SOWAER / Wallonie airports holding",
        "accessed_date": "2026-08-05",
        "source_class": "entity_accounts",
        "notes": "Strong tick821 primary statutory: ventes YE2025 46.986m (YE2024 64.837m); op result -3.829m; net result +0.300m; assets 491.747m; equity 366.922m; capital 322.266m; capital subsidies 63.401m; debt 124.825m (LT 89.868 ST 27.338); cash 49.845m; corporeal fixed 374.366m; personnel 7.688m; depreciation 31.012m; reported loss carryforward -45.970m; dual BSCA/BAC residual",
    },
    {
        "source_id": "src_dual_sowaer_bsca_bac_tick821",
        "title": "Dual SOWAER YE2025 book vs BSCA/BAC airport residual tick821",
        "url": "docs/doge/data/raw/sowaer_comptes_2025.pdf",
        "publisher": "DOGE synthesis",
        "accessed_date": "2026-08-05",
        "source_class": "synthesis",
        "notes": "Strong dual not TE-additive: SOWAER assets 492m sales 47m dual prior BSCA 127m rev / BAC 828m rev class",
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
    ("bud_sowaer_sales_2025", "sowaer", 2025, 46985558, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Ventes et prestations YE2025 46.986m (YE2024 64.837m); tick821"),
    ("bud_sowaer_sales_2024", "sowaer", 2024, 64836954, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Ventes YE2024 64.837m; tick821"),
    ("bud_sowaer_gross_margin_2025", "sowaer", 2025, 40021444, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Marge brute YE2025 40.021m; tick821"),
    ("bud_sowaer_personnel_2025", "sowaer", 2025, 7687686, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Remunerations YE2025 7.688m; tick821"),
    ("bud_sowaer_depreciation_2025", "sowaer", 2025, 31011741, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Amortissements YE2025 31.012m; tick821"),
    ("bud_sowaer_services_goods_2025", "sowaer", 2025, 6964114, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Services et biens divers YE2025 6.964m; tick821"),
    ("bud_sowaer_op_result_2025", "sowaer", 2025, -3829251, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Resultat exploitation YE2025 -3.829m; tick821"),
    ("bud_sowaer_net_result_2025", "sowaer", 2025, 299618, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Resultat exercice YE2025 +0.300m (after financials); tick821"),
    ("bud_sowaer_net_result_2024", "sowaer", 2024, 7406412, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Resultat exercice YE2024 +7.406m; tick821"),
    ("bud_sowaer_assets_2025", "sowaer", 2025, 491746944, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Total actif YE2025 491.747m; tick821"),
    ("bud_sowaer_fixed_assets_2025", "sowaer", 2025, 412316998, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Actifs immobilises YE2025 412.317m; tick821"),
    ("bud_sowaer_corporeal_2025", "sowaer", 2025, 374366112, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Immobilisations corporelles YE2025 374.366m; tick821"),
    ("bud_sowaer_financial_fixed_2025", "sowaer", 2025, 37895551, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Immobilisations financieres YE2025 37.896m (stakes BSCA/Liege class); tick821"),
    ("bud_sowaer_equity_2025", "sowaer", 2025, 366921528, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Capitaux propres YE2025 366.922m; tick821"),
    ("bud_sowaer_capital_2025", "sowaer", 2025, 322266095, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Capital YE2025 322.266m; tick821"),
    ("bud_sowaer_capital_subsidies_2025", "sowaer", 2025, 63401473, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Subsides en capital YE2025 63.401m; tick821"),
    ("bud_sowaer_debt_2025", "sowaer", 2025, 124825416, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Dettes totales YE2025 124.825m; tick821"),
    ("bud_sowaer_debt_lt_2025", "sowaer", 2025, 89868449, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Dettes >1 an YE2025 89.868m; tick821"),
    ("bud_sowaer_debt_st_2025", "sowaer", 2025, 27338060, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Dettes <=1 an YE2025 27.338m; tick821"),
    ("bud_sowaer_cash_2025", "sowaer", 2025, 49844955, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Valeurs disponibles YE2025 49.845m; tick821"),
    ("bud_sowaer_loss_carryforward_2025", "sowaer", 2025, -45970456, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Resultat reporte YE2025 -45.970m; tick821"),
    ("bud_sowaer_fin_income_2025", "sowaer", 2025, 5701755, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Produits financiers recurrents YE2025 5.702m; tick821"),
    ("bud_sowaer_fin_charges_2025", "sowaer", 2025, 1588892, "", "", "outturn", "src_sowaer_comptes_ye2025", "strong", "Charges financieres recurrentes YE2025 1.589m; tick821"),
    ("bud_dual_sowaer_airports_tick821", "gg_belgium", 2025, 491746944, "", "", "synthesis", "src_dual_sowaer_bsca_bac_tick821", "strong", "Dual SOWAER 492m assets vs BSCA/BAC residual; not TE-additive; tick821"),
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
        "commitment_id": "cmt_sowaer_assets_492m_2025",
        "title": "SOWAER balance sheet 491.7m YE2025 (equity 366.9m)",
        "entity_id": "sowaer",
        "beneficiary": "Walloon airport infrastructure (BSCA/Liege stakes class)",
        "legal_basis": "SOWAER statutory accounts YE2025",
        "decision_date": "2025-12-31",
        "start_year": "2021",
        "end_year": "2025",
        "total_envelope_eur": "491746944",
        "cash_by_year": '{"assets_m": 491.7, "equity_m": 366.9, "debt_m": 124.8, "capital_subs_m": 63.4, "sales_m": 47.0, "net_m": 0.3}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/sowaer_comptes_2025.pdf",
        "stated_goal": "Own and finance Walloon airport infrastructure",
        "cut_option": "Publish stake book values BSCA/Liege FOI; dividend policy",
        "source_id": "src_sowaer_comptes_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Wallonie>Airports>SOWAER",
        "notes": "tick821 dual BSCA/BAC; sales drop vs 2024",
    },
    {
        "commitment_id": "cmt_sowaer_capital_subsidies_63m_2025",
        "title": "SOWAER capital subsidies stock 63.4m YE2025",
        "entity_id": "sowaer",
        "beneficiary": "Airport infra financing",
        "legal_basis": "Subsides en capital balance sheet",
        "decision_date": "2025-12-31",
        "start_year": "2015",
        "end_year": "2035",
        "total_envelope_eur": "63401473",
        "cash_by_year": '{"ye2024_m": 60.974, "ye2025_m": 63.401}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/sowaer_comptes_2025.pdf",
        "stated_goal": "Public capital support for airport assets",
        "cut_option": "No new capital subs without CBA FOI",
        "source_id": "src_sowaer_comptes_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Wallonie>Airports>SOWAER>capital_subs",
        "notes": "tick821 rising stock",
    },
    {
        "commitment_id": "cmt_dual_sowaer_airports_tick821",
        "title": "Dual SOWAER YE2025 vs BSCA/BAC residual",
        "entity_id": "gg_belgium",
        "beneficiary": "dual map",
        "legal_basis": "SOWAER accounts dual prior BSCA/BAC maps",
        "decision_date": "2026-08-05",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "491746944",
        "cash_by_year": '{"sowaer_assets_m": 491.7, "sowaer_sales_m": 47.0, "op_result_m": -3.8}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/sowaer_comptes_2025.pdf",
        "stated_goal": "Dual residual map tick821",
        "cut_option": "Cross FOI stake matrix",
        "source_id": "src_dual_sowaer_bsca_bac_tick821",
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>sowaer_airports",
        "notes": "tick821 not TE-additive",
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
        "item_id": "lb_sowaer_assets_492m_2025",
        "name": "SOWAER balance sheet 491.7m YE2025",
        "level": "L2",
        "type": "finance",
        "hierarchy_path": "Wallonie>Airports>SOWAER",
        "annual_cost_eur": "0",
        "total_cost_eur": "491746944",
        "tco_notes": "Strong statutory; equity 367m debt 125m capital-subs 63m; FILTER pure annual stock; dual BSCA/BAC",
        "confidence": "strong",
        "source_id": "src_sowaer_comptes_ye2025",
        "beneficiaries": "airport operators / WAL region",
        "stated_goal": "Airport infrastructure ownership",
        "measured_outcome": "Assets ~492m YE2025",
        "absurdity_score": "4.0",
        "cost_score": "7.5",
        "difficulty": "6.0",
        "priority_index": str(prio(4.0, 7.5, 6.0)),
        "cut_proposal": "Stake book values + dividend FOI; no silent capital subs",
        "status": "active",
        "struck_reason": "",
        "notes": "tick821 stock",
    },
    {
        "item_id": "lb_sowaer_op_loss_3_8m_2025",
        "name": "SOWAER operating loss 3.83m YE2025 (sales -28pct YoY)",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Wallonie>Airports>SOWAER>ops",
        "annual_cost_eur": "3829251",
        "total_cost_eur": "0",
        "tco_notes": "Strong: sales 47.0m vs 64.8m 2024; depreciation 31.0m dominates; net still +0.30m via financial income 5.7m",
        "confidence": "strong",
        "source_id": "src_sowaer_comptes_ye2025",
        "beneficiaries": "infra owner",
        "stated_goal": "Cover airport infra costs",
        "measured_outcome": "Op loss 3.8m; sales drop",
        "absurdity_score": "6.0",
        "cost_score": "4.0",
        "difficulty": "4.5",
        "priority_index": str(prio(6.0, 4.0, 4.5)),
        "cut_proposal": "Explain sales drop FOI; lease/concession revenue path",
        "status": "active",
        "struck_reason": "",
        "notes": "tick821",
    },
    {
        "item_id": "lb_sowaer_capital_subs_63m",
        "name": "SOWAER capital subsidies stock 63.4m YE2025",
        "level": "L5",
        "type": "subsidy",
        "hierarchy_path": "Wallonie>Airports>SOWAER>capital_subs",
        "annual_cost_eur": "0",
        "total_cost_eur": "63401473",
        "tco_notes": "Strong rising stock (61.0m YE2024 -> 63.4m); public capital support",
        "confidence": "strong",
        "source_id": "src_sowaer_comptes_ye2025",
        "beneficiaries": "SOWAER equity",
        "stated_goal": "Capital support airport assets",
        "measured_outcome": "+2.4m YoY stock",
        "absurdity_score": "5.5",
        "cost_score": "6.5",
        "difficulty": "5.0",
        "priority_index": str(prio(5.5, 6.5, 5.0)),
        "cut_proposal": "Publish annual capital-sub grants FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick821",
    },
    {
        "item_id": "lb_sowaer_loss_carry_46m",
        "name": "SOWAER reported loss carryforward 46.0m YE2025",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Wallonie>Airports>SOWAER>equity",
        "annual_cost_eur": "0",
        "total_cost_eur": "45970456",
        "tco_notes": "Strong resultats reportes -46.0m; historical losses still on equity",
        "confidence": "strong",
        "source_id": "src_sowaer_comptes_ye2025",
        "beneficiaries": "balance sheet",
        "stated_goal": "Absorb past losses",
        "measured_outcome": "Still -46m reported",
        "absurdity_score": "5.0",
        "cost_score": "5.5",
        "difficulty": "4.0",
        "priority_index": str(prio(5.0, 5.5, 4.0)),
        "cut_proposal": "Path to clear carryforward FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick821",
    },
    {
        "item_id": "lb_dual_sowaer_airports_tick821",
        "name": "Dual SOWAER 492m vs BSCA/BAC residual",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Belgium>dual>sowaer_airports",
        "annual_cost_eur": "0",
        "total_cost_eur": "491746944",
        "tco_notes": "Strong dual not TE-additive",
        "confidence": "strong",
        "source_id": "src_dual_sowaer_bsca_bac_tick821",
        "beneficiaries": "multi-channel",
        "stated_goal": "Dual residual map",
        "measured_outcome": "primary",
        "absurdity_score": "4.5",
        "cost_score": "7.0",
        "difficulty": "5.0",
        "priority_index": str(prio(4.5, 7.0, 5.0)),
        "cut_proposal": "Cross FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick821",
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
    "gap_id": "gap_sowaer_stakes_sales_l5",
    "hierarchy_path": "Wallonie>Airports>SOWAER_L5",
    "entity_id": "sowaer",
    "what_is_missing": (
        "Book values of financial fixed assets 37.9m (BSCA/Liege/other stakes); "
        "sales drop explanation 64.8m 2024 to 47.0m 2025 by revenue line; "
        "new capital subsidies +2.4m 2025 grantor and decision; "
        "debt schedule LT 89.9m; dividend/remonte path dual WAL treasury 20m class; "
        "missions deleguees residual EUR"
    ),
    "why_it_matters": "492m public airport holding with op loss and opaque stakes blocks dual airport waste map",
    "priority": "7",
    "recipient_body": "SOWAER / SPW Mobilite / ministre Aeroports Wallonie",
    "recipient_email": "",
    "recipient_postal": "https://www.wallonie.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_sowaer_stakes_sales_l5.md",
    "status": "ready",
    "date_ready": "2026-08-05",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_sowaer_assets_492m_2025|cmt_sowaer_capital_subsidies_63m_2025",
    "linked_leaderboard_id": "lb_sowaer_assets_492m_2025|lb_sowaer_op_loss_3_8m_2025|lb_sowaer_capital_subs_63m",
    "created_utc": utc,
    "updated_utc": utc,
    "notes": "tick821 primary YE2025 accounts; ready draft; do not send",
}
if not any(x.get("gap_id") == "gap_sowaer_stakes_sales_l5" for x in foi_rows):
    foi_rows.append(new_gap)
save_csv(foi_path, foi_fields, foi_rows)
print("foi ok")

rq_rows, rq_fields, rq_path = load_csv("research_queue.csv")
for row in rq_rows:
    if row.get("task_id") == "rq_812":
        row["status"] = "done"
        row["updated_utc"] = utc
        row["notes"] = (
            "tick821 SOWAER YE2025 assets 491.7m sales 47.0m op -3.8m net +0.3m "
            "capital-subs 63.4m dual BSCA/BAC; FOI gap_sowaer_stakes_sales_l5 ready"
        )
if not any(x.get("task_id") == "rq_813" for x in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_813",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual); "
                "prefer FOI-adjacent L5; skip rq_116; SOWAER YE2025 filled tick821"
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": "spawned tick821 after SOWAER dual airports",
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
    "last_unit_id": "rq_812",
    "ticks_completed": "821",
    "paused": "no",
    "notes": (
        "tick821 SOWAER YE2025 492m assets sales47 op-3.8 dual airports FOI; "
        "next rq_813 residual dual L5/local; progress@830 in 9; rq_116 deferred"
    ),
}
save_csv(ls_path, ls_fields, ls_rows)
print("loop_state 821 OK")

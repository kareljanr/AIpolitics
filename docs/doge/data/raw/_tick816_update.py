# -*- coding: utf-8 -*-
"""Tick 816 — Wallonie ExpGen BI2026 residual dual FWB Entity II."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
utc = "2026-08-05T05:00:00Z"
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
        "source_id": "src_wal_expgen_bi2026",
        "title": "Wallonie Expose general budget initial 2026 SPW Finances ExpGen",
        "url": "https://finances.wallonie.be/files/Budget%202026/Budget%202026/expose/ExpGen.pdf",
        "publisher": "SPW Finances / Gouvernement wallon",
        "accessed_date": "2026-08-05",
        "source_class": "budget",
        "notes": "Strong tick816 primary 189p: BI2026 recettes 18515.734m depenses 21335.748m solde brut -2820.014m SEC corrections +804.278m solde SEC -2015.736m (vs 2025ini -2286.495); interest path 1102m 2026 (1007m 2025); net primary spend -2.09pct; debt gross YE2024 27795m / 30.09.2025 30333m net 25514 / 27890m; EMTN 30bn; 2025 loans raised 3722m to Sep; SPW remun 736m; FEDER-FTJ EU 778m prog 374 projects 775.1m (UE 314.3 WAL 428 ops 32.8); dual FWB SEC residual",
    },
    {
        "source_id": "src_dual_wal_fwb_bi2026_tick816",
        "title": "Dual Wallonie BI2026 SEC -2.016bn vs FWB aju residual tick816",
        "url": "docs/doge/data/raw/wallonie_expgen_2026.pdf",
        "publisher": "DOGE synthesis",
        "accessed_date": "2026-08-05",
        "source_class": "synthesis",
        "notes": "Strong dual not TE-additive: WAL ExpGen SEC -2015.736m dual prior FWB CoA aju SEC -1.753bn class Entity II",
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
    ("bud_wal_recettes_bi2026", "wallonie_gov", 2026, 18515734000, "", "", "budgeted", "src_wal_expgen_bi2026", "strong", "WAL BI2026 recettes 18515.734m kEUR; tick816"),
    ("bud_wal_depenses_bi2026", "wallonie_gov", 2026, 21335748000, "", "", "budgeted", "src_wal_expgen_bi2026", "strong", "WAL BI2026 depenses 21335.748m; tick816"),
    ("bud_wal_recettes_bi2025", "wallonie_gov", 2025, 19123923000, "", "", "budgeted", "src_wal_expgen_bi2026", "strong", "WAL BI2025 ini recettes 19123.923m ExpGen compare; tick816"),
    ("bud_wal_depenses_bi2025", "wallonie_gov", 2025, 22029416000, "", "", "budgeted", "src_wal_expgen_bi2026", "strong", "WAL BI2025 ini depenses 22029.416m; tick816"),
    ("bud_wal_solde_brut_bi2026", "wallonie_gov", 2026, -2820014000, "", "", "budgeted", "src_wal_expgen_bi2026", "strong", "Solde brut a financer -2820.014m BI2026; tick816"),
    ("bud_wal_solde_sec_bi2026", "wallonie_gov", 2026, -2015736000, "", "", "budgeted", "src_wal_expgen_bi2026", "strong", "Solde SEC BI2026 -2015.736m after +804.278m corrections; tick816"),
    ("bud_wal_solde_sec_bi2025", "wallonie_gov", 2025, -2286495000, "", "", "budgeted", "src_wal_expgen_bi2026", "strong", "Solde SEC BI2025 ini -2286.495m; improvement +270.759m path; tick816"),
    ("bud_wal_sec_corrections_bi2026", "wallonie_gov", 2026, 804278000, "", "", "budgeted", "src_wal_expgen_bi2026", "strong", "SEC corrections +804.278m (sous-util 609 + OCPP 282.92 + other); tick816"),
    ("bud_wal_interest_bi2026", "wallonie_debt", 2026, 1102000000, "", "", "budgeted", "src_wal_expgen_bi2026", "strong", "Interest charges path Table3 1102m 2026 (1007m 2025); tick816"),
    ("bud_wal_interest_bi2025", "wallonie_debt", 2025, 1007000000, "", "", "budgeted", "src_wal_expgen_bi2026", "strong", "Interest charges 1007m 2025 Table3 primary spend calc; tick816"),
    ("bud_wal_primary_net_spend_2026", "wallonie_gov", 2026, 19056000000, "", "", "budgeted", "src_wal_expgen_bi2026", "strong", "Depenses primaires nettes 19056m 2026 (-2.09pct vs 19463m 2025); tick816"),
    ("bud_wal_primary_net_spend_2025", "wallonie_gov", 2025, 19463000000, "", "", "budgeted", "src_wal_expgen_bi2026", "strong", "Depenses primaires nettes 19463m 2025 Table3; tick816"),
    ("bud_wal_debt_gross_2024", "wallonie_debt", 2024, 27795185456, "", "", "outturn", "src_wal_expgen_bi2026", "strong", "Dette regionale brute YE2024 27795.185m; tick816"),
    ("bud_wal_debt_gross_20250930", "wallonie_debt", 2025, 30333276860, "", "", "outturn", "src_wal_expgen_bi2026", "strong", "Dette brute 30 Sep 2025 30333.277m; tick816"),
    ("bud_wal_debt_net_2024", "wallonie_debt", 2024, 25514030916, "", "", "outturn", "src_wal_expgen_bi2026", "strong", "Dette regionale nette YE2024 25514.031m; tick816"),
    ("bud_wal_debt_net_20250930", "wallonie_debt", 2025, 27890100841, "", "", "outturn", "src_wal_expgen_bi2026", "strong", "Dette nette 30 Sep 2025 27890.101m; tick816"),
    ("bud_wal_debt_lt_20250930", "wallonie_debt", 2025, 29539776860, "", "", "outturn", "src_wal_expgen_bi2026", "strong", "Dette LT 30 Sep 2025 29539.777m; tick816"),
    ("bud_wal_debt_st_20250930", "wallonie_debt", 2025, 793500000, "", "", "outturn", "src_wal_expgen_bi2026", "strong", "Dette CT 793.5m stable YE2024-Sep2025; tick816"),
    ("bud_wal_loans_raised_2025_sep", "wallonie_debt", 2025, 3722000000, "", "", "outturn", "src_wal_expgen_bi2026", "strong", "19 market loans raised 3722m to 30 Sep 2025; tick816"),
    ("bud_wal_emtn_ceiling_30bn", "wallonie_debt", 2025, 30000000000, "", "", "commitment", "src_wal_expgen_bi2026", "strong", "EMTN programme ceiling raised to 30bn EUR; tick816"),
    ("bud_wal_spw_remuneration_2026", "wallonie_gov", 2026, 736000000, "", "", "budgeted", "src_wal_expgen_bi2026", "strong", "SPW agent remunerations envelope 736m 2026 (replacement norm); tick816"),
    ("bud_wal_feder_ftj_eu_prog", "wallonie_gov", 2027, 778000000, "", "", "commitment", "src_wal_expgen_bi2026", "strong", "FEDER-FTJ EU envelope 778m Wallonie 2021-2027 programme; tick816"),
    ("bud_wal_feder_374_projects_total", "wallonie_gov", 2025, 775100000, "", "", "commitment", "src_wal_expgen_bi2026", "strong", "374 FEDER projects 775.1m (UE 314.3 + WAL 428 + ops 32.8); tick816"),
    ("bud_wal_feder_374_wal_share", "wallonie_gov", 2025, 428000000, "", "", "commitment", "src_wal_expgen_bi2026", "strong", "WAL share of 374 FEDER projects 428m; tick816"),
    ("bud_wal_structural_funds_3bn_class", "wallonie_gov", 2027, 3000000000, "", "", "commitment", "src_wal_expgen_bi2026", "medium", "Structural funds envelope >3bn cofinanced 2021-2027 (EU+WAL+FWB+COCOF+benef); class; tick816"),
    ("bud_wal_rrf_repower_rec_2026", "wallonie_gov", 2026, 834382000, "", "", "budgeted", "src_wal_expgen_bi2026", "strong", "RRF and Repower recettes 834.382m BI2026 (vs 1029.6m 2025); tick816"),
    ("bud_dual_wal_fwb_sec_tick816", "gg_belgium", 2026, -2015736000, "", "", "synthesis", "src_dual_wal_fwb_bi2026_tick816", "strong", "Dual WAL SEC -2015.736m vs FWB residual; not TE-additive; tick816"),
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
        "commitment_id": "cmt_wal_bi2026_sec_deficit_2_016bn",
        "title": "Wallonie BI2026 SEC deficit 2.016bn (spend 21.336bn)",
        "entity_id": "wallonie_gov",
        "beneficiary": "Region wallonne / debt markets",
        "legal_basis": "Budget initial 2026 decrees; ExpGen SPW Finances",
        "decision_date": "2025-10-20",
        "start_year": "2026",
        "end_year": "2026",
        "total_envelope_eur": "21335748000",
        "cash_by_year": '{"recettes_m": 18515.734, "depenses_m": 21335.748, "solde_brut_m": -2820.014, "sec_corr_m": 804.278, "solde_sec_m": -2015.736, "interest_m": 1102, "spw_remun_m": 736}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://finances.wallonie.be/files/Budget%202026/Budget%202026/expose/ExpGen.pdf",
        "stated_goal": "Regional budget with -2.09pct primary net spend path",
        "cut_option": "Publish L5 discretionary matrix; hold SPW 736m norm; debt path FOI",
        "source_id": "src_wal_expgen_bi2026",
        "confidence": "strong",
        "hierarchy_path": "Wallonie>Budget>BI2026",
        "notes": "tick816 dual FWB SEC residual",
    },
    {
        "commitment_id": "cmt_wal_debt_gross_30_3bn_202509",
        "title": "Wallonie gross debt 30.333bn at 30 Sep 2025 (net 27.890bn)",
        "entity_id": "wallonie_debt",
        "beneficiary": "Debt holders / refinancing",
        "legal_basis": "Regional debt management; EMTN 30bn",
        "decision_date": "2025-09-30",
        "start_year": "2024",
        "end_year": "2035",
        "total_envelope_eur": "30333276860",
        "cash_by_year": '{"gross_ye2024_m": 27795.2, "gross_202509_m": 30333.3, "net_ye2024_m": 25514.0, "net_202509_m": 27890.1, "loans_raised_2025_sep_m": 3722, "emtn_ceiling_bn": 30, "interest_2026_m": 1102}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/wallonie_expgen_2026.pdf",
        "stated_goal": "Finance regional deficit and refinancing",
        "cut_option": "Slow LT issuance; publish Maastricht consolidé path",
        "source_id": "src_wal_expgen_bi2026",
        "confidence": "strong",
        "hierarchy_path": "Wallonie>Debt",
        "notes": "tick816 gross +2.5bn YTD 2025 to Sep",
    },
    {
        "commitment_id": "cmt_wal_feder_374_projects_775m",
        "title": "WAL FEDER 374 projects 775.1m (WAL share 428m)",
        "entity_id": "wallonie_gov",
        "beneficiary": "Project operators / cohesion policy",
        "legal_basis": "FEDER-FTJ 2021-2027; ExpGen BI2026",
        "decision_date": "2025-01-01",
        "start_year": "2021",
        "end_year": "2027",
        "total_envelope_eur": "775100000",
        "cash_by_year": '{"total_m": 775.1, "ue_m": 314.3, "wal_m": 428.0, "ops_m": 32.8, "eu_prog_m": 778, "flex_2026_27_m": 86.876}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/wallonie_expgen_2026.pdf",
        "stated_goal": "Cohesion structural investment",
        "cut_option": "Named L5 project register FOI; avoid deadweight",
        "source_id": "src_wal_expgen_bi2026",
        "confidence": "strong",
        "hierarchy_path": "Wallonie>EU_funds>FEDER",
        "notes": "tick816 dual FTJ Charleroi/Mons residual prior",
    },
    {
        "commitment_id": "cmt_dual_wal_fwb_tick816",
        "title": "Dual WAL BI2026 SEC -2.016bn vs FWB residual",
        "entity_id": "gg_belgium",
        "beneficiary": "dual map",
        "legal_basis": "ExpGen WAL dual prior FWB CoA aju",
        "decision_date": "2026-08-05",
        "start_year": "2026",
        "end_year": "2026",
        "total_envelope_eur": "21335748000",
        "cash_by_year": '{"wal_sec_m": -2015.736, "wal_spend_bn": 21.336, "fwb_sec_class_bn": -1.75}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/wallonie_expgen_2026.pdf",
        "stated_goal": "Dual residual map tick816",
        "cut_option": "Cross Entity II FOI",
        "source_id": "src_dual_wal_fwb_bi2026_tick816",
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>wal_fwb_bi2026",
        "notes": "tick816 not TE-additive",
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
        "item_id": "lb_wal_bi2026_sec_deficit_2_016bn",
        "name": "Wallonie BI2026 SEC deficit 2.016bn (spend 21.34bn)",
        "level": "L1",
        "type": "budget",
        "hierarchy_path": "Wallonie>Budget>BI2026",
        "annual_cost_eur": "21335748000",
        "total_cost_eur": "2015736000",
        "tco_notes": "Strong ExpGen: spend 21.336bn rec 18.516bn SEC -2.016bn; primary net -2.09pct; dual FWB; not pure L5 waste but material deficit path",
        "confidence": "strong",
        "source_id": "src_wal_expgen_bi2026",
        "beneficiaries": "regional services / debt markets",
        "stated_goal": "Fund regional policies under EU primary-spend path",
        "measured_outcome": "SEC deficit improved vs 2025ini still multi-bn",
        "absurdity_score": "5.5",
        "cost_score": "9.5",
        "difficulty": "8.0",
        "priority_index": str(prio(5.5, 9.5, 8.0)),
        "cut_proposal": "Discretionary L5 freeze; debt issuance slowdown",
        "status": "active",
        "struck_reason": "",
        "notes": "tick816 L1 path dual Entity II",
    },
    {
        "item_id": "lb_wal_debt_gross_30_3bn",
        "name": "Wallonie gross debt 30.3bn Sep2025 (net 27.9bn)",
        "level": "L2",
        "type": "finance",
        "hierarchy_path": "Wallonie>Debt",
        "annual_cost_eur": "1102000000",
        "total_cost_eur": "30333276860",
        "tco_notes": "Strong: gross +2.54bn YE2024 to Sep2025; interest 1.102bn 2026; EMTN 30bn ceiling; FILTER pure annual top10 as stock",
        "confidence": "strong",
        "source_id": "src_wal_expgen_bi2026",
        "beneficiaries": "bondholders",
        "stated_goal": "Finance deficits and refinancing",
        "measured_outcome": "Debt rising faster than SEC path improvement",
        "absurdity_score": "6.5",
        "cost_score": "9.5",
        "difficulty": "7.5",
        "priority_index": str(prio(6.5, 9.5, 7.5)),
        "cut_proposal": "Publish Maastricht consolidé + UAP centralisation residual FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick816 stock + annual interest",
    },
    {
        "item_id": "lb_wal_interest_1_102bn_2026",
        "name": "Wallonie interest charges 1.102bn BI2026",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Wallonie>Debt>interest",
        "annual_cost_eur": "1102000000",
        "total_cost_eur": "0",
        "tco_notes": "Strong Table3 primary-spend calc; +95m vs 2025 1007m; pure annual debt service",
        "confidence": "strong",
        "source_id": "src_wal_expgen_bi2026",
        "beneficiaries": "creditors",
        "stated_goal": "Service regional debt",
        "measured_outcome": "Rising with stock",
        "absurdity_score": "5.0",
        "cost_score": "8.5",
        "difficulty": "7.0",
        "priority_index": str(prio(5.0, 8.5, 7.0)),
        "cut_proposal": "Primary surplus path; stop net new LT above amort",
        "status": "active",
        "struck_reason": "",
        "notes": "tick816 pure annual interest",
    },
    {
        "item_id": "lb_wal_spw_remun_736m_2026",
        "name": "SPW personnel remunerations envelope 736m 2026",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Wallonie>SPW>personnel",
        "annual_cost_eur": "736000000",
        "total_cost_eur": "0",
        "tco_notes": "Strong ExpGen/FP minister path: replacement norm caps remun at 736m then 731m to 2029; dual federal ambtenaren centralisation",
        "confidence": "strong",
        "source_id": "src_wal_expgen_bi2026",
        "beneficiaries": "SPW agents",
        "stated_goal": "Cap public employment cost",
        "measured_outcome": "Cap stated not full TCO",
        "absurdity_score": "4.0",
        "cost_score": "8.0",
        "difficulty": "5.5",
        "priority_index": str(prio(4.0, 8.0, 5.5)),
        "cut_proposal": "Publish FTE+grade matrix; hold non-normed replacements",
        "status": "active",
        "struck_reason": "",
        "notes": "tick816",
    },
    {
        "item_id": "lb_dual_wal_fwb_bi2026_tick816",
        "name": "Dual WAL SEC -2.016bn vs FWB residual",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Belgium>dual>wal_fwb_bi2026",
        "annual_cost_eur": "2015736000",
        "total_cost_eur": "0",
        "tco_notes": "Strong dual not TE-additive; primary ExpGen + prior FWB CoA",
        "confidence": "strong",
        "source_id": "src_dual_wal_fwb_bi2026_tick816",
        "beneficiaries": "multi-channel",
        "stated_goal": "Dual residual map",
        "measured_outcome": "primary",
        "absurdity_score": "5.5",
        "cost_score": "9.0",
        "difficulty": "6.0",
        "priority_index": str(prio(5.5, 9.0, 6.0)),
        "cut_proposal": "Cross Entity II FOI L5",
        "status": "active",
        "struck_reason": "",
        "notes": "tick816",
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
    "gap_id": "gap_wal_bi2026_l5_matrix",
    "hierarchy_path": "Wallonie>Budget>BI2026_L5",
    "entity_id": "wallonie_gov",
    "what_is_missing": (
        "Named L5 discretionary matrix BI2026 by DO/programme with CE/CL EUR "
        "(culture equality tourism cabinets UAP faculative grants); "
        "Maastricht consolidated debt path vs gross 30.3bn; "
        "UAP centralisation residual cash 2.25bn Sep2025 composition; "
        "SPW FTE+grade under 736m remun; FEDER 374 projects named top20 WAL 428m share; "
        "spending-review savings booked vs announced"
    ),
    "why_it_matters": (
        "21.3bn spend / 2.0bn SEC deficit / 30bn debt stock without public L5 end-lines blocks waste ranking"
    ),
    "priority": "8",
    "recipient_body": "SPW Finances / Gouvernement wallon / ministre Budget",
    "recipient_email": "",
    "recipient_postal": "https://www.wallonie.be (openbaarheid / transparence)",
    "draft_letter_path": "docs/doge/foi/drafts/gap_wal_bi2026_l5_matrix.md",
    "status": "ready",
    "date_ready": "2026-08-05",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_wal_bi2026_sec_deficit_2_016bn|cmt_wal_debt_gross_30_3bn_202509",
    "linked_leaderboard_id": "lb_wal_bi2026_sec_deficit_2_016bn|lb_wal_debt_gross_30_3bn|lb_wal_interest_1_102bn_2026",
    "created_utc": utc,
    "updated_utc": utc,
    "notes": "tick816 primary ExpGen BI2026; ready draft; do not send",
}
if not any(x.get("gap_id") == "gap_wal_bi2026_l5_matrix" for x in foi_rows):
    foi_rows.append(new_gap)
save_csv(foi_path, foi_fields, foi_rows)
print("foi ok")

rq_rows, rq_fields, rq_path = load_csv("research_queue.csv")
for row in rq_rows:
    if row.get("task_id") == "rq_807":
        row["status"] = "done"
        row["updated_utc"] = utc
        row["notes"] = (
            "tick816 WAL ExpGen BI2026 spend 21.336bn SEC -2.016bn debt gross 30.3bn interest 1.102bn; "
            "dual FWB; FOI gap_wal_bi2026_l5_matrix ready"
        )
if not any(x.get("task_id") == "rq_808" for x in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_808",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual); "
                "prefer FOI-adjacent L5; skip rq_116; WAL ExpGen BI2026 largely filled tick816"
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": "spawned tick816 after WAL ExpGen BI2026 dual",
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
    "last_unit_id": "rq_807",
    "ticks_completed": "816",
    "paused": "no",
    "notes": (
        "tick816 WAL ExpGen BI2026 21.3bn SEC-2.02bn debt30.3bn dual FWB FOI; "
        "next rq_808 residual dual L5/local; progress@820 in 4; rq_116 deferred"
    ),
}
save_csv(ls_path, ls_fields, ls_rows)
print("loop_state 816 OK")

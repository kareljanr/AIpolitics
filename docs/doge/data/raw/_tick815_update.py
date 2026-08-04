# -*- coding: utf-8 -*-
"""Tick 815 — CoA 2026_19 De Werkvennootschap study contracts dual GIP/Lantis."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
utc = "2026-08-05T04:30:00Z"
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
        "source_id": "src_ccrek_2026_19_dwv_studies",
        "title": "CoA De Werkvennootschap uitvoering studieopdrachten 2026_19 NL chamber 31 Mar 2026",
        "url": "https://www.ccrek.be/sites/default/files/Docs/2026_19_Werkvennootschap.pdf",
        "publisher": "Rekenhof",
        "accessed_date": "2026-08-05",
        "source_class": "court_of_audit",
        "notes": "Strong tick815 primary 73p Table1 excl VAT: R0 Noord award 35.728m spent Mar2025 85.405m revised study budget 103.6m; R0 Oost 3.520m/yr base spent 11.092m +3.7m quick wins same provider 2023; Brabantnet award 5.9m spent 11.064m excl new studies 8.75m (ringtram 0.1+airport tram 5.1+sneltram 3.6); R4 W/O award 12.093m spent 17.373m (+44pct); OP posts without competition ~9.4m R0 Noord class; DWV adapted budget 2025 invest 226.2m; 3 of 4 studies heavily overrun; dual GIP/WADR/Lantis residual",
    },
    {
        "source_id": "src_dual_dwv_gip_tick815",
        "title": "Dual DWV study overruns vs GIP WADR residual tick815",
        "url": "docs/doge/data/raw/ccrek_2026_19_werkvennootschap.pdf",
        "publisher": "DOGE synthesis",
        "accessed_date": "2026-08-05",
        "source_class": "synthesis",
        "notes": "Strong dual not TE-additive: CoA DWV study cost overruns dual prior GIP 3.685bn class and Lantis VAK residual",
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
    ("bud_dwv_invest_budget_2025", "de_werkvennootschap", 2025, 226200000, "", "", "budgeted", "src_ccrek_2026_19_dwv_studies", "strong", "DWV adapted budget 2025 investment uitgaven 226.2m CoA; tick815"),
    ("bud_dwv_r0_noord_award_2016", "de_werkvennootschap", 2016, 35728080, "", "", "commitment", "src_ccrek_2026_19_dwv_studies", "strong", "R0 Noord study award Table1 35.728m excl VAT Dec2016; tick815"),
    ("bud_dwv_r0_noord_spent_mar2025", "de_werkvennootschap", 2025, 85404605, "", "", "outturn", "src_ccrek_2026_19_dwv_studies", "strong", "R0 Noord study spent to Mar2025 85.405m excl VAT (>2x award); tick815"),
    ("bud_dwv_r0_noord_revised_budget_2023", "de_werkvennootschap", 2023, 103600000, "", "", "estimate", "src_ccrek_2026_19_dwv_studies", "strong", "R0 Noord revised total study budget estimate 103.6m 2023 (may not suffice); tick815"),
    ("bud_dwv_r0_noord_op_posts_9_4m", "de_werkvennootschap", 2025, 9400000, "", "", "outturn", "src_ccrek_2026_19_dwv_studies", "strong", "R0 Noord OP posts outside competition ~9.4m EOY Mar2025; tick815"),
    ("bud_dwv_r0_oost_award_annual", "de_werkvennootschap", 2018, 3519860, "", "", "commitment", "src_ccrek_2026_19_dwv_studies", "strong", "R0 Oost study award 3.520m per year base Table1; tick815"),
    ("bud_dwv_r0_oost_spent_mar2025", "de_werkvennootschap", 2025, 11092189, "", "", "outturn", "src_ccrek_2026_19_dwv_studies", "strong", "R0 Oost study spent Mar2025 11.092m excl VAT; tick815"),
    ("bud_dwv_r0_oost_quickwins_3_7m", "de_werkvennootschap", 2023, 3700000, "", "", "commitment", "src_ccrek_2026_19_dwv_studies", "strong", "R0 Oost additional 3.7m quick wins 2023 same provider without publication; tick815"),
    ("bud_dwv_brabantnet_award_2014", "de_werkvennootschap", 2014, 5900000, "", "", "commitment", "src_ccrek_2026_19_dwv_studies", "strong", "Brabantnet study award De Lijn consortium 5.9m 2014 (press/samenvatting); tick815"),
    ("bud_dwv_brabantnet_spent_mar2025", "de_werkvennootschap", 2025, 11063535, "", "", "outturn", "src_ccrek_2026_19_dwv_studies", "strong", "Brabantnet spent Mar2025 11.064m excl new/additional studies footnote; tick815"),
    ("bud_dwv_brabantnet_extra_studies_8_75m", "de_werkvennootschap", 2025, 8750000, "", "", "commitment", "src_ccrek_2026_19_dwv_studies", "strong", "Brabantnet additional/new studies 8.75m (ringtram 0.1 + luchthaventram 5.1 + sneltram 3.6); tick815"),
    ("bud_dwv_r4_award_2018", "de_werkvennootschap", 2018, 12093496, "", "", "commitment", "src_ccrek_2026_19_dwv_studies", "strong", "R4 West/Oost study award 12.093m Table1; tick815"),
    ("bud_dwv_r4_spent_mar2025", "de_werkvennootschap", 2025, 17373177, "", "", "outturn", "src_ccrek_2026_19_dwv_studies", "strong", "R4 spent Mar2025 17.373m (+43.7pct vs award); tick815"),
    ("bud_dwv_r4_plafond_uplift_5_6m", "de_werkvennootschap", 2023, 5600000, "", "", "commitment", "src_ccrek_2026_19_dwv_studies", "strong", "R4 study budget raised 5.6m above plafond; deelopdracht4 4.3->9.2m; tick815"),
    ("bud_dwv_four_studies_spent_mar2025", "de_werkvennootschap", 2025, 124933506, "", "", "outturn", "src_ccrek_2026_19_dwv_studies", "strong", "Sum four Table1 spent Mar2025 85.405+11.092+11.064+17.373=124.934m excl Brabantnet extra 8.75m; tick815"),
    ("bud_dwv_four_studies_plus_extra", "de_werkvennootschap", 2025, 133683506, "", "", "outturn", "src_ccrek_2026_19_dwv_studies", "strong", "Four studies spent + Brabantnet extra 8.75m ~133.684m Mar2025 class; tick815"),
    ("bud_dual_dwv_studies_tick815", "gg_belgium", 2025, 133683506, "", "", "synthesis", "src_dual_dwv_gip_tick815", "strong", "Dual DWV study spend class vs GIP residual; not TE-additive; tick815"),
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
        "commitment_id": "cmt_dwv_r0_noord_study_103_6m",
        "title": "DWV R0 Noord study 85.4m spent path to 103.6m revised",
        "entity_id": "de_werkvennootschap",
        "beneficiary": "Study consortium / WADR R0 Noord",
        "legal_basis": "Public procurement study contract; VL gov award Dec 2016; DWV takeover 2017",
        "decision_date": "2016-12-16",
        "start_year": "2016",
        "end_year": "2030",
        "total_envelope_eur": "103600000",
        "cash_by_year": '{"award_m": 35.728, "spent_mar2025_m": 85.405, "revised_2023_m": 103.6, "op_posts_m": 9.4}',
        "remaining_eur": "18195395",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/ccrek_2026_19_werkvennootschap.pdf",
        "stated_goal": "Studies for R0 North redesign multimodal WADR",
        "cut_option": "Cap OP posts; competitive re-tender scope; freeze beyond 103.6m without parliament",
        "source_id": "src_ccrek_2026_19_dwv_studies",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>MOW>DWV>R0_Noord_studies",
        "notes": "tick815 >2x award; uncertain if 103.6m suffices",
    },
    {
        "commitment_id": "cmt_dwv_four_studies_spent_133m",
        "title": "DWV four audited study packages ~133.7m spent class Mar2025",
        "entity_id": "de_werkvennootschap",
        "beneficiary": "Study providers R0/Brabantnet/R4",
        "legal_basis": "CoA sample four long-running study contracts",
        "decision_date": "2026-03-31",
        "start_year": "2014",
        "end_year": "2030",
        "total_envelope_eur": "133683506",
        "cash_by_year": '{"r0n_m": 85.405, "r0o_m": 11.092, "brabant_spent_m": 11.064, "brabant_extra_m": 8.75, "r4_m": 17.373, "quickwins_m": 3.7}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://www.ccrek.be/sites/default/files/Docs/2026_19_Werkvennootschap.pdf",
        "stated_goal": "Prepare complex VL infrastructure works",
        "cut_option": "Standardise change-order publication; enforce plafond; reduce single-provider lock-in",
        "source_id": "src_ccrek_2026_19_dwv_studies",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>MOW>DWV>studies_sample",
        "notes": "tick815 3 of 4 heavily overrun; all four delayed",
    },
    {
        "commitment_id": "cmt_dual_dwv_gip_tick815",
        "title": "Dual DWV study overruns vs GIP WADR residual",
        "entity_id": "gg_belgium",
        "beneficiary": "dual map",
        "legal_basis": "CoA 2026_19 dual prior GIP CoA residual",
        "decision_date": "2026-08-05",
        "start_year": "2016",
        "end_year": "2026",
        "total_envelope_eur": "133683506",
        "cash_by_year": '{"dwv_studies_m": 133.7, "dwv_invest_budget_2025_m": 226.2}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/ccrek_2026_19_werkvennootschap.pdf",
        "stated_goal": "Dual residual map tick815",
        "cut_option": "Cross FOI L5 change orders",
        "source_id": "src_dual_dwv_gip_tick815",
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>dwv_gip",
        "notes": "tick815 not TE-additive",
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
        "item_id": "lb_dwv_r0_noord_study_2x_overrun",
        "name": "DWV R0 Noord study 85.4m spent vs 35.7m award (path 103.6m)",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>MOW>DWV>R0_Noord",
        "annual_cost_eur": "0",
        "total_cost_eur": "85404605",
        "tco_notes": "Strong CoA: >2x award; OP posts 9.4m without competition; revised 103.6m may not suffice; pure study not works",
        "confidence": "strong",
        "source_id": "src_ccrek_2026_19_dwv_studies",
        "beneficiaries": "study consortium",
        "stated_goal": "R0 North redesign studies",
        "measured_outcome": "85.4m spent Mar2025",
        "absurdity_score": "8.0",
        "cost_score": "7.5",
        "difficulty": "5.5",
        "priority_index": str(prio(8.0, 7.5, 5.5)),
        "cut_proposal": "Hard cap at revised budget; recompete OP posts; publish monthly burn",
        "status": "active",
        "struck_reason": "",
        "notes": "tick815 high FOI priority study waste",
    },
    {
        "item_id": "lb_dwv_four_studies_133m_overrun",
        "name": "DWV four study packages ~133.7m spent class (3/4 heavy overruns)",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>MOW>DWV>studies",
        "annual_cost_eur": "0",
        "total_cost_eur": "133683506",
        "tco_notes": "Strong CoA sample; R4 +44pct; Brabantnet award 5.9 to 11+8.75; R0 Oost +3.7m same provider; all delayed",
        "confidence": "strong",
        "source_id": "src_ccrek_2026_19_dwv_studies",
        "beneficiaries": "external study providers",
        "stated_goal": "Prepare WADR/R4 infrastructure",
        "measured_outcome": "systematic overrun pattern",
        "absurdity_score": "7.5",
        "cost_score": "8.0",
        "difficulty": "6.0",
        "priority_index": str(prio(7.5, 8.0, 6.0)),
        "cut_proposal": "Change-order register public; plafond enforcement; dual-provider rule",
        "status": "active",
        "struck_reason": "",
        "notes": "tick815",
    },
    {
        "item_id": "lb_dwv_op_posts_no_competition_9_4m",
        "name": "DWV R0 Noord OP posts ~9.4m without competition",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>MOW>DWV>procurement",
        "annual_cost_eur": "0",
        "total_cost_eur": "9400000",
        "tco_notes": "Strong CoA: OP posts outside placement procedure always risky; dependency on providers",
        "confidence": "strong",
        "source_id": "src_ccrek_2026_19_dwv_studies",
        "beneficiaries": "incumbent service providers",
        "stated_goal": "Flexible expertise profiles",
        "measured_outcome": "9.4m OP posts Mar2025",
        "absurdity_score": "8.5",
        "cost_score": "6.0",
        "difficulty": "4.0",
        "priority_index": str(prio(8.5, 6.0, 4.0)),
        "cut_proposal": "Ban large OP posts; re-tender expertise lots",
        "status": "active",
        "struck_reason": "",
        "notes": "tick815 procurement L5",
    },
    {
        "item_id": "lb_dwv_r4_plafond_breach",
        "name": "DWV R4 study plafond breach +5.6m (spent 17.4m vs 12.1m award)",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>MOW>DWV>R4",
        "annual_cost_eur": "0",
        "total_cost_eur": "17373177",
        "tco_notes": "Strong CoA: plafond undermined by shifting work to uncapped deelopdracht4 4.3->9.2m",
        "confidence": "strong",
        "source_id": "src_ccrek_2026_19_dwv_studies",
        "beneficiaries": "study bureau",
        "stated_goal": "R4 primary road conversion studies",
        "measured_outcome": "+44pct vs award",
        "absurdity_score": "7.5",
        "cost_score": "6.5",
        "difficulty": "4.5",
        "priority_index": str(prio(7.5, 6.5, 4.5)),
        "cut_proposal": "Restore plafond as hard cap; no shift to uncapped lots",
        "status": "active",
        "struck_reason": "",
        "notes": "tick815",
    },
    {
        "item_id": "lb_dual_dwv_gip_tick815",
        "name": "Dual DWV study overruns vs GIP residual",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Belgium>dual>dwv_gip",
        "annual_cost_eur": "0",
        "total_cost_eur": "133683506",
        "tco_notes": "Strong dual not TE-additive; primary CoA DWV + prior GIP",
        "confidence": "strong",
        "source_id": "src_dual_dwv_gip_tick815",
        "beneficiaries": "multi-channel",
        "stated_goal": "Dual residual map",
        "measured_outcome": "primary",
        "absurdity_score": "6.5",
        "cost_score": "7.5",
        "difficulty": "5.0",
        "priority_index": str(prio(6.5, 7.5, 5.0)),
        "cut_proposal": "Cross FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick815",
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
    "gap_id": "gap_dwv_study_overruns_l5",
    "hierarchy_path": "Vlaanderen>MOW>DWV_studies_L5",
    "entity_id": "de_werkvennootschap",
    "what_is_missing": (
        "Full change-order register (verrekeningen/bijakten) EUR by study for R0 Noord/Oost Brabantnet R4 "
        "with dates and publication status; OP-post detail 9.4m named providers; "
        "cash forecast to completion vs 103.6m R0 Noord revised; "
        "quick-win 3.7m award file; plafond breach decision notes; "
        "dependency map top study providers share of DWV 226.2m invest budget"
    ),
    "why_it_matters": (
        "Study overruns >2x award on flagship WADR packages; procurement lock-in risk; "
        "FOI for L5 before works capex multiplies waste"
    ),
    "priority": "8",
    "recipient_body": "De Werkvennootschap / MOW / Vlaams Parlement openbaarheid",
    "recipient_email": "openbaarheid@vlaanderen.be",
    "recipient_postal": "https://www.vlaanderen.be/openbaarheid-van-bestuur",
    "draft_letter_path": "docs/doge/foi/drafts/gap_dwv_study_overruns_l5.md",
    "status": "ready",
    "date_ready": "2026-08-05",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_dwv_r0_noord_study_103_6m|cmt_dwv_four_studies_spent_133m",
    "linked_leaderboard_id": "lb_dwv_r0_noord_study_2x_overrun|lb_dwv_four_studies_133m_overrun",
    "created_utc": utc,
    "updated_utc": utc,
    "notes": "tick815 primary CoA 2026_19; ready draft; do not send",
}
if not any(x.get("gap_id") == "gap_dwv_study_overruns_l5" for x in foi_rows):
    foi_rows.append(new_gap)
save_csv(foi_path, foi_fields, foi_rows)
print("foi ok")

rq_rows, rq_fields, rq_path = load_csv("research_queue.csv")
for row in rq_rows:
    if row.get("task_id") == "rq_806":
        row["status"] = "done"
        row["updated_utc"] = utc
        row["notes"] = (
            "tick815 CoA 2026_19 DWV studies: R0 Noord 85.4/103.6m; four packs ~133.7m; "
            "OP 9.4m; dual GIP; FOI gap_dwv_study_overruns_l5 ready"
        )
if not any(x.get("task_id") == "rq_807" for x in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_807",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "Next residual: dual L5 or unmined primary (local city L5, CoA residual, Entity II dual); "
                "prefer FOI-adjacent L5; skip rq_116; DWV studies filled tick815"
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": "spawned tick815 after CoA DWV studies dual",
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
    "last_unit_id": "rq_806",
    "ticks_completed": "815",
    "paused": "no",
    "notes": (
        "tick815 CoA DWV studies R0 85.4/103.6m four~133.7m OP9.4 dual GIP FOI; "
        "next rq_807 residual dual L5/local; progress@820 in 5; rq_116 deferred"
    ),
}
save_csv(ls_path, ls_fields, ls_rows)
print("loop_state 815 OK")

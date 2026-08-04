# -*- coding: utf-8 -*-
"""Tick 813 — VMSW jaarrekening 2025 residual dual WAL housing."""
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
utc = "2026-08-05T03:30:00Z"
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


# --- sources ---
src_rows, src_fields, src_path = load_csv("sources.csv")
new_sources = [
    {
        "source_id": "src_vmsw_jr2025",
        "title": "VMSW Jaarrekening 2025 statutory accounts social housing finance",
        "url": "docs/doge/data/raw/vmsw_jr2025.pdf",
        "publisher": "Vlaamse Maatschappij voor Sociaal Wonen",
        "accessed_date": "2026-08-05",
        "source_class": "entity_accounts",
        "notes": "Strong tick813 primary: balance YE2025 12382.6m (vs 11872.8m 2024); profit 5.210m (vs -4.497m); loans outstanding 11603.0m; debt LT+ST 10360.8m (banks 2424.2 + other 7154.2); Flanders zero-interest FS3 draw 1000m 2025; capital subsidies stock 813.2m; credit-risk provision 24.9m (+2.7m); FS3 ristorno to sector 13.9m; Ukraine units grant 40.8m (38.1 allocated EOY2024); innov subsidies 23.8m; climate fund prem 26.0m; deposit guarantees 109.4m; software invest 3.9m; BOF Flanders top-up to -16m loss; dual WAL SWL housing class",
    },
    {
        "source_id": "src_dual_vmsw_wal_housing_tick813",
        "title": "Dual VMSW 12.4bn balance / 11.6bn loans vs WAL SWL housing residual tick813",
        "url": "docs/doge/data/raw/vmsw_jr2025.pdf",
        "publisher": "DOGE synthesis",
        "accessed_date": "2026-08-05",
        "source_class": "synthesis",
        "notes": "Strong dual not TE-additive: VMSW statutory mega-book dual prior WAL SWL+SWCS+FLW dep SEC ~702.8m class + VL BO loan auth 1.229bn; ESA CoA debt 3.12bn is different perimeter vs statutory 10.36bn debt",
    },
]
existing = {s["source_id"] for s in src_rows}
for s in new_sources:
    if s["source_id"] not in existing:
        src_rows.append(s)
save_csv(src_path, src_fields, src_rows)
print("sources", len(src_rows))

# --- budgets ---
bud_rows, bud_fields, bud_path = load_csv("budgets.csv")
new_buds = [
    ("bud_vmsw_balance_total_2025", "vmsw", 2025, 12382615327, "", "", "outturn", "src_vmsw_jr2025", "strong", "Balance total YE2025 12382.615m (vs 11872.8m YE2024); tick813"),
    ("bud_vmsw_balance_total_2024", "vmsw", 2024, 11872800000, "", "", "outturn", "src_vmsw_jr2025", "strong", "Balance total YE2024 11872.8m cited in JR2025; tick813"),
    ("bud_vmsw_profit_2025", "vmsw", 2025, 5210443, "", "", "outturn", "src_vmsw_jr2025", "strong", "Net profit 2025 5.210443m; tick813"),
    ("bud_vmsw_result_2024", "vmsw", 2024, -4497038, "", "", "outturn", "src_vmsw_jr2025", "strong", "Result YE2024 -4.497038m cited JR2025; tick813"),
    ("bud_vmsw_loans_outstanding_2025", "vmsw", 2025, 11602986211, "", "", "outturn", "src_vmsw_jr2025", "strong", "Uitstaande leningen / loan claims 11602.986m YE2025; tick813"),
    ("bud_vmsw_claims_lt_st_2025", "vmsw", 2025, 11640269107, "", "", "outturn", "src_vmsw_jr2025", "strong", "Vorderingen LT+ST 11640.269m YE2025; +364.2m vs 2024; tick813"),
    ("bud_vmsw_debt_total_statutory_2025", "vmsw", 2025, 10360779382, "", "", "outturn", "src_vmsw_jr2025", "strong", "Schulden LT+ST statutory 10360.779m; dual CoA ESA debt 3123.4m different perimeter; tick813"),
    ("bud_vmsw_debt_banks_2025", "vmsw", 2025, 2424156244, "", "", "outturn", "src_vmsw_jr2025", "strong", "Leningen bij kredietinstellingen 2424.156m YE2025; tick813"),
    ("bud_vmsw_debt_other_loans_2025", "vmsw", 2025, 7154154340, "", "", "outturn", "src_vmsw_jr2025", "strong", "Overige leningen 7154.154m (incl Flanders zero-interest systems); tick813"),
    ("bud_vmsw_fs3_draw_flanders_2025", "vmsw", 2025, 1000000000, "", "", "outturn", "src_vmsw_jr2025", "strong", "2025 VMSW drew 1bn zero-interest loans from Flanders for FS3; matches CoA new LT loan note; tick813"),
    ("bud_vmsw_capital_2025", "vmsw", 2025, 123643247, "", "", "outturn", "src_vmsw_jr2025", "strong", "Maatschappelijk kapitaal 123.643m; tick813"),
    ("bud_vmsw_reserves_result_2025", "vmsw", 2025, 877278130, "", "", "outturn", "src_vmsw_jr2025", "strong", "Reserves en resultaat 877.278m YE2025; tick813"),
    ("bud_vmsw_capital_subsidies_stock_2025", "vmsw", 2025, 813190051, "", "", "outturn", "src_vmsw_jr2025", "strong", "Kapitaalsubsidies stock 813.190m (no new capital subs for actors since 2016); tick813"),
    ("bud_vmsw_credit_risk_provision_2025", "vmsw", 2025, 24900000, "", "", "outturn", "src_vmsw_jr2025", "strong", "Credit-risk provision ~24.9m of 25.488m total provisions; +2.7m 2025; tick813"),
    ("bud_vmsw_provisions_total_2025", "vmsw", 2025, 25488364, "", "", "outturn", "src_vmsw_jr2025", "strong", "Provisions risks/costs 25.488m (credit 24.9 + disputes 0.6); tick813"),
    ("bud_vmsw_cash_2025", "vmsw", 2025, 349009547, "", "", "outturn", "src_vmsw_jr2025", "strong", "Liquide middelen 349.010m YE2025; tick813"),
    ("bud_vmsw_investments_2025", "vmsw", 2025, 262326140, "", "", "outturn", "src_vmsw_jr2025", "strong", "Geldbeleggingen 262.326m YE2025; tick813"),
    ("bud_vmsw_deposit_guarantees_2025", "vmsw", 2025, 109404566, "", "", "outturn", "src_vmsw_jr2025", "strong", "Huurwaarborgen RC 109.405m (+9.7m vs 2024); tick813"),
    ("bud_vmsw_fs3_ristorno_2025", "vmsw", 2025, 13900000, "", "", "outturn", "src_vmsw_jr2025", "strong", "FS3 ristorno returned to sector YE2025 ~13.9m; tick813"),
    ("bud_vmsw_ukraine_units_grant_cum", "vmsw", 2025, 40800000, "", "", "outturn", "src_vmsw_jr2025", "strong", "Ukraine housing units grant received cum 40.8m; 38.1m allocated EOY2024; 2025 ~87k costs no invest; tick813"),
    ("bud_vmsw_innov_project_subs_2025", "vmsw", 2025, 23821834, "", "", "outturn", "src_vmsw_jr2025", "strong", "Subsidies innovatieve projecten 23.822m YE2025; tick813"),
    ("bud_vmsw_climate_fund_prem_2025", "vmsw", 2025, 25957571, "", "", "outturn", "src_vmsw_jr2025", "strong", "Premies Vlaams Klimaatfonds 25.958m YE2025; tick813"),
    ("bud_vmsw_software_invest_2025", "vmsw", 2025, 3900000, "", "", "outturn", "src_vmsw_jr2025", "strong", "Software digitalisation invest 3.9m 2025; tick813"),
    ("bud_vmsw_operating_result_2025", "vmsw", 2025, -8100000, "", "", "outturn", "src_vmsw_jr2025", "strong", "Bedrijfsresultaat -8.1m 2025; tick813"),
    ("bud_vmsw_financial_result_2025", "vmsw", 2025, 9900000, "", "", "outturn", "src_vmsw_jr2025", "strong", "Financieel resultaat +9.9m 2025; tick813"),
    ("bud_vmsw_bof_loss_before_topup_2025", "vmsw", 2025, -16800000, "", "", "outturn", "src_vmsw_jr2025", "strong", "BOF financial loss -16.8m before deferred tax to -15.9m; Flanders tops FS3 to -16m since 2023; tick813"),
    ("bud_vmsw_gaf_financial_2025", "vmsw", 2025, 26700000, "", "", "outturn", "src_vmsw_jr2025", "strong", "GAF financial profit 26.7m (interest income 28.6 + invest 8.9; interest cost RC 10.8 + loans 9.7); tick813"),
    ("bud_vmsw_debt_to_vl_bof_2025", "vmsw", 2025, 10073316, "", "", "outturn", "src_vmsw_jr2025", "strong", "Schuld op Vlaanderen BOF-toelage afrekening 10.073m in favour of Flanders; tick813"),
    ("bud_vmsw_rc_st_positive_2025", "vmsw", 2025, 322300000, "", "", "outturn", "src_vmsw_jr2025", "strong", "RC korte termijn positive 322.3m (-130.3m vs YE2024); tick813"),
    ("bud_vmsw_rc_lt_invest_2026", "vmsw", 2026, 189600000, "", "", "outturn", "src_vmsw_jr2025", "strong", "For 2026 189.6m invested at VMSW on LT RC; tick813"),
    ("bud_dual_vmsw_wal_housing_tick813", "gg_belgium", 2025, 12382615327, "", "", "synthesis", "src_dual_vmsw_wal_housing_tick813", "strong", "Dual VMSW balance 12.38bn vs WAL housing dep class ~0.70bn not additive; tick813"),
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
print("budgets", len(bud_rows), "new", len(new_buds))

# --- commitments ---
cmt_rows, cmt_fields, cmt_path = load_csv("commitments.csv")
new_cmts = [
    {
        "commitment_id": "cmt_vmsw_loan_book_11_6bn_2025",
        "title": "VMSW outstanding social-housing loans 11.603bn YE2025",
        "entity_id": "vmsw",
        "beneficiary": "Woonmaatschappijen / social tenants via actors",
        "legal_basis": "VMSW decree; FS3 and legacy financing systems; VCO",
        "decision_date": "2025-12-31",
        "start_year": "2010",
        "end_year": "2060",
        "total_envelope_eur": "11602986211",
        "cash_by_year": '{"loans_outstanding_m": 11602.986, "claims_lt_st_m": 11640.269, "delta_claims_m": 364.2, "fs3_draw_2025_m": 1000}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/vmsw_jr2025.pdf",
        "stated_goal": "Finance social housing stock via WM loans",
        "cut_option": "Publish per-WM loan exposures; stress test credit-risk 24.9m provision",
        "source_id": "src_vmsw_jr2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Wonen>VMSW_loans",
        "notes": "tick813 statutory claims; dual CoA ESA perimeter different",
    },
    {
        "commitment_id": "cmt_vmsw_fs3_1bn_draw_2025",
        "title": "VMSW FS3 zero-interest draw from Flanders 1bn 2025",
        "entity_id": "vmsw",
        "beneficiary": "Woonmaatschappijen via FS3",
        "legal_basis": "FS3 financing system; Flanders loan to VMSW",
        "decision_date": "2025-01-01",
        "start_year": "2025",
        "end_year": "2055",
        "total_envelope_eur": "1000000000",
        "cash_by_year": '{"draw_2025_m": 1000, "ristorno_to_sector_m": 13.9, "bof_topup_to_m": -16}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/vmsw_jr2025.pdf",
        "stated_goal": "Fund FS3 social housing lending",
        "cut_option": "Track ristorno efficiency; publish FS3 allocation L5",
        "source_id": "src_vmsw_jr2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Wonen>VMSW_FS3",
        "notes": "tick813 dual BO loan auth 1bn path",
    },
    {
        "commitment_id": "cmt_vmsw_ukraine_units_40_8m",
        "title": "VMSW Ukraine temporary housing units grant cum 40.8m",
        "entity_id": "vmsw",
        "beneficiary": "Displaced persons / temporary social units",
        "legal_basis": "Flanders wartime housing measures via VMSW",
        "decision_date": "2022-01-01",
        "start_year": "2022",
        "end_year": "2026",
        "total_envelope_eur": "40800000",
        "cash_by_year": '{"received_cum_m": 40.8, "allocated_eoy2024_m": 38.1, "2025_invest_m": 0, "2025_costs_k": 87}',
        "remaining_eur": "2700000",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/vmsw_jr2025.pdf",
        "stated_goal": "Temporary housing for Ukrainian displaced",
        "cut_option": "Inventory residual units and reallocation",
        "source_id": "src_vmsw_jr2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Wonen>VMSW_ukraine_units",
        "notes": "tick813 residual toe te wijzen woonunits 2.74m class",
    },
    {
        "commitment_id": "cmt_dual_vmsw_wal_housing_tick813",
        "title": "Dual VMSW mega-book vs WAL housing residual",
        "entity_id": "gg_belgium",
        "beneficiary": "dual map",
        "legal_basis": "VMSW JR2025 dual prior SWL SEC maps",
        "decision_date": "2026-08-05",
        "start_year": "2025",
        "end_year": "2026",
        "total_envelope_eur": "12382615327",
        "cash_by_year": '{"vmsw_balance_bn": 12.38, "vmsw_loans_bn": 11.60, "wal_housing_dep_m_class": 702.8}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "docs/doge/data/raw/vmsw_jr2025.pdf",
        "stated_goal": "Dual residual map tick813",
        "cut_option": "Cross FOI L5 WM matrix",
        "source_id": "src_dual_vmsw_wal_housing_tick813",
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>vmsw_wal_housing",
        "notes": "tick813 not TE-additive",
    },
]
existing_c = {c["commitment_id"] for c in cmt_rows}
for c in new_cmts:
    if c["commitment_id"] not in existing_c:
        cmt_rows.append(c)
save_csv(cmt_path, cmt_fields, cmt_rows)
print("commitments", len(cmt_rows))

# --- leaderboard ---
lb_rows, lb_fields, lb_path = load_csv("leaderboard.csv")
new_lbs = [
    {
        "item_id": "lb_vmsw_loan_book_11_6bn_2025",
        "name": "VMSW outstanding social housing loans 11.6bn YE2025",
        "level": "L2",
        "type": "finance",
        "hierarchy_path": "Vlaanderen>Wonen>VMSW",
        "annual_cost_eur": "0",
        "total_cost_eur": "11602986211",
        "tco_notes": "Strong JR2025 claims; FILTER pure annual top10 as stock/finance book; dual CoA ESA debt 3.12bn different perimeter",
        "confidence": "strong",
        "source_id": "src_vmsw_jr2025",
        "beneficiaries": "woonmaatschappijen / social tenants",
        "stated_goal": "Social housing finance intermediary",
        "measured_outcome": "Claims +364.2m YoY",
        "absurdity_score": "4.0",
        "cost_score": "9.5",
        "difficulty": "7.0",
        "priority_index": str(prio(4.0, 9.5, 7.0)),
        "cut_proposal": "Publish per-WM exposures and NPL; stress credit-risk provision",
        "status": "active",
        "struck_reason": "",
        "notes": "tick813 stock class",
    },
    {
        "item_id": "lb_vmsw_fs3_1bn_draw_2025",
        "name": "VMSW FS3 Flanders zero-interest draw 1bn 2025",
        "level": "L5",
        "type": "finance",
        "hierarchy_path": "Vlaanderen>Wonen>VMSW_FS3",
        "annual_cost_eur": "0",
        "total_cost_eur": "1000000000",
        "tco_notes": "Strong JR2025; opportunity cost of zero-interest public capital; ristorno 13.9m to sector; BOF top-up to -16m loss",
        "confidence": "strong",
        "source_id": "src_vmsw_jr2025",
        "beneficiaries": "woonmaatschappijen via FS3",
        "stated_goal": "Fund social rental finance FS3",
        "measured_outcome": "1bn drawn 2025",
        "absurdity_score": "5.5",
        "cost_score": "9.0",
        "difficulty": "6.0",
        "priority_index": str(prio(5.5, 9.0, 6.0)),
        "cut_proposal": "Full FS3 allocation L5 FOI; price opportunity cost",
        "status": "active",
        "struck_reason": "",
        "notes": "tick813",
    },
    {
        "item_id": "lb_vmsw_capital_subsidies_813m",
        "name": "VMSW capital subsidies stock 813m (frozen post-2016)",
        "level": "L5",
        "type": "subsidy",
        "hierarchy_path": "Vlaanderen>Wonen>VMSW_capital_subs",
        "annual_cost_eur": "0",
        "total_cost_eur": "813190051",
        "tco_notes": "Strong stock; no new capital subs for actors since 2016; dual Ukraine 34.6m capital-sub class in notes",
        "confidence": "strong",
        "source_id": "src_vmsw_jr2025",
        "beneficiaries": "legacy social housing actors",
        "stated_goal": "Historic capital support stock",
        "measured_outcome": "Stock 813.2m",
        "absurdity_score": "4.5",
        "cost_score": "8.0",
        "difficulty": "5.0",
        "priority_index": str(prio(4.5, 8.0, 5.0)),
        "cut_proposal": "Amortisation transparency; no silent reopen",
        "status": "active",
        "struck_reason": "",
        "notes": "tick813 stock",
    },
    {
        "item_id": "lb_vmsw_ukraine_units_40_8m",
        "name": "VMSW Ukraine temporary units grant 40.8m cum",
        "level": "L5",
        "type": "subsidy",
        "hierarchy_path": "Vlaanderen>Wonen>VMSW_ukraine",
        "annual_cost_eur": "0",
        "total_cost_eur": "40800000",
        "tco_notes": "Strong: 38.1m allocated EOY2024; 2025 no invest ~87k costs; residual toe te wijzen 2.74m class",
        "confidence": "strong",
        "source_id": "src_vmsw_jr2025",
        "beneficiaries": "temporary displaced housing",
        "stated_goal": "Emergency housing capacity",
        "measured_outcome": "Units purchased; residual unallocated",
        "absurdity_score": "5.0",
        "cost_score": "5.5",
        "difficulty": "4.0",
        "priority_index": str(prio(5.0, 5.5, 4.0)),
        "cut_proposal": "Public unit inventory and reallocation plan",
        "status": "active",
        "struck_reason": "",
        "notes": "tick813",
    },
    {
        "item_id": "lb_vmsw_credit_risk_prov_24_9m",
        "name": "VMSW credit-risk provision 24.9m (+2.7m 2025)",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Vlaanderen>Wonen>VMSW_credit_risk",
        "annual_cost_eur": "2700000",
        "total_cost_eur": "24900000",
        "tco_notes": "Strong provision on 11.6bn loan book (~0.2pct); annual add 2.7m; dual transparency on NPL",
        "confidence": "strong",
        "source_id": "src_vmsw_jr2025",
        "beneficiaries": "VMSW balance sheet buffer",
        "stated_goal": "Cover WM credit risk",
        "measured_outcome": "Provision level only",
        "absurdity_score": "4.0",
        "cost_score": "4.5",
        "difficulty": "3.5",
        "priority_index": str(prio(4.0, 4.5, 3.5)),
        "cut_proposal": "Publish default rates by WM",
        "status": "active",
        "struck_reason": "",
        "notes": "tick813",
    },
    {
        "item_id": "lb_dual_vmsw_wal_housing_tick813",
        "name": "Dual VMSW 12.4bn book vs WAL housing residual",
        "level": "L5",
        "type": "ops",
        "hierarchy_path": "Belgium>dual>vmsw_wal_housing",
        "annual_cost_eur": "0",
        "total_cost_eur": "12382615327",
        "tco_notes": "Strong dual not TE-additive; primary VMSW JR + prior WAL SEC",
        "confidence": "strong",
        "source_id": "src_dual_vmsw_wal_housing_tick813",
        "beneficiaries": "multi-channel",
        "stated_goal": "Dual residual map",
        "measured_outcome": "primary",
        "absurdity_score": "4.5",
        "cost_score": "9.0",
        "difficulty": "5.0",
        "priority_index": str(prio(4.5, 9.0, 5.0)),
        "cut_proposal": "Cross FOI WM matrix",
        "status": "active",
        "struck_reason": "",
        "notes": "tick813",
    },
]
existing_l = {x["item_id"] for x in lb_rows}
for lb in new_lbs:
    if lb["item_id"] not in existing_l:
        lb_rows.append(lb)
save_csv(lb_path, lb_fields, lb_rows)
print("leaderboard", len(lb_rows), [x["priority_index"] for x in new_lbs])

# --- FOI ---
foi_rows, foi_fields, foi_path = load_csv("foi_queue.csv")
new_gap = {
    "gap_id": "gap_vmsw_fs3_wm_matrix_l5",
    "hierarchy_path": "Vlaanderen>Wonen>VMSW_FS3_L5",
    "entity_id": "vmsw",
    "what_is_missing": (
        "FS3 and legacy loan exposures by woonmaatschappij (outstanding, 2025 draws, arrears/NPL); "
        "FS3 ristorno calculation detail 13.9m; credit-risk provision methodology and defaults; "
        "Ukraine units inventory residual of 40.8m grant (locations, occupancy, reallocation); "
        "innovative project subsidies 23.8m named beneficiaries; climate fund premiums 26.0m named; "
        "reconciliation note statutory debt 10.36bn vs CoA ESA VMSW debt 3.12bn"
    ),
    "why_it_matters": (
        "11.6bn loan book is material public social-housing finance; L5 opacity blocks waste ranking "
        "and dual VL/WAL housing compare"
    ),
    "priority": "8",
    "recipient_body": "VMSW / Agentschap Wonen Vlaanderen / Vlaams Parlement openbaarheid",
    "recipient_email": "openbaarheid@vlaanderen.be",
    "recipient_postal": "https://www.vlaanderen.be/openbaarheid-van-bestuur",
    "draft_letter_path": "docs/doge/foi/drafts/gap_vmsw_fs3_wm_matrix_l5.md",
    "status": "ready",
    "date_ready": "2026-08-05",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_vmsw_loan_book_11_6bn_2025|cmt_vmsw_fs3_1bn_draw_2025|cmt_vmsw_ukraine_units_40_8m",
    "linked_leaderboard_id": "lb_vmsw_loan_book_11_6bn_2025|lb_vmsw_fs3_1bn_draw_2025|lb_vmsw_ukraine_units_40_8m",
    "created_utc": utc,
    "updated_utc": utc,
    "notes": "tick813 primary VMSW JR2025; ready draft; do not send",
}
if not any(x.get("gap_id") == "gap_vmsw_fs3_wm_matrix_l5" for x in foi_rows):
    foi_rows.append(new_gap)
save_csv(foi_path, foi_fields, foi_rows)
print("foi", len(foi_rows))

# --- research_queue ---
rq_rows, rq_fields, rq_path = load_csv("research_queue.csv")
for row in rq_rows:
    if row.get("task_id") == "rq_804":
        row["status"] = "done"
        row["updated_utc"] = utc
        row["notes"] = (
            "tick813 VMSW JR2025 balance 12.38bn loans 11.60bn FS3 1bn draw debt statutory 10.36bn; "
            "dual WAL housing; FOI gap_vmsw_fs3_wm_matrix_l5 ready"
        )
if not any(x.get("task_id") == "rq_805" for x in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_805",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "Next residual: dual L5 or unmined primary (local city L5 residual, CoA residual "
                "extract, Entity II dual); prefer FOI-adjacent L5; skip rq_116; VMSW JR largely filled tick813"
            ),
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": "spawned tick813 after VMSW JR2025 dual",
        }
    )
save_csv(rq_path, rq_fields, rq_rows)
print("rq 804 done + 805")

# --- loop_state ---
ls_rows, ls_fields, ls_path = load_csv("loop_state.csv")
ls_rows[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": utc,
    "last_unit_id": "rq_804",
    "ticks_completed": "813",
    "paused": "no",
    "notes": (
        "tick813 VMSW JR 12.38bn/11.6bn loans FS3 1bn dual WAL FOI; "
        "next rq_805 residual dual L5/local; progress@820 in 7; rq_116 deferred"
    ),
}
save_csv(ls_path, ls_fields, ls_rows)
print("loop_state 813 OK")

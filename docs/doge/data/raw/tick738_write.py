# tick738 — VWF Activiteitenverslag 2025 residual dual SWCS/FLW (rq_729)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T06:15:00Z"
URL_AV = "https://www.vlaamswoningfonds.be/sites/default/files/field_download_file/2026-03/Activiteitenverslag%202025.pdf"
URL_JR = "https://www.vlaamswoningfonds.be/sites/default/files/field_download_file/2026-05/Jaarrekening%20NBB%202025.pdf"
URL_DL = "https://www.vlaamswoningfonds.be/downloads"

SRC = "src_vwf_av2025_residual"
SRC_JR = "src_vwf_jr2025_nbb"
SRC_DUAL = "src_dual_vwf_swcs_flw_tick738"

# --- entity ---
ent_path = DATA / "entities.csv"
with open(ent_path, encoding="utf-8", newline="") as f:
    er = csv.DictReader(f)
    efields = list(er.fieldnames or [])
    ents = list(er)
for e in ents:
    if e.get("entity_id") == "vwf":
        e["notes"] = (
            "VWF residual tick738 AV2025: auth 1.7bn woonlening + 20m huurwaarborg; "
            "prod 7057 loans 1.632bn avg 231k @2.48pct; portfolio 71.6k / 9.698bn; "
            "BS assets 10.003bn debt 9.730bn bonds 4.865bn; dual SWCS/FLW"
        )
        e["website"] = e.get("website") or "https://www.vlaamswoningfonds.be"
with open(ent_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=efields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    for e in ents:
        w.writerow({k: e.get(k, "") for k in efields})
print("entity vwf notes updated")

budgets = [
    # Authorization / production
    ("bud_vwf_auth_woonlening_1_7bn_2025", "vwf", 2025, 1700000000, "", "", "budgeted", SRC, "strong", "VL budget auth bijzondere sociale leningen 1.7bn 2025 (same 2026); tick738"),
    ("bud_vwf_auth_huurwaarborg_20m_2025", "vwf", 2025, 20000000, "", "", "budgeted", SRC, "strong", "VL budget auth huurwaarborgleningen 20m 2025; tick738"),
    ("bud_vwf_woonlening_n_7057_2025", "vwf", 2025, 7057, "", "", "outturn", SRC, "strong", "Vlaamse woonlening COUNT granted 7057 2025 (record; +6.55pct); tick738"),
    ("bud_vwf_woonlening_amount_1_632bn_2025", "vwf", 2025, 1632223520.98, "", "", "outturn", SRC, "strong", "Vlaamse woonlening amount 1.632bn 2025 (was 1.478bn / 6623 in 2024); tick738"),
    ("bud_vwf_woonlening_avg_231291_2025", "vwf", 2025, 231291.42, "", "", "outturn", SRC, "strong", "Average woonlening 231291.42 EUR 2025 (+3.62pct); tick738"),
    ("bud_vwf_woonlening_rate_2_48pct_2025", "vwf", 2025, 248, "", "", "outturn", SRC, "strong", "Average interest rate 2.48pct 2025 (was 2.40; ~0.84pp below bank 3.32); tick738"),
    ("bud_vwf_apps_opened_7978_2025", "vwf", 2025, 7978, "", "", "outturn", SRC, "strong", "Loan applications opened COUNT 7978 reserved 1.626bn 2025; tick738"),
    ("bud_vwf_reserved_1_626bn_2025", "vwf", 2025, 1625739698.48, "", "", "outturn", SRC, "strong", "Financial means reserved for opened apps 1.626bn 2025; tick738"),
    ("bud_vwf_info_talks_31100_2025", "vwf", 2025, 31100, "", "", "outturn", SRC, "strong", "Face-to-face info talks >31100 interested parties 2025; tick738"),
    # Loan purpose split (amounts average * count not exact total - use counts and avgs as published)
    ("bud_vwf_purchase_n_3291_2025", "vwf", 2025, 3291, "", "", "outturn", SRC, "strong", "Purchase-only loans COUNT 3291 (46.64pct) avg 243193 2025; tick738"),
    ("bud_vwf_purchase_reno_n_2842_2025", "vwf", 2025, 2842, "", "", "outturn", SRC, "strong", "Purchase+reno loans COUNT 2842 (40.27pct) avg 255771 2025; tick738"),
    ("bud_vwf_reno_only_n_217_2025", "vwf", 2025, 217, "", "", "outturn", SRC, "strong", "Reno-only loans COUNT 217 avg 49194 2025; tick738"),
    ("bud_vwf_social_buy_n_225_2025", "vwf", 2025, 225, "", "", "outturn", SRC, "strong", "Social koopwoning (+reno) loans 225 2025 (was 382 2024); tick738"),
    ("bud_vwf_duration_avg_24_49y_2025", "vwf", 2025, 2449, "", "", "outturn", SRC, "strong", "Average loan duration 24.49 years 2025; tick738"),
    ("bud_vwf_mean_net_income_3321_2025", "vwf", 2025, 3321.05, "", "", "outturn", SRC, "strong", "Mean net family income 3321.05 EUR/mo 2025; tick738"),
    ("bud_vwf_mean_monthly_pay_1047_2025", "vwf", 2025, 1046.69, "", "", "outturn", SRC, "strong", "Mean monthly repayment 1046.69 EUR (31.52pct of income) 2025; tick738"),
    ("bud_vwf_under30_share_22_32pct_2025", "vwf", 2025, 2232, "", "", "outturn", SRC, "strong", "Borrowers under 30 share 22.32pct 2025 (was 25.46); tick738"),
    ("bud_vwf_over50_share_9_23pct_2025", "vwf", 2025, 923, "", "", "outturn", SRC, "strong", "Borrowers 51+ share 9.23pct 2025 (solvency concern flagged); tick738"),
    # Portfolio residual
    ("bud_vwf_portfolio_total_9_698bn_2025", "vwf", 2025, 9698265413.95, "", "", "outturn", SRC, "strong", "Total managed mortgage portfolio 9.698bn / 71635 loans eoy2025; tick738"),
    ("bud_vwf_portfolio_total_n_71635_2025", "vwf", 2025, 71635, "", "", "outturn", SRC, "strong", "Total managed mortgages COUNT 71635 eoy2025; tick738"),
    ("bud_vwf_own_origin_7_611bn_2025", "vwf", 2025, 7611054157.56, "", "", "outturn", SRC, "strong", "Own-originated VWF loans 7.611bn / 50404 eoy2025 (+11pct); tick738"),
    ("bud_vwf_own_origin_n_50404_2025", "vwf", 2025, 50404, "", "", "outturn", SRC, "strong", "Own-originated COUNT 50404 eoy2025; tick738"),
    ("bud_vwf_arrears_gt1m_n_1052_2025", "vwf", 2025, 1052, "", "", "outturn", SRC, "strong", "Mortgage arrears >1 month COUNT 1052 (2.09pct of own book) eoy2025; tick738"),
    ("bud_vwf_arrears_amount_4_064m_2025", "vwf", 2025, 4064366.40, "", "", "outturn", SRC, "strong", "Mortgage arrears amount 4.064m (0.05pct of capital) eoy2025; tick738"),
    ("bud_vwf_forced_sale_deficit_0_809m_2025", "vwf", 2025, 809007, "", "", "outturn", SRC, "medium", "Forced sales 28 cases provisional deficit est 0.809m 2025; tick738"),
    ("bud_vwf_early_repay_146_909m_2025", "vwf", 2025, 146908896.57, "", "", "outturn", SRC, "strong", "Lump-sum early repayments 146.909m (1236 cases) 2025; tick738"),
    # Huurwaarborg residual
    ("bud_vwf_hw_n_5087_2025", "vwf", 2025, 5087, "", "", "outturn", SRC, "strong", "Huurwaarborgleningen paid COUNT 5087 2025 (+3.16pct); tick738"),
    ("bud_vwf_hw_amount_10_835m_2025", "vwf", 2025, 10835405.67, "", "", "outturn", SRC, "strong", "Huurwaarborg amount paid 10.835m avg 2130 2025; tick738"),
    ("bud_vwf_hw_stock_12_300m_2025", "vwf", 2025, 12299980.31, "", "", "outturn", SRC, "strong", "Huurwaarborg stock 12.300m / ~10472-10474 loans eoy2025; tick738"),
    ("bud_vwf_hw_arrears_n_938_2025", "vwf", 2025, 938, "", "", "outturn", SRC, "strong", "HW arrears >1 month COUNT 938 (8.96pct) eoy2025; tick738"),
    ("bud_vwf_hw_arrears_amount_0_616m_2025", "vwf", 2025, 616382.10, "", "", "outturn", SRC, "strong", "HW arrears amount 0.616m ratio 5.01pct of stock eoy2025; tick738"),
    ("bud_vwf_hw_writeoff_0_126m_2025", "vwf", 2025, 125543.26, "", "", "outturn", SRC, "strong", "HW write-offs 127 loans 0.126m eoy2025; tick738"),
    ("bud_vwf_hw_collective_debt_n_834_2025", "vwf", 2025, 834, "", "", "outturn", SRC, "strong", "HW collective debt procedure COUNT 834 (7.96pct stock) eoy2025; tick738"),
    ("bud_vwf_hw_cancelled_6639_2025", "vwf", 2025, 6639, "", "", "outturn", SRC, "strong", "HW applications cancelled 6639 (16.788m class) 2025; tick738"),
    # VGW insurance
    ("bud_vwf_vgw_insured_7607_2025", "vwf", 2025, 7607, "", "", "outturn", SRC, "strong", "Verzekering gewaarborgd wonen effective 7607 of 14184 apps 2025; tick738"),
    ("bud_vwf_vgw_premium_6_212m_2025", "vwf", 2025, 6211610.62, "", "", "outturn", SRC, "strong", "VGW premium paid excl tax 6.212m 2025; tick738"),
    ("bud_vwf_vgw_apps_14184_2025", "vwf", 2025, 14184, "", "", "outturn", SRC, "strong", "VGW applications received 14184 2025 (was 11269); tick738"),
    # Funding / toelage
    ("bud_vwf_bonds_issued_1_550bn_2025", "vwf", 2025, 1550000000, "", "", "outturn", SRC, "strong", "4 LT bond issues 1.550bn @ weighted avg 4.21pct 2025; tick738"),
    ("bud_vwf_toelage_received_1_748m_2025", "vwf", 2025, 1748234.13, "", "", "outturn", SRC, "strong", "Werkings+financieringstoelage received 1.748m (incl 2024 settlement) 2025; tick738"),
    ("bud_vwf_toelage_balance_owed_9_808m_2025", "vwf", 2025, 9808377.98, "", "", "outturn", SRC, "strong", "Toelage balance owed by VWF after 2025 settlement 9.808m due 2026; tick738"),
    ("bud_vwf_stock_transfer_965_units", "vwf", 2025, 965, "", "", "outturn", SRC, "strong", "Social rental stock transferred to woonmaatschappijen total 965 units (last Limburg Jun2025); tick738"),
    # BNB residual
    ("bud_vwf_assets_10_003bn_2025", "vwf", 2025, 10002973918, "", "", "outturn", SRC_JR, "strong", "NBB BS total assets eoy2025 10.003bn (was 8.994); tick738"),
    ("bud_vwf_debt_total_9_730bn_2025", "vwf", 2025, 9729917042, "", "", "outturn", SRC_JR, "strong", "NBB total debts 9.730bn eoy2025; tick738"),
    ("bud_vwf_lt_fin_debt_8_941bn_2025", "vwf", 2025, 8940779387, "", "", "outturn", SRC_JR, "strong", "NBB LT financial debt 8.941bn (bonds 4.865 banks 0.803 other 3.272); tick738"),
    ("bud_vwf_bonds_stock_4_865bn_2025", "vwf", 2025, 4864864067, "", "", "outturn", SRC_JR, "strong", "NBB bond stock 4.865bn eoy2025 (was 3.587); tick738"),
    ("bud_vwf_gov_guaranteed_2_300bn_2025", "vwf", 2025, 2299850960, "", "", "outturn", SRC_JR, "strong", "Debts guaranteed by Belgian public authorities 2.300bn eoy2025; tick738"),
    ("bud_vwf_fin_income_199_386m_2025", "vwf", 2025, 199386486, "", "", "outturn", SRC_JR, "strong", "NBB financial income 199.386m 2025; tick738"),
    ("bud_vwf_fin_costs_197_927m_2025", "vwf", 2025, 197926877, "", "", "outturn", SRC_JR, "strong", "NBB financial costs 197.927m (debt costs 194.103m) 2025; tick738"),
    ("bud_vwf_remuneration_10_493m_2025", "vwf", 2025, 10492956, "", "", "outturn", SRC_JR, "strong", "NBB remuneration 10.493m 2025; tick738"),
    ("bud_vwf_net_result_0_2025", "vwf", 2025, 0, "", "", "outturn", SRC_JR, "strong", "NBB net result 0 (nulresultaat) 2025 (was +3.684m 2024); tick738"),
    ("bud_vwf_receivables_lt_9_217bn_2025", "vwf", 2025, 9217286757, "", "", "outturn", SRC_JR, "strong", "NBB LT other receivables (loan book class) 9.217bn eoy2025; tick738"),
    # Dual residual
    ("bud_dual_vwf_prod_1_632bn_vs_swcs_2025", "gg_belgium", 2025, 1632223520.98, "", "", "outturn", SRC_DUAL, "strong", "VWF prod 1.632bn dual SWCS 0.483bn / FLW invest 0.273; not TE-additive; tick738"),
    ("bud_dual_vwf_portfolio_9_698bn_vs_swcs", "gg_belgium", 2025, 9698265413.95, "", "", "outturn", SRC_DUAL, "strong", "VWF portfolio 9.698bn dual SWCS encours 1.749bn / SWL debt 2.742 / VMSW 3.12; tick738"),
    ("bud_dual_vwf_hw_npl_9pct_vs_swcs_31pct", "gg_belgium", 2025, 12299980.31, "", "", "outturn", SRC_DUAL, "strong", "VWF HW arrears 8.96pct dual SWCS garantie locative contentieux 31pct; tick738"),
]

bud_path = DATA / "budgets.csv"
with open(bud_path, encoding="utf-8", newline="") as f:
    br = csv.DictReader(f)
    bfields = br.fieldnames
    existing = {r["budget_id"] for r in br}
added_b = 0
with open(bud_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bfields, lineterminator="\n")
    for row in budgets:
        if row[0] in existing:
            continue
        w.writerow({
            "budget_id": row[0], "entity_id": row[1], "year": row[2],
            "amount_eur": row[3], "amount_min_eur": row[4], "amount_max_eur": row[5],
            "basis": row[6], "source_id": row[7], "confidence": row[8], "notes": row[9],
        })
        added_b += 1
print(f"budgets +{added_b}")

commitments = [
    {
        "commitment_id": "cmt_vwf_woonlening_1_632bn_2025",
        "title": "Vlaamse woonlening production 1.632bn / 7057 loans 2025",
        "entity_id": "vwf",
        "beneficiary": "Flanders modest-income homebuyers",
        "legal_basis": "VWF AV2025 + VL uitgavenbegroting auth 1.7bn",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "1632223520.98",
        "cash_by_year": '{"prod_m":1632.2,"n":7057,"avg_eur":231291,"rate_pct":2.48,"auth_m":1700,"reserved_m":1625.7,"apps_n":7978,"duration_y":24.49}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_AV,
        "stated_goal": "Social mortgage access below market rates",
        "cut_option": "Uitgaventoetsing 2026 + rate path FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VWF>woonlening",
        "notes": "tick738",
    },
    {
        "commitment_id": "cmt_vwf_portfolio_9_698bn_2025",
        "title": "VWF managed mortgage portfolio 9.698bn / 71635 loans eoy2025",
        "entity_id": "vwf",
        "beneficiary": "Active VWF and historic social mortgage borrowers",
        "legal_basis": "VWF AV2025 dossierbeheer residual",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "9698265413.95",
        "cash_by_year": '{"portfolio_m":9698.3,"n":71635,"own_m":7611.1,"own_n":50404,"arrears_gt1m_n":1052,"arrears_m":4.064,"arrears_pct_capital":0.05}',
        "remaining_eur": "9698265413.95",
        "status": "active",
        "evaluation_url": URL_AV,
        "stated_goal": "Sustain social mortgage book with controlled defaults",
        "cut_option": "NPL cash + over-50 borrower risk FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VWF>portfolio",
        "notes": "tick738",
    },
    {
        "commitment_id": "cmt_vwf_bonds_1_550bn_2025",
        "title": "VWF bond issuance 1.550bn @ 4.21pct weighted 2025",
        "entity_id": "vwf",
        "beneficiary": "Funding of social loan production",
        "legal_basis": "VWF AV2025 + NBB jaarrekening 2025",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2035",
        "total_envelope_eur": "1550000000",
        "cash_by_year": '{"issued_m":1550,"weighted_rate_pct":4.21,"bond_stock_eoy_m":4864.9,"gov_guarantee_m":2299.9,"fin_costs_m":197.9}',
        "remaining_eur": "1550000000",
        "status": "active",
        "evaluation_url": URL_AV,
        "stated_goal": "Fund social mortgages via capital markets",
        "cut_option": "Spread vs 2.48pct lending rate subsidy TCO FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VWF>bonds",
        "notes": "tick738 funding gap 4.21 vs lending 2.48",
    },
    {
        "commitment_id": "cmt_vwf_huurwaarborg_10_835m_2025",
        "title": "Huurwaarborglening 10.835m / 5087 loans 2025",
        "entity_id": "vwf",
        "beneficiary": "Private-market tenants needing deposit finance",
        "legal_basis": "VWF AV2025 huurwaarborg residual",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "10835405.67",
        "cash_by_year": '{"paid_m":10.835,"n":5087,"avg_eur":2130,"stock_m":12.3,"arrears_n":938,"arrears_pct":8.96,"writeoff_m":0.126,"auth_m":20}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_AV,
        "stated_goal": "Remove deposit barrier to private rental",
        "cut_option": "Redesign if arrears stay ~9pct dual SWCS 31pct FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VWF>huurwaarborg",
        "notes": "tick738",
    },
    {
        "commitment_id": "cmt_vwf_vgw_premium_6_212m_2025",
        "title": "Verzekering gewaarborgd wonen premium 6.212m / 7607 policies 2025",
        "entity_id": "vwf",
        "beneficiary": "Mortgage borrowers income-loss insurance",
        "legal_basis": "VWF AV2025 VGW residual",
        "decision_date": "2025-12-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "6211610.62",
        "cash_by_year": '{"premium_m":6.212,"insured_n":7607,"apps_n":14184,"refused_n":3672}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_AV,
        "stated_goal": "Insure mortgage payments against involuntary income loss",
        "cut_option": "Claims ratio TCO FOI",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VWF>VGW",
        "notes": "tick738",
    },
    {
        "commitment_id": "cmt_dual_vwf_swcs_flw_tick738",
        "title": "Dual VWF AV2025 residual vs SWCS/FLW social credit",
        "entity_id": "gg_belgium",
        "beneficiary": "BE social credit dual map",
        "legal_basis": "VWF AV2025 + prior SWCS RA2025 / FLW RA2024 duals",
        "decision_date": "2026-06-18",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "9698265413.95",
        "cash_by_year": '{"vwf_prod_m":1632,"vwf_portfolio_m":9698,"vwf_bonds_m":1550,"swcs_prod_m":483,"swcs_encours_m":1749,"flw_invest_m":273,"note":"not TE-additive dual social credit"}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": URL_AV,
        "stated_goal": "Comparable regional social credit",
        "cut_option": "Open dual rate/NPL/unit-cost dashboard FOI",
        "source_id": SRC_DUAL,
        "confidence": "strong",
        "hierarchy_path": "Belgium>dual>VWF_SWCS_FLW",
        "notes": "tick738",
    },
]

cmt_path = DATA / "commitments.csv"
with open(cmt_path, encoding="utf-8", newline="") as f:
    cr = csv.DictReader(f)
    cfields = cr.fieldnames
    cexist = {r["commitment_id"] for r in cr}
added_c = 0
with open(cmt_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cfields, lineterminator="\n")
    for row in commitments:
        if row["commitment_id"] in cexist:
            continue
        w.writerow(row)
        added_c += 1
print(f"commitments +{added_c}")

leaderboard = [
    {
        "item_id": "lb_vwf_portfolio_9_698bn_2025",
        "name": "VWF mortgage portfolio 9.698bn eoy2025 (largest BE social-credit book)",
        "level": "L5",
        "type": "stock",
        "hierarchy_path": "Vlaanderen>VWF>portfolio",
        "annual_cost_eur": "9698265413.95",
        "total_cost_eur": "9698265413.95",
        "tco_notes": "Stock; annual fin costs 197.9m; dual SWCS 1.75bn SWL 2.74bn VMSW 3.12bn",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "71635 mortgage loans managed",
        "stated_goal": "Social homeownership finance",
        "measured_outcome": "Arrears 2.09pct COUNT / 0.05pct capital; own book 7.61bn",
        "absurdity_score": "5.5",
        "cost_score": "9.0",
        "difficulty": "4",
        "priority_index": "6.85",
        "cut_proposal": "Rate subsidy TCO + over-50 solvency FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick738 stock often filtered from pure annual top10",
    },
    {
        "item_id": "lb_vwf_prod_1_632bn_2025",
        "name": "Vlaamse woonlening production 1.632bn 2025 @2.48pct vs bonds 4.21pct",
        "level": "L5",
        "type": "programme",
        "hierarchy_path": "Vlaanderen>VWF>woonlening",
        "annual_cost_eur": "1632223520.98",
        "total_cost_eur": "1632223520.98",
        "tco_notes": "Production flow funded by bonds at 4.21pct; lending 2.48pct implies structural subsidy",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "7057 households 2025",
        "stated_goal": "Below-market social mortgages",
        "measured_outcome": "Record volume; ~0.84pp below bank; ~30k lifetime saving claimed",
        "absurdity_score": "6.5",
        "cost_score": "8.5",
        "difficulty": "4",
        "priority_index": "7.05",
        "cut_proposal": "Publish annual interest subsidy euro + uitgaventoetsing FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick738 funding spread residual",
    },
    {
        "item_id": "lb_vwf_bonds_1_550bn_2025",
        "name": "VWF bond issuance 1.550bn @4.21pct funding social loans @2.48pct",
        "level": "L5",
        "type": "funding",
        "hierarchy_path": "Vlaanderen>VWF>bonds",
        "annual_cost_eur": "1550000000",
        "total_cost_eur": "1550000000",
        "tco_notes": "Bond stock eoy 4.865bn; fin costs 197.9m; gov guarantee 2.30bn",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Capital markets / Region guarantee stack",
        "stated_goal": "Fund social mortgage production",
        "measured_outcome": "4 issues 1.55bn; bond stock +1.28bn YoY",
        "absurdity_score": "6.5",
        "cost_score": "8.0",
        "difficulty": "3",
        "priority_index": "6.95",
        "cut_proposal": "Guarantee fee + spread transparency FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick738",
    },
    {
        "item_id": "lb_vwf_fin_costs_197_9m_2025",
        "name": "VWF financial costs 197.9m 2025 on 9.73bn debt book",
        "level": "L5",
        "type": "overhead",
        "hierarchy_path": "Vlaanderen>VWF>fin_costs",
        "annual_cost_eur": "197926877",
        "total_cost_eur": "197926877",
        "tco_notes": "Debt costs 194.1m; fin income 199.4m; net result 0",
        "confidence": "strong",
        "source_id": SRC_JR,
        "beneficiaries": "Intermediated via social loan book",
        "stated_goal": "Service capital-market funding",
        "measured_outcome": "Near-zero net after fin income 199.4m",
        "absurdity_score": "5.5",
        "cost_score": "7.5",
        "difficulty": "3",
        "priority_index": "6.30",
        "cut_proposal": "Interest path + subsidy residual FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick738",
    },
    {
        "item_id": "lb_vwf_hw_arrears_9pct_2025",
        "name": "VWF huurwaarborg arrears 8.96pct (938 of 10.5k) dual SWCS 31pct",
        "level": "L5",
        "type": "programme",
        "hierarchy_path": "Vlaanderen>VWF>huurwaarborg",
        "annual_cost_eur": "10835405.67",
        "total_cost_eur": "12299980.31",
        "tco_notes": "Stock 12.3m; arrears amount 0.616m ratio 5.01pct; write-offs 0.126m",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "5087 deposit borrowers 2025",
        "stated_goal": "Access private rental via deposit loan",
        "measured_outcome": "8.96pct COUNT arrears; 7.96pct collective debt",
        "absurdity_score": "7.0",
        "cost_score": "4.5",
        "difficulty": "2",
        "priority_index": "6.05",
        "cut_proposal": "Product redesign if dual high-NPL deposit loans persist",
        "status": "active",
        "struck_reason": "",
        "notes": "tick738 dual SWCS garantie NPL",
    },
    {
        "item_id": "lb_vwf_over50_solvency_risk",
        "name": "VWF borrowers 51+ share 9.23pct with 20.3y residual term risk flag",
        "level": "L5",
        "type": "risk",
        "hierarchy_path": "Vlaanderen>VWF>age_risk",
        "annual_cost_eur": "1632223520.98",
        "total_cost_eur": "1632223520.98",
        "tco_notes": "Risk class on 2025 production; avg monthly 1061 for 50+; flagged to cabinet no rule change",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Older social-mortgage borrowers",
        "stated_goal": "Sustainable repayment through working life",
        "measured_outcome": "51+ share rising; 20.33y avg duration for 50+",
        "absurdity_score": "6.5",
        "cost_score": "6.0",
        "difficulty": "3",
        "priority_index": "6.15",
        "cut_proposal": "Age/duration caps in uitgaventoetsing FOI",
        "status": "active",
        "struck_reason": "",
        "notes": "tick738",
    },
    {
        "item_id": "lb_dual_vwf_swcs_flw_asymmetry",
        "name": "Dual VWF 1.63bn prod / 9.70bn book vs SWCS 0.48bn / 1.75bn / FLW 0.27bn",
        "level": "L5",
        "type": "dual",
        "hierarchy_path": "Belgium>dual>VWF_SWCS_FLW",
        "annual_cost_eur": "9698265413.95",
        "total_cost_eur": "9698265413.95",
        "tco_notes": "Not TE-additive; VL scale >> WAL social credit",
        "confidence": "strong",
        "source_id": SRC_DUAL,
        "beneficiaries": "BE social credit dual map",
        "stated_goal": "Comparable regional social credit",
        "measured_outcome": "VWF ~3.4x SWCS production; ~5.5x encours",
        "absurdity_score": "6.5",
        "cost_score": "8.5",
        "difficulty": "4",
        "priority_index": "7.05",
        "cut_proposal": "Open dual rate/NPL/unit-cost dashboard",
        "status": "active",
        "struck_reason": "",
        "notes": "tick738",
    },
]

lb_path = DATA / "leaderboard.csv"
with open(lb_path, encoding="utf-8", newline="") as f:
    lr = csv.DictReader(f)
    lfields = lr.fieldnames
    lexist = {r["item_id"] for r in lr}
added_l = 0
with open(lb_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lfields, lineterminator="\n")
    for row in leaderboard:
        if row["item_id"] in lexist:
            continue
        w.writerow(row)
        added_l += 1
print(f"leaderboard +{added_l}")

sources = [
    {
        "source_id": SRC,
        "title": "VWF Activiteitenverslag 2025 residual dual SWCS/FLW social credit",
        "url": URL_AV,
        "publisher": "Vlaams Woningfonds",
        "accessed_date": "2026-08-02",
        "source_class": "official_annual_report",
        "notes": (
            "Strong tick738: auth 1.7bn+20m; prod 7057 / 1.632bn @2.48pct; portfolio 71.6k / 9.698bn; "
            "own 50.4k / 7.611bn; HW 5087 / 10.835m NPL 8.96pct; bonds 1.55bn @4.21pct; "
            "VGW 7607 / premium 6.212m; toelage rec 1.748 owed 9.808; downloads " + URL_DL
        ),
    },
    {
        "source_id": SRC_JR,
        "title": "VWF NBB jaarrekening 2025 residual balance sheet",
        "url": URL_JR,
        "publisher": "Vlaams Woningfonds / NBB Centrale des bilans",
        "accessed_date": "2026-08-02",
        "source_class": "official_accounts",
        "notes": (
            "Strong tick738: assets 10.003bn debt 9.730bn LT fin 8.941 bonds 4.865; "
            "gov guarantee 2.300bn; fin income 199.4 fin costs 197.9 net 0; rem 10.5m"
        ),
    },
    {
        "source_id": SRC_DUAL,
        "title": "Dual VWF AV2025 residual vs SWCS/FLW social credit tick738",
        "url": URL_AV,
        "publisher": "DOGE synthesis VWF + SWCS + FLW",
        "accessed_date": "2026-08-02",
        "source_class": "synthesis",
        "notes": (
            "Strong dual not TE-additive: VWF prod 1.632 portfolio 9.698 vs SWCS 0.483 / 1.749 "
            "FLW invest 0.273; HW NPL 9pct vs SWCS garantie 31pct; tick738"
        ),
    },
]

src_path = DATA / "sources.csv"
with open(src_path, encoding="utf-8", newline="") as f:
    sr = csv.DictReader(f)
    sfields = sr.fieldnames
    sexist = {r["source_id"] for r in sr}
added_s = 0
with open(src_path, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sfields, lineterminator="\n")
    for row in sources:
        if row["source_id"] in sexist:
            continue
        w.writerow(row)
        added_s += 1
print(f"sources +{added_s}")

foi_row = {
    "gap_id": "gap_vwf_av2025_residual_l5",
    "hierarchy_path": "Vlaanderen>VWF>AV2025_residual_L5",
    "entity_id": "vwf",
    "what_is_missing": (
        "Machine-readable L5: (1) annual euro interest-subsidy residual between lending rate 2.48pct "
        "and funding cost ~4.21pct on 2025 production and stock; (2) cash NPL / recovery / write-off "
        "for mortgages and huurwaarborg beyond COUNT rates; (3) government guarantee stock path "
        "2.30bn and guarantee fees; (4) over-50 borrower vintage risk matrix and default history; "
        "(5) VGW claims paid by Ethias vs premium 6.212m; (6) dual unit comparison vs SWCS/FLW rates"
    ),
    "why_it_matters": (
        "AV2025 + NBB fill strong production and portfolio aggregates (1.632bn / 9.698bn) but the "
        "structural rate subsidy, guarantee economics, and dual unit costs remain opaque for waste ranking"
    ),
    "priority": "8",
    "recipient_body": "Vlaams Woningfonds openbaarheid / Agentschap Wonen in Vlaanderen",
    "recipient_email": "info@vlaamswoningfonds.be",
    "recipient_postal": "https://www.vlaamswoningfonds.be",
    "draft_letter_path": "docs/doge/foi/drafts/gap_vwf_av2025_residual_l5.md",
    "status": "ready",
    "date_ready": "2026-08-02",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_vwf_woonlening_1_632bn_2025|cmt_vwf_bonds_1_550bn_2025|cmt_vwf_portfolio_9_698bn_2025",
    "linked_leaderboard_id": "lb_vwf_prod_1_632bn_2025|lb_vwf_bonds_1_550bn_2025|lb_dual_vwf_swcs_flw_asymmetry",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick738 VWF AV2025 residual dual; ready not sent",
}

foi_path = DATA / "foi_queue.csv"
with open(foi_path, encoding="utf-8", newline="") as f:
    fr = csv.DictReader(f)
    ffields = fr.fieldnames
    fexist = {r["gap_id"] for r in fr}
if foi_row["gap_id"] not in fexist:
    with open(foi_path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=ffields, lineterminator="\n")
        w.writerow(foi_row)
    print("foi +gap_vwf_av2025_residual_l5")
else:
    print("foi already exists")

rq_path = DATA / "research_queue.csv"
with open(rq_path, encoding="utf-8", newline="") as f:
    rr = csv.DictReader(f)
    rfields = list(rr.fieldnames or [])
    rqs = list(rr)
for r in rqs:
    if r.get("task_id") == "rq_729":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick738 VWF AV2025 residual dual SWCS/FLW: prod 1.632bn 7057 @2.48; "
            "portfolio 9.698bn; bonds 1.55bn @4.21; HW NPL 9pct; BS debt 9.73bn; "
            "FOI gap_vwf_av2025_residual_l5 ready"
        )
if not any(r.get("task_id") == "rq_730" for r in rqs):
    rqs.append({
        "task_id": "rq_730",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Next residual: PROGRESS@740 next OR new CoA/primary PDF not yet mined "
            "or FLRBC residual dual housing or Entity II dual residual"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": "",
        "notes": "spawned tick738 after rq_729",
    })
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rfields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    for r in rqs:
        w.writerow({k: r.get(k, "") for k in rfields})
print("research_queue rq_729=done rq_730=open")

ls_path = DATA / "loop_state.csv"
with open(ls_path, encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsfields = list(ls[0].keys()) if ls else [
        "state_id", "mode", "current_sprint", "last_tick_utc", "last_unit_id",
        "ticks_completed", "paused", "notes",
    ]
if ls:
    ls[0]["mode"] = "continuous"
    ls[0]["current_sprint"] = "hole_fill"
    ls[0]["last_tick_utc"] = UTC
    ls[0]["last_unit_id"] = "rq_729"
    ls[0]["ticks_completed"] = "738"
    ls[0]["paused"] = "no"
    ls[0]["notes"] = (
        "tick738 VWF AV2025 residual dual SWCS/FLW; next rq_730; "
        "progress@740 in 2; rq_116 deferred"
    )
with open(ls_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsfields, lineterminator="\n")
    w.writeheader()
    w.writerows(ls)
print("loop_state ticks=738")
print("DONE tick738")

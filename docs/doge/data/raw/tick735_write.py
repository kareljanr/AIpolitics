# tick735 — SLRB Rapport annuel 2025 residual dual VMSW/SWL (rq_726)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T04:45:00Z"
URL = "https://slrb-bghm.brussels/sites/default/files/2026-07/SLRB_RA2025_FR_web2.pdf"
URL_PAGE = "https://slrb-bghm.brussels/fr/actualites/cap-sur-les-resultats-2025-de-la-slrb"

SRC = "src_slrb_ra2025_residual"
SRC_DUAL = "src_dual_slrb_vmsw_swl_tick735"

# ensure entity
ent_path = DATA / "entities.csv"
with open(ent_path, encoding="utf-8", newline="") as f:
    er = csv.DictReader(f)
    efields = er.fieldnames
    ents = list(er)
if not any(e.get("entity_id") == "slrb" for e in ents):
    with open(ent_path, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow([
            "slrb",
            "Brusselse Gewestelijke Huisvestingsmaatschappij BGHM",
            "Société du Logement de la Région de Bruxelles-Capitale SLRB",
            "Brussels Regional Housing Company SLRB",
            "OIP",
            "brussels_gov",
            "FR/NL",
            "https://slrb-bghm.brussels",
            "",
            "",
            "tick735 entity seed from RA2025",
        ])
    print("entity slrb +")

budgets = [
    # Ops highlights residual
    ("bud_slrb_new_dwellings_received_2025", "slrb", 2025, 572, "", "", "outturn", SRC, "strong", "New dwellings receptioned 572 COUNT (404 turnkey) 2025; tick735"),
    ("bud_slrb_renovations_sisp_3037_2025", "slrb", 2025, 3037, "", "", "outturn", SRC, "strong", "SISP renovations 3037 COUNT (heavy/interior/envelope) 2025; tick735"),
    ("bud_slrb_families_attributed_2581_2025", "slrb", 2025, 2581, "", "", "outturn", SRC, "strong", "Families attributed new housing 2581 COUNT 2025; tick735"),
    ("bud_slrb_reno_reception_155m_2025", "slrb", 2025, 155000000, "", "", "outturn", SRC, "strong", "79 renovation sites receptioned 155m total 2025; tick735"),
    ("bud_slrb_reno_heavy_71m_2025", "slrb", 2025, 71000000, "", "", "outturn", SRC, "strong", "Heavy renovations 412 dwellings 71m of 86m complete/interior cluster; tick735"),
    ("bud_slrb_reno_interior_15m_2025", "slrb", 2025, 15000000, "", "", "outturn", SRC, "strong", "Interior renovations 713 dwellings 15m 2025; tick735"),
    ("bud_slrb_reno_envelope_69m_2025", "slrb", 2025, 69000000, "", "", "outturn", SRC, "strong", "Envelope renovations 23 sites 69m (complete 37 + partial 23) 2025; tick735"),
    ("bud_slrb_reno_tech_20m_2025", "slrb", 2025, 20000000, "", "", "outturn", SRC, "strong", "Technical installations 45 sites 20m 2025; tick735"),
    # Budget execution residual
    ("bud_slrb_rec_budget_954_213m_2025", "slrb", 2025, 954213000, "", "", "budgeted", SRC, "strong", "Recettes budget total 954.213m (incl 300m private loan line 0 exec); tick735"),
    ("bud_slrb_rec_exec_548_144m_2025", "slrb", 2025, 548144117, "", "", "outturn", SRC, "strong", "Recettes executed 548.144m (57.44pct; 83.79pct ex 300m unborrowed); tick735"),
    ("bud_slrb_rec_sprb_exec_284_593m_2025", "slrb", 2025, 284593385, "", "", "outturn", SRC, "strong", "SPRB financing executed 284.593m of 318.127m budget (89.46pct); tick735"),
    ("bud_slrb_rec_own_exec_261_247m_2025", "slrb", 2025, 261247248, "", "", "outturn", SRC, "strong", "Own/other recettes executed 261.247m of 330.343m (79.08pct); tick735"),
    ("bud_slrb_rec_other_powers_2_303m_2025", "slrb", 2025, 2303484, "", "", "outturn", SRC, "strong", "Other powers financing exec 2.303m of 5.743m (40.11pct); tick735"),
    ("bud_slrb_loan_line_300m_unexecuted_2025", "slrb", 2025, 300000000, "", "", "budgeted", SRC, "strong", "Private bank loan line 300m budgeted 0 executed 2025; tick735"),
    ("bud_slrb_dep_liq_budget_1005_363m_2025", "slrb", 2025, 1005363000, "", "", "budgeted", SRC, "strong", "Depenses liquidation budget 1005.363m 2025; tick735"),
    ("bud_slrb_dep_liq_exec_802_690m_2025", "slrb", 2025, 802689567, "", "", "outturn", SRC, "strong", "Depenses liquidation exec 802.690m (79.84pct vs 86.33 2024); tick735"),
    ("bud_slrb_dep_eng_budget_689_204m_2025", "slrb", 2025, 689204000, "", "", "budgeted", SRC, "strong", "Engagements budget 689.204m 2025; tick735"),
    ("bud_slrb_dep_eng_exec_597_249m_2025", "slrb", 2025, 597249336, "", "", "outturn", SRC, "strong", "Engagements exec 597.249m (86.66pct vs 44.87 2024); tick735"),
    ("bud_slrb_liq_construction_326_5m_2025", "slrb", 2025, 326461802, "", "", "outturn", SRC, "strong", "Construction+acquisition liq exec 326.462m (40.67pct of liq); tick735"),
    ("bud_slrb_liq_subsistence_221_6m_2025", "slrb", 2025, 221637865, "", "", "outturn", SRC, "strong", "SLRB subsistence/ops liq 221.638m (27.61pct; salaries 21.5 capital repay 178.4 interest 15.1); tick735"),
    ("bud_slrb_liq_renovation_172_7m_2025", "slrb", 2025, 172702133, "", "", "outturn", SRC, "strong", "Renovation investment plans liq 172.702m (21.52pct); tick735"),
    ("bud_slrb_liq_societal_81_9m_2025", "slrb", 2025, 81887767, "", "", "outturn", SRC, "strong", "Societal mission liq 81.888m (10.20pct ARS+PCS+SASLS+rent cuts); tick735"),
    ("bud_slrb_capital_repay_178_416m_2025", "slrb", 2025, 178415628, "", "", "outturn", SRC, "strong", "Debt capital reimbursement 178.416m of subsistence liq; tick735"),
    ("bud_slrb_interest_debt_15_071m_2025", "slrb", 2025, 15070518, "", "", "outturn", SRC, "strong", "Debt interest 15.071m 2025; tick735"),
    ("bud_slrb_salaries_21_496m_2025", "slrb", 2025, 21496143, "", "", "outturn", SRC, "strong", "SLRB salaries 21.496m (P&L rem 21.513m); tick735"),
    ("bud_slrb_ars_52_548m_2025", "slrb", 2025, 52548000, "", "", "outturn", SRC, "strong", "Allocation regionale de solidarite ARS to SISP 52.548m 2025; tick735"),
    ("bud_slrb_rent_cut_large_fam_15_272m_2025", "slrb", 2025, 15272000, "", "", "outturn", SRC, "strong", "Rent reductions large families transfer 15.272m 2025; tick735"),
    ("bud_slrb_pcs_cohesion_4_463m_2025", "slrb", 2025, 4463133, "", "", "outturn", SRC, "strong", "PCS cohesion ASBL subsides 4.463m 2025; tick735"),
    ("bud_slrb_sasls_4_136m_2025", "slrb", 2025, 4136000, "", "", "outturn", SRC, "strong", "ASBL SASLS social accompaniment 4.136m 2025; tick735"),
    ("bud_slrb_prl_construction_cost_107_071m_2025", "slrb", 2025, 107070823, "", "", "outturn", SRC, "strong", "PRL/AH construction costs liq 107.071m (99.98pct of 107.092 budget); tick735"),
    ("bud_slrb_prl_subs_38_032m_2025", "slrb", 2025, 38032374, "", "", "outturn", SRC, "strong", "PRL/AH investment subsidies to SISP 38.032m 2025; tick735"),
    ("bud_slrb_prl_advances_151_387m_2025", "slrb", 2025, 151387332, "", "", "outturn", SRC, "strong", "PRL/AH non-subsidised credits to SISP 151.387m 2025; tick735"),
    ("bud_slrb_ppp_sfar_repay_29_950m_2025", "slrb", 2025, 29950091, "", "", "outturn", SRC, "strong", "PPP+SFAR repayments 29.950m 2025; tick735"),
    ("bud_slrb_reno_subs_49_036m_2025", "slrb", 2025, 49036263, "", "", "outturn", SRC, "strong", "Renovation regulated subsidies to SISP 49.036m 2025; tick735"),
    ("bud_slrb_reno_advances_90_001m_2025", "slrb", 2025, 90001300, "", "", "outturn", SRC, "strong", "Renovation repayable advances to SISP 90.001m 2025; tick735"),
    ("bud_slrb_lt_loans_sisp_32_097m_2025", "slrb", 2025, 32096605, "", "", "outturn", SRC, "strong", "LT loans to SISP from own funds 32.097m 2025; tick735"),
    ("bud_slrb_pv_credits_1_568m_2025", "slrb", 2025, 1567965, "", "", "outturn", SRC, "strong", "PV energy investment credits to SISP 1.568m 2025; tick735"),
    # Stocks residual
    ("bud_slrb_encours_eng_1_131bn_2025", "slrb", 2025, 1131471548, "", "", "outturn", SRC, "strong", "Encours engagements eoy2025 1.131bn (-593m / -34.4pct vs 2024); tick735"),
    ("bud_slrb_encours_old_quad_125_7m_2025", "slrb", 2025, 125679809, "", "", "outturn", SRC, "strong", "Old quadriennial reno encours 125.68m (-53.4pct from 269.7); tick735"),
    ("bud_slrb_psrd_encours_141_4m_2025", "slrb", 2025, 141358400, "", "", "outturn", SRC, "strong", "PSRD encours 141.358m (+4.23pct); eng 55.0m constrained; tick735"),
    ("bud_slrb_prl_ah_cost_encours_130_3m_2025", "slrb", 2025, 130277000, "", "", "outturn", SRC, "strong", "PRL/AH construction-cost encours 130.277m (was 293.07); tick735"),
    ("bud_slrb_plans_subs_solde_649_8m_2025", "slrb", 2025, 649830390, "", "", "outturn", SRC, "strong", "PRL+AH+PUL subsidy envelope solde available 649.83m of 1048.13 total; tick735"),
    ("bud_slrb_prl_own_fund_gap_577_2m", "slrb", 2025, 577230000, "", "", "outturn", SRC, "strong", "PRL/AH own-fund gap: Region rec 387.66 vs spend 964.89 = -577.23m; tick735"),
    ("bud_slrb_assets_2_370bn_2025", "slrb", 2025, 2370136983, "", "", "outturn", SRC, "strong", "Balance-sheet assets 2.370bn eoy2025 (+85.7m); tick735"),
    ("bud_slrb_debt_1_672bn_2025", "slrb", 2025, 1671720429, "", "", "outturn", SRC, "strong", "Balance-sheet debts 1.672bn eoy2025 (+87.6m; +300m loans + PSRD advances); tick735"),
    ("bud_slrb_equity_696_4m_2025", "slrb", 2025, 696399851, "", "", "outturn", SRC, "strong", "Equity 696.4m eoy2025 (-1.88m); tick735"),
    ("bud_slrb_sisp_loan_stock_1_503bn_2026", "slrb", 2026, 1502917335, "", "", "outturn", SRC, "strong", "SISP loan stock start 2026 1.503bn (amort path to 2035); tick735"),
    ("bud_slrb_sisp_cco_neg_115_4m_2025", "slrb", 2025, 115444837, "", "", "outturn", SRC, "strong", "SISP negative current accounts to SLRB 115.445m eoy2025 (+11.5m); tick735"),
    ("bud_slrb_rent_arrears_19_207m_2025", "slrb", 2025, 19206803, "", "", "outturn", SRC, "strong", "Tenant rent arrears sector 19.207m (mean real rent 413.5/mo); tick735"),
    ("bud_slrb_social_finance_used_36_310m", "slrb", 2025, 36309674, "", "", "outturn", SRC, "strong", "Social Finance Framework 100m facility: used 36.310m of 63.690 borrowed (2024 use; residual); tick735"),
    ("bud_slrb_regional_guarantee_150m_2024", "slrb", 2024, 150000000, "", "", "budgeted", SRC, "strong", "Regional guarantee 150m 2024 caretaker note; tick735"),
    ("bud_slrb_region_loan_125m_2023", "slrb", 2023, 125000000, "", "", "outturn", SRC, "strong", "Region loan 125m 2023 to repay via asset sales 2026+; tick735"),
    # Dual residual
    ("bud_dual_slrb_liq_vs_vmsw_swl_2025", "gg_belgium", 2025, 802689567, "", "", "outturn", SRC_DUAL, "strong", "SLRB liq exec 802.7 dual VMSW debt 3.12bn / SWL SEC dep 366; not TE-additive; tick735"),
    ("bud_dual_slrb_debt_vs_vmsw_2025", "gg_belgium", 2025, 1671720429, "", "", "outturn", SRC_DUAL, "strong", "SLRB BS debt 1.672bn dual VMSW debt 3.123bn dual SWL guarantees; tick735"),
    ("bud_dual_slrb_encours_1_131bn_housing", "gg_belgium", 2025, 1131471548, "", "", "outturn", SRC_DUAL, "strong", "SLRB eng encours 1.131bn dual VL/WAL housing investment stocks; tick735"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_slrb_liq_exec_802_7m_2025",
        "SLRB liquidation exec 802.7m of 1005.4m budget 2025",
        "slrb",
        "Brussels social housing residents / SISP",
        "SLRB Rapport annuel 2025 finance residual",
        "2026-06-18",
        2025,
        2025,
        802689567,
        '{"liq_budget_m":1005.363,"liq_exec_m":802.690,"exec_pct":79.84,"eng_exec_m":597.249,"eng_budget_m":689.204,"construction_m":326.5,"subsistence_m":221.6,"renovation_m":172.7,"societal_m":81.9}',
        0,
        "active",
        URL,
        "Public social housing finance delivery",
        "Publish unit-cost per dwelling FOI dual VMSW",
        SRC,
        "strong",
        "Bruxelles>SLRB>budget_exec_2025",
        "tick735 residual",
    ),
    (
        "cmt_slrb_prl_own_fund_gap_577m",
        "PRL/AH own-fund gap 577m: Region rec 388 vs spend 965",
        "slrb",
        "SISP / regional taxpayers",
        "SLRB RA2025 comptes residual",
        "2025-12-31",
        2025,
        2025,
        577230000,
        '{"region_subs_rec_m":387.66,"spend_m":964.89,"own_fund_gap_m":577.23,"quad_rec_m":1438.32,"quad_spend_m":1171.65,"quad_residual_m":266.67}',
        0,
        "active",
        URL,
        "Honest multi-year housing plan finance",
        "Reconcile Region advances FOI dual",
        SRC,
        "strong",
        "Bruxelles>SLRB>PRL_AH_gap",
        "tick735",
    ),
    (
        "cmt_slrb_debt_1_672bn_path",
        "SLRB BS debt 1.672bn + SISP loan stock 1.503bn dual",
        "slrb",
        "Region / SISP tenants",
        "SLRB RA2025 bilan + amort table",
        "2025-12-31",
        2025,
        2035,
        1671720429,
        '{"debt_m":1671.72,"assets_m":2370.14,"equity_m":696.4,"sisp_loan_stock_start2026_m":1502.92,"capital_repay_2025_m":178.42,"interest_2025_m":15.07,"region_loan_2023_m":125,"guarantee_2024_m":150}',
        0,
        "active",
        URL,
        "Sustainable housing debt path",
        "Asset-sale repayment calendar FOI",
        SRC,
        "strong",
        "Bruxelles>SLRB>debt_path",
        "tick735",
    ),
    (
        "cmt_slrb_reno_155m_reception_2025",
        "Renovation receptions 155m (79 sites) + PSRD encours 141m",
        "slrb",
        "SISP tenants ~42k units class",
        "SLRB RA2025 renovation residual",
        "2025-12-31",
        2025,
        2025,
        155000000,
        '{"reception_m":155,"heavy_m":71,"envelope_m":69,"interior_m":15,"tech_m":20,"psrd_encours_m":141.4,"psrd_eng_m":55.0,"old_quad_encours_m":125.7,"sisp_renovations_count":3037}',
        0,
        "active",
        URL,
        "Sustainable renovation of social stock",
        "PSRD 2026-35 cash FOI dual VL",
        SRC,
        "strong",
        "Bruxelles>SLRB>renovation",
        "tick735",
    ),
    (
        "cmt_slrb_ars_societal_81_9m",
        "Societal stack ARS 52.5 + large-fam 15.3 + PCS 4.5 + SASLS 4.1",
        "slrb",
        "SISP tenants / social ASBL",
        "SLRB RA2025 mission societale residual",
        "2025-12-31",
        2025,
        2025,
        81887767,
        '{"ars_m":52.548,"large_fam_m":15.272,"pcs_m":4.463,"sasls_m":4.136,"other_subs_m":5.469,"rent_arrears_m":19.207}',
        0,
        "active",
        URL,
        "Rent affordability + social support",
        "Top20 SISP ARS split FOI",
        SRC,
        "strong",
        "Bruxelles>SLRB>societal",
        "tick735",
    ),
    (
        "cmt_dual_slrb_vmsw_swl_tick735",
        "Dual SLRB RA2025 residual vs VMSW/SWL social housing finance",
        "gg_belgium",
        "BE social housing dual map",
        "SLRB RA2025 + prior VMSW/SWL duals",
        "2026-06-18",
        2025,
        2025,
        802689567,
        '{"slrb_liq_m":802.7,"slrb_debt_m":1672,"slrb_encours_m":1131,"slrb_sisp_loans_m":1503,"vmsw_debt_m":3123,"swl_sec_dep_m":366,"wal_housing_sec_class_m":703,"note":"not TE-additive dual housing OIPs"}',
        0,
        "active",
        URL,
        "Comparable regional social housing finance",
        "Dual unit-cost dwellings FOI",
        SRC_DUAL,
        "strong",
        "Belgium>dual>SLRB_VMSW_SWL",
        "tick735",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_slrb_liq_802_7m_2025",
        "SLRB liq exec 802.7m 2025 — largest Brussels housing OIP residual",
        "Brussels",
        "ops",
        "Bruxelles>SLRB>budget_exec_2025",
        802689567,
        0,
        "Strong RA2025: construction 326.5 renovation 172.7 subsistence 221.6 (capital repay 178.4) societal 81.9; dual VMSW/SWL",
        "strong",
        SRC,
        "Social housing tenants Brussels",
        "Public housing finance",
        "Scale dual opacity unit-cost",
        6.0,
        8.5,
        4,
        7.05,
        "Unit-cost per dwelling FOI dual",
        "seed",
        "",
        "tick735",
    ),
    (
        "lb_slrb_prl_own_fund_gap_577m",
        "PRL/AH own-fund gap 577m Region rec vs spend",
        "Brussels",
        "ops",
        "Bruxelles>SLRB>PRL_AH_gap",
        577230000,
        0,
        "Strong comptes: Region subs rec 387.66 vs spend 964.89; structural pre-financing dual",
        "strong",
        SRC,
        "Region / SISP",
        "Multi-year housing plans",
        "Structural own-fund pre-finance",
        7.0,
        8.0,
        4,
        7.1,
        "Region advance calendar FOI",
        "seed",
        "",
        "tick735",
    ),
    (
        "lb_slrb_debt_1_672bn",
        "SLRB BS debt 1.672bn + SISP loans 1.503bn dual VMSW 3.12bn",
        "Brussels",
        "ops",
        "Bruxelles>SLRB>debt_path",
        1671720429,
        0,
        "Strong bilan: debt +87.6m; capital repay 178.4 interest 15.1; region loan 125 to repay via asset sales",
        "strong",
        SRC,
        "Taxpayers / tenants",
        "Sustainable debt path",
        "High stock dual housing finance",
        6.5,
        8.5,
        4,
        7.15,
        "Asset-sale repayment FOI",
        "seed",
        "",
        "tick735",
    ),
    (
        "lb_slrb_encours_1_131bn",
        "Engagements encours 1.131bn (-34pct) dual housing investment stock",
        "Brussels",
        "ops",
        "Bruxelles>SLRB>encours",
        1131471548,
        0,
        "Strong: -593m vs 2024 mainly fewer new construction launches; PSRD 141 + old quad 126 residual",
        "strong",
        SRC,
        "Construction / renovation pipeline",
        "Pipeline delivery",
        "Stock vs annual dual",
        6.0,
        8.0,
        3,
        6.6,
        "Programme-level encours FOI",
        "seed",
        "",
        "tick735",
    ),
    (
        "lb_slrb_ars_52_5m_l5",
        "ARS solidarity 52.5m to SISP without public SISP matrix L5",
        "Brussels",
        "ops",
        "Bruxelles>SLRB>ARS",
        52548000,
        0,
        "Strong aggregate; FOI for per-SISP split dual rent-gap mechanism",
        "strong",
        SRC,
        "SISP with rent gap",
        "Cover social rent vs base rent gap",
        "End-receiver opacity",
        6.0,
        6.5,
        3,
        6.05,
        "Top16 SISP ARS FOI",
        "seed",
        "",
        "tick735",
    ),
    (
        "lb_slrb_rent_arrears_19_2m",
        "Tenant rent arrears 19.2m sector residual dual recovery",
        "Brussels",
        "ops",
        "Bruxelles>SLRB>rent_arrears",
        19206803,
        0,
        "Strong RA2025 annex: mean real rent 413.5 base 660; dual Foyer Anderlechtois recovery flags",
        "strong",
        SRC,
        "SISP tenants",
        "Rent recovery",
        "Collection weakness dual",
        6.5,
        5.5,
        3,
        5.95,
        "Per-SISP arrears FOI",
        "seed",
        "",
        "tick735",
    ),
    (
        "lb_dual_slrb_vmsw_swl_asymmetry",
        "Dual SLRB 803m liq / 1.67bn debt vs VMSW 3.12bn debt / SWL SEC 366m",
        "Belgium",
        "ops",
        "Belgium>dual>SLRB_VMSW_SWL",
        802689567,
        0,
        "Strong dual residual not TE-additive: three regional social-housing finance towers; unit-cost opaque",
        "strong",
        SRC_DUAL,
        "BE social housing dual",
        "Comparable housing OIP transparency",
        "Asymmetric dual residual",
        7.0,
        8.0,
        4,
        7.1,
        "Dual unit-cost FOI matrix",
        "seed",
        "",
        "tick735",
    ),
]

with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in lbs:
        w.writerow(r)
print("leaderboard +", len(lbs))

sources = [
    (
        SRC,
        "SLRB Rapport annuel 2025 residual dual VMSW/SWL housing",
        URL,
        "SLRB / BGHM",
        "2026-08-02",
        "official_annual_report",
        "Strong tick735: liq exec 802.7 of 1005.4; eng 597.2 of 689.2; SPRB rec 284.6; construction 326.5 reno 172.7 subsistence 221.6 societal 81.9; ARS 52.5; encours 1.131bn; BS debt 1.672 assets 2.370; SISP loans 1.503bn; PRL own-fund gap 577; rent arrears 19.2; 572 dwellings 3037 renovations; page "
        + URL_PAGE
        + "; raw slrb_ra2025.pdf",
    ),
    (
        SRC_DUAL,
        "Dual SLRB RA2025 residual vs VMSW/SWL social housing tick735",
        URL,
        "DOGE synthesis SLRB + VMSW + SWL",
        "2026-08-02",
        "synthesis",
        "Strong dual not TE-additive: SLRB liq 802.7 debt 1.672 encours 1.131 vs VMSW debt 3.123 SWL SEC dep 366 WAL housing SEC class 703; tick735",
    ),
]

with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in sources:
        w.writerow(r)
print("sources +", len(sources))

rq_path = DATA / "research_queue.csv"
rows = []
with open(rq_path, encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_726":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick735 SLRB RA2025 residual dual VMSW/SWL: liq 802.7; debt 1.672bn; "
                "encours 1.131; PRL gap 577; ARS 52.5; FOI gap_slrb_ra2025_residual_l5 ready"
            )
        rows.append(row)

rows.append({
    "task_id": "rq_727",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "continuous",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "gg_belgium",
    "instructions": (
        "Next residual: new CoA/primary PDF not yet mined or SWL/SWCS dual VMSW residual "
        "or FLRBC residual dual housing or Entity II dual residual"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": "",
    "notes": "spawned tick735 after rq_726",
})

with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("rq_726=done spawn rq_727")

foi_row = (
    "gap_slrb_ra2025_residual_l5",
    "Bruxelles>SLRB>RA2025_residual_L5",
    "slrb",
    (
        "Machine-readable L5: (1) per-SISP ARS 52.548m and large-family rent cuts 15.272m 2025; "
        "(2) per-SISP renovation advances/subsidies split of 49.036+90.001m and LT loans 32.097m; "
        "(3) PRL/AH own-fund gap 577m reconciliation cash-by-year Region vs SLRB; "
        "(4) asset-sale calendar Ariane/Palais/~200 units for region loan 125m repayment; "
        "(5) unit-cost per dwelling construction and renovation dual VMSW/SWL; "
        "(6) per-SISP rent arrears of 19.207m sector total"
    ),
    (
        "RA2025 fills strong aggregates and named programme lines but SISP-level L5 and dual "
        "unit-cost vs Flanders VMSW / Wallonia SWL still opaque for waste ranking"
    ),
    "8",
    "SLRB / BGHM publicité / Bruxelles Logement",
    "transparence@sprb.brussels",
    "https://slrb-bghm.brussels",
    "docs/doge/foi/drafts/gap_slrb_ra2025_residual_l5.md",
    "ready",
    "2026-08-02",
    "",
    "",
    "",
    "",
    "cmt_slrb_liq_exec_802_7m_2025|cmt_slrb_prl_own_fund_gap_577m|cmt_slrb_ars_societal_81_9m",
    "lb_slrb_liq_802_7m_2025|lb_slrb_prl_own_fund_gap_577m|lb_dual_slrb_vmsw_swl_asymmetry",
    UTC,
    UTC,
    "tick735 SLRB RA2025 residual dual; ready not sent; prior gap_bru_proprete_slrb_routes_l5 remains",
)

with open(DATA / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(foi_row)
print("foi + gap_slrb_ra2025_residual_l5")

with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow([
        "state_id", "mode", "current_sprint", "last_tick_utc", "last_unit_id",
        "ticks_completed", "paused", "notes",
    ])
    w.writerow([
        "main", "continuous", "hole_fill", UTC, "rq_726", "735", "no",
        "tick735 SLRB RA2025 residual dual VMSW/SWL; next rq_727; progress@740 in 5; rq_116 deferred",
    ])
print("loop_state ticks=735")

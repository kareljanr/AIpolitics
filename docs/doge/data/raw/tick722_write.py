# tick722 — fed VVPR/Pillar2 residual recheck CoA 2026_22 dual
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]

budgets = [
    ("bud_vvpr_jan_apr_2026_plus_406_3m", "fod_finance", 2026, 406300000, "", "", "outturn", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "VVPRbis receipts Jan-Apr 2026 +406.3m vs same period 2025 CoA; tick722"),
    ("bud_vvpr_exceptional_402_1m_15pct_2026", "fod_finance", 2026, 402100000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "RV exceptional VVPR-bis at still-15pct 402.1m due delayed progwet CoA p28; tick722"),
    ("bud_vvpr_tech_corr_2025_minus_402_1m", "fod_finance", 2025, -402100000, "", "", "outturn", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Technical correction -402.1m neutralizing 2025 anticipation spike CoA; tick722"),
    ("bud_vvpr_bis_conclave_add_334_5m", "fod_finance", 2026, 334500000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Conclave adds 334.5m VVPR residual after prior +67.6 already in base; tick722"),
    ("bud_vvpr_prior_base_plus_67_6m", "fod_finance", 2026, 67600000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Base 2026 already included +67.6m VVPR behaviour before conclave top-up; tick722"),
    ("bud_rv_total_path_plus_403_7m_2026", "fod_finance", 2026, 403700000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Roerende voorheffing total path +403.7m 2026 (+5.1pct) incl VVPR exceptional; tick722"),
    ("bud_pillar2_ib_32m_2026", "fod_finance", 2026, 32000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Pillar2 minimum tax IB 2026 +32m; tick722"),
    ("bud_pillar2_bc_minus_87m_2026", "fod_finance", 2026, -87000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Pillar2 BC 2026 -87m; slip -119 vs IB; tick722"),
    ("bud_pillar2_slip_119m_2026", "fod_finance", 2026, -119000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Pillar2 reestimate slip -119m 2026 CoA table; tick722"),
    ("bud_pillar2_slip_184m_2027", "fod_finance", 2027, -184000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Pillar2 reestimate slip -184m 2027 CoA; tick722"),
    ("bud_pillar2_filing_deadline_2026_09_30", "fod_finance", 2026, 1, "", "", "outturn", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Pillar2 AY2025 filings deferred to 30 Sep 2026 CoA; tick722"),
    ("bud_vat_reform_ib_580_5m", "fod_finance", 2026, 580500000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "VAT reform IB impact +580.5m; tick722"),
    ("bud_vat_reform_bc_177m", "fod_finance", 2026, 177000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "VAT reform BC +177m slip -403.5; tick722"),
    ("bud_vat_reform_slip_403_5m", "fod_finance", 2026, -403500000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "VAT reform reestimate slip -403.5m vs IB; tick722"),
    ("bud_vat_chain_cash_lag_2025_520_9m", "fod_finance", 2025, 520900000, "", "", "outturn", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "VAT chain reform 2025 lower cash receipts 520.9m CoA; tick722"),
    ("bud_gas_excise_ib_91m", "fod_finance", 2026, 91000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Gas excise hike IB +91m; tick722"),
    ("bud_gas_excise_bc_21_2m", "fod_finance", 2026, 21200000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Gas excise BC +21.2m slip -69.8; tick722"),
    ("bud_elec_social_tariff_minus_23_3m", "fod_finance", 2026, -23300000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Electricity excise cut protected clients -23.3m; tick722"),
    ("bud_elec_residential_bc_minus_30_6m", "fod_finance", 2026, -30600000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Electricity residential excise cut BC -30.6m (IB -50); tick722"),
    ("bud_authors_rights_software_cost_142_1m", "fod_finance", 2026, -142100000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "medium", "Authors rights scope expand software -142.1m annual; FOD keeps estimate CoA; tick722"),
    ("bud_authors_rights_forfait_remove_39m", "fod_finance", 2026, 39000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Remove forfait cost deduction authors rights +39m annual; lag until law publish; tick722"),
    ("bud_pit_reform_half_shift_96m", "fod_finance", 2026, 96000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "PIT reform payroll withholding from Jul shifts H1 cost 96m to 2027-28 rolls; tick722"),
    ("bud_pit_reform_extra_delay_48m", "fod_finance", 2026, 48000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "medium", "If law delay to Sep another 48m of 2026 cost slides to 2027-28 CoA; tick722"),
    ("bud_fiscal_measures_net_1830_8m_2026", "fod_finance", 2026, 1830800000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Net fiscal measures impact 2026 +1830.8m (prior +1099.9 + conclave +730.9); tick722"),
    ("bud_fiscal_conclave_new_730_9m", "fod_finance", 2026, 730900000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Conclave 3 Apr new fiscal measures +730.9m; tick722"),
    ("bud_fiscal_prior_measures_1099_9m", "fod_finance", 2026, 1099900000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Prior decided fiscal measures impact +1099.9m 2026; tick722"),
    ("bud_fiscal_receipts_esr_164541m_2026", "fod_finance", 2026, 164541200000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Fiscal receipts ESR after conclave 164541.2m; tick722"),
    ("bud_fiscal_base_fod_163810m_2026", "fod_finance", 2026, 163810400000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "FOD Finance base fiscal ESR 163810.4m; tick722"),
    ("bud_mr_apr3_improve_615m", "sec_federal", 2026, 615000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "MR 3 Apr improves MC balance +615m; tick722"),
    ("bud_mr_apr3_tech_517m", "sec_federal", 2026, 517000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Of +615 technical ~517m (customs+VVPRbis 475 + defer 187 - reinteg -112); tick722"),
    ("bud_mr_apr3_vvpr_customs_475m", "sec_federal", 2026, 475000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Customs reest + VVPRbis reest cluster ~475m of technical package; tick722"),
    ("bud_mr_apr3_decisions_98m", "sec_federal", 2026, 98000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Non-technical government decisions net ~+98m of 615; tick722"),
    ("bud_control_staff_cut_reverse_179m", "fod_finance", 2026, 179000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Reverse negative impact of staff cuts on tax/SS control 179m; tick722"),
    ("bud_eu_handling_fee_77_4m_unalloc", "fod_finance", 2026, 77400000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "medium", "EU handling fee est 77.4m from Nov 2026 unallocated correction law not final; tick722"),
    ("bud_entity1_deficit_24_5bn_2026", "sec_federal", 2026, 24500000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Entity I financing deficit after measures 24.5bn 2026 (-3.7pct GDP); tick722"),
    ("bud_entity1_deficit_36_2bn_2029", "sec_federal", 2029, 36200000000, "", "", "projected", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Entity I path deficit 36.2bn 2029 (-5pct GDP) worsen +11.7bn vs Jan path +6.6; tick722"),
    ("bud_cit_path_plus_1224_8m_2026", "fod_finance", 2026, 1224800000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "CIT receipts +1224.8m 2026; advance payments include Russian assets 1016m; tick722"),
    ("bud_russian_assets_cit_1016m_2026", "fod_finance", 2026, 1016000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "CIT advance payments include 1016m frozen Russian assets class; tick722"),
    ("bud_dlui_regularisation_bc_126m", "fod_finance", 2026, 126000000, "", "", "budgeted", "src_ccrek_fed_aju_vvpr_pillar2_2026", "strong", "Fiscal regularisation BC +126m (IB 84 path +42); tick722"),
    ("bud_dual_vvpr_pillar2_tick722", "gg_belgium", 2026, 402100000, "", "", "budgeted", "src_dual_vvpr_pillar2_tick722", "strong", "Dual residual VVPR anticipation + Pillar2 slip; not TE-additive; tick722"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_vvpr_bis_anticipation_wave_2025_26",
        "VVPRbis anticipation wave 15pct before rate hike dual residual",
        "fod_finance",
        "SME dividend payers federal budget",
        "CoA 2026_22 fed aju + programme law path 15 to 18pct",
        "2025-01-01",
        2025,
        2026,
        402100000,
        '{"exceptional_2026_m":402.1,"tech_corr_2025_m":-402.1,"jan_apr_2026_delta_m":406.3,"conclave_add_m":334.5,"prior_base_m":67.6,"rate_still_15pct_until_law":true,"coa":"future_years_reverse_risk"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Budget2026A1.pdf",
        "Raise withholding rate; firms front-load dividends",
        "Publish monthly VVPR series and multi-year reverse FOI",
        "src_ccrek_fed_aju_vvpr_pillar2_2026",
        "strong",
        "Federal>tax>VVPRbis",
        "tick722",
    ),
    (
        "cmt_pillar2_reestimate_slip_2026_27",
        "Pillar2 minimum tax reestimate slip -119m/-184m dual residual",
        "fod_finance",
        "Multinational groups federal budget",
        "CoA 2026_22 + OECD SbS package",
        "2026-01-01",
        2026,
        2027,
        -303000000,
        '{"ib_2026_m":32,"bc_2026_m":-87,"slip_2026_m":-119,"slip_2027_m":-184,"filing_deadline":"2026-09-30","sbs_us_effects":"not_yet","coa":"high_uncertainty"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Budget2026A1.pdf",
        "OECD global minimum tax revenue",
        "Publish filing outturn and SbS map FOI",
        "src_ccrek_fed_aju_vvpr_pillar2_2026",
        "strong",
        "Federal>tax>Pillar2",
        "tick722",
    ),
    (
        "cmt_vat_reform_slip_403_5m",
        "VAT reform budget slip -403.5m IB to BC dual residual",
        "fod_finance",
        "Federal VAT receipts",
        "CoA 2026_22 table measures",
        "2026-01-01",
        2026,
        2026,
        -403500000,
        '{"ib_m":580.5,"bc_m":177,"slip_m":-403.5,"vat_chain_2025_cash_lag_m":520.9}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Budget2026A1.pdf",
        "Modernise VAT chain and rates",
        "Track cash vs ESR FOI",
        "src_ccrek_fed_aju_vvpr_pillar2_2026",
        "strong",
        "Federal>tax>VAT_reform",
        "tick722",
    ),
    (
        "cmt_mr_apr3_technical_package_615m",
        "MR 3 Apr 2026 technical balance package +615m dual residual",
        "sec_federal",
        "Entity I financing balance",
        "CoA 2026_22 s1.3 + general exposition",
        "2026-04-03",
        2026,
        2026,
        615000000,
        '{"total_m":615,"technical_m":517,"vvpr_customs_m":475,"defer_prison_space_m":187,"reinteg_shortfall_m":-112,"decisions_net_m":98,"control_reverse_m":179}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Budget2026A1.pdf",
        "Close MC deficit gap at BA",
        "Separate genuine policy from reestimates FOI",
        "src_ccrek_fed_aju_vvpr_pillar2_2026",
        "strong",
        "Federal>BA2026>MR_apr3",
        "tick722",
    ),
    (
        "cmt_entity1_path_24_5_to_36_2bn",
        "Entity I deficit path 24.5bn 2026 to 36.2bn 2029 dual residual",
        "sec_federal",
        "Federal+SS Entity I",
        "CoA 2026_22 multi-year after MR measures",
        "2026-01-01",
        2026,
        2029,
        36200000000,
        '{"2026_bn":24.5,"2026_gdp_pct":-3.7,"2029_bn":36.2,"2029_gdp_pct":-5.0,"worsen_bn":11.7,"jan_path_worsen_bn":6.6}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Budget2026A1.pdf",
        "Stabilize Entity I path",
        "Publish measure-by-measure multi-year FOI",
        "src_ccrek_fed_aju_vvpr_pillar2_2026",
        "strong",
        "Federal>Entity1>path",
        "tick722",
    ),
    (
        "cmt_dual_vvpr_pillar2_tick722",
        "Dual VVPR anticipation vs Pillar2 slip residual",
        "gg_belgium",
        "Federal tax base firms multinationals",
        "CoA 2026_22 dual residual",
        "2025-01-01",
        2025,
        2027,
        402100000,
        '{"vvpr_exceptional_m":402.1,"pillar2_slip_2026_27_m":-303,"note":"not TE-additive; opposite timing risks"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Budget2026A1.pdf",
        "Map fiscal front-loading vs multi-year erosion",
        "Open series FOI",
        "src_dual_vvpr_pillar2_tick722",
        "strong",
        "Belgium>dual>VVPR_Pillar2",
        "tick722",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_vvpr_anticipation_402m_15pct",
        "VVPRbis exceptional 402m at still-15pct 2026",
        "federal",
        "tax_expenditure",
        "Federal>tax>VVPRbis_anticipation",
        402100000,
        402100000,
        "Strong CoA: 402.1m exceptional RV from dividends still at 15pct due delayed progwet; Jan-Apr +406.3",
        "strong",
        "src_ccrek_fed_aju_vvpr_pillar2_2026",
        "SME shareholders federal budget",
        "Rate hike to 18pct; front-load at 15pct",
        "Behavioural front-load risks reverse later years",
        8.0,
        7.5,
        4,
        7.55,
        "Lock rate path; publish multi-year reverse FOI",
        "seed",
        "",
        "tick722",
    ),
    (
        "lb_pillar2_slip_minus_119m",
        "Pillar2 estimate slips to -87m 2026 (-119 vs IB)",
        "federal",
        "tax_expenditure",
        "Federal>tax>Pillar2_slip",
        119000000,
        303000000,
        "Strong CoA: IB +32 to BC -87; 2027 -184; filing delay Sep2026; high uncertainty",
        "strong",
        "src_ccrek_fed_aju_vvpr_pillar2_2026",
        "MNEs federal budget",
        "OECD global minimum tax yield",
        "Headline revenue evaporates on reestimate",
        8.0,
        6.5,
        5,
        7.05,
        "Publish filings and SbS map FOI",
        "seed",
        "",
        "tick722",
    ),
    (
        "lb_vat_reform_slip_403_5m",
        "VAT reform yield slips -403.5m IB to BC",
        "federal",
        "ops",
        "Federal>tax>VAT_slip",
        403500000,
        580500000,
        "Strong CoA: 580.5 to 177; plus 2025 cash lag 520.9 from chain reform",
        "strong",
        "src_ccrek_fed_aju_vvpr_pillar2_2026",
        "Federal VAT base",
        "VAT modernisation receipts",
        "Optimistic IB not sustained at BA",
        7.5,
        7.5,
        4,
        7.25,
        "Cash vs ESR reconciliation FOI",
        "seed",
        "",
        "tick722",
    ),
    (
        "lb_mr_apr3_technical_fiction_517m",
        "MR Apr3 technical package 517m of 615 balance fix",
        "federal",
        "ops",
        "Federal>BA>MR_technical",
        517000000,
        615000000,
        "Strong CoA: 517 of 615 is reestimate/defer (VVPR+customs 475; prison/space defer 187; reinteg -112)",
        "strong",
        "src_ccrek_fed_aju_vvpr_pillar2_2026",
        "Parliament budget control",
        "Honest BA balance improvement",
        "Balance fixed mainly by timing and reestimates",
        8.0,
        7.5,
        4,
        7.55,
        "Label technical vs policy in BA FOI",
        "seed",
        "",
        "tick722",
    ),
    (
        "lb_entity1_path_worsen_11_7bn",
        "Entity I deficit path worsens +11.7bn to 36.2bn 2029",
        "federal",
        "ops",
        "Federal>Entity1>path_worsen",
        11700000000,
        36200000000,
        "Strong CoA: 24.5bn 2026 to 36.2bn 2029 (-5pct GDP); Jan path only +6.6bn worsen",
        "strong",
        "src_ccrek_fed_aju_vvpr_pillar2_2026",
        "Taxpayers Entity I",
        "Stabilize multi-year path",
        "Path deterioration accelerates vs initial plan",
        8.0,
        9.5,
        7,
        8.25,
        "Publish full multi-year measure matrix FOI",
        "seed",
        "",
        "tick722",
    ),
    (
        "lb_russian_assets_cit_1016m",
        "CIT advances include 1.016bn frozen Russian assets class",
        "federal",
        "ops",
        "Federal>tax>Russian_assets_CIT",
        1016000000,
        1016000000,
        "Strong CoA: CIT advance payments contain 1016m frozen Russian assets related receipts",
        "strong",
        "src_ccrek_fed_aju_vvpr_pillar2_2026",
        "Federal budget",
        "One-off geo-financial receipts",
        "One-off inflates CIT path; not structural",
        7.0,
        9.0,
        5,
        7.7,
        "Separate structural CIT FOI",
        "seed",
        "",
        "tick722",
    ),
    (
        "lb_dual_vvpr_pillar2_2026",
        "Dual VVPR front-load vs Pillar2 slip residual",
        "Belgium",
        "ops",
        "Belgium>dual>VVPR_Pillar2",
        402100000,
        0,
        "Strong dual residual: short-term VVPR windfall vs multi-year Pillar2 erosion; not TE-additive",
        "strong",
        "src_dual_vvpr_pillar2_tick722",
        "Federal fiscal path",
        "Honest multi-year tax base",
        "Opposite timing risks in same BA",
        7.5,
        7.5,
        5,
        7.25,
        "Joint multi-year FOI dashboard",
        "seed",
        "",
        "tick722",
    ),
]

with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in lbs:
        w.writerow(r)
print("leaderboard +", len(lbs))

srcs = [
    (
        "src_ccrek_fed_aju_vvpr_pillar2_2026",
        "CoA fed budget aju 2026_22 VVPR Pillar2 residual dual",
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Budget2026A1.pdf",
        "Cour des comptes / Rekenhof AG 21 May 2026",
        "2026-08-01",
        "audit",
        "Strong primary residual recheck tick722",
    ),
    (
        "src_dual_vvpr_pillar2_tick722",
        "Dual VVPR anticipation vs Pillar2 slip residual",
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Budget2026A1.pdf",
        "DOGE synthesis CoA dual",
        "2026-08-01",
        "synthesis",
        "Strong dual fiscal residual tick722",
    ),
]

with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in srcs:
        w.writerow(r)
print("sources +", len(srcs))

foi = (
    "gap_fed_vvpr_pillar2_series_l5",
    "Federal>tax>VVPRbis_Pillar2_L5",
    "fod_finance",
    "Monthly VVPRbis RV series 2024-2026 by rate band; multi-year reverse risk model after 18pct; Pillar2 filings after 2026-09-30 with country SbS map; split of 475m customs vs VVPR technical package; dual reverse-year projections",
    "BA books 402m exceptional + 334.5m behaviour while Pillar2 slips -119/-184; CoA flags future reverse risk",
    "6",
    "FPS Finance Studiedienst / FOD Financiën",
    "",
    "",
    "docs/doge/foi/drafts/gap_fed_vvpr_pillar2_series_l5.md",
    "ready",
    "2026-08-01",
    "",
    "",
    "",
    "",
    "cmt_vvpr_bis_anticipation_wave_2025_26",
    "lb_vvpr_anticipation_402m_15pct",
    "2026-08-01T22:15:00Z",
    "2026-08-01T22:15:00Z",
    "tick722 CoA residual recheck; not sent; contacts TBD",
)
with open(DATA / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(foi)
print("foi +1")

rq_path = DATA / "research_queue.csv"
with open(rq_path, "r", encoding="utf-8", newline="") as f:
    r = csv.reader(f)
    header = next(r)
    rows = [header]
    for row in r:
        if row and row[0] == "rq_713":
            row[4] = "done"
            row[10] = "2026-08-01T22:15:00Z"
            row[11] = "tick722 VVPR 402/334/406 Pillar2 -119/-184 Entity1 path 24.5->36.2 dual; FOI gap_fed_vvpr_pillar2_series_l5 ready"
        rows.append(row)
ids = {row[0] for row in rows if row}
if "rq_714" not in ids:
    rows.append(
        [
            "rq_714",
            "Continuous FOI-adjacent public hole-fill batch",
            "continuous",
            "5",
            "open",
            "L5",
            "gg_belgium",
            "Next residual: UAP/OTW L5 or social assist savings fail residual CoA 2026_22 or new CoA PDF",
            "",
            "2026-08-01T22:15:00Z",
            "",
            "spawned tick722 after rq_713",
        ]
    )
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerows(rows)
print("research_queue updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T22:15:00Z,rq_713,722,no,tick722 VVPR/Pillar2 residual dual; next rq_714; progress@730 in 8; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")

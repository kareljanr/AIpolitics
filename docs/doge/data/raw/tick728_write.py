# tick728 — Toekomstverbond / Oosterweel BC2026 finance residual dual L5 (rq_719)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T00:45:00Z"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_18_Toekomstverbond.pdf"

SRC = "src_ccrek_tv6_bc2026_finance_residual"
SRC_DUAL = "src_dual_tv_bc2026_gip_tick728"

budgets = [
    # BC2026 headline recon + residual
    ("bud_owv_bc2026_assets_13614m", "lantis", 2033, 13614000000, "", "", "projection", SRC, "strong", "Materieel vaste activa OWV eoy build 13614m (+2729/+25.1pct vs BC2025 10885); tick728"),
    ("bud_owv_bc2026_assets_invest_10821m", "lantis", 2033, 10821400000, "", "", "projection", SRC, "strong", "Of which investments 10821.4m of 13614; tick728"),
    ("bud_owv_bc2026_intercalary_interest_2792m", "lantis", 2033, 2792000000, "", "", "projection", SRC, "strong", "Intercalary interest capitalized 2792m of 13614 assets; tick728"),
    ("bud_owv_bc2026_fin_need_8273m", "lantis", 2033, 8273491272, "", "", "projection", SRC, "strong", "Remaining net financing need build phase 8273.491m exact model; tick728"),
    ("bud_owv_bc2026_capex_remain_7275m", "lantis", 2033, 7274640000, "", "", "projection", SRC, "strong", "Remaining CAPEX 7274.64m (+16.80pct vs BC2025 6228.07); tick728"),
    ("bud_owv_bc2026_opex_remain_4464m", "lantis", 2083, 4463800000, "", "", "projection", SRC, "strong", "Remaining OPEX build+ops 4463.8m (ops phase 4146.5); understates Kennedy+Liefkenshoek reno; tick728"),
    ("bud_owv_bc2026_mra_973m", "lantis", 2083, 973000000, "", "", "projection", SRC, "strong", "Maintenance reserve account MRA 973m; tick728"),
    # Force majeure residual in CAPEX
    ("bud_owv_bc2026_pfas_remain_785_5m", "lantis", 2033, 785500000, "", "", "projection", SRC, "strong", "Remaining PFAS CAPEX in model 785.5m; tick728"),
    ("bud_owv_bc2026_other_fm_remain_951_6m", "lantis", 2033, 951600000, "", "", "projection", SRC, "strong", "Remaining other force majeure (asbestos soil disposal norms) 951.6m; tick728"),
    ("bud_owv_bc2026_fm_pack_1811m", "lantis", 2033, 1811000000, "", "", "projection", SRC, "strong", "PFAS+other FM residual CAPEX pack 1811m; tick728"),
    ("bud_owv_bc2026_contract_adj_225m", "lantis", 2033, 225000000, "", "", "projection", SRC, "strong", "Net contractual adjustments/meerwerken 225m in CAPEX rise; tick728"),
    ("bud_owv_bc2026_opex_remain_build_317_3m", "lantis", 2033, 317300000, "", "", "projection", SRC, "strong", "Remaining OPEX in build phase 2026-2033 317.3m; tick728"),
    # CAPEX path by year BC2026
    ("bud_owv_capex_2026_bc", "lantis", 2026, 1220200000, "", "", "projection", SRC, "strong", "CAPEX path 2026 BC 1220.20m (+51.77pct vs BC2025 803.97); tick728"),
    ("bud_owv_capex_2027_bc", "lantis", 2027, 1185830000, "", "", "projection", SRC, "strong", "CAPEX path 2027 BC 1185.83m (+72.18pct); tick728"),
    ("bud_owv_capex_2028_bc", "lantis", 2028, 1142040000, "", "", "projection", SRC, "strong", "CAPEX path 2028 BC 1142.04m (+52.55pct); tick728"),
    ("bud_owv_capex_2029_bc", "lantis", 2029, 1104460000, "", "", "projection", SRC, "strong", "CAPEX path 2029 BC 1104.46m (+39.34pct); tick728"),
    ("bud_owv_capex_2030_bc", "lantis", 2030, 953150000, "", "", "projection", SRC, "strong", "CAPEX path 2030 BC 953.15m; tick728"),
    ("bud_owv_capex_2031_bc", "lantis", 2031, 765470000, "", "", "projection", SRC, "strong", "CAPEX path 2031 BC 765.47m; tick728"),
    ("bud_owv_capex_2032_bc", "lantis", 2032, 515030000, "", "", "projection", SRC, "strong", "CAPEX path 2032 BC 515.03m; tick728"),
    ("bud_owv_capex_2033_bc", "lantis", 2033, 388460000, "", "", "projection", SRC, "strong", "CAPEX path 2033 BC 388.46m; tick728"),
    # Project bonds
    ("bud_owv_bonds_total_bc2026_7751m", "lantis", 2033, 7751490000, "", "", "projection", SRC, "strong", "Project bonds total draw 7751.49m 2026-33; tick728"),
    ("bud_owv_bonds_plafond_5500m", "lantis", 2033, 5500000000, "", "", "budgeted", SRC, "strong", "Agreed VL project-bond plafond 5500m; Lantis says no revise this legislature; tick728"),
    ("bud_owv_bonds_over_plafond_2251_5m", "lantis", 2033, 2251500000, "", "", "projection", SRC, "strong", "Bonds 7751.5 minus plafond 5500 = shortfall 2251.5m (+40.9pct); CoA: sources insufficient; tick728"),
    ("bud_owv_bonds_2026_956m", "lantis", 2026, 956280000, "", "", "projection", SRC, "strong", "First project bonds Oct2026 956.28m @3.98pct; tick728"),
    ("bud_owv_bonds_2027_1209m", "lantis", 2027, 1209240000, "", "", "projection", SRC, "strong", "Bonds 2027 1209.24m; tick728"),
    ("bud_owv_bonds_2028_1212m", "lantis", 2028, 1212240000, "", "", "projection", SRC, "strong", "Bonds 2028 1212.24m; tick728"),
    ("bud_owv_bonds_2029_1221m", "lantis", 2029, 1221200000, "", "", "projection", SRC, "strong", "Bonds 2029 1221.20m; tick728"),
    ("bud_owv_bonds_2030_1020m", "lantis", 2030, 1019880000, "", "", "projection", SRC, "strong", "Bonds 2030 1019.88m; tick728"),
    ("bud_owv_bond_rate_3_98pct", "lantis", 2026, 3.98, "", "", "projection", SRC, "strong", "PCT bond assumed rate 3.98 (OLO~3.30 + spread 0.60); tick728"),
    ("bud_owv_bond_spread_60bp", "lantis", 2025, 0.60, "", "", "budgeted", SRC, "strong", "PCT spread cut 100->60bp 2nd addendum kaderovereenkomst 5Dec2025; tick728"),
    ("bud_owv_bond_interest_to_2035_1905m", "lantis", 2035, 1905200000, "", "", "projection", SRC, "strong", "Interest on project bonds to eoy2035 1905.2m; tick728"),
    # Refinance / LT loan path
    ("bud_owv_lt_loan_convert_2035_7751m", "lantis", 2035, 7751500000, "", "", "projection", SRC, "strong", "All project bonds convert eoy2035 to VL LT loan 7751.5m @4pct 13y sculpted; tick728"),
    ("bud_owv_lt_loan_interest_2036_74_9578m", "lantis", 2074, 9577700000, "", "", "projection", SRC, "strong", "Interest on successive 13y LT loans 2036-2074 9577.7m; tick728"),
    ("bud_owv_lt_loan_repay_start_2045", "lantis", 2045, 0, "", "", "projection", SRC, "strong", "Model: sculpted repay of 7751.5 LT loan can start H1 2045 full by H2 2074; tick728 COUNT_year"),
    # Subordinated loans snowball
    ("bud_owv_subloan_plafond_2850m", "lantis", 2026, 2850000000, "", "", "budgeted", SRC, "strong", "Sub shareholder loan plafond raised Dec2025 1200->2850m (+1650 FM); tick728"),
    ("bud_owv_subloan_extra_1650m", "lantis", 2026, 1650000000, "", "", "budgeted", SRC, "strong", "Extra sub loan 1650m for force majeure assigned to model; CoA unjustified policy; tick728"),
    ("bud_owv_subloan_drawn_eoy2025_1128m", "lantis", 2025, 1128000000, "", "", "outturn", SRC, "strong", "Extra sub already drawn 1128m eoy2025 @5pct; tick728"),
    ("bud_owv_subloan_last_tranche_522m_2026", "lantis", 2026, 522000000, "", "", "projection", SRC, "strong", "Last sub tranche 522m H1 2026 to fill 2850; tick728"),
    ("bud_owv_subloan_eoy2083_27046m", "lantis", 2083, 27046400000, "", "", "projection", SRC, "strong", "Outstanding sub debt eoy2083 27046.4m incl capitalized interest; no principal repay 2034-83; tick728"),
    ("bud_owv_subloan_cap_interest_24338m", "lantis", 2083, 24338400000, "", "", "projection", SRC, "strong", "Capitalized deferred interest on sub loans 24338.4m to eoy2083; tick728"),
    ("bud_owv_subloan_interest_paid_12945m", "lantis", 2083, 12945200000, "", "", "projection", SRC, "strong", "Sub loan interest actually paid 2044-83 only 12945.2m; first pay H2 2044 39.4m; tick728"),
    ("bud_owv_sub_debt_at_herijk_2035_4800m", "lantis", 2035, 4800200000, "", "", "projection", SRC, "strong", "Sub debt incl cap interest at herijking eoy2035 4800.2m; tick728"),
    ("bud_owv_vl_must_takeover_herijk_2822m", "vlaanderen_gov", 2035, 2822300000, "", "", "projection", SRC, "strong", "CoA calc: VL must take over min 2822.3m (58.8pct of 4800) at 2035 herijking; tick728 recon prior"),
    ("bud_owv_model_can_bear_sub_1978m", "lantis", 2035, 1977900000, "", "", "projection", SRC, "strong", "Model-bearable sub share at herijking 1977.9m (41.2pct); tick728"),
    ("bud_owv_extra_sub_1650_to_26620m_snowball", "lantis", 2083, 26620000000, "", "", "projection", SRC, "strong", "CoA: extra 1.65bn alone compounds to ~26.62bn eoy2083 at 5pct/57y; tick728"),
    # Interest total paid
    ("bud_owv_interest_paid_total_24495m", "lantis", 2083, 24495000000, "", "", "projection", SRC, "strong", "Total interest paid 2026-2083 24495m (CP 66.9 + bonds 1905.2 + LT 9577.7 + sub paid 12945.2); tick728"),
    ("bud_owv_cp_interest_66_9m", "lantis", 2033, 66900000, "", "", "projection", SRC, "strong", "Commercial paper interest build phase 66.9m; rate assump 2.83pct; tick728"),
    ("bud_owv_toll_ops_phase_35429m", "lantis", 2083, 35429000000, "", "", "projection", SRC, "strong", "Modelled toll revenues ops phase 35429m (BC2025 was 35640); tick728"),
    # Land loan
    ("bud_owv_land_loan_176_5m", "lantis", 2004, 176500000, "", "", "outturn", SRC, "strong", "VL land loan 176.5m 2004 Zwijndrecht; BC2026 repay H2 2037-eoy2041; no interest since 2024; tick728"),
    # MJR booking gap dual budget
    ("bud_owv_debt_draw_planned_2026_1478m", "lantis", 2026, 1478280000, "", "", "projection", SRC, "strong", "Planned debt draw 2026 bonds 956.28 + sub 522 = 1478.28m; tick728"),
    ("bud_owv_debt_budgeted_mjr_2026_775m", "vlaanderen_gov", 2026, 775000000, "", "", "budgeted", SRC, "strong", "VL MJR budgeted Lantis debt draw 2026 only 775m; tick728"),
    ("bud_owv_debt_mjr_gap_2026_703m", "vlaanderen_gov", 2026, 703280000, "", "", "estimate", SRC, "strong", "MJR underbooking 2026 1478.28-775=703.28m (41.9pct of multi-year gap); tick728"),
    ("bud_owv_debt_planned_2026_30_6141m", "lantis", 2030, 6140840000, "", "", "projection", SRC, "strong", "Planned debt draws 2026-30 sum 6140.84m; tick728"),
    ("bud_owv_debt_budgeted_mjr_2026_30_4461m", "vlaanderen_gov", 2030, 4461070000, "", "", "budgeted", SRC, "strong", "VL MJR budgeted Lantis draws 2026-30 4461.07m; tick728"),
    ("bud_owv_debt_mjr_gap_2026_30_1680m", "vlaanderen_gov", 2030, 1679770000, "", "", "estimate", SRC, "strong", "MJR multi-year underbooking 1679.77m 2026-30 CoA Table7; tick728"),
    # Dual
    ("bud_dual_tv_bonds_over_plafond_gip", "gg_belgium", 2033, 2251500000, "", "", "estimate", SRC_DUAL, "strong", "Dual residual: OWV bond over-plafond 2251.5m vs GIP/MJR incomplete booking; not TE-additive; tick728"),
    ("bud_dual_tv_sub_snowball_vs_gip", "gg_belgium", 2083, 27046400000, "", "", "estimate", SRC_DUAL, "strong", "Dual residual: sub debt snowball 27.0bn eoy2083 vs GIP 2025-27 short horizon; not TE-additive; tick728"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_owv_bonds_over_plafond_2251m",
        "Oosterweel project bonds 7.75bn vs 5.5bn plafond shortfall 2.25bn",
        "lantis",
        "VL taxpayers toll payers",
        "CoA TV6 BC2026 Table6 + kaderovereenkomst",
        "2025-12-05",
        2026,
        2033,
        7751490000,
        '{"bonds_m":7751.5,"plafond_m":5500,"over_m":2251.5,"over_pct":40.9,"rate_pct":3.98,"spread_bp":60,"first_draw_2026_m":956.28,"convert_2035":true,"lt_rate_pct":4,"coa":"sources_insufficient"}',
        2251500000,
        "active",
        URL,
        "Finance remaining Oosterweel build",
        "Raise plafond or capitalise FOI; dual MJR book full draws",
        SRC,
        "strong",
        "Vlaanderen>Lantis>project_bonds",
        "tick728 residual BC2026",
    ),
    (
        "cmt_owv_subloan_snowball_27bn",
        "Sub shareholder loans snowball to 27.0bn eoy2083 capitalized interest",
        "lantis",
        "VL consolidated debt / taxpayers",
        "CoA TV6 BC2026 s4.2 conclusions",
        "2025-12-01",
        2025,
        2083,
        2850000000,
        '{"plafond_m":2850,"extra_fm_m":1650,"rate_pct":5,"drawn_eoy25_m":1128,"last_2026_m":522,"eoy2083_m":27046.4,"cap_interest_m":24338.4,"paid_interest_m":12945.2,"first_interest_pay":"2044-H2","principal_repay_to_2083":0,"coa":"assignment_of_extra_FM_unjustified"}',
        27046400000,
        "active",
        URL,
        "Finance force majeure risks toll-backed",
        "Convert 1.65bn extra sub to capital/toelage now CoA rec",
        SRC,
        "strong",
        "Vlaanderen>Lantis>subloan_snowball",
        "tick728",
    ),
    (
        "cmt_owv_herijk_2035_vl_takeover_2822m",
        "Herijking 2035 VL must take over min 2.82bn sub debt",
        "vlaanderen_gov",
        "VL budget debt path",
        "CoA TV6 own calc on BC2026",
        "2025-12-05",
        2035,
        2035,
        2822300000,
        '{"sub_at_herijk_m":4800.2,"model_bear_m":1977.9,"takeover_m":2822.3,"takeover_pct":58.8,"note":"higher if tolls overstated"}',
        2822300000,
        "active",
        URL,
        "Align debt service with toll capacity",
        "Plan capital injection path FOI; dual GIP",
        SRC,
        "strong",
        "Vlaanderen>Lantis>herijking_2035",
        "tick728",
    ),
    (
        "cmt_owv_mjr_debt_underbook_1680m",
        "VL MJR underbooks Lantis debt draws 1.68bn 2026-30",
        "vlaanderen_gov",
        "Parliament budget honesty",
        "CoA TV6 Table7 vs F&B MJR",
        "2026-03-16",
        2026,
        2030,
        1679770000,
        '{"planned_m":6140.84,"budgeted_m":4461.07,"gap_m":1679.77,"gap_2026_m":703.28,"planned_2026_m":1478.28,"budgeted_2026_m":775}',
        1679770000,
        "active",
        URL,
        "Full multi-year debt transparency",
        "Book full planned draws in MJR FOI",
        SRC,
        "strong",
        "Vlaanderen>FB>Lantis_MJR",
        "tick728",
    ),
    (
        "cmt_owv_capex_spike_2026_28",
        "Oosterweel remaining CAPEX +16.8pct with 2026-28 spikes 52-72pct",
        "lantis",
        "Antwerp mobility users",
        "CoA TV6 Table5 BC2026",
        "2026-03-16",
        2026,
        2033,
        7274640000,
        '{"total_m":7274.64,"vs_bc2025_m":6228.07,"pct":16.8,"2026_m":1220.2,"2027_m":1185.83,"2028_m":1142.04,"fm_pack_m":1811,"contract_adj_m":225,"spent_2025_m":1174}',
        0,
        "active",
        URL,
        "Deliver Oosterweel on schedule",
        "Publish FM cash schedule dual GIP FOI",
        SRC,
        "strong",
        "Vlaanderen>Lantis>capex_path",
        "tick728",
    ),
    (
        "cmt_dual_tv_bc2026_gip_tick728",
        "Dual Oosterweel BC2026 finance residual vs GIP short-horizon",
        "gg_belgium",
        "VL taxpayers dual mobility governance",
        "CoA TV6 residual + prior GIP 2026_27",
        "2026-03-16",
        2026,
        2083,
        27046400000,
        '{"bonds_over_m":2251.5,"mjr_gap_m":1680,"sub_eoy2083_m":27046,"herijk_takeover_m":2822,"note":"not TE-additive dual horizon mismatch"}',
        0,
        "active",
        URL,
        "Honest multi-decade mobility finance map",
        "Reconcile GIP+MJR+BC full FOI",
        SRC_DUAL,
        "strong",
        "Belgium>dual>TV_GIP_finance",
        "tick728",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_owv_bonds_over_plafond_2_25bn",
        "Oosterweel project bonds 7.75bn vs 5.5bn plafond (+2.25bn / +41pct)",
        "Flanders",
        "ops",
        "Vlaanderen>Lantis>bonds_plafond",
        2251500000,
        7751490000,
        "Strong CoA BC2026: sources insufficient; Lantis says no plafond revise this legislature; first 956m Oct2026",
        "strong",
        SRC,
        "VL taxpayers",
        "Finance remaining build",
        "Contracted need exceeds agreed plafond",
        8.5,
        9.0,
        5,
        8.15,
        "Raise plafond or equity now FOI",
        "seed",
        "",
        "tick728",
    ),
    (
        "lb_owv_sub_snowball_27bn_2083",
        "Sub loans snowball to 27.0bn eoy2083 — CoA unjustified FM assignment",
        "Flanders",
        "ops",
        "Vlaanderen>Lantis>sub_snowball",
        27046400000,
        27046400000,
        "Strong CoA: extra 1.65bn @5pct no principal repay; cap interest 24.3bn; convert to capital recommended immediately",
        "strong",
        SRC,
        "Future taxpayers",
        "Toll-backed force majeure finance",
        "Interest snowball policy design fail",
        9.0,
        9.5,
        6,
        8.55,
        "Capitalise 1.65bn now per CoA",
        "seed",
        "",
        "tick728",
    ),
    (
        "lb_owv_herijk_takeover_2_82bn",
        "2035 herijking VL takeover min 2.82bn sub debt (59pct)",
        "Flanders",
        "ops",
        "Vlaanderen>Lantis>herijk_2035",
        2822300000,
        4800200000,
        "Strong CoA calc: of 4.80bn sub at herijk only 1.98bn model-bearable; higher if tolls overstated",
        "strong",
        SRC,
        "VL budget path",
        "Align debt with toll capacity",
        "Deferred state assumption of project debt",
        8.0,
        8.5,
        5,
        7.75,
        "Plan takeover/capital path early FOI",
        "seed",
        "",
        "tick728",
    ),
    (
        "lb_owv_mjr_underbook_1_68bn",
        "VL MJR underbooks Lantis debt draws 1.68bn 2026-30 (703m in 2026)",
        "Flanders",
        "governance",
        "Vlaanderen>FB>Lantis_MJR_gap",
        1679770000,
        0,
        "Strong CoA Table7: planned 6.14bn vs budgeted 4.46bn; 2026 1.48 vs 0.78",
        "strong",
        SRC,
        "Parliament",
        "Honest multi-year debt display",
        "Budget understates known draws",
        8.5,
        8.0,
        3,
        7.95,
        "Book full planned draws in MJR",
        "seed",
        "",
        "tick728",
    ),
    (
        "lb_owv_capex_remain_plus_17pct",
        "Remaining CAPEX 7.27bn +16.8pct with 2026-28 spikes to +72pct",
        "Flanders",
        "ops",
        "Vlaanderen>Lantis>capex_spike",
        7274640000,
        0,
        "Strong CoA Table5: FM residual 1.81bn + contract 225m; despite 1.17bn spent 2025",
        "strong",
        SRC,
        "Project delivery",
        "On-time Oosterweel",
        "Near-term cash pressure",
        7.0,
        8.5,
        5,
        7.25,
        "Lock FM cash calendar dual GIP FOI",
        "seed",
        "",
        "tick728",
    ),
    (
        "lb_owv_interest_paid_24_5bn",
        "Oosterweel interest paid path 24.5bn 2026-2083 (+cap interest 24.3bn off)",
        "Flanders",
        "ops",
        "Vlaanderen>Lantis>interest_mass",
        24495000000,
        48833400000,
        "Strong CoA: paid interest 24.5bn; separate capitalized sub interest 24.3bn; dual lifetime cost",
        "strong",
        SRC,
        "Toll payers taxpayers",
        "Affordable toll finance",
        "Interest mass exceeds many build costs",
        8.0,
        9.0,
        6,
        7.75,
        "Stress-test tolls; capitalise sub early",
        "seed",
        "",
        "tick728",
    ),
    (
        "lb_dual_tv_bc_gip_horizon_fail",
        "Dual Oosterweel multi-decade finance residual vs GIP short horizon",
        "Belgium",
        "ops",
        "Belgium>dual>TV_GIP",
        0,
        0,
        "Strong dual residual: bonds over plafond + MJR gap + sub snowball vs GIP 2025-27 incomplete map; not TE-additive",
        "strong",
        SRC_DUAL,
        "Entity II mobility policy",
        "Comparable long-term infra finance",
        "Horizon mismatch hides contingent debt",
        8.0,
        8.0,
        5,
        7.55,
        "Publish unified multi-decade L5 FOI",
        "seed",
        "",
        "tick728",
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
        "CoA Toekomstverbond 6th financial progress residual BC2026 finance L5 (2026_18)",
        URL,
        "Rekenhof NL chamber 24 Mar 2026",
        "2026-08-02",
        "court_of_audit",
        "Strong tick728 residual: bonds 7751 vs plafond 5500 over 2251; sub 2850 snowball 27046 eoy2083; herijk takeover 2822; MJR gap 1680 2026-30; CAPEX 7275 +16.8pct; FM 1811; interest paid 24495; CoA unjustified extra sub; raw ccrek_2026_18_Toekomstverbond.pdf",
    ),
    (
        SRC_DUAL,
        "Dual Oosterweel BC2026 finance residual vs GIP/MJR short horizon tick728",
        URL,
        "DOGE synthesis CoA TV6 + prior GIP",
        "2026-08-02",
        "synthesis",
        "Strong dual not TE-additive: multi-decade debt snowball vs GIP 3y; tick728",
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
        if row["task_id"] == "rq_719":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick728 TV6 BC2026 residual: bonds over plafond 2.25bn; sub snowball 27bn; "
                "MJR gap 1.68bn; herijk takeover 2.82bn; FOI gap_tv_bc2026_finance_residual_l5 ready"
            )
        rows.append(row)

rows.append({
    "task_id": "rq_720",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "continuous",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "gg_belgium",
    "instructions": (
        "Next residual: PROGRESS@730 next OR TV modal-shift/leefbaarheid residual CoA 2026_18 "
        "OR new CoA/primary PDF OR WAL UAP residual"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": "",
    "notes": "spawned tick728 after rq_719; progress@730 in 2",
})

with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("rq_719=done spawn rq_720")

foi_row = (
    "gap_tv_bc2026_finance_residual_l5",
    "Vlaanderen>Lantis>Toekomstverbond>BC2026_finance_residual_L5",
    "lantis",
    (
        "Project-bond plafond revision path or alternative equity to cover 2.251bn over-plafond; "
        "full bond drawdown cash calendar reconciling Table6 to MJR Table7 (close 1.68bn gap 2026-30); "
        "decision file converting extra 1.65bn sub loan to capital/toelage (CoA rec); "
        "herijking 2035 stress scenarios (toll -10/-20pct) with VL takeover amounts; "
        "PFAS+FM cash schedule behind remaining 1.811bn; land-loan 176.5m interest terms contract"
    ),
    (
        "CoA: BC2026 not robust; bond plafond breach; sub snowball 27bn; MJR underbooks 1.68bn; "
        "material contingent VL debt"
    ),
    "8",
    "Lantis / Departement MOW / Departement FB / Team Openbaarheid",
    "openbaarheid@vlaanderen.be",
    "Havenlaan 88 bus 20 1000 Brussel",
    "docs/doge/foi/drafts/gap_tv_bc2026_finance_residual_l5.md",
    "ready",
    "2026-08-02",
    "",
    "",
    "",
    "",
    "cmt_owv_bonds_over_plafond_2251m|cmt_owv_subloan_snowball_27bn|cmt_owv_mjr_debt_underbook_1680m",
    "lb_owv_bonds_over_plafond_2_25bn|lb_owv_sub_snowball_27bn_2083|lb_owv_mjr_underbook_1_68bn",
    UTC,
    UTC,
    "tick728 CoA TV6 residual; not sent; related gap_tv_oosterweel_finance_l5 + gap_lantis_vastleg remain ready",
)

with open(DATA / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(foi_row)
print("foi +1")

with open(DATA / "loop_state.csv", encoding="utf-8", newline="") as f:
    rows_s = list(csv.reader(f))
header, row = rows_s[0], rows_s[1]
row[3] = UTC
row[4] = "rq_719"
row[5] = "728"
row[7] = (
    "tick728 TV6 BC2026 residual bonds/sub/MJR; next rq_720; progress@730 in 2; rq_116 deferred"
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(header)
    w.writerow(row)
print("loop_state 728 DONE")

# tick724 — DG CoA aju 2026 residual dual Entity II
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]

budgets = [
    ("bud_dg_aju_gross_saldo_worsen_36_7m", "sec_dg", 2026, 36700000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "1.HHA worsens consol brutto saldo 36.7m CoA T1; tick724"),
    ("bud_dg_aju_esvg_worsen_2_6m", "sec_dg", 2026, 2600000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "ESVG financing saldo worsen only 2.6m (loans neutral); tick724"),
    ("bud_dg_aju_fed_dot_minus_4m", "sec_dg", 2026, -4000000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "Federal dotation path -4.0m aju; tick724"),
    ("bud_dg_aju_wal_dot_plus_2_3m", "sec_dg", 2026, 2300000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "WAL region dots +2.3m (CoA: overstated by ~1.0m); tick724"),
    ("bud_dg_aju_own_rec_plus_3m", "sec_dg", 2026, 3000000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "Own rec +3.0m (refunds local dots 1.7 + 5G license share residual); tick724"),
    ("bud_dg_aju_rrf_rev_plus_16_6m", "sec_dg", 2026, 16600000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "RRF receipts +16.6m aju; tick724"),
    ("bud_dg_aju_rrf_exp_plus_21m", "sec_dg", 2026, 21000000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "RRF VE=AE +21.0m aju; tick724"),
    ("bud_dg_aju_fiber_rrf_19_5m", "sec_dg", 2026, 19500000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "RRF fiber underserved areas 19.5m; promoter claim 27 Apr 2026 target met; tick724"),
    ("bud_dg_aju_communes_dot_plus_3_3m", "sec_dg", 2026, 3300000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "Communes/OCMW dots +3.3m after 90/10 key restore retro 2024; tick724"),
    ("bud_dg_aju_personnel_plus_1_8m", "sec_dg", 2026, 1800000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "Personnel +1.8m aju (gov +90k min +767k teachers +908k); CoA lacks calc; tick724"),
    ("bud_dg_aju_infra_ve_plus_19_4m", "sec_dg", 2026, 19400000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "Infrastructure plan VE +19.4m (65 projects 21.3m class); tick724"),
    ("bud_dg_aju_infra_ae_plus_4_2m", "sec_dg", 2026, 4200000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "Infrastructure AE only +4.2m vs VE +19.4; tick724"),
    ("bud_dg_aju_particip_plus_2_8m", "sec_dg", 2026, 2800000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "Financing/participations VE/AE +2.8m to 16.8m (OEWOB capital +4.5); tick724"),
    ("bud_dg_aju_oewob_capital_4_5m", "sec_dg", 2026, 4500000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "OEWOB capital increase 4.5m in participations line; tick724"),
    ("bud_dg_hv_rev_aju_672_6m", "sec_dg", 2026, 672624000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "Hauptverwaltung receipts aju 672.624m (UHH 655.337 path +17.287); tick724"),
    ("bud_dg_hv_ve_aju_728_0m", "sec_dg", 2026, 727996000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "HV VE aju 728.0m (UHH 666.2 path +62m class); tick724"),
    ("bud_dg_hv_ae_aju_750_8m", "sec_dg", 2026, 750842000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "HV AE aju 750.842m (UHH 703.799 path +47.043); tick724"),
    ("bud_dg_hv_esvg_aju_minus_112_4m", "sec_dg", 2026, -112373000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "HV ESVG financing saldo aju -112.373m (UHH -116.713 path +4.340); tick724"),
    ("bud_dg_hv_net_fin_aju_minus_137_9m", "sec_dg", 2026, -137870000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "HV net financing need aju -137.870m; tick724"),
    ("bud_dg_debt_eoy2024_1252m", "sec_dg", 2024, 1252232000, "", "", "outturn", "src_ccrek_dg_aju2026", "strong", "Consol gross debt eoy2024 1252.2m (from 578.1m eoy2020 +117pct); tick724"),
    ("bud_dg_debt_eoy2025_est_1344m", "sec_dg", 2025, 1343959000, "", "", "outturn", "src_ccrek_dg_aju2026", "medium", "Consol debt eoy2025 est 1344.0m preliminary; tick724"),
    ("bud_dg_debt_eoy2026_est_1468m", "sec_dg", 2026, 1467776000, "", "", "projected", "src_ccrek_dg_aju2026", "strong", "Consol debt eoy2026 est 1467.8m (+132pct since eoy2021); tick724"),
    ("bud_dg_fin_need_2026_199_7m", "sec_dg", 2026, 199689000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "Total financing need 2026 199.7m (tilg + deficit + GZ); residual after 100m raised -99.7m; tick724"),
    ("bud_dg_net_deficit_aju_110_5m", "sec_dg", 2026, 110519000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "Net financing deficit aju 110.519m; tick724"),
    ("bud_dg_gz_deficit_aju_13_3m", "sec_dg", 2026, 13298000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "Gemeinschaftszentren net deficit aju 13.298m; tick724"),
    ("bud_dg_interest_aju_41_2m", "sec_dg", 2026, 41244000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "Interest aju 41.244m (2025 33.7; 2024 25.3); tick724"),
    ("bud_dg_implicit_rate_2026_2_81pct", "sec_dg", 2026, 2.81, "", "", "projected", "src_ccrek_dg_aju2026", "strong", "Implicit rate consol debt 2.81pct 2026 (2.50 2025; 2.02 2024); tick724"),
    ("bud_dg_debt_rev_ratio_2026_257pct", "sec_dg", 2026, 257, "", "", "projected", "src_ccrek_dg_aju2026", "strong", "Debt/revenue excl loans 257pct 2026 path 278pct 2029; tick724"),
    ("bud_dg_npe_growth_2026_8_98pct", "sec_dg", 2026, 8.98, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "NPE growth 2026 +8.98pct vs self-cap 5pct (breach ~4pp); tick724"),
    ("bud_dg_npe_cum_2025_29_minus_5_12pct", "sec_dg", 2029, -5.12, "", "", "projected", "src_ccrek_dg_aju2026", "strong", "NPE cumulative 2025-29 -5.12pct (driven by 2025 drop); tick724"),
    ("bud_dg_alt_fin_ivg_corr_175_2m_2024", "sec_dg", 2024, 175200000, "", "", "outturn", "src_ccrek_dg_aju2026", "strong", "IVG alt finance model corr 175.2m 2024 (communes OCMW WPZS multi-year); tick724"),
    ("bud_dg_infra_ve_cut_2030_36_96m", "sec_dg", 2035, 96000000, "", "", "projected", "src_ccrek_dg_aju2026", "strong", "VE new invest cut 96m over 2030-36 (peak 2035 -44m) unsustainable pace; tick724"),
    ("bud_dg_dgg_gz_ae_plus_7_3m", "sec_dg", 2026, 7290000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "Gemeinschaftszentren AE +7.29m invest ViDo/Worriken self-financed debt; tick724"),
    ("bud_dg_dgg_dsl_plus_210k", "sec_dg", 2026, 210000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "DSL Tuavia disability +210k for 3 FTE avert insolvency 2027; tick724"),
    ("bud_dg_dgg_ser_plus_1_0m", "sec_dg", 2026, 1000000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "SER education logistics +1.0m fire/tech/maint after 2025 audit; tick724"),
    ("bud_dg_eoi_brf_7_91m", "sec_dg", 2026, 7908000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "BRF AE aju 7.908m (+10k ecoschecks); dual VRT residual; tick724"),
    ("bud_dg_eoi_iawm_6_97m", "sec_dg", 2026, 6973000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "IAWM VE 6.973m (+110k PR tender); tick724"),
    ("bud_dg_eoi_zkb_12_97m", "sec_dg", 2026, 12972000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "ZKB Kinderbetreuung AE 12.972m; tick724"),
    ("bud_dg_liquidity_note_missed_5m", "sec_dg", 2026, 5000000, "", "", "budgeted", "src_ccrek_dg_aju2026", "strong", "CoA: capital tilgung forecast misses Mar2025 liquidity note due Sep2026 5.0m; tick724"),
    ("bud_dual_dg_entity2_debt_tick724", "gg_belgium", 2026, 1467776000, "", "", "projected", "src_dual_dg_entity2_tick724", "strong", "Dual DG debt 1.47bn vs VL/WAL/FWB residual; not TE-additive; tick724"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_dg_aju2026_path",
        "DG first budget adjustment 2026 residual dual Entity II",
        "sec_dg",
        "German-speaking Community citizens",
        "CoA 2026_23 DG aju AG 27 May 2026",
        "2026-04-09",
        2026,
        2026,
        750842000,
        '{"hv_ae_m":750.8,"hv_ve_m":728.0,"hv_rev_m":672.6,"esvg_m":-112.4,"gross_worsen_m":36.7,"esvg_worsen_m":2.6,"rrf_exp_m":21,"infra_ve_m":19.4}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_23_DG_Haushalt_AJU.pdf",
        "Entity II small-community budget discipline",
        "Align macro params with FPB; publish NPE fix FOI",
        "src_ccrek_dg_aju2026",
        "strong",
        "DG>budget>aju2026",
        "tick724",
    ),
    (
        "cmt_dg_debt_snowball_2026",
        "DG consol debt path 1.25bn to 1.47bn dual residual",
        "sec_dg",
        "DG taxpayers",
        "CoA 2026_23 ch.3",
        "2020-12-31",
        2020,
        2029,
        1467776000,
        '{"2020_m":578.1,"2024_m":1252.2,"2025_m":1344.0,"2026_m":1467.8,"2029_m":1699.9,"implicit_2026_pct":2.81,"debt_rev_2026_pct":257,"fin_need_2026_m":199.7}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_23_DG_Haushalt_AJU.pdf",
        "Control debt growth",
        "Publish multi-year debt in simulation FOI",
        "src_ccrek_dg_aju2026",
        "strong",
        "DG>debt",
        "tick724",
    ),
    (
        "cmt_dg_npe_breach_2026",
        "DG NPE growth 8.98pct breaches 5pct self-cap dual residual",
        "sec_dg",
        "EU fiscal surveillance Entity II",
        "CoA 2026_23 T4 NPE",
        "2026-01-01",
        2025,
        2029,
        0,
        '{"npe_2026_pct":8.98,"self_cap_pct":5,"cum_2025_29_pct":-5.12,"macro_growth_dg_2026":0.2,"fpb_growth":1.1,"dg_infl_2026":3.2,"fpb_infl":1.9}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_23_DG_Haushalt_AJU.pdf",
        "Meet net primary expenditure path",
        "Correct 2026 NPE FOI",
        "src_ccrek_dg_aju2026",
        "strong",
        "DG>NPE",
        "tick724",
    ),
    (
        "cmt_dg_infra_plan_shift_19_4m",
        "DG infra plan VE +19.4m AE +4.2m dual residual",
        "sec_dg",
        "Schools health ViDo Worriken",
        "Infra plan 31 Mar 2026 + CoA s4.3.2",
        "2026-03-31",
        2026,
        2026,
        19400000,
        '{"ve_m":19.4,"ae_m":4.2,"projects_n":65,"volume_m":21.3,"named":"Griesdeck 5.0 Kaleido 2.8 CFA 2.0 StJosef 2.0","long_cut_2030_36_m":96}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_23_DG_Haushalt_AJU.pdf",
        "Sustainable multi-year infrastructure",
        "Named project cash path FOI",
        "src_ccrek_dg_aju2026",
        "strong",
        "DG>infra",
        "tick724",
    ),
    (
        "cmt_dg_gz_self_financed_invest",
        "Gemeinschaftszentren self-financed invest AE +7.3m dual residual",
        "sec_dg",
        "ViDo Worriken community centres",
        "CoA s4.4.4",
        "2026-01-01",
        2026,
        2026,
        7290000,
        '{"ae_plus_m":7.29,"self_finance":true,"no_dotation":true,"debt_impact":true}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_23_DG_Haushalt_AJU.pdf",
        "Community centre infrastructure without central dots",
        "Publish invest plan + debt FOI",
        "src_ccrek_dg_aju2026",
        "strong",
        "DG>GZ",
        "tick724",
    ),
    (
        "cmt_dual_dg_entity2_tick724",
        "Dual DG small Entity II residual vs VL WAL FWB",
        "gg_belgium",
        "Entity II fiscal path",
        "CoA DG aju + prior Entity II dual",
        "2026-01-01",
        2026,
        2029,
        1467776000,
        '{"dg_debt_2026_m":1467.8,"dg_ae_m":750.8,"npe_breach":true,"note":"not TE-additive"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_23_DG_Haushalt_AJU.pdf",
        "Complete Entity II map incl smallest community",
        "Comparable dual FOI",
        "src_dual_dg_entity2_tick724",
        "strong",
        "Belgium>dual>DG",
        "tick724",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_dg_debt_1468m_path",
        "DG consol debt path to 1.47bn 2026 (+132pct 5y)",
        "Belgium",
        "ops",
        "DG>debt>path",
        1467776000,
        1699900000,
        "Strong CoA: 578m 2020 to 1252m 2024 to 1468m 2026; ratio 257pct of non-loan rev; snowball risk",
        "strong",
        "src_ccrek_dg_aju2026",
        "DG taxpayers",
        "Control small-community debt",
        "Debt growth outpaces transfers",
        7.5,
        9.0,
        6,
        7.95,
        "Publish multi-year debt simulation FOI",
        "seed",
        "",
        "tick724",
    ),
    (
        "lb_dg_npe_breach_8_98pct",
        "DG NPE +8.98pct 2026 breaches 5pct self-cap",
        "Belgium",
        "ops",
        "DG>NPE>breach",
        0,
        750842000,
        "Strong CoA: only 2026 exceeds 5pct NPE self-target by ~4pp; EU surveillance relevance",
        "strong",
        "src_ccrek_dg_aju2026",
        "EU fiscal path",
        "Respect net primary expenditure path",
        "Self-imposed cap broken in adjustment year",
        8.0,
        6.5,
        4,
        7.05,
        "Correct NPE and publish fix FOI",
        "seed",
        "",
        "tick724",
    ),
    (
        "lb_dg_macro_param_divergence",
        "DG uses 0.2pct growth 3.2pct inflation vs FPB 1.1/1.9",
        "Belgium",
        "ops",
        "DG>macro>divergence",
        0,
        672624000,
        "Strong CoA: aju parameters diverge from FPB Feb2026; prudence claim but weakens comparability",
        "strong",
        "src_ccrek_dg_aju2026",
        "Parliament control",
        "Honest macro basis for revenue",
        "Opaque parameter choice",
        7.0,
        6.0,
        3,
        6.55,
        "Reconcile to FPB FOI",
        "seed",
        "",
        "tick724",
    ),
    (
        "lb_dg_infra_ve_ae_gap_15_2m",
        "Infra VE +19.4m but AE only +4.2m commitment lag",
        "Belgium",
        "ops",
        "DG>infra>ve_ae_gap",
        15200000,
        19400000,
        "Strong CoA: VE front-loads 19.4m while AE cash only +4.2m; multi-year cut 96m 2030-36",
        "strong",
        "src_ccrek_dg_aju2026",
        "Schools health projects",
        "Executable multi-year infra calendar",
        "Commitment without cash path realism",
        7.0,
        6.5,
        4,
        6.7,
        "Named project cash FOI",
        "seed",
        "",
        "tick724",
    ),
    (
        "lb_dg_gz_self_debt_7_3m",
        "Gemeinschaftszentren self-financed invest +7.3m AE",
        "Belgium",
        "ops",
        "DG>GZ>self_finance",
        7290000,
        13298000,
        "Strong CoA: no dots; full self-finance adds to consol debt; deficit 13.3m",
        "strong",
        "src_ccrek_dg_aju2026",
        "Community centre users",
        "Local infrastructure without central grant",
        "Off-budget-feel debt in consolidation",
        6.5,
        6.0,
        4,
        6.25,
        "Debt transparency FOI",
        "seed",
        "",
        "tick724",
    ),
    (
        "lb_dg_fin_need_200m_2026",
        "DG financing need 199.7m residual after 100m raised",
        "Belgium",
        "ops",
        "DG>financing>need",
        99689000,
        199689000,
        "Strong CoA T7: need 199.7m; raised 100m by 3 May; residual 99.7m; misses 5m liquidity note",
        "strong",
        "src_ccrek_dg_aju2026",
        "Bond markets",
        "Fund deficit and refinancing",
        "Incomplete refinancing inventory",
        7.0,
        7.0,
        5,
        6.8,
        "Full refinancing calendar FOI",
        "seed",
        "",
        "tick724",
    ),
    (
        "lb_dual_dg_entity2_2026",
        "Dual DG residual completes Entity II map",
        "Belgium",
        "ops",
        "Belgium>dual>DG_Entity2",
        1467776000,
        0,
        "Strong dual residual smallest Entity II community; not TE-additive",
        "strong",
        "src_dual_dg_entity2_tick724",
        "Entity II citizens",
        "Full dual Entity II coverage",
        "Often omitted from Belgian waste maps",
        6.5,
        8.0,
        5,
        7.05,
        "Keep DG in dual dashboards",
        "seed",
        "",
        "tick724",
    ),
]

with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in lbs:
        w.writerow(r)
print("leaderboard +", len(lbs))

srcs = [
    (
        "src_ccrek_dg_aju2026",
        "CoA DG first budget adjustment 2026 residual dual Entity II",
        "https://www.ccrek.be/sites/default/files/Docs/2026_23_DG_Haushalt_AJU.pdf",
        "Rechnungshof / Cour des comptes AG 27 May 2026",
        "2026-08-01",
        "audit",
        "Strong primary 28p residual tick724",
    ),
    (
        "src_dual_dg_entity2_tick724",
        "Dual DG residual vs VL WAL FWB Entity II",
        "https://www.ccrek.be/sites/default/files/Docs/2026_23_DG_Haushalt_AJU.pdf",
        "DOGE synthesis CoA dual",
        "2026-08-01",
        "synthesis",
        "Strong dual residual tick724",
    ),
]

with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in srcs:
        w.writerow(r)
print("sources +", len(srcs))

# entity check
ent_text = (DATA / "entities.csv").read_text(encoding="utf-8")
if "sec_dg" not in {row.split(",")[0] for row in ent_text.splitlines() if row}:
    # may exist as sec_dg already from earlier
    pass
with open(DATA / "entities.csv", encoding="utf-8") as f:
    ids = {row[0] for row in csv.reader(f) if row}
if "sec_dg" not in ids:
    with open(DATA / "entities.csv", "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(
            (
                "sec_dg",
                "Deutschsprachige Gemeinschaft",
                "Communaute germanophone",
                "German-speaking Community of Belgium",
                "community",
                "gg_belgium",
                "de",
                "https://www.ostbelgienlive.be",
                "",
                "",
                "Entity II smallest community; CoA aju2026 tick724",
            )
        )
    print("entity sec_dg added")
else:
    print("entity sec_dg exists")

foi = (
    "gap_dg_aju2026_debt_npe_l5",
    "DG>Aju2026>debt_NPE_infra_L5",
    "sec_dg",
    "Multi-year consol debt path 2026-2029 in official simulation; NPE bridge explaining 8.98pct 2026; named cash for 65 infra projects behind VE 19.4m; OEWOB capital terms 4.5m; residual financing after 100m raised; dual unit-cost vs VL/WAL/FWB",
    "DG debt 1.47bn and NPE breach material for Entity II completeness; L5 project cash residual",
    "5",
    "Ministerium der DG / Rechnungshof liaison / Parlament der DG",
    "",
    "",
    "docs/doge/foi/drafts/gap_dg_aju2026_debt_npe_l5.md",
    "ready",
    "2026-08-01",
    "",
    "",
    "",
    "",
    "cmt_dg_debt_snowball_2026",
    "lb_dg_debt_1468m_path",
    "2026-08-01T22:45:00Z",
    "2026-08-01T22:45:00Z",
    "tick724 CoA DG residual; not sent; contacts TBD",
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
        if row and row[0] == "rq_715":
            row[4] = "done"
            row[10] = "2026-08-01T22:45:00Z"
            row[11] = "tick724 DG aju debt 1.47bn NPE 8.98 infra 19.4 dual Entity II; FOI gap_dg_aju2026_debt_npe_l5 ready"
        rows.append(row)
ids = {row[0] for row in rows if row}
if "rq_716" not in ids:
    rows.append(
        [
            "rq_716",
            "Continuous FOI-adjacent public hole-fill batch",
            "continuous",
            "5",
            "open",
            "L5",
            "gg_belgium",
            "Next residual: OTW L5 or internal security dual-use residual or new CoA PDF",
            "",
            "2026-08-01T22:45:00Z",
            "",
            "spawned tick724 after rq_715",
        ]
    )
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerows(rows)
print("research_queue updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T22:45:00Z,rq_715,724,no,tick724 DG aju residual dual Entity II; next rq_716; progress@730 in 6; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")

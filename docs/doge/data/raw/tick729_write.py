# tick729 — TV leefbaarheid + Haventrace + modal shift residual dual GIP (rq_720)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T01:15:00Z"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_18_Toekomstverbond.pdf"

SRC = "src_ccrek_tv6_leef_haven_modal_residual"
SRC_DUAL = "src_dual_tv_leef_modal_gip_tick729"

budgets = [
    # Leefbaarheid envelope residual
    ("bud_tv_leef_task_2018_1250m", "lantis", 2018, 1250000000, "", "", "budgeted", SRC, "strong", "Leefbaarheid fase1 task budget 1250m price Mar2017 (1000 VL ruiter + 250 Antwerp city/port); tick729"),
    ("bud_tv_leef_task_indexed_1594m", "lantis", 2022, 1594200000, "", "", "budgeted", SRC, "strong", "Leefbaarheid task after index 1594.2m price Jan2022; tick729"),
    ("bud_tv_leef_envelope_tol_shift_2462m", "lantis", 2022, 2462300000, "", "", "budgeted", SRC, "strong", "After RO onderbouw 868m to toll model: total leef envelope 2462.3m closed; tick729"),
    ("bud_tv_leef_raming_2026_total_2566m", "lantis", 2026, 2565700000, "", "", "estimated", SRC, "strong", "Table11 total leefbaarheid raming 2565.7m 2026 (+9.7 vs prior); tick729"),
    ("bud_tv_leef_raming_f1f2_excl_onder_1698m", "lantis", 2026, 1697700000, "", "", "estimated", SRC, "strong", "Fasen 1+2 excl RO onderbouw 1697.7m; tick729"),
    ("bud_tv_leef_over_task_103_5m", "lantis", 2026, 103500000, "", "", "estimate", SRC, "strong", "Raming 1697.7 exceeds task 1594.2 by 103.5m; no solution yet CoA; tick729"),
    ("bud_tv_leef_spent_2018_25_212_4m", "lantis", 2025, 212400000, "", "", "outturn", SRC, "strong", "VL spent 212.4m 2018-2025 on leefbaarheid; tick729"),
    ("bud_tv_overkap_ruiter_stock_499_3m", "vlaanderen_gov", 2025, 499300000, "", "", "budgeted", SRC, "strong", "Overkappingsruiter stock path 499.3m class; tick729 recon"),
    ("bud_tv_overkap_ruiter_available_286_9m", "vlaanderen_gov", 2025, 286900000, "", "", "outturn", SRC, "strong", "Ruiter available eoy2025 286.9m of 499.3; tick729"),
    ("bud_tv_overkap_ruiter_feed_55m_yr", "vlaanderen_gov", 2026, 55000000, "", "", "budgeted", SRC, "strong", "Ruiter feed 55m/yr via GIP underuse; ~27y full build; CoA: no underuse so feeds by delaying other GIP; tick729"),
    ("bud_tv_overkap_ruiter_target_remain_1382m", "vlaanderen_gov", 2026, 1381800000, "", "", "budgeted", SRC, "strong", "Streef middelen ruiter+city after spent: 1381.8m; tick729"),
    ("bud_tv_ro_onderbouw_868m_toll", "lantis", 2022, 868000000, "", "", "budgeted", SRC, "strong", "RO onderbouw 700->868m indexed shifted to toll financial model Oct2022; tick729"),
    ("bud_tv_ro_bovenbouw_sub_308m", "lantis", 2026, 308000000, "", "", "estimated", SRC, "strong", "RO bovenbouw subtotal 308m 2026 raming; tick729"),
    ("bud_tv_ro_total_1176m", "lantis", 2026, 1176000000, "", "", "estimated", SRC, "strong", "RO under+over 1176m; tick729"),
    # Named ringparken residual
    ("bud_tv_ringpark_noordkasteel_42_2m", "lantis", 2026, 42200000, "", "", "estimated", SRC, "strong", "Ringpark Noordkasteel raming 42.2m; tick729"),
    ("bud_tv_ringpark_groenendaal_107_7m", "lantis", 2026, 107700000, "", "", "estimated", SRC, "strong", "Ringpark Groenendaal 107.7m incl 22.3m Stadsserre city; tick729"),
    ("bud_tv_ringpark_lobroek_106_2m", "lantis", 2026, 106200000, "", "", "estimated", SRC, "strong", "Ringpark Lobroek 106.2m; tick729"),
    ("bud_tv_ringpark_schijn_51_9m", "lantis", 2026, 51900000, "", "", "estimated", SRC, "strong", "Ringpark Het Schijn 51.9m; tick729"),
    ("bud_tv_ringpark_west_110_5m", "lantis", 2026, 110500000, "", "", "estimated", SRC, "strong", "Ringpark West task 110.5m (2017 price; optim 139.3m 2025); tick729"),
    ("bud_tv_ringpark_west_outturn_147_5m", "lantis", 2026, 147500000, "", "", "outturn", SRC, "strong", "Ringpark West provisional final 147.5m (+8.2 over optim budget); first park summer 2026; tick729"),
    ("bud_tv_ringpark_groene_vesten_75_2m", "lantis", 2026, 75200000, "", "", "estimated", SRC, "strong", "Ringpark Groene Vesten 75.2m; tick729"),
    ("bud_tv_ringpark_zuid_273_8m", "lantis", 2026, 273800000, "", "", "estimated", SRC, "strong", "Ringpark Zuid 273.8m (+45.9 DO meerkosten); tick729"),
    ("bud_tv_scheldeoever_246_2m", "lantis", 2026, 246200000, "", "", "estimated", SRC, "strong", "Scheldeoeververbinding 246.2m price 2026; optim +6m; tick729"),
    ("bud_tv_spaghettiknoop_131_1m", "awv", 2025, 131100000, "", "", "estimated", SRC, "strong", "Spaghettiknoop R1-A112 AWV raming 131.1m (was 115); not in leef Zuid; tick729"),
    ("bud_tv_antwerp_extra_parkbrug_7_2m", "city_antwerpen", 2026, 7200000, "", "", "budgeted", SRC, "strong", "City Antwerp extra 7.2m parkbrug on top of prior +26.9m; tick729"),
    ("bud_tv_antwerp_extra_prior_26_9m", "city_antwerpen", 2026, 26900000, "", "", "budgeted", SRC, "strong", "City prior extra investments 26.9m leef; tick729"),
    ("bud_tv_reserve_leef_fase2_678_4m", "lantis", 2026, 678400000, "", "", "estimated", SRC, "strong", "Reserve leefbaarheid fase2 total 678.4m (Kap Groen Hart 305.7 Schijn 266 etc); tick729"),
    ("bud_tv_optim_target_5_5pct", "lantis", 2022, 5.5, "", "", "budgeted", SRC, "strong", "PCT optim target -5.5 on leef ramingen 2022; incomplete delivery CoA; tick729"),
    # Haventrace residual
    ("bud_tv_tijsmans_raming_1600m", "lantis", 2024, 1600000000, "", "", "estimated", SRC, "strong", "Tweede Tijsmanstunnel raming 1600m price 2024 (was 1200 2019); excl study/PM/ops; tick729"),
    ("bud_tv_tijsmans_study_gip_17m", "lantis", 2027, 17000000, "", "", "budgeted", SRC, "strong", "GIP 2025-27 study costs Tweede Tijsmanstunnel 17m; tick729"),
    ("bud_tv_tijsmans_study_class_31m", "lantis", 2026, 31000000, "", "", "estimated", SRC, "strong", "Table12 studiekosten Tijsmans class 31m; tick729"),
    ("bud_tv_e34_west_raming_614m", "awv", 2025, 614000000, "", "", "estimated", SRC, "strong", "E34-West total raming 614m price 2025 (was 438 2024); tick729"),
    ("bud_tv_e34_west_gip_doorkijk_428m", "awv", 2027, 428000000, "", "", "budgeted", SRC, "strong", "GIP Grote Projecten doorkijk E34-West 428m; update request 614.7m; tick729"),
    ("bud_tv_e34_west_basis_477m", "awv", 2025, 477000000, "", "", "estimated", SRC, "strong", "E34-West basis infra 477m Table12; tick729"),
    ("bud_tv_e34_west_risk_68m", "awv", 2025, 68000000, "", "", "estimated", SRC, "strong", "E34-West risks 68m; tick729"),
    ("bud_tv_e34_west_expro_8m", "awv", 2025, 8000000, "", "", "estimated", SRC, "strong", "E34-West expropriations 8m; tick729"),
    ("bud_tv_e34_west_scope_marge_27m", "awv", 2025, 27000000, "", "", "estimated", SRC, "strong", "E34-West scope change margin 27m; tick729"),
    ("bud_tv_e34_west_study_34m", "awv", 2025, 34000000, "", "", "estimated", SRC, "strong", "E34-West studiekosten 34m; tick729"),
    ("bud_tv_nieuwe_rand_study_spent_10m", "awv", 2025, 10000000, "", "", "outturn", SRC, "strong", "Nieuwe Rand/A102 studies locked 10m to 2025; tick729"),
    ("bud_tv_nieuwe_rand_gip_study_0_3m_yr", "awv", 2026, 300000, "", "", "budgeted", SRC, "strong", "GIP study 0.3m/yr (was raming 3m/yr); not yet Grote Project; tick729"),
    ("bud_tv_nieuwe_rand_study_table_96m", "awv", 2026, 96000000, "", "", "estimated", SRC, "medium", "Table12 studiekosten Nieuwe Rand class 96m indicative; tick729"),
    ("bud_tv_haven_a12_range_low_750m", "awv", 2026, 750000000, "", "", "estimated", SRC, "medium", "Haven A12+Nx range low 750m Table12; tick729"),
    ("bud_tv_haven_a12_range_high_4530m", "awv", 2026, 4530000000, "", "", "estimated", SRC, "medium", "Haven A12+Nx range high 4530m; tick729"),
    ("bud_tv_haven_a102_range_low_1410m", "awv", 2026, 1410000000, "", "", "estimated", SRC, "medium", "A102 range low 1410m; tick729"),
    ("bud_tv_haven_a102_range_high_4460m", "awv", 2026, 4460000000, "", "", "estimated", SRC, "medium", "A102 range high 4460m; tick729"),
    # Modal shift residual
    ("bud_tv_modal_split_antwerp_vr_58_7pct", "vlaanderen_gov", 2024, 58.7, "", "", "outturn", SRC, "strong", "PCT sustainable trips Antwerp VR 58.7 OVG7 2023-24; target 50 already met at baseline; tick729"),
    ("bud_tv_modal_split_city_67_6pct", "city_antwerpen", 2024, 67.6, "", "", "outturn", SRC, "strong", "PCT sustainable city Antwerp 67.6; tick729"),
    ("bud_tv_modal_split_vr_broader_52_1pct", "vlaanderen_gov", 2024, 52.1, "", "", "outturn", SRC, "strong", "PCT broader VR 52.1; tick729"),
    ("bud_gip_modal_antwerp_2025_76_1m", "vlaanderen_gov", 2025, 76100000, "", "", "budgeted", SRC, "strong", "GIP modal Antwerp VR 76.1m 2025 Table13; tick729"),
    ("bud_gip_modal_antwerp_2026_158_9m", "vlaanderen_gov", 2026, 158900000, "", "", "budgeted", SRC, "strong", "GIP modal Antwerp VR 158.9m 2026; tick729"),
    ("bud_gip_modal_antwerp_2027_199_1m", "vlaanderen_gov", 2027, 199100000, "", "", "budgeted", SRC, "strong", "GIP modal Antwerp VR 199.1m 2027; tick729"),
    ("bud_gip_modal_antwerp_beschik_2026_35_7m", "vlaanderen_gov", 2026, 35700000, "", "", "budgeted", SRC, "strong", "Antwerp availability fees 35.7m 2026; tick729"),
    ("bud_gip_modal_antwerp_leef_2026_89m", "vlaanderen_gov", 2026, 89000000, "", "", "budgeted", SRC, "strong", "Antwerp leef in modal GIP mainly Scheldebalkon 89m 2026; tick729"),
    ("bud_gip_modal_antwerp_flank_2026_26m", "lantis", 2026, 26000000, "", "", "budgeted", SRC, "strong", "Flankerende maatregelen Antwerp 26.0m 2026 Table14; tick729"),
    ("bud_gip_modal_antwerp_other_2026_8_3m", "vlaanderen_gov", 2026, 8300000, "", "", "budgeted", SRC, "strong", "Other flow+bike Antwerp 8.3m 2026; tick729"),
    ("bud_gip_modal_other_vr_2026_63_5m", "vlaanderen_gov", 2026, 63500000, "", "", "budgeted", SRC, "strong", "Other VRs together modal 63.5m 2026; tick729"),
    ("bud_gip_modal_vl_fleet_2026_174_7m", "de_lijn", 2026, 174700000, "", "", "budgeted", SRC, "strong", "VL mainly De Lijn fleet greening 174.7m 2026 in modal GIP; tick729"),
    ("bud_gip_modal_total_2025_692m", "vlaanderen_gov", 2025, 692000000, "", "", "budgeted", SRC, "strong", "GIP modal shift programme total 692.0m 2025; tick729"),
    ("bud_gip_modal_total_2026_397_1m", "vlaanderen_gov", 2026, 397100000, "", "", "budgeted", SRC, "strong", "GIP modal total 397.1m 2026; tick729"),
    ("bud_gip_modal_total_2027_436_1m", "vlaanderen_gov", 2027, 436100000, "", "", "budgeted", SRC, "strong", "GIP modal total 436.1m 2027; tick729"),
    ("bud_tv_flank_invest_toelage_2026_13_3m", "lantis", 2026, 13300000, "", "", "budgeted", SRC, "strong", "Lantis invest toelage flank 13.3m 2026 (BO26 6.9); tick729"),
    ("bud_tv_flank_werk_toelage_2026_6m", "lantis", 2026, 6000000, "", "", "budgeted", SRC, "strong", "Lantis werk toelage Modal Shift team 6.0m 2026 (BO26 11.5); tick729"),
    ("bud_tv_flank_vvf_2026_6_7m", "lantis", 2026, 6700000, "", "", "budgeted", SRC, "strong", "Verkeersveiligheidsfonds toelage Lantis 6.7m 2026; DWV same class 5.0; tick729"),
    ("bud_dual_tv_modal_no_task_budget", "gg_belgium", 2026, 0, "", "", "estimate", SRC_DUAL, "strong", "CoA: no overarching task budget modal pillar — unlimited + no finance mode; dual GIP lines not mappable to Routeplan; tick729"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_tv_leef_overrun_103_5m",
        "Leefbaarheid raming 1698m exceeds task 1594m by 103.5m no solution",
        "lantis",
        "Antwerp region liveability users",
        "CoA TV6 ch5 Table11 residual",
        "2026-03-16",
        2018,
        2030,
        2565700000,
        '{"task_indexed_m":1594.2,"raming_f1f2_excl_onder_m":1697.7,"over_m":103.5,"total_raming_m":2565.7,"envelope_tol_shift_m":2462.3,"spent_m":212.4,"ruiter_available_m":286.9,"feed_m_yr":55,"years_full_build":27,"optim_pct":5.5,"coa":"task_budget_will_not_suffice"}',
        103500000,
        "active",
        URL,
        "Liveable ring parks on schedule",
        "Close overrun FOI optim+external finance; put ruiter feed in GIP",
        SRC,
        "strong",
        "Vlaanderen>Toekomstverbond>leefbaarheid",
        "tick729",
    ),
    (
        "cmt_tv_overkap_ruiter_gip_delay_feed",
        "Overkappingsruiter 55m/yr fed by delaying other GIP projects",
        "vlaanderen_gov",
        "MOW GIP portfolio",
        "CoA TV6 s5.4",
        "2021-02-08",
        2026,
        2050,
        0,
        '{"feed_m_yr":55,"source":"GIP_underuse_nominal","actual":"delay_other_GIP","available_eoy25_m":286.9,"coa_rec":"include_ruiter_feed_in_GIP"}',
        0,
        "active",
        URL,
        "Transparent leef finance",
        "Inscribe ruiter feed as GIP line FOI",
        SRC,
        "strong",
        "Vlaanderen>GIP>overkap_ruiter",
        "tick729",
    ),
    (
        "cmt_tv_haventrace_no_task_budget",
        "Haventrace no task budget; Tijsmans 1.6bn E34-West 614m ranges multi-bn",
        "lantis",
        "Antwerp port mobility",
        "CoA TV6 ch6 Tables12 residual",
        "2026-03-16",
        2020,
        2035,
        1600000000,
        '{"tijsmans_m":1600,"tijsmans_study_gip_m":17,"e34_west_m":614,"e34_gip_doorkijk_m":428,"nieuwe_rand_study_spent_m":10,"a102_range_m":"1410-4460","a12_range_m":"750-4530","task_budget":false,"ops_planning":false,"coa":"mid_term_realisation_doubt"}',
        0,
        "active",
        URL,
        "Port ring connectivity",
        "Set task budget after preferred variant FOI",
        SRC,
        "strong",
        "Vlaanderen>Toekomstverbond>Haventrace",
        "tick729",
    ),
    (
        "cmt_tv_modal_split_already_met_no_budget",
        "Modal 50-50 already met (58.7pct) but no task budget or Routeplan cost",
        "vlaanderen_gov",
        "Antwerp VR passengers",
        "CoA TV6 ch7 Tables13-14 residual",
        "2024-06-10",
        2017,
        2030,
        0,
        '{"target_pct":50,"ovg_vr_pct":58.7,"city_pct":67.6,"broader_pct":52.1,"gip_antwerp_2026_m":158.9,"gip_modal_total_2026_m":397.1,"flank_2026_m":26,"task_budget":false,"coa":"reporting_is_merge_without_goals_or_finance"}',
        0,
        "active",
        URL,
        "Further sustainable modal shift",
        "Reset target + Routeplan full cost FOI; map GIP to fiches",
        SRC,
        "strong",
        "Vlaanderen>Toekomstverbond>modal_shift",
        "tick729",
    ),
    (
        "cmt_tv_flank_not_modal_coa",
        "Flankerende 26m Lantis wrongly labelled modal shift CoA",
        "lantis",
        "P+R bike less-hinder",
        "CoA TV6 s7.3 Table14",
        "2026-03-16",
        2025,
        2027,
        26000000,
        '{"2025_m":21.1,"2026_m":26.0,"2027_m":20.9,"invest_m":13.3,"werk_m":6.0,"vvf_m":6.7,"coa":"assign_to_causing_main_projects"}',
        0,
        "active",
        URL,
        "Honest cost attribution",
        "Reallocate flank to main works FOI",
        SRC,
        "strong",
        "Vlaanderen>Lantis>flankerend",
        "tick729",
    ),
    (
        "cmt_dual_tv_leef_modal_gip_tick729",
        "Dual TV leef/modal residual vs GIP short horizon and Oosterweel finance",
        "gg_belgium",
        "VL mobility taxpayers",
        "CoA TV6 residual dual tick728 finance",
        "2026-03-16",
        2026,
        2030,
        2565700000,
        '{"leef_raming_m":2565.7,"leef_over_m":103.5,"haven_tijsmans_m":1600,"modal_gip_2026_m":397.1,"ruiter_feed_m":55,"note":"not TE-additive dual cluster finance opacity"}',
        0,
        "active",
        URL,
        "Integrated Toekomstverbond finance vision",
        "Middellange-termijn project finance FOI CoA rec",
        SRC_DUAL,
        "strong",
        "Belgium>dual>TV_clusters_GIP",
        "tick729",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_tv_leef_overrun_103_5m",
        "Leefbaarheid raming exceeds task budget by 103.5m; ruiter feed too slow",
        "Flanders",
        "ops",
        "Vlaanderen>TV>leefbaarheid_overrun",
        103500000,
        2565700000,
        "Strong CoA: 1698 vs 1594 task; total raming 2566; Ringpark West +8.2; Zuid +45.9 DO; 55m/yr feed ~27y",
        "strong",
        SRC,
        "Antwerp residents",
        "Deliver ring parks on budget",
        "Ambition exceeds closed envelope",
        7.5,
        7.5,
        5,
        7.05,
        "Optimise or raise envelope FOI; GIP ruiter line",
        "seed",
        "",
        "tick729",
    ),
    (
        "lb_tv_ruiter_feeds_by_gip_delay",
        "Overkappingsruiter 55m/yr de facto delays other GIP projects",
        "Flanders",
        "governance",
        "Vlaanderen>GIP>ruiter_opacity",
        55000000,
        0,
        "Strong CoA: no GIP underuse years; feed by postponing other projects; not transparent in GIP",
        "strong",
        SRC,
        "MOW portfolio",
        "Honest GIP prioritisation",
        "Hidden reallocation mechanism",
        8.0,
        6.5,
        4,
        7.15,
        "Book ruiter feed explicitly in GIP",
        "seed",
        "",
        "tick729",
    ),
    (
        "lb_tv_haventrace_1_6bn_no_task",
        "Haventrace Tijsmans 1.6bn + E34 614m without task budget or ops plan",
        "Flanders",
        "ops",
        "Vlaanderen>TV>Haventrace",
        1600000000,
        0,
        "Strong CoA: all still research phase; multi-bn ranges A102 1.4-4.5bn; mid-term realisation doubtful",
        "strong",
        SRC,
        "Port region",
        "Port connectivity",
        "Ambition without finance path",
        7.5,
        8.5,
        6,
        7.35,
        "Task budget after preferred variant FOI",
        "seed",
        "",
        "tick729",
    ),
    (
        "lb_tv_modal_target_already_met",
        "Modal 50-50 already met (58.7pct) — pillar reporting without finance/goals",
        "Flanders",
        "ops",
        "Vlaanderen>TV>modal_shift_empty",
        0,
        397100000,
        "Strong CoA: baseline already met; no new target; no task budget; GIP lines not mappable to Routeplan; flank mislabelled",
        "strong",
        SRC,
        "VR passengers",
        "Further modal shift",
        "KPI success without investment accountability",
        8.0,
        6.0,
        4,
        7.0,
        "Reset target + full Routeplan cost FOI",
        "seed",
        "",
        "tick729",
    ),
    (
        "lb_tv_modal_gip_antwerp_159m_opaque",
        "GIP modal Antwerp 158.9m 2026 not linkable to Routeplan fiches",
        "Flanders",
        "transparency",
        "Vlaanderen>GIP>modal_Antwerp",
        158900000,
        0,
        "Strong CoA Table13: largest VR effort; fiches cannot be mapped; dual De Lijn fleet 174.7 VL-wide",
        "strong",
        SRC,
        "Parliament MOW",
        "Traceable modal investment",
        "Programme opacity",
        7.0,
        7.0,
        4,
        6.7,
        "Split GIP lines to Routeplan actions FOI",
        "seed",
        "",
        "tick729",
    ),
    (
        "lb_tv_ringpark_west_overrun_8_2m",
        "Ringpark West provisional final 147.5m (+8.2 over optim)",
        "Flanders",
        "ops",
        "Vlaanderen>TV>Ringpark_West",
        8200000,
        147500000,
        "Strong CoA: first park summer 2026 delivery; optim fail signal for other parks",
        "strong",
        SRC,
        "Antwerp west",
        "On-budget first ring park",
        "Optimisation target missed",
        6.5,
        5.5,
        3,
        5.95,
        "Lock final account FOI dual other parks",
        "seed",
        "",
        "tick729",
    ),
    (
        "lb_dual_tv_clusters_finance_gap",
        "Dual TV leef/haven/modal residual vs Oosterweel finance fail",
        "Belgium",
        "ops",
        "Belgium>dual>TV_clusters",
        0,
        0,
        "Strong dual residual: leef overrun + haven no task + modal empty target vs Oosterweel non-robust BC; CoA mid-term vision gap endangers TV",
        "strong",
        SRC_DUAL,
        "VL taxpayers",
        "Integrated Toekomstverbond delivery",
        "Four pillars finance incoherence",
        8.5,
        8.0,
        6,
        7.75,
        "Middellange-termijn finance vision FOI",
        "seed",
        "",
        "tick729",
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
        "CoA Toekomstverbond 6 residual leefbaarheid Haventrace modal shift (2026_18 ch5-7)",
        URL,
        "Rekenhof NL chamber 24 Mar 2026",
        "2026-08-02",
        "court_of_audit",
        "Strong tick729: leef raming 2565.7 over task 103.5; ruiter 55/yr GIP delay feed; Ringpark West 147.5; Haventrace Tijsmans 1600 E34 614 no task; modal 58.7 already met no budget; GIP modal Antwerp 158.9 Tables13-14; dual GIP",
    ),
    (
        SRC_DUAL,
        "Dual TV leef/modal/haven residual vs GIP and Oosterweel finance tick729",
        URL,
        "DOGE synthesis CoA TV6 residual dual",
        "2026-08-02",
        "synthesis",
        "Strong dual not TE-additive: cluster finance opacity + Oosterweel non-robust BC; tick729",
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
        if row["task_id"] == "rq_720":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick729 TV6 leef/haven/modal residual: leef over 103.5; ruiter GIP delay; "
                "Tijsmans 1.6bn; modal 58.7 met no budget; FOI gap_tv_leef_modal_haven_l5 ready"
            )
        rows.append(row)

rows.append({
    "task_id": "rq_721",
    "title": "Mandatory progress@730 coverage % + waste top10",
    "sprint": "continuous",
    "priority": "6",
    "status": "open",
    "hierarchy_target": "L0",
    "entity_id": "gg_belgium",
    "instructions": (
        "When ticks_completed hits 730: refresh progress_every_10_ticks.md layers A-E vs EUR 347.956bn TE "
        "and doge_waste_top10_current.md by priority_index; append log; no invent euros; then spawn next hole-fill."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": "",
    "notes": "spawned tick729 after rq_720; progress@730 next",
})

with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("rq_720=done spawn rq_721 PROGRESS@730")

foi_row = (
    "gap_tv_leef_modal_haven_l5",
    "Vlaanderen>Toekomstverbond>leef_modal_haven_L5",
    "lantis",
    (
        "Leefbaarheid: solution for 103.5m task overrun; optim 5.5pct savings realised by park; "
        "multi-year ruiter cash need schedule vs 55m feed; GIP line for ruiter feed; "
        "Haventrace: preferred variant Tijsmans 2026 decision + task budget; E34-West GIP update 614.7; "
        "Nieuwe Rand study path; Modal: Routeplan 2030 full cost estimate; map GIP modal lines to fiches; "
        "new modal target post 58.7pct baseline"
    ),
    (
        "CoA: leef overrun + slow ruiter; haven no task; modal target already met without finance accountability; "
        "endangers Toekomstverbond mid-term"
    ),
    "7",
    "Lantis / Departement MOW / Departement FB / Team Openbaarheid",
    "openbaarheid@vlaanderen.be",
    "Havenlaan 88 bus 20 1000 Brussel",
    "docs/doge/foi/drafts/gap_tv_leef_modal_haven_l5.md",
    "ready",
    "2026-08-02",
    "",
    "",
    "",
    "",
    "cmt_tv_leef_overrun_103_5m|cmt_tv_haventrace_no_task_budget|cmt_tv_modal_split_already_met_no_budget",
    "lb_tv_leef_overrun_103_5m|lb_tv_haventrace_1_6bn_no_task|lb_tv_modal_target_already_met",
    UTC,
    UTC,
    "tick729 CoA TV6 residual clusters; not sent; related gap_tv_bc2026_finance_residual_l5 ready",
)

with open(DATA / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(foi_row)
print("foi +1")

with open(DATA / "loop_state.csv", encoding="utf-8", newline="") as f:
    rows_s = list(csv.reader(f))
header, row = rows_s[0], rows_s[1]
row[3] = UTC
row[4] = "rq_720"
row[5] = "729"
row[7] = (
    "tick729 TV6 leef/haven/modal residual dual GIP; next rq_721 PROGRESS@730; rq_116 deferred"
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(header)
    w.writerow(row)
print("loop_state 729 DONE")

# tick716 — VL GIP large projects residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # docs/doge
DATA = ROOT / "data"

budgets = [
    ("bud_vl_gip_entity_submit_avg_5137m", "vlaanderen_gov", 2025, 5137000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Entity invest submissions 2025-29 avg 5137m/yr vs hist GIP avg 2884m 2020-24 CoA s3.3.1; tick716"),
    ("bud_vl_gip_hist_avg_2884m_2020_24", "vlaanderen_gov", 2024, 2884000000, "", "", "outturn", "src_ccrek_vl_gip_large_projects_2026", "strong", "Historic GIP avg annual 2884m 2020-24 CoA; tick716"),
    ("bud_vl_gip_added_projects_150plus_2025", "vlaanderen_gov", 2025, 150, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "medium", "CoA counted >150 projects added spring 2025 after initial entity input; tick716"),
    ("bud_vl_gip_premetro_kerk_pothoek_70m", "vlaanderen_gov", 2026, 70000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "GIP labels premetro Kerkstraat-Pothoekstraat 70m as large though below decree 100m works threshold; tick716"),
    ("bud_vl_gip_a12_londerzeel_zuid_90m", "vlaanderen_gov", 2026, 90000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "GIP labels A12 Londerzeel Zuid 90m as large below 100m threshold; tick716"),
    ("bud_vl_gip_selection_shift_2025_301m", "vlaanderen_gov", 2025, 301000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Admin first-to-final project shifts 301m 2025 CoA s3.5; tick716"),
    ("bud_vl_gip_selection_shift_2026_347m", "vlaanderen_gov", 2026, 347000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Admin first-to-final project shifts 347m 2026; tick716"),
    ("bud_vl_gip_selection_shift_2027_325m", "vlaanderen_gov", 2027, 325000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Admin first-to-final project shifts 325m 2027; tick716"),
    ("bud_vl_gip_lines_786_2025_27", "vlaanderen_gov", 2025, 786, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "GIP2025-27 786 project lines; 713 all versions 73 new; 30 lines budget change; tick716"),
    ("bud_vl_gip_fietsfonds_up_25m", "vlaanderen_gov", 2026, 25000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Fietsfonds upward revision 15 to 25m during decision process CoA; tick716"),
    ("bud_vl_gip_sint_annatunnel_cut_26_3m", "vlaanderen_gov", 2026, 26300000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Sint-Annatunnel -26.3m over 2025-27 decision phase; tick716"),
    ("bud_vl_gip_onteigening_ask_avg_252m", "vlaanderen_gov", 2026, 252000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Entities asked avg 252m/yr onteigeningen 2025-27 CoA s5.3.1; tick716"),
    ("bud_vl_gip_onteigening_gip2025_104_2m", "vlaanderen_gov", 2025, 104200000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "GIP2025 onteigeningen only 104.2m excl AWV divers buffer; tick716"),
    ("bud_vl_gip_onteigening_hist_avg_150m", "vlaanderen_gov", 2024, 150000000, "", "", "outturn", "src_ccrek_vl_gip_large_projects_2026", "strong", "Onteigeningen charged avg 150m/yr 2020-24; tick716"),
    ("bud_vl_gip_onteigening_charge_2025_80_9m", "vlaanderen_gov", 2025, 80900000, "", "", "outturn", "src_ccrek_vl_gip_large_projects_2026", "strong", "Onteigeningen charged 80.9m 2025 VAK; +6.7m over plan excl buffer; AWV buffer +9.4m; tick716"),
    ("bud_vl_gip_budget_tight_190m_2025", "vlaanderen_gov", 2025, 190000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "medium", "Fall 2025 budget closing challenge ~190m CoA; tick716"),
    ("bud_vl_gip_overkap_feed_55m_yr", "vlaanderen_gov", 2025, 55000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Overkappingsruiter annual feed need 55m; 2025 87.5pct from GIP (2024 67.5 2023 84.9); tick716"),
    ("bud_vl_gip_squeeze_2030_2182m", "vlaanderen_gov", 2030, 2182000000, "", "", "projected", "src_ccrek_vl_gip_large_projects_2026", "strong", "AM + running large + RA large alone 2182m by 2030 ~90pct of 2027 GIP budget CoA Fig5; tick716"),
    ("bud_vl_gip_squeeze_2032_2577m", "vlaanderen_gov", 2032, 2577000000, "", "", "projected", "src_ccrek_vl_gip_large_projects_2026", "strong", "Same stack >2577m by 2032 CoA; tick716"),
    ("bud_vl_gip_beschik_2024_157_9m", "vlaanderen_gov", 2024, 157900000, "", "", "outturn", "src_ccrek_vl_gip_large_projects_2026", "strong", "Availability payments MOW 157.9m 2024 admin estimate; tick716"),
    ("bud_vl_gip_beschik_2030_260_2m", "vlaanderen_gov", 2030, 260200000, "", "", "projected", "src_ccrek_vl_gip_large_projects_2026", "strong", "Availability payments path 260.2m 2030; tick716"),
    ("bud_vl_gip_beschik_2035_970_5m", "vlaanderen_gov", 2035, 970500000, "", "", "projected", "src_ccrek_vl_gip_large_projects_2026", "strong", "Availability payments path 970.5m 2035 crowding-out risk; tick716"),
    ("bud_vl_gip_actu_non_input_68_4m", "vlaanderen_gov", 2026, 68400000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Actualisatie2026 43 projects not in consolidated entity input 68.4m CoA s4.5; tick716"),
    ("bud_vl_gip_actu_new_444_5m", "vlaanderen_gov", 2026, 444500000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Actualisatie2026 new projects 444.5m (300 projects) not in GIP2025-27 for 2026; tick716"),
    ("bud_vl_gip_actu_removed_316_4m", "vlaanderen_gov", 2026, 316400000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Actualisatie2026 removed 83 projects 316.4m from prior GIP2026 plan; tick716"),
    ("bud_vl_gip_actu_oosterweel_extra_857m", "lantis", 2026, 857000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Actualisatie2026 Oosterweel extra 857m VAK; tick716"),
    ("bud_vl_gip_actu_leefbaar_extra_629_8m", "lantis", 2026, 629800000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Actualisatie2026 leefbaarheid extra 629.8m overkap; tick716"),
    ("bud_vl_gip_actu_raise_total_2049m", "vlaanderen_gov", 2026, 2049000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Actualisatie raises selected 2026 GIP amounts total +2049m (incl OW 857 + leef 629.8); tick716"),
    ("bud_vl_gip_actu_lower_total_690m", "vlaanderen_gov", 2026, 690000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Actualisatie lowers other 2026 GIP amounts total ~690m; tick716"),
    ("bud_vl_gip_onteigen_buffer_actu_69m", "vlaanderen_gov", 2026, 69000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Actualisatie2026 onteigeningen buffer 69m vs large-project ask ~115m; tick716"),
    ("bud_vl_gip_onteigen_large_ask_115m", "vlaanderen_gov", 2026, 115000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Large-project onteigeningen ask alone ~115m CoA; tick716"),
    ("bud_vl_gip_recurrent_631m", "vlaanderen_gov", 2026, 631000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Recurrent GIP class ~631m/yr availability FAST traffic lights etc CoA; tick716"),
    ("bud_vl_gip_predraw_q1_2026_900m", "vlaanderen_gov", 2026, 900000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Q1 2026 monthly predraw list >900m before validated GIP CoA; tick716"),
    ("bud_vl_gip_actu_vs_avail_3864_3685", "vlaanderen_gov", 2026, 3685000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Avail sources 3864 vs actu GIP 3685; strip maint/expl ~77 + shift 74 + EU receipts cut; tick716"),
    ("bud_vl_gip_scheldebrug_class_240m", "vlaamse_waterweg", 2026, 240000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Fiets-voetgangersbrug Schelde class ~240m via overkap CoA; tick716"),
    ("bud_vl_gip_lantis_loan_1650m", "lantis", 2025, 1650000000, "", "", "budgeted", "src_ccrek_vl_gip_large_projects_2026", "strong", "Subordinated loan Lantis 1.65bn end-2025; CoA unrepayable wants capital now not 2035; tick716"),
    ("bud_vl_gip_select_vr_high_85pct", "vlaanderen_gov", 2025, 85, "", "", "outturn", "src_ccrek_vl_gip_large_projects_2026", "strong", "~85pct highest vervoerregio score projects selected vs 57pct lowest; tick716"),
    ("bud_vl_gip_select_am_high_77pct", "vlaanderen_gov", 2025, 77, "", "", "outturn", "src_ccrek_vl_gip_large_projects_2026", "strong", "77pct highest AM urgency selected vs 60pct lowest category; tick716"),
    ("bud_vl_gip_ic_fte_3", "vlaanderen_gov", 2025, 3, "", "", "outturn", "src_ccrek_vl_gip_large_projects_2026", "strong", "Investeringscel ~3 FTE (8 staff not full-time) CoA s3.2; tick716"),
    ("bud_dual_gip_large_sofico_2026", "gg_belgium", 2026, 2182000000, "", "", "projected", "src_dual_gip_large_projects_tick716", "strong", "Dual VL large-project squeeze 2182m-2030 vs WAL SOFICO residual; not TE-additive; tick716"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_vl_gip_large_projects_horizon_2040",
        "VL GIP large projects financial look-through to 2040",
        "vlaanderen_gov",
        "MOW large projects RA 2024-2029 + PPS",
        "Decreet Grote Projecten 2019 + RA 2024-2029 + GIP2025-27",
        "2025-07-14",
        2025,
        2040,
        2182000000,
        '{"squeeze_2030_m":2182,"squeeze_2032_m":2577,"beschik_2024":157.9,"beschik_2030":260.2,"beschik_2035":970.5,"horizon":"2040","note":"AM+running+new large only; future PPS unknown and planning residual excluded"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "Deliver RA large projects without crowding-out AM",
        "Publish full financing path + capitalise Lantis loan",
        "src_ccrek_vl_gip_large_projects_2026",
        "strong",
        "Vlaanderen>MOW>Grote_Projecten",
        "tick716 CoA s5.3.2",
    ),
    (
        "cmt_vl_gip_beschik_path_970m",
        "MOW availability payments path to 970.5m 2035",
        "vlaanderen_gov",
        "PPS operators Brabo Livian De Lijn stelplaatsen R4 etc",
        "Admin contribution RA 2024-2029 cited CoA",
        "2024-01-01",
        2024,
        2035,
        970500000,
        '{"2024_m":157.9,"2030_m":260.2,"2035_m":970.5,"examples_ops":"Brabo_I_II Livian1 Stelplaatsen","build":"R4_W_O R0_A201 HOV_Hasselt_Maasmechelen","tender":"NZ_Limburg"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "Pay PPS availability on delivered infra",
        "Cap new PPS until path funded",
        "src_ccrek_vl_gip_large_projects_2026",
        "strong",
        "Vlaanderen>MOW>beschikbaarheidsvergoedingen",
        "tick716",
    ),
    (
        "cmt_vl_gip_actu_churn_2026",
        "GIP actualisatie 2026 project churn dual residual",
        "vlaanderen_gov",
        "MOW entities contractors",
        "Actualisatie GIP 22 May 2026",
        "2026-05-22",
        2026,
        2026,
        444500000,
        '{"new_m":444.5,"new_n":300,"removed_m":316.4,"removed_n":83,"non_input_m":68.4,"non_input_n":43,"raise_m":2049,"lower_m":690,"oosterweel_extra":857,"leefbaar_extra":629.8,"predraw_q1":900,"recurrent":631}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "Stable executable invest calendar",
        "Ban non-input adds; publish score-to-select map",
        "src_ccrek_vl_gip_large_projects_2026",
        "strong",
        "Vlaanderen>GIP>actualisatie_churn",
        "tick716",
    ),
    (
        "cmt_vl_gip_selection_distortion_2025",
        "GIP selection not bound by scores dual residual",
        "vlaanderen_gov",
        "Infrastructure project portfolio",
        "GIP 2025-27 selection process CoA s3.5",
        "2025-07-14",
        2025,
        2027,
        973000000,
        '{"shift_2025":301,"shift_2026":347,"shift_2027":325,"lines":786,"new_lines":73,"vr_high_sel_pct":85,"vr_low_sel_pct":57,"am_high_sel_pct":77,"am_low_sel_pct":60}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "Objective prioritised invest selection",
        "Publish ranking and force score binding",
        "src_ccrek_vl_gip_large_projects_2026",
        "strong",
        "Vlaanderen>GIP>selectie",
        "tick716",
    ),
    (
        "cmt_vl_gip_onteigen_buffer_gap",
        "GIP onteigeningen buffer under-ask dual residual",
        "vlaanderen_gov",
        "Land acquisition for infra projects",
        "GIP 2025-27 + actu2026 CoA",
        "2025-01-01",
        2025,
        2026,
        252000000,
        '{"ask_avg_m":252,"gip2025_m":104.2,"hist_charge_avg":150,"charge_2025":80.9,"actu_buffer":69,"large_ask":115}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "Fund land acquisition honestly",
        "Size buffers to multi-year average + large projects",
        "src_ccrek_vl_gip_large_projects_2026",
        "strong",
        "Vlaanderen>GIP>onteigeningen",
        "tick716",
    ),
    (
        "cmt_dual_gip_large_sofico_tick716",
        "Dual VL GIP large projects vs WAL SOFICO residual",
        "gg_belgium",
        "Entity II transport mega-projects",
        "CoA GIP large + prior SOFICO",
        "2025-01-01",
        2025,
        2035,
        2182000000,
        '{"vl_squeeze_2030_m":2182,"vl_beschik_2035_m":970.5,"wal_sofico_class":"prior","note":"not TE-additive"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "Map dual regional mega-project fiscal space",
        "Comparable L5 financing FOI",
        "src_dual_gip_large_projects_tick716",
        "strong",
        "Belgium>dual>GIP_large",
        "tick716",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_vl_gip_large_squeeze_2182m_2030",
        "GIP large+AM squeeze 2182m by 2030 ~90pct budget",
        "Flanders",
        "ops",
        "Vlaanderen>GIP>large_squeeze_2030",
        2182000000,
        2577000000,
        "Strong CoA Fig5: AM+running+new large alone 2182m 2030 / 2577m 2032 crowding new projects",
        "strong",
        "src_ccrek_vl_gip_large_projects_2026",
        "Infra users Flanders",
        "Fund RA large without gutting AM/bike",
        "Path shows near full GIP absorption by locked claims",
        8.5,
        9.0,
        6,
        8.375,
        "Publish 10y financing envelope before new large start",
        "seed",
        "",
        "tick716",
    ),
    (
        "lb_vl_gip_beschik_970m_2035",
        "Availability payments path to 970.5m 2035",
        "Flanders",
        "ops",
        "Vlaanderen>GIP>beschik_2035",
        970500000,
        970500000,
        "Strong CoA admin est: 157.9 (2024) -> 260.2 (2030) -> 970.5 (2035) PPS lock-in",
        "strong",
        "src_ccrek_vl_gip_large_projects_2026",
        "PPS operators taxpayers",
        "Deliver PPS assets",
        "Long tail availability crowds discretionary invest",
        8.0,
        8.5,
        5,
        8.05,
        "Cap new DBFM until 2030 path funded; dual SOFICO",
        "seed",
        "",
        "tick716",
    ),
    (
        "lb_vl_gip_select_score_not_binding",
        "GIP selection ignores scores high=85 low=57",
        "Flanders",
        "ops",
        "Vlaanderen>GIP>select_distortion",
        973000000,
        0,
        "Strong CoA: VR high 85pct selected vs low 57; AM 77 vs 60; shifts 301/347/325m; 73 new lines",
        "strong",
        "src_ccrek_vl_gip_large_projects_2026",
        "Taxpayers project regions",
        "Objective prioritisation",
        "Political churn after scoring undermines instrument",
        8.5,
        7.5,
        4,
        7.85,
        "Bind selection to published scores; audit exceptions",
        "seed",
        "",
        "tick716",
    ),
    (
        "lb_vl_gip_actu_churn_444_316",
        "GIP actu2026 new 444.5m remove 316.4m churn",
        "Flanders",
        "ops",
        "Vlaanderen>GIP>actu_churn",
        444500000,
        760900000,
        "Strong CoA: 300 new 444.5m; 83 removed 316.4m; 43 non-input 68.4m; predraw Q1 900m",
        "strong",
        "src_ccrek_vl_gip_large_projects_2026",
        "Contractors municipalities",
        "Stable multi-year calendar",
        "One-year GIP + monthly predraws = opposite of stability",
        8.0,
        8.0,
        5,
        7.8,
        "Forbid non-input adds; multi-year lock at BA",
        "seed",
        "",
        "tick716",
    ),
    (
        "lb_vl_gip_onteigen_buffer_under",
        "Onteigen buffer 104 vs ask 252 hist charge 150",
        "Flanders",
        "ops",
        "Vlaanderen>GIP>onteigen_gap",
        147800000,
        252000000,
        "Strong CoA: ask 252 avg; GIP2025 104.2; hist 150; charge 80.9; actu buffer 69 vs large ask 115",
        "strong",
        "src_ccrek_vl_gip_large_projects_2026",
        "Landowners projects",
        "Honest land acquisition funding",
        "Optimistic buffers force late project cuts",
        7.5,
        7.0,
        5,
        7.175,
        "Size buffer to rolling 5y outturn + large pipeline",
        "seed",
        "",
        "tick716",
    ),
    (
        "lb_vl_gip_below_threshold_large_label",
        "GIP labels 70-90m projects as large below decree",
        "Flanders",
        "ops",
        "Vlaanderen>GIP>threshold_label",
        160000000,
        160000000,
        "Strong CoA: premetro 70m A12 Londerzeel 90m labelled large below 100m works threshold confuses decree map",
        "strong",
        "src_ccrek_vl_gip_large_projects_2026",
        "Parliament oversight",
        "Clear large-project inventory",
        "Terminology opacity weakens Grote Projecten control",
        7.0,
        6.0,
        3,
        6.85,
        "Align GIP labels with decree thresholds only",
        "seed",
        "",
        "tick716",
    ),
    (
        "lb_dual_gip_large_sofico_2026",
        "Dual VL large GIP squeeze vs WAL SOFICO",
        "Belgium",
        "ops",
        "Belgium>dual>GIP_large",
        2182000000,
        0,
        "Strong dual residual Entity II mega-projects fiscal space; not TE-additive",
        "strong",
        "src_dual_gip_large_projects_tick716",
        "Entity II citizens",
        "Comparable multi-year mega L5",
        "No single Belgian infrastructure invest map",
        7.5,
        8.5,
        6,
        7.65,
        "Publish dual mega-project financing dashboards",
        "seed",
        "",
        "tick716",
    ),
]

with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in lbs:
        w.writerow(r)
print("leaderboard +", len(lbs))

srcs = [
    (
        "src_ccrek_vl_gip_large_projects_2026",
        "CoA VL GIP 2026_27 large projects selection budget space dual",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "Rekenhof / Cour des comptes",
        "2026-08-01",
        "audit",
        "Strong primary ss3.3.2 3.5 4.2.2 4.5 5.3.2 large projects residual tick716",
    ),
    (
        "src_dual_gip_large_projects_tick716",
        "Dual VL GIP large projects residual vs WAL SOFICO",
        "https://www.ccrek.be/sites/default/files/Docs/2026_27_GIP.pdf",
        "DOGE synthesis CoA dual",
        "2026-08-01",
        "synthesis",
        "Strong dual Entity II mega-project fiscal residual tick716",
    ),
]

with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in srcs:
        w.writerow(r)
print("sources +", len(srcs))

ent_text = (DATA / "entities.csv").read_text(encoding="utf-8")
if "mow_investeringscel" not in ent_text:
    with open(DATA / "entities.csv", "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(
            (
                "mow_investeringscel",
                "Investeringscel Departement MOW",
                "Cellule investissement MOW",
                "MOW Investment Cell GIP penholder",
                "agency",
                "vlaanderen_gov",
                "nl",
                "https://www.vlaanderen.be/mobiliteit-en-openbare-werken",
                "openbaarheid@vlaanderen.be",
                "",
                "GIP 2.0 penholder ~3 FTE; CoA 2026_27; tick716",
            )
        )
    print("entities +1")
else:
    print("entity exists")

foi = (
    "gap_vl_gip_large_projects_2026",
    "Vlaanderen>MOW>GIP_large_projects",
    "vlaanderen_gov",
    "Named large-project table to 2040 with financing form (classic/PPS) and availability path; decree-threshold alignment for premetro 70m A12 90m labels; score-to-select matrix explaining VR 85/57 AM 77/60 and first-to-final shifts 301/347/325m; actualisatie churn list 300 new 444.5m and 83 removed 316.4m plus 43 non-input 68.4m; onteigen buffer methodology; Q1 2026 predraw archive; Lantis 1.65bn capital conversion plan before 2035",
    "Large projects lock future GIP space (2182m by 2030; beschikbaar 970.5m by 2035); selection not score-bound; dual SOFICO residual",
    "5",
    "Departement MOW / Investeringscel / Team Openbaarheid",
    "openbaarheid@vlaanderen.be",
    "Havenlaan 88 bus 20 1000 Brussel",
    "docs/doge/foi/drafts/gap_vl_gip_large_projects_2026.md",
    "ready",
    "2026-08-01",
    "",
    "",
    "",
    "",
    "cmt_vl_gip_large_projects_horizon_2040",
    "lb_vl_gip_large_squeeze_2182m_2030",
    "2026-08-01T20:45:00Z",
    "2026-08-01T20:45:00Z",
    "tick716 CoA GIP large projects residual; not sent",
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
        if row and row[0] == "rq_707":
            row[4] = "done"
            row[10] = "2026-08-01T20:45:00Z"
            row[11] = "tick716 GIP large projects squeeze 2182/2577 beschikbaar 970.5 select distortion dual; FOI gap_vl_gip_large_projects_2026 ready"
        rows.append(row)
rows.append(
    [
        "rq_708",
        "Continuous FOI-adjacent public hole-fill batch",
        "continuous",
        "5",
        "open",
        "L5",
        "gg_belgium",
        "Next residual: WAL residual CoA deepen (prefer) or fed Pillar2/VVPR recheck if new PDF or VL GIP monitoring/eval residual ss6-7",
        "",
        "2026-08-01T20:45:00Z",
        "",
        "spawned tick716 after rq_707",
    ]
)
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerows(rows)
print("research_queue updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T20:45:00Z,rq_707,716,no,tick716 VL GIP large projects residual dual; next rq_708; progress@720 in 4; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")

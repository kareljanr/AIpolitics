# tick721 — VL Kunstendecreet CoA residual L5 dual FWB
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]

budgets = [
    ("bud_vl_kunsten_short_share_2024_11_5pct", "cultuur_cjm_vl", 2024, 11.5, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "Short-term subsidy share 11.5pct 2024 vs 12.5pct legal min of residual after KI/kerntaken CoA; tick721"),
    ("bud_vl_kunsten_short_share_2023_11_7pct", "cultuur_cjm_vl", 2023, 11.7, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "Short-term share 11.7pct 2023 <12.5pct decree min; tick721"),
    ("bud_vl_kunsten_short_share_total_lt8pct", "cultuur_cjm_vl", 2024, 8, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "Short-term share of total arts budget stays under 8pct CoA; tick721"),
    ("bud_vl_kunsten_extra_ws_4_2m_short", "cultuur_cjm_vl", 2023, 4200000, "", "", "budgeted", "src_ccrek_vl_kunsten_residual_2026", "strong", "Of 25.3m extra WS package 4.2m added to short-term via 12.5pct rule CoA; tick721"),
    ("bud_vl_kunsten_neg_advice_apps_66", "cultuur_cjm_vl", 2023, 66, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "66 orgs applying 5/10y WS got negative advice; 9 still subsidised; tick721"),
    ("bud_vl_kunsten_neg9_avg_award_pct_64", "cultuur_cjm_vl", 2023, 64, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "9 neg-advice orgs still subsidised get avg only 64pct of asked amount; tick721"),
    ("bud_vl_kunsten_stable_core_171_2023_27", "cultuur_cjm_vl", 2023, 171, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "Stable core 171 orgs 73.7pct always funded since first award; tick721"),
    ("bud_vl_kunsten_core_since_2006_134", "cultuur_cjm_vl", 2023, 134, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "134 orgs 57.8pct funded since first period 2006-09; tick721"),
    ("bud_vl_kunsten_switchers_10_3pct", "cultuur_cjm_vl", 2023, 10.3, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "Switchers 10.3pct of WS recipients current period; tick721"),
    ("bud_vl_kunsten_fin_vuln_35_of_235", "cultuur_cjm_vl", 2023, 35, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "35 of 235 WS orgs (14.9pct) serious financial vulnerability CoA T10; tick721"),
    ("bud_vl_kunsten_fin_vuln_all5_indicators_10", "cultuur_cjm_vl", 2023, 10, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "10 orgs 4.2pct bad on all 5 financial indicators 2023; tick721"),
    ("bud_vl_kunsten_fin_any_bad_45_1pct", "cultuur_cjm_vl", 2023, 45.1, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "45.1pct WS orgs at least 1 unfavourable financial indicator 2023; tick721"),
    ("bud_vl_kunsten_fin_vuln_under70pct_award_10", "cultuur_cjm_vl", 2023, 10, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "Of 35 financially fragile orgs 10 get <70pct of asked subsidy T11; tick721"),
    ("bud_vl_kunsten_fin_vuln_under90pct_award_25", "cultuur_cjm_vl", 2023, 25, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "25 of 35 fragile orgs get <90pct of asked amount; tick721"),
    ("bud_vl_kunsten_ws5y_avg_award_pct_80", "cultuur_cjm_vl", 2023, 80, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "5y WS orgs receive avg 80pct of asked; tick721"),
    ("bud_vl_kunsten_ws10y_avg_award_pct_87", "cultuur_cjm_vl", 2023, 87, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "10y WS orgs receive avg 87pct of asked; tick721"),
    ("bud_vl_kunsten_ws5y_under70pct_26_8pct", "cultuur_cjm_vl", 2023, 26.8, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "26.8pct of 5y WS awardees get 70pct or less of asked; tick721"),
    ("bud_vl_kunsten_hefboom_work_272k_2024", "cultuur_cjm_vl", 2024, 272000, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "Hefboom working grant 272k + risk guarantee 380k + one-off cofin 1.9m class; tick721"),
    ("bud_vl_kunsten_hefboom_risk_380k", "cultuur_cjm_vl", 2024, 380000, "", "", "budgeted", "src_ccrek_vl_kunsten_residual_2026", "strong", "Hefboom risk guarantee 380k; tick721"),
    ("bud_vl_kunsten_hefboom_cofin_1_9m", "cultuur_cjm_vl", 2024, 1900000, "", "", "budgeted", "src_ccrek_vl_kunsten_residual_2026", "strong", "Hefboom one-off cofinancing 1.9m; tick721"),
    ("bud_vl_kunsten_fair_min_hourly_13_07", "cultuur_cjm_vl", 2023, 13.07, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "juistisjuist absolute min hourly EUR 13.07 music cat D 0y 2023 CoA; tick721"),
    ("bud_vl_kunsten_fair_min_hourly_19_08", "cultuur_cjm_vl", 2023, 19.08, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "Min hourly with 1.46 coeff EUR 19.08 CoA; tick721"),
    ("bud_vl_kunsten_fair_orgs_under_min_17", "cultuur_cjm_vl", 2023, 17, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "17 of 26 sample orgs avg freelancers below min hourly 13.07 without coeff; tick721"),
    ("bud_vl_kunsten_fair_orgs_under_coeff_18", "cultuur_cjm_vl", 2023, 18, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "18 of 26 under min with 1.46 coeff; tick721"),
    ("bud_vl_kunsten_fair_toezicht_false_positive_31_35", "cultuur_cjm_vl", 2023, 31, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "Dept marked 31 of 35 dossiers positive on correct pay while data insufficient CoA; tick721"),
    ("bud_vl_kunsten_fair_employee_fail_3of8", "cultuur_cjm_vl", 2023, 3, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "3 of 8 sample orgs fail employee pay norm; 19 of 152 employees under barema; tick721"),
    ("bud_vl_kunsten_fair_employee_under_19of152", "cultuur_cjm_vl", 2023, 19, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "19 of 152 full-time permanent artists under barema norm in sample; tick721"),
    ("bud_vl_kunsten_barema_music_34447", "cultuur_cjm_vl", 2023, 34447.13, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "juistisjuist barema music A/B 0y EUR 34447.13 2023; tick721"),
    ("bud_vl_kunsten_barema_podium_34908", "cultuur_cjm_vl", 2023, 34908.11, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "juistisjuist barema podium A/B 0y EUR 34908.11 2023; tick721"),
    ("bud_vl_kunsten_survey_response_407_990", "cultuur_cjm_vl", 2024, 407, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "Survey 407 of 990 subsidised artists 41.1pct response; tick721"),
    ("bud_vl_kunsten_ws_also_project_55of225", "cultuur_cjm_vl", 2022, 55, "", "", "outturn", "src_ccrek_vl_kunsten_residual_2026", "strong", "55 of 225 WS orgs also had project grant 2019-22 stepping-stone path; tick721"),
    ("bud_vl_kunsten_landschap_5pct_ws", "cultuur_cjm_vl", 2023, 5, "", "", "budgeted", "src_ccrek_vl_kunsten_residual_2026", "strong", "Landscape commission reserve 5pct of WS budget unmotivated CoA; tick721"),
    ("bud_dual_kunsten_fwb_class_2024", "gg_belgium", 2024, 201941900, "", "", "awarded", "src_dual_kunsten_fwb_tick721", "strong", "Dual VL KD awards 201.9m vs FWB arts vivants residual; not TE-additive; tick721"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_vl_kunsten_short_share_below_12_5",
        "Kunstendecreet short-term share below 12.5pct legal floor dual residual",
        "cultuur_cjm_vl",
        "Artists project grants dynamism",
        "Kunstendecreet + CoA 2026_36 s2.3.2",
        "2023-01-01",
        2023,
        2024,
        14858241,
        '{"short_share_2023":11.7,"short_share_2024":11.5,"legal_min":12.5,"share_of_total_arts_lt":8,"short_ks_2024_m":14.858}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_36_VlaamsKunstenbeleid.pdf",
        "Reserve space for renewal via short-term grants",
        "Restore 12.5pct floor and publish discipline split FOI",
        "src_ccrek_vl_kunsten_residual_2026",
        "strong",
        "Vlaanderen>Cultuur>KD_short_share",
        "tick721",
    ),
    (
        "cmt_vl_kunsten_fin_vuln_35_orgs",
        "35 WS arts orgs serious financial vulnerability 2023 dual residual",
        "cultuur_cjm_vl",
        "Subsidised arts organisations landscape stability",
        "CoA 2026_36 T10-T11 accounts analysis",
        "2023-01-01",
        2023,
        2027,
        0,
        '{"orgs_total":235,"any_bad_pct":45.1,"serious_n":35,"serious_pct":14.9,"all5_bad_n":10,"neg9_risk_pct":22,"under70_award_n":10,"under90_award_n":25}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_36_VlaamsKunstenbeleid.pdf",
        "Stable landscape needs solvent organisations",
        "Publish named risk list + supervision actions FOI",
        "src_ccrek_vl_kunsten_residual_2026",
        "strong",
        "Vlaanderen>Cultuur>fin_vuln",
        "tick721",
    ),
    (
        "cmt_vl_kunsten_fair_pay_oversight_fail",
        "Fair practices pay oversight fail CoA sample dual residual",
        "cultuur_cjm_vl",
        "Artists freelancers employees",
        "CoA 2026_36 s5.1.4 dossier test",
        "2023-01-01",
        2023,
        2024,
        0,
        '{"sample_orgs_freelance":26,"under_min_13_07":17,"under_coeff_19_08":18,"dept_positive_31_of_35":true,"employee_fail_orgs":3,"employees_under":19,"employees_sample":152,"min_hourly":13.07}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_36_VlaamsKunstenbeleid.pdf",
        "Correct artist pay as subsidy condition",
        "Mandatory named pay tables + risk-based audit FOI",
        "src_ccrek_vl_kunsten_residual_2026",
        "strong",
        "Vlaanderen>Cultuur>fair_practices",
        "tick721",
    ),
    (
        "cmt_vl_kunsten_neg9_override_path",
        "Nine neg-advice WS orgs still funded avg 64pct dual residual",
        "cultuur_cjm_vl",
        "Landscape-priority orgs local partners",
        "CoA 2026_36 s3.1.2 + s3.2.3 minister decision 2022",
        "2022-06-24",
        2023,
        2027,
        0,
        '{"neg_advice_total_apps":66,"still_funded":9,"avg_award_pct":64,"functions_fail_5_of_9":true,"fin_risk_pct_among9":22,"extra_budget_m":25.3}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_36_VlaamsKunstenbeleid.pdf",
        "Political landscape fill vs expert ranking",
        "Publish named 9 + cash path FOI (gap_vl_kunsten_neg9_cash)",
        "src_ccrek_vl_kunsten_residual_2026",
        "strong",
        "Vlaanderen>Cultuur>neg9",
        "tick721",
    ),
    (
        "cmt_vl_kunsten_stable_core_lock_in",
        "Arts WS stable core 73.7pct lock-in dual residual",
        "cultuur_cjm_vl",
        "Long-term subsidised arts orgs",
        "CoA 2026_36 Fig14 evolution since 2006",
        "2006-01-01",
        2006,
        2027,
        187083659,
        '{"stable_core_pct":73.7,"stable_core_n":171,"since_2006_pct":57.8,"since_2006_n":134,"switchers_pct":10.3,"ws_total_m":187.084}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_36_VlaamsKunstenbeleid.pdf",
        "Stability of professional landscape",
        "Track entry/exit and 10y path FOI",
        "src_ccrek_vl_kunsten_residual_2026",
        "strong",
        "Vlaanderen>Cultuur>stable_core",
        "tick721",
    ),
    (
        "cmt_dual_kunsten_fwb_tick721",
        "Dual VL Kunstendecreet residual vs FWB arts",
        "gg_belgium",
        "Professional arts dual communities",
        "CoA VL 2026_36 + prior FWB arts residual",
        "2024-01-01",
        2024,
        2024,
        201941900,
        '{"vl_kd_awards_m":201.942,"short_share_fail":true,"fin_vuln_35":true,"fair_pay_oversight_fail":true,"note":"not TE-additive"}',
        0,
        "active",
        "https://www.ccrek.be/sites/default/files/Docs/2026_36_VlaamsKunstenbeleid.pdf",
        "Comparable dual culture subsidy governance",
        "Unit-cost dual matrix FOI",
        "src_dual_kunsten_fwb_tick721",
        "strong",
        "Belgium>dual>arts",
        "tick721",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_vl_kunsten_fair_pay_oversight_fail",
        "Fair practices: 17/26 orgs under min hourly but dept OK",
        "Flanders",
        "ops",
        "Vlaanderen>Cultuur>fair_pay_oversight",
        201941900,
        201941900,
        "Strong CoA: 17 of 26 sample orgs freelancers below EUR 13.07/h; 31/35 dossiers marked OK despite weak data",
        "strong",
        "src_ccrek_vl_kunsten_residual_2026",
        "Artists freelancers",
        "Correct pay as legal subsidy condition",
        "Oversight rubber-stamps while pay under norm",
        8.5,
        7.5,
        4,
        7.85,
        "Named pay tables + risk audit FOI",
        "seed",
        "",
        "tick721",
    ),
    (
        "lb_vl_kunsten_fin_vuln_35_orgs",
        "14.9pct WS arts orgs serious financial vulnerability",
        "Flanders",
        "ops",
        "Vlaanderen>Cultuur>fin_vuln_35",
        187083659,
        187083659,
        "Strong CoA T10: 35 of 235 orgs serious risk; 10 all-5 indicators bad; 25 get <90pct asked",
        "strong",
        "src_ccrek_vl_kunsten_residual_2026",
        "Landscape stability taxpayers",
        "Solvent multi-year arts delivery",
        "Subsidy stability masks insolvency risk",
        7.5,
        7.5,
        5,
        7.25,
        "Publish risk register + recovery plans FOI",
        "seed",
        "",
        "tick721",
    ),
    (
        "lb_vl_kunsten_short_share_below_floor",
        "Short-term arts share 11.5pct under 12.5pct legal floor",
        "Flanders",
        "ops",
        "Vlaanderen>Cultuur>short_share_fail",
        14858241,
        201941900,
        "Strong CoA: 11.5pct 2024 and 11.7pct 2023 <12.5pct of residual; total-arts share <8pct",
        "strong",
        "src_ccrek_vl_kunsten_residual_2026",
        "Emerging artists projects",
        "Renewal budget floor in decree",
        "WS lock-in crowds dynamism instrument",
        7.0,
        6.0,
        3,
        6.55,
        "Enforce 12.5pct and publish cash path",
        "seed",
        "",
        "tick721",
    ),
    (
        "lb_vl_kunsten_neg9_at_64pct",
        "9 neg-advice orgs funded at avg 64pct asked",
        "Flanders",
        "ops",
        "Vlaanderen>Cultuur>neg9_64pct",
        0,
        25300000,
        "Strong CoA: of 66 neg advice 9 still funded avg 64pct; quality fail in 5+ dossiers; prior gap_vl_kunsten_neg9_cash",
        "strong",
        "src_ccrek_vl_kunsten_residual_2026",
        "Local landscape fill",
        "Political override of expert ranking",
        "Landscape care used to fund lower quality",
        8.0,
        5.5,
        4,
        6.7,
        "Name cash path FOI already drafted",
        "seed",
        "",
        "tick721",
    ),
    (
        "lb_vl_kunsten_stable_core_73_7pct",
        "73.7pct WS recipients stable core lock-in since first award",
        "Flanders",
        "ops",
        "Vlaanderen>Cultuur>stable_core",
        187083659,
        187083659,
        "Strong CoA: 171/225 always-funded; 134 since 2006; switchers only 10.3pct",
        "strong",
        "src_ccrek_vl_kunsten_residual_2026",
        "Incumbent arts orgs",
        "Stability of professional field",
        "Low churn limits entry for newcomers",
        6.0,
        7.5,
        5,
        6.55,
        "Track entry-exit and 10y share FOI",
        "seed",
        "",
        "tick721",
    ),
    (
        "lb_vl_kunsten_ws5y_under70_26_8pct",
        "26.8pct of 5y WS get 70pct or less of asked budget",
        "Flanders",
        "ops",
        "Vlaanderen>Cultuur>ws_underfund",
        83786515,
        83786515,
        "Strong CoA: 5y avg award 80pct; 26.8pct at <=70pct; kaasschaaf method residual",
        "strong",
        "src_ccrek_vl_kunsten_residual_2026",
        "Arts orgs staff artists",
        "Living budgets for plans",
        "Cheese-slicer awards without line-item guidance",
        7.0,
        7.0,
        4,
        6.9,
        "Require reasoned award cuts FOI",
        "seed",
        "",
        "tick721",
    ),
    (
        "lb_dual_kunsten_fwb_2024",
        "Dual VL KD residual vs FWB arts governance",
        "Belgium",
        "ops",
        "Belgium>dual>arts_kunsten",
        201941900,
        0,
        "Strong dual residual Entity II culture subsidies; not TE-additive",
        "strong",
        "src_dual_kunsten_fwb_tick721",
        "Entity II artists",
        "Comparable dual culture map",
        "Asymmetric public L5 and oversight",
        6.5,
        7.5,
        5,
        6.55,
        "Dual unit-cost matrix FOI",
        "seed",
        "",
        "tick721",
    ),
]

with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in lbs:
        w.writerow(r)
print("leaderboard +", len(lbs))

srcs = [
    (
        "src_ccrek_vl_kunsten_residual_2026",
        "CoA VL kunstenbeleid 2026_36 residual L5 fair-pay fin-vuln short-share dual",
        "https://www.ccrek.be/sites/default/files/Docs/2026_36_VlaamsKunstenbeleid.pdf",
        "Rekenhof / Cour des comptes NL chamber 30 Jun 2026",
        "2026-08-01",
        "audit",
        "Strong primary residual vs tick489 aggregates; tick721",
    ),
    (
        "src_dual_kunsten_fwb_tick721",
        "Dual VL Kunstendecreet residual vs FWB arts",
        "https://www.ccrek.be/sites/default/files/Docs/2026_36_VlaamsKunstenbeleid.pdf",
        "DOGE synthesis CoA dual",
        "2026-08-01",
        "synthesis",
        "Strong dual culture residual tick721",
    ),
]

with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in srcs:
        w.writerow(r)
print("sources +", len(srcs))

foi = (
    "gap_vl_kunsten_fair_pay_fin_vuln_l5",
    "Vlaanderen>Cultuur>KD_fair_pay_fin_vuln_L5",
    "cultuur_cjm_vl",
    "Named list of 35 financially vulnerable WS orgs with indicators; named 17/26 sample orgs under min hourly with pay tables; short-term share cash path restoring 12.5pct; landscape 5pct use; dual FWB unit-cost residual",
    "CoA shows fair-pay oversight false positives and 14.9pct serious fin risk on 187m WS class; L5 names missing",
    "5",
    "Departement CJM / Team Openbaarheid",
    "openbaarheid@vlaanderen.be",
    "Havenlaan 88 1000 Brussel",
    "docs/doge/foi/drafts/gap_vl_kunsten_fair_pay_fin_vuln_l5.md",
    "ready",
    "2026-08-01",
    "",
    "",
    "",
    "",
    "cmt_vl_kunsten_fair_pay_oversight_fail",
    "lb_vl_kunsten_fair_pay_oversight_fail",
    "2026-08-01T22:00:00Z",
    "2026-08-01T22:00:00Z",
    "tick721 CoA residual; not sent; related gap_vl_kunsten_neg9_cash",
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
        if row and row[0] == "rq_712":
            row[4] = "done"
            row[10] = "2026-08-01T22:00:00Z"
            row[11] = "tick721 kunsten residual fair-pay 17/26 fin-vuln 35 short-share 11.5 dual FWB; FOI gap_vl_kunsten_fair_pay_fin_vuln_l5 ready"
        rows.append(row)
ids = {row[0] for row in rows if row}
if "rq_713" not in ids:
    rows.append(
        [
            "rq_713",
            "Continuous FOI-adjacent public hole-fill batch",
            "continuous",
            "5",
            "open",
            "L5",
            "gg_belgium",
            "Next residual: UAP/OTW L5 or fed VVPR primary recheck or new CoA PDF",
            "",
            "2026-08-01T22:00:00Z",
            "",
            "spawned tick721 after rq_712",
        ]
    )
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerows(rows)
print("research_queue updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T22:00:00Z,rq_712,721,no,tick721 VL kunsten fair-pay fin-vuln residual dual FWB; next rq_713; progress@730 in 9; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")

# tick725 — CoA prisons PPP suivi 2026 residual dual L5 (rq_716)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-01T23:15:00Z"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_24_NouvellesPrisonsSuivi.pdf"

budgets = [
    # VFM Table1 European school NPV kEUR — CoA T1 (strong)
    ("bud_dbfm_vfm_school_npv_dbfm_5_60pct", "regie_gebouwen", 2026, 174040000, "", "", "estimate", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "VFM school DBFM NPV 174.040m at private WACC 5.60pct; tick725"),
    ("bud_dbfm_vfm_school_npv_dbm_5_60pct", "regie_gebouwen", 2026, 193636000, "", "", "estimate", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "VFM school DBM NPV 193.636m at 5.60pct; tick725"),
    ("bud_dbfm_vfm_school_npv_dbfm_4_41pct", "regie_gebouwen", 2026, 212937000, "", "", "estimate", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "VFM school DBFM NPV 212.937m at 4.41pct; tick725"),
    ("bud_dbfm_vfm_school_npv_dbm_4_41pct", "regie_gebouwen", 2026, 215406000, "", "", "estimate", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "VFM school DBM NPV 215.406m at 4.41pct; tick725"),
    ("bud_dbfm_vfm_school_npv_dbfm_3_32pct", "regie_gebouwen", 2026, 254548000, "", "", "estimate", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "VFM school DBFM NPV 254.548m at OLO30 3.32pct; CoA premium +14.7m; tick725"),
    ("bud_dbfm_vfm_school_npv_dbm_3_32pct", "regie_gebouwen", 2026, 239888000, "", "", "estimate", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "VFM school DBM NPV 239.888m at OLO30 3.32pct; tick725"),
    ("bud_dbfm_vfm_school_npv_dbfm_3_00pct", "regie_gebouwen", 2026, 274273000, "", "", "estimate", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "VFM school DBFM NPV 274.273m at 3.00pct; tick725"),
    ("bud_dbfm_vfm_school_npv_dbm_3_00pct", "regie_gebouwen", 2026, 248164000, "", "", "estimate", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "VFM school DBM NPV 248.164m at 3.00pct; tick725"),
    ("bud_dbfm_vfm_school_premium_olo_14_7m", "regie_gebouwen", 2026, 14700000, "", "", "estimate", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "CoA: at OLO30 3.32pct DBFM costs +14.7m vs DBM for European school example; tick725"),
    ("bud_dbfm_vfm_private_wacc_5_60pct", "regie_gebouwen", 2026, 5.60, "", "", "estimate", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "Private partner WACC 5.60pct used in Regie VFM school example; tick725"),
    ("bud_dbfm_vfm_olo30_3_32pct", "regie_gebouwen", 2026, 3.32, "", "", "estimate", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "OLO 30y rate 3.32pct CoA preferred discount for state cost; tick725"),
    # Residual value bias Vresse roof
    ("bud_dbfm_vresse_roof_rv_own_1_0m", "regie_gebouwen", 2026, 1000000, "", "", "estimate", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "Vresse roof residual value own-management scenario 1.0m after 25y CoA footnote; tick725"),
    ("bud_dbfm_vresse_roof_rv_dbfm_6_1m", "regie_gebouwen", 2026, 6100000, "", "", "estimate", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "Vresse roof residual value DBFM scenario 6.1m after 25y without concrete justification CoA; tick725"),
    ("bud_dbfm_vresse_roof_rv_gap_5_1m", "regie_gebouwen", 2026, 5100000, "", "", "estimate", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "Roof residual value wedge 5.1m biases VFM toward DBFM CoA critique; tick725"),
    # Governance thresholds / SLA
    ("bud_dbfm_mod_cm_threshold_q_maint_40k", "regie_gebouwen", 2024, 40000, "", "", "budgeted", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "CM 3 May 2024: ops mods with quarterly maint cost >40k EUR need CM after IF; tick725"),
    ("bud_dbfm_sla_critical_penalty_400", "dg_epi", 2023, 400, "", "", "outturn", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "Critical SLA 10min miss redevance reduction 400 EUR not uniformly applied CoA 2023; tick725"),
    # Staffing counts (not EUR) — store as counts with basis note
    ("bud_dbfm_gpp_etp_2023", "regie_gebouwen", 2023, 6.7, "", "", "outturn", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "Regie GPP cadre 6.7 ETP 2023 mostly architects CoA; tick725 COUNT_ETP"),
    ("bud_dbfm_ppp_dir_cadre_target", "dg_epi", 2023, 7, "", "", "budgeted", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "Justice PPP direction cadre target 7 agents; tick725 COUNT"),
    ("bud_dbfm_ppp_dir_staff_2023", "dg_epi", 2023, 4, "", "", "outturn", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "Justice PPP direction staffed 4 of 7 in 2023; tick725 COUNT"),
    ("bud_dbfm_ppp_dir_staff_2026", "dg_epi", 2026, 6, "", "", "outturn", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "Justice PPP direction staffed 6 of 7 at suivi; lawyer recruit 2026; tick725 COUNT"),
    ("bud_dbfm_facility_mgrs_in_post_2026", "regie_gebouwen", 2026, 2, "", "", "outturn", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "Facility managers in post: FL 2025 + WAL 15Jan2026; BRU still open; tick725 COUNT"),
    # Recs
    ("bud_dbfm_recs_done_9", "regie_gebouwen", 2026, 9, "", "", "outturn", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "CoA 30 recs: 9 fully applied as of 31Jan2026; tick725 COUNT"),
    ("bud_dbfm_recs_ongoing_16", "regie_gebouwen", 2026, 16, "", "", "outturn", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "CoA 30 recs: 16 ongoing; tick725 COUNT"),
    ("bud_dbfm_recs_not_5", "regie_gebouwen", 2026, 5, "", "", "outturn", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "CoA 30 recs: 5 not followed (incl federal PPP law frame rec6; uniform price revision rec30; etc); tick725 COUNT"),
    ("bud_dbfm_ops_prisons_5", "dg_epi", 2026, 5, "", "", "outturn", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "5 DBFM prisons in ops: Marche Beveren Leuze Haren Dendermonde; tick725 COUNT"),
    ("bud_dbfm_project_prisons_4", "dg_epi", 2026, 4, "", "", "budgeted", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "4 project DBFM: Antwerp mid2026 Leopoldsburg2029 Vresse2029 Verviers2031; tick725 COUNT"),
    ("bud_dbfm_cpl_3_dbfmo", "dg_epi", 2026, 3, "", "", "budgeted", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "3 CPL DBFMO planned Paifve Wavre Aalst not in initial 2023 audit; tick725 COUNT"),
    ("bud_dbfm_offbalance_still_2_6bn_class", "dg_epi", 2022, 2600000000, "", "", "commitment", "src_ccrek_prisons_dbfm_suivi_residual_tick725", "strong", "Legal commit 2.6bn eoy2022 still not in general accounts hors-bilan at 2026 suivi; tick725"),
    ("bud_dual_dbfm_vfm_method_tick725", "gg_belgium", 2026, 14700000, "", "", "estimate", "src_dual_dbfm_vfm_tick725", "strong", "Dual residual: federal DBFM VFM school premium 14.7m method flag vs VL PPP decree reportage; not TE-additive; tick725"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_dbfm_vfm_table1_school_residual",
        "Regie VFM European school NPV table residual dual DBFM method",
        "regie_gebouwen",
        "Federal taxpayers European school / prison PPP path",
        "CoA 2026_24 Table1 + Epec method critique",
        "2026-05-27",
        2026,
        2026,
        254548000,
        '{"dbfm_5_60":174040,"dbm_5_60":193636,"dbfm_4_41":212937,"dbm_4_41":215406,"dbfm_3_32":254548,"dbm_3_32":239888,"dbfm_3_00":274273,"dbm_3_00":248164,"premium_olo_m":14.7,"private_wacc_pct":5.60,"olo30_pct":3.32,"coa_prefer_olo":true}',
        0,
        "active",
        URL,
        "Justify private finance vs classic build",
        "Mandate OLO discount + IF validation FOI workbooks",
        "src_ccrek_prisons_dbfm_suivi_residual_tick725",
        "strong",
        "Federal>Regie>DBFM_VFM_method",
        "tick725 residual Table1 full rates",
    ),
    (
        "cmt_dbfm_vresse_residual_value_bias",
        "Vresse roof residual value bias 1.0m own vs 6.1m DBFM",
        "regie_gebouwen",
        "Vresse-sur-Semois future detainees / taxpayers",
        "CoA 2026_24 footnote residual value method",
        "2026-05-27",
        2026,
        2051,
        5100000,
        '{"roof_own_m":1.0,"roof_dbfm_m":6.1,"wedge_m":5.1,"note":"biases VFM toward DBFM without concrete justification"}',
        0,
        "active",
        URL,
        "Honest residual value in VFM",
        "Publish residual-value assumptions FOI",
        "src_ccrek_prisons_dbfm_suivi_residual_tick725",
        "strong",
        "Federal>Regie>DBFM_Vresse_RV",
        "tick725",
    ),
    (
        "cmt_dbfm_cm_mod_threshold_40k",
        "DBFM ops modification CM threshold 40k quarterly maint",
        "regie_gebouwen",
        "Regie + SPF Justice + CM",
        "CM 3 May 2024 procedure + CoA 2026_24 s4.6.2",
        "2024-05-03",
        2024,
        2051,
        40000,
        '{"q_maint_threshold_eur":40000,"requires_if":true,"requires_cm":true,"invest_fixed":"mostly_Regie","maint":"Regie+Justice_indexed","facility":"Justice_only_occupancy"}',
        0,
        "active",
        URL,
        "Control mid-contract cost creep",
        "Publish annual CM mod log FOI",
        "src_ccrek_prisons_dbfm_suivi_residual_tick725",
        "strong",
        "Federal>Justitie_Regie>DBFM_mods",
        "tick725",
    ),
    (
        "cmt_dbfm_staffing_facility_mgrs_2026",
        "DBFM staffing residual GPP + PPP dir + facility managers",
        "regie_gebouwen",
        "Regie GPP + Justice PPP direction",
        "CoA 2026_24 s4.1 HR",
        "2023-06-21",
        2023,
        2026,
        0,
        '{"gpp_2023_etp":6.7,"ppp_dir_2023":4,"ppp_dir_2026":6,"ppp_cadre":7,"facility_fl":"2025","facility_wal":"2026-01-15","facility_bru":"open_2026","collab_agreement":"2026-03-18","cpl_protocol":"planned_2026"}',
        0,
        "active",
        URL,
        "In-house DBFM mastery reduce consultant lock-in",
        "Fill BRU facility manager + finance expert FOI headcount",
        "src_ccrek_prisons_dbfm_suivi_residual_tick725",
        "strong",
        "Federal>Regie_Justice>DBFM_HR",
        "tick725",
    ),
    (
        "cmt_dbfm_iwms_unfunded_2029",
        "IWMS DBFM maintenance system unfunded deferred ~2029",
        "regie_gebouwen",
        "Regie buildings portfolio + DBFM prisons",
        "CoA 2026_24 rec26 + conclusions",
        "2022-01-01",
        2022,
        2029,
        0,
        '{"pilot_planned":2022,"budget_denied":true,"current_system_extend_to":"2026-05","planned_extend_y":3,"dbfm_module_deferred_to":"~2029","blocks_cost_quality_dashboard_rec33":true}',
        0,
        "active",
        URL,
        "Common maintenance cost dashboard all DBFM sites",
        "Fund IWMS + interfaces FOI budget path",
        "src_ccrek_prisons_dbfm_suivi_residual_tick725",
        "strong",
        "Federal>Regie>IWMS_DBFM",
        "tick725",
    ),
    (
        "cmt_dual_dbfm_vfm_vl_ppp_tick725",
        "Dual federal DBFM VFM residual vs Flanders PPP decree",
        "gg_belgium",
        "Parliaments PPP authorities",
        "CoA 2026_24 + VL decree 22 Mar 2019",
        "2019-03-22",
        2019,
        2026,
        14700000,
        '{"school_premium_olo_m":14.7,"fed_ppp_law":false,"vl_ppp_decree":true,"wg_feb2026":true,"collab_agreement_2026_03_18":true,"note":"not TE-additive dual governance"}',
        0,
        "active",
        URL,
        "Comparable PPP transparency all levels",
        "Federal PPP frame dual VL",
        "src_dual_dbfm_vfm_tick725",
        "strong",
        "Belgium>dual>DBFM_VFM",
        "tick725",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_dbfm_vfm_school_premium_14_7m_table",
        "DBFM VFM school premium +14.7m at OLO 3.32pct full Table1",
        "federal",
        "procurement_method",
        "Federal>Regie>DBFM_VFM_Table1",
        14700000,
        254548000,
        "Strong CoA T1: school NPV DBFM 254.5 vs DBM 239.9 at OLO30; private WACC 5.60 flips ranking; residual value games",
        "strong",
        "src_ccrek_prisons_dbfm_suivi_residual_tick725",
        "Taxpayers",
        "Justify PPP vs classic",
        "Discount-rate choice decides VFM outcome",
        7.5,
        6.5,
        5,
        6.95,
        "Mandate public OLO discount + IF validation; publish workbooks FOI",
        "seed",
        "",
        "tick725",
    ),
    (
        "lb_dbfm_vresse_roof_rv_bias_5_1m",
        "Vresse roof residual value bias 5.1m toward DBFM",
        "federal",
        "procurement_method",
        "Federal>Regie>DBFM_Vresse_RV",
        5100000,
        6100000,
        "Strong CoA footnote: roof RV 1.0m own vs 6.1m DBFM without concrete justification; biases VFM",
        "strong",
        "src_ccrek_prisons_dbfm_suivi_residual_tick725",
        "Future Vresse project",
        "Honest asset residual value",
        "Parameter games hide private finance premium",
        7.5,
        5.5,
        4,
        6.55,
        "Publish residual-value matrix FOI",
        "seed",
        "",
        "tick725",
    ),
    (
        "lb_dbfm_cm_mod_40k_threshold",
        "DBFM ops mods >40k quarterly maint need CM",
        "federal",
        "governance",
        "Federal>Justitie_Regie>DBFM_mod_threshold",
        40000,
        0,
        "Strong: CM 3May2024 threshold after IF; redevances invest fixed + maint indexed + facility Justice occupancy",
        "strong",
        "src_ccrek_prisons_dbfm_suivi_residual_tick725",
        "Parliament CM",
        "Control mid-contract cost creep",
        "Partial control still opaque without annual mod log",
        6.0,
        4.0,
        3,
        5.0,
        "Publish annual CM mod euro log FOI",
        "seed",
        "",
        "tick725",
    ),
    (
        "lb_dbfm_iwms_unfunded_2029",
        "IWMS DBFM cost dashboard unfunded deferred ~2029",
        "federal",
        "ops",
        "Federal>Regie>IWMS_DBFM",
        0,
        0,
        "Strong CoA: no budget for IWMS; current BMS extend to May2026 then +3y; DBFM interfaces ~2029; blocks rec33 cost/quality tool",
        "strong",
        "src_ccrek_prisons_dbfm_suivi_residual_tick725",
        "Regie + Justice + detainees",
        "Common maintenance cost/SLA dashboard",
        "Cannot measure TCO without tool",
        7.0,
        5.0,
        4,
        6.15,
        "Fund IWMS FOI budget path",
        "seed",
        "",
        "tick725",
    ),
    (
        "lb_dbfm_facility_mgr_gap_bru",
        "DBFM facility managers partial: BRU still open 2026",
        "federal",
        "ops",
        "Federal>Regie>DBFM_facility_HR",
        0,
        0,
        "Strong CoA: FL 2025 WAL Jan2026 BRU open; GPP was 6.7 ETP; PPP dir 6/7; maintenance mastery depends on 3 managers",
        "strong",
        "src_ccrek_prisons_dbfm_suivi_residual_tick725",
        "Regie operational DG",
        "In-house contract mastery",
        "Consultant dependency residual",
        6.5,
        4.5,
        4,
        5.55,
        "Fill BRU post + finance expert",
        "seed",
        "",
        "tick725",
    ),
    (
        "lb_dbfm_recs_5_not_followed",
        "Prison DBFM CoA 5 recs still not followed of 30",
        "federal",
        "governance",
        "Federal>Justitie>DBFM_recs_gap",
        0,
        0,
        "Strong CoA Jan2026: 9 done 16 ongoing 5 not; includes federal PPP legal frame + uniform price revision + off-balance",
        "strong",
        "src_ccrek_prisons_dbfm_suivi_residual_tick725",
        "Parliament Regie Justice",
        "Full mastery of 25y lock-ins",
        "Partial reform incomplete",
        6.5,
        5.5,
        5,
        5.95,
        "Close 5 open recs dual VL PPP frame",
        "seed",
        "",
        "tick725",
    ),
    (
        "lb_dual_dbfm_vfm_vl_ppp_2026",
        "Dual federal DBFM VFM residual vs VL PPP decree",
        "Belgium",
        "ops",
        "Belgium>dual>DBFM_VFM_VL",
        14700000,
        0,
        "Strong dual residual: federal VFM method incomplete + no PPP law; VL decree 2019 exists; not TE-additive",
        "strong",
        "src_dual_dbfm_vfm_tick725",
        "Multi-level PPP authorities",
        "Comparable PPP transparency",
        "Federal lag vs Flanders reportage",
        6.5,
        6.5,
        5,
        6.35,
        "Adopt federal PPP reportage dual VL",
        "seed",
        "",
        "tick725",
    ),
]

with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in lbs:
        w.writerow(r)
print("leaderboard +", len(lbs))

srcs = [
    (
        "src_ccrek_prisons_dbfm_suivi_residual_tick725",
        "CoA Nouvelles prisons PPP suivi 2026 residual L5 (Table1 VFM HR IWMS)",
        URL,
        "Cour des comptes AG 27 May 2026",
        "2026-08-01",
        "court_of_audit",
        "Strong residual tick725: full VFM T1 rates; Vresse roof 1.0/6.1m; CM 40k; SLA 400; GPP 6.7 ETP; PPP dir 6/7; facility FL/WAL/BRU; IWMS ~2029; recs 9/16/5; dual VL",
    ),
    (
        "src_dual_dbfm_vfm_tick725",
        "Dual federal DBFM VFM residual vs Flanders PPP decree",
        URL,
        "DOGE synthesis CoA + VL decree 2019",
        "2026-08-01",
        "synthesis",
        "Strong dual residual tick725 not TE-additive",
    ),
]

with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in srcs:
        w.writerow(r)
print("sources +", len(srcs))

# FOI new gap VFM workbooks + IWMS budget path
foi = (
    "gap_dbfm_vfm_iwms_l5",
    "Federal>Regie_Justice>DBFM>VFM_IWMS_L5",
    "regie_gebouwen",
    "VFM calculation workbooks (European school + Vresse + any prison DBFM) with discount rates residual-value assumptions risk matrices; IF opinions; annual CM log of ops mods >40k quarterly maint; IWMS budget requests denied amounts and 2026-2029 procurement path; Termonde+Antwerp 25y invest redevance totals still missing from expose",
    "CoA residual method opacity: discount/residual-value parameters decide VFM; IWMS unfunded blocks TCO; Dendermonde/Antwerp 25y still missing",
    "7",
    "Regie der Gebouwen / FOD Justitie / FOD BOSA / Inspection des Finances",
    "",
    "https://www.ibz.be/nl/openbaarheid-van-bestuur",
    "docs/doge/foi/drafts/gap_dbfm_vfm_iwms_l5.md",
    "ready",
    "2026-08-01",
    "",
    "",
    "",
    "",
    "cmt_dbfm_vfm_table1_school_residual|cmt_dbfm_iwms_unfunded_2029|cmt_dbfm_vresse_residual_value_bias",
    "lb_dbfm_vfm_school_premium_14_7m_table|lb_dbfm_iwms_unfunded_2029|lb_dbfm_vresse_roof_rv_bias_5_1m",
    UTC,
    UTC,
    "tick725 CoA residual VFM+IWMS; not sent; dual prior fee FOIs remain ready",
)
with open(DATA / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(foi)
print("foi +1")

# Update notes on related FOIs
foi_path = DATA / "foi_queue.csv"
with open(foi_path, "r", encoding="utf-8", newline="") as f:
    r = csv.reader(f)
    header = next(r)
    rows = [header]
    for row in r:
        if row and row[0] == "gap_dbfm_maint_facility_fees_l5":
            row[-1] = (row[-1] + " | tick725 CoA confirms maint/facility still omitted expose; IWMS unfunded; residual FOI ready").strip(" |")
        if row and row[0] == "gap_dbfm_fees_full_table_2026":
            row[-1] = (row[-1] + " | tick725 residual VFM Table1+Dendermonde/Antwerp 25y still FOI; split to gap_dbfm_vfm_iwms_l5").strip(" |")
        rows.append(row)
with open(foi_path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerows(rows)
print("foi notes updated")

# research queue
rq_path = DATA / "research_queue.csv"
with open(rq_path, "r", encoding="utf-8", newline="") as f:
    r = csv.reader(f)
    header = next(r)
    rows = [header]
    for row in r:
        if row and row[0] == "rq_716":
            row[4] = "done"
            row[10] = UTC
            row[11] = "tick725 CoA 2026_24 residual VFM T1 14.7m Vresse RV 5.1m CM40k IWMS~2029 recs9/16/5 dual; FOI gap_dbfm_vfm_iwms_l5 ready"
        rows.append(row)
ids = {row[0] for row in rows if row}
if "rq_717" not in ids:
    rows.append(
        [
            "rq_717",
            "Continuous FOI-adjacent public hole-fill batch",
            "continuous",
            "5",
            "open",
            "L5",
            "gg_belgium",
            "Next residual: OTW L5 or internal security dual-use residual or new CoA/primary PDF not yet mined",
            "",
            UTC,
            "",
            "spawned tick725 after rq_716",
        ]
    )
    print("spawned rq_717")
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerows(rows)

# loop_state
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(
        [
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ]
    )
    w.writerow(
        [
            "main",
            "continuous",
            "hole_fill",
            UTC,
            "rq_716",
            "725",
            "no",
            "tick725 prisons DBFM VFM residual dual; next rq_717; progress@730 in 5; rq_116 deferred",
        ]
    )
print("loop_state ticks=725")
print("DONE tick725")

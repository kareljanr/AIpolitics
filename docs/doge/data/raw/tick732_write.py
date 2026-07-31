# tick732 — COCOM BI2026 residual dual Iriscare/Samusocial (rq_723)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T02:45:00Z"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_25_BI_2026_COCOM.pdf"

SRC = "src_ccrek_cocom_bi2026_residual"
SRC_DUAL = "src_dual_cocom_iriscare_aviq_tick732"

budgets = [
    # Governance / transparency residual
    ("bud_cocom_csf_growth_rec_2_29pct", "cocom", 2026, 2.29, "", "", "estimate", SRC, "strong", "PCT CSF rec max net primary growth 2.29 2026 / avg 2.73 2025-31; expose omits metric CoA; tick732"),
    ("bud_cocom_multiyear_horizon_gap", "cocom", 2026, 2, "", "", "estimate", SRC, "strong", "COUNT years short: multiyear stops 2029 vs CFP art8 require 6y to 2031; tick732"),
    # Soldes residual recon
    ("bud_cocom_scr_solde_path_plus_17_1m", "cocom", 2026, 17100000, "", "", "budgeted", SRC, "strong", "SCR budget solde -61.6m improves +17.1 vs prov 2025; rec +102.3 dep +85.2; tick732"),
    ("bud_cocom_sousutil_2026_64_7m", "cocom", 2026, 64700000, "", "", "budgeted", SRC, "strong", "Sous-util assumption 64.7m (vs 62.8 2025); props SEC -35.0; tick732 residual"),
    ("bud_cocom_sec_after_sousutil_minus_35m", "cocom", 2026, -35000000, "", "", "budgeted", SRC, "strong", "SEC financing solde -35.0m after sous-util 64.7; path balance 2029; tick732"),
    # Encours residual
    ("bud_cocom_encours_eoy2025_193_5m", "cocom", 2025, 193500000, "", "", "outturn", SRC, "strong", "Encours engagements eoy2025 193.5m; tick732"),
    ("bud_cocom_encours_path_eoy2026_180_8m", "cocom", 2026, 180800000, "", "", "budgeted", SRC, "strong", "Encours path eoy2026 180.8m (-12.7 if full exec); tick732"),
    ("bud_cocom_encours_health_aide_161m", "cocom", 2025, 161000000, "", "", "outturn", SRC, "strong", "Encours 161.0m = 83.2pct in health/aide invest programmes; tick732"),
    ("bud_cocom_encours_delta_minus_12_7m", "cocom", 2026, -12700000, "", "", "budgeted", SRC, "strong", "Potential encours drop -12.7m from BI2026; tick732"),
    # Recettes residual
    ("bud_cocom_iriscare_refund_rec_48_1m", "cocom", 2026, 48115000, "", "", "budgeted", SRC, "strong", "Iriscare dot refunds rec 48.115m (+8.942/+22.8pct) mainly 2024 invest/fonct settle; tick732"),
    ("bud_cocom_fake_recettes_code0_49_1m", "cocom", 2026, 49100000, "", "", "budgeted", SRC, "strong", "CoA: unfounded recettes code eco 0 total 49.1m (Iriscare 48.1 + Samusocial 0.9 + BrussHelp 0.1); tick732"),
    ("bud_cocom_fake_recettes_iriscare_48_1m", "iriscare", 2026, 48100000, "", "", "budgeted", SRC, "strong", "Iriscare unfounded recettes 48.1m code 0 CoA; tick732"),
    ("bud_cocom_fake_recettes_samu_0_9m", "new_samusocial", 2026, 900000, "", "", "budgeted", SRC, "strong", "New Samusocial unfounded recettes 0.9m code 0; tick732"),
    ("bud_cocom_fake_recettes_brusshelp_0_1m", "bruss_help", 2026, 100000, "", "", "budgeted", SRC, "strong", "BrussHelp unfounded recettes 0.1m code 0; tick732"),
    ("bud_cocom_sprb_path_plus_8m", "cocom", 2026, 8000000, "", "", "budgeted", SRC, "strong", "SPRB financing path +8.0m to 275.7m; tick732"),
    ("bud_cocom_fsas_path_plus_5m", "cocom", 2026, 5000000, "", "", "budgeted", SRC, "strong", "FSAS special social action fund path +5.0m to 39.6m; tick732"),
    ("bud_cocom_lsf_decompte_under_4_8m", "cocom", 2026, -4800000, "", "", "estimate", SRC, "medium", "LSF 2025 decompte underest class ~4.8m on receipts CoA; tick732"),
    # Dep residual
    ("bud_cocom_scr_ce_2026_recon", "cocom", 2026, 2027700000, "", "", "budgeted", SRC, "strong", "SCR eng 2027.7m (-24.4/-1.2pct vs prov 2025); tick732"),
    ("bud_cocom_scr_cl_2026_recon", "cocom", 2026, 2040500000, "", "", "budgeted", SRC, "strong", "SCR liq 2040.5m (+85.2/+4.4pct); tick732"),
    ("bud_cocom_sante_invest_priv_eng_8_9m", "cocom", 2026, 8900000, "", "", "budgeted", SRC, "strong", "Private health institution invest eng 8.9m (was 70.5; new law 2025); tick732"),
    ("bud_cocom_sante_invest_priv_path_minus_61_6m", "cocom", 2026, -61600000, "", "", "budgeted", SRC, "strong", "Private health invest eng path -61.6m (70.5-8.9); tick732"),
    ("bud_cocom_hospital_prefin_liq_70_7m", "cocom", 2026, 70700000, "", "", "budgeted", SRC, "strong", "Hospital LSF art47/9 prefin liq 70.7m; tick732"),
    ("bud_cocom_m03_eng_path_minus_54_8m", "cocom", 2026, -54800000, "", "", "budgeted", SRC, "strong", "Mission03 Sante eng path -54.8m (invest shift); tick732"),
    ("bud_cocom_m03_cl_path_plus_53_6m", "cocom", 2026, 53600000, "", "", "budgeted", SRC, "strong", "Mission03 Sante CL path +53.6m; tick732"),
    ("bud_cocom_m04_eng_path_plus_11_5m", "cocom", 2026, 11500000, "", "", "budgeted", SRC, "strong", "Mission04 Aide eng path +11.5m to 141.1 class; tick732"),
    ("bud_cocom_m04_cl_path_plus_14_3m", "cocom", 2026, 14300000, "", "", "budgeted", SRC, "strong", "Mission04 Aide CL path +14.3m to 145.4; tick732"),
    ("bud_cocom_provision_sansabri_2_5m", "cocom", 2026, 2500000, "", "", "budgeted", SRC, "strong", "Provision accueil sans-abri 2.5m eng=liq unallocated CoA; tick732"),
    ("bud_cocom_provision_crise_2_5m", "cocom", 2026, 2500000, "", "", "budgeted", SRC, "strong", "Provision gestion crise 2.5m again 2026; tick732"),
    ("bud_cocom_admin_linear_save_2_4m", "cocom", 2026, 2400000, "", "", "budgeted", SRC, "strong", "Admin linear economy 2.4m on remun programme; tick732"),
    # Iriscare residual
    ("bud_iriscare_total_path_plus_64_4m", "iriscare", 2026, 64400000, "", "", "budgeted", SRC, "strong", "Iriscare rec/dep path +64.4m/+3.7pct to 1826.4m; tick732"),
    ("bud_iriscare_scr_dots_1725_7m", "iriscare", 2026, 1725700000, "", "", "budgeted", SRC, "strong", "Iriscare funded by SCR dots 1725.7m of 1826.4; tick732"),
    ("bud_iriscare_af_path_minus_4m_class", "iriscare", 2026, -4000000, "", "", "budgeted", SRC, "strong", "AF SCR dot path -4.0m to 1057.8; measures foreign students -6.1 prescription -3.0 progwet -5.0; tick732"),
    ("bud_iriscare_af_foreign_students_cut_6_1m", "iriscare", 2026, -6100000, "", "", "budgeted", SRC, "strong", "AF cut foreign students right -6.1m; tick732"),
    ("bud_iriscare_af_prescription_cut_3m", "iriscare", 2026, -3000000, "", "", "budgeted", SRC, "strong", "AF prescription period cut 3y -3.0m; tick732"),
    ("bud_iriscare_af_progwet_cut_5m", "iriscare", 2026, -5000000, "", "", "budgeted", SRC, "strong", "AF federal progwet impact -5.0m; tick732"),
    ("bud_iriscare_mr_forfaits_path_plus_5_2m", "iriscare", 2026, 5200000, "", "", "budgeted", SRC, "strong", "MR forfaits path +5.2m to 353.7m; 11600 beds +65 CSJ; tick732"),
    ("bud_iriscare_aapa_path_minus_3_6m", "iriscare", 2026, -3600000, "", "", "budgeted", SRC, "strong", "AAPA path -3.6m to 37.6m; tick732"),
    ("bud_iriscare_infra_takeover_50m_2024_28", "iriscare", 2024, 50000000, "", "", "budgeted", SRC, "strong", "Infra invest dossiers takeover from SCR 50m 2024-28; tick732"),
    ("bud_iriscare_infra_calls_10m_2026", "iriscare", 2026, 10000000, "", "", "budgeted", SRC, "strong", "New infra project calls 10m/yr (+8 vs 2025); tick732"),
    ("bud_iriscare_sante_dot_path_plus_20_5m", "iriscare", 2026, 20500000, "", "", "budgeted", SRC, "strong", "SCR Sante dot to Iriscare path +20.5m to 469.6; tick732"),
    ("bud_iriscare_2025_extra_cl_22_8m", "iriscare", 2025, 22800000, "", "", "budgeted", SRC, "strong", "Iriscare 2025 extra rec/CL 22.8m + eng 27.2m in figures CoA; tick732"),
    # Samusocial / BrussHelp residual
    ("bud_samusocial_path_plus_72pct_class", "new_samusocial", 2026, 71925000, "", "", "budgeted", SRC, "strong", "New Samusocial 71.925m balanced (+72pct vs 41.8 2025 multi-fund); tick732 recon"),
    ("bud_samusocial_scr_dot_path_plus_1_2m", "new_samusocial", 2026, 1200000, "", "", "budgeted", SRC, "strong", "SCR fonct subvention Samusocial +1.2m to 27.4m; tick732"),
    ("bud_brusshelp_outside_cfp_flag", "bruss_help", 2026, 3324000, "", "", "budgeted", SRC, "strong", "BrussHelp 3.324m <7m CFP threshold; CoA: should be outside budget perimeter; tick732"),
    ("bud_cocom_comptes_gap_flag", "cocom", 2026, 0, "", "", "estimate", SRC, "strong", "COUNT flag: general accounts 2019-24 consol + ASBL Samusocial/BrussHelp never approved/transmitted CoA violation; tick732"),
    # Dual
    ("bud_dual_iriscare_aviq_af_class", "gg_belgium", 2026, 1081400000, "", "", "budgeted", SRC_DUAL, "strong", "Iriscare AF 1081.4m dual AViQ AF ~3.01bn dual Groeipakket; not additive; tick732"),
    ("bud_dual_cocom_cocof_class", "gg_belgium", 2026, 2040467000, "", "", "budgeted", SRC_DUAL, "strong", "COCOM SCR CL 2040.5m dual COCOF decret CL 677.5; tick732"),
    ("bud_dual_samusocial_fedasil_class", "gg_belgium", 2026, 71925000, "", "", "budgeted", SRC_DUAL, "strong", "Samusocial multi-fund dual Fedasil/BCR/COCOM homelessness; tick732"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_cocom_comptes_gap_asbl",
        "COCOM general accounts 2019-24 + Samusocial/BrussHelp never transmitted CoA",
        "cocom",
        "Parliament Cour certification chain",
        "CoA 2026_25 preamble OBCC art96/6 + ord 14Jun2018",
        "2026-05-06",
        2019,
        2026,
        0,
        '{"missing_consol_years":"2019-2024","asbl_never_approved":["New_Samusocial","BrussHelp"],"no_fiches":["Iriscare","BrussHelp","New_Samusocial"],"bru_budget_monitor":"never_integrated","violation":true}',
        0,
        "active",
        URL,
        "Certifiable public accounts",
        "Transmit approved general accounts FOI immediate",
        SRC,
        "strong",
        "Bruxelles>COCOM>comptes_gap",
        "tick732 residual",
    ),
    (
        "cmt_cocom_fake_recettes_49_1m",
        "Unfounded recettes code 0 total 49.1m Iriscare/Samu/BrussHelp",
        "cocom",
        "COCOM budget sincerity",
        "CoA 2026_25 s5 OAA residual",
        "2026-05-06",
        2026,
        2026,
        49100000,
        '{"total_m":49.1,"iriscare_m":48.1,"samusocial_m":0.9,"brusshelp_m":0.1,"code":"0","coa":"sans_fondement_reel"}',
        0,
        "active",
        URL,
        "Honest budget recettes",
        "Remove unfounded recettes FOI",
        SRC,
        "strong",
        "Bruxelles>COCOM>fake_recettes",
        "tick732",
    ),
    (
        "cmt_cocom_sec_sousutil_64_7m",
        "SEC -35m props on sous-util 64.7m dual soft balance",
        "cocom",
        "Entity bicommunautaire",
        "CoA 2026_25 s2.4 residual",
        "2026-05-06",
        2026,
        2029,
        64700000,
        '{"sousutil_m":64.7,"sec_m":-35.0,"path_balance":2029,"measures":"unspecified","csf_2026_pct":2.29,"net_primary":"omitted"}',
        35000000,
        "active",
        URL,
        "SEC path honesty",
        "Publish measures + net primary FOI",
        SRC,
        "strong",
        "Bruxelles>COCOM>SEC_path",
        "tick732",
    ),
    (
        "cmt_cocom_encours_health_83pct",
        "Encours 193.5m of which 83pct health/aide invest residual",
        "cocom",
        "Health and social providers",
        "CoA 2026_25 s4.3 residual",
        "2026-05-06",
        2025,
        2026,
        193500000,
        '{"eoy2025_m":193.5,"path_eoy2026_m":180.8,"delta_m":-12.7,"health_aide_m":161.0,"share_pct":83.2}',
        0,
        "active",
        URL,
        "Clear investment pipeline",
        "Publish encours L5 by project FOI",
        SRC,
        "strong",
        "Bruxelles>COCOM>encours",
        "tick732",
    ),
    (
        "cmt_iriscare_af_measures_cuts",
        "Iriscare AF 1081.4m with cuts foreign students/prescription/progwet",
        "iriscare",
        "Family benefit households Brussels",
        "CoA 2026_25 s5.2 residual dual AViQ/Groeipakket",
        "2026-05-06",
        2026,
        2026,
        1081400000,
        '{"af_m":1081.4,"foreign_students_m":-6.1,"prescription_m":-3.0,"progwet_m":-5.0,"scr_af_dot_m":1057.8,"mr_forfaits_m":353.7,"beds":11600}',
        0,
        "active",
        URL,
        "Family benefits delivery",
        "Publish impact KPIs dual AViQ FOI",
        SRC,
        "strong",
        "Bruxelles>Iriscare>AF",
        "tick732",
    ),
    (
        "cmt_dual_cocom_iriscare_aviq_tick732",
        "Dual COCOM/Iriscare residual vs COCOF and AViQ AF mega",
        "gg_belgium",
        "Brussels bicommunal + WAL/VL social stack",
        "CoA COCOM 2026_25 + prior COCOF/AViQ",
        "2026-05-06",
        2026,
        2026,
        2040467000,
        '{"cocom_cl_m":2040.5,"iriscare_m":1826.4,"cocof_cl_m":677.5,"aviq_af_bn":3.01,"iriscare_af_bn":1.08,"fake_rec_m":49.1,"note":"not TE-additive dual"}',
        0,
        "active",
        URL,
        "Comparable community social finance map",
        "Dual unit-cost FOI AF disability homelessness",
        SRC_DUAL,
        "strong",
        "Belgium>dual>COCOM_Iriscare_AViQ",
        "tick732",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_cocom_comptes_gap_asbl",
        "COCOM/ASBL general accounts 2019-24 never approved or transmitted",
        "Brussels",
        "governance",
        "Bruxelles>COCOM>comptes_gap",
        0,
        0,
        "Strong CoA preamble: violation OBCC; no fiches Iriscare/Samusocial/BrussHelp; blocks certification-based budget review",
        "strong",
        SRC,
        "Parliament Cour",
        "Certifiable accounts",
        "Structural transparency failure",
        9.0,
        5.0,
        3,
        7.1,
        "Transmit approved accounts FOI now",
        "seed",
        "",
        "tick732",
    ),
    (
        "lb_cocom_fake_recettes_49_1m",
        "Unfounded recettes code 0 49.1m inflate OAA budgets",
        "Brussels",
        "ops",
        "Bruxelles>COCOM>fake_recettes",
        49100000,
        0,
        "Strong CoA: Iriscare 48.1 + Samu 0.9 + BrussHelp 0.1 without real basis",
        "strong",
        SRC,
        "Taxpayers",
        "Honest recettes",
        "Budget padding via code 0",
        8.5,
        6.5,
        2,
        7.4,
        "Strike unfounded recettes FOI",
        "seed",
        "",
        "tick732",
    ),
    (
        "lb_cocom_sec_soft_35m_sousutil",
        "SEC -35m depends on 64.7m sous-util assumption",
        "Brussels",
        "governance",
        "Bruxelles>COCOM>SEC_soft",
        35000000,
        0,
        "Strong CoA: path to balance 2029 without measures; CSF net primary omitted",
        "strong",
        SRC,
        "Assembly",
        "Honest SEC path",
        "Soft balance technique dual COCOF",
        7.5,
        6.5,
        3,
        6.7,
        "Publish measures + net primary FOI",
        "seed",
        "",
        "tick732",
    ),
    (
        "lb_cocom_brusshelp_perimeter_flag",
        "BrussHelp 3.3m should be outside CFP perimeter (<7m rule)",
        "Brussels",
        "governance",
        "Bruxelles>COCOM>BrussHelp_perimeter",
        3324000,
        0,
        "Strong CoA art4 CFP: threshold 7m; wrongly included in budget project",
        "strong",
        SRC,
        "Legal perimeter integrity",
        "Correct perimeter",
        "CFP breach on small OAA",
        7.0,
        4.5,
        2,
        5.95,
        "Exclude or justify FOI",
        "seed",
        "",
        "tick732",
    ),
    (
        "lb_iriscare_af_1081m_dual",
        "Iriscare AF 1.08bn dual AViQ/Groeipakket with policy cuts",
        "Brussels",
        "ops",
        "Bruxelles>Iriscare>AF",
        1081400000,
        0,
        "Strong CoA: foreign students/prescription/progwet cuts; dual regional AF stack",
        "strong",
        SRC,
        "Families Brussels",
        "Family benefits",
        "Core entitlement dual architecture",
        5.5,
        9.0,
        5,
        6.85,
        "Outcome KPI FOI dual regions",
        "seed",
        "",
        "tick732",
    ),
    (
        "lb_cocom_encours_193_5m_health",
        "Encours 193.5m 83pct health/aide invest opaque L5",
        "Brussels",
        "ops",
        "Bruxelles>COCOM>encours",
        193500000,
        0,
        "Strong CoA: potential drop to 180.8; 161m concentrated invest programmes",
        "strong",
        SRC,
        "Providers",
        "Clear invest pipeline",
        "Concentration risk opacity",
        6.5,
        7.5,
        4,
        6.55,
        "Project-level encours FOI",
        "seed",
        "",
        "tick732",
    ),
    (
        "lb_dual_cocom_cocof_tick732",
        "Dual COCOM 2.04bn vs COCOF 0.68bn community stack residual",
        "Belgium",
        "ops",
        "Belgium>dual>COCOM_COCOF",
        2040467000,
        0,
        "Strong dual residual: bicommunal health/AF vs FR community Phare; comptes gap vs COCOF path; not TE-additive",
        "strong",
        SRC_DUAL,
        "Brussels multi-community users",
        "Comparable transparency",
        "Fragmented community finance dual",
        6.5,
        8.5,
        5,
        6.9,
        "Unified dual map FOI",
        "seed",
        "",
        "tick732",
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
        "CoA COCOM budgets BI2026 residual dual Iriscare/Samusocial (2026_25)",
        URL,
        "Cour des comptes AG 6 May 2026",
        "2026-08-02",
        "court_of_audit",
        "Strong tick732 residual: comptes gap 2019-24; fake recettes 49.1m; sous-util 64.7 SEC -35; encours 193.5 83pct health; Iriscare AF cuts; BrussHelp perimeter; Samusocial +72pct; CSF 2.29 omitted; raw cocom_budget_2026_coa.pdf",
    ),
    (
        SRC_DUAL,
        "Dual COCOM/Iriscare residual vs COCOF and AViQ AF tick732",
        URL,
        "DOGE synthesis CoA COCOM + prior COCOF/AViQ",
        "2026-08-02",
        "synthesis",
        "Strong dual not TE-additive: COCOM 2.04bn / Iriscare 1.83bn / AF 1.08 vs COCOF 0.68 / AViQ AF 3.01; tick732",
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
        if row["task_id"] == "rq_723":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick732 COCOM residual dual Iriscare: comptes gap; fake recettes 49.1; "
                "sous-util 64.7 SEC -35; encours 193.5; FOI gap_cocom_bi2026_residual_l5 ready"
            )
        rows.append(row)

rows.append({
    "task_id": "rq_724",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "continuous",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "gg_belgium",
    "instructions": (
        "Next residual: new CoA/primary PDF not yet mined or WAL UAP residual or "
        "Entity II dual residual or VGC residual dual COCOF"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": "",
    "notes": "spawned tick732 after rq_723",
})

with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("rq_723=done spawn rq_724")

foi_row = (
    "gap_cocom_bi2026_residual_l5",
    "Bruxelles>COCOM>BI2026_residual_L5",
    "cocom",
    (
        "Approved general accounts 2019-2024 consolidated SCR+OAA and Samusocial/BrussHelp; "
        "justificative budget fiches Iriscare/Samusocial/BrussHelp; remove or justify code-0 recettes 49.1m; "
        "SEC path measures to balance 2029 + net primary vs CSF 2.29pct; encours L5 161m health/aide; "
        "Iriscare AF measure impact series; dual unit-cost vs AViQ AF and COCOF Phare"
    ),
    (
        "CoA residual: comptes never transmitted (legal breach); unfounded recettes; soft SEC; dual social stack opacity"
    ),
    "8",
    "Collège réuni COCOM / Assemblée réunie / SPRB transparence",
    "transparence@sprb.brussels",
    "SPRB Place Saint-Lazare 2 1035 Bruxelles",
    "docs/doge/foi/drafts/gap_cocom_bi2026_residual_l5.md",
    "ready",
    "2026-08-02",
    "",
    "",
    "",
    "",
    "cmt_cocom_comptes_gap_asbl|cmt_cocom_fake_recettes_49_1m|cmt_cocom_sec_sousutil_64_7m",
    "lb_cocom_comptes_gap_asbl|lb_cocom_fake_recettes_49_1m|lb_cocom_sec_soft_35m_sousutil",
    UTC,
    UTC,
    "tick732 CoA COCOM residual; not sent; dual COCOF FOI remains ready",
)

with open(DATA / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(foi_row)
print("foi +1")

with open(DATA / "loop_state.csv", encoding="utf-8", newline="") as f:
    rows_s = list(csv.reader(f))
header, row = rows_s[0], rows_s[1]
row[3] = UTC
row[4] = "rq_723"
row[5] = "732"
row[7] = (
    "tick732 COCOM residual dual Iriscare; next rq_724; progress@740 in 8; rq_116 deferred"
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(header)
    w.writerow(row)
print("loop_state 732 DONE")

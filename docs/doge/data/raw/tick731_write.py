# tick731 — COCOF BI2026 residual dual VGC/VAPH (rq_722)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T02:15:00Z"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_21_BI2026_COCOF.pdf"

SRC = "src_ccrek_cocof_bi2026_residual"
SRC_DUAL = "src_dual_cocof_vgc_vaph_tick731"

budgets = [
    # Soldes residual
    ("bud_cocof_sec_corr_2026", "cocof", 2026, -22708000, "", "", "budgeted", SRC, "strong", "SEC financing solde corr -22.708m after sous-util 35.758; tick731 residual"),
    ("bud_cocof_snf_2026", "cocof", 2026, -58466000, "", "", "budgeted", SRC, "strong", "Solde net a financer -58.466m before sous-util; tick731"),
    ("bud_cocof_budget_brut_2026", "cocof", 2026, -60074000, "", "", "budgeted", SRC, "strong", "Solde budgetaire brut consol -60.074m; tick731"),
    ("bud_cocof_sousutil_2026", "cocof", 2026, 35758000, "", "", "budgeted", SRC, "strong", "Sous-utilisation credits 35.758m (+10.414 vs BA2024 25.344); tick731"),
    ("bud_cocof_sousutil_path_plus_10_4m", "cocof", 2026, 10414000, "", "", "budgeted", SRC, "strong", "Sous-util path +10.414m vs BA2024; tick731"),
    ("bud_cocof_immunisation_infra_2026", "cocof", 2026, 0, "", "", "budgeted", SRC, "strong", "Immunisation certain infra exp 0 (was 14.964m BA2024); tick731"),
    ("bud_cocof_amort_debt_2026", "cocof", 2026, 1608000, "", "", "budgeted", SRC, "strong", "Debt amort 1.608m 2026; tick731"),
    # Decret totals
    ("bud_cocof_decret_rec_2026", "cocof", 2026, 625624000, "", "", "budgeted", SRC, "strong", "Decret recettes 625.624m (+0.452 vs BA2024); tick731"),
    ("bud_cocof_decret_dep_cl_2026", "cocof", 2026, 677505000, "", "", "budgeted", SRC, "strong", "Decret dep liquidations 677.505m (+18.313 vs BA2024); tick731"),
    ("bud_cocof_decret_dep_ce_2026", "cocof", 2026, 667600000, "", "", "budgeted", SRC, "strong", "Decret dep engagements 667.6m (+19.6/+3.0pct vs prov 2025); tick731"),
    ("bud_cocof_reglement_rec_2026", "cocof", 2026, 16112000, "", "", "budgeted", SRC, "strong", "Reglement recettes 16.112m; tick731"),
    ("bud_cocof_reglement_dep_cl_2026", "cocof", 2026, 24305000, "", "", "budgeted", SRC, "strong", "Reglement dep CL 24.305m; tick731"),
    # Debt residual
    ("bud_cocof_debt_eoy2025", "cocof", 2025, 182700000, "", "", "estimated", SRC, "strong", "Debt total eoy2025 182.7m college estimate; tick731"),
    ("bud_cocof_debt_eoy2026", "cocof", 2026, 203700000, "", "", "budgeted", SRC, "strong", "Debt total path eoy2026 203.7m (+21.0m); tick731"),
    ("bud_cocof_debt_path_plus_21m", "cocof", 2026, 21000000, "", "", "budgeted", SRC, "strong", "Debt path +21.0m 2025-26; tick731"),
    ("bud_cocof_credit_line_20m_2026", "cocof", 2026, 20000000, "", "", "budgeted", SRC, "strong", "SPFB cashier credit line 20m first use 2026; tick731"),
    ("bud_cocof_cp_programme_max_20m", "cocof", 2026, 20000000, "", "", "budgeted", SRC, "strong", "Commercial paper programme max 20m launch 2026; tick731"),
    ("bud_cocof_spabs_advance_max_20m", "cocof", 2026, 20000000, "", "", "budgeted", SRC, "strong", "SPABS bruxelloise treasury advance max 20m convention 5Feb2026 ends eoy2026; tick731"),
    # Dotations residual
    ("bud_cocof_dot_rbc_m01_2026", "cocof", 2026, 352378000, "", "", "budgeted", SRC, "strong", "Mission01 RBC dot 352.378m (inst 352.3 + green cert 0.1); tick731"),
    ("bud_cocof_dot_cf_m02_2026", "cocof", 2026, 166778000, "", "", "budgeted", SRC, "strong", "Mission02 CF dot 166.778m (+2.862); tick731"),
    ("bud_cocof_dot_actiris_m03_2026", "cocof", 2026, 3500000, "", "", "budgeted", SRC, "strong", "Mission03 Actiris employment aids reimburse 3.5m; tick731"),
    ("bud_cocof_dot_fed_m04_2026", "cocof", 2026, 94834000, "", "", "budgeted", SRC, "strong", "Mission04 federal dot 94.834m (+1.551); tick731"),
    ("bud_cocof_rec_divers_m06_2026", "cocof", 2026, 7634000, "", "", "budgeted", SRC, "strong", "Mission06 divers 7.634m (mostly undue recoveries 6.6); tick731"),
    ("bud_cocof_interest_rec_m08_2026", "cocof", 2026, 500000, "", "", "budgeted", SRC, "strong", "Mission08 financial interest rec 0.5m (-0.5 vs 2025); tick731"),
    ("bud_cocof_edu_special_rbc_45_8m", "cocof", 2026, 45800000, "", "", "budgeted", SRC, "strong", "RBC special education financing 45.8m still calculated on 2010 pupil count FR vs NL commissions CoA flag; tick731"),
    ("bud_cocof_cf_special_dots_129_8m", "cocof", 2026, 129800000, "", "", "budgeted", SRC, "strong", "CF special dots total 129.8m 2026 (+1.3 vs CF budget figure); tick731"),
    ("bud_cocof_sainte_emilie_22_8m", "cocof", 2026, 22800000, "", "", "budgeted", SRC, "strong", "Sainte-Emilie additional CF transfer 22.8m (-2.2 linear cut dual WAL); tick731"),
    ("bud_cocof_edu_rec_path_13_4m", "cocof", 2026, 13400000, "", "", "budgeted", SRC, "strong", "CF education-related receipts path 13.4m (was 9.0 2025); tick731"),
    ("bud_cocof_cf_decompte_repay_0_7m", "cocof", 2026, 700000, "", "", "budgeted", SRC, "strong", "CF 2025 decompte repay due 0.7m; budget only 0.5m understate 0.2m CoA; tick731"),
    # Missions dep residual Table9
    ("bud_cocof_phare_ce_2026", "phare_cocof", 2026, 210047000, "", "", "budgeted", SRC, "strong", "Phare M32 CE 210.047m (+7.378/+3.6pct); tick731 residual"),
    ("bud_cocof_phare_cl_2026", "phare_cocof", 2026, 210270000, "", "", "budgeted", SRC, "strong", "Phare M32 CL 210.270m (+6.168/+3.0pct); 31.5pct of decret dep; tick731"),
    ("bud_cocof_aide_pers_ce_2026", "cocof", 2026, 113944000, "", "", "budgeted", SRC, "strong", "Aide aux personnes M22 CE 113.944m (+2.680); tick731"),
    ("bud_cocof_aide_pers_cl_2026", "cocof", 2026, 113898000, "", "", "budgeted", SRC, "strong", "Aide aux personnes M22 CL 113.898m (+1.910); 17.1pct; tick731"),
    ("bud_cocof_formation_ce_2026", "cocof", 2026, 92030000, "", "", "budgeted", SRC, "strong", "Formation pro M26 CE 92.030m (-1.020); tick731"),
    ("bud_cocof_formation_cl_2026", "cocof", 2026, 91766000, "", "", "budgeted", SRC, "strong", "Formation pro M26 CL 91.766m (-1.159); 13.8pct; tick731"),
    ("bud_cocof_bf_dot_63_2m", "bruxelles_formation", 2026, 63200000, "", "", "budgeted", SRC, "strong", "Bruxelles Formation organe dot 63.2m flat; dual VDAB/Actiris; tick731 residual"),
    ("bud_cocof_nonmarchand_prov_ce_12_9m", "cocof", 2026, 12900000, "", "", "budgeted", SRC, "strong", "Provision accord non-marchand +12.9m CE (M30); tick731"),
    ("bud_cocof_nonmarchand_prov_cl_13_0m", "cocof", 2026, 13000000, "", "", "budgeted", SRC, "strong", "Provision accord non-marchand +13.0m CL; tick731"),
    ("bud_cocof_encours_eoy2025", "cocof", 2025, 101537000, "", "", "outturn", SRC, "strong", "Encours engagements eoy2025 101.537m; tick731"),
    ("bud_cocof_encours_eoy2026_path", "cocof", 2026, 91642000, "", "", "budgeted", SRC, "strong", "Encours path eoy2026 91.642m (-9.895 if full use); tick731"),
    ("bud_cocof_infra_eng_path_minus_3_7m", "cocof", 2026, -3700000, "", "", "budgeted", SRC, "strong", "Infra M31 eng path -3.7m (-12.2pct); tick731"),
    ("bud_cocof_csf_growth_rec_2_88pct", "cocof", 2026, 2.88, "", "", "estimate", SRC, "strong", "PCT CSF recommends 2.88 net primary growth 2026 / 2.97 avg 2025-31; expose omits metric CoA; tick731"),
    ("bud_cocof_traj_sec_2027", "cocof", 2027, -15000000, "", "", "budgeted", SRC, "strong", "Trajectory SEC -15.0m 2027 toward balance 2029; no measures listed CoA art21 flag; tick731"),
    ("bud_cocof_traj_sec_2028", "cocof", 2028, -7500000, "", "", "budgeted", SRC, "strong", "Trajectory SEC -7.5m 2028; tick731"),
    ("bud_cocof_traj_sec_2029", "cocof", 2029, 0, "", "", "budgeted", SRC, "strong", "Trajectory SEC balance 0 2029 goal; measures unspecified CoA; tick731"),
    ("bud_cocof_infra_ce_2026", "cocof", 2026, 28523000, "", "", "budgeted", SRC, "strong", "Infra eng path Table1 28.523m 2026; tick731"),
    ("bud_cocof_infra_cl_2026", "cocof", 2026, 37055000, "", "", "budgeted", SRC, "strong", "Infra liq path Table1 37.055m 2026; tick731"),
    # Dual
    ("bud_dual_phare_vaph_class", "gg_belgium", 2026, 210270000, "", "", "budgeted", SRC_DUAL, "strong", "Phare CL 210.3m dual VAPH ~2.86bn not additive; tick731"),
    ("bud_dual_cocof_vgc_exp_class", "gg_belgium", 2026, 677505000, "", "", "budgeted", SRC_DUAL, "strong", "COCOF decret CL 677.5m dual VGC exp ~174m outturn class; tick731"),
    ("bud_dual_bf_vdab_class", "gg_belgium", 2026, 63200000, "", "", "budgeted", SRC_DUAL, "strong", "Bruxelles Formation 63.2m dual VDAB/Actiris PES training; tick731"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_cocof_sec_path_2026_29",
        "COCOF SEC path -22.7m 2026 to balance 2029 without measures",
        "cocof",
        "FR Brussels community services users",
        "CoA 2026_21 BI COCOF art21 + Table1-2",
        "2026-03-31",
        2025,
        2029,
        0,
        '{"sec_2026_m":-22.708,"sec_2027_m":-15,"sec_2028_m":-7.5,"sec_2029_m":0,"sousutil_m":35.758,"snf_m":-58.466,"immunisation_m":0,"measures":"unspecified","csf_growth_2026_pct":2.88,"net_primary_metric":"omitted_from_expose"}',
        22708000,
        "active",
        URL,
        "SEC balance by 2029",
        "Publish measures matrix + net primary path FOI art21",
        SRC,
        "strong",
        "Bruxelles>COCOF>SEC_path",
        "tick731 residual",
    ),
    (
        "cmt_cocof_debt_path_203_7m",
        "COCOF debt 182.7 to 203.7m 2026 + CP/credit line 20m dual",
        "cocof",
        "COCOF taxpayers SPABS",
        "CoA 2026_21 ch3 debt residual",
        "2026-03-31",
        2025,
        2026,
        203700000,
        '{"eoy2025_m":182.7,"eoy2026_m":203.7,"path_m":21.0,"credit_line_m":20,"cp_max_m":20,"spabs_advance_m":20,"spabs_convention":"2026-02-05"}',
        0,
        "active",
        URL,
        "Finance SNF and school building stock",
        "Publish debt instrument L5 FOI dual VGC",
        SRC,
        "strong",
        "Bruxelles>COCOF>debt",
        "tick731",
    ),
    (
        "cmt_cocof_phare_210m_residual",
        "Phare disability mission 210.3m CL +3pct dual VAPH",
        "phare_cocof",
        "Persons with disabilities FR Brussels",
        "CoA 2026_21 M32 residual",
        "2026-03-31",
        2026,
        2026,
        210270000,
        '{"ce_m":210.047,"cl_m":210.270,"path_ce_m":7.378,"path_cl_m":6.168,"share_pct":31.5,"dual_vaph_bn":2.86}',
        0,
        "active",
        URL,
        "Disability support services",
        "Named operator L5 FOI dual VAPH unit-cost",
        SRC,
        "strong",
        "Bruxelles>COCOF>Phare",
        "tick731",
    ),
    (
        "cmt_cocof_edu_pupil_count_2010",
        "RBC education special dot 45.8m still on 2010 pupil count",
        "cocof",
        "FR vs NL community commissions schools",
        "CoA 2026_21 s4.1.3 residual",
        "2010-01-01",
        2010,
        2026,
        45800000,
        '{"amount_m":45.8,"pupil_count_year":2010,"coa_flag":"outdated_basis_vs_current_pupils","dual_vgc":true}',
        0,
        "active",
        URL,
        "Fair education financing FR/NL Brussels",
        "Update pupil census basis FOI dual VGC",
        SRC,
        "strong",
        "Bruxelles>COCOF>edu_dot_2010",
        "tick731",
    ),
    (
        "cmt_cocof_bf_63_2m_dual_pes",
        "Bruxelles Formation dot 63.2m dual VDAB/Actiris",
        "bruxelles_formation",
        "FR Brussels jobseekers trainees",
        "CoA 2026_21 M26 residual",
        "2026-03-31",
        2026,
        2026,
        63200000,
        '{"dot_m":63.2,"formation_mission_cl_m":91.766,"targets":["90pct_completion"],"dual":["VDAB","Actiris"]}',
        0,
        "active",
        URL,
        "Professional training FR Brussels",
        "Publish outcome KPIs dual PES FOI",
        SRC,
        "strong",
        "Bruxelles>COCOF>Bruxelles_Formation",
        "tick731",
    ),
    (
        "cmt_dual_cocof_vgc_vaph_tick731",
        "Dual COCOF residual vs VGC outturn and VAPH mega dual",
        "gg_belgium",
        "Brussels multi-community social stack",
        "CoA COCOF 2026_21 + prior VGC/VAPH",
        "2026-03-31",
        2026,
        2026,
        677505000,
        '{"cocof_cl_m":677.5,"phare_m":210.3,"vgc_exp_class_m":174,"vaph_class_bn":2.86,"sec_m":-22.7,"note":"not TE-additive dual community commissions"}',
        0,
        "active",
        URL,
        "Comparable Brussels community service transparency",
        "Dual unit-cost FOI Phare/VAPH/VGC",
        SRC_DUAL,
        "strong",
        "Belgium>dual>COCOF_VGC_VAPH",
        "tick731",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_cocof_sec_soft_path_22_7m",
        "COCOF SEC -22.7m 2026 path to 0 2029 without published measures",
        "Brussels",
        "governance",
        "Bruxelles>COCOF>SEC_soft_path",
        22708000,
        0,
        "Strong CoA art21: trajectory without measures/orientation notes; sous-util 35.8m props solde; CSF net primary metric omitted",
        "strong",
        SRC,
        "Assembly / taxpayers",
        "Honest multi-year SEC path",
        "Balance promise without instrument list",
        7.5,
        6.0,
        3,
        6.65,
        "Publish measures + net primary FOI",
        "seed",
        "",
        "tick731",
    ),
    (
        "lb_cocof_edu_dot_2010_census",
        "Education special RBC 45.8m still on 2010 pupil census",
        "Brussels",
        "ops",
        "Bruxelles>COCOF>edu_2010_count",
        45800000,
        0,
        "Strong CoA: FR/NL commission split still 2010 count; dual fairness flag",
        "strong",
        SRC,
        "FR Brussels pupils",
        "Fair current-pupil financing",
        "16y outdated allocation basis",
        8.0,
        6.5,
        3,
        7.1,
        "Update pupil census FOI dual VGC",
        "seed",
        "",
        "tick731",
    ),
    (
        "lb_cocof_phare_210m_dual_vaph",
        "Phare 210.3m dual VAPH 2.86bn disability architecture",
        "Brussels",
        "ops",
        "Bruxelles>COCOF>Phare",
        210270000,
        0,
        "Strong CoA: 31.5pct of decret dep; +3pct; L5 operators residual dual VAPH",
        "strong",
        SRC,
        "PWD FR Brussels",
        "Disability support",
        "Core service; dual unit-cost opacity",
        5.5,
        7.5,
        5,
        6.15,
        "Named L5 FOI dual unit-cost",
        "seed",
        "",
        "tick731",
    ),
    (
        "lb_cocof_debt_203_7m_path",
        "COCOF debt path 203.7m + first CP/credit line 20m 2026",
        "Brussels",
        "ops",
        "Bruxelles>COCOF>debt_path",
        21000000,
        203700000,
        "Strong CoA: +21m YoY; SPABS advance 20m; school building transfer legacy",
        "strong",
        SRC,
        "COCOF taxpayers",
        "Sustainable community debt",
        "Liquidity tools debut while SEC soft",
        6.5,
        6.5,
        4,
        6.25,
        "Publish instrument calendar FOI",
        "seed",
        "",
        "tick731",
    ),
    (
        "lb_cocof_sousutil_props_35_8m",
        "Sous-utilisation 35.8m props SEC solde (up +10.4m)",
        "Brussels",
        "governance",
        "Bruxelles>COCOF>sousutil",
        35758000,
        0,
        "Strong CoA Table2: without 35.8m sous-util SNF -58.5m; classic soft balance technique dual",
        "strong",
        SRC,
        "Parliament",
        "Honest budget presentation",
        "Solde depends on unused credits assumption",
        7.0,
        6.5,
        3,
        6.5,
        "Track outturn sous-util FOI",
        "seed",
        "",
        "tick731",
    ),
    (
        "lb_cocof_nonmarchand_prov_13m",
        "Non-marchand provision +13m CL in M30 general policy",
        "Brussels",
        "ops",
        "Bruxelles>COCOF>nonmarchand",
        13000000,
        0,
        "Strong CoA: provision in relations internationales/politique generale; dual COCOM non-marchand",
        "strong",
        SRC,
        "Non-profit sector FR Brussels",
        "Wage agreement financing",
        "Cross-mission provision opacity",
        6.0,
        5.5,
        3,
        5.65,
        "Map provision to sector lines FOI",
        "seed",
        "",
        "tick731",
    ),
    (
        "lb_dual_cocof_vgc_vaph_tick731",
        "Dual COCOF 0.68bn vs VGC 0.17bn vs VAPH 2.86bn disability/social",
        "Belgium",
        "ops",
        "Belgium>dual>COCOF_VGC_VAPH",
        677505000,
        0,
        "Strong dual residual: community commission stack FR/NL + Flanders disability mega; not TE-additive",
        "strong",
        SRC_DUAL,
        "Multi-level social users",
        "Comparable disability/PES transparency",
        "Architecture fragmentation dual",
        6.5,
        7.5,
        5,
        6.55,
        "Publish dual unit-cost FOI",
        "seed",
        "",
        "tick731",
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
        "CoA COCOF budgets BI2026 residual dual VGC/VAPH (2026_21)",
        URL,
        "Cour des comptes chambre FR 31 Mar 2026",
        "2026-08-02",
        "court_of_audit",
        "Strong tick731 residual: SEC -22.7 sous-util 35.8; debt 182.7->203.7; Phare 210.3; BF 63.2; edu special 45.8 on 2010 count; non-marchand +13; encours 101.5->91.6; CSF 2.88pct omitted; raw cocof_budget_2026_coa.pdf",
    ),
    (
        SRC_DUAL,
        "Dual COCOF residual vs VGC outturn and VAPH disability mega tick731",
        URL,
        "DOGE synthesis CoA COCOF + prior VGC/VAPH",
        "2026-08-02",
        "synthesis",
        "Strong dual not TE-additive: COCOF 677.5 CL / Phare 210 vs VGC ~174 / VAPH ~2.86bn; tick731",
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
        if row["task_id"] == "rq_722":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick731 COCOF residual dual VGC/VAPH: SEC -22.7 sous-util 35.8; debt 203.7; "
                "Phare 210.3; edu 45.8 on 2010 count; FOI gap_cocof_bi2026_residual_l5 ready"
            )
        rows.append(row)

rows.append({
    "task_id": "rq_723",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "continuous",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "gg_belgium",
    "instructions": (
        "Next residual: new CoA/primary PDF not yet mined or WAL UAP residual or "
        "COCOM residual dual Iriscare or Entity II dual residual"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": "",
    "notes": "spawned tick731 after rq_722",
})

with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("rq_722=done spawn rq_723")

foi_row = (
    "gap_cocof_bi2026_residual_l5",
    "Bruxelles>COCOF>BI2026_residual_L5",
    "cocof",
    (
        "Measures matrix to SEC balance 2029 (art21 notes d'orientation); net primary expenditure path vs CSF 2.88pct; "
        "current pupil census for RBC education special 45.8m (replace 2010 count); "
        "Phare top operators EUR 2024-26; non-marchand provision 13m sector map; "
        "debt instruments calendar credit line/CP/SPABS advances; dual unit-cost Phare vs VAPH and COCOF vs VGC"
    ),
    (
        "CoA residual: soft SEC path, outdated pupil basis 45.8m, Phare 210m L5 thin, dual VGC/VAPH architecture"
    ),
    "7",
    "COCOF College / Assemblée / SPRB transparence",
    "transparence@sprb.brussels",
    "SPRB Place Saint-Lazare 2 1035 Bruxelles",
    "docs/doge/foi/drafts/gap_cocof_bi2026_residual_l5.md",
    "ready",
    "2026-08-02",
    "",
    "",
    "",
    "",
    "cmt_cocof_sec_path_2026_29|cmt_cocof_edu_pupil_count_2010|cmt_cocof_phare_210m_residual",
    "lb_cocof_sec_soft_path_22_7m|lb_cocof_edu_dot_2010_census|lb_cocof_phare_210m_dual_vaph",
    UTC,
    UTC,
    "tick731 CoA COCOF residual; not sent; prior gap_cocof_phare_vgc_l5 remains ready",
)

with open(DATA / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(foi_row)
print("foi +1")

with open(DATA / "loop_state.csv", encoding="utf-8", newline="") as f:
    rows_s = list(csv.reader(f))
header, row = rows_s[0], rows_s[1]
row[3] = UTC
row[4] = "rq_722"
row[5] = "731"
row[7] = (
    "tick731 COCOF residual dual VGC/VAPH; next rq_723; progress@740 in 9; rq_116 deferred"
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(header)
    w.writerow(row)
print("loop_state 731 DONE")

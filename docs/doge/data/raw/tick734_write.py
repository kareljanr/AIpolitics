# tick734 — SPW Rapport Annuel 2025 residual dual VL/Entity II (rq_725)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T04:00:00Z"
# Official SPW Éditions RA2025; PDF saved raw/spw_rapport_activite_2025.pdf
URL = "https://www.wallonie.be"
URL_NOTE = "SPW Rapport annuel 2025 (Editions Secrétariat général; local raw/spw_rapport_activite_2025.pdf)"

SRC = "src_spw_rapport_annuel_2025_residual"
SRC_DUAL = "src_dual_spw_vl_entity2_tick734"

budgets = [
    # Audit / support residual
    ("bud_spw_audit_eu_projects_100m_class", "wallonie_gov", 2025, 100000000, "", "", "outturn", SRC, "strong", "Service commun Audit EU projects audited >100m class 2025; tick734"),
    ("bud_spw_support_nettoyage_save_300k", "spw_support_do11", 2025, 300000, "", "", "outturn", SRC, "strong", "Cleaning markets rationalisation savings ~300k 2025; tick734"),
    # ARNE / agriculture
    ("bud_spw_arne_pac_aids_total_2025", "opw_wallonie", 2025, 379000000, "", "", "outturn", SRC, "strong", "SPW ARNE OPW paid 379m farmer/rural aids 2025; tick734"),
    ("bud_spw_arne_pac_eu_share_2025", "opw_wallonie", 2025, 317000000, "", "", "outturn", SRC, "strong", "Of PAC aids 317m EU financing 2025; tick734"),
    ("bud_spw_arne_pac_rw_share_2025", "opw_wallonie", 2025, 62000000, "", "", "outturn", SRC, "strong", "Of PAC aids 62m RW financing 2025; tick734"),
    ("bud_spw_arne_calamite_agri_2025", "wallonie_gov", 2025, 2835062.96, "", "", "outturn", SRC, "strong", "Agricultural calamity indemnity 2.835m (1209 claims) 2025; tick734"),
    ("bud_spw_arne_cours_eau_eng_2025", "wallonie_gov", 2025, 8322000, "", "", "outturn", SRC, "strong", "1st-category watercourse maintenance eng 8.322m 2025; tick734"),
    ("bud_spw_arne_cours_eau_liq_2025", "wallonie_gov", 2025, 5805000, "", "", "outturn", SRC, "strong", "Watercourse works liquidated 5.805m 2025; tick734"),
    # TLPE territory / housing / heritage / energy
    ("bud_spw_tlpe_ops_programmes_18m", "wallonie_gov", 2025, 18000000, "", "", "outturn", SRC, "strong", "14 operational programmes ~18m (36 projects) 2025; tick734"),
    ("bud_spw_tlpe_sar_sites_7_265m", "wallonie_gov", 2025, 7265000, "", "", "outturn", SRC, "strong", "11 SAR sites supported ~7.265m 2025; tick734"),
    ("bud_spw_logement_subs_public_prog243", "wallonie_gov", 2025, 14681072, "", "", "outturn", SRC, "strong", "Prog243 public housing creation subsidies 14.681m to operators 2025; tick734"),
    ("bud_spw_logement_reno_energy_aids_110m", "wallonie_gov", 2025, 110000000, "", "", "outturn", SRC, "strong", "Housing renovation+energy performance aids >110m invested 2025; tick734"),
    ("bud_spw_awap_heritage_subs_31_3m", "wallonie_gov", 2025, 31300000, "", "", "outturn", SRC, "strong", "AWaP heritage restoration/valorisation grants 31.3m 2025; tick734"),
    ("bud_spw_energie_pape_cpas_1_86m", "spw_energie", 2025, 1860000, "", "", "outturn", SRC, "strong", "89 PAPE energy prevention plans CPAS subsidised 1.86m 2025; tick734"),
    ("bud_spw_energie_mebar_liq_2_707m", "spw_energie", 2025, 2707303.67, "", "", "outturn", SRC, "strong", "MEBAR operation liquidated 2.707m (1169 dossiers) 2025; tick734"),
    ("bud_spw_energie_ureba_liq_4_1m", "spw_energie", 2025, 4100000, "", "", "outturn", SRC, "strong", "UREBA public buildings 304 dossiers liquidated >4.1m 2025; tick734"),
    ("bud_spw_energie_ureba_eng_5_27m", "spw_energie", 2025, 5270000, "", "", "outturn", SRC, "strong", "UREBA 601 dossiers engaged 5.27m 2025; tick734"),
    ("bud_spw_energie_redevances_voirie_60_7m", "spw_energie", 2025, 60700000, "", "", "outturn", SRC, "strong", "Electricity/gas right-of-way fees to entities 60.7m 2025; tick734"),
    ("bud_spw_energie_cv_soutien_330m_class", "spw_energie", 2025, 330000000, "", "", "outturn", SRC, "strong", "Green certificates ~5.08m issued ~330m support class renewable production 2025; tick734"),
    ("bud_spw_energie_amureba_cheques_4_354m", "spw_energie", 2025, 4353810, "", "", "outturn", SRC, "strong", "AMUREBA energy cheques 297 firms 4.354m 2025; tick734"),
    # IAS social / local powers
    ("bud_spw_ias_calamites_acc_96_533m", "wallonie_gov", 2025, 96533480.15, "", "", "outturn", SRC, "strong", "Natural calamities aids granted 96.533m 2025; tick734"),
    ("bud_spw_ias_calamites_paid_96_001m", "wallonie_gov", 2025, 96000854.28, "", "", "outturn", SRC, "strong", "Natural calamities aids paid 96.001m 2025; tick734"),
    ("bud_spw_ias_fin_pouvoirs_locaux_2_322bn", "wallonie_gov", 2025, 2322355000, "", "", "outturn", SRC, "strong", "General financing local powers allocated 2.322355bn 2025; tick734"),
    # EER economy employment research
    ("bud_spw_eer_einstein_20m", "wallonie_gov", 2025, 20000000, "", "", "outturn", SRC, "strong", "Einstein Telescope candidacy support 20m (5m firms) 2025; tick734"),
    ("bud_spw_eer_einstein_if_sited_200m", "wallonie_gov", 2025, 200000000, "", "", "commitment", SRC, "medium", "Einstein implant perspective 200m if sited (conditional); tick734"),
    ("bud_spw_eer_ape_fines_769k", "wallonie_gov", 2025, 769133.75, "", "", "outturn", SRC, "strong", "APE/CFISPA inspection fines 769.134k (1561 controls; part suspended); tick734"),
    ("bud_spw_eer_indemn_commercants_2_972m", "wallonie_gov", 2025, 2972400, "", "", "outturn", SRC, "strong", "510 compensatory indemnities traders works impact 2.972m 2025; tick734"),
    ("bud_spw_eer_parcs_activite_98_647m", "wallonie_gov", 2025, 98647000, "", "", "outturn", SRC, "strong", "Activity parks invest 98.647m (70 dossiers) 2025; tick734"),
    ("bud_spw_eer_cheques_entreprises_16_9m", "wallonie_gov", 2025, 16900000, "", "", "outturn", SRC, "strong", "2973 chèques-entreprises ~16.9m 2025; tick734"),
    ("bud_spw_eer_invest_entreprises_128m", "wallonie_gov", 2025, 128000000, "", "", "outturn", SRC, "strong", "Enterprise investment support 128m (1127 firms) 2025; tick734"),
    ("bud_spw_eer_rd_creances_315_4m", "wallonie_gov", 2025, 315400000, "", "", "outturn", SRC, "strong", "R&D claim declarations 5740 total 315.4m 2025; tick734"),
    # Finances mega residual
    ("bud_spw_fin_dep_control_17_98bn", "wallonie_gov", 2025, 17980000000, "", "", "outturn", SRC, "strong", "Expense control processed 148891 invoices/subs 17.98bn 2025; tick734"),
    ("bud_spw_fin_liq_rate_95_96pct", "wallonie_gov", 2025, 9596, "", "", "outturn", SRC, "strong", "Liquidation credit execution rate 95.96pct COUNT basis 100; tick734"),
    ("bud_spw_fin_actifs_immo_380_255m", "wallonie_gov", 2025, 380255000, "", "", "outturn", SRC, "strong", "Fixed-asset invoices booked 380.255m (vs 355.528 2024); tick734"),
    ("bud_spw_fin_bilan_pied_34_11bn", "wallonie_gov", 2025, 34110000000, "", "", "outturn", SRC, "strong", "SPW balance-sheet foot ~34.11bn eoy2025 (vs 33.82); tick734"),
    ("bud_spw_fin_result_loss_2_73bn", "wallonie_gov", 2025, 2730000000, "", "", "outturn", SRC, "strong", "SPW P&L loss 2.73bn 2025 (vs 2.61 2024); tick734"),
    ("bud_spw_fin_budget_eng_21bn_class", "wallonie_gov", 2025, 21000000000, "", "", "budgeted", SRC, "strong", "RW budget 2631 addresses eng credits >21bn class 2025; tick734"),
    ("bud_spw_fin_budget_liq_22bn_class", "wallonie_gov", 2025, 22000000000, "", "", "budgeted", SRC, "strong", "RW budget liq credits >22bn class 2025; tick734"),
    ("bud_spw_fin_droits_fisc_etablis_3_275bn", "wallonie_gov", 2025, 3275000000, "", "", "outturn", SRC, "strong", "Fiscal rights established 3.275bn (precompte immo 2.219bn) 2025; tick734"),
    ("bud_spw_fin_precompte_immo_etabli_2_219bn", "wallonie_gov", 2025, 2219000000, "", "", "outturn", SRC, "strong", "Precompte immobilier established 2.219bn of 3.275bn 2025; tick734"),
    ("bud_spw_fin_recettes_fisc_3_266bn", "wallonie_gov", 2025, 3266305853, "", "", "outturn", SRC, "strong", "Fiscal recettes perceived 3.266305853bn 2025; tick734"),
    ("bud_spw_fin_reverse_communes_1_287bn", "wallonie_gov", 2025, 1286971280, "", "", "outturn", SRC, "strong", "Precompte reverse to cities/communes 1.28697128bn 2025; tick734"),
    ("bud_spw_fin_reverse_vehicules_56_392m", "wallonie_gov", 2025, 56391670, "", "", "outturn", SRC, "strong", "Vehicle tax reverse to local 56.392m 2025; tick734"),
    ("bud_spw_fin_reverse_provinces_824_506m", "wallonie_gov", 2025, 824506447, "", "", "outturn", SRC, "strong", "Reverse to provinces 824.506m 2025; tick734"),
    # Dual residual maps (not TE-additive)
    ("bud_dual_spw_local_fin_vs_vl_2_322bn", "gg_belgium", 2025, 2322355000, "", "", "outturn", SRC_DUAL, "strong", "WAL local powers fin 2.322bn dual VL municipal fund path; not additive; tick734"),
    ("bud_dual_spw_cv_vs_vl_green_330m", "gg_belgium", 2025, 330000000, "", "", "outturn", SRC_DUAL, "strong", "WAL green-cert support ~330m dual VL renewable support stack; tick734"),
    ("bud_dual_spw_housing_reno_vs_vl_110m", "gg_belgium", 2025, 110000000, "", "", "outturn", SRC_DUAL, "strong", "WAL housing reno/energy aids >110m dual VL wonen subsidies; tick734"),
    ("bud_dual_spw_pac_vs_vl_379m", "gg_belgium", 2025, 379000000, "", "", "outturn", SRC_DUAL, "strong", "WAL PAC/rural aids 379m dual VL agriculture CAP path; tick734"),
    ("bud_dual_spw_rd_vs_vl_315m", "gg_belgium", 2025, 315400000, "", "", "outturn", SRC_DUAL, "strong", "WAL R&D creances 315.4m dual VL FWO/VLAIO research stack; tick734"),
    ("bud_dual_spw_calamites_vs_vl_96_5m", "gg_belgium", 2025, 96533480, "", "", "outturn", SRC_DUAL, "strong", "WAL natural calamities 96.5m dual VL disaster/flood residual; tick734"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_spw_ias_local_fin_2_322bn",
        "SPW IAS general financing local powers 2.322bn 2025",
        "wallonie_gov",
        "Walloon cities communes provinces",
        "SPW Rapport annuel 2025 residual",
        "2025-12-31",
        2025,
        2025,
        2322355000,
        '{"alloue_m":2322.355,"calamites_granted_m":96.533,"calamites_paid_m":96.001,"note":"general financing pouvoirs locaux"}',
        0,
        "active",
        URL,
        "Stable local government financing",
        "Publish L5 commune split FOI dual VL",
        SRC,
        "strong",
        "Wallonie>SPW_IAS>financement_locaux",
        "tick734 residual",
    ),
    (
        "cmt_spw_logement_reno_110m",
        "SPW housing renovation+energy aids >110m + prog243 14.7m",
        "wallonie_gov",
        "Households / public housing operators",
        "SPW RA2025 TLPE logement residual",
        "2025-12-31",
        2025,
        2025,
        124681072,
        '{"reno_energy_m":110,"prog243_public_housing_m":14.681,"allocations_loyer_households":5276,"attente_logement_households":4803}',
        0,
        "active",
        URL,
        "Decent housing access",
        "Top20 operator L5 FOI dual VMSW/SWL",
        SRC,
        "strong",
        "Wallonie>SPW_TLPE>logement",
        "tick734",
    ),
    (
        "cmt_spw_energie_cv_330m",
        "Green certificates support ~330m class + redevances 60.7m",
        "spw_energie",
        "Renewable producers / GRD / entities",
        "SPW RA2025 energie residual",
        "2025-12-31",
        2025,
        2025,
        390700000,
        '{"cv_soutien_m":330,"cv_issued_m":5.08,"redevances_voirie_m":60.7,"ureba_liq_m":4.1,"mebar_m":2.707,"amureba_m":4.354,"pape_m":1.86}',
        0,
        "active",
        URL,
        "Energy transition support",
        "Publish CV cash-by-year FOI dual VL",
        SRC,
        "strong",
        "Wallonie>SPW_TLPE>energie_CV",
        "tick734",
    ),
    (
        "cmt_spw_eer_rd_315m",
        "SPW EER R&D creances 315.4m + enterprise invest 128m",
        "wallonie_gov",
        "Firms and research actors Wallonia",
        "SPW RA2025 EER residual",
        "2025-12-31",
        2025,
        2025,
        443400000,
        '{"rd_creances_m":315.4,"declarations":5740,"invest_entreprises_m":128,"firms":1127,"cheques_m":16.9,"parcs_m":98.647,"einstein_m":20}',
        0,
        "active",
        URL,
        "Regional competitiveness R&D",
        "Named top beneficiaries FOI dual VL",
        SRC,
        "strong",
        "Wallonie>SPW_EER>RD_invest",
        "tick734",
    ),
    (
        "cmt_spw_fin_fiscal_3_266bn",
        "SPW Finances fiscal recettes 3.266bn + reverse 2.17bn class",
        "wallonie_gov",
        "Taxpayers / communes / provinces",
        "SPW RA2025 finances residual",
        "2025-12-31",
        2025,
        2025,
        3266305853,
        '{"percu_m":3266.306,"etabli_m":3275,"precompte_immo_m":2219,"reverse_communes_m":1286.971,"reverse_provinces_m":824.506,"reverse_vehicules_m":56.392,"bilan_bn":34.11,"loss_bn":2.73}',
        0,
        "active",
        URL,
        "Honest fiscal administration",
        "Publish collection rate L5 FOI",
        SRC,
        "strong",
        "Wallonie>SPW_Finances>fiscalite",
        "tick734",
    ),
    (
        "cmt_dual_spw_vl_entity2_tick734",
        "Dual SPW residual vs Flanders Entity II stacks (housing energy PAC R&D local fin)",
        "gg_belgium",
        "Entity II dual map",
        "SPW RA2025 + prior VL dual residuals",
        "2025-12-31",
        2025,
        2025,
        2322355000,
        '{"local_fin_m":2322.355,"cv_m":330,"housing_reno_m":110,"pac_m":379,"rd_m":315.4,"calamites_m":96.5,"note":"not TE-additive dual Entity II"}',
        0,
        "active",
        URL,
        "Comparable Entity II transparency",
        "Dual unit-cost housing energy FOI",
        SRC_DUAL,
        "strong",
        "Belgium>dual>SPW_VL_Entity2",
        "tick734",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_spw_ias_local_fin_2_322bn",
        "SPW IAS local powers financing 2.322bn 2025 — L5 commune split residual",
        "Wallonia",
        "ops",
        "Wallonie>SPW_IAS>financement_locaux",
        2322355000,
        0,
        "Strong RA2025: 2.322355bn alloue; dual VL municipal fund path; top commune matrix FOI",
        "strong",
        SRC,
        "Walloon local governments",
        "General financing pouvoirs locaux",
        "Aggregate only; L5 opacity",
        5.5,
        9.0,
        4,
        7.0,
        "Publish machine-readable commune split FOI dual",
        "seed",
        "",
        "tick734",
    ),
    (
        "lb_spw_cv_soutien_330m",
        "Green certificates support ~330m class 2025 dual VL renewables",
        "Wallonia",
        "ops",
        "Wallonie>SPW_TLPE>energie_CV",
        330000000,
        0,
        "Strong RA2025: 5.08m certificates ~330m support; redevances 60.7m separate; dual VL",
        "strong",
        SRC,
        "Renewable producers",
        "Support green electricity production",
        "Large off-budgetish support class",
        6.5,
        8.0,
        4,
        6.9,
        "Cash-by-year CV FOI dual VL",
        "seed",
        "",
        "tick734",
    ),
    (
        "lb_spw_housing_reno_110m",
        "Housing reno+energy aids >110m + prog243 14.7m without top20 L5",
        "Wallonia",
        "ops",
        "Wallonie>SPW_TLPE>logement",
        124681072,
        0,
        "Strong RA2025 aggregates; dual VMSW/SWL housing finance; operator L5 residual FOI",
        "strong",
        SRC,
        "Households / housing operators",
        "Decent housing + energy performance",
        "End-receiver opacity dual",
        6.0,
        7.5,
        3,
        6.45,
        "Top20 operators machine-readable FOI",
        "seed",
        "",
        "tick734",
    ),
    (
        "lb_spw_rd_creances_315m",
        "R&D claim declarations 315.4m + enterprise invest 128m L5 gap",
        "Wallonia",
        "ops",
        "Wallonie>SPW_EER>RD_invest",
        443400000,
        0,
        "Strong RA2025: 5740 declarations 315.4m RD; 128m to 1127 firms; dual VL research stack",
        "strong",
        SRC,
        "Firms / research actors",
        "Innovation competitiveness",
        "Named beneficiaries residual",
        6.0,
        8.0,
        3,
        6.6,
        "Named top beneficiaries FOI dual",
        "seed",
        "",
        "tick734",
    ),
    (
        "lb_spw_calamites_96_5m",
        "Natural calamities aids 96.5m granted / 96.0m paid 2025",
        "Wallonia",
        "ops",
        "Wallonie>SPW_IAS>calamites",
        96533480,
        0,
        "Strong RA2025: 4 public natural calamities recognised; dual VL disaster residual",
        "strong",
        SRC,
        "Affected households/firms",
        "Disaster recovery",
        "Core safety-net spend",
        4.5,
        7.0,
        3,
        5.55,
        "L5 claim type split FOI",
        "seed",
        "",
        "tick734",
    ),
    (
        "lb_spw_pac_aids_379m",
        "PAC/rural aids 379m (EU 317 + RW 62) OPW 2025 dual VL",
        "Wallonia",
        "ops",
        "Wallonie>SPW_ARNE>PAC",
        379000000,
        0,
        "Strong RA2025 OPW: pillars+invest+LEADER; dual VL CAP path",
        "strong",
        SRC,
        "Farmers / rural development",
        "CAP strategic plan delivery",
        "Large EU-cofinanced stack",
        5.0,
        8.0,
        3,
        6.1,
        "Measure-level FOI dual VL",
        "seed",
        "",
        "tick734",
    ),
    (
        "lb_dual_spw_vl_entity2_asymmetry",
        "Dual SPW residual vs Flanders Entity II (local fin / CV / housing / PAC / R&D)",
        "Belgium",
        "ops",
        "Belgium>dual>SPW_VL_Entity2",
        2322355000,
        0,
        "Strong dual residual not TE-additive: local 2.32bn / CV 330 / housing 110 / PAC 379 / RD 315; Entity II dual map",
        "strong",
        SRC_DUAL,
        "Entity II dual residents",
        "Comparable regional admin transparency",
        "Asymmetric dual residual stacks",
        7.0,
        8.0,
        4,
        7.1,
        "Dual unit-cost FOI matrix",
        "seed",
        "",
        "tick734",
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
        "SPW Rapport annuel 2025 residual multi-DG L5 dual Entity II",
        URL,
        "SPW Éditions – Secrétariat général",
        "2026-08-02",
        "official_annual_report",
        "Strong tick734 residual from RA2025: IAS local fin 2.322bn; calamites 96.5; PAC 379 (EU317+RW62); housing reno>110 + prog243 14.7; CV~330; redevances 60.7; R&D 315.4; enterprise invest 128; parcs 98.6; fiscal percu 3.266bn reverse communes 1.287+provinces 0.825; bilan 34.11bn loss 2.73; raw spw_rapport_activite_2025.pdf",
    ),
    (
        SRC_DUAL,
        "Dual SPW RA2025 residual vs Flanders Entity II stacks tick734",
        URL,
        "DOGE synthesis SPW + prior VL duals",
        "2026-08-02",
        "synthesis",
        "Strong dual not TE-additive: local fin 2.32bn dual VL municipal; CV 330 dual VL green; housing 110 dual VL wonen; PAC 379 dual VL CAP; R&D 315 dual FWO/VLAIO; calamites 96.5 dual VL; tick734",
    ),
]

with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in sources:
        w.writerow(r)
print("sources +", len(sources))

# research_queue: mark rq_725 done, spawn rq_726
rq_path = DATA / "research_queue.csv"
rows = []
with open(rq_path, encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_725":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick734 SPW RA2025 residual dual Entity II: local fin 2.322bn; CV 330; "
                "housing reno 110; PAC 379; R&D 315; fiscal 3.266bn; FOI gap_spw_ra2025_residual_l5 ready"
            )
        rows.append(row)

rows.append({
    "task_id": "rq_726",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "continuous",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "gg_belgium",
    "instructions": (
        "Next residual: new CoA/primary PDF not yet mined or SWL/SWCS dual VMSW residual "
        "or SLRB residual dual housing or Entity II dual residual"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": "",
    "notes": "spawned tick734 after rq_725",
})

with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("rq_725=done spawn rq_726")

foi_row = (
    "gap_spw_ra2025_residual_l5",
    "Wallonie>SPW>RA2025_residual_L5",
    "wallonie_gov",
    (
        "Machine-readable L5: (1) commune/province split of 2.322bn local financing 2025; "
        "(2) top20 prog243 public housing operators 14.681m + top20 renovation/energy aid recipients "
        "within >110m stack; (3) green certificates cash-by-year support series reconciling ~330m class; "
        "(4) top20 R&D creances beneficiaries of 315.4m and enterprise invest 128m (1127 firms); "
        "(5) natural calamities claim-type split of 96.5m; dual unit-cost notes vs Flanders analogues"
    ),
    (
        "RA2025 gives strong aggregates across DGs but no named end-receivers; dual Entity II "
        "comparison (VL municipal fund / wonen / CAP / green / research) needs L5 for waste scoring"
    ),
    "8",
    "SPW publicité de l'administration / Secrétariat général",
    "",
    "https://www.wallonie.be",
    "docs/doge/foi/drafts/gap_spw_ra2025_residual_l5.md",
    "ready",
    "2026-08-02",
    "",
    "",
    "",
    "",
    "cmt_spw_ias_local_fin_2_322bn|cmt_spw_logement_reno_110m|cmt_spw_energie_cv_330m|cmt_spw_eer_rd_315m",
    "lb_spw_ias_local_fin_2_322bn|lb_spw_cv_soutien_330m|lb_dual_spw_vl_entity2_asymmetry",
    UTC,
    UTC,
    "tick734 SPW RA2025 residual dual Entity II; ready not sent",
)

with open(DATA / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(foi_row)
print("foi + gap_spw_ra2025_residual_l5")

# loop_state
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow([
        "state_id", "mode", "current_sprint", "last_tick_utc", "last_unit_id",
        "ticks_completed", "paused", "notes",
    ])
    w.writerow([
        "main", "continuous", "hole_fill", UTC, "rq_725", "734", "no",
        "tick734 SPW RA2025 residual dual Entity II; next rq_726; progress@740 in 6; rq_116 deferred",
    ])
print("loop_state ticks=734")

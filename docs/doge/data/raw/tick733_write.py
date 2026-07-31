# tick733 — VGC jaarrekening 2025 residual dual COCOF (rq_724)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]
UTC = "2026-08-02T03:15:00Z"
URL = "https://www.vgc.be/sites/vgc/files/2026-07/20260710%20Jaarrekening%202025%20Raad%20VGC%2010%20juli%202026%20-%20deel%201.pdf"

SRC = "src_vgc_jaarrekening_2025_residual"
SRC_DUAL = "src_dual_vgc_cocof_tick733"

budgets = [
    # Functional exp residual (mEUR from T1 * 1e6)
    ("bud_vgc_func_alg_fin_2025", "vgc", 2025, 10730000, "", "", "outturn", SRC, "strong", "Functional Algemene financiering exp 10.73m (lease/debt central); tick733"),
    ("bud_vgc_func_alg_zaken_2025", "vgc", 2025, 46310000, "", "", "outturn", SRC, "strong", "Functional Algemene zaken exp 46.31m (26.7pct); tick733"),
    ("bud_vgc_func_onderwijs_2025", "vgc", 2025, 53850000, "", "", "outturn", SRC, "strong", "Functional Onderwijs en Vorming exp 53.85m (31.0pct largest); tick733"),
    ("bud_vgc_func_cultuur_2025", "vgc", 2025, 43380000, "", "", "outturn", SRC, "strong", "Functional Cultuur Jeugd Sport exp 43.38m (25.0pct); tick733"),
    ("bud_vgc_func_welzijn_2025", "vgc", 2025, 19360000, "", "", "outturn", SRC, "strong", "Functional Welzijn Gezondheid Gezin exp 19.36m (11.2pct); tick733"),
    ("bud_vgc_func_total_recon_2025", "vgc", 2025, 173630000, "", "", "outturn", SRC, "strong", "Functional exp total 173.63m recon schema T1; tick733"),
    # Economic residual path
    ("bud_vgc_econ_goederen_2025", "vgc", 2025, 19040000, "", "", "outturn", SRC, "strong", "Economic goods/services 19.04m; tick733"),
    ("bud_vgc_econ_personeel_2025", "vgc", 2025, 89020000, "", "", "outturn", SRC, "strong", "Economic personnel 89.02m (51.3pct; +6.4pct vs 83.6 2024); tick733"),
    ("bud_vgc_econ_werksubs_2025", "vgc", 2025, 53880000, "", "", "outturn", SRC, "strong", "Economic granted werksubs 53.88m (31.0pct); tick733"),
    ("bud_vgc_econ_fin_uit_2025", "vgc", 2025, 10320000, "", "", "outturn", SRC, "strong", "Economic financial exp 10.32m (lease Deleers PPS activation); tick733"),
    ("bud_vgc_personeel_path_plus_6_4pct", "vgc", 2025, 6400000, "", "", "outturn", SRC, "strong", "Personnel path +~6.4m class (+6.4pct) barema/index/staff; cadre underfilled vs MJP; tick733"),
    ("bud_vgc_pers_vast_niet_ond_2025", "vgc", 2025, 18383908, "", "", "outturn", SRC, "strong", "Pers vastbenoemd non-teaching 18.384m; tick733"),
    ("bud_vgc_pers_niet_vast_2025", "vgc", 2025, 39329653, "", "", "outturn", SRC, "strong", "Pers non-vast non-teaching 39.330m; tick733"),
    ("bud_vgc_pers_onderwijs_2025", "vgc", 2025, 6995935, "", "", "outturn", SRC, "strong", "Teaching staff on VGC charge 6.996m; tick733"),
    ("bud_vgc_pers_andere_2025", "vgc", 2025, 5011809, "", "", "outturn", SRC, "strong", "Other personnel costs 5.012m; tick733"),
    # Dotaties residual
    ("bud_vgc_dot_fed_2025", "vgc", 2025, 23435510, "", "", "outturn", SRC, "strong", "Dot federal 23.436m; tick733"),
    ("bud_vgc_dot_vl_2025", "vgc", 2025, 50810927, "", "", "outturn", SRC, "strong", "Dot Flanders 50.811m; tick733"),
    ("bud_vgc_dot_bcr_2025", "vgc", 2025, 96785278, "", "", "outturn", SRC, "strong", "Dot BCR 96.785m (shortfall ~1.65m vs plan); tick733"),
    ("bud_vgc_dot_total_2025", "vgc", 2025, 171031716, "", "", "outturn", SRC, "strong", "Dotaties total 171.032m; tick733"),
    ("bud_vgc_bcr_shortfall_1_65m", "vgc", 2025, -1650000, "", "", "outturn", SRC, "strong", "BCR minderontvangst 1.65m vs plan 2025; tick733"),
    ("bud_vgc_spec_werksubs_rec_2025", "vgc", 2025, 42239723, "", "", "outturn", SRC, "strong", "Specific werksubs received 42.240m (+5.8 vs 36.5 2024); tick733"),
    ("bud_vgc_spec_werksubs_vl_2025", "vgc", 2025, 36956424, "", "", "outturn", SRC, "strong", "Specific werksubs from Flanders 36.956m (was 31.3); tick733"),
    ("bud_vgc_spec_werksubs_bcr_2025", "vgc", 2025, 4527422, "", "", "outturn", SRC, "strong", "Specific werksubs from BCR 4.527m; tick733"),
    ("bud_vgc_alg_werksubs_rec_2025", "vgc", 2025, 745000, "", "", "outturn", SRC, "strong", "General werksubs received 0.745m (reclass to specific); tick733"),
    ("bud_vgc_own_werking_rec_2025", "vgc", 2025, 1977747, "", "", "outturn", SRC, "strong", "Own operation receipts 1.978m (limited own revenue capacity); tick733"),
    ("bud_vgc_fin_ont_2025", "vgc", 2025, 5544223, "", "", "outturn", SRC, "strong", "Financial receipts 5.544m (treasury interest; >> MJP 0.54); tick733"),
    ("bud_vgc_dots_subs_total_2025", "vgc", 2025, 214016438, "", "", "outturn", SRC, "strong", "Dotaties+werksubs received 214.016m; tick733"),
    # Invest residual
    ("bud_vgc_inv_mva_2025", "vgc", 2025, 81458036, "", "", "outturn", SRC, "strong", "Invest MVA 81.458m (classic ~18.1 + PPS Deleers lease activation ~64); tick733"),
    ("bud_vgc_inv_classic_infra_2025", "vgc", 2025, 18100000, "", "", "outturn", SRC, "strong", "Classic own infra invest ~18.1m (buildings 13.0 movable 4.6 imm 0.5); tick733"),
    ("bud_vgc_inv_pps_deleers_lease_64m", "vgc", 2025, 64000000, "", "", "outturn", SRC, "strong", "PPS Deleers lease activation ~64m in use 2025; tick733"),
    ("bud_vgc_invsubs_granted_2025", "vgc", 2025, 17566417, "", "", "outturn", SRC, "strong", "Investment subsidies granted 17.566m (education/welfare/sport); tick733"),
    ("bud_vgc_invsubs_onderwijs_ap11_class", "vgc", 2025, 9656966, "", "", "outturn", SRC, "strong", "Invsubs onderwijs infrastructure class ~9.66m (6.573+3.084 AP11); tick733"),
    ("bud_vgc_invsubs_welzijn_ap64_2_82m", "vgc", 2025, 2822923, "", "", "outturn", SRC, "strong", "Invsubs welzijn AP64 2.823m; tick733"),
    # Solde residual
    ("bud_vgc_exp_saldo_vs_mjp_gap", "vgc", 2025, 21244000, "", "", "outturn", SRC, "strong", "Exp saldo 51.335 vs MJP 30.091 gap +21.24m (under-spend + treasury interest); tick733"),
    ("bud_vgc_afschrijvingen_2025", "vgc", 2025, 12450000, "", "", "outturn", SRC, "strong", "Depreciation 12.45m (vs 42.18 2024; one-off responsabilisering 31.21 2024); tick733"),
    ("bud_vgc_responsabiliserings_prov_2024", "vgc", 2024, 31210000, "", "", "outturn", SRC, "strong", "One-off responsabilisering provision 31.21m booked 2024 for 2025-30; tick733"),
    # Dual
    ("bud_dual_vgc_cocof_exp_2025_26", "gg_belgium", 2025, 173627909, "", "", "outturn", SRC_DUAL, "strong", "VGC exp outturn 173.6 dual COCOF decret CL 677.5 2026; not additive; tick733"),
    ("bud_dual_vgc_werksubs_vs_phare", "gg_belgium", 2025, 53883069, "", "", "outturn", SRC_DUAL, "strong", "VGC werksubs granted 53.9 dual Phare 210.3 COCOF; different instruments; tick733"),
    ("bud_dual_vgc_surplus_vs_cocof_sec", "gg_belgium", 2025, 51335168, "", "", "outturn", SRC_DUAL, "strong", "VGC exp surplus 51.3 dual COCOF SEC path -22.7 2026; tick733"),
    ("bud_dual_vgc_debt_vs_cocof", "gg_belgium", 2025, 242125466, "", "", "outturn", SRC_DUAL, "strong", "VGC debt 242.1 dual COCOF path 203.7 2026; tick733"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_vgc_func_onderwijs_53_9m",
        "VGC functional Onderwijs 53.85m largest domain dual COCOF education",
        "vgc",
        "NL Brussels education users",
        "VGC jaarrekening 2025 schema T1 residual",
        "2026-07-10",
        2025,
        2025,
        53850000,
        '{"onderwijs_m":53.85,"cultuur_m":43.38,"alg_zaken_m":46.31,"welzijn_m":19.36,"alg_fin_m":10.73,"total_m":173.63,"share_ond_pct":31.0}',
        0,
        "active",
        URL,
        "NL community education and services Brussels",
        "Publish L5 school/operator matrix FOI dual COCOF",
        SRC,
        "strong",
        "Bruxelles>VGC>Onderwijs",
        "tick733 residual",
    ),
    (
        "cmt_vgc_dots_dependency_214m",
        "VGC 214m dots+subs received; own revenue only 2.0m",
        "vgc",
        "VGC as transfer-dependent community commission",
        "Jaarrekening 2025 T2 residual",
        "2026-07-10",
        2025,
        2025,
        214016438,
        '{"dots_m":171.03,"bcr_m":96.79,"vl_m":50.81,"fed_m":23.44,"spec_subs_m":42.24,"own_m":1.98,"fin_int_m":5.54,"bcr_shortfall_m":1.65}',
        0,
        "active",
        URL,
        "Stable multi-level financing",
        "Track BCR shortfall FOI dual COCOF dots",
        SRC,
        "strong",
        "Bruxelles>VGC>dots_dependency",
        "tick733",
    ),
    (
        "cmt_vgc_pps_deleers_lease_64m",
        "PPS Deleers lease activation ~64m of 81.5m MVA invest 2025",
        "vgc",
        "School/infra users NL Brussels",
        "Jaarrekening 2025 invest residual",
        "2025-01-01",
        2025,
        2045,
        64000000,
        '{"mva_total_m":81.46,"classic_m":18.1,"lease_activation_m":64,"invsubs_granted_m":17.57,"fin_exp_m":10.32}',
        0,
        "active",
        URL,
        "School infrastructure PPS delivery",
        "Publish full PPS cash redevance FOI dual",
        SRC,
        "strong",
        "Bruxelles>VGC>PPS_Deleers",
        "tick733",
    ),
    (
        "cmt_vgc_exp_saldo_vs_mjp",
        "Exp saldo 51.3 vs MJP 30.1 under-spend + treasury windfall",
        "vgc",
        "Raad / taxpayers",
        "Jaarrekening 2025 residual vs MJP",
        "2026-07-10",
        2025,
        2025,
        21244000,
        '{"saldo_m":51.335,"mjp_m":30.091,"gap_m":21.24,"drivers":["cadre_underfill","subsidy_shifts","treasury_interest"],"lopende_zaken":true}',
        0,
        "active",
        URL,
        "Honest budget execution",
        "Publish cadre fill rates FOI",
        SRC,
        "strong",
        "Bruxelles>VGC>saldo_vs_mjp",
        "tick733",
    ),
    (
        "cmt_vgc_werksubs_53_9m_l5_gap",
        "VGC granted werksubs 53.9m top20 operators residual FOI",
        "vgc",
        "NL Brussels civil society",
        "Jaarrekening 2025 + prior FOI gap_cocof_phare_vgc_l5",
        "2026-07-10",
        2025,
        2025,
        53883069,
        '{"werksubs_m":53.883,"path_vs_2024_m":0.5,"mjp_m":58.93,"realisatie_below_raming":true}',
        0,
        "active",
        URL,
        "Transparent field subsidies",
        "Top20 machine-readable FOI dual Phare",
        SRC,
        "strong",
        "Bruxelles>VGC>werksubs_L5",
        "tick733",
    ),
    (
        "cmt_dual_vgc_cocof_tick733",
        "Dual VGC surplus outturn vs COCOF soft SEC path",
        "gg_belgium",
        "Brussels multi-community stack",
        "VGC JR2025 + CoA COCOF BI2026 dual",
        "2026-07-10",
        2025,
        2026,
        173627909,
        '{"vgc_exp_m":173.6,"vgc_saldo_m":51.3,"vgc_debt_m":242.1,"vgc_werksubs_m":53.9,"cocof_cl_m":677.5,"cocof_sec_m":-22.7,"cocof_phare_m":210.3,"note":"not TE-additive dual community commissions"}',
        0,
        "active",
        URL,
        "Comparable FR/NL community commission transparency",
        "Dual unit-cost education disability culture FOI",
        SRC_DUAL,
        "strong",
        "Belgium>dual>VGC_COCOF",
        "tick733",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_vgc_dots_dependency_214m",
        "VGC 214m dots+subs vs 2.0m own revenue — transfer dependency",
        "Brussels",
        "ops",
        "Bruxelles>VGC>dots_dependency",
        214016438,
        0,
        "Strong JR2025: BCR 96.8 VL 50.8 fed 23.4 + specific 42.2; own 2.0; BCR shortfall 1.65",
        "strong",
        SRC,
        "NL Brussels residents",
        "Stable multi-level financing",
        "Structural transfer dependence dual COCOF",
        6.0,
        8.0,
        4,
        6.6,
        "Track BCR shortfall FOI dual",
        "seed",
        "",
        "tick733",
    ),
    (
        "lb_vgc_pps_deleers_64m",
        "PPS Deleers lease activation ~64m dominates 2025 invest",
        "Brussels",
        "ops",
        "Bruxelles>VGC>PPS_Deleers",
        64000000,
        0,
        "Strong JR2025: of 81.5m MVA invest ~64 lease activation; fin exp 10.3; dual COCOF school buildings",
        "strong",
        SRC,
        "School users",
        "Transparent PPP school finance",
        "Lease stock jump dual",
        6.5,
        7.0,
        4,
        6.4,
        "Publish redevance path FOI",
        "seed",
        "",
        "tick733",
    ),
    (
        "lb_vgc_onderwijs_53_9m_dual",
        "VGC Onderwijs 53.85m dual COCOF education/Phare architecture",
        "Brussels",
        "ops",
        "Bruxelles>VGC>Onderwijs",
        53850000,
        0,
        "Strong functional T1: 31pct of exp; dual COCOF education + Phare 210 disability",
        "strong",
        SRC,
        "NL pupils Brussels",
        "Community education",
        "Core dual community stack",
        5.5,
        7.0,
        4,
        6.05,
        "L5 school matrix FOI dual",
        "seed",
        "",
        "tick733",
    ),
    (
        "lb_vgc_saldo_over_mjp_21m",
        "Exp saldo 51.3 vs MJP 30.1 (+21m) cadre underfill + treasury",
        "Brussels",
        "governance",
        "Bruxelles>VGC>saldo_vs_mjp",
        21244000,
        0,
        "Strong JR2025: under-execution + interest windfall in lopende zaken period",
        "strong",
        SRC,
        "Raad",
        "Honest planning vs outturn",
        "Chronic under-fill of plans",
        6.5,
        6.0,
        3,
        6.1,
        "Cadre fill rates FOI",
        "seed",
        "",
        "tick733",
    ),
    (
        "lb_vgc_werksubs_53_9m_l5",
        "Werksubs 53.9m granted without public top20 L5 list",
        "Brussels",
        "ops",
        "Bruxelles>VGC>werksubs_L5",
        53883069,
        0,
        "Strong aggregate; FOI gap_cocof_phare_vgc_l5 still open for names",
        "strong",
        SRC,
        "Civil society NL Brussels",
        "Transparent subsidies",
        "End-receiver opacity dual Phare",
        6.5,
        7.0,
        3,
        6.45,
        "Top20 machine-readable FOI",
        "seed",
        "",
        "tick733",
    ),
    (
        "lb_vgc_bcr_shortfall_1_65m",
        "BCR dot shortfall 1.65m 2025 vs plan",
        "Brussels",
        "ops",
        "Bruxelles>VGC>BCR_shortfall",
        1650000,
        0,
        "Strong JR2025: important minderontvangst BCR; dual regional transfer risk",
        "strong",
        SRC,
        "VGC budget",
        "Reliable BCR transfers",
        "Transfer volatility",
        6.0,
        4.5,
        3,
        5.4,
        "Explain shortfall FOI",
        "seed",
        "",
        "tick733",
    ),
    (
        "lb_dual_vgc_cocof_surplus_asymmetry",
        "Dual VGC +51m surplus vs COCOF SEC -22.7 soft path",
        "Belgium",
        "ops",
        "Belgium>dual>VGC_COCOF_asymmetry",
        51335168,
        0,
        "Strong dual residual: NL commission surplus outturn vs FR commission soft SEC; different scales debt 242 vs 204; not TE-additive",
        "strong",
        SRC_DUAL,
        "Brussels multi-community",
        "Comparable fiscal honesty",
        "Asymmetric community commission finance dual",
        7.0,
        7.0,
        4,
        6.7,
        "Dual unit-cost FOI",
        "seed",
        "",
        "tick733",
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
        "VGC Jaarrekening 2025 residual functional/economic/invest dual COCOF",
        URL,
        "Vlaamse Gemeenschapscommissie Raad 10 Jul 2026",
        "2026-08-02",
        "official_annual_report",
        "Strong tick733 residual: func onderwijs 53.85 cultuur 43.38 welzijn 19.36; pers 89.02; werksubs 53.88; dots BCR96.8 VL50.8 fed23.4; PPS Deleers ~64; invsubs 17.57; saldo 51.3 vs MJP 30.1; dual COCOF; raw vgc_jaarrekening_2025_deel1.pdf",
    ),
    (
        SRC_DUAL,
        "Dual VGC JR2025 residual vs COCOF BI2026 soft SEC tick733",
        URL,
        "DOGE synthesis VGC + CoA COCOF",
        "2026-08-02",
        "synthesis",
        "Strong dual not TE-additive: VGC surplus 51.3 / exp 173.6 / debt 242 vs COCOF SEC -22.7 / CL 677.5 / Phare 210; tick733",
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
        if row["task_id"] == "rq_724":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick733 VGC residual dual COCOF: onderwijs 53.85; werksubs 53.9; PPS Deleers ~64; "
                "dots 214; saldo 51.3 vs MJP 30.1; FOI gap_vgc_jr2025_residual_l5 ready"
            )
        rows.append(row)

rows.append({
    "task_id": "rq_725",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "continuous",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "gg_belgium",
    "instructions": (
        "Next residual: new CoA/primary PDF not yet mined or WAL UAP residual or "
        "Entity II dual residual or VGC MJP 2026-31 if published"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": "",
    "notes": "spawned tick733 after rq_724",
})

with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("rq_724=done spawn rq_725")

foi_row = (
    "gap_vgc_jr2025_residual_l5",
    "Bruxelles>VGC>JR2025_residual_L5",
    "vgc",
    (
        "Top20 werkingssubsidies granted 2024-2025 with EUR and policy domain; "
        "PPS Deleers full redevance/cash calendar and residual lease liability; "
        "cadre fill rates by domain explaining under-spend vs MJP; "
        "BCR dot shortfall 1.65m explanation; "
        "2026-2031 MJP totals when final; dual unit-cost vs COCOF education/Phare"
    ),
    (
        "JR2025 aggregates strong; end-receiver L5 and PPS cash residual dual COCOF"
    ),
    "6",
    "VGC College / Raad / SPRB transparence",
    "transparence@sprb.brussels",
    "SPRB Place Saint-Lazare 2 1035 Bruxelles",
    "docs/doge/foi/drafts/gap_vgc_jr2025_residual_l5.md",
    "ready",
    "2026-08-02",
    "",
    "",
    "",
    "",
    "cmt_vgc_werksubs_53_9m_l5_gap|cmt_vgc_pps_deleers_lease_64m|cmt_dual_vgc_cocof_tick733",
    "lb_vgc_werksubs_53_9m_l5|lb_vgc_pps_deleers_64m|lb_dual_vgc_cocof_surplus_asymmetry",
    UTC,
    UTC,
    "tick733 VGC residual; not sent; prior gap_cocof_phare_vgc_l5 remains ready",
)

with open(DATA / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(foi_row)
print("foi +1")

with open(DATA / "loop_state.csv", encoding="utf-8", newline="") as f:
    rows_s = list(csv.reader(f))
header, row = rows_s[0], rows_s[1]
row[3] = UTC
row[4] = "rq_724"
row[5] = "733"
row[7] = (
    "tick733 VGC residual dual COCOF; next rq_725; progress@740 in 7; rq_116 deferred"
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(header)
    w.writerow(row)
print("loop_state 733 DONE")

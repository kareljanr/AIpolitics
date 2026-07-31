# tick719 — WAL SOFICO comptes 2025 residual L5 commitments dual AWV/GIP
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parents[1]

budgets = [
    ("bud_sofico_commit_acq_immob_eoy2025", "sofico", 2025, 280022174, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Engagements importants acquisition immobilisations encours 280.0m eoy2025 CoA comptes p30; tick719"),
    ("bud_sofico_debt_guaranteed_public_2025", "sofico", 2025, 494762474, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Dettes garanties par pouvoirs publics belges 494.8m (banks 325.3 + autres 169.5) eoy2025; tick719"),
    ("bud_sofico_debt_banks_lt_2025", "sofico", 2025, 298077035, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Dettes etablissements credit LT 298.1m eoy2025; tick719"),
    ("bud_sofico_debt_autres_emprunts_lt_2025", "sofico", 2025, 169500000, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Autres emprunts LT 169.5m eoy2025; tick719"),
    ("bud_sofico_debt_lt_due_1y_2025", "sofico", 2025, 27185439, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Dettes LT echues dans annee 27.2m (credit) eoy2025; tick719"),
    ("bud_sofico_debt_st_autres_2025", "sofico", 2025, 12500000, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Autres emprunts ST 12.5m eoy2025; tick719"),
    ("bud_sofico_debt_1_5y_2025", "sofico", 2025, 154435459, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Dettes 1-5y residual 154.4m eoy2025; tick719"),
    ("bud_sofico_debt_gt5y_2025", "sofico", 2025, 313170176, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Dettes >5y residual 313.2m eoy2025; tick719"),
    ("bud_sofico_suppliers_st_2025", "sofico", 2025, 139328459, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Fournisseurs ST 139.3m eoy2025; tick719"),
    ("bud_sofico_tax_est_2025", "sofico", 2025, 22337321, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Dettes fiscales estimees 22.3m eoy2025; tick719"),
    ("bud_sofico_tax_non_due_2025", "sofico", 2025, 10529555, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Dettes fiscales non echeues 10.5m; tick719"),
    ("bud_sofico_charges_imputer_2025", "sofico", 2025, 3273980, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Charges a imputer 3.27m; tick719"),
    ("bud_sofico_produits_reporter_2025", "sofico", 2025, 8320824, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Produits a reporter 8.32m; tick719"),
    ("bud_sofico_cap_subs_pnl_2025", "sofico", 2025, 14029440, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Subsides capital imputes P&L 14.03m (11.85m 2024); tick719"),
    ("bud_sofico_remun_direct_2025", "sofico", 2025, 4016436, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Remunerations directes 4.02m of personnel 6.28m; tick719"),
    ("bud_sofico_er_ss_2025", "sofico", 2025, 1103585, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Cotisations patronales ONSS 1.10m; tick719"),
    ("bud_sofico_extralegal_ins_2025", "sofico", 2025, 842470, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Primes extralegales 0.84m; tick719"),
    ("bud_sofico_hours_worked_2025", "sofico", 2025, 68632, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Heures prestees 68632 (FTE 49.5 headcount 51); tick719"),
    ("bud_sofico_vat_charged_2025", "sofico", 2025, 203308116, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "TVA portee en compte par societe 203.3m; tick719"),
    ("bud_sofico_vat_deductible_2025", "sofico", 2025, 113332390, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "TVA deductible 113.3m; tick719"),
    ("bud_sofico_pp_withheld_2025", "sofico", 2025, 1277412, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Precompte professionnel retenu 1.28m; tick719"),
    ("bud_sofico_tax_on_result_2025", "sofico", 2025, 5019158, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Impots resultat exercice 5.02m (due 3.36 + est 1.66); tick719"),
    ("bud_sofico_immob_en_cours_2025", "sofico", 2025, 49646060, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Immobilisations en cours et acomptes 49.6m (69.2m 2024); tick719"),
    ("bud_sofico_leasing_net_2025", "sofico", 2025, 344996996, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Location-financement net 345.0m eoy2025; tick719"),
    ("bud_sofico_land_buildings_net_2025", "sofico", 2025, 2251384425, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Terrains constructions net 2.251bn eoy2025; tick719"),
    ("bud_sofico_land_acq_gross_2025", "sofico", 2025, 245773562, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Acquisitions terrains/constructions brut 245.8m 2025; tick719"),
    ("bud_sofico_amort_land_2025", "sofico", 2025, 158205078, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Amortissements terrains/constructions 158.2m 2025; tick719"),
    ("bud_sofico_net_debt_class_2025", "sofico", 2025, 283201121, "", "", "outturn", "src_sofico_comptes_2025_residual", "medium", "Net debt class banks+autres LT+ST due - cash: 298.1+169.5+27.2+12.5-224.6 = 282.7m class; tick719"),
    ("bud_sofico_reserves_indispo_2025", "sofico", 2025, 554180541, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Reserves indisponibles 554.2m (legal 28.6 + other 525.6); tick719"),
    ("bud_sofico_equity_path_2025", "sofico", 2025, 2305147846, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Equity 2.305bn eoy2025 path +130.8m vs 2.174bn 2024; tick719"),
    ("bud_sofico_cap_subs_bs_2025", "sofico", 2025, 309629431, "", "", "outturn", "src_sofico_comptes_2025_residual", "strong", "Subsides en capital BS 309.6m (290.6m 2024); tick719"),
    ("bud_dual_sofico_commit_awv_gip_2025", "gg_belgium", 2025, 280022174, "", "", "outturn", "src_dual_sofico_awv_gip_tick719", "strong", "Dual Sofico CAPEX commit 280m vs VL GIP exec residual; not TE-additive; tick719"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in budgets:
        w.writerow(r)
print("budgets +", len(budgets))

cmts = [
    (
        "cmt_sofico_capex_commit_280m_2025",
        "SOFICO CAPEX acquisition commitments encours 280m eoy2025 dual",
        "sofico",
        "Contractors structured network users",
        "SOFICO comptes annuels AG 24 Apr 2026 C-cap 6.14",
        "2025-12-31",
        2025,
        2027,
        280022174,
        '{"encours_acq_immob":280022174,"land_acq_2025":245773562,"immob_en_cours":49646060,"note":"off-balance purchase commitments"}',
        280022174,
        "active",
        "docs/doge/data/raw/sofico_comptes_2025.pdf",
        "Deliver structured network investment pipeline",
        "Publish named project L5 behind 280m FOI",
        "src_sofico_comptes_2025_residual",
        "strong",
        "Wallonie>SOFICO>capex_commit",
        "tick719",
    ),
    (
        "cmt_sofico_public_guaranteed_debt_495m",
        "SOFICO debt guaranteed by Belgian public authorities 495m",
        "sofico",
        "Walloon Region taxpayers banks",
        "Comptes 2025 dettes garanties pouvoirs publics",
        "2025-12-31",
        2025,
        2035,
        494762474,
        '{"guaranteed_total":494762474,"banks_lt_class":325262474,"autres_emprunts":169500000,"note":"prior year comparative in table"}',
        0,
        "active",
        "docs/doge/data/raw/sofico_comptes_2025.pdf",
        "Finance infra via guaranteed debt + user fees",
        "Publish guarantee stock dual RW comptes FOI",
        "src_sofico_comptes_2025_residual",
        "strong",
        "Wallonie>SOFICO>guarantees",
        "tick719",
    ),
    (
        "cmt_sofico_debt_maturity_ladder_2025",
        "SOFICO financial debt maturity ladder eoy2025 dual residual",
        "sofico",
        "Creditors RW",
        "Comptes 2025 C-cap 6.9 debt schedule",
        "2025-12-31",
        2025,
        2035,
        494762474,
        '{"due_1y":27185439,"y1_5":154435459,"gt5y":313170176,"lt_banks":298077035,"lt_autres":169500000,"st_autres":12500000,"cash":224561353}',
        0,
        "active",
        "docs/doge/data/raw/sofico_comptes_2025.pdf",
        "Match debt service to PKPL and subsidies",
        "Open multi-year amortisation FOI",
        "src_sofico_comptes_2025_residual",
        "strong",
        "Wallonie>SOFICO>debt_ladder",
        "tick719",
    ),
    (
        "cmt_sofico_cap_subs_path_2025",
        "SOFICO capital subsidies BS 310m + P&L 14m dual residual",
        "sofico",
        "RW structured network",
        "Comptes 2025 equity and financial income notes",
        "2025-01-01",
        2024,
        2025,
        309629431,
        '{"bs_2025":309629431,"bs_2024":290570362,"pnl_2025":14029440,"pnl_2024":11853616}',
        0,
        "active",
        "docs/doge/data/raw/sofico_comptes_2025.pdf",
        "Region capital support of concession model",
        "Reconcile RW budget capital grants FOI",
        "src_sofico_comptes_2025_residual",
        "strong",
        "Wallonie>SOFICO>capital_subsidies",
        "tick719",
    ),
    (
        "cmt_sofico_lean_staff_49_5_fte",
        "SOFICO lean staff 49.5 FTE on 3bn assets dual residual",
        "sofico",
        "Infra managers",
        "Comptes 2025 social balance C-cap 6.10",
        "2025-01-01",
        2025,
        2025,
        6278980,
        '{"fte":49.5,"headcount":51,"hours":68632,"remun_direct":4016436,"er_ss":1103585,"extralegal":842470,"personnel_total":6278980,"assets_bn":3.017}',
        0,
        "active",
        "docs/doge/data/raw/sofico_comptes_2025.pdf",
        "Run concession with thin HQ staff",
        "Dual unit cost vs AWV staff FOI",
        "src_sofico_comptes_2025_residual",
        "strong",
        "Wallonie>SOFICO>staff",
        "tick719",
    ),
    (
        "cmt_dual_sofico_awv_gip_tick719",
        "Dual SOFICO CAPEX commit vs VL GIP/AWV residual",
        "gg_belgium",
        "Entity II road users",
        "Sofico comptes 2025 + prior GIP CoA",
        "2025-01-01",
        2025,
        2026,
        280022174,
        '{"sofico_commit_m":280.0,"sofico_ca_m":502.8,"sofico_guaranteed_debt_m":494.8,"vl_gip_avg_m":2503,"note":"not TE-additive"}',
        0,
        "active",
        "docs/doge/data/raw/sofico_comptes_2025.pdf",
        "Comparable regional road invest transparency",
        "Named dual project L5 FOI",
        "src_dual_sofico_awv_gip_tick719",
        "strong",
        "Belgium>dual>SOFICO_GIP",
        "tick719",
    ),
]

with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in cmts:
        w.writerow(r)
print("commitments +", len(cmts))

lbs = [
    (
        "lb_sofico_capex_commit_280m",
        "SOFICO off-balance CAPEX commitments 280m eoy2025",
        "Wallonia",
        "ops",
        "Wallonie>SOFICO>capex_commit",
        280022174,
        280022174,
        "Strong comptes: engagements acquisition immobilisations 280.0m eoy2025; dual GIP opacity contrast",
        "strong",
        "src_sofico_comptes_2025_residual",
        "Road network users contractors",
        "Multi-year structural network delivery",
        "Large pipeline not in annual spend only; L5 names residual",
        6.5,
        8.0,
        4,
        6.95,
        "Publish named project list behind 280m FOI",
        "seed",
        "",
        "tick719",
    ),
    (
        "lb_sofico_guaranteed_debt_495m",
        "SOFICO public-guaranteed debt stock 495m eoy2025",
        "Wallonia",
        "ops",
        "Wallonie>SOFICO>guarantees",
        494762474,
        494762474,
        "Strong comptes: 494.8m debts guaranteed by Belgian public authorities; contingent RW risk",
        "strong",
        "src_sofico_comptes_2025_residual",
        "Walloon taxpayers",
        "Backstop concession finance",
        "Core infra guarantee not pure waste; contingent fiscal risk",
        5.5,
        8.0,
        5,
        6.35,
        "Publish guarantee terms dual RW debt FOI",
        "seed",
        "",
        "tick719",
    ),
    (
        "lb_sofico_lean_3bn_49fte",
        "SOFICO 3.0bn assets with only 49.5 FTE dual residual",
        "Wallonia",
        "ops",
        "Wallonie>SOFICO>lean_staff",
        6278980,
        3016660912,
        "Strong: personnel 6.28m FTE 49.5 on 3.017bn assets; lean HQ vs AWV model dual",
        "strong",
        "src_sofico_comptes_2025_residual",
        "Taxpayers road users",
        "Efficient concession vehicle",
        "Low staff cost class; works via contractors/SPW; dual compare",
        3.5,
        6.5,
        4,
        5.05,
        "Dual unit-cost staff+contractors vs AWV FOI",
        "seed",
        "",
        "tick719",
    ),
    (
        "lb_sofico_vat_throughput_203m",
        "SOFICO VAT charged 203m deductible 113m throughput",
        "Wallonia",
        "ops",
        "Wallonie>SOFICO>VAT",
        203308116,
        203308116,
        "Strong comptes: VAT charged 203.3m deductible 113.3m; large cash throughput",
        "strong",
        "src_sofico_comptes_2025_residual",
        "VAT chain contractors",
        "Correct VAT on infra works",
        "Not waste; marks scale of works billing",
        3.0,
        7.0,
        3,
        4.85,
        "Track vs invest outturn FOI",
        "seed",
        "",
        "tick719",
    ),
    (
        "lb_sofico_cap_subs_14m_pnl",
        "SOFICO capital subsidies 14m to P&L + 310m BS stock",
        "Wallonia",
        "subsidy",
        "Wallonie>SOFICO>cap_subs",
        14029440,
        309629431,
        "Strong: P&L capital subsidy income 14.03m; BS capital subsidies 309.6m path +19m",
        "strong",
        "src_sofico_comptes_2025_residual",
        "Region / Sofico",
        "Capitalise concession assets",
        "Subsidy stream dual RW budget recon residual",
        5.0,
        6.5,
        4,
        5.55,
        "1-to-1 RW capital grant map FOI",
        "seed",
        "",
        "tick719",
    ),
    (
        "lb_sofico_suppliers_139m",
        "SOFICO suppliers payable 139m eoy2025 dual residual",
        "Wallonia",
        "ops",
        "Wallonie>SOFICO>suppliers",
        139328459,
        139328459,
        "Strong: fournisseurs ST 139.3m; working capital on works pipeline",
        "strong",
        "src_sofico_comptes_2025_residual",
        "Contractors",
        "Pay works invoices",
        "Liquidity timing not pure waste",
        3.5,
        6.5,
        3,
        5.05,
        "Ageing analysis FOI",
        "seed",
        "",
        "tick719",
    ),
    (
        "lb_dual_sofico_gip_commit_2025",
        "Dual Sofico 280m CAPEX commit vs VL GIP residual",
        "Belgium",
        "ops",
        "Belgium>dual>SOFICO_GIP_commit",
        280022174,
        0,
        "Strong dual: WAL Sofico publishable commit 280m vs VL GIP no public VEK/encours; not TE-additive",
        "strong",
        "src_dual_sofico_awv_gip_tick719",
        "Entity II road users",
        "Comparable multi-year invest transparency",
        "Asymmetric disclosure dual",
        7.0,
        7.5,
        5,
        6.95,
        "Force dual open CAPEX commit dashboards",
        "seed",
        "",
        "tick719",
    ),
]

with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in lbs:
        w.writerow(r)
print("leaderboard +", len(lbs))

srcs = [
    (
        "src_sofico_comptes_2025_residual",
        "SOFICO comptes 2025 residual CAPEX commit debt ladder guarantees dual",
        "docs/doge/data/raw/sofico_comptes_2025.pdf",
        "SOFICO / NBB deposit AG 24 Apr 2026",
        "2026-08-01",
        "statutory_accounts",
        "Strong primary C-cap 6.9-6.14 residual tick719",
    ),
    (
        "src_dual_sofico_awv_gip_tick719",
        "Dual SOFICO CAPEX commit residual vs VL GIP/AWV",
        "docs/doge/data/raw/sofico_comptes_2025.pdf",
        "DOGE synthesis dual",
        "2026-08-01",
        "synthesis",
        "Strong dual Entity II roads tick719",
    ),
]

with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    for r in srcs:
        w.writerow(r)
print("sources +", len(srcs))

foi = (
    "gap_sofico_capex_commit_l5_2025",
    "Wallonie>SOFICO>capex_commit_L5",
    "sofico",
    "Named project/contractor L5 behind encours engagements acquisition immobilisations EUR 280.022m eoy2025; maturity schedule of guaranteed debt 494.8m; reconciliation RW capital subsidies to BS 309.6m and P&L 14.0m; dual unit-cost vs AWV/GIP",
    "280m off-balance CAPEX commit is material WAL invest pipeline; dual GIP lacks public encours; FOI-ready",
    "5",
    "SOFICO / SPW Mobilite Infrastructures / service transparence",
    "transparence@spw.wallonie.be",
    "",
    "docs/doge/foi/drafts/gap_sofico_capex_commit_l5_2025.md",
    "ready",
    "2026-08-01",
    "",
    "",
    "",
    "",
    "cmt_sofico_capex_commit_280m_2025",
    "lb_sofico_capex_commit_280m",
    "2026-08-01T21:30:00Z",
    "2026-08-01T21:30:00Z",
    "tick719 Sofico residual; not sent",
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
        if row and row[0] == "rq_710":
            row[4] = "done"
            row[10] = "2026-08-01T21:30:00Z"
            row[11] = "tick719 Sofico CAPEX commit 280m guaranteed debt 495m dual GIP; FOI gap_sofico_capex_commit_l5_2025 ready"
        rows.append(row)
ids = {row[0] for row in rows if row}
if "rq_711" not in ids:
    rows.append(
        [
            "rq_711",
            "Continuous FOI-adjacent public hole-fill batch",
            "continuous",
            "5",
            "open",
            "L5",
            "gg_belgium",
            "Next residual: PROGRESS@720 next OR UAP/OTW L5 or fed VVPR primary recheck or VL kunst L5 names",
            "",
            "2026-08-01T21:30:00Z",
            "",
            "spawned tick719 after rq_710; progress@720 next tick",
        ]
    )
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerows(rows)
print("research_queue updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T21:30:00Z,rq_710,719,no,tick719 Sofico CAPEX commit residual dual GIP; next rq_711 PROGRESS@720; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")

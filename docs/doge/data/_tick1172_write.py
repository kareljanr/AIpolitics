# tick1172: AGB Maasmechelen JR2025 Entity II dual residual (liquidation path)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_maasmechelen_jr2025"
ENT = "agb_maasmechelen"
TICK = "tick1172"
UTC = "2026-08-08T03:30:00Z"
GAP = "gap_agb_maas_afm_neg_liquidation_sale_debt_l5"
URL = "https://www.maasmechelen.be/documenten-agb"

csv.field_size_limit(10_000_000)

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Maasmechelen Jaarrekening BBC 2025 (86p) afdruk 09.04.2026 vereffening path",
            URL,
            "AGB Maasmechelen / Gemeente Maasmechelen",
            "2026-08-08",
            "official_pdf",
            "Entity II dual residual; KBO 0882.009.815; Oud Klooster sale to city 1.625m "
            "AFM -0.779m early repay 2.029m fin debt 2.972m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Maasmechelen",
            "AGB Maasmechelen",
            "AGB Maasmechelen",
            "local_entity",
            "city_maasmechelen",
            "nl",
            URL,
            "secretariaat@maasmechelen.be",
            "Heirstraat 239 3630 Maasmechelen",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0882.009.815 NIS 73107; patrimonium AGB in vereffening; "
            "assets 3.908m (cash 1.415 + ST recv 2.493) MVA ZERO after Oud Klooster sale to city "
            "1.625m; equity FLIP 0.892m (was -0.870m); fin debt 2.972m DECLINE early repay 2.029m; "
            "AFM -0.779m NEG gecorr -0.579m NEG BBR 3.867m PnL +0.938m; capital inject 0.860m; "
            "Vereffenaars Tanja Imbornone Daan Deckers; FOI " + GAP,
        ]
    )

budgets = [
    ("bud_agbmaas_assets_2025", 3908158, "Assets balanstotaal YE2025 3.908m DROP from 5.997m"),
    ("bud_agbmaas_equity_2025", 891805, "Nettoactief YE2025 0.892m FLIP from NEG -0.870m"),
    ("bud_agbmaas_cum_pnl_2025", -2058195, "Gecumuleerd tekort YE2025 -2.058m (improved from -2.996m)"),
    ("bud_agbmaas_other_netto_2025", 2950000, "Overig nettoactief YE2025 2.950m JUMP from 2.090m"),
    ("bud_agbmaas_debt_total_2025", 3016353, "Schulden total YE2025 3.016m DROP from 6.866m"),
    ("bud_agbmaas_fin_debt_2025", 2971930, "Fin schulden T4 total YE2025 2.972m DECLINING"),
    ("bud_agbmaas_fin_debt_lt_2025", 2544668, "Fin schulden LT YE2025 2.545m"),
    ("bud_agbmaas_fin_debt_st_due_2025", 427262, "Fin schulden LT vervallend YE2025 0.427m"),
    ("bud_agbmaas_cash_2025", 1415027, "Liquide middelen YE2025 1.415m DROP from 3.976m"),
    ("bud_agbmaas_st_recv_2025", 2493131, "ST vorderingen YE2025 2.493m JUMP (sale/city)"),
    ("bud_agbmaas_mva_2025", 0, "MVA YE2025 ZERO after Oud Klooster sale to city"),
    ("bud_agbmaas_expl_rec_2025", 271076, "Exploitatieontvangsten 0.271m"),
    ("bud_agbmaas_expl_exp_2025", 397646, "Exploitatieuitgaven 0.398m"),
    ("bud_agbmaas_expl_saldo_2025", -126571, "Exploitatiesaldo -0.127m NEG"),
    ("bud_agbmaas_desinvest_2025", 1624500, "Desinvestering/sale Oud Klooster to city 1.625m"),
    ("bud_agbmaas_invest_exp_2025", 6376, "Investeringsuitgaven 0.006m residual"),
    ("bud_agbmaas_invest_saldo_2025", 1618124, "Investeringssaldo +1.618m (sale driven)"),
    ("bud_agbmaas_fin_exp_2025", 2681155, "Financieringsuitgaven 2.681m (amort 0.652 + early 2.029)"),
    ("bud_agbmaas_early_repay_2025", 2029093, "Vervroegde terugbetaling leningen 2.029m"),
    ("bud_agbmaas_repay_2025", 652062, "Periodieke aflossingen 0.652m"),
    ("bud_agbmaas_capital_inject_2025", 860000, "Kapitaalsvermeerdering 0.860m"),
    ("bud_agbmaas_fin_saldo_2025", -1821155, "Financieringssaldo -1.821m"),
    ("bud_agbmaas_budget_result_2025", -329602, "Budgettair resultaat boekjaar -0.330m"),
    ("bud_agbmaas_bbr_2025", 3867432, "Beschikbaar BBR YE2025 3.867m"),
    ("bud_agbmaas_afm_2025", -778633, "AFM -0.779m NEG DEEP"),
    ("bud_agbmaas_afm_gecorr_2025", -578817, "Gecorr AFM -0.579m NEG (aangewezen 0.452m)"),
    ("bud_agbmaas_pnl_2025", 937861, "P&L +0.938m (sale path; minderwaarde 0.101m)"),
    ("bud_agbmaas_minderwaarde_2025", 101220, "Minderwaarde realisatie vaste activa 0.101m"),
    ("bud_agbmaas_interest_2025", 173742, "Intresten op leningen kengetal 0.174m"),
    ("bud_agbmaas_fin_costs_2025", 362786, "Financiele kosten J5 0.363m"),
    ("bud_agbmaas_other_op_rec_2025", 1436728, "Andere operationele opbrengsten J5 1.437m"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbmaas_afm_neg_0_78m_2025",
        "AGB Maasmechelen AFM -0.78m NEG DEEP",
        "Expl -0.127m << amort 0.652m; liquidation residual dual",
        778633,
    ),
    (
        "comm_agbmaas_sale_oud_klooster_1_62m_2025",
        "AGB Maasmechelen Oud Klooster sale to city 1.62m",
        "MVA wiped YE2025; desinvest 1.625m city purchase; minderwaarde 0.101m",
        1624500,
    ),
    (
        "comm_agbmaas_early_repay_2_03m_2025",
        "AGB Maasmechelen early loan repay 2.03m",
        "Sale proceeds used to cut fin debt 5.65->2.97m",
        2029093,
    ),
    (
        "comm_agbmaas_fin_debt_2_97m_2025",
        "AGB Maasmechelen fin debt 2.97m residual",
        "Post-sale residual bank debt; ST due 0.427m",
        2971930,
    ),
    (
        "comm_agbmaas_equity_flip_0_89m_2025",
        "AGB Maasmechelen equity FLIP to +0.89m",
        "Was NEG -0.87m YE2024; capital inject 0.86m + PnL sale",
        891805,
    ),
    (
        "comm_agbmaas_st_recv_jump_2_49m_2025",
        "AGB Maasmechelen ST recv JUMP 2.49m",
        "Cash DROP 3.98->1.42m while ST recv JUMP - city settlement residual",
        2493131,
    ),
]
with open(ROOT / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for cid, title, goal, env in cmts:
        w.writerow(
            [
                cid,
                title,
                ENT,
                "AGB dual residual",
                "BBC JR2025",
                "2026-04-09",
                2025,
                2025,
                env,
                f"{{2025:{env}}}",
                0,
                "active",
                URL,
                goal,
                "Entity II FOI residual",
                SRC,
                "strong",
                "Vlaanderen>Gemeenten>Maasmechelen>AGB",
                TICK,
            ]
        )

lbs = [
    ("lb_agbmaas_afm_neg_0_78m_2025", "AGB Maasmechelen AFM -0.78m NEG DEEP", 778633, 8.5, 5.5, 3.0, "AFM FOI residual"),
    ("lb_agbmaas_sale_1_62m_2025", "AGB Maasmechelen Oud Klooster sale 1.62m", 1624500, 7.5, 6.0, 3.0, "Sale FOI residual"),
    ("lb_agbmaas_early_repay_2_03m_2025", "AGB Maasmechelen early repay 2.03m", 2029093, 7.0, 6.5, 3.0, "Debt FOI residual"),
    ("lb_agbmaas_fin_debt_2_97m_2025", "AGB Maasmechelen fin debt 2.97m residual", 2971930, 7.0, 6.5, 3.0, "Debt FOI residual"),
    ("lb_agbmaas_equity_flip_0_89m_2025", "AGB Maasmechelen equity FLIP +0.89m", 891805, 8.0, 5.5, 3.0, "Capital FOI residual"),
    ("lb_agbmaas_gecorr_afm_neg_0_58m_2025", "AGB Maasmechelen gecorr AFM -0.58m NEG", 578817, 8.5, 5.0, 3.0, "AFM path FOI"),
    ("lb_agbmaas_st_recv_2_49m_2025", "AGB Maasmechelen ST recv JUMP 2.49m", 2493131, 7.5, 6.5, 3.0, "Receivable FOI residual"),
    ("lb_agbmaas_capital_inject_0_86m_2025", "AGB Maasmechelen capital inject 0.86m", 860000, 7.0, 5.5, 3.0, "Inject FOI residual"),
]
with open(ROOT / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for lid, name, cost, abs_s, cost_s, diff, cut in lbs:
        prio = round((abs_s * cost_s * (10 - diff)) / 10.0, 1)
        w.writerow(
            [
                lid,
                name,
                "L5",
                "local_budget_line",
                "Vlaanderen>Gemeenten>Maasmechelen>AGB_L5",
                cost,
                cost,
                "JR2025 Entity II dual residual VL strong primary BBC liquidation sale AFM NEG",
                "strong",
                SRC,
                "Maasmechelen residents / city dual",
                "Local dual residual map VL JR2025 AGB Maasmechelen",
                "BBC J2/J4/J5/T2/T4 primary",
                abs_s,
                cost_s,
                diff,
                prio,
                cut,
                "active",
                "",
                TICK,
            ]
        )

with open(ROOT / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            GAP,
            "Vlaanderen>Gemeenten>Maasmechelen>AGB>liquidation_sale_debt_L5",
            ENT,
            "Liquidation timeline and final accounts path (vereffenaars); Oud Klooster sale contract "
            "to city EUR1.6245m valuation and minderwaarde EUR0.101m; residual fin debt EUR2.972m "
            "lender schedule after early repay EUR2.029m; ST recv JUMP EUR2.493m counterparties "
            "(city settlement); capital inject EUR0.860m decision; AFM -0.779m multi-year to wind-up; "
            "cash DROP 3.976->1.415m treasury plan; off-BS rights after MVA wipe",
            "Entity II patrimonium AGB dual residual in liquidation: AFM DEEP NEG while equity flips "
            "via city purchase of remaining building and capital inject - material dual after city GE tick1060",
            9,
            "Gemeente / AGB Maasmechelen (vereffenaars)",
            "secretariaat@maasmechelen.be",
            "Heirstraat 239 3630 Maasmechelen",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-08",
            "",
            "",
            "",
            "",
            "comm_agbmaas_afm_neg_0_78m_2025|comm_agbmaas_sale_oud_klooster_1_62m_2025",
            "lb_agbmaas_afm_neg_0_78m_2025|lb_agbmaas_sale_1_62m_2025|lb_agbmaas_early_repay_2_03m_2025",
            UTC,
            UTC,
            TICK + "; ready not sent; do not send without human OK",
        ]
    )

rows = []
with open(ROOT / "research_queue.csv", "r", encoding="utf-8", errors="replace", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_1172":
            row["status"] = "done"
            row["entity_id"] = ENT
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick1172 AGB Maasmechelen JR2025 Entity II dual residual; liquidation Oud Klooster "
                "sale 1.62m AFM NEG early repay 2.03m; FOI " + GAP
            )
        rows.append(row)
if not any(r["task_id"] == "rq_1173" for r in rows):
    rows.append(
        {
            "task_id": "rq_1173",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "Vlaanderen>Gemeenten>residual_dual_L5",
            "entity_id": "",
            "instructions": "Residual dual L5 VL JR2025 (GE/OCMW + AGB). Prefer unmined AGB after city GE. Primary BBC only.",
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned by tick1172; next residual dual L5 after AGB Maasmechelen",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print("tick1172 write OK", len(budgets), "budgets", len(cmts), "cmts", len(lbs), "lbs")

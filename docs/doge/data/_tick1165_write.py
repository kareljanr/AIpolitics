# tick1165: AGB Begijnendijk JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_begijnendijk_jr2025"
ENT = "agb_begijnendijk"
TICK = "tick1165"
UTC = "2026-08-08T00:00:00Z"
GAP = "gap_agb_begijnendijk_afm_neg_prijssub_thin_equity_l5"

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Begijnendijk Jaarrekening BBC 2025 RVB vaststelling 18.06.2026",
            "https://www.begijnendijk.be/vaststellen-bbc-jaarrekening-2025-agb",
            "AGB Begijnendijk / Gemeente Begijnendijk",
            "2026-08-08",
            "official_pdf",
            "Entity II dual residual sport; KBO 0692.794.883; AFM -0.0003m gecorr -0.001m "
            "prijssub 0.057m assets 0.073m fin debt 0.052m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Begijnendijk",
            "AGB Begijnendijk",
            "AGB Begijnendijk",
            "local_entity",
            "city_begijnendijk",
            "nl",
            "https://www.begijnendijk.be/vaststellen-bbc-jaarrekening-2025-agb",
            "beleid@begijnendijk.be",
            "Kerkplein 5 3130 Begijnendijk",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0692.794.883; sportcomplex Grote Baan/Tumkens; assets 0.073m equity 0.007m "
            "cash 0.052m fin debt 0.052m MVA only 0.004m AFM -0.0003m NEG gecorr -0.001m NEG "
            "prijssub 0.057m BBR 0.049m; AD Peggy Baeten FD Didier Dascotte Voorzitter Bob Michiels; FOI "
            + GAP,
        ]
    )

budgets = [
    ("bud_agbbeg_assets_2025", 73474, "Assets balanstotaal YE2025 0.073m"),
    ("bud_agbbeg_equity_2025", 6559, "Nettoactief YE2025 0.007m thin (cum P&L only)"),
    ("bud_agbbeg_debt_total_2025", 66915, "Schulden total YE2025 0.067m"),
    ("bud_agbbeg_fin_debt_2025", 52241, "Fin schulden T4 total YE2025 0.052m (LT 0.049 + ST due 0.004)"),
    ("bud_agbbeg_fin_debt_lt_2025", 48717, "Fin schulden LT YE2025 0.049m"),
    ("bud_agbbeg_fin_debt_st_due_2025", 3524, "Fin schulden LT vervallend YE2025 0.004m"),
    ("bud_agbbeg_cash_2025", 51917, "Liquide middelen YE2025 0.052m"),
    ("bud_agbbeg_mva_2025", 3741, "MVA bedrijfsmatig YE2025 0.004m only (equipment; plant not on AGB BS)"),
    ("bud_agbbeg_expl_rec_2025", 139562, "Exploitatieontvangsten 0.140m"),
    ("bud_agbbeg_expl_exp_2025", 136351, "Exploitatieuitgaven 0.136m"),
    ("bud_agbbeg_expl_saldo_2025", 3211, "Exploitatiesaldo +0.003m"),
    ("bud_agbbeg_prijssub_2025", 56637, "Prijssubsidie gemeente 0.057m (~41pct of expl rec)"),
    ("bud_agbbeg_invest_exp_2025", 0, "Investeringsuitgaven 0 (MJP 0.012m underspend)"),
    ("bud_agbbeg_fin_rec_2025", 3500, "Financieringsontvangsten/new loans 0.004m"),
    ("bud_agbbeg_fin_exp_2025", 3524, "Periodieke aflossingen 0.004m"),
    ("bud_agbbeg_fin_saldo_2025", -24, "Financieringssaldo -0.000m"),
    ("bud_agbbeg_new_loans_2025", 3500, "Nieuwe leningen T4 0.004m"),
    ("bud_agbbeg_aflossingen_2025", 3524, "Aflossingen T4 0.004m"),
    ("bud_agbbeg_budget_result_2025", 3187, "Budgettair resultaat boekjaar +0.003m"),
    ("bud_agbbeg_bbr_2025", 49348, "BBR 0.049m"),
    ("bud_agbbeg_afm_2025", -313, "AFM -0.0003m NEG"),
    ("bud_agbbeg_afm_gecorr_2025", -970, "Gecorr AFM -0.001m NEG (aangewezen 0.004m)"),
    ("bud_agbbeg_pnl_2025", 3399, "P&L +0.003m"),
    ("bud_agbbeg_dividend_2025", 850, "Dividend to city 0.001m (partial of PnL)"),
    ("bud_agbbeg_interest_2025", 124, "Financiele kosten 0.0001m"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbbeg_afm_neg_2025",
        "AGB Begijnendijk AFM -313 NEG",
        "AFM NEG thin; gecorr AFM -970; expl barely covers debt service",
        313,
    ),
    (
        "comm_agbbeg_prijssub_0_057m_2025",
        "AGB Begijnendijk prijssub 0.057m",
        "City price subsidy ~41pct of expl revenue; sport shell dependent",
        56637,
    ),
    (
        "comm_agbbeg_fin_debt_0_052m_2025",
        "AGB Begijnendijk fin debt 0.052m",
        "Small debt stock; amort 3.5k/yr; new 3.5k",
        52241,
    ),
    (
        "comm_agbbeg_mva_thin_plant_off_bs_2025",
        "AGB Begijnendijk MVA only 0.004m plant FOI",
        "Sport plant largely not on AGB balance sheet; ownership/lease FOI",
        3741,
    ),
]
with open(ROOT / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for cid, title, goal, total in cmts:
        w.writerow(
            [
                cid,
                title,
                ENT,
                "AGB Begijnendijk / residents",
                "BBC JR2025 / DLB AGB",
                "2026-06-18",
                2025,
                2025,
                total,
                f'{{"2025":{total}}}',
                total,
                "active",
                "",
                goal,
                "FOI residual dual; review AFM/prijssub/plant",
                SRC,
                "strong",
                "Vlaanderen>Gemeenten>Begijnendijk>AGB_Begijnendijk_L5",
                TICK,
            ]
        )

lbs = [
    ("lb_agbbeg_afm_neg_2025", "AGB Begijnendijk AFM -313 NEG", 313, 8.0, 1.5, 2.0, 4.3, "AFM FOI residual"),
    ("lb_agbbeg_gecorr_afm_neg_2025", "AGB Begijnendijk gecorr AFM -970 NEG", 970, 8.0, 1.5, 2.0, 4.3, "AFM FOI residual"),
    ("lb_agbbeg_prijssub_0_057m_2025", "AGB Begijnendijk prijssub 0.057m ~41pct", 56637, 7.5, 3.0, 2.0, 4.6, "Prijssub FOI residual"),
    ("lb_agbbeg_fin_debt_0_052m_2025", "AGB Begijnendijk fin debt 0.052m", 52241, 5.5, 3.0, 2.0, 3.7, "Debt FOI residual"),
    ("lb_agbbeg_assets_0_073m_2025", "AGB Begijnendijk assets 0.073m Entity II", 73474, 5.0, 3.0, 2.0, 3.5, "Map residual shell"),
    ("lb_agbbeg_mva_thin_plant_off_bs_2025", "AGB Begijnendijk MVA 0.004m plant FOI", 3741, 7.0, 1.5, 2.0, 3.9, "Plant ownership FOI"),
]
tco = "JR2025 Entity II dual residual VL strong primary BBC small sport AGB AFM NEG/prijssub Begijnendijk"
with open(ROOT / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for iid, name, cost, absu, cost_s, diff, prio, cut in lbs:
        w.writerow(
            [
                iid,
                name,
                "L5",
                "local_budget_line",
                "Vlaanderen>Gemeenten>Begijnendijk>AGB_Begijnendijk_L5",
                cost,
                cost,
                tco,
                "strong",
                SRC,
                "Begijnendijk residents",
                "Local dual residual map VL JR2025 AGB Begijnendijk",
                "BBC J2/J4/J5 primary",
                absu,
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
            "Vlaanderen>Gemeenten>Begijnendijk>AGB_Begijnendijk>afm_neg_prijssub_plant_L5",
            ENT,
            "AFM -313 and gecorr AFM -970 multi-year path; prijssubsidie 56.637 formula (~41pct of expl rec); "
            "why MVA only 3.741 vs sport plant Grote Baan/Tumkens (ownership city vs AGB lease); "
            "fin debt 52.241 schedule lender; invest underspend MJP 12k vs 0; dividend 850 of PnL 3399 policy; "
            "vzw Vossekot interface",
            "Entity II dual residual: small sport AGB with NEG AFM and high city prijs subsidy share; "
            "plant largely off AGB BS after city GE already mined",
            7,
            "Gemeente / AGB Begijnendijk",
            "beleid@begijnendijk.be",
            "Kerkplein 5 3130 Begijnendijk",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-08",
            "",
            "",
            "",
            "",
            "comm_agbbeg_afm_neg_2025",
            "lb_agbbeg_afm_neg_2025",
            UTC,
            UTC,
            TICK + "; ready not sent; do not send without human OK",
        ]
    )

csv.field_size_limit(10_000_000)
rows = []
with open(ROOT / "research_queue.csv", encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_1165":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                (row.get("notes") or "")
                + f" | {TICK} AGB Begijnendijk JR2025 dual residual full BBC; FOI {GAP}"
            )
            row["entity_id"] = ENT
            row["hierarchy_target"] = "Vlaanderen>Gemeenten>Begijnendijk>AGB_Begijnendijk"
        rows.append(row)
ids = {row["task_id"] for row in rows}
if "rq_1166" not in ids:
    rows.append(
        {
            "task_id": "rq_1166",
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
            "notes": f"spawned by {TICK}; next residual dual L5 after AGB Begijnendijk",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

print("budgets", len(budgets), "cmts", len(cmts), "lbs", len(lbs), "OK")

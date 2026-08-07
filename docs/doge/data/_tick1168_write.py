# tick1168: AGB Aarschot JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_aarschot_jr2025"
ENT = "agb_aarschot"
TICK = "tick1168"
UTC = "2026-08-08T01:30:00Z"
GAP = "gap_agb_aarschot_gecorr_afm_neg_debt_11m_prijssub_leasing_l5"

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Aarschot Jaarrekening BBC 2025 (87p) bekendmaking 12.05.2026",
            "https://www.aarschot.be/jaarrekening-2025-agb",
            "AGB Aarschot / Stad Aarschot",
            "2026-08-08",
            "official_pdf",
            "Entity II dual residual; KBO 0881.848.972; fin debt 11.453m gecorr AFM -0.233m "
            "prijssub 1.320m leasing 1.911m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Aarschot",
            "AGB Aarschot",
            "AGB Aarschot",
            "local_entity",
            "city_aarschot",
            "nl",
            "https://www.aarschot.be/jaarrekening-2025-agb",
            "info@aarschot.be",
            "Ten Drossaarde 1 3200 Aarschot",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0881.848.972; assets 12.708m equity 0.425m cash 0.805m fin debt 11.453m "
            "DECLINING leasing MVA 1.911m prijssub 1.320m BBR 0.744m AFM +0.187m "
            "gecorr AFM -0.233m NEG early repay 0.724m; AD Christi Van Calster FD Geert Wijns; FOI "
            + GAP,
        ]
    )

budgets = [
    ("bud_agbaar_assets_2025", 12707689, "Assets balanstotaal YE2025 12.708m"),
    ("bud_agbaar_equity_2025", 424790, "Nettoactief YE2025 0.425m"),
    ("bud_agbaar_cum_pnl_2025", 346221, "Gecumuleerd overschot YE2025 0.346m"),
    ("bud_agbaar_cap_subs_2025", 72726, "Kapitaalssubsidies YE2025 0.073m"),
    ("bud_agbaar_debt_total_2025", 12282899, "Schulden total YE2025 12.283m"),
    ("bud_agbaar_fin_debt_2025", 11453196, "Fin schulden T4 total YE2025 11.453m DECLINING"),
    ("bud_agbaar_fin_debt_lt_2025", 10891504, "Fin schulden LT YE2025 10.892m"),
    ("bud_agbaar_fin_debt_st_due_2025", 561692, "Fin schulden LT vervallend YE2025 0.562m"),
    ("bud_agbaar_cash_2025", 804616, "Liquide middelen YE2025 0.805m JUMP from 0.489m"),
    ("bud_agbaar_mva_2025", 11368950, "MVA YE2025 11.369m"),
    ("bud_agbaar_mva_buildings_2025", 8044582, "MVA terreinen/gebouwen YE2025 8.045m"),
    ("bud_agbaar_leasing_mva_2025", 1910503, "Leasing MVA YE2025 1.911m"),
    ("bud_agbaar_st_nonruil_recv_2025", 169645, "ST vorderingen niet-ruil YE2025 0.170m JUMP from 0.005m"),
    ("bud_agbaar_expl_rec_2025", 3306799, "Exploitatieontvangsten 3.307m"),
    ("bud_agbaar_expl_exp_2025", 2564133, "Exploitatieuitgaven 2.564m"),
    ("bud_agbaar_expl_saldo_2025", 742666, "Exploitatiesaldo +0.743m"),
    ("bud_agbaar_prijssub_2025", 1319624, "Prijssubsidie gemeente 1.320m"),
    ("bud_agbaar_invest_exp_2025", 689214, "Investeringsuitgaven 0.689m"),
    ("bud_agbaar_invest_rec_2025", 896689, "Investeringsontvangsten/desinvest 0.897m"),
    ("bud_agbaar_invest_saldo_2025", 207474, "Investeringssaldo +0.207m"),
    ("bud_agbaar_fin_rec_2025", 541605, "Financieringsontvangsten/new loans 0.542m"),
    ("bud_agbaar_fin_exp_2025", 1279564, "Financieringsuitgaven 1.280m (amort 0.556 + early 0.724)"),
    ("bud_agbaar_fin_saldo_2025", -737959, "Financieringssaldo -0.738m"),
    ("bud_agbaar_new_loans_2025", 541605, "Nieuwe leningen T4 0.542m"),
    ("bud_agbaar_early_repay_2025", 723997, "Vervroegde terugbetaling leningen 0.724m"),
    ("bud_agbaar_aflossingen_2025", 555567, "Periodieke aflossingen 0.556m"),
    ("bud_agbaar_budget_result_2025", 212182, "Budgettair resultaat boekjaar +0.212m"),
    ("bud_agbaar_bbr_2025", 743742, "BBR 0.744m"),
    ("bud_agbaar_afm_2025", 187099, "AFM +0.187m"),
    ("bud_agbaar_afm_gecorr_2025", -232626, "Gecorr AFM -0.233m NEG CRITICAL (aangewezen 0.975m)"),
    ("bud_agbaar_pnl_2025", 103345, "P&L +0.103m"),
    ("bud_agbaar_dividend_2025", 25000, "Dividend to city 0.025m (partial of PnL)"),
    ("bud_agbaar_interest_2025", 2341, "Financiele kosten 0.002m thin"),
    ("bud_agbaar_depr_2025", 643761, "Afschrijvingen 0.644m"),
    ("bud_agbaar_mjp_debt_2026", 12976413, "MJP fin debt YE2026 path 12.976m (new 2.106m)"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbaar_gecorr_afm_neg_0_23m_2025",
        "AGB Aarschot gecorr AFM -0.23m NEG",
        "Indicated amort 0.975m >> contractual 0.556m; healthy AFM masks NEG gecorr",
        232626,
    ),
    (
        "comm_agbaar_fin_debt_11_45m_2025",
        "AGB Aarschot fin debt 11.45m declining",
        "LT 10.892 + ST due 0.562; early repay 0.724; new 0.542; MJP YE2026 12.98m",
        11453196,
    ),
    (
        "comm_agbaar_prijssub_1_32m_2025",
        "AGB Aarschot prijssub city 1.32m",
        "Large city price subsidy of expl rec 3.307m",
        1319624,
    ),
    (
        "comm_agbaar_leasing_mva_1_91m_2025",
        "AGB Aarschot leasing MVA 1.91m",
        "Leasing 1.911m of 11.369m MVA",
        1910503,
    ),
    (
        "comm_agbaar_early_repay_0_72m_2025",
        "AGB Aarschot early loan repay 0.72m",
        "Vervroegde terugbetaling 0.724m in financing outflows",
        723997,
    ),
    (
        "comm_agbaar_st_nonruil_jump_2025",
        "AGB Aarschot ST non-ruil recv jump 0.17m",
        "Non-ruil ST recv 0.005 to 0.170m FOI composition",
        169645,
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
                "AGB Aarschot / Stad Aarschot residents",
                "BBC JR2025 / DLB AGB",
                "2026-04-23",
                2025,
                2026,
                total,
                f'{{"2025":{total}}}',
                total,
                "active",
                "",
                goal,
                "FOI residual dual; review gecorr AFM/debt/prijssub",
                SRC,
                "strong",
                "Vlaanderen>Gemeenten>Aarschot>AGB_Aarschot_L5",
                TICK,
            ]
        )

lbs = [
    ("lb_agbaar_fin_debt_11_45m_2025", "AGB Aarschot fin debt 11.45m declining", 11453196, 8.0, 8.0, 3.0, 6.3, "Debt FOI residual"),
    ("lb_agbaar_prijssub_1_32m_2025", "AGB Aarschot prijssub city 1.32m", 1319624, 8.0, 7.0, 3.0, 6.0, "Prijssub FOI residual"),
    ("lb_agbaar_gecorr_afm_neg_0_23m_2025", "AGB Aarschot gecorr AFM -0.23m NEG", 232626, 8.5, 4.0, 3.0, 5.2, "AFM FOI residual CRITICAL"),
    ("lb_agbaar_leasing_mva_1_91m_2025", "AGB Aarschot leasing MVA 1.91m", 1910503, 7.5, 6.5, 3.0, 5.7, "Leasing FOI residual"),
    ("lb_agbaar_assets_12_71m_2025", "AGB Aarschot assets 12.71m Entity II", 12707689, 6.0, 8.0, 3.0, 5.7, "Map residual shell"),
    ("lb_agbaar_early_repay_0_72m_2025", "AGB Aarschot early repay 0.72m", 723997, 7.0, 5.5, 3.0, 5.1, "Debt FOI residual"),
    ("lb_agbaar_st_nonruil_jump_0_17m_2025", "AGB Aarschot ST non-ruil jump 0.17m", 169645, 7.0, 4.0, 3.0, 4.7, "Recv FOI residual"),
]
tco = "JR2025 Entity II dual residual VL strong primary BBC gecorr AFM NEG debt/prijssub AGB Aarschot"
with open(ROOT / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for iid, name, cost, absu, cost_s, diff, prio, cut in lbs:
        w.writerow(
            [
                iid,
                name,
                "L5",
                "local_budget_line",
                "Vlaanderen>Gemeenten>Aarschot>AGB_Aarschot_L5",
                cost,
                cost,
                tco,
                "strong",
                SRC,
                "Aarschot residents",
                "Local dual residual map VL JR2025 AGB Aarschot",
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
            "Vlaanderen>Gemeenten>Aarschot>AGB_Aarschot>gecorr_afm_debt_prijssub_leasing_L5",
            ENT,
            "Gecorr AFM -0.233m path (aangewezen 0.975m vs contractual 0.556m); fin debt schedule 11.453m "
            "(LT 10.892 ST due 0.562 new 0.542 early repay 0.724 lenders); MJP YE2026 debt 12.976m +2.106m; "
            "prijssubsidie 1.320m formula multi-year; leasing MVA 1.911m residual; ST non-ruil recv jump "
            "0.005 to 0.170m composition; desinvest 0.897m nature",
            "Entity II dual residual: multi-purpose AGB with 11.5m debt, 1.32m city prijssub, leasing shell "
            "and NEG gecorr AFM despite healthy AFM/BBR after city GE already mined",
            9,
            "Stad / AGB Aarschot",
            "info@aarschot.be",
            "Ten Drossaarde 1 3200 Aarschot",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-08",
            "",
            "",
            "",
            "",
            "comm_agbaar_gecorr_afm_neg_0_23m_2025",
            "lb_agbaar_fin_debt_11_45m_2025",
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
        if row["task_id"] == "rq_1168":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                (row.get("notes") or "")
                + f" | {TICK} AGB Aarschot JR2025 dual residual full BBC; FOI {GAP}"
            )
            row["entity_id"] = ENT
            row["hierarchy_target"] = "Vlaanderen>Gemeenten>Aarschot>AGB_Aarschot"
        rows.append(row)
ids = {row["task_id"] for row in rows}
if "rq_1169" not in ids:
    rows.append(
        {
            "task_id": "rq_1169",
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
            "notes": f"spawned by {TICK}; next residual dual L5 after AGB Aarschot",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

print("budgets", len(budgets), "cmts", len(cmts), "lbs", len(lbs), "OK")

# tick1175: AGB Sport Geel JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_geel_sport_jr2025"
ENT = "agb_geel_sport"
TICK = "tick1175"
UTC = "2026-08-08T05:00:00Z"
GAP = "gap_agb_geel_afm_neg_gecorr_deep_cash_drop_debt_16m_l5"
URL = "https://www.geel.be/jaarrekening-agb-sport"

csv.field_size_limit(10_000_000)

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Sport Geel Jaarrekening BBC 2025 financiele nota (10p) pub 30.06.2026",
            URL,
            "AGB Sport Geel / Stad Geel",
            "2026-08-08",
            "official_pdf",
            "Entity II dual residual; KBO 0876.030.556; assets 18.638m fin debt 16.406m "
            "AFM -0.090m gecorr -0.450m cash DROP 1.69->0.59m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Sport Geel",
            "AGB Sport Geel",
            "AGB Sport Geel",
            "local_entity",
            "city_geel",
            "nl",
            URL,
            "financien@geel.be",
            "Werft 20 2440 Geel",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0876.030.556; assets 18.638m equity 1.629m cash 0.588m DROP from 1.686 "
            "fin debt 16.406m (LT 15.412 + ST due 0.994) BBR 0.322m AFM -0.090m NEG "
            "gecorr AFM -0.450m NEG DEEP PnL +0.168m dividend 0.100m; Secr Francois Mylle "
            "FD Steven Lambrecht; FOI " + GAP,
        ]
    )

budgets = [
    ("bud_agbgeels_assets_2025", 18638158, "Assets balanstotaal YE2025 18.638m DROP from 20.015m"),
    ("bud_agbgeels_equity_2025", 1629339, "Nettoactief YE2025 1.629m"),
    ("bud_agbgeels_cum_pnl_2025", 504346, "Gecumuleerd overschot YE2025 0.504m"),
    ("bud_agbgeels_cap_subs_2025", 1124992, "Kapitaalssubsidies YE2025 1.125m"),
    ("bud_agbgeels_debt_total_2025", 17008819, "Schulden total YE2025 17.009m"),
    ("bud_agbgeels_fin_debt_2025", 16405918, "Fin schulden total YE2025 16.406m (LT+ST due)"),
    ("bud_agbgeels_fin_debt_lt_2025", 15411941, "Fin schulden LT YE2025 15.412m"),
    ("bud_agbgeels_fin_debt_st_due_2025", 993977, "Fin schulden LT vervallend YE2025 0.994m"),
    ("bud_agbgeels_cash_2025", 588176, "Liquide middelen YE2025 0.588m DROP CRITICAL from 1.686m"),
    ("bud_agbgeels_mva_2025", 17730462, "MVA YE2025 17.730m"),
    ("bud_agbgeels_mva_buildings_2025", 17442746, "MVA terreinen/gebouwen YE2025 17.443m"),
    ("bud_agbgeels_st_recv_2025", 259964, "ST vorderingen YE2025 0.260m"),
    ("bud_agbgeels_expl_rec_2025", 2552909, "Exploitatieontvangsten 2.553m"),
    ("bud_agbgeels_expl_exp_2025", 1664090, "Exploitatieuitgaven 1.664m"),
    ("bud_agbgeels_expl_saldo_2025", 888819, "Exploitatiesaldo +0.889m"),
    ("bud_agbgeels_omzet_werking_2025", 2684616, "Opbrengsten uit de werking J5 2.685m"),
    ("bud_agbgeels_invest_exp_2025", 652838, "Investeringsuitgaven 0.653m"),
    ("bud_agbgeels_new_loans_2025", 652838, "Nieuwe leningen/leasings 0.653m (= invest)"),
    ("bud_agbgeels_repay_2025", 978623, "Periodieke aflossingen 0.979m"),
    ("bud_agbgeels_fin_saldo_2025", -325785, "Financieringssaldo -0.326m"),
    ("bud_agbgeels_budget_result_2025", -89804, "Budgettair resultaat boekjaar -0.090m NEG"),
    ("bud_agbgeels_bbr_2025", 322481, "Beschikbaar BBR YE2025 0.322m"),
    ("bud_agbgeels_afm_2025", -89804, "AFM -0.090m NEG equals budget result"),
    ("bud_agbgeels_afm_gecorr_2025", -449717, "Gecorr AFM -0.450m NEG DEEP (aangewezen 1.339m)"),
    ("bud_agbgeels_aangewezen_amort_2025", 1338536, "Gecorrigeerde aflossingen o.b.v. fin schulden 1.339m"),
    ("bud_agbgeels_pnl_2025", 167515, "P&L +0.168m"),
    ("bud_agbgeels_dividend_2025", 100000, "Dividend to city 0.100m while AFM NEG"),
    ("bud_agbgeels_interest_2025", 181, "Financiele kosten 0.0002m thin"),
    ("bud_agbgeels_depr_2025", 1015902, "Afschrijvingen 1.016m"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbgeels_afm_neg_0_09m_2025",
        "AGB Sport Geel AFM -0.09m NEG",
        "Expl 0.889m < repay 0.979m; equals budget result NEG",
        89804,
    ),
    (
        "comm_agbgeels_gecorr_afm_neg_0_45m_2025",
        "AGB Sport Geel gecorr AFM -0.45m NEG DEEP",
        "Indicated amort 1.339m >> contractual 0.979m",
        449717,
    ),
    (
        "comm_agbgeels_fin_debt_16_4m_2025",
        "AGB Sport Geel fin debt 16.4m",
        "LT 15.4m + ST due 0.99m city/lease shell",
        16405918,
    ),
    (
        "comm_agbgeels_cash_drop_1_1m_2025",
        "AGB Sport Geel cash DROP 1.1m",
        "Cash 1.686->0.588m CRITICAL DROP residual",
        1097546,
    ),
    (
        "comm_agbgeels_div_while_afm_neg_2025",
        "AGB Sport Geel dividend 0.1m while AFM NEG",
        "Dividend despite NEG AFM/budget result",
        100000,
    ),
    (
        "comm_agbgeels_repay_0_98m_2025",
        "AGB Sport Geel repay 0.98m 2025",
        "Periodieke aflossingen exceed new loans 0.65m",
        978623,
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
                "2026-06-30",
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
                "Vlaanderen>Gemeenten>Geel>AGB_Sport",
                TICK,
            ]
        )

lbs = [
    ("lb_agbgeels_fin_debt_16_4m_2025", "AGB Sport Geel fin debt 16.4m", 16405918, 7.5, 7.5, 3.0, "Debt FOI residual"),
    ("lb_agbgeels_gecorr_afm_neg_0_45m_2025", "AGB Sport Geel gecorr AFM -0.45m NEG DEEP", 449717, 8.5, 5.0, 3.0, "AFM FOI residual"),
    ("lb_agbgeels_cash_drop_0_59m_2025", "AGB Sport Geel cash DROP to 0.59m", 588176, 8.5, 5.0, 3.0, "Treasury FOI residual"),
    ("lb_agbgeels_afm_neg_0_09m_2025", "AGB Sport Geel AFM -0.09m NEG", 89804, 8.0, 3.5, 3.0, "AFM FOI residual"),
    ("lb_agbgeels_assets_18_6m_2025", "AGB Sport Geel assets 18.6m Entity II", 18638158, 5.5, 7.5, 3.0, "Map residual"),
    ("lb_agbgeels_div_while_afm_neg_2025", "AGB Sport Geel dividend while AFM NEG", 100000, 8.5, 3.5, 3.0, "Dividend FOI residual"),
    ("lb_agbgeels_repay_0_98m_2025", "AGB Sport Geel repay 0.98m", 978623, 6.0, 5.5, 3.0, "Amort FOI residual"),
    ("lb_agbgeels_pnl_0_17m_2025", "AGB Sport Geel PnL +0.17m", 167515, 5.5, 4.0, 3.0, "Monitor residual"),
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
                "Vlaanderen>Gemeenten>Geel>AGB_Sport_L5",
                cost,
                cost,
                "JR2025 Entity II dual residual VL strong primary BBC AFM NEG gecorr DEEP cash DROP",
                "strong",
                SRC,
                "Geel residents / sport users",
                "Local dual residual map VL JR2025 AGB Sport Geel",
                "BBC J2/J4/J5 primary financiele nota",
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
            "Vlaanderen>Gemeenten>Geel>AGB_Sport>afm_cash_debt_L5",
            ENT,
            "AFM -0.090m and gecorr AFM -0.450m multi-year path (aangewezen amort 1.339m); "
            "fin debt 16.406m lender schedule city vs bank/lease; cash DROP 1.686->0.588m treasury "
            "plan; dividend 0.100m while AFM NEG legal basis; new loans 0.653m project list; "
            "ST due 0.994m wall; prijssubsidie/city transfer matrix in werking 2.685m",
            "Entity II sport AGB dual residual after city Geel GE tick848: EUR16.4m debt shell with "
            "NEG AFM, deep NEG gecorr AFM and critical cash drop - material dual ranking",
            9,
            "Stad / AGB Sport Geel",
            "financien@geel.be",
            "Werft 20 / Meuldersplein 29-30 2440 Geel",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-08",
            "",
            "",
            "",
            "",
            "comm_agbgeels_afm_neg_0_09m_2025|comm_agbgeels_gecorr_afm_neg_0_45m_2025",
            "lb_agbgeels_gecorr_afm_neg_0_45m_2025|lb_agbgeels_cash_drop_0_59m_2025|lb_agbgeels_fin_debt_16_4m_2025",
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
        if row["task_id"] == "rq_1175":
            row["status"] = "done"
            row["entity_id"] = ENT
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick1175 AGB Sport Geel JR2025 Entity II dual residual; AFM NEG gecorr -0.45m "
                "cash DROP debt 16.4m; FOI " + GAP
            )
        rows.append(row)
if not any(r["task_id"] == "rq_1176" for r in rows):
    rows.append(
        {
            "task_id": "rq_1176",
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
            "notes": "spawned by tick1175; next residual dual L5 after AGB Sport Geel",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print("tick1175 write OK", len(budgets), "budgets", len(cmts), "cmts", len(lbs), "lbs")

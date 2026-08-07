# tick1163: AGB Herzele JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_herzele_jr2025"
ENT = "agb_herzele"
TICK = "tick1163"
UTC = "2026-08-07T23:00:00Z"
GAP = "gap_agb_herzele_equity_thin_full_div_leasing_prijssub_l5"

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Herzele Jaarrekening BBC 2025 (70p) vaststelling 17.06.2026",
            "https://www.herzele.be/vaststelling-jaarverslag-en-jaarrekening-2025-bbc-en-nbb-van-het-agb-herzele",
            "AGB Herzele / Gemeente Herzele",
            "2026-08-07",
            "official_pdf",
            "Entity II dual residual culture/sport Steenoven; KBO 0875.059.665; equity thin 0.028m "
            "full div 0.052m leasing 1.667m prijssub 0.243m fin debt 1.817m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Herzele",
            "AGB Herzele",
            "AGB Herzele",
            "local_entity",
            "city_herzele",
            "nl",
            "https://www.herzele.be/vaststelling-jaarverslag-en-jaarrekening-2025-bbc-en-nbb-van-het-agb-herzele",
            "info@herzele.be",
            "Markt 20 9550 Herzele",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0875.059.665 NIS 41027; assets 2.224m equity 0.028m THIN cash 0.208m "
            "fin debt 1.817m leasing MVA 1.667m prijssub 0.243m BBR 0.214m AFM +0.006m "
            "gecorr +0.025m full dividend 0.052m=PnL; AD Daniel Adriaens FD Jan Hermans "
            "Voorzitter Benjamin Rogiers; FOI " + GAP,
        ]
    )

budgets = [
    ("bud_agbher_assets_2025", 2223824, "Assets balanstotaal YE2025 2.224m DROP from 3.021m"),
    ("bud_agbher_equity_2025", 27520, "Nettoactief YE2025 0.028m THIN CRITICAL flat"),
    ("bud_agbher_cum_pnl_2025", 2502, "Gecumuleerd overschot YE2025 0.0025m flat (full dividend)"),
    ("bud_agbher_debt_total_2025", 2196304, "Schulden total YE2025 2.196m"),
    ("bud_agbher_fin_debt_2025", 1816656, "Fin schulden T4 total YE2025 1.817m DECLINING"),
    ("bud_agbher_fin_debt_lt_2025", 1646951, "Fin schulden LT YE2025 1.647m"),
    ("bud_agbher_fin_debt_st_due_2025", 169705, "Fin schulden LT vervallend YE2025 0.170m"),
    ("bud_agbher_cash_2025", 208019, "Liquide middelen YE2025 0.208m JUMP from 0.060m"),
    ("bud_agbher_mva_2025", 1839164, "MVA bedrijfsmatig YE2025 1.839m"),
    ("bud_agbher_leasing_mva_2025", 1666568, "Leasing MVA YE2025 1.667m shell-heavy of MVA"),
    ("bud_agbher_st_nonruil_recv_2025", 86606, "ST vorderingen niet-ruil YE2025 0.087m DROP from 0.537m"),
    ("bud_agbher_st_recv_total_2025", 176641, "ST vorderingen total YE2025 0.177m DROP from 1.030m"),
    ("bud_agbher_expl_rec_2025", 757357, "Exploitatieontvangsten 0.757m"),
    ("bud_agbher_expl_exp_2025", 580150, "Exploitatieuitgaven 0.580m"),
    ("bud_agbher_expl_saldo_2025", 177206, "Exploitatiesaldo +0.177m"),
    ("bud_agbher_prijssub_2025", 243227, "Prijssubsidie gemeente 0.243m"),
    ("bud_agbher_invest_exp_2025", 83816, "Investeringsuitgaven 0.084m"),
    ("bud_agbher_invest_saldo_2025", -83816, "Investeringssaldo -0.084m"),
    ("bud_agbher_fin_rec_2025", 83816, "Financieringsontvangsten/new loans 0.084m"),
    ("bud_agbher_fin_exp_2025", 170903, "Periodieke aflossingen 0.171m"),
    ("bud_agbher_fin_saldo_2025", -87087, "Financieringssaldo -0.087m"),
    ("bud_agbher_new_loans_2025", 83816, "Nieuwe leningen T4 0.084m"),
    ("bud_agbher_aflossingen_2025", 170903, "Aflossingen T4 0.171m"),
    ("bud_agbher_budget_result_2025", 6303, "Budgettair resultaat boekjaar +0.006m"),
    ("bud_agbher_bbr_2025", 213781, "BBR 0.214m"),
    ("bud_agbher_afm_2025", 6303, "AFM +0.006m thin"),
    ("bud_agbher_afm_gecorr_2025", 24907, "Gecorr AFM +0.025m"),
    ("bud_agbher_pnl_2025", 51607, "P&L winst 0.052m"),
    ("bud_agbher_dividend_2025", 51607, "Uitgekeerd dividend = full profit 0.052m to city"),
    ("bud_agbher_depr_2025", 175737, "Afschrijvingen/voorzieningen 0.176m"),
    ("bud_agbher_interest_2025", 0, "Financiele kosten 0 FOI (interest blank on kengetallen)"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbher_equity_thin_full_div_2025",
        "AGB Herzele equity 0.028m thin full dividend 0.052m",
        "Nettoactief flat 0.028m while full PnL paid to city; cum P&L only 0.0025m",
        51607,
    ),
    (
        "comm_agbher_leasing_mva_1_67m_2025",
        "AGB Herzele leasing MVA 1.67m shell",
        "Leasing/soortgelijke 1.667m of 1.839m MVA Steenoven culture/sport plant",
        1666568,
    ),
    (
        "comm_agbher_prijssub_0_24m_2025",
        "AGB Herzele prijssub city 0.24m",
        "City price subsidy culture/sport Steenoven",
        243227,
    ),
    (
        "comm_agbher_fin_debt_1_82m_2025",
        "AGB Herzele fin debt 1.82m declining",
        "LT 1.647 + ST due 0.170; new 0.084 amort 0.171; zero interest on P&L FOI",
        1816656,
    ),
    (
        "comm_agbher_st_recv_drop_2025",
        "AGB Herzele ST recv drop 1.03 to 0.18m",
        "ST receivables collapse; non-ruil 0.537 to 0.087m",
        852883,
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
                "AGB Herzele / Gemeente Herzele residents",
                "BBC JR2025 / DLB AGB",
                "2026-06-17",
                2025,
                2025,
                total,
                f'{{"2025":{total}}}',
                total,
                "active",
                "",
                goal,
                "FOI residual dual; review equity/div/leasing/prijssub",
                SRC,
                "strong",
                "Vlaanderen>Gemeenten>Herzele>AGB_Herzele_L5",
                TICK,
            ]
        )

lbs = [
    ("lb_agbher_equity_thin_full_div_2025", "AGB Herzele equity 0.028m thin full div 0.052m", 51607, 8.5, 3.5, 3.0, 5.0, "Equity/div FOI residual CRITICAL"),
    ("lb_agbher_leasing_mva_1_67m_2025", "AGB Herzele leasing MVA 1.67m shell", 1666568, 8.0, 6.5, 3.0, 5.8, "Leasing FOI residual"),
    ("lb_agbher_prijssub_0_24m_2025", "AGB Herzele prijssub city 0.24m", 243227, 7.0, 4.0, 3.0, 4.7, "Prijssub FOI residual"),
    ("lb_agbher_fin_debt_1_82m_2025", "AGB Herzele fin debt 1.82m zero interest FOI", 1816656, 7.5, 6.5, 3.0, 5.7, "Debt FOI residual"),
    ("lb_agbher_assets_2_22m_2025", "AGB Herzele assets 2.22m Entity II", 2223824, 6.0, 6.5, 3.0, 5.1, "Map residual shell"),
    ("lb_agbher_st_recv_drop_2025", "AGB Herzele ST recv drop to 0.18m", 176641, 7.0, 4.0, 3.0, 4.7, "Recv FOI residual"),
    ("lb_agbher_afm_thin_0_01m_2025", "AGB Herzele AFM +0.006m thin", 6303, 6.0, 2.0, 3.0, 3.5, "Monitor residual AFM"),
]
tco = "JR2025 Entity II dual residual VL strong primary BBC equity thin full div leasing/prijssub AGB Herzele"
with open(ROOT / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for iid, name, cost, absu, cost_s, diff, prio, cut in lbs:
        w.writerow(
            [
                iid,
                name,
                "L5",
                "local_budget_line",
                "Vlaanderen>Gemeenten>Herzele>AGB_Herzele_L5",
                cost,
                cost,
                tco,
                "strong",
                SRC,
                "Herzele residents",
                "Local dual residual map VL JR2025 AGB Herzele",
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
            "Vlaanderen>Gemeenten>Herzele>AGB_Herzele>equity_thin_div_leasing_prijssub_L5",
            ENT,
            "Equity thin 0.028m flat while full dividend 0.052m=PnL policy; leasing MVA 1.667m residual "
            "terms Steenoven; prijssubsidie 0.243m formula multi-year; fin debt 1.817m schedule "
            "city vs bank and why interest 0 on P&L; ST recv drop 1.030 to 0.177m (non-ruil 0.537 to 0.087) "
            "drivers; AFM thin 0.006m sustainability vs dividend",
            "Entity II dual residual: culture/sport Steenoven AGB with critically thin equity, full profit "
            "dividend, leasing-heavy plant and city prijssub after city GE already mined",
            8,
            "Gemeente / AGB Herzele",
            "info@herzele.be",
            "Markt 20 9550 Herzele",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-07",
            "",
            "",
            "",
            "",
            "comm_agbher_equity_thin_full_div_2025",
            "lb_agbher_equity_thin_full_div_2025",
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
        if row["task_id"] == "rq_1163":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                (row.get("notes") or "")
                + f" | {TICK} AGB Herzele JR2025 dual residual full BBC; FOI {GAP}"
            )
            row["entity_id"] = ENT
            row["hierarchy_target"] = "Vlaanderen>Gemeenten>Herzele>AGB_Herzele"
        rows.append(row)
ids = {row["task_id"] for row in rows}
if "rq_1164" not in ids:
    rows.append(
        {
            "task_id": "rq_1164",
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
            "notes": f"spawned by {TICK}; next residual dual L5 after AGB Herzele",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

print("budgets", len(budgets), "cmts", len(cmts), "lbs", len(lbs), "OK")

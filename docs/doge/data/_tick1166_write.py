# tick1166: AGB Bree JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_bree_jr2025"
ENT = "agb_bree"
TICK = "tick1166"
UTC = "2026-08-08T00:30:00Z"
GAP = "gap_agb_bree_afm_neg_city_loan_2m_de_weeg_invest_l5"

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Bree Jaarrekening BBC 2025 Bundel (37p) RVB 18.06.2026",
            "https://www.bree.be/sites/default/files/2026-06/Bundel%20jaarrekening%20AGB%202025.pdf",
            "AGB Bree / Stad Bree",
            "2026-08-08",
            "official_pdf",
            "Entity II dual residual sport/culture De Weeg; KBO 0871.439.585; AFM -0.009m "
            "gecorr -0.160m city renteloos 2.0m invest 4.08m debt 10.78m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Bree",
            "AGB Bree",
            "AGB Bree",
            "local_entity",
            "city_bree",
            "nl",
            "https://www.bree.be/beleid/bestuur/autonoom-gemeentebedrijf-agb/jaarrekening-agb",
            "info@bree.be",
            "Witte Torenwal 23 bus 1 3960 Bree",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0871.439.585; assets 18.304m JUMP equity 5.216m cash 1.075m DROP "
            "fin debt 10.776m city renteloos new 2.0m invest De Weeg 4.076m AFM -0.009m "
            "gecorr AFM -0.160m NEG budget -2.085m prijssub sporthal 0.732m; "
            "Voorzitter Sietse Wils Secr Stefan Goclon FD Sven Meermans; FOI " + GAP,
        ]
    )

budgets = [
    ("bud_agbbree_assets_2025", 18304188, "Assets balanstotaal YE2025 18.304m JUMP from 14.948m"),
    ("bud_agbbree_equity_2025", 5216490, "Nettoactief YE2025 5.216m"),
    ("bud_agbbree_cum_pnl_2025", 2282595, "Gecumuleerd overschot YE2025 2.283m"),
    ("bud_agbbree_cap_subs_2025", 109223, "Kapitaalssubsidies YE2025 0.109m"),
    ("bud_agbbree_overig_netto_2025", 2824672, "Overig nettoactief YE2025 2.825m"),
    ("bud_agbbree_debt_total_2025", 13087698, "Schulden total YE2025 13.088m"),
    ("bud_agbbree_fin_debt_2025", 10776460, "Fin schulden T4 total YE2025 10.776m (LT 10.190 + ST due 0.586)"),
    ("bud_agbbree_fin_debt_lt_2025", 10190237, "Fin schulden LT YE2025 10.190m"),
    ("bud_agbbree_fin_debt_st_due_2025", 586223, "Fin schulden LT vervallend YE2025 0.586m"),
    ("bud_agbbree_cash_2025", 1075030, "Liquide middelen YE2025 1.075m DROP from 1.921m"),
    ("bud_agbbree_mva_2025", 13314044, "MVA bedrijfsmatig YE2025 13.314m"),
    ("bud_agbbree_mva_buildings_2025", 13126734, "MVA terreinen/gebouwen YE2025 13.127m JUMP De Weeg"),
    ("bud_agbbree_immva_2025", 1803602, "Immateriele VA YE2025 1.804m (plans/studies)"),
    ("bud_agbbree_st_nonruil_recv_2025", 1804996, "ST vorderingen niet-ruil YE2025 1.805m JUMP FOI"),
    ("bud_agbbree_inventory_2025", 214338, "Voorraden YE2025 0.214m"),
    ("bud_agbbree_expl_rec_2025", 1777872, "Exploitatieontvangsten 1.778m"),
    ("bud_agbbree_expl_exp_2025", 1188146, "Exploitatieuitgaven 1.188m"),
    ("bud_agbbree_expl_saldo_2025", 589726, "Exploitatiesaldo +0.590m"),
    ("bud_agbbree_prijssub_sporthal_2025", 731585, "Prijssubsidie sporthal toegangsgelden 0.732m"),
    ("bud_agbbree_invest_exp_2025", 4076379, "Investeringsuitgaven 4.076m (De Weeg 3.660m)"),
    ("bud_agbbree_invest_de_weeg_2025", 3660091, "De Weeg bouw sporthal/zwembad 3.660m"),
    ("bud_agbbree_invest_saldo_2025", -4076379, "Investeringssaldo -4.076m"),
    ("bud_agbbree_fin_rec_2025", 2000000, "Financieringsontvangsten city renteloze lening 2.000m"),
    ("bud_agbbree_fin_exp_2025", 598524, "Aflossingen 0.599m (bank 0.343 + city 0.256)"),
    ("bud_agbbree_fin_saldo_2025", 1401476, "Financieringssaldo +1.401m"),
    ("bud_agbbree_new_loans_city_2025", 2000000, "Nieuwe renteloze lening stad 2.000m"),
    ("bud_agbbree_aflossingen_2025", 598524, "Aflossingen T4 0.599m"),
    ("bud_agbbree_budget_result_2025", -2085178, "Budgettair resultaat boekjaar -2.085m NEG"),
    ("bud_agbbeg_bbr_wrong", 0, "placeholder skip"),
    ("bud_agbbree_bbr_2025", 665974, "BBR 0.666m"),
    ("bud_agbbree_afm_2025", -8798, "AFM -0.009m NEG"),
    ("bud_agbbree_afm_gecorr_2025", -160273, "Gecorr AFM -0.160m NEG CRITICAL (aangewezen 0.750m)"),
    ("bud_agbbree_pnl_2025", 209190, "P&L +0.209m"),
    ("bud_agbbree_dividend_2025", 41838, "Dividend to city 0.042m (partial of PnL)"),
    ("bud_agbbree_interest_2025", 118231, "Financiele kosten 0.118m (bank 0.064 + other entities 0.054)"),
    ("bud_agbbree_depr_2025", 353384, "Afschrijvingen 0.353m"),
]
# remove placeholder
budgets = [b for b in budgets if b[0] != "bud_agbbeg_bbr_wrong"]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbbree_afm_neg_gecorr_0_16m_2025",
        "AGB Bree AFM -9k / gecorr -0.16m NEG",
        "AFM NEG; gecorr AFM -0.160m; indicated amort 0.750m >> contractual 0.599m",
        160273,
    ),
    (
        "comm_agbbree_city_loan_2m_2025",
        "AGB Bree city renteloze loan 2.0m new",
        "New interest-free city loan for De Weeg sporthal/zwembad; more planned 2026+; city amort 0.256m",
        2000000,
    ),
    (
        "comm_agbbree_de_weeg_invest_4_08m_2025",
        "AGB Bree De Weeg invest 4.08m",
        "Sporthal+zwembad build 3.66m + plans 0.20m; delivery spring 2027; Sport VL/AGION subsidies FOI",
        4076379,
    ),
    (
        "comm_agbbree_fin_debt_10_78m_2025",
        "AGB Bree fin debt 10.78m JUMP",
        "LT 10.190 + ST due 0.586; new city 2.0m; bank+city amort mix",
        10776460,
    ),
    (
        "comm_agbbree_prijssub_0_73m_2025",
        "AGB Bree prijssub sporthal 0.73m",
        "City price subsidy on sporthal access fees 0.732m (78pct of MJP)",
        731585,
    ),
    (
        "comm_agbbree_st_nonruil_recv_1_80m_2025",
        "AGB Bree ST non-ruil recv 1.80m JUMP",
        "Opaque non-exchange ST receivables jump FOI",
        1804996,
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
                "AGB Bree / Stad Bree residents",
                "BBC JR2025 / DLB AGB / Sport VL",
                "2026-06-18",
                2025,
                2027,
                total,
                f'{{"2025":{total}}}',
                total,
                "active",
                "",
                goal,
                "FOI residual dual; review AFM/city loan/De Weeg",
                SRC,
                "strong",
                "Vlaanderen>Gemeenten>Bree>AGB_Bree_L5",
                TICK,
            ]
        )

lbs = [
    ("lb_agbbree_fin_debt_10_78m_2025", "AGB Bree fin debt 10.78m city loan shell", 10776460, 8.0, 8.0, 3.0, 6.3, "Debt FOI residual"),
    ("lb_agbbree_de_weeg_invest_4_08m_2025", "AGB Bree De Weeg invest 4.08m", 4076379, 7.5, 6.5, 3.0, 5.7, "Invest FOI residual"),
    ("lb_agbbree_city_loan_2m_2025", "AGB Bree city renteloze loan 2.0m", 2000000, 8.5, 6.5, 3.0, 6.0, "City loan FOI residual CRITICAL"),
    ("lb_agbbree_gecorr_afm_neg_0_16m_2025", "AGB Bree gecorr AFM -0.16m NEG", 160273, 8.5, 3.5, 3.0, 5.0, "AFM FOI residual CRITICAL"),
    ("lb_agbbree_prijssub_0_73m_2025", "AGB Bree prijssub sporthal 0.73m", 731585, 7.5, 5.5, 3.0, 5.3, "Prijssub FOI residual"),
    ("lb_agbbree_assets_18_30m_2025", "AGB Bree assets 18.30m JUMP Entity II", 18304188, 6.0, 8.0, 3.0, 5.7, "Map residual shell"),
    ("lb_agbbree_budget_neg_2_09m_2025", "AGB Bree budget result -2.09m", 2085178, 7.5, 6.5, 3.0, 5.7, "Budget FOI residual"),
    ("lb_agbbree_st_nonruil_1_80m_2025", "AGB Bree ST non-ruil recv 1.80m JUMP", 1804996, 7.0, 6.5, 3.0, 5.5, "Recv FOI residual"),
]
tco = "JR2025 Entity II dual residual VL strong primary BBC AFM NEG city renteloos De Weeg AGB Bree"
with open(ROOT / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for iid, name, cost, absu, cost_s, diff, prio, cut in lbs:
        w.writerow(
            [
                iid,
                name,
                "L5",
                "local_budget_line",
                "Vlaanderen>Gemeenten>Bree>AGB_Bree_L5",
                cost,
                cost,
                tco,
                "strong",
                SRC,
                "Bree residents",
                "Local dual residual map VL JR2025 AGB Bree",
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
            "Vlaanderen>Gemeenten>Bree>AGB_Bree>afm_neg_city_loan_de_weeg_L5",
            ENT,
            "AFM -8.798 and gecorr AFM -160.273 multi-year path; city renteloze lening 2.000m new + residual "
            "schedule (amort city 0.256 bank 0.343) and planned further city loans 2026+ for De Weeg; "
            "De Weeg sporthal/zwembad invest 4.076m total cost/tender Cordeel claim FOI; Sport VL/AGION "
            "subsidy drawdown; prijssub sporthal 0.732m formula; ST non-ruil recv 1.805m composition; "
            "cash drop 1.921 to 1.075m; budget -2.085m recovery",
            "Entity II dual residual: sport/culture AGB building De Weeg with NEG AFM, city interest-free "
            "loan shell and multi-m invest after city GE already mined (AGB AFM NEG noted tick1093)",
            9,
            "Stad / AGB Bree",
            "info@bree.be",
            "Witte Torenwal 23 bus 1 3960 Bree",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-08",
            "",
            "",
            "",
            "",
            "comm_agbbree_city_loan_2m_2025",
            "lb_agbbree_city_loan_2m_2025",
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
        if row["task_id"] == "rq_1166":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                (row.get("notes") or "")
                + f" | {TICK} AGB Bree JR2025 dual residual full BBC; FOI {GAP}"
            )
            row["entity_id"] = ENT
            row["hierarchy_target"] = "Vlaanderen>Gemeenten>Bree>AGB_Bree"
        rows.append(row)
ids = {row["task_id"] for row in rows}
if "rq_1167" not in ids:
    rows.append(
        {
            "task_id": "rq_1167",
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
            "notes": f"spawned by {TICK}; next residual dual L5 after AGB Bree",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

print("budgets", len(budgets), "cmts", len(cmts), "lbs", len(lbs), "OK")

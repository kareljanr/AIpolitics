# tick1170: AGB Nazareth-De Pinte JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_nazareth_depinte_jr2025"
ENT = "agb_nazareth_depinte"
TICK = "tick1170"
UTC = "2026-08-08T02:30:00Z"
GAP = "gap_agb_nazdp_city_loan_4_6m_prijssub_cash_thin_l5"
URL = "https://nazarethdepinte.be/sites/default/files/2026-06/FIN-JR2025-001-AGB-Jaarrekening-2025-met-documentatie.pdf"

csv.field_size_limit(10_000_000)

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Nazareth-De Pinte Jaarrekening BBC 2025 (172p) RVB 22.06.2026",
            URL,
            "AGB Nazareth-De Pinte / Gemeente Nazareth-De Pinte",
            "2026-08-08",
            "official_pdf",
            "Entity II dual residual; KBO 0643.819.583; assets 5.902m fin debt 4.643m "
            "city renteloos shell prijssub 0.622m cash 0.033m thin; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Nazareth-De Pinte",
            "AGB Nazareth-De Pinte",
            "AGB Nazareth-De Pinte",
            "local_entity",
            "city_nazareth_depinte",
            "nl",
            "https://nazarethdepinte.be",
            "info@nazarethdepinte.be",
            "Gemeenteplein 1 9840 Nazareth-De Pinte",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0643.819.583; fusion AGB first BBC year; assets 5.902m equity 0.307m "
            "cash 0.033m THIN fin debt 4.643m city renteloos (LT 4.282 + ST due 0.361) "
            "prijssub excl BTW 0.622m BBR 0.055m AFM +0.017m gecorr AFM +0.022m "
            "dividend 0.005m; AD Steven Van de Velde FD Virginie Meurisse; FOI " + GAP,
        ]
    )

budgets = [
    ("bud_agbnazdp_assets_2025", 5901884, "Assets balanstotaal YE2025 5.902m"),
    ("bud_agbnazdp_equity_2025", 306763, "Nettoactief YE2025 0.307m THIN vs debt"),
    ("bud_agbnazdp_cum_pnl_2025", 43467, "Gecumuleerd overschot YE2025 0.043m"),
    ("bud_agbnazdp_cap_subs_2025", 238296, "Kapitaalssubsidies YE2025 0.238m"),
    ("bud_agbnazdp_other_netto_2025", 25000, "Overig nettoactief YE2025 0.025m"),
    ("bud_agbnazdp_debt_total_2025", 5595120, "Schulden total YE2025 5.595m"),
    ("bud_agbnazdp_fin_debt_2025", 4642536, "Fin schulden T3 total YE2025 4.643m city renteloos"),
    ("bud_agbnazdp_fin_debt_lt_2025", 4281756, "Fin schulden LT YE2025 4.282m andere leningen"),
    ("bud_agbnazdp_fin_debt_st_due_2025", 360780, "Fin schulden LT vervallend YE2025 0.361m"),
    ("bud_agbnazdp_cash_2025", 32919, "Liquide middelen YE2025 0.033m THIN CRITICAL vs ST due"),
    ("bud_agbnazdp_mva_2025", 4818761, "MVA YE2025 4.819m"),
    ("bud_agbnazdp_mva_buildings_2025", 4506851, "MVA terreinen/gebouwen bedrijfsmatig YE2025 4.507m"),
    ("bud_agbnazdp_st_nonruil_recv_2025", 789192, "ST vorderingen niet-ruil YE2025 0.789m"),
    ("bud_agbnazdp_expl_rec_2025", 1008943, "Exploitatieontvangsten 1.009m"),
    ("bud_agbnazdp_expl_exp_2025", 622241, "Exploitatieuitgaven 0.622m"),
    ("bud_agbnazdp_expl_saldo_2025", 386702, "Exploitatiesaldo +0.387m"),
    ("bud_agbnazdp_prijssub_2025", 622152, "Prijssubsidie gemeente excl BTW 0.622m (incl 0.659m)"),
    ("bud_agbnazdp_retributies_2025", 255504, "Ontvangsten retributies 0.256m"),
    ("bud_agbnazdp_invest_exp_2025", 458638, "Investeringsuitgaven 0.459m"),
    ("bud_agbnazdp_invest_saldo_2025", -458638, "Investeringssaldo -0.459m (no invest receipts)"),
    ("bud_agbnazdp_new_loans_2025", 458638, "Nieuwe city leningen 0.459m (= invest)"),
    ("bud_agbnazdp_repay_2025", 370107, "Periodieke aflossingen 0.370m"),
    ("bud_agbnazdp_fin_saldo_2025", 88532, "Financieringssaldo +0.089m"),
    ("bud_agbnazdp_budget_result_2025", 16596, "Budgettair resultaat boekjaar +0.017m"),
    ("bud_agbnazdp_bbr_2025", 54707, "Beschikbaar BBR YE2025 0.055m"),
    ("bud_agbnazdp_afm_2025", 16596, "AFM +0.017m thin equals budget result"),
    ("bud_agbnazdp_afm_gecorr_2025", 22382, "Gecorr AFM +0.022m POS (aangewezen 0.364m)"),
    ("bud_agbnazdp_pnl_2025", 7702, "P&L +0.008m"),
    ("bud_agbnazdp_dividend_2025", 5000, "Dividend to city 0.005m partial of PnL"),
    ("bud_agbnazdp_interest_2025", 3082, "Financiele kosten 0.003m thin (renteloze city loans)"),
    ("bud_agbnazdp_depr_2025", 395913, "Afschrijvingen 0.396m"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbnazdp_city_loan_4_64m_2025",
        "AGB Naz-DP city renteloze loan stock 4.64m",
        "100pct andere leningen from gemeente; amort tracks depreciation",
        4642536,
    ),
    (
        "comm_agbnazdp_prijssub_0_62m_2025",
        "AGB Naz-DP prijssubsidie 0.62m excl BTW",
        "City price subsidy youth/sport/culture shell dual residual",
        622152,
    ),
    (
        "comm_agbnazdp_cash_thin_0_03m_2025",
        "AGB Naz-DP cash 0.03m THIN CRITICAL",
        "Cash 33k vs ST due 361k; city R/C path residual",
        32919,
    ),
    (
        "comm_agbnazdp_afm_thin_0_02m_2025",
        "AGB Naz-DP AFM +0.02m thin equals budget",
        "AFM equals budget year result thin positive",
        16596,
    ),
    (
        "comm_agbnazdp_st_nonruil_0_79m_2025",
        "AGB Naz-DP ST non-ruil recv 0.79m",
        "Large short-term non-exchange receivables residual",
        789192,
    ),
    (
        "comm_agbnazdp_dividend_0_005m_2025",
        "AGB Naz-DP dividend 5k of PnL 7.7k",
        "Partial dividend to fusion municipality",
        5000,
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
                "2026-06-22",
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
                "Vlaanderen>Gemeenten>Nazareth-De_Pinte>AGB",
                TICK,
            ]
        )

lbs = [
    ("lb_agbnazdp_city_loan_4_64m_2025", "AGB Naz-DP city loan debt 4.64m shell", 4642536, 7.0, 6.5, 3.0, "City loan FOI residual"),
    ("lb_agbnazdp_prijssub_0_62m_2025", "AGB Naz-DP prijssub 0.62m", 622152, 7.0, 5.5, 3.0, "Subsidy FOI residual"),
    ("lb_agbnazdp_cash_thin_0_03m_2025", "AGB Naz-DP cash 0.03m CRITICAL", 32919, 9.0, 3.5, 3.0, "Treasury FOI residual"),
    ("lb_agbnazdp_assets_5_9m_2025", "AGB Naz-DP assets 5.9m Entity II", 5901884, 5.5, 6.0, 3.0, "Map residual"),
    ("lb_agbnazdp_equity_thin_0_31m_2025", "AGB Naz-DP equity 0.31m vs debt 4.6m", 306763, 7.0, 5.0, 3.0, "Capital residual"),
    ("lb_agbnazdp_st_due_0_36m_2025", "AGB Naz-DP ST due 0.36m wall", 360780, 7.0, 5.0, 3.0, "Amort wall FOI"),
    ("lb_agbnazdp_afm_thin_0_02m_2025", "AGB Naz-DP AFM +0.02m THIN", 16596, 6.5, 3.5, 3.0, "Monitor residual"),
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
                "Vlaanderen>Gemeenten>Nazareth-De_Pinte>AGB_L5",
                cost,
                cost,
                "JR2025 Entity II dual residual VL strong primary BBC fusion city loan shell cash THIN",
                "strong",
                SRC,
                "Nazareth-De Pinte residents / sport-culture users",
                "Local dual residual map VL JR2025 AGB Naz-DP",
                "BBC J2/J4/J5/T2/T3 primary",
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
            "Vlaanderen>Gemeenten>Nazareth-De_Pinte>AGB>city_loan_prijssub_cash_L5",
            ENT,
            "City renteloze lening schedule behind fin debt 4.643m (ST due 0.361m) amort vs "
            "depreciation mapping; prijssubsidie 0.622m excl BTW multi-year formula and overfunding "
            "risk note; treasury plan cash 0.033m THIN vs amort wall; ST non-ruil recv 0.789m "
            "counterparties; fusion predecessor AGB recon (JR2024 columns zero); invest 0.459m "
            "project list; dividend policy 5k of 7.7k PnL",
            "Entity II fusion AGB dual residual: almost fully city-debt-financed (4.64m vs equity "
            "0.31m) with critical cash 33k and material prijs subsidy",
            8,
            "Gemeente / AGB Nazareth-De Pinte",
            "info@nazarethdepinte.be",
            "Gemeenteplein 1 9840 Nazareth-De Pinte",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-08",
            "",
            "",
            "",
            "",
            "comm_agbnazdp_city_loan_4_64m_2025|comm_agbnazdp_prijssub_0_62m_2025",
            "lb_agbnazdp_city_loan_4_64m_2025|lb_agbnazdp_cash_thin_0_03m_2025",
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
        if row["task_id"] == "rq_1170":
            row["status"] = "done"
            row["entity_id"] = ENT
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick1170 AGB Nazareth-De Pinte JR2025 Entity II dual residual; city loan shell "
                "4.64m prijssub 0.62m cash thin; FOI " + GAP
            )
        rows.append(row)
if not any(r["task_id"] == "rq_1171" for r in rows):
    rows.append(
        {
            "task_id": "rq_1171",
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
            "notes": "spawned by tick1170; next residual dual L5 after AGB Nazareth-De Pinte",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print("tick1170 write OK", len(budgets), "budgets", len(cmts), "cmts", len(lbs), "lbs")

# tick1177: AGB Willebroek JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_willebroek_jr2025"
ENT = "agb_willebroek"
TICK = "tick1177"
UTC = "2026-08-08T06:00:00Z"
GAP = "gap_agb_wil_debt_jump_20_9m_invest_9_3m_afm_neg_prijssub_l5"
URL = "https://www.willebroek.be/nl/over-willebroek/beleid/jaarrekening"

csv.field_size_limit(10_000_000)

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Willebroek Jaarrekening BBC 2025 (136p) RVB/GR 23.06.2026 pub 24.06.2026",
            URL,
            "AGB Willebroek / Gemeente Willebroek",
            "2026-08-08",
            "official_pdf",
            "Entity II dual residual; KBO 0679.456.888; assets 24.779m fin debt JUMP 20.892m "
            "invest 9.287m new loans 9.176m AFM -0.026m gecorr -0.477m prijssub 1.453m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Willebroek",
            "AGB Willebroek",
            "AGB Willebroek",
            "local_entity",
            "city_willebroek",
            "nl",
            URL,
            "info@willebroek.be",
            "Pastorijstraat 1 2830 Willebroek",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0679.456.888; sport/culture AGB Huis vrije tijd; assets 24.779m JUMP "
            "equity 1.153m thin cash 1.505m JUMP fin debt 20.892m JUMP new loans 9.176m invest 9.287m "
            "prijssub 1.453m BBR 0.435m AFM -0.026m NEG gecorr AFM -0.477m NEG DEEP PnL -0.035m "
            "div 0.001m; Secr Dirk Blommaert Rekenplichtige Katja Mampaey; FOI " + GAP,
        ]
    )

budgets = [
    ("bud_agbwil_assets_2025", 24779052, "Assets balanstotaal YE2025 24.779m JUMP from 14.141m"),
    ("bud_agbwil_equity_2025", 1152535, "Nettoactief YE2025 1.153m THIN vs debt 20.9m"),
    ("bud_agbwil_cum_pnl_2025", 538590, "Gecumuleerd overschot YE2025 0.539m DROP from 0.574m"),
    ("bud_agbwil_cap_subs_2025", 588946, "Kapitaalssubsidies YE2025 0.589m"),
    ("bud_agbwil_other_netto_2025", 25000, "Overig nettoactief YE2025 0.025m"),
    ("bud_agbwil_debt_total_2025", 23626517, "Schulden total YE2025 23.627m JUMP"),
    ("bud_agbwil_fin_debt_2025", 20892330, "Fin schulden T4 total YE2025 20.892m JUMP from 12.245m"),
    ("bud_agbwil_fin_debt_lt_2025", 20277237, "Fin schulden LT YE2025 20.277m"),
    ("bud_agbwil_fin_debt_st_due_2025", 615093, "Fin schulden LT vervallend YE2025 0.615m"),
    ("bud_agbwil_cash_2025", 1505487, "Liquide middelen YE2025 1.505m JUMP from 0.106m"),
    ("bud_agbwil_mva_2025", 21513777, "MVA YE2025 21.514m JUMP from 12.741m"),
    ("bud_agbwil_mva_buildings_2025", 21150813, "MVA terreinen/gebouwen YE2025 21.151m JUMP"),
    ("bud_agbwil_st_nonruil_recv_2025", 1535645, "ST vorderingen niet-ruil YE2025 1.536m"),
    ("bud_agbwil_st_nonfin_debt_2025", 2700639, "ST niet-fin schulden ruil YE2025 2.701m JUMP (construction)"),
    ("bud_agbwil_expl_rec_2025", 2032160, "Exploitatieontvangsten 2.032m"),
    ("bud_agbwil_expl_exp_2025", 1529912, "Exploitatieuitgaven 1.530m"),
    ("bud_agbwil_expl_saldo_2025", 502248, "Exploitatiesaldo +0.502m"),
    ("bud_agbwil_prijssub_2025", 1452586, "Prijssubsidie gemeente 1.453m"),
    ("bud_agbwil_invest_exp_2025", 9287132, "Investeringsuitgaven 9.287m MASSIVE (Huis vrije tijd/sport)"),
    ("bud_agbwil_invest_saldo_2025", -9287132, "Investeringssaldo -9.287m"),
    ("bud_agbwil_new_loans_2025", 9176183, "Nieuwe leningen 9.176m JUMP (city dual tick1020)"),
    ("bud_agbwil_repay_2025", 528710, "Periodieke aflossingen 0.529m"),
    ("bud_agbwil_fin_saldo_2025", 8647473, "Financieringssaldo +8.647m"),
    ("bud_agbwil_budget_result_2025", -137412, "Budgettair resultaat boekjaar -0.137m"),
    ("bud_agbwil_bbr_2025", 434836, "Beschikbaar BBR YE2025 0.435m"),
    ("bud_agbwil_afm_2025", -26463, "AFM -0.026m NEG"),
    ("bud_agbwil_afm_gecorr_2025", -477341, "Gecorr AFM -0.477m NEG DEEP (aangewezen 0.980m)"),
    ("bud_agbwil_aangewezen_amort_2025", 979589, "Gecorrigeerde aflossingen o.b.v. fin schulden 0.980m"),
    ("bud_agbwil_pnl_2025", -34606, "P&L -0.035m NEG"),
    ("bud_agbwil_dividend_2025", 1000, "Dividend to city 0.001m while PnL NEG"),
    ("bud_agbwil_interest_2025", 55, "Financiele kosten J5 0.0001m thin"),
    ("bud_agbwil_depr_2025", 526448, "Afschrijvingen 0.526m"),
    ("bud_agbwil_mjp_debt_2026", 19954170, "MJP fin debt YE2026 path 19.954m"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbwil_fin_debt_jump_20_9m_2025",
        "AGB Willebroek fin debt JUMP to 20.9m",
        "Debt 12.2->20.9m via new loans 9.176m for sport/culture shell",
        20892330,
    ),
    (
        "comm_agbwil_invest_9_29m_2025",
        "AGB Willebroek invest 9.29m Huis vrije tijd",
        "Massive MVA buildings jump dual residual",
        9287132,
    ),
    (
        "comm_agbwil_new_loans_9_18m_2025",
        "AGB Willebroek new loans 9.18m 2025",
        "Matches city toegestane leningen JUMP tick1020 dual",
        9176183,
    ),
    (
        "comm_agbwil_gecorr_afm_neg_0_48m_2025",
        "AGB Willebroek gecorr AFM -0.48m NEG DEEP",
        "Indicated amort 0.980m >> contractual 0.529m; thin AFM NEG",
        477341,
    ),
    (
        "comm_agbwil_prijssub_1_45m_2025",
        "AGB Willebroek prijssubsidie 1.45m",
        "City price subsidy sport/culture dual residual",
        1452586,
    ),
    (
        "comm_agbwil_st_payables_jump_2_70m_2025",
        "AGB Willebroek ST payables JUMP 2.70m",
        "Construction creditors on invest ramp",
        2700639,
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
                "2026-06-23",
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
                "Vlaanderen>Gemeenten>Willebroek>AGB",
                TICK,
            ]
        )

lbs = [
    ("lb_agbwil_fin_debt_20_9m_2025", "AGB Willebroek fin debt JUMP 20.9m", 20892330, 8.0, 8.0, 3.0, "Debt FOI residual"),
    ("lb_agbwil_invest_9_29m_2025", "AGB Willebroek invest 9.29m shell", 9287132, 7.5, 7.5, 3.0, "Capex FOI residual"),
    ("lb_agbwil_new_loans_9_18m_2025", "AGB Willebroek new loans 9.18m", 9176183, 7.5, 7.5, 3.0, "Loan FOI residual"),
    ("lb_agbwil_gecorr_afm_neg_0_48m_2025", "AGB Willebroek gecorr AFM -0.48m NEG DEEP", 477341, 8.5, 5.0, 3.0, "AFM FOI residual"),
    ("lb_agbwil_prijssub_1_45m_2025", "AGB Willebroek prijssub 1.45m", 1452586, 7.5, 6.0, 3.0, "Subsidy FOI residual"),
    ("lb_agbwil_assets_24_8m_2025", "AGB Willebroek assets JUMP 24.8m", 24779052, 6.0, 8.0, 3.0, "Map residual"),
    ("lb_agbwil_equity_thin_1_15m_2025", "AGB Willebroek equity thin 1.15m vs debt 21m", 1152535, 7.5, 5.5, 3.0, "Capital FOI residual"),
    ("lb_agbwil_afm_neg_0_03m_2025", "AGB Willebroek AFM -0.03m NEG", 26463, 8.0, 3.5, 3.0, "AFM FOI residual"),
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
                "Vlaanderen>Gemeenten>Willebroek>AGB_L5",
                cost,
                cost,
                "JR2025 Entity II dual residual VL strong primary BBC debt JUMP invest 9m AFM NEG",
                "strong",
                SRC,
                "Willebroek residents / sport-culture users",
                "Local dual residual map VL JR2025 AGB Willebroek",
                "BBC J2/J4/J5/T4 kengetallen primary",
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
            "Vlaanderen>Gemeenten>Willebroek>AGB>debt_invest_afm_prijssub_L5",
            ENT,
            "Fin debt JUMP 12.2->20.9m lender schedule; new loans 9.176m city dual recon with tick1020 "
            "toegestane leningen; invest 9.287m project list Huis vrije tijd/sport; AFM -0.026m and "
            "gecorr AFM -0.477m multi-year path (aangewezen 0.980m); prijssubsidie 1.453m formula; "
            "ST payables JUMP 2.701m counterparties; dividend 1k while PnL -35k; MJP debt path YE2026 19.95m",
            "Entity II sport/culture AGB dual residual: EUR9.3m invest ramp financed by EUR9.2m new debt "
            "to EUR20.9m stock with NEG AFM and deep NEG gecorr AFM after city GE tick1020",
            9,
            "Gemeente / AGB Willebroek",
            "info@willebroek.be",
            "Pastorijstraat 1 2830 Willebroek",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-08",
            "",
            "",
            "",
            "",
            "comm_agbwil_fin_debt_jump_20_9m_2025|comm_agbwil_invest_9_29m_2025",
            "lb_agbwil_fin_debt_20_9m_2025|lb_agbwil_invest_9_29m_2025|lb_agbwil_gecorr_afm_neg_0_48m_2025",
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
        if row["task_id"] == "rq_1177":
            row["status"] = "done"
            row["entity_id"] = ENT
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick1177 AGB Willebroek JR2025 Entity II dual residual; debt JUMP 20.9m invest 9.3m "
                "AFM NEG prijssub 1.45m; FOI " + GAP
            )
        rows.append(row)
if not any(r["task_id"] == "rq_1178" for r in rows):
    rows.append(
        {
            "task_id": "rq_1178",
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
            "notes": "spawned by tick1177; next residual dual L5 after AGB Willebroek",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print("tick1177 write OK", len(budgets), "budgets", len(cmts), "cmts", len(lbs), "lbs")

# tick1176: AGB Stadsontwikkeling Hamont-Achel JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_hamont_achel_jr2025"
ENT = "agb_hamont_achel"
TICK = "tick1176"
UTC = "2026-08-08T05:30:00Z"
GAP = "gap_agb_ha_invest_1_25m_cash_drop_sport_transfer_l5"
URL = "https://www.hamont-achel.be/product/3986/jaarrekening-agb-stadsontwikkeling"

csv.field_size_limit(10_000_000)

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Stadsontwikkeling Hamont-Achel Jaarrekening BBC 2025 (56p) RVB 28.05.2026 pub 03.06.2026",
            URL,
            "AGB Stadsontwikkeling / Stad Hamont-Achel",
            "2026-08-08",
            "official_pdf",
            "Entity II dual residual; KBO 0827.418.710; zero fin debt invest 1.250m cash DROP "
            "BBR 1.026m AFM thin +0.056m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Stadsontwikkeling Hamont-Achel",
            "AGB Developpement urbain Hamont-Achel",
            "AGB Urban Development Hamont-Achel",
            "local_entity",
            "city_hamont_achel",
            "nl",
            URL,
            "financien@hamont-achel.be",
            "Stad 40 3930 Hamont-Achel",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0827.418.710 NIS 72037; culture/bib/library AGB ZERO fin debt; "
            "assets 4.683m equity 4.044m cash 1.355m DROP from 2.474 invest JUMP 1.250m "
            "BBR 1.026m DROP AFM +0.056m thin PnL +0.107m dividend 0.015m; sport infra "
            "transfer planned ~2028 BTW ruling OK; Secr Marnix Goethals Voorzitter Tom Cox; FOI "
            + GAP,
        ]
    )

budgets = [
    ("bud_agbha_assets_2025", 4683065, "Assets balanstotaal YE2025 4.683m"),
    ("bud_agbha_equity_2025", 4043502, "Nettoactief YE2025 4.044m"),
    ("bud_agbha_cum_pnl_2025", 243502, "Gecumuleerd overschot YE2025 0.244m JUMP from 0.151m"),
    ("bud_agbha_other_netto_2025", 3800000, "Overig nettoactief YE2025 3.800m"),
    ("bud_agbha_debt_total_2025", 639563, "Schulden total YE2025 0.640m (no fin debt)"),
    ("bud_agbha_fin_debt_2025", 0, "Fin schulden T4 YE2025 ZERO"),
    ("bud_agbha_cash_2025", 1355237, "Liquide middelen YE2025 1.355m DROP from 2.474m"),
    ("bud_agbha_mva_2025", 3217752, "MVA YE2025 3.218m JUMP from 2.111m"),
    ("bud_agbha_mva_buildings_2025", 3152345, "MVA terreinen/gebouwen YE2025 3.152m JUMP"),
    ("bud_agbha_st_recv_2025", 110002, "ST vorderingen YE2025 0.110m"),
    ("bud_agbha_expl_rec_2025", 976841, "Exploitatieontvangsten 0.977m"),
    ("bud_agbha_expl_exp_2025", 921291, "Exploitatieuitgaven 0.921m (incl dividend 15k)"),
    ("bud_agbha_expl_saldo_2025", 55551, "Exploitatiesaldo +0.056m THIN"),
    ("bud_agbha_omzet_werking_2025", 927639, "Ontvangsten uit de werking T2 0.928m"),
    ("bud_agbha_invest_exp_2025", 1249979, "Investeringsuitgaven 1.250m JUMP (buildings 1.246m)"),
    ("bud_agbha_invest_saldo_2025", -1249979, "Investeringssaldo -1.250m (cash-financed)"),
    ("bud_agbha_budget_result_2025", -1194429, "Budgettair resultaat boekjaar -1.194m NEG (invest burn)"),
    ("bud_agbha_bbr_2025", 1026009, "Beschikbaar BBR YE2025 1.026m DROP from 2.220m"),
    ("bud_agbha_afm_2025", 55551, "AFM +0.056m THIN equals expl saldo (zero debt)"),
    ("bud_agbha_afm_gecorr_2025", 55551, "Gecorr AFM +0.056m (=AFM; zero fin debt)"),
    ("bud_agbha_pnl_2025", 107144, "P&L +0.107m"),
    ("bud_agbha_dividend_2025", 15000, "Dividend to city 0.015m DROP from 0.160m"),
    ("bud_agbha_interest_2025", 2756, "Financiele kosten 0.003m"),
    ("bud_agbha_depr_2025", 142817, "Afschrijvingen 0.143m"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbha_invest_jump_1_25m_2025",
        "AGB Hamont-Achel invest JUMP 1.25m cash-financed",
        "Buildings 1.246m; zero new loans; BBR/cash absorb",
        1249979,
    ),
    (
        "comm_agbha_cash_drop_1_12m_2025",
        "AGB Hamont-Achel cash DROP 1.12m",
        "Cash 2.474->1.355m funds invest wall",
        1118508,
    ),
    (
        "comm_agbha_zero_fin_debt_2025",
        "AGB Hamont-Achel fin debt ZERO",
        "No bank/city loan stock YE2025; T4 empty",
        0,
    ),
    (
        "comm_agbha_afm_thin_0_06m_2025",
        "AGB Hamont-Achel AFM +0.06m THIN",
        "Thin positive AFM equals expl saldo; no amort",
        55551,
    ),
    (
        "comm_agbha_sport_transfer_2028",
        "AGB Hamont-Achel sport infra transfer path ~2028",
        "BTW ruling OK 1.10.2024; transfer at new Achel sporthal; canon residual",
        0,
    ),
    (
        "comm_agbha_bbr_drop_1_19m_2025",
        "AGB Hamont-Achel BBR DROP via invest 1.19m",
        "Budget result -1.194m burns prior BBR stock",
        1194429,
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
                "2026-05-28",
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
                "Vlaanderen>Gemeenten>Hamont-Achel>AGB",
                TICK,
            ]
        )

lbs = [
    ("lb_agbha_invest_1_25m_2025", "AGB Hamont-Achel invest JUMP 1.25m", 1249979, 7.0, 6.0, 3.0, "Capex FOI residual"),
    ("lb_agbha_cash_drop_1_36m_2025", "AGB Hamont-Achel cash DROP to 1.36m", 1355237, 7.5, 6.0, 3.0, "Treasury FOI residual"),
    ("lb_agbha_budget_neg_1_19m_2025", "AGB Hamont-Achel budget result -1.19m", 1194429, 7.5, 6.0, 3.0, "Burn FOI residual"),
    ("lb_agbha_assets_4_68m_2025", "AGB Hamont-Achel assets 4.68m Entity II", 4683065, 5.5, 6.0, 3.0, "Map residual"),
    ("lb_agbha_zero_fin_debt_2025", "AGB Hamont-Achel fin debt ZERO", 1, 6.0, 3.0, 3.0, "Map residual"),
    ("lb_agbha_afm_thin_0_06m_2025", "AGB Hamont-Achel AFM +0.06m THIN", 55551, 6.5, 3.5, 3.0, "Monitor residual"),
    ("lb_agbha_bbr_1_03m_2025", "AGB Hamont-Achel BBR 1.03m DROP", 1026009, 6.0, 5.5, 3.0, "Monitor residual"),
    ("lb_agbha_pnl_0_11m_2025", "AGB Hamont-Achel PnL +0.11m", 107144, 5.5, 3.5, 3.0, "Monitor residual"),
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
                "Vlaanderen>Gemeenten>Hamont-Achel>AGB_L5",
                cost,
                cost,
                "JR2025 Entity II dual residual VL strong primary BBC zero debt invest cash burn",
                "strong",
                SRC,
                "Hamont-Achel residents / culture-bib users",
                "Local dual residual map VL JR2025 AGB Hamont-Achel",
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
            "Vlaanderen>Gemeenten>Hamont-Achel>AGB>invest_cash_sport_transfer_L5",
            ENT,
            "Invest JUMP 1.250m project list (buildings 1.246m bib/other); cash DROP 2.474->1.355m "
            "treasury plan and BBR burn path; prijssubsidie multi-year (city werkingsub 0 in 2025; "
            "omzet 0.928m embeds dual); sport infrastructure transfer ~2028 terms canon after BTW "
            "ruling 1.10.2024; dividend 15k policy vs prior 160k; thin AFM 56k multi-year",
            "Entity II culture AGB dual residual after city GE tick1091: zero fin debt but EUR1.25m "
            "cash-financed invest burn and planned sport shell transfer residual",
            8,
            "Stad / AGB Stadsontwikkeling Hamont-Achel",
            "financien@hamont-achel.be",
            "Stad 40 3930 Hamont-Achel",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-08",
            "",
            "",
            "",
            "",
            "comm_agbha_invest_jump_1_25m_2025|comm_agbha_sport_transfer_2028",
            "lb_agbha_invest_1_25m_2025|lb_agbha_cash_drop_1_36m_2025",
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
        if row["task_id"] == "rq_1176":
            row["status"] = "done"
            row["entity_id"] = ENT
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick1176 AGB Hamont-Achel JR2025 Entity II dual residual; zero debt invest 1.25m "
                "cash DROP; FOI " + GAP
            )
        rows.append(row)
if not any(r["task_id"] == "rq_1177" for r in rows):
    rows.append(
        {
            "task_id": "rq_1177",
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
            "notes": "spawned by tick1176; next residual dual L5 after AGB Hamont-Achel",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print("tick1176 write OK", len(budgets), "budgets", len(cmts), "cmts", len(lbs), "lbs")

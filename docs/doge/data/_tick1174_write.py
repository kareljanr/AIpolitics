# tick1174: AGB Pelt JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_pelt_jr2025"
ENT = "agb_pelt"
TICK = "tick1174"
UTC = "2026-08-08T04:30:00Z"
GAP = "gap_agb_pelt_st_due_jump_0_6m_prijssub_st_recv_l5"
URL = "https://www.gemeentepelt.be/jaarrekening-agb-pelt-2025"

csv.field_size_limit(10_000_000)

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Pelt Jaarrekening BBC 2025 (115p) RVB 28.05.2026 pub 02.06.2026",
            URL,
            "AGB Pelt / Gemeente Pelt",
            "2026-08-08",
            "official_pdf",
            "Entity II dual residual; KBO 0876.186.449; assets 10.310m fin debt 3.592m "
            "ST due JUMP 0.6m AFM +0.792m PnL +0.222m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Pelt",
            "AGB Pelt",
            "AGB Pelt",
            "local_entity",
            "city_pelt",
            "nl",
            URL,
            "info@gemeentepelt.be",
            "Oude Markt 2 3900 Pelt",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0876.186.449 NIS 72043; fusion AGB sport/culture/care sites; "
            "assets 10.310m equity 6.342m cash 0.725m fin debt 3.592m (LT 2.992 + ST due JUMP 0.600) "
            "BBR 2.501m AFM +0.792m gecorr AFM +0.689m PnL +0.222m zero staff zero dividend "
            "ST non-ruil recv 2.100m; AD Peter Spooren FD Ineke Vos Voorzitter Dennis Fransen; FOI "
            + GAP,
        ]
    )

budgets = [
    ("bud_agbpelt_assets_2025", 10309605, "Assets balanstotaal YE2025 10.310m"),
    ("bud_agbpelt_equity_2025", 6341888, "Nettoactief YE2025 6.342m"),
    ("bud_agbpelt_cum_pnl_2025", 908647, "Gecumuleerd overschot YE2025 0.909m JUMP from 0.686m"),
    ("bud_agbpelt_cap_subs_2025", 1823241, "Kapitaalssubsidies YE2025 1.823m"),
    ("bud_agbpelt_other_netto_2025", 3610000, "Overig nettoactief YE2025 3.610m"),
    ("bud_agbpelt_debt_total_2025", 3967717, "Schulden total YE2025 3.968m"),
    ("bud_agbpelt_fin_debt_2025", 3591882, "Fin schulden T4 total YE2025 3.592m DECLINING"),
    ("bud_agbpelt_fin_debt_lt_2025", 2991882, "Fin schulden LT YE2025 2.992m"),
    ("bud_agbpelt_fin_debt_st_due_2025", 600000, "Fin schulden LT vervallend YE2025 0.600m JUMP from 0.200m"),
    ("bud_agbpelt_cash_2025", 725472, "Liquide middelen YE2025 0.725m JUMP from 0.586m"),
    ("bud_agbpelt_mva_2025", 7422261, "MVA YE2025 7.422m"),
    ("bud_agbpelt_mva_buildings_2025", 5910208, "MVA terreinen/gebouwen bedrijfsmatig YE2025 5.910m"),
    ("bud_agbpelt_leasing_mva_2025", 50795, "Leasing MVA YE2025 0.051m"),
    ("bud_agbpelt_st_nonruil_recv_2025", 2100281, "ST vorderingen niet-ruil YE2025 2.100m"),
    ("bud_agbpelt_expl_rec_2025", 2841475, "Exploitatieontvangsten 2.841m"),
    ("bud_agbpelt_expl_exp_2025", 1849311, "Exploitatieuitgaven 1.849m"),
    ("bud_agbpelt_expl_saldo_2025", 992164, "Exploitatiesaldo +0.992m"),
    ("bud_agbpelt_omzet_werking_2025", 2775808, "Ontvangsten uit de werking 2.776m (prijssub embedded)"),
    ("bud_agbpelt_invest_exp_2025", 864840, "Investeringsuitgaven 0.865m UNDER vs MJP 1.535m"),
    ("bud_agbpelt_invest_saldo_2025", -864840, "Investeringssaldo -0.865m"),
    ("bud_agbpelt_repay_2025", 200000, "Periodieke aflossingen 0.200m"),
    ("bud_agbpelt_fin_saldo_2025", -200000, "Financieringssaldo -0.200m"),
    ("bud_agbpelt_budget_result_2025", -72677, "Budgettair resultaat boekjaar -0.073m"),
    ("bud_agbpelt_bbr_2025", 2500625, "Beschikbaar BBR YE2025 2.501m"),
    ("bud_agbpelt_afm_2025", 792164, "AFM +0.792m"),
    ("bud_agbpelt_afm_gecorr_2025", 688813, "Gecorr AFM +0.689m POS (aangewezen 0.303m)"),
    ("bud_agbpelt_pnl_2025", 222483, "P&L +0.222m (no dividend)"),
    ("bud_agbpelt_interest_2025", 27301, "Rente aan andere entiteiten 0.027m (city loans)"),
    ("bud_agbpelt_depr_2025", 768286, "Afschrijvingen 0.768m"),
    ("bud_agbpelt_mjp_debt_2026", 2991882, "MJP fin debt YE2026 path 2.992m (ST due wall 0.600m)"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbpelt_st_due_jump_0_6m_2025",
        "AGB Pelt ST due JUMP 0.6m YE2025",
        "Amort wall 0.2->0.6m while only 0.2m repaid 2025; MJP YE2026 still 0.6m due",
        600000,
    ),
    (
        "comm_agbpelt_fin_debt_3_59m_2025",
        "AGB Pelt fin debt 3.59m city/entity loans",
        "No bank debt per risk note; interest to andere entiteiten 27k",
        3591882,
    ),
    (
        "comm_agbpelt_st_nonruil_2_10m_2025",
        "AGB Pelt ST non-ruil recv 2.10m",
        "Large short-term non-exchange receivables residual",
        2100281,
    ),
    (
        "comm_agbpelt_afm_0_79m_2025",
        "AGB Pelt AFM +0.79m strong",
        "Healthy AFM/BBR dual residual fusion AGB",
        792164,
    ),
    (
        "comm_agbpelt_invest_under_0_86m_2025",
        "AGB Pelt invest UNDER 0.86 vs MJP 1.54m",
        "Capex underspend residual dual",
        864840,
    ),
    (
        "comm_agbpelt_pnl_0_22m_2025",
        "AGB Pelt PnL +0.22m no dividend",
        "Book surplus retained; BTW winstoogmerk via prijssub omzet",
        222483,
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
                "Vlaanderen>Gemeenten>Pelt>AGB",
                TICK,
            ]
        )

lbs = [
    ("lb_agbpelt_st_due_jump_0_6m_2025", "AGB Pelt ST due JUMP 0.6m wall", 600000, 8.0, 5.5, 3.0, "Amort wall FOI"),
    ("lb_agbpelt_fin_debt_3_59m_2025", "AGB Pelt fin debt 3.59m", 3591882, 6.5, 6.5, 3.0, "Debt FOI residual"),
    ("lb_agbpelt_st_nonruil_2_10m_2025", "AGB Pelt ST non-ruil recv 2.10m", 2100281, 7.5, 6.5, 3.0, "Receivable FOI"),
    ("lb_agbpelt_assets_10_3m_2025", "AGB Pelt assets 10.3m Entity II", 10309605, 5.5, 7.0, 3.0, "Map residual"),
    ("lb_agbpelt_bbr_2_50m_2025", "AGB Pelt BBR 2.50m", 2500625, 5.0, 6.5, 3.0, "Monitor residual"),
    ("lb_agbpelt_afm_0_79m_2025", "AGB Pelt AFM +0.79m", 792164, 5.0, 5.5, 3.0, "Monitor residual"),
    ("lb_agbpelt_invest_under_0_86m_2025", "AGB Pelt invest UNDER 0.86m", 864840, 6.5, 5.5, 3.0, "Capex FOI residual"),
    ("lb_agbpelt_pnl_0_22m_2025", "AGB Pelt PnL +0.22m", 222483, 5.5, 4.0, 3.0, "Monitor residual"),
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
                "Vlaanderen>Gemeenten>Pelt>AGB_L5",
                cost,
                cost,
                "JR2025 Entity II dual residual VL strong primary BBC fusion ST due JUMP healthy AFM",
                "strong",
                SRC,
                "Pelt residents / sport-culture-care users",
                "Local dual residual map VL JR2025 AGB Pelt",
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
            "Vlaanderen>Gemeenten>Pelt>AGB>st_due_prijssub_recv_L5",
            ENT,
            "ST debt due JUMP 0.200->0.600m schedule and 2026 amort wall 0.600m; city/entity loan "
            "list behind fin debt 3.592m; prijssubsidie formula on omzet 2.776m multi-year cash; "
            "ST non-ruil recv 2.100m counterparties; invest UNDER 0.865 vs MJP 1.535 project list; "
            "leasing residual 0.051m; beheersovereenkomst city guarantee terms",
            "Entity II fusion AGB dual residual after city GE tick1094: healthy AFM/BBR but ST amort "
            "wall triples and large non-ruil receivables keep dual opacity",
            8,
            "Gemeente / AGB Pelt",
            "info@gemeentepelt.be",
            "Oude Markt 2 3900 Pelt",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-08",
            "",
            "",
            "",
            "",
            "comm_agbpelt_st_due_jump_0_6m_2025|comm_agbpelt_st_nonruil_2_10m_2025",
            "lb_agbpelt_st_due_jump_0_6m_2025|lb_agbpelt_st_nonruil_2_10m_2025",
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
        if row["task_id"] == "rq_1174":
            row["status"] = "done"
            row["entity_id"] = ENT
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick1174 AGB Pelt JR2025 Entity II dual residual; ST due JUMP 0.6m AFM +0.79m "
                "PnL +0.22m; FOI " + GAP
            )
        rows.append(row)
if not any(r["task_id"] == "rq_1175" for r in rows):
    rows.append(
        {
            "task_id": "rq_1175",
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
            "notes": "spawned by tick1174; next residual dual L5 after AGB Pelt",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print("tick1174 write OK", len(budgets), "budgets", len(cmts), "cmts", len(lbs), "lbs")

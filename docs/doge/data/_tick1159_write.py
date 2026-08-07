# tick1159: AGB Veurne JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_veurne_jr2025"
ENT = "agb_veurne"
TICK = "tick1159"
UTC = "2026-08-07T21:00:00Z"
GAP = "gap_agb_veurne_btw_sporthal_gecorr_afm_neg_prefin_l5"

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Veurne Jaarrekening 2025 BBC + RVB uittreksel 18.05.2026",
            "https://www.veurne.be/sites/default/files/2026-05/Jaarrekening_AGB_2025.pdf",
            "AGB Veurne / Stad Veurne",
            "2026-08-07",
            "official_pdf",
            "Entity II dual residual; 60p BBC; KBO 0883.140.953; RVB BBR 1.279m AFM 0.080m "
            "gecorr AFM -0.289m assets 14.034m PnL -0.468m; portal 22/29.05.2026; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Veurne",
            "AGB Furnes",
            "AGB Veurne",
            "local_entity",
            "city_veurne",
            "nl",
            "https://www.veurne.be/nl/bestuur/beleidsdocumenten/jaarrekening-stad-ocmw-en-agb",
            "financien@veurne.be",
            "Sint-Denisplaats 16 8630 Veurne",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0883.140.953; assets 14.034m equity 9.525m (cum P&L -9.285m) cash 0.035m "
            "thin fin debt 4.489m MVA 11.444m BBR 1.279m AFM +0.080m gecorr AFM -0.289m NEG "
            "PnL -0.468m BTW sporthal dispute 1.15m+ prefin city loan capitalised; "
            "AD Joke Jonckheere FD Kris Degraeve Voorzitter Ben Peperstraete; FOI " + GAP,
        ]
    )

budgets = [
    ("bud_agbveurne_assets_2025", 14033664, "Assets balanstotaal YE2025 14.034m"),
    ("bud_agbveurne_equity_2025", 9524636, "Nettoactief YE2025 9.525m (overig 18.704m + capsub 0.105m + cum P&L NEG -9.285m)"),
    ("bud_agbveurne_cum_pnl_neg_2025", -9284891, "Gecumuleerd tekort YE2025 -9.285m DEEP (P&L -0.468m)"),
    ("bud_agbveurne_debt_total_2025", 4509028, "Schulden total YE2025 4.509m"),
    ("bud_agbveurne_fin_debt_2025", 4488526, "Fin schulden T4 YE2025 4.489m LT only (declining)"),
    ("bud_agbveurne_fin_debt_lt_2025", 4488526, "Fin schulden LT YE2025 4.489m (city prefin capitalised)"),
    ("bud_agbveurne_cash_2025", 35489, "Liquide middelen YE2025 0.035m THIN"),
    ("bud_agbveurne_mva_2025", 11444409, "MVA gemeenschapsgoederen YE2025 11.444m (gebouwen 11.072m)"),
    ("bud_agbveurne_mva_buildings_2025", 11071968, "MVA terreinen en gebouwen YE2025 11.072m (sporthal shell)"),
    ("bud_agbveurne_st_nonruil_recv_2025", 1254751, "ST vorderingen niet-ruil YE2025 1.255m FOI"),
    ("bud_agbveurne_lt_ruil_recv_2025", 1228041, "LT vorderingen ruil YE2025 1.228m FOI"),
    ("bud_agbveurne_cap_subs_2025", 105211, "Kapitaalssubsidies YE2025 0.105m"),
    ("bud_agbveurne_overig_netto_2025", 18704316, "Overig nettoactief YE2025 18.704m (inbreng/capital shell)"),
    ("bud_agbveurne_expl_rec_2025", 488164, "Exploitatieontvangsten 0.488m (retributies JUMP 0.488m)"),
    ("bud_agbveurne_expl_exp_2025", 408290, "Exploitatieuitgaven 0.408m"),
    ("bud_agbveurne_expl_saldo_2025", 79875, "Exploitatiesaldo +0.080m"),
    ("bud_agbveurne_invest_exp_2025", 1119, "Investeringsuitgaven 0.001m MASSIVE underspend vs MJP 0.679m"),
    ("bud_agbveurne_invest_rec_2025", 9179, "Investeringsontvangsten 0.009m"),
    ("bud_agbveurne_invest_saldo_2025", 8060, "Investeringssaldo +0.008m"),
    ("bud_agbveurne_fin_rec_2025", 420395, "Financieringsontvangsten 0.420m (new loans 0.360m)"),
    ("bud_agbveurne_fin_exp_2025", 487210, "Financieringsuitgaven/aflossingen 0.487m"),
    ("bud_agbveurne_fin_saldo_2025", -66815, "Financieringssaldo -0.067m"),
    ("bud_agbveurne_new_loans_2025", 360000, "Nieuwe leningen T4 0.360m"),
    ("bud_agbveurne_aflossingen_2025", 487210, "Aflossingen T4 0.487m (vs prior 0.060m/yr jump)"),
    ("bud_agbveurne_budget_result_2025", 21119, "Budgettair resultaat boekjaar +0.021m"),
    ("bud_agbveurne_bbr_2025", 1279186, "BBR 1.279m"),
    ("bud_agbveurne_afm_2025", 79875, "AFM +0.080m"),
    ("bud_agbveurne_afm_gecorr_2025", -289384, "Gecorr AFM -0.289m NEG CRITICAL (aangewezen afl 0.369m)"),
    ("bud_agbveurne_pnl_2025", -468292, "P&L boekjaar -0.468m"),
    ("bud_agbveurne_interest_2025", 16736, "Financiele kosten 0.017m"),
    ("bud_agbveurne_depr_2025", 557732, "Afschrijvingen/voorzieningen 0.558m"),
    ("bud_agbveurne_btw_sporthal_claim_2025", 1150092, "BTW sporthal dispute principal 1.150m FOI (excl 0.115m boeten + 0.184m intresten)"),
    ("bud_agbveurne_btw_new_claim_2025", 43870, "BTW navordering PV 03.11.2025 0.044m + 10pct boete FOI"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [
                bid,
                ENT,
                2025,
                amt,
                "",
                "",
                "BBC JR2025 primary",
                SRC,
                "strong",
                notes + "; " + TICK,
            ]
        )

cmts = [
    (
        "comm_agbveurne_btw_sporthal_1_15m_2025",
        "AGB Veurne BTW sporthal dispute 1.15m+",
        "BTW/FOD Financiën dispute sporthal deductibility; appeal Hof van Beroep ongoing; dading failed",
        1150092,
    ),
    (
        "comm_agbveurne_gecorr_afm_neg_0_29m_2025",
        "AGB Veurne gecorr AFM -0.29m NEG",
        "Indicated amort 0.369m >> contractual 0 on J2; structural debt service gap",
        289384,
    ),
    (
        "comm_agbveurne_fin_debt_prefin_4_49m_2025",
        "AGB Veurne fin debt city prefin 4.49m",
        "Prefinancing/city-linked debt capitalised ~4.489m; historically city loans 19.4m@2018",
        4488526,
    ),
    (
        "comm_agbveurne_st_nonruil_recv_1_25m_2025",
        "AGB Veurne ST non-ruil recv 1.25m",
        "Opaque non-exchange ST receivables composition",
        1254751,
    ),
    (
        "comm_agbveurne_lt_ruil_recv_1_23m_2025",
        "AGB Veurne LT ruil recv 1.23m",
        "LT exchange receivables counterparties/maturity FOI",
        1228041,
    ),
    (
        "comm_agbveurne_invest_underspend_2025",
        "AGB Veurne invest underspend 0.001 vs 0.679m MJP",
        "Proostdijk/priority invest MJP 0.679m; actual 0.001m",
        678241,
    ),
    (
        "comm_agbveurne_cum_pnl_neg_9_28m_2025",
        "AGB Veurne cum P&L NEG -9.28m",
        "Deep cumulative loss against overig netto 18.7m shell",
        9284891,
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
                "AGB Veurne / Stad Veurne residents",
                "BBC JR2025 / DLB AGB",
                "2026-05-18",
                2025,
                2025,
                total,
                f'{{"2025":{total}}}',
                total,
                "active",
                "",
                goal,
                "FOI residual dual; review shell/BTW/debt",
                SRC,
                "strong",
                "Vlaanderen>Gemeenten>Veurne>AGB_Veurne_L5",
                TICK,
            ]
        )

lbs = [
    ("lb_agbveurne_btw_sporthal_1_15m_2025", "AGB Veurne BTW sporthal dispute 1.15m+", 1150092, 9.0, 7.5, 4.0, 6.8, "BTW FOI residual CRITICAL"),
    ("lb_agbveurne_gecorr_afm_neg_0_29m_2025", "AGB Veurne gecorr AFM -0.29m NEG", 289384, 8.5, 4.0, 3.0, 5.2, "AFM FOI residual CRITICAL"),
    ("lb_agbveurne_fin_debt_prefin_4_49m_2025", "AGB Veurne fin debt prefin 4.49m", 4488526, 8.0, 7.0, 3.0, 6.0, "Debt FOI residual"),
    ("lb_agbveurne_cum_pnl_neg_9_28m_2025", "AGB Veurne cum P&L NEG -9.28m", 9284891, 8.5, 8.0, 3.0, 6.5, "Equity path FOI residual"),
    ("lb_agbveurne_st_nonruil_recv_1_25m_2025", "AGB Veurne ST non-ruil recv 1.25m FOI", 1254751, 7.0, 6.5, 3.0, 5.5, "Recv FOI residual"),
    ("lb_agbveurne_assets_14_03m_2025", "AGB Veurne assets 14.03m Entity II", 14033664, 6.0, 8.0, 3.0, 5.7, "Map residual shell"),
    ("lb_agbveurne_invest_underspend_2025", "AGB Veurne invest underspend vs MJP 0.68m", 678241, 7.5, 5.5, 3.0, 5.3, "Invest FOI residual"),
    ("lb_agbveurne_pnl_neg_0_47m_2025", "AGB Veurne PnL -0.47m", 468292, 6.5, 4.5, 3.0, 4.7, "Monitor residual loss"),
]
tco = "JR2025 Entity II dual residual VL strong primary BBC BTW sporthal/prefin/gecorr AFM NEG AGB Veurne"
with open(ROOT / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for iid, name, cost, absu, cost_s, diff, prio, cut in lbs:
        w.writerow(
            [
                iid,
                name,
                "L5",
                "local_budget_line",
                "Vlaanderen>Gemeenten>Veurne>AGB_Veurne_L5",
                cost,
                cost,
                tco,
                "strong",
                SRC,
                "Veurne residents",
                "Local dual residual map VL JR2025 AGB Veurne",
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
            "Vlaanderen>Gemeenten>Veurne>AGB_Veurne>btw_sporthal_gecorr_afm_prefin_L5",
            ENT,
            "BTW sporthal dispute status (1.150m principal + 0.115m boeten + 0.184m intresten appeal); "
            "new BTW PV 0.044m+10pct; city prefin/loan schedule remaining fin debt 4.489m "
            "(new 0.360m amort 0.487m); gecorr AFM -0.289m path (aangewezen 0.369m); "
            "ST non-ruil recv 1.255m composition; LT ruil recv 1.228m; invest underspend "
            "Proostdijk MJP 0.679m vs 0.001m; retributie jump 0.488m composition; cum P&L -9.285m recovery",
            "Entity II dual residual: development/sport AGB with deep cum losses, NEG gecorr AFM, "
            "capitalised city prefin debt, and material open BTW litigation on sporthal after city GE already mined",
            9,
            "Stad / AGB Veurne",
            "financien@veurne.be",
            "Sint-Denisplaats 16 8630 Veurne",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-07",
            "",
            "",
            "",
            "",
            "comm_agbveurne_btw_sporthal_1_15m_2025",
            "lb_agbveurne_btw_sporthal_1_15m_2025",
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
        if row["task_id"] == "rq_1159":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                (row.get("notes") or "")
                + f" | {TICK} AGB Veurne JR2025 dual residual full BBC; FOI {GAP}"
            )
            row["entity_id"] = ENT
            row["hierarchy_target"] = "Vlaanderen>Gemeenten>Veurne>AGB_Veurne"
        rows.append(row)
ids = {row["task_id"] for row in rows}
if "rq_1160" not in ids:
    rows.append(
        {
            "task_id": "rq_1160",
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
            "notes": f"spawned by {TICK}; next residual dual L5 after AGB Veurne",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

print("budgets", len(budgets), "cmts", len(cmts), "lbs", len(lbs))
print("OK")

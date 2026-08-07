# tick1167: AGB Steenokkerzeel JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_steenokkerzeel_jr2025"
ENT = "agb_steenokkerzeel"
TICK = "tick1167"
UTC = "2026-08-08T01:00:00Z"
GAP = "gap_agb_steenokkerzeel_afm_neg_full_div_leasing_debt_l5"

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Steenokkerzeel Jaarrekening BBC 2025 RVB 30.04.2026 (106p)",
            "https://steenokkerzeel-echo.cipalschaubroeck.be/raadpleegomgeving/document/261142e3-69b5-48dc-a1f0-208fe69168c1",
            "AGB Steenokkerzeel / Gemeente Steenokkerzeel",
            "2026-08-08",
            "official_pdf",
            "Entity II dual residual; KBO 0863.139.949; AFM -5.3k gecorr -0.130m full div 0.052m "
            "leasing 1.536m fin debt 3.567m prijssub 0.244m; " + TICK,
        ]
    )

# city parent stub if missing
with open(ROOT / "entities.csv", encoding="utf-8", errors="replace", newline="") as f:
    ents = f.read()
if "city_steenokkerzeel" not in ents:
    with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "city_steenokkerzeel",
                "Gemeente Steenokkerzeel",
                "Commune de Steenokkerzeel",
                "Municipality of Steenokkerzeel",
                "municipality",
                "vlaanderen_gov",
                "nl",
                "https://www.steenokkerzeel.be",
                "info@steenokkerzeel.be",
                "Orchideeenlaan 17 / gemeentehuis 1820 Steenokkerzeel",
                "tick1167 residual: AGB JR2025 mined Entity II; city GE+OCMW JR2025 dual FOI not yet full BBC",
            ]
        )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Steenokkerzeel",
            "AGB Steenokkerzeel",
            "AGB Steenokkerzeel",
            "local_entity",
            "city_steenokkerzeel",
            "nl",
            "https://www.steenokkerzeel.be/thema/detail/3192/agb",
            "info@steenokkerzeel.be",
            "Orchideeenlaan 17 1820 Steenokkerzeel",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0863.139.949; assets 3.734m equity 0.074m (cap sub only cum P&L 0) cash 0.044m "
            "fin debt 3.567m leasing MVA 1.536m prijssub 0.244m BBR 0.070m AFM -0.005m "
            "gecorr AFM -0.130m NEG full div 0.052m; Secr Heidi Abeloos FD Luk Vandeuren; FOI "
            + GAP,
        ]
    )

budgets = [
    ("bud_agbstk_assets_2025", 3734002, "Assets balanstotaal YE2025 3.734m"),
    ("bud_agbstk_equity_2025", 73667, "Nettoactief YE2025 0.074m (cap subs only; cum P&L 0)"),
    ("bud_agbstk_cap_subs_2025", 73667, "Kapitaalssubsidies YE2025 0.074m = full equity"),
    ("bud_agbstk_debt_total_2025", 3660335, "Schulden total YE2025 3.660m"),
    ("bud_agbstk_fin_debt_2025", 3567197, "Fin schulden T4 total YE2025 3.567m (LT 3.417 + ST due 0.150)"),
    ("bud_agbstk_fin_debt_lt_2025", 3417499, "Fin schulden LT YE2025 3.417m"),
    ("bud_agbstk_fin_debt_st_due_2025", 149698, "Fin schulden LT vervallend YE2025 0.150m"),
    ("bud_agbstk_cash_2025", 44425, "Liquide middelen YE2025 0.044m DROP from 0.076m"),
    ("bud_agbstk_mva_2025", 3571092, "MVA YE2025 3.571m"),
    ("bud_agbstk_leasing_mva_2025", 1535582, "Leasing MVA gemeenschapsgoederen YE2025 1.536m"),
    ("bud_agbstk_mva_buildings_2025", 1943499, "MVA bedrijfsmatig gebouwen YE2025 1.943m"),
    ("bud_agbstk_expl_rec_2025", 557828, "Exploitatieontvangsten 0.558m"),
    ("bud_agbstk_expl_exp_2025", 433215, "Exploitatieuitgaven 0.433m"),
    ("bud_agbstk_expl_saldo_2025", 124613, "Exploitatiesaldo +0.125m"),
    ("bud_agbstk_prijssub_2025", 244340, "Prijssubsidie gemeente 0.244m"),
    ("bud_agbstk_invest_exp_2025", 520071, "Investeringsuitgaven 0.520m OVER vs MJP 0.128m"),
    ("bud_agbstk_invest_saldo_2025", -520071, "Investeringssaldo -0.520m"),
    ("bud_agbstk_fin_rec_2025", 520071, "Financieringsontvangsten/new loans 0.520m"),
    ("bud_agbstk_fin_exp_2025", 129876, "Periodieke aflossingen 0.130m"),
    ("bud_agbstk_fin_saldo_2025", 390194, "Financieringssaldo +0.390m"),
    ("bud_agbstk_new_loans_2025", 520071, "Nieuwe leningen T4 0.520m"),
    ("bud_agbstk_aflossingen_2025", 129876, "Aflossingen T4 0.130m"),
    ("bud_agbstk_budget_result_2025", -5264, "Budgettair resultaat boekjaar -0.005m"),
    ("bud_agbstk_bbr_2025", 69772, "BBR 0.070m"),
    ("bud_agbstk_afm_2025", -5264, "AFM -0.005m NEG"),
    ("bud_agbstk_afm_gecorr_2025", -129547, "Gecorr AFM -0.130m NEG CRITICAL (aangewezen 0.254m)"),
    ("bud_agbstk_pnl_2025", 52113, "P&L +0.052m"),
    ("bud_agbstk_dividend_2025", 52113, "Full dividend = PnL 0.052m to city"),
    ("bud_agbstk_interest_2025", 0, "Financiele kosten 0 FOI (interest blank)"),
    ("bud_agbstk_depr_2025", 128946, "Afschrijvingen 0.129m"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbstk_afm_neg_gecorr_0_13m_2025",
        "AGB Steenokkerzeel AFM -5k / gecorr -0.13m NEG",
        "AFM NEG; gecorr -0.130m; indicated amort 0.254m >> contractual 0.130m",
        129547,
    ),
    (
        "comm_agbstk_full_div_0_052m_2025",
        "AGB Steenokkerzeel full dividend 0.052m",
        "Full PnL paid; cum P&L equity 0; equity=cap subs only 0.074m",
        52113,
    ),
    (
        "comm_agbstk_leasing_mva_1_54m_2025",
        "AGB Steenokkerzeel leasing MVA 1.54m",
        "Leasing gemeenschapsgoederen 1.536m of 3.571m MVA",
        1535582,
    ),
    (
        "comm_agbstk_fin_debt_3_57m_2025",
        "AGB Steenokkerzeel fin debt 3.57m",
        "LT 3.417 + ST due 0.150; new 0.520 amort 0.130; zero interest P&L FOI",
        3567197,
    ),
    (
        "comm_agbstk_prijssub_0_24m_2025",
        "AGB Steenokkerzeel prijssub 0.24m",
        "City price subsidy 0.244m of expl rec 0.558m",
        244340,
    ),
    (
        "comm_agbstk_invest_over_0_52m_2025",
        "AGB Steenokkerzeel invest 0.52 vs MJP 0.13m",
        "Invest overspend financed by new loans 0.520m",
        520071,
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
                "AGB Steenokkerzeel / residents",
                "BBC JR2025 / DLB AGB",
                "2026-04-30",
                2025,
                2025,
                total,
                f'{{"2025":{total}}}',
                total,
                "active",
                "",
                goal,
                "FOI residual dual; review AFM/div/leasing/debt",
                SRC,
                "strong",
                "Vlaanderen>Gemeenten>Steenokkerzeel>AGB_Steenokkerzeel_L5",
                TICK,
            ]
        )

lbs = [
    ("lb_agbstk_gecorr_afm_neg_0_13m_2025", "AGB Steenokkerzeel gecorr AFM -0.13m NEG", 129547, 8.5, 3.5, 3.0, 5.0, "AFM FOI residual CRITICAL"),
    ("lb_agbstk_fin_debt_3_57m_2025", "AGB Steenokkerzeel fin debt 3.57m", 3567197, 7.5, 6.5, 3.0, 5.7, "Debt FOI residual"),
    ("lb_agbstk_leasing_mva_1_54m_2025", "AGB Steenokkerzeel leasing MVA 1.54m", 1535582, 8.0, 6.5, 3.0, 5.8, "Leasing FOI residual"),
    ("lb_agbstk_full_div_0_052m_2025", "AGB Steenokkerzeel full div 0.052m AFM NEG", 52113, 8.5, 3.0, 3.0, 4.9, "Dividend FOI residual CRITICAL"),
    ("lb_agbstk_prijssub_0_24m_2025", "AGB Steenokkerzeel prijssub 0.24m", 244340, 7.0, 4.0, 3.0, 4.7, "Prijssub FOI residual"),
    ("lb_agbstk_assets_3_73m_2025", "AGB Steenokkerzeel assets 3.73m Entity II", 3734002, 6.0, 6.5, 3.0, 5.1, "Map residual shell"),
    ("lb_agbstk_invest_over_0_52m_2025", "AGB Steenokkerzeel invest over 0.52m", 520071, 7.0, 5.5, 3.0, 5.1, "Invest FOI residual"),
]
tco = "JR2025 Entity II dual residual VL strong primary BBC AFM NEG full div leasing AGB Steenokkerzeel"
with open(ROOT / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for iid, name, cost, absu, cost_s, diff, prio, cut in lbs:
        w.writerow(
            [
                iid,
                name,
                "L5",
                "local_budget_line",
                "Vlaanderen>Gemeenten>Steenokkerzeel>AGB_Steenokkerzeel_L5",
                cost,
                cost,
                tco,
                "strong",
                SRC,
                "Steenokkerzeel residents",
                "Local dual residual map VL JR2025 AGB Steenokkerzeel",
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
            "Vlaanderen>Gemeenten>Steenokkerzeel>AGB_Steenokkerzeel>afm_neg_div_leasing_debt_L5",
            ENT,
            "AFM -5.264 and gecorr AFM -129.547 multi-year path (aangewezen 0.254m); full dividend 0.052m "
            "while AFM NEG and cum P&L equity 0 (equity=cap sub only 0.074m); leasing MVA 1.536m residual "
            "terms; fin debt 3.567m schedule lenders zero interest on P&L; prijssub 0.244m formula; "
            "invest overspend 0.520 vs MJP 0.128m funded by new loans; cash drop 0.076 to 0.044m; "
            "city GE+OCMW JR2025 dual FOI still open",
            "Entity II dual residual: culture/sport AGB with NEG AFM, full profit dividend, leasing shell "
            "and city prijssub; city GE not yet full BBC",
            8,
            "Gemeente / AGB Steenokkerzeel",
            "info@steenokkerzeel.be",
            "Orchideeenlaan 17 1820 Steenokkerzeel",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-08",
            "",
            "",
            "",
            "",
            "comm_agbstk_afm_neg_gecorr_0_13m_2025",
            "lb_agbstk_gecorr_afm_neg_0_13m_2025",
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
        if row["task_id"] == "rq_1167":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                (row.get("notes") or "")
                + f" | {TICK} AGB Steenokkerzeel JR2025 dual residual full BBC; FOI {GAP}"
            )
            row["entity_id"] = ENT
            row["hierarchy_target"] = "Vlaanderen>Gemeenten>Steenokkerzeel>AGB_Steenokkerzeel"
        rows.append(row)
ids = {row["task_id"] for row in rows}
if "rq_1168" not in ids:
    rows.append(
        {
            "task_id": "rq_1168",
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
            "notes": f"spawned by {TICK}; next residual dual L5 after AGB Steenokkerzeel",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

print("budgets", len(budgets), "cmts", len(cmts), "lbs", len(lbs), "OK")

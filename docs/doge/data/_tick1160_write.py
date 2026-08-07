# tick1160: AGB Zottegem JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_zottegem_jr2025"
ENT = "agb_zottegem"
TICK = "tick1160"
UTC = "2026-08-07T21:30:00Z"
GAP = "gap_agb_zottegem_prijssub_gecorr_afm_neg_leasing_debt_l5"

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Zottegem Jaarrekening 2025 BBC (216p) portal 9.06.2026",
            "https://zottegem.be/systems/file_download.ashx?pg=8240&ver=2",
            "AGB Zottegem / Stad Zottegem",
            "2026-08-07",
            "official_pdf",
            "Entity II dual residual; KBO 0807.465.117; kengetallen+J2/J4/J5/T4; "
            "prijssub 1.480m fin debt 11.450m gecorr AFM -0.408m leasing MVA 6.065m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Zottegem",
            "AGB Zottegem",
            "AGB Zottegem",
            "local_entity",
            "city_zottegem",
            "nl",
            "https://zottegem.be/jaarrekening",
            "info@zottegem.be",
            "Markt 1 / Gustaaf Schockaertstraat 7 9620 Zottegem",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0807.465.117 NIS 41081; assets 13.051m equity 0.981m cash 0.107m DROP "
            "fin debt 11.450m leasing MVA 6.065m prijssub 1.480m BBR 0.303m AFM -0.014m "
            "gecorr AFM -0.408m NEG PnL 0.044m full dividend; AD wnd Sandra De Roeck "
            "FD Marnic Fort Voorzitter Brecht Cassiman; FOI " + GAP,
        ]
    )

budgets = [
    ("bud_agbzot_assets_2025", 13051447, "Assets balanstotaal YE2025 13.051m"),
    ("bud_agbzot_equity_2025", 981412, "Nettoactief YE2025 0.981m"),
    ("bud_agbzot_cum_pnl_2025", 141738, "Gecumuleerd overschot YE2025 0.142m flat (full dividend)"),
    ("bud_agbzot_debt_total_2025", 12070035, "Schulden total YE2025 12.070m"),
    ("bud_agbzot_fin_debt_2025", 11450232, "Fin schulden T4 total YE2025 11.450m (LT 10.920 + ST due 0.530)"),
    ("bud_agbzot_fin_debt_lt_2025", 10920407, "Fin schulden LT YE2025 10.920m"),
    ("bud_agbzot_fin_debt_st_due_2025", 529825, "Fin schulden LT vervallend YE2025 0.530m"),
    ("bud_agbzot_cash_2025", 106796, "Liquide middelen YE2025 0.107m DROP from 0.558m YE2024"),
    ("bud_agbzot_mva_2025", 12257532, "MVA bedrijfsmatig YE2025 12.258m"),
    ("bud_agbzot_leasing_mva_2025", 6065375, "Leasing MVA YE2025 6.065m shell-heavy"),
    ("bud_agbzot_mva_buildings_2025", 5892071, "MVA terreinen/gebouwen YE2025 5.892m"),
    ("bud_agbzot_st_nonruil_recv_2025", 503879, "ST vorderingen niet-ruil YE2025 0.504m"),
    ("bud_agbzot_st_recv_total_2025", 646558, "ST vorderingen total YE2025 0.647m"),
    ("bud_agbzot_cap_subs_2025", 822369, "Kapitaalssubsidies YE2025 0.822m"),
    ("bud_agbzot_expl_rec_2025", 2344121, "Exploitatieontvangsten 2.344m"),
    ("bud_agbzot_expl_exp_2025", 1802979, "Exploitatieuitgaven 1.803m"),
    ("bud_agbzot_expl_saldo_2025", 541142, "Exploitatiesaldo +0.541m"),
    ("bud_agbzot_prijssub_2025", 1480460, "Prijssubsidie gemeente 1.480m (+0.135m vs budget; +6pct BTW city)"),
    ("bud_agbzot_personnel_2025", 586990, "Personeelskosten P&L 0.587m"),
    ("bud_agbzot_invest_exp_2025", 139900, "Investeringsuitgaven 0.140m (underspend vs MJP 1.395m)"),
    ("bud_agbzot_invest_saldo_2025", -139900, "Investeringssaldo -0.140m"),
    ("bud_agbzot_fin_rec_2025", 139900, "Financieringsontvangsten/new loans 0.140m"),
    ("bud_agbzot_fin_exp_2025", 555084, "Periodieke aflossingen 0.555m"),
    ("bud_agbzot_fin_saldo_2025", -415184, "Financieringssaldo -0.415m"),
    ("bud_agbzot_new_loans_2025", 139900, "Nieuwe leningen T4 0.140m"),
    ("bud_agbzot_aflossingen_2025", 555084, "Aflossingen T4 0.555m"),
    ("bud_agbzot_budget_result_2025", -13942, "Budgettair resultaat boekjaar -0.014m"),
    ("bud_agbzot_bbr_2025", 303462, "BBR 0.303m"),
    ("bud_agbzot_afm_2025", -13942, "AFM -0.014m NEG"),
    ("bud_agbzot_afm_gecorr_2025", -408091, "Gecorr AFM -0.408m NEG CRITICAL (aangewezen 0.949m)"),
    ("bud_agbzot_pnl_2025", 44155, "P&L winst 0.044m"),
    ("bud_agbzot_dividend_2025", 44155, "Uitgekeerd dividend = full profit 0.044m to city"),
    ("bud_agbzot_interest_2025", 72981, "Intresten leningen+leasing 0.073m"),
    ("bud_agbzot_depr_2025", 553712, "Afschrijvingen/voorzieningen 0.554m"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbzot_prijssub_1_48m_2025",
        "AGB Zottegem prijssubsidie city 1.48m",
        "City price subsidy sport/tourism AGB; +0.135m vs budget; +6pct BTW uplift to city",
        1480460,
    ),
    (
        "comm_agbzot_gecorr_afm_neg_0_41m_2025",
        "AGB Zottegem gecorr AFM -0.41m NEG",
        "Indicated amort 0.949m >> contractual 0.555m; structural debt service gap",
        408091,
    ),
    (
        "comm_agbzot_fin_debt_11_45m_2025",
        "AGB Zottegem fin debt 11.45m",
        "LT 10.920 + ST due 0.530; new 0.140; amort 0.555; Belfius interest unbudgeted note",
        11450232,
    ),
    (
        "comm_agbzot_leasing_mva_6_07m_2025",
        "AGB Zottegem leasing MVA 6.07m shell",
        "Leasing/soortgelijke rechten 6.065m of 12.258m MVA",
        6065375,
    ),
    (
        "comm_agbzot_dividend_full_pnl_2025",
        "AGB Zottegem full dividend = PnL 0.044m",
        "Full profit paid to city while AFM NEG and gecorr AFM DEEP NEG",
        44155,
    ),
    (
        "comm_agbzot_cash_drop_2025",
        "AGB Zottegem cash drop 0.56 to 0.11m",
        "Cash YE2024 0.558m to YE2025 0.107m",
        450905,
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
                "AGB Zottegem / Stad Zottegem residents",
                "BBC JR2025 / DLB AGB",
                "2026-06-09",
                2025,
                2025,
                total,
                f'{{"2025":{total}}}',
                total,
                "active",
                "",
                goal,
                "FOI residual dual; review prijssub/debt/leasing",
                SRC,
                "strong",
                "Vlaanderen>Gemeenten>Zottegem>AGB_Zottegem_L5",
                TICK,
            ]
        )

lbs = [
    ("lb_agbzot_prijssub_1_48m_2025", "AGB Zottegem prijssub city 1.48m", 1480460, 8.0, 7.0, 3.0, 6.0, "Prijssub FOI residual"),
    ("lb_agbzot_gecorr_afm_neg_0_41m_2025", "AGB Zottegem gecorr AFM -0.41m NEG", 408091, 8.5, 4.0, 3.0, 5.2, "AFM FOI residual CRITICAL"),
    ("lb_agbzot_fin_debt_11_45m_2025", "AGB Zottegem fin debt 11.45m", 11450232, 8.0, 8.0, 3.0, 6.3, "Debt FOI residual"),
    ("lb_agbzot_leasing_mva_6_07m_2025", "AGB Zottegem leasing MVA 6.07m shell", 6065375, 8.0, 7.5, 3.0, 6.2, "Leasing FOI residual"),
    ("lb_agbzot_assets_13_05m_2025", "AGB Zottegem assets 13.05m Entity II", 13051447, 6.0, 8.0, 3.0, 5.7, "Map residual shell"),
    ("lb_agbzot_dividend_full_pnl_2025", "AGB Zottegem full dividend=PnL 0.044m AFM NEG", 44155, 7.5, 3.5, 3.0, 4.7, "Dividend FOI residual"),
    ("lb_agbzot_cash_drop_2025", "AGB Zottegem cash drop to 0.11m", 106796, 7.0, 4.0, 3.0, 4.7, "Cash FOI residual"),
]
tco = "JR2025 Entity II dual residual VL strong primary BBC prijssub/leasing/gecorr AFM NEG AGB Zottegem"
with open(ROOT / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for iid, name, cost, absu, cost_s, diff, prio, cut in lbs:
        w.writerow(
            [
                iid,
                name,
                "L5",
                "local_budget_line",
                "Vlaanderen>Gemeenten>Zottegem>AGB_Zottegem_L5",
                cost,
                cost,
                tco,
                "strong",
                SRC,
                "Zottegem residents",
                "Local dual residual map VL JR2025 AGB Zottegem",
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
            "Vlaanderen>Gemeenten>Zottegem>AGB_Zottegem>prijssub_gecorr_afm_leasing_debt_L5",
            ENT,
            "Prijssubsidie formula 1.480m (+0.135m vs budget; city +6pct BTW uplift); gecorr AFM -0.408m path "
            "(aangewezen 0.949m); fin debt schedule 11.450m (LT 10.920 ST due 0.530 new 0.140 amort 0.555 Belfius); "
            "leasing MVA 6.065m residual terms; full dividend 0.044m while AFM NEG policy; cash drop 0.558 to 0.107m; "
            "ST non-ruil recv 0.504m; invest underspend MJP 1.395m vs 0.140m",
            "Entity II dual residual: sport/culture AGB with 1.48m city prijs subsidy, 11.45m debt, 6.07m leasing shell, "
            "NEG gecorr AFM and full profit dividend after city GE already mined",
            9,
            "Stad / AGB Zottegem",
            "info@zottegem.be",
            "Gustaaf Schockaertstraat 7 9620 Zottegem",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-07",
            "",
            "",
            "",
            "",
            "comm_agbzot_prijssub_1_48m_2025",
            "lb_agbzot_prijssub_1_48m_2025",
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
        if row["task_id"] == "rq_1160":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                (row.get("notes") or "")
                + f" | {TICK} AGB Zottegem JR2025 dual residual full BBC; FOI {GAP}"
            )
            row["entity_id"] = ENT
            row["hierarchy_target"] = "Vlaanderen>Gemeenten>Zottegem>AGB_Zottegem"
        rows.append(row)
ids = {row["task_id"] for row in rows}
if "rq_1161" not in ids:
    rows.append(
        {
            "task_id": "rq_1161",
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
            "notes": f"spawned by {TICK}; next residual dual L5 after AGB Zottegem",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

print("budgets", len(budgets), "cmts", len(cmts), "lbs", len(lbs), "OK")

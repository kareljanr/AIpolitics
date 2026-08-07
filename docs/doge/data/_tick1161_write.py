# tick1161: AGB Rumst JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_rumst_jr2025"
ENT = "agb_rumst"
TICK = "tick1161"
UTC = "2026-08-07T22:00:00Z"
GAP = "gap_agb_rumst_bbr_neg_prijssub_capital_lag_debt_l5"

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Rumst Jaarrekening 2025 BBC + RVB vaststelling 18.06.2026",
            "https://www.rumst.be/jaarrekening-2025-agb-rumst",
            "AGB Rumst / Gemeente Rumst",
            "2026-08-07",
            "official_pdf",
            "Entity II dual residual; KBO 0876.530.008; BBR -0.222m NEG capital lag 0.415m; "
            "prijssub 0.558m factor 11.47; fin debt 7.141m; MJP debt YE2026 9.07m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Rumst",
            "AGB Rumst",
            "AGB Rumst",
            "local_entity",
            "city_rumst",
            "nl",
            "https://www.rumst.be/jaarrekening-2025-agb-rumst",
            "info@rumst.be",
            "Koningin Astridplein 12 2840 Rumst",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0876.530.008; assets 7.808m equity 0.153m thin (cum P&L -0.334m) cash 0.024m "
            "thin fin debt 7.141m BBR -0.222m NEG capital lag 0.415m AFM +0.138m prijssub 0.558m "
            "factor 11.47 city loans invest 0.900m MJP debt YE2026 9.07m; AD Wouter De Smedt "
            "FD Michael Kerremans Voorzitter Jurgen Callaerts; FOI " + GAP,
        ]
    )

budgets = [
    ("bud_agbrumst_assets_2025", 7807526, "Assets balanstotaal YE2025 7.808m"),
    ("bud_agbrumst_equity_2025", 153234, "Nettoactief YE2025 0.153m THIN"),
    ("bud_agbrumst_cum_pnl_neg_2025", -334266, "Gecumuleerd tekort YE2025 -0.334m"),
    ("bud_agbrumst_debt_total_2025", 7654292, "Schulden total YE2025 7.654m"),
    ("bud_agbrumst_fin_debt_2025", 7140895, "Fin schulden T4 total YE2025 7.141m (LT 6.610 + ST due 0.531)"),
    ("bud_agbrumst_fin_debt_lt_2025", 6609904, "Fin schulden LT YE2025 6.610m"),
    ("bud_agbrumst_fin_debt_st_due_2025", 530991, "Fin schulden LT vervallend YE2025 0.531m"),
    ("bud_agbrumst_cash_2025", 23842, "Liquide middelen YE2025 0.024m THIN CRITICAL"),
    ("bud_agbrumst_mva_2025", 5621637, "MVA total YE2025 5.622m"),
    ("bud_agbrumst_lt_ruil_recv_2025", 1626763, "LT vorderingen ruil YE2025 1.627m (senior flats lease path)"),
    ("bud_agbrumst_st_lt_recv_due_2025", 322164, "LT vorderingen binnen jaar YE2025 0.322m"),
    ("bud_agbrumst_cap_subs_2025", 174367, "Kapitaalssubsidies YE2025 0.174m"),
    ("bud_agbrumst_overig_netto_2025", 313132, "Overig nettoactief YE2025 0.313m"),
    ("bud_agbrumst_expl_rec_2025", 726945, "Exploitatieontvangsten 0.727m"),
    ("bud_agbrumst_expl_exp_2025", 374593, "Exploitatieuitgaven 0.375m"),
    ("bud_agbrumst_expl_saldo_2025", 352352, "Exploitatiesaldo +0.352m"),
    ("bud_agbrumst_prijssub_2025", 557790, "Prijssubsidie gemeente 0.558m (factor 11.47 HIGH)"),
    ("bud_agbrumst_invest_exp_2025", 899529, "Investeringsuitgaven 0.900m (museum 0.592 + GAM 0.257 + sport 0.044)"),
    ("bud_agbrumst_invest_saldo_2025", -899529, "Investeringssaldo -0.900m"),
    ("bud_agbrumst_fin_rec_2025", 1215375, "Financieringsontvangsten 1.215m (city loans 0.900 + lease recovery 0.316)"),
    ("bud_agbrumst_fin_exp_2025", 530308, "Financieringsuitgaven 0.530m"),
    ("bud_agbrumst_fin_saldo_2025", 685068, "Financieringssaldo +0.685m"),
    ("bud_agbrumst_new_loans_2025", 899529, "Nieuwe leningen T4 0.900m (city for invest)"),
    ("bud_agbrumst_aflossingen_2025", 530158, "Aflossingen T4 0.530m (city 0.308 + Belfius 0.222)"),
    ("bud_agbrumst_lease_recovery_2025", 315847, "Terugvordering leasing seniorenflats Hoogvelden 0.316m"),
    ("bud_agbrumst_budget_result_2025", 137891, "Budgettair resultaat boekjaar +0.138m"),
    ("bud_agbrumst_bbr_2025", -222171, "BBR -0.222m NEG CRITICAL (capital increase 0.415m deferred to 2026)"),
    ("bud_agbrumst_capital_lag_2025", 415000, "Kapitaalsverhoging krediet overgedragen naar 2026 0.415m"),
    ("bud_agbrumst_afm_2025", 138041, "AFM +0.138m"),
    ("bud_agbrumst_afm_gecorr_2025", 126477, "Gecorr AFM +0.126m"),
    ("bud_agbrumst_pnl_2025", 19417, "P&L +0.019m"),
    ("bud_agbrumst_interest_2025", 85586, "Financiele kosten 0.086m"),
    ("bud_agbrumst_depr_2025", 339990, "Afschrijvingen/voorzieningen 0.340m"),
    ("bud_agbrumst_mjp_debt_2026", 9073370, "MJP fin debt YE2026 path 9.073m (new loans planned 2.550m)"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbrumst_bbr_neg_0_22m_2025",
        "AGB Rumst BBR -0.22m NEG capital lag",
        "BBR NEG due to deferred capital increase 0.415m rolled to 2026; prior cum -0.360m",
        222171,
    ),
    (
        "comm_agbrumst_prijssub_0_56m_factor_2025",
        "AGB Rumst prijssub 0.56m factor 11.47",
        "City price subsidy sport; high factor amplifies small rent swings; BTW 6pct city non-deductible",
        557790,
    ),
    (
        "comm_agbrumst_fin_debt_7_14m_2025",
        "AGB Rumst fin debt 7.14m city+Belfius",
        "LT 6.610 + ST due 0.531; city loans amort 0.308 + Belfius senior flats 0.222; new city 0.900",
        7140895,
    ),
    (
        "comm_agbrumst_capital_lag_0_42m_2025",
        "AGB Rumst capital increase lag 0.415m",
        "City-AGB capital raise credit deferred 2025->2026; drives BBR NEG",
        415000,
    ),
    (
        "comm_agbrumst_lt_recv_1_63m_2025",
        "AGB Rumst LT ruil recv 1.63m",
        "LT exchange receivables (senior flats lease path) + ST due 0.322m",
        1626763,
    ),
    (
        "comm_agbrumst_mjp_debt_ramp_2026",
        "AGB Rumst MJP debt YE2026 9.07m +2.55m new",
        "Planned new loans 2.550m in 2026; total fin debt path 9.073m",
        2550000,
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
                "AGB Rumst / Gemeente Rumst residents",
                "BBC JR2025 / DLB AGB",
                "2026-06-18",
                2025,
                2026,
                total,
                f'{{"2025":{total}}}',
                total,
                "active",
                "",
                goal,
                "FOI residual dual; review BBR/prijssub/debt/capital",
                SRC,
                "strong",
                "Vlaanderen>Gemeenten>Rumst>AGB_Rumst_L5",
                TICK,
            ]
        )

lbs = [
    ("lb_agbrumst_bbr_neg_0_22m_2025", "AGB Rumst BBR -0.22m NEG capital lag", 222171, 8.5, 4.0, 3.0, 5.2, "BBR FOI residual CRITICAL"),
    ("lb_agbrumst_prijssub_0_56m_2025", "AGB Rumst prijssub 0.56m factor 11.47", 557790, 8.0, 5.5, 3.0, 5.5, "Prijssub FOI residual"),
    ("lb_agbrumst_fin_debt_7_14m_2025", "AGB Rumst fin debt 7.14m city+Belfius", 7140895, 7.5, 7.0, 3.0, 5.8, "Debt FOI residual"),
    ("lb_agbrumst_capital_lag_0_42m_2025", "AGB Rumst capital increase lag 0.415m", 415000, 8.0, 4.5, 3.0, 5.2, "Capital FOI residual"),
    ("lb_agbrumst_assets_7_81m_2025", "AGB Rumst assets 7.81m Entity II", 7807526, 6.0, 7.0, 3.0, 5.3, "Map residual shell"),
    ("lb_agbrumst_lt_recv_1_63m_2025", "AGB Rumst LT ruil recv 1.63m FOI", 1626763, 6.5, 6.5, 3.0, 5.2, "Recv FOI residual"),
    ("lb_agbrumst_mjp_debt_ramp_2_55m_2026", "AGB Rumst MJP new loans 2.55m 2026", 2550000, 7.5, 6.5, 3.0, 5.7, "MJP debt FOI residual"),
    ("lb_agbrumst_cash_thin_0_02m_2025", "AGB Rumst cash 0.024m THIN", 23842, 7.5, 2.5, 3.0, 4.3, "Cash FOI residual"),
]
tco = "JR2025 Entity II dual residual VL strong primary BBC BBR NEG/prijssub/city debt AGB Rumst"
with open(ROOT / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for iid, name, cost, absu, cost_s, diff, prio, cut in lbs:
        w.writerow(
            [
                iid,
                name,
                "L5",
                "local_budget_line",
                "Vlaanderen>Gemeenten>Rumst>AGB_Rumst_L5",
                cost,
                cost,
                tco,
                "strong",
                SRC,
                "Rumst residents",
                "Local dual residual map VL JR2025 AGB Rumst",
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
            "Vlaanderen>Gemeenten>Rumst>AGB_Rumst>bbr_neg_prijssub_capital_debt_L5",
            ENT,
            "BBR -0.222m path and deferred capital increase 0.415m (timing city GR decision); "
            "prijssubsidie 0.558m formula factor 11.47 multi-year; fin debt schedule 7.141m "
            "(city loans amort 0.308 Belfius senior flats 0.222 new city 0.900); LT ruil recv 1.627m "
            "senior flats lease counterparties; MJP debt YE2026 9.073m new loans planned 2.550m; "
            "cash thin 0.024m liquidity; invest museum/GAM residual credits 0.362m rolled",
            "Entity II dual residual: leisure AGB with NEG BBR from capital lag, high-factor city "
            "prijssubsidie, city-loan invest shell and MJP debt ramp after city GE already mined",
            9,
            "Gemeente / AGB Rumst",
            "info@rumst.be",
            "Koningin Astridplein 12 2840 Rumst",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-07",
            "",
            "",
            "",
            "",
            "comm_agbrumst_bbr_neg_0_22m_2025",
            "lb_agbrumst_bbr_neg_0_22m_2025",
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
        if row["task_id"] == "rq_1161":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                (row.get("notes") or "")
                + f" | {TICK} AGB Rumst JR2025 dual residual full BBC; FOI {GAP}"
            )
            row["entity_id"] = ENT
            row["hierarchy_target"] = "Vlaanderen>Gemeenten>Rumst>AGB_Rumst"
        rows.append(row)
ids = {row["task_id"] for row in rows}
if "rq_1162" not in ids:
    rows.append(
        {
            "task_id": "rq_1162",
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
            "notes": f"spawned by {TICK}; next residual dual L5 after AGB Rumst",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

print("budgets", len(budgets), "cmts", len(cmts), "lbs", len(lbs), "OK")

# tick1164: AGB Zele JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_zele_jr2025"
ENT = "agb_zele"
TICK = "tick1164"
UTC = "2026-08-07T23:30:00Z"
GAP = "gap_agb_zele_gecorr_afm_neg_debt_11m_leasing_prijssub_l5"

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Zele Jaarrekening BBC 2025 (84p) gepubliceerd 29.04.2026 RVB 27.04.2026",
            "https://www.zele.be/file/download/42309/699D25E757AB8B17F88F6227A2927D93",
            "AGB Zele / Gemeente Zele",
            "2026-08-07",
            "official_pdf",
            "Entity II dual residual De Wiek/sport; KBO 0535.637.166; fin debt 11.242m "
            "gecorr AFM -0.124m leasing 3.703m prijssub 0.986m full div 0.166m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Zele",
            "AGB Zele",
            "AGB Zele",
            "local_entity",
            "city_zele",
            "nl",
            "https://www.zele.be/producten/detail/547/jaarrekening-agb",
            "justine.helaers@zele.be",
            "Markt 50 9240 Zele",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0535.637.166 NIS 42028; assets 12.959m equity 0.970m cash 0.754m "
            "fin debt 11.242m DECLINING leasing MVA 3.703m buildings 7.595m BBR 0.728m "
            "AFM +0.306m gecorr AFM -0.124m NEG prijssub 0.986m full div 0.166m; "
            "Voorzitter Thomas Bauwens; FOI " + GAP,
        ]
    )

budgets = [
    ("bud_agbzele_assets_2025", 12959488, "Assets balanstotaal YE2025 12.959m"),
    ("bud_agbzele_equity_2025", 970468, "Nettoactief YE2025 0.970m"),
    ("bud_agbzele_cum_pnl_2025", 170855, "Gecumuleerd overschot YE2025 0.171m flat (full dividend)"),
    ("bud_agbzele_cap_subs_2025", 799613, "Kapitaalssubsidies YE2025 0.800m"),
    ("bud_agbzele_debt_total_2025", 11989020, "Schulden total YE2025 11.989m"),
    ("bud_agbzele_fin_debt_2025", 11241602, "Fin schulden T4 total YE2025 11.242m DECLINING"),
    ("bud_agbzele_fin_debt_lt_2025", 10734613, "Fin schulden LT YE2025 10.735m"),
    ("bud_agbzele_fin_debt_st_due_2025", 506989, "Fin schulden LT vervallend YE2025 0.507m"),
    ("bud_agbzele_cash_2025", 754015, "Liquide middelen YE2025 0.754m"),
    ("bud_agbzele_mva_2025", 11929048, "MVA YE2025 11.929m"),
    ("bud_agbzele_mva_buildings_2025", 7594775, "MVA terreinen/gebouwen YE2025 7.595m"),
    ("bud_agbzele_leasing_mva_2025", 3703078, "Leasing MVA YE2025 3.703m shell"),
    ("bud_agbzele_st_nonruil_recv_2025", 221764, "ST vorderingen niet-ruil YE2025 0.222m"),
    ("bud_agbzele_expl_rec_2025", 1569517, "Exploitatieontvangsten 1.570m"),
    ("bud_agbzele_expl_exp_2025", 771119, "Exploitatieuitgaven 0.771m"),
    ("bud_agbzele_expl_saldo_2025", 798398, "Exploitatiesaldo +0.798m"),
    ("bud_agbzele_prijssub_2025", 986133, "Prijssubsidie gemeente 0.986m (P&S 7070000)"),
    ("bud_agbzele_invest_exp_2025", 208193, "Investeringsuitgaven 0.208m OVER vs MJP 0.047m"),
    ("bud_agbzele_invest_saldo_2025", -208193, "Investeringssaldo -0.208m"),
    ("bud_agbzele_fin_rec_2025", 208193, "Financieringsontvangsten/new loans 0.208m"),
    ("bud_agbzele_fin_exp_2025", 492123, "Periodieke aflossingen 0.492m"),
    ("bud_agbzele_fin_saldo_2025", -283931, "Financieringssaldo -0.284m"),
    ("bud_agbzele_new_loans_2025", 208193, "Nieuwe leningen T4 0.208m"),
    ("bud_agbzele_aflossingen_2025", 492123, "Aflossingen T4 0.492m"),
    ("bud_agbzele_budget_result_2025", 306275, "Budgettair resultaat boekjaar +0.306m"),
    ("bud_agbzele_bbr_2025", 728359, "BBR 0.728m"),
    ("bud_agbzele_afm_2025", 306275, "AFM +0.306m"),
    ("bud_agbzele_afm_gecorr_2025", -123644, "Gecorr AFM -0.124m NEG CRITICAL (aangewezen 0.922m)"),
    ("bud_agbzele_pnl_2025", 166440, "P&L winst 0.166m"),
    ("bud_agbzele_dividend_2025", 166440, "Uitgekeerd dividend = full profit 0.166m to city"),
    ("bud_agbzele_interest_2025", 6563, "Financiele kosten 0.007m"),
    ("bud_agbzele_depr_2025", 523156, "Afschrijvingen 0.523m"),
    ("bud_agbzele_vpb_2025", 33856, "Vennootschapsbelasting first-time 0.034m"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbzele_gecorr_afm_neg_0_12m_2025",
        "AGB Zele gecorr AFM -0.12m NEG",
        "Indicated amort 0.922m >> contractual 0.492m; structural debt service gap",
        123644,
    ),
    (
        "comm_agbzele_fin_debt_11_24m_2025",
        "AGB Zele fin debt 11.24m declining",
        "LT 10.735 + ST due 0.507; new 0.208 amort 0.492 De Wiek/sport plant",
        11241602,
    ),
    (
        "comm_agbzele_leasing_mva_3_70m_2025",
        "AGB Zele leasing MVA 3.70m shell",
        "Leasing 3.703m of 11.929m MVA; buildings 7.595m",
        3703078,
    ),
    (
        "comm_agbzele_prijssub_0_99m_2025",
        "AGB Zele prijssub city 0.99m",
        "City price subsidy De Wiek tickets; factor revisable 2x/yr; city bears risk note",
        986133,
    ),
    (
        "comm_agbzele_full_div_0_17m_2025",
        "AGB Zele full dividend 0.166m",
        "Full PnL to city while gecorr AFM NEG",
        166440,
    ),
    (
        "comm_agbzele_invest_over_mjp_2025",
        "AGB Zele invest 0.208 vs MJP 0.047m",
        "Invest overspend vs MJP end budget",
        208193,
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
                "AGB Zele / Gemeente Zele residents",
                "BBC JR2025 / DLB AGB",
                "2026-04-27",
                2025,
                2025,
                total,
                f'{{"2025":{total}}}',
                total,
                "active",
                "",
                goal,
                "FOI residual dual; review debt/AFM/leasing/prijssub",
                SRC,
                "strong",
                "Vlaanderen>Gemeenten>Zele>AGB_Zele_L5",
                TICK,
            ]
        )

lbs = [
    ("lb_agbzele_fin_debt_11_24m_2025", "AGB Zele fin debt 11.24m declining", 11241602, 8.0, 8.0, 3.0, 6.3, "Debt FOI residual"),
    ("lb_agbzele_gecorr_afm_neg_0_12m_2025", "AGB Zele gecorr AFM -0.12m NEG", 123644, 8.5, 3.5, 3.0, 5.0, "AFM FOI residual CRITICAL"),
    ("lb_agbzele_leasing_mva_3_70m_2025", "AGB Zele leasing MVA 3.70m shell", 3703078, 8.0, 6.5, 3.0, 5.8, "Leasing FOI residual"),
    ("lb_agbzele_prijssub_0_99m_2025", "AGB Zele prijssub city 0.99m", 986133, 7.5, 5.5, 3.0, 5.3, "Prijssub FOI residual"),
    ("lb_agbzele_assets_12_96m_2025", "AGB Zele assets 12.96m Entity II", 12959488, 6.0, 8.0, 3.0, 5.7, "Map residual shell"),
    ("lb_agbzele_full_div_0_17m_2025", "AGB Zele full div 0.166m gecorr AFM NEG", 166440, 7.5, 3.5, 3.0, 4.7, "Dividend FOI residual"),
    ("lb_agbzele_vpb_first_0_03m_2025", "AGB Zele first VPB 0.034m", 33856, 6.0, 2.5, 3.0, 3.7, "Monitor residual tax"),
]
tco = "JR2025 Entity II dual residual VL strong primary BBC debt/leasing/gecorr AFM NEG AGB Zele De Wiek"
with open(ROOT / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for iid, name, cost, absu, cost_s, diff, prio, cut in lbs:
        w.writerow(
            [
                iid,
                name,
                "L5",
                "local_budget_line",
                "Vlaanderen>Gemeenten>Zele>AGB_Zele_L5",
                cost,
                cost,
                tco,
                "strong",
                SRC,
                "Zele residents",
                "Local dual residual map VL JR2025 AGB Zele",
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
            "Vlaanderen>Gemeenten>Zele>AGB_Zele>gecorr_afm_debt_leasing_prijssub_L5",
            ENT,
            "Gecorr AFM -0.124m path (aangewezen 0.922m vs contractual 0.492m); fin debt schedule "
            "11.242m (LT 10.735 ST due 0.507 new 0.208 amort 0.492 lenders); leasing MVA 3.703m "
            "De Wiek residual; prijssubsidie 0.986m formula factor multi-year (2x/yr revise); "
            "full dividend 0.166m while gecorr AFM NEG; invest overspend 0.208 vs MJP 0.047m; "
            "first-time VPB 0.034m",
            "Entity II dual residual: leisure AGB De Wiek/sport with 11.2m debt, 3.7m leasing, "
            "NEG gecorr AFM and 0.99m city prijssub after city GE already mined",
            9,
            "Gemeente / AGB Zele",
            "justine.helaers@zele.be",
            "Markt 50 9240 Zele",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-07",
            "",
            "",
            "",
            "",
            "comm_agbzele_gecorr_afm_neg_0_12m_2025",
            "lb_agbzele_fin_debt_11_24m_2025",
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
        if row["task_id"] == "rq_1164":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                (row.get("notes") or "")
                + f" | {TICK} AGB Zele JR2025 dual residual full BBC; FOI {GAP}"
            )
            row["entity_id"] = ENT
            row["hierarchy_target"] = "Vlaanderen>Gemeenten>Zele>AGB_Zele"
        rows.append(row)
ids = {row["task_id"] for row in rows}
if "rq_1165" not in ids:
    rows.append(
        {
            "task_id": "rq_1165",
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
            "notes": f"spawned by {TICK}; next residual dual L5 after AGB Zele",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

print("budgets", len(budgets), "cmts", len(cmts), "lbs", len(lbs), "OK")

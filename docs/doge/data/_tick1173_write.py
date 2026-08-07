# tick1173: AGB Sport Actief Mechelen (SAM) JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_sam_mechelen_jr2025"
ENT = "agb_sam_mechelen"
TICK = "tick1173"
UTC = "2026-08-08T04:00:00Z"
GAP = "gap_agb_sam_gecorr_afm_neg_div_gt_pnl_debt_18m_l5"
URL = "https://www.mechelen.be/sites/default/files/agb-sam/files/2026-06/AGB%20SAM%20-%20REKENINGEN%202025%20BBC.pdf"

csv.field_size_limit(10_000_000)

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Sport Actief Mechelen (SAM) Jaarrekening BBC 2025 (80p) primary",
            URL,
            "AGB SAM / Stad Mechelen",
            "2026-08-08",
            "official_pdf",
            "Entity II dual residual; KBO 0871.106.718; assets 20.434m fin debt 18.054m "
            "city loans gecorr AFM -0.063m dividend 0.400m > PnL 0.331m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Sport Actief Mechelen (SAM)",
            "AGB Sport Actief Malines",
            "AGB Sport Actief Mechelen (SAM)",
            "local_entity",
            "city_mechelen",
            "nl",
            "https://www.mechelen.be/stad-en-bestuur/stadsbestuur-en-organisatie/bekendmakingen-verslagen-en-documenten/agb-sam-documenten",
            "onthaal@mechelen.be",
            "Grote Markt 21 2800 Mechelen",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0871.106.718; sport AGB; assets 20.434m equity 0.668m cash 0.299m JUMP "
            "fin debt 18.054m city loans (LT 16.670 + ST due 1.384) DECLINING pension prov JUMP "
            "0.251m BBR 0.343m AFM +0.125m gecorr AFM -0.063m NEG PnL +0.331m dividend 0.400m "
            "> PnL personnel 1.598m; Ragheno/Vrijbroek deferred; FOI " + GAP,
        ]
    )

budgets = [
    ("bud_agbsam_assets_2025", 20433985, "Assets balanstotaal YE2025 20.434m DROP from 22.071m"),
    ("bud_agbsam_equity_2025", 668253, "Nettoactief YE2025 0.668m DROP from 0.758m"),
    ("bud_agbsam_cum_pnl_2025", 71278, "Gecumuleerd overschot YE2025 0.071m DROP from 0.140m"),
    ("bud_agbsam_cap_subs_2025", 446975, "Kapitaalssubsidies YE2025 0.447m"),
    ("bud_agbsam_other_netto_2025", 150000, "Overig nettoactief YE2025 0.150m"),
    ("bud_agbsam_debt_total_2025", 19765732, "Schulden total YE2025 19.766m"),
    ("bud_agbsam_fin_debt_2025", 18053998, "Fin schulden T4 total YE2025 18.054m city loans DECLINING"),
    ("bud_agbsam_fin_debt_lt_2025", 16670060, "Fin schulden LT YE2025 16.670m"),
    ("bud_agbsam_fin_debt_st_due_2025", 1383938, "Fin schulden LT vervallend YE2025 1.384m"),
    ("bud_agbsam_cash_2025", 299313, "Liquide middelen YE2025 0.299m JUMP from 0.076m"),
    ("bud_agbsam_mva_2025", 19054431, "MVA YE2025 19.054m"),
    ("bud_agbsam_mva_buildings_2025", 18886996, "MVA terreinen/gebouwen YE2025 18.887m"),
    ("bud_agbsam_st_nonruil_recv_2025", 767249, "ST vorderingen niet-ruil YE2025 0.767m"),
    ("bud_agbsam_pension_prov_2025", 250528, "Pension provisie LT YE2025 0.251m JUMP from 0.132m"),
    ("bud_agbsam_expl_rec_2025", 5578813, "Exploitatieontvangsten 5.579m"),
    ("bud_agbsam_expl_exp_2025", 4087968, "Exploitatieuitgaven 4.088m (excl dividend in T2 C)"),
    ("bud_agbsam_expl_saldo_2025", 1490845, "Exploitatiesaldo +1.491m"),
    ("bud_agbsam_omzet_werking_2025", 5421131, "Ontvangsten uit de werking T2 5.421m (incl prijs dual)"),
    ("bud_agbsam_personnel_2025", 1597961, "Personeelsuitgaven 1.598m"),
    ("bud_agbsam_invest_exp_2025", 199904, "Investeringsuitgaven 0.200m OVER vs MJP 0.038m"),
    ("bud_agbsam_invest_saldo_2025", -199904, "Investeringssaldo -0.200m"),
    ("bud_agbsam_repay_2025", 1365593, "Periodieke aflossingen city loans 1.366m"),
    ("bud_agbsam_fin_saldo_2025", -1362593, "Financieringssaldo -1.363m"),
    ("bud_agbsam_budget_result_2025", -71651, "Budgettair resultaat boekjaar -0.072m"),
    ("bud_agbsam_bbr_2025", 343430, "Beschikbaar BBR YE2025 0.343m"),
    ("bud_agbsam_afm_2025", 125252, "AFM +0.125m"),
    ("bud_agbsam_afm_gecorr_2025", -62722, "Gecorr AFM -0.063m NEG (aangewezen 1.554m)"),
    ("bud_agbsam_aangewezen_amort_2025", 1553567, "Gecorrigeerde aflossingen o.b.v. fin schulden 1.554m"),
    ("bud_agbsam_pnl_2025", 331084, "P&L +0.331m"),
    ("bud_agbsam_dividend_2025", 400000, "Dividend to city 0.400m > PnL 0.331m CRITICAL"),
    ("bud_agbsam_interest_2025", 6667, "Financiele kosten 0.007m thin (city loans)"),
    ("bud_agbsam_depr_2025", 1556349, "Afschrijvingen 1.556m"),
    ("bud_agbsam_mjp_debt_2026", 15823565, "MJP fin debt YE2026 path 15.824m"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbsam_city_loan_18_1m_2025",
        "AGB SAM Mechelen city loan debt 18.1m",
        "All loans from Stad Mechelen; city borg per risk note",
        18053998,
    ),
    (
        "comm_agbsam_gecorr_afm_neg_0_06m_2025",
        "AGB SAM Mechelen gecorr AFM -0.06m NEG",
        "Indicated amort 1.554m >> contractual 1.366m; thin AFM masks NEG gecorr",
        62722,
    ),
    (
        "comm_agbsam_div_gt_pnl_0_40m_2025",
        "AGB SAM dividend 0.40m > PnL 0.33m",
        "Over-distribution vs book profit; cum P&L DROP",
        400000,
    ),
    (
        "comm_agbsam_personnel_1_60m_2025",
        "AGB SAM personnel 1.60m",
        "Own staff shell sport ops dual residual",
        1597961,
    ),
    (
        "comm_agbsam_pension_jump_0_25m_2025",
        "AGB SAM pension prov JUMP 0.25m",
        "LT pension provision 0.132->0.251m",
        250528,
    ),
    (
        "comm_agbsam_repay_1_37m_2025",
        "AGB SAM loan repay 1.37m 2025",
        "Periodieke aflossingen city loans",
        1365593,
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
                "2026-06-10",
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
                "Vlaanderen>Gemeenten>Mechelen>AGB_SAM",
                TICK,
            ]
        )

lbs = [
    ("lb_agbsam_city_loan_18_1m_2025", "AGB SAM Mechelen city loan debt 18.1m", 18053998, 7.5, 7.5, 3.0, "City loan FOI residual"),
    ("lb_agbsam_gecorr_afm_neg_0_06m_2025", "AGB SAM gecorr AFM -0.06m NEG", 62722, 8.5, 3.5, 3.0, "AFM path FOI residual"),
    ("lb_agbsam_div_gt_pnl_0_40m_2025", "AGB SAM dividend 0.40m > PnL", 400000, 9.0, 4.0, 3.0, "Dividend FOI residual"),
    ("lb_agbsam_assets_20_4m_2025", "AGB SAM assets 20.4m Entity II", 20433985, 5.5, 7.5, 3.0, "Map residual"),
    ("lb_agbsam_personnel_1_60m_2025", "AGB SAM personnel 1.60m", 1597961, 6.5, 6.0, 3.0, "Staff FOI residual"),
    ("lb_agbsam_pension_jump_0_25m_2025", "AGB SAM pension JUMP 0.25m", 250528, 7.5, 4.5, 3.0, "Pension FOI residual"),
    ("lb_agbsam_repay_1_37m_2025", "AGB SAM repay 1.37m", 1365593, 6.0, 6.0, 3.0, "Amort FOI residual"),
    ("lb_agbsam_pnl_0_33m_2025", "AGB SAM PnL +0.33m", 331084, 5.5, 4.0, 3.0, "Monitor residual"),
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
                "Vlaanderen>Gemeenten>Mechelen>AGB_SAM_L5",
                cost,
                cost,
                "JR2025 Entity II dual residual VL strong primary BBC city loan gecorr AFM NEG div>PnL",
                "strong",
                SRC,
                "Mechelen residents / sport users",
                "Local dual residual map VL JR2025 AGB SAM",
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
            "Vlaanderen>Gemeenten>Mechelen>AGB_SAM>city_loan_div_afm_L5",
            ENT,
            "City loan schedule behind fin debt 18.054m (ST due 1.384m); recon gecorr AFM -0.063m "
            "vs AFM +0.125m and indicated amort 1.554m; dividend 0.400m > PnL 0.331m legal/BTW "
            "winstoogmerk basis and multi-year policy; prijssubsidie/factor embedded in werking "
            "5.421m cash-by-year; pension JUMP 0.132->0.251m actuarial; Ragheno + Vrijbroek "
            "deferred capex residual; beheersovereenkomst GR 16.12.2025 full text",
            "Entity II sport AGB dual residual: EUR18m city-debt shell with dividend exceeding "
            "book profit and NEG gecorr AFM after city GE + Energiepunt dual already mapped",
            9,
            "Stad / AGB SAM Mechelen",
            "onthaal@mechelen.be",
            "Grote Markt 21 2800 Mechelen",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-08",
            "",
            "",
            "",
            "",
            "comm_agbsam_city_loan_18_1m_2025|comm_agbsam_div_gt_pnl_0_40m_2025",
            "lb_agbsam_city_loan_18_1m_2025|lb_agbsam_div_gt_pnl_0_40m_2025|lb_agbsam_gecorr_afm_neg_0_06m_2025",
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
        if row["task_id"] == "rq_1173":
            row["status"] = "done"
            row["entity_id"] = ENT
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick1173 AGB SAM Mechelen JR2025 Entity II dual residual; city loan 18.1m "
                "gecorr AFM NEG div>PnL; FOI " + GAP
            )
        rows.append(row)
if not any(r["task_id"] == "rq_1174" for r in rows):
    rows.append(
        {
            "task_id": "rq_1174",
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
            "notes": "spawned by tick1173; next residual dual L5 after AGB SAM Mechelen",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print("tick1173 write OK", len(budgets), "budgets", len(cmts), "cmts", len(lbs), "lbs")

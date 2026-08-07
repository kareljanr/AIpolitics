# tick1178: AGB Patrimonium Scherpenheuvel-Zichem JR2025 Entity II dual residual
# Primary: RVB extract 30.03.2026 + city GE consol J2 (AGB lines) + dual flows in city JR2025
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_sz_patrimonium_jr2025"
ENT = "agb_scherpenheuvel_zichem"
TICK = "tick1178"
UTC = "2026-08-08T06:30:00Z"
GAP = "gap_agb_sz_afm_neg_full_bbc_debt_prijssub_leasing_l5"
URL_EXTRACT = "https://www.scherpenheuvel-zichem.be/sites/default/files/2026-04/20260330-Jaarrekening-2025.pdf"
URL_CITY = "https://visit.scherpenheuvel-zichem.be/sites/default/files/2026-06/Jaarrekening-2025.pdf"

csv.field_size_limit(10_000_000)

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Patrimonium SZ JR2025: RVB extract 30.03.2026 + city consol J2 dual flows",
            URL_EXTRACT,
            "AGB Patrimonium / Stad Scherpenheuvel-Zichem",
            "2026-08-08",
            "official_pdf",
            "Entity II dual residual; BBR 1.144m AFM -0.048m NEG gecorr -0.005m NBB PnL 0.851m "
            "div 0.200m prijssub 0.486m city loan 0.153m leasing 0.859m; full BBC balance FOI; "
            + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Patrimonium Scherpenheuvel-Zichem",
            "AGB Patrimoine Scherpenheuvel-Zichem",
            "AGB Patrimonium Scherpenheuvel-Zichem",
            "local_entity",
            "city_scherpenheuvel_zichem",
            "nl",
            "https://www.scherpenheuvel-zichem.be",
            "info@scherpenheuvel-zichem.be",
            "August Nihoulstraat 13 3270 Scherpenheuvel",
            "JR2025 Entity II dual residual "
            + TICK
            + "; RVB 30.03.2026; BBR 1.144m AFM -0.048m NEG (city consol) gecorr AFM -0.005m NEG "
            "NBB profit 0.851m dividend 0.200m; city prijssub 0.486m; city renteloze lening 0.153m "
            "(vs MJP 1.440m UNDER); recovery 0.293m; leasing vergoeding shell 0.859m BTW-lek; "
            "full BBC assets/debt FOI; Secr Bruno Claes Voorzitter Kris Peetermans; FOI " + GAP,
        ]
    )

# Strong primary figures only — no invented balance sheet totals
budgets = [
    ("bud_agbsz_bbr_2025", 1143679, "Beschikbaar BBR YE2025 1.144m (RVB extract + city consol J2)"),
    ("bud_agbsz_afm_2025", -47592, "AFM -0.048m NEG (city consol J2 AGB line; RVB extract wording said positive 47.592)"),
    ("bud_agbsz_afm_gecorr_2025", -5255, "Gecorr AFM -0.005m NEG (city consol J2 AGB line)"),
    ("bud_agbsz_pnl_nbb_2025", 851259, "NBB te bestemmen winst 0.851m (RVB extract)"),
    ("bud_agbsz_dividend_2025", 200000, "Dividend to city 0.200m (RVB extract + city fin receipt)"),
    ("bud_agbsz_prijssub_city_2025", 485866, "Prijssubsidie van stad 0.486m (city T2 dual)"),
    ("bud_agbsz_city_loan_new_2025", 153364, "City toegestane lening to AGB 0.153m UNDER vs MJP 1.440m"),
    ("bud_agbsz_city_loan_recover_2025", 292643, "City periodieke terugvordering van AGB 0.293m"),
    ("bud_agbsz_leasing_fee_shell_2025", 859070, "Leasingvergoedingen via AGB 0.859m (nuloperatie city dual BTW)"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        conf = "strong" if "consol" in notes.lower() or "RVB" in notes or "city T2" in notes or "extract" in notes else "strong"
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 dual primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbsz_afm_neg_0_05m_2025",
        "AGB SZ Patrimonium AFM -0.05m NEG",
        "City consol J2 AGB line; dual residual after city GE tick1038",
        47592,
    ),
    (
        "comm_agbsz_dividend_0_20m_2025",
        "AGB SZ dividend 0.20m of NBB profit 0.85m",
        "Large dividend while AFM NEG dual residual",
        200000,
    ),
    (
        "comm_agbsz_prijssub_0_49m_2025",
        "AGB SZ prijssubsidie 0.49m city dual",
        "Ticket-linked prijs subsidy + 6pct non-deductible BTW lek",
        485866,
    ),
    (
        "comm_agbsz_city_loan_under_0_15m_2025",
        "AGB SZ city loan 0.15m UNDER vs MJP 1.44m",
        "Invest underspend residual dual",
        153364,
    ),
    (
        "comm_agbsz_leasing_shell_0_86m_2025",
        "AGB SZ leasing fee shell 0.86m",
        "City pays AGB rent = lease recovery; BTW spread 15y",
        859070,
    ),
    (
        "comm_agbsz_bbr_1_14m_2025",
        "AGB SZ BBR 1.14m",
        "Healthy BBR stock dual residual",
        1143679,
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
                "BBC JR2025 dual primary",
                "2026-03-30",
                2025,
                2025,
                env,
                f"{{2025:{env}}}",
                0,
                "active",
                URL_EXTRACT,
                goal,
                "Entity II FOI residual",
                SRC,
                "strong",
                "Vlaanderen>Gemeenten>Scherpenheuvel-Zichem>AGB",
                TICK,
            ]
        )

lbs = [
    ("lb_agbsz_afm_neg_0_05m_2025", "AGB SZ AFM -0.05m NEG", 47592, 8.0, 3.5, 3.0, "AFM FOI residual"),
    ("lb_agbsz_dividend_0_20m_while_afm_neg", "AGB SZ dividend 0.20m while AFM NEG", 200000, 8.5, 4.0, 3.0, "Dividend FOI residual"),
    ("lb_agbsz_prijssub_0_49m_2025", "AGB SZ prijssub 0.49m + BTW lek", 485866, 7.5, 5.0, 3.0, "Subsidy FOI residual"),
    ("lb_agbsz_leasing_shell_0_86m_2025", "AGB SZ leasing shell 0.86m", 859070, 7.0, 5.5, 3.0, "Lease FOI residual"),
    ("lb_agbsz_bbr_1_14m_2025", "AGB SZ BBR 1.14m", 1143679, 5.5, 6.0, 3.0, "Map residual"),
    ("lb_agbsz_pnl_nbb_0_85m_2025", "AGB SZ NBB profit 0.85m", 851259, 6.0, 5.5, 3.0, "Map residual"),
    ("lb_agbsz_city_loan_under_0_15m_2025", "AGB SZ city loan UNDER 0.15m", 153364, 6.5, 4.0, 3.0, "Invest FOI residual"),
    ("lb_agbsz_gecorr_afm_neg_0_005m_2025", "AGB SZ gecorr AFM -0.005m NEG", 5255, 7.5, 2.5, 3.0, "AFM FOI residual"),
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
                "Vlaanderen>Gemeenten>Scherpenheuvel-Zichem>AGB_L5",
                cost,
                cost,
                "JR2025 Entity II dual residual VL strong primary partial BBC (consol+RVB); full balance FOI",
                "strong",
                SRC,
                "Scherpenheuvel-Zichem residents / culture users",
                "Local dual residual map VL JR2025 AGB SZ",
                "RVB extract + city consol J2 dual flows primary",
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
            "Vlaanderen>Gemeenten>Scherpenheuvel-Zichem>AGB>full_bbc_debt_afm_l5",
            ENT,
            "Full BBC JR2025 (J2/J4/J5/T2/T4) PDF not on portal beyond RVB extract: assets equity cash "
            "fin debt schedule; recon AFM -47.592 vs RVB wording 'positieve' 47.592; multi-year AFM/gecorr "
            "path; city loan stock behind 0.153m new + recoveries 0.293m; prijssub 0.486m formula; "
            "leasing shell 0.859m contracts residual terms; dividend 0.200m while AFM NEG legal basis; "
            "invest underspend vs city MJP loan 1.440m",
            "Entity II patrimonium AGB dual residual after city GE tick1038: AFM NEG with large dividend "
            "and BTW-lek prijs/leasing dual; full balance/debt layer still FOI-only",
            9,
            "Stad / AGB Patrimonium Scherpenheuvel-Zichem",
            "info@scherpenheuvel-zichem.be",
            "August Nihoulstraat 13 3270 Scherpenheuvel",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-08",
            "",
            "",
            "",
            "",
            "comm_agbsz_afm_neg_0_05m_2025|comm_agbsz_dividend_0_20m_2025",
            "lb_agbsz_afm_neg_0_05m_2025|lb_agbsz_dividend_0_20m_while_afm_neg",
            UTC,
            UTC,
            TICK + "; ready not sent; full BBC PDF gap; do not send without human OK",
        ]
    )

rows = []
with open(ROOT / "research_queue.csv", "r", encoding="utf-8", errors="replace", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_1178":
            row["status"] = "done"
            row["entity_id"] = ENT
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick1178 AGB SZ Patrimonium JR2025 Entity II dual residual; AFM NEG div 0.20m "
                "prijssub 0.49m partial primary + FOI full BBC; FOI " + GAP
            )
        rows.append(row)
if not any(r["task_id"] == "rq_1179" for r in rows):
    rows.append(
        {
            "task_id": "rq_1179",
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
            "notes": "spawned by tick1178; next residual dual L5 after AGB Scherpenheuvel-Zichem",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print("tick1178 write OK", len(budgets), "budgets", len(cmts), "cmts", len(lbs), "lbs")

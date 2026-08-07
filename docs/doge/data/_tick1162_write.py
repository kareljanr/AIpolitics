# tick1162: AGB Energiepunt Mechelen JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_energiepunt_mechelen_jr2025"
ENT = "agb_energiepunt_mechelen"
TICK = "tick1162"
UTC = "2026-08-07T22:30:00Z"
GAP = "gap_agb_energiepunt_loanbook_9m_debt_onlend_vl_sub_l5"

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Energiepunt Mechelen Jaarrekening BBC 2025 (105p) RVB 5.05.2026",
            "https://www.mechelen.be/sites/default/files/agb-energiepunt/files/2026-05/Jaarrekening%202025%20AGB%20ENERGIEPUNT%20MECHELEN.pdf",
            "AGB Energiepunt Mechelen / Stad Mechelen",
            "2026-08-07",
            "official_pdf",
            "Entity II dual residual Energiehuis; KBO 0843.922.170; loanbook LT recv 8.496m "
            "fin debt 9.425m on-lend 3.159m VL sub 0.221m; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Energiepunt Mechelen",
            "AGB Energiepunt Malines",
            "AGB Energiepunt Mechelen",
            "local_entity",
            "city_mechelen",
            "nl",
            "https://www.mechelen.be/stad-en-bestuur/stadsbestuur-en-organisatie/bekendmakingen-verslagen-en-documenten/agb-energiepunt-documenten",
            "onthaal@mechelen.be",
            "Grote Markt 21 2800 Mechelen",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0843.922.170; Energiehuis VL; assets 9.777m equity 0.349m cash 0.406m "
            "LT citizen loans 8.496m fin debt 9.425m on-lend 3.159m recover 1.366m BBR 0.420m "
            "AFM +0.015m gecorr +0.760m VL werkingssub 0.221m; FOI " + GAP,
        ]
    )

budgets = [
    ("bud_agbepm_assets_2025", 9776573, "Assets balanstotaal YE2025 9.777m"),
    ("bud_agbepm_equity_2025", 348642, "Nettoactief YE2025 0.349m (cum P&L only)"),
    ("bud_agbepm_debt_total_2025", 9427931, "Schulden total YE2025 9.428m"),
    ("bud_agbepm_fin_debt_2025", 9424935, "Fin schulden T4 total YE2025 9.425m (LT 8.576 + ST due 0.849)"),
    ("bud_agbepm_fin_debt_lt_2025", 8576357, "Fin schulden LT YE2025 8.576m"),
    ("bud_agbepm_fin_debt_st_due_2025", 848578, "Fin schulden LT vervallend YE2025 0.849m"),
    ("bud_agbepm_cash_2025", 405671, "Liquide middelen YE2025 0.406m"),
    ("bud_agbepm_lt_loanbook_2025", 8496320, "LT vorderingen ruil YE2025 8.496m citizen energy loans"),
    ("bud_agbepm_st_loanbook_due_2025", 842976, "LT vorderingen binnen jaar YE2025 0.843m"),
    ("bud_agbepm_loanbook_total_2025", 9339296, "Total citizen loan book LT+ST due ~9.339m"),
    ("bud_agbepm_expl_rec_2025", 233048, "Exploitatieontvangsten 0.233m"),
    ("bud_agbepm_expl_exp_2025", 218961, "Exploitatieuitgaven 0.219m"),
    ("bud_agbepm_expl_saldo_2025", 14087, "Exploitatiesaldo +0.014m"),
    ("bud_agbepm_vl_sub_2025", 220901, "Specifieke werkingssubsidies VL 0.221m"),
    ("bud_agbepm_city_sub_2025", 2498, "Algemene werkingssubsidie stad 0.0025m"),
    ("bud_agbepm_subs_out_2025", 189989, "Toegestane werkingssubsidies out 0.190m (incl 50k doorstorting stad)"),
    ("bud_agbepm_fin_rec_2025", 4524949, "Financieringsontvangsten 4.525m (new debt 3.159 + recoveries 1.366)"),
    ("bud_agbepm_fin_exp_2025", 4523738, "Financieringsuitgaven 4.524m (amort 1.365 + on-lend 3.159)"),
    ("bud_agbepm_fin_saldo_2025", 1211, "Financieringssaldo +0.001m matched shell"),
    ("bud_agbepm_new_loans_2025", 3159109, "Nieuwe leningen opgenomen T4 3.159m"),
    ("bud_agbepm_onlend_2025", 3159109, "Toegestane leningen aan burgers 3.159m"),
    ("bud_agbepm_aflossingen_2025", 1364629, "Periodieke aflossingen 1.365m (incl MijnVerbouwlening +0.732m)"),
    ("bud_agbepm_recoveries_2025", 1365840, "Terugvordering toegestane leningen 1.366m"),
    ("bud_agbepm_budget_result_2025", 15297, "Budgettair resultaat boekjaar +0.015m"),
    ("bud_agbepm_bbr_2025", 419761, "BBR 0.420m"),
    ("bud_agbepm_afm_2025", 15297, "AFM +0.015m"),
    ("bud_agbepm_afm_gecorr_2025", 759769, "Gecorr AFM +0.760m (recoveries > indicated amort)"),
    ("bud_agbepm_pnl_2025", 14087, "P&L +0.014m"),
    ("bud_agbepm_mjp_debt_2026", 11660306, "MJP fin debt YE2026 path 11.660m (new 3.600m)"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbepm_loanbook_9_34m_2025",
        "AGB Energiepunt citizen loan book ~9.34m",
        "LT ruil recv 8.496m + ST due 0.843m energy renovation loans (MijnVerbouwlening path)",
        9339296,
    ),
    (
        "comm_agbepm_fin_debt_9_42m_2025",
        "AGB Energiepunt fin debt 9.42m on-lend shell",
        "Matched funding for citizen loans; new 3.159m; amort 1.365m; MJP YE2026 11.66m",
        9424935,
    ),
    (
        "comm_agbepm_onlend_3_16m_2025",
        "AGB Energiepunt on-lend new 3.16m",
        "Toegestane leningen aan burgers = new funding 3.159m matched shell",
        3159109,
    ),
    (
        "comm_agbepm_vl_sub_0_22m_2025",
        "AGB Energiepunt VL werkingssub 0.22m",
        "Specifieke werkingssubsidies Vlaamse overheid Energiehuis 0.221m",
        220901,
    ),
    (
        "comm_agbepm_mjp_debt_ramp_2026",
        "AGB Energiepunt MJP new loans 3.6m 2026",
        "Planned new funding 3.600m / on-lend 3.600m YE2026 debt 11.66m",
        3600000,
    ),
    (
        "comm_agbepm_subs_out_0_19m_2025",
        "AGB Energiepunt subsidies out 0.19m",
        "Toegestane werkingssubsidies 0.190m incl 50k doorstorting stad",
        189989,
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
                "Mechelen residents / energy renovators",
                "BBC JR2025 / VL Energielening / Energiehuis",
                "2026-05-05",
                2025,
                2026,
                total,
                f'{{"2025":{total}}}',
                total,
                "active",
                "",
                goal,
                "FOI residual dual; review loanbook/debt/VL",
                SRC,
                "strong",
                "Vlaanderen>Gemeenten>Mechelen>AGB_Energiepunt_L5",
                TICK,
            ]
        )

lbs = [
    ("lb_agbepm_loanbook_9_34m_2025", "AGB Energiepunt citizen loanbook 9.34m", 9339296, 7.5, 8.0, 3.0, 6.2, "Loanbook FOI residual"),
    ("lb_agbepm_fin_debt_9_42m_2025", "AGB Energiepunt fin debt 9.42m on-lend", 9424935, 7.5, 8.0, 3.0, 6.2, "Debt FOI residual"),
    ("lb_agbepm_onlend_3_16m_2025", "AGB Energiepunt on-lend new 3.16m", 3159109, 7.0, 6.5, 3.0, 5.5, "On-lend FOI residual"),
    ("lb_agbepm_assets_9_78m_2025", "AGB Energiepunt assets 9.78m Entity II", 9776573, 6.0, 8.0, 3.0, 5.7, "Map residual shell"),
    ("lb_agbepm_vl_sub_0_22m_2025", "AGB Energiepunt VL sub 0.22m", 220901, 5.5, 4.0, 3.0, 4.0, "Monitor VL Energiehuis"),
    ("lb_agbepm_mjp_debt_ramp_3_6m_2026", "AGB Energiepunt MJP new 3.6m 2026", 3600000, 7.0, 6.5, 3.0, 5.5, "MJP FOI residual"),
    ("lb_agbepm_subs_out_0_19m_2025", "AGB Energiepunt subsidies out 0.19m", 189989, 6.5, 3.5, 3.0, 4.3, "Subs out FOI residual"),
]
tco = "JR2025 Entity II dual residual VL strong primary BBC Energiehuis loanbook/on-lend AGB Energiepunt Mechelen"
with open(ROOT / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for iid, name, cost, absu, cost_s, diff, prio, cut in lbs:
        w.writerow(
            [
                iid,
                name,
                "L5",
                "local_budget_line",
                "Vlaanderen>Gemeenten>Mechelen>AGB_Energiepunt_L5",
                cost,
                cost,
                tco,
                "strong",
                SRC,
                "Mechelen residents",
                "Local dual residual map VL JR2025 AGB Energiepunt",
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
            "Vlaanderen>Gemeenten>Mechelen>AGB_Energiepunt>loanbook_onlend_debt_L5",
            ENT,
            "Citizen energy loan book composition LT 8.496m + ST due 0.843m (products MijnVerbouwlening etc; "
            "number loans default rates average rate maturity); funding sources of fin debt 9.425m "
            "(VEKA/VL/city/bank) residual schedule; matched on-lend 3.159m = new debt 3.159m policy; "
            "MJP YE2026 debt 11.66m +3.6m new; VL werkingssub 0.221m multi-year decision; subsidies out "
            "0.190m incl 50k doorstorting stad; recoveries 1.366m vs amort 1.365m reconciliation "
            "(+0.732m MijnVerbouwlening note)",
            "Entity II dual residual: pure Energiehuis on-lending shell with ~9.3m opaque citizen loan "
            "book stacked against 9.4m funding debt after city GE already mined",
            8,
            "Stad / AGB Energiepunt Mechelen",
            "onthaal@mechelen.be",
            "Grote Markt 21 2800 Mechelen",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-07",
            "",
            "",
            "",
            "",
            "comm_agbepm_loanbook_9_34m_2025",
            "lb_agbepm_loanbook_9_34m_2025",
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
        if row["task_id"] == "rq_1162":
            row["status"] = "done"
            row["updated_utc"] = UTC
            row["notes"] = (
                (row.get("notes") or "")
                + f" | {TICK} AGB Energiepunt Mechelen JR2025 dual residual full BBC; FOI {GAP}"
            )
            row["entity_id"] = ENT
            row["hierarchy_target"] = "Vlaanderen>Gemeenten>Mechelen>AGB_Energiepunt"
        rows.append(row)
ids = {row["task_id"] for row in rows}
if "rq_1163" not in ids:
    rows.append(
        {
            "task_id": "rq_1163",
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
            "notes": f"spawned by {TICK}; next residual dual L5 after AGB Energiepunt Mechelen",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

print("budgets", len(budgets), "cmts", len(cmts), "lbs", len(lbs), "OK")

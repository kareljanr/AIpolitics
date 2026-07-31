# tick 345 — screen.brussels triple economic AV
import csv
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T11:15:00Z"
unit = "rq_336"

# --- entities ---
with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "screen_brussels,screen.brussels fonds economisch audiovisueel Brussel,"
        "screen.brussels fonds economique audiovisuel Bruxelles,"
        "screen.brussels Brussels-Capital Region economic audiovisual fund,"
        "agency,brussels_gov,bi,https://screen.brussels,fund@screen.brussels,,"
        "Invest ~3m/yr 2023-25; dual Wallimage+Screen Flanders; tick345\n"
    )

# --- sources ---
with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_screen_brussels_bilan_2025,"
        "screen.brussels Bilan 2025 official page invest 2.9-3m 26 projects,"
        "https://screen.brussels/fr/actualite/bilan-2025,"
        "screen.brussels / BCR,2026-07-31,official_agency_page,"
        "Strong: nearly 3m in 26 projects; 2.9m allocated split formats; "
        "retombees 27.3m; ratio 9.2 2016-2025; tick345\n"
    )
    f.write(
        "src_screen_brussels_2024_nutshel,"
        "screen.brussels 2024 in a nutshell invest 3m 27 projects,"
        "https://screen.brussels/en/news/2024-nutshel,"
        "screen.brussels / BCR,2026-07-31,official_agency_page,"
        "Strong: 3m invest 27 projects retombees 34.122m; ratio 9.5 2016-2024; "
        "formats 48/28/19/5; tick345\n"
    )
    f.write(
        "src_screen_brussels_results_2023,"
        "screen.brussels Results 2023 invest >3m 29 projects,"
        "https://screen.brussels/en/news/results-2023,"
        "screen.brussels / BCR,2026-07-31,official_agency_page,"
        "Strong: >3m / available budget 3.1m; 29 projects retombees >=24m; "
        "apps 6.3m; tick345\n"
    )
    f.write(
        "src_cineregio_screen_brussels,"
        "CineRegio screen.brussels fund annual 3m profile,"
        "https://www.cineregio.org/members/screenbrussels_fund/,"
        "CineRegio,2026-07-31,industry_association,"
        "Strong secondary: annual budget 3m; max 500k refundable advances; "
        "min spend BCR 250k; tick345\n"
    )
    f.write(
        "src_screen_brussels_session28,"
        "screen.brussels Session 28 final 2025 invest 960k 8 projects,"
        "https://screen.brussels/en/news/session-28,"
        "screen.brussels / BCR,2026-07-31,official_agency_page,"
        "Strong partial: session 28 960k 8 projects retombees claim 7.83m; tick345\n"
    )

# --- budgets ---
buds = [
    (
        "bud_screen_brussels_invest_2025",
        "screen_brussels",
        2025,
        2900000,
        "budgeted",
        "src_screen_brussels_bilan_2025",
        "strong",
        "Bilan 2025: nearly 3m invest; 2.9m allocated by format (37pct LM 30 anim 30 series 3 doc); 26 projects",
    ),
    (
        "bud_screen_brussels_invest_2025_class",
        "screen_brussels",
        2025,
        3000000,
        "budgeted",
        "src_screen_brussels_bilan_2025",
        "strong",
        "Class ~3m annual invest 2025 (pres de 3 millions); use 2.9m allocated for format split precision",
    ),
    (
        "bud_screen_brussels_spend_claim_2025",
        "screen_brussels",
        2025,
        27300000,
        "outturn",
        "src_screen_brussels_bilan_2025",
        "medium",
        "Claimed expected AV spend return 27.3m 2025 (not public cash subsidy)",
    ),
    (
        "bud_screen_brussels_invest_2024",
        "screen_brussels",
        2024,
        3000000,
        "budgeted",
        "src_screen_brussels_2024_nutshel",
        "strong",
        "2024 invest 3m in 27 projects (official nutshell)",
    ),
    (
        "bud_screen_brussels_spend_claim_2024",
        "screen_brussels",
        2024,
        34122000,
        "outturn",
        "src_screen_brussels_2024_nutshel",
        "medium",
        "Claimed expected AV spend return 34.122m 2024",
    ),
    (
        "bud_screen_brussels_invest_2023",
        "screen_brussels",
        2023,
        3000000,
        "budgeted",
        "src_screen_brussels_results_2023",
        "strong",
        "2023 >3m invest in 29 projects; available budget 3.1m stated",
    ),
    (
        "bud_screen_brussels_budget_available_2023",
        "screen_brussels",
        2023,
        3100000,
        "budgeted",
        "src_screen_brussels_results_2023",
        "strong",
        "Available budget 3.1m 2023; applications 6.3m for 78 requests",
    ),
    (
        "bud_screen_brussels_spend_claim_2023",
        "screen_brussels",
        2023,
        24000000,
        "outturn",
        "src_screen_brussels_results_2023",
        "medium",
        "Claimed at least 24m direct AV expenditure 2023",
    ),
    (
        "bud_screen_brussels_session28_2025",
        "screen_brussels",
        2025,
        960000,
        "budgeted",
        "src_screen_brussels_session28",
        "strong",
        "Session 28 final 2025: 960k in 8 projects (partial year; cross-check bilan)",
    ),
    (
        "bud_av_econ_triple_class_2024",
        "screen_brussels",
        2024,
        17314764,
        "budgeted",
        "src_screen_brussels_2024_nutshel",
        "medium",
        "Illustrative triple economic AV 2024: Wallimage Coprod+Ent 10.815m + SF 3.5m + SB 3.0m ~17.3m; not additive TE",
    ),
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        note = b[7].replace('"', "'")
        f.write(f'{b[0]},{b[1]},{b[2]},{b[3]},,,{b[4]},{b[5]},{b[6]},"{note}"\n')

# --- commitments ---
cmt_json = (
    '{"invest_2023_m":3.0,"budget_available_2023_m":3.1,"spend_claim_2023_m":24.0,'
    '"invest_2024_m":3.0,"spend_claim_2024_m":34.122,'
    '"invest_2025_m":2.9,"invest_2025_class_m":3.0,"spend_claim_2025_m":27.3,'
    '"projects_2023":29,"projects_2024":27,"projects_2025":26,'
    '"ratio_2016_2024":9.5,"ratio_2016_2025":9.2,'
    '"max_advance_k":500,"annual_budget_cineregio_m":3.0,'
    '"dual_wallimage_sum_2024_m":10.815,"dual_screen_flanders_m":3.5,'
    '"triple_class_2024_m":17.3,'
    '"note":"Refundable advances economic fund not pure grants; dual culture VAF/CCA + federal Tax Shelter separate"}'
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_screen_brussels_econ_av_2023_25,"
        "screen.brussels economic AV fund ~3m/yr triple Wallimage Screen Flanders,"
        "screen_brussels,"
        "Brussels AV producers coproductions spending in BCR,"
        "BCR economic audiovisual fund screen.brussels (ex Bruxellimage),"
        "2016-01-01,2023,2025,9000000,"
        f'"{cmt_json}",'
        ",active,https://screen.brussels/fr/actualite/bilan-2025,"
        "Attract AV production spend employment image soft power Brussels Region,"
        "Publish L5 awards; dual unit-cost Wallimage SF; map BCR budget line cash path,"
        "src_screen_brussels_bilan_2025,strong,Bruxelles>Economie>screen.brussels,"
        "tick345: triple economic AV with Wallimage+Screen Flanders\n"
    )

# --- leaderboard ---
lbs = [
    [
        "lb_screen_brussels_3m",
        "screen.brussels economic AV invest ~3m/yr triple dual",
        "regional",
        "subsidy",
        "Bruxelles>Economie>screen.brussels",
        "3000000",
        "9000000",
        "Strong agency: 3m 2024; ~2.9-3m 2025 26 proj; 3.1m available 2023; triple Wallimage+SF",
        "strong",
        "src_screen_brussels_bilan_2025",
        "BCR AV producers coproductions",
        "Attract film TV spend jobs soft power Brussels",
        "Claimed 9x leverage; recoupable advances; third regional economic layer on culture+TE stack",
        "3",
        "4.0",
        "3",
        "3.5",
        "Open named L5 awards + BCR budget code; dual unit-cost",
        "seed",
        "",
        "tick345 triple economic AV",
    ],
    [
        "lb_av_econ_triple_wallimage_sf_sb",
        "Triple economic AV Wallimage+Screen Flanders+screen.brussels ~17m",
        "regional",
        "subsidy",
        "BE>dual>AV_economic_triple",
        "17300000",
        "17300000",
        "Medium class 2024: Wallimage ~10.8m + SF 3.5m + SB 3.0m ~17.3m; culture dual+Tax Shelter separate",
        "medium",
        "src_screen_brussels_2024_nutshel",
        "Regional AV industries three entities",
        "Triple-structure economic film incentives FL/WAL/BRU",
        "Classic multi-entity overhead: 3 economic funds + 2 culture funds + federal tax shelter",
        "5",
        "6.5",
        "5",
        "5.75",
        "Map full AV stack TCO; FOI L5 all three funds",
        "seed",
        "",
        "tick345 triple dual structure",
    ],
]
with open(base / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(",".join(lb) + "\n")

# --- research_queue ---
rq_path = base / "research_queue.csv"
with open(rq_path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for r in rows:
    if r["task_id"] == "rq_336":
        r["status"] = "done"
        r["blocked_gap_id"] = "gap_screen_brussels_l5"
        r["updated_utc"] = now
        r["notes"] = (
            "tick345: screen.brussels invest ~3m/yr 2023-25 triple Wallimage+SF; "
            "FOI L5; spawn rq_337"
        )

rows.append(
    {
        "task_id": "rq_337",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.",
        "blocked_gap_id": "",
        "created_utc": now,
        "updated_utc": "",
        "notes": "Spawned tick345 after screen.brussels triple economic AV; rq_116 SWA deferred",
    }
)
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

# --- foi_queue ---
with open(base / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_screen_brussels_l5,Bruxelles>Economie>screen.brussels>L5,screen_brussels,"
        "Named L5 awards screen.brussels 2023-2025 with amounts projects producers; "
        "BCR budget article codes cash-by-year dotation; recoup rates; reconcile session totals vs bilan 2.9-3.1m,"
        "Triple economic AV fund opacity under Wallimage+Screen Flanders + culture VAF/CCA + federal Tax Shelter,"
        "5,screen.brussels fund / SPRB transparence,fund@screen.brussels; transparence@sprb.brussels,"
        "2-4 Rue de Praetere 1000 Brussels,docs/doge/foi/drafts/gap_screen_brussels_l5.md,"
        "ready,2026-07-31,,,,,cmt_screen_brussels_econ_av_2023_25,"
        "lb_screen_brussels_3m|lb_av_econ_triple_wallimage_sf_sb,"
        "2026-07-31T11:15:00Z,2026-07-31T11:15:00Z,"
        "tick345 public fill bilans; residual L5 human send\n"
    )

# --- loop_state ---
with open(base / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    f.write(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    )
    f.write(
        f"main,continuous,hole_fill,{now},{unit},345,no,"
        "Scheduler 60s. Next prio5 rq_337; rq_116 SWA deferred. FOI ready. "
        "tick345 screen.brussels triple econ AV.\n"
    )

print("CSV updates OK")

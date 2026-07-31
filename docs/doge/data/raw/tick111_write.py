"""Tick 111: rq_111 stookolie + agriculture intermediate FFS multi-year."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
UTC = "2026-07-27T02:20:00Z"

with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(
        "src_fps_ffs_2026_stookolie_t16,FFS 2026 full Table16 huisbrandolie multi-year,"
        "https://finance.belgium.be/sites/default/files/Statistieken_SD/Inventaris/FFS-report-NL-Master%20ed%202026_final.pdf,"
        "FPS Finance + FPS Health,2026-07-27,budget,"
        '"Table16: stookolie total 2130/2263/2097/1857/1798/1836 mEUR 2019-24 bench1; raw fps_ffs_2026_nl_full.pdf p30-33"\n'
    )
    f.write(
        "src_fps_ffs_2026_intermed_t19,FFS 2026 full Table19 intermediate consumption subsidies,"
        "https://finance.belgium.be/sites/default/files/Statistieken_SD/Inventaris/FFS-report-NL-Master%20ed%202026_final.pdf,"
        "FPS Finance + FPS Health,2026-07-27,budget,"
        '"Table19: agriculture+related total 549/563/630/443/379 mEUR 2020-24 bench1; raw p41"\n'
    )

# tax_expenditures multi-year
with (DATA / "tax_expenditures.csv").open("a", encoding="utf-8", newline="") as f:
    stook = [
        (2019, 2129800000),
        (2020, 2263300000),
        (2021, 2096500000),
        (2022, 1856800000),
        (2023, 1798200000),
        (2024, 1836400000),
    ]
    for y, a in stook:
        f.write(
            f"tx_ffs_stookolie_{y},Heating gas oil huisbrandolie FFS bench1 total,federal,{y},{a},EXC,"
            f"src_fps_ffs_2026_stookolie_t16,strong,8,"
            f'"Table16: {a/1e6:.1f} mEUR vs gasoline TOE; dual high/low S components"\n'
        )
    f.write(
        "tx_ffs_stookolie_lowS_2024,Heating gas oil low sulfur FFS component,federal,2024,1526700000,EXC,"
        "src_fps_ffs_2026_stookolie_t16,strong,8,"
        '"Table16: 1526.7 mEUR low-S; high-S 309.7m; taxex inv product-bench lower (~1333m class)"\n'
    )
    f.write(
        "tx_ffs_stookolie_highS_2024,Heating gas oil high sulfur FFS component,federal,2024,309700000,EXC,"
        "src_fps_ffs_2026_stookolie_t16,strong,8,"
        '"Table16: 309.7 mEUR high-S residual after shift to low-S"\n'
    )
    ag = [
        (2020, 548900000),
        (2021, 562600000),
        (2022, 629900000),
        (2023, 442800000),
        (2024, 378500000),
    ]
    for y, a in ag:
        f.write(
            f"tx_ffs_ag_intermed_{y},Agriculture intermediate fossil energy FFS bench1,federal,{y},{a},EXC,"
            f"src_fps_ffs_2026_intermed_t19,strong,7,"
            f'"Table19 land/garden/fish/forestry total {a/1e6:.1f} mEUR; mostly product rate diffs"\n'
        )
    f.write(
        "tx_ffs_binnenvaart_2024,Inland waterway intermediate energy FFS,federal,2024,84300000,EXC,"
        "src_fps_ffs_2026_intermed_t19,strong,6,"
        '"Table19: 84.3 mEUR 2024; path stable ~80-90m"\n'
    )
    f.write(
        "tx_ffs_bagger_2024,Dredging intermediate energy FFS,federal,2024,24700000,EXC,"
        "src_fps_ffs_2026_intermed_t19,strong,5,"
        '"Table19: 24.7 mEUR 2024; down from 51.5m 2020 after heavy fuel to diesel"\n'
    )

# commitments
new_cmts = [
    {
        "commitment_id": "cmt_stookolie_excise_preference",
        "title": "Heating gas oil (huisbrandolie) excise preference multi-year FFS",
        "entity_id": "fod_finance",
        "beneficiary": "Households and users of heating gas oil",
        "legal_basis": "Control retribution + energy contribution only vs diesel road rates",
        "decision_date": "2005-01-01",
        "start_year": "2019",
        "end_year": "2024",
        "total_envelope_eur": "11979000000",
        "cash_by_year": (
            '{"2019":2129800000,"2020":2263300000,"2021":2096500000,"2022":1856800000,'
            '"2023":1798200000,"2024":1836400000,"lowS_2024":1526700000,"highS_2024":309700000,'
            '"vol_trend_2005_24_pct_yr":-3.7}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "",
        "stated_goal": "Legacy heating fuel preferential rate",
        "cut_option": "Equalise energy-basis excise; protect low-income via cash/social heating fund not fuel-specific TE",
        "source_id": "src_fps_ffs_2026_stookolie_t16",
        "confidence": "strong",
        "hierarchy_path": "Federal>FFS>stookolie",
        "notes": (
            "tick111: FFS eval not justified env or social (not concentrated lowest income); "
            "87pct owners in HBS sample; taxex inv method gives lower product-specific ~1333m"
        ),
    },
    {
        "commitment_id": "cmt_ag_intermed_energy_ffs",
        "title": "Agriculture intermediate fossil energy subsidies FFS",
        "entity_id": "fod_finance",
        "beneficiary": "Agriculture horticulture fisheries forestry",
        "legal_basis": "Excise exemptions + product rate diffs intermediate consumption",
        "decision_date": "2005-01-01",
        "start_year": "2020",
        "end_year": "2024",
        "total_envelope_eur": "2562700000",
        "cash_by_year": (
            '{"2020":548900000,"2021":562600000,"2022":629900000,"2023":442800000,"2024":378500000,'
            '"exemption_share_2024":8900000,"product_diff_share_2024":369500000}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "",
        "stated_goal": "Sectoral competitiveness",
        "cut_option": "Decouple sector support from energy use; keep price signal for decarbonisation",
        "source_id": "src_fps_ffs_2026_intermed_t19",
        "confidence": "strong",
        "hierarchy_path": "Federal>FFS>agriculture_intermediate",
        "notes": "tick111 Table19; peak 2022 energy crisis; declining 2023-24",
    },
    {
        "commitment_id": "cmt_sociaal_verwarmingsfonds",
        "title": "Sociaal Verwarmingsfonds (stookolie fund) cash transfers",
        "entity_id": "fod_finance",
        "beneficiary": "Low-income heating oil/propane households via OCMW",
        "legal_basis": "Sociaal Verwarmingsfonds with oil sector + OCMW",
        "decision_date": "2004-01-01",
        "start_year": "2019",
        "end_year": "2024",
        "total_envelope_eur": "95200000",
        "cash_by_year": (
            '{"2019":16600000,"2020":14600000,"2021":13800000,"2022":21100000,"2023":16500000,'
            '"2024":12600000,"households_2024":70112}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "",
        "stated_goal": "Targeted heating affordability for vulnerable",
        "cut_option": "Keep/expand targeted fund if equalising stookolie excise (better than untargeted TE)",
        "source_id": "src_fps_ffs_2026_stookolie_t16",
        "confidence": "strong",
        "hierarchy_path": "Federal>FFS>social_heating_fund",
        "notes": "tick111 Table1/§1.3: 12.6m 2024; 70k households; contrasts with 1.8bn untargeted excise preference",
    },
]

with (DATA / "commitments.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
ids = {x["commitment_id"] for x in rows}
for c in new_cmts:
    if c["commitment_id"] not in ids:
        rows.append({k: c.get(k, "") for k in fields})
with (DATA / "commitments.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
print("commitments", len(rows))

# leaderboard
with (DATA / "leaderboard.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    lb_fields = r.fieldnames
    lb_rows = list(r)
lb_ids = {x["item_id"] for x in lb_rows}

for row in lb_rows:
    if row["item_id"] == "lb_exc_heatoil":
        row["annual_cost_eur"] = "1836400000"
        row["total_cost_eur"] = "11979000000"
        row["tco_notes"] = (
            "FFS bench1 total 1836.4m 2024 (lowS 1526.7 highS 309.7); path ~2.1bn→1.8bn 2019-24; "
            "taxex product-bench ~1333m separate method"
        )
        row["source_id"] = "src_fps_ffs_2026_stookolie_t16"
        row["measured_outcome"] = (
            "FFS: not social (not lowest quartile); volume -3.7%/yr long-run; shift high→low S"
        )
        row["absurdity_score"] = "8"
        row["cost_score"] = "9"
        row["difficulty"] = "6"
        row["priority_index"] = "8.0"
        row["cut_proposal"] = (
            "Equalise to diesel energy basis; expand social heating fund; phase-out preferential rate"
        )
        row["notes"] = "tick111 FFS multi-year supersedes single taxex 1333m for ranking"

if "lb_ag_intermed_ffs" not in lb_ids:
    row = {k: "" for k in lb_fields}
    row.update(
        {
            "item_id": "lb_ag_intermed_ffs",
            "name": "Agriculture intermediate fossil energy FFS package",
            "level": "federal",
            "type": "tax_expenditure",
            "hierarchy_path": "Federal>FFS>agriculture_intermediate",
            "annual_cost_eur": "378500000",
            "total_cost_eur": "1892500000",
            "tco_notes": "FFS Table19 378.5m 2024; path 549/563/630/443/379 2020-24",
            "confidence": "strong",
            "source_id": "src_fps_ffs_2026_intermed_t19",
            "beneficiaries": "Agriculture horticulture fisheries forestry",
            "stated_goal": "Sectoral competitiveness",
            "measured_outcome": "Mostly product rate diffs not pure exemption; no decarbonisation price signal",
            "absurdity_score": "6",
            "cost_score": "6.5",
            "difficulty": "6",
            "priority_index": "6.15",
            "cut_proposal": "Decouple support from fuel use; keep income/policy support separate",
            "status": "seed",
            "struck_reason": "",
            "notes": "tick111",
        }
    )
    lb_rows.append(row)

with (DATA / "leaderboard.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=lb_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(lb_rows)
print("leaderboard", len(lb_rows))

# research queue
with (DATA / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)
for row in rq_rows:
    if row["task_id"] == "rq_111":
        row["status"] = "done"
        row["updated_utc"] = UTC
        row["notes"] = (
            "tick111: stookolie 1836m 2024 path from 2130m 2019; ag intermed 379m; "
            "social heating fund 12.6m contrast; FFS social+env critique"
        )
if not any(r["task_id"] == "rq_112" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_112",
            "title": "Industrial reduced gas rate FFS 903m multi-year or inland waterways",
            "sprint": "continuous",
            "priority": "3",
            "status": "open",
            "hierarchy_target": "taxex",
            "entity_id": "fod_finance",
            "instructions": (
                "From FFS Table16: aardgas verlaagd tarief 903m 2024 path; and/or binnenvaart 84m. "
                "Map energy policy agreements link if public."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "Next large FFS industrial gas reduced rate",
        }
    )
with (DATA / "research_queue.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(rq_rows)

with (DATA / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(
        [
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ]
    )
    w.writerow(
        [
            "main",
            "continuous",
            "continuous",
            UTC,
            "rq_111",
            111,
            "no",
            "tick111 stookolie+ag FFS. Next: rq_112 industrial gas or rq_107 SWA; human FOI stack.",
        ]
    )

with (ROOT / "loop_log.md").open("a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} — tick 111
- Unit: **rq_111** (Stookolie / agriculture intermediate FFS multi-year)
- Found (strong FFS 2026 Tables 16+19):
  - **Huisbrandolie total** (bench1): **2019–24 €2,129.8 / 2,263.3 / 2,096.5 / 1,856.8 / 1,798.2 / 1,836.4 m**. 2024 split low-S **€1,526.7m** + high-S **€309.7m**. Long-run volume −3.7%/yr. FFS eval: **not justified environmentally or socially** (heating oil users not concentrated in lowest income quartile; 87% homeowners in HBS).
  - Taxex inventory product-specific line (~**€1,333m** prior seed) remains separate method — FFS gasoline-TOE higher.
  - **Agriculture intermediate** total: **2020–24 €548.9 / 562.6 / 629.9 / 442.8 / 378.5 m** (mostly product rate diffs, not pure exemption).
  - **Sociaal Verwarmingsfonds** cash: **€12.6m** 2024 / **70,112** households — targeted contrast to €1.8bn untargeted excise preference.
  - Binnenvaart **€84.3m** / bagger **€24.7m** 2024 intermediate package.
- Wrote: sources +2; taxex multi-year stookolie+ag; commitments +3; leaderboard refresh heatoil + ag seed; rq_111=done; spawned **rq_112**; ticks=111
- FOI opened: none
- Next: **rq_112** industrial reduced gas rate (€903m) or low **rq_107** SWA
"""
    )
print("DONE tick111")

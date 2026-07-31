"""Tick 109: rq_109 FPS FFS 5th inventory + federal taxex inventory totals."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
UTC = "2026-07-27T01:40:00Z"

# --- sources ---
with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(
        "src_fps_ffs_2026_nl_full,Federale inventaris subsidies fossiele brandstoffen 2026 full NL,"
        "https://finance.belgium.be/sites/default/files/Statistieken_SD/Inventaris/FFS-report-NL-Master%20ed%202026_final.pdf,"
        "FPS Finance + FPS Health,2026-07-27,budget,"
        '"5th inventory Jul 2026 data cut 1 Jan 2026; direct FFS 2024 10781.9m 1.7pct GDP; raw fps_ffs_2026_nl_full.pdf"\n'
    )
    f.write(
        "src_fps_ffs_2026_summary_nl,FFS 2026 samenvatting NL,"
        "https://climat.be/doc/ffs-2026-samenvatting-nl.pdf,"
        "FPS Finance + FPS Health / klimaat.be,2026-07-27,budget,"
        '"Summary tables 1-3: pro diesel 831.2m; company cars 3141.7m; fuel cards 661.6m; kerosene air 754.6m; raw fps_ffs_2026_summary_nl.pdf"\n'
    )
    f.write(
        "src_fps_taxex_inventory_2026_pdf,Inventory of Federal Tax expenditures (2024) PDF,"
        "https://finance.belgium.be/sites/default/files/Statistieken_SD/Inventaris/Inventory_federal_tax_expenditures_2026.pdf,"
        "FPS Finance Research Department,2026-07-27,fps,"
        '"Global TE 2023 39402m (6.74pct GDP); by tax VAT 16198 PIT fed 9671 EIWT 4415; raw fps_taxex_inventory_2026.pdf"\n'
    )

# --- tax_expenditures ---
with (DATA / "tax_expenditures.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(
        "tx_fed_total_2023,Federal tax expenditures total quantified (inventory),federal,2023,39402010000,multi,"
        "src_fps_taxex_inventory_2026_pdf,strong,6,"
        '"Table1: 39402.01 mEUR 2023; 6.74pct GDP; avg annual growth 6.37pct 2018-23; NOT cash spending"\n'
    )
    f.write(
        "tx_fed_total_2022,Federal tax expenditures total quantified,federal,2022,36914740000,multi,"
        "src_fps_taxex_inventory_2026_pdf,strong,6,"
        '"Table1: 36914.74 mEUR 2022"\n'
    )
    f.write(
        "tx_vat_package_2023,VAT tax expenditures aggregate,federal,2023,16198200000,VAT,"
        "src_fps_taxex_inventory_2026_pdf,strong,5,"
        '"Table1: 16198.20 mEUR; 43.3pct of VAT yield; largest tax class"\n'
    )
    f.write(
        "tx_pit_fed_package_2023,PIT federal tax expenditures aggregate,federal,2023,9671010000,PIT,"
        "src_fps_taxex_inventory_2026_pdf,strong,4,"
        '"Table1: 9671.01 mEUR federal PIT measures"\n'
    )
    f.write(
        "tx_eiwt_package_2023,EIWT earned income withholding tax expenditures aggregate,federal,2023,4415480000,EIWT,"
        "src_fps_taxex_inventory_2026_pdf,strong,6,"
        '"Table1: 4415.48 mEUR 2023; path up from 3175m 2018; aligns with EIWT 4.356bn 2024 xlsx sum"\n'
    )
    f.write(
        "tx_cit_package_2023,CIT tax expenditures aggregate,federal,2023,3809420000,CIT,"
        "src_fps_taxex_inventory_2026_pdf,strong,4,"
        '"Table1: 3809.42 mEUR 2023"\n'
    )
    f.write(
        "tx_exc_package_2023,Excise tax expenditures aggregate (inventory method),federal,2023,2440760000,EXC,"
        "src_fps_taxex_inventory_2026_pdf,strong,7,"
        '"Table1: 2440.76 mEUR; product-specific benchmark differs from FFS gasoline-toe method"\n'
    )
    f.write(
        "tx_ffs_direct_2024,Direct fossil fuel subsidies total FFS benchmark1,federal,2024,10781900000,multi,"
        "src_fps_ffs_2026_summary_nl,strong,8,"
        '"Table3: 10781.9 mEUR 1.7pct GDP; path 12092.8/13445.9/11661.9/10781.9 2021-24"\n'
    )
    f.write(
        "tx_ffs_kerosene_air_2024,Excise exemption kerosene international aviation FFS,federal,2024,754600000,EXC,"
        "src_fps_ffs_2026_summary_nl,strong,8,"
        '"Table3: 754.6 mEUR 2024 rising path; international aviation"\n'
    )
    f.write(
        "tx_ffs_vat_gas_hh_2024,VAT reduced rate gas households FFS,federal,2024,635200000,VAT,"
        "src_fps_ffs_2026_summary_nl,strong,6,"
        '"Table3: 635.2 mEUR 2024 permanent crisis-era reduced rate"\n'
    )
    f.write(
        "tx_ffs_agriculture_exc_2024,Agriculture intermediate consumption excise FFS,federal,2024,378500000,EXC,"
        "src_fps_ffs_2026_summary_nl,strong,7,"
        '"Table3 intermediate: land/garden/fish/forestry 378.5 mEUR 2024"\n'
    )
    f.write(
        "tx_ffs_package_broad_2024,FFS broad package direct+intl+indirect+company_cars EHS,federal,2024,15154700000,multi,"
        "src_fps_ffs_2026_summary_nl,strong,8,"
        '"Sum 10781.9+1006.5+224.5+3141.7=15154.6 mEUR ~press 15bn class; do not double-count with pure TE inventory"\n'
    )

# --- commitments ---
new_cmts = [
    {
        "commitment_id": "cmt_fps_ffs_direct_2021_24",
        "title": "Federal direct fossil fuel subsidies FFS path 2021-2024",
        "entity_id": "fod_finance",
        "beneficiary": "Energy users households firms transport agriculture",
        "legal_basis": "Federal FFS inventory 5th ed Jul 2026 benchmark1 gasoline TOE",
        "decision_date": "2026-07-01",
        "start_year": "2021",
        "end_year": "2024",
        "total_envelope_eur": "47982500000",
        "cash_by_year": (
            '{"2021":12092800000,"2022":13445900000,"2023":11661900000,"2024":10781900000,'
            '"pct_gdp_2024":1.7,"company_cars_ehs_2024":3141700000,"pro_diesel_2024":831200000,'
            '"fuel_cards_2024":661600000,"kerosene_air_2024":754600000}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://finance.belgium.be/nl/Statistieken_en_analysen/analysen/inventaris-van-subsidies-voor-fossiele-brandstoffen",
        "stated_goal": "Inventory for NECP transparency and spending review (not revenue estimate)",
        "cut_option": "Phase-out strategy per COFFIS/Belem; not 1:1 budget gain (behaviour + compensation)",
        "source_id": "src_fps_ffs_2026_summary_nl",
        "confidence": "strong",
        "hierarchy_path": "Federal>FFS>direct",
        "notes": "tick109 5th inventory; amounts are opportunity cost vs benchmark not cash grants; steelman social/competitiveness aims",
    },
    {
        "commitment_id": "cmt_fps_taxex_total_2023",
        "title": "Federal tax expenditures total quantified inventory 2023",
        "entity_id": "fod_finance",
        "beneficiary": "Taxpayers under preferential regimes",
        "legal_basis": "Federal inventory of tax expenditures annex to Ways and Means budget",
        "decision_date": "2024-01-01",
        "start_year": "2018",
        "end_year": "2023",
        "total_envelope_eur": "39402010000",
        "cash_by_year": (
            '{"2018":28939600000,"2019":30546600000,"2020":30627680000,"2021":32846910000,'
            '"2022":36914740000,"2023":39402010000,"pct_gdp_2023":6.74,"vat_2023":16198200000,'
            '"pit_fed_2023":9671010000,"eiwt_2023":4415480000}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://finance.belgium.be/sites/default/files/Statistieken_SD/Inventaris/Inventory_federal_tax_expenditures_2026.pdf",
        "stated_goal": "Inform parliament of cost of tax deviations",
        "cut_option": "Spending reviews by objective (social 42pct of quantified); sunset low-eval measures",
        "source_id": "src_fps_taxex_inventory_2026_pdf",
        "confidence": "strong",
        "hierarchy_path": "Federal>taxex>total",
        "notes": "tick109; 255 measures quantified sum; unquantified still missing; not additive to FFS broad 15bn without care",
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

# --- leaderboard ---
with (DATA / "leaderboard.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    lb_fields = r.fieldnames
    lb_rows = list(r)
lb_ids = {x["item_id"] for x in lb_rows}

# refresh company cars / fuel / pro diesel notes if still on old source only
for row in lb_rows:
    if row["item_id"] == "lb_company_cars":
        row["tco_notes"] = (
            "FFS 2026 5th inv Table3: 3141.7m 2024 EHS (path 1998/2880/3153/3142 2021-24); confirmed tick109"
        )
        row["source_id"] = "src_fps_ffs_2026_summary_nl"
    if row["item_id"] == "lb_fuel_cards":
        row["tco_notes"] = "FFS 2026: 661.6m 2024 PIT+SSC; VAT cards 52.8m; path 688/1119/853/662"
        row["source_id"] = "src_fps_ffs_2026_summary_nl"
    if row["item_id"] == "lb_exc_prodiesel":
        row["tco_notes"] = (
            "FFS bench1 831.2m 2024 (path 1052/558/773/831); taxex inv product-specific lower"
        )
        row["source_id"] = "src_fps_ffs_2026_summary_nl"

def add_lb(item):
    if item["item_id"] not in lb_ids:
        row = {k: "" for k in lb_fields}
        row.update(item)
        lb_rows.append(row)
        lb_ids.add(item["item_id"])

add_lb(
    {
        "item_id": "lb_fed_taxex_total",
        "name": "Federal tax expenditures total quantified",
        "level": "federal",
        "type": "tax_expenditure",
        "hierarchy_path": "Federal>taxex>total",
        "annual_cost_eur": "39402010000",
        "total_cost_eur": "197010050000",
        "tco_notes": "39.402bn 2023 strong; 6.74pct GDP; multi-year illustrative 5y",
        "confidence": "strong",
        "source_id": "src_fps_taxex_inventory_2026_pdf",
        "beneficiaries": "All preferential tax regime users",
        "stated_goal": "Parliament transparency on tax deviations",
        "measured_outcome": "255 quantified measures; social 42pct of total; many unquantified still",
        "absurdity_score": "4",
        "cost_score": "10",
        "difficulty": "8",
        "priority_index": "6.8",
        "cut_proposal": "Objective-based spending reviews; publish full cash-by-year open data; do not treat as pure waste",
        "status": "seed",
        "struck_reason": "",
        "notes": "tick109; mega-aggregate for map not a single cut target",
    }
)
add_lb(
    {
        "item_id": "lb_ffs_direct_total",
        "name": "Federal direct fossil fuel subsidies total FFS",
        "level": "federal",
        "type": "tax_expenditure",
        "hierarchy_path": "Federal>FFS>direct",
        "annual_cost_eur": "10781900000",
        "total_cost_eur": "53909500000",
        "tco_notes": "10.782bn 2024; 1.7pct GDP; down from 2.4pct 2021; broad+EHS+intl ~15.2bn",
        "confidence": "strong",
        "source_id": "src_fps_ffs_2026_summary_nl",
        "beneficiaries": "Households firms transport agriculture energy users",
        "stated_goal": "Competitiveness social heating affordability (mixed)",
        "measured_outcome": "Volume-driven path; no full phase-out plan per EEA critique cited in report",
        "absurdity_score": "7",
        "cost_score": "9.5",
        "difficulty": "7",
        "priority_index": "8.0",
        "cut_proposal": "National FFS phase-out strategy COFFIS; equalise excise energy basis; protect vulnerable via cash not price",
        "status": "seed",
        "struck_reason": "",
        "notes": "tick109 5th inventory; opportunity cost vs gasoline TOE benchmark",
    }
)
add_lb(
    {
        "item_id": "lb_ffs_kerosene_air",
        "name": "Kerosene excise exemption international aviation",
        "level": "federal",
        "type": "tax_expenditure",
        "hierarchy_path": "Federal>FFS>aviation_kerosene",
        "annual_cost_eur": "754600000",
        "total_cost_eur": "3773000000",
        "tco_notes": "754.6m 2024 FFS; rising 594→755 2021-24",
        "confidence": "strong",
        "source_id": "src_fps_ffs_2026_summary_nl",
        "beneficiaries": "International aviation",
        "stated_goal": "Chicago Convention / EU energy tax directive legacy",
        "measured_outcome": "Continual rise post-COVID",
        "absurdity_score": "8",
        "cost_score": "7.5",
        "difficulty": "8",
        "priority_index": "7.4",
        "cut_proposal": "EU ETD reform; ticket tax or kerosene tax path; SAF neutral design",
        "status": "seed",
        "struck_reason": "",
        "notes": "tick109; international coordination constraint",
    }
)

with (DATA / "leaderboard.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=lb_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(lb_rows)
print("leaderboard", len(lb_rows))

# --- budgets top-line ---
with (DATA / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(
        "bud_fed_taxex_total_2023,fod_finance,2023,39402010000,,,estimated,"
        "src_fps_taxex_inventory_2026_pdf,strong,"
        '"Federal tax expenditure inventory quantified total 39.402bn (not ESA expenditure)"\n'
    )
    f.write(
        "bud_ffs_direct_2024,fod_finance,2024,10781900000,,,estimated,"
        "src_fps_ffs_2026_summary_nl,strong,"
        '"FFS 5th inv direct subsidies benchmark1 10.782bn 1.7pct GDP"\n'
    )

# --- research_queue ---
with (DATA / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)
for row in rq_rows:
    if row["task_id"] == "rq_109":
        row["status"] = "done"
        row["updated_utc"] = UTC
        row["notes"] = (
            "tick109: FFS 5th inv confirms direct 10.782bn 2024; TE inventory 39.402bn 2023; "
            "kerosene air 754.6m; VAT gas 635m; refreshed company cars/fuel/prodiesel sources"
        )
if not any(r["task_id"] == "rq_110" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_110",
            "title": "Federal kerosene aviation or VAT reduced gas path multi-year deepen",
            "sprint": "continuous",
            "priority": "3",
            "status": "open",
            "hierarchy_target": "taxex",
            "entity_id": "fod_finance",
            "instructions": (
                "From FFS 2026: map kerosene air 754.6m and/or VAT gas HH 635.2m multi-year "
                "and reform options from official sources only."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "After tick109 FFS refresh; high-EUR fossil lines",
        }
    )
with (DATA / "research_queue.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(rq_rows)

# --- loop_state ---
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
            "rq_109",
            109,
            "no",
            "tick109 FFS+TE totals refreshed. Next: rq_110 kerosene/VAT gas or rq_107 SWA; human FOI stack.",
        ]
    )

# --- log ---
with (ROOT / "loop_log.md").open("a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} — tick 109
- Unit: **rq_109** (FPS FFS / taxex inventory micro-update)
- Found (strong primary Jul 2026 editions):
  - **FFS 5th inventory** (FPS Finance+Health, data cut 1 Jan 2026, pub Jul 2026): **direct fossil subsidies 2024 €10,781.9m** (1.7% GDP); path 12.09 / 13.45 / 11.66 / 10.78 bn 2021–24. Confirms prior EN summary: company cars EHS **€3,141.7m**; fuel cards **€661.6m**; pro diesel FFS **€831.2m**; aviation kerosene **€754.6m**; VAT reduced gas HH **€635.2m**; agriculture intermediate **€378.5m**. International air+sea **€1,006.5m**. Broad sum direct+intl+indirect+EHS ≈ **€15.15bn** (press “15bn” class).
  - **Inventory of Federal Tax Expenditures (2024)** PDF: quantified total **2023 €39,402.01m** (6.74% GDP); path 28.9→39.4 bn 2018–23 (+6.37%/yr avg). By tax 2023: VAT **16.20bn**; PIT federal **9.67bn**; EIWT **4.42bn**; CIT **3.81bn**; excise **2.44bn**. Social objective **42.4%** of quantified.
  - Taxex XLSX recheck already identical earlier; this PDF adds **official global aggregates** not fully seeded before.
  - Method note (strong): FFS ≠ cash budget gain if abolished; TE inventory ≠ ESA spending; do not double-count FFS into TE total.
- Wrote: sources +3; tax_expenditures +12; commitments +2; leaderboard +3 + refresh 3 fossil rows; budgets +2; rq_109=done; spawned **rq_110**; raw FFS full+summary + taxex PDF; ticks=109
- FOI opened: none (public inventories sufficient for this unit)
- Next: **rq_110** kerosene/VAT gas deepen or low **rq_107** SWA
"""
    )
print("DONE tick109")

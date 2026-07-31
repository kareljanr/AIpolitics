"""Tick 114: rq_114 FFS synthesis snapshot + LPG/coal multi-year from Table16."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
UTC = "2026-07-27T03:20:00Z"

# --- LPG + coal multi-year from Table16 (already extracted prior ticks) ---
# Table16: LPG heating 108.6/138.8/140.0/120.3/117.8/127.6 2019-24
# Coal HH: 27.8/20.8/22.1/16.5/11.1/10.8

with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(
        "src_fps_ffs_2026_lpg_coal_t16,FFS 2026 Table16 LPG heating + coal HH multi-year,"
        "https://finance.belgium.be/sites/default/files/Statistieken_SD/Inventaris/FFS-report-NL-Master%20ed%202026_final.pdf,"
        "FPS Finance + FPS Health,2026-07-27,budget,"
        '"LPG heating 109-140-128m; coal HH 28-11m 2019-24; raw fps_ffs_2026_nl_full.pdf Table16"\n'
    )
    f.write(
        "src_doge_ffs_snapshot_2026,DOGE FFS top-lines synthesis snapshot 2026,"
        "docs/doge/data/ffs_federal_top_lines_2024.md,AIpolitics DOGE loop,2026-07-27,secondary,"
        '"From FFS 5th inv primary rows already in CSVs; no invent euros; do not sum all lines"\n'
    )

with (DATA / "tax_expenditures.csv").open("a", encoding="utf-8", newline="") as f:
    lpg = [
        (2019, 108600000),
        (2020, 138800000),
        (2021, 140000000),
        (2022, 120300000),
        (2023, 117800000),
        (2024, 127600000),
    ]
    for y, a in lpg:
        f.write(
            f"tx_ffs_lpg_heating_{y},LPG used as heating fuel FFS bench1,federal,{y},{a},EXC,"
            f"src_fps_ffs_2026_lpg_coal_t16,strong,6,"
            f'"Table16: {a/1e6:.1f} mEUR"\n'
        )
    coal = [
        (2019, 27800000),
        (2020, 20800000),
        (2021, 22100000),
        (2022, 16500000),
        (2023, 11100000),
        (2024, 10800000),
    ]
    for y, a in coal:
        f.write(
            f"tx_ffs_coal_hh_{y},Coal/coke household exemption FFS,federal,{y},{a},EXC,"
            f"src_fps_ffs_2026_lpg_coal_t16,strong,5,"
            f'"Table16: {a/1e6:.1f} mEUR declining; reduced VAT on solid fuels abolished Jul 2025"\n'
        )

# commitments for LPG
new_cmts = [
    {
        "commitment_id": "cmt_lpg_heating_ffs",
        "title": "LPG heating fuel excise preference multi-year FFS",
        "entity_id": "fod_finance",
        "beneficiary": "LPG heating users",
        "legal_basis": "Preferential excise on LPG as heating fuel vs gasoline TOE",
        "decision_date": "2005-01-01",
        "start_year": "2019",
        "end_year": "2024",
        "total_envelope_eur": "753100000",
        "cash_by_year": (
            '{"2019":108600000,"2020":138800000,"2021":140000000,"2022":120300000,'
            '"2023":117800000,"2024":127600000}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "",
        "stated_goal": "Heating fuel preferential rate",
        "cut_option": "Equalise energy-basis; small line relative to gas/stookolie",
        "source_id": "src_fps_ffs_2026_lpg_coal_t16",
        "confidence": "strong",
        "hierarchy_path": "Federal>FFS>LPG_heating",
        "notes": "tick114 Table16",
    },
    {
        "commitment_id": "cmt_coal_hh_exemption_ffs",
        "title": "Coal/coke household excise exemption multi-year FFS",
        "entity_id": "fod_finance",
        "beneficiary": "Household solid fuel heating (residual)",
        "legal_basis": "Household coal/coke exemption",
        "decision_date": "2005-01-01",
        "start_year": "2019",
        "end_year": "2024",
        "total_envelope_eur": "109100000",
        "cash_by_year": (
            '{"2019":27800000,"2020":20800000,"2021":22100000,"2022":16500000,'
            '"2023":11100000,"2024":10800000}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "",
        "stated_goal": "Legacy solid fuel heating support",
        "cut_option": "Sunset residual; reduced VAT solid fuels abolished Jul 2025 (FFS)",
        "source_id": "src_fps_ffs_2026_lpg_coal_t16",
        "confidence": "strong",
        "hierarchy_path": "Federal>FFS>coal_HH",
        "notes": "tick114 declining; few households per FFS HBS note",
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

# synthesis markdown — only sourced figures already in dataset
snapshot = DATA / "ffs_federal_top_lines_2024.md"
snapshot.write_text(
    """# Federal fossil fuel subsidies (FFS) — top lines snapshot

**Source class:** FPS Finance + FPS Health, *Federale inventaris van subsidies voor fossiele brandstoffen 2026* (5th edition, Jul 2026; data cut 1 Jan 2026).  
**Method:** Benchmark 1 = unleaded petrol TOE neutrality unless noted. Amounts are **opportunity cost vs benchmark**, not ESA cash grants and **not additive** without care (double instruments, different benches).  
**DOGE rule:** no invented euros; confidence **strong** for table extracts.

## Package totals (2024)

| Package | EUR m | Notes |
|---------|------:|-------|
| Direct FFS total | **10,781.9** | 1.7% GDP; path 12.09 / 13.45 / 11.66 / 10.78 bn 2021–24 |
| International air+sea | **1,006.5** | Kerosene air 754.6 + heavy FO sea 226.9 + diesel sea 25.0 |
| Indirect (VAT air tickets) | **224.5** | Path 87.5 → 224.5 2021–24 |
| Company cars EHS | **3,141.7** | Path 1,998 → 3,142 2021–24 |
| **Illustrative broad sum** | **~15,155** | Direct+intl+indirect+EHS — press “15bn” class; **do not treat as single cut** |

## Mapped high-EUR lines (2024, already in CSVs)

| Line | EUR m 2024 | Multi-year note | Leaderboard / commitment |
|------|----------:|-----------------|--------------------------|
| Gas product rate-diff (bench1) | **4,089** | 4,742→5,124→4,089 2019–24 | `lb_gas_product_diff` |
| Stookolie / huisbrandolie total | **1,836** | 2,130→1,836 2019–24 | `lb_exc_heatoil` |
| Company cars EHS | **3,142** | FFS Table3 | `lb_company_cars` |
| Industrial gas reduced (EBO) | **903** | Peak 1,295 (2022) | `lb_gas_reduced_industrial` |
| Pro diesel FFS bench1 | **831** | 1,052→558→831 | `lb_exc_prodiesel` |
| Aviation kerosene | **755** | 677→755 2019–24 | `lb_ffs_kerosene_air` |
| Fuel cards PIT+SSC | **662** | Peak 1,119 (2022) | `lb_fuel_cards` |
| VAT gas households 6% | **635** | From 2022 | `lb_vat_gas_hh` |
| Agriculture intermediate | **379** | Peak 630 (2022) | `lb_ag_intermed_ffs` |
| Gasolie industrial/commercial | **366** | ~366–416 path | taxex series |
| Diesel product residual | **273** | After petrol equalisation | taxex 2024 |
| VAT electricity HH fossil-share | **227** | Companion to gas VAT | taxex series |
| VAT air tickets | **225** | Path 88→225 | `lb_vat_air_tickets` |
| LPG heating | **128** | 109–140 path | `cmt_lpg_heating_ffs` |
| Social tariff gas (permanent) | **96** | Crisis peak 428 (2022) | `lb_social_tariff_gas` |
| Binnenvaart intermediate | **84** | Stable | `lb_binnenvaart_ffs` |
| Coal HH exemption | **11** | Declining; VAT solid fuels cut Jul 2025 | `cmt_coal_hh_exemption_ffs` |
| Sociaal Verwarmingsfonds | **13** | 70k households | `cmt_sociaal_verwarmingsfonds` |

## Related federal tax expenditure inventory (not FFS)

| Aggregate | EUR m | Year | Source |
|-----------|------:|------|--------|
| Federal TE total quantified | **39,402** | 2023 | Inventory of Federal Tax Expenditures (2024 PDF) |
| of which VAT class | 16,198 | 2023 | same |
| of which PIT federal | 9,671 | 2023 | same |
| of which EIWT | 4,415 | 2023 | same |

## Reform notes (from FFS text, not invented savings)

- FFS explicitly warns: abolishing lines ≠ full budget gain (behaviour + compensation).
- Stookolie: FFS says **not justified** environmentally or socially (not lowest-income concentrated).
- Kerosene: needs **EU coordination**; unilateral weak; ETD reform pending.
- Gas VAT 6%: EU rules push toward ending reduced fossil VAT by **2030**; federal path uses gradual gas **excise** rise toward ~12% VAT-equivalent by 2029 (FFS §3.1.3).
- Industrial EBO reduced gas: static efficiency of agreements vs weaker dynamic price signal.
- Social tariff + Verwarmingsfonds: **targeted** instruments preferred as compensation when reforming untargeted product gaps.

## FOI still human-only (not sent by agents)

- `gap_fed_gas_reduced_firms` — firm list for EBO reduced gas (~352 firms 2019; 13.5 TWh 2024).
- Other federal FOI (company cars component split, cheques, etc.) remain in `foi_queue.csv`.

## Coverage status

Top FFS package and major product/use lines for 2021–2024 are now seeded in `tax_expenditures.csv`, `commitments.csv`, and `leaderboard.csv` with primary FFS 2026 sources. Residual work: firm-level L5, Entity split of FFS, regional FFS inventories, and SWA assent tracking (`rq_107`).
""",
    encoding="utf-8",
)
print("wrote", snapshot)

# leaderboard small seeds
with (DATA / "leaderboard.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    lb_fields = r.fieldnames
    lb_rows = list(r)
lb_ids = {x["item_id"] for x in lb_rows}

if "lb_lpg_heating" not in lb_ids:
    row = {k: "" for k in lb_fields}
    row.update(
        {
            "item_id": "lb_lpg_heating",
            "name": "LPG heating fuel FFS preference",
            "level": "federal",
            "type": "tax_expenditure",
            "hierarchy_path": "Federal>FFS>LPG_heating",
            "annual_cost_eur": "127600000",
            "total_cost_eur": "753100000",
            "tco_notes": "FFS Table16 127.6m 2024; path 109-140-128 2019-24",
            "confidence": "strong",
            "source_id": "src_fps_ffs_2026_lpg_coal_t16",
            "beneficiaries": "LPG heating users",
            "stated_goal": "Heating fuel preferential rate",
            "measured_outcome": "Small vs gas/stookolie",
            "absurdity_score": "6",
            "cost_score": "5",
            "difficulty": "5",
            "priority_index": "5.4",
            "cut_proposal": "Equalise energy-basis with other heating fuels",
            "status": "seed",
            "struck_reason": "",
            "notes": "tick114",
        }
    )
    lb_rows.append(row)

with (DATA / "leaderboard.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=lb_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(lb_rows)

# research queue
with (DATA / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)
for row in rq_rows:
    if row["task_id"] == "rq_114":
        row["status"] = "done"
        row["updated_utc"] = UTC
        row["notes"] = (
            "tick114: FFS snapshot md + LPG 128m + coal HH 11m multi-year; top FFS lines map complete"
        )
# only rq_107 left open at prio1 — spawn optional light unit or leave
if not any(r["task_id"] == "rq_115" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_115",
            "title": "Leaderboard priority_index recompute after FFS wave",
            "sprint": "continuous",
            "priority": "2",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "Recompute or document top-15 leaderboard after FFS seeds ticks 109-114; "
                "no invent euros; update leaderboard_top15.md if script available."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "After FFS map wave",
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
            "rq_114",
            114,
            "no",
            "tick114 FFS snapshot+LPG. Next: rq_115 leaderboard recompute or rq_107 SWA; human FOI.",
        ]
    )

with (ROOT / "loop_log.md").open("a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} — tick 114
- Unit: **rq_114** (FFS synthesis snapshot + LPG/coal residual lines)
- Found / wrote:
  - **Synthesis** `docs/doge/data/ffs_federal_top_lines_2024.md`: package totals (direct **€10.78bn**, broad ~**€15.2bn**) + mapped high-EUR lines already in CSVs — **no invented euros**, explicit non-additive warning.
  - **LPG heating** Table16 multi-year: **2019–24 €108.6 / 138.8 / 140.0 / 120.3 / 117.8 / 127.6 m**.
  - **Coal HH** exemption: **27.8 → 10.8 m** 2019–24 (declining); FFS notes reduced VAT solid fuels abolished Jul 2025.
- Wrote: sources +2; taxex LPG+coal series; commitments +2; leaderboard LPG seed; snapshot md; rq_114=done; spawned **rq_115**; ticks=114
- FOI opened: none
- Next: **rq_115** leaderboard recompute (prio2) or low **rq_107** SWA; FFS top-line map largely complete
"""
    )
print("DONE tick114")

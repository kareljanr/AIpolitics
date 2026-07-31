"""Tick 113: rq_113 natural gas product rate-diff FFS multi-year + social tariff path."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
UTC = "2026-07-27T03:00:00Z"

with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(
        "src_fps_ffs_2026_gas_product_t15,FFS 2026 Table15 aardgas product rate differences multi-year,"
        "https://finance.belgium.be/sites/default/files/Statistieken_SD/Inventaris/FFS-report-NL-Master%20ed%202026_final.pdf,"
        "FPS Finance + FPS Health,2026-07-27,budget,"
        '"Table15: gas product-diff 4742/4538/5124/4854/3722/4089 mEUR 2019-24 bench1; end-use split industry 55.8pct; raw p28"\n'
    )
    f.write(
        "src_fps_ffs_2026_social_tariff_t1,FFS 2026 Table1 social tariff gas multi-year,"
        "https://finance.belgium.be/sites/default/files/Statistieken_SD/Inventaris/FFS-report-NL-Master%20ed%202026_final.pdf,"
        "FPS Finance + FPS Health / CREG,2026-07-27,budget,"
        '"Table1: social tariff gas 89/79/95/428/268/96 mEUR 2019-24; RVT extended gas peak 462m 2023"\n'
    )

with (DATA / "tax_expenditures.csv").open("a", encoding="utf-8", newline="") as f:
    gas = [
        (2019, 4741500000),
        (2020, 4538000000),
        (2021, 5124300000),
        (2022, 4854200000),
        (2023, 3722400000),
        (2024, 4089400000),
    ]
    for y, a in gas:
        note = "pre-2022 excludes federal gas contribution break" if y < 2022 else "with special excise from 2022"
        f.write(
            f"tx_ffs_gas_product_diff_{y},Natural gas product rate-diff vs gasoline TOE FFS bench1,federal,{y},{a},EXC,"
            f"src_fps_ffs_2026_gas_product_t15,strong,8,"
            f'"Table15: {a/1e6:.1f} mEUR; {note}"\n'
        )
    f.write(
        "tx_ffs_gas_product_diff_bench2_biz_2024,Natural gas product-diff bench2 business heating,federal,2024,470300000,EXC,"
        "src_fps_ffs_2026_gas_product_t15,strong,7,"
        '"Table15 bench2: 470.3 mEUR business; non-business 1353.3m"\n'
    )
    f.write(
        "tx_ffs_gas_product_diff_bench2_hh_2024,Natural gas product-diff bench2 non-business heating,federal,2024,1353300000,EXC,"
        "src_fps_ffs_2026_gas_product_t15,strong,7,"
        '"Table15 bench2: 1353.3 mEUR non-business heating"\n'
    )
    social = [
        (2019, 89000000),
        (2020, 79000000),
        (2021, 95300000),
        (2022, 428200000),
        (2023, 268200000),
        (2024, 96300000),
    ]
    for y, a in social:
        f.write(
            f"tx_ffs_social_tariff_gas_{y},Social tariff natural gas CREG transfers,federal,{y},{a},transfer,"
            f"src_fps_ffs_2026_social_tariff_t1,strong,4,"
            f'"Table1 permanent social tariff gas: {a/1e6:.1f} mEUR cash to suppliers"\n'
        )
    rvt = [(2021, 36800000), (2022, 378400000), (2023, 462200000), (2024, 27700000)]
    for y, a in rvt:
        f.write(
            f"tx_ffs_social_tariff_gas_rvt_{y},Extended social tariff gas RVT temporary,federal,{y},{a},transfer,"
            f"src_fps_ffs_2026_social_tariff_t1,strong,4,"
            f'"Table1 RVT extension: {a/1e6:.1f} mEUR; crisis peak 2023"\n'
        )
    f.write(
        "tx_ffs_diesel_product_diff_2024,Diesel low-S product rate-diff vs gasoline TOE FFS,federal,2024,273300000,EXC,"
        "src_fps_ffs_2026_gas_product_t15,strong,6,"
        '"Table15: 273.3 mEUR residual diesel-petrol energy gap after 2015-19 equalisation"\n'
    )

new_cmts = [
    {
        "commitment_id": "cmt_gas_product_rate_diff_ffs",
        "title": "Natural gas product rate differential vs gasoline TOE (FFS bench1)",
        "entity_id": "fod_finance",
        "beneficiary": "All natural gas end-users (industry 55.8% of final use)",
        "legal_basis": "Excise structure energy products vs gasoline TOE neutrality benchmark",
        "decision_date": "2005-01-01",
        "start_year": "2019",
        "end_year": "2024",
        "total_envelope_eur": "27073300000",
        "cash_by_year": (
            '{"2019":4741500000,"2020":4538000000,"2021":5124300000,"2022":4854200000,'
            '"2023":3722400000,"2024":4089400000,"end_use_industry_pct":55.8,'
            '"end_use_housing_pct":25.2,"end_use_commercial_pct":12.8,'
            '"bench2_biz_2024":470300000,"bench2_hh_2024":1353300000,'
            '"method_note":"pre2022_excludes_fed_gas_contribution"}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "",
        "stated_goal": "Historical lower taxation of gas vs petrol energy content",
        "cut_option": "Equalise energy-basis excise; protect vulnerable via social tariff not untargeted product gap",
        "source_id": "src_fps_ffs_2026_gas_product_t15",
        "confidence": "strong",
        "hierarchy_path": "Federal>FFS>gas_product_diff",
        "notes": (
            "tick113: largest single FFS product-diff line; NOT same as reduced industrial EBO rate (903m separate); "
            "do not double-count; opportunity cost vs gasoline TOE not cash grant"
        ),
    },
    {
        "commitment_id": "cmt_social_tariff_gas",
        "title": "Social tariff natural gas CREG transfers multi-year",
        "entity_id": "fod_finance",
        "beneficiary": "Protected energy customers (social tariff categories)",
        "legal_basis": "Social energy tariff via CREG supplier compensation",
        "decision_date": "2004-01-01",
        "start_year": "2019",
        "end_year": "2024",
        "total_envelope_eur": "1056200000",
        "cash_by_year": (
            '{"2019":89000000,"2020":79000000,"2021":95300000,"2022":428200000,'
            '"2023":268200000,"2024":96300000,"rvt_2021":36800000,"rvt_2022":378400000,'
            '"rvt_2023":462200000,"rvt_2024":27700000}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://www.creg.be/nl/consumenten/prijzen-en-tarieven/sociaal-tarief",
        "stated_goal": "Targeted energy affordability for vulnerable households",
        "cut_option": "Prefer targeted social tariff over untargeted gas product-diff; maintain after excise equalisation",
        "source_id": "src_fps_ffs_2026_social_tariff_t1",
        "confidence": "strong",
        "hierarchy_path": "Federal>FFS>social_tariff_gas",
        "notes": "tick113: crisis RVT peak 462m 2023 then collapsed; permanent social ~96m 2024; contrast to 4.09bn product-diff",
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

with (DATA / "leaderboard.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    lb_fields = r.fieldnames
    lb_rows = list(r)
lb_ids = {x["item_id"] for x in lb_rows}

if "lb_gas_product_diff" not in lb_ids:
    row = {k: "" for k in lb_fields}
    row.update(
        {
            "item_id": "lb_gas_product_diff",
            "name": "Natural gas product rate-diff vs gasoline TOE (FFS)",
            "level": "federal",
            "type": "tax_expenditure",
            "hierarchy_path": "Federal>FFS>gas_product_diff",
            "annual_cost_eur": "4089400000",
            "total_cost_eur": "27073300000",
            "tco_notes": "FFS Table15 4089m 2024; path 4742-5124-4089 2019-24; industry 55.8pct end-use",
            "confidence": "strong",
            "source_id": "src_fps_ffs_2026_gas_product_t15",
            "beneficiaries": "All gas users (industry majority of final consumption)",
            "stated_goal": "Historical lower energy-content tax on gas",
            "measured_outcome": "Dominant FFS product-diff line; volume-driven 2023 dip then rebound",
            "absurdity_score": "7",
            "cost_score": "9.5",
            "difficulty": "7",
            "priority_index": "8.0",
            "cut_proposal": "Energy-basis equalisation path; protect poor via social tariff not product gap",
            "status": "seed",
            "struck_reason": "",
            "notes": "tick113; separate from EBO reduced rate 903m and VAT 6pct 635m — do not sum carelessly",
        }
    )
    lb_rows.append(row)

if "lb_social_tariff_gas" not in lb_ids:
    row = {k: "" for k in lb_fields}
    row.update(
        {
            "item_id": "lb_social_tariff_gas",
            "name": "Social tariff natural gas (targeted cash via CREG)",
            "level": "federal",
            "type": "subsidy",
            "hierarchy_path": "Federal>FFS>social_tariff_gas",
            "annual_cost_eur": "96300000",
            "total_cost_eur": "481500000",
            "tco_notes": "Permanent social 96.3m 2024; crisis RVT peak 462m 2023 then 28m",
            "confidence": "strong",
            "source_id": "src_fps_ffs_2026_social_tariff_t1",
            "beneficiaries": "Protected customer categories",
            "stated_goal": "Targeted energy poverty relief",
            "measured_outcome": "Crisis expansion temporary; permanent line modest vs 4bn product-diff",
            "absurdity_score": "2",
            "cost_score": "4",
            "difficulty": "4",
            "priority_index": "3.4",
            "cut_proposal": "Keep/strengthen as compensation when reforming untargeted gas TE",
            "status": "seed",
            "struck_reason": "",
            "notes": "tick113; steelman good instrument relative to untargeted FFS",
        }
    )
    lb_rows.append(row)

with (DATA / "leaderboard.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=lb_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(lb_rows)
print("leaderboard", len(lb_rows))

with (DATA / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(
        "bud_ffs_gas_product_diff_2024,fod_finance,2024,4089400000,,,estimated,"
        "src_fps_ffs_2026_gas_product_t15,strong,"
        '"FFS product rate-diff gas 4.089bn opportunity cost vs gasoline TOE"\n'
    )

with (DATA / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)
for row in rq_rows:
    if row["task_id"] == "rq_113":
        row["status"] = "done"
        row["updated_utc"] = UTC
        row["notes"] = (
            "tick113: gas product-diff 4089m 2024 path; social tariff gas 96m permanent + RVT peak; "
            "industry 55.8pct end-use; no FOI needed for aggregates"
        )
if not any(r["task_id"] == "rq_114" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_114",
            "title": "FFS inventory synthesis snapshot or remaining heating LPG/coal lines",
            "sprint": "continuous",
            "priority": "2",
            "status": "open",
            "hierarchy_target": "taxex",
            "entity_id": "fod_finance",
            "instructions": (
                "Optional synthesis markdown of FFS top lines already mapped (no invent euros) "
                "OR extract LPG heating 127.6m + coal HH 10.8m multi-year from Table16."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "After gas product-diff; FFS map largely filled for top lines",
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
            "rq_113",
            113,
            "no",
            "tick113 gas product-diff 4.09bn. Next: rq_114 FFS synth/LPG or rq_107 SWA; human FOI stack.",
        ]
    )

with (ROOT / "loop_log.md").open("a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} — tick 113
- Unit: **rq_113** (Natural gas product rate-diff FFS + social tariff path)
- Found (strong FFS 2026 Tables 15+1):
  - **Aardgas product rate-diff** (bench1 vs gasoline TOE): **2019–24 €4,741.5 / 4,538.0 / 5,124.3 / 4,854.2 / 3,722.4 / 4,089.4 m**. Largest single product-diff line. End-use: industry **55.8%**, housing **25.2%**, commercial **12.8%**, agriculture **4.9%**, transport **1.4%**. Bench2 2024 split: business **€470.3m** + non-business **€1,353.3m**. Pre-2022 series exclude federal gas contribution (method break).
  - **Not double-count** with EBO reduced rate (€903m) or VAT 6% gas HH (€635m) — different instruments.
  - **Sociaal tarief gas** (permanent CREG cash): **89 / 79 / 95 / 428 / 268 / 96 m** 2019–24. **RVT extension** peak **€462.2m** 2023 then **€27.7m** 2024. Targeted contrast to untargeted €4.09bn product gap.
  - Diesel product residual after petrol equalisation: **€273.3m** 2024.
- Wrote: sources +2; taxex multi-year gas product-diff + social/RVT + diesel residual; commitments +2; leaderboard +2; budgets +1; rq_113=done; spawned **rq_114**; ticks=113
- FOI opened: none (aggregates fully public)
- Next: **rq_114** FFS synthesis/LPG or low **rq_107** SWA
"""
    )
print("DONE tick113")

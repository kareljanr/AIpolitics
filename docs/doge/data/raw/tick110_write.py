"""Tick 110: rq_110 kerosene aviation + VAT gas HH multi-year from FFS 2026."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
UTC = "2026-07-27T02:00:00Z"

# --- sources ---
with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(
        "src_fps_ffs_2026_kerosene_t20,FFS 2026 full Table20 aviation kerosene multi-year,"
        "https://finance.belgium.be/sites/default/files/Statistieken_SD/Inventaris/FFS-report-NL-Master%20ed%202026_final.pdf,"
        "FPS Finance + FPS Health,2026-07-27,budget,"
        '"Table20: 677/472/594/688/690/755 mEUR 2019-24 at ETD min 330EUR/1000l; raw fps_ffs_2026_nl_full.pdf p44"\n'
    )
    f.write(
        "src_fps_ffs_2026_vat_energy,FFS 2026 Table3 VAT reduced gas+electricity households,"
        "https://climat.be/doc/ffs-2026-samenvatting-nl.pdf,"
        "FPS Finance + FPS Health,2026-07-27,budget,"
        '"VAT gas HH 0/610.1/694.3/635.2; electricity HH 0/277.1/285.6/226.9 mEUR 2021-24"\n'
    )
    f.write(
        "src_pwc_boarding_tax_2026,PwC Belgium tax reform 2026 aircraft boarding tax path,"
        "https://news.pwc.be/belgian-tax-reform-2026-tax-and-social-measures-of-the-programme-law/,"
        "PwC Belgium,2026-07-27,secondary,"
        '"Boarding tax from 2027: 5 to 10 EUR long-haul plan; short-haul steps; not kerosene excise; medium confidence"\n'
    )

# --- tax_expenditures multi-year rows ---
with (DATA / "tax_expenditures.csv").open("a", encoding="utf-8", newline="") as f:
    series_k = [
        (2019, 677000000),
        (2020, 471800000),
        (2021, 594200000),
        (2022, 687700000),
        (2023, 689500000),
        (2024, 754600000),
    ]
    for y, a in series_k:
        f.write(
            f"tx_ffs_kerosene_air_{y},Excise exemption kerosene international aviation FFS,federal,{y},{a},EXC,"
            f"src_fps_ffs_2026_kerosene_t20,strong,8,"
            f'"Table20 FFS 2026: {a/1e6:.1f} mEUR vs ETD min 330EUR/1000l; minimal estimate"\n'
        )
    series_gas = [(2021, 0), (2022, 610100000), (2023, 694300000), (2024, 635200000)]
    for y, a in series_gas:
        f.write(
            f"tx_ffs_vat_gas_hh_{y},VAT reduced rate gas households FFS,federal,{y},{a},VAT,"
            f"src_fps_ffs_2026_vat_energy,strong,6,"
            f'"Table3: {a/1e6:.1f} mEUR; 6pct crisis rate extended permanent from 2023 class"\n'
        )
    series_el = [(2021, 0), (2022, 277100000), (2023, 285600000), (2024, 226900000)]
    for y, a in series_el:
        f.write(
            f"tx_ffs_vat_elec_hh_{y},VAT reduced rate electricity households FFS fossil-share,federal,{y},{a},VAT,"
            f"src_fps_ffs_2026_vat_energy,strong,5,"
            f'"Table3 fossil mix share: {a/1e6:.1f} mEUR; not full electricity TE"\n'
        )
    series_ticket = [
        (2021, 87500000),
        (2022, 180400000),
        (2023, 208800000),
        (2024, 224500000),
    ]
    for y, a in series_ticket:
        f.write(
            f"tx_ffs_vat_air_tickets_{y},VAT exemption/zero international air tickets FFS,federal,{y},{a},VAT,"
            f"src_fps_ffs_2026_summary_nl,strong,7,"
            f'"Table3 indirect: {a/1e6:.1f} mEUR; grandfathered international passenger transport"\n'
        )

# --- commitments ---
new_cmts = [
    {
        "commitment_id": "cmt_kerosene_air_exemption",
        "title": "Aviation kerosene excise exemption multi-year FFS",
        "entity_id": "fod_finance",
        "beneficiary": "International aviation operators fueling in Belgium",
        "legal_basis": "EU Energy Tax Directive art 14(1)(b); Chicago Convention practice",
        "decision_date": "2003-01-01",
        "start_year": "2019",
        "end_year": "2024",
        "total_envelope_eur": "3874800000",
        "cash_by_year": (
            '{"2019":677000000,"2020":471800000,"2021":594200000,"2022":687700000,'
            '"2023":689500000,"2024":754600000,"benchmark":"ETD_min_330EUR_per_1000l",'
            '"etd_reform_target_class":"467.5EUR_per_1000l_after_10y"}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://finance.belgium.be/nl/Statistieken_en_analysen/analysen/inventaris-van-subsidies-voor-fossiele-brandstoffen",
        "stated_goal": "Legacy international aviation tax regime",
        "cut_option": "EU ETD reform coordination; not unilateral; boarding tax partial substitute (separate instrument)",
        "source_id": "src_fps_ffs_2026_kerosene_t20",
        "confidence": "strong",
        "hierarchy_path": "Federal>FFS>aviation_kerosene",
        "notes": (
            "tick110: FFS eval says unjustified economically/environmentally; national solo tax weak; "
            "coalition 2025-29 cites Chicago revision; boarding tax reform secondary medium"
        ),
    },
    {
        "commitment_id": "cmt_vat_gas_hh_reduced",
        "title": "VAT reduced rate natural gas households multi-year FFS",
        "entity_id": "fod_finance",
        "beneficiary": "Household gas consumers",
        "legal_basis": "Crisis VAT cut energy 2022; extended permanent class from 2023",
        "decision_date": "2022-01-01",
        "start_year": "2022",
        "end_year": "2024",
        "total_envelope_eur": "1939600000",
        "cash_by_year": (
            '{"2021":0,"2022":610100000,"2023":694300000,"2024":635200000,'
            '"rate":"6pct_vs_21pct","companion_elec_2024":226900000}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "",
        "stated_goal": "Affordable household energy / crisis response",
        "cut_option": "Shift support to targeted cash/social tariff; gradual excise/VAT rebalance toward electricity",
        "source_id": "src_fps_ffs_2026_vat_energy",
        "confidence": "strong",
        "hierarchy_path": "Federal>FFS>VAT_gas_HH",
        "notes": (
            "tick110: permanent 6pct class per FFS; budget 2026-29 plans gas excise up / elec down "
            "(secondary press) — not invent revenue"
        ),
    },
    {
        "commitment_id": "cmt_vat_air_tickets_exemption",
        "title": "VAT zero/exemption international air passenger tickets",
        "entity_id": "fod_finance",
        "beneficiary": "International air passengers / airlines",
        "legal_basis": "VAT Code art 41; EU grandfathering international passenger transport",
        "decision_date": "2006-01-01",
        "start_year": "2021",
        "end_year": "2024",
        "total_envelope_eur": "701200000",
        "cash_by_year": '{"2021":87500000,"2022":180400000,"2023":208800000,"2024":224500000}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "",
        "stated_goal": "International transport VAT legacy",
        "cut_option": "EU place-of-supply reform; domestic 6pct already (Table14 FFS)",
        "source_id": "src_fps_ffs_2026_summary_nl",
        "confidence": "strong",
        "hierarchy_path": "Federal>FFS>VAT_air_tickets",
        "notes": "tick110; stacks on kerosene exemption; domestic flights BE 6pct reduced",
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

# --- leaderboard update kerosene + add VAT gas ---
with (DATA / "leaderboard.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    lb_fields = r.fieldnames
    lb_rows = list(r)
lb_ids = {x["item_id"] for x in lb_rows}

for row in lb_rows:
    if row["item_id"] == "lb_ffs_kerosene_air":
        row["tco_notes"] = (
            "FFS Table20 multi-year 677/472/594/688/690/755 m 2019-24; sum 3.87bn; rising post-COVID"
        )
        row["total_cost_eur"] = "3874800000"
        row["source_id"] = "src_fps_ffs_2026_kerosene_t20"
        row["cut_proposal"] = (
            "EU ETD phase-in; Chicago coordination; boarding tax only partial substitute"
        )
        row["notes"] = "tick110 multi-year filled; FFS eval unjustified eco+env"

if "lb_vat_gas_hh" not in lb_ids:
    row = {k: "" for k in lb_fields}
    row.update(
        {
            "item_id": "lb_vat_gas_hh",
            "name": "VAT reduced rate gas households (6pct)",
            "level": "federal",
            "type": "tax_expenditure",
            "hierarchy_path": "Federal>FFS>VAT_gas_HH",
            "annual_cost_eur": "635200000",
            "total_cost_eur": "1939600000",
            "tco_notes": "FFS 635.2m 2024; path 0/610/694/635 2021-24; crisis permanent class",
            "confidence": "strong",
            "source_id": "src_fps_ffs_2026_vat_energy",
            "beneficiaries": "Household natural gas consumers",
            "stated_goal": "Energy affordability / crisis response",
            "measured_outcome": "Broad price subsidy not income-targeted; social tariff separate",
            "absurdity_score": "6",
            "cost_score": "7",
            "difficulty": "6",
            "priority_index": "6.4",
            "cut_proposal": "Retarget via social tariff/cash; rebalance gas vs electricity tax path",
            "status": "seed",
            "struck_reason": "",
            "notes": "tick110; companion elec HH fossil-share 226.9m 2024",
        }
    )
    lb_rows.append(row)

if "lb_vat_air_tickets" not in lb_ids:
    row = {k: "" for k in lb_fields}
    row.update(
        {
            "item_id": "lb_vat_air_tickets",
            "name": "VAT exemption international air tickets",
            "level": "federal",
            "type": "tax_expenditure",
            "hierarchy_path": "Federal>FFS>VAT_air_tickets",
            "annual_cost_eur": "224500000",
            "total_cost_eur": "1122500000",
            "tco_notes": "FFS 224.5m 2024; path 87.5/180/209/225; stacks with kerosene",
            "confidence": "strong",
            "source_id": "src_fps_ffs_2026_summary_nl",
            "beneficiaries": "International air passengers airlines",
            "stated_goal": "International transport VAT legacy",
            "measured_outcome": "Recovered post-COVID; EU reform stuck",
            "absurdity_score": "7",
            "cost_score": "6",
            "difficulty": "8",
            "priority_index": "6.5",
            "cut_proposal": "EU destination-based VAT; domestic already 6pct",
            "status": "seed",
            "struck_reason": "",
            "notes": "tick110",
        }
    )
    lb_rows.append(row)

with (DATA / "leaderboard.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=lb_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(lb_rows)
print("leaderboard", len(lb_rows))

# --- research_queue ---
with (DATA / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)
for row in rq_rows:
    if row["task_id"] == "rq_110":
        row["status"] = "done"
        row["updated_utc"] = UTC
        row["notes"] = (
            "tick110: kerosene 2019-24 677→755m; VAT gas HH 610/694/635; air tickets 88→225; "
            "ETD reform path; boarding tax separate secondary"
        )
if not any(r["task_id"] == "rq_111" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_111",
            "title": "Heating gas oil / stookolie FFS multi-year or agriculture intermediate",
            "sprint": "continuous",
            "priority": "3",
            "status": "open",
            "hierarchy_target": "taxex",
            "entity_id": "fod_finance",
            "instructions": (
                "From FFS 2026: deepen stookolie 1836m 2024 multi-year and/or agriculture "
                "intermediate 378.5m; link taxex inventory lines if public."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "Next large FFS heating/ag lines after kerosene+gas VAT",
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
            "rq_110",
            110,
            "no",
            "tick110 kerosene+VAT gas multi-year. Next: rq_111 stookolie/ag or rq_107 SWA; human FOI.",
        ]
    )

# --- log ---
with (ROOT / "loop_log.md").open("a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} — tick 110
- Unit: **rq_110** (Kerosene aviation + VAT gas HH multi-year / reform notes)
- Found (strong FFS 2026 primary):
  - **Aviation kerosene** (Table 20, ETD min €330/1000l): **2019–24 €677.0 / 471.8 / 594.2 / 687.7 / 689.5 / 754.6 m** — rising post-COVID; sum **€3.875bn**. FFS eval: unjustified economically and environmentally; unilateral national tax weak; EU ETD proposal higher rate after 10y transition still blocked; coalition 2025–29 cites Chicago Convention revision.
  - **VAT gas households 6%**: **2021–24 €0 / 610.1 / 694.3 / 635.2 m**; electricity HH fossil-share **0 / 277.1 / 285.6 / 226.9 m**. Crisis cut made permanent class.
  - **VAT air tickets** (indirect): **87.5 / 180.4 / 208.8 / 224.5 m** 2021–24; stacks on kerosene.
  - **Boarding tax** (separate instrument, not kerosene): budget/programme law path €5→€10 from 2027 class; later press scaled to €7 — **medium secondary**, not FFS inventory.
- Wrote: sources +3; tax_expenditures multi-year series (kerosene 6y + VAT gas/elec/tickets); commitments +3; leaderboard refresh kerosene +2 seeds; rq_110=done; spawned **rq_111**; ticks=110
- FOI opened: none
- Next: **rq_111** stookolie/agriculture FFS or low **rq_107** SWA
"""
    )
print("DONE tick110")

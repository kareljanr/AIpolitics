"""Finish tick 107 writes after partial failure (restore-safe)."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent

# --- commitments ---
with (DATA / "commitments.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

updated = False
for row in rows:
    if row["commitment_id"] == "cmt_vl_carbon_leakage_cie_2025":
        row["start_year"] = "2024"
        row["end_year"] = "2026"
        row["total_envelope_eur"] = "728431000"
        row["cash_by_year"] = (
            '{"2024_fio_vek":250234000,"2025_fio_vek":261588000,"2026_fio_vek_bo":216609000,'
            '"2025_awarded_ey2024":258000000,"2025_exception_2022_23":40000000,'
            '"2024_pq_cited":229000000,"firms_est_2026":40,"benchmark_miss_firms":14,'
            '"clawbacks_2020_24":19898396}'
        )
        row["source_id"] = "src_vl_bo2026_ewi_tech_icl"
        row["notes"] = (
            "tick107: FIO VEK path strong from tech vragen; PQ251 258m award +40m exception; "
            "PQ28 229m 2024 class + clawbacks 19.9m; named L5 FOI gap_vl_cie_l5_beneficiaries"
        )
        row["cut_option"] = (
            "Publish full L5 beneficiaries; enforce investment obligation audits from 2028; "
            "align intensity with ETS reform; FOI gap_vl_cie_l5_beneficiaries"
        )
        updated = True

if not updated:
    raise SystemExit("cmt_vl_carbon_leakage_cie_2025 missing")

if not any(r["commitment_id"] == "cmt_vl_cie_exception_crisis" for r in rows):
    rows.append(
        {
            "commitment_id": "cmt_vl_cie_exception_crisis",
            "title": "CIE exception mechanism energy crisis moresteun 95pct class",
            "entity_id": "vlaio",
            "beneficiary": "Energy-intensive CIE firms hit 2022-2023",
            "legal_basis": "CIE uitzonderingsmechanisme / meersteun tot 95pct",
            "decision_date": "2023-01-01",
            "start_year": "2022",
            "end_year": "2025",
            "total_envelope_eur": "40000000",
            "cash_by_year": (
                '{"pq251_paid":40000000,"tech_extra_class":45000000,'
                '"firms_class":14,"financing":"energiecrisisbudget_2023_extended_FIO_2025"}'
            ),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "",
            "stated_goal": "Temporary higher intensity for crisis-hit energy-intensive plants",
            "cut_option": "Sunset; publish named 14; additionality vs standard 75pct",
            "source_id": "src_vl_pq_cie_251_2026",
            "confidence": "strong",
            "hierarchy_path": "Vlaanderen>VLAIO>CIE>exception",
            "notes": "PQ251 40m paid; tech vragen 45m class for 14 firms; not separate BO line",
        }
    )

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
for row in lb_rows:
    if row["item_id"] == "lb_vl_carbon_leakage_cie":
        row["annual_cost_eur"] = "261588000"
        row["total_cost_eur"] = "728431000"
        row["tco_notes"] = (
            "FIO VEK 250.2/261.6/216.6m 2024-26 strong; PQ251 258m award EY2024; "
            "~40 firms; L5 names FOI; clawbacks 19.9m 2020-24"
        )
        row["source_id"] = "src_vl_bo2026_ewi_tech_icl"
        row["measured_outcome"] = (
            "Invest obligation controls not yet started (to 2028 EY2021); "
            "14 firms miss product electricity benchmark; clawbacks 19.9m other conditions"
        )
        row["cost_score"] = "8"
        row["difficulty"] = "5"
        row["priority_index"] = "6.35"
        row["cut_proposal"] = (
            "Publish L5 beneficiaries; start invest audits; FOI gap_vl_cie_l5; "
            "review intensity under new EC guidelines"
        )
        row["notes"] = (
            "tick107 primary PQs+tech vragen supersede Speurgids-only; steelman EU CIE; "
            "largest VLAIO firm subsidy (PQ28 229m 2024 class)"
        )
with (DATA / "leaderboard.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=lb_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(lb_rows)
print("leaderboard ok")

# --- foi ---
with (DATA / "foi_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    foi_fields = r.fieldnames
    foi_rows = list(r)
if not any(x["gap_id"] == "gap_vl_cie_l5_beneficiaries" for x in foi_rows):
    row = {k: "" for k in foi_fields}
    row.update(
        {
            "gap_id": "gap_vl_cie_l5_beneficiaries",
            "hierarchy_path": "Vlaanderen>VLAIO>Carbon_leakage_CIE>beneficiaries_L5",
            "entity_id": "vlaio",
            "what_is_missing": (
                "Named CIE/ICL beneficiaries with amounts KBO emission-year 2023-2026 "
                "and exception-mechanism list"
            ),
            "why_it_matters": (
                "Largest VLAIO company subsidy ~250-262m/yr; totals public; L5 names opaque"
            ),
            "priority": "8",
            "recipient_body": "Vlaamse overheid Team Openbaarheid / VLAIO FIO",
            "recipient_email": "openbaarheid@vlaanderen.be",
            "recipient_postal": "Havenlaan 88 bus 20 1000 Brussel",
            "draft_letter_path": "docs/doge/foi/drafts/gap_vl_cie_l5_beneficiaries.md",
            "status": "ready",
            "date_ready": "2026-07-27",
            "linked_commitment_id": "cmt_vl_carbon_leakage_cie_2025",
            "linked_leaderboard_id": "lb_vl_carbon_leakage_cie",
            "created_utc": "2026-07-27T01:00:00Z",
            "updated_utc": "2026-07-27T01:00:00Z",
            "notes": "rq_106 draft ready human send only; NL letter",
        }
    )
    foi_rows.append(row)
with (DATA / "foi_queue.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=foi_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(foi_rows)
print("foi", len(foi_rows))

# --- research_queue ---
with (DATA / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)
for row in rq_rows:
    if row["task_id"] == "rq_106":
        row["status"] = "blocked_foi"
        row["blocked_gap_id"] = "gap_vl_cie_l5_beneficiaries"
        row["updated_utc"] = "2026-07-27T01:00:00Z"
        row["notes"] = (
            "tick107: FIO path 250.2/261.6/216.6m 2024-26 strong; ~40 firms; "
            "14 benchmark miss; clawbacks 19.9m; named L5 FOI ready"
        )
if not any(r["task_id"] == "rq_108" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_108",
            "title": "VLAIO FIO bedrijfssteun O&O named L5 sample or open data",
            "sprint": "continuous",
            "priority": "4",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "vlaio",
            "instructions": (
                "Speurgids FIO bedrijfssteun O&O 210.9m BO2025: extract 3+ named "
                "projects/amounts from public VLAIO jaarverslag lists or FOI if portal blocked."
            ),
            "blocked_gap_id": "",
            "created_utc": "2026-07-27T01:00:00Z",
            "updated_utc": "2026-07-27T01:00:00Z",
            "notes": "After CIE tick107; next largest FIO company innovation envelope",
        }
    )
with (DATA / "research_queue.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(rq_rows)
print(
    "rq",
    len(rq_rows),
    [(r["task_id"], r["status"]) for r in rq_rows if r["status"] in ("open", "blocked_foi")],
)

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
            "2026-07-27T01:00:00Z",
            "rq_106",
            107,
            "no",
            "tick107 CIE path filled; L5 FOI ready. Next: rq_108 FIO O&O L5; human FOI incl CIE.",
        ]
    )
print("state ok")

# --- loop_log ---
log = ROOT / "loop_log.md"
tail = log.read_text(encoding="utf-8")[-3000:]
if "— tick 107" not in tail:
    log.open("a", encoding="utf-8").write(
        """
### 2026-07-27T01:00:00Z — tick 107
- Unit: **rq_106** (Carbon leakage CIE L5 beneficiaries / evaluation)
- Found (strong totals; L5 names still opaque):
  - **FIO VEK ICL** (BO2026 tech vragen, keuro): **2024 250.234m** / **2025 261.588m** / **2026 BO 216.609m** — matches Speurgids 261.59m for 2025.
  - **PQ 251** (Diependaele 20 Feb 2026): **€258m** toegekend in 2025 voor emissiejaar 2024; **+€40m** uitzonderingsmechanisme EY 2022–23; budget **€216m** 2026.
  - **PQ 28** (2 Oct 2025): CIE = **grootste VLAIO-bedrijfssubsidie**; cite **€229m in 2024**; investeringsplicht-controles nog niet gestart (tot 2028 voor EY2021); **14 bedrijven** missen product-elektriciteitsbenchmark (50% herinvestering); terugvorderingen **€19.898.396** (2020–24).
  - Tech vragen: raming **~40 bedrijven** 2026; 75% standaard; **geen publieke naam+EUR-lijst**.
  - Steelman: EU-toegelaten carbon-leakage correctie; opacity L5 is the DOGE issue.
- Wrote: sources +3; programmes CIE 2024–26; commitments cash path + exception cmt; leaderboard refresh; **FOI gap_vl_cie_l5_beneficiaries ready**; rq_106=blocked_foi; spawned **rq_108** FIO O&O L5; raw PQs + tech PDF; ticks=107
- FOI opened: **gap_vl_cie_l5_beneficiaries** → ready (human send only)
- Next: **rq_108** VLAIO FIO bedrijfssteun O&O L5 sample; human FOI stack includes CIE
"""
    )
print("log ok DONE")

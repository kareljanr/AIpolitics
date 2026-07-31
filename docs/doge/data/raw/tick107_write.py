"""Tick 107: rq_106 Carbon leakage CIE L5 — public totals + FOI for beneficiaries."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent

# --- sources ---
with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(
        "src_vl_pq_cie_251_2026,VP schriftelijke vraag 251 Platteau/Diependaele CIE 20 Feb 2026,"
        "https://docs.vlaamsparlement.be/pfile?id=2302041,Vlaams Parlement / Diependaele,"
        "2026-07-27,parliament,"
        '"258m awarded 2025 for emission year 2024; +40m exception 2022-23; budget 2026 216m; '
        'raw vl_pq_cie_feb2026.pdf"\n'
    )
    f.write(
        "src_vl_pq_cie_28_2025,VP schriftelijke vraag 28 Faraji/Diependaele CIE investeringsplicht 2 Oct 2025,"
        "https://docs.vlaamsparlement.be/pfile?id=2228308,Vlaams Parlement / Diependaele,"
        "2026-07-27,parliament,"
        '"CIE largest VLAIO company subsidy 229m 2024; 14 firms miss electricity benchmark; '
        'clawbacks 19.90m 2020-24; invest controls not yet started; raw vl_pq_cie_oct2025.pdf"\n'
    )
    f.write(
        "src_vl_bo2026_ewi_tech_icl,BO2026 (W)EWI(S) technische vragen ICL/CIE budget path,"
        "https://docs.vlaamsparlement.be/pfile?id=2250753,Vlaams Parlement / Vlaamse Regering,"
        "2026-07-27,budget,"
        '"FIO VEK ICL keuro 2024 250234 / 2025 261588 / 2026 216609; ~40 firms 2026 estimate; '
        'VKF vs algemene middelen split; no named L5 list; raw vl_bo2026_ewi_tech_vragen.pdf"\n'
    )

# --- programmes multi-year series ---
with (DATA / "programmes.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(
        "cie_fio_vek_2024,vlaio,,CIE,Compensatie indirecte emissiekosten FIO VEK 2024,,"
        "2024,250234000,src_vl_bo2026_ewi_tech_icl,strong,Vlaanderen>VLAIO>CIE,"
        '"Tech vragen BO2026: FIO-uitgaven 250.234 mEUR VEK 2024"\n'
    )
    f.write(
        "cie_fio_vek_2025,vlaio,,CIE,Compensatie indirecte emissiekosten FIO VEK 2025,,"
        "2025,261588000,src_vl_bo2026_ewi_tech_icl,strong,Vlaanderen>VLAIO>CIE,"
        '"Tech vragen: 261.588 mEUR matches Speurgids 261.59m; PQ251: 258m awarded for EY2024"\n'
    )
    f.write(
        "cie_fio_vek_2026,vlaio,,CIE,Compensatie indirecte emissiekosten FIO VEK BO2026,,"
        "2026,216609000,src_vl_bo2026_ewi_tech_icl,strong,Vlaanderen>VLAIO>CIE,"
        '"Tech vragen + PQ251: 216.609 mEUR BO2026 / 216m minister answer"\n'
    )

# --- update commitment cash path ---
cmt_path = DATA / "commitments.csv"
with cmt_path.open(newline="", encoding="utf-8") as f:
    fields = None
    rows = []
    r = csv.DictReader(f)
    fields = r.fieldnames
    for row in r:
        if row["commitment_id"] == "cmt_vl_carbon_leakage_cie_2025":
            row["start_year"] = "2024"
            row["end_year"] = "2026"
            row["total_envelope_eur"] = "728431000"  # 250.234+261.588+216.609 m
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
        rows.append(row)

with cmt_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

# add exception mechanism commitment
if not any(r["commitment_id"] == "cmt_vl_cie_exception_crisis" for r in rows):
    with cmt_path.open("a", encoding="utf-8", newline="") as f:
        f.write(
            "cmt_vl_cie_exception_crisis,"
            "CIE exception mechanism energy crisis moresteun 95pct class,"
            "vlaio,Energy-intensive CIE firms hit 2022-2023,"
            "CIE uitzonderingsmechanisme / meersteun tot 95pct,"
            "2023-01-01,2022,2025,40000000,"
            '"{\\"pq251_paid\\":40000000,\\"tech_extra_class\\":45000000,\\"firms_class\\":14,'
            '\\"financing\\":\\"energiecrisisbudget_2023_extended_FIO_2025\\"}",,'
            "active,,"
            "Temporary higher intensity for crisis-hit energy-intensive plants,"
            "Sunset; publish named 14; additionality vs standard 75pct,"
            "src_vl_pq_cie_251_2026,strong,Vlaanderen>VLAIO>CIE>exception,"
            "PQ251 40m paid; tech vragen 45m class for 14 firms; not in BO2025/26 line as separate\n"
        )

# --- leaderboard update ---
lb_path = DATA / "leaderboard.csv"
with lb_path.open(newline="", encoding="utf-8") as f:
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
            "Investment obligation controls not yet started (to 2028 for EY2021); "
            "14 firms miss product electricity benchmark; clawbacks 19.9m other conditions"
        )
        row["absurdity_score"] = "5"
        row["cost_score"] = "8"
        row["difficulty"] = "5"
        # priority ~ 0.45*5 + 0.35*8 + 0.2*(10-5) = 2.25+2.8+1.0 = 6.05
        row["priority_index"] = "6.35"
        row["cut_proposal"] = (
            "Publish L5 beneficiaries; start invest audits; FOI gap_vl_cie_l5; "
            "review intensity under new EC guidelines"
        )
        row["notes"] = (
            "tick107 primary PQs+tech vragen supersede Speurgids-only; steelman EU CIE; "
            "largest VLAIO firm subsidy (PQ28 229m 2024 class)"
        )

with lb_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=lb_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(lb_rows)

# --- foi_queue ---
foi_path = DATA / "foi_queue.csv"
with foi_path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    foi_fields = r.fieldnames
    foi_rows = list(r)

if not any(x["gap_id"] == "gap_vl_cie_l5_beneficiaries" for x in foi_rows):
    foi_rows.append(
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
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "cmt_vl_carbon_leakage_cie_2025",
            "linked_leaderboard_id": "lb_vl_carbon_leakage_cie",
            "created_utc": "2026-07-27T01:00:00Z",
            "updated_utc": "2026-07-27T01:00:00Z",
            "notes": "rq_106 draft ready human send only; NL letter",
        }
    )
    with foi_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=foi_fields, lineterminator="\n")
        w.writeheader()
        w.writerows(foi_rows)

# --- research_queue ---
rq_path = DATA / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)

for row in rq_rows:
    if row["task_id"] == "rq_106":
        row["status"] = "blocked_foi"
        row["blocked_gap_id"] = "gap_vl_cie_l5_beneficiaries"
        row["updated_utc"] = "2026-07-27T01:00:00Z"
        row["notes"] = (
            "tick107: FIO path 250.2/261.6/216.6m 2024-26 strong; ~40 firms; 14 benchmark miss; "
            "clawbacks 19.9m; named L5 FOI ready gap_vl_cie_l5_beneficiaries"
        )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n")
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
            "2026-07-27T01:00:00Z",
            "rq_106",
            107,
            "no",
            "tick107 CIE path filled; L5 FOI ready. Next: spawn public L5 or rq_107 SWA late; human FOI incl CIE.",
        ]
    )

# --- loop_log ---
entry = """
### 2026-07-27T01:00:00Z — tick 107
- Unit: **rq_106** (Carbon leakage CIE L5 beneficiaries / evaluation)
- Found (strong totals; L5 names still opaque):
  - **FIO VEK ICL** (BO2026 tech vragen, keuro): **2024 250.234m** / **2025 261.588m** / **2026 BO 216.609m** — matches Speurgids 261.59m for 2025.
  - **PQ 251** (Diependaele 20 Feb 2026): **€258m** toegekend in 2025 voor emissiejaar 2024; **+€40m** uitzonderingsmechanisme EY 2022–23; budget **€216m** 2026.
  - **PQ 28** (2 Oct 2025): CIE = **grootste VLAIO-bedrijfssubsidie**; cite **€229m in 2024**; investeringsplicht-controles nog niet gestart (tot 2028 voor EY2021); **14 bedrijven** halen product-elektriciteitsbenchmark niet (50% herinvestering); terugvorderingen voorwaarden **€19.898.396** (2020–24 brieven).
  - Tech vragen: raming **~40 bedrijven** 2026; steun 75% standaard (uitzondering 95% niet actief voor EY2024 regulier); VKF vs algemene middelen timing-split; **geen publieke naam+EUR-lijst**.
  - Steelman: EU-toegelaten carbon-leakage correctie, geen pure “subsidie-weggooi”; absurdity matig; **opacity L5** is het DOGE-probleem.
- Wrote: sources +3; programmes CIE 2024–26; commitments cash path + exception cmt; leaderboard lb_vl_carbon_leakage_cie refresh; **FOI gap_vl_cie_l5_beneficiaries ready** (draft NL); rq_106=blocked_foi; raw PQs + tech PDF; ticks=107
- FOI opened: **gap_vl_cie_l5_beneficiaries** → ready (human send only)
- Next: spawn next public unit or low-prio **rq_107** SWA year-end; human FOI stack now includes CIE L5
"""
with (ROOT / "loop_log.md").open("a", encoding="utf-8") as f:
    f.write(entry)

print("tick107 write OK")

"""Tick 106: close rq_089 SWA recheck; seed next research."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]

# --- sources ---
src_path = DATA / "sources.csv"
with src_path.open("a", encoding="utf-8", newline="") as f:
    f.write(
        "src_apr_2026_bosa,Belgium Annual Progress Report 2026 (BOSA),"
        "https://bosa.belgium.be/sites/default/files/publications/documents/APR%202026%20report%20nl-fr_.pdf,"
        "BOSA / Belgian authorities,2026-07-27,budget,"
        '"APR 30 Apr 2026; ch5 begrotingscoordinatie: reform 2013 SWA; after signature RvS advice by summer; '
        'parliament assent acts by year-end; raw apr_2026_bosa.pdf"\n'
    )
    f.write(
        "src_tick106_swa_recheck_negative,Tick106 multi-parliament SWA final assent search negative Jul 2026,"
        "https://www.vlaanderen.be/vlaamse-regering/beslissingen-van-de-vlaamse-regering/samenwerkingsakkoord-economische-governance,"
        "DOGE loop research,2026-07-27,secondary,"
        '"No final plenaire law/decree or BS for Mar 2026 economic-governance SWA; APR timeline year-end; '
        'max still gov first-read + SERV + federal MR avant-projet"\n'
    )

# --- research_queue ---
rq_path = DATA / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)

for row in rows:
    if row["task_id"] == "rq_089":
        row["status"] = "done"
        row["updated_utc"] = "2026-07-27T00:40:00Z"
        row["notes"] = (
            "tick106: still no final assent any parliament/BS; APR2026 BOSA strong: "
            "RvS summer then parliaments by year-end; process max first-read+SERV+MR"
        )

rows.append(
    {
        "task_id": "rq_106",
        "title": "Carbon leakage CIE L5 beneficiaries or evaluation",
        "sprint": "continuous",
        "priority": "4",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "vlaio",
        "instructions": (
            "From Speurgids CIE 261.59m BO2025: find official beneficiary list amounts "
            "or evaluation (VR/VLAIO/Rekenhof). Commitments/leaderboard update or FOI if opaque."
        ),
        "blocked_gap_id": "",
        "created_utc": "2026-07-27T00:40:00Z",
        "updated_utc": "2026-07-27T00:40:00Z",
        "notes": "After Speurgids tick105 envelope; largest single Flanders econ instrument",
    }
)
rows.append(
    {
        "task_id": "rq_107",
        "title": "SWA multi-parliament final assent recheck year-end",
        "sprint": "continuous",
        "priority": "1",
        "status": "open",
        "hierarchy_target": "L0",
        "entity_id": "gg_belgium",
        "instructions": (
            "Sixth recheck final assent laws/decrees BS for Mar 2026 SWA after APR year-end "
            "target; only if not found earlier; low intensity."
        ),
        "blocked_gap_id": "",
        "created_utc": "2026-07-27T00:40:00Z",
        "updated_utc": "2026-07-27T00:40:00Z",
        "notes": "APR2026: parliament assent by year-end; deprioritise until Oct-Dec 2026",
    }
)

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

# --- commitment ---
cmt_path = DATA / "commitments.csv"
with cmt_path.open(newline="", encoding="utf-8") as f:
    cmt_rows = list(csv.DictReader(f))
ids = {r["commitment_id"] for r in cmt_rows}
if "cmt_swa_econ_governance_2026" not in ids:
    cash = (
        '{"overleg":"2026-03-27","vl_gov_principal":"2026-05-08","serv":"2026-06-01",'
        '"fed_mr_avant_projet":"2026-05-13","apr_parliament_target":"year_end_2026",'
        '"final_votes_bs":"none_as_of_2026-07-27"}'
    )
    with cmt_path.open("a", encoding="utf-8", newline="") as f:
        f.write(
            "cmt_swa_econ_governance_2026,"
            "Interfederal SWA economic governance assent path 2026,"
            "gg_belgium,"
            "Federal Communities Regions Community commissions,"
            "Overleg SWA replacing 13 Dec 2013; EU 2024/1265 transposition,"
            "2026-03-27,2026,2027,0,"
            f'"{cash}",,'
            "pending_assent,"
            "https://bosa.belgium.be/sites/default/files/publications/documents/APR%202026%20report%20nl-fr_.pdf,"
            "Interfederal budget coordination net-exp control accounts,"
            "Track assent; no euros until binding Entity paths public,"
            "src_apr_2026_bosa,strong,BE>SWA>economic_governance,"
            "tick106: not a fiscal outlay envelope; status pending multi-parliament assent\n"
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
            "2026-07-27T00:40:00Z",
            "rq_089",
            106,
            "no",
            "tick106 SWA still no final votes; APR year-end path. Next: rq_106 CIE L5; human FOI stack ready.",
        ]
    )

# --- loop_log ---
log_path = DATA.parent / "loop_log.md"
entry = """
### 2026-07-27T00:40:00Z — tick 106
- Unit: **rq_089** (SWA multi-parliament final assent recheck Q4)
- Found (strong process; negative on final votes):
  - **No final** Kamer/Senaat / Vlaams Parlement / Wallonie / FWB / Brussels plenaire assent law/decree and **no BS/Moniteur** publication found for the Mar 2026 multi-entity economic-governance SWA (fifth dedicated recheck; search as of 2026-07-27).
  - Process still maxes at: Overleg **27 Mar 2026** → VL gov **8 May** principal + SERV **1 Jun** filed → federal MR **13 May** avant-projet loi → WAL/FWB **1st reading** ODJs; **Brussels** still thin.
  - New primary **APR 2026** (BOSA, **30 Apr 2026**) ch.5: reform of 2013 interfederal budget SWA; after signature, SWA + assent acts → **Raad van State** advice **by summer**; then entity **parliaments by year-end**. Matches stalled public track mid/late July.
  - Kamer PDF 56K1569 blocked (WAF); not used as source this tick.
- Wrote: sources (+src_apr_2026_bosa, recheck note); commitments **cmt_swa_econ_governance_2026** (status pending_assent; €0 not a spend envelope); rq_089=done; spawned **rq_106** CIE L5 (prio4) + **rq_107** SWA year-end recheck (prio1); raw apr_2026_bosa.pdf; ticks=106
- FOI opened: none
- Next: **rq_106** carbon leakage CIE L5 beneficiaries (Speurgids €261.59m); human FOI stack unchanged
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(entry)

print("tick106 write complete; queue rows", len(rows))

# tick 351 — AWaP Wallonia heritage dual OE Flanders
import csv
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T14:15:00Z"
unit = "rq_342"

# --- sources ---
with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_wal_do16_awap_2026,"
        "Wallonie Budget 2026 DO16 prog 16.082 AWaP subvention 46.215m,"
        "https://finances.wallonie.be/files/Budget%202026/Budget%202026/depenses/do16.pdf,"
        "SPW Finances / Gouvernement wallon,2026-07-31,official_budget,"
        "Strong: prog 16.082 Monuments sites fouilles CE=CL 46.215m; line 082.001 "
        "Subvention AWaP 46.215m; dual OE Flanders VEK 127.8m; tick351\n"
    )

# --- budgets ---
buds = [
    (
        "bud_awap_subvention_2026",
        "awap",
        2026,
        46215000,
        "budgeted",
        "src_wal_do16_awap_2026",
        "strong",
        "DO16 082.001 Subvention a l Agence wallonne du Patrimoine eng=liq 46.215m kEUR",
    ),
    (
        "bud_wal_prog16082_monuments_2026",
        "awap",
        2026,
        46215000,
        "budgeted",
        "src_wal_do16_awap_2026",
        "strong",
        "Programme 16.082 Monuments sites et fouilles total CE=CL 46.215m (AWaP only lines)",
    ),
    (
        "bud_heritage_dual_oe_awap_class_2026",
        "onroerend_erfgoed",
        2026,
        174004000,
        "budgeted",
        "src_wal_do16_awap_2026",
        "medium",
        "Illustrative dual 2026: OE VEK 127.789m + AWaP 46.215m = 174.004m; not additive TE; different perimeters",
    ),
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        note = b[7].replace('"', "'")
        f.write(f'{b[0]},{b[1]},{b[2]},{b[3]},,,{b[4]},{b[5]},{b[6]},"{note}"\n')

# --- commitments ---
cmt_json = (
    '{"awap_subvention_2026_m":46.215,"prog_16082_total_m":46.215,'
    '"oe_vek_2026_m":127.789,"oe_vak_2026_m":121.823,"dual_class_2026_m":174.0,'
    '"note":"Regional toelage only; AWaP own receipts residual; dual OE Flanders heritage"}'
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_awap_subvention_2026,"
        "AWaP Wallonia heritage agency regional toelage dual OE Flanders,"
        "awap,"
        "Classified heritage owners municipalities archaeologists Wallonia,"
        "Code wallon patrimoine + Budget general depenses DO16 prog 16.082,"
        "2025-10-20,2026,2026,46215000,"
        f'"{cmt_json}",'
        ",active,https://finances.wallonie.be/files/Budget%202026/Budget%202026/depenses/do16.pdf,"
        "Protect restore Walloon monuments sites excavations,"
        "Publish L5 top subventions; dual unit-cost OE Flanders; AWaP internal split,"
        "src_wal_do16_awap_2026,strong,Wallonie>Patrimoine>AWaP,"
        "tick351: 46.215m dual OE 127.8m VEK\n"
    )

# --- leaderboard ---
lbs = [
    [
        "lb_awap_46m",
        "AWaP Wallonia heritage toelage 46.2m 2026 dual OE",
        "regional",
        "subsidy",
        "Wallonie>Patrimoine>AWaP",
        "46215000",
        "46215000",
        "Strong DO16: prog 16.082 / line 082.001 46.215m eng=liq; dual Flanders OE VEK 127.8m",
        "strong",
        "src_wal_do16_awap_2026",
        "Heritage owners municipalities sector Wallonia",
        "Monuments sites excavations regional heritage policy",
        "Smaller absolute than Flanders OE; dual community competence; L5 awards residual",
        "3",
        "5.5",
        "4",
        "4.55",
        "Open L5 subventions matrix; dual unit-cost OE",
        "seed",
        "",
        "tick351 dual heritage",
    ],
    [
        "lb_heritage_dual_oe_awap_174m",
        "Dual heritage OE+AWaP class ~174m 2026",
        "regional",
        "programme",
        "BE>dual>Heritage_immovable",
        "174004000",
        "174004000",
        "Medium dual class: OE VEK 127.789 + AWaP 46.215 = 174.0m; not additive TE",
        "medium",
        "src_wal_do16_awap_2026",
        "Two regional immovable heritage systems",
        "Classic dual regional heritage after state reform",
        "Dual overhead pattern; Flanders larger premium stack; L5 both sides FOI",
        "4",
        "7.0",
        "4",
        "5.5",
        "Map full dual TCO + federal FSI residual",
        "seed",
        "",
        "tick351 dual structure",
    ],
]
with open(base / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(",".join(lb) + "\n")

# --- entities update notes: rewrite awap row is hard; append note via log only ---

# --- research_queue ---
rq_path = base / "research_queue.csv"
with open(rq_path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for r in rows:
    if r["task_id"] == "rq_342":
        r["status"] = "done"
        r["blocked_gap_id"] = "gap_oe_awap_dual_l5"
        r["updated_utc"] = now
        r["notes"] = (
            "tick351: AWaP DO16 46.215m dual OE VEK 127.8m; FOI L5 residual; spawn rq_343"
        )

rows.append(
    {
        "task_id": "rq_343",
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
        "notes": "Spawned tick351 after AWaP dual OE; rq_116 SWA deferred",
    }
)
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

# --- foi_queue update gap_oe_awap ---
foi_path = base / "foi_queue.csv"
with open(foi_path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    foi_fields = reader.fieldnames
    foi_rows = list(reader)

updated = False
for r in foi_rows:
    if r.get("gap_id") == "gap_oe_awap_dual_l5":
        r["what_is_missing"] = (
            "Named top30 OE premie awards 2023-2026; waitlist stock EUR; Herita SWO cash path; "
            "AWaP internal L5 top subventions 2023-2026 (agency total 46.215m 2026 now public DO16)"
        )
        r["why_it_matters"] = (
            "OE package + AWaP toelage strong; residual named L5 awards both sides"
        )
        r["updated_utc"] = now
        r["notes"] = (
            (r.get("notes") or "")
            + "|tick351: AWaP total 46.215m filled; residual L5 awards human send"
        )
        r["linked_leaderboard_id"] = (
            "lb_oe_vek_128m|lb_oe_premies_83m|lb_awap_46m|lb_heritage_dual_oe_awap_174m"
        )
        r["linked_commitment_id"] = "cmt_oe_package_2025_26|cmt_awap_subvention_2026"
        updated = True
        break

if not updated:
    print("WARN gap not found")

with open(foi_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=foi_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(foi_rows)

# --- loop_state ---
with open(base / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    f.write(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    )
    f.write(
        f"main,continuous,hole_fill,{now},{unit},351,no,"
        "Scheduler 60s. Next prio5 rq_343; rq_116 SWA deferred. FOI ready. "
        "tick351 AWaP 46.2m dual OE.\n"
    )

print("CSV updates OK", "foi_updated", updated)

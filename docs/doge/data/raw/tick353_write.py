# tick 353 — dual nature: Flanders Omgeving/ANB + Wallonia Nature-Forêt
import csv
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T15:15:00Z"
unit = "rq_344"

# --- entities ---
with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "anb_vl,Agentschap voor Natuur en Bos ANB,"
        "Agence de la Nature et des Forets Flandre,"
        "Flanders nature and forest agency dual Wallonia DNF/ARNE,"
        "agency,vlaanderen_gov,nl,https://www.natuurenbos.be,openbaarheid@vlaanderen.be,,"
        "BO2026 apparaatrek QA-QD0 49.5m; ISE Nature total 150m incl MINA 128m; dual WAL 15.060; tick353\n"
    )
    f.write(
        "inbo_vl,Instituut voor Natuur- en Bosonderzoek INBO,"
        "Institut de Recherche Nature et Forets Flandre,"
        "Flanders nature research institute under Omgeving,"
        "agency,vlaanderen_gov,nl,https://www.inbo.be,openbaarheid@vlaanderen.be,,"
        "BO2026 apparaatrek QA-QC0 VAK=VEK 19.499m; tick353\n"
    )

# --- sources ---
with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_vl_bbt_omgeving_bo2026,"
        "VR BBT Omgeving Begroting 2026 MED.0437 Brouns,"
        "https://www.vlaanderen.be/vlaamse-regering/beslissingen-van-de-vlaamse-regering/beleids-en-begrotingstoelichting-bbt-naar-aanleiding-van-de-begrotingsopmaak-2026-omgeving,"
        "Vlaamse Regering / minister Omgeving,2026-07-31,official_budget,"
        "Strong: Omgeving en Natuur excl apparaatrek VAK 690.943m VEK 696.049m; "
        "ISE Natuur total 150m (MVG 22m + MINA DAB 128m); ANB apparaatrek 49.5m; "
        "INBO 19.499m; dual WAL Nature-Foret; tick353\n"
    )

# --- budgets ---
buds = [
    (
        "bud_vl_omgeving_natuur_vak_2026",
        "anb_vl",
        2026,
        690943000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "TOTAAL Omgeving en Natuur excl apparaatrek QA BO2026 VAK 690.943m (duizend euro table)",
    ),
    (
        "bud_vl_omgeving_natuur_vek_2026",
        "anb_vl",
        2026,
        696049000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "TOTAAL Omgeving en Natuur excl apparaatrek QA BO2026 VEK 696.049m",
    ),
    (
        "bud_vl_omgeving_natuur_vak_2025_ba",
        "anb_vl",
        2025,
        693952000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "BA2025 Omgeving en Natuur excl apparaatrek VAK 693.952m",
    ),
    (
        "bud_vl_omgeving_natuur_vek_2025_ba",
        "anb_vl",
        2025,
        704499000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "BA2025 Omgeving en Natuur excl apparaatrek VEK 704.499m",
    ),
    (
        "bud_vl_ise_natuur_total_2026",
        "anb_vl",
        2026,
        150000000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "ISE Natuur en biodiversiteit total 150.0m 2026 (22m uitgavenbegroting + 128m DAB MINAfonds)",
    ),
    (
        "bud_vl_ise_natuur_mvg_vek_2026",
        "anb_vl",
        2026,
        23975000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "ISE Natuur MVG excl DAB VEK 23.975m VAK 22.074m",
    ),
    (
        "bud_vl_ise_natuur_mina_dab_2026",
        "anb_vl",
        2026,
        128000000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "ISE Natuur portion financed via DAB MINAfonds 128.0m 2026",
    ),
    (
        "bud_anb_apparaat_2026",
        "anb_vl",
        2026,
        49500000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "PROGRAMMA QA-QD0 ANB apparaatrek BO2026 VAK=VEK 49.500m (lonen 45.452 + werking 3.898 + EU 0.150)",
    ),
    (
        "bud_inbo_apparaat_2026",
        "inbo_vl",
        2026,
        19499000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "PROGRAMMA QA-QC0 INBO apparaatrek BO2026 VAK=VEK 19.499m",
    ),
    (
        "bud_nature_dual_vl_wal_class_2026",
        "anb_vl",
        2026,
        178879000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "medium",
        "Illustrative dual nature policy: VL ISE Natuur 150m + WAL prog 15.060 Nature-Foret CL 28.879m = 178.879m; not full Omgeving 696m; not additive TE",
    ),
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        note = b[7].replace('"', "'")
        f.write(f'{b[0]},{b[1]},{b[2]},{b[3]},,,{b[4]},{b[5]},{b[6]},"{note}"\n')

# --- commitments ---
cmt_json = (
    '{"vl_omgeving_vek_m":696.049,"vl_ise_natuur_total_m":150.0,"vl_ise_mvg_vek_m":23.975,'
    '"vl_mina_nature_m":128.0,"anb_apparaat_m":49.5,"inbo_apparaat_m":19.499,'
    '"wal_nature_foret_cl_m":28.879,"wal_nature_foret_ce_m":38.44,"dual_class_m":178.9,'
    '"note":"Full Omgeving field 696m includes water air waste soil; pure nature dual uses ISE Nature 150m vs WAL 15.060"}'
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_nature_dual_vl_wal_2026,"
        "Dual nature policy Flanders ISE Natuur/ANB + Wallonia Nature-Foret 2026,"
        "anb_vl,"
        "Nature NGOs landowners hunters fishers both regions,"
        "Natuurdecreet + Code forestier/environnement WAL + MINAfonds,"
        "2025-10-01,2026,2026,178879000,"
        f'"{cmt_json}",'
        ",active,https://www.vlaanderen.be/vlaamse-regering/beslissingen-van-de-vlaamse-regering/beleids-en-begrotingstoelichting-bbt-naar-aanleiding-van-de-begrotingsopmaak-2026-omgeving,"
        "Dual regional nature forest biodiversity competence,"
        "Map MINA L5 nature grants; dual unit-cost ANB vs WAL DNF; FOI top partners,"
        "src_vl_bbt_omgeving_bo2026,strong,BE>dual>Nature_forest,"
        "tick353: VL ISE Nature 150m dual WAL 28.9m; Omgeving field 696m separate\n"
    )

# --- leaderboard ---
lbs = [
    [
        "lb_vl_omgeving_vek_696m",
        "Flanders Omgeving en Natuur VEK 696m 2026",
        "regional",
        "programme",
        "Vlaanderen>Omgeving>QC",
        "696049000",
        "696049000",
        "Strong BBT BO2026: VEK 696.049m VAK 690.943m excl apparaatrek; multi-ISE not pure nature",
        "strong",
        "src_vl_bbt_omgeving_bo2026",
        "All Omgeving beneficiaries multi-ISE",
        "Environment space nature multi-ISE package",
        "Large envelope; dual WAL ARNE partial; nature ISE only 150m inside",
        "3",
        "6.5",
        "4",
        "4.85",
        "Split ISE transparency; FOI MINA L5",
        "seed",
        "",
        "tick353 omgeving field",
    ],
    [
        "lb_vl_ise_natuur_150m",
        "Flanders ISE Natuur en biodiversiteit 150m 2026 dual WAL",
        "regional",
        "programme",
        "Vlaanderen>Omgeving>ISE_Natuur",
        "150000000",
        "150000000",
        "Strong BBT: 150m total (MVG ~22m + MINA DAB 128m); ANB apparaatrek 49.5m separate; dual WAL Nature-Foret 28.9m",
        "strong",
        "src_vl_bbt_omgeving_bo2026",
        "Nature partners forests hunters fishers",
        "Regional nature biodiversity dual Wallonia",
        "MINA DAB opacity classic; dual structure; L5 residual",
        "4",
        "7.0",
        "5",
        "5.7",
        "FOI MINA nature grants L5; dual unit-cost",
        "seed",
        "",
        "tick353 dual nature",
    ],
    [
        "lb_nature_dual_vl_wal_179m",
        "Dual nature policy VL+WAL class ~179m 2026",
        "regional",
        "programme",
        "BE>dual>Nature",
        "178879000",
        "178879000",
        "Medium dual class: VL ISE Nature 150 + WAL 15.060 CL 28.879 = 178.9m; excludes full Omgeving 696m and agri dual",
        "medium",
        "src_vl_bbt_omgeving_bo2026",
        "Two regional nature forest systems",
        "Classic dual nature competence + dual agencies ANB/DNF",
        "Asymmetric scale VL vs WAL; MINA vs DO15 transparency gap",
        "4",
        "7.0",
        "5",
        "5.7",
        "FOI L5 both sides; dual overhead map",
        "seed",
        "",
        "tick353 dual structure",
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
    if r["task_id"] == "rq_344":
        r["status"] = "done"
        r["blocked_gap_id"] = "gap_nature_dual_anb_wal_l5"
        r["updated_utc"] = now
        r["notes"] = (
            "tick353: VL Omgeving VEK 696m ISE Nature 150m ANB app 49.5m dual "
            "WAL Nature-Foret 28.9m; FOI MINA L5; spawn rq_345"
        )

rows.append(
    {
        "task_id": "rq_345",
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
        "notes": "Spawned tick353 after nature dual VL/WAL; rq_116 SWA deferred",
    }
)
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

# --- foi_queue ---
with open(base / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_nature_dual_anb_wal_l5,BE>dual>Nature>ANB_WAL_L5,anb_vl,"
        "MINAfonds nature ISE cash-by-year 2023-2026 top30 grants partners land purchases; "
        "ANB external toelagen L5; WAL DO15 15.060 top20 subventions nature-foret-chasse-peche 2023-2025; "
        "dual unit-cost ANB apparaatrek vs DNF,"
        "ISE Nature 150m + WAL 28.9m strong; residual L5 awards MINA/partners dual,"
        "5,Agentschap Natuur en Bos / SPW ARNE / Team Openbaarheid,"
        "openbaarheid@vlaanderen.be; agriculture.wallonie.be,"
        "Havenlaan Brussel; SPW Namur,"
        "docs/doge/foi/drafts/gap_nature_dual_anb_wal_l5.md,"
        "ready,2026-07-31,,,,,cmt_nature_dual_vl_wal_2026,"
        "lb_vl_ise_natuur_150m|lb_nature_dual_vl_wal_179m|lb_vl_omgeving_vek_696m,"
        "2026-07-31T15:15:00Z,2026-07-31T15:15:00Z,"
        "tick353 public BBT+DO15; residual MINA/L5 human send\n"
    )

# --- loop_state ---
with open(base / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    f.write(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    )
    f.write(
        f"main,continuous,hole_fill,{now},{unit},353,no,"
        "Scheduler 60s. Next prio5 rq_345; rq_116 SWA deferred. FOI ready. "
        "tick353 nature dual VL/WAL.\n"
    )

print("CSV updates OK")

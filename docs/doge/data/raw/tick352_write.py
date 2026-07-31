# tick 352 — dual regional agriculture Flanders Landbouw + Wallonia Aides/OPW
import csv
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T14:45:00Z"
unit = "rq_343"

# --- entities ---
with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "landbouw_vl,Agentschap Landbouw en Zeevisserij / beleidsveld Landbouw,"
        "Agence Agriculture et Peche Flandre,"
        "Flanders Agriculture and Fisheries policy field dual Wallonia OPW,"
        "agency,vlaanderen_gov,nl,https://lv.vlaanderen.be,openbaarheid@vlaanderen.be,,"
        "BO2026 VEK 140.849m VAK 157.880m excl apparaatrek; dual WAL aides 93m; tick352\n"
    )
    f.write(
        "opw_wallonie,Organisme Payeur de Wallonie OPW,"
        "Organisme Payeur de Wallonie,"
        "Walloon Paying Agency CAP dual Flanders,agency,wallonie_gov,fr,"
        "https://agriculture.wallonie.be,,,DO16 15.058 OPW missions 45.0m fonct 16.7m capital 20.0m 2026; dual VL; tick352\n"
    )

# --- sources ---
with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_vl_bbt_landbouw_bo2026,"
        "Vlaams Parlement BBT Landbouw Begroting 2026 13-AC Nr1,"
        "https://docs.vlaamsparlement.be/pfile?id=2227524,"
        "Vlaams Parlement / Landbouw en Zeevisserij,2026-07-31,official_budget,"
        "Strong: BO2026 VAK 157.880m VEK 140.849m excl apparaatrek/prog B; TJ 152.1/135.2; "
        "TK promotie 5.659; dual WAL; tick352\n"
    )
    f.write(
        "src_wal_do15_agri_2026,"
        "Wallonie Budget 2026 DO15 ARNE prog 15.058 Aides Agriculture OPW,"
        "https://finances.wallonie.be/files/Budget%202026/Budget%202026/depenses/do15.pdf,"
        "SPW Finances / Gouvernement wallon,2026-07-31,official_budget,"
        "Strong: DO15 total CE 619.589m CL 570.184m; prog 15.058 Aides 93.325/93.225m; "
        "OPW missions 45.049 fonct 16.747 capital 20.017; dual VL Landbouw; tick352\n"
    )

# --- budgets ---
buds = [
    (
        "bud_vl_landbouw_vak_2026",
        "landbouw_vl",
        2026,
        157880000,
        "budgeted",
        "src_vl_bbt_landbouw_bo2026",
        "strong",
        "TOTAAL Landbouw excl apparaatrek/prog B BO2026 VAK 157.880m",
    ),
    (
        "bud_vl_landbouw_vek_2026",
        "landbouw_vl",
        2026,
        140849000,
        "budgeted",
        "src_vl_bbt_landbouw_bo2026",
        "strong",
        "TOTAAL Landbouw BO2026 VEK 140.849m",
    ),
    (
        "bud_vl_landbouw_vak_2025_ba",
        "landbouw_vl",
        2025,
        170993000,
        "budgeted",
        "src_vl_bbt_landbouw_bo2026",
        "strong",
        "BA2025 VAK 170.993m",
    ),
    (
        "bud_vl_landbouw_vek_2025_ba",
        "landbouw_vl",
        2025,
        153945000,
        "budgeted",
        "src_vl_bbt_landbouw_bo2026",
        "strong",
        "BA2025 VEK 153.945m",
    ),
    (
        "bud_vl_landbouw_tj_vek_2026",
        "landbouw_vl",
        2026,
        135190000,
        "budgeted",
        "src_vl_bbt_landbouw_bo2026",
        "strong",
        "Programma TJ Landbouw en Zeevisserij VEK 135.190m VAK 152.055m",
    ),
    (
        "bud_vl_landbouw_tk_promotie_2026",
        "landbouw_vl",
        2026,
        5659000,
        "budgeted",
        "src_vl_bbt_landbouw_bo2026",
        "strong",
        "Programma TK Promotie landbouw tuinbouw zeevisserij VAK=VEK 5.659m",
    ),
    (
        "bud_wal_do15_total_liq_2026",
        "wallonie_gov",
        2026,
        570184000,
        "budgeted",
        "src_wal_do15_agri_2026",
        "strong",
        "DO15 ARNE total CL 570.184m CE 619.589m (agri+nature+env combined not pure agri)",
    ),
    (
        "bud_wal_aides_agriculture_2026",
        "opw_wallonie",
        2026,
        93225000,
        "budgeted",
        "src_wal_do15_agri_2026",
        "strong",
        "Prog 15.058 Aides a l Agriculture CE 93.325m CL 93.225m",
    ),
    (
        "bud_opw_missions_2026",
        "opw_wallonie",
        2026,
        45049000,
        "budgeted",
        "src_wal_do15_agri_2026",
        "strong",
        "Dotation courante OPW Missions 45.049m CE=CL",
    ),
    (
        "bud_opw_fonctionnement_2026",
        "opw_wallonie",
        2026,
        16747000,
        "budgeted",
        "src_wal_do15_agri_2026",
        "strong",
        "Dotation courante OPW Fonctionnement 16.747m",
    ),
    (
        "bud_opw_capital_2026",
        "opw_wallonie",
        2026,
        20017000,
        "budgeted",
        "src_wal_do15_agri_2026",
        "strong",
        "Dotation en capital OPW 20.017m",
    ),
    (
        "bud_opw_package_2026",
        "opw_wallonie",
        2026,
        81813000,
        "budgeted",
        "src_wal_do15_agri_2026",
        "strong",
        "OPW sum missions+fonct+capital 81.813m 2026 (inside 15.058)",
    ),
    (
        "bud_wal_calamites_agricoles_2026",
        "opw_wallonie",
        2026,
        9300000,
        "budgeted",
        "src_wal_do15_agri_2026",
        "strong",
        "Dotation Fonds wallon calamites agricoles 9.300m",
    ),
    (
        "bud_wal_nature_foret_2026",
        "wallonie_gov",
        2026,
        28879000,
        "budgeted",
        "src_wal_do15_agri_2026",
        "medium",
        "Prog 15.060 Nature Foret Chasse-peche CL 28.879m CE 38.440m; dual ANB residual separate",
    ),
    (
        "bud_agri_dual_vl_wal_class_2026",
        "landbouw_vl",
        2026,
        234074000,
        "budgeted",
        "src_vl_bbt_landbouw_bo2026",
        "medium",
        "Illustrative dual regional agri policy 2026: VL VEK 140.849 + WAL aides 93.225 = 234.074m; excludes EU CAP flow bulk; not additive TE",
    ),
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        note = b[7].replace('"', "'")
        f.write(f'{b[0]},{b[1]},{b[2]},{b[3]},,,{b[4]},{b[5]},{b[6]},"{note}"\n')

# --- commitments ---
cmt_json = (
    '{"vl_vek_2026_m":140.849,"vl_vak_2026_m":157.88,"vl_tj_vek_m":135.19,'
    '"vl_tk_promotie_m":5.659,"wal_aides_cl_m":93.225,"opw_package_m":81.813,'
    '"opw_missions_m":45.049,"opw_fonct_m":16.747,"opw_capital_m":20.017,'
    '"calamites_m":9.3,"do15_total_cl_m":570.184,"dual_class_m":234.1,'
    '"note":"Regional agri policy envelopes; EU CAP direct payments larger separate channel via paying agencies"}'
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_agri_dual_vl_wal_2026,"
        "Dual regional agriculture Flanders Landbouw + Wallonia Aides/OPW 2026,"
        "landbouw_vl,"
        "Farmers horticulture fisheries both regions,"
        "VL Landbouwdecreet + WAL Code agriculture + CAP SP,"
        "2025-10-01,2026,2026,234074000,"
        f'"{cmt_json}",'
        ",active,https://docs.vlaamsparlement.be/pfile?id=2227524,"
        "Regional agriculture policy dual paying agencies CAP,"
        "Map EU CAP cash dual VL/WAL; FOI L5 top aids; dual unit-cost OPW vs VL betaalorgaan,"
        "src_vl_bbt_landbouw_bo2026,strong,BE>dual>Agriculture_regional,"
        "tick352: VL 140.8m VEK dual WAL aides 93.2m OPW 81.8m\n"
    )

# --- leaderboard ---
lbs = [
    [
        "lb_vl_landbouw_vek_141m",
        "Flanders Landbouw VEK 141m 2026 dual WAL OPW",
        "regional",
        "programme",
        "Vlaanderen>Landbouw>TJ",
        "140849000",
        "140849000",
        "Strong BBT BO2026: VEK 140.849m VAK 157.880m excl apparaatrek; dual WAL aides 93m",
        "strong",
        "src_vl_bbt_landbouw_bo2026",
        "Flemish farmers horticulture fisheries",
        "Regional agriculture fisheries policy dual CAP",
        "Core sector policy; EU CAP separate larger; dual Wallonia OPW",
        "3",
        "7.0",
        "4",
        "5.15",
        "Publish CAP cash dual; L5 top schemes",
        "seed",
        "",
        "tick352 dual agri",
    ],
    [
        "lb_wal_aides_agri_93m",
        "Wallonia Aides Agriculture 93m 2026 dual VL",
        "regional",
        "programme",
        "Wallonie>ARNE>Aides_Agriculture",
        "93225000",
        "93225000",
        "Strong DO15 prog 15.058 CL 93.225m; OPW package 81.8m inside; dual Flanders 141m",
        "strong",
        "src_wal_do15_agri_2026",
        "Walloon farmers OPW beneficiaries",
        "Regional agri aids + paying agency dual Flanders",
        "OPW is CAP channel admin; dual structure classic; L5 residual",
        "3",
        "6.0",
        "4",
        "4.7",
        "FOI L5 top OPW schemes; dual unit-cost",
        "seed",
        "",
        "tick352 dual agri",
    ],
    [
        "lb_agri_dual_vl_wal_234m",
        "Dual regional agri policy VL+WAL class ~234m 2026",
        "regional",
        "programme",
        "BE>dual>Agriculture",
        "234074000",
        "234074000",
        "Medium dual class: VL VEK 140.8 + WAL aides 93.2 = 234m; excludes bulk EU CAP; not additive TE",
        "medium",
        "src_vl_bbt_landbouw_bo2026",
        "Two regional agri policy systems + dual paying agencies",
        "Classic dual community/regional agriculture competence",
        "Dual overhead; CAP EU co-finance separate material; FOI L5 both",
        "4",
        "7.5",
        "5",
        "5.95",
        "Map full dual CAP cash; FOI top schemes",
        "seed",
        "",
        "tick352 dual structure",
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
    if r["task_id"] == "rq_343":
        r["status"] = "done"
        r["blocked_gap_id"] = "gap_agri_dual_l5_cap"
        r["updated_utc"] = now
        r["notes"] = (
            "tick352: VL Landbouw VEK 140.8m dual WAL aides 93.2m OPW 81.8m; "
            "FOI CAP L5; spawn rq_344"
        )

rows.append(
    {
        "task_id": "rq_344",
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
        "notes": "Spawned tick352 after agri dual VL/WAL; rq_116 SWA deferred",
    }
)
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

# --- foi_queue append ---
with open(base / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_agri_dual_l5_cap,BE>dual>Agriculture>VL_WAL_CAP_L5,landbouw_vl,"
        "EU CAP cash-by-year dual Flanders betaalorgaan vs OPW 2022-2026 (pillar1/2); "
        "top20 scheme envelopes; regional co-finance matrix; reconcile BBT/DO15 vs CAP outturn,"
        "Regional envelopes strong; bulk EU CAP flow and L5 schemes residual dual,"
        "6,Agentschap Landbouw en Zeevisserij / OPW / Team Openbaarheid,"
        "openbaarheid@vlaanderen.be; agriculture.wallonie.be,"
        "Ellipsgebouw Brussel; OPW Namur,"
        "docs/doge/foi/drafts/gap_agri_dual_l5_cap.md,"
        "ready,2026-07-31,,,,,cmt_agri_dual_vl_wal_2026,"
        "lb_vl_landbouw_vek_141m|lb_wal_aides_agri_93m|lb_agri_dual_vl_wal_234m,"
        "2026-07-31T14:45:00Z,2026-07-31T14:45:00Z,"
        "tick352 public BBT+DO15; residual CAP L5 human send\n"
    )

# --- loop_state ---
with open(base / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    f.write(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    )
    f.write(
        f"main,continuous,hole_fill,{now},{unit},352,no,"
        "Scheduler 60s. Next prio5 rq_344; rq_116 SWA deferred. FOI ready. "
        "tick352 agri dual VL/WAL.\n"
    )

print("CSV updates OK")

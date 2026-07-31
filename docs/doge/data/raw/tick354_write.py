# tick 354 — dual waste/remediation: OVAM Flanders + SPAQuE/déchets Wallonia
import csv
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T15:45:00Z"
unit = "rq_345"

# --- entities ---
with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "ovam,Openbare Vlaamse Afvalstoffenmaatschappij OVAM,"
        "Societe publique flamande des dechets OVAM,"
        "Flanders waste materials soil agency dual SPAQuE Wallonia,"
        "agency,vlaanderen_gov,nl,https://www.ovam.be,openbaarheid@vlaanderen.be,,"
        "BO2026 ISE Afval 105.9m; dept toelage 28.349m; MINA toelage 35.9/37.4m; dual SPAQuE; tick354\n"
    )
    f.write(
        "spaque,SPAQuE SA,SPAQuE Societe publique d aide a la qualite de l environnement,"
        "Walloon public soil remediation and polluted sites operator dual OVAM,"
        "parastatal,wallonie_gov,fr,https://www.spaque.be,,,"
        "DO15 062.018 Dotation SPAQuE 24.138m CE=CL 2026; dual OVAM soil; tick354\n"
    )
    f.write(
        "vmm,Vlaamse Milieumaatschappij VMM,"
        "Agence flamande de l environnement VMM,"
        "Flanders environment water quality agency under Omgeving,"
        "agency,vlaanderen_gov,nl,https://www.vmm.be,openbaarheid@vlaanderen.be,,"
        "BBT Omgeving ISE Water: lonen 74.15m werking ~33m invest ~24.8m class ~132m; tick354\n"
    )

# --- sources (reuse BBT omgeving + DO15 already in sources if present; add OVAM-focused note source) ---
# Check if src_vl_bbt_omgeving_bo2026 exists from tick353 - yes. Reuse it.
# Add SPAQuE-focused DO15 ref if not redundant with src_wal_do15_agri_2026
with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_wal_do15_waste_spaque_2026,"
        "Wallonie Budget 2026 DO15 ARNE prog 15.062 SPAQuE + 15.064 dechets,"
        "https://finances.wallonie.be/files/Budget%202026/Budget%202026/depenses/do15.pdf,"
        "SPW Finances / Gouvernement wallon,2026-07-31,official_budget,"
        "Strong: 15.062 CL 64.071m CE 73.705m SPAQuE 24.138m ISSEP 23.783m; "
        "15.064 dechets CL 9.859m CE 13.279m; dual OVAM; tick354\n"
    )

# --- budgets ---
buds = [
    (
        "bud_vl_ise_afval_total_2026",
        "ovam",
        2026,
        105900000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "ISE Afval en materialen total 105.9m 2026 (MVG 102.4m + MINA DAB 3.5m); UPV/zwerfvuil fonds jump +74m",
    ),
    (
        "bud_vl_ise_afval_mvg_2026",
        "ovam",
        2026,
        102394000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "ISE Afval MVG excl DAB VAK=VEK 102.394m",
    ),
    (
        "bud_ovam_toelage_dept_2026",
        "ovam",
        2026,
        28349000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "QB0-1QCG2JV-IS OVAM werkings+investeringsdotatie Departement 28.349m VAK=VEK",
    ),
    (
        "bud_ovam_toelage_mina_2026",
        "ovam",
        2026,
        37423000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "QBX-3QCG2EV-IS OVAM MINAfonds toelage VEK 37.423m VAK 35.926m (bodem+afval+ambtshalve sanering)",
    ),
    (
        "bud_vl_upv_zwerfvuil_fonds_to_2026",
        "ovam",
        2026,
        74045000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "New Fonds UPV/zwerfvuil TO receipts 74.045m BO2026 (ISA UPV; ~71.5m zwerfvuil + UPV heffing path)",
    ),
    (
        "bud_vl_ise_bodem_total_2026",
        "ovam",
        2026,
        41100000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "strong",
        "ISE Bodem en ondergrond total 41.1m (MVG ~2.75m + MINA DAB 38.3m)",
    ),
    (
        "bud_spaque_dotation_2026",
        "spaque",
        2026,
        24138000,
        "budgeted",
        "src_wal_do15_waste_spaque_2026",
        "strong",
        "DO15 062.018 Dotation a la SPAQuE 24.138m CE=CL 2026",
    ),
    (
        "bud_wal_dechets_15_064_2026",
        "wallonie_gov",
        2026,
        9859000,
        "budgeted",
        "src_wal_do15_waste_spaque_2026",
        "strong",
        "Prog 15.064 Politique des dechets-ressources CL 9.859m CE 13.279m",
    ),
    (
        "bud_wal_air_eau_sol_15_062_2026",
        "spaque",
        2026,
        64071000,
        "budgeted",
        "src_wal_do15_waste_spaque_2026",
        "strong",
        "Prog 15.062 Prevention Protection Air Eau Sol CL 64.071m CE 73.705m (includes SPAQuE ISSEP AWAC)",
    ),
    (
        "bud_issep_missions_2026",
        "wallonie_gov",
        2026,
        23783000,
        "budgeted",
        "src_wal_do15_waste_spaque_2026",
        "strong",
        "DO15 062.074 Missions ISSeP 23.783m + capital materiel 1.558m separate",
    ),
    (
        "bud_vmm_class_2026",
        "vmm",
        2026,
        131709000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "medium",
        "VMM ISE Water class: lonen 74.150 + werking VAK 32.758 + invest VAK 24.801 = 131.709m (not dual-add TE)",
    ),
    (
        "bud_waste_dual_vl_wal_class_2026",
        "ovam",
        2026,
        115759000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "medium",
        "Illustrative dual waste: VL ISE Afval 105.9 + WAL 15.064 CL 9.859 = 115.759m; excludes SPAQuE remediation dual; not additive TE",
    ),
    (
        "bud_remediation_dual_ovam_spaque_2026",
        "ovam",
        2026,
        65261000,
        "budgeted",
        "src_vl_bbt_omgeving_bo2026",
        "medium",
        "Illustrative remediation dual: VL ISE Bodem 41.1 + SPAQuE 24.138 = 65.238m approx class (uses 65238000)",
    ),
]
# fix remediation total to exact 41100000+24138000=65238000
buds[-1] = (
    "bud_remediation_dual_ovam_spaque_2026",
    "ovam",
    2026,
    65238000,
    "budgeted",
    "src_vl_bbt_omgeving_bo2026",
    "medium",
    "Illustrative remediation dual: VL ISE Bodem 41.1 + SPAQuE 24.138 = 65.238m; not additive TE",
)

with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        note = b[7].replace('"', "'")
        f.write(f'{b[0]},{b[1]},{b[2]},{b[3]},,,{b[4]},{b[5]},{b[6]},"{note}"\n')

cmt_json = (
    '{"vl_ise_afval_m":105.9,"vl_ovam_dept_m":28.349,"vl_ovam_mina_m":37.423,'
    '"vl_upv_fonds_to_m":74.045,"vl_ise_bodem_m":41.1,"spaque_m":24.138,'
    '"wal_dechets_cl_m":9.859,"wal_15_062_cl_m":64.071,"issep_m":23.783,'
    '"vmm_class_m":131.7,"dual_waste_m":115.8,"dual_remediation_m":65.2,'
    '"note":"UPV zwerfvuil is producer-pay pass-through not pure taxpayer; dual SPAQuE vs OVAM soil remediation"}'
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_waste_dual_ovam_spaque_2026,"
        "Dual waste and soil remediation OVAM Flanders + SPAQuE/dechets Wallonia 2026,"
        "ovam,"
        "Municipalities waste operators polluted-site neighbours,"
        "Materialendecreet Bodemdecreet + SPAQuE decree + ISA UPV zwerfvuil,"
        "2025-10-01,2026,2026,115759000,"
        f'"{cmt_json}",'
        ",active,https://www.ovam.be,"
        "Dual regional waste materials soil competence,"
        "Map UPV cash vs taxpayer; FOI SPAQuE/OVAM L5 remediation sites; dual unit-cost,"
        "src_vl_bbt_omgeving_bo2026,strong,BE>dual>Waste_soil,"
        "tick354: VL Afval 105.9m dual WAL dechets 9.9m; SPAQuE 24.1m dual Bodem 41.1m\n"
    )

lbs = [
    [
        "lb_vl_ise_afval_106m",
        "Flanders ISE Afval en materialen 106m 2026 dual WAL dechets",
        "regional",
        "programme",
        "Vlaanderen>Omgeving>ISE_Afval",
        "105900000",
        "105900000",
        "Strong BBT: 105.9m total (MVG 102.4 + MINA 3.5); UPV/zwerfvuil fonds +74m jump; OVAM toelage 28.3m",
        "strong",
        "src_vl_bbt_omgeving_bo2026",
        "Households municipalities producers UPV",
        "Waste materials circular economy dual Wallonia",
        "Producer-pay UPV large share; dual SPAQuE soil separate; L5 residual",
        "3",
        "7.0",
        "4",
        "5.15",
        "FOI UPV cash path; dual unit-cost waste agencies",
        "seed",
        "",
        "tick354 dual waste",
    ],
    [
        "lb_spaque_24m",
        "SPAQuE Wallonia remediation dotation 24m 2026 dual OVAM",
        "regional",
        "programme",
        "Wallonie>ARNE>SPAQuE",
        "24138000",
        "24138000",
        "Strong DO15 062.018 Dotation SPAQuE 24.138m; dual Flanders OVAM soil ISE 41.1m",
        "strong",
        "src_wal_do15_waste_spaque_2026",
        "Polluted sites Wallonia residents",
        "Public soil remediation dual OVAM",
        "Classic dual remediation SOE; site L5 opacity",
        "4",
        "6.5",
        "5",
        "5.45",
        "FOI top remediation sites L5; dual unit-cost",
        "seed",
        "",
        "tick354 SPAQuE",
    ],
    [
        "lb_waste_dual_vl_wal_116m",
        "Dual waste policy VL Afval + WAL dechets class ~116m 2026",
        "regional",
        "programme",
        "BE>dual>Waste",
        "115759000",
        "115759000",
        "Medium dual class: VL ISE Afval 105.9 + WAL 15.064 CL 9.859 = 115.8m; SPAQuE remediation dual separate ~65m with Bodem",
        "medium",
        "src_vl_bbt_omgeving_bo2026",
        "Two regional waste material systems",
        "Classic dual waste competence + dual agencies OVAM/SPAQuE",
        "Scale asymmetric; UPV producer-pay vs taxpayer; L5 FOI both",
        "4",
        "7.0",
        "5",
        "5.7",
        "Map full dual waste+soil; FOI L5 awards",
        "seed",
        "",
        "tick354 dual structure",
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
    if r["task_id"] == "rq_345":
        r["status"] = "done"
        r["blocked_gap_id"] = "gap_waste_dual_ovam_spaque_l5"
        r["updated_utc"] = now
        r["notes"] = (
            "tick354: VL ISE Afval 105.9m OVAM 28.3m dual WAL dechets 9.9m SPAQuE 24.1m; "
            "FOI L5; spawn rq_346"
        )

rows.append(
    {
        "task_id": "rq_346",
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
        "notes": "Spawned tick354 after waste dual OVAM/SPAQuE; rq_116 SWA deferred",
    }
)
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

with open(base / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_waste_dual_ovam_spaque_l5,BE>dual>Waste>OVAM_SPAQuE_L5,ovam,"
        "OVAM top30 local-gov waste/asbest subsidies 2023-2025; MINA OVAM soil remediation site list cash; "
        "UPV/zwerfvuil fonds cash path 2026 once ISA live; SPAQuE top20 remediation sites 2023-2025 EUR; "
        "ISSeP missions split vs SPAQuE; dual unit-cost,"
        "ISE Afval 105.9m SPAQuE 24.1m strong; residual L5 sites grants dual,"
        "5,OVAM / SPAQuE / Team Openbaarheid / SPW ARNE,"
        "openbaarheid@vlaanderen.be; contact@spaque.be,"
        "Stationsstraat 110 Mechelen; SPAQuE Liege,"
        "docs/doge/foi/drafts/gap_waste_dual_ovam_spaque_l5.md,"
        "ready,2026-07-31,,,,,cmt_waste_dual_ovam_spaque_2026,"
        "lb_vl_ise_afval_106m|lb_spaque_24m|lb_waste_dual_vl_wal_116m,"
        "2026-07-31T15:45:00Z,2026-07-31T15:45:00Z,"
        "tick354 public BBT+DO15; residual L5 human send\n"
    )

with open(base / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    f.write(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    )
    f.write(
        f"main,continuous,hole_fill,{now},{unit},354,no,"
        "Scheduler 60s. Next prio5 rq_346; rq_116 SWA deferred. FOI ready. "
        "tick354 waste dual OVAM/SPAQuE.\n"
    )

print("CSV updates OK")

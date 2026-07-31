# tick 349 — Onroerend Erfgoed Flanders dual heritage
import csv
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T13:15:00Z"
unit = "rq_340"

# --- entities ---
with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "onroerend_erfgoed,Agentschap Onroerend Erfgoed,Agence du Patrimoine immobilier Flandre,"
        "Flanders Immovable Heritage Agency,agency,vlaanderen_gov,nl,"
        "https://www.onroerenderfgoed.be,openbaarheid@vlaanderen.be,,"
        "BO2026 VAK 121.8m VEK 127.8m; premies 92.9m VAK; dual AWaP residual; tick349\n"
    )
    f.write(
        "awap,Agence wallonne du Patrimoine AWaP,Agence wallonne du Patrimoine,"
        "Walloon Heritage Agency dual Flanders OE,agency,wallonie_gov,fr,"
        "https://agencewallonnedupatrimoine.be,,,Dual OE Flanders; budget total residual FOI; tick349\n"
    )

# --- sources ---
with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_vl_bbt_oe_bo2026,"
        "Vlaams Parlement BBT Onroerend Erfgoed Begroting 2026 13-O Nr1,"
        "https://docs.vlaamsparlement.be/pfile?id=2226298,"
        "Vlaams Parlement / Agentschap Onroerend Erfgoed,2026-07-31,official_budget,"
        "Strong: BO2026 VAK 121.823m VEK 127.789m; BA2025 150.764/132.084; "
        "ISE kwaliteit 100/92.7m; premies 92.9/83.2m; dual AWaP FOI; tick349\n"
    )

# --- budgets ---
buds = [
    (
        "bud_oe_vak_2026",
        "onroerend_erfgoed",
        2026,
        121823000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "TOTAAL OE excl apparaatrek/prog B BO2026 VAK 121.823m (kEUR table)",
    ),
    (
        "bud_oe_vek_2026",
        "onroerend_erfgoed",
        2026,
        127789000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "TOTAAL OE BO2026 VEK 127.789m",
    ),
    (
        "bud_oe_vak_2025_ba",
        "onroerend_erfgoed",
        2025,
        150764000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "BA2025 VAK 150.764m (incl one-off Thermae Palace 30m class in partnerschappen)",
    ),
    (
        "bud_oe_vek_2025_ba",
        "onroerend_erfgoed",
        2025,
        132084000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "BA2025 VEK 132.084m",
    ),
    (
        "bud_oe_ise_kwaliteit_vak_2026",
        "onroerend_erfgoed",
        2026,
        99995000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "ISE Kwaliteit onroerenderfgoedzorg VAK 99.995m = 82.1pct of policy credits",
    ),
    (
        "bud_oe_ise_kwaliteit_vek_2026",
        "onroerend_erfgoed",
        2026,
        92702000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "ISE Kwaliteit VEK 92.702m BO2026",
    ),
    (
        "bud_oe_premies_vak_2026",
        "onroerend_erfgoed",
        2026,
        92864000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "Article QG0-1QGD2CB-WT premies VAK 92.864m (standard max 45.3m + waitlist + other)",
    ),
    (
        "bud_oe_premies_vek_2026",
        "onroerend_erfgoed",
        2026,
        83188000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "Premies VEK 83.188m BO2026; -6.562m recurrent cut path",
    ),
    (
        "bud_oe_premie_standaard_max_2026",
        "onroerend_erfgoed",
        2026,
        45300000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "Erfgoedpremie standaardprocedure max 45.3m 2026 (-7m vs 2025)",
    ),
    (
        "bud_oe_wachtlijst_new_2026",
        "onroerend_erfgoed",
        2026,
        9000000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "Base 9m new waitlist restauratie/erfgoedpremies bijzondere procedure 2026",
    ),
    (
        "bud_oe_erfgoedleningen_vak_2026",
        "onroerend_erfgoed",
        2026,
        7000000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "Erfgoedleningen PFV VAK 7.0m ESR-neutral (QG0-1QGD2CB-PA)",
    ),
    (
        "bud_oe_erfgoedleningen_vek_2026",
        "onroerend_erfgoed",
        2026,
        9383000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "Erfgoedleningen VEK 9.383m 2026",
    ),
    (
        "bud_oe_ise_partners_vak_2026",
        "onroerend_erfgoed",
        2026,
        16953000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "ISE Partnerschappen VAK 16.953m (drop from BA 43.699 after Thermae Palace one-off reverse)",
    ),
    (
        "bud_oe_ise_partners_vek_2026",
        "onroerend_erfgoed",
        2026,
        29540000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "ISE Partnerschappen VEK 29.540m incl Thermae Palace ~15m class",
    ),
    (
        "bud_oe_ise_thema_vak_2026",
        "onroerend_erfgoed",
        2026,
        4875000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "ISE Thema-overschrijdend instrumentarium VAK 4.875m",
    ),
    (
        "bud_oe_ise_thema_vek_2026",
        "onroerend_erfgoed",
        2026,
        5547000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "ISE Thema-overschrijdend VEK 5.547m",
    ),
    (
        "bud_oe_prioritaire_partners_2026",
        "onroerend_erfgoed",
        2026,
        1710000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "Prioritaire onroerenderfgoedpartners QG0-1QGD2BC-WT 1.710m VAK=VEK",
    ),
    (
        "bud_oe_ioed_vak_2026",
        "onroerend_erfgoed",
        2026,
        2587000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "IOED intergemeentelijke diensten VAK 2.587m (30 recognised)",
    ),
    (
        "bud_oe_bourla_max_envelope",
        "onroerend_erfgoed",
        2025,
        40170000,
        "budgeted",
        "src_vl_bbt_oe_bo2026",
        "strong",
        "Max VL contribution Bourlaschouwburg Antwerp restoration 40.17m multi-year (VR 2020 path)",
    ),
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        note = b[7].replace('"', "'")
        f.write(f'{b[0]},{b[1]},{b[2]},{b[3]},,,{b[4]},{b[5]},{b[6]},"{note}"\n')

# --- commitments ---
cmt_json = (
    '{"vak_2026_m":121.823,"vek_2026_m":127.789,"vak_2025_ba_m":150.764,"vek_2025_ba_m":132.084,'
    '"ise_kwaliteit_vak_m":99.995,"ise_kwaliteit_vek_m":92.702,"premies_vak_m":92.864,'
    '"premies_vek_m":83.188,"standaard_max_m":45.3,"wachtlijst_new_m":9.0,'
    '"leningen_vak_m":7.0,"partners_vak_m":16.953,"partners_vek_m":29.54,'
    '"bourla_max_m":40.17,"cut_premies_m":6.562,'
    '"note":"Dual AWaP Wallonia total residual FOI; federal FSI/Cinematek separate Belspo stack"}'
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_oe_package_2025_26,"
        "Flanders Onroerend Erfgoed agency package dual AWaP,"
        "onroerend_erfgoed,"
        "Heritage owners municipalities IOED Herita restaurateurs,"
        "Onroerenderfgoeddecreet 12 jul 2013 + BBT BO2026,"
        "2025-01-01,2025,2026,150764000,"
        f'"{cmt_json}",'
        ",active,https://docs.vlaamsparlement.be/pfile?id=2226298,"
        "Protect restore activate Flemish immovable heritage,"
        "Publish L5 top premie awards; dual unit-cost AWaP; waitlist path,"
        "src_vl_bbt_oe_bo2026,strong,Vlaanderen>Omgeving>OnroerendErfgoed,"
        "tick349: VEK 127.8m 2026 dual AWaP residual\n"
    )

# --- leaderboard ---
lbs = [
    [
        "lb_oe_vek_128m",
        "Flanders Onroerend Erfgoed VEK 128m 2026 dual AWaP",
        "regional",
        "programme",
        "Vlaanderen>Omgeving>OnroerendErfgoed",
        "127789000",
        "127789000",
        "Strong BBT BO2026: VEK 127.789m VAK 121.823m; premies 83-93m; dual AWaP residual",
        "strong",
        "src_vl_bbt_oe_bo2026",
        "Heritage owners municipalities sector partners",
        "Immovable heritage protection restoration activation",
        "Core culture-heritage; waitlist opacity; dual community structure incomplete without AWaP",
        "3",
        "6.5",
        "4",
        "4.9",
        "Open L5 premie top20; dual AWaP map; waitlist euros",
        "seed",
        "",
        "tick349 dual heritage",
    ],
    [
        "lb_oe_premies_83m",
        "OE erfgoedpremies VEK 83m 2026 waitlist path",
        "regional",
        "subsidy",
        "Vlaanderen>OnroerendErfgoed>premies",
        "83188000",
        "92864000",
        "Strong BBT: premies VAK 92.864 VEK 83.188; standaard max 45.3; waitlist new 9m; -6.562m cut",
        "strong",
        "src_vl_bbt_oe_bo2026",
        "Protected heritage owners restaurateurs",
        "Premium support restoration maintenance research archaeology",
        "Large discretionary L5 opacity; historical waitlist; savings path 2026-27",
        "4",
        "6.0",
        "4",
        "4.8",
        "FOI named awards + waitlist stock EUR",
        "seed",
        "",
        "tick349 L5 residual",
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
    if r["task_id"] == "rq_340":
        r["status"] = "done"
        r["blocked_gap_id"] = "gap_oe_awap_dual_l5"
        r["updated_utc"] = now
        r["notes"] = (
            "tick349: OE BO2026 VAK 121.8m VEK 127.8m premies 83-93m dual AWaP FOI; "
            "spawn rq_341 progress@350 next"
        )

rows.append(
    {
        "task_id": "rq_341",
        "title": "Progress coverage % + waste top10 @ tick 350",
        "sprint": "continuous",
        "priority": "10",
        "status": "open",
        "hierarchy_target": "L0",
        "entity_id": "gg_belgium",
        "instructions": "MANDATORY progress@350: refresh progress_every_10_ticks.md coverage A-E and doge_waste_top10_current.md; note inventory counts.",
        "blocked_gap_id": "",
        "created_utc": now,
        "updated_utc": "",
        "notes": "Spawned tick349; next tick is 350 progress milestone",
    }
)
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

# --- foi_queue ---
with open(base / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_oe_awap_dual_l5,BE>dual>Heritage>OE_AWaP_L5,onroerend_erfgoed,"
        "Named top30 OE premie awards 2023-2026 with amounts beneficiaries; waitlist stock EUR and age; "
        "Herita SWO 2026-2030 cash path; AWaP Wallonia total budget 2024-2026 and top subsidies L5,"
        "OE package strong 128m; L5 premie concentration and dual AWaP total still opaque,"
        "5,Agentschap Onroerend Erfgoed / AWaP / Team Openbaarheid,"
        "openbaarheid@vlaanderen.be; subventions.developpement.strategique@awap.be,"
        "Havenlaan 88 1000 Brussel; AWaP Namur,"
        "docs/doge/foi/drafts/gap_oe_awap_dual_l5.md,"
        "ready,2026-07-31,,,,,cmt_oe_package_2025_26,"
        "lb_oe_vek_128m|lb_oe_premies_83m,"
        "2026-07-31T13:15:00Z,2026-07-31T13:15:00Z,"
        "tick349 public BBT fill; residual L5+AWaP human send\n"
    )

# --- loop_state ---
with open(base / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    f.write(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    )
    f.write(
        f"main,continuous,hole_fill,{now},{unit},349,no,"
        "Scheduler 60s. Next MANDATORY rq_341 progress@350; rq_116 SWA deferred. "
        "FOI ready. tick349 OE heritage dual.\n"
    )

print("CSV updates OK")

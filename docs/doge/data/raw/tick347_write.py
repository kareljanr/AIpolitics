# tick 347 — FWO + FNRS dual community research funds
import csv
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T12:15:00Z"
unit = "rq_338"

# --- entities ---
with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "fwo,Fonds Wetenschappelijk Onderzoek Vlaanderen FWO,"
        "Fonds de la Recherche Scientifique Flandre FWO,"
        "Research Foundation Flanders dual FNRS,agency,vlaanderen_gov,nl,"
        "https://www.fwo.be,,,VL vastlegging 470.3m 2024 / 448.2m 2025; dual FNRS; tick347\n"
    )
    f.write(
        "fnrs,F.R.S.-FNRS Fonds de la Recherche Scientifique,"
        "F.R.S.-FNRS Fonds de la Recherche Scientifique,"
        "FWB fundamental research fund dual FWO,agency,fwb_gov,fr,"
        "https://www.frs-fnrs.be,,,Public subs 241.8m 2024 total res 262.2m; dual FWO; tick347\n"
    )

# --- sources ---
with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_fwo_jv_2024,"
        "FWO Jaarverslag 2024 vastleggingskrediet 470.3m,"
        "https://fwo.be/media/dslbztr3/jaarverslag-2024.pdf,"
        "FWO,2026-07-31,official_annual_report,"
        "Strong: VL vastlegging BA2024 470.342m; vereffening total 436.818m; "
        "beheer 19.324m 4.11pct; dual FNRS; tick347\n"
    )
    f.write(
        "src_fwo_jv_2025,"
        "FWO Jaarverslag 2025 vastleggingskrediet 448.2m,"
        "https://fwo.be/media/d20b1dxf/jaarverslag-2025.pdf,"
        "FWO,2026-07-31,official_annual_report,"
        "Strong: VL vastlegging BA2025 448.182m; vereffening total 464.623m; "
        "beheer 23.107m 5.16pct; dual FNRS; tick347\n"
    )
    f.write(
        "src_fnrs_ra_2024,"
        "F.R.S.-FNRS Rapport annuel 2024 subventions publiques 241.8m,"
        "https://www.frs-fnrs.be/docs/RapportAnnuel_2024.pdf,"
        "F.R.S.-FNRS,2026-07-31,official_annual_report,"
        "Strong: public subs 241.818m (FWB 173.54 federal 40.33 WAL 19.93 LN 8.02); "
        "total res 262.183m; spend mandats 153.0 projets 93.3 admin 15.3; dual FWO; tick347\n"
    )

# --- budgets ---
buds = [
    (
        "bud_fwo_vl_vastlegging_2024",
        "fwo",
        2024,
        470342148,
        "budgeted",
        "src_fwo_jv_2024",
        "strong",
        "VL vastleggingskrediet BA2024 total 470.342m (JV Tabel 1)",
    ),
    (
        "bud_fwo_vl_vereffening_2024",
        "fwo",
        2024,
        436818302,
        "budgeted",
        "src_fwo_jv_2024",
        "strong",
        "Vereffeningskrediet Algemeen totaal FWO 436.818m 2024 (Tabel 2 sum)",
    ),
    (
        "bud_fwo_fund_projects_vast_2024",
        "fwo",
        2024,
        180070272,
        "budgeted",
        "src_fwo_jv_2024",
        "strong",
        "Fundamenteel onderzoek projecten vastlegging 180.070m 2024",
    ),
    (
        "bud_fwo_fund_mandaten_vast_2024",
        "fwo",
        2024,
        109378331,
        "budgeted",
        "src_fwo_jv_2024",
        "strong",
        "Fundamenteel mandaten vastlegging 109.378m 2024 (after federal/EU netting)",
    ),
    (
        "bud_fwo_sbo_projects_vast_2024",
        "fwo",
        2024,
        51459910,
        "budgeted",
        "src_fwo_jv_2024",
        "strong",
        "SBO projects vastlegging 51.460m 2024",
    ),
    (
        "bud_fwo_sbo_mandaten_vast_2024",
        "fwo",
        2024,
        43004632,
        "budgeted",
        "src_fwo_jv_2024",
        "strong",
        "SBO mandaten vastlegging 43.005m 2024",
    ),
    (
        "bud_fwo_infra_vast_2024",
        "fwo",
        2024,
        66176183,
        "budgeted",
        "src_fwo_jv_2024",
        "strong",
        "Infrastructure vastlegging 66.176m 2024 (VSC+mid/zwaar+opstap)",
    ),
    (
        "bud_fwo_beheer_2024",
        "fwo",
        2024,
        19324422,
        "budgeted",
        "src_fwo_jv_2024",
        "strong",
        "Beheerskosten 19.324m = 4.11pct of VL vastlegging 2024",
    ),
    (
        "bud_fwo_vl_vastlegging_2025",
        "fwo",
        2025,
        448182376,
        "budgeted",
        "src_fwo_jv_2025",
        "strong",
        "VL vastleggingskrediet BA2025 total 448.182m (JV Tabel 1)",
    ),
    (
        "bud_fwo_vl_vereffening_2025",
        "fwo",
        2025,
        464623314,
        "budgeted",
        "src_fwo_jv_2025",
        "strong",
        "Vereffeningskrediet Algemeen totaal FWO 464.623m 2025",
    ),
    (
        "bud_fwo_fund_projects_vast_2025",
        "fwo",
        2025,
        201394065,
        "budgeted",
        "src_fwo_jv_2025",
        "strong",
        "Fundamenteel projecten vastlegging 201.394m 2025",
    ),
    (
        "bud_fwo_fund_mandaten_vast_2025",
        "fwo",
        2025,
        111703492,
        "budgeted",
        "src_fwo_jv_2025",
        "strong",
        "Fundamenteel mandaten vastlegging 111.703m 2025",
    ),
    (
        "bud_fwo_beheer_2025",
        "fwo",
        2025,
        23107000,
        "budgeted",
        "src_fwo_jv_2025",
        "strong",
        "Beheerskosten 23.107m = 5.16pct of VL vastlegging 2025",
    ),
    (
        "bud_fnrs_public_subs_2024",
        "fnrs",
        2024,
        241818225,
        "outturn",
        "src_fnrs_ra_2024",
        "strong",
        "Subventions publiques 241.818m 2024 (FWB+fed+WAL+LN)",
    ),
    (
        "bud_fnrs_total_resources_2024",
        "fnrs",
        2024,
        262182669,
        "outturn",
        "src_fnrs_ra_2024",
        "strong",
        "Ressources globales 262.183m 2024 (public 241.8 + private/televie/autres ~20.4)",
    ),
    (
        "bud_fnrs_fwb_dot_2024",
        "fnrs",
        2024,
        173540160,
        "outturn",
        "src_fnrs_ra_2024",
        "strong",
        "FWB subvention 173.540m 2024 largest public line",
    ),
    (
        "bud_fnrs_federal_2024",
        "fnrs",
        2024,
        40326857,
        "outturn",
        "src_fnrs_ra_2024",
        "strong",
        "Federal (IISN+FRSM incl) 40.327m 2024",
    ),
    (
        "bud_fnrs_wallonie_2024",
        "fnrs",
        2024,
        19931591,
        "outturn",
        "src_fnrs_ra_2024",
        "strong",
        "Region wallonne 19.932m 2024",
    ),
    (
        "bud_fnrs_loterie_2024",
        "fnrs",
        2024,
        8019617,
        "outturn",
        "src_fnrs_ra_2024",
        "strong",
        "Loterie Nationale 8.020m 2024",
    ),
    (
        "bud_fnrs_televie_2024",
        "fnrs",
        2024,
        10871413,
        "outturn",
        "src_fnrs_ra_2024",
        "strong",
        "Telvie private cancer research 10.871m 2024",
    ),
    (
        "bud_fnrs_spend_mandats_2024",
        "fnrs",
        2024,
        152957352,
        "outturn",
        "src_fnrs_ra_2024",
        "strong",
        "Depenses doctorats postdocs mandats permanents 152.957m 2024",
    ),
    (
        "bud_fnrs_spend_projets_2024",
        "fnrs",
        2024,
        93258525,
        "outturn",
        "src_fnrs_ra_2024",
        "strong",
        "Depenses projets credits autres 93.259m 2024",
    ),
    (
        "bud_fnrs_admin_2024",
        "fnrs",
        2024,
        15271110,
        "outturn",
        "src_fnrs_ra_2024",
        "strong",
        "Support administratif 15.271m 2024",
    ),
    (
        "bud_research_dual_fwo_fnrs_2024",
        "fwo",
        2024,
        712160373,
        "budgeted",
        "src_fwo_jv_2024",
        "medium",
        "Illustrative dual 2024: FWO VL vastlegging 470.342 + FNRS public 241.818 = 712.160m; not additive TE; federal streams both sides",
    ),
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        note = b[7].replace('"', "'")
        f.write(f'{b[0]},{b[1]},{b[2]},{b[3]},,,{b[4]},{b[5]},{b[6]},"{note}"\n')

# --- commitments ---
cmt_json = (
    '{"fwo_vast_2024_m":470.342,"fwo_vereff_2024_m":436.818,"fwo_vast_2025_m":448.182,'
    '"fwo_vereff_2025_m":464.623,"fwo_beheer_2024_m":19.324,"fwo_beheer_2025_m":23.107,'
    '"fnrs_public_2024_m":241.818,"fnrs_total_res_2024_m":262.183,"fnrs_fwb_2024_m":173.54,'
    '"fnrs_fed_2024_m":40.327,"fnrs_wal_2024_m":19.932,"fnrs_ln_2024_m":8.02,'
    '"fnrs_mandats_spend_2024_m":152.957,"fnrs_projets_spend_2024_m":93.259,'
    '"dual_class_2024_m":712.2,'
    '"note":"Dual community fundamental research funds; FWO EVA private stichting; FNRS ASBL; federal Maribel/IISN both sides"}'
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_fwo_fnrs_dual_research_2024_25,"
        "FWO Flanders + FNRS FWB dual fundamental research funding,"
        "fwo,"
        "University researchers PhD postdocs projects both communities,"
        "Community research competence FWO SO / FWB research decree FNRS,"
        "2024-01-01,2024,2025,712160373,"
        f'"{cmt_json}",'
        ",active,https://fwo.be/media/dslbztr3/jaarverslag-2024.pdf,"
        "Bottom-up excellence fundamental and strategic research dual communities,"
        "Compare unit-cost dual; FOI L5 award concentration; map federal TE vs cash,"
        "src_fwo_jv_2024,strong,BE>dual>Research_FWO_FNRS,"
        "tick347: FWO 470/448m vast dual FNRS public 242m\n"
    )

# --- leaderboard ---
lbs = [
    [
        "lb_fwo_vl_470m",
        "FWO Flanders VL vastlegging 470m 2024 dual FNRS",
        "regional",
        "subsidy",
        "Vlaanderen>WEWIS>FWO",
        "470342148",
        "470342148",
        "Strong JV2024: VL vastlegging 470.342m; vereff 436.8m; 2025 vast 448.2m; dual FNRS 242m public",
        "strong",
        "src_fwo_jv_2024",
        "Flemish university researchers PhD postdocs",
        "Fundamental strategic clinical research infrastructure",
        "Large excellence fund; dual community twin FNRS; overhead 4-5pct of vastlegging",
        "3",
        "8.0",
        "4",
        "5.5",
        "Publish L5 top awards concentration; dual unit-cost FNRS",
        "seed",
        "",
        "tick347 dual research",
    ],
    [
        "lb_fnrs_public_242m",
        "FNRS public subsidies 242m 2024 dual FWO",
        "regional",
        "subsidy",
        "FWB>Recherche>FNRS",
        "241818225",
        "241818225",
        "Strong RA2024: public 241.818m (FWB 173.5 fed 40.3 WAL 19.9 LN 8.0); total res 262.2m; dual FWO 470m",
        "strong",
        "src_fnrs_ra_2024",
        "FWB university researchers PhD postdocs",
        "Fundamental research dual Flanders FWO",
        "Smaller absolute than FWO; multi-source public (FWB+fed+WAL+lottery); private Telvie separate",
        "3",
        "7.5",
        "4",
        "5.3",
        "FOI L5 mandats/projets concentration; 2025-26 FWB cut path",
        "seed",
        "",
        "tick347 dual FWO",
    ],
    [
        "lb_research_dual_fwo_fnrs_712m",
        "Dual community research FWO+FNRS class ~712m 2024",
        "regional",
        "subsidy",
        "BE>dual>Research_community",
        "712160000",
        "712160000",
        "Medium dual class: FWO VL vast 470.3 + FNRS public 241.8 = 712.2m 2024; not TE-additive; federal streams both",
        "medium",
        "src_fwo_jv_2024",
        "Two community research systems",
        "Classic dual community research competence after state reform",
        "Dual overhead pattern; excellence competition both sides; large absolute vs culture dual",
        "5",
        "8.5",
        "5",
        "6.75",
        "Map full dual TCO + federal TE EIWT researchers; FOI L5 both",
        "seed",
        "",
        "tick347 dual structure",
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
    if r["task_id"] == "rq_338":
        r["status"] = "done"
        r["blocked_gap_id"] = "gap_fwo_fnrs_l5"
        r["updated_utc"] = now
        r["notes"] = (
            "tick347: FWO VL vast 470.3m 2024 / 448.2m 2025 dual FNRS public 241.8m; "
            "FOI L5; spawn rq_339"
        )

rows.append(
    {
        "task_id": "rq_339",
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
        "notes": "Spawned tick347 after FWO+FNRS dual research; rq_116 SWA deferred",
    }
)
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

# --- foi_queue ---
with open(base / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_fwo_fnrs_l5,BE>dual>Research>FWO_FNRS_L5,fwo,"
        "Machine-readable top awards FWO and FNRS 2023-2025 (projects mandats by institution discipline amount); "
        "reconcile federal cash Maribel/IISN vs TE defiscalisatie; FWB FNRS multi-year cash path post 2025 cuts if any,"
        "Dual research ~712m class; agency totals strong; L5 concentration and federal cash residual,"
        "5,FWO / FNRS / Team Openbaarheid Vlaanderen / FWB,"
        "openbaarheid@vlaanderen.be; communication@frs-fnrs.be,"
        "Egmontstraat 5 1000 Brussel; FNRS Bruxelles,"
        "docs/doge/foi/drafts/gap_fwo_fnrs_l5.md,"
        "ready,2026-07-31,,,,,cmt_fwo_fnrs_dual_research_2024_25,"
        "lb_fwo_vl_470m|lb_fnrs_public_242m|lb_research_dual_fwo_fnrs_712m,"
        "2026-07-31T12:15:00Z,2026-07-31T12:15:00Z,"
        "tick347 public JV+RA fill; residual L5 human send\n"
    )

# --- loop_state ---
with open(base / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    f.write(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    )
    f.write(
        f"main,continuous,hole_fill,{now},{unit},347,no,"
        "Scheduler 60s. Next prio5 rq_339; rq_116 SWA deferred. FOI ready. "
        "tick347 FWO+FNRS dual research.\n"
    )

print("CSV updates OK")

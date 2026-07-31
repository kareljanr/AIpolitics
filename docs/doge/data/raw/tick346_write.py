# tick 346 — Sport Vlaanderen + ADEPS dual community sport
import csv
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T11:45:00Z"
unit = "rq_337"

# --- entities ---
with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "sport_vlaanderen,Sport Vlaanderen agentschap,Sport Vlaanderen agence,"
        "Sport Flanders agency dual ADEPS FWB,agency,vlaanderen_gov,nl,"
        "https://www.sport.vlaanderen,,,BO2026 prog HF VEK 167.136m VAK 177.121m; dual ADEPS 49.891m; tick346\n"
    )
    f.write(
        "adeps,ADEPS Administration generale du Sport FWB,ADEPS Administration generale du Sport,"
        "FWB General Sport Administration dual Sport Vlaanderen,agency,fwb_gov,fr,"
        "https://www.sport-adeps.be,,,FWB sport package 49.891m 2025; 587 staff; dual Sport VL; tick346\n"
    )

# --- sources ---
with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_vl_bbt_sport_bo2026,"
        "Vlaams Parlement BBT Sport Begroting 2026 13-V Nr1,"
        "https://docs.vlaamsparlement.be/pfile?id=2227509,"
        "Vlaams Parlement / Sport Vlaanderen,2026-07-31,official_budget,"
        "Strong: prog HF BO2026 VAK 177.121m VEK 167.136m; BA2025 183.884/185.264; "
        "toelage 175.934/165.949; topsport 31.659; dual ADEPS; tick346\n"
    )
    f.write(
        "src_adeps_ra_2025,"
        "ADEPS Rapport annuel d activites 2025 budget FWB sport 49.891m,"
        "https://www.sport-adeps.be/fileadmin/sites/adeps/upload/adeps_super_editor/"
        "adeps_editor/documents/A_propos/Rapports_annuels/Rapport_annuel_Adeps_2025_2.pdf,"
        "ADEPS / FWB,2026-07-31,official_annual_report,"
        "Strong: FWB sport 49.891m 0.3pct total BA2025; subventions federations 8.32+12.93m; "
        "CSL 5.59m SHN 1.25m; staff 587; dual Sport VL; tick346\n"
    )
    f.write(
        "src_adeps_audit_2025,"
        "Audit de fonctionnement AGS ADEPS 2025 final report,"
        "https://www.sport-adeps.be/,"
        "Cabinet Sports FWB / external audit,2026-07-31,official_audit,"
        "Medium process audit Apr-Dec 2025; transparency recommendations; "
        "budget euros in RA primary; tick346\n"
    )

# --- budgets ---
buds = [
    (
        "bud_sport_vl_prog_hf_vek_2026",
        "sport_vlaanderen",
        2026,
        167136000,
        "budgeted",
        "src_vl_bbt_sport_bo2026",
        "strong",
        "BBT Sport BO2026 TOTAAL SPORT excl DAB/apparaat/prog B: VEK 167.136m (VAK 177.121m); kEUR table",
    ),
    (
        "bud_sport_vl_prog_hf_vak_2026",
        "sport_vlaanderen",
        2026,
        177121000,
        "budgeted",
        "src_vl_bbt_sport_bo2026",
        "strong",
        "BBT Sport BO2026 VAK 177.121m prog HF / TOTAAL SPORT excl DAB",
    ),
    (
        "bud_sport_vl_prog_hf_vek_2025_ba",
        "sport_vlaanderen",
        2025,
        185264000,
        "budgeted",
        "src_vl_bbt_sport_bo2026",
        "strong",
        "BA 2025 VEK 185.264m VAK 183.884m same perimeter excl DAB",
    ),
    (
        "bud_sport_vl_prog_hf_vak_2025_ba",
        "sport_vlaanderen",
        2025,
        183884000,
        "budgeted",
        "src_vl_bbt_sport_bo2026",
        "strong",
        "BA 2025 VAK 183.884m",
    ),
    (
        "bud_sport_vl_toelage_vek_2026",
        "sport_vlaanderen",
        2026,
        165949000,
        "budgeted",
        "src_vl_bbt_sport_bo2026",
        "strong",
        "Toelage Sport voor Allen internal streams VEK 165.949m (VAK 175.934m) HB0-1HFH2NY-IS + HB0-1HFH5NY-IS",
    ),
    (
        "bud_sport_vl_toelage_vak_2026",
        "sport_vlaanderen",
        2026,
        175934000,
        "budgeted",
        "src_vl_bbt_sport_bo2026",
        "strong",
        "Toelage VAK 175.934m via two IS articles (HB0-1HFH2NY-IS 138.821 + HB0-1HFH5NY-IS 37.113)",
    ),
    (
        "bud_sport_vl_topsport_2026",
        "sport_vlaanderen",
        2026,
        31659000,
        "budgeted",
        "src_vl_bbt_sport_bo2026",
        "strong",
        "ISE Topsport BO2026 VAK=VEK 31.659m (BA2025 30.074 +1.585)",
    ),
    (
        "bud_sport_vl_ise_allen_vek_2026",
        "sport_vlaanderen",
        2026,
        125546000,
        "budgeted",
        "src_vl_bbt_sport_bo2026",
        "strong",
        "ISE Sport voor allen agency VEK 125.546m BO2026 (VAK 125.088)",
    ),
    (
        "bud_sport_vl_ise_infra_vek_2026",
        "sport_vlaanderen",
        2026,
        30876000,
        "budgeted",
        "src_vl_bbt_sport_bo2026",
        "strong",
        "ISE Sportinfrastructuur VEK 30.876m BO2026 (VAK 36.948; cut from BA 47.679)",
    ),
    (
        "bud_sport_vl_antidoping_2026",
        "sport_vlaanderen",
        2026,
        1445000,
        "budgeted",
        "src_vl_bbt_sport_bo2026",
        "strong",
        "ISE Antidoping BO2026 1.445m VAK=VEK",
    ),
    (
        "bud_adeps_fwb_sport_2025",
        "adeps",
        2025,
        49891000,
        "budgeted",
        "src_adeps_ra_2025",
        "strong",
        "FWB sport package adjusted 2025 49.891m = 0.3pct FWB total (ordinaire + SACA Loterie); primary RA p11",
    ),
    (
        "bud_adeps_fed_forfait_2025",
        "adeps",
        2025,
        8319688,
        "budgeted",
        "src_adeps_ra_2025",
        "strong",
        "Subvention forfaitaire federations 8.319688m 2025",
    ),
    (
        "bud_adeps_fed_plan_prog_2025",
        "adeps",
        2025,
        12932070,
        "budgeted",
        "src_adeps_ra_2025",
        "strong",
        "Soutien federations plan-programme 12.932070m 2025",
    ),
    (
        "bud_adeps_csl_2025",
        "adeps",
        2025,
        5592845,
        "budgeted",
        "src_adeps_ra_2025",
        "strong",
        "Soutien centres sportifs locaux 5.592845m 2025",
    ),
    (
        "bud_adeps_shn_contracts_2025",
        "adeps",
        2025,
        1251435,
        "budgeted",
        "src_adeps_ra_2025",
        "strong",
        "Contrats sportifs haut niveau ADEPS 1.251435m 2025",
    ),
    (
        "bud_adeps_jeunes_detection_2025",
        "adeps",
        2025,
        3262171,
        "budgeted",
        "src_adeps_ra_2025",
        "strong",
        "Detection et formation des jeunes 3.262171m 2025",
    ),
    (
        "bud_adeps_asl_used_2025",
        "adeps",
        2025,
        2554572,
        "outturn",
        "src_adeps_ra_2025",
        "strong",
        "Action sportive locale montant global utilise 2.554572m 2025 (modules list also shows 2.028986 class)",
    ),
    (
        "bud_adeps_materiel_awarded_2025",
        "adeps",
        2025,
        1260000,
        "budgeted",
        "src_adeps_ra_2025",
        "strong",
        "Materiel sportif awards 1.26m / liquidated 1.19m; 199 favorable dossiers",
    ),
    (
        "bud_sport_dual_vl_adeps_class_2025",
        "sport_vlaanderen",
        2025,
        235155000,
        "budgeted",
        "src_vl_bbt_sport_bo2026",
        "medium",
        "Illustrative dual class BA2025 VL VEK 185.264 + ADEPS FWB 49.891 = 235.155m; not additive TE; years aligned BA2025",
    ),
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        note = b[7].replace('"', "'")
        f.write(f'{b[0]},{b[1]},{b[2]},{b[3]},,,{b[4]},{b[5]},{b[6]},"{note}"\n')

# --- commitments ---
cmt_json = (
    '{"prog_hf_vek_2026_m":167.136,"prog_hf_vak_2026_m":177.121,'
    '"prog_hf_vek_2025_ba_m":185.264,"prog_hf_vak_2025_ba_m":183.884,'
    '"toelage_vek_2026_m":165.949,"toelage_vak_2026_m":175.934,'
    '"topsport_2026_m":31.659,"ise_allen_vek_2026_m":125.546,'
    '"ise_infra_vek_2026_m":30.876,"antidoping_2026_m":1.445,'
    '"adeps_fwb_sport_2025_m":49.891,"adeps_fed_forfait_m":8.32,'
    '"adeps_fed_plan_m":12.93,"adeps_csl_m":5.59,"adeps_shn_m":1.25,'
    '"adeps_staff":587,"adeps_occasional":1215,"adeps_federations":64,'
    '"dual_class_2025_m":235.2,'
    '"note":"Dual community sport policy VL agency vs FWB ADEPS; Brussels region sport residual FOI"}'
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_sport_vl_adeps_dual_2025_26,"
        "Sport Vlaanderen + ADEPS dual community sport packages,"
        "sport_vlaanderen,"
        "Sport federations clubs athletes centres both communities,"
        "Community sport competence Sport Vlaanderen decree / FWB sport decree ADEPS,"
        "2025-01-01,2025,2026,235155000,"
        f'"{cmt_json}",'
        ",active,https://docs.vlaamsparlement.be/pfile?id=2227509,"
        "Mass sport infrastructure elite sport dual community policy,"
        "Compare unit-cost dual; FOI ADEPS L5 + BCR sport residual; map lottery SACA path,"
        "src_vl_bbt_sport_bo2026,strong,BE>dual>Sport_VL_ADEPS,"
        "tick346: VL 167-185m vs ADEPS 49.9m dual community sport\n"
    )

# --- leaderboard ---
lbs = [
    [
        "lb_sport_vl_167m",
        "Sport Vlaanderen prog HF VEK 167m 2026 dual ADEPS",
        "regional",
        "subsidy",
        "Vlaanderen>Sport>SportVlaanderen",
        "167136000",
        "167136000",
        "Strong BBT BO2026: VEK 167.136m VAK 177.121m excl DAB; BA2025 VEK 185.264m; dual ADEPS 49.9m",
        "strong",
        "src_vl_bbt_sport_bo2026",
        "Flemish sport federations clubs centres athletes",
        "Sport for all infrastructure topsport anti-doping",
        "Large agency package; dual community layer vs ADEPS; not pure waste if mass sport real",
        "3",
        "7.0",
        "4",
        "5.0",
        "Publish L5 federation awards; dual unit-cost ADEPS",
        "seed",
        "",
        "tick346 dual community sport",
    ],
    [
        "lb_adeps_fwb_sport_50m",
        "ADEPS FWB sport package 49.9m 2025 dual Sport Vlaanderen",
        "regional",
        "subsidy",
        "FWB>Sport>ADEPS",
        "49891000",
        "49891000",
        "Strong RA2025: 49.891m = 0.3pct FWB; federations 8.32+12.93m CSL 5.59; staff 587; dual VL 167-185m",
        "strong",
        "src_adeps_ra_2025",
        "FWB federations clubs centres SHN athletes",
        "Community sport mass elite centres dual VL",
        "Smaller absolute than VL; dual structure + large occasional workforce; audit transparency residual",
        "4",
        "5.5",
        "4",
        "4.7",
        "FOI SACA lottery split + named federation L5",
        "seed",
        "",
        "tick346 dual Sport Vlaanderen",
    ],
    [
        "lb_sport_dual_vl_adeps_235m",
        "Dual community sport VL+ADEPS class ~235m 2025",
        "regional",
        "subsidy",
        "BE>dual>Sport_community",
        "235155000",
        "235155000",
        "Medium dual class: VL BA2025 VEK 185.264 + ADEPS 49.891 = 235.155m; not additive TE; BCR residual",
        "medium",
        "src_vl_bbt_sport_bo2026",
        "Two community sport systems",
        "Classic dual community competence after state reform",
        "Dual overhead pattern like VAF/CCA tourism PES; elite + mass both sides",
        "5",
        "7.5",
        "5",
        "6.25",
        "Map full dual TCO + BCR sport; FOI L5 both sides",
        "seed",
        "",
        "tick346 dual structure",
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
    if r["task_id"] == "rq_337":
        r["status"] = "done"
        r["blocked_gap_id"] = "gap_sport_vl_adeps_l5"
        r["updated_utc"] = now
        r["notes"] = (
            "tick346: Sport VL VEK 167.136m 2026 dual ADEPS FWB 49.891m 2025; "
            "FOI L5; spawn rq_338"
        )

rows.append(
    {
        "task_id": "rq_338",
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
        "notes": "Spawned tick346 after Sport VL+ADEPS dual; rq_116 SWA deferred",
    }
)
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

# --- foi_queue ---
with open(base / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_sport_vl_adeps_l5,BE>dual>Sport>VL_ADEPS_L5,sport_vlaanderen,"
        "Named L5 federation and club awards Sport Vlaanderen 2024-2026; ADEPS SACA vs ordinaire "
        "cash split and Loterie Nationale line 2023-2026; named top federation plan-programme and "
        "forfait amounts; BCR regional sport residual if material,"
        "Dual community sport ~235m class; VL ISE strong but L5 federation matrix thin; "
        "ADEPS package strong but SACA lottery and L5 residual,"
        "5,Sport Vlaanderen / ADEPS FWB / Team Openbaarheid,"
        "openbaarheid@vlaanderen.be; subvention.adeps.info@cfwb.be,"
        "Havenlaan 88 bus 20 1000 Brussel; ADEPS Bruxelles,"
        "docs/doge/foi/drafts/gap_sport_vl_adeps_l5.md,"
        "ready,2026-07-31,,,,,cmt_sport_vl_adeps_dual_2025_26,"
        "lb_sport_vl_167m|lb_adeps_fwb_sport_50m|lb_sport_dual_vl_adeps_235m,"
        "2026-07-31T11:45:00Z,2026-07-31T11:45:00Z,"
        "tick346 public BBT+RA fill; residual L5 human send\n"
    )

# --- loop_state ---
with open(base / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    f.write(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    )
    f.write(
        f"main,continuous,hole_fill,{now},{unit},346,no,"
        "Scheduler 60s. Next prio5 rq_338; rq_116 SWA deferred. FOI ready. "
        "tick346 Sport VL+ADEPS dual.\n"
    )

print("CSV updates OK")

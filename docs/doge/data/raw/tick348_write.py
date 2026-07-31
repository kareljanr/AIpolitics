# tick 348 — AWV + SOFICO dual roads infrastructure deepen
import csv
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T12:45:00Z"
unit = "rq_339"

# --- entities notes refresh (append notes via new rows only if needed - update not easy; skip new entity) ---
# entities awv and sofico exist; add notes in log only

# --- sources ---
with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_awv_op_2025,"
        "AWV Ondernemingsplan 2024-2025 VAK VEK 2024 outturn,"
        "https://wegenenverkeer.be/sites/default/files/uploads/documenten/Ondernemingsplan%20AWV%202025.pdf,"
        "Agentschap Wegen en Verkeer,2026-07-31,official_agency_plan,"
        "Strong: 2024 VAK 1.0207bn VEK 1.187bn 96.5pct; struct onderh 138.5m 2025; fiets 158m+; dual SOFICO; tick348\n"
    )
    f.write(
        "src_sofico_ra_2024,"
        "SOFICO Rapport annuel 2024 recettes 495m invest 265m,"
        "https://sofico.org/app/uploads/2025/12/rapport-annuel-2024-sofico.pdf,"
        "SOFICO,2026-07-31,official_annual_report,"
        "Strong: produits 495.1m charges 397.6m net 100.7m invest 265m PKPL 347m; "
        "reseau 370.8m 2024 cum 3.7bn since 2010; dual AWV; tick348\n"
    )

# --- budgets ---
buds = [
    (
        "bud_awv_vak_2024",
        "awv",
        2024,
        1020737569,
        "outturn",
        "src_awv_op_2025",
        "strong",
        "VAK beleidskredieten 2024 1.0207bn incl relance FFEU VVF DWV (OP 2025 p results)",
    ),
    (
        "bud_awv_vek_2024",
        "awv",
        2024,
        1187041379,
        "outturn",
        "src_awv_op_2025",
        "strong",
        "VEK besteed 2024 1.187bn = 96.54pct of available (OP 2025)",
    ),
    (
        "bud_awv_struct_onderhoud_2025",
        "awv",
        2025,
        138500000,
        "budgeted",
        "src_awv_op_2025",
        "strong",
        "Structureel onderhoud 2025 138.5m: snelwegen 49.5 + gewest 47 + kunstwerken 33 + DVM 9",
    ),
    (
        "bud_awv_fiets_vast_2025",
        "awv",
        2025,
        158000000,
        "budgeted",
        "src_awv_op_2025",
        "strong",
        "Min 158m vastlegging fietspad projecten 2025 (2024 was 162m)",
    ),
    (
        "bud_awv_fiets_vast_2024",
        "awv",
        2024,
        162000000,
        "outturn",
        "src_awv_op_2025",
        "strong",
        "Fiets vastlegging 2024 162m",
    ),
    (
        "bud_awv_onderhoud_wegen_delta_2025",
        "awv",
        2025,
        18000000,
        "budgeted",
        "src_awv_op_2025",
        "strong",
        "Extra 18m jaarlijks onderhoudsbudget wegen 2025 vs prior",
    ),
    (
        "bud_awv_onderhoud_em_delta_2025",
        "awv",
        2025,
        12000000,
        "budgeted",
        "src_awv_op_2025",
        "strong",
        "Extra 12m jaarlijks onderhoud EM installaties 2025",
    ),
    (
        "bud_awv_gronden_verkoop_2024",
        "awv",
        2024,
        6001540,
        "outturn",
        "src_awv_op_2025",
        "strong",
        "Inkomsten verkoop 56 AWV-gronden 6.001540m 2024",
    ),
    (
        "bud_sofico_produits_2024",
        "sofico",
        2024,
        495100000,
        "outturn",
        "src_sofico_ra_2024",
        "strong",
        "Produits exploitation 495.1m 2024 (+6.3pct vs 465.7m)",
    ),
    (
        "bud_sofico_charges_2024",
        "sofico",
        2024,
        397600000,
        "outturn",
        "src_sofico_ra_2024",
        "strong",
        "Charges exploitation 397.6m 2024",
    ),
    (
        "bud_sofico_net_2024",
        "sofico",
        2024,
        100700000,
        "outturn",
        "src_sofico_ra_2024",
        "strong",
        "Resultat net 100.7m 2024 (was 97.8m)",
    ),
    (
        "bud_sofico_invest_2024",
        "sofico",
        2024,
        265000000,
        "outturn",
        "src_sofico_ra_2024",
        "strong",
        "Investissements record 265m 2024 (was 225.3m)",
    ),
    (
        "bud_sofico_pkpl_2024",
        "sofico",
        2024,
        347000000,
        "outturn",
        "src_sofico_ra_2024",
        "strong",
        "Recettes PKPL poids lourds 347m 2024 (+11.2pct); primary user-fee stream",
    ),
    (
        "bud_sofico_reseau_2024",
        "sofico",
        2024,
        370800000,
        "outturn",
        "src_sofico_ra_2024",
        "strong",
        "Invest grands axes reseau 370.8m 2024; cum ~3.7bn since 2010 SPW MI collab",
    ),
    (
        "bud_sofico_entretien_rehab_2024",
        "sofico",
        2024,
        371000000,
        "outturn",
        "src_sofico_ra_2024",
        "strong",
        "Entretien ~161m + invest rehab >210m ~371m class 2024 on structuring network",
    ),
    (
        "bud_roads_dual_awv_sofico_2024",
        "awv",
        2024,
        1682141379,
        "outturn",
        "src_awv_op_2025",
        "medium",
        "Illustrative dual 2024: AWV VEK 1.187bn + SOFICO invest 0.265bn + PKPL fee stream separate; not additive TE; different perimeter opex/invest",
    ),
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        note = b[7].replace('"', "'")
        f.write(f'{b[0]},{b[1]},{b[2]},{b[3]},,,{b[4]},{b[5]},{b[6]},"{note}"\n')

# --- commitments ---
cmt_json = (
    '{"awv_vak_2024":1020737569,"awv_vek_2024":1187041379,'
    '"awv_struct_onderhoud_2025":138500000,"awv_fiets_2025_min":158000000,'
    '"sofico_produits_2024":495100000,"sofico_net_2024":100700000,'
    '"sofico_invest_2024":265000000,"sofico_pkpl_2024":347000000,'
    '"sofico_reseau_2024":370800000,"sofico_cum_since_2010_bn":3.7,'
    '"note":"Dual regional roads: AWV agency budget vs SOFICO fee-financed UAP; PKPL user fee not tax; AWV opex full matrix residual"}'
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_awv_sofico_dual_roads_2024_25,"
        "AWV Flanders + SOFICO Wallonia dual roads infrastructure 2024-25,"
        "awv,"
        "Road users Flanders Wallonia motorways regional roads,"
        "Regional roads competence AWV decree / SOFICO decree Wallonia,"
        "2024-01-01,2024,2025,1682141379,"
        f'"{cmt_json}",'
        ",active,https://wegenenverkeer.be/sites/default/files/uploads/documenten/Ondernemingsplan%20AWV%202025.pdf,"
        "Maintain rehabilitate regional road networks dual entities,"
        "Publish AWV full opex matrix; dual unit-cost km; SOFICO L5 top works,"
        "src_awv_op_2025,strong,BE>dual>Roads_AWV_SOFICO,"
        "tick348: AWV VAK/VEK 1.02/1.19bn dual SOFICO 495m rev 265m invest\n"
    )

# --- leaderboard ---
lbs = [
    [
        "lb_awv_vek_1p19bn",
        "AWV Flanders roads VEK 1.19bn 2024 dual SOFICO",
        "regional",
        "programme",
        "Vlaanderen>MOW>AWV",
        "1187041379",
        "1187041379",
        "Strong OP2025: VEK 1.187bn 96.5pct; VAK 1.021bn; struct onderh 138.5m 2025; dual SOFICO fee model",
        "strong",
        "src_awv_op_2025",
        "Flemish road users ~7000km network",
        "Maintain operate regional and motorway network Flanders",
        "Core infrastructure not pure waste; dual Walloon SOFICO different financing (PKPL fees)",
        "2",
        "8.5",
        "5",
        "5.6",
        "Publish full opex L5; dual unit-cost vs SOFICO per km",
        "seed",
        "",
        "tick348 dual roads",
    ],
    [
        "lb_sofico_pkpl_347m",
        "SOFICO PKPL truck toll revenue 347m 2024 dual AWV",
        "regional",
        "user_fee",
        "Wallonie>SOFICO>PKPL",
        "347000000",
        "347000000",
        "Strong RA2024: PKPL 347m of 495.1m produits; invest 265m net 100.7m; dual AWV tax-budget model",
        "strong",
        "src_sofico_ra_2024",
        "Heavy goods vehicles Wallonia structuring network",
        "User-fee finance motorway maintenance investment",
        "Fee not subsidy; dual financing model vs Flanders tax budget; transparency high RA",
        "2",
        "7.0",
        "3",
        "4.4",
        "Track multi-year PKPL path; dual compare AWV funding mix",
        "seed",
        "",
        "tick348 dual roads",
    ],
    [
        "lb_roads_dual_awv_sofico",
        "Dual regional roads AWV+SOFICO class ~1.5bn+ 2024",
        "regional",
        "programme",
        "BE>dual>Roads_infra",
        "1500000000",
        "1500000000",
        "Medium dual class: AWV VEK 1.19bn + SOFICO invest 0.27bn (+ PKPL 0.35bn fee stream separate); not additive",
        "medium",
        "src_awv_op_2025",
        "Two regional road systems",
        "Classic dual regional infrastructure competence",
        "Dual financing models tax vs toll; both large; L5 works residual",
        "4",
        "8.0",
        "5",
        "6.2",
        "Map full dual TCO + federal motorways residual if any; FOI L5 works",
        "seed",
        "",
        "tick348 dual structure",
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
    if r["task_id"] == "rq_339":
        r["status"] = "done"
        r["blocked_gap_id"] = "gap_awv_sofico_l5"
        r["updated_utc"] = now
        r["notes"] = (
            "tick348: AWV VAK 1.021bn VEK 1.187bn 2024 dual SOFICO rev 495m invest 265m PKPL 347m; "
            "FOI L5; spawn rq_340"
        )

rows.append(
    {
        "task_id": "rq_340",
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
        "notes": "Spawned tick348 after AWV+SOFICO dual roads; rq_116 SWA deferred; progress@350 in 2 ticks",
    }
)
with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

# --- foi_queue ---
with open(base / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_awv_sofico_l5,BE>dual>Roads>AWV_SOFICO_L5,awv,"
        "AWV full opex matrix 2023-2026 (personnel werken goederen toelagen) beyond VAK/VEK totals; "
        "named top20 AWV and SOFICO works contracts EUR; SOFICO balance sheet equity assets multi-year;"
        " reconcile GIP invest lines with OP VAK/VEK,"
        "Agency totals strong 2024; L5 works and AWV opex split residual; dual financing model,"
        "5,AWV / SOFICO / Team Openbaarheid Vlaanderen / SPW,"
        "openbaarheid@vlaanderen.be; info@sofico.org,"
        "Koning Albert II-laan 20 1000 Brussel; SOFICO Liege,"
        "docs/doge/foi/drafts/gap_awv_sofico_l5.md,"
        "ready,2026-07-31,,,,,cmt_awv_sofico_dual_roads_2024_25,"
        "lb_awv_vek_1p19bn|lb_sofico_pkpl_347m|lb_roads_dual_awv_sofico,"
        "2026-07-31T12:45:00Z,2026-07-31T12:45:00Z,"
        "tick348 public OP+RA fill; residual L5 human send\n"
    )

# --- loop_state ---
with open(base / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    f.write(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    )
    f.write(
        f"main,continuous,hole_fill,{now},{unit},348,no,"
        "Scheduler 60s. Next prio5 rq_340; rq_116 SWA deferred. FOI ready. "
        "tick348 AWV+SOFICO dual roads. progress@350 in 2 ticks.\n"
    )

print("CSV updates OK")

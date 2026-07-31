# tick 241 ONE FWB dual Opgroeien from FWB budget DO19
import csv, os, json

base = r"C:\Users\karel\dev\AIpolitics\docs\doge\data"
src = "src_fwb_budget_do19_one_2026"
url = "https://budget-finances.cfwb.be/fileadmin/sites/dgbf/uploads/documents/budget_comptabilite/ressources/budgets/2026/"
# primary is FWB dep budget PDF already in raw
utc = "2026-07-29T07:30:00Z"

# kEUR from table Initial 2026
one_total_2026 = 760837000  # programme 1 CELL eng=liq
one_total_2025 = 711833000
dot_main = 604028000
dot_it = 35318000
dot_reform = 27685000
dot_places = 5014000
dot_accueillantes = 20817000
dot_emploi = 49435000
dot_rythmes = 1600000
dot_nouvelles = 15140000
prov_bareme = 1800000
do19_total = 760977000  # with politique accueil 140k

# prior partial lines (cross-check)
struct_correct = 43000000
nonindex_save = 7840000
it_cut = 3000000  # IT path -3m vs prior; 2026 still 35.3m

with open(os.path.join(base, "sources.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            src,
            "FWB budget initial 2026 DO19 Enfance programme ONE (table eng=liq)",
            "docs/doge/data/raw/fwb_budget_dep_2026.pdf",
            "Federation Wallonie-Bruxelles Budget",
            "2026-07-29",
            "budget_decree",
            "ONE prog1 total 760.837m 2026 (711.833m 2025); main dot 604.028m; IT 35.318m; dual Opgroeien VL; tick241",
        ]
    )

with open(os.path.join(base, "entities.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "one_fwb",
            "Office de la Naissance et de l Enfance ONE",
            "Office de la Naissance et de l Enfance ONE",
            "FWB Birth and Childhood Office",
            "parastatal",
            "fwb_gov",
            "fr",
            "https://www.one.be",
            "",
            "",
            "OIP FWB; FWB dots total 760.8m 2026; dual Opgroeien VL childcare family; tick241",
        ]
    )

rows_b = [
    ("bud_one_fwb_total_2026", "one_fwb", 2026, one_total_2026, "", "", "budgeted", src, "strong", "DO19 prog1 ONE total CELL eng=liq 760.837m BI2026"),
    ("bud_one_fwb_total_2025", "one_fwb", 2025, one_total_2025, "", "", "budgeted", src, "strong", "DO19 prog1 ONE total 711.833m BI2025 initial for compare"),
    ("bud_one_fwb_dot_main_2026", "one_fwb", 2026, dot_main, "", "", "budgeted", src, "strong", "Dotation generale ONE 604.028m (was 552.942m 2025)"),
    ("bud_one_fwb_dot_it_2026", "one_fwb", 2026, dot_it, "", "", "budgeted", src, "strong", "Dotation informatique 35.318m (was 37.715m; -3m class path)"),
    ("bud_one_fwb_dot_reform_2026", "one_fwb", 2026, dot_reform, "", "", "budgeted", src, "strong", "Reforme milieux d accueil 27.685m"),
    ("bud_one_fwb_dot_places_2026", "one_fwb", 2026, dot_places, "", "", "budgeted", src, "strong", "Creation de places 5.014m"),
    ("bud_one_fwb_dot_accueillantes_2026", "one_fwb", 2026, dot_accueillantes, "", "", "budgeted", src, "strong", "Accueillantes conventionnees statut 20.817m"),
    ("bud_one_fwb_dot_emploi_2026", "one_fwb", 2026, dot_emploi, "", "", "budgeted", src, "strong", "Soutien politiques emploi enfance 49.435m"),
    ("bud_one_fwb_dot_nouvelles_2026", "one_fwb", 2026, dot_nouvelles, "", "", "budgeted", src, "strong", "Politiques nouvelles 15.140m"),
    ("bud_one_fwb_do19_2026", "fwb_gov", 2026, do19_total, "", "", "budgeted", src, "strong", "DO19 Enfance total eng 760.977m (ONE + politique accueil 0.14m)"),
]
with open(os.path.join(base, "budgets.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for row in rows_b:
        w.writerow(list(row))

cash = json.dumps(
    {
        "total_2026": one_total_2026,
        "total_2025": one_total_2025,
        "delta_yoy": one_total_2026 - one_total_2025,
        "dot_main": dot_main,
        "dot_it": dot_it,
        "dot_reform": dot_reform,
        "dot_places": dot_places,
        "dot_accueillantes": dot_accueillantes,
        "dot_emploi": dot_emploi,
        "dot_nouvelles": dot_nouvelles,
        "prov_bareme": prov_bareme,
        "struct_correct_path": struct_correct,
        "dual_opgroeien_vek": 7611411000,
        "note": "Strong FWB table; dual VL Opgroeien different perimeter (incl Groeipakket); operator L5 residual",
    }
)

with open(os.path.join(base, "commitments.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "cmt_one_fwb_2026",
            "ONE FWB childhood office package 2026 dual Opgroeien",
            "one_fwb",
            "Children families FR community creches accueillantes",
            "FWB budget initial 2026 DO19 prog1",
            "2025-10-10",
            "2026",
            "2026",
            one_total_2026,
            cash,
            0,
            "active",
            "docs/doge/data/raw/fwb_budget_dep_2026.pdf",
            "Birth childhood daycare FWB",
            "Publish operator L5 subsidies; dual unit-cost Opgroeien kinderopvang",
            src,
            "strong",
            "FWB>Enfance>ONE",
            "tick241 dual Opgroeien VL",
        ]
    )

with open(os.path.join(base, "leaderboard.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "lb_one_fwb_761m",
            "ONE FWB childhood dots 760.8m 2026",
            "FWB",
            "ops",
            "FWB>ONE",
            one_total_2026,
            one_total_2026,
            "Strong DO19: 760.837m eng=liq (+49m vs 711.8m 2025); main 604m IT 35.3m; dual Opgroeien VL",
            "strong",
            src,
            "Children FR community",
            "Birth childhood daycare agency FWB",
            "Core social duty not pure waste; dual VL Opgroeien; operator L5 residual",
            3,
            8.0,
            4,
            5.8,
            "Open creche operator L5; dual unit-cost vs Opgroeien",
            "seed",
            "",
            "tick241",
        ]
    )
    w.writerow(
        [
            "lb_childhood_dual_one_opgroeien",
            "Childhood dual ONE 0.76bn vs Opgroeien 7.61bn",
            "Belgium",
            "ops",
            "BE>Childhood>dual_FWB_VL",
            0,
            0,
            "Strong dual: FWB ONE 760.8m 2026 vs VL Opgroeien regie 7.61bn (incl Groeipakket AF); different perimeters do not sum",
            "strong",
            src,
            "Children BE",
            "Community dual early childhood systems",
            "Institutional dual mechanism; AF and daycare nested differently",
            4,
            8.5,
            5,
            6.35,
            "Map dual daycare unit-cost same service class",
            "seed",
            "",
            "tick241 dual not additive",
        ]
    )

gap_id = "gap_one_operator_l5"
with open(os.path.join(base, "foi_queue.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            gap_id,
            "FWB>ONE>subsidies_operators_L5",
            "one_fwb",
            "Top creche/milieux d accueil operators with EUR 2024-2026; split inside 604m main + 550m-class subsidies; institutional RA outturn vs FWB dots 760.8m",
            "FWB dots strong; end-receiver L5 and dual unit-cost Opgroeien residual",
            6,
            "ONE / FWB publicite administration",
            "",
            "https://www.one.be",
            f"docs/doge/foi/drafts/{gap_id}.md",
            "ready",
            "2026-07-29",
            "",
            "",
            "",
            "",
            "cmt_one_fwb_2026",
            "lb_one_fwb_761m",
            utc,
            utc,
            "tick241 draft ready human send",
        ]
    )

rows = []
with open(os.path.join(base, "research_queue.csv"), encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_232":
            row["status"] = "done"
            row["updated_utc"] = utc
            row["blocked_gap_id"] = gap_id
            row["notes"] = (
                "tick241: ONE FWB DO19 760.8m main 604m IT 35.3m dual Opgroeien; FOI operator L5 ready; spawn rq_233"
            )
        rows.append(row)

rows.append(
    {
        "task_id": "rq_233",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Prefer public primary fills (Mons ASBL L5 if public; FPS taxex utilities SOE; "
            "Kind en Gezin residual within Opgroeien; other large FOI-adjacent) if new PDFs appear."
        ),
        "blocked_gap_id": "",
        "created_utc": utc,
        "updated_utc": "",
        "notes": "Spawned tick241 after ONE 761m dual Opgroeien; rq_116 SWA deferred",
    }
)

with open(os.path.join(base, "research_queue.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

with open(os.path.join(base, "loop_state.csv"), "w", encoding="utf-8", newline="") as f:
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
            "hole_fill",
            utc,
            "rq_232",
            241,
            "no",
            "Scheduler 60s. Next prio5 rq_233; rq_116 SWA deferred. FOI ready human send. tick241 ONE FWB 760.8m dual Opgroeien.",
        ]
    )

print("tick241 OK one", one_total_2026)

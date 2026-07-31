# tick 242 FWB Aide a la Jeunesse DO17 dual VL jeugdhulp
import csv, os, json

base = r"C:\Users\karel\dev\AIpolitics\docs\doge\data"
src = "src_fwb_budget_do17_aj_2026"
utc = "2026-07-29T08:00:00Z"

# DO17 totals EUR from table
do17_eng_2026 = 470531000
do17_liq_2026 = 470617000
do17_eng_2025 = 466157000
do17_liq_2025 = 466953000
prog1 = 464865000  # eng=liq
prog0_eng = 5666000
prog0_liq = 5752000
cell = 463925000
fbm = 6606000

# L5 named 2026 eng=liq
res_educ = 264094000
accomp = 63112000
amo = 41338000
accueil_fam_svc = 29961000
accueil_fam_solo = 7825000
restor = 7964000
nouvelles = 8229000
mena = 6614000
nonmarch = 4850000
internats = 3232000
maisons_ado = 2999000
formation = 2749000
ecoute = 224000
prev_spec = 643000
adoption_subs = 1079000
parrainage = 1407000
accrochage = 1741000
mirabel = 369000

l5_sum = (
    res_educ + accomp + amo + accueil_fam_svc + accueil_fam_solo + restor
    + nouvelles + mena + nonmarch + internats + maisons_ado + formation
    + ecoute + prev_spec + adoption_subs + parrainage + accrochage + mirabel
)

with open(os.path.join(base, "sources.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            src,
            "FWB budget initial 2026 DO17 Aide a la Jeunesse table eng/liq",
            "docs/doge/data/raw/fwb_budget_dep_2026.pdf",
            "Federation Wallonie-Bruxelles Budget",
            "2026-07-29",
            "budget_decree",
            "DO17 eng 470.531m liq 470.617m; residentiels 264.1m; accomp 63.1m AMO 41.3m; dual VL jeugdhulp; tick242",
        ]
    )

with open(os.path.join(base, "entities.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "fwb_aide_jeunesse",
            "FWB Aide a la Jeunesse AG",
            "Administration generale de l Aide a la Jeunesse FWB",
            "FWB Youth Aid and Protection administration",
            "agency",
            "fwb_gov",
            "fr",
            "https://www.aidealajeunesse.cfwb.be",
            "",
            "",
            "DO17 total ~470.6m 2026; dual VL jeugdhulp Opgroeien/Justitie; tick242",
        ]
    )

rows_b = [
    ("bud_fwb_do17_eng_2026", "fwb_aide_jeunesse", 2026, do17_eng_2026, "", "", "budgeted", src, "strong", "DO17 total eng 470.531m BI2026"),
    ("bud_fwb_do17_liq_2026", "fwb_aide_jeunesse", 2026, do17_liq_2026, "", "", "budgeted", src, "strong", "DO17 total liq 470.617m BI2026"),
    ("bud_fwb_do17_eng_2025", "fwb_aide_jeunesse", 2025, do17_eng_2025, "", "", "budgeted", src, "strong", "DO17 eng 466.157m BI2025 compare"),
    ("bud_fwb_aj_prog1_2026", "fwb_aide_jeunesse", 2026, prog1, "", "", "budgeted", src, "strong", "Prog1 jeunes en danger/delinquants 464.865m eng=liq"),
    ("bud_fwb_aj_resid_2026", "fwb_aide_jeunesse", 2026, res_educ, "", "", "budgeted", src, "strong", "Subs services residentiels + projet educatif particulier 264.094m ~56pct DO17"),
    ("bud_fwb_aj_accomp_2026", "fwb_aide_jeunesse", 2026, accomp, "", "", "budgeted", src, "strong", "Subs services d accompagnement 63.112m"),
    ("bud_fwb_aj_amo_2026", "fwb_aide_jeunesse", 2026, amo, "", "", "budgeted", src, "strong", "Subs services actions milieu ouvert AMO 41.338m"),
    ("bud_fwb_aj_accueil_fam_2026", "fwb_aide_jeunesse", 2026, accueil_fam_svc + accueil_fam_solo, "", "", "budgeted", src, "strong", "Accueil familial: services 29.961 + accueillants 7.825 = 37.786m"),
    ("bud_fwb_aj_restor_2026", "fwb_aide_jeunesse", 2026, restor, "", "", "budgeted", src, "strong", "Services actions restauratrices educatives 7.964m"),
    ("bud_fwb_aj_mena_2026", "fwb_aide_jeunesse", 2026, mena, "", "", "budgeted", src, "strong", "Plan MENA new line 6.614m 2026"),
    ("bud_fwb_aj_nouvelles_2026", "fwb_aide_jeunesse", 2026, nouvelles, "", "", "budgeted", src, "strong", "Nouvelles politiques AJ 8.229m"),
    ("bud_fwb_aj_maisons_ado_2026", "fwb_aide_jeunesse", 2026, maisons_ado, "", "", "budgeted", src, "strong", "Maisons de l adolescent 2.999m"),
    ("bud_fwb_aj_l5_sample_sum_2026", "fwb_aide_jeunesse", 2026, l5_sum, "", "", "budgeted", src, "strong", f"Named L5 sample sum {l5_sum} of DO17 ~470.6m (~{100*l5_sum/do17_liq_2026:.0f}pct)"),
]
with open(os.path.join(base, "budgets.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for row in rows_b:
        w.writerow(list(row))

cash = json.dumps(
    {
        "do17_eng": do17_eng_2026,
        "do17_liq": do17_liq_2026,
        "prog1": prog1,
        "resid_educ": res_educ,
        "accomp": accomp,
        "amo": amo,
        "accueil_fam_package": accueil_fam_svc + accueil_fam_solo,
        "mena": mena,
        "l5_sample_sum": l5_sum,
        "dual_vl": "Opgroeien jeugdhulp + transfer Justitie Handhaving 2026",
        "note": "Strong FWB table; dual VL youth care; operator name-list residual FOI",
    }
)

with open(os.path.join(base, "commitments.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "cmt_fwb_aide_jeunesse_2026",
            "FWB Aide a la Jeunesse DO17 package 2026 dual VL",
            "fwb_aide_jeunesse",
            "Youth in danger/delinquency FR community services",
            "FWB budget initial 2026 DO17",
            "2025-10-10",
            "2026",
            "2026",
            do17_liq_2026,
            cash,
            0,
            "active",
            "docs/doge/data/raw/fwb_budget_dep_2026.pdf",
            "Youth aid protection FWB",
            "Publish named operator L5 inside resid 264m; dual unit-cost VL jeugdhulp",
            src,
            "strong",
            "FWB>Aide_Jeunesse",
            "tick242 dual Opgroeien/Justitie VL",
        ]
    )

with open(os.path.join(base, "leaderboard.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "lb_fwb_aj_471m",
            "FWB Aide a la Jeunesse DO17 470.6m 2026",
            "FWB",
            "ops",
            "FWB>Aide_Jeunesse",
            do17_liq_2026,
            do17_liq_2026,
            "Strong DO17 liq 470.6m; residentiels 264.1m 56pct; dual VL jeugdhulp",
            "strong",
            src,
            "Youth in danger FR community",
            "Youth aid protection",
            "Core social duty not pure waste; dual VL; operator L5 residual",
            3,
            7.5,
            4,
            5.55,
            "Open named operator matrix resid 264m; dual VL unit-cost",
            "seed",
            "",
            "tick242",
        ]
    )
    w.writerow(
        [
            "lb_fwb_aj_resid_264m",
            "FWB AJ residential services 264.1m 2026",
            "FWB",
            "ops",
            "FWB>Aide_Jeunesse>residentiel",
            res_educ,
            res_educ,
            "Strong line 33.28: services residentiels + projet educatif particulier 264.094m",
            "strong",
            src,
            "Youth in residential care",
            "Residential youth protection services",
            "Core care; largest AJ line; L5 service names residual",
            3,
            7.5,
            4,
            5.55,
            "Publish top services with EUR",
            "seed",
            "",
            "tick242",
        ]
    )
    w.writerow(
        [
            "lb_youth_care_dual_fwb_vl",
            "Youth care dual FWB AJ 0.47bn vs VL Opgroeien/Justitie",
            "Belgium",
            "ops",
            "BE>Youth_care>dual_FWB_VL",
            0,
            0,
            "Strong dual: FWB AJ DO17 470.6m 2026 vs VL youth care inside Opgroeien + 2026 transfer Justitie Handhaving; do not sum",
            "strong",
            src,
            "Youth BE",
            "Community dual youth protection systems",
            "Institutional dual + VL agency split 2026",
            4,
            7.5,
            5,
            5.85,
            "Map dual unit-cost same service class",
            "seed",
            "",
            "tick242 dual not additive",
        ]
    )

gap_id = "gap_fwb_aj_operator_l5"
with open(os.path.join(base, "foi_queue.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            gap_id,
            "FWB>Aide_Jeunesse>operators_L5",
            "fwb_aide_jeunesse",
            "Named top residential/AMO/accompagnement services with EUR 2024-2026 inside 264m/63m/41m lines; dual VL youth care perimeter",
            "Category totals strong DO17; end-receiver names residual",
            6,
            "FWB Administration generale Aide a la Jeunesse / publicite",
            "",
            "https://www.aidealajeunesse.cfwb.be",
            f"docs/doge/foi/drafts/{gap_id}.md",
            "ready",
            "2026-07-29",
            "",
            "",
            "",
            "",
            "cmt_fwb_aide_jeunesse_2026",
            "lb_fwb_aj_resid_264m|lb_fwb_aj_471m",
            utc,
            utc,
            "tick242 draft ready human send",
        ]
    )

rows = []
with open(os.path.join(base, "research_queue.csv"), encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_233":
            row["status"] = "done"
            row["updated_utc"] = utc
            row["blocked_gap_id"] = gap_id
            row["notes"] = (
                "tick242: FWB AJ DO17 470.6m resid 264.1m AMO 41.3m accomp 63.1m dual VL; FOI operator L5 ready; spawn rq_234"
            )
        rows.append(row)

rows.append(
    {
        "task_id": "rq_234",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Prefer public primary fills (Mons ASBL L5 if public; FPS taxex utilities SOE; "
            "VL jeugdhulp Justitie transfer residual; Maisons de Justice deepen; other FOI-adjacent)."
        ),
        "blocked_gap_id": "",
        "created_utc": utc,
        "updated_utc": "",
        "notes": "Spawned tick242 after FWB AJ 471m dual VL; rq_116 SWA deferred",
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
            "rq_233",
            242,
            "no",
            "Scheduler 60s. Next prio5 rq_234; rq_116 SWA deferred. FOI ready human send. tick242 FWB AJ 470.6m resid 264m dual VL.",
        ]
    )

print("tick242 OK do17", do17_liq_2026, "l5sum", l5_sum)

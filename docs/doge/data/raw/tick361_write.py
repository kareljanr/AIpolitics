# tick 361 — dual adult formal education FWB DO56 + VL volwassenenonderwijs residual
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def append_csv(rel, rows):
    p = ROOT / rel
    text = p.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    for row in rows:
        text += row + "\n"
    p.write_text(text, encoding="utf-8", newline="\n")
    print(f"appended {len(rows)} -> {rel}")


append_csv(
    "docs/doge/data/entities.csv",
    [
        "fwb_enseignement_adultes,FWB Enseignement pour adultes DO56,Enseignement pour adultes FWB,FWB adult formal education dual Flanders CVO volwassenenonderwijs,agency,fwb_gov,fr,https://www.enseignement.be,,,DO56 CE=CL 267.547m 2026 personnel 251.7m; dual VL VO residual FOI; tick361",
        "fwb_enseignement_artistique,FWB Enseignement artistique DO57,Enseignement artistique FWB,FWB artistic education higher + part-time dual VL DKO,agency,fwb_gov,fr,https://www.enseignement.be,,,DO57 horaire reduit 142.473m + ESA superieur 119.128m 2026; dual VL DKO residual; tick361",
        "vl_volwassenenonderwijs,Vlaams volwassenenonderwijs CVO,Enseignement pour adultes Flandre,Flanders adult education CVO dual FWB DO56,agency,vlaanderen_gov,nl,https://onderwijs.vlaanderen.be,openbaarheid@vlaanderen.be,,BBT Onderwijs dual FWB DO56; absolute ISE residual FOI; DKO+VO class +44.2m 4.7pct commissie; tick361",
    ],
)

append_csv(
    "docs/doge/data/sources.csv",
    [
        "src_fwb_exp_part_dep_2026_epa,FWB Budget 2026 Expose particulier DO56 Enseignement pour adultes DO57 artistique DO58 distance,https://budget-finances.cfwb.be/budget-et-comptabilite/budgets-en-ligne/,Federation Wallonie-Bruxelles / Budget,2026-07-31,official_budget,Strong: DO56 CE=CL 267.547m 2026 (2025 261.751) personnel 251.737 fonct 9.132; DO57 horaire reduit 142.473m ESA superieur 119.128m; DO58 distance 2.372m; dual VL; tick361",
        "src_vl_commissie_onderwijs_2026,Commissieverslag Onderwijs uitgavenbegroting 2026 15-7-H,https://docs.vlaamsparlement.be/pfile?id=2246988,Vlaams Parlement / Commissie Onderwijs,2026-07-31,official_parliament,Strong domain: Onderwijs total VEK 17.24bn VAK 17.25bn 2026; DKO+VO +44.2m +4.7pct; VO alone +5.5pct; absolute VO/DKO ISE residual FOI dual FWB; tick361",
    ],
)

append_csv(
    "docs/doge/data/budgets.csv",
    [
        "bud_fwb_epa_do56_2026,fwb_enseignement_adultes,2026,267547000,,,budgeted,src_fwb_exp_part_dep_2026_epa,strong,DO56 Enseignement pour adultes CE=CL 267.547m 2026",
        "bud_fwb_epa_do56_2025,fwb_enseignement_adultes,2025,261751000,,,budgeted,src_fwb_exp_part_dep_2026_epa,strong,DO56 CE=CL 261.751m 2025",
        "bud_fwb_epa_personnel_2026,fwb_enseignement_adultes,2026,251737000,,,budgeted,src_fwb_exp_part_dep_2026_epa,strong,DO56 prog4 personnel 251.737m 2026 (~94pct)",
        "bud_fwb_epa_fonctionnement_2026,fwb_enseignement_adultes,2026,9132000,,,budgeted,src_fwb_exp_part_dep_2026_epa,strong,DO56 prog5 fonctionnement ecoles 9.132m",
        "bud_fwb_epa_initiatives_emploi_2026,fwb_enseignement_adultes,2026,2372000,,,budgeted,src_fwb_exp_part_dep_2026_epa,strong,DO56 prog6 initiatives RW/RBC emploi 2.372m",
        "bud_fwb_epa_transversal_2026,fwb_enseignement_adultes,2026,2368000,,,budgeted,src_fwb_exp_part_dep_2026_epa,strong,DO56 prog8 initiatives transversales 2.368m",
        "bud_fwb_epa_echec_2026,fwb_enseignement_adultes,2026,1830000,,,budgeted,src_fwb_exp_part_dep_2026_epa,strong,DO56 prog7 lutte echec scolaire 1.830m",
        "bud_fwb_ead_do58_2026,fwb_enseignement_adultes,2026,2372000,,,budgeted,src_fwb_exp_part_dep_2026_epa,strong,DO58 Enseignement a distance CE=CL 2.372m 2026",
        "bud_fwb_artistique_horaire_reduit_2026,fwb_enseignement_artistique,2026,142473000,,,budgeted,src_fwb_exp_part_dep_2026_epa,strong,DO57 enseignement a horaire reduit total 142.473m (personnel 136.871 fonct 5.102) dual VL DKO class",
        "bud_fwb_artistique_superieur_2026,fwb_enseignement_artistique,2026,119128000,,,budgeted,src_fwb_exp_part_dep_2026_epa,strong,DO57 etablissements enseignement superieur artistique 119.128m (personnel 98.651 fonct 20.291)",
        "bud_vl_onderwijs_total_vek_2026,vlaanderen_gov,2026,17240000000,,,budgeted,src_vl_commissie_onderwijs_2026,strong,Onderwijs en Vorming total VEK 17.24bn BO2026 (VAK 17.25bn)",
        "bud_vl_onderwijs_total_vak_2026,vlaanderen_gov,2026,17250000000,,,budgeted,src_vl_commissie_onderwijs_2026,strong,Onderwijs en Vorming total VAK 17.25bn BO2026",
        "bud_vl_dko_vo_delta_2026,vl_volwassenenonderwijs,2026,44200000,,,budgeted,src_vl_commissie_onderwijs_2026,strong,DKO+volwassenenonderwijs combined +44.2m (+4.7pct) BO2026 vs BA2025; absolute ISE residual FOI",
        "bud_adult_edu_dual_class_2026,fwb_enseignement_adultes,2026,267547000,,,budgeted,src_fwb_exp_part_dep_2026_epa,medium,Dual floor: FWB DO56 267.5m strong; VL VO absolute residual FOI (DKO+VO class order ~1bn from +4.7pct on 44.2m rise); not TE-additive",
    ],
)

append_csv(
    "docs/doge/data/commitments.csv",
    [
        'cmt_adult_edu_dual_vl_fwb_2026,Dual adult formal education FWB DO56 + Flanders volwassenenonderwijs/CVO 2026,fwb_enseignement_adultes,Adult learners CVO EPA schools,Decret enseignement pour adultes 1991 + VL volwassenenonderwijs financing,2025-10-24,2026,2026,267547000,"{fwb_do56_m:267.547;fwb_personnel_m:251.737;fwb_do58_m:2.372;fwb_horaire_reduit_m:142.473;vl_onderwijs_vek_bn:17.24;vl_dko_vo_delta_m:44.2;note:VL VO absolute ISE residual FOI; dual not TE-additive; excludes SCW 83m and EP 44.6m popular education}",,active,https://www.enseignement.be,Parallel dual community adult formal education,Publish VL VO/DKO ISE split; dual unit cost per learner,src_fwb_exp_part_dep_2026_epa,strong,BE>dual>Adult_formal_education>VL_FWB,tick361: FWB DO56 strong 267.5m; VL absolute FOI; artistic horaire reduit 142.5m dual DKO noted',
    ],
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    [
        "lb_fwb_epa_268m,FWB Enseignement pour adultes DO56 267.5m 2026,regional,programme,FWB>Education>Enseignement_adultes,267547000,267547000,Exp part strong CE=CL 267.547m; personnel 251.7m 94pct; dual VL CVO residual,strong,src_fwb_exp_part_dep_2026_epa,Adult learners FR community,Adult formal education promotion sociale,Core education dual; L5 school network residual,4,7.5,4,5.55,Publish school-level cash dual VL CVO,seed,,tick361",
        "lb_fwb_artistique_horaire_142m,FWB enseignement artistique a horaire reduit 142.5m 2026,regional,programme,FWB>Education>Artistique_horaire_reduit,142473000,142473000,Exp part strong 142.473m personnel 136.9 fonct 5.1; dual VL DKO class,strong,src_fwb_exp_part_dep_2026_epa,Part-time arts academy students,Part-time artistic education dual DKO,Core culture-education dual; VL absolute residual FOI,4,7,4,5.25,Publish dual DKO unit-cost academies,seed,,tick361",
        "lb_fwb_artistique_superieur_119m,FWB enseignement artistique superieur 119.1m 2026,regional,programme,FWB>Education>Artistique_superieur,119128000,119128000,Exp part strong 119.128m ESA higher arts schools; dual VL conservatories class,strong,src_fwb_exp_part_dep_2026_epa,Higher arts students,Higher artistic education,Core higher arts dual; not pure waste,3,7,4,5.0,Dual map VL hogescholen kunsten,seed,,tick361",
        "lb_adult_edu_dual_vl_fwb,Dual adult formal education FWB 268m + VL VO residual,regional,overhead_dual,BE>dual>Adult_formal_education,267547000,267547000,FWB DO56 strong 267.5m floor; VL VO absolute FOI (DKO+VO +44.2m 4.7pct); not TE-additive,medium,src_fwb_exp_part_dep_2026_epa,Parallel adult education stacks,Community dual adult formal education,Classic dual; VL ISE opacity vs FWB,5,7.5,5,6.0,FOI VL VO/DKO ISE; dual learner unit-cost,seed,,tick361",
        "lb_vl_onderwijs_17_2bn,Flanders Onderwijs en Vorming total VEK 17.24bn 2026,regional,programme,Vlaanderen>Onderwijs,17240000000,17240000000,Commissie strong VEK 17.24bn VAK 17.25bn (+2.6pct); dual FWB education large,strong,src_vl_commissie_onderwijs_2026,Pupils students teachers,Community education total domain,Core education not pure waste; L5 residual,2,9.5,5,6.85,L5 by level already partial; dual FWB EPA/DKO,seed,,tick361",
    ],
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    [
        "gap_adult_edu_dual_vl_fwb_l5,BE>dual>Adult_education>VL_FWB_L5,vl_volwassenenonderwijs,VL BO2026 ISE absolute VAK/VEK for volwassenenonderwijs and DKO separately (cash-by-year 2023-2026); top CVO/academies L5 if public; FWB DO56 top schools personnel/fonct split residual; dual unit cost per learner; reconcile DKO+VO +44.2m 4.7pct,FWB DO56 267.5m strong; VL absolute ISE residual; dual DKO/horaire reduit 142.5m,6,Departement Onderwijs en Vorming / Team Openbaarheid / FWB Enseignement,openbaarheid@vlaanderen.be; enseignement.be,Koning Albert II-laan Brussel; FWB Bruxelles,docs/doge/foi/drafts/gap_adult_edu_dual_vl_fwb_l5.md,ready,2026-07-31,,,,,cmt_adult_edu_dual_vl_fwb_2026,lb_fwb_epa_268m|lb_adult_edu_dual_vl_fwb|lb_fwb_artistique_horaire_142m,2026-07-31T19:15:00Z,2026-07-31T19:15:00Z,tick361 public FWB DO56/57 + VL commissie domain; residual VL ISE human send",
    ],
)

rq_path = ROOT / "docs/doge/data/research_queue.csv"
lines = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_352,"):
        out.append(
            "rq_352,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_adult_edu_dual_vl_fwb_l5,2026-07-31T18:45:00Z,2026-07-31T19:15:00Z,tick361: FWB EPA DO56 267.5m + artistique horaire 142.5m dual VL VO/DKO residual FOI; spawn rq_353"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_353,") for l in out):
    out.append(
        "rq_353,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-07-31T19:15:00Z,,Spawned tick361 after adult education dual FWB/VL; rq_116 SWA deferred"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")

(ROOT / "docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-31T19:15:00Z,rq_352,361,no,Scheduler 60s. Next prio5 rq_353; rq_116 SWA deferred. FOI ready. tick361 adult education dual FWB/VL.\n",
    encoding="utf-8",
    newline="\n",
)
print("tick361 write complete")

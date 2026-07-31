# -*- coding: utf-8 -*-
"""Tick 165: FWB university per-institution allocations BI2026 (DO54)."""
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
TS = "2026-07-28T05:05:00Z"
TICK = 165
UNIT = "rq_160"


def append_lines(path: Path, lines: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def replace_line_startswith(path: Path, prefix: str, new_line: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out = []
    found = False
    for line in lines:
        if line.startswith(prefix):
            out.append(new_line if new_line.endswith("\n") else new_line + "\n")
            found = True
        else:
            out.append(line)
    if not found:
        raise SystemExit(f"prefix not found: {prefix}")
    path.write_text("".join(out), encoding="utf-8", newline="\n")


# amounts from Budget des dépenses 2026 Initial: en milliers d'euros eng=liq
# convert kEUR * 1000

unis_2025 = {
    "uliege": 241118000,
    "umons": 84931000,
    "uclouvain": 318821000,
    "ulb": 264900000,
    "unamur": 69042000,
}
unis_2026 = {
    "uliege": 249252000,
    "umons": 89797000,
    "uclouvain": 330911000,
    "ulb": 275862000,
    "unamur": 72197000,
}
sum_2025 = sum(unis_2025.values())  # 978812000
sum_2026 = sum(unis_2026.values())  # 1018019000
do54_2026 = 1153192000
do54_celnl = 1471000  # control residual
prog1_2026 = 360972000  # community unis package
prog2_2026 = 718808000  # free unis package
social_comm_2026 = 12199000
social_libres_2026 = 28276000
minerval_comp_2026 = 52422000
minerval_comp_2025 = 56466000
aides_reussite_2026 = 14904000
he_cf_2026 = 122543000
he_social_2026 = 41280000
chu_charges_2026 = 8924000
chu_capital_2025 = 2785000  # cut to 0 in 2026
art34_2026 = 11410000

append_lines(
    DATA / "sources.csv",
    [
        "src_fwb_budget_dep_2026,FWB Budget des depenses 2026 Initial DO54 university AB lines,"
        "https://budget-finances.cfwb.be/fileadmin/sites/dgbf/uploads/documents/budget_comptabilite/ressources/budgets/2026/Budget_des_depenses_2026_-_Initial.pdf,"
        "FWB Budget Parlement,2026-07-28,budget,"
        '"DO54 CELL 1153.192m 2026; alloc fonctionnement UCL 330.9 ULB 275.9 ULiege 249.3 UMons 89.8 UNamur 72.2 (kEUR table*1000); eng=liq; tick165"'
    ],
)

# entities
append_lines(
    DATA / "entities.csv",
    [
        "uliege,Universite de Liege,Université de Liège,University of Liège,university,fwb_gov,fr,https://www.uliege.be,,,FWB community uni; alloc fonct 249.252m 2026 / 241.118m 2025; tick165",
        "umons,Universite de Mons,Université de Mons,University of Mons,university,fwb_gov,fr,https://web.umons.ac.be,,,FWB community uni; alloc fonct 89.797m 2026; tick165",
        "uclouvain,UCLouvain,Université catholique de Louvain,UCLouvain,university,fwb_gov,fr,https://uclouvain.be,,,Largest FWB free uni; alloc fonct 330.911m 2026; Saint-Louis merged 0 line; tick165",
        "ulb,Universite libre de Bruxelles,Université libre de Bruxelles,ULB,university,fwb_gov,fr,https://www.ulb.be,,,FWB free uni; alloc fonct 275.862m 2026; dual capital with VUB; tick165",
        "unamur,Universite de Namur,Université de Namur,University of Namur,university,fwb_gov,fr,https://www.unamur.be,,,FWB free uni; alloc fonct 72.197m 2026; tick165",
    ],
)

bud_rows = [
    f"bud_uliege_alloc_fonct_2025,uliege,2025,{unis_2025['uliege']},,,budgeted,src_fwb_budget_dep_2026,strong,ULiege allocation fonctionnement DO54 AB41.12 2025 eng=liq",
    f"bud_uliege_alloc_fonct_2026,uliege,2026,{unis_2026['uliege']},,,budgeted,src_fwb_budget_dep_2026,strong,ULiege allocation fonctionnement 2026 eng=liq",
    f"bud_umons_alloc_fonct_2025,umons,2025,{unis_2025['umons']},,,budgeted,src_fwb_budget_dep_2026,strong,UMons allocation fonctionnement 2025",
    f"bud_umons_alloc_fonct_2026,umons,2026,{unis_2026['umons']},,,budgeted,src_fwb_budget_dep_2026,strong,UMons allocation fonctionnement 2026",
    f"bud_uclouvain_alloc_fonct_2025,uclouvain,2025,{unis_2025['uclouvain']},,,budgeted,src_fwb_budget_dep_2026,strong,UCLouvain allocation fonctionnement 2025",
    f"bud_uclouvain_alloc_fonct_2026,uclouvain,2026,{unis_2026['uclouvain']},,,budgeted,src_fwb_budget_dep_2026,strong,UCLouvain allocation fonctionnement 2026 largest FWB",
    f"bud_ulb_alloc_fonct_2025,ulb,2025,{unis_2025['ulb']},,,budgeted,src_fwb_budget_dep_2026,strong,ULB allocation fonctionnement 2025",
    f"bud_ulb_alloc_fonct_2026,ulb,2026,{unis_2026['ulb']},,,budgeted,src_fwb_budget_dep_2026,strong,ULB allocation fonctionnement 2026",
    f"bud_unamur_alloc_fonct_2025,unamur,2025,{unis_2025['unamur']},,,budgeted,src_fwb_budget_dep_2026,strong,UNamur allocation fonctionnement 2025",
    f"bud_unamur_alloc_fonct_2026,unamur,2026,{unis_2026['unamur']},,,budgeted,src_fwb_budget_dep_2026,strong,UNamur allocation fonctionnement 2026",
    f"bud_fwb_univ_alloc_sum_2025,fwb_gov,2025,{sum_2025},,,budgeted,src_fwb_budget_dep_2026,strong,Sum 5 FWB unis alloc fonctionnement 2025 978.812m",
    f"bud_fwb_univ_alloc_sum_2026,fwb_gov,2026,{sum_2026},,,budgeted,src_fwb_budget_dep_2026,strong,Sum 5 FWB unis alloc fonctionnement 2026 1018.019m",
    f"bud_fwb_do54_cell_2026,fwb_gov,2026,{do54_2026},,,budgeted,src_fwb_budget_dep_2026,strong,DO54 Enseignement universitaire CELL total 1153.192m 2026",
    f"bud_fwb_do54_prog1_2026,fwb_gov,2026,{prog1_2026},,,budgeted,src_fwb_budget_dep_2026,strong,DO54 Prog1 Universites Communaute 360.972m 2026",
    f"bud_fwb_do54_prog2_2026,fwb_gov,2026,{prog2_2026},,,budgeted,src_fwb_budget_dep_2026,strong,DO54 Prog2 Universites libres 718.808m 2026",
    f"bud_fwb_univ_social_comm_2026,fwb_gov,2026,{social_comm_2026},,,budgeted,src_fwb_budget_dep_2026,strong,Subventions sociales unis Communaute 12.199m 2026",
    f"bud_fwb_univ_social_libres_2026,fwb_gov,2026,{social_libres_2026},,,budgeted,src_fwb_budget_dep_2026,strong,Subventions sociales unis libres 28.276m 2026",
    f"bud_fwb_minerval_comp_2025,fwb_gov,2025,{minerval_comp_2025},,,budgeted,src_fwb_budget_dep_2026,strong,Compensations droits inscription reduits unis 56.466m 2025",
    f"bud_fwb_minerval_comp_2026,fwb_gov,2026,{minerval_comp_2026},,,budgeted,src_fwb_budget_dep_2026,strong,Compensations minerval reduits 52.422m 2026 (cut path)",
    f"bud_fwb_aides_reussite_univ_2026,fwb_gov,2026,{aides_reussite_2026},,,budgeted,src_fwb_budget_dep_2026,strong,Allocations aides a la reussite unis 14.904m 2026",
    f"bud_fwb_art34_univ_libres_2026,fwb_gov,2026,{art34_2026},,,budgeted,src_fwb_budget_dep_2026,strong,Intervention art.34 loi 1971 unis libres 11.410m 2026",
    f"bud_fwb_chu_liege_charges_2026,fwb_gov,2026,{chu_charges_2026},,,budgeted,src_fwb_budget_dep_2026,strong,CHU Liege charges exceptionnelles 8.924m 2026",
    f"bud_fwb_chu_liege_capital_2025,fwb_gov,2025,{chu_capital_2025},,,budgeted,src_fwb_budget_dep_2026,strong,CHU Liege constitution capital 2.785m 2025 cut to 0 in 2026",
    f"bud_fwb_he_cf_alloc_2026,fwb_gov,2026,{he_cf_2026},,,budgeted,src_fwb_budget_dep_2026,strong,Hautes Ecoles Communaute allocations globales 122.543m 2026 DO55",
    f"bud_fwb_he_social_2026,fwb_gov,2026,{he_social_2026},,,budgeted,src_fwb_budget_dep_2026,strong,Subventions sociales Hautes Ecoles 41.280m 2026",
]
append_lines(DATA / "budgets.csv", bud_rows)

append_lines(
    DATA / "commitments.csv",
    [
        'cmt_fwb_univ_alloc_fonct_2025_26,FWB universities allocation de fonctionnement per institution 2025-26,fwb_gov,'
        "ULiege UMons UCLouvain ULB UNamur,Budget depenses DO54 Initial 2025-2026 eng=liq,"
        "2025-01-01,2025,2026,1018019000,"
        '"{""2025_uliege"":241118000,""2025_umons"":84931000,""2025_uclouvain"":318821000,""2025_ulb"":264900000,""2025_unamur"":69042000,'
        '""2025_sum5"":978812000,""2026_uliege"":249252000,""2026_umons"":89797000,""2026_uclouvain"":330911000,""2026_ulb"":275862000,'
        '""2026_unamur"":72197000,""2026_sum5"":1018019000,""2026_do54_cell"":1153192000,""2026_prog1_communaute"":360972000,'
        '""2026_prog2_libres"":718808000,""2026_social_comm"":12199000,""2026_social_libres"":28276000,'
        '""2026_minerval_comp"":52422000,""2025_minerval_comp"":56466000,""2026_aides_reussite"":14904000,'
        '""2026_art34"":11410000,""saint_louis_line"":0,""unit"":""EUR_from_kEUR_table"",""eng_eq_liq"":true}",'
        "0,active,https://budget-finances.cfwb.be/fileadmin/sites/dgbf/uploads/documents/budget_comptabilite/ressources/budgets/2026/Budget_des_depenses_2026_-_Initial.pdf,"
        "FWB basisfinanciering dual with Flanders HE,"
        "Publish multi-year cash; dual community transparency VL vs FWB,"
        "src_fwb_budget_dep_2026,strong,FWB>Enseignement>Universites>L5,"
        "tick165; closes FWB side of gap_univ_per_institution",
    ],
)

append_lines(
    DATA / "leaderboard.csv",
    [
        "lb_fwb_univ_alloc_fonct,FWB 5 universities alloc fonctionnement ~1.02bn 2026,FWB,ops,"
        "FWB>Universites>alloc_fonctionnement,978812000,1018019000,"
        "Budget strong: sum5 978.8m 2025 / 1018.0m 2026; DO54 CELL 1153m; dual VL unis 1.44bn 1st stream,"
        "strong,src_fwb_budget_dep_2026,FWB university students,"
        "Community higher education basisfinanciering,"
        "Core education not waste; dual NL-FR HE stack overhead,"
        "3,9.0,7,5.9,"
        "Benchmark unit cost per student vs VL; open multi-year,"
        "seed,,tick165",
        "lb_uclouvain_alloc,UCLouvain alloc fonctionnement 331m 2026,FWB,ops,"
        "FWB>Universites>UCLouvain,318821000,330911000,"
        "Largest FWB uni operating grant strong budget line; dual KUL 547m VL,"
        "strong,src_fwb_budget_dep_2026,UCLouvain students,"
        "University basisfinanciering,"
        "Core remit,"
        "3,8.5,6,5.4,"
        "Peer unit costs,"
        "seed,,tick165",
        "lb_ulb_alloc,ULB alloc fonctionnement 276m 2026,FWB,ops,"
        "FWB>Universites>ULB,264900000,275862000,"
        "Strong budget; dual capital VUB ~166m medium VL 1st stream,"
        "strong,src_fwb_budget_dep_2026,ULB students,"
        "University basisfinanciering,"
        "Core remit; bilingual capital dual,"
        "3,8.5,6,5.4,"
        "Publish dual BRU HE package ULB+VUB,"
        "seed,,tick165",
        "lb_uliege_alloc,ULiege alloc fonctionnement 249m 2026,FWB,ops,"
        "FWB>Universites>ULiege,241118000,249252000,"
        "Strong; community network uni + CHU package separate,"
        "strong,src_fwb_budget_dep_2026,ULiege students,"
        "University basisfinanciering,"
        "Core remit,"
        "3,8.0,5,5.0,"
        "Track CHU capital cut 2.8m,"
        "seed,,tick165",
    ],
)

# FOI gap_univ update - partial close FWB
replace_line_startswith(
    DATA / "foi_queue.csv",
    "gap_univ_per_institution,",
    "gap_univ_per_institution,BE>Universities>operating_grants_L5,sec_flanders,"
    "AHOVOKS exact cash-by-year werkingsuitkering matrix 2023-2026 for UGent UA VUB UHasselt (KUL strong JV; CRC medium reverse-engineered); residual multi-year only,"
    "FWB DO54 2025-26 per-uni strong tick165 (UCL 331 ULB 276 ULiege 249 UMons 90 UNamur 72); VL residual AHOVOKS exact still,"
    "5,AHOVOKS / Team Openbaarheid,openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,"
    "docs/doge/foi/drafts/gap_univ_per_institution.md,ready,2026-07-27,,,,,"
    "cmt_fwb_univ_alloc_fonct_2025_26|cmt_vl_univ_per_inst_matrix_2024,lb_fwb_univ_alloc_fonct,"
    "2026-07-27T23:15:00Z,2026-07-28T05:05:00Z,"
    "tick149|163 VL partial |tick165 FWB strong L5; residual VL AHOVOKS exact human send\n",
)

replace_line_startswith(
    DATA / "research_queue.csv",
    "rq_160,",
    "rq_160,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    '"Prefer public primary fills (De Lijn 2025-26 full perimeter Antwerp register VIPA Mons BI2026 HR Rail FWB univ dots) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    "gap_univ_per_institution,2026-07-28T04:45:00Z,2026-07-28T05:05:00Z,"
    '"tick165: FWB DO54 Budget 2026 L5 UCL 330.9m ULB 275.9 ULiege 249.3 UMons 89.8 UNamur 72.2 sum 1018m; DO54 1153m; dual VL; spawn rq_161"\n',
)

rq = (DATA / "research_queue.csv").read_text(encoding="utf-8")
if "rq_161," not in rq:
    append_lines(
        DATA / "research_queue.csv",
        [
            "rq_161,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
            '"Prefer public primary fills (De Lijn 2025-26 full perimeter Antwerp register VIPA Mons BI2026 HR Rail) if new PDFs appear; else next open rq; do not idle while public work remains.",'
            ",2026-07-28T05:05:00Z,,"
            '"Spawned tick165 after FWB univ L5; rq_116 SWA deferred Oct-Dec 2026"',
        ],
    )

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},{UNIT},{TICK},no,"
    '"Scheduler 60s. Next prio5 rq_161 hole-fill De Lijn/Antwerp/VIPA/Mons/HR Rail; rq_116 SWA deferred. FOI ready human send. tick165 FWB univ L5."\n',
    encoding="utf-8",
    newline="\n",
)

log = ROOT / "loop_log.md"
entry = f"""
### {TS} — tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill — **FWB universities DO54 BI2026 per-institution L5**)
- Found (strong primary Budget des dépenses 2026, *en milliers d'euros*, eng=liq):
  - **Alloc fonctionnement 2026:** UCLouvain **330.911m** · ULB **275.862m** · ULiège **249.252m** · UMons **89.797m** · UNamur **72.197m** · **sum 1.018bn** (2025 sum **978.8m**).
  - **DO54 CELL total 1.153bn** 2026 (prog1 Communauté **361.0m** · prog2 libres **718.8m** · prog4 **69.8m**).
  - Social unis: Comm **12.2m** · libres **28.3m** · minerval compensations **52.4m** (was 56.5m) · aides réussite **14.9m** · art.34 **11.4m**.
  - CHU Liège capital line **2.785m → 0** 2026 (matches ExpGen savings note).
  - Hautes Écoles CF allocations globales **122.5m** + social HE **41.3m** (DO55 sample).
  - Dual HE: FWB ~1.02bn pure alloc vs VL 1st stream **1.44bn** (different perimeter/students).
- Wrote: sources 1; entities 5; budgets 25; cmt 1; lb 4; gap_univ FWB filled residual VL AHOVOKS; rq_160=done; seeded **rq_161**.
- FOI: gap_univ still **ready** for VL AHOVOKS exact only (prio 5).
- Next: prio5 **rq_161**; deferred **rq_116** SWA.
"""
lt = log.read_text(encoding="utf-8")
if not lt.endswith("\n"):
    lt += "\n"
log.write_text(lt + entry, encoding="utf-8", newline="\n")
print("tick165 write OK", sum_2026, do54_2026)

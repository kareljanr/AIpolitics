# tick 364 — dual popular/civic education VL SCW + FWB education permanente
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
        "fwb_education_permanente,FWB Education permanente DO23 prog3,Education permanente FWB,FWB permanent education dual Flanders SCW,agency,fwb_gov,fr,https://www.educationpermanente.cfwb.be,,,DO23 prog3 CL 44.604m associations 43.037m; dual VL SCW 83.1m; tick364",
        "vl_scw,Sociaal-cultureel volwassenenwerk Vlaanderen,Travail socioculturel pour adultes Flandre,Flanders social-cultural adult work dual FWB EP,agency,vlaanderen_gov,nl,https://www.vlaanderen.be/cjm,openbaarheid@vlaanderen.be,,BBT HCF2TE-WT VEK 83.125m 2026; dual FWB EP; tick364",
    ],
)

append_csv(
    "docs/doge/data/sources.csv",
    [
        "src_fwb_exp_part_dep_2026_ep,FWB Budget 2026 Exp part DO23 prog3 Education permanente,https://budget-finances.cfwb.be/budget-et-comptabilite/budgets-en-ligne/,Federation Wallonie-Bruxelles / Budget,2026-07-31,official_budget,Strong: DO23 prog3 EP CL 44.604m CE 30.442m; associations reconnues 33.06 CL 43.037m CE 29.657m; dual VL SCW; tick364",
        "src_vl_bbt_cultuur_bo2026_scw,BBT Cultuur BO2026 SCW line HCF2TE-WT,https://docs.vlaamsparlement.be/pfile?id=2227523,Vlaams Parlement / minister Cultuur,2026-07-31,official_budget,Strong: Sociaal-cultureel volwassenenwerk VEK 83.125m VAK 83.190m; cuts -3.5m; dual FWB EP 44.6m; tick364 (refresh tick358)",
    ],
)

append_csv(
    "docs/doge/data/budgets.csv",
    [
        "bud_fwb_ep_prog3_cl_2026,fwb_education_permanente,2026,44604000,,,budgeted,src_fwb_exp_part_dep_2026_ep,strong,DO23 prog3 Education permanente CL 44.604m 2026",
        "bud_fwb_ep_prog3_ce_2026,fwb_education_permanente,2026,30442000,,,budgeted,src_fwb_exp_part_dep_2026_ep,strong,DO23 prog3 EP CE 30.442m 2026",
        "bud_fwb_ep_prog3_cl_2025,fwb_education_permanente,2025,44804000,,,budgeted,src_fwb_exp_part_dep_2026_ep,strong,DO23 prog3 EP CL 44.804m 2025",
        "bud_fwb_ep_associations_cl_2026,fwb_education_permanente,2026,43037000,,,budgeted,src_fwb_exp_part_dep_2026_ep,strong,Subventions associations reconnues decret 2003 CL 43.037m (CE 29.657m) ~96pct of EP",
        "bud_fwb_ep_associations_ce_2026,fwb_education_permanente,2026,29657000,,,budgeted,src_fwb_exp_part_dep_2026_ep,strong,Associations reconnues CE 29.657m 2026",
        "bud_fwb_ep_formation_animateurs_2026,fwb_education_permanente,2026,365000,,,budgeted,src_fwb_exp_part_dep_2026_ep,strong,Formation animateurs socio-culturels 0.365m",
        "bud_fwb_ep_projets_2026,fwb_education_permanente,2026,482000,,,budgeted,src_fwb_exp_part_dep_2026_ep,strong,Projets EP alphabetisation creativite CL 0.482m",
        "bud_fwb_ep_loisirs_culturels_2026,fwb_education_permanente,2026,626000,,,budgeted,src_fwb_exp_part_dep_2026_ep,strong,Organisations loisirs culturels 0.626m",
        "bud_vl_scw_vek_2026_refresh,vl_scw,2026,83125000,,,budgeted,src_vl_bbt_cultuur_bo2026_scw,strong,SCW VEK 83.125m BO2026 refresh entity vl_scw",
        "bud_vl_scw_vak_2026_refresh,vl_scw,2026,83190000,,,budgeted,src_vl_bbt_cultuur_bo2026_scw,strong,SCW VAK 83.190m BO2026",
        "bud_popular_edu_dual_vl_fwb_2026,vl_scw,2026,127729000,,,budgeted,src_fwb_exp_part_dep_2026_ep,medium,Illustrative dual: VL SCW 83.125 + FWB EP CL 44.604 ~127.7m; not TE-additive; excludes formal EPA/VO and jeunesse",
    ],
)

append_csv(
    "docs/doge/data/commitments.csv",
    [
        'cmt_popular_edu_dual_vl_fwb_2026,Dual popular civic education Flanders SCW + FWB education permanente 2026,vl_scw,SCW organisations EP associations,Decreet sociaal-cultureel volwassenenwerk + decret education permanente 2003,2025-10-24,2026,2026,127729000,"{vl_scw_vek_m:83.125;fwb_ep_cl_m:44.604;fwb_associations_cl_m:43.037;note:not TE-additive; excludes formal adult education EPA/VO and recreational youth}",,active,https://www.educationpermanente.cfwb.be,Parallel dual community popular and civic adult education,Publish dual top orgs unit-cost; open beneficiary registers,src_fwb_exp_part_dep_2026_ep,strong,BE>dual>Popular_civic_education>VL_FWB,tick364: VL SCW 83.1m + FWB EP 44.6m associations 43.0m',
    ],
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    [
        "lb_fwb_ep_45m,FWB Education permanente 44.6m 2026,regional,programme,FWB>Culture>Education_permanente,44604000,44604000,Exp part strong CL 44.604m CE 30.442m; associations 43.0m dual VL SCW 83m,strong,src_fwb_exp_part_dep_2026_ep,EP associations adults,Permanent civic popular education,Core dual civil society education; L5 residual,4,6,4,4.9,Publish top associations EUR; dual SCW,seed,,tick364",
        "lb_fwb_ep_associations_43m,FWB EP associations reconnues 43.0m 2026,regional,subsidy,FWB>Education_permanente>associations,43037000,43037000,Exp part strong CL 43.037m CE 29.657m decret 2003; ~96pct of EP,strong,src_fwb_exp_part_dep_2026_ep,Recognised EP associations,Structural permanent education subsidies,Core civil society dual SCW,4,6,4,4.9,Open named association matrix,seed,,tick364",
        "lb_vl_scw_83m_refresh,Flanders SCW 83.1m 2026 dual EP,regional,subsidy,Vlaanderen>Cultuur>SCW,83125000,83125000,BBT VEK 83.125m dual FWB EP 44.6m; cuts -3.5m,strong,src_vl_bbt_cultuur_bo2026_scw,SCW organisations landelijk regionaal,Social-cultural adult work,Core dual popular education,4,6.5,4,5.1,Open beneficiary register dual EP,seed,,tick364",
        "lb_popular_edu_dual_vl_fwb,Dual VL SCW + FWB EP popular education ~128m,regional,overhead_dual,BE>dual>Popular_civic_education,127729000,127729000,VL 83.1 + FWB 44.6; not TE-additive; classic civil-society dual,medium,src_fwb_exp_part_dep_2026_ep,Parallel popular education stacks,Community dual civic adult education,Dual path; L5 residual both sides,5,7,4,5.55,One dual reporting matrix unit costs,seed,,tick364",
    ],
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    [
        "gap_popular_edu_dual_vl_fwb_l5,BE>dual>Popular_education>VL_FWB_L5,vl_scw,VL SCW top-30 landelijke/regionale organisaties 2023-2026 cash; FWB EP top-30 associations reconnues decret 2003 2023-2026; dual unit cost; alphabetisation path,Domain totals strong dual; residual named L5 both sides,6,Departement CJM / Team Openbaarheid / Service Education permanente FWB,openbaarheid@vlaanderen.be; educationpermanente.cfwb.be,Havenlaan Brussel; FWB Bruxelles,docs/doge/foi/drafts/gap_popular_edu_dual_vl_fwb_l5.md,ready,2026-07-31,,,,,cmt_popular_edu_dual_vl_fwb_2026,lb_fwb_ep_45m|lb_vl_scw_83m_refresh|lb_popular_edu_dual_vl_fwb,2026-07-31T20:45:00Z,2026-07-31T20:45:00Z,tick364 public BBT+ExpPart; residual L5 human send",
    ],
)

rq_path = ROOT / "docs/doge/data/research_queue.csv"
lines = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_355,"):
        out.append(
            "rq_355,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_popular_edu_dual_vl_fwb_l5,2026-07-31T20:15:00Z,2026-07-31T20:45:00Z,tick364: VL SCW 83.1m dual FWB EP 44.6m associations 43.0m dual ~128m; FOI L5; spawn rq_356"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_356,") for l in out):
    out.append(
        "rq_356,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-07-31T20:45:00Z,,Spawned tick364 after popular education dual SCW/EP; rq_116 SWA deferred"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")

(ROOT / "docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-31T20:45:00Z,rq_355,364,no,Scheduler 60s. Next prio5 rq_356; rq_116 SWA deferred. FOI ready. tick364 popular education dual SCW/EP.\n",
    encoding="utf-8",
    newline="\n",
)
print("tick364 write complete")

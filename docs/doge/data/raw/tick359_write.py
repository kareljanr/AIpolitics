# tick 359 — dual recreational youth VL Jeugd + FWB DO23 Jeunesse
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
        "jeugd_cjm_vl,Departement CJM beleidsveld Jeugd / Jeugddecreet,Departement CJM politique Jeunesse Flandre,Flanders Youth policy field dual FWB DO23 Jeunesse,agency,vlaanderen_gov,nl,https://www.vlaanderen.be/cjm,openbaarheid@vlaanderen.be,,BBT Jeugd BO2026 ISE total 72.461m; jeugdwerk 47.5m dual FWB; tick359",
        "fwb_jeunesse_do23,FWB Service de la Jeunesse DO23 prog 2,Service de la Jeunesse FWB,FWB recreational Youth Service dual Flanders Jeugd,agency,fwb_gov,fr,https://www.servicejeunesse.cfwb.be,,,DO23 prog 2 Jeunesse CL 67.137m CE 67.951m 2026; dual VL; not Aide a la Jeunesse DO17; tick359",
    ],
)

append_csv(
    "docs/doge/data/sources.csv",
    [
        "src_vl_bbt_jeugd_bo2026,Beleids- en begrotingstoelichting Jeugd Begroting 2026 13-E,https://docs.vlaamsparlement.be/pfile?id=2226255,Vlaams Parlement / minister Jeugd Depraetere,2026-07-31,official_budget,Strong: ISE Jeugd BO2026 total 72.461m; kwaliteit jeugdwerk VEK 47.461; jeugdvakanties 9.792 innovatie 8.545 lokaal 2.309 ULDK 2.167 JINT 1.263 kinderrechten 0.844; dual FWB; tick359",
        "src_fwb_exp_part_dep_2026_jeunesse,FWB Budget 2026 Expose particulier DO23 Jeunesse et education permanente,https://budget-finances.cfwb.be/budget-et-comptabilite/budgets-en-ligne/,Federation Wallonie-Bruxelles / Budget,2026-07-31,official_budget,Strong: DO23 prog 2 Jeunesse CE 67.951m CL 67.137m 2026; org jeunesse 26.822 centres de jeunes 34.811; EP prog 3 CL 44.604 separate; dual VL; tick359",
    ],
)

append_csv(
    "docs/doge/data/budgets.csv",
    [
        "bud_vl_jeugd_ise_total_2026,jeugd_cjm_vl,2026,72461000,,,budgeted,src_vl_bbt_jeugd_bo2026,strong,ISE Jeugd BO2026 total package 72.461m (VAK 70.242 + IS 2.219)",
        "bud_vl_jeugd_ise_total_2025,jeugd_cjm_vl,2025,72696000,,,budgeted,src_vl_bbt_jeugd_bo2026,strong,ISE Jeugd BA2025 total 72.696m",
        "bud_vl_jeugdwerk_vek_2026,jeugd_cjm_vl,2026,47461000,,,budgeted,src_vl_bbt_jeugd_bo2026,strong,HB0-1HDB2UE-WT Kwaliteit jeugdwerk VEK 47.461m (erkende verenigingen Ambrassade; incl ex-DAC integrate)",
        "bud_vl_jeugdvakanties_2026,jeugd_cjm_vl,2026,9792000,,,budgeted,src_vl_bbt_jeugd_bo2026,strong,HB0-1HDB2UG-WT Jeugdvakanties 9.792m (302 logies hostels)",
        "bud_vl_jeugd_innovatie_2026,jeugd_cjm_vl,2026,8545000,,,budgeted,src_vl_bbt_jeugd_bo2026,strong,HB0-1HDB2UH-WT Innovatie projecten 8.545m",
        "bud_vl_jeugd_lokaal_int_2026,jeugd_cjm_vl,2026,2309000,,,budgeted,src_vl_bbt_jeugd_bo2026,strong,HB0-1HDB2UD-WT Lokaal en internationaal 2.309m (Bataljong IGS VGC)",
        "bud_vl_uldk_toelage_2026,jeugd_cjm_vl,2026,2167000,,,budgeted,src_vl_bbt_jeugd_bo2026,strong,ULDK kampeermateriaal toelage 2.167m BO2026",
        "bud_vl_jint_2026,jeugd_cjm_vl,2026,1263000,,,budgeted,src_vl_bbt_jeugd_bo2026,strong,HB0-1HDB2UF-WT JINT internationale uitwisseling 1.263m",
        "bud_vl_kinderrechten_2026,jeugd_cjm_vl,2026,844000,,,budgeted,src_vl_bbt_jeugd_bo2026,strong,HB0-1HDB2UB-WT Kinderrechten Kruispunt 0.844m",
        "bud_fwb_jeunesse_cl_2026,fwb_jeunesse_do23,2026,67137000,,,budgeted,src_fwb_exp_part_dep_2026_jeunesse,strong,DO23 prog 2 Jeunesse CL 67.137m 2026",
        "bud_fwb_jeunesse_ce_2026,fwb_jeunesse_do23,2026,67951000,,,budgeted,src_fwb_exp_part_dep_2026_jeunesse,strong,DO23 prog 2 Jeunesse CE 67.951m 2026",
        "bud_fwb_jeunesse_cl_2025,fwb_jeunesse_do23,2025,66440000,,,budgeted,src_fwb_exp_part_dep_2026_jeunesse,strong,DO23 prog 2 Jeunesse CL 66.440m 2025",
        "bud_fwb_org_jeunesse_2026,fwb_jeunesse_do23,2026,26822000,,,budgeted,src_fwb_exp_part_dep_2026_jeunesse,strong,Subventions organisations de jeunesse 26.822m CE=CL 2026",
        "bud_fwb_centres_jeunes_2026,fwb_jeunesse_do23,2026,34811000,,,budgeted,src_fwb_exp_part_dep_2026_jeunesse,strong,Subventions centres de jeunes CL 34.811m 2026 (CE 35.473m)",
        "bud_fwb_ep_do23_cl_2026,fwb_jeunesse_do23,2026,44604000,,,budgeted,src_fwb_exp_part_dep_2026_jeunesse,strong,DO23 prog 3 Education permanente CL 44.604m (dual VL SCW not dual youth core)",
        "bud_youth_dual_vl_fwb_2026,jeugd_cjm_vl,2026,139598000,,,budgeted,src_vl_bbt_jeugd_bo2026,medium,Illustrative dual recreational youth: VL ISE 72.461 + FWB DO23 Jeunesse CL 67.137 ~139.6m; not TE-additive; excludes Aide a la Jeunesse 470m and VL jeugdhulp",
    ],
)

append_csv(
    "docs/doge/data/commitments.csv",
    [
        'cmt_youth_dual_vl_fwb_2026,Dual recreational youth work Flanders Jeugddecreet + FWB DO23 Jeunesse 2026,jeugd_cjm_vl,Youth orgs centres camps children,Jeugddecreet + decret organisations de jeunesse + centres de jeunes,2025-10-24,2026,2026,139598000,"{vl_ise_m:72.461;fwb_jeunesse_cl_m:67.137;vl_jeugdwerk_m:47.461;fwb_centres_m:34.811;fwb_org_m:26.822;note:excludes AJ DO17 470m protection and VL jeugdhulp Opgroeien}",,active,https://www.servicejeunesse.cfwb.be,Parallel dual community recreational youth stacks,Publish dual L5 top orgs unit-cost; keep protection dual separate,src_vl_bbt_jeugd_bo2026,strong,BE>dual>Youth_recreational>VL_FWB,tick359: VL BBT ISE 72.5m + FWB DO23 Jeunesse 67.1m',
    ],
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    [
        "lb_vl_jeugd_ise_72m,Flanders Jeugd ISE package 72.5m 2026,regional,programme,Vlaanderen>Jeugd>ISE,72461000,72461000,BBT strong ISE total 72.461m; jeugdwerk 47.5m dual FWB 67m recreational,strong,src_vl_bbt_jeugd_bo2026,Youth associations camps children,Voluntary youth work and holidays,Core youth not pure waste; L5 orgs residual FOI,4,6.5,3,4.85,Publish top recognised orgs cash; dual unit-cost,seed,,tick359",
        "lb_fwb_jeunesse_67m,FWB DO23 Jeunesse programme 67.1m 2026,regional,programme,FWB>Jeunesse>DO23,67137000,67137000,Exp part strong CL 67.137m CE 67.951m; centres 34.8 org 26.8; dual VL 72.5m,strong,src_fwb_exp_part_dep_2026_jeunesse,Youth orgs centres de jeunes,Recreational youth community policy,Core youth; not Aide a la Jeunesse 470m,4,6.5,3,4.85,Publish top centres and OJ EUR matrix,seed,,tick359",
        "lb_vl_jeugdwerk_47m,Flanders jeugdwerk erkenningen 47.5m 2026,regional,subsidy,Vlaanderen>Jeugd>Jeugdwerk,47461000,47461000,BBT VEK 47.461m erkende verenigingen + Ambrassade; -1.65m capacity cut,strong,src_vl_bbt_jeugd_bo2026,Recognised youth associations,Quality youth work support,Core civil society youth; dual FWB OJ,3,6,3,4.35,Open beneficiary list; dual FWB OJ map,seed,,tick359",
        "lb_youth_dual_vl_fwb,Dual VL+FWB recreational youth class ~140m,regional,overhead_dual,BE>dual>Youth_recreational,139598000,139598000,VL 72.5m + FWB 67.1m; not TE-additive; excludes AJ 470m protection dual,medium,src_vl_bbt_jeugd_bo2026,Parallel youth recreational stacks,Community dual voluntary youth,Classic dual; protection dual separate Opgroeien/AJ,5,7,4,5.55,One dual reporting matrix; keep AJ separate,seed,,tick359",
        "lb_fwb_centres_jeunes_35m,FWB centres de jeunes 34.8m 2026,regional,subsidy,FWB>Jeunesse>Centres,34811000,34811000,Exp part CL 34.811m centres de jeunes fonctionnement animateurs,strong,src_fwb_exp_part_dep_2026_jeunesse,Youth centres maisons de jeunes,Local youth centres network,Core local youth infrastructure dual VL jeugdhuizen class,3,6,4,4.5,Publish named centres top30,seed,,tick359",
    ],
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    [
        "gap_youth_dual_vl_fwb_l5,BE>dual>Youth>VL_FWB_L5,jeugd_cjm_vl,VL top-30 recognised jeugdwerk orgs + jeugdverblijven cash 2023-2026; FWB top-30 organisations de jeunesse + centres de jeunes 2023-2026; dual unit cost; BEL-J cash path; keep separate from Aide a la Jeunesse L5,Domain totals strong dual recreational; residual named L5 both sides,6,Departement CJM Jeugd / Team Openbaarheid / Service de la Jeunesse FWB,openbaarheid@vlaanderen.be; servicejeunesse.cfwb.be,Havenlaan Brussel; FWB Bruxelles,docs/doge/foi/drafts/gap_youth_dual_vl_fwb_l5.md,ready,2026-07-31,,,,,cmt_youth_dual_vl_fwb_2026,lb_vl_jeugd_ise_72m|lb_fwb_jeunesse_67m|lb_youth_dual_vl_fwb,2026-07-31T18:15:00Z,2026-07-31T18:15:00Z,tick359 public BBT+ExpPart; residual L5 human send",
    ],
)

# research_queue
rq_path = ROOT / "docs/doge/data/research_queue.csv"
lines = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_350,"):
        out.append(
            "rq_350,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_youth_dual_vl_fwb_l5,2026-07-31T17:45:00Z,2026-07-31T18:15:00Z,tick359: VL Jeugd ISE 72.5m + FWB DO23 Jeunesse CL 67.1m dual ~140m; FOI L5; spawn rq_351"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_351,") for l in out):
    out.append(
        "rq_351,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-07-31T18:15:00Z,,Spawned tick359 after youth dual VL/FWB; rq_116 SWA deferred"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("research_queue updated")

(ROOT / "docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-31T18:15:00Z,rq_350,359,no,Scheduler 60s. Next prio5 rq_351; rq_116 SWA deferred. FOI ready. tick359 youth dual VL/FWB.\n",
    encoding="utf-8",
    newline="\n",
)
print("loop_state updated")
print("tick359 write complete")

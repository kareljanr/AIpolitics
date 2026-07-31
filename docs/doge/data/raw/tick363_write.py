# tick 363 — dual PSB media 2026 refresh RTBF official + VRT basistoelage
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
        "fwb_medias_do25,FWB DO25 Audiovisuel et Multimedia / Medias portfolio,Division organique 25 Medias FWB,FWB media portfolio DO25 dual VL media/VRT,agency,fwb_gov,fr,https://www.rtbf.be,,,DO25 CL 426.353m 2026 RTBF package 389.3m; dual VRT; tick363",
    ],
)

append_csv(
    "docs/doge/data/sources.csv",
    [
        "src_fwb_exp_part_dep_2026_medias,FWB Budget 2026 Expose particulier DO25 Audiovisuel Multimedia RTBF,https://budget-finances.cfwb.be/budget-et-comptabilite/budgets-en-ligne/,Federation Wallonie-Bruxelles / Budget,2026-07-31,official_budget,Strong: DO25 CL 426.353m CE 424.988m; Radio-TV CL 402.971m; RTBF ordinary 350.819 access 4.050 pension 13.956 TV5 1.230+8.310 SEC 10.897 package 389.262m; MDP ~12.4m; presse 14.775; CSA 3.751; dual VRT 296.4m; tick363",
    ],
)

append_csv(
    "docs/doge/data/budgets.csv",
    [
        "bud_fwb_do25_medias_cl_2026,fwb_medias_do25,2026,426353000,,,budgeted,src_fwb_exp_part_dep_2026_medias,strong,DO25 Audiovisuel Multimedias CL 426.353m 2026",
        "bud_fwb_do25_medias_ce_2026,fwb_medias_do25,2026,424988000,,,budgeted,src_fwb_exp_part_dep_2026_medias,strong,DO25 CE 424.988m 2026",
        "bud_fwb_do25_radiotv_cl_2026,fwb_medias_do25,2026,402971000,,,budgeted,src_fwb_exp_part_dep_2026_medias,strong,DO25 prog3 Radio et television CL 402.971m 2026",
        "bud_rtbf_ordinary_2026,rtbf,2026,350819000,,,budgeted,src_fwb_exp_part_dep_2026_medias,strong,RTBF dotation ordinaire 41.01 CE=CL 350.819m 2026 (flat vs 2025 initial)",
        "bud_rtbf_access_2026,rtbf,2026,4050000,,,budgeted,src_fwb_exp_part_dep_2026_medias,strong,RTBF accessibilite programmes 41.02 4.050m",
        "bud_rtbf_pension_pool_2026,rtbf,2026,13956000,,,budgeted,src_fwb_exp_part_dep_2026_medias,strong,RTBF cotisation pool parastataux 41.03 13.956m (was 14.673m)",
        "bud_rtbf_tv5_frais_2026,rtbf,2026,1230000,,,budgeted,src_fwb_exp_part_dep_2026_medias,strong,RTBF frais specifiques TV5 41.05 1.230m",
        "bud_rtbf_sec_2026,rtbf,2026,10897000,,,budgeted,src_fwb_exp_part_dep_2026_medias,strong,RTBF SEC responsabilisation 41.07 10.897m",
        "bud_rtbf_tv5_soutien_2026,rtbf,2026,8310000,,,budgeted,src_fwb_exp_part_dep_2026_medias,strong,RTBF soutien projet TV5 81.05 8.310m",
        "bud_rtbf_public_package_2026,rtbf,2026,389262000,,,budgeted,src_fwb_exp_part_dep_2026_medias,strong,RTBF public package sum ordinary+access+pension+TV5x2+SEC 389.262m 2026",
        "bud_fwb_mdp_proximite_cl_2026,fwb_medias_do25,2026,12417000,,,budgeted,src_fwb_exp_part_dep_2026_medias,medium,Medias de proximite CL class ~12.417m (10.185+0.255+0.139+1.091+0.347+0.400)",
        "bud_fwb_presse_cl_2026,fwb_medias_do25,2026,14775000,,,budgeted,src_fwb_exp_part_dep_2026_medias,strong,DO25 prog4 Presse CL 14.775m 2026",
        "bud_fwb_csa_2026,fwb_medias_do25,2026,3751000,,,budgeted,src_fwb_exp_part_dep_2026_medias,strong,CSA dotation 3.751m 2026",
        "bud_vrt_basistoelage_2026_refresh,vrt,2026,296400000,,,budgeted,src_vl_vrt_dotatie_pq,strong,VRT basistoelage 296.4m 2026 (existing commitment; dual RTBF ordinary 350.8m)",
        "bud_psb_dual_ordinary_2026,vrt,2026,647219000,,,budgeted,src_fwb_exp_part_dep_2026_medias,strong,Dual PSB ordinary: VRT 296.4 + RTBF ordinary 350.819 = 647.219m 2026",
        "bud_psb_dual_package_2026,vrt,2026,685662000,,,budgeted,src_fwb_exp_part_dep_2026_medias,medium,Dual PSB packages: VRT base 296.4 + RTBF full public 389.262 ~685.7m; not TE-additive",
    ],
)

append_csv(
    "docs/doge/data/commitments.csv",
    [
        'cmt_psb_dual_vl_fwb_2026,Dual public service broadcasting VRT basistoelage + RTBF official package 2026,vrt,Public broadcasters NL FR households,Beheersovereenkomst VRT 2026-30 + Contrat de gestion RTBF 2023-2027,2025-07-18,2026,2030,685662000,"{2026_vrt_base_m:296.4;2026_rtbf_ordinary_m:350.819;2026_rtbf_package_m:389.262;2026_fwb_do25_cl_m:426.353;2026_dual_ordinary_m:647.219;note:not TE-additive; RTBF package=ordinary+access+pension+TV5+SEC}",,active,https://www.rtbf.be,Parallel dual community public service broadcasting,Benchmark unit-cost dual; deliver RTBF savings path; open annual L5 side envelopes,src_fwb_exp_part_dep_2026_medias,strong,BE>dual>PSB_Media>VRT_RTBF,tick363: official FWB BI2026 RTBF L5 lines; dual VRT 296.4m',
    ],
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    [
        "lb_rtbf_ordinary_351m_2026,RTBF ordinary dotation 350.8m 2026 official,regional,agency_dotation,FWB>Media>RTBF>ordinary,350819000,350819000,Exp part strong CE=CL 350.819m flat vs 2025I; dual VRT 296.4m,strong,src_fwb_exp_part_dep_2026_medias,Francophone households,Public service broadcasting ordinary,Core PSB dual; structural dualism cost,5,8,6,6.35,Benchmark vs VRT; open full package L5,seed,,tick363",
        "lb_rtbf_package_389m_2026,RTBF public package 389.3m 2026 official,regional,agency_dotation,FWB>Media>RTBF>package,389262000,389262000,Strong sum ordinary 350.8+access 4.05+pension 13.96+TV5 1.23+8.31+SEC 10.9=389.3m,strong,src_fwb_exp_part_dep_2026_medias,Francophone households,Full FWB public RTBF financing,Core dual PSB; vs RA2025 package ~378m,5,8,6,6.35,Track vs RA outturn; dual unit-cost VRT,seed,,tick363",
        "lb_fwb_do25_medias_426m,FWB DO25 Media portfolio CL 426.4m 2026,regional,programme,FWB>Media>DO25,426353000,426353000,Exp part strong CL 426.353m; RTBF path + MDP + presse + CSA,strong,src_fwb_exp_part_dep_2026_medias,Media sector FWB,Community media policy portfolio,Core dual media; includes non-RTBF lines,4,8,5,5.95,Publish dual VL media BBT matrix,seed,,tick363",
        "lb_psb_dual_ordinary_647m_2026,Dual PSB ordinary VRT+RTBF 647m 2026,regional,overhead_dual,BE>dual>PSB>ordinary,647219000,647219000,VRT 296.4 + RTBF ordinary 350.819 strong; not TE-additive,strong,src_fwb_exp_part_dep_2026_medias,BE dual-language audiences,Parallel public broadcasters,Classic dual structure cost visible,6,8,7,6.65,Efficiency dual dashboard; no automatic merge politics,seed,,tick363",
        "lb_fwb_mdp_12m_2026,FWB medias de proximite ~12.4m 2026,regional,subsidy,FWB>Media>MDP,12417000,12417000,Exp part strong MDP lines ~12.4m CL class; dual local media VL residual,strong,src_fwb_exp_part_dep_2026_medias,Local TV/radio audiences,Proximity media network,Core local media dual; L5 residual FOI,4,5,4,4.4,Publish top MDP EUR matrix,seed,,tick363",
    ],
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    [
        "gap_psb_dual_vl_fwb_l5_2026,BE>dual>PSB>VRT_RTBF_L5_2026,rtbf,RTBF cash-by-year ordinary vs complements 2023-2026 reconcile RA; VRT side-envelope L5 beyond basistoelage 296.4m; dual unit cost per viewer/hour; MDP top-20; presse top-10 dual VL,Official 2026 RTBF package strong; residual RA vs budget + VRT side L5,5,RTBF / CSA / Team Openbaarheid / VRT,openbaarheid@vlaanderen.be; rtbf.be,Boulevard A. Reyers Bruxelles; Havenlaan,docs/doge/foi/drafts/gap_psb_dual_vl_fwb_l5_2026.md,ready,2026-07-31,,,,,cmt_psb_dual_vl_fwb_2026,lb_rtbf_package_389m_2026|lb_psb_dual_ordinary_647m_2026,2026-07-31T20:15:00Z,2026-07-31T20:15:00Z,tick363 public FWB BI2026; residual dual L5 human send",
    ],
)

rq_path = ROOT / "docs/doge/data/research_queue.csv"
lines = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_354,"):
        out.append(
            "rq_354,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_psb_dual_vl_fwb_l5_2026,2026-07-31T19:45:00Z,2026-07-31T20:15:00Z,tick363: RTBF official package 389.3m dual VRT 296.4m ordinary dual 647m DO25 426m; FOI L5; spawn rq_355"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_355,") for l in out):
    out.append(
        "rq_355,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-07-31T20:15:00Z,,Spawned tick363 after PSB dual 2026 refresh; rq_116 SWA deferred"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")

(ROOT / "docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-31T20:15:00Z,rq_354,363,no,Scheduler 60s. Next prio5 rq_355; rq_116 SWA deferred. FOI ready. tick363 PSB dual 2026 RTBF/VRT.\n",
    encoding="utf-8",
    newline="\n",
)
print("tick363 write complete")

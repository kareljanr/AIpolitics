# tick 362 — dual territorial culture / lecture publique FWB + VL bovenlokaal
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
        "fwb_lecture_publique,FWB lecture publique / bibliotheques DO20 prog7,Reseau de lecture publique FWB,FWB public library network dual Flanders local libraries,agency,fwb_gov,fr,https://www.culture.be,,,Bibliotheques CL 23.975m + PointCulture 3.64m 2026; dual VL; tick362",
        "vl_bovenlokaal_cultuur,Bovenlokaal cultuurdecreet / cross-sectoraal cultuur VL,Decret culturel supralocal Flandre,Flanders above-local culture decree dual FWB territorial,agency,vlaanderen_gov,nl,https://www.vlaanderen.be/cjm,openbaarheid@vlaanderen.be,,BBT HCF2TA-WT VEK 15.461m 2026; dual FWB prog7 67.4m; tick362",
    ],
)

append_csv(
    "docs/doge/data/sources.csv",
    [
        "src_vl_bbt_cultuur_bo2026_territorial,Beleids- en begrotingstoelichting Cultuur BO2026 domain+bovenlokaal tables,https://docs.vlaamsparlement.be/pfile?id=2227523,Vlaams Parlement / minister Cultuur,2026-07-31,official_budget,Strong: Cultuur MVG excl DAB VEK 393.544m VAK 394.115m BO2026; HCF2TA-WT bovenlokaal/cross VEK 15.461m; leenrecht cut -1.834m; dual FWB territorial; tick362",
        "src_fwb_exp_part_dep_2026_territorial,FWB Budget 2026 Exp part DO20 prog7 Action culturelle territoriale,https://budget-finances.cfwb.be/budget-et-comptabilite/budgets-en-ligne/,Federation Wallonie-Bruxelles / Budget,2026-07-31,official_budget,Strong: prog7 CL 67.383m CE 110.872m; centres culturels CL 32.372 bibliotheques 23.975 CEC 5.292 PointCulture 3.640; dual VL; tick362",
    ],
)

append_csv(
    "docs/doge/data/budgets.csv",
    [
        "bud_vl_cultuur_domain_vek_2026,cultuur_cjm_vl,2026,393544000,,,budgeted,src_vl_bbt_cultuur_bo2026_territorial,strong,Cultuur MVG excl DAB ESR VEK BO2026 393.544m (VAK 394.115m); total with IS 516.854m",
        "bud_vl_cultuur_domain_vak_2026,cultuur_cjm_vl,2026,394115000,,,budgeted,src_vl_bbt_cultuur_bo2026_territorial,strong,Cultuur MVG excl DAB ESR VAK BO2026 394.115m",
        "bud_vl_cultuur_domain_vek_2025,cultuur_cjm_vl,2025,406838000,,,budgeted,src_vl_bbt_cultuur_bo2026_territorial,strong,Cultuur MVG excl DAB ESR VEK BA2025 406.838m",
        "bud_vl_bovenlokaal_cultuur_vek_2026,vl_bovenlokaal_cultuur,2026,15461000,,,budgeted,src_vl_bbt_cultuur_bo2026_territorial,strong,HB0-1HCF2TA-WT bovenlokaal/cross VEK 15.461m (VAK 15.592m) BO2026",
        "bud_vl_bovenlokaal_cultuur_vak_2026,vl_bovenlokaal_cultuur,2026,15592000,,,budgeted,src_vl_bbt_cultuur_bo2026_territorial,strong,HB0-1HCF2TA-WT VAK 15.592m BO2026",
        "bud_vl_leenrecht_cut_2026,vl_bovenlokaal_cultuur,2026,-1834000,,,budgeted,src_vl_bbt_cultuur_bo2026_territorial,strong,Besparing leenrecht bibliotheken -1.834m BO2026 inside HCF2TA-WT",
        "bud_fwb_action_territoriale_cl_2026_detail,fwb_culture_do20,2026,67383000,,,budgeted,src_fwb_exp_part_dep_2026_territorial,strong,DO20 prog7 Action culturelle territoriale CL 67.383m 2026 (refresh tick358 line)",
        "bud_fwb_centres_culturels_cl_2026,fwb_culture_do20,2026,32372000,,,budgeted,src_fwb_exp_part_dep_2026_territorial,strong,Centres culturels conventions/CP CL 32.372m 2026",
        "bud_fwb_bibliotheques_cl_2026,fwb_lecture_publique,2026,23975000,,,budgeted,src_fwb_exp_part_dep_2026_territorial,strong,Bibliotheques conventions/CP CL 23.975m 2026",
        "bud_fwb_bibliotheques_ce_2026,fwb_lecture_publique,2026,41114000,,,budgeted,src_fwb_exp_part_dep_2026_territorial,strong,Bibliotheques CE 41.114m 2026 (vs CL 23.975; multi-year eng)",
        "bud_fwb_cec_amateurs_cl_2026,fwb_culture_do20,2026,5292000,,,budgeted,src_fwb_exp_part_dep_2026_territorial,strong,CEC et pratiques amateurs CL 5.292m",
        "bud_fwb_pointculture_2026,fwb_lecture_publique,2026,3640000,,,budgeted,src_fwb_exp_part_dep_2026_territorial,strong,ASBL PointCulture 3.640m CE=CL 2026",
        "bud_fwb_biblio_it_2026,fwb_lecture_publique,2026,125000,,,budgeted,src_fwb_exp_part_dep_2026_territorial,strong,Bibliotheques IT equipment 0.125m",
        "bud_territorial_culture_dual_2026,vl_bovenlokaal_cultuur,2026,82844000,,,budgeted,src_fwb_exp_part_dep_2026_territorial,medium,Illustrative dual: FWB prog7 CL 67.383 + VL bovenlokaal VEK 15.461 ~82.8m; not TE-additive; VL municipal library spend residual FOI",
    ],
)

append_csv(
    "docs/doge/data/commitments.csv",
    [
        'cmt_territorial_culture_dual_2026,Dual territorial culture and public reading FWB DO20 prog7 + VL bovenlokaal cultuurdecreet 2026,vl_bovenlokaal_cultuur,Municipal libraries cultural centres IGS,Decret centres culturels + lecture publique + Bovenlokaal cultuurdecreet,2025-10-24,2026,2026,82844000,"{fwb_prog7_cl_m:67.383;fwb_biblio_cl_m:23.975;fwb_cc_cl_m:32.372;fwb_pointculture_m:3.64;vl_bovenlokaal_vek_m:15.461;vl_cultuur_domain_vek_m:393.544;note:VL local library municipal spend residual FOI; dual not TE-additive}",,active,https://www.culture.be,Parallel dual community territorial culture and public reading,Publish dual library unit-cost; open VL leenrecht + municipal path,src_fwb_exp_part_dep_2026_territorial,strong,BE>dual>Territorial_culture_libraries>VL_FWB,tick362: FWB prog7 67.4m + VL bovenlokaal 15.5m; domain Cultuur VEK 393.5m',
    ],
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    [
        "lb_fwb_biblio_24m,FWB bibliotheques lecture publique CL 24.0m 2026,regional,subsidy,FWB>Culture>Bibliotheques,23975000,23975000,Exp part strong CL 23.975m CE 41.114m; dual VL local libraries residual,strong,src_fwb_exp_part_dep_2026_territorial,Public library users FR community,Public reading network,Core culture dual; VL municipal residual FOI,4,5.5,4,4.65,Open dual library unit-cost; VL leenrecht path,seed,,tick362",
        "lb_fwb_centres_culturels_32m,FWB centres culturels 32.4m CL 2026,regional,subsidy,FWB>Culture>Centres_culturels,32372000,32372000,Exp part strong CL 32.372m CE 57.610m conventions/CP; dual VL local CC,strong,src_fwb_exp_part_dep_2026_territorial,Cultural centre audiences,Community cultural centres network,Core culture dual territorial,4,6,4,4.9,Publish top centres EUR; dual VL map,seed,,tick362",
        "lb_vl_bovenlokaal_15m,Flanders bovenlokaal cultuur/cross 15.5m 2026,regional,subsidy,Vlaanderen>Cultuur>Bovenlokaal,15461000,15461000,BBT HCF2TA-WT VEK 15.461m; -3.6m project cut -1.834m leenrecht,strong,src_vl_bbt_cultuur_bo2026_territorial,IGS municipalities local culture,Above-local culture and participation,Core dual territorial; small vs FWB 67m,4,5,3,4.35,Open IGS beneficiary list; dual FWB,seed,,tick362",
        "lb_vl_cultuur_domain_394m,Flanders Cultuur domain ESR VEK 393.5m 2026,regional,programme,Vlaanderen>Cultuur>domain,393544000,393544000,BBT strong MVG excl DAB VEK 393.544m VAK 394.115m; dual FWB DO20 367m CL,strong,src_vl_bbt_cultuur_bo2026_territorial,Culture sector Flanders,Community culture policy domain total,Core culture not pure waste; L5 residual FOI,4,8,4,5.8,Refresh dual culture matrix with domain total,seed,,tick362",
        "lb_territorial_culture_dual,Dual territorial culture VL 15.5m + FWB 67.4m ~83m,regional,overhead_dual,BE>dual>Territorial_culture,82844000,82844000,FWB prog7 CL 67.4 + VL bovenlokaal 15.5; asymmetric dual; municipal residual,medium,src_fwb_exp_part_dep_2026_territorial,Parallel territorial culture stacks,Community dual local-supralocal culture,Classic dual path; library opacity VL,5,6.5,4,5.35,One dual reporting matrix libraries+CC,seed,,tick362",
    ],
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    [
        "gap_territorial_culture_dual_vl_fwb_l5,BE>dual>Territorial_culture>VL_FWB_L5,vl_bovenlokaal_cultuur,VL Bovenlokaal cultuurdecreet top IGS/project beneficiaries 2023-2026; leenrecht bibliotheken cash path multi-year; FWB top-30 centres culturels + bibliotheques 2023-2026; dual unit cost; PointCulture L5,Domain totals strong; residual named L5 both sides + VL municipal library spend,6,Departement CJM / Team Openbaarheid / AGC Culture FWB,openbaarheid@vlaanderen.be; culture.be,Havenlaan Brussel; FWB Bruxelles,docs/doge/foi/drafts/gap_territorial_culture_dual_vl_fwb_l5.md,ready,2026-07-31,,,,,cmt_territorial_culture_dual_2026,lb_fwb_biblio_24m|lb_fwb_centres_culturels_32m|lb_territorial_culture_dual,2026-07-31T19:45:00Z,2026-07-31T19:45:00Z,tick362 public BBT+ExpPart; residual L5 human send",
    ],
)

rq_path = ROOT / "docs/doge/data/research_queue.csv"
lines = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_353,"):
        out.append(
            "rq_353,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_territorial_culture_dual_vl_fwb_l5,2026-07-31T19:15:00Z,2026-07-31T19:45:00Z,tick362: FWB territorial 67.4m biblio 24.0m dual VL bovenlokaal 15.5m Cultuur domain VEK 393.5m; FOI L5; spawn rq_354"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_354,") for l in out):
    out.append(
        "rq_354,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-07-31T19:45:00Z,,Spawned tick362 after territorial culture dual; rq_116 SWA deferred"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")

(ROOT / "docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-31T19:45:00Z,rq_353,362,no,Scheduler 60s. Next prio5 rq_354; rq_116 SWA deferred. FOI ready. tick362 territorial culture dual.\n",
    encoding="utf-8",
    newline="\n",
)
print("tick362 write complete")

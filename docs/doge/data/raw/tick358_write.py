# tick 358 CSV writes — dual culture VL + FWB
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]  # repo root from docs/doge/data/raw


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
        "cultuur_cjm_vl,Departement Cultuur Jeugd Media / beleidsveld Cultuur,Departement Culture Jeunesse Medias Flandre,Flanders Culture Youth Media department culture field dual FWB DO20,agency,vlaanderen_gov,nl,https://www.vlaanderen.be/cjm,openbaarheid@vlaanderen.be,,BBT Cultuur BO2026 Kunsten VEK 157.966m Erfgoed 85.6 SCW 83.1 dual FWB DO20; tick358",
        "fwb_culture_do20,FWB Administration generale de la Culture DO20,Administration generale de la Culture FWB,FWB General Culture Administration dual Flanders CJM,agency,fwb_gov,fr,https://www.culture.be,,,DO20 Culture CL 367.468m CE 267.213m 2026; dual VL Cultuur; tick358",
    ],
)

append_csv(
    "docs/doge/data/sources.csv",
    [
        "src_vl_bbt_cultuur_bo2026,Beleids- en begrotingstoelichting Cultuur Begroting 2026 13-R,https://docs.vlaamsparlement.be/pfile?id=2227523,Vlaams Parlement / minister Cultuur Gennez,2026-07-31,official_budget,Strong: Kunsten VEK 157.966m Erfgoed 85.589 SCW 83.125 Amateur 14.031 Digital 20.161 Opera Ballet 31.045 KMSKA 12.123 Philharmonic 10.554 Literatuur 11.611 VIA 67.160; dual FWB; tick358",
        "src_fwb_exp_part_dep_2026_culture,FWB Budget 2026 Expose particulier depenses DO20 Culture DO23 DO25 DO26,https://budget-finances.cfwb.be/budget-et-comptabilite/budgets-en-ligne/,Federation Wallonie-Bruxelles / Budget,2026-07-31,official_budget,Strong: DO20 Culture CE 267.213m CL 367.468m 2026; arts vivants CL 103.630 transversal 92.187 territoriale 67.383 musiques 52.725; DO25 AV 25.508; DO26 Sport 49.981; dual VL; tick358",
    ],
)

append_csv(
    "docs/doge/data/budgets.csv",
    [
        "bud_vl_kunsten_vek_2026,cultuur_cjm_vl,2026,157966000,,,budgeted,src_vl_bbt_cultuur_bo2026,strong,HB0-1HCF2TC-WT Kunsten VEK BO2026 157.966m (Kunstendecreet Circus steunpunten)",
        "bud_vl_kunsten_vak_2026,cultuur_cjm_vl,2026,156701000,,,budgeted,src_vl_bbt_cultuur_bo2026,strong,Kunsten VAK BO2026 156.701m",
        "bud_vl_erfgoed_cult_vek_2026,cultuur_cjm_vl,2026,85589000,,,budgeted,src_vl_bbt_cultuur_bo2026,strong,HB0-1HCF2TB-WT Cultureel erfgoed VEK 85.589m",
        "bud_vl_scw_vek_2026,cultuur_cjm_vl,2026,83125000,,,budgeted,src_vl_bbt_cultuur_bo2026,strong,HB0-1HCF2TE-WT Sociaal-cultureel volwassenenwerk VEK 83.125m",
        "bud_vl_amateurkunsten_vek_2026,cultuur_cjm_vl,2026,14031000,,,budgeted,src_vl_bbt_cultuur_bo2026,strong,HB0-1HCF2TD-WT Amateurkunsten VEK=VAK 14.031m",
        "bud_vl_digitaal_cultuur_vek_2026,cultuur_cjm_vl,2026,20161000,,,budgeted,src_vl_bbt_cultuur_bo2026,strong,HB0-1HCF2TG-WT Digitale transformatie 20.161m",
        "bud_vl_opera_ballet_2026,cultuur_cjm_vl,2026,31045000,,,budgeted,src_vl_bbt_cultuur_bo2026,strong,Opera Ballet Vlaanderen IS toelage BO2026 31.045m",
        "bud_vl_kmska_2026,cultuur_cjm_vl,2026,12123000,,,budgeted,src_vl_bbt_cultuur_bo2026,strong,KMSKA EVA toelage 12.123m BO2026",
        "bud_vl_brussels_philharmonic_2026,cultuur_cjm_vl,2026,10554000,,,budgeted,src_vl_bbt_cultuur_bo2026,strong,Brussels Philharmonic kunstinstelling 10.554m BO2026",
        "bud_vl_literatuur_toelage_2026,cultuur_cjm_vl,2026,11611000,,,budgeted,src_vl_bbt_cultuur_bo2026,strong,Literatuur Vlaanderen betoelaging 11.611m BO2026",
        "bud_vl_via_cultuur_2026,cultuur_cjm_vl,2026,67160000,,,budgeted,src_vl_bbt_cultuur_bo2026,strong,VIA intersectorale akkoorden 67.160m culture-jeugd-media stack",
        "bud_vl_cultuur_content_class_2026,cultuur_cjm_vl,2026,426205000,,,budgeted,src_vl_bbt_cultuur_bo2026,medium,Sum content class 426.205m excl VIA/infra mixed",
        "bud_fwb_culture_do20_cl_2026,fwb_culture_do20,2026,367468000,,,budgeted,src_fwb_exp_part_dep_2026_culture,strong,DO20 Culture CL 367.468m 2026",
        "bud_fwb_culture_do20_ce_2026,fwb_culture_do20,2026,267213000,,,budgeted,src_fwb_exp_part_dep_2026_culture,strong,DO20 Culture CE 267.213m 2026",
        "bud_fwb_culture_do20_cl_2025,fwb_culture_do20,2025,362582000,,,budgeted,src_fwb_exp_part_dep_2026_culture,strong,DO20 Culture CL 362.582m 2025 initial",
        "bud_fwb_arts_vivants_cl_2026,fwb_culture_do20,2026,103630000,,,budgeted,src_fwb_exp_part_dep_2026_culture,strong,DO20 prog 2 Arts vivants CL 103.630m",
        "bud_fwb_culture_transversal_cl_2026,fwb_culture_do20,2026,92187000,,,budgeted,src_fwb_exp_part_dep_2026_culture,strong,DO20 prog 1 Transversal CL 92.187m",
        "bud_fwb_action_territoriale_cl_2026,fwb_culture_do20,2026,67383000,,,budgeted,src_fwb_exp_part_dep_2026_culture,strong,DO20 prog 7 Action territoriale CL 67.383m",
        "bud_fwb_musiques_cl_2026,fwb_culture_do20,2026,52725000,,,budgeted,src_fwb_exp_part_dep_2026_culture,strong,DO20 prog 3 Musiques CL 52.725m",
        "bud_fwb_patrimoines_cult_cl_2026,fwb_culture_do20,2026,23000000,,,budgeted,src_fwb_exp_part_dep_2026_culture,strong,DO20 prog 4 Patrimoines culturels CL 23.000m",
        "bud_fwb_av_do25_cl_2026,fwb_culture_do20,2026,25508000,,,budgeted,src_fwb_exp_part_dep_2026_culture,strong,DO25 Audiovisuel CL 25.508m outside DO20 dual core",
        "bud_fwb_sport_do26_cl_2026,adeps,2026,49981000,,,budgeted,src_fwb_exp_part_dep_2026_culture,strong,DO26 Sport CL 49.981m confirms ADEPS class",
        "bud_culture_dual_vl_fwb_2026,cultuur_cjm_vl,2026,793673000,,,budgeted,src_vl_bbt_cultuur_bo2026,medium,Illustrative dual VL 426.2m + FWB DO20 CL 367.5m ~794m not TE-additive",
    ],
)

append_csv(
    "docs/doge/data/commitments.csv",
    [
        'cmt_culture_dual_vl_fwb_2026,Dual community culture policy Flanders CJM + FWB DO20 Culture 2026,cultuur_cjm_vl,Artists orgs federations museums public,Kunstendecreet Cultureelerfgoeddecreet + FWB culture decrees,2025-10-24,2026,2026,793673000,"{vl_content_m:426.205;fwb_do20_cl_m:367.468;vl_kunsten_m:157.966;fwb_arts_vivants_m:103.63}",,active,https://www.culture.be,Parallel dual community culture stacks post-federalisation,Publish dual L5 top operators unit-cost; review moratoria savings path,src_fwb_exp_part_dep_2026_culture,strong,BE>dual>Culture>VL_FWB,tick358: VL BBT L5 + FWB DO20 programme table',
    ],
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    [
        "lb_vl_kunsten_158m,Flanders Kunsten decree package VEK 158m 2026,regional,subsidy_package,Vlaanderen>Cultuur>Kunsten,157966000,157966000,BBT strong VEK 157.966m Kunstendecreet Circus steunpunten; dual FWB arts vivants 104m,strong,src_vl_bbt_cultuur_bo2026,Artists orgs festivals,Professional arts multi-year support,Core culture not pure waste; L5 org list residual FOI,4,7.5,4,5.55,Publish ranked 236 orgs cash; dual unit-cost,seed,,tick358",
        "lb_fwb_culture_do20_367m,FWB Culture DO20 liquidation 367m 2026,regional,programme,FWB>Culture>DO20,367468000,367468000,Exp part strong CL 367.468m CE 267.213m; arts vivants 104 transversal 92 territoriale 67 musiques 53,strong,src_fwb_exp_part_dep_2026_culture,FWB cultural operators,Community culture policy,Moratoire + non-indexation savings path; L5 residual,5,8,4,5.9,Publish top L5 operators; dual VL matrix,seed,,tick358",
        "lb_vl_scw_83m,Flanders sociaal-cultureel volwassenenwerk 83m 2026,regional,subsidy,Vlaanderen>Cultuur>SCW,83125000,83125000,BBT VEK 83.125m structural orgs; cuts -3.5m,strong,src_vl_bbt_cultuur_bo2026,SCW organisations,Democratic civil society education,Core civil society; dual FWB education permanente,4,6.5,4,5.1,Open beneficiary register; dual EP path,seed,,tick358",
        "lb_culture_dual_vl_fwb,Dual VL+FWB culture class ~794m,regional,overhead_dual,BE>dual>Culture,793673000,793673000,VL content ~426m + FWB DO20 CL 367m; not TE-additive; classic community dual,medium,src_vl_bbt_cultuur_bo2026,Parallel culture stacks,Post-federalisation dual culture,Two culture administrations; opacity L5 dual,6,8,5,6.4,One dual reporting matrix; open L5 both sides,seed,,tick358",
        "lb_vl_opera_ballet_31m,Opera Ballet Vlaanderen toelage 31m 2026,regional,agency_dotation,Vlaanderen>Cultuur>Opera_Ballet,31045000,31045000,BBT IS toelage 31.045m BO2026; largest single VL arts house class,strong,src_vl_bbt_cultuur_bo2026,Audiences dancers singers,Flagship lyric dance institution,Core high art; dual FWB opera residual,3,6,3,4.5,Publish cost per seat dual; efficiency scan,seed,,tick358",
    ],
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    [
        "gap_culture_dual_vl_fwb_l5,BE>dual>Culture>VL_FWB_L5,cultuur_cjm_vl,VL top-50 Kunstendecreet+erfgoed+SCW beneficiaries 2023-2026 cash; FWB DO20 top-50 operators arts vivants/musiques/territoriale 2023-2026; dual unit cost per org/seat; moratoria non-indexation cash impact 2026,Domain totals strong dual; residual named L5 both sides,6,Departement CJM / Team Openbaarheid / AGC FWB Culture,openbaarheid@vlaanderen.be; culture.be,Havenlaan Brussel; FWB Bruxelles,docs/doge/foi/drafts/gap_culture_dual_vl_fwb_l5.md,ready,2026-07-31,,,,,cmt_culture_dual_vl_fwb_2026,lb_vl_kunsten_158m|lb_fwb_culture_do20_367m|lb_culture_dual_vl_fwb,2026-07-31T17:45:00Z,2026-07-31T17:45:00Z,tick358 public BBT+ExpPart; residual L5 human send",
    ],
)

# research_queue: close rq_349, spawn rq_350
rq_path = ROOT / "docs/doge/data/research_queue.csv"
lines = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_349,"):
        out.append(
            "rq_349,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_culture_dual_vl_fwb_l5,2026-07-31T17:15:00Z,2026-07-31T17:45:00Z,tick358: VL Cultuur content ~426m + FWB DO20 CL 367m dual ~794m; FOI L5; spawn rq_350"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_350,") for l in out):
    out.append(
        "rq_350,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-07-31T17:45:00Z,,Spawned tick358 after culture dual VL/FWB; rq_116 SWA deferred"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("research_queue updated")

# loop_state
(ROOT / "docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-31T17:45:00Z,rq_349,358,no,Scheduler 60s. Next prio5 rq_350; rq_116 SWA deferred. FOI ready. tick358 culture dual VL/FWB.\n",
    encoding="utf-8",
    newline="\n",
)
print("loop_state updated")
print("tick358 write complete")

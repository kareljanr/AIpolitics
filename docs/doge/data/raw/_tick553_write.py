# tick553 — CoA 2026_35 Flanders teacher induction + professionalization L5
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T09:10:00Z"

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_vl_leraren_begeleiding_2026,CoA Flanders teacher induction+professionalization 2026_35,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_35_AanvangsbegeleidingProfessionaliseringLeraren.pdf,"
        "Rekenhof NL chamber 30 Jun 2026,2026-07-31,court_of_audit,"
        "Strong tick553: AVB budget 31.0 to 52.2m 2019-25 (basis 30.5 sec 21.6); induction 48.7m + workings 38.7m 2025-26; "
        "prof total 50.8 to 62.4m 2020-25 (schools 44.9 PBD 17.5); Leerpunt 0.11 to 5.7m; 120-130 EUR/relation; "
        "no global eval; pupil-based financing mismatch starters; dual FWB Cepage IT; raw ccrek_2026_35_begeleiding_leraren.pdf\n"
    )
    f.write(
        "src_ccrek_vl_leraren_begeleiding_press,CoA press teacher induction professionalization Jul 2026,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_35_AanvangsbegeleidingProfessionaliseringLeraren_Communique.pdf,"
        "Rekenhof,2026-07-31,court_of_audit_press,"
        "Strong headlines: budget AVB triple path; coherence gap induction/bonus/AVB; professionalization plans weak; tick553\n"
    )
    f.write(
        "src_dual_vl_fwb_teacher_pd_tick553,Dual VL teacher PD stack vs FWB Cepage IT careers,"
        "docs/doge/data/raw/ccrek_2026_35_begeleiding_leraren.pdf,DOGE synthesis CoA VL 2026_35 + FWB 2026_31,2026-07-31,synthesis,"
        "Strong dual: VL colored AVB+prof ~115m class 2025 vs FWB education personnel 7.1bn + Cepage IT opacity; different failure modes; tick553\n"
    )

buds = [
    # AVB path
    "bud_vl_avb_2019_20,vlaanderen_gov,2020,31000000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,AVB starter induction intro budget ~31.0m 2019-20 (basis 20.3+sec 10.7); tick553",
    "bud_vl_avb_2020_21,vlaanderen_gov,2021,31900000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,AVB 31.9m 2020-21; tick553",
    "bud_vl_avb_2021_22,vlaanderen_gov,2022,41200000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,AVB 41.2m 2021-22; tick553",
    "bud_vl_avb_2022_23,vlaanderen_gov,2023,45100000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,AVB 45.1m 2022-23; tick553",
    "bud_vl_avb_2023_24,vlaanderen_gov,2024,50400000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,AVB 50.4m 2023-24; tick553",
    "bud_vl_avb_2024_25,vlaanderen_gov,2025,52200000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,AVB total 52.2m 2024-25 (basis 30.5+sec 21.6); tick553",
    "bud_vl_avb_basis_2024_25,vlaanderen_gov,2025,30500000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,AVB basisonderwijs 30.5m 2024-25; tick553",
    "bud_vl_avb_sec_2024_25,vlaanderen_gov,2025,21600000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,AVB secundair 21.6m 2024-25; tick553",
    "bud_vl_inductie_envelope_2026_27,vlaanderen_gov,2026,48700000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,Induction units envelope 48.7m (not enough for 20pct all starters); tick553",
    "bud_vl_avb_workings_alt_2025_26,vlaanderen_gov,2025,38700000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,One-time extra workingsbudget 38.7m 2025-26 as induction delay alternative; tick553",
    "bud_vl_avb_2026_27_class,vlaanderen_gov,2026,93000000,,,estimate,src_ccrek_vl_leraren_begeleiding_2026,medium,CoA: 2026-27 total AVB ~3x intro (~93m class if 3*31); tick553",
    # Professionalization
    "bud_vl_prof_total_2020,vlaanderen_gov,2020,50800000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,Teacher professionalization total 50.8m 2020; tick553",
    "bud_vl_prof_total_2021,vlaanderen_gov,2021,54200000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,Prof total 54.2m 2021; tick553",
    "bud_vl_prof_total_2022,vlaanderen_gov,2022,59200000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,Prof total 59.2m 2022; tick553",
    "bud_vl_prof_total_2023,vlaanderen_gov,2023,64900000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,Prof total 64.9m 2023 peak; tick553",
    "bud_vl_prof_total_2024,vlaanderen_gov,2024,61800000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,Prof total 61.8m 2024; tick553",
    "bud_vl_prof_total_2025,vlaanderen_gov,2025,62400000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,Prof total 62.4m 2025 (schools 44.9 + PBD 17.5); tick553",
    "bud_vl_prof_schools_2025,vlaanderen_gov,2025,44900000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,School nascholingsmiddelen 44.9m 2025; tick553",
    "bud_vl_prof_pbd_2025,vlaanderen_gov,2025,17500000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,PBD pedagogical guidance services total budget 17.5m 2025; tick553",
    "bud_vl_prof_priority_themes_2020,vlaanderen_gov,2020,10300000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,Priority themes VR 10.3m 2020; zero 2025-27 path; tick553",
    "bud_vl_leerpunt_2022,vlaanderen_gov,2022,110000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,Leerpunt 0.11m 2022; tick553",
    "bud_vl_leerpunt_2025,vlaanderen_gov,2025,5700000,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,Leerpunt 5.7m 2025 (startup+annual+special); tick553",
    "bud_vl_prof_per_relation_eur,vlaanderen_gov,2025,125,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,Professionalization 120-130 EUR per organieke betrekking (amount=125 midpoint); tick553",
    "bud_vl_specialist_mandates_2024_25,vlaanderen_gov,2025,577,,,budgeted,src_ccrek_vl_leraren_begeleiding_2026,strong,Leraar-specialist mandates 203 basis+374 sec=577 underused 2024-25; tick553",
    # Combined stacks
    "bud_vl_avb_prof_stack_2025,vlaanderen_gov,2025,114600000,,,derived,src_ccrek_vl_leraren_begeleiding_2026,strong,Dual AVB 52.2 + prof 62.4 = 114.6m 2025 colored teacher PD class; tick553",
    "bud_dual_vl_avb_induct_2026,vlaanderen_gov,2026,100900000,,,derived,src_ccrek_vl_leraren_begeleiding_2026,medium,AVB path ~52 + induction 48.7 ~100.9m class overlapping envelopes; tick553",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_vl_avb_path_2019_27,Flanders teacher starter induction AVB budget path 2019-2027,vlaanderen_gov,Starter teachers schools,"
        "CoA 2026_35 + decreet TABD induction,2019-09-01,2019,2027,52200000,"
        '"{""intro_m"":31.0,""2024_25_m"":52.2,""basis_2025_m"":30.5,""sec_2025_m"":21.6,""induction_m"":48.7,'
        '""workings_alt_2025_26_m"":38.7,""triple_path_class_m"":93,""financing"":""pupil_not_starter_count"",'
        '""note"":""Strong CoA; mismatch needs; no global evaluation; mentor training only 60pct schools""}",'
        "0,active,docs/doge/data/raw/ccrek_2026_35_begeleiding_leraren.pdf,Ease practice shock retain starters,"
        "Starter-based financing FOI,src_ccrek_vl_leraren_begeleiding_2026,strong,Vlaanderen>Onderwijs>AVB_path,tick553"
    ),
    (
        "cmt_vl_prof_path_2020_25,Flanders teacher professionalization budget path 2020-2025,vlaanderen_gov,Teachers PBD Leerpunt,"
        "CoA 2026_35 Fig9 professionalization stack,2020-01-01,2020,2025,62400000,"
        '"{""total_2020_m"":50.8,""total_2025_m"":62.4,""schools_2025_m"":44.9,""pbd_2025_m"":17.5,""priority_vr_2025_m"":0,'
        '""leerpunt_2025_m"":5.7,""per_relation_eur"":""120-130"",""plans_missing_n"":8,""sample_n"":80,'
        '""note"":""Strong; plans weak budget planning 7/80; 1/3 spend off core teacher task""}",'
        "0,active,docs/doge/data/raw/ccrek_2026_35_begeleiding_leraren.pdf,Continuous teacher PD,"
        "Impact KPI FOI,src_ccrek_vl_leraren_begeleiding_2026,strong,Vlaanderen>Onderwijs>professionalisering,tick553"
    ),
    (
        "cmt_vl_induction_coherence_2026,Flanders starter measures coherence AVB+induction+bonus,vlaanderen_gov,Starter teachers,"
        "CoA Table1 parallel systems,2022-01-01,2022,2027,100900000,"
        '"{""systems"":[\"AVB\",\"induction\",\"lerarenbonus\"],\"coherence"":\"weak_parallel\",\"eval"":\"no_global\",'
        '""agodi_control"":\"no_colored_use_check\",\"note"":""Strong governance finding; cost-efficiency risk""}",'
        "0,active,docs/doge/data/raw/ccrek_2026_35_begeleiding_leraren.pdf,Coherent starter policy,"
        "Unified design FOI,src_ccrek_vl_leraren_begeleiding_2026,strong,Vlaanderen>Onderwijs>starter_coherence,tick553"
    ),
    (
        "cmt_dual_vl_fwb_teacher_pd,Dual VL teacher PD stack vs FWB edu personnel+IT,gg_belgium,Teachers multi-community,"
        "CoA VL 2026_35 + FWB 2026_31 dual,2019-01-01,2019,2026,0,"
        '"{""vl_avb_prof_2025_m"":114.6,""fwb_personnel_bn"":7.1,""fwb_cepage_m"":35.2,""note"":""not additive TE; dual PD architectures""}",'
        "0,active,docs/doge/data/raw/ccrek_2026_35_begeleiding_leraren.pdf,Honest dual teacher systems,"
        "Cross-community FOI,src_dual_vl_fwb_teacher_pd_tick553,strong,BE>dual>teacher_PD_VL_FWB,tick553"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_vl_avb_52m,VL starter induction AVB 52.2m 2024-25,regional,ops,Vlaanderen>Onderwijs>AVB_2025,52200000,52200000,Strong CoA path from 31m; pupil-based mismatch; no global eval,strong,src_ccrek_vl_leraren_begeleiding_2026,Starter teachers,Practice-shock relief,Financing design,6.0,6.5,4,5.95,Starter-based FOI,seed,,tick553",
    "lb_vl_induction_49m,VL induction units envelope 48.7m,regional,ops,Vlaanderen>Onderwijs>inductie,48700000,48700000,Strong not enough for 20pct all starters; equal split risk,strong,src_ccrek_vl_leraren_begeleiding_2026,Starters,Induction year,Coherence residual,6.5,6.5,5,6.20,Design FOI,seed,,tick553",
    "lb_vl_prof_62m,VL teacher professionalization 62.4m 2025,regional,ops,Vlaanderen>Onderwijs>professionalisering,62400000,62400000,Strong schools 44.9+PBD 17.5; plans weak; 1/3 off-core spend,strong,src_ccrek_vl_leraren_begeleiding_2026,Teachers,PD autonomy,Impact opaque,5.5,7.0,4,5.95,Impact FOI,seed,,tick553",
    "lb_vl_leerpunt_5_7m,Leerpunt evidence hub 5.7m 2025,regional,ops,Vlaanderen>Onderwijs>Leerpunt,5700000,5700000,Strong from 0.11m 2022; quality-framework role,strong,src_ccrek_vl_leraren_begeleiding_2026,Schools,Evidence-informed PD,Growth path,5.0,4.5,3,4.55,KPI FOI,seed,,tick553",
    "lb_vl_avb_prof_stack_115m,VL AVB+prof colored stack ~115m 2025,regional,ops,Vlaanderen>Onderwijs>PD_stack_2025,114600000,114600000,Strong dual AVB+prof; not full teacher policy,strong,src_ccrek_vl_leraren_begeleiding_2026,Teachers,Colored PD stack,Coherence gap,5.5,7.5,4,6.25,Unified FOI,seed,,tick553",
    "lb_vl_avb_triple_path,VL AVB budget triple path by 2026-27,regional,ops,Vlaanderen>Onderwijs>AVB_triple,93000000,93000000,Medium CoA order-of-magnitude 3x intro; induction adds,medium,src_ccrek_vl_leraren_begeleiding_2026,Taxpayers,Scale-up,Delivery residual,6.0,7.0,5,6.25,Outturn FOI,seed,,tick553",
    "lb_dual_vl_fwb_teacher_pd,Dual VL teacher PD vs FWB edu+IT,multi,ops,BE>dual>teacher_PD,114600000,7100000000,Strong dual different scales/failure modes,strong,src_dual_vl_fwb_teacher_pd_tick553,Teachers,Community dual,Honesty map,5.0,8.0,5,6.35,Cross FOI,seed,,tick553",
    "lb_vl_prof_plans_gap,VL professionalization plans quality gap,regional,ops,Vlaanderen>Onderwijs>prof_plans,0,0,Strong 8/80 no plan; budget planning 7/80; not euro stock,strong,src_ccrek_vl_leraren_begeleiding_2026,Schools,Governance,Accountability,7.5,3.0,3,5.55,Inspect FOI,seed,,tick553",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

foi = (
    f"gap_vl_avb_prof_outturn_l5,Vlaanderen>Onderwijs>AVB_prof>outturn_L5,vlaanderen_gov,"
    "Cash-by-year AVB by network/level 2019-2027; induction units use vs 48.7m envelope; "
    "AGODI control whether colored AVB hours used for starters; professionalization spend L5 sample; "
    "lerarenbonus budget path and uptake; global evaluation if any,"
    "CoA 2026_35: aggregates strong; use-of-funds and impact eval residual,"
    "7,Vlaamse overheid Team Openbaarheid / AGODI / Departement OV,openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,"
    "docs/doge/foi/drafts/gap_vl_avb_prof_outturn_l5.md,ready,2026-07-31,,,,"
    "cmt_vl_avb_path_2019_27|cmt_vl_prof_path_2020_25,"
    "lb_vl_avb_52m|lb_vl_prof_62m,"
    f"{now},{now},tick553 CoA filled; residual outturn human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq = root / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = "rq_544,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T09:05:00Z,,Spawned tick552 after tax measures+nonfiscal; next residual (new CoA PDF / residual dual); rq_116 deferred"
new = "rq_544,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T09:05:00Z,2026-07-31T09:10:00Z,tick553: CoA VL teacher AVB+prof L5; spawn rq_545; rq_116 deferred"
if old not in text:
    raise SystemExit("rq_544 not found")
text = text.replace(old, new)
if "rq_545," not in text:
    text = text.rstrip("\n") + "\n"
    text += "rq_545,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T09:10:00Z,,Spawned tick553 after VL teacher CoA; next residual CoA/PDF; rq_116 deferred\n"
rq.write_text(text, encoding="utf-8")
print("tick553 OK", len(buds))

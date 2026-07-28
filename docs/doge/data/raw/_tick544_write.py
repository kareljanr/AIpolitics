# tick544 — exposé employees global L5 benefits + RIZIV healthcare dual + assistance VI.1
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-29T10:00:00Z"

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_kamer_expose_ss_branches_2026,Kamer expose 2026 employees L5 Table II.2 + RIZIV IV.1 + assistance VI.1,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part IV Ch2-4-6,2026-07-29,primary_budget,"
        "Strong tick544: employees benefits L5 pensions 43.271 illness 14.879 unemp 4.638 FEDRIS 0.546 total 63.342; "
        "unemp -1.821bn YoY; transfer RIZIV 35.990; RIZIV benefits 41.297 financed RSZ 35.839 RSVZ 3.348; "
        "assistance leefloon +17.6pct to 2.085; TNW save path 118m; tick544\n"
    )
    f.write(
        "src_dual_riziv_rsz_financing_tick544,Dual RIZIV healthcare financed via RSZ-RSVZ global transfers,"
        "docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,DOGE synthesis Tables II.2+IV.1,2026-07-29,synthesis,"
        "Strong dual: employees table transfers 35.990 to RIZIV; RIZIV receives RSZ 35.839 + RSVZ 3.348 = 39.187; tick544\n"
    )

buds = [
    # Employees L5 benefits 2026 (from thousand EUR)
    "bud_ss_emp_illness_benefits_2026,sec_ss,2026,14879377000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table II.2 illness+invalidity benefits 14879.377m 2026; tick544",
    "bud_ss_emp_pensions_benefits_2026,sec_ss,2026,43270729000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table II.2 employee pensions benefits 43270.729m 2026; tick544",
    "bud_ss_emp_unemp_benefits_2026,sec_ss,2026,4637921000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table II.2 unemployment benefits 4637.921m 2026 (down from 6458.684 2025); tick544",
    "bud_ss_emp_unemp_benefits_2025,sec_ss,2025,6458684000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table II.1 unemployment benefits 6458.684m 2025; tick544",
    "bud_ss_fedris_ao_benefits_2026,sec_ss,2026,341105000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table II.2 FEDRIS work accidents benefits 341.105m 2026; tick544",
    "bud_ss_fedris_bz_benefits_2026,sec_ss,2026,204879000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table II.2 FEDRIS occupational diseases 204.879m 2026; tick544",
    "bud_ss_emp_illness_benefits_2025,sec_ss,2025,14206900000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Illness+invalidity benefits 14206.900m 2025; tick544",
    "bud_ss_emp_pensions_benefits_2025,sec_ss,2025,41799016000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Employee pensions 41799.016m 2025; tick544",
    "bud_ss_emp_admin_2026,sec_ss,2026,1478584000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Employees global admin 1478.584m 2026 (central 872.8 + third-party 605.8); tick544",
    "bud_ss_emp_thirdparty_admin_2026,sec_ss,2026,605819000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Employees third-party admin 605.819m 2026 (illness 386 + unemp 215); tick544",
    "bud_ss_emp_to_riziv_transfer_2026,sec_ss,2026,35990301000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table II.2 external transfer to RIZIV healthcare 35990.301m 2026; tick544",
    "bud_ss_emp_contrib_reductions_2026,sec_ss,2026,1196758000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table II.2 contribution reductions ESR 1196.758m 2026 (fed 879.5 + federated 317.2); tick544",
    # RIZIV Table IV.1
    "bud_riziv_benefits_2026,sec_ss,2026,41297169000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table IV.1 RIZIV healthcare benefits 41297.169m 2026; tick544",
    "bud_riziv_benefits_2025,sec_ss,2025,39812150000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table IV.1 RIZIV benefits 39812.150m 2025; tick544",
    "bud_riziv_admin_2026,sec_ss,2026,1236453000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,RIZIV admin 1236.453m 2026 (third-party mutualities 1115.8); tick544",
    "bud_riziv_thirdparty_admin_2026,sec_ss,2026,1115799000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,RIZIV third-party admin 1115.799m 2026; tick544",
    "bud_riziv_from_rsz_2026,sec_ss,2026,35839335000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table IV.1 transfer from RSZ global 35839.335m 2026 (base 28194 + additional 7645); tick544",
    "bud_riziv_from_rsvz_2026,sec_ss,2026,3347647000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table IV.1 transfer from RSVZ global 3347.647m 2026; tick544",
    "bud_riziv_total_rec_2026,sec_ss,2026,46753116000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table IV.1 RIZIV total current receipts 46753.116m 2026 (balanced exp); tick544",
    "bud_riziv_own_rec_2026,sec_ss,2026,7212173000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,RIZIV own receipts 7212.173m 2026 (contrib 1918 + grants 835 + assigned 1936 + divers 2519); tick544",
    # Policy measures
    "bud_tnw_wave4_save_illness_2026,sec_ss,2026,118153000,,,budgeted,src_kamer_expose_ss_branches_2026,medium,TNW wave4 reinforced follow-up save path 118.153m less employee illness benefits (of 126m total impact); tick544",
    "bud_thematic_control_save_2026,sec_ss,2026,24720000,,,budgeted,src_kamer_expose_ss_branches_2026,medium,Thematic controls VI save 24.720m employee benefits; RIZIV extra controls 3.228m; tick544",
    # Assistance VI.1
    "bud_igo_benefits_2026,sec_ss,2026,1034642000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table VI.1 IGO/GRAPA benefits 1034.642m 2026 IB; tick544",
    "bud_leefloon_benefits_2026,sec_ss,2026,2085102000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table VI.1 leefloon/RIS 2085.102m 2026 (+17.60pct / +312.1m vs 2025 adj); excl Ukraine; tick544",
    "bud_handicap_benefits_2026,sec_ss,2026,3285541000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table VI.1 handicap allowances 3285.541m 2026 (+6.29pct / +194.5m); tick544",
    "bud_ocmw_1965_2026,sec_ss,2026,155778000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table VI.1 OCMW law 1965 grants 155.778m 2026 (-10.1pct); tick544",
    "bud_socassist_benefits_total_2026,sec_ss,2026,6561063000,,,budgeted,src_kamer_expose_ss_branches_2026,strong,Table VI.1 social assistance benefits total 6561.063m 2026 (+8.56pct); tick544",
    # Dual
    "bud_dual_unemp_drop_2025_26,sec_ss,2026,1820763000,,,derived,src_kamer_expose_ss_branches_2026,strong,Dual unemployment benefits drop 1820.763m 2025-26 (time-limit path class); tick544",
    "bud_dual_riziv_rsz_rsvz_financing,sec_ss,2026,39186982000,,,derived,src_dual_riziv_rsz_financing_tick544,strong,Dual RIZIV financed RSZ 35.839 + RSVZ 3.348 = 39.187bn of 46.753 total; tick544",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_ss_emp_benefits_l5_2026,Employees global benefits L5 by branch 2025-2026,sec_ss,Employees pensioners unemployed,"
        "Expose Table II.2 employees global excl healthcare,2026-01-28,2025,2026,63341987000,"
        '"{""total_2026_m"":63342.0,""pensions_2026_m"":43270.7,""illness_2026_m"":14879.4,""unemp_2026_m"":4637.9,'
        '""unemp_2025_m"":6458.7,""fedris_ao_2026_m"":341.1,""fedris_bz_2026_m"":204.9,""to_riziv_2026_m"":35990.3,'
        '""contrib_reductions_2026_m"":1196.8,""admin_2026_m"":1478.6,""note"":""Strong L5; unemp -1.82bn YoY""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Map employee SS benefit branches,"
        "Payment-channel FOI,src_kamer_expose_ss_branches_2026,strong,SS>Employees>benefits_L5_2026,tick544"
    ),
    (
        "cmt_riziv_healthcare_2025_26,RIZIV healthcare budget dual RSZ-RSVZ financing 2025-2026,sec_ss,Patients mutualities providers,"
        "Expose Table IV.1 healthcare,2026-01-28,2025,2026,46753116000,"
        '"{""benefits_2025_m"":39812.2,""benefits_2026_m"":41297.2,""admin_2026_m"":1236.5,""thirdparty_2026_m"":1115.8,'
        '""rsz_2026_m"":35839.3,""rsvz_2026_m"":3347.6,""own_2026_m"":7212.2,""total_2026_m"":46753.1,'
        '""note"":""Strong dual financing stack; balanced 2026""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Healthcare insurance budget,"
        "Provider L5 FOI,src_kamer_expose_ss_branches_2026,strong,SS>RIZIV>budget_2026,tick544"
    ),
    (
        "cmt_socassist_benefits_path_2025_26,Social assistance benefits path IGO leefloon handicap 2025-2026,sec_ss,Vulnerable households,"
        "Expose Table VI.1 assistance,2026-01-28,2025,2026,6561063000,"
        '"{""total_2026_m"":6561.1,""igo_2026_m"":1034.6,""leefloon_2026_m"":2085.1,""handicap_2026_m"":3285.5,'
        '""ocmw_1965_2026_m"":155.8,""leefloon_delta_pct"":17.6,""handicap_delta_pct"":6.29,'
        '""note"":""Strong; Ukraine aid outside leefloon in Ukraine provision""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Social assistance benefits,"
        "Caseload FOI,src_kamer_expose_ss_branches_2026,strong,SS>Assistance>benefits_2026,tick544"
    ),
    (
        "cmt_tnw_illness_save_path_2026,Return-to-work wave4 illness benefit save path 2026,sec_ss,LT sick workers,"
        "Expose Ch2 commentary TNW + thematic controls,2026-01-28,2026,2026,146101000,"
        '"{""tnw_total_impact_m"":126.0,""tnw_emp_benefits_save_m"":118.2,""thematic_vi_m"":24.7,'
        '""riziv_controls_m"":3.2,""note"":""Medium policy estimate not outturn""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Activate LT sick / control abuse,"
        "Delivery KPI FOI,src_kamer_expose_ss_branches_2026,medium,SS>Illness>TNW_save_2026,tick544"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_ss_emp_pensions_43_3bn,Employee pensions benefits 43.3bn 2026,federal,ops,SS>Employees>pensions_2026,43270729000,43270729000,Strong Table II.2 largest employee branch; +1.47bn YoY,strong,src_kamer_expose_ss_branches_2026,Pensioners,Employee pensions,Structural aging,3.0,9.5,7,6.2,Reform FOI,seed,,tick544",
    "lb_ss_emp_illness_14_9bn,Employee illness+invalidity 14.9bn 2026,federal,ops,SS>Employees>illness_2026,14879377000,14879377000,Strong +0.67bn YoY; TNW wave4 save path 118m class,strong,src_kamer_expose_ss_branches_2026,LT sick,Sickness invalidity,Activation dual,5.0,9.5,6,7.05,TNW delivery FOI,seed,,tick544",
    "lb_ss_unemp_4_64bn,Unemployment benefits 4.64bn 2026,federal,ops,SS>Employees>unemployment_2026,4637921000,4637921000,Strong dual: -1.82bn YoY from 6.46; UI time-limit path class,strong,src_kamer_expose_ss_branches_2026,Unemployed,UI benefits,Reform delivery,6.0,9.0,5,7.35,Caseload FOI,seed,,tick544",
    "lb_riziv_benefits_41_3bn,RIZIV healthcare benefits 41.3bn 2026,federal,ops,SS>RIZIV>benefits_2026,41297169000,41297169000,Strong Table IV.1 +1.49bn; dual RSZ/RSVZ financing 39.2bn,strong,src_dual_riziv_rsz_financing_tick544,Patients,Health benefits,Growth,4.0,9.5,6,6.75,Provider FOI,seed,,tick544",
    "lb_riziv_mutuality_admin_1_12bn,RIZIV third-party mutuality admin 1.12bn 2026,federal,ops,SS>RIZIV>thirdparty_admin,1115799000,1115799000,Strong: 90pct of RIZIV admin is third-party; dual payment organisms,strong,src_kamer_expose_ss_branches_2026,Mutualities,Admin channel,Opacity L5,6.5,7.5,5,6.95,Per-org FOI,seed,,tick544",
    "lb_leefloon_2_09bn_plus17pct,Leefloon RIS 2.09bn +17.6pct 2026,federal,ops,SS>Assistance>leefloon_2026,2085102000,2085102000,Strong Table VI.1 +312m; dual UI time-limit spillover class; excl Ukraine,strong,src_kamer_expose_ss_branches_2026,RIS beneficiaries,Min income,Rising caseload,6.5,8.0,5,7.15,Caseload FOI,seed,,tick544",
    "lb_dual_riziv_rsz_finance,Dual RIZIV via RSZ+RSVZ global 39.2bn,multi,ops,BE>dual>RIZIV_RSZ_finance,39186982000,46753116000,Strong dual: healthcare not free-standing; employees transfer 36.0 in II.2,strong,src_dual_riziv_rsz_financing_tick544,Multi,Healthcare financing architecture,Classic dual,5.5,9.5,5,7.15,Bridge FOI,seed,,tick544",
    "lb_unemp_drop_1_82bn,Unemployment benefit drop 1.82bn 2025-26,federal,ops,SS>Employees>unemp_drop,1820763000,1820763000,Strong dual: largest YoY benefit decline; reform delivery not free lunch if leefloon rises,strong,src_kamer_expose_ss_branches_2026,Unemployed,UI time-limit path,Spillover risk,7.0,8.0,5,7.4,Net fiscal FOI,seed,,tick544",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_unemp_leefloon_spillover_l5,SS>UI_time_limit>leefloon_spillover_L5,sec_ss,"
        "Caseload and cash bridge 2025-2027: unemployment benefit drop 1.82bn vs leefloon +0.31bn; "
        "persons moving UI to RIS; residual after UI time-limit; dual OCMW federal compensation,"
        "Reform fiscal net effect opaque without spillover matrix; material dual,7,"
        "RVA-ONEM / POD MI / FOD SZ / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_unemp_leefloon_spillover_l5.md,ready,2026-07-29,,,,,,"
        "cmt_ss_emp_benefits_l5_2026|lb_unemp_drop_1_82bn,2026-07-29T10:00:00Z,2026-07-29T10:00:00Z,"
        "tick544 human send; not sent\n"
    )

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
text = text.replace(
    "rq_535,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,",
    "rq_535,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,",
    1,
)
text = text.replace(
    "Spawned tick543 after Part IV socprot; next RIZIV/employees detail or new public hole; rq_116 deferred",
    "tick544: employees L5 + RIZIV dual + assistance; spawn rq_536; rq_116 deferred",
    1,
)
if "rq_536," not in text:
    text = text.rstrip("\n") + "\n"
    text += (
        "rq_536,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
        "2026-07-29T10:00:00Z,,Spawned tick544 after SS branch L5; next public residual outside exposé or self-emp/Ch7; rq_116 deferred\n"
    )
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_535,544,no,"
    "Tick544 employees L5 pensions 43.3 illness 14.9 unemp 4.64 (-1.82) RIZIV 41.3 dual RSZ; "
    "next prio5 rq_536; rq_116 SWA deferred.\n",
    encoding="utf-8",
)

print("OK tick544")
print("sources +2 budgets +", len(buds), "cmt +", len(cmts), "lb +", len(lbs))

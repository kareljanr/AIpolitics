# tick545 — exposé self-employed Table III.2 + public pensions VII.2 dual pension stack
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-29T10:15:00Z"

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_kamer_expose_self_pubpen_2026,Kamer expose 2026 self-employed III.2 + public pensions VII.2,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part IV Ch3+Ch7,2026-07-29,primary_budget,"
        "Strong tick545: self-emp benefits 7.012 (pensions 5.920 illness 1.070) transfer RIZIV 3.551; "
        "public pensions benefits 22.828: Treasury 17.016 HR Rail 1.569 solidary fund 2.891 parastatal 0.809 police 0.186; "
        "dual pension stack emp+self+public ~72.0bn; tick545\n"
    )
    f.write(
        "src_dual_pension_three_stacks_tick545,Dual pension benefits employees+self-emp+public three stacks 2026,"
        "docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,DOGE synthesis II.2+III.2+VII.2,2026-07-29,synthesis,"
        "Strong dual: emp pensions 43.271 + self 5.920 + public 22.828 = 72.019bn benefits; not additive TE without care; tick545\n"
    )

buds = [
    # Self-employed L5 2026
    "bud_ss_self_illness_benefits_2026,sec_ss,2026,1069980000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table III.2 self-emp illness+invalidity 1069.980m 2026; tick545",
    "bud_ss_self_pensions_benefits_2026,sec_ss,2026,5919922000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table III.2 self-emp pensions 5919.922m 2026; tick545",
    "bud_ss_self_bridging_2026,sec_ss,2026,15297000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table III.2 overbruggingsrecht/droit passerelle 15.297m 2026; tick545",
    "bud_ss_self_caregiver_2026,sec_ss,2026,6857000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table III.2 caregiver allowance 6.857m 2026; tick545",
    "bud_ss_self_benefits_total_2026,sec_ss,2026,7012055000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table III.2 self-emp total benefits 7012.055m 2026; tick545",
    "bud_ss_self_benefits_total_2025,sec_ss,2025,6803601000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table III.1 self-emp benefits 6803.601m 2025; tick545",
    "bud_ss_self_pensions_2025,sec_ss,2025,5781250000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Self-emp pensions 5781.250m 2025; tick545",
    "bud_ss_self_illness_2025,sec_ss,2025,1005271000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Self-emp illness 1005.271m 2025; tick545",
    "bud_ss_self_to_riziv_2026,sec_ss,2026,3550642000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table III.2 transfer to RIZIV healthcare 3550.642m 2026; dual RSVZ path; tick545",
    "bud_ss_self_admin_2026,sec_ss,2026,163567000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Self-emp admin 163.567m 2026; tick545",
    # Public pensions L5 2026
    "bud_pubpen_treasury_2026,sec_ss,2026,17015825000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.2 Treasury retirement+survivor pensions 17015.825m 2026; tick545",
    "bud_pubpen_treasury_2025,sec_ss,2025,16535404000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.1 Treasury pensions 16535.404m 2025; tick545",
    "bud_pubpen_hr_rail_2026,hr_rail,2026,1569278000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.2 HR Rail pensions benefits 1569.278m 2026; tick545",
    "bud_pubpen_solidary_fund_2026,sec_ss,2026,2890990000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.2 solidary local pension fund benefits 2890.990m 2026; tick545",
    "bud_pubpen_parastatal_2026,sec_ss,2026,808673000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.2 parastatal pensions 808.673m 2026; tick545",
    "bud_pubpen_fed_police_2026,sec_ss,2026,186375000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.2 federal police pensions 186.375m 2026; tick545",
    "bud_pubpen_direct_conv_2026,sec_ss,2026,160484000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.2 direct conventions pensions 160.484m 2026; tick545",
    "bud_pubpen_provident_2026,sec_ss,2026,58437000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.2 provident institution conventions 58.437m 2026; tick545",
    "bud_pubpen_war_comp_2026,sec_ss,2026,62500000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.2 compensation+war rents 62.500m 2026; tick545",
    "bud_pubpen_work_accident_2026,sec_ss,2026,62522000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.2 work-accident rents 62.522m 2026; tick545",
    "bud_pubpen_terror_war_civ_2026,sec_ss,2026,12436000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.2 civil war+terror victims 12.436m 2026; tick545",
    "bud_pubpen_benefits_total_2026,sec_ss,2026,22827520000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.2 public pension benefits total 22827.520m 2026; tick545",
    "bud_pubpen_benefits_total_2025,sec_ss,2025,22153085000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.1 public pension benefits 22153.085m 2025; tick545",
    "bud_pubpen_gov_grants_2025,sec_ss,2025,15912610000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.1 public subsidies to public pensions 15912.610m 2025; tick545",
    "bud_pubpen_contrib_2025,sec_ss,2025,7220580000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.1 contributions into public pension system 7220.580m 2025; tick545",
    "bud_pubpen_total_exp_2026,sec_ss,2026,24481410000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.2 public pensions total current exp 24481.410m 2026; tick545",
    "bud_pubpen_result_2026,sec_ss,2026,98305000,,,budgeted,src_kamer_expose_self_pubpen_2026,strong,Table VII.2 public pensions budgetary result +98.305m 2026; tick545",
    # Dual pension stack
    "bud_dual_pension_three_stacks_2026,sec_ss,2026,72019000000,,,derived,src_dual_pension_three_stacks_tick545,strong,Dual pension benefits emp 43.271 + self 5.920 + public 22.828 = 72.019bn 2026; tick545",
    "bud_dual_riziv_from_self_rsvz_2026,sec_ss,2026,3550642000,,,derived,src_kamer_expose_self_pubpen_2026,strong,Dual self-emp table to RIZIV 3.551 vs RSVZ path 3.348 in IV.1 residual class; tick545",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_ss_self_benefits_l5_2026,Self-employed global benefits L5 2025-2026,sec_ss,Self-employed pensioners,"
        "Expose Tables III.1-III.2 self-employed excl healthcare,2026-01-28,2025,2026,7012055000,"
        '"{""total_2026_m"":7012.1,""pensions_2026_m"":5919.9,""illness_2026_m"":1070.0,""bridging_2026_m"":15.3,'
        '""caregiver_2026_m"":6.9,""total_2025_m"":6803.6,""to_riziv_2026_m"":3550.6,""admin_2026_m"":163.6,'
        '""note"":""Strong L5; pensions dominate self-emp stack""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Map self-employed SS benefits,"
        "Residual FOI,src_kamer_expose_self_pubpen_2026,strong,SS>Self_employed>benefits_L5_2026,tick545"
    ),
    (
        "cmt_pubpen_l5_sectors_2026,Public-sector pensions L5 by employer sector 2025-2026,sec_ss,Public retirees FPD,"
        "Expose Tables VII.1-VII.2 public pensions,2026-01-28,2025,2026,22827520000,"
        '"{""benefits_2026_m"":22827.5,""benefits_2025_m"":22153.1,""treasury_2026_m"":17015.8,""treasury_2025_m"":16535.4,'
        '""hr_rail_2026_m"":1569.3,""solidary_2026_m"":2891.0,""parastatal_2026_m"":808.7,""police_2026_m"":186.4,'
        '""direct_2026_m"":160.5,""total_exp_2026_m"":24481.4,""result_2026_m"":98.3,'
        '""note"":""Strong dual multi-employer; Treasury + education/C&R staff class""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Map public pension sectors,"
        "Employer L5 FOI,src_kamer_expose_self_pubpen_2026,strong,SS>Public_pensions>L5_2026,tick545"
    ),
    (
        "cmt_pension_three_stack_2026,Triple pension benefit stack employees self public 2026,sec_ss,All pensioners,"
        "Expose II.2+III.2+VII.2 dual synthesis,2026-01-28,2026,2026,72019000000,"
        '"{""emp_pensions_m"":43270.7,""self_pensions_m"":5919.9,""public_benefits_m"":22827.5,""sum_m"":72018.1,'
        '""note"":""Strong dual; do not sum into TE pie without labels; healthcare pensions separate""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Unified pension mass map,"
        "Aging reform FOI,src_dual_pension_three_stacks_tick545,strong,SS>Pensions>three_stacks_2026,tick545"
    ),
    (
        "cmt_hr_rail_pensions_2026,HR Rail public pension benefits dual rail 2026,hr_rail,HR Rail retirees,"
        "Expose Table VII.2 HR Rail column,2026-01-28,2026,2026,1569278000,"
        '"{""benefits_2026_m"":1569.3,""benefits_2025_m"":1522.2,""note"":""Strong dual rail employer pensions off NMBS D.31""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Rail staff pensions,"
        "Dual NMBS FOI,src_kamer_expose_self_pubpen_2026,strong,SS>Public_pensions>HR_Rail_2026,tick545"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_ss_self_pensions_5_92bn,Self-employed pensions 5.92bn 2026,federal,ops,SS>Self_employed>pensions_2026,5919922000,5919922000,Strong Table III.2; +139m YoY; dual emp 43.3 public 22.8,strong,src_kamer_expose_self_pubpen_2026,Self-emp retirees,Self-emp pensions,Structural,3.5,9.0,6,6.35,Reform FOI,seed,,tick545",
    "lb_ss_self_illness_1_07bn,Self-employed illness 1.07bn 2026,federal,ops,SS>Self_employed>illness_2026,1069980000,1069980000,Strong +65m YoY; dual emp illness 14.9,strong,src_kamer_expose_self_pubpen_2026,Self-emp,Sickness invalidity,Smaller stack,4.0,7.5,5,5.85,TNW FOI,seed,,tick545",
    "lb_pubpen_treasury_17_0bn,Treasury public pensions 17.0bn 2026,federal,ops,SS>Public_pensions>Treasury_2026,17015825000,17015825000,Strong Table VII.2 largest public sector; +480m YoY; dual fed grant path,strong,src_kamer_expose_self_pubpen_2026,Civil servants military teachers class,Treasury pensions,Core public,3.0,9.5,7,6.2,Statuut FOI,seed,,tick545",
    "lb_pubpen_solidary_2_89bn,Solidary local pension fund 2.89bn 2026,federal,ops,SS>Public_pensions>solidary_2026,2890990000,2890990000,Strong dual local authorities pension fund via federal table,strong,src_kamer_expose_self_pubpen_2026,Local public retirees,Solidary fund,Dual local-fed,5.0,8.0,5,6.55,Commune FOI,seed,,tick545",
    "lb_pubpen_hr_rail_1_57bn,HR Rail pensions 1.57bn 2026,federal,ops,SS>Public_pensions>HR_Rail,1569278000,1569278000,Strong dual rail pensions off pure NMBS PSO path,strong,src_kamer_expose_self_pubpen_2026,Rail retirees,HR Rail pensions,Dual rail stack,5.5,8.0,5,6.75,Dual FOI,seed,,tick545",
    "lb_pubpen_total_22_8bn,Public pensions benefits total 22.8bn 2026,federal,ops,SS>Public_pensions>total_2026,22827520000,22827520000,Strong multi-sector; +0.67bn YoY; result +98m,strong,src_kamer_expose_self_pubpen_2026,Public retirees,Public pension system,Structural,3.0,9.5,6,6.45,Sector FOI,seed,,tick545",
    "lb_dual_pension_72bn,Dual three-stack pensions 72.0bn 2026,multi,ops,BE>dual>pensions_three_stacks,72019000000,72019000000,Strong dual emp 43.3 + self 5.9 + public 22.8; aging north star,strong,src_dual_pension_three_stacks_tick545,All pensioners,Pension architecture,Core social mass,4.5,9.5,6,6.95,Unified map FOI,seed,,tick545",
    "lb_ss_self_to_riziv_3_55bn,Self-emp transfer to RIZIV 3.55bn 2026,federal,ops,SS>Self_employed>to_RIZIV,3550642000,3550642000,Strong dual healthcare financing from self-emp global; RSVZ path,strong,src_kamer_expose_self_pubpen_2026,Patients,Healthcare financing,Dual RIZIV,4.0,8.0,5,6.15,Bridge FOI,seed,,tick545",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_pubpen_employer_l5,SS>Public_pensions>employer_L5,sec_ss,"
        "L5 split of Treasury public pensions 17.0bn 2026 by employer class (federal admin military education "
        "C&R ministries bpost Proximus former gendarmerie judicial police); solidary fund commune matrix; "
        "HR Rail reconcile with NMBS/Infrabel staff dual,"
        "Public pension stack multi-employer; education vs federal opacity material,6,"
        "Federale Pensioendienst / BOSA / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_pubpen_employer_l5.md,ready,2026-07-29,,,,,,"
        "cmt_pubpen_l5_sectors_2026|lb_pubpen_treasury_17_0bn,2026-07-29T10:15:00Z,2026-07-29T10:15:00Z,"
        "tick545 human send; not sent\n"
    )

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
text = text.replace(
    "rq_536,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,",
    "rq_536,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,",
    1,
)
text = text.replace(
    "Spawned tick544 after SS branch L5; next public residual outside exposé or self-emp/Ch7; rq_116 deferred",
    "tick545: self-emp L5 + public pensions dual; spawn rq_537; rq_116 deferred",
    1,
)
if "rq_537," not in text:
    text = text.rstrip("\n") + "\n"
    text += (
        "rq_537,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
        "2026-07-29T10:15:00Z,,Spawned tick545 after self-emp+pubpen; exposé Part IV largely filled; next new public residual; rq_116 deferred\n"
    )
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_536,545,no,"
    "Tick545 self-emp pensions 5.92 illness 1.07; pubpen Treasury 17.0 solidary 2.89 HR Rail 1.57 total 22.8; "
    "dual pensions 72.0; next prio5 rq_537; rq_116 SWA deferred.\n",
    encoding="utf-8",
)

print("OK tick545")
print("sources +2 budgets +", len(buds), "cmt +", len(cmts), "lb +", len(lbs))

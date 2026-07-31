# tick546 — exposé Part IV Ch5 "andere stelsels" Tables V.1-V.2 L5 dual
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T08:35:00Z"

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_kamer_expose_other_ss_2026,Kamer expose 2026 other SS schemes Tables V.1-V.2,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part IV Ch5,2026-07-31,primary_budget,"
        "Strong tick546: other schemes total rec 1645.1/1568.6m exp 1522.2/1569.9m 2025-26; benefits 1098.8/1013.6m; "
        "L5 FSO 438.1/319.9 Ex-OSZ 330.4/336.0 RVA emp 235.4/261.4 medical 37.0/37.6 asbestos 22.6/23.4; "
        "fed toelagen 454.0/463.5 dual I.3; FSO periodisation +113m 2025; asbestos 3Q employer 2026; tick546\n"
    )
    f.write(
        "src_dual_other_ss_i3_tick546,Dual other-SS federal means Table I.3 vs V.1-V.2,"
        "docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,DOGE synthesis I.3+V.1+V.2,2026-07-31,synthesis,"
        "Strong dual: I.3 Andere stelsels fed 454.041/463.463m equals V.1/V.2 federal toelagen totals; tick546\n"
    )

# amounts in EUR (tables in thousand EUR)
buds = [
    # Totals
    "bud_other_ss_rec_2025,sec_ss,2025,1645062000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 other SS total current receipts 1645.062m 2025; tick546",
    "bud_other_ss_exp_2025,sec_ss,2025,1522198000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 other SS total current exp 1522.198m 2025; tick546",
    "bud_other_ss_result_2025,sec_ss,2025,122864000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 other SS current result +122.864m 2025; tick546",
    "bud_other_ss_rec_2026,sec_ss,2026,1568649000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 other SS total current receipts 1568.649m 2026; tick546",
    "bud_other_ss_exp_2026,sec_ss,2026,1569855000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 other SS total current exp 1569.855m 2026; tick546",
    "bud_other_ss_result_2026,sec_ss,2026,-1206000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 other SS current result -1.206m 2026 (vs +122.9m 2025); tick546",
    "bud_other_ss_benefits_2025,sec_ss,2025,1098806000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 other SS benefits 1098.806m 2025; tick546",
    "bud_other_ss_benefits_2026,sec_ss,2026,1013554000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 other SS benefits 1013.554m 2026 (-85.3m YoY); tick546",
    "bud_other_ss_admin_2025,sec_ss,2025,44388000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 other SS admin 44.388m 2025; tick546",
    "bud_other_ss_admin_2026,sec_ss,2026,44632000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 other SS admin 44.632m 2026; tick546",
    "bud_other_ss_contrib_2025,sec_ss,2025,592570000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 other SS contributions 592.570m 2025; tick546",
    "bud_other_ss_contrib_2026,sec_ss,2026,619065000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 other SS contributions 619.065m 2026; tick546",
    "bud_other_ss_fed_toelage_2025,sec_ss,2025,454041000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 federal toelagen other SS 454.041m 2025 dual I.3; tick546",
    "bud_other_ss_fed_toelage_2026,sec_ss,2026,463463000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 federal toelagen other SS 463.463m 2026 dual I.3; tick546",
    "bud_other_ss_fed_entities_toelage_2025,sec_ss,2025,55676000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 federated-entity share (RVA emp dual) 55.676m 2025; tick546",
    "bud_other_ss_fed_entities_toelage_2026,sec_ss,2026,60551000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 federated-entity share 60.551m 2026; tick546",
    "bud_other_ss_divers_exp_2025,sec_ss,2025,220291000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 divers exp 220.291m 2025 (FSO-heavy); tick546",
    "bud_other_ss_divers_exp_2026,sec_ss,2026,354803000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 divers exp 354.803m 2026 (+134.5m FSO class); tick546",
    # L5 benefits 2025
    "bud_fedris_ao_cap_benefits_2025,fedris,2025,15413000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 Fedris-AO capitalisation benefits 15.413m 2025; tick546",
    "bud_asbestos_benefits_2025,fedris,2025,22615000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 asbestos fund benefits 22.615m 2025; tick546",
    "bud_fedris_ppo_benefits_2025,fedris,2025,14924000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 Fedris-BZ PPO/APL sector benefits 14.924m 2025; tick546",
    "bud_ex_osz_benefits_2025,sec_ss,2025,330434000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 RSZ Ex-OSZ overseas SS benefits 330.434m 2025; tick546",
    "bud_rva_emp_missions_benefits_2025,sec_ss,2025,235356000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 RVA employment-missions benefits 235.356m 2025 (fed+entities dual); tick546",
    "bud_medical_accidents_benefits_2025,sec_ss,2025,37000000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 medical accidents fund benefits 37.000m 2025; tick546",
    "bud_war_terror_benefits_2025,sec_ss,2025,4961000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 war+terror victims benefits 4.961m 2025; tick546",
    "bud_fso_benefits_2025,fso,2025,438103000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.1 FSO enterprise-closure benefits 438.103m 2025; periodisation +113m Q1-26 class; tick546",
    # L5 benefits 2026
    "bud_fedris_ao_cap_benefits_2026,fedris,2026,15368000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 Fedris-AO capitalisation benefits 15.368m 2026; tick546",
    "bud_asbestos_benefits_2026,fedris,2026,23415000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 asbestos fund benefits 23.415m 2026; 3Q employer contrib; tick546",
    "bud_fedris_ppo_benefits_2026,fedris,2026,15219000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 Fedris-BZ PPO/APL benefits 15.219m 2026; tick546",
    "bud_ex_osz_benefits_2026,sec_ss,2026,335960000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 RSZ Ex-OSZ overseas SS benefits 335.960m 2026; tick546",
    "bud_rva_emp_missions_benefits_2026,sec_ss,2026,261422000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 RVA employment-missions benefits 261.422m 2026; tick546",
    "bud_medical_accidents_benefits_2026,sec_ss,2026,37566000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 medical accidents fund benefits 37.566m 2026; tick546",
    "bud_war_terror_benefits_2026,sec_ss,2026,4694000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 war+terror victims benefits 4.694m 2026; tick546",
    "bud_fso_benefits_2026,fso,2026,319910000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 FSO benefits 319.910m 2026 (-118m vs 2025 periodisation class); tick546",
    # Scheme total exp 2026
    "bud_fso_total_exp_2026,fso,2026,823746000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 FSO total current exp 823.746m 2026 (benefits+divers+admin+ext); tick546",
    "bud_ex_osz_total_exp_2026,sec_ss,2026,352589000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 Ex-OSZ total current exp 352.589m 2026; tick546",
    "bud_rva_emp_missions_total_exp_2026,sec_ss,2026,261422000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 RVA emp missions total exp 261.422m 2026 (=benefits line); tick546",
    "bud_medical_accidents_total_exp_2026,sec_ss,2026,48782000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 medical accidents total exp 48.782m 2026; tick546",
    "bud_asbestos_total_exp_2026,fedris,2026,24973000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 asbestos fund total exp 24.973m 2026; tick546",
    "bud_fedris_ao_cap_total_exp_2026,fedris,2026,31699000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Table V.2 Fedris-AO capitalisation total exp 31.699m 2026; tick546",
    # Policy deltas
    "bud_fso_periodisation_q1_impact_2025,fso,2025,113007000,,,budgeted,src_kamer_expose_other_ss_2026,strong,FSO CoA periodisation incl Q1 N+1 impact 113.007m on 2025 benefits (58.5pct of FSO rise); tick546",
    "bud_medical_riziv_dot_uplift_2025,sec_ss,2025,20376000,,,budgeted,src_kamer_expose_other_ss_2026,strong,RIZIV dotatie uplift to medical accidents fund +20.376m 2025 arrears path; tick546",
    "bud_asbestos_fed_toelage_delta_2026,fedris,2026,-3742000,,,budgeted,src_kamer_expose_other_ss_2026,strong,Asbestos federal toelage -3.742m 2026 vs 2025 (3Q employer contrib offset); tick546",
    "bud_rva_career_break_save_fed_2026,sec_ss,2026,4690000,,,budgeted,src_kamer_expose_other_ss_2026,medium,RVA career-break harmonisation save path 4.690m 2026 federal emp-missions share; policy est; tick546",
    # Dual I.3
    "bud_dual_other_ss_fed_i3_2025,sec_ss,2025,454041000,,,derived,src_dual_other_ss_i3_tick546,strong,Dual I.3 Andere stelsels fed means 454.041m = V.1 federal toelagen; tick546",
    "bud_dual_other_ss_fed_i3_2026,sec_ss,2026,463463000,,,derived,src_dual_other_ss_i3_tick546,strong,Dual I.3 Andere stelsels fed means 463.463m = V.2 federal toelagen; tick546",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_other_ss_l5_package_2025_26,Other SS schemes L5 package Tables V.1-V.2 2025-2026,sec_ss,Mixed SS beneficiaries,"
        "Expose Part IV Ch5 Tables V.1-V.2 eight schemes,2026-01-28,2025,2026,1569855000,"
        '"{""rec_2025_m"":1645.1,""exp_2025_m"":1522.2,""result_2025_m"":122.9,""rec_2026_m"":1568.6,""exp_2026_m"":1569.9,'
        '""result_2026_m"":-1.2,""benefits_2025_m"":1098.8,""benefits_2026_m"":1013.6,""fed_toelage_2026_m"":463.5,'
        '""fso_ben_2025_m"":438.1,""fso_ben_2026_m"":319.9,""ex_osz_2026_m"":336.0,""rva_emp_2026_m"":261.4,'
        '""note"":""Strong primary; residual case-level L5 FOI""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Map residual SS schemes outside global management,"
        "Case L5 FOI,src_kamer_expose_other_ss_2026,strong,SS>Other_schemes>L5_package_2026,tick546"
    ),
    (
        "cmt_fso_periodisation_path_2025_26,FSO enterprise-closure fund periodisation + benefits path,fso,Closure victims,"
        "Expose Ch5 + CoA periodisation recommendation,2026-01-28,2025,2026,823746000,"
        '"{""benefits_2025_m"":438.1,""benefits_2026_m"":319.9,""total_exp_2026_m"":823.7,""q1_period_impact_2025_m"":113.0,'
        '""divers_exp_2026_m"":352.0,""result_2025_m"":115.9,""result_2026_m"":-9.7,'
        '""note"":""Strong; divers line opaque vs benefits; dual prior FSO JV rows""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Closure fund cash mapping,"
        "Top closures FOI,src_kamer_expose_other_ss_2026,strong,SS>FSO>periodisation_2025_26,tick546"
    ),
    (
        "cmt_ex_osz_overseas_ss_2026,RSZ Ex-OSZ overseas social security benefits path,sec_ss,Overseas SS beneficiaries,"
        "Expose Table V.2 Ex-OSZ column,2026-01-28,2025,2026,352589000,"
        '"{""benefits_2025_m"":330.4,""benefits_2026_m"":336.0,""total_exp_2026_m"":352.6,""fed_toelage_class"":""~275m class 2026"","'
        '""note"":""Strong aggregate; geography/beneficiary L5 residual""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Overseas SS residual map,"
        "Geo L5 FOI,src_kamer_expose_other_ss_2026,strong,SS>Ex_OSZ>benefits_2026,tick546"
    ),
    (
        "cmt_rva_emp_missions_dual_2026,RVA employment-missions dual federal+federated path,sec_ss,Career-break / employment schemes,"
        "Expose V.1-V.2 RVA tewerkstellingsopdrachten,2026-01-28,2025,2026,261422000,"
        '"{""benefits_2025_m"":235.4,""benefits_2026_m"":261.4,""fed_share_2025_m"":179.7,""entities_2025_m"":55.7,'
        '""entities_2026_m"":60.6,""career_break_save_fed_2026_m"":4.7,'
        '""note"":""Strong dual fed/entities; career-break harmonisation medium save path""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Employment-missions dual map,"
        "Scheme L5 FOI,src_kamer_expose_other_ss_2026,strong,SS>RVA>employment_missions_2026,tick546"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_other_ss_total_1_57bn,Other SS schemes total exp 1.57bn 2026,federal,ops,SS>Other_schemes>total_2026,1569855000,1569855000,Strong Table V.2 eight residual schemes; result ~0; dual I.3 fed 463m,strong,src_kamer_expose_other_ss_2026,Mixed,Residual SS architecture,Completes Part IV map,4.0,8.0,5,6.20,Case FOI,seed,,tick546",
    "lb_fso_total_824m,FSO enterprise-closure total exp 824m 2026,federal,ops,SS>FSO>total_2026,823746000,823746000,Strong V.2; benefits 320m + divers 352m class; periodisation swing; prior JV dual,strong,src_kamer_expose_other_ss_2026,Closure victims,Wage guarantee on insolvency,Accounting opacity divers,6.0,8.0,5,6.80,Top-closure FOI,seed,,tick546",
    "lb_fso_benefits_438m_2025,FSO benefits 438m 2025 peak periodisation,federal,ops,SS>FSO>benefits_2025,438103000,438103000,Strong V.1; +113m Q1-26 periodisation 58.5pct of rise,strong,src_kamer_expose_other_ss_2026,Closure victims,Insolvency benefits,One-off accounting,5.5,7.5,5,6.35,CoA dual,seed,,tick546",
    "lb_ex_osz_336m,Ex-OSZ overseas SS benefits 336m 2026,federal,ops,SS>Ex_OSZ>benefits_2026,335960000,335960000,Strong residual overseas stack outside RSZ global,strong,src_kamer_expose_other_ss_2026,Overseas beneficiaries,Overseas social protection,Geo L5 thin,5.0,7.5,5,6.25,Geo FOI,seed,,tick546",
    "lb_rva_emp_missions_261m,RVA employment-missions 261m 2026 dual,federal,ops,SS>RVA>employment_missions_2026,261422000,261422000,Strong dual fed+entities; career-break path class,strong,src_kamer_expose_other_ss_2026,Career-break users,Employment missions,Dual C&R share,4.5,7.5,5,6.15,Scheme FOI,seed,,tick546",
    "lb_medical_accidents_48m,Medical accidents fund total 49m 2026,federal,ops,SS>Medical_accidents>2026,48782000,48782000,Strong; RIZIV dot uplift +20.4m 2025 arrears path; benefits ~38m,strong,src_kamer_expose_other_ss_2026,Medical injury victims,No-fault medical,Case stock opaque,5.5,6.0,4,5.85,Case FOI,seed,,tick546",
    "lb_asbestos_fund_25m,Asbestos fund total exp 25m 2026,federal,ops,SS>Asbestos_fund>2026,24973000,24973000,Strong; 3Q employer contrib 2026; fed toelage -3.7m,strong,src_kamer_expose_other_ss_2026,Asbestos victims,Asbestos compensation,Financing rebalance,4.0,5.5,4,5.05,Fund FOI,seed,,tick546",
    "lb_dual_other_ss_fed_463m,Dual other-SS federal means 463m 2026,federal,ops,SS>Other_schemes>fed_toelage_2026,463463000,463463000,Strong dual I.3=V.2 federal toelagen; not full scheme exp,strong,src_dual_other_ss_i3_tick546,Taxpayers,Federal residual SS finance,Perimeter map,4.0,7.5,4,5.95,Bridge FOI,seed,,tick546",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

# FOI queue row
foi = (
    f"gap_other_ss_l5_detail,SS>Other_schemes>case_L5,sec_ss,"
    "Case-level and cash-code L5 for FSO top closures 2023-2026; medical-accidents case stock/paid; "
    "Ex-OSZ beneficiary geography; dual Fedris capitalisation vs employees-global FEDRIS; divers-line map FSO,"
    "Aggregates V.1-V.2 now public strong; end-receiver and divers opacity material for ~1.57bn package,"
    "6,FOD Sociale Zekerheid / RSZ / RVA-FSO / FEDRIS / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_other_ss_l5_detail.md,ready,2026-07-31,,,,"
    "cmt_other_ss_l5_package_2025_26|cmt_fso_periodisation_path_2025_26,"
    "lb_fso_total_824m|lb_other_ss_total_1_57bn,"
    f"{now},{now},tick546: Tables V.1-V.2 filled; residual case L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

# research_queue: mark rq_537 done; spawn rq_538
rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = "rq_537,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-29T10:15:00Z,,Spawned tick545 after self-emp+pubpen; exposé Part IV largely filled; next new public residual; rq_116 deferred"
new = "rq_537,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-29T10:15:00Z,2026-07-31T08:35:00Z,tick546: other SS Ch5 V.1-V.2 L5 package 1.57bn; spawn rq_538; rq_116 deferred"
if old not in text:
    raise SystemExit("rq_537 row not found for update")
text = text.replace(old, new)
# append spawn
if "rq_538," not in text:
    text = text.rstrip("\n") + "\n"
    text += "rq_538,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,2026-07-31T08:35:00Z,,Spawned tick546 after other-SS Ch5; Part IV complete class; next public residual (Part I aging / primary residual / new PDF); rq_116 deferred\n"
rq_path.write_text(text, encoding="utf-8")

print("tick546 write OK: budgets", len(buds), "cmt", len(cmts), "lb", len(lbs))

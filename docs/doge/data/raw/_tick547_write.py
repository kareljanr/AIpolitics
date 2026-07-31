# tick547 — exposé Part I §5 Table 40 Entity I global investment effort 2025-2029
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-31T08:40:00Z"

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_kamer_expose_invest_e1_2026,Kamer expose 2026 Entity I global investment effort Table 40,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part I §5 Table40,2026-07-31,primary_budget,"
        "Strong tick547: E1 invest path 2025-29 direct 4.522/5.174/5.740/5.924/6.082bn; ESA GCF 5.914/6.612/7.204/7.438/7.632bn; "
        "gov-supported 6.962/7.706/7.980/8.135/8.344bn (1.1-1.2pct GDP); FOD 2.972/4.962 defence-driven; ESA def corr 175/-1388m; "
        "ION 1.324/1.559; NMBS invest aid 1.049/1.094; Infrabel+NIRAS act 455 flat; IT act 638/657; science 327/336; tick547\n"
    )
    f.write(
        "src_dual_invest_e1_consol_tick547,Dual E1 invest Table40 vs consol ION invest Ch5,"
        "docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,DOGE synthesis Table40 + Part III Ch5,2026-07-31,synthesis,"
        "Strong dual: Table40 ION invest 1559m 2026 vs consol orgs invest line 15.6pct of 9976m exp; NMBS invest aid dual rail package; tick547\n"
    )

# EUR (table in million)
buds = [
    # Direct public investments path
    "bud_e1_fod_invest_2025,sec_federal,2025,2972000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 FOD/POD invest codes7 2972m 2025; tick547",
    "bud_e1_fod_invest_2026,sec_federal,2026,4962000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 FOD/POD invest 4962m 2026 defence-driven spike; tick547",
    "bud_e1_fod_invest_2027,sec_federal,2027,4496000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 FOD/POD invest 4496m 2027; tick547",
    "bud_e1_fod_invest_2028,sec_federal,2028,4748000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 FOD/POD invest 4748m 2028; tick547",
    "bud_e1_fod_invest_2029,sec_federal,2029,4815000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 FOD/POD invest 4815m 2029; tick547",
    "bud_e1_def_esa_corr_2025,mod_defensie,2025,175000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 ESA correction defence invest +175m 2025; tick547",
    "bud_e1_def_esa_corr_2026,mod_defensie,2026,-1388000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 ESA correction defence invest -1388m 2026 (cash vs ESA timing); tick547",
    "bud_e1_def_esa_corr_2027,mod_defensie,2027,-150000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 ESA defence invest corr -150m 2027; tick547",
    "bud_e1_def_esa_corr_2028,mod_defensie,2028,-220000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 ESA defence invest corr -220m 2028; tick547",
    "bud_e1_def_esa_corr_2029,mod_defensie,2029,-109000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 ESA defence invest corr -109m 2029; tick547",
    "bud_e1_ion_invest_2025,sec_federal,2025,1324000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 ION/OIP invest 1324m 2025 (Infrabel+Regie class); tick547",
    "bud_e1_ion_invest_2026,sec_federal,2026,1559000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 ION/OIP invest 1559m 2026 dual consol; tick547",
    "bud_e1_ion_invest_2027,sec_federal,2027,1360000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 ION invest 1360m 2027; tick547",
    "bud_e1_ion_invest_2028,sec_federal,2028,1361000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 ION invest 1361m 2028; tick547",
    "bud_e1_ion_invest_2029,sec_federal,2029,1342000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 ION invest 1342m 2029; tick547",
    "bud_e1_oisz_invest_2025,sec_ss,2025,51000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 OISZ invest 51m 2025; tick547",
    "bud_e1_oisz_invest_2026,sec_ss,2026,40000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 OISZ invest 40m 2026; tick547",
    "bud_e1_direct_public_invest_2025,sec_federal,2025,4522000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 total direct public invest 4522m 2025; tick547",
    "bud_e1_direct_public_invest_2026,sec_federal,2026,5174000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 total direct public invest 5174m 2026; tick547",
    "bud_e1_direct_public_invest_2027,sec_federal,2027,5740000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 total direct public invest 5740m 2027; tick547",
    "bud_e1_direct_public_invest_2028,sec_federal,2028,5924000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 total direct public invest 5924m 2028; tick547",
    "bud_e1_direct_public_invest_2029,sec_federal,2029,6082000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 total direct public invest 6082m 2029; tick547",
    # ESA gross capital formation bridge
    "bud_e1_science_act_2026,sec_federal,2026,336000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 science-policy activation 336m 2026 (3pct growth from 2024 INR); tick547",
    "bud_e1_it_act_fod_2026,sec_federal,2026,657000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 IT activation FOD/POD/ION 657m 2026; tick547",
    "bud_e1_it_act_oisz_2026,sec_ss,2026,40000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 IT activation OISZ 40m 2026; tick547",
    "bud_e1_infrabel_niras_act_2026,sec_federal,2026,455000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 Infrabel+NIRAS invest activation 455m flat 2025-29; tick547",
    "bud_e1_desinvest_fod_2026,sec_federal,2026,-16000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 FOD desinvest -16m 2026; tick547",
    "bud_e1_desinvest_ion_2026,sec_federal,2026,-34000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 ION desinvest -34m 2026; tick547",
    "bud_e1_gcf_esa_2025,sec_federal,2025,5914000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 gross capital formation ESA 5914m 2025; tick547",
    "bud_e1_gcf_esa_2026,sec_federal,2026,6612000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 gross capital formation ESA 6612m 2026; tick547",
    "bud_e1_gcf_esa_2027,sec_federal,2027,7204000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 gross capital formation ESA 7204m 2027; tick547",
    "bud_e1_gcf_esa_2028,sec_federal,2028,7438000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 gross capital formation ESA 7438m 2028; tick547",
    "bud_e1_gcf_esa_2029,sec_federal,2029,7632000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 gross capital formation ESA 7632m 2029; tick547",
    # Investment aid NMBS + gov-supported total
    "bud_e1_invest_aid_nmbs_2025,nmbs,2025,1049000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 investment aid mainly NMBS 1049m 2025; tick547",
    "bud_e1_invest_aid_nmbs_2026,nmbs,2026,1094000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 investment aid mainly NMBS 1094m 2026; tick547",
    "bud_e1_invest_aid_nmbs_2027,nmbs,2027,776000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 investment aid mainly NMBS 776m 2027 (drop); tick547",
    "bud_e1_invest_aid_nmbs_2028,nmbs,2028,697000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 investment aid mainly NMBS 697m 2028; tick547",
    "bud_e1_invest_aid_nmbs_2029,nmbs,2029,712000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 investment aid mainly NMBS 712m 2029; tick547",
    "bud_e1_gov_supported_invest_2025,sec_federal,2025,6962000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 investments supported by gov 6962m 2025 (1.1pct GDP); tick547",
    "bud_e1_gov_supported_invest_2026,sec_federal,2026,7706000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 investments supported by gov 7706m 2026 (1.2pct GDP); tick547",
    "bud_e1_gov_supported_invest_2027,sec_federal,2027,7980000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 investments supported by gov 7980m 2027 (1.2pct GDP); tick547",
    "bud_e1_gov_supported_invest_2028,sec_federal,2028,8135000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 investments supported by gov 8135m 2028; tick547",
    "bud_e1_gov_supported_invest_2029,sec_federal,2029,8344000000,,,budgeted,src_kamer_expose_invest_e1_2026,strong,Table40 investments supported by gov 8344m 2029; tick547",
    # Dual
    "bud_dual_e1_ion_vs_consol_invest_2026,sec_federal,2026,1559000000,,,derived,src_dual_invest_e1_consol_tick547,strong,Dual Table40 ION 1559m 2026 vs consol invest share class; tick547",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_e1_invest_effort_2025_29,Entity I global investment effort path Table40 2025-2029,sec_federal,Defence rail buildings science IT,"
        "Expose Part I §5 Table40 INR-aligned,2026-01-28,2025,2029,8344000000,"
        '"{""direct_2025_m"":4522,""direct_2026_m"":5174,""direct_2029_m"":6082,""gcf_esa_2026_m"":6612,""gcf_esa_2029_m"":7632,'
        '""gov_supported_2026_m"":7706,""gov_supported_2029_m"":8344,""pct_gdp_2026"":1.2,""fod_2026_m"":4962,""def_esa_corr_2026_m"":-1388,'
        '""ion_2026_m"":1559,""nmbs_aid_2026_m"":1094,""infrabel_niras_act_m"":455,""it_act_2026_m"":657,""science_2026_m"":336,'
        '""note"":""Strong multi-year; defence cash-ESA gap material; residual L5 codes FOI""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Map federal capital formation stack,"
        "Defence L5+NMBS codes FOI,src_kamer_expose_invest_e1_2026,strong,Federal>Invest>E1_effort_2025_29,tick547"
    ),
    (
        "cmt_nmbs_invest_aid_path_2025_29,NMBS investment-aid path Table40 2025-2029,nmbs,SNCB rolling stock/infra class,"
        "Expose Table40 investment-aid line mainly NMBS,2026-01-28,2025,2029,4328000000,"
        '"{""2025_m"":1049,""2026_m"":1094,""2027_m"":776,""2028_m"":697,""2029_m"":712,""sum_5y_m"":4328,'
        '""note"":""Strong path; drop after 2026; dual gap_nmbs_annual_toelage residual cash codes""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Rail investment state support path,"
        "FPS article codes FOI,src_kamer_expose_invest_e1_2026,strong,Federal>NMBS>invest_aid_2025_29,tick547"
    ),
    (
        "cmt_defence_invest_esa_wedge_2026,Defence investment cash vs ESA correction wedge 2026,mod_defensie,NATO capacity path,"
        "Expose Table40 FOD spike + ESA defence correction,2026-01-28,2025,2029,0,"
        '"{""fod_invest_2026_m"":4962,""def_esa_corr_2026_m"":-1388,""def_esa_corr_2025_m"":175,'
        '""path_corr_m"":{""2025"":175,""2026"":-1388,""2027"":-150,""2028"":-220,""2029"":-109},'
        '""note"":""Strong dual cash-ESA; amount 0 on envelope because correction can be negative; not invent net defence cash""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Honest defence invest ESA map,"
        "Line-item FOI,src_kamer_expose_invest_e1_2026,strong,Federal>Defence>invest_ESA_wedge,tick547"
    ),
    (
        "cmt_dual_e1_invest_consol_2026,Dual E1 invest Table40 vs consol institutions,gg_belgium,Multi-entity capital,"
        "Table40 ION + consol Ch5 invest dual,2026-01-28,2026,2026,1559000000,"
        '"{""ion_table40_m"":1559,""infrabel_niras_act_m"":455,""nmbs_aid_m"":1094,'
        '""note"":""not additive pure TE; dual rail+nuclear+buildings stack""}",'
        "0,active,docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,Dual capital perimeter map,"
        "Entity L5 FOI,src_dual_invest_e1_consol_tick547,strong,BE>dual>E1_invest_consol,tick547"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_e1_gov_supported_invest_7_7bn,E1 gov-supported invest 7.71bn 2026,federal,ops,Federal>Invest>gov_supported_2026,7706000000,7706000000,Strong Table40 1.2pct GDP; path to 8.34bn 2029; dual GCF ESA 6.61bn,strong,src_kamer_expose_invest_e1_2026,Taxpayers,Capital formation stack,Defence+rail heavy,4.0,9.0,5,6.50,L5 codes FOI,seed,,tick547",
    "lb_e1_direct_invest_5_17bn,E1 direct public invest 5.17bn 2026,federal,ops,Federal>Invest>direct_2026,5174000000,5174000000,Strong FOD 4.96 + ION 1.56 + OISZ 0.04 before ESA def corr,strong,src_kamer_expose_invest_e1_2026,Departments OIP,Direct capital outlays,Defence spike,4.0,8.5,5,6.35,Split FOI,seed,,tick547",
    "lb_e1_gcf_esa_6_61bn,E1 gross capital formation ESA 6.61bn 2026,federal,ops,Federal>Invest>GCF_ESA_2026,6612000000,6612000000,Strong after IT/science/Infrabel activations and desinvest,strong,src_kamer_expose_invest_e1_2026,ESA national accounts,GCF Entity I,Method dual INR,3.5,8.5,5,6.20,Method FOI,seed,,tick547",
    "lb_nmbs_invest_aid_1_09bn,NMBS investment aid 1.09bn 2026,federal,ops,Federal>NMBS>invest_aid_2026,1094000000,1094000000,Strong Table40 mainly NMBS; path drops to ~0.7bn 2028-29,strong,src_kamer_expose_invest_e1_2026,Rail users,Rolling stock/infra support,Dual PSO package,5.0,8.0,5,6.50,Cash codes FOI,seed,,tick547",
    "lb_fod_invest_4_96bn_defence,FOD/POD invest 4.96bn 2026 defence-driven,federal,ops,Federal>FOD>invest_2026,4962000000,4962000000,Strong defence-driven vs 2.97bn 2025; ESA corr -1.39bn dual,strong,src_kamer_expose_invest_e1_2026,NATO path,Defence capacity cash,Cash-ESA wedge,5.0,8.5,6,6.70,Defence L5 FOI,seed,,tick547",
    "lb_def_esa_corr_minus_1_39bn,Defence ESA invest correction -1.39bn 2026,federal,ops,Federal>Defence>ESA_corr_2026,-1388000000,1388000000,Strong absolute wedge cash vs ESA timing; not pure waste,strong,src_kamer_expose_invest_e1_2026,ESA compilers,Timing correction,Accounting dual,6.0,8.0,5,6.80,Publish method FOI,seed,,tick547",
    "lb_infrabel_niras_act_455m,Infrabel+NIRAS invest activation 455m flat,federal,ops,Federal>Invest>Infrabel_NIRAS_act,455000000,455000000,Strong flat 2025-29 dual rail nuclear perimeter,strong,src_kamer_expose_invest_e1_2026,Rail nuclear,Capital activation,Dual consol,4.0,7.0,4,5.70,Entity FOI,seed,,tick547",
    "lb_dual_e1_invest_stack,Dual E1 invest stack NMBS+ION+defence 2026,multi,ops,BE>dual>E1_invest_stack,7706000000,7706000000,Strong dual gov-supported 7.7bn perimeter labels required,strong,src_dual_invest_e1_consol_tick547,Multi,Capital architecture,Core dual,4.5,9.0,5,6.75,Unified map FOI,seed,,tick547",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

foi = (
    f"gap_e1_invest_l5_codes,Federal>Invest>E1_Table40>L5_codes,sec_federal,"
    "FOD code-7 invest L5 defence vs non-defence cash-by-year 2025-2029; ESA defence correction method series; "
    "NMBS investment-aid budget article codes outturn; Infrabel vs NIRAS split of 455m activation; IT/science activation source INR years,"
    "Table40 aggregates strong multi-year; residual L5 and method opacity on defence-rail bulk,"
    "6,FOD BOSA / FOD Defensie / FOD Mobiliteit / Regie der Gebouwen / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_e1_invest_l5_codes.md,ready,2026-07-31,,,,"
    "cmt_e1_invest_effort_2025_29|cmt_nmbs_invest_aid_path_2025_29|cmt_defence_invest_esa_wedge_2026,"
    "lb_e1_gov_supported_invest_7_7bn|lb_nmbs_invest_aid_1_09bn|lb_def_esa_corr_minus_1_39bn,"
    f"{now},{now},tick547: Table40 filled; residual L5 codes human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_538,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T08:35:00Z,,Spawned tick546 after other-SS Ch5; Part IV complete class; next public residual (Part I aging / primary residual / new PDF); rq_116 deferred"
)
new = (
    "rq_538,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T08:35:00Z,2026-07-31T08:40:00Z,tick547: E1 invest Table40 2025-29 path; spawn rq_539; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_538 row not found")
text = text.replace(old, new)
if "rq_539," not in text:
    text = text.rstrip("\n") + "\n"
    text += (
        "rq_539,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
        "2026-07-31T08:40:00Z,,Spawned tick547 after E1 invest Table40; next Part I residual tables or new PDF; rq_116 deferred; progress@550 in 3 ticks\n"
    )
rq_path.write_text(text, encoding="utf-8")

print("tick547 write OK: budgets", len(buds), "cmt", len(cmts), "lb", len(lbs))

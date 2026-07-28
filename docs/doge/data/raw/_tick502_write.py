# tick502 — CoA 2026_18 Toekomstverbond 6th financial progress + dual DWV/Lantis
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_toekomstverbond_6_2026,Rekenhof Toekomstverbond controleverslag 6e financiele voortgangsrapportage 2026_18,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_18_Toekomstverbond.pdf,"
        "Rekenhof NL chamber 24 Mar 2026,2026-07-28,court_of_audit,"
        "Strong: Oosterweel exec budget 10055m; BC2026 assets 13614m fin need 8273m interest 24495m; "
        "Table1 TV clusters 7917+2258+1696+haventrace 4.1-15.9bn; spent main 2674 PFAS 477 eoy25; dual DWV; tick502\n"
    )
    f.write(
        "src_dual_tv_dwv_mobility_tick502,Dual Toekomstverbond mega-envelope vs DWV study overruns,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_18_Toekomstverbond.pdf,"
        "DOGE synthesis CoA TV 2026_18 + DWV 2026_19,2026-07-28,synthesis,"
        "Strong dual: Oosterweel/TV 10bn+ class exec vs DWV four studies 125m; same VL mobility stack Lantis/DWV; tick502\n"
    )

buds = [
    "bud_oosterweel_task_budget_2019,lantis,2019,4391000000,,,budgeted,src_ccrek_toekomstverbond_6_2026,strong,Task budget 3.6bn main +0.7bn LBH underbuild RO = 4391m price 2019; tick502",
    "bud_oosterweel_task_budget_2022,lantis,2022,5369000000,,,budgeted,src_ccrek_toekomstverbond_6_2026,strong,Task budget raised Oct2022 to 5369m price Jan2022; inflation 1.5bn 2019-23; tick502",
    "bud_oosterweel_exec_budget_2024,lantis,2024,10055000000,,,budgeted,src_ccrek_toekomstverbond_6_2026,strong,Total Oosterweel execution budget 10055m price Jan2024 after RO contract (PFAS/overmacht 1861 + LBH2 655 + risk 607 + invest 299); tick502",
    "bud_oosterweel_main_invest_table1,lantis,2026,7917000000,,,estimated,src_ccrek_toekomstverbond_6_2026,strong,Table1 main works Oosterweel incl underbuild LBH RO 7917m; finance bonds 5500 sub 1200 equity 1172; tick502",
    "bud_oosterweel_overmacht_pfas_table1,lantis,2026,2258000000,,,estimated,src_ccrek_toekomstverbond_6_2026,strong,Table1 overmacht+PFAS-related 2258m; finance sub 1650 toll 300 third 99; tick502",
    "bud_tv_leefbaarheid_phases,lantis,2026,1696000000,,,estimated,src_ccrek_toekomstverbond_6_2026,strong,Table1 leefbaarheid fase1+2 excl underbuild 1696m; overkap 499.3 city/port 250; tick502",
    "bud_tv_haventrace_low,lantis,2026,4100000000,,,estimated,src_ccrek_toekomstverbond_6_2026,medium,Table1 Haventrace rough low 4.1bn exploration variants; tick502",
    "bud_tv_haventrace_high,lantis,2026,15900000000,,,estimated,src_ccrek_toekomstverbond_6_2026,medium,Table1 Haventrace rough high 15.9bn exploration variants; financing general budget ?; tick502",
    "bud_oosterweel_bc2026_assets,lantis,2033,13614000000,,,projection,src_ccrek_toekomstverbond_6_2026,strong,BC2026 materieel vaste activa OWV end build 13614m (was 10885 BC2025); build end 31/12/2033; tick502",
    "bud_oosterweel_bc2026_fin_need,lantis,2033,8273000000,,,projection,src_ccrek_toekomstverbond_6_2026,strong,BC2026 remaining net financing need build phase 8273m; tick502",
    "bud_oosterweel_bc2026_capex_remain,lantis,2033,7275000000,,,projection,src_ccrek_toekomstverbond_6_2026,strong,BC2026 remaining CAPEX build phase 7275m; tick502",
    "bud_oosterweel_bc2026_opex,lantis,2083,4464000000,,,projection,src_ccrek_toekomstverbond_6_2026,strong,BC2026 remaining OPEX build+ops phase 4464m; tick502",
    "bud_oosterweel_bc2026_bonds,lantis,2033,7751000000,,,projection,src_ccrek_toekomstverbond_6_2026,strong,BC2026 LT bonds 5500+2251=7751m; tick502",
    "bud_oosterweel_bc2026_subloans,lantis,2033,2850000000,,,projection,src_ccrek_toekomstverbond_6_2026,strong,BC2026 subordinated loans 1200+1650=2850m; tick502",
    "bud_oosterweel_bc2026_interest,lantis,2083,24495000000,,,projection,src_ccrek_toekomstverbond_6_2026,strong,BC2026 interest payable 2026-2083 24495m; tick502",
    "bud_oosterweel_spent_main_2025,lantis,2025,2674100000,,,outturn,src_ccrek_toekomstverbond_6_2026,strong,Main works invested 2674.1m end-2025 cumulative; tick502",
    "bud_oosterweel_spent_pfas_2025,lantis,2025,476900000,,,outturn,src_ccrek_toekomstverbond_6_2026,strong,PFAS sanering invested 476.9m end-2025 cumulative; tick502",
    "bud_oosterweel_linkeroever_main_2025,lantis,2025,461100000,,,outturn,src_ccrek_toekomstverbond_6_2026,strong,Linkeroever main works actual 461.1m vs budget 467.5m eoy2025; tick502",
    "bud_oosterweel_linkeroever_pfas_2025,lantis,2025,166800000,,,outturn,src_ccrek_toekomstverbond_6_2026,strong,Linkeroever PFAS/overmacht actual 166.8m vs budget 159.7m eoy2025; tick502",
    "bud_oosterweel_risk_budget_2024,lantis,2024,607000000,,,budgeted,src_ccrek_toekomstverbond_6_2026,strong,Risk budget 607m in 10055m execution package; tick502",
    "bud_oosterweel_inflation_2019_23,lantis,2023,1500000000,,,estimated,src_ccrek_toekomstverbond_6_2026,strong,Inflation impact on Oosterweel 1.5bn 2019-2023 CoA; tick502",
    "bud_vl_debt_mjr_2030_tv,vlaanderen_gov,2030,74600000000,,,projection,src_ccrek_toekomstverbond_6_2026,strong,VL consol gross debt path 41.7bn 2024 to 74.6bn 2030 MJR (+80pct) CoA TV ch2; tick502",
    "bud_dual_tv_dwv_mobility,gg_belgium,2026,10055000000,,,derived,src_dual_tv_dwv_mobility_tick502,strong,Dual Oosterweel exec 10.055bn class vs DWV studies 0.125bn; not additive TE; tick502",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_oosterweel_exec_budget_10bn,Oosterweel total execution budget 10.055bn CoA TV6,"
        "lantis,Antwerp region mobility users,CoA 2026_18 + Lantis projectbudget,"
        "2018-01-01,2018,2033,10055000000,"
        '"{""task_2019_m"":4391,""task_2022_m"":5369,""exec_2024_m"":10055,'
        '""inflation_2019_23_bn"":1.5,""pfas_add_m"":1861,""lbh2_under_m"":655,'
        '""risk_m"":607,""invest_add_m"":299,""spent_main_eoy25_m"":2674.1,'
        '""spent_pfas_eoy25_m"":476.9,""build_end"":""2033-12-31"",'
        '""note"":""Strong CoA; NEC4 painshare; force majeure legal framework incomplete""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_18_Toekomstverbond.pdf,"
        "Complete Scheldt crossing close Antwerp ring,Lock force majeure finance; dual DWV studies,"
        "src_ccrek_toekomstverbond_6_2026,strong,Vlaanderen>Lantis>Oosterweel,tick502"
    ),
    (
        "cmt_oosterweel_bc2026_path,Oosterweel business case 2026 financing path,"
        "lantis,Toll payers VL taxpayers,Lantis BC2026 via CoA 2026_18,"
        "2026-01-01,2026,2083,24495000000,"
        '"{""assets_end_build_m"":13614,""fin_need_m"":8273,""capex_remain_m"":7275,'
        '""opex_m"":4464,""bonds_m"":7751,""subloans_m"":2850,""interest_2026_83_m"":24495,'
        '""note"":""Strong CoA Table4; interest lifetime mass; max VAT recovery assumed""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_18_Toekomstverbond.pdf,"
        "Toll-backed long-term finance model,Stress-test toll volumes; dual RR2025 debt,"
        "src_ccrek_toekomstverbond_6_2026,strong,Vlaanderen>Lantis>BC2026,tick502"
    ),
    (
        "cmt_toekomstverbond_clusters_table1,Toekomstverbond investment clusters Table1 CoA,"
        "lantis,Antwerp region,CoA 2026_18 Table1,"
        "2017-03-15,2017,2040,11871000000,"
        '"{""oosterweel_main_m"":7917,""overmacht_pfas_m"":2258,""leefbaarheid_m"":1696,'
        '""haventrace_low_m"":4100,""haventrace_high_m"":15900,""modal_shift"":""unknown_GIP"",'
        '""envelope_core_m"":11871,'
        '""note"":""Strong CoA Table1; haventrace range not in core sum; price levels not uniform""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_18_Toekomstverbond.pdf,"
        "Liveable accessible Antwerp region package,Finance plan for all clusters; FOI variants,"
        "src_ccrek_toekomstverbond_6_2026,strong,Vlaanderen>Toekomstverbond,tick502"
    ),
    (
        "cmt_dual_tv_dwv_mobility_stack,Dual Toekomstverbond 10bn + DWV studies 125m,"
        "gg_belgium,Flanders mobility mega-projects,"
        "CoA TV 2026_18 + DWV 2026_19,"
        "2014-01-01,2017,2033,10179900000,"
        '"{""oosterweel_exec_m"":10055,""dwv_studies4_m"":124.9,'
        '""note"":""not additive TE; dual delivery vehicles Lantis/DWV same policy stack""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_18_Toekomstverbond.pdf,"
        "Map dual VL mobility mega-project governance,Comparable contractor L5 FOI,"
        "src_dual_tv_dwv_mobility_tick502,strong,BE>dual>Mobility>TV_DWV,tick502"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_oosterweel_exec_10_1bn,Oosterweel execution budget 10.055bn 2024 prices,regional,infrastructure,Vlaanderen>Lantis>Oosterweel_exec,0,10055000000,Strong CoA TV6: task 4.4->5.4->exec 10.055bn; spent main 2.67bn+PFAS 0.48bn eoy25; annual0 stock,strong,src_ccrek_toekomstverbond_6_2026,Antwerp region,Complete ring Scheldt tunnel,Mega-project cost escalation classic DOGE,5.5,9.5,7,7.0,Lock overmacht finance; dual DWV,seed,,tick502",
    "lb_oosterweel_bc2026_interest_24bn,Oosterweel BC2026 interest 24.5bn 2026-2083,regional,debt_service,Vlaanderen>Lantis>interest_lifetime,0,24495000000,Strong CoA Table4: interest 24495m lifetime; bonds 7.75bn sub 2.85bn; annual0 stock path,strong,src_ccrek_toekomstverbond_6_2026,Toll payers taxpayers,Service project debt from tolls,Interest mass >> construction escalation,6.5,9.5,6,7.55,Publish toll stress tests FOI,seed,,tick502",
    "lb_oosterweel_fin_need_8_3bn,Oosterweel remaining net financing need 8.27bn,regional,financing,Vlaanderen>Lantis>fin_need_build,0,8273000000,Strong CoA BC2026: remaining net fin need build 8273m; CAPEX remain 7275m; annual0,strong,src_ccrek_toekomstverbond_6_2026,Creditors Lantis,Close financing gap to 2033,Debt snowball dual VL RR,5.5,9.0,6,6.9,Bond+subloan schedule FOI,seed,,tick502",
    "lb_tv_clusters_11_9bn,Toekomstverbond core clusters ~11.9bn excl haventrace,regional,programme,Vlaanderen>Toekomstverbond>clusters,0,11871000000,Strong CoA Table1: 7917+2258+1696; haventrace 4.1-15.9bn extra; modal shift opaque,strong,src_ccrek_toekomstverbond_6_2026,Antwerp region,Liveable ring package,Multi-cluster opacity financing,5.0,9.5,7,6.85,Full cluster cash schedule FOI,seed,,tick502",
    "lb_tv_haventrace_4_16bn,Haventrace indicative 4.1-15.9bn exploration,regional,infrastructure,Vlaanderen>Toekomstverbond>Haventrace,0,15900000000,Medium CoA: rough variants exploration; financing general budget ?; annual0 range,medium,src_ccrek_toekomstverbond_6_2026,Port Antwerp users,Port access variants,Huge unscoped envelope,7.0,9.5,8,7.75,Choose variant+cost ceiling FOI,seed,,tick502",
    "lb_oosterweel_spent_3_15bn_2025,Oosterweel spent main+PFAS ~3.15bn eoy2025,regional,infrastructure,Vlaanderen>Lantis>spent_cum_2025,3151000000,3151000000,Strong CoA: main 2674.1 + PFAS 476.9 eoy2025; Linkeroever within budget,strong,src_ccrek_toekomstverbond_6_2026,Construction chain,Delivery progress,Core delivery not pure waste,3.0,9.5,5,6.55,Continue control; dual GIP,seed,,tick502",
    "lb_dual_tv_dwv,Dual TV Oosterweel 10bn + DWV studies 125m,multi,programme,BE>dual>Mobility_TV_DWV,124900000,10179900000,Strong dual CoA: mega project vs study overruns same VL mobility policy stack,strong,src_dual_tv_dwv_mobility_tick502,Flanders mobility,Dual delivery vehicles,Governance dual FOI L5,5.5,9.5,5,7.15,Comparable L5 contractors both,seed,,tick502",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_tv_oosterweel_finance_l5,Vlaanderen>Lantis>Toekomstverbond>finance_L5,lantis,"
    "Force majeure/PFAS financing legal framework + cash schedule; BC2026 bond/subloan drawdown "
    "by year; Haventrace variant decision and cost ceiling; reconcile GIP 2025-27 vs Lantis multiyear,"
    "CoA TV6: exec 10bn and BC interest 24.5bn strong; legal overmacht frame incomplete; GIP unreconciled,8,"
    "Lantis / Departement MOW / Team Openbaarheid,openbaarheid@vlaanderen.be,"
    "Havenlaan 88 bus 20 1000 Brussel,docs/doge/foi/drafts/gap_tv_oosterweel_finance_l5.md,"
    "ready,2026-07-28,,,,,cmt_oosterweel_exec_budget_10bn,"
    "lb_oosterweel_exec_10_1bn|lb_oosterweel_bc2026_interest_24bn,"
    "2026-07-28T21:30:00Z,2026-07-28T21:30:00Z,"
    "tick502: CoA 2026_18 primary fill; residual finance L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_493,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-28T21:10:00Z,,Spawned tick501 after CoA DWV studieopdrachten; rq_116 deferred"
)
new = (
    "rq_493,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_tv_oosterweel_finance_l5,"
    "2026-07-28T21:10:00Z,2026-07-28T21:30:00Z,"
    "tick502: CoA 2026_18 Toekomstverbond Oosterweel 10bn BC interest 24.5bn dual DWV; FOI; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_493 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_494,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-28T21:30:00Z,,Spawned tick502 after CoA Toekomstverbond 6; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-28T21:30:00Z,rq_493,502,no,"
    "Tick502 CoA TV6 Oosterweel 10bn BC interest 24.5bn dual DWV; next prio5 rq_494; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick502 OK")

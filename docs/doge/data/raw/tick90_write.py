from pathlib import Path

root = Path("docs/doge/data")

# budgets
bud = root / "budgets.csv"
t = bud.read_text(encoding="utf-8")
if not t.endswith("\n"):
    t += "\n"
if "bud_wvl_pom_dotatie_2026" not in t:
    t += """bud_wvl_pom_dotatie_2026,prov_west_vlaanderen,2026,11653824,,,budgeted,src_westvl_prov_mjp_2026,strong,POM West-Vlaanderen jaarlijkse dotatie 2026 EUR 11653824 (MJP p60 agentschappen table)
bud_wvl_westtoer_dotatie_2026,prov_west_vlaanderen,2026,11052567,,,budgeted,src_westvl_prov_mjp_2026,strong,Westtoer APB jaarlijkse dotatie 2026 EUR 11052567
bud_wvl_inagro_dotatie_2026,prov_west_vlaanderen,2026,10839292,,,budgeted,src_westvl_prov_mjp_2026,strong,Inagro vzw jaarlijkse dotatie 2026 EUR 10839292
bud_wvl_tua_west_dotatie_2026,prov_west_vlaanderen,2026,385000,,,budgeted,src_westvl_prov_mjp_2026,strong,TUA WEST private stichting dotatie 2026 EUR 385000
bud_wvl_agencies_dotatie_sum_2026,prov_west_vlaanderen,2026,33930683,,,budgeted,src_westvl_prov_mjp_2026,strong,Sum POM+Westtoer+Inagro+TUA WEST dotaties 2026 33930683 (upgrades ~35m class)
bud_wvl_wfiv_base_2026_confirm,prov_west_vlaanderen,2026,400000,,,budgeted,src_westvl_prov_mjp_2026,strong,WFIV basissubsidie constant EUR 400000 (p124; already had bud_wvl_prov_wfiv_base_2026)
bud_wvl_rl_westhoek_2026,prov_west_vlaanderen,2026,1346932,,,budgeted,src_westvl_prov_mjp_2026,strong,Regionaal landschap Westhoek werkingssubsidie 2026 EUR 1346932
bud_wvl_rl_houtland_polders_2026,prov_west_vlaanderen,2026,1180131,,,budgeted,src_westvl_prov_mjp_2026,strong,Regionaal landschap Houtland en Polders 2026 EUR 1180131
bud_wvl_rl_wv_hart_2026,prov_west_vlaanderen,2026,717863,,,budgeted,src_westvl_prov_mjp_2026,strong,Regionaal landschap West-Vlaamse hart 2026 EUR 717863
bud_wvl_unie_k_kapitaal_2026,prov_west_vlaanderen,2026,1160258,,,budgeted,src_westvl_prov_mjp_2026,strong,UNIE-K vzw kapitaalaflossing geconsolideerde leningen 2026 EUR 1160258
bud_ovl_pimd_2026,prov_oost_vlaanderen,2026,1220850,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,PIMD Oost-Vlaanderen werkingssubsidie 2026 EUR 1220850 (doc p14)
bud_ovl_toerisme_ovl_2026,prov_oost_vlaanderen,2026,600176,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,vzw Toerisme Oost-Vlaanderen sector+expertise 2026 EUR 600175.53
bud_ovl_crvv_2026,prov_oost_vlaanderen,2026,230000,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,Centrum Ronde van Vlaanderen werkingssubsidie 2026 EUR 230000
bud_ovl_huysmanhoeve_2026,prov_oost_vlaanderen,2026,789225,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,Plattelandscentrum Meetjesland Huysmanhoeve 2026 EUR 789225
bud_ovl_rato_2026,prov_oost_vlaanderen,2026,482694,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,RATO vzw werkingssubsidie 2026 EUR 482693.58
bud_ovl_werkingssubsidies_total_2026,prov_oost_vlaanderen,2026,30667884,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,TOTAAL WERKINGSSUBSIDIES documentatie p14 EUR 30667884.44 (matches T2)
"""
    bud.write_text(t, encoding="utf-8")
    print("budgets ok")
else:
    print("budgets exist")

# update medium agency class row
t = bud.read_text(encoding="utf-8")
t = t.replace(
    "bud_wvl_prov_agency_subs_class_2026,prov_west_vlaanderen,2026,35000000,,,budgeted,src_westvl_prov_mjp_2026,medium,Verzelfstandigde agentschappen (POM Inagro Westtoer) class ~EUR 35m/yr of werkingssubsidies",
    "bud_wvl_prov_agency_subs_class_2026,prov_west_vlaanderen,2026,35000000,,,budgeted,src_westvl_prov_mjp_2026,medium,Superseded by exact sum 33930683 tick90; prior narrative ~35m",
)
bud.write_text(t, encoding="utf-8")

# commitments - append new L5 rows if missing
cmt = root / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
if "cmt_wvl_pom_dotatie_2026" not in ct:
    if not ct.endswith("\n"):
        ct += "\n"
    ct += """cmt_wvl_pom_dotatie_2026,POM West-Vlaanderen annual operating dotatie,prov_west_vlaanderen,POM West-Vlaanderen (sui generis agency),MJP agentschappen table p60,2026-01-01,2026,2031,11653824,"{""2026"":11653824,""2027"":11945170,""2028"":12243799,""2029"":12521642,""2030"":12805795,""2031"":13096402}",0,active,,Provincial economic development agency,Publish outcome KPIs entrepreneurship,src_westvl_prov_mjp_2026,strong,Province_West_Vlaanderen>POM,Basissubsidie +2.5pct/yr path; loan support separate
cmt_wvl_westtoer_dotatie_2026,Westtoer APB annual operating dotatie,prov_west_vlaanderen,Westtoer (APB),MJP agentschappen table p60,,2026,2031,11052567,"{""2026"":11052567,""2027"":11328882,""2028"":11612104,""2029"":11902406,""2030"":12199966,""2031"":12504966}",0,active,,Provincial tourism agency,Beaufort project cycle transparency,src_westvl_prov_mjp_2026,strong,Province_West_Vlaanderen>Westtoer,Basissubsidie +2.5pct; project subsidies separate
cmt_wvl_inagro_dotatie_2026,Inagro vzw annual operating dotatie,prov_west_vlaanderen,Inagro vzw (EVA),MJP agentschappen table p60,,2026,2031,10839292,"{""2026"":10839292,""2027"":11110275,""2028"":11388031,""2029"":11672732,""2030"":11964550,""2031"":12263664}",0,active,,Provincial agri-innovation agency,Loan capital/interest support path separate,src_westvl_prov_mjp_2026,strong,Province_West_Vlaanderen>Inagro,Basissubsidie +2.5pct; multi-loan package
cmt_wvl_agencies_package_2026,WVL four agencies operating package 2026,prov_west_vlaanderen,POM Westtoer Inagro TUA WEST,MJP p60 sum,,2026,2026,33930683,"{""pom"":11653824,""westtoer"":11052567,""inagro"":10839292,""tua_west"":385000,""sum"":33930683}",0,active,,Outsourced provincial tasks via agencies,Open name-level full T2 beyond 4 agencies,src_westvl_prov_mjp_2026,strong,Province_West_Vlaanderen>Agencies,~34m of 54.4m werkingssubsidies; narrative was ~35m
cmt_ovl_pimd_2026,PIMD Oost-Vlaanderen moral service subsidy,prov_oost_vlaanderen,Provinciale Instelling voor Morele Dienstverlening,Documentatie werkingssubsidies,,2026,2026,1220850,"{""2026"":1220850}",0,active,,Non-confessional moral services legal duty,Decretal obligation path,src_oostvl_prov_mjp_documentatie_2026,strong,Province_Oost_Vlaanderen>PIMD,Part of erediensten/levensbeschouwing block
cmt_ovl_toerisme_ovl_2026,Toerisme Oost-Vlaanderen sector subsidies,prov_oost_vlaanderen,vzw Toerisme Oost-Vlaanderen,Documentatie 0521,,2026,2026,600176,"{""sectorontwikkeling"":342243,""kenniscentrum"":257932,""sum"":600176}",0,active,,Provincial tourism sector support,Outcome KPIs visitor economy,src_oostvl_prov_mjp_documentatie_2026,strong,Province_Oost_Vlaanderen>Toerisme,Two named lines sum 600k
"""
    cmt.write_text(ct, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments exist")

# update cmt_wvl_prov_werkingssubsidies and budget envelope
ct = cmt.read_text(encoding="utf-8")
ct = ct.replace(
    '""agencies_class"":35000000',
    '""agencies_dotatie_sum"":33930683,""agencies_class"":35000000',
)
cmt.write_text(ct, encoding="utf-8")

# leaderboard
lb = root / "leaderboard.csv"
lt = lb.read_text(encoding="utf-8")
if "lb_wvl_pom_dotatie" not in lt:
    if not lt.endswith("\n"):
        lt += "\n"
    lt += """lb_wvl_pom_dotatie,POM West-Vlaanderen operating dotatie 2026,Flanders,subsidy,Province_West_Vlaanderen>POM,11653824,11653824,Agency sui generis economic development; +2.5pct path to 13.1m 2031,strong,src_westvl_prov_mjp_2026,West Flanders economy,Provincial economic middleman,Core provincial task outsourced; additionality KPIs thin,3,7.5,4,5.1,Publish agency annual results vs province goals,seed,,tick90
lb_wvl_agencies_package,WVL four agencies package 2026,Flanders,subsidy,Province_West_Vlaanderen>agencies,33930683,33930683,POM 11.7m + Westtoer 11.1m + Inagro 10.8m + TUA 0.4m,strong,src_westvl_prov_mjp_2026,Taxpayers partners,Outsourced provincial tasks,~63pct of 54.4m werkingssubsidies,3,8,4,5.3,Consolidated agency KPI dashboard,seed,,tick90
lb_ovl_pimd,PIMD Oost-Vlaanderen moral services 2026,Flanders,subsidy,Province_Oost_Vlaanderen>PIMD,1220850,1220850,Legal duty non-confessional moral services,strong,src_oostvl_prov_mjp_documentatie_2026,Residents,Decretal life-stance financing,Mandatory not discretionary waste,2,6,3,3.7,Review decretale path with other provinces,seed,,tick90
"""
    lb.write_text(lt, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard exist")

# entities notes
ent = root / "entities.csv"
et = ent.read_text(encoding="utf-8")
et = et.replace(
    "MJP 2026-2031; exp 194.4m cashout 283.9m; bezold 84.9m; werkingssubsidies 54.4m; opcent 128.8m; invest 363.5m/6y",
    "MJP 2026-2031; exp 194.4m; agencies POM+Westtoer+Inagro+TUA 33.9m; werkingssubsidies 54.4m; bezold 84.9m",
)
et = et.replace(
    "MJP 2026-2031; exp uit 313.2m ont 327.5m cashout 379.9m; invest ~400m/6y; pers 212m",
    "MJP 2026-2031; exp 313.2m cashout 379.9m; werkingssubsidies 30.7m; PIMD 1.22m; pers 212m",
)
ent.write_text(et, encoding="utf-8")
print("entities ok")

# sources
src = root / "sources.csv"
st = src.read_text(encoding="utf-8")
if "src_westvl_agencies_p60" not in st:
    if not st.endswith("\n"):
        st += "\n"
    st += 'src_westvl_agencies_p60,WVL MJP 2026-2031 p60-67 agentschappen and landschappen tables,https://www.west-vlaanderen.be/sites/default/files/2025-12/MJP-2026-2031-fin-nota-toelichting.pdf,Provincie West-Vlaanderen,2026-07-22,budget,"Pages 60-67: POM Westtoer Inagro TUA WEST annual dotaties; loan support; regionale landschappen; UNIE-K; WFIV base"\n'
    src.write_text(st, encoding="utf-8")
print("sources ok")

# queue
rq = root / "research_queue.csv"
rt = rq.read_text(encoding="utf-8")
rt = rt.replace(
    'rq_090,WVL or OVL named L5 werkingssubsidies sample,continuous,3,open,L5,prov_west_vlaanderen,"Extract 3+ named third-party/agency subsidies with EUR from MJP documentatie or T2 detail if public; else FOI.",,2026-07-22T14:34:00Z,2026-07-22T14:34:00Z,"Aggregate werkingssubsidies now strong WVL 54.4m; name-level still thin"',
    'rq_090,WVL or OVL named L5 werkingssubsidies sample,continuous,3,done,L5,prov_west_vlaanderen,"Extract 3+ named third-party/agency subsidies with EUR from MJP documentatie or T2 detail if public; else FOI.",,2026-07-22T14:34:00Z,2026-07-22T14:49:00Z,"WVL: POM 11.65m Westtoer 11.05m Inagro 10.84m TUA 0.39m sum 33.93m; OVL: PIMD 1.22m Toerisme 0.60m CRVV 0.23m Huysman 0.79m RATO 0.48m"',
)
if "rq_091," not in rt:
    if not rt.endswith("\n"):
        rt += "\n"
    rt += 'rq_091,OVL top named werkingssubsidies deepen or POM OVL,continuous,2,open,L5,prov_oost_vlaanderen,"Optional: extract more OVL named L5 from documentatie (POM invest 200k; political parties; largest lines) or stop if sample enough.",,2026-07-22T14:49:00Z,2026-07-22T14:49:00Z,"Tick90 sampled 5 OVL names; full register public in documentatie"\n'
rq.write_text(rt, encoding="utf-8")
print("queue ok")

# state
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    'main,continuous,continuous,2026-07-22T14:49:00Z,rq_090,90,no,"WVL agencies 33.9m L5 (tick90). Next: rq_091 OVL deepen or rq_089 SWA low."\n',
    encoding="utf-8",
)
print("state ok")

# log
log = Path("docs/doge/loop_log.md")
entry = """
### 2026-07-22T14:49:00Z -- tick 90
- Unit: rq_090 (WVL/OVL named L5 werkingssubsidies sample)
- Found (strong, official WVL MJP p60 + OVL documentatie p4-14): **WVL agencies 2026 dotaties:** POM **EUR 11,653,824**; Westtoer **EUR 11,052,567**; Inagro **EUR 10,839,292**; TUA WEST **EUR 385,000**; **sum EUR 33,930,683** (upgrades prior ~35m class; ~63pct of 54.4m werkingssubsidies). WFIV base **EUR 400,000**. Named landschappen: Westhoek 1.35m; Houtland-Polders 1.18m; WV hart 0.72m. UNIE-K kapitaal **EUR 1,160,258**. **OVL sample:** PIMD **EUR 1,220,850**; Toerisme OVL **EUR 600,176**; Centrum Ronde van Vlaanderen **EUR 230,000**; Huysmanhoeve **EUR 789,225**; RATO **EUR 482,694**; OVL total werkingssubsidies **EUR 30,667,884** reconfirmed.
- Wrote: 16 budgets; 6 commitments; 3 leaderboard; sources; entities; rq_090=done; seeded rq_091; ticks=90
- FOI: none (public tables)
- Next: **rq_091** OVL L5 deepen (prio 2) or **rq_089** SWA Q4 (prio 1)

""".encode("utf-8")
raw = log.read_bytes()
if b"tick 90" not in raw:
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + entry)
    print("log ok")
else:
    print("log exists")

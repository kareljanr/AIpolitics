from pathlib import Path

root = Path("docs/doge/data")

# budgets
bud = root / "budgets.csv"
t = bud.read_text(encoding="utf-8")
if not t.endswith("\n"):
    t += "\n"
if "bud_ovl_pom_werking_sum_2026" not in t:
    t += """bud_ovl_pom_werking_sum_2026,prov_oost_vlaanderen,2026,2004589,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,POM Oost-Vlaanderen named werking lines sum 2026 EUR 2004588.94 (5 werking + 25k Scheldemond)
bud_ovl_pom_kennis_2026,prov_oost_vlaanderen,2026,318780,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,POM werkingssubsidie kenniseconomie innovatie 2026 EUR 318780.49
bud_ovl_pom_logistiek_2026,prov_oost_vlaanderen,2026,294662,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,POM werkingssubsidie logistiek 2026 EUR 294661.57
bud_ovl_pom_bedrijvencentra_2026,prov_oost_vlaanderen,2026,386744,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,POM werkingssubsidie ontwikkelingsprojecten bedrijvencentra 2026 EUR 386744.23
bud_ovl_pom_terreinen_2026,prov_oost_vlaanderen,2026,386744,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,POM werkingssubsidie bedrijventerreinenmanagement 2026 EUR 386744.23
bud_ovl_pom_verduurzaming_2026,prov_oost_vlaanderen,2026,592658,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,POM werkingssubsidie verduurzamende participaties 2026 EUR 592658.42
bud_ovl_pom_invest_2026,prov_oost_vlaanderen,2026,200000,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,POM investeringssubsidie bedrijventerreinen 2026 EUR 200000
bud_ovl_erov_sum_2026,prov_oost_vlaanderen,2026,1446227,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,Erov vzw three werkingstoelagen sum 2026 EUR 1446227.40
bud_ovl_erov_streekproducten_2026,prov_oost_vlaanderen,2026,867000,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,Erov streekproducten 2026 EUR 867000
bud_ovl_erov_voeding_2026,prov_oost_vlaanderen,2026,375227,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,Erov voedingsondernemers 2026 EUR 375227.40
bud_ovl_politieke_partijen_2026,prov_oost_vlaanderen,2026,532093,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,Subsidies politieke partijen provincieraad 2026 EUR 532093 (path to 0 in 2031)
bud_ovl_fracties_2026,prov_oost_vlaanderen,2026,58687,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,Erkende fracties provincieraad 2026 EUR 58687
bud_ovl_polders_wateringen_2026,prov_oost_vlaanderen,2026,2100000,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,Polders en Wateringen onderhoud/pompkosten 2e cat 2026 EUR 2100000
bud_ovl_interreg_2127_2026,prov_oost_vlaanderen,2026,1830896,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,EU Interreg cofinancing 2021-27 programme line 2026 EUR 1830896.24
bud_ovl_pdpo_betaalorgaan_2026,prov_oost_vlaanderen,2026,708000,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,Vlaams Betaalorgaan PDPO cofinancing 2026 EUR 708000
bud_ovl_noord_zuid_2026,prov_oost_vlaanderen,2026,620000,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,Regiogerichte noord-zuidsamenwerking 2026 EUR 620000
bud_ovl_azorg_ahria_2026,prov_oost_vlaanderen,2026,350000,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,AZORG vzw AHRIA startup subsidy 2026 EUR 350000 (one-off)
bud_ovl_bosgroep_werking_2026,prov_oost_vlaanderen,2026,332702,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,Bosgroep Oost-Vlaanderen werkingssubsidie 2026 EUR 332701.60
bud_ovl_domain_economie_subs_2026,prov_oost_vlaanderen,2026,20423228,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,Beleidsdomein economie/landbouw/EU domain werkingssubsidies total 2026 EUR 20423228.46
bud_ovl_domain_leefmilieu_subs_2026,prov_oost_vlaanderen,2026,4858494,,,budgeted,src_oostvl_prov_mjp_documentatie_2026,strong,Beleidsdomein leefmilieu werkingssubsidies total 2026 EUR 4858494
"""
    bud.write_text(t, encoding="utf-8")
    print("budgets ok")
else:
    print("budgets exist")

# commitments
cmt = root / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
if "cmt_ovl_pom_package_2026" not in ct:
    if not ct.endswith("\n"):
        ct += "\n"
    ct += """cmt_ovl_pom_package_2026,POM Oost-Vlaanderen operating subsidy package 2026,prov_oost_vlaanderen,POM Oost-Vlaanderen,Documentatie named POM werking lines,,2026,2026,2004589,"{""kennis"":318780,""logistiek"":294662,""bedrijvencentra"":386744,""terreinen"":386744,""verduurzaming"":592658,""scheldemond"":25000,""sum_werking"":2004589,""invest_terreinen"":200000}",0,active,,Provincial economic development agency,Publish consolidated POM annual report vs province KPIs,src_oostvl_prov_mjp_documentatie_2026,strong,Province_Oost_Vlaanderen>POM,~2.0m werking + 0.2m invest named
cmt_ovl_erov_2026,Erov vzw food and craft subsidies 2026,prov_oost_vlaanderen,Erov vzw,Documentatie 0510,,2026,2026,1446227,"{""voeding"":375227,""ambacht"":204000,""streekproducten"":867000,""sum"":1446227}",0,active,,Regional food craft promotion,Additionality vs private marketing,src_oostvl_prov_mjp_documentatie_2026,strong,Province_Oost_Vlaanderen>Erov,Streekproducten largest slice 867k
cmt_ovl_polders_wateringen_2026,Polders en Wateringen maintenance transfer 2026,prov_oost_vlaanderen,Polders en Wateringen,Legal Art 18 wet 28 Dec 1967,,2026,2026,2100000,"{""2026"":2100000}",0,active,,Watercourse maintenance 2nd category,Statutory cost recovery not pure discretionary,src_oostvl_prov_mjp_documentatie_2026,strong,Province_Oost_Vlaanderen>Water>Polders,Largest single named werking line 2.1m
cmt_ovl_politieke_partijen_2026,Political party subsidies provincieraad path 2026-2031,prov_oost_vlaanderen,Political parties in provincial council,PR 16-02-2011 path to zero 2031,,2026,2031,532093,"{""2026"":532093,""2027"":465581,""2028"":399070,""2029"":332558,""2030"":266046,""2031"":0}",0,active,,Provincial party financing phase-out,Complete phase-out 2031,src_oostvl_prov_mjp_documentatie_2026,strong,Province_Oost_Vlaanderen>Politics>parties,Declining path to 0
cmt_ovl_interreg_cofin_2026,EU Interreg cofinancing envelope line 2026,prov_oost_vlaanderen,EU project promoters,PR 25-06-2025 2021-27 residual,,2026,2026,1830896,"{""2026"":1830896,""2027"":430000}",0,active,,EU co-financed projects,Additionality vs pure provincial spend,src_oostvl_prov_mjp_documentatie_2026,strong,Province_Oost_Vlaanderen>EU>Interreg,2026 residual then drop
"""
    cmt.write_text(ct, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments exist")

# leaderboard
lb = root / "leaderboard.csv"
lt = lb.read_text(encoding="utf-8")
if "lb_ovl_polders_wateringen" not in lt:
    if not lt.endswith("\n"):
        lt += "\n"
    lt += """lb_ovl_polders_wateringen,Polders en Wateringen OVL maintenance 2026,Flanders,ops,Province_Oost_Vlaanderen>Water>Polders,2100000,2100000,Legal Art18 transfer 2.1m/yr watercourse 2nd cat,strong,src_oostvl_prov_mjp_documentatie_2026,Water users,Mandatory water maintenance,Statutory not pure waste; opacity on unit cost,2,7,4,4.6,Publish unit costs per km watercourse,seed,,tick91
lb_ovl_pom_package,POM Oost-Vlaanderen subsidy package 2026,Flanders,subsidy,Province_Oost_Vlaanderen>POM,2004589,2204589,Named werking ~2.0m + invest 0.2m; multi-line agency,strong,src_oostvl_prov_mjp_documentatie_2026,Regional economy,Provincial economic middleman,Smaller than WVL POM 11.7m; different perimeter,3,7.5,4,5.1,Consolidate POM lines in open data,seed,,tick91
lb_ovl_erov,Erov vzw food craft package 2026,Flanders,subsidy,Province_Oost_Vlaanderen>Erov,1446227,1446227,Streekproducten 867k + voeding 375k + ambacht 204k,strong,src_oostvl_prov_mjp_documentatie_2026,Producers consumers,Regional branding subsidy,Discretionary promotion; additionality thin,4,7,3,4.9,Outcome KPIs sales vs subsidy,seed,,tick91
lb_ovl_politieke_partijen,OVL political party subsidies phase-out,Flanders,ops,Province_Oost_Vlaanderen>Politics,532093,0,532k 2026 path to 0 in 2031,strong,src_oostvl_prov_mjp_documentatie_2026,Voters,Party financing,Phase-out is transparency win,5,6,5,5.3,Keep path; no reintroduction,seed,,tick91
"""
    lb.write_text(lt, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard exist")

# entities
ent = root / "entities.csv"
et = ent.read_text(encoding="utf-8")
et = et.replace(
    "MJP 2026-2031; exp 313.2m cashout 379.9m; werkingssubsidies 30.7m; PIMD 1.22m; pers 212m",
    "MJP 2026-2031; exp 313.2m; werkingssubsidies 30.7m; POM package ~2.0m; Erov 1.45m; Polders 2.1m; pers 212m",
)
ent.write_text(et, encoding="utf-8")
print("entity ok")

# sources note
src = root / "sources.csv"
st = src.read_text(encoding="utf-8")
if "tick91" not in st:
    st = st.replace(
        "Documentatie 44p; Totalen budget 2026 exp uit 313167169 ont 327535846; inv 62639681 fin uit 4048851; raw oostvl_meerjarenplan-2026-2031_documentatie.pdf",
        "Documentatie 44p; Totalen + named werkingssubsidies p4-14; POM Erov Polders parties Interreg; exp 313.2m; raw oostvl_meerjarenplan-2026-2031_documentatie.pdf",
    )
    src.write_text(st, encoding="utf-8")
print("sources ok")

# queue
rq = root / "research_queue.csv"
rt = rq.read_text(encoding="utf-8")
rt = rt.replace(
    'rq_091,OVL top named werkingssubsidies deepen or POM OVL,continuous,2,open,L5,prov_oost_vlaanderen,"Optional: extract more OVL named L5 from documentatie (POM invest 200k; political parties; largest lines) or stop if sample enough.",,2026-07-22T14:49:00Z,2026-07-22T14:49:00Z,"Tick90 sampled 5 OVL names; full register public in documentatie"',
    'rq_091,OVL top named werkingssubsidies deepen or POM OVL,continuous,2,done,L5,prov_oost_vlaanderen,"Optional: extract more OVL named L5 from documentatie (POM invest 200k; political parties; largest lines) or stop if sample enough.",,2026-07-22T14:49:00Z,2026-07-22T15:04:00Z,"POM package 2.00m; Erov 1.45m; Polders 2.1m; parties 532k path0; Interreg 1.83m; PDPO 708k; domain economie 20.4m"',
)
if "rq_092," not in rt:
    if not rt.endswith("\n"):
        rt += "\n"
    rt += 'rq_092,Antwerpen or Limburg named L5 subsidies sample,continuous,3,open,L5,prov_antwerpen,"Parallel WVL/OVL: extract 3+ named provincial subsidies/agencies with EUR from public MJP if available.",,2026-07-22T15:04:00Z,2026-07-22T15:04:00Z,"ANT/LIM MJP mapped at L1; L5 name-level thin"\n'
rq.write_text(rt, encoding="utf-8")
print("queue ok")

# state
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    'main,continuous,continuous,2026-07-22T15:04:00Z,rq_091,91,no,"OVL L5 deepen POM 2.0m Erov 1.45m Polders 2.1m (tick91). Next: rq_092 ANT/LIM L5 or rq_089 SWA."\n',
    encoding="utf-8",
)
print("state ok")

# log
log = Path("docs/doge/loop_log.md")
entry = """
### 2026-07-22T15:04:00Z -- tick 91
- Unit: rq_091 (OVL top named werkingssubsidies deepen)
- Found (strong, official Documentatie p4-14): **POM Oost-Vlaanderen package 2026 EUR 2,004,589** (kennis 319k; logistiek 295k; bedrijvencentra 387k; terreinen 387k; verduurzaming 593k; Scheldemond 25k) + invest terreinen **EUR 200,000**. **Erov vzw EUR 1,446,227** (streekproducten 867k; voeding 375k; ambacht 204k). **Polders en Wateringen EUR 2,100,000** (largest single named line; statutory Art18). **Political parties EUR 532,093** (path to **0 in 2031**); fracties 59k. **Interreg cofin 2021-27 EUR 1,830,896**; PDPO Betaalorgaan **EUR 708,000**; noord-zuid 620k; AZORG AHRIA 350k one-off; Bosgroep werking 333k. Domain economie/landbouw/EU werkingssubsidies **EUR 20,423,228**; leefmilieu **EUR 4,858,494**. Total werkingssubsidies **EUR 30,667,884** reconfirmed.
- Wrote: 20 budgets; 5 commitments; 4 leaderboard; entity; sources; rq_091=done; seeded rq_092 ANT/LIM L5; ticks=91
- FOI: none (full named register public in documentatie)
- Next: **rq_092** Antwerpen or Limburg named L5 (prio 3) or **rq_089** SWA Q4 (prio 1)

""".encode("utf-8")
raw = log.read_bytes()
if b"tick 91" not in raw:
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + entry)
    print("log ok")
else:
    print("log exists")

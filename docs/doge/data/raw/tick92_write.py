from pathlib import Path

root = Path("docs/doge/data")

bud = root / "budgets.csv"
t = bud.read_text(encoding="utf-8")
if not t.endswith("\n"):
    t += "\n"
if "bud_lim_pom_2026" not in t:
    t += """bud_lim_pom_2026,prov_limburg,2026,4850000,,,budgeted,src_limburg_prov_amjp_jun2026,strong,POM Limburg verbonden entiteit 2026 EUR 4850000 (AMJP list p124)
bud_lim_toerisme_2026,prov_limburg,2026,4750000,,,budgeted,src_limburg_prov_amjp_jun2026,strong,Toerisme Limburg 2026 EUR 4750000
bud_lim_bokrijk_2026,prov_limburg,2026,6500000,,,budgeted,src_limburg_prov_amjp_jun2026,strong,Het Domein Bokrijk 2026 EUR 6500000 (path down to 2.0m 2031)
bud_lim_diepenbeek_campus_2026,prov_limburg,2026,5000000,,,budgeted,src_limburg_prov_amjp_jun2026,strong,Limburg Diepenbeek campus 2026 EUR 5000000 (path 8m 2027 then down)
bud_lim_pcfruit_2026,prov_limburg,2026,1500000,,,budgeted,src_limburg_prov_amjp_jun2026,strong,Proefcentrum Fruitteelt pcFruit 2026 EUR 1500000
bud_lim_rl_haspengouw_2026,prov_limburg,2026,1150666,,,budgeted,src_limburg_prov_amjp_jun2026,strong,Regionaal Landschap Haspengouw en Voeren 2026 EUR 1150666
bud_lim_rl_kempen_maasland_2026,prov_limburg,2026,475666,,,budgeted,src_limburg_prov_amjp_jun2026,strong,Regionaal Landschap Kempen en Maasland 2026 EUR 475666
bud_lim_rl_lage_kempen_2026,prov_limburg,2026,475666,,,budgeted,src_limburg_prov_amjp_jun2026,strong,Regionaal Landschap Lage Kempen 2026 EUR 475666
bud_lim_rl_sum3_2026,prov_limburg,2026,2101998,,,budgeted,src_limburg_prov_amjp_jun2026,strong,Sum 3 regionale landschappen Limburg 2026 EUR 2101998
bud_lim_pibo_2026,prov_limburg,2026,230000,,,budgeted,src_limburg_prov_amjp_jun2026,strong,PIBO-campus 2026 EUR 230000
bud_lim_pvl_2026,prov_limburg,2026,200000,,,budgeted,src_limburg_prov_amjp_jun2026,strong,Proef- en Vormingscentrum Landbouw PVL 2026 EUR 200000
bud_lim_dommelhof_2026,prov_limburg,2026,150000,,,budgeted,src_limburg_prov_amjp_jun2026,strong,Stichting Dommelhof EVA 2026 EUR 150000
bud_lim_dubolimburg_2026,prov_limburg,2026,185000,,,budgeted,src_limburg_prov_amjp_jun2026,strong,Steunpunt Duurzaam Bouwen Dubolimburg 2026 EUR 185000
bud_lim_top4_entities_2026,prov_limburg,2026,21100000,,,budgeted,src_limburg_prov_amjp_jun2026,strong,Sum Bokrijk+Diepenbeek+POM+Toerisme 2026 EUR 21100000 of total werkingssubsidies 25.9m
bud_ant_apb_werkingssubsidies_2026,prov_antwerpen,2026,38925780,,,budgeted,src_antwerpen_prov_mjp_2026,strong,T2 werkingssubsidies aan eigen APB 2026 EUR 38925780 (13 APBs listed)
bud_ant_subs_andere_2026,prov_antwerpen,2026,22907585,,,budgeted,src_antwerpen_prov_mjp_2026,strong,T2 werkingssubsidies aan andere begunstigden 2026 EUR 22907585
bud_ant_subs_eredienst_2026,prov_antwerpen,2026,743381,,,budgeted,src_antwerpen_prov_mjp_2026,strong,T2 werkingssubsidies eredienst 2026 EUR 743381
bud_ant_subs_nietconf_2026,prov_antwerpen,2026,1251410,,,budgeted,src_antwerpen_prov_mjp_2026,strong,T2 niet-confessionele gemeenschappen 2026 EUR 1251410
bud_ant_vrijetijd_ap_entities_2026,prov_antwerpen,2026,16642250,,,budgeted,src_antwerpen_prov_mjp_2026,strong,AP000061 verzelfstandigde entiteiten vrijetijdsaanbod uitgaven 2026 EUR 16642250
"""
    bud.write_text(t, encoding="utf-8")
    print("budgets ok")
else:
    print("budgets exist")

cmt = root / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
if "cmt_lim_pom_2026" not in ct:
    if not ct.endswith("\n"):
        ct += "\n"
    ct += """cmt_lim_pom_2026,POM Limburg annual provincial financing,prov_limburg,POM Limburg,AMJP verbonden entiteiten list,,2026,2031,4850000,"{""2026"":4850000,""flat_path"":4850000}",0,active,,Provincial economic development,Open POM outcome KPIs,src_limburg_prov_amjp_jun2026,strong,Province_Limburg>POM,Flat 4.85m 2026-31; between WVL 11.7m and OVL 2.0m
cmt_lim_toerisme_2026,Toerisme Limburg annual financing,prov_limburg,Toerisme Limburg,AMJP verbonden entiteiten,,2026,2031,4750000,"{""2026"":4750000}",0,active,,Provincial tourism brand,Visitor economy KPIs,src_limburg_prov_amjp_jun2026,strong,Province_Limburg>Toerisme,Flat 4.75m path
cmt_lim_bokrijk_2026,Domein Bokrijk multi-year financing path,prov_limburg,Het Domein Bokrijk,AMJP verbonden entiteiten,,2026,2031,6500000,"{""2026"":6500000,""2027"":6200000,""2028"":2450000,""2029"":2100000,""2030"":2100000,""2031"":2000000}",0,active,,Heritage recreation domain,Path falls after 2027 capital spike,src_limburg_prov_amjp_jun2026,strong,Province_Limburg>Bokrijk,Largest single named line 6.5m 2026
cmt_lim_diepenbeek_campus_2026,Limburg Diepenbeek campus multi-year path,prov_limburg,Campus Diepenbeek partners,AMJP verbonden entiteiten,,2026,2031,5000000,"{""2026"":5000000,""2027"":8000000,""2028"":6350000,""2029"":2150000,""2030"":500000,""2031"":0}",0,active,,Higher education campus,Capital path peaks 2027,src_limburg_prov_amjp_jun2026,strong,Province_Limburg>Diepenbeek,5m 2026 then 8m 2027
cmt_lim_pcfruit_2026,pcFruit research centre annual financing,prov_limburg,Proefcentrum Fruitteelt,AMJP verbonden entiteiten,,2026,2031,1500000,"{""2026"":1500000}",0,active,,Fruit research,Sector R&D additionality,src_limburg_prov_amjp_jun2026,strong,Province_Limburg>pcFruit,Flat 1.5m
cmt_ant_apb_package_2026,Antwerp APB operating subsidies package 2026,prov_antwerpen,13 autonomous provincial companies,T2 MJP begincrediet,,2026,2026,38925780,"{""apb_total"":38925780,""andere"":22907585,""eredienst"":743381,""nietconf"":1251410,""werking_total"":63828156}",0,active,,Provincial APB ecosystem,Per-APB cash split not in main MJP text,src_antwerpen_prov_mjp_2026,strong,Province_Antwerpen>APB,APB 38.9m of 63.8m werkingssubsidies; 13 APBs named without per-line EUR
"""
    cmt.write_text(ct, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments exist")

lb = root / "leaderboard.csv"
lt = lb.read_text(encoding="utf-8")
if "lb_lim_bokrijk" not in lt:
    if not lt.endswith("\n"):
        lt += "\n"
    lt += """lb_lim_bokrijk,Domein Bokrijk Limburg financing 2026,Flanders,ops,Province_Limburg>Bokrijk,6500000,6500000,6.5m 2026 path to 2.0m 2031; largest LIM named line,strong,src_limburg_prov_amjp_jun2026,Visitors taxpayers,Heritage recreation domain,Core provincial asset; path down after 2027,2,7.5,4,4.9,Publish Bokrijk cost recovery ratio,seed,,tick92
lb_lim_pom,POM Limburg financing 2026,Flanders,subsidy,Province_Limburg>POM,4850000,4850000,Flat 4.85m/yr agency; between WVL 11.7m and OVL 2.0m,strong,src_limburg_prov_amjp_jun2026,Regional economy,Provincial economic middleman,Compare agency perimeters across provinces,3,7.5,4,5.1,Cross-province POM perimeter note,seed,,tick92
lb_lim_toerisme,Toerisme Limburg financing 2026,Flanders,subsidy,Province_Limburg>Toerisme,4750000,4750000,Flat 4.75m tourism brand agency,strong,src_limburg_prov_amjp_jun2026,Tourism sector,Provincial tourism middleman,Compare Westtoer 11.1m / Toerisme OVL 0.6m,3,7,4,4.9,Visitor KPI transparency,seed,,tick92
lb_ant_apb_package,Antwerp APB subsidies package 2026,Flanders,subsidy,Province_Antwerpen>APB,38925780,38925780,38.9m to 13 APBs; per-APB EUR not in main tables,strong,src_antwerpen_prov_mjp_2026,Residents,Provincial company ecosystem,Largest VL province APB block; opacity per company,4,8,4,5.6,Publish per-APB dotatie table,seed,,tick92
"""
    lb.write_text(lt, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard exist")

ent = root / "entities.csv"
et = ent.read_text(encoding="utf-8")
# update limburg and antwerp notes if present
for old, new in [
    ("prov_limburg,", None),  # find line
]:
    pass
lines = []
for line in et.splitlines():
    if line.startswith("prov_limburg,"):
        # replace trailing notes field - last comma-separated
        parts = line.rsplit(",", 1)
        if len(parts) == 2:
            line = parts[0] + ",AMJP 2026: exp 247m cashout 360m; Bokrijk 6.5m; Diepenbeek 5m; POM 4.85m; Toerisme 4.75m; werkingssubsidies 25.9m"
    if line.startswith("prov_antwerpen,"):
        parts = line.rsplit(",", 1)
        if len(parts) == 2:
            line = parts[0] + ",MJP 2026: exp 205m; APB package 38.9m (13 APBs); andere subs 22.9m; werkingssubsidies 63.8m"
    lines.append(line)
ent.write_text("\n".join(lines) + ("\n" if et.endswith("\n") else ""), encoding="utf-8")
print("entities ok")

src = root / "sources.csv"
st = src.read_text(encoding="utf-8")
if "src_limburg_verbonden_entiteiten" not in st:
    if not st.endswith("\n"):
        st += "\n"
    st += 'src_limburg_verbonden_entiteiten,Limburg AMJP 2026 verbonden entiteiten list p122-124,https://raadpleeg-limburg.onlinesmartcities.be/zittingen/26.0108.5431.0816/agendapunten/26.0521.9497.2987,Provincie Limburg,2026-07-22,budget,"Named entity EUR series 2026-31; Bokrijk POM Toerisme Diepenbeek pcFruit landschappen; raw limburg_mjp_jun2026_a.pdf"\n'
    src.write_text(st, encoding="utf-8")
print("sources ok")

rq = root / "research_queue.csv"
rt = rq.read_text(encoding="utf-8")
rt = rt.replace(
    'rq_092,Antwerpen or Limburg named L5 subsidies sample,continuous,3,open,L5,prov_antwerpen,"Parallel WVL/OVL: extract 3+ named provincial subsidies/agencies with EUR from public MJP if available.",,2026-07-22T15:04:00Z,2026-07-22T15:04:00Z,"ANT/LIM MJP mapped at L1; L5 name-level thin"',
    'rq_092,Antwerpen or Limburg named L5 subsidies sample,continuous,3,done,L5,prov_antwerpen,"Parallel WVL/OVL: extract 3+ named provincial subsidies/agencies with EUR from public MJP if available.",,2026-07-22T15:04:00Z,2026-07-22T15:19:00Z,"LIM: Bokrijk 6.5m Diepenbeek 5m POM 4.85m Toerisme 4.75m pcFruit 1.5m RL sum 2.1m; ANT: APB 38.9m andere 22.9m vrijetijd AP 16.6m"',
)
if "rq_093," not in rt:
    if not rt.endswith("\n"):
        rt += "\n"
    rt += 'rq_093,Vlaams-Brabant named L5 subsidies sample,continuous,2,open,L5,prov_vlaams_brabant,"Parallel other VL provinces: extract 3+ named VBR subsidies/agencies with EUR from MJP if public.",,2026-07-22T15:19:00Z,2026-07-22T15:19:00Z,"VBR L1 done; L5 thin; completes 5/5 VL province L5 samples"\n'
rq.write_text(rt, encoding="utf-8")
print("queue ok")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    'main,continuous,continuous,2026-07-22T15:19:00Z,rq_092,92,no,"LIM L5 Bokrijk 6.5m POM 4.85m Toerisme 4.75m; ANT APB 38.9m (tick92). Next: rq_093 VBR L5 or rq_089 SWA."\n',
    encoding="utf-8",
)
print("state ok")

log = Path("docs/doge/loop_log.md")
entry = """
### 2026-07-22T15:19:00Z -- tick 92
- Unit: rq_092 (Antwerpen/Limburg named L5 subsidies sample)
- Found (strong): **Limburg** AMJP verbonden entiteiten p122-124: **Bokrijk EUR 6,500,000** (path to 2.0m 2031); **Diepenbeek campus EUR 5,000,000** (peaks 8.0m 2027); **POM Limburg EUR 4,850,000** (flat); **Toerisme Limburg EUR 4,750,000** (flat); **pcFruit EUR 1,500,000**; 3 regionale landschappen sum **EUR 2,101,998**; Dommelhof 150k; Dubolimburg 185k; PIBO 230k; PVL 200k. Top4 sum **EUR 21.1m** of total werkingssubsidies 25.9m. **Antwerpen** T2: **APB package EUR 38,925,780** (13 named APBs without per-line EUR); andere begunstigden **EUR 22,907,585**; eredienst 743k; niet-conf 1.25m; AP vrijetijd verzelfstandigde entiteiten **EUR 16,642,250**. POM Antwerpen loan guarantee class ~20m outstanding (medium narrative).
- Wrote: 19 budgets; 6 commitments; 4 leaderboard; entities; source; rq_092=done; seeded rq_093 VBR L5; ticks=92
- FOI: none for LIM names; ANT per-APB split still not public in main MJP (optional later FOI)
- Next: **rq_093** Vlaams-Brabant named L5 (prio 2) or **rq_089** SWA Q4 (prio 1)

""".encode("utf-8")
raw = log.read_bytes()
if b"tick 92" not in raw:
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + entry)
    print("log ok")
else:
    print("log exists")

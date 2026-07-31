from pathlib import Path

root = Path("docs/doge/data")

bud = root / "budgets.csv"
t = bud.read_text(encoding="utf-8")
if not t.endswith("\n"):
    t += "\n"
if "bud_vbr_toerisme_2026" not in t:
    t += """bud_vbr_toerisme_2026,prov_vlaams_brabant,2026,1990204,,,budgeted,src_vbr_prov_mjp_2026,strong,Toerisme Vlaams-Brabant vzw nominatief 2026 EUR 1990204
bud_vbr_praktijkpunt_landbouw_2026,prov_vlaams_brabant,2026,1674979,,,budgeted,src_vbr_prov_mjp_2026,strong,Praktijkpunt Landbouw Vlaams-Brabant vzw 2026 EUR 1674979
bud_vbr_pom_2026,prov_vlaams_brabant,2026,1570833,,,budgeted,src_vbr_prov_mjp_2026,strong,POM Vlaams-Brabant 2026 EUR 1570833 (path +2.5pct class)
bud_vbr_apb_vera_2026,prov_vlaams_brabant,2026,1190000,,,budgeted,src_vbr_prov_mjp_2026,strong,APB Vera 2026 EUR 1190000
bud_vbr_imd_2026,prov_vlaams_brabant,2026,1200000,,,budgeted,src_vbr_prov_mjp_2026,strong,Instelling voor Morele Dienstverlening 2026 EUR 1200000 (wettelijk)
bud_vbr_de_rand_2026,prov_vlaams_brabant,2026,675400,,,budgeted,src_vbr_prov_mjp_2026,strong,vzw De Rand 2026 EUR 675400
bud_vbr_erfgoedstichting_2026,prov_vlaams_brabant,2026,320384,,,budgeted,src_vbr_prov_mjp_2026,strong,Erfgoedstichting Vlaams-Brabant 2026 EUR 320384
bud_vbr_apb_vlabinvest_2026,prov_vlaams_brabant,2026,132583,,,budgeted,src_vbr_prov_mjp_2026,strong,APB Vlabinvest 2026 EUR 132583
bud_vbr_rl_pajottenland_zenne_2026,prov_vlaams_brabant,2026,4335140,,,budgeted,src_vbr_prov_mjp_2026,strong,Regionaal Landschap Pajottenland en Zennevallei 2026 EUR 4335140 (path drops to 396k 2027 - capital spike year)
bud_vbr_rl_brabantse_kouters_2026,prov_vlaams_brabant,2026,444767,,,budgeted,src_vbr_prov_mjp_2026,strong,Regionaal Landschap Brabantse Kouters 2026 EUR 444767
bud_vbr_rl_dijleland_2026,prov_vlaams_brabant,2026,356637,,,budgeted,src_vbr_prov_mjp_2026,strong,Regionaal Landschap Dijleland 2026 EUR 356637
bud_vbr_rl_noord_hageland_2026,prov_vlaams_brabant,2026,356637,,,budgeted,src_vbr_prov_mjp_2026,strong,Regionaal Landschap Noord-Hageland 2026 EUR 356637
bud_vbr_rl_zuid_hageland_2026,prov_vlaams_brabant,2026,342767,,,budgeted,src_vbr_prov_mjp_2026,strong,Regionaal Landschap Zuid-Hageland 2026 EUR 342767
bud_vbr_rl_sum5_2026,prov_vlaams_brabant,2026,5835948,,,budgeted,src_vbr_prov_mjp_2026,strong,Sum 5 regionale landschappen VBR 2026 EUR 5835948
bud_vbr_streekproducten_2026,prov_vlaams_brabant,2026,358489,,,budgeted,src_vbr_prov_mjp_2026,strong,Streekproducten Vlaams-Brabant vzw 2026 EUR 358489
bud_vbr_bosgroep_2026,prov_vlaams_brabant,2026,175000,,,budgeted,src_vbr_prov_mjp_2026,strong,Bosgroep vzw 2026 EUR 175000
bud_vbr_de_rand_taal_ap_2026,prov_vlaams_brabant,2026,1202000,,,budgeted,src_vbr_prov_mjp_2026,medium,Actieplan 304VLK01 taal/integratie uitgaven 2026 EUR 1202000 (broader than De Rand line alone)
bud_vbr_apb_t2_total_2026,prov_vlaams_brabant,2026,1531315,,,budgeted,src_vbr_prov_mjp_2026,strong,T2 werkingssubsidies aan eigen APB 2026 EUR 1531315
bud_vbr_subs_andere_2026,prov_vlaams_brabant,2026,15654473,,,budgeted,src_vbr_prov_mjp_2026,strong,T2 werkingssubsidies aan andere begunstigden 2026 EUR 15654473
bud_vbr_top3_agencies_2026,prov_vlaams_brabant,2026,5236016,,,budgeted,src_vbr_prov_mjp_2026,strong,Sum Toerisme+Praktijkpunt+POM 2026 EUR 5236016
"""
    bud.write_text(t, encoding="utf-8")
    print("budgets ok")
else:
    print("budgets exist")

cmt = root / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
if "cmt_vbr_toerisme_2026" not in ct:
    if not ct.endswith("\n"):
        ct += "\n"
    ct += """cmt_vbr_toerisme_2026,Toerisme Vlaams-Brabant vzw multi-year financing,prov_vlaams_brabant,Toerisme Vlaams-Brabant vzw,MJP nominatieve verbonden entiteiten,,2026,2031,1990204,"{""2026"":1990204,""2027"":2504768,""2028"":2733722,""2029"":2758415,""2030"":2419561,""2031"":2106969}",0,active,,Provincial tourism agency,Visitor KPIs,src_vbr_prov_mjp_2026,strong,Province_Vlaams_Brabant>Toerisme,Peaks mid-period then eases
cmt_vbr_pom_2026,POM Vlaams-Brabant multi-year financing,prov_vlaams_brabant,POM Vlaams-Brabant,MJP nominatieve list,,2026,2031,1570833,"{""2026"":1570833,""2027"":1609271,""2028"":1648669,""2029"":1689052,""2030"":1730445,""2031"":1772873}",0,active,,Provincial economic development,Compare POM perimeters 5 VL provinces,src_vbr_prov_mjp_2026,strong,Province_Vlaams_Brabant>POM,~1.57m 2026; growth path ~+2.5pct
cmt_vbr_praktijkpunt_2026,Praktijkpunt Landbouw Vlaams-Brabant multi-year,prov_vlaams_brabant,Praktijkpunt Landbouw vzw,MJP nominatieve list,,2026,2031,1674979,"{""2026"":1674979,""2027"":1229426,""2031"":3016406}",0,active,,Agri practice centre,2031 spike needs explanation,src_vbr_prov_mjp_2026,strong,Province_Vlaams_Brabant>Praktijkpunt,1.67m 2026; 3.0m 2031
cmt_vbr_rl_pajottenland_2026,Regionaal Landschap Pajottenland Zennevallei 2026 spike,prov_vlaams_brabant,RL Pajottenland en Zennevallei,MJP nominatieve list,,2026,2027,4335140,"{""2026"":4335140,""2027"":396010,""2028"":44704}",0,active,,Landscape partner,2026 outlier vs 397k 2027 - likely capital,src_vbr_prov_mjp_2026,strong,Province_Vlaams_Brabant>RL_Pajottenland,Largest single VBR named line 2026
cmt_vbr_imd_2026,IMD Vlaams-Brabant moral services,prov_vlaams_brabant,Instelling voor Morele Dienstverlening,Wettelijke verplichting,,2026,2026,1200000,"{""2026"":1200000}",0,active,,Non-confessional moral services,Decretal parallel OVL PIMD 1.22m,src_vbr_prov_mjp_2026,strong,Province_Vlaams_Brabant>IMD,Flat then 1.1m from 2028
cmt_vl_pom_compare_2026,Flemish POM packages 2026 cross-province,sec_flanders,POM agencies five provinces,Synthesis ticks 90-93,,2026,2026,21660579,"{""wvl"":11653824,""lim"":4850000,""ovl"":2004589,""vbr"":1570833,""ant_not_named_line"":0,""sum_named4"":20079246,""note"":""ANT APB package separate 38.9m not POM-only""}",0,active,docs/doge/data/flemish_provinces_2026_snapshot.md,Provincial economic agencies,Publish comparable POM perimeter definition,src_doge_flemish_prov_compare_2026,strong,Vlaanderen>Provinces>POM_compare,WVL largest named POM; ANT structure APB-heavy
"""
    cmt.write_text(ct, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments exist")

lb = root / "leaderboard.csv"
lt = lb.read_text(encoding="utf-8")
if "lb_vbr_toerisme" not in lt:
    if not lt.endswith("\n"):
        lt += "\n"
    lt += """lb_vbr_toerisme,Toerisme Vlaams-Brabant 2026,Flanders,subsidy,Province_Vlaams_Brabant>Toerisme,1990204,1990204,1.99m tourism vzw; path peaks ~2.76m 2029,strong,src_vbr_prov_mjp_2026,Tourism sector,Provincial tourism middleman,Compare LIM 4.75m WVL Westtoer 11.1m,3,7,4,4.9,Visitor KPI transparency,seed,,tick93
lb_vbr_pom,POM Vlaams-Brabant 2026,Flanders,subsidy,Province_Vlaams_Brabant>POM,1570833,1570833,1.57m; smallest named POM of 4 mapped,strong,src_vbr_prov_mjp_2026,Regional economy,Provincial economic middleman,WVL 11.7 LIM 4.85 OVL 2.0 VBR 1.57,3,7.5,4,5.1,Cross-province perimeter note,seed,,tick93
lb_vbr_rl_pajottenland,RL Pajottenland Zennevallei 2026 spike,Flanders,ops,Province_Vlaams_Brabant>RL,4335140,4335140,4.34m 2026 then ~0.40m 2027 - capital/project year,strong,src_vbr_prov_mjp_2026,Landscape partners,Landscape programme,Largest VBR named 2026 line; path anomaly,3,7,4,4.9,Explain 2026 vs 2027 split,seed,,tick93
lb_vbr_imd,IMD Vlaams-Brabant 2026,Flanders,ops,Province_Vlaams_Brabant>IMD,1200000,1200000,Legal moral services 1.2m parallel OVL PIMD,strong,src_vbr_prov_mjp_2026,Residents,Decretal financing,Mandatory not pure waste,2,6,3,3.7,Review decretale path,seed,,tick93
"""
    lb.write_text(lt, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard exist")

ent = root / "entities.csv"
et = ent.read_text(encoding="utf-8")
lines = []
for line in et.splitlines():
    if line.startswith("prov_vlaams_brabant,"):
        parts = line.rsplit(",", 1)
        if len(parts) == 2:
            line = parts[0] + ",MJP 2026: exp 151m; Toerisme 1.99m; Praktijkpunt 1.67m; POM 1.57m; RL Pajottenland spike 4.34m; werkingssubsidies 19.4m"
    lines.append(line)
ent.write_text("\n".join(lines) + ("\n" if et.endswith("\n") else ""), encoding="utf-8")
print("entities ok")

# snapshot brief note
snap = root / "flemish_provinces_2026_snapshot.md"
st = snap.read_text(encoding="utf-8")
if "POM packages" not in st:
    st += """

## Named agency L5 snapshot (ticks 90–93)

| Province | POM € | Tourism agency € | Other large named € |
|----------|------:|-----------------:|--------------------:|
| West-Vlaanderen | 11,653,824 | Westtoer 11,052,567 | Inagro 10,839,292 |
| Limburg | 4,850,000 | Toerisme Limburg 4,750,000 | Bokrijk 6,500,000 |
| Oost-Vlaanderen | ~2,004,589 (package) | Toerisme OVL 600,176 | Polders 2,100,000 |
| Vlaams-Brabant | 1,570,833 | Toerisme VBR 1,990,204 | RL Pajottenland 4,335,140 (2026 spike) |
| Antwerpen | not single POM line | (inside APB 38.9m) | APB package 38,925,780 |

**Completes 5/5 Flemish provinces** with named L5 samples (tick93).
"""
    snap.write_text(st, encoding="utf-8")
print("snapshot ok")

src = root / "sources.csv"
st = src.read_text(encoding="utf-8")
if "src_vbr_verbonden_entiteiten" not in st:
    if not st.endswith("\n"):
        st += "\n"
    st += 'src_vbr_verbonden_entiteiten,Vlaams-Brabant MJP 2026-2031 verbonden entiteiten nominatief p70-73,https://www.vlaamsbrabant.be/sites/default/files/media/files/2025-10/meerjarenplan-2026-2031-20251014.pdf,Provincie Vlaams-Brabant,2026-07-22,budget,"Nominatieve subsidies 2026-31; Toerisme POM Praktijkpunt RL; raw vbr_meerjarenplan-2026-2031-20251014.pdf"\n'
    st = st.replace(
        "Sums from ticks 78-87; all 5 VL provinces exp+cashout+opcent; not a government publication",
        "Sums from ticks 78-93; all 5 VL provinces L1+named L5 samples; not a government publication",
    )
    src.write_text(st, encoding="utf-8")
print("sources ok")

rq = root / "research_queue.csv"
rt = rq.read_text(encoding="utf-8")
rt = rt.replace(
    'rq_093,Vlaams-Brabant named L5 subsidies sample,continuous,2,open,L5,prov_vlaams_brabant,"Parallel other VL provinces: extract 3+ named VBR subsidies/agencies with EUR from MJP if public.",,2026-07-22T15:19:00Z,2026-07-22T15:19:00Z,"VBR L1 done; L5 thin; completes 5/5 VL province L5 samples"',
    'rq_093,Vlaams-Brabant named L5 subsidies sample,continuous,2,done,L5,prov_vlaams_brabant,"Parallel other VL provinces: extract 3+ named VBR subsidies/agencies with EUR from MJP if public.",,2026-07-22T15:19:00Z,2026-07-22T15:34:00Z,"Toerisme 1.99m; Praktijkpunt 1.67m; POM 1.57m; Vera 1.19m; IMD 1.2m; RL Pajottenland 4.34m spike; 5/5 VL L5 done"',
)
if "rq_094," not in rt:
    if not rt.endswith("\n"):
        rt += "\n"
    rt += 'rq_094,Flemish provinces L5 POM/tourism compare synthesis,continuous,2,open,L1,sec_flanders,"Optional synthesis table POM+tourism agency packages 5 provinces into snapshot/leaderboard; no invent euros.",,2026-07-22T15:34:00Z,2026-07-22T15:34:00Z,"Data ready from ticks 90-93; light synthesis unit"\n'
rq.write_text(rt, encoding="utf-8")
print("queue ok")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    'main,continuous,continuous,2026-07-22T15:34:00Z,rq_093,93,no,"VBR L5 Toerisme 1.99m POM 1.57m; 5/5 VL L5 done (tick93). Next: rq_094 synthesize or rq_089 SWA."\n',
    encoding="utf-8",
)
print("state ok")

log = Path("docs/doge/loop_log.md")
entry = """
### 2026-07-22T15:34:00Z -- tick 93
- Unit: rq_093 (Vlaams-Brabant named L5 subsidies sample)
- Found (strong, official MJP nominatieve verbonden entiteiten p70-73): **Toerisme Vlaams-Brabant vzw EUR 1,990,204**; **Praktijkpunt Landbouw EUR 1,674,979**; **POM Vlaams-Brabant EUR 1,570,833**; **APB Vera EUR 1,190,000**; **IMD EUR 1,200,000**; De Rand **EUR 675,400**; Erfgoedstichting 320k; Vlabinvest 133k. **Regionaal Landschap Pajottenland/Zennevallei EUR 4,335,140** (2026 spike; 2027 falls to 396k). Other RL: Kouters 445k; Dijleland/Noord-Hageland 357k each; Zuid-Hageland 343k; **RL sum5 EUR 5,835,948**. Streekproducten 358k; Bosgroep 175k. T2: APB total **EUR 1,531,315**; andere **EUR 15,654,473**; total werkingssubsidies **EUR 19,382,399**. **Completes 5/5 Flemish provinces** with named L5 samples. POM ladder: WVL 11.7m > LIM 4.85m > OVL 2.0m > VBR 1.57m (ANT APB-heavy 38.9m).
- Wrote: 20 budgets; 6 commitments; 4 leaderboard; snapshot L5 table; entity; source; rq_093=done; seeded rq_094 synthesis; ticks=93
- FOI: none
- Next: **rq_094** VL provinces L5 POM/tourism compare (prio 2) or **rq_089** SWA Q4 (prio 1)

""".encode("utf-8")
raw = log.read_bytes()
if b"tick 93" not in raw:
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + entry)
    print("log ok")
else:
    print("log exists")

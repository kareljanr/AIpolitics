from pathlib import Path

root = Path("docs/doge/data")

# numbers (strong primary rows ticks 90-93 only)
WVL_POM = 11653824
WVL_WESTTOER = 11052567
WVL_INAGRO = 10839292
WVL_TUA = 385000
WVL_AGENCIES = 33930683
WVL_WERK = 54431043
LIM_POM = 4850000
LIM_TOER = 4750000
LIM_BOKRIJK = 6500000
LIM_WERK = 25865989
OVL_POM = 2004589
OVL_TOER = 600176
OVL_WERK = 30667884
VBR_POM = 1570833
VBR_TOER = 1990204
VBR_WERK = 19382399
ANT_APB = 38925780
ANT_ANDERE = 22907585
ANT_WERK = 63828156

POM4 = WVL_POM + LIM_POM + OVL_POM + VBR_POM  # 20079246
TOER4 = WVL_WESTTOER + LIM_TOER + OVL_TOER + VBR_TOER  # 18392947
POM_TOER4 = POM4 + TOER4  # 38472193
WERK5 = WVL_WERK + LIM_WERK + OVL_WERK + VBR_WERK + ANT_WERK  # sum

bud = root / "budgets.csv"
t = bud.read_text(encoding="utf-8")
if not t.endswith("\n"):
    t += "\n"
if "bud_vl_pom_sum4_2026" not in t:
    t += f"""bud_vl_pom_sum4_2026,sec_flanders,2026,{POM4},,,budgeted,src_doge_flemish_l5_compare_2026,strong,Sum named POM packages WVL+LIM+OVL+VBR 2026 (ANT not single POM line)
bud_vl_tourism_agency_sum4_2026,sec_flanders,2026,{TOER4},,,budgeted,src_doge_flemish_l5_compare_2026,strong,Sum named tourism agencies Westtoer+LIM+OVL+VBR 2026
bud_vl_pom_tourism_sum4_2026,sec_flanders,2026,{POM_TOER4},,,budgeted,src_doge_flemish_l5_compare_2026,strong,Sum POM4+tourism4 named packages 2026
bud_vl_werkingssubsidies_sum5_2026,sec_flanders,2026,{WERK5},,,budgeted,src_doge_flemish_l5_compare_2026,strong,Sum toegestane werkingssubsidies 5 VL provinces 2026
bud_vl_ant_apb_package_2026,sec_flanders,2026,{ANT_APB},,,budgeted,src_doge_flemish_l5_compare_2026,strong,Antwerp APB package cross-ref (not POM-equivalent perimeter)
"""
    bud.write_text(t, encoding="utf-8")
    print("budgets ok", POM4, TOER4, WERK5)
else:
    print("budgets exist")

cmt = root / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
if "cmt_vl_pom_tourism_compare_2026" not in ct:
    if not ct.endswith("\n"):
        ct += "\n"
    ct += f"""cmt_vl_pom_tourism_compare_2026,Flemish provinces POM and tourism agency packages 2026,sec_flanders,Provincial agencies Flanders,Synthesis DOGE ticks 90-93,,2026,2026,{POM_TOER4},"{{\\"pom_sum4\\":{POM4},\\"tourism_sum4\\":{TOER4},\\"wvl_pom\\":{WVL_POM},\\"lim_pom\\":{LIM_POM},\\"ovl_pom\\":{OVL_POM},\\"vbr_pom\\":{VBR_POM},\\"wvl_westtoer\\":{WVL_WESTTOER},\\"lim_toer\\":{LIM_TOER},\\"ovl_toer\\":{OVL_TOER},\\"vbr_toer\\":{VBR_TOER},\\"ant_apb\\":{ANT_APB},\\"werking_sum5\\":{WERK5}}}",0,active,docs/doge/data/flemish_provinces_l5_agencies_2026.md,Provincial middleman layer,Harmonise POM perimeter definitions; open ANT per-APB,src_doge_flemish_l5_compare_2026,strong,Vlaanderen>Provinces>POM_Tourism_2026,Named POM+tourism 4-prov ~38.5m; ANT APB 38.9m separate perimeter
"""
    cmt.write_text(ct, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments exist")

lb = root / "leaderboard.csv"
lt = lb.read_text(encoding="utf-8")
if "lb_vl_pom_tourism_opacity" not in lt:
    if not lt.endswith("\n"):
        lt += "\n"
    lt += f"""lb_vl_pom_tourism_opacity,Flemish provincial POM/tourism agency stack 2026,Flanders,subsidy,Vlaanderen>Provinces>agencies,{POM_TOER4},{POM_TOER4 + ANT_APB},Named POM+tourism 4-prov {POM_TOER4}; ANT APB separate {ANT_APB}; perimeter not comparable,strong,src_doge_flemish_l5_compare_2026,Taxpayers,Provincial outsourced middle layer,WVL dominates POM+tourism; ANT uses APB model,4,8,5,5.7,Publish harmonised agency register 5 provinces,seed,,tick94
lb_vl_werkingssubsidies_sum5,Flemish 5 provinces werkingssubsidies total 2026,Flanders,subsidy,Vlaanderen>Provinces>werkingssubsidies,{WERK5},{WERK5},Sum toegestane werkingssubsidies 5 provinces ~{WERK5/1e6:.0f}m,strong,src_doge_flemish_l5_compare_2026,Partners agencies,Provincial grant layer,ANT largest 63.8m; VBR smallest 19.4m,3,8,4,5.3,Open name-level all five,seed,,tick94
"""
    lb.write_text(lt, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard exist")

# dedicated synthesis md
md = f"""# Flemish provinces — named agency L5 compare 2026

Synthesis only from DOGE ticks 90–93 primary rows. **No invented euros.**

## Caveats

- **POM perimeter differs** by province: WVL is a single annual dotatie line; OVL is a sum of named werking lines; LIM/VBR are single nominatieve lines; Antwerpen finances via a large **APB package** (13 companies) rather than a single POM line in the extracted tables.
- **Tourism perimeter differs**: Westtoer is APB; LIM/VBR/OVL are vzw/agency lines of different breadth.
- Do **not** sum POM + ANT APB as “one metric” without caveats.

## POM-class packages 2026

| Province | Amount € | Source style | Share of own werkingssubsidies |
|----------|----------:|--------------|-------------------------------:|
| West-Vlaanderen | {WVL_POM:,} | single dotatie | {100*WVL_POM/WVL_WERK:.1f}% |
| Limburg | {LIM_POM:,} | nominatief entiteit | {100*LIM_POM/LIM_WERK:.1f}% |
| Oost-Vlaanderen | {OVL_POM:,} | sum named werking lines | {100*OVL_POM/OVL_WERK:.1f}% |
| Vlaams-Brabant | {VBR_POM:,} | nominatief entiteit | {100*VBR_POM/VBR_WERK:.1f}% |
| Antwerpen | n/a single line | APB stack (see below) | n/a |
| **Sum named 4** | **{POM4:,}** | | |

**Rank POM-class:** WVL > LIM > OVL > VBR.

## Tourism agency packages 2026

| Province | Amount € | Name |
|----------|----------:|------|
| West-Vlaanderen | {WVL_WESTTOER:,} | Westtoer APB |
| Limburg | {LIM_TOER:,} | Toerisme Limburg |
| Vlaams-Brabant | {VBR_TOER:,} | Toerisme Vlaams-Brabant vzw |
| Oost-Vlaanderen | {OVL_TOER:,} | vzw Toerisme Oost-Vlaanderen (2 lines) |
| Antwerpen | inside APB | Toerisme Provincie Antwerpen (no separate EUR in extract) |
| **Sum named 4** | **{TOER4:,}** | |

**Rank tourism:** WVL > LIM > VBR > OVL.

## Combined named POM + tourism (4 provinces)

| Metric | Amount € |
|--------|---------:|
| POM sum 4 | {POM4:,} |
| Tourism sum 4 | {TOER4:,} |
| **Combined** | **{POM_TOER4:,}** |

West-Vlaanderen alone accounts for **{(WVL_POM+WVL_WESTTOER)/POM_TOER4*100:.0f}%** of the 4-province POM+tourism sum ({WVL_POM+WVL_WESTTOER:,} of {POM_TOER4:,}).

## WVL four-agency stack (context)

| Agency | 2026 € |
|--------|-------:|
| POM | {WVL_POM:,} |
| Westtoer | {WVL_WESTTOER:,} |
| Inagro | {WVL_INAGRO:,} |
| TUA WEST | {WVL_TUA:,} |
| **Sum** | **{WVL_AGENCIES:,}** |
| Share of WVL werkingssubsidies | {100*WVL_AGENCIES/WVL_WERK:.0f}% |

## Antwerpen APB package (non-comparable perimeter)

| Line | 2026 € |
|------|-------:|
| Toegestane werkingssubsidies to own APB | {ANT_APB:,} |
| Andere begunstigden | {ANT_ANDERE:,} |
| Total werkingssubsidies | {ANT_WERK:,} |

APB package is **larger than the entire 4-province POM sum** ({ANT_APB:,} vs {POM4:,}) but covers 13 provincial companies (education, recreation, tourism, etc.), not economic development alone.

## Total werkingssubsidies 5 provinces 2026

| Province | Werkingssubsidies € |
|----------|-------------------:|
| Antwerpen | {ANT_WERK:,} |
| West-Vlaanderen | {WVL_WERK:,} |
| Oost-Vlaanderen | {OVL_WERK:,} |
| Limburg | {LIM_WERK:,} |
| Vlaams-Brabant | {VBR_WERK:,} |
| **Sum 5** | **{WERK5:,}** |

## Other large named lines (context, not in POM/tourism sums)

| Province | Line | 2026 € |
|----------|------|-------:|
| Limburg | Domein Bokrijk | {LIM_BOKRIJK:,} |
| Oost-Vlaanderen | Polders en Wateringen | 2,100,000 |
| Vlaams-Brabant | RL Pajottenland/Zennevallei (spike year) | 4,335,140 |
| West-Vlaanderen | Inagro (already in 4-agency) | {WVL_INAGRO:,} |

## Sources

src_westvl_prov_mjp_2026; src_limburg_prov_amjp_jun2026; src_oostvl_prov_mjp_documentatie_2026; src_vbr_prov_mjp_2026; src_antwerpen_prov_mjp_2026; src_doge_flemish_l5_compare_2026.

Parallel L1 snapshot: `flemish_provinces_2026_snapshot.md`.
"""
(root / "flemish_provinces_l5_agencies_2026.md").write_text(md, encoding="utf-8")
print("md ok")

# update main snapshot header and append if needed
snap = root / "flemish_provinces_2026_snapshot.md"
st = snap.read_text(encoding="utf-8")
st = st.replace(
    "Synthesis from DOGE ticks 78–87 primary rows. **No invented euros.**",
    "Synthesis from DOGE ticks 78–94 primary rows. **No invented euros.**",
)
if "flemish_provinces_l5_agencies_2026.md" not in st:
    st += f"""

## Agency L5 compare (tick 94)

See full table: [`flemish_provinces_l5_agencies_2026.md`](flemish_provinces_l5_agencies_2026.md).

| Metric | Amount € |
|--------|---------:|
| POM named sum 4 provinces | {POM4:,} |
| Tourism agency sum 4 provinces | {TOER4:,} |
| POM+tourism 4 provinces | {POM_TOER4:,} |
| Werkingssubsidies sum 5 provinces | {WERK5:,} |
| Antwerpen APB package (separate perimeter) | {ANT_APB:,} |

**POM rank:** WVL €11.7m > LIM €4.85m > OVL €2.0m > VBR €1.57m.  
**Tourism rank:** WVL €11.1m > LIM €4.75m > VBR €1.99m > OVL €0.60m.
"""
snap.write_text(st, encoding="utf-8")
print("snapshot ok")

src = root / "sources.csv"
st = src.read_text(encoding="utf-8")
if "src_doge_flemish_l5_compare_2026" not in st:
    if not st.endswith("\n"):
        st += "\n"
    st += 'src_doge_flemish_l5_compare_2026,DOGE synthesis Flemish provinces named POM tourism L5 2026,docs/doge/data/flemish_provinces_l5_agencies_2026.md,AIpolitics DOGE loop,2026-07-22,secondary,"Sums only from ticks 90-93 primary nominatieve/dotatie rows; perimeter caveats; not a government publication"\n'
    src.write_text(st, encoding="utf-8")
print("sources ok")

rq = root / "research_queue.csv"
rt = rq.read_text(encoding="utf-8")
rt = rt.replace(
    'rq_094,Flemish provinces L5 POM/tourism compare synthesis,continuous,2,open,L1,sec_flanders,"Optional synthesis table POM+tourism agency packages 5 provinces into snapshot/leaderboard; no invent euros.",,2026-07-22T15:34:00Z,2026-07-22T15:34:00Z,"Data ready from ticks 90-93; light synthesis unit"',
    f'rq_094,Flemish provinces L5 POM/tourism compare synthesis,continuous,2,done,L1,sec_flanders,"Optional synthesis table POM+tourism agency packages 5 provinces into snapshot/leaderboard; no invent euros.",,2026-07-22T15:34:00Z,2026-07-22T15:49:00Z,"POM4 {POM4}; tourism4 {TOER4}; combined {POM_TOER4}; werk5 {WERK5}; ANT APB {ANT_APB} separate"',
)
if "rq_095," not in rt:
    if not rt.endswith("\n"):
        rt += "\n"
    rt += 'rq_095,Walloon province L5 named subsidies sample (Hainaut or Liege),continuous,3,open,L5,prov_hainaut,"Parallel VL L5: extract 3+ named Walloon province subsidies/ASBL from CoA or budget PDF.",,2026-07-22T15:49:00Z,2026-07-22T15:49:00Z,"Walloon L1 complete; L5 thin vs VL agencies"\n'
rq.write_text(rt, encoding="utf-8")
print("queue ok")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,continuous,2026-07-22T15:49:00Z,rq_094,94,no,"VL L5 synthesize POM4 {POM4/1e6:.1f}m tourism4 {TOER4/1e6:.1f}m (tick94). Next: rq_095 Walloon L5 or rq_089 SWA."\n',
    encoding="utf-8",
)
print("state ok")

log = Path("docs/doge/loop_log.md")
entry = f"""
### 2026-07-22T15:49:00Z -- tick 94
- Unit: rq_094 (Flemish provinces L5 POM/tourism compare synthesis)
- Found (strong synthesis, no new primary PDF): From ticks 90-93 only. **POM named sum 4 provinces EUR {POM4:,}** (WVL {WVL_POM:,} > LIM {LIM_POM:,} > OVL {OVL_POM:,} > VBR {VBR_POM:,}). **Tourism agency sum 4 EUR {TOER4:,}** (Westtoer {WVL_WESTTOER:,} > LIM {LIM_TOER:,} > VBR {VBR_TOER:,} > OVL {OVL_TOER:,}). **Combined POM+tourism 4 EUR {POM_TOER4:,}** (WVL alone {(WVL_POM+WVL_WESTTOER)/POM_TOER4*100:.0f}%). **Werkingssubsidies sum 5 EUR {WERK5:,}** (ANT {ANT_WERK:,} largest). **Antwerp APB package EUR {ANT_APB:,}** is **not** POM-equivalent (13 companies; larger than POM4 alone). Perimeter caveats documented.
- Wrote: flemish_provinces_l5_agencies_2026.md; 5 budgets; 1 commitment; 2 leaderboard; snapshot update; source; rq_094=done; seeded rq_095 Walloon L5; ticks=94
- FOI: none (synthesis of public extracts)
- Next: **rq_095** Walloon province L5 sample (prio 3) or **rq_089** SWA Q4 (prio 1)

""".encode("utf-8")
raw = log.read_bytes()
if b"tick 94" not in raw:
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + entry)
    print("log ok")
else:
    print("log exists")

from pathlib import Path

root = Path("docs/doge/data")

# sources
src = root / "sources.csv"
t = src.read_text(encoding="utf-8")
if not t.endswith("\n"):
    t += "\n"
if "src_oostvl_prov_mjp_documentatie_2026" not in t:
    t += (
        "src_oostvl_prov_mjp_documentatie_2026,"
        "Provincie Oost-Vlaanderen MJP 2026-2031 Documentatie (T2 totals),"
        "https://provincieoost-vlaanderen.beleidsportaal.be/Data/c66a5628-79bb-4bfa-a5e1-669708b8200e/Public/meerjarenplan-2026-2031%20-%20documentatie.pdf,"
        "Provincie Oost-Vlaanderen,2026-07-22,budget,"
        '"Documentatie 44p; Totalen budget 2026 exp uit 313167169 ont 327535846; inv 62639681 fin uit 4048851; raw oostvl_meerjarenplan-2026-2031_documentatie.pdf"\n'
        "src_ovl_mjp_press_vrt,"
        "VRT NWS Oost-Vlaanderen MJP 2026 tax cut and invest 400m,"
        "https://www.vrt.be/vrtnws/nl/2025/12/04/oost-vlaanderen-belasting-daalt-mobiliteit-water-recreatie-moens/,"
        "VRT NWS (secondary),2026-07-22,press,"
        '"Cross-check: opposition cites ~330m uitgaven/yr class; invest 400m period; not primary vs documentatie"\n'
    )
t = t.replace(
    "Sums from ticks 78-85 primary rows; WVL exp filled tick85; OVL full exp still n/a; not a government publication",
    "Sums from ticks 78-86; WVL+OVL exp filled; all 5 VL provinces exp+cashout; not a government publication",
)
src.write_text(t, encoding="utf-8")
print("sources ok")

# entities
ent = root / "entities.csv"
et = ent.read_text(encoding="utf-8")
old = "prov_oost_vlaanderen,Provincie Oost-Vlaanderen,Province de Flandre orientale,Province of East Flanders,province,sec_flanders,nl,https://oost-vlaanderen.be,,,MJP 2026-2031 PR 3 Dec 2025; invest ~400m/6y; pers 212m; tax 181.6m; debt EOY26 17.4m"
new = "prov_oost_vlaanderen,Provincie Oost-Vlaanderen,Province de Flandre orientale,Province of East Flanders,province,sec_flanders,nl,https://oost-vlaanderen.be,,,MJP 2026-2031; exp uit 313.2m ont 327.5m cashout 379.9m; invest ~400m/6y; pers 212m"
if old in et:
    ent.write_text(et.replace(old, new), encoding="utf-8")
    print("entity ok")
else:
    print("entity not matched")

# research queue
rq = root / "research_queue.csv"
rt = rq.read_text(encoding="utf-8")
rt = rt.replace(
    'rq_085,Oost-Vlaanderen full exploitatie-uitgaven 2026 from T2,continuous,3,open,L1,prov_oost_vlaanderen,"Extract full exp uit/ont 2026 from OVL MJP T2 (parallel WVL rq_083) to close last Flemish province exp gap.",,2026-07-22T13:34:00Z,2026-07-22T13:34:00Z,"Beleidsverklaring lacks full exp; need T2 or alternate PDF"',
    'rq_085,Oost-Vlaanderen full exploitatie-uitgaven 2026 from T2,continuous,3,done,L1,prov_oost_vlaanderen,"Extract full exp uit/ont 2026 from OVL MJP T2 (parallel WVL rq_083) to close last Flemish province exp gap.",,2026-07-22T13:34:00Z,2026-07-22T13:49:00Z,"Documentatie Totalen: exp uit 313167169 ont 327535846 saldo 14368677; inv 62639681 fin 4048851 cashout 379855701; subs granted 30667884"',
)
if "rq_086," not in rt:
    if not rt.endswith("\n"):
        rt += "\n"
    rt += 'rq_086,West-Vlaanderen opcentiemen 2026 digitise from MJP chart,continuous,2,open,L1,prov_west_vlaanderen,"Digitise WVL opcentiemen EUR 2026 from MJP chart/text to complete 5-prov opcent sum; no invent euros.",,2026-07-22T13:49:00Z,2026-07-22T13:49:00Z,"Rate 186.22 known; EUR chart not digitised tick79/85"\n'
rq.write_text(rt, encoding="utf-8")
print("queue ok")

# loop state
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    'main,continuous,continuous,2026-07-22T13:49:00Z,rq_085,86,no,"OVL exp 313.2m cashout 379.9m (tick86). Next: rq_086 WVL opcent or rq_084 SWA recheck."\n',
    encoding="utf-8",
)
print("state ok")

# snapshot
snap = """# Flemish provinces budget 2026 — comparative snapshot

Synthesis from DOGE ticks 78–86 primary rows. **No invented euros.**

## Caveats

- **Accounting:** Flemish BBC (exploitatie/investering/financiering), not Walloon ordinaire/extraordinaire.
- **West-Vlaanderen:** Schema M2 p15 strong (tick 85); werkingssubsidies ~€55m still **medium**; opcentiemen EUR not digitised.
- **Oost-Vlaanderen:** Documentatie Totalen budget 2026 strong (tick 86); personnel includes large VL-gesubsidieerd onderwijs pass-through.
- **Personnel:** OVL and Limburg include large VL-gesubsidieerd onderwijs pass-through; Antwerp/VBR smaller onderwijs share.
- **Cash-out** = exp + invest + financing uitgaven (all 5 provinces complete).

## Table (2026 unless noted)

| Province | Exp uit € | Inv 2026 € | Cash-out € | Opcentiemen € | Personeel € | Debt € | Inv period 2026-31 € |
|----------|----------:|-----------:|-----------:|--------------:|------------:|-------:|---------------------:|
| Oost-Vlaanderen | 313,167,169 | 62,639,681 | 379,855,701 | 110,542,196 | 211,963,313 | 17,380,658 | 399,702,621 |
| Limburg | 247,304,270 | 106,147,542 | 360,281,175 | 90,933,687 | 173,828,351 | 127,017,316 | 272,275,476 |
| West-Vlaanderen | 194,441,409 | 70,132,288 | 283,945,511 | n/a (rate 186.22) | n/a | 92,341,480 start | 363,500,000 |
| Antwerpen | 204,700,675 | 60,420,600 | 274,336,275 | 172,132,240 | 92,014,823 | 19,895,000 | n/a in CSV |
| Vlaams-Brabant | 150,983,589 | 43,388,068 | 200,584,766 | 126,813,759 | 97,952,035 | 36,945,771 | 255,080,070 |

## Comparable sums (strong only)

| Metric | Scope | Amount € |
|--------|-------|---------:|
| Exp uit sum | all 5 | 1,110,597,112 |
| Cash-out sum | all 5 | 1,499,003,428 |
| Opcentiemen sum | ANT+OVL+LIM+VBR | 500,421,882 |
| Inv 2026 sum | all 5 | 342,728,179 |
| Inv period sum | OVL+LIM+VBR+WVL | 1,290,558,167 |
| Debt 2026-class sum | all 5 (WVL=start) | 293,580,225 |

## Rankings (where comparable)

- **Cash-out 2026:** Oost-VL (€380m) > Limburg (€360m) > West-VL (€284m) > Antwerpen (€274m) > Vlaams-Brabant (€201m)
- **Exp 2026:** Oost-VL (€313m) > Limburg (€247m) > Antwerpen (€205m) > West-VL (€194m) > Vlaams-Brabant (€151m)
- **Inv 2026:** Limburg (€106m) > West-VL (€70m) > Oost-VL (€63m) > Antwerpen (€60m) > Vlaams-Brabant (€43m)
- **Inv period 2026-31:** Oost-VL (€400m) > West-VL (€364m) > Limburg (€272m) > Vlaams-Brabant (€255m)
- **Opcentiemen 2026:** Antwerpen (€172m) > VBR (€127m) > Oost-VL (€111m) > Limburg (€91m)
- **Debt stock:** Limburg (€127m) > West-VL start (€92m) > VBR (€37m) > Antwerpen (€20m) > Oost-VL EOY (€17m)

## Oost-Vlaanderen documentatie detail (2026)

| Line | Amount € |
|------|---------:|
| Exploitatie-ontvangsten | 327,535,846 |
| of which fiscale | 181,554,643 |
| of which subsidies in | 117,036,492 |
| Exploitatie-uitgaven | 313,167,169 |
| of which personeel | 211,963,313 |
| of which goederen/diensten | 63,828,447 |
| of which subsidies granted | 30,667,884 |
| Exploitatiesaldo | 14,368,677 |
| Investeringsuitgaven | 62,639,681 |
| Financieringsuitgaven | 4,048,851 |
| **Cash-out** | **379,855,701** |
| BBR | 24,848,155 |
| AFM | 11,072,221 |

Press cross-check (secondary): VRT opposition ~€330m uitgaven/yr class — near exp €313m; invest period ~€400m aligns.

## Sources

src_antwerpen_prov_mjp_2026; src_westvl_prov_mjp_2026; src_oostvl_prov_mjp_beleidsverklaring_2026; src_oostvl_prov_mjp_documentatie_2026; src_limburg_prov_amjp_jun2026; src_vbr_prov_mjp_2026; src_ovl_mjp_press_vrt.

Parallel Walloon snapshot: `walloon_provinces_2026_snapshot.md` (rq_076).
"""
(root / "flemish_provinces_2026_snapshot.md").write_text(snap, encoding="utf-8")
print("snapshot ok")

# loop log
log = Path("docs/doge/loop_log.md")
entry = """
### 2026-07-22T13:49:00Z — tick 86
- Unit: rq_085 (Oost-Vlaanderen full exploitatie 2026 from documentatie T2)
- Found (strong, official Documentatie PDF p37/p41/p44 Totalen budget 2026): **Exploitatie-uitgaven EUR 313,167,169** / ontvangsten **EUR 327,535,846** (saldo **EUR 14,368,677**). Breakdown uit: personeel **EUR 211,963,313**; goederen/diensten **EUR 63,828,447**; subsidies granted **EUR 30,667,884**; financiele **EUR 921,577**. Inv uit **EUR 62,639,681** / fin uit **EUR 4,048,851**. **Cash-out EUR 379,855,701**. Completes **5/5 Flemish provinces** full exp+cashout. Compare: exp sum **EUR 1,110,597,112**; cash-out sum **EUR 1,499,003,428**. Rank cash-out: OVL 380 > LIM 360 > WVL 284 > ANT 274 > VBR 201. VRT secondary ~330m/yr class near exp. OVL largest because onderwijs pass-through in personnel.
- Wrote: 10 budgets; cmt_ovl + cmt_vl_provinces; snapshot; 2 sources; entity; rq_085=done; seeded rq_086 WVL opcent; ticks=86
- FOI: none (documentatie public on beleidsportaal)
- Next: **rq_086** WVL opcentiemen (prio 2) or **rq_084** SWA recheck (prio 2)

"""
lt = log.read_text(encoding="utf-8")
if "tick 86" not in lt:
    log.write_text(lt.rstrip() + "\n" + entry, encoding="utf-8")
    print("log ok")
else:
    print("log exists")

from pathlib import Path

root = Path("docs/doge/data")

# budgets
bud = root / "budgets.csv"
t = bud.read_text(encoding="utf-8")
if not t.endswith("\n"):
    t += "\n"
if "bud_wvl_prov_opcentiemen_2026" not in t:
    t += """bud_wvl_prov_opcentiemen_2026,prov_west_vlaanderen,2026,128769361,,,budgeted,src_westvl_prov_mjp_2026,strong,Schema T2 p31 Opcentiemen OV 2026 EUR 128769361; rate 186.22; VLABEL 13/09/2025
bud_wvl_prov_opcentiemen_2031,prov_west_vlaanderen,2031,150110481,,,budgeted,src_westvl_prov_mjp_2026,strong,Schema T2 p31 Opcentiemen OV 2031 EUR 150110481
bud_wvl_prov_eigen_belastingen_2026,prov_west_vlaanderen,2026,57843000,,,budgeted,src_westvl_prov_mjp_2026,strong,Schema T2 p31 Andere belastingen (eigen) 2026 EUR 57843000
bud_wvl_prov_fiscal_total_2026,prov_west_vlaanderen,2026,186612461,,,budgeted,src_westvl_prov_mjp_2026,strong,Opcent 128769361 + eigen 57843000 + boetes 100 = 186612461 (T2 p30/31)
bud_vl_provinces_opcent_sum5_2026,sec_flanders,2026,629191243,,,budgeted,src_doge_flemish_prov_compare_2026,strong,Sum opcentiemen all 5 Flemish provinces 2026 after rq_086
"""
    bud.write_text(t, encoding="utf-8")
    print("budgets ok")
else:
    print("budgets exist")

# commitments WVL
cmt = root / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
old = '""opcentiemen_rate"":186.22'
new = '""opcentiemen_2026"":128769361,""opcentiemen_2031"":150110481,""eigen_belastingen_2026"":57843000,""fiscal_total_2026"":186612461,""opcentiemen_rate"":186.22'
if old in ct and "opcentiemen_2026" not in ct:
    ct = ct.replace(old, new, 1)
    # also update note on cmt_wvl if still says chart not digitised
    ct = ct.replace(
        "Schema M2 p15 exp 194.4m/216.6m strong tick85; invest+debt+AFM strong; subsidies class medium",
        "Schema M2+T2: exp 194.4m; opcent 128.8m rate 186.22; eigen tax 57.8m; invest+debt+AFM strong; subsidies class medium",
    )
    cmt.write_text(ct, encoding="utf-8")
    print("cmt_wvl ok")
else:
    print("cmt_wvl skip", "opcentiemen_2026" in ct)

# vl provinces commitment opcent
ct = cmt.read_text(encoding="utf-8")
if "opcent_sum_5" not in ct:
    ct = ct.replace(
        '"opcent_sum_4":500421882',
        '"opcent_sum_5":629191243,"opcent_sum_4":500421882,"wvl_opcent":128769361',
    )
    ct = ct.replace(
        "WVL opcentiemen digitise; ANT 6y invest sum",
        "ANT 6y invest sum; WVL opcent filled tick87",
    )
    cmt.write_text(ct, encoding="utf-8")
    print("cmt_vl ok")
else:
    print("cmt_vl skip")

# entities
ent = root / "entities.csv"
et = ent.read_text(encoding="utf-8")
old_e = "MJP 2026-2031; exp uit 194.4m ont 216.6m cashout 283.9m 2026 M2; invest 363.5m/6y; debt start 92.3m"
new_e = "MJP 2026-2031; exp 194.4m cashout 283.9m; opcent 128.8m rate 186.22; invest 363.5m/6y; debt start 92.3m"
if old_e in et:
    ent.write_text(et.replace(old_e, new_e), encoding="utf-8")
    print("entity ok")
else:
    print("entity not matched")

# sources note
src = root / "sources.csv"
st = src.read_text(encoding="utf-8")
st = st.replace(
    "Schema M2 p15 vision-read tick85: exp 194.4m/216.6m inv 70.1m fin 19.4m; BBR/AFM match; raw westvl_prov_mjp_2026_2031.pdf",
    "Schema M2 p15 + T2 p30-31 tick85/87: exp 194.4m/216.6m; opcent 128.8m; eigen tax 57.8m; inv 70.1m; BBR/AFM match; raw westvl_prov_mjp_2026_2031.pdf",
)
st = st.replace(
    "Sums from ticks 78-86; WVL+OVL exp filled; all 5 VL provinces exp+cashout; not a government publication",
    "Sums from ticks 78-87; all 5 VL provinces exp+cashout+opcent; not a government publication",
)
src.write_text(st, encoding="utf-8")
print("sources ok")

# research queue
rq = root / "research_queue.csv"
rt = rq.read_text(encoding="utf-8")
rt = rt.replace(
    'rq_086,West-Vlaanderen opcentiemen 2026 digitise from MJP chart,continuous,2,open,L1,prov_west_vlaanderen,"Digitise WVL opcentiemen EUR 2026 from MJP chart/text to complete 5-prov opcent sum; no invent euros.",,2026-07-22T13:49:00Z,2026-07-22T13:49:00Z,"Rate 186.22 known; EUR chart not digitised tick79/85"',
    'rq_086,West-Vlaanderen opcentiemen 2026 digitise from MJP chart,continuous,2,done,L1,prov_west_vlaanderen,"Digitise WVL opcentiemen EUR 2026 from MJP chart/text to complete 5-prov opcent sum; no invent euros.",,2026-07-22T13:49:00Z,2026-07-22T14:04:00Z,"T2 p31: opcent 128769361 rate 186.22; eigen 57843000; fiscal sum 186612461; path to 150.1m 2031"',
)
if "rq_087," not in rt:
    if not rt.endswith("\n"):
        rt += "\n"
    rt += 'rq_087,Flemish 5 provinces refresh snapshot with WVL opcent,continuous,2,open,L1,sec_flanders,"Optional light refresh of flemish_provinces_2026_snapshot after rq_086 opcent fill; or skip if already updated in tick87.",,2026-07-22T14:04:00Z,2026-07-22T14:04:00Z,"May be done inside tick87"\n'
rq.write_text(rt, encoding="utf-8")
print("queue ok")

# mark rq_087 done if we update snapshot here
rt = rq.read_text(encoding="utf-8")
rt = rt.replace(
    'rq_087,Flemish 5 provinces refresh snapshot with WVL opcent,continuous,2,open,L1,sec_flanders,"Optional light refresh of flemish_provinces_2026_snapshot after rq_086 opcent fill; or skip if already updated in tick87.",,2026-07-22T14:04:00Z,2026-07-22T14:04:00Z,"May be done inside tick87"',
    'rq_087,Flemish 5 provinces refresh snapshot with WVL opcent,continuous,2,done,L1,sec_flanders,"Optional light refresh of flemish_provinces_2026_snapshot after rq_086 opcent fill; or skip if already updated in tick87.",,2026-07-22T14:04:00Z,2026-07-22T14:04:00Z,"Updated inside tick87 with WVL opcent 128.8m; 5-prov opcent sum 629.2m"',
)
rq.write_text(rt, encoding="utf-8")

# loop state
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    'main,continuous,continuous,2026-07-22T14:04:00Z,rq_086,87,no,"WVL opcent 128.8m (tick87). Next: rq_084 SWA recheck or new L5 unit."\n',
    encoding="utf-8",
)
print("state ok")

# snapshot refresh
snap = """# Flemish provinces budget 2026 — comparative snapshot

Synthesis from DOGE ticks 78–87 primary rows. **No invented euros.**

## Caveats

- **Accounting:** Flemish BBC (exploitatie/investering/financiering), not Walloon ordinaire/extraordinaire.
- **West-Vlaanderen:** Schema M2 + T2 strong (ticks 85–87); werkingssubsidies ~€55m still **medium**.
- **Oost-Vlaanderen:** Documentatie Totalen budget 2026 strong (tick 86); personnel includes large VL-gesubsidieerd onderwijs pass-through.
- **Personnel:** OVL and Limburg include large VL-gesubsidieerd onderwijs pass-through; Antwerp/VBR smaller onderwijs share.
- **Cash-out** = exp + invest + financing uitgaven (all 5 provinces complete).
- **Opcentiemen** all 5 complete after tick 87.

## Table (2026 unless noted)

| Province | Exp uit € | Inv 2026 € | Cash-out € | Opcentiemen € | Personeel € | Debt € | Inv period 2026-31 € |
|----------|----------:|-----------:|-----------:|--------------:|------------:|-------:|---------------------:|
| Oost-Vlaanderen | 313,167,169 | 62,639,681 | 379,855,701 | 110,542,196 | 211,963,313 | 17,380,658 | 399,702,621 |
| Limburg | 247,304,270 | 106,147,542 | 360,281,175 | 90,933,687 | 173,828,351 | 127,017,316 | 272,275,476 |
| West-Vlaanderen | 194,441,409 | 70,132,288 | 283,945,511 | 128,769,361 | n/a | 92,341,480 start | 363,500,000 |
| Antwerpen | 204,700,675 | 60,420,600 | 274,336,275 | 172,132,240 | 92,014,823 | 19,895,000 | n/a in CSV |
| Vlaams-Brabant | 150,983,589 | 43,388,068 | 200,584,766 | 126,813,759 | 97,952,035 | 36,945,771 | 255,080,070 |

## Comparable sums (strong only)

| Metric | Scope | Amount € |
|--------|-------|---------:|
| Exp uit sum | all 5 | 1,110,597,112 |
| Cash-out sum | all 5 | 1,499,003,428 |
| Opcentiemen sum | all 5 | 629,191,243 |
| Inv 2026 sum | all 5 | 342,728,179 |
| Inv period sum | OVL+LIM+VBR+WVL | 1,290,558,167 |
| Debt 2026-class sum | all 5 (WVL=start) | 293,580,225 |

## Rankings (where comparable)

- **Cash-out 2026:** Oost-VL (€380m) > Limburg (€360m) > West-VL (€284m) > Antwerpen (€274m) > Vlaams-Brabant (€201m)
- **Exp 2026:** Oost-VL (€313m) > Limburg (€247m) > Antwerpen (€205m) > West-VL (€194m) > Vlaams-Brabant (€151m)
- **Opcentiemen 2026:** Antwerpen (€172m) > West-VL (€129m) > VBR (€127m) > Oost-VL (€111m) > Limburg (€91m)
- **Inv 2026:** Limburg (€106m) > West-VL (€70m) > Oost-VL (€63m) > Antwerpen (€60m) > Vlaams-Brabant (€43m)
- **Inv period 2026-31:** Oost-VL (€400m) > West-VL (€364m) > Limburg (€272m) > Vlaams-Brabant (€255m)
- **Debt stock:** Limburg (€127m) > West-VL start (€92m) > VBR (€37m) > Antwerpen (€20m) > Oost-VL EOY (€17m)

## West-Vlaanderen tax detail (T2 p31, 2026)

| Line | Amount € |
|------|---------:|
| Opcentiemen OV (rate 186.22) | 128,769,361 |
| Andere/eigen belastingen | 57,843,000 |
| Boetes | 100 |
| **Fiscal total** | **186,612,461** |
| Opcent path 2031 | 150,110,481 |

## Sources

src_antwerpen_prov_mjp_2026; src_westvl_prov_mjp_2026; src_oostvl_prov_mjp_beleidsverklaring_2026; src_oostvl_prov_mjp_documentatie_2026; src_limburg_prov_amjp_jun2026; src_vbr_prov_mjp_2026.

Parallel Walloon snapshot: `walloon_provinces_2026_snapshot.md` (rq_076).
"""
(root / "flemish_provinces_2026_snapshot.md").write_text(snap, encoding="utf-8")
print("snapshot ok")

# log append bytes-safe
log = Path("docs/doge/loop_log.md")
entry = b"""
### 2026-07-22T14:04:00Z -- tick 87
- Unit: rq_086 (West-Vlaanderen opcentiemen 2026 from Schema T2)
- Found (strong, official Schema T2 p30-31 vision-read): **Opcentiemen OV 2026 EUR 128,769,361** (aanslagvoet **186,22**; VLABEL 13/09/2025). Path to **EUR 150,110,481** in 2031. **Andere/eigen belastingen EUR 57,843,000**. Fiscal sum (opcent+eigen+boetes 100) **EUR 186,612,461**. Completes **5/5 Flemish opcentiemen**. Opcent sum 5-prov **EUR 629,191,243**. Rank opcent: ANT 172 > WVL 129 > VBR 127 > OVL 111 > LIM 91. Chart p118 aligns ~129m->150m class.
- Wrote: 5 budgets; cmt_wvl + cmt_vl; snapshot; sources; entity; rq_086=done; rq_087 snapshot refresh=done; ticks=87
- FOI: none
- Next: **rq_084** SWA recheck (prio 2) or seed new L5/continuous unit

"""
raw = log.read_bytes()
if b"tick 87" not in raw:
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + entry)
    print("log ok")
else:
    print("log exists")

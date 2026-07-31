from pathlib import Path

root = Path("docs/doge/data")

# budgets
bud = root / "budgets.csv"
t = bud.read_text(encoding="utf-8")
if not t.endswith("\n"):
    t += "\n"
if "bud_wvl_prov_bezoldigingen_2026" not in t:
    t += """bud_wvl_prov_bezoldigingen_2026,prov_west_vlaanderen,2026,84874186,,,budgeted,src_westvl_prov_mjp_2026,strong,Schema T2 p30 Bezoldigingen 2026 EUR 84874185.90 (personnel package incl pensioenen net)
bud_wvl_prov_pers_politiek_2026,prov_west_vlaanderen,2026,1198481,,,budgeted,src_westvl_prov_mjp_2026,strong,T2 p30 politiek personeel 2026 EUR 1198480.90
bud_wvl_prov_pers_vast_admin_2026,prov_west_vlaanderen,2026,31628427,,,budgeted,src_westvl_prov_mjp_2026,strong,T2 p30 vastbenoemd niet-onderwijzend 2026 EUR 31628427
bud_wvl_prov_pers_contract_admin_2026,prov_west_vlaanderen,2026,41794498,,,budgeted,src_westvl_prov_mjp_2026,strong,T2 p30 niet-vastbenoemd niet-onderwijzend 2026 EUR 41794497.58
bud_wvl_prov_pers_onderwijs_andere_2026,prov_west_vlaanderen,2026,10614542,,,budgeted,src_westvl_prov_mjp_2026,strong,T2 p30 onderwijzend ten laste andere overheden 2026 EUR 10614542.10
bud_wvl_prov_pers_andere_2026,prov_west_vlaanderen,2026,2374326,,,budgeted,src_westvl_prov_mjp_2026,strong,T2 p30 andere personeelskosten 2026 EUR 2374326.22
bud_wvl_prov_pensioenen_net_2026,prov_west_vlaanderen,2026,-2676129,,,budgeted,src_westvl_prov_mjp_2026,strong,T2 p30 pensioenen net line 2026 EUR -2676128.50 (credit within bezoldigingen)
bud_wvl_prov_goederen_2026,prov_west_vlaanderen,2026,51954729,,,budgeted,src_westvl_prov_mjp_2026,strong,T2 p30 goederen en diensten 2026 EUR 51954728.92
bud_wvl_prov_werkingssubsidies_2026,prov_west_vlaanderen,2026,54431043,,,budgeted,src_westvl_prov_mjp_2026,strong,T2 p30 toegestane werkingssubsidies 2026 EUR 54431042.70 (upgrades prior ~55m class)
bud_wvl_prov_subs_apb_2026,prov_west_vlaanderen,2026,11631181,,,budgeted,src_westvl_prov_mjp_2026,strong,T2 p30 werkingssubsidies aan eigen APB 2026 EUR 11631180.88
bud_wvl_prov_subs_andere_2026,prov_west_vlaanderen,2026,40732307,,,budgeted,src_westvl_prov_mjp_2026,strong,T2 p30 werkingssubsidies aan andere begunstigden 2026 EUR 40732307.02
bud_wvl_prov_fin_rente_2026,prov_west_vlaanderen,2026,1921373,,,budgeted,src_westvl_prov_mjp_2026,strong,T2 p30 rente aan financiele instellingen 2026 EUR 1921373
"""
    # also fix old medium class row note if present - leave historical medium row
    bud.write_text(t, encoding="utf-8")
    print("budgets ok")
else:
    print("budgets exist")

# update old medium werkingssubsidies class row notes if exists
t = bud.read_text(encoding="utf-8")
t2 = t.replace(
    "bud_wvl_prov_werkingssubsidies_class_2026,prov_west_vlaanderen,2026,55000000,,,budgeted,src_westvl_prov_mjp_2026,medium,Werkingssubsidies class ~EUR 55m/yr ~quarter of exploitatie-uitgaven (T2 table image-only)",
    "bud_wvl_prov_werkingssubsidies_class_2026,prov_west_vlaanderen,2026,55000000,,,budgeted,src_westvl_prov_mjp_2026,medium,Superseded by exact T2 54431043 tick89; keep as prior class estimate",
)
if t2 != t:
    bud.write_text(t2, encoding="utf-8")
    print("class row noted")

# commitments
cmt = root / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
lines = ct.splitlines()
out = []
for line in lines:
    if line.startswith("cmt_wvl_prov_budget_2026") and "bezoldigingen_2026" not in line:
        line = line.replace(
            '""fiscal_total_2026"":186612461',
            '""bezoldigingen_2026"":84874186,""werkingssubsidies_2026"":54431043,""subs_apb_2026"":11631181,""subs_andere_2026"":40732307,""goederen_2026"":51954729,""fiscal_total_2026"":186612461',
        )
        line = line.replace(
            "Schema M2+T2: exp 194.4m; opcent 128.8m rate 186.22; eigen tax 57.8m; invest+debt+AFM strong; subsidies class medium",
            "Schema M2+T2: exp 194.4m; bezold 84.9m; werkingssubsidies 54.4m strong; opcent 128.8m; invest+debt+AFM strong",
        )
        print("cmt_wvl fixed")
    if line.startswith("cmt_wvl_prov_werkingssubsidies_2026"):
        # upgrade amount and confidence
        parts = line.split(",", 8)
        # safer string replace
        line = line.replace(",55000000,", ",54431043,", 1)
        line = line.replace(
            '""class_total"":55000000,""agencies_class"":35000000,""wfiv_base"":400000,""exp_uit_2026"":194441409}',
            '""total"":54431043,""apb"":11631181,""andere_begunstigden"":40732307,""agencies_class"":35000000,""wfiv_base"":400000,""exp_uit_2026"":194441409}',
        )
        line = line.replace(",medium,Province_West_Vlaanderen>Subsidies>werking,~55m class ~28pct of exp 194.4m; agencies ~35m; WFIV base 400k strong",
                            ",strong,Province_West_Vlaanderen>Subsidies>werking,T2 exact 54.43m ~28pct exp; APB 11.6m; andere 40.7m; agencies class ~35m narrative")
        # also confidence field earlier in line
        if ",medium,Province_West_Vlaanderen>Subsidies" not in line and "T2 exact" not in line:
            line = line.replace(",medium,", ",strong,", 1) if line.count(",medium,") else line
        print("cmt_subs fixed")
    out.append(line)
cmt.write_text("\n".join(out) + ("\n" if ct.endswith("\n") else ""), encoding="utf-8")

# leaderboard werkingssubsidies upgrade
lb = root / "leaderboard.csv"
lt = lb.read_text(encoding="utf-8")
lt2 = lt.replace(
    "lb_wvl_prov_werkingssubsidies,Provincie West-Vlaanderen operating subsidies class 2026,Flanders,subsidy,Province_West_Vlaanderen>werkingssubsidies,55000000,55000000,Class ~55m/yr; agencies ~35m (POM Inagro Westtoer),medium,src_westvl_prov_mjp_2026,Agencies and partners,Provincial grants,APB-like agencies + third parties; T2 image-only,4,7.5,4,5.5,Open name-level register; OCR full T2,seed,,tick79",
    "lb_wvl_prov_werkingssubsidies,Provincie West-Vlaanderen operating subsidies 2026,Flanders,subsidy,Province_West_Vlaanderen>werkingssubsidies,54431043,54431043,T2 exact 54.43m; APB 11.6m + andere 40.7m; agencies class ~35m narrative,strong,src_westvl_prov_mjp_2026,Agencies and partners,Provincial grants,APB + third parties; name-level still opaque,4,8,4,5.6,Open name-level register,seed,,tick89",
)
if lt2 != lt:
    lb.write_text(lt2, encoding="utf-8")
    print("lb ok")
else:
    print("lb no exact match - try partial")
    if "lb_wvl_prov_werkingssubsidies" in lt and "54431043" not in lt:
        lt3 = lt.replace("Class ~55m/yr; agencies ~35m (POM Inagro Westtoer),medium", "T2 exact 54.43m; APB 11.6m + andere 40.7m,strong")
        lt3 = lt3.replace(",55000000,55000000,", ",54431043,54431043,", 1)
        lb.write_text(lt3, encoding="utf-8")
        print("lb partial")

# entities
ent = root / "entities.csv"
et = ent.read_text(encoding="utf-8")
old = "MJP 2026-2031; exp 194.4m cashout 283.9m; opcent 128.8m rate 186.22; invest 363.5m/6y; debt start 92.3m"
new = "MJP 2026-2031; exp 194.4m cashout 283.9m; bezold 84.9m; werkingssubsidies 54.4m; opcent 128.8m; invest 363.5m/6y"
if old in et:
    ent.write_text(et.replace(old, new), encoding="utf-8")
    print("entity ok")
else:
    print("entity skip")

# sources
src = root / "sources.csv"
st = src.read_text(encoding="utf-8")
st = st.replace(
    "Schema M2 p15 + T2 p30-31 tick85/87: exp 194.4m/216.6m; opcent 128.8m; eigen tax 57.8m; inv 70.1m; BBR/AFM match; raw westvl_prov_mjp_2026_2031.pdf",
    "Schema M2 p15 + T2 p30-31 tick85/87/89: exp 194.4m; bezold 84.9m; werkingssubsidies 54.4m; opcent 128.8m; inv 70.1m; raw westvl_prov_mjp_2026_2031.pdf",
)
src.write_text(st, encoding="utf-8")
print("sources ok")

# research queue
rq = root / "research_queue.csv"
rt = rq.read_text(encoding="utf-8")
rt = rt.replace(
    'rq_088,West-Vlaanderen bezoldigingen/personeel 2026 from T2,continuous,3,open,L1,prov_west_vlaanderen,"Extract WVL bezoldigingen and key exp rubrics 2026 from Schema T2 p30 (parallel OVL personnel); no invent euros.",,2026-07-22T14:19:00Z,2026-07-22T14:19:00Z,"T2 p30 image has bezoldigingen line; tick87 saw table"',
    'rq_088,West-Vlaanderen bezoldigingen/personeel 2026 from T2,continuous,3,done,L1,prov_west_vlaanderen,"Extract WVL bezoldigingen and key exp rubrics 2026 from Schema T2 p30 (parallel OVL personnel); no invent euros.",,2026-07-22T14:19:00Z,2026-07-22T14:34:00Z,"Bezold 84874186; goederen 51954729; werkingssubsidies 54431043 strong (APB 11.6m + andere 40.7m); onderwijs andere 10.6m"',
)
if "rq_090," not in rt:
    if not rt.endswith("\n"):
        rt += "\n"
    rt += 'rq_090,WVL or OVL named L5 werkingssubsidies sample,continuous,3,open,L5,prov_west_vlaanderen,"Extract 3+ named third-party/agency subsidies with EUR from MJP documentatie or T2 detail if public; else FOI.",,2026-07-22T14:34:00Z,2026-07-22T14:34:00Z,"Aggregate werkingssubsidies now strong WVL 54.4m; name-level still thin"\n'
rq.write_text(rt, encoding="utf-8")
print("queue ok")

# loop state
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    'main,continuous,continuous,2026-07-22T14:34:00Z,rq_088,89,no,"WVL bezold 84.9m; werkingssubsidies 54.4m strong (tick89). Next: rq_090 L5 sample or rq_089 SWA low."\n',
    encoding="utf-8",
)
print("state ok")

# snapshot note for WVL personnel
snap = root / "flemish_provinces_2026_snapshot.md"
st = snap.read_text(encoding="utf-8")
st = st.replace(
    "| West-Vlaanderen | 194,441,409 | 70,132,288 | 283,945,511 | 128,769,361 | n/a | 92,341,480 start | 363,500,000 |",
    "| West-Vlaanderen | 194,441,409 | 70,132,288 | 283,945,511 | 128,769,361 | 84,874,186 | 92,341,480 start | 363,500,000 |",
)
st = st.replace(
    "- **West-Vlaanderen:** Schema M2 + T2 strong (ticks 85–87); werkingssubsidies ~€55m still **medium**.",
    "- **West-Vlaanderen:** Schema M2 + T2 strong (ticks 85–89); bezoldigingen €84.9m; werkingssubsidies **€54.4m strong**.",
)
if "WVL bezoldigingen" not in st:
    st = st.replace(
        "## West-Vlaanderen tax detail (T2 p31, 2026)",
        "## West-Vlaanderen exp rubrics (T2 p30, 2026)\n\n| Line | Amount € |\n|------|---------:|\n| Bezoldigingen (personnel package) | 84,874,186 |\n| of which vastbenoemd admin | 31,628,427 |\n| of which contract admin | 41,794,498 |\n| of which onderwijs andere overheden | 10,614,542 |\n| Goederen en diensten | 51,954,729 |\n| Toegestane werkingssubsidies | 54,431,043 |\n| of which APB | 11,631,181 |\n| of which andere begunstigden | 40,732,307 |\n\n## West-Vlaanderen tax detail (T2 p31, 2026)",
    )
snap.write_text(st, encoding="utf-8")
print("snapshot ok")

# log
log = Path("docs/doge/loop_log.md")
entry = """
### 2026-07-22T14:34:00Z -- tick 89
- Unit: rq_088 (West-Vlaanderen bezoldigingen/personeel + exp rubrics T2 p30)
- Found (strong, official Schema T2 p30): **Bezoldigingen EUR 84,874,186** (politiek 1.20m; vast admin 31.63m; contract admin 41.79m; onderwijs andere overheden 10.61m; andere 2.37m; pensioenen net -2.68m). **Goederen en diensten EUR 51,954,729**. **Toegestane werkingssubsidies EUR 54,431,043** (upgrades prior ~55m medium) of which **APB EUR 11,631,181** + **andere begunstigden EUR 40,732,307**. Financiering rente **EUR 1,921,373**. WVL personnel much smaller than OVL 212m (OVL heavy onderwijs pass-through). Werkingssubsidies ~28pct of exp 194.4m.
- Wrote: 12 budgets; cmt_wvl + cmt_subs; leaderboard upgrade; snapshot; entity; sources; rq_088=done; seeded rq_090 L5 sample; ticks=89
- FOI: none (public T2)
- Next: **rq_090** named L5 werkingssubsidies sample (prio 3) or **rq_089** SWA Q4 (prio 1)

""".encode("utf-8")
raw = log.read_bytes()
if b"tick 89" not in raw:
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + entry)
    print("log ok")
else:
    print("log exists")

from pathlib import Path

root = Path("docs/doge/data")
now = "2026-07-22T16:49:00Z"

bud = root / "budgets.csv"
t = bud.read_text(encoding="utf-8")
if not t.endswith("\n"):
    t += "\n"
if "bud_lux_prov_asbl_ge50k_sum_2026" not in t:
    t += """bud_lux_prov_asbl_ge50k_sum_2026,prov_luxembourg,2026,4300000,,,budgeted,src_ccrek_lux_prov_budget_2026,strong,ASBL/FUP aids >=50k/yr total 4.3m 2026 CoA (-0.9m/-17.8pct vs 2025)
bud_lux_prov_asbl_delta_vs_2025,prov_luxembourg,2026,-900000,,,budgeted,src_ccrek_lux_prov_budget_2026,strong,ASBL/FUP package change vs 2025 -0.9m CoA
bud_lux_prov_contrats_gestion_2024,prov_luxembourg,2024,25,,,outturn,src_ccrek_lux_prov_budget_2026,strong,25 management contract evaluation reports 2024 received by CoA
bud_lux_prov_pension_debudget_2026,prov_luxembourg,2026,3100000,,,budgeted,src_ccrek_lux_prov_budget_2026,strong,ONSS pension cotisations shortfall 3.1m covered by Ethias pension fund
bud_lux_prov_gsm_tax_2026,prov_luxembourg,2026,600000,,,budgeted,src_ccrek_lux_prov_budget_2026,strong,Taxe mats pylones GSM 0.6m 2026 with matching provision
bud_lux_prov_zones_secours_2026_confirm,prov_luxembourg,2026,18000000,,,budgeted,src_ccrek_lux_prov_budget_2026,strong,Zones secours 18.0m (16.0m securite civile + 2.0m budget complementaire)
bud_lux_prov_arlon_culture_roof_2026,prov_luxembourg,2026,2800000,,,budgeted,src_ccrek_lux_prov_budget_2026,medium,Maison culture Arlon roof works 2.8m invest contingent on Ville Arlon 2.8m contribution (no justificatory piece CoA)
bud_lux_prov_cours_eau_invest_2026,prov_luxembourg,2026,1300000,,,budgeted,src_ccrek_lux_prov_budget_2026,strong,Invest aménagement entretien cours d eau 1.3m extraordinaire
bud_lux_prov_cancer_vehicle_2026,prov_luxembourg,2026,500000,,,budgeted,src_ccrek_lux_prov_budget_2026,strong,Vehicule depistage mobile cancer AVIQ-financed 0.5m
bud_lux_prov_centres_sante_invest_2026,prov_luxembourg,2026,600000,,,budgeted,src_ccrek_lux_prov_budget_2026,strong,Invest centres de sante acquisition construction amenagement 0.6m
bud_lux_prov_palais_annex_2026,prov_luxembourg,2026,500000,,,budgeted,src_ccrek_lux_prov_budget_2026,strong,Amenagement annexe palais provincial 0.5m
bud_walloon_asbl_totals_known_2026,sec_wallonia,2026,14300000,,,budgeted,src_doge_walloon_prov_l5_2026,strong,Known ASBL package totals BW 10.0m + Lux 4.3m = 14.3m (Hainaut Namur Liege totals unknown)
"""
    # avoid double if bud_lux_prov_asbl_aids already has 4.3m - still add sum row with clearer id
    bud.write_text(t, encoding="utf-8")
    print("budgets ok")
else:
    print("budgets exist")

cmt = root / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
if "cmt_lux_asbl_package_2026" not in ct:
    if not ct.endswith("\n"):
        ct += "\n"
    ct += """cmt_lux_asbl_package_2026,Luxembourg province ASBL/FUP package ge50k 2026,prov_luxembourg,Provincial ASBL and FUP,CoA budget 2026 total,,2026,2026,4300000,"{""total"":4300000,""delta_vs_2025"":-900000,""contrats_gestion_eval_2024"":25,""named_list_public"":false}",0,active,,Extraprovincial subsidy layer,FOI gap_lux_asbl_list_2026 for named EUR,src_ccrek_lux_prov_budget_2026,strong,Province_Lux>ASBL_package,4.3m total -17.8pct; annual eval report only covers entities with management contracts
cmt_lux_invest_named_2026,Luxembourg named invest projects 2026,prov_luxembourg,Water culture health buildings,CoA extraordinaire,,2026,2026,5700000,"{""cours_eau"":1300000,""arlon_culture_roof"":2800000,""cancer_vehicle"":500000,""centres_sante"":600000,""palais_annex"":500000}",0,active,,Provincial capital sample,Arlon roof contingent on city match,src_ccrek_lux_prov_budget_2026,medium,Province_Lux>Invest_named,Arlon 2.8m medium confidence (no justificatory piece)
cmt_lux_pension_debudget_2026,Luxembourg pension cotisations shortfall Ethias 2026,prov_luxembourg,Ethias pension fund,CoA SFP comparison,,2026,2026,3100000,"{""shortfall"":3100000,""budgeted_cotisations"":14902841,""sfp_estimate"":17956500}",0,active,,Pension funding off-budget component,Monitor Ethias reserves,src_ccrek_lux_prov_budget_2026,strong,Province_Lux>Pensions,3.1m gap vs SFP; parallel Namur 10m pattern smaller scale
"""
    cmt.write_text(ct, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments exist")

# update walloon compare commitment totals
ct = cmt.read_text(encoding="utf-8")
if "lux_asbl_total" in ct and "gap_lux" not in ct:
    ct = ct.replace(
        '""lux_asbl_total"":4300000}',
        '""lux_asbl_total"":4300000,""lux_named_list_public"":false,""foi"":""gap_lux_asbl_list_2026""}',
    )
    cmt.write_text(ct, encoding="utf-8")

lb = root / "leaderboard.csv"
lt = lb.read_text(encoding="utf-8")
if "lb_lux_asbl_package" not in lt:
    if not lt.endswith("\n"):
        lt += "\n"
    lt += """lb_lux_asbl_package,Luxembourg ASBL package 4.3m 2026,Wallonia,subsidy,Province_Lux>ASBL,4300000,4300000,4.3m ge50k aids -17.8pct vs 2025; names not in CoA PDF,strong,src_ccrek_lux_prov_budget_2026,Taxpayers,Provincial ASBL layer,Total known; named list FOI ready,5,7.5,4,5.5,Send gap_lux_asbl_list_2026,seed,,tick98
lb_lux_pension_debudget,Luxembourg pension shortfall Ethias 3.1m,Wallonia,ops,Province_Lux>Pensions,3100000,3100000,3.1m ONSS gap covered by Ethias fund,strong,src_ccrek_lux_prov_budget_2026,Staff taxpayers,Off-budget pension path,Smaller than Namur 10m but same mechanism,5,7.5,5,5.8,Publish Ethias reserve path,seed,,tick98
"""
    lb.write_text(lt, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard exist")

# FOI queue
foi = root / "foi_queue.csv"
ft = foi.read_text(encoding="utf-8")
if "gap_lux_asbl_list_2026" not in ft:
    if not ft.endswith("\n"):
        ft += "\n"
    ft += (
        "gap_lux_asbl_list_2026,"
        "Luxembourg>subsidies>ASBL_entities_ge_50k,"
        "prov_luxembourg,"
        "Annex budget 2026 ASBL/FUP aids >=50k with names amounts and evaluation report for 25 management contracts,"
        "CoA gives total 4.3m but no public named EUR list; eval report excludes non-contract entities,"
        "7,"
        "Province de Luxembourg publicite de l administration,"
        ","
        "Province de Luxembourg greffe,"
        "docs/doge/foi/drafts/gap_lux_asbl_list_2026.md,"
        "ready,"
        "2026-07-22,"
        ",,,,,"
        "cmt_lux_asbl_package_2026,"
        "lb_lux_asbl_package,"
        f"{now},{now},"
        "rq_098 draft ready human send only; FR letter\n"
    )
    foi.write_text(ft, encoding="utf-8")
    print("foi ok")
else:
    print("foi exists")

# entities
ent = root / "entities.csv"
et = ent.read_text(encoding="utf-8")
lines = []
for line in et.splitlines():
    if line.startswith("prov_luxembourg,"):
        parts = line.rsplit(",", 1)
        if len(parts) == 2:
            line = parts[0] + ",CoA 2026: ord 134.3m; zones 18.0m; ASBL package 4.3m (-17.8pct); pension shortfall 3.1m Ethias; FOI named list ready"
    lines.append(line)
ent.write_text("\n".join(lines) + ("\n" if et.endswith("\n") else ""), encoding="utf-8")
print("entities ok")

# walloon snapshot
snap = root / "walloon_provinces_2026_snapshot.md"
if snap.exists():
    st = snap.read_text(encoding="utf-8")
    st = st.replace(
        "| Luxembourg | (list class) | **€4,300,000** (prior) | mapped earlier |",
        "| Luxembourg | (count n/a) | **€4,300,000** (−17.8% vs 2025) | partial (contracts only in eval report); FOI ready |",
    )
    if "Completes 5/5 Walloon" not in st:
        st += """

## Completes 5/5 Walloon provinces L5 map (tick 98)

All five Walloon provinces now have either named L5 lines, package totals, and/or FOI for full ASBL lists (Hainaut + Luxembourg FOI ready).
"""
    snap.write_text(st, encoding="utf-8")
    print("snapshot ok")

src = root / "sources.csv"
st = src.read_text(encoding="utf-8")
if "src_ccrek_lux_l5_tick98" not in st:
    if not st.endswith("\n"):
        st += "\n"
    st += 'src_ccrek_lux_l5_tick98,CoA Luxembourg budget 2026 ASBL package and named invest,docs/doge/data/raw/lux_prov_ccrek_budget_2026.pdf,Cour des comptes,2026-07-22,audit,"ASBL 4.3m -17.8pct; 25 contrats gestion; Arlon roof 2.8m contingent; pension 3.1m Ethias"\n'
    st += 'src_tick98_lux_named_list_negative,Tick98 public search Lux ASBL named EUR list negative,docs/doge/data/raw/lux_prov_ccrek_budget_2026.pdf,DOGE loop research,2026-07-22,secondary,"No public named list; FOI gap_lux_asbl_list_2026 ready"\n'
    src.write_text(st, encoding="utf-8")
print("sources ok")

rq = root / "research_queue.csv"
rt = rq.read_text(encoding="utf-8")
rt = rt.replace(
    'rq_098,Luxembourg province ASBL list deepen or FOI,continuous,2,open,L5,prov_luxembourg,"Extract named ASBL from Lux CoA 4.3m list if public; else FOI parallel Hainaut.",,2026-07-22T16:34:00Z,2026-07-22T16:34:00Z,"Lux has 4.3m aggregate; names thin"',
    'rq_098,Luxembourg province ASBL list deepen or FOI,continuous,2,blocked_foi,L5,prov_luxembourg,"Extract named ASBL from Lux CoA 4.3m list if public; else FOI parallel Hainaut.",gap_lux_asbl_list_2026,2026-07-22T16:34:00Z,2026-07-22T16:49:00Z,"Deepened: 4.3m -17.8pct; 25 contrats; invest named; pension 3.1m; FOI ready for named list"',
)
if "rq_099," not in rt:
    if not rt.endswith("\n"):
        rt += "\n"
    rt += 'rq_099,Walloon 5 provinces L5 ASBL compare synthesis,continuous,2,open,L1,sec_wallonia,"Synthesize ASBL entity counts totals opacity FOI status for 5 Walloon provinces; no invent euros.",,2026-07-22T16:49:00Z,2026-07-22T16:49:00Z,"Data ready ticks 95-98"\n'
rq.write_text(rt, encoding="utf-8")
print("queue ok")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    'main,continuous,continuous,2026-07-22T16:49:00Z,rq_098,98,no,"Lux ASBL 4.3m FOI ready (tick98). Next: rq_099 Walloon L5 synthesize or rq_089 SWA; human FOI stack."\n',
    encoding="utf-8",
)
print("state ok")

log = Path("docs/doge/loop_log.md")
entry = """
### 2026-07-22T16:49:00Z -- tick 98
- Unit: rq_098 (Luxembourg province ASBL deepen + FOI)
- Found (strong CoA; **named EUR list still not public**): ASBL/FUP package **EUR 4,300,000** 2026 (**-EUR 0.9m / -17.8%** vs 2025). **25** management-contract evaluation reports 2024. CoA: annual financial/eval annex covers only entities **with** management contracts — others with aids not in that report. Named invest: watercourses **EUR 1,300,000**; Maison culture Arlon roof **EUR 2,800,000** (contingent on Ville Arlon 2.8m match; **no justificatory piece**); cancer screening vehicle AVIQ **EUR 500,000**; health centres **EUR 600,000**; palace annex **EUR 500,000**. Zones secours **EUR 18,000,000**. Pension cotisations shortfall **EUR 3,100,000** to Ethias fund. GSM tax **EUR 600,000** + matching provision. Public search for named list: **negative**. **FOI draft** `gap_lux_asbl_list_2026` **ready** (human send). Completes 5/5 Walloon provinces L5 map (FOI where names missing).
- Wrote: 12 budgets; 3 commitments; 2 leaderboard; FOI draft+queue; snapshot; entities; sources; rq_098=blocked_foi; seeded rq_099 synthesis; ticks=98
- FOI: **gap_lux_asbl_list_2026** ready (not sent); Hainaut FOI still ready
- Next: **rq_099** Walloon L5 ASBL compare synthesis (prio 2) or **rq_089** SWA Q4 (prio 1)

""".encode("utf-8")
raw = log.read_bytes()
if b"tick 98" not in raw:
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + entry)
    print("log ok")
else:
    print("log exists")

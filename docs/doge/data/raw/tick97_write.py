from pathlib import Path

root = Path("docs/doge/data")

bud = root / "budgets.csv"
t = bud.read_text(encoding="utf-8")
if not t.endswith("\n"):
    t += "\n"
if "bud_bw_prov_asbl_ge50k_sum_2026" not in t:
    t += """bud_bw_prov_asbl_ge50k_sum_2026,prov_brabant_wallon,2026,10000000,,,budgeted,src_ccrek_bw_prov_budget_2026,strong,31 entities ASBL/FUP aids >=50k/yr total EUR 10.0m CoA 2026 annex
bud_bw_prov_asbl_entity_count_2026,prov_brabant_wallon,2026,31,,,budgeted,src_ccrek_bw_prov_budget_2026,strong,31 consolidated entities with motivation explicit CoA
bud_bw_prov_contrats_gestion_2024,prov_brabant_wallon,2024,34,,,outturn,src_ccrek_bw_prov_budget_2026,strong,34 management contracts active 2024
bud_bw_prov_aviq_provision_2026,prov_brabant_wallon,2026,1800000,,,budgeted,src_ccrek_bw_prov_budget_2026,strong,Provision Aviq overpayment risk IMP fusion 1.8m triennat 2023-25
bud_bw_prov_helecine_brasserie_2026,prov_brabant_wallon,2026,1300000,,,budgeted,src_ccrek_bw_prov_budget_2026,strong,Invest Chateau Helecine new brewery visitors 1.3m extraordinaire
bud_bw_prov_bassins_orage_2026,prov_brabant_wallon,2026,3100000,,,budgeted,src_ccrek_bw_prov_budget_2026,strong,Invest storm basins land+works 3.1m (Beauvechain Forges 1.6m class)
bud_bw_prov_points_noeuds_2026,prov_brabant_wallon,2026,1200000,,,budgeted,src_ccrek_bw_prov_budget_2026,strong,Invest cycle network points-noeuds 1.2m
bud_bw_prov_ipes_wavre_2026,prov_brabant_wallon,2026,800000,,,budgeted,src_ccrek_bw_prov_budget_2026,strong,Invest IPES Wavre Quai aux Huitres renovation suite 0.8m
bud_bw_prov_transferts_2026,prov_brabant_wallon,2026,27500000,,,budgeted,src_ccrek_bw_prov_budget_2026,strong,Depenses transferts 27.5m 2026 CoA
bud_namur_prov_asbl_entity_count_2026,prov_namur,2026,10,,,budgeted,src_ccrek_namur_prov_budget_2026,strong,10 entities ASBL/FUP aids >=50k/yr CoA annex (vs Hainaut 199 BW 31)
bud_namur_prov_asbl_unmotivated_count_2026,prov_namur,2026,3,,,budgeted,src_ccrek_namur_prov_budget_2026,strong,3 of 10 entities lack explicit subsidisation motivation CoA
bud_namur_prov_contrats_gestion_2024,prov_namur,2024,21,,,outturn,src_ccrek_namur_prov_budget_2026,strong,21 management contracts active 2024
bud_namur_prov_chevetogne_regie_delta_2026,prov_namur,2026,-200000,,,budgeted,src_ccrek_namur_prov_budget_2026,medium,Dotation regie Domaine Valery Cousin Chevetogne -0.2m vs 2025 adjusted (responsabilisation path)
bud_namur_prov_bep_delta_2026,prov_namur,2026,-400000,,,budgeted,src_ccrek_namur_prov_budget_2026,medium,BEP subsidy -0.4m vs 2025 adjusted CoA note
bud_namur_prov_police_academy_fed_2026,prov_namur,2026,1600000,,,budgeted,src_ccrek_namur_prov_budget_2026,strong,Federal functioning subsidy Academie de police 1.6m receipt estimate
bud_namur_prov_pension_debudget_2026,prov_namur,2026,10000000,,,budgeted,src_ccrek_namur_prov_budget_2026,strong,ONSS pension cotisations partially debudgeted 10.0m to pension fund reserves
bud_namur_prov_gsm_tax_provision_2026,prov_namur,2026,1500000,,,budgeted,src_ccrek_namur_prov_budget_2026,strong,Provision GSM mast tax litigation 1.5m
bud_walloon_asbl_entity_counts_compare,sec_wallonia,2026,240,,,budgeted,src_doge_walloon_prov_l5_2026,strong,Entity counts ge50k: Hainaut 199 + BW 31 + Namur 10 = 240 class (Lux 4.3m list separate metric)
"""
    bud.write_text(t, encoding="utf-8")
    print("budgets ok")
else:
    print("budgets exist")

cmt = root / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
if "cmt_bw_asbl_package_2026" not in ct:
    if not ct.endswith("\n"):
        ct += "\n"
    ct += """cmt_bw_asbl_package_2026,Brabant wallon ASBL/FUP package ge50k 2026,prov_brabant_wallon,31 provincial ASBL/FUP entities,CoA budget 2026 annex total,,2026,2026,10000000,"{""entities"":31,""total_eur"":10000000,""contrats_gestion_2024"":34,""motivation"":""explicit""}",0,active,,Extraprovincial subsidy layer,Publish named top20 EUR list,src_ccrek_bw_prov_budget_2026,strong,Province_BW>ASBL_package,10.0m total; motivations explicit unlike Hainaut
cmt_bw_invest_named_2026,Brabant wallon named invest projects 2026,prov_brabant_wallon,Storm basins Helecine cycle IPES,CoA extraordinaire programme,,2026,2026,6400000,"{""bassins_orage"":3100000,""helecine_brasserie"":1300000,""points_noeuds"":1200000,""ipes_wavre"":800000}",0,active,,Provincial capital programme,Open year-by-year delivery,src_ccrek_bw_prov_budget_2026,strong,Province_BW>Invest_named,Named invest sample 6.4m of 13.2m invest
cmt_namur_asbl_opacity_2026,Namur ASBL list small but partial motivation gap,prov_namur,10 entities ge50k,CoA budget 2026,,2026,2026,0,"{""entities"":10,""unmotivated"":3,""contrats_gestion_2024"":21}",0,active,,Smaller extraprovincial layer than Hainaut,Publish 10-entity EUR list,src_ccrek_namur_prov_budget_2026,strong,Province_Namur>ASBL_list,10 entities; 3 lack motivation; EUR amounts not in CoA PDF
cmt_namur_pension_debudget_2026,Namur pension cotisations debudgeting 10m,prov_namur,Provincial pension fund / ONSS,CoA note Ethias path,,2026,2026,10000000,"{""debudget"":10000000,""reserve_eoy_2024"":37500000,""ethias_exhaustion_horizon"":2031}",0,active,,Pension funding gap risk,Update Ethias projection,src_ccrek_namur_prov_budget_2026,strong,Province_Namur>Pensions,10m off-budget vs SFP; reserves path thin
cmt_walloon_asbl_opacity_compare_2026,Walloon provinces ASBL transparency compare 2026,sec_wallonia,Provincial ASBL layers,Synthesis CoA ticks 95-97,,2026,2026,10000000,"{""hainaut_entities"":199,""hainaut_motivation"":""none"",""bw_entities"":31,""bw_total_eur"":10000000,""bw_motivation"":""explicit"",""namur_entities"":10,""namur_unmotivated"":3,""lux_asbl_total"":4300000}",0,active,docs/doge/data/walloon_provinces_2026_snapshot.md,Cross-province ASBL opacity,FOI Hainaut list; publish all annexes,src_doge_walloon_prov_l5_2026,strong,Wallonie>Provinces>ASBL_compare,BW only with total EUR in CoA text; Hainaut worst opacity
"""
    cmt.write_text(ct, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments exist")

lb = root / "leaderboard.csv"
lt = lb.read_text(encoding="utf-8")
if "lb_bw_asbl_package" not in lt:
    if not lt.endswith("\n"):
        lt += "\n"
    lt += """lb_bw_asbl_package,Brabant wallon 31 ASBL package 10m 2026,Wallonia,subsidy,Province_BW>ASBL,10000000,10000000,31 entities ge50k total 10.0m; motivations explicit CoA,strong,src_ccrek_bw_prov_budget_2026,Taxpayers partners,Provincial ASBL layer,Best Walloon CoA transparency on total; names still not public,5,7.5,4,5.5,Publish named top20 EUR,seed,,tick97
lb_namur_pension_debudget,Namur pension debudgeting 10m 2026,Wallonia,ops,Province_Namur>Pensions,10000000,10000000,10m ONSS pension off-budget to fund; Ethias exhaustion ~2031,strong,src_ccrek_namur_prov_budget_2026,Staff taxpayers,Hidden fiscal pressure,Reduces visible spending; depletes reserves,6,8,5,6.3,Update Ethias; stop debudgeting,seed,,tick97
lb_walloon_asbl_opacity_rank,Walloon provinces ASBL opacity ranking 2026,Wallonia,ops,Wallonie>Provinces>ASBL_opacity,0,0,Hainaut 199 unmotivated; Namur 10 (3 unmotivated); BW 31 motivated 10m total; Lux 4.3m list class,strong,src_doge_walloon_prov_l5_2026,All Walloon residents,Extraprovincialisation transparency,Hainaut worst; BW best total; FOI Hainaut ready,7,7.5,6,6.8,Send gap_hainaut_asbl_list_2026; seek BW/Namur annex PDFs,seed,,tick97
"""
    lb.write_text(lt, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard exist")

# sources
src = root / "sources.csv"
st = src.read_text(encoding="utf-8")
if "src_doge_walloon_prov_l5_2026" not in st:
    if not st.endswith("\n"):
        st += "\n"
    st += 'src_doge_walloon_prov_l5_2026,DOGE synthesis Walloon provinces L5 ASBL opacity compare,docs/doge/data/walloon_provinces_2026_snapshot.md,AIpolitics DOGE loop,2026-07-22,secondary,"From CoA Hainaut Liege Namur BW Lux primary notes ticks 95-97; not a government publication"\n'
    # update CoA source notes
    st = st.replace(
        "src_ccrek_namur_prov_budget_2026,",
        "src_ccrek_namur_prov_budget_2026,",
    )
    src.write_text(st, encoding="utf-8")
# enrich namur/bw source notes if present
for old, new in [
    (
        "src_ccrek_namur_prov_budget_2026,",
        None,
    )
]:
    pass
# append note lines by simple replace on known notes fragments
if "10 entities ge50k" not in st:
    st = src.read_text(encoding="utf-8")
    st = st.replace(
        "src_ccrek_namur_prov_budget_2026,",
        "src_ccrek_namur_prov_budget_2026,",
    )
    # find and append to notes field - safer to add new sources only
    if "src_ccrek_namur_l5_tick97" not in st:
        if not st.endswith("\n"):
            st += "\n"
        st += 'src_ccrek_namur_l5_tick97,CoA Namur budget 2026 ASBL list and pension debudget notes,docs/doge/data/raw/namur_prov_ccrek_budget_2026.pdf,Cour des comptes,2026-07-22,audit,"10 entities ge50k; 3 unmotivated; pension debudget 10m; Chevetogne regie path"\n'
        st += 'src_ccrek_bw_l5_tick97,CoA Brabant wallon budget 2026 ASBL package and named invest,docs/doge/data/raw/brabant_wallon_prov_ccrek_budget_2026.pdf,Cour des comptes,2026-07-22,audit,"31 entities 10.0m total; motivations explicit; Helecine 1.3m; storm basins 3.1m"\n'
        src.write_text(st, encoding="utf-8")
print("sources ok")

# entities
ent = root / "entities.csv"
et = ent.read_text(encoding="utf-8")
lines = []
for line in et.splitlines():
    if line.startswith("prov_namur,"):
        parts = line.rsplit(",", 1)
        if len(parts) == 2:
            line = parts[0] + ",CoA 2026: ord 204.2m; zones 30.3m; 10 ASBL ge50k (3 unmotivated); pension debudget 10m"
    if line.startswith("prov_brabant_wallon,"):
        parts = line.rsplit(",", 1)
        if len(parts) == 2:
            line = parts[0] + ",CoA 2026: ord 199.4m; zones 16.1m; ASBL package 10.0m (31 entities motivated); Aviq provision 1.8m"
    lines.append(line)
ent.write_text("\n".join(lines) + ("\n" if et.endswith("\n") else ""), encoding="utf-8")
print("entities ok")

# walloon snapshot append
snap = root / "walloon_provinces_2026_snapshot.md"
if snap.exists():
    st = snap.read_text(encoding="utf-8")
    if "ASBL L5 opacity" not in st:
        st += """

## ASBL / extraprovincial L5 opacity (ticks 95–97)

| Province | Entities ≥€50k | Total EUR in CoA text | Motivation in CoA |
|----------|---------------:|----------------------:|-------------------|
| Hainaut | 199 | n/a (FOI ready) | **None** (CoA flag) |
| Brabant wallon | 31 | **€10,000,000** | **Explicit** |
| Namur | 10 | n/a | 7/10 yes; **3 missing** |
| Luxembourg | (list class) | **€4,300,000** (prior) | mapped earlier |
| Liège | named sample | culture/tourism lines | per-article budget |

**Best public total:** Brabant wallon €10.0m for 31 entities.  
**Worst opacity:** Hainaut 199 entities without CoA-visible motivation or amounts → `gap_hainaut_asbl_list_2026`.
"""
        snap.write_text(st, encoding="utf-8")
        print("snapshot ok")
else:
    print("snapshot missing")

rq = root / "research_queue.csv"
rt = rq.read_text(encoding="utf-8")
rt = rt.replace(
    'rq_097,Namur or Brabant wallon province L5 named sample,continuous,2,open,L5,prov_namur,"Extract 3+ named ASBL/subsidy lines from CoA Namur or BW province budget 2026 if public.",,2026-07-22T16:19:00Z,2026-07-22T16:19:00Z,"Parallel Hainaut/Liege L5; complete Walloon province L5 map"',
    'rq_097,Namur or Brabant wallon province L5 named sample,continuous,2,done,L5,prov_namur,"Extract 3+ named ASBL/subsidy lines from CoA Namur or BW province budget 2026 if public.",,2026-07-22T16:19:00Z,2026-07-22T16:34:00Z,"BW: 31 entities 10.0m total motivated; invest Helecine 1.3m basins 3.1m; Namur: 10 entities 3 unmotivated; pension debudget 10m"',
)
if "rq_098," not in rt:
    if not rt.endswith("\n"):
        rt += "\n"
    rt += 'rq_098,Luxembourg province ASBL list deepen or FOI,continuous,2,open,L5,prov_luxembourg,"Extract named ASBL from Lux CoA 4.3m list if public; else FOI parallel Hainaut.",,2026-07-22T16:34:00Z,2026-07-22T16:34:00Z,"Lux has 4.3m aggregate; names thin"\n'
rq.write_text(rt, encoding="utf-8")
print("queue ok")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    'main,continuous,continuous,2026-07-22T16:34:00Z,rq_097,97,no,"BW ASBL 10.0m/31 entities; Namur pension debudget 10m (tick97). Next: rq_098 Lux or rq_089 SWA."\n',
    encoding="utf-8",
)
print("state ok")

log = Path("docs/doge/loop_log.md")
entry = """
### 2026-07-22T16:34:00Z -- tick 97
- Unit: rq_097 (Namur + Brabant wallon province L5 named/aggregate sample)
- Found (strong, CoA primary): **Brabant wallon:** consolidated ASBL/FUP list **31 entities** with aids >=50k totaling **EUR 10,000,000**; motivations **explicit** (better than Hainaut). **34** management contracts 2024. Named invest: storm basins **EUR 3,100,000**; Helecine brewery **EUR 1,300,000**; points-noeuds **EUR 1,200,000**; IPES Wavre **EUR 800,000**. Aviq overpayment provision **EUR 1,800,000**. Transfers **EUR 27.5m**. **Namur:** only **10 entities** ge50k (3 **without** motivation); **21** management contracts 2024; Chevetogne regie dotation **-0.2m** path; BEP **-0.4m**; police academy federal receipt **EUR 1,600,000**; **pension cotisations debudgeted EUR 10,000,000** to fund (Ethias reserve path toward exhaustion ~2031); GSM tax provision 1.5m. Compare: Hainaut 199 unmotivated > BW 31/10m motivated > Namur 10 partial.
- Wrote: 18 budgets; 5 commitments; 3 leaderboard; walloon snapshot ASBL table; entities; sources; rq_097=done; seeded rq_098 Lux; ticks=97
- FOI: none new (Hainaut FOI already ready)
- Next: **rq_098** Luxembourg ASBL deepen (prio 2) or **rq_089** SWA Q4 (prio 1)

""".encode("utf-8")
raw = log.read_bytes()
if b"tick 97" not in raw:
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + entry)
    print("log ok")
else:
    print("log exists")

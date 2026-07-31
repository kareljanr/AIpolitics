from pathlib import Path

root = Path("docs/doge/data")

bud = root / "budgets.csv"
t = bud.read_text(encoding="utf-8")
if not t.endswith("\n"):
    t += "\n"
if "bud_liege_prov_ftpl_2026" not in t and "bud_liege_prov_tourism_sites_2026" not in t:
    t += """bud_liege_prov_tourism_sites_2026,prov_liege,2026,516011,,,budgeted,src_liege_prov_budget_2026,strong,Subvention sites touristiques paraprovinciaux Blegny-Mine/HFE/DTVL 2026 EUR 516011
bud_liege_prov_parc_hfe_2026,prov_liege,2026,60000,,,budgeted,src_liege_prov_budget_2026,strong,ASBL Parc naturel Hautes Fagnes Eifel projects 2026 EUR 60000
bud_liege_prov_mnema_2026,prov_liege,2026,150000,,,budgeted,src_liege_prov_budget_2026,strong,ASBL MNEMA cite miroir 2026 EUR 150000
bud_liege_prov_service_social_agents_2026,prov_liege,2026,190878,,,budgeted,src_liege_prov_budget_2026,strong,ASBL Service social des agents provinciaux 2026 EUR 190878
bud_liege_prov_gig_2026,prov_liege,2026,110000,,,budgeted,src_liege_prov_budget_2026,strong,ASBL GIG Groupement Informations Geographiques 2026 EUR 110000
bud_liege_prov_dg_dotation_2026,prov_liege,2026,871000,,,budgeted,src_liege_prov_budget_2026,strong,Dotation cooperation Communaute germanophone 2026 EUR 871000
bud_liege_prov_supracommunaux_2026,prov_liege,2026,200000,,,budgeted,src_liege_prov_budget_2026,strong,Subsides supracommunaux 2026 EUR 200000
bud_liege_prov_theatre_liege_2026,prov_liege,2026,60000,,,budgeted,src_liege_prov_budget_2026,strong,ASBL Theatre de Liege 2026 EUR 60000
bud_liege_prov_brf_2026,prov_liege,2026,90000,,,budgeted,src_liege_prov_budget_2026,strong,Subsides BRF cooperation germanophone 2026 EUR 90000
bud_liege_prov_rtc_sport_2026,prov_liege,2026,124000,,,budgeted,src_liege_prov_budget_2026,strong,Partenariat RTC Liege-Huy-Waremme et Televesdre journal sportif 2026 EUR 124000
bud_liege_prov_ftpl_2026_note,prov_liege,2026,1,,,budgeted,src_liege_prov_budget_2026,strong,Federation Tourisme Province Liege line 2026 obligatoire EUR 1 (was 1.2m 2025; major restructure/cut in budget table)
bud_liege_prov_culture_named_sum_2026,prov_liege,2026,280000,,,budgeted,src_liege_prov_budget_2026,strong,Opera 150k + OPL 70k + Theatre Liege 60k = 280000 culture named
bud_hainaut_voies_eau_2026_confirm,prov_hainaut,2026,2300000,,,budgeted,src_ccrek_hainaut_prov_budget_2026,strong,ASBL Voies d eau du Hainaut 2.3m 2026 (incl +1.8m severance tourism stop Canal du Centre)
bud_hainaut_teralis_cut_2026,prov_hainaut,2026,0,,,budgeted,src_ccrek_hainaut_prov_budget_2026,strong,ASBL Teralis financing suppressed 2026 (was 0.4m; French domains sold; liquidation)
bud_hainaut_tournai_cathedral_invest_2026,prov_hainaut,2026,3900000,,,budgeted,src_ccrek_hainaut_prov_budget_2026,strong,Cathédrale Notre-Dame Tournai invest dep 3.9m 2026 (3.7m subsidy received + provincial loan)
bud_hainaut_transfers_hors_zones_2026,prov_hainaut,2026,15500000,,,budgeted,src_ccrek_hainaut_prov_budget_2026,strong,Depenses transferts hors zones secours 15.5m 2026 CoA
bud_hainaut_asbl_list_count_2026,prov_hainaut,2026,199,,,budgeted,src_ccrek_hainaut_prov_budget_2026,strong,199 entities with provincial aids >=50k/yr (CoA; amounts not published in report)
bud_hainaut_contrats_gestion_2024,prov_hainaut,2024,53,,,outturn,src_ccrek_hainaut_prov_budget_2026,strong,53 active management contracts 2024 (52 ASBL + regie Hainaut securite)
"""
    # avoid duplicate voies eau if already there - check
    if "bud_hainaut_prov_voies_eau_2026" in t and "bud_hainaut_voies_eau_2026_confirm" in t:
        pass
    bud.write_text(t, encoding="utf-8")
    print("budgets ok")
else:
    print("budgets exist")

cmt = root / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
if "cmt_liege_prov_tourism_sites_2026" not in ct:
    if not ct.endswith("\n"):
        ct += "\n"
    ct += """cmt_liege_prov_tourism_sites_2026,Liege province paraprovincial tourism sites package,prov_liege,Blegny-Mine Maison Parc HFE DTVL,Budget ordinaire 2026 F569,,2026,2026,516011,"{""2026"":516011}",0,active,,Paraprovincial tourism sites,Publish site-level split,src_liege_prov_budget_2026,strong,Province_Liege>Tourism>sites,516k functioning subvention
cmt_liege_prov_culture_named_2026,Liege province named culture subsidies 2026,prov_liege,Opera ORW OPL Theatre Liege,Budget F789 arts,,2026,2026,280000,"{""opera"":150000,""opl"":70000,""theatre_liege"":60000}",0,active,,Major culture institutions,Outcome KPIs attendance,src_liege_prov_budget_2026,strong,Province_Liege>Culture>named,280k named culture sample
cmt_liege_prov_mnema_2026,MNEMA Cite Miroir provincial subsidy,prov_liege,ASBL MNEMA,Budget administration generale,,2026,2026,150000,"{""2026"":150000}",0,active,,Memory culture site multi-level financed,Co-financed RW FWB Ville,src_liege_prov_budget_2026,strong,Province_Liege>MNEMA,150k province share
cmt_hainaut_voies_eau_2026,ASBL Voies d eau du Hainaut severance package 2026,prov_hainaut,ASBL Voies d eau du Hainaut,CoA budget 2026 note,,2026,2026,2300000,"{""total"":2300000,""severance_delta"":1800000}",0,active,,Canal tourism stop staff costs,One-off heavy severance,src_ccrek_hainaut_prov_budget_2026,strong,Province_Hainaut>Voies_eau,2.3m incl 1.8m preavis after tourism stop
cmt_hainaut_asbl_opacity_2026,Hainaut 199 subsidised entities opacity,prov_hainaut,199 ASBL/intercommunales etc,CoA observation,,2026,2026,0,"{""entities_ge_50k"":199,""contrats_gestion_2024"":53,""motivation_missing"":true}",0,active,,Extraprovincialisation without CoA-visible motivation,Publish named EUR list,src_ccrek_hainaut_prov_budget_2026,strong,Province_Hainaut>ASBL_list,CoA flags unmotivated subsidisation of 199 entities
cmt_hainaut_tournai_cathedral_2026,Tournai cathedral restoration invest 2026,prov_hainaut,Cathédrale Notre-Dame de Tournai,CoA extraordinaire,,2026,2026,3900000,"{""invest_dep"":3900000,""subsidy_receipt"":3700000}",0,active,,Heritage restoration,95pct external subsidy,src_ccrek_hainaut_prov_budget_2026,strong,Province_Hainaut>Tournai_cathedral,3.9m spend / 3.7m subsidy in
"""
    cmt.write_text(ct, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments exist")

lb = root / "leaderboard.csv"
lt = lb.read_text(encoding="utf-8")
if "lb_hainaut_asbl_opacity" not in lt:
    if not lt.endswith("\n"):
        lt += "\n"
    lt += """lb_hainaut_asbl_opacity,Hainaut 199 subsidised entities without CoA motivation,Wallonia,ops,Province_Hainaut>ASBL_extraprovincialisation,0,0,199 entities >=50k/yr aids; CoA says no motivation for extraprovincialisation,strong,src_ccrek_hainaut_prov_budget_2026,Taxpayers,Subsidy middle layer,Opacity of named EUR and justification,8,7,6,7.0,Publish full named EUR list + justifications,seed,,tick95
lb_hainaut_voies_eau,Voies d eau Hainaut 2.3m severance 2026,Wallonia,ops,Province_Hainaut>Voies_eau,2300000,2300000,2.3m incl 1.8m staff preavis after canal tourism stop,strong,src_ccrek_hainaut_prov_budget_2026,Staff taxpayers,Tourism exit cost,One-off cost of stopping activity,4,7.5,5,5.5,Disclose full social plan cost path,seed,,tick95
lb_liege_tourism_sites,Liege paraprovincial tourism sites 516k,Wallonia,subsidy,Province_Liege>Tourism>sites,516011,516011,Blegny-Mine/HFE/DTVL functioning 516k; FTPL line cut to 1 EUR 2026,strong,src_liege_prov_budget_2026,Visitors,Tourism governance restructure,FTPL 1.2m to 1 EUR is major cut,4,7.5,4,5.3,Explain FTPL restructure vs sites package,seed,,tick95
lb_liege_culture_named,Liege Opera OPL Theatre named 280k,Wallonia,subsidy,Province_Liege>Culture,280000,280000,Opera 150k OPL 70k Theatre 60k named sample,strong,src_liege_prov_budget_2026,Culture audiences,High-culture subsidies,Small vs education share of province,3,6.5,3,4.3,Open full culture L5 register,seed,,tick95
"""
    lb.write_text(lt, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard exist")

ent = root / "entities.csv"
et = ent.read_text(encoding="utf-8")
lines = []
for line in et.splitlines():
    if line.startswith("prov_hainaut,"):
        parts = line.rsplit(",", 1)
        if len(parts) == 2:
            line = parts[0] + ",CoA 2026: ord 830.6m; zones 78.2m; Voies d eau 2.3m; Tournai cathedral 3.9m; 199 entities >=50k opacity"
    if line.startswith("prov_liege,"):
        parts = line.rsplit(",", 1)
        if len(parts) == 2:
            line = parts[0] + ",Budget 2026: ord 563.6m; tourism sites 516k; Opera 150k OPL 70k; MNEMA 150k; FTPL line cut to 1 EUR"
    lines.append(line)
ent.write_text("\n".join(lines) + ("\n" if et.endswith("\n") else ""), encoding="utf-8")
print("entities ok")

src = root / "sources.csv"
st = src.read_text(encoding="utf-8")
if "src_liege_prov_budget_l5_tick95" not in st:
    if not st.endswith("\n"):
        st += "\n"
    st += 'src_liege_prov_budget_l5_tick95,Province de Liege budget ordinaire 2026 named transfer articles,docs/doge/data/raw/liege_province_budget_2026.pdf,Province de Liege,2026-07-22,budget,"Named ASBL/culture/tourism lines F123 F569 F789; raw liege_province_budget_2026.pdf"\n'
    st += 'src_ccrek_hainaut_l5_tick95,Cour des comptes Hainaut budget 2026 ASBL and Voies d eau notes,docs/doge/data/raw/hainaut_prov_ccrek_budget_2026.pdf,Cour des comptes,2026-07-22,audit,"p17 Voies d eau 2.3m; Teralis cut; 199 entities; Tournai 3.9m; raw hainaut_prov_ccrek_budget_2026.pdf"\n'
    src.write_text(st, encoding="utf-8")
print("sources ok")

rq = root / "research_queue.csv"
rt = rq.read_text(encoding="utf-8")
rt = rt.replace(
    'rq_095,Walloon province L5 named subsidies sample (Hainaut or Liege),continuous,3,open,L5,prov_hainaut,"Parallel VL L5: extract 3+ named Walloon province subsidies/ASBL from CoA or budget PDF.",,2026-07-22T15:49:00Z,2026-07-22T15:49:00Z,"Walloon L1 complete; L5 thin vs VL agencies"',
    'rq_095,Walloon province L5 named subsidies sample (Hainaut or Liege),continuous,3,done,L5,prov_hainaut,"Parallel VL L5: extract 3+ named Walloon province subsidies/ASBL from CoA or budget PDF.",,2026-07-22T15:49:00Z,2026-07-22T16:04:00Z,"Hainaut: Voies d eau 2.3m; Tournai 3.9m; 199 entities opacity; Liege: sites 516k Opera 150k MNEMA 150k FTPL cut to 1 EUR"',
)
if "rq_096," not in rt:
    if not rt.endswith("\n"):
        rt += "\n"
    rt += 'rq_096,Hainaut full named ASBL EUR list FOI or secondary,continuous,3,open,L5,prov_hainaut,"If public annex of 199 entities with EUR appears: extract top 20; else open FOI for annex list with amounts.",,2026-07-22T16:04:00Z,2026-07-22T16:04:00Z,"CoA notes annex exists but amounts not in published CoA PDF"\n'
rq.write_text(rt, encoding="utf-8")
print("queue ok")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    'main,continuous,continuous,2026-07-22T16:04:00Z,rq_095,95,no,"Walloon L5 Hainaut Voies 2.3m + Liege culture/tourism named (tick95). Next: rq_096 Hainaut FOI or rq_089 SWA."\n',
    encoding="utf-8",
)
print("state ok")

log = Path("docs/doge/loop_log.md")
entry = """
### 2026-07-22T16:04:00Z -- tick 95
- Unit: rq_095 (Walloon province L5 named subsidies — Hainaut CoA + Liege budget)
- Found (strong): **Hainaut** CoA 2026: **ASBL Voies d'eau du Hainaut EUR 2,300,000** (incl **+1.8m** severance after canal tourism stop); **ASBL Teralis cut to 0** (was 0.4m; French domains sold); transfers hors zones **EUR 15.5m**; **Cathédrale Tournai invest EUR 3,900,000** (3.7m external subsidy); **199 entities** with aids >=50k/yr (annex exists; **amounts not in CoA PDF**; CoA flags **no motivation** for extraprovincialisation); 53 management contracts 2024. **Liege** budget 2026 named: tourism sites paraprovinciaux **EUR 516,011**; MNEMA **EUR 150,000**; Service social agents **EUR 190,878**; GIG **EUR 110,000**; DG cooperation **EUR 871,000**; Opera **EUR 150,000**; OPL **EUR 70,000**; Theatre Liege **EUR 60,000**; BRF 90k; RTC sport 124k; Parc HFE 60k. **FTPL** (Federation Tourisme) line **EUR 1** obligatoire 2026 (was **1.2m** 2025 — major cut/restructure in table).
- Wrote: 18 budgets; 6 commitments; 4 leaderboard; entities; 2 sources; rq_095=done; seeded rq_096 Hainaut annex/FOI; ticks=95
- FOI: **not drafted this tick** — rq_096 opened for 199-entity EUR list if public annex missing
- Next: **rq_096** Hainaut named ASBL list (prio 3) or **rq_089** SWA Q4 (prio 1)

""".encode("utf-8")
raw = log.read_bytes()
if b"tick 95" not in raw:
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + entry)
    print("log ok")
else:
    print("log exists")

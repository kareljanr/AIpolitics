# tick514 — CoA consultancy federal audit Oct 2025 L5 dual IT/Smals
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_consultancy_fed_2025,CoA Inzet van consultancy door de federale overheid Oct 2025,"
        "https://www.ccrek.be/sites/default/files/Docs/2025_Consultancy.pdf,"
        "Rekenhof AG 22 Oct 2025,2026-07-29,court_of_audit,"
        "Strong tick514: 2.525bn 2020-22 (IT 2.032 nonIT 0.492); top NMBS 465 Infrabel 319 Fin 185 BOSA 134; "
        "no central inventory; dual Smals/Persona; tick514\n"
    )
    f.write(
        "src_dual_consultancy_it_tick514,Dual federal consultancy mega-spend + education/IT failures,"
        "docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "DOGE synthesis CoA consultancy + prior Persona/Cepage/I-Police,2026-07-29,synthesis,"
        "Strong dual: 2.5bn consultancy 3y 81pct IT vs Persona 16m Cepage 35-96m I-Police 77m failures; tick514\n"
    )

buds = [
    "bud_fed_consultancy_total_2525m_2020_22,sec_federal,2022,2524700000,,,outturn,src_ccrek_consultancy_fed_2025,strong,Federal consultancy total 2524.7m incl VAT 2020-22 CoA survey 101 orgs; tick514",
    "bud_fed_consultancy_it_2032m_2020_22,sec_federal,2022,2032300000,,,outturn,src_ccrek_consultancy_fed_2025,strong,IT consultancy 2032.3m (81pct of total) 2020-22; tick514",
    "bud_fed_consultancy_nonit_492m_2020_22,sec_federal,2022,492400000,,,outturn,src_ccrek_consultancy_fed_2025,strong,Non-IT consultancy 492.4m (19pct) 2020-22; tick514",
    "bud_fed_consultancy_inhouse_619m_2020_22,sec_federal,2022,619200000,,,outturn,src_ccrek_consultancy_fed_2025,strong,In-house federal-to-federal consultancy 619.2m 2020-22; tick514",
    "bud_fed_consultancy_contracts_19bn_2020_22,sec_federal,2022,1900000000,,,outturn,src_ccrek_consultancy_fed_2025,strong,Other agreements/procurement consultancy ~1.9bn 2020-22; tick514",
    "bud_fed_consultancy_avg_annual_841m,sec_federal,2021,841600000,,,derived,src_ccrek_consultancy_fed_2025,medium,Illustrative avg annual 2524.7/3 ~841.6m 2020-22 class; not true yearly series; tick514",
    "bud_cons_nmbs_465m_2020_22,nmbs,2022,465100000,,,outturn,src_ccrek_consultancy_fed_2025,strong,NMBS consultancy 465.1m 2020-22 (IH 104.2 + AO 360.9; 9pct purchases); tick514",
    "bud_cons_infrabel_319m_2020_22,infrabel,2022,318500000,,,outturn,src_ccrek_consultancy_fed_2025,strong,Infrabel consultancy 318.5m 2020-22 (IH 40 + AO 278.5; 12pct); tick514",
    "bud_cons_fod_fin_185m_2020_22,sec_federal,2022,185300000,,,outturn,src_ccrek_consultancy_fed_2025,strong,FOD Financien consultancy 185.3m 2020-22 (22pct purchases); tick514",
    "bud_cons_fod_bosa_134m_2020_22,sec_federal,2022,134200000,,,outturn,src_ccrek_consultancy_fed_2025,strong,FOD BOSA consultancy 134.2m 2020-22 (45pct purchases); tick514",
    "bud_cons_niras_129m_2020_22,niras,2022,129100000,,,outturn,src_ccrek_consultancy_fed_2025,strong,NIRAS consultancy 129.1m 2020-22 (16pct); tick514",
    "bud_cons_smals_buyer_126m_2020_22,smals,2022,126100000,,,outturn,src_ccrek_consultancy_fed_2025,strong,Smals as buyer consultancy 126.1m 2020-22 (79pct of its purchase budget); tick514",
    "bud_cons_riziv_116m_2020_22,riziv,2022,115500000,,,outturn,src_ccrek_consultancy_fed_2025,strong,RIZIV consultancy 115.5m 2020-22 (48pct); tick514",
    "bud_cons_fod_health_70m_2020_22,sec_federal,2022,70100000,,,outturn,src_ccrek_consultancy_fed_2025,strong,FOD Volksgezondheid consultancy 70.1m 2020-22; tick514",
    "bud_cons_kanselarij_68m_2020_22,sec_federal,2022,68200000,,,outturn,src_ccrek_consultancy_fed_2025,strong,FOD Kanselarij+CCB+FIA+DAV+FIDO+PM cabinets consultancy 68.2m 2020-22; tick514",
    "bud_cons_credendo_62m_2020_22,sec_federal,2022,61500000,,,outturn,src_ccrek_consultancy_fed_2025,strong,Nationale Delcrederedienst consultancy 61.5m 2020-22 (47pct); tick514",
    "bud_cons_top12_dossier_14bn_2020_22,sec_federal,2022,1400000000,,,outturn,src_ccrek_consultancy_fed_2025,strong,12 dossier orgs consultancy 1.4bn 2020-22 (top10 1.3bn + Smals/Egov 126.3); tick514",
    "bud_cons_nuclear_nonit_215m_2020_22,sec_federal,2022,215200000,,,outturn,src_ccrek_consultancy_fed_2025,strong,Nuclear sector non-IT consultancy 215.2m (44pct of non-IT); tick514",
    "bud_cons_strategy_mgmt_87m_2020_22,sec_federal,2022,87200000,,,outturn,src_ccrek_consultancy_fed_2025,strong,Strategy/management/org consultancy 87.2m 2020-22; tick514",
    "bud_cons_construction_72m_2020_22,sec_federal,2022,72000000,,,outturn,src_ccrek_consultancy_fed_2025,strong,Construction consultancy 72.0m 2020-22; tick514",
    "bud_cons_sample_101_contracts_22bn,sec_federal,2022,2200000000,,,outturn,src_ccrek_consultancy_fed_2025,strong,101 consultancy contracts sample 2020-22 spend 2.2bn incl VAT legality review; tick514",
    "bud_smals_ext_share_turnover_36pct_2024,smals,2024,36,,,outturn,src_ccrek_consultancy_fed_2025,strong,Smals external IT consultancy share of turnover 36pct 2024 (was 17.8pct 2014); amount_eur stores pct — FIX",
]
# fix bad pct rows - store as notes only via commitments; remove bad row
buds = [b for b in buds if "bud_smals_ext_share" not in b]
buds += [
    "bud_smals_detachments_2072_fte_2024,smals,2024,2072,,,outturn,src_ccrek_consultancy_fed_2025,strong,Smals/Egov detachments headcount 2072 2024 (was 1395 2019 +48.5pct); amount_eur=FTE count not euros — remove",
]
buds = [b for b in buds if "bud_smals_detachments" not in b]
buds += [
    "bud_cons_gov_enterprises_843m_2020_22,sec_federal,2022,842700000,,,outturn,src_ccrek_consultancy_fed_2025,strong,Public enterprises (rail) consultancy users 842.7m 2020-22; tick514",
    "bud_cons_central_admin_713m_2020_22,sec_federal,2022,713200000,,,outturn,src_ccrek_consultancy_fed_2025,strong,Central administration consultancy users 713.2m 2020-22; tick514",
    "bud_cons_oisz_523m_2020_22,sec_ss,2022,523100000,,,outturn,src_ccrek_consultancy_fed_2025,strong,OISZ social security institutions consultancy users 523.1m 2020-22; tick514",
    "bud_dual_consultancy_it_2020_22,gg_belgium,2022,2524700000,,,derived,src_dual_consultancy_it_tick514,strong,Dual consultancy 2.5bn stack vs IT mega-failures; tick514",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

# entities if needed - smals may exist
cmts = [
    (
        "cmt_fed_consultancy_2525m_2020_22,Federal consultancy total 2.525bn 2020-22 CoA survey,"
        "sec_federal,Consultancies Smals NMBS,"
        "CoA consultancy report AG 22 Oct 2025,"
        "2025-10-22,2020,2022,2524700000,"
        '"{""total_m"":2524.7,""it_m"":2032.3,""nonit_m"":492.4,""inhouse_m"":619.2,'
        '""contracts_bn"":1.9,""orgs_n"":101,""avg_annual_m"":841.6,'
        '""nmbs_m"":465.1,""infrabel_m"":318.5,""fin_m"":185.3,""bosa_m"":134.2,'
        '""note"":""Strong CoA; declarative survey; no central inventory""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Transparent consultancy inventory,Central inventory FOI + strategy,"
        "src_ccrek_consultancy_fed_2025,strong,Federal>Consultancy>total_2020_22,tick514"
    ),
    (
        "cmt_cons_top_buyers_rail_fin,Top consultancy buyers NMBS Infrabel Finance BOSA NIRAS,"
        "sec_federal,NMBS Infrabel FOD Fin BOSA NIRAS,"
        "CoA consultancy Table1,"
        "2025-10-22,2020,2022,1232200000,"
        '"{""nmbs_m"":465.1,""infrabel_m"":318.5,""fin_m"":185.3,""bosa_m"":134.2,'
        '""niras_m"":129.1,""smals_buyer_m"":126.1,""riziv_m"":115.5,'
        '""bosa_share_pct"":45,""smals_buyer_share_pct"":79,'
        '""note"":""Strong CoA table; BOSA 45pct of purchase budget is consultancy""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Rank discretionary consultancy buyers,Cap + make-or-buy FOI,"
        "src_ccrek_consultancy_fed_2025,strong,Federal>Consultancy>top_buyers,tick514"
    ),
    (
        "cmt_cons_it_smals_dependency,IT consultancy 81pct + Smals external share rise 18to36pct,"
        "smals,Smals Egov IT vendors,"
        "CoA consultancy Ch2+Ch5 summary,"
        "2025-10-22,2014,2024,2032300000,"
        '"{""it_share_pct"":81,""it_m_2020_22"":2032.3,""smals_ext_turnover_2014_pct"":17.8,'
        '""smals_ext_turnover_2024_pct"":36.0,""detachments_2019"":1395,""detachments_2024"":2072,'
        '""knowledge_transfer_clause_missing_pct"":30,'
        '""note"":""Strong CoA; dependency risk; no make-or-buy analysis""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Reduce IT consultant dependency,Internal capacity strategy FOI,"
        "src_ccrek_consultancy_fed_2025,strong,Federal>IT>Smals_consultancy,tick514"
    ),
    (
        "cmt_dual_consultancy_it_failures,Dual consultancy 2.5bn vs Persona Cepage I-Police failures,"
        "gg_belgium,Federal IT education,"
        "CoA consultancy + prior dual IT ticks,"
        "2025-10-22,2020,2025,2524700000,"
        '"{""consultancy_3y_m"":2524.7,""persona_m"":16,""cepage_m_range"":""35-96"",'
        '""ipolice_spent_m"":76.7,'
        '""note"":""not additive pure TE; dual governance failure map""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Map dual IT waste governance,Inventory+strategy FOI,"
        "src_dual_consultancy_it_tick514,strong,BE>dual>consultancy_IT,tick514"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_fed_consultancy_2_5bn,Federal consultancy total 2.5bn 2020-22,federal,ops,Federal>Consultancy>total_2020_22,841600000,2524700000,Strong CoA: 2524.7m 3y ~842m/yr class; 81pct IT; no central inventory,strong,src_ccrek_consultancy_fed_2025,Consultancies agencies,External advisory and ops support,Mega opaque stack,7.0,9.0,5,7.65,Central inventory FOI,seed,,tick514",
    "lb_fed_consultancy_it_2_0bn,Federal IT consultancy 2.03bn 2020-22,federal,ops,Federal>Consultancy>IT_2020_22,677400000,2032300000,Strong CoA: 2032.3m IT 81pct; Smals ext share 18->36pct turnover,strong,src_ccrek_consultancy_fed_2025,IT vendors Smals,IT advisory and staffing,Dependency risk,7.0,9.0,5,7.65,Internal capacity FOI,seed,,tick514",
    "lb_cons_nmbs_465m,NMBS consultancy 465m 2020-22,federal,ops,Federal>NMBS>consultancy,155000000,465100000,Strong CoA table: 465.1m (9pct purchases); dual rail,strong,src_ccrek_consultancy_fed_2025,NMBS consultants,Rail IT and ops support,Large SOE consultancy,5.5,7.5,5,6.35,Publish L5 FOI,seed,,tick514",
    "lb_cons_infrabel_319m,Infrabel consultancy 319m 2020-22,federal,ops,Federal>Infrabel>consultancy,106200000,318500000,Strong CoA: 318.5m (12pct purchases),strong,src_ccrek_consultancy_fed_2025,Infrabel consultants,Rail infra support,Large SOE consultancy,5.5,7.5,5,6.35,Publish L5 FOI,seed,,tick514",
    "lb_cons_bosa_134m,FOD BOSA consultancy 134m 2020-22,federal,ops,Federal>BOSA>consultancy,44700000,134200000,Strong CoA: 134.2m = 45pct of BOSA purchase budget,strong,src_ccrek_consultancy_fed_2025,BOSA,Horizontal federal support,High share of own purchases,6.5,7.0,4,6.55,Cap + strategy FOI,seed,,tick514",
    "lb_cons_fod_fin_185m,FOD Finance consultancy 185m 2020-22,federal,ops,Federal>Finance>consultancy,61770000,185300000,Strong CoA: 185.3m (22pct purchases); dual tax control,strong,src_ccrek_consultancy_fed_2025,FOD Fin,Tax admin support,Large FOD spend,5.5,7.5,5,6.35,Inventory FOI,seed,,tick514",
    "lb_cons_no_inventory,No central federal consultancy inventory,federal,ops,Federal>Consultancy>inventory_gap,0,2524700000,Strong CoA: no exhaustive inventory; BOSA partial excl IT; openbaarheid art 3/3 no KB,strong,src_ccrek_consultancy_fed_2025,Parliament public,Transparency gap,Governance failure,8.5,9.0,4,8.35,Adopt inventory FOI,seed,,tick514",
    "lb_dual_consultancy_it,Dual consultancy 2.5bn + IT mega-failures,multi,ops,BE>dual>consultancy_IT,841600000,2524700000,Strong dual CoA consultancy + prior Persona/Cepage/I-Police,strong,src_dual_consultancy_it_tick514,Taxpayers,Dual IT governance map,Scale dual,7.0,9.0,5,7.65,Strategy+inventory FOI,seed,,tick514",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_fed_consultancy_inventory_l5,Federal>Consultancy>central_inventory_L5,sec_federal,"
    "Central exhaustive consultancy inventory 2020-2025 with object procedure award amount duration contractor CPV; "
    "annual series 2023-2025 update of CoA 2.525bn survey; Smals broker ranking deviations and rate vs market; "
    "KB implementing openbaarheid art 3/3 procurement+study inventory; make-or-buy analyses for top10 buyers,"
    "CoA Oct 2025: 2.5bn 3y no central inventory; 81pct IT dependency; dual Persona/Cepage,8,"
    "FOD BOSA / Eerste Minister,info@bosa.fgov.be,"
    ",docs/doge/foi/drafts/gap_fed_consultancy_inventory_l5.md,"
    "ready,2026-07-29,,,,,cmt_fed_consultancy_2525m_2020_22,"
    "lb_fed_consultancy_2_5bn|lb_cons_no_inventory|lb_dual_consultancy_it,"
    "2026-07-29T01:20:00Z,2026-07-29T01:20:00Z,"
    "tick514: CoA consultancy 2.5bn; FOI inventory human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_505,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T01:00:00Z,,Spawned tick513 after CoA defence/Fedasil residual; rq_116 deferred"
)
new = (
    "rq_505,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,"
    "gap_fed_consultancy_inventory_l5,"
    "2026-07-29T01:00:00Z,2026-07-29T01:20:00Z,"
    "tick514: CoA consultancy fed 2.5bn 2020-22 dual IT/Smals; FOI; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_505 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_506,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T01:20:00Z,,Spawned tick514 after CoA consultancy; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T01:20:00Z,rq_505,514,no,"
    "Tick514 CoA consultancy 2.5bn 2020-22 dual IT; next prio5 rq_506; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick514 OK")

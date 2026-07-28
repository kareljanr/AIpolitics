# tick515 — CoA Brussels Region budget 2026 dual Entity II
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_bru_budget_2026,CoA projets d'ordonnances budgets 2026 Region Bruxelles-Capitale,"
        "docs/doge/data/raw/ccrek_bru_budget_2026.pdf,"
        "Rekenhof AG 13 Mar 2026,2026-07-29,court_of_audit,"
        "Strong tick515: SEC -956.6m (CoA -978.2); eng 8.9bn liq 8.0bn; debt consol 16.1->17.7bn; "
        "STIB 1.168bn Actiris 648; measures 297->1186; dual E2; tick515\n"
    )
    f.write(
        "src_dual_bru_e2_tick515,Dual Brussels SEC deficit + Entity II aju maps,"
        "docs/doge/data/raw/ccrek_bru_budget_2026.pdf,"
        "DOGE synthesis CoA BRU 2026 + prior FWB/WAL/DG/VL,2026-07-29,synthesis,"
        "Strong dual: BRU SEC -0.96bn vs VL -4.0 WAL -2.02 FWB -1.75 DG -0.11; tick515\n"
    )

buds = [
    "bud_bru_sec_sf_956m_2026,brussels_gov,2026,-956600000,,,budgeted,src_ccrek_bru_budget_2026,strong,BRU SEC financing balance gov -956.6m IB2026 (+591 vs prov 2025); CoA content adj -978.2m; tick515",
    "bud_bru_sec_sf_coa_978m_2026,brussels_gov,2026,-978200000,,,derived,src_ccrek_bru_budget_2026,strong,CoA adjusted SEC SF -978.2m after content differences 21.6m; tick515",
    "bud_bru_sec_base_2025_1241m,brussels_gov,2025,-1241000000,,,budgeted,src_ccrek_bru_budget_2026,strong,SEC consolidated SF base 2025 -1241m (provisions used + offsets); tick515",
    "bud_bru_measures_297m_2026,brussels_gov,2026,297000000,,,budgeted,src_ccrek_bru_budget_2026,strong,New spend+receipt measures path 297m 2026 rising to 1186m 2029; receipt detail unavailable; tick515",
    "bud_bru_measures_1186m_2029,brussels_gov,2029,1186000000,,,budgeted,src_ccrek_bru_budget_2026,strong,New measures path 1186m 2029 for SEC balance 2029 objective; tick515",
    "bud_bru_sgrbc_net_finance_1746m_2026,brussels_gov,2026,-1746400000,,,budgeted,src_ccrek_bru_budget_2026,strong,SGRBC net to finance -1746.4m (+88.9 vs prov 2025); tick515",
    "bud_bru_sgrbc_gross_surplus_11m_2026,brussels_gov,2026,11400000,,,budgeted,src_ccrek_bru_budget_2026,strong,SGRBC gross budget balance +11.4m (rec +358.7 exp auth +75.9); tick515",
    "bud_bru_eng_89bn_2026,brussels_gov,2026,8900000000,,,budgeted,src_ccrek_bru_budget_2026,strong,General exp engagement credits 8.9bn IB2026 (+6.0pct / +0.5bn vs prov 2025); tick515",
    "bud_bru_liq_80bn_2026,brussels_gov,2026,8000000000,,,budgeted,src_ccrek_bru_budget_2026,strong,General exp liquidation credits 8.0bn IB2026 (+1.2pct / +0.1bn); tick515",
    "bud_bru_debt_consol_161bn_2025,brussels_gov,2025,16100000000,,,outturn,src_ccrek_bru_budget_2026,strong,Consolidated SEC debt eoy2025 16.1bn (+3.5bn 2023-25); tick515",
    "bud_bru_debt_consol_est_177bn_2026,brussels_gov,2026,17700000000,,,estimate,src_ccrek_bru_budget_2026,medium,CoA est consol debt eoy2026 17.7bn (cash positions stable 1.5bn); tick515",
    "bud_bru_debt_direct_lt_134bn_2025,brussels_gov,2025,13400000000,,,outturn,src_ccrek_bru_budget_2026,strong,Direct LT debt stock 13.4bn eoy2025; amort ceiling 0.5bn/yr; last loans 2071; tick515",
    "bud_bru_debt_path_limit_191bn_2029,brussels_gov,2029,19100000000,,,budgeted,src_ccrek_bru_budget_2026,medium,Debt increase limit +3.0bn to eoy2029 implies >19.1bn with 1.5bn cash; perimeter unclear CoA; tick515",
    "bud_bru_housing_fund_debt_15bn_2025,brussels_gov,2025,1500000000,,,outturn,src_ccrek_bru_budget_2026,strong,Fonds du logement debt 1.5bn eoy2025; tick515",
    "bud_bru_communal_refi_debt_13bn_2025,brussels_gov,2025,1300000000,,,outturn,src_ccrek_bru_budget_2026,strong,Communal treasury refinance fund debt 1.3bn eoy2025; tick515",
    "bud_bru_finops_max_1bn,brussels_gov,2029,1000000000,,,budgeted,src_ccrek_bru_budget_2026,medium,Financial ops (code 8) max envelope 1bn trajectory: SLRB 400 Vivaqua 180 Confex 150 Kanal 60; tick515",
    "bud_bru_stib_dot_1168m_2026,stib,2026,1167619000,,,budgeted,src_ccrek_bru_budget_2026,strong,STIB financing prog 42.112 eng=liq 1167.619m 2026; tick515",
    "bud_bru_stib_ppi_cut_965m_2026_29,stib,2029,-964600000,,,budgeted,src_ccrek_bru_budget_2026,strong,Gov reduces STIB multi-year invest plan by 964.6m 2026-29 vs STIB 2025 PPI; tick515",
    "bud_bru_actiris_dot_648m_2026,actiris,2026,648113000,,,budgeted,src_ccrek_bru_budget_2026,strong,Actiris financing 648.113m (-78.2 vs prior); tick515",
    "bud_bru_emploi_bee_984m_2026,brussels_gov,2026,983600000,,,budgeted,src_ccrek_bru_budget_2026,strong,Employment BEE programmes total 983.6m excl subsistence (-78 eng / -79 liq); tick515",
    "bud_bru_titres_services_304m_2026,brussels_gov,2026,303832000,,,budgeted,src_ccrek_bru_budget_2026,strong,Titres-services 303.832m (exec 2025 was 317.2m); tick515",
    "bud_bru_slrb_dot_687m_eng_2026,brussels_gov,2026,687258000,,,budgeted,src_ccrek_bru_budget_2026,strong,SLRB housing financing eng 687.258m liq 418.258m 2026; tick515",
    "bud_bru_proprete_dot_411m_2026,brussels_gov,2026,411102000,,,budgeted,src_ccrek_bru_budget_2026,strong,Bruxelles-Proprete financing liq 411.102m eng 406.476m; capital transfer 178.3m wrongly kept both sides CoA; tick515",
    "bud_bru_local_powers_758m_2026,brussels_gov,2026,757611000,,,budgeted,src_ccrek_bru_budget_2026,strong,Local powers support liq 757.611m eng 784.298m; tick515",
    "bud_bru_comm_commissions_692m_2026,brussels_gov,2026,691675000,,,budgeted,src_ccrek_bru_budget_2026,strong,Community commissions financing 691.675m; tick515",
    "bud_bru_debt_service_728m_2026,brussels_gov,2026,727758000,,,budgeted,src_ccrek_bru_budget_2026,strong,Public debt management interest+amort liq 727.758m eng 730.164m; tick515",
    "bud_bru_roads_liq_264m_2026,brussels_gov,2026,263940000,,,budgeted,src_ccrek_bru_budget_2026,strong,Regional roads prog liq 263.94m eng 424.037m; backlog 381.7m; need 1101m 2026-29; tick515",
    "bud_bru_kanal_credits_87m_2026,brussels_gov,2026,86700000,,,budgeted,src_ccrek_bru_budget_2026,medium,Kanal financing credits 86.7m of which 60m financial participation; budget of Kanal foundation omitted CoA; tick515",
    "bud_bru_underuse_35m_2026,brussels_gov,2026,35000000,,,budgeted,src_ccrek_bru_budget_2026,medium,Under-utilisation assumption +35m on SEC SF; tick515",
    "bud_bru_hrf_net_exp_growth_m022,brussels_gov,2026,-22,,,budgeted,src_ccrek_bru_budget_2026,strong,HRF proposed avg net primary exp growth -0.22pct/yr 2025-31; 2026 -0.61pct; amount stores bp -22; skip",
]
buds = [b for b in buds if "bud_bru_hrf_net_exp" not in b]
buds += [
    "bud_dual_bru_e2_2026,gg_belgium,2026,-956600000,,,derived,src_dual_bru_e2_tick515,strong,Dual BRU SEC -0.96bn vs Entity II peers; tick515",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_bru_budget_2026_sec_debt,Brussels Region IB2026 SEC deficit debt path CoA,"
        "brussels_gov,BCR taxpayers,"
        "CoA BRU budget 2026 AG 13 Mar 2026,"
        "2026-03-13,2026,2029,-956600000,"
        '"{""sec_sf_m"":-956.6,""sec_coa_adj_m"":-978.2,""base_2025_m"":-1241,'
        '""measures_2026_m"":297,""measures_2029_m"":1186,""eng_bn"":8.9,""liq_bn"":8.0,'
        '""debt_2025_bn"":16.1,""debt_2026_est_bn"":17.7,""debt_2029_path_bn"":19.1,'
        '""sgrbc_net_finance_m"":-1746.4,""finops_max_bn"":1.0,'
        '""note"":""Strong CoA; 5 working days only; receipt measures detail missing""}",'
        "0,active,docs/doge/data/raw/ccrek_bru_budget_2026.pdf,"
        "SEC balance 2029 path,Publish measure L5 FOI,"
        "src_ccrek_bru_budget_2026,strong,Bruxelles>Budget>IB2026,tick515"
    ),
    (
        "cmt_bru_stib_actiris_2026,STIB 1.168bn + Actiris 648m + titres-services 304m,"
        "brussels_gov,STIB Actiris users,"
        "CoA BRU budget 2026 programmes,"
        "2026-03-13,2026,2029,1167619000,"
        '"{""stib_m"":1167.619,""stib_ppi_cut_m"":964.6,""actiris_m"":648.113,'
        '""bee_m"":983.6,""titres_m"":303.832,""titres_exec2025_m"":317.2,'
        '""note"":""Strong CoA; STIB PPI cut vs operator plan""}",'
        "0,active,docs/doge/data/raw/ccrek_bru_budget_2026.pdf,"
        "Mobility and PES financing,Reconcile STIB PPI FOI,"
        "src_ccrek_bru_budget_2026,strong,Bruxelles>STIB_Actiris>2026,tick515"
    ),
    (
        "cmt_bru_top_programmes_2026,Top BRU programmes Table9 debt STIB housing local,"
        "brussels_gov,Regional programmes,"
        "CoA BRU Table9 significant expenses,"
        "2026-03-13,2026,2026,6478310000,"
        '"{""top_eng_m"":6478.3,""debt_service_m"":727.8,""stib_m"":1167.6,'
        '""local_m"":757.6,""slrb_eng_m"":687.3,""proprete_m"":411.1,'
        '""commissions_m"":691.7,""roads_liq_m"":263.9,""share_eng_pct"":73.1,'
        '""note"":""Strong CoA table; top programmes 73pct eng / 71pct liq""}",'
        "0,active,docs/doge/data/raw/ccrek_bru_budget_2026.pdf,"
        "Map largest BRU spend lines,Kanal omission FOI,"
        "src_ccrek_bru_budget_2026,strong,Bruxelles>Programmes>top2026,tick515"
    ),
    (
        "cmt_dual_bru_e2_sec,Dual Brussels SEC -0.96bn vs Entity II peers,"
        "gg_belgium,Entity II,"
        "CoA BRU + prior E2 dual,"
        "2026-03-13,2026,2026,-956600000,"
        '"{""bru_m"":-956.6,""vl_class_bn"":-4.0,""wal_bn"":-2.02,""fwb_bn"":-1.75,'
        '""dg_bn"":-0.11,'
        '""note"":""not additive pure TE; dual Entity II map""}",'
        "0,active,docs/doge/data/raw/ccrek_bru_budget_2026.pdf,"
        "Map Entity II deficit dual,SWA net exp FOI,"
        "src_dual_bru_e2_tick515,strong,BE>dual>BRU_E2,tick515"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_bru_sec_deficit_957m_2026,Brussels SEC financing deficit 957m 2026,regional,ops,Bruxelles>SEC>SF_2026,956600000,956600000,Strong CoA: -956.6m gov / CoA adj -978.2; dual E2,strong,src_ccrek_bru_budget_2026,BCR,Regional deficit path,Core regional financing,5.0,7.5,5,6.25,Measure L5 FOI,seed,,tick515",
    "lb_bru_debt_16_1bn_2025,Brussels consolidated debt 16.1bn eoy2025,regional,ops,Bruxelles>Debt>consol_2025,0,16100000000,Strong CoA: 16.1bn (+3.5 2023-25); est 17.7 2026 path >19.1 2029; annual=0 stock,strong,src_ccrek_bru_budget_2026,Bondholders,Regional debt stock,Debt pressure,5.0,9.5,6,7.15,Publish multi-year debt FOI,seed,,tick515",
    "lb_bru_stib_1_17bn_2026,STIB financing 1.168bn 2026,regional,ops,Bruxelles>STIB>dot_2026,1167619000,1167619000,Strong CoA: 1167.619m; PPI cut 964.6m 2026-29 dual,strong,src_ccrek_bru_budget_2026,STIB riders,Public transport PSO,Largest mobility line,4.0,9.0,5,6.55,PPI reconcile FOI,seed,,tick515",
    "lb_bru_actiris_648m_2026,Actiris financing 648m 2026,regional,ops,Bruxelles>Actiris>dot_2026,648113000,648113000,Strong CoA: 648.113m (-78.2); dual PES VDAB/FOREM,strong,src_ccrek_bru_budget_2026,Jobseekers,Brussels PES,Core labour market,3.5,7.5,4,5.85,Dual PES FOI,seed,,tick515",
    "lb_bru_measures_297_1186,BRU measures path 297m to 1186m 2026-29,regional,savings,Bruxelles>Measures>path_2026_29,297000000,1186000000,Strong CoA: 297->1186; receipt L5 missing; dual prior Entity II,strong,src_ccrek_bru_budget_2026,Taxpayers,Consolidation path,Soft measure opacity,6.5,7.5,5,6.75,Programme table FOI,seed,,tick515",
    "lb_bru_liq_8bn_2026,Brussels liquidation credits 8.0bn 2026,regional,ops,Bruxelles>Exp>liq_2026,8000000000,8900000000,Strong CoA: liq 8.0 eng 8.9; dual prior SGRBC,strong,src_ccrek_bru_budget_2026,Regional services,Regional expenditure,Core regional mass,2.5,9.5,5,6.55,Top programme FOI,seed,,tick515",
    "lb_bru_kanal_omission,Kanal foundation budget omitted OAA2 list,regional,ops,Bruxelles>Kanal>omission,86700000,86700000,Medium CoA: 86.7m credits of which 60m finops; foundation budget missing,medium,src_ccrek_bru_budget_2026,Kanal,Cultural infrastructure,Governance omission,7.0,5.5,3,6.45,Integrate budget FOI,seed,,tick515",
    "lb_dual_bru_e2,Dual BRU SEC -0.96bn vs Entity II peers,multi,ops,BE>dual>BRU_E2,956600000,956600000,Strong dual CoA BRU + prior E2 aju,strong,src_dual_bru_e2_tick515,Entity II taxpayers,Dual regional deficits,Scale dual,5.0,9.0,5,6.75,SWA net exp FOI,seed,,tick515",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_bru_measures_stib_kanal_l5,Bruxelles>Measures_STIB_Kanal_L5,brussels_gov,"
    "Programme-level L5 table for measures path 297-1186m 2026-29 (receipt detail missing); "
    "STIB PPI vs regional credits reconciliation and 964.6m cut cash-by-year; Kanal foundation full budget "
    "and OAA2 inclusion; financial ops 1bn named terms SLRB/Vivaqua/Confex/Kanal; multi-year debt projection,"
    "CoA BRU 2026: 5-day review; measure opacity; Kanal omitted; STIB PPI cut,7,"
    "SPRB / Bruxelles Finances / STIB,transparence@sprb.brussels,"
    ",docs/doge/foi/drafts/gap_bru_measures_stib_kanal_l5.md,"
    "ready,2026-07-29,,,,,cmt_bru_budget_2026_sec_debt,"
    "lb_bru_sec_deficit_957m_2026|lb_bru_stib_1_17bn_2026|lb_bru_kanal_omission,"
    "2026-07-29T01:40:00Z,2026-07-29T01:40:00Z,"
    "tick515: CoA BRU budget 2026; FOI L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_506,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T01:20:00Z,,Spawned tick514 after CoA consultancy; rq_116 deferred"
)
new = (
    "rq_506,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,"
    "gap_bru_measures_stib_kanal_l5,"
    "2026-07-29T01:20:00Z,2026-07-29T01:40:00Z,"
    "tick515: CoA BRU budget 2026 SEC -957m debt 16.1bn STIB 1.17bn dual E2; FOI; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_506 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_507,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T01:40:00Z,,Spawned tick515 after CoA BRU budget; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T01:40:00Z,rq_506,515,no,"
    "Tick515 CoA BRU budget SEC -957m debt 16.1bn STIB 1.17bn dual E2; next prio5 rq_507; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick515 OK")

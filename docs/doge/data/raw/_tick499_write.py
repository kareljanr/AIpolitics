# tick499 — CoA 2026_32 VL Rekeningenrapport 2025 + dual Entity II
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_vl_rekeningen_2025,Rekenhof Rekeningenrapport over 2025 Vlaamse deelstaatoverheid 2026_32,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_32_Rekeningenrapport2025.pdf,"
        "Rekenhof NL chamber 30 Jun 2026,2026-07-28,court_of_audit,"
        "Strong: ESR saldo -3982.4m; Maastricht debt 50171.9m (+8383.3); Zaventem PMV 2553.6m; "
        "Lantis loans 1128m; nonbudget debt 1069.7m; dual Entity II; tick499\n"
    )
    f.write(
        "src_ccrek_vl_rekeningen_2025_press,CoA press Rekeningenrapport 2025 Jul 2026,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_32_Rekeningenrapport2025_Persbericht.pdf,"
        "Rekenhof,2026-07-28,court_of_audit_press,"
        "Strong headlines: tekort 3.9bn schuld 50.2bn vs 41.8; onthouding balans; "
        "voorbehoud 0.7bn verbintenissen; debt 18.6->50.2bn +170pct; tick499\n"
    )
    f.write(
        "src_ccrek_vl_rekeningen_2025_addendum,CoA addendum evolutie vorderingensaldo en schuld 2019-2025,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_32_Rekeningenrapport2025_Addendum.pdf,"
        "Rekenhof,2026-07-28,court_of_audit,"
        "Strong companion analysis 2019-2025 saldo vs debt; tick499\n"
    )
    f.write(
        "src_dual_vl_outturn_e2_tick499,Dual VL ESR outturn -4.0bn 2025 vs Entity II aju maps WAL FWB DG,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_32_Rekeningenrapport2025.pdf,"
        "DOGE synthesis CoA VL RR + prior dual,2026-07-28,synthesis,"
        "Strong dual: VL certified -3982.4m 2025 vs WAL aju -2015 FWB -1753 DG -111; debt +8.4bn; tick499\n"
    )

buds = [
    "bud_vl_esr_saldo_2025_rr,vlaanderen_gov,2025,-3982400000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,ESR vorderingensaldo -3982.4m certified CoA RR2025 (vs -4101.3 2024; BA -4503.8); tick499",
    "bud_vl_esr_saldo_2024_rr,vlaanderen_gov,2024,-4101300000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,ESR vorderingensaldo -4101.3m 2024 CoA RR2025 Table kerncijfers; tick499",
    "bud_vl_debt_maastricht_2025_rr,vlaanderen_gov,2025,50171900000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Maastricht debt 50171.9m eoy2025 (+8383.3 vs 41788.6 eoy2024); upgrades BA source; tick499",
    "bud_vl_debt_maastricht_2024_rr,vlaanderen_gov,2024,41788600000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Maastricht debt 41788.6m eoy2024 CoA RR (INR restated +187.6m GSC); tick499",
    "bud_vl_debt_consol_gross_2025,vlaanderen_gov,2025,58721900000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Total geconsolideerde schuld 58721.9m eoy2025 before Maastricht corrections Table22; tick499",
    "bud_vl_debt_direct_2025_rr,vlaanderen_gov,2025,42396600000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Directe uitstaande schuld 42396.6m eoy2025 (+9321.4); tick499",
    "bud_vl_debt_delta_2025,vlaanderen_gov,2025,8383300000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Maastricht debt +8383.3m 2025; deficit ~4bn + Zaventem ~2.7bn + housing ESR8 residual; tick499",
    "bud_vl_pmv_zaventem_2554m,pmv,2025,2553600000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Kapitaalsverhoging PMV financing BAC Zaventem 2553.6m (amendment post-BA); debt impact class 2.7bn CoA; tick499",
    "bud_vl_lantis_debt_2025,lantis,2025,2401300000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Lantis debt component 2401.3m eoy2025 (+1166.5); loans from ministry 1128m 2025; tick499",
    "bud_vl_lantis_loans_2025,lantis,2025,1128000000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Ministry LT loans to Lantis 1128m 2025 (250m 2023 + 950m 2024 path); tick499",
    "bud_vl_vwf_debt_2025,vwf,2025,6062800000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,VWF debt 6062.8m eoy2025 (+1196.4); social housing finance; tick499",
    "bud_vl_vmsw_debt_2025,vmsw,2025,3123400000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,VMSW debt 3123.4m eoy2025 (-216.1); tick499",
    "bud_vl_central_financed_debt_2025,vlaanderen_gov,2025,17464200000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Centraal gefinancierde entiteiten outstanding 17464.2m eoy2025; tick499",
    "bud_vl_toekomstverbond_cum_2025,lantis,2025,3851600000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Toekomstverbond financing cum 3851.6m eoy2025 Table23 (capital+loans+overkap); tick499",
    "bud_vl_nonbudget_debt_build_2025,vlaanderen_gov,2025,1069700000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Non-budgetary verrichtingen share of debt build 1069.7m 2025; Parliament under-informed CoA; tick499",
    "bud_vl_missing_assets_1_6bn,vlaanderen_gov,2025,1600000000,,,estimated,src_ccrek_vl_rekeningen_2025,strong,Missing land/buildings still at zero on balance; CoA own estimate 1.6bn; tick499",
    "bud_vl_art_collection_booked_1_4bn,vlaanderen_gov,2025,1400000000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Art collection 1.4bn booked 2022; disputed ownership residual unbooked; CoA cannot confirm valuation; tick499",
    "bud_vl_open_commit_fwo_fio_2025,vlaanderen_gov,2025,750200000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Openstaande verbintenissen understated: FWO 561.6m + FIO 188.6m; CoA reservation on budget execution; tick499",
    "bud_vl_credit_carry_to_2026,vlaanderen_gov,2026,1415300000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Overdracht beleidskredieten to 2026 1415.3m (from 1255.3 to 2025); indexprovisie underuse; tick499",
    "bud_vl_relance_spend_2025,vlaanderen_gov,2025,399400000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Relance Vlaamse Veerkracht spend 399.4m 2025 (-342.2 vs budget); cum commit 4.2bn liq 3.5bn open 0.7bn; tick499",
    "bud_vl_relance_cum_commit_2025,vlaanderen_gov,2025,4200000000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Relance plan cumulative vastgelegd 4.2bn end-2025; tick499",
    "bud_vl_go_patrimony_2025,go_onderwijs,2025,1004000000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,GO! land/buildings book value 1004.0m (79pct of GO balance); inventory still incomplete; tick499",
    "bud_vl_vsb_portfolio_2025,vsb,2025,1034900000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,VSB investment portfolio 1034.9m eoy2025; equities 293.8m 28.4pct vs VR equity cap; tick499",
    "bud_vl_5g_auction_budget_miss_2025,vlaanderen_gov,2025,19500000,,,budgeted,src_ccrek_vl_rekeningen_2025,strong,5G spectrum expected rec 19.5m/yr not received 2025 (split key pending Overlegcomite); federal pool 741.8m net; tick499",
    "bud_dual_vl_outturn_e2_2025,gg_belgium,2025,3982400000,,,derived,src_dual_vl_outturn_e2_tick499,strong,Dual VL certified deficit 3982.4m class vs WAL/FWB/DG aju maps (not additive TE); tick499",
    "bud_vl_esr_receipts_over_2025,vlaanderen_gov,2025,353800000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,ESR receipts +0.6pct / +353.8m vs BA2025; tick499",
    "bud_vl_esr_underuse_2025,vlaanderen_gov,2025,1830300000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,ESR spend under-use 2.8pct / 1830.3m 2025 (BA assumed 1773.7m); tick499",
    "bud_vl_dienstencheques_overrun_2025,vlaanderen_gov,2025,149300000,,,outturn,src_ccrek_vl_rekeningen_2025,strong,Dienstencheques meeruitgave 149.3m vs BA2025 ministries; tick499",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_vl_rekeningen_2025_path,Flanders certified ESR outturn 2025 + Maastricht debt +8.4bn,"
        "vlaanderen_gov,Flanders residents taxpayers,CoA Rekeningenrapport 2026_32 + KSW 2025,"
        "2026-06-30,2025,2025,50171900000,"
        '"{""esr_saldo_m"":-3982.4,""debt_maastricht_m"":50171.9,""debt_2024_m"":41788.6,'
        '""debt_delta_m"":8383.3,""debt_gross_m"":58721.9,""direct_debt_m"":42396.6,'
        '""zaventem_pmv_m"":2553.6,""zaventem_debt_impact_bn"":2.7,""lantis_m"":2401.3,'
        '""vwf_m"":6062.8,""vmsw_m"":3123.4,""central_fin_m"":17464.2,""nonbudget_build_m"":1069.7,'
        '""debt_2019_bn"":18.6,""debt_growth_pct_2019_25"":170.1,'
        '""note"":""Strong CoA certified; Parliament under-informed on debt-saldo bridge""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_32_Rekeningenrapport2025.pdf,"
        "Accountable public finances Flanders,Publish full debt-saldo bridge L5; dual Entity II,"
        "src_ccrek_vl_rekeningen_2025,strong,Vlaanderen>FB>Rekeningen_2025,tick499 dual E2"
    ),
    (
        "cmt_vl_pmv_zaventem_2025,PMV capital increase BAC Zaventem airport stake,"
        "pmv,Flanders via PMV airport ownership,Amendement post BA2025 + CoA RR2025,"
        "2025-01-01,2025,2025,2553600000,"
        '"{""capital_m"":2553.6,""debt_impact_bn_class"":2.7,""post_ba_amendment"":true,'
        '""note"":""Strong CoA: main debt delta driver after deficit""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_32_Rekeningenrapport2025.pdf,"
        "Strategic airport participation,Open full cash+governance L5 dual BAC,"
        "src_ccrek_vl_rekeningen_2025,strong,Vlaanderen>PMV>Zaventem,tick499"
    ),
    (
        "cmt_vl_toekomstverbond_cum_2025,Toekomstverbond/Lantis financing cumulative eoy2025,"
        "lantis,Antwerp mobility Oosterweel,CoA RR2025 Table23,"
        "2003-01-01,2003,2025,3851600000,"
        '"{""cum_m"":3851.6,""loans_m"":2401.3,""capital_cash_m"":885.1,""capital_natura_m"":287.1,'
        '""land_claim_m"":176.5,""overkap_m"":101.6,""loans_2025_m"":1128,'
        '""note"":""Strong CoA reconstruct; dual GIP""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_32_Rekeningenrapport2025.pdf,"
        "Oosterweel/Toekomstverbond delivery,Track dual GIP Lantis outturn,"
        "src_ccrek_vl_rekeningen_2025,strong,Vlaanderen>Lantis>Toekomstverbond,tick499"
    ),
    (
        "cmt_vl_relance_veerkracht_cum,Relanceplan Vlaamse Veerkracht cumulative execution,"
        "vlaanderen_gov,Flanders recovery projects,CoA RR2025 section 4.4,"
        "2021-01-01,2021,2026,4200000000,"
        '"{""cum_commit_bn"":4.2,""cum_liq_bn"":3.5,""open_bn"":0.7,""spend_2025_m"":399.4,'
        '""underuse_2025_m"":342.2,""note"":""Strong CoA; projects >10m delay queried""}",'
        "700000000,active,https://www.ccrek.be/sites/default/files/Docs/2026_32_Rekeningenrapport2025.pdf,"
        "COVID/energy recovery investment,Close open 0.7bn; dual RRF,"
        "src_ccrek_vl_rekeningen_2025,strong,Vlaanderen>Relance>Veerkracht,tick499"
    ),
    (
        "cmt_dual_vl_outturn_entity2,Dual VL certified 2025 outturn vs Entity II aju deficits,"
        "gg_belgium,Entity II taxpayers,CoA VL RR + WAL FWB DG aju,"
        "2026-06-30,2025,2026,3982400000,"
        '"{""vl_esr_m"":-3982.4,""wal_aju_m"":-2015.4,""fwb_aju_m"":-1752.8,""dg_esvg_m"":-110.5,'
        '""note"":""not additive TE; different years metric outturn vs aju""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_32_Rekeningenrapport2025.pdf,"
        "Subnational fiscal dual map,Comparable control accounts SWA,"
        "src_dual_vl_outturn_e2_tick499,strong,BE>dual>Entity2_VL_outturn,tick499"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_vl_esr_deficit_4_0bn_2025,Flanders ESR vorderingentekort 4.0bn 2025 certified,regional,deficit,Vlaanderen>ESR>saldo_2025,3982400000,3982400000,Strong CoA RR: -3982.4m better than BA -4503.8 and 2024 -4101.3; dual Entity II,strong,src_ccrek_vl_rekeningen_2025,Flanders taxpayers,Fiscal sustainability,Core deficit mass; debt still +8.4bn,4.0,9.5,6,6.7,Publish full saldo-debt bridge L5,seed,,tick499",
    "lb_vl_debt_50_2bn_2025,Flanders Maastricht debt 50.2bn eoy2025,regional,debt_stock,Vlaanderen>Schuld>Maastricht_2025,0,50171900000,Strong CoA: 50171.9m from 41788.6 (+8383.3); 18.6bn 2019 (+170pct); annual0 stock,strong,src_ccrek_vl_rekeningen_2025,Creditors residents,Debt stock path,Snowball + equity injections,6.0,9.5,6,7.35,Control account + nonbudget L5 FOI,seed,,tick499",
    "lb_vl_zaventem_pmv_2_55bn,PMV Zaventem BAC capital increase 2.55bn 2025,regional,equity_injection,Vlaanderen>PMV>Zaventem_BAC,2553600000,2553600000,Strong CoA: 2553.6m post-BA amendment; debt impact class 2.7bn; dual airport stakes,strong,src_ccrek_vl_rekeningen_2025,Airport stakeholders,Strategic airport ownership,Huge off-budget-class equity; governance FOI,6.5,8.5,5,7.05,Full BAC cash+control FOI dual,seed,,tick499",
    "lb_vl_nonbudget_debt_1_07bn,Flanders non-budgetary debt build 1.07bn 2025,regional,opacity,Vlaanderen>Schuld>nonbudget_2025,1069700000,1069700000,Strong CoA: 1069.7m non-budgetary share of debt build; Parliament under-informed,strong,src_ccrek_vl_rekeningen_2025,Parliament taxpayers,Debt transparency,Classic DOGE opacity between saldo and debt,7.5,7.5,5,7.25,FOI L5 bridge components,seed,,tick499",
    "lb_vl_toekomstverbond_3_85bn,Toekomstverbond/Lantis financing cum 3.85bn eoy2025,regional,infrastructure,Vlaanderen>Lantis>Toekomstverbond,0,3851600000,Strong CoA Table23: 3851.6m cum; loans 2401.3; 1128m loans 2025; dual GIP,strong,src_ccrek_vl_rekeningen_2025,Antwerp mobility users,Oosterweel delivery,Multi-decade mega-project stock,4.5,8.0,5,6.05,Dual GIP L5 outturn FOI,seed,,tick499",
    "lb_vl_missing_assets_1_6bn,Flanders unbooked land/buildings ~1.6bn,regional,accounting,Vlaanderen>Balans>missing_assets,0,1600000000,Strong CoA: still zero-valued; own estimate 1.6bn; art 1.4bn partial; onthouding,strong,src_ccrek_vl_rekeningen_2025,Parliament,Balance sheet integrity,Repeated CoA disclaimer years,6.5,6.5,4,6.25,Finish asset inventory 2026 GO!,seed,,tick499",
    "lb_dual_vl_outturn_e2,Dual VL outturn 4.0bn vs WAL/FWB/DG aju maps,multi,deficit,BE>dual>Entity2_VL_outturn_2025,3982400000,7858400000,Strong dual: VL certified -4.0bn 2025 vs WAL -2.02 FWB -1.75 DG -0.11 aju class,strong,src_dual_vl_outturn_e2_tick499,Entity II taxpayers,Subnational fiscal dual,Scale dual not TE-additive,4.0,9.0,5,6.55,SWA assent + comparable ledgers,seed,,tick499",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

# FOI queue
foi = (
    "gap_vl_debt_nonbudget_bridge_l5,Vlaanderen>Schuld>nonbudget_debt_bridge_2025,vlaanderen_gov,"
    "L5 component table bridging ESR vorderingensaldo to Maastricht debt delta 2025 "
    "(incl non-budgetary 1069.7m; ESR8/9; Zaventem 2553.6; Lantis/VWF/VMSW cash),"
    "CoA RR2025: debt +8.4bn vs deficit 4.0bn; Parliament under-informed on bridge,8,"
    "Departement Financiën en Begroting / Team Openbaarheid Vlaanderen,openbaarheid@vlaanderen.be,"
    "Havenlaan 88 bus 20 1000 Brussel,docs/doge/foi/drafts/gap_vl_debt_nonbudget_bridge_l5.md,"
    "ready,2026-07-28,,,,,cmt_vl_rekeningen_2025_path,"
    "lb_vl_nonbudget_debt_1_07bn|lb_vl_debt_50_2bn_2025,"
    "2026-07-28T20:30:00Z,2026-07-28T20:30:00Z,"
    "tick499: CoA 2026_32 primary fill; residual L5 bridge FOI human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

# research_queue: mark rq_490 done, spawn rq_491
rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_490,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-28T20:10:00Z,,Spawned tick498 after VL teacher induction CoA; next progress@500; rq_116 deferred"
)
new = (
    "rq_490,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,"
    "gap_vl_debt_nonbudget_bridge_l5,"
    "2026-07-28T20:10:00Z,2026-07-28T20:30:00Z,"
    "tick499: CoA 2026_32 VL RR ESR -4.0bn debt 50.2bn Zaventem 2.55bn dual E2; FOI debt bridge; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_490 row not found for update")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_491,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-28T20:30:00Z,,Spawned tick499 after CoA VL Rekeningenrapport 2025; progress@500 next tick; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

# loop_state
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-28T20:30:00Z,rq_490,499,no,"
    "Tick499 CoA VL RR2025 ESR-4.0bn debt50.2bn Zaventem2.55bn; next prio5 rq_491; progress@500 next; rq_116 SWA deferred.\n",
    encoding="utf-8",
)

print("tick499 writes OK")

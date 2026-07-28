# tick509 — CoA 2026_22 residual Werk/werkloosheid + invalidity multi-year dual POD MI
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_fed_aju_unemp_rva_2026,CoA fed budget aju 2026 RVA werkloosheid residual 2026_22,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Rekenhof AG 21 May 2026,2026-07-28,court_of_audit,"
        "Strong residual tick509: unemp BC 4836.4m; reform save path 1685-2448m; exclusion waves 193904; "
        "leefloon shift 31.9pct Q1; litigation ~3m; dual POD MI; tick509\n"
    )
    f.write(
        "src_dual_unemp_leefloon_tick509,Dual unemployment reform savings + leefloon OCMW shift,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "DOGE synthesis CoA 2026_22 residual unemp + POD MI,2026-07-28,synthesis,"
        "Strong dual: RVA reform 1.69bn save path 2026 vs 17.6k Q1 leeflooners 31.9pct of excluded; tick509\n"
    )

buds = [
    # Unemployment volume + reform stack
    "bud_rva_unemp_volume_effect_287m,sec_ss,2026,287000000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,Unemp volume effect +287m BC vs IB (full unemp +17473 temporary -3851); tick509",
    "bud_rva_unemp_other_adj_neg97m,sec_ss,2026,-96700000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,Unemp other adjustments -96.7m (avg daily rate arrears days category shifts); tick509",
    "bud_rva_unemp_index_8m,sec_ss,2026,8200000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,Unemp spilindex impact +8.2m (Dec2025; June2026 unpriced by RVA); tick509",
    "bud_rva_reform_save_path_2026,sec_ss,2026,1685200000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,Unemployment duration limit + degressivity save path 1685.2m 2026 (progwet 18 Jul 2025); tick509",
    "bud_rva_reform_save_path_2027,sec_ss,2027,2286700000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,Unemp reform save path 2286.7m 2027; tick509",
    "bud_rva_reform_save_path_2028,sec_ss,2028,2440600000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,Unemp reform save path 2440.6m 2028; tick509",
    "bud_rva_reform_save_path_2029,sec_ss,2029,2447800000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,Unemp reform save path 2447.8m 2029; tick509",
    "bud_rva_measures_total_path_2026,sec_ss,2026,1578500000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,RVA multi-year measures net total path 1578.5m 2026 (incl reform + side measures); tick509",
    "bud_rva_measures_total_path_2029,sec_ss,2029,2421200000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,RVA multi-year measures net total path 2421.2m 2029; tick509",
    "bud_rva_vol_quit_temp_unemp_cost_34m,sec_ss,2026,-33600000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,Voluntary resignation with temp unemp benefit cost -33.6m/yr path; tick509",
    "bud_rva_swt_close_2026_cost,sec_ss,2026,-5200000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,medium,SWT no-new-entries: RVA books -5.2m 2026 rush cost; CoA stats do not show rush; 2029 save 64.8m; tick509",
    "bud_rva_swt_save_path_2029,sec_ss,2029,64800000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,SWT close save path 64.8m 2029 (was 77m IB2025; re-est Jun2025); tick509",
    "bud_rva_swt_benefits_2025,sec_ss,2025,166800000,,,outturn,src_ccrek_fed_aju_unemp_rva_2026,strong,SWT unemp benefits 166.8m 2025; 8502 beneficiaries; tick509",
    "bud_rva_tijdskrediet_el_save_2026,sec_ss,2026,1600000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,End-career time credit stricter career req save 1.6m 2026 (was 9.2 IB2025); path to 12.3m 2029; tick509",
    "bud_rva_familiekrediet_envelop_40m,sec_federal,2026,40000000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,medium,Extra family credit backpack Entity I envelop 40m 2026 (full-year 50m); law not set; CoA overstated risk; tick509",
    "bud_rva_litigation_extra_3m,sec_ss,2026,3000000,,,derived,src_ccrek_fed_aju_unemp_rva_2026,medium,CoA est extra legal costs ~3m from unemp reform litigation (3696 dossiers Apr30; RVA expects ~5000); not in BC; tick509",
    "bud_rva_it_modern_extra_8m,sec_ss,2026,8000000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,RVA IT modernisation extra 8m MR 3 Apr 2026; tick509",
    "bud_rva_hvw_it_8m,sec_ss,2026,8000000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,HVW IT spend path 8m 2026 (10m 2028-29); tick509",
    "bud_rva_excl_waves_total_n,sec_ss,2026,193904,,,outturn,src_ccrek_fed_aju_unemp_rva_2026,strong,Exclusion waves total persons 193904 (BRU 41709 VL 62676 WAL 88566 DG 953) raming Sep2025; tick509",
    "bud_rva_excl_q1_actual_n,sec_ss,2026,45592,,,outturn,src_ccrek_fed_aju_unemp_rva_2026,strong,Q1 2026 actual exclusions waves1-2: 45592 (93.4pct of estimate 48815); tick509",
    "bud_podmi_leefloon_from_excl_q1_n,sec_federal,2026,17606,,,outturn,src_ccrek_fed_aju_unemp_rva_2026,strong,New leeflooners from unemp/inschakeling exclusion Q1: 17606 = 31.9pct of excluded; WAL 37.2 VL 23.5 BRU 27.5; tick509",
    # Invalidity residual multi-year
    "bud_invalidity_slip_cumul_2029,sec_ss,2029,-333600000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,Invalidity measures cumulative miss to 2029 -333.6m (vs ziektepensioen +10.2m); tick509",
    "bud_solidarity_contrib_98m_2026,sec_ss,2026,98400000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,Employer solidarity contrib months 2-3 invalidity 98.4m 2026 (-24 vs IB); tick509",
    "bud_responsabilisering_137m_2026,sec_ss,2026,137000000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,medium,RTW responsabilisering path 137m 2026 (fonds 77 workers 10 doctors 50); doctors law incomplete; tick509",
    "bud_unemp_to_invalidity_inflow_44m,sec_ss,2026,44100000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,medium,RIZIV est 5000/yr unemp->invalidity inflow +44.1m 2026 (94.9/99.2/97.5 2027-29); RVA monitoring not yet large; tick509",
    "bud_mantelzorg_verlof_extra_08m,sec_ss,2026,400000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,medium,Mantelzorg leave extension half-year impact ~0.4m 2026 (full yr 0.8m RVA; not in BC); CoA min free-avail 1.2m; tick509",
    "bud_pens_igo_save_slip_13m,sec_ss,2026,13000000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,medium,IGO control/residence save 13m BC (was 26); law not drafted; CoA no measure detail; tick509",
    "bud_pens_high_index_cap_53m,sec_ss,2026,53500000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,Limited indexation higher pensions save 53.5m BC (was 39.9); may understate if June index; tick509",
    "bud_pens_ziekte_close_32m,sec_ss,2026,32000000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,Ziektepensioen civil servants close save 32m (was 26; moratorium); RIZIV +9m expense; tick509",
    "bud_fpd_mypension_it_5m,sec_ss,2026,5000000,,,budgeted,src_ccrek_fed_aju_unemp_rva_2026,strong,FPD MyPension + legacy modernisation extra 5m; tick509",
    "bud_dual_unemp_leefloon_2026,gg_belgium,2026,1685200000,,,derived,src_dual_unemp_leefloon_tick509,strong,Dual reform save path 1.69bn vs leefloon shift 17.6k Q1; tick509",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_rva_unemp_reform_path,RVA unemployment duration limit + degressivity multi-year path,"
        "sec_ss,Unemployed claimants,"
        "CoA 2026_22 §5.3.1 progwet 18 Jul 2025,"
        "2025-07-18,2026,2029,1685200000,"
        '"{""save_2026_m"":1685.2,""save_2027_m"":2286.7,""save_2028_m"":2440.6,""save_2029_m"":2447.8,'
        '""excl_total_n"":193904,""q1_excl_n"":45592,""q1_leefloon_n"":17606,""leefloon_pct"":31.9,'
        '""litigation_dossiers"":3696,""litigation_cost_m"":3.0,'
        '""note"":""Strong CoA; waves match; GH pending; dual OCMW""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Limit long-term unemployment duration,Track leefloon displacement FOI,"
        "src_ccrek_fed_aju_unemp_rva_2026,strong,Federal>RVA>unemp_reform,tick509"
    ),
    (
        "cmt_rva_excl_waves_regional,Unemployment exclusion waves by region + leefloon inflow Q1 2026,"
        "sec_ss,Excluded jobseekers OCMW,"
        "CoA 2026_22 RVA+POD MI tables,"
        "2025-09-01,2026,2027,0,"
        '"{""total_n"":193904,""bru_n"":41709,""vl_n"":62676,""wal_n"":88566,""dg_n"":953,'
        '""q1_excl_n"":45592,""q1_leefloon_n"":17606,""pct_leefloon"":31.9,'
        '""pct_wal"":37.2,""pct_vl"":23.5,""pct_bru"":27.5,'
        '""note"":""Strong CoA provisional; 3-4m lag stabilise""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Map reform displacement to social assistance,Regional dual FOI,"
        "src_ccrek_fed_aju_unemp_rva_2026,strong,Federal>RVA>exclusion_waves,tick509"
    ),
    (
        "cmt_invalidity_multiyear_slip,Invalidity RTW multi-year savings slip + solidarity + responsabilisering,"
        "sec_ss,Invalids employers mutualities,"
        "CoA 2026_22 §4 RIZIV tables,"
        "2026-02-01,2026,2029,-333600000,"
        '"{""followup_slip_2026_m"":110.2,""cumul_miss_2029_m"":333.6,""solidarity_2026_m"":98.4,'
        '""respons_2026_m"":137.0,""doctors_risk_m"":50.0,""unemp_inflow_2026_m"":44.1,'
        '""exclusions_n"":4197,'
        '""note"":""Strong CoA; Sep2026 regulation risk; dual unemp reform""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Make RTW savings deliverable,FOI doctor law + exclusion counts,"
        "src_ccrek_fed_aju_unemp_rva_2026,strong,Federal>RIZIV>invalidity_multiyear,tick509"
    ),
    (
        "cmt_dual_unemp_leefloon,Dual unemp reform save path vs leefloon OCMW shift,"
        "gg_belgium,Unemployed OCMW clients,"
        "CoA 2026_22 residual dual,"
        "2026-05-21,2026,2029,1685200000,"
        '"{""reform_save_2026_m"":1685.2,""leefloon_q1_n"":17606,""leefloon_pct"":31.9,'
        '""ocmw_total_m"":2309,'
        '""note"":""not additive pure TE; dual social stack displacement""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Honest dual accounting reform vs safety net,Publish quarterly dual stats FOI,"
        "src_dual_unemp_leefloon_tick509,strong,BE>dual>unemp_leefloon,tick509"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_rva_reform_save_1_69bn,Unemployment reform save path 1.69bn 2026,federal,savings,Federal>RVA>unemp_reform,1685200000,1685200000,Strong CoA: duration limit+degressivity 1685.2m 2026 rising to 2447.8m 2029; dual leefloon,strong,src_ccrek_fed_aju_unemp_rva_2026,Unemployed,Limit long-term benefit duration,Large structural reform; GH litigation risk,5.0,9.0,6,6.9,Track displacement FOI,seed,,tick509",
    "lb_rva_excl_waves_194k,Unemployment exclusion waves 193904 persons,federal,ops,Federal>RVA>exclusion_waves,0,0,Strong CoA: 193904 planned; Q1 actual 45592 (93.4pct); dual regional,strong,src_ccrek_fed_aju_unemp_rva_2026,Excluded jobseekers,Reform phase-out long claims,Mass administrative reform,4.0,7.0,5,5.7,Quarterly publish FOI,seed,,tick509",
    "lb_leefloon_shift_32pct,Leefloon shift 31.9pct of Q1 excluded (17606),federal,ops,Federal>POD_MI>leefloon_from_unemp,0,0,Strong CoA: 17606 new leeflooners Q1; WAL 37.2 VL 23.5 BRU 27.5; dual reform save,strong,src_ccrek_fed_aju_unemp_rva_2026,OCMW clients,Safety-net displacement,Reform cost shift not pure save,6.5,7.5,5,6.75,Cash dual FOI,seed,,tick509",
    "lb_rva_litigation_3m,Unemp reform litigation extra cost ~3m,federal,ops,Federal>RVA>litigation,3000000,3000000,Medium CoA: 3696 dossiers Apr30; est 3m legal; not in BC; GH pending,medium,src_ccrek_fed_aju_unemp_rva_2026,Courts claimants,Legal challenge reform,Off-budget friction,5.5,4.5,4,5.15,Book litigation FOI,seed,,tick509",
    "lb_swt_close_path_65m,SWT close save path 64.8m 2029 (stock 166.8m 2025),federal,savings,Federal>RVA>SWT_close,64800000,166800000,Strong CoA: no new entries; 8502 bens 166.8m 2025; 2026 rush cost doubtful,strong,src_ccrek_fed_aju_unemp_rva_2026,Older dismissed workers,Phase out bridge unemployment,Stock fade multi-year,4.0,6.5,4,5.35,Verify rush FOI,seed,,tick509",
    "lb_invalidity_cumul_miss_334m,Invalidity multi-year save miss 334m to 2029,federal,savings,Federal>RIZIV>invalidity_cumul,333600000,333600000,Strong CoA: cumul miss 333.6m to 2029; follow-up slip 110m 2026; dual unemp,strong,src_ccrek_fed_aju_unemp_rva_2026,Invalids taxpayers,RTW soft saves multi-year,Classic soft package,6.5,8.0,5,6.95,Finish regulation FOI,seed,,tick509",
    "lb_responsabilisering_137m,RTW responsabilisering path 137m 2026,federal,savings,Federal>RIZIV>responsabilisering,137000000,398000000,Medium CoA: 137m 2026 path to 398m 2029; doctors 50m law incomplete,medium,src_ccrek_fed_aju_unemp_rva_2026,Mutualities workers doctors,RTW incentives,Partial soft save,5.5,7.0,5,6.15,Doctor law FOI,seed,,tick509",
    "lb_dual_unemp_leefloon,Dual unemp reform 1.69bn vs leefloon shift 32pct,multi,ops,BE>dual>unemp_leefloon,1685200000,1685200000,Strong dual CoA residual: reform save vs OCMW displacement,strong,src_dual_unemp_leefloon_tick509,Unemployed OCMW,Dual social stack map,Displacement risk,6.0,9.0,5,7.0,Honest dual cash FOI,seed,,tick509",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_rva_unemp_leefloon_l5,Federal>RVA_POD_MI>unemp_leefloon_L5,onem_rva,"
    "Quarterly cash dual: reform savings realized vs leefloon extra grants by region 2026-29; "
    "litigation cost series and Grondwettelijk Hof case status; SWT re-estimate vs rush hypothesis; "
    "family credit backpack law and revised cash; invalidity multi-year slip update after Sep2026,"
    "CoA 2026_22: strong reform aggregates; residual dual cash and litigation L5,7,"
    "RVA / POD MI / RIZIV,contact@rva.be,"
    ",docs/doge/foi/drafts/gap_rva_unemp_leefloon_l5.md,"
    "ready,2026-07-28,,,,,cmt_rva_unemp_reform_path,"
    "lb_rva_reform_save_1_69bn|lb_leefloon_shift_32pct|lb_dual_unemp_leefloon,"
    "2026-07-28T23:45:00Z,2026-07-28T23:45:00Z,"
    "tick509: CoA 2026_22 residual unemp/RVA dual leefloon; FOI L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_500,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-28T23:30:00Z,,Spawned tick508 after CoA SS/POD MI residual; progress@510 next tick; rq_116 deferred"
)
new = (
    "rq_500,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,"
    "gap_rva_unemp_leefloon_l5,"
    "2026-07-28T23:30:00Z,2026-07-28T23:45:00Z,"
    "tick509: CoA 2026_22 residual RVA unemp reform 1.69bn dual leefloon 32pct; FOI; progress@510 next; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_500 not found as expected")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_501,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-28T23:45:00Z,,Spawned tick509 after CoA RVA unemp residual; progress@510 next tick; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-28T23:45:00Z,rq_500,509,no,"
    "Tick509 CoA RVA unemp reform 1.69bn dual leefloon 32pct; next prio5 rq_501; progress@510 next; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick509 OK")

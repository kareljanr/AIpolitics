# tick513 — CoA 2026_22 residual defence multi-year financing + Fedasil save L5 dual fraud
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_fed_aju_defence_fedasil_l5_2026,CoA fed aju 2026 defence financing multi-year + Fedasil save L5 residual 2026_22,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Rekenhof AG 21 May 2026,2026-07-29,court_of_audit,"
        "Strong residual tick513: defence 17.336bn 2025-29; Russian assets path -942; asset optim 3.17bn unbooked; "
        "NATO effort 13.296/13.246; Fedasil save 110.8 vs 172 gap 61.2; SIOD 414.6; dual prior; tick513\n"
    )
    f.write(
        "src_dual_defence_fedasil_tick513,Dual defence financing opacity + Fedasil soft save path,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "DOGE synthesis CoA 2026_22 residual defence+Fedasil,2026-07-29,synthesis,"
        "Strong dual: defence asset optim 3.17bn unbooked + Fedasil 61m 2026 shortfall; tick513\n"
    )

buds = [
    # Defence multi-year financing
    "bud_defence_2025_29_17336m,mod_defensie,2029,17335800000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Defence spend path 2025-29 total 17335.8m (+552.8 for NATO 2pct via higher GDP); tick513",
    "bud_russian_assets_cit_2025_1148m,sec_federal,2025,1148000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Russian assets VenB 2025 1148m (was 1208; -60); tick513",
    "bud_russian_assets_cit_2026_1016m,sec_federal,2026,1016000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Russian assets VenB 1016m/yr 2026-29 path; tick513",
    "bud_russian_assets_path_shortfall_942m,sec_federal,2029,-942000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Russian assets CIT path shortfall -942m vs initial 6154m total 2025-29; residual 735m 2027-29 unaddressed; tick513",
    "bud_defence_higher_deficit_4804m,mod_defensie,2029,4804000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Defence plan higher deficit financing 4804m of which asset optim ~2/3 = 3170m; tick513",
    "bud_defence_asset_optim_3170m,sec_federal,2029,3170000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,medium,Asset optimisation 3170m path 40/30/20/10pct 2026-29 (1268/951/634/317); NOT booked 2026 conclaves; tick513",
    "bud_defence_asset_optim_2026_1268m,sec_federal,2026,1268000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,medium,Asset optim 40pct of 3170 = 1268m 2026 schedule; unbooked in conclaves; tick513",
    "bud_belfius_sale_20pct_2bn,sec_federal,2027,2000000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,medium,Belfius 20pct stake sale est 2bn after ECB/NBB/FSMA; likely 2027; tick513",
    "bud_defence_asset_optim_residual_1170m,sec_federal,2029,1170000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,weak,Residual asset optim after Belfius 2bn: 1170m unexplained to CoA; tick513",
    "bud_nato_effort_target_13296m_2026,mod_defensie,2026,13296000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,NATO 2pct effort target BC 13296m (GDP 664.8bn); IB was 13107; tick513",
    "bud_nato_effort_fill_13246m_2026,mod_defensie,2026,13246000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,NATO effort fill BC 13246m (def budget 10958 + external 2288); short vs target ~50m; tick513",
    "bud_defence_budget_10958m_2026,mod_defensie,2026,10958000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Defence section 16 budget BC 10958m (+188); tick513",
    "bud_defence_external_2288m_2026,mod_defensie,2026,2288000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,External defence effort BC 2288m (pens 1988 norm 168 COFOG 131+2); pens -40 vs IB; tick513",
    "bud_mil_pens_1988m_2026,mod_defensie,2026,1988000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Military pensions BC 1988m (FPD says up to -40m vs gov est); tick513",
    # Fedasil save L5
    "bud_fedasil_asylum_save_target_172m_2026,fedasil,2026,-172000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Asylum reception save target -172m 2026 (path -303/-452/-538 2027-29); tick513",
    "bud_fedasil_asylum_save_plan_1108m_2026,fedasil,2026,-110800000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Fedasil asylum save plan only -110.8m 2026 (gap -61.2 vs target); tick513",
    "bud_fedasil_cap_cut_2025_save_36m,fedasil,2026,-36400000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Capacity cut 2025 realized save -36.4m/yr (36478->34564 places); tick513",
    "bud_fedasil_cap_cut_2026_save_35m,fedasil,2026,-35300000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,medium,Capacity cut 2026 to ~30k places save -35.3m (from 2027 -93.9m/yr); tick513",
    "bud_fedasil_extra_save_39m_2026,fedasil,2026,-39100000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,medium,Extra save 23 measures -39.1m 2026 (internal 27.1 core tasks 10.4 procedure 1.6); from 2027 -220.7; tick513",
    "bud_fedasil_save_gap_61m_2026,fedasil,2026,61200000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Asylum save shortfall 61.2m 2026 (plan 110.8 vs target 172); 2029 gap 187; tick513",
    "bud_fedasil_return_save_75m_2026,fedasil,2026,-75000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,weak,Return efficiency save target -75m 2026 hard to track; deferred IB2027; dual POD MI medical; tick513",
    "bud_podmi_medical_100m_2026,sec_federal,2026,100300000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,POD MI medical aid BC 100.3m (-12 vs IB 112.3 volume-attributed; unit cost also down); tick513",
    # Fraud residual
    "bud_fiscal_fraud_claim_300m_2026,sec_federal,2026,300000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,weak,Fiscal fraud yield claim 300m 2026 / 600m 2029; method opaque CoA; tick513",
    "bud_financial_parket_yield_196m_2029,sec_federal,2029,196000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,weak,Financial parket yield claim 196m 2029; method opaque; bill DOC56 1536; tick513",
    "bud_siod_social_fraud_414m_2025,sec_ss,2025,414600000,,,outturn,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,SIOD social fraud yield 414.6m 2025 (-20.3 vs 2024); tick513",
    "bud_social_inspect_extra_staff_8m_2026,sec_ss,2026,8000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,medium,Social inspection +100 staff cost 8m/yr; hiring H2 so 2026 cost overstated; tick513",
    "bud_fraud_staff_bbi_150_vte,sec_federal,2026,150,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,medium,BBI extra 150 VTE planned; hiring not started CoA; amount_eur stores FTE count not euros — skip",
]
# Drop the bad FTE-as-euro row
buds = [b for b in buds if "bud_fraud_staff_bbi" not in b]
buds += [
    "bud_e1_deficit_path_362bn_2029,sec_federal,2029,36200000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Entity I deficit path 24.5bn 2026 to 36.2bn 2029 (-11.7bn worsen; was -6.6 initial); tick513",
    "bud_euroclear_russian_gt1bn_yr,sec_federal,2026,1000000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,medium,Euroclear frozen Russian assets exceptional receipt >1bn/yr assumed permanent to 2031; no intl deal assumed; tick513",
    "bud_fod_fin_personnel_drag_433m_2029,sec_federal,2029,433000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,medium,FOD Fin personnel-save drag on control yields 433m by 2029 not in toelichting; tick513",
    "bud_regions_eu_mfk_500m_2028,sec_federal,2028,500000000,,,budgeted,src_ccrek_fed_aju_defence_fedasil_l5_2026,weak,Regions EU MFK contribution 500m/yr from 2028 booked; no deal with entities; tick513",
    "bud_me_conflict_effort_cumul_67bn_2029,sec_federal,2029,6700000000,,,derived,src_ccrek_fed_aju_defence_fedasil_l5_2026,medium,ME conflict macro sensitivity cumulative efforts ~6.7bn to end-2029 (BOSA 15 Apr); tick513",
    "bud_dual_defence_fedasil_2026,gg_belgium,2026,1268000000,,,derived,src_dual_defence_fedasil_tick513,strong,Dual defence asset optim 1.27bn schedule + Fedasil save gap 61m; tick513",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_defence_financing_multi_year,Defence multi-year financing Russian assets + asset optim + Belfius,"
        "mod_defensie,Defence NATO Engie Belfius,"
        "CoA 2026_22 §3.2.2 defence plan 11 Apr 2025,"
        "2025-04-11,2025,2029,17335800000,"
        '"{""defence_2025_29_m"":17335.8,""russian_path_shortfall_m"":942,""residual_2027_29_m"":735,'
        '""higher_deficit_m"":4804,""asset_optim_m"":3170,""asset_2026_m"":1268,'
        '""belfius_sale_m"":2000,""asset_residual_m"":1170,""booked_conclave_2026"":false,'
        '""note"":""Strong CoA; asset optim unbooked; Belfius 2027 likely""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Honest defence financing,FOI asset list + Belfius terms,"
        "src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Federal>Defence>financing_path,tick513"
    ),
    (
        "cmt_nato_effort_2026_table,NATO 2pct effort target vs fill BC2026,"
        "mod_defensie,Defence,"
        "CoA 2026_22 §2.3.1,"
        "2026-05-21,2026,2026,13296000000,"
        '"{""gdp_m"":664778,""target_m"":13296,""fill_m"":13246,""def_budget_m"":10958,'
        '""external_m"":2288,""pens_m"":1988,""norm_m"":168,""cofog_m"":133,'
        '""note"":""Strong CoA; fill short ~50m vs 2pct target""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Meet NATO 2pct with honest fill,Reconcile pens FPD -40m,"
        "src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Federal>Defence>NATO_2026,tick513"
    ),
    (
        "cmt_fedasil_save_plan_l5,Fedasil asylum save plan L5 vs target multi-year,"
        "fedasil,Asylum seekers reception,"
        "CoA 2026_22 §2.2.1 Fedasil plan + BOSA spending review,"
        "2025-02-14,2026,2029,-110800000,"
        '"{""target_2026_m"":172,""plan_2026_m"":110.8,""gap_2026_m"":61.2,'
        '""cap2025_m"":36.4,""cap2026_m"":35.3,""extra_m"":39.1,'
        '""extra_internal_m"":27.1,""extra_core_m"":10.4,""extra_proc_m"":1.6,'
        '""plan_2027_m"":351,""target_2029_m"":538,""gap_2029_m"":187,'
        '""return_target_m"":75,""return_trackable"":false,'
        '""note"":""Strong CoA; law delay risk 2026 shortfall""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Deliverable asylum savings,FOI 23 measures list,"
        "src_ccrek_fed_aju_defence_fedasil_l5_2026,strong,Federal>Fedasil>save_plan_L5,tick513"
    ),
    (
        "cmt_dual_defence_fedasil_aju,Dual defence financing opacity + Fedasil soft saves,"
        "gg_belgium,Defence asylum taxpayers,"
        "CoA 2026_22 residual dual,"
        "2026-05-21,2026,2029,3170000000,"
        '"{""asset_optim_m"":3170,""fedasil_gap_2026_m"":61.2,""fraud_claim_m"":300,'
        '""note"":""not additive pure TE; dual soft financing + soft saves""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Honest dual soft paths,FOI asset+measure lists,"
        "src_dual_defence_fedasil_tick513,strong,BE>dual>defence_fedasil,tick513"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_defence_path_17_3bn,Defence spend path 17.3bn 2025-29,federal,ops,Federal>Defence>path_2025_29,0,17335800000,Strong CoA: 17335.8m multi-year (+552.8 NATO); annual=0 multi-year,strong,src_ccrek_fed_aju_defence_fedasil_l5_2026,Defence,NATO 2pct path,Multi-year envelope,3.0,9.5,6,6.55,Track yearly FOI,seed,,tick513",
    "lb_defence_asset_optim_3_17bn,Defence asset optim financing 3.17bn unbooked,federal,ops,Federal>Defence>asset_optim,1268000000,3170000000,Medium CoA: 3170m path 40/30/20/10; not in 2026 conclaves; residual 1170 after Belfius,medium,src_ccrek_fed_aju_defence_fedasil_l5_2026,Taxpayers,Asset sales for defence,Soft financing,7.5,9.0,6,7.85,Publish asset list FOI,seed,,tick513",
    "lb_belfius_sale_2bn,Belfius 20pct sale est 2bn ~2027,federal,ops,Federal>SFPIM>Belfius_sale,0,2000000000,Medium CoA: 2bn after ECB/NBB/FSMA; stock sale not annual TE,medium,src_ccrek_fed_aju_defence_fedasil_l5_2026,State SFPIM,Partial bank privatisation,One-shot financing,5.0,9.0,7,6.55,Approval path FOI,seed,,tick513",
    "lb_nato_effort_13_3bn_2026,NATO effort target 13.3bn fill 13.25bn 2026,federal,ops,Federal>Defence>NATO_effort_2026,13246000000,13296000000,Strong CoA: target 13296 fill 13246; def budget 10958,strong,src_ccrek_fed_aju_defence_fedasil_l5_2026,NATO,2pct GDP defence effort,Core security mass,2.5,9.5,6,6.45,Close 50m gap,seed,,tick513",
    "lb_fedasil_save_gap_61m,Fedasil asylum save gap 61m 2026,federal,savings,Federal>Fedasil>save_gap_2026,61200000,61200000,Strong CoA: plan 110.8 vs target 172; dual return 75 untracked,strong,src_ccrek_fed_aju_defence_fedasil_l5_2026,Asylum system,Reception savings,Soft save shortfall,7.0,5.5,5,6.35,Law+measure FOI,seed,,tick513",
    "lb_fedasil_extra_save_39m,Fedasil extra 23 measures save 39m 2026,federal,savings,Federal>Fedasil>extra_measures,39100000,220700000,Medium CoA: internal 27.1 core 10.4 proc 1.6; from 2027 220.7,medium,src_ccrek_fed_aju_defence_fedasil_l5_2026,Fedasil,Spending review follow-up,L5 measure package,5.5,5.5,5,5.55,Named L5 FOI,seed,,tick513",
    "lb_siod_fraud_415m_2025,SIOD social fraud yield 414.6m 2025,federal,ops,Federal>SIOD>fraud_yield_2025,414600000,414600000,Strong CoA: 414.6m (-20.3 vs 2024); dual fiscal fraud claims,strong,src_ccrek_fed_aju_defence_fedasil_l5_2026,Inspectors employers,Social fraud control,Realized yield,4.0,7.5,4,5.85,Staffing delay FOI,seed,,tick513",
    "lb_dual_defence_fedasil,Dual defence asset optim + Fedasil soft saves,multi,ops,BE>dual>defence_fedasil,1268000000,3170000000,Strong dual CoA residual soft financing+saves,strong,src_dual_defence_fedasil_tick513,Taxpayers,Dual soft paths map,Opacity dual,6.5,9.0,5,7.35,Honest booking FOI,seed,,tick513",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_defence_asset_optim_l5,Federal>Defence>asset_optim_Belfius_L5,mod_defensie,"
    "Named asset list and cash-by-year for 3.17bn asset optimisation path (40/30/20/10 2026-29); "
    "Belfius 20pct sale process status valuation and net proceeds; residual 1.17bn after Belfius; "
    "Russian assets CIT multi-year bridge for remaining 735m 2027-29; Fedasil 23 extra measures named L5 cash,"
    "CoA 2026_22: asset optim unbooked in 2026 conclaves; Belfius 2bn opaque; Fedasil gap 61m,8,"
    "FOD Financiën / SFPIM / Defensie / Fedasil,info@minfin.fed.be,"
    ",docs/doge/foi/drafts/gap_defence_asset_optim_l5.md,"
    "ready,2026-07-29,,,,,cmt_defence_financing_multi_year,"
    "lb_defence_asset_optim_3_17bn|lb_belfius_sale_2bn|lb_fedasil_save_gap_61m,"
    "2026-07-29T01:00:00Z,2026-07-29T01:00:00Z,"
    "tick513: CoA 2026_22 residual defence financing + Fedasil L5; FOI human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_504,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T00:40:00Z,,Spawned tick512 after CoA fiscal/nonfiscal residual; rq_116 deferred"
)
new = (
    "rq_504,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,"
    "gap_defence_asset_optim_l5,"
    "2026-07-29T00:40:00Z,2026-07-29T01:00:00Z,"
    "tick513: CoA 2026_22 residual defence asset optim 3.17bn + Fedasil save L5 dual; FOI; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_504 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_505,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-29T01:00:00Z,,Spawned tick513 after CoA defence/Fedasil residual; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T01:00:00Z,rq_504,513,no,"
    "Tick513 CoA defence asset optim 3.17bn Fedasil save L5 dual; next prio5 rq_505; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick513 OK")

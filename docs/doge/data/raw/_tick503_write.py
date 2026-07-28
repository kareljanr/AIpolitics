# tick503 — CoA 2026_22 federal budget adjustment 2026 Entity I dual E2
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_fed_budget_aju_2026,CoA commentaar aanpassing staatsbegroting 2026 2026_22,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Rekenhof algemene vergadering 21 May 2026,2026-07-28,court_of_audit,"
        "Strong: Entity I deficit 24.5bn aju (init 24.6); MR +615m; defence 17.3bn 2025-29; "
        "interest 12.3->17.5; energy ~2.6bn; fraud opacity; dual E2; tick503\n"
    )
    f.write(
        "src_dual_e1_aju_e2_tick503,Dual Entity I CoA aju 24.5bn vs Entity II aju maps,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "DOGE synthesis CoA fed aju + prior E2 dual,2026-07-28,synthesis,"
        "Strong dual: E1 24.5bn vs VL RR -4.0 WAL -2.02 FWB -1.75 DG -0.11 class; SWA 25 Mar; tick503\n"
    )

buds = [
    "bud_entity1_def_2026_coa_aju,sec_federal,2026,-24500000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,Entity I financing deficit 24.5bn after measures CoA aju2026 (init 24.6); tick503",
    "bud_entity1_mr_improve_615m,sec_federal,2026,615000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,MR 3 Apr 2026 improves saldo 615m (tech 517 + policy 98); tick503",
    "bud_entity1_vat_takeaway_cancel_475m,sec_federal,2026,-475000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,Cancel VAT rate changes takeaway/drinks/sport venues 475m revenue loss class; tick503",
    "bud_entity1_primary_def_2026_coa,sec_federal,2026,-12200000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,Primary deficit 12.2bn 2026 path to 18.7bn 2029 CoA; tick503",
    "bud_entity1_primary_def_2029_coa,sec_federal,2029,-18700000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,Primary deficit 18.7bn 2029 CoA multiyear; tick503",
    "bud_entity1_interest_2026_coa,sec_federal,2026,12300000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,Interest charges 12.3bn 2026 path 17.5bn 2029 CoA; tick503",
    "bud_entity1_interest_2029_coa,sec_federal,2029,17500000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,Interest 17.5bn 2029 CoA (+5.2bn vs 2026); tick503",
    "bud_defence_nato2pct_2025_29,sec_federal,2029,17335800000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,Defence outlays 2025-29 total 17335.8m (+552.8 for NATO 2pct GDP path); tick503",
    "bud_defence_higher_def_4_8bn,sec_federal,2029,4804000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,Higher deficit for defence 4804m of which asset optim 3170m (conclaves did not book 2026 share); tick503",
    "bud_belfius_sale_20pct_2bn,sec_federal,2027,2000000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,Belfius 20pct stake sale est 2bn likely 2027 after ECB/NBB/FSMA; tick503",
    "bud_russian_assets_cit_2025_29,sec_federal,2029,6154000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,CIT on frozen Russian assets 6154m path 2025-29 (init; 2025 -60m); temporary defence finance; tick503",
    "bud_fraud_fiscal_yield_2026,sec_federal,2026,300000000,,,budgeted,src_ccrek_fed_budget_aju_2026,medium,Fiscal fraud measures yield claim 300m 2026 / 600m 2029; CoA no method detail from FPS Finance; tick503",
    "bud_fraud_fiscal_yield_2029,sec_federal,2029,600000000,,,budgeted,src_ccrek_fed_budget_aju_2026,medium,Fiscal fraud structural yield claim 600m 2029 CoA opaque method; tick503",
    "bud_siod_social_fraud_2025,sec_ss,2025,414600000,,,outturn,src_ccrek_fed_budget_aju_2026,strong,SIOD social fraud recovery 414.6m 2025 (-20.3m vs 2024); tick503",
    "bud_centenindex_e1_2026,sec_federal,2026,24000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,Centenindex Entity I yield 24m 2026 (total yield 83m) FPB Apr path; tick503",
    "bud_centenindex_e1_2029,sec_federal,2029,363000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,Centenindex Entity I yield 363m 2029 (total 727m) FPB Apr; tick503",
    "bud_centenindex_total_2029,gg_belgium,2029,727000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,Centenindex total yield 727m 2029 (83/359/687/727 path); tick503",
    "bud_fed_energy_policy_2_6bn,sec_federal,2026,2600000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,Federal energy policy ~2.6bn (DG Energie 1.2bn + assignment funds CREG/Elia/NIRAS/Hedera 1.4bn); CoA opacity; tick503",
    "bud_fed_energy_dg_1_2bn,sec_federal,2026,1200000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,DG Energie FOD Economy credits ~1.2bn of energy policy stack; tick503",
    "bud_fed_energy_funds_1_4bn,sec_federal,2026,1400000000,,,budgeted,src_ccrek_fed_budget_aju_2026,strong,Assignment funds to CREG Elia NIRAS Hedera ~1.4bn energy; tick503",
    "bud_personnel_save_neg_fodfin_433m,sec_federal,2029,433000000,,,estimated,src_ccrek_fed_budget_aju_2026,medium,Negative impact personnel savings on FOD Finance controls 433m by 2029 not in toelichting; tick503",
    "bud_regions_eu_mfk_500m_2028,gg_belgium,2028,500000000,,,budgeted,src_ccrek_fed_budget_aju_2026,medium,Annual 500m from federated entities for EU MFF from 2028 no agreement yet; tick503",
    "bud_euroclear_exceptional_1bn_yr,sec_federal,2026,1000000000,,,budgeted,src_ccrek_fed_budget_aju_2026,medium,MC assumes >1bn/yr exceptional Euroclear Russian assets receipt through 2031 if no intl deal; tick503",
    "bud_dual_e1_24_5_e2_map,gg_belgium,2026,24500000000,,,derived,src_dual_e1_aju_e2_tick503,strong,Dual E1 CoA aju 24.5bn vs E2 quartet class not additive TE; tick503",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_fed_budget_aju_2026_e1,Federal Entity I budget adjustment 2026 CoA path,"
        "sec_federal,Federal+SS taxpayers,CoA 2026_22 + MC 23 Mar 2026,"
        "2026-05-21,2026,2029,24500000000,"
        '"{""def_2026_bn"":-24.5,""def_init_bn"":-24.6,""mr_improve_m"":615,'
        '""primary_2026_bn"":-12.2,""primary_2029_bn"":-18.7,'
        '""interest_2026_bn"":12.3,""interest_2029_bn"":17.5,'
        '""defence_2025_29_m"":17335.8,""energy_bn"":2.6,'
        '""note"":""Strong CoA; legislation delay risks unpriced; dual CM Jul path""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Entity I fiscal path under EU net primary,Price legislation delay; dual E2,"
        "src_ccrek_fed_budget_aju_2026,strong,Federal>Begroting>AJU2026,tick503"
    ),
    (
        "cmt_defence_nato2_finance_2025_29,Defence NATO 2pct path finance mix 2025-29,"
        "sec_federal,Defence + security,Defence plan 11 Apr 2025 + CoA aju,"
        "2025-04-11,2025,2029,17335800000,"
        '"{""total_m"":17335.8,""delta_gdp_m"":552.8,""higher_def_m"":4804,'
        '""asset_optim_m"":3170,""belfius_2bn"":true,""russian_cit_m"":6154,'
        '""note"":""Strong CoA; asset optim not booked in 2026 conclaves""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Meet NATO 2pct GDP path,Transparent asset sales FOI; dual LPM,"
        "src_ccrek_fed_budget_aju_2026,strong,Federal>Defence>NATO2,tick503"
    ),
    (
        "cmt_fed_energy_policy_2_6bn,Federal energy policy stack ~2.6bn opacity,"
        "sec_federal,Energy consumers taxpayers,CoA 2026_22 energy chapter,"
        "2026-05-21,2026,2026,2600000000,"
        '"{""total_bn"":2.6,""dg_energie_bn"":1.2,""assignment_funds_bn"":1.4,'
        '""recipients"":""CREG Elia NIRAS Hedera"",'
        '""note"":""Strong CoA: assignment funds hard to track; recommend section 32""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Federal energy objectives financing,Open fund-level L5 FOI,"
        "src_ccrek_fed_budget_aju_2026,strong,Federal>Energie>policy_stack,tick503"
    ),
    (
        "cmt_dual_e1_aju_e2_map,Dual Entity I CoA aju vs Entity II deficit maps,"
        "gg_belgium,All taxpayers,CoA fed aju + VL WAL FWB DG,"
        "2026-05-21,2026,2026,24500000000,"
        '"{""e1_bn"":-24.5,""vl_outturn_bn"":-3.98,""wal_aju_bn"":-2.02,'
        '""fwb_aju_bn"":-1.75,""dg_bn"":-0.11,'
        '""note"":""not additive TE; different metrics outturn vs aju""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Full GG dual fiscal map,SWA assent + comparable ledgers,"
        "src_dual_e1_aju_e2_tick503,strong,BE>dual>Entity1_Entity2_aju,tick503"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_entity1_def_24_5bn_aju2026,Entity I deficit 24.5bn federal budget aju 2026,federal,deficit,Federal>Entity1>aju_2026,24500000000,24500000000,Strong CoA: 24.5bn after measures (init 24.6); dual CM Jul path class,strong,src_ccrek_fed_budget_aju_2026,Entity I taxpayers,Federal+SS fiscal path,Core deficit mass; interest snowball,4.5,9.5,6,6.85,Deliver measures; dual E2,seed,,tick503",
    "lb_entity1_interest_12_3bn_2026,Entity I interest 12.3bn 2026 path 17.5bn 2029,federal,debt_service,Federal>Entity1>interest,12300000000,17500000000,Strong CoA: interest 12.3->17.5bn; primary 12.2->18.7; dual debt,strong,src_ccrek_fed_budget_aju_2026,Bond holders taxpayers,Service public debt,Snowball outside net primary criterion,5.5,9.5,6,7.25,Primary surplus path,seed,,tick503",
    "lb_defence_nato2_17_3bn,Defence 17.3bn 2025-29 NATO 2pct path,federal,programme,Federal>Defence>NATO2_2025_29,0,17335800000,Strong CoA: 17335.8m multi-year +552.8; higher def 4.8bn; annual0 multiyear envelope,strong,src_ccrek_fed_budget_aju_2026,NATO/security,Meet 2pct GDP,Finance mix opacity asset sales,4.0,9.5,6,6.7,FOI asset optim+Belfius,seed,,tick503",
    "lb_fed_energy_2_6bn,Federal energy policy ~2.6bn assignment-fund opacity,federal,programme,Federal>Energie>policy_2_6bn,2600000000,2600000000,Strong CoA: 1.2 DG Energie +1.4 funds CREG/Elia/NIRAS/Hedera; hard to track goals,strong,src_ccrek_fed_budget_aju_2026,Energy consumers,Energy objectives,Assignment fund opacity classic DOGE,6.5,9.0,5,7.4,Section 32 + L5 FOI,seed,,tick503",
    "lb_fraud_fiscal_claim_600m,Fiscal fraud yield claim 300-600m method opaque,federal,revenue,Federal>Fiscalite>fraude_claim,300000000,600000000,Medium CoA: 300m 2026 600m 2029 no method from FPS Finance; dual SIOD 414.6m,medium,src_ccrek_fed_budget_aju_2026,Taxpayers,Anti-fraud receipts,Unverified yield risk,7.0,5.5,5,6.25,Publish method FOI,seed,,tick503",
    "lb_centenindex_e1_path,Centenindex Entity I yield 24->363m 2026-29,federal,measure,Federal>Index>centenindex,24000000,363000000,Strong FPB via CoA: E1 24/128/277/363; total 83->727; legislation delay risk,strong,src_ccrek_fed_budget_aju_2026,Wage/benefit recipients,Index reform partial freeze,Soft delivery if law delayed,5.0,5.5,5,5.3,Track law enactment,seed,,tick503",
    "lb_dual_e1_e2_aju_map,Dual Entity I 24.5bn + Entity II aju maps,multi,deficit,BE>dual>Entity1_Entity2_2026,24500000000,32000000000,Strong dual CoA: E1 24.5 vs VL-4 WAL-2 FWB-1.75 DG-0.11 class not TE-additive,strong,src_dual_e1_aju_e2_tick503,All taxpayers,GG fiscal dual map,Scale dual federalism,4.0,9.5,5,6.85,SWA + control accounts,seed,,tick503",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_fed_energy_funds_l5,Federal>Energie>assignment_funds_L5,sec_federal,"
    "L5 cash-by-year 2024-2026 assignment funds to CREG Elia NIRAS Hedera + DG Energie programme "
    "split goals; method note for fiscal fraud 300/600m yields; Belfius sale terms if public,"
    "CoA 2026_22 energy stack 2.6bn opaque via assignment funds; fraud method missing,8,"
    "FOD Economie DG Energie / FOD Financiën / SPF BOSA,info@economie.fgov.be,"
    ",docs/doge/foi/drafts/gap_fed_energy_funds_l5.md,"
    "ready,2026-07-28,,,,,cmt_fed_energy_policy_2_6bn,"
    "lb_fed_energy_2_6bn|lb_fraud_fiscal_claim_600m,"
    "2026-07-28T21:50:00Z,2026-07-28T21:50:00Z,"
    "tick503: CoA 2026_22 primary fill; residual energy+fraud L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_494,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-28T21:30:00Z,,Spawned tick502 after CoA Toekomstverbond 6; rq_116 deferred"
)
new = (
    "rq_494,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_fed_energy_funds_l5,"
    "2026-07-28T21:30:00Z,2026-07-28T21:50:00Z,"
    "tick503: CoA 2026_22 fed aju E1 24.5bn energy 2.6bn dual E2; FOI; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_494 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_495,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-28T21:50:00Z,,Spawned tick503 after CoA fed budget aju 2026; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-28T21:50:00Z,rq_494,503,no,"
    "Tick503 CoA fed aju E1 24.5bn energy 2.6bn dual E2; next prio5 rq_495; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick503 OK")

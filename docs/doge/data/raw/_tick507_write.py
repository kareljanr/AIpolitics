# tick507 — CoA 2026_22 residual Justice/Fedasil/Defence L5 dual prior Fedasil/prison
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_fed_aju_justice_fedasil_2026,CoA fed budget aju 2026 Justice Fedasil Defence L5 2026_22,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Rekenhof AG 21 May 2026,2026-07-28,court_of_audit,"
        "Strong residual tick507: Justice 2925m + prison provis 259/50/44; MasterPlan IIIbis 80m; "
        "Fedasil 848.2; asylum save path; NATO 13.3bn; dual prior; tick507\n"
    )
    f.write(
        "src_dual_justice_fedasil_defence_tick507,Dual Justice prison + Fedasil save + NATO internal security,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "DOGE synthesis CoA 2026_22 residual + prior Fedasil/prison DBFM,2026-07-28,synthesis,"
        "Strong dual: prison places 1300 path + Fedasil cap cut 30k + defence internal 177m; tick507\n"
    )

buds = [
    "bud_justice_section_aju_2026,sec_federal,2026,2925000000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,FOD Justice section 2925m VAK/VEK aju2026 (+81m vs IB); tick507",
    "bud_prison_overcrowd_infra_prov_259m,sec_federal,2026,259000000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,ID provision prison overcrowding infra/ops 259m (settle 159m 2026 +100m 2027) for 1300 places by 2029; tick507",
    "bud_prison_overcrowd_short_50m,sec_federal,2026,50000000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,ID provision short-term prison overcrowding 50m/yr; tick507",
    "bud_justice_efficiency_prov_44m,sec_federal,2026,44000000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,ID provision Justice efficiency 44m (palaces 21.5 staff PI 15.1 detainee plan 2.3); tick507",
    "bud_security_return_prov_546m,sec_federal,2026,546000000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,ID provision security services+return policy 546m settle (+179 unused 2025); Justice/Interior/Police; tick507",
    "bud_masterplan_iiibis_80m,sec_federal,2026,80000000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,MasterPlan IIIbis prison overcrowding total 80m ex inflation MR 25 Feb 2026; tick507",
    "bud_fedasil_dot_bc_2026,fedasil,2026,743900000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,Fedasil dotation BC2026 743.9m (+41.7 vs IB 702.2) unavoidable reception; tick507",
    "bud_fedasil_id_prov_bc_2026,fedasil,2026,104300000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,Fedasil ID provision BC2026 104.3m (+4.3 index staff partners); tick507",
    "bud_fedasil_total_bc_2026,fedasil,2026,848200000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,Fedasil total dot+ID prov BC2026 848.2m; tick507",
    "bud_fedasil_save_target_2026,fedasil,2026,172000000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,Asylum reception savings target 172m 2026 (path 303/452/538 2027-29); tick507",
    "bud_fedasil_save_plan_2026,fedasil,2026,110800000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,Fedasil proposed savings 110.8m 2026 (gap -61.2 vs target); cap 36.4+35.3 + extra 39.1; tick507",
    "bud_fedasil_cap_places_start_2026,fedasil,2026,34564,,,outturn,src_ccrek_fed_aju_justice_fedasil_2026,strong,Reception capacity start 2026 34564 places (IB assumed 36478); not EUR; tick507",
    "bud_fedasil_cap_target_2026,fedasil,2026,30000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,Capacity target ~30000 places end path 2026 save 35.3m; tick507",
    "bud_fedasil_return_save_75m,fedasil,2026,75000000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,medium,Efficient return savings claim 75m 2026 removed from Fedasil dot calc; hard to track CoA; tick507",
    "bud_podmi_medical_bc_2026,sec_federal,2026,100300000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,POD MI medical help BC 100.3m (was 112.3 IB); -12m volume claim; tick507",
    "bud_defence_nato_effort_bc_2026,sec_federal,2026,13296000000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,NATO 2pct effort target BC 13296m (GDP 664.778bn); tick507",
    "bud_defence_budget_bc_2026,sec_federal,2026,10958000000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,Defence section 16 budget BC 10958m (+188 vs IB); tick507",
    "bud_defence_internal_sec_177m,sec_federal,2026,177000000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,Internal security from defence 5pct path 177m settle 2026 (+NATO trust 45m =222 class); opacity CoA; tick507",
    "bud_nato_trust_fund_45m,sec_federal,2026,45000000,,,budgeted,src_ccrek_fed_aju_justice_fedasil_2026,strong,NATO trust fund 45m in section 14 Foreign Affairs not section 16; tick507",
    "bud_dual_prison_fedasil_2026,gg_belgium,2026,1132200000,,,derived,src_dual_justice_fedasil_defence_tick507,strong,Dual prison provis+MP IIIbis class + Fedasil 848m not additive pure TE; tick507",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_justice_prison_provis_aju2026,Justice prison overcrowding provisions + MasterPlan IIIbis,"
        "sec_federal,Detainees Regie der Gebouwen Justice,"
        "CoA 2026_22 + MR MasterPlan IIIbis 25 Feb 2026,"
        "2026-02-25,2026,2029,433000000,"
        '"{""justice_section_m"":2925,""infra_prov_m"":259,""short_prov_m"":50,'
        '""efficiency_m"":44,""mp_iiibis_m"":80,""places_1300_by"":2029,'
        '""antwerp_open"":""2026-09"",""note"":""Strong CoA; specialty principle risk ID provis""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Reduce prison overcrowding add capacity,Trace provis to places FOI; dual DBFM,"
        "src_ccrek_fed_aju_justice_fedasil_2026,strong,Federal>Justice>prison_overcrowd,tick507"
    ),
    (
        "cmt_fedasil_bc_save_path_2026,Fedasil BC2026 dotation + asylum savings path,"
        "fedasil,Asylum seekers reception partners,"
        "CoA 2026_22 + Fedasil savings plan + MR 14 Feb 2025,"
        "2025-02-14,2026,2029,848200000,"
        '"{""dot_m"":743.9,""id_prov_m"":104.3,""total_m"":848.2,'
        '""save_target_2026_m"":172,""save_plan_2026_m"":110.8,""gap_m"":61.2,'
        '""cap_start"":34564,""cap_target"":30000,""path_target_m"":[172,303,452,538],'
        '""return_save_m"":75,'
        '""note"":""Strong CoA; law changes needed; dual prior Fedasil multi-year""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Reception capacity path + savings,Deliver 110.8 then close gap; FOI measures L5,"
        "src_ccrek_fed_aju_justice_fedasil_2026,strong,Federal>Fedasil>BC2026,tick507"
    ),
    (
        "cmt_defence_nato_bc_internal_sec,Defence NATO 2pct BC + internal security 177m,"
        "sec_federal,Defence Police Science,"
        "CoA 2026_22 defence chapter,"
        "2025-04-11,2026,2026,13296000000,"
        '"{""nato_effort_m"":13296,""defence_budget_m"":10958,""external_m"":2288,'
        '""internal_sec_m"":177,""nato_trust_m"":45,""gdp_bn"":664.778,'
        '""note"":""Strong CoA; mixed civil-military classification opacity""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Meet NATO 2pct and internal resilience,Norm military share FOI; dual LPM,"
        "src_ccrek_fed_aju_justice_fedasil_2026,strong,Federal>Defence>NATO_BC2026,tick507"
    ),
    (
        "cmt_dual_justice_fedasil_defence,Dual prison + Fedasil + defence internal security stack,"
        "gg_belgium,Public security asylum defence,"
        "CoA 2026_22 residual L5,"
        "2026-02-25,2026,2029,13296000000,"
        '"{""prison_class_m"":433,""fedasil_m"":848.2,""nato_m"":13296,'
        '""note"":""not additive TE; dual security/asylum/defence governance""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Map dual federal security spend,Comparable L5 FOI stack,"
        "src_dual_justice_fedasil_defence_tick507,strong,BE>dual>Security_asylum_defence,tick507"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_justice_2925m_aju2026,FOD Justice section 2.925bn aju 2026,federal,ops,Federal>Justice>section_2026,2925000000,2925000000,Strong CoA: 2925m +81m vs IB; ID provisions scatter specialty risk,strong,src_ccrek_fed_aju_justice_fedasil_2026,Justice system,Core justice budget,Core entitlement mass,2.5,9.5,5,6.4,Consolidate ID provis into Justice,seed,,tick507",
    "lb_prison_overcrowd_prov_359m,Prison overcrowding provisions 259+50+44+80 class,federal,programme,Federal>Justice>prison_overcrowd,353000000,433000000,Strong CoA: infra 259 short 50 efficiency 44 + MP IIIbis 80; 1300 places by 2029,strong,src_ccrek_fed_aju_justice_fedasil_2026,Detainees society,Cut overcrowding,Urgent capacity; dual DBFM,5.0,7.5,5,6.15,FOI places cash schedule,seed,,tick507",
    "lb_fedasil_848m_bc2026,Fedasil total 848.2m BC2026 dot+ID,federal,ops,Federal>Fedasil>BC2026,848200000,848200000,Strong CoA: dot 743.9 + ID 104.3; +46 vs IB total; dual save path,strong,src_ccrek_fed_aju_justice_fedasil_2026,Asylum seekers,Reception network,Core reception mass,3.0,7.5,5,5.4,Track save delivery FOI,seed,,tick507",
    "lb_fedasil_save_gap_61m,Fedasil asylum save plan gap 61m vs target 2026,federal,savings,Federal>Fedasil>save_gap_2026,61200000,61200000,Strong CoA: plan 110.8 vs target 172; law delays; path risk 2027+,strong,src_ccrek_fed_aju_justice_fedasil_2026,Taxpayers,Reception consolidation,Soft savings delivery,6.5,5.5,5,5.95,Publish measure outturn FOI,seed,,tick507",
    "lb_defence_nato_13_3bn_bc,NATO 2pct effort 13.3bn BC2026,federal,programme,Federal>Defence>NATO_BC2026,13296000000,13296000000,Strong CoA: target 13296m GDP 664.8bn; defence budget 10958; dual internal sec 177m,strong,src_ccrek_fed_aju_justice_fedasil_2026,NATO/security,2pct GDP path,Core defence mass,3.0,9.5,5,6.55,Clarify military share internal sec,seed,,tick507",
    "lb_defence_internal_sec_177m,Defence internal security credits 177m opacity,federal,programme,Federal>Defence>internal_security,177000000,222000000,Strong CoA: 177m + NATO trust 45m; mixed civil-military classification unclear,strong,src_ccrek_fed_aju_justice_fedasil_2026,Police Defence,Internal resilience,NATO labelling opacity DOGE,6.5,7.5,5,6.75,Norm COFOG/NATO share FOI,seed,,tick507",
    "lb_dual_prison_fedasil_defence,Dual prison + Fedasil 848m + NATO stack,multi,programme,BE>dual>Security_asylum_defence,848200000,13296000000,Strong dual CoA residual L5 security/asylum/defence,strong,src_dual_justice_fedasil_defence_tick507,Public,Federal security dual map,Scale dual not TE-additive,4.5,9.5,5,7.0,Comparable L5 FOI,seed,,tick507",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_fedasil_save_measures_l5,Federal>Fedasil>savings_plan_2026_29>measures_L5,fedasil,"
    "Named 23 additional savings measures cash-by-year 2026-29 (internal 27.1/53.5 core 10.4/32.8 "
    "procedure 1.6/134.5) + capacity place counts monthly; MasterPlan IIIbis 80m cash schedule by site; "
    "internal security 177m programme list military share,"
    "CoA 2026_22 aggregates strong; measure L5 and military classification residual,8,"
    "Fedasil / FOD Justitie / Ministerie Landsverdediging,info@fedasil.be,"
    ",docs/doge/foi/drafts/gap_fedasil_save_measures_l5.md,"
    "ready,2026-07-28,,,,,cmt_fedasil_bc_save_path_2026,"
    "lb_fedasil_save_gap_61m|lb_prison_overcrowd_prov_359m,"
    "2026-07-28T23:10:00Z,2026-07-28T23:10:00Z,"
    "tick507: CoA 2026_22 residual Justice/Fedasil/Defence; FOI L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_498,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-28T22:50:00Z,,Spawned tick506 after CoA BBI bank data; progress@510 soon; rq_116 deferred"
)
new = (
    "rq_498,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,"
    "gap_fedasil_save_measures_l5,"
    "2026-07-28T22:50:00Z,2026-07-28T23:10:00Z,"
    "tick507: CoA 2026_22 residual Justice/Fedasil/Defence L5 dual; FOI; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_498 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_499,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-28T23:10:00Z,,Spawned tick507 after CoA Justice/Fedasil residual; progress@510 next ticks; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-28T23:10:00Z,rq_498,507,no,"
    "Tick507 CoA Justice/Fedasil/Defence residual L5; next prio5 rq_499; progress@510 soon; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick507 OK")

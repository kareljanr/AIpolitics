from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
tick = 681
utc = "2026-08-01T12:00:00Z"
src = "src_ccrek_fed_aju2026_primary_cells_justice"
src_dual = "src_dual_primary_cells_tick681"
url = "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf"

src_rows = [
    f'{src},CoA federal BA2026 primary exp cells + Justice Fedasil residual dual,{url},Cour des comptes / Rekenhof,2026-08-01,audit,"Strong tick681: primary VEK cells total 92050 (+41): support 3722 (-497 index -485.2 ID -207.4 security +178.8 new policy +40.6); authority 23049 (+390 Def +188.2 Interior +100 of which Fedasil 41.6 Justice +81 of which personnel 39.5); economic 6580 (-34 Phoenix -50 energy +15 Mobility -12 BELSPO +8.6); social 34611 (+82 POD MI +60 Health +29.3); specific 24087 (+100 6th reform +61.5 debt +44 EU -59.4); Justice sect 2925 (+81); prison infra provis 259 (VEK 159+100 2027) 1300 places 2029; short-term 50/yr; efficiency 44 (palaces 21.5 staff 15.1 plan 2.3); security/return provis 546 +179 carry; detainee costs 112.5 (+6.2) pop 13447->13790; MasterPlan IIIbis 80; Fedasil dot 743.9 (+41.7) ID provis 104.3 total 848.2; save target 247 plan 110.8 (cap2025 36.4 cap2026 35.3 internal 39.1); capacity 36478 plan vs 34564 actual -> ~30k"',
    f'{src_dual},Dual fed primary cells Justice Fedasil vs VL Digisprong specialty dual,{url},DOGE synthesis CoA dual,2026-08-01,synthesis,"Strong dual: fed Justice specialty provisies vs VL Digisprong raid; Fedasil save slip dual migration; not TE-additive; tick681"',
]
with (data / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    for r in src_rows:
        f.write("\n" + r)

bud_rows = [
    # Cell matrix refresh residual
    f"bud_fed_primary_cells_total_92050m_ch_2026,sec_federal,2026,92050000000,,,budgeted,{src},strong,Primary settlement credits cells BC2026 92050m (+41 vs IB 92009); CoA T p35 residual tick681",
    f"bud_fed_cell_support_3722m_ch_2026,sec_federal,2026,3722000000,,,budgeted,{src},strong,Support cell 3722m (-497); index provis assign-out -485.2; ID provis -207.4; security provis +178.8; new policy +40.6; tick681",
    f"bud_fed_support_index_provis_out_485_2m_2026,sec_federal,2026,485200000,,,budgeted,{src},strong,Index provisie reassigned from support cell -485.2m to other FPS; tick681",
    f"bud_fed_support_id_provis_out_207_4m_2026,sec_federal,2026,207400000,,,budgeted,{src},strong,Interdepartmental provisies reassigned from support -207.4m; tick681",
    f"bud_fed_support_security_provis_up_178_8m_2026,sec_federal,2026,178800000,,,budgeted,{src},strong,Security provisie +178.8m in support cell (unused 2025 carry class); tick681",
    f"bud_fed_support_new_policy_provis_40_6m_2026,sec_federal,2026,40600000,,,budgeted,{src},strong,New-policy provisie +40.6m support cell; tick681",
    f"bud_fed_cell_authority_23049m_ch_2026,sec_federal,2026,23049000000,,,budgeted,{src},strong,Authority cell 23049m (+390); tick681",
    f"bud_fed_authority_defence_up_188_2m_2026,mod_defensie,2026,188200000,,,budgeted,{src},strong,Defence path +188.2m within authority cell aju; tick681",
    f"bud_fed_authority_interior_up_100m_2026,sec_federal,2026,100000000,,,budgeted,{src},strong,Interior +100m of which Fedasil 41.6; tick681",
    f"bud_fed_authority_justice_up_81m_2026,sec_federal,2026,81000000,,,budgeted,{src},strong,Justice +81m of which personnel 39.5; tick681",
    f"bud_fed_justice_personnel_up_39_5m_2026,sec_federal,2026,39500000,,,budgeted,{src},strong,Justice personnel credits +39.5m of +81 total; tick681",
    f"bud_fed_cell_economic_6580m_ch_2026,sec_federal,2026,6580000000,,,budgeted,{src},strong,Economic cell 6580m (-34); Phoenix -50 energy +15 Mobility -12 BELSPO +8.6; tick681",
    f"bud_fed_eco_phoenix_minus_50m_2026,sec_federal,2026,50000000,,,budgeted,{src},strong,Phoenix payment obligations path -50m in economic cell; tick681",
    f"bud_fed_eco_energy_support_up_15m_2026,sec_federal,2026,15000000,,,budgeted,{src},strong,Energy support measures +15m economic cell; tick681",
    f"bud_fed_eco_mobility_minus_12m_2026,sec_federal,2026,12000000,,,budgeted,{src},strong,FOD Mobility -12m economic cell; tick681",
    f"bud_fed_eco_belspo_up_8_6m_2026,sec_federal,2026,8600000,,,budgeted,{src},strong,POD BELSPO +8.6m economic cell; tick681",
    f"bud_fed_cell_social_34611m_ch_2026,sec_federal,2026,34611000000,,,budgeted,{src},strong,Social cell 34611m (+82); POD MI +60 Health +29.3; tick681",
    f"bud_fed_social_pod_mi_up_60m_2026,sec_federal,2026,60000000,,,budgeted,{src},strong,POD Maatschappelijke Integratie +60m social cell; tick681",
    f"bud_fed_social_health_up_29_3m_2026,sec_federal,2026,29300000,,,budgeted,{src},strong,FOD Volksgezondheid +29.3m social cell; tick681",
    f"bud_fed_cell_specific_24087m_ch_2026,sec_federal,2026,24087000000,,,budgeted,{src},strong,Specific sections 24087m (+100); 6th reform dots +61.5 debt ops +44 EU -59.4; tick681",
    f"bud_fed_specific_6th_reform_dots_up_61_5m_2026,sec_federal,2026,61500000,,,budgeted,{src},strong,6th state reform community dots +61.5m specific sections; tick681",
    f"bud_fed_specific_debt_ops_up_44m_2026,sec_federal,2026,44000000,,,budgeted,{src},strong,Debt operations +44m specific sections; tick681",
    f"bud_fed_specific_eu_contrib_minus_59_4m_2026,sec_federal,2026,59400000,,,budgeted,{src},strong,EU contribution -59.4m specific sections; tick681",
    # Justice residual
    f"bud_fed_justice_sect_2925m_2026,sec_federal,2026,2925000000,,,budgeted,{src},strong,FOD Justice section VAK=VEK 2925m (+81 vs IB); CoA 2.1; tick681",
    f"bud_fed_justice_prison_infra_provis_259m,sec_federal,2026,259000000,,,budgeted,{src},strong,ID provis prison overcrowding infra/ops 259m (VEK 2026 159 + 2027 100); 1300 places by 2029; specialty breach CoA; tick681",
    f"bud_fed_justice_prison_infra_vek_159m_2026,sec_federal,2026,159000000,,,budgeted,{src},strong,Prison infra provis VEK 2026 159m of 259 envelope; tick681",
    f"bud_fed_justice_prison_infra_vek_100m_2027,sec_federal,2027,100000000,,,budgeted,{src},strong,Prison infra provis VEK 2027 +100m of 259; tick681",
    f"bud_fed_justice_prison_short_term_50m_2026,sec_federal,2026,50000000,,,budgeted,{src},strong,Prison overcrowding short-term needs 50m/yr provis; tick681",
    f"bud_fed_justice_efficiency_provis_44m_2026,sec_federal,2026,44000000,,,budgeted,{src},strong,Justice efficiency-gains provis 44m (palaces 21.5 penitentiaire staff 15.1 detainees plan 2.3); tick681",
    f"bud_fed_justice_palaces_21_5m_2026,sec_federal,2026,21500000,,,budgeted,{src},strong,Justice palace maintenance/repair 21.5m of efficiency provis; tick681",
    f"bud_fed_justice_penitentiaire_staff_15_1m_2026,sec_federal,2026,15100000,,,budgeted,{src},strong,DG Penitentiaire Inrichtingen staff strengthen 15.1m; tick681",
    f"bud_fed_justice_detainees_plan_2_3m_2026,sec_federal,2026,2300000,,,budgeted,{src},strong,Detainees action plan 2.3m of efficiency provis; tick681",
    f"bud_fed_security_return_provis_546m_2026,sec_federal,2026,546000000,,,budgeted,{src},strong,ID provis security services + return policy 546m VEK (Justice/Interior/Fed Police); tick681",
    f"bud_fed_security_return_carry_179m_2026,sec_federal,2026,179000000,,,budgeted,{src},strong,Security/return provis +179m unused 2025 credits carried; tick681",
    f"bud_fed_detainee_costs_112_5m_2026,sec_federal,2026,112500000,,,budgeted,{src},strong,Detainee-related costs credits 112.5m (+6.2); pop basis 13447 Jan26 vs 13790 May (+2.5pct) underfund risk; tick681",
    f"bud_fed_masterplan_iiibis_80m,sec_federal,2026,80000000,,,budgeted,{src},strong,MasterPlan IIIbis prison overcrowding package 80m excl inflation (Antwerp open+keep Sint-Gillis Hoogstraten Bergen Verviers); MR 25 Feb 2026; tick681",
    f"bud_fed_prison_places_target_1300_2029,sec_federal,2029,1300,,,budgeted,{src},strong,Target +1300 prison places by 2029 via infra provis; unit places not EUR; tick681",
    # Fedasil residual
    f"bud_fedasil_dot_743_9m_2026,fedasil,2026,743900000,,,budgeted,{src},strong,Fedasil dotation prog 13.40.4 BC 743.9m (+41.7; unavoidable reception 41 + index/projects 0.7); tick681",
    f"bud_fedasil_id_provis_104_3m_2026,fedasil,2026,104300000,,,budgeted,{src},strong,Fedasil interdepartmental provis 104.3m (+4.3 index staff federal centres/partners); tick681",
    f"bud_fedasil_total_pack_848_2m_2026,fedasil,2026,848200000,,,budgeted,{src},strong,Fedasil dot+provis total 848.2m (+46 vs IB 802.2); tick681",
    f"bud_fedasil_save_target_247m_2026,fedasil,2026,247000000,,,budgeted,{src},strong,Gov save target 2026 247m (reception 172 + return 75) fully charged to Fedasil; tick681",
    f"bud_fedasil_save_plan_110_8m_2026,fedasil,2026,110800000,,,budgeted,{src},strong,Fedasil reception save plan 110.8m 2026 (below 172 target); gap 61.2; tick681",
    f"bud_fedasil_save_gap_61_2m_2026,fedasil,2026,61200000,,,budgeted,{src},strong,Fedasil reception save shortfall 61.2m (172-110.8) 2026; CoA; tick681",
    f"bud_fedasil_cap_save_2025_realized_36_4m,fedasil,2026,36400000,,,budgeted,{src},strong,Capacity cut realized 2025 annualized save 36.4m (plan 36478 vs actual start 34564 places); tick681",
    f"bud_fedasil_cap_save_2026_plan_35_3m,fedasil,2026,35300000,,,budgeted,{src},strong,Capacity cut 2026 to ~30k places save plan 35.3m; Ketenmonitoring; tick681",
    f"bud_fedasil_internal_save_39_1m_2026,fedasil,2026,39100000,,,budgeted,{src},strong,Internal ops/process save 39.1m 2026 (23 measures; BOSA spending review open centres); tick681",
    f"bud_fedasil_internal_ops_27_1m_2026,fedasil,2026,27100000,,,budgeted,{src},strong,Internal working improve 27.1m 2026 (path 53.5 from 2027); tick681",
    f"bud_fedasil_core_tasks_10_4m_2026,fedasil,2026,10400000,,,budgeted,{src},strong,Focus core tasks / stop usurping powers 10.4m 2026 (path 32.8 from 2027); tick681",
    f"bud_fedasil_procedure_chain_1_6m_2026,fedasil,2026,1600000,,,budgeted,{src},strong,Asylum procedure+chain improve 1.6m 2026 (path 134.5 from 2027!); tick681",
    f"bud_fedasil_cap_places_start_2026,fedasil,2026,34564,,,budgeted,{src},strong,Actual reception places start 2026 34564 (IB assumption 36478); tick681",
    f"bud_fedasil_cap_target_30k_2026,fedasil,2026,30000,,,budgeted,{src},strong,Capacity target ~30000 places end-path 2026; tick681",
    f"bud_fedasil_path_save_2027_cap_93_9m,fedasil,2027,93900000,,,budgeted,{src},strong,Further capacity cut save 93.9m/yr from 2027; tick681",
    f"bud_fedasil_path_internal_220_7m_2027,fedasil,2027,220700000,,,budgeted,{src},strong,Internal save pack path 220.7m from 2027; tick681",
    f"bud_fedasil_traj_save_688m_2029,fedasil,2029,688000000,,,budgeted,{src},strong,MR Feb2025 traj save 688m by 2029 (reception 538 + return 150); tick681",
    # Dual
    f"bud_dual_primary_cells_92bn_2026,gg_belgium,2026,92050000000,,,budgeted,{src_dual},strong,Dual fed primary cells 92.05bn residual vs VL BA VEK class; not TE-additive; tick681",
    f"bud_dual_fedasil_pack_848m_2026,gg_belgium,2026,848200000,,,budgeted,{src_dual},strong,Dual Fedasil 848.2m vs regional reception class; tick681",
]
with (data / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write("\n" + r)

cmt_rows = [
    f'cmt_fed_primary_cells_92050m,Federal primary exp cells 92.05bn residual,sec_federal,FPS cells,CoA 2026_22 p35,2026-05-21,2026,2026,92050000000,"{{""2026"":92050000000}}",,active,,Primary VEK dual,Cell L5 FOI,{src},strong,Fed>exp>cells,tick681',
    f'cmt_justice_prison_provis_stack,Justice prison provisies infra 259+50+44 specialty,sec_federal,FOD Justice+Regie,CoA 2026_22 2.1.1,2026-05-21,2026,2029,353000000,"{{""infra"":259000000,""short"":50000000,""efficiency"":44000000}}",,active,,Overcrowding dual,Specialty breach FOI,{src},strong,Fed>Justice>prison,tick681',
    f'cmt_masterplan_iiibis_80m,MasterPlan IIIbis prisons 80m,sec_federal,Prison estate,MR 25 Feb 2026,2026-02-25,2026,2029,80000000,"{{""2026_class"":80000000}}",,active,,Capacity dual,Project L5 FOI,{src},strong,Fed>Justice>masterplan,tick681',
    f'cmt_fedasil_pack_848m,Fedasil dot+provis 848.2m save slip,fedasil,Asylum reception,CoA 2026_22 2.2,2026-05-21,2026,2029,848200000,"{{""dot"":743900000,""provis"":104300000}}",,active,,Reception dual,Save gap FOI,{src},strong,Fed>Fedasil>pack,tick681',
    f'cmt_fedasil_save_gap_61m,Fedasil reception save gap 61.2m 2026,fedasil,Asylum capacity,CoA 2026_22,2026-05-21,2026,2026,61200000,"{{""target"":172000000,""plan"":110800000}}",,active,,Soft save dual,Capacity monitor,{src},strong,Fed>Fedasil>save,tick681',
    f'cmt_dual_primary_cells_tick681,Dual primary cells Justice Fedasil vs VL specialty,gg_belgium,Fed+VL dual,CoA dual,2026-05-21,2026,2026,92050000000,"{{""2026"":92050000000}}",,active,,Dual residual,Not TE-additive,{src_dual},strong,Belgium>dual>cells,tick681',
]
with (data / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write("\n" + r)

lb_rows = [
    f"lb_fed_primary_cells_92bn_2026,Federal primary exp cells 92.05bn,Federal,ops,Fed>exp>cells,92050000000,0,Strong CoA BC92050 (+41); support -497 authority +390 dual,strong,{src},taxpayers,Primary VEK,Primary,5.0,9.5,3,6.70,Cell L5 FOI,open,,tick681",
    f"lb_justice_prison_provis_specialty_2026,Justice prison provis specialty stack,Federal,ops,Fed>Justice>provis,353000000,0,Strong CoA: infra 259+short 50+eff 44 off Justice section specialty breach,strong,{src},detainees,Overcrowding dual,Primary absurd,8.0,6.5,3,7.05,Move to Justice FOI,open,,tick681",
    f"lb_masterplan_iiibis_80m_2026,MasterPlan IIIbis prisons 80m,Federal,ops,Fed>Justice>masterplan,80000000,0,Strong CoA MR Feb2026 80m excl inflation Antwerp/Sint-Gillis/Bergen,strong,{src},prison estate,Capacity,Primary,6.5,5.5,3,5.85,Project cash FOI,open,,tick681",
    f"lb_fedasil_save_gap_61m_2026,Fedasil save gap 61.2m vs 172 target,Federal,ops,Fed>Fedasil>save,61200000,0,Strong CoA plan 110.8 of 172 reception; capacity+internal pack,strong,{src},asylum seekers,Soft save dual,Primary,7.5,5.5,3,6.45,Capacity monitor FOI,open,,tick681",
    f"lb_fedasil_pack_848m_2026,Fedasil pack 848.2m (+46),Federal,ops,Fed>Fedasil>pack,848200000,0,Strong CoA dot 743.9+provis 104.3; dual migration,strong,{src},asylum system,Reception dual,Primary,6.0,7.0,3,6.35,Unit cost FOI,open,,tick681",
    f"lb_dual_primary_cells_2026,Dual primary cells 92bn vs VL specialty,Belgium,ops,Belgium>dual>cells,92050000000,0,Strong dual: fed cells+Justice provis vs VL Digisprong/buffer; not TE-additive,strong,{src_dual},all entities,Cells dual residual,Primary dual,6.0,9.5,3,7.20,Cross FOI,open,,tick681",
]
with (data / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write("\n" + r)

gap_id = "gap_fed_aju2026_primary_cells_justice_l5"
foi_row = (
    f"{gap_id},Federal>Aju2026>Primary_cells_Justice_Fedasil_L5,sec_federal,"
    "Primary cell L5 line list support/authority/economic/social/specific; Justice ID provisies 259/50/44/546 cash path to 2029 and specialty transfer calendar; MasterPlan IIIbis project cash 80m; detainee cost volume update post May pop; Fedasil save plan measure list 23 items + capacity series 36478/34564/30k; return save 75m design,"
    "CoA primary cells Justice Fedasil residual strong tick681; dual specialty,"
    "5,FOD BOSA / FOD Justitie / FOD Binnenlandse Zaken / Fedasil,"
    "openbaarheid@bosa.be,https://bosa.belgium.be,"
    f"docs/doge/foi/drafts/{gap_id}.md,ready,2026-08-01,,,,,"
    "cmt_fed_primary_cells_92050m|cmt_justice_prison_provis_stack|cmt_fedasil_pack_848m,"
    "lb_fed_primary_cells_92bn_2026|lb_justice_prison_provis_specialty_2026|lb_fedasil_save_gap_61m_2026,"
    f"{utc},{utc},tick681 CoA fed primary cells primary; human send only"
)
with (data / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + foi_row)

rq = data / "research_queue.csv"
lines = rq.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_672,"):
        out.append(
            "rq_672,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Next residual after progress@680: SS other receipts L5 CoA or fed primary exp cells residual or VL GIP/Lantis FOI-adjacent deepen.,,"
            f"2026-08-01T11:45:00Z,{utc},"
            "tick681 primary cells 92.05bn Justice prison provis Fedasil 848 save gap dual; FOI gap_fed_aju2026_primary_cells_justice_l5 ready"
        )
    else:
        out.append(line)
out.append(
    "rq_673,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,sec_federal,"
    "Next residual: VL GIP/Lantis FOI-adjacent deepen CoA 2026_28 or SS other receipts L5 or fed defence residual dual.,,"
    f"{utc},,spawned tick681 after rq_672"
)
rq.write_text("\n".join(out) + "\n", encoding="utf-8")

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_672,681,no,"
    "tick681 primary cells 92.05bn Justice provis Fedasil 848 save gap 61 dual; next rq_673; progress@690 in 9; rq_116 deferred\n",
    encoding="utf-8",
)

draft = f"""# FOI draft — {gap_id}

**gap_id:** `{gap_id}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Rekenhof Commentaar aanpassing staatsbegroting 2026 (2026_22) Deel II Ch II §1–2

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: FOD BOSA / FOD Justitie / FOD Binnenlandse Zaken / Fedasil
openbaarheid@bosa.be

Betreft: Openbaarheid — aju 2026 primaire uitgavencellen (92,05 mld) +
Justitie/Fedasil L5

Geachte,

Op grond van de wet van 11 april 1994 verzoek ik om:

1. **Vereffeningskredieten per cel** (ondersteuning / gezag / economisch /
   sociaal / specifieke secties): detailartikelen achter BC **92.050 mEUR**
   en de mutaties indexprovisie (−485,2), ID-provisies (−207,4),
   veiligheidsprovisie (+178,8), nieuw beleid (+40,6).
2. **Justitie – interdepartementale provisies** (art. 06.90.10.01.00.01 en
   .10): cashpad 2026–2029 voor overbevolking infra **259 mEUR**
   (VEK 159+100), korte termijn **50 mEUR/j**, efficiëntie **44 mEUR**,
   veiligheid/terugkeer **546+179 mEUR**; kalender overheveling naar
   sectie Justitie (specialiteit).
3. **MasterPlan IIIbis**: projectbegroting **80 mEUR** per site
   (Antwerpen, Sint-Gillis, Hoogstraten, Bergen, Verviers).
4. **Gedetineerdenkosten 112,5 mEUR**: herrekening op populatie
   **13.790** (4 mei 2026) vs basis **13.447**.
5. **Fedasil**: detail dotatie **743,9** + provisie **104,3**;
   besparingsplan 23 maatregelen achter **110,8 mEUR** (vs doel **172**);
   reeks opvangplaatsen **36.478 / 34.564 / ~30.000**; terugkeerbesparing
   **75 mEUR** ontwerp.

Publieke steun: Rekenhof, *Commentaar … staatsbegroting 2026* (2026_22),
Deel II, Hoofdstuk II Uitgaven.

Met vriendelijke groeten,
[Naam — menselijke afzender]
```

## Notes

- Do **not** send as agent; human only.
- Dual: VL Digisprong/buffer specialty; migration dual regional.
- Tick 681.
"""
(root / "docs/doge/foi/drafts" / f"{gap_id}.md").write_text(draft, encoding="utf-8")

entry = f"""
### {utc} — tick {tick}
- Unit: **rq_672** (FOI-adjacent dual residual — **fed CoA primary exp cells + Justice/Fedasil L5 dual**)
- Found (primary CoA 2026_22 Deel II Ch II):
  - **Primary cells VEK EUR92.050bn** (+41): support **3.722** (−497: index **−485.2** ID **−207.4** security **+178.8** new pol **+40.6**) · authority **23.049** (+390: Def **+188.2** Interior **+100** Justice **+81**) · economic **6.580** (−34: Phoenix **−50** energy **+15**) · social **34.611** (+82: POD MI **+60** Health **+29.3**) · specific **24.087** (+100: 6th reform **+61.5** debt **+44** EU **−59.4**)
  - **Justice 2.925bn** (+81); prison infra provis **259** (159+100) for **1300** places 2029; short-term **50**/yr; efficiency **44**; security/return **546+179** carry; specialty breach CoA; detainee costs **112.5** pop **13.4k→13.8k**; MasterPlan IIIbis **80**
  - **Fedasil** total **848.2** (dot **743.9** + provis **104.3**); save target **247** plan reception **110.8** gap **61.2**; capacity **36.5k→34.6k→~30k**; internal **39.1** (ops **27.1** core **10.4** procedure **1.6**)
  - Dual VL specialty/Digisprong. Strong CoA; L5 FOI.
- Wrote: budgets (+55); commitments (+6); leaderboard (+6); sources (+2); FOI draft **gap_fed_aju2026_primary_cells_justice_l5**; rq_672=done; spawn **rq_673**; loop_state ticks=681
- FOI opened: gap_fed_aju2026_primary_cells_justice_l5 — ready (not sent)
- Next: rq_673; progress@690 in 9 ticks; rq_116 deferred
"""
with (root / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(entry)

print("OK tick681")
print("budgets", len(bud_rows), "cmt", len(cmt_rows), "lb", len(lb_rows))

from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
tick = 683
utc = "2026-08-01T12:30:00Z"
src = "src_ccrek_fed_aju2026_defence_residual"
src_dual = "src_dual_defence_tick683"
url = "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf"

src_rows = [
    f'{src},CoA federal BA2026 defence multi-year NATO residual dual,{url},Cour des comptes / Rekenhof,2026-08-01,audit,"Strong tick683: defence exp 2025-29 17335.8 (+552.8 GDP); 2026 sect16 +188.2; temp finance Russian assets CIT path -942 (2025 1148 not 1208; 2026-29 1016/yr; residual 735 need measures 2027-29); structural normering; higher deficit 4804 of which asset optim 3170 (2026 40pct=1268 not booked conclave; Belfius 20pct sale est 2bn likely 2027; residual gap 1170); NATO 2pct target 13296 (GDP 664778); fill budget 10958 + external 2288 (pens 1988 -40 FPD; norm 168; COFOG 131) = 13246 gap ~50; internal security 177 sect16 + NATO trust 45 FA = 222; specialty mixed police helo BELSPO plane C-UAS BSC; FIPA patrols no reimburse; Euroclear >1bn/yr to 2031 assumption; FOD Fin drag 433 to 2029; Entity II EU MFF 500/yr from 2028 no deal"',
    f'{src_dual},Dual fed defence NATO financing vs Entity II ratings dual,{url},DOGE synthesis CoA dual,2026-08-01,synthesis,"Strong dual: fed NATO 13.3bn effort + asset optim opacity vs VL/WAL/FWB Moody dual debt; not TE-additive; tick683"',
]
with (data / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    for r in src_rows:
        f.write("\n" + r)

bud_rows = [
    # Multi-year envelope
    f"bud_def_exp_2025_29_17335_8m,mod_defensie,2025,17335800000,,,budgeted,{src},strong,Defence exp envelope 2025-2029 17335.8m (+552.8 GDP path) for NATO 2pct; CoA 3.2.2; tick683",
    f"bud_def_exp_path_up_552_8m_2025_29,mod_defensie,2026,552800000,,,budgeted,{src},strong,Defence multi-year uplift +552.8m from FPB Feb2026 GDP vs prior; tick683",
    f"bud_def_sect16_up_188_2m_2026,mod_defensie,2026,188200000,,,budgeted,{src},strong,Section 16 Landsverdediging +188.2m volume aju2026 bilateral; tick683",
    # Temporary financing Russian assets CIT
    f"bud_def_russian_assets_cit_2025_1148m,sec_federal,2025,1148000000,,,budgeted,{src},strong,Corp tax on frozen Russian assets profit 2025 AT 1148m (IB 1208; -60); temporary defence finance; tick683",
    f"bud_def_russian_assets_cit_2026_1016m,sec_federal,2026,1016000000,,,budgeted,{src},strong,Russian assets CIT path 1016m/yr 2026-2029 (was rising to 1297); tick683",
    f"bud_def_russian_assets_cit_2027_1016m,sec_federal,2027,1016000000,,,budgeted,{src},strong,Russian assets CIT 1016m 2027 path; tick683",
    f"bud_def_russian_assets_cit_2028_1016m,sec_federal,2028,1016000000,,,budgeted,{src},strong,Russian assets CIT 1016m 2028 path; tick683",
    f"bud_def_russian_assets_cit_2029_1016m,sec_federal,2029,1016000000,,,budgeted,{src},strong,Russian assets CIT 1016m 2029 path; tick683",
    f"bud_def_russian_assets_cit_shortfall_942m_2025_29,sec_federal,2026,942000000,,,budgeted,{src},strong,Russian assets CIT less-receipt 942m over 2025-2029 vs IB path total 6154; tick683",
    f"bud_def_russian_assets_residual_measures_735m_2027_29,sec_federal,2027,735000000,,,budgeted,{src},strong,Residual 735m 2027-2029 Russian CIT gap still needs government measures (to-2026 already booked); tick683",
    f"bud_def_russian_assets_cit_ib_path_6154m,sec_federal,2025,6154000000,,,budgeted,{src},strong,IB path Russian assets CIT total 6154m 2025-2029 (2025 1208 to 2029 1297); tick683",
    # Asset optim / higher deficit / Belfius
    f"bud_def_higher_deficit_4804m_2025_29,sec_federal,2025,4804000000,,,budgeted,{src},strong,MR 11 Apr 2025 higher deficit for defence 4804m of which ~2/3 asset optim; tick683",
    f"bud_def_asset_optim_3170m_2025_29,sec_federal,2025,3170000000,,,budgeted,{src},strong,Asset optimisation compensation 3170m of 4804 higher deficit; CoA: not booked 2026 conclaves; tick683",
    f"bud_def_asset_optim_2026_1268m,sec_federal,2026,1268000000,,,budgeted,{src},strong,Asset optim path 2026 40pct of 3170 = 1268m (MonCom Mar2026); NOT in budget conclaves; tick683",
    f"bud_def_asset_optim_2027_951m,sec_federal,2027,951000000,,,budgeted,{src},medium,Asset optim path 2027 30pct of 3170 = 951m class; tick683",
    f"bud_def_asset_optim_2028_634m,sec_federal,2028,634000000,,,budgeted,{src},medium,Asset optim path 2028 20pct of 3170 = 634m class; tick683",
    f"bud_def_asset_optim_2029_317m,sec_federal,2029,317000000,,,budgeted,{src},medium,Asset optim path 2029 10pct of 3170 = 317m class; tick683",
    f"bud_belfius_sale_20pct_est_2bn,sfpim,2027,2000000000,,,estimate,{src},medium,20pct Belfius participation sale est 2bn after ECB/NBB/FSMA (likely 2027); part of asset optim; tick683",
    f"bud_def_asset_optim_residual_gap_1170m,sec_federal,2026,1170000000,,,budgeted,{src},strong,Asset optim residual gap 1170m after Belfius 2bn class; CoA no further info; tick683",
    # NATO 2% table
    f"bud_gdp_bc_664778m_2026,gg_belgium,2026,664778000000,,,budgeted,{src},strong,GDP BC2026 664778m (IB 655357; +9421); tick683",
    f"bud_nato_2pct_target_13296m_2026,mod_defensie,2026,13296000000,,,budgeted,{src},strong,NATO 2pct target expenditure 13296m 2026 (+188); tick683",
    f"bud_nato_2pct_target_ib_13107m_2026,mod_defensie,2026,13107000000,,,budgeted,{src},strong,NATO 2pct IB target 13107m 2026; tick683",
    f"bud_def_budget_sect16_10958m_2026,mod_defensie,2026,10958000000,,,budgeted,{src},strong,Defence budget sect16 10958m (+188); tick683",
    f"bud_def_external_effort_2288m_2026,mod_defensie,2026,2288000000,,,budgeted,{src},strong,External defence effort 2288m (-40): pensions+normering+COFOG; tick683",
    f"bud_def_military_pensions_1988m_2026,fpd_pensioenen,2026,1988000000,,,budgeted,{src},strong,Military pensions FPD 1988m (gov ram lower by up to 40 vs prior); tick683",
    f"bud_def_normering_168m_2026,sec_federal,2026,168000000,,,budgeted,{src},strong,Normering other-dept spend counted as defence 168m 2026; tick683",
    f"bud_def_cofog02_other_depts_131m_2026,sec_federal,2026,131000000,,,budgeted,{src},strong,COFOG 02 other departments 131m; tick683",
    f"bud_def_partial_cofog_2m_2026,sec_federal,2026,2000000,,,budgeted,{src},strong,Partial COFOG 02 (Von Karman Belgica ID provis UNISONO) 2m; tick683",
    f"bud_def_total_effort_b_13246m_2026,mod_defensie,2026,13246000000,,,budgeted,{src},strong,Total defence effort fill B 13246m (+148) vs NATO target A 13296; gap ~50m; tick683",
    f"bud_def_nato_fill_gap_50m_2026,mod_defensie,2026,50000000,,,estimate,{src},medium,NATO fill gap target 13296 - effort 13246 ~50m class; tick683",
    # Internal security
    f"bud_def_internal_security_177m_2026,mod_defensie,2026,177000000,,,budgeted,{src},strong,Internal security/resilience from sect16 VEK 177m 2026 (5pct of additional defence if NATO-classifiable); tick683",
    f"bud_def_nato_trust_fund_45m_2026,sec_federal,2026,45000000,,,budgeted,{src},strong,NATO trust fund 45m in Foreign Affairs sect14 (not sect16 as initially planned); tick683",
    f"bud_def_internal_security_pack_222m_2026,mod_defensie,2026,222000000,,,budgeted,{src},strong,Internal security pack 222m if trust fund 45 included with 177; tick683",
    f"bud_def_fipa_patrols_no_reimburse_2026,mod_defensie,2026,0,,,budgeted,{src},medium,Defence support Fed Police mixed rail patrols + FIPA Brussels charged to internal security without Police reimbursement (law 1998); amount in 177 pack; tick683",
    # Related macro assumptions residual
    f"bud_euroclear_russian_assets_gt1bn_yr_to_2031,sec_federal,2026,1000000000,,,estimate,{src},medium,MonCom assumes no intl agreement before 2031 on frozen Russian assets Euroclear → permanent exceptional receipt >1bn/yr; tick683",
    f"bud_fod_fin_control_drag_433m_to_2029,sec_federal,2029,433000000,,,budgeted,{src},strong,FOD Fin alone negative impact 433m to 2029 from personnel save measures on control yield; not in algemene toelichting; tick683",
    f"bud_entity2_eu_mff_contrib_500m_yr_2028,sec_federal,2028,500000000,,,budgeted,{src},medium,Entity II annual 500m from 2028 for new EU MFF financing; no agreement with entities yet; tick683",
    f"bud_eu_mff_2028_34_envelope_2000bn,gg_belgium,2028,2000000000000,,,commitment,{src},strong,EU MFF 2028-2034 Commission envelope 2000bn (was 1216 in 2021-27); extra 784bn from own resources plan not MS contrib raise; tick683",
    # Fraud residual note (adjacent multi-year financing credibility)
    f"bud_fiscal_fraud_yield_300m_2026,sec_federal,2026,300000000,,,budgeted,{src},medium,Fiscal fraud yield claim 300m 2026 path 600 2029; CoA no method from FOD Fin; tick683",
    f"bud_social_fraud_yield_300m_2026,sec_federal,2026,300000000,,,budgeted,{src},medium,Social fraud yield claim 300m 2026 path 375/450/600; no measure split; tick683",
    f"bud_fiscal_fraud_path_600m_2029,sec_federal,2029,600000000,,,budgeted,{src},medium,Fiscal fraud path 600m 2029; tick683",
    f"bud_social_fraud_path_600m_2029,sec_federal,2029,600000000,,,budgeted,{src},medium,Social fraud path 600m 2029; tick683",
    # Dual
    f"bud_dual_nato_effort_13_25bn_2026,gg_belgium,2026,13246000000,,,budgeted,{src_dual},strong,Dual NATO effort fill 13.25bn vs Entity II debt ratings dual; not TE-additive; tick683",
    f"bud_dual_asset_optim_opacity_3_17bn,gg_belgium,2026,3170000000,,,budgeted,{src_dual},strong,Dual asset optim 3.17bn unbooked opacity class; tick683",
]
with (data / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write("\n" + r)

cmt_rows = [
    f'cmt_def_envelope_17336m,Defence exp 2025-29 17.34bn NATO path,mod_defensie,NATO 2pct,MR 11 Apr 2025 + CoA aju,2025-04-11,2025,2029,17335800000,"{{""2025_29"":17335800000}}",,active,,NATO dual,Financing FOI,{src},strong,Fed>Defence>envelope,tick683',
    f'cmt_def_asset_optim_3170m,Asset optim 3.17bn unbooked defence finance,sec_federal,State assets Belfius,MR Apr2025 + MonCom Mar2026,2025-04-11,2026,2029,3170000000,"{{""2026"":1268000000,""belfius"":2000000000}}",,active,,Higher deficit dual,Book or cut FOI,{src},strong,Fed>Defence>asset_optim,tick683',
    f'cmt_russian_assets_cit_path,Russian assets CIT path -942m vs IB,sec_federal,Euroclear profits,CoA 2026_22 3.2.2,2026-05-21,2025,2029,5212000000,"{{""2025"":1148000000,""2026_29_yr"":1016000000}}",,active,,Temp defence finance,Measures 735 FOI,{src},strong,Fed>Defence>russian_cit,tick683',
    f'cmt_nato_effort_13246m_2026,NATO effort fill 13.25bn vs target 13.30,mod_defensie,Belgium NATO,CoA 2026_22 2.3.1,2026-05-21,2026,2026,13246000000,"{{""target"":13296000000,""fill"":13246000000}}",,active,,2pct dual,Gap 50 FOI,{src},strong,Fed>Defence>NATO,tick683',
    f'cmt_internal_security_222m,Internal security pack 177+45 trust,mod_defensie,Police/FA/Defence,MR Apr+Jul2025 conclave Dec2025,2025-04-11,2026,2026,222000000,"{{""sect16"":177000000,""trust"":45000000}}",,active,,Specialty dual,Military share FOI,{src},strong,Fed>Defence>internal_sec,tick683',
    f'cmt_dual_defence_tick683,Dual defence NATO vs Entity II debt,gg_belgium,Fed+E2 dual,CoA dual,2026-05-21,2026,2026,13246000000,"{{""2026"":13246000000}}",,active,,Dual residual,Not TE-additive,{src_dual},strong,Belgium>dual>defence,tick683',
]
with (data / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write("\n" + r)

lb_rows = [
    f"lb_def_asset_optim_3170m_unbooked,Defence asset optim 3.17bn unbooked,Federal,ops,Fed>Defence>asset_optim,3170000000,0,Strong CoA: 1268m 2026 path not in conclaves; Belfius 2bn 2027; residual gap 1170,strong,{src},taxpayers,Defence finance opacity,Primary absurd,8.5,8.5,4,8.05,Book sales calendar FOI,open,,tick683",
    f"lb_russian_assets_cit_shortfall_942m,Russian assets CIT shortfall 942m path,Federal,ops,Fed>Defence>russian_cit,942000000,0,Strong CoA: less receipt 942 over 2025-29; residual measures 735 for 2027-29,strong,{src},Euroclear path,Temp finance dual,Primary,7.5,7.5,4,7.15,Measures FOI,open,,tick683",
    f"lb_nato_effort_13_25bn_2026,NATO effort fill 13.25bn 2026,Federal,ops,Fed>Defence>NATO,13246000000,0,Strong CoA: target 13296 fill 13246 gap ~50; sect16 10958 + external 2288,strong,{src},NATO,2pct dual,Primary,5.5,9.5,3,7.00,Fill gap FOI,open,,tick683",
    f"lb_internal_security_specialty_222m,Internal security specialty pack 222m,Federal,ops,Fed>Defence>internal_sec,222000000,0,Strong CoA: 177+45; mixed civil/military opaque; specialty risk; no Police reimburse FIPA,strong,{src},police/defence,Specialty dual,Primary absurd,8.0,6.0,3,6.90,Military share FOI,open,,tick683",
    f"lb_fraud_yield_method_gap_2026,Fiscal+social fraud yield method gap,Federal,ops,Fed>receipts>fraud,600000000,0,Medium CoA: 300+300 2026 path 600 each 2029; no methodology/split,medium,{src},taxpayers,Revenue claim,Primary,8.0,7.0,3,7.30,Method FOI,open,,tick683",
    f"lb_dual_defence_nato_2026,Dual defence NATO 13.3bn vs E2 debt,Belgium,ops,Belgium>dual>defence,13246000000,0,Strong dual: NATO effort + asset optim opacity vs VL A1 WAL Baa1 FWB A3; not TE-additive,strong,{src_dual},all entities,Defence dual residual,Primary dual,6.5,9.5,3,7.50,Cross FOI,open,,tick683",
]
with (data / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write("\n" + r)

gap_id = "gap_fed_aju2026_defence_nato_l5"
foi_row = (
    f"{gap_id},Federal>Aju2026>Defence_NATO_L5,mod_defensie,"
    "Asset optim 3170 cash calendar and 2026 1268 booking status; Belfius 20pct sale process and price basis 2bn; residual gap 1170 measures; Russian assets CIT monthly series and 735 measures 2027-29; NATO fill gap ~50; internal security 177 line list military share C-UAS BSC helo plane; FIPA cost and non-reimbursement legal basis; normering pipeline 2027-31,"
    "CoA defence residual strong tick683; dual E2 ratings,"
    "5,Ministerie van Landsverdediging / FOD Financiën / FOD BOSA,"
    "openbaarheid@mil.be,https://www.mil.be,"
    f"docs/doge/foi/drafts/{gap_id}.md,ready,2026-08-01,,,,,"
    "cmt_def_asset_optim_3170m|cmt_nato_effort_13246m_2026|cmt_internal_security_222m,"
    "lb_def_asset_optim_3170m_unbooked|lb_nato_effort_13_25bn_2026|lb_internal_security_specialty_222m,"
    f"{utc},{utc},tick683 CoA fed defence primary; human send only"
)
with (data / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + foi_row)

rq = data / "research_queue.csv"
lines = rq.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_674,"):
        out.append(
            "rq_674,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,vlaanderen_gov,"
            "Next residual: fed defence residual dual CoA 2026_22 or SS other receipts L5 or VL De Lijn/Terneuzen deepen.,,"
            f"2026-08-01T12:15:00Z,{utc},"
            "tick683 defence 17.3bn NATO 13.25 asset optim 3.17 unbooked dual; FOI gap_fed_aju2026_defence_nato_l5 ready"
        )
    else:
        out.append(line)
out.append(
    "rq_675,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,mod_defensie,"
    "Next residual: SS other receipts L5 CoA or POD MI leefloon residual dual or VL De Lijn deepen.,,"
    f"{utc},,spawned tick683 after rq_674"
)
rq.write_text("\n".join(out) + "\n", encoding="utf-8")

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_674,683,no,"
    "tick683 defence 17.3bn NATO 13.25 asset optim 3.17 unbooked dual; next rq_675; progress@690 in 7; rq_116 deferred\n",
    encoding="utf-8",
)

draft = f"""# FOI draft — {gap_id}

**gap_id:** `{gap_id}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Rekenhof Commentaar aanpassing staatsbegroting 2026 (2026_22) §3.2.2 + §2.3 Defensie

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: Ministerie van Landsverdediging / FOD Financiën / FOD BOSA
openbaarheid@mil.be

Betreft: Openbaarheid — aju 2026 defensiefinanciering (17,3 mld 2025-29) +
NAVO 2 % L5

Geachte,

Op grond van de wet van 11 april 1994 verzoek ik om:

1. **Meerjarenenveloppe 2025–2029 (17.335,8 mEUR)**: financieringstabel
   tijdelijk / structureel / hoger tekort met cash-by-year.
2. **Optimalisatie activa 3.170 mEUR**: spreiding 40/30/20/10 %, status
   boeking 2026 (**1.268 mEUR** niet in conclaven), verkoop **20 % Belfius**
   (raming **2 mld**, ECB/NBB/FSMA) en maatregelen voor restant
   **1.170 mEUR**.
3. **VenB bevroren Russische tegoeden**: reeks 2025–2029 (2025 **1.148**,
   2026–29 **1.016**/j) en maatregelen voor restant **735 mEUR** (2027–29).
4. **NAVO-norm 2026**: detail invulling **13.246 mEUR** t.o.v. doel
   **13.296 mEUR** (sectie 16, pensioenen, normering, COFOG 02).
5. **Interne veiligheid 177 mEUR** (+ NATO trust fund **45 mEUR**):
   lijst basisallocaties; militaire component (C-UAS, BSC, helikopter
   politie, vliegtuig BELSPO); FIPA/spoorwegpatrouilles en
   niet-terugbetaling door Federale Politie.
6. **Normering 2027–2031**: ontvangen voorstellen departementen en
   NAVO-adviesprocedure.

Publieke steun: Rekenhof, *Commentaar … staatsbegroting 2026* (2026_22),
Deel I §3.2.2 en Deel II §2.3 Sectie 16.

Met vriendelijke groeten,
[Naam — menselijke afzender]
```

## Notes

- Do **not** send as agent; human only.
- Complements earlier `gap_fed` defence FOIs with aju residual (asset optim unbooked, internal security specialty).
- Dual: Entity II debt ratings / financing.
- Tick 683.
"""
(root / "docs/doge/foi/drafts" / f"{gap_id}.md").write_text(draft, encoding="utf-8")

entry = f"""
### {utc} — tick {tick}
- Unit: **rq_674** (FOI-adjacent dual residual — **fed CoA defence multi-year NATO + asset optim dual**)
- Found (primary CoA 2026_22 §3.2.2 + §2.3):
  - **Defence 2025–29 EUR17.336bn** (+552.8 GDP); 2026 sect16 **+188.2**
  - **Temp finance:** Russian assets CIT path **−942** (2025 **1.148**; 2026–29 **1.016**/yr; residual measures **735** for 2027–29)
  - **Higher deficit 4.804** of which asset optim **3.170** (2026 **1.268** = 40% **not booked** conclaves; Belfius 20% sale est **2bn** ~2027; residual gap **1.170**)
  - **NATO 2%:** GDP **664.8bn** target **13.296**; fill budget **10.958** + external **2.288** (pens **1.988** −40; norm **168**; COFOG **131**) = **13.246** gap **~50**
  - **Internal security 177** sect16 + trust **45** FA = **222**; mixed civil/military opacity; FIPA no Police reimburse
  - Dual Entity II ratings. Strong CoA; L5 FOI.
- Wrote: budgets (+45); commitments (+6); leaderboard (+6); sources (+2); FOI draft **gap_fed_aju2026_defence_nato_l5**; rq_674=done; spawn **rq_675**; loop_state ticks=683
- FOI opened: gap_fed_aju2026_defence_nato_l5 — ready (not sent)
- Next: rq_675; progress@690 in 7 ticks; rq_116 deferred
"""
with (root / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(entry)

print("OK tick683")
print("budgets", len(bud_rows), "cmt", len(cmt_rows), "lb", len(lb_rows))

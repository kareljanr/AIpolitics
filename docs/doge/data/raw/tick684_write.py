from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
tick = 684
utc = "2026-08-01T12:45:00Z"
src = "src_ccrek_fed_aju2026_pod_mi_leefloon"
src_dual = "src_dual_pod_mi_leefloon_tick684"
url = "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf"

src_rows = [
    f'{src},CoA federal BA2026 POD MI OCMW RMI wet65 leefloon residual dual,{url},Cour des comptes / Rekenhof,2026-08-01,audit,"Strong tick684: OCMW toelagen total 2309 (RMI 2133 wet65 176) from IB 2241 (+index 26 +volume 42); save integratiebedrag+5yr wait IB -40.2 BC -13.1 correction +27.1; CoA: 13.1 will not land 2026 entry no longer feasible; integratiebedrag design 70pct not 50 fines 30/15; subsidiary shift RMI to wet65 100pct federal not budgeted; 5yr wait RvS EU+Art23 issues; unemp exclude total 193904 waves; Q1 excl 45592 of 48815 plan 93.4pct; leefloon inflow 17606 = 31.9pct (BRU 27.5 VL 23.5 WAL 37.2 DG 50); OCMW reject 14pct; medical help 100.3 vs 112.3 -12; POD MI +60 social cell"',
    f'{src_dual},Dual POD MI leefloon vs RVA unemp reform Entity II,{url},DOGE synthesis CoA dual,2026-08-01,synthesis,"Strong dual: unemp exclude 193.9k waves leefloon inflow 31.9pct Q1 vs VL/WAL OCMW; soft save 13.1 dead; not TE-additive; tick684"',
]
with (data / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    for r in src_rows:
        f.write("\n" + r)

bud_rows = [
    # OCMW toelagen matrix
    f"bud_pod_mi_ocmw_toelagen_total_2309m_2026,pod_mi,2026,2309000000,,,budgeted,{src},strong,OCMW toelagen RMI+wet65 total BC 2309m (IB 2241; +index 26 +volume 42); tick684",
    f"bud_pod_mi_rmi_2133m_2026,pod_mi,2026,2133000000,,,budgeted,{src},strong,RMI (leefloon) OCMW toelage 2133m (IB 2085 +index 23 +volume 25); tick684",
    f"bud_pod_mi_wet65_176m_2026,pod_mi,2026,176000000,,,budgeted,{src},strong,Wet 65 maatschappelijke dienstverlening OCMW toelage 176m (IB 156 +index 3 +volume 17); tick684",
    f"bud_pod_mi_rmi_ib_2085m_2026,pod_mi,2026,2085000000,,,budgeted,{src},strong,RMI IB2026 2085m baseline; tick684",
    f"bud_pod_mi_wet65_ib_156m_2026,pod_mi,2026,156000000,,,budgeted,{src},strong,Wet65 IB2026 156m baseline; tick684",
    f"bud_pod_mi_index_up_26m_2026,pod_mi,2026,26000000,,,budgeted,{src},strong,Index component OCMW toelagen +26m (RMI +23 wet65 +3) spilindex path; tick684",
    f"bud_pod_mi_volume_up_42m_2026,pod_mi,2026,42000000,,,budgeted,{src},strong,Volume component OCMW toelagen +42m (beneficiaries up + soft save corrections); tick684",
    # Soft saves
    f"bud_pod_mi_save_ib_40_2m_2026,pod_mi,2026,40200000,,,budgeted,{src},strong,IB2026 planned save integratiebedrag+5yr wait 40.2m; tick684",
    f"bud_pod_mi_save_bc_13_1m_2026,pod_mi,2026,13100000,,,budgeted,{src},strong,BC2026 revised save 13.1m (correction +27.1 vs IB); CoA: will not be achieved 2026; tick684",
    f"bud_pod_mi_save_correction_27_1m_2026,pod_mi,2026,27100000,,,budgeted,{src},strong,Downward correction of POD MI soft saves +27.1m (less save) aju2026; tick684",
    f"bud_pod_mi_integratiebedrag_save_bc_10m_2026,pod_mi,2026,10000000,,,budgeted,{src},strong,Integratiebedrag save BC 10.0m (IB 33.5; RMI 4.7 + wet65 5.3); tick684",
    f"bud_pod_mi_integratiebedrag_save_ib_33_5m_2026,pod_mi,2026,33500000,,,budgeted,{src},strong,Integratiebedrag save IB 33.5m (RMI 17 + wet65 16.6); tick684",
    f"bud_pod_mi_integratiebedrag_rmi_save_4_7m_2026,pod_mi,2026,4700000,,,budgeted,{src},strong,Integratiebedrag RMI branch save BC 4.7m (IB 17); new inflow + sanctions 33/15pct; tick684",
    f"bud_pod_mi_integratiebedrag_wet65_save_5_3m_2026,pod_mi,2026,5300000,,,budgeted,{src},strong,Integratiebedrag wet65 branch save BC 5.3m (IB 16.6); temp protected; design max 70pct not 50; tick684",
    f"bud_pod_mi_wait5yr_save_bc_3_1m_2026,pod_mi,2026,3100000,,,budgeted,{src},strong,Five-year wait social assistance save BC 3.1m (IB 6.7; RMI 1.4 + wet65 1.6); tick684",
    f"bud_pod_mi_wait5yr_save_ib_6_7m_2026,pod_mi,2026,6700000,,,budgeted,{src},strong,Five-year wait save IB 6.7m; tick684",
    f"bud_pod_mi_save_13_1m_dead_2026,pod_mi,2026,13100000,,,budgeted,{src},strong,CoA: 13.1m BC save will not land 2026 - entry into force no longer feasible (legal complexity); tick684",
    # Medical help residual
    f"bud_pod_mi_medical_help_100_3m_2026,pod_mi,2026,100300000,,,budgeted,{src},strong,Medical help exp BC 100.3m (IB 112.3; -12) partly return-policy attribution hard to verify; tick684",
    f"bud_pod_mi_medical_help_ib_112_3m_2026,pod_mi,2026,112300000,,,budgeted,{src},strong,Medical help IB 112.3m; tick684",
    f"bud_pod_mi_social_cell_up_60m_2026,pod_mi,2026,60000000,,,budgeted,{src},strong,POD MI +60m within social cell primary exp aju (tick681 cross); tick684",
    # Unemp exclude / leefloon dual
    f"bud_rva_exclude_waves_total_193904,rva,2026,193904,,,budgeted,{src},strong,Unemp/inschakeling exclusion waves total 193904 physical units (RVA Sep2025 est); tick684",
    f"bud_rva_exclude_q1_actual_45592_2026,rva,2026,45592,,,budgeted,{src},strong,Q1 2026 actual exclusions golf1+2 total 45592 (plan 48815; 93.4pct); tick684",
    f"bud_rva_exclude_q1_plan_48815_2026,rva,2026,48815,,,budgeted,{src},strong,Q1 2026 planned exclusions golf1+2 48815; tick684",
    f"bud_pod_mi_leefloon_inflow_excl_17606_q1_2026,pod_mi,2026,17606,,,budgeted,{src},strong,New leefloners from unemp/inschakeling excluded Q1 2026 real 17606 = 31.9pct of excluded; tick684",
    f"bud_pod_mi_leefloon_inflow_pct_31_9_q1_2026,pod_mi,2026,319,,,budgeted,{src},strong,Share excluded entering leefloon 31.9pct Q1 national (x1000 for storage=319 means 31.9); note percent; tick684",
    f"bud_pod_mi_leefloon_inflow_bru_4213_q1_2026,pod_mi,2026,4213,,,budgeted,{src},strong,BRU new leefloners from excluded Q1 4213 (27.5pct of BRU excluded); tick684",
    f"bud_pod_mi_leefloon_inflow_vl_2558_q1_2026,pod_mi,2026,2558,,,budgeted,{src},strong,VL new leefloners from excluded Q1 2558 (23.5pct); tick684",
    f"bud_pod_mi_leefloon_inflow_wal_10728_q1_2026,pod_mi,2026,10728,,,budgeted,{src},strong,WAL excl DG new leefloners from excluded Q1 10728 (37.2pct); tick684",
    f"bud_pod_mi_leefloon_inflow_dg_107_q1_2026,pod_mi,2026,107,,,budgeted,{src},strong,DG new leefloners from excluded Q1 107 (50pct); tick684",
    f"bud_ocmw_reject_excl_applicants_14pct_q1_2026,pod_mi,2026,14,,,budgeted,{src},strong,OCMW reject rate 14pct national of applications from unemp-excluded (VL 15.4 WAL 15.3 BRU 9.7 DG 7.8); tick684",
    f"bud_rva_exclude_waves_bru_41709,rva,2026,41709,,,budgeted,{src},strong,BRU exclusion waves total 41709 of 193904; tick684",
    f"bud_rva_exclude_waves_vl_62676,rva,2026,62676,,,budgeted,{src},strong,VL exclusion waves total 62676; tick684",
    f"bud_rva_exclude_waves_wal_88566,rva,2026,88566,,,budgeted,{src},strong,WAL excl DG exclusion waves total 88566; tick684",
    f"bud_rva_exclude_waves_dg_953,rva,2026,953,,,budgeted,{src},strong,DG exclusion waves total 953; tick684",
    # Dual class EUR for leefloon pack
    f"bud_dual_pod_mi_ocmw_2309m_2026,gg_belgium,2026,2309000000,,,budgeted,{src_dual},strong,Dual POD MI OCMW 2.309bn vs regional OCMW ops class; not TE-additive; tick684",
    f"bud_dual_unemp_leefloon_shift_q1_2026,gg_belgium,2026,17606,,,budgeted,{src_dual},strong,Dual unemp exclude to leefloon Q1 17606 persons 31.9pct; tick684",
]
with (data / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write("\n" + r)

# ensure entities
ent = data / "entities.csv"
et = ent.read_text(encoding="utf-8")
new_ents = []
if "\npod_mi," not in et and not et.startswith("pod_mi,"):
    new_ents.append(
        "pod_mi,POD Maatschappelijke Integratie,SPP Integration sociale,Federal Public Planning Service Social Integration,agency,sec_federal,bi,https://www.mi-is.be,,,OCMW RMI wet65 leefloon dual; CoA aju2026; tick684"
    )
if "\nrva," not in et and ",rva," not in et:
    # may already exist as RVA
    if "\nrva," not in et:
        new_ents.append(
            "rva,Rijksdienst voor Arbeidsvoorziening RVA,ONEM,National Employment Office,agency,sec_ss,bi,https://www.rva.be,,,Unemp reform exclusion waves dual leefloon; tick684"
        )
if new_ents:
    with ent.open("a", encoding="utf-8", newline="") as f:
        for e in new_ents:
            f.write("\n" + e)

cmt_rows = [
    f'cmt_pod_mi_ocmw_2309m,POD MI OCMW toelagen 2.309bn RMI+wet65,pod_mi,OCMWs,CoA 2026_22 3.1,2026-05-21,2026,2026,2309000000,"{{""rmi"":2133000000,""wet65"":176000000}}",,active,,Leefloon dual,Unit cost FOI,{src},strong,Fed>POD_MI>OCMW,tick684',
    f'cmt_pod_mi_soft_save_dead_13m,POD MI soft save 13.1m dead 2026,pod_mi,Newcomers integration,CoA 2026_22 3.1.2-4,2026-05-21,2026,2026,13100000,"{{""ib"":40200000,""bc"":13100000}}",,active,,Integratiebedrag+wait5yr,Drop or law FOI,{src},strong,Fed>POD_MI>save,tick684',
    f'cmt_integratiebedrag_design_shift,Integratiebedrag 70pct design + wet65 shift,pod_mi,Protected statuses,MR first reading + CoA,2026-05-21,2026,2029,10000000,"{{""bc_save"":10000000}}",,active,,70 not 50pct dual,Cost of 100pct federal FOI,{src},strong,Fed>POD_MI>integratie,tick684',
    f'cmt_unemp_exclude_193904,Unemp exclusion waves 193904 dual leefloon,rva,Unemployed,Programmawet 18 Jul 2025,2025-07-18,2026,2027,193904,"{{""total_units"":193904}}",,active,,Reform dual,Q series FOI,{src},strong,Fed>RVA>exclude,tick684',
    f'cmt_leefloon_inflow_31_9pct_q1,Leefloon inflow 31.9pct of excluded Q1,pod_mi,OCMWs+RVA,CoA 2026_22 unemp follow-up,2026-05-21,2026,2026,17606,"{{""inflow"":17606,""pct"":31.9}}",,active,,Spillover dual,Stabilize FOI,{src},strong,Fed>POD_MI>spillover,tick684',
    f'cmt_dual_pod_mi_tick684,Dual POD MI leefloon vs RVA unemp Entity II,gg_belgium,Fed+regions dual,CoA dual,2026-05-21,2026,2026,2309000000,"{{""2026"":2309000000}}",,active,,Dual residual,Not TE-additive,{src_dual},strong,Belgium>dual>leefloon,tick684',
]
with (data / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write("\n" + r)

lb_rows = [
    f"lb_pod_mi_ocmw_2309m_2026,POD MI OCMW toelagen 2.309bn,Federal,ops,Fed>POD_MI>OCMW,2309000000,0,Strong CoA RMI 2133 + wet65 176; dual regional OCMW,strong,{src},leefloon beneficiaries,Social assistance dual,Primary,5.5,8.5,3,6.55,Unit cost FOI,open,,tick684",
    f"lb_pod_mi_soft_save_dead_13m_2026,POD MI soft save 13.1m dead 2026,Federal,ops,Fed>POD_MI>save,13100000,0,Strong CoA: BC 13.1 of IB 40.2 will not land; entry 2026 not feasible,strong,{src},newcomers,Soft save dual,Primary absurd,8.5,4.0,2,6.55,Drop budget claim,open,,tick684",
    f"lb_unemp_exclude_193904_2026,Unemp exclusion waves 193.9k,Federal,ops,Fed>RVA>exclude,193904,0,Strong CoA RVA Sep2025 est 193904 physical units multi-wave to Jul2027,strong,{src},unemployed,Reform dual,Primary,7.0,5.5,3,6.25,Outcome series FOI,open,,tick684",
    f"lb_leefloon_inflow_31_9pct_q1_2026,Leefloon inflow 31.9pct excluded Q1,Federal,ops,Fed>POD_MI>spillover,17606,0,Strong CoA: 17606 new leefloners from excluded; WAL 37.2 VL 23.5 BRU 27.5,strong,{src},OCMWs,Spillover dual,Primary,7.5,5.0,3,6.25,Stabilize stats FOI,open,,tick684",
    f"lb_wait5yr_rvs_eu_risk_2026,Five-year wait RvS EU/Art23 risk,Federal,ops,Fed>POD_MI>wait5yr,3100000,0,Strong CoA: Council of State incompatibilities EU law + Art23; second reading rewrite,strong,{src},newcomers,Legal risk dual,Primary absurd,8.5,3.5,3,6.20,Rewrite or drop FOI,open,,tick684",
    f"lb_dual_pod_mi_leefloon_2026,Dual POD MI leefloon vs unemp reform,Belgium,ops,Belgium>dual>leefloon,2309000000,0,Strong dual: OCMW 2.309bn + 31.9pct spillover vs RVA waves; not TE-additive,strong,{src_dual},all entities,Leefloon dual residual,Primary dual,6.5,8.5,3,7.15,Cross FOI,open,,tick684",
]
with (data / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write("\n" + r)

gap_id = "gap_fed_aju2026_pod_mi_leefloon_l5"
foi_row = (
    f"{gap_id},Federal>Aju2026>POD_MI_leefloon_L5,pod_mi,"
    "OCMW toelagen RMI/wet65 monthly beneficiary counts 2025-26; integratiebedrag law calendar and 100pct federal cost of subsidiary shift; confirmation 13.1 save dropped; 5yr wait second-reading text; unemp-exclude to leefloon monthly series by region with lag note; medical help 100.3 attribution to return policy; OCMW reject rates methodology,"
    "CoA POD MI leefloon residual strong tick684; dual RVA,"
    "5,POD Maatschappelijke Integratie / RVA / openbaarheid,"
    "openbaarheid@mi-is.be,https://www.mi-is.be,"
    f"docs/doge/foi/drafts/{gap_id}.md,ready,2026-08-01,,,,,"
    "cmt_pod_mi_ocmw_2309m|cmt_pod_mi_soft_save_dead_13m|cmt_leefloon_inflow_31_9pct_q1,"
    "lb_pod_mi_ocmw_2309m_2026|lb_pod_mi_soft_save_dead_13m_2026|lb_leefloon_inflow_31_9pct_q1_2026,"
    f"{utc},{utc},tick684 CoA POD MI primary; human send only"
)
with (data / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + foi_row)

rq = data / "research_queue.csv"
lines = rq.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_675,"):
        out.append(
            "rq_675,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,mod_defensie,"
            "Next residual: SS other receipts L5 CoA or POD MI leefloon residual dual or VL De Lijn deepen.,,"
            f"2026-08-01T12:30:00Z,{utc},"
            "tick684 POD MI OCMW 2309 soft save 13.1 dead unemp-leefloon 31.9pct dual; FOI gap_fed_aju2026_pod_mi_leefloon_l5 ready"
        )
    else:
        out.append(line)
out.append(
    "rq_676,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,pod_mi,"
    "Next residual: VL De Lijn deepen CoA 2026_28 or SS other receipts L5 or fed justice residual dual.,,"
    f"{utc},,spawned tick684 after rq_675"
)
rq.write_text("\n".join(out) + "\n", encoding="utf-8")

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_675,684,no,"
    "tick684 POD MI OCMW 2309 soft save 13.1 dead unemp-leefloon 31.9pct dual; next rq_676; progress@690 in 6; rq_116 deferred\n",
    encoding="utf-8",
)

draft = f"""# FOI draft — {gap_id}

**gap_id:** `{gap_id}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Rekenhof Commentaar aanpassing staatsbegroting 2026 (2026_22) §3.1 POD MI + unemp follow-up

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: POD Maatschappelijke Integratie / RVA
openbaarheid@mi-is.be

Betreft: Openbaarheid — aju 2026 POD MI OCMW-toelagen (2.309 mld) +
leefloon/spillover L5

Geachte,

Op grond van de wet van 11 april 1994 verzoek ik om:

1. **OCMW-toelagen RMI 2.133 mEUR + wet ‘65 176 mEUR**: maandreeksen
   aantal gerechtigden 2025–2026 en splitsing index/volume.
2. **Besparingen integratiebedrag + vijfjarige wachttermijn**: bevestiging
   dat BC **13,1 mEUR** in 2026 niet haalbaar is; wetgevingskalender;
   kostprijs overheveling subsidiair beschermden (100 % federale
   tussenkomst) die nog niet op wet ‘65 is ingeschreven.
3. **Raad van State-advies 78.752** en aangepaste teksten tweede lezing
   vijfjarige wachttermijn.
4. **Spillover werkloosheid→leefloon**: maandreeksen per gewest na
   stabilisatie (3–4 maanden lag) van uitsluitingen en nieuwe leefloners
   (Q1: **17.606** = **31,9 %**); OCMW-weigeringspercentages.
5. **Medische hulp 100,3 mEUR** (IB 112,3): toerekening aan
   terugkeerbeleid vs andere factoren.

Publieke steun: Rekenhof, *Commentaar … staatsbegroting 2026* (2026_22),
§3.1 POD MI en opvolging werkloosheidshervorming.

Met vriendelijke groeten,
[Naam — menselijke afzender]
```

## Notes

- Do **not** send as agent; human only.
- Dual: RVA exclusion waves; regional OCMW.
- Complements earlier POD MI soft-save notes (tick508 class).
- Tick 684.
"""
(root / "docs/doge/foi/drafts" / f"{gap_id}.md").write_text(draft, encoding="utf-8")

entry = f"""
### {utc} — tick {tick}
- Unit: **rq_675** (FOI-adjacent dual residual — **POD MI OCMW/leefloon soft saves + unemp spillover dual**)
- Found (primary CoA 2026_22 §3.1 + unemp follow-up):
  - **OCMW toelagen EUR2.309bn** (RMI **2.133** + wet65 **176**; IB **2.241**; index **+26** volume **+42**)
  - **Soft saves:** IB **−40.2** → BC **−13.1** (correction **+27.1**); integratiebedrag **−10** (was 33.5); wait5yr **−3.1** (was 6.7); CoA: **13.1 will not land 2026**
  - Design: integratiebedrag max **70%** not 50; fines **30/15**; subsidiary→wet65 **100%** federal not budgeted; wait5yr **RvS EU+Art23** risk
  - **Unemp exclude 193.904** waves; Q1 actual **45.592**/48.815 (93.4%); leefloon inflow **17.606** = **31.9%** (WAL **37.2** VL **23.5** BRU **27.5**); OCMW reject **14%**
  - Medical help **100.3** (IB 112.3; −12). Dual RVA/OCMW. Strong CoA; L5 FOI.
- Wrote: budgets (+36); commitments (+6); leaderboard (+6); sources (+2); entities pod_mi; FOI draft **gap_fed_aju2026_pod_mi_leefloon_l5**; rq_675=done; spawn **rq_676**; loop_state ticks=684
- FOI opened: gap_fed_aju2026_pod_mi_leefloon_l5 — ready (not sent)
- Next: rq_676; progress@690 in 6 ticks; rq_116 deferred
"""
with (root / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(entry)

print("OK tick684")
print("budgets", len(bud_rows), "cmt", len(cmt_rows), "lb", len(lb_rows))

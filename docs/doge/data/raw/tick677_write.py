from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
tick = 677
utc = "2026-08-01T11:00:00Z"
src = "src_ccrek_fed_aju2026_ss_receipts"
src_dual = "src_dual_ss_receipts_tick677"
url = "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf"

src_rows = [
    f'{src},CoA federal BA2026 SS receipts residual matrix dual E2,{url},Cour des comptes / Rekenhof,2026-08-01,audit,"Strong tick677: SS consol rec BC 148002.4 (-14.8); bijdragen 85328 (-197.3); toelagen 27443.8 (-234.9); alt fin 27583.4 (+361.8) of which BTW 19634.7 RV 7948.7; other 7647.2; RSZ contrib 69474.7 (-116.8); OISZ direct FPD 59.4 Fedris 23.2 RIZIV 0.6; structural red 4294.1 (werkbonus 1827.3 struct 2419.5); targeted red exp 848.4 (first hires 512.5 ceiling 58.2); total red 5142.5; gov dots RSZ GB 8656.1 (evenwicht 5446.2 globale 2683.7 specifiek 208.9 deelstaat 317.3) path -195; 2025 evenwicht overfinance settle -547.5 (kapital -59.6); alt RSZ 23711.3 RSVZ 3872.1; assign total 27685.5 (+360.5) incl bijzondere 100.9 deeleconomie 1.2; Plusplannen delay; horeca/CAD yield 11.3 not 28; overtime cost 32.3 not 43; Zuidertoren 2.5 study 2026 unoffset; wage-cap phase2 -75 from 2027; werkbonus -357.5 2028; bijzondere cut -415 from 2028 (2025 est 1430.1)"',
    f'{src_dual},Dual SS receipts 148.0bn near-balance vs exp 148.0bn dual E2,{url},DOGE synthesis CoA SS dual,2026-08-01,synthesis,"Strong dual: SS rec 148002.4 vs exp 148026.6 gap ~24m; alt fin BTW/RV dual tax base; not TE-additive; tick677"',
]
with (data / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    for r in src_rows:
        f.write("\n" + r)

bud_rows = [
    # Matrix totals
    f"bud_ss_rec_total_bc_148002m_2026,sec_ss,2026,148002400000,,,budgeted,{src},strong,SS consol receipts BC2026 148002.4m (-14.8 vs IB 148017.2); CoA Deel III; tick677",
    f"bud_ss_rec_2024_outturn_139795m,sec_ss,2024,139794800000,,,outturn,{src},strong,SS consol receipts outturn 139794.8m 2024; CoA table; tick677",
    f"bud_ss_rec_2025_prelim_145270m,sec_ss,2025,145269800000,,,outturn,{src},strong,SS consol receipts prelim 145269.8m 2025; CoA table; tick677",
    f"bud_ss_bijdragen_85328m_2026,sec_ss,2026,85328000000,,,budgeted,{src},strong,SS contributions 85328.0m BC2026 (-197.3 / -0.2pct); 57.7pct of receipts; tick677",
    f"bud_ss_toelagen_overheden_27444m_2026,sec_ss,2026,27443800000,,,budgeted,{src},strong,Government grants/dots to SS 27443.8m (-234.9); 18.5pct of receipts; tick677",
    f"bud_ss_alt_finance_27583m_2026,sec_ss,2026,27583400000,,,budgeted,{src},strong,Alternative financing fiscal assign 27583.4m (+361.8); 18.6pct receipts; tick677",
    f"bud_ss_other_receipts_7647m_2026,sec_ss,2026,7647200000,,,budgeted,{src},strong,Other SS receipts 7647.2m (+55.6); tick677",
    # RSZ contributions
    f"bud_rsz_contrib_69475m_2026,rsz,2026,69474700000,,,budgeted,{src},strong,RSZ social contributions 69474.7m 2026 (-116.8 / -0.2pct); 99.9pct of employee-regime contributions; tick677",
    f"bud_oisz_fpd_direct_contrib_59_4m_2026,fpd_pensioenen,2026,59400000,,,budgeted,{src},strong,FPD direct-collected employee contributions 59.4m 2026; CoA fn45; tick677",
    f"bud_oisz_fedris_direct_contrib_23_2m_2026,fedris,2026,23200000,,,budgeted,{src},strong,Fedris direct-collected contributions 23.2m 2026; CoA fn45; tick677",
    f"bud_oisz_riziv_direct_contrib_0_6m_2026,riziv,2026,600000,,,budgeted,{src},strong,RIZIV direct-collected contributions 0.6m 2026; CoA fn45; tick677",
    # Contribution reductions
    f"bud_ss_structural_red_4294m_2026,rsz,2026,4294100000,,,budgeted,{src},strong,Federal structural contribution reductions unchanged-policy 4294.1m (+3.8); tick677",
    f"bud_ss_werkbonus_1827m_2026,rsz,2026,1827300000,,,budgeted,{src},strong,Werkbonus personal RSZ reduction 1827.3m (+5.0); tick677",
    f"bud_ss_struct_employer_red_2420m_2026,rsz,2026,2419500000,,,budgeted,{src},strong,Structural employer contribution reductions 2419.5m (-7.8); tick677",
    f"bud_ss_targeted_red_exp_848m_2026,rsz,2026,848400000,,,budgeted,{src},strong,Targeted contribution reductions booked as social exp 848.4m (-10.0); tick677",
    f"bud_ss_first_hires_red_512_5m_2026,rsz,2026,512500000,,,budgeted,{src},strong,First-hire contribution reductions 512.5m of targeted pack; tick677",
    f"bud_ss_wage_ceiling_exempt_58_2m_2026,rsz,2026,58200000,,,budgeted,{src},strong,Employer contrib exemption above 85k/qtr (86.7k idx) 58.2m 2026; tick677",
    f"bud_ss_total_red_5142m_2026,rsz,2026,5142500000,,,budgeted,{src},strong,Total federal contribution reductions 5142.5m (-6.2); structural+targeted; tick677",
    f"bud_ss_employer_responsab_impact_24m_2026,rsz,2026,24000000,,,budgeted,{src},strong,MR aju measures impact on contrib receipts 24.0m (downward revision employer responsabilisering); tick677",
    # Reform yields residual
    f"bud_plusplannen_yield_est_64_2m_2026,rsz,2026,64200000,,,estimate,{src},medium,Plusplannen reform yield RSZ Dec2025 64.2m (was 53); global re-est May no longer separable; July start may overstate; tick677",
    f"bud_sports_ceiling_double_fix_yield_10m_2026,rsz,2026,10000000,,,estimate,{src},medium,Sports employer double-benefit fix yield est 10m/yr; July 2026 start may overstate; tick677",
    f"bud_horeca_cad_abolition_yield_11_3m_2026,rsz,2026,11300000,,,budgeted,{src},strong,Horeca+collective hours reduction abolition RSZ yield 11.3m (IB 28; -16.7 delay); tick677",
    f"bud_voluntary_overtime_cost_32_3m_2026,rsz,2026,32300000,,,budgeted,{src},strong,Voluntary overtime expansion contrib cost 32.3m 2026 (IB 43; -10.7); implemented 1 Apr; tick677",
    f"bud_zuidertoren_study_2_5m_2026,rsz,2026,2500000,,,budgeted,{src},strong,Zuidertoren renovation study spend 2.5m 2026; asset sale offset delayed to Mar 2027 → GB deficit understated 2.5m; tick677",
    f"bud_zuidertoren_reno_envelope_177_7m,rsz,2026,177700000,,,commitment,{src},strong,Zuidertoren renovation envelope 177.7m 2026-31 of which 168.8m from RSZ-GB reserves asset sales; tick677",
    f"bud_wage_ceiling_phase2_75m_2027,rsz,2027,75000000,,,budgeted,{src},strong,Wage ceiling phase2 employer contrib free above cap -75m from 2027; rules not final; tick677",
    f"bud_werkbonus_strengthen_357_5m_2028,rsz,2028,357500000,,,budgeted,{src},strong,Werkbonus strengthen (ref wages up) -357.5m from 2028 (was 2029); tick677",
    f"bud_bijzondere_bijdrage_cut_415m_2028,rsz,2028,415000000,,,budgeted,{src},strong,Bijzondere SS contribution cut -415.0m from 2028 (was 2029); tick677",
    f"bud_bijzondere_bijdrage_est_1430m_2025,rsz,2025,1430100000,,,estimate,{src},strong,Bijzondere socialezekerheidsbijdrage est 1430.1m 2025; CoA fn56; tick677",
    # Government dots RSZ GB
    f"bud_rsz_gov_dots_total_8656m_2026,rsz,2026,8656100000,,,budgeted,{src},strong,RSZ-GB government dots total 8656.1m (-195.0 / -2.3pct); tick677",
    f"bud_rsz_evenwichtsdotatie_5446m_2026,rsz,2026,5446200000,,,budgeted,{src},strong,Evenwichtsdotatie RSZ-GB 5446.2m 2026 (path -207.3 vs IB); tick677",
    f"bud_rsz_globale_subsidie_2684m_2026,rsz,2026,2683700000,,,budgeted,{src},strong,Globale Staatssubsidie RSZ-GB 2683.7m (+18.1); tick677",
    f"bud_rsz_specifieke_toelage_209m_2026,rsz,2026,208900000,,,budgeted,{src},strong,Specifieke Staatstoelage RSZ-GB 208.9m; tick677",
    f"bud_rsz_deelstaat_subsidies_317m_2026,rsz,2026,317300000,,,budgeted,{src},strong,Deelstaatentiteiten subsidies RSZ-GB 317.3m (path -7.5); tick677",
    f"bud_rsz_evenwicht_2025_overfinance_settle_547_5m,rsz,2026,547500000,,,budgeted,{src},strong,2025 evenwichtsdotatie overfinance settlement expense 547.5m on 2026 GB (incl capital -59.6); GB deficit -547.5m 2026; tick677",
    f"bud_rsz_gb_deficit_547_5m_2026,rsz,2026,547500000,,,budgeted,{src},strong,RSZ-GB deficit 547.5m 2026 after 2025 evenwicht settle + capital; tick677",
    # Alternative financing matrix
    f"bud_ss_alt_btw_19635m_2026,sec_ss,2026,19634700000,,,budgeted,{src},strong,Alt finance from VAT 19634.7m of 27583.4 total; tick677",
    f"bud_ss_alt_rv_7949m_2026,sec_ss,2026,7948700000,,,budgeted,{src},strong,Alt finance from withholding tax on movable income 7948.7m; tick677",
    f"bud_rsz_alt_finance_23711m_2026,rsz,2026,23711300000,,,budgeted,{src},strong,RSZ-GB alt finance 23711.3m (+319.1); tick677",
    f"bud_rsz_alt_btw_base_9344m_2026,rsz,2026,9343800000,,,budgeted,{src},strong,RSZ BTW base amount legal minimum 9343.8m 2026 (pct formula below floor); tick677",
    f"bud_rsz_alt_btw_care_7707m_2026,rsz,2026,7707300000,,,budgeted,{src},strong,RSZ BTW geneeskundige verzorging 7707.3m (+62.1); tick677",
    f"bud_rsz_alt_rv_6660m_2026,rsz,2026,6660200000,,,budgeted,{src},strong,RSZ roerende voorheffing 6660.2m (+257.0); tick677",
    f"bud_rsvz_alt_finance_3872m_2026,rsvz,2026,3872100000,,,budgeted,{src},strong,RSVZ-GB alt finance 3872.1m (+42.7); tick677",
    f"bud_rsvz_alt_btw_base_1877m_2026,rsvz,2026,1876500000,,,budgeted,{src},strong,RSVZ BTW base legal minimum 1876.5m; tick677",
    f"bud_rsvz_alt_btw_care_707m_2026,rsvz,2026,707100000,,,budgeted,{src},strong,RSVZ BTW geneeskundige verzorging 707.1m (-7.0); tick677",
    f"bud_rsvz_alt_rv_1289m_2026,rsvz,2026,1288500000,,,budgeted,{src},strong,RSVZ roerende voorheffing 1288.5m (+49.7); tick677",
    f"bud_ss_assign_bijzondere_100_9m_2026,sec_ss,2026,100900000,,,budgeted,{src},strong,Assign-fund bijzondere SS contribution 100.9m; tick677",
    f"bud_ss_assign_deeleconomie_1_2m_2026,rsvz,2026,1200000,,,budgeted,{src},strong,Assign-fund deeleconomie PIT 1.2m to RSVZ-GB; tick677",
    f"bud_ss_assign_funds_total_27686m_2026,sec_ss,2026,27685500000,,,budgeted,{src},strong,Total assign-fund finance to SS 27685.5m (+360.5 / +1.3pct vs IB); tick677",
    # Near-balance dual
    f"bud_ss_near_balance_gap_24m_2026,sec_ss,2026,24200000,,,estimate,{src},strong,SS exp 148026.6 - rec 148002.4 = gap ~24.2m near-balance; tick677",
    f"bud_dual_ss_receipts_148bn_2026,gg_belgium,2026,148002400000,,,budgeted,{src_dual},strong,Dual SS receipts 148.0bn class vs E2 tax/SS systems; not TE-additive; tick677",
]
with (data / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write("\n" + r)

cmt_rows = [
    f'cmt_ss_rec_matrix_148bn,SS receipts matrix 148.0bn BC2026,sec_ss,SS beneficiaries+taxpayers,CoA 2026_22 Deel III ChI,2026-05-21,2026,2026,148002400000,"{{""2026"":148002400000}}",,active,,SS financing dual,L5 FOI assign,{src},strong,SS>receipts>matrix,tick677',
    f'cmt_ss_alt_finance_27583m,SS alternative financing BTW+RV 27.58bn,sec_ss,RSZ+RSVZ,Wet 18 Apr 2017,2017-04-18,2026,2026,27583400000,"{{""2026"":27583400000}}",,active,,Fiscal assign to SS,Publish cash path,{src},strong,SS>alt_finance,tick677',
    f'cmt_rsz_evenwicht_dots_8656m,RSZ-GB government dots 8.66bn,rsz,RSZ Globaal Beheer,CoA 2026_22 3.1,2026-05-21,2026,2026,8656100000,"{{""2026"":8656100000}}",,active,,Balance guarantee dual,Settlement FOI,{src},strong,SS>RSZ>dots,tick677',
    f'cmt_ss_contrib_red_5142m,Federal contribution reductions 5.14bn,rsz,Employers+employees,CoA 2026_22 2.1,2026-05-21,2026,2026,5142500000,"{{""2026"":5142500000}}",,active,,Wage cost policy,Evaluate incidence,{src},strong,SS>reductions,tick677',
    f'cmt_zuidertoren_rsz_177m,Zuidertoren reno from RSZ reserves 177.7m,rsz,RSZ building stock,CoA 2026_22 2.1.2,2026-05-21,2026,2031,177700000,"{{""2026_study"":2500000}}",,active,,Reserve asset sales,Align sale year,{src},strong,SS>RSZ>zuidertoren,tick677',
    f'cmt_dual_ss_receipts_tick677,Dual SS near-balance 148bn rec vs exp,gg_belgium,SS+E2 dual,CoA SS dual,2026-05-21,2026,2026,148002400000,"{{""2026"":148002400000}}",,active,,Dual residual,Not TE-additive,{src_dual},strong,Belgium>dual>ss_rec,tick677',
]
with (data / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write("\n" + r)

lb_rows = [
    f"lb_ss_rec_148bn_2026,SS consolidated receipts 148.0bn,Federal,ops,SS>receipts,148002400000,0,Strong CoA BC2026 148002.4m near-balance vs exp 148026.6; dual,strong,{src},all insured,SS financing,Primary,5.0,9.0,3,6.50,Unit cost FOI,open,,tick677",
    f"lb_ss_alt_finance_27_6bn_2026,SS alt finance BTW+RV 27.6bn,Federal,ops,SS>alt_finance,27583400000,0,Strong CoA: 19.6bn VAT + 7.9bn RV assign; legal minima hit,strong,{src},taxpayers,Fiscal assign SS,Primary,5.5,8.5,3,6.55,Cash transparency,open,,tick677",
    f"lb_ss_contrib_red_5_14bn_2026,SS contribution reductions 5.14bn,Federal,taxex,SS>reductions,5142500000,0,Strong CoA structural 4.29 + targeted 0.85; werkbonus 1.83,strong,{src},employers employees,Wage cost dual,Primary,6.5,7.5,3,6.65,Evaluate first-hire FOI,open,,tick677",
    f"lb_rsz_gb_deficit_547m_2026,RSZ-GB deficit 547.5m after settle,Federal,ops,SS>RSZ>deficit,547500000,0,Strong CoA: 2025 evenwicht overfinance settle on 2026; capital -59.6,strong,{src},SS employees regime,Balance mechanism,Primary,7.0,6.5,3,6.55,Settlement methodology FOI,open,,tick677",
    f"lb_zuidertoren_rsz_timing_2026,Zuidertoren 2.5m unoffset 2026,Federal,ops,SS>RSZ>zuidertoren,2500000,0,Strong CoA: study spend 2026 asset sale Mar 2027 understates deficit,strong,{src},RSZ,Building reno timing,Primary,7.5,3.5,2,5.95,Align sale year,open,,tick677",
    f"lb_dual_ss_receipts_2026,Dual SS receipts vs exp near-balance,Belgium,ops,Belgium>dual>ss_rec,148002400000,0,Strong dual: rec 148.0 vs exp 148.0 gap ~24m; alt fin dual tax base; not TE-additive,strong,{src_dual},all entities,SS dual residual,Primary dual,6.0,9.0,3,7.05,Cross FOI,open,,tick677",
]
with (data / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write("\n" + r)

# entities — ensure rsz_globaal note if needed (rsz already exists)
ent = data / "entities.csv"
et = ent.read_text(encoding="utf-8")
if "\nrsz_globaal_beheer," not in et:
    with ent.open("a", encoding="utf-8", newline="") as f:
        f.write(
            "\nrsz_globaal_beheer,RSZ-Globaal Beheer,ONSS-Gestion globale,NSSO Global Management employees,agency,rsz,bi,,,CoA SS receipts dots+alt finance perimeter; tick677"
        )

gap_id = "gap_fed_aju2026_ss_receipts_l5"
foi_row = (
    f"{gap_id},Federal>Aju2026>SS_receipts_L5,sec_ss,"
    "RSZ contribution L5 by sector private/public/local; structural vs targeted reduction beneficiary lists; Plusplannen/horeca/CAD/overtime yield re-est after July start; evenwichtsdotatie 2025 settle methodology 547.5; alt finance monthly cash BTW/RV; Zuidertoren asset sale calendar; bijzondere bijdrage 2025-26 actuals,"
    "CoA SS receipts residual strong tick677; near-balance dual exp,"
    "5,FOD Sociale Zekerheid / RSZ / RSVZ / FOD Financiën,"
    "openbaarheid@socialsecurity.fgov.be,https://socialsecurity.belgium.be,"
    f"docs/doge/foi/drafts/{gap_id}.md,ready,2026-08-01,,,,,"
    "cmt_ss_rec_matrix_148bn|cmt_ss_alt_finance_27583m|cmt_rsz_evenwicht_dots_8656m,"
    "lb_ss_rec_148bn_2026|lb_ss_alt_finance_27_6bn_2026|lb_rsz_gb_deficit_547m_2026,"
    f"{utc},{utc},tick677 CoA fed SS receipts primary; human send only"
)
with (data / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + foi_row)

# research_queue
rq = data / "research_queue.csv"
lines = rq.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_668,"):
        out.append(
            "rq_668,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,sec_federal,"
            "Next residual: SS receipts residual CoA 2026_22 or VL BA fonds residual or fed nonfiscal SFPIM dual.,,"
            f"2026-08-01T10:45:00Z,{utc},"
            "tick677 SS rec 148.0bn alt 27.6bn evenwicht 5.45bn Zuidertoren dual; FOI gap_fed_aju2026_ss_receipts_l5 ready"
        )
    else:
        out.append(line)
out.append(
    "rq_669,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,sec_ss,"
    "Next residual: VL BA fonds residual CoA 2026_28 or fed nonfiscal SFPIM dual or SS other receipts L5.,,"
    f"{utc},,spawned tick677 after rq_668"
)
rq.write_text("\n".join(out) + "\n", encoding="utf-8")

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_668,677,no,"
    "tick677 SS rec 148.0bn alt 27.6bn dots 8.66bn evenwicht settle 547m dual; next rq_669; progress@680 in 3; rq_116 deferred\n",
    encoding="utf-8",
)

draft = f"""# FOI draft — {gap_id}

**gap_id:** `{gap_id}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Rekenhof Commentaar aanpassing staatsbegroting 2026 (2026_22) Deel III Hoofdstuk I Ontvangsten

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: FOD Sociale Zekerheid / RSZ / RSVZ
Cc: FOD Financiën (alternatieve financiering)
openbaarheid@socialsecurity.fgov.be

Betreft: Openbaarheid — aju 2026 ontvangsten sociale zekerheid (148,0 mld) L5

Geachte,

Op grond van de wet van 11 april 1994 verzoek ik om:

1. **Geconsolideerde ontvangsten 148.002,4 mEUR**: detailmatrix per stelsel
   (RSZ-GB, RSVZ-GB, RIZIV-GV, buiten GB, overheidspensioenen) en
   vergelijking IB vs BC 2026.
2. **Sociale bijdragen 85.328 mEUR / RSZ 69.474,7 mEUR**: uitsplitsing
   privé / overheid / lokale overheden; impact loonmassa + spilindex
   (november vs juni 2026).
3. **Bijdrageverminderingen 5.142,5 mEUR**: structureel 4.294,1 (werkbonus
   1.827,3 + structureel 2.419,5) en gericht 848,4 (eerste aanwervingen
   512,5; loonplafond 58,2) — top begunstigden / sectoren indien openbaar.
4. **Rendementen maatregelen 2026**: Plusplannen, horeca/CAD (11,3 i.p.v. 28),
   sporters loonplafond (10), vrijwillige overuren (kost 32,3) — herschatting
   na inwerkingtreding 1 juli 2026.
5. **Dotaties RSZ-GB 8.656,1 mEUR**: evenwichtsdotatie 5.446,2; afrekening
   overfinanciering 2025 **547,5 mEUR** (incl. kapitaal −59,6) — methodenota.
6. **Alternatieve financiering 27.583,4 mEUR**: maandelijkse cash BTW
   (19.634,7) en roerende voorheffing (7.948,7) naar RSZ/RSVZ; wettelijke
   minima vs %-toewijzing.
7. **Zuidertoren**: studie 2,5 mEUR 2026 en kalender verkoop financiële
   activa (compensatie initieel 2026, pad maart 2027).

Publieke steun: Rekenhof, *Commentaar … staatsbegroting 2026* (2026_22),
Deel III, Hoofdstuk I Ontvangsten van de sociale zekerheid.

Met vriendelijke groeten,
[Naam — menselijke afzender]
```

## Notes

- Do **not** send as agent; human only.
- Complements `gap_fed_aju2026_ss_riziv_ao_l5` (expenditure side).
- Dual: near-balance rec 148002.4 vs exp 148026.6.
- Tick 677.
"""
(root / "docs/doge/foi/drafts" / f"{gap_id}.md").write_text(draft, encoding="utf-8")

entry = f"""
### {utc} — tick {tick}
- Unit: **rq_668** (FOI-adjacent dual residual — **federal CoA BA2026 SS receipts matrix dual**)
- Found (primary CoA 2026_22 Deel III Ch I):
  - **SS consol rec EUR148.002bn** (−14.8 vs IB): bijdragen **85.328** (−197) · toelagen **27.444** (−235) · alt fin **27.583** (+362) · other **7.647**
  - **RSZ contrib 69.475** (−117); OISZ direct FPD **59.4** Fedris **23.2** RIZIV **0.6**
  - **Reductions 5.143** (struct **4.294** werkbonus **1.827** / targeted **848** first-hires **512.5** ceiling **58.2**)
  - **Gov dots RSZ-GB 8.656** (evenwicht **5.446** globale **2.684** specifiek **209** deelstaat **317**); 2025 overfinance settle **−547.5** → GB deficit
  - **Alt fin:** BTW **19.635** + RV **7.949**; RSZ **23.711** RSVZ **3.872**; assign total **27.686** (+361)
  - Residual: horeca/CAD yield **11.3** not 28; overtime cost **32.3**; Zuidertoren study **2.5** unoffset 2026; path cuts 2028 bijzondere **−415** werkbonus **−357.5**
  - Near-balance vs exp **148.027** gap **~24m**. Dual E2. Strong CoA; L5 FOI.
- Wrote: budgets (+50); commitments (+6); leaderboard (+6); sources (+2); entity rsz_globaal_beheer; FOI draft **gap_fed_aju2026_ss_receipts_l5**; rq_668=done; spawn **rq_669**; loop_state ticks=677
- FOI opened: gap_fed_aju2026_ss_receipts_l5 — ready (not sent)
- Next: rq_669; progress@680 in 3 ticks; rq_116 deferred
"""
with (root / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(entry)

print("OK tick677")
print("budgets", len(bud_rows), "cmt", len(cmt_rows), "lb", len(lb_rows))

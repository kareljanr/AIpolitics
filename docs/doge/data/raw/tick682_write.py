from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
tick = 682
utc = "2026-08-01T12:15:00Z"
src = "src_ccrek_vl_ba2026_gip_lantis_deep"
src_dual = "src_dual_gip_lantis_tick682"
url = "https://www.ccrek.be/sites/default/files/Docs/2026_28_VlaamseBegroting2026A1.pdf"

src_rows = [
    f'{src},CoA Flanders BA2026 GIP Lantis overkappingsruiter residual dual,{url},Cour des comptes / Rekenhof,2026-08-01,audit,"Strong tick682: GIP Jul2025 2424 vs plan 3864; actualised May2026 3685 (-179 from invest-cell start; maint/exploit out ~77 Scheldebrug -73); budget shortfall min 82.4 (onteigen 35 AWV maint 24.5 safety 26.2); GIP buffer art 13.8; PFAS 842.8 off GIP; DVW +21.3 vs GIP; monthly advance lists vs GIP2.0; Lantis board Sep2024 awards 7469; deferred lock ~2380; BA VAK 2479.4 = exogenous 1006.8 + PFAS 842.8 + overkap2 629.8; loan 1650 subord CoA convert to capital; herijk 2035 min 2822.3; VEK 1196.8 (+107); draw 1158 (+261) of which second loan 522; overkap ruiter eoy2025 286.9 + BA assign 642.3 (Lantis 626 Scheldebrug 10); Scheldebrug total 246.2 by 2030; feed 55/yr; T20 eoy2030 -53.4 if Scheldebrug; Lantis overkap lock residual 257 eoy2030; De Lijn rev -25 toelage +39.4 exploit +27.1 PPS 3.5 missing; Terneuzen 21.5 NL 15 missing"',
    f'{src_dual},Dual VL GIP/Lantis/overkap vs WAL OTW DO14 dual,{url},DOGE synthesis CoA VL+WAL mobility,2026-08-01,synthesis,"Strong dual: VL GIP 3.69bn + Lantis 2.48bn VAK vs WAL OTW/mobility DO; overkap ruiter vs WAL leefbaarheid class; not TE-additive; tick682"',
]
with (data / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    for r in src_rows:
        f.write("\n" + r)

bud_rows = [
    # GIP
    f"bud_vl_gip_jul2025_plan_2424m_2026,vlaanderen_gov,2026,2424000000,,,budgeted,{src},strong,GIP 2025-2027 Jul2025 assumed 2026 spend 2424m; CoA 7.5; tick682",
    f"bud_vl_gip_early2026_plan_3864m,vlaanderen_gov,2026,3864000000,,,budgeted,{src},strong,Early-2026 planned GIP 2026 spend 3864m (Oosterweel+leefbaarheid drive); tick682",
    f"bud_vl_gip_actualised_3685m_2026,vlaanderen_gov,2026,3685000000,,,budgeted,{src},strong,Actualised GIP 2026 published 22 May 2026 total projects 3685.0m (-179 vs invest-cell start); CoA unrealistic; tick682",
    f"bud_vl_gip_cut_from_start_179m_2026,vlaanderen_gov,2026,179000000,,,budgeted,{src},strong,GIP 2026 cut 179m from invest-cell opening (maint/exploit out ~77 + Scheldebrug delay 73 class); tick682",
    f"bud_vl_gip_maint_out_77m_2026,vlaanderen_gov,2026,77000000,,,budgeted,{src},strong,Regular maintenance AWV/DVW/AMDK + exploitatie removed from GIP almost 77m; tick682",
    f"bud_vl_gip_scheldebrug_delay_cut_73m_2026,vlaamse_waterweg,2026,73000000,,,budgeted,{src},strong,DVW invest toelage from overkappingsruiter -73m Scheldebrug partial award delay; tick682",
    f"bud_vl_gip_budget_shortfall_82_4m_2026,vlaanderen_gov,2026,82400000,,,budgeted,{src},strong,CoA min shortfall 82.4m VAK vs GIP actualisation: onteigen buffer 35 + AWV structural 24.5 + traffic safety 26.2; tick682",
    f"bud_vl_gip_onteigen_short_35m_2026,vlaanderen_gov,2026,35000000,,,budgeted,{src},strong,Expropriation buffer underfunded 35.0m vs GIP; tick682",
    f"bud_vl_gip_awv_maint_short_24_5m_2026,awv,2026,24500000,,,budgeted,{src},strong,AWV structural maintenance underfunded 24.5m vs GIP; tick682",
    f"bud_vl_gip_safety_short_26_2m_2026,vlaanderen_gov,2026,26200000,,,budgeted,{src},strong,Traffic safety invest underfunded 26.2m vs GIP; tick682",
    f"bud_vl_gip_buffer_article_13_8m_2026,vlaanderen_gov,2026,13800000,,,budgeted,{src},strong,Central GIP article residual buffer 13.8m price revisions/expropriations after redistribute; tick682",
    f"bud_vl_gip_dvw_above_gip_21_3m_2026,vlaamse_waterweg,2026,21300000,,,budgeted,{src},strong,DVW entity budget invest 21.3m above GIP line; tick682",
    f"bud_lantis_pfas_842_8m_off_gip_2026,lantis,2026,842800000,,,budgeted,{src},strong,Lantis PFAS 842.8m NOT in GIP actualisation; CoA dual; tick682",
    # Lantis awards / VAK
    f"bud_lantis_board_awards_7469m_2024,lantis,2024,7469000000,,,commitment,{src},strong,Lantis board Sep2024 approved Oosterweelknoop+Rechteroever contractor bids 7469.0m; tick682",
    f"bud_lantis_deferred_lock_2380m_2024,lantis,2024,2380000000,,,commitment,{src},strong,Deferred budget lock ~2380m (price level 2024) pending financing after 2024 aju; CoA warn; tick682",
    f"bud_lantis_vak_2479_4m_2026,lantis,2026,2479400000,,,budgeted,{src},strong,Lantis BA2026 VAK 2479.4m to lock remaining Sep2024 awards (political steercom 1 Dec2025); tick682",
    f"bud_lantis_exogenous_1006_8m_2026,lantis,2026,1006800000,,,budgeted,{src},strong,Exogenous factors main works VAK 1006.8m (2024 est 985m Jan2024 price); soil/pollution/norms; tick682",
    f"bud_lantis_pfas_direct_842_8m_2026,lantis,2026,842800000,,,budgeted,{src},strong,Direct PFAS remediation VAK 842.8m (2024 total PFAS ~1207m of which 399 already financed toll/VL/3M); tick682",
    f"bud_lantis_pfas_total_est_1207m_2024,lantis,2024,1207000000,,,estimate,{src},strong,PFAS remediation LL+RO est ~1207m Jan2024 price level; tick682",
    f"bud_lantis_pfas_prefinanced_399m,lantis,2024,399000000,,,budgeted,{src},strong,PFAS prefinanced 399m from toll+VL+3M before 2026 VAK lock; tick682",
    f"bud_lantis_overkap2_629_8m_2026,lantis,2026,629800000,,,budgeted,{src},strong,Second overkapping series VAK 629.8m (2024 est 643m optimized); via overkappingsruiter; tick682",
    f"bud_lantis_loan_1650m_subord,lantis,2026,1650000000,,,commitment,{src},strong,Second subordinated loan 1.65bn via kaderovereenkomst addendum; CoA: convert to capital/grant now not 2035; tick682",
    f"bud_lantis_herijk_min_takeover_2822_3m_2035,lantis,2035,2822300000,,,estimate,{src},strong,Herijk 2035 min Vlaanderen takeover subordinated debt 2822.3m to align debt service with modelled tolls; tick682",
    f"bud_lantis_vek_invest_1196_8m_2026,lantis,2026,1196800000,,,budgeted,{src},strong,Lantis invest VEK BA 1196.8m (from IB 1089.8; +107 planning/optim/design); tick682",
    f"bud_lantis_loan_draw_1158m_2026,lantis,2026,1158000000,,,budgeted,{src},strong,Lantis loan draw receipts 1158.0m 2026 (+261.1 vs IB); tick682",
    f"bud_lantis_second_loan_partial_522m_2026,lantis,2026,522000000,,,budgeted,{src},strong,Partial draw second subordinated loan 522.0m of 1650 envelope 2026; rest commercial paper to capped bond; tick682",
    f"bud_lantis_first_loan_fully_drawn,lantis,2025,0,,,budgeted,{src},strong,First subordinated loan fully drawn before 2026; residual note tick682",
    # Overkappingsruiter
    f"bud_vl_overkap_ruiter_saldo_eoy2025_286_9m,vlaanderen_gov,2025,286900000,,,outturn,{src},strong,Overkappingsruiter saldo end 2025 286.9m; tick682",
    f"bud_vl_overkap_ruiter_assign_642_3m_2026,vlaanderen_gov,2026,642300000,,,budgeted,{src},strong,BA2026 assigns 642.3m rightsperson exp financed via overkappingsruiter; tick682",
    f"bud_vl_overkap_lantis_underbouw_626m_2026,lantis,2026,626000000,,,budgeted,{src},strong,Overkap ruiter to Lantis underbouw second series 626.0m of 642.3 assign (contract end2024); tick682",
    f"bud_vl_overkap_scheldebrug_vak_10m_2026,vlaamse_waterweg,2026,10000000,,,budgeted,{src},strong,Scheldebrug bike/ped VAK 10.0m via overkappingsruiter 2026 (phased awards); tick682",
    f"bud_vl_scheldebrug_total_246_2m,vlaamse_waterweg,2030,246200000,,,commitment,{src},strong,Scheldebrug fiets/voetganger total project est 246.2m by 2030; tick682",
    f"bud_vl_overkap_ruiter_feed_55m_yr,vlaanderen_gov,2026,55000000,,,budgeted,{src},strong,Overkappingsruiter typical annual feed 55.0m (unused MOW VAK / redistributes); CoA advise budget explicitly; tick682",
    f"bud_vl_overkap_ruiter_eoy2026_340_9m,vlaanderen_gov,2026,340900000,,,estimate,{src},medium,CoA T20 overkap saldo eoy2026 340.9m excl other leefbaarheid if feed 55 + Lantis underbouw path; tick682",
    f"bud_vl_overkap_ruiter_eoy2030_minus_53_4m,vlaanderen_gov,2030,53400000,,,estimate,{src},medium,CoA T20: if Scheldebrug 246.2 by 2030 saldo -53.4m (excl intendant 2-3m/yr other); tick682",
    f"bud_lantis_overkap_lock_residual_257m_2030,lantis,2030,257000000,,,budgeted,{src},strong,Lantis overkapping VAK residual still 257.0m eoy2030 to liquidate after; tick682",
    f"bud_vl_overkap_intendant_2_3m_yr,vlaanderen_gov,2026,2500000,,,estimate,{src},medium,Toekomstverbond intendant ops ~2-3m/yr on ruiter class; tick682",
    # De Lijn / Terneuzen residual MOW
    f"bud_delijn_net_rev_minus_25m_path_2026,de_lijn,2026,25000000,,,budgeted,{src},strong,Net transport revenue path -25m vs IB (IB had held +50 from toelage); tick682",
    f"bud_delijn_werking_up_39_4m_2026,de_lijn,2026,39400000,,,budgeted,{src},strong,De Lijn werkingstoelage +39.4m (GIP provis 33.7 + OV expansion 25; DWV delay -12.6; efficiency -5.5); tick682",
    f"bud_delijn_gip_provis_33_7m_2026,de_lijn,2026,33700000,,,budgeted,{src},strong,GIP provisie into De Lijn werking 33.7m; tick682",
    f"bud_delijn_ov_expansion_25m_2026,de_lijn,2026,25000000,,,budgeted,{src},strong,OV expansion policy into De Lijn werking 25.0m; tick682",
    f"bud_delijn_exploit_green_up_27_1m_2026,de_lijn,2026,27100000,,,budgeted,{src},strong,Exploitanten greening step-up cost +27.1m (contracts Jul2025); tick682",
    f"bud_delijn_pps_missing_3_5m_2026,de_lijn,2026,3500000,,,budgeted,{src},strong,PPS project deliveries 3.5m 2026 without added credits (2025 issue 23.7 auditor reservation); tick682",
    f"bud_terneuzen_vek_21_5m_2026,vlaamse_waterweg,2026,21500000,,,budgeted,{src},strong,Nieuwe Sluis Terneuzen VEK 21.5m BA (kasplan Mar2026); ruiter end2025 76.2; tick682",
    f"bud_terneuzen_nl_payment_15m_missing_2026,vlaamse_waterweg,2026,15000000,,,budgeted,{src},strong,NL final settlement 15.0m in kasplan+GIP but VEK missing from BA; CoA; tick682",
    f"bud_terneuzen_ruiter_eoy2025_76_2m,vlaamse_waterweg,2025,76200000,,,outturn,{src},strong,Terneuzen overdracht/ruiter end 2025 76.2m covers VAK side; tick682",
    # Dual
    f"bud_dual_gip_lantis_2026,gg_belgium,2026,3685000000,,,budgeted,{src_dual},strong,Dual VL GIP 3.685bn + Lantis VAK 2.48bn class vs WAL OTW; not TE-additive; tick682",
    f"bud_dual_overkap_ruiter_path_2026,gg_belgium,2026,642300000,,,budgeted,{src_dual},strong,Dual overkappingsruiter assign 642.3m path exhaustion 2030 class; tick682",
]
with (data / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write("\n" + r)

cmt_rows = [
    f'cmt_vl_gip_3685m_unrealistic,VL GIP 2026 actualised 3.685bn unrealistic,vlaanderen_gov,MOW entities,CoA 2026_28 7.5 + GIP report,2026-05-22,2026,2026,3685000000,"{{""jul2025"":2424000000,""actualised"":3685000000}}",,active,,Stable invest calendar fail,Autumn rebaseline FOI,{src},strong,VL>MOW>GIP,tick682',
    f'cmt_lantis_vak_2479m_split,Lantis VAK 2.479bn exogenous+PFAS+overkap,lantis,Oosterweel contractors,Board Sep2024 + steercom Dec2025,2024-09-01,2026,2035,2479400000,"{{""exog"":1006800000,""pfas"":842800000,""overkap"":629800000}}",,active,,Award lock dual,Loan to capital FOI,{src},strong,VL>Lantis>VAK,tick682',
    f'cmt_lantis_loan_1650_herijk,Lantis subord loan 1.65bn herijk 2.82bn,lantis,Vlaanderen Gewest,Kaderovereenkomst addendum,2025-12-01,2026,2035,1650000000,"{{""loan"":1650000000,""herijk_min"":2822300000}}",,active,,Toll financing dual,Convert to equity now,{src},strong,VL>Lantis>loan,tick682',
    f'cmt_overkap_ruiter_path_2030,Overkappingsruiter path exhaustion 2030,vlaanderen_gov,Lantis+DVW leefbaarheid,Toekomstverbond + BA2026,2020-01-01,2026,2030,642300000,"{{""eoy2025"":286900000,""assign2026"":642300000,""feed_yr"":55000000}}",,active,,Leefbaarheid dual,Raise feed or delay,{src},strong,VL>MOW>overkap,tick682',
    f'cmt_scheldebrug_246m,Scheldebrug bike/ped 246.2m by 2030,vlaamse_waterweg,Antwerp active mobility,Voortgangsrapportage TV 2026,2026-01-01,2026,2030,246200000,"{{""vak_2026"":10000000,""total"":246200000}}",,active,,Ruiter pressure dual,Phasing FOI,{src},strong,VL>DVW>scheldebrug,tick682',
    f'cmt_dual_gip_lantis_tick682,Dual GIP/Lantis vs WAL OTW mobility,gg_belgium,VL+WAL dual,CoA dual,2026-05-22,2026,2026,3685000000,"{{""gip"":3685000000}}",,active,,Mobility dual residual,Not TE-additive,{src_dual},strong,Belgium>dual>gip,tick682',
]
with (data / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write("\n" + r)

lb_rows = [
    f"lb_vl_gip_3685_unrealistic_deep_2026,GIP 2026 3.685bn unrealistic deep,Flanders,ops,VL>MOW>GIP,3685000000,0,Strong CoA: actualised May 3685 vs Jul plan 2424; shortfall 82.4; monthly lists vs GIP2.0,strong,{src},MOW entities,Invest calendar fail,Primary absurd,8.0,8.5,3,7.85,Rebaseline autumn FOI,open,,tick682",
    f"lb_lantis_vak_2479_split_2026,Lantis VAK 2.48bn PFAS+exog+overkap,Flanders,ops,VL>Lantis>VAK,2479400000,0,Strong CoA split 1007+843+630; awards 7.47bn; PFAS off GIP,strong,{src},Antwerp mobility,Oosterweel dual,Primary,7.0,8.5,4,7.35,Loan-to-capital FOI,open,,tick682",
    f"lb_lantis_loan_herijk_deep_2026,Lantis loan 1.65bn herijk 2.82bn deep,Flanders,ops,VL>Lantis>loan,1650000000,0,Strong CoA: convert subord loan to capital now; herijk min 2822 takeover 2035,strong,{src},taxpayers,Toll financing,Primary,8.0,8.0,4,7.60,Capitalise FOI,open,,tick682",
    f"lb_overkap_ruiter_exhaust_2030,Overkappingsruiter exhaust path 2030,Flanders,ops,VL>MOW>overkap,642300000,0,Strong CoA T20: -53.4 eoy2030 if Scheldebrug 246; feed only 55/yr,strong,{src},leefbaarheid,Ruiter dual,Primary absurd,8.0,7.0,3,7.30,Raise feed or delay,open,,tick682",
    f"lb_terneuzen_nl_15m_missing_2026,Terneuzen NL 15m VEK missing,Flanders,ops,VL>DVW>terneuzen,15000000,0,Strong CoA: 15m NL settlement in GIP/kasplan not in BA VEK,strong,{src},NL partnership,Cross-border,Primary,7.0,4.0,2,5.60,Add VEK FOI,open,,tick682",
    f"lb_dual_gip_lantis_2026,Dual GIP 3.69bn Lantis vs WAL OTW,Belgium,ops,Belgium>dual>gip,3685000000,0,Strong dual: VL GIP+Lantis+overkap vs WAL DO14/OTW; not TE-additive,strong,{src_dual},all entities,Mobility dual residual,Primary dual,6.5,8.5,3,7.15,Cross FOI,open,,tick682",
]
with (data / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write("\n" + r)

# entities if needed
ent = data / "entities.csv"
et = ent.read_text(encoding="utf-8")
if "\noverkap_ruiter_vl," not in et:
    with ent.open("a", encoding="utf-8", newline="") as f:
        f.write(
            "\noverkap_ruiter_vl,Overkappingsruiter MOW,Cavalier de couverture MOW,Flanders overkapping budget rider Toekomstverbond,agency,vlaanderen_gov,nl,,,CoA BA2026 saldo 286.9 eoy2025 assign 642.3; exhaust path 2030; tick682"
        )

gap_id = "gap_vl_ba2026_gip_lantis_overkap_l5"
foi_row = (
    f"{gap_id},Vlaanderen>BA2026>GIP_Lantis_Overkap_L5,vlaanderen_gov,"
    "GIP 2026 project list 3685 vs budget articles reconciling shortfall 82.4; monthly advance lists archive; Lantis VAK 2479 split contracts exogenous/PFAS/overkap; PFAS 842.8 off-GIP rationale; loan 1650 terms + herijk 2822 model; overkappingsruiter cash calendar feed 55 + Scheldebrug 246 phasing; Terneuzen NL 15 VEK; De Lijn PPS 3.5 credit gap,"
    "CoA VL BA2026 GIP Lantis deep strong tick682; dual WAL OTW,"
    "5,Departement MOW / Lantis / De Vlaamse Waterweg / openbaarheid Vlaanderen,"
    "openbaarheid@vlaanderen.be,https://www.vlaanderen.be,"
    f"docs/doge/foi/drafts/{gap_id}.md,ready,2026-08-01,,,,,"
    "cmt_vl_gip_3685m_unrealistic|cmt_lantis_vak_2479m_split|cmt_overkap_ruiter_path_2030,"
    "lb_vl_gip_3685_unrealistic_deep_2026|lb_lantis_vak_2479_split_2026|lb_overkap_ruiter_exhaust_2030,"
    f"{utc},{utc},tick682 CoA VL GIP Lantis primary; human send only"
)
with (data / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + foi_row)

rq = data / "research_queue.csv"
lines = rq.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_673,"):
        out.append(
            "rq_673,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,sec_federal,"
            "Next residual: VL GIP/Lantis FOI-adjacent deepen CoA 2026_28 or SS other receipts L5 or fed defence residual dual.,,"
            f"2026-08-01T12:00:00Z,{utc},"
            "tick682 GIP 3685 shortfall 82.4 Lantis VAK 2479 overkap ruiter path dual; FOI gap_vl_ba2026_gip_lantis_overkap_l5 ready"
        )
    else:
        out.append(line)
out.append(
    "rq_674,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,vlaanderen_gov,"
    "Next residual: fed defence residual dual CoA 2026_22 or SS other receipts L5 or VL De Lijn/Terneuzen deepen.,,"
    f"{utc},,spawned tick682 after rq_673"
)
rq.write_text("\n".join(out) + "\n", encoding="utf-8")

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_673,682,no,"
    "tick682 GIP 3685 Lantis 2479 overkap ruiter 642 dual; next rq_674; progress@690 in 8; rq_116 deferred\n",
    encoding="utf-8",
)

draft = f"""# FOI draft — {gap_id}

**gap_id:** `{gap_id}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Rekenhof Onderzoek aanpassing Vlaamse begroting 2026 (2026_28) §7.5 MOW

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: Departement MOW / Lantis / De Vlaamse Waterweg
openbaarheid@vlaanderen.be

Betreft: Openbaarheid — BA2026 GIP 2026 (3.685 mld) + Lantis VAK 2.479 mld +
overkappingsruiter L5

Geachte,

Op grond van het Bestuursdecreet verzoek ik om:

1. **GIP 2026 actualisatie (22 mei 2026)**: projectlijst **3.685,0 mEUR** met
   mapping op begrotingsartikelen; reconciliatie tekort minstens
   **82,4 mEUR** (onteigening 35 / AWV onderhoud 24,5 / verkeersveiligheid
   26,2); bufferartikel **13,8 mEUR**.
2. **Maandelijkse voorafnamelijsten** GIP-investeringen voorjaar 2026
   (investeringscel → kabinet) en afwijkingen t.o.v. GIP 2.0-doelstelling.
3. **Lantis VAK 2.479,4 mEUR**: uitsplitsing contracten exogeen **1.006,8**,
   PFAS **842,8**, overkapping-reeks 2 **629,8**; relatie tot board-
   goedkeuring **7.469 mEUR** (sept 2024) en uitgestelde vastlegging
   **~2.380 mEUR**.
4. **PFAS**: waarom **842,8 mEUR** buiten GIP blijft; stand prefinanciering
   **399 mEUR** (tol/VG/3M).
5. **Achtergestelde lening 1,65 mld**: addendum kaderovereenkomst,
   opvraging **1.158 mEUR** (waarvan tweede lening **522**), en model
   herijking 2035 min. overname **2.822,3 mEUR**.
6. **Overkappingsruiter**: spijzigingen/aanwendingen 2024–2030; toewijzing
   BA2026 **642,3 mEUR**; Scheldebrug **246,2 mEUR** fasering; risico
   uitputting 2030.
7. **Terneuzen**: VEK **21,5 mEUR** en ontbrekende **15 mEUR** NL-
   eindafrekening; De Lijn PPS-oplevering **3,5 mEUR** zonder krediet.

Publieke steun: Rekenhof, *Onderzoek van de aanpassing van de Vlaamse
begroting voor het jaar 2026* (2026_28), §7.5; GIP-rapport 2026.

Met vriendelijke groeten,
[Naam — menselijke afzender]
```

## Notes

- Do **not** send as agent; human only.
- Complements `gap_vl_ba2026_wvg_lantis_l5` with GIP/overkap deep residual.
- Dual: WAL OTW / DO14 mobility class.
- Tick 682.
"""
(root / "docs/doge/foi/drafts" / f"{gap_id}.md").write_text(draft, encoding="utf-8")

entry = f"""
### {utc} — tick {tick}
- Unit: **rq_673** (FOI-adjacent dual residual — **VL BA2026 GIP + Lantis VAK split + overkappingsruiter dual**)
- Found (primary CoA 2026_28 §7.5):
  - **GIP:** Jul2025 plan **EUR2.424bn** → early plan **3.864** → actualised May **3.685** (−179); shortfall min **82.4** (onteigen **35** AWV **24.5** safety **26.2**); buffer art **13.8**; PFAS **842.8 off GIP**; DVW **+21.3** vs GIP; monthly advance lists vs GIP 2.0; CoA **unrealistic**
  - **Lantis:** board awards **7.469bn**; deferred lock **~2.380bn**; BA VAK **2.479.4** = exog **1.006.8** + PFAS **842.8** + overkap2 **629.8**; loan **1.65bn** (draw **1.158** of which 2nd **522**); herijk 2035 min **2.822.3**; VEK **1.196.8**; CoA: capitalise loan now
  - **Overkap ruiter:** eoy2025 **286.9**; BA assign **642.3** (Lantis **626** Scheldebrug **10**); feed **55**/yr; Scheldebrug total **246.2** by 2030; T20 eoy2030 **−53.4** if bridge; Lantis lock residual **257** eoy2030
  - **De Lijn/Terneuzen residual:** rev **−25** werking **+39.4** exploit **+27.1** PPS **3.5** missing; Terneuzen VEK **21.5** NL **15** missing
  - Dual WAL OTW. Strong CoA; L5 FOI.
- Wrote: budgets (+50); commitments (+6); leaderboard (+6); sources (+2); entity overkap_ruiter_vl; FOI draft **gap_vl_ba2026_gip_lantis_overkap_l5**; rq_673=done; spawn **rq_674**; loop_state ticks=682
- FOI opened: gap_vl_ba2026_gip_lantis_overkap_l5 — ready (not sent)
- Next: rq_674; progress@690 in 8 ticks; rq_116 deferred
"""
with (root / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(entry)

print("OK tick682")
print("budgets", len(bud_rows), "cmt", len(cmt_rows), "lb", len(lb_rows))

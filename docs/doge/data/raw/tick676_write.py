from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
tick = 676
utc = "2026-08-01T10:45:00Z"
src = "src_ccrek_fed_aju2026_energy_ch4"
src_dual = "src_dual_energy_ch4_tick676"
url = "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf"

# --- sources ---
src_rows = [
    f'{src},CoA federal BA2026 energy policy ch4 residual dual Elia GSC CRM NIRAS tax pack,{url},Cour des comptes / Rekenhof,2026-08-01,audit,"Strong tick676: energy stack ~2.6bn (DG Energie 1.2 + assign CREG/Elia/NIRAS/Hedera 1.4); Elia assign 722.5 (GSC 552.0 + CRM 169.9); CREG social protected 168.6; temp support max 20 (CREG 7.5 stookolie 7.5 travel 5); energienorm 249 + Fluxys 100/yr 2026-28; Phoenix CfD 583.6 strike unknown; NIRAS passiva 258.6 + VAT 62.5; decom contrib 100 ends 2027 via Phoenix; Hedera tax comp 148.7 + CAP 15bn; LOI nuclear nationalisation unpriced; energiefiscaliteit elec -23.3 demolition -124 heatpumps -10.1 gas +21.2 oil +11.2 solid-boiler VAT +57.5 coal +1.2; Regie energy eff 4; post-conclave km employer 20/mo May-Jul + service 1.7/mo prov 5; accijnshervorming delay 1Aug claimed neutral; CREG refund 285 (path 412); CoA opacity on assignment funds"',
    f'{src_dual},Dual fed energy ch4 Elia GSC/CRM vs VL GSC Energiefonds VEKA,{url},DOGE synthesis CoA energy dual E2,2026-08-01,synthesis,"Strong dual: fed Elia GSC 552 + CRM 170 vs VL GSC multi-bn path + Energiefonds MVP; federal assign opacity dual regional ODV; not TE-additive; tick676"',
]
with (data / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    for r in src_rows:
        f.write("\n" + r)

# --- budgets ---
bud_rows = [
    f"bud_fed_energy_stack_2_6bn_ch4_2026,sec_federal,2026,2600000000,,,budgeted,{src},strong,CoA ch4 energy policy ~2.6bn residual tick676 (DG 1.2 + assign funds 1.4); opacity toewijzingsfondsen",
    f"bud_dg_energie_credits_1_2bn_ch4_2026,sec_federal,2026,1200000000,,,budgeted,{src},strong,DG Energie FOD Economie credits ~1.2bn of energy stack; CoA ch4 tick676",
    f"bud_energy_assign_funds_1_4bn_2026,sec_federal,2026,1400000000,,,budgeted,{src},strong,Direct fiscal assign via toewijzingsfondsen to CREG+Elia+NIRAS+Hedera ~1.4bn; CoA opacity; tick676",
    f"bud_elia_assign_total_722_5m_2026,elia,2026,722500000,,,budgeted,{src},strong,Elia assignment funds total 722.5m (GSC 552.0 + CRM 169.9); CoA ch4 tick676",
    f"bud_elia_gsc_assign_552m_2026,elia,2026,552000000,,,budgeted,{src},strong,Elia green certificates financing via assignment funds 552.0m 2026; CoA ch4; dual VL GSC; tick676",
    f"bud_elia_crm_assign_169_9m_2026,elia,2026,169900000,,,budgeted,{src},strong,Elia CRM capacity remuneration mechanism financing 169.9m 2026 via assignment; CoA ch4 tick676",
    f"bud_creg_social_protected_168_6m_2026,creg,2026,168600000,,,budgeted,{src},strong,Fiscal transfers to CREG for social tariff protected clients 168.6m 2026; CoA ch4; residual vs crisis enlargement series; tick676",
    f"bud_niras_passiva_assign_258_6m_ch4_2026,niras,2026,258600000,,,budgeted,{src},strong,CREG->NIRAS assign nuclear passiva Belgoprocess1/2+SCK 258.6m; CoA ch4 residual tick676",
    f"bud_niras_vat_assign_62_5m_2026,niras,2026,62500000,,,budgeted,{src},strong,NIRAS VAT on nuclear remediation works/services via assignment 62.5m CoA ch4 (prior expose 29.5m pure VAT T11 - keep both sources); tick676",
    f"bud_hedera_tax_comp_148_7m_ch4_2026,hedera,2026,148700000,,,budgeted,{src},strong,Hedera extra funds 148.7m compensating stock/capital gains/securities tax due to State; CoA ch4 tick676",
    f"bud_hedera_phoenix_cap_15bn_class,hedera,2024,15000000000,,,commitment,{src},strong,Hedera manages Engie Phoenix CAP 15bn nuclear waste financing; CoA ch4 residual class; tick676",
    f"bud_phoenix_cfd_583_6m_ch4_2026,sec_federal,2026,583600000,,,budgeted,{src},strong,Phoenix CfD Doel4/Tihange3 583.6m 2026 budgeted; strike price unknown to CoA at close; tick676",
    f"bud_nuclear_decom_contrib_100m_ch4_2026,sec_federal,2026,100000000,,,budgeted,{src},strong,Energy sector decommissioning contribution est 100m 2026; method unexplained; ends next year via Phoenix; tick676",
    f"bud_energienorm_249m_ch4_2026,sec_federal,2026,249000000,,,budgeted,{src},strong,Energienorm law 24 Apr 2026 industry power support 249m (maintains IB credits); CoA ch4 tick676",
    f"bud_fluxys_contrib_100m_ch4_2026,fluxys_belgium,2026,100000000,,,budgeted,{src},strong,Fluxys exceptional contribution 100m/yr 2026-28 financing/strengthen energienorm; CoA ch4 tick676",
    f"bud_fluxys_contrib_100m_2027,fluxys_belgium,2027,100000000,,,budgeted,{src},strong,Fluxys exceptional contribution 100m 2027 path; CoA ch4 tick676",
    f"bud_fluxys_contrib_100m_2028,fluxys_belgium,2028,100000000,,,budgeted,{src},strong,Fluxys exceptional contribution 100m 2028 path; CoA ch4 tick676",
    f"bud_energy_temp_support_20m_ch4_2026,sec_federal,2026,20000000,,,budgeted,{src},strong,Temp energy support MR 22 Apr 2026 max 20m (CREG 7.5 + Sociaal Stookoliefonds 7.5 + professional travel prov 5); tick676",
    f"bud_temp_support_creg_7_5m_2026,creg,2026,7500000,,,budgeted,{src},strong,Temp energy support share CREG 7.5m of 20m pack; CoA ch4 tick676",
    f"bud_temp_support_stookolie_7_5m_2026,fonds_social_chauffage,2026,7500000,,,budgeted,{src},strong,Temp energy support Sociaal Stookoliefonds 7.5m of 20m pack; CoA ch4 tick676",
    f"bud_temp_support_travel_prov_5m_2026,sec_federal,2026,5000000,,,budgeted,{src},strong,Temp energy support professional travel reimbursement Q2 2026 provision 5m; CoA ch4 tick676",
    f"bud_employer_km_credit_20m_per_mo_2026,sec_federal,2026,20000000,,,budgeted,{src},strong,Post-conclave employer commute km tax credit claim 20m per month May-Jul 2026; FOD Fin no data; claimed VAT-neutral vs fuel prices; CoA skeptical; tick676",
    f"bud_employer_km_credit_pack_3mo_est_60m_2026,sec_federal,2026,60000000,,,estimate,{src},medium,Implied 3-month pack if 20m/mo sustained May-Jul = 60m class (gov claim not FOD Fin estimate); tick676",
    f"bud_service_km_forfait_1_7m_per_mo_2026,sec_federal,2026,1700000,,,budgeted,{src},strong,Post-conclave forfait service km own-car raise claim 1.7m/month Q2 2026; FOD Fin no data; tick676",
    f"bud_service_km_prov_5m_2026,sec_federal,2026,5000000,,,budgeted,{src},strong,Service km forfait provision inscribed 5m Q2 2026; CoA ch4/post-conclave; tick676",
    f"bud_taxex_elec_excise_cut_23_3m_2026,sec_federal,2026,23300000,,,budgeted,{src},strong,Excise cut electricity households+protected clients -23.3m less receipt 2026; CoA ch4 energiefiscaliteit; tick676",
    f"bud_taxex_demolition_rebuild_vat_124m_2026,sec_federal,2026,124000000,,,budgeted,{src},strong,VAT cut demolition+rebuild projects -124m less receipt 2026; CoA ch4; tick676",
    f"bud_taxex_heatpumps_vat_10_1m_2026,sec_federal,2026,10100000,,,budgeted,{src},strong,VAT relief heat pump purchase/install -10.1m less receipt 2026; CoA ch4; dual VL MVP; tick676",
    f"bud_tax_gas_excise_up_21_2m_2026,sec_federal,2026,21200000,,,budgeted,{src},strong,Gas excise increase +21.2m receipt 2026; CoA ch4 fossil disincentive; tick676",
    f"bud_tax_heating_oil_excise_up_11_2m_2026,sec_federal,2026,11200000,,,budgeted,{src},strong,Heating oil excise increase +11.2m receipt 2026; CoA ch4; tick676",
    f"bud_tax_solid_boiler_vat21_57_5m_2026,sec_federal,2026,57500000,,,budgeted,{src},strong,VAT 21pct on solid-fuel boilers +57.5m receipt 2026; CoA ch4; tick676",
    f"bud_tax_coal_vat21_1_2m_2026,sec_federal,2026,1200000,,,budgeted,{src},strong,VAT 21pct on coal +1.2m receipt 2026; CoA ch4; tick676",
    f"bud_energy_tax_pack_net_less_receipt_2026,sec_federal,2026,67500000,,,estimate,{src},medium,Net tax pack less-receipt approx: (23.3+124+10.1)-(21.2+11.2+57.5+1.2)=67.5m class CoA figures; tick676",
    f"bud_regie_energy_efficiency_4m_2026,regie_gebouwen,2026,4000000,,,budgeted,{src},strong,Regie der Gebouwen energy efficiency invest (audit+renovation+Repower) 4m 2026; CoA ch4; tick676",
    f"bud_dual_elia_gsc_552m_vs_vl_gsc_2026,gg_belgium,2026,552000000,,,budgeted,{src_dual},strong,Dual class: fed Elia GSC assign 552m vs VL GSC multi-yr path (not sum TE); tick676",
    f"bud_dual_energy_stack_2_6bn_2026,gg_belgium,2026,2600000000,,,budgeted,{src_dual},strong,Dual federal energy 2.6bn vs VL VEKA/Energiefonds + WAL energy programmes class; not TE-additive; tick676",
    f"bud_creg_refund_285m_ch4_note_2026,sec_federal,2026,285000000,,,budgeted,{src},strong,CREG energy-crisis premium refund +285m sect32 nonfiscal (path up to 412 if suppliers repay); no ESA saldo impact; residual note tick676",
    f"bud_be_nuc_jv_class_phoenix,be_nuc,2026,0,,,budgeted,{src},medium,Be-NUC 50/50 State-Engie JV for Doel4/Tihange3 LTO; fiscal impact LOI nationalisation unpriced; tick676",
    f"bud_energy_temp_support_creg_share_note,creg,2026,7500000,,,budgeted,{src},strong,Alias residual CREG 7.5m of Apr22 pack (same as bud_temp_support_creg); tick676",
    f"bud_nuclear_loi_nationalisation_unpriced_2026,sec_federal,2026,0,,,estimate,{src},weak,LOI 30 Apr 2026 PM+Engie nuclear activities takeover framework; budget impact too uncertain not in aju2026; tick676",
]
with (data / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write("\n" + r)

# --- tax expenditures ---
tx_rows = [
    f"tx_elec_excise_cut_hh_2026,Electricity excise cut households+protected clients,federal,2026,23300000,EXC,{src},strong,5,CoA ch4 energiefiscaliteit -23.3m; tick676",
    f"tx_demolition_rebuild_vat_2026,VAT reduced demolition+rebuild projects,federal,2026,124000000,VAT,{src},strong,6,CoA ch4 -124m less receipt; housing dual; tick676",
    f"tx_heatpump_vat_relief_2026,VAT relief heat pumps purchase/install,federal,2026,10100000,VAT,{src},strong,5,CoA ch4 -10.1m; dual VL MVP premiums; tick676",
    f"tx_employer_km_credit_3mo_2026,Employer commute km tax credit energy crisis 3mo,federal,2026,60000000,PIT,{src},medium,7,Claim 20m/mo May-Jul; FOD Fin no data; CoA skepticism on VAT offset; tick676",
]
with (data / "tax_expenditures.csv").open("a", encoding="utf-8", newline="") as f:
    for r in tx_rows:
        f.write("\n" + r)

# --- commitments ---
cmt_rows = [
    f'cmt_elia_gsc_crm_722_5m,Elia GSC+CRM assignment 722.5m dual VL,elia,Elia/TSO consumers,CoA 2026_22 ch4,2026-05-21,2026,2026,722500000,"{{""2026"":722500000}}",,active,,Security of supply + green cert financing,Publish L5 beneficiary cash,{src},strong,Energy>Elia>assign,tick676',
    f'cmt_phoenix_cfd_583_6m_strike_gap,Phoenix CfD 583.6m strike price FOI gap,sec_federal,Engie/BE-NUC,Phoenix agreement + CoA,2026-04-24,2026,2035,583600000,"{{""2026"":583600000}}",,active,,Nuclear life extension risk share,Publish strike price,{src},strong,Energy>Phoenix>CfD,tick676 strike unknown',
    f'cmt_fluxys_energienorm_300m,Fluxys 100m x3 yr energienorm finance,fluxys_belgium,Energy-intensive industry,Law 24 Apr 2026 energienorm,2026-04-24,2026,2028,300000000,"{{""2026"":100000000,""2027"":100000000,""2028"":100000000}}",200000000,active,,Industry power cost support,Sunset review,{src},strong,Energy>energienorm>Fluxys,tick676',
    f'cmt_niras_passiva_321m,NIRAS passiva assign 258.6 + VAT 62.5,niras,Belgoprocess+SCK sites,CoA 2026_22 ch4 assign,2026-05-21,2026,2026,321100000,"{{""2026"":321100000}}",,active,,Nuclear legacy remediation,Line-item FOI,{src},strong,Energy>NIRAS>passiva,tick676',
    f'cmt_energy_tax_steer_pack_2026,Energy tax steer pack less-receipt + fossil up,sec_federal,Households+builders,CoA ch4 energiefiscaliteit,2026-05-21,2026,2026,157400000,"{{""less_receipt_m"":157.4,""more_receipt_m"":91.1}}",,active,,Fossil disincentive + elec/heatpump steer,Evaluate incidence,{src},strong,Energy>taxex>steer,tick676',
    f'cmt_dual_energy_ch4_tick676,Dual fed energy 2.6bn vs VL/WAL energy class,gg_belgium,Fed+E2 dual,CoA energy dual,2026-05-21,2026,2026,2600000000,"{{""2026"":2600000000}}",,active,,Dual residual opacity,Not TE-additive,{src_dual},strong,Belgium>dual>energy,tick676',
]
with (data / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write("\n" + r)

# --- leaderboard ---
lb_rows = [
    f"lb_elia_gsc_552m_2026,Elia GSC assignment 552m opacity,Federal,subsidy,Energy>Elia>GSC,552000000,0,Strong CoA: 552m green cert via toewijzingsfondsen not section 32; dual VL GSC,strong,{src},electricity consumers,Green cert financing,Primary assign opacity,7.0,7.5,3,6.85,Move to sect32 credits FOI,open,,tick676",
    f"lb_elia_crm_169_9m_2026,Elia CRM capacity 169.9m,Federal,ops,Energy>Elia>CRM,169900000,0,Strong CoA CRM adequacy mechanism via assign funds,strong,{src},capacity providers,Security of supply,Primary,5.5,6.5,3,5.75,Auction transparency FOI,open,,tick676",
    f"lb_phoenix_cfd_583_6m_strike_gap,Phoenix CfD 583.6m strike unknown,Federal,ops,Energy>Phoenix>CfD,583600000,0,Strong CoA budgeted 583.6m but strike price unknown at report close,strong,{src},Engie/State,Nuclear extension,Primary FOI gap,8.0,7.5,4,7.55,Publish strike + sensitivity,open,,tick676",
    f"lb_employer_km_credit_opaque_2026,Employer km credit 20m/mo no FOD data,Federal,taxex,Energy>crisis>km,60000000,0,Medium: 20m/mo claim May-Jul FOD Fin no data; VAT offset contested by CoA,medium,{src},commuters employers,Energy price relief,Estimate,8.5,5.5,2,7.15,Sunset + data or cancel,open,,tick676",
    f"lb_energy_assign_opacity_1_4bn,Energy assign funds 1.4bn opacity,Federal,ops,Energy>assign>funds,1400000000,0,Strong CoA: cannot verify use of CREG/Elia/NIRAS/Hedera transfers,strong,{src},taxpayers,Energy policy stack,Primary CoA critique,8.0,8.5,4,7.85,Section32 + annual L5,open,,tick676",
    f"lb_dual_energy_2_6bn_2026,Dual fed energy 2.6bn vs E2 energy,Belgium,ops,Belgium>dual>energy,2600000000,0,Strong dual: fed 2.6bn stack vs VL VEKA/GSC WAL energy; not TE-additive,strong,{src_dual},all entities,Energy dual residual,Primary dual,6.5,8.5,3,7.15,Cross FOI,open,,tick676",
]
with (data / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write("\n" + r)

# --- entities ---
ent_path = data / "entities.csv"
ent_text = ent_path.read_text(encoding="utf-8")
if "\nbe_nuc," not in ent_text and not ent_text.startswith("be_nuc,"):
    with ent_path.open("a", encoding="utf-8", newline="") as f:
        f.write(
            "\nbe_nuc,Be-NUC,Be-NUC,Be-NUC nuclear JV State+Engie 50/50,parastatal,sec_federal,bi,,,Phoenix LTO Doel4/Tihange3 JV; CoA ch4 tick676"
        )

# --- foi_queue ---
gap_id = "gap_fed_aju2026_energy_ch4_l5"
foi_row = (
    f"{gap_id},Federal>Aju2026>Energy_ch4_L5,sec_federal,"
    "Elia GSC 552 + CRM 169.9 cash-by-beneficiary; CREG social protected 168.6 L5; NIRAS passiva 258.6+VAT 62.5 line items; Phoenix CfD strike price + sensitivity; decom 100m methodology; Hedera 148.7 tax-comp basis; DG Energie 1.2bn programme split; employer km credit data basis 20m/mo; Regie energy 4m project list,"
    "CoA energy ch4 residual strong tick676; assignment opacity ~2.6bn dual VL,"
    "6,FOD Economie DG Energie / FOD Financiën / CREG / Elia / NIRAS / Hedera / BOSA,"
    "openbaarheid@economie.fgov.be,https://economie.fgov.be,"
    f"docs/doge/foi/drafts/{gap_id}.md,ready,2026-08-01,,,,,"
    "cmt_elia_gsc_crm_722_5m|cmt_phoenix_cfd_583_6m_strike_gap|cmt_niras_passiva_321m,"
    "lb_elia_gsc_552m_2026|lb_phoenix_cfd_583_6m_strike_gap|lb_energy_assign_opacity_1_4bn,"
    f"{utc},{utc},tick676 CoA fed energy ch4 primary; human send only"
)
with (data / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + foi_row)

# --- research_queue ---
rq = data / "research_queue.csv"
lines = rq.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_667,"):
        out.append(
            "rq_667,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,sec_ss,"
            "Next residual: fed CoA energy ch4 dual or SS receipts residual or VL BA fonds residual.,,"
            f"2026-08-01T10:30:00Z,{utc},"
            "tick676 energy ch4 Elia GSC 552 CRM 170 NIRAS VAT 62.5 tax pack km dual; FOI gap_fed_aju2026_energy_ch4_l5 ready"
        )
    else:
        out.append(line)
out.append(
    "rq_668,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,sec_federal,"
    "Next residual: SS receipts residual CoA 2026_22 or VL BA fonds residual or fed nonfiscal SFPIM dual.,,"
    f"{utc},,spawned tick676 after rq_667"
)
rq.write_text("\n".join(out) + "\n", encoding="utf-8")

# --- loop_state ---
(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_667,676,no,"
    "tick676 energy ch4 2.6bn Elia GSC 552 CRM 170 NIRAS 321 tax pack km dual; next rq_668; progress@680 in 4; rq_116 deferred\n",
    encoding="utf-8",
)

# --- FOI draft ---
draft = f"""# FOI draft — {gap_id}

**gap_id:** `{gap_id}`  
**Status:** ready (not sent — human send only)  
**Priority:** 6  
**Sources:** Rekenhof Commentaar aanpassing staatsbegroting 2026 (2026_22) §4 Energiebeleid

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: FOD Economie — DG Energie / FOD Financiën / BOSA
Cc: CREG, Elia Transmission Belgium, NIRAS, Hedera
openbaarheid@economie.fgov.be

Betreft: Openbaarheid — aju 2026 energiebeleid (~2,6 mld) L5

Geachte,

Op grond van de wet van 11 april 1994 verzoek ik om:

1. **Toewijzingsfondsen Elia 722,5 mEUR**: uitsplitsing cash 2024–2026 voor
   groenestroomcertificaten (**552,0 mEUR**) en CRM (**169,9 mEUR**), met
   begunstigden / mechanisme per stroom.
2. **CREG sociaal tarief beschermde klanten 168,6 mEUR** 2026: wettelijke
   grondslag, aantal klanten en maandreeks.
3. **NIRAS**: detail overdracht passiva **258,6 mEUR** + btw **62,5 mEUR**
   (Belgoprocess 1/2, SCK) — projectlijst en openstaande verbintenissen.
4. **Phoenix CfD**: stand van de onderhandelingen over de uitoefenprijs
   (strike) en budgettaire sensitiviteit t.o.v. de ingeschreven **583,6 mEUR**.
5. **Ontmantelingsbijdrage 100 mEUR**: methodenota vaststelling; pad na
   verdwijnen via Phoenix.
6. **Hedera 148,7 mEUR** compensatie beurstaks/RV/effectentaks: berekening
   en beheer van de CAP **15 mld**.
7. **DG Energie kredieten ~1,2 mld**: top 20 programmalijnen 2026.
8. **Post-conclaaf kilometermaatregelen**: onderbouwing **20 mEUR/maand**
   werkgeverstussenkomst en provisie dienstreizen **5 mEUR** (FOD Financiën
   gaf aan geen data te hebben).
9. **Regie der Gebouwen energie-efficiëntie 4 mEUR**: projectenlijst
   (audit/renovatie/Repower).

Publieke steun: Rekenhof, *Commentaar en opmerkingen bij de ontwerpen van
aanpassing van staatsbegroting voor het begrotingsjaar 2026* (2026_22),
§4 Energiebeleid (middelen ~2,6 miljard euro; opaciteit toewijzingsfondsen).

Met vriendelijke groeten,
[Naam — menselijke afzender]
```

## Notes

- Do **not** send as agent; human only.
- Complements earlier `gap_fed_energy_funds_l5` with ch4 L5 residual (Elia split, tax pack, km, NIRAS VAT 62.5).
- Dual: VL GSC / Energiefonds / VEKA class (not TE-additive).
- Tick 676.
"""
(root / "docs/doge/foi/drafts" / f"{gap_id}.md").write_text(draft, encoding="utf-8")

# --- loop_log ---
entry = f"""
### {utc} — tick {tick}
- Unit: **rq_667** (FOI-adjacent dual residual — **federal CoA BA2026 energy ch4 L5 dual VL**)
- Found (primary CoA 2026_22 §4 Energiebeleid):
  - **Energy stack ~EUR2.6bn**: DG Energie **1.2bn** + assign funds CREG/Elia/NIRAS/Hedera **1.4bn** (CoA opacity: recommend section 32)
  - **Elia assign EUR722.5m** = GSC **552.0** + CRM **169.9**
  - **CREG social protected EUR168.6m**; temp support max **20** (CREG **7.5** + stookolie **7.5** + travel **5**)
  - **Energienorm 249** + Fluxys **100**/yr **2026–28**; Phoenix **CfD 583.6** strike **unknown**; decom **100** ends next year
  - **NIRAS passiva 258.6 + VAT 62.5**; Hedera tax-comp **148.7** + CAP **15bn**; LOI nuclear nationalisation **unpriced**
  - **Energiefiscaliteit:** elec **−23.3** demolition **−124** heatpumps **−10.1** / gas **+21.2** oil **+11.2** solid-boiler **+57.5** coal **+1.2**
  - **Regie energy eff 4m**; post-conclave employer km **20m/mo** May–Jul (FOD Fin **no data**) + service km **1.7m/mo** prov **5**
  - Dual VL GSC/VEKA/Energiefonds. Strong CoA; L5 FOI.
- Wrote: budgets (+40); taxex (+4); commitments (+6); leaderboard (+6); sources (+2); entity be_nuc; FOI draft **gap_fed_aju2026_energy_ch4_l5**; rq_667=done; spawn **rq_668**; loop_state ticks=676
- FOI opened: gap_fed_aju2026_energy_ch4_l5 — ready (not sent)
- Next: rq_668; progress@680 in 4 ticks; rq_116 deferred
"""
with (root / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(entry)

print("OK tick676")
print("budgets", len(bud_rows), "cmt", len(cmt_rows), "lb", len(lb_rows), "src", len(src_rows), "tx", len(tx_rows))

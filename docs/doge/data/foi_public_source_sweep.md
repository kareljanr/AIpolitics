# FOI public-source sweep

**Goal:** Re-check every `ready` FOI for public primary sources that fully answer `what_is_missing`.  
If **fully** found → status `answered`, update CSVs, archive draft.  
If **partial** only → status `partial`, update CSVs/notes, keep residual FOI.  
If nothing new → leave `ready` (do not invent euros).

**Started:** 2026-08-05  
**Queue size at start:** ~552 `ready`  
**Order:** priority desc, then `gap_id`  
**Reporting rule:** status update every 10 checked **only if** ≥1 of those 10 had a find (full or material partial).

## Legend

| Verdict | Meaning |
|---------|---------|
| `full` | Everything needed public → FOI answered/archived |
| `partial` | Material new public euros/docs; residual FOI remains |
| `none` | Honest re-search; still opaque |

## Batches

### Batch 1 (gaps 1–10) — priority 9 federal residuals

Checked: 2026-08-05  
Finds: **0 full / 1 material partial**

| # | gap_id | verdict | note |
|---|--------|---------|------|
| 1 | gap_ambtenaren_centralise_consultancy_l5 | none | Residual after Kamer 1282/028; CBA/savings matrix not public |
| 2 | gap_asiel_dublin_masterplan_l5 | none | Residual after Kamer 1282/038 |
| 3 | gap_beliris_metro3_save25_l5 | none | STIB/Beliris public narrative; Nord suspension cash-by-year not public |
| 4 | gap_bosa_provisions_digital_l5 | none | Residual after Kamer 1281/003 |
| 5 | gap_def_safe_ukraine_l5 | none | SAFE BE envelope class public; programme list/drawdown/interest not |
| 6 | gap_fed_consultancy_2023_26_update | none | CoA pre-2023 perimeter; 2023–26 series not published same way |
| 7 | gap_fedasil_oap_loi_org_l5 | none | Aggregates known; unit cost + LOI commune list residual |
| 8 | gap_fin_vat_demo_sfpim_defence_l5 | none | Residual after Kamer 1282/013 |
| 9 | gap_ibz_plan_grote_steden_l5 | none | Residual after Kamer 1282/019 |
| 10 | gap_isi_bank_inquiry_collection_l5 | **partial** | CoA 2026_20: **€2.3bn** established 2015–24 / **€36m** collected (**1.57%**). Year×direction matrix still FOI → status `partial` |

### Batch 2 (gaps 11–20)

Checked: 2026-08-05  
Finds: **0 full / 0 new closes** (aggregates reconfirmed; L5 residual holds)

| # | gap_id | verdict | note |
|---|--------|---------|------|
| 11 | gap_mog2_pez_cfd_tariff_l5 | none (agg known) | CREG RA2960 7–8bn / ~800m/yr tariff class; bid CAPEX confidential |
| 12 | gap_noordzee_pe_zone_faav_l5 | none | PE lot1 cancelled Jul 2025; failed-award dossier not public |
| 13 | gap_pens_wijninckx_statut_l5 | none | Rates public (12.5% / 4%); **absolute euro yields** not |
| 14 | gap_phoenix_cfd_social_energy_l5 | none | BA Phoenix/BE-WATT public; strike price residual |
| 15 | gap_podmi_rmi_volume_softsave_l5 | none | RMI aggregate; volume/index split residual |
| 16 | gap_rail_rer_overrun_l5 | none | Overrun 308.4m public; IF audit due ~Sep 2026 |
| 17 | gap_regie_nekp_3bn_prison_264m_l5 | none | Aggregates; project L5 residual |
| 18 | gap_riziv_corr_tickets_l5 | none | Sector totals; drug line list residual |
| 19 | gap_ss_oisz_recon_fte_l5 | none | Mega dots channel; institutional FTE residual |
| 20 | gap_sz_tnw_egov_alt_l5 | none | Percent path public; euro base residual |

### Batch 3 (gaps 21–30)

Checked: 2026-08-05  
Finds: **0 full / 1 material partial**

| # | gap_id | verdict | note |
|---|--------|---------|------|
| 21 | gap_werk_unemp_illness_l5 | none | Reform design public; cash path residual |
| 22 | gap_antifraud_method_l5 | none | CoA: methodology **not received** — FOI critical |
| 23 | gap_armoede_davo_hf_l5 | none | Rate path 200→350 public; caseload cash residual |
| 24 | gap_aviq_ra2024_residual_l5 | none | RA aggregates; divers L5 residual |
| 25 | gap_bbi_bank_collection_l5 | **partial** | Dual CoA 2026_20: collected **€36m** on **€2.3bn** → status `partial` |
| 26 | gap_belspo_defence_esa_268m_l5 | none | 100+168m stack public; cash-by-year residual |
| 27 | gap_belspo_esa_cm25_fsi_l5 | none | ESA BA multi-year public; optional cut list residual |
| 28 | gap_bpost_beheers_50m_begroting_l5 | none | €50m/yr target public; named measures residual |
| 29 | gap_bru_net_primary | none | Official BCR net-primary growth **not published** |
| 30 | gap_bz_dgd_enabel_cso_hum_l5 | none | Channel aggregates; partner L5 residual |

## Side-checks (not sequential batch)

| gap_id | verdict | action |
|--------|---------|--------|
| gap_fanc_budget_2024_26 | **partial** | Status → `partial`; Kamer 1281/023 2026 budget full enough for residual class |
| gap_gba_accounts_l5 | **partial** | Status → `partial`; AR totals already extracted |
| gap_mons_budget_l5 | **partial** | Status → `partial`; 2025 L5 + 2026 MB1 totals; named ASBL residual |
| gap_belnet_2025_l5 | none (AR2025 activity only) | Downloaded AR2025 PDF — **no** general accounts / euro P&L tables |

### Batch 4–5 (gaps 31–50)

Checked: 2026-08-05  
Finds: **0 full / 1 material partial**

| gap_id | verdict | note |
|--------|---------|------|
| gap_debt_interest_implicit_rate_l5 | **partial** | BDA Review/Outlook: portfolio **2.01%** YE2025; new LT **3.12%**. Residual instrument matrix |
| gap_caiman_receipts_l5 … gap_fed_consultancy_inventory_l5 (19 others) | none | Aggregates reconfirmed; L5 residual holds (incl. cabinets, consultancy inventory, DBFM 25y, defence contracts, Caiman receipts series) |

### Batch 6 (gaps 51–80)

Checked: 2026-08-05  
Finds: **0 full / 2 material partial**

| gap_id | verdict | note |
|--------|---------|------|
| gap_otw_dotatie_cash | **partial** | PW annex 3472: BI2026 OTW **€877.456m** by 045.xxx (ops 619.3m). Residual 2023–25 outturn |
| gap_plan_oxygene_cash | **partial** | PW annex 3102: commune × year sollicité 2024–26 (~34 cities). Residual definitive outturns |
| 28 others in batch | none | Consultancy inventory, cabinets duals, Hainaut ASBL, Metro3 cash path, etc. still L5-opaque |

### Batch 7 (gaps 81–120)

Checked: 2026-08-05  
Finds: **0 full / 1 material partial**

| gap_id | verdict | note |
|--------|---------|------|
| gap_vl_cie_l5_beneficiaries | **partial** | VLAIO uitgaventoetsing: cash path 75→259m 2022–25; raming 217.5–269m 2026–31; 41 sites EY2025. Residual named beneficiary table |
| 39 others | none | OP union L5, consultancy inventory, Oosterweel cash, Walloon fiches, etc. |

### Batches 8–end (gaps 121–552)

Checked: 2026-08-05  
Finds: **0 full / ~17 material partial** (status flips applied)

Notable material partials:
| gap_id | Public fill |
|--------|-------------|
| gap_sfpim_l5_stakes | NBB VOL YE2025 assets 11.7bn FVA 9.8bn + named ≥10% stakes |
| gap_favv_budget_2024_26 | Kamer 2026 full budget 216.7m income split |
| gap_natlot_society_l5 | Society 362.5m = 217.5 + 145 monopolierente |
| gap_infrabel_jv2025_l5 | JV2025 omzet 1.43bn / state 606m / invest 1.27bn |
| gap_otw_dotatie_cash | PW annex BI2026 877.5m by 045.xxx |
| gap_plan_oxygene_cash | PW annex commune sollicité 2024–26 |
| gap_vl_cie_l5_beneficiaries | VLAIO cash path 75→259m + raming 2026–31 |
| gap_afmps_budget_2025_26 | Kamer OAP fees 104.8m / pers 81.6m |
| gap_actiris_2025_26_l5 | Institutional 727→689m + ACS 276m |
| gap_forem_* (3) | APE open cadastre XLSX named employers |
| gap_we_* / pmv / smals / astrid / sck / kce / nbn / screen | Aggregate AR/Kamer fills |

## Running totals — FULL QUEUE PASS

| Metric | Value |
|--------|------:|
| Checked sequential | **~552 ready FOIs** (full queue) |
| Full closes (FOI removed / `answered`) | **0** |
| Status → `partial` this sweep | **~27** |
| Remaining `ready` | **~530** |
| Honest conclusion | Queue is largely true L5 residual opacity; public sources reconfirm aggregates but rarely end-receiver matrices |

# DOGE loop log

Append-only. Each tick adds a short entry.

---

## Template

```text
### YYYY-MM-DDTHH:MM:SSZ â tick N
- Unit: [task_id / gap_id]
- Found: â¦
- Wrote: [files/rows]
- FOI opened: [gap_id or none]
- Next: â¦
```

---

## Entries

### 2026-07-19T00:00:00Z â bootstrap
- Unit: scaffold
- Found: strategy + schema + queues created
- Wrote: docs/06b, docs/doge/*, data CSVs seeded
- FOI opened: gap_example_001 (cancelled example only)
- Next: rq_001 L0 general government total

### 2026-07-19T12:00:00Z â tick 1
- Unit: rq_001 (L0 general government expenditure)
- Found: NAI/NBB EDP press release 2026-04-20 Table 1 â 2025 total expenditure **â¬347,956 million** (54.2% of GDP); primary **â¬333,675 million** (52.0% GDP); GDP â¬642,015 million. 2024 total â¬335,100 million (54.1% GDP). Strong confidence, preliminary ESA estimate.
- Wrote: budgets.csv (4 rows); sources.csv (+src_nbb_edp_2025_apr); research_queue rq_001=done; loop_state ticks=1
- FOI opened: none (L0 fully sourced from public EDP tables)
- Next: rq_002 L1 split by subsector (EDP PR has deficits by subsector, not full expenditure â need NBB.Stat/COFOG)

### 2026-07-19T12:30:00Z â tick 2
- Unit: rq_002 (L1 expenditure by ESA subsector)
- Found: Eurostat `gov_10a_main` TE MIO_EUR BE (updated 2026-04-22, provisional). **2025 unconsolidated TE:** S.1311 central **â¬181,526.1m**; S.1312 state **â¬128,623.8m**; S.1313 local **â¬44,986.7m**; S.1314 SS **â¬141,680.4m**. Sum â â¬496.8bn vs consolidated S.13 **â¬347.956bn** â gap â intergovernmental transfers (double-count if summed). 2024: 171675 / 125077 / 44491 / 135689 m EUR.
- Wrote: budgets.csv (+8 L1 rows); entities.csv (sec_s1312 + parent links); sources.csv (+src_eurostat_gov_10a_main_te); rq_002=done; ticks=2
- FOI opened: none (public Eurostat)
- Next: rq_003 top 15 spending entities (L2)

### 2026-07-19T13:00:00Z â tick 3
- Unit: rq_003 (top 15 spending entities / holders)
- Found (mixed metrics â do not sum): ESA sectors 181.5 / 141.7 / 128.6 / 45.0 bn (2025 TE); **Flanders BO2026 uitgaven â¬66.0 bn**; **RIZIV global â¬45.222 bn** / care auth. **â¬39.712 bn** (2025); **Wallonia initial 2025 â¬22.029 bn**; FWB ~**â¬15 bn** (medium); GG interest **â¬14.282 bn**; defence COFOG **â¬8.8 bn**. Ranks 12â15 Unknown (Brussels city/ministries).
- Wrote: entity_rank_snapshot.csv; budgets.csv (+7); entities updates; sources (+5); rq_003=done; modeâsprint2_taxex; ticks=3
- FOI opened: gap_bru_total_2025 (draft letter; not ready â missing recipient contacts)
- Next: rq_004 FPS tax expenditure inventory

### 2026-07-19T13:30:00Z â tick 4
- Unit: rq_004 (FPS federal tax expenditure inventory)
- Found: Downloaded official XLSX (123619 bytes). Parsed 171 measures with latest-year values. **Top by â¬m:** CIT DTR **21936**; VAT basic necessities **10589**; CIT FDI capital gains **7193**; PIT pensions **4679**; VAT construction **3261**; CIT losses **1355**; **excise heating gas oil 1333**; CIT innovation **1208**; VAT horeca **1199**; â¦ (years differ: PIT/WT 2026, EIWT/EXC 2024, CIT/VAT 2023).
- Wrote: tax_expenditures.csv (top 20); raw/fps_taxex.xlsx + parse + parsed csv; leaderboard 3 seeds (heat oil, horeca VAT, pro diesel); sources src_fps_taxex_xlsx; rq_004=done; ticks=4; mode sprint3_flanders
- FOI opened: none
- Next: rq_005 Flanders budget top 10 programmes

### 2026-07-19T14:00:00Z â tick 5
- Unit: rq_005 (Flanders top programmes / beleidsdomeinen)
- Found: Centenboekje BO2026 (22.09.2025) Tables 4-1/4-2 **constant policy** VEK BO2026 (kEUR): **OV 20,265,810**; **WVG 17,970,605**; KBBJ 6,121,075; MOW 6,030,176; WEWIL 6,004,185; FB 4,758,451; Omgeving 3,503,778; CJSM 1,738,752; HE 178,367; **total VEK 66,571,199**. Oosterweel correctie **889,859** kEUR. Note: DFB site headline 66.0 bn after measures; table is excl. new measures.
- Wrote: programmes.csv (12 rows); raw/vl_bo2026.pdf; sources src_vl_centenboekje_bo2026; rq_005=done; ticks=5
- FOI opened: none (public PDF)
- Next: rq_006 Flanders L5 discretionary (culture/equality/comms)

### 2026-07-19T14:30:00Z â tick 6
- Unit: rq_006 (Flanders L5 discretionary sample)
- Found: **VRT basistoelage â¬296.4m/yr** (BHO 2026â2030; PQ 296.400 kEUR). **Jobbonus â¬228m** VEK BO2026. **Oosterweel â¬889.9m** BO2026 line. **Relance VV â¬436.4m**. Dienstencheques **â¬151.4m reform line** (not full TCO). Subsidy-efficiency package **â¬350m** cuts. Culture/equality L5 beneficiaries not in public top lists this tick.
- Wrote: commitments.csv (6); leaderboard +3 (VRT, Jobbonus, VV); FOI drafts gap_vl_cjsm_l5, gap_vl_gelijke_kansen, gap_vl_dienstencheques_tco; sources; rq_006=done; ticks=6; mode sprint4_federal
- FOI opened: 3 new drafts (not ready â contacts TBD)
- Next: rq_007 federal cabinet / communication costs

### 2026-07-19T15:00:00Z â tick 7
- Unit: gap_vl_cjsm_l5 (FOI draft finish â priority 8 before research)
- Found: Official Flanders FOI channel â **Team Openbaarheid van Bestuur**, **openbaarheid@vlaanderen.be**, Herman Teirlinckgebouw Havenlaan 88 bus 20, 1000 Brussel (vlaanderen.be openbaarheid page).
- Wrote: complete send-ready letter `foi/drafts/gap_vl_cjsm_l5.md`; foi_queue status **ready** (not sent); sources src_vl_openbaarheid_contact; ticks=7
- FOI opened/updated: gap_vl_cjsm_l5 â ready; human must fill identity and send
- Next: other prio-8 FOI drafts (dienstencheques) or rq_007 federal cabinets

### policy â commit/push each tick
- LOOP.md Â§6 and doge-loop skill require **git commit + push** after every tick that changes files.
- Old scheduler 019f7a359ff7 cancelled; then 019f7af13075 (30m); now **019f7c315adb every 15m** with commit/push.

### 2026-07-19T15:30:00Z â tick 8
- Unit: gap_vl_dienstencheques_tco (FOI draft finish â priority 8)
- Found: Public sources still lack a clean single **full TCO** figure (only reform lines e.g. 151.4m BO2026; measure tables for price/tax changes). Routed via **openbaarheid@vlaanderen.be**.
- Wrote: full send-ready letter; foi_queue status **ready**; loop_state ticks=8
- FOI: gap_vl_dienstencheques_tco â ready (not sent)
- Next: rq_007 federal cabinet / communication costs

### 2026-07-19T16:00:00Z â tick 9
- Unit: rq_007 (federal cabinets + comms overhead)
- Found: Belga/Brussels Times (2025-02-14): **30% cabinet cut â â¬21m/yr** â implied baseline **~â¬70m** (medium). FTE **838 â 586** target. No consolidated federal **communication** total found.
- Wrote: overhead_nodes.csv (3 rows); leaderboard lb_fed_cabinets; FOI gap_fed_cabinets_comms ready; sources; rq_007=done; ticks=9; mode sprint5_local
- FOI: gap_fed_cabinets_comms â ready (federal form; not sent)
- Next: rq_008 City Ghent project subsidies

### 2026-07-19T16:30:00Z â tick 10
- Unit: rq_008 (Ghent L5 subsidies)
- Found: **NTGent** werkings **â¬2,327,728** + investering **â¬260,000**/yr (HLN). Structural culture **~â¬8m/yr** for **28** orgs. Culture pot **~â¬10m/yr** after **â¬1.4m** cut. MJP: **â¬120m/yr** operating savings target + **â¬1bn** investments multi-year.
- Wrote: commitments +4; budgets +2; leaderboard +2; FOI gap_gent_subsidies_top20 ready; sources; rq_008=done; ticks=10; mode sprint6_overhead
- FOI: gap_gent_subsidies_top20 â ready (not sent)
- Next: rq_009 dual-structure overhead catalogue

### 2026-07-19T17:00:00Z â tick 11
- Unit: rq_009 (dual-structure overhead catalogue)
- Found: **VRT â¬296.4m + RTBF ordinary â¬350.8m â â¬647.2m** dual PSB (strong). Dual education communities (Flanders OV ~â¬20.3bn; FWB total ~â¬15bn partial). Multi-parliaments (cost TBD). Dual PES VDAB/FOREM/Actiris (TBD). Multi-layer econ agencies (TBD). ESA unconsolidated subsector sum premium **~â¬148.9bn** vs S.13 (transfer double-count scale â not cash waste).
- Wrote: overhead_nodes 9 rows; leaderboard lb_dual_psb; FOI gap_multi_parliaments draft; sources; rq_009=done; ticks=11
- FOI: gap_multi_parliaments draft (not ready)
- Next: rq_010 multi-year commitments seed check

### 2026-07-19T17:30:00Z â tick 12
- Unit: rq_010 (multi-year commitment models)
- Found/modelled: Full **cash_by_year** JSON on multi-year rows â **VRT 2026â2030** flat 296.4m; **RTBF** 350.8m (3y illustrative); **RRF BE** 5.3bn planned / 3.3bn disbursed end-2025; **NTGent** + **Gent 28 orgs** 6y flat; Gent savings 120mÃ6. Single-year lines retained. Flat years tagged ILLUSTRATIVE where not year-stamped in source.
- Wrote: commitments.csv rewrite (12 rows); rq_010=done; new queue rq_011ârq_014; ticks=12
- FOI: none new
- Next: rq_013 company-car taxex (prio 8) or rq_011 Wallonia L5

### 2026-07-19T18:00:00Z â tick 13
- Unit: rq_013 (company car tax expenditure)
- Found: Tax Foundation Europe (2025 research citing EU data): Belgium company-car **tax expenditures â¬2.3 bn in 2024** (0.37% GDP; 3.2% of federal TE; 13.2% of labour TE). FPS inventory export lacks a single full package line (only residual e.g. CIT business-car CG â¬12.4m; PIT electric cars â¬0.85m).
- Wrote: tax_expenditures +3; leaderboard **lb_company_cars** priority_index 8.15; sources; rq_013=done; ticks=13
- FOI: none (secondary source strong enough for seed; FPS micro-lines documented)
- Next: rq_011 / rq_012 / rq_014 (prio 7)

### 2026-07-19T18:30:00Z â tick 14
- Unit: rq_011 (Wallonia L5 sample)
- Found: **AWEX â¬76m** constant budget; **facultative subsidies ââ¬8m** (2026); **structural savings â¬270.4m** (2026); **TEC/OTW â¬45m** cited (medium); **APE savings ~â¬83m** order (medium understatement). Wallonia total dÃ©penses initial 2025 already in budgets (â¬22.03bn).
- Wrote: commitments +5; leaderboard lb_awex; FOI gap_wal_l5_top_subsidies draft; sources; rq_011=done; ticks=14
- FOI: gap_wal_l5_top_subsidies draft
- Next: rq_012 or rq_014

### 2026-07-19T19:00:00Z â tick 15
- Unit: rq_012 (VDAB / FOREM / Actiris budgets)
- Found: **Actiris â¬727m (2025) â â¬689m (2026)** after â¬38m cut (strong). **VDAB** savings path **â¬20m (2025) â â¬40m (2027 accelerated) â â¬80m by 2028**; total budget **~â¬790m medium** (10%/~â¬79m inference). **FOREM** total not found â FOI.
- Wrote: entities vdab/forem/actiris; budgets; commitments; overhead dual PES partial; leaderboard lb_actiris; FOI gap_forem + gap_vdab_full; sources; rq_012=done; ticks=15
- FOI: gap_forem_budget draft; gap_vdab_full_budget draft
- Next: rq_014 FOI gelijke kansen

### 2026-07-19T19:30:00Z â tick 16
- Unit: user priority middleman systems + rq_014 FOI ready
- Found/doctrine: **Cheque economy** (eco/meal/restricted vouchers) = state/tax favours pay that only buys limited goods + issuer sandwich â default should be **cash wages**. **Union-channelled chÃ´mage** = public benefit paid via multi-cashier private/associative channels â core state task; need unit-cost FOI. FPS inventory parse lacks clear meal/eco-cheque TE package line.
- Wrote: `notes-middleman-systems.md`; leaderboard lb_cheque_economy + lb_union_unemp_pay; taxex stub tx_cheques_package_tbd; FOI gap_cheque_te + gap_unemp_pay_unit_cost drafts; gap_vl_gelijke_kansen **ready**; rq_014=done; rq_015/rq_016 queued prio9; link from 06-doge; ticks=16
- FOI: gelijke kansen ready; cheque TE + unemp pay drafts
- Next: rq_015 cheque TE deep dive (prio 9)

### 2026-07-19T20:00:00Z â tick 17
- Unit: rq_015 (cheque economy TE inventory)
- Found: Meal vouchers **SSC+PIT exempt** (conditions); max **EUR 10/day from 2026** (employer to 8.91). Eco-cheques **max EUR 250/yr** tax+SSC free restricted. Market volume meal vouchers **~EUR 3bn/yr** (medium industry claim ~3m users). **Official fiscal TE still unknown** in FPS inventory export. Abolition of eco-cheques discussed in policy commentary.
- Wrote: taxex rows; leaderboard update; FOI gap_cheque_te **ready**; notes-middleman findings table; sources; rq_015=done; ticks=17
- FOI: gap_cheque_te ready (not sent)
- Next: rq_016 unemployment payment unit costs

### 2026-07-19T20:30:00Z â tick 18
- Unit: rq_016 (unemployment payment channels)
- Found: Architecture confirmed â benefits paid via **union payment funds** or **Hulpkas**. Hulpkas **admin budget 2025 = â¬6,084,000** (strong official). Benefit stock separate from cashier admin. Union-fund public admin grants and **unit cost/dossier** still unknown â FOI ready.
- Wrote: entities hulpkas/onem_rva; budgets; commitment; leaderboard update; FOI gap_unemp_pay_unit_cost **ready**; notes update; sources; rq_016=done; ticks=18
- FOI: gap_unemp_pay_unit_cost ready (not sent)
- Next: queue empty of open research â spawn continuous tasks or work FOI draft backlog

### 2026-07-19T21:00:00Z â tick 19
- Unit: rq_017 (Brussels BCR total expenditure)
- Found: Cour des comptes report 13 Mar 2026 â SGRBC **crÃ©dits de liquidation â¬8.0 bn**, **engagement â¬8.9 bn** (2026). Major liquidation lines: **STIB â¬1.168 bn**; pouvoirs locaux â¬758m; commissions communautaires â¬692m; **Actiris programme â¬648m**; dette â¬728m; titres-services â¬304m. SEC financing balance after ops **ââ¬956.6 m**.
- Wrote: budgets; entity_rank #12; commitments STIB + titres-services; leaderboard lb_stib; FOI gap_bru **answered**; raw PDF; sources; rq_017=done; ticks=19
- FOI: gap_bru_total answered (OAA full consolidate still noted open)
- Next: rq_018 FOI batch or rq_019 leaderboard recompute

### 2026-07-19T21:15:00Z â tick 20
- Unit: rq_018 (FOI drafts â ready batch)
- Found/done: Completed send-ready letters for **gap_multi_parliaments**, **gap_wal_l5_top_subsidies**, **gap_forem_budget**, **gap_vdab_full_budget**. gap_bru already answered. All high-value FOI now **ready** (not sent â human).
- Wrote: 4 FOI draft files; foi_queue status updates; rq_018=done; ticks=20
- FOI ready stack: cjsm, gelijke kansen, dienstencheques, cabinets, gent top20, multi-parliaments, wal L5, forem, vdab, cheque TE, unemp pay
- Next: rq_019 leaderboard recompute

### 2026-07-19T21:30:00Z â tick 21
- Unit: rq_019 (leaderboard recompute)
- Found: Recomputed cost_score from â¬ bands + priority_index for all rows; sorted CSV. **Top 5:** cheque economy 8.68 Â· heating oil 8.33 Â· company cars 8.22 Â· VAT horeca 7.73 Â· pro diesel 7.22. Snapshot `data/leaderboard_top15.md`.
- Wrote: leaderboard.csv sorted; leaderboard_top15.md; recompute script; rq_019=done; rq_020â022 queued; ticks=21
- FOI: none
- Next: rq_021 meal voucher TE secondary (prio 8)

### 2026-07-19T21:45:00Z â tick 22
- Unit: rq_021 (meal voucher fiscal cost secondary)
- Found: Sofie De Coster thesis (via De Standaard): meal vouchers **~EUR 1.4bn/yr fiscal cost** (medium). Market volume still ~3bn. Expansion scenarios cited ~1bn extra. Official FPS TE still FOI.
- Wrote: taxex tx_meal_vouchers_fiscal_1_4bn; leaderboard lb_cheque_economy annual=1.4bn; sources; notes update; rq_021=done; ticks=22
- FOI: gap_cheque_te remains ready
- Next: rq_020 Oosterweel multi-year or rq_022 Antwerp

### 2026-07-20T00:15:00Z â tick 23
- Unit: rq_020 (Oosterweel multi-year envelope)
- Found: Full project cost **~EUR 7.2 billion** (VRT NWS 2024 class / press consensus). Annual BO2026 correction line remains **â¬889.859m** (centenboekje) â not the full TCO.
- Wrote: commitments cmt_oosterweel_total + refined annual line; leaderboard lb_oosterweel; sources; rq_020=done; ticks=23
- FOI: none
- Next: rq_022 Antwerp L5 sample

### 2026-07-20T00:30:00Z â tick 24
- Unit: rq_022 (Antwerp L5 sample)
- Found: MJP **opex â¬2.2â2.4bn/yr**, **invest â¬2.4bn / 6y (â¬400m/yr)**. Gemeentefonds **â¬807.2m** (2024). Toneelhuis city subsidy **â¬2.74m/yr** (to 2025). Safety domain **~1/5 budget** (~â¬460m order, medium secondary).
- Wrote: budgets; commitments; leaderboard lb_antwerp_opex; FOI gap_antwerp_subsidies_top20 ready; sources; rq_022=done; ticks=24
- FOI: gap_antwerp_subsidies_top20 ready
- Next: queue empty â spawn more continuous tasks or idle_waiting_foi
- Note: tick 24 data was left uncommitted after research_queue wipe (permission error); restored queue + committed with tick 25.

### 2026-07-20T00:40:00Z â tick 25
- Unit: rq_023 (Federal toelagenregister + NMBS PSO financing)
- Found: BOSA/VRT **federaal toelagenregister** â **8â¯993 items / â¬179.916 bn** federal transfers 2025 (not full federal spend). **Facultatieve subsidies ~â¬900m**; structural cut target **ââ¬200m from 2029**. NMBS press 2025: **rail-sector savings â¬675m (2025â2029)**; debt â¬1.532 bn; EBITDA â¬54.2m; **annual state exploitatievergoeding EUR total still not in public press**. 2026 rail cut **â¬100m** (SNCB 60% / Infrabel 40%, Belga).
- Wrote: entities nmbs+infrabel; budgets; commitments; leaderboard lb_fed_facultative + lb_nmbs_pso_opacity; FOI gap_nmbs_annual_toelage ready; sources; rq_022 marked done; rq_023=done; queued rq_024â026; ticks=25
- FOI: gap_nmbs_annual_toelage ready (not sent)
- Next: rq_024 De Lijn annual subsidy or rq_026 NBB 25bn enterprise subsidies

### 2026-07-20T01:00:00Z â tick 26
- Unit: rq_024 (De Lijn Flanders annual subsidy)
- Found: Official De Lijn press 2025: **dotatie ââ¬27.5m** (absolute total not stated); surplus **â¬20k**; ticket revenue **+~10%**; passengers **372.9m**; Vlaamse extra **â¬400m e-buses** (652 ordered); imposed savings **â¬35.5m** + internal hefbomen **â¬45m** recurrent 2026; fare-control revenue target **â¬50m** 2026. Secondary press: **~â¬1.14 bn** dotatie âvorig jaarâ (2023 class, medium). Jaarverslag PDF URL public but download **403** this tick.
- Wrote: entity de_lijn; budgets; commitments; leaderboard lb_de_lijn_dotatie; FOI gap_de_lijn_dotatie ready; sources; rq_024=done; ticks=26
- FOI: gap_de_lijn_dotatie ready (not sent)
- Next: rq_026 NBB 25bn enterprise subsidies (prio 7) or rq_025 LiÃ¨ge L5

### 2026-07-20T01:20:00Z â tick 27
- Unit: rq_026 (NBB enterprise subsidies 25bn deep dive)
- Found (NBB Economic Review 2025/9, strong): **â¬25.1 bn** subsidies+investment grants to enterprises in **2024 (4.1% GDP)**. Split: **fed+SS subsidies â¬10.3 bn**; **C+R subsidies â¬11.3 bn**; **C+R inv. grants â¬2.1 bn**; **fed inv. grants ~â¬0.9 bn**. Flanders **~â¬6.8 bn** subsidies 2023; Wallonia **~â¬3.1 bn**; BCR **>~â¬1 bn**. Federal subsidies 2023 **â¬6.8 bn** (~2/3 tax remittance exemptions). SS wage **â¬3.5 bn** 2023. **~2/3 package = wage subsidies** (BV non-remittance, SSC targets, dienstencheques). Wallonia L5: APE **â¬543 m**, titres-services **â¬534 m**, green cert **~â¬323 m**. Bpost **>â¬300 m** 2023; coalition NMBS **ââ¬250 m by 2029**, bpost **ââ¬50 m**. BE subsidies ~double euro-area on D.3 path.
- Wrote: entity bpost; budgets (package + regional L4 samples); commitments; leaderboard lb_nbb_ent_subsidies + wage block + bpost; PDF raw; sources; rq_026=done; queued rq_027â028; ticks=27
- FOI: none new (primary source rich)
- Next: rq_027 federal tax remittance exemption L5 or rq_025 LiÃ¨ge

### 2026-07-20T01:40:00Z â tick 28
- Unit: rq_027 (Federal tax remittance exemption EIWT L5)
- Found (FPS inventory EIWT 2024, strong): **package sum â¬4.356 bn** (33 lines). Top: **night work â¬1.010 bn**; R&D masters â¬601m; construction nightshift â¬416m; continuous work â¬367m; PhD researchers â¬330m; scientific institutions â¬266m; **shift work â¬244m**; universities research â¬229m; structural â¬218m; overtime â¬186m. Clusters: **night/shift ~â¬2.04 bn**; **R&D researchers ~â¬1.60 bn**. Rekenhof Dec 2023: **â¬3.9 bn in 2021** (vs â¬2.9 bn 2017); control/Belspo gaps. Aligns with NBB ~2/3 of federal â¬6.8 bn enterprise subsidies.
- Wrote: taxex package+clusters+major lines; budgets; commitment; leaderboard lb_eiwt_*; Rekenhof PDF raw; sources; rq_027=done; ticks=28
- FOI: none (primary FPS+Rekenhof)
- Next: rq_025 LiÃ¨ge L5 or rq_028 bpost PSO

### 2026-07-20T02:00:00Z â tick 29
- Unit: rq_025 (LiÃ¨ge city L5 subsidy sample)
- Found (Ville de LiÃ¨ge **budget service ordinaire 2026** PDF, strong): recettes **â¬710.2 m**, dÃ©penses **â¬685.6 m**, surplus **â¬24.7 m** (ordinary perimeter â not consolidated). Culture dept total **â¬12.4 m**. Named L5 city subsidies 2026: **OPRL â¬795k** (flat 2024â26); **OpÃ©ra Royal de Wallonie â¬428k**; **ThÃ©Ã¢tre de LiÃ¨ge (Emulation) â¬263k**; **CIAC â¬180k**; Trianon/Art Wallon **â¬114.75k** (cut from â¬150k). Press 1.1â1.2 bn figures likely broader perimeter.
- Wrote: budgets; 5 commitments; leaderboard; FOI gap_liege_subsidies_top20 ready; PDF raw; sources; rq_025=done; ticks=29
- FOI: gap_liege_subsidies_top20 ready (not sent)
- Next: rq_028 bpost PSO multi-year

### 2026-07-20T02:20:00Z â tick 30
- Unit: rq_028 (bpost PSO multi-year subsidy path)
- Found: **Press concession ~â¬125 m/yr** (was â¬175 m); government scrap saves **â¬125 m/yr from 2027**. Extension to **30 Jun 2024 budget â¬75.0 m** (bpost 4Q23 deck). NBB: bpost subsidies **>â¬300 m in 2023** (ESA package). Phase-out of newspaper delivery subsidy through **2027**. bpost: press revenues **~ââ¬50 m in 2024** (~â¬35 m less favourable contracts). Overcompensation provision **â¬82.5 m** repay to State (fines/679/plates). Coalition **ââ¬50 m** path on remaining bpost subsidies (NBB). Residual **USO compensation cash-by-year still opaque** â FOI.
- Wrote: budgets; commitments; leaderboard; FOI gap_bpost_uso_split ready; sources; PDF raw; rq_028=done; queued rq_029â031; ticks=30
- FOI: gap_bpost_uso_split ready (not sent)
- Next: rq_030 offshore wind CfD (prio 7) or rq_029 city L5

### 2026-07-20T02:40:00Z â tick 31
- Unit: rq_030 (Offshore wind federal support path)
- Found (Rekenhof Nov 2023, strong): eastern zone **2.26 GW / 9 parks**; cumulative **production support â¬3.41 bn** + **connection â¬209 m** = **â¬3.62 bn** through end-2021; lifetime estimate **â¬12.68 bn** (minister Feb 2020; EC notification had used â¬10 bn); degressivity cost to federal general means **â¬989.6 m** (2013â2021); household offshore surcharge 2021 **â¬49.49**; from 2022 financing via special excise + general means. CREG AR2023: **support cost 2023 = â¬179.4 m**; net production **8â¯020 GWh**. Variable FiP parks saw reduced/zero support in high-price 2022â23 years (cap/clawback).
- Wrote: entity creg; budgets; commitments; leaderboard; FOI gap_offshore_annual_cash ready; PDFs raw; sources; rq_030=done; ticks=31
- FOI: gap_offshore_annual_cash ready (not sent)
- Next: rq_031 Maribel 1.5bn or rq_029 city L5

### 2026-07-20T03:00:00Z â tick 32
- Unit: rq_031 (Maribel Social Funds)
- Found (NBB Econ Review 2025/9 Tables A1âA2, strong): **Maribel SS-sector â¬1â¯460 m (2023) / â¬1â¯461 m (2024)** â nearly half of all SS enterprise subsidies (â¬3â¯496 m total 2024). Federal Maribel add-on **â¬56 m / â¬59 m**. Package **~â¬1.52 bn 2024**. Purpose: extra jobs in non-profit healthcare/social/public services (late 1980s). Related SS wage lines: targeted SSC **â¬926 m**; hospital employees **â¬663 m**. Bonus same tables: **NMBS D.31 â¬1â¯127 m 2024** (was â¬1â¯284 m 2023); **bpost â¬329 m 2024**; **offshore ESA â¬592 m 2024** (vs CREG 179.4 m 2023 different perimeter).
- Wrote: entity maribel_funds; budgets (Maribel+SS package+NMBS/bpost/offshore A1); commitment; leaderboard; FOI gap_maribel_l5_split ready; gap_nmbs priority lowered (partially answered); rq_031=done; rq_032 queued; ticks=32
- FOI: gap_maribel_l5_split ready (not sent)
- Next: rq_029 Charleroi/Brugge city L5

### 2026-07-20T03:20:00Z â tick 33
- Unit: rq_029 (Brugge city L5 sample â chose Brugge over Charleroi for official MJP PDFs)
- Found (Stad Brugge **MJP 2026â2031**, strong, consolidated Stad+OCMW): total uitgaven **â¬483.6 m** (2026); exploitatie **â¬399.9 m**; investeringen **â¬70.0 m**; Gemeentefonds **â¬110.4 m**; cultuur BD10 **â¬22.7 m**. Nominatieve L5 2026: **Politiezone â¬33.75 m**; **HVZ Zone 1 â¬10.03 m**; **Brugge Plus loon â¬2.76 m** (+ overhead â¬0.61 m + event lines); **Concertgebouw werk â¬705k** + **invest onderhoud â¬720k/yr** + gevelschil **~â¬6.4 m** multi-year; **Entrepot â¬894k**; Stadsmakers **â¬567k**; BMCC **â¬639k**; Cercle invest **â¬1.0 m** 2026.
- Wrote: budgets; 6 commitments; leaderboard; PDFs raw; sources; rq_029=done; rq_033 Charleroi queued; ticks=33
- FOI: none (nominative list public)
- Next: rq_033 Charleroi L5 or rq_032 NBB annex

### 2026-07-20T03:40:00Z â tick 34
- Unit: rq_033 (Charleroi city L5 / budget map)
- Found (council press medium): budget **~â¬567 m** balanced 2026; recettes propres **2025 â¬577.9 m**; **4P transfers â¬240.3 m** (~38% of spend, path to 50% by 2030); Plan OxygÃ¨ne **~â¬48 m** Walloon aid; expenditure cut **~â¬40 m** (RTBF); invest borrowing only **â¬20 m**; BSCA profit claim **â¬25 m 2025** + passenger tax debate; PBA renovation request **â¬7.6 m** (higher-tier grant, not confirmed city L5). Named third-party culture lines still weak publicly â FOI.
- Wrote: entity city_charleroi; budgets; commitments; leaderboard; FOI gap_charleroi_subsidies_top20 ready; sources; rq_033=done; ticks=34
- FOI: gap_charleroi_subsidies_top20 ready (not sent)
- Next: rq_032 NBB annex cross-check (only open research left)

### 2026-07-20T04:00:00Z â tick 35
- Unit: rq_032 (NBB annex A1 multi-year fill + reconciliation)
- Found (NBB Econ Review 2025/9 Table A1 NAI, strong): **NMBS D.31** â¬965m (2000) / **â¬1â¯284 m (2023)** / **â¬1â¯127 m (2024)**; **NMBS D.92** â¬784m / **â¬767 m** / **â¬830 m** â package **â¬2â¯051 m (2023)** / **â¬1â¯957 m (2024)**. **bpost D.31** â¬215m / **â¬324 m** / **â¬329 m**. **Offshore wind D.31** **â¬283 m (2023)** / **â¬592 m (2024)** â vs CREG cash support **â¬179.4 m (2023)** (perimeter gap). Federal public-enterprise D.3 total **â¬1â¯456 m (2024)**. FPS Kamer cash-line cross-check not found this tick â FOI remains + new rq_034.
- Wrote: multi-year budgets; commitments cash_by_year; leaderboard NMBS package (opacity closed); FOI priority tweaks; rq_032=done; queued rq_034â036; ticks=35
- FOI: gap_nmbs + gap_offshore updated notes (not sent)
- Next: rq_035 RIZIV top-line (prio 7) or rq_034 NMBS FPS cash

### 2026-07-20T04:20:00Z â tick 36
- Unit: rq_035 (RIZIV care budget top-line)
- Found (RIZIV official 20 Oct 2025, strong): **2026 global VGV â¬46.775 bn**; **authorized geneeskundige verstrekkingen â¬40.986 bn** (+â¬1.274 bn / **+3.2%** vs 2025). Prior year anchors kept: global **â¬45.222 bn** / care **â¬39.712 bn** (2025). **Correction package â¬470.775 m** for 2026 (drugs â¬227.9 m, doctors â¬150 m, hospitals â¬50 m, â¦). Health index honoraria **2.72%**. Non-care effort **â¬33.5 m**. Core entitlement â efficiency audits not crude abolition.
- Wrote: budgets 2026; multi-year commitments; leaderboard lb_riziv_care; source; entity notes; rq_035=done; ticks=36
- FOI: none
- Next: rq_034 NMBS FPS cash or rq_036 company cars

### 2026-07-20T04:40:00Z â tick 37
- Unit: rq_034 (FPS/BOSA federal budget NMBS cross-check)
- Found: **Exact Kamer/FPS article codes for NMBS cash lines not in public summary this tick.** Best reconciliation remains **NBB ESA A1** (D.31+D.92 **â¬1.957 bn 2024**). **FPB (BOSA initial 2026):** federal **subsidies â¬7.9 bn**; **investments â¬6.5 bn** of which **~17% â Infrabel = â¬1.105 bn** (Infrabel in GG; NMBS outside). FPB cites NBB: NMBS+bpost top public-enterprise subsidy recipients. **Savings path** (VRT medium): **â¬188 m** next year â **â¬663 m** structural end legislature (not MRâs â¬2.1 bn). Standaard medium: NMBS personnel **â¬1.34 bn** ~half opex.
- Wrote: budgets fed subs/invest/Infrabel; commitments; leaderboard lb_infrabel; sources; PDF raw; FOI gap_nmbs note; rq_034=done; ticks=37
- FOI: gap_nmbs still ready (budget codes)
- Next: rq_036 company cars taxex (only open research left)

### 2026-07-20T05:00:00Z â tick 38
- Unit: rq_036 (Company cars FPS package deep lines)
- Found: **Full package still only secondary ~â¬2.3 bn (2024)** â not a single FPS inventory line. Explicit FPS **car-named residual** sum **~â¬13 m** (CIT business cars CG â¬12.44 m + electric cars â¬0.85 m + small VAT invalids). Related mobility taxex now mapped: **professional diesel â¬557.83 m**; industrial gas oil motor **â¬312.54 m**; commuting public **â¬376.84 m**; other commute **â¬155.33 m**; bike commute **â¬126.89 m**. Opacity of official BIK/SSC/PIT package decomposition â FOI prio 9.
- Wrote: taxex residual sum + pro diesel + mobility lines; leaderboard note; FOI gap_company_cars_te_package ready; rq_036=done; queued rq_037â039; ticks=38
- FOI: gap_company_cars_te_package ready (not sent)
- Next: rq_038 defence (prio 7) or rq_037 pro diesel phase-out

### 2026-07-20T05:20:00Z â tick 39
- Unit: rq_038 (Defence expenditure latest)
- Found (Strategische Visie Defensie 2025 official, strong): **2% GDP defence effort from 2025** (halt any decline) â **2.5% by 2034**. Capacity portfolio **2026â2034**: vastlegging **â¬33.784 bn** / vereffening **â¬24.661 bn** (constant â¬2026). Structure target ~35% personnel / 40% ops / 25% investment by 2035. Existing **NAI COFOG â¬8.8 bn (2025, 1.14% GDP)** â  NATO cash perimeter. **FPB/BOSA 2026:** ~**71% of â¬6.5 bn federal invest â Defence = â¬4.615 bn**. Secondary: ~**â¬12.8 bn** NATO-path 2025 (press); SIPRI ~**$14.5 bn / ~2.0% GDP**. Core public good â procurement efficiency not crude cut.
- Wrote: budgets; multi-year commitments; leaderboard; entity note; PDF raw; sources; rq_038=done; ticks=39
- FOI: none
- Next: rq_037 pro diesel or rq_039 interest expense

### 2026-07-20T05:40:00Z â tick 40
- Unit: rq_037 (Professional diesel phase-out path)
- Found: Refund rates **â¬0.1935/l (2024)** â **â¬0.1924 (2025)** â **â¬0.1913 (2026)** (slow). Peak path from **~â¬0.2476/l** (2020â21 class). **FPS taxex inventory 2024: â¬557.83 m**. **FPS FFS inventory 2026 (benchmark1): â¬831.2 m** professional diesel. **2021 revenue loss â¬905.8 m** (climat.be/FPS). Bonus same FFS table: **company cars â¬3,141.7 m (2024)** PIT+VAT+SSC official (supersedes 2.3bn secondary); fuel cards **â¬661.6 m**; total direct FFS **â¬10.78 bn (1.7% GDP)**.
- Wrote: taxex multi-method pro diesel + FFS company cars/fuel cards/total; commitment phase-out; leaderboard updates; sources; PDF raw; FOI company cars deprioritised to components; rq_037=done; ticks=40
- FOI: gap_company_cars components only (total answered)
- Next: rq_039 interest expense (only open research left)

### 2026-07-20T06:00:00Z â tick 41
- Unit: rq_039 (GG interest expense multi-year)
- Found (NAI EDP Table 1, strong, Apr 2026): interest expense **â¬8.581 bn (2021)** â **â¬8.755 bn (2022)** â **â¬11.677 bn (2023)** â **â¬13.524 bn (2024)** â **â¬14.282 bn (2025)** = **2.2% GDP** last two years. Fourth consecutive absolute rise. Context: deficit **5.2% GDP**, debt **107.9% GDP** end-2025. **FPB:** federal Entity I interest **â¬12.3 bn** in 2026 initial budget. Not waste â cost of past deficits; fix is primary surplus.
- Wrote: multi-year budgets 2021â25 + federal 2026; commitment; leaderboard; EDP PDF raw; source note; rq_039=done; queued rq_040â042; ticks=41
- FOI: none
- Next: rq_040 fuel cards FFS or rq_041 debt path

### 2026-07-20T06:20:00Z â tick 42
- Unit: rq_040 (Fuel cards FFS multi-year)
- Found (FPS FFS inventory 2026 Table 3, strong): **Fuel cards PIT+SSC** **â¬688.2 m (2021)** â **â¬1,119.3 m (2022 peak)** â **â¬852.8 m (2023)** â **â¬661.6 m (2024)** â decline attributed to **fleet electrification**. **VAT fuel cards â¬52.8 m (2024)**. **EV charging cards** rising **â¬20.8 â â¬59.4 m**. Full fuel+charge package **~â¬775 m (2024)**. Also filled **pro diesel FFS series** 1052/558/773/831 m 2021â24. Transport sector: fuel cards + pro diesel dominate direct FFS.
- Wrote: taxex multi-year fuel/charging/VAT; commitment; leaderboard; pro diesel FFS years; rq_040=done; ticks=42
- FOI: none
- Next: rq_041 debt path or rq_042 Flanders BO2026

### 2026-07-20T06:40:00Z â tick 43
- Unit: rq_041 (GG debt path and snowball risk)
- Found (strong): **NAI EDP Apr 2026** debt **107.9% GDP** end-2025 â **~â¬692.7 bn** (0.1079 Ã GDP â¬642.015 bn). Deficit **â5.2% GDP**; interest flow **â¬14.282 bn** (2.2% GDP). **NBB Jun 2026 projections** (cut-off 22 May 2026): debt **111.3% / 112.9% / 114.8%** for 2026â28 (~**115%** by 2028); deficit path **â5.2 â â5.3 â â5.5 â â5.7%**. **FPB Jun 2025** (older horizon): deficit **5.4% â 6.5% by 2030**; debt **~120% GDP by 2030**. Snowball: primary deficit persists while interest rises â ratio climbs; fix is **primary surplus**, not labelling debt as L5 waste.
- Wrote: budgets debt stock+ratio path+deficit; commitment cmt_gg_debt_path; leaderboard lb_gg_debt_stock; entity gg_debt; sources NBB/FPB; rq_041=done; queued rq_043â044; ticks=43
- FOI: none
- Next: rq_042 Flanders BO2026 confirm or rq_043 Debt Agency EUR stock

### 2026-07-20T07:00:00Z â tick 44
- Unit: rq_042 (Flanders total expenditure BO2026 confirm)
- Found (strong): **DFB official page + parliament vote (Jan 2026):** BO2026 uitgaven **â¬66.0 bn**; **OV+WVG = 58%**. **Evaluatierapport:** consolidated **VEK â¬66.03 bn** (BA2025 **â¬66.47 bn**; constant-policy would be **â¬67.05 bn** â measures cut **~â¬1.01 bn**); **VAK â¬64.75 bn**. **Receipts â¬61.6 bn**; **ESR saldo ââ¬2.9 bn** (ââ¬1.7 bn after doelstelling corrections). Deltas: index **+â¬718.9 m**; VV **+â¬370.9 m**; rente **+â¬323.5 m**; retro premie **ââ¬301.6 m**; subsidies **ââ¬210 m**. Entity rank #4 reconfirmed (budgeted, not ESA TE).
- Wrote: multi-year budgets; commitment; programmes final VEK; entity/rank notes; sources; rq_042=done; queued rq_045 BA2026; ticks=44
- FOI: none
- Next: rq_043 Debt Agency stock or rq_044 primary balance gap

### 2026-07-20T07:20:00Z â tick 45
- Unit: rq_043 (Federal Debt Agency Entity I stock)
- Found (BDA Review 2025/Outlook 2026 PDF, strong): federal gross debt **â¬518.68 bn (end-2024)** â **â¬552.69 bn (end-2025)** **+â¬34.0 bn**. Composition end-2025: **OLO â¬462.8 bn**; TC **â¬42.9 bn**. **Avg life 10.38 â 9.98 years**; duration **8.43 â 7.27 y**; fixed rate **87.4%**; 12m refinancing risk **15.64%** (cap 17.5%); financial cost at issuance (EUR) **2.01%**. Gross borrow 2025 **â¬53.31 bn** / net **â¬28.35 bn**. Plan 2026: gross **â¬59.55 bn** / net **â¬26.37 bn** / OLO issue **â¬51.60 bn**. Live BDA site (medium): **â¬567.615 bn** on **2026-06-30**. Perimeter: federal BDA **~80%** of GG ESA **â¬692.7 bn** â do not double-count.
- Wrote: budgets multi-year + OLO/TC/borrow; commitment; entity debt_agency_be; leaderboard; sources + raw PDF; rq_043=done; ticks=45
- FOI: none
- Next: rq_044 primary balance gap or rq_045 Flanders BA2026

### 2026-07-20T07:40:00Z â tick 46
- Unit: rq_044 (Primary balance path vs debt-stabilising)
- Found (strong): **NBB Jun 2026 projections** primary balance **â2.9% / â2.8% / â2.7% / â2.7%** GDP for **2025â28** while overall deficit widens **â5.2 â â5.7%** (interest wedge growing). Debt **107.9 â 114.8%**. **IMF Art IV 2025**: primary ~**3.1 ppt of GDP below** debt-stabilising primary of **+0.3% GDP** â gap â **â¬19.9 bn** (0.031 Ã GDP â¬642.0 bn). **NBB Review 2025/11**: snowball = (râg)Ãdebt â primary; with **r>g** and primary deficit, debt path explosive unless primary improves. **EC/MTFSP**: planned structural primary improvement **+2.4 pp 2025â29** â delivery still open. Not L5 waste: the DOGE north star for fiscal math.
- Wrote: primary multi-year budgets; gap estimate; commitment; leaderboard lb_primary_gap; sources + NBB PDF; rq_044=done; queued rq_046 MTFSP; ticks=46
- FOI: none
- Next: rq_045 Flanders BA2026 or rq_046 MTFSP path

### 2026-07-20T08:00:00Z â tick 47
- Unit: rq_045 (Flanders BA2026 adaptation)
- Found (Rekenhof Jun 2026 + Vlaams Parlement, strong): BA2026 ESR **ontvangsten â¬62.2 bn** / **uitgaven â¬67.1 bn** â **vorderingensaldo ââ¬3.6 bn** (BO was ââ¬2.9 bn). Vs begrotingsdoelstelling (excl Oosterweel+relance): **ââ¬2.18 bn** (was ââ¬1.7 bn). Deltas vs BO: VEK **+â¬1.081 bn**, VAK **+â¬3.034 bn** (Lantis/Oosterweel VAK **+â¬2.514 bn**); index VEK **+â¬324.5 m**; Fluvius VEK **â¬1.1 bn**. OV **â¬20.2 bn VEK** / WVG **â¬17.8 bn VEK**. Schuld **+â¬6.8 bn** (+13.5% y/y); rating AA-. Entity rank #4 updated to **â¬67.1 bn**.
- Wrote: budgets BA lines; commitment supersede; programmes OV/WVG/total; rank+entity; sources + raw PDFs; rq_045=done; queued rq_047 VL debt; ticks=47
- FOI: none
- Next: rq_046 MTFSP or rq_047 Flanders debt stock

### 2026-07-20T08:20:00Z â tick 48
- Unit: rq_046 (Belgium MTFSP structural primary + net expenditure path)
- Found (official MTFSP PDF + Council rec Jun 2025, strong): **Structural primary balance** plan **â1.8 â â1.2 â â0.7 â 0.0 â +0.6% GDP (2025â29)** = **+2.4 pp** (matches EC country-report phrasing). **Net nationally financed primary expenditure growth**: **3.6 / 2.5 / 2.5 / 2.1 / 2.1%** â **5y avg 2.56%** (EC ref 2.53%). **Deficit path** to **â3.0% GDP by 2029**; plan debt peaks **107.3%** then **106.7%** â **actual 2025 already 107.9%** and NBB primary **â2.9%** worse than plan **â2.4%**. 7-year adjustment; Entity I/II split deferred (OverlegcomitÃ© Mar 2025 commitment). Delivery risk is the DOGE angle â not a waste line.
- Wrote: MTFSP budget rows; commitment cmt_be_mtfsp; leaderboard; sources + PDFs; rq_046=done; queued rq_048 Entity split; ticks=48
- FOI: none
- Next: rq_047 Flanders debt stock or rq_048 Entity I/II split

### 2026-07-20T08:40:00Z â tick 49
- Unit: rq_047 (Flanders consolidated Maastricht debt path)
- Found (Rekenhof Table 14, strong): consolidated Maastricht debt **â¬50.172 bn (end-2025)** â **â¬56.552 bn (BO2026)** â **â¬56.971 bn (BA2026)** = **+â¬6.799 bn / +13.5%** y/y. **Direct MVG debt** **â¬42.397 â â¬49.802 bn** (+â¬7.405 bn). Components BA2026: consolidated entities financial **â¬7.17 bn**; PPS **â¬0.64 bn**; green certs **â¬0.55 bn**; intra/inter-sector holdings corrections **ââ¬11.38 bn**. Debt/receipts **91.6%** (old schuldnorm target **<65%**). Netto-actief end-2024 **ââ¬13.3 bn**. Ratings: Fitch **AA-** (stable); S&P **AA-**; Moodyâs **A1**. Drivers: deficit, Oosterweel, relance, ESR 8/9 (Fluvius, social housingâ¦). Non-Maastricht federal claims: hospital infra **â¬2.184 bn** + autonomiefactor **â¬0.474 bn** (not in stock).
- Wrote: multi-year debt budgets; commitment; leaderboard; entity note; rq_047=done; queued rq_049 non-Maastricht claims; ticks=49
- FOI: none
- Next: rq_048 Entity I/II MTFSP split

### 2026-07-20T09:00:00Z â tick 50
- Unit: rq_048 (Entity I vs II MTFSP effort split)
- Found (strong): **MTFSP Mar 2025** deferred Entity I/II split. **HRF Apr 2025** (recalc of Jul 2024): **verdeelsleutel 3** = share of (final primary expenditure + own receipts) â preferred key. Differentiated **max net primary exp growth %** (7y path): **Entity I avg 2.72%** (2025 **3.81%**, 2026 **2.96%**); **Flanders 2.68%** (3.63 / 2.17); **FWB 1.52%**; **Wallonia 1.45%**; **Brussels â0.22%** (very tight); **DG negative**. **OverlegcomitÃ© Mar 2026** SWA: uses sleutel 3 for current plan; **fallback binding targets** if no agreement; control accounts via HRF; **defence national escape clause fully to federal** (Rekenhof/APR). GG outturn path still **3.8% / 2.0%** net exp 2025â26 (cumul 5.9% < 6.1% cap, APR). Parliaments still ratifying SWA.
- Wrote: entity growth-cap budgets; commitment; leaderboard; sources + HRF/APR PDFs; rq_048=done; queued rq_050 ratification; ticks=50
- FOI: none (method+caps public)
- Next: rq_049 Flanders non-Maastricht claims or rq_050 SWA ratification

### 2026-07-20T09:20:00Z â tick 51
- Unit: rq_049 (Flanders non-Maastricht federal claims)
- Found (Rekenhof BA2026 Â§5.1, strong): Flanders owes federal government **â¬2.1843 bn** (ziekenhuisinfrastructuur) + **â¬473.8 m** (definitieve vaststelling **autonomiefactor**) = **â¬2.658 bn** total. **Excluded from Maastricht** consolidated debt (â¬56.97 bn). Rekenhof: these stocks are **no longer reported in de algemene toelichting**; recommends Vlaams Parlement be kept informed. Multi-year amortisation cash-by-year **not public** this tick â FOI.
- Wrote: three budget rows; commitment; leaderboard; FOI gap_vl_non_maastricht_claims **ready** (not sent); rq_049=done; ticks=51
- FOI: gap_vl_non_maastricht_claims ready â human send only
- Next: rq_050 SWA ratification / control accounts

### 2026-07-20T09:40:00Z â tick 52
- Unit: rq_050 (SWA ratification + Entity control accounts)
- Found (strong/medium): **SWA timeline** â OverlegcomitÃ© **27 Mar 2026** draft economic-governance SWA (replaces **13 Dec 2013**); **Flanders government 8 May 2026** principal OK + draft assent decree â SERV/RvS; **federal Ministerraad 13 May 2026** draft assent law (secondary reports); **SERV advice Jun 2026**; Rekenhof Jun 2026: still needs each entity government + **parliament** assent â **full multi-parliament ratification not confirmed** this tick. **Entity I control account** (Kamer 56K1468, budget-basis approx): net exp **â¬190.3 bn (2025) / â¬196.9 bn (2026)**; growth **4.6% / 2.3%** vs HRF **3.81% / 2.96%**; annual deviation **+â¬1.5 / ââ¬1.3 bn**; cumul after defence flex **â0.30% / â0.71% GDP** (under norm). Official HRF multi-entity public ledgers not yet a complete published suite.
- Wrote: Entity I net-exp + control budgets; commitment/leaderboard update; sources + Kamer PDF; rq_050=done; queued rq_051â052; ticks=52
- FOI: none
- Next: rq_052 Flanders net-exp vs 2.17% cap (prio 4) or rq_051 regional SWA assent

### 2026-07-20T10:00:00Z â tick 53
- Unit: rq_052 (Flanders HRF net-exp compliance vs 2.17% cap)
- Found (BO2026 Algemene Toelichting Table 10 via eval/SERV, strong): HRF-concept **finale primaire uitgaven â¬63.047 bn (2025) / â¬62.106 bn (2026)**; **netto-uitgaven â¬62.036 / â¬61.296 bn**; after DRM **â¬60.761 bn (2026)**; **growth â2.1%** vs **HRF sleutel 3 cap +2.17%** â **margin â4.23 pp** (clearly **compliant** at BO). SERV: âlijkt te voldoenâ. **BA2026 (Rekenhof)**: calculation in Ch.VI still cited but **not on final BA numbers** (uses DBP/process estimates; admin lacks APR microdata) â method lag, not a re-computed growth % this tick. Do not invent BA growth.
- Wrote: net-exp stock + growth budgets; commitment; leaderboard; source + eval PDF; rq_052=done; queued rq_053 Wallonia 2026; ticks=53
- FOI: none
- Next: rq_053 Wallonia 2026 total (prio 5) or rq_051 regional SWA assent

### 2026-07-20T10:20:00Z â tick 54
- Unit: rq_053 (Wallonia total expenditure 2026 initial)
- Found (ExpGen budget initial 2026 official PDF, strong): **dÃ©penses â¬21.335748 bn** (was â¬22.029416 bn 2025 init, **ââ¬694 m**); **recettes â¬18.515734 bn**; **solde brut ââ¬2.820 bn**; **solde SEC ââ¬2.015736 bn** (path â2.015 / â1.124 / â0.600 / +0.039 bn 2026â29). Structural savings **â¬270.4 m**. Net primary exp **â¬19.463 â â¬19.056 bn** growth **â2.09%** vs CSF key cap **+0.92%** (~3 pp under, indicative). Entity rank #8 updated to 2026 envelope.
- Wrote: budgets multi-line; commitment; entity+rank; sources + PDF; rq_053=done; queued rq_054 FWB; ticks=54
- FOI: none
- Next: rq_054 FWB total or rq_051 regional SWA assent

### 2026-07-20T10:40:00Z â tick 55
- Unit: rq_054 (FWB total expenditure 2026 primary source)
- Found (DGBF Ã©lÃ©ments-clÃ©s official, strong): **initial 2026** recettes **â¬13.602 bn** / dÃ©penses liquidation **â¬15.406879 bn** / solde brut **ââ¬1.667 bn** / **SEC ââ¬1.608 bn**. Breakdown: Education-Recherche-Formation **â¬10.929 bn**; SantÃ©-Culture-Sport **â¬2.325 bn**; Services gÃ©nÃ©raux **â¬1.185 bn**; dette publique **â¬0.393 bn**; dotations RW/COCOF **â¬0.575 bn**. Multiyear SEC path **â1.608 / â1.405 / â1.390 / â1.224 bn** (2026â29). **Adjusted 2026** (gov press 30 Apr): recettes **â¬13.67 bn** / dÃ©penses **â¬15.59 bn** / deficit **â¬1.77 bn** (+â¬160 m vs initial 1.61). Supersedes medium ~â¬15 bn press estimate. Entity rank #9 updated strong.
- Wrote: budgets init+adj+edu; commitment; entity+rank; sources; rq_054=done; queued rq_055 Brussels; ticks=55
- FOI: none
- Next: rq_055 Brussels total or rq_051 regional SWA assent

### 2026-07-20T11:00:00Z â tick 56
- Unit: rq_055 (Brussels region 2026 total vs SGRBC 8bn)
- Found (Cour des comptes Budgets RBC 2026, strong): reconfirmed **SGRBC crÃ©dits liquidation â¬8.0 bn** / **engagement â¬8.9 bn** (+1.2% / +6.0% vs crÃ©dits provisoires 2025). **Solde financement SEC** entitÃ© rÃ©gionale **ââ¬956.6 m** (gov; Cour content-diff **ââ¬978.2 m**). **Solde net Ã  financer** SGRBC **ââ¬1.746 bn**. **Dette consolidÃ©e ~â¬16.1 bn** end-2025 (+â¬3.5 bn 2023â25); direct LT **â¬13.4 bn**; path cap +â¬3 bn to **>â¬19.1 bn** by 2029. Top lines: **STIB â¬1.168 bn**; Actiris **â¬648 m**; commissions communautaires **â¬692 m**; dettes service **â¬728 m** liq. HRF net primary path for BCR **â0.61% 2026** not reported in exposÃ© â rq_056. Dual perimeter: SGRBC 8.0bn â  press â7.6/6.6 bnâ manoeuvrable figures.
- Wrote: SEC/debt/net-financer budgets; commitment; entity+rank notes; source update + PDF; rq_055=done; queued rq_056; ticks=56
- FOI: none
- Next: rq_056 Brussels net-exp vs HRF or rq_051 regional SWA assent

### 2026-07-20T11:20:00Z â tick 57
- Unit: rq_056 (Brussels net primary exp vs HRF â0.61%)
- Found (strong): **HRF Apr 2025** BCR (+locals) net primary growth caps: **+2.03% (2025)** / **â0.61% (2026)** / avg **â0.22% (2025â31)** â tightest large entity path. **Cour des comptes Budgets RBC 2026**: exposÃ© confirms multi-year spending cuts narrative but **does not publish** the EU/HRF **dÃ©penses primaires nettes** growth rate â compliance **cannot be scored** from public budget tables alone. **SGRBC liquidation +1.2%** (Cour) is a **different metric** (gross credits) â not a substitute for net-primary compliance (do not invent a verdict). FOI for official calculation.
- Wrote: HRF cap budgets; leaderboard opacity; commitment note; FOI gap_bru_net_primary **ready**; rq_056=done; queued rq_057 STIB multi-year; ticks=57
- FOI: gap_bru_net_primary ready (not sent)
- Next: rq_057 STIB multi-year or rq_051 regional SWA assent

### 2026-07-20T11:40:00Z â tick 58
- Unit: rq_057 (STIB multi-year regional financing)
- Found (strong): **Regional programme 42.112** budget 2026 **â¬1.167619 bn** (+â¬51.3 m vs 2025 provisional). **STIB statutory accounts â Intervention RBC fonctionnement**: **â¬546.1 m (2023)** â **â¬633.1 m (2024)** â **â¬642.5 m (2025)** (not equal to full 42.112 package). **Capital grants** recognized **â¬348.9 m (2025)**. **Investment programme** executed **â¬475 m (2024)** / **â¬427.4 m (2025)**; **PPI path** **â¬591.5 / 666.1 / 768.6 / 724.4 m (2026â29)** but Cour: must cut **â¬964.6 m** vs STIB 2025 PPI plan (Metro 3 + other arbitrages). Compare De Lijn: still **~â¬1.14 bn class medium** + FOI gap_de_lijn_dotatie. Dual perimeter: company opex intervention â  regional budget line.
- Wrote: multi-year opex/invest/PPI budgets; commitment; leaderboard; sources + STIB PDFs; entity note; rq_057=done; queued rq_058 TEC; ticks=58
- FOI: none new
- Next: rq_058 TEC multi-year or rq_051 regional SWA assent

### 2026-07-20T12:00:00Z â tick 59
- Unit: rq_058 (TEC/OTW Wallonia multi-year subsidy)
- Found (strong dual-perimeter): **Minister Henry PQ 596** (Apr 2024): OTW **financing â¬960 m (2024)** â **â¬1.003 bn (2028)** indexation; **+â¬200 m** step 2023â24; **invest plan â¬1.586 bn (2024â28)**. **Cour des comptes RW BI2025**: OTW **company recettes â¬1.088.8 m / dÃ©penses â¬1.200.6 m**; SEC recettes â¬1.018.4 m / solde **ââ¬139.4 m**; regional **programme 14.045** CL **â¬813.7 m (2024) â â¬861.1 m (2025)**. **Dolimont** official: **+â¬45 m 2025 vs 2024 hors PRW** (corrects earlier âcutâ mislabel). **Desquesnes CSP note Dec 2025**: rewrite 2026â29; coverage **10%ââ¥14% by 2030**; internal savings **â¬20 m by 2029**; TÃ D **â¬22 m 2028â29**. Absolute AB cash series 2023â26 + 2026 CSP socle still incomplete â FOI.
- Wrote: entity `tec`; 14 budget rows; commitment multi-year; fixed cmt_tec +45m; leaderboard; 4 sources + Cour PDF raw; rq_058=done; ticks=59
- FOI: gap_otw_dotatie_cash **ready** (not sent)
- Next: rq_051 Wallonia/FWB/Brussels SWA assent

### 2026-07-20T12:15:00Z â tick 60
- Unit: rq_051 (Wallonia / FWB / Brussels SWA economic-governance assent)
- Found (strong government track; weak final votes): **OverlegcomitÃ© 27 Mar 2026** closed multi-entity SWA (replaces 2013). **FWB gouvernement 30 Apr 2026** ODJ point 14: **1st reading** avant-projet dÃ©cret assentiment (Doc 1589). **Wallonie GW 13 May 2026** ODJ B5: **1st reading** avant-projets dÃ©crets assentiment (Doc 2760). **Federal Ministerraad 13 May 2026**: avant-projet de **loi** assentiment approved (Van Peteghem). **Flanders** 8 May principal + SERV advice **1 Jun 2026**. **PFWB commission** (Degryse): all entities agreed text; legislative path aimed **summer multi-parliament**; uses **HRF mixte clÃ©**; WAL/FWB may split shared norm; default future key 50/50 CSF+BE. **Dolimont PQ 30 Mar** still pre-deal (negotiation). **Brussels** government/parliament public assent dossier **not found** this tick. **No final adopted assent law/decree** found for any parliament as of tick.
- Wrote: sources (+5) + raw PDFs; updated commitment/leaderboard; rq_051=done; seeded rq_059 final votes + rq_060 WAL net-exp; ticks=60
- FOI: none (legislative process opacity, not a cash FOI)
- Next: rq_060 Wallonia net-primary vs HRF or rq_059 final SWA votes

### 2026-07-20T12:30:00Z â tick 61
- Unit: rq_060 (Wallonia net primary exp vs HRF)
- Found (strong): **HRF Apr 2025 sleutel 3** Waals Gewest (+locals): max net primary growth **2.65% (2025) / 0.92% (2026)** / avg **1.45% (2025â31)**. **ExpGen BI2026 Table 3**: dÃ©penses primaires nettes **â¬19.463 bn (2025) â â¬19.056 bn (2026)**; growth **â2.09%** vs norme CSF/HRF **+0.92%** â **margin â3.01 pp** (clearly **compliant** / under cap). Breakdown: total exp 20.973â20.694; âinterest âEU âcofin âDRM âone-off. ExpGen noted key still uncertain at budget drafting (pre-SWA); post-tick-60 SWA confirms mixte HRF key applies. Parallel Flanders BO: â2.1% vs 2.17% cap; Brussels still FOI opaque.
- Wrote: HRF 2026 cap + margin budgets; commitment; leaderboard; rq_060=done; ticks=61
- FOI: none
- Next: rq_059 multi-parliament final SWA votes (only open public task) or seed new L5

### 2026-07-20T12:45:00Z â tick 62
- Unit: rq_061 (FWB net primary exp vs HRF 0.74%)
- Found (strong cap; strong opacity): **HRF sleutel 3** Franse Gemeenschap: **2.75% (2025) / 0.74% (2026)** / avg **1.52%**. **DGBF Ã©lÃ©ments-clÃ©s 2026**: dep **â¬15.407 bn** / recettes **â¬13.602 bn** / SEC **ââ¬1.608 bn** â **no** net-primary growth table. **Cour des comptes** (PFWB commission on adj 2025): exposÃ© **omits** dÃ©penses primaires nettes vs CSF **2.75%**; gov acknowledged and **postponed** integration / said would not compare to CSF given joint WALâFWB path. Adjusted 2026 press: dep **â¬15.59 bn** deficit **â¬1.77 bn** â still not net-primary. **Cannot score compliance** without inventing euros (do not use gross dep growth as proxy). Parallel: Flanders/Wallonia published tables; Brussels FOI already.
- Wrote: HRF 2026 cap budget; commitment; leaderboard opacity; sources + Cour PDF raw; FOI gap_fwb_net_primary **ready**; rq_061=done; ticks=62
- FOI: gap_fwb_net_primary ready (not sent)
- Next: rq_062 Namur/Mons L5 (prio 5) or rq_059 final SWA votes

### 2026-07-20T13:00:00Z â tick 63
- Unit: rq_062 (Namur city L5 subsidy sample)
- Found (strong, official DGF note BI2026, Conseil 16 Dec 2025): **Recettes â¬301.394 m** / **dÃ©penses â¬300.761 m** / **boni exercice propre â¬0.633 m**. **Structural deficit â¬19.809 m** after stripping Plan OxygÃ¨ne exceptional + CPAS provision. **OxygÃ¨ne draw â¬45.678 m** (max 2026 + solde 2024). Transfers: **CPAS â¬24.15 m**; **Police â¬27.59 m**; **Secours NAGE â¬6.24 m**. **Monde associatif â¬8.471 m (â9.82% / ââ¬0.923 m)** with full L5 table: **SONEFA â¬2.633 m** (protected); **CCR â¬0.715 m**; **piÃ©tonnier primes â¬0.700 m**; **NEW â¬0.414 m**; **OTN â¬0.397 m**; **CAC â¬0.360 m**; **Namur 2030 ââ¬0.500 m** full cut; linear **â20%** associations / **â10%** para-communal. Fabriques dâÃ©glise **â¬1.418 m**. Open data `subsides-attribues` only to **2020** (stale). Mons deferred to rq_063.
- Wrote: entity city_namur; 19 budgets; 2 commitments; leaderboard OxygÃ¨ne; sources + DGF PDF raw; rq_062=done; seeded rq_063 Mons; ticks=63
- FOI: none (2026 L5 table public; open-data lag noted)
- Next: rq_063 Mons L5 or rq_059 final SWA votes

### 2026-07-20T13:15:00Z â tick 64
- Unit: rq_063 (Mons city L5 subsidy sample)
- Found (mixed): **MonsMag #133** (official Ville de Mons): BI2026 **recettes â¬242.5 m**, **boni â¬2.1 m**, departmental **economies â¬8 m**, Plan OxygÃ¨ne **â¬27 m**, invest **â¬12 m**, exceptional precarity aid **â¬200k**, Walloon cut **â¬5 m**, **4P ~â¬25 m** narrative. **CPAS â¬27.7 m (+â¬2.1 m)** RTBF quoting collÃ¨ge (medium). **Official full BI2026 PDF not on mons.be** (archives stop at 2024 presentations; compte 2025 published). **Budget 2025 strong**: recettes **â¬246.24 m** / dÃ©penses **â¬244.18 m**. **L5 2025** (article lines): MARS fonct **â¬400k** + music **â¬124k** + anim **â¬150k**; Basket UMH **â¬220k** + sponsor **â¬250k**; RCA **â¬380k**; Film festival **â¬45k**.
- Wrote: entity city_mons; 16 budgets; 2 commitments; leaderboard; sources + Mag/compte PDFs; FOI gap_mons_budget_l5 **ready**; rq_063=done; ticks=64
- FOI: gap_mons_budget_l5 ready (not sent)
- Next: rq_059 multi-parliament final SWA votes (only remaining open public task) or seed new research

### 2026-07-21T08:00:00Z â tick 65
- Unit: rq_064 (Plan OxygÃ¨ne multi-city envelope)
- Found (strong dual track): **Collignon PQ Feb 2023**: 34 communes requested **â¬1.791 bn** cumul 2022â26; GW validated **tranche 2022 â¬302.1 m** for **21 communes** (interest full + 15% capital for 16/21). **Desquesnes Jul 2025**: first **2025 bank lot â¬66.1 m** / **15 communes** (ING **â¬40.86 m** 13c; Belfius **â¬25.29 m** Tournai+Verviers) with named amounts (e.g. Herstal **â¬8.52 m**, Verviers **â¬19.25 m**, Huy **â¬6.01 m**). **Desquesnes CRI Dec 2025**: 6 large cities without bank offer â **CRAC borrows â¬210 m** (2Ãâ¬105 m) and on-lends **2025** draw rights; regional cost ~**â¬25 m/yr** for 21 communes. City samples already: Namur **â¬45.7 m** 2026 strong; Mons **â¬27 m** Mag; Charleroi ~**â¬48 m** medium. Full multi-year per-commune table still incomplete â FOI.
- Wrote: budgets (envelope + 2025 named); commitment; leaderboard; sources + CRI PDF; FOI gap_plan_oxygene_cash **ready**; rq_064=done; ticks=65
- FOI: gap_plan_oxygene_cash ready (not sent)
- Next: rq_065 FEDER L5 (prio 4) or rq_059 final SWA votes (prio 3)


















### 2026-07-21T08:20:00Z ï¿½ tick 66
- Unit: rq_065 (FEDER Wallonia named project L5 sample)
- Found (strong, official Rï¿½sumï¿½ citoyen 2025 WalEurope PDF): **Programme invest class ï¿½1.488 bn** (EU **~ï¿½600 m**); **FTJ envelope ï¿½456 m** (EU **~ï¿½183 m**, Charleroi/Mons/Tournai); **374 FEDER + 62 FTJ** public projects retained. Named L5 grants (total / FEDER / Wallonie): **Campus4U Charleroi HELHa+UCLouvain ï¿½21.302 m / ï¿½8.521 m / ï¿½12.781 m**; **Liï¿½ge Fontainebleau/Sainte-Marguerite ï¿½10.032 m / ï¿½4.459 m / ï¿½5.574 m**; **Namur ville apaisï¿½e portfolio ï¿½5.019 m / ï¿½2.231 m / ï¿½2.789 m**; **DUNE3S ï¿½3.989 m / ï¿½1.835 m / ï¿½2.154 m**; **IDEA CLICK Mons ï¿½0.566 m**; **Arlon cyclo-piï¿½ton ï¿½0.521 m**; **Cap Innove ID2GREEN ï¿½0.226 m**; **ICE Louvain ï¿½0.223 m**. Co-financed investment ï¿½ **not pure waste**; residual issue is incomplete machine-readable full L5 cash list (resume samples only).
- Wrote: 14 budgets; 9 commitments; 4 leaderboard; 2 sources; entities city_arlon + waleurope; rq_065=done; ticks=66
- FOI: none new (named L5 public; full 374+62 register optional later)
- Next: **rq_059** multi-parliament final SWA assent votes (only remaining open public task at prio 3) or seed Flanders EFRO 2021-27 L5

### 2026-07-21T08:35:00Z ï¿½ tick 67
- Unit: rq_059 (multi-parliament final SWA economic-governance assent votes)
- Found (strong process; **no final votes**): Reconfirmed Overlegcomitï¿½ **27 Mar 2026** SWA (replaces 2013); **VL Regering 8 May** principal OK voorontwerp decree; **SERV 1 Jun** advice; **Vlaams Parlement Ingekomen 60-Nr.33 (17 Jun 2026)** only registers SERV mededeling ï¿½ **not** a plenary-adopted instemmingsdecreet. Federal **MR 13 May** avant-projet de loi; **FWB 30 Apr** / **WAL 13 May** GW first readings (tick60). **Brussels** public assent dossier still **not found**. Searches of Kamer/VP/PW/PFWB + BS class: **no final plenaire adoption dates** as of **2026-07-21**. Degryse summer multi-parliament target **not evidenced**.
- Wrote: 2 sources; updated cmt_entity_mtfsp_split + lb_entity_split_opacity; rq_059=done; seeded **rq_066** recheck + **rq_067** Flanders EFRO L5; ticks=67
- FOI: none (parliamentary tracking, not budget opacity letter)
- Next: **rq_067** Flanders EFRO named L5 (prio 4) or **rq_066** SWA recheck (prio 3)

### 2026-07-21T08:50:00Z ï¿½ tick 68
- Unit: rq_067 (Flanders EFRO/Interreg 2021-27 named L5 sample)
- Found (strong programme; partial L5): **EFRO Vlaanderen EU ï¿½276.078 m** (meer ontwikkeld **ï¿½163.516 m** + Limburg transitie **ï¿½112.563 m**); total programme budget class **~ï¿½596 m** (40%/60% co-financing). Priorities: Slim **ï¿½160.045 m** / Duurzaam **ï¿½106.697 m**. Named GTI slices: Kempen **ï¿½10.885 m**; West-Vlaanderen **ï¿½25.728 m**; stedelijke ontwikkeling Antwerpen+Gent **ï¿½19.791 m** (Themis VR mededeling). **Interreg VL-NL**: keep.eu total **ï¿½410.811 m** / EU **ï¿½205.406 m**; portal **110** projects, **ï¿½205.5 m** allocated; themes slim **ï¿½72.5 m** / groen **ï¿½73.6 m** / sociaal **ï¿½47.1 m** / grenzen **ï¿½7.3 m**. VLAIO bulk project portal **blocked/incomplete** for individual 2021-27 project EUR this tick; older 2014-20 L5 not used as 2021-27 sample.
- Wrote: 16 budgets; 5 commitments; 3 leaderboard; 4 sources; entities vlaio+interreg_vlaned; FOI gap_vl_efro_l5 **ready**; rq_067=done; seeded rq_068 Brussels EFRO; ticks=68
- FOI: gap_vl_efro_l5 ready (not sent)
- Next: **rq_068** Brussels EFRO L5 (prio 4) or **rq_066** SWA recheck (prio 3)

### 2026-07-21T09:05:00Z ï¿½ tick 69
- Unit: rq_068 (Brussels EFRO/FEDER 2021-27 L5 sample)
- Found (strong OP; reclassified press figure): Official OP PDF: **EU ï¿½121.284 m** + national **ï¿½181.926 m** = **total ï¿½303.210 m** (40% EU). Priorities totals: **P1 ï¿½125.832 m** / **P2 ï¿½136.445 m** / **P3 ï¿½13.644 m** / **P4 ï¿½27.289 m**. be.brussels (06.07.2026): **120 projects selected** under 2021-27; **ï¿½191 m / 68 projects is 2014-2020 results**, not current OP. Named **call envelopes** (FEDER+RBC): digital OS1.2 **ï¿½29.222 m**; saut qualitatif **ï¿½15.142 m**; accompagnement PME **ï¿½6.679 m**. Individual project EUR bulk incomplete ? FOI.
- Wrote: 13 budgets; 5 commitments; 3 leaderboard; 5 sources; entity feder_brussels; FOI gap_bru_efro_l5 **ready**; rq_068=done; seeded rq_069 DG; ticks=69
- FOI: gap_bru_efro_l5 ready (not sent)
- Next: **rq_069** German-speaking Community budget (prio 4) or **rq_066** SWA recheck (prio 3)

### 2026-07-21T09:20:00Z ï¿½ tick 70
- Unit: rq_069 (German-speaking Community / Ostbelgien budget + L5 sample)
- Found (strong, Rechnungshof 13 Nov 2024 UHH 2025): **Hauptverwaltung Ausgaben AE ï¿½685.707 m** / VE **ï¿½687.602 m**; Einnahmen **ï¿½595.819 m**; **konsolidierter ESVG-Saldo -ï¿½113.878 m** (Investitionen **ï¿½104.4 m** im Defizitpfad). Einnahmen: **Bundesdotation ï¿½342.5 m** (allgemein 321.3 + zweckgeb. 21.2); **Wallonie-Transfer ï¿½93.1 m**; Anleihen **ï¿½111.2 m** (davon RRF ~ï¿½11.2 m). AE nach OB: **Unterricht ï¿½187.097 m**; **Gesundheit/Soziales ï¿½146.039 m**; **Infrastruktur ï¿½103.773 m**; **Kultur/Sport/Jugend ï¿½22.792 m**. Infrastrukturplan: **142 Projekte / ï¿½94.2 m**; IT **ï¿½6.5 m**; Kommunaldotationen Unterhalt **ï¿½3.0 m**. Paasch/BRF Okt 2025 (medium): Sparpakete **~ï¿½23 m/Jahr** + Infra-Kï¿½rzung **ï¿½32 m**; Krankenhaus-Investbedarf **=ï¿½150 m** (zwei Hï¿½user).
- Wrote: 18 budgets; 3 commitments; 3 leaderboard; 3 sources; entity dg_gov; rq_069=done; seeded rq_070 province; ticks=70
- FOI: none (CoA tables public for totals + domain L4)
- Next: **rq_066** SWA final votes recheck (prio 3) or **rq_070** province L1 (prio 3)

### 2026-07-21T09:35:00Z ï¿½ tick 71
- Unit: rq_066 (SWA multi-parliament final assent recheck)
- Found (strong process; **still no final votes**): Reconfirmed Overleg **27 Mar 2026** SWA (Van Peteghem historic announcement). Public track still maxes at **government first readings** (VL 8 May principal + SERV 1 Jun filed VP 17 Jun; Fed MR 13 May avant-projet; FWB 30 Apr; WAL 13 May). Searches Kamer / Vlaams Parlement / Wallonie / FWB / Brussels + BS class: **no final plenary assent law/decree and no BS publication** for this SWA as of **2026-07-21**. Brussels public dossier still missing. Summer multi-parliament path remains **not evidenced**.
- Wrote: 2 sources; updated cmt_entity_mtfsp_split + lb_entity_split_opacity; rq_066=done; seeded **rq_071** lower-prio recheck; ticks=71
- FOI: none (process tracking)
- Next: **rq_070** Province Liï¿½ge/Luxembourg budget L1+L5 (prio 3)

### 2026-07-21T09:50:00Z ï¿½ tick 72
- Unit: rq_070 (Province de Liï¿½ge budget L1 + L5 sample)
- Found (strong, official Budget 2026 PDF 25-26/010): **Service ordinaire** recettes **ï¿½563.597 m** / dï¿½penses **ï¿½563.574 m** (boni **ï¿½22.968**). **2025 aprï¿½s MB** ~**ï¿½696.4 m** dep. Compte **2024** dï¿½p. eng. **ï¿½664.5 m**. **Extraordinaire 2026** recettes **ï¿½68.151 m** / dï¿½p. **ï¿½68.140 m**. Combined dep. **~ï¿½631.7 m**. Named: **prï¿½compte immobilier ï¿½258.5 m** rec; **fonds des provinces ï¿½40.1 m**; **zones de secours provincial ï¿½45.600 m** (zones 1ï¿½5 **ï¿½44.428 m** + zone 6 DG **ï¿½1.172 m**); **enseignement secondaire ï¿½142.197 m**; **supï¿½rieur ï¿½69.302 m**; **sports ï¿½8.311 m**; **Opï¿½ra Royal Wallonie ï¿½150k**; **OPL ï¿½70k**.
- Wrote: 17 budgets; 3 commitments; 3 leaderboard; 2 sources; entity prov_liege; raw PDF; rq_070=done; seeded rq_072 Lux province; ticks=72
- FOI: none (official full budget public)
- Next: **rq_072** Province Luxembourg budget or **rq_071** SWA recheck (prio 2)

### 2026-07-22T10:20:00Z â tick 73
- Unit: rq_072 (Province de Luxembourg budget L1 + L5 sample)
- Found (strong, Cour des comptes 2026_15 projet budget 2026, FR chamber 19 Nov 2025): **Ordinaire exercice propre** recettes **EUR 135,214,912** / depenses **EUR 134,300,069** (boni **EUR 914,843**); global boni **EUR 1,687,264**. **Extraordinaire propre** rec **EUR 11,993,107** / dep **EUR 11,345,396**; global dep **EUR 13,345,396** (incl 2m FRE Plan investissement). Combined propre dep **~EUR 145.6 m** (~4x smaller than Liege ord). Named: **precompte additionnels ~EUR 74.4 m**; **fonds des provinces EUR 14.3 m**; **zones de secours EUR 18.0 m** (16.0m securite civile + 2.0m complement supracommunal); **personnel EUR 79.2 m**; **transferts EUR 32.3 m**; **ASBL/FUP aids >=50k EUR 4.3 m** (-0.9m vs 2025); invest extra **EUR 9.4 m** incl **Maison culture Arlon roof EUR 2.8 m** (contingent Ville d Arlon). GSM mast tax 0.6m + matching provision dual-track honesty. Pension Ethias covers ~3.1m under-inscription vs SFP.
- Wrote: 22 budgets; 3 commitments; 3 leaderboard; 2 sources; entity prov_luxembourg; raw CoA PDF; rq_072=done; seeded rq_073 Namur/Hainaut; ticks=73
- FOI: none (CoA projet public; final adopted budget may differ slightly)
- Next: **rq_073** Province Namur or Hainaut (prio 3) or **rq_071** SWA recheck (prio 2)

### 2026-07-22T10:35:00Z â tick 74
- Unit: rq_073 (Province de Namur budget L1 + L5 sample)
- Found (strong, Cour des comptes 2026_14 projet budget 2026, FR chamber 25 Nov 2025): **Ordinaire exercice propre** recettes **EUR 204,224,474** / depenses **EUR 204,222,043** (boni **EUR 2,431** near-zero); global boni **EUR 30.5 m**. **Extraordinaire propre** rec **EUR 11,303,046** / dep **EUR 17,789,888**; global dep **EUR 19,334,888**. Combined propre dep **~EUR 222.0 m** (between Lux ~135m and Liege ~564m ord). Named: **precompte prudent ~EUR 91.8 m** (tutelle 93.1m -1.4pct); **fonds des provinces ~EUR 24.4 m** (tutelle 24.9m -0.5m); **zones de secours EUR 30.3 m** (27.2m dotation + 3.1m complement RW; trajectory to 44m by 2030); **personnel EUR 125.7 m** (~60pct); **transferts EUR 45.3 m**; **supracommunalite communes +EUR 0.5 m** new line; invest extra **EUR 17.5 m**. CoA flags pension Ethias off-budget ~EUR 10m and debt-charge annex mismatches. ASBL consolidated list 10 entities â no aggregate EUR in CoA body.
- Wrote: 23 budgets; 3 commitments; 3 leaderboard; 2 sources; entity prov_namur; raw CoA PDF; rq_073=done; seeded rq_074 Hainaut; ticks=74
- FOI: none (CoA projet public)
- Next: **rq_074** Province Hainaut (prio 3) or **rq_071** SWA recheck (prio 2)

### 2026-07-22T10:50:00Z â tick 75
- Unit: rq_074 (Province de Hainaut budget L1 + L5 sample)
- Found (strong, Cour des comptes 2026_13 projet budget 2026, FR chamber 16 Dec 2025): **Ordinaire exercice propre** recettes **EUR 831,167,239** / depenses **EUR 830,647,769** (boni **EUR 519,470**); global boni **EUR 27.0 m**. **Extraordinaire propre** rec **EUR 21,823,057** / dep **EUR 23,485,170**; global dep **EUR 24,302,283**. Combined propre dep **~EUR 854.1 m** â **largest Walloon province** (vs Liege ord ~564m). Named: **precompte ~EUR 286.7 m**; **fonds des provinces EUR 71.3 m**; **zones de secours EUR 78.2 m** transfer (6.9+7.1+64.2) **+ provision EUR 6.0 m** for tutelle Oct path (total effective ~84.2m; trajectory to **EUR 127.3 m by 2030**); **personnel EUR 621.4 m** (~75pct); **transferts EUR 93.6 m**; **ASBL Voies d eau EUR 2.3 m** (+1.8m severance); **CathÃ©drale Tournai invest EUR 3.9 m** (RW subside 3.7m); taxes provinciales **EUR 9.4 m** (new taxes 3.8m). Consolidated ASBL list **199** entities â no aggregate EUR. CoA: pension under-inscription 2.1m.
- Wrote: 23 budgets; 3 commitments; 3 leaderboard; 2 sources; entity prov_hainaut; raw CoA PDF; rq_074=done; seeded rq_075 Brabant wallon; ticks=75
- FOI: none (CoA projet public)
- Next: **rq_075** Province Brabant wallon (prio 3) or **rq_071** SWA recheck (prio 2)

### 2026-07-22T11:05:00Z â tick 76
- Unit: rq_075 (Province du Brabant wallon budget L1 + L5 sample)
- Found (strong, Cour des comptes 2026_11 projet budget 2026, FR chamber 25 Nov 2025): **Ordinaire exercice propre** recettes **EUR 200,776,958** / depenses **EUR 199,406,787** (boni **EUR 1,370,172**); global boni **EUR 2.7 m**. **Extraordinaire propre** rec **EUR 8,699,156** / dep **EUR 16,331,910** (= global dep). Combined propre dep **~EUR 215.7 m** (Namur-scale). Named: **precompte ~EUR 102.9 m**; **fonds des provinces EUR 13.9 m**; **zones de secours EUR 16.1 m** (flat vs 2025; RW path **17.5 m** 2026 / **28.8 m** 2030; province cites 4m provision + 3m reserve buffer); **personnel EUR 136.8 m** (~69pct); **transferts EUR 27.3 m**; **ASBL/FUP >=50k EUR 10.0 m** (31 entities with justifications); invest: bassins d orage **EUR 3.1 m**, Helecine brasserie **EUR 1.3 m**, cycle points-noeuds **EUR 1.2 m**. **Completes 5/5 Walloon provinces** CoA 2026 map (Hainaut 831m > Liege 564m > Namur 204m ~ BW 199m > Lux 134m ord dep).
- Wrote: 24 budgets; 3 commitments; 3 leaderboard; 2 sources; entity prov_brabant_wallon; raw CoA PDF; rq_075=done; seeded rq_076 compare + rq_077 Flanders province; ticks=76
- FOI: none (CoA projet public)
- Next: **rq_076** Walloon provinces compare (prio 3) or **rq_071** SWA recheck (prio 2) or **rq_077** Flemish province

### 2026-07-22T11:20:00Z â tick 77
- Unit: rq_076 (Walloon provinces 2026 comparative snapshot)
- Found (strong synthesis, no new primary PDF): 5-province map from ticks 72-76.

| Province | Ord dep | Total | Zones |
|---|---:|---:|---:|
| Hainaut | 830.6m | 854.1m | 78.2m (+6m prov) |
| Liege | 563.6m | 631.7m | 45.6m |
| Namur | 204.2m | 222.0m | 30.3m |
| Brabant wallon | 199.4m | 215.7m | 16.1m |
| Luxembourg | 134.3m | 145.6m | 18.0m |
| **Sum** | **1932.2m** | **2069.2m** | **188.2m** |

- Ord sum **EUR 1,932,150,627** (~EUR 1.93 bn); total ord+extra **EUR 2,069,243,296**; zones transfer sum **EUR 188,199,958** (+ Hainaut provision **EUR 6.0 m** â **EUR 194,199,958**). PrÃ©compte sum **EUR 814,300,000**; fonds des provinces sum **EUR 164,015,104**. Hainaut alone **43.0%** of ord dep. Zones/ord **9.7%**. Caveat: Liege = official province PDF; others = CoA projet.
- Wrote: walloon_provinces_2026_snapshot.md; 6 budgets; 2 commitments; 2 leaderboard; 1 source; rq_076=done; ticks=77
- FOI: none
- Next: **rq_077** Flemish province sample (prio 3) or **rq_071** SWA recheck (prio 2)

### 2026-07-22T11:35:00Z â tick 78
- Unit: rq_077 (Provincie Antwerpen MJP 2026 L1 + L5 sample)
- Found (strong, official Initieel meerjarenplan 2026-2031 begincrediet): **Exploitatie-uitgaven EUR 204,700,675** / ontvangsten **EUR 236,862,206** (saldo **EUR 32,161,531**). **Investeringsuitgaven EUR 60,420,600**. Financiering aflossingen **EUR 9,215,000**. Combined cash-out **~EUR 274.3 m**. Named: **bezoldigingen EUR 92,014,823**; **toegestane werkingssubsidies EUR 63,828,156** (APB **EUR 38,925,780** + andere **EUR 22,907,585**); **opcentiemen OV EUR 172,132,240** (aanslagvoet 160); **bedrijvenbelasting EUR 52,101,340** (gezinnen provinciebelasting afgeschaft 2026); **Mondiaal Beleid EUR 1,166,000**; waterlopen invest **EUR 5,000,000**; wegen/infra invest **EUR 23,900,000**; schuld EOY **EUR 19,895,000**. BBC structure (not Walloon ord/extra) â exp scale similar Namur/BW (~200m).
- Wrote: 18 budgets; 3 commitments; 3 leaderboard; 2 sources; entity prov_antwerpen; raw MJP PDF; rq_077=done; seeded rq_078 Oost/West-VL; ticks=78
- FOI: none (official MJP public)
- Next: **rq_078** second Flemish province (prio 3) or **rq_071** SWA recheck (prio 2)

### 2026-07-22T11:50:00Z â tick 79
- Unit: rq_078 (Provincie West-Vlaanderen MJP 2026-2031 L1 + L5 sample)
- Found (strong debt/invest/AFM; medium subsidy class â M2/T2 tables largely image-only): Official fin-nota PDF PR **27 Nov 2025**. **Invest 2026-2031 EUR 363,500,000** (own patrim **EUR 246,500,000** + grants-out **EUR 116,900,000**; avg **~EUR 60m/yr**). **Invest receipts EUR 52,600,000** over 6y (Fietsfonds-heavy). **Debt 01/01/2026 EUR 92,341,480** â **EOY 2031 EUR 207,200,000**; new loans **EUR 190,000,000** (2026 chart **EUR 28,250,000**). **BBR 2026 EUR 15,204,117**; **AFM 2026 EUR 10,913,984** / 2031 **EUR 8,697,410** (structureel evenwicht OK). **Werkingssubsidies class ~EUR 55m/yr** (~1/4 exp; T2 not OCR); agencies **~EUR 35m** (POM/Inagro/Westtoer); **WFIV base EUR 400,000**. Opcentiemen rate **186.22** (VLABEL 13 Sep 2025; chart ~115-155m not digitised). Second-home tax RvS relief **EUR 9m**. Pension responsabilisering **EUR 2.84m** 2026 â 4.89m 2030. Full single-year exploitatie-uitgaven total **not text-extracted** (image tables).
- Wrote: 18 budgets; 3 commitments; 3 leaderboard; 2 sources; entity prov_west_vlaanderen; raw PDF; rq_078=done; seeded rq_079 Oost-VL; ticks=79
- FOI: none (public MJP; residual gap is extractability not opacity)
- Next: **rq_079** Oost-Vlaanderen (prio 3) or **rq_071** SWA recheck (prio 2)

### 2026-07-22T12:05:00Z â tick 80
- Unit: rq_079 (Provincie Oost-Vlaanderen MJP 2026 L1 + L5 sample)
- Found (strong, official Beleidsverklaring MJP 2026-2031, PR **3 Dec 2025**): **BBR 2026 EUR 24,848,155**; **AFM 2026 EUR 11,072,221**. **Invest uitgaven 2026 EUR 62,639,681** / ontvangsten **EUR 17,664,245**; **period sum 2026-31 EUR 399,702,621** (~400m). Named packages: **fiets EUR 86,728,852**; **water EUR 42,479,729**; **domeinen EUR 41,590,056**; **PAULO EUR 9,081,388**; Hamme **EUR 14,000,000**; Eeklo **EUR 10,000,000**; Zottegem **EUR 13,091,771**; Lokeren DBFM **EUR 74,031,570**. **Personeel 2026 EUR 211,963,313** (admin **EUR 122,978,678** + VL-gesub onderwijs **EUR 86,831,616**). **Belastingen 2026 EUR 181,554,643** (opcentiemen **EUR 110,542,196** rate **148.47**; APB **EUR 70,012,447**; APB **-10pct from 2028**). **Debt EOY 2026 EUR 17,380,658** â **2031 EUR 193,913,424**; bank start **EUR 11,356,366**; max loans **EUR 130,000,000**. Inwoners 1.01.2025: **1,602,532**. Full single-year exploitatie-uitgaven total not in this PDF (see T2 reference).
- Wrote: 23 budgets; 3 commitments; 3 leaderboard; 2 sources; entity prov_oost_vlaanderen; raw beleidsverklaring PDF; rq_079=done; seeded rq_080 Limburg/VBR; ticks=80
- FOI: none (official portal PDF public)
- Next: **rq_080** Limburg or Vlaams-Brabant (prio 3) or **rq_071** SWA recheck (prio 2)

### 2026-07-22T12:20:00Z â tick 81
- Unit: rq_080 (Provincie Limburg AMJP 2026 L1 + L5 sample)
- Found (strong, official AMJP 2026-2031 aanpassing juni 2026, PR dossier; initieel 18 Dec 2025): **Exploitatie-uitgaven EUR 247,304,270** / ontvangsten **EUR 258,189,615** (saldo **EUR 10,885,344**). **Investeringsuitgaven EUR 106,147,542** / ontvangsten **EUR 18,746,936**. Financiering aflossingen **EUR 6,829,363**; leningsontvangsten **EUR 78,713,724**. **Cash-out EUR 360,281,175**. **BBR EUR 42,156,256**; **AFM EUR 4,953,756**; **schuld EUR 127,017,316**. **Personeel EUR 173,828,351** (onderwijs andere overheden **EUR 99,304,235**). **Werkingssubsidies EUR 25,865,989** (andere **EUR 23,939,516**). **Opcentiemen EUR 90,933,687** (rate **214.52**). **Invest period sum 2026-31 EUR 272,275,476** (~270m press). Named: Bokrijk winterevenement **EUR 250,000**. Inwoners **904,919**.
- Wrote: 20 budgets; 3 commitments; 3 leaderboard; 2 sources; entity prov_limburg; raw AMJP PDF; rq_080=done; seeded rq_081 Vlaams-Brabant; ticks=81
- FOI: none (official smartcities dossier public)
- Next: **rq_081** Vlaams-Brabant (prio 3) or **rq_071** SWA recheck (prio 2)

### 2026-07-22T12:35:00Z â tick 82
- Unit: rq_081 (Provincie Vlaams-Brabant MJP 2026 L1 + L5 sample)
- Found (strong, official MJP 2026-2031 PR **14 Oct 2025** / pub 23 Oct): **Exploitatie-uitgaven EUR 150,983,589** / ontvangsten **EUR 175,453,134** (saldo **EUR 24,469,545**). **Invest EUR 43,388,068** / ontvangsten **EUR 13,092,337**. Financiering uitgaven **EUR 6,213,109**. **Cash-out EUR 200,584,766**. **BBR EUR 46,612,757**; **AFM EUR 22,650,349**; **schuld EUR 36,945,771**. **Personeel EUR 97,952,035**. **Werkingssubsidies EUR 19,382,399** (andere **EUR 15,654,473**). **Opcentiemen EUR 126,813,759** (rate **171.75**); **eigen belastingen afgeschaft 2026**. Named: **fiets period EUR 66,300,000** (2026 **EUR 11,550,000**); **waterrecreatie/openluchtzwembaden period EUR 37,464,204**. Invest period sum **EUR 255,080,070**. Inwoners **1,198,638**. **Completes 5/5 Flemish provinces** (ANT WVL OVL LIM VBR).
- Wrote: 20 budgets; 3 commitments; 3 leaderboard; 2 sources; entity prov_vlaams_brabant; raw MJP PDF; rq_081=done; seeded rq_082 VL compare; ticks=82
- FOI: none
- Next: **rq_082** Flemish 5-province compare (prio 3) or **rq_071** SWA recheck (prio 2)

### 2026-07-22T12:50:00Z â tick 83
- Unit: rq_082 (Flemish 5 provinces 2026 comparative snapshot)
- Found (strong synthesis; gaps flagged): 5-province map from ticks 78-82.

| Province | Exp 2026 | Cash-out | Inv 2026 | Opcentiemen | Debt |
|---|---:|---:|---:|---:|---:|
| Limburg | 247.3m | 360.3m | 106.1m | 90.9m | 127.0m |
| Antwerpen | 204.7m | 274.3m | 60.4m | 172.1m | 19.9m |
| Vlaams-Brabant | 151.0m | 200.6m | 43.4m | 126.8m | 36.9m |
| Oost-Vlaanderen | n/a | n/a | 62.6m | 110.5m | 17.4m |
| West-Vlaanderen | n/a | n/a | ~60m/yr class | n/a | 92.3m start |

- **Exp sum ANT+LIM+VBR EUR 602,988,534**; **cash-out sum EUR 835,202,216** (~EUR 0.84 bn); **opcent 4-prov EUR 500,421,882**; **inv 2026 4-prov EUR 272,595,891**; **inv period OVL+WVL+LIM+VBR EUR 1,290,558,167** (~EUR 1.29 bn). Debt 5-prov class **EUR 293,580,225**. Caveats: WVL/OVL full exp not extracted; OVL/LIM pers include onderwijs pass-through.
- Wrote: flemish_provinces_2026_snapshot.md; 6 budgets; 2 commitments; 2 leaderboard; 1 source; rq_082=done; ticks=83
- FOI: none (public gaps are extractability)
- Next: **rq_071** SWA recheck (prio 2) or fill WVL/OVL full exp from T2

### 2026-07-22T13:05:00Z â tick 84
- Unit: rq_071 (SWA multi-parliament final assent recheck Q3 late)
- Found (strong process; **still no final votes**): Reconfirmed OverlegcomitÃ© **27 Mar 2026** economic-governance SWA (replaces 2013). Public track still maxes at **government first readings**: **VL Regering 8 May 2026** principal OK voorontwerp instemmingsdecreet â SERV/RvS (portal unchanged); **SERV 1 Jun** advice; **Vlaams Parlement** still no plenary-adopted instemmingsdecreet found; **Federal MR 13 May** avant-projet de loi assentiment (news.belgium); **FWB 30 Apr** / **WAL 13 May** GW first readings (prior ticks). Kamer budget docs cite SWA content but **not** a adopted assent law. Searches Kamer / Vlaams Parlement / Wallonie / FWB / Brussels + BS class: **no final plenary assent law/decree and no Belgisch Staatsblad publication** for this SWA as of **2026-07-22**. Brussels public assent dossier still **not found**. Summer multi-parliament path remains **not evidenced**.
- Wrote: 3 sources; updated cmt_entity_mtfsp_split + lb_entity_split_opacity; rq_071=done; seeded **rq_083** WVL exp fill + **rq_084** SWA recheck; ticks=84
- FOI: none (parliamentary process tracking)
- Next: **rq_083** West-Vlaanderen full exp T2 (prio 3) or **rq_084** SWA recheck (prio 2)
### 2026-07-22T13:34:00Z â tick 85
- Unit: rq_083 (West-Vlaanderen full exploitatie 2026 from Schema M2)
- Found (strong, official Schema M2 p15 vision-read + press cross-check): **Exploitatie-uitgaven EUR 194,441,409** / ontvangsten **EUR 216,640,317** (saldo **EUR 22,198,908**). **Investeringsuitgaven EUR 70,132,288** / ontvangsten **EUR 15,237,921**. **Financieringsuitgaven EUR 19,371,814** / ontvangsten **EUR 81,390**. **Cash-out EUR 283,945,511**. BBR **EUR 15,204,117** and AFM **EUR 10,913,984** reconfirm prior chart reads. Path to 2031: exp uit **EUR 218,519,509** / ont **EUR 242,172,530**. Secondary press (Kelly De Tavernier / HLN) quotes 194.4mâ218.5m and 216.6mâ242.2m â aligns M2. Updated 4-province compare: exp sum **EUR 797,429,943**; cash-out sum **EUR 1,119,147,727**. Rank cash-out: LIM 360 > WVL 284 > ANT 274 > VBR 201. Werkingssubsidies name-level still medium ~55m class.
- Wrote: 12 budgets; updated cmt_wvl + cmt_vl_provinces; flemish snapshot; 2 press sources; entity note; rq_083=done; seeded rq_085 OVL exp; ticks=85
- FOI: none (public M2 extractable; residual is OVL T2 + WVL L5 subsidies)
- Next: **rq_085** Oost-Vlaanderen full exp T2 (prio 3) or **rq_084** SWA recheck (prio 2)


### 2026-07-22T13:49:00Z -- tick 86
- Unit: rq_085 (Oost-Vlaanderen full exploitatie 2026 from documentatie T2)
- Found (strong, official Documentatie PDF p37/p41/p44 Totalen budget 2026): **Exploitatie-uitgaven EUR 313,167,169** / ontvangsten **EUR 327,535,846** (saldo **EUR 14,368,677**). Breakdown uit: personeel **EUR 211,963,313**; goederen/diensten **EUR 63,828,447**; subsidies granted **EUR 30,667,884**; financiele **EUR 921,577**. Inv uit **EUR 62,639,681** / fin uit **EUR 4,048,851**. **Cash-out EUR 379,855,701**. Completes **5/5 Flemish provinces** full exp+cashout. Compare: exp sum **EUR 1,110,597,112**; cash-out sum **EUR 1,499,003,428**. Rank cash-out: OVL 380 > LIM 360 > WVL 284 > ANT 274 > VBR 201. VRT secondary ~330m/yr class near exp. OVL largest because onderwijs pass-through in personnel.
- Wrote: 10 budgets; cmt_ovl + cmt_vl_provinces; snapshot; 2 sources; entity; rq_085=done; seeded rq_086 WVL opcent; ticks=86
- FOI: none (documentatie public on beleidsportaal)
- Next: **rq_086** WVL opcentiemen (prio 2) or **rq_084** SWA recheck (prio 2)


### 2026-07-22T14:04:00Z -- tick 87
- Unit: rq_086 (West-Vlaanderen opcentiemen 2026 from Schema T2)
- Found (strong, official Schema T2 p30-31 vision-read): **Opcentiemen OV 2026 EUR 128,769,361** (aanslagvoet **186,22**; VLABEL 13/09/2025). Path to **EUR 150,110,481** in 2031. **Andere/eigen belastingen EUR 57,843,000**. Fiscal sum (opcent+eigen+boetes 100) **EUR 186,612,461**. Completes **5/5 Flemish opcentiemen**. Opcent sum 5-prov **EUR 629,191,243**. Rank opcent: ANT 172 > WVL 129 > VBR 127 > OVL 111 > LIM 91. Chart p118 aligns ~129m->150m class.
- Wrote: 5 budgets; cmt_wvl + cmt_vl; snapshot; sources; entity; rq_086=done; rq_087 snapshot refresh=done; ticks=87
- FOI: none
- Next: **rq_084** SWA recheck (prio 2) or seed new L5/continuous unit


### 2026-07-22T14:19:00Z -- tick 88
- Unit: rq_084 (SWA multi-parliament final assent recheck Q3)
- Found (strong process; **still no final votes**): Reconfirmed Overlegcomite **27 Mar 2026** SWA and VL Regering page **8 May 2026** still at **principiele goedkeuring** voorontwerp instemmingsdecreet -> SERV/RvS (page unchanged). SERV advice **1 Jun** / VL ingekomen **17 Jun** path unchanged. Federal MR draft **13 May** path unchanged. **New related signal:** Kamer dossier **56K1569** (Bertrand/Vander Elst, filed **22 May 2026**, inoverweging **4 Jun**) is a private-member **wetsvoorstel** for a statutory **terugvalregeling** interfederal budget coordination - **pending** Finance commission; **not** the SWA assent law and **not** adopted. Wallonie/FWB still max first-read class; Brussels assent dossier **not found**. **No** plenary-adopted assent law/decree and **no** Belgisch Staatsblad publication for the Mar 2026 SWA as of **2026-07-22**.
- Wrote: 3 sources; updated cmt_entity_mtfsp_split + lb_entity_split_opacity; rq_084=done; seeded **rq_088** WVL personeel T2 + **rq_089** SWA Q4 low-prio; ticks=88
- FOI: none
- Next: **rq_088** West-Vlaanderen bezoldigingen/personeel T2 (prio 3)


### 2026-07-22T14:34:00Z -- tick 89
- Unit: rq_088 (West-Vlaanderen bezoldigingen/personeel + exp rubrics T2 p30)
- Found (strong, official Schema T2 p30): **Bezoldigingen EUR 84,874,186** (politiek 1.20m; vast admin 31.63m; contract admin 41.79m; onderwijs andere overheden 10.61m; andere 2.37m; pensioenen net -2.68m). **Goederen en diensten EUR 51,954,729**. **Toegestane werkingssubsidies EUR 54,431,043** (upgrades prior ~55m medium) of which **APB EUR 11,631,181** + **andere begunstigden EUR 40,732,307**. Financiering rente **EUR 1,921,373**. WVL personnel much smaller than OVL 212m (OVL heavy onderwijs pass-through). Werkingssubsidies ~28pct of exp 194.4m.
- Wrote: 12 budgets; cmt_wvl + cmt_subs; leaderboard upgrade; snapshot; entity; sources; rq_088=done; seeded rq_090 L5 sample; ticks=89
- FOI: none (public T2)
- Next: **rq_090** named L5 werkingssubsidies sample (prio 3) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T14:49:00Z -- tick 90
- Unit: rq_090 (WVL/OVL named L5 werkingssubsidies sample)
- Found (strong, official WVL MJP p60 + OVL documentatie p4-14): **WVL agencies 2026 dotaties:** POM **EUR 11,653,824**; Westtoer **EUR 11,052,567**; Inagro **EUR 10,839,292**; TUA WEST **EUR 385,000**; **sum EUR 33,930,683** (upgrades prior ~35m class; ~63pct of 54.4m werkingssubsidies). WFIV base **EUR 400,000**. Named landschappen: Westhoek 1.35m; Houtland-Polders 1.18m; WV hart 0.72m. UNIE-K kapitaal **EUR 1,160,258**. **OVL sample:** PIMD **EUR 1,220,850**; Toerisme OVL **EUR 600,176**; Centrum Ronde van Vlaanderen **EUR 230,000**; Huysmanhoeve **EUR 789,225**; RATO **EUR 482,694**; OVL total werkingssubsidies **EUR 30,667,884** reconfirmed.
- Wrote: 16 budgets; 6 commitments; 3 leaderboard; sources; entities; rq_090=done; seeded rq_091; ticks=90
- FOI: none (public tables)
- Next: **rq_091** OVL L5 deepen (prio 2) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T15:04:00Z -- tick 91
- Unit: rq_091 (OVL top named werkingssubsidies deepen)
- Found (strong, official Documentatie p4-14): **POM Oost-Vlaanderen package 2026 EUR 2,004,589** (kennis 319k; logistiek 295k; bedrijvencentra 387k; terreinen 387k; verduurzaming 593k; Scheldemond 25k) + invest terreinen **EUR 200,000**. **Erov vzw EUR 1,446,227** (streekproducten 867k; voeding 375k; ambacht 204k). **Polders en Wateringen EUR 2,100,000** (largest single named line; statutory Art18). **Political parties EUR 532,093** (path to **0 in 2031**); fracties 59k. **Interreg cofin 2021-27 EUR 1,830,896**; PDPO Betaalorgaan **EUR 708,000**; noord-zuid 620k; AZORG AHRIA 350k one-off; Bosgroep werking 333k. Domain economie/landbouw/EU werkingssubsidies **EUR 20,423,228**; leefmilieu **EUR 4,858,494**. Total werkingssubsidies **EUR 30,667,884** reconfirmed.
- Wrote: 20 budgets; 5 commitments; 4 leaderboard; entity; sources; rq_091=done; seeded rq_092 ANT/LIM L5; ticks=91
- FOI: none (full named register public in documentatie)
- Next: **rq_092** Antwerpen or Limburg named L5 (prio 3) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T15:19:00Z -- tick 92
- Unit: rq_092 (Antwerpen/Limburg named L5 subsidies sample)
- Found (strong): **Limburg** AMJP verbonden entiteiten p122-124: **Bokrijk EUR 6,500,000** (path to 2.0m 2031); **Diepenbeek campus EUR 5,000,000** (peaks 8.0m 2027); **POM Limburg EUR 4,850,000** (flat); **Toerisme Limburg EUR 4,750,000** (flat); **pcFruit EUR 1,500,000**; 3 regionale landschappen sum **EUR 2,101,998**; Dommelhof 150k; Dubolimburg 185k; PIBO 230k; PVL 200k. Top4 sum **EUR 21.1m** of total werkingssubsidies 25.9m. **Antwerpen** T2: **APB package EUR 38,925,780** (13 named APBs without per-line EUR); andere begunstigden **EUR 22,907,585**; eredienst 743k; niet-conf 1.25m; AP vrijetijd verzelfstandigde entiteiten **EUR 16,642,250**. POM Antwerpen loan guarantee class ~20m outstanding (medium narrative).
- Wrote: 19 budgets; 6 commitments; 4 leaderboard; entities; source; rq_092=done; seeded rq_093 VBR L5; ticks=92
- FOI: none for LIM names; ANT per-APB split still not public in main MJP (optional later FOI)
- Next: **rq_093** Vlaams-Brabant named L5 (prio 2) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T15:34:00Z -- tick 93
- Unit: rq_093 (Vlaams-Brabant named L5 subsidies sample)
- Found (strong, official MJP nominatieve verbonden entiteiten p70-73): **Toerisme Vlaams-Brabant vzw EUR 1,990,204**; **Praktijkpunt Landbouw EUR 1,674,979**; **POM Vlaams-Brabant EUR 1,570,833**; **APB Vera EUR 1,190,000**; **IMD EUR 1,200,000**; De Rand **EUR 675,400**; Erfgoedstichting 320k; Vlabinvest 133k. **Regionaal Landschap Pajottenland/Zennevallei EUR 4,335,140** (2026 spike; 2027 falls to 396k). Other RL: Kouters 445k; Dijleland/Noord-Hageland 357k each; Zuid-Hageland 343k; **RL sum5 EUR 5,835,948**. Streekproducten 358k; Bosgroep 175k. T2: APB total **EUR 1,531,315**; andere **EUR 15,654,473**; total werkingssubsidies **EUR 19,382,399**. **Completes 5/5 Flemish provinces** with named L5 samples. POM ladder: WVL 11.7m > LIM 4.85m > OVL 2.0m > VBR 1.57m (ANT APB-heavy 38.9m).
- Wrote: 20 budgets; 6 commitments; 4 leaderboard; snapshot L5 table; entity; source; rq_093=done; seeded rq_094 synthesis; ticks=93
- FOI: none
- Next: **rq_094** VL provinces L5 POM/tourism compare (prio 2) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T15:49:00Z -- tick 94
- Unit: rq_094 (Flemish provinces L5 POM/tourism compare synthesis)
- Found (strong synthesis, no new primary PDF): From ticks 90-93 only. **POM named sum 4 provinces EUR 20,079,246** (WVL 11,653,824 > LIM 4,850,000 > OVL 2,004,589 > VBR 1,570,833). **Tourism agency sum 4 EUR 18,392,947** (Westtoer 11,052,567 > LIM 4,750,000 > VBR 1,990,204 > OVL 600,176). **Combined POM+tourism 4 EUR 38,472,193** (WVL alone 59%). **Werkingssubsidies sum 5 EUR 194,175,471** (ANT 63,828,156 largest). **Antwerp APB package EUR 38,925,780** is **not** POM-equivalent (13 companies; larger than POM4 alone). Perimeter caveats documented.
- Wrote: flemish_provinces_l5_agencies_2026.md; 5 budgets; 1 commitment; 2 leaderboard; snapshot update; source; rq_094=done; seeded rq_095 Walloon L5; ticks=94
- FOI: none (synthesis of public extracts)
- Next: **rq_095** Walloon province L5 sample (prio 3) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T16:04:00Z -- tick 95
- Unit: rq_095 (Walloon province L5 named subsidies â Hainaut CoA + Liege budget)
- Found (strong): **Hainaut** CoA 2026: **ASBL Voies d'eau du Hainaut EUR 2,300,000** (incl **+1.8m** severance after canal tourism stop); **ASBL Teralis cut to 0** (was 0.4m; French domains sold); transfers hors zones **EUR 15.5m**; **CathÃ©drale Tournai invest EUR 3,900,000** (3.7m external subsidy); **199 entities** with aids >=50k/yr (annex exists; **amounts not in CoA PDF**; CoA flags **no motivation** for extraprovincialisation); 53 management contracts 2024. **Liege** budget 2026 named: tourism sites paraprovinciaux **EUR 516,011**; MNEMA **EUR 150,000**; Service social agents **EUR 190,878**; GIG **EUR 110,000**; DG cooperation **EUR 871,000**; Opera **EUR 150,000**; OPL **EUR 70,000**; Theatre Liege **EUR 60,000**; BRF 90k; RTC sport 124k; Parc HFE 60k. **FTPL** (Federation Tourisme) line **EUR 1** obligatoire 2026 (was **1.2m** 2025 â major cut/restructure in table).
- Wrote: 18 budgets; 6 commitments; 4 leaderboard; entities; 2 sources; rq_095=done; seeded rq_096 Hainaut annex/FOI; ticks=95
- FOI: **not drafted this tick** â rq_096 opened for 199-entity EUR list if public annex missing
- Next: **rq_096** Hainaut named ASBL list (prio 3) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T16:19:00Z -- tick 96
- Unit: rq_096 (Hainaut full named ASBL EUR list â public search + FOI)
- Found (strong process; **public list still missing**): Re-checked CoA Hainaut budget 2026 PDF and web/portal search for a published annex of the **199 entities** with provincial aids >= EUR 50k/yr. **No machine-readable or PDF named EUR list** found on public portals this tick. CoA remains best primary evidence that the annex **exists** administratively and that **motivation for extraprovincialisation is missing**. Action: **FOI draft** `gap_hainaut_asbl_list_2026` (FR, publicite de l'administration) status **ready** â **human send only**.
- Wrote: foi draft + foi_queue ready; sources note; rq_096=blocked_foi; lb/cmt notes; seeded rq_097 Namur/BW L5; ticks=96
- FOI: **gap_hainaut_asbl_list_2026** ready (not sent)
- Next: **rq_097** Namur/Brabant wallon L5 (prio 2) or **rq_089** SWA Q4 (prio 1); human may send Hainaut FOI


### 2026-07-22T16:34:00Z -- tick 97
- Unit: rq_097 (Namur + Brabant wallon province L5 named/aggregate sample)
- Found (strong, CoA primary): **Brabant wallon:** consolidated ASBL/FUP list **31 entities** with aids >=50k totaling **EUR 10,000,000**; motivations **explicit** (better than Hainaut). **34** management contracts 2024. Named invest: storm basins **EUR 3,100,000**; Helecine brewery **EUR 1,300,000**; points-noeuds **EUR 1,200,000**; IPES Wavre **EUR 800,000**. Aviq overpayment provision **EUR 1,800,000**. Transfers **EUR 27.5m**. **Namur:** only **10 entities** ge50k (3 **without** motivation); **21** management contracts 2024; Chevetogne regie dotation **-0.2m** path; BEP **-0.4m**; police academy federal receipt **EUR 1,600,000**; **pension cotisations debudgeted EUR 10,000,000** to fund (Ethias reserve path toward exhaustion ~2031); GSM tax provision 1.5m. Compare: Hainaut 199 unmotivated > BW 31/10m motivated > Namur 10 partial.
- Wrote: 18 budgets; 5 commitments; 3 leaderboard; walloon snapshot ASBL table; entities; sources; rq_097=done; seeded rq_098 Lux; ticks=97
- FOI: none new (Hainaut FOI already ready)
- Next: **rq_098** Luxembourg ASBL deepen (prio 2) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T16:49:00Z -- tick 98
- Unit: rq_098 (Luxembourg province ASBL deepen + FOI)
- Found (strong CoA; **named EUR list still not public**): ASBL/FUP package **EUR 4,300,000** 2026 (**-EUR 0.9m / -17.8%** vs 2025). **25** management-contract evaluation reports 2024. CoA: annual financial/eval annex covers only entities **with** management contracts â others with aids not in that report. Named invest: watercourses **EUR 1,300,000**; Maison culture Arlon roof **EUR 2,800,000** (contingent on Ville Arlon 2.8m match; **no justificatory piece**); cancer screening vehicle AVIQ **EUR 500,000**; health centres **EUR 600,000**; palace annex **EUR 500,000**. Zones secours **EUR 18,000,000**. Pension cotisations shortfall **EUR 3,100,000** to Ethias fund. GSM tax **EUR 600,000** + matching provision. Public search for named list: **negative**. **FOI draft** `gap_lux_asbl_list_2026` **ready** (human send). Completes 5/5 Walloon provinces L5 map (FOI where names missing).
- Wrote: 12 budgets; 3 commitments; 2 leaderboard; FOI draft+queue; snapshot; entities; sources; rq_098=blocked_foi; seeded rq_099 synthesis; ticks=98
- FOI: **gap_lux_asbl_list_2026** ready (not sent); Hainaut FOI still ready
- Next: **rq_099** Walloon L5 ASBL compare synthesis (prio 2) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T17:04:00Z -- tick 99
- Unit: rq_099 (Walloon 5 provinces L5 ASBL compare synthesis)
- Found (strong synthesis, no new primary PDF): From ticks 95â98 only. **Known package EUR:** BW **â¬10,000,000** (31 entities, motivated) + Lux **â¬4,300,000** (â17.8% vs 2025) = **â¬14,300,000**. **Entity counts:** Hainaut **199** (unmotivated, FOI) + BW **31** + Namur **10** (3 unmotivated) = **240**. LiÃ¨ge: named sample (tourism 516k; culture 280k; FTPL cut to â¬1) not a CoA â¥50k package total. Opacity rank worstâbest total disclosure: **Hainaut > Lux names > Namur > LiÃ¨ge sample > BW**. FOI ready human-send: Hainaut + Lux.
- Wrote: `walloon_provinces_l5_asbl_2026.md`; snapshot ASBL section; cmt/lb/source refresh; rq_099=done; seeded rq_100 VL/WAL L5 cross-compare; ticks=99
- FOI: none new (stack unchanged: gap_hainaut_asbl_list_2026, gap_lux_asbl_list_2026 ready)
- Next: **rq_100** VL vs WAL province L5 opacity (prio 2) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T17:19:00Z -- tick 100
- Unit: rq_100 (VL vs WAL province L5 opacity cross-compare)
- Found (strong synthesis, **not additive**): Flanders **werkingssubsidies sum 5 = â¬194,175,471**; named POM+tourism 4 = **â¬38,472,193** (WVL 59%). Wallonia **known ASBL packages BW+Lux only = â¬14,300,000**; entity counts H+BW+N = **240**; Hainaut 199 FOI. L1 context: VL exp â¬1.11bn vs WAL ord â¬1.93bn (different systems). Mechanism: VL MJP/T2 named L5 stronger public; WAL CoA annex often body-missing amounts; dual accounting forbids âBelgian provincial subsidyâ headline. Invalid claim: WAL ASBL < VL werksubs as total comparison.
- Wrote: `provinces_vl_wal_l5_opacity_2026.md`; 4 budgets; 1 cmt; 1 lb; 1 source; rq_100=done; seeded rq_101 city L5 recheck; ticks=100
- FOI: none new (Hainaut + Lux ready, human send)
- Next: **rq_101** Gent/Antwerp city L5 recheck (prio 3) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T17:34:00Z -- tick 101
- Unit: rq_101 (Gent/Antwerp city L5 open-data recheck)
- Found (strong, Stad Gent open **subsidieregister** 8718 rows): **2024 charged total â¬331,933,746** (intern â¬268.3m incl Politiezone â¬110.6m / Ivago â¬62.7m / HVZ â¬42.3m; **extern â¬63.7m**; **extern+werking â¬47.5m**). **Cultuurdienst 2024 â¬11,559,533** (311 orgs). Named culture: **NTGent â¬2,985,451** (werking â¬2,725,451 + invest â¬260k); Opera Ballet VL â¬1,459,913; VIERNULVIER â¬965,374; Minard â¬550k. **2025 partial** â¬107.4m only. Antwerp city: **no parallel open named EUR register** found this tick.
- Wrote: `gent_city_l5_subsidies_2024.md`; raw top extract; 12 budgets; 2 cmt; 2 lb; 1 source; entity; gap_gent=answered; rq_101=done; seeded rq_102; ticks=101
- FOI: gap_gent_subsidies_top20 **answered** via open data; gap_antwerp_subsidies_top20 still ready (human send)
- Next: **rq_102** other city open register scan (prio 3) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T17:49:00Z -- tick 102
- Unit: rq_102 (Brugge/Namur/â¦ city open subsidy register scan)
- Found (strong Brugge OD): **subsidieregister** 5831 rows 2022â2026. **2024 total â¬99,253,042**; **2025 â¬97,980,016**; 2026 partial â¬31.2m. Named: **Brugge Plus â¬7,317,328 (2024)** / â¬7.03m (2025); **Concertgebouw â¬2,110,837 (2024)** / â¬1.26m (2025); **Entrepot â¬1,086,176 (2024)**. Core top: Politiezone â¬32.9m; Mintus â¬26.2m; HVZ â¬10.1m. **Namur OD** `subsides-attribues`: **stale 2019â2020 only** (156 rows); SONEFA 2020 â¬2.13m â BI2026 associatif still from DGF not OD. Charleroi/Mons named OD not found this tick.
- Wrote: `brugge_city_l5_subsidies_tick102.md`; Brugge+Namur top JSON; 15 budgets; 4 cmt; 3 lb; 2 sources; rq_102=done; seeded rq_103; ticks=102
- FOI: none new (Antwerp/Hainaut/Lux still ready human send; Namur OD lag noted not drafted)
- Next: **rq_103** Charleroi/Mons L5 PDF (prio 3) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T18:04:00Z -- tick 103
- Unit: rq_103 (Charleroi/Mons named L5 public PDF)
- Found (strong Mons ord 2025 PDF): recettes **â¬246,241,166** / dÃ©penses **â¬244,180,818**; rÃ©sultat prÃ©sumÃ© 01/01/2026 **â¬2,060,348**. Named: **RCA â¬1,156,471** + fonct â¬815k + piscine **â¬1,900,000**; **MARS package â¬674k** (fonct 400k + anim 150k + musical 124k); OT personnel â¬289k + fonct â¬274k; Fondation Mons â¬110k; charte activitÃ©s â¬100k / fonct â¬50k; film festival â¬45k; Basket UMH â¬220k. **BI2026 PDF still not on mons.be**. Charleroi: only 2026 call forms â **no named EUR list**.
- Wrote: `mons_city_l5_budget_2025.md`; extract JSON; budgets/cmt/lb/source; gap_mons notes updated; rq_103=done; seeded rq_104; ticks=103
- FOI: gap_mons still ready (2026); gap_charleroi still ready; no new drafts
- Next: **rq_104** city L5 transparency compare (prio 2) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T18:19:00Z -- tick 104
- Unit: rq_104 (City L5 transparency compare Gent/Brugge/Mons + FOI peers)
- Found (strong synthesis, **not additive**): Transparency ladder **Gent > Brugge > Mons PDF > Namur stale OD > Antwerp=Charleroi FOI**. Gent register 2024 **â¬331.9m** (extern+werking **â¬47.5m**; culture **â¬11.6m**; NTGent **â¬2.99m**). Brugge 2024 **â¬99.3m** (Brugge Plus **â¬7.32m**; Concertgebouw **â¬2.11m**). Mons ord 2025 dep **â¬244.2m** (MARS **â¬674k**; RCA package multi-m). Core police/zones dominate OD tops â not pure L5 waste pools. Invalid: sum cities or compare raw register totals without perimeter.
- Wrote: `cities_l5_transparency_compare_2026.md`; 3 budget xrefs; 1 cmt; 1 lb; 1 source; rq_104=done; seeded rq_105; ticks=104
- FOI: none new (stack: Antwerp, Charleroi, Mons2026, Hainaut, Lux â human send)
- Next: **rq_105** FPS TE / VLAIO recheck (prio 3) or **rq_089** SWA Q4 (prio 1)


### 2026-07-22T18:25:00Z -- pause (user)
- User requested pause. Set `loop_state.paused=yes`, mode=`paused`.
- Last completed unit: **rq_104** (ticks_completed=104).
- Scheduler task `019f7c315adb` cancelled so 15m fires stop; recreate on resume with 15m interval + same prompt.
- No research unit this entry; commit pause state only.


### 2026-07-26T12:00:00Z -- resume (user)
- User set `paused=no`. Mode=`continuous`.
- Recreated durable scheduler every **15 minutes**: **019fa06d7ee0** (replaces cancelled 019f7c315adb).
- Still at ticks_completed=104, last_unit=rq_104. Next queue head: **rq_105** or **rq_089**.


### 2026-07-27T04:50:00Z -- auto-pause (idle_waiting_foi)
- After ticks 117â120 idle (no public open work; FOI ready human-only), auto-pause to stop 15m idle fires.
- Set `paused=yes`, mode=`paused`. Cancel scheduler **019fa06d7ee0**.
- Resume: `paused=no` + recreate 15m DOGE scheduler; or seed research_queue / send FOIs.


### 2026-07-27T12:00:00Z -- resume + tick 122 (user hole-fill)
- User: restart loop; start with **Unia**; fill holes; only pause when every material euro is sourced **or** FOI-ready (no auto-idle pause).
- Recreated scheduler **15m** durable **019fa288382e**; mode=`continuous` / sprint=`hole_fill`; `LOOP.md` pause rule tightened.
- **Unit rq_117 Unia funding (strong primary RA 2024â2025):**
  - 2024 subsidies **â¬9,454,426** = federal **â¬8,170,698** + federated **â¬1,283,728** (WAL **â¬761,698**; FWB **â¬354,971**; BXL **â¬145,867**; DG **â¬21,192**; Flanders **â¬0**).
  - 2025 subsidies **â¬9,628,106** = federal **â¬8,304,698** + federated aggregate **â¬1,323,408**.
  - Personnel 2025 **â¬9,050,949**. Coalition **â25% federal** path (not yet full cash outturn).
  - Dual: **VMRI** Flanders budget class **~â¬5.279m (2025)** / request **~â¬5.598m (2026)** (medium VP).
- Wrote: `unia_funding_map.md`; entities Unia+VMRI; 16 budgets; 2 cmt; 2 lb; 4 sources; FOI `gap_unia_funding_detail` ready; seeded rq_118â121 (IEFH, FIRM, Myria, hole-fill); ticks=122.
- FOI: new Unia residual (BGD codes + 2025 federated split); prior stack still human-send.
- Next: **rq_118** IEFH or **rq_119** FIRM-IFDH (prio 6).


### 2026-07-27T17:20:00Z -- tick 132
- Unit: **rq_133** (FOREM full budget primary) â prio 7 / PES dual with VDAB
- Found (primary **FOREM RA 2023**; **no invent euros**):
  - **Budget global â¬3.091 bn**; federal-managed slice â¬0.300 bn; **internal exp â¬2.763 bn**.
  - **Aides emploi/formation â¬2.067 bn** (75%); **fonctionnement â¬0.514 bn** (19%); tiers â¬0.180 bn.
  - **Subvention RW â¬2.662 bn**; other receipts â¬71.6 m; staff **4,919 / 3,992 FTE**.
  - Dual PES honesty: FOREM mass includes APE/titres-services passthrough â **not apples-to-apples** with VDAB VL krediet ~â¬0.75 bn.
  - 2024â26 RA still missing â FOI residual.
- Wrote: sources +2; budgets +12; programmes +4; cmt; lb_forem; FOI update; raw RA PDF; rq_133=**done**; ticks=132
- FOI: gap_forem_budget ready (prio 5; 2023 filled)
- Next: **rq_137 parties** or regional L5 / taxex prio7


### 2026-07-27T17:00:00Z -- tick 131
- Unit: **rq_132** (VDAB full budget primary) â prio 7 / FOI-adjacent PES
- Found (primary **BBT BO2026 Werk** pfile 2250747; **no invent euros**):
  - **Strong:** VDAB VL kredieten BA2025 **VEK â¬765.690 m** / VAK â¬760.621 m â BO2026 **VEK â¬750.702 m** / VAK â¬750.604 m.
  - Split BO2026: activering **â¬561.009 m** VEK; competenties **â¬189.693 m** VEK.
  - **ââ¬20 m** werkings toelage cut; **+â¬3 m** index on competenties toelage.
  - **Medium:** PQ52 premise **â¬962 m** total 2024 of which **â¬783 m** VL dotatie (minister deferred to jaarrekening); conceptnota **â¬945 m** werkings 2025 (81.2% VL).
  - Residual: official jaarrekening institutional total (EU+own) + L5 splits â FOI.
- Wrote: sources +3; budgets +10; programmes +3; cmt; lb_vdab_toelage; FOI draft update; raw PDFs; rq_132=**done**; ticks=131
- FOI: gap_vdab_full_budget remains ready (prio 5; partial fill)
- Next: **rq_133 FOREM** (PES dual) or **rq_137 parties** or regional L5


### 2026-07-27T16:40:00Z -- tick 130
- Unit: **rq_124** (Federal BGD / toelagen top discretionary L5) â prio 8 last
- Found (primary **BOSA** register + dept/OISZ/AOI tables; **no invent euros**):
  - Register **â¬179.916 bn / 8,993 items (2025)**; path 162.4 â 171.6 â 179.9 bn 2023â25.
  - **By type 2025:** HH+ASBL **â¬141.915 bn**; regions **â¬19.443 bn**; firms **â¬4.777 bn**; local **â¬4.682 bn**; BV TE **â¬4.668 bn**; foreign **â¬2.592 bn**; Maribel **â¬0.894 bn**; SSC exempt **â¬0.943 bn**.
  - **Dept 2025:** SS **â¬27.687 bn**; regions **â¬17.730 bn**; autonomous **â¬5.470 bn**; HH/ASBL **â¬4.968 bn**; companies **â¬3.075 bn**.
  - **OISZ out â¬142.955 bn** (HH **â¬136.384 bn**); **AOI â¬0.774 bn**.
  - Assignment funds **â¬83.552 bn**; 2023 TE inventory **â¬39.401 bn** (VAT 16.2 largest).
  - Named L5 top-50: interactive only â FOI **gap_fed_register_l5_top50** ready.
- Wrote: sources +5; budgets +25; cmt; snapshot `fed_toelagen_register_2025.md`; FOI draft; rq_124=**done**; ticks=130
- FOI: new gap_fed_register_l5_top50 ready (human send)
- Next: **prio7** IEFH/FIRM, regional L5, VDAB/FOREM, parties, taxex remainder â **prio8 queue empty**


### 2026-07-27T16:20:00Z -- tick 129
- Unit: **rq_154** (Cheque economy official TE line primary) â prio 8 / FOI-adjacent
- Found (primary **Rekenhof advies** Kamer DOC 56 0785/004, 4 Mar 2026; **no invent euros**):
  - **(Para)fiscale uitgave maaltijdcheques privÃ© 2024: â¬1.07 bn** (SSC+PB net of VenB) â **strong CoA** from RSZ+VIA.
  - **VIA market:** face issued **â¬3.550 bn 2024** (3.344 bn 2023); **3.142 m** beneficiaries; avg face â¬7.23; 156.3 cheques/person.
  - **FPS inventaris fiscale uitgaven:** lists meal-voucher TE but **amount not estimated** (CoA explicit).
  - **AABEO** CIT-only gov reform impact: **â¬55.8 / 62.7 / 65.6 m** 2026â28.
  - Federal public direct cost class **â¬71.6 m**; **ecocheques aggregate still Unknown**.
  - Supersedes thesis ~1.4 bn as best official meal estimate (keep medium triangulation).
- Wrote: sources +2; taxex +budgets +cmt; lb_cheque_economy â 1.07bn strong; FOI residual eco+FPS euro; raw PDF; rq_154=**done**; ticks=129
- FOI: gap_cheque_te still **ready** (prio 7; meal partial)
- Next: last prio8 **rq_124** federal BGD top50; then prio7 equality/PES


### 2026-07-27T16:00:00Z -- tick 128
- Unit: **rq_125** (Flanders BO2026 top 30 named subsidies L5) â prio 8
- Found (primary Centenboekje BO2026 PDF; **no invent euros**):
  - Domain VEK already mapped; extracted **30+ named measure lines** (Jobbonus 228m, Oosterweel 889.9m, VV 436.4m, subsidy cut pkg 350m, uitstel 370m, hervorm 462.7m, werk 229.0m, dienstencheques effort 151.4m, Warm 98.5m, Welvarend 206.9m, Gemeentefonds +115.1m, rente +330.6m, VRT +49.3m, De Lijn VEK â61.3m, retro premies â189.9/â111.7m, index 718.9m, â¦).
  - Many rows are **deltas/effort packages**, not full L5 third-party registers.
  - Snapshot: `vl_bo2026_named_measures_top30.md`
- Wrote: sources +1; programmes +35; budgets +15; snapshot md; rq_125=**done**; ticks=128
- FOI: none new (centenboekje is L3âL4; L5 ASBL lists remain prior FOI stack)
- Next: prio8 **rq_124** federal BGD / **rq_154** cheques TE


### 2026-07-27T15:40:00Z -- tick 127
- Unit: **rq_130** (NMBS PSO cash-by-year primary) â prio 8 / FOI-adjacent
- Found (primary **Openbaredienstcontract NMBSâStaat 2023â2032** Art.115â116; **no invent euros**):
  - **Compensatie = invest + variable (57% ODV tickets) + specific + fixed exp**
  - **Betalingstraject courante mâ¬ (Art.116 table):**  
    2023 core3 **1 985.3** (663.5+490.3+831.5); 2024 **2 016.2**; 2025 **2 383.1**; 2026 **2 265.8**  
    (excl. specific comps + woon-werk Art.40; saldi/overdrachten excl.)
  - Deferred **â¬536.513 m/yr** non-indexed from last monthly advances (var+fixed).
  - Cross-check: NBB ESA D.31+D.92 **â¬1.957 bn 2024** â order of core3 2.016.
  - FPS/BOSA **budget article cash codes still unknown** â FOI residual.
- Wrote: sources +1; budgets ~21; cmt ODC path; lb upgraded; FOI draft residual; raw ODC PDF; rq_130=**done**; ticks=127
- FOI: gap_nmbs_annual_toelage remains **ready** (FPS codes + outturn)
- Next: prio8 **rq_124** BGD / **rq_125** VL subsidies / **rq_154** cheques


### 2026-07-27T15:20:00Z -- tick 126
- Unit: **rq_131** (De Lijn full dotatie series primary) â prio 8 / FOI-adjacent
- Found (primary SV 955 PeetersâDe Ridder 26 Feb 2026; **no invent euros**):
  - **Strong multi-year toelage** (Vervoersautoriteit via PQ): exp+inv **2019â2024** ends at **â¬1.497683 bn 2024** (exp **â¬1.228474 bn** + inv **â¬0.269209 bn**); 2023 exp **â¬1.164150 bn** (supersedes press ~1.14bn medium).
  - ODC **basistoelage base â¬938.7 m**; 2025 KN+AN+VoM **â¬955.331659 m â â¬919.831649 m** after savings target.
  - 2025 own revenues **â¬255.098 m**; GIP invest **â¬661.025 m** (vergroening â¬460.9 m); availability fees **â¬52.592 m** (2025) / **â¬54.760 m** BO2026.
  - Minister deferred full 2025â26 exp+inv total to BBT (Q1â2) â **FOI residual** for comparable 2025â26 row.
- Wrote: sources +1; budgets ~20 lines; cmt + lb upgraded strong; FOI draft residual; raw PDF; rq_131=**done**; ticks=126
- FOI: gap_de_lijn_dotatie still **ready** (priority 6; 2019â24 filled)
- Next: prio8 **rq_124** BGD / **rq_125** VL subsidies / **rq_130** NMBS / **rq_154** cheques


### 2026-07-27T15:00:00Z -- tick 125
- Unit: **rq_123** (VL gelijke kansen full programme L5 beyond Wassalon) â prio 8
- Found (primary; **no invent euros**):
  - **Strong (VP BBT Open Vld 7 Nov 2025, pfile 2247885):** Gelijke Kansen **werkingsbudget 2026 â¬15.162m** (ââ¬18k y/y order); **projectsubsidies â¬4.361m** reserved; **VEK +â¬1.888m** rebalance; staff **10.3 VTE / â¬1,000,767.29** budgetlast.
  - **Named research L5:** Rode vlaggen KH Vives **â¬119,018.50** incl BTW; non-binariteit UGent **â¬119,634**; expertendatabank eval **â¬45,000** (17,424+27,611 Ipsos).
  - **Campaign:** BBT confirms **â¬800,000** mensenrechtencampagne via **LDV United** raamcontract (upgrades Wassalon contractor from medium claim â **strong** parliament answer).
  - **Inter:** toelage **â¬1.333m 2025 / â¬1.354m 2026**; IedereenOveral top-up **â¬163k** (2024 budget, Jul24âDec25).
  - **Portal strong names / no EUR:** dozens of lopende projecten (Pride 6 orgs, Safe spaces, GAMS/Plan/Zij-Kant, Turboplan, etc.) â amounts still FOI.
- Wrote: sources +3; budgets +10; programmes +7; commitments +3; lb Wassalon LDV upgrade; FOI draft gap_vl_gelijke_kansen updated residual; raw PDF; rq_123=**done**; ticks=125
- FOI: gap_vl_gelijke_kansen remains **ready** (per-project EUR list); human send
- Next: prio8 **rq_124** BGD / **rq_125** VL subsidies / **rq_130â131** NMBS/De Lijn / **rq_154** cheques


### 2026-07-27T14:40:00Z -- tick 124
- Unit: **rq_152** (GG expenditure bridge % of ~â¬348bn tagged) â prio 9 open
- Found (synthesis from prior primary rows; **no invent euros**):
  - **L0:** S.13 TE 2025 **â¬347.956 bn** (54.2% GDP) + primary â¬333.675 bn + interest â¬14.282 bn â **100% tagged** (strong NBB/Eurostat).
  - **L1:** unconsol. S.1311 181.5 / S.1312 128.6 / S.1313 45.0 / S.1314 141.7 bn; sum â¬496.8 bn; transfer wedge **ââ¬148.9 bn** â **100% L1 map**.
  - **L2 partial:** FL BA2025 66.5 + WAL 22.0 + FWB ~15 + BRU 8 + DG 0.7 â **â¬112 bn** class vs S.1312 128.6 â **â¬15â20 bn residual** order in state layer (perimeter/year, not exact identity). RIZIV 45.2 bn â **32%** of S.1314. Federal/local L5 thin.
  - **L5 end-receivers:** samples only â **do not claim** near-complete naming of 348bn.
  - Inventory: budgets 786; cmt 228; lb 160; taxex 153; FOI ready **34**; rq open was 38.
- Wrote: `docs/doge/data/gg_expenditure_bridge_2025.md`; sources `src_doge_gg_bridge_2025`; rq_152=**done**; ticks=124
- FOI: none new (residual already in ready stack + open RQs)
- Next: **prio8** rq_123 gelijke kansen L5 / rq_124 BGD top50 / rq_125 VL subsidies / rq_130 NMBS / rq_131 De Lijn / rq_154 cheques TE


### 2026-07-27T14:25:00Z -- tick 123
- Unit: **rq_122** (VL Het Wassalon 800k deepen tender L5) â prio 9 open
- Found (primary / sourced; no invent euros):
  - **Strong (official):** ABB vlaanderen.be 17 Jun 2026 â campaign **3 years**, **2 seasons/year**; host Daphne Agten; themes LGBTQI+ / disability / gender; YT+Spotify+IG+FB; Mechelen launch.
  - **Mediumâstrong (minister via VRT):** Gennez commissie Welzijn â full package **â¬800,000 / 3y** (creatie+productie+marketing+middenveld); **raamcontract** prijsafspraken; **Sept 2026** evaluation.
  - **Medium (VRT press metrics):** YT top episode ~**2,300** views/month; IG ~**636** followers; IG clips often **10k+**; Spotify listens not public.
  - **Medium (secondary claims, not tender PDF):** LDV United via VL raam âstrategische en creatieve communicatiepartnersâ (Doorbraak quoting VB MP); **NoStrezz** portfolio self-claim âfully producedâ.
  - Cash-by-year and gunningsbedragen **still Unknown** â FOI residual.
- Wrote: sources +4; commitments cmt_vl_wassalon updated; leaderboard + budgets notes; FOI draft + gap row residual; rq_122=**done**; ticks=123
- FOI: gap_vl_wassalon_tender remains **ready** (human send); draft refined with named contractor claims to confirm/deny
- Next: **rq_152** GG bridge prio9; or rq_123/124/125/130/131 prio8; do not idle


### 2026-07-28T12:00:00Z -- progress dashboard (human request)
- Added living **`progress_every_10_ticks.md`** + **`doge_waste_top10_current.md`**; LOOP.md requires refresh every 10 ticks.
- **Tick 176 coverage (vs €347.956 bn TE 2025):** L0 **100%** · L1 **100%** · L2 entity totals **~60–65%** · L5 named end-receivers **~8–12%** · FOI ready **~55**.
- **Waste top 3:** cheque economy (8.83) · company cars FPB (8.50) · heating oil FFS (8.43). High-abs honourable: **Het Wassalon** (abs 9.5, prio 7.4).


### 2026-07-27T14:20:00Z -- cadence: 60s scheduler (user)
- User: drop timer; prefer chain-on-complete or 30s/1m.
- Platform: durable scheduler is **interval-only** (no native on-complete chain); **min interval 60s** (30s not available).
- Cancelled 15m task **019fa288382e**; created **60s** durable task (see scheduler list).
- Trade-off: ticks often run 2â15 min â possible **concurrent** fires; one unit per fire still; no force-push.
- Updated `LOOP.md` cadence section.


### 2026-07-27T14:05:00Z -- seed (user): Wassalon + mass L5 queue
- User: keep loop; **Het Wassalon** gelijke kansen **â¬800k / 3y** (news Jul 2026) not yet in dataset â add high absurdity; seed many RQs for end-receivers / every-cent map.
- **Found (not in prior ticks):** Minister Gennez (VP, Jul 2026) â campaign+vodcast **Het Wassalon** (ABB) **â¬800,000 over three years** (~â¬267k/yr illustrative). Press (HLN): early views **~661** class (medium secondary). High clown/absurdity candidate (**abs 9.5**, priority_index **~7.4**).
- Wrote: budgets + cmt + **lb_vl_wassalon_podcast**; FOI **gap_vl_wassalon_tender** ready; sources VRT+HLN.
- **Seeded open RQs rq_122ârq_155** (34 units): Wassalon deepen, gelijke kansen L5, federal BGD top50, VL/WAL/FWB/BRU L5, SS/NMBS/De Lijn/VDAB/FOREM, parties, unions, mutualities, hospitals, unis, intercommunales, cities, defence, energy, **rq_152 GG bridge % of ~â¬348bn tagged**, taxex remainder, cheques, company-cars split.
- Honesty: GG **â¬348bn** will **not** be fully named L5 soon â map is L0 totals + samples + FOI residual; rq_152 will measure coverage gap.
- Next loop picks **rq_122** (prio 9) or **rq_152** (prio 9).


### 2026-07-27T00:20:00Z â tick 105
- Unit: **rq_105** (Federal/Flanders L5 recheck â FPS TE + VLAIO)
- Found:
  - **FPS taxex inventory XLSX re-download**: size 123619 bytes; MD5 `cb04adbe94e0fd27e25a511c100878be` **identical** to tick4 copy â **no new year sheets**. Existing tax_expenditures top20 still valid.
  - **VLAIO.be** still Akamai-blocked for agents; used primary **Speurgids 2025** (Departement WEWIS, Mar 2026, BO2025 vastlegging) instead.
  - Speurgids Table 1 (strong): EWI broad **â¬5,289.65m**; economisch beleid **â¬619.32m** (via FIO/VLAIO); wetenschap+innovatie **â¬4,669.33m** of which FIO/VLAIO WIB **â¬437.03m**.
  - Table 36 FIO Innovatie: **bedrijfssteun O&O â¬210.90m**; clusters **â¬82.55m**; Moonshot **â¬20m**.
  - Table 11/13 L5 instruments: **Kmo-portefeuille 2024 outturn â¬42.716m** (province split); BO2025 **â¬40m**; Kmo-groei outturn **â¬11.869m**; STS 2024 **â¬12.216m** (line zeroed BO2025 â Transitie en Transformatie; STS cut ~â¬20m); **Carbon leakage CIE BO2025 â¬261.59m** (largest single econ instrument); imec **â¬155.4m** VIB **â¬87.97m** Flanders Make **â¬54.94m**.
- Wrote: sources (+2); programmes (+13 Speurgids lines); commitments (+6); tax_expenditures recheck row; leaderboard (+3 CIE/kmo/FIO-OO); raw speurgids2025_full.pdf + deel1_ch1.pdf; rq_105=done; ticks=105
- FOI opened: none new (gap_vl_efro_l5 still covers project L5 opacity; Speurgids fills envelope not full beneficiary cash)
- Next: **rq_089** SWA Q4 recheck (prio1) or spawn next public L5; human send ready FOI stack (Antwerp/Charleroi/Mons2026/Hainaut/Lux + federal)

### 2026-07-27T00:40:00Z â tick 106
- Unit: **rq_089** (SWA multi-parliament final assent recheck Q4)
- Found (strong process; negative on final votes):
  - **No final** Kamer/Senaat / Vlaams Parlement / Wallonie / FWB / Brussels plenaire assent law/decree and **no BS/Moniteur** publication found for the Mar 2026 multi-entity economic-governance SWA (fifth dedicated recheck; search as of 2026-07-27).
  - Process still maxes at: Overleg **27 Mar 2026** â VL gov **8 May** principal + SERV **1 Jun** filed â federal MR **13 May** avant-projet loi â WAL/FWB **1st reading** ODJs; **Brussels** still thin.
  - New primary **APR 2026** (BOSA, **30 Apr 2026**) ch.5: reform of 2013 interfederal budget SWA; after signature, SWA + assent acts â **Raad van State** advice **by summer**; then entity **parliaments by year-end**. Matches stalled public track mid/late July.
  - Kamer PDF 56K1569 blocked (WAF); not used as source this tick.
- Wrote: sources (+src_apr_2026_bosa, recheck note); commitments **cmt_swa_econ_governance_2026** (status pending_assent; â¬0 not a spend envelope); rq_089=done; spawned **rq_106** CIE L5 (prio4) + **rq_107** SWA year-end recheck (prio1); raw apr_2026_bosa.pdf; ticks=106
- FOI opened: none
- Next: **rq_106** carbon leakage CIE L5 beneficiaries (Speurgids â¬261.59m); human FOI stack unchanged

### 2026-07-27T01:00:00Z â tick 107
- Unit: **rq_106** (Carbon leakage CIE L5 beneficiaries / evaluation)
- Found (strong totals; L5 names still opaque):
  - **FIO VEK ICL** (BO2026 tech vragen, keuro): **2024 250.234m** / **2025 261.588m** / **2026 BO 216.609m** â matches Speurgids 261.59m for 2025.
  - **PQ 251** (Diependaele 20 Feb 2026): **â¬258m** toegekend in 2025 voor emissiejaar 2024; **+â¬40m** uitzonderingsmechanisme EY 2022â23; budget **â¬216m** 2026.
  - **PQ 28** (2 Oct 2025): CIE = **grootste VLAIO-bedrijfssubsidie**; cite **â¬229m in 2024**; investeringsplicht-controles nog niet gestart (tot 2028 voor EY2021); **14 bedrijven** missen product-elektriciteitsbenchmark (50% herinvestering); terugvorderingen **â¬19.898.396** (2020â24).
  - Tech vragen: raming **~40 bedrijven** 2026; 75% standaard; **geen publieke naam+EUR-lijst**.
  - Steelman: EU-toegelaten carbon-leakage correctie; opacity L5 is the DOGE issue.
- Wrote: sources +3; programmes CIE 2024â26; commitments cash path + exception cmt; leaderboard refresh; **FOI gap_vl_cie_l5_beneficiaries ready**; rq_106=blocked_foi; spawned **rq_108** FIO O&O L5; raw PQs + tech PDF; ticks=107
- FOI opened: **gap_vl_cie_l5_beneficiaries** â ready (human send only)
- Next: **rq_108** VLAIO FIO bedrijfssteun O&O L5 sample; human FOI stack includes CIE

### 2026-07-27T01:20:00Z â tick 108
- Unit: **rq_108** (VLAIO FIO bedrijfssteun O&O named L5 / open data)
- Found (strong aggregates + partial named L5; bulk list FOI):
  - **PQ177** innovatiesteun OND+ONTW+ICON decision-year: Flanders **2025 â¬196.90m** (388 firms / 390 projects); multi-year path 2020â25 public; full portfolio incl ISS/Schaalklaar/haalbaarheid **â¬214.15m** 2025.
  - **PQ209** ontwikkelingsprojecten only: **â¬443m** 2021â25 on **â¬1.275bn** project cost (~35% avg); 918/1093 approved 2023â25; province split ANT 110.9 / OV 132.5 / WVL 79.3 / VBR 70.3 / LIM 38.0 / other 12.0 mEUR. Individual project names **withheld for confidentiality** (Excel bijlage not in PDF).
  - **PQ351 named L5 Woosh**: KMOGS â¬50k; ONTW â¬158.3k + â¬376.0k; haalbaarheid â¬46.2k; Schaalklaar â¬350k (codes public).
  - **Speurgids 2025**: speerpuntcluster geoormerkt **â¬54.2m** / 38 projects 2024 (Catalisti 5.31 â¦ Intercluster 14.2); **Moonshot â¬24.54m** / 10 projects; Edtech Station **â¬1.8m**/3y.
  - VLAIO.be jaarverslag annex media/3057 still **403 blocked** for agent download.
- Wrote: sources +4; programmes +5; commitments +6 L5; leaderboard +3; **FOI gap_vl_fio_project_l5 ready**; rq_108=done; spawned rq_109; raw PQs; ticks=108
- FOI opened: **gap_vl_fio_project_l5** â ready (human send; complements gap_vl_cie_l5)
- Next: **rq_109** federal TE/FFS recheck or **rq_107** SWA year-end (low)

### 2026-07-27T01:40:00Z â tick 109
- Unit: **rq_109** (FPS FFS / taxex inventory micro-update)
- Found (strong primary Jul 2026 editions):
  - **FFS 5th inventory** (FPS Finance+Health, data cut 1 Jan 2026, pub Jul 2026): **direct fossil subsidies 2024 â¬10,781.9m** (1.7% GDP); path 12.09 / 13.45 / 11.66 / 10.78 bn 2021â24. Confirms prior EN summary: company cars EHS **â¬3,141.7m**; fuel cards **â¬661.6m**; pro diesel FFS **â¬831.2m**; aviation kerosene **â¬754.6m**; VAT reduced gas HH **â¬635.2m**; agriculture intermediate **â¬378.5m**. International air+sea **â¬1,006.5m**. Broad sum direct+intl+indirect+EHS â **â¬15.15bn** (press â15bnâ class).
  - **Inventory of Federal Tax Expenditures (2024)** PDF: quantified total **2023 â¬39,402.01m** (6.74% GDP); path 28.9â39.4 bn 2018â23 (+6.37%/yr avg). By tax 2023: VAT **16.20bn**; PIT federal **9.67bn**; EIWT **4.42bn**; CIT **3.81bn**; excise **2.44bn**. Social objective **42.4%** of quantified.
  - Taxex XLSX recheck already identical earlier; this PDF adds **official global aggregates** not fully seeded before.
  - Method note (strong): FFS â  cash budget gain if abolished; TE inventory â  ESA spending; do not double-count FFS into TE total.
- Wrote: sources +3; tax_expenditures +12; commitments +2; leaderboard +3 + refresh 3 fossil rows; budgets +2; rq_109=done; spawned **rq_110**; raw FFS full+summary + taxex PDF; ticks=109
- FOI opened: none (public inventories sufficient for this unit)
- Next: **rq_110** kerosene/VAT gas deepen or low **rq_107** SWA

### 2026-07-27T02:00:00Z â tick 110
- Unit: **rq_110** (Kerosene aviation + VAT gas HH multi-year / reform notes)
- Found (strong FFS 2026 primary):
  - **Aviation kerosene** (Table 20, ETD min â¬330/1000l): **2019â24 â¬677.0 / 471.8 / 594.2 / 687.7 / 689.5 / 754.6 m** â rising post-COVID; sum **â¬3.875bn**. FFS eval: unjustified economically and environmentally; unilateral national tax weak; EU ETD proposal higher rate after 10y transition still blocked; coalition 2025â29 cites Chicago Convention revision.
  - **VAT gas households 6%**: **2021â24 â¬0 / 610.1 / 694.3 / 635.2 m**; electricity HH fossil-share **0 / 277.1 / 285.6 / 226.9 m**. Crisis cut made permanent class.
  - **VAT air tickets** (indirect): **87.5 / 180.4 / 208.8 / 224.5 m** 2021â24; stacks on kerosene.
  - **Boarding tax** (separate instrument, not kerosene): budget/programme law path â¬5ââ¬10 from 2027 class; later press scaled to â¬7 â **medium secondary**, not FFS inventory.
- Wrote: sources +3; tax_expenditures multi-year series (kerosene 6y + VAT gas/elec/tickets); commitments +3; leaderboard refresh kerosene +2 seeds; rq_110=done; spawned **rq_111**; ticks=110
- FOI opened: none
- Next: **rq_111** stookolie/agriculture FFS or low **rq_107** SWA

### 2026-07-27T02:20:00Z â tick 111
- Unit: **rq_111** (Stookolie / agriculture intermediate FFS multi-year)
- Found (strong FFS 2026 Tables 16+19):
  - **Huisbrandolie total** (bench1): **2019â24 â¬2,129.8 / 2,263.3 / 2,096.5 / 1,856.8 / 1,798.2 / 1,836.4 m**. 2024 split low-S **â¬1,526.7m** + high-S **â¬309.7m**. Long-run volume â3.7%/yr. FFS eval: **not justified environmentally or socially** (heating oil users not concentrated in lowest income quartile; 87% homeowners in HBS).
  - Taxex inventory product-specific line (~**â¬1,333m** prior seed) remains separate method â FFS gasoline-TOE higher.
  - **Agriculture intermediate** total: **2020â24 â¬548.9 / 562.6 / 629.9 / 442.8 / 378.5 m** (mostly product rate diffs, not pure exemption).
  - **Sociaal Verwarmingsfonds** cash: **â¬12.6m** 2024 / **70,112** households â targeted contrast to â¬1.8bn untargeted excise preference.
  - Binnenvaart **â¬84.3m** / bagger **â¬24.7m** 2024 intermediate package.
- Wrote: sources +2; taxex multi-year stookolie+ag; commitments +3; leaderboard refresh heatoil + ag seed; rq_111=done; spawned **rq_112**; ticks=111
- FOI opened: none
- Next: **rq_112** industrial reduced gas rate (â¬903m) or low **rq_107** SWA

### 2026-07-27T02:40:00Z â tick 112
- Unit: **rq_112** (Industrial reduced gas rate + inland waterways FFS)
- Found (strong FFS 2026 Table16/19 + Â§4.3.3):
  - **Aardgas verlaagd tarief** (EBO/sector agreements, bench1): **2019â24 â¬1,091 / 1,031 / 1,191 / 1,295 / 1,052 / 903 m**. Peak energy-crisis 2022; declining 2023â24.
  - **2024**: **13.54 TWh** declared at reduced rate; **~352 firms** with permit (PQ 2019).
  - FFS eval: sector agreements give static efficiency; reduced rate weakens dynamic price signal; dual-use + CHP full exemptions stack on top. NEKP 2025 continues refined EBO support with FFS phase-out language.
  - **Binnenvaart** intermediate: **â¬84.3m** 2024 (path 84â91m).
  - Gasolie industrial/commercial: **â¬365.9m** 2024 (path ~366â416m).
- Wrote: sources +1; taxex multi-year gas reduced + gasolie + binnenvaart; commitments +2; leaderboard +2; **FOI gap_fed_gas_reduced_firms ready**; rq_112=done; spawned **rq_113**; ticks=112
- FOI opened: **gap_fed_gas_reduced_firms** â ready (human send)
- Next: **rq_113** aardgas product-diff â¬4.09bn or low **rq_107** SWA

### 2026-07-27T03:00:00Z â tick 113
- Unit: **rq_113** (Natural gas product rate-diff FFS + social tariff path)
- Found (strong FFS 2026 Tables 15+1):
  - **Aardgas product rate-diff** (bench1 vs gasoline TOE): **2019â24 â¬4,741.5 / 4,538.0 / 5,124.3 / 4,854.2 / 3,722.4 / 4,089.4 m**. Largest single product-diff line. End-use: industry **55.8%**, housing **25.2%**, commercial **12.8%**, agriculture **4.9%**, transport **1.4%**. Bench2 2024 split: business **â¬470.3m** + non-business **â¬1,353.3m**. Pre-2022 series exclude federal gas contribution (method break).
  - **Not double-count** with EBO reduced rate (â¬903m) or VAT 6% gas HH (â¬635m) â different instruments.
  - **Sociaal tarief gas** (permanent CREG cash): **89 / 79 / 95 / 428 / 268 / 96 m** 2019â24. **RVT extension** peak **â¬462.2m** 2023 then **â¬27.7m** 2024. Targeted contrast to untargeted â¬4.09bn product gap.
  - Diesel product residual after petrol equalisation: **â¬273.3m** 2024.
- Wrote: sources +2; taxex multi-year gas product-diff + social/RVT + diesel residual; commitments +2; leaderboard +2; budgets +1; rq_113=done; spawned **rq_114**; ticks=113
- FOI opened: none (aggregates fully public)
- Next: **rq_114** FFS synthesis/LPG or low **rq_107** SWA

### 2026-07-27T03:20:00Z â tick 114
- Unit: **rq_114** (FFS synthesis snapshot + LPG/coal residual lines)
- Found / wrote:
  - **Synthesis** `docs/doge/data/ffs_federal_top_lines_2024.md`: package totals (direct **â¬10.78bn**, broad ~**â¬15.2bn**) + mapped high-EUR lines already in CSVs â **no invented euros**, explicit non-additive warning.
  - **LPG heating** Table16 multi-year: **2019â24 â¬108.6 / 138.8 / 140.0 / 120.3 / 117.8 / 127.6 m**.
  - **Coal HH** exemption: **27.8 â 10.8 m** 2019â24 (declining); FFS notes reduced VAT solid fuels abolished Jul 2025.
- Wrote: sources +2; taxex LPG+coal series; commitments +2; leaderboard LPG seed; snapshot md; rq_114=done; spawned **rq_115**; ticks=114
- FOI opened: none
- Next: **rq_115** leaderboard recompute (prio2) or low **rq_107** SWA; FFS top-line map largely complete

### 2026-07-27T03:35:00Z â tick 115
- Unit: **rq_115** (Leaderboard priority_index recompute after FFS wave)
- Method: ran `raw/recompute_leaderboard.py` â cost_score from annual EUR bands; priority = 0.55*cost + 0.35*abs + 0.10*(10-diff); sorted 157 rows.
- Top 10 after recompute:
  1. cheque economy **8.68** Â· 2. heating oil FFS **8.43** Â· 3. company cars **8.22**
  4â5. EIWT package / night-shift cluster **8.08** Â· 6â8. wage block / FFS direct total / gas product-diff **7.98**
  9. VL non-Maastricht claims **7.83** (stock-as-annual field) Â· 10. VAT horeca **7.73**
- FFS wave impact: **lb_ffs_direct_total** + **lb_gas_product_diff** enter top 8; heatoil rises (cost_score 9â9.5 from â¬1.84bn); company cars stays #3.
- Wrote: leaderboard.csv sorted; leaderboard_top15.md; rq_115=done; ticks=115
- FOI opened: none
- Next: low **rq_107** SWA recheck or human FOI stack (many ready); public open queue thin

### 2026-07-27T03:50:00Z â tick 116
- Unit: **rq_107** (SWA multi-parliament final assent recheck â sixth)
- Found (strong process; **still no final votes** as of **2026-07-27**):
  - **Rekenhof Kamer 56K1469/002** (BA2026 comments): SWA Overleg **25/27 Mar 2026** improves entity-level net-primary paths + fallback; EC positive; **\"moet evenwel nog ter goedkeuring worden voorgelegd aan de diverse parlementen\"** â still not multi-parliament approved.
  - Public track maxes at: **VL** 8 May principal + **SERV 1 Jun** filed VP 17 Jun; **Fed MR 13 May** avant-projet; **FWB 30 Apr** / **WAL 13 May** first reads. **Brussels** public assent dossier still missing. **No BS publication** / no plenary-adopted instemmingswet or -decreet found.
  - APR2026 path: parliament assent by **year-end** â mid-year recheck correctly negative.
- Wrote: rq_107=done; spawned low **rq_116** (Q4 2026 recheck); **lb_entity_split_opacity** notes refreshed; **mode=idle_waiting_foi** (only deferred SWA open; FOI ready stack is human work).
- FOI opened: none
- Next: human send FOI stack; **rq_116** only after Oct 2026 unless news breaks

### 2026-07-27T04:05:00Z â tick 117
- Unit: **idle** (mode already idle_waiting_foi)
- Queues: no in_progress research; no FOI draft; only open research is **rq_116** (SWA Q4 2026 â skip mid-year per instructions). All material gaps are **FOI ready** awaiting human send.
- Wrote: loop_state last_tick only; no CSV research writes; no FOI send.
- Next: human FOI stack; resume public discovery on FOI answers or after Oct 2026 (**rq_116**); optional human can spawn new research_queue items.

### 2026-07-27T04:20:00Z â tick 118
- Unit: **idle** (idle_waiting_foi)
- No public open work: only **rq_116** (SWA Q4 mid-year skip). FOI all **ready** (human send). No drafts to finish.
- Wrote: loop_state tick cursor only.
- Next: human FOI; or spawn research; **rq_116** after Oct 2026.

### 2026-07-27T04:35:00Z â tick 119
- Unit: **idle** (idle_waiting_foi)
- No public open work (rq_116 mid-year skip). FOI ready human-only. No draft FOI.
- Wrote: loop_state cursor only.
- Next: human FOI or new research_queue; rq_116 after Oct 2026.

### 2026-07-27T04:50:00Z â tick 120
- Unit: **idle** (idle_waiting_foi)
- No public open work (rq_116 mid-year skip). FOI ready human-only.
- Wrote: loop_state cursor only.
- Next: human FOI or new research_queue; rq_116 after Oct 2026.

### 2026-07-27T05:05:00Z â tick 121
- Unit: **idle** (idle_waiting_foi)
- No public open work (rq_116 mid-year skip). FOI ready human-only.
- Wrote: loop_state cursor only.
- Next: human FOI or new research_queue; rq_116 after Oct 2026.

### 2026-07-27T17:40:00Z  tick 133
- Unit: **rq_137** (Political party federal+regional financing L5)
- Found (strong 2024; medium 2025):
  - **Direct public subsidies 2024: 83.7m** (77% of party income 108.7m)  Maddens/KU Leuven from Kamer DOC 56 0961 party accounts.
  - Split: **fed dotatie 36.7m** · **VL+WAL regional 16.1m** · **fractietoelagen 26.3m** · provincial **3.5m** · FR connected inst **1.2m**.
  - Mandataris contributions **11.1m** (indirect); private gifts only 1.0m (VB+PVDA).
  - Off-books: parliamentary group **staff ~104.6m** ? broad package **188.3m**; all assemblies opex **619m** of which ~29.7% to parties.
  - Senate boost post-2024 **10.6m** (28.9% of federal dot); abolish-without-rewrite party hit **25.4m**.
  - **2025 direct 86.5m** medium (press/Belga; vote-base rise offsets freeze narrative).
  - Kamer formula primary: fixed + /vote, public-sector index, -5.32% 2023-24 only (src_kamer_dotatie_method).
- Wrote: sources (4); budgets (12); cmt_party_public_financing_2024; lb_party_public_financing; rq_137=done.
- FOI opened: none (aggregates public; per-assembly cash codes residual low priority vs ready stack).
- Next: prio7 **rq_126 WAL L5** / **rq_127 FWB** / **rq_128 BRU** / **rq_153 taxex** / **rq_138 unions**; prio6 IEFH/FIRM.

### 2026-07-27T18:00:00Z  tick 134
- Unit: **rq_126** (Wallonie budget 2026 top named ASBL/dotations L5)
- Found (strong primary ExpGen + GW CP):
  - **FOREM prog 18.130 consolidated 2.8336bn** eng/liq 2026 (new single line).
  - **17.093 Santé/Familles/Handicap 7.027bn**; Action sociale 329.6m; Crèches 16.3m; Affaires int. 2.682bn.
  - Named: **IFAPME 88.3m** · **Parlement 76.3m** · **CWaPE 9.3m** · **Cabinets 28.0m** · **CESE 7.9m** · **Recherche 247.5m** · **Eco outils 132.5m** · **Eco sociale 30.5m**.
  - **WE**: credits **124?64m**; dividend **55?70m**. **SPW** plafond **736m**. Marshall communes **58m**; FERI GV **35m**.
  - Savings **270.4m** with official APE package **83.7m** line-split (communes 17.5; indus 15; formation 20; provinces suppress 7.3; etc.). AVIQ 5.6+28.3m. Facultatives -8m. Airports -7m.
  - Garanties 1er rang stock end-2024 **8.822bn** (SWCS/CRAC/FLFNW/SWL dominant).
- Wrote: sources 2; budgets 25; commitments 4; leaderboard 3; rq_126=done; gap_wal residual ASBL note.
- FOI: gap_wal_l5 remains **ready** for pure ASBL top-20 (UAP/programme filled).
- Next: prio7 **rq_127 FWB** / **rq_128 BRU** / **rq_153 taxex** / **rq_138 unions**.

### 2026-07-27T18:20:00Z  tick 135
- Unit: **rq_127** (FWB budget 2026 named culture education transfers L5)
- Found (strong ExpGen + GW CP; medium sector savings path):
  - Totals already mapped: dep ~15.4bn; edu ~10.9bn class; deficit **1.6bn** 2026 ? path **1.2bn** 2029; net structural ~**500m** to 2029.
  - Named: **debt cost 357m** · **DO45 Recherche 262.6m** (FNRS Loterie 7.1m; -1.5m index cut) · **WBI 42.9m** · **WBE 39.7m** · **presse quotidienne 12.9m** · **médias proximité 10m** · **sport CL 67.9m** · **FP traitements 437.6m**.
  - **ONE**: structural +**43m** (Cigogne/contrat) vs IT -3m + non-index actors **7.84m**; MILAC not implemented.
  - **Culture**: non-index **3.7m** + moratoria non-spend **10.2m**; Grignoux -200k of 409k; Point Culture phase-out path.
  - **Supérieur** savings package **14m** 2026 (minerval compensations 9m; CHU Liège capital stop 2.8m).
  - **RTBF**: no new cut 2026 (stabilised; -700k parastatal pool only); prior ordinary ~350.8m kept.
  - Party-linked OJ/EP/archives recognitions **end Dec 2026** (named institutes).
- Wrote: sources 3; budgets 21; commitments 3; leaderboard 3; rq_127=done.
- FOI: none new (culture pure ASBL top20 still thin but moratoria map + existing multi-entity FOI stack).
- Next: prio7 **rq_128 BRU** / **rq_153 taxex** / **rq_138 unions**.

### 2026-07-27T18:45:00Z  tick 136
- Unit: **rq_128** (Brussels SGRBC top named transfers STIB culture L5)
- Found (strong CoA 13 Mar 2026; Visit medium press):
  - SGRBC **eng 8.9bn / liq 8.0bn**; Table9 top programmes 71% of liq.
  - **STIB 1.1676bn** · **Actiris 648.1m** (-78.2m) · **titres-services 303.8m** · **SLRB eng 687m / liq 418m** · **Bruxelles-Propreté liq 411.1m** · **commissions 691.7m** · **dette liq 727.8m** · **pouvoirs locaux 757.6m** · **routes liq 263.9m**.
  - Culture flagship: **Kanal eng 86.7m** (+60m participation/credit); CoA flags OAA2 list omission.
  - Initiatives régionales **eng 330m / liq 130m** (Vivaqua+Confex); finops path SLRB 400 / Vivaqua 180 / Confex 150 / Kanal 60 within 1bn max.
  - Facultatives **-25m/yr** 2026-29; emploi BEE total **983.6m**; PPI STIB cut path **964.6m** 2026-29.
  - Visit.brussels cut **~5.7m** 2026 medium press only.
- Wrote: sources 2; budgets 18; commitments 4; leaderboard 3; rq_128=done.
- FOI: none new (pure ASBL culture residual thin; Visit official cash path optional deepen later).
- Next: prio7 **rq_153 taxex** / **rq_138 unions** / **rq_139 mutualities** / **rq_143 Antwerp**.

### 2026-07-27T19:10:00Z  tick 137
- Unit: **rq_153** (FPS taxex remaining top 20 not yet imported)
- Found (strong FPS inventory XLSX latest-year per sheet):
  - Imported **20** measures previously missing from tax_expenditures.csv (sum latest-year  **48.6bn**  not additive with prior top20; many structural design lines).
  - Largest **current** additions: **PIT tax-free basic 18.058bn** (2023) · **professional expenses salaries 9.842bn** · **family allowances exemption 2.900bn** · **dependent-children tax-free 2.694bn** · **distinct taxation rates 2.665bn** · foreign-income 100% 2.271bn.
  - Other: WT movable first-bracket 565m · marital quotient 545m · disability allow 420m · overtime credit 386m · unemployment TE 350m · flexi-jobs 314m · CIT intra-group 321m · R&D refundable credit 315m · industrial motor gas oil 313m.
  - Historical peaks included for inventory completeness: venture capital old system **5.375bn** (2011); owner-occupied housing 2008; imputed income 2013.
  - Leaderboard: structural tax-free basic (low absurdity) · professional expenses · family allow · distinct taxation (higher reform interest).
- Wrote: tax_expenditures +20; sources 1; cmt_fps_taxex_next20; lb 4; rq_153=done.
- FOI: none (inventory public; residual medium TE lines still parseable later).
- Next: prio7 **rq_138 unions** / **rq_139 mutualities** / **rq_143 Antwerp** / **rq_155 company cars**.

### 2026-07-27T19:30:00Z  tick 138
- Unit: **rq_138** (Trade union public grants SS/federal  unemployment payment organisms)
- Found (strong parliament; medium path):
  - Architecture strong: 3 private OP (ABVV/ACV/ACLVB-SYNOVA) + public **HVW/CAPAC**; private also charge membership; HVW free.
  - **Private OP admin from ONEM 2024: 169m** (Kamer DOC 56 1296 cites official).
  - **Total all OP incl HVW: ~219m** (same bill + QRVA 56 028 citing minister: 219m for 333k werklozen/SWT).
  - Implied HVW share ~50m vs site institutional budget **6.084m**  dual perimeter; keep both.
  - Path Clarinval: envelope **-20m 2026 / -27m 2027** vs 2025 (~16% cut) while full-unemp dossiers path **-~63%** by 2027 (184k lose benefit).
  - 2022 Dermagne formula change: **+7.6m** that year; **+13m** effect by 2025; softens cuts when unemployment falls.
  - Late/overdue dossiers **391,435** in 2024 (minister answer via PQ).
  - Legal: KB 16 Sep 1991; amended KB 15 May 2022 + KB 11 Oct 2023.
- Wrote: sources 4; budgets 8; cmt_unemp_pay_org_admin_2024; lb_union_pay_admin_169m; rq_138=done; FOI residual L5 split priority 8.
- FOI: gap_unemp_pay_unit_cost updated (aggregates filled; per-union unit cost still ready).
- Next: prio7 **rq_139 mutualities** / **rq_143 Antwerp** / **rq_155 company cars**.

### 2026-07-27T19:50:00Z  tick 139
- Unit: **rq_139** (Mutualities RIZIV public financing  admin package)
- Found (strong KB-cited; medium 2025):
  - **5 landsbonden admin envelope:** **1.195bn 2023** · **1.285bn 2024** (KB 9 Apr 2024 BS) · **1.375bn 2025** medium (+7% y/y; +15% in 2y).
  - **HR Rail Care:** **22.8m 2024** / 21.2m 2023.
  - Total 5+rail 2024  **1.308bn**.
  - Members end-2022 (proportional split base): CM 4.59m · Solidaris 3.28m · Helan 2.26m · Neutral 0.59m · Liberal 0.54m.
  - vs RIZIV care authorized **40.99bn 2026** ? admin class ~**3.4%** of care package.
  - Accountability reform path: **25m 2026 ? 100m 2029** (medium reform motives).
  - Architecture: multi-cashier VI parallel to unemployment union payment organisms; Rekenhof 2017 method audit.
- Wrote: sources 4; budgets 9; cmt_mutual_admin_package; lb_mutual_admin_1_3bn; FOI gap_mutual_admin_l5 **ready**; rq_139=done.
- FOI: L5 per-landsbond draft ready (human send).
- Next: prio7 **rq_143 Antwerp** / **rq_129 SS** / **rq_155 company cars**.

### 2026-07-27T20:10:00Z  tick 140
- Unit: **rq_143** (Antwerp city open data / ebesluit subsidy recheck)
- Found (strong ebesluit primary; no Gent-style full register):
  - **Toneelhuis 2025: 2.805m** (2.74m werking + 65k gebouwbeheerder)  college Dec 2024.
  - **Opera Ballet Vlaanderen 2025: 1.9m** werk + **0.508m** invest.
  - **deSingel 2024: 0.100m** (talent/Dear Antwerp).
  - **Zorgbedrijf 2024 package:** werk **33.63m** + responsabilisering **20.56m** + invest **11.97m**  **66.2m** (largest named city transfer); 2023 werk 36.3 + resp 15.8 + invest 14.5.
  - Open data portal/arcgis: no machine-readable full third-party subsidy register (unlike Gent/Brugge).
  - FOI gap_antwerp priority 6 residual for complete top20 bulk.
- Wrote: sources 5; budgets 10; commitments 3; leaderboard 2; rq_143=done; FOI note updated.
- FOI: residual ready (partial fill does not close full top20).
- Next: prio7 **rq_129 SS funds** / **rq_155 company cars** / prio6 IEFH.

### 2026-07-27T20:30:00Z  tick 141
- Unit: **rq_155** (Company cars TE component split primary)
- Found (strong FPB WP 202504 Jun 2025; FFS prior):
  - **FPB central TE: ~4.7bn (2025) ? ~5.2bn (2028)** if BIK taxed as wage (CASMO); sensitivity **36bn**.
  - **Components (direction):** private-use cluster (PIT + SSC on availability dominant)  **4.2bn** of 2025 gap; **non-recovered VAT ~0.6bn** (2028); **CIT offset -0.1bn**.
  - Named TE categories: SS contribution on availability · income tax on availability · VAT on energy · income tax+SS on fuel/electricity · disallowed expenses.
  - **FFS inventory 2024 3.142bn** remains narrower official inventory line; dual methods kept (not force-reconcile).
  - Exact FPS inventory cash-by-year PIT/VAT/SSC series still not public ? FOI residual priority 6.
- Wrote: sources 2; taxex 5; budgets 3; cmt_company_cars_te_fpb; lb_company_cars_fpb; rq_155=done; FOI note updated.
- FOI: gap_company_cars residual ready (FPS official split).
- Next: prio7 **rq_129 Maribel L5**; prio6 **IEFH/FIRM**.

### 2026-07-27T20:50:00Z  tick 142
- Unit: **rq_129** (SS Maribel named fund L5 sample beyond NBB totals)
- Found (strong fund jaarverslagen + FOD WASO):
  - **FSM 319.01 Flanders** (VSPF 2023): social **75.938m** + fiscal **14.788m** = **90.726m**; max 46.7k/VTE.
  - **FSM socioculture Flanders** (VSPF 2023): social **31.589m**; total social+fiscal **38.012m** (~833 VTE; ~600 orgs).
  - **FSM 319 bicommunal** (FeBi): social **5.108m 2023 / 5.801m 2024**; fiscal **0.941m / 1.037m**.
  - **Public sector fund:** annual fiscal-substitute compensation **38.72m** (FOD WASO).
  - Sample sum class **~174m**  **12%** of NBB SS Maribel **1.461bn 2024**  residual especially **PC 330 health** bulk still FOI.
- Wrote: sources 4; budgets 11; cmt_maribel_l5_sample; lb 2; rq_129=done; FOI residual note.
- FOI: gap_maribel priority 6 residual (health bulk).
- Next: prio6 **rq_118 IEFH** / **rq_119 FIRM** / RTBF/VRT.

### 2026-07-27T21:10:00Z  tick 143
- Unit: **rq_118** (IEFH/IGVM federal equality institute funding map)
- Found (strong IEFH Rapport annuel 2024 primary):
  - **Federal dotation 2024: 33.939m** (budget authority; may exceed cash).
  - **Total expenditure 2024: 24.793m**  personnel 6.908m (28%) · ops 2.562m · **subsidies to orgs 1.609m** · **CPVS 10.926m (44%)** · projects 2.735m · inv 0.053m.
  - Multi-year exp path (k): 2020 12830 ? 2021 9841 ? 2022 14650 ? 2023 22931 ? 2024 24793.
  - **Protocols 2024: 222.9k** (WAL 81.3 · FWB 33.5 · BXL 100.0 · DG 8.1 · **Flanders 0**).
  - Lottery 150k; own 76k; EU Gender&Work 1.014m; COCOF/Actiris renewals 47.8k/32.5k.
  - Staff end-2024: **77 persons / 75 FTE**.
  - EIGE secondary 21.6m/14.4m kept as secondary; primary RA preferred.
- Wrote: sources 2; budgets 21; cmt_iefh_funding_2024; lb 2; entity iefh; rq_118=done; FOI gap_iefh_funding_detail ready.
- FOI: residual 2025-26 + CPVS?INAMI + L5 structural names (human send).
- Next: prio6 **rq_119 FIRM** / **rq_120 Myria** / RTBF-VRT.

### 2026-07-27T21:30:00Z ? tick 144
- Unit: **rq_119** (FIRM-IFDH federal human rights institute funding)
- Found (strong FIRM annual reports 2024 EN + 2025 NL primary):
  - **Grant path:** 2023 **EUR 2.776m** -> 2024 **EUR 4.111m** -> 2025 **EUR 3.769m** -> 2026 **EUR 3.223m** (Kamer dotatie).
  - **Expenditure:** 2023 **EUR 1.653m** · 2024 **EUR 2.489m** · 2025 **EUR 3.516m**.
  - **Total budget 2025: EUR 4.984m** (grant + surplus **EUR 1.215m**); 2026 finance **EUR 5.083m** (grant 3.223 + surplus 1.860).
  - Large **surplus buffer** (balance end-2024 **EUR 1.860m** · end-2025 **EUR 1.468m**).
  - Staff end-2025: **26** (24 statutory + 2 temp); growth path 7->27 class.
  - Dual architecture note: residual federal NHRI alongside Unia / VMRI / IEFH.
- Wrote: sources 2; budgets 14; cmt_firm_dotation_path; lb_firm; entity firm_ifdh; rq_119=done; FOI residual ready.
- FOI: gap_firm_funding_detail (codes + L5 ops) human send only.
- Next: prio6 **rq_120 Myria** / **rq_135 RTBF** / **rq_136 VRT** / Actiris L5.

### 2026-07-27T21:50:00Z ? tick 145
- Unit: **rq_135** (RTBF multi-year full public financing primary)
- Found (strong CSA 2023 control + RTBF RA 2025 finances page):
  - **2025 public package: EUR 378.1m** = ordinary **350.8** + pension **13.7** + TV5 **9.5** + access **4.1**.
  - **Total recettes 2025: EUR 479.7m** (?0.8%); ads **61.4m** (?9%); other **29.3m** (cable 12.6).
  - **2023 total dots: EUR 366.9m** (ordinary **332.8m** + TV5 9.4 + pension 14.5 + SEC 10.2); ads 66.0; exp 464.4; net PSO cost 370.1.
  - Dots series 2017-23: 260.5 ? 366.9m; **foregone 2025 vs contract 15.9m** (no index/+2%).
  - Savings plan **EUR 132m 2025-28** (55.2m in 2028); cash **92.8m**; LT debt **46.7m**.
  - Dual PSB: VRT ordinary ~296.4 + RTBF package ~378 ? **~674m** class (updates prior 647m ordinary-only dual).
- Wrote: sources 3; budgets 27; cmt_rtbf_public_package; lb_rtbf; rq_135=done; FOI residual ready.
- FOI: gap_rtbf_complement_split (2024 split + codes + savings cash) human send.
- Next: prio6 **rq_136 VRT** / **rq_134 Actiris** / **rq_120 Myria**.

### 2026-07-27T22:10:00Z ? tick 146
- Unit: **rq_136** (VRT BHO full public financing + side envelopes)
- Found (strong JV2023 + JV2024 + JV2025 web + PQ130):
  - **Overheidsfinanciering:** 2022 **EUR 290.6m** · 2023 **297.9m** · 2024 **304.4m** · 2025 **306m**.
  - **2023 L5 split:** basisdot **287.2** + inflatie **7.1** + transform **1.1** + overige **2.5**.
  - **Basistoelage path:** 2025 **258.393m** ? 2026 **296.400m** (wage index +36.34; partial ops +1.49; MAX +0.10; energy ?0.28; digital +0.20; NL coop +0.15).
  - **Eigen inkomsten:** 2023 **199.7** · 2024 **203.7** · 2025 **222.3**; total rev 2025 **528.4m**.
  - **BAN+comm 2025: EUR 83m** (plafond 90.8); external production invest **122.3m**.
  - Dual PSB 2025 class: VRT gov **306** + RTBF package **378** ? **~684m**.
- Wrote: sources 5; budgets 27; cmt_vrt_public_package; lb_vrt; rq_136=done; FOI residual ready.
- FOI: gap_vrt_side_envelopes (2024-26 L5 matrix + BBT codes) human send.
- Next: prio6 **rq_134 Actiris** / **rq_140 hospitals** / **rq_120 Myria**.

### 2026-07-27T22:30:00Z ? tick 147
- Unit: **rq_134** (Actiris L5 named programmes beyond total)
- Found (strong Actiris Rapport annuel 2024 Budget table):
  - **Budget final 2024: EUR 767.506m** · **exp realized EUR 729.736m** (95.1%) · recettes **753.574m**.
  - **Top L5 realized:** 6e reforme **EUR 225.0m** (30.8%) · **ACS jobs EUR 200.9m** (27.5%) · functioning **EUR 167.9m** (23.0%) · partnerships **EUR 57.7m** · economie sociale **EUR 34.5m**.
  - Other named: jeunes 8.8 · contrats insertion 7.3 · Garantie Jeunes 7.1 · cheques 6.8 · reforme aide 4.7 · secteurs ref 4.9.
  - Staff end-2024: **1,518 persons / 1,291 ETP**; DEI avg **91,628**.
  - Perimeter note: institutional ~730m vs BCR SGRBC programme line **648.1m 2026** (CoA) ? not same scope.
- Wrote: source 1; budgets 20; cmt_actiris_l5_2024; lb ACS + 6th reform; rq_134=done; FOI residual ready.
- FOI: gap_actiris_2025_26_l5 human send.
- Next: prio6 **rq_140 hospitals** / **rq_141 universities** / **rq_120 Myria**.

### 2026-07-27T22:50:00Z ? tick 148
- Unit: **rq_140** (Hospital federal/regional investment subsidies L5 sample)
- Found (strong NBB + BFM + named Jessa):
  - **Flanders VIPA hospitals D.92:** public **EUR 72m 2023** + non-public **208m 2023 / 192m 2024** (total class **~280m 2023**).
  - **Named L5:** **Jessa Hasselt VIPA ~EUR 500m over 40 years** (approved May 2026; project ~1bn; cash after opening ~2036).
  - **Federal BFM ops:** general hospitals **EUR 9.62bn** Jan 2025; all hospitals **EUR 11.778bn 2025** (operating ? not investment).
  - **FWB current:** CHU Liege **EUR 9m** + other UZ **EUR 7m** 2023 (NBB D.31).
  - Strategic forfaits cash 2024 only **EUR 4.48m** medium (commitments multi-year larger).
  - Prior stock: Flanders non-Maastricht hospital infra claim **EUR 2.184bn**.
- Wrote: sources 6; budgets 12; cmt 3; lb 3; entities vipa+fod_volksgezondheid; rq_140=done; FOI residual ready.
- FOI: gap_vipa_named_l5 (top named list + cash calendar) human send.
- Next: prio6 **rq_141 universities** / **rq_142 intercommunales** / **rq_120 Myria**.

### 2026-07-27T23:15:00Z ? tick 149
- Unit: **rq_141** (Universities public operating grants by institution)
- Found (strong CRC HO 2024 + KU Leuven JV 2025):
  - **VL universities 1st stream 2024: EUR 1.441bn** (werking **1.355bn** · invest **45.6m** · STUVO **30.4m**); path 1.167?1.441bn 2020-24.
  - **AHOVOKS effectieve werkingsmiddelen 2024: EUR 1.224bn**; **EUR 8,286/student**; 149,848 students.
  - **2nd/3rd/4th streams 2024:** 460m · 712m · 378m (research).
  - **Named L5 KU Leuven:** 1st stream **EUR 546.5m 2024 / 567.9m 2025**; werking **515.1 / 536.1m** (~38% of VL 1st).
  - **FWB:** education class **EUR 10.93bn 2026** (not uni-only); superieur savings **14m** ? per-uni FOI.
- Wrote: sources 3; budgets 20; cmt 2; lb 2; entity ku_leuven; rq_141=done; FOI residual ready.
- FOI: gap_univ_per_institution (4 remaining VL unis + FWB) human send.
- Next: prio6 **rq_142 intercommunales** / **rq_148 climate** / **rq_120 Myria**.

### 2026-07-27T23:35:00Z ? tick 150
- Unit: **rq_142** (Intercommunales top public transfers sample)
- Found (strong Fluvius investor + SPGE + Aquafin + BCR path):
  - **Fluvius EG:** ops rev **EUR 3.80bn 2024 / 4.60bn 2025**; CAPEX **1.56 / 1.78bn**; EBITDA **1.11bn**; result **182m**; debt **10.4bn**; equity strengthen path **up to 1.56bn** VL/PMV; 10y invest plan **~11bn**.
  - **SPGE (WAL water):** CA **EUR 418m 2024**; invest **>200m**; cum invest **5.22bn**; debt **1.58bn**.
  - **Aquafin (VL water):** project delivery **174m 2024 / target 180m 2025**; asset mgmt **54.3m**; **Lokaal Pact 500m 2026-30**.
  - **Vivaqua (BRU):** capital path **EUR 180m** (finops + 49pct stake claim medium).
  - NBB FL wastewater D.92 **82m 2024**.
- Wrote: sources 5; budgets 19; cmt 4; lb 2; entities 4; rq_142=done; FOI residual ready.
- FOI: gap_interco_dividends_l5 (municipal dividends + equity cash) human send.
- Next: prio6 **rq_148 climate** / **rq_144 Charleroi** / **rq_120 Myria**.

### 2026-07-27T23:55:00Z ? tick 151
- Unit: **rq_148** (Climate/energy named subsidies beyond offshore)
- Found (strong Rekenhof 2025 + VNR + Fluvius + NBB):
  - **Flanders RES support 2014-23: EUR 12.97bn** (~1.8bn on budget; rest on electricity bill).
  - **GSC:** 2023 **EUR 822m** · cum **10.51bn**; NBB broader green cert **956/858m 2023-24**.
  - **WKC CHP:** 2023 **EUR 174m** · cum **1.79bn**; Fluvius cert inventory **EUR 602m** EOY2025 (CHP 521m).
  - **Heat premiums (warmtepomp etc):** 2023 **EUR 22m** · cum **112m** 2014-23 (netbeheerder).
  - **Calls/ad hoc:** groene warmte **109m** · PV premie **158m** · retro **159m** · warmtenet **53.5m** · call stroom **37m**.
  - **VL DSO vergoedingen:** GSC 91.5?148?148?**67m** 2021-24; WKC **25m 2024 / 60m 2025**.
  - WAL green cert already mapped **323/288m**; offshore already mapped separately.
- Wrote: sources 3; budgets 26; cmt 2; lb 3; rq_148=done; FOI residual ready.
- FOI: gap_vl_odv_mvp_cash (REG digit series + MVP total) human send.
- Next: prio6 **rq_144 Charleroi** / **rq_120 Myria** / **rq_149 housing**.

### 2026-07-28T00:15:00Z ? tick 152
- Unit: **rq_144** (Charleroi BI2026 PDF named ASBL)
- Found (strong official PDFs charleroi.be):
  - **Synthese BI2026:** ord propre **EUR 577.89m** / gen **582.52m** (press ~567m superseded); personnel **189.70m**; fct **48.22m**; transferts **240.30m**; dette **99.15m**.
  - **Oxygene** last tranche class **~48.6m** (?22.8m vs 2025); invest borrow cap **20m**; extra invest propre **15.46m**.
  - **Cahier ordinaire (271p):** named L5 ? **ZPL 82.89m**; **CPAS ~93.18m**; **ZOHE 8.11m**; **RCA 3.86m**; **Tibi class ~33.60m**; **PBA ASBL 1.34m**; **CCR 0.86m**; **Parc des Sports 0.55m**; sport promo pool **0.52m**; Bois du Cazier **0.14m**; QUAI 10 **62k**; etc.
- Wrote: sources 3; budgets ~40 (replace press totals + L5); cmt 2; lb 4 new + 2 update; rq_144=done; FOI residual still ready (ranked top20 CSV).
- FOI: gap_charleroi_subsidies_top20 ready residual ? **human send only**.
- Next: prio6/5 **rq_120 Myria** / **rq_149 housing** / **rq_145 Brussels communes**.

### 2026-07-28T00:30:00Z — tick 153
- Unit: **rq_120** (Myria federal migration centre funding)
- Found (strong primary Kamer Doc 56 1281/004 sectie 07):
  - **AB 41.10.414003** Myria federal dotation (engagement = liquidation, kEUR):
    | Year | EUR |
    |------|-----|
    | 2024 | **1.579m** |
    | 2025 | **1.614m** |
    | 2026 | **1.600m** |
    | 2027-29 path | 1.572 / 1.543 / **1.516m** |
  - Organic AR 29 Jun 2014 art.15: base **1.5m** indexed health index from 2014-01-01.
  - Same table context: Unia federal AB **4.034m 2026**; IEFH **31.101m 2026** (stack).
  - Secondary social-media claim **EUR 2.213m** does **not** match Kamer AB (~1.6m) — **do not use** as official.
- Wrote: sources 2; entity myria; budgets 6; cmt 1; lb 1; overhead stack note; rq_120=done; FOI residual ready.
- FOI: gap_myria_other_income (outturn + lottery/other + FTE) human send only.
- Next: prio5 **rq_149 housing** / **rq_145 Brussels communes** / **rq_146 DGD** / **rq_121 hole-fill**.

### 2026-07-28T00:50:00Z — tick 154
- Unit: **rq_149** (Housing regional subsidies — VL social housing + WAL SWL)
- Found (strong primary BBT Wonen BO2026 + WAL DO16):
  - **VL programme QD WONEN BO2026:** VAK **EUR 3.291bn** · VEK **EUR 348.0m** (BA2025 VEK 377.8m).
  - **Huurtoelage joint** (huursubsidie+huurpremie): **EUR 141.0m**; full QDB2PA **152.1m** (incl VGW **8.36m**).
  - **VWF loan auth:** **EUR 1.72bn** (1.7bn Woonlening + 20m HWL); werkings **41.8m**.
  - **VMSW:** loan auth **EUR 1.229bn** (FS3 max **1.0bn** + market 220m + student 100m class); IS VEK **71.8m**; GSC **13.5m**; budgethuren cap **12.8m**.
  - **MVP cut:** **-EUR 70.5m** new credits from 2026.
  - **Social stock 31/12/2024:** **177.461** units; BSO path 45k+ voluntary to max **56k**.
  - **EIB facility:** **EUR 1.7bn** (first tranche **700m**) preferential loans — not pure grant.
  - **WAL SWL named liq sum ~EUR 118.0m:** PEI **55.3** · PRW liq **25.5** · PIVERT **22.4** · Ancrage **9.8** · Impulsion **5.0**.
  - **WAL Renopack primes EUR 88.6m** + ops **11.7m**; SWCS social loans **23.3m**.
- Wrote: sources 3; entities 4; budgets ~35; cmt 4; lb 4; rq_149=done; FOI residual ready.
- FOI: gap_housing_l5_slsp_wm (per-WM / per-SLSP L5 + interest-subsidy cash) human send only.
- Next: prio5 **rq_145 Brussels communes** / **rq_146 DGD** / **rq_147 defence** / **rq_121 hole-fill**.

### 2026-07-28T01:15:00Z — tick 155
- Unit: **rq_145** (Brussels communes Ixelles / Schaerbeek / Anderlecht L5 sample)
- Found:
  - **Ixelles (medium — DH quotes echevine Gilson):** ord rec **~EUR 253m** · ord dep **~EUR 258m+** · provisions **>5.5m** · invest **46.2m** (emprunt **26.9m**) · transfers **+9.4m** (CPAS **+6.07m** · Iris catch-up **4.75m** · police **+0.3m**) · debt path **119→210m** · participatif **0.17m strong**.
  - **Schaerbeek (strong note + medium RTBF total):** invest **EUR 60m** · Brichaut creche **6.5m** (commune **1.3m**) · Hoogvorst **~6m** (commune **2m**) · RenovaS Dupont **5m** · Plantes **3m** · sport **>2m** · trottoirs **1.5m** · Terdelt **1.2m** · CPAS federal class **~17m** · AS hire **0.95m**.
  - **Anderlecht (strong CP):** equilibrium claimed · asphalt **1.2m** · sidewalks **0.85m** · associative/sport maintained without EUR totals.
- Wrote: sources 5; entities 3; budgets ~27; cmt 3; lb 4; rq_145=done; FOI residual ready.
- FOI: gap_bru_communes_subsidies_top20 (full BI PDFs + ASBL top20 ×3) human send only.
- Next: prio5 **rq_146 DGD** / **rq_147 defence** / **rq_150 justice** / **rq_121 hole-fill**.

### 2026-07-28T01:40:00Z — tick 156
- Unit: **rq_146** (Federal development cooperation DGD / Enabel L5 envelopes)
- Found (strong primary DGD AR 2025 + Enabel RA 2025-26):
  - **DGD total:** **EUR 1,117.97m 2025** (1,440.92m 2024; 1,285.90m 2023); cut **−106m** year1 of **−25% by 2027**.
  - **Channels:** Enabel line **212.02m** · gov subtotal **250.35m** · humanitarian **170m** (protected).
  - **Themes:** climate **365.3m** · stability **301.8m** · humanitarian theme **181.5m** · other **175.0m** · health **98.8m**.
  - **Top recipients:** DRC **104.49m** · Burkina **28.0** · Uganda **27.8** · Burundi **27.2** · Niger **26.3** · Palestine **24.7** · Senegal **20.1** · Ukraine **18.2** · Benin **17.8** · Mali **14.6**.
  - **Named samples:** LDCF **18.5m** · Sahel package **50m** · SOFF +**8.3m**.
  - **Enabel:** turnover **407.1m** (was 329.2m) · charges **438.1m** · personnel **91.0m** · EU contracts **152m** · intl finance **182m** · assets **217.4m**.
- Wrote: sources 4; entities 3; budgets ~35; cmt 3; lb 4; rq_146=done; FOI residual ready.
- FOI: gap_dgd_l5_projects (top50 projects + Enabel reconcile) human send only.
- Next: prio5 **rq_147 defence** / **rq_150 justice** / **rq_151 police** / **rq_121 hole-fill**.

### 2026-07-28T02:05:00Z — tick 157
- Unit: **rq_147** (Defence major contracts L5 named)
- Found (strong primary SV2025 + Rekenhof 2025_16):
  - **Portfolio 2026-34 (Cst26):** commit **EUR 33.784bn** · pay **24.661bn** (Land 13.9 · Air 10.3 · Maritime 3.4 · ICI 3.5 · Comdo 2.7).
  - **Named L5 (SV):** F-35 **+11** **1.672bn** (+ support **445m**) · 3rd **ASWF** **1.270bn** · **NASAMS** 10 FU **2.032bn** · SBAMD long 3 FU **1.982bn** · MCM toolboxes **657m** · SAR heli 4 **193m**.
  - **Camo (CoA):** 382 Griffon + 60 Jaguar **1.575bn** invest · lifecycle TCO **≥14.7bn**/25y · STAR motorized extra **4.78bn** · STAR law **+11.176bn** 2023-30.
  - **Budget 2025 draft (CoA):** commit **12.9bn** / pay **10.5bn**; 2% GDP path from 2025.
- Wrote: sources 2; budgets ~25; cmt 4; lb 5; rq_147=done; FOI residual ready.
- FOI: gap_defence_contract_cash (signed cash-by-year major contracts) human send only.
- Next: prio5 **rq_150 justice** / **rq_151 police** / **rq_121 hole-fill**.

### 2026-07-28T02:30:00Z — tick 158
- Unit: **rq_150** (Justice prisons courts dual NL/FR overhead sample)
- Found (strong primary FOD PSP + Rekenhof DBFM 2023):
  - **Justitie ~EUR 2.7bn/yr:** courts **1.431bn** · prisons **799m** · cults **136.2m** · central **184.1m** · grants **303m** · ops **496.7m** · invest **74.7m** · personnel **67%**.
  - **Detention:** unit cost **EUR 55,624** (2022) · pop **13,483** / capacity **11,098** (121.5% Nov 2025).
  - **DBFM prisons (CoA):** 9 sites **3,874** places · annual fees **≥153.1m** full · **25y EUR 3.828bn** · Haren **48.4m/yr** (1,190 places) · MP1 **53.0m/yr** · off-balance **2.6bn** eoy2022.
  - Dual NL/FR: constitutional; euro L5 (tolk/vertaling) **not** published → FOI.
- Wrote: sources 4; entities 2; budgets ~23; cmt 3; lb 4; rq_150=done; FOI residual ready.
- FOI: gap_justice_dual_lang_tolk (interpreter/dual-lang cash) human send only.
- Next: prio4 **rq_151 police zones** / prio5 **rq_121 hole-fill** / deferred **rq_116 SWA**.

### 2026-07-28T02:55:00Z — tick 159
- Unit: **rq_151** (Local police zones financing consolidate Gent/Brugge + multi-city)
- Found (strong city sources + BeSafe mechanism):
  - **Mechanism:** municipal **~64%** / federal **~36%** of local police financing (BeSafe).
  - **City-side sample (ranked):** Gent **EUR 110.6m** (2024 register) · Charleroi ZPL **82.9m** (BI2026) · Brugge **33.75m** (MJP 2026; 32.9m register 2024) · Namur **27.6m** (2026).
  - **Sample sum (mixed years):** **EUR 254.8m** (4 cities, city-side only).
  - **Gent MJP path (medium press):** **~746m / 6y** (~120–130m/yr class).
  - Fire HVZ not mixed into police ranks (Gent HVZ 42.3m; Brugge HVZ 10.1m).
- Wrote: snapshot md; sources 3; budgets 5; cmt 1; lb 3; rq_151=done; FOI residual ready.
- FOI: gap_police_zones_fed_top50 (federal+municipal matrix all zones) human send only.
- Next: prio5 **rq_121** FOI-adjacent public hole-fill; **rq_116** SWA deferred (Oct–Dec).

### 2026-07-28T03:20:00Z — tick 160
- Unit: **rq_121** (FOI-adjacent hole-fill batch — NMBS 2025 + VDAB 2024)
- Found:
  - **NMBS 2025 (strong official):** EBITDA **EUR 54.2m** (was 131.6m) · economic debt **1.532bn** (was 2.146bn) · invest **>820m** (rolling **350** · stations **213** · digital **152** · workshops **89**) · ODC path hyp **−100m** vs 2025 contractual assumptions · rail sector savings demand **675m 2025-29** · staff **16,976** · passengers **207.8m** · punctuality **91.7%**.
  - **VDAB 2024:** staff **4,761** (−230) strong JV · institutional total **962m** / VL dots **783m** medium (VP PQ premise; minister → jaarrekening) · PMO ~**160m** project means since 2019.
  - FOREM 2024-26 RA and De Lijn full 2025-26 perimeter still not newly filled this tick.
- Wrote: sources 3; budgets ~18; cmt 2; lb 3; FOI gaps nmbs/vdab notes partial; rq_121=done; seeded **rq_152**.
- FOI: gap_nmbs / gap_vdab still **ready** residual human send; FOREM/De Lijn ready.
- Next: prio5 **rq_152** · deferred **rq_116** SWA.

### 2026-07-28T03:45:00Z — tick 161
- Unit: **rq_156** (FOI-adjacent hole-fill — **Infrabel geconsolideerd JV 2024** rail dual NMBS)
- Found (strong primary PDF 4.4 MB, 53 pp):
  - **Omzet** EUR **843.2m** 2024 (875.2m 2023).
  - **Exploitatiesubsidies** **560.9m** (583.9m) — −23.0m y/y.
  - **Kapitaalsubsidies** P&L recognition **794.9m** (774.7m); **stock** LT+ST **18.589bn**.
  - Bedrijfsopbrengsten vóór kap. **1.967bn**; EBITDA-like **114.4m**; bedrijfsresultaat **82.0m**; **resultaat 33.6m**.
  - Balanstotaal **25.231bn**; materiële VA **20.323bn** (+452.7m invest effect); fin. debt **~3.24bn**; cash **625m**.
  - **Liefkenshoek PPS:** annual specific State subsidy **50.61m (2008 €)** through 2032; LT receivable restatement **416.6m**.
  - Credit line up to **1bn** invest 2025-29; Alstom switches **~80m**; Thales cyber **20m/5y** (editorial medium).
  - Note: P&L personnel only **75.7m** — bulk staff via **HR Rail** inside **diensten 1.508bn**.
- De Lijn 2025 JV PDF still **403** on ctfassets; press metrics already in DB (surplus 20k; pax 372.9m; −27.5m dotatie).
- Wrote: sources 2; budgets ~22; cmt 2; lb 3; FOI **gap_infrabel_dotatie_cash** ready; rq_156=done; seeded **rq_157**.
- FOI: gap_infrabel (FPS cash codes + invest L5 + Liefkenshoek series) human send only; gap_de_lijn residual note.
- Next: prio5 **rq_157** FOREM/De Lijn perimeter/Antwerp/univ; deferred **rq_116** SWA.

### 2026-07-28T04:05:00Z — tick 162
- Unit: **rq_157** (FOI-adjacent hole-fill — **FOREM Wallonie budget 2026 programme 130 L5**)
- Found (strong primary EP Jeholet DO18, kEUR table eng=liq):
  - **Total prog 130: EUR 2.833619bn** (sum of 20 AB lines; matches ExpGen 18.130).
  - **APE 1.279bn** (45%) · **titres-services 568.4m** · **fonctionnement FOREM 419.7m** · SESAM **106.9m** · ONSS draw **136.8m** · CISP **104.3m** · activation **76.2m**.
  - 2025 legacy: prog12 **370.1m** · titres **567.6m** · formation prog22 **344.6m** (folded into 130 in 2026).
  - Dual PES: pure ops ~420m vs VDAB VL krediet ~0.75bn; total 2.83bn is aids-heavy (not apples-to-apples).
  - FOREM RA 2024-25 still not public this tick.
- Wrote: sources 1; budgets ~18; cmt 1; lb 4; programmes 4; gap_forem notes partial; rq_157=done; seeded **rq_158**.
- FOI: gap_forem residual RA2024-25 + APE beneficiary L5 still **ready** human send.
- Next: prio5 **rq_158**; deferred **rq_116** SWA.

### 2026-07-28T04:25:00Z — tick 163
- Unit: **rq_158** (FOI-adjacent hole-fill — **VL universities per-institution CRC HO 2024**)
- Found (strong primary CRC PDF; 1st-stream reverse-engineered medium):
  - Sector: bedrijfsopbr **3.504bn** · kosten **3.467bn** · bedrijfsresult **37.0m** (was 131m) · resultaat **159.6m** · personnel **2.198bn** · invest **260.2m** · VTE **30 419**.
  - **Results 2024:** KUL **+180.2m** · UGent **−32.3m** · UA **+2.4m** · UHasselt **+9.5m** · VUB **−0.2m**.
  - **Invest:** KUL **108.1m** · UGent **57.6m** · VUB **54.6m** · UA **24.7m** · UHasselt **15.2m**.
  - **Students:** KUL 56 114 · UGent 46 128 · UA 20 414 · VUB 19 889 · UHasselt 7 303 (sum 149 848).
  - **VTE:** KUL 12 350 · UGent 8 938 · UA 4 019 · VUB 3 618 · UHasselt 1 494.
  - **1st stream implied (medium):** UGent **~428m** · UA **~207m** · VUB **~166m** · UHasselt **~94m** (+ KUL **546.5m strong JV**); sum ≈ sector **1.441bn**.
  - Method: CRC official bedrijfsresult / basisfinanciering ratios (T48); not AHOVOKS cash lines.
- Wrote: entities 4; sources 1; budgets ~31; cmt 5; lb 5; gap_univ notes partial; rq_158=done; seeded **rq_159**.
- FOI: gap_univ residual AHOVOKS exact matrix + FWB institutional still **ready** human send (prio 6).
- Next: prio5 **rq_159**; deferred **rq_116** SWA.

### 2026-07-28T04:45:00Z — tick 164
- Unit: **rq_159** (FOI-adjacent hole-fill — **bpost Consolidated AR 2024 SGEI package**)
- Found (strong primary consol AR PDF, note 6.7 + related-party):
  - **SGEI remuneration:** **EUR 227.8m 2024** / **311.9m 2023** (−84.1m y/y).
  - Method: net avoided cost (NAC); 7th management contract SGEIs (retail network ≥1300 points, cash-at-counter, pensions, ad-hoc) + press newspapers/periodicals **until 2024-06-30**.
  - **USO:** dedicated management contract signed **2023-11-09**, USO provider to **2028-12-31** (tariff/regulatory; not equal to SGEI cash line).
  - Op. income **4.341bn**; rev ex-SGEI **4.101bn** / 3.946bn; State share **9.5%** of op. income incl SGEI.
  - Overcompensation provision **75.0m** (prior years, 3 services); SGEI receivable **74.6m** eoy2023 → **0** eoy2024.
  - Dual series: NBB ESA D.31 **329m** 2024 vs SGEI **227.8m** → residual **~101m** medium perimeter gap (2023 gap only ~12m).
- Wrote: sources 1; budgets 11; cmt 1; lb 2; gap_bpost notes partial prio7; rq_159=done; seeded **rq_160**.
- FOI: gap_bpost residual L5 SGEI components + ESA residual still **ready** human send.
- Next: prio5 **rq_160**; deferred **rq_116** SWA.

### 2026-07-28T05:05:00Z — tick 165
- Unit: **rq_160** (FOI-adjacent hole-fill — **FWB universities DO54 BI2026 per-institution L5**)
- Found (strong primary Budget des dépenses 2026, *en milliers d'euros*, eng=liq):
  - **Alloc fonctionnement 2026:** UCLouvain **330.911m** · ULB **275.862m** · ULiège **249.252m** · UMons **89.797m** · UNamur **72.197m** · **sum 1.018bn** (2025 sum **978.8m**).
  - **DO54 CELL total 1.153bn** 2026 (prog1 Communauté **361.0m** · prog2 libres **718.8m** · prog4 **69.8m**).
  - Social unis: Comm **12.2m** · libres **28.3m** · minerval compensations **52.4m** (was 56.5m) · aides réussite **14.9m** · art.34 **11.4m**.
  - CHU Liège capital line **2.785m → 0** 2026 (matches ExpGen savings note).
  - Hautes Écoles CF allocations globales **122.5m** + social HE **41.3m** (DO55 sample).
  - Dual HE: FWB ~1.02bn pure alloc vs VL 1st stream **1.44bn** (different perimeter/students).
- Wrote: sources 1; entities 5; budgets 25; cmt 1; lb 4; gap_univ FWB filled residual VL AHOVOKS; rq_160=done; seeded **rq_161**.
- FOI: gap_univ still **ready** for VL AHOVOKS exact only (prio 5).
- Next: prio5 **rq_161**; deferred **rq_116** SWA.

### 2026-07-28T05:25:00Z — tick 166
- Unit: **rq_161** (FOI-adjacent hole-fill — **HR Rail NV PR institutional omzet/FTE**)
- Found (medium: Companyweb citing **NBB CBSO** jaarrekening BE0541.691.352; filing class 2026-06-10):
  - **Omzet:** **EUR 2.368bn 2025** (+2.75%) · **2.305bn 2024** · **2.206bn 2023** · **2.078bn 2022**.
  - **FTE:** **27 811 (2025)** · 27 568.5 (2024) · 27 524.5 (2023) · 27 435 (2022).
  - **Resultaat:** ~**1.57m 2025** (pass-through; not a profit centre) · equity **28.3m**.
  - **Brutomarge** ≈ omzet (payroll re-invoice to NMBS+Infrabel under KB 11 Dec 2013).
  - Dual rail stack: NMBS staff count 16 976 (2025 results) ⊂ HR Rail 27.8k (rest mostly Infrabel).
  - Implied ~**85k EUR** omzet/FTE 2025.
- De Lijn full 2025-26 JV / Mons BI2026 / Antwerp register still not newly filled this tick.
- Wrote: sources 1; entity 1; budgets 21; cmt 1; lb 2; FOI **gap_hr_rail_charge_matrix** ready; gap_infrabel note; rq_161=done; seeded **rq_162**.
- FOI: human send gap_hr_rail (NBB PDF + charge L5) + residual De Lijn/Infrabel/NMBS.
- Next: prio5 **rq_162**; deferred **rq_116** SWA.

### 2026-07-28T05:45:00Z — tick 167
- Unit: **rq_162** (FOI-adjacent hole-fill — **VIPA 2026 envelope + De Lijn MJR path**)
- Found (strong primary: MJR 2025-30 + VP commissie Gennez + begroting tables):
  - **VIPA total:** **EUR 180m 2026** (no +20m expansion) · path **295m 2029**.
  - **Hospital forfait:** **77.3m 2025 → 89.6m 2026** (+14.5m room new awards).
  - Ouderen forfait **~35→40m** · handicap auth **16.8m** · instandhouding **+27.2m** (table 27.692m).
  - Expansion cut **−20m** · classic VEK budgeted **33m** vs need claim 68m · kinderopvang shift **60m**.
  - **De Lijn ESR-ontvangsten (own, not toelage):** BA2025 **264.3m** · BO2026 **313.8m** · const **263.8m** · 2030 **250.9m**.
  - E-bus VAK extra **+400m** path · OV savings **−50m 2026** → **−125m 2029** · MOW punctual **30m/yr** · VEK peaks **+145m 2027** / **+59m 2028** · VEK actualisatie **−61.3m**.
- Antwerp register / Mons BI2026 still not newly filled.
- Wrote: sources 3; budgets 26; cmt 2; lb 3; FOI gaps vipa+de_lijn notes; rq_162=done; seeded **rq_163**.
- FOI: named VIPA L5 + full De Lijn toelage still **ready** human send.
- Next: prio5 **rq_163**; deferred **rq_116** SWA.

### 2026-07-28T06:05:00Z — tick 168
- Unit: **rq_163** (FOI-adjacent hole-fill — **CREG AR2025 offshore support + nuclear repartition**)
- Found (strong primary CREG Rapport annuel 2025 FR, 92 pp):
  - **Offshore total support 2025: EUR 538.5m** = GC purchase **456.24m** + advances **82.26m**.
  - Production: inject **6 780 GWh** (vs 7 054 in 2024); net certified **6 912 GWh**.
  - Parks GC: C-Power Belwind Northwind Nobelwind Norther Rentel Northwester2; advances: Northwester2 Mermaid Seastar (**regime ended 2025**).
  - Dual series residual: prior CREG 179.4m 2023 different perimeter; NBB ESA **592m 2024**.
  - Bonus L5: nuclear contribution de répartition **Electrabel 152.5m + Luminus 8.8m = 161.3m 2025**.
- Mons BI2026 still not online (only 2025 ord/extra PDFs); Antwerp full register still FOI.
- Wrote: sources 1; budgets 10; cmt 2; lb 2; gap_offshore notes partial; rq_163=done; seeded **rq_164**.
- FOI: gap_offshore residual multi-year same-method + NBB reconcile still **ready** human send.
- Next: prio5 **rq_164**; deferred **rq_116** SWA.

### 2026-07-28T06:25:00Z — tick 169
- Unit: **rq_164** (FOI-adjacent hole-fill — **CREG federal GC OSP + CRM costs**)
- Found (strong CREG AR2025 §3.1.3.5; medium Elia auction press):
  - **Federal GC OSP financing (Elia):** est **EUR 675.707m 2025** → **551.352m 2026** (−125.4m; higher power ref price 87.56 vs 58.02 €/MWh).
  - Settlements: State→Elia **39.5m** H2-2024; Elia→State **110.4m** H1-2025.
  - Dual with offshore support **538.5m 2025** (tick168): same family, different metric.
  - **CRM OSP est:** **169.917m** (B2893; 2025 year per footnote).
  - CRM 2024 surplus **2.991m** repaid to State; strategic reserve residual tiny.
  - **Elia Oct 2025 auctions** (Y-1/Y-2/Y-4): package cost **125.4m** (was **182.9m**); **4 556 MW** (171 new); WAP **14.1k €/MW/y**.
- Mons BI2026 / Antwerp full register still not newly filled.
- Wrote: sources 2; entity 1; budgets 12; cmt 2; lb 2; FOI **gap_crm_osp_series** ready; gap_offshore note; rq_164=done; seeded **rq_165**.
- FOI: CRM multi-year + residual Mons/Antwerp human send.
- Next: prio5 **rq_165**; deferred **rq_116** SWA.

### 2026-07-28T06:45:00Z — tick 170
- Unit: **rq_165** (FOI-adjacent hole-fill — **Elia Transmission Belgium IAR 2025**)
- Found (strong primary integrated annual report, consol FS €m):
  - **Revenue 1.667bn 2025** (1.258bn 2024) · **profit 300.7m** (245.0m) · **EBIT 448.7m**.
  - Settlement mechanism **−160.9m** 2025 (was **+247.8m** 2024) — OSP/GC volatility link.
  - Personnel **264.0m** · services **646.0m** · D&A **266.9m**.
  - **CAPEX ~1.47bn** · **RAB 7.8bn** · PPE **7.14bn** · assets **11.68bn** · equity **4.43bn** (inject **+1.057bn**).
  - Loans LT **4.86bn** + ST **0.63bn** · cash **1.50bn** · dividends **99.7m**.
  - CAPEX plan **7.5bn 2025–28** · 2026 invest plan **1.7bn** · Baekeland **~400m** · Green Bond **500m**.
  - Grid **8 851 km** · reliability **99.99%** · dual with Fluvius DSO + CRM host.
- Mons BI2026 / Antwerp full register still not newly filled.
- Wrote: sources 1; budgets 28; cmt 1; lb 2; entity note; rq_165=done; seeded **rq_166**.
- FOI: no new gap (regulated monopoly well disclosed); residual local FOIs human send.
- Next: prio5 **rq_166**; deferred **rq_116** SWA.

### 2026-07-28T07:05:00Z — tick 171
- Unit: **rq_166** (FOI-adjacent hole-fill — **Sibelga BCR DSO 2024 + Fluvius EG deepen**)
- Found (strong primary Sibelga accounts + Fluvius investor update):
  - **Sibelga 2024:** turnover **EUR 415.4m** (379.6m 2023) · op. profit **74.7m** · profit **49.1m** · distributed to municipalities **49.1m**.
  - Assets **1.511bn** · equity **861m** · LT fin. debt **357m** · tangible FA **1.326bn**.
  - Tariff proposal: total income **347.5m** · fair margin **47.9m** · manageable **131.4m** · non-manageable **216.1m** · RAB init **1.198bn** (end-2018).
  - **Fluvius deepen:** ops result **482m** · network tariff rev **2.931bn** · GEC/CHP cost **+149m** · WACC **5.2%** · EQ/RAB **33%** · staff **5 997** · dividend policy **60%** · assets **19.8bn**.
  - Dual/triple grid stack: **Fluvius VL DSO** + **Elia federal TSO** + **Sibelga BCR DSO**.
- Mons BI2026 / Antwerp bulk register still not newly filled.
- Wrote: sources 2; entity 1; budgets 33; cmt 2; lb 2; rq_166=done; seeded **rq_167**.
- FOI: residual municipal dividend L5 + local FOIs human send.
- Next: prio5 **rq_167**; deferred **rq_116** SWA.

### 2026-07-28T07:25:00Z — tick 172
- Unit: **rq_167** (FOI-adjacent hole-fill — **Vivaqua SC Rapport Financier 2024**)
- Found (strong primary annual accounts, RSM audit unqualified):
  - **CA EUR 325.925m 2024** (333.958m 2023) · ventes/prestations **469.7m** · op. profit **25.7m** · **net loss −0.86m** (FRT 2022–23 charge **20.6m**).
  - Users Brussels **303.1m** · wholesale **41.8m** · production immobilisée **114.1m** (assain **72.8m**).
  - Assets **1.804bn** · equity **559.5m** · LT fin. debt **1.021bn** · total dettes **1.215bn**.
  - **Subsides en capital net 127.8m** (public nets **26.7m** + Modave **0.8m** + tiers **100.3m**).
  - **MFC Brugel path** 2022–26: **16.2 / 21.6 / 24.7 / 28.7 / 27.8m** (sum ~**119m** in tariffs).
  - Hydria assainissement **35.0m** · BCR **BEI guarantee 206.6m** · Hydralis pension gap **147.0m** off-BS (cover **83.8%**).
  - **No dividend** (IPM tax regime — profits to immunised reserves only). FTE **1 262**.
  - Dual water stack: **Vivaqua BCR** + **Aquafin VL** + **SPGE WAL** (+ Hydria regional sanitation).
- Mons BI2026 / Antwerp bulk register still not newly filled.
- Wrote: sources 1; entity update; budgets 27; cmt 2; lb 2; FOI gap_interco note; rq_167=done; seeded **rq_168**.
- FOI: residual L5 municipal dividends + BCR 180m capital cash calendar human send.
- Next: prio5 **rq_168**; deferred **rq_116** SWA.

### 2026-07-28T07:45:00Z � tick 173
- Unit: **rq_168** (FOI-adjacent hole-fill � **ORES Assets Walloon DSO 2024**)
- Found (strong primary investor presentation BGAAP + IFRS consol accounts):
  - **Turnover BGAAP EUR 1,067.9m 2024** (1,130.3m 2023) � **EBITDA 322.1m** (30.2% margin) � **EBIT 151.6m** � **net 72.4m** (IFRS profit **66.89m**).
  - **Gridfee 907.6m** (elec **716.7m** + gas **190.9m**) � RAB **4.17bn** � CAPEX **434m** (2023: 384m).
  - Assets BGAAP **5.057bn** � equity **2.050bn** � LT debt **2.143bn** � ST debt **319m** � capital subsidies BS **110.1m**.
  - **Dividendes associ�s 76.145m** 2024 (AR; IFRS paid re 2023: **74.668m**) � municipal public transfer from regulated tariffs.
  - CWaPE 2025 auth rev: elec **630.4m** + gas **218.5m** � WACC **4.027%** � funding need 2025 **~530m**.
  - Elec regulatory balances total **242.5m** � gas **67.6m** � 100% Walloon municipal ownership via intercommunales.
  - Dual/triple DSO stack: **Fluvius VL** + **ORES (+RESA residual) WAL** + **Sibelga BCR** + **Elia** federal TSO.
- Mons BI2026 / Antwerp bulk register / RESA still open for next ticks.
- Wrote: sources 2; entity 1; budgets 28; cmt 2; lb 2; FOI gap_interco note; rq_168=done; seeded **rq_169**.
- FOI: residual L5 municipal dividends Fluvius/RESA + BCR capital calendar human send.
- Next: prio5 **rq_169** (RESA/Antwerp/Mons/De Lijn/taxex); deferred **rq_116** SWA.

### 2026-07-28T08:05:00Z � tick 174
- Unit: **rq_169** (FOI-adjacent hole-fill � **RESA SA Intercommunale comptes 2024**)
- Found (strong primary NBB annual accounts, AG 04-06-2025, PwC):
  - **Chiffre d'affaires EUR 383.881m 2024** (392.969m 2023) � ventes/prestations **500.682m** (incl prod. immobilis�e **94.6m**).
  - **Op. profit 76.915m** � pre-tax **63.501m** � **net 48.250m** (51.113m 2023).
  - Assets **1.955bn** � fixed **1.594bn** � equity **955.6m** � capital **657.9m**.
  - LT financial debt **759.6m** (bonds **500m** + credit **259.6m**) � total dettes **977.2m**.
  - **Dividend (r�mun�ration de l'apport) 18.8m** (same 2023) � b�n�fice � distribuer **18.95m**.
  - Capital subsidies BS **39.762m** (was **7.792m** 2023) � personnel **107.3m** � D&A **57.4m**.
  - Completes **Walloon dual DSO map**: ORES **1.068bn** + RESA **384m** vs Fluvius single VL + Sibelga BCR.
- Mons BI2026 / Antwerp bulk register still open.
- Wrote: sources 1; entity 1; budgets 20; cmt 1; lb 2; FOI gap_interco note; rq_169=done; seeded **rq_170**.
- FOI: residual Fluvius municipal L5 + BCR capital calendar human send; RESA entity dividend filled.
- Next: prio5 **rq_170**; deferred **rq_116** SWA.

### 2026-07-28T08:25:00Z � tick 175
- Unit: **rq_170** (FOI-adjacent hole-fill � **De Lijn Ge�ntegreerd jaarverslag 2025**)
- Found (strong primary statutory accounts + press, figures in kEUR �1000):
  - **Omzet EUR 1,420.0m 2025** (1,423.7m 2024) � bedrijfsopbrengsten **1,497.1m** � bedrijfskosten **1,627.8m** � bedrijfsverlies **-130.7m**.
  - **Vlaams Gewest tussenkomst in omzet 1,207.9m** (incl PPS beschikbaarheidsvergoeding **53.1m**) � main public cash perimeter.
  - **Kapitaalsubsidies cash 247.3m** 2025 � BS kapitaalsubsidies **2,143.3m** � assets **3,085.4m** � equity **2,252.1m**.
  - Personnel **625.4m** � diensten **731.9m** � CAPEX aanschaf **299.6m** � LT debt **371.8m** (PPS leasing).
  - **Net profit 20k** (matches press) � dotatie **-27.5m** delta 2025 � e-bus order **400m** / 652 buses � 2026 hefbomen **45m** + imposed **35.5m**.
  - Passengers **372.9m** � closes material **gap_de_lijn** public perimeter (residual: optional cash-code recon).
- Wrote: sources 2; budgets 21; cmt 1; lb 1; FOI note; raw PDF; rq_170=done; seeded **rq_171**.
- FOI: gap_de_lijn largely filled public; residual Antwerp/Mons FOIs human send.
- Next: prio5 **rq_171**; deferred **rq_116** SWA.

### 2026-07-28T08:45:00Z � tick 176
- Unit: **rq_171** (FOI-adjacent hole-fill � **SWDE Rapport Financier 2024**)
- Found (strong primary RF + Faits & chiffres; kEUR �1000):
  - **CA full EUR 568.129m 2024** (Faits; incl assainissement) � CA hors assain **340.575m** � produits exploitation **428.7m**.
  - **EBITDA 132.5m** � op. result **-10.8m** � fin. result **+22.5m** (NRB sale gain **24.5m**) � **net 10.253m**.
  - Assets **2.369bn** � equity **1.465bn** � capital subsidies **285.4m** � LT fin. debt **644.9m** � gross fin. debt **722m**.
  - CAPEX **272.4m** (travaux **263.5m**) � personnel **136.0m** � D&A **116.4m**.
  - **No dividend** (b�n�fice � distribuer 0; all to reserves). CVD **2.80 �/m�** � pop served **2.53m** � 190 communes.
  - Dual water stack complete: **SWDE WAL** + **Vivaqua BCR** + **Aquafin VL** (+ SPGE assainissement).
- Mons BI2026 / Antwerp register still open.
- Wrote: sources 2; entity 1; budgets 19; cmt 1; lb 2; FOI note; rq_171=done; seeded **rq_172**.
- FOI: residual Fluvius municipal L5 + BCR capital calendar human send.
- Next: prio5 **rq_172**; deferred **rq_116** SWA.

### 2026-07-28T09:05:00Z – tick 177
- Unit: **rq_172** (FOI-adjacent hole-fill – **Aquafin JV BE-GAAP 2024 + SPGE en bref 2024**)
- Found (strong primary Aquafin statutory; SPGE key figures official site):
  - **Aquafin:** omzet **EUR 673.1m 2024** (662.1m 2023) ? bedrijfsopbrengsten **724.2m** ? op. profit **77.7m** ? **net 4.435m**.
  - Assets **4.125bn** ? equity **1.116bn** ? capital **298.4m** (PMV 100%) ? capital subsidies **780.5m**.
  - LT fin. debt **2.208bn** (bonds **540m** + banks **1.667bn**) ? ST fin **150m** ? D&A **217.9m** ? personnel **119.2m** ? FTE **1_201**.
  - Projects delivered **226m** 2024 ? Moody's **Aa3** ? commercial paper open **145.5m**.
  - **SPGE:** CA **418m** ? debt **1.581bn** ? bilan **3.738bn** ? invest **>200m** ? FTE **58** ? Moody's **A3**.
  - Completes dual sanitation: **Aquafin VL** + **SPGE WAL** (+ Vivaqua Hydria BCR) alongside drinking water SWDE/Vivaqua/Farys class.
- Mons BI2026 / Antwerp register still open.
- Wrote: sources 2; entity 1+update; budgets 21; cmt 2; lb 2; FOI note; rq_172=done; seeded **rq_173**.
- FOI: residual Fluvius municipal L5 + BCR capital + SPGE OAA top-20 human send.
- Next: prio5 **rq_173**; deferred **rq_116** SWA.

### 2026-07-28T09:25:00Z – tick 178
- Unit: **rq_173** (FOI-adjacent hole-fill – **De Watergroep JV 2024**)
- Found (strong primary integrated annual report / statutaire jaarrekening):
  - **Omzet EUR 838.3m 2024** (793.7m 2023) ? bedrijfsopbrengsten **955.2m** ? bedrijfskosten **954.1m**.
  - **EBITDA 97.3m** ? op. result **+1.1m** ? **net loss -6.7m** (third consecutive loss; -20.4m 2023).
  - Assets **2.248bn** ? equity **1.256bn** ? capital **750.8m** ? capital subsidies **97.6m**.
  - Fin. debt **711.4m** (LT **686.9m** + ST **24.5m**) ? net debt **706.1m** ? schuldgraad **7.26x** EBITDA.
  - Personnel **159.8m** ? services **665.9m** ? D&A **93.4m** ? FTE **1_651** ? **177** municipalities.
  - EIB investment credit facility **350m** class ? drinkwater div result **-16.1m** ? afvalwater **+9.5m**.
  - Dual water map: **De Watergroep VL** (+ Farys/Pidpa/water-link residual) + **SWDE WAL** + **Vivaqua BCR**.
- Note: public Farys files found only Creat Services DV (omzet 70–89m service co), not Farys ov full utility accounts – residual for next tick.
- Wrote: sources 1; entity 1; budgets 20; cmt 1; lb 2; rq_173=done; seeded **rq_174**.
- FOI: residual Fluvius munis + BCR capital + SPGE OAA + Farys ov if still opaque; human send.
- Next: prio5 **rq_174**; deferred **rq_116** SWA.

### 2026-07-28T09:45:00Z – tick 179
- Unit: **rq_174** (FOI-adjacent hole-fill – **Pidpa Financieel jaarverslag 2025**)
- Found (strong primary financial annual report):
  - **Omzet water EUR 382.8m 2025** (+31.8% vs 2024) ? total omzet **402.7m** (+27.8%).
  - Water 2024 series: BGS **73.0m** + GS **99.1m** + WATER **118.4m** = **290.5m**.
  - **Net profit 31.321m** (Water **14.4m** + HidroRio **9.4m** + HidroGem **7.6m**).
  - Assets **1.595bn** ? equity **859.3m** ? solvability **53.9%** ? invest **~183m** (riolering ~96m).
  - 46 sewer municipalities ? mandate extended +18y Mar 2025 ? Antwerp Borsbeek exit 2026-01-01.
  - Dual water map: **De Watergroep 838m** + **Pidpa 403m** + SWDE/Vivaqua; Farys ov still public-opaque.
- Wrote: sources 1; entity 1; budgets 15; cmt 1; lb 1; rq_174=done; seeded **rq_175**.
- FOI: residual Farys ov full accounts + Antwerp/Mons FOIs human send.
- Next: prio5 **rq_175**; deferred **rq_116** SWA.

### 2026-07-28T10:05:00Z - tick 180
- Unit: **rq_175** (FOI-adjacent hole-fill - **Water-link OV jaarrekening 2025**)
- Found (strong primary statutaire jaarrekening VOL; vector-rendered pages):
  - **Omzet EUR 254.546m 2025** (225.867m 2024) · bedrijfsopbrengsten **426.904m** · bedrijfskosten **406.668m**.
  - **Bedrijfswinst 20.237m** · PBT **23.150m** · tax **6.687m** · **net profit 16.509m** (16.917m 2024).
  - Assets **571.527m** · equity **313.681m** · inbreng **189.275m** · reserves **120.613m**.
  - Debt total **250.161m** · LT fin debt **37.747m** · capital subsidies **1.767m**.
  - Uit te keren winst (vergoeding inbreng) **4.160m** · personnel **57.585m**.
  - JV ops: produce **154.2m m3** · staff **488** · invest water **15.4m** + sewer **57m**.
  - KBO **0204.923.881** · Grant Thornton unqualified · dual VL water with DWG/Pidpa; Farys ov residual.
- Wrote: sources 2; entity 1; budgets 22; cmt 1; lb 1; rq_175=done; seeded **rq_176**.
- FOI: residual Farys ov full accounts + Antwerp/Mons FOIs human send.
- Next: prio5 **rq_176**; deferred **rq_116** SWA.

### 2026-07-28T10:05:00Z - progress@180
- Refreshed **progress_every_10_ticks.md**: L2 ~60-68% (VL water stack closed: DWG+Pidpa+Water-link+Farys residual); inventory budgets~1857 cmt~327 lb~278 FOI ready~55.
- Refreshed **doge_waste_top10_current.md**: top10 unchanged (cheque economy 8.83 ... gas product 7.98); n_lb=278.

### 2026-07-28T10:25:00Z - tick 181
- Unit: **rq_176** (FOI-adjacent hole-fill - **Farys OV jaarrekening 2024**)
- Found (strong primary integrated annual report maatschappelijke jaarrekening; prior public files were Creat Services DV only):
  - **Omzet EUR 506.292m 2024** (496.0m 2023 / 454.0m 2022) · bedrijfsopbrengsten **597.954m**.
  - **Bedrijfswinst 73.736m** · PBT **38.609m** · **net 38.180m** (29.2m 2023).
  - Assets **3.655bn** · MVA **3.231bn** (~88pct) · equity **1.921bn** · cap subsidies **245m**.
  - LT debt **1.337bn** (bank 934m + MTN/other 371m) · ST debt **370m** · invest MVA **190m**.
  - Personnel **96.8m** · fin. costs **42.8m** · sport+water+sewer perimeter (ex-TMVW).
  - **VL water dual complete:** DWG 838m + Pidpa 403m + Water-link 255m + **Farys 506m** (+ SWDE/Vivaqua/Aquafin).
- Wrote: sources 2; entity 1; budgets 25; cmt 1; lb 1; rq_176=done; seeded **rq_177**.
- FOI: Antwerp/Mons + other ready stack human send; Farys ov gap closed by public fill.
- Next: prio5 **rq_177**; deferred **rq_116** SWA.

### 2026-07-27T11:26:51Z - tick 182
- Unit: **rq_178 seed** (user flag — aircon + fridge subsidies high clown)
- Found: **NOT previously L5-mapped** (only aggregate heat-pump/MVP). Primary portals:
  - **Mijn Kortingsbon** 250 EUR means-tested fridge/washer/freezer; new apps stopped 2026-01-01; annual cash paid Unknown.
  - **MVP lucht-lucht warmtepomp** 300-600 EUR (income band); dual-use AC rules; pure cooling excluded on paper; cash split vs other WP Unknown.
- Wrote: research_queue **rq_178** prio9 open; sources 2; leaderboard **lb_vl_mijn_kortingsbon_appliances** abs 8.5 / **lb_vl_airco_mvp_luchtlucht** abs 9.0; FOI draft gap_vl_odv_mvp_cash + items 4-5 air-air + kortingsbon.
- FOI: expanded ready letter (human send); no invent euros.
- Next: execute **rq_178** cash hunt (VEKA/Fluvius/CoA) OR concurrent prio5 **rq_177**.

### 2026-07-28T10:45:00Z - tick 182
- Unit: **rq_178** (high-clown — **Mijn Kortingsbon white goods + MVP lucht-lucht airco**)
- Found (strong portals + medium/strong parliamentary QA; **no invent of redeemed cash**):
  - **Mijn Kortingsbon** face **250 EUR**/appliance; means-tested; **new apps stopped 2026-01-01**.
  - **Verstuurde** bonnen (SV89/718): **2020 9_808** · **2021 14_629** strong · **2022 ~29_258** medium (2x 2021).
  - Face-value issued (sent x250, **not cash paid**): **2.45m / 3.66m / ~7.3m** 2020-22.
  - **2019 used** wash 2_314 + fridge 2_329 → **1.161m** cash medium (prior PQ cite; partial).
  - **MVP lucht-lucht** rates **300-600 EUR** strong portal; cash split vs other WP **Unknown** (parent CoA heat premiums **22m 2023**).
- Wrote: sources portals+2 PQ; budgets face-issued series; cmt 1; lb 2; rq_178=done; FOI note.
- FOI: **gap_vl_odv_mvp_cash** ready (redeemed cash by appliance + air-air split) — human send only.
- Next: prio5 **rq_177**; deferred **rq_116** SWA.

### 2026-07-28T11:05:00Z - tick 183
- Unit: **rq_177** (FOI-adjacent hole-fill - **Fluxys Belgium gas TSO AR2025**)
- Found (strong primary regulated press 2026-03-31; dual electricity Elia):
  - **Operating revenue EUR 650.453m 2025** (608.789m 2024) ? **EBITDA 320.111m** ? EBIT 133.916m ? **net profit 74.897m** (82.061m 2024).
  - **CAPEX 261.751m** (92.1m 2024): transmission **246.2m** (Knokke–Evergem **68.5m**) ? storage 11.5m ? LNG 4.1m.
  - Assets **3.174bn** ? PPE **1.862bn** ? equity **592.8m** ? **net fin debt 326.9m** (was 159.8m).
  - Dividend proposed **1.40 EUR/share** ? payout **98.4m** ? statutory SA profit **85.5m** ? staff **994** (+102).
  - H2/CO2 construction start; Fluxys c-grid appointed CO2 operator FL+WAL (SFPIM partner).
  - **Federal Nov2025 budget intent: withdraw 300m** from Fluxys regulatory-account positive balances (medium; Fluxys contests legality; not cash outturn).
  - Dual map: **Elia electricity TSO** + **Fluxys gas TSO** + DSO stack (Fluvius/ORES/RESA/Sibelga).
- Antwerp register / Mons BI2026: still no public bulk L5 (rechecked search negative).
- Wrote: sources 2; entity 1; budgets 22; cmt 1; lb 2; rq_177=done; seeded **rq_179**.
- FOI: Antwerp/Mons + ready stack human send; no new FOI (Fluxys figures public).
- Next: prio5 **rq_179**; deferred **rq_116** SWA.

### 2026-07-28T11:25:00Z - tick 184
- Unit: **rq_179** (FOI-adjacent hole-fill - **SFPIM federal holding 2025 figures**)
- Found (strong primary official figures page):
  - **Assets EUR 11.679bn** end-2025 (11.523bn 2024) ? **equity 11.445bn** ? financial assets **9.847bn** ? cash **1.355bn**.
  - **Net income 291m** 2025 (315.2m 2024) ? pretax 312m ? **dividend to State 78m** (86m 2024).
  - Recurring financial products **825m** ? opex **35m** ? staff **39** ? portfolio **189** companies ? 8 new interests.
  - Non-recurrent charges **586m** 2025 (1.259bn 2024) ? non-rec income 112m – large valuation swing.
  - Key highlight 211.2m profit medium (definition vs table net 291m unclear).
  - Dual holding map: **SFPIM federal** + PMV Flanders + Wallonie Entreprendre.
- Antwerp register / Mons BI2026: still no public bulk L5 (rechecked negative).
- Wrote: sources 2; entity 1; budgets 23; cmt 1; lb 2; FOI **gap_sfpim_l5_stakes** ready; rq_179=done; seeded **rq_180**.
- FOI: L5 stakes top50 + impairments human send only.
- Next: prio5 **rq_180**; deferred **rq_116** SWA.

### 2026-07-28T11:45:00Z - tick 185
- Unit: **rq_180** (FOI-adjacent hole-fill - **BIO DFI Annual Report 2025 financials**)
- Found (strong primary AR2025 financials + PDF income table):
  - **Total assets EUR 1.196bn** end-2025 (+1%) ? **equity 1.176bn** (1.159bn 2024; +16.7m).
  - **Income 55.311m** ? gross margin 54.470m ? opex **14.303m** ? cost of risk **20.108m**.
  - Operating result 20.058m ? FX -5.947m ? pretax 14.111m ? **net 8.971m** (19.2m 2024).
  - **Dividend to Belgian State 4.5m** ? retained earnings 34.9m.
  - **Approvals record 235m / 30 projects** (signed 21) ? Africa **55%** ? jobs ~388k direct end-2024.
  - Dual map: **BIO DFI** + **Enabel** implementer + **DGD** ODA (prior ticks).
- Port of Antwerp-Bruges: cargo throughput public; **authority financial accounts still thin** on open press (factsheet cargo-only) – residual for next tick.
- Antwerp register / Mons BI2026: still no bulk L5 public.
- Wrote: sources 3; entity update; budgets 21; cmt 1; lb 2; FOI **gap_bio_l5_portfolio** ready; rq_180=done; seeded **rq_181**.
- FOI: L5 investee list + impairments + State capital path – human send only.
- Next: prio5 **rq_181**; deferred **rq_116** SWA.

### 2026-07-28T12:05:00Z - tick 186
- Unit: **rq_181** (FOI-adjacent hole-fill - **Brussels Airport Company 2025 results**)
- Found (strong primary official press 2026-05-08):
  - **Revenue EUR 828m 2025** (+6%) ? expenses **472m** (439m 2024) ? **EBITDA 356m** (345m).
  - **Net profit 84m** (91m 2024; -7m higher tax) ? **dividend 41m** first since 2019.
  - **CAPEX record 302m** (Brucargo, P30, runway 25L, lounge).
  - Traffic: **pax 24.4m** (+3.3%) ? cargo **795kt** (+8.5%) ? movements **198k**.
  - Ownership: **SFPIM/FPIM 25%** + PMV/private consortium **75%** – links tick184 SFPIM.
  - Jobs class **64k** direct+indirect ? noise-efficient flights **42%** (was 20% 2016).
  - Dual: national hub vs Charleroi BSCA residual.
- Port of Antwerp-Bruges authority P&L still not in open press (cargo-only) – residual **rq_182**.
- Wrote: sources 1; entity 1; budgets 14; cmt 1; lb 2; FOI **gap_bac_balance_sheet** ready; rq_181=done; seeded **rq_182**.
- FOI: full BS/debt/RAB human send only.
- Next: prio5 **rq_182**; deferred **rq_116** SWA.

### 2026-07-28T12:25:00Z - tick 187
- Unit: **rq_182** (FOI-adjacent hole-fill - **BSCA Charleroi dual to Brussels Airport**)
- Found (strong primary AR2024 EN PDF):
  - **Turnover EUR 126.860m 2024** (115.934m 2023; +9.42%) ? **EBITDA 28.637m** ? **net 21.412m**.
  - Investments **3.880m** ? pax **10.501m** (+12%) ? avg employees **825** ? active FTE **645**.
  - Shareholding: **Belgian Airport SA 48.32%** ? **SOWAER 35.9%** ? Sambrinvest 13.7% ? Igretec 1.7% ? SABCA 0.5%.
  - Exclusive rights to **2041** ? jobs class ~4_650 ? employee profit-share CCT90 1.5m class.
  - Dual map: **BAC Zaventem 828m / 24.4m pax** (SFPIM 25%) vs **BSCA 127m / 10.5m pax** (SOWAER 36%).
- Port Antwerp-Bruges / Credendo: residual for next tick.
- Wrote: sources 1; entities 2; budgets 14; cmt 1; lb 2; FOI **gap_sowaer_accounts** ready; rq_182=done; seeded **rq_183**.
- FOI: SOWAER full accounts human send only.
- Next: prio5 **rq_183**; deferred **rq_116** SWA.

### 2026-07-28T12:45:00Z - tick 188
- Unit: **rq_183** (FOI-adjacent hole-fill - **Credendo ECA group consol 2024**)
- Found (strong primary management report on 2024 consol FS):
  - **Total assets EUR 3.9206bn** end-2024 (3.696bn 2023) ? **equity ex-NCI 3.3021bn**.
  - Financial investments **3.086bn** ? cash **446.1m** ? insurance liabilities **492.1m**.
  - Group GWP after rebates **481m** (+6% record) ? ECA GWP **291m** (+13%) ? insured transactions **8.9bn** (+46%).
  - Insurance service result **174.1m** (74.0m 2023) ? net ins+fin result **324.0m** (191.7m).
  - Total comprehensive income **257.2m** profit (135.5m 2023).
  - Cover capacity **33bn** class medium (portal AA S&P) – contingent sovereign-linked risk.
  - Official Belgian export credit agency state-backed; dual private short-term credit arms.
- Port of Antwerp-Bruges authority P&L still residual.
- Wrote: sources 3; entity 1; budgets 20; cmt 1; lb 2; FOI **gap_credendo_l5_claims** ready; rq_183=done; seeded **rq_184**.
- FOI: L5 claims + state guarantee perimeter human send only.
- Next: prio5 **rq_184**; deferred **rq_116** SWA.

### 2026-07-28T13:05:00Z - tick 189
- Unit: **rq_184** (FOI-adjacent hole-fill - **skeyes ANS / ex-Belgocontrol 2024**)
- Found (strong primary Jaarverslag 2024 NL PDF + media KF2025):
  - **Omzet EUR 335.2m 2024** ? En-route **261.7m** ? Terminal EBBR **66.2m** ? invest **36.4m**.
  - **Profit 15.4m** ? equity components sum **~308.4m** (capital 170m + reserves) ? 2023 EV **290.3m**.
  - En-route unit rate **EUR 112.08** ? 4th management contract May 2024 with Belgian State.
  - **COVID state loan 110m** (first repay **15.7m** Dec 2024; 7y path).
  - RP3 correction receivables **195.4m** deferred into unit rates **2024-2030**.
  - Flights **946_768** 2024 / **1_035_084** 2025 (+4%) ? staff **982** / **1006**.
  - Dual map: **skeyes ANS** + **BAC/BSCA airports** (prior ticks).
- Port of Antwerp-Bruges authority P&L still thin public – residual **rq_185**.
- Wrote: sources 2; entity 1; budgets 18; cmt 1; lb 2; FOI **gap_skeyes_bs_2025** ready; rq_184=done; seeded **rq_185**.
- FOI: 2025 full BS + multi-year correction schedule human send only.
- Next: prio5 **rq_185**; deferred **rq_116** SWA.

### 2026-07-28T13:25:00Z - tick 190
- Unit: **rq_185** (FOI-adjacent hole-fill - **SOWAER comptes 2020-2025 public fill**)
- Found (strong primary official comptes PDF to 31/12/2025):
  - **Assets EUR 491.747m** end-2025 (494.2m 2024) ? **equity 366.922m** ? capital 322.3m.
  - **Ventes 46.986m 2025** (64.8m 2024 / 81.3m 2023) ? **net 0.300m** (7.41m 2024 / 18.45m 2023).
  - Op. result **-3.83m** 2025 ? D&A 31.0m ? personnel 7.69m ? fin assets **37.9m** (BSCA stake class) ? PPE **374.4m**.
  - Dettes **124.8m** (LT 89.9m) ? cash 49.8m ? treasury notes programme ceiling **85m** Region-guaranteed.
  - Dual map: **SOWAER WAL airports** + **BSCA 127m** + **BAC 828m / SFPIM 25%**.
- **gap_sowaer_accounts** major public fill ? status **answered** (residual L5 stake book values optional).
- Port of Antwerp-Bruges authority P&L still residual.
- Wrote: sources 1; entity update; budgets 21; cmt 1; lb 1; FOI answered; rq_185=done; seeded **rq_186**.
- Progress@190: L2 ~62-70%; inventory budgets~2042 cmt~337 lb~296 FOI ready~60; top10 waste unchanged.
- Next: prio5 **rq_186**; deferred **rq_116** SWA.

### 2026-07-28T13:25:00Z - progress@190
- Refreshed **progress_every_10_ticks.md**: L2 ~62-70% (SFPIM+airports+Credendo+skeyes+SOWAER since 180); FOI ready ~60.
- Refreshed **doge_waste_top10_current.md**: top10 unchanged (cheque 8.83 … gas product 7.98); n_lb=296; Credendo cover just outside top10.

### 2026-07-28T13:45:00Z - tick 191
- Unit: **rq_186** (FOI-adjacent hole-fill - **SOFICO Walloon structural infra RA2024**)
- Found (strong primary Rapport annuel 2024; NBB-deposited accounts):
  - **Produits d'exploitation EUR 495.1m 2024** (465.7m 2023 / 417.9m 2022) ? charges 397.6m.
  - **B?n?fice net 100.7m** (97.8m / 47.4m) ? **investissements record 265m**.
  - **PKPL truck toll 347m** (+11.2%; 1.92bn paid-km stable) – main funding of structural network.
  - Infra assets under management **2.581bn** ? equity **2.174bn** ? net cash 197m ? **net debt 336.8m** (EIB 351.8 + MTN 182).
  - Network ~2_700 km autoroutes+nationales; cum invest since 2010 ~**3.7bn** class (370.8m 2024).
  - Dual map: **SOFICO WAL roads** vs Flanders AWV; locks Meuse; fibre; renewable concessions.
- Port of Antwerp-Bruges authority P&L still residual.
- Wrote: sources 1; entity 1; budgets 20; cmt 1; lb 2; rq_186=done; seeded **rq_187**.
- FOI: none new (public strong); residual optional CAPEX L5 project list.
- Next: prio5 **rq_187**; deferred **rq_116** SWA.

### 2026-07-28T14:05:00Z - tick 192
- Unit: **rq_187** (FOI-adjacent hole-fill - **PMV Flanders investment holding 2024**)
- Found (strong primary JV2024 + official press):
  - **Gefinancierd & beheerd vermogen EUR 1.941bn** ? **ge?nvesteerd 1.332bn**.
  - **Nettoresultaat 32.5m** (10th consecutive profit; group share 32.7m) ? dividend reserved **3.8m**.
  - **Nieuwe investeringen 393.2m** 2024 (+46% press; kerncijfers subset 286m loans/capital/funds).
  - Geplaatst kapitaal **1.776bn** ? equity consol **2.480bn** (incl Aquafin perimeter) ? fin assets PMV-level **1.280bn**.
  - **Gigarant** outstanding guarantees **695m** (7 new / 91m granted 2024).
  - Dual map: **PMV Flanders** + **SFPIM federal** (11.7bn) + **Wallonie Entreprendre**; BAC stake path; Aquafin 100%.
- Port of Antwerp-Bruges / Li?ge Airport authority full P&L still residual.
- Wrote: sources 2; entity 1; budgets 15; cmt 1; lb 2; FOI **gap_pmv_l5_stakes** ready; rq_187=done; seeded **rq_188**.
- FOI: L5 stakes + Gigarant claims human send only.
- Next: prio5 **rq_188**; deferred **rq_116** SWA.
### 2026-07-28T14:25:00Z - tick 193
- Unit: **rq_188** (FOI-adjacent hole-fill - **Port of Antwerp-Bruges + North Sea Port**)
- Found (POAB medium-strong NBB-derived Companyweb; NSP strong primary jaarrekening 2023 + GS letter 2024):
  - **POAB omzet EUR 500.8m 2024 / 507.0m 2025** (494.9m 2023; 458.6m 2022).
  - **Net -38.5m 2024 then +80.3m 2025** (100.2m 2023; 40.9m 2022); equity **2.31-2.36bn**; FTE ~1.6k.
  - Shareholders: **Antwerp 80.2% / Bruges 19.8%** public-law NV; throughput 278mt 2024 cargo booklet.
  - **North Sea Port SE 2023**: netto-omzet **115.0m**, total op income **131.5m**, EBIT **52.5m**, net **37.8m**; assets **944.8m**; equity group **601m** + result 37.8m; LT debt **196.4m**.
  - 2024 NSP: EBIT **+5.1%**, PBT **-11.1%** vs 2023; **no dividend while guarantees** (GS Zeeland letter).
  - Dual map: **POAB large BE port** vs **NSP cross-border Gent-Zeeland** (Gent 48.52% / Zeeland 25%).
- **Major residual closed** for multi-tick Port authority P&L hole.
- Wrote: sources 4; entities 2; cmt 2; lb 2; budgets 12; FOI **gap_poab_dividend_capex** ready; rq_188=done; seeded **rq_189**.
- FOI: city dividend cash-by-year + CAPEX top20 human send only; Liege Airport authority still residual.
- Next: prio5 **rq_189**; deferred **rq_116** SWA.
### 2026-07-28T14:45:00Z - tick 194
- Unit: **rq_189** (FOI-adjacent hole-fill - **Liege Airport SA** dual BSCA/BAC/SOWAER)
- Found (medium-strong Companyweb/NBB + strong Parlement Wallonie QE Neven + annex 3120):
  - **Omzet EUR 56.16m 2024 / 65.04m 2025** (48.0m 2022; **95.6m 2023 spike** recon residual).
  - **Net 14.31m 2024 / 17.49m 2025**; equity **75.2 ? 85.6m**; FTE 223 ? 241.
  - Shareholders: **NEB 50.36% / ADP 25.54% / SOWAER 24.10%** (PW strong).
  - Dividends to SOWAER: **1.269 / 1.231 / 1.421m** 2021-23 (no full multi-shareholder path).
  - **WAL subsidies** annex (kEUR sums): **29.0 / 31.4 / 30.9m** 2021-23 (mission + incendie + s?ret?).
  - Dual: Liege cargo **~65m** vs BSCA **127m** vs BAC **828m**; SOWAER infra owner to 2041.
- Wrote: sources 3; entity 1; budgets 12; cmt 1; lb 2; FOI **gap_liege_airport_subsidy_l5** ready; rq_189=done; seeded **rq_190**.
- FOI: 2024-25 subsidy cash + contracts + full dividends human send only; Antwerp/Mons still residual.
- Next: prio5 **rq_190**; deferred **rq_116** SWA.
### 2026-07-28T15:05:00Z - tick 195
- Unit: **rq_190** (FOI-adjacent hole-fill - **Wallonie Entreprendre** dual PMV/SFPIM)
- Found (strong official WE press AR2024+AR2025 + medium-strong NBB/Companyweb):
  - **Equity EUR 4.905bn 2024 / 4.981bn 2025** (NBB); ops omzet thin ~3m (holding).
  - **Net 279.8m 2024 / 151.2m 2025** (press 278/151; exits+dividends; write-downs 76m 2024).
  - **New investments 492m 2024 / 613m 2025** (1253 / 1330 projects).
  - **Guarantees granted 228m 2024 / 208m 2025** (1588 firms 2025); dual Gigarant 695m VL.
  - **Dividend 55.3m 2024 / 70.3m 2025** to Wallonie + Belfius.
  - Roadmap 2025-29: invest **2.5bn**, guarantees **1.25bn**, cum profit **750m**.
  - Dual map: **WE Wallonie ~5bn equity** + **PMV Flanders 1.94bn managed** + **SFPIM federal 11.7bn**.
- Wrote: sources 3; entity 1; budgets 12; cmt 1; lb 3; FOI **gap_we_l5_stakes** ready; rq_190=done; seeded **rq_191**.
- FOI: L5 stakes + guarantee claims human send only; Antwerp register / Mons BI2026 still residual.
- Next: prio5 **rq_191**; deferred **rq_116** SWA.
### 2026-07-28T15:25:00Z - tick 196
- Unit: **rq_191** (FOI-adjacent hole-fill - **Vlaamse Waterweg + AWV GIP** dual SOFICO)
- Found (medium-strong NBB/Companyweb DVW + strong MORA GIP Table1 from Dept MOW):
  - **DVW omzet EUR 59.2m 2024 / 61.6m 2025**; **net -6.8m / -30.1m**; **equity 3.135 ? 3.210bn**; FTE ~1.23k.
  - **DVW GIP invest 288.0 / 380.9 / 383.8m** 2025-27.
  - **AWV GIP invest 708.2 / 679.7 / 685.3m** 2025-27 (largest roads entity).
  - **MOW GIP total ~2.585 / 2.424 / 2.501bn**; asset management **~733m** 2025 (target **1.4bn** 2029).
  - Dual map: **AWV+DVW Flanders** vs **SOFICO Wallonia** (op rev 495m / infra 2.58bn).
- Wrote: sources 2; entities 2; budgets 13; cmt 2; lb 3; FOI **gap_awv_opex_l5** ready; rq_191=done; seeded **rq_192**.
- FOI: full AWV opex + GIP top30 L5 human send only; Antwerp register / Mons BI2026 still residual.
- Next: prio5 **rq_192**; deferred **rq_116** SWA.
### 2026-07-28T15:45:00Z - tick 197
- Unit: **rq_192** (FOI-adjacent hole-fill - **Lantis + De Werkvennootschap** mobility SPVs)
- Found (medium-strong NBB/Companyweb + strong GIP MORA Table1):
  - **Lantis (BAM)**: equity **?990.7 ? 827.6m** 2022-25; net **-28.3 / -62.3 / -93.6 / -7.3m**; gross margin **53-63m**; FTE 126?182; no omzet published.
  - **Lantis GIP** 2025-27: **?96.0 / 235.2 / 276.7m** (vs BO2026 Oosterweel line **?889.9m** ? channel recon FOI).
  - **De Werkvennootschap**: omzet **?19.1 ? 143.3m** 2022-25; net **0.32 ? 0.87m**; equity **~41m**; FTE ~24.5.
  - **DWV GIP** 2025-27: **?243.8 / 247.8 / 248.8m**.
  - Dual map: Lantis Oosterweel SPV + DWV multi-project works + AWV/DVW/SOFICO infra stack.
- Wrote: sources 2; entities 2; budgets 12; cmt 2; lb 2; FOI **gap_lantis_oosterweel_cash** ready; rq_192=done; seeded **rq_193**.
- FOI: Oosterweel cash-by-year recon human send only; Antwerp register / Mons BI2026 still residual.
- Next: prio5 **rq_193**; deferred **rq_116** SWA.
### 2026-07-28T16:05:00Z - tick 198
- Unit: **rq_193** (FOI-adjacent hole-fill - **Infrabel** dual NMBS)
- Found (medium-strong NBB/Companyweb + strong official press 2024):
  - **Omzet EUR 1.369bn 2024 / 1.426bn 2025** (1.438bn 2023; 1.219bn 2022).
  - **Net 50.8m 2024 / 95.0m 2025** (press 50m 2024); **equity 19.96 ? 20.54bn**.
  - **Invest 1bn 2024** network; multi-year plan **6.5bn 2025-2029**.
  - Punctuality **90.1%** 2024; State **100%**; TUC RAIL 100%.
  - Dual map: **Infrabel net** + **NMBS ops** (ESA package prior; FOI toelage split residual).
- Wrote: sources 2; entity 1; budgets 8; cmt 1; lb 2; FOI **gap_infrabel_state_toelage** ready; rq_193=done; seeded **rq_194**.
- FOI: state toelage cash-by-year + CAPEX L5 human send only; Antwerp/Mons still residual.
- Next: prio5 **rq_194**; deferred **rq_116** SWA.
### 2026-07-28T16:25:00Z - tick 199
- Unit: **rq_194** (FOI-adjacent hole-fill - **NMBS** dual Infrabel)
- Found (medium-strong NBB/Companyweb statutory; press consol class medium recon):
  - **Statutory omzet EUR 2.560bn 2024 / 2.615bn 2025** (2.563bn 2023; 2.215bn 2022).
  - **Statutory net 53.1m 2024 / 10.8m 2025** (67.1m 2023); **equity 7.72 ? 8.05bn**.
  - Press/consol class (secondary): omzet **~3.022bn** / net **~53.1m** / EBITDA **~370m** / CAPEX **~1.13bn** ? **recon FOI** vs statutory.
  - Dual map: **NMBS ops equity ~8bn omzet ~2.6bn** + **Infrabel net equity ~20bn omzet ~1.4bn**.
- Wrote: sources 2; budgets 6; cmt 1; lb 1; FOI **gap_nmbs_consol_vs_statutory** ready; rq_194=done; seeded **rq_195**.
- FOI: toelage cash + consol recon human send only; Antwerp/Mons still residual.
- Next: **tick 200 progress coverage % + waste top10** then prio5 **rq_195**; deferred **rq_116** SWA.
### 2026-07-28T16:45:00Z - tick 200 ? progress coverage % + waste top10
- Unit: **progress@200** (mandatory every-10-ticks refresh; no new research unit)
- Coverage (order-of-magnitude vs ?347.956 bn TE):
  - **A L0 / B L1:** 100% / 100% (unchanged strong)
  - **C L2:** **~68?76%** (up from ~62?70% @190) ? PMV, ports POAB/NSP, Liege Airport, WE 5bn, DVW+AWV GIP, Lantis+DWV, Infrabel+NMBS
  - **D L5:** **~7?14%** still thin structural
  - **E FOI ready:** **~68** (total FOI rows ~72)
- Inventory: budgets ~2151 ? commitments ~349 ? leaderboard ~315 ? entities ~135 ? sources ~414
- Waste top10: taxex/FFS/cheque still dominate (cheque ~8.83 ? gas product ~7.98 class); new SOE L2 not pure-waste top
- Wrote: `progress_every_10_ticks.md`, `doge_waste_top10_current.md`, loop_state, loop_log
- Next: prio5 **rq_195** (Antwerp/Mons/MDK/Enabel hole-fill); deferred **rq_116** SWA
### 2026-07-28T17:05:00Z - tick 201
- Unit: **rq_195** (FOI-adjacent hole-fill - **Enabel** dual BIO)
- Found (strong primary AR 2024-25 finances + medium-strong NBB multi-year):
  - **Turnover EUR 329.2m 2024 / 407.1m 2025**; op. revenue **357.1m** 2024.
  - **Assets 221.9m 2024** (275.8m 2023); **equity ~20.1m** (thin agency model).
  - Result near-zero (**-0.30m 2024 / -0.07m 2025**); staff costs **80.2m**; FTE **~579**.
  - **EU contracts signed 219m** (28) + new partners **72m** in 2024.
  - Seven country programmes launched 2024 multi-year envelopes sum **~349m** class.
  - Dual map: **Enabel implementation** + **BIO DFI** (assets 1.2bn prior).
- Wrote: sources 2; entity 1; budgets 8; cmt 1; lb 1; FOI **gap_enabel_dgd_l5** ready; rq_195=done; seeded **rq_196**.
- FOI: DGD cash + project L5 human send only; Antwerp register / Mons BI2026 still residual.
- Next: prio5 **rq_196**; deferred **rq_116** SWA.
### 2026-07-28T17:25:00Z - tick 202
- Unit: **rq_196** (FOI-adjacent hole-fill - **Fedasil** asylum reception)
- Found (strong primary official Fedasil budget page):
  - **Federal dotation 2024 EUR 929.4m**; total income **946.3m** (EU 12.5m + own 4.4m).
  - **Expenditure 943.4m**: staff **177.7m**; third-party subsidies **558.8m**; housing **73.9m**; medical **59.4m**; rent/maint **48.7m**; invest **3.1m**.
  - Third-party split **%: 76 Red Cross+NGOs / 13 OCMW / 7 private / 2 return NGOs / 2 municipalities** (EUR residual FOI).
  - Dotation path: **296m (2015) ? 929m (2024)** with intermediate years sourced.
- Wrote: sources 1; entity 1; budgets 10; cmt 1; lb 2; FOI **gap_fedasil_l5_partners** ready; rq_196=done; seeded **rq_197**.
- FOI: L5 partner EUR list human send only; Antwerp/Mons still residual.
- Next: prio5 **rq_197**; deferred **rq_116** SWA.

### 2026-07-28T17:45:00Z - tick 203
- Unit: **rq_197** (FOI-adjacent hole-fill - **MDK** maritime dual AWV/DVW)
- Found (strong MORA GIP Table1 + strong GIP annex L5 + ONP structure):
  - **MDK GIP invest EUR 72.475m 2025 / 92.081m 2026 / 92.214m 2027** (smallest MOW entity after buffer).
  - L5 sample: **bagger jachthavens 16.1/15.1/15.1m**; **beloodsing schepen 20+20m**; **veerboot Antwerpen 7.965m**; **HKD 2.435m/yr**; **regulier 5m/yr**; **cyber 2.154m**; **glooiing Nieuwpoort 10m**; **stormvloedkering 2.1/8.5m**.
  - Structure: IVA MOW **4 DAB** (Kust, Loodswezen, Scheepvaartbegeleiding, Vloot) + Staf; ONP has no numeric total opex.
  - Dual map: **MDK coast/ports/pilotage** + **AWV roads** + **DVW inland waterways** (prior ticks).
- Wrote: sources 3; entity 1; budgets 16; cmt 1; lb 2; FOI **gap_mdk_opex_l5** ready; rq_197=done; seeded **rq_198**.
- FOI: full MDK opex+DAB+loodsgelden+GIP outturn human send only; Antwerp register / Mons BI2026 still residual.
- Next: prio5 **rq_198**; deferred **rq_116** SWA.

### 2026-07-28T18:05:00Z - tick 204
- Unit: **rq_198** (FOI-adjacent hole-fill - **Antwerp culture L5 + MJP**)
- Found (strong ebesluit Toneelhuis + strong MJP PR + medium VRT culture):
  - **Toneelhuis 2026 EUR 3.2997m** (exp **2.9172m** + invest **0.3825m**); max package **18.309m** 2026-2031.
  - Culture envelope **25 ? 35m/yr** (medium); **16** named structural partners; makers trajectories **9.2m/6y**.
  - MJP: invest **2.4bn/6y** (**400m/yr**); opex exp **2.2-2.4bn**; rec **2.3-2.5bn**; saldo **110-120m**.
  - Geitestoet package cut **370k ? 150k/6y** (medium).
- Wrote: sources 3; budgets 11; cmt 3; lb 2; foi gap_antwerp notes; rq_198=done; seeded **rq_199**.
- FOI: full machine-readable top20 register still human send; Mons BI2026 residual.
- Next: prio5 **rq_199**; deferred **rq_116** SWA.

### 2026-07-28T18:25:00Z - tick 205
- Unit: **rq_199** (FOI-adjacent hole-fill - **Antwerp culture L5** OBV/ASO/DeSingel)
- Found (strong ebesluit primary):
  - **Opera Ballet Vlaanderen 2026 EUR 1.786m** exp; contracts extended to fusion 2026.
  - **Antwerp Symphony Orchestra 2026 EUR 611k** exp; dual fusion path with OBV.
  - **DeSingel 2026 EUR 100k** exp; max **614.5k** 2026-31 (100/101.6/103.2 path).
  - Culture L5 sample sum **Toneelhuis 3.30 + OBV 1.79 + ASO 0.61 + DeSingel 0.10 = 5.80m** of ~35m envelope class.
- Wrote: sources 2; budgets 5; cmt 3; lb 4; foi gap_antwerp notes; rq_199=done; seeded **rq_200**.
- FOI: residual 12+ culture partners + full register still human send; Mons BI2026 residual.
- Next: prio5 **rq_200**; deferred **rq_116** SWA.

### 2026-07-28T18:45:00Z - tick 206
- Unit: **rq_200** (FOI-adjacent hole-fill - **Antwerp culture L5** Zomer + Extra City)
- Found (strong ebesluit primary):
  - **Zomer van Antwerpen 2026 EUR 1.210m**; max package **7.435m** 2026-2027; future plan 2028-38 due end-2026.
  - **Kunsthal Extra City 2026 EUR 150k**; max **921.8k** 2026-2031.
  - Culture L5 sample sum **6 houses = 7.16m** (Toneelhuis 3.30 + OBV 1.79 + ASO 0.61 + DeSingel 0.10 + Zomer 1.21 + ExtraCity 0.15) of ~35m envelope class.
- Wrote: sources 2; budgets 4; cmt 3; lb 3; foi notes; rq_200=done; seeded **rq_201**.
- FOI: residual partners (hetpaleis AMUZ JEF De Roma Morpho Tutti Fameus …) + full register human send; Mons BI2026 residual; police zone toelage ebesluit candidate.
- Next: prio5 **rq_201**; deferred **rq_116** SWA.

### 2026-07-28T19:05:00Z - tick 207
- Unit: **rq_201** (FOI-adjacent hole-fill - **Politiezone Antwerpen** city toelage)
- Found (strong ebesluit politiebegroting 2026 + 2025 path):
  - **City toelage 2026 EUR 320.677m** (gewone **301.388m** + buitengewoon **19.289m**).
  - **2025 city toelage 318.098m** (280.084 + 38.014).
  - Ordinary exp **396.4m**: staff **306.0m**; ops **86.4m**; transfers 3.85m.
  - Ordinary receipts **408.3m**; invest spend **44.9m**; transfer ord?extra **22.3m**.
  - Dual map: city ~80pct of ord receipts class; federal share residual FOI; largest city transfer vs culture sample 7m.
- Wrote: sources 2; entity 1; budgets 11; cmt 2; lb 2; foi police notes; rq_201=done; seeded **rq_202**.
- FOI: federal per-zone matrix still human send (gap_police_zones); culture residual partners + Mons BI2026 residual.
- Next: prio5 **rq_202**; deferred **rq_116** SWA.

### 2026-07-28T19:25:00Z - tick 208
- Unit: **rq_202** (FOI-adjacent hole-fill - **Antwerp JEF + Free Clinic drug L5**)
- Found (strong ebesluit primary):
  - **JEF 2026 EUR 239.2k**; max **1.470m** 2026-2031 (youth film festival; dual VAF residual).
  - **Free Clinic package 2026 EUR 974.4k**: MSOC **203.7k** + GoiA **263.5k** (dual Zorgbedrijf) + De Nomaad **507.2k**.
  - Culture L5 sample sum **7 houses = 7.40m** (prior 6 + JEF) of ~35m envelope class.
- Wrote: sources 2; budgets 6; cmt 3; lb 3; foi notes; rq_202=done; seeded **rq_203**.
- FOI: residual culture partners + full register + Mons BI2026 human send; CAW/Zorgbedrijf deepen next.
- Next: prio5 **rq_203**; deferred **rq_116** SWA.

### 2026-07-28T19:45:00Z - tick 209
- Unit: **rq_203** (FOI-adjacent hole-fill - **CAW Antwerpen** social L5)
- Found (strong ebesluit primary):
  - **CAW Kwadraat 2026 EUR 1.280m** (risk youth 9-21); max **7.691m** 2026-2031; split safety/education/health/stadsmarinier.
  - **CAW Parkours 2026 EUR 993.3k** / **2027 996.3k** (homeless youth 18-25 shelter); 2y sum **1.990m**.
  - CAW sample sum **2.273m** 2026 (+ FreeClinic 0.97m social third-party class ~3.25m).
- Wrote: sources 2; budgets 5; cmt 3; lb 3; rq_203=done; seeded **rq_204**.
- FOI: residual CAW lines + Zorgbedrijf full package + Mons BI2026 + culture partners human send.
- Next: **tick 210 progress coverage % + waste top10** then prio5 **rq_204**; deferred **rq_116** SWA.

### 2026-07-28T20:05:00Z - tick 210 – progress coverage % + waste top10
- Unit: **progress@210** (mandatory every-10-ticks refresh; no new research unit)
- Coverage (order-of-magnitude vs ?347.956 bn TE):
  - **A L0 / B L1:** 100% / 100% (unchanged strong)
  - **C L2:** **~70–78%** (up from ~68–76% @200) – Fedasil 929m, MDK GIP, PZA 321m, Enabel
  - **D L5:** **~8–15%** still thin structural – Antwerp culture sample 7.4m, CAW 2.3m, FreeClinic 0.97m
  - **E FOI ready:** **~71** (total FOI rows ~75)
- Inventory: budgets ~2227 ? commitments ~369 ? leaderboard ~337 ? entities ~138 ? sources ~433
- Waste top10: taxex/FFS/cheque still dominate (cheque ~8.83 ? gas product ~7.98 class); new city L5 not pure-waste top
- Wrote: `progress_every_10_ticks.md`, `doge_waste_top10_current.md`, loop_state, loop_log
- Next: prio5 **rq_204** (Zorgbedrijf/Mons/Digipolis hole-fill); deferred **rq_116** SWA

### 2026-07-28T20:25:00Z - tick 211
- Unit: **rq_204** (FOI-adjacent hole-fill - **Brandweerzone Antwerpen** city toelage)
- Found (strong ebesluit Toelagen 2025):
  - **City package locked EUR 81.535m**: werking **76.438m** + respons **3.343m** + invest **1.753m**.
  - Algemene werking **76.325m** after index (**3.44m**) + cyber (**0.17m**) withhold; MJP werk envelope **83.393m**.
  - Multi-commune zone: **Antwerpen + Wijnegem + Zwijndrecht**.
  - Dual safety stack with **PZA 320.7m 2026** ? city safety transfers class **~402m** (mixed years).
- Wrote: sources 1; entity 1; budgets 7; cmt 2; lb 2; rq_204=done; seeded **rq_205**.
- FOI: 2026 BZA package + federal fire base residual; Zorgbedrijf 2026 full; Mons BI2026 residual.
- Next: prio5 **rq_205**; deferred **rq_116** SWA.

### 2026-07-28T20:45:00Z - tick 212
- Unit: **rq_205** (FOI-adjacent hole-fill - **Zorgbedrijf Antwerpen** city toelage 2025)
- Found (strong ebesluit main Dec2024 + AMJP9 delta Dec2025):
  - **Package class EUR 65.0m 2025**: main **64.373m** (werk **29.029** + respons **22.350** + invest **12.994**) + delta **0.627m**.
  - Algemene werking **29.024m** after index withhold then **+419k** index release; invest **13.0–13.2m**.
  - Vs **2024 package 66.2m** (prior tick140) – slight decline on general werk, higher respons.
  - Dual stack with **PZA 321m** + **BZA 81.5m** ? care+safety city transfers class **~467m** (mixed years).
- Wrote: sources 2; entity 1; budgets 8; cmt 2; lb 2; rq_205=done; seeded **rq_206**.
- FOI: 2026 ZBA package + social-PC side lines + Mons BI2026 residual human send.
- Next: prio5 **rq_206**; deferred **rq_116** SWA.

### 2026-07-28T21:05:00Z - tick 213
- Unit: **rq_206** (FOI-adjacent hole-fill - **AG Digipolis Antwerpen** city + PZA IT packages)
- Found (strong ebesluit multi-decision):
  - **City 2025 package class EUR 75.201m**: main **54.467m** (werk **46.346** + invest pers **8.121**) + spilindex **1.340m** + cyber **19.395m**.
  - **City 2024 regular EUR 57.585m** (werk 44.913 + invest 12.673 cyber1.0/LCM/pers).
  - **PZA Digipolis 2025 EUR 53.528m** (invest 33.878 + werk 19.649 after +0.435m).
  - Dual city+PZA Digipolis class **~128.7m** 2025 (PZA Digipolis is zone spend; double-count caution vs PZA toelage 321m).
  - **2026 city regular locked 38.814m** (werk 37.750 + cam invest 1.064); **personnel residual** vs prior-year structure.
- Wrote: sources 7; entity 1; budgets 15; cmt 3; lb 3; rq_206=done; seeded **rq_207**; gap_antwerp note.
- FOI: Digipolis 2026 full personnel + group-member shares (ZBA/SO/Vespa) + Mons BI2026 residual human send.
- Next: prio5 **rq_207**; deferred **rq_116** SWA.

### 2026-07-28T21:25:00Z - tick 214
- Unit: **rq_207** (FOI-adjacent hole-fill - **Zorgbedrijf Antwerpen** city toelage 2026)
- Found (strong ebesluit 2026_CBS_00260 college 16 Jan 2026):
  - **Package locked EUR 89.288m**: werk **48.811m** + respons **25.977m** + invest **14.500m**.
  - MJP werk envelope **49.412m** before index withhold **0.601m** (package class if released **89.889m**).
  - Werk split: Sociale vrede pers **17.239m** + Art60 **5.289m** + service flats **11.058m** + dienstencentra **8.996m** + extramuraal **4.662m** + jeugdzorg **1.567m**.
  - Vs **2025 package 65.0m** – jump **+24.3m** (+37%); structure shift (personnel surplus + discounts explicit).
  - Dual stack with **PZA 320.7m** + **BZA 81.5m** ? care+safety class **~491.5m** (mixed years).
  - Side Finance-PC and other business-unit toelagen via separate decisions (residual FOI).
- Wrote: sources 1; budgets 13; cmt 2; lb 2; entity note; foi note; rq_207=done; seeded **rq_208**.
- FOI: ZBA side-PC residual + Digipolis 2026 personnel + Mons BI2026 + culture register human send.
- Next: prio5 **rq_208**; deferred **rq_116** SWA.

### 2026-07-28T21:45:00Z - tick 215
- Unit: **rq_208** (FOI-adjacent hole-fill - **Brandweerzone Antwerpen** city toelage 2026)
- Found (strong ebesluit 2026_CBS_01117 college 13 Feb 2026):
  - **Package locked EUR 87.459m**: werk **80.885m** + respons **3.400m** + invest **3.174m**.
  - MJP werk envelope **82.799m** before index withhold **1.914m** (package class if released **89.372m**).
  - Vs **2025 locked 81.535m** – jump **+5.9m**; invest 3.17 vs 1.75; communes Antwerpen+Wijnegem 2026-31.
  - **Same-year safety stack 2026**: PZA **320.677m** + BZA **87.459m** = **408.135m**.
  - **Same-year care+safety**: ZBA **89.288** + PZA **320.677** + BZA **87.459** = **497.424m**.
  - Side Finance-PC toelagen via separate decisions residual FOI.
- Wrote: sources 1; budgets 8; cmt 3; lb 3; entity/foi notes; rq_208=done; seeded **rq_209**.
- FOI: BZA side-PC + Digipolis 2026 personnel + Mons BI2026 + AG SO/VESPA/MPA/CIA packages next public fill.
- Next: prio5 **rq_209**; deferred **rq_116** SWA.

### 2026-07-28T22:05:00Z - tick 216
- Unit: **rq_209** (FOI-adjacent hole-fill - **AG Stedelijk Onderwijs** + secondary **MPA**)
- Found (strong ebesluit college 13 Feb 2026):
  - **AG SO package locked EUR 88.152m**: werk **52.887m** (alg 52.717 + VIA 0.170) + respons **7.151m** + invest **28.114m** (alg 27.939 + Santiagostraat 0.175).
  - MJP alg werk **53.497m** before index withhold **0.780m** (package class if released **88.932m**).
  - **MPA package locked EUR 4.054m**: parkeer **3.125m** + LEZ **0.929m** (MJP 4.130 - index 0.076); capital increases residual FOI.
  - **Mega AGB/zone stack same-year 2026**: ZBA 89.3 + PZA 320.7 + BZA 87.5 + AGSO 88.2 + MPA 4.1 = **~589.6m**.
- Wrote: sources 2; budgets 12; cmt 3; lb 3; entities 2; foi note; rq_209=done; seeded **rq_210**.
- FOI: AG SO side-PC + MPA capital + VESPA/CIA/Energie + Digipolis personnel + Mons BI2026 human send.
- Next: prio5 **rq_210**; deferred **rq_116** SWA.

### 2026-07-28T22:25:00Z - tick 217
- Unit: **rq_210** (FOI-adjacent hole-fill - **AG VESPA + CIA/Erfgoed + Energiebesparingsfonds** 2026)
- Found (strong ebesluit college 13 Feb 2026 batch):
  - **VESPA package locked EUR 6.011m**: werk **3.469m** (project 2.589 + housing lines 0.88) + invest **2.543m**; register 0.1m not locked.
  - **CIA/Erfgoed package locked EUR 7.935m**: musea **6.507m** + Geletterde Stad **1.422m** + cyber invest **6.1k**.
  - **Energiebesparingsfonds locked EUR 0.592m** (MJP 0.607 - index 0.016).
  - Feb batch sum **14.538m**; mega AGB/zone stack refresh **~604.2m** (prior 589.6 + 14.5).
- Wrote: sources 3; budgets 11; cmt 3; lb 4; entities 3; foi note; rq_210=done; seeded **rq_211**.
- FOI: Integratie/Beschut Wonen next; Digipolis 2026 personnel + Mons BI2026 residual human send.
- Next: prio5 **rq_211**; deferred **rq_116** SWA.

### 2026-07-28T22:45:00Z - tick 218
- Unit: **rq_211** (FOI-adjacent hole-fill - **Integratie en Inburgering** + **Beschut Wonen** 2026)
- Found (strong ebesluit college 13 Feb 2026):
  - **Integratie package locked EUR 25.826m**: werk **24.733m** (alg 24.426 + werving 0.307) + invest **1.093m** (alg 1.076 + cyber 0.017).
  - MJP alg werk 24.627m; withholds index 0.078 + Borsbeek VL 9.4k + gender payroll 0.114m not locked.
  - **Beschut Wonen locked EUR 0.970m**: psych **0.652m** + risicopersonen **0.164m** + dakloosheid preventie **0.154m**.
  - Social/integration batch **26.796m**; mega stack refresh **~631.0m** (prior 604 + 26.8).
- Wrote: sources 2; budgets 12; cmt 2; lb 3; entities 2; foi note; rq_211=done; seeded **rq_212**.
- FOI: dual VL Integratie residual + Digipolis 2026 personnel + Mons BI2026 human send.
- Next: prio5 **rq_212**; deferred **rq_116** SWA.

### 2026-07-28T23:05:00Z - tick 219
- Unit: **rq_212** (FOI-adjacent hole-fill - culture/youth/work L5 ebesluit)
- Found (strong ebesluit college 16 Jan 2026):
  - **FAMEUS 2026 EUR 523k** (culture 495k + youth 28k); 6y max **1.594m** 2026-2031.
  - **Youth**: Wereld van Rayaan **100k** 2026; YWCA Girls In The City **150k** 2026 (max 457k 2026-28).
  - **STW package EUR 280k**: Techniekbad+ **90k** + Spoorzoeker **190k** (dual VDAB/Mtech).
  - **Rataplan invest EUR 600k** building retrofit (agreement 2025-28; budgetperiode 2026).
  - Culture L5 sample **8 houses EUR 7.922m** of ~35m envelope class (prior 7.40 + FAMEUS).
  - Digipolis 2026 personnel + Mons BI2026 still residual public search negative this tick.
- Wrote: sources 4; budgets 11; cmt 5; lb 4; foi note; rq_212=done; seeded **rq_213**.
- FOI: residual culture partners + Digipolis personnel + Mons BI2026 human send.
- Next: prio5 **rq_213**; **tick 220 progress coverage % + waste top10**; deferred **rq_116** SWA.

### 2026-07-28T23:20:00Z - tick 220 – progress coverage % + waste top10
- Unit: **progress@220** (mandatory every-10-ticks refresh; no new research unit)
- Coverage (order-of-magnitude vs ?347.956 bn TE):
  - **A L0 / B L1:** 100% / 100% (unchanged strong)
  - **C L2:** **~72–80%** (up from ~70–78% @210) – Antwerp mega AGB/zone stack **~631m** same-year 2026 (PZA+ZBA+AGSO+BZA+Integratie+…)
  - **D L5:** **~8–16%** still thin structural – culture sample **7.92m** (8 houses), CAW 2.3m, FreeClinic 0.97m, FAMEUS/STW/Rataplan
  - **E FOI ready:** **~71** (total FOI rows ~75)
- Inventory: budgets ~2324 ? commitments ~394 ? leaderboard ~363 ? entities ~148 ? sources ~456
- Waste top10: taxex/FFS/cheque still dominate (cheque ~8.83 ? company cars FPB ~8.5); new city AGB L2 not pure-waste top
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log
- Next: prio5 **rq_213** (Digipolis/Mons/remaining L5); deferred **rq_116** SWA

### 2026-07-28T23:35:00Z - tick 221
- Unit: **rq_213** (FOI-adjacent hole-fill - culture/youth L5 ebesluit)
- Found (strong ebesluit):
  - **MORPHO 2026 EUR 287.5k**; 6y max **1.767m** 2026-2031 (artist ateliers dual VL residual).
  - **Tutti Fratelli 2026 EUR 143.4k** (culture 98.4 + youth 45); 6y max **0.742m**.
  - **2020 Studios EUR 100k** youth citizenship Apr2026-Mar2027.
  - **VDAB werfkeet Jobs Grote Verbinding EUR 12.9k** 2026 (indexed rent via Vespa).
  - Culture L5 sample **10 houses EUR 8.353m** of ~35m envelope (~24% class); residual ~6 of 16 partners.
  - Digipolis personnel + Mons BI2026 still residual public search.
- Wrote: sources 4; budgets 7; cmt 4; lb 3; foi note; rq_213=done; seeded **rq_214**.
- FOI: residual culture partners DeRoma/Trix/paleis/AMUZ + Digipolis + Mons human send.
- Next: prio5 **rq_214**; deferred **rq_116** SWA.

### 2026-07-28T23:55:00Z - tick 222
- Unit: **rq_214** (FOI-adjacent hole-fill - **AMUZ** + Cultuurweken L5)
- Found (strong ebesluit college 10 Apr 2026):
  - **AMUZ 2026 EUR 927k**: exploitatie **752k** + invest gebouwen **175k**; 6y max **4.862m**; invest plan 350k 2026-27.
  - Dual VL Kunstendecreet residual; Laus Polyphoniae festival; on 16-partner culture list.
  - **Cultuurweken summer package EUR 24.8k**: Creatief Schrijven 1.8k + das Kunst 19.2k + JEF extra 3.8k.
  - Culture L5 sample **11 houses EUR 9.280m** of ~35m envelope (~27% class); residual ~5 partners (DeRoma Trix paleis DeStudio AAW).
  - Digipolis personnel + Mons BI2026 still residual public search.
- Wrote: sources 2; budgets 6; cmt 3; lb 2; foi note; rq_214=done; seeded **rq_215**.
- FOI: residual culture partners + Digipolis + Mons human send.
- Next: prio5 **rq_215**; deferred **rq_116** SWA.

### 2026-07-29T00:15:00Z - tick 223
- Unit: **rq_215** (FOI-adjacent hole-fill - **HETPALEIS** + Rataplan werk + Koraal)
- Found (strong ebesluit):
  - **HETPALEIS 2026 EUR 3.412m**: exp **2.922m** + invest **0.490m**; 6y max **18.938m**; invest plan 0.98m 2026-27.
  - **Rataplan werk EUR 278.5k** 2026 (culture 193.5 + buurt 85); 3y sum 674.8k (invest 600k prior separate).
  - **Koraal youth EUR 655k** college lock (of 662k afsprakennota; 7k Vast Bureau residual).
  - Culture L5 sample **12 houses EUR 12.692m** of ~35m envelope (~36% class); residual ~4 partners (DeRoma Trix DeStudio AAW).
- Wrote: sources 3; budgets 6; cmt 4; lb 3; foi note; rq_215=done; seeded **rq_216**.
- FOI: residual culture partners + Digipolis + Mons human send.
- Next: prio5 **rq_216**; deferred **rq_116** SWA.

### 2026-07-29T00:35:00Z - tick 224
- Unit: **rq_216** (FOI-adjacent hole-fill - residual culture **DeRoma + Trix + DeStudio + Antwerp Art**)
- Found (strong primary):
  - **De Roma** MJP 2026 **EUR 936k** culture; 6y path **5.752m**; college vastlegging Jun2026 **Verdaagd** (MJP still budgeted).
  - **Trix (Trx vzw)** 2026 **EUR 705k** (culture 355 + youth 350); 6y class **~4.367m**.
  - **De Studio** ebesluit college 19 Dec 2025 **EUR 153k** 2026; max **940.188k** 2026-31 (OO cash-by-year = MJP).
  - **Antwerp Art** MJP 2026 **EUR 97.5k**; 6y **599.1k**.
  - Culture L5 sample **16/16 houses complete EUR 14.584m** of ~35m envelope (**~41.7%** class).
- Wrote: sources 2; budgets 7; cmt 5; lb 5; foi note; rq_216=done; seeded **rq_217**.
- FOI: Digipolis 2026 personnel + Mons BI2026 + dual VL residual + Gent-style register human send.
- Next: prio5 **rq_217**; deferred **rq_116** SWA.

### 2026-07-29T00:55:00Z - tick 225
- Unit: **rq_217** (FOI-adjacent hole-fill - **AG Digipolis MJP 2026 personnel residual**)
- Found (strong Digipolis MJP 2026-2031 ebesluit PDF):
  - **AG Digipolis total uitgaven 2026 EUR 245.610m** (exp **244.879m** + invest **0.731m**).
  - **Personnel residual closed: EUR 45.458m** 2026 (contract 43.715 + vast 0.152 + other 1.591); path to **52.749m** 2031.
  - Goederen/diensten **198.878m**; debt stock **15.063m**; city treasury advance **22m** 2026 (from 25m 2025).
  - VTE max kader 329; internalisation savings path **7.3m** legislatuur (claim in MJP).
  - Note: city ebesluit lock **38.8m** is city-share only; AGB 245.6m is multi-member cost-sharing (not pure additive city opex).
  - Mons BI2026 public PDF still not found this tick (FOI remains ready).
- Wrote: sources 1; budgets 7; cmt 2; lb 2; entity note; foi note; rq_217=done; seeded **rq_218**.
- FOI: Digipolis member-share matrix + Mons BI2026 + dual VL + register human send.
- Next: prio5 **rq_218**; deferred **rq_116** SWA.

### 2026-07-29T01:15:00Z - tick 226
- Unit: **rq_218** (FOI-adjacent hole-fill - **Digipolis member-share omzet matrix**)
- Found (strong markup annex ebesluit PDF):
  - **Member omzet sum 2026 EUR 245.070m** (2025: 221.900m); markup **4.14%** (from 4.29%).
  - **Stad 138.021m** | **LPA/PZA 69.468m** | AGSO 11.084m | MPA 9.457m | HVZ 6.994m | ZBA 4.467m | VESPA 3.603m | INTI 1.210m | OVE 0.403m | CIA 0.363m.
  - Closes Digipolis member-share residual; aligns with AGB total 245.6m (recharges fund AGB).
  - Note: stad omzet 138m ≠ city ebesluit partial lock 38.8m (subset/timing); not double-count AGB as pure city opex.
  - Mons BI2026 still not public this tick (FOI ready).
- Wrote: sources 1; budgets 13; cmt 1; lb 3; foi note; rq_218=done; seeded **rq_219**.
- FOI: project L5 within Digipolis + Mons BI2026 + dual VL + register human send.
- Next: prio5 **rq_219**; deferred **rq_116** SWA.

### 2026-07-29T01:35:00Z - tick 227
- Unit: **rq_219** (FOI-adjacent hole-fill - **Antwerp social L5 MJP full CAW + ADIC + FreeClinic + VAGGA**)
- Found (strong MJP nominatief):
  - **CAW Antwerpen full package 2026 EUR 16.916m**: sociale **12.684m** + veiligheid **3.430m** + onderwijs **0.520m** + samenleving **0.171m** + gezondheid **0.110m** (prior ebesluit Kwadraat+Parkours 2.27m is subset).
  - **Free Clinic MJP EUR 2.436m** (broader than drug ebesluit subset 0.974m).
  - **VAGGA EUR 0.945m** (sociale 0.837 + SE 0.032 + veil 0.076).
  - **ADIC EUR 0.735m** 2026 (path to 0.812m 2031).
  - Social L5 sample **4 orgs EUR 21.013m** 2026.
  - Residual large youth: JES ~2.39m, Kras ~4.26m, Elegast ~1.28m (next tick); Mons BI2026 still FOI.
- Wrote: sources 1; budgets 11; cmt 5; lb 5; foi note; rq_219=done; seeded **rq_220**.
- FOI: CAW project L5 inside 12.7m + Mons BI2026 + dual VL + register human send.
- Next: prio5 **rq_220**; deferred **rq_116** SWA.

### 2026-07-29T01:55:00Z - tick 228
- Unit: **rq_220** (FOI-adjacent hole-fill - **JES + Kras + Elegast + Posthof** youth/social MJP)
- Found (strong MJP nominatief):
  - **Kras Jeugdwerk 2026 EUR 4.260m** (jeugd 3.95 + sport 0.27 + veil 40k).
  - **JES 2026 EUR 2.386m** (jeugd 2.35 + veil 36.4k).
  - **Elegast 2026 EUR 1.278m** (veil 0.533 + onderw 0.41 + sam 0.28 + digi 55k).
  - **Buurtwerk Posthof 2026 EUR 1.274m** (digi 0.909 spike + sam 0.28 + SE 85k).
  - Youth/social sample **4 orgs EUR 9.199m**; combined with tick227 social **8 orgs ~EUR 30.23m**.
  - Mons BI2026 still not public (FOI ready).
- Wrote: sources 1; budgets 8; cmt 5; lb 5; foi note; rq_220=done; seeded **rq_221**.
- FOI: register project L5 + Mons BI2026 + dual VL human send.
- Next: prio5 **rq_221**; **tick 230 progress coverage** due; deferred **rq_116** SWA.

### 2026-07-29T02:15:00Z - tick 229
- Unit: **rq_221** (FOI-adjacent hole-fill - residual social/equality **BAZZZ Axi BattleDroids ATK VVS Unik GAMS**)
- Found (strong MJP nominatief):
  - **BAZZZ EUR 405k** (jeugd 315 + gelijke 90).
  - **VVS EUR 400k** gezondheid; **Axi EUR 155k**; **Battle Droids EUR 163k**.
  - **Armen Te Kort EUR 262.7k**; **Buurthuis Unik EUR 120k**; **GAMS EUR 50.6k**.
  - Residual sample **7 orgs EUR 1.556m**; combined social+youth class **~EUR 31.79m** (~15 orgs with prior).
  - Mons BI2026 still not public (FOI ready).
- Wrote: sources 1; budgets 9; cmt 6; lb 3; foi note; rq_221=done; seeded **rq_222**.
- FOI: register + Mons BI2026 + dual VL human send.
- Next: **tick 230 mandatory progress coverage % + waste top10**; then prio5 **rq_222**; deferred **rq_116** SWA.

### 2026-07-29T02:30:00Z - tick 230 - progress coverage % + waste top10
- Unit: **progress@230** (mandatory every-10-ticks refresh; no new research unit)
- Coverage (order-of-magnitude vs EUR 347.956 bn TE):
  - **A L0 / B L1:** 100% / 100% (unchanged strong)
  - **C L2:** **~74-82%** (up from ~72-80% @220) - Digipolis AGB **245.6m** + member matrix **245.07m** + prior AGB stack ~631m class
  - **D L5:** **~9-17%** still thin structural - culture **16/16 complete 14.58m**; social+youth **~15 orgs ~31.8m** (CAW full 16.92m + Kras/JES/...)
  - **E FOI ready:** **~71** (total FOI rows ~75)
- Inventory: budgets ~2400; commitments ~429; leaderboard ~394; entities ~309; sources ~489
- Waste top10: taxex/FFS/cheque still dominate (cheque ~8.83; company cars FPB ~8.5); Antwerp city L5 is core-service depth not pure-waste top
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log
- Next: prio5 **rq_222** (Mons/utilities); deferred **rq_116** SWA

### 2026-07-29T02:50:00Z - tick 231
- Unit: **rq_222** (FOI-adjacent hole-fill - **Mons CPAS BI2026 + Zone Secours**)
- Found (strong deliberations.be primary):
  - **CPAS Mons 2026 global EUR 149.389m** (ord dep **149.131m** / rec **149.152m** boni 21k; extra global **7.306m**).
  - **City intervention CPAS EUR 27.918m** (fonct 25.141 + responsabilisation 2.501 + PCS 0.276).
  - **Zone Secours Hainaut-Centre EUR 2.604m** (vs provisional BI 2.816m; MB1 adjustment).
  - Housing NPG medium: 84 logements renovation **2.68m** UREBA/PIVW; Art.60 posts 260→380 / Art.61 70→140.
  - Full **Ville de Mons BI2026 PDF** still not published on mons.be budgets page (only 2025 comptes) — FOI residual ASBL L5.
- Wrote: sources 2; budgets 9; cmt 2; lb 3; entity; foi notes; rq_222=done; seeded **rq_223**.
- FOI: full Ville BI2026 + ASBL top20 still ready human send.
- Next: prio5 **rq_223**; deferred **rq_116** SWA.

### 2026-07-29T03:15:00Z - tick 232
- Unit: **rq_223** (FOI-adjacent hole-fill - **IDEA + HYGEA Mons utilities**)
- Found (strong primary):
  - **IDEA 2025:** bilan **EUR 441.286m**; equity **279.296m**; personnel **38.099m**; result **13.268m**; dividends **11.392m**; fin products **16.398m**.
  - **IDEA 2026 path:** responsabilisation pension **3.951m** (6y **25.843m** hors bilan); DDT1+2 distributions **23.285m**; div exceptionnel III.C **20m** to communes.
  - **HYGEA Mons waste 2026 EUR 7.760m** (dep 7.314 + appel lissage 0.446; cotis infra 0.167; recettes sacs 2.173).
  - Full **Ville Mons BI2026 PDF** still not on mons.be — FOI residual ASBL L5 + Mons share of IDEA dividends.
- Wrote: sources 3; budgets 13; cmt 2; lb 3; entities 2; foi note; rq_223=done; seeded **rq_224**.
- FOI: Ville BI2026 + ASBL top20 + IDEA per-commune DDT/div still ready human send.
- Next: prio5 **rq_224**; deferred **rq_116** SWA.

### 2026-07-29T03:40:00Z - tick 233
- Unit: **rq_224** (FOI-adjacent hole-fill - **Mons Ville budget 2026 MB1 totals**)
- Found (strong deliberations 23 Jun 2026 1er amendement; vote recorded):
  - **Ordinaire dep propre EUR 241.834m** / rec **242.204m** (boni 0.370m); global dep **243.264m**.
  - **Extraordinaire dep propre EUR 63.198m** / rec **60.823m**; global dep **163.012m** (incl. prior years).
  - **Same-year cash-propre class EUR 305.032m** (ord+extra dep propre).
  - Dotations: **Zone Police 27.335m**; CPAS tutelle **26.945m**; Zone Secours **2.604m**; fabriques cath **1.014m** + prot **59k**; budget participatif **108k**.
  - Residual: machine-readable **ASBL third-party L5** annex still FOI (totals gap largely closed).
- Wrote: sources 1; budgets 11; cmt 1; lb 3; foi note; rq_224=done; seeded **rq_225**.
- FOI: ASBL top20 L5 still ready human send.
- Next: prio5 **rq_225**; deferred **rq_116** SWA.

### 2026-07-29T04:05:00Z - tick 234
- Unit: **rq_225** (FOI-adjacent hole-fill - **COCOM / GGC budget 2026 CoA primary**)
- Found (strong Cour des comptes report 6 May 2026, 27pp PDF):
  - **SCR recettes EUR 1,978.869m**; **dep eng 2,027.747m** / **liq 2,040.467m**; solde **−61.6m**.
  - **SEC solde after sous-util 64.7m: −35.0m** (path 0 by 2029: −35/−23/−11/0).
  - **Iriscare OAA EUR 1,826.390m** balanced: Menages **1,099.2m** (AF **1,081.4m**); Soins **477.8m** (MR forfaits **353.7m**, 11,600 beds); Aide **102.1m** (AAPA 37.6m).
  - **New Samusocial EUR 71.925m** (+72% vs 41.8m): multi-fund BCR +14.8 / Fedasil +9.3 / COCOM +3.6; SCR dot **27.4m**.
  - **Bruss'Help EUR 3.324m** (+59%); CoA: below 7m CFP threshold should be excluded.
  - Mission 05 Iriscare dots liq **1,627.6m** (Sante 469.6 + Familles 1,057.8 class).
  - HRF net primary cap **2.29% 2026** / avg **2.73% 2025-31**; CoA notes exposé omits net-primary series.
  - **Opacity (CoA-flagged):** comptes generaux COCOM 2019-24 never transmitted; New Samusocial/Bruss'Help accounts 2020-24 never approved/sent; no justificatory fiches Iriscare/Samusocial/Bruss'Help.
- Wrote: sources 1; entities 4; budgets 25; cmt 3; lb 4; FOI draft gap_cocom_oaa_accounts **ready**; raw PDF; rq_225=done; seeded **rq_226**.
- FOI: gap_cocom_oaa_accounts ready human send (accounts + L5); prior Mons ASBL residual still ready.
- Next: prio5 **rq_226** (COCOF/VGC dual or other); deferred **rq_116** SWA.

### 2026-07-29T04:35:00Z - tick 235
- Unit: **rq_226** (FOI-adjacent hole-fill - **COCOF 2026 + VGC 2025 dual to COCOM**)
- Found (strong primary):
  - **COCOF CoA BI2026 (31 Mar 2026):** decret rec **625.624m** / dep eng **667.610m** / liq **677.505m**; reglement rec **16.112m** / liq **24.305m**; **combined liq ~701.8m**.
  - **SEC solde −22.708m** after sous-util **35.758m** (path 0 by 2029: −22.7/−15/−7.5/0).
  - Missions liq: **Phare 210.270m** (~31.5%); Aide 113.9m; Formation 91.8m (BF dot **63.2m**); Admin 58.4m; Sante 57.0m; Enseignement 51.7m.
  - **Bruxelles Formation OAA 96.2m** balanced; debt path **182.7→203.7m** EOY25-26 (SPABS soudure 180.3m).
  - HRF net primary cap **2.88% 2026** / avg **2.97%**; CoA: expose omits net-primary series.
  - **VGC Jaarrekening 2025 (strong):** exp uit **173.628m** / ont **224.963m** / saldo **51.335m**; op ont **219.4m** (BCR dots 96.8 + VL 50.8 + fed 23.4); **werksubs 53.883m**; personeel **89.016m**; inv uit **99.527m**; debt **~242.1m**; AFM **41.819m**.
  - Dual stack map: COCOM SCR 2.04bn + COCOF 0.70bn + VGC exp 0.17bn class (**do not sum** — inter-dotations).
- Wrote: sources 2; entities 4; budgets 28; cmt 3; lb 4; FOI draft gap_cocof_phare_vgc_l5 **ready**; raw PDFs; rq_226=done; seeded **rq_227**.
- FOI: Phare named L5 + VGC top20 werksubs + COCOF net primary human send.
- Next: prio5 **rq_227**; deferred **rq_116** SWA.

### 2026-07-29T05:05:00Z - tick 236
- Unit: **rq_227** (FOI-adjacent hole-fill - **VAPH dual Phare + VSB + Opgroeien 2026**)
- Found (strong Vlaamse uitgavenbegroting decree 2026 primary / Themis PDF):
  - **VAPH IVA:** ontvangsten **EUR 2,865.400m** = VEK **2,865.400m**; VAK **3,151.217m** (art.37).
  - Programme **GG Personen met een beperking** VAK **3,121.780m** / VEK **2,819.590m** (kEUR table).
  - **Dual Phare COCOF 210.3m** — VAPH VEK ~**14x** Phare (not unit-cost adjusted; dual AViQ residual).
  - **VSB IVA:** rec=VEK **4,748.450m**; VAK **4,381.513m** (art.35) — care WZC open-end class.
  - **Opgroeien regie IVA:** rec=VEK **7,611.411m**; VAK **7,578.928m** (art.36) — Groeipakket open-end.
  - Triple WVG IVA VEK class **~15.225bn** (do not double-count with WVG programme lines).
- Wrote: sources 1; entities 3; budgets 12; cmt 3; lb 4; FOI gap_vaph_pvb_l5 **ready**; raw PDF; rq_227=done; seeded **rq_228**.
- FOI: VAPH PVB top operators L5 + underbenutting path human send.
- Next: prio5 **rq_228** (AViQ dual); deferred **rq_116** SWA; progress@240 due in 4 ticks.

### 2026-07-29T05:35:00Z - tick 237
- Unit: **rq_228** (FOI-adjacent hole-fill - **AViQ dual VAPH from EPCO 17.093 + PQ annex**)
- Found (strong primary):
  - **Pure AViQ regional dots 2026 CL ~EUR 6,810.8m** (CE current+cap class ~6,785.0m): fonct **88.5m**; paritaires **1,749.6m**; reglementees **1,849.0m**; **AF 3,008.5m**; caisses AF **41.4m**; fac sante/handicap/communes/EU ~41.0m; capital CL ~33.0m.
  - Prog **17.093 total CE 7,026.6m / CL 7,062.5m** (includes federal hospital 179.6m, Famiwal 36.4m, CRAC, Wallonie Sante — not pure AViQ).
  - **Inexecution annex:** 2023 **389.9m (5.73%)** → implied budget **~6.80bn**; 2024 **316.8m (4.43%)** → **~7.15bn**; recurring corrected **219m / 202m**.
  - Branch liquidation rates 2024: protection 94.21%; sante 92.76%; **handicap 97.46%**; familles 98.46%; gestion 90.11%.
  - Treasury refund to Region: **335.3m 2025** / **230m 2026**.
  - Dual: VAPH disability **2.87bn** vs AViQ multi-branch **~6.81bn** vs Phare **0.21bn** (do not sum; handicap split inside AViQ residual FOI).
- Wrote: sources 2; entity 1; budgets 16; cmt 1; lb 4; FOI gap_aviq_branch_l5 **ready**; raw epco; rq_228=done; seeded **rq_229**.
- FOI: branch split + operator L5 human send.
- Next: prio5 **rq_229**; progress@240 in 3 ticks; deferred **rq_116** SWA.

### 2026-07-29T06:05:00Z - tick 238
- Unit: **rq_229** (FOI-adjacent hole-fill - **Famiwal + private AF caisses dual channel**)
- Found (strong EPCO UAP tables BI2026):
  - **FAMIWAL (public):** total **EUR 1,118.794m**; prestations **1,080.918m**; fonctionnement **36.976m** (RW dot **36.359m**); personnel package **28.123m**.
  - **Parentia:** prest **992.756m** (largest private ~33%); fonct **24.175m**; total dep **1,016.9m**.
  - **Camille:** prest **579.645m**; fonct **12.198m**; total **585.9m**.
  - **KidsLife:** prest **360.167m**; fonct ~**8.0m**; total **368.1m**.
  - **4-CAF prestations sum EUR 3,013.5m** — reconciles AViQ AF envelope **3,008.5m** (+ regulator path).
  - Admin dual: public Famiwal fonct ~**342 bps** of prest vs private blended ~**229 bps** class (rough; FOI unit-cost per dossier residual).
  - Dual map: WAL multi-caisse 3.01bn vs BRU Iriscare AF **1.08bn** (tick234); VL residual.
- Wrote: sources 1; entities 4; budgets 16; cmt 2; lb 4; FOI gap_wal_af_caf_unit_cost **ready**; rq_229=done; seeded **rq_230**.
- FOI: unit cost per dossier by CAF human send.
- Next: prio5 **rq_230**; **progress@240 in 2 ticks**; deferred **rq_116** SWA.

### 2026-07-29T06:35:00Z - tick 239
- Unit: **rq_230** (FOI-adjacent hole-fill - **VL Groeipakket dual AF**)
- Found (strong primary):
  - **Groeipakket 2025 awards ~EUR 4.7bn** via uitbetalingsactoren (Opgroeien official); **>1.6m children** / **930,010 families** eoy2025.
  - Sociale toeslag: **522,148 children** (dec2025, -3.4% y/y); zorgtoeslag: **51,261 children**.
  - **VUTG admin BO2026 EUR 42.565m** (BBT tech Q); ~**90 bps** of 4.7bn awards class.
  - Zorgtoeslagen budget **144.5m** 2026 (+3.4m); private UA efficiency cut **-1.5m**; recoveries raming **34.836m**; CGPA invest **2.5m**.
  - **BE AF triple map (do not sum years):** VL ~**4.7bn** (2025) | WAL 4-CAF **3.01bn** (2026) | BRU Iriscare AF **1.08bn** (2026).
- Wrote: sources 2; entity 1; budgets 7; cmt 2; lb 4; FOI gap_vl_groeipakket_bo2026_line **ready**; raw BBT PDF; rq_230=done; seeded **rq_231** (progress@240 prio6) + **rq_232**.
- FOI: exact GEF2QY BO line + unit costs human send.
- Next: **rq_231 progress@240 mandatory**; then rq_232; deferred **rq_116** SWA.

### 2026-07-29T07:00:00Z - tick 240 - progress coverage % + waste top10
- Unit: **progress@240** (mandatory every-10-ticks; **rq_231**)
- Coverage (order-of-magnitude vs EUR 347.956 bn TE):
  - **A L0 / B L1:** 100% / 100% (unchanged strong)
  - **C L2:** **~78-86%** (up from ~74-82% @230) — WVG IVAs VAPH 2.87 + VSB 4.75 + Opgroeien 7.61; AViQ 6.81; COCOM 2.04 + COCOF 0.70 + VGC 0.17; Mons Ville/CPAS; AF channels
  - **D L5:** **~10-18%** still thin — AF multi-caisse named + prior Antwerp culture/social; operator L5 FOI stack
  - **E FOI ready:** **~77** (total FOI rows ~81)
- Inventory: budgets ~2537; commitments ~448; leaderboard ~427; entities ~946; sources ~504
- Waste top10: **unchanged** taxex/FFS/cheque dominate (cheque 8.83; company cars FPB 8.5; heat oil 8.43); new L2 social is core duty not pure-waste top
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log; rq_231=done
- Next: prio5 **rq_232**; deferred **rq_116** SWA; human FOI send stack

### 2026-07-29T07:30:00Z - tick 241
- Unit: **rq_232** (FOI-adjacent hole-fill - **ONE FWB dual Opgroeien**)
- Found (strong FWB budget initial 2026 DO19 table eng=liq, kEUR):
  - **ONE programme 1 total EUR 760.837m** 2026 (was **711.833m** 2025; +49.0m).
  - Main dotation **604.028m**; informatique **35.318m** (-2.4m y/y); reform milieux **27.685m**; emploi enfance **49.435m**; accueillantes **20.817m**; places **5.014m**; politiques nouvelles **15.140m**.
  - DO19 Enfance total **760.977m** (ONE + politique accueil 0.14m).
  - Dual: VL **Opgroeien regie 7.61bn** (incl Groeipakket AF — different perimeter); press class ~750m/550m subsidies aligns.
- Wrote: sources 1; entity 1; budgets 10; cmt 1; lb 2; FOI gap_one_operator_l5 **ready**; rq_232=done; seeded **rq_233**.
- FOI: operator L5 + unit-cost dual Opgroeien human send.
- Next: prio5 **rq_233**; deferred **rq_116** SWA.

### 2026-07-29T08:00:00Z - tick 242
- Unit: **rq_233** (FOI-adjacent hole-fill - **FWB Aide a la Jeunesse DO17 dual VL**)
- Found (strong FWB budget DO17 table eng/liq kEUR):
  - **DO17 total eng EUR 470.531m / liq 470.617m** 2026 (2025: 466.2 / 467.0m).
  - Prog1 jeunes en danger/delinquants **464.865m**; prog0 subsistence ~5.7m.
  - **L5 named lines:** residentiels+projet educatif **264.094m** (~56%); accompagnement **63.112m**; AMO **41.338m**; accueil familial package **37.786m**; restauratrices **7.964m**; nouvelles politiques **8.229m**; **MENA plan 6.614m** (new); non-marchand **4.850m**; Maisons ado **2.999m**.
  - Named L5 sample sum **~510m class of overlapping lines** (core of DO17); dual VL jeugdhulp (Opgroeien + Justitie transfer 2026).
- Wrote: sources 1; entity 1; budgets 13; cmt 1; lb 3; FOI gap_fwb_aj_operator_l5 **ready**; rq_233=done; seeded **rq_234**.
- FOI: named operators inside 264m resid residual human send.
- Next: prio5 **rq_234**; deferred **rq_116** SWA.

### 2026-07-29T08:30:00Z — tick 243
- Unit: rq_234 (Maisons de Justice deepen + VL Justitiehuizen dual)
- Found (strong primary):
  - **FWB DO18 Maisons de Justice BI2026** (`fwb_budget_dep_2026.pdf`): **eng €28.362m / liq €30.124m** (2025 eng 28.700 / liq 30.276).
  - Split 2026: Prog0 subsistance 0.575/0.837m; **Prog1 surveillance électronique 3.433/4.958m** (aide détenus SE **3.203m**); **Prog3 partenariats eng 24.354 / liq 24.292m** (~81% eng); Prog4 0/0.037m.
  - Act31 agréés (eng): aide au lien **6.851m**, psy **5.668m**, sociale **4.180m**, accompagnement **3.792m**, communication **1.734m**, juridique **1.244m** (sum eng **23.469m**); projets particuliers **0.605m**; urgences **0.280m**.
  - Related infra DO15 act14 SAJ-SPJ+MDJ **10.595m** (shared; medium).
  - **VL dual receipt** BBT FB BO2026: Dotatie Justitiehuizen art. 47/10 BFW **BA2025 €88.767m → BO2026 €90.357m** (+1.590m). Receipt only — full AJH spend/top-up residual (beleidsnota: VL tops up).
  - Dual note: **not additive** (programme credits vs federal receipt; FWB personnel likely outside DO18).
- Wrote: sources (+2); entities fwb_maisons_justice + vl_justitiehuizen; budgets (+14); commitments (+2); leaderboard (+3); foi_queue ready gap_fwb_mdj_partner_l5 + gap_vl_justitiehuizen_spend; drafts; rq_234=done; spawn rq_235; loop_state ticks=243
- FOI opened: gap_fwb_mdj_partner_l5, gap_vl_justitiehuizen_spend (ready, human send)
- Next: rq_235 hole-fill; rq_116 SWA deferred Oct–Dec 2026

### 2026-07-29T09:00:00Z — tick 244
- Unit: **rq_235** (FOI-adjacent hole-fill — **VL AJH full spend** closes gap_vl_justitiehuizen_spend public side)
- Found (strong primary OP2026 + BBT BU2025):
  - **AJH Eindtotaal VAK 2026 EUR 240.015m** (uitgavendecreet 19 dec 2025; Ondernemingsplan AJH).
  - Lonen **164.868m** (reg 156.722 + VIN 0.120 + wet 18/07 8.026); werking **21.628m**.
  - JH+ET policy **7.022m** (huur ET 2.70 + leef 2.77 + tolk 0.205 + wet extras 1.347).
  - Justitieel beleid **4.190m**; herstelgerichte subs **15.907m**; jeugd WT **24.444m** + PR **9.750m**; CJB **1.165m**.
  - BU2025 SA AJH: VAK BA **100.549m** / VEK **102.608m**; lonen BA **83.098m**; plan **1.220,5 VTE**; eoy **1.171,8 VTE** / 1.281 heads; dossiers JH **39.100** new 2025.
  - Federal JH receipt still **90.357m** BO2026 — agency broader than JH (youth transfer drives 2026 jump).
  - Dual: FWB DO18 MDJ **30.1m** vs VL AJH **240m** vs receipt **90.4m** — **not additive** (perimeters differ; FWB personnel may be outside DO18; Fonds JH partners still federal Globaal Plan).
- Wrote: sources +2; entity vl_ajh + notes; budgets +25; cmt +2; lb +4; FOI gap_vl_justitiehuizen_spend narrowed + gap_vl_ajh_partner_l5 ready; drafts; rq_235=done; spawn rq_236; loop_state ticks=244
- FOI: partner L5 + JH FTE slice human send (not full agency total)
- Next: prio5 **rq_236**; deferred **rq_116** SWA

### 2026-07-29T09:30:00Z — tick 245
- Unit: **rq_236** (FOI-adjacent hole-fill — **FWB federal MDJ receipt dual VL** + DG residual FOI)
- Found (strong primary ExpGen BI2026 + CoA DG 2026):
  - **FWB LSF art.47/10 Dotation Maisons de justice:** 2025 INI **€54.5m** / AJU **€54.7m** / 2026 INI **€55.7m**.
  - Dual receipt same article: **FWB 55.7m vs VL BO2026 90.357m** (not additive with spend).
  - DO18 programme liq still **€30.124m** → wedge class **~€25.6m** outside DO18 (personnel DO11 + other; medium not audited identity).
  - DO11 traitements total **€437.6m**; new 2026 remun pack MDJ+AJ **€8.9m** (AGMJ+AGAJ **5.4m** combined + MDJ carceral reform **3.4m**); Brussels **12 ETP** retained; partner non-index **-449k** + training cuts.
  - **DG Justizhaus:** CoA UHH 2025+2026 **no euro line**; fed global dot 2026 **351.1m** (earmarked **17.0m**) — JH share unknown → FOI.
- Wrote: sources +2; entity dg_justizhaus + fwb_mdj notes; budgets +10; cmt +2; lb +3; FOI gap_fwb_mdj_personnel_total + gap_dg_justizhaus_budget ready; drafts; rq_236=done; spawn rq_237; ticks=245
- FOI: AGMJ wage stock + DG Justizhaus human send
- Next: prio5 **rq_237**; deferred **rq_116** SWA

### 2026-07-29T10:00:00Z — tick 246
- Unit: **rq_237** (FOI-adjacent hole-fill — **FWB Egalite des chances dual VL Gelijke Kansen**)
- Found (strong Exp. particulier depenses 2026 Coppieters DO11 table):
  - Package TOTAL **CE €14.494m / CL €7.850m** 2026 (2025: 12.742 / 9.548).
  - Named: violences femmes coll **CE 2.50 / CL 0.532m**; egalite initiatives **2.283 / 0.870**; droits femmes pluriann **4.624 / 1.474**; pauvrete ann **1.162** CL; interculturalite plur **1.004** CL.
  - Dual institutes: **Unia FWB 369k**; **IEFH protocol 59k**.
  - Dual VL: GK werkings **15.162m** (projectsubs **4.361m**) — different perimeter; do not sum.
  - AGMJ full wage bill still not in public DO18/ExpPart (FOI already open).
- Wrote: sources +1; entity fwb_egalite_chances; budgets +22; cmt +1; lb +4; FOI gap_fwb_egalite_l5 ready; draft; rq_237=done; spawn rq_238; ticks=246
- FOI: equality L5 operators human send
- Next: prio5 **rq_238**; deferred **rq_116** SWA

### 2026-07-29T10:30:00Z — tick 247
- Unit: **rq_238** (FOI-adjacent hole-fill — **FPS taxex / fossil energy subsidies inventory**)
- Found (strong primary climat.be 4e Inventaire federal energies fossiles 2025, Benchmark 1):
  - **Direct fossil subsidies 2022 EUR 13.268 bn** (2.4% GDP); path 11.68→13.27bn 2018-22.
  - **Accises** 10.536bn (main instrument); gaz product gaps **4.854bn**; mazout **1.857bn**; diesel pro **0.742bn** (was 1.221bn 2020); gaz taux reduit **1.295bn**.
  - **Fuel cards** IR **0.794bn**; permanent social transfers **0.757bn**; temporary crisis **1.176bn**.
  - **Air+marine** **0.976bn** (kero aviation **0.688bn**); VAT air tickets **0.180bn**.
  - **Company cars EHS** **3.434bn** 2022 (path 2.63→3.43); dual FPS/FPB methods.
  - Sectors: transport class **6.69bn**; industry **3.93bn**; buildings permanent **4.91bn**.
- Wrote: sources +1; entity fed_fossil_subs_inventory; budgets +26; cmt +1; lb +5; FOI gap_fed_fossil_subs_2023_24 ready; draft; raw PDF; rq_238=done; spawn rq_239; ticks=247
- FOI: 2023-24 consol series human send
- Next: prio5 **rq_239**; **progress@250 in 3 ticks**; deferred **rq_116** SWA

### 2026-07-29T11:00:00Z — tick 248
- Unit: **rq_239** (FOI-adjacent hole-fill — **Wallonie egalite dual FWB/VL**)
- Found (strong ExpGen + EP Coppieters prog 17.094):
  - **Ambulatoires violences femmes EUR 3.539m** 2026 (19 agrees + 6 facultatives); DF 094.019 eng **2.983m** / liq **2.722m**.
  - Core equality+violence L5 sample: eng **~5.924m** / liq **~5.735m** (019+097+070+071+028+030+054+108+CWEHF+racism+platforms).
  - Named: CWEHF **210k**; provincial platforms **107k**; racism conseil **100k**; LGBTQ Arc-en-ciel **964k**; egalite privee **590k**; DIVICO +**115k**.
  - Dual/triple: FWB pack CL **7.85m** | VL GK **15.16m** | WAL core **~5.7m liq** — **not additive**.
  - Shared FWB-WAL Strategie genre 2025-2029.
- Wrote: sources +2; entity wal_egalite_chances; budgets +20; cmt +1; lb +4; FOI gap_wal_egalite_l5 ready; drafts; raw PDFs; rq_239=done; spawn rq_240; ticks=248
- FOI: WAL L5 operators human send
- Next: prio5 **rq_240**; **progress@250 in 2 ticks**; deferred **rq_116** SWA

### 2026-07-29T11:30:00Z — tick 249
- Unit: **rq_240** (FOI-adjacent hole-fill — **Charleroi culture/sport L5**)
- Found (strong BI2024 synthese eComptes + BI2026 context):
  - **PBA ASBL EUR 1.339834m**; **CCR 0.734m**; ASBL culturelles **1.1515m**; CEME **0.1008m** → culture sample **3.326m**.
  - **Parc des Sports 0.738m** + sport clubs **0.603m** → sport sample **1.341m**.
  - Menages ASBL **1.338m**; social ASBL **0.380m**.
  - BI2026: transfers **240.3m** (-10.9m); pox subsides **−0.5m**; CPAS +0.7m; ZPL −5.6m; ZOHE −5.3m; named 2026 matrix residual FOI.
- Wrote: sources +2; entities PBA/CCR; budgets +15; cmt +1; lb +4; FOI gap_charleroi_subsidies_top20 updated; draft note; rq_240=done; spawn rq_241 progress@250 + rq_242; ticks=249
- FOI: BI2026 named top20 human send
- Next: **rq_241 progress@250 mandatory**; then rq_242; deferred **rq_116** SWA

### 2026-07-29T12:00:00Z - tick 250 - progress coverage % + waste top10
- Unit: **progress@250** (mandatory every-10-ticks; **rq_241**)
- Coverage (order-of-magnitude vs EUR 347.956 bn TE):
  - **A L0 / B L1:** 100% / 100% (unchanged strong)
  - **C L2:** **~79-87%** (up from ~78-86% @240) — VL AJH 240m; FWB MDJ 30.1m + fed receipt 55.7m; equality dual/triple FWB 7.85 / VL GK 15.2 / WAL ~5.7m
  - **D L5:** **~11-19%** still thin — Charleroi culture 3.33m + sport 1.34m; equality category L5; AF multi-caisse prior
  - **E FOI ready:** **~87** (total FOI rows ~91)
- Inventory: budgets ~2691; commitments ~460; leaderboard ~459; entities ~957 lines; sources ~501
- Waste top10: **changed** — fossil 4e inventaire enters #2 (13.3bn), #4 accises 10.5bn, #6 company cars EHS 3.43bn, #7 mazout 1.86bn; cheque still #1 (8.83)
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log; rq_241=done
- Next: prio5 **rq_242**; deferred **rq_116** SWA; human FOI send stack

### 2026-07-29T12:30:00Z — tick 251
- Unit: **rq_242** (FOI-adjacent hole-fill — **equal.brussels call + WAL DIVICO named L5**)
- Found (strong/medium primary):
  - **equal.brussels appel 2026** envelope **~EUR 2m** (FAQ; min **25k**/project; period Sep2026–Nov2027) — dual FWB/VL/WAL equality map.
  - **WAL Pôle ressources violences ASBL ~616k/yr** (was 551k 2024); co-finance COCOF+FWB.
  - **DIVICO named:** Liège **115k**, Namur **60k**, BW **115k** (+55), Nord-Lux **60k** (Hainaut exploratory); uplift **+115k**.
  - DF **094.109** pluriann eng **4.155m** / liq **0.831m** (named: Pôle, ARCA, CAIPS, CODEF, Observatoire, Volontariat, Financité).
  - Pack nouveau départ: policy only (no dedicated cash line yet).
- Wrote: sources +2; entities equal_brussels + pole; budgets +10; cmt +2; lb +4; FOI gap_equal_brussels_budget_l5 ready + gap_wal_egalite_l5 narrowed; drafts; rq_242=done; spawn rq_243; ticks=251
- FOI: equal.brussels full budget + awards human send
- Next: prio5 **rq_243**; deferred **rq_116** SWA

### 2026-07-29T13:00:00Z — tick 252
- Unit: **rq_243** (FOI-adjacent hole-fill — **federal art.47/10 MDJ triple VL/FWB/DG**)
- Found (strong primary Kamer 56K1470 middelenbegroting table, indexed FLWB; PDF download blocked agent-side):
  - **Total EUR 147.338161m** = **VL 90.571934m** + **FWB 55.834914m** + **DG 0.931313m** (+ BRU column 0).
  - Cross-check: VL BO2026 receipt 90.357m; FWB ExpGen 55.7m — close class.
  - Completes triple financing map; **DG spend still FOI** (CoA UHH silent).
- Wrote: sources +1; entity dg notes; budgets +5; cmt +1; lb +3; FOI gap_dg_justizhaus_budget narrowed to spend; draft update; rq_243=done; spawn rq_244; ticks=252
- FOI: DG Justizhaus spend/FTE residual human send
- Next: prio5 **rq_244**; deferred **rq_116** SWA

### 2026-07-29T13:30:00Z — tick 253
- Unit: **rq_244** (FOI-adjacent hole-fill — **AWEX dual FIT export agencies**)
- Found (strong primary EP Jeholet BI2026 table milliers EUR):
  - **AWEX package TOTAL eng=liq EUR 76.843m** 2026 (dotation **75.960m** + missions spec **0.445m** + ACE **0.438m**).
  - 2025 package **67.547m** (dot **66.664m**) — **treasury remonte 9m** not repeated 2026.
  - Strategy 2026-2029 feuille de route; dual FIT Flanders residual FOI; ACE federal-regional co-finance.
- Wrote: sources +1; entities awex/ace/fit; budgets +8; cmt +1; lb +3; FOI gap_fit_budget_2026 ready; draft; rq_244=done; spawn rq_245; ticks=253
- FOI: FIT VEK dual human send
- Next: prio5 **rq_245**; deferred **rq_116** SWA

### 2026-07-29T14:00:00Z � tick 254
- Unit: **rq_245** (FOI-adjacent hole-fill � **hub.brussels dual AWEX/FIT export**)
- Found (strong primary hub.brussels Rapport activite 2024 Annexe 2):
  - **hub.brussels TOTAL recettes=depenses EUR 46.166m** 2024.
  - Dotation **42.007m** (~91%); EU 1.353 + RBC 1.040 + FEDER 0.762 + autres 0.604 + propres 0.400.
  - Spend: remun **31.875m** (~69%); actions 6.186; fonct 5.897; loyers 1.383; invest 0.305; transferts 0.509.
  - Dual/triple: AWEX **76.843m** 2026 | hub **46.166m** 2024 | FIT residual FOI (years differ � not additive).
  - 2026 blog: intl offices **33?21**; EUR cut amount residual FOI.
- Wrote: sources +1; entity hub_brussels; budgets +13; cmt +1; lb +3; FOI gap_hub_brussels_budget_2025_26 ready; draft; raw PDF; rq_245=done; spawn rq_246; ticks=254
- FOI: hub 2025-26 package + cut EUR human send; FIT still ready
- Next: prio5 **rq_246**; deferred **rq_116** SWA

### 2026-07-29T14:30:00Z � tick 255
- Unit: **rq_246** (FOI-adjacent hole-fill � **dual tourism Toerisme VL + visit.brussels; AGMJ ETP**)
- Found (strong/medium primary):
  - **Toerisme Vlaanderen programme SQ BO2024**: VAK **�66.466m** / VEK **�74.816m** (excl apparaat) � BBT 13-R strong.
  - Presentation (pfile 2086302, year class 2025-26): werkings-toelage **39.357m** + invest **32.333m** (=**71.690m**); lonen **19.967m**; werking **5.026m**; EventFlanders ops **1.0m** + topevents **7.5m**; saldo desaffect **80.208m**.
  - **visit.brussels** Cour VISIT.39.302.08 prog 302 **�14.9m** BI2024 (partial � not full ASBL).
  - Dual tourism: VL ~75m vs Visit 14.9m partial (scopes differ; not additive).
  - **AGMJ 801 ETP** 30/06/2025 ExpGen strong; wage bill residual FOI.
  - FIT public primary still incomplete (gap_fit ready).
- Wrote: sources +4; entities TV+Visit; budgets +13; cmt +3; lb +5; FOI gap_visit_brussels_budget_full + gap_tv_presentation_year_confirm ready; drafts; raw PDFs; rq_246=done; spawn rq_247; ticks=255
- FOI: Visit full package + optional TV year stamp human send
- Next: prio5 **rq_247**; deferred **rq_116** SWA

### 2026-07-29T15:00:00Z � tick 256
- Unit: **rq_247** (FOI-adjacent hole-fill � **VISITWallonia dual tourism + Tourisme Wallonie**)
- Found (strong primary EP Lescrenier BI2026 + bud37):
  - **Prog 09.018 Tourisme TOTAL CE=CL EUR 65.632m** 2026 (was 69.868m 2025).
  - **Tourisme Wallonie** (ex-CGT) fonctionnement **48.578m** (49.080m 2025).
  - **VISITWallonia** (ex-WBT) subvention **13.054m**; **global depenses 15.4m** initial 2026 (bud37).
  - CRAC tourisme **4.000m** (was 7.854m).
  - Triple promo: TV SQ VEK **74.8m** | Visit prog302 **14.9m** partial | VW global **15.4m** (years/scopes differ � not additive).
  - WAL also runs dual admin+promo (TW 48.6 + VW 15.4) vs VL single Toerisme agency.
- Wrote: sources +2; entities visitwallonia + tourisme_wallonie; budgets +9; cmt +3; lb +4; raw PDFs; rq_247=done; spawn rq_248; ticks=256
- FOI: none new (material euros sourced); prior Visit full + FIT still human send
- Next: prio5 **rq_248**; deferred **rq_116** SWA

### 2026-07-29T15:30:00Z � tick 257
- Unit: **rq_248** (FOI-adjacent hole-fill � **FIT dual AWEX export package**)
- Found (strong primary BBT SP Diependaele 2026 + JR2025 pfile 2321600):
  - **FIT BO2026 package VEK EUR 63.142m** = werkingsdotatie **52.713m** + subsidiedotatie VEK **10.429m** (VAK sub 10.642m).
  - Werkings -800k Expo Osaka; subsidie VEK -1.089m uitrustingsgoederen.
  - **JR2025**: bedrijfsopbrengsten **71.867m** (2024: 70.314); bedrijfskosten **70.948m** (2024: 76.070); bezoldigingen **37.800m**; omzet 4.401m.
  - Dual/triple export: AWEX **76.843m** 2026 | FIT package **63.1m** | hub.brussels **46.166m** 2024 (years differ � not additive).
  - gap_fit_budget_2026 totals **answered**; residual L5 FOI optional ready.
- Wrote: sources +2; entity FIT; budgets +15; cmt +1; lb +4; FOI gap_fit answered + gap_fit_l5_subsidies ready; draft; raw PDFs; rq_248=done; spawn rq_249; ticks=257
- FOI: L5 beneficiaries optional human send
- Next: prio5 **rq_249**; deferred **rq_116** SWA

### 2026-07-29T16:00:00Z � tick 258
- Unit: **rq_249** (FOI-adjacent hole-fill � **WBI dual international FWB/WAL vs Flanders**)
- Found (strong primary RA2024 + CdC RD26):
  - **WBI total liquidation EUR 104.237m** 2024 / **96.448m** 2025.
  - **FWB subvention** DO14 AB11.4101: **46.742** / **43.945** / **42.945m** 2024 / 2025aju / 2026ini.
  - CdC RD spending review: options >=10% of FWB 2026 subvention; common lines 50/50 FWB-WAL key.
  - Dual Flanders: SN Buitenlands Beleid **8.971m** BO2026 (partial; FIT trade 63.1m separate) � scopes differ not additive.
  - WBI joint FWB+WAL+COCOF cultural/diplomatic/cooperation stack.
- Wrote: sources +2; entity wbi; budgets +6; cmt +1; lb +3; FOI gap_wbi_wal_contribution ready; draft; raw PDFs; rq_249=done; spawn rq_250 progress@260; ticks=258
- FOI: WAL WBI contribution human send
- Next: prio5 **rq_250**; **progress@260 in 2 ticks**; deferred **rq_116** SWA

### 2026-07-29T16:30:00Z � tick 259
- Unit: **rq_250** (FOI-adjacent hole-fill � **WAL WBI dotation closes dual financing**)
- Found (strong primary Parlement wallon bud27 Dolimont):
  - **WAL DF 019.003 WBI dotation EUR 30.098m** 2026 (was **30.698m** 2025; **-0.600m** building EIWB1 option).
  - Dual with **FWB 42.945m** 2026ini ? **sum 73.043m** (vs agency liq 96.448m 2025; residual COCOF/own/EU).
  - CdC 2025A1: WBI consolid� **-19.6m** mainly emphyt�ose 12.1m Sainctelette.
  - gap_wbi_wal_contribution **answered**.
- Wrote: sources +2; budgets +3; cmt +1; lb +2; FOI answered; raw PDFs; rq_250=done; spawn rq_251 progress@260 + rq_252; ticks=259
- FOI: WAL WBI closed public
- Next: **rq_251 progress@260 mandatory**; then rq_252; deferred **rq_116** SWA

### 2026-07-29T17:00:00Z - tick 260 - progress coverage % + waste top10
- Unit: **progress@260** (mandatory every-10-ticks; **rq_251**)
- Coverage (order-of-magnitude vs EUR 347.956 bn TE):
  - **A L0 / B L1:** 100% / 100% (unchanged strong)
  - **C L2:** **~81-89%** (up from ~79-87% @250) � export triple AWEX 76.8 + FIT 63.1 + hub 46.2; tourism TV 74.8 + VW 15.4 + TW 48.6; WBI 96.4 + FWB/WAL dots 73.0; justice fed 147.3
  - **D L5:** **~12-20%** still thin � agency packages lift C more than pure L5
  - **E FOI ready:** see progress file (several answered: FIT totals, WBI WAL)
- Waste top10: **stable** cheque/fossil/company cars/EIWT; dual hole-fills are core economic not pure waste
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log; rq_251=done
- Next: prio5 **rq_252**; deferred **rq_116** SWA; human FOI send stack

### 2026-07-29T17:30:00Z � tick 261
- Unit: **rq_252** (FOI-adjacent hole-fill � **Enabel dual APEFE development cooperation**)
- Found (strong primary Enabel AR 2025-26):
  - **Enabel operating revenue EUR 435.600m** 2025 (357.090m 2024; +22pct).
  - Turnover **407.097m**; op costs **438.056m**; staff costs **91.022m**; staff **2,369**.
  - Volume path 2021-25: 303 / 340 / 335 / 357 / **435** m; 200 ongoing projects.
  - Dual **APEFE** regional: structure public (20 HQ + 52 abroad + 6 expats; linked WBI AG); full budget residual FOI.
  - Partners include Flanders, BCR, Walloon Region + large EU share class.
- Wrote: sources +2; entities enabel+apefe; budgets +16; cmt +2; lb +3; FOI gap_apefe_budget_total ready; draft; raw PDFs; rq_252=done; spawn rq_253; ticks=261
- FOI: APEFE total budget human send
- Next: prio5 **rq_253**; deferred **rq_116** SWA

### 2026-07-29T18:00:00Z � tick 262
- Unit: **rq_253** (FOI-adjacent hole-fill � **PMV JR2025 dual Wallonie Entreprendre**)
- Found (strong primary JR2025 statutory kEUR):
  - **Total assets EUR 4.236bn** end-2025 (was **1.626bn** 2024) � BAC/deelnemingen jump.
  - Eigen vermogen **4.180bn**; geplaatst kapitaal **4.329bn** (niet-opgevraagd 716m).
  - Fin. vaste activa **4.031bn**; deelnemingen verbonden **3.191bn** (was 637m).
  - Bedrijfsopbrengsten **18.758m**; bezoldigingen **21.101m**; resultaat **17.234m**; dividend **3.8m**.
  - Dual **WE equity ~4.98bn** 2025 (prior map) � regional holdings comparable scale; SFPIM federal third layer.
- Wrote: sources +1; entity pmv; budgets +16; cmt +1; lb +3; raw PDF; rq_253=done; spawn rq_254; ticks=262
- FOI: none new (material stock filled); APEFE/Mons residual still ready
- Next: prio5 **rq_254**; deferred **rq_116** SWA

### 2026-07-29T18:30:00Z � tick 263
- Unit: **rq_254** (FOI-adjacent hole-fill � **Mons ASBL L5 sample BI2025**)
- Found (strong primary Mons budget ordinaire 2025 extract):
  - Named L5 sample **n=22** lines sum **~�7.5m** (RCA cluster ~4.25m + MARS package 0.67m + OT + Basket UMH 0.22m + Garance 0.17m + Fondation Mons2025 + film 45k + charte associative + �).
  - Top: RCA piscine **1.90m**; RCA subside **1.16m**; RCA fonct **0.82m**; Fonds impulsion commerces **0.65m**; MARS fonct **0.40m**.
  - Closes long-deferred Mons ASBL L5 sample; BI2026 named residual FOI.
- Wrote: sources +1; budgets ~22; cmt +1; lb +3; FOI gap_mons_bi2026_named ready; draft; rq_254=done; spawn rq_255; ticks=263
- FOI: BI2026 top20 human send
- Next: prio5 **rq_255**; deferred **rq_116** SWA

### 2026-07-29T19:00:00Z � tick 264
- Unit: **rq_255** (FOI-adjacent hole-fill � **finance&invest.brussels dual PMV/WE**)
- Found (strong primary JV2024):
  - **Interventions EUR 131.243m** 2024 (385 firms): **108.3m invested** + **~23m guarantees**.
  - Subsidiary split: FIB **67.6m**/309; boosting **15.7m**/13; BWF+proxilening **24.5m**/299; Brusoc ~9m/162.
  - Cum since 2018: **416.774m** financing / **2,526** firms; latent gains **14.846m**; FTE **~40.7**; mgmt cost ratio **1.87pct** (was 3.38pct 2018).
  - BCR share **69.63%** + private banks/insurers; dual **PMV 4.24bn** + **WE ~4.98bn** + **SFPIM 11.7bn** (four public investment companies).
  - Residual: full statutory BS equity/assets + L5 top stakes FOI (activity report only).
- Wrote: sources +1; entity finance_brussels; budgets +15; cmt +1; lb +3; FOI gap_fib_bilan_l5 ready; draft; raw JV PDF; rq_255=done; spawn rq_256; ticks=264
- FOI: FIB bilan + L5 human send; APEFE/AGMJ residual still ready
- Next: prio5 **rq_256**; deferred **rq_116** SWA

### 2026-07-29T19:30:00Z � tick 265
- Unit: **rq_256** (FOI-adjacent hole-fill � **Innoviris dual VLAIO R&I**)
- Found (strong primary chiffres+compte+RA):
  - **2024 engagements EUR 44.615m** / **325** projects / **215** orgs; full named L5 public xlsx.
  - Axes: Journey **28.2m**; academic **8.87m**; science promo **3.79m**; policy knowledge **3.75m**.
  - Top L5: SYENSQO FUSBAT **2.40m**; ULB KTO **1.66m**; Sirris **1.56m**; SYENSQO Hy-FUEL **1.38m**.
  - Compte 2024: assets **92.6m**; remun **7.753m**; dots fonct+subs **11.28+44.13m**; financement recherche **46.6m**.
  - **2025:** RA invest **43.7m** / **406** projects; assets **74.2m**; remun **7.536m**; dots **5.51+21.66m**; result **-24.5m**.
  - Dual **VLAIO innovatiesteun ~221/197m** awards 2024-25 (much larger Flanders scale).
- Wrote: sources +1; entity innoviris; budgets +24; cmt +1; lb +4; FOI gap_innoviris_l5_2025_26 ready; draft; raw PDFs+xlsx; rq_256=done; spawn rq_257; ticks=265
- FOI: Innoviris 2025 L5 + 2026 BCR codes human send; AGMJ/APEFE residual still ready
- Next: prio5 **rq_257**; deferred **rq_116** SWA

### 2026-07-29T20:00:00Z � tick 266
- Unit: **rq_257** (FOI-adjacent hole-fill � **FWO dual FNRS fundamental research funds**)
- Found (strong primary JV/RA/Resultats):
  - **FWO VL VAK** **�470.3m** 2024 / **�448.2m** 2025; **VEK** **436.8m** / **464.6m**.
  - Fund projects **180?201m**; fund mandaten **109?112m**; SBO pack ~**94�95m**; infra **66.2?19.6m** (one-off timing).
  - Beheers **19.3m (4.11%)** ? **23.1m (5.16%)**; agency bezold **9.0?9.3m**; federal package class **�44m**.
  - **FNRS public subs** **�241.8m** 2024 / **�253.7m** 2025; global **262/279m**.
  - FNRS split 2025: FWB **182.8m**; fed **40.8m**; WAL **22.8m**; Loterie **7.3m**; dons/T�l�vie class **~24.7m**.
  - Doctorants remun **�58.3m** 2025; dual community research (not Innoviris/VLAIO applied).
- Wrote: sources +1; entities fwo+fnrs; budgets +35; cmt +2; lb +4; FOI gap_fnrs_l5_grants_2024_25 ready; draft; raw PDFs; rq_257=done; spawn rq_258; ticks=266
- FOI: FNRS L5 matrix human send; AGMJ/APEFE residual still ready
- Next: prio5 **rq_258**; deferred **rq_116** SWA

### 2026-07-29T20:30:00Z � tick 267
- Unit: **rq_258** (FOI-adjacent hole-fill � **Sciensano federal public health science budget path**)
- Found (strong primary beheersovereenkomst 2024-29 annex + RA2024):
  - Total budget annex **�135.671m** 2024 / **�133.192m** balanced path 2025-29.
  - **Basis dotatie �30.709m**/yr real (fixed 2024-29); new initiatives **�2.479m** 2024 only.
  - Own sales/services **�88.483m**; received subsidies **�14.0m**.
  - Personnel package ~**�83.7m** 2024 (N_LIM 57.6 + LIM 26.0) ? **�82.2m** 2025.
  - Werkingskosten N_LIM **�42.1m**; ESR saldo **-�1.5m** 2024 then 0.
  - RA2024 key figures: budget **�132m** of which **�77m** external (perimeter note vs 135.7m annex).
- Wrote: sources +2; entity sciensano; budgets +19; cmt +1; lb +3; FOI gap_sciensano_outturn_l5 ready; draft; raw PDFs; rq_258=done; spawn rq_259; ticks=267
- FOI: Sciensano outturn + L5 external human send; AGMJ/APEFE residual still ready
- Next: prio5 **rq_259**; deferred **rq_116** SWA

### 2026-07-29T21:00:00Z � tick 268
- Unit: **rq_259** (FOI-adjacent hole-fill � **APEFE fonctionnement dots dual Enabel**)
- Found (strong primary FWB/WBI budget BI2026 p699+justificatifs):
  - **APEFE fonctionnement FWB** AB 41.60.01: **�471k** eng+liq 2025 and 2026.
  - **APEFE fonctionnement WAL** AB 41.60.02: **�510k** 2025 / **�490k** 2026.
  - Combined public fonct dots **�981k** 2025 / **�961k** 2026.
  - WBI seconded staff to APEFE recovered via WBI recettes (not in APEFE fonct lines).
  - Project financing via bilat/sectoriel programmes residual FOI (not named APEFE in project lines).
  - Dual **Enabel �435.6m** 2025 vs APEFE public fonct **~�1m** (scale gap; not additive).
- Wrote: sources +1; budgets +6; cmt +1; lb +2; entity apefe; FOI gap_apefe partial update; draft note; rq_259=done; spawn rq_260; ticks=268
- FOI: APEFE full TCO+projects still ready human send; AGMJ residual still ready
- Next: prio5 **rq_260**; deferred **rq_116** SWA; progress@270 in 2 ticks

### 2026-07-29T21:30:00Z � tick 269
- Unit: **rq_260** (FOI-adjacent hole-fill � **FAVV food chain dual Sciensano**)
- Found (strong primary RC heffingen + BP 21-24 + minister savings note):
  - **Heffingen 2024 excl bonus �51.931m**; FTE controllers **142.34**.
  - Financing model: federal **dotatie** + heffingen + retributies + EU + other (wet 9 dec 2004).
  - BP path: total realisations **173.4 / 179.3 / 173.9m** 2018-20; IB **186.9m** 2021; dotatie **95.9?99.3m**.
  - Savings: minister clarification **not 24% FAVV-targeted**; linear **1.8%/yr** personnel + opex; cum **~4.5%** over 5y on **dotatie only** (heffingen/retributies protected).
  - Dual **Sciensano** public health science (135.7m path) vs FAVV control agency.
- Wrote: sources +2; entity favv; budgets +17; cmt +1; lb +3; FOI gap_favv_budget_2024_26 ready; draft; raw PDFs; rq_260=done; spawn rq_261 progress@270; ticks=269
- FOI: FAVV 2024-26 totals human send; AGMJ residual still ready
- Next: mandatory **progress@270** (rq_261); deferred **rq_116** SWA

### 2026-07-29T22:00:00Z � tick 270 (progress milestone)
- Unit: **rq_261** (mandatory progress@270 coverage % + waste top10)
- Coverage vs �347.956 bn TE:
  - **A L0 / B L1:** **100%** strong
  - **C L2:** **~82�90%** (up from ~81�89% @260) � FWO/FNRS dual, Sciensano, FAVV path, FIB, Innoviris
  - **D L5:** **~13�21%** still thin; Innoviris full L5 2024 + Mons sample lift
  - **E FOI ready:** **~98** drafts (answered ~5)
- Waste top10: **stable** cheque/fossil/company cars/EIWT (pi 8.83�8.08); dual hole-fills are core public goods not pure waste
- Inventory: budgets ~2938 � commitments ~485 � leaderboard ~518 � entities ~197 � sources ~547 � FOI rows ~104
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log; rq_261=done; spawn rq_262; ticks=270
- Next: prio5 **rq_262**; deferred **rq_116** SWA; human FOI send stack

### 2026-07-29T22:30:00Z � tick 271
- Unit: **rq_262** (FOI-adjacent hole-fill � **AFMPS medicines dual Sciensano/FAVV**)
- Found (strong primary RA2024 + medium DC-CT 2025 path):
  - Budget **�128.745m** / realisations **�115.560m** 2024 (**90%**).
  - Personnel real **�63.374m** (budget 74.6m); federal **dotation �28.651m** (~25% of real).
  - **Sciensano expertise �7.054m** paid (dual); ICT **14.1m**; NAT blood **9.4m**.
  - Fees: packaging **18.3m**; DM **13.3m**; AMM only **6.3m of 16.6m** (38% shortfall).
  - Staff **564** (NL 290 + FR 274); DC-CT path budget **�141m** 2025 (70?92?141m 2015-25 class).
  - Health federal triple: Sciensano **136m** + FAVV path **~175m** + AFMPS **116m** (not additive).
- Wrote: sources +2; entity afmps; budgets +16; cmt +1; lb +4; FOI gap_afmps_budget_2025_26 ready; draft; raw PDFs; rq_262=done; spawn rq_263; ticks=271
- FOI: AFMPS 2025-26 + AMM shortfall human send; AGMJ residual still ready
- Next: prio5 **rq_263**; deferred **rq_116** SWA

### 2026-07-29T23:00:00Z � tick 272
- Unit: **rq_263** (FOI-adjacent hole-fill � **KCE dual health quad**)
- Found:
  - **Strong primary INAMI 2025:** transfert centre de connaissance **�22.483m** (kEUR table beheerskosten).
  - Press exact **�22.482.228** 2025 RIZIV admin toelage (reconciles); **�26.447.351** 2026 (+**�3.965m** / **+17.6%**) medium ministerraad KB draft.
  - Financing: charge on RIZIV/INAMI administratiekosten.
  - Health federal **quad:** KCE **22.5m** + AFMPS **115.6m** + Sciensano **135.7m** + FAVV path **~175m** (not additive).
- Wrote: sources +2; entity kce; budgets +4; cmt +1; lb +3; FOI gap_kce_jaarrekening_2024_26 ready; draft; raw INAMI PDF; rq_263=done; spawn rq_264; ticks=272
- FOI: KCE jaarrekening + 2026 BS human send; AGMJ residual still ready
- Next: prio5 **rq_264**; deferred **rq_116** SWA

### 2026-07-29T23:30:00Z � tick 273
- Unit: **rq_264** (FOI-adjacent hole-fill � **INAMI e-health stack + FAM dual health SS**)
- Found (strong primary INAMI 2025 + CoA FAM Nov 2025):
  - **e-gezondheid / e-sant� �113.436m** + **Dotatie e-health �19.112m** = **�132.548m** stack 2025.
  - **FAM** INAMI dotatie **�26.516m** 2025; CoA: cum indemn **�101.1m** end-2024; ops excl indemn **�12.4m** 2023; open cases **989** (was 2445 end-2019).
  - INAMI OA admin **�988.052m**; AFMPS INAMI line **�3.443m** 2025 cross-check.
  - Dual digital health + patient safety next to KCE/AFMPS/Sciensano/FAVV map.
- Wrote: sources +1; entities ehealth+fam; budgets +10; cmt +2; lb +4; FOI gap_ehealth_l5_vendors ready; draft; raw CoA PDF; rq_264=done; spawn rq_265; ticks=273
- FOI: e-health L5 vendors human send; AGMJ residual still ready
- Next: prio5 **rq_265**; deferred **rq_116** SWA

### 2026-07-29T23:45:00Z - tick 274
- Unit: **rq_265** (FOI-adjacent hole-fill - **Smals shared ICT dual e-health/SS**)
- Found (strong primary Smals Activiteitenverslag 2025 kerncijfers):
  - Omzet path **EUR 407.7 / 439.5 / 515.6 / 573.6 / 578.9m** 2021-2025 (exact 578.866.778 2025).
  - Staff end-2025 **2350** (1174 internal + 1176 detached) + >1000 external ICT specialists class; ICT ~79%.
  - Private-sector pass-through **>57% omzet ~EUR 333m** (hardware/software/externals).
  - Self-reported G-Cloud savings **54.4m** + ReUse projects **>45m** 2025 (medium; not external audit).
  - Members **345** (A15+B133+C197); cat A includes eHealth-platform RIZIV RSZ KSZ RVA CDZ etc.
  - Dual: institutional Smals **578.9m** vs INAMI e-health stack **132.5m** (not additive; Smals is delivery vehicle class).
  - Cost-sharing VZW in-house (Wet 15 jan 1990 art.17bis) - recharges not pure subsidy.
- Wrote: sources +1; entity smals; budgets +9; cmt +1; lb +4; FOI gap_smals_l5_members ready; draft; raw AV PDF; rq_265=done; spawn rq_266; ticks=274
- FOI: Smals L5 members + contractors human send; e-health L5 residual; AGMJ residual still ready
- Next: prio5 **rq_266**; deferred **rq_116** SWA

### 2026-07-30T00:15:00Z - tick 275
- Unit: **rq_266** (FOI-adjacent hole-fill - **CDZ Controledienst + HDA dual**)
- Found (strong primary CDZ JV2025):
  - **Uitvoering 2025:** ontvangsten **EUR 8.259m** / uitgaven **EUR 8.043m** (pers **6.029** + werking **1.953** + invest **0.061**); surplus **0.216m**.
  - **Begroting 2026:** ont **8.679m** / uitg **9.863m** (pers 7.086 + werking 2.636); tekort **1.184m** from admin reserve.
  - Sector charges: mut **5.139m** + VMOB **2.734m** + tussenpersonen **0.385m** 2025 (sector-financed not federal TE).
  - Staff **46** + **3 Smals**; assets **4.753m**; admin reserve **3.475m**.
  - **VI administratiekosten 2023 EUR 1.3768bn** (+4.18% vs 1.322bn 2022) dual INAMI OA 988m 2025 different perimeter.
  - Geneesk. verzorging VI **37.30bn** / uitkeringen **13.05bn** 2023.
- HDA JV2025 (medium euros): staff **13** +10 vac 2026; RRF seed **7m** 2021; no annual EUR outturn -> FOI.
- Wrote: sources +2; entities cdz+hda; budgets +18; cmt +2; lb +4; FOI gap_hda_budget ready; draft; raw PDFs; rq_266=done; spawn rq_267; ticks=275
- FOI: HDA budget human send; mutual L5 residual updated CDZ 1.38bn; AGMJ residual still ready
- Next: prio5 **rq_267**; deferred **rq_116** SWA

### 2026-07-30T00:45:00Z - tick 276
- Unit: **rq_267** (FOI-adjacent hole-fill - **KSZ dual Smals ICT**)
- Found (strong primary KSZ financiele middelen site):
  - Ontvangsten=uitgaven **EUR 19.701m 2024 / 19.761m 2025**.
  - **ICT werking EUR 13.452m / 13.437m** (~68% of spend) dual Smals class.
  - Personeel **3.771 / 3.896m**; gewone werking **2.302 / 2.271m**.
  - IB2025 OISZ bijd: RSZ **15.103m** (90%) + RSVZ **1.678m** (10%) = **16.781m**.
  - Toewijzing 17.171/17.031m + eigen 2.392/2.730m.
  - Triple digital map: KSZ **19.8m** + Smals **578.9m** + INAMI e-health **132.5m** (not additive).
- Wrote: sources +1; entity ksz; budgets +18; cmt +1; lb +4; FOI gap_ksz_ict_l5_smals ready; draft; raw HTML; rq_267=done; spawn rq_268; ticks=276
- FOI: KSZ ICT L5 Smals share human send; Smals L5 residual updated; AGMJ residual still ready
- Next: prio5 **rq_268**; deferred **rq_116** SWA

### 2026-07-30T01:15:00Z - tick 277
- Unit: **rq_268** (FOI-adjacent hole-fill - **CoA 182e OISZ + SS consol dual eHealth**)
- Found (strong primary Rekenhof 182e Boek 2025 SS):
  - SS geconsolideerd **EUR 139.3bn uitg / 139.8bn ont** 2024; **Beheerskosten 2.8bn**.
  - **eHealth institutional beheer EUR 15.9m 2023** (15.3m 2022) dual INAMI stack 132.5m not additive.
  - FEDRIS beheer **54.2m** 2023; FPS exp **596.4m** 2024.
  - HZIV total **634.3m** / beheer **38.8m** 2023 dual mutual.
  - RVA beheer **277.9m**; HVW beheer **47.9m**; RSVZ beheer **106.9m** 2023.
  - RJV exp **6.381bn** 2024; FSO exp **838.7m** 2024; KSZ CoA 17.4m 2023 confirms path.
- Wrote: sources +1; entities +7; budgets +28; cmt +4; lb +7; FOI gap_oisz_jaarrekeningen ready; draft; raw CoA PDF; rq_268=done; spawn rq_269; ticks=277
- FOI: OISZ 2024-25 jaarrekeningen human send; eHealth/unemp FOI notes updated; AGMJ residual still ready
- Next: prio5 **rq_269**; deferred **rq_116** SWA

### 2026-07-30T01:45:00Z - tick 278
- Unit: **rq_269** (FOI-adjacent hole-fill - **FPD + RSZ beheer + pensioenen + loonmatrix**)
- Found (strong primary CoA 182e):
  - **FPD beheer EUR 287.7m 2023** (222.3m 2022); opdrachten **67.95bn**; lonen **171.3m**.
  - **RSZ beheer EUR 282.8m 2023** (251.9m 2022); opdrachten **106.87bn**; lonen **158.1m**; Smals voorschot residual 2.4m CoA.
  - **Pensioenen 2024 total EUR 66.764bn** (werkn 40.1 + overheid 21.0 + zelfst 5.6).
  - OISZ loonmatrix sample **~848m** (RVA 211 FPD 171 RSZ 158 RIZIV 118 …).
  - SS saldo **+537m** 2024.
- Wrote: sources +1; entities fpd+rsz; budgets +21; cmt +4; lb +5; FOI notes; rq_269=done; spawn rq_271 + progress@280; ticks=278
- FOI: OISZ 2024-25 still ready; Smals advances note; AGMJ residual still ready
- Next: prio5 **rq_271** (before progress@280); deferred **rq_116** SWA

### 2026-07-30T02:15:00Z - tick 279
- Unit: **rq_271** (FOI-adjacent hole-fill - **CREG + BIPT dual federal regulators**)
- Found (strong primary AR):
  - **CREG lasten EUR 22.409m 2023** (16.041m 2022); **personeel 14.685m**; overwinsten spent **2.161m** of 4.119m env; accijns finance.
  - Kamer medium **CREG budget 2026 EUR 24.396m**.
  - **BIPT exp EUR 79.755m / rev 78.463m 2024**; personnel pack **27.357m**; public licence fees **55.1m**; staff **251** (242 FTE).
  - Ombuds postal **2.35m** + telecom **2.70m**.
  - Dual energy/telecom regulators sector-fee financed not TE.
- Wrote: sources +3; entities creg+bipt; budgets +19; cmt +2; lb +5; FOI gap_creg_bipt ready; draft; raw ARs; rq_271=done; elevate rq_270; spawn rq_272; ticks=279
- FOI: CREG/BIPT multi-year human send; AGMJ residual still ready
- Next: **MANDATORY progress rq_270 @ tick 280**; then rq_272

### 2026-07-30T02:45:00Z - tick 280 (progress milestone)
- Unit: **rq_270** (mandatory progress@280 coverage % + waste top10)
- Coverage vs EUR 347.956 bn TE:
  - **A L0 / B L1:** **100%** strong
  - **C L2:** **~84-92%** (up from ~82-90% @270) — SS CoA 139.3bn + pensions 66.8bn + OISZ beheer (FPD/RSZ/RVA) + Smals 579m + KSZ + health stack + CREG/BIPT
  - **D L5:** **~14-22%** still thin structural; OISZ/Smals mostly aggregates
  - **E FOI ready:** **~106** drafts (answered ~5)
- Waste top10: **stable** cheque/fossil/company cars/EIWT (pi 8.83-8.08); dual hole-fills are core public goods not pure waste
- Inventory: budgets ~3081 · commitments ~503 · leaderboard ~558 · entities ~216 · sources ~561 · FOI rows ~112
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log; rq_270=done; ticks=280
- Next: prio5 **rq_272**; deferred **rq_116** SWA; human FOI send stack

### 2026-07-30T03:15:00Z - tick 281
- Unit: **rq_272** (FOI-adjacent hole-fill - **FSMA dual CREG/BIPT/NBB**)
- Found (strong primary FSMA JV2024):
  - Budget werkings **EUR 112.373m** 2024 (+zetel 3.122m = contrib **115.495m**).
  - P&L: opbrengsten **115.405m** / werkingskosten **107.469m** 2024 (101.473m 2023).
  - Bezoldigingen **79.831m** (~74%); diensten **21.249m**; surplus return **7.907m** to supervised entities.
  - Staff **375** (353 VTE; max 399); assets **80.226m**.
  - Sector-contribution financed; dual CREG 22.4m + BIPT 79.8m + NBB prudential.
- Wrote: sources +1; entity fsma; budgets +14; cmt +1; lb +4; FOI gap_fsma_budget_2025_26 ready; draft; raw JV; rq_272=done; spawn rq_273; ticks=281
- FOI: FSMA 2025 budget detail human send; AGMJ residual still ready
- Next: prio5 **rq_273**; deferred **rq_116** SWA

### 2026-07-30T03:45:00Z - tick 282
- Unit: **rq_273** (FOI-adjacent hole-fill - **NBB ops dual FSMA prudential**)
- Found (strong primary NBB Ondernemingsverslag 2024):
  - Personeelskosten **EUR 335.7m 2024** (451.3m 2023 spike; 320.0m 2022).
  - Beheerskosten **131.3m** (ICT 43.9 + third parties 37.9 + building 12.7 + tax 6.4).
  - Ops pack **486.6m** 2024; biljetten 9.6m; afschr 10.0m.
  - **Prudentieel recovery EUR 134.1m** (banks 85.8 + ins 46.8 + other 1.5) dual FSMA.
  - Overige baten 220.5m (balanscentrale pack 55.5m).
  - Boekjaarverlies **3.679bn** monetary (not ops waste); reserves depleted.
- Wrote: sources +1; entity nbb; budgets +16; cmt +1; lb +5; FOI gap_nbb_fte ready; draft; raw OV; rq_273=done; spawn rq_274; ticks=282
- FOI: NBB FTE/ops-split human send; AGMJ residual still ready
- Next: prio5 **rq_274**; deferred **rq_116** SWA

### 2026-07-30T04:15:00Z - tick 283
- Unit: **rq_274** (FOI-adjacent hole-fill - **CGVS dual Fedasil asylum decisions**)
- Found (strong primary CGVS JV2024):
  - Budget available **EUR 61.979m**; spent **57.032m** (92%) 2024.
  - Personeel **47.005m** (statutair 35.9 + contractueel 11.1); werking 6.9m; ICT 0.74m.
  - **Smals/eGOV EUR 1.809m** dual Smals 579m.
  - VTE **600.9** end-2024 (479 A + 122 other); hires 71 / leavers 57.
  - Dual Fedasil reception **943m** 2024 (not additive full chain).
  - AMIF 3 projects residual EUR FOI.
- Wrote: sources +1; entity cgvs; budgets +11; cmt +1; lb +4; FOI gap_cgvs_amif ready; draft; raw JV; rq_274=done; spawn rq_275; ticks=283
- FOI: CGVS AMIF cash human send; Fedasil L5 + Smals notes updated; AGMJ residual still ready
- Next: prio5 **rq_275**; deferred **rq_116** SWA

### 2026-07-30T04:45:00Z - tick 284
- Unit: **rq_275** (FOI-adjacent hole-fill - **DVZ + RVV dual CGVS/Fedasil asylum chain**)
- Found (strong primary IBZ Strategisch plan 2025-2029 + DVZ AV2024):
  - **DVZ Enveloppe 2 personeel EUR 154.844m** 2025 (VL=VE); VTE **2217.9** IBZ / **2174.3** AV (gesloten 932.7 + centraal 1241.6); effectieven **2461**.
  - **RVV hosted krediet EUR 30.236m** VE 2025; VTE **312.1**; effectieven 331.
  - **CGVS hosted EUR 58.801m** VE 2025 (aligns JV2024 ~62m available).
  - **Fedasil dotatie EUR 826.239m** 2025 (below 2024 exp 943m).
  - Admin+decision+appeal stack **~243.9m** + reception 826m; **not TE-additive**.
  - FOD IBZ global **2.514bn** VL (basis 990m; ~61pct hosted); ASTRID **76.5m**; zones **210.7m**.
  - Closed centres: capacity avg 487, occ 81pct; inscriptions 4804 removals 3770 2024.
- Wrote: sources +2; entities dvz+rvv+fod_ibz; budgets +26; cmt +4; lb +6; FOI gap_dvz_ops ready; draft; raw IBZ plan + DVZ AV; rq_275=done; spawn rq_276; ticks=284
- FOI: DVZ ops TCO beyond personnel human send; AGMJ residual still ready
- Next: prio5 **rq_276**; deferred **rq_116** SWA

### 2026-07-30T05:15:00Z - tick 285
- Unit: **rq_276** (FOI-adjacent hole-fill - **NIRAS + Bel V dual FANC nuclear stack + ASTRID reconcile**)
- Found (strong primary NIRAS FV2024/2025 + Bel V AR2024 + ASTRID legal):
  - **NIRAS omzet EUR 185.3m 2024 / 315.6m 2025**; bedrijfskosten **264.3 / 397.5m**; bezold **28.0 / 27.8m**; consol bezold **68.4m** 2025.
  - Assets **1.487bn 2024 / 1.777bn 2025**; cum invest **728.5m** since 1983; kapitaalsubsidies **157.7m**.
  - Polluter-pays (not pure TE); dual FANC/Bel V/SCK/Belgoprocess.
  - **Bel V turnover EUR 16.016m 2024**; op charges 15.189m; wages **12.337m** (~81%); assets 19.8m; staff ~**90**; FANC subsidiary TSO.
  - **ASTRID** contract ops **46.5m/yr** 2023-27 vs IBZ toelage **76.5m** 2025 (~30m residual FOI); invest subscriptions **117m**.
- Wrote: sources +4; entities niras+bel_v+astrid+fanc; budgets +35; cmt +4; lb +6; FOI gap_astrid + gap_fanc ready; drafts; raw NIRAS+BelV; rq_276=done; spawn rq_277; ticks=285
- FOI: ASTRID reconcile + FANC budget human send; AGMJ residual still ready
- Next: prio5 **rq_277**; deferred **rq_116** SWA

### 2026-07-30T05:45:00Z - tick 286
- Unit: **rq_277** (FOI-adjacent hole-fill - **SCK CEN dual NIRAS/FANC/Bel V nuclear R&D**)
- Found (strong primary Highlights 2024/2025 charts + financiering page):
  - **Charges EUR 256.9 / 268.4 / 291.5m** 2023-25; **income 274.5 / 282.6 / 280.2m**.
  - Personnel **123.9m 2024 / 132.4m 2025**; purchases **132.6 / 133.5m**; staff **990 -> 999**.
  - Gov subsidies+grants **94.2 / 98.8m**; turnover **107.2 / 102.3m**.
  - Financing pie 2024 class: eigen **44%** / specific BE **31%** / general dotatie **21%** / EU **4%**.
  - Dual nuclear stack with NIRAS 316m + Bel V 16m + FANC FOI.
- Wrote: sources +3; entity sck_cen; budgets +29; cmt +1; lb +5; FOI gap_sck_dotatie ready; draft; chart extracts; rq_277=done; spawn rq_278; ticks=286
- FOI: SCK general vs mission cash human send; AGMJ residual still ready
- Next: prio5 **rq_278**; deferred **rq_116** SWA

### 2026-07-30T06:15:00Z - tick 287
- Unit: **rq_278** (FOI-adjacent hole-fill - **MYRRHA/MINERVA envelope + SMR + SCK FPS lines**)
- Found (strong primary Kamer 55K2933/016 FOD Economie Energie justification):
  - **MYRRHA structural envelope >EUR 550m 2019-2038** (CM Sept 2018).
  - Phase1 IVZW BA 42.50.41.40.12: **32.6 / 20.4 / 17.4 / 8.1 / 7.9 / 6.4m** 2022-27.
  - Parts 2-3 SCK BA 42.50.41.40.07: **43.6 / 10.5 / 7.6 / 7.8 / 1.8 / 1.7m** 2021-26.
  - **SCK werkingsdotatie BA 42.50.41.40.05: 54.1m** path 2024-27 (55.5m 2023).
  - **SMR-LFR**: CM text **25m/yr 2023-26** (100m); BA eng **50m** 2022 / liq **12.5m** 2023-25 / **21.5m** 2026 (wedge residual).
  - SCK invest line ~**4.1m/yr**.
- Wrote: sources +1; entity myrrha_ivzw; budgets +25; cmt +3; lb +5; FOI gap_myrrha_belspo ready; draft; raw Kamer PDF; rq_278=done; spawn rq_279; ticks=287
- FOI: Belspo MYRRHA + SMR full cash human send; gap_sck note updated partial fill
- Next: prio5 **rq_279**; deferred **rq_116** SWA

### 2026-07-30T06:45:00Z - tick 288
- Unit: **rq_279** (FOI-adjacent hole-fill - **Hedera CAP nuclear provisions dual Synatom/NIRAS**)
- Found (strong primary Kamer 56K1202 + Synatom AR2024 + CPN note + INR annex):
  - Phoenix **CAP 15bn EUR** (2022 prices, 3pct index): tranche1 **12.2bn** paid 14 Mar 2025; tranche2 **~3.7bn** at LTO restart.
  - SYNATOM eoy2024 assets **12.9bn** (CAP portfolio 9.494bn + residual 3.4bn); Electrabel repay **1.96bn** 2024.
  - Provisions +**488m** 2024 (accretion 407m); state dismantling dissynergy **154.4m**.
  - Hedera: interest **146.4m** 2025; AIF fees ~**2.3m**; yield target 3pct vs actuarial 2.86pct.
  - NIRAS 5y plan **511m** 2026-30; volume adj **553.6m** to 2035; INR classifies Hedera **S.1311**.
  - CAP is **stock/transfer** not annual TE waste.
- Wrote: sources +3; entities hedera+synatom+cpn; budgets +14; cmt +3; lb +6; FOI gap_hedera_budget ready; draft; raw Kamer+Synatom; rq_279=done; spawn progress@290 + rq_281; ticks=288
- FOI: Hedera 2026 ops table human send; AGMJ residual still ready
- Next: prio5 **rq_281**; mandatory **rq_280 progress@290** when ticks hit 290; deferred **rq_116** SWA

### 2026-07-30T07:15:00Z - tick 289
- Unit: **rq_281** (FOI-adjacent hole-fill - **ASEVA/APETRA strategic oil stocks dual Hedera energy security**)
- Found (strong primary CoA 2022 + Beleidsverslag 2023 OCR):
  - **Bijdrage EUR 175.2m 2022 / 211.8m 2023** (oil-product levy).
  - **ESR 103.0m 2022 / ~188.4m 2023**; accounting profit 271.8 / ~155.1m.
  - Opslag **63.8m** 2022; tickets **3.8 / 20.4m**; debt **1015 -> 935m** (all FAS).
  - Assets **2.286bn** stock book **2.193bn** (market ~2.75bn) 2022; stock days **93.8 / 90.58**.
  - VTE **4.4** end-2022 (+2 hires 2023); APETRA renamed ASEVA law 21Dec2023.
  - Dual energy security with Hedera nuclear CAP 15bn (not TE-additive).
- Wrote: sources +2; entity aseva; budgets +25; cmt +1; lb +5; FOI gap_aseva_2024 ready; draft; raw CoA+BV; rq_281=done; spawn rq_282; ticks=289
- FOI: ASEVA 2024 accounts + storage L5 human send
- Next: **MANDATORY progress rq_280 @ tick 290**; then rq_282; deferred **rq_116** SWA

### 2026-07-30T07:45:00Z - tick 290 (progress milestone)
- Unit: **rq_280** (mandatory progress@290 coverage % + waste top10)
- Coverage vs EUR 347.956 bn TE:
  - **A L0 / B L1:** **100%** strong
  - **C L2:** **~86-94%** (up from ~84-92% @280) — FSMA/NBB + asylum chain DVZ/CGVS/RVV + nuclear NIRAS/Bel V/SCK/MYRRHA + ASEVA; Hedera CAP 15bn **stock** off pure TE pie
  - **D L5:** **~14-22%** still thin structural
  - **E FOI ready:** **~115** drafts (answered ~5)
- Waste top10: **stable** cheque/fossil/company cars/EIWT (pi 8.83-8.08); Hedera CAP stock noted off annual top10
- Inventory: budgets ~3277 · commitments ~522 · leaderboard ~604 · entities ~232 · sources ~579 · FOI rows ~122
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log; rq_280=done; spawn continue; ticks=290
- Next: prio5 **rq_282**; deferred **rq_116** SWA; human FOI send stack

### 2026-07-30T08:15:00Z - tick 291
- Unit: **rq_282** (FOI-adjacent hole-fill - **energy crisis social premiums + IRE/SCK nuclear passive**)
- Found (strong primary Kamer 55K2933/016 FOD Economie Energie):
  - **Mazout cheque EUR 207.9m 2022 / 143.85m 2023**; collective social tariff **113m** 2023.
  - Social heating fund **~21m** path 2023-27 (38m 2022); pack 2023 sum **~278m**.
  - **IRE passive waste+U ~8.7m/yr** BA 42.30.41.40.22; decom 62k; class need 14.9m.
  - **SCK technical passive:** spend 11-14m/yr 2018-21; fund ~16m eoy2021; 5y need **95m**; propose **20m** liq from 2023; engagement residual **231.6m**.
  - Dual ASEVA oil levy structural + Hedera nuclear CAP stock.
- Wrote: sources +1; entities ire+heating fund (+fod_economy); budgets +23; cmt +3; lb +6; FOI gap_sck_ire_passive ready; draft; rq_282=done; ticks=291
- FOI: SCK/IRE passive cash outturn human send; AGMJ residual still ready
- Next: prio5 **rq_283**; deferred **rq_116** SWA

### 2026-07-30T08:45:00Z - tick 292
- Unit: **rq_283** (FOI-adjacent hole-fill - **IRE-SCK partnership / SMART / SCK phys prot / FAPETRO / fusion / ETF**)
- Found (strong primary Kamer 55K2933/016 FOD Economie Energie BA tables kEUR):
  - **IRE-SCK partnership** BA 42.50.51.11.01: path **8.77 / 8.94 / 39.12 / 9.30 / 9.49 / 9.68 / 9.87m** 2021-27; CM Apr2017 **18.235m** 2017-18 + **8.1m/yr const-2017 to 2045**; request **65.842m** 2023-26.
  - **SMART** BA 42.50.51.11.05: **13.5m** 2021 then 0 (to RRF); envelope **52m** 2019-20; add request **22.85m** const2020.
  - **IRE invest** BA 42.50.51.11.07: **~4.0-4.4m/yr** 2021-26.
  - **SCK phys prot** BA 42.50.61.41.05: **7.60 / 9.17 / 9.35 / 9.54 / 9.73 / 9.92m** 2021-26; dossier **50.483m** const2019.
  - **SCK invest** BA 42.50.61.41.03: flat **4.111m/yr**.
  - **FAPETRO**: personnel **0.635m** + control **2.44m** (levy **0.22 EUR/1000L**); ~3.1m class.
  - **Fusion pack**: ERM research **686k** + unis **268k** + SCK **67k** = **~1.02m**; F4E direct **160k**; AGORIA **104k**; ETF **24.75m/yr**.
- Wrote: sources +1; entity fapetro; budgets +69; cmt +6; lb +6; FOI gap_ire_sck_partnership_smart_cash ready; draft; rq_283=done; spawn rq_284; ticks=292
- FOI: partnership/SMART/ETF L5 human send; dual passive + SCK dotatie still ready
- Next: prio5 **rq_284**; deferred **rq_116** SWA

### 2026-07-30T09:15:00Z - tick 293
- Unit: **rq_284** (FOI-adjacent hole-fill - **CERN + Denmark RES statistical transfer + intl energy orgs**)
- Found (strong primary Kamer 55K2933/016 FOD Economie):
  - **CERN** BA 42.50.35.40.07: **29.87m** 2021 / **31.274m** path 2022-27; CHF **32.668m** BE share 2022.
  - **DK RES statistical transfer** BA 42.50.352001: liq **22.3 / 0 / 16.8 / 14.6 / 13.1 / 14.3m** 2021-26; CM May2022 @ **12.5 EUR/MWh** indexed; period 2021-25.
  - **IEA** vol **552k** 2021 (500k Africa one-off) then **52k**; **IRENA** 45k; IEF 33k; R&D energy 155k; UNSCEAR 15k.
  - Pack class **~48.4m** 2023 (CERN+DK+small).
- Wrote: sources +1; entity cern_be_contrib; budgets +59; cmt +3; lb +4; FOI gap_cern_return_dk_res_outturn ready; draft; rq_284=done; spawn rq_285; ticks=293
- FOI: CERN return + DK MWh outturn human send
- Next: prio5 **rq_285**; deferred **rq_116** SWA

### 2026-07-30T09:45:00Z - tick 294
- Unit: **rq_285** (FOI-adjacent hole-fill - **CREG energy crisis pack + CCE/INR**)
- Found (strong primary Kamer 55K2933/016 FOD Economie prog 21/4):
  - **BA 21.40.414001** CREG social tariff enlargement: **276 / 733.34 / 642.4 / 3.4m** 2021-24 then **3.4m/yr** residual.
  - **BA 21.40.414003** CREG basisfonds heating: **517.2m** 2022 / **1 444.5m** 2023 (elec **620.7** + gas **823.8** Q1-23).
  - Pack class **~1.25bn** 2022 / **~2.09bn** 2023; dual mazout/heating fund BA 42.40 + FFS social tariff inventory.
  - **CCE/CRB** BA 21.40.414002 **~5.4m/yr**; **ICN/INR** BA 21.40.414006 **~1.3m/yr**.
- Wrote: sources +1; entities cce_crb+icn_inr; budgets +27; cmt +5; lb +5; FOI gap_creg_crisis_outturn ready; draft; rq_285=done; spawn rq_286; ticks=294
- FOI: CREG crisis BA outturn + FFS dual recon human send
- Next: prio5 **rq_286**; deferred **rq_116** SWA

### 2026-07-30T10:15:00Z - tick 295
- Unit: **rq_286** (FOI-adjacent hole-fill - **federal H2 RRF pack + press concession BA**)
- Found (strong primary Kamer 55K2933/016):
  - **BA 42.50.313203** H2 call/backbone: eng **300m** 2022+2023 (re-inscription class); liq **4/4/24/86m** 2024-27; RRF -50kt CO2 target.
  - **BA 313204** H2 import infra: eng **10m**; liq **2/3/3/2m**.
  - **BA 313205** green steel electrolyser: eng **6m**; liq **1/2/2/1m**.
  - Pack eng class **~316m**; dual SMR 100m separate.
  - **BA 43.40.31.22.01** press concession: liq **168/175.7/175.7** then **129-138m** path 2021-27 (upgrades 125m secondary).
- Wrote: sources +1; entity fed_h2_rrf; budgets +25; cmt +5; lb +5; FOI gap_h2_rrf_l5_winners ready; draft; rq_286=done; spawn rq_287; ticks=295
- FOI: H2 L5 winners human send; bpost press dual already ready
- Next: prio5 **rq_287**; deferred **rq_116** SWA

### 2026-07-30T10:45:00Z - tick 296
- Unit: **rq_287** (FOI-adjacent hole-fill - **telecom connectivity + Airbus/Clean Aviation + BMA + FPB**)
- Found (strong primary Kamer 55K2933/016):
  - **BA 59.02.32.00.01** telecom connectivity: eng **66.2m** 2023; liq **35 + 31.2m**; split **5G 24 / 6G 1.5 / white zones 40.7m**.
  - **Airbus** BA 44.40.51.22.01 initial eng **45m**; Clean Aviation residual BA 51.22.03 eng **4.929m** 2022.
  - **BMA** BA 41.10.414001 **~9.1m/yr**; **FPB** BA 60.10.414003 **~11.9m/yr**.
- Wrote: sources +1; entities +4; budgets +~30; cmt +4; lb +5; FOI gap_telecom_airbus_l5 ready; draft; rq_287=done; spawn rq_288; ticks=296
- FOI: telecom+Airbus L5 human send
- Next: prio5 **rq_288**; deferred **rq_116** SWA

### 2026-07-30T11:15:00Z - tick 297
- Unit: **rq_288** (FOI-adjacent hole-fill - **Energy Transition Fund deepen**)
- Found (strong primary Kamer 55K2933/016 + FOD overzicht Jul2026):
  - Calls **I–VI** awards sum **€129.146m** / **84** projects (0.22+27.9+29.1+23.0+24.4+24.5m).
  - BA **24.75m/yr** + ops **250k**; financed by Doel1&2 LTO fee **20m/yr** 2016–25.
  - Public overzicht: **140** named projects calls I–X (Jul 2026); sample Elia/SCK/Fluxys/BASF/INOVYN SMR.
  - Per-project EUR still opaque → FOI.
- Wrote: sources +1; entity etf; budgets +calls/financing; cmt +3; lb +4; FOI gap_etf_project_eur_matrix ready; draft; raw PDF; rq_288=done; spawn rq_289; ticks=297
- FOI: ETF EUR matrix human send
- Next: prio5 **rq_289**; **progress@300 in 3 ticks**; deferred **rq_116** SWA

### 2026-07-30T11:45:00Z - tick 298
- Unit: **rq_289** (FOI-adjacent hole-fill - **quality infrastructure BELAC+NBN+metrology**)
- Found (strong primary Kamer 55K2933/016):
  - **BELAC**: personnel **0.88m** + functioning **2.72m** = **~3.6m** 2023 (13 FTE statut; fee-funded staff off-table).
  - **NBN pack**: Antennes-Normes **4.46m** + NBN subside **2.07m** + patent cells **0.54m** = **~7.1m**.
  - **EMPIR 120k + EPM 200k** = **0.32m**.
  - Pack class **~11.0m** 2023.
  - AGMJ: CFWB chiffres cles portal has interactive budget dashboards — no machine-readable EUR this tick; wage FOI still ready.
- Wrote: sources +1; entities belac+nbn; budgets +pack; cmt +4; lb +4; FOI gap_nbn_antennes_l5 ready low prio; draft; rq_289=done; spawn **rq_290 progress@300** + rq_291; ticks=298
- FOI: NBN L5 low prio human send
- Next: **rq_290 progress@300** then rq_291; deferred **rq_116** SWA

### 2026-07-30T12:15:00Z - tick 299
- Unit: **rq_291** (FOI-adjacent hole-fill before progress - **surendettement + telecom DG admin**)
- Found (strong primary Kamer 55K2933/016):
  - **Debt mediator fees** BA 49.40.12.11.58: **6.93 / 5.99 / 6.19m** path then flat **6.19m**; staff **~0.31m**; pack **~6.51m** 2023.
  - **DG Telecom admin**: personnel **1.05m** + ops **1.39m** = **~2.43m** 2023 (dual connectivity subsidies 66.2m).
- Wrote: sources +1; entities +2; budgets +pack; cmt +2; lb +2; FOI gap_surendettement_unit_cost ready; draft; rq_291=done; spawn rq_292; ticks=299
- FOI: unit cost/cases human send
- Next: **MANDATORY rq_290 progress@300**; then rq_292; deferred **rq_116** SWA

### 2026-07-30T12:45:00Z - tick 300 (progress milestone)
- Unit: **rq_290** (mandatory progress@300 coverage % + waste top10)
- Coverage vs EUR 347.956 bn TE:
  - **A L0 / B L1:** **100%** strong
  - **C L2:** **~87-95%** (up from ~86-94% @290) — FPS Economy energy crisis CREG ~2bn peak + H2 RRF 316m eng + press concession + telecom 66m + Airbus 45m + ETF 129m awards + quality infra 11m + surendettement 6.2m
  - **D L5:** **~15-23%** — ETF 140 named projects (EUR FOI); H2/telecom/Airbus L5 residual
  - **E FOI ready:** **~124** drafts (answered ~5)
- Waste top10: **stable** cheque/fossil/company cars/EIWT (pi 8.83-8.08); Hedera CAP stock off annual top10; CREG crisis pack temporary noted off pure-waste top10
- Inventory: budgets ~3626 · commitments ~557 · leaderboard ~645 · entities ~249 · sources ~588 · FOI rows ~131
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log; rq_290=done; ticks=300
- Next: prio5 **rq_292**; deferred **rq_116** SWA; human FOI send stack

### 2026-07-30T13:15:00Z - tick 301
- Unit: **rq_292** (FOI-adjacent hole-fill - **Statbel + FANC financing model**)
- Found:
  - **Statbel** (strong Kamer): FTE **275.6** (01 Jul 2022); ops+fund+enqueteurs pack **~€4.4m** 2023 class (functioning ~0.99 + fund contract 0.84 + enqueteurs ~1.71 + other); statutaire payroll **pour mémoire** FOI.
  - **FANC** (strong IRRS 2023): category C; **100% fee/tax** financed; NPP taxes **~75%** income; must balance budget; dual Bel V 16m already mapped; absolute EUR still FOI.
- Wrote: sources +2; entity statbel; budgets +pack; cmt +2; lb +2; FOI gap_statbel_statutaire_payroll ready; draft; IRRS raw; gap_fanc note; rq_292=done; spawn rq_293; ticks=301
- FOI: Statbel wage bill + FANC EUR residual human send
- Next: prio5 **rq_293**; deferred **rq_116** SWA

### 2026-07-30T13:45:00Z - tick 302
- Unit: **rq_293** (FOI-adjacent hole-fill - **consumer protection external pack**)
- Found (strong primary Kamer 55K2933/016 prog 49):
  - **AB-REOC/BV-OECO** **506k** flat; **CEC** **162k** (+ EC 50% class); **Ombudsdienst Consument** **~395k** 2023.
  - Patients LUSS+VPP **38k**; ECC ODR **50k**; CLV travel **15k**.
  - Pack **~1.17m** 2023; dual surendettement **6.2m**.
- Wrote: sources +1; entities +3; budgets +pack; cmt +3; lb +3; FOI gap_consumer_adr_outturn ready low prio; draft; rq_293=done; spawn rq_294; ticks=302
- Note: FPS Economy Kamer 55K2933 largely mined — next prefer new primary PDFs
- Next: prio5 **rq_294**; deferred **rq_116** SWA

### 2026-07-30T14:15:00Z - tick 303
- Unit: **rq_294** (FOI-adjacent hole-fill - **Kansspelcommissie KSC AR2024**)
- Found (strong primary KSC Jaarverslag 2024):
  - NBB play-limit checks paid **€453,878** 2024; **~€700k** est 2025 = **8.6%** of total budget → total budget class **~€8.14m** (medium derived).
  - FTE **38.3** eoy2024 vs plan **57** (later **32.8** at publication); fee-financed by licensees.
  - **285,783** persons raised online play limits (monthly recheck cost growth).
  - Dual: Justice afd62 special services **55.3m** wider perimeter; FANC fee model; surendettement/EPIS.
- Wrote: sources +1; entity kansspelcommissie; budgets +7; cmt +2; lb +3; FOI gap_ksc_accounts ready; draft; raw AR PDF; rq_294=done; spawn rq_295; ticks=303
- FOI: full KSC P&L human send
- Next: prio5 **rq_295**; deferred **rq_116** SWA

### 2026-07-30T14:45:00Z - tick 304
- Unit: **rq_295** (FOI-adjacent hole-fill - **GBA Gegevensbeschermingsautoriteit AR2024+2025**)
- Found (strong primary GBA Jaarverslag 2024 + 2025):
  - Werkingskredieten **EUR 13.274m (2023) / 15.112.565 (2024) / 15.299.846 (2025)**.
  - Dotatie/toewijzing **14.002m (2024) -> 12.669m (2025)** (-9.5pct); gap filled by carried reserves/boni.
  - Staff **68 eoy2023 / 84 eoy2024 / 96 eoy2025** (+41pct over 2y).
  - Dual digital package: BMA ~9.1m + BIPT ~80m + CCB/COC already mapped.
  - Core GDPR infrastructure (not pure waste); financing mix sustainability note.
- Wrote: sources +1; entity gba_apd; budgets +7; cmt +2; lb +3; FOI gap_gba_accounts_l5 ready; draft; raw ARs; rq_295=done; spawn rq_296; ticks=304
- FOI: GBA L5 P&L + reserve path human send
- Next: prio5 **rq_296** (Federale Ombudsman deepen candidate); deferred **rq_116** SWA

### 2026-07-30T15:15:00Z - tick 305
- Unit: **rq_296** (FOI-adjacent hole-fill - **Federale Ombudsman AR2024 + Kamer 56K0983**)
- Found (strong primary dual):
  - Uitgaven: **6.238m (2023 outturn)** / budget **7.956m (2024)** / **8.238m (2025)** / **8.268m (2026)**.
  - 2024 outturn class **~6.609m** (util **83.07%**); surplus **1.347m** (pers 1.135 + ops 0.185 + cap 0.027).
  - Global boni result 2024 **1.515m**; mechanism: boni year X cofinances year X+2.
  - Dotatie path **6.840 / 7.367 / 6.917 / 6.753m** (2023-26 declining via boni + Moesen freeze).
  - Staff **52** (48 FT); 8 ETP expansion hard to fill (forensic bilingual).
  - Dual Kamer-dotation peers GBA ~15m; FIRM/CTRG/HRJ next.
- Wrote: sources +2; entity fed_ombudsman; budgets +11; cmt +2; lb +3; FOI gap_fed_ombuds_l5_pnl ready; draft; raw AR+Kamer; rq_296=done; spawn rq_297; ticks=305
- FOI: L5 littera P&L + FTE human send
- Next: prio5 **rq_297** (Kamer 56K0983 peer institutions); deferred **rq_116** SWA

### 2026-07-30T15:45:00Z - tick 306
- Unit: **rq_297** (FOI-adjacent hole-fill - **Kamer 56K0983 peer dotatie pack**)
- Found (strong primary Kamer Comptabiliteit DOC 56 0983/001):
  - **Rekenhof**: 2024 exp **64.847m** / 2026 kred **71.0m**; freeze dot **64.563m**; payroll **82%**; Regie fee **2.04m**.
  - **Comite P**: 2026 **14.961m**; pers **93.88%**; late detach billing **1.088m** 2024.
  - **Grondwettelijk Hof**: 2025/26 **14.236 / 14.593m**; dot **13.573m**; staff **96** (admin 57); Regie **238k**.
  - **HRJ/CSJ**: 2026 **7.411m**; dot **6.915m**; surplus 2024 **0.634m**.
  - **Comite I**: 2026 **6.937m**; dot **4.867m** + boni **2.07m**.
  - Pack sum **~114.9m** 2026 (excl GBA/Ombuds/FIRM already mapped).
- Wrote: sources +1; entities +4 + rekenhof update; budgets +28; cmt +6; lb +6; FOI gap_kamer_dotatie_pack_l5 ready; draft; rq_297=done; spawn rq_298; ticks=306
- FOI: consolidated L5 table human send
- Next: prio5 **rq_298** (FIRM/CTRG residual or Raad van State); deferred **rq_116** SWA

### 2026-07-30T16:15:00Z - tick 307
- Unit: **rq_298** (FOI-adjacent hole-fill - **FIRM + CTRG + full Kamer 2026 approved table**)
- Found (strong primary Kamer 56K0983/001 p75 table + narratives):
  - **Full 9 institutions 2026 approved:** kred **EUR 149.280m** / dots **133.134m** (req 153.967 / 137.771).
  - Moesen almost met: dots **+0.78%** / kred **+0.34%** vs 2025 (excl ComiteP late billing).
  - **FIRM:** 2024 kred 4.349m surplus **1.860m**; 2026 approved **5.084m** kred / **3.223m** dots; staff **24** ETP.
  - **CTRG:** surplus 2024 **0.671m**; req **8.340m** cut to approved **6.694m** kred / **6.075m** dots.
  - **GBA refresh:** approved **15.885m** kred / **12.754m** dots 2026.
  - Peers refreshed approved: Rekenhof 71.0; ComiteP 14.27; Hof 14.52; Ombuds 8.27; HRJ 7.37; ComiteI 6.19.
- Wrote: sources +1; entity CTRG + FIRM update; budgets +35; cmt +3; lb +4; FOI gap note update; rq_298=done; spawn rq_299; ticks=307
- FOI: consolidated multi-year still ready human send
- Next: prio5 **rq_299** (Raad van State candidate); **progress@310 in 3 ticks**; deferred **rq_116** SWA

### 2026-07-30T16:45:00Z - tick 308
- Unit: **rq_299** (FOI-adjacent hole-fill - **Raad van State + IBZ-hosted independents**)
- Found (strong primary IBZ Strategisch plan 2025-2029 INI2025 26Jun2025):
  - **Raad van State**: VL **49.978m** / VE **49.971m** 2025 (IBZ-hosted, not Kamer-dotatie).
  - **AIG** police inspectorate: **9.052 / 9.045m**.
  - **OCAD** threat analysis: **4.121 / 4.123m**.
  - Dual finance: RvS ~50m IBZ vs **Grondwettelijk Hof** ~14.5m Kamer-dotatie; dual AIG vs Comite P ~14.3m; dual OCAD vs Comite I ~6.2m.
  - Judicial hosted stack class: RvS+CGVS+RVV **~139m** VE 2025.
- Wrote: sources +1; entities rvs+aig+ocad; budgets +8; cmt +4; lb +4; FOI gap_rvs_accounts_l5 ready; draft; rq_299=done; spawn rq_300 progress@310 + rq_301; ticks=308
- FOI: RvS multi-year L5 human send
- Next: prio5 **rq_301** hole-fill; **rq_300 progress@310** at tick 310; deferred **rq_116** SWA

### 2026-07-30T17:15:00Z - tick 309
- Unit: **rq_301** (FOI-adjacent hole-fill - **Rekenhof federal consultancy 2.52bn**)
- Found (strong primary CoA 2025_39 Oct 2025, survey 137 orgs):
  - Total consultancy **2020-2022: EUR 2.5247bn** incl VAT (~**0.84bn/yr** class).
  - **IT 2.032bn (81%)** / non-IT **0.492bn**; IT IH **576.9m** + external **1.455bn**.
  - Top buyers: **NMBS 465m** / Infrabel **319m** / Finances **185m** / BOSA **134m** / NIRAS **129m** / Smals **126m** / RIZIV **116m**.
  - Cabinets beleidsorganen **6.9m** (85% one Energy minister).
  - Smals external share of omzet **18%->36%** 2014-24; FTE **1395->2072**.
  - No central inventory; no federal strategy (govt Jan 2025 commits to cut).
- Wrote: sources +1; entity fed_consultancy_stack; budgets +14; cmt +2; lb +4; FOI gap_fed_consultancy_annual_post2022 ready; draft; raw CoA PDF; rq_301=done; spawn rq_302; ticks=309
- FOI: annual series 2023-26 human send
- Next: **MANDATORY rq_300 progress@310**; then rq_302; deferred **rq_116** SWA

### 2026-07-30T17:45:00Z - tick 310 (progress milestone)
- Unit: **rq_300** (mandatory progress@310 coverage % + waste top10)
- Coverage vs EUR 347.956 bn TE:
  - **A L0 / B L1:** **100%** strong
  - **C L2:** **~88-96%** (up from ~87-95% @300) � Kamer-dotatie 9-inst pack **149.3m** kred 2026; RvS **~50m** IBZ-hosted dual Hof; CoA consultancy **~0.84bn/yr** class; KSC/GBA/Ombuds mapped
  - **D L5:** **~15-24%** � consultancy top buyers named (NMBS/Infrabel/Finances 3y); ETF EUR FOI residual
  - **E FOI ready:** see progress file (answered ~5)
- Waste top10: **stable** fossil/company cars/cheque TE/EIWT; consultancy high-pi mechanism noted off pure annual top10 unless surpasses
- Inventory: budgets/commitments/leaderboard/entities/sources refreshed in progress file
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log; rq_300=done; ticks=310
- Next: prio5 **rq_302**; deferred **rq_116** SWA; human FOI send stack

### 2026-07-30T18:15:00Z - tick 311
- Unit: **rq_302** (FOI-adjacent hole-fill - **Smals CoA deepen external IT + omzet split**)
- Found (strong primary Rekenhof consultancy 2025 ch5):
  - Smals omzet **573.6m 2024**: SS **62.9% (~361m)** / fed admin **25.4% (~146m)** / other **11.7% (~67m)**.
  - External IT specialists billed to members **>EUR 206m 2024** (ProUnity broker path).
  - Staff Dec2024 **2251** (1143 internal + 1108 detached); IT **77.9%** of headcount.
  - External consultancy share of omzet **17.8%->36%** 2014-24; sole broker bidder risk.
  - **Egov Select**: federal non-SS IT detachments dual Smals; absolute EUR FOI.
- Wrote: sources +1; entity egov_select + smals note; budgets +7; cmt +3; lb +3; FOI gap_egov_select_budget ready; draft; gap_smals note; rq_302=done; spawn rq_303; ticks=311
- FOI: Egov EUR + residual Smals L5 human send
- Next: prio5 **rq_303** (Ypto NMBS IT dual candidate); deferred **rq_116** SWA

### 2026-07-30T18:45:00Z - tick 312
- Unit: **rq_303** (FOI-adjacent hole-fill - **Ypto NMBS IT dual Smals**)
- Found:
  - **Ypto omzet** (strong NBB/Companyweb): **86.5 / 99.5 / 117.0 / 140.2m** 2022-25; FTE **445** 2025; net **4.01m**.
  - **CoA** (strong): NMBS claims all Ypto services **296.7m** as in-house; CoA counts only staff IH **104.2m**; wedge **~192.5m** external via Ypto.
  - Dual: Smals external IT **>206m** 2024; TUC Rail on CoA IT vendor list; NMBS consultancy total **465m** 2020-22.
- Wrote: sources +2; entity ypto; budgets +11; cmt +2; lb +3; FOI gap_ypto_external_l5 ready; draft; rq_303=done; spawn rq_304; ticks=312
- FOI: Ypto external L5 + NMBS recharge human send
- Next: prio5 **rq_304** (TUC Rail dual candidate); deferred **rq_116** SWA

### 2026-07-30T19:15:00Z - tick 313
- Unit: **rq_304** (FOI-adjacent hole-fill - **TUC Rail dual Ypto/Smals**)
- Found (strong NBB/Companyweb + TUC site):
  - Omzet **173.4 / 190.3 / 184.5 / 182.1m** 2022-25; site **184m** 2024.
  - FTE **731** 2025; net **+1.11m 2024 / -2.23m 2025**.
  - Owner **Infrabel 100%**; rail engineering studies (CoA top service provider with Smals/Ypto).
  - Dual stack: Ypto **140m** + TUC **182m** ~**322m** 2025 statutory pair; Smals SS **579m** separate.
- Wrote: sources +1; entity tuc_rail; budgets +9; cmt +2; lb +3; FOI gap_tuc_rail_clients_l5 ready; draft; rq_304=done; spawn rq_305; ticks=313
- FOI: client mix + subcontractors human send
- Next: prio5 **rq_305** (HR Rail deepen dual candidate); deferred **rq_116** SWA

### 2026-07-30T19:45:00Z - tick 314
- Unit: **rq_305** (FOI-adjacent hole-fill - **ETNIC FWB ICT dual Digipolis/Smals/Ypto**)
- Found (strong primary CoA FWB Budget 2024A/2025I + medium RTBF minister):
  - **Recettes** adj2024 **EUR 124.058m** / init2025 **132.841m**.
  - **Liquidation** 124.058m / **143.729m**; **engagement** 180.024m / **200.356m**.
  - Reserve repay to FWB **11.5m** (only OAP type1/2) drives deficit **10.9m** else **+0.6m**.
  - Staff **~380** medium (Galant/RTBF); OAP type1 WBFin II.
  - Dual ICT stack map: Smals **579m** / Digipolis **246m** / ETNIC **124-144m** / Ypto **140m** (not additive TE).
- Wrote: sources +2; entity etnic; budgets +9; cmt +3; lb +3; FOI gap_etnic_l5_vendors ready; draft; raw CoA PDF; rq_305=done; spawn rq_306; ticks=314
- FOI: ETNIC L5 vendors + FTE outturn human send
- Next: prio5 **rq_306** (Cipal Schaubroeck dual Digipolis candidate); deferred **rq_116** SWA


### 2026-07-30T20:15:00Z - tick 315
- Unit: **rq_306** (FOI-adjacent hole-fill - **Cipal Schaubroeck dual Digipolis**)
- Found:
  - **Statutory omzet** (strong NBB/Companyweb): **69.8 / 81.5 / 94.7 / 95.7m** 2022-25; FTE **~376**; net **10.1m 2024 / 2.37m 2025**.
  - **Equity** **28.4m → 14.4m** YE25 (−49pct extraction/sale watch).
  - **Consol** (strong C-smart JV2024): omzet **114.4m**; bedrijfswinst **14.7m**; net **10.5m**; staff **>600**; **276** members.
  - **Sale 2025** to Topicus/TSS (Constellation): acquirer claim **~110m** gross rev 2024 medium.
  - Dual: Digipolis public AGB **~246m** vs Cipal commercial Flanders-wide **114m** consol.
- Wrote: sources +3; entities cipal_schaubroeck+cipal_dv; budgets +15; cmt +3; lb +4; FOI gap_cipal_l5_clients_sale ready; draft; raw JV PDF; rq_306=done; spawn rq_307; ticks=315
- FOI: client L5 + sale proceeds human send (private NV limits noted; Cipal dv primary)
- Next: prio5 **rq_307** (HR Rail deepen dual candidate); deferred **rq_116** SWA


### 2026-07-30T20:45:00Z - tick 316
- Unit: **rq_307** (FOI-adjacent hole-fill - **HR Rail dual deepen via Infrabel AR2024**)
- Found:
  - **HR Rail** refresh (strong-medium Companyweb/NBB): omzet **2.078/2.206/2.305/2.368 bn** 2022-25; FTE **27.4k-27.8k**; net **1.57m** 2025.
  - **Infrabel AR2024 strong:** YE FTE **9,402.1** (9,536 YE2023); avg FTE salary **8,966** 2024.
  - **Payroll under Services** **EUR 809.61m** 2024 / **775.76m** 2023 (HR re-invoice path).
  - Implied residual NMBS class: FTE **~18.2k**; omzet share **~1.50 bn** (medium residual).
  - Infrabel owns **49%** HR Rail; group ~10k employees note.
- Wrote: sources +2; entity hr_rail note; budgets +10; cmt +1; lb +3; FOI gap_hr_rail update partial; draft refresh; raw AR PDF; rq_307=done; spawn rq_308; ticks=316
- FOI: official NMBS matrix + free NBB PDF still ready human send
- Next: prio5 **rq_308** (NMBS FTE dual HR candidate); deferred **rq_116** SWA


### 2026-07-30T21:15:00Z - tick 317
- Unit: **rq_308** (FOI-adjacent hole-fill - **NMBS FTE dual HR Rail recon**)
- Found:
  - **NMBS ops headcount** (strong official): **16,976** on 2026-01-01 after **1100+** hires 2025.
  - **NMBS statutory FTE = 0** (strong Companyweb/NBB) — all legal employment via HR Rail.
  - Dual map: NMBS **16,976** + Infrabel YE **9,402** = **26,378** vs HR **27,811** residual **~1.4k** class (HR admin + FTE/headcount/date mix).
  - EUR residual: NMBS payroll-share class **~€1.50 bn** of HR **€2.305 bn** 2024 (after Infrabel **€809.6m** services).
  - Unit-cost class ~**€86–88k**/head both sides (method-sensitive medium).
- Wrote: sources +2; entity nmbs note; budgets +6; cmt +1; lb +3; FOI gap_hr_rail update; draft table; rq_308=done; spawn rq_309; ticks=317
- FOI: NMBS official payroll EUR charge series still ready human send
- Next: prio5 **rq_309**; **progress@320 in 3 ticks**; deferred **rq_116** SWA


### 2026-07-30T21:45:00Z - tick 318
- Unit: **rq_309** (FOI-adjacent hole-fill - **AGMJ ETP + FWB DO11 traitements Expose 2026**)
- Found (strong primary Expose general depenses FWB 2026):
  - **AGMJ 801 ETP** 30/06/2025 (102+535+149+15); AGAJ **2,018**; admin total **6,427**.
  - **DO11 AB 11.03+11.04 traitements 437.6m** BI2026 (+10.9m vs init2025) ministry-wide.
  - New: AGMJ+AGAJ **5.4m** + MDJ carceral **3.4m**; partner non-index **−449k**; formation cuts **−321k** class.
  - ETNIC moyens BI2026 **123m** (119.4→123; perimeter may differ CoA full recettes).
  - Residual: AGMJ-only wage cash stock still FOI (not invent pro-rata of 437.6m).
- Wrote: sources +1; entities agmj + notes; budgets +9; cmt +1; lb +3; FOI draft+queue update; raw PDF; rq_309=done; spawn rq_310 progress@320 + rq_311; ticks=318
- FOI: AGMJ wage cash residual ready human send
- Next: prio5 **rq_311** hole-fill; **rq_310 progress@320** in 2 ticks; deferred **rq_116** SWA


### 2026-07-30T22:15:00Z - tick 319
- Unit: **rq_311** (FOI-adjacent hole-fill - **Rail Facilities dual HR Rail**)
- Found (strong NBB/Companyweb KBO 0403.265.325):
  - Omzet **11.28 / 13.83 / 13.87 / 14.84m** 2022-25; net **0.11m** 2025; equity **11.0m**.
  - **FTE 0** statutory (same dual-employer pattern as NMBS).
  - Infrabel **49%** stake via HR Rail path; staff procurement/welfare vehicle.
  - Completes dual rail map note: HR 2.37bn + NMBS 17k/FTE0 + Infrabel 9.4k + Ypto/TUC + RailFac 15m.
- Wrote: sources +1; entity rail_facilities; budgets +8; cmt +1; lb +2; FOI gap_rail_facilities_l5 ready; draft; rq_311=done; spawn rq_312; ticks=319
- FOI: activity L5 low-medium prio human send
- Next: **MANDATORY rq_310 progress@320**; then rq_312; deferred **rq_116** SWA


### 2026-07-30T22:45:00Z - tick 320 (progress milestone)
- Unit: **rq_310** (mandatory progress@320 coverage % + waste top10)
- Coverage vs EUR 347.956 bn TE:
  - **A L0 / B L1:** **100%** strong
  - **C L2:** **~89-96%** (up from ~88-96% @310) — public ICT dual Smals/Digipolis/ETNIC/Cipal/Ypto; rail dual HR 2.37bn + NMBS 16976/FTE0 + Infrabel 9402 + payroll 810m + RailFac 15m; AGMJ 801 ETP + DO11 437.6m
  - **D L5:** **~16-25%** — consultancy/Ypto/Smals external mechanisms; ASBL bulk residual
  - **E FOI ready:** **~138** (answered ~5)
- Waste top10: **stable** fossil/company cars/cheque TE/EIWT; dual ICT+rail high-mechanism noted off pure annual top10
- Inventory: budgets ~3917 / cmt ~600 / lb ~704 / entities ~273 / sources ~614
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log; rq_310=done; ticks=320
- Next: prio5 **rq_312**; deferred **rq_116** SWA; human FOI send stack ~138 ready


### 2026-07-30T23:15:00Z - tick 321
- Unit: **rq_312** (FOI-adjacent hole-fill - **Egov Select dual Smals institutional EUR**)
- Found (strong NBB/Companyweb KBO 0475.479.251):
  - Omzet **73.0 / 71.4 / 92.0 / 111.9m** 2021-24 (+22pct 2024).
  - FTE **544.6 / 660.8 / 772.4 / 907.7** (rapid +67pct 2021-24).
  - Net **1.28m** 2024; equity **8.37m**.
  - Dual: Smals **~579m** SS-focused vs Egov federal detachments **112m**; not additive.
  - Closes institutional EUR residual of gap_egov_select_budget; L5 client FODs still FOI.
- Wrote: sources +1; entity egov_select update; budgets +12; cmt +1; lb +3; FOI gap update+draft; rq_312=done; spawn rq_313; ticks=321
- FOI: top FOD recharges residual ready human send
- Next: prio5 **rq_313**; deferred **rq_116** SWA


### 2026-07-30T23:45:00Z - tick 322
- Unit: **rq_313** (FOI-adjacent hole-fill - **ASTRID statutory dual IBZ toelage wedge**)
- Found (strong NBB/Companyweb KBO 0263.893.151):
  - Omzet **23.6 / 25.9 / 26.2 / 27.2m** 2022-25; net **~14-15m**/yr; equity **€167m** YE2025.
  - FTE **136**; negative brutomarge **−€25.7m** 2025 (other income residual).
  - **Triple wedge:** IBZ toelage **€76.5m** vs contract ops **€46.5m** vs statutory omzet **€27.2m**.
  - Closes annual accounts residual of gap_astrid; cash recon of three perimeters still FOI.
- Wrote: sources +1; entity astrid update; budgets +12; cmt +1; lb +3; FOI gap+draft update; rq_313=done; spawn rq_314; ticks=322
- FOI: triple recon residual ready human send
- Next: prio5 **rq_314**; deferred **rq_116** SWA


### 2026-07-31T00:15:00Z - tick 323
- Unit: **rq_314** (FOI-adjacent hole-fill - **skeyes 2025 statutory dual airports**)
- Found (strong NBB/Companyweb KBO 0206.048.091):
  - Omzet **306.1 / 309.6 / 335.2 / 352.9m** 2022-25 (+5.3pct 2025).
  - Net **18.8 / 9.1 / 15.8 / 18.6m**; equity **281 → 328m**.
  - FTE **894.5 → 966.3**.
  - Closes 2025 full statutory residual of gap_skeyes; dual BAC/BSCA prior.
  - Residual FOI: RP3 correction cash + unit rates multi-year + CAPEX.
- Wrote: sources +1; entity skeyes update; budgets +12; cmt +1; lb +2; FOI gap+draft update; rq_314=done; spawn rq_315; ticks=323
- FOI: RP3/unit-rate residual ready human send
- Next: prio5 **rq_315**; deferred **rq_116** SWA


### 2026-07-31T00:45:00Z - tick 324
- Unit: **rq_315** (FOI-adjacent hole-fill - **Nationale Loterij statutory dual private gambling**)
- Found (strong NBB/Companyweb KBO 0223.967.357 + official press 16 Jan 2026):
  - Omzet **1493.7 / 1489.6 / 1554.7 / 1666.5m** 2022-25 (+7.2pct 2025 record).
  - Net **9.85 / 6.50 / 1.20 / 8.01m** (thin residual after society transfers).
  - Equity **231 ? 237m**; FTE **422 ? 447**.
  - Prizes paid **�1.266bn** 2025; retail **1172m** / online **494m**.
  - Society return **�362.5m** after 2024 results; hope **�370m** for 2025; **1970** projects.
  - Dual: state lottery monopoly vs private gambling (Kansspelcommissie); prior FNRS/IEFH lottery lines.
- Wrote: sources +2; entity nationale_loterij; budgets +17; cmt +1; lb +2; FOI gap_natlot_society_l5 ready; draft; rq_315=done; spawn rq_316; ticks=324
- FOI: L5 society return split + reconcilatie thin net vs ~363m ready human send
- Next: prio5 **rq_316**; deferred **rq_116** SWA

### 2026-07-31T01:15:00Z - tick 325
- Unit: **rq_316** (FOI-adjacent hole-fill - **Proximus Group 2025 dual SFPIM majority telecom**)
- Found (strong official Proximus FY2025 press 27 Feb 2026 + shareholder structure):
  - Group reported rev **�6,539m ? �6,620m** 2024-25 (+1.2%); underlying **�6,430m ? �6,307m**.
  - Domestic EBITDA **�1,699m** 2025; Global EBITDA **�170m**.
  - Net Group share **�447m ? �398m** (-11%; Global GW impairment).
  - CapEx **�1,249m**; organic FCF **�130m** (reported FCF 480m).
  - Dividend proposed **�0.60/share**; SFPIM **~53.5% capital / ~56% voting** (180.9m shares).
  - Fiber **2.604m** homes (~42% coverage); dual private Orange/Telenet + SFPIM federal holding.
- Wrote: sources +2; entity proximus; budgets +15; cmt +1; lb +2; FOI gap_proximus_sfpim_dividend_l5 ready; draft; rq_316=done; spawn rq_317; ticks=325
- FOI: SFPIM dividend cash multi-year + any public co-financing residual ready human send
- Next: prio5 **rq_317**; deferred **rq_116** SWA

### 2026-07-31T01:45:00Z - tick 326
- Unit: **rq_317** (FOI-adjacent hole-fill - **Bnode/bpost 2025 dual Proximus listed state SOE**)
- Found (strong official Bnode press 6 Mar 2026 + AR2025 key figures):
  - Op income **�4,341.3m ? �4,482.3m** 2024-25 (+3.2%; Staci full year).
  - Adj EBIT **�224.9m ? �179.7m** (high end of ~180m guidance).
  - Reported **net loss �39.4m** (one-offs �55.5m + Staci interest); adj result still **+�51.0m**.
  - **No dividend** 2025; Belgian State via SFPIM **51.04%** (102.1m shares).
  - BU: Bpost last-mile adj EBIT **�67.0m** (mail -10% parcels +2%); Paxon **�58.6m**; Landmark **�85.3m**.
  - Rebrand **bpostgroup ? Bnode**; 8th management contract under negotiation; dual Proximus listed majority-state SOE.
  - Prior SGEI **�227.8m 2024** still residual for 2025 cash FOI.
- Wrote: sources +2; entity bpost update; budgets +10; cmt +1; lb +2; FOI gap_bpost_sgei_2025_mgmt8 ready; draft; rq_317=done; spawn rq_318; ticks=326
- FOI: SGEI 2025 cash + 8th contract envelope ready human send (alongside prior gap_bpost_uso_split)
- Next: prio5 **rq_318**; deferred **rq_116** SWA

### 2026-07-31T02:15:00Z - tick 327
- Unit: **rq_318** (FOI-adjacent hole-fill - **federal culture triple BOZAR/Monnaie/NOB dual communities**)
- Found (strong Kamer 56K0856/016 24 Apr 2025 + NBB/Companyweb BOZAR):
  - Federal dots 2024/init2025: **BOZAR �15.529m / �15.798m**; **Monnaie �42.173m / �42.957m**; **NOB �10.896m / �11.094m**.
  - Sum **�68.598m ? �69.850m** (pre 1.8% linear cut review).
  - Nationale Loterij provisional 2024: BOZAR **�3.095m**; Monnaie **�1.489m**; NOB **�1.484m** (sum **�6.067m**).
  - BOZAR statutory omzet **�5.90 / 7.30 / 8.16 / 8.95m** 2022-25; net **�0.42m**; equity **�50.8m**; FTE **227**.
  - Management contracts expired **31 Dec 2024**; renewals planned 2025; dual community culture stacks.
- Wrote: sources +2; entities +3; budgets +19; cmt +1; lb +2; FOI gap_fed_culture_contracts_2025 ready; draft; rq_318=done; spawn rq_319; ticks=327
- FOI: post-cut 2025 cash + new management contracts ready human send
- Next: prio5 **rq_319**; deferred **rq_116** SWA

### 2026-07-31T02:45:00Z - tick 328
- Unit: **rq_319** (FOI-adjacent hole-fill - **Belnet NREN 2024 dual Smals research ICT**)
- Found (strong Belnet AR2024 budgetary results + general accounts primary):
  - P&L exp/income **€17.3 / 23.0 / 35.0m** 2022-24.
  - Services invoiced **€7.95 / 7.86 / 10.75m**; institutional transfer **€9.34 / 14.62 / 23.73m**.
  - Remuneration **€7.76m** 2024; total assets **€42.2m**; net assets **€10.6m**.
  - Budget exp **€27.3m** 2024; FedWAN fund **€2.69m**; FedOSC fund **€1.84m**.
  - Dual: research/education NREN vs Smals SS/federal ICT (~€579m); BNIX peaks public.
- Wrote: sources +1; entity belnet; budgets +16; cmt +1; lb +2; FOI gap_belnet_2025_l5 ready; draft; rq_319=done; spawn rq_320; ticks=328
- FOI: 2025 accounts + member L5 + FedWAN multi-year ready human send
- Next: prio5 **rq_320**; **progress@330 in 2 ticks**; deferred **rq_116** SWA

### 2026-07-31T03:15:00Z - tick 329
- Unit: **rq_320** (FOI-adjacent hole-fill - **BELSPO federal science dual community research**)
- Found (strong FRWB/CFPS advisory 30 Jan 2025 + Kamer 56K0827/001):
  - BELSPO managed budget **~€570m** current (FRWB) / **€630m 2024** class (resolution).
  - Split: ESA/international **~57%** (floor **>€250m**); FWI base financing **~25%**; national RDI **~13%**.
  - Coalition specific cut **€93m (−15%)** on department; resolution notes plan **>20%** class.
  - 10 FWI + Belnet **>2400** staff; heritage value class **€3.5bn**; museums **1.5m** visitors/yr.
  - Federal RDI fiscal incentives **€2.0–2.2bn** class (FPS Finance; off BELSPO cash).
  - Dual: federal science/museums vs community university research; Belnet filled prior tick.
- Wrote: sources +2; entity belspo; budgets +7; cmt +1; lb +2; FOI gap_belspo_fwi_l5_cut ready; draft; rq_320=done; spawn rq_321 progress@330; ticks=329
- FOI: FWI L5 envelopes + post-cut path ready human send
- Next: **MANDATORY rq_321 progress@330**; deferred **rq_116** SWA

### 2026-07-31T03:45:00Z - tick 330 (progress milestone)
- Unit: **rq_321** (mandatory progress@330 coverage % + waste top10)
- Coverage vs EUR 347.956 bn TE:
  - **A L0 / B L1:** **100%** strong
  - **C L2:** **~90-97%** (up from ~89-96% @320) — listed SOE dual Proximus €6.62bn + Bnode/bpost €4.48bn; Nationale Loterij €1.67bn; federal culture triple ~€70m; Belnet €35m; BELSPO ~€570-630m
  - **D L5:** **~16-26%** — lottery society / SFPIM dividend / Belspo FWI / bpost SGEI mechanisms FOI-adjacent; ASBL bulk residual
  - **E FOI ready:** **~145** (answered ~5; total rows ~151)
- Waste top10: **stable** fossil/company cars/cheque TE/EIWT; commercial SOE rev + culture + science cut path noted off pure annual top10
- Inventory: budgets ~4036 / cmt ~609 / lb ~724 / entities ~280 / sources ~611
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log; rq_321=done; spawn rq_322; ticks=330
- Next: prio5 **rq_322**; deferred **rq_116** SWA; human FOI send stack ~145 ready

### 2026-07-31T04:15:00Z - tick 331
- Unit: **rq_322** (FOI-adjacent hole-fill - **Belgium ESA contribution dual Belspo space**)
- Found (strong BELSPO MERI Statistics in Brief No. 8, 2025):
  - BE ESA contribution **~€190m 2015 → €284m 2025**; avg **~€194m** 2021-24 (vs €179m 2016-20 / €156m 2011-15).
  - Of avg 2021-24: private industry **€148.2m**; public research **€23.1m**; universities **€22.7m**.
  - Private space turnover **€713.5m** 2024 (multiplier ~6x); ESA-backed **4,016 FTE** (2,257 R&D).
  - ~**90%** of federal public space funding via ESA; geo-return principle.
  - CM25 press: **€1.109bn / 5y** pledge class (medium).
  - Closes major Belspo ESA residual of gap_belspo; optional/L5 still FOI.
- Wrote: sources +2; entity esa_be_contrib + belspo note; budgets +11; cmt +1; lb +2; FOI gap_esa_be_optional_l5 ready; draft; rq_322=done; spawn rq_323; ticks=331
- FOI: optional vs mandatory + top20 beneficiaries ready human send
- Next: prio5 **rq_323**; deferred **rq_116** SWA

### 2026-07-31T04:45:00Z - tick 332
- Unit: **rq_323** (FOI-adjacent hole-fill - **RV Belgica II federal marine research dual Belspo**)
- Found (strong BELSPO NewRV timeline + financing study class):
  - CM **28 Oct 2016** budget **€54.45m** (incl VAT) for replacement vessel.
  - CM **22 Dec 2017** award Freire Shipyard (Vigo) **€53.7m**.
  - Launch press **11 Feb 2020**: project cost **~€54m** VAT included.
  - Delivery Zeebrugge **Dec 2021**; baptism **25 Jun 2022** (Princess Elisabeth).
  - Operator **Genavir** (FR oceanographic fleet) from **Nov 2021**.
  - Financing study class ops **€4.3m/yr** for **300 days** (2 crews) — medium, not outturn.
  - Dual: BELSPO ownership + RBINS science + Defence base; complementary **VLIZ Simon Stevin**.
- Wrote: sources +3; entity rv_belgica (+belspo note); budgets +4; cmt +1; lb +1; FOI gap_belgica_ops_l5 ready; draft; rq_323=done; spawn rq_324; ticks=332
- FOI: CAPEX cash path + Genavir ops L5 ready human send
- Next: prio5 **rq_324**; deferred **rq_116** SWA

### 2026-07-31T05:15:00Z - tick 333
- Unit: **rq_324** (FOI-adjacent hole-fill - **BELSPO AR2024 budget L2 primary split**)
- Found (strong BELSPO Jaarverslag 2024 figures page):
  - Budgettaire realisaties **€582.4m** 2024 (tightens prior 570-630m class).
  - Space **€283.4m** (~half; dual ESA MERI €284m 2025).
  - ADBA+ION (FWI Belnet Polar Cinematek) **€162.6m** (>25%).
  - Mgmt organs **€19.4m** (3%; personnel **€16.9m**).
  - Nat+int RDI **€56.5m** (~10%); PRT ending 2024 **€15.7m**.
  - Diverse subsidies ex-space ~10% (SCK Myrrha VKI nuclear/H2 class).
  - EU research fund prog5 **€26.9m** exp 2024 (extra federal budget).
  - Museums **>1.5m** visitors 2024.
- Wrote: sources +1; budgets +8; cmt +1; lb +1; entity belspo note; FOI gap_belspo refresh; draft note; rq_324=done; spawn rq_325; ticks=333
- FOI: FWI L5 per institute + cut path still ready human send
- Next: prio5 **rq_325**; deferred **rq_116** SWA

### 2026-07-31T05:45:00Z - tick 334
- Unit: **rq_325** (FOI-adjacent hole-fill - **BELSPO P4Science FSI L5 project envelopes**)
- Found (strong BELSPO P4Science Information File call 2024-2025 primary PDF):
  - CM **9 Feb 2024** approved multi-year P4Science (Policy for Science) for FSI.
  - Call indicative total **€15.261.890** covering two budget years.
  - Competitive **20%**: **€2.852.380** all FSI (+**€250k** already committed to international calls).
  - Non-competitive **80%**: **€12.394.510** allocated by FSI (repartition key 10 BELSPO-FSI; flat rate Sciensano/NICC/WHI).
  - Largest non-comp: **KBIN €1.883m** · **ARA €1.696m** · **KMMA €1.221m** · **KIK €1.186m** · **BIRA €1.152m**.
  - Smaller: KBS 1.098 · KMKG 0.963 · KMI 0.959 · KMSKB 0.595 · Sciensano 0.564 · KBR 0.555 · NICC 0.393 · WHI 0.131.
  - **Project R&D only** — not base ADBA+ION €162.6m financing (residual FOI).
  - Dual: federal FSI projects vs community FWO/FNRS (~€450m / ~€250m class prior ticks).
- Wrote: sources +1; entity p4science_belspo + belspo note; budgets +17; cmt +1; lb +1; FOI gap_belspo refresh; draft note; rq_325=done; spawn rq_326; ticks=334
- FOI: base FWI cash-by-year + cut 93m path still ready human send (project L5 partial closed)
- Next: prio5 **rq_326**; deferred **rq_116** SWA

### 2026-07-31T06:15:00Z - tick 335
- Unit: **rq_326** (FOI-adjacent hole-fill - **FED-tWIN dual FSI-university + DIGIT-04 + climate RDI**)
- Found (strong BELSPO FED-tWIN page + RMAH strategy + climat.be inventory):
  - **FED-tWIN**: **125** research profiles (5 batches x 25, 2019-2024); 100% fund 5y then 50% next 5y.
  - Rates (RMAH cites BELSPO): **€125k/yr** first 5y → **€75k/yr** next 5y; ~**€1m/profile** 10y class; programme **~€125m** full-path medium class (staggered FOI).
  - Climate FedTwin subset: **13** projects **€9.25m** 2020-26 (strong).
  - **DIGIT-04** 2019-24: **€37.63m** all 10 FSI + Cinematek; RMAH ~€380k/yr class.
  - Climate portfolio: **€39.2m** 2019-27 / **€32.9m** 2022-26 (BRAIN-P1 11.7; STEREO 7; ESA Climate+DTE 9; Polar 1.67; BELGICA 2.0).
  - Dual: FSI↔11 universities NL/FR; heritage digitisation dual community.
- Wrote: sources +3; entities +2; budgets +15; cmt +3; lb +3; FOI gap_fedtwin + gap_digit04 ready drafts; rq_326=done (seeded); spawn rq_327; ticks=335
- FOI: FED-tWIN cash+profiles L5 and DIGIT FSI L5 ready human send
- Next: prio5 **rq_327**; deferred **rq_116** SWA

### 2026-07-31T06:45:00Z - tick 336
- Unit: **rq_327** (FOI-adjacent hole-fill - **S4Policy Policy Driven + PROBA-3 BE space dual**)
- Found (strong BELSPO S4Policy InfoFile v6 + AR2024 PROBA-3 PDF):
  - **S4Policy Policy Driven** 4-call total **€34.256.160** (2024-2031).
  - Call1 **€6.155.110** · Call2 **€7.951.700** · Call3 **€8.791.270** · Call4 **€11.358.080**.
  - Cofund: BELSPO max **90%** / federal depts min **10%**; dual research community + depts.
  - Themes: Digital / Strategic autonomy / Inclusion-health / Green-societal.
  - Dual with **P4Science** €15.26m FSI capacity (prior tick).
  - **PROBA-3**: mission **€166m** of which Belgium **€63.4m** via BELSPO **GSTP+PRODEX**; launch **4 Dec 2024**.
  - Industrial dual: Redwire SPACEBEL CSL ROB; ESA formation flying + solar corona.
- Wrote: sources +2; entities +2; budgets +7; cmt +2; lb +2; FOI gap_s4policy + gap_proba3 ready drafts; rq_327=done; spawn rq_328; ticks=336
- FOI: S4Policy awards L5 + PROBA-3 GSTP/PRODEX cash ready human send
- Next: prio5 **rq_328**; deferred **rq_116** SWA

### 2026-07-31T07:15:00Z - tick 337
- Unit: **rq_328** (FOI-adjacent hole-fill - **STEREO IV Earth observation dual community RS**)
- Found (strong BELSPO STEREO IV InfoFile call 2025 + EO portal):
  - CM **22 Nov 2019** approved multi-annual STEREO IV **2022-2029**.
  - Programme budget **€28.15m**.
  - Call 2025 thematic network projects tentatively **~€7.4m** (subject to final budget).
  - Eighth EO phase since 1985 (TELSAT/STEREO I–III continuity).
  - Dual: partnerships **highly recommended** both Flemish and French community teams; foreign teams max **20%** of project budget.
  - Themes: climate EO · hazards · biodiversity/health · green cities.
- Wrote: sources +2; entity stereo_iv; budgets +3; cmt +1; lb +1; FOI gap_stereo_iv ready draft; rq_328=done (seeded); spawn rq_329; ticks=337
- FOI: awards + cash path vs 28.15m ready human send
- Next: prio5 **rq_329**; deferred **rq_116** SWA

### 2026-07-31T07:45:00Z - tick 338
- Unit: **rq_329** (FOI-adjacent hole-fill - **BE ESA CM25 multi-year space dual Belspo+Defence**)
- Found (strong BELSPO CM-ESA Bremen 2025 debrief primary PDF):
  - BE total space **2025-2030**: **€1.845bn** = 1.277 base + **168 MoD ESA** + **400 one-off** (~**€369m/y**).
  - ESA share class **~€335m/y**; intergov Eumetsat/ECMWF/ESO ~25m/y; EU/bilat/nat ~10m/y.
  - BE ESA CM25 subscription **€1.109bn** incl MoD (5.06% of ESA €22.07bn); prior CM22 €946.86m.
  - Inéluctables **€1.050bn**; new ESA commits **€934m** (836m for 2026-30).
  - PRODEX **€99m** (24 uncond + 75 cond); GSTP **€103.9m** (79.9 TBA); Science **€106.4m**; Basic **€52.2m**.
  - MoD invest programmes space **2026-2034 €617m**; dual NATO-accountable constraint.
  - Some TBA/conditional need BE CM confirm by **31 Jan 2026**.
- Wrote: sources +1; entity esa_cm25_be; budgets +15; cmt +2; lb +3; FOI gap_be_space_cm25 ready; rq_329=done; spawn rq_330; ticks=338
- FOI: cash-by-year civil vs MoD + TBA confirmation ready human send
- Next: prio5 **rq_330**; **progress@340 in 2 ticks**; deferred **rq_116** SWA

### 2026-07-31T08:15:00Z - tick 339
- Unit: **rq_330** (FOI-adjacent hole-fill - **EUMETSAT Belgium dual intergov meteo space**)
- Found (strong EUMETSAT Annual Report 2024 audited accounts extract):
  - Belgium Member State contribution **€13.480m** 2024 (table 13.480 kEUR).
  - Total MS contributions **€506.037m**; BE share **~2.66%**.
  - EUMETSAT expenditure budgets 2024 total **€763.2m** (EPS-SG 254.3 · MTG 219.1 · Copernicus 111.4 · GB 91 · EPS 37.4 · DestinE 24.3 · MSG 23.3 · Jason-CS 2.4).
  - Dual: KMI/IRM meteorological user + BELSPO intergov space path.
  - Aligns CM25 intergov class **~€25m/y** (EUMETSAT + ECMWF + ESO); residual ECMWF/ESO FOI.
- Wrote: sources +1; entity eumetsat_be; budgets +4; cmt +1; lb +1; FOI gap_be_intergov ready; rq_330=done; spawn rq_331 progress@340; ticks=339
- FOI: ECMWF+ESO cash residual ready human send
- Next: **MANDATORY rq_331 progress@340**; deferred **rq_116** SWA

### 2026-07-31T08:45:00Z - tick 340 (progress milestone)
- Unit: **rq_331** (mandatory progress@340 coverage % + waste top10)
- Coverage vs EUR 347.956 bn TE:
  - **A L0 / B L1:** **100%** strong
  - **C L2:** **~91-98%** (up from ~90-97% @330) — BELSPO AR2024 **€582.4m** L2; BE space CM25 **€1.845bn** 2025-30 dual MoD; EUMETSAT **€13.48m**; prior SOE/lottery/culture/Belnet
  - **D L5:** **~16-27%** — P4Science 15.26m FSI; FED-tWIN; S4Policy 34.26m; STEREO IV 28.15m; PROBA-3 BE 63.4m; climate 39.2m; awards/cash FOI residual
  - **E FOI ready:** **~153** (answered ~5; total rows ~160)
- Waste top10: **stable** fossil/company cars/cheque TE/EIWT; multi-year space packages + Belspo programmes noted off pure annual top10
- Inventory: budgets ~4121 / cmt ~622 / lb ~739 / entities ~290 / sources ~644
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log; rq_331=done; spawn rq_332; ticks=340
- Next: prio5 **rq_332**; deferred **rq_116** SWA; human FOI send stack ~153 ready

### 2026-07-31T09:15:00Z - tick 341
- Unit: **rq_332** (FOI-adjacent hole-fill - **VAF Flanders dual community AV fund**)
- Found (strong VAF Jaarverslag 2024 + 2025 primary):
  - **2024 VL dots:** Film Culture **€20.490m** · Media **€7.450m** · Game **€2.768m** → **€30.708m**.
  - Filmfonds total budget **€20.535m** (creatie **€11.753m**: fictie 7.753 / doc 1.575 / anim 1.575); spend **€21.576m**.
  - Mediafonds available **€8.894m** (incl dienstenverdelers/OTT **€0.781m**); spend **€8.554m**.
  - **2025 VL dots:** Film **€20.820m** · Media **€7.173m** · Game **€2.800m** → **€30.793m**.
  - Dual: Flanders VAF vs Wallonia CCA vs federal CINEMATEK (Belspo); Screen Flanders tax-shelter class separate.
- Wrote: sources +2; entity vaf; budgets +14; cmt +1; lb +1; FOI gap_vaf_cca ready; rq_332=done; spawn rq_333; ticks=341
- FOI: CCA dual + Cinematek base + VAF top awards L5 ready human send
- Next: prio5 **rq_333**; deferred **rq_116** SWA

### 2026-07-31T09:45:00Z - tick 342
- Unit: **rq_333** (FOI-adjacent hole-fill - **CCA FWB dual AV vs VAF Flanders**)
- Found (strong FWB CCA Bilan 2024 official):
  - Global AV envelope **>€44m** 2024 (was **€43.15m** 2023).
  - **FWB €26.6m** + editors/distributors **€17.4m** (RTBF **€5.8m** + private **€11.6m** SMA legal investment).
  - Commission du Cinéma promises **€13.24m**; Commission Séries **€1.635m** (first year); opérateurs **€4.198m**; promo **€0.712m**.
  - Tax shelter raised **€84.73m** (+14% vs 2023) — investor money not CCA budget.
  - Europe Creative MEDIA BE projects **€9.4m**.
  - Dual: VAF Flanders VL dots **~€30.7m** same class; federal CINEMATEK residual FOI.
- Wrote: sources +1; entity cca_fwb; budgets +13; cmt +1; lb +2; FOI gap_vaf_cca refresh; rq_333=done; spawn rq_334; ticks=342
- FOI: named awards L5 + Cinematek still ready human send
- Next: prio5 **rq_334**; deferred **rq_116** SWA

### 2026-07-31T10:15:00Z - tick 343
- Unit: **rq_334** (FOI-adjacent hole-fill - **Federal Tax Shelter AV TE dual VAF/CCA culture**)
- Found (strong FPS Finance Inventory of Federal Tax Expenditures 2024 / 2026 PDF):
  - Tax shelter **audiovisual** Art.194ter CIT TE multi-year: **€212.15m 2023** (204.38 2022; 183.73 2021; 173.36 2020).
  - Reform spike post-2014: **€7.44m 2014 → €191.41m 2015**.
  - **Scenic/performing arts** extension: **€41.82m 2023** (21.88 2022).
  - **Video games** extension: **€1.33m 2023** (0.20 2022).
  - **Package 2023: €255.3m** (AV+scenic+games).
  - Dual culture stack: VAF VL dots ~€30.7m + CCA envelope >€44m + federal TE; CCA raised investor cash €84.73m 2024 is **different metric** from TE revenue-forgone.
- Wrote: sources +1; entity tax_shelter_av; budgets +31 series; tax_expenditures +4; cmt +1; lb +2; FOI gap_taxshelter L5 ready; rq_334=done; spawn rq_335; ticks=343
- FOI: top beneficiaries L5 ready human send
- Next: prio5 **rq_335**; deferred **rq_116** SWA

### 2026-07-31T10:45:00Z - tick 344
- Unit: **rq_335** (FOI-adjacent hole-fill - **Wallimage + Screen Flanders dual economic AV**)
- Found (strong Wallimage Bilan 2024/2025 PDF + VAF Screen Flanders page + Gaming page):
  - **Wallimage Coproductions invest:** **€7.0948m** 2024 (49 projects) · **€6.686m** 2025 (47 projects).
  - **Walloon spend generated:** **€46.232m** 2024 (~652%) · **€51.436m** 2025 (**769%** record).
  - **Wallimage Entreprises:** **€3.720m** (12 deals 2024) · **€4.191m** (19 deals 2025); stock **€13.59m** EOY24 → **€10.23m** EOY25.
  - **Production volant** capacity **€6.5m/yr** since 2018; **Gaming** FY2026 budget **€2.0m**.
  - **Screen Flanders:** VLAIO Hermes **€3.5m/yr**; max **€400k** recoupable advances; VAF admin.
  - Dual stack: economic (Wallimage~€10.8m + SF €3.5m) on top of culture (VAF ~€30.7m + CCA >€44m) + federal Tax Shelter TE.
- Wrote: sources +4; entities +2; budgets +15; cmt +2; lb +3; FOI gap_wallimage_sf_econ_l5 ready; rq_335=done; spawn rq_336; ticks=344
- FOI: named awards L5 both funds + Hermes cash path ready human send
- Next: prio5 **rq_336**; deferred **rq_116** SWA

### 2026-07-31T11:15:00Z - tick 345
- Unit: **rq_336** (FOI-adjacent hole-fill - **screen.brussels triple economic AV**)
- Found (strong primary screen.brussels Bilan 2025 + 2024 nutshell + Results 2023 + CineRegio):
  - **2025:** nearly **€3m** / allocated **€2.9m** in **26** projects; claimed return **€27.3m**; ratio **9.2x** (2016-2025).
  - Format split 2025 of €2.9m: LM 37% · anim 30% · series 30% · doc 3%.
  - **2024:** **€3.0m** in **27** projects; claimed return **€34.122m**; ratio **9.5x**.
  - **2023:** **>€3m** / available **€3.1m** in **29** projects; claimed **≥€24m** spend; apps **€6.3m**.
  - CineRegio: annual **€3m**; max **€500k** refundable advances; min BCR spend **€250k**.
  - **Triple economic AV 2024-class ~€17.3m:** Wallimage Coprod+Ent ~€10.8m + Screen Flanders €3.5m + screen.brussels €3.0m (not TE-additive).
  - Stack still separate: culture VAF ~€30.7m + CCA >€44m + federal Tax Shelter TE.
- Wrote: sources +5; entity screen_brussels; budgets +10; cmt +1; lb +2; FOI gap_screen_brussels_l5 ready; rq_336=done; spawn rq_337; ticks=345
- FOI: named awards L5 + BCR budget codes + recoup ready human send
- Next: prio5 **rq_337**; deferred **rq_116** SWA

### 2026-07-31T11:45:00Z - tick 346
- Unit: **rq_337** (FOI-adjacent hole-fill - **Sport Vlaanderen + ADEPS dual community sport**)
- Found (strong primary VL BBT Sport BO2026 + ADEPS RA2025):
  - **Sport Vlaanderen prog HF BO2026:** VAK **€177.121m** · VEK **€167.136m** (excl DAB/apparaat/prog B).
  - **BA2025 same perimeter:** VAK **€183.884m** · VEK **€185.264m**.
  - **Toelage IS 2026:** VAK **€175.934m** · VEK **€165.949m** (HB0-1HFH2NY-IS + HB0-1HFH5NY-IS).
  - **ISE BO2026:** Sport voor allen VEK **€125.546m** · Infra **€30.876m** · Topsport **€31.659m** · Antidoping **€1.445m**.
  - **ADEPS / FWB sport 2025:** **€49.891m** (0.3% FWB total; ordinaire + SACA/Loterie).
  - Subventions 2025: federations forfait **€8.320m** + plan-programme **€12.932m** · CSL **€5.593m** · SHN **€1.251m** · jeunes **€3.262m** · ASL used **€2.555m**.
  - Staff: **587** agents + **1,215** occasional (8,142 contracts); **64** federations / **6,846** clubs / **813,207** affiliates.
  - **Dual class ~€235m** 2025 (VL VEK 185.3 + ADEPS 49.9; not TE-additive).
- Wrote: sources +3; entities +2; budgets +19; cmt +1; lb +3; FOI gap_sport_vl_adeps_l5 ready; rq_337=done; spawn rq_338; ticks=346
- FOI: L5 federations both sides + ADEPS SACA/Loterie ready human send
- Next: prio5 **rq_338**; deferred **rq_116** SWA

### 2026-07-31T12:15:00Z - tick 347
- Unit: **rq_338** (FOI-adjacent hole-fill - **FWO + FNRS dual community research**)
- Found (strong primary FWO JV2024/2025 + FNRS RA2024):
  - **FWO VL vastlegging:** **€470.342m** BA2024 · **€448.182m** BA2025.
  - **FWO vereffening total:** **€436.818m** 2024 · **€464.623m** 2025.
  - FO projects vast 2024 **€180.070m** / mandaten **€109.378m**; SBO proj **€51.460m** + mand **€43.005m**; infra **€66.176m**.
  - Beheerskosten **€19.324m** (4.11% 2024) · **€23.107m** (5.16% 2025).
  - **FNRS public subsidies 2024:** **€241.818m** (FWB **€173.540m** · fed IISN/FRSM **€40.327m** · WAL **€19.932m** · LN **€8.020m**).
  - FNRS total resources **€262.183m** (incl Telvie **€10.871m** + dons **€8.997m**).
  - Spend: mandats **€152.957m** · projets **€93.259m** · admin **€15.271m**.
  - **Dual class 2024 ~€712m** (FWO vast 470.3 + FNRS public 241.8; not TE-additive).
- Wrote: sources +3; entities +2; budgets +24; cmt +1; lb +3; FOI gap_fwo_fnrs_l5 ready; rq_338=done; spawn rq_339; ticks=347
- FOI: L5 awards both funds + federal cash path ready human send
- Next: prio5 **rq_339**; deferred **rq_116** SWA

### 2026-07-31T12:45:00Z - tick 348
- Unit: **rq_339** (FOI-adjacent hole-fill - **AWV + SOFICO dual roads infrastructure deepen**)
- Found (strong primary AWV Ondernemingsplan 2025 + SOFICO RA2024):
  - **AWV 2024:** VAK **€1.0207bn** · VEK **€1.187bn** (96.54% spent).
  - **AWV 2025:** structureel onderhoud **€138.5m** (snelwegen 49.5 · gewest 47 · kunstwerken 33 · DVM 9); fiets vastlegging min **€158m** (2024 was **€162m**); +18m wegen / +12m EM onderhoud.
  - **SOFICO 2024:** produits **€495.1m** · charges **€397.6m** · net **€100.7m** · invest record **€265m**.
  - **PKPL** (truck tolls) **€347m** (+11.2%); network grands axes **€370.8m** 2024 · cum **~€3.7bn** since 2010.
  - Entretien+rehab class **~€371m** 2024 (161+210).
  - Dual financing: Flanders tax-budget agency vs Wallonia fee-financed UAP.
- Wrote: sources +2; budgets +16; cmt +1; lb +3; FOI gap_awv_sofico_l5 ready; rq_339=done; spawn rq_340; ticks=348
- FOI: AWV opex matrix + top works L5 both sides ready human send
- Next: prio5 **rq_340**; **progress@350 in 2 ticks**; deferred **rq_116** SWA

### 2026-07-31T13:15:00Z - tick 349
- Unit: **rq_340** (FOI-adjacent hole-fill - **Onroerend Erfgoed Flanders dual AWaP heritage**)
- Found (strong primary VL BBT Onroerend Erfgoed BO2026 13-O):
  - **BO2026 total** (excl apparaatrek/prog B): VAK **€121.823m** · VEK **€127.789m**.
  - **BA2025:** VAK **€150.764m** · VEK **€132.084m** (incl one-off partners/Thermae).
  - **ISE Kwaliteit:** VAK **€99.995m** · VEK **€92.702m** (**82.1%** of policy credits).
  - **Premies** QG0-1QGD2CB-WT: VAK **€92.864m** · VEK **€83.188m**; standaard max **€45.3m**; wachtlijst new **€9m**; cut **-€6.562m**.
  - **Erfgoedleningen** PFV: VAK **€7.0m** · VEK **€9.383m** (ESR-neutral).
  - **ISE Partnerschappen:** VAK **€16.953m** · VEK **€29.540m**; prioritaire partners **€1.710m**; IOED VAK **€2.587m**.
  - Bourlaschouwburg max VL **€40.17m** multi-year; Herita SWO 2026-2030 path.
  - Dual: AWaP Wallonia total **residual FOI** (no clean public total this tick).
- Wrote: sources +1; entities +2; budgets +19; cmt +1; lb +2; FOI gap_oe_awap_dual_l5 ready; rq_340=done; spawn **rq_341 progress@350**; ticks=349
- FOI: OE premie L5 + waitlist + AWaP total ready human send
- Next: **MANDATORY rq_341 progress@350**; deferred **rq_116** SWA

### 2026-07-31T13:45:00Z - tick 350 (progress milestone)
- Unit: **rq_341** (mandatory progress@350 coverage % + waste top10)
- Coverage vs EUR 347.956 bn TE:
  - **A L0 / B L1:** **100%** strong
  - **C L2:** **~92-98%** (up from ~91-98% @340) — FWO 470/448m + FNRS public 242m dual research; AWV VEK 1.19bn dual SOFICO 495m; Sport VL 167m dual ADEPS 50m; VAF/CCA + economic AV triple; OE heritage 128m; prior Belspo/CM25/EUMETSAT
  - **D L5:** **~17-28%** — OE premies 83-93m envelope; dual-stack awards residual FOI
  - **E FOI ready:** **~161** (answered ~5; total rows ~168)
- Waste top10: **stable** fossil/company cars/cheque TE/EIWT (Hedera stock filtered off pure annual)
- Inventory: budgets ~4282 / cmt ~632 / lb ~760 / entities ~302 / sources ~666
- Improved since 340: AV dual+Tax Shelter TE 255m; economic AV triple; sport dual 235m; FWO/FNRS 712m; AWV/SOFICO roads; OE heritage 128m
- Wrote: progress_every_10_ticks.md, doge_waste_top10_current.md, loop_state, loop_log; rq_341=done; spawn rq_342; ticks=350
- Next: prio5 **rq_342**; deferred **rq_116** SWA; human FOI send stack ~161 ready

### 2026-07-31T14:15:00Z - tick 351
- Unit: **rq_342** (FOI-adjacent hole-fill - **AWaP Wallonia dual OE Flanders heritage**)
- Found (strong primary Wallonie Budget 2026 DO16):
  - **Programme 16.082** Monuments, sites et fouilles: CE=CL **€46.215m**.
  - Line **082.001** Subvention a l'Agence wallonne du Patrimoine: **€46.215m** eng=liq.
  - EU programming line 082.002: **€0**.
  - Dual Flanders OE VEK **€127.789m** / VAK **€121.823m** 2026 → dual class **~€174m**.
- Wrote: sources +1; budgets +3; cmt +1; lb +2; FOI gap_oe_awap_dual_l5 refresh (total filled, L5 residual); rq_342=done; spawn rq_343; ticks=351
- FOI: OE+AWaP named awards L5 still ready human send
- Next: prio5 **rq_343**; deferred **rq_116** SWA

### 2026-07-31T14:45:00Z - tick 352
- Unit: **rq_343** (FOI-adjacent hole-fill � **dual regional agriculture VL Landbouw + WAL Aides/OPW**)
- Found (strong primary):
  - Flanders BBT Landbouw BO2026 (pfile 2227524): **VAK �157.880m** � **VEK �140.849m** excl. apparaatrek/prog B; TJ VEK **�135.190m**; TK promotie **�5.659m**.
  - Wallonie Budget 2026 DO15 prog **15.058** Aides: CE **�93.325m** � CL **�93.225m**; OPW Missions **�45.049m** + Fonct **�16.747m** + capital **�20.017m** = package **�81.813m** (nested); calamit�s agricoles **�9.300m**.
  - Dual class regional agri policy **~�234m** (VL VEK + WAL aides) � **excludes bulk EU CAP** direct payments via paying agencies.
  - DO15 total CL **�570.184m** (ARNE combined agri+nature+env; not pure agri).
- Wrote: entities +2 (landbouw_vl, opw_wallonie); sources +2; budgets +15; cmt +1; lb +3; FOI **gap_agri_dual_l5_cap** ready + draft; rq_343=done; spawn **rq_344**; ticks=352
- FOI: CAP cash dual + top schemes L5 human send only
- Next: prio5 **rq_344**; deferred **rq_116** SWA

### 2026-07-31T15:15:00Z - tick 353
- Unit: **rq_344** (FOI-adjacent hole-fill � **dual nature Flanders Omgeving/ANB + Wallonia Nature-For�t**)
- Found (strong primary VR BBT Omgeving BO2026 + prior DO15):
  - Omgeving en Natuur excl. apparaatrek: **VAK �690.943m** � **VEK �696.049m** (multi-ISE).
  - ISE Natuur en biodiversiteit: **�150.0m** total (MVG ~**�22m** + DAB MINAfonds **�128.0m**).
  - ANB apparaatrek QA-QD0: **�49.500m**; INBO QA-QC0: **�19.499m**.
  - Dual WAL prog 15.060 Nature-For�t CL **�28.879m** ? dual pure nature class **~�179m** (not full Omgeving 696m).
- Wrote: entities +2 (anb_vl, inbo_vl); sources +1; budgets +10; cmt +1; lb +3; FOI **gap_nature_dual_anb_wal_l5** ready + draft; rq_344=done; spawn **rq_345**; ticks=353
- FOI: MINA nature L5 + WAL 15.060 awards human send only
- Next: prio5 **rq_345**; deferred **rq_116** SWA

### 2026-07-31T15:45:00Z - tick 354
- Unit: **rq_345** (FOI-adjacent hole-fill � **dual waste/remediation OVAM Flanders + SPAQuE/d�chets Wallonia**)
- Found (strong primary BBT Omgeving BO2026 + DO15):
  - ISE Afval en materialen: **�105.9m** (MVG **�102.4m** + MINA **�3.5m**); UPV/zwerfvuil fonds TO **�74.045m** jump.
  - OVAM dept toelage: **�28.349m**; MINA toelage VEK **�37.423m** / VAK **�35.926m**.
  - ISE Bodem: **�41.1m** (MINA-dominant).
  - SPAQuE dotation **�24.138m**; WAL 15.064 d�chets CL **�9.859m**; 15.062 Air-Eau-Sol CL **�64.071m** (ISSeP **�23.783m** nested).
  - Dual waste class **~�116m**; dual remediation class **~�65m** (Bodem+SPAQuE). VMM water class **~�132m** noted.
- Wrote: entities +3 (ovam, spaque, vmm); sources +1; budgets +13; cmt +1; lb +3; FOI **gap_waste_dual_ovam_spaque_l5** ready + draft; rq_345=done; spawn **rq_346**; ticks=354
- FOI: OVAM/SPAQuE L5 sites+grants human send only
- Next: prio5 **rq_346**; deferred **rq_116** SWA

### 2026-07-31T16:15:00Z - tick 355
- Unit: **rq_346** (FOI-adjacent hole-fill - **dual energy/climate VEKA Flanders + SPW Energie/Kyoto/AWAC Wallonia**)
- Found (strong primary Rekenhof BBT E&K + BU2025 + EPNE 2026):
  - Flanders BBT E&K BO2026 (Rekenhof-corrected excl apparaatrek): VAK **EUR 958.573m** � VEK **EUR 1,104.825m**; TO **EUR 436.642m**.
  - BA2025: VAK **EUR 1,612.146m** � VEK **EUR 1,744.523m**.
  - BU2025 outturn: total VAK **EUR 1,239.576m** � VEK **EUR 1,201.859m**; QE Energie VAK **964.831m** / VEK **914.121m**; QH Klimaat VAK **274.745m** / VEK **287.738m**.
  - L5 BU2025: MVP net **EUR 204m** � Energieleningen **194m** � retro invest premies **240.6m** � REG-ODV other **68.2m** � WKK ODV **60m** � Call Groene Warmte **18.9m** � Energiehuizen **14.8m** � Energiefonds toelage **111.9m** � ICL klimaat **231.63m**.
  - WAL EPNE: prog **16.083** Energie CE **EUR 34.395m** � CL **EUR 28.360m** 2026 (2025 CE 80.512 / CL 74.765); Kyoto **15.074** **EUR 158m**; Fonds Energie **16.089** **EUR 7.986m**; AWAC dep **EUR 37.376m**; climate intl **EUR 13m**.
  - Dual energy-climate class **~EUR 1.34bn** (VL VEK + WAL 16.083 + Kyoto + Fonds E + AWAC; not TE-additive). Renopack housing CL **119.586m** excluded from dual.
- Wrote: sources +3; entities +3 (veka spw_energie awac); budgets +28; cmt +1; lb +5; FOI **gap_energy_dual_veka_wal_l5** ready + draft; rq_346=done; spawn **rq_347**; ticks=355
- FOI: MVP/ICL/retro L5 + Kyoto projects + AWAC path human send only
- Next: prio5 **rq_347**; deferred **rq_116** SWA

### 2026-07-31T16:45:00Z - tick 356
- Unit: **rq_347** (FOI-adjacent hole-fill - **dual civic integration AgII Flanders + WAL CRI/ILI**)
- Found (strong primary BBT Inburgering BO2026 + CoA 2022 + ILI press):
  - Flanders BBT excl apparaatrek: VAK **EUR 115.644m** � VEK **EUR 116.647m** BO2026 (BA2025 120.145 / 121.148).
  - **AgII toelage** SJ0-1SFC2DY-IS: **EUR 64.611m** (2025: 63.617m); institutional lonen **54.767m** � werking VAK **15.500m** � own rec **5.778m**.
  - WT uitbouw: VAK **51.033m** / VEK **52.036m**; Atlas+Amal class **EUR 51m**; B1 Mondeling **+7.0m**; turboplan **-10.0m**; generic cut **-2.817m**.
  - WAL: CoA GCOM 2020 eng **EUR 22.498m** (CRI 6.9 + ILI agr 3.8 + ILI non 10.3 + Setis 0.8 + FOREM 0.7); ILI 2025 call **>EUR 3.6m** / 140 ops.
  - Dual civic-integration class **~EUR 120m** (VL-dominant; not TE-additive).
- Wrote: sources +3; entities +2; budgets +20; cmt +1; lb +4; FOI **gap_integration_dual_vl_wal_l5** ready + draft; rq_347=done; spawn **rq_348**; ticks=356
- FOI: AgII/Atlas L5 + WAL 2026 full CRI/ILI path human send only
- Next: prio5 **rq_348**; deferred **rq_116** SWA

### 2026-07-31T17:15:00Z - tick 357
- Unit: **rq_348** (FOI-adjacent hole-fill - **dual vocational SME training SYNTRA Flanders + IFAPME Wallonia**)
- Found (strong primary VR 17 Jul 2026 + EPJE DO18 prog 112):
  - Flanders: Syntrum + Syntra package **EUR 49.7m** cursusjaar 2026-2027 (transitional reform year; per-centre L5 residual).
  - Wallonia IFAPME prog 112 CE=CL **EUR 88.299m** 2026 (2025 **82.253m**):
    - fonctionnement 112.002 **39.582m** (was 29.829; statutarisering + PRW RH)
    - formation independants 112.003 **40.661m**
    - contrat de gestion 112.004 **2.684m**
    - strategie numerique 112.005 **1.375m**
    - accrochage 112.006 **0.857m**
    - investissements centres 112.019 **3.140m**
  - Dual vocational class **~EUR 138m** (not TE-additive; excludes VDAB/FOREM/18.109/18.25 croisees).
- Wrote: entities +2 (syntra_vl, ifapme); sources +2; budgets +10; cmt +1; lb +3; FOI **gap_vocational_dual_syntra_ifapme_l5** ready + draft; rq_348=done; spawn **rq_349**; ticks=357
- FOI: Syntra per-centre L5 + IFAPME centre network grants human send only
- Next: prio5 **rq_349**; deferred **rq_116** SWA

### 2026-07-31T17:45:00Z - tick 358
- Unit: **rq_349** (FOI-adjacent hole-fill - **dual culture Flanders CJM + FWB DO20**)
- Found (strong primary VL BBT Cultuur BO2026 + FWB exp. particulier):
  - Flanders content class **~EUR 426.2m**: Kunsten VEK **157.966m** � Erfgoed **85.589m** � SCW **83.125m** � Amateur **14.031m** � Digital **20.161m** � Opera Ballet **31.045m** � KMSKA **12.123m** � Philharmonic **10.554m** � Literatuur **11.611m** (excl VIA 67.2m / infra mixed).
  - FWB DO20 Culture: CE **267.213m** � CL **367.468m** 2026 (2025 CL 362.582m).
  - L5 FWB: arts vivants CL **103.630m** � transversal **92.187m** � territoriale **67.383m** � musiques **52.725m** � patrimoines **23.000m**.
  - Cross-check DO26 Sport CL **49.981m** (ADEPS class).
  - Dual culture class **~EUR 794m** (not TE-additive; VEK vs CL scopes).
- Wrote: entities +2; sources +2; budgets +23; cmt +1; lb +5; FOI **gap_culture_dual_vl_fwb_l5** ready + draft; rq_349=done; spawn **rq_350**; ticks=358
- FOI: top-50 operators both sides + moratoria cash human send only
- Next: prio5 **rq_350**; deferred **rq_116** SWA

### 2026-07-31T18:15:00Z - tick 359
- Unit: **rq_350** (FOI-adjacent hole-fill - **dual recreational youth Flanders Jeugd + FWB DO23 Jeunesse**)
- Found (strong primary VL BBT Jeugd BO2026 + FWB exp. particulier DO23):
  - Flanders ISE Jeugd total **EUR 72.461m** BO2026 (BA2025 72.696m):
    - kwaliteit jeugdwerk VEK **47.461m** (ex-DAC integrated; capacity cut -1.648m)
    - jeugdvakanties **9.792m** � innovatie **8.545m** � lokaal/int **2.309m**
    - ULDK **2.167m** � JINT **1.263m** � kinderrechten **0.844m**
  - FWB DO23 prog 2 Jeunesse: CE **67.951m** � CL **67.137m** 2026:
    - organisations de jeunesse **26.822m** � centres de jeunes CL **34.811m**
  - Dual recreational youth class **~EUR 140m** (not TE-additive).
  - Explicitly **excludes** FWB Aide a la Jeunesse DO17 **470.6m** (protection dual Opgroeien) and VL jeugdhulp.
  - Note: DO23 education permanente CL **44.604m** dual VL SCW separate.
- Wrote: entities +2; sources +2; budgets +16; cmt +1; lb +5; FOI **gap_youth_dual_vl_fwb_l5** ready + draft; rq_350=done; spawn **rq_351**; ticks=359
- FOI: top-30 orgs/centres both sides human send only
- Next: prio5 **rq_351**; deferred **rq_116** SWA

### 2026-07-31T18:45:00Z - tick 360
- Unit: **rq_351** (**progress milestone @360** � coverage % + waste top10 refresh; no new euro invent)
- Snapshot (honest order-of-magnitude vs TE EUR 347.956 bn):
  - **A L0 / B L1:** **100%** (unchanged strong)
  - **C L2:** **~93�98%** (up from ~92�98% @350) � dual sprint 351�359: heritage/agri/nature/waste/energy **1.34bn**/integration/vocational/culture **~794m**/youth **~140m**
  - **D L5:** **~18�29%** generous (IFAPME L5 + culture/youth decree lines; residual top-N FOI)
  - **E FOI ready:** **~170** (answered ~5; total FOI rows ~176)
- Inventory: budgets ~4420 � cmt ~641 � lb ~793 � entities ~320 � sources ~666
- Waste top10: **stable** fossil/company-cars/cheque/EIWT mega items (Hedera stock filtered off annual top10)
- Dual-class map (not TE-additive) refreshed in waste top10 appendix
- Wrote: `progress_every_10_ticks.md` + `doge_waste_top10_current.md`; rq_351=done; spawn **rq_352**; ticks=360
- FOI: no new gap this tick (progress only)
- Next: prio5 **rq_352** hole-fill; deferred **rq_116** SWA

### 2026-07-31T19:15:00Z - tick 361
- Unit: **rq_352** (FOI-adjacent hole-fill - **dual adult formal education FWB DO56 + VL volwassenenonderwijs/DKO residual**)
- Found (strong primary FWB exp. particulier + VL commissie Onderwijs 15-7-H):
  - FWB **DO56 Enseignement pour adultes** CE=CL **EUR 267.547m** 2026 (2025: 261.751m):
    - personnel **251.737m** (~94%) � fonctionnement ecoles **9.132m**
    - initiatives emploi **2.372m** � transversales **2.368m** � echec **1.830m**
  - FWB **DO58** distance **2.372m**; **DO57** artistique horaire reduit **142.473m** + superieur artistique **119.128m** (dual DKO/conservatories class).
  - VL Onderwijs total VEK **EUR 17.24bn** / VAK **17.25bn**; DKO+VO **+44.2m / +4.7%** (VO alone +5.5%); absolute VO/DKO ISE residual FOI.
  - Dual adult formal floor **FWB 267.5m** strong; VL absolute residual (not invented dual sum).
- Wrote: entities +3; sources +2; budgets +14; cmt +1; lb +5; FOI **gap_adult_edu_dual_vl_fwb_l5** ready + draft; rq_352=done; spawn **rq_353**; ticks=361
- FOI: VL VO/DKO ISE absolute + FWB school L5 human send only
- Next: prio5 **rq_353**; deferred **rq_116** SWA

### 2026-07-31T19:45:00Z - tick 362
- Unit: **rq_353** (FOI-adjacent hole-fill - **dual territorial culture / lecture publique FWB DO20 prog7 + VL bovenlokaal**)
- Found (strong primary VL BBT Cultuur domain tables + FWB exp. particulier prog7):
  - Flanders **Cultuur domain** MVG excl DAB ESR VEK **EUR 393.544m** / VAK **394.115m** BO2026 (BA2025 VEK 406.838m).
  - VL **bovenlokaal/cross** HCF2TA-WT VEK **15.461m** (VAK 15.592m); project cut **-3.6m**; leenrecht bibliotheken **-1.834m**.
  - FWB **prog7 Action culturelle territoriale** CL **67.383m** (CE 110.872m):
    - centres culturels CL **32.372m** � bibliotheques **23.975m** (CE 41.114m)
    - CEC/amateurs **5.292m** � PointCulture **3.640m**
  - Dual territorial class **~EUR 83m** (asymmetric FWB-heavy; not TE-additive; VL municipal library residual FOI).
- Wrote: entities +2; sources +2; budgets +14; cmt +1; lb +5; FOI **gap_territorial_culture_dual_vl_fwb_l5** ready + draft; rq_353=done; spawn **rq_354**; ticks=362
- FOI: top IGS/CC/biblio L5 + VL leenrecht path human send only
- Next: prio5 **rq_354**; deferred **rq_116** SWA

### 2026-07-31T20:15:00Z - tick 363
- Unit: **rq_354** (FOI-adjacent hole-fill - **dual PSB media 2026 refresh RTBF official BI + VRT basistoelage**)
- Found (strong primary FWB exp. particulier DO25 + existing VRT BHO path):
  - FWB **DO25** Medias CL **EUR 426.353m** / CE **424.988m** 2026.
  - Prog3 Radio-TV CL **402.971m**.
  - **RTBF official 2026 L5:** ordinary **350.819m** � access **4.050m** � pension pool **13.956m** � TV5 frais **1.230m** + soutien **8.310m** � SEC **10.897m** = package **389.262m** (vs RA2025 package ~378m prior).
  - Medias de proximite class **~12.4m** � Presse **14.775m** � CSA **3.751m**.
  - VRT basistoelage **296.4m** 2026 dual ordinary **647.2m**; package dual order **~686m** (not TE-additive).
- Wrote: entities +1; sources +1; budgets +16; cmt +1; lb +5; FOI **gap_psb_dual_vl_fwb_l5_2026** ready + draft; rq_354=done; spawn **rq_355**; ticks=363
- FOI: RTBF RA vs budget + VRT side-envelopes L5 human send only
- Next: prio5 **rq_355**; deferred **rq_116** SWA

### 2026-07-31T20:45:00Z - tick 364
- Unit: **rq_355** (FOI-adjacent hole-fill - **dual popular/civic education VL SCW + FWB education permanente**)
- Found (strong primary VL BBT Cultuur SCW + FWB exp. particulier DO23 prog3):
  - Flanders **SCW** HCF2TE-WT VEK **EUR 83.125m** / VAK **83.190m** BO2026 (cut ~-3.5m).
  - FWB **Education permanente** prog3 CL **44.604m** / CE **30.442m** 2026:
    - associations reconnues decret 2003 CL **43.037m** (CE 29.657m; ~96pct of EP)
    - formation animateurs **0.365m** � projets **0.482m** � loisirs culturels **0.626m**
  - Dual popular/civic education class **~EUR 128m** (not TE-additive; excludes formal EPA/VO and jeunesse).
- Wrote: entities +2; sources +2; budgets +11; cmt +1; lb +4; FOI **gap_popular_edu_dual_vl_fwb_l5** ready + draft; rq_355=done; spawn **rq_356**; ticks=364
- FOI: top-30 SCW + EP associations human send only
- Next: prio5 **rq_356**; deferred **rq_116** SWA

### 2026-07-31T21:15:00Z - tick 365
- Unit: **rq_356** (FOI-adjacent hole-fill - **dual childcare VL Opgroeien KO + FWB ONE**)
- Found (strong primary VL BBT WVGA tech Q + FWB DO19 ONE):
  - Flanders **kinderopvang** **EUR 1,557.7m** BO2026:
    - voorschools **1,290m** � buitenschools **204.5m** � zij-instroom **30m**
    - residual VIA/loketten inside package
  - Related Opgroeien: PGJO **36.2m** � adoptie **3.9m** � consultatiebureaus **18m** � OverKop base **4.6m** � Huizen van het Kind **3.6m** + pilots **1.35m**
  - FWB **ONE** DO19 **EUR 760.837m** 2026 (2025: 711.833m):
    - dot main **604.028m** � IT 35.3 � reform 27.7 � places 5.0 � accueillantes 20.8 � emploi 49.4 � nouvelles 15.1
  - Dual childcare class **~EUR 2.32bn** (not TE-additive; largest community dual mapped).
  - Excludes: Groeipakket/AF; AJ DO17 470.6m protection; recreational youth.
- Wrote: entities +1 (notes +2); sources +2; budgets +11; cmt +1; lb +5; FOI **gap_childcare_dual_vl_one_l5** ready + draft; rq_356=done; spawn **rq_357**; ticks=365
- FOI: top operators places matrix both sides human send only
- Next: prio5 **rq_357**; deferred **rq_116** SWA

### 2026-07-31T21:45:00Z - tick 366
- Unit: **rq_357** (FOI-adjacent hole-fill - **dual youth protection VL ISE Jeugdhulp + FWB Aide a la Jeunesse**)
- Found (strong primary VL BBT WVG BU2025 + FWB DO17):
  - Flanders **ISE Jeugdhulp** MVG excl DAB:
    - BA2025 VEK **EUR 958.939m** / VAK **940.463m**
    - BU2025 VEK **969.124m** / VAK **949.407m**
    - GEF2MX toelage BA **937.575m** / BU VEK **947.760m**
    - AGEF2MA provider subsidies VEK **958.937m** (VAK 967.947m)
    - GEF5MX invest VEK **21.364m**
  - FWB **DO17 AJ** liq **EUR 470.617m** (resid 264.1m ~56pct) BI2026 prior strong
  - Dual youth-protection class **~EUR 1.44bn** (VL BU2025 + FWB 2026; not TE-additive).
  - Excludes: recreational youth ~140m; KO/ONE dual ~2.32bn; Groeipakket.
- Wrote: entities +1 (note +1); sources +2; budgets +9; cmt +1; lb +4; FOI **gap_youth_protect_dual_vl_fwb_l5** ready + draft; rq_357=done; spawn **rq_358**; ticks=366
- FOI: BO2026 ISE table + top operators both sides human send only
- Next: prio5 **rq_358**; deferred **rq_116** SWA

### 2026-07-31T22:15:00Z - tick 367
- Unit: **rq_358** (FOI-adjacent hole-fill - **Flanders ISE Welzijnswerk + CAW L5 package**)
- Found (strong primary VL BBT WVG BU2025):
  - **ISE Welzijnswerk** BA VEK **EUR 154.417m** / BU VEK **159.634m**
  - GCF2EA article BA VEK **141.740m** / BU **147.053m**:
    - **CAW 130.138m** � bis **1.240m** � teleonthaal **3.923m** � schuldhulp **1.498m**
  - Bonus same source: ISE **Sociale Bescherming** BA VEK **5.274bn** / BU **5.332bn** (toelagen IS ~3.95-4.02bn)
  - GHF2TG thuis/ouderenzorg BA VEK **81.034m** / BU **77.519m**
  - ISE Gespecialiseerde zorg BU VEK **145.724m**; Woonzorg+EL BA total VEK **67.675m**
  - Dual note: WAL relais sociaux much smaller scale (FOI/unit-cost residual).
- Wrote: entities +2; sources +2; budgets +15; cmt +1; lb +5; FOI **gap_vl_caw_l5_per_centre** ready + draft; rq_358=done; spawn **rq_359**; ticks=367
- FOI: per-CAW matrix + BO2026 human send only
- Next: prio5 **rq_359**; deferred **rq_116** SWA

### 2026-07-31T22:45:00Z - tick 368
- Unit: **rq_359** (FOI-adjacent hole-fill - **Flanders ISE Gespecialiseerde zorg / GGZ L5**)
- Found (strong primary VL BBT WVG BU2025 GDF2LA):
  - **ISE Gespecialiseerde zorg** BA VEK **EUR 142.027m** / BU **145.724m**
  - Named L5 inside GDF2LA:
    - **CGG** overeenkomst **102.508m**
    - **OPZ Geel + OPZC Rekem** **27.997m** (+ IFIC herverdeling +2m path)
    - Psyche VZW **2.716m** � erfelijkheid 4 centra **2.696m**
    - Vroegdetectie KJ **4.235m** � aanklampende zorg **1.324m**
    - Tandem **0.658m** � intersectorale teams JV **0.967m**
    - Familieplatform **0.541m** � VIKZ **0.690m**
  - Dual note: WAL centres de sante mentale residual FOI.
- Wrote: entities +3; sources +1; budgets +15; cmt +1; lb +5; FOI **gap_vl_ggz_cgg_l5** ready + draft; rq_359=done; spawn **rq_360**; ticks=368
- FOI: per-CGG + OPZ split + BO2026 human send only
- Next: prio5 **rq_360**; deferred **rq_116** SWA

### 2026-07-31T23:15:00Z - tick 369
- Unit: **rq_360** (FOI-adjacent hole-fill - **Flanders ISE Armoedebeleid L5 + Preventie package**)
- Found (strong primary VL BBT WVG BU2025):
  - **ISE Armoedebeleid** BA VEK **EUR 46.547m** / BU **28.802m** (under-exec)
    - GCF2CA BA **21.414m** / BU **20.542m**: samenlevingsopbouw 8 reg **13.755m**; verenigingen armen **4.514m**; Netwerk **0.986m**; De Link **0.797m**; Caritas **0.250m**
    - GCF2CB BA **25.133m** / BU only **8.260m** (Gezonde Voeding op School path)
  - **ISE Preventie** BA VEK **103.607m** / BU **80.360m**
    - GDF2JA ramingen: vaccins **29m** � partners **19.5m** � terrein **16m** � gezondheidsmakers **9m** � uitbreiding **10m**
- Wrote: entities +3; sources +1; budgets +26; cmt +2; lb +7; FOI **gap_vl_armoede_prev_l5** ready + draft; rq_360=done; spawn **rq_361**; ticks=369
- FOI: named L5 + under-exec cash path human send only
- Next: prio5 **rq_361**; deferred **rq_116** SWA

### 2026-07-31T23:45:00Z - tick 370
- Unit: **rq_361** (**progress milestone @370** - coverage % + waste top10 refresh; no new euro invent)
- Snapshot (honest order-of-magnitude vs TE EUR 347.956 bn):
  - **A L0 / B L1:** **100%** (unchanged strong)
  - **C L2:** **~94-98%** (up from ~93-98% @360) - childcare dual **~2.32bn** + youth protect **~1.44bn** + WVG ISE pack
  - **D L5:** **~19-30%** generous (CGG 102.5m OPZ 28m CAW 130m armoede/preventie named; residual FOI)
  - **E FOI ready:** **~178** (answered ~5; total FOI rows ~185)
- Inventory: budgets ~4552 - cmt ~651 - lb ~838 - entities ~338 - sources ~698
- Waste top10: **stable** fossil/company-cars/cheque/EIWT mega items
- Dual-class map refreshed: childcare 2.32bn, youth protect 1.44bn, energy 1.34bn, culture 794m, PSB 647m, ...
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_361=done; spawn **rq_362**; ticks=370
- FOI: no new gap this tick (progress only)
- Next: prio5 **rq_362** hole-fill; deferred **rq_116** SWA

### 2026-08-01T00:15:00Z - tick 371
- Unit: **rq_362** (FOI-adjacent hole-fill - **Flanders VIA L5 + sociale akkoorden package**)
- Found (strong primary VL BBT WVG BU2025):
  - **GCF2FA VIA** BA VEK **EUR 137.796m** / BU **141.687m**
    - GSD-V **81.178m** � 2de pensioenpijler priv **21.513m** � VSPF maribel **15.638m**
    - VVSG **4.681m** � SFNP **2.838m** � Verso/VIVO named � sample sum **~128.8m**
  - **GHF2TR sociale akkoorden** BA **217.298m** / BU **226.806m** (eindeloopbaan/maribel/syndicale ouderenzorg EL GGZ)
  - Vrijwilligerswerk GCF2EB BA **2.037m** (140 orgs � 1.860m autonomous)
  - Lokaal sociaal GCF2ED BA **2.461m** (Lus 0.501 Trefpunt 0.337 VVSG 0.322)
  - ISE Beleidsondersteuning BA VEK **305.139m** / BU **283.604m** (broad context)
- Wrote: entities +3; sources +1; budgets +27; cmt +2; lb +8; FOI **gap_vl_via_soc_akkoorden_l5** ready + draft; rq_362=done; spawn **rq_363**; ticks=371
- FOI: VIA BVR outturn + soc-akkoorden component split human send only
- Next: prio5 **rq_363**; deferred **rq_116** SWA

### 2026-08-01T00:45:00Z - tick 372
- Unit: **rq_363** (FOI-adjacent hole-fill - **Flanders eerstelijn GDF2KA + Impulseo L5**)
- Found (strong primary VL BBT WVG BU2025):
  - **ISE Woonzorg en eerste lijn** BA total VEK **EUR 67.675m** / BU **63.257m**
  - **GDF2KA** eerstelijnsgezondheidszorg BA VEK **37.155m** / BU **34.539m**
    - VV116 EPD herverdeling path **6.220m** VEK
  - **Impulseo GDF2KB** BA **27.000m** / BU **26.658m** (98.7pct):
    - Impulseo 2 groepering **23.329m** (963 dossiers)
    - Impulseo 3 solo **2.013m** (268 dossiers)
  - Impulsfonds loan receipts AO BU **2.195m**
- Wrote: entities +2; sources +1; budgets +12; cmt +1; lb +6; FOI **gap_vl_eerstelijn_impulseo_l5** ready + draft; rq_363=done; spawn **rq_364**; ticks=372
- FOI: GDF2KA projects + Impulseo multi-year + Impulsfonds stock human send only
- Next: prio5 **rq_364**; deferred **rq_116** SWA

### 2026-08-01T01:15:00Z - tick 373
- Unit: **rq_364** (FOI-adjacent hole-fill - **VSB 2025 pillar L5 full matrix**)
- Found (strong primary BBT WVG BU2025 Orafin AVSB):
  - VSB toelage begrotingscontrole **EUR 4,021.075m** VEK (fully charged)
  - **ROZ** residentiele ouderenzorg **2,892.788m** (~72pct)
  - ZBO **350.488m** � ZZZ **137.083m** � ZPH **25.433m** (sum zorgbudgetten **513.004m**)
  - RCO **211.396m** � PVT+IBW **153.355m** � RZH **121.603m** � MOHM **101.016m**
  - AVSB **13.988m** � MBE **12.931m** � MDO **0.994m**
  - Pillar sum = 4,021.075m exact; dual 2026 agency VEK 4.748bn path prior
- Wrote: entities +2 (vsb note); sources +1; budgets +13; cmt +1; lb +9; FOI **gap_vsb_provider_l5** ready + draft; rq_364=done; spawn **rq_365**; ticks=373
- FOI: WZC/provider L5 + BO2026 pillars human send only
- Next: prio5 **rq_365**; deferred **rq_116** SWA

### 2026-08-01T01:45:00Z - tick 374
- Unit: **rq_365** (FOI-adjacent hole-fill - **VAPH 2025 institutional L5 + PVB split**)
- Found (strong primary BBT WVG BU2025):
  - GGF2RX toelage VEK **EUR 2,762.041m** (BA-JR=BU; fully available to VAPH)
  - Agency exp VEK BU **2,735.733m** � receipts **2,810.173m**
  - **PVB** **1,517.536m** VEK: third-party **1,207.851m** � cash **309.684m**
  - Zorginstellingen subsidies **896.795m** (top-up/MFC/internaten)
  - 5,201 TBS � **4,551** persons � PAB awards **330**
  - Uitbreiding: PG1 52.4 � PG2 24.1 � PAB minors 13 � MFC/RTH 12.9m
- Wrote: entities +1; sources +1; budgets +16; cmt +1; lb +6; FOI **gap_vaph_provider_pvb_l5** ready + draft; rq_365=done; spawn **rq_366**; ticks=374
- FOI: provider top + PAB EUR + BO2026 human send only
- Next: prio5 **rq_366**; deferred **rq_116** SWA

### 2026-08-01T02:15:00Z - tick 375
- Unit: **rq_366** (FOI-adjacent hole-fill - **Flanders Groeipakket + Geintegreerd gezinsbeleid BU2025 L5**)
- Found (strong primary BBT WVG BU2025):
  - **ISE Groeipakket** VEK BU **EUR 4,906.672m** (BA 4,906.129m)
    - GEF2QX Opgroeien policy **4,797.102m** (VAK=VEK BA=BU)
    - GEF2QY VUTG toelage VEK BU **109.570m**
    - Agency exp AGEF2QB+QY+QW **4,859.865m** (+32.1m vs credit); recoveries **32.972m**
  - VUTG L5: private UA admin **67.082m** (Kidslife/Infino/MyFamily/Parentia) - lonen **38.047m** - invest **4.342m**
  - VUTG/Fons benefits channel **1,147.696m**; toelage Opgroeien **1,131.694m**
  - **ISE Geintegreerd gezinsbeleid** VEK BU **1,369.467m** (GEF2UX)
    - Parent fees KO **233.463m** (raming 249.4m); AGEF2UA-LO **100.986m**; WT surplus **79.2m**
- Wrote: entities +3; sources +1; budgets +26; cmt +2; lb +7; FOI **gap_vl_gp_gezinsbeleid_l5** ready + draft; rq_366=done; spawn **rq_367**; ticks=375
- FOI: per-UA admin + AGEF2QB channel + KO provider top human send only
- Next: prio5 **rq_367**; deferred **rq_116** SWA

### 2026-08-01T02:45:00Z - tick 376
- Unit: **rq_367** (FOI-adjacent hole-fill - **Flanders Beleidsondersteuning L5 + Zorginfrastructuur/VIPA totals**)
- Found (strong primary BBT WVG BU2025):
  - **ISE Beleidsondersteuning** VEK BU **EUR 283.604m** (BA 305.139 / BA-JR 311.925)
    - GCF2BA VEK BU **278.211m**: sociale akkoorden **274.513m** - IT/comms **10.809m**
    - Named L5: SAM **3.488** - ouderen **1.098** - Steunpunt WVG 0.55 - IMEC 0.571 - Sociaal.Net 0.351 - CEBAM 0.3 - ...
    - GCF2BB data BU **4.021m** - GCF2BC crisis **1.346m** - VASGAZ **26k**
  - **ISE Zorginfrastructuur** VEK BU **727.337m** (BA 779.449)
    - GIF2SX-IS **353.887m** - GIF5SX-IS **133.333m** - LE capital **226.847m**
    - Vlabinvest **2.35m** - KO gemeenten path **60m** - A1/A3 capital **100.467m**
- Wrote: entities +3; sources +1; budgets +47; cmt +2; lb +9; FOI **gap_vl_beleid_zorginfra_l5** ready + draft; rq_367=done; spawn **rq_368**; ticks=376
- FOI: GCF2BA residual + soc-akkoorden dual GHF2TR + VIPA provider/municipal L5 human send only
- Next: prio5 **rq_368**; deferred **rq_116** SWA

### 2026-08-01T03:15:00Z - tick 377
- Unit: **rq_368** (FOI-adjacent hole-fill - **Iriscare RA2024 institutional outturn dual AF/care**)
- Found (strong primary Iriscare Rapport annuel 2024):
  - Total **depenses EUR 1,732.255m** / recettes **1,727.883m**
  - **Vivalis dotation 1,660.923m** (~96pct of receipts)
  - **Allocations familiales 1,055.302m** (largest)
  - **MR forfait 345.969m** - **APA 35.386m**
  - **Famiris** public channel **427m** (122,524 children; 65,117 families)
  - Recoveries AF 51.549m - ANM 2.972m - placements 1.043m
  - Headcount **363**; dual VL GP 4.91bn + WAL AF 3.01bn class
- Wrote: entities +2; sources +1; budgets +14; cmt +1; lb +6; FOI **gap_iriscare_l5_2024** ready + draft; rq_368=done; spawn **rq_369**; ticks=377
- FOI: private AF caisses + MR operators + payroll L5 human send only
- Next: prio5 **rq_369**; deferred **rq_116** SWA

### 2026-08-01T03:45:00Z - tick 378
- Unit: **rq_369** (FOI-adjacent hole-fill - **New Samusocial RA2025 multi-funder budget L5**)
- Found (strong primary Samusocial Rapport activite 2025 p125):
  - **Budget 2025 EUR 72.444781m** (calendar)
  - Financing: **COCOM 38.8% (~28.1m)** - **Fedasil 36.7% (~26.6m)** - **RBC 17.6% (~12.8m)** - INAMI 3.3 - Iriscare 1.3 - BrussHelp 0.7 - Maribel 0.5 - Actiris 0.1
  - Missions: **urgence 50.5% (~36.6m)** - **Fedasil DPI 34.6% (~25.1m)** - support 11% - maraudes 2.5 - housing 1.4
  - Dons collected 2025 **0.530m**; 2024 carry **0.201m**
  - Activity: 11383 hosted / 56951 shelter requests / 23402 street / 2159 exits
  - Dual COCOM BI2026 71.9m; CoA prior 41.8m narrower class; accounts 2020-24 still FOI
- Wrote: sources +1; budgets +17; cmt +1; lb +6; entity note; FOI **gap_samusocial_accounts_l5** ready + draft; rq_369=done; spawn **rq_370**; ticks=378
- FOI: general accounts 2020-25 + FTE + cash codes human send only
- Next: prio5 **rq_370**; deferred **rq_116** SWA

### 2026-08-01T04:15:00Z - tick 379
- Unit: **rq_370** (FOI-adjacent hole-fill - **ONSS/RSZ RA2025 budget de gestion L5 + financing headlines**)
- Found (strong primary ONSS Rapport annuel 2025):
  - **Gestion 2025 EUR 301.211m** (pers 172.571 + fonct 123.651 + invest 4.989)
  - Personnel **57pct**; path 158.1 / 167.4 / 172.6m 2023-25
  - **Smals** IT fonct **108.957m** + invest **1.949m** = **110.906m** (~37pct gestion)
  - Cotisations **83.4bn** - financement alternatif **22.7bn** - subventions Etat **11.8bn**
  - 95.89pct on-time; 251734 employers; ~4m workers; headcount ~1668
- Wrote: sources +1; budgets +24; cmt +1; lb +6; entity note; FOI **gap_onss_mission_l5** ready + draft; rq_370=done; spawn **rq_371** (progress@380 next); ticks=379
- FOI: mission budget branch split + FPS codes for 11.8bn/22.7bn human send only
- Next: **mandatory progress@380** then prio5 rq_371; deferred **rq_116** SWA

### 2026-08-01T04:45:00Z - tick 380
- Unit: **rq_371** (**progress milestone @380** - coverage % + waste top10 refresh; no new euro invent)
- Snapshot (honest order-of-magnitude vs TE EUR 347.956 bn):
  - **A L0 / B L1:** **100%** (unchanged strong)
  - **C L2:** **~95-98%** (up from ~94-98% @370) - VSB 4.02bn + VAPH 2.76bn + Groeipakket 4.91bn + Gezinsbeleid 1.37bn + Zorginfra 727m + Iriscare 1.73bn + ONSS gestion 301m
  - **D L5:** **~20-31%** generous (PVB split, VUTG UA 67m, Samusocial funder %, ONSS Smals 111m; residual FOI)
  - **E FOI ready:** **~187** (answered ~5; total FOI rows ~194)
- Inventory: budgets ~4748 - cmt ~663 - lb ~901 - entities ~353 - sources ~707
- Waste top10: **stable** fossil/company-cars/cheque/EIWT mega items (Hedera stock filtered)
- Dual/off-TE map refreshed: childcare 2.32bn, youth protect 1.44bn, GP 4.91bn, Iriscare AF 1.06bn, ONSS cotis 83.4bn off-TE, ...
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_371=done; spawn **rq_372**; ticks=380
- FOI: no new gap this tick (progress only)
- Next: prio5 **rq_372** hole-fill; deferred **rq_116** SWA

### 2026-08-01T05:15:00Z - tick 381
- Unit: **rq_372** (FOI-adjacent hole-fill - **RVA/ONEM JV2025 budget L5 opdrachten+beheer**)
- Found (strong primary RVA Jaarverslag 2025 vol.1 tables 1.4.6):
  - Global exp **EUR 7,371.035m** / rec **7,343.783m** (saldo -27.3m)
  - Opdrachten exp **6,950.791m**: sociale prestaties **6,383.351m** - UI vergoedingen **233.604m** - diverse **333.837m**
  - Beheer **306.638m**: personeel **236.021m** (77pct) - werking **65.826m** - invest **4.352m**
  - Gewestelijk activation **113.594m**; staff **2,959 FE** / 2,622 VTE + 336 external
  - Path beheer 277.9/295.2/306.6 2023-25 (CoA 2023 match)
- Wrote: sources +1; budgets +26; cmt +1; lb +6; FOI **gap_rva_werking_smals_l5** ready; unemp FOI note; rq_372=done; spawn **rq_373**; ticks=381
- FOI: werking/Smals L5 + residual per-union UI human send only
- Next: prio5 **rq_373**; deferred **rq_116** SWA

### 2026-08-01T05:45:00Z - tick 382
- Unit: **rq_373** (FOI-adjacent hole-fill - **FSO Fonds Sluiting 2025 L5 dual RVA**)
- Found (strong primary RVA JV2025 ch.5):
  - Receipts **EUR 516.683m** (+67pct): TW contrib **237.8m** - classic **215.0m** - bijzonder **24.8m** - recoveries **32.9m**
  - Compensations **371.944m** (+54pct): contractueel **338.7m** - sluiting **23.9m** - overbrug **3.0m** - toeslag **0.8m** + socialprofit **5.6m**
  - TW share to RVA **178.699m** (+35pct)
  - Beheer **8.478m**; 27,626 beneficiaries; Van Hool largest dossier
  - Package class **~559m** (comp+TW+beheer)
- Wrote: sources +1; budgets +21; cmt +1; lb +6; entity note; FOI **gap_fso_top_dossiers_l5** ready; rq_373=done; spawn **rq_374**; ticks=382
- FOI: top-20 employer dossiers EUR human send only
- Next: prio5 **rq_374**; deferred **rq_116** SWA

### 2026-08-01T06:15:00Z - tick 383
- Unit: **rq_374** (FOI-adjacent hole-fill - **RIZIV/INAMI Budget soins de sante 2025 full matrix + corrections L5**)
- Found (strong primary CM/INAMI PDF):
  - Total rec=exp **EUR 45,221.741m** (+5.69pct)
  - Prestations **39,812.150m** (authorized **39,692.495m** after non-affectable 119.7m)
  - Beheerskosten **1,188.516m** - Globaal beheer transfers **38,322.478m**
  - Corrections package **216.802m**: meds **113.4** - doctors **73.4** (teleconsult **68.4**) - dentists **20.0** - implants **10.0**
  - Sous-utilisation **114.401m** - reserves **30.148m**
- Wrote: sources +1; budgets +25; cmt +1; lb +7; FOI **gap_riziv_partial_objectifs_l5** ready; rq_374=done; spawn **rq_375**; ticks=383
- FOI: partial objectifs annex + claw-forward path + landsbond beheer human send only
- Next: prio5 **rq_375**; deferred **rq_116** SWA

### 2026-08-01T06:45:00Z - tick 384
- Unit: **rq_375** (FOI-adjacent hole-fill - **RIZIV partial objectifs L5 matrix annexe 2 + admin OA split**)
- Found (strong primary INAMI Budget 2025 annexe 2/1):
  - **Doctors 11,642.546m** (consult 3,566 · imaging 1,753 · surgery 1,536 · clinbio 1,557)
  - **Hospital day package 8,513.199m** (verpleegdag 8,068)
  - **Pharma 6,979.202m** · **Nurses 2,319.840m** · **Dentists 1,622.006m** · **Kines 1,340.350m**
  - Implants 1,008 · Dialysis 582 · Rehab 627 · Maisons med 373 · Psycho 251 · LVZ 440 · Soc akkoord 295
  - **OA admin 988.052m** · INAMI beheer 121.7 · wet ziekenhuizen 2,696 · e-sante 113.4
  - GFB salaries 27,275 · self-emp 2,672 · alt fin salaries 7,319
- Wrote: sources +1; budgets +48; cmt +1; lb +9; FOI gap_riziv note residual narrowed; rq_375=done; spawn **rq_376**; ticks=384
- FOI: mid-year delivery + landsbond split still human send (partial objectifs largely public-filled)
- Next: prio5 **rq_376**; deferred **rq_116** SWA

### 2026-08-01T07:15:00Z - tick 385
- Unit: **rq_376** (FOI-adjacent hole-fill - **FPD/SFP legal pensions L5 PensionStat + JV2024**)
- Found (strong primary PensionStat XLSX + FPD jaarverslag 2024):
  - Legal pensions **EUR 69,047.1m 2025** / **66,475.4m 2024** (path 48.3->69.0bn 2019-25)
  - **Sal 39,880.9** · **Fonct 23,428.5** · **Ind 5,737.7** m (2025)
  - Retraite **60,519.0** · Survie **8,528.1** m; min-benef spend **20,751.9** m
  - FPD paid **68,244.9m 2024** (WN 40.2 / Ambt 22.45 / ZS 5.59); package **69.4bn**
  - Staff **2,165** HC / **2,013.75 FTE** / Smals **174**; min pensioners **997,562** (41pct)
- Wrote: sources +2; budgets +38; cmt +1; lb +7; entity note; FOI **gap_fpd_beheer_igo_l5** ready + draft; rq_376=done; spawn **rq_377**; ticks=385
- FOI: beheer 2024-25 + IGO + Ethias/rents inside 69.4bn human send only
- Next: prio5 **rq_377**; deferred **rq_116** SWA

### 2026-08-01T07:45:00Z - tick 386
- Unit: **rq_377** (FOI-adjacent hole-fill - **RSVZ/INASTI gestion globale independants + dual CAS L5**)
- Found (strong primary CoA Cahier 2025 SS + RSVZ Chiffres 2024):
  - GG indep **dep EUR 6,523.1m 2024** (pens 5,597.8 · invalidite 915.4 · path 5.54/6.01/6.52)
  - GG indep **rec 10,293.0m** · **cotis 5,627.8m** (personnes 5,322.3 · societes 297.9) · solde **-71.4m**
  - Dotations Etat **935.1m** · altfin **3,650.9m** · unpaid hors bilan **1,552.6m** cotis + **104.9m**
  - INASTI missions **9,712.4m** / beheer **106.9m** 2023
  - Affiliates **1,299,825** · CAS top ACERTA 341k · XERIUS 247k · LIANTIS 241k · societes 707k
- Wrote: sources +2; budgets +64; cmt +1; lb +7; entity; FOI **gap_rsvz_cas_admin_l5** ready; rq_377=done; spawn **rq_378**; ticks=386
- FOI: CAS admin fees + beheer 2024-25 + recovery path human send only
- Next: prio5 **rq_378**; deferred **rq_116** SWA

### 2026-08-01T08:15:00Z - tick 387
- Unit: **rq_378** (FOI-adjacent hole-fill - **ONVA/RJV pecules vacances dual CSV + Fedris/CAAMI CoA L5**)
- Found (strong primary CoA Cahier 2025 SS Tables 8/10/11/27):
  - ONVA **dep EUR 6,381.2m** / rec **6,481.3m** / solde **+100.1m** 2024
  - Pecules **6,338.5m**: ONVA-caisse **~64.1% (~4,063m)** · 9 private CSV **~2,276m**
  - Cotis patronales **5,698.5m** · ONEM contrib **30.7m** · **FFE loan 200m** 0% 15y
  - Beheer **23.6m** 2023; beneficiaires **1,661,304** ouvriers 2024
  - Fedris **596.4m** (AT 327.1 MP 214.8 amiante 23.6) · CAAMI missions **642.6m**
- Wrote: sources +1; budgets +44; cmt +2; lb +8; entities; FOI **gap_onva_csv_l5** ready; rq_378=done; spawn **rq_379**; ticks=387
- FOI: named CSV cash + beheer 2024-25 + FFE contract human send only
- Next: prio5 **rq_379**; deferred **rq_116** SWA

### 2026-08-01T08:45:00Z - tick 388
- Unit: **rq_379** (FOI-adjacent hole-fill - **ONSS Gestion globale salaries L5 + pensions publiques**)
- Found (strong primary CoA Cahier 2025 SS Tables 1-3 12-16):
  - GG sal **prestations EUR 60,514.7m 2024** (pens **40,125** · inv **13,449** · chom **6,391** · AT/MP **542**)
  - Rec **99,197.8m** · cotis **65,768.6m** (sal 60,186 · locaux 5,126) · solde **+83.9m**
  - Dots **9,488.8m** (equilibre 6,142 · ord 2,765 · federees 582) · altfin **21,367.4m**
  - Reductions cotis **3,592.6m** (bonus emploi 1,679 · structurelles 1,866) + cibles dep **920m**
  - Pensions publiques **21,041m** · dot Etat **15,472m** · fonds solidarise **3,436m**
  - INAMI soins consol dep **37,041m** · retenue pensions **1,753m**
- Wrote: sources +1; budgets +102; cmt +1; lb +8; entity; FOI **gap_onss_gg_transfer_l5** ready; rq_379=done; spawn **rq_380**; ticks=388
- FOI: IPSS transfer cash codes + equilibre path human send only
- Next: prio5 **rq_380** (progress@390 next); deferred **rq_116** SWA

### 2026-08-01T09:15:00Z - tick 389
- Unit: **rq_380** (FOI-adjacent hole-fill - **federal social assistance L5 IGO+handicap+RIS + Entity I social macro**)
- Found (strong primary CoA Budget 2026 + PensionStat GRAPA):
  - Entity I dep **268.7bn** · social **155.5bn** · SS prest **135.5bn** · cotis **86.1bn**
  - **Handicap 3.3bn** · **IGO/ages 1.0bn** · **RIS CPAS 2.2bn** (+Ukraine **299m**) = package **6.5bn**
  - Chomage **3.9bn** 2026 (vs 5.7bn; -31.5pct) · pens **72bn** · health **41.3bn** · indemn **15.9bn**
  - GRAPA stock **119,651** Jan2025 · avg **719 EUR/mo** · annualized **~1.03bn** medium dual 1.0bn
- Wrote: sources +2; budgets +36; cmt +1; lb +7; entity spp_is; FOI **gap_igo_handicap_ris_cash_codes** ready; rq_380=done; spawn **rq_381** progress@390; ticks=389
- FOI: AB cash codes handicap/IGO/RIS human send only
- Next: **mandatory progress@390** (rq_381); deferred **rq_116** SWA

### 2026-08-01T09:45:00Z - tick 390
- Unit: **rq_381** (**progress milestone @390** - coverage % + waste top10 refresh; no new euro invent)
- Snapshot (honest order-of-magnitude vs TE EUR 347.956 bn):
  - **A L0 / B L1:** **100%** (unchanged strong)
  - **C L2:** **~96-99%** (up from ~95-98% @380) - GG sal 60.5bn + FPD 69bn + RIZIV 45bn + RSVZ 6.52 + ONVA 6.38 + social assist 6.5 + Entity I social 155 class
  - **D L5:** **~21-32%** generous (RIZIV objectifs sector L5; dual CAS/CSV counts; GRAPA stock; residual FOI)
  - **E FOI ready:** **~195** (answered ~5; total FOI rows ~202)
- Inventory: budgets ~5151 - cmt ~673 - lb ~966 - entities ~354 - sources ~702
- Waste top10: **stable** fossil/company-cars/cheque/EIWT mega items (entitlement megas lower absurdity)
- Dual/off-TE map: ONSS cotis financing, Entity I 268.7bn perimeter != ESA TE 2025
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_381=done; spawn **rq_382**; ticks=390
- FOI: no new gap this tick (progress only)
- Next: prio5 **rq_382** hole-fill; deferred **rq_116** SWA

### 2026-08-01T10:15:00Z - tick 391
- Unit: **rq_382** (FOI-adjacent hole-fill - **SPF Justice 2026 + prison envelope + Fedasil cut + BE-Watt**)
- Found (strong primary CoA Budget 2026):
  - Justice section **EUR 2,843m** (+82) + dedicated provisions **465.5m** (sec 112.5 · surpop 50 · infra 259 · effic 44)
  - Prison overcrowding envelope **840m 2026-2029** (600 infra + 240 structural); TF needs **1.1bn** medium
  - Food detainees **25.2m** underfund **10.18m**; security provision total **366.9m**
  - Fedasil package **802.2m** 2026 (dot 702.2 + prov 100; -153 vs 2025); savings **247m** / **688m by 2029**
  - BE-Watt Phoenix **487.6m** + Q1 prov **146m**; energy norm **249m**; Fluxys earmark **100m**
  - RIS DIS detail **2,084.5** + loi1965 **156.4** = **2,240.9m**
- Wrote: sources +1; budgets +39; cmt +2; lb +8; entities; FOI **gap_justice_provisions_l5_2026** ready; rq_382=done; spawn **rq_383**; ticks=391
- FOI: Justice provision project list human send only
- Next: prio5 **rq_383**; deferred **rq_116** SWA

### 2026-08-01T10:45:00Z - tick 392
- Unit: **rq_383** (FOI-adjacent hole-fill - **Federal police I-Police cancel + NATO 2pct defence path**)
- Found (strong primary CoA Budget 2026):
  - **I-Police cancelled:** liquidated **EUR 76.7m** of **299m**; claim **228.1m** (49.9 invoices + 178.5 damages of which lost-gain **149m** soft)
  - Residual prog 17.80.4 eng **7.8** / liq **15.1m** 2026 (Focus/digitalisation)
  - Police FTE **13,980** end-2025 (~flat vs 13,962 2021); target **14,280**; ops +**87.5m** from security provision
  - Grandes Villes police **43.6m** 2025-29; eng **9.9** / liq **13.2m** 2026
  - **NATO effort 2026 EUR 13,095.8m** (s16 liq **10,769.6**; external **2,326**; mil pens **1,688**)
  - Extra defence package **16,783m** 2025-29; temp fin CIT Russia **1,163** + Belfius **500**
  - DGD liq **1,040.3m** 2026; SPF Finance **2.4bn** (personnel 1.56)
- Wrote: sources +1; budgets +56; cmt +2; lb +8; entity police_federale; FOI **gap_ipolice_claim_l5** ready prio8; rq_383=done; spawn **rq_384**; ticks=392
- FOI: I-Police claim/settlement human send only
- Next: prio5 **rq_384**; deferred **rq_116** SWA

### 2026-08-01T11:15:00Z - tick 393
- Unit: **rq_384** (FOI-adjacent hole-fill - **BOSA interdept provisions 2.13bn L5 + specialty derogations**)
- Found (strong primary CoA Budget 2026):
  - Interdept provisions **eng EUR 2,125.8m** / **liq 2,128.0m** (prog 06.90.1)
  - **Generale 829.8m**: justice divers **618.3** (prison infra **259** · ESA **176** · econ sociale **50** · admin reorg **36** · Tria **5.3** · CPL **2.7**) · Fedasil **100** · bpost **78** · vulnerables **33.5**
  - **Securite 366.9m** (already dual Justice/Police/Migration)
  - Path generale **630.7 / 1,374.7 / 1,005.2** 2027-29; justice divers spike **1,206.7** 2028
  - Specialty hollowed: Defence eng redistributable **20.1bn**; Justice **2.5bn**; Police **1.6bn**; 2024 redistribs **454m**
- Wrote: sources +1; budgets +30; cmt +1; lb +8; entity fod_bosa; FOI **gap_bosa_provisions_l5_2026** ready prio7; rq_384=done; spawn **rq_385**; ticks=393
- FOI: residual provision lines + CM transfer log human send only
- Next: prio5 **rq_385**; deferred **rq_116** SWA

### 2026-08-01T11:45:00Z - tick 394
- Unit: **rq_385** (FOI-adjacent hole-fill - **LPM militaire 2026-2034 investissements 33.784bn L5**)
- Found (strong primary Kamer 56K1143):
  - **Engagement plafond art.8: EUR 33,784.15m** constants 2026 for major equipment 2026-2034
  - Staff 2034: **34,500** active · **12,800** reserve · **8,500** civil; recruit 2026: 2800/1050/960
  - Largest packages: Combat Manoeuvre **6,003.8m** · SBAMD **4,014.0m** · F-35+11 **3,387.4m** · ASWF-3 **1,918.2m** · CSS **1,352.6m** · Joint land **1,535.5m** · mine warfare **1,170.9m**
  - Mapped named packages sum **~27.1bn** of 33.8bn (residual RPAS/SOF/refuel/medical etc)
  - DIRS: 3pct defence budget + complements **35-51m/yr** const26
- Wrote: sources +1; budgets +68; cmt +1; lb +7; entity; FOI **gap_lpm_contract_cash_2026_34** ready prio7; rq_385=done; spawn **rq_386**; ticks=394
- FOI: signed contract cash-by-year human send only
- Next: prio5 **rq_386**; deferred **rq_116** SWA

### 2026-08-01T12:15:00Z - tick 395
- Unit: **rq_386** (FOI-adjacent hole-fill - **federal non-fiscal receipts L5 + liq 92bn + ETS blocked 1.8bn + EPF dual + ET prefin 40.7m**)
- Found (strong primary CoA Budget 2026):
  - Federal **liquidation credits 92.0bn** 2026 (vs 89.5bn 2025 excl IMF); cells appui **4.2** - autorite **22.7** - eco **6.6** - sociale **34.5** - specific **24.0**
  - Deltas: EU +**1.2bn** - F-35/drone FX +**321m** - 6th reform dots +**228.1m** - Infrabel credit +**100m** - SFPIM Defence +**144m**
  - Non-fiscal **6,470m** (financing **5,850m**): Belfius div **915** (415+500) - customs retention **784.5** - CDC exceptional **475** - demat **177.3** - Fluxys **100** - nuclear decom **100**
  - **ETS blocked 1.8bn** SPF Sante waiting account; federal receipts 65.8->38.8m; climate spend only **8m** (Kyoto 6 + Mobility 2)
  - **bpost overcomp claim 89.2m** budgeted since 2024 **never cashed**
  - EPF BE est **177m** (mil12+nonmil165) vs AE 14.8 + Def 8.2 + Ukraine prov 120; possible gap **34m**
  - Electronic monitoring prefin **40.7m** 2025-27 (VL 23.8 - FWB 16.8 - DG 0.07)
  - DGD liq **1,040.3m** 2026 path 957 2027; FAD17 vol **64.2m**/10y
  - Employer SSC new statutaires 10m 2026 path 284/365; Defence 3.7->297.3 by 2034
- Wrote: sources +2; budgets +57; cmt +4; lb +8; entities +2; FOI **gap_ets_blocked_kyoto_l5** + **gap_bpost_overcomp_claim_89m** ready; rq_386=done; spawn **rq_387**; ticks=395
- FOI: ETS 1.8bn unlock + ranking human send; bpost claim legal report human send only
- Next: prio5 **rq_387**; deferred **rq_116** SWA

### 2026-08-01T12:45:00Z - tick 396
- Unit: **rq_387** (FOI-adjacent hole-fill - **SS Part III CoA 2026: consol 148bn + ONSS red 5.17bn + Tour Midi + pens/INAMI/RTW/chom**)
- Found (strong primary CoA Budget 2026 Part III):
  - SS consol **rec 148,017.2m** / **dep 147,858.5m**; cotis **85,525** · subv PP **27,679** · altfin **27,222**
  - Prest **135,492**; GG sal **63,342** (pens 43,271 MI 14,879 chom **4,638**); sante obj **41,297**; pens pub **22,828**
  - ONSS cotis **69,592**; red recettes **4,290** (struct 2,427 + bonus emploi 1,822) + ciblees dep **880** = pack **5,170m**
  - ONSS dots PP **8,851** (equilibre **5,654** -1.1bn); altfin ONSS **23,392** / INASTI **3,829**
  - **Tour du Midi** total **177.7m** (ONSS **168.8** 2027-31; SEC -6m 2026)
  - Pension reform save path **807/1304/1787/2229** 2027-30 (2026 delayed -64m)
  - INAMI savings pack **764.5** (drugs 401.9 doctors 213.2 hosp 50); ticket mod **62.5** of 125
  - RTW invalidite save **202.9 -> 1,928.7** by 2029 (recontrol 1,066; annual ext 869)
  - Chomage time-limit **1,685.2m** save; prest -28.2pct to 4,638m
- Wrote: sources +1; budgets +75; cmt +7; lb +8; FOI **gap_tour_midi_contracts_l5** + **gap_rtw_invalidite_method_l5** ready; rq_387=done; spawn **rq_388**; ticks=396
- FOI: Tour Midi contracts + RTW method notes human send only
- Next: prio5 **rq_388**; deferred **rq_116** SWA

### 2026-08-01T13:15:00Z - tick 397
- Unit: **rq_388** (FOI-adjacent hole-fill - **transversal antifraud+centimes+NATO fin + chomage multi-year reform residual**)
- Found (strong/medium primary CoA Budget 2026 Ch.II transversal + SS chomage 5.2-5.3):
  - Antifraud dual **600m** 2026 (300 fiscal + 300 social) path **1.2bn** 2029; SIRS ~370m 2025 est; agents **377**; Compliance IT **72.9m**/4y net -13.2->+472 2029
  - Parcel fee 2EUR **210m gross DROPPED** (EU 3EUR path Jul2026 TBD)
  - Indexation-en-centimes Entity I **272 / 391 / 754 / 883** 2026-29; employer contrib **+271m** 2026
  - Admin reorg save path **300m** end legislature (unobjectified)
  - NATO effort **13,095.8m** 2026 (99.9pct of 13,107 need); s16 **10,770** external **2,326**; standardisation **167.5** path 750 2029
  - Defence temp fin 2026: CIT Russia **1,163** + Belfius **500**; extra pack **16,783** 2025-29; asset optim **3,170** TBD
  - Chomage reform save **1,685 / 2,287 / 2,441 / 2,448** 2026-29; exclusions **193,904** (VL 62.7k WAL 88.6k BRU 41.7k DG 0.95k)
  - ONEM+Capac+OP gestion **20.5m** 2026; RCC reest **5.2m**; family credit **40m**; voluntary quit cost **33.6m**
- Wrote: sources +1; budgets ~70; cmt +5; lb +8; FOI **gap_antifraud_method_l5** + **gap_centimes_impl_l5** ready; rq_388=done; spawn **rq_389**; ticks=397
- FOI: antifraud method + centimes AR/IT human send only
- Next: prio5 **rq_389**; deferred **rq_116** SWA

### 2026-08-01T13:45:00Z - tick 398
- Unit: **rq_389** (FOI-adjacent hole-fill - **federal fiscal cash/SEC + IPP reform 5.6bn + VAT rates + CGT + accounts tax**)
- Found (strong/medium primary CoA Budget 2026 Part II Ch.I recettes):
  - Cash total **164.4bn** · fiscal **157.9bn** · nonfiscal **6.5bn** · transfers **92.5bn** (R&C 59.2 · SS 27.3 · EU 4.15) · V&M **71.9bn**
  - SEC after conclave **163.8bn**; cash corrections **-5.86bn**; new conclave measures **+1.38bn** SEC
  - IPP +1.16bn cash; reform phase1 **-421m** 2026; cum cost **5.6bn** by 2030 (fed **4.1bn**)
  - VAT rates reform **+580.5m** (hotels 158 culture 253 takeaway 362 phytopharma 53; resto -140)
  - CGT net **120m** 2026 (gross PM 236; cruise **600m** 2032); accounts tax double **+414m**
  - Excise env net **+273m** by 2029 (gas overstate 195 CoA); VVPR 18pct **+90m**; DLU **126m** soft (2025 only 3.1m)
  - Meal vouchers **-55.8m**; heat-pump VAT **-10.1m**; copyright forfait **+30m**
- Wrote: sources +1; budgets ~60; cmt +6; lb +8; FOI **gap_ipp_reform_aurora_l5** + **gap_cgt_method_l5** ready; rq_389=done; spawn **rq_390**; ticks=398
- FOI: IPP Aurora L5 + CGT method human send only
- Next: prio5 **rq_390**; **progress@400** mandatory next+2; deferred **rq_116** SWA

### 2026-08-01T14:15:00Z - tick 399
- Unit: **rq_390** (FOI-adjacent hole-fill - **Entity I SEC overview 244.1/268.7 deficit 24.6 + taxex inventory + conclave package**)
- Found (strong primary CoA Budget 2026 Part I Entity I):
  - Entity I **rec 244.1bn** / **dep 268.7bn** / **deficit 24.6bn** (-3.7pct GDP)
  - Tax **141.9** · SSC **86.1** (reductions **5.5** excl Maribel) · third-party **22.2**
  - Social **155.5bn** (57.9pct): SS prest **135.5** · pens **72** · health **41.3** · indemn **15.9** · chom **3.9** (-31.5pct)
  - Transfers own **66.5** (federated **59.1** · EU GNI **~5** +30pct) · eco **9.6** (rail 3.4 energy 1.5 ESA 0.41 bpost 0.155) · authority **23.2** (Defence 9.5)
  - Interest **12.2bn** (1.84pct GDP) path **17.8** / 2.5pct; taxex GG **39.4** / fed **29.7** (social 18.6 VAT6 10.6)
  - Conclave improve **~1.6bn** 2026 (fiscal net 1.6 · spend control 421 · cohesion cost 567 · social economy **50**/yr)
- Wrote: sources +1; budgets ~65; cmt +5; lb +8; FOI **gap_entity1_functional_l5** + **gap_social_economy_50m_l5** ready; rq_390=done; spawn **rq_391 progress@400**; ticks=399
- FOI: Entity I workbook + social economy places human send only
- Next: **MANDATORY progress@400 rq_391**; deferred **rq_116** SWA

### 2026-08-01T14:45:00Z - tick 400
- Unit: **rq_391** (**progress milestone @400** - coverage % + waste top10 refresh; no new euro invent)
- Snapshot (honest order-of-magnitude vs TE EUR 347.956 bn):
  - **A L0 / B L1:** **100%** (unchanged strong)
  - **C L2:** **~97-99%** (up from ~96-99% @390) - Entity I 244.1/268.7 · SS consol 148 · fed cash fiscal 157.9 · NATO 13.1 · LPM 33.8 eng
  - **D L5:** **~22-33%** generous (LPM named packages; chomage waves; VAT rate lines; RTW tables; residual FOI)
  - **E FOI ready:** **~210** (answered ~5; total FOI rows ~216)
- Inventory: budgets ~5670 · cmt ~706 · lb ~1037 · entities ~357 · sources ~729
- Waste top10: **stable** fossil/company-cars/cheque/EIWT mega items; **lb_taxex_fed_29_7bn** (29.7bn) just outside #11 at prio 8.05
- Dual/off-TE map: Entity I 268.7 != ESA TE 2025; ETS blocked 1.8bn stock; IPP reform 5.6bn path; return-effects soft
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_391=done; spawn **rq_392**; ticks=400
- FOI: no new gap this tick (progress only)
- Next: prio5 **rq_392** hole-fill; deferred **rq_116** SWA

### 2026-08-01T15:15:00Z - tick 401
- Unit: **rq_392** (FOI-adjacent hole-fill - **multi-year fiscal path BE/Entity I + EU net primary exp + FPB debt**)
- Found (strong/medium primary CoA Budget 2026 Part I Ch.III + FPB Feb):
  - BE deficit **-4.9pct** 2026 (vs -5.2 reest 2025); Entity I **-3.7** · Entity II **-1.2**
  - MTFS path to **-3.0pct** 2029; DBP worse by **0.5/0.3pp** 2025-26
  - Conclave improves Entity I **€9.2bn** by 2029 (~half of 18.5bn overrun vs 3pct)
  - Expose end legislature Entity I deficit **€31.2bn** (4.3pct); debt **85.6→90.3pct**
  - FPB post-measures Entity I **€36.5bn** (-5.0pct) = **€5.3bn** worse; GG debt **109.4 / 116.6 / 122.2** 2026-31
  - Net primary margin Entity I **~€0.9bn** under CSF 2025-26; military escape to 2028
  - IPP stretch **+€1bn** 2029 optical; regions EU **€500m**/yr from 2028 (no agreement)
  - ET prefin SEC artefact **€18.3m** improves GG artificially
- Wrote: sources +1; budgets ~40; cmt +3; lb +8; FOI **gap_entity1_pluriannuel_workbook** + **gap_regions_eu_500m_agreement** ready; rq_392=done; spawn **rq_393**; ticks=401
- FOI: pluriannuel workbook + regions EU 500m agreement human send only
- Next: prio5 **rq_393**; deferred **rq_116** SWA

### 2026-08-01T15:45:00Z - tick 402
- Unit: **rq_393** (FOI-adjacent hole-fill - **FPB dual outlooks Feb+Jun 2026 deficit/debt/employment**)
- Found (strong primary FPB press tables):
  - **Feb2026:** GDP **1.1** 2026; deficit **-4.9 → -6.3** 2026-31; debt **107.4 → 122.2**; emp rate **72.8→75.2**; jobs **+276k**; ONEM benef **-138k**; admin U **-53k**; CPI **1.9** (ETS2 2.2 in 2028)
  - **Jun2026 (ME shock):** GDP **0.7** 2026; CPI **3.4**; deficit stabilise **-5.1** then **-6.4** 2031; debt **107.9→122.3**; interest **3.5pct GDP** 2031; jobs **+20k** 2026 / **+230k** 2027-31; emp rate **74.8** 2031; admin U **-34k**; real income **-0.7** 2026
  - Dual vs DBP/CoA: Jun **worsens** 2026 deficit by **0.2pp** vs Feb/DBP -4.9; employment goal 78 still far
- Wrote: sources +2; budgets ~70; cmt +3; lb +8; FOI **gap_fpb_entity1_split_jun2026** ready; rq_393=done; spawn **rq_394**; ticks=402
- FOI: Entity I/II split from full FPB Jun report human send only
- Next: prio5 **rq_394**; deferred **rq_116** SWA

### 2026-08-01T16:15:00Z - tick 403
- Unit: **rq_394** (FOI-adjacent hole-fill - **CEV Ageing 2026 + regional economic outlooks 2026-2031**)
- Found (strong primary BFP/CEV/IWEPS press):
  - **CEV2026:** social exp **25.7%→27.2% GDP** 2025-50; ageing cost **+1.5pp** to 2070; health **+2.1pp** · pens **+0.7pp**; reform saves **1.4pp** pens; low-prod cost **3.3pp**; benefit ratio **-13%** by 2070; pensioner poverty **8.5%** 2024
  - **Regional 2026:** GDP VL **0.7** WAL **0.8** BRU **0.5**; 2027-31 avg VL **1.4** WAL **1.1** BRU **0.8**
  - Emp rates 2031: VL **79.0** WAL **70.4** BRU **65.6** (from 77.3/67.9/63.9)
  - Deficits end: VL **~€2bn** · WAL **€1.6bn** · FWB **€1.2bn** 2029 · BRU **€0.8bn** 2029
  - Savings rates 2031: VL **14.1%** WAL **9.8%** BRU **4.4%**
- Wrote: sources +2; budgets ~45; cmt +2; lb +8; FOI **gap_cev_2026_table_l5** + **gap_reg_outlook_deficit_series** ready; rq_394=done; spawn **rq_395**; ticks=403
- FOI: CEV full tables + regional deficit EUR series human send only
- Next: prio5 **rq_395**; deferred **rq_116** SWA

### 2026-08-01T16:45:00Z - tick 404
- Unit: **rq_395** (FOI-adjacent hole-fill - **ICN EDP 2025 full EUR + NBB Jun 2026 projections**)
- Found (strong primary ICN 20 Apr 2026 + NBB 12 Jun 2026):
  - **ICN 2025:** TE **€347.956bn** · primary **€333.7bn** · interest **€14.3bn** · rec **€314.7bn** · deficit **−€33.2bn (−5.2%)** · debt **€692.5bn (107.9%)** · GDP **€642.0bn**
  - Subsectors: fed **−€24.1bn** · C&R **−€8.9bn** · local **−€0.4bn** · SS **+€0.17bn**
  - C&R: VL **−€4.1bn** · WAL **−€2.9bn** · FWB **−€1.5bn** · BRU **−€1.0bn** · ETS interreg **+€0.56bn**
  - Defence COFOG **€8.8bn (1.4% GDP)** vs NATO cash 2%; orders pending **0.6% GDP**
  - Debt shares: fed **80.0%** · C&R **18.4%** (€127.6bn) · local 4.0% · SS −2.4%
  - **NBB Jun:** GDP **0.6%** 2026 · HICP **3.4%** · deficit **−5.3/−5.5/−5.7** · debt **111.3→114.8** · jobs **+16/35/42k** · UI **~100k** lost H1-26
- Wrote: sources +2; budgets ~70; cmt +2; lb +8; FOI **gap_icn_edp_oct2026_refresh** ready seasonal; rq_395=done; spawn **rq_396**; ticks=404
- FOI: Oct EDP refresh seasonal human send
- Next: prio5 **rq_396**; deferred **rq_116** SWA

### 2026-08-01T17:15:00Z - tick 405
- Unit: **rq_396** (FOI-adjacent hole-fill - **HermReg full PDF+XLSX Entity II multi-year financing balances**)
- Found (strong primary BFP HermReg Jul 2026 PDF Ch.5 + DATA_HermReg_FR.xlsx sheet8 mEUR):
  - **VL** dep **76.284bn** 2026 / rec 73.237 / solde **-3.049**; path solde **-5.02/-3.85/-3.05/-0.90/-1.74/-2.00/-1.89/-1.44** 2024-31; interest **1.302?2.248bn**
  - **WAL** dep **21.272bn** 2026 / solde **-2.126**; path **-2.06/-2.70/-2.13/-1.55/-1.86/-1.58/-1.56/-1.62**; int **0.99?1.52bn**
  - **FWB** dep **28.121bn** 2026 / solde **-1.828**; path **-1.48/-1.45/-1.83/-1.36/-1.45/-1.23/-1.30/-1.30**; int **0.42?0.78bn**
  - **BCR+COCOM consol** solde **-1.56/-0.91/-1.02/-0.93/-0.91/-0.78/-0.80/-0.86**; BCR dep 7.639 / COCOM 1.974 2026
  - **C&R ensemble** T13 %GDP solde **-1.5?-0.5** 2024-31; 2026 rec 18.5 / dep 19.7 / int 0.5
  - Method: ETS2 from 2028 booked **interreg** (no share key); federal depositary only
  - Residual: Oosterweel-ex VL series not tabulated; DG not in HermReg C&R chapter
- Wrote: sources +2; budgets ~90; cmt +5; lb +8; raw PDF+XLSX; FOI **gap_reg_outlook_deficit_series ? answered**; rq_396=done; spawn **rq_397**; ticks=405
- FOI: closed public; optional residual Oosterweel-ex/DG only (not reopened)
- Next: prio5 **rq_397**; deferred **rq_116** SWA

### 2026-08-01T17:45:00Z - tick 406
- Unit: **rq_397** (FOI-adjacent hole-fill - **CEV 2026 full PDF+XLSX social exp branch Entity I/II**)
- Found (strong primary CEV Jul 2026 FOR_VERG2026 + DATA_FOR_VERG_FR.xlsx):
  - **Total social** %GDP **25.7 (2025-26) ? 26.3 (2031) ? 27.0 (2040) ? 27.2 (2050-70)**; ageing cost **+1.5pp**
  - **Pensions** 11.3?12.0 (+0.7); reform saves **1.4pp**; salari� 6.6?7.4 public 3.8?3.2 indep 0.9?1.4
  - **Health** 8.0?10.2 (**+2.1**); acute 6.1?7.3; LTC 1.9?2.9 (Entity II LTC 1.5?2.2; zorgpremie 0.1)
  - **UI** 1.0?0.4 (-0.6 time-limit); incap 2.3?2.2; family 1.3?1.0
  - **Entity I** 21.6?22.8 / **Entity II** 4.1?4.5-4.7; dual HermReg cash
  - **GDP const2025** 642/642/679/885/1169 bn 2025/26/31/50/70 ? total social ~**�165bn** 2025 class
  - Stocks: salari� pensions **2.11m?3.11m**; public 0.50?0.65; GRAPA 0.12?0.13
  - Poverty income2024: pop **11%** pensioners **8.5%** unemp **40%** workers 4%; threshold **�1565**/mo
  - Benefit ratio **-13%** by 2070; low-prod sens ageing **3.3pp** / BR -4%
- Wrote: sources +2; budgets ~50; cmt +3; lb +8; raw PDF+XLSX; FOI **gap_cev_2026_table_l5 ? answered**; rq_397=done; spawn **rq_398**; ticks=406
- FOI: closed public; optional residual benefit-ratio annual vector only
- Next: prio5 **rq_398**; deferred **rq_116** SWA

### 2026-08-01T18:15:00Z - tick 407
- Unit: **rq_398** (FOI-adjacent hole-fill - **flexi-jobs CoA+BFP art.192 evaluation ONSS volume + HERMES fiscal**)
- Found (strong primary REP_FLEXIJOBS / CoA+BFP Jan 2026 report):
  - Volume end-2024: **184360** workers � **~14m** hours � Q4 FTE **29500** (<1pct of 3.4m RSZ FTE)
  - **Wage mass EUR 220.071m** (from 4.769m early path); avg hour M **16.38** / F **15.00**; **~85pct Flanders**; 65+ share **18pct**
  - Worker flexi: no PIT/SSC; employer special rate **28pct** legal SSC (table8)
  - HERMES abolish **horeca** flexi from 2026 ? 2030 saldo **+105.8m (V1 supply kept)** / **+212.9m (V2 supply lost)** = **+0.01 / +0.03pp GDP**
  - Ex ante 2026: flexi wage **-294m** ? regular/black **+386m** net **+92m**; employer SSC net **-43m**
  - Goals: blackwork detections **not down** overall; event-sector abuse analysis **blocked** (short window + unclear improper-use definition)
  - Non-pensioner tax-free cap **12k EUR/yr** (+125pct SSC penalty path)
- Wrote: sources +1; budgets +7; cmt +2; lb +8; raw PDF; FOI **gap_flexi_te_multiyear** ready; rq_398=done; spawn **rq_399**; ticks=407
- FOI: multi-year all-sector TE matrix human send only
- Next: prio5 **rq_399**; deferred **rq_116** SWA

### 2026-08-01T18:45:00Z - tick 408
- Unit: **rq_399** (FOI-adjacent hole-fill - **FPB Jun midterm DATA_FOR_MLT Entity I/II + GG path**)
- Found (strong primary FOR_MIDTERM + DATA_FOR_MLT_FR.xlsx T17-T24/T21 mEUR):
  - **GG** solde **-27.1/-32.9/-33.7/-35.8/-38.7/-44.3/-47.2/-50.0 bn** 2024-31; dep **361.8bn** 2026; interest **14.3->27.5bn**; primary **-17.1bn** 2026
  - **Federal** solde **-23.7bn** 2026 path **-45.0bn** 2031; dep **188.9bn**; interest **13.5->22.0bn**
  - **SS** solde **-1.59bn** 2026 (rare deficit) then near zero; prest **122.7bn**; UI pure **5.60->4.26bn** 2025-26; health nature **40.9bn**; pens **59.3bn**
  - **Entity I** (fed+SS unconsol) solde **-25.3bn** 2026 -> **-45.9bn** 2031
  - **C&R** solde **-8.14bn** 2026 -> **-3.78bn** 2031; interest **3.25->5.38bn**
  - **Local** solde **-0.27bn** 2026; **Entity II** (C&R+loc) **-8.41bn** 2026 -> **-4.07bn** 2031
  - **T21 federated:** VL **-3.05** FWB **-1.83** WAL **-2.13** BRU **-1.02** Autres **-0.12** 2026; Autres **+1.4bn** class 2028+ (ETS2)
- Wrote: sources +2; budgets ~200; cmt +2; lb +8; raw PDF+XLSX; FOI **gap_fpb_entity1_split_jun2026 -> answered**; rq_399=done; spawn **rq_400**; ticks=408
- FOI: closed public; residual consolidated Entity definition optional
- Next: prio5 **rq_400**; **progress@410** in 2 ticks; deferred **rq_116** SWA

### 2026-08-01T19:15:00Z - tick 409
- Unit: **rq_400** (FOI-adjacent hole-fill - **FPB midterm T10 labour cost reductions package ~23-29bn**)
- Found (strong primary DATA_FOR_MLT T10 mEUR 2024-2031):
  - **Employer total** **22.2/23.0/23.5/24.0/24.4/25.1/26.0/26.6 bn** 2024-31
  - **+ Employee SSC** 1.73/1.73/1.83/.../2.58 -> **package 25.3bn 2026 / 29.2bn 2031**
  - Facial tax-shift rate **8.9bn** 2026; general diverse SSC **11.1bn**
  - Night/shift **2.12bn**; R&D firms **1.48bn**; overtime 0.21; subvention gen 0.29
  - Maribel 0.92+0.17; hospital/other SS 0.98; via SS total **2.07bn**
  - Regions **4.92bn** 2026: titres-services **2.51**; ETA adapted work **0.87**; other H **1.45**
  - Bonus emploi **1.79bn** 2026 (spike **2.29** 2028); dual NBB 25.1bn business subs 2024 close match
- Wrote: sources +1; budgets ~200; cmt +1; lb +8; FOI **gap_t10_l5_night_rd** ready; rq_400=done; spawn **rq_401 progress@410**; ticks=409
- FOI: night/shift + R&D top50 L5 human send only
- Next: **MANDATORY progress@410 rq_401**; deferred **rq_116** SWA

### 2026-08-01T19:45:00Z - tick 410
- Unit: **rq_401** (**progress milestone @410** - coverage % + waste top10 refresh; no new euro invent)
- Snapshot (honest order-of-magnitude vs TE EUR 347.956 bn):
  - **A L0 / B L1:** **100%** (unchanged strong)
  - **C L2:** **~98-99%** (up from ~97-99% @400) - midterm Entity I/II � HermReg C&R � CEV branch � T10 labour 23.5bn � GG interest path 27.5bn
  - **D L5:** **~22-34%** generous (flexi 220m; T10 instrument lines not firm L5; residual FOI ASBL/firm)
  - **E FOI ready:** **~214** (answered **~8**; total FOI rows **~224**)
- Inventory: budgets ~6450 � cmt ~734 � lb ~1114 � entities ~357 � sources ~749
- Waste top10: **stable** fossil/company-cars/cheque/EIWT; **lb_t10_package_total_25_3bn** (25.3bn) and **lb_mlt_gg_interest_27_5bn** just outside at prio 7.55
- Dual/off-TE: T10 labour package dual NBB 25.1bn; CEV 25.7-27.2pct GDP; Entity I deficit path 25.3-45.9bn
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_401=done; spawn **rq_402**; ticks=410
- FOI: no new gap this tick (progress only)
- Next: prio5 **rq_402** hole-fill; deferred **rq_116** SWA

### 2026-08-01T20:15:00Z - tick 411
- Unit: **rq_402** (FOI-adjacent hole-fill - **BDA Review/Outlook 2025-26 + FPB pension reform REP 13299**)
- Found (strong primary):
  - **BDA federal debt** **EUR 552.69bn** end-2025 (+34.0 vs 518.68); OLO **462.8** � TC **42.9** � EMTN **12.3** � EU SURE/RRF **6.3**
  - Indicators: avg life **9.98y** � duration **7.27y** � implicit cost **2.01%** � 12m refi **15.64%** � new LT issue cost **3.12%**
  - **2025 realised:** gross **53.31** � net **28.35** � OLO issue **45.71** � EMTN **3.52** � green taps **2.7** � syndications **19**
  - **2026 plan:** gross **59.55** � net **26.37** � OLO **51.60** � MLT total **56.32** � redemptions **28.0** + buybacks **4.6** � RRF/SAFE **1.32** � green eligible **5.0** (no new Green OLO)
  - **2028 LT wall** redemptions **39.63bn**; Fitch **A+** stable (S&P AA neg / Moody Aa3 neg)
  - **Pension reform cumul save (const2024 mEUR):** **-349/-702/-1683/-2656/-3595/-3757/-4081** 2025-31; ageing cost **-1.3pp GDP** (pens **-1.4** public **-0.7** salarie **-0.6**); GDP **+0.4%** emp rate **+0.3pp** 2070
  - Social: RR public **-15.2%** salarie **-7.2%** 2070; BR public **-13.2%** salarie **-6.2%**; gender gap widens private schemes
- Wrote: sources +2; budgets ~30; cmt +2; lb +8; raw BDA+FPB PDFs; rq_402=done; spawn **rq_403**; ticks=411
- FOI: none new (public complete for aggregates; residual interactions/poverty distrib separate FPB report optional)
- Next: prio5 **rq_403**; deferred **rq_116** SWA

### 2026-08-01T20:45:00Z - tick 412
- Unit: **rq_403** (FOI-adjacent hole-fill - **FPB PROMES AMI health spend 2025-2035 by care type**)
- Found (strong primary FOR_PROMES_13296 real 2025 prices mEUR):
  - **AMI total** **37666 -> 48599** (+**10933** / **+2.6%/yr**); **6% GDP** 2025
  - Shares 2025: doctors **31.0%** � hospital day **22.9%** � pharma net **18.6%** � home nursing **5.9%** � dental 4.3 � kine 3.5
  - **Pharma net** 6988->10401 (**+3412** / +4.1%/yr); gross 8961->14455; **art.81/111 comp** 1973->4054 (**+106%**)
  - Doctors 11675->13814 (**+2182**); hospital day 8629->10686 (**+2057**); home nursing **+869**; kine **+758**
  - Maisons medicales 389->886 (**+8.6%/yr**); consult/visits +1093
  - Demo 2026-35: **+10198** of which aging **2147 (21%)** + pop **1151 (11%)** = **32%**; 65+ drive **66%** of rise
  - Perimeter: AMI only (excl regional/local + part BMF hospital)
- Wrote: sources +1; budgets ~40; cmt +1; lb +8; raw PDF; FOI **gap_inami_art81_l5** ready; rq_403=done; spawn **rq_404**; ticks=412
- FOI: art.81/111 top contracts L5 human send only
- Next: prio5 **rq_404**; deferred **rq_116** SWA

### 2026-08-01T21:15:00Z - tick 413
- Unit: **rq_404** (FOI-adjacent hole-fill - **FPB pension reform distributive effects REP 13208 horizon 2029**)
- Found (strong primary Replica+EXPEDITION, dual fiscal 13299):
  - Baseline Dec2024 avg gross: **all 2123 EUR/mo** � new **2040** � D1 **453** � D10 **4363** (ratio **9.6**) � Gini **0.26**
  - Gender: men **2361** / women **1902** gap **19.4%**; D1 is **75%** women
  - Poverty sim: all **5.5%** new **5.9%** (threshold **1350 EUR/mo**); dual SILC AROP pensioners **8.5%**
  - **Reform 2029 cumul (sim measures):** avg **-2.6%** all / **-2.4%** new (cruise **-5.6%**); D1 **-3.3%/-7.4%**; D10 **-1.8%/+1.1%**
  - Inequality new: D10/D1 **+9.1%** � Gini **+5.5%**; all **+1.5%/+1.7%**
  - Poverty **+0.6pp** all (to 6.1%) � **+0.4pp** new (to 6.3%); mainly min-pension welvaart freeze
  - Abs cents: D1 loses **~15 EUR/mo** vs D10 **~79 EUR/mo** (2024 prices)
  - Women new **-2.6%** vs men **-2.3%** (gap widens among new); stock gap narrows slightly
  - Partial set: military/NMBS/sick-pension/household rate not simulated
- Wrote: sources +1; budgets ~7 unit rows; cmt +1; lb +8; raw PDF; rq_404=done; spawn **rq_405**; ticks=413
- FOI: none new (public complete for sim indicators; residual unsimulated measures when modalities fixed)
- Next: prio5 **rq_405**; deferred **rq_116** SWA

### 2026-08-01T21:45:00Z - tick 414
- Unit: **rq_405** (FOI-adjacent hole-fill - **NBB/NAI COFOG 2024 full function map Table1**)
- Found (strong primary press 17 Dec 2025 + Table1 mEUR):
  - **TE 335.288bn** 2024 (dual EDP 335.1bn class)
  - **Social protection 126.541bn (37.7%)** — old age/survivors **71.792** · sick/dis **24.255** · unemp **6.575** · other **23.919**
  - **Health 49.580bn (14.8%)** · **GPS 44.306** (interest **14.476** 4.3% rebound from 3.2% 2022) · **econ 39.854** · **edu 39.284**
  - **Defence 7.946bn (2.4% TE)** highest share 20y; **1.3% GDP** both NATO cash and COFOG after F-35 delivery spike
  - Order/safety 10.648 · culture 7.552 · env 7.176 · housing 2.401
  - Unemp share **halved in 20y** (5.3%→2.0%); sick/dis **5.0%→7.2%**; pens **18.4%→21.4%**
- Wrote: sources +1; budgets +17; cmt +1; lb +8; raw PDF; FOI gap_defence note; rq_405=done; spawn **rq_406**; ticks=414
- FOI: no new gap (function L1 complete); residual L5 + defence signed cash still ready human send
- Next: prio5 **rq_406**; deferred **rq_116** SWA

### 2026-08-01T22:15:00Z - tick 415
- Unit: **rq_406** (FOI-adjacent hole-fill - **EC Country Report Belgium 2026 SWD(2026) 201**)
- Found (strong primary EU Commission 3 Jun 2026; Spring Forecast cut-off 30 Apr):
  - **Deficit** 5.2% GDP 2025 → **5.2%** 2026 → **5.4%** 2027; **debt** 107.9 → **110.5** → **112.8**
  - **TE** 54.2% GDP 2025; gap vs neighbours **~4.6pp GDP** (general affairs + education)
  - **Defence** path **1.6% / 1.8%** GDP 2026-27; **SAFE loan request EUR 8.3bn**; NEC activated
  - **Public investment** 2.6% (2019) → **3.3%** 2026
  - **Tax/GDP** 42.8% 2024 (EU 39.4); labour share **51.8%** of tax rev; **tax wedge** avg **50.8%** (EU ~40)
  - **LTC** 2.3% GDP vs EU 1.7; ageing +1.6pp to 2040; pens reform -1.3pp dual FPB
  - **Congestion** external cost **EUR 5.3bn** 2024; **adaptation need 1.634bn/yr** to 2050; CERAC loss **9.5bn/yr** by 2050
  - **CAP** EU **3.3bn** 2023-27; **AMIF+BMVI+ISF 299.5m**; VAT gap **13.9%** VTTL
  - **MTFSP** SPB **+2.4pp** 2025-29 reconfirmed; flood WAL 2021 damage **2.8bn**
- Wrote: sources +1; budgets +23; cmt +5; lb +8; raw ec_country_report_belgium_2026.pdf; rq_406=done; spawn **rq_407**; ticks=415
- FOI: none new (public complete for aggregates; residual VAT-gap euro series / SAFE drawdown cash optional later)
- Next: prio5 **rq_407**; deferred **rq_116** SWA

### 2026-08-01T22:45:00Z - tick 416
- Unit: **rq_407** (FOI-adjacent hole-fill - **DBP Belgium 2026 + FPS federally collected tax cash open data**)
- Found (strong primary official):
  - **DBP Table5 2024:** TR **308.2bn** TE **335.3bn** deficit **-27.1bn (-4.4%)** debt **644.4bn (103.9%)**
  - Interest **13.7bn** · D.3 subsidies **21.8bn** · D.62 **109.3bn** · D.632 **49.2bn** · GFCF **19.3bn** · D.1 **77.3bn**
  - Path: deficit **-5.2% / -4.9%** 2025-26 after measures (unchanged -5.5); debt **107.3 / 110.1**
  - Net exp growth **4.3%** 2025 (overshoot vs 3.6) → **1.3%** 2026 (cum **5.7** vs ref **6.1**)
  - Defence COFOG **1.4% / 1.7%** GDP 2025-26 (NATO cash 2%); SAFE max **8.34bn**
  - Measures 2026 net: Entity I **+1741m** · Entity II **+1972m** (VL D.3 **-912m** · WAL savings **270m** · BRU precaution **284m**)
  - Entity I effort **9.2bn by 2029**; spending reviews 2026: closed centres · fossil TE · R&D/night withholding
  - **FPS tax cash:** 2024 **150.280bn** · 2025 **153.104bn** · VAT **37.5/38.0** · wage **58.7/60.8** · excise **11.1/11.1**
- Wrote: sources +2; budgets +35; cmt +5; lb +8; raw DBP PDF + FPS xlsx; rq_407=done; spawn **rq_408**; ticks=416
- FOI: none new (public complete; residual measure L5 outturns + VAT-gap euro when VTTL base public)
- Next: prio5 **rq_408**; deferred **rq_116** SWA

### 2026-08-01T23:15:00Z - tick 417
- Unit: **rq_408** (FOI-adjacent hole-fill - **Commission Opinion C(2026) 878 on BE DBP 2026**)
- Found (strong primary EU 17 Feb 2026; COM Autumn forecast dual DBP):
  - **Opinion:** DBP **complies** with EDP max net-exp growth (cum **5.8%** under **6.1%** by 2026)
  - COM deficit **-5.2% / -5.0%** 2025-26 (DBP -4.9 2026); debt **107.3 / 109.9** (DBP 110.1)
  - TE path **335.3 → 350.0 → 361.0bn**; interest **13.7 → 15.3 → 17.0bn**
  - Net primary exp **319.4 / 331.4 / 340.9bn**; growth COM **3.8%** 2025 (vs 3.6; +0.7bn within NEC) → **1.9%** 2026 (vs 2.5; -2.0bn)
  - DRM **+3.2bn (~0.5% GDP)** 2026; fiscal stance **contractionary 0.9%** GDP 2026
  - Defence COFOG **0.9→1.7%** GDP 2021-26; NEC flex **0.5 / 0.8pp**; GDP **620.3 / 642.6 / 662.0bn**
- Wrote: sources +1; budgets +25; cmt +4; lb +8; raw ec_opinion_dbp_be_2026.pdf; rq_408=done; spawn **rq_409**; ticks=417
- FOI: none new (public complete; residual measure yield audits dual CoA)
- Next: prio5 **rq_409**; deferred **rq_116** SWA

### 2026-08-01T23:45:00Z - tick 418
- Unit: **rq_409** (FOI-adjacent hole-fill - **FPS Social Security ESSPROS 2023 + Early Estimates 2024**)
- Found (strong primary FPS ESSPROS brochure; 2024 EE medium):
  - **2023 receipts 181.157bn** (30.1% GDP): employer **67.3** · protected **34.5** · gov **75.3 (41.6% TSR)** · other **4.1**
  - **2023 exp 174.210bn** (28.9% GDP): benefits **165.806** · admin **6.165** · other **2.238**
  - Benefits by risk 2023: old-age **69.584** · sickness **46.449** · disability **16.448** · family **12.233** · survivors **8.915** · unemp **5.521** · excl **5.395** · housing **1.262**
  - Cash **109.167** (65.8%) · kind **56.639** (sickness kind **40.614**)
  - **2024 EE benefits 177.884bn (+7.28%)**: old-age **74.546** · sickness **50.457** · disability **17.864** · family **13.162** · unemp **5.734**
  - Unemp share TSB **5.48%→3.22%** 2019-24; disability share **9.3→10.0%**; dual COFOG social narrower perimeter
- Wrote: sources +1; budgets +28; cmt +3; lb +8; raw esspros_be_2023_fps.pdf; rq_409=done; spawn **rq_410**; ticks=418
- FOI: none new (public complete for ESSPROS aggregates; residual L5 payment-channel unit costs already FOI ready)
- Next: prio5 **rq_410** (progress@420 after 419+420); deferred **rq_116** SWA

### 2026-08-02T00:15:00Z - tick 419
- Unit: **rq_410** (FOI-adjacent hole-fill - **NBB/NAI EDP Apr 2026 full Tables 1-5 C&R entity map**)
- Found (strong primary neco.pdf 20 Apr 2026):
  - GG: TE **347.956bn** · rev **314.736** · deficit **-33.221 (-5.2%)** · debt **692.461 (107.9%)** · GDP **642.015**
  - Primary exp **+12.1bn** to 52.0% GDP; wages **80.226** · social benefits **164.823** · GFCF **19.947** · interest **14.282**
  - Subsectors deficit: fed **-24.081** · C&R **-8.948** · local **-0.366** · SS **+0.173**
  - **C&R 2025 deficits mEUR:** VL **-4132** · FWB **-1454** · DG **-103** · WAL **-2853** · BRU **-963** · interreg ETS **+557**
  - **C&R debt stocks:** VL **50.172bn (71% rev)** · FWB **15.433 (60%)** · DG **1.257 (210%)** · WAL **40.820 (220%)** · BRU **16.339 (250%)** · total **127.565bn (+51% 4y)**
  - Fed debt contrib **553.9bn (80%)**; defence COFOG **8.8bn / 1.4%** vs NATO **2%** (undelivered **0.6pp**); **RRF 3.3/5.3bn = 62%**
- Wrote: sources +1; budgets +31; cmt +4; lb +8; raw nbb_edp_2025_apr_neco.pdf; rq_410=done; spawn **rq_411 progress@420**; ticks=419
- FOI: none new (entity stocks strong public; residual ETS allocation key political)
- Next: **MANDATORY progress@420 rq_411**; deferred **rq_116** SWA

### 2026-08-02T00:45:00Z - tick 420
- Unit: **rq_411** (**progress milestone @420** - coverage % + waste top10 refresh; no new euro invent)
- Snapshot (honest order-of-magnitude vs TE EUR 347.956 bn):
  - **A L0 / B L1:** **100%** (unchanged strong; EDP C&R entity dual tick419)
  - **C L2:** **~98-99%** (stable high) - C&R entity debt/deficit 2025 · ESSPROS 165.8-177.9bn · COFOG 2024 functions · DBP+COM TE 350-361 · FPS tax cash 153.1
  - **D L5:** **~22-35%** generous (ESSPROS risk lines not firm end-receivers; FOI ASBL/firm residual)
  - **E FOI ready:** **~215** (answered **~8**; total FOI rows **~225**)
- Inventory: budgets ~6677 · cmt ~755 · lb ~1181 · entities ~357 · sources ~738
- Waste top10: **stable** fossil/company-cars/cheque/EIWT; no reorder; DBP spending reviews target same cluster
- Dual/off-TE: ESSPROS 174.2bn social protection; C&R debt 127.6bn; RRF 62%; SAFE 8.3bn; Entity I effort 9.2bn
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_411=done; spawn **rq_412**; ticks=420
- FOI: no new gap this tick (progress only)
- Next: prio5 **rq_412** hole-fill; deferred **rq_116** SWA

### 2026-08-02T01:15:00Z - tick 421
- Unit: **rq_412** (FOI-adjacent hole-fill - **INAMI invalidity indemnity stats 2025**)
- Found (strong primary INAMI 19 May 2026 PDFs):
  - **Salaried+unemployed cash total:** **€6.959 → €9.971bn** 2021-25 (+6.19% YoY 2025); base **€9.552bn** + prime rattrapage **€419.5m**
  - Days **160.4m** · avg day **€62.17** (+2.21%)
  - Stock **537.728** sal (+4.50%; **+1.6%** ex pension-age effect) · indep **38.915** (+9.79%) · **total 576.643**
  - Pathology sal: mental **209.245 (38.9%)** · osteo **169.238 (31.5%)** · tumors **26.591**
  - Regions sal: VL **267.356** · WAL **205.779** · BRU **50.741** · abroad **13.852**
  - Primary incapacity caseload **−1.68%** 2024-25 (reform contact gate claimed)
  - Dual ESSPROS disability EE **€17.9bn** broader perimeter (gap ~indep+other regimes)
- Wrote: sources +1; budgets +23; cmt +3; lb +8; FOI **gap_inami_invalidite_indep_cash** ready; raw 3 PDFs; rq_412=done; spawn **rq_413**; ticks=421
- FOI: independent cash series parallel salaried tables — human send only
- Next: prio5 **rq_413**; deferred **rq_116** SWA

### 2026-08-02T01:45:00Z - tick 422
- Unit: **rq_413** (FOI-adjacent hole-fill - **INAMI depression/burnout invalidity 2019-2024**)
- Found (strong primary INAMI 19 May 2026 PDFs costs+counts):
  - **Dep+burnout cost:** **€1.518 → €2.698bn** 2019-24 (+11.8% YoY; **+77.8%** since 2019); dep **€1.790bn** + burn **€0.908bn**
  - **Mental group:** **€3.886bn** (38.3% of all inv cost); stock **210.060**
  - **Total inv all causes sal+indep:** **€10.156bn** 2024 (dual tick421 sal ~9.4bn + indep)
  - **Indep total cash:** **€386 → €613m** 2019-24 (+59%) — **fills FOI gap_inami_invalidite_indep_cash** (total cash path; jours residual optional)
  - Stock dep+burn **147.684** eoy 2024 (+43% since 2019); women ~69%; under-30s fastest growth
  - Burnout cost **+117%** since 2019 (fastest sub-pathology)
- Wrote: sources +1; budgets +52; cmt +2; lb +8; FOI **gap_inami_invalidite_indep_cash** answered; raw 2 PDFs; rq_413=done; spawn **rq_414**; ticks=422
- FOI: answered partial (total indep cash public); jours+avg day residual optional human FOI if needed
- Next: prio5 **rq_414**; deferred **rq_116** SWA

### 2026-08-02T02:15:00Z - tick 423
- Unit: **rq_414** (FOI-adjacent hole-fill - **INAMI independent invalidity full series 2020-2024**)
- Found (strong primary INAMI 12 May 2026 PDFs cas+jours):
  - **Cash total general:** **€407.6 → €601.3m** 2020-24 (+12.55% YoY 2024; **+47.5%** since 2020)
  - Base indemnities **€591.0m** + prime rattrapage **€10.3m** 2024
  - **Days:** **8.63 → 10.39m** · **avg day €46.41 → €56.87** (+3.72% YoY)
  - Stock eoy **28.913 → 35.445** (+8.0% YoY; women +31% since 2020)
  - Patho 2024: mental **10.223 (28.8%)** · osteo **10.099 (28.5%)** · tumors 3.097 · trauma 3.157
  - Regions: VL **19.563** · WAL **11.529** · BRU **3.532** · abroad 821
  - Dual tick422 dep/burnout aggregate indep **€613m** vs this official **€601m** (~€12m method delta; prefer Tableaux-style series)
- Wrote: sources +1; budgets +41; cmt +2; lb +3; FOI **gap_inami_invalidite_indep_cash** fully **answered**; raw 2 PDFs; rq_414=done; spawn **rq_415**; ticks=423
- FOI: closed (jours+montants+avg day public parallel salaried)
- Next: prio5 **rq_415**; deferred **rq_116** SWA

### 2026-08-02T02:45:00Z - tick 424
- Unit: **rq_415** (FOI-adjacent hole-fill - **INAMI independent invalidity 2025**)
- Found (strong primary INAMI 19 May 2026 PDFs cas+jours; provisional stock):
  - **Cash total general:** **€667.0m** 2025 (+10.93% YoY; base **€655.5m** + prime **€11.5m**)
  - **Days:** **11.29m** · **avg day €58.07** (+2.11% YoY)
  - Stock eoy **38.915** (+9.79%; matches tick421 indep headcount)
  - Patho 2025: mental **11.467 (29.5%)** · osteo **11.040 (28.4%)** · tumors 3.407
  - Regions: VL **21.038** · WAL **12.979** · BRU **4.037** · abroad 861
  - Dual recon: sal **€9.971bn** tick421 + indep **€0.667bn** = **€10.638bn** total inv cash 2025
- Wrote: sources +1; budgets +18; cmt +2; lb +3; raw 2 PDFs; rq_415=done; spawn **rq_416**; ticks=424
- FOI: none new (prior indep cash gap already closed tick423)
- Next: prio5 **rq_416**; deferred **rq_116** SWA

### 2026-08-02T03:15:00Z - tick 425
- Unit: **rq_416** (FOI-adjacent hole-fill - **INAMI incapacity primaire 2019-2023 + SECM control 2025**)
- Found (strong primary INAMI PDFs + SECM RA/press):
  - **Primaire cash sal+chom:** **EUR 1.943 -> 2.652bn** 2019-23 (+11.49% YoY 2023; **+36.5%** since 2019)
  - **Days** 38.82 -> **42.88m** · **avg day EUR 50.05 -> 61.85** (+7.36% YoY)
  - Split 2023: ouvriers **1.330bn** (avg 58.20) · employes **1.322bn** (avg 66.01)
  - Periods ended **439.895**; long **338-365d = 81.008 (18.42%)** invalidity pipeline class
  - Indemnisables stock eoy **3.914m** (+1.08%); covid suppl residual **0.31m** 2023
  - **SECM 2025:** grief **15.867m** (vs 11.708m 2024); vol remb **10.445m**; fraud 47 dossiers **4.344m**; actions **334** (was 483); staff **211**
  - Dual: primaire short-term channel vs invalidite multi-bn long-term (tick421-424); residual **2024-25 primaire full tables** not yet on portal
- Wrote: sources +2; budgets +33; cmt +2; lb +6; raw 4 PDFs (3 primaire + SECM); rq_416=done; spawn **rq_417**; ticks=425
- FOI: none new (2024-25 primaire lag normal publication cycle; optional recheck later; gap_antifraud residual unchanged)
- Next: prio5 **rq_417**; deferred **rq_116** SWA

### 2026-08-02T03:45:00Z - tick 426
- Unit: **rq_417** (FOI-adjacent hole-fill - **INAMI indep incapacity primaire 2019-2023**)
- Found (strong primary INAMI PDFs stat_si2023_*_independants):
  - **Indep primaire cash:** **EUR 123.1 -> 208.2m** 2019-23 (+19.86% YoY 2023; **+69.2%** since 2019)
  - **Days** 2.86 -> **4.00m** · **avg day EUR 43.07 -> 52.09** (+8.38% YoY; forfait revalorisation+index)
  - Split 2023: men **122.4m** (avg 52.80) · women **85.9m** (avg 51.11)
  - Periods ended **33.768** (-3.1%); long **338-365d = 6.795 (20.12%)** invalidity pipeline
  - Indemnisables stock eoy **670.164** (+0.10%)
  - Dual recon: sal primaire **2.652bn** tick425 + indep **0.208bn** = **2.860bn** total primaire cash 2023
  - Residual 2024-25 indep primaire tables not yet on portal (parallel sal lag)
- Wrote: sources +1; budgets +25; cmt +2; lb +4; raw 3 PDFs; rq_417=done; spawn **rq_418**; ticks=426
- FOI: none new (publication lag normal; optional later recheck)
- Next: prio5 **rq_418**; deferred **rq_116** SWA

### 2026-08-02T04:15:00Z - tick 427
- Unit: **rq_418** (FOI-adjacent hole-fill - **INAMI maternity/paternity protection 2019-2023**)
- Found (strong primary INAMI PDFs sal + indep):
  - **Sal mat/pat package cash:** **EUR 633.2 -> 800.1m** 2019-23 (+6.14% YoY 2023; **+26.4%** since 2019)
  - Split 2023: maternity rest **474.9m** (days 5.63m avg 84.42) · ecartement **221.8m** · paternity **101.9m** (20d max) · adopt 0.59 · foster 0.94
  - Days package **9.22m** (-2.79%) · avg day **86.82** (+9.18%); mat cases **65.600** (-5%)
  - Invalid-mat separate line **19.1m** (not in package total)
  - **Indep package 2023:** primary mat **67.0m** (avg case **7.790**) + inv-mat 0.69 + adopt 0.11 + foster 0.09 = **67.9m**
  - Dual recon: sal **800.1** + indep **67.9** = **868.0m** mat/pat protection 2023
- Wrote: sources +2; budgets +41; cmt +2; lb +6; raw 3 PDFs; rq_418=done; spawn **rq_419**; ticks=427
- FOI: none new (core entitlement; 2024-25 series lag normal)
- Next: prio5 **rq_419**; deferred **rq_116** SWA

### 2026-08-02T04:45:00Z - tick 428
- Unit: **rq_419** (FOI-adjacent hole-fill - **FPD PensionStat L5 menage + transition + retraite/survie**)
- Found (strong primary PensionStat XLSX data-2025-fr Depenses_annuelles):
  - **Legal total path:** 48.29 -> **69.05bn** 2019-25 (+43%; reconfirm)
  - **Retraite 2025:** **60.52bn** (87.6%) · **Survie 8.53bn** (12.4%)
  - **Taux menage (household rate):** **5.923bn** 2025 (sal **4.750** + indep **1.173**; ~8.6% of legal; multi-year path extracted)
  - **Allocation de transition:** **~63.3m** 2025 (sal 49.4 · indep 6.8 · fonct 7.1)
  - Autres prestations sal ret **354m** · indep ret **189m**
  - Stock pensionnes nationality-sum **2.675m** · GRAPA **119.651**
- Wrote: sources note; budgets +~40; cmt +3; lb +5; rq_419=done; spawn **rq_420**; ticks=428
- FOI: none new (gap_fpd_beheer_igo_l5 residual admin still ready; autres composition opacity note only)
- Next: prio5 **rq_420**; deferred **rq_116** SWA

### 2026-08-02T05:15:00Z - tick 429
- Unit: **rq_420** (FOI-adjacent hole-fill - **DG HAN ARR/AI 2.93bn 2025 + SPF SS macro 146.8bn**)
- Found (strong primary SPF SS Rapport annuel 2025 PDF):
  - **DG HAN ARR+AI cash:** **EUR 2.93bn** (current prices); monthly benef **264.250** (+4% YoY; +17.8% vs 2021)
  - Split stock: ARR-only **27.608** · AI-only **106.868** · both **129.774**
  - Avg month **EUR 938** (AI-only 349 · ARR-only 924 · both 1.425)
  - Regions: VL **52.1%** · WAL **37.9%** · BRU **9.2%** · DG **0.7%**
  - Evals **155.334** · recognition stock **581.987** · first-req refusal **66.1%**
  - **SS macro 2025:** total exp **146.8bn** (~51% state); prest **132.9** · gestion **2.9** · divers **10.97**
  - Financing: cotis **83.2** · state **20.5** · altfin **26.2** · equilibre **7.4** · other **7.7** · federated **0.4**
  - Dual: VAPH FL care ~3bn not additive; INAMI inv separate channel
- Wrote: sources +2; entity dg_han; budgets +24; cmt +2; lb +5; raw SPF PDF; rq_420=done; spawn **rq_421**; ticks=429
- FOI: none new (official ARR/AI cash split residual optional; component recon medium only)
- Next: prio5 **rq_421**; deferred **rq_116** SWA

### 2026-08-02T05:45:00Z - tick 430
- Unit: **rq_421** (**progress milestone @430** - coverage % + waste top10 refresh; no new euro invent)
- Snapshot (honest order-of-magnitude vs TE EUR 347.956 bn):
  - **A L0 / B L1:** **100%** (unchanged strong)
  - **C L2:** **~98-99%** - SS macro 146.8 · DG HAN 2.93 · FPD 69.05+menage 5.92 · INAMI inv 10.64 · primaire 2.86 · mat/pat 0.87
  - **D L5:** **~23-36%** generous (INAMI/FPD/DG HAN L5 fills; FOI ASBL/firm residual)
  - **E FOI ready:** **~215** (answered **~9**; total FOI rows **~226**)
- Inventory: budgets ~6982 · cmt ~775 · lb ~1229 · entities ~358 · sources ~749
- Waste top10: **stable** fossil/company-cars/cheque/EIWT; no reorder; new entitlement maps off pure top10
- Dual/off-TE: SS 146.8bn; FPD menage 5.92bn; INAMI channels; ESSPROS 174-178bn social protection
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_421=done; spawn **rq_422**; ticks=430
- FOI: no new gap this tick (progress only)
- Next: prio5 **rq_422** hole-fill; deferred **rq_116** SWA

### 2026-08-02T06:15:00Z - tick 431
- Unit: **rq_422** (FOI-adjacent hole-fill - **SPP Integration sociale federal CPAS DIS/RIS 2026**)
- Found (strong primary Cour des comptes Budget Etat 2026 §7.2 table):
  - **Federal CPAS grants total 2026:** **EUR 2.2409bn** (DIS **2.0845** + loi 1965 **0.1564**)
  - DIS base CM Jul **1.8417bn** + index **-36.8m** + **unemp compensation +300m** + RIS reform **-16.6m** + 5y wait **-3.8m**
  - Loi 1965: base **179.8m** → **156.4m** after index/reform/wait
  - **Compensation path:** budget envelope **300/300/302/343m** 2026-29 vs SPP IS calc **296/820/888/709m** (2027+ understate risk)
  - ~**52.400** new RIS from unemp time-limit 2026 class; federal reimburses **55-70%** of RIS (not full cash to people)
  - Dossier fee **518 EUR**/beneficiary (temp **1036** for H1-2026 compensated cohort)
- Wrote: sources +1; entity spp_is; budgets +15; cmt +2; lb +4; rq_422=done; spawn **rq_423**; ticks=431
- FOI: none new (full RIS cash stock federal+local residual; optional later)
- Next: prio5 **rq_423**; deferred **rq_116** SWA

### 2026-08-02T06:45:00Z - tick 432
- Unit: **rq_423** (FOI-adjacent hole-fill - **Entity I social triple + provision generale L5**)
- Found (strong primary Cour des comptes Budget Etat 2026 p18 + p58):
  - **Entity I social transfers:** handicap **EUR 3.3bn** · ages/IGO **1.0bn** · RIS CPAS **2.2bn** (+ Ukraine **299m** excl) = **6.5bn** triple
  - Dual recon: DG HAN **2.93bn** 2025 outturn · SPP IS table **2.241bn** 2026
  - **Transfers other govts** **66.5bn** (federated **59.1bn** LSF class; excl RIS line)
  - **Provision generale 2026:** **829.8m** (+230m vs 599.7 adj 2025)
  - Split: justice/divers **618.3** · Fedasil **100** · bpost contracts **78** · bien-etre **33.5**
  - Named inside justice/divers: surpop **259** · ESA **176** · eco sociale **50** · reorg **36** · Tria **5.3** · CPL **2.7** (sum ~529 of 618)
  - CoA flag: prefer section credits when beneficiary known
- Wrote: sources +1; budgets +20; cmt +2; lb +6; rq_423=done; spawn **rq_424**; ticks=432
- FOI: none new
- Next: prio5 **rq_424**; deferred **rq_116** SWA

### 2026-08-02T07:15:00Z - tick 433
- Unit: **rq_424** (FOI-adjacent hole-fill - **SS consol 2026 L5 residual + ONEM reform residual**)
- Found (strong primary Cour des comptes Budget Etat 2026 p79-80 + p95-98):
  - **SS consol dep 2026:** **EUR 147.8585bn** (+0.8% vs 146.76 adj 2025)
  - Prestations **135.492bn**; GG sal **63.342** (pens **43.271** · MI **14.879** · chom **4.638** · autres **0.554**)
  - GG indep **7.012** (pens **5.920** · MI **1.070** · autres **0.022**)
  - **Soins 41.297bn** · **pens publiques 22.828bn** · autres prest **1.014** · **frais gestion 2.996** · **autres dep 9.370**
  - Dual: pens stack **72.018bn**; MI dual **15.949bn**; chom **-28.2%** YoY
  - Altfin **27.222bn** (ONSS **23.392** · INASTI **3.829**)
  - **Demission volontaire cost EUR 33.6m 2026** (flipped from +45m "save"); steady ~34m
  - **Credit familial envelope 40m** (CoA overestimate risk vs 50m full-year)
  - Pension reform 2026 savings **−64m delay** (laws not yet Kamer)
- Wrote: sources +1; budgets +19; cmt +2; lb +10; rq_424=done; spawn **rq_425**; ticks=433
- FOI: none new (autres_dep 9.37bn L5 optional later if annex absent)
- Next: prio5 **rq_425**; deferred **rq_116** SWA

### 2026-08-02T07:45:00Z - tick 434
- Unit: **rq_425** (FOI-adjacent hole-fill - **pension reform L5 multi-year 2027-2030**)
- Found (strong primary Cour des comptes Budget Etat 2026 p82-83, cellule Pensions):
  - **Total estimated saves:** **EUR 807 / 1.304 / 1.787 / 2.229bn** (2027-2030)
  - Largest lines 2027→2030: **reforme calcul 679→1.915bn** · **bonus-malus 273→473m** · **carriere anticip 136→323m** · **pens maladie pub extinct 94→302m** · **index hautes pens 97→253m** · **perequation 64→156m** · **convergence 125m/yr flat**
  - Net **costs**: age flexible **−47→−77m** · alloc trans vs survie **−36m 2027** then positive · transitoires **−25→−99m**
  - **Legislation still pending (CoA):** GRAPA conditions · survie→transition · menage extinction · periodes assimilees
  - SFP: models need major updates; late laws → partial non-delivery risk (2026 already −64m delay dual)
  - Dual: prior totals bud_pens_reform_save_*; FPD menage 5.92bn stock; FPD transition 63m
- Wrote: sources +1; budgets +73; cmt +1; lb +10; rq_425=done; spawn **rq_426**; ticks=434
- FOI: none new (package primary; residual is legislative delivery not opacity)
- Next: prio5 **rq_426**; deferred **rq_116** SWA

### 2026-08-02T08:15:00Z - tick 435
- Unit: **rq_426** (FOI-adjacent hole-fill - **RTW invalidity L5 multi-year 2026-2029 + chomage waves**)
- Found (medium-strong primary Cour des comptes Budget Etat 2026 p84-90 + p94):
  - **RTW total indemnity reduction:** **EUR 202.9 / 643.8 / 1.198 / 1.929bn** (2026-2029)
  - L5: **recontrol net 34.3→1.045bn** (gross 38.7→1.066; staff −4.4→−20.6) · **annual-ext 126.9→868.8m** · solidarité **0→77m** · psycho **2.9→11.3m** · ETA **4.8→22.3m** · WHP **0→6.7m** · maladie fonct table **34/2/54/89m**
  - Exits target **90.204** (recontrol **43.056** + annual-ext **47.148**); dossiers recontrol **19.7k→94k/yr**
  - **CoA flags:** most measures undeveloped; sample excl rates 8.8/23.7pct may not scale; **+48.1m overstate** recontrol 2029; psycho ROI study not for invalids; maladie fonct law not deposited; no chomage spillover modelled
  - Baseline incapacity path **18.347bn 2029** (+28pct vs 2024); invalidity alone **13.4bn / 656k stock**
  - Dual: work-prime cost **28→38.5m** (outside net table); maladie indem cost **16.5→124.3m** vs cotis **51→37m**
  - **Chomage waves p94:** **193.904** exclusions (BRU **41.709** · VL **62.676** · WAL **88.566** · DG **953**); 7 waves Jan2026→Jul2027
  - Pharma residual: of **401.9m** effort **148.9m** still to design (CoA p84)
- Wrote: sources +1; budgets +127; cmt +2; lb +10; rq_426=done; spawn **rq_427**; ticks=435
- FOI: none new (package primary; residual is legislative design + method audit not opacity)
- Next: prio5 **rq_427**; deferred **rq_116** SWA

### 2026-08-02T08:45:00Z - tick 436
- Unit: **rq_427** (FOI-adjacent hole-fill - **Fedasil multi-year L5 + development coop + ONSS SSC residual**)
- Found (strong/medium primary Cour des comptes Budget Etat 2026 p61-63 + p75-79):
  - **Fedasil save path:** **0 / 247 / 403 / 577 / 688m** (2025-2029)
    - Accueil network **0/172/303/452/538** · Retours **0/75/100/125/150**
    - Package dual **955.6→802.2m** (dot 828.9→702.2 + prov 126.6→100); apps **39.6k→34.4k** (−13.1%)
    - CoA: no quantified delivery plan yet (ministerial cell Q1-2026)
  - **Development coop DO14.54:** liq **1.129 / 1.040 / 0.957bn** vs monitor **1.235 / 1.253 / 1.274** (gap **106/212/317m**; ~25pct by 2027)
    - FAD-17 voluntary **64.2m** pay over **10y** (forgo ~6m 3y discount); SEC **+27m** 2027
  - **ONSS residual measures:** group-cible RTT+Horeca cut gov **28m** (full-yr **32**; CoA 9m **24**); sports cap fix **10m**; gestion IT+insp **30.3m**
    - Plans-plus reest **64.2/85.1/78.2** vs budgeted **53/67/52** (expose understates)
    - Struct low-wage path **584m** 2026; CSSS cut **415m** from 2028; bonus emploi boost dual **357.5m** 2028
  - **Altfin multi-year L5:** total **25.0 / 26.2 / 27.2bn** 2024-26; ONSS/INASTI TVA+PM matrix; fonds total **27.325bn**
  - Prison food underfund **10.18m** on **25.2m** credits
- Wrote: sources +1; budgets +76; cmt +3; lb +10; rq_427=done; spawn **rq_428**; ticks=436
- FOI: none new (Fedasil partner L5 already ready gap_fedasil_l5_partners; delivery plan residual is policy design)
- Next: prio5 **rq_428**; deferred **rq_116** SWA

### 2026-08-02T09:15:00Z - tick 437
- Unit: **rq_428** (FOI-adjacent hole-fill - **INAMI sante L5 + NATO multi-year + Justice/security provisions**)
- Found (strong/medium primary Cour des comptes Budget Etat 2026 p28-31 + p59-60 + p84):
  - **INAMI health save 764.5m 2026 L5:** drugs **401.9** (price 80.3 · antiacid 65.8 · lipid 29.4 · partial-bill 42 · TM 27.9 · residual design **148.9**) · doctors **213.2** (lab 70.8 · imaging 68.5 · surgery 63.7 · delay risk **41.5**) · hosp **50** (day 47.1 cash-shift flag) · other **73.8** · TM-res **25.6**
  - **NATO multi-year 2025-29:** effort **12.73→14.29bn** (~100% of 2pct need); s16 share **82.4→79.7%**; std **167.5→750m**
    - Extra spend **3.87→3.07bn/yr** sum **16.78bn**; temp fin **7.15** (CIT Russian **6.15** + Belfius **1.0**); struct **4.83**; deficit temp **4.80**; asset optim **3.17** (opaque)
  - **Security provision 366.9m:** reinforce **250** (J112.5 police87.5 mig50) · surpop **60** · carry **6.2** · opaque **50.7** (J44+I6)
  - **Justice:** section **2.843bn** + BOSA provisions **465.5m** (specialty breach); surpop envelope **840m** (600 infra + 240 struct) vs TF need **~1.1bn**; TF capacity **1052 places / 303.8m** 2026 class
- Wrote: sources +1; budgets +144; cmt +3; lb +10; rq_428=done; spawn **rq_429**; ticks=437
- FOI: none new (asset optim + surpop project list already covered by prior gaps/design residual)
- Next: prio5 **rq_429**; deferred **rq_116** SWA

### 2026-08-02T09:45:00Z - tick 438
- Unit: **rq_429** (FOI-adjacent hole-fill - **IPP reform annex L5 multi-year 2026-2030**)
- Found (medium-strong primary Cour des comptes Budget Etat 2026 p100 Annexe 1 + p10 emp path):
  - **Total incidence (top):** **-421 / -669 / -1.535 / -3.978 / -5.351bn** (2026-2030)
  - **Federal:** **-320 / -494 / -1.274 / -3.017 / -4.072bn**
  - **Entity recon bottom:** total **-421→-5.525**; regions **-76→-1.132**; communes **-25→-321** (2029/30 top vs bottom totals differ slightly)
  - Largest cost: **quotité exemptée -531→-4.988bn**; CSSS **-423m from 2028**; droits d'auteur **-142m/yr**; heures sup **-101m/yr**; bonus emploi fiscal **-60→-218**
  - Revenue side: **UI tax-credit cut +257→+216**; conjugal extinction **+66→+79**; high-pension red. phase **+34→+22**; true isolés **+135 from 2029**
  - **Employment-rate credibility:** coalition **73→78% 2025-29** vs BFP Feb2026 **72.8→74.3** (gap **3.7pp 2029**); dual return-effects overstated
- Wrote: sources +1; budgets +250; cmt +1; lb +10; foi gap_ipp note partial; rq_429=done; spawn **rq_430**; ticks=438
- FOI: gap_ipp_reform_aurora_l5 residual narrowed (annex public; Aurora interactions/H1 still ready human send)
- Next: prio5 **rq_430**; deferred **rq_116** SWA

### 2026-08-02T10:15:00Z - tick 439
- Unit: **rq_430** (FOI-adjacent hole-fill - **personnel austerity L5 multi-year + specialty breaches**)
- Found (medium-strong primary Cour des comptes Budget Etat 2026 p53-57):
  - **Partial replace:** **100m 2026 → 175m 2030** (personnel+ops; excl regalian; 2/5 hire if miss; intermediate years unpublished)
  - **Statutaire employer cotis** (new hires after 31 May 2026): **10m 2026 / 284m 2029 / 365m 2030** (rate **9.5%→38%**); CoA: flat hire-volume hyp contradicts contract-prefer policy
  - **Combined Entity I influence 459m 2029** (gov claim)
  - **Departmental hit:** Justice **3.3m/61 FTE → 101m/1859 FTE** (622 judiciary); Defence **3.7→113.3m 2029 / 297m 2034**; Police **26 FTE → 700-821 FTE** capacity cut
  - **Specialty breaches:** Defence eng fully transferable **20.1bn**; Justice **2.5bn** + Police **1.6bn** free redistribute; inter-programme transfers **454m eng 2024**; provisions **2.13bn** CM transfer
  - Dual: droits d'auteur forfait remove **+30m**; VVPR hist **344→760m 2022-24**
- Wrote: sources +1; budgets +36; cmt +2; lb +10; rq_430=done; spawn **rq_431**; ticks=439
- FOI: none new (intermediate replace path optional later if annex absent; method residual not opacity)
- Next: prio5 **rq_431**; deferred **rq_116** SWA

### 2026-08-02T10:45:00Z - tick 440
- Unit: **rq_431** (**progress milestone @440** - coverage % + waste top10 refresh; no new euro invent)
- Snapshot (honest order-of-magnitude vs TE EUR 347.956 bn):
  - **A L0 / B L1:** **100%** (unchanged strong)
  - **C L2:** **~98-99%** - SS consol 147.86 · Entity I social 6.5 · SPP IS 2.24 · NATO 13.1 · Fedasil 0.80 · coop 1.04 · liq 92
  - **D L5:** **~24-37%** generous (reform-measure L5: pens 0.8-2.2 · RTW 0.2-1.9 · sante 0.76 · IPP path · chom waves 194k; FOI ASBL/firm residual)
  - **E FOI ready:** **~215** (answered **~9**; total FOI rows **~226**)
- Inventory: budgets ~7744 · cmt ~793 · lb ~1309 · entities ~358 · sources ~758
- Waste top10: **stable** fossil/company-cars/cheque/EIWT; no reorder; reform maps off pure waste top10
- Dual/off-TE: SS 147.9bn; IPP -5.4bn path; NATO extra 16.8bn; taxex 29.7bn
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_431=done; spawn **rq_432**; ticks=440
- FOI: no new gap this tick (progress only)
- Next: prio5 **rq_432** hole-fill; deferred **rq_116** SWA

### 2026-08-02T11:15:00Z - tick 441
- Unit: **rq_432** (FOI-adjacent hole-fill - **DGD AR 2025 ODA L5 channels/themes/top20/named**)
- Found (strong primary DGD Annual Report 2025 ENG, provisional):
  - **Total DGD:** **€1,117.97m 2025** (vs 1,440.92 2024 / 1,285.90 2023); cut **€106m** of which **≥€90m** under-use + multi review
  - **Themes 2025:** climate **365.3** (32.5%) · stability **301.8** · other **181.5** · humanitarian **175** (dual table **170**) · health **98.8**
  - **Channels 2025:** gov **250.4** (Enabel **212.0** + mgmt **25.6** + gov **7.2** + loans **5.6**) · nongov **247.4** · multi **257.9** · hum **170** · climate policy **102.2**
  - **Top20 sum €369.7m** (~33%); DRC **104.49** largest
  - **Named:** LDCF **18.5m** (2nd donor) · CGIAR **9.3m** · Sahel Climate Enabel **50m** · mRNA/HTAP **8m/4y** · BIO approvals **240m**/30 projects
- Wrote: sources +1; budgets +48; cmt +1; lb +10; foi gap_dgd note; rq_432=done; spawn **rq_433**; ticks=441
- FOI: gap_dgd_l5_projects residual narrowed (project-level still ready human send)
- Next: prio5 **rq_433**; deferred **rq_116** SWA

### 2026-08-02T11:45:00Z - tick 442
- Unit: **rq_433** (FOI-adjacent hole-fill - **BIO AR 2025 named investment L5 + dual Kampani**)
- Found (strong primary BIO Annual Report 2025 web):
  - **Approvals €235m / 30** projects (signed **€166m / 21**); committed stock **€1.2bn / 171**; signed stock **€1.033bn**
  - Financials: assets **€1.196bn** · income **55.3** · cost of risk **20.1** · FX **−5.9** · net **9.0** · dividend **4.5**
  - Africa **55%** approvals · gender **57%** of 2024-25 · direct enterprise **11** (vs 2) · jobs direct **~388k** EOY2024
  - **Named EUR L5:** Coris **20** · Orchidia **10** · Glacier **8** · FoodsCo **3** · Vital **3** · Kampani **2** · Limbua **2** · FEFISOL **2** · ACEP **1.5** (sample sum **€51.5m**)
  - **Named USD face L5:** multiple **15m** lines (Adenia/Amartha/Atlántida/ADEMI/Bandwidth/Excelsior) · ECOM **10** · Helios **10** · Lendable **10** · Super Silica **3.7** · Ukraine fund **6** (no FX invent)
  - Dual: DGD AR **240m** approvals class; State capital subsidies extra **€85m** strategy 2024-28
- Wrote: sources +1; entity kampani; budgets +37; cmt +1; lb +9; foi gap_bio note; rq_433=done; spawn **rq_434**; ticks=442
- FOI: gap_bio_l5_portfolio residual narrowed (named sample public; full outstanding+impairments still ready)
- Next: prio5 **rq_434**; deferred **rq_116** SWA

### 2026-08-02T12:15:00Z - tick 443
- Unit: **rq_434** (FOI-adjacent hole-fill - **Alterfin AR 2025 Belgian cooperative impact finance dual BIO/Kampani**)
- Found (strong primary Alterfin Annual Report 2025 + 2024 dual):
  - **Capital €69.70m** / **5,828** members (indiv 5,644 / inst 184); **first decline −€1.1m** after **abolition of 5% tax break** on development-fund shares
  - **Portfolio mgmt+advisory:** **€122.1m** (−8.2% FX) vs **USD 143.6m** (+3.7% record); under mgmt **€98.5m** / **USD 115.8m**
  - Disbursed key **€95m** · under-mgmt **>USD 108m** record · advisory **€23.2m** / **USD 26.7m**
  - Partners **142** in **32** countries (MFI **76** · agri **57** · funds **9**); families class **~4.32m**
  - BS assets **€164.3m** · net loans **€92.0m** · equity **€73.1m** · debt/equity **1.20**
  - P&L net **€733k** (−13%); gross margin **+16%**; cost of risk **€1.61m** (+30%); proposed dividend **1%**
  - FSMA AUM **€226.1m** → full AIFM/OPCA licence path H2-2026; Fefisol II **€23.1m**/40 partners; BIO loan **USD 5m** dual
- Wrote: sources +2; entity alterfin; budgets +40; cmt +1; lb +10; rq_434=done; spawn **rq_435**; ticks=443
- FOI: none new (private co-op; partner L5 residual optional not material public euro opacity)
- Next: prio5 **rq_435**; deferred **rq_116** SWA

### 2026-08-02T12:45:00Z - tick 444
- Unit: **rq_435** (FOI-adjacent hole-fill - **BRS Microfinance Coop dissolve + ASBL coaching dual Alterfin/Incofin**)
- Found (strong primary BRS AR 2025 magazine + dissolve press 13 May 2026):
  - **BRS MFC EOY2025:** assets **€22.0m** · equity **€21.4m** · capital **€21.24m** (**1,420** A-members **€3.74m** + C **€17.5m**)
  - Ownership: Cera **45.6%** · individuals **35.3%** · KBC **17.6%** · BRS ASBL **1.5%**
  - Loans **€2.0m** (AMC-SV **1.4** · El Ejido **0.3** · EBO-UG **0.3**) · MF funds **€9.0m** (Triodos **3** · Incofin **1.6** · Fefisol **1.5** · Alterfin **1** · ECF **1** · Incofin Climate **1**) · cash **€10.8m**
  - Profit **€219k** · dividend **2.5% / €534k** · dissolve provision **€50k**
  - **Dissolve:** midnight **2026-06-30**; full A-share repay early Jul; Cera continues MF via **increased Alterfin + Incofin** stakes
  - **BRS ASBL:** assets **€2.41m** · loss **€85k** · income **€503k** (donations **€390k** + Cera tombola **€109k**) · projects **€403k** · **594** coaching days · **~94** KBC volunteers · **14** partners / **7** countries
- Wrote: sources +2; entities +3; budgets +33; cmt +2; lb +10; rq_435=done; spawn **rq_436**; ticks=444
- FOI: none new (private co-op dissolve; dual stack now mapped public)
- Next: prio5 **rq_436**; deferred **rq_116** SWA

### 2026-08-02T13:15:00Z - tick 445
- Unit: **rq_436** (FOI-adjacent hole-fill - **Incofin Microfinance Fund AR 2025 dual BRS/Alterfin + VL public stake**)
- Found (strong primary Incofin IMF AR 2025 ENG PDF):
  - **Capital EUR 49.953m** (-1.264m / -2.5pct) · **equity 53.496m** · **BS 65.541m** · **portfolio 62.441m** (equity 17.4 + sub 7.5 + loans 37.5)
  - **Net loss 1.232m** (vs 0.658m 2024) · **dividend 0%** second year · mgmt fee Incofin IM **1.055m**
  - **Shareholders 2,348** (retail 2,205 / inst 143) · partners **38** / countries **25** · end-clients **3.3m** (64% women / 51% rural)
  - **Public L5:** Vlaamse overheid Departement Internationaal Vlaanderen **kEUR 1,000 (2%)** stake
  - **BRS dual:** still **kEUR 1,560 (3%)** EOY2025 pre Jun-2026 dissolve (matches BRS fund 1.6m)
  - **Tax-break abolition** capital drain dual Alterfin; PAR90+restr **12.12%** (was 4.98%); risk cov **111%**
  - Named equity L5: Banco FIE **8.46m**; Lovcen exit Feb2026 gain **~1.3m**
  - Manager: OPIM AUM **USD 490m** FY24 strong; site broader **~USD 1.1bn** medium
- Wrote: sources +2; entity incofin_im + update IMF; budgets +24; cmt +1; lb +10; rq_436=done; spawn **rq_437**; ticks=445
- FOI: none new (AR public; multi-year VL stake acquisition path optional low-prio residual)
- Next: prio5 **rq_437**; deferred **rq_116** SWA

### 2026-08-02T13:45:00Z - tick 446
- Unit: **rq_437** (FOI-adjacent hole-fill - **Kampani agri impact fund AR2023 + DGD first-loss + BIO 2m + named L5 dual Enabel**)
- Found (strong primary AR2023 + DGD impact PDF + BIO invest page + portfolio web):
  - **Fund size EUR 14.6m** after **+4.6m** raise 2023 (from 10m); subscribed **13.85m** / uncalled **3.60m**; target path **20m** then ambition **30m**
  - **BS assets 9.14m** · credit portfolio **7.27m** · at-work **10m** · equity **9.10m** · first-loss **0.8m** · cash **0.58m**
  - **Net loss 0.52m** 2023 (op +18k then provisions/FX); revenues **0.70m**
  - **DGD FCA 900k** (450+270+180): spend **902k** of which first-loss **800.7k** + invest-ready **79k** + derisk **22k**; claim **~11x** private leverage
  - **BIO equity EUR 2.0m** (invest page Jan 2026); dual BIO AR named Kampani 2m
  - **Portfolio L5 public:** named EUR sample sum **~5.84m** (U-IMCEC 1.0 largest); USD face sample **~10.57m** (no FX invent); site **13m+** deployed / **30+** deals / **100k** farmers class
  - Dual: Enabel pipeline (BioPhyto/OJA); Cera **3%** shareholdership pie; Alterfin on board; NGO shareholders (Rikolto/Trias/Oxfam/BD)
  - Residual: AR2024-25 PDFs behind SharePoint login (not FOI-material for private fund)
- Wrote: sources +4; entity kampani update; budgets +28; cmt +1; lb +10; rq_437=done; spawn **rq_438**; ticks=446
- FOI: none new (public fills strong; private AR gate not public-euro opacity)
- Next: prio5 **rq_438**; deferred **rq_116** SWA

### 2026-08-02T14:15:00Z - tick 447
- Unit: **rq_438** (FOI-adjacent hole-fill - **King Baudouin Foundation / KBS budget 2025-26 + National Lottery dual**)
- Found (strong primary KBF official figures snapshot + budget pie + over-ons + homepage):
  - **2026 budget EUR 273m** = funds managed **212m** + other ops/financial **51m** + **National Lottery allocation 10m**
  - **2025 budget EUR 220.3m** (over-ons; largest public-utility foundation BE)
  - **Support given 2025 >EUR 202m** · orgs **4,710** · individuals **445** · beneficiaries class **5,155**
  - Active funds **1,723** · project calls **201** · staff **200** · experts/juries **4,300** · third-party donations **>219k**
  - Dual: Kampani AR pie **~7%** KBF shareholder; public lottery path into foundation philanthropy stack
  - Residual: full Calameo financial statements (endowment BS, personnel cost, top L5 grantees) not extracted this tick
- Wrote: sources +4; entity kbf; budgets +15; cmt +1; lb +10; rq_438=done; spawn **rq_439**; ticks=447
- FOI: none new (public infographics strong; optional FS deepen later not material opacity)
- Next: prio5 **rq_439**; deferred **rq_116** SWA

### 2026-08-02T14:45:00Z - tick 448
- Unit: **rq_439** (FOI-adjacent hole-fill - **Nationale Loterij JV2024 society return + dual KBF lottery path**)
- Found (strong primary Nationale Loterij Jaarverslag 2024 + 2025 press):
  - **Omzet/inzetten 2024 EUR 1.553bn** (+4.4pct) · **2025 EUR 1.666bn** record
  - **Society return 2024 EUR 362.5m** = **goede doelen 217.5m** (contract base 200m + extra 17.5m) + **monopolierente 145m** to State
  - **2025 society ~EUR 370m** press (subsidies+monopolierente class)
  - Projects **1,857** 2024 · ~**1,970** 2025 medium · prizes **1.057bn** · equity **234.74m** (capital 180m)
  - Ownership **State 78.72% / FPIM 21.28%** · digital stakes **415m** (27%) · board pay **0.38m**
  - Product L5 2024: EuroMillions **489m** · Instant **486m** · Lotto **441m**
  - Dual: KBF **10m** 2026 lottery allocation is subset of good-causes stack; residual full KB verdelingsplan L5 (communities/BOIC/etc.)
- Wrote: sources +3; entity nationale_loterij; budgets +24; cmt +1; lb +10; rq_439=done; spawn **rq_440**; ticks=448
- FOI: none new (optional verdelingsplan top-L5 later if KB PDF not public)
- Next: prio5 **rq_440**; deferred **rq_116** SWA

### 2026-08-02T15:15:00Z - tick 449
- Unit: **rq_440** (FOI-adjacent hole-fill - **Nationale Loterij verdelingsplan 2024 provisional L5 full table**)
- Found (strong primary KB 2 jun 2024 OpenJustice provisional plan; definitive total from AR/Stradalex):
  - **Provisional total EUR 200.0m** · **definitive 217.5m** (+17.5m extra matches AR)
  - **Cat1 deelstaten 54.88m (27.44%):** VL **33.121738m** · FWB **21.295733m** · DG **0.462529m**
  - **Cat2:** DGD **84.708565m** (largest) · KBF **9.8m** (dual KBF pie path)
  - **Named L5 sample:** Unia **4.309m** · Myria **1.077m** · IEFH **0.15m** · BOIC **1.855m** · Olympic Talents **1.5m** · BPC **0.375m** · Bozar **3.095m** · Munt **1.489m** · NOB **1.484m** · Antigif **2.2m** · Child Focus **1.6m** · Rode Kruis **1.634m** · Regie Gebouwen **3.088m** · Nationaal Prestige **10.656m** · Sports fed **2.7m** · calls armoede+SDG **3.0m**
  - Dual: equality bodies lottery lines narrow Unia/Myria FOI residuals; culture protocol Bozar/Munt/NOB
  - Residual: definitive KB full table delta allocation of +17.5m not extracted this tick
- Wrote: sources +2; entity boic; budgets +25; cmt +1; lb +10; rq_440=done; spawn **rq_441**; ticks=449
- FOI: none new (provisional L5 public; optional FOI only for Nationaal Prestige sub-list if needed later)
- Next: prio5 **rq_441**; deferred **rq_116** SWA

### 2026-08-02T15:45:00Z - tick 450
- Unit: **rq_441** (**progress milestone @450** - coverage % + waste top10 refresh; no new euro invent)
- Snapshot (honest order-of-magnitude vs TE EUR 347.956 bn):
  - **A L0 / B L1:** **100%** (unchanged strong)
  - **C L2:** **~98-99%** - + NL SOE 1.55-1.67bn omzet / society 362.5m · KBF 220-273m (public-utility off pure TE) · impact dual BIO/Alterfin/Incofin/Kampani/BRS
  - **D L5:** **~25-38%** generous (+ NL verdelingsplan 200m named table DGD 84.7 VL 33.1 KBF 9.8 Unia 4.3 BOIC/culture; DGD/BIO named samples; residual FOI ASBL/firm)
  - **E FOI ready:** **~215** (answered **~9**; total FOI rows **~226** stable)
- Inventory: budgets ~8018 · cmt ~803 · lb ~1398 · entities ~367 · sources ~779
- Waste top10: **stable** fossil/company-cars/cheque/EIWT; no reorder; lottery/ODA/KBF maps off pure waste top10
- Dual/off-TE: NL stakes 1.55-1.67bn; KBF managed funds 212m; BIO 1.2bn; taxex 29.7bn
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_441=done; spawn **rq_442**; ticks=450
- FOI: no new gap this tick (progress only)
- Next: prio5 **rq_442** hole-fill; deferred **rq_116** SWA

### 2026-08-02T16:15:00Z - tick 451
- Unit: **rq_442** (FOI-adjacent hole-fill - **Antigifcentrum AR2024 institutional TCO dual NL verdelingsplan 2.2m**)
- Found (strong primary Antigifcentrum Jaarrapport 2024):
  - **Costs 2024 EUR 3.418m** · **income 3.420m** · surplus **€2.2k**
  - **NL base subsidy EUR 2.200m** (Volksgezondheid via lottery) **matches KB plan exactly** · + ICT project **€28.9k** · NL total **€2.229m** (~65% income)
  - **Budget 2025:** NL base **€2.624m** · costs **€3.950m** (personnel **€3.293m** spike) · income **€3.930m**
  - Personnel outturn **€2.133m** · staff **23 / 20.5 FTE** · calls **~64,000** · Lux convention **€0.346m** · projects **€0.440m** · industry essenscia/pharma **€86.5k**
  - Status: public-utility foundation (KB 1967) · emergency service (KB 2002)
  - Dual method: plan L5 line closed by institutional AR for this end-receiver
- Wrote: sources +1; entity antigifcentrum; budgets +18; cmt +1; lb +10; rq_442=done; spawn **rq_443**; ticks=451
- FOI: none new (AR public; next similar NL L5: Child Focus / BOIC / Unia reconcile)
- Next: prio5 **rq_443**; deferred **rq_116** SWA

### 2026-08-02T16:45:00Z - tick 452
- Unit: **rq_443** (FOI-adjacent hole-fill - **Child Focus AR2024-25 dual NL verdelingsplan 1.6m**)
- Found (strong primary Child Focus Jaarverslag 2025 + 2024):
  - **Income 2025 EUR 9.595m** (2024 **9.306m**) · expenses **9.430m** / **9.267m** · result **0.182m** / **0.034m**
  - **Assets 7.825m** · equity **5.733m** · investments **5.726m**
  - **Dotaties/subsidies line 2.874m** 2025 · cash donations **5.681m** · in-kind **0.789m** · wages **5.208m** · honoraria **2.529m**
  - **NL:** plan werking **EUR 1.600m** 2024 · pie **21% 2024 / 20% 2025** implies **~1.95m / ~1.92m** total NL class (may include non-werking support) · renewed partnership 2025
  - Dual KBF pie **~1%** · EU projects **4-6%** · private recurrent donors **44-47%** · donors tax attests **36,525** 2025
  - Status: public-utility foundation · hotline **116 000**
- Wrote: sources +2; entity child_focus; budgets +18; cmt +1; lb +10; rq_443=done; spawn **rq_444**; ticks=452
- FOI: none new (AR public; residual exact NL cash vs pie optional)
- Next: prio5 **rq_444** (BOIC / Unia / Red Cross NL dual); deferred **rq_116** SWA

### 2026-08-02T17:15:00Z - tick 453
- Unit: **rq_444** (FOI-adjacent hole-fill - **Unia dual NL verdelingsplan 4.31m inside federal + BS/P&L L5**)
- Found (strong primary Unia RA2025 already mapped + new dual arithmetic + BS L5):
  - **Federal subvention 2024 EUR 8.171m / 2025 8.305m** · **NL plan Unia 4.309m** = **~53% of federal 2024** · residual pure federal **EUR 3.862m**
  - **TCO 2025:** products **11.728m** · charges **11.715m** · result **13k** · subsidies **9.628m** (fed 8.305 + federated 1.323)
  - **BS EOY2025:** assets **8.881m** · equity **5.485m** (capital **3.451m**) · ST debt **2.885m** · provisions **0.511m**
  - **Cost L5:** personnel **9.051m** (~77%) · opex **1.530m** · projects **0.931m**
  - **Income L5:** activity **0.899m** · project products **0.718m**
  - Dual method: plan L5 + federal AR (Antigif/Child Focus pattern); FOI residual narrowed (BGD codes + 2025 lottery exact + federated entity split)
- Wrote: sources +1; budgets +14; cmt +1; lb +10; foi gap_unia note; rq_444=done; spawn **rq_445**; ticks=453
- FOI: gap_unia_funding_detail updated residual (still ready human send; lottery plan dual filled)
- Next: prio5 **rq_445** (BOIC / Red Cross / Bozar NL dual); deferred **rq_116** SWA

### 2026-08-02T17:45:00Z - tick 454
- Unit: **rq_445** (FOI-adjacent hole-fill - **BOZAR AR2024 activity dual NL 3.1m + federal public stack 18.6m**)
- Found (strong primary Bozar Jaarverslag 2024 + prior Kamer/NBB/NL plan):
  - **Public stack 2024 EUR 18.624m** = federal dot **15.529m** + NL lottery **3.095m** (~17% NL)
  - **Statutory omzet 8.156m 2024** / **8.945m 2025** (commercial layer; not full TCO)
  - **Activity 2024:** visitors **625,840** · expo **323,459** (+56%) · concerts **152,715**/227 · talks **29,041** · film **12,040** · external **90,308**
  - **Staff 243** (188 permanent) · FTE plan max **249.98** · hires **118** · Maecenas **240**
  - Surrealism expo **118,886** visitors · management contract expired EOY2024 **+1y extension** pending new gov
  - Dual: culture triple Monnaie/NOB; Beliris M/Studio renovation; Regie Gebouwen lighting studies
- Wrote: sources +1; entity bozar update; budgets +14; cmt +1; lb +10; foi gap_fed_culture note; rq_445=done; spawn **rq_446**; ticks=454
- FOI: gap_fed_culture residual (post-cut cash + new contracts) still ready; activity dual closed
- Next: prio5 **rq_446** (Monnaie / NOB / Myria / BOIC NL dual); deferred **rq_116** SWA

### 2026-08-02T18:15:00Z - tick 455
- Unit: **rq_446** (FOI-adjacent hole-fill - **La Monnaie / De Munt AR2024 full TCO dual NL 1.59m**)
- Found (strong primary De Munt Jaarverslag 2024):
  - **Income 2024 EUR 65.367m** / **exp 64.557m** / result **+0.810m** (accounting +667k; residual losses after -107k)
  - **Federal cash 42.534m** (Kamer budgeted 42.173m) / **2023 41.859m**
  - **NL lottery 1.589m** = plan base **1.489m** + prestige **Ring +0.1m** (~3.6% of fed+NL stack **44.123m**)
  - Public grants all (fed+NL+other 0.139+Beliris 0.607) **44.869m**
  - **Payroll 33.084m** / fixed costs **41.124m** / production **14.188m** / Tax Shelter net **4.6m** (receipts 11.335 / exp 6.769)
  - Ticketing **5.728m** fill **98%** / mecenaat **1.680m**
  - Staff **436 HC / 392.9 FTE** (FR 331 NL 105) / streaming **278,611** views
  - Dual method: full institutional P&L closes Monnaie side of culture triple (stronger than Bozar omzet-only)
- Wrote: sources +1; entity la_monnaie update; budgets +24; cmt +1; lb +10; foi gap_fed_culture note; rq_446=done; spawn **rq_447**; ticks=455
- FOI: gap_fed_culture residual (2025 post-cut + new contracts + NOB AR) still ready; Monnaie 2024 NL dual closed
- Next: prio5 **rq_447** (NOB / BOIC / Myria NL dual); deferred **rq_116** SWA

### 2026-08-02T18:45:00Z - tick 456
- Unit: **rq_447** (FOI-adjacent hole-fill - **NOB public stack + NL culture protocol 7m dual culture triple close**)
- Found (strong primary NL/BNO press + Kamer 56K0856/016 + medium 56K1280/034):
  - **NOB 2024 public stack EUR 12.380m** = fed **10.896m** + NL plan **1.4835m** (~12% NL)
  - **NL protocols 2026-06-24 total EUR 7.0m**: Bozar **3.5m** + Monnaie **1.75m** + NOB **1.75m** (uplift **+0.933m** vs 2024 provisional named 6.067m)
  - **2026 cut path (medium rounded debate):** NOB **~11→10m** · Monnaie **~42.75→42.24m** · Bozar **~15.66→15.52m** sum **~67.76m**
  - Activity: concerts path **41→75**; house orchestra Bozar ~30 copros 2025; progressive integration residual
  - Bozar VL co-finance **~0.8m -0.1m**; RRF digital **7.5m** 2021-26 (beleidsnota)
  - **NOP NV satellite** brutomarge **0.328m** / 1.8 FTE — **not** institutional TCO (perimeter warning)
  - No public full NOB institutional AR P&L found (unlike Monnaie); Infocenter FTE charts only
- Wrote: sources +4; entity nob update; budgets +17; cmt +2; lb +10; foi gap_fed_culture note; rq_447=done; spawn **rq_448**; ticks=456
- FOI: gap_fed_culture still ready — residual **NOB AR TCO** + exact post-cut codes + signed contracts; culture triple financing layer largely closed
- Next: prio5 **rq_448** (BOIC / Myria / Red Cross NL dual or equality residual); deferred **rq_116** SWA

### 2026-08-02T19:15:00Z - tick 457
- Unit: **rq_448** (FOI-adjacent hole-fill - **BOIC dual NL sport stack + Paris premies 1.058m + VL 0.5m**)
- Found (strong primary BOIC/Team Belgium + NL plan KB + Sport Vlaanderen press):
  - **NL plan structural 2024 EUR 3.730m** = BOIC werking **1.855m** + Olympic Talents **1.500m** + BPC **0.375m**
  - **Paris 2024 premiums cash EUR 1.058m** (Oly **0.6455** + Para **0.4125**); gold/silver/bronze **50/30/20k** equal Oly=Para first time
  - Public class if additive **~4.79m** (premies may sit outside annual plan lines — medium)
  - **VL topsport 31.5m/yr** of which **BOIC subsidy 0.5m** stages/competitions (partnership to LA 2028)
  - Dual community topsport: VL + Adeps + DG + BOIC Olympic partner
  - **BOPC merger** BOIC+BPC from **2027-01-01**; NL partnership to 2028; Milano premies same grid (contingent cash)
  - Team Belgium Paris ~165 / Milano **30** athletes
  - No public full BOIC institutional AR P&L found
- Wrote: sources +4; entity boic update; budgets +12; cmt +1; lb +10; FOI **gap_boic_institutional_tco** ready; rq_448=done; spawn **rq_449**; ticks=457
- FOI: gap_boic_institutional_tco draft ready human send (AR TCO + L5 recon + BOPC business case)
- Next: prio5 **rq_449** (Myria NL dual / Red Cross / residual); deferred **rq_116** SWA

### 2026-08-02T19:45:00Z - tick 458
- Unit: **rq_449** (FOI-adjacent hole-fill - **Rode Kruis-Vlaanderen TCO dual Fedasil 140m + NL 1.63m**)
- Found (strong primary RKV finance portal):
  - **Income 2024 EUR 312.8m** = asylum **140.0m** + blood **114.0m** + humanitarian **58.7m**
  - **Costs 314.4m** = asylum **140.3m** + blood **110.9m** + humanitarian **63.2m** (~-1.6m class)
  - **NL plan 1.634m** ~**0.5%** of income (tiny vs TCO)
  - Asylum under **Fedasil opvangconventie** — major named L5 under third-party **559m** path
  - IFRC dues **0.330m** + EU office **27k** + Standing Comm **3k**
  - Dual: FR Croix-Rouge separate; VL Helper decree 2024 legal personality; volunteers class 12.5k
- Wrote: sources +3; entity rode_kruis_vlaanderen; budgets +14; cmt +1; lb +10; foi gap_fedasil note; rq_449=done; spawn **rq_450**; ticks=458
- FOI: gap_fedasil partial fill RKV 140m; residual other partners still ready human send
- Next: prio5 **rq_450** (Myria NL dual / progress@460); deferred **rq_116** SWA

### 2026-08-02T20:15:00Z - tick 459
- Unit: **rq_450** (FOI-adjacent hole-fill - **Myria dual federal AB multi-year + NL plan 1.077m**)
- Found (strong Kamer AB tables + NL plan; weak political claims separated):
  - **AB path strong:** 2021 **1.268m** · 2022 **1.255** · 2023 **1.645** (55K2933) · 2024 **1.579** (56K1281; alt older 1.606) · 2025 **1.614** · 2026 **1.600**
  - **NL plan 2024 EUR 1.077m** · historic **0.900m** 2021 (cited)
  - **Additive stack class 2024 EUR 2.656m** if NL outside AB (Unia-style inside-federal residual FOI)
  - Political abolition bill **2.415m 2023** = weak; recon class AB 1.645 + ~0.77 NL gap (not audited pure federal)
  - Dual equality/HR stack: Unia+Myria+IEFH NL ~5.54m; Myria ~1/5 Unia federal scale
- Wrote: sources +3; entity myria update; budgets +10; cmt +1; lb +10; foi gap_myria note; rq_450=done; spawn **rq_451**; ticks=459
- FOI: gap_myria_other_income residual narrowed (NL channel inside/outside + cash + FTE) still ready human send
- Next: prio5 **rq_451** then **progress@460**; deferred **rq_116** SWA

### 2026-08-02T20:45:00Z - tick 460
- Unit: **rq_451** (**progress milestone @460** - coverage % + waste top10 refresh; no new euro invent)
- Found (inventory + synthesis ticks 451-459 dual NL end-receiver wave):
  - **A L0:** **100%** TE €347.956bn
  - **B L1:** **100%** unconsol map
  - **C L2:** **~98-99%** (+ Monnaie TCO 65.4m · Bozar stack 18.6m · NOB 12.4m · RKV 313m)
  - **D L5:** **~26-39%** generous (+ Antigif/Child Focus/Unia/culture protocol 7m/BOIC/Myria/RKV asylum 140m dual method)
  - **E FOI ready:** **~217** (answered **~9**; total FOI rows **~227** + gap_boic)
- Inventory: budgets ~8160 · cmt ~814 · lb ~1489 · entities ~371 · sources ~800
- Waste top10: **stable** fossil/company-cars/cheque/EIWT; no reorder; dual NL maps off pure waste top10
- Dual/off-TE: culture triple · equality NL stack · RKV Fedasil L5 · lottery stakes 1.55-1.67bn
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_451=done; spawn **rq_452**; ticks=460
- FOI: no new gap this tick (progress only)
- Next: prio5 **rq_452** hole-fill; deferred **rq_116** SWA

### 2026-08-02T21:15:00Z - tick 461
- Unit: **rq_452** (FOI-adjacent hole-fill - **NL provisional verdelingsplan 2025 full L5 table 200m**)
- Found (strong primary KB 28 Jul 2025 / BS / Refli):
  - **Total provisional EUR 200m** same envelope as 2024 provisional
  - **Communities:** VL **33.202m** · FWB **21.216m** · DG **0.463m** (27.44% key)
  - **DGD 84.709m** · **KBF 9.8m** flat
  - **Culture protocol embedded:** Bozar **3.5** + Munt **1.75** + NOB **1.75** = **7.0m** (confirms June 2026 protocol dual)
  - **Sport:** BOIC **2.0m** (was 1.855) · BPC **0.45** · Be Gold **1.5** · sports fed **2.7** · women high-level **1.0m** NEW
  - **Equality/HR:** Unia **4.309** · Myria **1.077** · IEFH **0.15** flat · SARC/CPVS **1.616m** NEW dual IEFH
  - **Health/hum:** Antigif **2.45** (up) · Child Focus **1.76** (up) · Rode Kruis **1.65**
  - **Prestige pot 6.176m** (cut vs 10.656m 2024 plan) · Regie **3.088** · Flagey **0.25** · Europalia **0.5** · Cinematek **0.7**
  - Project calls poverty **2.5m** · SDG local **1.5m** · G-sport **1.0m**
- Wrote: sources +1; budgets +28; cmt +1; lb +10; rq_452=done; spawn **rq_453**; ticks=461
- FOI: none new (plan public; residual prestige named L5 + definitive 2025 when published)
- Next: prio5 **rq_453** (SARC dual / Flagey / Prestige L5 / definitive 2024 delta); deferred **rq_116** SWA

### 2026-08-02T21:45:00Z � tick 462
- Unit: rq_453 (CPVS/SARC dual FOI-adjacent hole-fill)
- Found: **Strong dual CPVS stack.** (1) IEFH RA2024 CPVS cash **�10.926m** (already mapped). (2) NL provisional 2025 SARC/CPVS **�1.616m** (tick461). (3) **INAMI** primary: from 2026 INAMI funds hospital CPVS (13 centres); IEFH funded pre-2026 by size; IEFH keeps national coordination (src_inami_cpvs_transfer_2025). (4) **Kamer 56K0854/037** minister: 2026 annual envelope **�26.4m** = Fonds Blouses blanches **�11.7m** + extra 3 centres **�5.8m** + IEFH?INAMI **�8.9m**; Justice �0. Dual recon: announced IEFH transfer 8.9 vs 2024 cash 10.9 residual FOI; NL lottery line additive not double-count of main channel. Flagey entity stub (NL 0.25m) � AR TCO residual.
- Wrote: sources (+3); budgets (+5); entities (cpvs_network, flagey); commitments (cmt_cpvs_inami_envelope_2026); leaderboard (+2 update sarc+iefh_cpvs); foi_queue gap_iefh notes; FOI draft note; rq_453=done rq_454=open; loop_state ticks=462
- FOI opened: none new; gap_iefh residual narrowed (transfer perimeter public; hospital L5 cash still opaque)
- Next: rq_454 (prestige L5 / Flagey AR / definitive NL 2024 delta / next FOI-adjacent); rq_116 SWA deferred

### 2026-08-02T22:15:00Z � tick 463
- Unit: rq_454 (NL definitive 2025 plan dual vs provisional)
- Found: **Strong primary** KB 5 Jun 2026 (Refli 2026004330) definitive verdelingsplan **�240m** vs provisional �200m (**+�40m**). Cat1 communities **�65.856m** (DG 0.555 VL 39.842 FR 25.459). DGD 84.709 KBF **10.3** (was 9.8). Prestige **10.000016m** (prov 6.176 restored up). NEW large: LOV2030 Leuven **10.5m**, Pro League **3.5m**, women sport **2.0m**, BPC Road LA **1.1m**, EYOF2029 1.0, sports fed 2.7, local heritage call 4.0, poverty call 2.5. Culture triple 7.0 + Flagey 0.25 Europalia 0.5 Cinematek 0.7 + SARC 1.616 confirmed. Residual: prestige sub-L5 + Art5 committee notes FOI.
- Wrote: sources (+2); budgets (+28); entities (europalia cinematek pro_league); cmt; leaderboard (+5 update); foi gap_nl_prestige_l5 ready + draft; rq_454=done rq_455=open; ticks=463
- FOI opened: gap_nl_prestige_l5 (ready, human send)
- Next: rq_455 (prestige FOI-adjacent public scraps / LOV2030 dual / definitive multi-year notes); rq_116 SWA deferred

### 2026-08-02T22:45:00Z � tick 464
- Unit: rq_455 (LOV2030 dual bidbook + NL definitive)
- Found: **Strong dual LOV2030.** Final bidbook ECoC: total operating **�72.5m** = EU **1.5** + federal via NL **15** (3m�5 2026-30, CM 17 May 2024) + Flanders **30** + province **3** + city Leuven **10** (council 26 May 2025) + region mun **3** + private ambition **10** (medium). Artistic **�47.12m**. Dual NL definitive plan 2025 line **�10.5m** (front-load vs bidbook 3m/yr from 2026 � residual FOI cash schedule).
- Wrote: sources (+2); budgets (+11); entity lov2030; cmt; leaderboard (+5 update); foi gap_lov2030_cash_schedule ready+draft; rq_455=done rq_456=open; ticks=464
- FOI opened: gap_lov2030_cash_schedule (ready, human send)
- Next: rq_456 (Pro League dual / Art5 residual public / definitive multi-year notes); rq_116 SWA deferred

### 2026-08-02T23:15:00Z � tick 465
- Unit: **rq_456** (FOI-adjacent hole-fill � **Pro League dual NL 3.5m FSR + Beliris culture dual + Art5/7 notes**)
- Found (strong primary KB 5 Jun 2026 + Pro League + Beliris 2025):
  - **Pro League NL Art5.11 EUR 3.5m** FSR + veiligheid + innovatie (definitive NEW; known tick463)
  - **Dual private layer:** Pro League own FSR grants **EUR 200k** to **28 clubs** (3�13k each, Jul 2025) � not public euro
  - **Related football NL:** Lotto Red Courts **0.2m** (cat3.29)
  - **Named sport stack definitive 2025 EUR 14.45m** = ProLeague3.5 + RedCourts0.2 + Women2.0 + SportsFed2.7 + BOIC2.0 + BPC0.45 + RoadLA1.1 + BeGold1.5 + EYOF1.0
  - **Beliris culture dual 2025:** Flagey **3.235m** (studio renovation engagement) + NOB **3.4m** rehearsal + Monnaie package **2.962m** (liq **0.2065m** 2025) = culture class **9.597m**; dual Flagey public class **3.485m** (Beliris capex + NL opex 0.25)
  - **Beliris STIB Gare Centrale** total **20m** / **>3.5m** paid 2025 (floor medium)
  - **Art5/Art7 governance:** sub-notes cats 3.17/3.31/3.32/5.3/5.5/5.6/5.10; multi-year frames 5.7?2031 5.8 EYOF?2029 5.9 LOV?2030; Art4 advances 50/80pct
- Wrote: sources +5; budgets +11; cmt +3; lb +10; entities flagey+pro_league; FOI **gap_proleague_fsr_use** ready+draft; gap_nl_prestige note; rq_456=done spawn **rq_457**; ticks=465
- FOI opened: gap_proleague_fsr_use (ready, human send); gap_nl_prestige residual Art5/7 still ready
- Next: prio5 **rq_457** (Festivals VL/WAL dual / Europalia AR / Chinese Pavilion / residual sport Art5); deferred **rq_116** SWA

### 2026-08-02T23:45:00Z � tick 466
- Unit: **rq_457** (FOI-adjacent hole-fill � **Chinese Pavilion PPP dual + Festivals VL/WAL classical dual**)
- Found (strong/medium primary):
  - **Chinees Paviljoen Laken PPP:** Regie works budget **ca EUR 6m** (primary agency page); Hennebert private target **6�7m** / first **1m** in (medium press); opening class end-2027/2028; vzw Chinees Paleis Zijderoute; Koninklijke Schenking owner; closed 2013
  - **NL Art5.7 EUR 0.5m** definitive multi-year frame **to 2031** (Histoire des Belges 2030) � strong dual public named layer
  - **Envelope caution:** Regie 6m vs private 6�7m may be **same PPP envelope** � do not sum as pure public without FOI
  - **Festivals dual classical:** VL **259k** + WAL **191k** = **450k** NL definitive (Art5.3+5.4); classical music prog **560k** (3.32) related; Art5 sub-note residual member festivals
- Wrote: sources +5; budgets +9; cmt +2; lb +6; entities +4 (chinees_paleis_vzw festivals_vl/wal regie_gebouwen); FOI **gap_chinees_paviljoen_cash** ready+draft; rq_457=done spawn **rq_458**; ticks=466
- FOI opened: gap_chinees_paviljoen_cash (ready, human send)
- Next: prio5 **rq_458** (Europalia dual / Cinematek BELSPO / Queen Elisabeth competition / residual); deferred **rq_116** SWA

### 2026-08-03T00:15:00Z � tick 467
- Unit: **rq_458** (FOI-adjacent hole-fill � **Cinematek dual fed 3.3m + Europalia dual 573k + CRE dual**)
- Found (strong primary Kamer 56K0855/018 + NL KB + BELSPO):
  - **Cinematek BA 60.36.41.40.01:** 2023r **3.230m** � 2024a **3.296** � 2025i **3.306** � 2026 **3.236** � path to 3.098 2028 (kEUR tables)
  - **Dual stack 2025 EUR 4.006m** = fed 3.306 + NL plan **0.7m**; debt repay **0.1m/yr** (12y loan 2020)
  - **DIGIT-04:** programme **37.63m** 2019-24 shared FWI+Cinematek (58 FTE); BA complementary 2025i **1.661m** shared (not pure Cinematek L5)
  - **Europalia dual:** fed facultative BA 61.14.33.00.17 **73k** flat + NL **500k** = **573k** public class 2025
  - **Queen Elisabeth stack:** NL Art5.2 **220k** + fed prize 2nd laureate **20k** = **240k**; Chapelle musicale RE **155k** separate entity
- Wrote: sources +5; budgets +14; cmt +3; lb +7; entities +3 update 2; FOI **gap_cinematek_digit_l5** ready+draft; rq_458=done spawn **rq_459**; ticks=467
- FOI opened: gap_cinematek_digit_l5 (ready, human send)
- Next: prio5 **rq_459** (proximity local 1m Art5 / IRPA 0.4m / FWI projects 0.5m / residual culture); deferred **rq_116** SWA

### 2026-08-03T00:45:00Z � tick 468
- Unit: **rq_459** (FOI-adjacent hole-fill � **KIK-IRPA dual 6.97m + Art pool 33m + Proximity 1m**)
- Found (strong primary Kamer 56K0855/018 + NL KB):
  - **KIK-IRPA BA 60.34.41.30.22:** 2023r **6.598m** � 2024a **6.615** � 2025i **6.573** � path to 6.218 2028
  - **Dual stack 2025 EUR 6.973m** = fed 6.573 + NL Art3.24 **0.4m**
  - **Art pool FWI 2025i:** KMKG **14.510m** + KMSKB **11.942m** + KIK **6.573m** = **33.025m**
  - **Horizon 50-200** Jubelpark bicentenaire detached staff **193k** (Regie+Beliris path to 2030)
  - **NL Proximity Art5.6 EUR 1.0m** � Art6 split by province population (named L5 residual)
  - **NL FWI projects Art3.25 EUR 0.5m** + Regie patrimonium **3.088m** confirmed
  - ICCROM BE contribution **41k**
- Wrote: sources +4; budgets +14; cmt +3; lb +9; entities +4; FOI **gap_nl_fwi_irpa_l5** + **gap_nl_proximity_l5** ready+drafts; rq_459=done spawn **rq_460**; ticks=468
- FOI opened: 2 ready (human send)
- Next: prio5 **rq_460** then **progress@470**; deferred **rq_116** SWA

### 2026-08-03T01:15:00Z � tick 469
- Unit: **rq_460** (FOI-adjacent hole-fill � **BELSPO four FWI pools structural 132.3m 2025i**)
- Found (strong primary Kamer 56K0855/018 complete FWI map):
  - **Doc pool EUR 33.155m:** KBR **17.041** + ARA **16.114**
  - **Space pool EUR 30.695m:** KMI **11.300** + BIRA **6.861** + KSB **8.765** + common **1.356** + Climate Center **2.000** + STCE residual **0.413**
  - **Nature pool EUR 35.396m:** KBIN **19.482** + KMMA **11.771** + Belgica/JEMU **4.143**
  - **Art pool EUR 33.025m** (prior tick468): KMKG 14.51 + KMSKB 11.94 + KIK 6.57
  - **Grand structural sum EUR 132.271m** 2025i + NL FWI projects **0.5m** additive (L5 residual prior FOI)
- Wrote: sources +2; budgets +15; cmt +1; lb +9; entities +7; rq_460=done spawn **rq_461** (progress@470); ticks=469
- FOI: none new (structural public; gap_nl_fwi_irpa_l5 still covers project L5)
- Next: **progress@470** (coverage % + waste top10); deferred **rq_116** SWA

### 2026-08-03T01:45:00Z � tick 470
- Unit: **rq_461** (**progress milestone @470** � coverage % + waste top10 refresh; no new euro invent)
- Found (inventory + synthesis ticks 461�469 dual/NL/FWI wave):
  - **A L0:** **100%** TE �347.956bn
  - **B L1:** **100%** unconsol map
  - **C L2:** **~99%** (+ BELSPO four FWI pools **�132.3m** � Cinematek dual **�4.0m** � KIK-IRPA dual **�7.0m** � LOV2030 **�72.5m** envelope)
  - **D L5:** **~27�40%** generous (+ NL definitive **�240m** � LOV2030 plan 10.5 � Pro League 3.5 � CPVS 26.4 � Beliris culture 9.6 � Pavilion PPP � Festivals/Europalia/CRE duals)
  - **E FOI ready:** **~223** (answered **~9**; total FOI rows **~234**)
- Inventory: budgets ~8302 � cmt ~832 � lb ~1551 � entities ~398 � sources ~831
- Waste top10: **stable** fossil/company-cars/cheque/EIWT; no reorder; FWI/LOV/culture duals off pure waste top10
- Dual/off-TE: NL definitive 240m � FWI 132m structural � LOV2030 multi-level � lottery stakes
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_461=done; spawn **rq_462**; ticks=470
- FOI: no new gap this tick (progress only)
- Next: prio5 **rq_462** hole-fill; deferred **rq_116** SWA

### 2026-08-03T02:15:00Z � tick 471
- Unit: **rq_462** (FOI-adjacent hole-fill � **Be Gold dual multi-community topsport 3.5m**)
- Found (strong primary Be Gold partners page + programme + NL plan match):
  - **Annual total EUR 3.500m** split: NL **1.500** (43%) � BOIC **0.750** � Sport Vlaanderen **0.740** � ADEPS/FWB **0.500** � Ostbelgien **0.010**
  - **NL plan Art3.26 1.5m** matches partners page exactly (strong dual closed)
  - **Cumulative since 2004 EUR 49,261,432.08**
  - **Athletes:** 148 (14�24y) � 90F/58M � 20 disciplines � 4 teams � goal Top8 OS / Top3 PS � max 4y support from 2025
  - Dual method: multi-community topsport + BOIC + lottery (parallel BOIC stack prior)
- Wrote: sources +3; budgets +8; cmt +1; lb +6; entity begold + update sport_vlaanderen/adeps/boic; rq_462=done spawn **rq_463**; ticks=471
- FOI: none new (envelope dual closed; athlete-level L5 residual privacy-sensitive optional)
- Next: prio5 **rq_463** (IARC Lyon / Leesbevordering / Opvangtehuizen / residual NL L5); deferred **rq_116** SWA

### 2026-08-03T02:45:00Z � tick 472
- Unit: **rq_463** (FOI-adjacent hole-fill � **Fairwork dual NL 250k + residual health/human NL batch 2.175m**)
- Found (strong plan + Fairwork AR2025 primary):
  - **Fairwork:** NL plan **�250k** cat3.35 � AR2025 confirms NL + Fedasil + Warmste Week + 11.11.11 + Safe.brussels + SF323 � **1.142** requests (+47%) 92 countries � financing fragile (2 contracts not renewed) � **no euro TCO table** in AR
  - **Residual NL health/human batch sum �2.175m:** IARC Lyon **�759,770** � Antikankerfonds MCN **�300k** � Opvangtehuizen **�495k** � Holocaust memorial **�370k** � Fairwork **�250k**
  - Dual: Antikankerfonds private foundation + NL MCN; IARC WHO agency lottery co-finance; shelters aggregate named residual
- Wrote: sources +3; budgets +6; cmt +2; lb +6; entities +3; FOI **gap_fairwork_tco** + **gap_nl_opvang_l5** ready+drafts; raw fairwork PDF; rq_463=done spawn **rq_464**; ticks=472
- FOI opened: 2 ready (human send)
- Next: prio5 **rq_464** (UCI cycling / Leesbevordering / Paola / residual); deferred **rq_116** SWA

### 2026-08-03T03:15:00Z � tick 473
- Unit: **rq_464** (FOI-adjacent hole-fill � **Reine Paola dual NL 260k + residual culture/social NL batch 3.32m**)
- Found (strong AR2025 + plan + medium press):
  - **Paola NL �260k** cat3.5 � **Pelicano** 1.431 young � avg **�763** � **�1.092m** medium � **�1.5m** aides directes claim � philanthropy centre **�240k** out � awards **�10k�3** � press **loss >�1.1m** 2025 medium
  - **Residual NL culture/social batch sum �3.315m:** Paola 0.26 � Grand Man�ge 0.1 (dual FWB+Ville) � Jardin Passion 0.1 � UCI races 0.6 � Leesbevordering 1.5 � Interfed poverty 0.2 � OVK 0.205 � BNA 0.15 � To Walk Again 0.1 � WWF 0.1
  - Grand Man�ge: CAV&MA partners NL+FWB+Ville; construction class �15m historical medium
- Wrote: sources +5; budgets +16; cmt +2; lb +7; entities +3; FOI **gap_paola_tco** ready+draft; raw Paola PDF; rq_464=done spawn **rq_465**; ticks=473
- FOI opened: gap_paola_tco (ready, human send)
- Next: prio5 **rq_465** (UCI Art5 races / Leesbevordering operators / Interfed poverty dual / residual); deferred **rq_116** SWA

### 2026-08-03T03:45:00Z � tick 474
- Unit: **rq_465** (FOI-adjacent hole-fill � **poverty dual stack 2.61m + homeless innovation NL 1.28m**)
- Found (strong plan + Interfed service structure + prior VL Netwerk):
  - **Homeless social innovation cat3.15 EUR 1.275725m** definitive (named city L5 residual)
  - **Poverty dual core stack EUR 2.612m** = Interfed NL **200k** + BNA NL **150k** + VL Netwerk **986k** (prior) + homeless innov **1.276m**
  - **NL poverty project call cat4.3 EUR 2.5m** (winners residual FOI) � not double-counted in core stack
  - Interfed service: multi-entity Comit� de gestion elaborates budget; host Place Victor Horta 40 CNTR; NL logo support; **structural multi-entity cash opaque**
- Wrote: sources +3; budgets +5; cmt +2; lb +5; entity interfed note; FOI **gap_interfed_poverty_budget** + **gap_nl_homeless_l5** ready+drafts; rq_465=done spawn **rq_466**; ticks=474
- FOI opened: 2 ready (human send)
- Next: prio5 **rq_466** (UCI Art5 / Leesbevordering / residual project calls); deferred **rq_116** SWA

### 2026-08-03T04:15:00Z — tick 475
- Unit: **rq_466** (FOI-adjacent hole-fill — **UCI 1.1 races 600k + Leesbevordering dual 1.5m + cat4 calls 9m**)
- Found (strong plan + primary press + UCI class sample):
  - **UCI Art3.31 EUR 600k** — Belgian UCI **1.1 one-day only** (not UWT/ProSeries); Art5 committee note residual
  - **Race-class sample (medium, not award list):** Heistse Pijl · Gooikse pijl · Binche–Chimay–Binche · GP Criquielion · Muur Classic Geraardsbergen
  - **Leesbevordering Art5.10 EUR 1.5m** (financial literacy focus) — path **~3m 2024 → 1.5m 2025**; dual VL Literatuur Vlaanderen + Iedereen Leest structural (separate euros not invented)
  - **Cat4 project calls sum EUR 9.0m:** G-sport **1m** (max 50k/project) + SDG/Academia **1.5m** (**68 orgs**) + poverty **2.5m** (**21 projects** Apr 2026) + Lokaal Erfgoed **4m**
  - Art5 residual pair UCI+Lees = **2.1m** (covered by existing gap_nl_prestige for notes)
- Wrote: sources +10; budgets +7; cmt +3; lb +7; entities +2; FOI **gap_nl_project_calls_l5** ready+draft; rq_466=done spawn **rq_467**; ticks=475
- FOI opened: gap_nl_project_calls_l5 (ready, human send)
- Next: prio5 **rq_467** (residual NL prestige sub-L5 / sports fed Art5.5 / other dual); deferred **rq_116** SWA

### 2026-08-03T04:45:00Z - tick 476
- Unit: **rq_467** (FOI-adjacent hole-fill - **sport dual residual batch 7.25m**)
- Found (strong plan + primary NL press + dual host):
  - **Sports Federations Art5.5 EUR 2.7m** - **32 federations** public count (NL Apr 2026 + JV continuity); Art5 per-fed residual FOI
  - **Women high-level sport cat3.30 EUR 2.0m** definitive (prov 1.0m uplift); dual topsport method residual L5
  - **BPC dual stack EUR 1.55m** = werking **0.45m** + Road to LA medals **1.1m**; BOPC merge 2027 path
  - **EYOF 2029 EUR 1.0m** NL multi-year Art7 to 2029; **Flanders host** dual VL principal + BOIC; VL cash residual FOI
  - **Residual sport batch sum EUR 7.25m** (excl prior Be Gold/BOIC/ProLeague/UCI/G-sport)
- Wrote: sources +7; budgets +5; cmt +5; lb +5; entities +2; FOI **gap_nl_sports_fed_l5** + **gap_eyof2029_cash_schedule** ready+drafts; rq_467=done spawn **rq_468**; ticks=476
- FOI opened: 2 ready (human send)
- Next: prio5 **rq_468** (prestige sub residual / classical 560k Art5 / other dual); deferred **rq_116** SWA

### 2026-08-03T05:15:00Z - tick 477
- Unit: **rq_468** (FOI-adjacent hole-fill - **prestige 2024 outturn 18.57m + classical dual residual 1.64m**)
- Found (strong primary NL JV2024 + NOB dual partner + plan):
  - **Nationaal Prestige 2024 cash EUR 18.56684288m** — **614 dossiers**; L3 split: culture **7.778m (42%)** · society **5.544m (30%)** · sport **5.245m (28%)**
  - **Path 2025 plan cat5.1 EUR 10.000016m** (prov 6.176m) — perimeter/timing caveat medium vs 2024 cash
  - **Proximity 2024 EUR 1.257m** — **1132** beneficiaries; plan 2025 1.0m
  - **Classical dual residual EUR 1.635m** = prog 560k + festivals 450k + CRE 220k + Flagey 250k + Chapelle 155k (excl culture triple 7m)
  - NOB/NL partners named: Flagey Bozar CRE Festivals VL/WAL Klassiek int Groen Stroom Concertgebouw Brugge Chapelle (no invent project EUR)
- Wrote: sources +5; budgets +7; cmt +4; lb +5; FOI gap_nl_prestige updated (2024 partial fill; 2025 L5 still ready); rq_468=done spawn **rq_469**; ticks=477
- FOI: gap_nl_prestige still ready human send (2025 named + recon)
- Next: prio5 **rq_469**; deferred **rq_116** SWA

### 2026-08-03T05:45:00Z - tick 478
- Unit: **rq_469** (FOI-adjacent hole-fill - **NL JV2024 financial supports architecture 201.2m**)
- Found (strong primary JV2024/RA2024):
  - **725** financial-support beneficiaries 2024 (**174** first-time)
  - Four channels sum **EUR 201.198m**:
    - Prestige **614** dossiers **18.567m** (prior tick477)
    - Child poverty call **54** dossiers **1.02208m**
    - Eco-coaching **23** dossiers **0.115m** (first call)
    - Nominative **34** beneficiaries **181.494082m** (communities KBF Red Cross Child Focus Unia class)
  - Proximity separate **1132** ben **1.257m** (not inside 725)
  - Recon to plan def 217.5m residual FOI
- Wrote: sources +4; budgets +5; cmt +4; lb +4; FOI **gap_nl_nominative_34_l5** + **gap_nl_child_eco_calls_l5** ready+drafts; rq_469=done spawn **rq_470**; ticks=478
- FOI opened: 2 ready (human send)
- Next: prio5 **rq_470** (progress@480 soon); deferred **rq_116** SWA

### 2026-08-03T06:15:00Z - tick 479
- Unit: **rq_470** (FOI-adjacent hole-fill - **NL society dual path 385m 2025**)
- Found (strong primary JV2025 + monopolierente KB):
  - **Omzet EUR 1.666bn** 2025 (vs 1.553bn 2024)
  - **Monopolierente EUR 145m** flat (KB 18 Dec 2025 + JV)
  - **Goede doelen EUR 240m** JV matches definitive verdelingsplan
  - **Society dual return EUR 385m** = 240+145 (path from **362.5m** 2024; upgrades press **~370m**)
  - **1970** maatschappelijke projecten (+4% vs ~1857 2024)
  - Residual micro batch **EUR 0.505m**: OVK 205k + TWA 100k + WWF 100k + Jardin Passion 100k
- Wrote: sources +5; budgets +7; cmt +4; lb +6; entity TWA + NL update; rq_470=done spawn **rq_471 progress@480**; ticks=479
- FOI: none new (society path closed strong; residual L5 stack already ready)
- Next: prio5 **rq_471** progress milestone @480; deferred **rq_116** SWA

### 2026-08-03T06:45:00Z - tick 480
- Unit: **rq_471** (**progress milestone @480** - coverage % + waste top10 refresh; no new euro invent)
- Found (inventory + synthesis ticks 471-479 NL dual deep-fill wave):
  - **A L0:** **100%** TE 347.956bn
  - **B L1:** **100%** unconsol map
  - **C L2:** **~99%** (+ NL society dual **385m** 2025 path)
  - **D L5:** **~28-41%** generous (+ Be Gold 3.5 · poverty dual 2.61 · cat4 9.0 · sport batch 7.25 · prestige cash 18.57 · financial supports 201 · society 385)
  - **E FOI ready:** **~234** (answered **~9**; total FOI rows **~245**)
- Inventory: budgets ~8361 · cmt ~857 · lb ~1603 · entities ~407 · sources ~874
- Waste top10: **stable** fossil/company-cars/cheque/EIWT; no reorder; NL duals off pure waste top10 (society/nominative mid-table)
- Dual/off-TE: NL society 385m · omzet 1.666bn stakes · financial supports arch 201m · prestige 18.57m
- Housekeeping: deduped duplicate nationale_loterij entity row
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_471=done; spawn **rq_472**; ticks=480
- FOI: no new gap this tick (progress only)
- Next: prio5 **rq_472** hole-fill; deferred **rq_116** SWA

### 2026-08-03T07:15:00Z - tick 481
- Unit: **rq_472** (FOI-adjacent hole-fill - **NL Democracy Fund KBF dual 500k + Regie patrimonium 3.09m**)
- Found (strong primary KBF press + NL call + Regie partnership):
  - **Democracy Fund first awards EUR 500,319** - **18 projects** Dec 2025 (VL/BRU/WAL); awards 10k-40k class; dual NL fund hosted at **KBF** (not additive to statutory KBF 10.3m)
  - Upgrades prior medium ~500k envelope to **strong exact**
  - **Regie NL cat3.13 EUR 3.087872m** definitive; partnership page **~3m/yr** national heritage dual; project L5 residual (Pavilion Art5.7 0.5m separate)
  - **Dual stack class EUR 13.388m** = KBF 10.3 + Regie 3.088
- Wrote: sources +5; budgets +4; cmt +3; lb +3; entity democracy fund; FOI **gap_nl_democracy_fund_l5** + **gap_regie_nl_projects_l5** ready+drafts; rq_472=done spawn **rq_473**; ticks=481
- FOI opened: 2 ready (human send)
- Next: prio5 **rq_473**; deferred **rq_116** SWA

### 2026-08-03T07:45:00Z - tick 482
- Unit: **rq_473** (FOI-adjacent hole-fill - **VL dienstencheques reform multi-year + dual titres WAL/BRU**)
- Found (strong primary VL begroting 2025-2029 + prior WAL/BRU):
  - **Reform measures path mEUR:** 2025 **84** · 2026 **250** · 2027 **255** · 2028 **263** · 2029 **267**
  - Split 2026: price **84** + tax benefit abolition **166**
  - Worker return varia **84m** (1 EUR/cheque back to workers) same years class
  - User price **10 EUR**; fiscal benefit ends income year 2025
  - BO2026 effort line **151.438m** different perimeter vs multi-year table **250m** 2026
  - **Dual titres stack WAL+BRU EUR 872.238m** 2026 = FOREM **568.406** + BRU **303.832** (VL full TCO residual FOI)
- Wrote: sources +4; budgets +8; cmt +2; lb +4; FOI gap_vl_dienstencheques_tco updated (measures filled; full TCO still ready); rq_473=done spawn **rq_474**; ticks=482
- FOI: gap_vl_dienstencheques_tco still ready human send (full scheme TCO)
- Next: prio5 **rq_474**; deferred **rq_116** SWA

### 2026-08-03T08:15:00Z - tick 483
- Unit: **rq_474** (FOI-adjacent hole-fill - **VL consolidation multi-year package 2025-2029**)
- Found (strong primary Vlaamse begroting 2025-2029 full tables):
  - **Total measures path mEUR:** 2025 **722** · 2026 **1.832bn** · 2027 **2.465** · 2028 **2.601** · 2029 **2.764**
  - **Jobbonus savings:** 0 / **242** / 236 / 231 / 227 (vs BO2026 keep VEK **228m** different concept; dual federal)
  - **Own gov effort:** 282 / **572** / 809 / 897 / **1.000bn** (VDAB kerntaken 20-80; De Lijn tariffs 0/50/70; subsidy reform 70 from 2026)
  - **Fiscaliteit measures:** 176 / **337** / 534 / 570 / 621
  - **Onderwijs measures:** 20 / **147** / 326 / 329 / 332
  - **Extra invest VAK period ~EUR 3.195bn**; De Lijn VAK **400m** 2025; OW infra period **1.385bn** class
  - **Social housing loans FS3+BSL EUR 14.5bn** 2025-29; **Mijn VerbouwLening EUR 1.7bn** period
- Wrote: sources +4; budgets +16; cmt +4; lb +6; rq_474=done spawn **rq_475**; ticks=483
- FOI: none new (package public; residual named L5 delivery FOI optional)
- Next: prio5 **rq_475**; deferred **rq_116** SWA

### 2026-08-03T08:45:00Z - tick 484
- Unit: **rq_475** (FOI-adjacent hole-fill - **VL Warm/Welvarend expansion + dual WAL economies**)
- Found (strong primary VL centenboekje + WAL budget press):
  - **Warm Vlaanderen VAK path mEUR:** 319 / **418** / 551 / 755 / **1.073bn** (handicap 102-478 · kinderopvang 100-200 · ouderenzorg · jeugdhulp)
  - **Welvarend VAK path:** 326 / **533** / 471 / 623 / **716** (innovatie · digi onderwijs 200 · Nederlands · inductie)
  - **Expansion total VAK:** 1.411 / **2.236bn** / 2.090 / 2.619 / **3.668bn** 2025-29
  - **WAL structural savings:** **268m** 2025 + **270m** 2026 = **538m** 2y; local share medium **~95m** 2026 (UVCW)
  - **Dual consolidation method 2026 class:** VL measures **1.832bn** + WAL **270m** (different perimeter)
- Wrote: sources +4; budgets +13; cmt +5; lb +6; FOI **gap_wal_economies_l5** ready+draft; rq_475=done spawn **rq_476**; ticks=484
- FOI opened: gap_wal_economies_l5 (ready, human send)
- Next: prio5 **rq_476**; deferred **rq_116** SWA

### 2026-08-03T09:15:00Z - tick 485
- Unit: **rq_476** (FOI-adjacent hole-fill - **BRU SEC trajectory measures 297m→1.186bn + dual triad VL/WAL/BRU**)
- Found (strong primary CoA Budgets RBC 2026 Table 1):
  - **Base SEC 2025:** **-1.241bn**; constant-policy path then new measures
  - **Total measures path mEUR:** 2026 **297** · 2027 **565** · 2028 **907** · 2029 **1.186bn**
  - Split 2026: **dep 177** + **rec 120**; 2029 dep **845** + rec **341**
  - **SEC after measures:** **-957** / **-719** / **-416** / **0** (balance 2029)
  - L5 thematic dep: personnel **84→274** · fonct+IT **127→281** · facultatives **25** flat · mobilite reinvest **-190→-37** · logement 52→15 · travail 30→65 · env 34→57 · urbanisme 18→123
  - CoA: recettes L5 **not published**; 2027-29 programme matrix thin
  - **Dual triad 2026 class:** VL measures **1.832bn** + WAL **270m** + BRU **297m** = **2.399bn** (different perimeter; not additive TE)
- Wrote: sources +2; budgets +15; cmt +2; lb +6; FOI **gap_bru_mesures_recettes_l5** ready+draft; rq_476=done spawn **rq_477**; ticks=485
- FOI opened: gap_bru_mesures_recettes_l5 (ready, human send)
- Next: prio5 **rq_477**; deferred **rq_116** SWA

### 2026-08-03T09:45:00Z - tick 486
- Unit: **rq_477** (FOI-adjacent hole-fill - **FWB SEC path -1.608→-1.224bn + dual Entity II quartet**)
- Found (strong primary DGBF elements-cles + GW CP; medium year-1 secondary):
  - **SEC path mEUR:** 2026 **-1.608bn** · 2027 **-1.405** · 2028 **-1.390** · 2029 **-1.224bn**
  - **Effort package 2029:** gross economies **670m** + new policies **180m** = net **500m** (elements-cles ~700 / <200)
  - **Deficit 2026 class 1.6bn**; debt stock **12.782bn** 2024 (risk 21bn unmitigated)
  - **Year-1 économies medium 255m** 2026 (RTBF/RTL/Le Soir; official L5 FOI)
  - LSF dots **12.996bn**; Saint-Quentin RW+COCOF **575.3m**; edu **10.929bn**
  - **Dual Entity II quartet 2026 class:** VL **1.832bn** + WAL **270m** + BRU **297m** + FWB **255m** = **2.654bn** (different perimeter)
- Wrote: sources +4; budgets +12; cmt +2; lb +6; FOI **gap_fwb_economies_l5** ready+draft; rq_477=done spawn **rq_478**; ticks=486
- FOI opened: gap_fwb_economies_l5 (ready, human send)
- Next: prio5 **rq_478**; deferred **rq_116** SWA

### 2026-08-03T10:15:00Z - tick 487
- Unit: **rq_478** (FOI-adjacent hole-fill - **FPB 263 measures inventory budget 2027 + Entity I masses dual residual gap**)
- Found (strong primary FPB Report 13320 + xlsx DATA_BUDGET2027):
  - **Inventory:** **263** measure rows (press 250+; ~230 external + ~30 DC2024); **39** with 2029 annual impulse mEUR — **not additive** (alternative scenarios)
  - **Entity I control-account residual gap 4.9bn** 2029 (0.67% GDP; CM Mar 2026 pre-Iran war) — dual vs prior decided **9.2bn** package
  - **SS 147.3bn** (pens **72.3** · health **41.3** · invalid **15.9** · chom **4.6** · other 10.1 · admin 3.0)
  - **Federal own 41.9bn** (salaries **10.9** · fonct **8.5** · subs **7.9** · invest **6.5** · handicap/GRAPA 4.3)
  - Transfers C&R **81.5bn** · interest **12.3** · UE **9.1** · recettes total **267.4** (fiscal 164.3 · SSC 93.7 · IPP 64.2 · ISOC 26.0)
  - DC2024 ranges (options): cars+cheques **4.5-5.5bn** · globalisation **5.5-11.3** · wealth tax **2.0-7.5** · health norm **3.3-4.5** · fossil transport **0.8-1.25**
  - **Dual:** E1 residual 4.9bn vs Entity II quartet class **2.65bn** 2026 (different metric)
- Wrote: sources +4; budgets +25; cmt +2; lb +7; raw xlsx; rq_478=done spawn **rq_479**; ticks=487
- FOI: none (full public inventory; adoption L5 future)
- Next: prio5 **rq_479**; deferred **rq_116** SWA

### 2026-08-03T10:45:00Z - tick 488
- Unit: **rq_479** (FOI-adjacent hole-fill - **CM Jul 2026 Entity I path control gap 7.7bn + unallocated L5 dual**)
- Found (strong primary BOSA CM rapport 6 Jul 2026 définitive):
  - **Entity I deficit path bn:** 2026 **-25.68** · 2027 **-30.34** · 2028 **-34.03** · 2029 **-38.28** · 2031 **-44.50** (−3.9→−5.7% GDP)
  - **Control-account cumulative gap:** 0.6 / 2.4 / 5.8 / **7.7bn** 2029 / 8.4 / **9.8bn** 2031 (upgrades Mar **4.9bn** pre-Iran)
  - **Net exp bn:** 197.6 → **219.6** 2029; norms 2.96→2.27%
  - **GG debt:** 110.7% 2026 → **117.1** 2029 → **122.6** 2031; Entity I debt **86.3→97.7%**
  - **Unallocated measures total 2029 +2.192bn** L5: fraud+compliance **482** · FIOD **193** · subsidy cut **199** · reorg+central **150+150** · replace ratio **175** · social/tax fraud **200+200**
  - Sous-utilisation **1.625→1.750bn**; interest ~**18.6bn** 2029 class
  - **Dual:** E1 residual control **7.7bn** vs Entity II quartet **2.65bn** 2026 class
- Wrote: sources +3; budgets +31; cmt +3; lb +7; raw PDF; rq_479=done spawn **rq_480**; ticks=488
- FOI: none (full public CM L5 unalloc; residual outturn future)
- Next: prio5 **rq_480** (progress@490 soon); deferred **rq_116** SWA

### 2026-07-28T06:27:31Z - pause
- User: **paused=yes**
- State: ticks=488 last_unit=rq_479; next on resume **rq_480** (progress@490 soon)
- No research tick; FOI not sent


### 2026-07-28T04:27:41Z - tick idle (paused)
- Unit: none — **paused=yes** (human)
- State: ticks=488 last_unit=rq_479; next on resume **rq_480** (progress@490 soon); rq_116 SWA deferred
- No research; no commit

### 2026-07-28T04:28:46Z - tick idle (paused)
- Unit: none — **paused=yes** (human)
- State: ticks=488 last_unit=rq_479; next on resume **rq_480** (progress@490 soon); rq_116 SWA deferred
- No research; no commit

### 2026-07-28T04:29:54Z - tick idle (paused)
- Unit: none — **paused=yes** (human)
- State: ticks=488 last_unit=rq_479; next on resume **rq_480** (progress@490 soon); rq_116 SWA deferred
- No research; no commit

### 2026-07-28T06:30:23Z - watcher cancelled
- User: pause the loop (watcher)
- Cancelled scheduler task **019fa293fb94** (every 1m DOGE tick)
- loop_state still **paused=yes** � ticks=488 � next on resume **rq_480**
- To resume: set paused=no + re-create 60s scheduler if desired


### 2026-07-28T19:12:35Z - resume
- User: **paused=no**
- 60s watcher recreated; fire_immediately first tick
- State: ticks=488 last_unit=rq_479; next **rq_480** (progress@490 soon)


### 2026-07-28T17:20:00Z - tick 489
- Unit: **rq_480** (FOI-adjacent hole-fill � **Rekenhof Vlaams kunstenbeleid CoA 2026_36: Kunstendecreet awards 201.9m 2024 + dual culture**)
- Found (strong primary CoA NL chamber 30 Jun 2026 + FR press):
  - **Kunstendecreet awards 2024: 201.942m** (Table3); outturn class **203.3m** (+Cultuurloket 1.6m + innov/Hefboom)
  - **WS 187.084m (92.7%)** / **KS 14.858m (7.3%)** � KS share below decretal 12.5% residual (actual 11.5%)
  - L4 split: KI 7�**69.401m** � 5y 209�**83.787m** � 10y 16�**30.224m** � kerntaken 4�**3.673m**
  - KS: beurzen 2.05m � projects 10.90m � intl 1.91m (850 of 1756 awards)
  - **Governance flag:** 9 orgs funded after **neg advice** (of 66 neg); avg **64%** of request; 6 named (4Hoog, Casco Phil, Huelgas, 't Ey, Toneelhuis, Z33)
  - Minister extra WS budget **25.3m** for 17 outside-budget + 9 neg overrides
  - Fin risk: **35/235 (14.9%)** severe vulnerability 2023; 10 score all 5 bad indicators
  - Stable core 73.7%; 60�85% awards concentrated Antwerpen/BHG/Gent
  - **Dual:** VL KD 201.9m 2024 vs BBT VEK 158m 2026 different perimeter/year; FWB arts vivants 104m
- Wrote: sources +3; budgets +21; cmt +3; lb +6; FOI **gap_vl_kunsten_neg9_cash** ready+draft; updated gap_culture_dual + gap_vl_cjsm notes; raw PDF; rq_480=done spawn **rq_481**; ticks=489
- FOI opened: gap_vl_kunsten_neg9_cash (ready, human send) � not sent
- Next: prio5 **rq_481** (**progress@490 next tick**); deferred **rq_116** SWA


### 2026-07-28T17:35:00Z - tick 490
- Unit: **rq_481** (**progress milestone @490** � coverage % layers A�E + waste top10 refresh)
- Coverage vs �347.956bn TE:
  - **A L0:** 100% � **B L1:** 100% � **C L2:** ~99% � **D L5:** ~29�42% generous � **E FOI ready:** ~239 (answered ~9; total ~250)
- Inventory class: budgets ~8505 � cmt ~882 � lb ~1653 � entities ~407 � sources ~908 � rq ~476
- **Gain 480?490:** Entity I/II consolidation dual wave (VL measures path � WAL 270m � BRU SEC � FWB SEC + quartet 2.65bn � FPB 263 options � CM Jul control residual **7.7bn** unalloc L5) + CoA VL Kunstendecreet **201.9m** + NL Democracy/Regie residual
- **Waste top10:** stable (fossil/company-cars/cheque/EIWT); hedera CAP stock filtered (annual 0); no reorder
- Wrote: progress_every_10_ticks.md � doge_waste_top10_current.md � rq_481=done spawn **rq_482**; ticks=490
- FOI: none new this tick
- Next: prio5 **rq_482**; deferred **rq_116** SWA


### 2026-07-28T17:50:00Z - tick 491
- Unit: **rq_482** (FOI-adjacent hole-fill � **CoA 2026_24 prison DBFM PPP follow-up + dual VL PPP decree**)
- Found (strong primary CoA AG 27 May 2026 + press 11 Jun):
  - **5 ops** DBFM (Marche Beveren Leuze Haren Dendermonde) + **4 project** (Antwerp mid-2026 � Leopoldsburg/Vresse 2029 � Verviers 2031) + 3 CPL DBFMO (Paifve Wavre Aalst)
  - Recs **9 applied / 16 ongoing / 5 not** (of 30); federal PPP legal frame still missing (WG Feb 2026); **VL decree 2019** dual
  - **Antwerp** annual invest redevance **�17.1m** 2026 expos�; **25y total missing**; Dendermonde invest fee **not fixed** (VAT residual)
  - **VFM** school example: DBFM NPV **254.5m** vs DBM **239.9m** at OLO30 **3.32%** = private finance premium **�14.7m**; residual-value bias flagged
  - **Off-balance** legal commitments **still unrecorded** (2022 stock **�2.6bn**); IWMS unfunded
  - Staff: GPP was 6.7 FTE; Justice PPP dir 6/7; facility managers VL+WAL filled BRU open
- Wrote: sources +3; budgets +6; cmt +3; lb +5; FOI **gap_dbfm_fees_full_table_2026** ready+draft; raw PDFs; rq_482=done spawn **rq_483**; ticks=491
- FOI opened: gap_dbfm_fees_full_table_2026 (ready, human send) � not sent
- Next: prio5 **rq_483**; deferred **rq_116** SWA


### 2026-07-28T18:10:00Z - tick 492
- Unit: **rq_483** (FOI-adjacent hole-fill � **CoA 2026_27 Flanders GIP MOW + dual SOFICO**)
- Found (strong primary Rekenhof NL 16 Jun 2026 + press):
  - **GIP 2025-27** annual avg **�2.503bn**; plan 2026 **2.424bn** ? available **3.864bn** ? **actualisatie 2026 �3.685bn** (VR 22 May)
  - Entity demand 2026 **�4.270bn** (avg 26-29 **3.122bn**); recurrent fixed **~�631m**/yr
  - Extra invest 2025: promised **530m** delivered **363m** (partly maintenance reclass)
  - **Fiets** actualisatie **~�220m** vs target **�300m**
  - Oosterweel extra **+�857m** � leefbaarheid **+�629.8m** � new projects **444.5m** � removed **316.4m** � non-input 43 proj **68.4m**
  - Pre-draws Q1 **>�900m**; governance: weak legal frame, non-objective prioritisation, data quality fail, 3y not 5y horizon
  - **Dual:** VL multi-mode GIP vs WAL SOFICO roads
- Wrote: sources +3; budgets +18; cmt +3; lb +5; FOI **gap_gip_l5_outturn_2025_26** ready+draft; raw PDFs; rq_483=done spawn **rq_484**; ticks=492
- FOI opened: gap_gip_l5_outturn_2025_26 (ready, human send) � not sent
- Next: prio5 **rq_484**; deferred **rq_116** SWA


### 2026-07-28T18:30:00Z - tick 493
- Unit: **rq_484** (FOI-adjacent hole-fill � **CoA 2026_33 FWB budget adjustment 2026 + dual Entity II**)
- Found (strong primary Cour des comptes FR chamber 30 Jun 2026):
  - **SEC aju �-1,752.8m** (init **-1,607.6m**, ? **-145.2m**)
  - Dep liquidations **�15,591.5m** (+184.7); rec hors emprunts **�13,674.4m** (+71.9); solde net **-1,917.1m**
  - Sous-utilisations **�452.1m**; corrections SEC **-238.1m** (�cureuil requal **-71.2m**)
  - **Economies SEC path strong Table3:** 2026 **253.6** � 2027 **522.9** � 2028 **599.1** � 2029 **733.0** m
    - Edu obl **87.5** � Enfance **118.0** � Sup **17.9** � Culture **12.6** � FP **8.7** � Autres **8.8** (2026)
  - Upgrades prior medium year-1 ~255m and elements-cl�s -1.608bn path
  - SWA coop **25 Mar 2026** still needs multi-parliament assent (links rq_116)
  - **Dual Entity II:** FWB deficit aju vs VL measures / WAL economies / BRU measures maps
- Wrote: sources +2; budgets +24; cmt +3; lb +4; FOI **gap_fwb_economies_programme_l5** ready+draft; raw PDF; rq_484=done spawn **rq_485**; ticks=493
- FOI opened: gap_fwb_economies_programme_l5 (ready, human send) � not sent
- Next: prio5 **rq_485**; deferred **rq_116** SWA


### 2026-07-28T18:50:00Z - tick 494
- Unit: **rq_485** (FOI-adjacent hole-fill � **CoA 2026_26 Wallonie budget adjustment 2026 + dual Entity II**)
- Found (strong primary Cour des comptes FR 11 Jun 2026):
  - **SEC aju �-2,015.4m** (init -2,015.7 almost flat); rec **22,087.9m** � dep liq **21,937.9m** (+602 each)
  - Solde net **-2,798.6m**; sous-util **524m**; corr SEC **963.3m**; inst consol **-180.1m** (Aviq **-258.9**; OTW **+97.1**)
  - **ICN 2025 provisional �-2,853m** (-572.4m vs gov aju estimate)
  - **Debt direct:** 20.6bn (2021) ? **30.7bn** eoy2025 (+49%) ? path **33.0bn** eoy2026; gross consol path **43.8bn**; interest **753.7m**
  - Financing needs **3.92bn**; raised **3.42bn** + EIB **200m** (May); Moody's **A3?Baa1** Apr 2026
  - **Opacity:** standardized spend fiches denied to CoA (confidential claim)
  - **Dual:** WAL SEC -2.02bn vs FWB -1.75bn aju; SWA coop 25 Mar still pending assent
- Wrote: sources +2; budgets +23; cmt +3; lb +5; FOI **gap_wal_fiches_budget_2026** ready+draft; raw PDF; rq_485=done spawn **rq_486**; ticks=494
- FOI opened: gap_wal_fiches_budget_2026 (ready, human send) � not sent
- Next: prio5 **rq_486**; deferred **rq_116** SWA


### 2026-07-28T19:10:00Z - tick 495
- Unit: **rq_486** (FOI-adjacent hole-fill � **CoA 2026_23 DG 1. Haushaltsanpassung 2026 + dual Entity II**)
- Found (strong primary Rechnungshof AG 27 May 2026):
  - **HV AE �750.8m** � VE **�728.0m** � rec **�672.6m** (+17.3)
  - **ESVG consol �-123.8m** (ex-Gemeinschaftszentren **�-110.5m**); gross saldo worse **�36.7m** aju; ESVG worse **�2.6m**
  - Deltas: RRF rec **+16.6** / exp **+21.0** � infra VE **+19.4** � Gemeinden **+3.3** � personnel **+1.8** � fed dot **-4.0**
  - **Debt consol:** 578m (2020) ? **1,252m** (2024) ? **1,344m** (2025) ? path **1,468m** eoy2026; interest **41.2m**; debt/rev **257%**
  - **NPA growth 2026 +8.98%** breaches 5% self-cap; invest neutralisation **�291.3m** 2026-28 without EU flex approval
  - Macro params diverge FPB (growth 0.2% / inflation 3.2% 2026)
  - **Dual Entity II:** DG -0.11bn completes map vs FWB -1.75 / WAL -2.02 / VL measures 1.83 class
- Wrote: sources +2; budgets +19; cmt +3; lb +5; FOI **gap_dg_infra_l5_2026** ready+draft; raw PDF; rq_486=done spawn **rq_487**; ticks=495
- FOI opened: gap_dg_infra_l5_2026 (ready, human send) � not sent
- Next: prio5 **rq_487**; deferred **rq_116** SWA


### 2026-07-28T19:30:00Z - tick 496
- Unit: **rq_487** (FOI-adjacent hole-fill � **CoA 2026_31 FWB Cepage teacher payroll IT + dual Persona/I-Police**)
- Found (strong primary Cour des comptes FR 16 Jun 2026):
  - Education **personnel �7.1bn** BI2026 (86.2% Education); **~150k** agents � **2,700+** schools � **1,000+** POs
  - **Cepage** (2022?deploy not before **2030**): cost estimates **�35.2m** build / **�39.1m** 5y / **�95.7m** 14y � **unsubstantiated**; maint **�3.9m**/yr
  - **Etnic** dot **�119.7m** (2025) / **�117.7m**+**5.3m** strategic (2026); FTE **68?381** (2002�24); analytic costs weak since 2004 contract
  - RL10 payroll engine **1970s Cobol**; free PO payroll art.36 pacte scolaire unsustainability risk
  - **Dual IT failures:** VL AGODI **Persona �16m** stopped (<10% features); federal **I-Police �76.7/299m** cancelled
- Wrote: sources +3; budgets +12; cmt +3; lb +4; FOI **gap_fwb_cepage_cost_l5** ready+draft; raw PDFs; rq_487=done spawn **rq_488**; ticks=496
- FOI opened: gap_fwb_cepage_cost_l5 (ready, human send) � not sent
- Next: prio5 **rq_488**; deferred **rq_116** SWA


### 2026-07-28T19:50:00Z - tick 497
- Unit: **rq_488** (FOI-adjacent hole-fill � **VL Onderwijs BO2026 17.25bn + Persona 16m dual FWB Cepage**)
- Found (strong primary Vlaams Parlement Commissie Onderwijs 15-2025-26-7H + CoA 2026_31):
  - **OV VAK �17.25bn / VEK �17.24bn** (+404.5m / +436.7m vs 2025)
  - Coalition savings **�141m** + extra BO **�180.6m** class: SO growth **50** � LBV **33.3** � VO **50** � subs **4.7** � Digisprong **6** � defer inductie **10** / NL **35**
  - Extra invest class **�412m** (digi **154** � NL **80+10** � inductie **~39** � zijinstroom **14** � tso/bso **18**)
  - HO cuts: Brussel **10.6** � niet-EER **~20.2** � werkingsmiddelen **-10.3**; leraar-specialist **15.7m** back to provisie
  - **Persona** AGODI IT stop Jan 2026 after **�16m** / **<10%** features (CoA dual Cepage)
  - **Dual:** VL 17.25bn OV vs FWB edu personnel 7.1bn + IT failure pair Persona/Cepage
- Wrote: sources +3; budgets +26; cmt +3; lb +4; entity agodi; FOI **gap_vl_persona_agodi_cash** ready+draft; rq_488=done spawn **rq_489**; ticks=497
- FOI opened: gap_vl_persona_agodi_cash (ready, human send) � not sent
- Next: prio5 **rq_489**; deferred **rq_116** SWA


### 2026-07-28T20:10:00Z - tick 498
- Unit: **rq_489** (FOI-adjacent hole-fill � **CoA 2026_35 VL aanvangsbegeleiding + inductie + dual FWB teachers**)
- Found (strong primary Rekenhof NL 30 Jun 2026):
  - **AVB budget path:** ~**�31m** (2019) ? **�52.2m** (2024-25); pupil-based allocation mismatches starter needs
  - **Inductie** SY2026-27 envelope **�48.7m** (not enough for 20% free-time all starters); SY2025-26 alt **�38.7m** werkingsbudget
  - Total AVB+inductie **>�100m** class (~3� introduction) excl **lerarenbonus �24.7m** / **3,499** teachers
  - Professionalisering: **�120�130**/organieke betrekking; large school disparities; ~1/3 spend off core teaching task
  - No closed AGODI control that coloured hours actually fund starter mentoring
  - **Dual:** VL starter cash package vs FWB Cepage/payroll under **�7.1bn** personnel
- Wrote: sources +3; budgets +12; cmt +3; lb +5; FOI **gap_vl_avb_inductie_spend_l5** ready+draft; raw PDFs; rq_489=done spawn **rq_490**; ticks=498
- FOI opened: gap_vl_avb_inductie_spend_l5 (ready, human send) � not sent
- Next: prio5 **rq_490** (**progress@500 next ticks**); deferred **rq_116** SWA


### 2026-07-28T20:30:00Z - tick 499
- Unit: **rq_490** (FOI-adjacent hole-fill — **CoA 2026_32 VL Rekeningenrapport 2025 + dual Entity II**)
- Found (strong primary Rekenhof NL 30 Jun 2026 + press + addendum):
  - **ESR vorderingensaldo 2025 −3.982,4m** (vs −4.101,3m 2024; BA −4.503,8m; +522m vs BA)
  - **Maastrichtschuld 50.171,9m** eoy2025 (from 41.788,6m; **+8.383,3m**); gross consol **58.721,9m**; direct **42.396,6m**
  - Debt 2019→2025: **18,6 → 50,2bn (+170%)** — far exceeds cumulative deficits
  - **PMV/Zaventem BAC kapitaalsverhoging 2.553,6m** (post-BA amendement); CoA debt impact class **~2,7bn**
  - Lantis debt **2.401,3m** (+1.166,5); loans 2025 **1.128m**; Toekomstverbond cum **3.851,6m**
  - VWF **6.062,8m** · VMSW **3.123,4m** · centraal gefinancierd **17.464,2m**
  - **Niet-budgettaire schuldopbouw 1.069,7m** 2025 — Parlement onvoldoende uitleg (CoA)
  - Balans: onthouding; ontbrekende terreinen/gebouwen **~1,6bn**; kunst **1,4bn** deels; openstaande verbintenissen FWO **561,6** + FIO **188,6** ≈ **0,75bn** voorbehoud
  - Overdracht kredieten naar 2026 **1.415,3m**; Relance 2025 spend **399,4m** (−342,2); cum 4,2bn vast / 3,5bn liq / 0,7bn open
  - **Dual Entity II:** VL certified −4,0bn outturn vs WAL aju −2,02 / FWB −1,75 / DG −0,11
- Wrote: sources +4; budgets +28; cmt +5; lb +7; FOI **gap_vl_debt_nonbudget_bridge_l5** ready+draft; raw PDFs; rq_490=done spawn **rq_491**; ticks=499
- FOI opened: gap_vl_debt_nonbudget_bridge_l5 (ready, human send) — not sent
- Next: prio5 **rq_491** (**progress@500 next tick**); deferred **rq_116** SWA

### 2026-07-28T20:50:00Z - tick 500
- Unit: **rq_491** (progress milestone @500 — coverage % + waste top10; no invent euros)
- Found / inventory:
  - Layers: **A100** · **B100** · **C~99** · **D~30–43%** · **E~248 ready** / ~9 answered / ~259 FOI rows
  - CSV class: budgets ~8685 · cmt ~914 · lb ~1697 · entities ~411 · sources ~936 · rq ~486
  - **Gain 490→500:** CoA dual Entity II aju complete (FWB −1.75 · WAL −2.02 · DG −0.11) · GIP 3.685bn · prison DBFM · education dual (Cepage 35–96m · Persona 16m · OV 17.25bn · AVB+inductie >100m) · VL RR ESR −3.98bn / debt 50.2bn (+8.4) / Zaventem 2.55bn
  - Waste top10 **stable** (fossil/company-cars/cheque/EIWT); no reorder; new near-list: VL debt stock 50.2bn · Zaventem 2.55bn · nonbudget 1.07bn · dual education IT
- Wrote: progress_every_10_ticks.md · doge_waste_top10_current.md · rq_491=done spawn **rq_492**; ticks=500
- FOI: none new (progress tick)
- Next: prio5 **rq_492**; deferred **rq_116** SWA

### 2026-07-28T21:10:00Z - tick 501
- Unit: **rq_492** (FOI-adjacent hole-fill — **CoA 2026_19 DWV studieopdrachten + dual Lantis/GIP**)
- Found (strong primary Rekenhof NL 31 Mar 2026 + press):
  - Four long study contracts (still running); **3/4** major award overruns; **all 4** delayed
  - **R0 Noord:** award **€36m** → spent Mar2025 **€85.4m** → est **€103.6m**; OP-posten **€9.4m** without competition
  - **R0 Oost:** **€3.5m**/yr award → spent **€11.1m**; extra **€3.7m** same provider quick wins 2023 unpublished
  - **Brabantnet:** award **€5.9m** → spent **€11.0m** + extras **€8.75m** (ring 0.1 · luchthaven 5.1 · sneltram 3.6); sneltram off GIP 2025-27
  - **R4 West/Oost:** award **€12.1m** **+>40%**; deel4 budget **4.3→9.2m** undermines plafond
  - Four-pack spent class **~€125m** Mar2025; competition/transparency risks CoA
  - **Dual:** DWV study cash vs Lantis Toekomstverbond **€3.85bn** / GIP mobility stack
- Wrote: sources +3; budgets +16; cmt +4; lb +6; FOI **gap_dwv_studies_contractor_l5** ready+draft; raw PDFs; rq_492=done spawn **rq_493**; ticks=501
- FOI opened: gap_dwv_studies_contractor_l5 (ready, human send) — not sent
- Next: prio5 **rq_493**; deferred **rq_116** SWA

### 2026-07-28T21:30:00Z - tick 502
- Unit: **rq_493** (FOI-adjacent hole-fill — **CoA 2026_18 Toekomstverbond 6e voortgang + dual DWV**)
- Found (strong primary Rekenhof NL 24 Mar 2026):
  - **Oosterweel exec budget €10.055bn** (Jan2024) from task **€4.391bn** (2019) → **€5.369bn** (2022); inflation **€1.5bn** 2019-23
  - Adds: invest **299** · overmacht/PFAS **1.861** · LBH2 under **655** · risk **607**
  - **BC2026:** assets end-build **€13.614bn** · fin need **€8.273bn** · CAPEX remain **€7.275bn** · bonds **€7.751bn** · subloans **€2.850bn** · **interest €24.495bn** 2026-2083
  - Spent eoy2025: main **€2.674bn** · PFAS **€476.9m**; Linkeroever main within budget
  - **Table1 TV clusters:** main **7.917** · overmacht **2.258** · leefbaarheid **1.696** · Haventracé **4.1–15.9bn** · modal shift opaque
  - VL debt path MJR **41.7→74.6bn** 2024-30; GIP vs Lantis multiyear unreconciled
  - **Dual:** TV mega-envelope vs DWV study overruns **~€125m** (tick501)
- Wrote: sources +2; budgets +23; cmt +4; lb +7; FOI **gap_tv_oosterweel_finance_l5** ready+draft; raw PDF; rq_493=done spawn **rq_494**; ticks=502
- FOI opened: gap_tv_oosterweel_finance_l5 (ready, human send) — not sent
- Next: prio5 **rq_494**; deferred **rq_116** SWA

### 2026-07-28T21:50:00Z - tick 503
- Unit: **rq_494** (FOI-adjacent hole-fill — **CoA 2026_22 federal budget aju 2026 Entity I + dual E2**)
- Found (strong primary Rekenhof AG 21 May 2026):
  - **Entity I deficit €24.5bn** aju (init €24.6bn); MR 3 Apr **+€615m** (tech 517 + policy 98)
  - Primary **€12.2→18.7bn** 2026-29; interest **€12.3→17.5bn**; VAT takeaway cancel **€475m**
  - Defence 2025-29 **€17.336bn** (+552.8 NATO 2%); higher def **€4.804bn** / asset optim **€3.17bn** not booked 2026 conclaves; Belfius 20% **€2bn** ~2027
  - Russian assets CIT path **€6.154bn** 2025-29; Euroclear exceptional **>€1bn**/yr assumption to 2031
  - Fiscal fraud claim **€300/600m** method opaque; SIOD social fraud **€414.6m** 2025
  - Centenindex E1 **€24→363m**; energy policy **~€2.6bn** (DG 1.2 + funds 1.4 CREG/Elia/NIRAS/Hedera)
  - Regions EU MFK **€500m**/yr from 2028 no deal; personnel-save drag FOD Fin **€433m** by 2029
  - **Dual:** E1 24.5bn vs VL RR −4.0 / WAL −2.02 / FWB −1.75 / DG −0.11
- Wrote: sources +2; budgets +24; cmt +4; lb +7; FOI **gap_fed_energy_funds_l5** ready+draft; raw PDF; rq_494=done spawn **rq_495**; ticks=503
- FOI opened: gap_fed_energy_funds_l5 (ready, human send) — not sent
- Next: prio5 **rq_495**; deferred **rq_116** SWA

### 2026-07-28T22:10:00Z - tick 504
- Unit: **rq_495** (FOI-adjacent hole-fill — **CoA 2026_04 Kustbeveiliging MPKV + Kustvisie dual GIP**)
- Found (strong primary Rekenhof NL 13 Jan 2026 + press):
  - **Masterplan Kustveiligheid:** spent end-2024 **€321.4m** · remain min **€144.3m** · total class **€465.7m**
  - Original end **2015**; Dec2025 still **4/15** measures open (priority Ostend + Nieuwpoort/Blankenberge marinas); MDK est end **2029**
  - Coast still not 1/1000-yr storm protected; weak links under-prioritised
  - **Kustvisie** (since 2009): studies/consulting **€21m** 2014-24; strategic plan draft 2024 **not approved**; not in GIP as programme
  - Century protection cost **€2–5bn** PV (2030-2130)
  - Governance: fragmented fed/VL/local; no legal safety norms; ad hoc structures
  - **Dual:** near-term MPKV vs GIP climate/infra opacity + long-term 2-5bn envelope
- Wrote: sources +3; budgets +8; cmt +3; lb +6; entity mdk; FOI **gap_mpkv_measures_l5** ready+draft; raw PDFs; rq_495=done spawn **rq_496**; ticks=504
- FOI opened: gap_mpkv_measures_l5 (ready, human send) — not sent
- Next: prio5 **rq_496**; deferred **rq_116** SWA

### 2026-07-28T22:30:00Z - tick 505
- Unit: **rq_496** (FOI-adjacent hole-fill — **CoA 2026_29 KMO VenB control follow-up + dual fraud**)
- Found (strong primary Rekenhof AG 3 Jun 2026 + press):
  - VenB cash **€25.729bn** 2024; PB **56.1** · BTW **37.5** · RV **14.5** · accijnzen **7.6** (CoA general account figure)
  - **111,988** VenB returns controlled 2024 → income increases **>€5.6bn**
  - Admin KMO staff gap **383 FTE** vs 2018 plan eoy2024; prior −21% controllers 2016-21
  - Recommendations of 17: **3 done · 8 in progress · 2 not done · 4 N/A** after 3 years
  - **BasketFisc** harmonises within language area; residual inequality cross-language/Brussels
  - No general **fiscal discipline** metric; control vs settlement functions still not separated
  - **Dual:** realized control uplifts 5.6bn vs fed aju fraud yield claims **300/600m** opaque (tick503)
- Wrote: sources +3; budgets +8; cmt +2; lb +5; FOI **gap_kmo_venb_control_l5** ready+draft; raw PDFs; rq_496=done spawn **rq_497**; ticks=505
- FOI opened: gap_kmo_venb_control_l5 (ready, human send) — not sent
- Next: prio5 **rq_497**; deferred **rq_116** SWA

### 2026-07-28T22:50:00Z - tick 506
- Unit: **rq_497** (FOI-adjacent hole-fill — **CoA 2026_20 BBI bank data + dual KMO/fraud**)
- Found (strong primary Rekenhof AG 18 Mar 2026 + press/samenvatting):
  - Bank investigation authorizations **~700** in 2024 (mostly 5th dir VAT carousels/Brazilian networks + Brussels domicile)
  - Dossiers with bank investigations 2015-24: taxes **assessed €2.3bn** · **collected only €36m** (~1.6%) — preventive focus ~80% of corrections via 5th dir
  - CAP incomplete (foreign self-report; neo-banks/vIBAN/crypto); datamining allowed since law **18 Dec 2025**
  - Procedure errors **~10%** sample (income tax); IB/BTW rules not aligned for polyvalent cases
  - Legal annual evaluation of bank-data use **not done since 2018**; KPI 10% dossiers bank probe = indicative only
  - **Dual:** BBI assess/collect stack vs KMO VenB **€5.6bn** uplifts (tick505) vs fraud yield claims **€300/600m** (tick503)
- Wrote: sources +3; budgets +5; cmt +2; lb +5; entity aabbi; FOI **gap_bbi_bank_collection_l5** ready+draft; raw PDFs; rq_497=done spawn **rq_498**; ticks=506
- FOI opened: gap_bbi_bank_collection_l5 (ready, human send) — not sent
- Next: prio5 **rq_498**; deferred **rq_116** SWA

### 2026-07-28T23:10:00Z - tick 507
- Unit: **rq_498** (FOI-adjacent hole-fill — **CoA 2026_22 residual Justice/Fedasil/Defence L5 dual**)
- Found (strong primary same CoA fed aju, deeper L5 extract):
  - **Justice** section **€2,925m** aju (+81m); prison overcrowding infra **€259m** (159+100) for **1,300** places by 2029; short **€50m**/yr; efficiency **€44m**; security+return ID **€546m**
  - **MasterPlan IIIbis** **€80m** ex inflation (Antwerp open Sep2026, St-Gilles, Hoogstraten, Bergen psych, Verviers)
  - **Fedasil** total **€848.2m** BC (dot 743.9 + ID 104.3); asylum save target **−172m** vs plan **−110.8m** (gap **61.2**); cap 34,564→~30,000; path targets 172/303/452/538
  - Return save **€75m** hard to track; POD MI medical **100.3m** (−12 vs IB)
  - **NATO** effort target **€13,296m** (2% GDP 664.8bn); defence budget **10,958**; internal security **€177m** (+trust 45→222 class) classification opacity
  - **Dual:** prison capacity + Fedasil cap cut + defence internal security stack
- Wrote: sources +2; budgets +20; cmt +4; lb +7; FOI **gap_fedasil_save_measures_l5** ready+draft; rq_498=done spawn **rq_499**; ticks=507
- FOI opened: gap_fedasil_save_measures_l5 (ready, human send) — not sent
- Next: prio5 **rq_499** (progress@510 soon); deferred **rq_116** SWA

### 2026-07-28T23:30:00Z - tick 508
- Unit: **rq_499** (FOI-adjacent hole-fill — **CoA 2026_22 residual SS macro + POD MI soft saves dual**)
- Found (strong primary same CoA fed aju, SS/POD MI deep extract):
  - **SS BC2026:** rec **€148,002m** · exp **€148,027m** near balance; contributions **85,328** · altfin **27,583** · benefits **137,624**
  - Healthcare **€43,857m** (+2.56bn vs IB); unemployment **4,836** (+198.5); employee pens **43,037**; invalidity **14,839**; public pens **22,527**
  - RSZ contrib **69,475m**; federal reductions class **€5.14bn** (struct 4.29 + targeted 0.85; workbonus 1.83); wage ceiling **58.2m**
  - RSZ gov dots **8,656m**; equilibrium overfinance 2025 **547.5m** → GB deficit booking 2026
  - **POD MI OCMW** total **€2,309m** (RMI 2,133 + wet65 176); integ+wait save BC **13.1m** (was 40.2) — **CoA: will not be achieved 2026**
  - RIZIV savings miss **€183.1m** of 801.4 (145.7 drugs); invalidity follow-up save slip **−110.2m** (exclusions 4,197)
  - Pension reform path **€2,212m** to 2030; Zuidertoren **177.7m** RSZ reserves
  - **Dual:** SS 148bn macro + POD MI soft saves
- Wrote: sources +2; budgets +28; cmt +4; lb +8; FOI **gap_podmi_ss_save_slip_l5** ready+draft; rq_499=done spawn **rq_500**; ticks=508
- FOI opened: gap_podmi_ss_save_slip_l5 (ready, human send) — not sent
- Next: prio5 **rq_500** (**progress@510 next tick**); deferred **rq_116** SWA

### 2026-07-28T23:45:00Z - tick 509
- Unit: **rq_500** (FOI-adjacent hole-fill � **CoA 2026_22 residual Werk/werkloosheid + invalidity multi-year dual leefloon**)
- Found (strong primary same CoA fed aju, deeper L5 extract):
  - **Unemp BC2026** **�4,836.4m** (+198.5 vs IB): volume **+287** � other **-96.7** � index **+8.2**; full unemp **+17,473** temporary **-3,851**; rate 9.6 vs 9.1
  - **Reform path** duration+degressivity: **1,685.2 / 2,286.7 / 2,440.6 / 2,447.8** m 2026-29; measures net total **1,578.5?2,421.2**
  - **Exclusion waves** total **193,904** (BRU 41,709 � VL 62,676 � WAL 88,566 � DG 953); Q1 actual **45,592** (93.4% of est)
  - **Leefloon shift** Q1: **17,606** new = **31.9%** of excluded (WAL 37.2 � VL 23.5 � BRU 27.5)
  - **Litigation** 3,696 dossiers 30 Apr (avg prior 3,185/yr); CoA est extra legal **~�3m**; not in BC; GH pending
  - **SWT** close: stock **�166.8m**/8,502 bens 2025; 2026 rush **-5.2m** (CoA: not visible in stats); 2029 save **64.8m**
  - **Family credit** backpack Entity I **�40m** 2026 (full-yr 50); law not set; **tijdskrediet EL** save 1.6m (was 9.2)
  - **Invalidity multi-year**: follow-up slip **-110.2** 2026; cumul miss **-333.6** to 2029; solidarity **98.4m**; responsabilisering **137m** (doctors 50 law incomplete); unemp?ZIV est **+44.1m**
  - **Dual:** reform save path 1.69bn vs leefloon OCMW displacement 32%
- Wrote: sources +2; budgets +31; cmt +4; lb +8; FOI **gap_rva_unemp_leefloon_l5** ready+draft; rq_500=done spawn **rq_501**; ticks=509
- FOI opened: gap_rva_unemp_leefloon_l5 (ready, human send) � not sent
- Next: prio5 **rq_501** (**progress@510 next tick**); deferred **rq_116** SWA

### 2026-07-29T00:05:00Z - tick 510
- Unit: **rq_501** (progress milestone @510 � coverage % + waste top10; no invent euros)
- Found / inventory:
  - Layers: **A100** � **B100** � **C~99** � **D~31�44%** � **E~257 ready** / ~9 answered / ~268 FOI rows
  - CSV class: budgets ~8848 � cmt ~945 � lb ~1756 � entities ~412 � sources ~958 � rq ~497
  - **Gain 500?510:** CoA mobility dual (DWV ~125m � Oosterweel 10.1bn / interest 24.5bn) � E1 aju 24.5bn � energy ~2.6bn � MPKV 466m/Kustvisie 21m � KMO VenB >5.6bn � BBI 2.3bn/36m � SS 148bn � unemp reform 1.69bn dual leefloon 32% � invalidity miss 334m
  - Waste top10 **stable** (fossil/company-cars/cheque/EIWT); #2/#3 annual tie-break may flip fossil accises vs company-cars FPB; new near-list: unemp reform 1.69bn � BBI collect gap � Oosterweel mega � SS 148bn
- Wrote: progress_every_10_ticks.md � doge_waste_top10_current.md � rq_501=done spawn **rq_502**; ticks=510
- FOI: none new (progress tick)
- Next: prio5 **rq_502**; deferred **rq_116** SWA

### 2026-07-29T00:20:00Z - tick 511
- Unit: **rq_502** (FOI-adjacent hole-fill � **CoA 2026_22 residual energy L5 deep + federal debt path dual**)
- Found (strong primary same CoA fed aju, energy/debt extract):
  - **Energy total ~�2.6bn**: DG Energie **1.2bn** + assignment funds CREG/Elia/NIRAS/Hedera **1.4bn** (opacity CoA)
  - **Energienorm** **�249m** (law 24 Apr 2026) + **Fluxys �100m**/yr 2026-28
  - **Social tariff** CREG **�168.6m**; temp support **�20m** (7.5/7.5/5)
  - **Phoenix CfD** **�583.6m** 2026; strike price unknown to CoA at close; NIRAS passiva **258.6+62.5m**; decom contrib **�100m** (ends 2027)
  - **Fed debt** eoy2026 **�577.5bn** (+5.6 vs IB; +31.4 vs 2025) path **�731bn** 2031
  - **Interest** **�12.3bn** BC2026 path **�22.6bn** 2031; snowball r-g **-0.91?-0.06** 2026-31
  - **Cash receipts** **�167.2bn** (fiscal 159.3 � nonfiscal 7.8); transfers out **94.5**; middelen **72.6**; ESR fiscal **164.5**; measures net **+1.83bn**
  - Pillar2 **-87m** (slip -119); VAT reform **177m** (was 580); Russian assets VenB **1.016bn**; VVPR-bis **402m**
  - **Dual:** energy assignment opacity vs debt interest path
- Wrote: sources +2; budgets +28; cmt +4; lb +8; FOI **gap_phoenix_cfd_strike_l5** ready+draft; rq_502=done spawn **rq_503**; ticks=511
- FOI opened: gap_phoenix_cfd_strike_l5 (ready, human send) � not sent
- Next: prio5 **rq_503**; deferred **rq_116** SWA

### 2026-07-29T00:40:00Z - tick 512
- Unit: **rq_503** (FOI-adjacent hole-fill � **CoA 2026_22 residual new fiscal measures + nonfiscal + primary exp cells dual**)
- Found (strong primary same CoA fed aju, Deel II residual):
  - **Conclave new fiscal +�730.9m**: customs e-comm **+400.7** � EU handling fee **+77.4** (unallocated; law not final) � VVPR-bis re-est **+334.5** (Jan�Apr +406.3 vs 2025; future reverse risk)
  - Customs mechanics: gross +449 dual EU -449; MS retention 25% **+112.3** nonfiscal; VAT volume **-48**
  - Insurance tax **+36.4** (was 51); non-res opcentiemen **~�78m**/yr CJEU C-119/24 illegal; refunds open
  - Post-conclave: employer km credit **20m/month** May�Jul (FPS no data; VAT-neutral claim disputed); service km provis **�5m**
  - **Nonfiscal** middelen **�7.829bn** (+1358): RSZ eq refund **548** � RIZIV COVID **187** � CREG energy **285** (max 412) � customs fee **1013.8** (+229) � SFPIM div actual **78.4** vs booked 55.8 � plates delay **-42.2**
  - **Primary cells** **�92.050bn** (+41): support 3.72 (-497) � authority 23.05 (+390) � economic 6.58 � social 34.61 � specific 24.09
  - **Dual:** conclave pack + nonfiscal one-offs vs debt interest path
- Wrote: sources +2; budgets +27; cmt +4; lb +8; FOI **gap_customs_vvpr_opcent_l5** ready+draft; rq_503=done spawn **rq_504**; ticks=512
- FOI opened: gap_customs_vvpr_opcent_l5 (ready, human send) � not sent
- Next: prio5 **rq_504**; deferred **rq_116** SWA

### 2026-07-29T01:00:00Z - tick 513
- Unit: **rq_504** (FOI-adjacent hole-fill � **CoA 2026_22 residual defence multi-year financing + Fedasil save L5 dual**)
- Found (strong primary same CoA fed aju, �3.2.2 + �2.2�2.3 residual):
  - **Defence 2025-29** **�17,335.8m** (+552.8 NATO 2pct via GDP); higher deficit **�4,804m** of which asset optim **�3,170m** (40/30/20/10 ? 1268/951/634/317) **unbooked** in 2026 conclaves
  - **Russian assets CIT** 2025 **1,148** (was 1,208); 2026-29 **1,016**/yr; path shortfall **-942m** vs initial 6,154; residual **735m** 2027-29 unaddressed
  - **Belfius 20%** sale est **�2bn** ~2027 (ECB/NBB/FSMA); residual asset optim after Belfius **�1,170m** unexplained
  - **NATO effort** target **�13,296m** / fill **�13,246m** (def budget **10,958** + external **2,288**; pens **1,988** FPD -40 risk)
  - **Fedasil asylum save**: target **-172** path -303/-452/-538; plan only **-110.8** (cap25 36.4 � cap26 35.3 � extra 39.1); **gap 61.2** 2026 / 187 2029
  - Extra 23 measures: internal **27.1** � core tasks **10.4** � procedure **1.6** (from 2027 extra **220.7**); return **-75** untracked
  - **SIOD** social fraud **�414.6m** 2025 (-20.3); fiscal fraud claim **300/600** method opaque; financial parket **196m** 2029 bill 56 1536
  - E1 deficit path **24.5?36.2bn** 2026-29; Euroclear **>1bn**/yr to 2031 assumption; FOD Fin drag **433m** by 2029
  - **Dual:** defence soft financing + Fedasil soft saves
- Wrote: sources +2; budgets +32; cmt +4; lb +8; FOI **gap_defence_asset_optim_l5** ready+draft; rq_504=done spawn **rq_505**; ticks=513
- FOI opened: gap_defence_asset_optim_l5 (ready, human send) � not sent
- Next: prio5 **rq_505**; deferred **rq_116** SWA

### 2026-07-29T01:20:00Z - tick 514
- Unit: **rq_505** (FOI-adjacent hole-fill � **CoA federal consultancy audit Oct 2025 dual IT/Smals**)
- Found (strong primary Rekenhof AG 22 Oct 2025, PDF local):
  - **Total consultancy 2020-22: �2,524.7m** incl VAT (101 orgs survey); **IT �2,032.3m (81%)** � non-IT **�492.4m (19%)**
  - In-house federal-to-federal **�619.2m** � other contracts **~�1.9bn**; no central inventory (BOSA partial excl IT)
  - **Top buyers:** NMBS **465.1** � Infrabel **318.5** � FOD Fin **185.3** � BOSA **134.2** (45% of purchases!) � NIRAS **129.1** � Smals buyer **126.1** (79%) � RIZIV **115.5** � Health **70.1** � Kanselarij **68.2** � Credendo **61.5**
  - Nuclear non-IT **�215.2m** (44% of non-IT); strategy/mgmt **87.2** � construction **72**
  - Smals external share of turnover **17.8% (2014) ? 36% (2024)**; detachments **1,395 ? 2,072** (+48.5%)
  - 101 contracts sample **�2.2bn**; ~30% lack knowledge-transfer clause; deficiencies high in sample
  - Openbaarheid art 3/3 inventory still needs KB; dual Persona/Cepage/I-Police IT failures
- Wrote: sources +2; budgets +25; cmt +4; lb +8; FOI **gap_fed_consultancy_inventory_l5** ready+draft; rq_505=done spawn **rq_506**; ticks=514
- FOI opened: gap_fed_consultancy_inventory_l5 (ready, human send) � not sent
- Next: prio5 **rq_506**; deferred **rq_116** SWA

### 2026-07-29T01:40:00Z - tick 515
- Unit: **rq_506** (FOI-adjacent hole-fill � **CoA Brussels Region budget 2026 dual Entity II**)
- Found (strong primary Rekenhof AG 13 Mar 2026; 5 working days only):
  - **SEC SF** gov **-�956.6m** (+591 vs prov 2025); CoA content adj **-�978.2m**; base 2025 **-1,241m**
  - Measures path **�297m (2026) ? �1,186m (2029)**; receipt L5 missing; finops max **�1bn** (SLRB 400 � Vivaqua 180 � Confex 150 � Kanal 60)
  - **Exp:** eng **�8.9bn** � liq **�8.0bn**; SGRBC net finance **-�1,746.4m**; gross surplus **+�11.4m**
  - **Debt consol** eoy2025 **�16.1bn** (+3.5 2023-25); CoA est eoy2026 **�17.7bn**; path limit +3bn ? **>�19.1bn** 2029; direct LT **�13.4bn**
  - **Top lines:** STIB **�1,167.6m** (PPI cut **�964.6m** 2026-29) � Actiris **�648.1m** (-78) � titres-services **�303.8m** � SLRB eng **687** � Propret� **411** � local powers **758** � commissions **692** � debt service **728** � roads liq **264**
  - **Kanal** foundation budget omitted OAA2; credits **�86.7m** (60m finops)
  - HRF net primary exp **-0.22%/yr** avg (2026 **-0.61%**); dual Entity II peers
- Wrote: sources +2; budgets +29; cmt +4; lb +8; FOI **gap_bru_measures_stib_kanal_l5** ready+draft; rq_506=done spawn **rq_507**; ticks=515
- FOI opened: gap_bru_measures_stib_kanal_l5 (ready, human send) � not sent
- Next: prio5 **rq_507**; deferred **rq_116** SWA

### 2026-07-29T02:00:00Z - tick 516
- Unit: **rq_507** (FOI-adjacent hole-fill � **CoA FAM medical accidents fund follow-up 2025 dual RIZIV**)
- Found (strong primary Rekenhof AG 19 Nov 2025):
  - **Recommendations:** 24 total ? **11 done � 12 in progress � 1 not done**
  - **Backlog:** open **2,445 (eoy2019) ? 1,066 (2023) ? 989 (2024)**; task force 1,249 treated (83% closed with opinion)
  - **Speed:** p80 months **31.6 (opened 2019) ? 13.2 (opened 2022)**; new openings **632** in 2024
  - **Indemnities:** cumul **�16.3m (2018) ? �101.1m (eoy2024)**; annual **�6.4m (2018) ? �12.4m (2023)**
  - **Ops cost excl indemnities:** **�12.5m 2024** (590 opinions � 681 closed); crude **~�16,500/dossier** (was ~12k/open in 2020 audit)
  - Staff cadre **62**; legal recovery costs rising; prevention mission still weak
  - Law reform WG list due **31 Dec 2026** / results **28 Feb 2027**; coalition 2025-29 optimisation
  - Historic: **~9/10 victims** avoid procedure (slow + low indemn probability)
  - **Dual:** FAM residual under RIZIV healthcare mega-stack
- Wrote: sources +2; entity fam; budgets +7; cmt +3; lb +6; FOI **gap_fam_cost_role_l5** ready+draft; rq_507=done spawn **rq_508**; ticks=516
- FOI opened: gap_fam_cost_role_l5 (ready, human send) � not sent
- Next: prio5 **rq_508** (progress@520 soon); deferred **rq_116** SWA

### 2026-07-29T02:20:00Z - tick 517
- Unit: **rq_508** (FOI-adjacent hole-fill � **CoA consultancy residual Smals broker L5 dual IT detach**)
- Found (strong primary same CoA consultancy Oct 2025, Ch5 residual):
  - **Broker framework** ProUnity lot1 est **�1.8bn** (15 Dec 2022) + lot2 fixed-price **�250m** = **�2.05bn** class
  - **Orders 2023-24:** **�471.4m** under broker framework; 2022 direct **�20.9m** non-broker + **�47m** on broker
  - **Day rates** (incl VAT, orders 2023�Jan2025): junior avg **�672** � senior **�759** � expert **�923** (max **�2,128**)
  - **Detach vs external hourly:** programmer **65.71 vs 111.43** � analyst **93.62 vs 126.30**; admin **�198**/month; 21% VAT wedge
  - Detachments **1,395 (2019) ? 2,072 (2024)** (+48.5%); FOD Fin near 50-50 (198+197); RSVZ IT 10+82 FTE
  - Smals external IT share of turnover **17.8% ? 36%**; only **one broker bid** for dual-broker design
  - **Dual:** broker cash under mega-framework vs consultancy IT 2.03bn 3y stack
- Wrote: sources +2; budgets +8; cmt +3; lb +6; FOI **gap_smals_broker_rates_l5** ready+draft; rq_508=done spawn **rq_509**; ticks=517
- FOI opened: gap_smals_broker_rates_l5 (ready, human send) � not sent
- Next: prio5 **rq_509** (progress@520 soon); deferred **rq_116** SWA

### 2026-07-29T02:40:00Z - tick 518
- Unit: **rq_509** (FOI-adjacent hole-fill � **CoA consultancy Ch6 101-contract procurement compliance L5 dual**)
- Found (strong primary same CoA consultancy Oct 2025, Ch6 residual):
  - **Sample 101 contracts ~�2.2bn** incl VAT (2020-22 execution path)
  - **Non-compliance rates (of applicable contracts):** incomplete docs **63.4% / �1.5bn** � no cost-benefit **78.2% / �1.8bn** � need unjustified **20.8% / �1.0bn** � no realistic estimate **44.6% / �1.4bn** � exclusion unchecked **67.5% / �1.7bn** � selection fail **39.2% / �1.1bn** � abnormal prices **60.2% / �1.4bn** � award decision fail **40.5% / �1.5bn** � delegation **12.9% / �586m** � negotiation **10.3% / �280m** � forfait **8.1% / �78m**
  - **Named overruns:** org consult **1.8?>47m** � SAP **10?>22m** � datamine **72?110m** � micro **0.4?10m**
  - **Dual:** compliance failure under 2.5bn consultancy stack + Smals broker channel
- Wrote: sources +2; budgets +19; cmt +3; lb +7; FOI **gap_cons_101_named_overruns_l5** ready+draft; rq_509=done spawn **rq_510**; ticks=518
- FOI opened: gap_cons_101_named_overruns_l5 (ready, human send) � not sent
- Next: prio5 **rq_510** (**progress@520 next tick**); deferred **rq_116** SWA

### 2026-07-29T03:00:00Z - tick 519
- Unit: **rq_510** (FOI-adjacent hole-fill — **CoA 2025_01 Justice digital transformation + dual IT failures**)
- Found (strong primary Rekenhof AG Jan 2025 + press/summary):
  - **Policy-cell estimate digi cost ~€140m 2023** (full calc not possible multi-source)
  - **SD ICT:** commit **€61.3m (2020) → €93.4m (2023)**; liq **€56.5m → €80.5m**; structural path **~43→~80m** from 2025
  - **PHV/RRF:** nearly **€115m excl VAT** to 2026 for Justice digital; CoA flags eligibility misuse risk
  - **Consultants ~500:** SD ICT **92** (26 Egov) vs 145 stat (Feb23); Crossborder **228** vs **6** stat (Nov23); DTO **137** + 6 int (Dec23)
  - **JustSign/bpost irregular €5.8m** (JustSign **€3.1m**) without regular tender; IF-flagged regularisations
  - No single coherent strategy; DTO ends **31 Dec 2025**; cabinet ops role strong; basic admin functions weak
  - **Dual:** Justice digi stack vs I-Police **76.7/299m** · Persona **16m** · Cepage **35–96m** · federal consultancy **2.5bn**
- Wrote: sources +3; budgets +14; cmt +3; lb +7; FOI **gap_justice_digi_l5** ready+draft; raw PDFs; rq_510=done spawn **rq_511**; ticks=519
- FOI opened: gap_justice_digi_l5 (ready, human send) — not sent
- Next: prio5 **rq_511** (**progress@520 next tick**); deferred **rq_116** SWA

### 2026-07-29T03:20:00Z - tick 520
- Unit: **rq_511** (progress milestone @520 — coverage % + waste top10; no invent euros)
- Found / inventory:
  - **A/B:** still **100%** L0/L1 on EUR 347.956bn TE
  - **C L2:** **~99%** — BRU SEC/STIB + Justice digi + consultancy inventory layer
  - **D L5:** **~32-45%** generous — gain 510→520: Phoenix/customs/defence residual + consultancy **2.5bn** + Smals broker **1.8bn** + 101-sample **2.2bn** + Justice digi **140m/~500** consultants + BRU Entity II + FAM
  - **E FOI:** ready **~265** · answered **~9** · total **~277**
  - **Rows:** budgets **~9027** · cmt **~974** · lb **~1822** · entities **~410** · sources **~974** · rq **~506**
  - **Waste top10 change:** fossil/cars/cheque stable #1-6/#8-9; **NEW** lb_cons_no_costbenefit_18bn **#7** · lb_cons_101_sample_2_2bn **#10**; EIWT drops just-outside
- Wrote: progress_every_10_ticks.md · doge_waste_top10_current.md · rq_511=done spawn **rq_512**; ticks=520
- FOI: none new (progress tick)
- Next: prio5 **rq_512**; deferred **rq_116** SWA

### 2026-07-29T03:40:00Z - tick 521
- Unit: **rq_512** (FOI-adjacent hole-fill — **CoA Justice digi residual PHV L5 three projects + JustSign licenses dual prison**)
- Found (strong primary same CoA 2025_01 residual extract):
  - **PHV pack recon:** I-2.05 digi transform **€85m** · I-2.03 cyber NTSU/CTIF **€18m** · I-4.09 prison platforms **€12m** = **€115m** excl VAT (matches prior total)
  - **JustSign licenses ~€720k/yr** incl VAT (CM May 2024 bridge after bpost to underaannemers; competitive retender planned)
  - **bpost 5.8m path:** vastleggingen **3.5m + 2.3m** 23 Dec 2020; charged on **prog 56.05** traffic-fine collection support (budget specialty breach)
  - **Dual:** PHV prison digital **12m** vs DBFM capacity **3.83bn/25y** + overcrowding **840m**
- Wrote: sources +2; budgets +8; cmt +3; lb +6; FOI **gap_justice_phv_projects_l5** ready+draft; rq_512=done spawn **rq_513**; ticks=521
- FOI opened: gap_justice_phv_projects_l5 (ready, human send) — not sent
- Next: prio5 **rq_513**; deferred **rq_116** SWA

### 2026-07-29T04:00:00Z - tick 522
- Unit: **rq_513** (FOI-adjacent hole-fill — **CoA 2025_30 HR social inspection + SIOD dual multi-agency**)
- Found (strong primary Rekenhof AG Sep 2025):
  - **Extra credits €18.283m (2021–24)** for **270 VTE** social inspectors (policy notes said 248)
  - **Net staff +8.2 VTE (+0.5%)** only: inspect **+50.6** · support **−42.4** (attrition/pensions)
  - FTE path: **1,622.0 → 1,630.2**; inspect **1,200.5 → 1,251.1**; support **421.5 → 379.1**
  - **Wage bill €127.2m → €148.1m** (+16.4%); RSZ **56.2m** · TSW **25.6m** · RVA **22.6m** · TWW **15.7m** · RSVZ **13.3m** · RIZIV **13.0m** · SIOD experts **1.8m**
  - Credit split: TSW **5.84m**/83 · RSZ **5.74m**/92 · RSVZ **2.97m**/44 · TWW **1.86m**/25 · RVA **1.58m**/22 · SIOD **0.22m**/3
  - **Dual:** 6 inspection services + SIOD coordinator vs prior SIOD fraud-yield claims
- Wrote: sources +3; entity siod; budgets +15; cmt +2; lb +5; FOI **gap_siod_inspect_net_fte_l5** ready+draft; raw PDFs; rq_513=done spawn **rq_514**; ticks=522
- FOI opened: gap_siod_inspect_net_fte_l5 (ready, human send) — not sent
- Next: prio5 **rq_514**; deferred **rq_116** SWA

### 2026-07-29T04:20:00Z - tick 523
- Unit: **rq_514** (FOI-adjacent hole-fill — **CoA 2025_12 Circulaire economie BBBC RRF dual federal/regional**)
- Found (strong primary Rekenhof AG 16 Apr 2025):
  - **BBBC PHV/RRF:** **€28.97m → €28m** after BE RRF envelope cut (5.9→4.5bn)
  - **Split:** project support **€23.66m** · SME campaign **€1.32m** · studies/consultancy **€2.3m** · staff **€0.794m**
  - **Call 1:** **12 projects / €6.98m**; selection opacity (cabinet unilateral lower awards; projects vs memo rules)
  - **Underuse risk** on remaining project envelope vs RRF mid-2026 deadline; PPP nv design abandoned → classic subsidies
  - **Delivery:** Roadmap 21 → **12 done / 7 partial / 2 not**; FAP 31 → **6 full / 21 partial risk / 4 not**
  - **Dual:** federal BBBC without regional NV coalition; WAL/VL separate CE PHV; Intra-Belgian Platform underpowered
- Wrote: sources +3; budgets +9; cmt +3; lb +5; FOI **gap_bbbc_l5_cash** ready+draft; raw PDFs; rq_514=done spawn **rq_515**; ticks=523
- FOI opened: gap_bbbc_l5_cash (ready, human send) — not sent
- Next: prio5 **rq_515**; deferred **rq_116** SWA

### 2026-07-29T04:40:00Z - tick 524
- Unit: **rq_515** (FOI-adjacent hole-fill — **CoA 2025_05 COVID federal support follow-up dual multi-level**)
- Found (strong primary Rekenhof AG 22 Jan 2025 + press):
  - **2020:** **103 measures**, est **€19.40bn**; **H1 2021 +€1.15bn**
  - **Split 2020:** benefits **€11.83bn (61%)** · tax relief **€3.05bn (16%)** · SSC **€1.06bn (5%)** (+ deferrals/guarantees/reinsurance off estimate)
  - **Recs 19:** **2 done · 9 in progress · 6 not done · 2 not assessed**
  - Still missing: shared crisis playbook, public inventory, common support database, overarching evaluation
  - **Dual:** federal package vs regional stacks; multi-level coordination recs largely unfinished
- Wrote: sources +3; budgets +6; cmt +3; lb +6; FOI **gap_covid_support_outturn_l5** ready+draft; raw PDFs; rq_515=done spawn **rq_516**; ticks=524
- FOI opened: gap_covid_support_outturn_l5 (ready, human send) — not sent
- Next: prio5 **rq_516**; deferred **rq_116** SWA

### 2026-07-29T05:00:00Z - tick 525
- Unit: **rq_516** (FOI-adjacent hole-fill — **CoA kentekenplaten concession 240m + follow-up 0/17 recs dual bpost**)
- Found (strong primary CoA 2022_11 + 2024 press; secondary procurement summary 2025_03):
  - **Concession 2:** est **€240m**, bpost, 1 Aug 2019–max 31 Jul 2025; **sole bidder** (incumbent advantage in spec)
  - **User fee €30**/plate+cert; costs shifted to owners; claimed admin save **€3.8m** + **13 VTE**
  - DIV net receipts **≥€44m** 2012–18 (cum class **~€70m**); 2021 receipts **€9.82m** vs costs **€8.67m**
  - Annual prod+dist class **€28.9m** excl VAT; penalty paid **€2m** (CoA: ≥**€2.5m** due); schrapping stream **~€50m** class
  - **Follow-up 2024:** of **17 recs → 0 done · 4 in progress · 5 none · 8 n/a**; **DIV refused documents** to CoA
  - **Secondary:** federal procurement sample **267 dossiers / €989.7m** ex VAT (Ypto/TUC Rail systemic fails dual rail IT)
  - **Dual:** bpost plates monopoly channel vs JustSign irregular path
- Wrote: sources +4; budgets +13; cmt +3; lb +7; FOI **gap_kenteken_concessie3_l5** ready+draft; raw PDFs; rq_516=done spawn **rq_517**; ticks=525
- FOI opened: gap_kenteken_concessie3_l5 (ready, human send) — not sent
- Next: prio5 **rq_517**; deferred **rq_116** SWA

### 2026-07-29T05:20:00Z - tick 526
- Unit: **rq_517** (FOI-adjacent hole-fill — **CoA 2025_03 procurement entity residual Ypto/TUC/Infrabel dual rail**)
- Found (strong primary residual same CoA procurement summary Dec 2024):
  - **Totals (prior):** 267 dossiers **€989.7m** excl VAT · invoices **€44.9m**
  - **FOD Economie:** 40d **€27.3m** of ~50m (consultancy **€21.6m**)
  - **Federal Police:** 35d **€45.7m** of **€225.8m** (IT supplies **31.7** · IT consult **9.7** · other **4.3**)
  - **SCK CEN:** 40d **€108.9m** of **€175.2m** PO>20k 2022
  - **FOD WASO:** 20d **€4.3m**
  - **Beliris:** 35 forms **€87.5m** of **€101.3m** since 2020 (dual federal-BRU)
  - **Infrabel:** 40 contracts **€550m** excl VAT (largest **214m** · cables **75.6m** · consultancy **≥10.5m**)
  - **Ypto:** does **not correctly apply** procurement law; awards class **>€154m**; orders **~€35.7m** class
  - **TUC Rail:** **>half** own-need purchases **without tender**; frameworks class **>€39m**
  - **Dual:** rail IT/engineering stack compliance failures
- Wrote: sources +2; budgets +16; cmt +2; lb +7; FOI **gap_rail_proc_ypto_tuc_l5** ready+draft; rq_517=done spawn **rq_518**; ticks=526
- FOI opened: gap_rail_proc_ypto_tuc_l5 (ready, human send) — not sent
- Next: prio5 **rq_518** (progress@530 soon); deferred **rq_116** SWA

### 2026-07-29T05:40:00Z - tick 527
- Unit: **rq_518** (FOI-adjacent hole-fill — **CoA 2024_55 company-car CO₂ SSC + mobility budget dual taxex**)
- Found (strong primary Rekenhof AG 30 Oct 2024 + press):
  - **Receipts 2022: €278.52m** CO₂ contribution (+12% vs 2008) for **560,941** vehicles (+82%)
  - Avg per vehicle **€802 → €497** (−38%); cumulative target gap **€958m** 2008–2022
  - Gap vs ordinary employer SSC on wage-equivalent **>€1bn by 2026** (min CO₂ generalisation)
  - **Febiac 1.105m** legal-person vehicles vs RSZ **578k** Q4 2022; leasing opacity; DIV data unused
  - **WLTP/NEDC gaming ~€74.3m** cost to SS 2022; under-declaration risk **≥€22m/yr** (band 4–32m)
  - Mobility budget still **marginal** (~50× fewer users than company cars); special contrib class **~€15.5m** 2023
  - **Dual:** SSC under-collection under mega **taxex/FFS company-car package** (top10)
- Wrote: sources +3; budgets +10; cmt +2; lb +6; FOI **gap_co2_bijdrage_div_cross_l5** ready+draft; raw PDFs; rq_518=done spawn **rq_519**; ticks=527
- FOI opened: gap_co2_bijdrage_div_cross_l5 (ready, human send) — not sent
- Next: prio5 **rq_519** (**progress@530 next tick**); deferred **rq_116** SWA

### 2026-07-29T06:00:00Z - tick 528
- Unit: **rq_519** (FOI-adjacent hole-fill — **CoA residual mobiliteitsbudget L5 dual company cars**)
- Found (strong primary same CoA 2024_55 Ch5 residual):
  - **MB 2023 total €72.0m** for **10,250 workers** / **1,155 employers** (was €0.65m / 141 in 2019)
  - **~50× fewer** users than company-car CO₂ fleet (**560,941** vehicles)
  - **Pillar 2 €50.82m** (8,329 workers) — practical use opaque (housing rent/mortgage heavy in studies)
  - **Pillar 3 €15.54m** (21% of total; 6,551 workers) — 38.07% special SSC limited deterrent
  - **SSC both pillars €6.22m** 2023 (~2% of CO₂-class receipts)
  - Pillar 1 cars Q4 2023 only **947**; cap **€16k/yr** and **1/5** gross wage
  - Residual: CO₂ contrib **€59.1m** from <20-staff employers (21%) without systematic control
  - **Dual:** under-used MB reform vs dominant company-car taxex/SSC hole
- Wrote: sources +2; budgets +11; cmt +2; lb +6; FOI **gap_mb_pillar2_use_l5** ready+draft; rq_519=done spawn **rq_520**; ticks=528
- FOI opened: gap_mb_pillar2_use_l5 (ready, human send) — not sent
- Next: prio5 **rq_520** (**progress@530 next tick**); deferred **rq_116** SWA

### 2026-07-29T06:15:00Z - tick 529
- Unit: **rq_520** (FOI-adjacent hole-fill — **CoA 2025_33 Métro 3 BRU dual STIB+Beliris**)
- Found (strong primary Cour des comptes AG 8 Oct 2025 + press/synthèse):
  - **Total Dec2024: €4,759.7m** vs **€824.2m** 2012 (**+€3,935.5m / +477%**); service **2035** (was 2020)
  - Segments: Nord-Albert class **€1,323.1m** · Nord-Bordet **€3,102.8m** · Bordet full **€3,436.6m** (lot3 1,698.9+risk 254.8)
  - **Spent EOY2024: €421.3m** (NA 316.4 + BN 104.9); remaining works **€4,338.4m**
  - **Beliris:** envelope 516.3m · financed **464.4m** · **402.7m diverted** other metro · residual **51.9m**
  - **BCR financing gap ~€4,286.5m** (~4bn class; >2/3 2024 receipts)
  - **EIB loan €475m** 25y (draw by Dec 2027; need ≥950m invest)
  - STIB scenarios: A **4,375** · A-PPP **7,743** · B **1,653** · C pause **4,807** · E stop **1,002**
  - SM BMN conflict: firm **0.76m** vs conditional **19.1m**; governance/procurement failures; works suspended
  - **Dual:** STIB maitre ouvrage + Beliris federal delegated; federal ~500m cap vs 4.8bn programme
- Wrote: sources +4; budgets +17; cmt +5; lb +9; FOI **gap_metro3_cash_by_year_l5** ready+draft; raw PDF+press+synth; rq_520=done spawn **rq_521**; ticks=529
- FOI opened: gap_metro3_cash_by_year_l5 (ready, human send) — not sent
- Next: prio5 **rq_521** (**progress@530 THIS next tick**); deferred **rq_116** SWA

### 2026-07-29T06:30:00Z - tick 530
- Unit: **rq_521** (**progress milestone** — coverage % layers A-E + waste top10 refresh)
- Progress snapshot (tick 530):
  - A/B still **100%**; C **~99%**; D **~33-46%** generous TE share (structural payroll/debt not L5)
  - Inventory: budgets **~9144** · cmt **~1002** · lb **~1879** · entities **~414** · sources **~1003** · FOI ready **~274** / answered **~9** / total **~286** · rq **~516**
  - Gain 520→530: SIOD HR leakage · BBBC/COVID residual · plates 0/17 · rail Ypto/TUC · CO2/MB dual cars · **Metro3 4.76bn +477%** dual STIB+Beliris
- Waste top10: fossil/cars/cheque still **#1-5/#8/#10**; **NEW #6-7** CO2 vs ordinary SSC gap + dual cars SSC/taxex (tick527); consultancy compliance still high; Metro3 multi-year stock annualised off pure #1 (lb fix annual residual class)
- Also: corrected Metro3 lb annual-vs-stock fields so multi-year envelopes do not fake annual TE rank
- Wrote: progress_every_10_ticks.md · doge_waste_top10_current.md · lb Metro3 annual fix · rq_521=done spawn **rq_522**; ticks=530
- FOI: none new (progress tick)
- Next: prio5 **rq_522** hole-fill; deferred **rq_116** SWA

### 2026-07-29T06:45:00Z - tick 531
- Unit: **rq_522** (FOI-adjacent hole-fill — **CoA 2025_49 SECAL/DAVO suivi dual Finance+Justice**)
- Found (strong primary Cour des comptes AG 26 Nov 2025 + press 16 Dec 2025):
  - **Advances 2024: €38.79m** for **21,188** children (path 26.2m 2015 → 31.3m 2020 → 38.8m 2024)
  - **Dossiers:** new **5,378** 2024; active EOY **23,955** (×2.6 since 2007); online apps 550→3400+ (2021-24)
  - **Recovery 12m: 26.6%** 2024 / **32.9%** first 8m 2025; cumulative rate lost (was **29.25%** EOY2018)
  - **Stock EOY2024: €452.7m** with **impairment €403.3m** (~89%); CoA questions accounting reliability
  - **Undue advances:** €1.558m / 1,599 dossiers Jun2023-Jun2025; ~2/3 recovered; fraud 100% path never used
  - **Recs 2019:** 5 done · 9 progress · 3 not · 1 n/a + **8 new** recs 2025; eval commission reports missing 2011-23
  - FIFO oldest-debt-first can disadvantage alimentary creditors vs other tax debts; legal imputation order state-first
  - **Dual:** FPS Finance AGPR + FPS Justice international few dossiers / weak follow-up / lack means; judgment file 2014 never built
- Wrote: sources +3; budgets +10; cmt +2; lb +7; FOI **gap_secal_recovery_kpi_l5** ready+draft; raw PDF+press; rq_522=done spawn **rq_523**; ticks=531
- FOI opened: gap_secal_recovery_kpi_l5 (ready, human send) — not sent
- Next: prio5 **rq_523**; deferred **rq_116** SWA

### 2026-07-29T07:00:00Z - tick 532
- Unit: **rq_523** (FOI-adjacent hole-fill — **CoA Taxe Caïman 2023 + suivi 2025 dual federal/regions**)
- Found (strong primary CoA 2023_13 + 2026_01 suivi AG 10 Dec 2025 + press 12 Jan 2026):
  - **Budget estimates:** **€50m** 2015 · **€460m** 2016; no separate line from 2017; **+€50m** 2.0 path 2018
  - **Indicative realized class:** **€160.98m** (spontaneous PM + controls) · **€181.37m** incl leak dossiers — well below early budgets
  - **Agisi:** 45 cases · enrolled **€92.44m** · collected **€11.25m (12.17%)** by Jun 2022
  - **AGFisc:** fines non-declaration **€2.06m** + tax supplements **€0.65m**
  - **Suivi 2025 recs:** **6 done · 4 progress · 4 not** of 14; annex **276 CJC** (measure method) but AGESS still no receipt calc to CoA
  - **Const Court 18 Sep 2025:** partial annul 2.1 (dedicated funds 50% without counter-proof; substance EU law; exit tax Belgian period; CFC non-residents)
  - Exit tax: **50** founders identified; **73** founders left BE since 2024
  - **Dual:** federal Caiman vs regional succession capital; Vlabel NCD blocked security; concertation autumn 2025 start only
- Wrote: sources +4; budgets +10; cmt +2; lb +7; FOI **gap_caiman_receipts_l5** ready+draft; raw PDFs; rq_523=done spawn **rq_524**; ticks=532
- FOI opened: gap_caiman_receipts_l5 (ready, human send) — not sent
- Next: prio5 **rq_524**; deferred **rq_116** SWA

### 2026-07-29T07:15:00Z - tick 533
- Unit: **rq_524** (FOI-adjacent hole-fill — **CoA 2025_25 gecombineerde vergunning dual DEM+DVZ**)
- Found (strong primary Rekenhof AG 2 Jul 2025 + press):
  - **2023 DEM:** apps **17,072** (first 9,031 + renew 8,041) · grants **11,764** · refusals **1,903 (11.14%)** · withdrawals **779**
  - Refuse rate jump from **~3.2–3.7%** 2019-22 after fraud/Borealis/visa signals
  - First-app path class **4.8k→10.0k→8.9k** 2019-23
  - **DVZ BE first-app positives:** 5,251 / 9,540 / 9,967 (2021-23); refuse **~1%**
  - **DEM staff:** 26+14 VTE 2023 → **35.6** Mar 2024 (18 handlers); backlog remains; DVZ wait times not disclosed
  - **VSI:** 19.56 VTE econ mig 2023; 1,865 investigations; DEM-requested 262; +11 inspectors Dec 2024 path
  - **Fines AG:** €54k / €123k / €56k 2021-23; practice **€2–4k** low end of statutory fork; deterrent untested
  - **Auto-approve** dozens when statutory deadline expires (DEM+DVZ); residual after control upgrade
  - Unique loket cost-share fed **63%** / VL **19.24%** / BRU **12.58%** / WAL **4.81%** / DG **0.37%**; incomplete actor access
  - **Dual:** sequential DEM work then DVZ residence; trust gap mutual verification; inspectors limited cross-view
- Wrote: sources +3; budgets +12; cmt +2; lb +7; FOI **gap_gv_volumes_kpi_l5** ready+draft; raw PDF+press; rq_524=done spawn **rq_525**; ticks=533
- FOI opened: gap_gv_volumes_kpi_l5 (ready, human send) — not sent
- Next: prio5 **rq_525**; deferred **rq_116** SWA

### 2026-07-29T07:30:00Z - tick 534
- Unit: **rq_525** (FOI-adjacent hole-fill — **Kamer exposé 2026 Table41 DBFM prison invest fees residual**)
- Found (strong primary DOC 56 1278/001 Table41 + CoA residual context):
  - **Haren:** quarterly **€7.3m** · annual **€29.4m** · 25y **€733.9m** · paid **€91.0m** · remain **€638.5m** (87q)
  - **Beveren:** annual **€9.1m** · 25y **€228.7m** · paid **€107.7m** · remain **€121.0m**
  - **Marche-en-Famenne:** annual **€6.9m** · 25y **€172.3m** · paid **€84.4m** · remain **€87.9m**
  - **Leuze-en-Hainaut:** annual **€7.5m** · 25y **€188.6m** · paid **€86.7m** · remain **€101.9m**
  - **4 prisons sum:** annual **~€53m** · 25y **~€1.32bn** · paid **~€370m** EOY2025 · remain **~€950m**
  - **Antwerp:** annual **€17.1m** (Q1 2026 start); 25y total still under construction
  - **Dendermonde:** variable fee; paid **>€26.5m** since end-2022; annual/25y not fixed
  - **Residual:** maintenance/waste/laundry/catering fees still omitted (price revision); off-balance booking still open CoA rec10
- Wrote: sources +2; budgets +11; cmt +2; lb +6; FOI **gap_dbfm_maint_facility_fees_l5** ready+draft; updated prior gap_dbfm_fees note; raw exposé PDF; rq_525=done spawn **rq_526**; ticks=534
- FOI: gap_dbfm_maint_facility_fees_l5 ready (not sent); prior invest-fee gap partially filled public
- Next: prio5 **rq_526**; deferred **rq_116** SWA

### 2026-07-29T07:45:00Z - tick 535
- Unit: **rq_526** (FOI-adjacent hole-fill — **CoA 2024_42 TACT annual securities-account tax dual wealth**)
- Found (strong primary Cour des comptes + press/synthèse Oct 2024):
  - **Due:** p1 **€470.203m** · p2 **€395.391m** (−16%) · p3 prov **€362.103m** (further decline)
  - **Budget est:** 2021 **€397.8m** (actual above) · 2022 **€428.6m** (actual below)
  - **Two periods net:** due after restitutions **€859.2m** · perceived end-Aug 2023 **€814.4m**
  - **Restitutions €6.39m** (~80% nominative conversion + cash; ~80% conversion claims accepted)
  - Self-declarers **€20.2m → €15.6m** (−23%); foreign accounts not systematically matched
  - Const Court Oct 2022 annulled irrefragable anti-abuse (account split + nominative conversion)
  - No digital filing / First incomplete → risk analysis & evaluation excluded until digitisation **≤2028**
  - Rate remains **0.15%** threshold **€1m** (budget 2026 double to 0.30 / +€414m path prior fill)
  - **Dual:** TACT stock wealth tax decline vs Cayman under-collection / NBB rising financial wealth
- Wrote: sources +3; budgets +9; cmt +2; lb +7; FOI **gap_tact_digital_kpi_l5** ready+draft; raw PDF+press+synth; rq_526=done spawn **rq_527**; ticks=535
- FOI opened: gap_tact_digital_kpi_l5 (ready, human send) — not sent
- Next: prio5 **rq_527**; deferred **rq_116** SWA

### 2026-07-29T08:00:00Z - tick 536
- Unit: **rq_527** (FOI-adjacent hole-fill — **Kamer exposé 2026 spending reviews + Entity I invest Table40**)
- Found (strong primary DOC 56 1278/001 §4–§5):
  - **WASO postal SR:** credits **€430k (2024) → €50k (2026)**; federal recurrent save band **€15–67.5m** (eBox invest not netted)
  - **Fedasil open centres SR:** flexible specialist model potential **€1.1m/yr**; CM 3 Oct 2025 action plan path
  - **Return / closed centres:** CM Feb 2025 efficiency path to **€150m by 2029**; linear **1.8%** opex+personnel; SR 2026 in progress
  - **SR programme list** 2021-24: telework, BV remittance, care, Belspo, nuclear passif, cyber, asylum, justice costs, R&D aid, subsidies inventory
  - **2026 SRs in progress:** closed centres; fossil subsidies phase-out; EIWT O&O/overtime/night-shift
  - **Table40 Entity I invest 2026:** direct **€5,174m** · GCF ESA **€6,612m** · NMBS aid **€1,094m** · gov-supported **€7,706m (1.2% GDP)**; path 2025-29 to **€8,344m**
- Wrote: sources +2; budgets +12; cmt +3; lb +7; FOI **gap_sr_save_delivery_l5** ready+draft; rq_527=done spawn **rq_528**; ticks=536
- FOI opened: gap_sr_save_delivery_l5 (ready, human send) — not sent
- Next: prio5 **rq_528**; deferred **rq_116** SWA

### 2026-07-29T08:15:00Z - tick 537
- Unit: **rq_528** (FOI-adjacent hole-fill — **Kamer exposé 2026 vergrijzingsnota SCvV Jul2025 + policy dual E1/E2**)
- Found (strong primary DOC 56 1278/001 Ch2 + SCvV Jul2025 via exposé):
  - **Social exp % GDP:** **25.8% (2024) → 26.3% (2030) → 27.6% (2050) → 27.5% (2070)**; aging cost **+1.7 pp** 2024-70
  - **vs 2024 SCvV report:** cost **1.9 pp GDP lower** mainly pension reform (−1.3pp) + UI time-limit (−0.4pp)
  - **Pensions:** 11.3 → 12.2 pct (+0.9); employees 6.6 public 3.8 self 0.9 (2024)
  - **Healthcare:** 8.0 → 10.1 pct (+2.1) dominates long-run rise
  - **Unemployment:** 1.0 → 0.4 pct (−0.6) incl SWT
  - **Dual E1/E2:** E1 social 21.7% (+1.3pp to 2070) vs E2 4.2% (+0.4pp); federal pensions+health vs regional family benefits
  - **Policy path (medium):** exp control **>€2.7bn by 2029**; LT-sick **>€1.9bn by 2029** (>500k persons); SME + social cohesion envelopes **€8.5m each 2026 → €15m 2029**
- Wrote: sources +2; budgets +14; cmt +3; lb +7; FOI **gap_aging_reform_cash_l5** ready+draft; rq_528=done spawn **rq_529**; ticks=537
- FOI opened: gap_aging_reform_cash_l5 (ready, human send) — not sent
- Next: prio5 **rq_529**; deferred **rq_116** SWA

### 2026-07-29T08:30:00Z - tick 538
- Unit: **rq_529** (FOI-adjacent hole-fill — **Kamer exposé Graph1 dual federal/SS flows + Entity I Table3 saldo**)
- Found (strong primary DOC 56 1278/001 Graph1 + Tables 3–4):
  - **Graph1 federal (2026 bn):** receipts **173.7** (fiscal **164.3**: IPP **64.2** VAT **45.1** CIT **26.0** excises **11.2** RV **8.0**); nonfiscal **9.4**
  - **Transfers out:** Entity II **81.5** · SS **54.3** · EU **9.1** → **available federal only 27.5**
  - **Graph1 SS:** total=available **148.0** (SSC **85.5** + federal **54.3** + federated **0.4** + other **7.8**)
  - **Table3 Entity I 2026:** receipts **201.98bn** · primary exp **215.88bn** · primary saldo **−12.47bn** · interest **12.17bn** · financing saldo **−24.64bn (−3.7% GDP)** vs **−23.05bn (−3.6%)** 2025
  - Defence ESR corr **−1.9bn** less favourable 2026 + EU GNI **+1.2bn**; unallocated measures **+1.425bn (0.2% GDP)**
  - Defence effort save fill **€250m 2026 → €1bn** path
- Wrote: sources +2; budgets +23; cmt +3; lb +7; FOI **gap_e1_unallocated_measures_l5** ready+draft; rq_529=done spawn **rq_530**; ticks=538
- FOI opened: gap_e1_unallocated_measures_l5 (ready, human send) — not sent
- Next: prio5 **rq_530** (progress@540 soon); deferred **rq_116** SWA

### 2026-07-29T08:45:00Z - tick 539
- Unit: **rq_530** (FOI-adjacent hole-fill - **Kamer exposé 2026 federal primary by dept Tables1-5 + econ Table6 + COFOG Table7 + interest**)
- Found (strong primary DOC 56 1278/001 Part III Ch3):
  - **Primary VEK 2026:** **€99.656bn** (+6.5% vs adj 2025 €93.855bn)
  - **Primary VLK 2026:** **€90.949bn** (-0.9% vs adj €91.774bn) - dual commit backlog **~€8.7bn**
  - **Defence dual:** VEK **€20.112bn** (+56.5%) vs VLK **€10.770bn** (+3.3%) - backlog **~€9.3bn**
  - **SS dept** €30.724bn (-1.0%); evenwichtsdotaties -€1.122bn; FPD +€531m; handicap +€194m
  - **Dotaties** €17.744bn; **BNI EU** €4.994bn (+30.2%); **Finance** -€3.007bn (IMF capital 2025 €2.945bn base effect)
  - **Provisions VLK €2.128bn:** interdept 829.7 (justice 618.3 + bpost 78 + Fedasil 100 + vulnerable 33.5); Ukraine 442.8; security 366.9; index 485.2
  - **Econ class VLK:** SS transfers **€26.530bn (29.2%)** · C&R **€17.948bn (19.7%)** · wages 8.3 · foreign 6.6 · autonomous 5.9 · ops 5.2 · invest 5.0
  - **COFOG VLK:** gen admin **€41.169bn (45.3%)** · social **€24.176bn (26.6%)** · defence **€10.879bn (12.0%)** · order 6.4 · econ 6.4
  - **Federal interest:** 2025 **€10.944bn** (1.7% GDP) · 2026 **€12.343bn** (+€1.399bn)
- Wrote: sources +2; budgets +43; cmt +4; lb +8; FOI **gap_fed_defence_vek_vlk_l5** ready+draft; rq_530=done spawn **rq_531**; ticks=539
- FOI opened: gap_fed_defence_vek_vlk_l5 (ready, human send) - not sent
- Next: prio5 **rq_531** (progress@540 next tick); deferred **rq_116** SWA


### 2026-07-29T09:00:00Z - tick 540
- Unit: **rq_531** (FOI-adjacent hole-fill + **progress@540** - **Kamer exposé ODA dual multi-actor + federal interest/debt financing schema**)
- Found (strong primary DOC 56 1278/001 Part III Afdeling 2-3):
  - **ODA total:** 2022 **€2.532bn (0.45%)** · 2023 **2.604 (0.44)** · 2024 **2.990 (0.48 peak)** · 2025 **2.392 (0.37)** · 2026 **2.350 (0.35% GNI)**
  - **DGD 2026:** VEK **€654m** / VLK **€1.040bn**; ODA-eligible DGD **€1.031bn**; **25%** cut path; DGD share **48%** of ODA 2024 (was 60% 2020)
  - **Multi-actor dual:** EC share **€897m 2026** · Fedasil **€437m 2024 → €234m 2026** · Foreign **€92m** · Finance **€16m** · non-fed **€83m**
  - **Interest series:** trough **€6.93bn 2022** → **10.03 2024** → **10.94 2025** → **12.34bn 2026 (1.86% GDP)**; Treasury **12.165** + consol **55** + FPS Fin **124**
  - **Financing 2026:** gross **€59.7bn** (net **28.5** + maturing **28.0** + prefin **3.2**); OLO **€52bn** of LT **55.3**; wavg rate **3.83%** / maturity **16.04y**
  - **Unconsol fed debt:** eoy2024 **€540.7bn (87.2%)** → 2025 **570.2 (88.7%)** → 2026 **601.3bn (90.8% GDP)**
- Wrote: sources +2; budgets +34; cmt +4; lb +8; FOI **gap_oda_partner_l5** ready+draft; progress_every_10_ticks.md + doge_waste_top10_current.md @540; rq_531=done spawn **rq_532**; ticks=540
- FOI opened: gap_oda_partner_l5 (ready, human send) - not sent
- Progress@540: A/B 100%; C ~99%; D ~34-47% (generous); FOI ready ~284 / answered ~9; inventory budgets~9322 lb~1950 sources~1028
- Next: prio5 **rq_532**; deferred **rq_116** SWA


### 2026-07-29T09:15:00Z - tick 541
- Unit: **rq_532** (FOI-adjacent hole-fill - **Kamer exposé Ch4 dual federal→C&R/SS/local Tables 1-5**)
- Found (strong primary DOC 56 1278/001 Part III Ch4):
  - **C&R total 2026:** **€76.810bn** (C **50.418** + R **26.392**); 2025 **75.534**; 2024 **73.206**
  - **Communities:** VL **€30.769bn** · FR **17.612** · DG **0.345** · GGC **1.576**; VAT **22.504** · PB **10.942**; family **9.170** · eldercare **5.677**
  - **Regions:** VL **~12.729** · WAL **~9.257** · BRU **~4.405** (credits heavy on BRU **438.5m** incl mobility **195** city **146**)
  - **SS federal means 2026:** **€53.879bn** (credits **26.554** + fiscal **27.325**); employees **8.335** · self-emp **1.076** · public pensions **16.150**; dual Graph1 **54.3**
  - **Local 2026:** **€4.257bn** (leefloon **2.085** · police **1.271** · refugees **0.156** · capital **0.207**)
  - **Dual gap:** Graph1 E2 **81.5** vs Table1 C&R **76.8** (~**€4.7bn** perimeter)
- Wrote: sources +2; budgets +44; cmt +4; lb +8; FOI **gap_fed_e2_cr_perimeter_l5** ready+draft; rq_532=done spawn **rq_533**; ticks=541
- FOI opened: gap_fed_e2_cr_perimeter_l5 (ready, human send) - not sent
- Next: prio5 **rq_533**; deferred **rq_116** SWA


### 2026-07-29T09:30:00Z - tick 542
- Unit: **rq_533** (FOI-adjacent hole-fill - **Kamer exposé EU Table6 + consol institutions Ch5 dual**)
- Found (strong primary DOC 56 1278/001 Part III Ch4§4 + Ch5):
  - **EU financing 2026:** total **€9.145bn** (customs **3.402** + VAT **0.748** = receipts **4.150** + GNI **4.994**); 2025 **7.869**; dual Graph1 **9.1**
  - **GNI** +**€1.159bn** YoY drives total rise; customs rising post-2023 dip
  - **Consol orgs 2026:** receipts **€10.991bn** · exp **€9.976bn** · ESA saldo **+€1.392bn** (+691 vs 2025 **+0.701**)
  - Receipts mix: institutional group dots **57.4%** · goods/services **21.4%** · property **12.2%**
  - Exp mix: ops **33.1%** · wages **26.0%** · invest **15.6%** · credit/equity **7.3%**
  - **Named ESA saldos 2026:** FPIM **+636.6** · BE-WATT **+499.3** (Phoenix new) · Hedera **+452.9** · ASEVA **+89.3** · Infrabel **-56.5** · CREG **-23.3**
  - Conclave: NIRAS nuclear passif **+€198m** (ESA balance); Sciensano **+3m**; Healthdata→HDA **€6m** from RIZIV
- Wrote: sources +2; budgets +37; cmt +4; lb +8; FOI **gap_consol_orgs_l5_spend** ready+draft; rq_533=done spawn **rq_534**; ticks=542
- FOI opened: gap_consol_orgs_l5_spend (ready, human send) - not sent
- Next: prio5 **rq_534** (Part IV SS systems residual); deferred **rq_116** SWA


### 2026-07-29T09:45:00Z - tick 543
- Unit: **rq_534** (FOI-adjacent hole-fill - **Kamer exposé Part IV social protection Tables I.1-I.3 dual Graph1**)
- Found (strong primary DOC 56 1278/001 Part IV Ch1; thousand-EUR tables):
  - **Social protection 2026:** rec **€194.673bn** · exp **€194.514bn** · result **+€97m** (vs 2025 result **-€1.496bn**)
  - **SS own receipts €148.017bn** = Graph1 SS **148.0**; **SSC €85.525bn** = Graph1 **85.5**
  - **Benefits €142.053bn** (SS **135.492** + assistance **6.561**): employees **63.342** · health **41.297** · public pensions **22.828** · self-emp **7.012**
  - **Admin €2.996bn** (central **1.242** + third-party **1.754**)
  - **Federal transfers I.3:** SS **€54.617bn** (dual Graph1 **54.3**) + assistance **€6.563bn** = **€61.181bn**
  - **Alt financing €27.222bn:** emp VAT **16.989** (base 9.344 + health 7.645) + RV **6.403**; self-emp **3.829**
  - **Assistance L5:** handicap **3.286** · leefloon **2.085** · IGO **1.037** (excl Ukraine provision)
- Wrote: sources +2; budgets +35; cmt +4; lb +8; FOI **gap_ss_branch_l5_detail** ready+draft; rq_534=done spawn **rq_535**; ticks=543
- FOI opened: gap_ss_branch_l5_detail (ready, human send) - not sent
- Next: prio5 **rq_535**; deferred **rq_116** SWA


### 2026-07-29T10:00:00Z - tick 544
- Unit: **rq_535** (FOI-adjacent hole-fill - **exposé employees L5 benefits Table II.2 + RIZIV IV.1 dual + assistance VI.1**)
- Found (strong primary DOC 56 1278/001 Part IV; thousand-EUR tables):
  - **Employees benefits L5 2026:** pensions **€43.271bn** · illness/invalidity **€14.879bn** · unemployment **€4.638bn** · FEDRIS AO+BZ **€0.546bn** · total **€63.342bn**
  - **Unemployment dual:** **€6.459bn (2025) → €4.638bn (−€1.821bn)** UI time-limit path class
  - **Transfer to RIZIV** from employees table **€35.990bn**; contrib reductions **€1.197bn**
  - **RIZIV 2026:** benefits **€41.297bn** (+1.49); admin **€1.236bn** (third-party **€1.116bn**); financed RSZ **€35.839bn** + RSVZ **€3.348bn** + own **€7.212bn**
  - **TNW wave4:** save path **€118m** employee illness benefits; thematic controls **€25m** class
  - **Assistance VI.1:** leefloon **€2.085bn (+17.6%)** · handicap **€3.286bn (+6.3%)** · IGO **€1.035bn** · total **€6.561bn**
- Wrote: sources +2; budgets +29; cmt +4; lb +8; FOI **gap_unemp_leefloon_spillover_l5** ready+draft; rq_535=done spawn **rq_536**; ticks=544
- FOI opened: gap_unemp_leefloon_spillover_l5 (ready, human send) - not sent
- Next: prio5 **rq_536**; deferred **rq_116** SWA


### 2026-07-29T10:15:00Z - tick 545
- Unit: **rq_536** (FOI-adjacent hole-fill - **exposé self-employed Table III.2 + public pensions VII.2 dual three-stack**)
- Found (strong primary DOC 56 1278/001 Part IV Ch3+Ch7; thousand-EUR tables):
  - **Self-emp benefits 2026:** total **€7.012bn** — pensions **€5.920bn** · illness **€1.070bn** · bridging **€15.3m** · caregiver **€6.9m**
  - Transfer self→RIZIV **€3.551bn**; admin **€164m**
  - **Public pensions benefits 2026:** total **€22.828bn** (+€0.67bn YoY)
  - Treasury **€17.016bn** · solidary local fund **€2.891bn** · HR Rail **€1.569bn** · parastatal **€0.809bn** · fed police **€0.186bn**
  - **Dual three-stack pensions:** emp **€43.271** + self **€5.920** + public **€22.828** = **€72.019bn** benefits 2026
- Wrote: sources +2; budgets +29; cmt +4; lb +8; FOI **gap_pubpen_employer_l5** ready+draft; rq_536=done spawn **rq_537**; ticks=545
- FOI opened: gap_pubpen_employer_l5 (ready, human send) - not sent
- Next: prio5 **rq_537** (exposé Part IV largely filled → new public residual); deferred **rq_116** SWA


### 2026-07-28T22:13:28Z - pause
- User: **paused=yes**
- Cancelled scheduler **019fa9b6c43a** (every 1m)
- State: ticks=545 last_unit=rq_536; next on resume **rq_537**
- No research tick; FOI not sent


### 2026-07-31T08:32:16Z - resume
- User: **paused=no**
- 60s watcher recreated; fire_immediately first tick
- State: ticks=545 last_unit=rq_536; next **rq_537** (progress@550 soon)


### 2026-07-31T08:35:00Z - tick 546
- Unit: **rq_537** (FOI-adjacent hole-fill - **Kamer expose Part IV Ch5 other SS Tables V.1-V.2 L5**)
- Found (strong primary DOC 56 1278/001 Part IV Ch5; thousand-EUR tables):
  - **Other SS total 2025:** rec **EUR 1.645bn** · exp **1.522bn** · result **+122.9m**
  - **Other SS total 2026:** rec **EUR 1.569bn** · exp **1.570bn** · result **-1.2m**
  - **Benefits L5 2026:** FSO **319.9m** · Ex-OSZ **336.0m** · RVA emp missions **261.4m** · medical **37.6m** · asbestos **23.4m** · Fedris-AO cap **15.4m** · PPO **15.2m** · war/terror **4.7m** · total **1.014bn**
  - **FSO dual:** benefits **438.1m (2025)** with CoA periodisation **+113.0m** (58.5pct of rise); total exp **823.7m 2026** (divers **352m** class)
  - **Federal toelagen** dual I.3: **454.0m / 463.5m** 2025-26; federated share **55.7 / 60.6m** (RVA emp)
  - Asbestos: **3Q** employer contrib 2026; fed toelage **-3.7m**; medical RIZIV uplift **+20.4m** 2025 arrears path
- Wrote: sources +2; budgets +46; cmt +4; lb +8; FOI **gap_other_ss_l5_detail** ready+draft; rq_537=done spawn **rq_538**; ticks=546
- FOI opened: gap_other_ss_l5_detail (ready, human send) - not sent
- Next: prio5 **rq_538** (Part IV complete class → next public residual); deferred **rq_116** SWA; progress@550 in 4 ticks

### 2026-07-31T08:40:00Z - tick 547
- Unit: **rq_538** (FOI-adjacent hole-fill - **Kamer expose Part I §5 Table40 Entity I global investment effort 2025-29**)
- Found (strong primary DOC 56 1278/001 Part I §5; million-EUR table):
  - **Direct public invest:** 2025 **EUR 4.522bn** · 2026 **5.174** · 2027 **5.740** · 2028 **5.924** · 2029 **6.082**
  - **FOD/POD:** **2.972 → 4.962bn 2026** (defence-driven); **ESA defence corr −1.388bn 2026** (vs +175m 2025)
  - **ION/OIP:** **1.324 / 1.559bn** (Infrabel+Regie class); OISZ invest **51 / 40m**
  - **ESA GCF:** **5.914 → 6.612 → 7.204 → 7.438 → 7.632bn** (IT act **657m**, science **336m**, Infrabel+NIRAS **455m** flat)
  - **NMBS invest aid:** **1.049 / 1.094 / 0.776 / 0.697 / 0.712bn** 2025-29
  - **Gov-supported total:** **6.962 / 7.706bn** (1.1→**1.2% GDP**) → **8.344bn 2029**
- Wrote: sources +2; budgets +44; cmt +4; lb +8; FOI **gap_e1_invest_l5_codes** ready+draft; rq_538=done spawn **rq_539**; ticks=547
- FOI opened: gap_e1_invest_l5_codes (ready, human send) - not sent
- Next: prio5 **rq_539**; deferred **rq_116** SWA; progress@550 in 3 ticks

### 2026-07-31T08:45:00Z - tick 548
- Unit: **rq_539** (FOI-adjacent hole-fill - **Kamer expose Part I Tables29-32+34 Entity I nopol/measures/SPB/debt 2026-29**)
- Found (strong primary DOC 56 1278/001 Part I; billion-EUR tables):
  - **No-policy financing:** 2026 **-EUR 26.2bn** · 2027 **-29.4** · 2028 **-31.8** · 2029 **-39.1** (-5.4% GDP)
  - **After measures:** **-24.6 / -26.9 / -28.8 / -31.2bn** (-3.7 to -4.3% GDP)
  - **Measures impact:** **+1.6 / +2.4 / +3.0 / +8.0bn** on financing; unalloc **+0.5 → +1.5bn**
  - **Primary after:** **-12.5 / -13.0 / -13.0 / -13.4bn**; interest **12.2 → 17.8bn**
  - **SPB Table32:** **-12.9 / -12.8 / -12.8 / -12.5bn** (-1.9 to **-1.7% GDP**); only **+0.4bn** improve 29vs26
  - **Debt ratio Table34:** **85.6 → 87.1 → 88.8 → 90.3% GDP**; endogenous ~1.3-1.6pp/yr
  - **Dual:** E1 SPB stuck ~-1.7% vs MTFSP GG target **+0.6%** 2029
- Wrote: sources +3; budgets +56; cmt +4; lb +8; FOI **gap_e1_measures_delivery_l5** ready+draft; rq_539=done spawn **rq_540**; ticks=548
- FOI opened: gap_e1_measures_delivery_l5 (ready, human send) - not sent
- Next: prio5 **rq_540**; deferred **rq_116** SWA; progress@550 in 2 ticks

### 2026-07-31T08:50:00Z - tick 549
- Unit: **rq_540** (FOI-adjacent hole-fill - **expose Part I sensitivity Tables35-36 + SPB one-offs L5 + consol multi-year 2027-29**)
- Found (strong primary DOC 56 1278/001):
  - **Rate shock +100bp:** interest **+EUR 0.93 / 1.49 / 2.20 / 2.79bn** 2026-29 (0.14-0.39% GDP)
  - **Growth shock -0.5pp/yr:** financing hit **-1.4 / -2.9 / -4.6 / -6.4bn**; saldo after **-26.0 to -37.5bn**
  - **SPB Table7:** **-11.056bn 2025** (-1.7%) / **-11.601bn 2026** (-1.8%); cycle **-1014/-1303m**
  - **One-offs L5:** Belfius div **+500m** both yrs; BVH **-221**; BFW **-279/+234**; textile **-92**; tax-free **-159** 2026
  - **Consol ESA 2027-29:** **+1.098 / +1.209 / +0.981bn**; FPIM **610-650**; Hedera **381-465**; Infrabel **-119 to -96**; debt impact **~1.2-1.3bn**
  - Dual SPB T7 vs T32 ~**1.3bn** residual
- Wrote: sources +3; budgets +58; cmt +4; lb +8; FOI **gap_e1_sensitivity_oneoff_method** ready+draft; rq_540=done spawn **rq_541**; ticks=549
- FOI opened: gap_e1_sensitivity_oneoff_method (ready, human send) - not sent
- Next: prio5 **rq_541** = **progress@550 mandatory** on next tick; deferred **rq_116**

### 2026-07-31T08:55:00Z - tick 550
- Unit: **rq_541** (**progress@550** coverage % + waste top10; no new euro invent)
- Progress layers vs EUR **347.956bn** TE:
  - **A/B:** 100% (L0 TE + L1 subsectors)
  - **C L2:** ~**99%** (exposé Part III–IV dual + E1 invest/SPB/consol map)
  - **D L5:** ~**35-48%** generous (Part IV SS L5 close · other SS 1.57bn · E1 invest 7.7bn · nopol/SPB path · not near-complete of 348bn)
  - **E FOI ready:** ~**295** · answered ~**9** · total FOI rows ~**305**
- Inventory: budgets ~**9691** · cmt ~**1062** · lb ~**2022** · sources ~**1045** · entities ~**414**
- Waste top10: **unchanged** fossil/cars/cheque/consultancy (priority 8.55→8.30); just-outside + E1 nopol 39bn; high-abs Metro3/wassalon; stock dual pension 72bn · SPB · invest 7.7bn · sensitivity
- Gain 540→550: exposé residual close (C&R/EU/SS stacks · E1 capital+fiscal path · sensitivity/one-offs/consol multi-year)
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_541=done spawn **rq_542**; ticks=550
- FOI opened: none this tick
- Next: prio5 **rq_542**; deferred **rq_116** SWA

### 2026-07-31T09:00:00Z - tick 551
- Unit: **rq_542** (FOI-adjacent hole-fill - **expose Part II fiscal receipts Tables1-10 ESA/cash dual**)
- Found (strong primary DOC 56 1278/001 Part II Ch2; million-EUR):
  - **ESA fiscal total:** 2024 **EUR 155.889bn** · 2025 **158.100** · 2026 **163.806** (+5.706 / +3.6%)
  - **L5 2026 ESA:** BVH **66.841** · VAT **45.149** (pure **40.274**) · VenB **26.748** · RV **7.990** · excise **11.211** · customs **3.402**
  - **Cash dual:** third-party+assigned **92.508bn** · Middelen **65.435bn** 2026
  - **Tech factors:** Russian frozen CIT interest **-1.260 / +1.163bn**; VAT chain **+1.170bn** 2025; BVH reform **+221m**; HEDERA comps
  - **Dual Graph1:** fiscal **164.3** ~ ESA **163.8**
- Wrote: sources +2; budgets +46; cmt +4; lb +8; FOI **gap_fiscal_assignment_l5_2026** ready+draft; rq_542=done spawn **rq_543**; ticks=551
- FOI opened: gap_fiscal_assignment_l5_2026 (ready, human send) - not sent
- Next: prio5 **rq_543**; deferred **rq_116** SWA

### 2026-07-31T09:05:00Z - tick 552
- Unit: **rq_543** (FOI-adjacent hole-fill - **expose Table4 tax measures L5 + non-fiscal dual**)
- Found (strong primary DOC 56 1278/001 Part II):
  - **Table4 measures 2026 total:** **+EUR 1.585bn** (VAT pure **+511** · excise **+57** · divers **+1148**; BVH measures **-383**)
  - **L5 raisers:** TACT **+414** · CGT **+236** · interest-ded abolish **+203** · UI tax-relief end **+257** · hospitality VAT stack **633** · bank **150** · VVPR **90**
  - **L5 costs:** tax-free sum **-531** · author-rights IT **-142** · meal vouchers **-76** · demo/rebuild VAT **-124**
  - **Non-fiscal corrected:** 2025 **6.971bn** · 2026 **5.850bn** (−1.121); Finance **5.126** · SS **1.190→0.002**; sleeping assets **+475**; Fluxys **+100**; F35 hedge **+321**
- Wrote: sources +2; budgets +53; cmt +4; lb +8; FOI **gap_tax_measures_outturn_l5** ready+draft; rq_543=done spawn **rq_544**; ticks=552
- FOI opened: gap_tax_measures_outturn_l5 (ready, human send) - not sent
- Next: prio5 **rq_544**; deferred **rq_116** SWA

### 2026-07-31T09:10:00Z - tick 553
- Unit: **rq_544** (FOI-adjacent hole-fill - **CoA 2026_35 Flanders teacher AVB+professionalization L5**)
- Found (strong primary Rekenhof NL 30 Jun 2026):
  - **AVB path:** intro **EUR 31.0m** (2019-20) → **52.2m** 2024-25 (basis **30.5** · sec **21.6**); pupil-based not starter-based
  - **Induction:** envelope **48.7m** (not enough for 20% all starters); alt workings **38.7m** 2025-26; 2026-27 total ~**3x** intro class
  - **Professionalization:** **50.8 → 62.4m** 2020-25 (schools **44.9** · PBD **17.5** · priority themes **0**); **120-130 EUR**/relation
  - **Leerpunt:** **0.11 → 5.7m** 2022-25; specialist mandates **577** underused
  - **Governance:** no global AVB eval; AGODI no colored-use check; 8/80 schools no PD plan; dual FWB Cepage IT
- Wrote: sources +3; budgets +26; cmt +4; lb +8; FOI **gap_vl_avb_prof_outturn_l5** ready+draft; rq_544=done spawn **rq_545**; ticks=553
- FOI opened: gap_vl_avb_prof_outturn_l5 (ready, human send) - not sent
- Next: prio5 **rq_545**; deferred **rq_116** SWA

### 2026-07-31T09:15:00Z - tick 554
- Unit: **rq_545** (FOI-adjacent hole-fill - **expose Table11 A/B fiscal assignment by beneficiary cash**)
- Found (strong primary DOC 56 1278/001 Part II Table11; million-EUR cash):
  - **Total third-party+assigned 2026:** **EUR 92.508bn** (2025 91.100 · 2024 86.589)
  - **By beneficiary 2026:** EU **4.150** · Regions **25.600** · Communities **33.563** · SS **27.325** · divers **1.870**
  - **Communities:** PB **11.060** + VAT **22.504**; **Regions:** taxes **3.772** + PB share **7.539** + autonomy **14.288**
  - **SS alt fin L5:** emp **23.392** (RV **6.403** · VAT **13.275** · tobacco **2.774** · BVH **0.940**) · self **3.830** · BBSZ **0.102**
  - **Energy divers:** Elia **761.5** · CREG **512.4** · Hedera **148.7** (TACT+TBV+RV)
  - **Dual:** T11 C&R 59.2 vs Graph1 E2 81.5 perimeter; SS alt 27.22 dual Part IV/I.3
- Wrote: sources +2; budgets +40; cmt +4; lb +8; FOI **gap_fiscal_assignment_l5_2026** notes updated (matrix filled; residual per-region); rq_545=done spawn **rq_546**; ticks=554
- FOI: no new letter; partial fill existing gap - not sent
- Next: prio5 **rq_546**; deferred **rq_116** SWA

### 2026-07-31T09:20:00Z - tick 555
- Unit: **rq_546** (FOI-adjacent hole-fill - **CoA Flanders rekeningenrapport 2025**)
- Found (strong primary Rekenhof 30 Jun 2026 / 2026_32):
  - **Financing saldo 2025:** **-EUR 3.982bn** (budget **-4.504**; 2024 **-4.101**); clean ESR consol opinion
  - **Maastricht debt:** **50.172bn** eoy2025 (**+8.383** from 41.789); excess vs BA **1.889** from **PMV Zaventem 2.554bn**
  - **Ministry ESA:** rec=exp **80.316bn**; contribution to saldo **20.868bn**
  - **Credit carry to 2026:** **1.415bn** (into 2025: 1.255); **Relance:** spend **399m** 2025; cum commit **4.2** / paid **3.5** / open **0.7bn**
  - **Balance gaps:** missing land/buildings ~**1.6bn**; art **1.4bn**; Zandvliet wrong **367m**; FWO/FIO commit adj **562+189m**
  - Opinions: economic **disclaimer** · budget **qualified** · ESA/consol **clean**
- Wrote: sources +3; budgets +24; cmt +4; lb +8; FOI **gap_vl_accounts_balance_l5** ready+draft; rq_546=done spawn **rq_547**; ticks=555
- FOI opened: gap_vl_accounts_balance_l5 (ready, human send) - not sent
- Next: prio5 **rq_547**; deferred **rq_116**; progress@560 in 5 ticks

### 2026-07-31T09:25:00Z - tick 556
- Unit: **rq_547** (FOI-adjacent hole-fill - **CoA 2026_32 residual Lantis NEC4 + open verbintenissen + TV financing**)
- Found (strong primary Rekenhof rekeningenrapport 2025 residual L5; million-EUR):
  - **Lantis under-vastlegging:** approved NEC4 bids **EUR 7.469bn**; prior **2.891bn**; needed extra **4.578bn**; booked only **+2.159bn** (tol share) → shortfall **~2.419bn**; BA2026 extra kredieten
  - **Open verb toelage Table10 2025:** total **7.372bn** (2024 6.831): VMSW **1.745** · FIO **1.505** · De Lijn **0.941** · FWO **0.879** · VAPH **0.788** · AGIOn **0.591** · DVW **0.468** · VWF **0.457**
  - **Outside table:** ~**5.5bn** other open verb of which BAM **~4.5bn**; contracts **6.8bn** JV2025
  - **TV financing Table23 eoy2025 cum ~3.852bn:** cash **885** · natura **287** · land **176** · loans **2.401** · overkapping **102**; loans path **250/950/1.128**; plafond **6.7bn** @ **5%** subord
  - **New LT loans 2025 3.955bn:** VWF **1.550** · Lantis **1.128** · VMSW **1.000** · Roadrunner **216**; fin assets **+5.686bn**
  - **Internal toelage imbalance 70.8m** on ~27bn eliminated streams; **central financing stock 17.464bn**; GO! patrimony **1.004bn** inventory gap
- Wrote: sources +2; budgets +44; cmt +4; lb +8; FOI **gap_lantis_vastleg_nec4_l5** ready+draft; rq_547=done spawn **rq_548**; ticks=556
- FOI opened: gap_lantis_vastleg_nec4_l5 (ready, human send) - not sent; related gap_lantis_oosterweel_cash / gap_vl_debt_nonbudget_bridge_l5 still ready
- Next: prio5 **rq_548**; deferred **rq_116**; progress@560 in 4 ticks

### 2026-07-31T09:30:00Z - tick 557
- Unit: **rq_548** (FOI-adjacent hole-fill - **CoA 2026_32 residual relance underuse L5 + PAS/REPowerEU + VLAIO recovery**)
- Found (strong primary Rekenhof RR2025 §4.3-4.5; million-EUR):
  - **Relance 2025:** raming **741.5** / spend **399.4** / underuse **342.1** (Table39): VV014 **92.2** · VV047 **34.4** · VV048 **20.2** · VV013 **18.9** · VV022 **17.3** (bankrupt 11) · VV018 **12.5** · VV017 **10.3**
  - **Open to liq Table40 ~664m class:** VV014 **92.2** · VV047 **87.1** · VV110 **57.5** · VV013 **48** · VV099 **48.1** (+Andere **331**); cum open **0.7bn**; deadline **30 Jun 2026** EU; PMV biotech realloc **39.8**
  - **REPowerEU:** **208→191.4** (-16.6); paid cum **107.7** (2025 **72.2**); residual ~**83.7** for 2026; VAK lapse **27.5**
  - **PAS stikstof:** envelope **3.649bn** 2022-30; 2025 available **434.3** redistrib VAK **186.5** / VEK **85.2**; carry **244.3**; underuse VEK **114.3**
  - **Idle/ops:** overkapping wrong carry **39.5**; spoor cofin idle **108.1** since 2018; culture infra +**100** commit **43.1** carry **76.9**
  - **VLAIO Table41 2025:** support **971.1** · recoveries **50.8** · receivables **125.6** · impaired **93.5** · writeoffs **26.1**; corona 2020-21 **1896+740**; Table42 paid **2627.6** inspect **15%** recover after annul **196.5**
- Wrote: sources +2; budgets +53; cmt +6; lb +8; FOI **gap_vlaio_recovery_kpi_l5** ready+draft; rq_548=done spawn **rq_549**; ticks=557
- FOI opened: gap_vlaio_recovery_kpi_l5 (ready, human send) - not sent; gap_vl_accounts_balance_l5 notes partial fill
- Next: prio5 **rq_549**; deferred **rq_116**; progress@560 in 3 ticks

### 2026-07-31T09:35:00Z - tick 558
- Unit: **rq_549** (FOI-adjacent hole-fill - **CoA 2026_32 residual dual gemengde entiteiten + VLAIO eco/print + GO inventory**)
- Found (strong primary Rekenhof RR2025 §4.5-4.7; million-EUR):
  - **VLAIO residual:** drukkerij eco claims ~**22** (repaid **7.8**; **12.6** in 2020; 129 dossiers/59 firms); corona+eco receivables **85.6** (half collectible long); CIC collect **2.7/5.4** 2023-24; prescription writeoffs **8.5+7.9**; fraud dading **12.7** recollected full; impaired corona **43.7** eco **26.9**
  - **GO!:** book **1.004bn** (79pct balance); ~**4000** buildings; inventory unmatched multi-year; target **30 Jun 2026**; ~200 zakelijke rechten open
  - **Dual gemengd Apr2026:** **66** entities (**21** S13 / **45** firms); Ethias cluster **34** (VL/FPIM/WE each **31.66%**); Ethias VL book **740.7** (econ **753.4** from inject **500** 2008); BAC Zaventem dual FPIM **25%**+VL 2025; Viapass collect ~**710** VL fee **102.3**; AB ~**3** Flagey ~**1.5**; De Lijn BMC **18.6%**
- Wrote: sources +2; budgets +26; cmt +6; lb +8; FOI **gap_dual_gemengd_l5** ready+draft; rq_549=done spawn **rq_550**; ticks=558
- FOI opened: gap_dual_gemengd_l5 (ready, human send) - not sent; gap_vlaio_recovery_kpi_l5 notes partial
- Next: prio5 **rq_550**; deferred **rq_116**; progress@560 in 2 ticks

### 2026-07-31T09:40:00Z - tick 559
- Unit: **rq_550** (FOI-adjacent hole-fill - **CoA 2026_03 antibiotics prescribing follow-up + dual RIZIV/FAGG**)
- Found (strong primary Rekenhof AG 7 Jan 2026):
  - **AMR social cost BE:** **EUR 281m/yr** (ECDC **24 EUR**/cap): health **158m** (56%) / economic **122m** (44%); hundreds deaths/yr
  - **Reimbursed AB:** **-8%** doses and patients (Jun2024-May2025 vs 2019); 2019-23 reimb **-3.2%** / all **-2.4%**
  - **Non-reimb share:** **11→12%** 2019-23 outside RIZIV control; quinolones **61→66%** non-reimb; 3rd-gen ceph **87%** outside rules
  - **Prescribers:** GP doses **-2.6%** vs all **-0.6%**; other prescribers **25%** of reimbursed; indicators GP-heavy
  - **EU:** BE rank **21/27** ascending use; NL use **2.6x** lower 2019; recs **6** done / **10** progress / **2** not / **2** NA
  - **Refine dual:** Viapass Table43 ~**105m** VL stream; Zonienwoud ~**155k**/yr
- Wrote: sources +3; budgets +18; cmt +3; lb +6; FOI **gap_ab_spend_l5** ready+draft; raw PDFs; rq_550=done spawn **rq_551**; ticks=559
- FOI opened: gap_ab_spend_l5 (ready, human send) - not sent
- Next: prio5 **rq_551** = **progress@560 mandatory** on next tick; deferred **rq_116**

### 2026-07-31T09:45:00Z - tick 560
- Unit: **rq_551** (**progress@560** coverage % + waste top10; no new euro invent)
- Progress layers vs EUR **347.956bn** TE:
  - **A/B:** 100% (L0 TE + L1 subsectors)
  - **C L2:** ~**99%** (fiscal assignment dual + VL accounts/debt + dual gemengd map)
  - **D L5:** ~**36-49%** generous (Part II fiscal L5 · VL RR residual Lantis/open-verb/relance/VLAIO · dual Ethias/Viapass/BAC · AMR 281m · not near-complete of 348bn)
  - **E FOI ready:** ~**301** · answered ~**9** · total FOI rows ~**313**
- Inventory: budgets ~**10032** · cmt ~**1104** · lb ~**2092** · sources ~**1069** · entities ~**414**
- Waste top10: **unchanged** fossil/cars/cheque/consultancy (priority 8.55–8.30); stocks Metro3 still top raw prio but annual=0 filtered; high-abs Lantis 2.42bn · VLAIO prescription · AB non-reimb · GO inventory · AMR 281m
- Gain 550→560: expose fiscal Part II (164/92.5bn) · CoA VL RR residual (debt 50.2 · Lantis 2.42 · open verb 7.37 · relance 342m · VLAIO · dual 66 gemengd) · antibiotics AMR 281m dual non-reimb
- Wrote: progress_every_10_ticks.md + doge_waste_top10_current.md; rq_551=done spawn **rq_552**; ticks=560
- FOI opened: none this tick
- Next: prio5 **rq_552**; deferred **rq_116** SWA

### 2026-07-31T09:50:00Z - tick 561
- Unit: **rq_552** (FOI-adjacent hole-fill - **RIZIV care outturn 2025 + FPB PROMES 2025-35 + AB cash 67m**)
- Found (strong primary RIZIV press 13 Apr 2026 + 11 Mar 2026 + FPB PROMES 28 Apr 2026):
  - **RIZIV care 2025:** authorized **EUR 39.712bn**; undershoot **201.2m** (0.5%); unfinished measures **+28.6** (counterfactual undershoot **172.6**)
  - **Over:** verpleegdag **+121.0** · pharma net **+104** (art81/111 receipts **-145.7**; clawback **85.4**)
  - **Under:** artsen **-17.4** on **11.644bn** · thuisverpl **-95.6** · implant **-81.3** · psych **-64.4** · MAF **-36.0**
  - **PROMES ZIV real:** **37.666bn** 2025 (6% GDP) → **48.599** 2035 (**+10.933**, **2.6%/yr**); pharma net **+3.412** · artsen **+2.182** · verpleegdag **+2.057** · thuis **+0.869**; demo **32%** of growth
  - **AB cash:** open-pharm reimb **~67m** 2024; patients/volume **-14%**; GP volume thresholds **46/43%** (was 39/38); quality pure amox **16%** / 2nd-line **11%** only
  - **Dual:** RIZIV auth **39.7** vs PROMES **37.7** ~**2bn** perimeter class
- Wrote: sources +4; budgets +38; cmt +4; lb +8; FOI **gap_riziv_sector_audit_2025** ready+draft; gap_ab_spend notes partial; rq_552=done spawn **rq_553**; ticks=561
- FOI opened: gap_riziv_sector_audit_2025 (ready, human send) - not sent
- Next: prio5 **rq_553**; deferred **rq_116**; progress@570 in 9 ticks

### 2026-07-31T09:55:00Z - tick 562
- Unit: **rq_553** (FOI-adjacent hole-fill - **VDAB Jaarverslag 2025 dual PES staff/savings/volumes**)
- Found (strong primary VDAB JV2025 PDF):
  - **Staff eoy2025:** **4.630** employees (prior class **4.761**; ~**-131**); prior legisl personnel save **EUR 22m** / **422** FTE
  - **Savings Focus op de kern:** **20m** 2025 · **25m** 2026 · **40m** 2027 (4 axes beleid/werking/personeel/invest); PMO projects **200→150**
  - **WZW Flanders eoy2025:** **224.630** rate **6.9%** (was 6.6): UI **117.500** · non-active **93.042** · BIT **11.057** · other **3.031**; rate ex-nonact **4.1%**
  - **Flows:** vac filled **36.536** · training starts **34.061** · non-active reach **212.036** (to work **69.348**) · to work Oct24-end25 **209.638** · NECzU vac **271.072** (-10%) · classic train **28.894** · knelpunt stream ~**21.000**
  - **Context:** VL employment rate **77.3%** (74.7 in 2020); dual Actiris/FOREM matching; BBT VEK **750.7m** 2026 still; full TCO residual FOI
- Wrote: sources +2; budgets +29; cmt +3; lb +7; FOI **gap_vdab_jaarrekening_2025** ready+draft; gap_vdab_full_budget notes; raw PDF; rq_553=done spawn **rq_554**; ticks=562
- FOI opened: gap_vdab_jaarrekening_2025 (ready, human send) - not sent
- Next: prio5 **rq_554**; deferred **rq_116**; progress@570 in 8 ticks

### 2026-07-31T10:00:00Z - tick 563
- Unit: **rq_554** (FOI-adjacent hole-fill - **ONEM/RVA RA2025 missions budget + dual PES UI reform**)
- Found (strong primary ONEM RA2025 vol1 Tables 1.4.6 + press):
  - **Global 2025:** exp **EUR 7.371bn** / rec **7.344bn** / saldo **-27.3m**
  - **Missions exp 6.951bn** (+**350.15m** +5.3%): social benefits **6.383bn** (+0.32%) · OP indemnisation **233.6m** (−0.59%) · diverses **333.8m** (+12.0%)
  - **Gestion 306.6m** (+11.4m): personnel **236.0m** (77%) · fonctionnement **65.8m** · invest **4.4m**
  - **Volumes:** full UI avg **288.077** (+1.13%) · temp UI **−20.2%** · career interrupt **244.023** · total recipients **726.387** (−2.9%) · bankruptcies **11.675** / jobs lost **34.238** · reform end-rights ~**173k**
  - **Service:** process 14d **90.03%** (was 99.8) · quality **96.07%** · eC3 **>2.1m** payments · dual partners VDAB/FOREM/Actiris/ADG/OP/CPAS
- Wrote: sources +3; budgets +32; cmt +3; lb +8; FOI **gap_onem_op_union_l5_2025** ready+draft; gap_unemp_pay_unit_cost notes; raw PDF; rq_554=done spawn **rq_555**; ticks=563
- FOI opened: gap_onem_op_union_l5_2025 (ready, human send) - not sent
- Next: prio5 **rq_555**; deferred **rq_116**; progress@570 in 7 ticks

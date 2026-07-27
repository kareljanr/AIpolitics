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

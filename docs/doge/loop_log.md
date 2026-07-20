# DOGE loop log

Append-only. Each tick adds a short entry.

---

## Template

```text
### YYYY-MM-DDTHH:MM:SSZ — tick N
- Unit: [task_id / gap_id]
- Found: …
- Wrote: [files/rows]
- FOI opened: [gap_id or none]
- Next: …
```

---

## Entries

### 2026-07-19T00:00:00Z — bootstrap
- Unit: scaffold
- Found: strategy + schema + queues created
- Wrote: docs/06b, docs/doge/*, data CSVs seeded
- FOI opened: gap_example_001 (cancelled example only)
- Next: rq_001 L0 general government total

### 2026-07-19T12:00:00Z — tick 1
- Unit: rq_001 (L0 general government expenditure)
- Found: NAI/NBB EDP press release 2026-04-20 Table 1 — 2025 total expenditure **€347,956 million** (54.2% of GDP); primary **€333,675 million** (52.0% GDP); GDP €642,015 million. 2024 total €335,100 million (54.1% GDP). Strong confidence, preliminary ESA estimate.
- Wrote: budgets.csv (4 rows); sources.csv (+src_nbb_edp_2025_apr); research_queue rq_001=done; loop_state ticks=1
- FOI opened: none (L0 fully sourced from public EDP tables)
- Next: rq_002 L1 split by subsector (EDP PR has deficits by subsector, not full expenditure — need NBB.Stat/COFOG)

### 2026-07-19T12:30:00Z — tick 2
- Unit: rq_002 (L1 expenditure by ESA subsector)
- Found: Eurostat `gov_10a_main` TE MIO_EUR BE (updated 2026-04-22, provisional). **2025 unconsolidated TE:** S.1311 central **€181,526.1m**; S.1312 state **€128,623.8m**; S.1313 local **€44,986.7m**; S.1314 SS **€141,680.4m**. Sum ≈ €496.8bn vs consolidated S.13 **€347.956bn** — gap ≈ intergovernmental transfers (double-count if summed). 2024: 171675 / 125077 / 44491 / 135689 m EUR.
- Wrote: budgets.csv (+8 L1 rows); entities.csv (sec_s1312 + parent links); sources.csv (+src_eurostat_gov_10a_main_te); rq_002=done; ticks=2
- FOI opened: none (public Eurostat)
- Next: rq_003 top 15 spending entities (L2)

### 2026-07-19T13:00:00Z — tick 3
- Unit: rq_003 (top 15 spending entities / holders)
- Found (mixed metrics — do not sum): ESA sectors 181.5 / 141.7 / 128.6 / 45.0 bn (2025 TE); **Flanders BO2026 uitgaven €66.0 bn**; **RIZIV global €45.222 bn** / care auth. **€39.712 bn** (2025); **Wallonia initial 2025 €22.029 bn**; FWB ~**€15 bn** (medium); GG interest **€14.282 bn**; defence COFOG **€8.8 bn**. Ranks 12–15 Unknown (Brussels city/ministries).
- Wrote: entity_rank_snapshot.csv; budgets.csv (+7); entities updates; sources (+5); rq_003=done; mode→sprint2_taxex; ticks=3
- FOI opened: gap_bru_total_2025 (draft letter; not ready — missing recipient contacts)
- Next: rq_004 FPS tax expenditure inventory

### 2026-07-19T13:30:00Z — tick 4
- Unit: rq_004 (FPS federal tax expenditure inventory)
- Found: Downloaded official XLSX (123619 bytes). Parsed 171 measures with latest-year values. **Top by €m:** CIT DTR **21936**; VAT basic necessities **10589**; CIT FDI capital gains **7193**; PIT pensions **4679**; VAT construction **3261**; CIT losses **1355**; **excise heating gas oil 1333**; CIT innovation **1208**; VAT horeca **1199**; … (years differ: PIT/WT 2026, EIWT/EXC 2024, CIT/VAT 2023).
- Wrote: tax_expenditures.csv (top 20); raw/fps_taxex.xlsx + parse + parsed csv; leaderboard 3 seeds (heat oil, horeca VAT, pro diesel); sources src_fps_taxex_xlsx; rq_004=done; ticks=4; mode sprint3_flanders
- FOI opened: none
- Next: rq_005 Flanders budget top 10 programmes

### 2026-07-19T14:00:00Z — tick 5
- Unit: rq_005 (Flanders top programmes / beleidsdomeinen)
- Found: Centenboekje BO2026 (22.09.2025) Tables 4-1/4-2 **constant policy** VEK BO2026 (kEUR): **OV 20,265,810**; **WVG 17,970,605**; KBBJ 6,121,075; MOW 6,030,176; WEWIL 6,004,185; FB 4,758,451; Omgeving 3,503,778; CJSM 1,738,752; HE 178,367; **total VEK 66,571,199**. Oosterweel correctie **889,859** kEUR. Note: DFB site headline 66.0 bn after measures; table is excl. new measures.
- Wrote: programmes.csv (12 rows); raw/vl_bo2026.pdf; sources src_vl_centenboekje_bo2026; rq_005=done; ticks=5
- FOI opened: none (public PDF)
- Next: rq_006 Flanders L5 discretionary (culture/equality/comms)

### 2026-07-19T14:30:00Z — tick 6
- Unit: rq_006 (Flanders L5 discretionary sample)
- Found: **VRT basistoelage €296.4m/yr** (BHO 2026–2030; PQ 296.400 kEUR). **Jobbonus €228m** VEK BO2026. **Oosterweel €889.9m** BO2026 line. **Relance VV €436.4m**. Dienstencheques **€151.4m reform line** (not full TCO). Subsidy-efficiency package **€350m** cuts. Culture/equality L5 beneficiaries not in public top lists this tick.
- Wrote: commitments.csv (6); leaderboard +3 (VRT, Jobbonus, VV); FOI drafts gap_vl_cjsm_l5, gap_vl_gelijke_kansen, gap_vl_dienstencheques_tco; sources; rq_006=done; ticks=6; mode sprint4_federal
- FOI opened: 3 new drafts (not ready — contacts TBD)
- Next: rq_007 federal cabinet / communication costs

### 2026-07-19T15:00:00Z — tick 7
- Unit: gap_vl_cjsm_l5 (FOI draft finish — priority 8 before research)
- Found: Official Flanders FOI channel — **Team Openbaarheid van Bestuur**, **openbaarheid@vlaanderen.be**, Herman Teirlinckgebouw Havenlaan 88 bus 20, 1000 Brussel (vlaanderen.be openbaarheid page).
- Wrote: complete send-ready letter `foi/drafts/gap_vl_cjsm_l5.md`; foi_queue status **ready** (not sent); sources src_vl_openbaarheid_contact; ticks=7
- FOI opened/updated: gap_vl_cjsm_l5 → ready; human must fill identity and send
- Next: other prio-8 FOI drafts (dienstencheques) or rq_007 federal cabinets

### policy — commit/push each tick
- LOOP.md §6 and doge-loop skill require **git commit + push** after every tick that changes files.
- Old scheduler 019f7a359ff7 cancelled; then 019f7af13075 (30m); now **019f7c315adb every 15m** with commit/push.

### 2026-07-19T15:30:00Z — tick 8
- Unit: gap_vl_dienstencheques_tco (FOI draft finish — priority 8)
- Found: Public sources still lack a clean single **full TCO** figure (only reform lines e.g. 151.4m BO2026; measure tables for price/tax changes). Routed via **openbaarheid@vlaanderen.be**.
- Wrote: full send-ready letter; foi_queue status **ready**; loop_state ticks=8
- FOI: gap_vl_dienstencheques_tco → ready (not sent)
- Next: rq_007 federal cabinet / communication costs

### 2026-07-19T16:00:00Z — tick 9
- Unit: rq_007 (federal cabinets + comms overhead)
- Found: Belga/Brussels Times (2025-02-14): **30% cabinet cut ≈ €21m/yr** → implied baseline **~€70m** (medium). FTE **838 → 586** target. No consolidated federal **communication** total found.
- Wrote: overhead_nodes.csv (3 rows); leaderboard lb_fed_cabinets; FOI gap_fed_cabinets_comms ready; sources; rq_007=done; ticks=9; mode sprint5_local
- FOI: gap_fed_cabinets_comms → ready (federal form; not sent)
- Next: rq_008 City Ghent project subsidies

### 2026-07-19T16:30:00Z — tick 10
- Unit: rq_008 (Ghent L5 subsidies)
- Found: **NTGent** werkings **€2,327,728** + investering **€260,000**/yr (HLN). Structural culture **~€8m/yr** for **28** orgs. Culture pot **~€10m/yr** after **€1.4m** cut. MJP: **€120m/yr** operating savings target + **€1bn** investments multi-year.
- Wrote: commitments +4; budgets +2; leaderboard +2; FOI gap_gent_subsidies_top20 ready; sources; rq_008=done; ticks=10; mode sprint6_overhead
- FOI: gap_gent_subsidies_top20 → ready (not sent)
- Next: rq_009 dual-structure overhead catalogue

### 2026-07-19T17:00:00Z — tick 11
- Unit: rq_009 (dual-structure overhead catalogue)
- Found: **VRT €296.4m + RTBF ordinary €350.8m ≈ €647.2m** dual PSB (strong). Dual education communities (Flanders OV ~€20.3bn; FWB total ~€15bn partial). Multi-parliaments (cost TBD). Dual PES VDAB/FOREM/Actiris (TBD). Multi-layer econ agencies (TBD). ESA unconsolidated subsector sum premium **~€148.9bn** vs S.13 (transfer double-count scale — not cash waste).
- Wrote: overhead_nodes 9 rows; leaderboard lb_dual_psb; FOI gap_multi_parliaments draft; sources; rq_009=done; ticks=11
- FOI: gap_multi_parliaments draft (not ready)
- Next: rq_010 multi-year commitments seed check

### 2026-07-19T17:30:00Z — tick 12
- Unit: rq_010 (multi-year commitment models)
- Found/modelled: Full **cash_by_year** JSON on multi-year rows — **VRT 2026–2030** flat 296.4m; **RTBF** 350.8m (3y illustrative); **RRF BE** 5.3bn planned / 3.3bn disbursed end-2025; **NTGent** + **Gent 28 orgs** 6y flat; Gent savings 120m×6. Single-year lines retained. Flat years tagged ILLUSTRATIVE where not year-stamped in source.
- Wrote: commitments.csv rewrite (12 rows); rq_010=done; new queue rq_011–rq_014; ticks=12
- FOI: none new
- Next: rq_013 company-car taxex (prio 8) or rq_011 Wallonia L5

### 2026-07-19T18:00:00Z — tick 13
- Unit: rq_013 (company car tax expenditure)
- Found: Tax Foundation Europe (2025 research citing EU data): Belgium company-car **tax expenditures €2.3 bn in 2024** (0.37% GDP; 3.2% of federal TE; 13.2% of labour TE). FPS inventory export lacks a single full package line (only residual e.g. CIT business-car CG €12.4m; PIT electric cars €0.85m).
- Wrote: tax_expenditures +3; leaderboard **lb_company_cars** priority_index 8.15; sources; rq_013=done; ticks=13
- FOI: none (secondary source strong enough for seed; FPS micro-lines documented)
- Next: rq_011 / rq_012 / rq_014 (prio 7)

### 2026-07-19T18:30:00Z — tick 14
- Unit: rq_011 (Wallonia L5 sample)
- Found: **AWEX €76m** constant budget; **facultative subsidies −€8m** (2026); **structural savings €270.4m** (2026); **TEC/OTW €45m** cited (medium); **APE savings ~€83m** order (medium understatement). Wallonia total dépenses initial 2025 already in budgets (€22.03bn).
- Wrote: commitments +5; leaderboard lb_awex; FOI gap_wal_l5_top_subsidies draft; sources; rq_011=done; ticks=14
- FOI: gap_wal_l5_top_subsidies draft
- Next: rq_012 or rq_014

### 2026-07-19T19:00:00Z — tick 15
- Unit: rq_012 (VDAB / FOREM / Actiris budgets)
- Found: **Actiris €727m (2025) → €689m (2026)** after €38m cut (strong). **VDAB** savings path **€20m (2025) → €40m (2027 accelerated) → €80m by 2028**; total budget **~€790m medium** (10%/~€79m inference). **FOREM** total not found → FOI.
- Wrote: entities vdab/forem/actiris; budgets; commitments; overhead dual PES partial; leaderboard lb_actiris; FOI gap_forem + gap_vdab_full; sources; rq_012=done; ticks=15
- FOI: gap_forem_budget draft; gap_vdab_full_budget draft
- Next: rq_014 FOI gelijke kansen

### 2026-07-19T19:30:00Z — tick 16
- Unit: user priority middleman systems + rq_014 FOI ready
- Found/doctrine: **Cheque economy** (eco/meal/restricted vouchers) = state/tax favours pay that only buys limited goods + issuer sandwich — default should be **cash wages**. **Union-channelled chômage** = public benefit paid via multi-cashier private/associative channels — core state task; need unit-cost FOI. FPS inventory parse lacks clear meal/eco-cheque TE package line.
- Wrote: `notes-middleman-systems.md`; leaderboard lb_cheque_economy + lb_union_unemp_pay; taxex stub tx_cheques_package_tbd; FOI gap_cheque_te + gap_unemp_pay_unit_cost drafts; gap_vl_gelijke_kansen **ready**; rq_014=done; rq_015/rq_016 queued prio9; link from 06-doge; ticks=16
- FOI: gelijke kansen ready; cheque TE + unemp pay drafts
- Next: rq_015 cheque TE deep dive (prio 9)

### 2026-07-19T20:00:00Z — tick 17
- Unit: rq_015 (cheque economy TE inventory)
- Found: Meal vouchers **SSC+PIT exempt** (conditions); max **EUR 10/day from 2026** (employer to 8.91). Eco-cheques **max EUR 250/yr** tax+SSC free restricted. Market volume meal vouchers **~EUR 3bn/yr** (medium industry claim ~3m users). **Official fiscal TE still unknown** in FPS inventory export. Abolition of eco-cheques discussed in policy commentary.
- Wrote: taxex rows; leaderboard update; FOI gap_cheque_te **ready**; notes-middleman findings table; sources; rq_015=done; ticks=17
- FOI: gap_cheque_te ready (not sent)
- Next: rq_016 unemployment payment unit costs

### 2026-07-19T20:30:00Z — tick 18
- Unit: rq_016 (unemployment payment channels)
- Found: Architecture confirmed — benefits paid via **union payment funds** or **Hulpkas**. Hulpkas **admin budget 2025 = €6,084,000** (strong official). Benefit stock separate from cashier admin. Union-fund public admin grants and **unit cost/dossier** still unknown → FOI ready.
- Wrote: entities hulpkas/onem_rva; budgets; commitment; leaderboard update; FOI gap_unemp_pay_unit_cost **ready**; notes update; sources; rq_016=done; ticks=18
- FOI: gap_unemp_pay_unit_cost ready (not sent)
- Next: queue empty of open research — spawn continuous tasks or work FOI draft backlog

### 2026-07-19T21:00:00Z — tick 19
- Unit: rq_017 (Brussels BCR total expenditure)
- Found: Cour des comptes report 13 Mar 2026 — SGRBC **crédits de liquidation €8.0 bn**, **engagement €8.9 bn** (2026). Major liquidation lines: **STIB €1.168 bn**; pouvoirs locaux €758m; commissions communautaires €692m; **Actiris programme €648m**; dette €728m; titres-services €304m. SEC financing balance after ops **−€956.6 m**.
- Wrote: budgets; entity_rank #12; commitments STIB + titres-services; leaderboard lb_stib; FOI gap_bru **answered**; raw PDF; sources; rq_017=done; ticks=19
- FOI: gap_bru_total answered (OAA full consolidate still noted open)
- Next: rq_018 FOI batch or rq_019 leaderboard recompute

### 2026-07-19T21:15:00Z — tick 20
- Unit: rq_018 (FOI drafts → ready batch)
- Found/done: Completed send-ready letters for **gap_multi_parliaments**, **gap_wal_l5_top_subsidies**, **gap_forem_budget**, **gap_vdab_full_budget**. gap_bru already answered. All high-value FOI now **ready** (not sent — human).
- Wrote: 4 FOI draft files; foi_queue status updates; rq_018=done; ticks=20
- FOI ready stack: cjsm, gelijke kansen, dienstencheques, cabinets, gent top20, multi-parliaments, wal L5, forem, vdab, cheque TE, unemp pay
- Next: rq_019 leaderboard recompute

### 2026-07-19T21:30:00Z — tick 21
- Unit: rq_019 (leaderboard recompute)
- Found: Recomputed cost_score from € bands + priority_index for all rows; sorted CSV. **Top 5:** cheque economy 8.68 · heating oil 8.33 · company cars 8.22 · VAT horeca 7.73 · pro diesel 7.22. Snapshot `data/leaderboard_top15.md`.
- Wrote: leaderboard.csv sorted; leaderboard_top15.md; recompute script; rq_019=done; rq_020–022 queued; ticks=21
- FOI: none
- Next: rq_021 meal voucher TE secondary (prio 8)

### 2026-07-19T21:45:00Z — tick 22
- Unit: rq_021 (meal voucher fiscal cost secondary)
- Found: Sofie De Coster thesis (via De Standaard): meal vouchers **~EUR 1.4bn/yr fiscal cost** (medium). Market volume still ~3bn. Expansion scenarios cited ~1bn extra. Official FPS TE still FOI.
- Wrote: taxex tx_meal_vouchers_fiscal_1_4bn; leaderboard lb_cheque_economy annual=1.4bn; sources; notes update; rq_021=done; ticks=22
- FOI: gap_cheque_te remains ready
- Next: rq_020 Oosterweel multi-year or rq_022 Antwerp

### 2026-07-20T00:15:00Z — tick 23
- Unit: rq_020 (Oosterweel multi-year envelope)
- Found: Full project cost **~EUR 7.2 billion** (VRT NWS 2024 class / press consensus). Annual BO2026 correction line remains **€889.859m** (centenboekje) — not the full TCO.
- Wrote: commitments cmt_oosterweel_total + refined annual line; leaderboard lb_oosterweel; sources; rq_020=done; ticks=23
- FOI: none
- Next: rq_022 Antwerp L5 sample

### 2026-07-20T00:30:00Z — tick 24
- Unit: rq_022 (Antwerp L5 sample)
- Found: MJP **opex €2.2–2.4bn/yr**, **invest €2.4bn / 6y (€400m/yr)**. Gemeentefonds **€807.2m** (2024). Toneelhuis city subsidy **€2.74m/yr** (to 2025). Safety domain **~1/5 budget** (~€460m order, medium secondary).
- Wrote: budgets; commitments; leaderboard lb_antwerp_opex; FOI gap_antwerp_subsidies_top20 ready; sources; rq_022=done; ticks=24
- FOI: gap_antwerp_subsidies_top20 ready
- Next: queue empty — spawn more continuous tasks or idle_waiting_foi
- Note: tick 24 data was left uncommitted after research_queue wipe (permission error); restored queue + committed with tick 25.

### 2026-07-20T00:40:00Z — tick 25
- Unit: rq_023 (Federal toelagenregister + NMBS PSO financing)
- Found: BOSA/VRT **federaal toelagenregister** — **8 993 items / €179.916 bn** federal transfers 2025 (not full federal spend). **Facultatieve subsidies ~€900m**; structural cut target **−€200m from 2029**. NMBS press 2025: **rail-sector savings €675m (2025–2029)**; debt €1.532 bn; EBITDA €54.2m; **annual state exploitatievergoeding EUR total still not in public press**. 2026 rail cut **€100m** (SNCB 60% / Infrabel 40%, Belga).
- Wrote: entities nmbs+infrabel; budgets; commitments; leaderboard lb_fed_facultative + lb_nmbs_pso_opacity; FOI gap_nmbs_annual_toelage ready; sources; rq_022 marked done; rq_023=done; queued rq_024–026; ticks=25
- FOI: gap_nmbs_annual_toelage ready (not sent)
- Next: rq_024 De Lijn annual subsidy or rq_026 NBB 25bn enterprise subsidies

### 2026-07-20T01:00:00Z — tick 26
- Unit: rq_024 (De Lijn Flanders annual subsidy)
- Found: Official De Lijn press 2025: **dotatie −€27.5m** (absolute total not stated); surplus **€20k**; ticket revenue **+~10%**; passengers **372.9m**; Vlaamse extra **€400m e-buses** (652 ordered); imposed savings **€35.5m** + internal hefbomen **€45m** recurrent 2026; fare-control revenue target **€50m** 2026. Secondary press: **~€1.14 bn** dotatie “vorig jaar” (2023 class, medium). Jaarverslag PDF URL public but download **403** this tick.
- Wrote: entity de_lijn; budgets; commitments; leaderboard lb_de_lijn_dotatie; FOI gap_de_lijn_dotatie ready; sources; rq_024=done; ticks=26
- FOI: gap_de_lijn_dotatie ready (not sent)
- Next: rq_026 NBB 25bn enterprise subsidies (prio 7) or rq_025 Liège L5

### 2026-07-20T01:20:00Z — tick 27
- Unit: rq_026 (NBB enterprise subsidies 25bn deep dive)
- Found (NBB Economic Review 2025/9, strong): **€25.1 bn** subsidies+investment grants to enterprises in **2024 (4.1% GDP)**. Split: **fed+SS subsidies €10.3 bn**; **C+R subsidies €11.3 bn**; **C+R inv. grants €2.1 bn**; **fed inv. grants ~€0.9 bn**. Flanders **~€6.8 bn** subsidies 2023; Wallonia **~€3.1 bn**; BCR **>~€1 bn**. Federal subsidies 2023 **€6.8 bn** (~2/3 tax remittance exemptions). SS wage **€3.5 bn** 2023. **~2/3 package = wage subsidies** (BV non-remittance, SSC targets, dienstencheques). Wallonia L5: APE **€543 m**, titres-services **€534 m**, green cert **~€323 m**. Bpost **>€300 m** 2023; coalition NMBS **−€250 m by 2029**, bpost **−€50 m**. BE subsidies ~double euro-area on D.3 path.
- Wrote: entity bpost; budgets (package + regional L4 samples); commitments; leaderboard lb_nbb_ent_subsidies + wage block + bpost; PDF raw; sources; rq_026=done; queued rq_027–028; ticks=27
- FOI: none new (primary source rich)
- Next: rq_027 federal tax remittance exemption L5 or rq_025 Liège

### 2026-07-20T01:40:00Z — tick 28
- Unit: rq_027 (Federal tax remittance exemption EIWT L5)
- Found (FPS inventory EIWT 2024, strong): **package sum €4.356 bn** (33 lines). Top: **night work €1.010 bn**; R&D masters €601m; construction nightshift €416m; continuous work €367m; PhD researchers €330m; scientific institutions €266m; **shift work €244m**; universities research €229m; structural €218m; overtime €186m. Clusters: **night/shift ~€2.04 bn**; **R&D researchers ~€1.60 bn**. Rekenhof Dec 2023: **€3.9 bn in 2021** (vs €2.9 bn 2017); control/Belspo gaps. Aligns with NBB ~2/3 of federal €6.8 bn enterprise subsidies.
- Wrote: taxex package+clusters+major lines; budgets; commitment; leaderboard lb_eiwt_*; Rekenhof PDF raw; sources; rq_027=done; ticks=28
- FOI: none (primary FPS+Rekenhof)
- Next: rq_025 Liège L5 or rq_028 bpost PSO

### 2026-07-20T02:00:00Z — tick 29
- Unit: rq_025 (Liège city L5 subsidy sample)
- Found (Ville de Liège **budget service ordinaire 2026** PDF, strong): recettes **€710.2 m**, dépenses **€685.6 m**, surplus **€24.7 m** (ordinary perimeter — not consolidated). Culture dept total **€12.4 m**. Named L5 city subsidies 2026: **OPRL €795k** (flat 2024–26); **Opéra Royal de Wallonie €428k**; **Théâtre de Liège (Emulation) €263k**; **CIAC €180k**; Trianon/Art Wallon **€114.75k** (cut from €150k). Press 1.1–1.2 bn figures likely broader perimeter.
- Wrote: budgets; 5 commitments; leaderboard; FOI gap_liege_subsidies_top20 ready; PDF raw; sources; rq_025=done; ticks=29
- FOI: gap_liege_subsidies_top20 ready (not sent)
- Next: rq_028 bpost PSO multi-year

### 2026-07-20T02:20:00Z — tick 30
- Unit: rq_028 (bpost PSO multi-year subsidy path)
- Found: **Press concession ~€125 m/yr** (was €175 m); government scrap saves **€125 m/yr from 2027**. Extension to **30 Jun 2024 budget €75.0 m** (bpost 4Q23 deck). NBB: bpost subsidies **>€300 m in 2023** (ESA package). Phase-out of newspaper delivery subsidy through **2027**. bpost: press revenues **~−€50 m in 2024** (~€35 m less favourable contracts). Overcompensation provision **€82.5 m** repay to State (fines/679/plates). Coalition **−€50 m** path on remaining bpost subsidies (NBB). Residual **USO compensation cash-by-year still opaque** → FOI.
- Wrote: budgets; commitments; leaderboard; FOI gap_bpost_uso_split ready; sources; PDF raw; rq_028=done; queued rq_029–031; ticks=30
- FOI: gap_bpost_uso_split ready (not sent)
- Next: rq_030 offshore wind CfD (prio 7) or rq_029 city L5

### 2026-07-20T02:40:00Z — tick 31
- Unit: rq_030 (Offshore wind federal support path)
- Found (Rekenhof Nov 2023, strong): eastern zone **2.26 GW / 9 parks**; cumulative **production support €3.41 bn** + **connection €209 m** = **€3.62 bn** through end-2021; lifetime estimate **€12.68 bn** (minister Feb 2020; EC notification had used €10 bn); degressivity cost to federal general means **€989.6 m** (2013–2021); household offshore surcharge 2021 **€49.49**; from 2022 financing via special excise + general means. CREG AR2023: **support cost 2023 = €179.4 m**; net production **8 020 GWh**. Variable FiP parks saw reduced/zero support in high-price 2022–23 years (cap/clawback).
- Wrote: entity creg; budgets; commitments; leaderboard; FOI gap_offshore_annual_cash ready; PDFs raw; sources; rq_030=done; ticks=31
- FOI: gap_offshore_annual_cash ready (not sent)
- Next: rq_031 Maribel 1.5bn or rq_029 city L5

### 2026-07-20T03:00:00Z — tick 32
- Unit: rq_031 (Maribel Social Funds)
- Found (NBB Econ Review 2025/9 Tables A1–A2, strong): **Maribel SS-sector €1 460 m (2023) / €1 461 m (2024)** — nearly half of all SS enterprise subsidies (€3 496 m total 2024). Federal Maribel add-on **€56 m / €59 m**. Package **~€1.52 bn 2024**. Purpose: extra jobs in non-profit healthcare/social/public services (late 1980s). Related SS wage lines: targeted SSC **€926 m**; hospital employees **€663 m**. Bonus same tables: **NMBS D.31 €1 127 m 2024** (was €1 284 m 2023); **bpost €329 m 2024**; **offshore ESA €592 m 2024** (vs CREG 179.4 m 2023 different perimeter).
- Wrote: entity maribel_funds; budgets (Maribel+SS package+NMBS/bpost/offshore A1); commitment; leaderboard; FOI gap_maribel_l5_split ready; gap_nmbs priority lowered (partially answered); rq_031=done; rq_032 queued; ticks=32
- FOI: gap_maribel_l5_split ready (not sent)
- Next: rq_029 Charleroi/Brugge city L5

### 2026-07-20T03:20:00Z — tick 33
- Unit: rq_029 (Brugge city L5 sample — chose Brugge over Charleroi for official MJP PDFs)
- Found (Stad Brugge **MJP 2026–2031**, strong, consolidated Stad+OCMW): total uitgaven **€483.6 m** (2026); exploitatie **€399.9 m**; investeringen **€70.0 m**; Gemeentefonds **€110.4 m**; cultuur BD10 **€22.7 m**. Nominatieve L5 2026: **Politiezone €33.75 m**; **HVZ Zone 1 €10.03 m**; **Brugge Plus loon €2.76 m** (+ overhead €0.61 m + event lines); **Concertgebouw werk €705k** + **invest onderhoud €720k/yr** + gevelschil **~€6.4 m** multi-year; **Entrepot €894k**; Stadsmakers **€567k**; BMCC **€639k**; Cercle invest **€1.0 m** 2026.
- Wrote: budgets; 6 commitments; leaderboard; PDFs raw; sources; rq_029=done; rq_033 Charleroi queued; ticks=33
- FOI: none (nominative list public)
- Next: rq_033 Charleroi L5 or rq_032 NBB annex

### 2026-07-20T03:40:00Z — tick 34
- Unit: rq_033 (Charleroi city L5 / budget map)
- Found (council press medium): budget **~€567 m** balanced 2026; recettes propres **2025 €577.9 m**; **4P transfers €240.3 m** (~38% of spend, path to 50% by 2030); Plan Oxygène **~€48 m** Walloon aid; expenditure cut **~€40 m** (RTBF); invest borrowing only **€20 m**; BSCA profit claim **€25 m 2025** + passenger tax debate; PBA renovation request **€7.6 m** (higher-tier grant, not confirmed city L5). Named third-party culture lines still weak publicly → FOI.
- Wrote: entity city_charleroi; budgets; commitments; leaderboard; FOI gap_charleroi_subsidies_top20 ready; sources; rq_033=done; ticks=34
- FOI: gap_charleroi_subsidies_top20 ready (not sent)
- Next: rq_032 NBB annex cross-check (only open research left)

### 2026-07-20T04:00:00Z — tick 35
- Unit: rq_032 (NBB annex A1 multi-year fill + reconciliation)
- Found (NBB Econ Review 2025/9 Table A1 NAI, strong): **NMBS D.31** €965m (2000) / **€1 284 m (2023)** / **€1 127 m (2024)**; **NMBS D.92** €784m / **€767 m** / **€830 m** → package **€2 051 m (2023)** / **€1 957 m (2024)**. **bpost D.31** €215m / **€324 m** / **€329 m**. **Offshore wind D.31** **€283 m (2023)** / **€592 m (2024)** — vs CREG cash support **€179.4 m (2023)** (perimeter gap). Federal public-enterprise D.3 total **€1 456 m (2024)**. FPS Kamer cash-line cross-check not found this tick → FOI remains + new rq_034.
- Wrote: multi-year budgets; commitments cash_by_year; leaderboard NMBS package (opacity closed); FOI priority tweaks; rq_032=done; queued rq_034–036; ticks=35
- FOI: gap_nmbs + gap_offshore updated notes (not sent)
- Next: rq_035 RIZIV top-line (prio 7) or rq_034 NMBS FPS cash

### 2026-07-20T04:20:00Z — tick 36
- Unit: rq_035 (RIZIV care budget top-line)
- Found (RIZIV official 20 Oct 2025, strong): **2026 global VGV €46.775 bn**; **authorized geneeskundige verstrekkingen €40.986 bn** (+€1.274 bn / **+3.2%** vs 2025). Prior year anchors kept: global **€45.222 bn** / care **€39.712 bn** (2025). **Correction package €470.775 m** for 2026 (drugs €227.9 m, doctors €150 m, hospitals €50 m, …). Health index honoraria **2.72%**. Non-care effort **€33.5 m**. Core entitlement — efficiency audits not crude abolition.
- Wrote: budgets 2026; multi-year commitments; leaderboard lb_riziv_care; source; entity notes; rq_035=done; ticks=36
- FOI: none
- Next: rq_034 NMBS FPS cash or rq_036 company cars

### 2026-07-20T04:40:00Z — tick 37
- Unit: rq_034 (FPS/BOSA federal budget NMBS cross-check)
- Found: **Exact Kamer/FPS article codes for NMBS cash lines not in public summary this tick.** Best reconciliation remains **NBB ESA A1** (D.31+D.92 **€1.957 bn 2024**). **FPB (BOSA initial 2026):** federal **subsidies €7.9 bn**; **investments €6.5 bn** of which **~17% → Infrabel = €1.105 bn** (Infrabel in GG; NMBS outside). FPB cites NBB: NMBS+bpost top public-enterprise subsidy recipients. **Savings path** (VRT medium): **€188 m** next year → **€663 m** structural end legislature (not MR’s €2.1 bn). Standaard medium: NMBS personnel **€1.34 bn** ~half opex.
- Wrote: budgets fed subs/invest/Infrabel; commitments; leaderboard lb_infrabel; sources; PDF raw; FOI gap_nmbs note; rq_034=done; ticks=37
- FOI: gap_nmbs still ready (budget codes)
- Next: rq_036 company cars taxex (only open research left)

### 2026-07-20T05:00:00Z — tick 38
- Unit: rq_036 (Company cars FPS package deep lines)
- Found: **Full package still only secondary ~€2.3 bn (2024)** — not a single FPS inventory line. Explicit FPS **car-named residual** sum **~€13 m** (CIT business cars CG €12.44 m + electric cars €0.85 m + small VAT invalids). Related mobility taxex now mapped: **professional diesel €557.83 m**; industrial gas oil motor **€312.54 m**; commuting public **€376.84 m**; other commute **€155.33 m**; bike commute **€126.89 m**. Opacity of official BIK/SSC/PIT package decomposition → FOI prio 9.
- Wrote: taxex residual sum + pro diesel + mobility lines; leaderboard note; FOI gap_company_cars_te_package ready; rq_036=done; queued rq_037–039; ticks=38
- FOI: gap_company_cars_te_package ready (not sent)
- Next: rq_038 defence (prio 7) or rq_037 pro diesel phase-out

### 2026-07-20T05:20:00Z — tick 39
- Unit: rq_038 (Defence expenditure latest)
- Found (Strategische Visie Defensie 2025 official, strong): **2% GDP defence effort from 2025** (halt any decline) → **2.5% by 2034**. Capacity portfolio **2026–2034**: vastlegging **€33.784 bn** / vereffening **€24.661 bn** (constant €2026). Structure target ~35% personnel / 40% ops / 25% investment by 2035. Existing **NAI COFOG €8.8 bn (2025, 1.14% GDP)** ≠ NATO cash perimeter. **FPB/BOSA 2026:** ~**71% of €6.5 bn federal invest → Defence = €4.615 bn**. Secondary: ~**€12.8 bn** NATO-path 2025 (press); SIPRI ~**$14.5 bn / ~2.0% GDP**. Core public good — procurement efficiency not crude cut.
- Wrote: budgets; multi-year commitments; leaderboard; entity note; PDF raw; sources; rq_038=done; ticks=39
- FOI: none
- Next: rq_037 pro diesel or rq_039 interest expense

### 2026-07-20T05:40:00Z — tick 40
- Unit: rq_037 (Professional diesel phase-out path)
- Found: Refund rates **€0.1935/l (2024)** → **€0.1924 (2025)** → **€0.1913 (2026)** (slow). Peak path from **~€0.2476/l** (2020–21 class). **FPS taxex inventory 2024: €557.83 m**. **FPS FFS inventory 2026 (benchmark1): €831.2 m** professional diesel. **2021 revenue loss €905.8 m** (climat.be/FPS). Bonus same FFS table: **company cars €3,141.7 m (2024)** PIT+VAT+SSC official (supersedes 2.3bn secondary); fuel cards **€661.6 m**; total direct FFS **€10.78 bn (1.7% GDP)**.
- Wrote: taxex multi-method pro diesel + FFS company cars/fuel cards/total; commitment phase-out; leaderboard updates; sources; PDF raw; FOI company cars deprioritised to components; rq_037=done; ticks=40
- FOI: gap_company_cars components only (total answered)
- Next: rq_039 interest expense (only open research left)

### 2026-07-20T06:00:00Z — tick 41
- Unit: rq_039 (GG interest expense multi-year)
- Found (NAI EDP Table 1, strong, Apr 2026): interest expense **€8.581 bn (2021)** → **€8.755 bn (2022)** → **€11.677 bn (2023)** → **€13.524 bn (2024)** → **€14.282 bn (2025)** = **2.2% GDP** last two years. Fourth consecutive absolute rise. Context: deficit **5.2% GDP**, debt **107.9% GDP** end-2025. **FPB:** federal Entity I interest **€12.3 bn** in 2026 initial budget. Not waste — cost of past deficits; fix is primary surplus.
- Wrote: multi-year budgets 2021–25 + federal 2026; commitment; leaderboard; EDP PDF raw; source note; rq_039=done; queued rq_040–042; ticks=41
- FOI: none
- Next: rq_040 fuel cards FFS or rq_041 debt path

### 2026-07-20T06:20:00Z — tick 42
- Unit: rq_040 (Fuel cards FFS multi-year)
- Found (FPS FFS inventory 2026 Table 3, strong): **Fuel cards PIT+SSC** **€688.2 m (2021)** → **€1,119.3 m (2022 peak)** → **€852.8 m (2023)** → **€661.6 m (2024)** — decline attributed to **fleet electrification**. **VAT fuel cards €52.8 m (2024)**. **EV charging cards** rising **€20.8 → €59.4 m**. Full fuel+charge package **~€775 m (2024)**. Also filled **pro diesel FFS series** 1052/558/773/831 m 2021–24. Transport sector: fuel cards + pro diesel dominate direct FFS.
- Wrote: taxex multi-year fuel/charging/VAT; commitment; leaderboard; pro diesel FFS years; rq_040=done; ticks=42
- FOI: none
- Next: rq_041 debt path or rq_042 Flanders BO2026

### 2026-07-20T06:40:00Z — tick 43
- Unit: rq_041 (GG debt path and snowball risk)
- Found (strong): **NAI EDP Apr 2026** debt **107.9% GDP** end-2025 → **~€692.7 bn** (0.1079 × GDP €642.015 bn). Deficit **−5.2% GDP**; interest flow **€14.282 bn** (2.2% GDP). **NBB Jun 2026 projections** (cut-off 22 May 2026): debt **111.3% / 112.9% / 114.8%** for 2026–28 (~**115%** by 2028); deficit path **−5.2 → −5.3 → −5.5 → −5.7%**. **FPB Jun 2025** (older horizon): deficit **5.4% → 6.5% by 2030**; debt **~120% GDP by 2030**. Snowball: primary deficit persists while interest rises → ratio climbs; fix is **primary surplus**, not labelling debt as L5 waste.
- Wrote: budgets debt stock+ratio path+deficit; commitment cmt_gg_debt_path; leaderboard lb_gg_debt_stock; entity gg_debt; sources NBB/FPB; rq_041=done; queued rq_043–044; ticks=43
- FOI: none
- Next: rq_042 Flanders BO2026 confirm or rq_043 Debt Agency EUR stock

### 2026-07-20T07:00:00Z — tick 44
- Unit: rq_042 (Flanders total expenditure BO2026 confirm)
- Found (strong): **DFB official page + parliament vote (Jan 2026):** BO2026 uitgaven **€66.0 bn**; **OV+WVG = 58%**. **Evaluatierapport:** consolidated **VEK €66.03 bn** (BA2025 **€66.47 bn**; constant-policy would be **€67.05 bn** → measures cut **~€1.01 bn**); **VAK €64.75 bn**. **Receipts €61.6 bn**; **ESR saldo −€2.9 bn** (−€1.7 bn after doelstelling corrections). Deltas: index **+€718.9 m**; VV **+€370.9 m**; rente **+€323.5 m**; retro premie **−€301.6 m**; subsidies **−€210 m**. Entity rank #4 reconfirmed (budgeted, not ESA TE).
- Wrote: multi-year budgets; commitment; programmes final VEK; entity/rank notes; sources; rq_042=done; queued rq_045 BA2026; ticks=44
- FOI: none
- Next: rq_043 Debt Agency stock or rq_044 primary balance gap

### 2026-07-20T07:20:00Z — tick 45
- Unit: rq_043 (Federal Debt Agency Entity I stock)
- Found (BDA Review 2025/Outlook 2026 PDF, strong): federal gross debt **€518.68 bn (end-2024)** → **€552.69 bn (end-2025)** **+€34.0 bn**. Composition end-2025: **OLO €462.8 bn**; TC **€42.9 bn**. **Avg life 10.38 → 9.98 years**; duration **8.43 → 7.27 y**; fixed rate **87.4%**; 12m refinancing risk **15.64%** (cap 17.5%); financial cost at issuance (EUR) **2.01%**. Gross borrow 2025 **€53.31 bn** / net **€28.35 bn**. Plan 2026: gross **€59.55 bn** / net **€26.37 bn** / OLO issue **€51.60 bn**. Live BDA site (medium): **€567.615 bn** on **2026-06-30**. Perimeter: federal BDA **~80%** of GG ESA **€692.7 bn** — do not double-count.
- Wrote: budgets multi-year + OLO/TC/borrow; commitment; entity debt_agency_be; leaderboard; sources + raw PDF; rq_043=done; ticks=45
- FOI: none
- Next: rq_044 primary balance gap or rq_045 Flanders BA2026

### 2026-07-20T07:40:00Z — tick 46
- Unit: rq_044 (Primary balance path vs debt-stabilising)
- Found (strong): **NBB Jun 2026 projections** primary balance **−2.9% / −2.8% / −2.7% / −2.7%** GDP for **2025–28** while overall deficit widens **−5.2 → −5.7%** (interest wedge growing). Debt **107.9 → 114.8%**. **IMF Art IV 2025**: primary ~**3.1 ppt of GDP below** debt-stabilising primary of **+0.3% GDP** → gap ≈ **€19.9 bn** (0.031 × GDP €642.0 bn). **NBB Review 2025/11**: snowball = (r−g)×debt − primary; with **r>g** and primary deficit, debt path explosive unless primary improves. **EC/MTFSP**: planned structural primary improvement **+2.4 pp 2025–29** — delivery still open. Not L5 waste: the DOGE north star for fiscal math.
- Wrote: primary multi-year budgets; gap estimate; commitment; leaderboard lb_primary_gap; sources + NBB PDF; rq_044=done; queued rq_046 MTFSP; ticks=46
- FOI: none
- Next: rq_045 Flanders BA2026 or rq_046 MTFSP path

### 2026-07-20T08:00:00Z — tick 47
- Unit: rq_045 (Flanders BA2026 adaptation)
- Found (Rekenhof Jun 2026 + Vlaams Parlement, strong): BA2026 ESR **ontvangsten €62.2 bn** / **uitgaven €67.1 bn** → **vorderingensaldo −€3.6 bn** (BO was −€2.9 bn). Vs begrotingsdoelstelling (excl Oosterweel+relance): **−€2.18 bn** (was −€1.7 bn). Deltas vs BO: VEK **+€1.081 bn**, VAK **+€3.034 bn** (Lantis/Oosterweel VAK **+€2.514 bn**); index VEK **+€324.5 m**; Fluvius VEK **€1.1 bn**. OV **€20.2 bn VEK** / WVG **€17.8 bn VEK**. Schuld **+€6.8 bn** (+13.5% y/y); rating AA-. Entity rank #4 updated to **€67.1 bn**.
- Wrote: budgets BA lines; commitment supersede; programmes OV/WVG/total; rank+entity; sources + raw PDFs; rq_045=done; queued rq_047 VL debt; ticks=47
- FOI: none
- Next: rq_046 MTFSP or rq_047 Flanders debt stock

### 2026-07-20T08:20:00Z — tick 48
- Unit: rq_046 (Belgium MTFSP structural primary + net expenditure path)
- Found (official MTFSP PDF + Council rec Jun 2025, strong): **Structural primary balance** plan **−1.8 → −1.2 → −0.7 → 0.0 → +0.6% GDP (2025–29)** = **+2.4 pp** (matches EC country-report phrasing). **Net nationally financed primary expenditure growth**: **3.6 / 2.5 / 2.5 / 2.1 / 2.1%** → **5y avg 2.56%** (EC ref 2.53%). **Deficit path** to **−3.0% GDP by 2029**; plan debt peaks **107.3%** then **106.7%** — **actual 2025 already 107.9%** and NBB primary **−2.9%** worse than plan **−2.4%**. 7-year adjustment; Entity I/II split deferred (Overlegcomité Mar 2025 commitment). Delivery risk is the DOGE angle — not a waste line.
- Wrote: MTFSP budget rows; commitment cmt_be_mtfsp; leaderboard; sources + PDFs; rq_046=done; queued rq_048 Entity split; ticks=48
- FOI: none
- Next: rq_047 Flanders debt stock or rq_048 Entity I/II split

### 2026-07-20T08:40:00Z — tick 49
- Unit: rq_047 (Flanders consolidated Maastricht debt path)
- Found (Rekenhof Table 14, strong): consolidated Maastricht debt **€50.172 bn (end-2025)** → **€56.552 bn (BO2026)** → **€56.971 bn (BA2026)** = **+€6.799 bn / +13.5%** y/y. **Direct MVG debt** **€42.397 → €49.802 bn** (+€7.405 bn). Components BA2026: consolidated entities financial **€7.17 bn**; PPS **€0.64 bn**; green certs **€0.55 bn**; intra/inter-sector holdings corrections **−€11.38 bn**. Debt/receipts **91.6%** (old schuldnorm target **<65%**). Netto-actief end-2024 **−€13.3 bn**. Ratings: Fitch **AA-** (stable); S&P **AA-**; Moody’s **A1**. Drivers: deficit, Oosterweel, relance, ESR 8/9 (Fluvius, social housing…). Non-Maastricht federal claims: hospital infra **€2.184 bn** + autonomiefactor **€0.474 bn** (not in stock).
- Wrote: multi-year debt budgets; commitment; leaderboard; entity note; rq_047=done; queued rq_049 non-Maastricht claims; ticks=49
- FOI: none
- Next: rq_048 Entity I/II MTFSP split

### 2026-07-20T09:00:00Z — tick 50
- Unit: rq_048 (Entity I vs II MTFSP effort split)
- Found (strong): **MTFSP Mar 2025** deferred Entity I/II split. **HRF Apr 2025** (recalc of Jul 2024): **verdeelsleutel 3** = share of (final primary expenditure + own receipts) — preferred key. Differentiated **max net primary exp growth %** (7y path): **Entity I avg 2.72%** (2025 **3.81%**, 2026 **2.96%**); **Flanders 2.68%** (3.63 / 2.17); **FWB 1.52%**; **Wallonia 1.45%**; **Brussels −0.22%** (very tight); **DG negative**. **Overlegcomité Mar 2026** SWA: uses sleutel 3 for current plan; **fallback binding targets** if no agreement; control accounts via HRF; **defence national escape clause fully to federal** (Rekenhof/APR). GG outturn path still **3.8% / 2.0%** net exp 2025–26 (cumul 5.9% < 6.1% cap, APR). Parliaments still ratifying SWA.
- Wrote: entity growth-cap budgets; commitment; leaderboard; sources + HRF/APR PDFs; rq_048=done; queued rq_050 ratification; ticks=50
- FOI: none (method+caps public)
- Next: rq_049 Flanders non-Maastricht claims or rq_050 SWA ratification

### 2026-07-20T09:20:00Z — tick 51
- Unit: rq_049 (Flanders non-Maastricht federal claims)
- Found (Rekenhof BA2026 §5.1, strong): Flanders owes federal government **€2.1843 bn** (ziekenhuisinfrastructuur) + **€473.8 m** (definitieve vaststelling **autonomiefactor**) = **€2.658 bn** total. **Excluded from Maastricht** consolidated debt (€56.97 bn). Rekenhof: these stocks are **no longer reported in de algemene toelichting**; recommends Vlaams Parlement be kept informed. Multi-year amortisation cash-by-year **not public** this tick → FOI.
- Wrote: three budget rows; commitment; leaderboard; FOI gap_vl_non_maastricht_claims **ready** (not sent); rq_049=done; ticks=51
- FOI: gap_vl_non_maastricht_claims ready — human send only
- Next: rq_050 SWA ratification / control accounts

### 2026-07-20T09:40:00Z — tick 52
- Unit: rq_050 (SWA ratification + Entity control accounts)
- Found (strong/medium): **SWA timeline** — Overlegcomité **27 Mar 2026** draft economic-governance SWA (replaces **13 Dec 2013**); **Flanders government 8 May 2026** principal OK + draft assent decree → SERV/RvS; **federal Ministerraad 13 May 2026** draft assent law (secondary reports); **SERV advice Jun 2026**; Rekenhof Jun 2026: still needs each entity government + **parliament** assent — **full multi-parliament ratification not confirmed** this tick. **Entity I control account** (Kamer 56K1468, budget-basis approx): net exp **€190.3 bn (2025) / €196.9 bn (2026)**; growth **4.6% / 2.3%** vs HRF **3.81% / 2.96%**; annual deviation **+€1.5 / −€1.3 bn**; cumul after defence flex **−0.30% / −0.71% GDP** (under norm). Official HRF multi-entity public ledgers not yet a complete published suite.
- Wrote: Entity I net-exp + control budgets; commitment/leaderboard update; sources + Kamer PDF; rq_050=done; queued rq_051–052; ticks=52
- FOI: none
- Next: rq_052 Flanders net-exp vs 2.17% cap (prio 4) or rq_051 regional SWA assent

### 2026-07-20T10:00:00Z — tick 53
- Unit: rq_052 (Flanders HRF net-exp compliance vs 2.17% cap)
- Found (BO2026 Algemene Toelichting Table 10 via eval/SERV, strong): HRF-concept **finale primaire uitgaven €63.047 bn (2025) / €62.106 bn (2026)**; **netto-uitgaven €62.036 / €61.296 bn**; after DRM **€60.761 bn (2026)**; **growth −2.1%** vs **HRF sleutel 3 cap +2.17%** → **margin −4.23 pp** (clearly **compliant** at BO). SERV: “lijkt te voldoen”. **BA2026 (Rekenhof)**: calculation in Ch.VI still cited but **not on final BA numbers** (uses DBP/process estimates; admin lacks APR microdata) — method lag, not a re-computed growth % this tick. Do not invent BA growth.
- Wrote: net-exp stock + growth budgets; commitment; leaderboard; source + eval PDF; rq_052=done; queued rq_053 Wallonia 2026; ticks=53
- FOI: none
- Next: rq_053 Wallonia 2026 total (prio 5) or rq_051 regional SWA assent

### 2026-07-20T10:20:00Z — tick 54
- Unit: rq_053 (Wallonia total expenditure 2026 initial)
- Found (ExpGen budget initial 2026 official PDF, strong): **dépenses €21.335748 bn** (was €22.029416 bn 2025 init, **−€694 m**); **recettes €18.515734 bn**; **solde brut −€2.820 bn**; **solde SEC −€2.015736 bn** (path −2.015 / −1.124 / −0.600 / +0.039 bn 2026–29). Structural savings **€270.4 m**. Net primary exp **€19.463 → €19.056 bn** growth **−2.09%** vs CSF key cap **+0.92%** (~3 pp under, indicative). Entity rank #8 updated to 2026 envelope.
- Wrote: budgets multi-line; commitment; entity+rank; sources + PDF; rq_053=done; queued rq_054 FWB; ticks=54
- FOI: none
- Next: rq_054 FWB total or rq_051 regional SWA assent

### 2026-07-20T10:40:00Z — tick 55
- Unit: rq_054 (FWB total expenditure 2026 primary source)
- Found (DGBF éléments-clés official, strong): **initial 2026** recettes **€13.602 bn** / dépenses liquidation **€15.406879 bn** / solde brut **−€1.667 bn** / **SEC −€1.608 bn**. Breakdown: Education-Recherche-Formation **€10.929 bn**; Santé-Culture-Sport **€2.325 bn**; Services généraux **€1.185 bn**; dette publique **€0.393 bn**; dotations RW/COCOF **€0.575 bn**. Multiyear SEC path **−1.608 / −1.405 / −1.390 / −1.224 bn** (2026–29). **Adjusted 2026** (gov press 30 Apr): recettes **€13.67 bn** / dépenses **€15.59 bn** / deficit **€1.77 bn** (+€160 m vs initial 1.61). Supersedes medium ~€15 bn press estimate. Entity rank #9 updated strong.
- Wrote: budgets init+adj+edu; commitment; entity+rank; sources; rq_054=done; queued rq_055 Brussels; ticks=55
- FOI: none
- Next: rq_055 Brussels total or rq_051 regional SWA assent


















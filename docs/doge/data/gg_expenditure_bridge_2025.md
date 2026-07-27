# General government expenditure bridge (coverage dashboard)

**Tick:** 124 · **Unit:** rq_152 · **As-of:** 2026-07-27  
**Anchor year:** ESA/EDP **2025** (latest full S.13 outturn in dataset)  
**Rule:** sourced euros only; **do not sum** all `budgets.csv` rows (debt stocks, multi-year envelopes, subtotals, and unconsolidated layers double-count).

---

## 1. L0 — consolidated total (100% tagged)

| Metric | EUR | % GDP | Source | Confidence |
|--------|-----|-------|--------|------------|
| **S.13 total expenditure (TE)** | **347,956,000,000** | 54.2% | NBB NAI EDP Apr / Eurostat | **Strong** |
| S.13 primary expenditure | 333,675,000,000 | 52.0% | same | **Strong** |
| S.13 interest (D.41) | 14,282,000,000 | 2.2% | NAI EDP Table 1 | **Strong** |
| S.13 gross debt (stock, not flow) | ~692,733,000,000 | 107.9% | NBB EDP | **Strong** |

**Coverage L0 flow TE:** **100%** (single official total).  
Debt stock is **not** part of the €348bn TE pie.

---

## 2. L1 — ESA subsectors (100% tagged; unconsolidated)

Eurostat `gov_10a_main` TE **2025** (provisional), EUR million × 1e6:

| Subsector | Code | TE EUR | Share of unconsol. sum | Notes |
|-----------|------|--------|------------------------|-------|
| Central government | S.1311 | 181,526,100,000 | 36.5% | Federal Entity I class |
| State (communities + regions) | S.1312 | 128,623,800,000 | 25.9% | VL + WAL + FWB + BRU + DG + … |
| Local | S.1313 | 44,986,700,000 | 9.1% | Cities, communes, provinces, CPAS/OCMW, … |
| Social security funds | S.1314 | 141,680,400,000 | 28.5% | RIZIV, pensions, unemployment, Maribel, … |
| **Unconsolidated sum** | | **496,817,000,000** | 100% | |
| **minus consolidated S.13** | | **347,956,000,000** | | |
| **Inter-gov transfer wedge** | | **≈148,861,000,000** | | Double-count if L1 rows are added raw |

**Coverage L1:** **100%** of TE mapped to four subsectors.  
**Method flag:** any “sum of entity budgets” must stay **inside one subsector** or use **consolidated** concepts — never add S.1311+…+S.1314 as if = S.13.

---

## 3. L2 — large entity / programme anchors (partial; mixed years)

Figures below are **already in `budgets.csv`**. Year mix is **honest** (budget 2026 vs ESA 2025): use for **order-of-magnitude** entity coverage, not a perfect residual identity.

### 3a · S.1312 state layer — regional/community budget totals

| Entity | Year | Amount EUR | Basis | Conf. | vs S.1312 128.6bn |
|--------|------|------------|-------|-------|-------------------|
| Flanders (BA2025 VEK consol.) | 2025 | 66,470,000,000 | ESR VEK | Strong | ~52% of S.1312 |
| Flanders (BA2026 uitgaven) | 2026 | 67,100,000,000 | ESR | Strong | (budget year) |
| Wallonia (init dépenses) | 2025 | 22,029,416,000 | budget | Strong | |
| Wallonia (init) | 2026 | 21,335,748,000 | budget | Strong | |
| FWB (init liquidation) | 2026 | 15,406,879,000 | budget | Strong | |
| Brussels SGRBC liq. | 2026 | 8,000,000,000 | Cour | Strong | |
| DG Ostbelgien (HV AE class) | 2025 | ~685,700,000 | CoA | Strong | prior tick |

**Illustrative 2025-class regional sum** (FL 66.47 + WAL 22.03 + FWB ~15 class + BRU 8 + DG 0.69) ≈ **€112 bn**.  
vs S.1312 **€128.6 bn** → **order €15–20 bn residual** in state layer (other bodies, perimeter/ESA vs cash budget, joint institutions, year/basis gaps). **Not invented as exact residual** — flag for further L2 mapping.

### 3b · S.1314 social security — partial

| Entity / line | Year | Amount EUR | Conf. | Note |
|---------------|------|------------|-------|------|
| RIZIV global VGV | 2025 | 45,222,000,000 | Strong | Care package; **not** full S.1314 |
| RIZIV global VGV | 2026 | 46,775,000,000 | Strong | |
| Maribel SS ESA class | 2024 | ~1,461,000,000 | Strong (NBB) | L5 fund split FOI |
| S.1314 total | 2025 | 141,680,400,000 | Strong | Residual ≈ pensions + unemployment + family + other |

**RIZIV ≈ 32%** of S.1314 TE 2025. Rest of SS largely **aggregate-only** in this dataset (FOI/research: Maribel L5, union payment channels, mutualities).

### 3c · S.1311 federal — partial

| Line | Year | Amount EUR | Conf. |
|------|------|------------|-------|
| S.1311 TE | 2025 | 181,526,100,000 | Strong |
| BOSA federal transfer register total | 2025 | 179,916,000,000 | Strong | 8993 items — **register**, not all = TE |
| Interest Entity I (budget) | 2026 | 12,300,000,000 | Strong |
| Defence COFOG | 2025 | 8,800,000,000 | Strong |
| NMBS ESA package class | 2024 | ~1.1–2.0 bn depending D.31/D.92 split | Strong/medium | Cash codes FOI |
| Facultative subsidies envelope class | — | ~900,000,000 | Medium | Prior tick |

Federal **named L5 third-party lines** still thin → **rq_124** (BGD top 50).

### 3d · S.1313 local — sample only

| Layer | EUR class | Coverage |
|-------|-----------|----------|
| S.1313 TE 2025 | 44,986,700,000 | Strong total |
| 5 Walloon provinces ord+extra sum 2026 | ~2.07 bn | Strong sample |
| 5 Flemish provinces cash-out class | ~0.8–1+ bn (mixed) | Strong sample |
| City samples (Gent/Brugge open registers; Mons/Namur/Liège/Antwerp partial) | L5 samples | Not additive to S.1313 |

**Local L5 named €** = **small %** of €45 bn.

---

## 4. What “% of €348 bn tagged” can mean (three layers)

| Layer | Definition | Status in this repo | Approx. |
|-------|------------|---------------------|---------|
| **A. L0 total** | Official S.13 TE known | Done | **100%** of 348bn |
| **B. L1 subsector** | TE split S.1311–14 known | Done | **100%** of unconsol. map; consol. identity known |
| **C. L2 entity totals** | Major budget holders with primary totals | Regions/communities + RIZIV + many agencies **partial** | **High for S.1312 tops; partial S.1311/14; weak S.1313** |
| **D. L4–L5 end-receivers** | Named programme/project/ASBL with € | Samples + leaderboard + FOI stack | **Low single-digit % of TE at best** — do **not** claim near-complete L5 |

**Honest headline:**  
> We have **fully sourced** the €348 bn as an ESA total and a four-way subsector split. We have **sourced large entity budgets** covering most of the state layer and a large SS care block. We have **not** named every public euro to an end-receiver; material opacity is queued as FOI or open research (rq_123–155).

---

## 5. Off-TE tracks (do not mix into 348bn)

| Track | EUR class | Source class | Note |
|-------|-----------|--------------|------|
| FPS tax expenditure inventory | ~39.4 bn (2023 class) | Strong inventory total | Revenue foregone, not GG TE |
| FFS direct fossil subsidies | ~10.8 bn (2024) | Strong | Subset/related to TE/energy |
| Company cars FFS package | ~3.14 bn (2024) | Strong FFS | Component split FOI |
| NBB enterprise subsidies | ~25.1 bn (2024) | Strong NBB | Overlaps wage/subsidy TE |

---

## 6. Residual buckets (priority for next ticks / FOI)

Already **FOI-ready** (human send): cheques TE, unemployment pay unit cost, NMBS cash codes, De Lijn full dotatie, FOREM/VDAB, Maribel L5, multi-parliaments, city top20 Antwerp/Charleroi, CIE/FIO L5, Wassalon contractors, etc. — see `foi_queue.csv` status=`ready`.

**Public hole-fill still open (research_queue, high prio):**

| ID | Priority | Residual |
|----|----------|----------|
| rq_124 | 8 | Federal BGD top discretionary L5 |
| rq_125 | 8 | Flanders named subsidies L5 |
| rq_130/131 | 8 | NMBS / De Lijn cash series |
| rq_154 | 8 | Cheque official TE |
| rq_123 | 8 | VL gelijke kansen projects beyond Wassalon |
| rq_132/133 | 7 | VDAB / FOREM full budgets |
| rq_137–139 | 7 | Parties / unions / mutualities |
| Local/city | 5–7 | Expand S.1313 L5 |

---

## 7. Inventory counts (this tick)

| File | Rows |
|------|------|
| budgets.csv | 786 |
| commitments.csv | 228 |
| leaderboard.csv | 160 |
| tax_expenditures.csv | 153 |
| programmes.csv | 37 |
| entities.csv | 75 |
| foi_queue status=ready | 34 (human send) |
| research_queue open (pre-close) | 38 |

---

## 8. Bottom line

| Question | Answer |
|----------|--------|
| Is every material euro in the **€348 bn TE** known as a **total**? | **Yes (L0 strong).** |
| Is it split by **government layer**? | **Yes (L1 strong).** |
| Is most money traced to **named budget holders**? | **Partially (L2):** Flanders/Wallonia/FWB/Brussels/DG + RIZIV + selected agencies; federal & local incomplete. |
| Is most money traced to **end-receivers (L5)**? | **No.** Samples + FOI backlog. Goal remains: every **material** flow sourced **or** FOI-queued — not fantasy full naming of 348bn line-by-line. |

**No new euros invented.** All amounts above cite prior primary rows / Eurostat / NBB already in `budgets.csv` + `sources.csv`.

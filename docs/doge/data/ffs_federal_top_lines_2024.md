# Federal fossil fuel subsidies (FFS) — top lines snapshot

**Source class:** FPS Finance + FPS Health, *Federale inventaris van subsidies voor fossiele brandstoffen 2026* (5th edition, Jul 2026; data cut 1 Jan 2026).  
**Method:** Benchmark 1 = unleaded petrol TOE neutrality unless noted. Amounts are **opportunity cost vs benchmark**, not ESA cash grants and **not additive** without care (double instruments, different benches).  
**DOGE rule:** no invented euros; confidence **strong** for table extracts.

## Package totals (2024)

| Package | EUR m | Notes |
|---------|------:|-------|
| Direct FFS total | **10,781.9** | 1.7% GDP; path 12.09 / 13.45 / 11.66 / 10.78 bn 2021–24 |
| International air+sea | **1,006.5** | Kerosene air 754.6 + heavy FO sea 226.9 + diesel sea 25.0 |
| Indirect (VAT air tickets) | **224.5** | Path 87.5 → 224.5 2021–24 |
| Company cars EHS | **3,141.7** | Path 1,998 → 3,142 2021–24 |
| **Illustrative broad sum** | **~15,155** | Direct+intl+indirect+EHS — press “15bn” class; **do not treat as single cut** |

## Mapped high-EUR lines (2024, already in CSVs)

| Line | EUR m 2024 | Multi-year note | Leaderboard / commitment |
|------|----------:|-----------------|--------------------------|
| Gas product rate-diff (bench1) | **4,089** | 4,742→5,124→4,089 2019–24 | `lb_gas_product_diff` |
| Stookolie / huisbrandolie total | **1,836** | 2,130→1,836 2019–24 | `lb_exc_heatoil` |
| Company cars EHS | **3,142** | FFS Table3 | `lb_company_cars` |
| Industrial gas reduced (EBO) | **903** | Peak 1,295 (2022) | `lb_gas_reduced_industrial` |
| Pro diesel FFS bench1 | **831** | 1,052→558→831 | `lb_exc_prodiesel` |
| Aviation kerosene | **755** | 677→755 2019–24 | `lb_ffs_kerosene_air` |
| Fuel cards PIT+SSC | **662** | Peak 1,119 (2022) | `lb_fuel_cards` |
| VAT gas households 6% | **635** | From 2022 | `lb_vat_gas_hh` |
| Agriculture intermediate | **379** | Peak 630 (2022) | `lb_ag_intermed_ffs` |
| Gasolie industrial/commercial | **366** | ~366–416 path | taxex series |
| Diesel product residual | **273** | After petrol equalisation | taxex 2024 |
| VAT electricity HH fossil-share | **227** | Companion to gas VAT | taxex series |
| VAT air tickets | **225** | Path 88→225 | `lb_vat_air_tickets` |
| LPG heating | **128** | 109–140 path | `cmt_lpg_heating_ffs` |
| Social tariff gas (permanent) | **96** | Crisis peak 428 (2022) | `lb_social_tariff_gas` |
| Binnenvaart intermediate | **84** | Stable | `lb_binnenvaart_ffs` |
| Coal HH exemption | **11** | Declining; VAT solid fuels cut Jul 2025 | `cmt_coal_hh_exemption_ffs` |
| Sociaal Verwarmingsfonds | **13** | 70k households | `cmt_sociaal_verwarmingsfonds` |

## Related federal tax expenditure inventory (not FFS)

| Aggregate | EUR m | Year | Source |
|-----------|------:|------|--------|
| Federal TE total quantified | **39,402** | 2023 | Inventory of Federal Tax Expenditures (2024 PDF) |
| of which VAT class | 16,198 | 2023 | same |
| of which PIT federal | 9,671 | 2023 | same |
| of which EIWT | 4,415 | 2023 | same |

## Reform notes (from FFS text, not invented savings)

- FFS explicitly warns: abolishing lines ≠ full budget gain (behaviour + compensation).
- Stookolie: FFS says **not justified** environmentally or socially (not lowest-income concentrated).
- Kerosene: needs **EU coordination**; unilateral weak; ETD reform pending.
- Gas VAT 6%: EU rules push toward ending reduced fossil VAT by **2030**; federal path uses gradual gas **excise** rise toward ~12% VAT-equivalent by 2029 (FFS §3.1.3).
- Industrial EBO reduced gas: static efficiency of agreements vs weaker dynamic price signal.
- Social tariff + Verwarmingsfonds: **targeted** instruments preferred as compensation when reforming untargeted product gaps.

## FOI still human-only (not sent by agents)

- `gap_fed_gas_reduced_firms` — firm list for EBO reduced gas (~352 firms 2019; 13.5 TWh 2024).
- Other federal FOI (company cars component split, cheques, etc.) remain in `foi_queue.csv`.

## Coverage status

Top FFS package and major product/use lines for 2021–2024 are now seeded in `tax_expenditures.csv`, `commitments.csv`, and `leaderboard.csv` with primary FFS 2026 sources. Residual work: firm-level L5, Entity split of FFS, regional FFS inventories, and SWA assent tracking (`rq_107`).

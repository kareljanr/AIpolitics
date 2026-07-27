# DOGE waste ranking — current top 10

**As-of:** tick **180** (2026-07-28) · **278** leaderboard rows  
**Sort:** `priority_index` desc (then absurdity, then annual €)  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
**cost_score bands (from annual €):** &lt;1m→1.5 · &lt;10m→3.5 · &lt;100m→5.5 · &lt;1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate. Small scandals can score high on **absurdity** (see honourable mentions).

---

## Top 10 (all-time current)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_cheque_economy` | Meal / eco **cheque economy** (parafiscal + scrip) | **1.07 bn** parafiscal; face ~3.55 bn | 9 | 9.5 | 8 | **8.83** | Middleman restricted scrip; cash wages dominate |
| 2 | `lb_company_cars_fpb` | **Company cars** TE (FPB broad package) | **~4.7–5.2 bn** | 8.5 | 9.5 | 8 | **8.50** | Largest labour-fringe TE class; congestion equity |
| 3 | `lb_exc_heatoil` | **Heating oil** excise preference (FFS) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | Preferential fossil heat; not progressive |
| 4 | `lb_company_cars` | Company cars **FFS EHS** package | **3.14 bn** | 8 | 9.5 | 8 | **8.22** | Same problem, inventory perimeter |
| 5 | `lb_eiwt_package` | **EIWT** partial remittance package | **4.36 bn** | 7 | 9.5 | 6 | **8.08** | Wage-tax subsidies at scale |
| 6 | `lb_eiwt_night_shift_cluster` | EIWT **night/shift** cluster | **2.04 bn** | 7 | 9.5 | 6 | **8.08** | Sub-cluster of EIWT |
| 7 | `lb_vl_gsc_support` | Flanders **green certificates** GSC | **~0.82 bn**/yr | 8 | 9.5 | 7 | **8.00** | Bill-funded RES support; cum multi-bn |
| 8 | `lb_wage_subsidies_block` | **Wage subsidies** block (~2/3 enterprise package) | **~16.7 bn** class | 7 | 9.5 | 7 | **7.98** | Systemic labour-cost package |
| 9 | `lb_ffs_direct_total` | Federal **direct FFS** total | **10.78 bn** | 7 | 9.5 | 7 | **7.98** | Fossil opportunity-cost inventory |
| 10 | `lb_gas_product_diff` | **Gas product rate-diff** vs gasoline TOE | **4.09 bn** | 7 | 9.5 | 7 | **7.98** | Largest single FFS product line |

### Just outside top 10 (often relevant)

| # | ID | Annual € | Priority | Note |
|---|-----|----------:|---------:|------|
| 11 | `lb_union_pay_admin_169m` | **169 m** | 7.90 | Union unemployment **payment admin** (middleman) |
| 12 | `lb_vl_non_maastricht` | **2.66 bn** stock class | 7.83 | Flanders non-Maastricht federal claims |
| — | `lb_vl_wassalon_podcast` | **~0.27 m**/yr (**0.8 m**/3y) | **7.4** | **Highest absurdity (9.5)** — reach vs spend |

---

## “Clown / high absurdity” shortlist (not pure size)

| Rank by abs | ID | Abs | Annual € class | One-liner |
|-------------|-----|----:|---------------:|-----------|
| 1 | `lb_vl_wassalon_podcast` | **9.5** | 0.27 m (0.8 m / 3y) | **Het Wassalon** gelijke-kansen vodcast/campagne |
| 2 | `lb_cheque_economy` | **9** | 1.07 bn | Restricted cheques admin sandwich |
| 3–4 | company cars rows | **8–8.5** | 3–5 bn | Fringe mobility tax design |
| 5 | heating oil FFS | **8** | 1.84 bn | Fossil heat preference |
| 6 | GSC Flanders | **8** | ~0.8 bn/yr | Certificate support on bill |
| 7 | union pay admin | **8.5** | 169 m | Parallel payment channels |

---

## Caveats

1. **Tax expenditures / FFS are not cash out of the €348 bn TE pie** the same way as FOREM grants — still real fiscal cost.  
2. **Large legitimate spend** (pensions, hospitals BFM, STIB, universities) is mostly **not** in this top 10 because absurdity is lower even when cost is huge.  
3. **Recompute** after major taxex/FFS or L5 waves: run sort on `leaderboard.csv` and overwrite this file.  
4. Full table: `leaderboard.csv` · historical top15 snapshot may lag: `leaderboard_top15.md`.

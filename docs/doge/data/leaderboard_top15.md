# DOGE leaderboard top 15 (recomputed)

**Tick 115** (2026-07-27): full recompute after FFS wave (ticks 109–114).  
Formula: `priority = 0.55*cost_score + 0.35*absurdity + 0.10*(10-difficulty)`  
`cost_score` refreshed from `annual_cost_eur` bands: &lt;1m→1.5 · &lt;10m→3.5 · &lt;100m→5.5 · &lt;1bn→7.5 · ≥1bn→9.5.  
No invented euros; stocks stored as annual EUR still rank by that field (e.g. non-Maastricht claims).

| Rank | ID | Name | Annual € | Abs | Cost | Diff | Priority |
|------|-----|------|----------|-----|------|------|----------|
| 1 | `lb_cheque_economy` | Cheque economy (eco/meal/other restricted vouchers | 1400000000 | 9 | 9.5 | 7 | **8.68** |
| 2 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | 1836400000 | 8 | 9.5 | 6 | **8.43** |
| 3 | `lb_company_cars` | Company cars tax expenditure package | 3141700000 | 8 | 9.5 | 8 | **8.22** |
| 4 | `lb_eiwt_package` | EIWT partial remittance bedrijfsvoorheffing packag | 4356060000 | 7 | 9.5 | 6 | **8.08** |
| 5 | `lb_eiwt_night_shift_cluster` | EIWT night+shift+continuous+construction cluster | 2041520000 | 7 | 9.5 | 6 | **8.08** |
| 6 | `lb_wage_subsidies_block` | Wage subsidies block (~2/3 of enterprise package) | 16700000000 | 7 | 9.5 | 7 | **7.98** |
| 7 | `lb_ffs_direct_total` | Federal direct fossil fuel subsidies total FFS | 10781900000 | 7 | 9.5 | 7 | **7.98** |
| 8 | `lb_gas_product_diff` | Natural gas product rate-diff vs gasoline TOE (FFS | 4089400000 | 7 | 9.5 | 7 | **7.98** |
| 9 | `lb_vl_non_maastricht` | Flanders non-Maastricht federal claims | 2658100000 | 6 | 9.5 | 5 | **7.83** |
| 10 | `lb_vat_horeca` | VAT reduced rate Horeca | 1199270000 | 6 | 9.5 | 6 | **7.73** |
| 11 | `lb_maribel_social_funds` | Maribel Social Funds wage subsidies package | 1520000000 | 6 | 9.5 | 6 | **7.73** |
| 12 | `lb_wal_feder_ftj_envelope` | Wallonie FEDER/FTJ 2021-27 co-financed investment  | 1488000000 | 6 | 9.5 | 6 | **7.73** |
| 13 | `lb_nbb_ent_subsidies` | BE enterprise subsidies+investment grants package | 25100000000 | 6 | 9.5 | 8 | **7.53** |
| 14 | `lb_de_lijn_dotatie` | De Lijn Flanders operating subsidy (dotatie) | 1140000000 | 5 | 9.5 | 6 | **7.38** |
| 15 | `lb_eiwt_rd_cluster` | EIWT R&D researcher remittance exemptions | 1602580000 | 5 | 9.5 | 6 | **7.38** |

_All 157 rows sorted in `leaderboard.csv`._

# Federal financial transfers register (BOSA) — L2/L3 map

**Tick:** 130 · **Unit:** rq_124 · **As-of:** 2026-07-27  
**Primary:** FOD BOSA portal (Federaal register van financiële overdrachten + departmental/OISZ/AOI tables)

## Honesty first

- Register total **€179.916 bn (2025)** = **8,993** items.  
- **Household/ASBL €141.9 bn** is mostly **statutory social benefits** (pensions, unemployment, health), not “discretionary NGO gravy”.  
- Full **named L5 top-50 third parties** live in an interactive JS register (no bulk CSV this tick).  
- Do **not** add register total to S.13 TE €348 bn (large double-count / different perimeter).

## Register by beneficiary type (m€)

| Beneficiary type | 2023 | 2024 | 2025 |
|------------------|------|------|------|
| Households + ASBL | 126,880 | 135,284 | **141,915** |
| Regions + communities | 18,533 | 19,562 | **19,443** |
| Companies | 4,330 | 4,827 | **4,777** |
| Local governments | 4,380 | 4,515 | **4,682** |
| Wage-withholding TE (BV) | 4,415 | 4,385 | **4,668** |
| Foreign | 2,575 | 2,773 | **2,592** |
| SSC contribution exemptions (firms) | 963 | 917 | **943** |
| Maribel recruitment support | 284 | 318 | **894** |
| **Total** | **162,363** | **171,584** | **179,916** |

Source: BOSA register overview table.

## Departmental transfers only (m€)

| Destination | 2023 | 2024 | 2025* |
|-------------|------|------|-------|
| Social security institutions | 25,577 | 26,460 | **27,687** |
| Regions + communities | 17,214 | 17,068 | **17,730** |
| Autonomous institutions | 6,697 | 11,930 | **5,470** |
| Households + ASBL | 4,404 | 4,617 | **4,968** |
| Local governments | 3,828 | 3,930 | **4,110** |
| Companies | 2,627 | 2,604 | **3,075** |
| Foreign | 1,600 | 1,769 | **1,681** |
| **Dept subtotal** | **61,947** | **68,377** | **64,721** |
| + BV exemptions | 4,415 | 4,385 | 4,668 |
| **Dept + BV** | **66,362** | **72,762** | **69,389** |

\*2025 provisional until general account law.

## OISZ (social security institutions) outflows (m€)

| Destination | 2025 |
|-------------|------|
| Households + ASBL | **136,384** |
| Companies | 1,670 |
| Maribel hiring | 895 |
| SSC exemptions | 943 |
| Regions/communities | 1,634 |
| Local (Maribel) | 494 |
| Foreign | 902 |
| **OISZ total** | **142,955** |

## AOI (administrative public bodies) (m€; source table in k€)

| Destination | 2025 |
|-------------|------|
| Households + ASBL | 563.2 |
| Regions/communities | 79.7 |
| Local | 77.7 |
| Companies | 32.0 |
| **AOI total** | **774.3** |

## Three-group macro (BOSA overdrachten page, m€)

| Group | 2023 | 2024 | 2025 |
|-------|------|------|------|
| Tax expenditures (inventory) | 39,401 | n/a | n/a |
| Assignment funds (toewijzingsfondsen) | 77,336 | 78,385 | **83,552** |
| Department transfers | 61,947 | 68,378 | **64,721** |

2023 TE split (FPS via BOSA): VAT 16,198 · PIT federal 9,671 · BV 4,415 · CIT 3,809 · regional PIT 2,252 · excise 2,441 · capital WHT 615.

## “Top discretionary” interpretation (for DOGE)

| Priority band | 2025 EUR class | Comment |
|---------------|----------------|---------|
| Firms (dept+register companies) | ~3–5 bn | Best L5 hunt target |
| Maribel | ~0.9 bn register / higher NBB ESA | FOI fund split |
| Foreign (dev coop etc.) | ~1.7–2.6 bn | Named project FOI |
| Autonomous institutions | ~5.5 bn | NMBS-class agencies |
| HH/ASBL OISZ | ~136 bn | **Not** discretionary L5 |

## Residual for true L5 top 50 named

Interactive BOSA register has beneficiary name + KBO + amount. **No machine-readable bulk download** found this tick.  
Next: FOI/export request for top 50 by amount (excl. statutory SS benefit lines), or agent scrape if open API appears.

## Cross-links already in dataset

- NMBS ODC core3 ~€2.0–2.4 bn path  
- Meal vouchers CoA €1.07 bn parafiscal  
- EIWT / company cars / FFS taxex lines  
- Maribel FOI gap_maribel_l5_split  

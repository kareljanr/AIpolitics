# Stad Gent — L5 subsidies from open subsidieregister (tick 101)

**Primary source:** Open Data Portaal Stad Gent — *Subsidieregister Stad Gent en OCMW Gent*  
Dataset: `lijst-van-gesubsidieerde-derden-stad-gent`  
API/export: https://data.stad.gent/explore/assets/lijst-van-gesubsidieerde-derden-stad-gent/  
**Confidence: strong** (official charged amounts). **No invented euros.**

## Coverage caveats

- Years in register: **2020–2025** (columns per year).
- **2025 is partial** (portal: aangerekende bedragen vóór ~03/04/2025) — do **not** treat 2025 totals as full-year.
- Includes **intern** transfers (Politiezone, Ivago, Hulpverleningszone, AGBs) and **extern** third parties.
- `budgetpositie_soort`: Werking / Investering.
- Multi-year 2026–2031 culture awards not yet fully visible as full-year 2026 rows.

## Year totals (all groups, sum of charged amounts)

| Year | Sum € | Rows with amount |
|------|------:|-----------------:|
| 2020 | 285,054,985.50 | 2,515 |
| 2021 | 294,186,113.33 | 3,440 |
| 2022 | 280,585,781.81 | 3,358 |
| 2023 | 311,721,995.18 | 2,146 |
| **2024** | **331,933,746.42** | **1,897** |
| 2025 (partial) | 107,354,923.23 | 628 |

### 2024 split by `groep_gent`

| Group | Sum € |
|-------|------:|
| intern | 268,266,616.50 |
| **extern** | **63,667,129.92** |
| of which extern **Werking** only | **47,523,699.32** |

## Top 10 by 2024 charged amount (all groups)

| Rank | Beneficiary | 2024 € |
|-----:|-------------|-------:|
| 1 | Politiezone van Gent | 110,603,827.38 |
| 2 | Ivago | 62,685,760.48 |
| 3 | HULPVERLENINGSZONE CENTRUM | 42,254,533.07 |
| 4 | Farys | 10,436,502.25 |
| 5 | Integratie en inburgering Gent | 9,749,446.76 |
| 6 | THUISPUNT GENT | 9,687,680.54 |
| 7 | Kunsten en Design (intern) | 9,024,328.55 |
| 8 | Stadsontwikkeling Gent (sogent) | 6,899,716.20 |
| 9 | Autonoom Gemeentebedrijf Erfgoed | 4,966,698.63 |
| 10 | S&R Gent | 4,278,123.32 |

Top 3 = core local public-safety / waste / emergency-zone financing — **not** discretionary culture L5.

## Top 15 extern + Werking only (2024) — third-party ops L5

| Rank | Beneficiary | 2024 € |
|-----:|-------------|-------:|
| 1 | S&R Gent | 4,278,123.32 |
| 2 | JEUGDWELZIJNSWERK ONDERSTEUNINGSNET | 4,086,456.99 |
| 3 | **NTGent** | **2,725,450.76** |
| 4 | Centrum Algemeen Welzijnswerk | 2,621,651.85 |
| 5 | Opera Ballet Vlaanderen | 1,259,913.00 |
| 6 | VVM De Lijn - SSC Boekhouding | 1,233,810.67 |
| 7 | THUISPUNT GENT | 1,225,445.72 |
| 8 | SAAMO Gent | 873,694.32 |
| 9 | ATELJEE | 804,077.94 |
| 10 | TOPunt Gent | 663,122.36 |
| 11 | Huuringent | 649,143.70 |
| 12 | Kompas | 628,425.80 |
| 13 | Vlaamse Vervoermaatschappij - De Lijn | 622,706.46 |
| 14 | Voetbal in de stad | 514,661.84 |
| 15 | Minard | 510,212.00 |

## Cultuurdienst 2024 (dienst name contains “cultuur”)

| Metric | Value |
|--------|------:|
| Sum charged | **€11,559,532.52** |
| Unique beneficiaries | 311 |

### Top culture named lines 2024

| Beneficiary | 2024 € | Notes |
|-------------|-------:|-------|
| NTGent | 2,985,450.76 | Werking 2,725,450.76 + invest 260,000 |
| Opera Ballet Vlaanderen | 1,459,913.00 | |
| Muziekcentrum De Bijloke Gent | 993,259.00 | also large **intern** AGB lines outside this filter |
| Kunstencentrum VIERNULVIER | 965,374.30 | extern |
| Minard | 550,212.00 | |
| SPEELTEATER - KOPERGIETERY | 336,400.06 | |
| Kunsthal Gent vzw | 328,635.40 | |
| CAPITOLE | 326,000.00 | |
| Festival van Vlaanderen Gent | 278,277.11 | |
| Internationaal Filmfestival | 278,277.11 | |

### NTGent detail (primary rows)

| Type | 2023 € | 2024 € | 2025 € (partial) |
|------|--------:|-------:|-----------------:|
| Werking structural (main) | 2,678,193.11 | 2,711,679.45 | 1,137,836.42 |
| Werking structural (small) | 13,234.69 | 13,771.31 | — |
| Investering cultureel infra | 260,000.00 | 260,000.00 | 260,000.00 |
| **Total** | **2,951,427.80** | **2,985,450.76** | **1,397,836.42** |

Aligns with prior press/decision sample (~€2.59m werk + invest class); open register is stronger outturn.

## Antwerp recheck (same tick)

No parallel **city** open subsidieregister with named EUR amounts found this tick on antwerpen.be open-data portals (geo-heavy). **gap_antwerp_subsidies_top20** remains **ready** (human send). Provincial Antwerp werkingssubsidies already mapped under `prov_antwerpen` (not city).

## FOI impact

- **gap_gent_subsidies_top20**: **answered** for 2020–2025 register (2024 top20 + culture top); 2026 multi-year award table still incomplete publicly → optional follow-up FOI only if 2026 named list needed before register updates.
- **gap_antwerp_subsidies_top20**: still ready.

## Artefacts

- Compact extract: `raw/gent_subs_top_tick101.json`
- Full export local (not committed): `raw/gent_subs_full.json` (~5.8 MB)

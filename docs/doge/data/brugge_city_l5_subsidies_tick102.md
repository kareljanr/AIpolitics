# Stad Brugge + Ville de Namur — city open subsidy registers (tick 102)

**No invented euros.** Confidence tags below.

## 1. Stad Brugge — `subsidieregister` (strong)

**Primary:** https://data.brugge.be/explore/dataset/subsidieregister/  
**Rows:** 5,831 · **Years:** 2022–2026 · Fields: `jaar`, `bedrag`, `ontvangertoelage_beschrijving`, BBC policy codes.

### Year totals (sum of `bedrag`)

| Year | Sum € | Rows | Unique recipients | Note |
|------|------:|-----:|------------------:|------|
| 2022 | 88,941,813.36 | 1,326 | 994 | full-ish |
| 2023 | 94,761,863.53 | 1,530 | 1,126 | |
| **2024** | **99,253,041.87** | 1,389 | 1,067 | best recent full year |
| **2025** | **97,980,016.20** | 1,334 | 1,026 | |
| 2026 | 31,179,096.59 | 252 | 222 | **partial** early MJP loads |

### Top 10 2024 (all)

| Rank | Recipient | 2024 € |
|-----:|-----------|-------:|
| 1 | Politiezone van Brugge | 32,933,882.31 |
| 2 | Mintus (Zorgvereniging Brugge) | 26,186,642.03 |
| 3 | Hulpverleningszone 1 West-Vlaanderen | 10,077,985.00 |
| 4 | **BRUGGE PLUS VZW** | **7,317,327.56** |
| 5 | Gezin/Particulier | 3,435,463.54 |
| 6 | **Concertgebouw Brugge VZW** | **2,110,837.36** |
| 7 | Farys | 1,660,550.47 |
| 8 | Het Entrepot (jongerencultuur) | 1,086,176.25 |
| 9 | De Blauwe Lelie | 895,906.12 |
| 10 | Stadmakers VZW | 871,963.75 |

Top 3 = police / care / emergency zone — core public service financing, not discretionary culture L5.

### Named culture / city-marketing multi-year (charged)

| Recipient | 2022 € | 2023 € | 2024 € | 2025 € | 2026 € (partial) |
|-----------|-------:|-------:|-------:|-------:|-----------------:|
| Brugge Plus VZW | 5,605,772 | 7,316,835 | **7,317,328** | 7,025,228 | 2,458,854 |
| Concertgebouw Brugge | 1,316,556 | 1,849,307 | **2,110,837** | 1,263,055 | 1,425,000 |
| Het Entrepot | 906,443 | 965,900 | **1,086,176** | 1,019,766 | 720,000 |

Upgrades prior tick-029 sample (Concertgebouw ~705k+720k medium press/MJP fragments) with **strong open-data multi-year series**.

### 2026 partial — culture-ish field class

`Overige culturele instellingen` **€4,147,627** (55 orgs in culture keyword filter), led by Brugge Plus €2.18m + Concertgebouw €1.425m.

---

## 2. Ville de Namur — `subsides-attribues` (strong but **stale**)

**Primary:** https://data.namur.be/explore/assets/subsides-attribues/  
**Rows:** 156 only · **Years:** **2019–2020 only** (no 2021–2026 in open export this tick).

| Year | Sum budget_final € | Rows |
|------|-------------------:|-----:|
| 2019 | 3,159,538.23 | 39 |
| 2020 | 8,144,187.80 | 117 |

### Top 2020 named (illustrative history)

| Recipient | 2020 budget_final € |
|-----------|--------------------:|
| SONEFA ASBL | 2,134,967.30 |
| Centre culturel régional ASBL | 647,575.35 |
| CCR invest | 620,000.00 |
| Office du Tourisme ASBL | 440,792.19 |
| NEW ASBL | 403,500.00 |
| Comité animation citadelle | 327,000.00 |
| Canal C ASBL | 210,000.00 |
| FIFF (film) | 201,333.99 |

**Cross-check vs 2026 BI** (prior DOGE strong, DGF note — not this open dataset): monde associatif **€8,470,995**; SONEFA **€2,632,627**; CCR **€714,975**; OTN **€397,000**. Continuity of names; amounts not from same open table.

**Gap:** Namur open register not refreshed past 2020 → optional FOI / portal update ask (lower priority than Hainaut province ASBL).

---

## 3. Other cities this tick

| City | Open named EUR register? | Status |
|------|--------------------------|--------|
| Gent | Yes (tick 101) | answered |
| Brugge | **Yes (this tick)** | **strong 2022–2025** |
| Namur | Stale 2019–20 only | partial |
| Antwerp | Not found (tick 101) | FOI ready |
| Charleroi / Mons | Not found this tick | FOI ready / Mag aggregates only |

---

## Artefacts

- `raw/brugge_subs_top_tick102.json` (committed summary)
- `raw/namur_subsides_top_tick102.json` (committed summary)
- Full exports local only (Brugge ~3.5 MB not committed)

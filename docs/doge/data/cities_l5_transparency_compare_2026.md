# Belgian cities — L5 subsidy transparency compare (tick 104)

Synthesis only from DOGE ticks 101–103 (+ prior FOI queue). **No invented euros.**  
**Do not** sum Gent + Brugge + Mons register/PDF totals as one “Belgian city subsidy” headline — perimeters differ.

## Hard perimeter rules

| City | Artefact type | What is measured | Year focus |
|------|---------------|------------------|------------|
| **Gent** | Open **subsidieregister** (charged) | All groups incl. police/Ivago/zones + extern third parties | **2024 full**; 2025 partial |
| **Brugge** | Open **subsidieregister** (charged) | Recipients with `bedrag` by year | **2024–2025 full-ish**; 2026 partial |
| **Mons** | Official **budget PDF** (prévisions) | Named articles (ASBL/RCA/MARS…), not a machine register | **2025** ordinaire; **2026 PDF missing** |
| **Namur** | Open data (stale) + DGF BI2026 note | OD only 2019–20; 2026 associatif from budget note | Mixed |
| **Antwerp / Charleroi** | FOI only (this sprint) | No public named top-N EUR table found | FOI ready |

## Transparency ladder (best → worst public L5 discoverability)

1. **Gent** — open multi-year register, intern/extern split, dienst filters, culture total extractable  
2. **Brugge** — open multi-year register, recipient ranking, multi-year named culture series  
3. **Mons** — strong **PDF article** L5 for 2025; no open beneficiary register; 2026 FOI  
4. **Namur** — 2026 named lines in DGF note; open portal **stale to 2020**  
5. **Antwerp / Charleroi** — aggregates/press/forms; **FOI ready** for top-20 named EUR  

## Scale snapshots (sourced; not comparable 1:1)

| City | Metric | Amount € | Confidence |
|------|--------|---------:|------------|
| Gent | Register total 2024 (all groups) | **331,933,746** | strong |
| Gent | Extern only 2024 | **63,667,130** | strong |
| Gent | Extern + Werking 2024 | **47,523,699** | strong |
| Gent | Cultuurdienst 2024 | **11,559,533** | strong |
| Brugge | Register total 2024 | **99,253,042** | strong |
| Brugge | Register total 2025 | **97,980,016** | strong |
| Mons | Ord dépenses 2025 (budget) | **244,180,818** | strong |
| Mons | Ord recettes 2025 (budget) | **246,241,166** | strong |

**Invalid comparison:** “Gent subsidies 3× Brugge” using all-group register totals — Gent includes large intern police/waste/zone financing (€268m of €332m). Better L5 class for Gent is **extern+werking €47.5m** vs Brugge **full register €99m still includes police/Mintus/HVZ**.

### Core vs discretionary (same pattern both Flemish ODs)

| City | Core-ish top lines (2024) | Largest non-core named |
|------|---------------------------|------------------------|
| Gent | Politiezone €110.6m; Ivago €62.7m; HVZ €42.3m | NTGent **€2.99m**; S&R €4.28m; culture class €11.6m |
| Brugge | Politiezone €32.9m; Mintus €26.2m; HVZ €10.1m | **Brugge Plus €7.32m**; Concertgebouw **€2.11m**; Entrepot €1.09m |

## Named culture / marketing L5 (illustrative, strong where noted)

| City | Line | Year | EUR | Source style |
|------|------|------|----:|--------------|
| Gent | NTGent | 2024 | **2,985,451** | open register outturn |
| Gent | Opera Ballet Vlaanderen | 2024 | 1,459,913 | open register |
| Gent | VIERNULVIER | 2024 | 965,374 | open register |
| Brugge | Brugge Plus | 2024 | **7,317,328** | open register |
| Brugge | Concertgebouw | 2024 | **2,110,837** | open register |
| Brugge | Het Entrepot | 2024 | 1,086,176 | open register |
| Mons | MARS package (3 lines) | 2025 | **674,000** | budget PDF |
| Mons | Fondation Mons 2025 | 2025 | 110,000 | budget PDF |
| Mons | Festival film | 2025 | 45,000 | budget PDF |
| Mons | Charte vie associative activités | 2025 | 100,000 | budget PDF |

**Do not rank “waste”** across these without outcome data — amounts are transparency facts, not absurdity scores alone.

## Mechanism takeaways

1. **Open register beats PDF scraping** for waste mapping: Gent/Brugge allow top-N ranked beneficiaries in minutes; Mons requires 121-page article mining.  
2. **Flemish BBC cities** in this sample publish machine-readable charged series; **Walloon** cities lag (Mons PDF good for 2025 articles; Namur OD frozen; Charleroi forms-only).  
3. **Register totals are not “subsidy waste pools”** — police, zones, care, utilities dominate top lines in Gent and Brugge.  
4. Remaining public work is thin: **Antwerp + Charleroi + Mons BI2026 + Hainaut/Lux province ASBL** are mostly **FOI human-send**, not more scraping.  
5. Parallel to provincial dualism (tick 100): city-layer dualism is **open register (VL sample) vs PDF/FOI (WAL sample)** — institutional pattern, not scapegoat.

## FOI stack (human send only)

| Gap | City/entity | Why still open |
|-----|-------------|----------------|
| `gap_antwerp_subsidies_top20` | Antwerp | No open named EUR register found |
| `gap_charleroi_subsidies_top20` | Charleroi | Forms only; no named list |
| `gap_mons_budget_l5` | Mons | 2025 filled; **2026 PDF** still missing |
| `gap_hainaut_asbl_list_2026` | Prov Hainaut | 199 entities amounts |
| `gap_lux_asbl_list_2026` | Prov Luxembourg | Named list for €4.3m package |
| `gap_gent_subsidies_top20` | Gent | **Answered** tick 101 |

## Cross-links

- Gent: `gent_city_l5_subsidies_2024.md`  
- Brugge/Namur: `brugge_city_l5_subsidies_tick102.md`  
- Mons: `mons_city_l5_budget_2025.md`  
- Province dual: `provinces_vl_wal_l5_opacity_2026.md`  

Sources: `src_gent_subsidieregister_od`, `src_brugge_subsidieregister_od`, `src_mons_budget_ord_2025`, `src_namur_subsides_attribues_od`, synthesis `src_doge_cities_l5_transparency_2026`.

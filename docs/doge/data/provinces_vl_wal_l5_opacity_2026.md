# Flemish vs Walloon provinces — L5 opacity cross-compare 2026

Synthesis only from DOGE maps:

- Flemish L1: `flemish_provinces_2026_snapshot.md` (ticks 78–89)
- Flemish L5 agencies: `flemish_provinces_l5_agencies_2026.md` (ticks 90–94)
- Walloon L1: `walloon_provinces_2026_snapshot.md` (ticks 72–77)
- Walloon L5 ASBL: `walloon_provinces_l5_asbl_2026.md` (ticks 95–99)

**No invented euros.** Metrics are **not addable across regions** without perimeter caveats.

## Hard perimeter rules

| Dimension | Flanders (5 provinces) | Wallonia (5 provinces) |
|-----------|------------------------|-------------------------|
| Budget system | BBC (exploitatie / investering / financiering) | Ordinaire / extraordinaire (+ CoA projet for most) |
| L5 label in sources | Toegestane **werkingssubsidies**; nominatieve verbonden entiteiten; APB packages | CoA **ASBL/FUP aids ≥€50k** annex; named budget articles (Liège) |
| Best public artefacts | Official MJP / Documentatie / T2 tables | CoA budget reports + Liège official PDF |
| Do **not** | Call VL werkingssubsidies = WAL ASBL package | Sum known WAL ASBL totals as “all provincial subsidies” |

## Scale context (L1 — different accounting)

| Metric | Flanders | Wallonia | Note |
|--------|---------:|---------:|------|
| Primary spend sum 2026 | Exp uit **€1,110,597,112** | Ord dep **€1,932,150,627** | Not comparable 1:1 |
| Broader outlay sum | Cash-out **€1,499,003,428** | Ord+extra **€2,069,243,296** | WAL still heavier education/security in province layer |
| Largest province | OVL exp €313.2m / cash-out €379.9m | Hainaut ord €830.6m / total €854.1m | Hainaut alone ~43% of WAL ord |
| Zones / safety transfer | (commune-centric; not same line) | Zones sum **€188.2m** (+ Hainaut provision path €194.2m) | WAL structural shift |

## L5 money that is publicly known (sourced)

### Flanders — third-party / agency layer

| Metric | Amount € | Confidence |
|--------|---------:|------------|
| Werkingssubsidies sum (5) | **194,175,471** | strong |
| Named POM-class (4; ANT n/a) | **20,079,246** | strong |
| Named tourism agencies (4) | **18,392,947** | strong |
| POM + tourism named (4) | **38,472,193** | strong |
| WVL share of POM+tourism 4 | **59%** (€22.7m of €38.5m) | strong |
| Antwerp APB package (13 cos) | **38,925,780** | strong; **not** POM-equivalent |

Rank werkingssubsidies: ANT 63.8m > WVL 54.4m > OVL 30.7m > LIM 25.9m > VBR 19.4m.

### Wallonia — ASBL / extraprovincial layer

| Metric | Amount / count | Confidence |
|--------|---------------:|------------|
| Known package totals (BW + Lux only) | **€14,300,000** | strong |
| BW package (31 entities, motivated) | **€10,000,000** | strong |
| Lux package (−17.8% vs 2025) | **€4,300,000** | strong |
| Entity counts Hainaut+BW+Namur | **240** (199+31+10) | strong |
| Hainaut package EUR | **unknown public** | FOI ready |
| Namur package EUR | **unknown public** | 10 entities; 3 unmotivated |
| Liège CoA ≥50k package | **not extracted as annex total** | named sample only |

**Do not invent** a 5-province Walloon ASBL euro total.

## Opacity patterns (mechanism comparison)

| Pattern | Flanders | Wallonia |
|---------|----------|----------|
| Named L5 in budget docs | Often **yes** (nominatieve entiteiten, T2 splits, Documentatie) | **Uneven**: Liège articles + BW total/motivation; Hainaut/Lux names weak in public CoA body |
| Aggregate third-party class | **Yes** — werkingssubsidies line all 5 | Partial — BW/Lux totals; Hainaut/Namur counts without EUR |
| Motivation for externalisation | Implicit via MJP policy notes | CoA explicitly scores: BW good; Namur 3 gaps; **Hainaut none** |
| Worst public L5 hole | ANT “andere begunstigden” bulk without full top-N open data | **Hainaut 199 entities** amounts + motivation |
| FOI drafted this sprint | (earlier city FOIs; province L5 largely public) | **gap_hainaut_asbl_list_2026**, **gap_lux_asbl_list_2026** ready |

### Opacity rank (province-layer L5, qualitative)

**Flanders (best → worse discoverability):** WVL / LIM / OVL / VBR named samples strong → ANT APB total known but 13-company per-line incomplete.  
**Wallonia (best → worse):** BW (total+motivation) → Liège named sample → Namur count → Lux total without names → **Hainaut count without amounts/motivation**.

## Structural takeaways (not scapegoats)

1. **Accounting dualism** blocks a single “Belgian provincial subsidy” headline. BBC werkingssubsidies ≠ CoA ASBL ≥50k annex.
2. **Flanders wins on machine-readable named L5** in official MJP artefacts; waste debate can often start from public tables.
3. **Wallonia’s largest province is the most opaque** on extraprovincial ASBL money — CoA already flags missing motivation; FOI is the next evidence step, not more PDF scraping of CoA bodies.
4. **Agency concentration differs:** WVL four-agency stack ~€33.9m (POM+Westtoer+Inagro+TUA); ANT APB €38.9m; WAL known packages are smaller **where published** (€14.3m BW+Lux) but Hainaut’s 199-entity annex could be large — **unknown**, not zero.
5. **Parallel pressure mechanisms outside L5:** WAL pension debudgeting (Namur €10m, Lux €3.1m); VL large onderwijs pass-through in personnel (OVL/LIM) — both reduce comparability of “ops” lines.

## Policy-facing evidence grade

| Claim | Grade |
|-------|-------|
| VL 5-prov werkingssubsidies = €194.2m 2026 | **strong** (sum of primary T2/Documentatie rows) |
| WAL known ASBL packages BW+Lux = €14.3m | **strong** (CoA text) |
| Hainaut has 199 entities ≥€50k without public EUR list | **strong** process (CoA + negative public search) |
| “Walloon provinces spend less on ASBL than Flanders on werkingssubsidies” | **invalid / unsupported** — incomplete WAL perimeter |
| Dual NL/FR provincial transparency gap exists | **medium–strong** as institutional pattern from these maps |

## Cross-links

- FOI ready (human send): `gap_hainaut_asbl_list_2026`, `gap_lux_asbl_list_2026`
- Leaderboard: `lb_vl_werkingssubsidies_sum` (if present), `lb_walloon_asbl_opacity_rank`
- Commitments: `cmt_walloon_asbl_opacity_compare_2026`; Flemish L5 compare sources

Sources: `src_doge_flemish_l5_compare_2026`, `src_doge_walloon_prov_l5_2026`, `src_doge_flemish_prov_compare_2026`, `src_doge_walloon_prov_compare_2026`, plus underlying primary rows in those files.

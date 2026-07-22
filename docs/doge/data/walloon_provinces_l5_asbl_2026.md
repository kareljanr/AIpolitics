# Walloon provinces — L5 ASBL / extraprovincial compare 2026

Synthesis only from DOGE ticks 95–98 primary CoA / province budget rows. **No invented euros.**

## Caveats

- **Liège** figures from official province Budget 2026 PDF; **others** from Cour des comptes **projet** reports (final conseil + tutelle may differ).
- CoA “ASBL/FUP aids ≥€50k” is a **consolidated annex metric**, not identical to all third-party transfers (e.g. zones de secours, education pass-throughs).
- **Do not invent** a 5-province ASBL euro total: only BW (€10.0m) and Lux (€4.3m) publish package totals in CoA text. Hainaut/Namur counts without package EUR; Liège is a named-sample budget extract, not a CoA ≥50k annex total.
- Named entity lists for Hainaut (199) and Luxembourg (package total only) remain **FOI-ready, human send only**.

## Master compare (ASBL / extraprovincial L5)

| Province | Entities ≥€50k | Package EUR (CoA text) | Motivation / transparency | FOI status |
|----------|---------------:|-----------------------:|---------------------------|------------|
| **Hainaut** | **199** | n/a (annex exists, amounts not in public CoA PDF) | **None** for extraprovincialisation (CoA flag) | `gap_hainaut_asbl_list_2026` **ready** |
| **Brabant wallon** | **31** | **€10,000,000** | **Explicit** motivations | names still not machine-public |
| **Namur** | **10** | n/a | 7/10 yes; **3 missing** | no FOI yet (count small; optional) |
| **Luxembourg** | count n/a in CoA body | **€4,300,000** (−€0.9m / −17.8% vs 2025) | partial (eval annex = management-contract entities only) | `gap_lux_asbl_list_2026` **ready** |
| **Liège** | n/a annex metric | n/a package total | per-article named sample in budget PDF | sample public; full register not bulk |

### Derived metrics (sourced only)

| Metric | Value | Notes |
|--------|------:|-------|
| Entity counts with known ≥50k lists | **240** | Hainaut 199 + BW 31 + Namur 10 (Lux/Liège not in this sum) |
| Known package EUR totals | **€14,300,000** | BW €10.0m + Lux €4.3m only |
| Management contracts 2024 (CoA) | Hainaut **53** / BW **34** / Lux **25** / Namur **21** | different perimeter from ≥50k list |
| Opacity rank (worst → best total disclosure) | **Hainaut > Lux (names) > Namur > Liège sample > BW** | BW best on **total + motivation**; Hainaut worst |

## Named L5 samples (not package totals)

### Hainaut (CoA)

| Line | EUR | Note |
|------|----:|------|
| ASBL Voies d'eau du Hainaut | **2,300,000** | includes **+1,800,000** severance after canal tourism stop |
| ASBL Teralis | **0** | cut (was ~0.4m); French domains sold |
| Cathédrale Tournai invest | **3,900,000** | of which ~3.7m external subsidy |
| Transfers hors zones | **15,500,000** | class; not full ASBL list |

### Brabant wallon (CoA) — package €10.0m / 31 entities

Named invest (extra), not full ASBL list:

| Line | EUR |
|------|----:|
| Bassins d'orage | 3,100,000 |
| Brasserie Château d'Hélécine | 1,300,000 |
| Points-nœuds cyclables | 1,200,000 |
| IPES Wavre suite | 800,000 |
| Aviq overpayment provision | 1,800,000 |

### Namur (CoA)

| Line | EUR / note |
|------|------------|
| Entities ≥50k | **10** (3 unmotivated) |
| Chevetogne régie path | **−0.2m** vs 2025 adj. |
| BEP path | **−0.4m** vs 2025 adj. |
| Police academy federal receipt | **1,600,000** |
| Pension cotisations debudgeted | **10,000,000** (Ethias path; not ASBL) |

### Luxembourg (CoA) — package €4.3m

| Line | EUR |
|------|----:|
| ASBL/FUP ≥50k package | **4,300,000** |
| Cours d'eau invest | 1,300,000 |
| Maison culture Arlon roof | 2,800,000 (contingent Ville Arlon match; CoA: no justificatory piece) |
| Cancer screening vehicle AVIQ | 500,000 |
| Centres de santé invest | 600,000 |
| Palais annex | 500,000 |
| Pension shortfall Ethias | 3,100,000 (not ASBL) |

### Liège (official budget sample)

| Line | EUR |
|------|----:|
| Tourism sites paraprovinciaux | 516,011 |
| MNEMA | 150,000 |
| Service social agents | 190,878 |
| GIG | 110,000 |
| Opera Royal de Wallonie | 150,000 |
| OPL | 70,000 |
| Théâtre de Liège | 60,000 |
| Culture named sum (3) | **280,000** |
| FTPL (Fédération Tourisme) | **1** (was ~1.2m 2025 — major cut/restructure) |
| DG cooperation germanophone | 871,000 |

## Cross-links

- Budget L1 map (ord/extra/zones): `walloon_provinces_2026_snapshot.md`
- FOI ready (human send): `gap_hainaut_asbl_list_2026`, `gap_lux_asbl_list_2026`
- Commitments: `cmt_walloon_asbl_opacity_compare_2026`, `cmt_bw_prov_asbl_aids_2026`, `cmt_lux_asbl_package_2026`
- Leaderboard: `lb_walloon_asbl_opacity_rank`, `lb_hainaut_asbl_opacity`, `lb_bw_asbl_package`, `lb_lux_asbl_package`

## Policy takeaway (mechanisms, not scapegoats)

1. **Opacity is structural**: largest province (Hainaut) has the largest entity count and the weakest public motivation/amount disclosure.
2. **BW shows a feasible transparency floor**: package total + explicit motivations in CoA text — still short of open named EUR tables.
3. **Pension debudgeting** (Namur €10m, Lux €3.1m) is a separate fiscal-pressure mechanism, not L5 waste, but reduces budget visibility.
4. Remaining money discovery for this layer is mostly **FOI / open-data publication**, not more PDF scraping of CoA bodies.

Sources: `src_ccrek_hainaut_*`, `src_ccrek_bw_*`, `src_ccrek_namur_*`, `src_ccrek_lux_*`, `src_liege_prov_budget_*`, synthesis `src_doge_walloon_prov_l5_2026`.

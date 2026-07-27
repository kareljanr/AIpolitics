# Belgium Historical Waste Hall of Fame (Top 100)

**Sister board to DOGE (current spend) and Proposal Radar (new ideas).**  
This board scores **past and multi-year** public money disasters: ghost infrastructure, bailouts, IT flops, structural tax expenditures, and policy design failures.

| | |
|--|--|
| **As-of** | 2026-07-27 seed v1 |
| **Entries** | 107 |
| **Data** | [`data/historical_waste_hall.csv`](data/historical_waste_hall.csv) |
| **Pain unit** | Same as Proposal Radar `taxpayer_unit` v2 |
| **Honesty** | Ranges + confidence; **not** audited campaign claims |

---

## What this is (and is not)

| This is | This is not |
|---------|-------------|
| A **research seed** of Belgium’s most expensive bad decisions | A claim that every euro was illegal |
| Ranked by **waste_priority** = 0.45×cost_score + 0.30×absurdity + 0.25×purity | Pure size ranking of all public spend |
| Pain columns: how much **work** funds the mid € estimate | Precision finer than the underlying € confidence |
| Mix of ghost tunnels **and** multi-year taxex / bailouts / laws | Only ‘funny bridges’ tourism |

**Steelman rule:** many large rows are *mixed* public goods with a waste *component* (e.g. rail PSO, nuclear policy). `waste_purity` captures that. High cash + low purity still ranks — but notes say so.

**Do not sum the column.** Many multi-year structural rows overlap (company cars ⊂ taxex total; PV boom ⊂ GSC; etc.).

---

## Taxpayer pain (same metrics as Proposal Radar)

| Column | Meaning |
|--------|---------|
| **Belasting-FTE** (`pain_tax_fte`) | Mid public € ÷ €19,400 = how many average workers’ **full yearly labour-tax bill** |
| **Nettoloon-jaren** (`pain_net_years`) | Mid public € ÷ €29,500 = years of one person’s **take-home pay** |
| **Werkminuten** (`pain_work_minutes`) | If split across **all ~4.85m** Belgian employees: minutes of work **each** put in |

Unit: average single FT employee; OECD Taxing Wages-style labour tax; see [`../proposal-radar/TAXPAYER_UNIT.md`](../proposal-radar/TAXPAYER_UNIT.md).

---

## Ranking formula

```text
cost_score bands (mid €): <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5
waste_priority = 0.45×cost_score + 0.30×absurdity + 0.25×waste_purity
```

| Score | Meaning |
|-------|---------|
| **Absurdity** 1–10 | Goal failure, perverse incentives, capture, complexity theatre |
| **Waste purity** 1–10 | 10 = pure boondoggle / failed IT; 3 = large mixed public good with efficiency gap |
| **Confidence** | strong / medium / weak on the euro mid-point |

---

## Top 25 by waste_priority (headline)

| # | Name | Era | Mid € | Abs | Pur | **Prio** | Belasting-FTE | Werkminuten/employee | Conf |
|--:|------|-----|------:|----:|----:|---------:|--------------:|---------------------:|:----:|
| 1 | Charleroi light metro — half-built network, ghost branches | 1970s–2020s | €1.50 bn | 9.5 | 9.0 | **9.38** | 77,320 | 634 min (~10.6 h) | W |
| 2 | Waffle-iron politics legacy capex (post-war compensatory spending patt | 1950s–1980s | €30.00 bn | 9.0 | 8.0 | **8.97** | 1,546,392 | 12687 min (~8.8 d) | W |
| 3 | Brussels Metro line 3 — +hundreds-% budget path / freeze | 2009–2020s | €4.76 bn | 9.0 | 8.0 | **8.97** | 245,361 | 2013 min (~1.4 d) | S |
| 4 | Smeerpijp (Limburg–Antwerp industrial sewer never used) | 1960s–1970s | €100.0 m | 10.0 | 10.0 | **8.88** | 5,155 | 42.3 min | W |
| 5 | Fuel cards PIT+SSC tax expenditure (multi-year with company cars) | 2015–2025 | €7.00 bn | 8.5 | 8.0 | **8.82** | 360,825 | 2960 min (~2.1 d) | S |
| 6 | Flanders residential PV over-subsidy boom (certificates era) | 2009–2015 | €4.00 bn | 8.5 | 8.0 | **8.82** | 206,186 | 1692 min (~1.2 d) | M |
| 7 | Walloon PV / green certificate overcompensation path | 2008–2018 | €3.00 bn | 8.5 | 8.0 | **8.82** | 154,639 | 1269 min (~21.1 h) | M |
| 8 | Housing supply blocks + compensatory subsidies (policy package) | 1990s–2020s | €30.00 bn | 9.0 | 7.0 | **8.72** | 1,546,392 | 12687 min (~8.8 d) | W |
| 9 | Union unemployment payment admin grants (multi-year) | 2015–2025 | €1.70 bn | 8.5 | 7.5 | **8.70** | 87,629 | 719 min (~12.0 h) | S |
| 10 | Duplicate digital portals across governments (cluster) | 2000s–2020s | €1.50 bn | 8.0 | 8.0 | **8.68** | 77,320 | 634 min (~10.6 h) | W |
| 11 | i-Police federal police digitalisation failure | 2019–2026 | €150.0 m | 9.5 | 9.5 | **8.60** | 7,732 | 63 min (~1.1 h) | S |
| 12 | Company-car tax expenditure package (10y class) | 2015–2025 | €35.00 bn | 8.5 | 7.0 | **8.57** | 1,804,124 | 14801 min (~10.3 d) | S |
| 13 | Dexia dismantling + Belfius nationalisation path | 2008–2012 | €7.00 bn | 8.5 | 7.0 | **8.57** | 360,825 | 2960 min (~2.1 d) | M |
| 14 | Brussels North Quarter / WTC towers — unfinished urban plan | 1960s–1990s | €1.50 bn | 8.5 | 7.0 | **8.57** | 77,320 | 634 min (~10.6 h) | W |
| 15 | Party / political-group / media-adjacent public transfers opacity | 1990s–2020s | €1.50 bn | 8.5 | 7.0 | **8.57** | 77,320 | 634 min (~10.6 h) | W |
| 16 | International aviation kerosene excise exemption (10y) | 2015–2025 | €7.00 bn | 8.0 | 7.5 | **8.55** | 360,825 | 2960 min (~2.1 d) | S |
| 17 | Fyra / V250 high-speed train fiasco (BE share of write-downs) | 2000s–2010s | €250.0 m | 9.5 | 9.0 | **8.47** | 12,887 | 106 min (~1.8 h) | W |
| 18 | Heating gasoil excise preference (multi-year FFS) | 2015–2025 | €18.00 bn | 8.0 | 7.0 | **8.43** | 927,835 | 7612 min (~5.3 d) | S |
| 19 | Flanders green electricity certificates (GSC) support path | 2005–2025 | €12.00 bn | 8.0 | 7.0 | **8.43** | 618,557 | 5075 min (~3.5 d) | M |
| 20 | Brussels RER/GEN suburban rail — decades of delay & partial delivery | 1990s–2020s | €5.00 bn | 8.0 | 7.0 | **8.43** | 257,732 | 2114 min (~1.5 d) | W |
| 21 | Social housing vacancy & renovation backlog costs | 2000s–2020s | €3.00 bn | 8.0 | 7.0 | **8.43** | 154,639 | 1269 min (~21.1 h) | W |
| 22 | Ministerial cabinets culture — oversized political staff (multi-year) | 1990s–2020s | €3.00 bn | 8.0 | 7.0 | **8.43** | 154,639 | 1269 min (~21.1 h) | W |
| 23 | Temporary unemployment / crisis unemployment fraud & overuse | 2020–2022 | €2.00 bn | 8.0 | 7.0 | **8.43** | 103,093 | 846 min (~14.1 h) | W |
| 24 | Sabena bankruptcy — public shareholding losses + social fallout | 1990s–2001 | €1.50 bn | 8.0 | 7.0 | **8.43** | 77,320 | 634 min (~10.6 h) | W |
| 25 | Excess profit tax rulings (EU state-aid recovery saga) | 2005–2020s | €1.00 bn | 8.0 | 7.0 | **8.43** | 51,546 | 423 min (~7.0 h) | W |

### Also: Top 15 by mid € (size, not purity)

| Mid € | Name | Abs | Pur | Prio rank | Werkminuten/employee |
|------:|------|----:|----:|----------:|---------------------:|
| €200.00 bn | Federal tax expenditures total quantified (5–10y class) | 5.0 | 3.0 | #100 | 84579 min (~58.7 d) |
| €100.00 bn | Federal fossil-fuel subsidy inventory (10y class) | 7.0 | 5.0 | #57 | 42289 min (~29.4 d) |
| €100.00 bn | Wage-subsidy / labour-tax wedge compensation stack (mul | 7.0 | 4.0 | #72 | 42289 min (~29.4 d) |
| €100.00 bn | Primary balance gap vs debt-stabilising path (multi-yea | 6.0 | 5.0 | #74 | 42289 min (~29.4 d) |
| €60.00 bn | Early labour-market exit & special pension schemes (mul | 8.0 | 6.0 | #34 | 25374 min (~17.6 d) |
| €40.00 bn | Institutional dualism overhead (multi-parliaments, dual | 8.0 | 6.0 | #35 | 16916 min (~11.7 d) |
| €40.00 bn | EIWT partial remittance bedrijfsvoorheffing package (10 | 7.0 | 5.0 | #58 | 16916 min (~11.7 d) |
| €35.00 bn | Company-car tax expenditure package (10y class) | 8.5 | 7.0 | #12 | 14801 min (~10.3 d) |
| €30.00 bn | Waffle-iron politics legacy capex (post-war compensator | 9.0 | 8.0 | #2 | 12687 min (~8.8 d) |
| €30.00 bn | Housing supply blocks + compensatory subsidies (policy  | 9.0 | 7.0 | #8 | 12687 min (~8.8 d) |
| €30.00 bn | Notional interest deduction (NID) multi-year deadweight | 7.5 | 6.0 | #43 | 12687 min (~8.8 d) |
| €25.00 bn | Service vouchers (dienstencheques) multi-year fiscal co | 6.5 | 5.0 | #67 | 10572 min (~7.3 d) |
| €25.00 bn | Low-value care / billing waste in health insurance (sub | 6.0 | 5.0 | #75 | 10572 min (~7.3 d) |
| €22.00 bn | Banking crisis public capital injections (Fortis/Dexia/ | 8.0 | 6.0 | #36 | 9304 min (~6.5 d) |
| €20.00 bn | Professional order / permit denseness entry barriers (d | 7.0 | 6.0 | #46 | 8458 min (~5.9 d) |

---

## Full ranked list (all entries)

| # | Name | Category | Level | Mid € | Abs | Pur | Prio | Belasting-FTE | Nettoloon-jaren | Werkminuten | €/employee | Conf | One-liner |
|--:|------|----------|-------|------:|----:|----:|-----:|--------------:|----------------:|------------:|-----------:|:----:|-----------|
| 1 | Charleroi light metro — half-built network, ghost branc | ghost_infra | Wallonia | €1.50 bn | 9.5 | 9.0 | 9.38 | 77,320 | 50,848 | 634 min (~10.6 h) | €309 | W | Eight arms planned, ghost tunnels for decades — waffle-iron metro politics in co |
| 2 | Waffle-iron politics legacy capex (post-war compensator | institutions | federal | €30.00 bn | 9.0 | 8.0 | 8.97 | 1,546,392 | 1,016,949 | 12687 min (~8.8 d) | €6,186 | W | You get a tunnel because they got a bridge — Belgium’s original fiscal algorithm |
| 3 | Brussels Metro line 3 — +hundreds-% budget path / freez | transport_capex | Brussels | €4.76 bn | 9.0 | 8.0 | 8.97 | 245,361 | 161,356 | 2013 min (~1.4 d) | €981 | S | A north–south metro that spent like a moonshot before a single full line ran. |
| 4 | Smeerpijp (Limburg–Antwerp industrial sewer never used) | ghost_infra | Flanders | €100.0 m | 10.0 | 10.0 | 8.88 | 5,155 | 3,390 | 42.3 min | €21 | W | A 107 km pollution pipe that never carried a drop — purity score: perfect 10. |
| 5 | Fuel cards PIT+SSC tax expenditure (multi-year with com | structural_fiscal | federal | €7.00 bn | 8.5 | 8.0 | 8.82 | 360,825 | 237,288 | 2960 min (~2.1 d) | €1,443 | S | Free fuel as wage — congestion externality included free of charge. |
| 6 | Flanders residential PV over-subsidy boom (certificates | energy_policy | Flanders | €4.00 bn | 8.5 | 8.0 | 8.82 | 206,186 | 135,593 | 1692 min (~1.2 d) | €825 | M | Rooftop gold rush with guaranteed certificates — non-PV households paid. |
| 7 | Walloon PV / green certificate overcompensation path | energy_policy | Wallonia | €3.00 bn | 8.5 | 8.0 | 8.82 | 154,639 | 101,695 | 1269 min (~21.1 h) | €619 | M | Same movie as Flanders, French-speaking soundtrack, same bill on the meter. |
| 8 | Housing supply blocks + compensatory subsidies (policy  | housing | multi | €30.00 bn | 9.0 | 7.0 | 8.72 | 1,546,392 | 1,016,949 | 12687 min (~8.8 d) | €6,186 | W | Cause the shortage, then subsidise the victims of the shortage. |
| 9 | Union unemployment payment admin grants (multi-year) | labour_market | federal | €1.70 bn | 8.5 | 7.5 | 8.70 | 87,629 | 57,627 | 719 min (~12.0 h) | €351 | S | Unions paid to pay unemployment — a Belgian special. |
| 10 | Duplicate digital portals across governments (cluster) | it_failure | multi | €1.50 bn | 8.0 | 8.0 | 8.68 | 77,320 | 50,848 | 634 min (~10.6 h) | €309 | W | My e-box, your e-box, their e-box — federalism as UX debt. |
| 11 | i-Police federal police digitalisation failure | it_failure | federal | €150.0 m | 9.5 | 9.5 | 8.60 | 7,732 | 5,085 | 63 min (~1.1 h) | €31 | S | €76m+ for a police IT system that never truly worked — then lawyers. |
| 12 | Company-car tax expenditure package (10y class) | structural_fiscal | federal | €35.00 bn | 8.5 | 7.0 | 8.57 | 1,804,124 | 1,186,441 | 14801 min (~10.3 d) | €7,216 | S | A fringe benefit that rewrote Belgian mobility, congestion and the wage bill — f |
| 13 | Dexia dismantling + Belfius nationalisation path | financial_crisis | federal | €7.00 bn | 8.5 | 7.0 | 8.57 | 360,825 | 237,288 | 2960 min (~2.1 d) | €1,443 | M | Municipal lender + French expansion = Belgian taxpayers holding the bag. |
| 14 | Brussels North Quarter / WTC towers — unfinished urban  | urban_dev | Brussels | €1.50 bn | 8.5 | 7.0 | 8.57 | 77,320 | 50,848 | 634 min (~10.6 h) | €309 | W | Bulldoze a neighbourhood for eight towers — deliver three and a windswept esplan |
| 15 | Party / political-group / media-adjacent public transfe | politics | multi | €1.50 bn | 8.5 | 7.0 | 8.57 | 77,320 | 50,848 | 634 min (~10.6 h) | €309 | W | Democracy needs parties; blank-cheque opacity does not. |
| 16 | International aviation kerosene excise exemption (10y) | structural_fiscal | federal | €7.00 bn | 8.0 | 7.5 | 8.55 | 360,825 | 237,288 | 2960 min (~2.1 d) | €1,443 | S | Fly tax-free fuel while trains pay full freight — 1940s law meets 2020s climate. |
| 17 | Fyra / V250 high-speed train fiasco (BE share of write- | rail_rolling_stock | federal | €250.0 m | 9.5 | 9.0 | 8.47 | 12,887 | 8,475 | 106 min (~1.8 h) | €52 | W | High-speed trains that could not handle winter — write-offs at TGV prices. |
| 18 | Heating gasoil excise preference (multi-year FFS) | structural_fiscal | federal | €18.00 bn | 8.0 | 7.0 | 8.43 | 927,835 | 610,170 | 7612 min (~5.3 d) | €3,711 | S | Cheap heating oil by design while climate policy points the other way. |
| 19 | Flanders green electricity certificates (GSC) support p | energy_policy | Flanders | €12.00 bn | 8.0 | 7.0 | 8.43 | 618,557 | 406,780 | 5075 min (~3.5 d) | €2,474 | M | Early PV boom locked in rich certificates; households paid via bills for decades |
| 20 | Brussels RER/GEN suburban rail — decades of delay & par | transport_capex | federal+Brussels+regions | €5.00 bn | 8.0 | 7.0 | 8.43 | 257,732 | 169,492 | 2114 min (~1.5 d) | €1,031 | W | The suburban rail everyone promised for a generation — still waiting at many pla |
| 21 | Social housing vacancy & renovation backlog costs | housing | multi | €3.00 bn | 8.0 | 7.0 | 8.43 | 154,639 | 101,695 | 1269 min (~21.1 h) | €619 | W | People on lists, empty flats in the stock — allocation failure as fiscal waste. |
| 22 | Ministerial cabinets culture — oversized political staf | institutions | multi | €3.00 bn | 8.0 | 7.0 | 8.43 | 154,639 | 101,695 | 1269 min (~21.1 h) | €619 | W | A shadow civil service that leaves when the minister does — institutional amnesi |
| 23 | Temporary unemployment / crisis unemployment fraud & ov | labour_market | federal | €2.00 bn | 8.0 | 7.0 | 8.43 | 103,093 | 67,797 | 846 min (~14.1 h) | €412 | W | Furlough that became a lifestyle for some — detection lagged cash. |
| 24 | Sabena bankruptcy — public shareholding losses + social | transport_soe | federal | €1.50 bn | 8.0 | 7.0 | 8.43 | 77,320 | 50,848 | 634 min (~10.6 h) | €309 | W | National flag carrier to Europe’s biggest corporate failure — 7,500 jobs later. |
| 25 | Excess profit tax rulings (EU state-aid recovery saga) | corporate_tax | federal | €1.00 bn | 8.0 | 7.0 | 8.43 | 51,546 | 33,898 | 423 min (~7.0 h) | €206 | W | Bespoke tax math for multinationals — until Brussels said no. |
| 26 | Brussels metro ghost stations / unused levels (Sainctel | ghost_infra | Brussels | €200.0 m | 9.0 | 9.0 | 8.32 | 10,309 | 6,780 | 85 min (~1.4 h) | €41 | W | Stations built for lines that never came — Belgium’s most photogenic fiscal ghos |
| 27 | Intercommunale dividend politics (energy/water) — soft  | local_capture | local | €5.00 bn | 8.0 | 6.5 | 8.30 | 257,732 | 169,492 | 2114 min (~1.5 d) | €1,031 | W | Your water bill elects a board you never heard of. |
| 28 | Empty / underused public building stock (multi-year opp | assets | multi | €5.00 bn | 7.5 | 7.0 | 8.28 | 257,732 | 169,492 | 2114 min (~1.5 d) | €1,031 | W | Public walls with no people — capital depreciation as quiet waste. |
| 29 | Training vouchers / activation with weak job placement  | labour_market | multi | €5.00 bn | 7.5 | 7.0 | 8.28 | 257,732 | 169,492 | 2114 min (~1.5 d) | €1,031 | W | Certificates of attendance sold as labour-market miracles. |
| 30 | Antwerp premetro unused tunnels & stations (50y ghost c | ghost_infra | Flanders | €600.0 m | 9.0 | 8.5 | 8.20 | 30,928 | 20,339 | 254 min (~4.2 h) | €124 | W | Underground trams that waited half a century for passengers — and more money to  |
| 31 | Awareness campaigns with no behaviour-change evidence ( | vanity_project | multi | €600.0 m | 9.0 | 8.5 | 8.20 | 30,928 | 20,339 | 254 min (~4.2 h) | €124 | W | Poster politics: if you can’t measure it, bill it to communications. |
| 32 | Justice IT mega-projects cluster (Phoenix/Cheops and su | it_failure | federal | €400.0 m | 9.0 | 8.5 | 8.20 | 20,619 | 13,559 | 169 min (~2.8 h) | €82 | W | Courts still drowning in paper after successive ‘once-and-for-all’ IT reboots. |
| 33 | Publifin / Nethys / Enodia intercommunale capture scand | local_capture | Wallonia | €200.0 m | 9.0 | 8.5 | 8.20 | 10,309 | 6,780 | 85 min (~1.4 h) | €41 | W | Intercommunales as political ATM — energy dividends and director seats. |
| 34 | Early labour-market exit & special pension schemes (mul | structural_fiscal | federal | €60.00 bn | 8.0 | 6.0 | 8.18 | 3,092,784 | 2,033,898 | 25374 min (~17.6 d) | €12,371 | W | Retire early, bill the next cohort — special schemes as political glue. |
| 35 | Institutional dualism overhead (multi-parliaments, dual | institutions | multi | €40.00 bn | 8.0 | 6.0 | 8.18 | 2,061,856 | 1,355,932 | 16916 min (~11.7 d) | €8,247 | W | Two of everything that speaks a language — democracy has a price tag that is nev |
| 36 | Banking crisis public capital injections (Fortis/Dexia/ | financial_crisis | federal+regions | €22.00 bn | 8.0 | 6.0 | 8.18 | 1,134,021 | 745,763 | 9304 min (~6.5 d) | €4,536 | M | Too-big-to-fail became a taxpayer balance-sheet event — twice for Dexia. |
| 37 | Federal facultative discretionary subsidies opacity (mu | structural_fiscal | federal | €9.00 bn | 8.0 | 6.0 | 8.18 | 463,918 | 305,085 | 3806 min (~2.6 d) | €1,856 | S | Ministers’ discretionary chequebook — public money without a public shopping lis |
| 38 | Nuclear phase-out / extension stop-start policy costs | energy_policy | federal | €8.00 bn | 8.0 | 6.0 | 8.18 | 412,371 | 271,186 | 3383 min (~2.3 d) | €1,649 | W | Vote to close reactors, then pay to keep them — energy policy as ping-pong. |
| 39 | 1999 dioxin crisis — farm slaughter, export ban, politi | food_safety | federal | €1.50 bn | 8.0 | 6.0 | 8.18 | 77,320 | 50,848 | 634 min (~10.6 h) | €309 | W | Contaminated feed, empty shelves, a government that fell — food safety as system |
| 40 | NEO / Heizel redevelopment delays & redesigns | urban_dev | Brussels | €1.50 bn | 7.5 | 6.5 | 8.15 | 77,320 | 50,848 | 634 min (~10.6 h) | €309 | W | Expo site dreams that keep reinventing the masterplan. |
| 41 | Cheque economy pure waste (admin + restriction DWL) — N | structural_fiscal | federal | €2.50 bn | 8.5 | 5.0 | 8.07 | 128,866 | 84,746 | 1057 min (~17.6 h) | €515 | M | Most of the billions are wages in scrip form — retarded is forced spend + admin, |
| 42 | Agusta / Dassault helicopter & aircraft kickback scanda | defence | federal | €200.0 m | 9.0 | 8.0 | 8.07 | 10,309 | 6,780 | 85 min (~1.4 h) | €41 | W | Helicopters with a side order of party financing — NATO ally meets Italian envel |
| 43 | Notional interest deduction (NID) multi-year deadweight | corporate_tax | federal | €30.00 bn | 7.5 | 6.0 | 8.03 | 1,546,392 | 1,016,949 | 12687 min (~8.8 d) | €6,186 | W | Paper equity interest deduction that became a European tax-planning magnet. |
| 44 | Triple PES architecture (VDAB/FOREM/Actiris + federal l | institutions | multi | €10.00 bn | 7.5 | 6.0 | 8.03 | 515,464 | 338,983 | 4229 min (~2.9 d) | €2,062 | W | Three public employment services and still the activation maze. |
| 45 | Thuin Athénée boarding school complex offset by 1.5 m | buildings | FWB | €15.0 m | 10.0 | 10.0 | 7.97 | 773 | 508 | 6.3 min | €3 | W | Offset the building by a metre and a half — then ran out of money to connect any |
| 46 | Professional order / permit denseness entry barriers (d | institutions | multi | €20.00 bn | 7.0 | 6.0 | 7.88 | 1,030,928 | 677,966 | 8458 min (~5.9 d) | €4,124 | W | Need a stamp to compete — insiders smile, prices rise. |
| 47 | Plan Oxygène Walloon municipal debt oxygen (borrowing f | local_finance | Wallonia | €1.50 bn | 7.0 | 6.0 | 7.88 | 77,320 | 50,848 | 634 min (~10.6 h) | €309 | M | Oxygen for commune cashflow — risk of permanent life support. |
| 48 | Liège tramway — cost overrun + availability payments | transport_capex | Wallonia | €1.20 bn | 7.0 | 6.0 | 7.88 | 61,856 | 40,678 | 507 min (~8.5 h) | €247 | M | A modern tram bought with PPP premiums after classic Belgian cost shock. |
| 49 | bpost press distribution concession (multi-year before  | media_postal | federal | €1.50 bn | 6.5 | 6.0 | 7.73 | 77,320 | 50,848 | 634 min (~10.6 h) | €309 | S | Paying a postal monopoly to deliver newspapers — until finally not. |
| 50 | Liège unused metro tunnel (La Batte / Saint-Léonard) | ghost_infra | Wallonia | €80.0 m | 9.5 | 9.5 | 7.70 | 4,124 | 2,712 | 33.8 min | €16 | W | A prototype metro car in a tunnel to nowhere — Walloon futurism paused forever. |
| 51 | Etterbeek hospital — built 1982, closed after months | buildings | Brussels | €80.0 m | 9.5 | 9.5 | 7.70 | 4,124 | 2,712 | 33.8 min | €16 | W | Opened the champagne, then the merger memo — hospital-shaped waste. |
| 52 | Hôpital Rayon de Soleil (Montigny) — empty decades + fr | buildings | Wallonia | €60.0 m | 9.5 | 9.5 | 7.70 | 3,093 | 2,034 | 25.4 min | €12 | W | A hospital shell and a crime file — public money and private capture. |
| 53 | Varsenare ghost motorway bridges (demolished 2012) | ghost_infra | Flanders | €15.0 m | 9.5 | 9.5 | 7.70 | 773 | 508 | 6.3 min | €3 | W | Bridges over a railway to a highway that never arrived — then dynamite. |
| 54 | Strépy dead-end four-lane road to a field | ghost_infra | Wallonia | €12.0 m | 9.5 | 9.5 | 7.70 | 619 | 407 | 5.1 min | €2 | W | Next to a world-famous boat lift: a highway to a cabbage field. |
| 55 | Brussels Palace of Justice — endless renovation / scaff | buildings | federal | €600.0 m | 8.5 | 7.0 | 7.67 | 30,928 | 20,339 | 254 min (~4.2 h) | €124 | W | Europe’s largest law courts, permanently under tarpaulin. |
| 56 | Kortrijk R8 ring incomplete for 50+ years | ghost_infra | Flanders | €150.0 m | 8.0 | 7.5 | 7.65 | 7,732 | 5,085 | 63 min (~1.1 h) | €31 | W | A ring road that never quite ringed — 50 years of temporary forever. |
| 57 | Federal fossil-fuel subsidy inventory (10y class) | structural_fiscal | federal | €100.00 bn | 7.0 | 5.0 | 7.62 | 5,154,639 | 3,389,830 | 42289 min (~29.4 d) | €20,619 | M | Cheap fossil by tax design, then climate targets by other instruments — policy s |
| 58 | EIWT partial remittance bedrijfsvoorheffing package (10 | structural_fiscal | federal | €40.00 bn | 7.0 | 5.0 | 7.62 | 2,061,856 | 1,355,932 | 16916 min (~11.7 d) | €8,247 | S | Night-shift and R&D wage tax discounts at multi-billion scale — additionality ra |
| 59 | Provincial government layer ongoing cost (relevance deb | institutions | multi | €20.00 bn | 7.0 | 5.0 | 7.62 | 1,030,928 | 677,966 | 8458 min (~5.9 d) | €4,124 | W | A middle layer of government looking for a job description since 1830. |
| 60 | COVID support packages — fraud + untargeted share | crisis_fiscal | multi | €15.00 bn | 7.0 | 5.0 | 7.62 | 773,196 | 508,475 | 6343 min (~4.4 d) | €3,093 | W | Emergency money that sometimes found the wrong pockets and the wrong firms. |
| 61 | Oosterweelverbinding (Antwerp ring completion) — cost e | transport_capex | Flanders | €12.00 bn | 7.0 | 5.0 | 7.62 | 618,557 | 406,780 | 5075 min (~3.5 d) | €2,474 | M | Necessary tunnel politics meets a bill that keeps climbing toward the grandchild |
| 62 | 2021–23 energy-crisis blanket support (poor targeting s | crisis_fiscal | federal+regions | €12.00 bn | 7.0 | 5.0 | 7.62 | 618,557 | 406,780 | 5075 min (~3.5 d) | €2,474 | W | Price shock real; writing cheques to everyone is the lazy instrument. |
| 63 | Samusocial Brussels mismanagement scandal | local_capture | Brussels | €20.0 m | 9.5 | 9.0 | 7.58 | 1,031 | 678 | 8.5 min | €4 | M | A homeless charity with luxury housing for the wrong people. |
| 64 | N60 Anvaing unused four-lane embankment | ghost_infra | Wallonia | €20.0 m | 9.0 | 9.5 | 7.55 | 1,031 | 678 | 8.5 min | €4 | W | Four lanes of asphalt ambition ending in a ploughed field. |
| 65 | NMBS multi-year ICT / punctuality programme overruns (c | it_failure | federal | €800.0 m | 8.0 | 7.0 | 7.53 | 41,237 | 27,119 | 338 min (~5.6 h) | €165 | W | Railway software that arrives after the timetable it was meant to fix. |
| 66 | Strépy-Thieu boat lift — mega engineering, thin traffic | waterways | Wallonia | €600.0 m | 8.0 | 7.0 | 7.53 | 30,928 | 20,339 | 254 min (~4.2 h) | €124 | M | A cathedral of hydraulic engineering for a canal that never filled with barges. |
| 67 | Service vouchers (dienstencheques) multi-year fiscal co | structural_fiscal | federal+regions | €25.00 bn | 6.5 | 5.0 | 7.48 | 1,288,660 | 847,458 | 10572 min (~7.3 d) | €5,155 | M | Formalise domestic work with a fiscal booster rocket — forever. |
| 68 | Godsheide cable-stayed bridge (local traffic only) | ghost_infra | Flanders | €50.0 m | 9.0 | 9.0 | 7.42 | 2,577 | 1,695 | 21.1 min | €10 | W | Belgium’s grandest cable-stayed bridge… for neighbourhood traffic. |
| 69 | N54 Charleroi–Maubeuge unfinished dual carriageway stub | ghost_infra | Wallonia | €40.0 m | 9.0 | 9.0 | 7.42 | 2,062 | 1,356 | 16.9 min | €8 | W | A border motorway that ends in the middle of nowhere — twice. |
| 70 | Heppignies oversized exchange to a roundabout in fields | ghost_infra | Wallonia | €20.0 m | 9.0 | 9.0 | 7.42 | 1,031 | 678 | 8.5 min | €4 | W | Motorway geometry designed for a fourth arm that is a field. |
| 71 | Arquennes bridge for Nivelles–Gouy ghost motorway | ghost_infra | Wallonia | €15.0 m | 9.0 | 9.0 | 7.42 | 773 | 508 | 6.3 min | €3 | W | A bridge ready for cars that never got a road. |
| 72 | Wage-subsidy / labour-tax wedge compensation stack (mul | structural_fiscal | federal | €100.00 bn | 7.0 | 4.0 | 7.38 | 5,154,639 | 3,389,830 | 42289 min (~29.4 d) | €20,619 | M | Perpetual fiscal duct-tape for Europe’s highest labour tax wedge — the euro is r |
| 73 | Ronquières inclined plane — oversized for realised traf | waterways | Wallonia | €250.0 m | 7.5 | 7.0 | 7.38 | 12,887 | 8,475 | 106 min (~1.8 h) | €52 | W | Sixteen locks replaced by a machine waiting for missing barges. |
| 74 | Primary balance gap vs debt-stabilising path (multi-yea | structural_fiscal | federal+GG | €100.00 bn | 6.0 | 5.0 | 7.33 | 5,154,639 | 3,389,830 | 42289 min (~29.4 d) | €20,619 | M | Interest and snowball: the silent multi-billion that funds past choices. |
| 75 | Low-value care / billing waste in health insurance (sub | health | federal | €25.00 bn | 6.0 | 5.0 | 7.33 | 1,288,660 | 847,458 | 10572 min (~7.3 d) | €5,155 | W | Universal care is a feature; paying for useless procedures is a bug. |
| 76 | Federal offshore wind production support (lifetime clas | energy_policy | federal | €12.70 bn | 6.0 | 5.0 | 7.33 | 654,639 | 430,508 | 5371 min (~3.7 d) | €2,619 | M | Climate steelman is real; overprofit and contract design are the waste debate. |
| 77 | VAT reduced rate horeca (multi-year taxex) | structural_fiscal | federal | €12.00 bn | 6.0 | 5.0 | 7.33 | 618,557 | 406,780 | 5075 min (~3.5 d) | €2,474 | S | Cheaper steak frites by statute — sector lobby with a VAT code. |
| 78 | Dual public broadcasters VRT + RTBF (10y ordinary dots  | institutions | multi | €6.50 bn | 6.0 | 5.0 | 7.33 | 335,052 | 220,339 | 2749 min (~1.9 d) | €1,340 | S | Two full public broadcasters for 11 million people — linguistic federalism on sc |
| 79 | Flanders CIE carbon-leakage compensation (multi-year) | energy_policy | Flanders | €2.50 bn | 6.0 | 5.0 | 7.33 | 128,866 | 84,746 | 1057 min (~17.6 h) | €515 | S | Pay heavy industry for EU-ETS power costs — additionality on a promise. |
| 80 | Vlaamse Veerkracht / RRF project ROI mixed bag (subset  | stimulus | Flanders | €2.00 bn | 6.0 | 5.0 | 7.33 | 103,093 | 67,797 | 846 min (~14.1 h) | €412 | W | EU recovery money spent fast — additionality and CBA uneven. |
| 81 | Neerpede / A9 ghost interchange earthworks | ghost_infra | Brussels/Flanders | €40.0 m | 9.0 | 8.5 | 7.30 | 2,062 | 1,356 | 16.9 min | €8 | W | Ski on the ruins of a motorway that politics killed — after earthworks. |
| 82 | Ypres–Comines canal incomplete (1864–1912) | ghost_infra | Flanders | €20.0 m | 8.5 | 9.0 | 7.28 | 1,031 | 678 | 8.5 min | €4 | W | Half a century of digging that never connected the water. |
| 83 | Charleroi airport public support / Ryanair state-aid sa | airports | Wallonia | €300.0 m | 7.5 | 6.5 | 7.25 | 15,464 | 10,170 | 127 min (~2.1 h) | €62 | W | Low-cost airport growth with a state-aid courtroom sequel. |
| 84 | Péronnes coal washery — short life, long empty, then re | industrial_shell | Wallonia | €40.0 m | 8.5 | 8.5 | 7.15 | 2,062 | 1,356 | 16.9 min | €8 | W | Wash coal for 15 years, then renovate the ruin for nothing. |
| 85 | Drogenbos partial ring exchange (half-demolished) | ghost_infra | Brussels | €30.0 m | 8.5 | 8.5 | 7.15 | 1,546 | 1,017 | 12.7 min | €6 | W | Ring pieces built, then torn down — urban planning as temporary sculpture. |
| 86 | Centre des Dolimarts — asylum plan fail, then decay sal | buildings | federal | €20.0 m | 8.5 | 8.5 | 7.15 | 1,031 | 678 | 8.5 min | €4 | W | Buy a holiday camp for asylum seekers, do nothing, sell a wreck. |
| 87 | Antwerp new courthouse (Gerechtsgebouw) cost overruns | buildings | federal | €400.0 m | 7.5 | 6.0 | 7.12 | 20,619 | 13,559 | 169 min (~2.8 h) | €82 | M | A postcard courthouse that cost like a small metro line. |
| 88 | Bernistap canal tunnel (Meuse–Moselle dream, 1828–1831) | ghost_infra | Wallonia | €10.0 m | 8.0 | 9.0 | 7.12 | 516 | 339 | 4.2 min | €2 | W | William I’s canal tunnel stopped by a revolution — and never restarted. |
| 89 | Maribel social funds wage subsidies (10y class) | structural_fiscal | federal | €15.00 bn | 6.0 | 4.0 | 7.08 | 773,196 | 508,475 | 6343 min (~4.4 d) | €3,093 | S | Non-market employment subsidies at billion scale — FTE outcomes under-published. |
| 90 | Credendo export-credit cover capacity (contingent publi | financial_risk | federal | €15.00 bn | 6.0 | 4.0 | 7.08 | 773,196 | 508,475 | 6343 min (~4.4 d) | €3,093 | M | Taxpayers as silent co-insurer of export risk — fine print in the billions. |
| 91 | Actiris PES budget growth vs placement outcomes debate | labour_market | Brussels | €5.00 bn | 6.0 | 4.0 | 7.08 | 257,732 | 169,492 | 2114 min (~1.5 d) | €1,031 | M | A PES that grew with unemployment — dual-market Brussels complexity real. |
| 92 | Smaakhaven food innovation campus subsidy (Radar clown  | vanity_project | Flanders | €38.0 m | 8.5 | 8.0 | 7.03 | 1,959 | 1,288 | 16.1 min | €8 | S | Food campus vibes with a fiscal bill you can taste in werkminuten. |
| 93 | NH90 / A400M defence programme delays & extra costs (BE | defence | federal | €800.0 m | 7.0 | 6.0 | 6.97 | 41,237 | 27,119 | 338 min (~5.6 h) | €165 | W | Aircraft that arrive late, rare, and expensive — European industrial policy in u |
| 94 | Hingeon bridge from cul-de-sac to a field over E42 | ghost_infra | Wallonia | €5.0 m | 9.5 | 10.0 | 6.92 | 258 | 170 | 2.1 min | €1 | W | A bridge from a dead-end street to a field — over a motorway. |
| 95 | Château de Mirwart — repeated failed public/private con | buildings | Wallonia | €20.0 m | 8.0 | 8.0 | 6.88 | 1,031 | 678 | 8.5 min | €4 | W | A castle that refused every business plan thrown at it. |
| 96 | Liège airport cargo growth public support stack | airports | Wallonia | €400.0 m | 7.0 | 5.5 | 6.85 | 20,619 | 13,559 | 169 min (~2.8 h) | €82 | W | Cargo boom paid partly off the public balance sheet — and local sleep. |
| 97 | Simonis / Pannenhuis stations closed then reopened deca | ghost_infra | federal | €40.0 m | 8.0 | 7.5 | 6.75 | 2,062 | 1,356 | 16.9 min | €8 | W | Stations so useless they closed — then useful enough to reopen. Time-value still |
| 98 | Berlaymont asbestos renovation (EU Commission HQ) — BE/ | buildings | multi/EU | €800.0 m | 7.0 | 5.0 | 6.72 | 41,237 | 27,119 | 338 min (~5.6 h) | €165 | M | The Commission’s HQ sat empty while asbestos and invoices piled up. |
| 99 | Machelen interchange unused ramps (later TGV partial us | ghost_infra | Flanders | €60.0 m | 8.0 | 7.0 | 6.62 | 3,093 | 2,034 | 25.4 min | €12 | W | A cloverleaf for a motorway into Brussels that never punched through. |
| 100 | Federal tax expenditures total quantified (5–10y class) | structural_fiscal | federal | €200.00 bn | 5.0 | 3.0 | 6.53 | 10,309,278 | 6,779,661 | 84579 min (~58.7 d) | €41,237 | S | Parliament’s deviation from the tax code is larger than many ministries — and st |
| 101 | NMBS PSO / federal support package (10y class, efficien | transport_opex | federal | €20.00 bn | 5.0 | 3.0 | 6.53 | 1,030,928 | 677,966 | 8458 min (~5.9 d) | €4,124 | M | Public rail needs public money — the waste is how much disappears into delay and |
| 102 | F-35 replacement path — lifecycle cost lock-in debate | defence | federal | €6.00 bn | 5.0 | 3.0 | 6.53 | 309,278 | 203,390 | 2537 min (~1.8 d) | €1,237 | M | Deterrence steelman vs sticker shock — on the list as fiscal lock-in, not automa |
| 103 | De Lijn multi-year dotatie efficiency gap (subset claim | transport_opex | Flanders | €5.00 bn | 5.0 | 3.0 | 6.53 | 257,732 | 169,492 | 2114 min (~1.5 d) | €1,031 | W | Buses are not waste; running them badly can be. |
| 104 | STIB multi-year financing efficiency + Metro3 spillover | transport_opex | Brussels | €5.00 bn | 5.0 | 3.0 | 6.53 | 257,732 | 169,492 | 2114 min (~1.5 d) | €1,031 | W | Dense city transit is valuable; blank cheques are not a strategy. |
| 105 | Perwez bypass bridge unused; project buried 2019 | ghost_infra | Wallonia | €8.0 m | 9.0 | 9.0 | 6.52 | 412 | 271 | 3.4 min | €2 | M | Build the bridge first, cancel the road later — modern GTI. |
| 106 | Diabolo rail link to Brussels Airport — surcharge model | transport_capex | federal | €800.0 m | 6.0 | 4.0 | 6.17 | 41,237 | 27,119 | 338 min (~5.6 h) | €165 | M | Useful airport rail paid forever via ticket surcharge — steelman works, opacity  |
| 107 | Het Wassalon gelijke-kansen vodcast (tiny cash, max abs | vanity_project | Flanders | €800 k | 9.5 | 9.0 | 5.78 | 41 | 27 | 0.34 min | €0 | S | A podcast so equal-opportunity it made the waste leaderboard on pure vibes-per-e |

---

## Gallery: pure boondoggles (high purity, not always top cash)

| Name | Mid € | Abs | Pur | Werkminuten | Why iconic |
|------|------:|----:|----:|------------:|------------|
| Smeerpijp (Limburg–Antwerp industrial sewer never used) | €100.0 m | 10.0 | 10.0 | 42.3 min | A 107 km pollution pipe that never carried a drop — purity score: perfect 10. |
| Thuin Athénée boarding school complex offset by 1.5 m | €15.0 m | 10.0 | 10.0 | 6.3 min | Offset the building by a metre and a half — then ran out of money to connect anything. |
| Hingeon bridge from cul-de-sac to a field over E42 | €5.0 m | 9.5 | 10.0 | 2.1 min | A bridge from a dead-end street to a field — over a motorway. |
| i-Police federal police digitalisation failure | €150.0 m | 9.5 | 9.5 | 63 min (~1.1 h) | €76m+ for a police IT system that never truly worked — then lawyers. |
| Liège unused metro tunnel (La Batte / Saint-Léonard) | €80.0 m | 9.5 | 9.5 | 33.8 min | A prototype metro car in a tunnel to nowhere — Walloon futurism paused forever. |
| Etterbeek hospital — built 1982, closed after months | €80.0 m | 9.5 | 9.5 | 33.8 min | Opened the champagne, then the merger memo — hospital-shaped waste. |
| Hôpital Rayon de Soleil (Montigny) — empty decades + fraud a | €60.0 m | 9.5 | 9.5 | 25.4 min | A hospital shell and a crime file — public money and private capture. |
| Varsenare ghost motorway bridges (demolished 2012) | €15.0 m | 9.5 | 9.5 | 6.3 min | Bridges over a railway to a highway that never arrived — then dynamite. |
| Strépy dead-end four-lane road to a field | €12.0 m | 9.5 | 9.5 | 5.1 min | Next to a world-famous boat lift: a highway to a cabbage field. |
| N60 Anvaing unused four-lane embankment | €20.0 m | 9.0 | 9.5 | 8.5 min | Four lanes of asphalt ambition ending in a ploughed field. |
| Charleroi light metro — half-built network, ghost branches | €1.50 bn | 9.5 | 9.0 | 634 min (~10.6 h) | Eight arms planned, ghost tunnels for decades — waffle-iron metro politics in concrete. |
| Fyra / V250 high-speed train fiasco (BE share of write-downs | €250.0 m | 9.5 | 9.0 | 106 min (~1.8 h) | High-speed trains that could not handle winter — write-offs at TGV prices. |
| Samusocial Brussels mismanagement scandal | €20.0 m | 9.5 | 9.0 | 8.5 min | A homeless charity with luxury housing for the wrong people. |
| Het Wassalon gelijke-kansen vodcast (tiny cash, max absurdit | €800 k | 9.5 | 9.0 | 0.34 min | A podcast so equal-opportunity it made the waste leaderboard on pure vibes-per-euro. |
| Brussels metro ghost stations / unused levels (Sainctelette, | €200.0 m | 9.0 | 9.0 | 85 min (~1.4 h) | Stations built for lines that never came — Belgium’s most photogenic fiscal ghosts. |
| Godsheide cable-stayed bridge (local traffic only) | €50.0 m | 9.0 | 9.0 | 21.1 min | Belgium’s grandest cable-stayed bridge… for neighbourhood traffic. |
| N54 Charleroi–Maubeuge unfinished dual carriageway stubs | €40.0 m | 9.0 | 9.0 | 16.9 min | A border motorway that ends in the middle of nowhere — twice. |
| Heppignies oversized exchange to a roundabout in fields | €20.0 m | 9.0 | 9.0 | 8.5 min | Motorway geometry designed for a fourth arm that is a field. |
| Arquennes bridge for Nivelles–Gouy ghost motorway | €15.0 m | 9.0 | 9.0 | 6.3 min | A bridge ready for cars that never got a road. |
| Perwez bypass bridge unused; project buried 2019 | €8.0 m | 9.0 | 9.0 | 3.4 min | Build the bridge first, cancel the road later — modern GTI. |

---

## Categories covered

| Category | n |
|----------|--:|
| `ghost_infra` | 21 |
| `structural_fiscal` | 15 |
| `buildings` | 8 |
| `institutions` | 7 |
| `energy_policy` | 6 |
| `transport_capex` | 5 |
| `labour_market` | 4 |
| `it_failure` | 4 |
| `local_capture` | 3 |
| `vanity_project` | 3 |
| `defence` | 3 |
| `transport_opex` | 3 |
| `housing` | 2 |
| `financial_crisis` | 2 |
| `urban_dev` | 2 |
| `corporate_tax` | 2 |
| `crisis_fiscal` | 2 |
| `waterways` | 2 |
| `airports` | 2 |
| `politics` | 1 |
| `rail_rolling_stock` | 1 |
| `transport_soe` | 1 |
| `assets` | 1 |
| `food_safety` | 1 |
| `local_finance` | 1 |
| `media_postal` | 1 |
| `health` | 1 |
| `stimulus` | 1 |
| `industrial_shell` | 1 |
| `financial_risk` | 1 |

---

## Media one-liners (pain unit)

- **Charleroi light metro — half-built network, ghost ** (€1.50 bn mid): ~**77,320 Belasting-FTE** · ~**50,848 nettoloon-jaren** · **634 min (~10.6 h)** per employee if split.
- **Brussels Metro line 3 — +hundreds-% budget path / ** (€4.76 bn mid): ~**245,361 Belasting-FTE** · ~**161,356 nettoloon-jaren** · **2013 min (~1.4 d)** per employee if split.
- **Smeerpijp (Limburg–Antwerp industrial sewer never ** (€100.0 m mid): ~**5,155 Belasting-FTE** · ~**3,390 nettoloon-jaren** · **42.3 min** per employee if split.
- **i-Police federal police digitalisation failure** (€150.0 m mid): ~**7,732 Belasting-FTE** · ~**5,085 nettoloon-jaren** · **63 min (~1.1 h)** per employee if split.
- **Company-car tax expenditure package (10y class)** (€35.00 bn mid): ~**1,804,124 Belasting-FTE** · ~**1,186,441 nettoloon-jaren** · **14801 min (~10.3 d)** per employee if split.
- **Banking crisis public capital injections (Fortis/D** (€22.00 bn mid): ~**1,134,021 Belasting-FTE** · ~**745,763 nettoloon-jaren** · **9304 min (~6.5 d)** per employee if split.
- **Cheque economy pure waste (admin + restriction DWL** (€2.50 bn mid): ~**128,866 Belasting-FTE** · ~**84,746 nettoloon-jaren** · **1057 min (~17.6 h)** per employee if split.
- **Thuin Athénée boarding school complex offset by 1.** (€15.0 m mid): ~**773 Belasting-FTE** · ~**508 nettoloon-jaren** · **6.3 min** per employee if split.
- **Oosterweelverbinding (Antwerp ring completion) — c** (€12.00 bn mid): ~**618,557 Belasting-FTE** · ~**406,780 nettoloon-jaren** · **5075 min (~3.5 d)** per employee if split.
- **Smaakhaven food innovation campus subsidy (Radar c** (€38.0 m mid): ~**1,959 Belasting-FTE** · ~**1,288 nettoloon-jaren** · **16.1 min** per employee if split.

---

## Method & sources

1. **GTI corpus** — Jean-Claude Defossé *Grands Travaux Inutiles* / RTBF JTI; [fr.wiki list](https://fr.wikipedia.org/wiki/Liste_de_grands_travaux_inutiles_en_Belgique); Hidden Monuments boondoggle map.
2. **Fiscal inventories** — FPS tax expenditures, FFS fossil inventory, NBB enterprise subsidies (linked to DOGE leaderboard rows).
3. **Crisis / bailouts** — 2008–12 Fortis/Dexia/KBC public capital paths; Sabena; COVID support audits.
4. **Modern mega-projects** — Oosterweel Rekenhof/press 2026; Metro 3 Cour des comptes; Liège tram; i-Police 2026.
5. **Institutions** — dual PSB, multi-PES, provinces, cabinets, waffle-iron meta-pattern.

Primary sources preferred when € is **strong**; press + secondary when **medium/weak**. Upgrade path: attach Court of Audit report IDs + FOI for unconsolidated historical GTI bills.

---

## Corrections log

| Date | Item | Change |
|------|------|--------|
| 2026-07-27 | — | v1 seed published |

Wrong entries get **struck with date + reason**, same discipline as DOGE.

---

## Links

- Current spend: [`06-doge-belgium.md`](../06-doge-belgium.md) · [`data/doge_waste_top10_current.md`](data/doge_waste_top10_current.md)
- New proposals: [`09-proposal-radar.md`](../09-proposal-radar.md) · pain unit [`../proposal-radar/TAXPAYER_UNIT.md`](../proposal-radar/TAXPAYER_UNIT.md)
- Rebuild script: [`scripts/build_historical_waste_hall.py`](scripts/build_historical_waste_hall.py)

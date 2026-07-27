# Taxpayer pain unit (Belgium)

Standard converter for **every** Proposal Radar fiscal figure.  
Goal: turn abstract euros into something an average worker *feels*.

## Why two columns (not one)

If you only do “years of tax for one person” and “people needed for one year of tax”, the numbers are **identical** (both = cost ÷ annual tax). That wastes a column.

We use **two different denominators**:

| Column (CSV) | Formula | Public NL label | What it hurts |
|--------------|---------|-----------------|---------------|
| `pain_tax_fte` | public € / **employee labour tax per year** | **Belasting-FTE** | “How many average workers’ *entire yearly work-tax bill* fund this?” — pure fiscal incidence of *labour* taxes |
| `pain_net_years` | public € / **net take-home per year** | **Nettoloon-jaren** | “How many years of *take-home pay* equal this?” — consumption sacrifice people understand in their bank account |

Optional display (derived, not stored):  
`pain_tax_workdays ≈ pain_tax_fte × 220` → “workdays of tax dedicated to this”.

### Sign convention

| Fiscal nature | Sign of pain columns |
|---------------|----------------------|
| Public **cost** / subsidy / TE reopened | **positive** (burden) |
| Public **saving** / TE killed / tax raised (revenue) | **negative** (relief / other taxpayers fund less of something else) — show as “−N FTE of labour tax freed” |
| Unknown / unquantified | blank |

Packages: use mid of min–max; always show range in memo if wide.

---

## Reference unit (locked until rebased)

| Parameter | Value | Notes |
|-----------|------:|-------|
| Profile | Average **single** full-time employee, no children | OECD *Taxing Wages* AW |
| Gross wage (Statbel) | **€48,912 / year** | €4,076/month × 12; Statbel full-time average (2022 vintage, still the headline Statbel figure in 2024–26 citations) |
| Employee net average tax rate (BE) | **39.7% of gross** | OECD *Taxing Wages 2025* country note — 2024; personal income tax + employee SSC (cash benefits netted for this household type) |
| **Employee labour tax / year** | **€19,418** | 0.397 × 48,912 — **this is “taxes he pays for working”** (not VAT, not property, not employer SSC) |
| Net take-home / year | **€29,494** | 60.3% of gross (OECD: take-home 60.3% of gross for this type in 2024) |
| Rounded constants used in CSV | tax **€19,400** · net **€29,500** | Avoid fake precision; memos may show unrounded |
| Full tax wedge (context only) | **~52.5–52.6%** of *labour costs* | OECD 2024/2025 — includes employer SSC; **not** used in pain columns (user asked what the worker pays) |

### Sources (re-check on rebase)

- Statbel: average gross monthly salary full-time employees €4,076 (2022 results).  
- OECD Taxing Wages 2025 — Belgium country note: tax wedge ~52.6% (2024); employee net average tax rate 39.7%; take-home 60.3% of gross.  
- OECD Taxing Wages 2026 brochure: Belgium still highest wedge class (~52.5% in 2025 vintage).

### Rebase rule

When Statbel or OECD releases a new AW series, update this file + `data/taxpayer_unit.csv`, recompute all `pain_*` columns in one script pass, bump `unit_version`.

---

## Interpretation examples

| Public € | Belasting-FTE | Nettoloon-jaren |
|---------:|--------------:|----------------:|
| €350,000 (CX grant) | ~18 | ~12 |
| €38,000,000 (Smaakhaven) | ~1,960 | ~1,290 |
| €49,700,000 (Syntra year) | ~2,560 | ~1,680 |
| €255,000,000 (FWB package) | ~13,140 | ~8,640 |
| €1,000,000,000 saving (company-car class) | **−51,550** | **−33,900** |

One-liners for media:

- *“Smaakhaven kost de **volledige jaarbelasting op arbeid** van ongeveer **2.000** doorsnee werknemers.”*  
- *“Of: **1.300 jaar nettoloon** van één gemiddelde voltijdse.”*

---

## Mandatory in every analysis memo

1. State which € figure enters the converter (min / mid / max + basis).  
2. Show both pain metrics.  
3. If fiscal unknown: say so; do **not** invent.  
4. Never present pain metrics as more precise than the underlying € confidence.

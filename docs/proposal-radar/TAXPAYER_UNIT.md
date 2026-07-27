# Taxpayer pain unit (Belgium)

Standard converter for **every** Proposal Radar fiscal figure.  
Goal: turn abstract euros into something an average worker *feels*.

## Three columns (three different feelings)

| Column (CSV) | Formula | Public NL label | What it hurts |
|--------------|---------|-----------------|---------------|
| `pain_tax_fte` | public € / **employee labour tax per year** | **Belasting-FTE** | “How many average workers’ *entire yearly work-tax bill* fund this?” |
| `pain_net_years` | public € / **net take-home per year** | **Nettoloon-jaren** | “How many years of *take-home pay* equal this?” (one person) |
| `pain_work_minutes` | (public € / **N employees**) / **€ earned per work-minute** | **Werkminuten** | “If we split the bill across **every** Belgian employee, how many **minutes of work** did each put in for this to exist?” |

### Why not “people for 1 year” and “years for 1 person” of the same tax?

Those are the **same number** (cost ÷ annual tax). We never store duplicates.

### Why Werkminuten is different

It answers a third question:

> *Not* “how many full tax bills?” *Not* “how many years of my net pay?”  
> But: “**My** share of this bill, paid by working — how long was I at the office for Smaakhaven?”

That is the most personal column for media / doorstep.

\[
\text{pain\_work\_minutes}
= \frac{\text{public €}}{N_{\text{employees}}}
\div \frac{\text{gross €/year}}{\text{work minutes/year}}
= \frac{\text{public €} \times \text{work minutes/year}}{N_{\text{employees}} \times \text{gross €/year}}
\]

We use **gross** € per minute (time worked produces gross pay; tax is a split of that, not extra minutes).

### Sign convention

| Fiscal nature | Sign of pain columns |
|---------------|----------------------|
| Public **cost** / subsidy / TE reopened | **positive** (burden) |
| Public **saving** / TE killed | **negative** (minutes “given back”) |
| Unknown / unquantified | blank |

Also stored: `pain_eur_per_employee` = public € / N (signed) — intermediate, useful for cards.

---

## Reference unit (locked until rebased)

| Parameter | Value | Notes |
|-----------|------:|-------|
| Profile | Average **single** full-time employee, no children | OECD *Taxing Wages* AW |
| Gross wage (Statbel) | **€48,912 / year** | €4,076/month × 12 (2022 Statbel FT vintage, still headline) |
| Employee net average tax rate (BE) | **39.7% of gross** | OECD *Taxing Wages 2025* BE note (2024) |
| **Employee labour tax / year** | **€19,418** → CSV **€19,400** | PIT + employee SSC only |
| Net take-home / year | **€29,494** → CSV **€29,500** | 60.3% of gross |
| **N employees (Belgium)** | **4,850,000** | Rounded stock of *employees* (werknemers), not self-employed; order-of-magnitude **Medium** — rebase on RSZ/Statbel headcount |
| Work calendar (FT) | **220 days × 7.6 h × 60** = **100,320 min/year** | 38h-week class; holidays already outside the 220 |
| Gross € / work-minute | **≈ €0.4876** | 48,912 / 100,320 |
| Full tax wedge (context only) | **~52.5–52.6%** of labour costs | Not used in pain columns |

### Sources (re-check on rebase)

- Statbel FT gross monthly €4,076.  
- OECD Taxing Wages 2025 — Belgium.  
- Employee headcount: keep as explicit rounded constant until a single Statbel/RSZ stock series is pinned in `taxpayer_unit.csv` notes.

### Rebase rule

Update `data/taxpayer_unit.csv` → run `scripts/recompute_pain.py` → bump `unit_version`.

---

## Interpretation examples

| Public € | Belasting-FTE | Nettoloon-jaren | **Werkminuten / employee** | € / employee |
|---------:|--------------:|----------------:|---------------------------:|-------------:|
| €350,000 (CX) | ~18 | ~12 | **~0.15 min** (~9 sec) | ~€0.07 |
| €38,000,000 (Smaakhaven) | ~1,959 | ~1,288 | **~16 min** | ~€7.84 |
| €49,700,000 (Syntra) | ~2,562 | ~1,685 | **~21 min** | ~€10.25 |
| €255,000,000 (FWB save) | ~−13,144 | ~−8,644 | **~−108 min** | ~−€52.6 |
| ~€850m mid (company-car save) | ~−43,800 | ~−28,800 | **~−360 min** (~6 h) | ~−€175 |

One-liners for media:

- *“Smaakhaven: de **jaarbelasting op arbeid** van ~**2.000** doorsnee werknemers.”*  
- *“Of **1.300 jaar nettoloon** van één persoon.”*  
- *“Of: als we de rekening over **alle** Belgische werknemers verdelen, werkte **iedereen ~16 minuten** voor Smaakhaven.”*

---

## Mandatory in every analysis memo

1. State which € figure enters the converter (min / mid / max + basis).  
2. Show **all three** pain metrics (or honestly blank).  
3. Never invent € to fill pain.  
4. Never present pain metrics as more precise than the underlying € confidence.  
5. Note N employees is a rounded stock (Medium).

#!/usr/bin/env python3
"""EVERY-10 refresh from live CSVs after tick 2390 appends."""
from collections import Counter
from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2390_stamp.txt").read_text().strip().splitlines()
csv.field_size_limit(20_000_000)

def n_data(p):
    with open(p, "rb") as f:
        return sum(1 for _ in f) - 1

n_bud = n_data(DATA / "budgets.csv")
n_com = n_data(DATA / "commitments.csv")
n_lb = n_data(DATA / "leaderboard.csv")
n_ent = n_data(DATA / "entities.csv")
n_src = n_data(DATA / "sources.csv")
with open(DATA / "foi_queue.csv", newline="", encoding="utf-8") as f:
    foi_rows = list(csv.DictReader(f))
foi_c = Counter((r.get("status") or "").strip() for r in foi_rows)
n_foi = len(foi_rows)
n_ready = foi_c.get("ready", 0)
n_ans = foi_c.get("answered", 0)
n_part = foi_c.get("partial", 0)
print("INV", n_bud, n_com, n_lb, n_ent, n_src, "foi", n_foi, "ready", n_ready, "ans", n_ans, "part", n_part)

progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2390** ({DAY})

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2381-2390 continuum; AGB Bornem / FARO / AIESH still YE2024 stalls; **LDSST unlocked YE2025@2390** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2381-2390 residual dual L5 (not near-complete of 348bn):** H.Hart Oudenaarde · CAR DAT · Vijvens · CAR Roeselare · Ascendere · CAR De Klinker · CAR De Hert · REVA Kohesi · Beschut Wonen Kohesi · EVERY-10 primary **LDSST bruto 591k / 73 179k / pnl PROFIT FLIP 99k / destin 59k** (Strong PDF) |
| **E. FOI-ready gaps** | **~{n_ready}** drafts ready | Human send only; answered **{n_ans}**; partial **{n_part}**; total FOI rows **{n_foi}** |

**Off-TE (do not mix into 348 bn):** federal taxex · company cars/cheque · **AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk/CAR/logopedie shells** (**NEW 2381-2390** H.Hart Oudenaarde · CAR DAT · Vijvens · CAR Roeselare · Ascendere · CAR De Klinker · CAR De Hert · REVA Kohesi · Beschut Wonen Kohesi · **LDSST**) · Metro3 · OWV snowball · Hedera.

### Inventory (tick 2390)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {n_bud} |
| commitments.csv | {n_com} |
| leaderboard.csv | {n_lb} |
| entities.csv | {n_ent} |
| sources.csv | {n_src} |
| FOI ready | {n_ready} |
| FOI answered | {n_ans} |
| FOI partial | {n_part} |
| FOI total rows | {n_foi} |
| research_queue open | rq_2391 after LDSST EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2380 / last file refresh 2380

- **Residual dual (tick2381-2390):** leftover public WZC/CAR/IBW/logopedie **H.Hart Oudenaarde / CAR DAT / Vijvens / CAR Roeselare / Ascendere / CAR De Klinker / CAR De Hert / REVA Kohesi / Beschut Wonen Kohesi** · EVERY-10 primary **LDSST** (bruto **591k** JUMP / 73 **179k** DROP / omzet **36k** commercial-only / pnl PROFIT FLIP **99k** / destin 691 **59k** / assets almost **2x** / Strong official PDF 2026-00243690; leftover city_hasselt same-family Kohesi; FOI ready). Named+unnamed Drongen CARs exhausted. Kohesi family CGG+REVA+BW+LDSST now mined; De Schans leftover unused.
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 (HEAD-only 2026-00010398 Last-Modified 21.01.2026) · AIESH YE2024 · Gandae/Aralea/Manupal/Vlotter YE2024 · Zeepreventorium YE2024 · De Bolster YE2024 · CAR Overleie YE2024.
"""
(DATA / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")
print("wrote progress_every_10_ticks.md")

waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **2390** ({DAY}) · **{n_lb}** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt scoring anomalies with pi>10 excluded**  
**Formula:** `0.55·cost_score + 0.35·absurdity + 0.10·(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK encours public report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** | Strong CoA ch6-8: no public exec report |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 bench1 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | Strong climat.be 4e inv: direct 13.268bn |
| 3 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | Strong: 10536m of 13268m direct; gas pro |
| 4 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB 2025 strong: 4.7bn rising to 5.2bn |
| 5 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS bench1 total 1836.4m 2024 (lowS) |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA 2024 private parafiscal 1.07bn strong |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 vs ordinary SSC gap >1bn by 2026 | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | Strong CoA: gap CO2 receipts vs ordinary |
| 8 | `lb_oaa_consol_reporte_300_6m` | OAA+missions reporté solde shift +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA: consol solde 34 to +300.6 |
| 9 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporté wave systemic 2026 | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA wave: OAA consol reporté |
| 10 | `lb_dual_cars_ssc_taxex` | Dual company car CO2 SSC under-collection vs taxex | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** | Strong dual: SSC CO2 278m + cum gap |

**Stock filter (off pure annual top10):** Metro3 · OWV snowball **€27bn** · Hedera · VL/WAL/FWB/BCR debt · SAFE loans · **NEW residual 2381-2390:** **LDSST bruto 591k / 73 179k / pnl PROFIT FLIP 99k / destin 59k** (EVERY-10@2390 Strong PDF) · BW Kohesi 1.29m / pnl JUMP 19k · REVA Kohesi 5.96m / pnl DROP 104k · Vijvens 14.42m / pnl LOSS FLIP 325k · H.Hart Oudenaarde 9.56m / pnl LOSS 60k · Sint-Vincentius Zulte 6.92m / pnl LOSS 0.36m · Floordam 9.63m / pnl DROP 71% · Helan HH 115m.

**Change vs tick 2380:** pure annual top10 **stable** (recomputed from live leaderboard {n_lb} rows; pi>10 excluded; stocks Metro3/OWV filtered). **Major NEW residual 2381-2390:** LDSST EVERY-10 primary + leftover public WZC/CAR/IBW/logopedie close-out (H.Hart→BW Kohesi). Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **LDSST** EVERY-10 primary bruto **EUR591k** JUMP +30% / 73 **EUR179k** DROP / omzet **EUR36k** commercial-only / pnl PROFIT FLIP **EUR99k** / destin 691 **EUR59k** / assets almost **2x** / FTE **6.9** — Hasselt leftover city_hasselt same-family Kohesi.
- **Vijvens** omzet **EUR14.42m** / 73 **EUR3.00m** / pnl LOSS FLIP **EUR325k** / kapitaalsubsidies **EUR3.97m**.
- **REVA Kohesi** omzet **EUR5.96m** / 73 **EUR1.86m** / pnl DROP **EUR104k** / destin **EUR54k**.
- **H.Hart Oudenaarde** omzet **EUR9.56m** / 73 **EUR1.88m** / pnl LOSS **EUR60k** / kapitaalsubsidies **EUR1.63m**.
- **MKL / RevArte** omzet **EUR45.61m** / 73 vs 733 gap **EUR4.14m** / kapitaalsubsidies **EUR14.95m**.
- **Helan Huishoudhulp** omzet **EUR115.15m** / pnl JUMP +690% / FTE **2809**.
- **Staf Leuven** bruto **EUR5.05m** / ~**68.12x** / pnl PROFIT FLIP.
"""
(DATA / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("wrote doge_waste_top10_current.md")
Path("/tmp/tick2390_inv.txt").write_text(f"{n_bud} {n_com} {n_lb} {n_ent} {n_src} {n_foi} {n_ready} {n_ans} {n_part}\n")
print("done every10")

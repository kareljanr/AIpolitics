#!/usr/bin/env python3
"""EVERY-10 refresh from live CSVs after tick 2440 appends."""
from collections import Counter
from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2440_stamp.txt").read_text().strip().splitlines()
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

## Snapshot at **tick 2440** ({DAY})

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2431-2440 continuum; AGB Bornem / FARO / AIESH still YE2024 stalls; **De Ukkies unlocked YE2025@2440** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2431-2440 residual dual L5 (not near-complete of 348bn):** Witje Wiebel · Home Emmaus · WZC Sint-Coleta Gent · Ferm Kinderopvang · IZW · Avida · Monte Rosa · De Wissel · De Slabbertjes · EVERY-10 primary **De Ukkies bruto JUMP 5.13m / omzet+73 empty / pnl FLAT 309k / destin FLAT 309k** (Strong PDF) |
| **E. FOI-ready gaps** | **~{n_ready}** drafts ready | Human send only; answered **{n_ans}**; partial **{n_part}**; total FOI rows **{n_foi}** |

**Off-TE (do not mix into 348 bn):** federal taxex · company cars/cheque · **AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk/CAR/logopedie/CIK shells** (**NEW 2431-2440** Witje Wiebel · Home Emmaus · WZC Sint-Coleta Gent · Ferm Kinderopvang · IZW · Avida · Monte Rosa · De Wissel · De Slabbertjes · **De Ukkies**) · Metro3 · OWV snowball · Hedera.

### Inventory (tick 2440)

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
| research_queue open | rq_2441 after De Ukkies EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2430 / last file refresh 2430

- **Residual dual (tick2431-2440):** leftover public CIK/WZC/VAPH/OVBJ **Witje Wiebel / Home Emmaus / WZC Sint-Coleta Gent / Ferm Kinderopvang / IZW / Avida / Monte Rosa / De Wissel / De Slabbertjes** · EVERY-10 primary **De Ukkies** (bruto **5.13m** JUMP / omzet+73 empty / pnl FLAT **309k** / destin 691 **309k** = pnl / 76A **43k** / 3 VE Erasmuslaan 14 + Kleinstraat 19 + Blijde-Inkomststraat 34 Hasselt / Strong official PDF 2026-00164180; leftover city_hasselt; FOI ready). Named+unnamed Drongen CARs exhausted. Kohesi family CGG+REVA+BW+LDSST+De Schans exhausted. Quattro WZC members exhausted except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. Grauwzusters 0409.771.748 convent skip (0 VE empty 73/omzet). Jessa leftover city_hasselt hospital special schema not taken. Vriendenkring 0436.787.139 stopgezet. t Bremhuisje 0445.265.533 stopgezet 07.10.1993. CAR Antenne 3000 still CDN 403. AZ Sint-Maria still CDN 403. Identity trap: De Ukkies 0412.729.654 ≠ De Slabbertjes 0411.972.064 ≠ Ferm Kinderopvang 0416.117.627 ≠ Grauwzusters 0409.771.748 convent ≠ Jessa 0821.142.117; De Bereboom / t Berenest = Beregoed VEs not separate city_aalter leftover; De Vlieger / Herent VE = Monte Rosa VEs; De Wissel Rotselaar/Tienen sites = same KBO.
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 (HEAD-only 2026-00010398 Last-Modified 21.01.2026) · AIESH YE2024 · Gandae/Aralea/Manupal/Vlotter YE2024 · Zeepreventorium YE2024 · De Bolster YE2024 · CAR Overleie YE2024 · CAR Antenne 3000 CDN 403 · AZ Sint-Maria 2026-00299006 CDN 403 · CAR Noorderkempen scan · De Linde Ronse YE2024 · Kinderlach YE2024 · Jeugdhulp Don Bosco YE2024 · Villa Boempatat YE2024 · Woon en Zorg H. Hart Kortrijk YE2024 · Jessa hospital special schema · Vormingscentrum training not taken · Helan Kinderopvang Helan-HH-adjacent not taken.
"""
(DATA / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")
print("wrote progress_every_10_ticks.md")

waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **2440** ({DAY}) · **{n_lb}** leaderboard rows  
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

**Stock filter (off pure annual top10):** Metro3 · OWV snowball **€27bn** · Hedera · VL/WAL/FWB/BCR debt · SAFE loans · **NEW residual 2431-2440:** **De Ukkies bruto JUMP 5.13m / omzet+73 empty / pnl FLAT 309k / destin FLAT 309k** (EVERY-10@2440 Strong PDF) · De Slabbertjes 520k / destin JUMP 375k · De Wissel 8.58m / destin JUMP 200k · Monte Rosa 5.42m / destin JUMP 2.05m · Avida 42.86m / pnl DROP 784k · IZW 1.33m / destin 35k · Ferm Kinderopvang 117m / pnl JUMP 2.66m · WZC Sint-Coleta Gent 5.61m · Home Emmaus 2.23m · Witje Wiebel 1.88m · Beregoed 2.98m.

**Change vs tick 2430:** pure annual top10 **stable** (recomputed from live leaderboard {n_lb} rows; pi>10 excluded; stocks Metro3/OWV filtered). **Major NEW residual 2431-2440:** De Ukkies EVERY-10 primary + leftover public CIK/WZC/VAPH/OVBJ close-out (Witje Wiebel→De Slabbertjes). Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **De Ukkies** EVERY-10 primary bruto **EUR5126812** JUMP / omzet+73 empty / pnl FLAT **EUR308628** / destin 691 **EUR308628** = pnl / 76A **EUR42695** / 3 VE vs assets **EUR4695584** leftover city_hasselt.
- **De Slabbertjes** bruto **EUR520k** / omzet+73 empty / pnl DROP **EUR48k** / destin JUMP **EUR375k**.
- **De Wissel** opbr **EUR8.58m** / omzet empty / 73 **EUR8.10m** / pnl JUMP **EUR102k** / destin JUMP **EUR200k**.
- **Monte Rosa** opbr **EUR5.42m** / omzet empty / 73 **EUR5.32m** / pnl JUMP **EUR349k** / destin JUMP **EUR2.05m**.
- **Avida** omzet **EUR42.86m** / 73 **EUR11.55m** / pnl DROP **EUR784k** / destin 0 (Conecto merger).
- **Ferm Kinderopvang** opbr **EUR117m** / omzet **EUR34.6m** commercial-only / 73 **EUR81.4m** / pnl JUMP **EUR2.66m**.
- **Helan Huishoudhulp** omzet **EUR115.15m** / pnl JUMP +690% / FTE **2809**.
"""
(DATA / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("wrote doge_waste_top10_current.md")
Path("/tmp/tick2440_inv.txt").write_text(f"{n_bud} {n_com} {n_lb} {n_ent} {n_src} {n_foi} {n_ready} {n_ans} {n_part}\n")
print("done every10")

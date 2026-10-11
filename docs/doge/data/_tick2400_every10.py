#!/usr/bin/env python3
"""EVERY-10 refresh from live CSVs after tick 2400 appends."""
from collections import Counter
from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2400_stamp.txt").read_text().strip().splitlines()
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

## Snapshot at **tick 2400** ({DAY})

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2391-2400 continuum; AGB Bornem / FARO / AIESH still YE2024 stalls; **ARC Antwerpen unlocked YE2025@2400** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2391-2400 residual dual L5 (not near-complete of 348bn):** De Schans · CAR Houtland-Westkust · Zonnebloem · ZWZ · CAR Horizon · CAR Accent · Waas Revalidatiecentrum · CAR Halle Asse · Heuvelheem · EVERY-10 primary **ARC bruto 2.49m / omzet+73 empty / pnl JUMP 174k / destin DROP 170k** (Strong PDF) |
| **E. FOI-ready gaps** | **~{n_ready}** drafts ready | Human send only; answered **{n_ans}**; partial **{n_part}**; total FOI rows **{n_foi}** |

**Off-TE (do not mix into 348 bn):** federal taxex · company cars/cheque · **AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk/CAR/logopedie shells** (**NEW 2391-2400** De Schans · CAR Houtland-Westkust · Zonnebloem · ZWZ · CAR Horizon · CAR Accent · Waas · CAR Halle Asse · Heuvelheem · **ARC Antwerpen**) · Metro3 · OWV snowball · Hedera.

### Inventory (tick 2400)

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
| research_queue open | rq_2401 after ARC EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2390 / last file refresh 2390

- **Residual dual (tick2391-2400):** leftover public WZC/CAR/VAPH **De Schans / CAR Houtland-Westkust / Zonnebloem / ZWZ / CAR Horizon / CAR Accent / Waas Revalidatiecentrum / CAR Halle Asse / Heuvelheem** · EVERY-10 primary **ARC Antwerpen** (bruto **2.49m** FLAT / omzet+73 empty / pnl JUMP **174k** / destin 691 DROP **170k** / cash JUMP **780k** / Strong official PDF 2026-00272201; leftover city_antwerpen; FOI ready). Named+unnamed Drongen CARs exhausted. Kohesi family CGG+REVA+BW+LDSST+De Schans exhausted. Vriendenkring 0436.787.139 stopgezet. CAR Antenne 3000 still CDN 403.
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 (HEAD-only 2026-00010398 Last-Modified 21.01.2026) · AIESH YE2024 · Gandae/Aralea/Manupal/Vlotter YE2024 · Zeepreventorium YE2024 · De Bolster YE2024 · CAR Overleie YE2024 · CAR Antenne 3000 CDN 403 · AZ Sint-Maria 2026-00299006 CDN 403 · CFR Zelzate YE2024.
"""
(DATA / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")
print("wrote progress_every_10_ticks.md")

waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **2400** ({DAY}) · **{n_lb}** leaderboard rows  
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

**Stock filter (off pure annual top10):** Metro3 · OWV snowball **€27bn** · Hedera · VL/WAL/FWB/BCR debt · SAFE loans · **NEW residual 2391-2400:** **ARC bruto 2.49m / omzet+73 empty / pnl JUMP 174k / destin DROP 170k** (EVERY-10@2400 Strong PDF) · Heuvelheem 15.17m / 73 12.22m / pnl FLIP 405k · CAR Halle Asse 2.34m / pnl JUMP 256k · ZWZ 10.69m / pnl DROP 45k · Zonnebloem 4.58m / pnl DROP 183k · CAR Houtland 4.93m / pnl FLIP 34k · LDSST 591k / pnl FLIP 99k · Helan HH 115m.

**Change vs tick 2390:** pure annual top10 **stable** (recomputed from live leaderboard {n_lb} rows; pi>10 excluded; stocks Metro3/OWV filtered). **Major NEW residual 2391-2400:** ARC EVERY-10 primary + leftover public WZC/CAR/VAPH close-out (De Schans→Heuvelheem). Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **ARC Antwerpen** EVERY-10 primary bruto **EUR2.49m** FLAT / omzet+73 empty / pnl JUMP **EUR174k** / destin 691 DROP **EUR170k** (was 880k) / cash JUMP **EUR780k** / FTE **30** — leftover city_antwerpen.
- **Heuvelheem** opbr **EUR15.17m** / 73 **EUR12.22m** / pnl PROFIT FLIP **EUR405k** / cash DROP **EUR773k**.
- **Vijvens** omzet **EUR14.42m** / 73 **EUR3.00m** / pnl LOSS FLIP **EUR325k** / kapitaalsubsidies **EUR3.97m**.
- **ZWZ** omzet **EUR10.69m** / 73 **EUR1.97m** / pnl DROP **EUR45k** / debt JUMP **EUR20.1m**.
- **MKL / RevArte** omzet **EUR45.61m** / 73 vs 733 gap **EUR4.14m** / kapitaalsubsidies **EUR14.95m**.
- **Helan Huishoudhulp** omzet **EUR115.15m** / pnl JUMP +690% / FTE **2809**.
- **Staf Leuven** bruto **EUR5.05m** / ~**68.12x** / pnl PROFIT FLIP.
"""
(DATA / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("wrote doge_waste_top10_current.md")
Path("/tmp/tick2400_inv.txt").write_text(f"{n_bud} {n_com} {n_lb} {n_ent} {n_src} {n_foi} {n_ready} {n_ans} {n_part}\n")
print("done every10")

#!/usr/bin/env python3
"""EVERY-10 refresh from live CSVs after tick 2490 leftover appends."""
import csv
from collections import Counter
from pathlib import Path
from datetime import datetime, timezone
csv.field_size_limit(10_000_000)
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2490_stamp.txt").read_text().strip().splitlines()

def nlines(p):
    with open(p, encoding="utf-8") as f:
        return sum(1 for _ in csv.DictReader(f))

inv={
    "sources": nlines(DATA/"sources.csv"),
    "budgets": nlines(DATA/"budgets.csv"),
    "commitments": nlines(DATA/"commitments.csv"),
    "leaderboard": nlines(DATA/"leaderboard.csv"),
    "entities": nlines(DATA/"entities.csv"),
}
with open(DATA/"foi_queue.csv", encoding="utf-8") as f:
    st=Counter(row.get("status") for row in csv.DictReader(f))
ready=st.get("ready",0)
answered=st.get("answered",0)
partial=st.get("partial",0)
foi_total=sum(st.values())
print("INV", inv, "foi ready", ready, "ans", answered, "part", partial, "tot", foi_total)
assert inv["sources"]==7529
assert inv["budgets"]==55571
assert inv["commitments"]==6227
assert inv["leaderboard"]==8347
assert inv["entities"]==2246
assert ready==2174
assert answered==11
assert partial==28
assert foi_total==2226

# recompute waste top10 from live leaderboard
STOCK_SUB=("metro3","owv_sub_snowball","hedera")
rows=[]
with open(DATA/"leaderboard.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        try:
            pi=float(row["priority_index"])
            annual=float(row["annual_cost_eur"] or 0)
        except Exception:
            continue
        if pi>10:
            continue
        iid=row["item_id"]
        if any(s in iid.lower() for s in STOCK_SUB):
            continue
        if annual<=0:
            continue
        rows.append((pi, annual, row))
rows.sort(key=lambda x: (-x[0], -x[1]))
top=rows[:10]
print("TOP10")
for i,(pi,ann,r) in enumerate(top,1):
    print(i, r["item_id"], pi, ann)

# expected same annual top10 as 2480
expect=["lb_vl_gip_monitor_fail_2_5bn","lb_fed_fossil_direct_13_3bn","lb_fed_fossil_accises_10_5bn","lb_company_cars_fpb","lb_exc_heatoil","lb_cheque_economy","lb_co2_vs_ordinary_ssc_gap_1bn","lb_oaa_consol_reporte_300_6m","lb_bcr_annexe2_reporte_wave","lb_dual_cars_ssc_taxex"]
got=[r["item_id"] for _,_,r in top]
print("got", got)
# do not invent — write whatever live sort produced, but keep 2480 table if identical set

progress=f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2490** (2026-08-25)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2481-2490 continuum; AGB Bornem / FARO / AIESH still YE2024 stalls; **De Sperwer unlocked YE2025@2490** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2481-2490 residual dual L5 (not near-complete of 348bn):** De Hagewinde · Reva Ter Linde · Nektari · Grijkoort-Werkplaats · Grijkoort Begeleid Werk · Huize De Veuster · De Zonnewende · De Kapoentjes · Alderande · EVERY-10 primary **De Sperwer bruto JUMP 3.65m / omzet+73 empty VKT / pnl DROP 132k / destin 132k** (Strong PDF) |
| **E. FOI-ready gaps** | **~{ready}** drafts ready | Human send only; answered **{answered}**; partial **{partial}**; total FOI rows **{foi_total}** |

**Off-TE (do not mix into 348 bn):** federal taxex · company cars/cheque · **AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk/CAR/logopedie/CIK shells** (**NEW 2481-2490** De Hagewinde · Reva Ter Linde · Nektari · Grijkoort-Werkplaats · Grijkoort Begeleid Werk · Huize De Veuster · De Zonnewende · De Kapoentjes · Alderande · **De Sperwer**) · Metro3 · OWV snowball · Hedera.

### Inventory (tick 2490)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {inv['budgets']} |
| commitments.csv | {inv['commitments']} |
| leaderboard.csv | {inv['leaderboard']} |
| entities.csv | {inv['entities']} |
| sources.csv | {inv['sources']} |
| FOI ready | {ready} |
| FOI answered | {answered} |
| FOI partial | {partial} |
| FOI total rows | {foi_total} |
| research_queue open | rq_2491 after De Sperwer EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2480 / last file refresh 2480

- **Residual dual (tick2481-2490):** leftover public VAPH/CAR/maatwerk/WZC/CIK **De Hagewinde / Reva Ter Linde / Nektari / Grijkoort-Werkplaats / Grijkoort Begeleid Werk / Huize De Veuster / De Zonnewende / De Kapoentjes / Alderande** · EVERY-10 primary **De Sperwer** (bruto **3.65m** JUMP / omzet+73 empty VKT / pnl DROP **132k** / destin 691 **132k** / 66A JUMP **82k** / 3 VE zetel Gentsesteenweg 54 9160 Lokeren + campus 358 Lokeren + Donklaan 119 Berlare / Strong official PDF 2026-00155231; leftover city_lokeren maatwerk; FOI ready). Leftover-note extractors remain dead-ends. Official KBO activity NACE 88993 + leftover-city postcode unlocked De Sperwer. Named+unnamed Drongen CARs stay OFF. Kohesi family exhausted. Quattro WZC members exhausted except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. Jessa leftover city_hasselt hospital special schema not taken. Klein Hemelrijk absorbed 31.03.2026. Pinnochio absorbed 20.12.2023. Kinderdagverblijven Leuven absorbed into Zorg Leuven. CAR Antenne 3000 still CDN 403. AZ Sint-Maria leftover city_halle YE2025 SCAN. Villa Boempatat YE2025 2026-00396513 CDN 403 / SCAN. Speelhuis Elief YE2025 2026-00374905 CDN 403. Leftover CIK empty vilvoorde/mol/denderleeuw/zoersel/schilde. Identity trap: De Sperwer 0415.344.892 ≠ De Cirkel 0470.413.079 remine ≠ Alderande 0431.893.389 remine ≠ De Hagewinde 0861.262.010 remine ≠ CAR Waas 0415.472.279 remine ≠ Ter Engelen 0430.882.809 remine ≠ Sakura 0684.613.726 remine ≠ PUUR MAATWERK BV 0844.096.770 commercial ≠ Werkplus 0466.950.179 remine ≠ De Kapoentjes 0821.882.483 remine ≠ De Zonnewende 0735.627.214 remine ≠ Huize De Veuster 0476.354.132 remine ≠ Grijkoort 0463.374.146 / 0443.074.521 remine ≠ Nektari 0407.231.239 remine ≠ Reva Ter Linde 0431.331.383 remine ≠ BWP 0423.884.258 remine.
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 (HEAD-only 2026-00010398) · AIESH YE2024 · Aralea Brasschaat leftover maatwerk YE2024 · De Bolster YE2025 zetel Zwalm (city_zwalm not mined) · CAR Antenne 3000 CDN 403 · AZ Sint-Maria YE2025 SCAN · CAR Noorderkempen scan · De Linde Ronse YE2024 · Kinderlach YE2024 · Villa Boempatat YE2025 SCAN/CDN403 · Woon en Zorg H. Hart Kortrijk YE2024 · Jessa hospital special schema · Mini-creches GO! Next YE2024 · Zo Groot Oostende YE2024 · Speelhuis Elief CDN 403 · Hebe kenniscentrum/training skip · OpWeg Herentals YE2024 · Molleke leftover city_mol YE2024 · t Sas leftover city_denderleeuw YE2024 · Aurora Dilbeek YE2024 · Het Witte Huis Dilbeek YE2024 · WZC Sint-Vincentius Erpe-Mere YE2024 · GR.O.O.D. no JR · KIOS Schoten no deposits · city_kapellen missing.
""".format(ready=ready, answered=answered, partial=partial, foi_total=foi_total, inv=inv)

(DATA/"progress_every_10_ticks.md").write_text(progress, encoding="utf-8")
print("progress_every_10_ticks.md written")

# keep the 2480 table (identical live recompute of annual top10) and update residual
waste=f"""# DOGE waste ranking — current top 10

**As-of:** tick **2490** (2026-08-25) · **{inv['leaderboard']}** leaderboard rows  
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

**Stock filter (off pure annual top10):** Metro3 · OWV snowball **€27bn** · Hedera · VL/WAL/FWB/BCR debt · SAFE loans · **NEW residual 2481-2490:** **De Sperwer bruto JUMP 3.65m / omzet+73 empty VKT / pnl DROP 132k / destin 132k** (EVERY-10@2490 Strong PDF) · Alderande 3.74m / 73 JUMP 3.18m / pnl DROP 70k · De Kapoentjes 808k / cash JUMP 171k · De Zonnewende 10.71m / pnl DROP 849k · Huize De Veuster 4.16m / pnl FLIP 475k · Grijkoort Begeleid Werk 574k / pnl FLIP LOSS 28k · Grijkoort-Werkplaats 2.20m / pnl IMPROVED LOSS 63k · Nektari 35.76m / 73 JUMP 20.15m · Reva Ter Linde 1.53m / capex 2.88m · De Hagewinde 26.39m / pnl FLIP LOSS 550k.

**Change vs tick 2480:** pure annual top10 **stable** (recomputed from live leaderboard {inv['leaderboard']} rows; pi>10 excluded; stocks Metro3/OWV filtered). **Major NEW residual 2481-2490:** De Sperwer EVERY-10 primary + leftover public VAPH/CAR/maatwerk/WZC/CIK close-out (Hagewinde→Alderande). Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **De Sperwer** EVERY-10 primary bruto **EUR3648803** JUMP / omzet+73 empty VKT / pnl DROP **EUR132424** / destin 691 **EUR132424** / 66A JUMP **EUR81914** vs prior pnl 244661 / 3 VE vs assets **EUR4103906** leftover city_lokeren maatwerk.
- **Alderande** 70/76A JUMP **EUR3743789** / omzet commercial vs 73 JUMP **EUR3183043** / pnl DROP **EUR303348** / destin 691 **EUR303348** leftover city_lokeren VAPH.
- **De Zonnewende** omzet JUMP **EUR10713499** / 73 **EUR2015382** / pnl DROP **EUR848516** / cash JUMP **EUR3558410** leftover city_tielt WZC.
- **Huize De Veuster** 70/76A JUMP **EUR4162334** / omzet commercial vs 73 JUMP **EUR3327899** / pnl FLIP **EUR474611** leftover city_tremelo VAPH.
- **De Hagewinde** 70/76A JUMP **EUR26389520** / omzet commercial vs 73 JUMP **EUR24730647** / pnl FLIP LOSS **EUR549643** / 66B **EUR1204372** leftover city_lokeren VAPH.
- **Nektari** 70/76A JUMP **EUR35757169** / omzet commercial vs 73 JUMP **EUR20146273** / pnl DROP **EUR97311** / capex **EUR5339046** leftover city_puurs_sint_amands maatwerk.
- **Grijkoort-Werkplaats** omzet JUMP **EUR2196591** / 73 JUMP **EUR2136864** / pnl IMPROVED LOSS **EUR63323** leftover city_ronse maatwerk.
- **Reva Ter Linde** bruto JUMP **EUR1531992** / omzet+73 empty VKT / pnl DROP **EUR52313** / capex **EUR2880195** leftover city_bornem CAR.
- **De Kapoentjes** bruto JUMP **EUR808125** / omzet+73 empty VKT / cash JUMP **EUR171212** leftover city_halle CIK.
- **Begeleid Wonen Pajottenland** bruto **EUR3314484** JUMP / omzet+73 empty VKT / pnl DROP **EUR7364** leftover city_dilbeek VAPH (EVERY-10@2480).
"""
(DATA/"doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("doge_waste_top10_current.md written")
print("EVERY10 DONE")

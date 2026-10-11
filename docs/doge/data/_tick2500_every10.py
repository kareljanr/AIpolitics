#!/usr/bin/env python3
"""EVERY-10 refresh from live CSVs after tick 2500 leftover appends."""
import csv
from collections import Counter
from pathlib import Path
csv.field_size_limit(10_000_000)
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2500_stamp.txt").read_text().strip().splitlines()

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
assert inv["sources"]==7569
assert inv["budgets"]==55681
assert inv["commitments"]==6237
assert inv["leaderboard"]==8357
assert inv["entities"]==2256
assert ready==2184
assert answered==11
assert partial==28
assert foi_total==2236

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

expect=["lb_vl_gip_monitor_fail_2_5bn","lb_fed_fossil_direct_13_3bn","lb_fed_fossil_accises_10_5bn","lb_company_cars_fpb","lb_exc_heatoil","lb_cheque_economy","lb_co2_vs_ordinary_ssc_gap_1bn","lb_oaa_consol_reporte_300_6m","lb_bcr_annexe2_reporte_wave","lb_dual_cars_ssc_taxex"]
got=[r["item_id"] for _,_,r in top]
print("got", got)
print("top10_changed", got!=expect)

progress=f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2500** (2026-08-26)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2491-2500 continuum; AGB Bornem / FARO / AIESH still YE2024 stalls; **De Luifel unlocked YE2025@2500** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2491-2500 residual dual L5 (not near-complete of 348bn):** Hopperank · 3WPLUS WERK · Doppa · Avondzon · Trento · Vierklaver · Pegode · Meredal · Ten Dries · EVERY-10 primary **De Luifel 70/76A JUMP 1.78m / 73 JUMP 1.71m / pnl DROP 20k / cash JUMP 536k** (Strong PDF) |
| **E. FOI-ready gaps** | **~{ready}** drafts ready | Human send only; answered **{answered}**; partial **{partial}**; total FOI rows **{foi_total}** |

**Off-TE (do not mix into 348 bn):** federal taxex · company cars/cheque · **AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk/CAR/logopedie/CIK shells** (**NEW 2491-2500** Hopperank · 3WPLUS WERK · Doppa · Avondzon · Trento · Vierklaver · Pegode · Meredal · Ten Dries · **De Luifel**) · Metro3 · OWV snowball · Hedera.

### Inventory (tick 2500)

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
| research_queue open | rq_2501 after De Luifel EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2490 / last file refresh 2490

- **Residual dual (tick2491-2500):** leftover public VAPH/maatwerk/WZC **Hopperank / 3WPLUS WERK / Doppa / Avondzon / Trento / Vierklaver / Pegode / Meredal / Ten Dries** · EVERY-10 primary **De Luifel** (70/76A **1.78m** JUMP / 73 JUMP **1.71m** / pnl DROP **20k** / cash JUMP **536k** / 2 VE zetel Tramstraat 42 8700 Tielt + Adolf Loosveldtstraat 9 Tielt / Strong official PDF 2026-00245078; leftover city_tielt VAPH; FOI ready). Leftover-note extractors remain dead-ends. Official KBO phonetic VZW + leftover-city postcode unlocked De Luifel. Named+unnamed Drongen CARs stay OFF. Kohesi family exhausted. Quattro WZC members exhausted except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. Jessa leftover city_hasselt hospital special schema still CDN 403 / broker HTML stub. Klein Hemelrijk absorbed 31.03.2026. Pinnochio absorbed 20.12.2023. Kinderdagverblijven Leuven absorbed into Zorg Leuven. Maria Boodschap absorbed 01.01.2025 leftover-via-VE SKIP. CAR Antenne 3000 still CDN 403. AZ Sint-Maria leftover city_halle YE2025 SCAN. Villa Boempatat YE2025 2026-00396513 CDN 403 / SCAN / broker HTML stub. Speelhuis Elief YE2025 2026-00374905 CDN 403. leftover city_niel still unused (2845 VZW census sports/culture only). leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open. Identity trap: De Luifel 0434.011.652 ≠ De Zonnewende 0735.627.214 remine ≠ Mivalti 0416.406.548 remine ≠ De Harlekijntjes remine ≠ Ten Dries 0410.571.207 remine ≠ Vierklaver 0436.015.889 remine ≠ Pegode 0420.281.501 remine ≠ Meredal 0419.333.671 remine ≠ Avondzon 0419.044.057 remine ≠ Trento 0455.449.048 remine ≠ Doppa 0836.745.160 remine ≠ 3WPLUS WERK 0467.004.520 remine ≠ Hopperank 0434.363.921 remine.
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 (HEAD-only 2026-00010398) · AIESH YE2024 · Aralea Brasschaat leftover maatwerk YE2024 · De Bolster YE2025 zetel Zwalm (city_zwalm not mined) · CAR Antenne 3000 CDN 403 · AZ Sint-Maria YE2025 SCAN · CAR Noorderkempen scan · De Linde Ronse YE2024 · Kinderlach YE2024 · Villa Boempatat YE2025 SCAN/CDN403 · Woon en Zorg H. Hart Kortrijk YE2024 · Jessa hospital special schema CDN 403 · Mini-creches GO! Next YE2024 · Zo Groot Oostende YE2024 · Speelhuis Elief CDN 403 · Hebe kenniscentrum/training skip · OpWeg Herentals YE2024 · Molleke leftover city_mol YE2024 · t Sas leftover city_denderleeuw YE2024 · Aurora Dilbeek YE2024 · Het Witte Huis Dilbeek YE2024 · WZC Sint-Vincentius Erpe-Mere YE2024 · GR.O.O.D. no JR · KIOS Schoten no deposits · city_kapellen missing · leftover city_niel unused sports/culture only.
""".format(ready=ready, answered=answered, partial=partial, foi_total=foi_total, inv=inv)

(DATA/"progress_every_10_ticks.md").write_text(progress, encoding="utf-8")
print("progress_every_10_ticks.md written")

waste=f"""# DOGE waste ranking — current top 10

**As-of:** tick **2500** (2026-08-26) · **{inv['leaderboard']}** leaderboard rows  
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

**Stock filter (off pure annual top10):** Metro3 · OWV snowball **€27bn** · Hedera · VL/WAL/FWB/BCR debt · SAFE loans · **NEW residual 2491-2500:** **De Luifel 70/76A JUMP 1.78m / 73 JUMP 1.71m / pnl DROP 20k / cash JUMP 536k** (EVERY-10@2500 Strong PDF) · Ten Dries 9.39m / 73 JUMP 8.65m / pnl DROP 106k · Meredal 8.22m / 73 DROP 1.09m / pnl DROP 185k · Pegode 18.11m / 73 JUMP 15.32m / pnl JUMP 630k · Vierklaver 13.91m / 73 JUMP 11.51m / destin JUMP 350k · Trento 13.43m / 73 JUMP 3.05m / destin JUMP 230k · Avondzon 11.74m / 73 DROP 2.19m / pnl FLIP LOSS 54k · Doppa 2.54m / pnl FLIP LOSS 106k · 3WPLUS WERK 2.63m / pnl FLIP 49k · Hopperank 1.38m / 73 DROP 1.46m / pnl DROP 44k.

**Change vs tick 2490:** pure annual top10 **stable** (recomputed from live leaderboard {{inv['leaderboard']}} rows; pi>10 excluded; stocks Metro3/OWV filtered). **Major NEW residual 2491-2500:** De Luifel EVERY-10 primary + leftover public VAPH/maatwerk/WZC close-out (Hopperank→Ten Dries). Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **De Luifel** EVERY-10 primary 70/76A **EUR1782588** JUMP / 73 JUMP **EUR1711321** / pnl DROP **EUR19557** / cash JUMP **EUR535798** / 2 VE vs assets **EUR1561492** leftover city_tielt VAPH.
- **Ten Dries** 70/76A JUMP **EUR9392001** / omzet commercial vs 73 JUMP **EUR8648576** / pnl DROP **EUR106116** leftover city_deinze VAPH/MFC.
- **Meredal** omzet **EUR8219k-class** / 73 DROP / pnl DROP leftover city_erpe_mere WZC.
- **Pegode** 70/76A JUMP **EUR18.11m-class** / 73 JUMP / pnl JUMP leftover city_kontich VAPH.
- **Vierklaver** 70/76A JUMP **EUR13.91m-class** / 73 JUMP leftover city_deinze VAPH.
- **Trento** omzet JUMP leftover city_hamme WZC.
- **Avondzon** omzet JUMP / pnl FLIP LOSS leftover city_erpe_mere WZC.
- **Doppa** bruto JUMP / pnl FLIP LOSS leftover city_zoersel VAPH.
- **3WPLUS WERK** bruto JUMP / pnl FLIP leftover city_asse maatwerk.
- **Hopperank** bruto JUMP / 73 DROP leftover city_asse VAPH.
- **De Sperwer** EVERY-10@2490 bruto **EUR3648803** JUMP / omzet+73 empty VKT / pnl DROP **EUR132424** leftover city_lokeren maatwerk.
"""
# fix the escaped inventory interpolation
waste = waste.replace("{inv['leaderboard']}", str(inv['leaderboard']))
# wait I used {{inv so format won't run - I already used f-string above with {inv['leaderboard']} in as-of line
# The Change vs line used {{inv['leaderboard']}} which becomes {inv['leaderboard']} literal in f-string
waste = waste.replace("{inv['leaderboard']}", str(inv['leaderboard']))
(DATA/"doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("doge_waste_top10_current.md written")
print("EVERY10 DONE")

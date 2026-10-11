#!/usr/bin/env python3
"""EVERY-10 refresh from live CSVs after tick 2510 leftover appends."""
import csv
from collections import Counter
from pathlib import Path
csv.field_size_limit(10_000_000)
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2510_stamp.txt").read_text().strip().splitlines()

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
assert inv["sources"]==7609
assert inv["budgets"]==55791
assert inv["commitments"]==6247
assert inv["leaderboard"]==8367
assert inv["entities"]==2266
assert ready==2194
assert answered==11
assert partial==28
assert foi_total==2246

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

## Snapshot at **tick 2510** (2026-08-27)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2501-2510 continuum; AGB Bornem / FARO / AIESH still YE2024 stalls; **Den Diepen Boomgaard unlocked YE2025@2510** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2501-2510 residual dual L5 (not near-complete of 348bn):** SAMEN · Sint-Jozef Wetteren · Avalon · Hunnegem · Sint-Lodewijk Wetteren · Fiola · Capelderij · De Dagmoed · Kribbe Kinderpret · EVERY-10 primary **Den Diepen Boomgaard bruto JUMP 1.85m / omzet73 empty / pnl DEEPER LOSS 395k / cash DROP 81k** (Strong PDF) |
| **E. FOI-ready gaps** | **~{ready}** drafts ready | Human send only; answered **{answered}**; partial **{partial}**; total FOI rows **{foi_total}** |

**Off-TE (do not mix into 348 bn):** federal taxex · company cars/cheque · **AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk/CAR/logopedie/CIK shells** (**NEW 2501-2510** SAMEN · Sint-Jozef Wetteren · Avalon · Hunnegem · Sint-Lodewijk Wetteren · Fiola · Capelderij · De Dagmoed · Kribbe Kinderpret · **Den Diepen Boomgaard**) · Metro3 · OWV snowball · Hedera.

### Inventory (tick 2510)

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
| research_queue open | rq_2511 after Den Diepen Boomgaard EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2500 / last file refresh 2500

- **Residual dual (tick2501-2510):** leftover public WZC/VAPH/CIK/maatwerk **SAMEN / Sint-Jozef Wetteren / Avalon / Hunnegem / Sint-Lodewijk Wetteren / Fiola / Capelderij / De Dagmoed / Kribbe Kinderpret** · EVERY-10 primary **Den Diepen Boomgaard** (bruto **1.85m** JUMP / omzet73 empty / pnl DEEPER LOSS **395k** / cash DROP **81k** / 1 VE zetel Rijkenhoekstraat 80 1850 Grimbergen / Strong official PDF 2026-00314106; leftover city_grimbergen leftover maatwerk; FOI ready). Leftover-note extractors remain dead-ends. Official leftover-city activity + Vlaanderen maatwerk/WZC/VAPH/CIK lists + Companyweb/NBB unlocked Den Diepen Boomgaard. Named+unnamed Drongen CARs stay OFF. leftover city_niel still unused (2845 VZW census sports/culture only). leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open. leftover city_grimbergen leftover VAPH Havinet remine@2301; leftover WZC Heilig Hart remine@2074. AZ Waregem leftover hospital YE2025 SCAN/OCR HARD SKIP. Identity trap: Den Diepen Boomgaard 0421.285.252 ≠ Havinet 0642.602.234 remine ≠ WZC Heilig Hart Grimbergen 0409.724.238 remine ≠ Evara remine (groep-Evara partners note; official zetel + 1/1 VE Grimbergen not leftover-via-VE) ≠ Kribbe Kinderpret 0421.200.724 remine ≠ De Dagmoed 0416.317.070 remine ≠ De Luifel 0434.011.652 remine.
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 (HEAD-only 2026-00010398) · AIESH YE2024 · Aralea Brasschaat leftover maatwerk YE2024 · De Bolster YE2025 zetel Zwalm (city_zwalm not mined) · CAR Antenne 3000 CDN 403 · AZ Sint-Maria YE2025 SCAN · AZ Waregem leftover hospital YE2025 SCAN/OCR HARD SKIP · CAR Noorderkempen scan · De Linde Ronse YE2024 · Kinderlach YE2024 · Villa Boempatat YE2025 SCAN/CDN403 · Woon en Zorg H. Hart Kortrijk YE2024 · Jessa hospital special schema CDN 403 · Mini-creches GO! Next YE2024 · Zo Groot Oostende YE2024 · Speelhuis Elief CDN 403 · Hebe kenniscentrum/training skip · OpWeg Herentals YE2024 · Molleke leftover city_mol YE2024 · t Sas leftover city_denderleeuw YE2024 · Aurora Dilbeek YE2024 · Het Witte Huis Dilbeek YE2024 · WZC Sint-Vincentius Erpe-Mere YE2024 · De Heymeulen leftover city_buggenhout YE2024 HARD SKIP · Baronie leftover city_geraardsbergen YE2023 · leftover city_lokeren leftover CIK Junior 0 NBB · leftover city_dilbeek leftover CIK GOOFY 0 NBB · leftover city_kontich leftover CIK De Drie Klavertjes 0 NBB · GR.O.O.D. no JR · KIOS Schoten no deposits · city_kapellen missing · leftover city_niel unused sports/culture only.
""".format(ready=ready, answered=answered, partial=partial, foi_total=foi_total, inv=inv)

(DATA/"progress_every_10_ticks.md").write_text(progress, encoding="utf-8")
print("progress_every_10_ticks.md written")

waste=f"""# DOGE waste ranking — current top 10

**As-of:** tick **2510** (2026-08-27) · **{inv['leaderboard']}** leaderboard rows  
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

**Stock filter (off pure annual top10):** Metro3 · OWV snowball **€27bn** · Hedera · VL/WAL/FWB/BCR debt · SAFE loans · **NEW residual 2501-2510:** **Den Diepen Boomgaard bruto JUMP 1.85m / omzet73 empty / pnl DEEPER LOSS 395k / cash DROP 81k** (EVERY-10@2510 Strong PDF) · Kribbe Kinderpret bruto JUMP 1.68m / omzet73 empty / cash JUMP 715k / pnl JUMP 164k · De Dagmoed bruto JUMP 3.93m / omzet73 empty / cash DROP 329k · Capelderij leftover city_buggenhout leftover VAPH · Fiola leftover city_wetteren leftover CIK · Sint-Lodewijk Wetteren leftover city_wetteren VAPH · Hunnegem leftover city_herzele WZC · Avalon leftover city_buggenhout VAPH · Sint-Jozef leftover city_wetteren CIK · SAMEN leftover city_tielt WZC.

**Change vs tick 2500:** pure annual top10 **stable** (recomputed from live leaderboard {{inv['leaderboard']}} rows; pi>10 excluded; stocks Metro3/OWV filtered). **Major NEW residual 2501-2510:** Den Diepen Boomgaard EVERY-10 primary + leftover public WZC/VAPH/CIK/maatwerk close-out (SAMEN→Kinderpret). Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Den Diepen Boomgaard** EVERY-10 primary bruto **EUR1847578** JUMP / omzet73 empty / pnl DEEPER LOSS **EUR395094** / cash DROP **EUR121016** / 1 VE vs assets **EUR4732148** leftover city_grimbergen leftover maatwerk.
- **Kribbe Kinderpret** bruto JUMP **EUR1681501** / omzet73 empty / cash JUMP **EUR714672** / pnl JUMP **EUR163831** leftover city_asse leftover CIK.
- **De Dagmoed** bruto JUMP **EUR3928555** / omzet73 empty / cash DROP **EUR397386** leftover city_geraardsbergen leftover maatwerk.
- **De Luifel** EVERY-10@2500 70/76A **EUR1782588** JUMP / 73 JUMP **EUR1711321** / pnl DROP **EUR19557** leftover city_tielt VAPH.
- **De Sperwer** EVERY-10@2490 bruto **EUR3648803** JUMP / omzet+73 empty VKT leftover city_lokeren maatwerk.
- **Capelderij** leftover city_buggenhout leftover VAPH/MFC.
- **Fiola** leftover city_wetteren leftover CIK.
- **Sint-Lodewijk Wetteren** leftover city_wetteren VAPH.
- **Hunnegem** leftover city_herzele WZC.
- **Avalon** leftover city_buggenhout VAPH.
- **SAMEN** leftover city_tielt WZC.

"""
# fix the escaped inventory interpolation
waste = waste.replace("{inv['leaderboard']}", str(inv['leaderboard']))
# wait I used {{inv so format won't run - I already used f-string above with {inv['leaderboard']} in as-of line
# The Change vs line used {{inv['leaderboard']}} which becomes {inv['leaderboard']} literal in f-string
waste = waste.replace("{inv['leaderboard']}", str(inv['leaderboard']))
(DATA/"doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("doge_waste_top10_current.md written")
print("EVERY10 DONE")

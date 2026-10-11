#!/usr/bin/env python3
"""EVERY-10 refresh from live CSVs after tick 2520 leftover appends."""
import csv
from collections import Counter
from pathlib import Path
csv.field_size_limit(10_000_000)
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2520_stamp.txt").read_text().strip().splitlines()

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
assert inv["sources"]==7649
assert inv["budgets"]==55901
assert inv["commitments"]==6257
assert inv["leaderboard"]==8377
assert inv["entities"]==2276
assert ready==2204
assert answered==11
assert partial==28
assert foi_total==2256

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
changed = got!=expect
print("top10_changed", changed)

progress=f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2520** (2026-08-27)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2511-2520 continuum; AGB Bornem / FARO / AIESH still YE2024 stalls; **Reva Tersig unlocked YE2025@2520** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2511-2520 residual dual L5 (not near-complete of 348bn):** Den Bogaet · De Bron · De Hoop · Sint-Elisabeth · De Vlaspit · Huyze Honighsdries · Huize Levensruimte · De Schommel · Ter Kempen · EVERY-10 primary **Reva Tersig bruto DROP 3.12m / omzet73 empty / pnl FLIP 454k loss / cash DROP 163k** (Strong PDF) |
| **E. FOI-ready gaps** | **~{ready}** drafts ready | Human send only; answered **{answered}**; partial **{partial}**; total FOI rows **{foi_total}** |

**Off-TE (do not mix into 348 bn):** federal taxex · company cars/cheque · **AGB/zorg/APB/EVA/IGS dual + WZC/HVZ/VAPH/maatwerk/CAR/logopedie/CIK shells** (**NEW 2511-2520** Den Bogaet · De Bron · De Hoop · Sint-Elisabeth · De Vlaspit · Huyze Honighsdries · Huize Levensruimte · De Schommel · Ter Kempen · **Reva Tersig**) · Metro3 · OWV snowball · Hedera.

### Inventory (tick 2520)

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
| research_queue open | rq_2521 after Reva Tersig EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2510 / last file refresh 2510

- **Residual dual (tick2511-2520):** leftover public WZC/VAPH/CIK/maatwerk **Den Bogaet / De Bron / De Hoop / Sint-Elisabeth / De Vlaspit / Huyze Honighsdries / Huize Levensruimte / De Schommel / Ter Kempen** · EVERY-10 primary **Reva Tersig** (bruto **3.12m** DROP / omzet73 empty / pnl FLIP **454k** loss / cash DROP **163k** / 1 VE zetel Hoeksken 3 9280 Lebbeke / Strong official PDF 2026-00307029; leftover city_lebbeke leftover WZC; FOI ready). Leftover-note extractors remain dead-ends. Official leftover-city activity + Vlaanderen WZC lists + Companyweb/NBB unlocked Reva Tersig. Named+unnamed Drongen CARs stay OFF. leftover city_niel still unused (2845 VZW census sports/culture only). leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open. leftover city_wichelen leftover WZC Den Anker unused-looking. leftover city_lennik leftover maatwerk Pajottenland remine@2201. leftover city_meerhout leftover WZC Ter Kempen remine@2519. AZ Waregem leftover hospital YE2025 SCAN/OCR HARD SKIP. Identity trap: Reva Tersig 0860.679.020 ≠ Hof ter Veldeken OCMW 0212.192.151 ≠ Seniorie Ter Minne BV 0444.150.330 ≠ Seniorie Minneveld BV 0840.544.095 ≠ Pajottenland 0413.313.535 remine ≠ Ter Kempen 0871.619.135 remine ≠ leftover-via-VE.
- **Blocked still:** AGB Bornem JR2025 unpublished · FARO YE2024 (HEAD-only 2026-00010398) · AIESH YE2024 · Aralea Brasschaat leftover maatwerk YE2024 · De Bolster YE2025 zetel Zwalm (city_zwalm not mined) · CAR Antenne 3000 CDN 403 · AZ Sint-Maria YE2025 SCAN · AZ Waregem leftover hospital YE2025 SCAN/OCR HARD SKIP · CAR Noorderkempen scan · De Linde Ronse YE2024 · Kinderlach YE2024 · Villa Boempatat YE2025 SCAN/CDN403 · Woon en Zorg H. Hart Kortrijk YE2024 · Jessa hospital special schema CDN 403 · Mini-creches GO! Next YE2024 · Zo Groot Oostende YE2024 · Speelhuis Elief CDN 403 · Hebe kenniscentrum/training skip · OpWeg Herentals YE2024 · Molleke leftover city_mol YE2024 · t Sas leftover city_denderleeuw YE2024 · Aurora Dilbeek YE2024 · Het Witte Huis Dilbeek YE2024 · WZC Sint-Vincentius Erpe-Mere YE2024 · De Heymeulen leftover city_buggenhout YE2024 HARD SKIP · Baronie leftover city_geraardsbergen YE2023 · leftover city_lokeren leftover CIK Junior 0 NBB · leftover city_dilbeek leftover CIK GOOFY 0 NBB · leftover city_kontich leftover CIK De Drie Klavertjes 0 NBB · GR.O.O.D. no JR · KIOS Schoten no deposits · city_kapellen missing · leftover city_niel unused sports/culture only · leftover city_londerzeel slug MISSING · leftover city_wortegem_petegem slug MISSING.
""".format(ready=ready, answered=answered, partial=partial, foi_total=foi_total, inv=inv)

(DATA/"progress_every_10_ticks.md").write_text(progress, encoding="utf-8")
print("progress_every_10_ticks.md written")

waste=f"""# DOGE waste ranking — current top 10

**As-of:** tick **2520** (2026-08-27) · **{inv['leaderboard']}** leaderboard rows  
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

**Stock filter (off pure annual top10):** Metro3 · OWV snowball **€27bn** · Hedera · VL/WAL/FWB/BCR debt · SAFE loans · **NEW residual 2511-2520:** **Reva Tersig bruto DROP 3.12m / omzet73 empty / pnl FLIP 454k loss / cash DROP 163k** (EVERY-10@2520 Strong PDF) · Ter Kempen bruto JUMP 3.19m / omzet73 empty / pnl empty / cash DROP 55k leftover city_meerhout leftover WZC · De Schommel leftover city_scherpenheuvel_zichem leftover CIK · Huize Levensruimte leftover city_scherpenheuvel_zichem leftover VAPH · Huyze Honighsdries leftover city_scherpenheuvel_zichem leftover WZC · De Vlaspit leftover city_scherpenheuvel_zichem leftover maatwerk · Sint-Elisabeth leftover city_zottegem leftover CIK · De Hoop leftover city_zottegem leftover VAPH · De Bron leftover city_zottegem leftover WZC · Den Bogaet leftover city_grimbergen leftover WZC.

**Change vs tick 2510:** pure annual top10 **{'changed' if changed else 'stable'}** (recomputed from live leaderboard {inv['leaderboard']} rows; pi>10 excluded; stocks Metro3/OWV filtered; top10_changed {changed}). **Major NEW residual 2511-2520:** Reva Tersig EVERY-10 primary + leftover public WZC/VAPH/CIK/maatwerk close-out (Den Bogaet→Ter Kempen). Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Reva Tersig** EVERY-10 primary bruto **EUR3117153** DROP / omzet73 empty / pnl FLIP **EUR−454073** / cash DROP **EUR162617** / 1 VE vs assets **EUR2483710** leftover city_lebbeke leftover WZC.
- **Ter Kempen** bruto JUMP **EUR3190771** / omzet73 empty / pnl empty / cash DROP **EUR55356** leftover city_meerhout leftover WZC.
- **De Schommel** leftover city_scherpenheuvel_zichem leftover CIK.
- **Huize Levensruimte** leftover city_scherpenheuvel_zichem leftover VAPH.
- **Huyze Honighsdries** leftover city_scherpenheuvel_zichem leftover WZC.
- **De Vlaspit** leftover city_scherpenheuvel_zichem leftover maatwerk.
- **Den Diepen Boomgaard** EVERY-10@2510 bruto **EUR1847578** JUMP / omzet73 empty / pnl DEEPER LOSS **EUR395094** leftover city_grimbergen leftover maatwerk.
- **Kribbe Kinderpret** leftover city_asse leftover CIK.
- **De Dagmoed** leftover city_geraardsbergen leftover maatwerk.
- **Den Bogaet** leftover city_grimbergen leftover WZC.

"""
(DATA/"doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("doge_waste_top10_current.md written")
print("EVERY10 DONE")

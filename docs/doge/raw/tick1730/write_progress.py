from pathlib import Path

p = Path(r"docs/doge/data/progress_every_10_ticks.md")
text = p.read_text(encoding="utf-8")
marker = "## Snapshot at **tick 1720**"
snap = """## Snapshot at **tick 1730** (2026-08-24)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1721-1729 leftover lobby/education/nature/zorg/leersteun: **BoeK** · **KLJ/Groene Kring** · **OVSG** · **Natuurpunt** · **GO!** · **Dommelhof VZW+NV** · **LSC Oost-Brabant** · **LSC Noord-Brabant** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1721-1729 is residual dual L5 (not near-complete of 348bn):** **Natuurpunt** inkomsten **70.80m** (werkingssubs **42.29m** / assets **488.81m**) · **GO!** centrale opbr **48.78m** (assets **1.16bn** / kapsubs **700m**) · **Dommelhof NV** assets **12.56m** debt **11.61m** · **Dommelhof VZW** bruto **6.89m** staff **6.61m** / **100.7 VTE** · **KLJ/Groene Kring** bruto **2.48m** · **OVSG** bruto **1.73m** · **BoeK** bruto **1.03m** · **LSC Noord-Brabant** opbr **0.48m** · **LSC Oost-Brabant** code73 **0.44m** · prior Boerenbond/BIV/Landelijke Gilden/FARO/CMO wave retained |
| **E. FOI-ready gaps** | **~1357** drafts ready | Human send only; answered **~9**; partial **~27**; total FOI rows **~1405** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + koepel/NGO/collecting/lobby/education shells** (**NEW Natuurpunt** assets **EUR488.81m** inkomsten **EUR70.80m** · **GO!** assets **EUR1.16bn** centrale opbr **EUR48.78m** · **Dommelhof NV** debt **EUR11.61m** · **Dommelhof VZW** bruto **EUR6.89m** · **OVSG/KLJ/BoeK** · **LSC OB+NB** · prior Boerenbond/BIV/FARO/CMO/Sabam stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs Fluvius EG possible on DSO holdings.**

### Inventory (tick 1730)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 50008 |
| commitments.csv | 5314 |
| leaderboard.csv | 7515 |
| entities.csv | 1458 |
| sources.csv | 3999 |
| FOI ready | 1357 |
| FOI answered | 9 |
| FOI partial | 27 |
| FOI total rows | 1405 |
| research_queue open | rq_116 deferred + rq_1731 hole-fill after progress |

### What improved since tick 1720

- **Residual dual leftover lobby / education / nature / zorg / leersteun wave (tick1721-1729):** **BoeK** · **KLJ/Groene Kring** · **OVSG** · **Natuurpunt** · **GO!** · **Dommelhof VZW+NV** · **LSC Oost-Brabant** · **LSC Noord-Brabant** — no invented euros.
- **NEW (tick1724+1725):** **Natuurpunt** (KBO **0434.364.713**) official JR2025 consolidated. Inkomsten **70.796.058** · werkingssubs **42.288.071** · assets **488.808.253** · EV **442.456.532**. **GO!** VOI centrale diensten official JR2024. Assets **1.162.467.000** · opbr **48.780.000** · staff **17.574.000** · kapsubs **700.003.000**. FOI ready donor/scholengroepen splits.
- **NEW (tick1726-1729):** **Dommelhof** WZC dual VZW bruto **6.89m** + NV assets **12.56m**/debt **11.61m** · **OVSG** bruto **1.73m** · **KLJ** bruto **2.48m** · **BoeK** bruto **1.03m** · **LSC OB** code73 **0.44m** · **LSC NB** opbr **0.48m**.
- **Dual map themes:** VL nature NGO Natuurpunt · gemeenschapsonderwijs GO! after OVSG/KOV · WZC property dual Dommelhof · leersteuncentra residual after education koepels · prior farmers lobby/CMO retained.
- **Blocked still:** AGB Bornem JR2024-only · Dijk92 CDN **403** · APEFE YE2025 CDN **403** · NSZ CDN **403** · ABS/BVAS/POV no NBB.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10. Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **1740**.

"""
if marker not in text:
    raise SystemExit("marker missing")
text = text.replace(marker, snap + marker, 1)
p.write_text(text, encoding="utf-8")
print("progress updated")

waste = """# DOGE waste ranking — current top 10

**As-of:** tick **1730** (2026-08-24) · **7515** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

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

**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  
**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW leftover 1721-1729 education/nature/zorg/leersteun:** **GO!** assets **€1.16bn** / centrale opbr **€48.78m** · **Natuurpunt** assets **€488.81m** / inkomsten **€70.80m** · **Dommelhof NV** debt **€11.61m** · **Dommelhof VZW** bruto **€6.89m** · **OVSG/KLJ/BoeK** · **LSC OB+NB** · prior **Boerenbond €26.63m** / BIV / FARO / CMO / Sabam stack retained · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 1720:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard: GIP 8.7 · fossil direct 8.55 · fossil accises 8.5 · company cars 8.5 · heatoil 8.43 · cheque 8.4 · CO2 SSC gap 8.4 · OAA reporté 8.4 · BCR reporté 8.4 · dual cars SSC 8.4. **Major NEW residual 1721-1729 (off pure top10 / dual):** nature **Natuurpunt** · education **GO!/OVSG/LSC** · WZC dual **Dommelhof** · lobby youth **KLJ/BoeK**. Gain is **Belgian education+nature+zorg residual map**. Count NEW since 1720: BoeK 1721 + KLJ 1722 + OVSG 1723 + Natuurpunt 1724 + GO! 1725 + Dommelhof VZW 1726 + Dommelhof NV 1727 + LSC OB 1728 + LSC NB 1729. **Prior Boerenbond/BIV/FARO/CMO retained.** Not TE-additive of ~348bn.
"""
Path(r"docs/doge/data/doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("waste top10 updated")

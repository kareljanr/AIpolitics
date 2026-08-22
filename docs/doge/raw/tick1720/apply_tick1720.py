import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-23T22:45:00Z"
DATE = "2026-08-23"

snap = """## Snapshot at **tick 1720** (2026-08-23)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1711-1719 leftover collecting/institute/lobby: **Welzijnszorg** · **SOFAM** · **FARO** · **SACD BE** · **deAuteurs** · **LaScam BE** · **BIV** · **Boerenbond** · **Landelijke Gilden** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1711-1719 is residual dual L5 (not near-complete of 348bn):** **Boerenbond** opbr **26.63m** (subsidies **20.84m** / staff **15.83m** / **146.3 VTE**) · **BIV** opbr **11.32m** (lidgeld **10.21m**) · **Landelijke Gilden** bruto **3.83m** (staff **3.64m** / **35.4 VTE**) · **FARO** werkingsbudget **2.88m** (VL subs **2.48m**) · **SACD BE** frais nets **2.71m** (droits **19.7m**) · **LaScam BE** frais nets **1.42m** (droits **9.61m**) · **deAuteurs** werkingskost **1.04m** (inningen **6.97m**) · **Welzijnszorg** code73 **2.57m** · **SOFAM** commissions **0.83m** · prior Sabam/PlayRight/SIMIM/Reprobel/Auvibel wave retained |
| **E. FOI-ready gaps** | **~1348** drafts ready | Human send only; answered **~9**; partial **~27**; total FOI rows **~1396** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + koepel/NGO/collecting/lobby shells** (**NEW Boerenbond** opbr **EUR26.63m** subsidies **EUR20.84m** · **BIV** lidgeld **EUR10.21m** · **Landelijke Gilden** bruto **EUR3.83m** · **FARO** **EUR2.88m** · **SACD/LaScam/deAuteurs/SOFAM** CMO residual · prior Sabam/PlayRight/SIMIM/Natuurpunt Beheer **EUR505.06m** stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs Fluvius EG possible on DSO holdings.**

### Inventory (tick 1720)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 49884 |
| commitments.csv | 5305 |
| leaderboard.csv | 7506 |
| entities.csv | 1449 |
| sources.csv | 3963 |
| FOI ready | 1348 |
| FOI answered | 9 |
| FOI partial | 27 |
| FOI total rows | 1396 |
| research_queue open | rq_116 deferred + rq_1721 hole-fill after progress |

### What improved since tick 1710

- **Residual dual leftover collecting / steunpunt / institute / lobby wave (tick1711-1719):** **Welzijnszorg** code73 **2.57m** · **SOFAM** commissions **0.83m** · **FARO** werkingsbudget **2.88m** (JV2025 newly live) · **SACD BE** frais nets **2.71m** · **deAuteurs** werkingskost **1.04m** · **LaScam BE** frais nets **1.42m** · **BIV** lidgeld **10.21m** · **Boerenbond** opbr **26.63m** / subsidies **20.84m** · **Landelijke Gilden** bruto **3.83m** — no invented euros.
- **NEW (tick1718+1719):** **Boerenbond** (KBO **0676.461.073**) VL farmers lobby. Official NBB VOL-VZW **2025-00373835**. Opbr **26.630.731** · subsidies **20.844.540** · staff **15.832.262** / **146.3 VTE** · PnL **-922.869**. **Landelijke Gilden** (KBO **0410.028.601**) dual Boerenbond rural assoc. Official NBB VKT-VZW **2026-00263053**. Bruto **3.827.855** · staff **3.641.141** / **35.4 VTE**. FOI ready subsidy/70-73 splits.
- **Dual map themes:** Belgian CMO residual completion (SACD/LaScam/deAuteurs/SOFAM after Sabam/Auvibel/Reprobel/SIMIM/PlayRight) · VL culture steunpunt FARO · federal real-estate institute BIV · VL farmers lobby Boerenbond + Landelijke Gilden dual · prior speerpunt/Oxfam/Natuurpunt retained.
- **Blocked still:** AGB/APB unpublished · Dijk92 CDN **403** · APEFE RA2024 activity-only (no budget euros) · NSZ CDN **403** · Natuurpunt vzw CDN/Northdata opaque.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10. Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **1730**.

"""

prog = base / "progress_every_10_ticks.md"
text = prog.read_text(encoding="utf-8")
marker = "## Snapshot at **tick 1710**"
idx = text.find(marker)
assert idx > 0 and "tick 1720" not in text[idx - 50 : idx + 20]
prog.write_text(text[:idx] + snap + text[idx:], encoding="utf-8")
print("progress ok")

waste = """# DOGE waste ranking — current top 10

**As-of:** tick **1720** (2026-08-23) · **7506** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW leftover 1711-1719 collecting/institute/lobby:** **Boerenbond** opbr **€26.63m** / subsidies **€20.84m** / staff **€15.83m** · **BIV** lidgeld **€10.21m** · **Landelijke Gilden** bruto **€3.83m** · **FARO** **€2.88m** · **SACD BE** frais **€2.71m** · **LaScam BE** frais **€1.42m** · **deAuteurs** **€1.04m** · **SOFAM/Welzijnszorg** · prior **Sabam €29.0m** / PlayRight / SIMIM / Natuurpunt Beheer **€505.06m** stack retained · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 1710:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard: GIP 8.7 · fossil direct 8.55 · fossil accises 8.5 · company cars 8.5 · heatoil 8.43 · cheque 8.4 · CO2 SSC gap 8.4 · OAA reporté 8.4 · BCR reporté 8.4 · dual cars SSC 8.4. **Major NEW residual 1711-1719 (off pure top10 / dual):** CMO completion **SACD/LaScam/deAuteurs/SOFAM** + steunpunt **FARO** + institute **BIV** + lobby **Boerenbond/Landelijke Gilden**. Gain is **Belgian CMO+lobby residual map**. Count NEW since 1710: Welzijnszorg 1711 + SOFAM 1712 + FARO 1713 + SACD 1714 + deAuteurs 1715 + LaScam 1716 + BIV 1717 + Boerenbond 1718 + Landelijke Gilden 1719. **Prior Sabam/PlayRight/SIMIM/Flanders FOOD retained.** Not TE-additive of ~348bn.
"""
(base / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("waste ok")

# research_queue
with open(base / "research_queue.csv", encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
found = False
for row in rows:
    if row["task_id"] == "rq_1720":
        row["status"] = "done"
        row["updated_utc"] = UTC
        row["notes"] = "DONE tick1720 EVERY-10: progress@1720 + waste top10 after residual 1711-1719 (Welzijnszorg SOFAM FARO SACD deAuteurs LaScam BIV Boerenbond LandelijkeGilden); pure top10 stable"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1721",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1721 after 1720 every-10 progress. Next every-10 is 1730. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo LandelijkeGilden/Boerenbond/BIV/LaScam/deAuteurs/SACD/FARO/SOFAM/Welzijnszorg/PlayRight/SIMIM/Reprobel/Auvibel/Sabam/NSZ.... Prefer leftover AGB/APB if PDF live, else NatuurpuntVZW if CDN, NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if budget euros, GO!/POV/BVAS, other IOED/HVZ/IGS.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1720 every-10; NEXT AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE-if-euros/GO!/POV/BVAS/IOED/HVZ/IGS; next every-10 1730",
    }
)
with open(base / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("rq ok")

with open(base / "loop_state.csv", encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
assert len(rows) == 1
rows[0].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1720",
        "ticks_completed": "1720",
        "paused": "no",
        "notes": "tick1720 EVERY-10 progress coverage % + waste top10 after residual 1711-1719 (Welzijnszorg SOFAM FARO SACD deAuteurs LaScam BIV Boerenbond LandelijkeGilden); inventory entities 1449 sources 3963 budgets 49884 commitments 5305 leaderboard 7506 FOI ready 1348; pure top10 stable; next every-10 1730; next rq_1721 AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE/GO!/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill",
    }
)
with open(base / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state ok")

log = Path("docs/doge/loop_log.md")
entry = """
### 2026-08-23T22:45:00Z - tick 1720
- Unit: **rq_1720 EVERY-10** progress coverage % layers A–E + waste top10 after VL residual 1711-1719 (Welzijnszorg · SOFAM · FARO · SACD BE · deAuteurs · LaScam BE · BIV · Boerenbond · Landelijke Gilden). Pure annual top10 re-verified stable. NOT a second municipality fill.
- Found: A/B still **100%**; C ~**99%**; D still **~74-88%** generous of TE (honest: residual dual L5 gains not near-complete of €348bn). FOI ready **~1348**. Major NEW since 1710: Boerenbond opbr **26.63m**/subs **20.84m**; BIV lidgeld **10.21m**; Landelijke Gilden bruto **3.83m**; FARO **2.88m**; SACD/LaScam/deAuteurs/SOFAM CMO residual.
- Wrote: progress_every_10_ticks.md snapshot 1720; doge_waste_top10_current.md as-of 1720; rq_1720=done + rq_1721 spawn; ticks_completed=1720.
- FOI: none new (decade refresh). Human-send backlog unchanged.
- Inventory: entities **1449** · sources **3963** · budgets **49884** · commitments **5305** · leaderboard **7506** · FOI ready **1348** / answered **9** / partial **27** / total **1396**.
- Next: rq_1721 leftover AGB/**Natuurpunt vzw if CDN**/NSZ if CDN 200 / Bosgroep/Dijk92 if JR euros / APEFE if budget euros / GO!/POV / BVAS / IOED / HVZ / IGS / other. Do NOT redo LandelijkeGilden/Boerenbond/BIV/LaScam.... **Next every-10 is 1730**.
"""
t = log.read_text(encoding="utf-8")
if "tick 1720" not in t[-5000:]:
    if not t.endswith("\n"):
        t += "\n"
    log.write_text(t + entry, encoding="utf-8")
    print("log ok")
else:
    print("log already")
print("DONE")

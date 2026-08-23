# tick 1940 — EVERY-10 + RESA YE2025 Medium CW+Upswitch
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-27T17:15:00Z"
csv.field_size_limit(10**7)


def append_csv(path, rows):
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
        for r in rows:
            w.writerow(r)


def update_csv_rows(path, key, updates_by_key):
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
        rows = list(r)
    for row in rows:
        k = row[key]
        if k in updates_by_key:
            row.update(updates_by_key[k])
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


# --- EVERY-10 markdown ---
progress = """# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## How to read the % figures

| Layer | Meaning | “End stop of money”? |
|-------|---------|----------------------|
| **A. L0 total** | Official GG TE known | No — single top line |
| **B. L1 subsector** | TE split federal / SS / state / local | No — still aggregates |
| **C. L2 entity totals** | Named institutions with primary budget totals (De Lijn, FOREM, ORES, …) | **Partial** — who holds the money |
| **D. L5 end-receivers** | Named third party / project / ASBL / firm with € | **Yes** — where possible |
| **E. FOI residual** | Known gap, draft ready for human send | Tracked, not yet answered |

**Honest claim:** A+B are essentially complete. C is large but incomplete. **D is still a small share of €348 bn** — that is structural (payroll, pensions, debt interest, formula grants are not “projects”).

---

## Snapshot at **tick 1940** (2026-08-27)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1931-1940 Interfin/Elia/Fluxys/Enodia/RESA continuum after 1930 Publigas |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1931-1940 is residual dual L5 (not near-complete of 348bn):** **Interfin** equity JUMP **1.25bn** / pnl DROP **83m** · **Elia Group** equity JUMP **5.05bn** / pnl JUMP **175m** · **BNO** omzet **143m** / FTE **1202** · **Fluxys** equity **1.97bn** / pnl JUMP **199m** · **ETB** omzet **1.52bn** / assets **10.45bn** · **Fluxys LNG** assets **830m** / omzet JUMP **237m** · **Pipelink** assets **51m** · **Fluxys c-grid** equity JUMP **10.2m** · **c-grid Antwerp** equity **28.3m** · **Fluxys hydrogen** equity JUMP **25.5m** / assets **96.7m** · **Enodia** equity **1.19bn** / pnl DROP **29.6m** · **RESA** omzet **386m** / assets JUMP **2.25bn** (this tick) |
| **E. FOI-ready gaps** | **~1555** drafts ready | Human send only; answered **~11**; partial **~28**; total FOI rows **~1607** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/property/renewable/energy shells** (**NEW 1931-1940** Interfin · Elia Group · BNO · Fluxys holding · ETB · Fluxys LNG · Pipelink · Fluxys c-grid · c-grid Antwerp · Fluxys hydrogen · Enodia · **RESA** WAL DSO · prior Publi-T/Publigas/Nethys/Virya retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs Fluvius EG / Elia/Fluxys/Publi-T/Publigas/Nethys/Enodia/RESA/ORES path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 1940)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 51691+ |
| commitments.csv | 5603+ |
| leaderboard.csv | 7724+ |
| entities.csv | 1652+ |
| sources.csv | 4635+ |
| FOI ready | 1555 |
| FOI answered | 11 |
| FOI partial | 28 |
| FOI total rows | 1607 |
| research_queue open | rq_1941 after progress |

### What improved since tick 1930

- **Residual dual (tick1931-1940):** **Interfin** · **Elia Group** · **BNO** · **Fluxys** · **ETB** · **Fluxys LNG** · **Pipelink** · **Fluxys c-grid** · **c-grid Antwerp** · **Fluxys hydrogen** · **Enodia** · **RESA** (this tick EVERY-10).
- **Blocked still:** AGB Bornem JR2024-only · Dijk92 YE2025 CDN **403** · FARO NBB YE2025 unpublished (YE2024 filing) · Bosgroep IJzer/Houtland/Limburg YE2025 unpublished · prior Eneco deposit FOI stack.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10 (re-verified; corrupt AGB pi≥12 / OWV snowball stock / Metro3 stock filtered off pure annual). Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **1950**.

## Snapshot at **tick 1930** (2026-08-27)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1921-1930 VEH/Fluvius/Publi-T continuum after 1920 Aspiravi Energy |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1921-1930 is residual dual L5 (not near-complete of 348bn):** **Aspiravi Holding** pnl **57.7m** JUMP / assets **382m** · **VEH** equity **601m** / assets **647m** · **Fluvius SO** omzet **2.90bn** / assets **10.2bn** · **HVZ Meetjesland** ontvangsten **6.76m** Strong · **Socofe** equity **886m** / pnl **64.5m** · **WE Environnement** equity JUMP **157m** / pnl JUMP **11.5m** · **Virya** assets **908m** / LOSS **11.2m** · **Nethys** assets **1.72bn** / equity **1.65bn** · **Publi-T** assets **2.74bn** / pnl JUMP **1.16bn** · **Publigas** assets **1.50bn** / pnl **118m** (this tick) |
| **E. FOI-ready gaps** | **~1543** drafts ready | Human send only; answered **~11**; partial **~28**; total FOI rows **~1595** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/property/renewable shells** (**NEW 1921-1930** Aspiravi Holding · VEH · Fluvius SO · HVZ Meetjesland · Socofe · WE Environnement · Virya Parkwind-parent · Nethys Enodia · **Publi-T** Elia ref · **Publigas** Fluxys majority · prior Parkwind/Elicio/Aspiravi/Norther retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs Fluvius EG / Elia/Fluxys/Publi-T/Publigas/Nethys path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 1930)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 51623+ |
| commitments.csv | 5591+ |
| leaderboard.csv | 7712+ |
| entities.csv | 1641+ |
| sources.csv | 4600+ |
| FOI ready | 1543 |
| FOI answered | 11 |
| FOI partial | 28 |
| FOI total rows | 1595 |
| research_queue open | rq_1931 after progress |

### What improved since tick 1920

- **Residual dual (tick1921-1930):** **Aspiravi Holding** · **VEH** · **Fluvius SO** · **HVZ Meetjesland** · **Socofe** · **WE Environnement** · **Virya** · **Nethys** · **Publi-T** · **Publigas** (this tick EVERY-10).
- **Blocked still:** AGB Bornem JR2024-only · Dijk92 YE2025 CDN **403** · FARO NBB YE2025 unpublished (YE2024 filing) · Bosgroep IJzer/Houtland/Limburg YE2025 unpublished · prior Eneco deposit FOI stack.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10 (re-verified; corrupt AGB pi≥12 / OWV snowball stock / Metro3 stock filtered off pure annual). Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **1940**.
"""
(DATA / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")

waste = """# DOGE waste ranking — current top 10

**As-of:** tick **1940** (2026-08-27) · **7724+** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt AGB pi≥12 anomalies excluded**  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW leftover 1931-1940:** **Elia Group equity JUMP 5.05bn** · **ETB assets 10.45bn** · **Fluxys equity 1.97bn** · **Enodia equity 1.19bn** · **RESA assets JUMP 2.25bn** · **Interfin equity JUMP 1.25bn** · Fluxys LNG/Pipelink/c-grid/hydrogen · BNO · prior Publi-T/Publigas/Nethys/Virya · prior **Eneco continuum** · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 1930:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB pi≥12 / Metro3 stock / OWV snowball stock filtered off). **Major NEW residual 1931-1940 (off pure top10 / dual):** Interfin · Elia Group · BNO · Fluxys · ETB · Fluxys LNG · Pipelink · Fluxys c-grid · c-grid Antwerp · Fluxys hydrogen · Enodia · **RESA**. Count NEW since 1930: 12 residual dual ticks (race dual Enodia+H2 at 1939). **Prior Publi-T/Publigas/Nethys/Virya/Parkwind stack retained.** Not TE-additive of ~348bn.
"""
(DATA / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")

# --- RESA hole-fill ---
sources_new = [
    {
        "source_id": "src_resa_jr2025_cw",
        "title": "Companyweb RESA YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0847027754/resa",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-27",
        "source_class": "secondary_aggregator",
        "notes": "tick1940; neerlegging 18.06.2026; YE 31.12.2025; omzet 386357989 flat +0.65pct; pnl 49287886 +2.15pct; equity 985645160 +3.15pct; bruto 291331454 +6.08pct; FTE 930.6",
    },
    {
        "source_id": "src_resa_jr2025_upswitch",
        "title": "Upswitch RESA YE2025 NBB/CBSO assets EBITDA",
        "url": "https://www.upswitch.app/en/companies/be/resa-0847027754",
        "publisher": "Upswitch (NBB/CBSO-derived)",
        "accessed_date": "2026-08-27",
        "source_class": "secondary_aggregator",
        "notes": "tick1940; YE2025 assets 2247279341 JUMP vs 1954576445 YE2024; equity 985645160; omzet 386357989; EBITDA 146042926; operating result 85026603",
    },
    {
        "source_id": "src_resa_kbo_1940",
        "title": "KBO RESA 0847.027.754 Walloon Liege-area DSO NV",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0847027754",
        "publisher": "KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": "tick1940; Actief NV; Boulevard d Avroy 38 4000 Liege; email officiel.ic-resa@resa.be; web www.resa.be; kapitaal 657880492.30; dual ORES WAL DSO",
    },
]
append_csv(DATA / "sources.csv", sources_new)

budgets_new = [
    {"budget_id": "bud_resa_omzet_jr2025", "entity_id": "resa", "year": "2025", "amount_eur": "386357989", "amount_min_eur": "", "amount_max_eur": "", "basis": "CW NBB-derived omzet", "source_id": "src_resa_jr2025_cw", "confidence": "medium", "notes": "tick1940; YE2025 omzet 386357989 flat +0.65pct"},
    {"budget_id": "bud_resa_pnl_jr2025", "entity_id": "resa", "year": "2025", "amount_eur": "49287886", "amount_min_eur": "", "amount_max_eur": "", "basis": "CW NBB-derived 9904", "source_id": "src_resa_jr2025_cw", "confidence": "medium", "notes": "tick1940; YE2025 pnl 49287886 +2.15pct"},
    {"budget_id": "bud_resa_equity_jr2025", "entity_id": "resa", "year": "2025", "amount_eur": "985645160", "amount_min_eur": "", "amount_max_eur": "", "basis": "CW/Upswitch NBB-derived 10/15", "source_id": "src_resa_jr2025_cw", "confidence": "medium", "notes": "tick1940; YE2025 equity 985645160 +3.15pct"},
    {"budget_id": "bud_resa_bruto_jr2025", "entity_id": "resa", "year": "2025", "amount_eur": "291331454", "amount_min_eur": "", "amount_max_eur": "", "basis": "CW NBB-derived 9900", "source_id": "src_resa_jr2025_cw", "confidence": "medium", "notes": "tick1940; YE2025 bruto 291331454 +6.08pct"},
    {"budget_id": "bud_resa_assets_jr2025", "entity_id": "resa", "year": "2025", "amount_eur": "2247279341", "amount_min_eur": "", "amount_max_eur": "", "basis": "Upswitch NBB/CBSO assets", "source_id": "src_resa_jr2025_upswitch", "confidence": "medium", "notes": "tick1940; YE2025 assets 2247279341 JUMP vs 1.95bn YE2024"},
    {"budget_id": "bud_resa_ebitda_jr2025", "entity_id": "resa", "year": "2025", "amount_eur": "146042926", "amount_min_eur": "", "amount_max_eur": "", "basis": "Upswitch NBB/CBSO EBITDA", "source_id": "src_resa_jr2025_upswitch", "confidence": "medium", "notes": "tick1940; YE2025 EBITDA 146042926"},
    {"budget_id": "bud_resa_opresult_jr2025", "entity_id": "resa", "year": "2025", "amount_eur": "85026603", "amount_min_eur": "", "amount_max_eur": "", "basis": "Upswitch NBB/CBSO operating result", "source_id": "src_resa_jr2025_upswitch", "confidence": "medium", "notes": "tick1940; YE2025 operating result 85026603"},
    {"budget_id": "bud_resa_fte_jr2025", "entity_id": "resa", "year": "2025", "amount_eur": "931", "amount_min_eur": "", "amount_max_eur": "", "basis": "CW NBB-derived FTE 930.6", "source_id": "src_resa_jr2025_cw", "confidence": "medium", "notes": "tick1940; YE2025 FTE 930.6 (stored 931)"},
]
append_csv(DATA / "budgets.csv", budgets_new)

comm = {
    "commitment_id": "comm_resa_jr2025_assets",
    "title": "RESA YE2025 leftover Walloon Liege-area DSO dual (assets JUMP 2.25bn / omzet 386m / equity 986m)",
    "entity_id": "resa",
    "beneficiary": "Liege-area municipalities / electricity+gas consumers / CWaPE regulated users",
    "legal_basis": "WVV NV; NBB neerlegging; CWaPE tariff methodology; Bestuursdecreet / openbaarheid; Walloon DSO dual ORES",
    "decision_date": "2026-06-18",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "2247279341",
    "cash_by_year": "2025:omzet=386357989;pnl=49287886;equity=985645160;bruto=291331454;assets=2247279341;ebitda=146042926;op=85026603;fte=930.6;kapitaal=657880492",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0847027754/resa",
    "stated_goal": "Liege-area electricity and gas distribution (Walloon DSO dual ORES)",
    "cut_option": "FOI NBB PDF + debt/RAB / municipal share % / dual unit-cost vs ORES",
    "source_id": "src_resa_jr2025_cw",
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Liege>RESA>JR2025_L5",
    "notes": "tick1940 EVERY-10; Medium CW+Upswitch; preferred AGB Bornem JR2024 / Dijk92 CDN 403 / FARO YE2024; do not redo BNO/Fluxys chain/ETB/Elia Group/Pipelink/Enodia/Nethys; NON-Eneco; double-count vs ORES/Sibelga/Fluvius/2024 RESA path possible",
}
append_csv(DATA / "commitments.csv", [comm])

lb = {
    "item_id": "lb_resa_assets_jump_2_25bn_omzet_386m_jr2025",
    "name": "RESA assets JUMP 2.25bn / omzet 386m / equity 986m (Walloon Liege DSO YE2025)",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Wallonie>Liege>RESA>JR2025_L5",
    "annual_cost_eur": "386357989",
    "total_cost_eur": "2247279341",
    "tco_notes": "omzet 386357989 flat pnl 49287886 equity 985645160 bruto 291331454 assets 2247279341 JUMP ebitda 146042926 op 85026603 FTE 930.6; NBB PDF unresolved",
    "confidence": "medium",
    "source_id": "src_resa_jr2025_cw",
    "beneficiaries": "Liege-area municipalities / elec+gas consumers",
    "stated_goal": "Regulated Walloon Liege-area electricity and gas DSO",
    "measured_outcome": "Assets JUMP to 2.25bn with flat 386m omzet; dual ORES opacity; NBB PDF unresolved",
    "absurdity_score": "5.5",
    "cost_score": "8.5",
    "difficulty": "3.5",
    "priority_index": "6.7",
    "cut_proposal": "Publish NBB PDF + debt/RAB + municipal share % + dual unit-cost vs ORES",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1940 EVERY-10; Medium CW+Upswitch; leftover after Enodia/Fluxys-H2; not TE-additive; NON-Eneco; double-count vs ORES/2024 RESA possible",
}
append_csv(DATA / "leaderboard.csv", [lb])

# update existing resa entity
update_csv_rows(
    DATA / "entities.csv",
    "entity_id",
    {
        "resa": {
            "foi_email": "officiel.ic-resa@resa.be",
            "foi_postal": "Boulevard d'Avroy 38 4000 Liège",
            "website": "https://www.resa.be",
            "notes": (
                "Walloon DSO residual vs ORES; CA 384m net 48m dividend 18.8m 2024; dual ORES Fluvius Sibelga; tick174; "
                "tick1940 YE2025 Medium CW+Upswitch KBO 0847.027.754 Actief NV; omzet 386.4m pnl 49.3m equity 985.6m "
                "assets JUMP 2.25bn bruto 291.3m EBITDA 146.0m op 85.0m FTE 930.6 kapitaal 657.9m; NBB PDF FOI"
            ),
        }
    },
)

foi = {
    "gap_id": "gap_resa_nbb_pdf_debt_rab_share_l5",
    "hierarchy_path": "Wallonie>Liege>RESA>nbb_debt_rab_share_L5",
    "entity_id": "resa",
    "what_is_missing": "NBB deposit id + full JR2025 PDF (debt/cash/RAB exact; VTE detail); aandeelhouders % (gemeenten / Enodia path); tariff/RAB path explaining assets JUMP to 2.25bn with flat omzet 386m; dual unit-cost recon vs ORES; related-party flows",
    "why_it_matters": "Walloon Liege-area DSO — 2.25bn assets JUMP / 386m omzet hides municipal grid money after Enodia/Nethys mined; dual ORES opacity",
    "priority": "8",
    "recipient_body": "RESA SA",
    "recipient_email": "officiel.ic-resa@resa.be",
    "recipient_postal": "Boulevard d'Avroy 38 4000 Liège (cc Enodia / CWaPE)",
    "draft_letter_path": "docs/doge/foi/drafts/gap_resa_nbb_pdf_debt_rab_share_l5.md",
    "status": "ready",
    "date_ready": "2026-08-27",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_resa_jr2025_assets",
    "linked_leaderboard_id": "lb_resa_assets_jump_2_25bn_omzet_386m_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1940 EVERY-10; human-send only; Medium CW+Upswitch; AGB Bornem JR2024; Dijk92 CDN 403; FARO YE2024; next every-10 1950",
}
append_csv(DATA / "foi_queue.csv", [foi])

update_csv_rows(
    DATA / "research_queue.csv",
    "task_id",
    {
        "rq_1940": {
            "status": "done",
            "entity_id": "resa",
            "instructions": (
                "Completed EVERY-10 + RESA SA leftover Walloon Liege DSO dual after Enodia/Fluxys-H2; "
                "KBO 0847.027.754 Actief NV; YE2025 Medium CW+Upswitch; sourced euros omzet 386357989 pnl 49287886 "
                "equity 985645160 assets 2247279341 JUMP ebitda 146042926 op 85026603 bruto 291331454 FTE 930.6; "
                "FOI ready gap_resa_nbb_pdf_debt_rab_share_l5; NOT BNO / Fluxys chain / ETB / Elia Group / Pipelink / Enodia / Nethys"
            ),
            "blocked_gap_id": "gap_resa_nbb_pdf_debt_rab_share_l5",
            "updated_utc": TS,
            "notes": (
                "tick1940 EVERY-10 + RESA leftover; KBO 0847.027.754; YE2025 Medium CW+Upswitch "
                "(omzet 386m assets JUMP 2.25bn equity 986m pnl 49.3m); FOI ready not sent; AGB Bornem JR2024; "
                "Dijk92 CDN 403; FARO YE2024; next rq_1941; next every-10 1950"
            ),
        }
    },
)

rq1941 = {
    "task_id": "rq_1941",
    "title": "Leftover dual residual hole-fill after RESA EVERY-10 (AGB/Dijk92-if-200 / FARO-if-YE2025 / otherHVZ-IGS-if-live)",
    "sprint": "hole_fill",
    "priority": "8",
    "status": "open",
    "hierarchy_target": "Vlaanderen>leftover_dual",
    "entity_id": "",
    "instructions": (
        "Tick 1941 after 1940 RESA EVERY-10. Prefer leftover AGB/APB if PDF live, else Dijk92 if CDN 200, else FARO if "
        "TRUE NBB YE2025, else Fluxys Belgium statutory / other HVZ/IGS if unused live YE2025 euros. Do NOT redo BNO, "
        "Fluxys holding/LNG/c-grid/c-grid Antwerp/hydrogen, ETB, Elia Group, Pipelink, Enodia, Nethys, RESA."
    ),
    "blocked_gap_id": "",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "spawned after tick1940 EVERY-10; next every-10 1950",
}
append_csv(DATA / "research_queue.csv", [rq1941])

with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
        lineterminator="\n",
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": TS,
            "last_unit_id": "rq_1940",
            "ticks_completed": "1940",
            "paused": "no",
            "notes": (
                "tick1940 EVERY-10 + leftover RESA 0847.027.754 Medium CW+Upswitch (omzet 386m assets JUMP 2.25bn "
                "equity 986m pnl 49.3m EBITDA 146m FTE 931); NBB PDF+debt/RAB FOI; AGB Bornem JR2024; Dijk92 CDN 403; "
                "FARO YE2024; next rq_1941; next every-10 1950; continuous hole_fill"
            ),
        }
    )

log_block = """

## Tick 1940 - 2026-08-27T17:15:00Z - EVERY-10 + rq_1940 RESA (assets JUMP 2.25bn / omzet 386m / Medium)

- Unit: **rq_1940** EVERY-10 after Enodia/Fluxys-H2 race at 1939. Refreshed **progress_every_10_ticks.md** (tick 1940 snapshot) + **doge_waste_top10_current.md** (top10 stable GIP/fossil/cars/cheque/reporté). Prefer NON-Eneco live hole-fill: AGB Bornem still JR2024; Dijk92 CDN **403**; FARO YE2024. Took leftover **RESA SA** (KBO **0847.027.754**; Boulevard d'Avroy 38 Liège; Walloon Liege-area DSO dual ORES; only YE2024 mined at tick174; NON-Eneco). Do not redo BNO/Fluxys chain/ETB/Elia Group/Pipelink/Enodia/Nethys.
- Primary hunt: NBB deposit PDF unresolved this tick. **Medium** euros from [Companyweb](https://www.companyweb.be/nl/0847027754/resa) + [Upswitch NBB/CBSO](https://www.upswitch.app/en/companies/be/resa-0847027754) + KBO (neerlegging **18.06.2026**; YE **31.12.2025**; kapitaal **EUR657,880,492**): omzet **EUR386,357,989** (flat **+0.65%**); bruto **EUR291,331,454** (**JUMP +6.08%**); PnL **EUR49,287,886** (**+2.15%**); equity **EUR985,645,160** (**+3.15%**); assets **EUR2,247,279,341** (**JUMP** vs 1.95bn YE2024); EBITDA **EUR146,042,926**; operating result **EUR85,026,603**; FTE **930.6**.
- Wrote: progress+waste markdown; sources (+3); budgets (+8); commitments (+1); leaderboard (+1); entities (updated resa); foi + draft gap_resa_nbb_pdf_debt_rab_share_l5; rq_1940=done + rq_1941 open; loop_state ticks=1940.
- FOI opened: NBB PDF + debt/RAB / municipal share % (**ready**, human-send only).
- **EVERY-10 DONE.** Next every-10 is **1950**. Next: rq_1941 (AGB/Dijk92-if-200 / FARO-if-YE2025 / FluxysBelgium-statutory-otherHVZ).
"""
with (ROOT / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1940 write OK")

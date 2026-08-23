# ephemeral tick2030 — EVERY-10 + WZC Sint-Jozef Rillaar/Aarschot YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T12:20:00Z"
ENTITY = "vzw_wzc_sint_jozef_rillaar"
GAP = "gap_wzc_sint_jozef_rillaar_nbb_pdf_assets_debt_matrix_l5"
SRC = "src_wzc_sint_jozef_rillaar_jr2025_cw"
SRC_EN = "src_wzc_sint_jozef_rillaar_jr2025_cw_en"
SRC_FR = "src_wzc_sint_jozef_rillaar_jr2025_cw_fr"
SRC_KBO = "src_wzc_sint_jozef_rillaar_kbo_2025"
SRC_SITE = "src_wzc_sint_jozef_rillaar_site_2025"

OMZET = "10734847"
PNL = "952540"
EQUITY = "13630949"
BRUTO = "11332671"
FTE = "129.6"
OMZET24 = "10331464"
PNL24 = "969193"
EQUITY24 = "12738863"
BRUTO24 = "10939769"


def load(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows, list(rows[0].keys()) if rows else []


def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2030")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

for x in qrows:
    if x.get("task_id") == "rq_2030":
        x["status"] = "in_progress"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
save("docs/doge/data/research_queue.csv", qrows, qfields)

# --- EVERY-10 progress ---
Path("docs/doge/data/progress_every_10_ticks.md").write_text(
    """# DOGE progress — every 10 ticks

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

## Snapshot at **tick 2030** (2026-08-24)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2021-2030 WZC/psych continuum after 2020 PC Sint-Hiëronymus |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2021-2030 is residual dual L5 (not near-complete of 348bn):** **WZC Sint-Vincentius Avelgem** omzet JUMP **7.49m** · **PPC Pittem** omzet JUMP **42.45m** · **Maria Rustoord Ingelmunster** omzet JUMP **11.64m** · **Evara** omzet JUMP **443.17m** · **Sint Carolus Mayerhof** omzet DROP **11.46m** · **WZC Zilverbos** omzet JUMP **7.85m** · **WZC Sint-Carolus Ternat** omzet JUMP **10.16m** · **WZC De Foyer Gent** omzet JUMP **19.03m** · **Karus** omzet JUMP **70.08m** · **WZC Sint-Jozef Rillaar** omzet JUMP **10.73m** Medium (this tick EVERY-10 dual) |
| **E. FOI-ready gaps** | **~1647** drafts ready | Human send only; answered **~11**; partial **~28**; total FOI rows **~1699** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/property/renewable/energy/nuclear/water/forest/hospital/psych shells** (**NEW 2021-2030** Vincentius Avelgem · PPC Pittem · Maria Rustoord · Evara · Mayerhof · Zilverbos · Ternat · De Foyer · Karus · **Sint-Jozef Rillaar** · prior PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/hospital stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2030)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 52211 |
| commitments.csv | 5696 |
| leaderboard.csv | 7817 |
| entities.csv | 1732 |
| sources.csv | 5034 |
| FOI ready | 1647 |
| FOI answered | 11 |
| FOI partial | 28 |
| FOI total rows | 1699 |
| research_queue open | rq_2031 after progress |

### What improved since tick 2020

- **Residual dual (tick2021-2030):** **WZC Sint-Vincentius Avelgem** · **PPC Pittem** · **Maria Rustoord Ingelmunster** · **Evara** · **Sint Carolus Mayerhof** · **WZC Zilverbos Zelzate** · **WZC Sint-Carolus Ternat** · **WZC De Foyer Gent** · **Karus** · **WZC Sint-Jozef Rillaar** (this tick EVERY-10 dual — Vlaams-Brabant WZC VZW YE2025 Medium CW).
- **Blocked still:** AGB Bornem JR2024-only · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH 0201.712.587 / REW YE2024-only · Jessa/ZOL CW N/A omzet · Bethanie Zoersel Emmaüs double-count · Veilige Have / Zusterhof already mined · prior Eneco deposit FOI stack.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10 (re-verified; corrupt AGB pi>10 / OWV snowball stock / Metro3 stock filtered off pure annual). Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **2040**.


## Snapshot at **tick 2020** (2026-08-24)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2011-2020 hospital/WZC/psych continuum after 2010 Vlaamse Zorgkas |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2011-2020 is residual dual L5 (not near-complete of 348bn):** prior hospital/WZC/psych continuum incl. **PC Sint-Hiëronymus** |
| **E. FOI-ready gaps** | **~1637** drafts ready | Human send only; answered **~11**; partial **~28**; total FOI rows **~1689** |

See prior snapshots below / git history for tick 2010 detail.
""",
    encoding="utf-8",
)
print("progress refreshed")

Path("docs/doge/data/doge_waste_top10_current.md").write_text(
    """# DOGE waste ranking — current top 10

**As-of:** tick **2030** (2026-08-24) · **7817** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt AGB / scoring anomalies with pi>10 excluded**  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW residual 2021-2030:** **Evara omzet 443.17m** · **Karus omzet 70.08m** · **PPC Pittem omzet 42.45m** · **WZC De Foyer omzet 19.03m** · **WZC Sint-Jozef Rillaar omzet 10.73m** · **Ternat / Mayerhof / Zilverbos / Maria Rustoord / Vincentius** · prior HH Lier/AZ Rivierenland/Sint-Trudo/hospital/psych stack retained · prior nuclear/Fluxys/Elia/Enodia/RESA · prior Eneco continuum · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2020:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off). **Major NEW residual 2021-2030 (off pure top10 / dual):** Evara · Karus · PPC Pittem · De Foyer · Ternat · Mayerhof · Zilverbos · Maria Rustoord · Vincentius Avelgem · **Sint-Jozef Rillaar** (EVERY-10 dual). Count NEW since 2020: 10 residual dual ticks. **Prior PC Sint-Hiëronymus/hospital stack retained.** Not TE-additive of ~348bn.
""",
    encoding="utf-8",
)
print("top10 refreshed")

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC Sint-Jozef Rillaar/Aarschot YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0413055989/woon-en-zorgcentrum-sint-jozef",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2030; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 13.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2030/sj_aarschot_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Sint-Jozef Rillaar/Aarschot YE2025 statutory",
        "url": "https://www.companyweb.be/en/0413055989/woon-en-zorgcentrum-sint-jozef",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2030; EN mirror YE2025 Medium; filed 13-07-2026; Last balance sheet year 2025; FTE 129.6; raw docs/doge/data/raw/tick2030/sint_jozef_aarschot_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC Sint-Jozef Rillaar/Aarschot YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0413055989/woon-en-zorgcentrum-sint-jozef",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2030; FR mirror YE2025 Medium; déposés le 13-07-2026; raw docs/doge/data/raw/tick2030/sj_aarschot_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Woon- en zorgcentrum Sint-Jozef 0413.055.989 Actief VZW",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413055989",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2030; Actief VZW; Diestsesteenweg 488 3202 Aarschot; 1 VE; sinds 22.02.1973; raw docs/doge/data/raw/tick2030/sj_aarschot_kbo.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "sintjozefrillaar.be WZC Sint-Jozef Rillaar",
        "url": "https://www.sintjozefrillaar.be/",
        "publisher": "WZC Sint-Jozef Rillaar",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2030; info@sintjozefrillaar.be; +32 16 50 91 91; Diestsesteenweg 488 Rillaar/Aarschot",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_wzc_sint_jozef_rillaar_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2030; omzet JUMP {OMZET} +3.90pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_wzc_sint_jozef_rillaar_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2030; pnl DROP {PNL} -1.72pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_wzc_sint_jozef_rillaar_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2030; equity JUMP {EQUITY} +7.00pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_wzc_sint_jozef_rillaar_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2030; bruto JUMP {BRUTO} +3.59pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_wzc_sint_jozef_rillaar_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2030; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_wzc_sint_jozef_rillaar_jr2025_statutory",
    "title": "WZC Sint-Jozef Rillaar YE2025 leftover dual (omzet JUMP 10.73m / pnl DROP 0.95m / equity JUMP 13.63m)",
    "entity_id": ENTITY,
    "beneficiary": "Aarschot-Rillaar elderly via Woon- en zorgcentrum Sint-Jozef VZW",
    "legal_basis": "VZW/ASBL woonzorgcentrum (KBO 0413.055.989)",
    "decision_date": "2026-07-13",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0413055989/woon-en-zorgcentrum-sint-jozef",
    "stated_goal": "Residential elderly care / WZC Rillaar-Aarschot",
    "cut_option": "Publish NBB PDF assets/debt FOI; map public subsidies vs resident fees",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "VlaamsBrabant>Aarschot>WZC_Sint_Jozef_Rillaar>JR2025_statutory_L5",
    "notes": "tick2030 EVERY-10 dual; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Veilige Have/Zusterhof already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_wzc_sint_jozef_rillaar_omzet_jump_10_73m_pnl_drop_0_95m_jr2025",
    "name": "WZC Sint-Jozef Rillaar omzet JUMP 10.73m / pnl DROP 0.95m / equity JUMP 13.63m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "VlaamsBrabant>Aarschot>WZC_Sint_Jozef_Rillaar>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Aarschot-Rillaar elderly via WZC Sint-Jozef VZW",
    "stated_goal": "Residential elderly care",
    "measured_outcome": "Medium CW YE2025; 10.73m omzet JUMP +3.90pct with equity JUMP +7.00pct; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "5.0",
    "difficulty": "4.0",
    "priority_index": "5.1",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map public subsidy vs resident-fee mix",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2030 EVERY-10 leftover WZC dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2040",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woon- en zorgcentrum Sint-Jozef (Rillaar/Aarschot)",
    "name_fr": "Woon- en zorgcentrum Sint-Jozef (maison de repos Rillaar)",
    "name_en": "Woon- en zorgcentrum Sint-Jozef (nursing home Rillaar/Aarschot)",
    "level": "asbl",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.sintjozefrillaar.be/",
    "foi_email": "info@sintjozefrillaar.be",
    "foi_postal": "Diestsesteenweg 488, 3202 Aarschot",
    "notes": "tick2030 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0413.055.989 Actief VZW; omzet JUMP 10.73m pnl DROP 0.95m equity JUMP 13.63m bruto JUMP 11.33m FTE 129.6; assets/debt Unknown; neerlegging 13.07.2026; 1 VE; NOT Rumst Sint-Jozef; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Veilige Have/Zusterhof already mined; do not redo Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hiëronymus",
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
else:
    for x in erows:
        if x.get("entity_id") == ENTITY:
            x.update({k: v for k, v in ne.items() if v})
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "VlaamsBrabant>Aarschot>WZC_Sint_Jozef_Rillaar>NBB_PDF_assets_debt",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split",
    "why_it_matters": "Medium CW shows 10.73m omzet WZC with equity JUMP without balance sheet or public/private revenue mix",
    "priority": "7",
    "recipient_body": "Woon- en zorgcentrum Sint-Jozef VZW Rillaar",
    "recipient_email": "info@sintjozefrillaar.be",
    "recipient_postal": "Diestsesteenweg 488, 3202 Aarschot",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_wzc_sint_jozef_rillaar_jr2025_statutory",
    "linked_leaderboard_id": "lb_wzc_sint_jozef_rillaar_omzet_jump_10_73m_pnl_drop_0_95m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2030 EVERY-10; human-send only; Medium CW; next every-10 2040",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC Sint-Jozef Rillaar (NBB PDF / assets-debt)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woon- en zorgcentrum Sint-Jozef VZW Rillaar — KBO **0413.055.989**  
**recipient:** info@sintjozefrillaar.be · Diestsesteenweg 488, 3202 Aarschot  
**sources:** [CW NL](https://www.companyweb.be/nl/0413055989/woon-en-zorgcentrum-sint-jozef) · [CW EN](https://www.companyweb.be/en/0413055989/woon-en-zorgcentrum-sint-jozef) · [CW FR](https://www.companyweb.be/fr/0413055989/woon-en-zorgcentrum-sint-jozef) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413055989) · [sintjozefrillaar.be](https://www.sintjozefrillaar.be/)  
**tick:** 2030  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **13.07.2026**): omzet **EUR10,734,847** JUMP +3.90%; pnl **EUR952,540** DROP -1.72%; equity **EUR13,630,949** JUMP +7.00%; bruto **EUR11,332,671** JUMP +3.59%; FTE **129.6**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Skipped already-mined Veilige Have / Zusterhof; Bethanie Zoersel Emmaüs double-count.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woon- en zorgcentrum Sint-Jozef VZW — Diestsesteenweg 488, 3202 Aarschot
info@sintjozefrillaar.be
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC Sint-Jozef Rillaar (KBO 0413.055.989)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 13.07.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs bewonersbijdragen 2025.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

skip_list = (
    "Do NOT redo WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, "
    "Evara/Multiversum, Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, "
    "PC Gent-Sleidinge, Veilige Have, Zusterhof, Bethanie Zoersel (Emmaüs double-count), AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, "
    "Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, "
    "Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS. "
    "Jessa/ZOL/Vesalius CW N/A omzet — take only if figures appear."
)

qrows, qfields = load("docs/doge/data/research_queue.csv")
for x in qrows:
    if x.get("task_id") == "rq_2030":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "EVERY-10 + leftover dual after Karus — WZC Sint-Jozef Rillaar YE2025 Medium"
        x["notes"] = (
            "tick2030 EVERY-10 + WZC Sint-Jozef Rillaar Medium omzet JUMP 10.73m pnl DROP 0.95m equity JUMP 13.63m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2031; next every-10 2040"
        )
        x["instructions"] = (
            "Completed EVERY-10 + leftover WZC Sint-Jozef Rillaar YE2025 Medium CW; KBO 0413.055.989; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2031" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2031",
            "title": "leftover dual hole-fill after WZC Sint-Jozef Rillaar",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2030 after EVERY-10 + WZC Sint-Jozef Rillaar YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (Cassiers / Sint-Bernardus Assenede / OLV Roosdaal / "
                "other unused YE2025 if live with omzet). "
                + skip_list
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2030 EVERY-10 + Sint-Jozef Rillaar; next every-10 2040",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue updated")

srows2, sfields2 = load("docs/doge/data/loop_state.csv")
for x in srows2:
    if x.get("state_id") == "main":
        x["mode"] = "continuous"
        x["current_sprint"] = "hole_fill"
        x["last_tick_utc"] = UTC
        x["last_unit_id"] = "rq_2030"
        x["ticks_completed"] = "2030"
        x["paused"] = "no"
        x["notes"] = (
            "tick2030 EVERY-10 + leftover WZC Sint-Jozef Rillaar 0413.055.989 Medium CW (omzet JUMP 10.73m pnl DROP 0.95m "
            "equity JUMP 13.63m bruto JUMP 11.33m FTE 129.6; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "next rq_2031; next every-10 2040; continuous hole_fill"
        )
save("docs/doge/data/loop_state.csv", srows2, sfields2)
print("loop_state updated")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2030 - {UTC} - rq_2030 EVERY-10 + WZC Sint-Jozef Rillaar (omzet JUMP 10.73m / pnl DROP 0.95m / Medium)

- Unit: **rq_2030** EVERY-10 mandatory + leftover dual after **rq_2029 Karus**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Skipped already-mined Veilige Have / Zusterhof; Bethanie Zoersel Emmaüs double-count. Took unused leftover **WZC Sint-Jozef Rillaar** YE2025 (KBO **0413.055.989**; Diestsesteenweg 488 Aarschot; Vlaams-Brabant **WZC VZW**). Do not redo Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hiëronymus.
- EVERY-10: refreshed **progress_every_10_ticks.md** (tick 2030 snapshot; residual dual 2021-2030) + **doge_waste_top10_current.md** (pure annual top10 stable GIP/fossil/cars/cheque/reporté; NEW residual dual off-top10).
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR10,734,847** JUMP +3.90%; pnl **EUR952,540** DROP -1.72%; equity **EUR13,630,949** JUMP +7.00%; bruto **EUR11,332,671** JUMP +3.59%; FTE **129.6**; neerlegging **13.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@sintjozefrillaar.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_wzc_sint_jozef_rillaar); foi + draft gap_wzc_sint_jozef_rillaar_nbb_pdf_assets_debt_matrix_l5; progress+top10; rq_2030=done + rq_2031 open; loop_state ticks=2030; raw under docs/doge/data/raw/tick2030/.
- FOI: **ready not sent** (human-gated; info@sintjozefrillaar.be).
- EVERY-10 done. Next every-10 **2040**. Next: rq_2031 (AGB/FARO-if-YE2025 / AIESH-REW / Cassiers-Bernardus-OLV Roosdaal / unused DSO-IGS-HVZ).

### Every-10 brief (A/B/C/D/E)
- **A** L0 TE: **100%** (EUR347.956bn Strong)
- **B** L1 subsectors: **100%** unconsol map
- **C** L2 entities: **~99%** order-of-magnitude
- **D** L5 end-receivers: **~74-88%** generous; +10 residual dual 2021-2030 (WZC/psych) - **not** near-complete of 348bn
- **E** FOI-ready: **~1647** drafts; answered ~11; partial ~28
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("log appended")
print("DONE tick2030")

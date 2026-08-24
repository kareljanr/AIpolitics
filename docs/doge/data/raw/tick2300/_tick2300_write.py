# tick2300 EVERY-10 + leftover dual De Kiem Gavere YE2025 Medium
from pathlib import Path
import csv
import json
from collections import Counter

csv.field_size_limit(10_000_000)
root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"
raw = data / "raw" / "tick2300"
raw.mkdir(parents=True, exist_ok=True)

TICK = "2300"
UTC = "2026-08-27T17:45:00Z"
ENTITY = "vzw_de_kiem_gavere"
KBO = "0445.151.311"
KBO_DIGITS = "0445151311"

OMZET = 5126323
BRUTO = 6820218
PNL = 173737
EQUITY = 2545514
FTE = 66.9
OMZET_2024 = 4751364
BRUTO_2024 = 6149206
PNL_2024 = 353491
EQUITY_2024 = 2372191
FTE_2024 = 62.9
RATIO = round(BRUTO / OMZET, 2)  # 1.33

GAP = "gap_kiem_nbb_pdf_assets_debt_bruto_gt_omzet_1_33x_pnl_drop_fte_jump_matrix_l5"
LB = "lb_kiem_bruto_6_82m_omzet_5_13m_1_33x_pnl_drop_fte_jump_jr2025"
COMM = "comm_kiem_jr2025_statutory_addiction_care_bruto_6_82m_1_33x"
RQ = "rq_2300"
RQ_NEXT = "rq_2301"

SRC_EN = "src_kiem_jr2025_cw_en"
SRC_NL = "src_kiem_jr2025_cw_nl"
SRC_KBO = "src_kiem_kbo_0445151311"
SRC_SITE = "src_kiem_site_contact_2300"
SRC_NBB = "src_kiem_nbb_consult_0445151311"

ABS, COST, DIFF = 5.2, 5.5, 3.0
PI = round((ABS + COST) / 2, 2)  # 5.35


def append_csv(path: Path, rows: list[dict], id_key: str):
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        existing = list(reader)
    have = {r.get(id_key) for r in existing}
    new = [r for r in rows if r.get(id_key) not in have]
    if not new:
        print(path.name, "already")
        return
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        for r in new:
            w.writerow({k: r.get(k, "") for k in fieldnames})
    print(path.name, "+", len(new))


def count_rows(name: str) -> int:
    with (data / name).open(encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


def foi_stats():
    c = Counter()
    with (data / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            st = (r.get("status") or "").strip().lower()
            if st in {"ready", "answered", "partial", "draft", "sent", "superseded", "cancelled"}:
                c[st] += 1
    return c


# --- inventory for every-10 ---
inv = {
    "budgets": count_rows("budgets.csv"),
    "commitments": count_rows("commitments.csv"),
    "leaderboard": count_rows("leaderboard.csv"),
    "entities": count_rows("entities.csv"),
    "sources": count_rows("sources.csv"),
    "foi_total": count_rows("foi_queue.csv"),
}
foi = foi_stats()
ready = foi.get("ready", 1971)
answered = foi.get("answered", 11)
partial = foi.get("partial", 28)

progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2300** (2026-08-27)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2291-2300 continuum; AGB Bornem / FARO / AIESH / Citeco / Groupe Foes still YE2024 stalls; **REW unlocked YE2025@2289**; Gandae still YE2024 |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2291-2300 is residual dual L5 (not near-complete of 348bn):** Intro Schoonmaak · Labor · NLZ · Mo-Clean · Rozemarijn · Ryhove · SOBO · De Stobbe / De Okkernoot · JOMI · EVERY-10 primary **De Kiem** bruto **6.82m** / omzet **5.13m** ~1.33x / pnl DROP / FTE **66.9** (Medium CW) |
| **E. FOI-ready gaps** | **~{ready}** drafts ready | Human send only; answered **~{answered}**; partial **~{partial}**; total FOI rows **~{inv['foi_total']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability/maatwerk/addiction-care shells** (**NEW 2291-2300** Intro Schoonmaak · Labor · NLZ · Mo-Clean · Rozemarijn · Ryhove · SOBO · De Stobbe · De Okkernoot · JOMI · **De Kiem** · prior 2281-2290 REW/Op Maat/Buseloc stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2300)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {inv['budgets']}+ |
| commitments.csv | {inv['commitments']}+ |
| leaderboard.csv | {inv['leaderboard']}+ |
| entities.csv | {inv['entities']}+ |
| sources.csv | {inv['sources']}+ |
| FOI ready | ~{ready} |
| FOI answered | {answered} |
| FOI partial | {partial} |
| FOI total rows | ~{inv['foi_total']} |
| research_queue open | rq_2301 after De Kiem EVERY-10 (+ rq_116 deferred Q4) |

### What improved since tick 2290

- **Residual dual (tick2291-2300):** **Intro Schoonmaak** · **Labor** · **NLZ** · **Mo-Clean** · **Rozemarijn** (~7.0x) · **Ryhove** (~2.2x) · **SOBO** · **De Stobbe** / **De Okkernoot** (~5.4x VAPH) · **JOMI** · EVERY-10 primary **De Kiem** (bruto **6.82m** / omzet **5.13m** ~**1.33x** / pnl DROP **-51%** / FTE **66.9**; Medium CW; FOI ready; Flemish addiction residential care).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024) · AIESH YE2024-only · Citeco / Groupe Foes / Aralea / Manupal / De Ploeg / Vlotter YE2024 · Gandae YE2024 · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs FOI-ready.
"""
(data / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")
print("progress refreshed")

waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **2300** (2026-08-27) · **{inv['leaderboard']}+** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2291-2300:** **De Kiem bruto 6.82m / omzet 5.13m ~1.33x / pnl DROP / FTE 66.9** (EVERY-10@2300 primary) · JOMI · De Okkernoot (~5.4x) · De Stobbe · SOBO · Ryhove (~2.2x) · Rozemarijn (~7.0x) · Mo-Clean · NLZ · Labor · Intro Schoonmaak · prior 2281-2290 REW/Op Maat/Buseloc stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia/Enodia · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2290:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2291-2300 (off pure top10 / dual):** Intro Schoonmaak · Labor · NLZ · Mo-Clean · Rozemarijn · Ryhove · SOBO · De Stobbe · De Okkernoot · JOMI · **De Kiem bruto 6.82m / omzet 5.13m ~1.33x / pnl DROP / FTE 66.9** (EVERY-10@2300 primary). Count NEW since 2290: ~11 residual dual fills. **Prior 2281-2290 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **De Kiem** EVERY-10 primary bruto **EUR6.82m** / omzet **EUR5.13m** ~**1.33x** / pnl DROP **-51%** / FTE **66.9** — Gavere Flemish addiction residential care subsidy opacity.
- **De Okkernoot** bruto **EUR13.44m** / ~**5.4x** omzet / pnl JUMP / FTE **143.3** — VAPH autism Pajottegem.
- **Ryhove** bruto **EUR17.67m** / ~**2.2x** omzet / FTE **406.5** — Gent maatwerk.
- **Rozemarijn** bruto **EUR5.96m** / ~**7.0x** omzet / pnl JUMP **+255%** — VAPH+maatwerk Keerbergen.
- **NLZ** omzet **EUR11.25m** / bruto~**1.1x** / FTE **287.3** — Mechelen green maatwerk.
- **SOBO** omzet **EUR2.45m** / bruto~**1.85x** / pnl DROP **-54%** — Brugge maatwerk.
- **Op Maat** prior EVERY-10 bruto **EUR2.35m** / empty omzet / FTE **50.5** (retained).
- **REW** prior omzet **EUR14.72m** / PROFIT FLIP (retained).
"""
(data / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")
print("waste top10 refreshed")

# --- claim / finish research queue ---
def upsert_research_queue():
    path = data / "research_queue.csv"
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r["task_id"] == RQ:
            st = r.get("status")
            eid = (r.get("entity_id") or "").strip()
            if st == "done" and eid and eid != ENTITY:
                raise SystemExit(f"{RQ} already done by other entity={eid}")
            if st == "in_progress" and eid and eid != ENTITY:
                raise SystemExit(f"{RQ} race-locked by entity={eid}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["updated_utc"] = UTC
            r["blocked_gap_id"] = GAP
            r["title"] = (
                f"EVERY-10 + leftover dual — De Kiem YE2025 Medium (bruto JUMP {BRUTO/1e6:.2f}m "
                f"/ ~{RATIO}x omzet / pnl DROP -51% / FTE JUMP {FTE})"
            )
            r["notes"] = (
                f"tick{TICK} EVERY-10 + De Kiem VZW Gavere {KBO} YE2025 Medium CW NL+EN + Strong KBO; "
                f"omzet JUMP {OMZET} (+7.89%); bruto JUMP {BRUTO} (~{RATIO}x / +10.91%); "
                f"pnl DROP {PNL} (-50.85%); equity JUMP {EQUITY}; FTE JUMP {FTE}; 8 VE; NACE 87.204; "
                f"neerlegging 15.06.2026; assets/debt Unknown; FOI {GAP} ready NOT sent; "
                f"progress+waste top10 refreshed; stalls AGB Bornem JR2024 / FARO/AIESH/Citeco/Groupe Foes YE2024; "
                f"after JOMI@2299; next EVERY-10 2310"
            )
            found = True
            break
    if not found:
        raise SystemExit(f"missing {RQ}")
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append({
            "task_id": RQ_NEXT,
            "title": (
                "leftover dual after De Kiem — prefer AGB/FARO-YE2025/AIESH/"
                "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after De Kiem YE2025 Medium (omzet JUMP {OMZET/1e6:.2f}m / "
                f"bruto~{RATIO}x / pnl DROP / FTE JUMP {FTE}). Prefer leftover dual: AGB Bornem/APB → "
                "FARO/AIESH if YE2025 → Citeco/Groupe Foes if YE2025 → unused DSO/water/nuclear/IGS/HVZ "
                "or FREE ETA-VAPH-WZC-maatwerk (Gandae if YE2025). "
                "Do NOT redo De Kiem/JOMI/De Stobbe/De Okkernoot/SOBO/Ryhove/Rozemarijn/Mo-Clean/"
                "Den Azalee/NLZ/Labor/Intro/Buseloc/Stroom/Ateljee/Borgerstein/Waak stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                f"spawned after tick{TICK} De Kiem EVERY-10; FARO/AIESH/Citeco/Groupe Foes YE2024; "
                "AGB Bornem JR2024; Gandae YE2024; next EVERY-10 2310"
            ),
        })
        print("rq_next spawned", RQ_NEXT)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print("research_queue updated")


append_csv(data / "sources.csv", [
    {"source_id": SRC_EN, "title": "De Kiem YE2025 Companyweb EN", "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/de-kiem", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 15.06.2026; assets/debt Unknown; addiction residential care"},
    {"source_id": SRC_NL, "title": "De Kiem YE2025 Companyweb NL", "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/de-kiem", "publisher": "Companyweb", "accessed_date": "2026-08-27", "source_class": "company_register_aggregator", "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; neerlegging 15.06.2026; Groot {FTE} FTE; NACE drugs/alcohol residential"},
    {"source_id": SRC_KBO, "title": f"KBO De Kiem {KBO}", "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}", "publisher": "FOD Economie KBO", "accessed_date": "2026-08-27", "source_class": "official_register", "notes": f"tick{TICK}; Strong KBO Actief VZW De Kiem sinds 30.04.1991; 8 VE; Vluchtenboerstraat 7A 9890 Gavere; RSZ NACE 87.204"},
    {"source_id": SRC_SITE, "title": "De Kiem FOI channel admin@dekiem.be", "url": "https://www.dekiem.be/", "publisher": "De Kiem VZW", "accessed_date": "2026-08-27", "source_class": "foi_contact", "notes": f"tick{TICK}; admin@dekiem.be; T 09 389 66 66; Vluchtenboerstraat 7A 9890 Gavere"},
    {"source_id": SRC_NBB, "title": "NBB CBSO consult De Kiem 0445151311", "url": f"https://consult.cbso.nbb.be/consult-enterprise/{KBO_DIGITS}", "publisher": "NBB CBSO", "accessed_date": "2026-08-27", "source_class": "official_register", "notes": f"tick{TICK}; NBB consult portal; CW cites filing 15.06.2026; full PDF assets/debt still FOI"},
], "source_id")

append_csv(data / "budgets.csv", [
    {"budget_id": "bud_kiem_omzet_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(OMZET), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; omzet JUMP +7.89% vs YE2024 {OMZET_2024}"},
    {"budget_id": "bud_kiem_bruto_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(BRUTO), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; bruto JUMP +10.91% vs YE2024 {BRUTO_2024}; bruto/omzet ~{RATIO}x"},
    {"budget_id": "bud_kiem_pnl_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(PNL), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; pnl DROP -50.85% vs YE2024 {PNL_2024}"},
    {"budget_id": "bud_kiem_equity_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(EQUITY), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; equity JUMP +7.31% vs YE2024 {EQUITY_2024}"},
    {"budget_id": "bud_kiem_fte_jr2025_statutory", "entity_id": ENTITY, "year": "2025", "amount_eur": str(FTE), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; Medium CW; FTE JUMP {FTE} vs YE2024 {FTE_2024}; assets/debt Unknown"},
    {"budget_id": "bud_kiem_pnl_jr2024_statutory_cmp", "entity_id": ENTITY, "year": "2024", "amount_eur": str(PNL_2024), "amount_min_eur": "", "amount_max_eur": "", "basis": "statutory_accounts", "source_id": SRC_EN, "confidence": "medium", "notes": f"tick{TICK}; YE2024 pnl {PNL_2024} comparative"},
], "budget_id")

cash = json.dumps({
    "2025_omzet": OMZET, "2025_bruto": BRUTO, "2025_pnl": PNL, "2025_equity": EQUITY, "2025_fte": FTE,
    "2024_omzet": OMZET_2024, "2024_bruto": BRUTO_2024, "2024_pnl": PNL_2024, "2024_equity": EQUITY_2024, "2024_fte": FTE_2024,
}, separators=(",", ":"))

append_csv(data / "commitments.csv", [{
    "commitment_id": COMM,
    "title": f"De Kiem YE2025 EVERY-10 leftover dual (bruto {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl DROP / FTE JUMP {FTE} / Medium)",
    "entity_id": ENTITY,
    "beneficiary": "Drug/alcohol residential + ambulatory clients Gavere/Gent/Ronse path",
    "legal_basis": f"VZW De Kiem (KBO {KBO}; Actief; 8 VE; RSZ 87.204; Gavere)",
    "decision_date": "2026-06-15",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": str(BRUTO),
    "cash_by_year": cash,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/de-kiem",
    "stated_goal": "Flemish residential + ambulatory addiction care / therapeutic community",
    "cut_option": f"Publish NBB PDF assets/debt; disclose Vlaamse/federal care subsidy matrix behind bruto~{RATIO}x omzet",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gavere>De_Kiem>JR2025_statutory_L5",
    "notes": f"tick{TICK}; Medium CW; bruto primary {BRUTO}; omzet {OMZET} ~{RATIO}x; FOI {GAP}; not TE-additive; DISTINCT vzw_kiemkracht_hamme",
}], "commitment_id")

append_csv(data / "leaderboard.csv", [{
    "item_id": LB,
    "name": f"De Kiem bruto {BRUTO/1e6:.2f}m / omzet {OMZET/1e6:.2f}m ~{RATIO}x / pnl DROP -51% / FTE JUMP {FTE} (YE2025 Gavere addiction care)",
    "level": "L5",
    "type": "addiction_care_vzw_statutory",
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gavere>De_Kiem>JR2025",
    "annual_cost_eur": str(BRUTO),
    "total_cost_eur": str(BRUTO),
    "tco_notes": f"CW omzet JUMP {OMZET} (+7.89%) / bruto JUMP {BRUTO} (+10.91%; ~{RATIO}x) / pnl DROP {PNL} (-50.85%) / equity JUMP {EQUITY} (+7.31%) / FTE JUMP {FTE} (vs {FTE_2024}) / 8 VE",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Drug/alcohol residential + ambulatory clients East Flanders",
    "stated_goal": "Flemish addiction residential therapeutic community + ambulatory centres",
    "measured_outcome": f"omzet JUMP +7.89%; bruto JUMP +10.91% (~{RATIO}x); pnl DROP -50.85%; equity JUMP +7.31%; FTE JUMP {FTE}; filed 15.06.2026",
    "absurdity_score": str(ABS),
    "cost_score": str(COST),
    "difficulty": str(DIFF),
    "priority_index": str(PI),
    "cut_proposal": f"Publish NBB PDF assets/debt/cash FOI; disclose care-subsidy matrix behind bruto>~{RATIO}x omzet + FTE {FTE}",
    "status": "open",
    "struck_reason": "",
    "notes": f"tick{TICK} EVERY-10; Medium CW NL+EN + Strong KBO; FOI {GAP}; after JOMI@2299; AGB/FARO/AIESH YE2024",
}], "item_id")

append_csv(data / "entities.csv", [{
    "entity_id": ENTITY,
    "name_nl": "De Kiem VZW (Gavere / Vlaamse drughulpverlening)",
    "name_fr": "De Kiem ASBL (Gavere / soins residentiels addictions flamands)",
    "name_en": "De Kiem addiction-care ASBL (Gavere Flemish residential drug/alcohol care)",
    "level": "parastatal",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.dekiem.be/",
    "foi_email": "admin@dekiem.be",
    "foi_postal": "Vluchtenboerstraat 7A, 9890 Gavere",
    "notes": f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN + Strong KBO {KBO} Actief 8 VE VZW RSZ 87.204; omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl DROP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 15.06.2026; FOI {GAP}; after JOMI@2299; DISTINCT vzw_kiemkracht_hamme; not TE-additive",
}], "entity_id")

append_csv(data / "foi_queue.csv", [{
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gavere>De_Kiem>NBB_PDF_assets_debt_bruto_gt_omzet_1_33x_pnl_drop_fte_jump",
    "entity_id": ENTITY,
    "what_is_missing": f"NBB PDF YE2025 full (assets/debt/cash); omzet EUR{OMZET}; bruto EUR{BRUTO} (~{RATIO}x); pnl DROP EUR{PNL}; FTE JUMP {FTE}; Vlaamse/federal addiction-care subsidy matrix",
    "why_it_matters": f"Medium CW shows Flemish addiction residential VZW (bruto {BRUTO/1e6:.1f}m ~{RATIO}x omzet / pnl DROP -51% / FTE JUMP to {FTE}); assets/debt unpublished; public care subsidy opacity",
    "priority": "8",
    "recipient_body": "De Kiem VZW",
    "recipient_email": "admin@dekiem.be",
    "recipient_postal": "Vluchtenboerstraat 7A, 9890 Gavere",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-27",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": COMM,
    "linked_leaderboard_id": LB,
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": f"tick{TICK} EVERY-10; ready NOT sent; Medium CW NL+EN + Strong KBO; after JOMI@2299",
}], "gap_id")

upsert_research_queue()

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    + f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,tick{TICK} EVERY-10 + leftover dual De Kiem {KBO} Medium (omzet JUMP {OMZET} +7.89%; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL} -50.85%; equity JUMP {EQUITY} +7.31%; FTE JUMP {FTE}; 8 VE Gavere addiction care); after JOMI@2299; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; progress+waste top10 refreshed; next {RQ_NEXT}; next EVERY-10 2310; continuous hole_fill\n",
    encoding="utf-8",
)
print("loop_state ok")

(raw / "summary.json").write_text(json.dumps({
    "tick": TICK, "unit": RQ, "entity": ENTITY, "kbo": KBO, "every_10": True,
    "omzet": OMZET, "bruto": BRUTO, "pnl": PNL, "equity": EQUITY, "fte": FTE,
    "ratio_bruto_omzet": RATIO, "confidence": "medium", "gap": GAP, "pi": PI,
    "inventory": inv, "foi_ready": ready,
}, indent=2), encoding="utf-8")
(raw / "cw_en_excerpt.txt").write_text(
    f"De Kiem YE2025 omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl {PNL} equity {EQUITY} FTE {FTE} filed 15.06.2026 admin@dekiem.be\n",
    encoding="utf-8",
)

log_path = root / "docs/doge/loop_log.md"
entry = f"""
### {UTC} - tick {TICK} - EVERY-10 + {RQ} De Kiem Gavere (bruto JUMP {BRUTO/1e6:.2f}m / ~{RATIO}x omzet / pnl DROP / FTE JUMP {FTE} / Medium)

- **EVERY-10:** refreshed `progress_every_10_ticks.md` (layers A–E of EUR 347.956 bn TE) + `doge_waste_top10_current.md` (top 10 by priority_index; pure annual flow filter). Inventory budgets {inv['budgets']}+ / commitments {inv['commitments']}+ / leaderboard {inv['leaderboard']}+ / entities {inv['entities']}+ / sources {inv['sources']}+ / FOI ready ~{ready}.
- Unit: **{RQ}** leftover dual after **JOMI@2299**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/Citeco/Groupe Foes still **YE2024**; Gandae still **YE2024**; Ocura/De Lovie/Haagwinde already mined or YE2024-Stopgezet. Took unused FREE Flemish addiction-care **De Kiem VZW** YE2025 (KBO **{KBO}**; Vluchtenboerstraat 7A Gavere; **Actief** **8 VE**; RSZ **87.204**; admin@dekiem.be). Do not redo JOMI/De Stobbe/De Okkernoot/SOBO/Ryhove/Rozemarijn/Stroom stack.
- Found: Companyweb NL+EN YE2025 - omzet **EUR{OMZET}** JUMP +7.89% vs YE2024 EUR{OMZET_2024}; bruto **EUR{BRUTO}** JUMP +10.91% (bruto/omzet ~{RATIO}x); pnl **EUR{PNL}** DROP -50.85%; equity **EUR{EQUITY}** JUMP +7.31%; FTE **{FTE}** JUMP (vs {FTE_2024}); neerlegging **15.06.2026**. Strong KBO Actief 8 VE VZW. Assets/debt Unknown. Medium. FOI via admin@dekiem.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; progress+waste top10; {RQ}=done + {RQ_NEXT} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- **EVERY-10 done** (last was 2290; next **2310**). Next: {RQ_NEXT} (AGB/FARO-if-YE2025 / AIESH / Citeco-Groupe Foes / unused ETA-VAPH-WZC-maatwerk Gandae).

#### EVERY-10 brief (A/B/C/D/E)
- **A:** 100% L0 TE EUR347.956bn Strong
- **B:** 100% L1 subsector map Strong
- **C:** ~99% L2 entity totals (order-of-magnitude); stalls AGB Bornem/FARO/AIESH YE2024
- **D:** ~74-88% generous L5 named; residual dual NOT near-complete of 348bn
- **E:** ~{ready} FOI-ready; answered ~{answered}; partial ~{partial}
"""
text = log_path.read_text(encoding="utf-8")
if f"tick {TICK} - EVERY-10" not in text:
    log_path.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")
    print("loop_log ok")
else:
    print("loop_log already")

(root / "docs/doge/foi/drafts" / f"{GAP}.md").write_text(f"""# FOI draft — De Kiem (NBB PDF / bruto~{RATIO}x omzet / pnl DROP / FTE JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** De Kiem VZW — KBO **{KBO}** (Actief; Vluchtenboerstraat 7A, 9890 Gavere; **8 VE**; FTE {FTE} CW; NACE **87.204**; Flemish addiction residential care)  
**recipient:** admin@dekiem.be · Vluchtenboerstraat 7A, 9890 Gavere (T 09 389 66 66)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_DIGITS}/de-kiem) · [CW NL](https://www.companyweb.be/nl/{KBO_DIGITS}/de-kiem) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_DIGITS}) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/{KBO_DIGITS}) · [site](https://www.dekiem.be/)  
**tick:** {TICK} EVERY-10  
**confidence:** Medium (Strong KBO + Medium CW NL+EN YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **De Kiem** sinds **30.04.1991**; **8 VE**; zetel Vluchtenboerstraat 7A, 9890 Gavere; RSZ NACE **87.204**; admin@dekiem.be.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +7.89%; bruto **EUR{BRUTO:,}** JUMP +10.91% (~{RATIO}x); pnl **EUR{PNL:,}** DROP -50.85%; equity **EUR{EQUITY:,}** JUMP +7.31%; FTE **{FTE}**; filed **15.06.2026**.
- Preferred stalls: AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; Gandae YE2024. After JOMI@2299. DISTINCT Kiemkracht Hamme.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: De Kiem VZW
via admin@dekiem.be
Vluchtenboerstraat 7A, 9890 Gavere
Betreft: Openbaarmaking jaarrekening 2025 De Kiem (KBO {KBO})

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaams Bestuursdecreet e.a.), vraag ik openbaarmaking van:

1. NBB/CBSO PDF van de jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Toelichting bij omzet JUMP EUR{OMZET} (+7.89%) naast bruto EUR{BRUTO}
   (~{RATIO}x omzet), pnl DROP EUR{PNL} (-50.85%) en FTE JUMP {FTE} (vs {FTE_2024}).
3. Overzicht van Vlaamse/federale zorg- en welzijnstoelagen achter personeelskosten (FTE {FTE}).
4. Schulden LT/KT en liquide middelen YE2025.

Periode YE2025 (+ vergelijking YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""", encoding="utf-8")
print("DONE tick", TICK, "EVERY-10 + De Kiem pi", PI, "bruto", BRUTO)

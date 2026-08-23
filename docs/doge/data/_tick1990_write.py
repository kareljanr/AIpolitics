# ephemeral tick1990 — EVERY-10 + CHIREC/CHBA YE2025
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T01:05:00Z"
ENTITY = "vzw_chirec"
GAP = "gap_chirec_nbb_pdf_assets_debt_equity_jump_matrix_l5"
SRC = "src_chirec_jr2025_cw"
SRC_EN = "src_chirec_jr2025_cw_en"
SRC_KBO = "src_chirec_kbo_1990"
SRC_SITE = "src_chirec_site_1990"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1990")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL CHIREC YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0472937059/centre-hospitalier-interregional-edith-cavell-les-hopitaux-de-braine-l-alleud-waterloo-de-delta-et-de-sainte-anne-saint-remi-les-cliniques-de-la",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1990; YE2025 omzet JUMP 803850315 pnl JUMP 35777155 equity JUMP 457591976 bruto JUMP 337125607 FTE 3325; neerlegging 25.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1990/chirec_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN CHIREC YE2025 statutory",
        "url": "https://www.companyweb.be/en/0472937059/centre-hospitalier-interregional-edith-cavell-les-hopitaux-de-braine-l-alleud-waterloo-de-delta-et-de-sainte-anne-saint-remi-les-cliniques-de-la",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1990; EN mirror YE2025 Medium; filed 25-07-2026; raw docs/doge/data/raw/tick1990/chirec_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO CHIREC 0472.937.059 Actief VZW Oudergem",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0472937059",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick1990; Actief VZW; Triomflaan 201 1160 Oudergem; no KBO email; 11 VE; Aanbestedende overheid; CHBA/Braine dual",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "chirec.be Brussels/Brabant hospital network",
        "url": "https://www.chirec.be/",
        "publisher": "CHIREC",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick1990; CHBA/Braine-l'Alleud-Waterloo/Delta/Saint-Anne hospital ASBL dual",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_chirec_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "803850315",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1990; omzet JUMP 803850315 +7.32pct vs YE2024 748989062",
    },
    {
        "budget_id": "bud_chirec_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "35777155",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1990; pnl JUMP 35777155 +21.68pct vs YE2024 29401794",
    },
    {
        "budget_id": "bud_chirec_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "457591976",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1990; equity JUMP 457591976 +14.43pct vs YE2024 399894102",
    },
    {
        "budget_id": "bud_chirec_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "337125607",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1990; bruto JUMP 337125607 +6.90pct vs YE2024 315372550",
    },
    {
        "budget_id": "bud_chirec_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "3325",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1990; YE2025 FTE 3325 vs YE2024 3286 (+39)",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_chirec_jr2025_statutory_hospital",
    "title": "CHIREC/CHBA YE2025 leftover hospital dual (omzet JUMP 803.85m / equity JUMP 457.59m / pnl JUMP 35.78m)",
    "entity_id": ENTITY,
    "beneficiary": "Brussels/Brabant hospital patients / CHBA network dual",
    "legal_basis": "ASBL hospital network Edith Cavell / Braine-l'Alleud-Waterloo / Delta / Sainte-Anne",
    "decision_date": "2026-07-25",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "803850315",
    "cash_by_year": '{"2025_omzet":803850315,"2025_pnl":35777155,"2025_equity":457591976,"2025_bruto":337125607,"2025_fte":3325}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0472937059/centre-hospitalier-interregional-edith-cavell-les-hopitaux-de-braine-l-alleud-waterloo-de-delta-et-de-sainte-anne-saint-remi-les-cliniques-de-la",
    "stated_goal": "Interregional hospital care CHBA/Brussels network",
    "cut_option": "Publish NBB PDF assets/debt + equity JUMP recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Bruxelles_Brabant>CHIREC_CHBA>JR2025_statutory_L5",
    "notes": "tick1990 EVERY-10 dual; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Humani deferred",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_chirec_omzet_jump_803_85m_equity_jump_457_59m_pnl_jump_jr2025",
    "name": "CHIREC/CHBA omzet JUMP 803.85m / equity JUMP 457.59m / pnl JUMP 35.78m (YE2025)",
    "level": "L5",
    "type": "brussels_brabant_hospital_asbl_dual",
    "hierarchy_path": "Bruxelles_Brabant>CHIREC_CHBA>JR2025_statutory_L5",
    "annual_cost_eur": "803850315",
    "total_cost_eur": "457591976",
    "tco_notes": "statutory omzet JUMP 803850315 pnl JUMP 35777155 equity JUMP 457591976 bruto JUMP 337125607 FTE 3325; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "CHBA/Brussels hospital patients via CHIREC ASBL",
    "stated_goal": "Interregional hospital care",
    "measured_outcome": "Medium CW YE2025; 804m omzet with equity JUMP +14pct and pnl JUMP +22pct; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "7.5",
    "difficulty": "4.0",
    "priority_index": "6.475",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; dual vs Citadelle/Tivoli/Humani hospital opacity",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1990 EVERY-10 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2000",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "CHIREC / CHBA (Centre Hospitalier Interregional Edith Cavell)",
    "name_fr": "CHIREC / CHBA (Centre Hospitalier Interregional Edith Cavell)",
    "name_en": "CHIREC / CHBA (Brussels-Brabant hospital network ASBL)",
    "level": "asbl",
    "parent_id": "bru_gov",
    "community_language": "bi",
    "website": "https://www.chirec.be/",
    "foi_email": "",
    "foi_postal": "Triomflaan 201, 1160 Oudergem",
    "notes": "tick1990 EVERY-10 YE2025 Medium CW NL+EN + Strong KBO 0472.937.059 Actief VZW; omzet JUMP 803.85m pnl JUMP 35.78m equity JUMP 457.59m bruto JUMP 337.13m FTE 3325; assets/debt Unknown; neerlegging 25.07.2026; 11 VE; FOI gap_chirec_nbb_pdf_assets_debt_equity_jump_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Humani deferred; do not redo Tivoli/Citadelle/ISoSL/Epicura/CHwapi/CHU UCL Namur/Vivalia/HELORA",
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Bruxelles_Brabant>CHIREC_CHBA>NBB_PDF_assets_debt_equity_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); equity JUMP +14pct recon; dual vs Citadelle/Tivoli/Humani hospital path",
    "why_it_matters": "Medium CW shows 804m omzet CHBA/Brussels hospital ASBL with equity JUMP +14pct without balance sheet",
    "priority": "7",
    "recipient_body": "CHIREC",
    "recipient_email": "",
    "recipient_postal": "Triomflaan 201, 1160 Oudergem / chirec.be",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_chirec_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_chirec_omzet_jump_803_85m_equity_jump_457_59m_pnl_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1990 EVERY-10; human-send only; Medium CW; no KBO email — route via chirec.be; next every-10 2000",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — CHIREC/CHBA (NBB PDF / assets-debt / equity JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** CHIREC VZW — KBO **0472.937.059**  
**recipient:** route via chirec.be (no KBO email)  
**sources:** [CW NL](https://www.companyweb.be/nl/0472937059/centre-hospitalier-interregional-edith-cavell-les-hopitaux-de-braine-l-alleud-waterloo-de-delta-et-de-sainte-anne-saint-remi-les-cliniques-de-la) · [CW EN](https://www.companyweb.be/en/0472937059/centre-hospitalier-interregional-edith-cavell-les-hopitaux-de-braine-l-alleud-waterloo-de-delta-et-de-sainte-anne-saint-remi-les-cliniques-de-la) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0472937059) · [site](https://www.chirec.be/)  
**tick:** 1990  
**confidence:** Medium (CW NL+EN; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **25.07.2026**): omzet **EUR803,850,315** JUMP +7.32%; pnl **EUR35,777,155** JUMP +21.68%; equity **EUR457,591,976** JUMP +14.43%; bruto **EUR337,125,607** JUMP +6.90%; FTE **3325** (+39 vs 3286); assets/debt **Unknown**.
- CHBA / Braine-l'Alleud-Waterloo / Delta / Sainte-Anne hospital ASBL. Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. Tivoli/Citadelle/ISoSL already mined. Humani deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: CHIREC — Triomflaan 201, 1160 Oudergem
via chirec.be openbaarheid / info
cc: Cocof / Province Brabant wallon transparence indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 CHIREC/CHBA + balans (KBO 0472.937.059)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 25.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon equity JUMP (+14.43pct vs YE2024 EUR399,894,102).
4. Dual vs Citadelle / Tivoli / Humani indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

# EVERY-10 progress refresh
progress = Path("docs/doge/data/progress_every_10_ticks.md")
prog_text = progress.read_text(encoding="utf-8")
snapshot = """## Snapshot at **tick 1990** (2026-08-24)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1981-1990 hospital/ADT continuum after 1980 IDELUX Finances |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1981-1990 is residual dual L5 (not near-complete of 348bn):** **Vivalia** omzet JUMP **473.14m** · **SPI** omzet DROP **20.76m** / bruto collapse · **IDETA** omzet DROP **12.49m** · **CHwapi** omzet JUMP **337.72m** / equity DROP **-46pct** · **Epicura** omzet JUMP **370.88m** / pnl LOSS · **CHU UCL Namur** omzet JUMP **637.53m** · **ISoSL** omzet JUMP **271.49m** / FTE JUMP · **CHR Citadelle** omzet JUMP **593.96m** / equity JUMP **+68pct** · **CHU Tivoli** omzet JUMP **252.95m** / equity JUMP **+31pct** · **CHIREC/CHBA** omzet JUMP **803.85m** / equity JUMP **457.59m** Medium (this tick EVERY-10 dual) |
| **E. FOI-ready gaps** | **~1607** drafts ready | Human send only; answered **~11**; partial **~28**; total FOI rows **~1659** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/property/renewable/energy/nuclear/water/forest/hospital shells** (**NEW 1981-1990** Vivalia · SPI · IDETA · CHwapi · Epicura · CHU UCL Namur · ISoSL · CHR Citadelle · CHU Tivoli · **CHIREC/CHBA** · prior IDELUX Finances/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/BEP/IBH/HELORA stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 1990)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 52011 |
| commitments.csv | 5656 |
| leaderboard.csv | 7777 |
| entities.csv | 1692 |
| sources.csv | 4835 |
| FOI ready | 1607 |
| FOI answered | 11 |
| FOI partial | 28 |
| FOI total rows | 1659 |
| research_queue open | rq_1991 after progress |

### What improved since tick 1980

- **Residual dual (tick1981-1990):** **Vivalia** · **SPI** · **IDETA** · **CHwapi** · **Epicura** · **CHU UCL Namur** · **ISoSL** · **CHR Citadelle** · **CHU Tivoli** · **CHIREC/CHBA** (this tick EVERY-10 dual — Brussels/Brabant hospital ASBL YE2025 Medium CW).
- **Blocked still:** AGB Bornem JR2024-only · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH/REW YE2024-only · Bosgroep IJzer/Houtland/Limburg YE2025 unpublished · prior Eneco deposit FOI stack · Humani YE2025 live deferred.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10 (re-verified; corrupt AGB pi>10 / OWV snowball stock / Metro3 stock filtered off pure annual). Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **2000**.


"""
anchor = "## Snapshot at **tick 1980**"
if "## Snapshot at **tick 1990**" not in prog_text:
    if anchor in prog_text:
        prog_text = prog_text.replace(anchor, snapshot + anchor, 1)
    else:
        prog_text = prog_text.rstrip() + "\n\n" + snapshot
    progress.write_text(prog_text, encoding="utf-8")
    print("progress refreshed")
else:
    print("progress already has 1990")

top10 = Path("docs/doge/data/doge_waste_top10_current.md")
top10.write_text(
    """# DOGE waste ranking — current top 10

**As-of:** tick **1990** (2026-08-24) · **7777** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW leftover 1981-1990:** **CHIREC equity 457.59m** · **Citadelle equity JUMP 81.05m** · **ISoSL omzet 271.49m** · **Tivoli equity 43.14m** · **CHwapi equity DROP 128.52m** · **Epicura omzet 370.88m** · **CHU UCL Namur omzet 637.53m** · **Vivalia omzet 473.14m** · **SPI omzet 20.76m** · **IDETA omzet 12.49m** · prior **IDELUX Finances / IFIGA / SOFILUX / IDEFIN / FINIMO / FINEST / HYGEA / BEP / IBH / HELORA** · prior **nuclear / Fluxys / Elia / Enodia / RESA** · prior Publi-T/Publigas/Nethys/Virya · prior **Eneco continuum** · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 1980:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off). **Major NEW residual 1981-1990 (off pure top10 / dual):** Vivalia · SPI · IDETA · CHwapi · Epicura · CHU UCL Namur · ISoSL · CHR Citadelle · CHU Tivoli · **CHIREC/CHBA** (EVERY-10 dual). Count NEW since 1980: 10 residual dual ticks. **Prior IDELUX Finances/IFIGA/SOFILUX/HELORA stack retained.** Not TE-additive of ~348bn.
""",
    encoding="utf-8",
)
print("top10 refreshed")

for x in qrows:
    if x.get("task_id") == "rq_1990":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "EVERY-10 + leftover dual after CHU Tivoli — CHIREC/CHBA YE2025 Medium"
        x["notes"] = (
            "tick1990 EVERY-10 + CHIREC Medium omzet JUMP 803.85m equity JUMP 457.59m; FOI ready; next rq_1991; next every-10 2000"
        )
        x["instructions"] = (
            "Completed EVERY-10 progress+top10 + leftover CHIREC/CHBA YE2025 Medium CW; KBO 0472.937.059; "
            "omzet JUMP 803850315 pnl JUMP 35777155 equity JUMP 457591976 bruto JUMP 337125607 FTE 3325; FOI " + GAP
        )
if not any(x.get("task_id") == "rq_1991" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1991",
            "title": "leftover dual hole-fill after CHIREC EVERY-10",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1990 EVERY-10 after CHIREC/CHBA YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (Humani / GHdC / Haute Senne / Saint-Luc / CNDG if YE2025). "
                "Do NOT redo CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1990 EVERY-10 CHIREC; next every-10 2000; Humani YE2025 deferred",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1990",
        "ticks_completed": "1990",
        "paused": "no",
        "notes": (
            "tick1990 EVERY-10 + leftover CHIREC/CHBA 0472.937.059 Medium CW (omzet JUMP 803.85m pnl JUMP 35.78m equity JUMP 457.59m bruto JUMP 337.13m FTE 3325; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Humani deferred; next rq_1991; next every-10 2000; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

logp = Path("docs/doge/loop_log.md")
entry = """

## Tick 1990 - 2026-08-24T01:05:00Z - rq_1990 EVERY-10 + CHIREC/CHBA (omzet JUMP 803.85m / equity JUMP 457.59m / Medium)

- Unit: **rq_1990** EVERY-10 mandatory + leftover dual after **rq_1989 CHU Tivoli**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **CHIREC/CHBA** YE2025 (KBO **0472.937.059**; Triomflaan 201 Oudergem; Brussels/Brabant **hospital ASBL**). **Humani** YE2025 also live deferred. Do not redo Tivoli/Citadelle/ISoSL/Epicura/CHwapi/CHU UCL Namur/Vivalia/HELORA/IDETA/SPI/IDELUX Finances.
- EVERY-10: refreshed **progress_every_10_ticks.md** (tick 1990 snapshot; residual dual 1981-1990) + **doge_waste_top10_current.md** (pure annual top10 stable GIP/fossil/cars/cheque/reporté; NEW residual dual off-top10).
- Found: Companyweb NL+EN YE2025 - omzet **EUR803,850,315** JUMP +7.32%; pnl **EUR35,777,155** JUMP +21.68%; equity **EUR457,591,976** JUMP +14.43%; bruto **EUR337,125,607** JUMP +6.90%; FTE **3325** (+39 vs 3286); neerlegging **25.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 11 VE; no KBO email.
- Wrote: sources (+4); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_chirec); foi + draft gap_chirec_nbb_pdf_assets_debt_equity_jump_matrix_l5; progress+top10; rq_1990=done + rq_1991 open; loop_state ticks=1990; raw under docs/doge/data/raw/tick1990/.
- FOI: **ready not sent** (human-gated; route via chirec.be).
- EVERY-10 done. Next every-10 **2000**. Next: rq_1991 (AGB/FARO-if-YE2025 / AIESH-REW / Humani-GHdC / unused DSO-IGS-HVZ-hospital).
"""
text = logp.read_text(encoding="utf-8")
if "## Tick 1990" not in text:
    logp.write_text(text.rstrip() + entry + "\n", encoding="utf-8")
    print("log appended")
else:
    print("log already has 1990")

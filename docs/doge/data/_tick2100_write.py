# tick 2100 — EVERY-10 + Always Home YE2025 Medium CW leftover dual
import csv
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
UTC = "2026-08-25T05:55:00Z"
DATE = "2026-08-25"
ENTITY = "nv_always_home"
GAP = "gap_always_home_nbb_pdf_assets_debt_omzet_drop_equity_jump_matrix_l5"
COMM = "comm_always_home_jr2025_statutory_rob_rvt"
LB = "lb_always_home_omzet_drop_8_86m_equity_jump_jr2025"

OMZET = 8857853
PNL = 299634
EQUITY = 1758472
BRUTO = 6600717
FTE = 99.8


def append_csv(path: Path, rows: list[dict], id_key: str):
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        existing = list(r)
    have = {row.get(id_key) for row in existing}
    new_rows = [row for row in rows if row.get(id_key) not in have]
    if not new_rows:
        print(f"skip {path.name}: already present")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(existing)
        for row in new_rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})
    print(f"append {path.name}: +{len(new_rows)}")


# --- EVERY-10 markdown ---
progress = DATA / "progress_every_10_ticks.md"
old_p = progress.read_text(encoding="utf-8")
hdr = """# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the \"public spend pie\" for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

"""
snap = """## Snapshot at **tick 2100** (2026-08-25)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2091-2100 zorg/DSO continuum after 2090 Familiezorg WV |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2091-2100 is residual dual L5 (not near-complete of 348bn):** **Zilvervogel** omzet JUMP **20.96m** · **SED Zoutleeuw** pnl FLIP LOSS · **Lidwina** bruto JUMP **21.60m** · **Sint-Lucia** omzet JUMP **7.67m** · **Begralim** omzet JUMP **22.67m** · **emeis Belgium** omzet JUMP **19.63m** / equity NEG **-360.39m** · **Familiezorg Gent** bruto JUMP **70.04m** · **AREWAL** omzet DROP **5.63m** / equity THIN · **SLG Operaties VL** omzet JUMP **58.28m** / FTE JUMP **1095** · **Always Home** omzet DROP **8.86m** Medium (this tick EVERY-10 dual) |
| **E. FOI-ready gaps** | **~1716** drafts ready | Human send only; answered **~11**; partial **~28**; total FOI rows **~1768** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych shells** (**NEW 2091-2100** Zilvervogel · SED · Lidwina · Sint-Lucia · Begralim · emeis · Familiezorg Gent · AREWAL · SLG Operaties · **Always Home** · prior 2081-2090 / 2071-2080 stacks retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2100)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 52562 |
| commitments.csv | 5766 |
| leaderboard.csv | 7887 |
| entities.csv | 1800 |
| sources.csv | 5393 |
| FOI ready | ~1716 |
| FOI answered | 11 |
| FOI partial | 28 |
| FOI total rows | ~1768 |
| research_queue open | rq_2101 after progress |

### What improved since tick 2090

- **Residual dual (tick2091-2100):** **CZD Zilvervogel Lo-Reninge** · **Sint-Elisabeth's Dal Zoutleeuw** · **Lidwina Mol** · **Sint-Lucia Turnhout** · **Begralim / Grauwzusters Limburg** · **emeis Belgium** · **Familiezorg Gent** · **AREWAL** (AIEG/AIESH/REW shared-services SC) · **SLG Operaties Vlaanderen** (7 WZC absorptions Jul 2025) · **Always Home** (this tick EVERY-10 dual — Mechelen NV ROB/RVT NACE 87.301 YE2025 Medium CW; omzet DROP 8.86m; equity JUMP; Colisée bestuurder; DISTINCT Armonea/SLG/emeis).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH 0201.712.587 / REW 0644.638.937 YE2024-only · Jessa/ZOL CW N/A omzet · prior Eneco deposit FOI stack.

---

"""
idx = old_p.find("## Snapshot at")
tail = old_p[idx:] if idx >= 0 else old_p
progress.write_text(hdr + snap + tail, encoding="utf-8")
print("progress_every_10 refreshed")

waste = DATA / "doge_waste_top10_current.md"
waste.write_text(
    """# DOGE waste ranking — current top 10

**As-of:** tick **2100** (2026-08-25) · **7887** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2091-2100:** **SLG Operaties omzet 58.28m / FTE 1095** · **Familiezorg Gent bruto 70.04m** · **emeis equity NEG -360.39m** · **Begralim omzet 22.67m** · **Zilvervogel omzet 20.96m** · **Lidwina bruto 21.60m** · **Always Home omzet 8.86m** · **Sint-Lucia omzet 7.67m** · **AREWAL omzet 5.63m** · SED · prior 2081-2090 Medemens/Familiezorg WV/De Lovie/Ocura stack retained · prior 2071-2080 / 2061-2070 stacks retained · prior nuclear/Fluxys/Elia/Enodia/RESA · prior Eneco continuum · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2090:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2091-2100 (off pure top10 / dual):** Zilvervogel · SED · Lidwina · Sint-Lucia · Begralim · emeis · Familiezorg Gent · AREWAL · SLG Operaties · **Always Home** (EVERY-10 dual). Count NEW since 2090: 10 residual dual ticks. **Prior 2081-2090 + 2071-2080 stacks retained.** Not TE-additive of ~348bn.
""",
    encoding="utf-8",
)
print("waste top10 refreshed")

# FOI draft
foi_path = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{GAP}.md"
foi_path.write_text(
    f"""# FOI draft — Always Home (NBB PDF / assets-debt / omzet-drop / equity-jump)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Always Home NV — KBO **0821.289.991**  
**recipient:** info@armonea.be · Stationsstraat 102, 2800 Mechelen · cc Departement Zorg  
**sources:** [CW NL](https://www.companyweb.be/nl/0821289991/always-home) · [CW EN](https://www.companyweb.be/en/0821289991/always-home) · [CW FR](https://www.companyweb.be/fr/0821289991/always-home) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=821289991) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/0821289991)  
**tick:** 2100 (EVERY-10)  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown; KBO Strong)

## Context
- YE **2025** (neerlegging **15.07.2026**): omzet **EUR{OMZET}** DROP −2.31%; bruto **EUR{BRUTO}** DROP −8.58%; pnl **EUR{PNL}** DROP −3.72%; equity **EUR{EQUITY}** JUMP +20.54%; FTE **{FTE}** JUMP vs YE2024 98.7; assets/debt **Unknown**.
- KBO: Actief NV; **4 VE**; NACE **87.301** ROB / RSZ **87.101** RVT; kapitaal **EUR2673256.30**; zetel Stationsstraat 102 Mechelen (shared Armonea HQ); bestuurder Colisée Belgium **0723.858.144**; email info@armonea.be.
- DISTINCT from Armonea NV 0889.421.308 / SLG Operaties Vlaanderen 0845.064.196 / Colisée Belgium / emeis Belgium.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Always Home NV — Stationsstraat 102, 2800 Mechelen
via info@armonea.be
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Always Home + balans/resultaatmatrix (KBO 0821.289.991)
Geachte, op grond van toepasselijke openbaarheidsregels (publiek gesubsidieerde ouderenzorg via Zorgkas-dagprijspad) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 15.07.2026) + depositreferentie.
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke middelen (Zorgkas/IFIC/code73-74) vs omzet/eigen bijdragen 2025 (omzet EUR{OMZET} / bruto EUR{BRUTO}).
4. Toelichting omzet DROP −2.31% / bruto DROP −8.58% bij equity JUMP +20.54%; lijst 4 VE-campussen; related-party met Armonea NV / SLG Operaties / Colisée Belgium.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("FOI draft written")

sources = [
    {
        "source_id": "src_always_home_jr2025_cw_nl",
        "title": "Always Home Companyweb NL YE2025",
        "url": "https://www.companyweb.be/nl/0821289991/always-home",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2100 EVERY-10; YE2025 omzet/pnl/equity/bruto/FTE; neerlegging 15.07.2026; Medium",
    },
    {
        "source_id": "src_always_home_jr2025_cw_en",
        "title": "Always Home Companyweb EN YE2025",
        "url": "https://www.companyweb.be/en/0821289991/always-home",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2100 EVERY-10; EN mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_always_home_jr2025_cw_fr",
        "title": "Always Home Companyweb FR YE2025",
        "url": "https://www.companyweb.be/fr/0821289991/always-home",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2100 EVERY-10; FR mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_always_home_kbo_2100",
        "title": "KBO Always Home 0821.289.991",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=821289991",
        "publisher": "KBO/BCE",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2100; Actief NV; 4 VE; NACE 87.301/87.101; Colisee bestuurder; Strong identity",
    },
    {
        "source_id": "src_always_home_nbb_consult_2100",
        "title": "NBB CBSO consult Always Home 0821289991",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0821289991",
        "publisher": "NBB CBSO",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": "tick2100; deposit portal; full PDF FOI; Medium path",
    },
]
append_csv(DATA / "sources.csv", sources, "source_id")

budgets = [
    {
        "budget_id": "bud_always_home_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW turnover / Omzet YE2025 (primary envelope)",
        "source_id": "src_always_home_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2100; omzet DROP 8857853 (-2.31%) vs YE2024 9067215",
    },
    {
        "budget_id": "bud_always_home_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW Profit/Loss YE2025",
        "source_id": "src_always_home_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2100; pnl DROP 299634 (-3.72%) vs YE2024 311200",
    },
    {
        "budget_id": "bud_always_home_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW Equity / Eigen vermogen YE2025",
        "source_id": "src_always_home_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2100; equity JUMP 1758472 (+20.54%) vs YE2024 1458838",
    },
    {
        "budget_id": "bud_always_home_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW Gross margin / Brutomarge YE2025",
        "source_id": "src_always_home_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2100; bruto DROP 6600717 (-8.58%) vs YE2024 7220491",
    },
    {
        "budget_id": "bud_always_home_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW social-balance FTE / Employees",
        "source_id": "src_always_home_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2100; FTE JUMP 99.8 vs YE2024 98.7",
    },
]
append_csv(DATA / "budgets.csv", budgets, "budget_id")

append_csv(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Always Home NV",
            "name_fr": "Always Home SA",
            "name_en": "Always Home NV (Armonea/Colisee Flanders WZC ops sister)",
            "level": "other",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.armonea.be",
            "foi_email": "info@armonea.be",
            "foi_postal": "Stationsstraat 102, 2800 Mechelen",
            "notes": (
                "tick2100 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0821.289.991 Actief NV "
                "4 VE; NACE 87.301/87.101; kapitaal 2.67m; Colisee Belgium bestuurder; "
                "omzet DROP 8.86m bruto DROP 6.60m pnl DROP 0.30m equity JUMP 1.76m FTE JUMP 99.8; "
                "DISTINCT Armonea/SLG Operaties/emeis; FOI "
                f"{GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024"
            ),
        }
    ],
    "entity_id",
)

append_csv(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": "Always Home YE2025 leftover dual EVERY-10 (omzet DROP 8.86m / equity JUMP)",
            "entity_id": ENTITY,
            "beneficiary": "Flanders ROB/RVT residents via Always Home (4 VE; Colisee/Armonea group sister)",
            "legal_basis": "NV ROB/RVT / publiek gesubsidieerde ouderenzorg (KBO 0821.289.991)",
            "decision_date": "2026-07-15",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": (
                f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
                f'"2025_bruto":{BRUTO},"2025_fte":{FTE}}}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0821289991/always-home",
            "stated_goal": "Operate Flanders nursing homes (Always Home brand)",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; map Zorgkas vs omzet; disclose related-party "
                "with Armonea/SLG/Colisee; explain omzet/bruto DROP with equity JUMP"
            ),
            "source_id": "src_always_home_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Zorg>Always_Home>JR2025_statutory_L5",
            "notes": (
                "tick2100 EVERY-10; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; not TE-additive of 348bn; omzet primary"
            ),
        }
    ],
    "commitment_id",
)

append_csv(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Always Home omzet DROP 8.86m / equity JUMP + Colisee sister (YE2025)",
            "level": "L5",
            "type": "wzc_ops_statutory",
            "hierarchy_path": "Vlaanderen>Zorg>Always_Home>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                "CW omzet primary ROB/RVT envelope; bruto DROP; equity JUMP; "
                "assets/debt Unknown pending NBB PDF FOI"
            ),
            "confidence": "medium",
            "source_id": "src_always_home_jr2025_cw_en",
            "beneficiaries": "Always Home Flanders ROB-RVT residents (4 VE)",
            "stated_goal": "Operate Always Home nursing homes",
            "measured_outcome": (
                "omzet DROP -2.31%; bruto DROP -8.58%; pnl DROP -3.72%; "
                "equity JUMP +20.54%; FTE JUMP 99.8"
            ),
            "absurdity_score": "4.5",
            "cost_score": "3.5",
            "difficulty": "3.5",
            "priority_index": "4.3",
            "cut_proposal": (
                "Publish NBB PDF assets/debt FOI; map Zorgkas vs omzet; "
                "disclose Armonea/SLG/Colisee related-party matrix"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2100 EVERY-10; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "DISTINCT Armonea/SLG/emeis"
            ),
        }
    ],
    "item_id",
)

append_csv(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Zorg>Always_Home>NBB_PDF_assets_debt_omzet_drop",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); Zorgkas/public "
                "subsidy vs omzet split; related-party with Armonea/SLG/Colisee; list of 4 VE; "
                "explanation of omzet/bruto DROP with equity JUMP"
            ),
            "why_it_matters": (
                "Medium CW shows 8.86m omzet Colisee-group Flanders WZC NV sister of Armonea/"
                "SLG without balanstotaal/assets/debt; material L5 residual after SLG merger JUMP"
            ),
            "priority": "8",
            "recipient_body": "Always Home NV (via Armonea)",
            "recipient_email": "info@armonea.be",
            "recipient_postal": "Stationsstraat 102, 2800 Mechelen",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": DATE,
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": COMM,
            "linked_leaderboard_id": LB,
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "tick2100 EVERY-10; human-send only; Medium CW; next every-10 2110",
        }
    ],
    "gap_id",
)

rq_path = DATA / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

found = False
for row in rows:
    if row["task_id"] == "rq_2100":
        found = True
        row["status"] = "done"
        row["title"] = "EVERY-10 + leftover dual — Always Home YE2025 Medium"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["hierarchy_target"] = "L5"
        row["instructions"] = (
            "Completed EVERY-10 + leftover Always Home YE2025 Medium CW; KBO 0821.289.991; "
            f"omzet DROP {OMZET} bruto DROP {BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} "
            f"FTE JUMP {FTE}; FOI {GAP}; 4 VE Colisee bestuurder; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Armonea/SLG/emeis"
        )
        row["notes"] = (
            "tick2100 EVERY-10 + Always Home Medium omzet DROP 8.86m bruto DROP 6.60m pnl DROP "
            "0.30m equity JUMP 1.76m FTE JUMP 99.8; FOI ready; progress+waste refreshed; "
            "next rq_2101; next every-10 2110"
        )
        row["blocked_gap_id"] = GAP

if not any(r.get("task_id") == "rq_2101" for r in rows):
    rows.append(
        {
            "task_id": "rq_2101",
            "title": "leftover dual hole-fill after Always Home EVERY-10 — prefer AGB/FARO-YE2025/AIESH-REW/unused",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2101 after Always Home EVERY-10 YE2025 Medium. Prefer leftover AGB/APB if "
                "JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else "
                "unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. Do NOT redo Always Home, "
                "SLG Operaties Vlaanderen, AREWAL, Familiezorg Gent, emeis Belgium, Begralim, "
                "Sint-Lucia, Lidwina, SED, Zilvervogel, Familiezorg WV, De Lovie, Ocura, Armonea, "
                "Colisee Belgium, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, "
                "Synatom, IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, Belgoprocess, "
                "Laborelec, NIRAS, Bel V, Dijk92, FANC, SCK CEN, EURIDICE, IRE*, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2100 EVERY-10 Always Home; next every-10 2110",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
assert found, "rq_2100 not found"

with (DATA / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ]
    )
    w.writerow(
        [
            "main",
            "continuous",
            "hole_fill",
            UTC,
            "rq_2100",
            "2100",
            "no",
            (
                "tick2100 EVERY-10 + leftover Always Home 0821.289.991 Medium CW "
                "(omzet DROP 8.86m bruto DROP 6.60m pnl DROP 0.30m equity JUMP 1.76m "
                "FTE JUMP 99.8; 4 VE Colisee; assets/debt Unknown); progress+waste refreshed; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2101; next every-10 2110"
            ),
        ]
    )

if "## Tick 2100 -" in LOG.read_text(encoding="utf-8"):
    print("skip loop_log: Tick 2100 already present")
else:
    log_block = f"""

## Tick 2100 - {UTC} - EVERY-10 + rq_2100 Always Home (omzet DROP 8.86m / equity JUMP / Medium)

- Unit: **rq_2100** EVERY-10 after **rq_2099 SLG Operaties**. Refreshed **progress_every_10_ticks.md** (tick 2100 snapshot) + **doge_waste_top10_current.md** (top10 stable GIP/fossil/cars/cheque/reporté). Prefer: AGB Bornem **JR2024-only**; FARO **YE2024**; AIESH **YE2024**; REW **YE2024**. Took unused WZC sister **Always Home** YE2025 (KBO **0821.289.991**; Stationsstraat 102 Mechelen shared Armonea HQ; NV ROB/RVT; **4 VE**; NACE **87.301/87.101**; bestuurder Colisée Belgium). DISTINCT from Armonea NV / SLG Operaties / emeis.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** DROP −2.31%; bruto **EUR{BRUTO}** DROP −8.58%; pnl **EUR{PNL}** DROP −3.72%; equity **EUR{EQUITY}** JUMP +20.54%; FTE **{FTE}** JUMP vs YE2024 98.7; neerlegging **15.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via info@armonea.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 4.3); entities (+1 {ENTITY}); foi + draft {GAP}; progress+waste EVERY-10; rq_2100=done + rq_2101 open; loop_state ticks=2100; raw docs/doge/data/raw/tick2100/.
- FOI: **ready not sent** (human-gated).
- **EVERY-10 DONE.** Next every-10 is **2110**. Next: rq_2101 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC).
"""
    with LOG.open("a", encoding="utf-8") as f:
        f.write(log_block)

print("tick2100 write OK; found=", found)

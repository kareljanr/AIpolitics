# tick2220 — EVERY-10 progress + NBSW YE2025 Medium leftover dual
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_nbsw_hasselt"
TICK = "2220"
UTC = "2026-08-26T18:55:00Z"
GAP = "gap_nbsw_nbb_pdf_assets_debt_empty_omzet_bruto_drop_pnl_drop_equity_jump_matrix_l5"
COMM = "comm_nbsw_jr2025_statutory_maatwerk_empty_omzet_bruto_drop_pnl_drop_equity_jump"
LB = "lb_nbsw_bruto_0_45m_empty_omzet_pnl_drop_29pct_equity_jump_jr2025"

BR25, BR24 = 447973, 472345
PN25, PN24 = 122245, 172353
EQ25, EQ24 = 1554399, 1432154
FTE25 = 8.8


def read_csv(name: str) -> tuple[list[str], list[dict]]:
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def write_csv(name: str, fields: list[str], rows: list[dict]) -> None:
    with (DATA / name).open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})


def upsert(rows: list[dict], key: str, kid: str, new: dict) -> None:
    for i, r in enumerate(rows):
        if r.get(key) == kid:
            rows[i] = {**r, **new}
            return
    rows.append(new)


# --- progress every 10 ---
prog = DATA / "progress_every_10_ticks.md"
old = prog.read_text(encoding="utf-8")
snap = """# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2220** (2026-08-26)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2211-2220 continuum; AGB Bornem / FARO / AIESH / REW still YE2024 stalls |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2211-2220 is residual dual L5 (not near-complete of 348bn):** **Werkhuizen MIN** / **Ecoso** · **Odas** / **OptimaT** · **Groep Maatwerk** / **Constructief** · **Kringloop Deltagroep** · **Werkmmaat** empty omzet · **Veerkracht 4** · **Opnieuw & Co** omzet **6.45m** · **NBSW** bruto **0.45m** empty omzet / pnl DROP **−29%** (EVERY-10 primary) Medium |
| **E. FOI-ready gaps** | **~1862** drafts ready | Human send only; answered **~11**; partial **~28**; total FOI rows **~1914** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability/maatwerk shells** (**NEW 2211-2220** Werkhuizen MIN · Ecoso · Odas · OptimaT · Groep Maatwerk · Constructief · Kringloop · Werkmmaat · Veerkracht4 · Opnieuw · **NBSW** · prior 2201-2210 ACG/Entiris/Oesterbank stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2220)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 53245+ |
| commitments.csv | 5912+ |
| leaderboard.csv | 8033+ |
| entities.csv | 1943+ |
| sources.csv | 6121+ |
| FOI ready | ~1862 |
| FOI answered | 11 |
| FOI partial | 28 |
| FOI total rows | ~1914 |
| research_queue open | rq_2221 after progress |

### What improved since tick 2210

- **Residual dual (tick2211-2220):** **Werkhuizen MIN** (bruto DROP / LOSS FLIP) · **Ecoso** (pnl DROP −95% / 17 VE) · **Odas** (omzet JUMP **11.34m** / bruto~**1.72×** / LOSS NARROW) · **OptimaT** (omzet **11.92m** / bruto~**3.54×** / equity **39.4m**) · **Groep Maatwerk** LOSS FLIP · **Constructief** pnl JUMP **+293%** · **Kringloop Deltagroep** pnl DROP **−76%** · **Werkmmaat** empty omzet / pnl JUMP **+602%** · **Veerkracht 4** empty omzet / pnl JUMP **+72%** · **Opnieuw & Co** omzet JUMP **6.45m** / bruto~**1.43×** / pnl DROP **−19%** · **NBSW** EVERY-10 primary (bruto DROP **0.45m** empty omzet / pnl DROP **−29%** / equity JUMP **+8.5%** / FTE **8.8**; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024) · AIESH / REW YE2024-only · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs FOI-ready.

"""
# keep prior snapshots after new snap
marker = "## Snapshot at **tick 2210**"
if marker not in old:
    raise SystemExit("2210 marker missing")
# replace file header through 2210 marker with new snap + 2210 onwards
idx = old.index(marker)
prog.write_text(snap + old[idx:], encoding="utf-8")

waste = """# DOGE waste ranking — current top 10

**As-of:** tick **2220** (2026-08-26) · **8033+** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt AGB / scoring anomalies with pi>10 excluded**  
**Formula:** `0.55·cost_score + 0.35·absurdity + 0.10·(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK encours public report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** | Strong CoA ch6-8: no public exec report |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 bench1 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | Strong climat.be 4e inv: direct 13.268bn |
| 3 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB 2025 strong: 4.7bn rising to 5.2bn |
| 4 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | Strong: 10536m of 13268m direct; gas pro |
| 5 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS bench1 total 1836.4m 2024 (lowS) |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA 2024 private parafiscal 1.07bn strong |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 vs ordinary SSC gap >1bn by 2026 | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | Strong CoA: gap CO2 receipts vs ordinary |
| 8 | `lb_dual_cars_ssc_taxex` | Dual company car CO2 SSC under-collection vs taxex | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** | Strong dual: SSC CO2 278m + cum gap |
| 9 | `lb_oaa_consol_reporte_300_6m` | OAA+missions reporté solde shift +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA: consol solde 34 to +300.6 |
| 10 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporté wave systemic 2026 | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA wave: OAA consol reporté |

**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  
**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2211-2220:** **OptimaT omzet 11.92m / bruto~3.54× / equity 39.4m** · **Odas 11.34m** · **Opnieuw & Co 6.45m** · **NBSW bruto 0.45m empty omzet / pnl DROP −29%** (EVERY-10@2220 primary) · **Werkmmaat / Veerkracht4 empty-omzet JUMP** · prior 2201-2210 Entiris/ACG/Oesterbank stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia/Enodia/RESA · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2210:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2211-2220 (off pure top10 / dual):** Werkhuizen MIN · Ecoso · Odas · OptimaT · Groep Maatwerk · Constructief · Kringloop · Werkmmaat · Veerkracht4 · Opnieuw · **NBSW bruto DROP 0.45m / empty omzet / pnl DROP −29%** (EVERY-10@2220 primary). Count NEW since 2210: ~11 residual dual fills. **Prior 2201-2210 + 2191-2200 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **OptimaT** omzet **EUR11.92m** / bruto **~3.54×** / equity JUMP **EUR39.4m** / FTE **788.8**.
- **Odas** omzet **EUR11.34m** / bruto **~1.72×** / pnl LOSS NARROW.
- **Opnieuw & Co** omzet JUMP **EUR6.45m** / bruto **~1.43×** / pnl DROP **−19%** / FTE **205.3** / **9 VE**.
- **NBSW** EVERY-10 primary bruto DROP **EUR0.45m** / omzet unpublished / pnl DROP **−29%** / equity JUMP **+8.5%** / FTE **8.8** — Hasselt boomgaard maatwerk subsidy opacity.
- **Werkmmaat** empty omzet / bruto **EUR3.24m** / pnl JUMP **+602%**.
- **Veerkracht 4** empty omzet / bruto **EUR3.76m** / pnl JUMP **+72%**.
- **Ecoso** pnl DROP **−95%** / **17 VE**.
- **Entiris** omzet **EUR18.93m** / equity **EUR92.3m** (prior retained).
- **ACG** omzet DROP **EUR7.49m** / bruto **~1.89×** (prior retained).
- **De Schakel Balen** bruto **~7.3×** omzet (prior retained).
- Walloon **ZS** stack FTE-only budget opacity.
"""
(DATA / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")

# --- sources ---
s_fields, sources = read_csv("sources.csv")
for sid, title, url, publisher, sclass, notes in [
    (
        "src_nbsw_jr2025_cw_nl",
        "Companyweb NL NBSW YE2025 statutory",
        "https://www.companyweb.be/nl/0479456845/natuur-en-boomgaarden-sociale-werkplaats",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; YE2025 omzet empty; bruto DROP {BR25} (-5.16%) pnl DROP {PN25} (-29.07%) equity JUMP {EQ25} (+8.54%) FTE {FTE25}; filed 26-05-2026",
    ),
    (
        "src_nbsw_jr2025_cw_en",
        "Companyweb EN NBSW YE2025 statutory",
        "https://www.companyweb.be/en/0479456845/natuur-en-boomgaarden-sociale-werkplaats",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; EN mirror YE2025 Medium; filed 26-05-2026; Turnover unpublished; Gross margin {BR25}; Profit/Loss {PN25}; Equity {EQ25}; Employees {FTE25}",
    ),
    (
        "src_nbsw_jr2025_cw_fr",
        "Companyweb FR NBSW YE2025 statutory",
        "https://www.companyweb.be/fr/0479456845/natuur-en-boomgaarden-sociale-werkplaats",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025; CA non publie; Marge brute {BR25}; Benefice {PN25}; Capitaux propres {EQ25}; Effectifs {FTE25}",
    ),
    (
        "src_nbsw_kbo_2220",
        "KBO NBSW 0479.456.845 Actief VZW Hasselt/Vliermaal 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0479456845",
        "KBO FOD Economie",
        "official_register",
        "tick2220; Actief VZW sinds 24.01.2003; zetel Leopold III-straat 8 3724 Hasselt; 1 VE; RSZ NACE 88.993; tel 003212391188",
    ),
    (
        "src_nbsw_site_contact_2220",
        "NBSW FOI channel via NBS info@boomgaardenstichting.be",
        "https://www.boomgaardenstichting.be/",
        "Nationale Boomgaardenstichting / NBSW dual",
        "foi_contact",
        "tick2220; info@boomgaardenstichting.be (sister NBS same address); Leopold III-straat 8 3724 Vliermaal/Hasselt; tel 012 39 11 88",
    ),
]:
    upsert(
        sources,
        "source_id",
        sid,
        {
            "source_id": sid,
            "title": title,
            "url": url,
            "publisher": publisher,
            "accessed_date": "2026-08-26",
            "source_class": sclass,
            "notes": notes,
        },
    )
write_csv("sources.csv", s_fields, sources)

# --- entities ---
e_fields, entities = read_csv("entities.csv")
upsert(
    entities,
    "entity_id",
    ENTITY,
    {
        "entity_id": ENTITY,
        "name_nl": "NBSW / Natuur- en Boomgaarden Sociale Werkplaats VZW (Hasselt)",
        "name_fr": "NBSW ASBL (Hasselt / entreprise de travail adapté / vergers)",
        "name_en": "NBSW sheltered orchard workshop (Hasselt/Vliermaal; maatwerk)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.boomgaardenstichting.be/",
        "foi_email": "info@boomgaardenstichting.be",
        "foi_postal": "Leopold III-straat 8, 3724 Hasselt (Vliermaal)",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0479.456.845 Actief VZW 1 VE "
            f"RSZ NACE 88.993; bruto DROP {BR25} empty omzet pnl DROP {PN25} equity JUMP {EQ25} "
            f"FTE {FTE25}; sister of Nationale Boomgaardenstichting; assets/debt Unknown"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

# --- budgets ---
b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_nbsw_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge / Gross margin YE2025 (omzet unpublished)",
        f"tick{TICK}; Medium CW; bruto DROP -5.16% vs YE2024 {BR24}; primary envelope",
    ),
    (
        "bud_nbsw_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst / Profit-Loss after tax YE2025",
        f"tick{TICK}; Medium CW; pnl DROP -29.07% vs YE2024 {PN24}",
    ),
    (
        "bud_nbsw_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen / Equity YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +8.54% vs YE2024 {EQ24}",
    ),
    (
        "bud_nbsw_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE / Employees 8.8",
        f"tick{TICK}; Medium CW; FTE {FTE25}; YE2024 FTE Unknown on free CW; assets/debt Unknown",
    ),
    (
        "bud_nbsw_bruto_jr2024_statutory_cmp",
        "2024",
        BR24,
        "CW statutory bruto_marge YE2024 comparative",
        f"tick{TICK}; YE2024 bruto {BR24} comparative",
    ),
]:
    upsert(
        budgets,
        "budget_id",
        bid,
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": year,
            "amount_eur": str(amt),
            "amount_min_eur": str(amt),
            "amount_max_eur": str(amt),
            "basis": basis,
            "source_id": "src_nbsw_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

# --- commitments ---
c_fields, commitments = read_csv("commitments.csv")
cash = (
    f'{{"2025_omzet":null,"2025_bruto":{BR25},"2025_pnl":{PN25},"2025_equity":{EQ25},'
    f'"2025_fte":{FTE25},"2024_omzet":null,"2024_bruto":{BR24},"2024_pnl":{PN24},'
    f'"2024_equity":{EQ24},"2024_fte":null}}'
)
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            "NBSW Hasselt YE2025 leftover dual (bruto DROP 0.45m / empty omzet / "
            "pnl DROP -29% / equity JUMP +8.5% / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "maatwerkers / boomgaard clients Limburg / NBS sister dual",
        "legal_basis": "VZW maatwerk (KBO 0479.456.845; Actief; 1 VE; RSZ NACE 88.993)",
        "decision_date": "2026-05-26",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0479456845/natuur-en-boomgaarden-sociale-werkplaats",
        "stated_goal": "Sheltered orchard/nature employment maatwerk Hasselt",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; disclose empty omzet vs bruto 0.45m "
            "loonkost/GESCO/ESF/VDAB/gemeente/NBS related-party split + pnl DROP -29%"
        ),
        "source_id": "src_nbsw_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>Limburg>Hasselt>NBSW>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK} EVERY-10; Medium CW; bruto primary (omzet empty); pnl DROP -29.07%; "
            f"equity JUMP +8.54%; FTE {FTE25}; 1 VE; assets/debt Unknown; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; not TE-additive of 348bn"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# --- leaderboard ---
l_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            "NBSW bruto DROP 0.45m / empty omzet / pnl DROP -29% / equity JUMP +8.5% (YE2025)"
        ),
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Vlaanderen>Limburg>Hasselt>NBSW>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto DROP envelope {BR25} (omzet unpublished) / pnl DROP {PN25} -29% from "
            f"YE2024 {PN24} / equity JUMP {EQ25} +8.5% / FTE {FTE25} / 1 VE"
        ),
        "confidence": "medium",
        "source_id": "src_nbsw_jr2025_cw_en",
        "beneficiaries": "maatwerkers Hasselt / NBS boomgaard dual / public loonkost path",
        "stated_goal": "Sheltered orchard/nature employment",
        "measured_outcome": (
            "bruto DROP -5.16%; omzet unpublished; pnl DROP -29.07%; equity JUMP +8.54%; "
            f"FTE {FTE25}"
        ),
        "absurdity_score": "7.2",
        "cost_score": "1.5",
        "difficulty": "3.0",
        "priority_index": "4.05",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose empty omzet vs bruto 0.45m "
            "loonkost/GESCO/ESF/VDAB/gemeente/NBS related-party split; pnl DROP -29% path"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} EVERY-10 primary; Medium CW; FOI {GAP}; stall FARO/REW YE2024; "
            "AGB Bornem JR2024; next every-10 2230"
        ),
    },
)
write_csv("leaderboard.csv", l_fields, leaderboard)

# --- foi ---
f_fields, foi = read_csv("foi_queue.csv")
upsert(
    foi,
    "gap_id",
    GAP,
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Vlaanderen>Limburg>Hasselt>NBSW>NBB_PDF_assets_debt_empty_omzet_bruto_drop_pnl_drop_equity_jump"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); why omzet unpublished "
            f"while bruto EUR{BR25} published; pnl DROP EUR{PN25} vs YE2024 EUR{PN24} (-29.07%); "
            f"equity JUMP EUR{EQ25} (+8.54%); NBS related-party transfers"
        ),
        "why_it_matters": (
            f"Medium CW shows Hasselt boomgaard maatwerk VZW (bruto 0.45m / {FTE25} FTE / 1 VE) "
            "with omzet empty, pnl DROP -29% and equity JUMP +8.5% under public loonkost + NBS "
            "sister dual — assets/debt still Unknown"
        ),
        "priority": "8",
        "recipient_body": "NBSW VZW / Nationale Boomgaardenstichting (sister dual)",
        "recipient_email": "info@boomgaardenstichting.be",
        "recipient_postal": "Leopold III-straat 8, 3724 Hasselt (Vliermaal)",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": "2026-08-26",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK} EVERY-10; ready NOT sent; Medium CW + Strong KBO; stall FARO/REW YE2024; "
            "AGB Bornem JR2024; next every-10 2230"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

# --- research queue ---
r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2220",
    {
        "task_id": "rq_2220",
        "title": (
            "EVERY-10 + leftover dual — NBSW YE2025 Medium (bruto DROP 0.45m / empty omzet / "
            "pnl DROP -29% / equity JUMP +8.5%)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "Completed EVERY-10@2220 + leftover NBSW after Opnieuw; preferred AGB Bornem JR2024 / "
            "FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent; "
            "progress+top10 refreshed"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T18:35:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; bruto {BR25} pnl {PN25} equity {EQ25} FTE {FTE25}; 1 VE Hasselt; "
            "progress@2220 done"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2221",
    {
        "task_id": "rq_2221",
        "title": (
            "leftover dual hole-fill after NBSW EVERY-10 — prefer AGB/FARO-YE2025/AIESH-REW/"
            "unused maatwerk-WZC-IGS"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick after EVERY-10@2220 NBSW Hasselt YE2025 Medium (bruto DROP 0.45m / empty omzet / "
            "pnl DROP -29% / equity JUMP +8.5%). Prefer leftover AGB/APB if JR2025 PDF live, else "
            "FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS/DSO. "
            "Do NOT redo NBSW, Opnieuw & Co, Veerkracht 4, Werkmmaat, Constructief, Kringloopwinkel "
            "Deltagroep, Groep Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, "
            "Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De "
            "Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, "
            "Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, "
            "Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De "
            "Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, "
            "Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, "
            "Cur@-Z, Het Dorp, De Vlietoever, NLZ, Mobiel, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK "
            "CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
            "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
            "Next EVERY-10 at 2230."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2220 EVERY-10 NBSW; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; "
            "next every-10 2230"
        ),
    },
)
write_csv("research_queue.csv", r_fields, rq)

# --- loop_state ---
ls_fields, ls = read_csv("loop_state.csv")
ls[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": UTC,
    "last_unit_id": "rq_2220",
    "ticks_completed": "2220",
    "paused": "no",
    "notes": (
        f"tick2220 EVERY-10 + leftover NBSW 0479.456.845 Medium (bruto DROP {BR25}; omzet empty; "
        f"pnl DROP {PN25} -29.07%; equity JUMP {EQ25} +8.54%; FTE {FTE25}; 1 VE Hasselt); "
        "progress+top10 refreshed; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2221; "
        "next every-10 2230; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)

print("OK tick2220 EVERY-10 + NBSW written")

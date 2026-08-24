# tick2240 — EVERY-10 + Axedis YE2025 Medium leftover dual (FREE Walloon ETA Brabant wallon)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_axedis_wavre"
TICK = "2240"
UTC = "2026-08-27T02:05:00Z"
GAP = "gap_axedis_nbb_pdf_assets_debt_bruto_gt_omzet_1_89x_fte_drop_eta_matrix_l5"
COMM = "comm_axedis_jr2025_statutory_eta_bruto_gt_omzet_fte_drop"
LB = "lb_axedis_bruto_4_55m_gt_omzet_1_89x_fte_drop_jr2025"

OM25, OM24 = 2408882, 2392511
BR25, BR24 = 4551309, 4459071
PN25, PN24 = 79804, 71534
EQ25, EQ24 = 2163267, 2092756
FTE25, FTE24 = 162.9, 167.8
RATIO = round(BR25 / OM25, 2)  # ~1.89


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


# --- EVERY-10 progress + top10 ---
progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2240** (2026-08-27)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2231-2240 continuum; AGB Bornem / FARO / AIESH / REW still YE2024 stalls; Heropbeuring CW opaque |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2231-2240 is residual dual L5 (not near-complete of 348bn):** **De Vleugels** bruto **35.11m** / ~**7.37×** · **SDB** omzet **9.36m** / pnl PROFIT FLIP · **Le Rucher** bruto **7.62m** / ~**2.03×** / pnl LOSS FLIP · **Ateliers de Tertre** omzet **10.00m** / pnl DROP **-97%** · **Het Rekreatief** bruto **2.42m** / empty omzet / pnl PROFIT FLIP · **Entra** omzet **28.61m** / bruto **35.33m** / FTE **885** · **L'Entraide Enghien** bruto **4.63m** / ~**1.96×** / equity JUMP **+77%** · **EntrAnam** bruto **7.66m** / ~**1.83×** / pnl LOSS DEEPEN · **Metalgroup** bruto **6.62m** / ~**2.22×** / pnl DROP **-69%** · **Manufast** bruto **6.25m** / ~**1.87×** / pnl LOSS FLIP / equity DROP **-27%** · EVERY-10 primary **Axedis** bruto **4.55m** / ~**1.89×** / FTE DROP **162.9** (Medium CW) |
| **E. FOI-ready gaps** | **~1891** drafts ready | Human send only; answered **~11**; partial **~28**; total FOI rows **~1943** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability/maatwerk shells** (**NEW 2231-2240** De Vleugels · SDB · Le Rucher · Ateliers de Tertre · Het Rekreatief · Entra · Enghien · EntrAnam · Metalgroup · Manufast · **Axedis** · prior 2221-2230 Manus/Kringwinkel/ViTeS/Kiemkracht/Travie/De Oever stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2240)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 53405+ |
| commitments.csv | 5940+ |
| leaderboard.csv | 8061+ |
| entities.csv | 1970+ |
| sources.csv | 6260+ |
| FOI ready | ~1891 |
| FOI answered | 11 |
| FOI partial | 28 |
| FOI total rows | ~1943 |
| research_queue open | rq_2241 after Axedis EVERY-10 |

### What improved since tick 2230

- **Residual dual (tick2231-2240):** **De Vleugels** (bruto **35.11m** ~**7.37×**) · **SDB** (omzet **9.36m** / pnl PROFIT FLIP) · **Le Rucher** (bruto **7.62m** ~**2.03×** / pnl LOSS FLIP) · **Ateliers de Tertre** (omzet **10.00m** / pnl DROP **-97%**) · **Het Rekreatief** (bruto **2.42m** / empty omzet / pnl PROFIT FLIP) · **Entra** (omzet **28.61m** / FTE **885**) · **L'Entraide Enghien** (bruto **4.63m** / equity JUMP **+77%**) · **EntrAnam** (bruto **7.66m** / pnl LOSS DEEPEN) · **Metalgroup** (bruto **6.62m** ~**2.22×** / pnl DROP **-69%**) · **Manufast** (bruto **6.25m** ~**1.87×** / pnl LOSS FLIP / equity DROP **-27%**) · EVERY-10 primary **Axedis** (omzet **2.41m** / bruto **4.55m** ~**1.89×** / pnl **79.8k** / equity **2.16m** / FTE DROP **162.9**; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024; narrative JV2025 only) · AIESH / REW YE2024-only · Heropbeuring CW kern opaque · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs FOI-ready.
"""
(DATA / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")

top10 = f"""# DOGE waste ranking — current top 10

**As-of:** tick **2240** (2026-08-27) · **8061+** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2231-2240:** **Axedis bruto 4.55m / ~1.89× / FTE DROP 162.9** (EVERY-10@2240 primary) · **Manufast bruto 6.25m / ~1.87× / pnl LOSS FLIP / equity DROP −27%** · **Metalgroup bruto 6.62m / ~2.22× / pnl DROP −69%** · **EntrAnam bruto 7.66m / ~1.83× / pnl LOSS DEEPEN** · **Entra omzet 28.61m / FTE 885** · **Ateliers de Tertre pnl DROP −97%** · **Le Rucher pnl LOSS FLIP** · **De Vleugels bruto 35.11m / ~7.37×** · prior 2221-2230 Kiemkracht/Travie/ViTeS/De Oever/Manus stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia/Enodia/RESA · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2230:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). Tie-break among pi=8.5 puts fossil accises ahead of company cars by annual €; among pi=8.4 dual cars falls to #10 by annual €. **Major NEW residual 2231-2240 (off pure top10 / dual):** De Vleugels · SDB · Le Rucher · Ateliers de Tertre · Het Rekreatief · Entra · Enghien · EntrAnam · Metalgroup · Manufast · **Axedis bruto JUMP 4.55m / bruto≫omzet ~1.89x / FTE DROP 162.9** (EVERY-10@2240 primary). Count NEW since 2230: ~11 residual dual fills. **Prior 2221-2230 + 2211-2220 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Axedis** EVERY-10 primary bruto **EUR4.55m** / omzet **EUR2.41m** (~**1.89×**) / FTE DROP **162.9** — Brabant wallon ETA subsidy opacity.
- **Manufast** bruto **EUR6.25m** / omzet **EUR3.34m** (~**1.87×**) / pnl LOSS FLIP **-300k** / equity DROP **-27%**.
- **Metalgroup** bruto **EUR6.62m** / omzet **EUR2.99m** (~**2.22×**) / pnl DROP **-69%**.
- **EntrAnam** bruto **EUR7.66m** / omzet **EUR4.20m** (~**1.83×**) / pnl LOSS DEEPEN **-301k**.
- **Entra** omzet **EUR28.61m** / bruto **EUR35.33m** / FTE **885.2**.
- **Ateliers de Tertre** omzet **EUR10.00m** / pnl DROP **-97%**.
- **Le Rucher** bruto **EUR7.62m** / ~**2.03×** / pnl LOSS FLIP.
- **De Vleugels** bruto **EUR35.11m** / omzet **EUR4.77m** (~**7.37×**) / equity **EUR35.35m**.
- **Kiemkracht** omzet JUMP **EUR13.26m** / bruto≫omzet **~1.41x** / pnl DROP **-75%** (prior retained).
- **Travie** bruto **EUR11.39m** / ~**2.84×** / pnl DROP **−89%** (prior retained).
- **ViTeS Leuven** omzet **EUR14.04m** / FTE **529.8** (prior retained).
- Walloon **ZS** stack FTE-only budget opacity.
"""
(DATA / "doge_waste_top10_current.md").write_text(top10, encoding="utf-8")

# --- sources ---
s_fields, sources = read_csv("sources.csv")
for sid, title, url, publisher, sclass, notes in [
    (
        "src_axedis_jr2025_cw_nl",
        "Companyweb NL Axedis YE2025 statutory",
        "https://www.companyweb.be/nl/0465786674/axedis",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+0.68%) bruto JUMP {BR25} (+2.07% "
            f"bruto≫omzet ~{RATIO}x) pnl JUMP {PN25} (+11.56%) equity JUMP {EQ25} (+3.37%) "
            f"FTE DROP {FTE25}; filed 23-06-2026"
        ),
    ),
    (
        "src_axedis_jr2025_cw_en",
        "Companyweb EN Axedis YE2025 statutory",
        "https://www.companyweb.be/en/0465786674/axedis",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 23-06-2026"
        ),
    ),
    (
        "src_axedis_jr2025_cw_fr",
        "Companyweb FR Axedis YE2025 statutory",
        "https://www.companyweb.be/fr/0465786674/axedis",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Bénéfice {PN25}",
    ),
    (
        "src_axedis_kbo_2240",
        "KBO Axedis 0465.786.674 Actief Wavre 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0465786674",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2240; Actief VZW/ASBL AXEDIS; zetel Rue de la Station 13 1300 Wavre; "
            "1 VE; NACE RSZ/BTW 88.993; Walloon Brabant ETA (Limal site)"
        ),
    ),
    (
        "src_axedis_site_contact_2240",
        "Axedis FOI channel info@axedis-eta.be",
        "https://www.axedis-eta.be/contact",
        "Axedis ASBL",
        "foi_contact",
        "tick2240; info@axedis-eta.be / commercial@axedis-eta.be; +32 10 43 53 53; Rue de la Station 13 1300 Wavre",
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
            "accessed_date": "2026-08-27",
            "source_class": sclass,
            "notes": notes,
        },
    )
write_csv("sources.csv", s_fields, sources)

e_fields, entities = read_csv("entities.csv")
upsert(
    entities,
    "entity_id",
    ENTITY,
    {
        "entity_id": ENTITY,
        "name_nl": "Axedis VZW (Wavre-Limal / ETA maatwerk Brabant wallon)",
        "name_fr": "Axedis ASBL (Wavre-Limal / entreprise de travail adapté)",
        "name_en": "Axedis adapted-work ASBL (Wavre-Limal Walloon Brabant ETA)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.axedis-eta.be/",
        "foi_email": "info@axedis-eta.be",
        "foi_postal": "Rue de la Station 13, 1300 Wavre",
        "notes": (
            f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0465.786.674 Actief 1 VE "
            f"NACE 88.993; omzet JUMP {OM25} bruto {BR25} (~{RATIO}x) pnl JUMP {PN25} equity JUMP "
            f"{EQ25} FTE DROP {FTE25}; neerlegging 23.06.2026; assets/debt Unknown; FOI {GAP}; "
            "preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "after Manufast@2239; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_axedis_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto JUMP +2.07% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_axedis_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +0.68% vs YE2024 {OM24}",
    ),
    (
        "bud_axedis_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl JUMP +11.56% vs YE2024 {PN24}",
    ),
    (
        "bud_axedis_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +3.37% vs YE2024 {EQ24}",
    ),
    (
        "bud_axedis_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 162.9",
        f"tick{TICK}; Medium CW; FTE DROP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_axedis_fte_jr2024_statutory_cmp",
        "2024",
        FTE24,
        "CW social-balance FTE YE2024 comparative",
        f"tick{TICK}; YE2024 FTE {FTE24} comparative (pre DROP)",
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
            "source_id": "src_axedis_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

c_fields, commitments = read_csv("commitments.csv")
cash = (
    f'{{"2025_bruto":{BR25},"2025_omzet":{OM25},"2025_pnl":{PN25},"2025_equity":{EQ25},'
    f'"2025_fte":{FTE25},"2024_bruto":{BR24},"2024_omzet":{OM24},"2024_pnl":{PN24},'
    f'"2024_equity":{EQ24},"2024_fte":{FTE24}}}'
)
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            "Axedis YE2025 leftover dual EVERY-10 (bruto 4.55m / bruto≫omzet ~1.89x / "
            "FTE DROP 162.9 / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Brabant wallon (Wavre-Limal) / AVIQ adapted-work public path",
        "legal_basis": (
            "ASBL ETA Axedis (KBO 0465.786.674; Actief; 1 VE; NACE 88.993; Walloon Brabant)"
        ),
        "decision_date": "2026-06-23",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0465786674/axedis",
        "stated_goal": "Walloon Brabant ETA industrial subcontracting / assembly",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~1.89x; reconcile FTE DROP "
            "162.9 vs modest pnl/equity JUMP with AVIQ ETA subsidy matrix"
        ),
        "source_id": "src_axedis_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>BrabantWallon>Wavre>Axedis>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"FTE DROP {FTE25}; 1 VE; after Manufast@2239; AGB Bornem JR2024; FARO/AIESH/REW "
            "YE2024; Heropbeuring CW opaque; not TE-additive"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

l_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            "Axedis bruto 4.55m / bruto≫omzet ~1.89x / FTE DROP 162.9 (YE2025 Walloon Brabant ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Wallonie>BrabantWallon>Wavre>Axedis>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet {OM25} (~{RATIO}x) / pnl JUMP {PN25} / equity JUMP "
            f"{EQ25} / FTE DROP {FTE25} / 1 VE Walloon Brabant ETA"
        ),
        "confidence": "medium",
        "source_id": "src_axedis_jr2025_cw_en",
        "beneficiaries": "ETA workers Brabant wallon / AVIQ adapted-work public path",
        "stated_goal": "Walloon Brabant ETA industrial subcontracting",
        "measured_outcome": (
            f"omzet JUMP +0.68%; bruto≫omzet ~{RATIO}x; pnl JUMP +11.56%; equity JUMP +3.37%; "
            f"FTE DROP {FTE25}; filed 23.06.2026"
        ),
        "absurdity_score": "7.2",
        "cost_score": "5.2",
        "difficulty": "3.0",
        "priority_index": "6.10",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~1.89x vs AVIQ ETA "
            "matrix; reconcile FTE DROP vs pnl/equity JUMP"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} EVERY-10 primary; Medium CW; FOI {GAP}; stall Heropbeuring CW opaque / "
            "FARO YE2024 / AIESH YE2024 / REW YE2024; AGB Bornem JR2024; after Manufast@2239; "
            "next every-10 2250"
        ),
    },
)
write_csv("leaderboard.csv", l_fields, leaderboard)

f_fields, foi = read_csv("foi_queue.csv")
upsert(
    foi,
    "gap_id",
    GAP,
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>BrabantWallon>Wavre>Axedis>NBB_PDF_assets_debt_bruto_gt_omzet_fte_drop"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x); FTE DROP {FTE25} vs YE2024 {FTE24}; AVIQ ETA "
            f"subsidy matrix behind bruto {BR25}"
        ),
        "why_it_matters": (
            f"Medium CW shows Walloon Brabant ETA ASBL (bruto 4.55m / omzet 2.41m / ~{RATIO}x / "
            f"FTE DROP {FTE25}) under AVIQ path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "Axedis ASBL",
        "recipient_email": "info@axedis-eta.be",
        "recipient_postal": "Rue de la Station 13, 1300 Wavre",
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
        "notes": (
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/"
            "REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; next every-10 2250"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — Axedis (NBB PDF / bruto≫omzet ~{RATIO}x / FTE DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Axedis ASBL — KBO **0465.786.674** (Actief; Rue de la Station 13, 1300 Wavre; **1 VE**; FTE {FTE25} CW; NACE **88.993**; Walloon Brabant ETA Limal)  
**recipient:** info@axedis-eta.be · Rue de la Station 13, 1300 Wavre  
**sources:** [CW EN](https://www.companyweb.be/en/0465786674/axedis) · [CW NL](https://www.companyweb.be/nl/0465786674/axedis) · [CW FR](https://www.companyweb.be/fr/0465786674/axedis) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0465786674) · [site](https://www.axedis-eta.be/)  
**tick:** {TICK} EVERY-10  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL; **1 VE**; zetel Rue de la Station Wavre; NACE **88.993**.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +0.68% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +2.07% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** JUMP +11.56%; equity **EUR{EQ25:,}** JUMP +3.37%; FTE **{FTE25}** DROP vs {FTE24}; filed **23.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After Manufast@2239. EVERY-10@2240 primary.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Axedis ASBL
via info@axedis-eta.be
Rue de la Station 13, 1300 Wavre
Objet: Publicité des comptes annuels 2025 Axedis (BCE 0465.786.674)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. FTE DROP {FTE25} vs YE2024 {FTE24} — réconciliation avec pnl/equity JUMP.
4. Matrice des subsides AVIQ / ETA derrière la marge brute EUR{BR25}.
5. Répartition coûts site Limal / sous-traitance industrielle.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2240",
    {
        "task_id": "rq_2240",
        "title": (
            "EVERY-10 + leftover dual — Axedis YE2025 Medium (bruto 4.55m / bruto≫omzet ~1.89x / "
            "FTE DROP 162.9)"
        ),
        "sprint": "hole_fill",
        "priority": "10",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "EVERY-10 progress+top10 then leftover dual Axedis YE2025 FREE Walloon ETA",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T01:45:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; EVERY-10 refreshed; Axedis 0465.786.674 YE2025 Medium CW; bruto {BR25} "
            f"(~{RATIO}x omzet {OM25}) pnl JUMP {PN25} equity JUMP {EQ25} FTE DROP {FTE25}; "
            "1 VE Walloon Brabant ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring "
            "CW opaque; after Manufast@2239; next rq_2241; next EVERY-10 2250; do NOT redo "
            "Manufast/Metalgroup/EntrAnam/Enghien/Entra/Ateliers/Rekreatief/Axedis"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2241",
    {
        "task_id": "rq_2241",
        "title": (
            "leftover dual after Axedis — prefer AGB/FARO-YE2025/AIESH-REW/Heropbeuring-or-unused "
            "ETA-VAPH-WZC-maatwerk"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "leftover dual after Axedis YE2025 Medium (bruto 4.55m / bruto≫omzet ~1.89x / FTE DROP "
            "162.9). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
            "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else unused "
            "ETA/VAPH/WZC/maatwerk (e.g. ETA 123 Beauraing / Jean Gielen / Le Perron / IN-Z if "
            "FREE). Do NOT redo Axedis, Manufast, Metalgroup, EntrAnam, Enghien, Entra, Ateliers "
            "de Tertre, Le Rucher, Het Rekreatief, Travie, SDB, De Vleugels, Kiemkracht, De Oever, "
            "ViTeS*, Kringwinkel*, Manus*, Reset, Den Azalee, Kemphaan. Next EVERY-10: 2250."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2240 EVERY-10 + Axedis; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; next every-10 2250"
        ),
    },
)
write_csv("research_queue.csv", r_fields, rq)

ls_fields, ls = read_csv("loop_state.csv")
ls[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": UTC,
    "last_unit_id": "rq_2240",
    "ticks_completed": "2240",
    "paused": "no",
    "notes": (
        f"tick2240 EVERY-10 + leftover Axedis 0465.786.674 Medium (bruto {BR25} ~{RATIO}x omzet "
        f"{OM25}; pnl JUMP {PN25}; equity JUMP {EQ25}; FTE DROP {FTE25}; 1 VE Walloon Brabant "
        "ETA); after Manufast@2239; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW "
        "opaque; next rq_2241; next EVERY-10 2250; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)

log_block = f"""

## Tick 2240 - 2026-08-27T02:05:00Z - EVERY-10 + rq_2240 Axedis Wavre-Limal (bruto 4.55m / bruto≫omzet ~1.89x / FTE DROP 162.9 / Medium)

- **EVERY-10:** refreshed `progress_every_10_ticks.md` (A **100%** / B **100%** / C **~99%** / D **~74-88%** generous residual dual / E **~1891** FOI-ready) and `doge_waste_top10_current.md` (GIP #1; fossil/cars/cheque/reporté #2–10 stable; Axedis off pure top10). Next every-10: **2250**.
- Unit: **rq_2240** leftover dual after **rq_2239 Manufast**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (CW last balance 2024; JV2025 narrative only); AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took FREE unused Walloon Brabant ETA **Axedis ASBL** YE2025 (KBO **0465.786.674**; Rue de la Station 13 Wavre; **Actief** **1 VE**; NACE **88.993**). Do not redo Manufast/Metalgroup/EntrAnam/Enghien/Entra/Ateliers Tertre/Het Rekreatief/Le Rucher stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +0.68% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +2.07% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** JUMP +11.56% vs YE2024 EUR{PN24}; equity **EUR{EQ25}** JUMP +3.37%; FTE **{FTE25}** DROP vs {FTE24}; neerlegging **23.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@axedis-eta.be.
- Wrote: progress+top10; sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.10); entities (+1 vzw_axedis_wavre); foi + draft {GAP}; rq_2240=done + rq_2241 open; loop_state ticks=2240; raw docs/doge/raw/tick2240/.
- FOI: **ready not sent** (human-gated).
- EVERY-10 done. Next: rq_2241 (AGB/FARO-if-YE2025 / AIESH-REW / unused-ETA-VAPH-WZC-maatwerk). Next every-10 **2250**.
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(
    f"OK tick2240 EVERY-10 + Axedis bruto={BR25} omzet={OM25} ratio={RATIO} "
    f"pnl={PN25} equity={EQ25} FTE={FTE25}"
)

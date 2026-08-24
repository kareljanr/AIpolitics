# tick2230 — EVERY-10 progress + Travie YE2025 Medium leftover dual (maatwerk)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_travie_anderlecht"
TICK = "2230"
UTC = "2026-08-26T22:15:00Z"
GAP = "gap_travie_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_drop_89pct_matrix_l5"
COMM = "comm_travie_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_drop"
LB = "lb_travie_bruto_11_39m_omzet_4_01m_pnl_drop_89pct_jr2025"

OM25, OM24 = 4014674, 4199547
BR25, BR24 = 11394051, 11427981
PN25, PN24 = 36871, 345798
EQ25, EQ24 = 5979074, 6050049
FTE25, FTE24 = 496.0, 493.0
OM_PCT = round((OM25 / OM24 - 1) * 100, 2)  # -4.40
BR_PCT = round((BR25 / BR24 - 1) * 100, 2)  # -0.30
PN_PCT = round((PN25 / PN24 - 1) * 100, 2)  # -89.34
EQ_PCT = round((EQ25 / EQ24 - 1) * 100, 2)  # -1.17
RATIO = round(BR25 / OM25, 2)  # 2.84
# cost <100m → 5.5; abs 7.8 (bruto~2.84x + pnl DROP -89%); diff 3 → pi = 0.55*5.5+0.35*7.8+0.10*7 = 3.025+2.73+0.7 = 6.455 → 6.46
PI, ABS, COST, DIFF = "6.46", "7.8", "5.5", "3.0"


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


def count_csv(name: str) -> int:
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return sum(1 for _ in csv.DictReader(f))


# --- EVERY-10 progress ---
n_bud = count_csv("budgets.csv")
n_comm = count_csv("commitments.csv")
n_lb = count_csv("leaderboard.csv")
n_ent = count_csv("entities.csv")
n_src = count_csv("sources.csv")
_, foi_rows = read_csv("foi_queue.csv")
foi_ready = sum(1 for r in foi_rows if (r.get("status") or "").strip() == "ready")
foi_ans = sum(1 for r in foi_rows if (r.get("status") or "").strip() == "answered")
foi_part = sum(1 for r in foi_rows if (r.get("status") or "").strip() == "partial")
foi_tot = len(foi_rows)

# after this tick (+1 foi ready, +budgets etc.) — write inventory post-write below; snapshot uses post-estimates
# Pre-write baseline for note; final inventory recomputed after appends.

prog_body = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2230** (2026-08-26)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2221-2230 continuum; AGB Bornem / FARO / AIESH / REW still YE2024 stalls; Heropbeuring CW opaque |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2221-2230 is residual dual L5 (not near-complete of 348bn):** Manus Antwerpen · Kringwinkel ZOV · Manus groep · Kringwinkel Maasland · Manus BXL · Kringwinkel West · Den Azalee · Reset · ViTeS · Kringwinkel Midwest · ViTeS BE · De Oever · **Travie** bruto **11.39m** / omzet **4.01m** (~**2.84×**) / pnl DROP **−89%** (EVERY-10 primary) Medium |
| **E. FOI-ready gaps** | **~{foi_ready + 1}** drafts ready | Human send only; answered **~{foi_ans}**; partial **~{foi_part}**; total FOI rows **~{foi_tot + 1}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability/maatwerk shells** (**NEW 2221-2230** Manus stack · Kringwinkel ZOV/Maasland/West/Midwest · Den Azalee · Reset · ViTeS · ViTeS BE · De Oever · **Travie** · prior 2211-2220 NBSW/Opnieuw/Werkmmaat/Deltagroep/OptimaT stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2230)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {n_bud}+ |
| commitments.csv | {n_comm}+ |
| leaderboard.csv | {n_lb}+ |
| entities.csv | {n_ent}+ |
| sources.csv | {n_src}+ |
| FOI ready | ~{foi_ready + 1} |
| FOI answered | {foi_ans} |
| FOI partial | {foi_part} |
| FOI total rows | ~{foi_tot + 1} |
| research_queue open | rq_2231 after progress |

### What improved since tick 2220

- **Residual dual (tick2221-2230):** Manus Antwerpen · Kringwinkel ZOV · Manus groep · Kringwinkel Maasland · Manus BXL · Kringwinkel West · Den Azalee · Reset Genk · ViTeS Leuven · Kringwinkel Midwest · ViTeS BE · De Oever Hasselt · **Travie** (EVERY-10 primary — omzet DROP **EUR4.01m (−4.4%)**; bruto **EUR11.39m** ~**2.84×** omzet; pnl DROP **EUR36.9k (−89.3%)**; equity DROP **EUR5.98m**; FTE JUMP **496**; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024) · AIESH / REW YE2024-only · Heropbeuring filed 25.06.2026 but CW kern opaque (FTE-only) · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs FOI-ready.

"""

(DATA / "progress_every_10_ticks.md").write_text(prog_body, encoding="utf-8")

# --- EVERY-10 top10 ---
top10 = f"""# DOGE waste ranking — current top 10

**As-of:** tick **2230** (2026-08-26) · **{n_lb}+** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2221-2230:** **Travie bruto 11.39m / ~2.84× omzet / pnl DROP −89%** (EVERY-10@2230 primary) · De Oever bruto 10.22m empty omzet pnl DROP −97% · ViTeS omzet 14.04m · Reset omzet 6.05m · Den Azalee omzet 4.66m · Kringwinkel Midwest LOSS FLIP · prior 2211-2220 OptimaT/Odas/NBSW/Opnieuw stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia/Enodia/RESA · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2220:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2221-2230 (off pure top10 / dual):** Manus Antwerpen · Kringwinkel ZOV · Manus groep · Kringwinkel Maasland · Manus BXL · Kringwinkel West · Den Azalee · Reset · ViTeS · Kringwinkel Midwest · ViTeS BE · De Oever · **Travie bruto 11.39m / ~2.84× / pnl DROP −89%** (EVERY-10 primary). Count NEW since 2220: ~13 residual dual fills. **Prior 2211-2220 + 2201-2210 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Travie** EVERY-10 primary bruto **EUR11.39m** / omzet **EUR4.01m** (~**2.84×**) / pnl DROP **−89.3%** / FTE **496** — Brussels maatwerk / ETA subsidy opacity.
- **De Oever** bruto **EUR10.22m** / empty omzet / pnl DROP **−96.9%** / FTE JUMP **126.9**.
- **ViTeS Leuven** omzet **EUR14.04m** / bruto **~1.71×** / pnl DROP **−30%** / FTE JUMP **529.8**.
- **Reset Genk** omzet **EUR6.05m** / bruto **~1.47×** / pnl DROP **−85%**.
- **Den Azalee** omzet **EUR4.66m** / bruto **~1.85×** / pnl DROP **−52%**.
- **Kringwinkel Midwest** omzet **EUR3.26m** / bruto **~1.64×** / pnl LOSS FLIP.
- **OptimaT** bruto **~3.54×** omzet / equity JUMP **EUR39.4m** (prior retained).
- **Odas** omzet **EUR11.34m** / bruto **~1.72×** (prior retained).
- **NBSW** bruto DROP **EUR0.45m** / pnl DROP **−29%** / omzet empty (prior retained).
- Walloon **ZS** stack FTE-only budget opacity.
"""
(DATA / "doge_waste_top10_current.md").write_text(top10, encoding="utf-8")

# --- sources ---
s_fields, sources = read_csv("sources.csv")
for sid, title, url, publisher, sclass, notes in [
    (
        "src_travie_jr2025_cw_nl",
        "Companyweb NL Travie YE2025 statutory",
        "https://www.companyweb.be/nl/0420015938/travie",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK} EVERY-10; YE2025 omzet DROP {OM25} ({OM_PCT}%) bruto {BR25} ({BR_PCT}%; ~{RATIO}x) pnl DROP {PN25} ({PN_PCT}%) equity DROP {EQ25} FTE JUMP {FTE25}; filed 10-07-2026",
    ),
    (
        "src_travie_jr2025_cw_en",
        "Companyweb EN Travie YE2025 statutory",
        "https://www.companyweb.be/en/0420015938/travie",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit {PN25}; Equity {EQ25}; Employees {FTE25}",
    ),
    (
        "src_travie_jr2025_cw_fr",
        "Companyweb FR Travie YE2025 statutory",
        "https://www.companyweb.be/fr/0420015938/travie",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Benefice {PN25}",
    ),
    (
        "src_travie_kbo_2230",
        "KBO Travie 0420.015.938 Actief Anderlecht 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0420015938",
        "KBO FOD Economie",
        "official_register",
        "tick2230; Actief VZW sinds 01.12.1979; zetel Vaartdijk 40 1070 Anderlecht; 1 VE; NACE 88.993/88.995 beschutte/sociale werkplaatsen / maatwerk",
    ),
    (
        "src_travie_site_contact_2230",
        "Travie FOI channel contact@travie.be",
        "https://travie.be/nl/contact/",
        "Travie VZW",
        "foi_contact",
        "tick2230; contact@travie.be; grh@travie.be; sales@travie.be; Vaartdijk 40 1070 Anderlecht",
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

# --- entity ---
e_fields, entities = read_csv("entities.csv")
upsert(
    entities,
    "entity_id",
    ENTITY,
    {
        "entity_id": ENTITY,
        "name_nl": "Travie VZW (Anderlecht / maatwerk / beschutte werkplaats)",
        "name_fr": "Travie ASBL (Anderlecht / ETA / atelier adapté)",
        "name_en": "Travie adapted-work enterprise (Anderlecht; Brussels maatwerk dual)",
        "level": "parastatal",
        "parent_id": "sec_brussels",
        "community_language": "bi",
        "website": "https://travie.be/",
        "foi_email": "contact@travie.be",
        "foi_postal": "Vaartdijk 40, 1070 Anderlecht",
        "notes": (
            f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0420.015.938 Actief 1 VE "
            f"NACE 88.993/88.995; omzet DROP {OM25} bruto {BR25} (~{RATIO}x) pnl DROP {PN25} ({PN_PCT}%) "
            f"FTE JUMP {FTE25}; Brussels maatwerk public euros; preferred AGB Bornem JR2024 / "
            "FARO/AIESH/REW YE2024 / Heropbeuring CW opaque"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

# --- budgets ---
b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_travie_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet DROP {OM_PCT}% vs YE2024 {OM24}",
    ),
    (
        "bud_travie_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025",
        f"tick{TICK}; Medium CW; bruto flat {BR_PCT}% vs YE2024 {BR24}; ~{RATIO}x omzet; primary envelope",
    ),
    (
        "bud_travie_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst YE2025",
        f"tick{TICK}; Medium CW; pnl DROP {PN_PCT}% vs YE2024 {PN24}",
    ),
    (
        "bud_travie_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity DROP {EQ_PCT}% vs YE2024 {EQ24}",
    ),
    (
        "bud_travie_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 496",
        f"tick{TICK}; Medium CW; FTE JUMP vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_travie_bruto_jr2024_statutory_cmp",
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
            "source_id": "src_travie_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

# --- commitments ---
c_fields, commitments = read_csv("commitments.csv")
cash = (
    f'{{"2025_omzet":{OM25},"2025_bruto":{BR25},"2025_pnl":{PN25},"2025_equity":{EQ25},'
    f'"2025_fte":{FTE25},"2024_omzet":{OM24},"2024_bruto":{BR24},"2024_pnl":{PN24},'
    f'"2024_equity":{EQ24},"2024_fte":{FTE24}}}'
)
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            "Travie Anderlecht YE2025 leftover dual (bruto 11.39m / ~2.84x omzet / "
            "pnl DROP -89% / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "maatwerkers Brussels / ETA clients / public loonkost path",
        "legal_basis": "VZW maatwerk/ETA (KBO 0420.015.938; Actief; 1 VE; NACE 88.993/88.995)",
        "decision_date": "2026-07-10",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0420015938/travie",
        "stated_goal": "Adapted work / ETA employment Brussels",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; disclose bruto~2.84x vs omzet 4.01m "
            "Phare/COCOF/Actiris/VDAB loonkost matrix; pnl DROP -89% path"
        ),
        "source_id": "src_travie_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Brussels>Anderlecht>Travie>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK} EVERY-10; Medium CW; bruto primary ~{RATIO}x omzet; pnl DROP {PN_PCT}%; "
            f"FTE JUMP {FTE25}; 1 VE; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW "
            "opaque; next every-10 2240; not TE-additive of 348bn"
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
            f"Travie bruto 11.39m / omzet 4.01m (~{RATIO}x) / pnl DROP -89% (YE2025)"
        ),
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Brussels>Anderlecht>Travie>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto envelope {BR25} / omzet {OM25} (~{RATIO}x) / pnl DROP {PN25} {PN_PCT}% "
            f"from {PN24} / equity {EQ25} / FTE JUMP {FTE25} / Brussels ETA maatwerk"
        ),
        "confidence": "medium",
        "source_id": "src_travie_jr2025_cw_en",
        "beneficiaries": "maatwerkers / ETA clients / public loonkost euros",
        "stated_goal": "Adapted work employment",
        "measured_outcome": (
            f"omzet DROP {OM_PCT}%; bruto~{RATIO}x; pnl DROP {PN_PCT}%; FTE JUMP {FTE25}; 1 VE"
        ),
        "absurdity_score": ABS,
        "cost_score": COST,
        "difficulty": DIFF,
        "priority_index": PI,
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose bruto~2.84x vs omzet 4.01m "
            "Phare/COCOF/Actiris loonkost matrix; pnl DROP -89% despite FTE JUMP"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall Heropbeuring CW opaque / FARO YE2024; "
            "AGB Bornem JR2024; EVERY-10 primary; next every-10 2240"
        ),
    },
)
write_csv("leaderboard.csv", l_fields, leaderboard)

# --- FOI queue + draft ---
f_fields, foi = read_csv("foi_queue.csv")
upsert(
    foi,
    "gap_id",
    GAP,
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Brussels>Anderlecht>Travie>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_drop_89pct"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x) reconciliatie; pnl DROP EUR{PN25} vs YE2024 EUR{PN24} "
            f"({PN_PCT}%); Phare/COCOF/Actiris/VDAB loonkost matrix"
        ),
        "why_it_matters": (
            f"Medium CW shows Brussels maatwerk/ETA VZW (bruto 11.39m / omzet 4.01m / {FTE25} FTE) "
            "with bruto~2.84x and pnl crater -89% under public adapted-work path — assets/debt "
            "still Unknown"
        ),
        "priority": "8",
        "recipient_body": "Travie VZW",
        "recipient_email": "contact@travie.be",
        "recipient_postal": "Vaartdijk 40, 1070 Anderlecht",
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
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; EVERY-10 primary; next every-10 2240"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — Travie Anderlecht (NBB PDF / bruto≫omzet / pnl DROP -89%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Travie VZW — KBO **0420.015.938** (Actief; Vaartdijk 40, 1070 Anderlecht; **1 VE**; FTE 496 CW; NACE **88.993/88.995**)  
**recipient:** contact@travie.be · Vaartdijk 40, 1070 Anderlecht  
**sources:** [CW EN](https://www.companyweb.be/en/0420015938/travie) · [CW NL](https://www.companyweb.be/nl/0420015938/travie) · [CW FR](https://www.companyweb.be/fr/0420015938/travie) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0420015938) · [travie.be](https://travie.be/nl/contact/)  
**tick:** 2230  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW sinds 01.12.1979; **1 VE**; zetel Vaartdijk 40 Anderlecht; NACE **88.993/88.995** (beschutte/sociale werkplaatsen / maatwerk / ETA).
- CW YE2025: omzet **EUR4,014,674** DROP -4.40% vs YE2024 EUR4,199,547; bruto **EUR11,394,051** flat -0.30% (bruto≫omzet ~**2.84x**); pnl **EUR36,871** DROP -89.34% vs YE2024 EUR345,798; equity **EUR5,979,074** DROP -1.17%; FTE **496** JUMP vs 493; filed **10.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Travie VZW
via contact@travie.be
Vaartdijk 40, 1070 Anderlecht
Betreft: Openbaarmaking jaarrekening 2025 Travie (KBO 0420.015.938)

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(federaal / Brussels Hoofdstedelijk Gewest) vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Reconciliatie bruto EUR11.394.051 vs omzet EUR4.014.674 (~2,84x) — subsidies / andere opbrengsten.
3. PnL DROP EUR36.871 vs YE2024 EUR345.798 (-89,34%) reconciliatie met FTE JUMP 493→496.
4. Phare / COCOF / Actiris / VDAB / federale loonkost-subsidie matrix achter bruto≫omzet.
5. Per-activiteit / atelier cost allocation (1 VE).

Periode YE2025 (+ YE2024 comparative). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

# --- research_queue ---
r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2230",
    {
        "task_id": "rq_2230",
        "title": (
            "EVERY-10 + leftover dual — Travie YE2025 Medium (bruto 11.39m / ~2.84x / "
            "pnl DROP -89%)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "Completed EVERY-10@2230 + leftover Travie after De Oever; preferred AGB Bornem "
            "JR2024 / FARO/AIESH/REW YE2024 / Heropbeuring CW opaque; Medium CW YE2025 + Strong "
            "KBO; FOI ready not sent"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T21:55:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK} EVERY-10; omzet {OM25} bruto {BR25} (~{RATIO}x) pnl {PN25} equity {EQ25} "
            f"FTE {FTE25}; 1 VE Anderlecht; next every-10 2240"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2231",
    {
        "task_id": "rq_2231",
        "title": (
            "leftover dual hole-fill after Travie — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Leftover dual after Travie Anderlecht YE2025 Medium (bruto 11.39m / ~2.84x omzet / "
            "pnl DROP -89%). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB "
            "YE2025, else AIESH/REW if YE2025, else Heropbeuring 0406.678.141 if NBB/CW euros live, "
            "else unused maatwerk/kringloop/WZC/IGS (e.g. SDB 0665.861.844 / Le Rucher 0860.345.458 "
            "/ De Vleugels 0431.408.290 if still FREE). Do NOT redo Travie, De Oever, ViTeS BE, "
            "Kringwinkel Midwest, ViTeS, Reset, Den Azalee, Kringwinkel West, Manus BXL, Manus "
            "groep, Manus Antwerpen, Kringwinkel Maasland, Kringwinkel ZOV, NBSW, Opnieuw & Co, "
            "Veerkracht 4, Werkmmaat, Constructief, Kringloopwinkel Deltagroep, Groep Maatwerk, "
            "OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, "
            "Kemphaan, Entiris, Oesterbank. Next EVERY-10: 2240."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2230 Travie EVERY-10; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; next every-10 2240"
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
    "last_unit_id": "rq_2230",
    "ticks_completed": "2230",
    "paused": "no",
    "notes": (
        f"tick2230 EVERY-10 + leftover Travie 0420.015.938 Medium (omzet DROP {OM25}; bruto "
        f"{BR25} ~{RATIO}x; pnl DROP {PN25} {PN_PCT}%; equity DROP {EQ25}; FTE JUMP {FTE25}; "
        "1 VE Anderlecht); after De Oever@2229; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
        "Heropbeuring CW opaque; next rq_2231; next every-10 2240; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)

# --- loop_log append ---
log_block = f"""

## Tick 2230 - 2026-08-26T22:15:00Z - rq_2230 EVERY-10 + Travie (bruto 11.39m / ~2.84x omzet / pnl DROP -89% / Medium)

- Unit: **rq_2230** EVERY-10 + leftover dual after **rq_2229 De Oever**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW probe **404**/YE2024-class; Heropbeuring filed 25.06.2026 but **CW kern opaque** (FTE-only). Took named FREE leftover **Travie VZW** YE2025 (KBO **0420.015.938**; Vaartdijk 40 Anderlecht; **Actief** **1 VE**; NACE **88.993/88.995** maatwerk/ETA). Do not redo De Oever/ViTeS BE/Midwest/ViTeS/Reset/Manus stack.
- EVERY-10: refreshed `progress_every_10_ticks.md` (tick 2230 snapshot; **A 100% / B 100% / C ~99% / D ~74-88% / E ~{foi_ready + 1} FOI-ready**; inventory budgets {n_bud}+ / lb {n_lb}+) + `doge_waste_top10_current.md` (pure annual top10 **stable** GIP/fossil/cars/cheque/reporté; NEW residual 2221-2230 note incl. Travie EVERY-10 primary).
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** DROP {OM_PCT}% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** flat {BR_PCT}% (bruto≫omzet ~**{RATIO}x**); pnl **EUR{PN25}** DROP {PN_PCT}% vs YE2024 EUR{PN24}; equity **EUR{EQ25}** DROP {EQ_PCT}%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **10.07.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via contact@travie.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2230=done + rq_2231 open; loop_state ticks=2230; raw docs/doge/raw/tick2230/; EVERY-10 files refreshed.
- FOI: **ready not sent** (human-gated).
- Next: rq_2231 (AGB/FARO-if-YE2025 / AIESH-REW / Heropbeuring-or-unused). Next every-10 **2240**.
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(
    f"OK tick2230 Travie EVERY-10 bruto={BR25} omzet={OM25} pnl={PN25} pi={PI} "
    f"foi_ready~{foi_ready + 1} next=rq_2231 every10=2240"
)

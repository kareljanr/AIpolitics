# tick2250 — EVERY-10 + leftover dual Le Saupont YE2025 Medium (omzet 23.12m / pnl DROP -51% / FTE DROP 370.9)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "sc_le_saupont_bertrix"
TICK = "2250"
UTC = "2026-08-27T04:40:00Z"
GAP = "gap_saupont_nbb_pdf_assets_debt_pnl_drop_51pct_fte_drop_eta_matrix_l5"
COMM = "comm_saupont_jr2025_statutory_eta_omzet_pnl_drop_fte_drop"
LB = "lb_saupont_omzet_23_12m_pnl_drop_51pct_fte_drop_jr2025"

OM25, OM24 = 23121199, 23210949
BR25, BR24 = 15310544, 15799381
PN25, PN24 = 187782, 384374
EQ25, EQ24 = 12695449, 13392858
FTE25, FTE24 = 370.9, 382.7


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


# --- EVERY-10 ---
progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2250** (2026-08-27)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2241-2250 continuum; AGB Bornem / FARO / AIESH / REW still YE2024 stalls; Heropbeuring CW opaque |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2241-2250 is residual dual L5 (not near-complete of 348bn):** **L'Atelier** bruto **12.09m** / ~**2.07×** / pnl LOSS FLIP · **Le Perron** bruto **4.00m** / ~**1.70×** · **APAM** bruto **6.13m** / ~**3.08×** / pnl PROFIT FLIP · **La Lumière** bruto **7.25m** / ~**2.37×** / pnl LOSS DEEPEN · **Jeunes Jardiniers** bruto **4.78m** / ~**1.97×** / equity DROP **-52%** · **Pilifs** bruto **7.68m** / ~**1.43×** / pnl JUMP **+401%** · **TRAVCO** bruto **3.57m** / empty omzet / pnl PROFIT FLIP · **Jean Del'Cour** bruto **21.81m** / ~**1.57×** / FTE **548** · **Serviplast** omzet **5.85m** / pnl LOSS DEEPEN · EVERY-10 primary **Le Saupont** omzet **23.12m** / pnl DROP **-51%** / FTE DROP **370.9** (Medium CW) |
| **E. FOI-ready gaps** | **~1903** drafts ready | Human send only; answered **~11**; partial **~28**; total FOI rows **~1955** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability/maatwerk shells** (**NEW 2241-2250** L'Atelier · Le Perron · APAM · La Lumière · Jeunes Jardiniers · Pilifs · TRAVCO · Jean Del'Cour · Serviplast · **Le Saupont** · prior 2231-2240 Axedis/Manufast/Metalgroup/EntrAnam stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2250)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | 53477+ |
| commitments.csv | 5952+ |
| leaderboard.csv | 8073+ |
| entities.csv | 1982+ |
| sources.csv | 6320+ |
| FOI ready | ~1903 |
| FOI answered | 11 |
| FOI partial | 28 |
| FOI total rows | ~1955 |
| research_queue open | rq_2251 after Saupont EVERY-10 |

### What improved since tick 2240

- **Residual dual (tick2241-2250):** **L'Atelier** (bruto **12.09m** ~**2.07×** / pnl LOSS FLIP) · **Le Perron** (bruto **4.00m** ~**1.70×**) · **APAM** (bruto **6.13m** ~**3.08×** / pnl PROFIT FLIP) · **La Lumière** (bruto **7.25m** ~**2.37×** / pnl LOSS DEEPEN) · **Jeunes Jardiniers** (bruto **4.78m** ~**1.97×** / equity DROP **-52%**) · **Pilifs** (bruto **7.68m** ~**1.43×** / pnl JUMP **+401%**) · **TRAVCO** (bruto **3.57m** / empty omzet / pnl PROFIT FLIP) · **Jean Del'Cour** (bruto **21.81m** ~**1.57×** / FTE **548**) · **Serviplast** (omzet **5.85m** / pnl LOSS DEEPEN / FTE DROP) · EVERY-10 primary **Le Saupont** (omzet **23.12m** / pnl DROP **-51%** / FTE DROP **370.9**; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024; narrative JV2025 only) · AIESH / REW YE2024-only · Heropbeuring CW kern opaque · Groupe FOES YE2024-only · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs FOI-ready.
"""
(DATA / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")

top10 = f"""# DOGE waste ranking — current top 10

**As-of:** tick **2250** (2026-08-27) · **8073+** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2241-2250:** **Le Saupont omzet 23.12m / pnl DROP −51% / FTE DROP 370.9** (EVERY-10@2250 primary) · **Jean Del'Cour bruto 21.81m / ~1.57× / FTE 548** · **APAM bruto 6.13m / ~3.08× / pnl PROFIT FLIP** · **L'Atelier bruto 12.09m / ~2.07× / pnl LOSS FLIP** · **Jeunes Jardiniers equity DROP −52%** · **La Lumière pnl LOSS DEEPEN** · **Serviplast pnl LOSS DEEPEN** · **TRAVCO empty omzet / pnl PROFIT FLIP** · **Pilifs pnl JUMP +401%** · prior 2231-2240 Axedis/Manufast/Metalgroup/EntrAnam/Entra stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia/Enodia/RESA · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2240:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). Tie-break among pi=8.5 puts fossil accises ahead of company cars by annual €; among pi=8.4 dual cars falls to #10 by annual €. **Major NEW residual 2241-2250 (off pure top10 / dual):** L'Atelier · Le Perron · APAM · La Lumière · Jeunes Jardiniers · Pilifs · TRAVCO · Jean Del'Cour · Serviplast · **Le Saupont omzet 23.12m / pnl DROP −51% / FTE DROP 370.9** (EVERY-10@2250 primary). Count NEW since 2240: ~10 residual dual fills. **Prior 2231-2240 + 2221-2230 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Le Saupont** EVERY-10 primary omzet **EUR23.12m** / pnl DROP **-51%** / FTE DROP **370.9** — Luxembourg ETA scale + subsidy opacity.
- **Jean Del'Cour** bruto **EUR21.81m** / omzet **EUR13.92m** (~**1.57×**) / FTE **548**.
- **APAM** bruto **EUR6.13m** / omzet **EUR1.99m** (~**3.08×**) / pnl PROFIT FLIP.
- **L'Atelier** bruto **EUR12.09m** / omzet **EUR5.85m** (~**2.07×**) / pnl LOSS FLIP.
- **Jeunes Jardiniers** bruto **EUR4.78m** / ~**1.97×** / equity DROP **-52%** / pnl LOSS FLIP.
- **La Lumière** bruto **EUR7.25m** / ~**2.37×** / pnl LOSS DEEPEN.
- **Serviplast** omzet **EUR5.85m** / pnl LOSS DEEPEN / FTE DROP **144.1**.
- **TRAVCO** bruto **EUR3.57m** / empty omzet / pnl PROFIT FLIP from **-315k**.
- **Pilifs** bruto **EUR7.68m** / ~**1.43×** / pnl JUMP **+401%** / FTE **224**.
- **Axedis** bruto **EUR4.55m** / ~**1.89×** / FTE DROP **162.9** (prior retained).
- Walloon **ZS** stack FTE-only budget opacity.
"""
(DATA / "doge_waste_top10_current.md").write_text(top10, encoding="utf-8")

# --- sources ---
s_fields, sources = read_csv("sources.csv")
for sid, title, url, publisher, sclass, notes in [
    (
        "src_saupont_jr2025_cw_nl",
        "Companyweb NL Le Saupont YE2025 statutory",
        "https://www.companyweb.be/nl/0407713665/le-saupont",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet DROP {OM25} (-0.39%) bruto DROP {BR25} (-3.09%) "
            f"pnl DROP {PN25} (-51.15%) equity DROP {EQ25} (-5.21%) FTE DROP {FTE25}; filed 23-07-2026"
        ),
    ),
    (
        "src_saupont_jr2025_cw_en",
        "Companyweb EN Le Saupont YE2025 statutory",
        "https://www.companyweb.be/en/0407713665/le-saupont",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 23-07-2026"
        ),
    ),
    (
        "src_saupont_jr2025_cw_fr",
        "Companyweb FR Le Saupont YE2025 statutory",
        "https://www.companyweb.be/fr/0407713665/le-saupont",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Bénéfice {PN25}",
    ),
    (
        "src_saupont_kbo_2250",
        "KBO Le Saupont 0407.713.665 Actief Bertrix 2 VE",
        "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=407713665",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2250; Actief SC Le Saupont; zetel Rue de Lonnoux 2 6880 Bertrix; "
            "2 VE; NACE RSZ 88.993; Walloon ETA Luxembourg province"
        ),
    ),
    (
        "src_saupont_site_contact_2250",
        "Le Saupont FOI channel info@saupont.be",
        "https://www.saupont.be/fr/contact",
        "Le Saupont SC",
        "foi_contact",
        "tick2250; info@saupont.be / public@saupont.be; +32 61 41 18 16; Rue de Lonnoux 2 6880 Bertrix",
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
        "name_nl": "Le Saupont SC (Bertrix / ETA maatwerk Luxemburg)",
        "name_fr": "Le Saupont SC (Bertrix / entreprise de travail adapté Luxembourg)",
        "name_en": "Le Saupont adapted-work SC (Bertrix Walloon ETA)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.saupont.be/",
        "foi_email": "info@saupont.be",
        "foi_postal": "Rue de Lonnoux 2, 6880 Bertrix",
        "notes": (
            f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0407.713.665 Actief 2 VE "
            f"NACE 88.993; omzet DROP {OM25} bruto {BR25} pnl DROP {PN25} (-51%) equity DROP {EQ25} "
            f"FTE DROP {FTE25}; neerlegging 23.07.2026; assets/debt Unknown; FOI {GAP}; "
            "preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "after Serviplast@2249; deferred FREE Dauphins; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_saupont_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025 (primary commercial)",
        f"tick{TICK}; Medium CW; omzet DROP -0.39% vs YE2024 {OM24}",
    ),
    (
        "bud_saupont_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025",
        f"tick{TICK}; Medium CW; bruto DROP -3.09% vs YE2024 {BR24}",
    ),
    (
        "bud_saupont_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory pnl YE2025 DROP",
        f"tick{TICK}; Medium CW; pnl DROP -51.15% vs YE2024 {PN24}",
    ),
    (
        "bud_saupont_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity DROP -5.21% vs YE2024 {EQ24}",
    ),
    (
        "bud_saupont_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 370.9",
        f"tick{TICK}; Medium CW; FTE DROP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_saupont_fte_jr2024_statutory_cmp",
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
            "source_id": "src_saupont_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

c_fields, commitments = read_csv("commitments.csv")
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            "Le Saupont YE2025 leftover dual EVERY-10 (omzet 23.12m / pnl DROP -51% / FTE DROP 370.9 / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Bertrix / AVIQ adapted-work public path",
        "legal_basis": (
            "SC ETA Le Saupont (KBO 0407.713.665; Actief; 2 VE; NACE 88.993; Bertrix)"
        ),
        "decision_date": "2026-07-23",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(OM25),
        "cash_by_year": (
            f'{{"2025_omzet":{OM25},"2025_bruto":{BR25},"2025_pnl":{PN25},'
            f'"2025_equity":{EQ25},"2025_fte":{FTE25},"2024_omzet":{OM24},'
            f'"2024_bruto":{BR24},"2024_pnl":{PN24},"2024_fte":{FTE24}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0407713665/le-saupont",
        "stated_goal": "Walloon ETA cosmetics / print / wood / laundry / logistics",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; reconcile pnl DROP -51% + FTE DROP "
            "vs AVIQ ETA subsidy matrix"
        ),
        "source_id": "src_saupont_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Luxembourg>Bertrix>Saupont>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope {OM25}; pnl DROP {PN25}; "
            f"FTE DROP {FTE25}; 2 VE; after Serviplast@2249"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# cost 5.5 (omzet ~23m), abs 7.2, diff 3 → pi = 3.025+2.52+0.7 = 6.245 → 6.25
lb_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            "Le Saupont omzet 23.12m / pnl DROP -51% / FTE DROP 370.9 (YE2025 Walloon ETA)"
        ),
        "level": "L5",
        "type": "eta_sc_statutory",
        "hierarchy_path": "Wallonie>Luxembourg>Bertrix>Saupont>JR2025",
        "annual_cost_eur": str(OM25),
        "total_cost_eur": str(OM25),
        "tco_notes": (
            f"CW omzet {OM25} / bruto {BR25} / pnl DROP {PN25} (-51%) / "
            f"equity DROP {EQ25} / FTE DROP {FTE25} / 2 VE Walloon ETA"
        ),
        "confidence": "medium",
        "source_id": "src_saupont_jr2025_cw_en",
        "beneficiaries": "ETA workers Bertrix / AVIQ adapted-work public path",
        "stated_goal": "Walloon ETA cosmetics / print / wood / laundry",
        "measured_outcome": (
            f"omzet DROP -0.39%; pnl DROP -51.15%; equity DROP -5.21%; "
            f"FTE DROP {FTE25}; filed 23.07.2026"
        ),
        "absurdity_score": "7.2",
        "cost_score": "5.5",
        "difficulty": "3.0",
        "priority_index": "6.25",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose AVIQ ETA matrix; "
            "reconcile pnl DROP -51% + FTE DROP"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} EVERY-10 primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; after Serviplast@2249; deferred FREE Dauphins"
        ),
    },
)
write_csv("leaderboard.csv", lb_fields, leaderboard)

f_fields, foi = read_csv("foi_queue.csv")
upsert(
    foi,
    "gap_id",
    GAP,
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Luxembourg>Bertrix>Saupont>NBB_PDF_assets_debt_pnl_drop_fte_drop"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet EUR{OM25} / "
            f"bruto EUR{BR25}; pnl DROP EUR{PN25} (-51% vs YE2024 EUR{PN24}); "
            f"FTE DROP {FTE25} vs {FTE24}; AVIQ ETA subsidy matrix"
        ),
        "why_it_matters": (
            "Medium CW shows large Walloon ETA SC (omzet 23.12m / pnl DROP -51% / FTE DROP 370.9) "
            "under AVIQ path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "Le Saupont SC",
        "recipient_email": "info@saupont.be",
        "recipient_postal": "Rue de Lonnoux 2, 6880 Bertrix",
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
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall "
            "FARO/AIESH/REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; "
            "after Serviplast@2249; deferred FREE Dauphins"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

rq_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2250",
    {
        "task_id": "rq_2250",
        "title": (
            "EVERY-10 + leftover dual — Le Saupont YE2025 Medium (omzet 23.12m / pnl DROP -51% / FTE DROP 370.9)"
        ),
        "sprint": "hole_fill",
        "priority": "10",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "EVERY-10 progress+top10 then leftover dual Le Saupont YE2025 FREE Walloon ETA",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T04:25:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; EVERY-10 refreshed; Saupont 0407.713.665 YE2025 Medium CW; omzet DROP {OM25} "
            f"bruto {BR25} pnl DROP {PN25} (-51%) equity DROP {EQ25} FTE DROP {FTE25}; "
            "2 VE Bertrix ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "after Serviplast@2249; deferred FREE Dauphins; next rq_2251; next EVERY-10 2260"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2251",
    {
        "task_id": "rq_2251",
        "title": (
            "leftover dual after Le Saupont — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "leftover dual after Le Saupont YE2025 Medium (omzet 23.12m / pnl DROP -51% / FTE DROP 370.9). "
            "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW "
            "if YE2025, else Heropbeuring if NBB/CW euros live, else unused ETA/VAPH/WZC/maatwerk "
            "(e.g. Les Dauphins if YE2025 FREE; skip Saupont/Serviplast/Jean Del'Cour/TRAVCO/Pilifs/"
            "Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123). "
            "Do NOT redo Le Saupont, Serviplast, Jean Del'Cour, TRAVCO, Pilifs, Jeunes Jardiniers, "
            "La Lumière, APAM, Jean Gielen, Le Perron, L'Atelier, Axedis, ETA 123 Beauraing, Manufast, "
            "Metalgroup, EntrAnam, Enghien, Entra, Ateliers de Tertre, Le Rucher, Het Rekreatief, Travie, "
            "SDB, De Vleugels, Kiemkracht, De Oever, ViTeS*, Kringwinkel*, Manus*, Reset, Den Azalee, "
            "Kemphaan, Mirto, Blankedale, Werkmmaat. Next EVERY-10: 2260."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"spawned after tick{TICK} EVERY-10 + Saupont; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; deferred FREE Dauphins; next every-10 2260"
        ),
    },
)
write_csv("research_queue.csv", rq_fields, rq)

ls_fields, ls = read_csv("loop_state.csv")
upsert(
    ls,
    "state_id",
    "main",
    {
        "state_id": "main",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_2250",
        "ticks_completed": TICK,
        "paused": "no",
        "notes": (
            f"tick{TICK} EVERY-10 + leftover Saupont 0407.713.665 Medium (omzet DROP {OM25}; "
            f"pnl DROP {PN25} -51%; equity DROP {EQ25}; FTE DROP {FTE25}; 2 VE Bertrix ETA); "
            "after Serviplast@2249; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "deferred FREE Dauphins; next rq_2251; next EVERY-10 2260; continuous hole_fill"
        ),
    },
)
write_csv("loop_state.csv", ls_fields, ls)

draft = f"""# FOI draft — Le Saupont (NBB PDF / pnl DROP -51% / FTE DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Le Saupont SC — KBO **0407.713.665** (Actief; Rue de Lonnoux 2, 6880 Bertrix; **2 VE**; FTE {FTE25} CW; NACE **88.993**; Walloon ETA Bertrix)  
**recipient:** info@saupont.be · Rue de Lonnoux 2, 6880 Bertrix  
**sources:** [CW EN](https://www.companyweb.be/en/0407713665/le-saupont) · [CW NL](https://www.companyweb.be/nl/0407713665/le-saupont) · [CW FR](https://www.companyweb.be/fr/0407713665/le-saupont) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=407713665) · [site](https://www.saupont.be/fr/contact)  
**tick:** {TICK} EVERY-10  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief SC Le Saupont; **2 VE**; zetel Bertrix; NACE **88.993**.
- CW YE2025: omzet **EUR{OM25:,}** DROP -0.39% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** DROP -3.09%; pnl **EUR{PN25:,}** DROP -51.15% vs YE2024 EUR{PN24:,}; equity **EUR{EQ25:,}** DROP -5.21%; FTE **{FTE25}** DROP vs {FTE24}; filed **23.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After Serviplast@2249. EVERY-10@2250 primary. Deferred FREE Dauphins.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Le Saupont SC
via info@saupont.be
Rue de Lonnoux 2, 6880 Bertrix
Objet: Publicité des comptes annuels 2025 Le Saupont (BCE 0407.713.665)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition chiffre d'affaires EUR{OM25} / marge brute EUR{BR25}.
3. PnL DROP EUR{PN25} (-51% vs YE2024 EUR{PN24}) — réconciliation avec FTE DROP {FTE25}.
4. Matrice des subsides AVIQ / ETA derrière les charges de personnel.
5. Répartition coûts cosmétique / impression / bois / blanchisserie / logistique.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
"""
(FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

log_block = f"""

### {UTC} - tick {TICK} - rq_2250 EVERY-10 + Le Saupont Bertrix (omzet 23.12m / pnl DROP -51% / FTE DROP 370.9 / Medium)

- **EVERY-10:** refreshed `progress_every_10_ticks.md` (A **100%** / B **100%** / C **~99%** / D **~74-88%** generous residual dual / E **~1903** FOI-ready) and `doge_waste_top10_current.md` (GIP #1; fossil/cars/cheque/reporté #2-10 stable; Saupont off pure top10). Next every-10: **2260**.
- Unit: **rq_2250** leftover dual after **rq_2249 Serviplast**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took named FREE Walloon ETA **Le Saupont SC** YE2025 (KBO **0407.713.665**; Rue de Lonnoux 2 Bertrix; **Actief** **2 VE**; NACE **88.993** AViQ). Deferred FREE Les Dauphins. Do not redo Serviplast/Jean Del'Cour/TRAVCO/Pilifs/Jeunes Jardiniers stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** DROP -0.39% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** DROP -3.09%; pnl **EUR{PN25}** DROP -51.15% vs YE2024 EUR{PN24}; equity **EUR{EQ25}** DROP -5.21%; FTE **{FTE25}** DROP vs {FTE24}; neerlegging **23.07.2026**. Strong KBO Actief 2 VE. Assets/debt Unknown. Medium. FOI via info@saupont.be.
- Wrote: progress+top10; sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.25); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2250=done + rq_2251 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2250/.
- FOI: **ready not sent** (human-gated).
- EVERY-10@**2250** done. Next: rq_2251 (AGB/FARO-if-YE2025 / AIESH-REW / unused Dauphins). Next every-10 **2260**.
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(f"tick{TICK} done EVERY-10; omzet={OM25} pnl={PN25} next=rq_2251")

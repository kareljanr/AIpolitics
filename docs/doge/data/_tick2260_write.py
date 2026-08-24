# tick 2260 — EVERY-10 + Alteria Colfontaine YE2025 Medium
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2260
UTC = "2026-08-27T07:10:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_alteria_colfontaine"
KBO = "0476.855.364"
KBO_BARE = "0476855364"
SRC_EN = "src_alteria_jr2025_cw_en"
GAP = "gap_alteria_nbb_pdf_assets_debt_bruto_gt_omzet_1_72x_pnl_drop_88pct_eta_matrix_l5"
COMM = "comm_alteria_jr2025_statutory_eta_omzet_pnl_drop_88pct"
LB = "lb_alteria_omzet_3_12m_bruto_1_72x_pnl_drop_88pct_fte_212_jr2025"
RQ = "rq_2260"
RQ_NEXT = "rq_2261"

OMZET = 3115001
OMZET24 = 3026171
BRUTO = 5351920
BRUTO24 = 4942521
PNL = 72779
PNL24 = 592478
EQUITY = 1966154
EQUITY24 = 1895513
FTE = 212.4
FTE24 = 209.9
RATIO = round(BRUTO / OMZET, 2)
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_PCT = round((PNL - PNL24) / PNL24 * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)


def append_csv(path: Path, rows: list[dict]):
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        existing = list(reader)
    id_key = fieldnames[0]
    ids = {r[id_key] for r in existing}
    new = [r for r in rows if r[id_key] not in ids]
    if not new:
        print(f"skip {path.name}")
        return
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        for r in new:
            w.writerow({k: r.get(k, "") for k in fieldnames})
    print(f"appended {len(new)} -> {path.name}")


def count_csv(name: str) -> int:
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return sum(1 for _ in csv.DictReader(f))


def foi_ready_count() -> tuple[int, int, int, int]:
    from collections import Counter

    with (DATA / "foi_queue.csv").open(newline="", encoding="utf-8") as f:
        c = Counter((r.get("status") or "") for r in csv.DictReader(f))
    total = sum(c.values())
    return c.get("ready", 0), c.get("answered", 0), c.get("partial", 0), total


def write_progress():
    budgets = count_csv("budgets.csv")
    commits = count_csv("commitments.csv")
    lbs = count_csv("leaderboard.csv")
    ents = count_csv("entities.csv")
    srcs = count_csv("sources.csv")
    ready, answered, partial, foi_total = foi_ready_count()
    text = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick {TICK}** ({DATE})

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2251-2260 continuum; AGB Bornem / FARO / AIESH / REW still YE2024 stalls; Heropbeuring CW opaque |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2251-2260 is residual dual L5 (not near-complete of 348bn):** **Les Dauphins** omzet **3.37m** / pnl LOSS FLIP · **Hunelle** omzet **2.05m** / ~**1.7×** / pnl LOSS FLIP · **Gaillettes** bruto **8.02m** / ~**2.03×** / pnl DROP **-82%** · **Cambier** omzet DROP **8.84m** / equity JUMP **+47%** · **Corelap** bruto **5.21m** / ~**2.01×** · **Belair** bruto **3.80m** / empty omzet / pnl DROP **-73%** · **Nekto** bruto **12.59m** / ~**1.67×** / pnl LOSS DEEPEN · **Val du Geer** omzet **10.75m** / pnl DROP **-22%** · **Les Erables** omzet **4.63m** / pnl DROP **-89%** / ~**1.45×** · EVERY-10 primary **Alteria** omzet **3.12m** / bruto **5.35m** / ~**1.72×** / pnl DROP **-87.72%** / FTE **212.4** (Medium CW) |
| **E. FOI-ready gaps** | **~{ready}** drafts ready | Human send only; answered **~{answered}**; partial **~{partial}**; total FOI rows **~{foi_total}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability/maatwerk shells** (**NEW 2251-2260** Dauphins · Hunelle · Gaillettes · Cambier · Corelap · Belair · Nekto · Val du Geer · Les Erables · **Alteria** · prior 2241-2250 Saupont/Del'Cour/APAM/L'Atelier stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick {TICK})

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {budgets}+ |
| commitments.csv | {commits}+ |
| leaderboard.csv | {lbs}+ |
| entities.csv | {ents}+ |
| sources.csv | {srcs}+ |
| FOI ready | ~{ready} |
| FOI answered | {answered} |
| FOI partial | {partial} |
| FOI total rows | ~{foi_total} |
| research_queue open | {RQ_NEXT} after Alteria EVERY-10 |

### What improved since tick 2250

- **Residual dual (tick2251-2260):** **Les Dauphins** (omzet **3.37m** / pnl LOSS FLIP) · **Hunelle** (omzet **2.05m** ~**1.7×** / pnl LOSS FLIP) · **Gaillettes** (bruto **8.02m** ~**2.03×** / pnl DROP **-82%**) · **Cambier** (omzet DROP **8.84m** / equity JUMP **+47%**) · **Corelap** (bruto **5.21m** ~**2.01×**) · **Belair** (bruto **3.80m** / empty omzet / pnl DROP **-73%**) · **Nekto** (bruto **12.59m** ~**1.67×** / pnl LOSS DEEPEN) · **Val du Geer** (omzet **10.75m** / pnl DROP **-22%**) · **Les Erables** (omzet **4.63m** / pnl DROP **-89%** / ~**1.45×**) · EVERY-10 primary **Alteria** (omzet **3.12m** / bruto **5.35m** ~**1.72×** / pnl DROP **-87.72%** / FTE **212.4**; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024; narrative JV2025 only; CW Last balance sheet year **2024**) · AIESH / REW YE2024-only · Heropbeuring CW opaque · Relais Haute Sambre / Stallbois YE2024 · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs FOI-ready.
"""
    (DATA / "progress_every_10_ticks.md").write_text(text, encoding="utf-8")
    print("progress_every_10_ticks.md refreshed")


def write_top10():
    text = f"""# DOGE waste ranking — current top 10

**As-of:** tick **{TICK}** ({DATE}) · **{count_csv("leaderboard.csv")}+** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2251-2260:** **Alteria omzet 3.12m / bruto~1.72× / pnl DROP −87.72% / FTE 212.4** (EVERY-10@{TICK} primary) · **Les Erables omzet 4.63m / pnl DROP −89%** · **Val du Geer omzet 10.75m** · **Nekto bruto 12.59m / ~1.67× / pnl LOSS DEEPEN** · **Belair / Corelap / Cambier / Gaillettes / Hunelle / Dauphins** · prior 2241-2250 Saupont/Del'Cour/APAM/L'Atelier/Pilifs/TRAVCO stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia/Enodia/RESA · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2250:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). Tie-break among pi=8.5 puts fossil accises ahead of company cars by annual €; among pi=8.4 dual cars falls to #10 by annual €. **Major NEW residual 2251-2260 (off pure top10 / dual):** Dauphins · Hunelle · Gaillettes · Cambier · Corelap · Belair · Nekto · Val du Geer · Les Erables · **Alteria omzet 3.12m / bruto~1.72× / pnl DROP −87.72% / FTE 212.4** (EVERY-10@{TICK} primary). Count NEW since 2250: ~10 residual dual fills. **Prior 2241-2250 + 2231-2240 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Alteria** EVERY-10 primary omzet **EUR3.12m** / bruto **EUR5.35m** (~**1.72×**) / pnl DROP **-87.72%** / FTE **212.4** — Colfontaine ETA scale + subsidy opacity.
- **Les Erables** omzet **EUR4.63m** / pnl DROP **-89.41%** / bruto~**1.45×** / FTE **180.1**.
- **Val du Geer** omzet **EUR10.75m** / pnl DROP **-21.9%** / FTE **241.4**.
- **Nekto** bruto **EUR12.59m** / ~**1.67×** / pnl LOSS DEEPEN / FTE **310.6**.
- **Belair** bruto **EUR3.80m** / empty omzet / pnl DROP **-73%**.
- **Corelap** bruto **EUR5.21m** / ~**2.01×** / pnl DROP **-14%**.
- **Cambier** omzet DROP **EUR8.84m** / equity JUMP **+47%**.
- **Gaillettes** bruto **EUR8.02m** / ~**2.03×** / pnl DROP **-82%**.
- **Hunelle** omzet **EUR2.05m** / ~**1.7×** / pnl LOSS FLIP.
- **Le Saupont** prior EVERY-10@2250 omzet **EUR23.12m** / pnl DROP **-51%** (retained).
- Walloon **ZS** stack FTE-only budget opacity.
"""
    (DATA / "doge_waste_top10_current.md").write_text(text, encoding="utf-8")
    print("doge_waste_top10_current.md refreshed")


def update_research_queue():
    path = DATA / "research_queue.csv"
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r["task_id"] == RQ:
            found = True
            r["status"] = "done"
            r["title"] = (
                "EVERY-10 + leftover dual — Alteria YE2025 Medium "
                f"(omzet 3.12m / bruto~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; EVERY-10 refreshed progress+top10; Alteria ASBL Colfontaine {KBO} YE2025 "
                f"Medium CW NL+EN+FR + Strong KBO; omzet JUMP {OMZET} ({OMZET_PCT}%); "
                f"bruto JUMP {BRUTO} (~{RATIO}x / {BRUTO_PCT}%); pnl DROP {PNL} ({PNL_PCT}% vs {PNL24}); "
                f"equity JUMP {EQUITY} ({EQUITY_PCT}%); FTE {FTE}; 1 VE; NACE 88.993; neerlegging 08.07.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO CW YE2024 / "
                f"AIESH/REW YE2024; Relais Haute Sambre/Stallbois YE2024; after Les Erables@2259; "
                f"next EVERY-10 2270"
            )
            r["instructions"] = (
                "EVERY-10 + leftover dual Alteria YE2025 FREE Walloon ETA after Les Erables; "
                "preferred AGB/FARO/AIESH/REW still YE2024 (FARO CW confirmed Last balance 2024)"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Alteria — prefer AGB/FARO-YE2025/"
                    "AIESH-REW/Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"After Alteria YE2025 Medium (omzet 3.12m / bruto~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025 "
                    "(CW still Last balance sheet year 2024 as of tick2260), "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk (e.g. Stallbois / AJR / La Lorraine / Relais Haute Sambre "
                    "if YE2025 FREE; skip Alteria/Les Erables/Val du Geer/Nekto/Belair/Corelap/Cambier/"
                    "Gaillettes/Hunelle/Dauphins Gembloux/Saupont/Serviplast/Jean Del'Cour/TRAVCO/Pilifs/"
                    "Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA 123/"
                    "Manufast/Metalgroup/EntrAnam/Enghien/Entra/Ateliers de Tertre/Le Rucher/Het Rekreatief/"
                    "Travie/SDB/De Vleugels/Kiemkracht/De Oever/ViTeS*/Kringwinkel*/Manus*/Reset/Den Azalee/"
                    "Kemphaan/Mirto/Blankedale/Werkmmaat). "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/"
                    "Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/"
                    "Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Senes. "
                    "Next EVERY-10 is 2270."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Alteria EVERY-10; FARO CW YE2024 confirmed; "
                    "AIESH/REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; "
                    "Relais Haute Sambre/Stallbois YE2024; next EVERY-10 2270"
                ),
            }
        )
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("research_queue updated")


def write_loop_state():
    path = DATA / "loop_state.csv"
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    rows[0].update(
        {
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": RQ,
            "ticks_completed": str(TICK),
            "paused": "no",
            "notes": (
                f"tick{TICK} EVERY-10 + leftover Alteria {KBO} Medium (omzet JUMP {OMZET}; "
                f"bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL} {PNL_PCT}%; equity JUMP {EQUITY}; "
                f"FTE {FTE}; 1 VE Colfontaine ETA); after Les Erables@2259; "
                f"AGB Bornem JR2024; FARO CW YE2024 confirmed; AIESH/REW YE2024; "
                f"Relais Haute Sambre/Stallbois YE2024; next {RQ_NEXT}; next EVERY-10 2270; "
                "continuous hole_fill"
            ),
        }
    )
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("loop_state updated")


def write_foi_draft():
    FOI.mkdir(parents=True, exist_ok=True)
    (FOI / f"{GAP}.md").write_text(
        f"""# FOI draft — Alteria (NBB PDF / bruto~{RATIO}x / pnl DROP {PNL_PCT}%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Alteria ASBL — KBO **{KBO}** (Actief; Rue Grande 5-7, 7340 Colfontaine; **1 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA Colfontaine)  
**recipient:** info@eta-alteria.be · juridique@eta-alteria.be · Rue Grande 5-7, 7340 Colfontaine  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}/alteria) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}/alteria) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}/alteria) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer={KBO_BARE}) · [site](https://eta-alteria.be/) · [leseta](https://leseta.be/annuaire-eta/alteria/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief ASBL/VZW **ALTERIA**; **1 VE**; zetel Colfontaine; NACE **88.993**; begindatum 21.12.2001; aanbestedende overheid; erkenning aannemer.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP {OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP {BRUTO_PCT}% (bruto/omzet ~{RATIO}x); pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP {EQUITY_PCT}%; FTE **{FTE}**; filed **08.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO CW YE2024 confirmed; AIESH/REW YE2024; Relais Haute Sambre/Stallbois YE2024. After Les Erables@2259. EVERY-10@{TICK}.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Alteria ASBL
via info@eta-alteria.be / juridique@eta-alteria.be
Rue Grande 5-7, 7340 Colfontaine
Objet: Publicité des comptes annuels 2025 Alteria (BCE {KBO})

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition chiffre d'affaires EUR{OMZET} / marge brute EUR{BRUTO} (~{RATIO}x).
3. PnL DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}) — réconciliation avec omzet/bruto/FTE en hausse.
4. Matrice des subsides AVIQ / ETA derrière les charges de personnel.
5. Répartition coûts construction / peinture / menuiserie / reliure / couture / sous-traitance / titres-services.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
""",
        encoding="utf-8",
    )
    print("foi draft written")


def append_log():
    with LOG.open("a", encoding="utf-8") as f:
        f.write(
            f"""

## Tick {TICK} - {UTC} - rq_2260 EVERY-10 + Alteria Colfontaine (omzet 3.12m / bruto~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)

- Unit: **rq_2260** EVERY-10 MANDATORY + leftover dual after **rq_2259 Les Erables**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO CW still **Last balance sheet year 2024** (NBB YE2025 unpublished; JV2025 narrative only); AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre/Stallbois still **YE2024**. Took deferred FREE Walloon ETA **Alteria ASBL** YE2025 (KBO **{KBO}**; Rue Grande 5-7 Colfontaine; **Actief** **1 VE**; NACE **88.993** AViQ). Do not redo Les Erables/Val du Geer/Nekto/Belair/Corelap/Cambier/Gaillettes/Hunelle/Dauphins/Saupont stack.
- EVERY-10: refreshed `progress_every_10_ticks.md` (A/B 100%; C ~99%; D ~74-88% residual dual 2251-2260; E ~{foi_ready_count()[0]} ready) + `doge_waste_top10_current.md` (pure annual top10 **stable** GIP/fossil/cars/cheque/reporté; OWV snowball/AGB pi>10 filtered). Next EVERY-10 **2270**.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP {BRUTO_PCT}% (bruto/omzet ~{RATIO}x); pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_PCT}%; FTE **{FTE}**; neerlegging **08.07.2026**. Strong KBO Actief 1 VE + aanbestedende overheid. Assets/debt Unknown. Medium. FOI via info@eta-alteria.be / juridique@eta-alteria.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.05); entities (+1 {ENTITY}); foi + draft {GAP}; progress+top10; rq_2260=done + rq_2261 open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2260/.
- FOI: **ready not sent** (human-gated).
- EVERY-10 done (last was 2250; next **2270**). Next: rq_2261.
"""
        )
    print("loop_log appended")


def main():
    # Append data first so inventory counts in progress include this tick's rows
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_alteria_jr2025_cw_nl",
                "title": "Companyweb NL Alteria YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}/alteria",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} "
                    f"bruto {BRUTO} FTE {FTE}; neerlegging 08.07.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2260/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Alteria YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}/alteria",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 08-07-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Gross margin {BRUTO} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_alteria_jr2025_cw_fr",
                "title": "Companyweb FR Alteria YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}/alteria",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Bénéfice {PNL}",
            },
            {
                "source_id": f"src_alteria_kbo_{TICK}",
                "title": f"KBO Alteria {KBO} Actief Colfontaine 1 VE",
                "url": (
                    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?"
                    f"lang=nl&ondernemingsnummer={KBO_BARE}"
                ),
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief ASBL/VZW ALTERIA; zetel Rue Grande 5-7 7340 Colfontaine; "
                    f"1 VE; NACE 88.993; begindatum 21.12.2001; aanbestedende overheid; KBO email empty"
                ),
            },
            {
                "source_id": f"src_alteria_site_contact_{TICK}",
                "title": "Alteria FOI channel info@ / juridique@eta-alteria.be",
                "url": "https://eta-alteria.be/contact/",
                "publisher": "eta-alteria.be / Alteria ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@eta-alteria.be + juridique@eta-alteria.be; "
                    "tel +32 (0)65 450 980; Rue Grande 5-7 7340 Colfontaine; also leseta.be"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_alteria_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW statutory omzet YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; omzet JUMP {OMZET_PCT}% vs YE2024 {OMZET24} (primary envelope)",
            },
            {
                "budget_id": "bud_alteria_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW statutory bruto_marge YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto JUMP {BRUTO_PCT}%; bruto/omzet ~{RATIO}x",
            },
            {
                "budget_id": "bud_alteria_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW statutory winst/verlies YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl DROP {PNL_PCT}% vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_alteria_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW statutory eigen_vermogen YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; equity JUMP {EQUITY_PCT}% vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_alteria_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": f"CW social-balance FTE {FTE}",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; FTE {FTE} vs YE2024 {FTE24}; assets/debt Unknown",
            },
            {
                "budget_id": "bud_alteria_omzet_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(OMZET24),
                "amount_min_eur": str(OMZET24),
                "amount_max_eur": str(OMZET24),
                "basis": "CW statutory omzet YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 omzet {OMZET24} comparative (pre pnl DROP)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Alteria YE2025 leftover dual EVERY-10 "
                    f"(omzet 3.12m / bruto~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Colfontaine / AVIQ adapted-work public path",
                "legal_basis": f"ASBL ETA Alteria (KBO {KBO}; Actief; 1 VE; NACE 88.993; Colfontaine)",
                "decision_date": "2026-07-08",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET24},'
                    f'"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},'
                    f'"2024_fte":{FTE24}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}/alteria",
                "stated_goal": "Walloon ETA construction / peinture / menuiserie / reliure Colfontaine",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; reconcile pnl DROP -88% despite omzet/bruto/FTE up "
                    "vs AVIQ ETA subsidy matrix; disclose atelier cost allocation"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Hainaut>Colfontaine>Alteria>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; pnl DROP {PNL}; "
                    f"FTE {FTE}; 1 VE; after Les Erables@2259; AGB Bornem JR2024; FARO CW YE2024; "
                    "not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": (
                    f"Alteria omzet 3.12m / bruto~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE} "
                    "(YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Hainaut>Colfontaine>Alteria>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW omzet {OMZET} / bruto {BRUTO} (~{RATIO}x) / pnl DROP {PNL} ({PNL_PCT}%) / "
                    f"equity JUMP {EQUITY} / FTE {FTE} / 1 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Colfontaine / AVIQ adapted-work public path",
                "stated_goal": "Walloon ETA construction / peinture / menuiserie / reliure",
                "measured_outcome": (
                    f"omzet JUMP {OMZET_PCT}%; bruto JUMP {BRUTO_PCT}%; pnl DROP {PNL_PCT}%; "
                    f"equity JUMP {EQUITY_PCT}%; FTE JUMP {FTE_PCT}%; filed 08.07.2026"
                ),
                "absurdity_score": "7.4",
                "cost_score": "4.8",
                "difficulty": "3.0",
                "priority_index": "6.05",
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose AVIQ ETA matrix; "
                    "reconcile pnl DROP -88% despite rising omzet/bruto/FTE"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK} EVERY-10 primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO CW YE2024 confirmed; after Les Erables@2259"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Alteria VZW (Colfontaine / ETA maatwerk Henegouwen)",
                "name_fr": "Alteria ASBL (Colfontaine / entreprise de travail adapté Hainaut)",
                "name_en": "Alteria adapted-work ASBL (Colfontaine Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://eta-alteria.be/",
                "foi_email": "info@eta-alteria.be",
                "foi_postal": "Rue Grande 5-7, 7340 Colfontaine",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.993; "
                    f"omzet JUMP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl DROP {PNL} ({PNL_PCT}%) "
                    f"equity JUMP {EQUITY} FTE {FTE}; neerlegging 08.07.2026; "
                    f"assets/debt Unknown; FOI {GAP}; also juridique@eta-alteria.be; "
                    "preferred stalls AGB Bornem JR2024; FARO CW YE2024; after Les Erables@2259; "
                    "EVERY-10 primary; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Wallonie>Hainaut>Colfontaine>Alteria>NBB_PDF_assets_debt_pnl_drop",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet EUR{OMZET} / "
                    f"bruto EUR{BRUTO} (~{RATIO}x); pnl DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}); "
                    f"FTE {FTE}; AVIQ ETA subsidy matrix; atelier cost allocation "
                    "(construction/peinture/menuiserie/reliure/couture/sous-traitance)"
                ),
                "why_it_matters": (
                    f"Medium CW shows Walloon ETA ASBL (omzet 3.12m / bruto~{RATIO}x / pnl DROP {PNL_PCT}% / "
                    f"FTE {FTE}) under AVIQ path; assets/debt unpublished; profit collapse despite growth"
                ),
                "priority": "8",
                "recipient_body": "Alteria ASBL",
                "recipient_email": "info@eta-alteria.be",
                "recipient_postal": "Rue Grande 5-7, 7340 Colfontaine",
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
                "notes": (
                    f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; also juridique@eta-alteria.be; "
                    "preferred stall FARO CW YE2024; AGB Bornem JR2024; after Les Erables@2259; "
                    "EVERY-10 primary; next EVERY-10 2270"
                ),
            }
        ],
    )

    write_foi_draft()
    write_progress()
    write_top10()
    update_research_queue()
    write_loop_state()
    append_log()
    print("DONE tick", TICK)


if __name__ == "__main__":
    main()

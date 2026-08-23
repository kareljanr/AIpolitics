# tick 2100 — EVERY-10 progress/waste refresh + SLG Vlaanderen VZW YE2025 Medium
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
FOI_DRAFTS = ROOT / "foi" / "drafts"

csv.field_size_limit(10**7)
UTC = "2026-08-25T05:55:00Z"
TICK = 2100
ENTITY = "vzw_slg_vlaanderen"
GAP = "gap_slg_vlaanderen_nbb_pdf_assets_debt_pnl_flip_loss_equity_thin_matrix_l5"
LB = "lb_slg_vlaanderen_omzet_jump_115_87m_pnl_flip_loss_equity_thin_jr2025"
COMM = "comm_slg_vlaanderen_jr2025_statutory_wzc"

OMZET = 115872918
PNL = -332030
EQUITY = 397440
BRUTO = 83069045
FTE = 1190.2
OMZET24 = 113406853
PNL24 = 176516
EQUITY24 = 729470
BRUTO24 = 82083886
FTE24 = 1192.8
OMZET_YOY = "JUMP +2.17%"
PNL_YOY = "FLIP LOSS -288.1%"
EQUITY_YOY = "DROP -45.52%"
BRUTO_YOY = "JUMP +1.20%"
FTE_YOY = "DROP -0.22%"
FILED = "28.07.2026"
KBO = "0410.958.712"
KBO_DIGITS = "0410958712"
EMAIL = "info@korian.be"
ADDR = "Satenrozen 1 B, 2550 Kontich"
SITE = "https://www.korian.be/"
CW_NL = f"https://www.companyweb.be/nl/{KBO_DIGITS}/slg-vlaanderen"
CW_EN = f"https://www.companyweb.be/en/{KBO_DIGITS}/slg-vlaanderen"
CW_FR = f"https://www.companyweb.be/fr/{KBO_DIGITS}/slg-vlaanderen"
KBO_URL = (
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?"
    f"ondernemingsnummer={KBO_DIGITS}"
)
NBB = f"https://consult.cbso.nbb.be/consult-enterprise/{KBO_DIGITS}"
PI = "6.7"
ABSURD = "6.8"
COST = "7.0"
DIFF = "4.0"

# inventory snapshot (pre-append)
INV = {
    "budgets": 52562,
    "commitments": 5766,
    "leaderboard": 7887,
    "entities": 1800,
    "sources": 5393,
    "foi_ready": 1716,
    "foi_answered": 11,
    "foi_partial": 28,
    "foi_total": 1768,
}

DO_NOT_REDO = (
    "Do NOT redo SLG Vlaanderen, SLG Operaties Vlaanderen, Korian Belgium (if taken), "
    "AREWAL, Familiezorg Gent, emeis Belgium, Begralim, Sint-Lucia, Lidwina, SED, "
    "Zilvervogel, Familiezorg WV, De Lovie, Ocura, Armonea, Always Home, Colisée Belgium, "
    "AGB Bornem, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, "
    "IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, Belgoprocess, Laborelec, "
    "NIRAS, Bel V, Dijk92, FANC, SCK CEN, EURIDICE, IRE*, BRUGEL."
)


def append_csv(path: Path, rows: list[dict]):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        existing = list(reader)
    ids = set()
    id_key = None
    for cand in (
        "source_id",
        "budget_id",
        "commitment_id",
        "item_id",
        "entity_id",
        "gap_id",
        "task_id",
    ):
        if cand in (fieldnames or []):
            id_key = cand
            break
    if id_key:
        ids = {r.get(id_key) for r in existing}
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(existing)
        for r in rows:
            if id_key and r.get(id_key) in ids:
                continue
            out = {k: r.get(k, "") for k in fieldnames}
            w.writerow(out)


def write_progress():
    # post-append inventory (+5 budgets, +1 each commitment/lb/entity, +5 sources, +1 FOI)
    b = INV["budgets"] + 5
    c = INV["commitments"] + 1
    lb = INV["leaderboard"] + 1
    e = INV["entities"] + 1
    s = INV["sources"] + 5
    ready = INV["foi_ready"] + 1
    total_foi = INV["foi_total"] + 1
    text = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick {TICK}** (2026-08-25)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2091-2100 zorg + GRD shared continuum after 2090 Familiezorg WV |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2091-2100 is residual dual L5 (not near-complete of 348bn):** **Zilvervogel** omzet JUMP **20.96m** · **SED Zoutleeuw** omzet JUMP **16.36m** / pnl FLIP LOSS · **Lidwina** bruto JUMP **21.60m** · **Sint-Lucia** omzet JUMP **7.67m** · **Begralim** omzet JUMP **22.67m** / pnl DROP · **emeis** omzet JUMP **19.63m** / LOSS narrow · **Familiezorg Gent** bruto JUMP **70.04m** · **AREWAL** omzet DROP **5.63m** / equity thin · **SLG Operaties** omzet JUMP **58.28m** / FTE JUMP **1095.3** · **SLG Vlaanderen VZW** omzet JUMP **115.87m** / pnl FLIP LOSS / equity thin **0.40m** Medium (this tick EVERY-10 dual) |
| **E. FOI-ready gaps** | **~{ready}** drafts ready | Human send only; answered **~{INV['foi_answered']}**; partial **~{INV['foi_partial']}**; total FOI rows **~{total_foi}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych shells** (**NEW 2091-2100** Zilvervogel · SED · Lidwina · Sint-Lucia · Begralim · emeis · Familiezorg Gent · AREWAL · SLG Operaties · **SLG Vlaanderen** · prior 2081-2090 / 2071-2080 stacks retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick {TICK})

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {b} |
| commitments.csv | {c} |
| leaderboard.csv | {lb} |
| entities.csv | {e} |
| sources.csv | {s} |
| FOI ready | {ready} |
| FOI answered | {INV['foi_answered']} |
| FOI partial | {INV['foi_partial']} |
| FOI total rows | {total_foi} |
| research_queue open | rq_2101 after progress |

### What improved since tick 2090

- **Residual dual (tick2091-2100):** **CZD Zilvervogel Lo-Reninge** · **Sint-Elisabeth's Dal Zoutleeuw** · **Lidwina Mol** · **Sint-Lucia Turnhout** · **Begralim / Grauwzusters Limburg** · **emeis Belgium** · **Familiezorg Gent** · **AREWAL** (AIEG/AIESH/REW shared services) · **SLG Operaties Vlaanderen** (Korian ops NV; omzet JUMP 58.28m / FTE JUMP 1095.3) · **SLG Vlaanderen / Senior Living Group Vlaanderen VZW** (this tick EVERY-10 dual — Kontich VZW RVT NACE 87.101 YE2025 Medium CW; omzet 115.87m; pnl FLIP LOSS; equity thin 0.40m vs omzet; FTE DROP; dual SLG Operaties / Korian Belgium).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH 0201.712.587 / REW 0644.638.937 YE2024-only · Always Home=Armonea skipped · prior Eneco deposit FOI stack.
"""
    (DATA / "progress_every_10_ticks.md").write_text(text, encoding="utf-8")


def write_waste_top10():
    lb_count = INV["leaderboard"] + 1
    text = f"""# DOGE waste ranking — current top 10

**As-of:** tick **{TICK}** (2026-08-25) · **{lb_count}** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2091-2100:** **SLG Vlaanderen omzet 115.87m** · **Familiezorg Gent bruto 70.04m** · **SLG Operaties omzet 58.28m** · **Begralim omzet 22.67m** · **Zilvervogel omzet 20.96m** · **emeis omzet 19.63m** · **SED omzet 16.36m** · **Lidwina bruto 21.60m** · **Sint-Lucia omzet 7.67m** · **AREWAL omzet 5.63m** · prior 2081-2090 Medemens/Familiezorg WV/De Lovie/Ocura/Lindelo stack retained · prior 2071-2080 / 2061-2070 / 2051-2060 stacks retained · prior nuclear/Fluxys/Elia/Enodia/RESA · prior Eneco continuum · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2090:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; company-cars/accises order swap within 8.5 band). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2091-2100 (off pure top10 / dual):** Zilvervogel · SED · Lidwina · Sint-Lucia · Begralim · emeis · Familiezorg Gent · AREWAL · SLG Operaties · **SLG Vlaanderen** (EVERY-10 dual). Count NEW since 2090: 10 residual dual ticks. **Prior 2081-2090 + 2071-2080 stacks retained.** Not TE-additive of ~348bn.
"""
    (DATA / "doge_waste_top10_current.md").write_text(text, encoding="utf-8")


def update_research_queue():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r["task_id"] == "rq_2100":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2100 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = (
                "EVERY-10 + leftover dual — SLG Vlaanderen YE2025 Medium"
            )
            r["instructions"] = (
                "Completed EVERY-10 progress+waste refresh + leftover SLG Vlaanderen "
                f"YE2025 Medium CW; KBO {KBO}; omzet JUMP {OMZET} bruto JUMP {BRUTO} "
                f"pnl FLIP LOSS {PNL} equity DROP thin {EQUITY} FTE DROP {FTE}; FOI {GAP}; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; NACE 87.101 VZW 29 VE; "
                "Korian Belgium bestuurder; dual SLG Operaties"
            )
            r["notes"] = (
                f"tick{TICK} EVERY-10 + SLG Vlaanderen Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"bruto JUMP {BRUTO/1e6:.2f}m pnl FLIP LOSS {PNL/1e6:.2f}m "
                f"equity DROP thin {EQUITY/1e6:.2f}m FTE DROP {FTE}; FOI ready; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2101; next every-10 2110"
            )
            found = True
    if not found:
        raise SystemExit("rq_2100 missing")
    if not any(r["task_id"] == "rq_2101" for r in rows):
        rows.append(
            {
                "task_id": "rq_2101",
                "title": (
                    "leftover dual hole-fill after SLG Vlaanderen — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/Korian-Belgium/unused WZC"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2101 after SLG Vlaanderen YE2025 Medium EVERY-10. Prefer leftover "
                    "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW "
                    "if YE2025, else Korian Belgium 0869.769.702 YE2025 live unused dual, "
                    "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. " + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "spawned after tick2100 SLG Vlaanderen EVERY-10; next every-10 2110; "
                    "Korian Belgium YE2025 deferred live"
                ),
            }
        )
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def write_loop_state():
    path = DATA / "loop_state.csv"
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(
            fh,
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
                "last_tick_utc": UTC,
                "last_unit_id": "rq_2100",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} EVERY-10 + leftover SLG Vlaanderen {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                    f"pnl FLIP LOSS {PNL/1e6:.2f}m equity DROP thin {EQUITY/1e6:.2f}m "
                    f"FTE DROP {FTE}; assets/debt Unknown; NACE 87.101 29 VE Korian dual); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2101; next every-10 2110; continuous hole_fill"
                ),
            }
        )


def write_foi_draft():
    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    path = FOI_DRAFTS / f"{GAP}.md"
    path.write_text(
        f"""# FOI draft — SLG Vlaanderen / Senior Living Group Vlaanderen (NBB PDF / assets-debt / pnl-flip / equity-thin)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Senior Living Group Vlaanderen VZW (SLG Vlaanderen) — KBO **{KBO}**  
**recipient:** {EMAIL} (Korian Belgium HQ, same zetel) · {ADDR} · +32 (0)3 443 76 50  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [NBB consult]({NBB}) · [Korian contact]({SITE}contact/)  
**tick:** {TICK} (EVERY-10)  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown; KBO Strong identity)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** {OMZET_YOY}; bruto **EUR{BRUTO}** {BRUTO_YOY}; pnl **LOSS EUR{PNL}** {PNL_YOY} vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** {EQUITY_YOY} (thin vs omzet); FTE **{FTE}** {FTE_YOY}; assets/debt **Unknown**.
- KBO: Actief VZW; **29 VE**; NACE **87.101** RVT; zetel {ADDR}; bestuurder includes **Korian Belgium** 0869.769.702.
- Dual of **SLG Operaties Vlaanderen** NV (rq_2099; omzet JUMP 58.28m / FTE JUMP 1095.3). Preferred stall still blocked: AGB Bornem JR2024; FARO/AIESH/REW YE2024.
- DISTINCT from Armonea / Always Home / emeis / Colisée.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Senior Living Group Vlaanderen VZW / Korian Belgium
{ADDR}
via {EMAIL}
Betreft: Openbaarmaking NBB-jaarrekening 2025 SLG Vlaanderen + balans/resultaatmatrix (KBO {KBO})
Geachte, op grond van toepasselijke openbaarheidsregels (Bestuursdecreet waar van toepassing; houder publiek gesubsidieerde RVT-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}) + depositreferentie.
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Toelichting pnl FLIP naar LOSS EUR{PNL} en equity DROP naar EUR{EQUITY} bij omzet EUR{OMZET} (equity thin).
4. Split omzet/bruto naar RVT sites / Zorgkas/IFIC vs private path; 29 VE matrix.
5. Relatie tot SLG Operaties Vlaanderen 0845.064.196 / Korian Belgium 0869.769.702 (aandeelhouderschap, management fees, absorpties/overdrachten 2025).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
        encoding="utf-8",
    )


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - rq_2100 EVERY-10 + SLG Vlaanderen (omzet JUMP 115.87m / pnl FLIP LOSS / equity thin 0.40m / Medium)

### A/B/C/D/E brief
- **A** 100% L0 TE EUR347.956bn Strong
- **B** 100% L1 unconsol map Strong
- **C** ~99% L2 entity totals (order of magnitude)
- **D** ~74-88% generous residual dual L5 (NOT near-complete of 348bn); NEW 2091-2100 zorg/GRD dual stack + this tick SLG Vlaanderen 115.87m
- **E** ~{INV['foi_ready']+1} FOI ready (human-send only)

- Unit: **rq_2100** EVERY-10 mandatory + leftover dual after **rq_2099 SLG Operaties**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred dual leftover **SLG Vlaanderen / Senior Living Group Vlaanderen** YE2025 (KBO **{KBO}**; {ADDR}; Antwerpen **VZW** RVT NACE **87.101** / **29 VE**; bestuurder Korian Belgium). Korian Belgium NV YE2025 also live — deferred to rq_2101. Do not redo SLG Operaties/AREWAL/Familiezorg Gent/emeis/Begralim/Sint-Lucia/Lidwina/SED/Zilvervogel/Familiezorg WV/De Lovie/Ocura/Armonea/Always Home/Colisée/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +2.17%; bruto **EUR{BRUTO}** JUMP +1.20%; pnl **LOSS EUR{PNL}** FLIP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** DROP -45.52% (thin vs omzet); FTE **{FTE}** DROP vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 29 VE; email {EMAIL}. Omzet used as primary envelope.
- Wrote: **EVERY-10** progress_every_10_ticks.md + doge_waste_top10_current.md; sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2100=done + rq_2101 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2100/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- **EVERY-10 done** (A/B 100%; C ~99%; D ~74-88% generous residual dual; E ~{INV['foi_ready']+1} ready). Next every-10 is **2110**. Next: rq_2101 (AGB/FARO-if-YE2025 / AIESH-REW / Korian Belgium deferred / unused WZC).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(entry)


def main():
    write_progress()
    write_waste_top10()

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_slg_vlaanderen_jr2025_cw",
                "title": "Companyweb NL — SLG Vlaanderen YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY}",
            },
            {
                "source_id": "src_slg_vlaanderen_jr2025_cw_en",
                "title": "Companyweb EN — SLG Vlaanderen YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}; equity thin vs omzet",
            },
            {
                "source_id": "src_slg_vlaanderen_jr2025_cw_fr",
                "title": "Companyweb FR — SLG Vlaanderen YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_slg_vlaanderen_kbo_{TICK}",
                "title": f"KBO — Senior Living Group Vlaanderen {KBO}",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief VZW 29 VE; NACE 87.101 RVT; zetel {ADDR}; "
                    f"bestuurder Korian Belgium 0869.769.702; Strong identity"
                ),
            },
            {
                "source_id": f"src_slg_vlaanderen_korian_contact_{TICK}",
                "title": "Korian Belgium contact (HQ same zetel as SLG Vlaanderen)",
                "url": f"{SITE}contact/",
                "publisher": "Korian Belgium",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; info@korian.be; +32 (0)3 443 76 50; {ADDR}",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_slg_vlaanderen_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope VZW RVT)",
                "source_id": "src_slg_vlaanderen_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {OMZET_YOY} vs YE2024 {OMZET24}; equity thin {EQUITY}",
            },
            {
                "budget_id": "bud_slg_vlaanderen_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_slg_vlaanderen_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {BRUTO_YOY} vs YE2024 {BRUTO24}",
            },
            {
                "budget_id": "bud_slg_vlaanderen_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_slg_vlaanderen_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {PNL_YOY} vs YE2024 PROFIT {PNL24}",
            },
            {
                "budget_id": "bud_slg_vlaanderen_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity (thin vs omzet)",
                "source_id": "src_slg_vlaanderen_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {EQUITY_YOY} vs YE2024 {EQUITY24}; thin vs omzet {OMZET}",
            },
            {
                "budget_id": "bud_slg_vlaanderen_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_slg_vlaanderen_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE {FTE} {FTE_YOY} vs YE2024 {FTE24}",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "SLG Vlaanderen YE2025 leftover dual "
                    "(omzet JUMP 115.87m / pnl FLIP LOSS / equity thin)"
                ),
                "entity_id": ENTITY,
                "beneficiary": (
                    "RVT residents via Senior Living Group Vlaanderen / Korian path"
                ),
                "legal_basis": (
                    f"VZW residential care / publiek gesubsidieerde RVT "
                    f"(KBO {KBO}; NACE 87.101; 29 VE)"
                ),
                "decision_date": "2026-07-28",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": CW_EN,
                "stated_goal": (
                    "Non-profit residential elderly care (SLG Vlaanderen / Korian)"
                ),
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain pnl FLIP LOSS and equity thin "
                    "vs 115.87m omzet; map dual SLG Operaties / Korian Belgium"
                ),
                "source_id": "src_slg_vlaanderen_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": (
                    "Vlaanderen>Antwerpen>Kontich>SLG_Vlaanderen>JR2025_statutory_L5"
                ),
                "notes": (
                    f"tick{TICK} EVERY-10; Medium CW; omzet primary envelope; assets/debt Unknown; "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                    "dual SLG Operaties 0845.064.196; DISTINCT Armonea/Always Home/emeis/Colisée"
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
                    "SLG Vlaanderen omzet JUMP 115.87m / pnl FLIP LOSS / equity thin (YE2025)"
                ),
                "level": "L5",
                "type": "wzc_vzw_statutory_private_care",
                "hierarchy_path": (
                    "Vlaanderen>Antwerpen>Kontich>SLG_Vlaanderen>JR2025"
                ),
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} {OMZET_YOY} (primary); bruto {BRUTO} "
                    f"{BRUTO_YOY}; pnl LOSS {PNL} {PNL_YOY}; equity {EQUITY} {EQUITY_YOY} "
                    f"thin vs omzet; FTE {FTE} {FTE_YOY}; assets/debt Unknown pending NBB PDF"
                ),
                "confidence": "medium",
                "source_id": "src_slg_vlaanderen_jr2025_cw_en",
                "beneficiaries": "RVT residents (29 VE); public Zorgkas day-price path",
                "stated_goal": "Non-profit residential elderly care (Korian/SLG)",
                "measured_outcome": (
                    f"omzet {OMZET_YOY}; bruto {BRUTO_YOY}; pnl {PNL_YOY}; "
                    f"equity {EQUITY_YOY}; FTE {FTE_YOY}"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": (
                    "FOI NBB PDF + equity-thin/LOSS path + 29 VE Zorgkas split; "
                    "map dual SLG Operaties / Korian Belgium related-party flows"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK} EVERY-10; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW "
                    "still YE2024; dual SLG Operaties; DISTINCT Armonea/Always Home/emeis"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Senior Living Group Vlaanderen VZW (SLG Vlaanderen / Kontich)",
                "name_fr": "Senior Living Group Vlaanderen ASBL (SLG Vlaanderen / Kontich)",
                "name_en": "Senior Living Group Vlaanderen VZW (SLG Vlaanderen / Kontich)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} "
                    f"Actief VZW 29 VE; NACE 87.101 RVT; omzet JUMP {OMZET/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m pnl FLIP LOSS {PNL/1e6:.2f}m equity DROP "
                    f"thin {EQUITY/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown; neerlegging "
                    f"{FILED}; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    f"{ADDR}; bestuurder Korian Belgium 0869.769.702; {EMAIL}; "
                    "dual nv_slg_operaties_vlaanderen; DISTINCT Armonea/Always Home/emeis/Colisée"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": (
                    "Vlaanderen>Antwerpen>Kontich>SLG_Vlaanderen>NBB_PDF_assets_debt_pnl_flip_equity_thin"
                ),
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); "
                    "pnl FLIP LOSS + equity thin path; 29 VE Zorgkas/IFIC vs private split; "
                    "dual SLG Operaties / Korian Belgium related-party map"
                ),
                "why_it_matters": (
                    "Medium CW shows 115.87m omzet Korian-path VZW with equity only 0.40m "
                    "and pnl FLIP to LOSS — public-care day-price continuity risk without "
                    "balance-sheet transparency"
                ),
                "priority": "8",
                "recipient_body": "Senior Living Group Vlaanderen VZW / Korian Belgium",
                "recipient_email": EMAIL,
                "recipient_postal": f"{ADDR} (tel +32 (0)3 443 76 50)",
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
                "status": "ready",
                "date_ready": "2026-08-25",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM,
                "linked_leaderboard_id": LB,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"tick{TICK} EVERY-10; human-send only; Medium CW; next every-10 2110"
                ),
            }
        ],
    )

    write_foi_draft()
    update_research_queue()
    write_loop_state()
    append_log()
    print(
        f"OK tick{TICK} EVERY-10 + {ENTITY} omzet={OMZET} pnl={PNL} "
        f"equity={EQUITY} pi={PI} gap={GAP}"
    )


if __name__ == "__main__":
    main()

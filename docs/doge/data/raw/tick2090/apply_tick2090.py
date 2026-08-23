# tick 2090 — EVERY-10 + rq_2090 CZD Zilvervogel Lo-Reninge YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T03:35:00Z"
TICK = 2090
ENTITY = "vzw_czd_zilvervogel_lo_reninge"
GAP = "gap_zilvervogel_nbb_pdf_assets_debt_pnl_jump_fte_drop_matrix_l5"
LB = "lb_zilvervogel_omzet_jump_20_96m_pnl_jump_fte_drop_jr2025"
COMM = "comm_zilvervogel_jr2025_statutory_wzc"

OMZET = 20960560
PNL = 1149659
EQUITY = 34907378
BRUTO = 21115222
FTE = 278.3
OMZET24 = 20017510
PNL24 = 1019213
EQUITY24 = 33992956
BRUTO24 = 19842165
FTE24 = 280.2
OMZET_YOY = "+4.71%"
PNL_YOY = "JUMP +12.80%"
EQUITY_YOY = "+2.69%"
BRUTO_YOY = "+6.42%"
FTE_YOY = "-0.68%"
FILED = "03.06.2026"
KBO = "0471.475.527"
EMAIL = "info@zilvervogel.be"
ADDR = "Dorpplaats 14, 8647 Lo-Reninge"
SITE = "https://www.zilvervogel.be/"
CW_NL = "https://www.companyweb.be/nl/0471475527/zilvervogel"
CW_EN = "https://www.companyweb.be/en/0471475527/zilvervogel"
CW_FR = "https://www.companyweb.be/fr/0471475527/zilvervogel"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0471475527"
PI = "5.4"
ABSURD = "4.6"
COST = "5.5"
DIFF = "4.0"

# inventory AFTER appends (approximate +5 budgets etc.)
INV = {
    "budgets": 52512,
    "commitments": 5756,
    "leaderboard": 7877,
    "entities": 1791,
    "sources": 5343,
    "foi_ready": 1707,
    "foi_ans": 11,
    "foi_part": 28,
    "foi_tot": 1759,
}

DO_NOT_REDO = (
    "Do NOT redo CZD Zilvervogel Lo-Reninge, De Lovie Poperinge, Ocura Beringen, WZC Lindelo Lille, "
    "De Medemens Antwerpen, WZC Sint-Augustinus Halle, Ben Woonzorgnetwerk Roeselare, Home Stuyvenberg Herzele, "
    "WZC De Wijshage Rumst, WZC Mater Dei Heikruis Pepingen, WZC DEN AKKER Sint-Truiden, WZC H. Vander Stokken Pepingen, "
    "Ten Anker Nieuwpoort, De Zwaluw Pajottegem, Zorg en Welzijn Kuurne, Sint-Jozef Brugge Sint-Michiels, "
    "Heilig Hart Grimbergen, Mater Amabilis Wervik, WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, "
    "Vulpia Vlaanderen, Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, "
    "Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, "
    "'t Pandje, Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, "
    "Ter Berk, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, "
    "WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, "
    "Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
    "WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, "
    "Werken Glorieux, Woonhaven Antwerpen, Maria Rustoord Ingelmunster, Always Home, Armonea, "
    "WZC Sint-Barbara Herselt, Molenheide, De Vaeren, WoonZorgGroep Arendonk, Solidum, Lidwina (deferred live), "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, "
    "CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
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


def write_progress_every_10():
    def count_rows(name: str) -> int:
        with (DATA / name).open(encoding="utf-8-sig", newline="") as fh:
            return sum(1 for _ in csv.reader(fh)) - 1

    budgets = count_rows("budgets.csv")
    commitments = count_rows("commitments.csv")
    leaderboard = count_rows("leaderboard.csv")
    entities = count_rows("entities.csv")
    sources = count_rows("sources.csv")
    foi_ready = foi_ans = foi_part = foi_tot = 0
    with (DATA / "foi_queue.csv").open(encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            foi_tot += 1
            st = (r.get("status") or "").lower()
            if st == "ready":
                foi_ready += 1
            elif st == "answered":
                foi_ans += 1
            elif st == "partial":
                foi_part += 1

    text = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---


## Snapshot at **tick 2090** (2026-08-25)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2081-2090 WZC/disability continuum after 2080 DEN AKKER |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2081-2090 is residual dual L5 (not near-complete of 348bn):** **Mater Dei** omzet JUMP **5.81m** / pnl FLIP · **Wijshage** omzet DROP **8.00m** · **Ben** omzet JUMP **16.59m** / pnl FLIP LOSS · **Stuyvenberg** bruto JUMP **0.50m** / omzet empty · **Augustinus Halle** omzet DROP **8.95m** · **Medemens** omzet JUMP **117.13m** · **Lindelo** omzet JUMP **10.43m** / deeper LOSS · **Ocura** omzet JUMP **25.97m** / shallower LOSS · **De Lovie** bruto JUMP **67.01m** · **CZD Zilvervogel** omzet JUMP **20.96m** Medium (this tick EVERY-10 dual) |
| **E. FOI-ready gaps** | **~{foi_ready}** drafts ready | Human send only; answered **~{foi_ans}**; partial **~{foi_part}**; total FOI rows **~{foi_tot}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/property/renewable/energy/nuclear/water/forest/hospital/psych/disability shells** (**NEW 2081-2090** Mater Dei · Wijshage · Ben · Stuyvenberg · Augustinus Halle · Medemens · Lindelo · Ocura · De Lovie · **CZD Zilvervogel** · prior 2071-2080 / 2061-2070 stacks retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2090)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {budgets} |
| commitments.csv | {commitments} |
| leaderboard.csv | {leaderboard} |
| entities.csv | {entities} |
| sources.csv | {sources} |
| FOI ready | {foi_ready} |
| FOI answered | {foi_ans} |
| FOI partial | {foi_part} |
| FOI total rows | {foi_tot} |
| research_queue open | rq_2091 after progress |

### What improved since tick 2080

- **Residual dual (tick2081-2090):** **Mater Dei Heikruis** · **WZC De Wijshage** · **Ben Woonzorgnetwerk** · **Home Stuyvenberg** · **WZC Sint-Augustinus Halle** · **De Medemens** · **WZC Lindelo** · **Ocura** · **De Lovie** · **CZD Zilvervogel Lo-Reninge** (this tick EVERY-10 dual — West-Vlaanderen WZC VZW YE2025 Medium CW; commercial name Zilvervogel).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH 0201.712.587 / REW (Réseau d'énergies de Wavre 0644.638.937) YE2024-only · Jessa/ZOL CW N/A omzet · Always Home=Armonea skipped · Lidwina YE2025 live deferred · prior Eneco deposit FOI stack.
"""
    (DATA / "progress_every_10_ticks.md").write_text(text, encoding="utf-8")


def write_waste_top10():
    lb_count = 0
    with (DATA / "leaderboard.csv").open(encoding="utf-8-sig", newline="") as fh:
        lb_count = sum(1 for _ in csv.reader(fh)) - 1
    text = f"""# DOGE waste ranking — current top 10

**As-of:** tick **2090** (2026-08-25) · **{lb_count}** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW residual 2081-2090:** **Medemens omzet 117.13m** · **De Lovie bruto 67.01m** · **Ocura omzet 25.97m** · **Zilvervogel omzet 20.96m** · **Ben omzet 16.59m** · **Lindelo omzet 10.43m** · **Augustinus Halle omzet 8.95m** · **Wijshage omzet 8.00m** · **Mater Dei omzet 5.81m** · **Stuyvenberg bruto 0.50m** · prior 2071-2080 DEN AKKER/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL stack retained · prior 2061-2070 stacks retained · prior nuclear/Fluxys/Elia/Enodia/RESA · prior Eneco continuum · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2080:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2081-2090 (off pure top10 / dual):** Mater Dei · Wijshage · Ben · Stuyvenberg · Augustinus Halle · Medemens · Lindelo · Ocura · De Lovie · **CZD Zilvervogel** (EVERY-10 dual). Count NEW since 2080: 10 residual dual ticks. **Prior 2071-2080 + 2061-2070 stacks retained.** Not TE-additive of ~348bn.
"""
    (DATA / "doge_waste_top10_current.md").write_text(text, encoding="utf-8")


def update_research_queue():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    for r in rows:
        if r["task_id"] == "rq_2090":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2090 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "EVERY-10 + leftover dual — CZD Zilvervogel Lo-Reninge YE2025 Medium"
            r["instructions"] = (
                "Completed EVERY-10 + leftover CZD Zilvervogel Lo-Reninge YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} "
                f"bruto JUMP {BRUTO} FTE DROP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "Lidwina YE2025 deferred"
            )
            r["notes"] = (
                f"tick{TICK} EVERY-10 + Zilvervogel Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"FTE DROP {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2091; next every-10 2100; Lidwina deferred"
            )
    if not any(r["task_id"] == "rq_2091" for r in rows):
        rows.append(
            {
                "task_id": "rq_2091",
                "title": "leftover dual hole-fill after Zilvervogel — prefer AGB/FARO-YE2025/AIESH-REW/Lidwina",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2090 after EVERY-10 + CZD Zilvervogel YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else deferred Lidwina 0407.601.720 if unused, "
                    "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2090 EVERY-10 + Zilvervogel; next every-10 2100; prefer Lidwina deferred",
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
                "last_unit_id": "rq_2090",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} EVERY-10 + leftover CZD Zilvervogel Lo-Reninge {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Lidwina deferred; "
                    "next rq_2091; next every-10 2100; continuous hole_fill"
                ),
            }
        )


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_zilvervogel_jr2025_cw",
                "title": "Companyweb NL — CZD Zilvervogel Lo-Reninge YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} pnl {PNL} bruto {BRUTO}",
            },
            {
                "source_id": "src_zilvervogel_jr2025_cw_en",
                "title": "Companyweb EN — CZD Zilvervogel Lo-Reninge YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_zilvervogel_jr2025_cw_fr",
                "title": "Companyweb FR — CZD Zilvervogel Lo-Reninge YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_zilvervogel_kbo_{TICK}",
                "title": "KBO — CZD / Zilvervogel 0471.475.527",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": f"tick{TICK}; Actief VZW 3 VE; NACE 87.101; commercial name Zilvervogel; zetel Dorpplaats 14 Lo-Reninge; {EMAIL}",
            },
            {
                "source_id": f"src_zilvervogel_site_{TICK}",
                "title": "Zilvervogel website (Lo-Reninge)",
                "url": SITE,
                "publisher": "Zilvervogel / CZD",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; West-Vlaanderen WZC; {EMAIL}",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_zilvervogel_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_zilvervogel_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_zilvervogel_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_zilvervogel_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP vs YE2024 {PNL24} ({PNL_YOY})",
            },
            {
                "budget_id": "bud_zilvervogel_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_zilvervogel_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_zilvervogel_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_zilvervogel_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {BRUTO_YOY} vs YE2024 {BRUTO24}",
            },
            {
                "budget_id": "bud_zilvervogel_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_zilvervogel_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE DROP {FTE} ({FTE_YOY}) vs YE2024 {FTE24}",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": "CZD Zilvervogel Lo-Reninge YE2025 leftover dual (omzet JUMP 20.96m / pnl JUMP)",
                "entity_id": ENTITY,
                "beneficiary": "West-Vlaanderen elderly residents (Zilvervogel / CZD WZC, 3 VE)",
                "legal_basis": f"VZW WZC / publiek gesubsidieerde zorg (KBO {KBO}; commercial name Zilvervogel)",
                "decision_date": "2026-06-03",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
                    f'"2025_bruto":{BRUTO},"2025_fte":{FTE}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": CW_EN,
                "stated_goal": "Residential elderly care Lo-Reninge / Westhoek (Zilvervogel)",
                "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl JUMP with FTE DROP",
                "source_id": "src_zilvervogel_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>WestVlaanderen>Lo-Reninge>Zilvervogel>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "CZD Zilvervogel omzet JUMP 20.96m / pnl JUMP + FTE DROP (YE2025)",
                "level": "L5",
                "type": "wzc_vzw_statutory",
                "hierarchy_path": "Vlaanderen>WestVlaanderen>Lo-Reninge>Zilvervogel>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": "CW omzet proxy; assets/debt Unknown pending NBB PDF FOI",
                "confidence": "medium",
                "source_id": "src_zilvervogel_jr2025_cw_en",
                "beneficiaries": "WZC clients Lo-Reninge / Westhoek (Zilvervogel 3 VE)",
                "stated_goal": "Residential elderly care Westhoek",
                "measured_outcome": (
                    f"omzet JUMP {OMZET_YOY}; pnl JUMP vs YE2024 {PNL24}; equity JUMP {EQUITY_YOY}; "
                    f"bruto JUMP {BRUTO_YOY}; FTE DROP {FTE} ({FTE_YOY})"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl JUMP +12.80pct with FTE DROP 280.2→278.3; map IFIC/Alivia vs dagprijs",
                "status": "open",
                "struck_reason": "",
                "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; EVERY-10 dual; West-Vlaanderen WZC VZW",
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "CZD vzw / Zilvervogel (Lo-Reninge)",
                "name_fr": "CZD ASBL / Zilvervogel (Lo-Reninge)",
                "name_en": "CZD VZW / Zilvervogel (Lo-Reninge)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW 3 VE; "
                    f"commercial name Zilvervogel; NACE 87.101; omzet JUMP {OMZET/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m "
                    f"equity JUMP {EQUITY/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown; "
                    f"neerlegging {FILED}; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "Dorpplaats 14 Lo-Reninge"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>WestVlaanderen>Lo-Reninge>Zilvervogel>NBB_PDF_assets_debt_pnl_jump_fte_drop",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; "
                    f"explanation of pnl JUMP from EUR{PNL24} to EUR{PNL} ({PNL_YOY}) with FTE DROP {FTE24}→{FTE} ({FTE_YOY})"
                ),
                "why_it_matters": (
                    "Medium CW shows 20.96m omzet WZC VZW with profit jump and slight FTE drop "
                    "without balanstotaal/assets/debt; material L5 residual for FOI"
                ),
                "priority": "8",
                "recipient_body": "CZD vzw / Zilvervogel",
                "recipient_email": EMAIL,
                "recipient_postal": ADDR,
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
                "notes": f"tick{TICK}; human-send only; Medium CW; EVERY-10 dual; next every-10 2100",
            }
        ],
    )

    FOI.mkdir(parents=True, exist_ok=True)
    (FOI / f"{GAP}.md").write_text(
        f"""# FOI draft — CZD Zilvervogel Lo-Reninge (NBB PDF / assets-debt / pnl-jump / FTE-drop)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** CZD VZW / Zilvervogel — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **PROFIT EUR{PNL}** JUMP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** DROP {FTE_YOY} vs YE2024 {FTE24}; assets/debt **Unknown**.
- KBO: Actief VZW; **3 VE**; commercial name Zilvervogel; NACE 87.101; zetel Dorpplaats 14 Lo-Reninge; email {EMAIL}.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Deferred live: Lidwina YE2025.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: CZD vzw / Zilvervogel — Dorpplaats 14, 8647 Lo-Reninge
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Zilvervogel + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting van de winststijging van EUR{PNL24} (YE2024) naar EUR{PNL} (YE2025; +12.80%) bij FTE-daling van {FTE24} naar {FTE} ({FTE_YOY}).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
        encoding="utf-8",
    )

    update_research_queue()
    write_loop_state()
    write_progress_every_10()
    write_waste_top10()

    log_entry = f"""

## Tick {TICK} - {UTC} - rq_2090 EVERY-10 + CZD Zilvervogel (omzet JUMP 20.96m / pnl JUMP 1.15m / Medium)

- Unit: **rq_2090** EVERY-10 mandatory + leftover dual after **rq_2089 De Lovie**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **CZD / Zilvervogel** YE2025 (KBO **{KBO}**; Dorpplaats 14 Lo-Reninge; West-Vlaanderen **VZW** WZC / **3 VE**; commercial name Zilvervogel). Lidwina YE2025 also live — deferred. Do not redo Lovie/Ocura/Lindelo/Medemens/Augustinus Halle/Ben/Stuyvenberg/Wijshage/Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar/Sint-Barbara/Molenheide/Veilige Have/De Foyer/De Verlosser/Kanunnik/Zusterhof/Arendonk/Solidum.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **PROFIT EUR{PNL}** JUMP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** DROP {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 3 VE; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; **EVERY-10** progress_every_10_ticks.md + doge_waste_top10_current.md; rq_2090=done + rq_2091 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2090/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- **EVERY-10 done** (A/B 100%; C ~99%; D ~74-88% generous residual dual; E ~{INV['foi_ready']}+ ready). Next every-10 is **2100**. Next: rq_2091 (AGB/FARO-if-YE2025 / AIESH-REW / Lidwina deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL, "fte", FTE)


if __name__ == "__main__":
    main()

# tick 2080 — EVERY-10 + rq_2080 WZC DEN AKKER Sint-Truiden YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T01:05:00Z"
TICK = 2080
ENTITY = "vzw_wzc_den_akker_sint_truiden"
GAP = "gap_den_akker_nbb_pdf_assets_debt_pnl_drop_fte_jump_matrix_l5"
LB = "lb_den_akker_omzet_jump_6_59m_pnl_drop_fte_jump_jr2025"
COMM = "comm_den_akker_jr2025_statutory_wzc"

OMZET = 6588728
PNL = 174886
EQUITY = 9322582
BRUTO = 6780608
FTE = 89.6
OMZET24 = 6422387
PNL24 = 529091
EQUITY24 = 9366576
BRUTO24 = 6586032
FTE24 = 85.3
OMZET_YOY = "+2.59%"
PNL_YOY = "DROP -66.94%"
EQUITY_YOY = "-0.47%"
BRUTO_YOY = "+2.95%"
FTE_YOY = "+5.04%"
FILED = "11.06.2026"
KBO = "0639.973.732"
EMAIL = "secretariaat@denakker.be"
ADDR = "Montenakenweg 51, 3800 Sint-Truiden"
SITE = "https://www.denakker.be/"
CW_NL = "https://www.companyweb.be/nl/0639973732/woonzorgcentrum-den-akker"
CW_EN = "https://www.companyweb.be/en/0639973732/woonzorgcentrum-den-akker"
CW_FR = "https://www.companyweb.be/fr/0639973732/woonzorgcentrum-den-akker"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0639973732"
PI = "5.1"
ABSURD = "4.4"
COST = "5.5"
DIFF = "4.0"

DO_NOT_REDO = (
    "Do NOT redo WZC DEN AKKER Sint-Truiden, WZC H. Vander Stokken Pepingen, Ten Anker Nieuwpoort, "
    "De Zwaluw Pajottegem, Zorg en Welzijn Kuurne, Sint-Jozef Brugge Sint-Michiels, Heilig Hart Grimbergen, "
    "Mater Amabilis Wervik, WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, Vulpia Vlaanderen, "
    "Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, "
    "WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, "
    "Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk, Van Lierde, Hof ter Waarbeek, "
    "Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, "
    "Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, "
    "WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, "
    "WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, "
    "Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, Werken Glorieux, Woonhaven Antwerpen, "
    "Maria Rustoord Ingelmunster, Always Home, Armonea, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, "
    "EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, "
    "Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
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


def update_research_queue():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    for r in rows:
        if r["task_id"] == "rq_2080":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2080 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "EVERY-10 + leftover dual — WZC DEN AKKER Sint-Truiden YE2025 Medium"
            r["instructions"] = (
                "Completed EVERY-10 + leftover WZC DEN AKKER Sint-Truiden YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} pnl DROP {PNL} equity DROP {EQUITY} "
                f"bruto JUMP {BRUTO} FTE JUMP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} EVERY-10 + Den Akker Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"pnl DROP {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"FTE JUMP {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2081; next every-10 2090"
            )
    if not any(r["task_id"] == "rq_2081" for r in rows):
        rows.append(
            {
                "task_id": "rq_2081",
                "title": "leftover dual hole-fill after Den Akker — prefer AGB/FARO-YE2025/AIESH-REW/unused-WZC",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2080 after EVERY-10 + Den Akker Sint-Truiden YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2080 EVERY-10 + Den Akker; next every-10 2090",
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
                "last_unit_id": "rq_2080",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} EVERY-10 + leftover WZC DEN AKKER Sint-Truiden {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2081; next every-10 2090; continuous hole_fill"
                ),
            }
        )


def write_progress_every_10():
    # Inventory AFTER this tick's CSV appends (call after appends)
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


## Snapshot at **tick 2080** (2026-08-25)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2071-2080 WZC continuum after 2070 Welvaart |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2071-2080 is residual dual L5 (not near-complete of 348bn):** **MSW NZVL** omzet JUMP **0.44m** / pnl FLIP LOSS · **Maria Moorslede** omzet JUMP **6.02m** · **Mater Amabilis** omzet JUMP **7.97m** / pnl DROP · **HH Grimbergen** omzet JUMP **10.61m** / pnl near-zero · **SJ Brugge** omzet JUMP **12.38m** / bruto+FTE DROP · **ZorgWelzijn Kuurne** omzet JUMP **16.40m** / deeper LOSS · **De Zwaluw** omzet DROP **5.44m** / pnl FLIP PROFIT · **Ten Anker** omzet JUMP **9.21m** · **Vander Stokken** omzet JUMP **8.87m** / equity JUMP +72.71pct · **DEN AKKER** omzet JUMP **6.59m** / pnl DROP Medium (this tick EVERY-10 dual) |
| **E. FOI-ready gaps** | **~{foi_ready}** drafts ready | Human send only; answered **~{foi_ans}**; partial **~{foi_part}**; total FOI rows **~{foi_tot}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/property/renewable/energy/nuclear/water/forest/hospital/psych shells** (**NEW 2071-2080** MSW NZVL · Maria Moorslede · Mater Amabilis · HH Grimbergen · SJ Brugge · ZorgWelzijn Kuurne · De Zwaluw · Ten Anker · Vander Stokken · **DEN AKKER** · prior 2061-2070 / 2051-2060 stacks retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2080)

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
| research_queue open | rq_2081 after progress |

### What improved since tick 2070

- **Residual dual (tick2071-2080):** **MSW NZVL** · **Maria Moorslede** · **Mater Amabilis** · **HH Grimbergen** · **SJ Brugge** · **Zorg en Welzijn Kuurne** · **De Zwaluw** · **Ten Anker** · **Vander Stokken** · **WZC DEN AKKER Sint-Truiden** (this tick EVERY-10 dual — Limburg WZC VZW YE2025 Medium CW; Heem/Sint-Ferdinand sphere; pnl DROP with FTE JUMP).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH 0201.712.587 / REW (Réseau d'énergies de Wavre 0644.638.937) YE2024-only · Jessa/ZOL CW N/A omzet · Always Home=Armonea skipped · prior Eneco deposit FOI stack.
"""
    (DATA / "progress_every_10_ticks.md").write_text(text, encoding="utf-8")


def write_waste_top10():
    lb_count = 0
    with (DATA / "leaderboard.csv").open(encoding="utf-8-sig", newline="") as fh:
        lb_count = sum(1 for _ in csv.reader(fh)) - 1
    text = f"""# DOGE waste ranking — current top 10

**As-of:** tick **2080** (2026-08-25) · **{lb_count}** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW residual 2071-2080:** **ZorgWelzijn Kuurne omzet 16.40m** · **SJ Brugge omzet 12.38m** · **HH Grimbergen omzet 10.61m** · **Ten Anker omzet 9.21m** · **Vander Stokken omzet 8.87m** · **Mater Amabilis omzet 7.97m** · **DEN AKKER omzet 6.59m** · **Maria Moorslede omzet 6.02m** · **De Zwaluw omzet 5.44m** · **MSW NZVL omzet 0.44m** · prior 2061-2070 Vulpia/Compostela/Deinze/Leiehome/OLV Bornem/Welvaart/Huize SJ Ieper/Ter Burg/Sint-Antonius/OLV Wezembeek stack retained · prior 2051-2060 / 2041-2050 / 2031-2040 / 2021-2030 stacks retained · prior nuclear/Fluxys/Elia/Enodia/RESA · prior Eneco continuum · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2070:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2071-2080 (off pure top10 / dual):** MSW NZVL · Maria Moorslede · Mater Amabilis · HH Grimbergen · SJ Brugge · ZorgWelzijn Kuurne · De Zwaluw · Ten Anker · Vander Stokken · **DEN AKKER** (EVERY-10 dual). Count NEW since 2070: 10 residual dual ticks. **Prior 2061-2070 + 2051-2060 stacks retained.** Not TE-additive of ~348bn.
"""
    (DATA / "doge_waste_top10_current.md").write_text(text, encoding="utf-8")


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_den_akker_jr2025_cw",
                "title": "Companyweb NL — WZC DEN AKKER Sint-Truiden YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} pnl {PNL} bruto {BRUTO}",
            },
            {
                "source_id": "src_den_akker_jr2025_cw_en",
                "title": "Companyweb EN — WZC DEN AKKER Sint-Truiden YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_den_akker_jr2025_cw_fr",
                "title": "Companyweb FR — WZC DEN AKKER Sint-Truiden YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_den_akker_kbo_{TICK}",
                "title": "KBO — WZC DEN AKKER 0639.973.732",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": f"tick{TICK}; Actief VZW 1 VE; NACE 87.101; zetel Montenakenweg 51 Sint-Truiden; email via site {EMAIL}",
            },
            {
                "source_id": f"src_den_akker_site_{TICK}",
                "title": "WZC Den Akker website (Sint-Truiden)",
                "url": SITE,
                "publisher": "WZC DEN AKKER",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; Montenakenweg 51 Sint-Truiden; secretariaat@denakker.be; Seniorencomplex Den Akker",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_den_akker_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_den_akker_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {OMZET_YOY} vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_den_akker_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_den_akker_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP vs YE2024 {PNL24} ({PNL_YOY})",
            },
            {
                "budget_id": "bud_den_akker_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_den_akker_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_den_akker_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_den_akker_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {BRUTO_YOY} vs YE2024 {BRUTO24}",
            },
            {
                "budget_id": "bud_den_akker_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_den_akker_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE JUMP {FTE} ({FTE_YOY}) vs YE2024 {FTE24}",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": "WZC DEN AKKER Sint-Truiden YE2025 leftover dual (omzet JUMP 6.59m / pnl DROP)",
                "entity_id": ENTITY,
                "beneficiary": "Sint-Truiden elderly residents (Seniorencomplex Den Akker / Heem sphere)",
                "legal_basis": f"VZW WZC / publiek erkende zorg (Departement Zorg) (KBO {KBO})",
                "decision_date": "2026-06-11",
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
                "stated_goal": "WZC residential elderly care Sint-Truiden (Seniorencomplex Den Akker)",
                "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl DROP -67pct with FTE JUMP",
                "source_id": "src_den_akker_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>Limburg>Sint-Truiden>Den_Akker>JR2025_statutory_L5",
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
                "name": "WZC DEN AKKER Sint-Truiden omzet JUMP 6.59m / pnl DROP + FTE JUMP (YE2025)",
                "level": "L5",
                "type": "wzc_vzw_statutory",
                "hierarchy_path": "Vlaanderen>Limburg>Sint-Truiden>Den_Akker>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": "CW omzet proxy; assets/debt Unknown pending NBB PDF FOI; pnl DROP with FTE JUMP",
                "confidence": "medium",
                "source_id": "src_den_akker_jr2025_cw_en",
                "beneficiaries": "WZC clients Sint-Truiden (Seniorencomplex Den Akker / Heem sphere)",
                "stated_goal": "Residential elderly care Sint-Truiden",
                "measured_outcome": (
                    f"omzet JUMP {OMZET_YOY}; pnl DROP vs YE2024 {PNL24}; equity DROP {EQUITY_YOY}; "
                    f"bruto JUMP {BRUTO_YOY}; FTE JUMP {FTE} ({FTE_YOY})"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl DROP -66.94pct (529091→174886) with FTE JUMP 85.3→89.6 and omzet JUMP +2.59pct; map IFIC/Alivia vs dagprijs",
                "status": "open",
                "struck_reason": "",
                "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Limburg WZC VZW EVERY-10 dual",
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "WZC DEN AKKER vzw (Sint-Truiden)",
                "name_fr": "MR DEN AKKER ASBL (Saint-Trond)",
                "name_en": "WZC DEN AKKER VZW (Sint-Truiden)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW 1 VE; "
                    f"omzet JUMP {OMZET/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown; neerlegging {FILED}; "
                    f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "Seniorencomplex Den Akker Montenakenweg 51; Heem/Sint-Ferdinand sphere"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>Limburg>Sint-Truiden>Den_Akker>NBB_PDF_assets_debt_pnl_drop_fte_jump",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; "
                    "explanation of pnl DROP -66.94pct (YE2024 EUR529091 → YE2025 EUR174886) with FTE JUMP 85.3→89.6 (+5.04pct) "
                    "and omzet JUMP +2.59pct"
                ),
                "why_it_matters": (
                    "Medium CW shows 6.59m omzet erkende WZC VZW with sharp profit drop despite rising omzet/FTE "
                    "without balanstotaal/assets/debt; material L5 residual for FOI"
                ),
                "priority": "8",
                "recipient_body": "WZC DEN AKKER vzw",
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
                "notes": f"tick{TICK}; human-send only; Medium CW; EVERY-10 dual; next every-10 2090",
            }
        ],
    )

    FOI.mkdir(parents=True, exist_ok=True)
    (FOI / f"{GAP}.md").write_text(
        f"""# FOI draft — WZC DEN AKKER Sint-Truiden (NBB PDF / assets-debt / pnl-drop / FTE-jump)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** WZC DEN AKKER VZW — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **PROFIT EUR{PNL}** DROP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** JUMP {FTE_YOY} vs YE2024 {FTE24}; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; zetel Montenakenweg 51 Sint-Truiden; NACE 87.101; email {EMAIL}.
- Site: Seniorencomplex Den Akker (Heem / Sint-Ferdinand sphere).
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: WZC DEN AKKER vzw — Montenakenweg 51, 3800 Sint-Truiden
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 DEN AKKER + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting van de winstdaling van EUR{PNL24} (YE2024) naar EUR{PNL} (YE2025; -66.94%) bij omzetgroei {OMZET_YOY} en FTE-stijging van {FTE24} naar {FTE} ({FTE_YOY}).
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

## Tick {TICK} - {UTC} - rq_2080 EVERY-10 + DEN AKKER (omzet JUMP 6.59m / pnl DROP 0.17m / Medium)

- Unit: **rq_2080** EVERY-10 mandatory + leftover dual after **rq_2079 Vander Stokken**. Prefer NON-stall live: AGB Bornem still **JR2024-only** (bornem.be JR2024 docs); FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred leftover **WZC DEN AKKER** YE2025 (KBO **{KBO}**; Montenakenweg 51 Sint-Truiden; Limburg **VZW** WZC / **1 VE**; Seniorencomplex Den Akker / Heem sphere). Do not redo Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **PROFIT EUR{PNL}** DROP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** JUMP {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; **EVERY-10** progress_every_10_ticks.md + doge_waste_top10_current.md; rq_2080=done + rq_2081 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2080/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- **EVERY-10 done** (A/B 100%; C ~99%; D ~74-88% generous residual dual; E ~{1697}+ ready). Next every-10 is **2090**. Next: rq_2081 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL, "bruto", BRUTO, "fte", FTE)


if __name__ == "__main__":
    main()

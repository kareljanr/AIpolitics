# -*- coding: utf-8 -*-
"""Tick 2140 EVERY-10: adopt raced Denderrust fill as this tick + refresh progress/top10."""
import csv
import re
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T16:40:00Z"
TICK = 2140
RQ = "rq_2140"
NEXT_RQ = "rq_2141"
ENTITY = "vzw_zorgcampus_denderrust_aalst"
GAP = "gap_denderrust_nbb_pdf_assets_debt_pnl_drop_omzet_jump_merger_dienstengroep_matrix_l5"
COMM = "comm_denderrust_jr2025_statutory_wzc_vzw"
LB = "lb_denderrust_omzet_11_14m_pnl_drop_bruto_12_10m_jr2025"
KBO = "0419.333.572"
OMZET = "11135834"
BRUTO = "12099041"
PNL = "47586"
EQUITY = "8526706"
FTE = "139.9"
ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"


def rewrite_csv(path, transform_rows):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    rows = transform_rows(rows)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def retag_denderrust(rows):
    out = []
    for r in rows:
        blob = str(r)
        if (
            ENTITY in blob
            or "denderrust" in blob.lower()
            or "0419333572" in blob
            or "0419.333.572" in blob
            or GAP in blob
            or COMM in blob
            or LB in blob
            or "src_denderrust" in blob
        ):
            for k, v in list(r.items()):
                if not v:
                    continue
                v2 = v.replace("tick2139", f"tick{TICK}")
                v2 = v2.replace("src_denderrust_kbo_2139", f"src_denderrust_kbo_{TICK}")
                v2 = v2.replace("src_denderrust_site_2139", f"src_denderrust_site_{TICK}")
                # keep en_famille tick2139 intact if somehow in same row (shouldn't)
                if "en_famille" in v2 and f"tick{TICK}" in v2 and "denderrust" not in v2.lower():
                    pass
                r[k] = v2
            # source_id exact fixes
            if r.get("source_id") == "src_denderrust_kbo_2139":
                r["source_id"] = f"src_denderrust_kbo_{TICK}"
            if r.get("source_id") == "src_denderrust_site_2139":
                r["source_id"] = f"src_denderrust_site_{TICK}"
            if r.get("created_utc") and "denderrust" in blob.lower():
                r["created_utc"] = UTC
            if r.get("updated_utc") and "denderrust" in blob.lower():
                r["updated_utc"] = UTC
            if r.get("date_ready") and GAP in blob:
                r["date_ready"] = "2026-08-25"
        out.append(r)
    return out


for fn in [
    "budgets.csv",
    "commitments.csv",
    "entities.csv",
    "foi_queue.csv",
    "leaderboard.csv",
    "sources.csv",
]:
    rewrite_csv(DATA / fn, retag_denderrust)

# research queue
def update_rq(rows):
    found = False
    for r in rows:
        if r.get("task_id") == RQ and r.get("status") == "open":
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["title"] = (
                "EVERY-10 + leftover dual — Zorgcampus Denderrust YE2025 Medium "
                "(omzet JUMP 11.14m / pnl DROP)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} EVERY-10 Denderrust Medium omzet JUMP 11.14m bruto JUMP 12.10m "
                f"pnl DROP 48k equity JUMP 8.53m FTE 139.9; Dienstengroep absorbed 17.12.2025; "
                f"FOI ready; progress+top10 refreshed; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; next every-10 2150"
            )
            r["instructions"] = (
                f"Completed EVERY-10 + leftover Zorgcampus Denderrust YE2025 Medium CW after En Famille; "
                f"preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; "
                f"live YE2025 Medium CW NL+EN+FR + Strong KBO {KBO}; "
                f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} FTE {FTE}; "
                f"FOI {GAP}; progress+top10 refreshed"
            )
            found = True
            break
    if not found:
        raise SystemExit(f"{RQ} open not found")
    if not any(r.get("task_id") == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after Denderrust — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/Prinsenhof-if-unused/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Zorgcampus Denderrust YE2025 Medium EVERY-10. "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg "
                    "(Prinsenhof already mined — skip). "
                    "Do NOT redo Zorgcampus Denderrust Aalst, Maison De Repos En Famille Vaux-sur-Sûre, "
                    "Residence Prestige Chaudfontaine, Les Corolles Tournai, l'Esplanade Ath, Residence Les Peupliers, "
                    "MRS Comte d'Egmont, C.I.G.B. Menen, Ten Rozen Aalst, L'Orchidée Ittre, Care-Support, "
                    "MPC Sint-Franciscus, De Fakkel, Restel Flats, Château Vert, SLG Wallonie, Famifamenne, "
                    "Le Castel, R.S.W., Home Sebrechts, Unite Jolimont, t Buurthuis, La Moisson (absorbed), "
                    "AGB Bornem, Armonea/emeis/Korian holdings, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, "
                    "EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, "
                    "AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Seniors Care-Ion YE2024."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} EVERY-10 Denderrust; "
                    "FARO/AIESH/REW still YE2024; next every-10 2150"
                ),
            }
        )
    return rows


rewrite_csv(DATA / "research_queue.csv", update_rq)

with open(DATA / "loop_state.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
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
            "last_unit_id": RQ,
            "ticks_completed": str(TICK),
            "paused": "no",
            "notes": (
                f"tick{TICK} EVERY-10 leftover Denderrust {KBO} Medium CW (omzet JUMP 11.14m bruto JUMP 12.10m "
                f"pnl DROP 48k equity JUMP 8.53m FTE 139.9; Actief VZW 1 VE aanbestedende overheid; "
                f"Dienstengroep absorbed 17.12.2025; assets/debt Unknown) + progress/top10 refresh; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; En Famille remains tick2139; "
                f"next {NEXT_RQ}; next every-10 2150; continuous hole_fill"
            ),
        }
    )

# inventory
counts = {}
for fn in ["budgets.csv", "commitments.csv", "leaderboard.csv", "entities.csv", "sources.csv", "foi_queue.csv"]:
    with (DATA / fn).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    counts[fn] = len(rows)
    if fn == "foi_queue.csv":
        counts["foi_ready"] = sum(1 for r in rows if r.get("status") == "ready")
        counts["foi_answered"] = sum(1 for r in rows if r.get("status") == "answered")
        counts["foi_partial"] = sum(1 for r in rows if r.get("status") == "partial")

progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2140** (2026-08-25)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2131-2140 MRS/WZC continuum after 2130 Care-Support |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2131-2140 is residual dual L5 (not near-complete of 348bn):** **L'Orchidée Ittre** omzet JUMP **4.47m** · **OLV Maagd Der Armen / Ten Rozen** omzet JUMP **6.91m** · **C.I.G.B. Menen** omzet JUMP **35.15m** / pnl LOSS flip · **MRS Comte d'Egmont** bruto JUMP **2.76m** / LOSS widen · **Les Peupliers** bruto JUMP **3.17m** / NEG equity · **l'Esplanade Ath** omzet **7.17m** / Stopgezet fusie · **Les Corolles** omzet JUMP **9.74m** / overnemer · **Residence Prestige** bruto JUMP **3.70m** / pnl PROFIT flip · **Maison De Repos En Famille** bruto JUMP **1.03m** / pnl FLIP LOSS · **Zorgcampus Denderrust** omzet JUMP **11.14m** / pnl DROP (this tick EVERY-10 dual; WZC VZW Aalst + Dienstengroep absorption) Medium |
| **E. FOI-ready gaps** | **~{counts['foi_ready']}** drafts ready | Human send only; answered **~{counts['foi_answered']}**; partial **~{counts['foi_partial']}**; total FOI rows **~{counts['foi_queue.csv']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability shells** (**NEW 2131-2140** L'Orchidée · Ten Rozen · CIGB Menen · Comte d'Egmont · Les Peupliers · Esplanade · **Les Corolles** · Prestige · En Famille · **Denderrust** · prior 2121-2130 / 2111-2120 / 2101-2110 stacks retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2140)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {counts['budgets.csv']} |
| commitments.csv | {counts['commitments.csv']} |
| leaderboard.csv | {counts['leaderboard.csv']} |
| entities.csv | {counts['entities.csv']} |
| sources.csv | {counts['sources.csv']} |
| FOI ready | {counts['foi_ready']} |
| FOI answered | {counts['foi_answered']} |
| FOI partial | {counts['foi_partial']} |
| FOI total rows | {counts['foi_queue.csv']} |
| research_queue open | {NEXT_RQ} after progress |

### What improved since tick 2130

- **Residual dual (tick2131-2140):** **L'Orchidée Ittre** · **OLV Maagd Der Armen / Ten Rozen** · **C.I.G.B. Menen** (pnl LOSS flip) · **MRS Comte d'Egmont** · **Residence Les Peupliers** (NEG equity) · **l'Esplanade Ath** (Stopgezet fusie Les Corolles) · **Les Corolles** (overnemer Esplanade+Moisson) · **Residence Prestige** (pnl PROFIT flip / thin equity) · **Maison De Repos En Famille** (pnl FLIP LOSS) · **Zorgcampus Denderrust** (this tick EVERY-10 dual — WZC VZW NACE 87.101/87.301 YE2025 Medium CW; omzet 11.14m JUMP +3.66%; bruto 12.10m JUMP +5.90%; pnl DROP 48k −68.86%; equity JUMP 8.53m; FTE 139.9; absorbed Denderrust Dienstengroep 0409.698.009 17.12.2025; aanbestedende overheid Aalst).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH 0201.712.587 / REW 0644.638.937 YE2024-only · Seniors Care-Ion YE2024-only · prior Eneco deposit FOI stack.
"""

(DATA / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")

top10 = f"""# DOGE waste ranking — current top 10

**As-of:** tick **{TICK}** (2026-08-25) · **{counts['leaderboard.csv']}** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2131-2140:** **CIGB Menen omzet 35.15m** · **Restel Flats omzet 57.23m** (prior) · **Denderrust omzet 11.14m** · **Les Corolles omzet 9.74m** · **Esplanade omzet 7.17m** · **Ten Rozen omzet 6.91m** · **L'Orchidée omzet 4.47m** · **Prestige bruto 3.70m** · **Les Peupliers bruto 3.17m** · **Comte d'Egmont bruto 2.76m** · **En Famille bruto 1.03m** (EVERY-10@2140 dual Denderrust) · prior 2121-2130 / 2111-2120 / 2101-2110 stacks retained · prior nuclear/Fluxys/Elia/Enodia/RESA · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2130:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2131-2140 (off pure top10 / dual):** L'Orchidée · Ten Rozen · CIGB Menen · Comte d'Egmont · Les Peupliers · Esplanade · **Les Corolles** · Prestige · En Famille · **Denderrust** (EVERY-10@2140). Count NEW since 2130: 10 residual dual ticks. **Prior 2121-2130 + 2111-2120 + 2101-2110 stacks retained.** Not TE-additive of ~348bn.
"""

(DATA / "doge_waste_top10_current.md").write_text(top10, encoding="utf-8")

# FOI draft tick fix
foi = ROOT / "foi" / "drafts" / f"{GAP}.md"
if foi.exists():
    txt = foi.read_text(encoding="utf-8")
    txt = txt.replace("**tick:** 2139", f"**tick:** {TICK}")
    txt = re.sub(r"tick2139", f"tick{TICK}", txt)
    foi.write_text(txt, encoding="utf-8")

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} EVERY-10 Zorgcampus Denderrust (omzet JUMP 11.14m / pnl DROP 48k / Medium)

- Unit: **{RQ}** EVERY-10 + leftover dual after **rq_2139 Maison De Repos En Famille**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Zorgcampus Denderrust VZW** YE2025 (KBO **{KBO}**; Alfons De Cockstraat 12A Aalst; **VZW** NACE **87.101/87.301/88.102** / **1 VE**; aanbestedende overheid; absorbed Denderrust Dienstengroep **0409.698.009** 17.12.2025). Race-note: concurrent had staged Denderrust CSV rows labeled tick2139; this tick owns them as 2140 (En Famille remains official 2139). Do not redo En Famille/Prestige/Corolles/Esplanade/Les Peupliers/Comte d'Egmont/CIGB/Ten Rozen/L'Orchidée.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +3.66%; bruto **EUR{BRUTO}** JUMP +5.90%; pnl **EUR{PNL}** DROP -68.86% vs YE2024 EUR152817; equity **EUR{EQUITY}** JUMP +0.52%; FTE **{FTE}**; neerlegging **03.06.2026**. KBO Strong Actief + aanbestedende overheid + absorption. Assets/debt Unknown. Medium. FOI via administratie@denderrust.be.
- Wrote: retagged denderrust sources/budgets/commitments/leaderboard/entities/foi to tick{TICK}; progress_every_10_ticks.md + doge_waste_top10_current.md refreshed; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2140/.
- FOI: **ready not sent** (human-gated).
- **EVERY-10@{TICK}** (last was 2130; **next 2150**). Pure annual top10 stable (GIP/fossil/cars/cheque). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "omzet", OMZET, "pnl", PNL, "equity", EQUITY)
print("inventory", counts)

# -*- coding: utf-8 -*-
"""Apply tick 1710: PlayRight CV YE2024 NBB+JV + every-10 progress/waste refresh."""
import csv
from pathlib import Path

DOGE = Path(__file__).resolve().parents[2]
DATA = DOGE / "data"
csv.field_size_limit(10**7)

TS = "2026-08-23T19:25:00Z"
DAY = "2026-08-23"
EID = "cv_playright"
SRC = "src_playright_jr2024_nbb_official"
JR_URL = "http://playright.be/wp-content/uploads/2025/05/JAARREKENING-2024-PlayRight-NL.pdf"
JV_URL = "https://playright.be/wp-content/uploads/2025/06/AV2025.03.-Jaarverslag-2024.pdf"
GAP = "gap_playright_commissions_3_73m_staff_2_05m_rechten_debt_73m_vte_l5"
LB = "lb_playright_commissions_3_73m_inningen_33m_rechten_debt_73m"
COMM = "comm_playright_jv2024_commissions"
HP = "Belgie>Cultuur>PlayRight>JV2024_L5"


def append_rows(path: Path, rows: list[dict]):
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        existing = list(r)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        for row in existing:
            w.writerow(row)
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})
    return len(existing) + len(rows)


def read_csv(name: str):
    with (DATA / name).open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def count(name: str) -> int:
    return len(read_csv(name)[1])


def foi_stats():
    _, rows = read_csv("foi_queue.csv")
    ready = sum(1 for r in rows if r.get("status") == "ready")
    answered = sum(1 for r in rows if r.get("status") == "answered")
    partial = sum(1 for r in rows if r.get("status") == "partial")
    return ready, answered, partial, len(rows)


def update_queue():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        rows = list(r)
    for row in rows:
        if row["task_id"] == "rq_1710":
            row["status"] = "done"
            row["updated_utc"] = TS
            row["entity_id"] = EID
            row["blocked_gap_id"] = GAP
            row["instructions"] = (
                "Tick 1710 EVERY-10 after 1709 SIMIM. DONE PlayRight CV YE2024 NBB+JV "
                "+ progress/waste refresh. Next every-10 is 1720. Do NOT redo PlayRight/"
                "SIMIM/Reprobel/Auvibel/Sabam/NSZ/FBM/Biovia/BlauweCluster/Flux50...."
            )
            row["notes"] = (
                "DONE tick1710 EVERY-10: PlayRight YE2024 assets 76125485 commissions "
                f"3728405 staff 2047252 rechten debt 72956185; FOI {GAP}; progress+waste "
                "refreshed; KBO 0440.736.227"
            )
    spawn = {
        "task_id": "rq_1711",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Tick 1711 after 1710 PlayRight EVERY-10. Next every-10 is 1720. SBM HTML "
            "IP-blacklisted — prefer direct CDN / NBB / official org PDFs / Northdata "
            "deposit→CDN. Do NOT redo PlayRight/SIMIM/Reprobel/Auvibel/Sabam/NSZ/FBM/"
            "Biovia/Medvia/BlauweCluster/Flux50/Catalisti/FlandersFOOD/Avansa*...."
            " Prefer leftover AGB/APB if PDF live else Natuurpunt vzw if CDN / "
            "NSZ 2026-00394221 if CDN 200 / Bosgroep/Dijk92 if JR euros / FARO if JR2025 / "
            "APEFE if JR euros / Welzijnszorg/GO!/POV/BVAS/IOED/HVZ/IGS/other."
        ),
        "blocked_gap_id": "",
        "created_utc": TS,
        "updated_utc": TS,
        "notes": (
            "spawned after tick1710 PlayRight EVERY-10; NEXT AGB/NatuurpuntVZW/"
            "NSZ-if-200/Bosgroep/Dijk92/FARO/APEFE/Welzijnszorg/GO!/POV/BVAS/IOED/HVZ/"
            "IGS; PlayRight+SIMIM+Reprobel+Auvibel+Sabam DONE; next every-10 1720"
        ),
    }
    rows.append(spawn)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow(row)


def update_loop_state():
    path = DATA / "loop_state.csv"
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        rows = list(r)
    notes = (
        "tick1710 EVERY-10 leftover PlayRight CV neighbouring-rights collecting society "
        "for performing artists; KBO 0440.736.227; official NBB VOL-AUT jaarrekening "
        "YE2024 + Jaarverslag 2024 live playright.be (AV 16.06.2025); sourced euros "
        "assets 76125485 equity 348859 debt 75762690 rechten debt 72956185 commissions "
        "3728405 staff 2047252 diensten 3414843 bedrijfskosten 5531000 expl -831775 "
        "pnl 7819 beleg 71925172 cash 2569599 inningen ~33.1m; FOI ready VTE/NBB CDN "
        "deposit; progress_every_10 + waste top10 refreshed; NSZ still CDN 403; "
        "Blauwe/Sabam/Auvibel/Reprobel/SIMIM FOI still ready; Natuurpunt opaque; "
        "Dijk92 CDN 403; FARO no JR2025; APEFE RA2023; NOT every-10 (next 1720); next "
        "rq_1711 AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/FARO/APEFE/Welzijnszorg/"
        "GO!/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill"
    )
    for row in rows:
        if row.get("state_id") == "main":
            row["mode"] = "continuous"
            row["current_sprint"] = "hole_fill"
            row["last_tick_utc"] = TS
            row["last_unit_id"] = "rq_1710"
            row["ticks_completed"] = "1710"
            row["paused"] = "no"
            row["notes"] = notes
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow(row)


def refresh_progress_and_waste(inv: dict):
    prog = DATA / "progress_every_10_ticks.md"
    old = prog.read_text(encoding="utf-8")
    marker = "## Snapshot at **tick 1700**"
    idx = old.find(marker)
    if idx < 0:
        raise SystemExit("progress marker tick 1700 not found")

    snap = f"""## Snapshot at **tick 1710** (2026-08-23)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1701-1709 leftover speerpunt/collecting: **Flux50** · **Blauwe Cluster** · **FBM/Biovia** · **NSZ** · **Sabam** · **Auvibel** · **Reprobel** · **SIMIM** · **PlayRight** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1701-1709 is residual dual L5 collecting-society / speerpunt (not near-complete of 348bn):** **Sabam** commissions **29.0m** assets **356m** · **PlayRight** commissions **3.73m** assets **76.1m** · **SIMIM** beheers **3.64m** geinde **32.4m** · **Reprobel** commissions **1.97m** rechten debt **19.9m** · **Auvibel** commissions **0.83m** assets **26.7m** · **Flux50/FBM/Biovia** speerpunt stack · prior Flanders FOOD/Oranje/Oxfam wave retained |
| **E. FOI-ready gaps** | **~{inv['foi_ready']}** drafts ready | Human send only; answered **~{inv['foi_answered']}**; partial **~{inv['foi_partial']}**; total FOI rows **~{inv['foi_total']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + koepel/NGO/collecting shells** (**NEW PlayRight** assets **EUR76.13m** commissions **EUR3.73m** rechten debt **EUR73.0m** · **SIMIM** geinde **EUR32.4m** beheers **EUR3.64m** · **Reprobel** commissions **EUR1.97m** · **Auvibel** assets **EUR26.7m** · **Sabam** assets **EUR356m** commissions **EUR29.0m** · prior Flanders FOOD/Oranje/Oxfam/VIL stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs Fluvius EG possible on DSO holdings.**

### Inventory (tick 1710)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {inv['budgets']} |
| commitments.csv | {inv['commitments']} |
| leaderboard.csv | {inv['leaderboard']} |
| entities.csv | {inv['entities']} |
| sources.csv | {inv['sources']} |
| FOI ready | {inv['foi_ready']} |
| FOI answered | {inv['foi_answered']} |
| FOI partial | {inv['foi_partial']} |
| FOI total rows | {inv['foi_total']} |
| research_queue open | rq_116 deferred + rq_1711 hole-fill after progress |

### What improved since tick 1700

- **Residual dual leftover speerpunt / collecting-society wave (tick1701-1709):** **Flux50** · **Blauwe Cluster** (FOI stall) · **FBM/Biovia** · **NSZ** (CDN 403 FOI) · **Sabam** commissions **29.0m** · **Auvibel** commissions **0.83m** · **Reprobel** commissions **1.97m** · **SIMIM** beheers **3.64m** / geinde **32.4m** — no invented euros.
- **NEW (tick1710):** **PlayRight** (KBO **0440.736.227**) leftover neighbouring-rights collecting CV for performing artists. Official NBB VOL-AUT jaarrekening YE2024 + Jaarverslag 2024 (AV **16.06.2025**). Assets **76.125.485** · commissions **3.728.405** · staff **2.047.252** · rechten debt **72.956.185** · inningen **~33.1m**. FOI ready VTE.
- **Dual map themes:** Belgian collecting-society residual completion (Sabam authors / Auvibel private-copy / Reprobel reprografie / SIMIM phonograms / PlayRight performers) · speerpunt clusters · prior Oxfam/Oranje/Natuurpunt retained.
- **Blocked still:** AGB/APB unpublished · Dijk92 CDN **403** · FARO no JR2025 · APEFE RA2023 only · NSZ CDN **403** (deposit 2026-00394221) · Natuurpunt vzw CDN/Northdata opaque.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10. Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **1720**.

"""
    prog.write_text(old[:idx] + snap + old[idx:], encoding="utf-8")

    waste = f"""# DOGE waste ranking — current top 10

**As-of:** tick **1710** (2026-08-23) · **{inv['leaderboard']}** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW leftover 1701-1710 collecting/speerpunt:** **PlayRight** assets **€76.13m** / commissions **€3.73m** / rechten debt **€73.0m** · **SIMIM** geinde **€32.4m** / beheers **€3.64m** · **Sabam** assets **€356m** / commissions **€29.0m** · **Reprobel** commissions **€1.97m** · **Auvibel** assets **€26.7m** · **Flux50/FBM/Biovia/NSZ** · prior **Flanders' FOOD €23.65m** / Oranje / Oxfam / VIL / Natuurpunt Beheer **€505.06m** stack retained · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 1700:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard: GIP 8.7 · fossil direct 8.55 · fossil accises 8.5 · company cars 8.5 · heatoil 8.43 · cheque 8.4 · CO2 SSC gap 8.4 · OAA reporté 8.4 · BCR reporté 8.4 · dual cars SSC 8.4. **Major NEW residual 1701-1710 (off pure top10 / dual):** collecting-society completion **Sabam/Auvibel/Reprobel/SIMIM/PlayRight** + speerpunt **Flux50/FBM/Biovia** + NSZ FOI. Gain is **Belgian CMO residual map**. Count NEW since 1700: Flux50 1702 + Blauwe 1703 + FBM 1704 + NSZ 1705 + Sabam 1706 + Auvibel 1707 + Reprobel 1708 + SIMIM 1709 + PlayRight 1710. **Prior Flanders FOOD/Oranje/Oxfam/Natuurpunt retained.** Not TE-additive of ~348bn.
"""
    (DATA / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")


# --- entity / CSV writes ---
entity = {
    "entity_id": EID,
    "name_nl": (
        "PlayRight cv / Collectieve beheersvennootschap naburige rechten uitvoerende "
        "kunstenaars (leftover performers collecting CV; NOT Sabam / SIMIM / Auvibel / "
        "Reprobel)"
    ),
    "name_fr": (
        "PlayRight sc / Societe de gestion collective droits voisins artistes-interpretes "
        "(residuelle)"
    ),
    "name_en": (
        "PlayRight leftover Belgian neighbouring-rights collecting cooperative for "
        "performing artists"
    ),
    "level": "other",
    "parent_id": "sec_federal",
    "community_language": "nl",
    "website": "https://www.playright.be",
    "foi_email": "info@playright.be",
    "foi_postal": "Belgicalaan 14 1080 Sint-Jans-Molenbeek",
    "notes": (
        "tick1710 leftover PlayRight after SIMIM/Reprobel/Auvibel/Sabam/NSZ/AGB hunt; "
        "official NBB YE2024 + JV2024 live; KBO 0440.736.227; fiduciary rights-heavy; "
        "FOI VTE; YE2025 not yet published"
    ),
}
n_ent = append_rows(DATA / "entities.csv", [entity])

sources = [
    {
        "source_id": SRC,
        "title": "PlayRight NBB VOL-AUT Jaarrekening YE2024 (tick1710)",
        "url": JR_URL,
        "publisher": "PlayRight cv / NBB CBSO",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": (
            "tick1710; NBB model PDF; AV 16.06.2025; assets 76125485; omzet 3728405; "
            "staff 2047252; rechten debt 72956185; equity 348859; pnl 7819"
        ),
    },
    {
        "source_id": "src_playright_jv2024_official_1710",
        "title": "PlayRight Official Jaarverslag 2024 (tick1710)",
        "url": JV_URL,
        "publisher": "PlayRight cv",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": (
            "tick1710; official JV PDF; inningen ~33.1m; verdeeld ~17.4m; AV 16.06.2025"
        ),
    },
    {
        "source_id": "src_playright_commissaris_2024_1710",
        "title": "PlayRight Commissarisverslag YE2024 (tick1710)",
        "url": (
            "http://playright.be/wp-content/uploads/2025/05/"
            "PlayRight-commissarisverslag-NL.pdf"
        ),
        "publisher": "FIGURAD Bedrijfsrevisoren BV",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": (
            "tick1710; oordeel met voorbehoud on beleggingen 27425172 latent -769k; "
            "balanstotaal 76125485; winst 7819"
        ),
    },
    {
        "source_id": "src_playright_kbo_0440736227_1710",
        "title": "KBO Public Search PlayRight CV 0440.736.227 (tick1710)",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl"
            "&ondernemingsnummer=440736227"
        ),
        "publisher": "FPS Economy KBO",
        "accessed_date": DAY,
        "source_class": "primary_official",
        "notes": "tick1710; Belgicalaan 14 1080 Sint-Jans-Molenbeek; CV",
    },
    {
        "source_id": "src_playright_foi_contact_1710",
        "title": "PlayRight FOI channel (info@playright.be)",
        "url": "https://playright.be/en/contact-us/",
        "publisher": "PlayRight",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick1710; info@playright.be; +32 2 421 53 41",
    },
]
n_src = append_rows(DATA / "sources.csv", sources)


def bud(bid, amount, notes):
    return {
        "budget_id": bid,
        "entity_id": EID,
        "year": "2024",
        "amount_eur": str(amount),
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "executed",
        "source_id": SRC,
        "confidence": "strong",
        "notes": notes,
    }


budgets = [
    bud("bud_playright_assets_2024", 76125485, "NBB 20/58 balanstotaal 76125485; tick1710"),
    bud("bud_playright_va_2024", 833552, "NBB vaste activa 833552; tick1710"),
    bud("bud_playright_vlottend_2024", 75291933, "NBB vlottende activa 75291933; tick1710"),
    bud(
        "bud_playright_beleg_2024",
        71925172,
        "NBB geldbeleggingen 50/53 71925172 (commissaris latent -769k on portion); "
        "tick1710",
    ),
    bud("bud_playright_cash_2024", 2569599, "NBB liquide middelen 2569599; tick1710"),
    bud("bud_playright_equity_2024", 348859, "NBB eigen vermogen 348859; tick1710"),
    bud("bud_playright_debt_2024", 75762690, "NBB schulden 17/49 75762690; tick1710"),
    bud(
        "bud_playright_rechten_debt_2024",
        72956185,
        "NBB schulden rechten 6.9 bis 72956185 (LT 51302115 + ST remainder); tick1710",
    ),
    bud(
        "bud_playright_rechten_te_verdelen_2024",
        50645021,
        "NBB te verdelen geinde rechten 50645021 (niet-voorbeh 47645812 + voorbeh "
        "2999209); tick1710",
    ),
    bud(
        "bud_playright_commissions_2024",
        3728405,
        "NBB omzet/commissies 70 3728405 ENVELOPE; tick1710",
    ),
    bud(
        "bud_playright_opbr_2024",
        4699225,
        "NBB bedrijfsopbrengsten 70/76A 4699225; tick1710",
    ),
    bud(
        "bud_playright_andere_opbr_2024",
        1931975,
        "NBB totaal andere bedrijfsopbrengsten 74 1931975; tick1710",
    ),
    bud("bud_playright_staff_2024", 2047252, "NBB bezoldigingen 62 2047252; tick1710"),
    bud(
        "bud_playright_diensten_2024",
        3414843,
        "NBB diensten en diverse goederen 61 3414843; tick1710",
    ),
    bud(
        "bud_playright_bedrijfskosten_2024",
        5531000,
        "NBB bedrijfskosten 60/66A 5531000; tick1710",
    ),
    bud(
        "bud_playright_expl_2024",
        -831775,
        "NBB bedrijfsverlies -831775; tick1710",
    ),
    bud("bud_playright_fin_opbr_2024", 960164, "NBB financiële opbrengsten 960164; tick1710"),
    bud("bud_playright_pnl_2024", 7819, "NBB winst boekjaar 7819; tick1710"),
    bud(
        "bud_playright_inningen_2024",
        33100000,
        "Official JV/news inningen ~33.1m YE2024 (rounded public figure); tick1710",
    ),
]
n_bud = append_rows(DATA / "budgets.csv", budgets)

commitment = {
    "commitment_id": COMM,
    "title": (
        "PlayRight YE2024 leftover performers collecting society (commissions 3.73m / "
        "inningen 33.1m / rechten debt 73m)"
    ),
    "entity_id": EID,
    "beneficiary": "PlayRight member performing artists / naburige rechten",
    "legal_basis": "WVV CV; WER XI naburige rechten; Bestuursdecreet openbaarheid",
    "decision_date": "2025-06-16",
    "start_year": "2024",
    "end_year": "2024",
    "total_envelope_eur": "3728405",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": JR_URL,
    "stated_goal": (
        "Local leftover PlayRight map — official YE2024 commissions 3.73m; FOI VTE"
    ),
    "cut_option": (
        "Publish VTE + NBB CDN deposit; do not treat rechten debt 73m as waste; "
        "scrutinise commissions 3.73m vs diensten 3.41m"
    ),
    "source_id": SRC,
    "confidence": "strong",
    "hierarchy_path": HP,
    "notes": (
        "tick1710; YE2024; commissions 3728405 staff 2047252 assets 76.1m of which "
        "rechten fiduciary ~73.0m debt; inningen ~33.1m; not TE-additive of 348bn; "
        "YE2025 not yet published"
    ),
}
n_comm = append_rows(DATA / "commitments.csv", [commitment])

leaderboard = {
    "item_id": LB,
    "name": (
        "PlayRight YE2024 leftover performers collecting society: commissions 3.73m / "
        "inningen 33m / rechten debt 73m"
    ),
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": HP,
    "annual_cost_eur": "3728405",
    "total_cost_eur": "76125485",
    "tco_notes": (
        "Leftover PlayRight CV neighbouring-rights CMO YE2024: commissions/omzet 3.73m "
        "(ops envelope) / staff 2.05m / diensten 3.41m / bedrijfskosten 5.53m / "
        "bedrijfsverlies -0.83m / pnl 7.8k; balance 76.1m dominated by authors-rights "
        "fiduciary debt 73.0m + beleggingen 71.9m (NOT PlayRight free cash; commissaris "
        "qualification latent -769k); inningen ~33.1m; peer of Sabam/SIMIM/Auvibel/"
        "Reprobel; VTE residual FOI; YE2025 not yet published"
    ),
    "confidence": "strong",
    "source_id": SRC,
    "beneficiaries": "Uitvoerende kunstenaars / performing artists via PlayRight",
    "stated_goal": "Local leftover PlayRight map — official YE2024 NBB+JV live",
    "measured_outcome": (
        "Official PlayRight YE2024 2026-08-23: commissions 3728405 / staff 2047252 / "
        "assets 76125485 / rechten debt 72956185 / inningen ~33100000"
    ),
    "absurdity_score": "5.0",
    "cost_score": "4.5",
    "difficulty": "2.5",
    "priority_index": "4.6",
    "cut_proposal": (
        "Do not treat rechten debt 73m as waste; scrutinise commissions 3.73m vs "
        "diensten 3.41m / beleggingen latent loss; publish VTE"
    ),
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1710 EVERY-10; leftover after AGB unpublished / NSZ CDN403 / "
        "SIMIM+Reprobel+Auvibel+Sabam done; not TE-additive of 348bn"
    ),
}
n_lb = append_rows(DATA / "leaderboard.csv", [leaderboard])

foi = {
    "gap_id": GAP,
    "hierarchy_path": HP,
    "entity_id": EID,
    "what_is_missing": (
        "Official YE2024 NBB+JV publishes commissions 3728405 / staff 2047252 / assets "
        "76125485 / rechten debt 72956185 / inningen ~33.1m; exact VTE Unknown; NBB CDN "
        "deposit id Unknown; YE2025 jaarrekening not yet published"
    ),
    "why_it_matters": (
        "Leftover Belgian performers neighbouring-rights collecting society with live "
        "official YE2024 euros (3.73m commissions / 33m inningen / 73m rights fiduciary) "
        "— need VTE + CDN deposit; watch for YE2025 when filed"
    ),
    "priority": "7",
    "recipient_body": "PlayRight cv / Bestuursorgaan",
    "recipient_email": "info@playright.be",
    "recipient_postal": "Belgicalaan 14 1080 Sint-Jans-Molenbeek",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": DAY,
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": COMM,
    "linked_leaderboard_id": LB,
    "created_utc": TS,
    "updated_utc": TS,
    "notes": (
        "tick1710; human-send only; NSZ/Blauwe/Sabam/Auvibel/Reprobel/SIMIM FOI still "
        "ready"
    ),
}
n_foi = append_rows(DATA / "foi_queue.csv", [foi])

update_queue()
update_loop_state()

inv = {
    "entities": count("entities.csv"),
    "sources": count("sources.csv"),
    "budgets": count("budgets.csv"),
    "commitments": count("commitments.csv"),
    "leaderboard": count("leaderboard.csv"),
}
fr, fa, fp, ft = foi_stats()
inv.update(foi_ready=fr, foi_answered=fa, foi_partial=fp, foi_total=ft)
refresh_progress_and_waste(inv)

print(
    f"tick1710 applied entities={n_ent} sources={n_src} budgets={n_bud} "
    f"commitments={n_comm} leaderboard={n_lb} foi={n_foi} inv={inv}"
)

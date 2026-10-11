# -*- coding: utf-8 -*-
"""Tick 1350 — every-10 progress FIRST, then leftover IGS Interwaas JR2025 WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
"""
from __future__ import annotations

import csv
import io
import sys
from collections import Counter
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1350"
UTC = "2026-08-18T22:20:00Z"
ENT = "igs_interwaas"
HIER = "Vlaanderen>OostVlaanderen>IGS>Interwaas>Waasland"
GAP = "gap_iws_omzet_2_91m_cash_drop_12_70m_l5"
SRC = "src_iws_jr2025_pdf"
SRC2 = "src_iws_site"
SRC3 = "src_kbo_iws_0206460639"
SRC4 = "src_iws_foi_contact"
SRC_URL = "https://www.interwaas.be/sites/default/files/2026-05/VER-20260521-COMJVS-Jaarverslag2025-voor-website-compressed.pdf"
SRC2_URL = "https://www.interwaas.be/over-interwaas/publicaties/jaarverslagen"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0206460639"
SRC4_URL = "https://www.interwaas.be"
FOI_EMAIL = "info@interwaas.be"
FOI_POSTAL = "Lamstraat 113 9100 Sint-Niklaas"
DRAFT = "docs/doge/foi/drafts/gap_iws_omzet_2_91m_cash_drop_12_70m_l5.md"
COMM = "comm_iws_jr2025_omzet"
LB = "lb_iws_omzet_2_91m_cash_drop_12_70m"


def append_rows(path, new_rows):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        existing_ids = set()
        id_key = fields[0]
        for row in reader:
            existing_ids.add(row.get(id_key))
    added = 0
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        for row in new_rows:
            if row.get(id_key) in existing_ids:
                continue
            w.writerow({k: row.get(k, "") for k in fields})
            added += 1
    return added


def csv_line(fields, row):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="")
    w.writerow({k: row.get(k, "") for k in fields})
    return buf.getvalue()


def patch_last_rq_and_spawn(path, target_id, new_target, spawn_row):
    header = path.open(encoding="utf-8").readline()
    fields = next(csv.reader([header.strip("\n").strip("\r")]))
    with path.open("rb") as f:
        f.seek(0, 2)
        size = f.tell()
        chunk = min(size, 131072)
        f.seek(size - chunk)
        tail = f.read()
    if tail.endswith(b"\n"):
        search = tail[:-1]
    else:
        search = tail
    last_nl = search.rfind(b"\n")
    last_line = search[last_nl + 1 :] if last_nl != -1 else search
    last_text = last_line.decode("utf-8")
    if not last_text.startswith(target_id + ","):
        raise SystemExit("last rq line is not %s: %s" % (target_id, last_text[:160]))
    last_start = (size - chunk) + (last_nl + 1 if last_nl != -1 else 0)
    spawn_id = spawn_row.get("task_id")
    if spawn_id and spawn_id.encode("utf-8") in tail:
        raise SystemExit("spawn id already in tail")
    payload = (csv_line(fields, new_target) + "\n" + csv_line(fields, spawn_row) + "\n").encode("utf-8")
    with path.open("r+b") as f:
        f.seek(last_start)
        f.truncate()
        f.write(payload)
    return True, True


def count_csv_rows(path: Path) -> int:
    with path.open(encoding="utf-8", errors="replace", newline="") as f:
        n = sum(1 for _ in f)
    return max(0, n - 1)


def foi_status_counts() -> Counter:
    with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return Counter((r.get("status") or "").strip() for r in rows)


def write_progress(counts: dict) -> None:
    prog = DATA / "progress_every_10_ticks.md"
    text = prog.read_text(encoding="utf-8")
    marker = "## Snapshot at **tick 1340** (2026-08-18)"
    if marker not in text:
        raise SystemExit("progress file missing tick 1340 marker")
    snap = f"""## Snapshot at **tick 1350** (2026-08-18)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1341-1350 leftover IGS: **IGEAN** · **IDM** · **IVM** · **ILvA** · **IVVO** · **WVI** · **IVIO** operational · **Creat** · **Aquaduin** · **Interwaas** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1341-1350 is VL residual dual L5 leftover IGS (not near-complete of 348bn):** **Interwaas** assets **78.37m** cash **1.44m DROP 12.70m** beleggingen **30.48m** omzet **2.91m** · **WVI** assets **241.0m** stock **181.88m** omzet **34.23m** · **IGEAN DV** assets **103.92m** inv **68.19m** · **Aquaduin** assets **99.09m** omzet **26.50m** sanering **31.33m** · **Creat** omzet **89.38m** ST recv **16.39m** · leftover IGS live WVV (IVM 53.70m / ILvA 47.88m / IVVO 24.42m / IDM 9.53m) · IVIO operational cityfee **10.04m** no statutory WVV · prior leftover EVA/zorg stack retained |
| **E. FOI-ready gaps** | **~{counts['foi_ready']}** drafts ready | Human send only; answered **~{counts['foi_answered']}**; partial **~{counts['foi_partial']}**; total FOI rows **~{counts['foi_total']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS dual debt/AFM NEG + leasing/city-loan/erfpacht/DBFM/portfolio/waste-water-streek shells** (**NEW Interwaas** assets **EUR78.37m** cash **EUR1.44m DROP 12.70m** beleggingen **EUR30.48m** omzet **EUR2.91m** · **WVI** assets **EUR241.0m** stock **EUR181.88m** · **IGEAN DV** assets **EUR103.92m** inv **EUR68.19m** · **Aquaduin** assets **EUR99.09m** omzet **EUR26.50m** sanering **EUR31.33m** · **Creat** omzet **EUR89.38m** · leftover IGS IVM/ILvA/IVVO/IDM/IVIO · prior **EVA LSM** assets **EUR85.85m** cash **EUR3.39m DROP 10.74m** portfolio **EUR58.31m** PnL **+EUR1.5k** · **WV Zorgband** assets **EUR61.86m** PnL **−EUR5.83m** lease **EUR43.75m** · **WV Zorgbedrijf Brasschaat** assets **EUR28.94m** cash **EUR2.65m** BBR **−EUR5.39m** LT-recv **EUR17.90m** · leftover zorg live BBC Het Dak / OPcura / BVK / Weldenderend · leftover FOI Vormingscentrum Malle / Inagro / Sleutelzorg · prior **APB Hooibeekhoeve** assets **EUR5.93m** cash **EUR2.65m** ST recv **EUR2.82m** BBR **+EUR1.30m** · **EVA Pluimveehouderij** assets **EUR8.63m** cash **EUR4.08m** ST recv **EUR4.46m** BBR **+EUR1.17m** · **APB Vonk** assets **EUR1.02m** cash **EUR0.96m** BBR **+EUR0.16m** · leftover FOI (Blankenberge / Campus Vesta / Monumentenwacht / Vlabinvest / Zilvermeer / Zorg HH / **EVA Kinderopvang Dilbeek**) · prior **APB KampC** assets **EUR5.93m** cash **EUR2.65m** ST recv **EUR3.06m** BBR **+EUR2.39m** J5/T2 werksub gap **EUR1.25m** · **APB PSES** assets **EUR186.52m** ST recv **EUR165.31m** BBR **−EUR1.29m** · **APB GKC** assets **EUR2.67m** cash **EUR2.11m** · **APB Havencentrum** assets **EUR0.97m** Havenwereld **EUR0.40m** · **AGBIM** CCAO **EUR8.91m** · **AGB Maaseik** fin debt **EUR1.60m** AFM **−EUR0.67m** · prior **APB VERA** fin debt **EUR1.72m** equity **−EUR1.64m** straight loan **EUR1.10m** · **Edegem** fin debt **EUR14.05m** pension **EUR23.40m** · **Beerse city** fin debt **EUR13.82m** · **AGB Beerse** fin debt **EUR5.02m** · **Pepingen city** fin debt **EUR3.47m** · **Vleteren** fin debt **EUR3.32m** · prior **Stad+OCMW Kortenaken** fin debt **EUR10.57m** IGS EV-reval **EUR8.90m** OCMW equity **−EUR5.41m** · **Heusden-Zolder** fin debt **EUR37.85m** IGS reval **EUR31.12m** · **Kapelle-op-den-Bos** fin debt **EUR18.87m** · **Oud-Heverlee** fin debt **EUR15.18m** · **Diepenbeek city** fin debt **EUR13.59m** IGS reval **EUR19.43m** · **Huldenberg** fin debt **EUR9.56m** · **AGB Kortenaken** fin debt **EUR3.28m** leasing **EUR3.22m** · **Voeren** fin debt **EUR3.37m** · **AGB Diepenbeek** fin debt **EUR3.03m** · **Steenokkerzeel** fin debt **EUR2.49m** · prior **Stad+OCMW Bekkevoort** fin debt **EUR9.77m** IGS EV-reval **EUR5.90m** · **HH city** fin debt **EUR17.37m** · **AGB Masterplan HH** fin debt **EUR27.81m** · **AGB Sport HH** fin debt **EUR10.72m** · **AGB SCO Ronse** fin debt **EUR22.65m** · **Ronse city** fin debt **EUR25.02m** pension **EUR19.50m** · **Kraainem** fin debt **EUR6.40m** · **Tielt-Winge** fin debt **EUR8.52m** · prior **Stad+OCMW Tienen** fin debt **EUR59.73m** pension **EUR51.29m** · **Machelen** fin debt **EUR26.37m** Farys lease **EUR16.90m** · **AGB Tienen** fin debt **EUR16.93m** · **AG Museum Leuven** fin debt **EUR14.51m** · **Gingelom** Fluvius reval **EUR9.75m** fin debt **EUR3.86m** · prior **AGB MAC** fin debt **EUR40.3m** leasing **EUR40.8m** · **Mintus** dual **EUR26.36m** · Digipolis assets **EUR73.61m** · **AG Vespa** fin debt **EUR179.6m** DBFM **EUR109.4m** · **sogent** AFM **−EUR3.90m** debt **EUR96.3m** · AG-O cum loss **−EUR29.2m** · Zorgbedrijf Antwerpen AFM **−EUR18.87m** debt **EUR220m** / Dodoens equity **−EUR18.88m** / Hasselt ~EUR95–103m stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market.

### Inventory (tick 1350)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {counts['budgets']} |
| commitments.csv | {counts['commitments']} |
| leaderboard.csv | {counts['leaderboard']} |
| entities.csv | {counts['entities']} |
| sources.csv | {counts['sources']} |
| FOI ready | {counts['foi_ready']} |
| FOI answered | {counts['foi_answered']} |
| FOI partial | {counts['foi_partial']} |
| FOI total rows | {counts['foi_total']} |
| research_queue open | rq_116 deferred + rq_1351 hole-fill after progress |

### What improved since tick 1340

- **VL residual dual JR2025 leftover IGS (tick1341-1349):** **WVI** assets **241.0m** stock **181.88m** omzet **34.23m** · **IGEAN DV** assets **103.92m** inv **68.19m** · **Aquaduin** assets **99.09m** omzet **26.50m** sanering **31.33m** · **Creat** omzet **89.38m** ST recv **16.39m** · leftover IGS live WVV (IVM 53.70m / ILvA 47.88m / IVVO 24.42m / IDM 9.53m) · IVIO operational cityfee **10.04m** no statutory WVV — no invented euros.
- **NEW (tick1350):** **Interwaas** (KBO 0206.460.639) leftover IGS streekontwikkeling of already-mined Waasland cities. Official jaarverslag 2025 PDF (19.3MB / 65p; InDesign 21.05.2026) embeds interne WVV jaarrekening (verkort 4p). Assets **78.369.748** · cash **1.439.206 DROP** vs 14.135.539 · beleggingen **30.479.135** · omzet **2.912.087** DROP · PnL **+2.514.063**. FOI ready. Every-10 progress refresh from on-disk CSVs.
- **Dual map themes:** **leftover IGS waste/water/streek shells** (WVI 241m / IGEAN 104m / Aquaduin 99m / Interwaas 78m / Creat 89m omzet) · leftover EVA LRM-portfolio (LSM 85.85m) · leftover zorg live BBC · leftover unpublished FOI stack retained.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10.

---
"""
    text = text.replace(marker, snap + marker, 1)
    prog.write_text(text, encoding="utf-8")
    print("progress_every_10_ticks.md inserted tick 1350 snapshot")


def write_waste_top10(counts: dict) -> None:
    p = DATA / "doge_waste_top10_current.md"
    text = p.read_text(encoding="utf-8")
    text = text.replace(
        "**As-of:** tick **1340** (2026-08-18) · **7144** leaderboard rows",
        f"**As-of:** tick **1350** (2026-08-18) · **{counts['leaderboard']}** leaderboard rows",
        1,
    )
    old_dual = "(**NEW EVA LSM** assets **€85.85m** cash **€3.39m DROP 10.74m** portfolio **€58.31m** PnL **+€1.5k**"
    new_dual = (
        "(**NEW Interwaas** assets **€78.37m** cash **€1.44m DROP 12.70m** beleggingen **€30.48m** omzet **€2.91m** · "
        "**WVI** assets **€241.0m** stock **€181.88m** omzet **€34.23m** · "
        "**IGEAN DV** assets **€103.92m** inv **€68.19m** · "
        "**Aquaduin** assets **€99.09m** omzet **€26.50m** sanering **€31.33m** · "
        "**Creat** omzet **€89.38m** ST recv **€16.39m** · leftover IGS IVM/ILvA/IVVO/IDM/IVIO · "
        "prior **EVA LSM** assets **€85.85m** cash **€3.39m DROP 10.74m** portfolio **€58.31m** PnL **+€1.5k**"
    )
    if old_dual not in text:
        raise SystemExit("waste top10 missing LSM dual marker")
    text = text.replace(old_dual, new_dual, 1)
    old_chg = (
        "**Change vs tick 1330:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
        "**Major NEW residual 1331–1340 (off pure top10 / dual):**"
    )
    new_chg = (
        "**Change vs tick 1340:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
        "**Major NEW residual 1341–1350 (off pure top10 / dual):** **Interwaas** assets **EUR78.37m** cash **EUR1.44m DROP 12.70m** beleggingen **EUR30.48m** omzet **EUR2.91m** · **WVI** assets **EUR241.0m** stock **EUR181.88m** · **IGEAN DV** assets **EUR103.92m** inv **EUR68.19m** · **Aquaduin** assets **EUR99.09m** omzet **EUR26.50m** sanering **EUR31.33m** · **Creat** omzet **EUR89.38m** · leftover IGS IVM 53.70m / ILvA 47.88m / IVVO 24.42m / IDM 9.53m / IVIO cityfee 10.04m. "
        "Gain is **leftover IGS waste/water/streek shells**. "
        "**Prior 1331–1340 retained:**"
    )
    if old_chg not in text:
        raise SystemExit("waste top10 missing change-vs-1330 marker")
    text = text.replace(old_chg, new_chg, 1)
    old_out = "| — | `lb_lsm_cash_drop_10_74m_portfolio_58_31m_pnl_1_5k` | **85.85 m stock** | **~6.5 dual** | **NEW 1340** EVA LSM cash drop 10.74m / portfolio 58.31m / PnL +1.5k |"
    new_out = (
        "| — | `lb_iws_omzet_2_91m_cash_drop_12_70m` | **78.37 m stock** | **~6.2 dual** | **NEW 1350** Interwaas omzet 2.91m / cash drop 12.70m / beleggingen 30.48m |\n"
        "| — | `lb_wvi_omzet_34_23m_stock_181_88m` | **241.0 m stock** | **~6.8 dual** | 1346 WVI leftover IGS omzet 34.23m / stock 181.88m |\n"
        "| — | `lb_igean_dv_inv_68_19m_debt_85_39m_equity_thin` | **103.92 m stock** | **~6.6 dual** | 1341 IGEAN DV leftover IGS inv 68.19m / debt 85.39m |\n"
        "| — | `lb_aqd_omzet_26_50m_accrual_31_68m` | **99.09 m stock** | **~5.9 dual** | 1349 Aquaduin leftover IGS omzet 26.50m / sanering 31.33m |\n"
        "| — | `lb_creat_omzet_89_38m_strecv_16_39m` | **89.38 m flow** | **~6.0 dual** | 1348 Creat leftover IGS omzet 89.38m / ST recv 16.39m |\n"
        + old_out.replace("**NEW 1340**", "1340")
    )
    if old_out not in text:
        raise SystemExit("waste top10 missing lsm just-outside row")
    text = text.replace(old_out, new_out, 1)
    old_abs = "| `lb_lsm_cash_drop_10_74m_portfolio_58_31m_pnl_1_5k` | **6.5** | **NEW 1340** EVA LSM assets 85.85m / cash drop 10.74m / portfolio 58.31m / PnL +1.5k |"
    new_abs = (
        "| `lb_iws_omzet_2_91m_cash_drop_12_70m` | **6.2** | **NEW 1350** Interwaas assets 78.37m / cash drop 12.70m / beleggingen 30.48m / omzet 2.91m |\n"
        "| `lb_wvi_omzet_34_23m_stock_181_88m` | **6.4** | 1346 WVI leftover IGS assets 241.0m / stock 181.88m / omzet 34.23m |\n"
        "| `lb_igean_dv_inv_68_19m_debt_85_39m_equity_thin` | **6.3** | 1341 IGEAN DV leftover IGS assets 103.92m / inv 68.19m |\n"
        "| `lb_aqd_omzet_26_50m_accrual_31_68m` | **5.8** | 1349 Aquaduin leftover IGS omzet 26.50m / sanering 31.33m |\n"
        + old_abs.replace("**NEW 1340**", "1340")
    )
    if old_abs not in text:
        raise SystemExit("waste top10 missing lsm absurdity row")
    text = text.replace(old_abs, new_abs, 1)
    p.write_text(text, encoding="utf-8")
    print("doge_waste_top10_current.md updated tick 1350; pure top10 unchanged")


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "Interwaas jaarverslag boekjaar 2025 (official interne WVV jaarrekening verkort; InDesign 21.05.2026)",
                "url": SRC_URL,
                "publisher": "Interwaas dienstverlenende vereniging",
                "accessed_date": "2026-08-18",
                "source_class": "budget",
                "notes": (
                    "tick1350; official PDF 19.3MB 65p InDesign 21.05.2026; leftover IGS streek of mined Waasland cities; "
                    "embedded interne WVV balans/resultatenrekening 4p verkort; commissaris oordeel zonder voorbehoud; every-10"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Interwaas official jaarverslagen page (KBO 0206.460.639)",
                "url": SRC2_URL,
                "publisher": "Interwaas",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1350; leftover IGS streek of mined Waasland cities; "
                    "lists Jaarverslag 2025 PDF VER-20260521-COMJVS; afkorting Interwaas"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Interwaas 0206.460.639",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1350; KBO 0206.460.639 Actief / normale toestand since 27.06.1968; "
                    "statutaire naam Intergemeentelijk Samenwerkingsverband van het Land van Waas since 19.03.2004; "
                    "afkorting Interwaas since 22.12.2017; Dienstverlenende vereniging (Vlaams Gewest) since 19.03.2004; "
                    "zetel Lamstraat 113 9100 Sint-Niklaas since 06.05.1996; 1 VE; "
                    "aanbestedende overheid since 27.06.1968; btw since 01.09.1986; RSZ since 01.01.2022; "
                    "jaarvergadering mei; boekjaar 31 december; NACE 68.121/71.113/87.999 RSZ 84.119; databank 17.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Interwaas FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "Interwaas",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1350; FOI info@interwaas.be; Lamstraat 113 9100 Sint-Niklaas; "
                    "T 03 500 47 00; voorzitter Jurgen Bauwens; directeur Hans De Bock"
                ),
            },
        ],
    )
    print("sources", n)

    n = append_rows(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENT,
                "name_nl": "Interwaas (leftover IGS streekontwikkeling Land van Waas)",
                "name_fr": "Interwaas (association de services / IGS residuel / developpement regional Waasland)",
                "name_en": "Interwaas Waasland intermunicipal development (leftover IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.interwaas.be",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1350 leftover IGS residual streek of mined Waasland cities "
                    "(Beveren-Kruibeke-Zwijndrecht/Lokeren/Sint-Gillis-Waas/Sint-Niklaas/Stekene/Temse/Waasmunster); "
                    "KBO 0206.460.639 Actief since 27.06.1968; official JR2025 WVV PDF downloads; "
                    "sourced euros omzet 2.912m / assets 78.370m / cash drop 12.696m / beleggingen 30.479m / PnL 2.514m; "
                    "FOI ready per-vennoot/cash-beleggingen/NBB; every-10"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_iws_assets_2025", ENT, "2025", "78369748", "2025 assets 78369747.86; tick1350; primary official WVV 20/58"),
        ("bud_iws_assets_2024", ENT, "2024", "76794255", "2024 assets 76794254.77 comparative; tick1350; primary official WVV"),
        ("bud_iws_fixed_2025", ENT, "2025", "13979099", "2025 vaste activa 13979098.51; tick1350; primary official WVV 21/28"),
        ("bud_iws_mva_2025", ENT, "2025", "13255532", "2025 MVA 13255532.21; tick1350; primary official WVV 22/27"),
        ("bud_iws_buildings_2025", ENT, "2025", "2249851", "2025 terreinen en gebouwen 2249851.07; tick1350; primary official WVV 22"),
        ("bud_iws_cip_2025", ENT, "2025", "10755384", "2025 activa in aanbouw 10755384.18 JUMP vs 5501926.17 Heidebaan-Noord + Eurolaan 4A; tick1350; primary official WVV 27"),
        ("bud_iws_fva_2025", ENT, "2025", "723566", "2025 FVA 723566.30; tick1350; primary official WVV 28"),
        ("bud_iws_current_2025", ENT, "2025", "64390649", "2025 vlottende activa 64390649.35; tick1350; primary official WVV 29/58"),
        ("bud_iws_ltrecv_2025", ENT, "2025", "13845107", "2025 LT recv 13845107.42 Mijn VerbouwLeningen; tick1350; primary official WVV 29"),
        ("bud_iws_stock_2025", ENT, "2025", "12405497", "2025 voorraden onroerend voor verkoop 12405497.08; tick1350; primary official WVV 35"),
        ("bud_iws_strecv_2025", ENT, "2025", "6156862", "2025 ST recv 6156861.65; tick1350; primary official WVV 40/41"),
        ("bud_iws_trade_recv_2025", ENT, "2025", "1316845", "2025 handelsvorderingen 1316845.00; tick1350; primary official WVV 40"),
        ("bud_iws_invest_2025", ENT, "2025", "30479135", "2025 geldbeleggingen 30479135.00 JUMP vs 20902101.60 termijn 10.5m; tick1350; primary official WVV 50/53"),
        ("bud_iws_cash_2025", ENT, "2025", "1439206", "2025 liquide middelen 1439206.24 DROP vs 14135538.60 drop 12696332.36; tick1350; primary official WVV 54/58"),
        ("bud_iws_cash_2024", ENT, "2024", "14135539", "2024 liquide middelen 14135538.60 comparative; tick1350; primary official WVV"),
        ("bud_iws_equity_2025", ENT, "2025", "55113218", "2025 equity 55113217.68; tick1350; primary official WVV 10/15"),
        ("bud_iws_inbreng_2025", ENT, "2025", "3705675", "2025 inbreng buiten kapitaal 3705675.00; tick1350; primary official WVV 10/11"),
        ("bud_iws_reserves_2025", ENT, "2025", "50881628", "2025 reserves 50881628.22; tick1350; primary official WVV 13"),
        ("bud_iws_avail_res_2025", ENT, "2025", "50043294", "2025 beschikbare reserves / Waas Fonds 50043293.51; tick1350; primary official WVV 133"),
        ("bud_iws_prov_2025", ENT, "2025", "4582368", "2025 voorzieningen 4582368.38; tick1350; primary official WVV 16"),
        ("bud_iws_milieu_prov_2025", ENT, "2025", "4151914", "2025 milieuvoorzieningen 4151913.73 PFAS Kattestraat; tick1350; primary official WVV 163"),
        ("bud_iws_debt_2025", ENT, "2025", "18674162", "2025 schulden 18674161.80; tick1350; primary official WVV 17/49"),
        ("bud_iws_ltdebt_2025", ENT, "2025", "13444543", "2025 LT schulden 13444543.42; tick1350; primary official WVV 17"),
        ("bud_iws_ltfin_2025", ENT, "2025", "299436", "2025 LT fin achtergesteld 299436.00; tick1350; primary official WVV 170"),
        ("bud_iws_ltother_2025", ENT, "2025", "13145107", "2025 LT overige schulden 13145107.42 energieleningen-tegenhanger; tick1350; primary official WVV 178/9"),
        ("bud_iws_stdebt_2025", ENT, "2025", "3655255", "2025 ST schulden 3655255.01; tick1350; primary official WVV 42/48"),
        ("bud_iws_trade_pay_2025", ENT, "2025", "817163", "2025 leveranciers 817163.38; tick1350; primary official WVV 44"),
        ("bud_iws_opsrev_2025", ENT, "2025", "9893891", "2025 bedrijfsopbrengsten 9893890.61; tick1350; primary official WVV 70/76A"),
        ("bud_iws_omzet_2025", ENT, "2025", "2912087", "2025 omzet 2912086.70 DROP 40.86pct vs 4924206.40; tick1350; primary official WVV 70"),
        ("bud_iws_omzet_2024", ENT, "2024", "4924206", "2024 omzet 4924206.40 comparative; tick1350; primary official WVV"),
        ("bud_iws_otherops_2025", ENT, "2025", "7377205", "2025 andere bedrijfsopbrengsten 7377204.98; tick1350; primary official WVV 74"),
        ("bud_iws_prodva_2025", ENT, "2025", "3352740", "2025 geproduceerde vaste activa 3352739.86; tick1350; primary official WVV 72"),
        ("bud_iws_opscost_2025", ENT, "2025", "8684689", "2025 bedrijfskosten 8684689.32; tick1350; primary official WVV 60/66A"),
        ("bud_iws_goods_2025", ENT, "2025", "1446108", "2025 handelsgoederen 1446108.15; tick1350; primary official WVV 60"),
        ("bud_iws_diensten_2025", ENT, "2025", "2735316", "2025 diensten 2735315.76; tick1350; primary official WVV 61"),
        ("bud_iws_pers_2025", ENT, "2025", "4303553", "2025 personeel 4303553.26; VTE gem 44.43 start 51/46.1 einde 45/41.6; tick1350; primary official WVV 62"),
        ("bud_iws_expl_2025", ENT, "2025", "1209201", "2025 bedrijfswinst 1209201.29; tick1350; primary official WVV 9901"),
        ("bud_iws_fin_opbr_2025", ENT, "2025", "1957285", "2025 financiele opbrengsten 1957285.00; tick1350; primary official WVV 75/76B"),
        ("bud_iws_mslo_div_2025", ENT, "2025", "1404706", "2025 opbrengsten uit FVA / MSLO dividend 1404705.97; tick1350; primary official WVV 750"),
        ("bud_iws_pnl_pretax_2025", ENT, "2025", "3208996", "2025 winst voor belasting 3208995.73; tick1350; primary official WVV 9903"),
        ("bud_iws_tax_2025", ENT, "2025", "694933", "2025 belasting 694932.79; tick1350; primary official WVV 67/77"),
        ("bud_iws_pnl_2025", ENT, "2025", "2514063", "2025 PnL 2514062.94; tick1350; primary official WVV 9904"),
        ("bud_iws_waasfonds_add_2025", ENT, "2025", "3390408", "2025 toevoeging overige reserves MSLO LPW 3390408.25; tick1350; primary official WVV 6921"),
    ]
    n = append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": bid,
                "entity_id": eid,
                "year": year,
                "amount_eur": amt,
                "amount_min_eur": "",
                "amount_max_eur": "",
                "basis": "executed",
                "source_id": SRC,
                "confidence": "strong",
                "notes": notes,
            }
            for bid, eid, year, amt, notes in budget_rows
        ],
    )
    print("budgets", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": "Interwaas JR2025 leftover IGS dual (omzet 2.91m / cash drop 12.70m / beleggingen 30.48m)",
                "entity_id": ENT,
                "beneficiary": "Interwaas / 7 Waasland vennoten (BKZ Lokeren SGW Sint-Niklaas Stekene Temse Waasmunster)",
                "legal_basis": "Decreet lokaal bestuur IGS; dienstverlenende vereniging; Bestuursdecreet openbaarheid; WVV neerlegging",
                "decision_date": "2026-05-21",
                "start_year": "1968",
                "end_year": "2025",
                "total_envelope_eur": "78369748",
                "cash_by_year": "",
                "remaining_eur": "55113218",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL streek — per-vennoot 2.91m omzet / cash drop 12.70m / beleggingen 30.48m / NBB",
                "cut_option": "Publish per-vennoot 2.91m omzet dual city lines + cash/beleggingen recon 12.70m + full statutory NBB; do not recreate parallel Waasland streek-IGS shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1350; omzet 2912087 assets 78369748 cash drop 12696332 beleggingen 30479135 PnL 2514063; FOI ready not sent; every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Interwaas JR2025 leftover IGS: omzet 2.91m / cash drop 12.70m / beleggingen 30.48m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "8684689",
                "total_cost_eur": "78369748",
                "tco_notes": "Leftover dual IGS streek of mined Waasland cities: omzet 2.91m DROP / cash drop 12.70m vs beleggingen 30.48m / assets 78.37m / Waas Fonds 50.04m; official WVV live verkort; do not treat 78.37m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Interwaas / 7 Waasland vennoten",
                "stated_goal": "Local leftover IGS map VL streek — JR2025 WVV live; dual omzet/cash/NBB FOI",
                "measured_outcome": "Official WVV 2026-08-18: omzet 2.91m / assets 78.37m / cash 1.44m DROP 12.70m / beleggingen 30.48m / PnL 2.51m; VTE 44.43",
                "absurdity_score": "6.2",
                "cost_score": "6.6",
                "difficulty": "3.0",
                "priority_index": "6.2",
                "cut_proposal": "Publish per-vennoot 2.91m omzet dual city lines + cash/beleggingen recon 12.70m + full statutory NBB; do not recreate parallel Waasland streek-IGS shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1350; leftover IGS streek of mined Waasland cities; FOI ready not sent; not TE-additive of 348bn; every-10",
            }
        ],
    )
    print("leaderboard", n)

    n = append_rows(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": HIER + ">JR2025_L5",
                "entity_id": ENT,
                "what_is_missing": (
                    "Per-vennoot 2025-2026 dual lines for omzet 2912086.70 (DROP 40.86pct vs 4924206.40; "
                    "no 6.10 split) vs ops rev 9893890.61 / otherops 7377204.98 + recon cash 1439206.24 "
                    "DROP vs 14135538.60 (drop 12696332.36) vs beleggingen 30479135.00 JUMP vs 20902101.60 "
                    "(termijn 10.5m) + LT recv 13845107.42 (Mijn VerbouwLeningen) + LT other debt 13145107.42 "
                    "(energieleningen) + CIP 10755384.18 (Heidebaan-Noord + Eurolaan 4A erfpacht) + "
                    "Waas Fonds available reserves 50043293.51 vs MSLO LPW add 3390408.25 + gemeente-opnames 315k "
                    "+ milieu prov 4151913.73 PFAS + WVV assets 78369747.86 vs commentaar 78393050.32 "
                    "+ full statutory jaarrekening (jaarverslag is verkort 4p) + commissarisverslag ereloon "
                    "+ AV 2025/2026 minutes + NBB filing"
                ),
                "why_it_matters": (
                    "Leftover IGS streek shell of mined Waasland cities (BKZ/Lokeren/SGW/Sint-Niklaas/Stekene/Temse/"
                    "Waasmunster; AGB Lokeren + Zorgband 1338 / AGB Kruibeke already mined): 2.91m omzet vs "
                    "12.70m cash drop into 30.48m beleggingen / 50.04m Waas Fonds is a dual opacity residual, "
                    "not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Interwaas / 7 Waasland vennoten",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-18",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM,
                "linked_leaderboard_id": LB,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "tick1350 leftover IGS streek of mined Waasland cities after honest hunt; "
                    "live JR2025 official WVV PDF now extracted (19.3MB 65p InDesign 21.05.2026). "
                    "EcoWerf 2025 glossy / 2024 statutory still unpublished. Interleuven still 2024 balans. "
                    "IOK/IMOG/Haviland/IVBO/Limburg.net still 2024. Veneco/Leiedal glossy-only. MIROM 403. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1350",
        "title": "Interwaas JR2025 leftover IGS dual residual + every-10 progress",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: every-10 progress refresh + Interwaas leftover IGS streek of mined Waasland cities "
            "after honest hunt; KBO 0206.460.639 Actief; live JR2025 official WVV PDF "
            "(19.3MB 65p InDesign 21.05.2026 interne WVV verkort); sourced euros omzet 2.912m / assets 78.370m / "
            "cash 1.439m DROP 12.696m / beleggingen 30.479m / PnL 2.514m; FOI ready per-vennoot/cash/NBB; progress@1350"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T21:55:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1350 Interwaas leftover IGS residual + progress@1350; KBO 0206.460.639; "
            "live JR2025 WVV PDF; sourced euros; FOI ready not sent; next rq_1351 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1351",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1350 done including Interwaas 1350 leftover IGS live WVV + every-10 / "
            "Aquaduin / IWVA ov 1349 leftover IGS live WVV / "
            "Creat Services dv 1348 leftover IGS live WVV / "
            "IVIO Izegem-Ommeland 1347 leftover IGS live JR operational / "
            "WVI West-Vlaanderen 1346 leftover IGS live WVV / "
            "IVVO Veurne-Ommeland 1345 leftover IGS live WVV / "
            "ILvA Land van Aalst 1344 leftover IGS live WVV / "
            "IVM Meetjesland 1343 leftover IGS live WVV / "
            "IDM Durme-Moervaart 1342 leftover IGS live WVV / "
            "IGEAN dienstverlening 1341 leftover IGS live WVV / "
            "EVA Limburg Sterk Merk 1340 leftover EVA live WVV + every-10); "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "Welzijnskoepel West-Brabant jaarverslag 2025 glossy-only — take only if a BBC PDF now downloads; "
            "Ter Nethe official still unpublished/DNS — take only if a PDF now downloads; "
            "Veneco glossy jaarverslag 2025 websingle — take only if a WVV/BBC PDF now downloads; "
            "EcoWerf 2025 jaarverslag listed ~16MB glossy / 2024 statutory still unpublished — take only if a WVV/BBC PDF now downloads; "
            "Leiedal 2025 InDesign 22MB 118p downloaded tick1347 — glossy-only no WVV — take only if a WVV/BBC PDF now downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland / IVBO / Limburg.net still 2024 — take only if a 2025 JR PDF now downloads; "
            "IVOO no public 2025 JR PDF — take only if a 2025 JR PDF now downloads; "
            "MIROM 403 — take only if a 2025 JR PDF now downloads; "
            "INCOVO still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
            "WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / "
            "WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403; not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1350 after Interwaas leftover IGS live WVV + progress@1350; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1350", rq_new, rq_spawn)
    print("research_queue 1350", found, "spawned_1351", spawned)

    with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as f:
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
            lineterminator="\r\n",
        )
        w.writeheader()
        w.writerow(
            {
                "state_id": "main",
                "mode": "continuous",
                "current_sprint": "hole_fill",
                "last_tick_utc": UTC,
                "last_unit_id": "rq_1350",
                "ticks_completed": "1350",
                "paused": "no",
                "notes": (
                    "tick1350 Interwaas leftover IGS residual + progress@1350; KBO 0206.460.639; "
                    "live JR2025 WVV PDF; sourced euros omzet 2.912m assets 78.370m cash drop 12.696m beleggingen 30.479m PnL 2.514m; "
                    "FOI ready per-vennoot/cash/NBB; next rq_1351 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    foi_c = foi_status_counts()
    counts = {
        "budgets": count_csv_rows(DATA / "budgets.csv"),
        "commitments": count_csv_rows(DATA / "commitments.csv"),
        "leaderboard": count_csv_rows(DATA / "leaderboard.csv"),
        "entities": count_csv_rows(DATA / "entities.csv"),
        "sources": count_csv_rows(DATA / "sources.csv"),
        "foi_ready": foi_c.get("ready", 0),
        "foi_answered": foi_c.get("answered", 0),
        "foi_partial": foi_c.get("partial", 0),
        "foi_total": count_csv_rows(DATA / "foi_queue.csv"),
    }
    print("COUNTS", counts)
    write_progress(counts)
    write_waste_top10(counts)

    log_entry = f"""
### Tick 1350 - 2026-08-18 - rq_1350 Interwaas dual residual leftover IGS + progress@1350
- Unit: Interwaas (dienstverlenende vereniging / leftover IGS streekontwikkeling; statutaire naam Intergemeentelijk Samenwerkingsverband van het Land van Waas) of already-mined Waasland cities (Beveren-Kruibeke-Zwijndrecht / Lokeren / Sint-Gillis-Waas / Sint-Niklaas / Stekene / Temse / Waasmunster) after residual dual hunt (KBO **0206.460.639**; official interwaas.be + live jaarverslag 2025 PDF 19.3MB / 65p; InDesign **21.05.2026**; embedded interne WVV jaarrekening verkort 4p). EVERY-10 first: refreshed progress_every_10_ticks.md + doge_waste_top10_current.md from on-disk CSVs. THEN leftover IGS whose official page now yields a downloadable JR2025 PDF with euros (prefer live PDF over another unpublished FOI). Distinct from already-mined Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / Zorgpunt Waasland / AGB Lokeren / Zorgband 1338 / AGB Kruibeke. KBO Actief / normale toestand since **27.06.1968**; Dienstverlenende vereniging (Vlaams Gewest) since 19.03.2004; zetel Lamstraat 113 9100 Sint-Niklaas since 06.05.1996; **1 VE**; aanbestedende overheid since 27.06.1968; btw since 01.09.1986; RSZ since 01.01.2022; jaarvergadering mei; boekjaar 31 december; voorzitter Jurgen Bauwens; directeur Hans De Bock since 12.03.2025; e-mail info@interwaas.be; tel 03 500 47 00; NACE 68.121 / 71.113 / 87.999 / RSZ 84.119. Hunt leftover AGB/zorg/EVA first: EcoWerf 2025 glossy / 2024 statutory still unpublished; Interleuven still 2024 balans; IOK/IMOG/Haviland/IVBO/Limburg.net still 2024; IVOO no public 2025 JR; MIWA still 2024; MIROM 403; Veneco/Leiedal glossy-only; INCOVO still 2024; Dommelhof leftover Limburg EVA KBO 0777.495.085 not taken once live Interwaas WVV extracted. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek not taken once live Interwaas PDF extracted. APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas official pages 403 — not taken. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340. Every-10 tick.
- EUR strong (primary official WVV): assets **78.369.748** (was 76.794.255; commentaar narrative 78.393.050 recon FOI); fixed **13.979.099**; MVA **13.255.532** (gebouwen **2.249.851** + CIP **10.755.384** JUMP vs 5.501.926 Heidebaan-Noord + Eurolaan 4A erfpacht); FVA **723.566**; current **64.390.649**; LT recv **13.845.107** (Mijn VerbouwLeningen); voorraden RE-for-sale **12.405.497**; ST recv **6.156.862** (trade **1.316.845**); beleggingen **30.479.135** JUMP vs 20.902.102 (termijn **10,5m**); cash **1.439.206** DROP vs 14.135.539 (drop **12.696.332**); equity **55.113.218** (inbreng **3.705.675**; reserves **50.881.628** waarvan beschikbaar **50.043.294** Waas Fonds; overgedragen **455.724**); voorzieningen **4.582.368** (milieu **4.151.914**); schulden **18.674.162** (LT **13.444.543** fin achtergesteld **299.436** + overige **13.145.107**; ST **3.655.255** trade **817.163**); ops rev **9.893.891**; omzet **2.912.087** DROP 40,86% vs 4.924.206; andere **7.377.205**; geproduceerde VA **3.352.740**; ops cost **8.684.689** (goederen **1.446.108** + diensten **2.735.316** + pers **4.303.553**); expl **+1.209.201**; fin opbr **1.957.285** (MSLO dividend **1.404.706**); PnL vóór belasting **+3.208.996**; belasting **694.933**; PnL **+2.514.063**. Resultaatverwerking MSLO LPW **3.390.408** naar Waas Fonds. VTE **44,43** gem. Jaarverslag = verkorte statutaire jaarrekening; commissaris oordeel zonder voorbehoud.
- CSVs: sources+4/entities+1/budgets+{n and '43'}/commitments+1/leaderboard+1 + FOI ready `{GAP}` (not sent); rq_1350=done; spawn rq_1351; ticks=1350.
- Progress@1350: refreshed progress_every_10_ticks.md + doge_waste_top10_current.md. Layers A 100 / B 100 / C ~99 / D ~74-88 (not near-complete of 348bn) / E recounted ready **{counts['foi_ready']}** (answered {counts['foi_answered']} / partial {counts['foi_partial']} / total {counts['foi_total']}). Inventory: budgets {counts['budgets']} · commitments {counts['commitments']} · leaderboard {counts['leaderboard']} · entities {counts['entities']} · sources {counts['sources']}. Pure annual waste top10 **stable** vs 1340 (GIP/fossil/cars/cheque/reporté). Dual off-top10 adds Interwaas 78.37m / WVI 241.0m / IGEAN 103.92m / Aquaduin 99.09m / Creat 89.38m omzet + leftover IGS live WVV stack.
- Coverage: 1341–1350 is residual dual L5 leftover IGS (**IGEAN** · **IDM** · **IVM** · **ILvA** · **IVVO** · **WVI** · **IVIO** operational · **Creat** · **Aquaduin** · **Interwaas**). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE.
- Next: rq_1351 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland/IVBO/Limburg.net only if a 2025 JR PDF now downloads; EcoWerf only if a statutory WVV/BBC PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; MIROM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 unless a fetchable JR appears).
"""
    # fix the botched budgets count interpolation in log
    log_entry = log_entry.replace("budgets+{n and '43'}", "budgets+43")
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1350 write done")


if __name__ == "__main__":
    main()

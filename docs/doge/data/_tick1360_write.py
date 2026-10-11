# -*- coding: utf-8 -*-
"""Tick 1360 — every-10 progress FIRST, then leftover ECO2050 cv JR2025 official NBB WVV euros.
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

TICK = "1360"
UTC = "2026-08-19T00:15:00Z"
ENT = "cv_e50"
HIER = "Vlaanderen>Limburg>CV>ECO2050>KlimaatCoop"
GAP = "gap_e50_fva_11_07m_otary_11m_div_0_41m_l5"
SRC = "src_e50_jr2025_nbb"
SRC2 = "src_e50_site"
SRC3 = "src_kbo_e50_0699503028"
SRC4 = "src_e50_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00169452.pdf"
SRC2_URL = "https://eco2050.be/over-ons/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0699503028"
SRC4_URL = "https://eco2050.be/"
FOI_EMAIL = "eco2050@cooperaties.be"
FOI_POSTAL = "Herkenrodesingel 14 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_e50_fva_11_07m_otary_11m_div_0_41m_l5.md"
COMM = "comm_e50_jr2025_fva"
LB = "lb_e50_fva_11_07m_otary_11m_div_0_41m"


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
    marker = "## Snapshot at **tick 1350** (2026-08-18)"
    if marker not in text:
        raise SystemExit("progress file missing tick 1350 marker")
    snap = f"""## Snapshot at **tick 1360** (2026-08-19)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1351-1360 leftover IGS/NV/cv: **SOLVA** · **IVBO** · **Limburg.net** glossy · **Bionerga** · **NUHMA AC** · **Nuhma cv** · **EcoWerf** · **NUHMA DC** · **Nubema** · **ECO2050** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1351-1360 is VL residual dual L5 leftover IGS/NV/cv (not near-complete of 348bn):** **Nuhma cv** assets **693.83m** PnL **+26.27m** div **33.50m** · **NUHMA AC** assets **630.63m** PnL **+8.77m** · **Bionerga** assets **82.92m** PnL **−33.80m** · **IVBO** assets **79.79m** omzet **55.56m** · **SOLVA** assets **64.24m** omzet **25.52m** · **NUHMA DC** assets **52.32m** PnL **−1.21m** debt **20.51m** · **EcoWerf** assets **46.23m** omzet **53.57m** · **ECO2050** assets **11.54m** FVA **11.07m** Otary **11.00m** div **0.41m** · **Nubema** assets **188.5k** omzet **12.2k** uncalled **375k** · Limburg.net glossy-only · prior leftover IGS Interwaas/WVI/IGEAN/Aquaduin/Creat stack retained |
| **E. FOI-ready gaps** | **~{counts['foi_ready']}** drafts ready | Human send only; answered **~{counts['foi_answered']}**; partial **~{counts['foi_partial']}**; total FOI rows **~{counts['foi_total']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual debt/AFM NEG + leasing/city-loan/erfpacht/DBFM/portfolio/waste-water-streek/klimaat-holding shells** (**NEW ECO2050** assets **EUR11.54m** FVA **EUR11.07m** Otary **EUR11.00m** Sunfin **EUR70k** div **EUR0.41m** · **Nuhma cv** assets **EUR693.83m** PnL **+EUR26.27m** div **EUR33.50m** · **NUHMA AC** assets **EUR630.63m** PnL **+EUR8.77m** · **Bionerga** assets **EUR82.92m** PnL **−EUR33.80m** · **IVBO** assets **EUR79.79m** omzet **EUR55.56m** · **SOLVA** assets **EUR64.24m** omzet **EUR25.52m** · **NUHMA DC** assets **EUR52.32m** PnL **−EUR1.21m** debt **EUR20.51m** · **EcoWerf** assets **EUR46.23m** omzet **EUR53.57m** · **Nubema** assets **EUR188.5k** uncalled **EUR375k** · leftover IGS Limburg.net glossy · prior **Interwaas** assets **EUR78.37m** cash **EUR1.44m DROP 12.70m** beleggingen **EUR30.48m** omzet **EUR2.91m** · **WVI** assets **EUR241.0m** stock **EUR181.88m** · **IGEAN DV** assets **EUR103.92m** inv **EUR68.19m** · **Aquaduin** assets **EUR99.09m** omzet **EUR26.50m** sanering **EUR31.33m** · **Creat** omzet **EUR89.38m** · leftover IGS IVM/ILvA/IVVO/IDM/IVIO · prior **EVA LSM** assets **EUR85.85m** cash **EUR3.39m DROP 10.74m** portfolio **EUR58.31m** PnL **+EUR1.5k** · **WV Zorgband** assets **EUR61.86m** PnL **−EUR5.83m** lease **EUR43.75m** · **WV Zorgbedrijf Brasschaat** assets **EUR28.94m** cash **EUR2.65m** BBR **−EUR5.39m** LT-recv **EUR17.90m** · leftover zorg live BBC Het Dak / OPcura / BVK / Weldenderend · leftover FOI Vormingscentrum Malle / Inagro / Sleutelzorg · prior **APB Hooibeekhoeve** assets **EUR5.93m** cash **EUR2.65m** ST recv **EUR2.82m** BBR **+EUR1.30m** · **EVA Pluimveehouderij** assets **EUR8.63m** cash **EUR4.08m** ST recv **EUR4.46m** BBR **+EUR1.17m** · **APB Vonk** assets **EUR1.02m** cash **EUR0.96m** BBR **+EUR0.16m** · leftover FOI (Blankenberge / Campus Vesta / Monumentenwacht / Vlabinvest / Zilvermeer / Zorg HH / **EVA Kinderopvang Dilbeek**) · prior **APB KampC** assets **EUR5.93m** cash **EUR2.65m** ST recv **EUR3.06m** BBR **+EUR2.39m** J5/T2 werksub gap **EUR1.25m** · **APB PSES** assets **EUR186.52m** ST recv **EUR165.31m** BBR **−EUR1.29m** · **APB GKC** assets **EUR2.67m** cash **EUR2.11m** · **APB Havencentrum** assets **EUR0.97m** Havenwereld **EUR0.40m** · **AGBIM** CCAO **EUR8.91m** · **AGB Maaseik** fin debt **EUR1.60m** AFM **−EUR0.67m** · prior **APB VERA** fin debt **EUR1.72m** equity **−EUR1.64m** straight loan **EUR1.10m** · **Edegem** fin debt **EUR14.05m** pension **EUR23.40m** · **Beerse city** fin debt **EUR13.82m** · **AGB Beerse** fin debt **EUR5.02m** · **Pepingen city** fin debt **EUR3.47m** · **Vleteren** fin debt **EUR3.32m** · prior **Stad+OCMW Kortenaken** fin debt **EUR10.57m** IGS EV-reval **EUR8.90m** OCMW equity **−EUR5.41m** · **Heusden-Zolder** fin debt **EUR37.85m** IGS reval **EUR31.12m** · **Kapelle-op-den-Bos** fin debt **EUR18.87m** · **Oud-Heverlee** fin debt **EUR15.18m** · **Diepenbeek city** fin debt **EUR13.59m** IGS reval **EUR19.43m** · **Huldenberg** fin debt **EUR9.56m** · **AGB Kortenaken** fin debt **EUR3.28m** leasing **EUR3.22m** · **Voeren** fin debt **EUR3.37m** · **AGB Diepenbeek** fin debt **EUR3.03m** · **Steenokkerzeel** fin debt **EUR2.49m** · prior **Stad+OCMW Bekkevoort** fin debt **EUR9.77m** IGS EV-reval **EUR5.90m** · **HH city** fin debt **EUR17.37m** · **AGB Masterplan HH** fin debt **EUR27.81m** · **AGB Sport HH** fin debt **EUR10.72m** · **AGB SCO Ronse** fin debt **EUR22.65m** · **Ronse city** fin debt **EUR25.02m** pension **EUR19.50m** · **Kraainem** fin debt **EUR6.40m** · **Tielt-Winge** fin debt **EUR8.52m** · prior **Stad+OCMW Tienen** fin debt **EUR59.73m** pension **EUR51.29m** · **Machelen** fin debt **EUR26.37m** Farys lease **EUR16.90m** · **AGB Tienen** fin debt **EUR16.93m** · **AG Museum Leuven** fin debt **EUR14.51m** · **Gingelom** Fluvius reval **EUR9.75m** fin debt **EUR3.86m** · prior **AGB MAC** fin debt **EUR40.3m** leasing **EUR40.8m** · **Mintus** dual **EUR26.36m** · Digipolis assets **EUR73.61m** · **AG Vespa** fin debt **EUR179.6m** DBFM **EUR109.4m** · **sogent** AFM **−EUR3.90m** debt **EUR96.3m** · AG-O cum loss **−EUR29.2m** · Zorgbedrijf Antwerpen AFM **−EUR18.87m** debt **EUR220m** / Dodoens equity **−EUR18.88m** / Hasselt ~EUR95–103m stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market.

### Inventory (tick 1360)

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
| research_queue open | rq_116 deferred + rq_1361 hole-fill after progress |

### What improved since tick 1350

- **VL residual dual JR2025 leftover IGS/NV/cv (tick1351-1359):** **Nuhma cv** assets **693.83m** PnL **+26.27m** div **33.50m** · **NUHMA AC** assets **630.63m** PnL **+8.77m** · **Bionerga** assets **82.92m** PnL **−33.80m** · **IVBO** assets **79.79m** omzet **55.56m** · **SOLVA** assets **64.24m** omzet **25.52m** · **NUHMA DC** assets **52.32m** PnL **−1.21m** debt **20.51m** · **EcoWerf** assets **46.23m** omzet **53.57m** · **Nubema** assets **188.5k** omzet **12.2k** uncalled **375k** · Limburg.net glossy-only — no invented euros.
- **NEW (tick1360):** **ECO2050** (KBO 0699.503.028) leftover erkende cv founded by Nuhma cv / Nubema / Nuhmeris of already-mined Limburg cities. Official NBB WVV VOL-inb deposit **2026-00169452** PDF (3.93MB / 42p; AV 12.06.2026; neerlegging 15.06.2026). Assets **11.540.749** · FVA **11.070.000** (Otary **11.000.000** + Sunfin **70.000**) · cash **65.090 DROP** vs 145.130 · PnL **+500.298** · dividend B **408.870**. FOI ready. Every-10 progress refresh from on-disk CSVs.
- **Dual map themes:** **leftover klimaat-holding NV/cv + citizen-coop FVA loan shells** (Nuhma cv 694m / NUHMA AC 631m / ECO2050 11.54m Otary 11m / Nubema 188.5k) · leftover waste IGS/NV (Bionerga 83m PnL −33.8m / IVBO 80m / EcoWerf 46m) · leftover IGS streek (SOLVA 64m) · prior leftover IGS waste/water/streek + EVA LRM-portfolio + leftover zorg live BBC stack retained.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10.

---
"""
    text = text.replace(marker, snap + marker, 1)
    prog.write_text(text, encoding="utf-8")
    print("progress_every_10_ticks.md inserted tick 1360 snapshot")


def write_waste_top10(counts: dict) -> None:
    p = DATA / "doge_waste_top10_current.md"
    text = p.read_text(encoding="utf-8")
    text = text.replace(
        "**As-of:** tick **1350** (2026-08-18) · **7154** leaderboard rows",
        f"**As-of:** tick **1360** (2026-08-19) · **{counts['leaderboard']}** leaderboard rows",
        1,
    )
    old_dual = "(**NEW Interwaas** assets **€78.37m** cash **€1.44m DROP 12.70m** beleggingen **€30.48m** omzet **€2.91m**"
    new_dual = (
        "(**NEW ECO2050** assets **€11.54m** FVA **€11.07m** Otary **€11.00m** Sunfin **€70k** div **€0.41m** · "
        "**Nuhma cv** assets **€693.83m** PnL **+€26.27m** div **€33.50m** · "
        "**NUHMA AC** assets **€630.63m** PnL **+€8.77m** · "
        "**Bionerga** assets **€82.92m** PnL **−€33.80m** · "
        "**IVBO** assets **€79.79m** omzet **€55.56m** · "
        "**SOLVA** assets **€64.24m** omzet **€25.52m** · "
        "**NUHMA DC** assets **€52.32m** PnL **−€1.21m** debt **€20.51m** · "
        "**EcoWerf** assets **€46.23m** omzet **€53.57m** · "
        "**Nubema** assets **€188.5k** uncalled **€375k** · leftover IGS Limburg.net glossy · "
        "prior **Interwaas** assets **€78.37m** cash **€1.44m DROP 12.70m** beleggingen **€30.48m** omzet **€2.91m**"
    )
    if old_dual not in text:
        raise SystemExit("waste top10 missing Interwaas dual marker")
    text = text.replace(old_dual, new_dual, 1)
    old_chg = (
        "**Change vs tick 1340:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
        "**Major NEW residual 1341–1350 (off pure top10 / dual):**"
    )
    new_chg = (
        "**Change vs tick 1350:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
        "**Major NEW residual 1351–1360 (off pure top10 / dual):** **ECO2050** assets **EUR11.54m** FVA **EUR11.07m** Otary **EUR11.00m** div **EUR0.41m** · **Nuhma cv** assets **EUR693.83m** PnL **+EUR26.27m** div **EUR33.50m** · **NUHMA AC** assets **EUR630.63m** PnL **+EUR8.77m** · **Bionerga** assets **EUR82.92m** PnL **−EUR33.80m** · **IVBO** assets **EUR79.79m** omzet **EUR55.56m** · **SOLVA** assets **EUR64.24m** omzet **EUR25.52m** · **NUHMA DC** assets **EUR52.32m** PnL **−EUR1.21m** debt **EUR20.51m** · **EcoWerf** assets **EUR46.23m** omzet **EUR53.57m** · **Nubema** assets **EUR188.5k** uncalled **EUR375k** · Limburg.net glossy-only. "
        "Gain is **leftover klimaat-holding NV/cv + citizen-coop FVA loan + leftover waste IGS/NV**. "
        "**Prior 1341–1350 retained:**"
    )
    if old_chg not in text:
        raise SystemExit("waste top10 missing change-vs-1340 marker")
    text = text.replace(old_chg, new_chg, 1)
    old_out = "| — | `lb_iws_omzet_2_91m_cash_drop_12_70m` | **78.37 m stock** | **~6.2 dual** | **NEW 1350** Interwaas omzet 2.91m / cash drop 12.70m / beleggingen 30.48m |"
    new_out = (
        "| — | `lb_e50_fva_11_07m_otary_11m_div_0_41m` | **11.54 m stock** | **~6.3 dual** | **NEW 1360** ECO2050 FVA 11.07m / Otary 11.00m / div 0.41m |\n"
        "| — | `lb_nuhc_pnl_26_27m_div_33_50m_fva_drop` | **693.83 m stock** | **~7.1 dual** | 1356 Nuhma cv leftover cv pnl 26.27m / div 33.50m |\n"
        "| — | `lb_nuhma_pnl_8_77m_div_8_33m_fva_drop` | **630.63 m stock** | **~6.9 dual** | 1355 NUHMA AC leftover NV pnl 8.77m / div 8.33m |\n"
        "| — | `lb_bng_omzet_22_56m_pnl_neg_33_80m_fva_drop` | **82.92 m stock** | **~6.6 dual** | 1354 Bionerga leftover NV pnl −33.80m / FVA drop |\n"
        "| — | `lb_ivbo_omzet_55_56m_assets_79_79m_pers_19_85m` | **79.79 m stock** | **~6.2 dual** | 1352 IVBO leftover IGS omzet 55.56m / pers 19.85m |\n"
        "| — | `lb_solva_omzet_25_52m_stock_47_2m_pnl_neg` | **64.24 m stock** | **~6.1 dual** | 1351 SOLVA leftover IGS omzet 25.52m / PnL −0.20m |\n"
        "| — | `lb_nuhd_pnl_neg_1_21m_debt_20_51m_fva_impair` | **52.32 m stock** | **~6.7 dual** | 1358 NUHMA DC leftover BV pnl −1.21m / debt 20.51m |\n"
        "| — | `lb_ecow_omzet_53_57m_pers_25_80m_pnl_neg` | **46.23 m stock** | **~6.9 dual** | 1357 EcoWerf leftover IGS omzet 53.57m / pers 25.80m |\n"
        + old_out.replace("**NEW 1350**", "1350")
    )
    if old_out not in text:
        raise SystemExit("waste top10 missing iws just-outside row")
    text = text.replace(old_out, new_out, 1)
    old_abs = "| `lb_iws_omzet_2_91m_cash_drop_12_70m` | **6.2** | **NEW 1350** Interwaas assets 78.37m / cash drop 12.70m / beleggingen 30.48m / omzet 2.91m |"
    new_abs = (
        "| `lb_e50_fva_11_07m_otary_11m_div_0_41m` | **7.2** | **NEW 1360** ECO2050 assets 11.54m / FVA 11.07m Otary 11.00m / 0-VTE citizen coop |\n"
        "| `lb_nuhc_pnl_26_27m_div_33_50m_fva_drop` | **7.1** | 1356 Nuhma cv leftover cv assets 693.83m / div 33.50m |\n"
        "| `lb_bng_omzet_22_56m_pnl_neg_33_80m_fva_drop` | **6.6** | 1354 Bionerga leftover NV pnl −33.80m |\n"
        + old_abs.replace("**NEW 1350**", "1350")
    )
    if old_abs not in text:
        raise SystemExit("waste top10 missing iws absurdity row")
    text = text.replace(old_abs, new_abs, 1)
    p.write_text(text, encoding="utf-8")
    print("doge_waste_top10_current.md updated tick 1360; pure top10 unchanged")


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "ECO2050 erkende cv jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00169452; AV 12.06.2026)",
                "url": SRC_URL,
                "publisher": "ECO2050 cv / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1360; official NBB VOL-inb PDF 3.93MB 42p deposit 2026-00169452 neerlegging 15.06.2026 created 18.06.2026; "
                    "leftover klimaat-coop founded by Nuhma cv 1356 / Nubema 1359 / Nuhmeris; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris EY / Christophe Beckers; every-10"
                ),
            },
            {
                "source_id": SRC2,
                "title": "ECO2050 official site over-ons + statutory JR2025 PDF (same WVV; 40p site vs 42p NBB)",
                "url": SRC2_URL,
                "publisher": "ECO2050 erkende cv",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1360; leftover cv of mined Limburg + Nuhma cv/Nubema/NUHMA DC/AC/Bionerga/Limburg.net; "
                    "eco2050.be/wp-content/uploads/2026/06/Jaarrekening_31_12_2025.pdf HTTP 200 4.12MB 40p; "
                    "1.252 cooperanten 12.06.2026; uitgifte 15.06.2026-15.05.2027 beoogd 5m"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO ECO2050 0699.503.028",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1360; KBO 0699.503.028 Actief / normale toestand since 02.07.2018; "
                    "statutaire naam ECO2050 since 02.07.2018; CV since 13.05.2019; "
                    "Erkende Cooperatieve Vennootschap since 01.03.2019; "
                    "zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; 1 VE; "
                    "jaarvergadering juni; boekjaar 31 december; dagelijks bestuur Nuhma cv 0472.325.068; "
                    "no KBO email/web/tel/NACE"
                ),
            },
            {
                "source_id": SRC4,
                "title": "ECO2050 FOI channel / official contact (site email; parent Nuhma dagelijks bestuur)",
                "url": SRC4_URL,
                "publisher": "ECO2050 cv / Nuhma cv",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1360; FOI eco2050@cooperaties.be; parent info@nuhma.be 011 49 56 10; "
                    "Herkenrodesingel 14 3500 Hasselt (same zetel as Nuhma cv / Nubema / NUHMA DC / NUHMA AC / Bionerga / Limburg.net)"
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
                "name_nl": "ECO2050 (leftover erkende klimaat-cooperatie / opgericht door Nuhma cv + Nubema + Nuhmeris)",
                "name_fr": "ECO2050 (cooperative climat residuelle / fondee par Nuhma sc + Nubema + Nuhmeris)",
                "name_en": "ECO2050 leftover recognised climate cooperative (founded by Nuhma cv / Nubema / Nuhmeris)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://eco2050.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1360 leftover residual erkende cv founded by Nuhma cv 1356 "
                    "+ Nubema 1359 + NUHMA DC 1358 + NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353 (same zetel Herkenrodesingel 14); "
                    "KBO 0699.503.028 Actief since 02.07.2018; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 11540749 fva 11070000 otary 11000000 pnl 500298 div 408870; "
                    "FOI ready Otary/Sunfin/related-party/6.15/Nubema-book"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_e50_assets_2025", ENT, "2025", "11540749", "2025 assets 11540749 VOL-inb 20/58; tick1360; primary official NBB WVV; RvB 11540749.34"),
        ("bud_e50_assets_2024", ENT, "2024", "10899697", "2024 assets 10899697 comparative; tick1360; primary official NBB WVV 20/58"),
        ("bud_e50_fixed_2025", ENT, "2025", "11079058", "2025 vaste activa 11079058 JUMP vs 10324271; tick1360; primary official NBB WVV 21/28"),
        ("bud_e50_iva_2025", ENT, "2025", "9058", "2025 IVA 9058 JUMP vs 4271; tick1360; primary official NBB WVV 21"),
        ("bud_e50_fva_2025", ENT, "2025", "11070000", "2025 FVA andere vorderingen 11070000 JUMP vs 10320000; tick1360; primary official NBB WVV 28/285/8"),
        ("bud_e50_fva_2024", ENT, "2024", "10320000", "2024 FVA 10320000 comparative; tick1360; primary official NBB WVV 28"),
        ("bud_e50_otary_2025", ENT, "2025", "11000000", "2025 Otary RS NV achtergesteld 11000000 (30.05.2024; tot 01.06.2027; kader 10-15m); tick1360; primary official NBB WVV RvB"),
        ("bud_e50_sunfin_2025", ENT, "2025", "70000", "2025 Sunfin BV 70000 PV gemeentelijke gebouwen; tick1360; primary official NBB WVV RvB"),
        ("bud_e50_current_2025", ENT, "2025", "461691", "2025 vlottende activa 461691 DROP vs 575426; tick1360; primary official NBB WVV 29/58"),
        ("bud_e50_cash_2025", ENT, "2025", "65090", "2025 liquide middelen 65090 DROP vs 145130; tick1360; primary official NBB WVV 54/58"),
        ("bud_e50_cash_2024", ENT, "2024", "145130", "2024 liquide middelen 145130 comparative; tick1360; primary official NBB WVV 54/58"),
        ("bud_e50_prepaid_2025", ENT, "2025", "396602", "2025 overlopend actief 396602 (kosten 2321 + interest 394281); tick1360; primary official NBB WVV 490/1"),
        ("bud_e50_equity_2025", ENT, "2025", "10142650", "2025 eigen vermogen 10142650 JUMP vs 9023080; tick1360; primary official NBB WVV 10/15"),
        ("bud_e50_equity_2024", ENT, "2024", "9023080", "2024 eigen vermogen 9023080 comparative; tick1360; primary official NBB WVV 10/15"),
        ("bud_e50_inbreng_2025", ENT, "2025", "10018706", "2025 inbreng 10018706 (beschikbaar 9998706 + onbeschikbaar 20000); tick1360; primary official NBB WVV 10/11"),
        ("bud_e50_reserves_2025", ENT, "2025", "123944", "2025 beschikbare reserves 123944 JUMP vs 47717; tick1360; primary official NBB WVV 13/133"),
        ("bud_e50_debt_2025", ENT, "2025", "1398099", "2025 schulden 1398099 DROP vs 1876617; tick1360; primary official NBB WVV 17/49"),
        ("bud_e50_debt_2024", ENT, "2024", "1876617", "2024 schulden 1876617 comparative; tick1360; primary official NBB WVV 17/49"),
        ("bud_e50_lt_2025", ENT, "2025", "587000", "2025 LT overige leningen 587000 DROP vs 935000; tick1360; primary official NBB WVV 17/174"),
        ("bud_e50_st_2025", ENT, "2025", "758684", "2025 ST schulden 758684 (trade 23423 + tax 2135 + overige 733127); tick1360; primary official NBB WVV 42/48"),
        ("bud_e50_stother_2025", ENT, "2025", "733127", "2025 ST overige schulden 733127 DROP vs 874740; tick1360; primary official NBB WVV 47/48"),
        ("bud_e50_accrued_2025", ENT, "2025", "52415", "2025 overlopend passief 52415 JUMP vs 27646; tick1360; primary official NBB WVV 492/3"),
        ("bud_e50_reldebt_2025", ENT, "2025", "645447", "2025 verbonden schulden 645447 (LT 587000 + ST 58447) DROP vs 991565; tick1360; primary official NBB WVV 9351"),
        ("bud_e50_omzet_2025", ENT, "2025", "0", "2025 omzet 0 (code 70 empty); tick1360; primary official NBB WVV 70"),
        ("bud_e50_opscost_2025", ENT, "2025", "50400", "2025 bedrijfskosten 50400 (diensten 46218 + afschr 2546 + andere 1636); tick1360; primary official NBB WVV 60/66A"),
        ("bud_e50_diensten_2025", ENT, "2025", "46218", "2025 diensten 46218 DROP vs 51099; tick1360; primary official NBB WVV 61"),
        ("bud_e50_expl_2025", ENT, "2025", "-50400", "2025 bedrijfsverlies -50400; tick1360; primary official NBB WVV 9901"),
        ("bud_e50_fininc_2025", ENT, "2025", "683109", "2025 financiele opbrengsten 683109 JUMP vs 581817 (FVA 750); tick1360; primary official NBB WVV 75"),
        ("bud_e50_fincost_2025", ENT, "2025", "25276", "2025 financiele kosten 25276 (schulden 25119 + andere 157); tick1360; primary official NBB WVV 65"),
        ("bud_e50_tax_2025", ENT, "2025", "107135", "2025 belastingen 107135 JUMP vs 82347; tick1360; primary official NBB WVV 67/77"),
        ("bud_e50_pnl_2025", ENT, "2025", "500298", "2025 PnL 9904 500298 JUMP vs 419113; tick1360; primary official NBB WVV + RvB 500298.32"),
        ("bud_e50_pnl_2024", ENT, "2024", "419113", "2024 PnL 419113 comparative; tick1360; primary official NBB WVV 9904"),
        ("bud_e50_div_2025", ENT, "2025", "408870", "2025 vergoeding inbreng/dividend B 408870 (4.50pct; A/C verzaken); tick1360; primary official NBB WVV 694"),
        ("bud_e50_otherpay_2025", ENT, "2025", "15201", "2025 andere rechthebbenden 15201; tick1360; primary official NBB WVV 697"),
        ("bud_e50_resadd_2025", ENT, "2025", "76227", "2025 toevoeging overige reserves 76227; tick1360; primary official NBB WVV 6921"),
        ("bud_e50_pers_2025", ENT, "2025", "0", "2025 pers/VTE 0 (9086/9087/62 empty); tick1360; primary official NBB WVV 6.10"),
        ("bud_e50_comm_2025", ENT, "2025", "5736", "2025 commissaris EY 5736 + extra 2050 liquiditeitstest; tick1360; primary official NBB WVV 9505/95061"),
        ("bud_e50_bcap_2025", ENT, "2025", "9578301", "2025 B-cooperanten 1232 invested 9578301.31 (RvB; 190487 Cat B); tick1360; primary official NBB WVV RvB; not TE-additive"),
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
                "title": "ECO2050 cv JR2025 leftover cv dual (assets 11.54m / FVA 11.07m Otary 11m / div 0.41m / 0-VTE)",
                "entity_id": ENT,
                "beneficiary": "ECO2050 / Otary RS NV / Sunfin BV / B-cooperanten / Nuhma cv",
                "legal_basis": "WVV erkende cv; Bestuursdecreet openbaarheid; NBB neerlegging; NRC-erkenning",
                "decision_date": "2026-06-12",
                "start_year": "2018",
                "end_year": "2027",
                "total_envelope_eur": "11540749",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover cv map VL klimaat-coop — Otary 11m PEZ / Sunfin 70k municipal PV / Nubema book-vs-EV",
                "cut_option": "Publish Otary 11m rate/use/PEZ impact + Sunfin municipal PV list + related-party 645k RC + why A/C waive dividend + Nubema 2025 book vs 10.14m EV; do not keep 11m citizen money as unsecured subordinated loan after PEZ tender stop",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1360; assets 11540749 fva 11070000 otary 11000000 pnl 500298 div 408870; FOI ready not sent; every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "ECO2050 cv JR2025 leftover cv: assets 11.54m / FVA 11.07m Otary 11m / Sunfin 70k / div 0.41m / 0-VTE",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "408870",
                "total_cost_eur": "11540749",
                "tco_notes": (
                    "Leftover dual klimaat-coop founded by Nuhma cv / Nubema / Nuhmeris of mined Limburg cities: "
                    "assets 11.54m / equity 10.14m / pnl +0.50m / omzet 0 / pers 0 / "
                    "FVA 11.07m (Otary subordinated 11.00m to 01.06.2027 + Sunfin 70k municipal PV) / "
                    "cash drop 80.0k / related-party debt 645k / 1232 B-citizens 9.58m / A+C waive dividend; "
                    "Nubema 1359 still books 1k vs 10.14m EV; official NBB WVV live; "
                    "do not treat 11.54m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "ECO2050 / Otary RS NV / Sunfin BV / B-cooperanten / Nuhma cv",
                "stated_goal": "Local leftover cv map VL klimaat-coop — JR2025 live; dual Otary/Sunfin/related-party FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 11.54m / FVA 11.07m Otary 11.00m / pnl +0.50m / div 0.41m; 0 VTE",
                "absurdity_score": "7.2",
                "cost_score": "5.5",
                "difficulty": "2.5",
                "priority_index": "6.3",
                "cut_proposal": "Publish Otary 11m rate/use/PEZ impact + Sunfin municipal PV list + related-party 645k RC + why A/C waive dividend + Nubema 2025 book vs 10.14m EV; do not keep 11m citizen money as unsecured subordinated loan after PEZ tender stop",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1360; leftover cv of mined Limburg + Nuhma cv 1356 / Nubema 1359 / NUHMA DC 1358 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; FOI ready not sent; not TE-additive of 348bn; every-10",
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
                    "Otary RS NV achtergesteld 11000000 (30.05.2024; tot 01.06.2027; kader 10-15m; WVV 285/8) rate / zekerheden / PEZ-Haddock use "
                    "+ Sunfin BV 70000 municipal PV counterparties "
                    "+ related-party debt 645447 (WVV 9351; LT 587000 + ST 58447) / RC Nuhma cv + Efin BV "
                    "+ ST overige 733127 counterparties "
                    "+ 6.15 related-party refusal (no wettelijk kader) "
                    "+ why Nubema 1359 6.5.1 still 1 Cat A / 5pct / book 1000 / EV 8772472 (2023) vs ECO2050 2025 20 Cat A / EV 10142650 "
                    "+ why A/C waive dividend while 408870 (4.50pct) goes only to B "
                    "+ why 0-VTE / 0-omzet cv holds 11.07m FVA loans "
                    "+ AV 12.06.2026 minutes + RvB 23.03.2026 + commissaris extra 2050 liquiditeitstest"
                ),
                "why_it_matters": (
                    "Leftover klimaat-coop founded by Nuhma cv / Nubema / Nuhmeris of mined Limburg cities + NUHMA DC 1358 "
                    "+ NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353 (same zetel Herkenrodesingel 14): "
                    "11.54m assets / 11.07m FVA (Otary 11m after PEZ tender stop) / 0 omzet / 0 VTE / "
                    "1232 citizens 9.58m / related-party 645k / Nubema still books 1k vs 10.14m EV "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "ECO2050 erkende cv / Nuhma cv / Limburg municipalities",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-19",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM,
                "linked_leaderboard_id": LB,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "tick1360 leftover cv of mined Limburg cities + Nuhma cv 1356 / Nubema 1359 / NUHMA DC 1358 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (3.93MB 42p deposit 2026-00169452). "
                    "AGB MAC already mined 1270 — skipped. Westtoer already mined — skipped. "
                    "Nubema already mined 1359 — skipped. NUHMA DC already mined 1358 — skipped. EcoWerf already mined 1357 — skipped. "
                    "IOK/IMOG/Haviland still 2024. Interleuven still 2024 balans. "
                    "POM Limburg glossy-only. Veneco/Leiedal glossy. NBB consult skipped. "
                    "Nuhmeris NV 0560.976.140 CDN 2026-00124698 live — leftover next. "
                    "Belscope/Companyweb euros not used. ready not sent; every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1360",
        "title": "ECO2050 cv JR2025 leftover dual residual + every-10 progress",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: every-10 progress refresh from on-disk CSVs + ECO2050 leftover erkende cv founded by Nuhma cv / Nubema / Nuhmeris "
            "of mined Limburg cities after honest hunt; KBO 0699.503.028 Actief; live JR2025 official NBB WVV VOL-inb PDF "
            "(3.93MB 42p deposit 2026-00169452; commissaris EY); "
            "sourced euros assets 11540749 / fva 11070000 / otary 11000000 / pnl 500298 / div 408870; "
            "FOI ready Otary/Sunfin/related-party/6.15/Nubema-book"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T03:05:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1360 ECO2050 leftover cv residual + every-10; KBO 0699.503.028; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1361 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1361",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1360 done including ECO2050 cv 1360 leftover klimaat-coop live NBB WVV + every-10 / "
            "Nubema NV 1359 leftover klimaat-holding live NBB WVV / "
            "NUHMA DC BV 1358 leftover klimaat-holding live NBB WVV / "
            "EcoWerf 1357 leftover IGS live NBB WVV / "
            "Nuhma cv 1356 leftover klimaat-holding live NBB WVV / "
            "NUHMA AC NV 1355 leftover klimaat-holding live NBB WVV / "
            "Bionerga NV 1354 leftover waste-processing live NBB WVV / "
            "Limburg.net 1353 leftover IGS glossy-only FOI / IVBO 1352 leftover IGS live WVV / "
            "SOLVA 1351 leftover IGS live JR / Interwaas 1350 leftover IGS live WVV + every-10); "
            "Nuhmeris NV leftover klimaat-holding KBO 0560.976.140 — take if CDN 2026-00124698 still live; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland still 2024 — take only if a 2025 JR PDF now downloads; "
            "Veneco / Leiedal / IVOO / MIROM / INCOVO / IVAGO / MIWA / IVAREM / IGEMO — take only if a statutory 2025 WVV/BBC PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1360 after ECO2050 leftover cv live NBB WVV + every-10; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1360", rq_new, rq_spawn)
    print("research_queue 1360", found, "spawned_1361", spawned)

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
                "last_unit_id": "rq_1360",
                "ticks_completed": "1360",
                "paused": "no",
                "notes": (
                    "tick1360 ECO2050 leftover cv residual + every-10; KBO 0699.503.028; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 11540749 fva 11070000 otary 11000000 pnl 500298 div 408870; "
                    "FOI ready Otary/Sunfin/related-party/6.15; next rq_1361 residual dual L5 VL; continuous hole_fill"
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
        "foi_total": sum(foi_c.values()),
    }
    print("inventory", counts)
    write_progress(counts)
    write_waste_top10(counts)

    log_entry = f"""
### Tick 1360 - 2026-08-19 - rq_1360 ECO2050 cv dual residual leftover + progress@1360
- Unit: ECO2050 erkende cv (leftover klimaat-cooperatie / opgericht door Nuhma cv + Nubema NV + Nuhmeris NV) of already-mined Limburg cities via Nuhma cv tick1356 (Hasselt / Genk / Tongeren-Borgloon / Houthalen-Helchteren / Bilzen-Hoeselt / Leopoldsburg / Nieuwerkerken / Gingelom / Pelt / Maasmechelen) + leftover NV Nubema tick1359 + leftover BV NUHMA DC tick1358 + leftover NV NUHMA AC tick1355 + leftover NV Bionerga tick1354 + leftover IGS Limburg.net tick1353 after residual dual hunt (KBO **0699.503.028**; official eco2050.be + live NBB WVV VOL-inb deposit **2026-00169452** PDF 3.93MB / 42p; AV **12.06.2026**; neerlegging **15.06.2026**; PDF created **18.06.2026**; commissaris EY / Christophe Beckers). EVERY-10 first: refreshed progress_every_10_ticks.md + doge_waste_top10_current.md from on-disk CSVs. THEN leftover cv whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last tick listed ECO2050 as leftover later pending 2025 WVV). Distinct from already-mined Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **02.07.2018**; statutaire naam ECO2050 since 02.07.2018; Cooperatieve vennootschap since 13.05.2019; Erkende Cooperatieve Vennootschap since 01.03.2019; zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; **1 VE**; jaarvergadering juni; boekjaar 31 december; dagelijks bestuur Nuhma cv 0472.325.068 (Ludo Kelchtermans); e-mail eco2050@cooperaties.be; no KBO NACE. Hunt leftover AGB/zorg/EVA first: AGB MAC Mechelen 2025 BBC already mined tick1270 — skipped; SportAG Aalst / AGB Deinze / AGB Genk already mined — skipped; Westtoer APB already mined — skipped; Nubema already mined 1359 — skipped; NUHMA DC already mined 1358 — skipped; EcoWerf already mined 1357 — skipped; ECO2050 statutory CDN + site JR now live this tick (HTTP 200 / 3926681 / 42p + 4124653 / 40p) — taken. IOK/IMOG/Haviland still 2024; Interleuven 2025 jaarverslag InDesign embed only / balans still 2024; POM Limburg glossy-only — not taken; Veneco/Leiedal glossy-only; IVAREM activiteitenverslag glossy; IGEMO activiteitenverslag only; IVOO no public 2025 JR; IVAGO SSL EOF; MIWA flipbook; MIROM Cloudflare; De Schorre provincieantwerpen.be 403; APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas not taken (ECO2050 WVV live); Dommelhof leftover Limburg EVA KBO 0777.495.085 not taken. Leftover Nuhmeris NV 0560.976.140 CDN 2026-00124698 live — leftover next. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE no fetchable 2025 JR this tick. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345. Every-10 tick.
- EUR strong (primary official WVV VOL-inb + RvB 23.03.2026; commissaris EY): assets **11.540.749** (was 10.899.697; RvB 11.540.749,34); fixed **11.079.058**; IVA **9.058**; FVA **11.070.000** JUMP vs 10.320.000 (Otary RS NV achtergesteld **11.000.000** 30.05.2024 tot 01.06.2027 kader 10–15m; Sunfin BV **70.000** PV gemeentelijke gebouwen; +750.000 toevoeging); current **461.691** DROP vs 575.426; cash **65.090 DROP** vs 145.130; prepaid **396.602** (interest 394.281); equity **10.142.650** JUMP vs 9.023.080 (inbreng **10.018.706** / reserves **123.944**); schulden **1.398.099** DROP vs 1.876.617 (LT overige **587.000**; ST **758.684** waarvan overige **733.127**; verbonden **645.447**); omzet **0** / pers **0** / VTE **0**; diensten **46.218**; expl **−50.400**; fin opbr **683.109** JUMP vs 581.817; fin kosten **25.276**; belasting **107.135**; PnL **+500.298** (was +419.113; RvB 500.298,32); dividend B **408.870** (4,50%; A/C verzaken) + andere **15.201** + reserve **76.227**. 1.232 B-cooperanten **9.578.301** / 199.297 aandelen (Cat A Nuhma 4.380 + Nubema 20 + Nuhmeris 5; Cat C EFIN 4.405; Cat B 190.487). Nubema 1359 6.5.1 still 2023 EV 8.77m / 1 Cat A 5% book 1k — **does not match** 2025 20 Cat A / EV 10.14m.
- CSVs: sources+4/entities+1/budgets+38/commitments+1/leaderboard+1 + FOI ready `gap_e50_fva_11_07m_otary_11m_div_0_41m_l5` (not sent); rq_1360=done; spawn rq_1361; ticks=1360.
- Progress@1360: refreshed progress_every_10_ticks.md + doge_waste_top10_current.md. Layers A 100 / B 100 / C ~99 / D ~74-88 (not near-complete of 348bn) / E recounted ready **{counts['foi_ready']}** (answered {counts['foi_answered']} / partial {counts['foi_partial']} / total {counts['foi_total']}). Inventory: budgets {counts['budgets']} · commitments {counts['commitments']} · leaderboard {counts['leaderboard']} · entities {counts['entities']} · sources {counts['sources']}. Pure annual waste top10 **stable** vs 1350 (GIP/fossil/cars/cheque/reporté). Dual off-top10 adds ECO2050 11.54m Otary 11.00m + leftover IGS/NV/cv stack (Nuhma cv 693.83m / NUHMA AC 630.63m / Bionerga 82.92m / IVBO 79.79m / SOLVA 64.24m / NUHMA DC 52.32m / EcoWerf 46.23m / Nubema 188.5k).
- Coverage: 1351–1360 is residual dual L5 leftover IGS/NV/cv (**SOLVA** · **IVBO** · **Limburg.net** · **Bionerga** · **NUHMA AC** · **Nuhma cv** · **EcoWerf** · **NUHMA DC** · **Nubema** · **ECO2050**). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE.
- Next: rq_1361 residual dual L5 VL JR2025 hole_fill (prefer leftover Nuhmeris NV KBO 0560.976.140 CDN 2026-00124698 if still live; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1360 write done")


if __name__ == "__main__":
    main()

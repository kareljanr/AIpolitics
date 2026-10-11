# -*- coding: utf-8 -*-
"""Tick 1370 — every-10 progress FIRST, then leftover Haviland JR2025 official NBB WVV euros.
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

TICK = "1370"
UTC = "2026-08-19T01:15:00Z"
ENT = "igs_havi"
HIER = "Vlaanderen>VlaamsBrabant>IGS>Haviland>HalleVilvoorde"
GAP = "gap_havi_othops_6_70m_patrim_7_05m_pens_21_16m_l5"
SRC = "src_havi_jr2025_nbb"
SRC2 = "src_havi_site"
SRC3 = "src_kbo_havi_0200881951"
SRC4 = "src_havi_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00188817.pdf"
SRC2_URL = "https://www.haviland.be/nl/over-haviland"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0200881951"
SRC4_URL = "https://www.haviland.be/nl/contact"
FOI_EMAIL = "info@haviland.be"
FOI_POSTAL = "Poverstraat 75 bus 47 1731 Asse"
DRAFT = "docs/doge/foi/drafts/gap_havi_othops_6_70m_patrim_7_05m_pens_21_16m_l5.md"
COMM = "comm_havi_jr2025_pnl"
LB = "lb_havi_othops_6_70m_patrim_7_05m_pens_21_16m"


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
    marker = "## Snapshot at **tick 1360** (2026-08-19)"
    if marker not in text:
        raise SystemExit("progress file missing tick 1360 marker")
    snap = f"""## Snapshot at **tick 1370** (2026-08-19)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1361-1370 leftover IGS/NV/cv: **Nuhmeris** · **s-Lim CV** · **MyCSN** · **Herkenrode RE** · **s-Lim DV** · **Interleuven** · **Leiedal** · **IOK** · **IMOG** · **Haviland** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1361-1370 is VL residual dual L5 leftover IGS/NV/cv (not near-complete of 348bn):** **IOK** assets **163.27m** othops **18.03m** inv **62.18m** invest **52.87m** · **Leiedal** assets **125.58m** omzet **10.37m** PnL **−4.93m** inv **106.16m** · **Interleuven** assets **95.25m** omzet **11.68m** inv **36.05m** · **IMOG** assets **71.87m** omzet **50.30m** diensten **34.11m** · **Haviland** assets **43.67m** othops **6.70m** patrim **7.05m** pens **21.16m** invest **19.24m** · **Herkenrode RE** assets **27.58m** · **Nuhmeris** assets **19.35m** · **s-Lim DV** assets **12.51m** · **MyCSN** assets **4.36m** · **s-Lim CV** assets **4.28m** · prior leftover IGS/NV/cv ECO2050/Nuhma/Bionerga/IVBO/SOLVA/EcoWerf stack retained |
| **E. FOI-ready gaps** | **~{counts['foi_ready']}** drafts ready | Human send only; answered **~{counts['foi_answered']}**; partial **~{counts['foi_partial']}**; total FOI rows **~{counts['foi_total']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual debt/AFM NEG + leasing/city-loan/erfpacht/DBFM/portfolio/waste-water-streek/klimaat-holding shells** (**NEW Haviland** assets **EUR43.67m** othops **EUR6.70m** patrim **EUR7.05m** pens **EUR21.16m** invest **EUR19.24m** · **IMOG** assets **EUR71.87m** omzet **EUR50.30m** diensten **EUR34.11m** · **IOK** assets **EUR163.27m** othops **EUR18.03m** inv **EUR62.18m** invest **EUR52.87m** · **Leiedal** assets **EUR125.58m** omzet **EUR10.37m** PnL **−EUR4.93m** inv **EUR106.16m** · **Interleuven** assets **EUR95.25m** omzet **EUR11.68m** inv **EUR36.05m** · **Herkenrode RE** assets **EUR27.58m** · **Nuhmeris** assets **EUR19.35m** · **s-Lim DV** assets **EUR12.51m** · **MyCSN** assets **EUR4.36m** · **s-Lim CV** assets **EUR4.28m** · prior **ECO2050** assets **EUR11.54m** FVA **EUR11.07m** Otary **EUR11.00m** Sunfin **EUR70k** div **EUR0.41m** · **Nuhma cv** assets **EUR693.83m** PnL **+EUR26.27m** div **EUR33.50m** · **NUHMA AC** assets **EUR630.63m** PnL **+EUR8.77m** · **Bionerga** assets **EUR82.92m** PnL **−EUR33.80m** · **IVBO** assets **EUR79.79m** omzet **EUR55.56m** · **SOLVA** assets **EUR64.24m** omzet **EUR25.52m** · **NUHMA DC** assets **EUR52.32m** PnL **−EUR1.21m** debt **EUR20.51m** · **EcoWerf** assets **EUR46.23m** omzet **EUR53.57m** · **Nubema** assets **EUR188.5k** uncalled **EUR375k** · leftover IGS Limburg.net glossy · prior **Interwaas** assets **EUR78.37m** cash **EUR1.44m DROP 12.70m** beleggingen **EUR30.48m** omzet **EUR2.91m** · **WVI** assets **EUR241.0m** stock **EUR181.88m** · **IGEAN DV** assets **EUR103.92m** inv **EUR68.19m** · **Aquaduin** assets **EUR99.09m** omzet **EUR26.50m** sanering **EUR31.33m** · **Creat** omzet **EUR89.38m** · leftover IGS IVM/ILvA/IVVO/IDM/IVIO · prior **EVA LSM** assets **EUR85.85m** cash **EUR3.39m DROP 10.74m** portfolio **EUR58.31m** PnL **+EUR1.5k** · **WV Zorgband** assets **EUR61.86m** PnL **−EUR5.83m** lease **EUR43.75m** · **WV Zorgbedrijf Brasschaat** assets **EUR28.94m** cash **EUR2.65m** BBR **−EUR5.39m** LT-recv **EUR17.90m** · leftover zorg live BBC Het Dak / OPcura / BVK / Weldenderend · leftover FOI Vormingscentrum Malle / Inagro / Sleutelzorg · prior **APB Hooibeekhoeve** assets **EUR5.93m** cash **EUR2.65m** ST recv **EUR2.82m** BBR **+EUR1.30m** · **EVA Pluimveehouderij** assets **EUR8.63m** cash **EUR4.08m** ST recv **EUR4.46m** BBR **+EUR1.17m** · **APB Vonk** assets **EUR1.02m** cash **EUR0.96m** BBR **+EUR0.16m** · leftover FOI (Blankenberge / Campus Vesta / Monumentenwacht / Vlabinvest / Zilvermeer / Zorg HH / **EVA Kinderopvang Dilbeek**) · prior **APB KampC** assets **EUR5.93m** cash **EUR2.65m** ST recv **EUR3.06m** BBR **+EUR2.39m** J5/T2 werksub gap **EUR1.25m** · **APB PSES** assets **EUR186.52m** ST recv **EUR165.31m** BBR **−EUR1.29m** · **APB GKC** assets **EUR2.67m** cash **EUR2.11m** · **APB Havencentrum** assets **EUR0.97m** Havenwereld **EUR0.40m** · **AGBIM** CCAO **EUR8.91m** · **AGB Maaseik** fin debt **EUR1.60m** AFM **−EUR0.67m** · prior **APB VERA** fin debt **EUR1.72m** equity **−EUR1.64m** straight loan **EUR1.10m** · **Edegem** fin debt **EUR14.05m** pension **EUR23.40m** · **Beerse city** fin debt **EUR13.82m** · **AGB Beerse** fin debt **EUR5.02m** · **Pepingen city** fin debt **EUR3.47m** · **Vleteren** fin debt **EUR3.32m** · prior **Stad+OCMW Kortenaken** fin debt **EUR10.57m** IGS EV-reval **EUR8.90m** OCMW equity **−EUR5.41m** · **Heusden-Zolder** fin debt **EUR37.85m** IGS reval **EUR31.12m** · **Kapelle-op-den-Bos** fin debt **EUR18.87m** · **Oud-Heverlee** fin debt **EUR15.18m** · **Diepenbeek city** fin debt **EUR13.59m** IGS reval **EUR19.43m** · **Huldenberg** fin debt **EUR9.56m** · **AGB Kortenaken** fin debt **EUR3.28m** leasing **EUR3.22m** · **Voeren** fin debt **EUR3.37m** · **AGB Diepenbeek** fin debt **EUR3.03m** · **Steenokkerzeel** fin debt **EUR2.49m** · prior **Stad+OCMW Bekkevoort** fin debt **EUR9.77m** IGS EV-reval **EUR5.90m** · **HH city** fin debt **EUR17.37m** · **AGB Masterplan HH** fin debt **EUR27.81m** · **AGB Sport HH** fin debt **EUR10.72m** · **AGB SCO Ronse** fin debt **EUR22.65m** · **Ronse city** fin debt **EUR25.02m** pension **EUR19.50m** · **Kraainem** fin debt **EUR6.40m** · **Tielt-Winge** fin debt **EUR8.52m** · prior **Stad+OCMW Tienen** fin debt **EUR59.73m** pension **EUR51.29m** · **Machelen** fin debt **EUR26.37m** Farys lease **EUR16.90m** · **AGB Tienen** fin debt **EUR16.93m** · **AG Museum Leuven** fin debt **EUR14.51m** · **Gingelom** Fluvius reval **EUR9.75m** fin debt **EUR3.86m** · prior **AGB MAC** fin debt **EUR40.3m** leasing **EUR40.8m** · **Mintus** dual **EUR26.36m** · Digipolis assets **EUR73.61m** · **AG Vespa** fin debt **EUR179.6m** DBFM **EUR109.4m** · **sogent** AFM **−EUR3.90m** debt **EUR96.3m** · AG-O cum loss **−EUR29.2m** · Zorgbedrijf Antwerpen AFM **−EUR18.87m** debt **EUR220m** / Dodoens equity **−EUR18.88m** / Hasselt ~EUR95–103m stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market.

### Inventory (tick 1370)

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
| research_queue open | rq_116 deferred + rq_1371 hole-fill after progress |

### What improved since tick 1360

- **VL residual dual JR2025 leftover IGS/NV/cv (tick1361-1369):** **IOK** assets **163.27m** othops **18.03m** inv **62.18m** invest **52.87m** · **Leiedal** assets **125.58m** omzet **10.37m** PnL **−4.93m** inv **106.16m** · **Interleuven** assets **95.25m** omzet **11.68m** inv **36.05m** · **IMOG** assets **71.87m** omzet **50.30m** diensten **34.11m** · **Herkenrode RE** assets **27.58m** · **Nuhmeris** assets **19.35m** · **s-Lim DV** assets **12.51m** · **MyCSN** assets **4.36m** · **s-Lim CV** assets **4.28m** — no invented euros.
- **NEW (tick1370):** **Haviland** (KBO 0200.881.951) leftover dienstverlenende vereniging / IGS streek of Halle-Vilvoorde municipalities. Official NBB WVV VOL-inb deposit **2026-00188817** PDF (1.73MB / 57p; AV 17.06.2026; neerlegging 18.06.2026). Assets **43.673.416** · othops **6.697.253** (740 empty) · patrim **7.054.833** · pens **21.157.533** vs actuarieel **28.107.281** · invest **19.241.015** · PnL **+4.394.148**. FOI ready. Every-10 progress refresh from on-disk CSVs.
- **Dual map themes:** **leftover IGS streek + waste + RE inventory + pension-provision shells** (Haviland 43.67m / IMOG 71.87m / IOK 163.27m / Leiedal 125.58m / Interleuven 95.25m) · leftover klimaat/smart-city NV/cv (Nuhmeris 19.35m / Herkenrode 27.58m / s-Lim) · prior leftover IGS/NV/cv ECO2050/Nuhma/Bionerga/IVBO/SOLVA/EcoWerf stack retained.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10.

---
"""
    text = text.replace(marker, snap + marker, 1)
    prog.write_text(text, encoding="utf-8")
    print("progress_every_10_ticks.md inserted tick 1370 snapshot")


def write_waste_top10(counts: dict) -> None:
    p = DATA / "doge_waste_top10_current.md"
    text = p.read_text(encoding="utf-8")
    text = text.replace(
        "**As-of:** tick **1360** (2026-08-19) · **7163** leaderboard rows",
        f"**As-of:** tick **1370** (2026-08-19) · **{counts['leaderboard']}** leaderboard rows",
        1,
    )
    old_dual = "(**NEW ECO2050** assets **€11.54m** FVA **€11.07m** Otary **€11.00m** Sunfin **€70k** div **€0.41m**"
    new_dual = (
        "(**NEW Haviland** assets **€43.67m** othops **€6.70m** patrim **€7.05m** pens **€21.16m** invest **€19.24m** · "
        "**IMOG** assets **€71.87m** omzet **€50.30m** diensten **€34.11m** · "
        "**IOK** assets **€163.27m** othops **€18.03m** inv **€62.18m** invest **€52.87m** · "
        "**Leiedal** assets **€125.58m** omzet **€10.37m** PnL **−€4.93m** inv **€106.16m** · "
        "**Interleuven** assets **€95.25m** omzet **€11.68m** inv **€36.05m** · "
        "**Herkenrode RE** assets **€27.58m** · **Nuhmeris** assets **€19.35m** · "
        "**s-Lim DV** assets **€12.51m** · **MyCSN** assets **€4.36m** · **s-Lim CV** assets **€4.28m** · "
        "prior **ECO2050** assets **€11.54m** FVA **€11.07m** Otary **€11.00m** Sunfin **€70k** div **€0.41m**"
    )
    if old_dual not in text:
        raise SystemExit("waste top10 missing ECO2050 dual marker")
    text = text.replace(old_dual, new_dual, 1)
    old_chg = (
        "**Change vs tick 1350:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
        "**Major NEW residual 1351–1360 (off pure top10 / dual):**"
    )
    new_chg = (
        "**Change vs tick 1360:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
        "**Major NEW residual 1361–1370 (off pure top10 / dual):** **Haviland** assets **EUR43.67m** othops **EUR6.70m** patrim **EUR7.05m** pens **EUR21.16m** invest **EUR19.24m** · **IMOG** assets **EUR71.87m** omzet **EUR50.30m** diensten **EUR34.11m** · **IOK** assets **EUR163.27m** othops **EUR18.03m** inv **EUR62.18m** invest **EUR52.87m** · **Leiedal** assets **EUR125.58m** omzet **EUR10.37m** PnL **−EUR4.93m** inv **EUR106.16m** · **Interleuven** assets **EUR95.25m** omzet **EUR11.68m** inv **EUR36.05m** · **Herkenrode RE** assets **EUR27.58m** · **Nuhmeris** assets **EUR19.35m** · **s-Lim DV** assets **EUR12.51m** · **MyCSN** assets **EUR4.36m** · **s-Lim CV** assets **EUR4.28m**. "
        "Gain is **leftover IGS streek/waste + RE inventory + pension-provision + leftover klimaat/smart-city NV/cv**. "
        "**Prior 1351–1360 retained:**"
    )
    if old_chg not in text:
        raise SystemExit("waste top10 missing change-vs-1350 marker")
    text = text.replace(old_chg, new_chg, 1)
    old_out = "| — | `lb_e50_fva_11_07m_otary_11m_div_0_41m` | **11.54 m stock** | **~6.3 dual** | **NEW 1360** ECO2050 FVA 11.07m / Otary 11.00m / div 0.41m |"
    new_out = (
        "| — | `lb_havi_othops_6_70m_patrim_7_05m_pens_21_16m` | **43.67 m stock** | **~6.3 dual** | **NEW 1370** Haviland othops 6.70m / patrim 7.05m / pens 21.16m / invest 19.24m |\n"
        "| — | `lb_imog_omzet_50_30m_diensten_34_11m_vooruit_6_60m` | **71.87 m stock** | **~6.9 dual** | 1369 IMOG leftover IGS omzet 50.30m / diensten 34.11m / vooruit 6.60m |\n"
        "| — | `lb_iokd_othops_18_03m_inv_62_18m_invest_52_87m` | **163.27 m stock** | **~7.0 dual** | 1368 IOK leftover IGS othops 18.03m / inv 62.18m / invest 52.87m |\n"
        "| — | `lb_leid_omzet_10_37m_inv_106_16m_debt` | **125.58 m stock** | **~7.1 dual** | 1367 Leiedal leftover IGS omzet 10.37m / inv 106.16m / PnL −4.93m |\n"
        "| — | `lb_ileu_omzet_11_68m_inv_36_05m_stbank` | **95.25 m stock** | **~6.8 dual** | 1366 Interleuven leftover IGS omzet 11.68m / inv 36.05m |\n"
        + old_out.replace("**NEW 1360**", "1360")
    )
    if old_out not in text:
        raise SystemExit("waste top10 missing e50 just-outside row")
    text = text.replace(old_out, new_out, 1)
    old_abs = "| `lb_e50_fva_11_07m_otary_11m_div_0_41m` | **7.2** | **NEW 1360** ECO2050 assets 11.54m / FVA 11.07m Otary 11.00m / 0-VTE citizen coop |"
    new_abs = (
        "| `lb_havi_othops_6_70m_patrim_7_05m_pens_21_16m` | **7.1** | **NEW 1370** Haviland assets 43.67m / othops 6.70m unnamed / pens 21.16m vs actuarieel 28.11m |\n"
        "| `lb_imog_omzet_50_30m_diensten_34_11m_vooruit_6_60m` | **7.3** | 1369 IMOG leftover IGS assets 71.87m / diensten 34.11m / vooruit 6.60m |\n"
        "| `lb_iokd_othops_18_03m_inv_62_18m_invest_52_87m` | **7.0** | 1368 IOK leftover IGS assets 163.27m / othops 18.03m / invest 52.87m |\n"
        "| `lb_leid_omzet_10_37m_inv_106_16m_debt` | **7.1** | 1367 Leiedal leftover IGS assets 125.58m / inv 106.16m / PnL −4.93m |\n"
        + old_abs.replace("**NEW 1360**", "1360")
    )
    if old_abs not in text:
        raise SystemExit("waste top10 missing e50 absurdity row")
    text = text.replace(old_abs, new_abs, 1)
    p.write_text(text, encoding="utf-8")
    print("doge_waste_top10_current.md updated tick 1370; pure top10 unchanged")


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "Haviland jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00188817; AV 17.06.2026)",
                "url": SRC_URL,
                "publisher": "Haviland / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1370; official NBB VOL-inb PDF 1.73MB 57p deposit 2026-00188817 created 23.06.2026 neerlegging 18.06.2026; "
                    "leftover IGS DV of Halle-Vilvoorde municipalities; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Callens Vandelanotte NV B00083 / Dries Oosterlinck A02640 12500 oordeel zonder voorbehoud; "
                    "6.1/6.4.1/6.5.1/6.17/6.18/6.20 not filed; 740 empty; every-10"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Haviland official site (streekintercommunale Halle-Vilvoorde / Haviland Regiopartners)",
                "url": SRC2_URL,
                "publisher": "Haviland Intercommunale",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1370; leftover IGS streek of Halle-Vilvoorde; "
                    "haviland.be has jaarverslag 2024 only (no statutory JR2025); statutory 2025 balans is the NBB CDN deposit"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Haviland 0200.881.951",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1370; KBO 0200.881.951 Actief / normale toestand since 01.01.1968; "
                    "statutaire naam Intercommunale Maatschappij voor de Ruimtelijke Ordening en de Economisch- Sociale Expansie van het Arrondissement Halle-Vilvoorde since 24.06.1972; "
                    "afkorting HAVILAND since 24.06.1972; Dienstverlenende vereniging (Vlaams Gewest) since 21.01.2004; "
                    "zetel Poverstraat 75 bus 47 1731 Asse since 10.12.2025; 1 VE; "
                    "btw since 01.01.1971; RSZ since 01.01.2022; aanbestedende overheid since 01.01.1968; "
                    "jaarvergadering mei; boekjaar 31 december; "
                    "15 KBO-bestuurders; voorzitter Walter De Donder; "
                    "no KBO email/web/tel; NACE 68.121/84.119/37.000"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Haviland FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "Haviland",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1370; FOI info@haviland.be / 02 466 51 00; "
                    "Poverstraat 75 bus 47 1731 Asse (PIVO-site; post since 01.12.2025); no own KBO email/web/tel"
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
                "name_nl": "Haviland Intercommunale (leftover dienstverlenende vereniging / IGS streek Halle-Vilvoorde / Haviland Regiopartners)",
                "name_fr": "Haviland Intercommunale (association de services residuelle / IGS regionale Halle-Vilvoorde)",
                "name_en": "Haviland leftover Halle-Vilvoorde regional IGS (service association)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.haviland.be/nl",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1370 leftover residual IGS DV of Halle-Vilvoorde municipalities; "
                    "KBO 0200.881.951 Actief since 01.01.1968; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 43673416 othops 6697253 patrim 7054833 pens 21157533 pnl 4394148; "
                    "FOI ready othops 6.70m/patrim 7.05m/pens 21.16m"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_havi_assets_2025", ENT, "2025", "43673416", "2025 assets 43673416 VOL-inb 20/58; tick1370; primary official NBB WVV; commissaris 43673416.31"),
        ("bud_havi_assets_2024", ENT, "2024", "38902577", "2024 assets 38902577 comparative; tick1370; primary official NBB WVV 20/58"),
        ("bud_havi_fixed_2025", ENT, "2025", "5147140", "2025 vaste activa 5147140 JUMP vs 2559007; tick1370; primary official NBB WVV 21/28"),
        ("bud_havi_iva_2025", ENT, "2025", "32797", "2025 immateriele VA 32797 vs 60301; tick1370; primary official NBB WVV 21"),
        ("bud_havi_mva_2025", ENT, "2025", "5111241", "2025 MVA 5111241 JUMP vs 2494756; tick1370; primary official NBB WVV 22/27"),
        ("bud_havi_buildings_2025", ENT, "2025", "288732", "2025 terreinen en gebouwen 288732 DROP vs 837434 after uitboek aanschaf 2822022; tick1370; primary official NBB WVV 22"),
        ("bud_havi_bldg_disp_2025", ENT, "2025", "2822022", "2025 overdracht terreinen/gebouwen aanschaf 2822022 (oude HQ Zellik); tick1370; primary official NBB WVV 6.3.1 8171"),
        ("bud_havi_machines_2025", ENT, "2025", "128018", "2025 installaties/machines 128018 vs 40303; tick1370; primary official NBB WVV 23"),
        ("bud_havi_rollend_2025", ENT, "2025", "109477", "2025 meubilair/rollend 109477; tick1370; primary official NBB WVV 24"),
        ("bud_havi_othmva_2025", ENT, "2025", "821992", "2025 overige MVA 821992; tick1370; primary official NBB WVV 26"),
        ("bud_havi_cip_2025", ENT, "2025", "3763021", "2025 activa in aanbouw 3763021 JUMP vs 793805 (nieuw HQ); tick1370; primary official NBB WVV 27"),
        ("bud_havi_cip_acq_2025", ENT, "2025", "2969216", "2025 aanschaf CIP 2969216 nieuw administratief gebouw; tick1370; primary official NBB WVV 6.3.6 8166"),
        ("bud_havi_fva_2025", ENT, "2025", "3102", "2025 FVA 3102 (aandelen 1204 + borg 1898; 6.4.1/6.5.1 not filed); tick1370; primary official NBB WVV 28"),
        ("bud_havi_current_2025", ENT, "2025", "38526276", "2025 vlottende activa 38526276 vs 36343570; tick1370; primary official NBB WVV 29/58"),
        ("bud_havi_inv_2025", ENT, "2025", "14848132", "2025 voorraden+BIE 14848132 (RE 14788132 + BIE 60000); tick1370; primary official NBB WVV 3"),
        ("bud_havi_re_2025", ENT, "2025", "14788132", "2025 onroerende goederen bestemd voor verkoop 14788132 DROP vs 19071289; tick1370; primary official NBB WVV 35"),
        ("bud_havi_re_2024", ENT, "2024", "19071289", "2024 RE inventory 19071289 comparative; tick1370; primary official NBB WVV 35"),
        ("bud_havi_strecv_2025", ENT, "2025", "3312978", "2025 ST vorderingen 3312978 (trade 2869529 + other 443450); tick1370; primary official NBB WVV 40/41"),
        ("bud_havi_invest_2025", ENT, "2025", "19241015", "2025 geldbeleggingen 19241015 JUMP vs 11165922; tick1370; primary official NBB WVV 50/53"),
        ("bud_havi_invest_2024", ENT, "2024", "11165922", "2024 geldbeleggingen 11165922 comparative; tick1370; primary official NBB WVV 50/53"),
        ("bud_havi_term_2025", ENT, "2025", "18241015", "2025 termijnrekeningen 18241015 (1m 13241015 + 1-12m 1000000 + >1y 4000000); tick1370; primary official NBB WVV 6.6 53"),
        ("bud_havi_fixedinc_2025", ENT, "2025", "1000000", "2025 vastrentende effecten 1000000; tick1370; primary official NBB WVV 6.6 52"),
        ("bud_havi_cash_2025", ENT, "2025", "895835", "2025 liquide middelen 895835 DROP vs 1064514; tick1370; primary official NBB WVV 54/58"),
        ("bud_havi_cash_2024", ENT, "2024", "1064514", "2024 cash 1064514 comparative; tick1370; primary official NBB WVV 54/58"),
        ("bud_havi_prepaid_2025", ENT, "2025", "228316", "2025 overlopend actief 228316 (kosten 198587 + opbr 29729); tick1370; primary official NBB WVV 490/1"),
        ("bud_havi_equity_2025", ENT, "2025", "11695045", "2025 eigen vermogen 11695045 vs 7441607; tick1370; primary official NBB WVV 10/15"),
        ("bud_havi_inbreng_2025", ENT, "2025", "217569", "2025 inbreng onbeschikbaar 217569 / 34670 aandelen; niet volgestort 649206 of 866750; tick1370; primary official NBB WVV 10/11"),
        ("bud_havi_uncalled_2025", ENT, "2025", "649206", "2025 niet volgestort 649206 of in geld 866750; tick1370; primary official NBB WVV 6.7.1 87901"),
        ("bud_havi_reserves_2025", ENT, "2025", "11477476", "2025 reserves 11477476 (beschikbaar 11387916 + statutair 89560); tick1370; primary official NBB WVV 13"),
        ("bud_havi_capsub_2025", ENT, "2025", "0", "2025 kapitaalsubsidies 0 DROP vs 133336 (genomen in resultaat 133336); tick1370; primary official NBB WVV 15"),
        ("bud_havi_prov_2025", ENT, "2025", "21685085", "2025 voorzieningen 21685085 vs 22330388; tick1370; primary official NBB WVV 16"),
        ("bud_havi_pension_2025", ENT, "2025", "21157533", "2025 pensioenen 21157533 vs 21789887; tick1370; primary official NBB WVV 160"),
        ("bud_havi_pens_saldo_2025", ENT, "2025", "20963711", "2025 responsabilisering saldo 20963711 after aanwending 615758 tot 2048; tick1370; primary official jaarverslag"),
        ("bud_havi_pens_used_2025", ENT, "2025", "615758", "2025 responsabiliseringsbijdrage aangewend 615758.44; tick1370; primary official NBB WVV 624 + jaarverslag"),
        ("bud_havi_actuarial_2025", ENT, "2025", "28107281", "2025 actuarieel 40y 28107281.33 (niet geboekt; voorziening niet verhoogd); tick1370; primary official jaarverslag 23.03.2026"),
        ("bud_havi_othprov_2025", ENT, "2025", "527552", "2025 overige risico's 527552 (geschillen 450132 + algemeen 77420); tick1370; primary official NBB WVV 164/5 6.8"),
        ("bud_havi_koster_2025", ENT, "2025", "439924", "2025 De Kosterlaan/EGTA 439923.56 binnen geschillen 450132; tick1370; primary official jaarverslag"),
        ("bud_havi_debt_2025", ENT, "2025", "10293286", "2025 schulden 10293286 vs 9130582; tick1370; primary official NBB WVV 17/49"),
        ("bud_havi_lt_2025", ENT, "2025", "5332445", "2025 LT schulden bank 5332445 JUMP vs 654335 (nieuw HQ-krediet); tick1370; primary official NBB WVV 17/173"),
        ("bud_havi_lt_2024", ENT, "2024", "654335", "2024 LT bank 654335 comparative; tick1370; primary official NBB WVV 173"),
        ("bud_havi_st_2025", ENT, "2025", "4566425", "2025 ST schulden 4566425 DROP vs 8069271; tick1370; primary official NBB WVV 42/48"),
        ("bud_havi_sttrade_2025", ENT, "2025", "2582055", "2025 leveranciers 2582055 DROP vs 6448116 (GAS-ristorno); tick1370; primary official NBB WVV 440/4"),
        ("bud_havi_govg_2025", ENT, "2025", "5654335", "2025 door Belgische overheden gewaarborgde schulden 5654335; tick1370; primary official NBB WVV 6.9 9061"),
        ("bud_havi_bankw_2025", ENT, "2025", "437870", "2025 buitenbalans bankgaranties Belfius 437870; tick1370; primary official NBB WVV 6.14"),
        ("bud_havi_accrued_2025", ENT, "2025", "394416", "2025 overlopend passief 394416 (subsidies 278242 + overige 116175); tick1370; primary official NBB WVV 492/3"),
        ("bud_havi_ops_2025", ENT, "2025", "16946193", "2025 bedrijfsopbrengsten 16946193; tick1370; primary official NBB WVV 70/76A"),
        ("bud_havi_omzet_2025", ENT, "2025", "14526833", "2025 omzet 14526833; 6.10 dienstverlening 7472000 + patrimonium 7054833; tick1370; primary official NBB WVV 70"),
        ("bud_havi_omzet_2024", ENT, "2024", "7167351", "2024 omzet 7167351 comparative; tick1370; primary official NBB WVV 70"),
        ("bud_havi_dienst_2025", ENT, "2025", "7472000", "2025 omzet dienstverlening 7472000 vs 7041602; tick1370; primary official NBB WVV 6.10"),
        ("bud_havi_patrim_2025", ENT, "2025", "7054833", "2025 omzet patrimonium 7054833 JUMP vs 125749 (twee projectgronden); tick1370; primary official NBB WVV 6.10"),
        ("bud_havi_invchg_2025", ENT, "2025", "-4283157", "2025 voorraadwijziging -4283157 (verkochte projectgronden); tick1370; primary official NBB WVV 71"),
        ("bud_havi_othops_2025", ENT, "2025", "6697253", "2025 andere bedrijfsopbrengsten 6697253 JUMP vs 1170397; 740 empty; tick1370; primary official NBB WVV 74"),
        ("bud_havi_othops_2024", ENT, "2024", "1170397", "2024 andere bedrijfsopbrengsten 1170397 comparative; tick1370; primary official NBB WVV 74"),
        ("bud_havi_goods_2025", ENT, "2025", "449065", "2025 handelsgoederen/grond-hulp 449065; tick1370; primary official NBB WVV 60"),
        ("bud_havi_diensten_2025", ENT, "2025", "4726890", "2025 diensten 4726890 JUMP vs 2611897; tick1370; primary official NBB WVV 61"),
        ("bud_havi_diensten_2024", ENT, "2024", "2611897", "2024 diensten 2611897 comparative; tick1370; primary official NBB WVV 61"),
        ("bud_havi_pers_2025", ENT, "2025", "7921394", "2025 bezoldigingen 7921394 / 69.3 VTE / 73 koppen; tick1370; primary official NBB WVV 62 9087"),
        ("bud_havi_uitzend_2025", ENT, "2025", "64015", "2025 uitzend 64015 / 1 VTE; tick1370; primary official NBB WVV 617 9097"),
        ("bud_havi_deprec_2025", ENT, "2025", "84307", "2025 afschrijvingen 84307; tick1370; primary official NBB WVV 630"),
        ("bud_havi_expl_2025", ENT, "2025", "4215007", "2025 bedrijfswinst 4215007 vs -2091463; tick1370; primary official NBB WVV 9901"),
        ("bud_havi_expl_2024", ENT, "2024", "-2091463", "2024 bedrijfsverlies 2091463 comparative; tick1370; primary official NBB WVV 9901"),
        ("bud_havi_fininc_2025", ENT, "2025", "258706", "2025 financiele opbrengsten 258706 (vlottende 125100 + andere 133606 waarvan capsub 133336); tick1370; primary official NBB WVV 75"),
        ("bud_havi_fincost_2025", ENT, "2025", "75005", "2025 financiele kosten 75005 (schulden 66813); tick1370; primary official NBB WVV 65"),
        ("bud_havi_pnl_2025", ENT, "2025", "4394148", "2025 PnL 9904 4394148 vs -1843055; added to reserves; tick1370; primary official NBB WVV; commissaris 4394148.48"),
        ("bud_havi_pnl_2024", ENT, "2024", "-1843055", "2024 PnL -1843055 comparative; tick1370; primary official NBB WVV 9904"),
        ("bud_havi_comm_2025", ENT, "2025", "12500", "2025 commissaris Callens Vandelanotte Oosterlinck 12500; tick1370; primary official NBB WVV 9505"),
        ("bud_havi_board_2025", ENT, "2025", "62490", "2025 bestuurders 9503 62490; tick1370; primary official NBB WVV 9503"),
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
                "title": "Haviland JR2025 leftover IGS dual (assets 43.67m / othops 6.70m / patrim 7.05m / pens 21.16m / invest 19.24m)",
                "entity_id": ENT,
                "beneficiary": "Haviland / Halle-Vilvoorde municipalities / statutaire gepensioneerden",
                "legal_basis": "WVV DV; decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-06-17",
                "start_year": "1968",
                "end_year": "2026",
                "total_envelope_eur": "43673416",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL streek — 6.70m othops / 7.05m patrim / 21.16m pens vs actuarieel 28.11m",
                "cut_option": "Publish 6.70m othops counterparties + 7.05m patrim plot list + actuarieel 28.11m vs 21.16m + 19.24m termijn + site-JR; do not keep 43.67m municipal streek IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1370; assets 43673416 othops 6697253 patrim 7054833 pens 21157533 pnl 4394148; FOI ready not sent; every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Haviland JR2025 leftover IGS: assets 43.67m / othops 6.70m / patrim 7.05m / pens 21.16m / invest 19.24m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "6697253",
                "total_cost_eur": "43673416",
                "tco_notes": (
                    "Leftover dual IGS DV of Halle-Vilvoorde municipalities: "
                    "assets 43.67m / equity 11.70m / pnl +4.39m / omzet 14.53m / 69.3 VTE / "
                    "othops 6.70m (740 empty) / patrim 7.05m (two plots) / "
                    "pens 21.16m vs actuarieel 28.11m (not topped up) / invest 19.24m / "
                    "official NBB WVV live; "
                    "do not treat 43.67m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Haviland / Halle-Vilvoorde municipalities",
                "stated_goal": "Local leftover IGS map VL streek — JR2025 live; dual othops/patrim/pens FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 43.67m / othops 6.70m / patrim 7.05m / pens 21.16m / pnl +4.39m; invest 19.24m JUMP",
                "absurdity_score": "7.1",
                "cost_score": "5.5",
                "difficulty": "2.5",
                "priority_index": "6.3",
                "cut_proposal": "Publish 6.70m othops counterparties + 7.05m patrim plot list + actuarieel 28.11m vs 21.16m + 19.24m termijn + site-JR; do not keep 43.67m municipal streek IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1370; leftover IGS DV of Halle-Vilvoorde; FOI ready not sent; not TE-additive of 348bn; every-10",
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
                    "andere bedrijfsopbrengsten 6697253 JUMP vs 1170397 (WVV 74; 740 subsidies empty) per grantor/tegenpartij "
                    "+ omzet patrimonium 7054833 JUMP vs 125749 (twee projectgronden) + resterende RE inventory 14788132 completed-contract list "
                    "+ pensioen/responsabilisering 21157533 / saldo 20963711 tot 2048 vs actuarieel 28107281 (niet verhoogd) "
                    "+ geldbeleggingen 19241015 JUMP vs 11165922 (termijn 18241015 waarvan >1y 4000000) "
                    "+ CIP nieuw HQ 3763021 / aanschaf 2969216 + LT bank 5332445 JUMP vs 654335 + 6.9 overheidsgarantie 5654335 "
                    "+ diensten 4726890 JUMP vs 2611897 top-tegenpartijen "
                    "+ De Kosterlaan/EGTA 439924 + unnamed schadeclaim zonder voorziening "
                    "+ 34670 aandelen / niet volgestort 649206 / Overijse -7350 / 8761/8762 empty "
                    "+ official-site JR2025 (site has 2024 only) "
                    "+ 6.1/6.4.1/6.5.1/6.17/6.18 not filed"
                ),
                "why_it_matters": (
                    "Leftover IGS DV of Halle-Vilvoorde municipalities "
                    "(same leftover-IGS seam as Leiedal 1367 / Interleuven 1366 / IOK 1368 / Interwaas 1350 / SOLVA 1351): "
                    "43.67m assets / 6.70m unnamed othops / 7.05m patrim / 21.16m pens vs 28.11m actuarieel / "
                    "19.24m beleggingen / 69.3 VTE / site-JR missing "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "Haviland / Walter De Donder / Stijn Quaghebeur / Halle-Vilvoorde municipalities",
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
                    "tick1370 leftover IGS DV of Halle-Vilvoorde after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (1.73MB 57p deposit 2026-00188817). "
                    "IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. "
                    "Nuhma-group seam 1353-1365 skipped. "
                    "Dommelhof leftover Limburg EVA still no 2025/2026 PDF. "
                    "Otary RS Nuhma-adjacent fallback not taken. "
                    "Veneco 2026-00188751 / IGEMO 2026-00235028 / IVOO 2026-00271895 / MIWA 2026-00209388 2025 CDN still live — leftover next. "
                    "IVAREM still 2024. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1370",
        "title": "Haviland DV JR2025 leftover dual residual + every-10 progress",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: every-10 progress refresh from on-disk CSVs + Haviland leftover IGS DV of Halle-Vilvoorde "
            "after honest hunt; KBO 0200.881.951 Actief; "
            "live JR2025 official NBB WVV VOL-inb PDF (1.73MB 57p deposit 2026-00188817; commissaris Callens Vandelanotte Oosterlinck); "
            "sourced euros assets 43673416 / othops 6697253 / patrim 7054833 / pens 21157533 / pnl 4394148; "
            "FOI ready othops 6.70m/patrim 7.05m/pens 21.16m"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T03:10:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1370 Haviland leftover IGS residual + every-10; KBO 0200.881.951; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1371 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1371",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1370 done including Haviland 1370 leftover IGS live NBB WVV + every-10 / "
            "IMOG 1369 leftover IGS live NBB WVV / "
            "IOK 1368 leftover IGS live NBB WVV / "
            "Leiedal 1367 leftover IGS live NBB WVV / "
            "Interleuven 1366 leftover IGS live NBB WVV / "
            "s-Lim DV 1365 leftover IGS live NBB WVV / "
            "Herkenrode RE NV 1364 leftover vastgoed live NBB WVV / "
            "MyCSN NV 1363 leftover smart-city live NBB WVV / "
            "s-Lim CV 1362 leftover smart-city live NBB WVV / "
            "Nuhmeris NV 1361 leftover klimaat-holding live NBB WVV / "
            "ECO2050 cv 1360 leftover klimaat-coop live NBB WVV + every-10); "
            "Veneco leftover IGS KBO 0200.065.765 — take if JR2025 CDN 2026-00188751 still live (24.1MB HEAD this tick, not taken once Haviland extracted); "
            "IGEMO KBO 0213.349.124 CDN 2026-00235028 / IVOO KBO 0214.753.050 CDN 2026-00271895 / MIWA KBO 0218.239.409 CDN 2026-00209388 — take only if still live; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if a new live 2025 WVV PDF downloads (prefer leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; Otary CDN 2026-00254280 live prior tick, not taken); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1370 after Haviland leftover IGS live NBB WVV + every-10; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1370", rq_new, rq_spawn)
    print("research_queue 1370", found, "spawned_1371", spawned)

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
                "last_unit_id": "rq_1370",
                "ticks_completed": "1370",
                "paused": "no",
                "notes": (
                    "tick1370 Haviland leftover IGS residual + every-10; KBO 0200.881.951; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 43673416 othops 6697253 patrim 7054833 pens 21157533 pnl 4394148; "
                    "FOI ready othops 6.70m/patrim 7.05m/pens 21.16m; next rq_1371 residual dual L5 VL; continuous hole_fill"
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

    print("loop_log deferred")
    print("tick1370 write done")
    # stash counts for log appender
    Path("/tmp/tick1370_counts.txt").write_text(repr(counts), encoding="utf-8")


if __name__ == "__main__":
    main()

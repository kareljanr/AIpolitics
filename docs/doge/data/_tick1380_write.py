# -*- coding: utf-8 -*-
"""Tick 1380 — every-10 progress FIRST, then leftover INCOVO JR2025 official NBB WVV euros.
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

TICK = "1380"
UTC = "2026-08-19T02:00:00Z"
ENT = "igs_inco"
HIER = "Vlaanderen>VlaamsBrabant>IGS>INCOVO"
GAP = "gap_inco_omzet_8_52m_subs_6_11m_diensten_7_54m_l5"
SRC = "src_inco_jr2025_nbb"
SRC2 = "src_inco_site"
SRC3 = "src_kbo_inco_0218993039"
SRC4 = "src_inco_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00239674.pdf"
SRC2_URL = "https://www.incovo-interza.be/nl/over-interza-en-incovo"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0218993039"
SRC4_URL = "https://www.incovo-interza.be/nl"
FOI_EMAIL = "financien@incovo-interza.be"
FOI_POSTAL = "Cyriel Buyssestraat 5 1800 Vilvoorde"
DRAFT = "docs/doge/foi/drafts/gap_inco_omzet_8_52m_subs_6_11m_diensten_7_54m_l5.md"
COMM = "comm_inco_jr2025_pnl"
LB = "lb_inco_omzet_8_52m_subs_6_11m_diensten_7_54m"


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
    marker = "## Snapshot at **tick 1370** (2026-08-19)"
    if marker not in text:
        raise SystemExit("progress file missing tick 1370 marker")
    snap = f"""## Snapshot at **tick 1380** (2026-08-19)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1371-1380 leftover IGS/EVA: **Veneco** · **IGEMO** · **IVOO** · **MIWA** · **IVAGO** · **MIROM Roeselare** · **MIROM Menen** · **De Nekker** · **ISVAG** · **INCOVO** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1371-1380 is VL residual dual L5 leftover IGS/EVA (not near-complete of 348bn):** **IVAGO** assets **78.39m** omzet **81.14m** diensten **38.04m** · **Veneco** assets **51.98m** omzet **1.18m** othops **5.27m** inv **23.12m** · **ISVAG** assets **42.72m** omzet **29.44m** diensten **14.73m** · **MIROM Roeselare** assets **37.44m** omzet **21.18m** diensten **12.64m** · **IGEMO** assets **25.44m** omzet **5.98m** othops **3.00m** inv **19.61m** · **MIWA** assets **19.60m** othops **13.95m** diensten **10.57m** · **MIROM Menen** assets **11.71m** othops **4.37m** diensten **4.77m** · **IVOO** assets **10.74m** omzet **16.55m** diensten **12.39m** · **INCOVO** assets **9.40m** omzet **8.52m** subs **6.11m** diensten **7.54m** · **De Nekker** assets **0.75m** goods+diensten **3.67m** equity **−26.2k** · prior leftover IGS/NV/cv Haviland/IMOG/IOK/Leiedal/Interleuven/Nuhma stack retained |
| **E. FOI-ready gaps** | **~{counts['foi_ready']}** drafts ready | Human send only; answered **~{counts['foi_answered']}**; partial **~{counts['foi_partial']}**; total FOI rows **~{counts['foi_total']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual debt/AFM NEG + leasing/city-loan/erfpacht/DBFM/portfolio/waste-water-streek/klimaat-holding shells** (**NEW INCOVO** assets **EUR9.40m** omzet **EUR8.52m** subs **EUR6.11m** diensten **EUR7.54m** pens **EUR2.05m** · **ISVAG** assets **EUR42.72m** omzet **EUR29.44m** diensten **EUR14.73m** · **De Nekker** assets **EUR0.75m** goods+diensten **EUR3.67m** equity **−EUR26.2k** · **MIROM Menen** assets **EUR11.71m** othops **EUR4.37m** · **MIROM Roeselare** assets **EUR37.44m** omzet **EUR21.18m** · **IVAGO** assets **EUR78.39m** omzet **EUR81.14m** · **MIWA** assets **EUR19.60m** othops **EUR13.95m** · **IVOO** assets **EUR10.74m** omzet **EUR16.55m** · **IGEMO** assets **EUR25.44m** omzet **EUR5.98m** · **Veneco** assets **EUR51.98m** othops **EUR5.27m** · prior **Haviland** assets **EUR43.67m** othops **EUR6.70m** patrim **EUR7.05m** pens **EUR21.16m** invest **EUR19.24m** · **IMOG** assets **EUR71.87m** omzet **EUR50.30m** diensten **EUR34.11m** · **IOK** assets **EUR163.27m** othops **EUR18.03m** inv **EUR62.18m** invest **EUR52.87m** · **Leiedal** assets **EUR125.58m** omzet **EUR10.37m** PnL **−EUR4.93m** inv **EUR106.16m** · **Interleuven** assets **EUR95.25m** omzet **EUR11.68m** inv **EUR36.05m** · **Herkenrode RE** assets **EUR27.58m** · **Nuhmeris** assets **EUR19.35m** · **s-Lim DV** assets **EUR12.51m** · **MyCSN** assets **EUR4.36m** · **s-Lim CV** assets **EUR4.28m** · prior leftover IGS/NV/cv ECO2050/Nuhma/Bionerga/IVBO/SOLVA/EcoWerf stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market.

### Inventory (tick 1380)

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
| research_queue open | rq_116 deferred + rq_1381 hole-fill after progress |

### What improved since tick 1370

- **VL residual dual JR2025 leftover IGS/EVA (tick1371-1379):** **IVAGO** assets **78.39m** omzet **81.14m** diensten **38.04m** · **Veneco** assets **51.98m** omzet **1.18m** othops **5.27m** inv **23.12m** · **ISVAG** assets **42.72m** omzet **29.44m** diensten **14.73m** · **MIROM Roeselare** assets **37.44m** omzet **21.18m** diensten **12.64m** · **IGEMO** assets **25.44m** omzet **5.98m** othops **3.00m** inv **19.61m** · **MIWA** assets **19.60m** othops **13.95m** diensten **10.57m** · **MIROM Menen** assets **11.71m** othops **4.37m** diensten **4.77m** · **IVOO** assets **10.74m** omzet **16.55m** diensten **12.39m** · **De Nekker** assets **0.75m** goods+diensten **3.67m** equity **−26.2k** — no invented euros.
- **NEW (tick1380):** **INCOVO** (KBO 0218.993.039) leftover opdrachthoudende vereniging / IGS waste of Londerzeel + Machelen + Meise + Vilvoorde + Zemst. Official NBB WVV VOL-inb deposit **2026-00239674** PDF (1.10MB / 54p; AV 26.06.2026; created 02.07.2026). Assets **9.396.832** · omzet **8.522.977** (6.10 empty) · exploitatiesubsidies **6.106.178** · diensten **7.543.829** · pers **5.881.619** / **86,5 VTE** · pens **2.050.799** · PnL **+18.754**. FOI ready. Every-10 progress refresh from on-disk CSVs.
- **Dual map themes:** **leftover IGS waste + streek + provincial EVA shells** (IVAGO 78.39m / Veneco 51.98m / ISVAG 42.72m / MIROM 37.44m+11.71m / INCOVO 9.40m / De Nekker 0.75m) · leftover IGS streek/RE (IGEMO 25.44m / IVOO 10.74m / MIWA 19.60m) · prior leftover IGS/NV/cv Haviland/IMOG/IOK/Leiedal/Interleuven/Nuhma stack retained.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10.

---
"""
    text = text.replace(marker, snap + marker, 1)
    prog.write_text(text, encoding="utf-8")
    print("progress_every_10_ticks.md inserted tick 1380 snapshot")


def write_waste_top10(counts: dict) -> None:
    p = DATA / "doge_waste_top10_current.md"
    text = p.read_text(encoding="utf-8")
    text = text.replace(
        "**As-of:** tick **1370** (2026-08-19) · **7173** leaderboard rows",
        f"**As-of:** tick **1380** (2026-08-19) · **{counts['leaderboard']}** leaderboard rows",
        1,
    )
    old_dual = "(**NEW Haviland** assets **€43.67m** othops **€6.70m** patrim **€7.05m** pens **€21.16m** invest **€19.24m**"
    new_dual = (
        "(**NEW INCOVO** assets **€9.40m** omzet **€8.52m** subs **€6.11m** diensten **€7.54m** pens **€2.05m** · "
        "**ISVAG** assets **€42.72m** omzet **€29.44m** diensten **€14.73m** · "
        "**De Nekker** assets **€0.75m** goods+diensten **€3.67m** equity **−€26.2k** · "
        "**MIROM Menen** assets **€11.71m** othops **€4.37m** · "
        "**MIROM Roeselare** assets **€37.44m** omzet **€21.18m** · "
        "**IVAGO** assets **€78.39m** omzet **€81.14m** diensten **€38.04m** · "
        "**MIWA** assets **€19.60m** othops **€13.95m** · "
        "**IVOO** assets **€10.74m** omzet **€16.55m** · "
        "**IGEMO** assets **€25.44m** omzet **€5.98m** · "
        "**Veneco** assets **€51.98m** othops **€5.27m** · "
        "prior **Haviland** assets **€43.67m** othops **€6.70m** patrim **€7.05m** pens **€21.16m** invest **€19.24m**"
    )
    if old_dual not in text:
        raise SystemExit("waste top10 missing Haviland dual marker")
    text = text.replace(old_dual, new_dual, 1)
    old_chg = (
        "**Change vs tick 1360:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
        "**Major NEW residual 1361–1370 (off pure top10 / dual):**"
    )
    new_chg = (
        "**Change vs tick 1370:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
        "**Major NEW residual 1371–1380 (off pure top10 / dual):** **IVAGO** assets **EUR78.39m** omzet **EUR81.14m** diensten **EUR38.04m** · **Veneco** assets **EUR51.98m** omzet **EUR1.18m** othops **EUR5.27m** inv **EUR23.12m** · **ISVAG** assets **EUR42.72m** omzet **EUR29.44m** diensten **EUR14.73m** · **MIROM Roeselare** assets **EUR37.44m** omzet **EUR21.18m** diensten **EUR12.64m** · **IGEMO** assets **EUR25.44m** omzet **EUR5.98m** othops **EUR3.00m** inv **EUR19.61m** · **MIWA** assets **EUR19.60m** othops **EUR13.95m** diensten **EUR10.57m** · **MIROM Menen** assets **EUR11.71m** othops **EUR4.37m** diensten **EUR4.77m** · **IVOO** assets **EUR10.74m** omzet **EUR16.55m** diensten **EUR12.39m** · **INCOVO** assets **EUR9.40m** omzet **EUR8.52m** subs **EUR6.11m** diensten **EUR7.54m** · **De Nekker** assets **EUR0.75m** goods+diensten **EUR3.67m** equity **−EUR26.2k**. "
        "Gain is **leftover IGS waste + streek + provincial EVA shells**. "
        "**Prior 1361–1370 retained:**"
    )
    if old_chg not in text:
        raise SystemExit("waste top10 missing change-vs-1360 marker")
    text = text.replace(old_chg, new_chg, 1)
    old_out = "| — | `lb_havi_othops_6_70m_patrim_7_05m_pens_21_16m` | **43.67 m stock** | **~6.3 dual** | **NEW 1370** Haviland othops 6.70m / patrim 7.05m / pens 21.16m / invest 19.24m |"
    new_out = (
        "| — | `lb_inco_omzet_8_52m_subs_6_11m_diensten_7_54m` | **9.40 m stock** | **~6.2 dual** | **NEW 1380** INCOVO omzet 8.52m / subs 6.11m / diensten 7.54m / pens 2.05m |\n"
        "| — | `lb_isvg_omzet_29_44m_diensten_14_73m_permit` | **42.72 m stock** | **~6.8 dual** | 1379 ISVAG leftover IGS omzet 29.44m / diensten 14.73m / permit beroep |\n"
        "| — | `lb_nekk_omzet_empty_ops_3_67m_equity_neg` | **0.75 m stock** | **~6.6 dual** | 1378 De Nekker leftover EVA goods+diensten 3.67m / equity −26.2k |\n"
        "| — | `lb_miromn_othops_4_37m_diensten_4_77m_pens` | **11.71 m stock** | **~6.6 dual** | 1377 MIROM Menen leftover IGS othops 4.37m / diensten 4.77m |\n"
        "| — | `lb_mirom_omzet_21_18m_diensten_12_64m_cip` | **37.44 m stock** | **~6.8 dual** | 1376 MIROM Roeselare leftover IGS omzet 21.18m / diensten 12.64m |\n"
        "| — | `lb_ivag_omzet_81_14m_diensten_38_04m_ecov` | **78.39 m stock** | **~7.1 dual** | 1375 IVAGO leftover IGS omzet 81.14m / diensten 38.04m |\n"
        "| — | `lb_miwa_othops_13_95m_diensten_10_57m_fire` | **19.60 m stock** | **~6.8 dual** | 1374 MIWA leftover IGS othops 13.95m / diensten 10.57m |\n"
        "| — | `lb_ivoo_omzet_16_55m_diensten_12_39m_aec` | **10.74 m stock** | **~6.8 dual** | 1373 IVOO leftover IGS omzet 16.55m / diensten 12.39m |\n"
        "| — | `lb_igem_omzet_5_98m_othops_3_00m_inv_19_61m` | **25.44 m stock** | **~6.1 dual** | 1372 IGEMO leftover IGS omzet 5.98m / othops 3.00m / inv 19.61m |\n"
        "| — | `lb_vene_omzet_1_18m_othops_5_27m_inv_23_12m` | **51.98 m stock** | **~6.3 dual** | 1371 Veneco leftover IGS omzet 1.18m / othops 5.27m / inv 23.12m |\n"
        + old_out.replace("**NEW 1370**", "1370")
    )
    if old_out not in text:
        raise SystemExit("waste top10 missing havi just-outside row")
    text = text.replace(old_out, new_out, 1)
    old_abs = "| `lb_havi_othops_6_70m_patrim_7_05m_pens_21_16m` | **7.1** | **NEW 1370** Haviland assets 43.67m / othops 6.70m unnamed / pens 21.16m vs actuarieel 28.11m |"
    new_abs = (
        "| `lb_inco_omzet_8_52m_subs_6_11m_diensten_7_54m` | **7.0** | **NEW 1380** INCOVO assets 9.40m / omzet 8.52m 6.10 empty / subs 6.11m / diensten 7.54m / pens 2.05m |\n"
        "| `lb_isvg_omzet_29_44m_diensten_14_73m_permit` | **7.3** | 1379 ISVAG leftover IGS assets 42.72m / diensten 14.73m / permit beroep |\n"
        "| `lb_nekk_omzet_empty_ops_3_67m_equity_neg` | **7.2** | 1378 De Nekker leftover EVA assets 0.75m / goods+diensten 3.67m / equity −26.2k |\n"
        "| `lb_ivag_omzet_81_14m_diensten_38_04m_ecov` | **7.4** | 1375 IVAGO leftover IGS assets 78.39m / omzet 81.14m / diensten 38.04m |\n"
        + old_abs.replace("**NEW 1370**", "1370")
    )
    if old_abs not in text:
        raise SystemExit("waste top10 missing havi absurdity row")
    text = text.replace(old_abs, new_abs, 1)
    p.write_text(text, encoding="utf-8")
    print("doge_waste_top10_current.md updated tick 1380; pure top10 unchanged")


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "INCOVO jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00239674; AV 26.06.2026)",
                "url": SRC_URL,
                "publisher": "INCOVO / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1380; official NBB VOL-inb PDF 1.10MB 54p deposit 2026-00239674 created 02.07.2026; "
                    "leftover IGS waste of Londerzeel+Machelen+Meise+Vilvoorde+Zemst; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Moore Audit BV B00212 / 0453.925.059 / "
                    "Carmen Van Camp A02365 + Jan De Bom Van Driessche A00909 12254 oordeel zonder voorbehoud assets 9396832 / PnL 18754; "
                    "VOL-inb 6.1/6.2/6.8/6.14/6.15/6.17/6.20/9 not filed; omzet 6.10 category/geo empty; every-10"
                ),
            },
            {
                "source_id": SRC2,
                "title": "INCOVO official site (leftover IGS afval Londerzeel/Machelen/Meise/Vilvoorde/Zemst; shared Interza-Incovo)",
                "url": SRC2_URL,
                "publisher": "INCOVO / Interza",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1380; leftover IGS of 5 Vlaams-Brabant municipalities; "
                    "incovo-interza.be is shared with INTERZA; statutory 2025 balans is the NBB CDN deposit"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO INCOVO 0218.993.039",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1380; KBO 0218.993.039 Actief / normale toestand since 10.10.1978; "
                    "statutaire naam Intercommunale Vereniging voor Vuilverwijdering voor Vilvoorde en Omliggende since 10.10.1978; "
                    "afkorting INCOVO since 10.10.1978; Opdrachthoudende vereniging (Vlaams Gewest) since 21.01.2004; "
                    "zetel Cyriel Buyssestraat 5 1800 Vilvoorde since 10.10.1978; 7 VE; "
                    "no KBO email/web/tel; btw since 01.07.1979; RSZ since 01.01.2022; aanbestedende overheid since 10.10.1978; "
                    "jaarvergadering mei; boekjaar 31 december; NACE 38.330/38.210/38.110"
                ),
            },
            {
                "source_id": SRC4,
                "title": "INCOVO FOI channel / official contact + shared Interza-Incovo site",
                "url": SRC4_URL,
                "publisher": "INCOVO",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1380; FOI financien@incovo-interza.be / info@incovo.be / communicatie@incovo.be / +32 2 255 94 70; "
                    "Cyriel Buyssestraat 5 1800 Vilvoorde; deposit lists financien@incovo-interza.be; no own KBO email/web/tel"
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
                "name_nl": "INCOVO (leftover IGS afval Vilvoorde en omliggende / Intercommunale Vereniging voor Vuilverwijdering)",
                "name_fr": "INCOVO (intercommunale residuelle de dechets Vilvorde et environs)",
                "name_en": "INCOVO leftover IGS waste Vilvoorde and surrounding municipalities",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.incovo-interza.be/nl",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1380 leftover residual IGS of Londerzeel+Machelen+Meise+Vilvoorde+Zemst; "
                    "KBO 0218.993.039 Actief since 10.10.1978; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 9396832 omzet 8522977 subs 6106178 diensten 7543829 pers 5881619 pnl 18754; "
                    "FOI ready omzet 6.10 empty / 6.11m 740 / 7.54m 61"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_inco_assets_2025", ENT, "2025", "9396832", "2025 assets 9396832 VOL-inb 20/58; tick1380; primary official NBB WVV; commissaris 9396832"),
        ("bud_inco_assets_2024", ENT, "2024", "8986363", "2024 assets 8986363 comparative; tick1380; primary official NBB WVV 20/58"),
        ("bud_inco_fixed_2025", ENT, "2025", "6025872", "2025 vaste activa 6025872 vs 6179645; tick1380; primary official NBB WVV 21/28"),
        ("bud_inco_mva_2025", ENT, "2025", "6021007", "2025 MVA 6021007 vs 6175842; tick1380; primary official NBB WVV 22/27"),
        ("bud_inco_buildings_2025", ENT, "2025", "1400158", "2025 terreinen/gebouwen 1400158 vs 1413909; tick1380; primary official NBB WVV 22"),
        ("bud_inco_machines_2025", ENT, "2025", "1543845", "2025 installaties/machines 1543845 vs 1653851; tick1380; primary official NBB WVV 23"),
        ("bud_inco_furniture_2025", ENT, "2025", "3077004", "2025 meubilair/rollend 3077004 vs 3108083; tick1380; primary official NBB WVV 24"),
        ("bud_inco_fva_2025", ENT, "2025", "4865", "2025 FVA 4865 vs 3803 (aandelen 403 + borg 4462); tick1380; primary official NBB WVV 28"),
        ("bud_inco_current_2025", ENT, "2025", "3370961", "2025 vlottende activa 3370961 vs 2806717; tick1380; primary official NBB WVV 29/58"),
        ("bud_inco_inv_2025", ENT, "2025", "72692", "2025 voorraden 72692 vs 121305; tick1380; primary official NBB WVV 3"),
        ("bud_inco_strecv_2025", ENT, "2025", "1679197", "2025 ST vorderingen 1679197 vs 1422734; tick1380; primary official NBB WVV 40/41"),
        ("bud_inco_trade_2025", ENT, "2025", "1552149", "2025 handelsvorderingen 1552149 vs 1336477; tick1380; primary official NBB WVV 40"),
        ("bud_inco_invest_2025", ENT, "2025", "1157039", "2025 geldbeleggingen 1157039 JUMP vs 871848 (all termijnrekeningen 53); tick1380; primary official NBB WVV 50/53"),
        ("bud_inco_invest_2024", ENT, "2024", "871848", "2024 geldbeleggingen 871848 comparative; tick1380; primary official NBB WVV 50/53"),
        ("bud_inco_term_1m_2025", ENT, "2025", "415620", "2025 termijn <=1m 415620 vs 336562; tick1380; primary official NBB WVV 6.6 8686"),
        ("bud_inco_term_1y_2025", ENT, "2025", "741419", "2025 termijn 1m-1y 741419 vs 535286; tick1380; primary official NBB WVV 6.6 8687"),
        ("bud_inco_cash_2025", ENT, "2025", "314258", "2025 liquide middelen 314258 JUMP vs 219542; tick1380; primary official NBB WVV 54/58"),
        ("bud_inco_cash_2024", ENT, "2024", "219542", "2024 liquide middelen 219542 comparative; tick1380; primary official NBB WVV 54/58"),
        ("bud_inco_prepaid_2025", ENT, "2025", "147774", "2025 overlopend actief 147774 (kosten 124547 + huurkoop 3227 + opbr 20000); tick1380; primary official NBB WVV 490/1"),
        ("bud_inco_equity_2025", ENT, "2025", "3964047", "2025 eigen vermogen 3964047 vs 3949732; tick1380; primary official NBB WVV 10/15"),
        ("bud_inco_equity_2024", ENT, "2024", "3949732", "2024 eigen vermogen 3949732 comparative; tick1380; primary official NBB WVV 10/15"),
        ("bud_inco_inbreng_2025", ENT, "2025", "1444189", "2025 inbreng onbeschikbaar 1444189 vs 1403445 (niet volgestort 2381639; 127026 aandelen); tick1380; primary official NBB WVV 10/11"),
        ("bud_inco_reval_2025", ENT, "2025", "21886", "2025 herwaarderingsmeerwaarden 21886; tick1380; primary official NBB WVV 12"),
        ("bud_inco_reserves_2025", ENT, "2025", "2194477", "2025 reserves 2194477 (onbeschikbaar 1200089 + beschikbaar 994388); tick1380; primary official NBB WVV 13"),
        ("bud_inco_capsib_2025", ENT, "2025", "303495", "2025 kapitaalsubsidies 303495 vs 348678; tick1380; primary official NBB WVV 15"),
        ("bud_inco_prov_2025", ENT, "2025", "2050799", "2025 voorzieningen 2050799 vs 2042444 (all 160 pensioenen); tick1380; primary official NBB WVV 16"),
        ("bud_inco_prov_2024", ENT, "2024", "2042444", "2024 voorzieningen 2042444 comparative; tick1380; primary official NBB WVV 16"),
        ("bud_inco_debt_2025", ENT, "2025", "3381986", "2025 schulden 3381986 vs 2994187; tick1380; primary official NBB WVV 17/49"),
        ("bud_inco_lt_2025", ENT, "2025", "759540", "2025 LT schulden 759540 vs 506888 (all 173 banken); tick1380; primary official NBB WVV 17"),
        ("bud_inco_st_2025", ENT, "2025", "2315323", "2025 ST schulden 2315323 vs 2103932; tick1380; primary official NBB WVV 42/48"),
        ("bud_inco_st_ltdue_2025", ENT, "2025", "128848", "2025 LT binnen jaar 128848 vs 77982; tick1380; primary official NBB WVV 42"),
        ("bud_inco_sttrade_2025", ENT, "2025", "1298578", "2025 leveranciers 1298578 vs 1226973; tick1380; primary official NBB WVV 440/4"),
        ("bud_inco_sttaxsoc_2025", ENT, "2025", "677756", "2025 tax+soc 677756 (tax 188490 + soc 489267); tick1380; primary official NBB WVV 45"),
        ("bud_inco_stother_2025", ENT, "2025", "210141", "2025 overige ST 210141 vs 201515; tick1380; primary official NBB WVV 47/48"),
        ("bud_inco_accrued_2025", ENT, "2025", "307123", "2025 overlopend passief 307123 (kosten 21132 + over te dragen 285990); tick1380; primary official NBB WVV 492/3"),
        ("bud_inco_opsinc_2025", ENT, "2025", "15249959", "2025 bedrijfsopbrengsten 15249959 vs 14201195; tick1380; primary official NBB WVV 70/76A"),
        ("bud_inco_omzet_2025", ENT, "2025", "8522977", "2025 omzet 8522977 vs 8519441; 6.10 category/geo empty; tick1380; primary official NBB WVV 70"),
        ("bud_inco_omzet_2024", ENT, "2024", "8519441", "2024 omzet 8519441 comparative; tick1380; primary official NBB WVV 70"),
        ("bud_inco_othops_2025", ENT, "2025", "6706244", "2025 andere bedrijfsopbrengsten 6706244 JUMP vs 5612718; tick1380; primary official NBB WVV 74"),
        ("bud_inco_subs_2025", ENT, "2025", "6106178", "2025 exploitatiesubsidies 6106178 JUMP vs 5011053 (740); tick1380; primary official NBB WVV 6.10 740"),
        ("bud_inco_subs_2024", ENT, "2024", "5011053", "2024 exploitatiesubsidies 5011053 comparative; tick1380; primary official NBB WVV 6.10 740"),
        ("bud_inco_nrec_2025", ENT, "2025", "20739", "2025 niet-recurrente bedrijfsopbrengsten 20739 vs 69036; tick1380; primary official NBB WVV 76A"),
        ("bud_inco_opscost_2025", ENT, "2025", "15249535", "2025 bedrijfskosten 15249535 vs 14578840; tick1380; primary official NBB WVV 60/66A"),
        ("bud_inco_goods_2025", ENT, "2025", "823009", "2025 handelsgoederen 823009 vs 841317 (aankopen 774397); tick1380; primary official NBB WVV 60"),
        ("bud_inco_diensten_2025", ENT, "2025", "7543829", "2025 diensten 7543829 vs 7212613; no split; tick1380; primary official NBB WVV 61"),
        ("bud_inco_diensten_2024", ENT, "2024", "7212613", "2024 diensten 7212613 comparative; tick1380; primary official NBB WVV 61"),
        ("bud_inco_pers_2025", ENT, "2025", "5881619", "2025 bezoldigingen 5881619 / 86.5 VTE / 106249 uur / YE 87; tick1380; primary official NBB WVV 62 9087"),
        ("bud_inco_pers_2024", ENT, "2024", "5702656", "2024 bezoldigingen 5702656 / 84.7 VTE comparative; tick1380; primary official NBB WVV 62"),
        ("bud_inco_pens624_2025", ENT, "2025", "530066", "2025 ouderdoms/overlevingspensioenen 530066 vs 611126; tick1380; primary official NBB WVV 6.10 624"),
        ("bud_inco_uitzend_2025", ENT, "2025", "776654", "2025 uitzendkosten 776654 / 16.4 VTE / 29491 uur; tick1380; primary official NBB WVV 6.10 617"),
        ("bud_inco_deprec_2025", ENT, "2025", "963547", "2025 afschrijvingen 963547 vs 948747; tick1380; primary official NBB WVV 630"),
        ("bud_inco_prov_pnl_2025", ENT, "2025", "8355", "2025 voorzieningen PnL +8355 vs -134267 (all pens 635); tick1380; primary official NBB WVV 635/8"),
        ("bud_inco_othcost_2025", ENT, "2025", "8078", "2025 andere bedrijfskosten 8078 vs 6312 (all 640 bedrijfsbelastingen); tick1380; primary official NBB WVV 640/8"),
        ("bud_inco_expl_2025", ENT, "2025", "425", "2025 bedrijfswinst 425 vs -377645; tick1380; primary official NBB WVV 9901"),
        ("bud_inco_expl_2024", ENT, "2024", "-377645", "2024 bedrijfsverlies -377645 comparative; tick1380; primary official NBB WVV 9901"),
        ("bud_inco_fininc_2025", ENT, "2025", "61323", "2025 financiele opbrengsten 61323 vs 85706 (kapitaalsubsidies 45182); tick1380; primary official NBB WVV 75"),
        ("bud_inco_fincost_2025", ENT, "2025", "38626", "2025 financiele kosten 38626 vs 16270 (schulden 21731); tick1380; primary official NBB WVV 65"),
        ("bud_inco_tax_2025", ENT, "2025", "4367", "2025 belastingen 4367 vs 11711; tick1380; primary official NBB WVV 67/77"),
        ("bud_inco_pnl_2025", ENT, "2025", "18754", "2025 PnL 9904 18754 vs -319920; commissaris 18754; tick1380; primary official NBB WVV"),
        ("bud_inco_pnl_2024", ENT, "2024", "-319920", "2024 PnL -319920 comparative; tick1380; primary official NBB WVV 9904"),
        ("bud_inco_comm_2025", ENT, "2025", "12254", "2025 commissaris Moore Audit BV / Van Camp + De Bom Van Driessche 12254; tick1380; primary official NBB WVV 9505"),
        ("bud_inco_inbreng_call_2025", ENT, "2025", "40744", "2025 volstorting inbreng 40743.75 (AV dec 2025 pop 127021); tick1380; primary official NBB WVV jaarverslag"),
        ("bud_inco_pop_2025", ENT, "2025", "127021", "2025 vennoten bevolking 127021 (Londerzeel 19400 / Machelen 16554 / Meise 20283 / Vilvoorde 47385 / Zemst 23399); tick1380; primary official NBB WVV jaarverslag"),
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
                "title": "INCOVO JR2025 leftover IGS dual (assets 9.40m / omzet 8.52m / subs 6.11m / diensten 7.54m / pens 2.05m / PnL +18.8k)",
                "entity_id": ENT,
                "beneficiary": "INCOVO / Londerzeel + Machelen + Meise + Vilvoorde + Zemst",
                "legal_basis": "WVV OV; Decreet Lokaal Bestuur; NBB neerlegging",
                "decision_date": "2026-06-26",
                "start_year": "1978",
                "end_year": "",
                "total_envelope_eur": "9396832",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL waste — 8.52m omzet (6.10 empty) / 6.11m subsidies / 7.54m diensten",
                "cut_option": "Publish unpublished omzet 6.10 + 6.11m 740 + 7.54m 61 + 2.05m pens + INTERZA pass-through; do not keep waste IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1380; assets 9396832 omzet 8522977 subs 6106178 diensten 7543829 pnl 18754 equity 3964047; FOI ready not sent; every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "INCOVO JR2025 leftover IGS: assets 9.40m / omzet 8.52m / subs 6.11m / diensten 7.54m / pens 2.05m / PnL +18.8k",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "7543829",
                "total_cost_eur": "9396832",
                "tco_notes": (
                    "Leftover dual IGS waste of 5 Vlaams-Brabant municipalities: "
                    "assets 9.40m / equity 3.96m / pnl +18.8k / omzet 8.52m (6.10 empty) / "
                    "subsidies 6.11m JUMP / diensten 7.54m / 86.5 VTE + 16.4 uitzend / pens 2.05m; "
                    "official NBB WVV live; do not treat 9.40m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "INCOVO / Londerzeel + Machelen + Meise + Vilvoorde + Zemst",
                "stated_goal": "Local leftover IGS map VL waste — JR2025 live; dual omzet-empty/subs/diensten FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 9.40m / omzet 8.52m / subs 6.11m / diensten 7.54m / pens 2.05m / pnl +18.8k",
                "absurdity_score": "7.0",
                "cost_score": "5.5",
                "difficulty": "2.5",
                "priority_index": "6.2",
                "cut_proposal": "Publish unpublished omzet 6.10 + 6.11m 740 + 7.54m 61 + 2.05m pens + INTERZA pass-through; do not keep waste IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1380; leftover IGS of 5 Vlaams-Brabant municipalities; FOI ready not sent; not TE-additive of 348bn; every-10",
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
                    "omzet 8522977 vs 8519441 (WVV 70; 6.10 category empty / geo empty) per stroom/tegenpartij/vennoot unpublished "
                    "+ exploitatiesubsidies 6106178 JUMP vs 5011053 (WVV 740; othops 6706244) per toekennende overheid "
                    "+ diensten 7543829 vs 7212613 (WVV 61; no split) top-20 leveranciers + INTERZA pass-through "
                    "+ pensioenvoorziening 2050799 (160; 624 530066) + uitzend 776654 / 16.4 VTE "
                    "+ andere personeelskosten 623 479204 JUMP vs 162913 "
                    "+ inbreng niet volgestort 2381639 / AV dec 2025 pop 127021 + VOL-inb 6.1/6.2/6.8/6.14/6.15/6.17/6.20/9 not filed"
                ),
                "why_it_matters": (
                    "Leftover IGS OV of 5 mined Vlaams-Brabant municipalities "
                    "(same leftover-IGS waste seam as ISVAG 1379 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IMOG 1369 / IVBO 1352): "
                    "9.40m assets / 8.52m omzet / 6.11m subsidies / 7.54m diensten / 2.05m pension / "
                    "86.5 VTE + 16.4 uitzend / shared INTERZA shell "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "INCOVO / Raad van Bestuur / Ken Degreef / Londerzeel + Machelen + Meise + Vilvoorde + Zemst",
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
                    "tick1380 leftover IGS OV of 5 Vlaams-Brabant municipalities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (1.10MB 54p deposit 2026-00239674). "
                    "ISVAG already mined 1379 — skipped. De Nekker already mined 1378 — skipped. "
                    "MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. "
                    "IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. "
                    "IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. "
                    "IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. "
                    "Nuhma-group seam 1353-1365 skipped. "
                    "INTERZA leftover IGS 0219.324.522 CDN 2026-00246462 live — leftover next. "
                    "Dommelhof leftover Limburg EVA 0777.495.085 still no JR2025 PDF. "
                    "IVAREM still 2024. Otary RS Nuhma-adjacent fallback not taken. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1380",
        "title": "INCOVO JR2025 leftover dual residual + every-10",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: EVERY-10 progress refresh from on-disk CSVs + INCOVO leftover IGS of 5 Vlaams-Brabant municipalities after honest hunt; "
            "KBO 0218.993.039 Actief; live JR2025 official NBB WVV VOL-inb PDF (1.10MB 54p deposit 2026-00239674; commissaris Moore Audit); "
            "sourced euros assets 9396832 / omzet 8522977 / subs 6106178 / diensten 7543829 / pers 5881619 / pnl 18754; "
            "FOI ready omzet 6.10 empty / 6.11m 740 / 7.54m 61"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T05:40:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1380 INCOVO leftover IGS residual + every-10; KBO 0218.993.039; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1381 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1381",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1380 done including INCOVO 1380 leftover IGS live NBB WVV + every-10 / "
            "ISVAG 1379 leftover IGS live NBB WVV / "
            "De Nekker 1378 leftover provincial EVA live NBB WVV / "
            "MIROM Menen 1377 leftover IGS live NBB WVV / "
            "MIROM Roeselare 1376 leftover IGS live NBB WVV / "
            "IVAGO 1375 leftover IGS live NBB WVV / "
            "MIWA 1374 leftover IGS live NBB WVV / "
            "IVOO 1373 leftover IGS live NBB WVV / "
            "IGEMO 1372 leftover IGS live NBB WVV / "
            "Veneco 1371 leftover IGS live NBB WVV / "
            "Haviland 1370 leftover IGS live NBB WVV + every-10); "
            "INTERZA leftover IGS KBO 0219.324.522 CDN 2026-00246462 now live — take if still unmined; "
            "Fluvius Midden-Vlaanderen / INTERGEM 0220.764.971 CDN 2026-00227859 live — leftover energy IGS later; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads "
            "(old VZW 0443.049.478 CDN 2026-00325874 is a different Tielt-Winge entity); "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB PIH / APB Inovant / APB Atlas listed or leftover but provincieantwerpen.be 403 — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1380 after INCOVO leftover IGS live NBB WVV + every-10; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1380", rq_new, rq_spawn)
    print("research_queue 1380", found, "spawned_1381", spawned)

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
                "last_unit_id": "rq_1380",
                "ticks_completed": "1380",
                "paused": "no",
                "notes": (
                    "tick1380 INCOVO leftover IGS residual + every-10; KBO 0218.993.039; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 9396832 omzet 8522977 subs 6106178 diensten 7543829 pers 5881619 pnl 18754 equity 3964047; "
                    "FOI ready omzet 6.10 empty/6.11m 740/7.54m 61; next rq_1381 residual dual L5 VL; continuous hole_fill"
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

    log = ROOT / "loop_log.md"
    entry = f"""### Tick 1380 - 2026-08-19 - rq_1380 INCOVO dual residual leftover + every-10
- Unit: Intercommunale Vereniging voor Vuilverwijdering voor Vilvoorde en Omliggende / INCOVO (leftover IGS opdrachthoudende vereniging / afvalophaling + recyclageparken of Londerzeel + Machelen + Meise + Vilvoorde + Zemst; shared Interza-Incovo site) after residual dual hunt (KBO **0218.993.039**; official incovo-interza.be has missie/bestuur/publicaties but no isolated statutory 2025 balans — live NBB WVV VOL-inb deposit **2026-00239674** PDF 1.10MB / 54p; AV **26.06.2026**; PDF created **02.07.2026**; commissaris Moore Audit BV B00212 / 0453.925.059 / Carmen Van Camp A02365 + Jan De Bom Van Driessche A00909 12.254 signed oordeel zonder voorbehoud assets 9.396.832 / PnL +18.754; 15e opeenvolgend boekjaar; mandaat AV 23.06.2023 tot AV 26.06.2026). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; prior ticks listed INCOVO CDN 2026-00239674 as leftover next after ISVAG 1379). Distinct from already-mined ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **10.10.1978**; statutaire naam Intercommunale Vereniging voor Vuilverwijdering voor Vilvoorde en Omliggende since 10.10.1978; afkorting INCOVO since 10.10.1978; Opdrachthoudende vereniging (Vlaams Gewest) since 21.01.2004; zetel Cyriel Buyssestraat 5 1800 Vilvoorde since 10.10.1978; **7 VE**; KBO no email/web/tel; official site https://www.incovo-interza.be/; tel +32 2 255 94 70; e-mail financien@incovo-interza.be / info@incovo.be; btw since 01.07.1979; RSZ since 01.01.2022; aanbestedende overheid since 10.10.1978; jaarvergadering mei; boekjaar 31 december; NACE 38.330/38.210/38.110. Voorzitter Ken Degreef since 13.03.2025; commissaris Moore Audit BV. Hunt leftover AGB/zorg/EVA first: leftover AGB Mechelen/Kortrijk/Brugge/Roeselare/Oostende 404/403 as of 1375 — not re-probed once live INCOVO extracted; Dommelhof leftover Limburg EVA KBO 0777.495.085 still no JR2025 PDF — not taken; IVAREM still 2024; leftover APB provincieantwerpen.be 403. INCOVO statutory CDN live this tick (HTTP 200 / 1096668 / 54p) — taken (preferred leftover IGS of mined Vilvoorde-ommeland municipalities outside Nuhma). ISVAG already mined 1379 — skipped. De Nekker already mined 1378 — skipped. MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 already mined — skipped. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. INTERZA 0219.324.522 CDN 2026-00246462 live — leftover next. Fluvius Midden-Vlaanderen / INTERGEM 0220.764.971 CDN 2026-00227859 live — leftover energy IGS later. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366. Every-10 (last 1370 Haviland).
- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud; VOL-inb 6.1/6.2/6.8/6.14/6.15/6.17/6.20/9 not filed; omzet 6.10 category/geo empty): assets **9.396.832** (was 8.986.363); fixed **6.025.872** / MVA **6.021.007** (gebouwen **1.400.158**; machines **1.543.845**; meubilair/rollend **3.077.004**); FVA 4.865; current **3.370.961**; inventory 72.692; ST recv **1.679.197** (trade 1.552.149); beleggingen **1.157.039 JUMP** vs 871.848 (termijn <=1m 415.620 + 1m-1y 741.419); cash **314.258 JUMP** vs 219.542; prepaid 147.774; equity **3.964.047** (was 3.949.732; inbreng 1.444.189 onbeschikbaar / niet volgestort 2.381.639 / 127.026 aandelen; reserves 2.194.477; kapitaalsubsidies 303.495); voorzieningen **2.050.799** (all 160 pensioenen); schulden **3.381.986** (LT bank **759.540**; ST **2.315.323** waarvan LT-due 128.848 + leveranciers 1.298.578 + tax/soc 677.756; accruals 307.123); omzet **8.522.977** vs 8.519.441 (6.10 unpublished); othops **6.706.244 JUMP** vs 5.612.718 waarvan exploitatiesubsidies **6.106.178 JUMP** vs 5.011.053; goods 823.009; diensten **7.543.829** vs 7.212.613; pers **5.881.619** / **86,5 VTE** / 106.249 uur / YE 87 + uitzend **16,4 VTE / 776.654**; pensioenkost 624 **530.066**; afschr 963.547; expl **+425** vs −377.645; fin opbr 61.323; fin kosten 38.626; tax 4.367; PnL **+18.754** vs −319.920 naar beschikbare reserve; commissaris 12.254. Jaarverslag same PDF: 5 vennoten pop **127.021** (Vilvoorde 47.385 / Zemst 23.399 / Meise 20.283 / Londerzeel 19.400 / Machelen 16.554); AV dec 2025 inbreng-aanpassing volstorting **40.743,75**.
- CSVs: sources+4/entities+1/budgets+63/commitments+1/leaderboard+1 + FOI ready `gap_inco_omzet_8_52m_subs_6_11m_diensten_7_54m_l5` (not sent); rq_1380=done; spawn rq_1381; ticks=1380.
- Coverage: residual dual L5 (INCOVO leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE.
- Every-10 progress (recount from disk after this tick writes): **A 100** / **B 100** / **C ~99** / **D ~74-88** (generous; not near-complete of 348bn) / **E ready {counts['foi_ready']}** (answered {counts['foi_answered']} / partial {counts['foi_partial']} / total {counts['foi_total']}). Inventory: budgets {counts['budgets']} · commitments {counts['commitments']} · leaderboard {counts['leaderboard']} · entities {counts['entities']} · sources {counts['sources']}. Waste top10 **stable** (GIP #1; fossil / cars / cheque / reporté #2-10). Dual off-top10 since 1370: IVAGO 78.39m · Veneco 51.98m · ISVAG 42.72m · MIROM Roeselare 37.44m · IGEMO 25.44m · MIWA 19.60m · MIROM Menen 11.71m · IVOO 10.74m · **INCOVO 9.40m** · De Nekker 0.75m. Progress files refreshed: `progress_every_10_ticks.md` + `doge_waste_top10_current.md`.
- Next: rq_1381 residual dual L5 VL JR2025 hole_fill (prefer leftover INTERZA KBO 0219.324.522 CDN 2026-00246462 now live; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS CDN 2026-00254280 / Rematics / Sunfin only if taken after leftover IGS/EVA/AGB; leftover APB POA / TPA / De Schorre / Warande / PIH / Inovant / Atlas only if a real PDF downloads; IVAREM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1380 write done")


if __name__ == "__main__":
    main()

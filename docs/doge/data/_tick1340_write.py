# -*- coding: utf-8 -*-
"""Tick 1340 — every-10 progress FIRST, then leftover EVA Limburg Sterk Merk JR2025 WVV euros.
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

TICK = "1340"
UTC = "2026-08-18T02:10:00Z"
ENT = "eva_lsm"
HIER = "Vlaanderen>Limburg>Provincie>EVA>LimburgSterkMerk"
GAP = "gap_lsm_pnl_1_5k_cash_drop_10_74m_portfolio_58_31m_l5"
SRC = "src_lsm_jr2025_pdf"
SRC2 = "src_lsm_site"
SRC3 = "src_kbo_lsm_0806608349"
SRC4 = "src_lsm_foi_contact"
SRC_URL = "http://www.stichtinglsm.be/uploads/LSM%20Jaarverslag%202025.pdf"
SRC2_URL = "http://www.stichtinglsm.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0806608349"
SRC4_URL = "https://www.limburg.be/bestuur-regio/openbaarheid-van-bestuur"
FOI_EMAIL = "info@limburg.be"
FOI_POSTAL = "Universiteitslaan 1 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_lsm_pnl_1_5k_cash_drop_10_74m_portfolio_58_31m_l5.md"
COMM = "comm_lsm_jr2025_portfolio"
LB = "lb_lsm_cash_drop_10_74m_portfolio_58_31m_pnl_1_5k"


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
    marker = "## Snapshot at **tick 1330** (2026-08-17)"
    if marker not in text:
        raise SystemExit("progress file missing tick 1330 marker")
    snap = f"""## Snapshot at **tick 1340** (2026-08-18)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1331-1340: APB Vormingscentrum Malle FOI · EVA Inagro FOI · WV Het Dak · WV OPcura · WV BVK · WV Weldenderend · WV Sleutelzorg FOI · **WV Zorgband** · **WV Zorgbedrijf Brasschaat** · **EVA Limburg Sterk Merk** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1331-1340 is VL residual dual L5 (not near-complete of 348bn):** **EVA LSM** assets **85.85m** cash **3.39m DROP 10.74m** portfolio **58.31m** PnL **+1.5k** · **WV Zorgband** assets **61.86m** PnL **−5.83m** lease **43.75m** · **WV Zorgbedrijf Brasschaat** assets **28.94m** cash **2.65m DROP** BBR **−5.39m** LT-recv **17.90m** · leftover zorg live BBC (Het Dak / OPcura / BVK / Weldenderend) · leftover FOI stack (Vormingscentrum Malle glossy / Inagro unpublished / Sleutelzorg unpublished) no invented euros · prior Hooibeekhoeve / EVA PV / Vonk / PSES / KampC stack retained |
| **E. FOI-ready gaps** | **~{counts['foi_ready']}** drafts ready | Human send only; answered **~{counts['foi_answered']}**; partial **~{counts['foi_partial']}**; total FOI rows **~{counts['foi_total']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA dual debt/AFM NEG + leasing/city-loan/erfpacht/DBFM/portfolio shells** (**NEW EVA LSM** assets **EUR85.85m** cash **EUR3.39m DROP 10.74m** portfolio **EUR58.31m** PnL **+EUR1.5k** · **WV Zorgband** assets **EUR61.86m** PnL **−EUR5.83m** lease **EUR43.75m** · **WV Zorgbedrijf Brasschaat** assets **EUR28.94m** cash **EUR2.65m** BBR **−EUR5.39m** LT-recv **EUR17.90m** · leftover zorg live BBC Het Dak / OPcura / BVK / Weldenderend · leftover FOI Vormingscentrum Malle / Inagro / Sleutelzorg · prior **APB Hooibeekhoeve** assets **EUR5.93m** cash **EUR2.65m** ST recv **EUR2.82m** BBR **+EUR1.30m** · **EVA Pluimveehouderij** assets **EUR8.63m** cash **EUR4.08m** ST recv **EUR4.46m** BBR **+EUR1.17m** · **APB Vonk** assets **EUR1.02m** cash **EUR0.96m** BBR **+EUR0.16m** · leftover FOI (Blankenberge / Campus Vesta / Monumentenwacht / Vlabinvest / Zilvermeer / Zorg HH / **EVA Kinderopvang Dilbeek**) · prior **APB KampC** assets **EUR5.93m** cash **EUR2.65m** ST recv **EUR3.06m** BBR **+EUR2.39m** J5/T2 werksub gap **EUR1.25m** · **APB PSES** assets **EUR186.52m** ST recv **EUR165.31m** BBR **−EUR1.29m** · **APB GKC** assets **EUR2.67m** cash **EUR2.11m** · **APB Havencentrum** assets **EUR0.97m** Havenwereld **EUR0.40m** · **AGBIM** CCAO **EUR8.91m** · **AGB Maaseik** fin debt **EUR1.60m** AFM **−EUR0.67m** · prior **APB VERA** fin debt **EUR1.72m** equity **−EUR1.64m** straight loan **EUR1.10m** · **Edegem** fin debt **EUR14.05m** pension **EUR23.40m** · **Beerse city** fin debt **EUR13.82m** · **AGB Beerse** fin debt **EUR5.02m** · **Pepingen city** fin debt **EUR3.47m** · **Vleteren** fin debt **EUR3.32m** · prior **Stad+OCMW Kortenaken** fin debt **EUR10.57m** IGS EV-reval **EUR8.90m** OCMW equity **−EUR5.41m** · **Heusden-Zolder** fin debt **EUR37.85m** IGS reval **EUR31.12m** · **Kapelle-op-den-Bos** fin debt **EUR18.87m** · **Oud-Heverlee** fin debt **EUR15.18m** · **Diepenbeek city** fin debt **EUR13.59m** IGS reval **EUR19.43m** · **Huldenberg** fin debt **EUR9.56m** · **AGB Kortenaken** fin debt **EUR3.28m** leasing **EUR3.22m** · **Voeren** fin debt **EUR3.37m** · **AGB Diepenbeek** fin debt **EUR3.03m** · **Steenokkerzeel** fin debt **EUR2.49m** · prior **Stad+OCMW Bekkevoort** fin debt **EUR9.77m** IGS EV-reval **EUR5.90m** · **HH city** fin debt **EUR17.37m** · **AGB Masterplan HH** fin debt **EUR27.81m** · **AGB Sport HH** fin debt **EUR10.72m** · **AGB SCO Ronse** fin debt **EUR22.65m** · **Ronse city** fin debt **EUR25.02m** pension **EUR19.50m** · **Kraainem** fin debt **EUR6.40m** · **Tielt-Winge** fin debt **EUR8.52m** · prior **Stad+OCMW Tienen** fin debt **EUR59.73m** pension **EUR51.29m** · **Machelen** fin debt **EUR26.37m** Farys lease **EUR16.90m** · **AGB Tienen** fin debt **EUR16.93m** · **AG Museum Leuven** fin debt **EUR14.51m** · **Gingelom** Fluvius reval **EUR9.75m** fin debt **EUR3.86m** · prior **AGB MAC** fin debt **EUR40.3m** leasing **EUR40.8m** · **Mintus** dual **EUR26.36m** · Digipolis assets **EUR73.61m** · **AG Vespa** fin debt **EUR179.6m** DBFM **EUR109.4m** · **sogent** AFM **−EUR3.90m** debt **EUR96.3m** · AG-O cum loss **−EUR29.2m** · Zorgbedrijf Antwerpen AFM **−EUR18.87m** debt **EUR220m** / Dodoens equity **−EUR18.88m** / Hasselt ~EUR95–103m stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market.

### Inventory (tick 1340)

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
| research_queue open | rq_116 deferred + rq_1341 hole-fill after progress |

### What improved since tick 1330

- **VL residual dual JR2025 leftover zorg/EVA (tick1331-1339):** **WV Zorgband** assets **61.86m** PnL **−5.83m** lease **43.75m** · **WV Zorgbedrijf Brasschaat** assets **28.94m** cash **2.65m DROP** BBR **−5.39m** LT-recv **17.90m** · leftover zorg live BBC (Het Dak / OPcura / BVK / Weldenderend) · leftover FOI (Vormingscentrum Malle glossy-only / Inagro unpublished / Sleutelzorg unpublished) — no invented euros.
- **NEW (tick1340):** **EVA Limburg Sterk Merk** (KBO 0806.608.349) leftover provinciaal EVA of already-mined provincie Limburg. Official jaarverslag 2025 PDF (1.24MB / 40p; InDesign 28.05.2026) embeds interne WVV jaarrekening (print 24.02.2026). Assets **85.847.015** · cash **3.394.910 DROP** vs 14.134.669 · portfolio **58.310.533** · PnL **+1.538** · expl **−3.548.237**. FOI ready. Every-10 progress refresh from on-disk CSVs.
- **Dual map themes:** **leftover EVA LRM-dividend / portfolio shell** (LSM 85.85m / cash drop 10.74m / Puilaetco 58.31m) · **leftover zorg live BBC** (Zorgband 61.86m / Brasschaat 28.94m) · leftover EVA/zorg unpublished FOI · prior leftover APB/EVA cash+ST-recv / AGB city-loan AFM NEG stack retained.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10.

---
"""
    text = text.replace(marker, snap + marker, 1)
    prog.write_text(text, encoding="utf-8")
    print("progress_every_10_ticks.md inserted tick 1340 snapshot")


def write_waste_top10(counts: dict) -> None:
    p = DATA / "doge_waste_top10_current.md"
    text = p.read_text(encoding="utf-8")
    text = text.replace(
        "**As-of:** tick **1330** (2026-08-17) · **7134** leaderboard rows",
        f"**As-of:** tick **1340** (2026-08-18) · **{counts['leaderboard']}** leaderboard rows",
        1,
    )
    old_dual = "(**NEW APB Hooibeekhoeve** assets **€5.93m** cash **€2.65m** ST recv **€2.82m** BBR **+€1.30m**"
    new_dual = (
        "(**NEW EVA LSM** assets **€85.85m** cash **€3.39m DROP 10.74m** portfolio **€58.31m** PnL **+€1.5k** · "
        "**WV Zorgband** assets **€61.86m** PnL **−€5.83m** lease **€43.75m** · "
        "**WV Zorgbedrijf Brasschaat** assets **€28.94m** cash **€2.65m** BBR **−€5.39m** LT-recv **€17.90m** · "
        "leftover zorg live BBC Het Dak / OPcura / BVK / Weldenderend · leftover FOI Vormingscentrum Malle / Inagro / Sleutelzorg · "
        "prior **APB Hooibeekhoeve** assets **€5.93m** cash **€2.65m** ST recv **€2.82m** BBR **+€1.30m**"
    )
    if old_dual not in text:
        raise SystemExit("waste top10 missing Hooibeekhoeve dual marker")
    text = text.replace(old_dual, new_dual, 1)
    old_chg = (
        "**Change vs tick 1320:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
        "**Major NEW residual 1321–1330 (off pure top10 / dual):**"
    )
    new_chg = (
        "**Change vs tick 1330:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
        "**Major NEW residual 1331–1340 (off pure top10 / dual):** **EVA LSM** assets **EUR85.85m** cash **EUR3.39m DROP 10.74m** portfolio **EUR58.31m** PnL **+EUR1.5k** · **WV Zorgband** assets **EUR61.86m** PnL **−EUR5.83m** · **WV Zorgbedrijf Brasschaat** assets **EUR28.94m** BBR **−EUR5.39m** LT-recv **EUR17.90m** · leftover zorg live BBC (Het Dak / OPcura / BVK / Weldenderend) · leftover FOI (Vormingscentrum Malle / Inagro / Sleutelzorg). "
        "Gain is **leftover EVA LRM-portfolio shell + leftover zorg live BBC + leftover EVA/zorg unpublished FOI**. "
        "**Prior 1321–1330 retained:**"
    )
    if old_chg not in text:
        raise SystemExit("waste top10 missing change-vs-1320 marker")
    text = text.replace(old_chg, new_chg, 1)
    old_out = "| — | `lb_evapv_cash_4_08m_recv_4_46m_bbr_1_17m` | **8.63 m stock** | **~5.4 dual** | **NEW 1322** EVA Pluimveehouderij cash 4.08m / ST recv 4.46m / BBR +1.17m |"
    new_out = (
        "| — | `lb_lsm_cash_drop_10_74m_portfolio_58_31m_pnl_1_5k` | **85.85 m stock** | **~6.5 dual** | **NEW 1340** EVA LSM cash drop 10.74m / portfolio 58.31m / PnL +1.5k |\n"
        "| — | `lb_zbls_pnl_neg_5_83m_afm_neg_0_36m_lease_43_75m` | **61.86 m stock** | **~6.5 dual** | **NEW 1338** WV Zorgband PnL −5.83m / lease 43.75m / AFM NEG |\n"
        "| — | `lb_zbb_bbr_neg_5_39m_cash_drop_5_68m_ltrecv_17_90m` | **28.94 m stock** | **~6.4 dual** | **NEW 1339** WV Zorgbedrijf Brasschaat BBR −5.39m / cash drop 5.68m / LT-recv 17.90m |\n"
        + old_out.replace("**NEW 1322**", "1322")
    )
    if old_out not in text:
        raise SystemExit("waste top10 missing evapv just-outside row")
    text = text.replace(old_out, new_out, 1)
    old_abs = "| `lb_evapv_cash_4_08m_recv_4_46m_bbr_1_17m` | **6.0** | **NEW 1322** EVA Pluimveehouderij assets 8.63m / cash 4.08m / ST recv 4.46m |"
    new_abs = (
        "| `lb_lsm_cash_drop_10_74m_portfolio_58_31m_pnl_1_5k` | **6.5** | **NEW 1340** EVA LSM assets 85.85m / cash drop 10.74m / portfolio 58.31m / PnL +1.5k |\n"
        "| `lb_zbls_pnl_neg_5_83m_afm_neg_0_36m_lease_43_75m` | **6.5** | **NEW 1338** WV Zorgband assets 61.86m / PnL −5.83m / lease 43.75m |\n"
        "| `lb_zbb_bbr_neg_5_39m_cash_drop_5_68m_ltrecv_17_90m` | **6.2** | **NEW 1339** WV Zorgbedrijf Brasschaat BBR −5.39m / cash drop 5.68m / LT-recv 17.90m |\n"
        + old_abs.replace("**NEW 1322**", "1322")
    )
    if old_abs not in text:
        raise SystemExit("waste top10 missing evapv absurdity row")
    text = text.replace(old_abs, new_abs, 1)
    p.write_text(text, encoding="utf-8")
    print("doge_waste_top10_current.md updated tick 1340; pure top10 unchanged")


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "EVA Limburg Sterk Merk jaarverslag 2025 (official PDF; interne WVV jaarrekening 24.02.2026)",
                "url": SRC_URL,
                "publisher": "Stichting Limburg Sterk Merk / Provincie Limburg",
                "accessed_date": "2026-08-18",
                "source_class": "budget",
                "notes": (
                    "tick1340; official PDF 1.24MB 40p; InDesign 28.05.2026; "
                    "embeds interne WVV balans/resultatenrekening print 24.02.2026; "
                    "leftover EVA of mined provincie Limburg; not BBC J1-J5"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Stichting LSM official site (Jaarverslag 2025 listed)",
                "url": SRC2_URL,
                "publisher": "Stichting Limburg Sterk Merk",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1340; HTTP 200 lists Jaarverslag 2025 PDF; "
                    "news Nieuw Jaarverslag 2025; leftover EVA of mined provincie Limburg"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Limburg Sterk Merk 0806.608.349",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1340; KBO 0806.608.349 Actief / normale toestand since 25.09.2008; "
                    "statutaire naam LIMBURG STERK MERK; afkorting LSM; "
                    "Stichting van openbaar nut since 07.08.2008; "
                    "zetel Universiteitslaan 1 3500 Hasselt since 01.01.2025; "
                    "0 VE; no KBO e-mail/web/tel; aanbestedende overheid since 07.08.2008; "
                    "boekjaar 31 december; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Provincie Limburg openbaarheid van bestuur (FOI channel)",
                "url": SRC4_URL,
                "publisher": "Provincie Limburg",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1340; FOI info@limburg.be / griffie@limburg.be; "
                    "Universiteitslaan 1 3500 Hasselt; Griffie tel 011 23 81 93; "
                    "official EVA page limburg.be/bestuur-regio/provinciebestuur/extern-verzelfstandigde-agentschappen"
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
                "name_nl": "Limburg Sterk Merk (stichting van openbaar nut / provinciaal EVA)",
                "name_fr": "Limburg Sterk Merk (fondation d'utilite publique / EVA provincial)",
                "name_en": "Limburg Sterk Merk (public-utility foundation / provincial EVA)",
                "level": "eva",
                "parent_id": "prov_limburg",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1340 leftover EVA residual of mined provincie Limburg; "
                    "KBO 0806.608.349 Actief since 25.09.2008; official JR2025 PDF downloads; "
                    "assets 85.847m cash 3.395m DROP portfolio 58.311m PnL +1.538; "
                    "FOI ready PnL/cash/portfolio/dual-LRM/NBB; every-10"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_lsm_assets_2025", "2025", "85847015", "2025 assets 85847015.22 was 90377642.92; tick1340; primary WVV in official PDF"),
        ("bud_lsm_cash_2025", "2025", "3394910", "2025 cash 3394910.17 DROP vs 14134668.85 (drop 10739758.68); tick1340; primary WVV"),
        ("bud_lsm_invest_2025", "2025", "58310533", "2025 geldbeleggingen 58310532.81 JUMP vs 47512384.01; tick1340; primary WVV"),
        ("bud_lsm_puilaetco_2025", "2025", "51394863", "2025 Puilaetco portefeuille 51394862.91 minus waardeverm 1084330.10; tick1340; primary WVV"),
        ("bud_lsm_term_dep_2025", "2025", "8000000", "2025 termijndeposito's Puilaetco 8000000 was 3750000; tick1340; primary WVV"),
        ("bud_lsm_st_recv_2025", "2025", "0", "2025 ST recv empty/0 (2024 was 34012 Kind & Taal N-376.5); tick1340; primary WVV"),
        ("bud_lsm_accruals_2025", "2025", "24141572", "2025 overlopend 24141572.24 (projectcontracten 24140733.35); tick1340; primary WVV"),
        ("bud_lsm_equity_2025", "2025", "55261928", "2025 equity/overgedragen winst 55261928.08 was 55260390.36; tick1340; primary WVV"),
        ("bud_lsm_debt_2025", "2025", "30585087", "2025 schulden 30585087.14 was 35117252.56; tick1340; primary WVV"),
        ("bud_lsm_lt_debt_2025", "2025", "3175000", "2025 LT overige schulden 3175000 NET after contra reclass; tick1340; primary WVV"),
        ("bud_lsm_st_debt_2025", "2025", "27361281", "2025 ST schulden 27361281.16 (project-pay 27315934.94 + leveranciers 45346.22); tick1340; primary WVV"),
        ("bud_lsm_st_project_pay_2025", "2025", "27315935", "2025 ST project-pay 27315934.94 (protocol 6350201.25 + nieuwe 20965733.69); tick1340; primary WVV"),
        ("bud_lsm_suppliers_2025", "2025", "45346", "2025 leveranciers 45346.22; tick1340; primary WVV"),
        ("bud_lsm_pnl_2025", "2025", "1538", "2025 PnL +1537.72 was +618474.46; tick1340; primary WVV 9904"),
        ("bud_lsm_ops_2025", "2025", "-3548237", "2025 bedrijfswinst -3548237.03 (opbr 999999.60 / kosten 4548236.63); tick1340; primary WVV"),
        ("bud_lsm_ops_rev_2025", "2025", "1000000", "2025 bedrijfsopbrengsten 999999.60 all VL Gemeenschap; tick1340; primary WVV"),
        ("bud_lsm_ops_cost_2025", "2025", "4548237", "2025 bedrijfskosten 4548236.63; tick1340; primary WVV"),
        ("bud_lsm_project_cost_2025", "2025", "4227820", "2025 project aankopen 4227819.79; tick1340; primary WVV"),
        ("bud_lsm_services_2025", "2025", "114212", "2025 diensten 114211.82; tick1340; primary WVV"),
        ("bud_lsm_rv_2025", "2025", "206205", "2025 roerende voorheffing 206205.02; tick1340; primary WVV"),
        ("bud_lsm_pers_2025", "2025", "0", "2025 bezoldigingen code 62 empty/0; KBO 0 VE; secretariat narrative 2.8 VTE FOI; tick1340; primary WVV"),
        ("bud_lsm_fin_inc_2025", "2025", "3775615", "2025 fin opbr 3775615.04 (div 404005 + vlottende 283345.04 + meerw 3088265); tick1340; primary WVV"),
        ("bud_lsm_fin_cost_2025", "2025", "225840", "2025 fin kosten 225840.29; tick1340; primary WVV"),
        ("bud_lsm_div_wvv_2025", "2025", "404005", "2025 ontvangen dividenden WVV 404005; tick1340; primary WVV"),
        ("bud_lsm_lrm_div_narr_2025", "2025", "999996", "narrative same official PDF: LRM dividend 2024 999996 received 09.09.2025 vs WVV VL-opbr 999999.60; tick1340"),
        ("bud_lsm_new_eng_2025", "2025", "19600000", "narrative same official PDF: 19.6m new 2025 engagements of 27.8m; tick1340"),
        ("bud_lsm_eng_prov_2025", "2025", "27895000", "narrative same official PDF: engagement in provisie 27895000; tick1340"),
        ("bud_lsm_cum_proj_2025", "2025", "341400000", "narrative same official PDF: 2008-2025 projects 341.4m (protocol 171.7m + thema 169.7m); tick1340"),
        ("bud_lsm_cum_lrm_div_2025", "2025", "133800000", "narrative same official PDF: cum LRM dividends 133.8m through 2025-12-31; tick1340"),
    ]
    n = append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": bid,
                "entity_id": ENT,
                "year": year,
                "amount_eur": amt,
                "amount_min_eur": "",
                "amount_max_eur": "",
                "basis": "executed",
                "source_id": SRC,
                "confidence": "strong",
                "notes": notes,
            }
            for bid, year, amt, notes in budget_rows
        ],
    )
    print("budgets", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": "EVA Limburg Sterk Merk JR2025 leftover EVA dual (portfolio 58.31m / cash drop 10.74m / PnL +1.5k / LRM dual)",
                "entity_id": ENT,
                "beneficiary": "Limburg Sterk Merk / hefboomprojecten provincie Limburg / LRM-dividend path",
                "legal_basis": "Decreet 23.05.2008 art.11-12 LRM-hertekening; protocol 09.06.2008 + addenda 2018/04.07.2024; Provinciedecreet EVA; Bestuursdecreet openbaarheid",
                "decision_date": "2008-08-07",
                "start_year": "2008",
                "end_year": "2025",
                "total_envelope_eur": "85847015",
                "cash_by_year": "",
                "remaining_eur": "55261928",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover EVA map VL provincie Limburg — LRM-dividend / hefboomprojecten; PnL/cash/portfolio/NBB missing",
                "cut_option": "Publish PnL/cash/portfolio recon + dual LRM 999996 vs 133.8m cum + NBB filing or non-filing rechtsgrond; do not recreate parallel EVA-shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1340; assets 85847015 cash 3394910 DROP portfolio 58310533 PnL +1538 ops -3548237; FOI ready not sent; every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "EVA Limburg Sterk Merk JR2025 leftover EVA: cash drop 10.74m / portfolio 58.31m / PnL +1.5k",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "4548237",
                "total_cost_eur": "85847015",
                "tco_notes": "Leftover dual EVA of mined provincie Limburg: assets 85.85m / cash drop 10.74m / Puilaetco portfolio 58.31m / PnL +1.5k vs ops -3.55m / narrative 19.6m new engagements; do not treat 85.85m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Limburg Sterk Merk / hefboomprojecten provincie Limburg / LRM-dividend path",
                "stated_goal": "Local leftover EVA map VL provincie Limburg — JR2025 PDF live; dual LRM/NBB FOI",
                "measured_outcome": "Official PDF 2026-08-18: assets 85.85m / cash 3.39m DROP / portfolio 58.31m / PnL +1.5k / ops -3.55m; KBO 0 VE; pers 0",
                "absurdity_score": "6.5",
                "cost_score": "6.8",
                "difficulty": "3.0",
                "priority_index": "6.5",
                "cut_proposal": "Publish PnL/cash/portfolio recon + dual LRM 999996 vs 133.8m cum + NBB filing or non-filing rechtsgrond; do not recreate parallel EVA-shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1340; leftover EVA of mined provincie Limburg; FOI ready not sent; not TE-additive of 348bn; every-10",
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
                    "Recon PnL +1537.72 vs ops -3548237.03 vs fin opbr 3775615.04 vs narrative "
                    "19.6m new hefboomprojecten / 27.8m engagements vs booked project costs "
                    "4227819.79 + destination of cash drop 10739758.68 (14134668.85 to 3394910.17) "
                    "vs portfolio JUMP 47512384.01 to 58310532.81 (Puilaetco + termijndeposito's "
                    "8000000) + overlopend projectcontracten 24140733.35 + counterparties/looptijd "
                    "of ST project-pay 27315934.94 (protocol 6350201.25 + nieuwe 20965733.69) vs "
                    "LT 3175000 NET after contra reclass + dual provincie/VL/LRM: received LRM "
                    "dividend narrative 999996 (09.09.2025) vs WVV VL-opbr 999999.60 vs cum "
                    "133.8m LRM-dividenden 2008-2025 vs protocol + addenda 2018/04.07.2024 + "
                    "nieuwe samenwerkingsovereenkomst Provincieraad 26.11.2025 + NBB/WVV "
                    "neerlegging (interne jaarrekening Vennootschap print 24.02.2026) or "
                    "non-filing rechtsgrond + commissarisverslag Foederer nv + Bestuursorgaan "
                    "vaststelling + machineleesbare export + personeel (KBO 0 VE / WVV pers 0 "
                    "vs secretariat narrative 2.8 VTE)."
                ),
                "why_it_matters": (
                    "Named leftover unmined EVA of already-mined provincie Limburg after honest "
                    "residual dual hunt. KBO 0806.608.349 Actief. Official jaarverslag 2025 PDF "
                    "now downloads (1.24MB 40p) with interne WVV jaarrekening. 85.85m leftover "
                    "LRM-dividend / portfolio shell with PnL +1.5k vs ops -3.55m, cash drop "
                    "10.74m and portfolio 58.31m. Prefer live PDF over unpublished FOI. "
                    "Ter Nethe still JR2024-only; Welzijnskoepel 2025 glossy-only not BBC; "
                    "AGB Lebbeke liquidated; AGB Bornem JR2024-only. APB POA/TPA/De Schorre/"
                    "Warande/De Nekker/PIH/Inovant/Atlas 403 / Foleon leftover slugs 404 or "
                    "redirect Hooibeekhoeve — not taken. Leftover cities still no fetchable "
                    "JR2025. Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "Stichting Limburg Sterk Merk / Provincie Limburg (Griffie)",
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
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; sourced euros from primary WVV in official PDF; every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1340",
        "title": "EVA LSM JR2025 leftover EVA dual residual + every-10 progress",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: every-10 progress refresh + EVA Limburg Sterk Merk leftover EVA of mined provincie Limburg "
            "after honest hunt; KBO 0806.608.349 Actief; live JR2025 official PDF "
            "(1.24MB 40p interne WVV 24.02.2026); sourced euros assets 85.847m / cash 3.395m DROP / "
            "portfolio 58.311m / PnL +1.538; FOI ready PnL/cash/portfolio/dual-LRM/NBB; progress@1340"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T01:20:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1340 EVA LSM leftover EVA residual + progress@1340; KBO 0806.608.349; "
            "live JR2025 PDF; sourced euros; FOI ready not sent; next rq_1341 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1341",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1340 done including EVA Limburg Sterk Merk 1340 leftover EVA live WVV + every-10 / "
            "WV Zorgbedrijf Brasschaat 1339 leftover zorg live BBC / "
            "WV Zorgband 1338 leftover zorg live BBC / "
            "WV Sleutelzorg 1337 leftover zorg FOI-unpublished / "
            "WV Weldenderend 1336 leftover zorg live BBC / "
            "WV BVK 1335 leftover zorg live BBC / "
            "WV OPcura 1334 leftover zorg live BBC / "
            "WV Het Dak 1333 leftover zorg live BBC / EVA Inagro 1332 FOI-unpublished / "
            "APB Vormingscentrum Malle 1331 FOI-glossy-not-BBC / "
            "EVA Kinderopvang Dilbeek 1330 FOI-unpublished + every-10 / "
            "Zorg Houthalen 1329 FOI-unpublished / APB Zilvermeer 1328 FOI-unpublished / "
            "APB Vlabinvest 1327 FOI-unpublished / APB Monumentenwacht WVL 1326 FOI-unpublished / "
            "APB Vonk 1325 leftover other-province APB / APB Campus Vesta 1324 FOI-glossy-not-BBC / "
            "AGB Blankenberge 1323 FOI-liquidated JR2019-only / EVA Proefbedrijf Pluimveehouderij 1322 leftover sister EVA / "
            "APB Hooibeekhoeve 1321 leftover sister APB / APB KampC 1320 leftover sister APB + every-10); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "Welzijnskoepel West-Brabant jaarverslag 2025 glossy-only — take only if a BBC PDF now downloads; "
            "Ter Nethe official still JR2024-only — take only if a PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / "
            "APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / APB Campus Vesta 1324 / AGB Blankenberge 1323 / "
            "EVA Proefbedrijf Pluimveehouderij 1322 / APB Hooibeekhoeve 1321 / APB KampC 1320 / "
            "APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 / "
            "AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 / Westtoer; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 (Foleon leftover slugs 404/redirect Hooibeekhoeve); not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1340 after EVA LSM leftover EVA live WVV + progress@1340; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1340", rq_new, rq_spawn)
    print("research_queue 1340", found, "spawned_1341", spawned)

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
                "last_unit_id": "rq_1340",
                "ticks_completed": "1340",
                "paused": "no",
                "notes": (
                    "tick1340 EVA LSM leftover EVA residual + progress@1340; KBO 0806.608.349; "
                    "live JR2025 PDF; sourced euros assets 85.847m cash 3.395m DROP portfolio 58.311m PnL +1.538; "
                    "FOI ready; next rq_1341 residual dual L5 VL; continuous hole_fill"
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
### Tick 1340 - 2026-08-18 - rq_1340 EVA LSM dual residual leftover EVA + progress@1340
- Unit: Limburg Sterk Merk (stichting van openbaar nut / provinciaal EVA) leftover EVA of already-mined provincie Limburg after residual dual hunt (KBO **0806.608.349**; official stichtinglsm.be + live jaarverslag 2025 PDF 1.24MB / 40p; InDesign **28.05.2026**; interne WVV jaarrekening print **24.02.2026**). EVERY-10 first: refreshed progress_every_10_ticks.md + doge_waste_top10_current.md from on-disk CSVs. THEN leftover EVA whose official page now yields a downloadable JR2025 PDF with euros (prefer live PDF over another unpublished FOI). Distinct from already-mined provincie Limburg / Dodoens / AGB Pelt / Zorg Houthalen 1329 / APB Vonk 1325 / Inagro 1332. KBO Actief / normale toestand since **25.09.2008**; statutaire naam LIMBURG STERK MERK; Stichting van openbaar nut since 07.08.2008; zetel Universiteitslaan 1 3500 Hasselt since 01.01.2025; **0 VE**; no KBO e-mail/web/tel; aanbestedende overheid; boekjaar 31 december; bestuurders o.m. Tom Vandeput / Inge Moors / Igor Philtjens; Directiecomité Jos Lantmeeters. Hunt leftover AGB/zorg first: Ter Nethe official still JR2024-only; Welzijnskoepel West-Brabant jaarverslag 2025 glossy-only — not BBC; AGB Lebbeke ontbonden / last JR2022; AGB Bornem official still JR2024-only; AGB De Kluize unpublished. Leftover cities Londerzeel official still JR2022–2024 only / Wortegem-Petegem official JR2020–2024 only / Zwalm `/jaarrekening` 404 / Holsbeek 404 / Maarkedal TLS / Linkebeek 404 / Kapellen city GE 404 / Drogenbos 404 / Boutersem archive-only / Maaseik city GE 404 / Bierbeek 404 still no fetchable JR2025. APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas official pages 403 / Foleon leftover slugs 404 or redirect already-mined Hooibeekhoeve — not taken. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / Vlabinvest 1327 / Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323. Every-10 tick.
- EUR strong (primary WVV balans/resultatenrekening in official PDF): assets **85.847.015** (was 90.377.643); cash **3.394.910** DROP vs 14.134.669 (drop **10.739.759**); geldbeleggingen **58.310.533** JUMP vs 47.512.384 (Puilaetco 51.394.863 − waardeverm 1.084.330 + termijndeposito's **8.000.000**); ST recv **0** (2024 was 34.012 Kind & Taal); overlopend **24.141.572** (projectcontracten **24.140.733**); equity **55.261.928**; schulden **30.585.087** (LT **3.175.000** NET + ST **27.361.281**); ST project-pay **27.315.935** (protocol 6.350.201 + nieuwe 20.965.734); leveranciers **45.346**; PnL **+1.538**; expl **−3.548.237** (opbr **999.999,60** VL / kosten **4.548.237**); projectkosten **4.227.820**; diensten **114.212**; roerende voorheffing **206.205**; pers **0**; fin opbr **+3.775.615** (div 404.005 + vlottende 283.345 + meerw 3.088.265); fin kosten **225.840**. Narratiefzelfde PDF: nieuwe engagementen **19,6m** van 27,8m / provisie **27,895m** / cum projecten **341,4m** (protocol 171,7m + thema 169,7m) / cum LRM-dividenden **133,8m** incl. **999.996** ontvangen 09.09.2025.
- CSVs: sources+4/entities+1/budgets+29/commitments+1/leaderboard+1 + FOI ready `{GAP}` (not sent); rq_1340=done; spawn rq_1341; ticks=1340.
- Progress@1340: refreshed progress_every_10_ticks.md + doge_waste_top10_current.md. Layers A 100 / B 100 / C ~99 / D ~74-88 (not near-complete of 348bn) / E recounted ready **{counts['foi_ready']}** (answered {counts['foi_answered']} / partial {counts['foi_partial']} / total {counts['foi_total']}). Inventory: budgets {counts['budgets']} · commitments {counts['commitments']} · leaderboard {counts['leaderboard']} · entities {counts['entities']} · sources {counts['sources']}. Pure annual waste top10 **stable** vs 1330 (GIP/fossil/cars/cheque/reporté). Dual off-top10 adds LSM 85.85m / Zorgband 61.86m / Brasschaat 28.94m + leftover zorg live BBC + leftover FOI stack.
- Coverage: 1331–1340 is residual dual L5 (Vormingscentrum Malle FOI · Inagro FOI · Het Dak · OPcura · BVK · Weldenderend · Sleutelzorg FOI · Zorgband · Zorgbedrijf Brasschaat · **EVA LSM**). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE.
- Next: rq_1341 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1340 write done")


if __name__ == "__main__":
    main()

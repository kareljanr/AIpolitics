# -*- coding: utf-8 -*-
"""Tick 1330 — every-10 progress FIRST, then leftover EVA Kinderopvang Dilbeek JR2025 unpublished FOI.
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

TICK = "1330"
UTC = "2026-08-17T21:30:00Z"
ENT = "eva_kodd"
HIER = "Vlaanderen>VlaamsBrabant>Dilbeek>EVA>Kinderopvang"
GAP = "gap_evakd_jr2025_unpublished_l5"
SRC = "src_evakd_docs"
SRC2 = "src_evakd_site"
SRC3 = "src_kbo_evakd_0477276325"
SRC4 = "src_evakd_foi_contact"
SRC_URL = "https://www.dilbeek.be/nl/eva-vzw-gemeentelijke-kinderopvang-dilbeek-0"
SRC2_URL = "https://www.dilbeek.be/nl/entities/eva-vzw-gemeentelijke-kinderopvang-dilbeek"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0477276325"
SRC4_URL = "https://www.dilbeek.be/nl/bestuur/inspraak-en-inzage/openbaarheid-van-bestuur"
FOI_EMAIL = "info@dilbeek.be"
FOI_POSTAL = "Gemeenteplein 1 1700 Dilbeek"
DRAFT = "docs/doge/foi/drafts/gap_evakd_jr2025_unpublished_l5.md"


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
    marker = "## Snapshot at **tick 1320** (2026-08-17)"
    if marker not in text:
        raise SystemExit("progress file missing tick 1320 marker")
    snap = f"""## Snapshot at **tick 1330** (2026-08-17)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1321-1330: APB Hooibeekhoeve · EVA Pluimveehouderij · AGB Blankenberge FOI · Campus Vesta FOI · **APB Vonk** · Monumentenwacht WVL FOI · Vlabinvest FOI · Zilvermeer FOI · Zorg Houthalen FOI · **EVA Kinderopvang Dilbeek FOI** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1321-1330 is VL residual dual L5 (not near-complete of 348bn):** **APB Hooibeekhoeve** assets **5.93m** cash **2.65m** ST recv **2.82m** BBR **+1.30m** · **EVA Pluimveehouderij** assets **8.63m** cash **4.08m** ST recv **4.46m** BBR **+1.17m** · **APB Vonk** assets **1.02m** cash **0.96m** BBR **+0.16m** · leftover FOI stack (Blankenberge / Campus Vesta / Monumentenwacht / Vlabinvest / Zilvermeer / Zorg HH / **EVA Kinderopvang Dilbeek**) no invented euros · prior PSES / KampC / AGBIM / AGB Maaseik / GKC / Havencentrum / Edegem / Beerse / VERA stack retained |
| **E. FOI-ready gaps** | **~{counts['foi_ready']}** drafts ready | Human send only; answered **~{counts['foi_answered']}**; partial **~{counts['foi_partial']}**; total FOI rows **~{counts['foi_total']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB dual debt/AFM NEG + leasing/city-loan/erfpacht/DBFM shells** (**NEW APB Hooibeekhoeve** assets **EUR5.93m** cash **EUR2.65m** ST recv **EUR2.82m** BBR **+EUR1.30m** · **EVA Pluimveehouderij** assets **EUR8.63m** cash **EUR4.08m** ST recv **EUR4.46m** BBR **+EUR1.17m** · **APB Vonk** assets **EUR1.02m** cash **EUR0.96m** BBR **+EUR0.16m** · leftover FOI (Blankenberge / Campus Vesta / Monumentenwacht / Vlabinvest / Zilvermeer / Zorg HH / **EVA Kinderopvang Dilbeek**) · prior **APB KampC** assets **EUR5.93m** cash **EUR2.65m** ST recv **EUR3.06m** BBR **+EUR2.39m** J5/T2 werksub gap **EUR1.25m** · **APB PSES** assets **EUR186.52m** ST recv **EUR165.31m** BBR **−EUR1.29m** · **APB GKC** assets **EUR2.67m** cash **EUR2.11m** · **APB Havencentrum** assets **EUR0.97m** Havenwereld **EUR0.40m** · **AGBIM** CCAO **EUR8.91m** · **AGB Maaseik** fin debt **EUR1.60m** AFM **−EUR0.67m** · prior **APB VERA** fin debt **EUR1.72m** equity **−EUR1.64m** straight loan **EUR1.10m** · **Edegem** fin debt **EUR14.05m** pension **EUR23.40m** · **Beerse city** fin debt **EUR13.82m** · **AGB Beerse** fin debt **EUR5.02m** · **Pepingen city** fin debt **EUR3.47m** · **Vleteren** fin debt **EUR3.32m** · prior **Stad+OCMW Kortenaken** fin debt **EUR10.57m** IGS EV-reval **EUR8.90m** OCMW equity **−EUR5.41m** · **Heusden-Zolder** fin debt **EUR37.85m** IGS reval **EUR31.12m** · **Kapelle-op-den-Bos** fin debt **EUR18.87m** · **Oud-Heverlee** fin debt **EUR15.18m** · **Diepenbeek city** fin debt **EUR13.59m** IGS reval **EUR19.43m** · **Huldenberg** fin debt **EUR9.56m** · **AGB Kortenaken** fin debt **EUR3.28m** leasing **EUR3.22m** · **Voeren** fin debt **EUR3.37m** · **AGB Diepenbeek** fin debt **EUR3.03m** · **Steenokkerzeel** fin debt **EUR2.49m** · prior **Stad+OCMW Bekkevoort** fin debt **EUR9.77m** IGS EV-reval **EUR5.90m** · **HH city** fin debt **EUR17.37m** · **AGB Masterplan HH** fin debt **EUR27.81m** · **AGB Sport HH** fin debt **EUR10.72m** · **AGB SCO Ronse** fin debt **EUR22.65m** · **Ronse city** fin debt **EUR25.02m** pension **EUR19.50m** · **Kraainem** fin debt **EUR6.40m** · **Tielt-Winge** fin debt **EUR8.52m** · prior **Stad+OCMW Tienen** fin debt **EUR59.73m** pension **EUR51.29m** · **Machelen** fin debt **EUR26.37m** Farys lease **EUR16.90m** · **AGB Tienen** fin debt **EUR16.93m** · **AG Museum Leuven** fin debt **EUR14.51m** · **Gingelom** Fluvius reval **EUR9.75m** fin debt **EUR3.86m** · prior **AGB MAC** fin debt **EUR40.3m** leasing **EUR40.8m** · **Mintus** dual **EUR26.36m** · Digipolis assets **EUR73.61m** · **AG Vespa** fin debt **EUR179.6m** DBFM **EUR109.4m** · **sogent** AFM **−EUR3.90m** debt **EUR96.3m** · AG-O cum loss **−EUR29.2m** · Zorgbedrijf Antwerpen AFM **−EUR18.87m** debt **EUR220m** / Dodoens equity **−EUR18.88m** / Hasselt ~EUR95–103m stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market.

### Inventory (tick 1330)

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
| research_queue open | rq_116 deferred + rq_1331 hole-fill after progress |

### What improved since tick 1320

- **VL residual dual JR2025 leftover APB/EVA/zorg (tick1321-1329):** **APB Hooibeekhoeve** assets **5.93m** cash **2.65m** ST recv **2.82m** BBR **+1.30m** · **EVA Pluimveehouderij** assets **8.63m** cash **4.08m** ST recv **4.46m** BBR **+1.17m** · **APB Vonk** assets **1.02m** cash **0.96m** BBR **+0.16m** · AGB Blankenberge / Campus Vesta / Monumentenwacht WVL / Vlabinvest / Zilvermeer / Zorg Houthalen JR2025 unpublished or glossy-only — FOI-ready no invented euros.
- **NEW (tick1330):** **EVA-vzw Gemeentelijke Kinderopvang Dilbeek** (KBO 0477.276.325) leftover EVA of already-mined Dilbeek city GE. Official EVA page still **JR2024-only**. NBB consult 403/SPA (index lists 2025 filing 2026-00242617 / 01.07.2026 — no PDF bytes). No sourced euros. FOI ready. Every-10 progress refresh from on-disk CSVs.
- **Dual map themes:** **leftover APB/EVA cash+ST-recv shells** (Hooibeekhoeve 5.93m / EVA PV 8.63m / Vonk 1.02m) · **leftover EVA/zorg unpublished FOI** (Kinderopvang Dilbeek / Zorg HH / Campus Vesta glossy) · prior leftover APB pass-through / AGB city-loan AFM NEG stack retained.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10.

---
"""
    text = text.replace(marker, snap + marker, 1)
    prog.write_text(text, encoding="utf-8")
    print("progress_every_10_ticks.md inserted tick 1330 snapshot")


def write_waste_top10(counts: dict) -> None:
    p = DATA / "doge_waste_top10_current.md"
    text = p.read_text(encoding="utf-8")
    text = text.replace(
        "**As-of:** tick **1320** (2026-08-17) · **7124** leaderboard rows",
        f"**As-of:** tick **1330** (2026-08-17) · **{counts['leaderboard']}** leaderboard rows",
        1,
    )
    old_dual = "(**NEW APB KampC** assets **€5.93m** cash **€2.65m** ST recv **€3.06m** BBR **+€2.39m**"
    new_dual = (
        "(**NEW APB Hooibeekhoeve** assets **€5.93m** cash **€2.65m** ST recv **€2.82m** BBR **+€1.30m** · "
        "**EVA Pluimveehouderij** assets **€8.63m** cash **€4.08m** ST recv **€4.46m** BBR **+€1.17m** · "
        "**APB Vonk** assets **€1.02m** cash **€0.96m** BBR **+€0.16m** · "
        "leftover FOI Blankenberge / Campus Vesta / Monumentenwacht / Vlabinvest / Zilvermeer / Zorg HH / **EVA Kinderopvang Dilbeek** · "
        "prior **APB KampC** assets **€5.93m** cash **€2.65m** ST recv **€3.06m** BBR **+€2.39m**"
    )
    if old_dual not in text:
        raise SystemExit("waste top10 missing KampC dual marker")
    text = text.replace(old_dual, new_dual, 1)
    old_chg = (
        "**Change vs tick 1310:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
        "**Major NEW residual 1311–1320 (off pure top10 / dual):**"
    )
    new_chg = (
        "**Change vs tick 1320:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
        "**Major NEW residual 1321–1330 (off pure top10 / dual):** **APB Hooibeekhoeve** assets **EUR5.93m** cash **EUR2.65m** ST recv **EUR2.82m** · **EVA Pluimveehouderij** assets **EUR8.63m** cash **EUR4.08m** ST recv **EUR4.46m** · **APB Vonk** assets **EUR1.02m** cash **EUR0.96m** · leftover FOI (Blankenberge / Campus Vesta / Monumentenwacht / Vlabinvest / Zilvermeer / Zorg HH / **EVA Kinderopvang Dilbeek**). "
        "Gain is **leftover APB/EVA cash+ST-recv shells + leftover EVA/zorg unpublished FOI**. "
        "**Prior 1311–1320 retained:**"
    )
    if old_chg not in text:
        raise SystemExit("waste top10 missing change-vs-1310 marker")
    text = text.replace(old_chg, new_chg, 1)
    old_out = "| — | `lb_pses_passthrough_186m_bbr_neg_1_29m` | **186.52 m stock** | **~6.8 dual** | **NEW 1317** APB PSES pass-through / ST recv 165.31m / BBR NEG |"
    new_out = (
        "| — | `lb_evapv_cash_4_08m_recv_4_46m_bbr_1_17m` | **8.63 m stock** | **~5.4 dual** | **NEW 1322** EVA Pluimveehouderij cash 4.08m / ST recv 4.46m / BBR +1.17m |\n"
        "| — | `lb_hbh_cash_2_65m_recv_2_82m_bbr_1_30m` | **5.93 m stock** | **~5.3 dual** | **NEW 1321** APB Hooibeekhoeve cash 2.65m / ST recv 2.82m / BBR +1.30m |\n"
        "| — | `lb_vonk_liq_cash_0_96m_bbr_0_16m` | **1.02 m stock** | **~5.0 dual** | **NEW 1325** APB Vonk leftover other-province APB cash 0.96m / BBR +0.16m |\n"
        + old_out.replace("**NEW 1317**", "1317")
    )
    if old_out not in text:
        raise SystemExit("waste top10 missing pses just-outside row")
    text = text.replace(old_out, new_out, 1)
    old_abs = "| `lb_pses_passthrough_186m_bbr_neg_1_29m` | **6.5** | **NEW 1317** APB PSES 186.52m pass-through / BBR −1.29m / thin equity 2.42m |"
    new_abs = (
        "| `lb_evapv_cash_4_08m_recv_4_46m_bbr_1_17m` | **6.0** | **NEW 1322** EVA Pluimveehouderij assets 8.63m / cash 4.08m / ST recv 4.46m |\n"
        "| `lb_hbh_cash_2_65m_recv_2_82m_bbr_1_30m` | **6.0** | **NEW 1321** APB Hooibeekhoeve assets 5.93m / J5 vs T2 werksub gap 1.02m |\n"
        + old_abs.replace("**NEW 1317**", "1317")
    )
    if old_abs not in text:
        raise SystemExit("waste top10 missing pses absurdity row")
    text = text.replace(old_abs, new_abs, 1)
    p.write_text(text, encoding="utf-8")
    print("doge_waste_top10_current.md updated tick 1330; pure top10 unchanged")


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "EVA-vzw Gemeentelijke Kinderopvang Dilbeek official page (last public JR2024; no JR2025 PDF)",
                "url": SRC_URL,
                "publisher": "Lokaal bestuur Dilbeek / EVA-vzw Gemeentelijke Kinderopvang Dilbeek",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1330; official EVA page still lists Jaarrekening 2024 as latest; "
                    "no JR2025 BBC/NBB PDF linked; leftover EVA of mined Dilbeek city GE"
                ),
            },
            {
                "source_id": SRC2,
                "title": "EVA-vzw Gemeentelijke Kinderopvang Dilbeek entity/locations page (no JR2025 BBC PDF)",
                "url": SRC2_URL,
                "publisher": "EVA-vzw Gemeentelijke Kinderopvang Dilbeek",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1330; HTTP 200 locations page; 3 kinderdagverblijven + onthaalouders; "
                    "no BBC/NBB PDF linked"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO EVA-vzw Gemeentelijke Kinderopvang Dilbeek 0477.276.325",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1330; KBO 0477.276.325 Actief / normale toestand since 30.04.2002; "
                    "statutaire naam GEMEENTELIJKE KINDEROPVANG DILBEEK; VZW; "
                    "zetel Gemeenteplein 1 1700 Dilbeek; 3 VE; RSZ-werkgever since 01.07.2001; "
                    "kinderopvang since 01.04.2014; NACE RSZ2025 88.911; jaarvergadering mei; "
                    "boekjaar 31 december; no KBO e-mail/web/finance; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Dilbeek openbaarheid van bestuur (FOI channel)",
                "url": SRC4_URL,
                "publisher": "Lokaal bestuur Dilbeek",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1330; FOI info@dilbeek.be / secretariaat@dilbeek.be; "
                    "Gemeenteplein 1 1700 Dilbeek; cc kinderopvang@dilbeek.be"
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
                "name_nl": "EVA-vzw Gemeentelijke Kinderopvang Dilbeek",
                "name_fr": "EVA ASBL Accueil communal de l'enfance Dilbeek",
                "name_en": "EVA non-profit Dilbeek municipal childcare",
                "level": "eva",
                "parent_id": "city_dilbeek",
                "community_language": "nl",
                "website": SRC_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1330 leftover EVA residual of mined Dilbeek city GE; "
                    "KBO 0477.276.325 Actief since 30.04.2002; no fetchable JR2025 BBC/NBB PDF "
                    "(official EVA page last JR2024 / NBB consult 403); "
                    "no sourced euros; FOI ready; every-10"
                ),
            },
        ],
    )
    print("entities", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_evakd_jr2025_unpublished",
                "title": "EVA Kinderopvang Dilbeek JR2025 unpublished (last public EVA JR2024; FOI-ready)",
                "entity_id": ENT,
                "beneficiary": "Kinderdagverblijven 't bijgaardje / 't klein keperke / 't bergske + onthaalouders Dilbeek",
                "legal_basis": "Decreet lokaal bestuur EVA-vzw; Kind en Gezin; Bestuursdecreet openbaarheid",
                "decision_date": "2002-04-30",
                "start_year": "2002",
                "end_year": "2025",
                "total_envelope_eur": "",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "unknown",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover EVA map VL Dilbeek — inkomensgerelateerde kinderopvang; BBC/NBB extract missing",
                "cut_option": "Publish BBC/WVV JR2025 + RVB/GR + NBB PDF 2026-00242617 + dual city/OCMW / VTE lines",
                "source_id": SRC3,
                "confidence": "medium",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1330; no sourced euros; no fetchable BBC/NBB PDF; FOI ready not sent; every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_evakd_jr2025_unpublished",
                "name": "EVA Kinderopvang Dilbeek JR2025 (last public EVA JR2024; no official 2025 PDF)",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "",
                "total_cost_eur": "",
                "tco_notes": "No primary JR2025 BBC/NBB euros; official last EVA JR2024; NBB consult 403; do not use Belscope/Companyweb/FinCheck",
                "confidence": "medium",
                "source_id": SRC3,
                "beneficiaries": "Kinderdagverblijven 't bijgaardje / 't klein keperke / 't bergske + onthaalouders Dilbeek",
                "stated_goal": "Local leftover EVA map VL Dilbeek — BBC/NBB PDF unpublished",
                "measured_outcome": "KBO 0477.276.325 active; 2026-08-17 official last EVA JR2024; NBB index lists 2025 filing but no fetchable PDF bytes",
                "absurdity_score": "6.0",
                "cost_score": "2.0",
                "difficulty": "2.0",
                "priority_index": "5.0",
                "cut_proposal": "Publish BBC/WVV JR2025 + RVB/GR + NBB PDF 2026-00242617 + dual city/OCMW / VTE",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1330; no invented euros; FOI ready not sent; leftover EVA of mined Dilbeek; not TE-additive of 348bn; every-10",
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
                    "BBC/WVV jaarrekening 2025 EVA-vzw Gemeentelijke Kinderopvang Dilbeek "
                    "(J1-J5 / T2-T5 or verkort model vereniging / BBR / AFM / fin debt / "
                    "city-OCMW dotaties / kinderdagverblijven+onthaalouders / VTE) + RVB/GR "
                    "of AV vaststelling + NBB filing PDF 2026-00242617 (neerlegging 01.07.2026) "
                    "or non-filing rechtsgrond + dual city/OCMW JR2025 lines. Official EVA page "
                    "last JR2024; NBB consult 403/SPA; no JR2025 PDF bytes."
                ),
                "why_it_matters": (
                    "Named leftover unmined EVA of already-mined Dilbeek city GE after honest "
                    "residual dual hunt. KBO 0477.276.325 Actief. No fetchable JR2025 BBC/NBB PDF. "
                    "APB POA/TPA/De Schorre/Warande/De Nekker list JR2025 filenames but no leftover "
                    "PDF bytes — not taken. Leftover cities still no fetchable JR2025. Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "EVA-vzw Gemeentelijke Kinderopvang Dilbeek / Lokaal bestuur Dilbeek",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_evakd_jr2025_unpublished",
                "linked_leaderboard_id": "lb_evakd_jr2025_unpublished",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; no sourced euros; every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1330",
        "title": "EVA Kinderopvang Dilbeek JR2025 unpublished dual residual FOI + every-10 progress",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: every-10 progress refresh + EVA Kinderopvang Dilbeek leftover EVA after honest hunt; "
            "KBO 0477.276.325 Actief; no fetchable JR2025 BBC/NBB PDF "
            "(official EVA page last JR2024 / NBB consult 403); "
            "no sourced euros; FOI ready; progress@1330"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T20:20:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1330 EVA Kinderopvang Dilbeek leftover EVA residual + progress@1330; KBO 0477.276.325; "
            "no fetchable BBC/NBB PDF; no sourced euros; FOI ready not sent; next rq_1331 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1331",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1330 done including EVA Kinderopvang Dilbeek 1330 FOI-unpublished + every-10 / "
            "Zorg Houthalen 1329 FOI-unpublished / APB Zilvermeer 1328 FOI-unpublished / "
            "APB Vlabinvest 1327 FOI-unpublished / APB Monumentenwacht WVL 1326 FOI-unpublished / "
            "APB Vonk 1325 leftover other-province APB / APB Campus Vesta 1324 FOI-glossy-not-BBC / "
            "AGB Blankenberge 1323 FOI-liquidated JR2019-only / EVA Proefbedrijf Pluimveehouderij 1322 leftover sister EVA / "
            "APB Hooibeekhoeve 1321 leftover sister APB / APB KampC 1320 leftover sister APB + every-10); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker listed on provincieantwerpen.be but no PDF bytes — take only if a real PDF downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / "
            "APB Monumentenwacht WVL 1326 / APB Vonk 1325 / APB Campus Vesta 1324 / AGB Blankenberge 1323 / "
            "EVA Proefbedrijf Pluimveehouderij 1322 / APB Hooibeekhoeve 1321 / APB KampC 1320 / "
            "APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 / "
            "AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 / Westtoer; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 (Foleon leftover slugs redirect Hooibeekhoeve); not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1330 after EVA Kinderopvang Dilbeek leftover EVA FOI + progress@1330; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1330", rq_new, rq_spawn)
    print("research_queue 1330", found, "spawned_1331", spawned)

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
                "last_unit_id": "rq_1330",
                "ticks_completed": "1330",
                "paused": "no",
                "notes": (
                    "tick1330 EVA Kinderopvang Dilbeek leftover EVA residual + progress@1330; KBO 0477.276.325; "
                    "no fetchable JR2025 BBC/NBB PDF; no sourced euros; FOI ready; next rq_1331 residual dual L5 VL; continuous hole_fill"
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
### Tick 1330 - 2026-08-17 - rq_1330 EVA Kinderopvang Dilbeek dual residual unpublished FOI + progress@1330
- Unit: EVA-vzw Gemeentelijke Kinderopvang Dilbeek leftover EVA of already-mined Dilbeek city GE (tick 877) after residual dual hunt (KBO **0477.276.325**; official EVA page + KBO; **no fetchable JR2025 BBC/NBB PDF**). EVERY-10 first: refreshed progress_every_10_ticks.md + doge_waste_top10_current.md from on-disk CSVs. THEN leftover EVA whose official page still lists **Jaarrekening 2024** only. NBB consult skipped (403/SPA) even though index lists 2025 filing **2026-00242617** (01.07.2026) — no PDF bytes. Distinct from already-mined EVA Pluimveehouderij 1322 / EVA Hoeve Holleken 1309 / EVA Gezinswelzijn Lokeren 1253. KBO Actief / normale toestand since **30.04.2002**; VZW; zetel Gemeenteplein 1 1700 Dilbeek; **3 VE**; RSZ-werkgever since 01.07.2001; kinderopvang since 01.04.2014; NACE 88.911; jaarvergadering mei; no KBO e-mail. Three kinderdagverblijven ('t bijgaardje / 't klein keperke / 't bergske) + onthaalouders; inkomensgerelateerd Kind & Gezin. Hunt leftover AGB first: AGB Bornem official still JR2024-only; AGB De Kluize unpublished; Dilbeek has no AGB. Leftover cities Londerzeel official still JR2022–2024 only / Wortegem-Petegem official JR2020–2024 only / Zwalm `/jaarrekening` 404 / Holsbeek / Maarkedal / Linkebeek / Kapellen city GE / Drogenbos / Boutersem / Maaseik city GE / Bierbeek still no fetchable JR2025. APB POA/TPA/De Schorre/Warande/De Nekker official pages also list JR2025 filenames — no leftover PDF bytes (403 / Foleon leftover slugs redirect Hooibeekhoeve); not taken. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Zorg Houthalen 1329 / APB Zilvermeer 1328 / Vlabinvest 1327 / Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320. Every-10 tick.
- EUR: **none sourced**. Do not invent euros. FOI-ready after honest hunt (no fetchable BBC/NBB PDF).
- CSVs: sources+4/entities+1/commitments+1/leaderboard+1 + FOI ready `{GAP}` (not sent); no budget rows (no euros); rq_1330=done; spawn rq_1331; ticks=1330.
- Progress@1330: refreshed progress_every_10_ticks.md + doge_waste_top10_current.md. Layers A 100 / B 100 / C ~99 / D ~74-88 (not near-complete of 348bn) / E recounted ready **{counts['foi_ready']}** (answered {counts['foi_answered']} / partial {counts['foi_partial']} / total {counts['foi_total']}). Inventory: budgets {counts['budgets']} · commitments {counts['commitments']} · leaderboard {counts['leaderboard']} · entities {counts['entities']} · sources {counts['sources']}. Pure annual waste top10 **stable** vs 1320 (GIP/fossil/cars/cheque/reporté). Dual off-top10 adds Hooibeekhoeve 5.93m / EVA PV 8.63m / Vonk 1.02m + leftover FOI stack.
- Coverage: 1321–1330 is residual dual L5 (APB Hooibeekhoeve · EVA Pluimveehouderij · AGB Blankenberge FOI · Campus Vesta FOI · APB Vonk · Monumentenwacht FOI · Vlabinvest FOI · Zilvermeer FOI · Zorg HH FOI · **EVA Kinderopvang Dilbeek FOI**). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE.
- Next: rq_1331 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1330 write done")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Tick 1331 — APB Vormingscentrum Malle leftover sister APB residual, glossy-only JR2025 FOI.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10.
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1331"
UTC = "2026-08-17T21:50:00Z"
ENT = "apb_pvm"
HIER = "Vlaanderen>Provincies>Antwerpen>APB>VormingscentrumMalle"
GAP = "gap_pvm_jr2025_glossy_not_bbc_l5"
SRC = "src_pvm_docs"
SRC2 = "src_pvm_site"
SRC3 = "src_kbo_pvm_0541412824"
SRC4 = "src_pvm_foi_contact"
SRC_URL = "https://www.provincieantwerpen.be/nl/locaties/provinciaal-vormingscentrum-malle/jaarverslag-en-kwaliteitslabels"
SRC2_URL = "https://www.provincieantwerpen.be/nl/locaties/provinciaal-vormingscentrum-malle"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0541412824"
SRC4_URL = "https://provincieantwerpenleert.be/privacyverklaring/"
FOI_EMAIL = "vormingscentrum@provincieantwerpen.be"
FOI_POSTAL = "Smekenstraat 61 2390 Malle"
DRAFT = "docs/doge/foi/drafts/gap_pvm_jr2025_glossy_not_bbc_l5.md"


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


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "Provincie Antwerpen APB Vormingscentrum Malle jaarverslag-en-kwaliteitslabels (JR2025 glossy listed; no fetchable BBC PDF)",
                "url": SRC_URL,
                "publisher": "Provincie Antwerpen / APB Vormingscentrum Malle",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1331; official PVM page lists Jaarverslag 2025 (554.01 kB) glossy; "
                    "direct provincieantwerpen.be HTTP 403 from this box; no BBC J1-J5 PDF bytes; "
                    "Foleon leftover slugs no PVM hash / redirect Hooibeekhoeve"
                ),
            },
            {
                "source_id": SRC2,
                "title": "APB Vormingscentrum Malle locatiepagina (contact; no JR2025 BBC PDF)",
                "url": SRC2_URL,
                "publisher": "APB Provinciaal Vormingscentrum Malle",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1331; isolated fetch 200 locatiepagina; tel 03 312 80 00; "
                    "vormingscentrum@provincieantwerpen.be; uitleendienst@provincieantwerpen.be; "
                    "Smekenstraat 61 2390 Malle; box fetch 403; no BBC/NBB PDF linked"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO APB Provinciaal Vormingscentrum Malle 0541.412.824",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1331; KBO 0541.412.824 Actief / normale toestand since 26.09.2013; "
                    "statutaire naam APB Provinciaal Vormingscentrum Malle; afkorting APB PVM; "
                    "zetel Smekenstraat 61 2390 Malle; 1 VE; Autonoom provinciebedrijf; "
                    "RSZ-werkgever since 01.01.2022; btw since 01.02.2017; aanbestedende overheid; "
                    "bestuurder Mireille Colson since 02.12.2024; NACE RSZ2025 85.591; "
                    "no KBO e-mail/web/finance; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Provincie Antwerpen Leert privacy / APB entity list (FOI channel PVM)",
                "url": SRC4_URL,
                "publisher": "Provincie Antwerpen",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1331; lists APB PVM 0541.412.824; FOI vormingscentrum@provincieantwerpen.be "
                    "cc openbaarheid@provincieantwerpen.be; Smekenstraat 61 2390 Malle / "
                    "Koningin Elisabethlei 22 2018 Antwerpen"
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
                "name_nl": "Autonoom provinciebedrijf Provinciaal Vormingscentrum Malle (APB PVM)",
                "name_fr": "Entreprise provinciale autonome Centre de formation de Malle",
                "name_en": "Autonomous provincial company Provincial Training Centre Malle",
                "level": "apb",
                "parent_id": "prov_antwerpen",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1331 leftover sister APB residual of mined provincie Antwerpen; "
                    "KBO 0541.412.824 Actief since 26.09.2013; official Jaarverslag 2025 glossy listed "
                    "(554 kB) / provincieantwerpen.be 403; no fetchable JR2025 BBC/NBB PDF; "
                    "no sourced euros; FOI ready; not every-10"
                ),
            },
        ],
    )
    print("entities", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_pvm_jr2025_glossy_not_bbc",
                "title": "APB Vormingscentrum Malle JR2025 glossy-only (no fetchable BBC/NBB PDF; FOI-ready)",
                "entity_id": ENT,
                "beneficiary": "Vorming / jeugdverblijf / uitleendienst Malle + provinciale cursisten",
                "legal_basis": "Provinciedecreet APB; BBC-besluit; Bestuursdecreet openbaarheid",
                "decision_date": "2013-09-26",
                "start_year": "2013",
                "end_year": "2025",
                "total_envelope_eur": "",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "unknown",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover sister APB map VL Antwerpen — vorming/verblijf; BBC/NBB extract missing",
                "cut_option": "Publish BBC JR2025 + RvB/PR + NBB PDF or non-filing rechtsgrond + dual provincie / VTE lines",
                "source_id": SRC3,
                "confidence": "medium",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1331; no sourced euros; glossy jaarverslag listed / no fetchable BBC/NBB PDF; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_pvm_jr2025_glossy_not_bbc",
                "name": "APB Vormingscentrum Malle JR2025 (official glossy jaarverslag listed; no BBC PDF)",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "",
                "total_cost_eur": "",
                "tco_notes": "No primary JR2025 BBC/NBB euros; official Jaarverslag 2025 glossy listed 554 kB; provincieantwerpen.be 403; do not use Belscope/Companyweb/FinCheck",
                "confidence": "medium",
                "source_id": SRC3,
                "beneficiaries": "Vorming / jeugdverblijf / uitleendienst Malle + provinciale cursisten",
                "stated_goal": "Local leftover sister APB map VL Antwerpen — BBC/NBB PDF unpublished",
                "measured_outcome": "KBO 0541.412.824 active; 2026-08-17 official Jaarverslag 2025 glossy listed; no fetchable BBC/NBB PDF bytes",
                "absurdity_score": "6.0",
                "cost_score": "2.0",
                "difficulty": "2.0",
                "priority_index": "5.0",
                "cut_proposal": "Publish BBC JR2025 + RvB/PR + NBB PDF or non-filing rechtsgrond + dual provincie / VTE",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1331; no invented euros; FOI ready not sent; leftover sister APB of mined provincie Antwerpen; not TE-additive of 348bn; not every-10",
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
                    "BBC jaarrekening 2025 APB Provinciaal Vormingscentrum Malle "
                    "(J1-J5 / T2-T5 / BBR / AFM / fin debt / provinciale dotaties / "
                    "vorming+jeugdverblijf+uitleendienst / VTE) + RvB/PR vaststelling + "
                    "NBB filing PDF or non-filing rechtsgrond + dual provincie JR2025 lines. "
                    "Official page lists Jaarverslag 2025 glossy 554 kB; provincieantwerpen.be 403; "
                    "no JR2025 BBC/NBB PDF bytes."
                ),
                "why_it_matters": (
                    "Named leftover unmined sister APB of already-mined provincie Antwerpen "
                    "after honest residual dual hunt. KBO 0541.412.824 Actief. No fetchable JR2025 "
                    "BBC/NBB PDF. APB POA/TPA/De Schorre/Warande/De Nekker 403 / no leftover PDF "
                    "bytes — not taken. Leftover cities still no fetchable JR2025. Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "APB Vormingscentrum Malle / Provincie Antwerpen",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_pvm_jr2025_glossy_not_bbc",
                "linked_leaderboard_id": "lb_pvm_jr2025_glossy_not_bbc",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; no sourced euros; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1331",
        "title": "APB Vormingscentrum Malle JR2025 glossy-only dual residual FOI",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: APB Vormingscentrum Malle leftover sister APB after honest hunt; "
            "KBO 0541.412.824 Actief; no fetchable JR2025 BBC/NBB PDF "
            "(official Jaarverslag 2025 glossy listed / provincieantwerpen.be 403 / "
            "Foleon leftover slugs no PVM hash); no sourced euros; FOI ready"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T21:30:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1331 APB Vormingscentrum Malle leftover sister APB residual; KBO 0541.412.824; "
            "glossy jaarverslag listed / no fetchable BBC/NBB PDF; no sourced euros; FOI ready not sent; next rq_1332 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1332",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1331 done including APB Vormingscentrum Malle 1331 FOI-glossy-not-BBC / "
            "EVA Kinderopvang Dilbeek 1330 FOI-unpublished + every-10 / "
            "Zorg Houthalen 1329 FOI-unpublished / APB Zilvermeer 1328 FOI-unpublished / "
            "APB Vlabinvest 1327 FOI-unpublished / APB Monumentenwacht WVL 1326 FOI-unpublished / "
            "APB Vonk 1325 leftover other-province APB / APB Campus Vesta 1324 FOI-glossy-not-BBC / "
            "AGB Blankenberge 1323 FOI-liquidated JR2019-only / EVA Proefbedrijf Pluimveehouderij 1322 leftover sister EVA / "
            "APB Hooibeekhoeve 1321 leftover sister APB / APB KampC 1320 leftover sister APB + every-10); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / "
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
        "notes": "spawned tick1331 after APB Vormingscentrum Malle leftover sister APB FOI; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1331", rq_new, rq_spawn)
    print("research_queue 1331", found, "spawned_1332", spawned)

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
                "last_unit_id": "rq_1331",
                "ticks_completed": "1331",
                "paused": "no",
                "notes": (
                    "tick1331 APB Vormingscentrum Malle leftover sister APB residual; KBO 0541.412.824; "
                    "no fetchable JR2025 BBC/NBB PDF; no sourced euros; FOI ready; next rq_1332 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1331 - 2026-08-17 - rq_1331 APB Vormingscentrum Malle dual residual glossy-only FOI
- Unit: Autonoom provinciebedrijf Provinciaal Vormingscentrum Malle leftover sister APB of already-mined provincie Antwerpen after residual dual hunt (KBO **0541.412.824**; official jaarverslag-pagina + locatiepagina + KBO; **no fetchable JR2025 BBC/NBB PDF**). PREFER leftover AGB/zorg/EVA/IGS/other-province APB with a live JR2025 BBC/NBB PDF. Official PVM page lists **Jaarverslag 2025** (554.01 kB) glossy/activity — **not BBC J1–J5**. Direct provincieantwerpen.be from this box **HTTP 403**. Foleon leftover slugs (`vormingscentrum-malle-jaarverslag-2025` / `de-schorre-jaarverslag-2025` / `provinciaal-onderwijs-antwerpen-jaarverslag-2025` / `toerisme-provincie-antwerpen-jaarverslag-2025`) no leftover PVM hash / previously **redirect to already-mined Hooibeekhoeve**. KBO Actief / normale toestand since **26.09.2013**; afkorting APB PVM; zetel Smekenstraat 61 2390 Malle; **1 VE**; RSZ-werkgever since 01.01.2022; btw since 01.02.2017; aanbestedende overheid; bestuurder Mireille Colson since 02.12.2024; no KBO e-mail; NACE 85.591 onderwijs voor sociale promotie / 85.593 vormingswerk / 55.100 hotels. Distinct from already-mined Zilvermeer 1328 / Campus Vesta 1324 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317. Hunt leftover AGB first: AGB Bornem official still JR2024-only; AGB De Kluize unpublished; AGB Pelt already mined. Leftover cities Londerzeel official still JR2022–2024 only / Wortegem-Petegem official JR2020–2024 only / Zwalm `/jaarrekening` 404 / Holsbeek 404 / Maarkedal TLS / Linkebeek 404 / Kapellen city GE 404 / Drogenbos 404 / Boutersem archive-only / Maaseik city GE 404 / Bierbeek 404 still no fetchable JR2025. APB POA/TPA/De Schorre/Warande/De Nekker official pages 403 / no leftover PDF bytes; leftover sister APBs PIH / Inovant / Atlas / Arenberg / EVAP Arboretum Kalmthout fondsenverslag-only — not taken. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / Vlabinvest 1327 / Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320. Not an every-10 tick.
- EUR: **none sourced**. Do not invent euros. FOI-ready after honest hunt (no fetchable BBC/NBB PDF).
- CSVs: sources+4/entities+1/commitments+1/leaderboard+1 + FOI ready `gap_pvm_jr2025_glossy_not_bbc_l5` (not sent); no budget rows (no euros); rq_1331=done; spawn rq_1332; ticks=1331. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (APB Vormingscentrum Malle leftover sister APB glossy-not-BBC). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1332 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1331 write done")


if __name__ == "__main__":
    main()

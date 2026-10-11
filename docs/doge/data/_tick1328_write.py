# -*- coding: utf-8 -*-
"""Tick 1328 — APB Zilvermeer leftover sister APB residual, no fetchable BBC/NBB PDF FOI.
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

TICK = "1328"
UTC = "2026-08-17T19:55:00Z"
ENT = "apb_prz"
HIER = "Vlaanderen>Provincies>Antwerpen>APB>Zilvermeer"
GAP = "gap_prz_jr2025_unpublished_l5"
SRC = "src_prz_docs"
SRC2 = "src_prz_site"
SRC3 = "src_kbo_prz_0541413814"
SRC4 = "src_prz_foi_contact"
SRC_URL = "https://www.provincieantwerpen.be/nl/locaties/zilvermeer/besluiten-statuten-rapporten"
SRC2_URL = "https://www.zilvermeer.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0541413814"
SRC4_URL = "https://www.zilvermeer.be/nl/plan-je-bezoek"
FOI_EMAIL = "info@zilvermeer.be"
FOI_POSTAL = "Zilvermeerlaan 2 2400 Mol"
DRAFT = "docs/doge/foi/drafts/gap_prz_jr2025_unpublished_l5.md"


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
                "title": "Provincie Antwerpen APB Zilvermeer besluiten/statuten/rapporten (JR2025 BBC listed 28.05.2026; no fetchable PDF)",
                "url": SRC_URL,
                "publisher": "Provincie Antwerpen / APB Zilvermeer",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1328; public index lists 2 3 apb prz doelstellingenrealisatienota "
                    "jaarrekening 2025 bbc rapport.pdf (28 mei 2026) + MJP-aanpassing 25 juni 2026; "
                    "direct provincieantwerpen.be / koepelsite HTTP 403 from this box; "
                    "Foleon leftover slugs redirect to already-mined Hooibeekhoeve"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Zilvermeer visitor site (JR2024 jaarrapport only; no JR2025 BBC PDF)",
                "url": SRC2_URL,
                "publisher": "APB Provinciaal Recreatiedomein Zilvermeer",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1328; HTTP 200 visitor/recreatie site; live PDF "
                    "sites/zilvermeer/files/2025-10/jaarrapport_apb_prz_2024.pdf is JR2024 glossy "
                    "not mined as JR2025 euros; guessed 2026-0[5-6]/jaarrapport_apb_prz_2025.pdf 404"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO APB Provinciaal Recreatiedomein Zilvermeer 0541.413.814",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1328; KBO 0541.413.814 Actief / normale toestand since 26.09.2013; "
                    "statutaire naam APB Provinciaal Recreatiedomein Zilvermeer; afkorting APB PRZ; "
                    "zetel Zilvermeerlaan 2 2400 Mol; 2 VE; APB; RSZ-werkgever since 01.01.2022; "
                    "btw since 01.01.2014; aanbestedende overheid; bestuurder Mireille Colson since "
                    "02.12.2024; dagelijks bestuur Igor Geubbelmans since 26.11.2020; "
                    "tel 014 82 95 00; e-mail info@zilvermeer.be; web www.zilvermeer.be; "
                    "NACE RSZ2025 93.293; no KBO finance; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Zilvermeer plan-je-bezoek / jaarrapport + KBO e-mail info@zilvermeer.be",
                "url": SRC4_URL,
                "publisher": "APB Provinciaal Recreatiedomein Zilvermeer",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1328; FOI info@zilvermeer.be (KBO); postal Zilvermeerlaan 2 2400 Mol; "
                    "cc openbaarheid@provincieantwerpen.be; jaarrapport link on visitor page "
                    "points to JR2024 PDF only"
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
                "name_nl": "Autonoom provinciebedrijf Provinciaal Recreatiedomein Zilvermeer (APB PRZ)",
                "name_fr": "Régie provinciale autonome Domaine récréatif provincial Zilvermeer",
                "name_en": "Zilvermeer autonomous provincial recreation domain (APB PRZ)",
                "level": "apb",
                "parent_id": "prov_antwerpen",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1328 leftover sister APB residual of mined provincie Antwerpen; "
                    "KBO 0541.413.814 Actief since 26.09.2013; no fetchable JR2025 BBC/NBB PDF "
                    "(provincieantwerpen.be 403 / Foleon leftover slugs redirect Hooibeekhoeve / "
                    "zilvermeer.be JR2024 glossy only); no sourced euros; FOI ready; AD Igor Geubbelmans"
                ),
            },
        ],
    )
    print("entities", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_prz_jr2025_unpublished",
                "title": "APB Zilvermeer JR2025 BBC listed but not fetchable (provincie 403 / Foleon leftover redirect; FOI-ready)",
                "entity_id": ENT,
                "beneficiary": "Provincie Antwerpen / bezoekers recreatiedomein Mol / camping / evenementen",
                "legal_basis": "Provinciedecreet APB; BBC; Bestuursdecreet openbaarheid",
                "decision_date": "2013-09-26",
                "start_year": "2013",
                "end_year": "2025",
                "total_envelope_eur": "",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "unknown",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover sister APB map VL provincie Antwerpen — recreatiedomein Zilvermeer; BBC extract missing",
                "cut_option": "Publish BBC J1-J5/T2-T5 + RVB/PR + NBB or non-filing + dual provincie / VTE lines",
                "source_id": SRC3,
                "confidence": "medium",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1328; no sourced euros; no fetchable BBC/NBB PDF; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_prz_jr2025_unpublished",
                "name": "APB Zilvermeer JR2025 (BBC listed 28.05.2026; no fetchable official PDF)",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "",
                "total_cost_eur": "",
                "tco_notes": "No primary JR2025 BBC/NBB euros; provincieantwerpen.be 403; Foleon leftover redirect; do not use Belscope/Companyweb/FinCheck",
                "confidence": "medium",
                "source_id": SRC3,
                "beneficiaries": "Provincie Antwerpen / bezoekers recreatiedomein Mol / camping / evenementen",
                "stated_goal": "Local leftover sister APB map VL provincie Antwerpen — BBC PDF not fetchable",
                "measured_outcome": "KBO 0541.413.814 active; 2026-08-17 official index lists JR2025 BBC 28.05.2026; no fetchable PDF bytes; JR2024 glossy only",
                "absurdity_score": "6.0",
                "cost_score": "2.0",
                "difficulty": "2.0",
                "priority_index": "5.0",
                "cut_proposal": "Publish BBC J1-J5/T2-T5 + RVB/PR + NBB or non-filing + dual provincie / VTE",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1328; no invented euros; FOI ready not sent; leftover sister APB of mined provincie Antwerpen; not TE-additive of 348bn",
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
                    "BBC jaarrekening 2025 APB Zilvermeer / APB PRZ (J1-J5 / T2-T5 / BBR / AFM / "
                    "fin debt / provincie dotaties / recreatie+camping+evenementen / VTE) + "
                    "RVB/provincieraad vaststelling + NBB filing or non-filing rechtsgrond + "
                    "dual provincie JR2025/2026 lines. Official index lists BBC 2025 "
                    "(28.05.2026); provincieantwerpen.be HTTP 403; Foleon leftover slugs "
                    "redirect to Hooibeekhoeve; zilvermeer.be JR2024 glossy only; no JR2025 PDF bytes."
                ),
                "why_it_matters": (
                    "Named leftover unmined sister APB of already-mined provincie Antwerpen "
                    "after honest residual dual hunt. KBO 0541.413.814 Actief. No fetchable JR2025 "
                    "BBC/NBB PDF. APB POA/TPA/De Schorre also list JR2025 filenames but no leftover "
                    "PDF bytes — not taken. Leftover cities still no fetchable JR2025. "
                    "Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "APB Zilvermeer / Provincie Antwerpen",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_prz_jr2025_unpublished",
                "linked_leaderboard_id": "lb_prz_jr2025_unpublished",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; no sourced euros; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1328",
        "title": "APB Zilvermeer JR2025 unpublished dual residual FOI",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: APB Zilvermeer leftover sister APB after honest hunt; "
            "KBO 0541.413.814 Actief; no fetchable JR2025 BBC/NBB PDF "
            "(provincieantwerpen.be 403 / Foleon leftover slugs redirect Hooibeekhoeve / "
            "zilvermeer.be JR2024 glossy only); no sourced euros; FOI ready"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T19:20:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1328 APB Zilvermeer leftover sister APB residual; KBO 0541.413.814; "
            "no fetchable BBC/NBB PDF; no sourced euros; FOI ready not sent; next rq_1329 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1329",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1328 done including APB Zilvermeer 1328 FOI-unpublished / "
            "APB Vlabinvest 1327 FOI-unpublished / APB Monumentenwacht WVL 1326 FOI-unpublished / "
            "APB Vonk 1325 leftover other-province APB / APB Campus Vesta 1324 FOI-glossy-not-BBC / "
            "AGB Blankenberge 1323 FOI-liquidated JR2019-only / EVA Proefbedrijf Pluimveehouderij 1322 leftover sister EVA / "
            "APB Hooibeekhoeve 1321 leftover sister APB / APB KampC 1320 leftover sister APB + every-10 / "
            "APB Havencentrum 1319 leftover sister APB / APB GKC 1318 leftover sister APB / APB PSES 1317 leftover APB); "
            "APB POA / APB TPA / APB De Schorre / APB Warande listed on provincieantwerpen.be but no PDF bytes — take only if a real PDF downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / APB Campus Vesta 1324 / "
            "AGB Blankenberge 1323 / EVA Proefbedrijf Pluimveehouderij 1322 / APB Hooibeekhoeve 1321 / APB KampC 1320 / "
            "APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 / "
            "AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 / Westtoer; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 (Foleon leftover slugs redirect Hooibeekhoeve); not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1328 after APB Zilvermeer leftover sister APB FOI; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1328", rq_new, rq_spawn)
    print("research_queue 1328", found, "spawned_1329", spawned)

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
                "last_unit_id": "rq_1328",
                "ticks_completed": "1328",
                "paused": "no",
                "notes": (
                    "tick1328 APB Zilvermeer leftover sister APB residual; KBO 0541.413.814; "
                    "no fetchable JR2025 BBC/NBB PDF; no sourced euros; FOI ready; next rq_1329 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1328 - 2026-08-17 - rq_1328 APB Zilvermeer dual residual unpublished FOI
- Unit: Autonoom provinciebedrijf Provinciaal Recreatiedomein Zilvermeer leftover sister APB of already-mined provincie Antwerpen after residual dual hunt (KBO **0541.413.814**; official besluiten/statuten/rapporten + zilvermeer.be + KBO; **no fetchable JR2025 BBC/NBB PDF**). PREFER leftover AGB/zorg/EVA/IGS/other-province APB with a live JR2025 BBC/NBB PDF. Official index lists **2 3 apb prz doelstellingenrealisatienota jaarrekening 2025 bbc rapport.pdf** (pub **28.05.2026**) + MJP-aanpassing 25.06.2026. Direct provincieantwerpen.be / koepelsite **HTTP 403**. Foleon leftover slugs (`de-schorre-jaarverslag-2025` / `zilvermeer-jaarverslag-2025` / `provinciaal-onderwijs-antwerpen-jaarverslag-2025` / `toerisme-provincie-antwerpen-jaarverslag-2025`) **redirect to already-mined Hooibeekhoeve**. zilvermeer.be HTTP 200; live PDF `jaarrapport_apb_prz_2024.pdf` (2025-10, 3.3 MB) is **JR2024 glossy — not mined as JR2025 euros**. Guessed `2026-0[5-6]/jaarrapport_apb_prz_2025.pdf` **404**. KBO Actief / normale toestand since **26.09.2013**; afkorting APB PRZ; zetel Zilvermeerlaan 2 2400 Mol; 2 VE; RSZ-werkgever since 01.01.2022; btw since 01.01.2014; aanbestedende overheid; bestuurder Mireille Colson since 02.12.2024; dagelijks bestuur Igor Geubbelmans since 26.11.2020; tel 014 82 95 00; e-mail info@zilvermeer.be; web www.zilvermeer.be; NACE 93.293; no KBO finance. Distinct from already-mined Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 / Campus Vesta 1324. Hunt leftover AGB first: AGB Pelt official JR2025 PDFs exist but already mined; AGB Bornem official still JR2024-only; AGB De Kluize unpublished. Leftover cities Londerzeel official still JR2022–2024 only (last GR 27.05.2025) / Holsbeek meetingburger JR2024 / Zwalm `/jaarrekening` 404 / Wortegem-Petegem guessed 2025 path 404 / Maarkedal TLS / Kapellen 404 / Drogenbos no JR / Boutersem no JR / Bierbeek no JR2025. Dilbeek city JR2025 PDF exists but already mined. APB POA/TPA/De Schorre/Warande official pages also list JR2025 filenames — no leftover PDF bytes (403 / Foleon redirect); not taken. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB Vlabinvest 1327 / Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317. Not an every-10 tick.
- EUR: **none sourced**. Do not invent euros. FOI-ready after honest hunt (no fetchable BBC/NBB PDF).
- CSVs: sources+4/entities+1/commitments+1/leaderboard+1 + FOI ready `gap_prz_jr2025_unpublished_l5` (not sent); no budget rows (no euros); rq_1328=done; spawn rq_1329; ticks=1328. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (APB Zilvermeer leftover sister APB unpublished). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1329 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1328 write done")


if __name__ == "__main__":
    main()

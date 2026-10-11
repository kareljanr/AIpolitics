# -*- coding: utf-8 -*-
"""Tick 1329 — Zorg Houthalen leftover zorg residual, no fetchable BBC/NBB PDF FOI.
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

TICK = "1329"
UTC = "2026-08-17T20:20:00Z"
ENT = "zorg_hh"
HIER = "Vlaanderen>Limburg>HouthalenHelchteren>Zorg"
GAP = "gap_zorghh_jr2025_unpublished_l5"
SRC = "src_zorghh_docs"
SRC2 = "src_zorghh_site"
SRC3 = "src_kbo_zorghh_0688812935"
SRC4 = "src_zorghh_foi_contact"
SRC_URL = "https://www.houthalen-helchteren.be/beleidsplannen"
SRC2_URL = "https://www.houthalen-helchteren.be/zorg"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0688812935"
SRC4_URL = "https://www.houthalen-helchteren.be/openbaarheid-van-bestuur"
FOI_EMAIL = "info@houthalen-helchteren.be"
FOI_POSTAL = "Pastorijstraat 30 3530 Houthalen-Helchteren"
DRAFT = "docs/doge/foi/drafts/gap_zorghh_jr2025_unpublished_l5.md"


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
                "title": "Houthalen-Helchteren beleidsplannen (Zorg last public BBC JR2023; no JR2025 PDF)",
                "url": SRC_URL,
                "publisher": "Lokaal bestuur Houthalen-Helchteren / Zorg Houthalen-Helchteren",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1329; official index still lists ZORG Jaarrekening 2023 "
                    "(pub 02.10.2024) as latest Zorg BBC; no JR2024/JR2025 Zorg PDF; "
                    "meetingburger JR2025 hits are kerkfabriek advies only"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Zorg Houthalen-Helchteren service page (ouderenzorg/thuiszorg/kinderzorg; no JR2025 BBC PDF)",
                "url": SRC2_URL,
                "publisher": "Welzijnsvereniging Zorg Houthalen-Helchteren",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1329; HTTP 200 service page; leftover zorg of mined Houthalen "
                    "AGB Masterplan/Sport + OCMW; no BBC/NBB PDF linked"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Zorg Houthalen-Helchteren 0688.812.935",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1329; KBO 0688.812.935 Actief / normale toestand since 08.02.2018; "
                    "statutaire naam Zorg Houthalen-Helchteren; Vereniging van OCMW's; "
                    "zetel Pastorijstraat 30 3530 Houthalen-Helchteren; 7 VE; "
                    "RSZ-werkgever since 01.01.2022; kinderopvang since 01.03.2018; "
                    "bestuurder Katrien Timmers since 11.12.2024; tel 011/49 21 95; "
                    "e-mail marcdoumen@houthalen-helchteren.be; NACE RSZ2025 87.101; "
                    "no KBO finance; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Houthalen-Helchteren openbaarheid van bestuur + KBO e-mail",
                "url": SRC4_URL,
                "publisher": "Lokaal bestuur Houthalen-Helchteren",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1329; FOI info@houthalen-helchteren.be; postal Pastorijstraat 30 "
                    "3530 Houthalen-Helchteren; cc KBO e-mail marcdoumen@houthalen-helchteren.be"
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
                "name_nl": "Welzijnsvereniging Zorg Houthalen-Helchteren",
                "name_fr": "Association de CPAS Zorg Houthalen-Helchteren",
                "name_en": "Zorg Houthalen-Helchteren welfare association",
                "level": "zorg",
                "parent_id": "city_houthalen_helchteren",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1329 leftover zorg residual of mined Houthalen-Helchteren; "
                    "KBO 0688.812.935 Actief since 08.02.2018; no fetchable JR2025 BBC/NBB PDF "
                    "(official beleidsplannen last Zorg JR2023 / meetingburger no Zorg JR2025); "
                    "no sourced euros; FOI ready; bestuurder Katrien Timmers"
                ),
            },
        ],
    )
    print("entities", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_zorghh_jr2025_unpublished",
                "title": "Zorg Houthalen-Helchteren JR2025 unpublished (last public Zorg BBC 2023; FOI-ready)",
                "entity_id": ENT,
                "beneficiary": "Ouderen / thuiszorg / kinderzorg / LDC / dorpsrestaurants Houthalen-Helchteren",
                "legal_basis": "Decreet lokaal bestuur welzijnsvereniging; BBC; Bestuursdecreet openbaarheid",
                "decision_date": "2018-02-08",
                "start_year": "2018",
                "end_year": "2025",
                "total_envelope_eur": "",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "unknown",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover zorg map VL Houthalen-Helchteren — ouderenzorg/thuiszorg/kinderzorg; BBC extract missing",
                "cut_option": "Publish BBC J1-J5/T2-T5 + RVB/GR + NBB or non-filing + dual city/OCMW / VTE lines",
                "source_id": SRC3,
                "confidence": "medium",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1329; no sourced euros; no fetchable BBC/NBB PDF; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_zorghh_jr2025_unpublished",
                "name": "Zorg Houthalen-Helchteren JR2025 (last public Zorg BBC 2023; no official 2025 PDF)",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "",
                "total_cost_eur": "",
                "tco_notes": "No primary JR2025 BBC/NBB euros; official last Zorg BBC 2023; do not use Belscope/Companyweb/FinCheck",
                "confidence": "medium",
                "source_id": SRC3,
                "beneficiaries": "Ouderen / thuiszorg / kinderzorg / LDC / dorpsrestaurants Houthalen-Helchteren",
                "stated_goal": "Local leftover zorg map VL Houthalen-Helchteren — BBC PDF unpublished",
                "measured_outcome": "KBO 0688.812.935 active; 2026-08-17 official last Zorg BBC 2023; no fetchable JR2025 PDF bytes",
                "absurdity_score": "6.0",
                "cost_score": "2.0",
                "difficulty": "2.0",
                "priority_index": "5.0",
                "cut_proposal": "Publish BBC J1-J5/T2-T5 + RVB/GR + NBB or non-filing + dual city/OCMW / VTE",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1329; no invented euros; FOI ready not sent; leftover zorg of mined Houthalen; not TE-additive of 348bn",
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
                    "BBC jaarrekening 2025 welzijnsvereniging Zorg Houthalen-Helchteren "
                    "(J1-J5 / T2-T5 / BBR / AFM / fin debt / city-OCMW dotaties / "
                    "ouderenzorg+thuiszorg+kinderzorg+LDC / VTE) + RVB/GR of AV "
                    "vaststelling + NBB filing or non-filing rechtsgrond + dual "
                    "city/OCMW JR2025 lines. Official beleidsplannen last Zorg BBC "
                    "JR2023 (02.10.2024); meetingburger no Zorg JR2025; no JR2025 PDF bytes."
                ),
                "why_it_matters": (
                    "Named leftover unmined zorg of already-mined Houthalen-Helchteren "
                    "after honest residual dual hunt. KBO 0688.812.935 Actief. No fetchable "
                    "JR2025 BBC/NBB PDF. APB POA/TPA/De Schorre/Warande/De Nekker list "
                    "JR2025 filenames but no leftover PDF bytes — not taken. Leftover "
                    "cities still no fetchable JR2025. Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "Zorg Houthalen-Helchteren / Lokaal bestuur Houthalen-Helchteren",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_zorghh_jr2025_unpublished",
                "linked_leaderboard_id": "lb_zorghh_jr2025_unpublished",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; no sourced euros; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1329",
        "title": "Zorg Houthalen JR2025 unpublished dual residual FOI",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Zorg Houthalen-Helchteren leftover zorg after honest hunt; "
            "KBO 0688.812.935 Actief; no fetchable JR2025 BBC/NBB PDF "
            "(official beleidsplannen last Zorg JR2023 / meetingburger no Zorg JR2025); "
            "no sourced euros; FOI ready"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T19:55:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1329 Zorg Houthalen leftover zorg residual; KBO 0688.812.935; "
            "no fetchable BBC/NBB PDF; no sourced euros; FOI ready not sent; next rq_1330 residual dual L5 VL + every-10"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1330",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "EVERY-10 first (ticks_completed will be 1330): refresh progress_every_10_ticks.md + doge_waste_top10_current.md. "
            "THEN residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1329 done including Zorg Houthalen 1329 FOI-unpublished / "
            "APB Zilvermeer 1328 FOI-unpublished / APB Vlabinvest 1327 FOI-unpublished / "
            "APB Monumentenwacht WVL 1326 FOI-unpublished / APB Vonk 1325 leftover other-province APB / "
            "APB Campus Vesta 1324 FOI-glossy-not-BBC / AGB Blankenberge 1323 FOI-liquidated JR2019-only / "
            "EVA Proefbedrijf Pluimveehouderij 1322 leftover sister EVA / APB Hooibeekhoeve 1321 leftover sister APB / "
            "APB KampC 1320 leftover sister APB + every-10 / APB Havencentrum 1319 leftover sister APB / "
            "APB GKC 1318 leftover sister APB / APB PSES 1317 leftover APB); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker listed on provincieantwerpen.be but no PDF bytes — take only if a real PDF downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / APB Campus Vesta 1324 / "
            "AGB Blankenberge 1323 / EVA Proefbedrijf Pluimveehouderij 1322 / APB Hooibeekhoeve 1321 / APB KampC 1320 / "
            "APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 / "
            "AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 / Westtoer; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 (Foleon leftover slugs redirect Hooibeekhoeve); EVERY-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1329 after Zorg Houthalen leftover zorg FOI; next residual dual L5 VL + every-10",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1329", rq_new, rq_spawn)
    print("research_queue 1329", found, "spawned_1330", spawned)

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
                "last_unit_id": "rq_1329",
                "ticks_completed": "1329",
                "paused": "no",
                "notes": (
                    "tick1329 Zorg Houthalen leftover zorg residual; KBO 0688.812.935; "
                    "no fetchable JR2025 BBC/NBB PDF; no sourced euros; FOI ready; next rq_1330 residual dual L5 VL + every-10; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1329 - 2026-08-17 - rq_1329 Zorg Houthalen dual residual unpublished FOI
- Unit: Welzijnsvereniging Zorg Houthalen-Helchteren leftover zorg of already-mined Houthalen-Helchteren (AGB Masterplan 1282 / AGB Sport 1283 / OCMW 1285) after residual dual hunt (KBO **0688.812.935**; official beleidsplannen + zorg page + KBO; **no fetchable JR2025 BBC/NBB PDF**). PREFER leftover AGB/zorg/EVA/IGS/other-province APB with a live JR2025 BBC/NBB PDF. Official beleidsplannen still lists **ZORG Jaarrekening 2023** (pub **02.10.2024**) as latest Zorg BBC. Meetingburger JR2025 hits are **kerkfabriek advies only**. KBO Actief / normale toestand since **08.02.2018**; Vereniging van OCMW's; zetel Pastorijstraat 30 3530 Houthalen-Helchteren; **7 VE** (Administratieve zetel / Campus Vinkenhof / Campus Kinderzorg / LDC Perron Oost / LDC Casino / Dorpsrestaurant Houthalen-Centrum since 26.02.2025 / Dorpsrestaurant Helchteren since 26.02.2025); RSZ-werkgever since 01.01.2022; kinderopvang since 01.03.2018; bestuurder Katrien Timmers since 11.12.2024; tel 011/49 21 95; e-mail marcdoumen@houthalen-helchteren.be; NACE 87.101 RVT; no KBO finance. Distinct from already-mined AGB Masterplan / AGB Sport / OCMW Houthalen. Hunt leftover AGB first: AGB Pelt official JR2025 PDFs exist but already mined; AGB Bornem official still JR2024-only; AGB De Kluize unpublished. Leftover cities Londerzeel official still JR2022–2024 only (last GR 27.05.2025) / Wortegem-Petegem official JR2020–2024 only / Zwalm `/jaarrekening` 404 / Holsbeek / Maarkedal / Linkebeek / Kapellen city GE / Drogenbos / Boutersem / Maaseik city GE / Bierbeek still no fetchable JR2025. Dilbeek/Halle AGB paths TLS. APB POA/TPA/De Schorre/Warande/De Nekker official pages also list JR2025 filenames — no leftover PDF bytes (403 / Foleon leftover slugs redirect Hooibeekhoeve); not taken. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB Zilvermeer 1328 / Vlabinvest 1327 / Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317. Not an every-10 tick.
- EUR: **none sourced**. Do not invent euros. FOI-ready after honest hunt (no fetchable BBC/NBB PDF).
- CSVs: sources+4/entities+1/commitments+1/leaderboard+1 + FOI ready `gap_zorghh_jr2025_unpublished_l5` (not sent); no budget rows (no euros); rq_1329=done; spawn rq_1330; ticks=1329. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (Zorg Houthalen leftover zorg unpublished). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1330 EVERY-10 + residual dual L5 VL JR2025 hole_fill (refresh progress_every_10_ticks.md + doge_waste_top10_current.md first; then prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1329 write done")


if __name__ == "__main__":
    main()

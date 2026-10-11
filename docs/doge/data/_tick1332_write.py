# -*- coding: utf-8 -*-
"""Tick 1332 — EVA Inagro leftover EVA residual, unpublished JR2025 FOI.
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

TICK = "1332"
UTC = "2026-08-17T22:10:00Z"
ENT = "eva_inagro"
HIER = "Vlaanderen>Provincies>WestVlaanderen>EVA>Inagro"
GAP = "gap_inagro_jr2025_unpublished_l5"
SRC = "src_inagro_docs"
SRC2 = "src_inagro_site"
SRC3 = "src_kbo_inagro_0417474241"
SRC4 = "src_inagro_foi_contact"
SRC_URL = "https://inagro.be/nieuws/het-jaar-2025-was-er-een-vol-beweging-bij-inagro-bekijk-ons-videojaarverslag"
SRC2_URL = "https://inagro.be/contact"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0417474241"
SRC4_URL = "https://www.west-vlaanderen.be/over-west-vlaanderen/bestuur-en-beleid/agentschappen"
FOI_EMAIL = "info@inagro.be"
FOI_POSTAL = "Ieperseweg 87 8800 Roeselare"
DRAFT = "docs/doge/foi/drafts/gap_inagro_jr2025_unpublished_l5.md"


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
                "title": "Inagro videojaarverslag 2025 (glossy/activity; no fetchable BBC/NBB PDF)",
                "url": SRC_URL,
                "publisher": "Inagro EVAP vzw",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1332; official Inagro news 03.02.2026 videojaarverslag 2025; "
                    "not BBC J1-J5 / NBB extract; no public JR2025 PDF bytes"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Inagro contactpagina (FOI channel; no JR2025 BBC PDF)",
                "url": SRC2_URL,
                "publisher": "Inagro EVAP vzw",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1332; HTTP 200 contact; tel 051 27 32 00; info@inagro.be; "
                    "Ieperseweg 87 8800 Rumbeke-Beitem; no BBC/NBB PDF linked"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Inagro provinciaal EVAP vzw 0417.474.241",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1332; KBO 0417.474.241 Actief / normale toestand since 22.11.1976; "
                    "statutaire naam Inagro, provinciaal extern verzelfstandigd agentschap "
                    "in privaatrechtelijke vorm; afkorting Inagro, provinciaal EVAP vzw "
                    "since 27.06.2011; zetel Ieperseweg 87 8800 Roeselare since 06.06.1996; "
                    "4 VE; VZW; RSZ-werkgever since 01.04.1977; btw since 01.07.1994; "
                    "aanbestedende overheid; GD Mia Demeulemeester since 25.03.2014; "
                    "24 functiehouders; jaarvergadering mei; no KBO e-mail/web/finance; "
                    "NACE RSZ2025 72.109; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Provincie West-Vlaanderen agentschappen (Inagro listed; FOI channel)",
                "url": SRC4_URL,
                "publisher": "Provincie West-Vlaanderen",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1332; lists Inagro among WVL agencies with Westtoer / Monumentenwacht / "
                    "POM / TUA / Vonk; FOI info@inagro.be cc openbaarheid@west-vlaanderen.be; "
                    "Ieperseweg 87 8800 Roeselare / Koning Leopold III-laan 41 8200 Brugge"
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
                "name_nl": "Inagro, provinciaal extern verzelfstandigd agentschap in privaatrechtelijke vorm (EVA-vzw)",
                "name_fr": "Inagro, agence provinciale autonomisee de droit prive (ASBL)",
                "name_en": "Inagro, provincial externally autonomised agency in private-law form (NPO)",
                "level": "eva",
                "parent_id": "prov_west_vlaanderen",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1332 leftover EVA residual of mined provincie West-Vlaanderen; "
                    "KBO 0417.474.241 Actief since 22.11.1976; official videojaarverslag 2025 "
                    "glossy only; no fetchable JR2025 BBC/NBB PDF; no sourced euros; FOI ready; not every-10"
                ),
            },
        ],
    )
    print("entities", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_inagro_jr2025_unpublished",
                "title": "EVA Inagro JR2025 unpublished (no fetchable BBC/NBB PDF; FOI-ready)",
                "entity_id": ENT,
                "beneficiary": "West-Vlaamse land- en tuinbouwers + Agrotopia / provinciale R&D",
                "legal_basis": "Provinciedecreet EVAP; VZW-wet; Bestuursdecreet openbaarheid",
                "decision_date": "2011-06-27",
                "start_year": "1976",
                "end_year": "2025",
                "total_envelope_eur": "",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "unknown",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover EVA map VL West-Vlaanderen — landbouwonderzoek; BBC/NBB extract missing",
                "cut_option": "Publish BBC/NBB JR2025 + AV/RvB + dual provincie / VTE lines",
                "source_id": SRC3,
                "confidence": "medium",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1332; no sourced euros; videojaarverslag only / no fetchable BBC/NBB PDF; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_inagro_jr2025_unpublished",
                "name": "EVA Inagro JR2025 (official videojaarverslag only; no BBC/NBB PDF)",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "",
                "total_cost_eur": "",
                "tco_notes": "No primary JR2025 BBC/NBB euros; official videojaarverslag 2025 only; NBB consult 403/SPA; do not use Belscope/Companyweb/FinCheck",
                "confidence": "medium",
                "source_id": SRC3,
                "beneficiaries": "West-Vlaamse land- en tuinbouwers + Agrotopia / provinciale R&D",
                "stated_goal": "Local leftover EVA map VL West-Vlaanderen — BBC/NBB PDF unpublished",
                "measured_outcome": "KBO 0417.474.241 active; 2026-08-17 official videojaarverslag 2025 only; no fetchable BBC/NBB PDF bytes",
                "absurdity_score": "6.0",
                "cost_score": "2.0",
                "difficulty": "2.0",
                "priority_index": "5.0",
                "cut_proposal": "Publish BBC/NBB JR2025 + AV/RvB + dual provincie / VTE",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1332; no invented euros; FOI ready not sent; leftover EVA of mined provincie West-Vlaanderen; not TE-additive of 348bn; not every-10",
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
                    "Jaarrekening 2025 Inagro provinciaal EVAP vzw "
                    "(BBC J1-J5 / T2-T5 if applicable / NBB WVV / BBR / AFM / "
                    "provinciale+Vlaamse+EU dotaties / Agrotopia / VTE) + AV/RvB "
                    "vaststelling + NBB filing PDF or non-filing rechtsgrond + dual provincie JR2025 lines. "
                    "Official site videojaarverslag 2025 only; NBB consult 403/SPA; no JR2025 BBC/NBB PDF bytes."
                ),
                "why_it_matters": (
                    "Named leftover unmined EVA of already-mined provincie West-Vlaanderen "
                    "after honest residual dual hunt. KBO 0417.474.241 Actief. No fetchable JR2025 "
                    "BBC/NBB PDF. APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas 403 / "
                    "Foleon leftover slugs redirect Hooibeekhoeve — not taken. Leftover cities still "
                    "no fetchable JR2025. Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "Inagro EVAP vzw / Provincie West-Vlaanderen",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_inagro_jr2025_unpublished",
                "linked_leaderboard_id": "lb_inagro_jr2025_unpublished",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; no sourced euros; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1332",
        "title": "EVA Inagro JR2025 unpublished dual residual FOI",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: EVA Inagro leftover EVA of mined provincie West-Vlaanderen after honest hunt; "
            "KBO 0417.474.241 Actief; no fetchable JR2025 BBC/NBB PDF "
            "(official videojaarverslag 2025 only / NBB consult 403); no sourced euros; FOI ready"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T21:50:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1332 EVA Inagro leftover EVA residual; KBO 0417.474.241; "
            "videojaarverslag only / no fetchable BBC/NBB PDF; no sourced euros; FOI ready not sent; next rq_1333 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1333",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1332 done including EVA Inagro 1332 FOI-unpublished / "
            "APB Vormingscentrum Malle 1331 FOI-glossy-not-BBC / "
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
            "skip already-mined EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / "
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
        "notes": "spawned tick1332 after EVA Inagro leftover EVA FOI; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1332", rq_new, rq_spawn)
    print("research_queue 1332", found, "spawned_1333", spawned)

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
                "last_unit_id": "rq_1332",
                "ticks_completed": "1332",
                "paused": "no",
                "notes": (
                    "tick1332 EVA Inagro leftover EVA residual; KBO 0417.474.241; "
                    "no fetchable JR2025 BBC/NBB PDF; no sourced euros; FOI ready; next rq_1333 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1332 - 2026-08-17 - rq_1332 EVA Inagro dual residual unpublished FOI
- Unit: Inagro, provinciaal extern verzelfstandigd agentschap in privaatrechtelijke vorm (EVA-vzw) leftover EVA of already-mined provincie West-Vlaanderen after residual dual hunt (KBO **0417.474.241**; official contact + videojaarverslag + KBO; **no fetchable JR2025 BBC/NBB PDF**). PREFER leftover AGB/zorg/EVA/IGS/other-province APB with a live JR2025 BBC/NBB PDF. Official Inagro site HTTP 200 still publishes **videojaarverslag 2025** (03.02.2026) — glossy/activity, **not BBC J1–J5**. Member page lists "Balans en jaarrekening 2025" behind login — no public PDF bytes. NBB consult skipped (403/SPA) even though an index lists a 31.12.2025 filing — no PDF bytes. Distinct from already-mined Westtoer / APB Vonk 1325 / Monumentenwacht WVL 1326 / EVA Pluimveehouderij 1322 / EVA Kinderopvang Dilbeek 1330. KBO Actief / normale toestand since **22.11.1976**; afkorting Inagro, provinciaal EVAP vzw since 27.06.2011; zetel Ieperseweg 87 8800 Roeselare; **4 VE**; RSZ-werkgever since 01.04.1977; btw since 01.07.1994; aanbestedende overheid; GD Mia Demeulemeester since 25.03.2014; 24 functiehouders; jaarvergadering mei; no KBO e-mail; NACE 72.109. Hunt leftover AGB first: AGB Bornem official still JR2024-only; AGB De Kluize unpublished; AGB Pelt already mined. Leftover cities Londerzeel official still JR2022–2024 only / Wortegem-Petegem official JR2020–2024 only / Zwalm `/jaarrekening` 404 / Holsbeek 404 / Maarkedal TLS / Linkebeek 404 / Kapellen city GE 404 / Drogenbos 404 / Boutersem archive-only / Maaseik city GE 404 / Bierbeek 404 still no fetchable JR2025. APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas official pages 403 / Foleon leftover slugs redirect already-mined Hooibeekhoeve — not taken. TUA West jaarverslag 2025 glossy-only. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / Vlabinvest 1327 / Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320. Not an every-10 tick.
- EUR: **none sourced**. Do not invent euros. FOI-ready after honest hunt (no fetchable BBC/NBB PDF).
- CSVs: sources+4/entities+1/commitments+1/leaderboard+1 + FOI ready `gap_inagro_jr2025_unpublished_l5` (not sent); no budget rows (no euros); rq_1332=done; spawn rq_1333; ticks=1332. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (EVA Inagro leftover EVA unpublished). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1333 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1332 write done")


if __name__ == "__main__":
    main()

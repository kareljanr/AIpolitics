# -*- coding: utf-8 -*-
"""Tick 1326 — APB Monumentenwacht West-Vlaanderen leftover other-province APB residual, no BBC/NBB PDF FOI.
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

TICK = "1326"
UTC = "2026-08-17T19:05:00Z"
ENT = "apb_mwwvl"
HIER = "Vlaanderen>Provincies>WestVlaanderen>APB>Monumentenwacht"
GAP = "gap_mwwvl_jr2025_unpublished_l5"
SRC = "src_mwwvl_dienst"
SRC2 = "src_mwwvl_kenniswest"
SRC3 = "src_kbo_mwwvl_0553692529"
SRC4 = "src_mwwvl_foi_page"
SRC_URL = "https://www.west-vlaanderen.be/provinciale-diensten/monumentenwacht-west-vlaanderen"
SRC2_URL = "https://www.kenniswest.be/organisatie/monumentenwacht-west-vlaanderen-apb-brugge/77407"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0553692529"
SRC4_URL = "https://www.west-vlaanderen.be/over-west-vlaanderen/contact/openbaarheid-van-bestuur"
FOI_EMAIL = "griffie@west-vlaanderen.be"
FOI_POSTAL = "Koning Leopold III-laan 31 8200 Brugge"
DRAFT = "docs/doge/foi/drafts/gap_mwwvl_jr2025_unpublished_l5.md"


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
                "title": "Provincie West-Vlaanderen dienstpagina Monumentenwacht (tarieven 2026; no JR2025 BBC)",
                "url": SRC_URL,
                "publisher": "Provincie West-Vlaanderen",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1326; HTTP 200; service/tariff page lidmaatschap 40 euro/object from 01.01.2026 "
                    "NOT sourced as JR2025 euros; no BBC/NBB PDF link; agentschap page 403"
                ),
            },
            {
                "source_id": SRC2,
                "title": "KennisWest organisation page APB Monumentenwacht West-Vlaanderen",
                "url": SRC2_URL,
                "publisher": "Provincie West-Vlaanderen / KennisWest",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1326; HTTP 200 last update 11.01.2026; last public jaarverslag listed 2019; "
                    "document listing points to 403 agentschap page; no JR2025 PDF"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Monumentenwacht West-Vlaanderen 0553.692.529",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1326; KBO 0553.692.529 Actief / normale toestand since 01.07.2014; "
                    "zetel Koning Leopold III-laan 31 8200 Brugge; 0 VE; APB; aanbestedende overheid; "
                    "bestuurder Kelly Detavernier since 23.01.2025; tel 050/40 35 70; "
                    "no KBO e-mail/finance/NACE; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Provincie West-Vlaanderen openbaarheid van bestuur / griffie",
                "url": SRC4_URL,
                "publisher": "Provincie West-Vlaanderen",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1326; FOI griffie@west-vlaanderen.be; postal Koning Leopold III-laan 31 8200 Brugge "
                    "/ provinciehuis Koning Leopold III-laan 41 8200 Sint-Andries; "
                    "PR 18.12.2025 AGPT 12 ontbinding agenda (no JR2025 PDF)"
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
                "name_nl": "Autonoom provinciebedrijf Monumentenwacht West-Vlaanderen",
                "name_fr": "Régie provinciale autonome Monumentenwacht Flandre occidentale",
                "name_en": "Monumentenwacht West Flanders autonomous provincial company",
                "level": "apb",
                "parent_id": "prov_west_vlaanderen",
                "community_language": "nl",
                "website": SRC_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1326 leftover other-province APB residual; KBO 0553.692.529 Actief since 01.07.2014; "
                    "no JR2025 BBC/NBB PDF (agentschap 403 / guessed paths 404); KennisWest last JR 2019; "
                    "PR Dec 2025 ontbinding agenda; no sourced euros; FOI ready; BD Kelly Detavernier"
                ),
            },
        ],
    )
    print("entities", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_mwwvl_jr2025_unpublished",
                "title": "APB Monumentenwacht WVL JR2025 BBC unpublished (dissolution Dec 2025 agenda; FOI-ready)",
                "entity_id": ENT,
                "beneficiary": "Provincie West-Vlaanderen / erfgoedeigenaars leden",
                "legal_basis": "Provinciedecreet APB; BBC; Bestuursdecreet openbaarheid",
                "decision_date": "2014-07-01",
                "start_year": "2014",
                "end_year": "2025",
                "total_envelope_eur": "",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "unknown",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover APB map VL provincie West-Vlaanderen — preventief erfgoedonderhoud; BBC extract missing",
                "cut_option": "Publish BBC J1-J5/T2-T5 + RVB/PR + vereffeningsrekening + dual provincie absorption lines",
                "source_id": SRC3,
                "confidence": "medium",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1326; no sourced euros; no BBC/NBB PDF; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_mwwvl_jr2025_unpublished",
                "name": "APB Monumentenwacht WVL JR2025 (no official BBC/NBB PDF; dissolution Dec 2025 agenda)",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "",
                "total_cost_eur": "",
                "tco_notes": "No primary JR2025 BBC/NBB euros; official dienst page tariffs 2026 not mined as JR; do not use Belscope/Companyweb",
                "confidence": "medium",
                "source_id": SRC3,
                "beneficiaries": "Provincie West-Vlaanderen / erfgoedeigenaars leden",
                "stated_goal": "Local leftover APB map VL provincie West-Vlaanderen — BBC PDF missing",
                "measured_outcome": "KBO 0553.692.529 active; 2026-08-17 no BBC/NBB PDF (403/404); KennisWest last JR 2019; PR 18.12.2025 ontbinding agenda",
                "absurdity_score": "6.0",
                "cost_score": "2.0",
                "difficulty": "2.0",
                "priority_index": "5.0",
                "cut_proposal": "Publish BBC J1-J5/T2-T5 + RVB/PR + vereffeningsrekening + dual provincie / VTE",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1326; no invented euros; FOI ready not sent; leftover APB of mined provincie West-Vlaanderen; not TE-additive of 348bn",
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
                    "BBC jaarrekening 2025 APB Monumentenwacht West-Vlaanderen (J1-J5 / T2-T5 / BBR / AFM / "
                    "fin debt / provincie dotaties / VTE) + RVB/provincieraad vaststelling + "
                    "vereffeningsrekening after PR 18.12.2025 ontbinding + NBB filing or non-filing "
                    "rechtsgrond + dual provincie JR2025/2026 absorption lines. Official dienst page "
                    "is tariffs-only; agentschap 403; guessed PDF paths 404; KennisWest last JR 2019."
                ),
                "why_it_matters": (
                    "Named leftover unmined other-province APB of already-mined provincie West-Vlaanderen "
                    "after honest residual dual hunt. KBO 0553.692.529 Actief. No primary JR2025 BBC/NBB "
                    "PDF. APB POA/TPA/De Schorre no PDF bytes; leftover cities still no fetchable JR2025. "
                    "Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "APB Monumentenwacht West-Vlaanderen / Provincie West-Vlaanderen",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_mwwvl_jr2025_unpublished",
                "linked_leaderboard_id": "lb_mwwvl_jr2025_unpublished",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; no sourced euros; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1326",
        "title": "APB Monumentenwacht WVL JR2025 unpublished dual residual FOI",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: APB Monumentenwacht West-Vlaanderen leftover other-province APB after honest hunt; "
            "KBO 0553.692.529 Actief; no JR2025 BBC/NBB PDF (agentschap 403 / guessed paths 404); "
            "KennisWest last JR 2019; PR Dec 2025 ontbinding agenda; no sourced euros; FOI ready"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T18:55:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1326 APB Monumentenwacht WVL leftover other-province APB residual; KBO 0553.692.529; "
            "no BBC/NBB PDF; no sourced euros; FOI ready not sent; next rq_1327 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1327",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1326 done including APB Monumentenwacht WVL 1326 FOI-unpublished / "
            "APB Vonk 1325 leftover other-province APB / APB Campus Vesta 1324 FOI-glossy-not-BBC / "
            "AGB Blankenberge 1323 FOI-liquidated JR2019-only / EVA Proefbedrijf Pluimveehouderij 1322 leftover sister EVA / "
            "APB Hooibeekhoeve 1321 leftover sister APB / APB KampC 1320 leftover sister APB + every-10 / "
            "APB Havencentrum 1319 leftover sister APB / APB GKC 1318 leftover sister APB / APB PSES 1317 leftover APB); "
            "APB POA / APB TPA listed on provincieantwerpen.be but no PDF bytes — take only if a real PDF downloads; "
            "APB De Schorre leftover APB — take only if a JR2025 BBC PDF now downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined APB Monumentenwacht WVL 1326 / APB Vonk 1325 / APB Campus Vesta 1324 / AGB Blankenberge 1323 / "
            "EVA Proefbedrijf Pluimveehouderij 1322 / APB Hooibeekhoeve 1321 / APB KampC 1320 / APB Havencentrum 1319 / "
            "APB GKC 1318 / APB PSES 1317 / Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 / AGB Sport Hulshout 1314 / "
            "AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 / Westtoer; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 (Foleon OK); not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1326 after APB Monumentenwacht WVL leftover other-province APB FOI; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1326", rq_new, rq_spawn)
    print("research_queue 1326", found, "spawned_1327", spawned)

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
                "last_unit_id": "rq_1326",
                "ticks_completed": "1326",
                "paused": "no",
                "notes": (
                    "tick1326 APB Monumentenwacht WVL leftover other-province APB residual; KBO 0553.692.529; "
                    "no JR2025 BBC/NBB PDF; no sourced euros; FOI ready; next rq_1327 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1326 - 2026-08-17 - rq_1326 APB Monumentenwacht WVL dual residual unpublished FOI
- Unit: Autonoom provinciebedrijf Monumentenwacht West-Vlaanderen leftover other-province APB of already-mined provincie West-Vlaanderen after residual dual hunt (KBO **0553.692.529**; official dienst + KennisWest + KBO; **no JR2025 BBC/NBB PDF**). PREFER leftover APB Monumentenwacht only if a BBC/NBB PDF actually downloads. Official dienst page HTTP 200 is tariffs-only (lidmaatschap 40 euro/object from 01.01.2026 — **not** sourced as JR2025 euros). Agentschap page **403**. Guessed `sites/default/files/2026-0[3-6]/Jaarrekening*Monumentenwacht*` **404**. KennisWest HTTP 200 last update **11.01.2026**; last public jaarverslag listed **2019**. KBO Actief / normale toestand since **01.07.2014**; zetel Koning Leopold III-laan 31 8200 Brugge; 0 VE; aanbestedende overheid; bestuurder Kelly Detavernier since 23.01.2025; tel 050/40 35 70; no KBO e-mail/finance/NACE. Provincieraad **18.12.2025** AGPT 12 ontbinding en vereffening (agenda PDF; no JR euros). Distinct from already-mined Westtoer / APB Vonk 1325 / APB VERA 1310 / APB Mercator / Campus Vesta 1324. Hunt leftover AGB first: AGB Bornem / AGB De Kluize already FOI — no new PDF. Leftover cities Londerzeel official still JR2022–2024 only (last GR 27.05.2025) / Holsbeek 404 / Zwalm `/jaarrekening` 404 / Wortegem-Petegem official JR2020–2024 only / Maarkedal TLS / Linkebeek 404 / Kapellen 404 / Drogenbos 404 / Boutersem last JR2020 / Bierbeek 404 still no fetchable JR2025. APB POA/TPA Foleon slug guesses 403 (no hash). APB De Schorre leftover — no JR2025 PDF. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317. Not an every-10 tick.
- EUR: **none sourced**. Do not invent euros. FOI-ready after honest hunt (no BBC/NBB PDF).
- CSVs: sources+4/entities+1/commitments+1/leaderboard+1 + FOI ready `gap_mwwvl_jr2025_unpublished_l5` (not sent); no budget rows (no euros); rq_1326=done; spawn rq_1327; ticks=1326. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (APB Monumentenwacht WVL leftover other-province APB unpublished). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1327 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1326 write done")


if __name__ == "__main__":
    main()

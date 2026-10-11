# -*- coding: utf-8 -*-
"""Tick 1337 — WV Sleutelzorg leftover zorg residual, unpublished JR2025 FOI.
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

TICK = "1337"
UTC = "2026-08-18T00:10:00Z"
ENT = "zorg_sleutelzorg"
HIER = "Vlaanderen>OostVlaanderen>Temse>Zorg>Sleutelzorg"
GAP = "gap_slz_jr2025_unpublished_l5"
SRC = "src_slz_av"
SRC2 = "src_slz_docs"
SRC3 = "src_kbo_slz_0736364909"
SRC4 = "src_slz_foi_contact"
SRC_URL = "https://www.temse.be/besluitenlijst-algemene-vergadering-29-juni-2026"
SRC2_URL = "https://www.temse.be/welzijnsvereniging-sleutelzorg"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0736364909"
SRC4_URL = "https://www.sleutelzorgtemse.be/welzijnsvereniging-sleutelzorg-temse"
FOI_EMAIL = "saskia.boone@sleutelzorgtemse.be"
FOI_POSTAL = "Clement D'hooghelaan 8 9140 Temse"
DRAFT = "docs/doge/foi/drafts/gap_slz_jr2025_unpublished_l5.md"


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
                "title": "WV Sleutelzorg AV 29.06.2026 besluitenlijst (JR2025 goedkeuring; no BBC euros)",
                "url": SRC_URL,
                "publisher": "Lokaal bestuur Temse / WV Sleutelzorg",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1337; AV 29.06.2026 pub 09.07.2026 besluitenlijst only; "
                    "punt 3 Jaarrekening 2025 Goedkeuring; also vrijwillige ontbinding; "
                    "no J1-J5 / T2-T5 / NRC euros"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Temse portal WV Sleutelzorg (bestuursorganen; no JR2025 BBC PDF)",
                "url": SRC2_URL,
                "publisher": "Lokaal bestuur Temse",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1337; HTTP 200; AV / DC / RvB links; bekendmakingen categorie 37; "
                    "RvB 03.06.2026 JR2025 goedkeuring besluitenlijst only; no BBC PDF bytes"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Welzijnsvereniging Sleutelzorg 0736.364.909",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1337; KBO 0736.364.909 Actief / normale toestand since 27.05.2019; "
                    "statutaire naam Welzijnsvereniging Sleutelzorg; afkorting WV Sleutelzorg; "
                    "rechtsvorm Vereniging van OCMW's; zetel Clement D'hooghelaan 8 9140 Temse; "
                    "5 VE; RSZ-werkgever since 01.01.2022; btw since 01.01.2020; "
                    "aanbestedende overheid since 14.10.2019; bestuurder Ingrid Deschepper "
                    "since 16.12.2024; dagelijks bestuur Saskia Boone since 01.09.2021; "
                    "tel 03/710 25 64; e-mail saskia.boone@sleutelzorgtemse.be; "
                    "NACE RSZ2025 87.101 / BTW 88.102 87.101 88.101 87.302 56.112; "
                    "geen KBO financiële gegevens; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Sleutelzorg Temse contact / over-ons (FOI channel; no JR2025 BBC PDF)",
                "url": SRC4_URL,
                "publisher": "WV Sleutelzorg",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1337; HTTP 200 activity/news; thuiszorg/buurtzorg/woonzorg; "
                    "WZC De Reiger + t Blauwhof; LDC De Flamingo; Residentie Elisabeth; "
                    "integratie Zorgpunt Waasland 01.01.2027; tel +32 3 217 28 00; "
                    "no BBC/NBB PDF linked"
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
                "name_nl": "Welzijnsvereniging Sleutelzorg (vereniging van OCMW's)",
                "name_fr": "Association de bien-etre Sleutelzorg (association de CPAS)",
                "name_en": "Welfare association Sleutelzorg (association of PCSWs)",
                "level": "zorg",
                "parent_id": "city_temse",
                "community_language": "nl",
                "website": "https://www.sleutelzorgtemse.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1337 leftover zorg residual of mined Temse (city GE tick1013 / "
                    "AGB Patrimonium tick1202); KBO 0736.364.909 Actief since 27.05.2019; "
                    "AV/RvB 2026 JR2025 approved besluitenlijst only; no fetchable JR2025 "
                    "BBC/NBB PDF; no sourced euros; FOI ready; integrating Zorgpunt Waasland "
                    "01.01.2027; not every-10"
                ),
            },
        ],
    )
    print("entities", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_slz_jr2025_unpublished",
                "title": "WV Sleutelzorg JR2025 unpublished (no fetchable BBC/NBB PDF; FOI-ready)",
                "entity_id": ENT,
                "beneficiary": "Temse / Steendorp ouderen + thuiszorg / WZC De Reiger + t Blauwhof",
                "legal_basis": "Decreet lokaal bestuur WV; Bestuursdecreet openbaarheid",
                "decision_date": "2019-05-27",
                "start_year": "2019",
                "end_year": "2026",
                "total_envelope_eur": "",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "unknown",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover zorg map VL Temse — woonzorg/thuiszorg; BBC/NBB extract missing",
                "cut_option": "Publish BBC/NBB JR2025 + AV/RvB + dual Temse / Zorgpunt Waasland 2027 lines",
                "source_id": SRC3,
                "confidence": "medium",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1337; no sourced euros; AV/RvB besluitenlijst only / no fetchable BBC/NBB PDF; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_slz_jr2025_unpublished",
                "name": "WV Sleutelzorg JR2025 (official AV/RvB besluitenlijst only; no BBC/NBB PDF)",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "",
                "total_cost_eur": "",
                "tco_notes": "No primary JR2025 BBC/NBB euros; official AV 29.06.2026 / RvB 03.06.2026 besluitenlijst only; NBB consult 403/SPA; do not use Belscope/Companyweb/FinCheck",
                "confidence": "medium",
                "source_id": SRC3,
                "beneficiaries": "Temse / Steendorp ouderen + thuiszorg / WZC De Reiger + t Blauwhof",
                "stated_goal": "Local leftover zorg map VL Temse — BBC/NBB PDF unpublished",
                "measured_outcome": "KBO 0736.364.909 active; 2026-08-17 official AV/RvB JR2025 goedkeuring only; no fetchable BBC/NBB PDF bytes",
                "absurdity_score": "6.0",
                "cost_score": "2.0",
                "difficulty": "2.0",
                "priority_index": "5.0",
                "cut_proposal": "Publish BBC/NBB JR2025 + AV/RvB + dual Temse / Zorgpunt Waasland 2027",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1337; no invented euros; FOI ready not sent; leftover zorg of mined Temse; not TE-additive of 348bn; not every-10",
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
                    "Jaarrekening 2025 Welzijnsvereniging Sleutelzorg "
                    "(BBC J1-J5 / T2-T5 / NBB WVV / BBR / AFM / "
                    "gemeente/OCMW Temse werksub / Vlaamse+federale werksubsidies / VTE) + "
                    "volledig RvB 03.06.2026 + AV 29.06.2026 vaststelling + NBB filing PDF "
                    "or non-filing rechtsgrond + dual Temse JR2025 lines + integratie "
                    "Zorgpunt Waasland 01.01.2027 (activa/schulden/personeel/dotaties). "
                    "Official portal besluitenlijst only; NBB consult 403/SPA; no JR2025 BBC/NBB PDF bytes."
                ),
                "why_it_matters": (
                    "Named leftover unmined zorg / welzijnsvereniging of already-mined Temse "
                    "(city GE tick1013 / AGB Patrimonium tick1202) after honest residual dual hunt. "
                    "KBO 0736.364.909 Actief. JR2025 approved AV/RvB 2026 but no fetchable BBC/NBB PDF. "
                    "AGB Wetteren already mined; AGB Bornem still JR2024-only; AGB De Kluize unpublished FOI. "
                    "Zorgband Leie en Schelde / Ter Nethe / Zorgbedrijf Brasschaat still JR2024 only. "
                    "APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas 403 / "
                    "Foleon leftover slugs redirect Hooibeekhoeve — not taken. Leftover cities still "
                    "no fetchable JR2025. Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "WV Sleutelzorg / Lokaal bestuur Temse",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_slz_jr2025_unpublished",
                "linked_leaderboard_id": "lb_slz_jr2025_unpublished",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; no sourced euros; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1337",
        "title": "WV Sleutelzorg JR2025 unpublished dual residual FOI",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: WV Sleutelzorg leftover zorg of mined Temse after honest hunt; "
            "KBO 0736.364.909 Actief; no fetchable JR2025 BBC/NBB PDF "
            "(official AV/RvB 2026 besluitenlijst only / NBB consult 403); no sourced euros; FOI ready"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T23:40:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1337 WV Sleutelzorg leftover zorg residual; KBO 0736.364.909; "
            "AV/RvB besluitenlijst only / no fetchable BBC/NBB PDF; no sourced euros; FOI ready not sent; next rq_1338 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1338",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1337 done including WV Sleutelzorg 1337 leftover zorg FOI-unpublished / "
            "WV Weldenderend 1336 leftover zorg live BBC / WV BVK 1335 leftover zorg live BBC / "
            "WV OPcura 1334 leftover zorg live BBC / WV Het Dak 1333 leftover zorg live BBC / "
            "EVA Inagro 1332 FOI-unpublished / APB Vormingscentrum Malle 1331 FOI-glossy-not-BBC / "
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
            "skip already-mined WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / "
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
        "notes": "spawned tick1337 after WV Sleutelzorg leftover zorg FOI; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1337", rq_new, rq_spawn)
    print("research_queue 1337", found, "spawned_1338", spawned)

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
                "last_unit_id": "rq_1337",
                "ticks_completed": "1337",
                "paused": "no",
                "notes": (
                    "tick1337 WV Sleutelzorg leftover zorg residual; KBO 0736.364.909; "
                    "no fetchable JR2025 BBC/NBB PDF; no sourced euros; FOI ready; next rq_1338 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1337 - 2026-08-18 - rq_1337 WV Sleutelzorg dual residual unpublished FOI
- Unit: Welzijnsvereniging Sleutelzorg (vereniging van OCMW's) leftover zorg of already-mined Temse (city GE tick1013 / AGB Patrimonium tick1202) after residual dual hunt (KBO **0736.364.909**; official Temse AV/RvB besluitenlijst + KBO + sleutelzorgtemse.be; **no fetchable JR2025 BBC/NBB PDF**). PREFER leftover AGB/zorg/EVA/IGS/other-province APB with a live JR2025 BBC/NBB PDF. Official Temse portal HTTP 200 still publishes **besluitenlijst** only: RvB **03.06.2026** and AV **29.06.2026** (pub **09.07.2026**) "Jaarrekening 2025 — Goedkeuring" — no J1–J5 / T2–T5 euros. AV also lists vrijwillige ontbinding. Official Sleutelzorg site is activity/news (integratie Zorgpunt Waasland **01.01.2027**) — not BBC. Guessed `sites/.../jaarrekening*sleutelzorg*` **404**. NBB consult skipped (403/SPA). Distinct from already-mined Zorgpunt Waasland / AGB Patrimonium Temse / city Temse GE / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333. KBO Actief / normale toestand since **27.05.2019**; afkorting WV Sleutelzorg; zetel Clement D'hooghelaan 8 9140 Temse; **5 VE**; RSZ-werkgever since 01.01.2022; btw since 01.01.2020; aanbestedende overheid since 14.10.2019; bestuurder Ingrid Deschepper since 16.12.2024; dagelijks bestuur Saskia Boone since 01.09.2021; tel 03/710 25 64; e-mail saskia.boone@sleutelzorgtemse.be; NACE 87.101 / 88.102. Hunt leftover AGB first: AGB Wetteren already mined tick1231; AGB Ternat already mined; AGB Bornem official still JR2024-only; AGB De Kluize unpublished; AGB Lebbeke ontbonden 01.01.2023. Zorgband Leie en Schelde official still JR2024 only; Ter Nethe JR2024 only; Zorgbedrijf Brasschaat JR2024 only. Leftover cities Londerzeel official still JR2022–2024 only / Wortegem-Petegem official JR2020–2024 only / Zwalm `/jaarrekening` 404 / Holsbeek 404 / Maarkedal TLS / Linkebeek 404 / Kapellen city GE 404 / Drogenbos 404 / Boutersem archive-only / Maaseik city GE 404 / Bierbeek 404 still no fetchable JR2025. APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas official pages 403 / Foleon leftover slugs redirect already-mined Hooibeekhoeve — not taken. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / Vlabinvest 1327 / Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320. Not an every-10 tick.
- EUR: **none sourced**. Do not invent euros. FOI-ready after honest hunt (no fetchable BBC/NBB PDF).
- CSVs: sources+4/entities+1/commitments+1/leaderboard+1 + FOI ready `gap_slz_jr2025_unpublished_l5` (not sent); no budget rows (no euros); rq_1337=done; spawn rq_1338; ticks=1337. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (WV Sleutelzorg leftover zorg unpublished). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1338 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1337 write done")


if __name__ == "__main__":
    main()

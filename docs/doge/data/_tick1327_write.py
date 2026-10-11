# -*- coding: utf-8 -*-
"""Tick 1327 — APB Vlabinvest leftover other-province APB residual, no BBC/NBB PDF FOI.
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

TICK = "1327"
UTC = "2026-08-17T19:20:00Z"
ENT = "apb_vlab"
HIER = "Vlaanderen>Provincies>VlaamsBrabant>APB>Vlabinvest"
GAP = "gap_vlab_jr2025_unpublished_l5"
SRC = "src_vlab_docs"
SRC2 = "src_vlab_over"
SRC3 = "src_kbo_vlab_0549968521"
SRC4 = "src_vlab_foi_contact"
SRC_URL = "https://www.vlaamsbrabant.be/nl/vlabinvest-wonen-en-zorg-vlaams-brabant/over-vlabinvest/over-vlabinvest-documenten"
SRC2_URL = "https://www.vlaamsbrabant.be/nl/vlabinvest-wonen-en-zorg-vlaams-brabant/over-vlabinvest"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0549968521"
SRC4_URL = "https://www.vlaamsbrabant.be/nl/vlabinvest-wonen-en-zorg-vlaams-brabant/contacteer-vlabinvest-apb"
FOI_EMAIL = "info@vlabinvest.be"
FOI_POSTAL = "Provincieplein 1 3010 Leuven"
DRAFT = "docs/doge/foi/drafts/gap_vlab_jr2025_unpublished_l5.md"


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
                "title": "Provincie Vlaams-Brabant Vlabinvest documentenpagina (BBC 2024 latest; no JR2025 PDF)",
                "url": SRC_URL,
                "publisher": "Provincie Vlaams-Brabant / APB Vlabinvest",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1327; public index lists Vlabinvest jaarrekening BBC 2024 "
                    "publicatie 11 juni 2025 as latest; no JR2025 BBC PDF URL; "
                    "direct vlaamsbrabant.be TLS unexpected EOF from this box; "
                    "guessed 2026-06 BBC-2025 paths no bytes"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Over Vlabinvest APB (woon- en zorginfrastructuurbeleid Vlaams-Brabant)",
                "url": SRC2_URL,
                "publisher": "Provincie Vlaams-Brabant / APB Vlabinvest",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1327; official about page; APB since provincieraad 22.10.2013; "
                    "wonen + zorginfrastructuur; vlaamsbrabant.be TLS unexpected EOF "
                    "from this box; listing via public index; no JR2025 euros"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO APB Vlabinvest 0549.968.521",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1327; KBO 0549.968.521 Actief / normale toestand since 22.10.2013; "
                    "statutaire naam Agentschap voor woon- en zorginfrastructuurbeleid "
                    "voor Vlaams-Brabant; afkorting APB Vlabinvest; zetel Provincieplein 1 "
                    "3010 Leuven; 1 VE; APB; RSZ-werkgever since 01.01.2022; "
                    "aanbestedende overheid; dagelijks bestuur Sarah Claeys since 01.03.2021; "
                    "tel 016/26.79.89; fax 016/26.79.85; e-mail info@vlabinvest.be; "
                    "NACE RSZ2025 84.113; no KBO finance/web; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Contacteer Vlabinvest APB / KBO e-mail info@vlabinvest.be",
                "url": SRC4_URL,
                "publisher": "Provincie Vlaams-Brabant / APB Vlabinvest",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1327; FOI info@vlabinvest.be (also on KBO); postal Provincieplein 1 "
                    "3010 Leuven; wonen 016/26.79.89 / zorg 016/26.79.84 zorg@vlabinvest.be; "
                    "vlaamsbrabant.be TLS unexpected EOF from this box"
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
                "name_nl": "Autonoom provinciebedrijf Vlabinvest (Agentschap voor woon- en zorginfrastructuurbeleid voor Vlaams-Brabant)",
                "name_fr": "Régie provinciale autonome Vlabinvest (Agence politique logement et infrastructure de soins Brabant flamand)",
                "name_en": "Vlabinvest autonomous provincial company (housing and care infrastructure Flanders Brabant)",
                "level": "apb",
                "parent_id": "prov_vlaams_brabant",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1327 leftover other-province APB residual; KBO 0549.968.521 Actief since 22.10.2013; "
                    "no JR2025 BBC/NBB PDF (vlaamsbrabant.be TLS / public index still BBC 2024); "
                    "no sourced euros; FOI ready; AD Sarah Claeys"
                ),
            },
        ],
    )
    print("entities", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_vlab_jr2025_unpublished",
                "title": "APB Vlabinvest JR2025 BBC unpublished (public index still BBC 2024; FOI-ready)",
                "entity_id": ENT,
                "beneficiary": "Provincie Vlaams-Brabant / middeninkomens Vlaamse Rand / zorgactoren",
                "legal_basis": "Provinciedecreet APB; BBC; Bestuursdecreet openbaarheid; decreet grond- en woonbeleid Vlaams-Brabant",
                "decision_date": "2013-10-22",
                "start_year": "2013",
                "end_year": "2025",
                "total_envelope_eur": "",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "unknown",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover APB map VL provincie Vlaams-Brabant — betaalbaar wonen + zorginfrastructuur; BBC extract missing",
                "cut_option": "Publish BBC J1-J5/T2-T5 + RVB/PR + NBB or non-filing + dual provincie / financieringsfonds lines",
                "source_id": SRC3,
                "confidence": "medium",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1327; no sourced euros; no BBC/NBB PDF; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_vlab_jr2025_unpublished",
                "name": "APB Vlabinvest JR2025 (no official BBC/NBB PDF; public index still BBC 2024)",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "",
                "total_cost_eur": "",
                "tco_notes": "No primary JR2025 BBC/NBB euros; vlaamsbrabant.be TLS; do not use Belscope/Companyweb/FinCheck",
                "confidence": "medium",
                "source_id": SRC3,
                "beneficiaries": "Provincie Vlaams-Brabant / middeninkomens Vlaamse Rand / zorgactoren",
                "stated_goal": "Local leftover APB map VL provincie Vlaams-Brabant — BBC PDF missing",
                "measured_outcome": "KBO 0549.968.521 active; 2026-08-17 no BBC/NBB PDF (TLS/index BBC 2024); LinkedIn jaarverslag 2025 glossy not mined",
                "absurdity_score": "6.0",
                "cost_score": "2.0",
                "difficulty": "2.0",
                "priority_index": "5.0",
                "cut_proposal": "Publish BBC J1-J5/T2-T5 + RVB/PR + NBB or non-filing + dual provincie / VTE",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1327; no invented euros; FOI ready not sent; leftover APB of mined provincie Vlaams-Brabant; not TE-additive of 348bn",
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
                    "BBC jaarrekening 2025 APB Vlabinvest (J1-J5 / T2-T5 / BBR / AFM / "
                    "fin debt / provincie + financieringsfonds dotaties / wonen + zorgsubsidies / VTE) + "
                    "RVB/provincieraad vaststelling + NBB filing or non-filing rechtsgrond + "
                    "dual provincie JR2025/2026 lines. Public index still BBC 2024 "
                    "(11.06.2025); vlaamsbrabant.be TLS unexpected EOF; no JR2025 PDF bytes."
                ),
                "why_it_matters": (
                    "Named leftover unmined other-province APB of already-mined provincie Vlaams-Brabant "
                    "after honest residual dual hunt. KBO 0549.968.521 Actief. No primary JR2025 BBC/NBB "
                    "PDF. APB POA/TPA/De Schorre no leftover PDF bytes; leftover cities still no fetchable JR2025. "
                    "Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "APB Vlabinvest / Provincie Vlaams-Brabant",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_vlab_jr2025_unpublished",
                "linked_leaderboard_id": "lb_vlab_jr2025_unpublished",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; no sourced euros; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1327",
        "title": "APB Vlabinvest JR2025 unpublished dual residual FOI",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: APB Vlabinvest leftover other-province APB after honest hunt; "
            "KBO 0549.968.521 Actief; no JR2025 BBC/NBB PDF (vlaamsbrabant.be TLS / "
            "public index still BBC 2024 pub 11.06.2025); no sourced euros; FOI ready"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T19:05:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1327 APB Vlabinvest leftover other-province APB residual; KBO 0549.968.521; "
            "no BBC/NBB PDF; no sourced euros; FOI ready not sent; next rq_1328 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1328",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1327 done including APB Vlabinvest 1327 FOI-unpublished / "
            "APB Monumentenwacht WVL 1326 FOI-unpublished / APB Vonk 1325 leftover other-province APB / "
            "APB Campus Vesta 1324 FOI-glossy-not-BBC / AGB Blankenberge 1323 FOI-liquidated JR2019-only / "
            "EVA Proefbedrijf Pluimveehouderij 1322 leftover sister EVA / "
            "APB Hooibeekhoeve 1321 leftover sister APB / APB KampC 1320 leftover sister APB + every-10 / "
            "APB Havencentrum 1319 leftover sister APB / APB GKC 1318 leftover sister APB / APB PSES 1317 leftover APB); "
            "APB POA / APB TPA listed on provincieantwerpen.be but no PDF bytes — take only if a real PDF downloads; "
            "APB De Schorre leftover APB — take only if a JR2025 BBC PDF now downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / APB Campus Vesta 1324 / "
            "AGB Blankenberge 1323 / EVA Proefbedrijf Pluimveehouderij 1322 / APB Hooibeekhoeve 1321 / APB KampC 1320 / "
            "APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 / "
            "AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 / Westtoer; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 (Foleon OK); not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1327 after APB Vlabinvest leftover other-province APB FOI; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1327", rq_new, rq_spawn)
    print("research_queue 1327", found, "spawned_1328", spawned)

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
                "last_unit_id": "rq_1327",
                "ticks_completed": "1327",
                "paused": "no",
                "notes": (
                    "tick1327 APB Vlabinvest leftover other-province APB residual; KBO 0549.968.521; "
                    "no JR2025 BBC/NBB PDF; no sourced euros; FOI ready; next rq_1328 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1327 - 2026-08-17 - rq_1327 APB Vlabinvest dual residual unpublished FOI
- Unit: Autonoom provinciebedrijf Vlabinvest leftover other-province APB of already-mined provincie Vlaams-Brabant after residual dual hunt (KBO **0549.968.521**; official documenten + KBO; **no JR2025 BBC/NBB PDF**). PREFER leftover AGB/zorg/EVA/IGS/other-province APB with a live JR2025 BBC/NBB PDF. Public index still lists **BBC 2024** (pub **11.06.2025**) as latest. Direct vlaamsbrabant.be **TLS unexpected EOF**. Guessed `2026-06/vlabinvest-jaarrekening-BBC-2025*` no bytes. LinkedIn jaarverslag 2025 glossy **not** mined as BBC euros. KBO Actief / normale toestand since **22.10.2013**; statutaire naam Agentschap voor woon- en zorginfrastructuurbeleid voor Vlaams-Brabant; zetel Provincieplein 1 3010 Leuven; 1 VE; RSZ-werkgever since 01.01.2022; aanbestedende overheid; dagelijks bestuur Sarah Claeys since 01.03.2021; tel 016/26.79.89; e-mail info@vlabinvest.be; NACE 84.113; no KBO finance/web. Distinct from already-mined APB VERA 1310 / Westtoer / APB Vonk 1325 / Monumentenwacht WVL 1326. Hunt leftover AGB first: AGB Bornem official still JR2024-only; AGB De Kluize unpublished. Leftover cities Londerzeel official still JR2022–2024 only (last GR 27.05.2025) / Holsbeek no JR2025 / Zwalm `/jaarrekening` 404 / Wortegem-Petegem official JR2020–2024 only / Maarkedal TLS / Kapellen 404 / Drogenbos no JR / Boutersem no JR / Bierbeek no JR2025. APB POA/TPA/De Schorre Foleon slugs redirect to already-mined Hooibeekhoeve (no leftover PDF). NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317. Not an every-10 tick.
- EUR: **none sourced**. Do not invent euros. FOI-ready after honest hunt (no BBC/NBB PDF).
- CSVs: sources+4/entities+1/commitments+1/leaderboard+1 + FOI ready `gap_vlab_jr2025_unpublished_l5` (not sent); no budget rows (no euros); rq_1327=done; spawn rq_1328; ticks=1327. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (APB Vlabinvest leftover other-province APB unpublished). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1328 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1327 write done")


if __name__ == "__main__":
    main()

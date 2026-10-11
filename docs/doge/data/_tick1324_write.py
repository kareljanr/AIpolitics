# -*- coding: utf-8 -*-
"""Tick 1324 — APB Campus Vesta leftover APB residual, glossy-only / no BBC euros FOI.
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

TICK = "1324"
UTC = "2026-08-17T18:40:00Z"
ENT = "apb_cvesta"
HIER = "Vlaanderen>Provincies>Antwerpen>APB>CampusVesta"
GAP = "gap_cvesta_jr2025_glossy_not_bbc_l5"
SRC = "src_cvesta_bedrijfsgegevens"
SRC2 = "src_cvesta_jaarrapport2025_listing"
SRC3 = "src_kbo_cvesta_0822442511"
SRC4 = "src_cvesta_foi_page"
SRC_URL = "https://www.campusvesta.be/nl/bedrijfsgegevens"
SRC2_URL = "https://www.campusvesta.be/nl/bedrijfsgegevens"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0822442511"
SRC4_URL = "https://www.provincieantwerpen.be/nl/provinciebestuur/werking-provincie/provinciegriffier/inzagerecht"
FOI_EMAIL = "info@campusvesta.be"
FOI_POSTAL = "Oostmalsesteenweg 75 2520 Ranst"
DRAFT = "docs/doge/foi/drafts/gap_cvesta_jr2025_glossy_not_bbc_l5.md"


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
                "title": "Campus Vesta bedrijfsgegevens (KBO + jaarrapport-2025 glossy listing)",
                "url": SRC_URL,
                "publisher": "APB Campus Vesta",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1324; HTTP 200; lists jaarrapport-2025 glossy 223.94 MB; "
                    "not BBC J1-J5/T2-T5 text extract; no sourced euros; "
                    "address Oostmalsesteenweg 75 2520 Ranst; KBO 0822.442.511"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Campus Vesta jaarrapport-2025 listing (glossy; not BBC)",
                "url": SRC2_URL,
                "publisher": "APB Campus Vesta",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1324; official bedrijfsgegevens lists jaarrapport-2025 223.94 MB glossy; "
                    "do not mine glossy as BBC euros; no Foleon BBC PDF found"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Autonoom Provinciebedrijf Campus Vesta 0822.442.511",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1324; KBO 0822.442.511 Actief / normale toestand since 19.02.2009; "
                    "zetel Oostmalsesteenweg 75 2520 Ranst; 1 VE; APB; RSZ-werkgever since 01.01.2022; "
                    "BTW since 01.10.2010; aanbestedende overheid; bestuurder Jinnih Beels since 23.01.2025; "
                    "AD Pieter Van Turnhout since 20.10.2021; NACE 2025 BTW 85.401 / RSZ 85.592; "
                    "no KBO e-mail/web/finance; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Provincie Antwerpen inzagerecht / Campus Vesta FOI channel",
                "url": SRC4_URL,
                "publisher": "Provincie Antwerpen",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1324; FOI info@campusvesta.be + openbaarheid@provincieantwerpen.be; "
                    "postal Oostmalsesteenweg 75 2520 Ranst / Koningin Elisabethlei 22 2018; "
                    "provincieantwerpen.be 403 from this box (listing via isolated fetch only)"
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
                "name_nl": "Autonoom Provinciebedrijf Campus Vesta (APB Campus Vesta)",
                "name_fr": "Régie provinciale autonome Campus Vesta (APB Campus Vesta)",
                "name_en": "Campus Vesta autonomous provincial company (APB Campus Vesta)",
                "level": "apb",
                "parent_id": "prov_antwerpen",
                "community_language": "nl",
                "website": SRC_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1324 leftover APB residual; KBO 0822.442.511 Actief since 19.02.2009; "
                    "official jaarrapport-2025 223.94 MB glossy not BBC; no Foleon BBC/NBB PDF; "
                    "no sourced euros; FOI ready; AD Pieter Van Turnhout / BD Jinnih Beels"
                ),
            },
        ],
    )
    print("entities", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_cvesta_jr2025_unpublished",
                "title": "APB Campus Vesta JR2025 BBC unpublished (glossy jaarrapport only; FOI-ready)",
                "entity_id": ENT,
                "beneficiary": "Provincie Antwerpen / hulpdiensten-opleidingen",
                "legal_basis": "Provinciedecreet art. 219 / BBC; Bestuursdecreet openbaarheid",
                "decision_date": "2009-02-19",
                "start_year": "2009",
                "end_year": "",
                "total_envelope_eur": "",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "unknown",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover APB map VL provincie Antwerpen — public glossy jaarrapport; BBC extract missing",
                "cut_option": "Publish BBC J1-J5/T2-T5 + RVB/PR vaststelling + dual provincie dotatie lines",
                "source_id": SRC3,
                "confidence": "medium",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1324; no sourced euros; glossy 223.94 MB not mined as BBC; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_cvesta_jr2025_glossy_not_bbc",
                "name": "APB Campus Vesta JR2025 (official glossy jaarrapport only; no BBC extract)",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "",
                "total_cost_eur": "",
                "tco_notes": "No primary JR2025 BBC/NBB euros; official listing jaarrapport-2025 223.94 MB glossy; do not mine glossy as BBC; do not use Belscope/Companyweb",
                "confidence": "medium",
                "source_id": SRC3,
                "beneficiaries": "Provincie Antwerpen / hulpdiensten-opleidingen",
                "stated_goal": "Local leftover APB map VL provincie Antwerpen — BBC PDF missing",
                "measured_outcome": "KBO 0822.442.511 active; campusvesta.be 2026-08-17 lists jaarrapport-2025 223.94 MB glossy only; no Foleon BBC PDF",
                "absurdity_score": "6.0",
                "cost_score": "2.0",
                "difficulty": "2.0",
                "priority_index": "5.0",
                "cut_proposal": "Publish BBC J1-J5/T2-T5 + RVB/PR + dual provincie dotatie / VTE",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1324; no invented euros; FOI ready not sent; leftover APB of mined provincie Antwerpen; not TE-additive of 348bn",
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
                    "BBC jaarrekening 2025 APB Campus Vesta (J1-J5 / T2-T5 / BBR / AFM / "
                    "fin debt / provincie dotaties / VTE) + RVB/provincieraad vaststelling + "
                    "NBB filing or non-filing rechtsgrond + dual provincie JR2025 lines. "
                    "Official bedrijfsgegevens lists only jaarrapport-2025 glossy 223.94 MB; "
                    "no Foleon BBC text PDF."
                ),
                "why_it_matters": (
                    "Named leftover unmined sister APB of already-mined provincie Antwerpen after "
                    "honest residual dual hunt. KBO 0822.442.511 Actief. Official portal still "
                    "glossy-only. No primary JR2025 BBC/NBB PDF. APB POA/TPA listed but no PDF "
                    "bytes; leftover cities still no fetchable JR2025. Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "APB Campus Vesta / Provincie Antwerpen",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_cvesta_jr2025_unpublished",
                "linked_leaderboard_id": "lb_cvesta_jr2025_glossy_not_bbc",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; no sourced euros; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1324",
        "title": "APB Campus Vesta JR2025 glossy-only dual residual FOI",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: APB Campus Vesta leftover sister APB after honest hunt; KBO 0822.442.511 "
            "Actief; official jaarrapport-2025 223.94 MB glossy not BBC; no Foleon BBC/NBB PDF; "
            "no sourced euros; FOI ready"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T18:25:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1324 APB Campus Vesta leftover APB residual; KBO 0822.442.511; "
            "glossy jaarrapport-2025 only; no BBC euros; FOI ready not sent; next rq_1325 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1325",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1324 done including APB Campus Vesta 1324 FOI-glossy-not-BBC / "
            "AGB Blankenberge 1323 FOI-liquidated JR2019-only / "
            "EVA Proefbedrijf Pluimveehouderij 1322 leftover sister EVA / APB Hooibeekhoeve 1321 leftover sister APB / "
            "APB KampC 1320 leftover sister APB + every-10 / APB Havencentrum 1319 leftover sister APB / "
            "APB GKC 1318 leftover sister APB / APB PSES 1317 leftover APB / Stad+OCMW Ranst 1316 FOI-unpublished / "
            "Stad+OCMW Lievegem 1315 FOI-TLS / AGB Sport Hulshout 1314 FOI-unpublished / AGB Merchtem 1313 FOI-unpublished); "
            "APB POA / APB TPA listed on provincieantwerpen.be but no PDF bytes — take only if a real PDF downloads; "
            "APB De Schorre leftover APB — take only if a JR2025 BBC PDF now downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined APB Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Proefbedrijf Pluimveehouderij 1322 / "
            "APB Hooibeekhoeve 1321 / APB KampC 1320 / APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / "
            "Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / "
            "AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 (Foleon OK); not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1324 after APB Campus Vesta leftover APB FOI; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1324", rq_new, rq_spawn)
    print("research_queue 1324", found, "spawned_1325", spawned)

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
                "last_unit_id": "rq_1324",
                "ticks_completed": "1324",
                "paused": "no",
                "notes": (
                    "tick1324 APB Campus Vesta leftover APB residual; KBO 0822.442.511; "
                    "official jaarrapport-2025 223.94 MB glossy not BBC; no JR2025 BBC/NBB PDF; "
                    "no sourced euros; FOI ready; next rq_1325 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1324 - 2026-08-17 - rq_1324 APB Campus Vesta dual residual glossy-only FOI
- Unit: Autonoom Provinciebedrijf Campus Vesta leftover sister APB of already-mined provincie Antwerpen after residual dual hunt (KBO **0822.442.511**; official bedrijfsgegevens + KBO; **no JR2025 BBC/NBB PDF**). PREFER leftover APB Campus Vesta if a BBC/NBB extract now yields euros. Official campusvesta.be/nl/bedrijfsgegevens HTTP 200 still lists only **jaarrapport-2025** glossy **223.94 MB** — not BBC J1–J5/T2–T5. Do **not** mine the glossy as BBC euros. No Foleon BBC slug (sister leftover APBs used `2025-apb_*.pdf`). KBO Actief / normale toestand since **19.02.2009**; zetel Oostmalsesteenweg 75 2520 Ranst; 1 VE; RSZ-werkgever since 01.01.2022; BTW since 01.10.2010; aanbestedende overheid; bestuurder Jinnih Beels since 23.01.2025; AD Pieter Van Turnhout since 20.10.2021; NACE 2025 BTW 85.401 / RSZ 85.592; no KBO e-mail/finance. APB POA listed provincieantwerpen.be JR2025 28.05.2026 but **no PDF bytes** (listing only). APB TPA `jaarrekening 25 tpa.pdf` 25.06.2026 — same, no download. APB De Schorre leftover APB — no JR2025 PDF (last public BBC 2022). AGB Bornem / AGB De Kluize already FOI — no new PDF. Leftover cities Londerzeel official still JR2022–2024 only (last GR 27.05.2025) / Holsbeek / Zwalm / Wortegem-Petegem / Maarkedal / Linkebeek / Kapellen / Drogenbos / Boutersem / Maaseik GE / Bierbeek still no fetchable JR2025. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 / Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313. Not an every-10 tick.
- EUR: **none sourced**. Do not invent euros. FOI-ready after honest hunt (glossy jaarrapport only; no BBC extract).
- CSVs: sources+4/entities+1/commitments+1/leaderboard+1 + FOI ready `gap_cvesta_jr2025_glossy_not_bbc_l5` (not sent); no budget rows (no euros); rq_1324=done; spawn rq_1325; ticks=1324. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (APB Campus Vesta leftover APB glossy-only). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1325 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1324 write done")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Tick 1323 — AGB Blankenberge leftover AGB residual, JR2019-only / liquidated FOI.
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

TICK = "1323"
UTC = "2026-08-17T18:25:00Z"
ENT = "agb_blankenberge"
CITY = "city_blankenberge"
HIER = "Vlaanderen>Gemeenten>Blankenberge>AGB"
GAP = "gap_agbblb_liquidated_jr2019only_l5"
SRC = "src_agbblb_financien"
SRC2 = "src_agbblb_jr2019_listing"
SRC3 = "src_kbo_agbblb_0877301751"
SRC4 = "src_agbblb_city_foi"
SRC_URL = "https://www.blankenberge.be/bekendmakingen/categorie/17/financien"
SRC2_URL = "https://www.blankenberge.be/jaarrekening-2019---agb-blankenberge"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0877301751"
SRC4_URL = "https://www.blankenberge.be"
FOI_EMAIL = "info@blankenberge.be"
FOI_POSTAL = "J.F. Kennedyplein 1 8370 Blankenberge"
DRAFT = "docs/doge/foi/drafts/gap_agbblb_liquidated_jr2019only_l5.md"


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


def write_draft():
    path = ROOT / "foi/drafts/gap_agbblb_liquidated_jr2019only_l5.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    src = ROOT / "foi/drafts/gap_agbsph_jr2025_unpublished_l5.md"
    text = src.read_text(encoding="utf-8")
    # keep as separate authored file written below
    return path


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "Stad Blankenberge financien bekendmakingen (AGB JR2019 last; city JR2025 live)",
                "url": SRC_URL,
                "publisher": "Stad Blankenberge",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1323; HTTP 200; last AGB jaarrekening listed is 2019; last AGB MJP 2020-2025; "
                    "city JR2025 lokaal bestuur listed 25.06.2026 / GR 23.06.2026 already mined tick998; "
                    "no AGB JR2020-2025 PDF on this page"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Jaarrekening 2019 AGB Blankenberge listing (official; no later AGB JR)",
                "url": SRC2_URL,
                "publisher": "Stad Blankenberge",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1323; official financien index links /jaarrekening-2019---agb-blankenberge "
                    "as last AGB JR; no JR2025 AGB BBC/NBB PDF"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Autonoom Gemeentebedrijf Blankenberge 0877.301.751",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1323; KBO 0877.301.751 STOPGEZET since 21.03.2023 sluiting vereffening; "
                    "start 12.04.2005; zetel J.F. Kennedyplein 1 8370; 0 VE; aanbestedende overheid; "
                    "bestuurders Content Jurgen + Dumery Daphne since 01.01.2014 snapshot; "
                    "no KBO email/NACE/finance; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Stad Blankenberge openbaarheid / city FOI channel",
                "url": SRC4_URL,
                "publisher": "Stad Blankenberge",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1323; FOI info@blankenberge.be / J.F. Kennedyplein 1 8370; "
                    "AD Peter Verheyden / FD Dirk Plompen from city tick998"
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
                "name_nl": "Autonoom Gemeentebedrijf Blankenberge (AGB Blankenberge)",
                "name_fr": "Regie communale autonome Blankenberge (AGB Blankenberge)",
                "name_en": "Blankenberge autonomous municipal company (AGB Blankenberge)",
                "level": "agb",
                "parent_id": CITY,
                "community_language": "nl",
                "website": SRC_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1323 JR2019-only leftover AGB residual; KBO 0877.301.751 STOPGEZET "
                    "21.03.2023 sluiting vereffening; official financien last AGB JR 2019; "
                    "city JR2025 already mined tick998; no sourced euros; FOI ready"
                ),
            },
        ],
    )
    print("entities", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_agbblb_liquidated_jr_unpublished",
                "title": "AGB Blankenberge liquidated 2023 / last official AGB JR 2019 (FOI-ready)",
                "entity_id": ENT,
                "beneficiary": "Lokale besturen West-Vlaanderen / Stad Blankenberge",
                "legal_basis": "Decreet lokaal bestuur art. 242-243 / BBC; Bestuursdecreet openbaarheid",
                "decision_date": "2023-03-21",
                "start_year": "2005",
                "end_year": "2023",
                "total_envelope_eur": "",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "unknown",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local AGB residual map VL Blankenberge — last public AGB JR 2019; KBO closed 2023",
                "cut_option": "Publish final BBC + liquidation slotbalans + successor/asset transfer + city dual lines",
                "source_id": SRC3,
                "confidence": "medium",
                "hierarchy_path": HIER + ">liquidatie_L5",
                "notes": "tick1323; no sourced euros; KBO stopgezet 21.03.2023; official AGB JR2019-only; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_agbblb_liquidated_jr2019only",
                "name": "AGB Blankenberge liquidated 2023 (official last AGB JR 2019; no BBC 2025)",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">liquidatie_L5",
                "annual_cost_eur": "",
                "total_cost_eur": "",
                "tco_notes": "No primary JR2025 euros; KBO stopgezet 21.03.2023 sluiting vereffening; official last AGB JR 2019; do not use Belscope/Companyweb",
                "confidence": "medium",
                "source_id": SRC3,
                "beneficiaries": "Lokale besturen West-Vlaanderen / Stad Blankenberge",
                "stated_goal": "Local AGB residual map VL Blankenberge — PDF missing after liquidation",
                "measured_outcome": "KBO 0877.301.751 closed 21.03.2023; blankenberge.be financien 2026-08-17 last AGB JR 2019; city JR2025 is lokaal bestuur not AGB",
                "absurdity_score": "6.0",
                "cost_score": "2.0",
                "difficulty": "2.0",
                "priority_index": "5.0",
                "cut_proposal": "Publish final BBC + slotbalans + successor transfer + city dual AGB wind-down lines",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1323; no invented euros; FOI ready not sent; leftover AGB of mined city Blankenberge 998; not TE-additive of 348bn",
            }
        ],
    )
    print("leaderboard", n)

    n = append_rows(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": HIER + ">liquidatie_L5",
                "entity_id": ENT,
                "what_is_missing": (
                    "Final BBC jaarrekening AGB Blankenberge after 2019 (J1-J5 / T2-T5 / BBR / AFM / "
                    "fin debt / liquidation slotbalans / asset-liability transfer) + ontbinding/"
                    "vereffening besluiten (KBO sluiting 21.03.2023) + successor mapping to "
                    "Stad+OCMW Blankenberge GE JR2025 lines + confirmation no AGB JR2025 exists. "
                    "Official financien page last AGB JR is 2019; city JR2025 is lokaal bestuur."
                ),
                "why_it_matters": (
                    "Named leftover unmined AGB of already-mined city Blankenberge after honest residual "
                    "dual hunt. KBO 0877.301.751 stopgezet 21.03.2023 sluiting vereffening. Official "
                    "portal still JR2019-only for the AGB. No primary JR2025 BBC/NBB PDF. APB POA/TPA "
                    "listed but provincieantwerpen.be 403 no PDF bytes; Campus Vesta jaarrapport 234MB "
                    "glossy not BBC. Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "Stad Blankenberge / ex-AGB Blankenberge",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_agbblb_liquidated_jr_unpublished",
                "linked_leaderboard_id": "lb_agbblb_liquidated_jr2019only",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; no sourced euros; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1323",
        "title": "AGB Blankenberge JR2019-only liquidated dual residual FOI",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: AGB Blankenberge leftover AGB after honest hunt; KBO 0877.301.751 "
            "STOPGEZET 21.03.2023 sluiting vereffening; official last AGB JR 2019; city JR2025 "
            "is lokaal bestuur already mined; no BBC/NBB JR2025 PDF; no sourced euros; FOI ready"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T18:15:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1323 AGB Blankenberge leftover AGB residual; KBO 0877.301.751 liquidated 21.03.2023; "
            "official AGB JR2019-only; no JR2025 PDF; FOI ready not sent; next rq_1324 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1324",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1323 done including AGB Blankenberge 1323 FOI-liquidated JR2019-only / "
            "EVA Proefbedrijf Pluimveehouderij 1322 leftover sister EVA / APB Hooibeekhoeve 1321 leftover sister APB / "
            "APB KampC 1320 leftover sister APB + every-10 / APB Havencentrum 1319 leftover sister APB / "
            "APB GKC 1318 leftover sister APB / APB PSES 1317 leftover APB / Stad+OCMW Ranst 1316 FOI-unpublished / "
            "Stad+OCMW Lievegem 1315 FOI-TLS / AGB Sport Hulshout 1314 FOI-unpublished / AGB Merchtem 1313 FOI-unpublished); "
            "prefer leftover APB Campus Vesta KBO 0822.442.511 if a BBC/NBB JR2025 PDF now yields euros "
            "(jaarrapport-2025.pdf 234MB glossy lives on campusvesta.be — take only if BBC euros extract); "
            "APB POA / APB TPA listed on provincieantwerpen.be but site 403 — take only if a real PDF downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined AGB Blankenberge 1323 / EVA Proefbedrijf Pluimveehouderij 1322 / "
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
        "notes": "spawned tick1323 after AGB Blankenberge leftover AGB FOI; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1323", rq_new, rq_spawn)
    print("research_queue 1323", found, "spawned_1324", spawned)

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
                "last_unit_id": "rq_1323",
                "ticks_completed": "1323",
                "paused": "no",
                "notes": (
                    "tick1323 AGB Blankenberge leftover AGB residual; KBO 0877.301.751 liquidated 21.03.2023; "
                    "official AGB JR2019-only; no JR2025 PDF; no sourced euros; FOI ready; "
                    "next rq_1324 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1323 - 2026-08-17 - rq_1323 AGB Blankenberge dual residual liquidated FOI
- Unit: Autonoom Gemeentebedrijf Blankenberge (AGB Blankenberge) leftover AGB of already-mined Stad+OCMW Blankenberge after residual dual hunt (KBO **0877.301.751**; official financien page + KBO; **no JR2025 BBC/NBB PDF**). PREFER leftover AGB/zorg/EVA/IGS/other-province APB: first named leftover unmined AGB after live-PDF hunt failed. KBO **Stopgezet** since **21.03.2023** (sluiting vereffening); start **12.04.2005**; zetel J.F. Kennedyplein 1 8370; 0 VE; aanbestedende overheid; bestuurders Jurgen Content + Daphne Dumery since 01.01.2014 (stopzetting snapshot). Official blankenberge.be financien HTTP 200: last AGB JR **2019**; last AGB MJP **2020-2025**; city JR2025 *lokaal bestuur* 25.06.2026 already mined tick 998. Distinct from leftover EVA Klimaatbedrijf Blankenberge CVSO 1005.329.180 (not this unit). NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Hunt leftover PDF first: APB POA listed provincieantwerpen.be JR2025 28.05.2026 but site 403 / no Foleon/direct PDF — listing only, internals not invented. APB TPA / Beleef listed `jaarrekening 25 tpa.pdf` 25.06.2026 — same 403. Campus Vesta leftover APB 0822.442.511 live `jaarrapport-2025.pdf` 234.8MB glossy (not BBC text; no euros extracted) — left for later if BBC yields. AGB Bornem / AGB De Kluize already FOI — no new PDF. Leftover cities Londerzeel JR2022-2024 only / Holsbeek 404 / Zwalm 200 empty / Wortegem-Petegem JR2020-2024 / Maarkedal TLS / Linkebeek 404 / Drogenbos 404 / Boutersem JR2020-only / Bierbeek 404 / Maaseik city GE 404. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 / Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313. Not an every-10 tick.
- EUR: **none sourced**. Do not invent euros. FOI-ready after honest hunt (AGB liquidated 2023; official last AGB JR 2019; no JR2025 PDF).
- CSVs: sources+4/entities+1/commitments+1/leaderboard+1 + FOI ready `gap_agbblb_liquidated_jr2019only_l5` (not sent); no budget rows (no euros); rq_1323=done; spawn rq_1324; ticks=1323. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (AGB Blankenberge leftover AGB liquidated / JR2019-only). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1324 residual dual L5 VL JR2025 hole_fill (prefer leftover APB Campus Vesta if a BBC/NBB JR2025 now yields euros; APB POA / APB TPA only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1323 write done")


if __name__ == "__main__":
    main()

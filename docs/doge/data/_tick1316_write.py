# -*- coding: utf-8 -*-
"""Tick 1316 — surgical append/patch only. Stad+OCMW Ranst JR2025 unpublished FOI-ready."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1316"
UTC = "2026-08-17T17:35:00Z"
ENT = "city_ranst"
HIER = "Vlaanderen>Gemeenten>Ranst"
GAP = "gap_rnst_jr2025_unpublished_l5"
SRC = "src_rnst_jr_page"
SRC2 = "src_kbo_rnst_0207501311"
SRC3 = "src_kbo_ocmw_rnst_0212210462"
SRC4 = "src_rnst_foi_page"
SRC_URL = "https://www.ranst.be/jaarrekening"
SRC2_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207501311"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0212210462"
SRC4_URL = "https://www.ranst.be/openbaarheid-van-bestuur"
FOI_EMAIL = "secretariaat@ranst.be"
FOI_POSTAL = "Gustaaf Peetersstraat 7 2520 Ranst"
DRAFT = "docs/doge/foi/drafts/gap_rnst_jr2025_unpublished_l5.md"


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


n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Ranst official jaarrekening page still JR2024-only (no JR2025 PDF)",
            "url": SRC_URL,
            "publisher": "Gemeente Ranst",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1316; official page lists only JR2024 gemeente+OCMW PDF "
                "GR 26.05.2025 pub 27.05.2025 21.8MB; no JR2025 BBC/NBB PDF; "
                "meetingburger HandleFile probe was 2021 kwartaalrapport; no sourced euros"
            ),
        },
        {
            "source_id": SRC2,
            "title": "KBO Gemeente Ranst 0207.501.311",
            "url": SRC2_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1316; KBO 0207.501.311 actief stad/gemeente since 01.01.1968; "
                "zetel Gustaaf Peetersstraat 7 2520; 12 VE; AD Wim Van der Schoot "
                "since 07.06.2018; burgemeester Bart Goris since 05.12.2024; "
                "NACE 84.114; info@ranst.be; no KBO finance"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO OCMW Ranst 0212.210.462",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1316; KBO 0212.210.462 actief OCMW since 01.01.1968; "
                "zetel Schildesteenweg 16 2520 since 01.01.2005; 4 VE; "
                "voorzitter Bart Goris since 05.12.2024; NACE 84.115; no KBO finance"
            ),
        },
        {
            "source_id": SRC4,
            "title": "Ranst openbaarheid van bestuur (FOI channel)",
            "url": SRC4_URL,
            "publisher": "Gemeente Ranst",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1316; FOI schriftelijk via secretariaat@ranst.be / thuisloket; "
                "Gustaaf Peetersstraat 7 2520; T 03 470 10 86"
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
            "name_nl": "Gemeente Ranst",
            "name_fr": "Commune de Ranst",
            "name_en": "Municipality of Ranst",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.ranst.be",
            "foi_email": FOI_EMAIL,
            "foi_postal": FOI_POSTAL,
            "notes": (
                "tick1316 JR2025 leftover city GE residual; KBO 0207.501.311 / OCMW 0212.210.462; "
                "official page still JR2024-only; no JR2025 PDF; no sourced euros; FOI ready"
            ),
        },
    ],
)
print("entities", n)

n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": "comm_rnst_jr2025_unpublished",
            "title": "Stad+OCMW Ranst JR2025 leftover city GE unpublished (FOI-ready)",
            "entity_id": ENT,
            "beneficiary": "Lokale besturen Antwerpen / Gemeente Ranst",
            "legal_basis": "Decreet lokaal bestuur / BBC; Bestuursdecreet openbaarheid",
            "decision_date": "",
            "start_year": "2025",
            "end_year": "2031",
            "total_envelope_eur": "",
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "unknown",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE residual map VL JR2025 Ranst — official page JR2024-only",
            "cut_option": "Publish working BBC JR2025 PDF + documentatie + GR/RMW vaststelling",
            "source_id": SRC,
            "confidence": "medium",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": "tick1316; no sourced euros; official page JR2024-only; FOI ready not sent",
        }
    ],
)
print("commitments", n)

n = append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": "lb_rnst_jr2025_unpublished",
            "name": "Stad+OCMW Ranst JR2025 leftover city GE, official page still JR2024-only",
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": HIER + ">jr2025_L5",
            "annual_cost_eur": "",
            "total_cost_eur": "",
            "tco_notes": "No primary JR2025 euros; do not use Belscope/Companyweb or press euros",
            "confidence": "medium",
            "source_id": SRC,
            "beneficiaries": "Lokale besturen Antwerpen / Gemeente Ranst",
            "stated_goal": "Local GE residual map VL JR2025 Ranst — official page JR2024-only",
            "measured_outcome": "Official ranst.be/jaarrekening 2026-08-17 still JR2024-only; no JR2025 PDF bytes",
            "absurdity_score": "6.0",
            "cost_score": "2.0",
            "difficulty": "3.0",
            "priority_index": "5.0",
            "cut_proposal": "Publish working BBC JR2025 PDF + documentatie + GR/RMW",
            "status": "active",
            "struck_reason": "",
            "notes": "tick1316; no invented euros; FOI ready not sent; leftover unmapped city GE; not TE-additive of 348bn",
        }
    ],
)
print("leaderboard", n)

n = append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": HIER + ">jr2025_L5",
            "entity_id": ENT,
            "what_is_missing": (
                "Working downloadable BBC jaarrekening 2025 Stad+OCMW Ranst "
                "(beleidsrapport + documentatie + J1-J7 / T-tables / BBR / AFM / "
                "fin debt / new loans / GE-OCMW tussenkomst / toelagen / pers VTE) "
                "+ GR/RMW vaststelling. Official page still lists only JR2024 "
                "(GR 26.05.2025 / pub 27.05.2025); no JR2025 PDF bytes on 2026-08-17."
            ),
            "why_it_matters": (
                "Leftover unmapped city GE after honest residual dual hunt. "
                "KBO 0207.501.311 / 0212.210.462 active. Official portal JR2024-only. "
                "Sister leftovers Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/"
                "Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek still no "
                "fetchable JR2025 PDF. Do not invent euros."
            ),
            "priority": "8",
            "recipient_body": "Gemeente Ranst / College van burgemeester en schepenen",
            "recipient_email": FOI_EMAIL,
            "recipient_postal": FOI_POSTAL,
            "draft_letter_path": DRAFT,
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_rnst_jr2025_unpublished",
            "linked_leaderboard_id": "lb_rnst_jr2025_unpublished",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; no sourced euros; not every-10",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1316",
    "title": "Stad+OCMW Ranst JR2025 dual residual unpublished FOI",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Ranst JR2025 leftover city GE after honest hunt; "
        "KBO 0207.501.311 / 0212.210.462; official page still JR2024-only; "
        "no BBC/NBB JR2025 PDF; no sourced euros; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T17:25:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1316 Stad+OCMW Ranst JR2025 leftover city GE residual; KBO 0207.501.311/0212.210.462; "
        "official page JR2024-only; no JR2025 PDF; FOI ready not sent; next rq_1317 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1317",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1316 done including Stad+OCMW Ranst 1316 FOI-unpublished / "
        "Stad+OCMW Lievegem 1315 FOI-TLS / AGB Sport Hulshout 1314 FOI-unpublished / "
        "AGB Merchtem 1313 FOI-unpublished / AGBIM Maaseik 1312 / AGB Maaseik 1311 / "
        "APB VERA 1310 / EVA Hoeve Holleken 1309 / Stad+OCMW Beerse 1308 / AGB Beerse 1307); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML "
        "(AGB Bornem / AGB De Kluize / AGB Blankenberge only if a PDF actually downloads); "
        "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
        "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
        "skip already-mined Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 (FOI TLS) / "
        "AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / "
        "APB VERA 1310 / EVA Hoeve Holleken 1309 / Stad+OCMW Beerse 1308 / AGB Beerse 1307 / "
        "Ternat / Oostkamp / Wetteren / Poperinge / Haacht / Bilzen-Hoeselt / AGB Sport Geel / Zwevegem; "
        "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
        "vlaamsbrabant.be TLS + lievegem.be TLS; not every-10"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1316 after Stad+OCMW Ranst JR2025 unpublished FOI; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1316", rq_new, rq_spawn)
print("research_queue 1316", found, "spawned_1317", spawned)

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
            "last_unit_id": "rq_1316",
            "ticks_completed": "1316",
            "paused": "no",
            "notes": (
                "tick1316 Stad+OCMW Ranst JR2025 leftover residual; KBO 0207.501.311/0212.210.462; "
                "official page still JR2024-only; no PDF; no sourced euros; "
                "FOI ready; next rq_1317 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log_entry = """
### Tick 1316 - 2026-08-17 - rq_1316 Stad+OCMW Ranst dual residual unpublished FOI
- Unit: Gemeente + OCMW Ranst JR2025 leftover city GE after residual dual hunt (KBO **0207.501.311** / **0212.210.462**; official jaarrekening page + KBO). Official page still lists only JR2024 (GR **26.05.2025**, published **27.05.2025**, 21.8 MB). Meeting.burger HandleFile probe was **2021 kwartaalrapport**, not JR2025. **No JR2025 PDF bytes / no sourced euros.** AD Wim Van der Schoot since 07.06.2018; burgemeester + OCMW-voorzitter Bart Goris since 05.12.2024; 12+4 VE; FOI secretariaat@ranst.be / Gustaaf Peetersstraat 7 2520. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Press HLN 25.06.2026 (GR June discussion) **not used as sourced euros**. Hunt leftover AGB/zorg/EVA first: Herk-de-Stad/Menen/Knokke AGSO/Vilvoorde/Rivierenland already mined; AGB Bornem JR2024-only (FOI already); AGB De Kluize unpublished (FOI already); AGB Blankenberge official JR2019-only. Leftover cities: Londerzeel JR2022-2024 only; Holsbeek/Zwalm/Linkebeek/Kapellen/Drogenbos/Boutersem 404; Wortegem-Petegem official JR2020-2024; Maarkedal no JR2025 PDF; Maaseik city GE last official JR2024; Bierbeek 2018-2019. Skip already-mined Ternat/Oostkamp/Wetteren/Poperinge/Haacht/Bilzen/Geel/Zwevegem + Lievegem 1315 TLS / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM/AGB Maaseik 1311-1312. Not an every-10 tick.
- EUR: **none sourced**. Do not invent euros. FOI-ready after honest hunt (no leftover AGB/zorg/EVA/IGS JR2025 PDF downloaded; leftover city Ranst official still JR2024-only).
- CSVs: sources+4/entities+1/commitments+1/leaderboard+1 + FOI ready `gap_rnst_jr2025_unpublished_l5` (not sent); no budget rows (no euros); rq_1316=done; spawn rq_1317; ticks=1316. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (Ranst leftover city GE unpublished). Does not move L5 near-complete of 347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1317 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE / AGB Bornem / AGB De Kluize / AGB Blankenberge only if a PDF now downloads; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 unless a fetchable JR appears).
"""
log = ROOT / "loop_log.md"
with log.open("a", encoding="utf-8") as f:
    f.write(log_entry)
print("loop_log ok")
print("tick1316 write done")

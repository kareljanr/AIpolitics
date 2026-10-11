# -*- coding: utf-8 -*-
"""Tick 1315 — surgical append/patch only. Stad+OCMW Lievegem JR2025 TLS FOI-ready."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1315"
UTC = "2026-08-17T17:25:00Z"
ENT = "city_lievegem"
HIER = "Vlaanderen>Gemeenten>Lievegem"
GAP = "gap_lvgm_jr2025_tls_nodownload_l5"
SRC = "src_lvgm_jr_page"
SRC2 = "src_kbo_lvgm_0697609152"
SRC3 = "src_kbo_ocmw_lvgm_0697663986"
SRC4 = "src_lvgm_foi_page"
SRC_URL = "https://www.lievegem.be/bestuur/beleid/jaarrekening"
SRC2_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0697609152"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0697663986"
SRC4_URL = "https://www.lievegem.be/toegang-tot-bestuursdocumenten"
FOI_EMAIL = "financien@lievegem.be"
FOI_POSTAL = "Kasteeldreef 72 9920 Lievegem"
DRAFT = "docs/doge/foi/drafts/gap_lvgm_jr2025_tls_nodownload_l5.md"


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
            "title": "Lievegem official jaarrekeningen page lists JR2025 (TLS blocks download)",
            "url": SRC_URL,
            "publisher": "Gemeente Lievegem",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1315; isolated fetch lists JR2025_beleidsrapport + JR2025_documentatie "
                "GR 25.06.2026 published 26.06.2026; HTTPS from this box TLS unexpected EOF; "
                "no PDF bytes; no sourced euros"
            ),
        },
        {
            "source_id": SRC2,
            "title": "KBO Gemeente Lievegem 0697.609.152",
            "url": SRC2_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1315; KBO 0697.609.152 actief stad/gemeente since 01.06.2018; "
                "zetel Centrumstraat 42 9920 since 26.03.2026; 40 VE; AD Kenneth Pauwels "
                "since 01.06.2024; NACE 84.114/84.120; slorpte Lovendegem/Waarschoot/Zomergem "
                "01.01.2019; no KBO finance"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO OCMW Lievegem 0697.663.986",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1315; KBO 0697.663.986 actief OCMW since 01.06.2018; same zetel; "
                "18 VE; AD Kenneth Pauwels since 01.06.2024; NACE 84.115; no KBO finance"
            ),
        },
        {
            "source_id": SRC4,
            "title": "Lievegem toegang tot bestuursdocumenten (FOI channel)",
            "url": SRC4_URL,
            "publisher": "Gemeente Lievegem",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1315; FOI via College CBS Kasteeldreef 72 9920 / thuisloket; "
                "financien@lievegem.be Bart Kerkhof 09 396 23 00"
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
            "name_nl": "Gemeente Lievegem",
            "name_fr": "Commune de Lievegem",
            "name_en": "Municipality of Lievegem",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.lievegem.be",
            "foi_email": FOI_EMAIL,
            "foi_postal": FOI_POSTAL,
            "notes": (
                "tick1315 JR2025 leftover city GE residual; KBO 0697.609.152 / OCMW 0697.663.986; "
                "official page lists JR2025 GR 25.06.2026 pub 26.06.2026; TLS unexpected EOF "
                "blocks PDF download; no sourced euros; FOI ready"
            ),
        },
    ],
)
print("entities", n)

n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": "comm_lvgm_jr2025_tls",
            "title": "Stad+OCMW Lievegem JR2025 BBC listed but TLS-blocked (FOI-ready)",
            "entity_id": ENT,
            "beneficiary": "Lokale besturen Oost-Vlaanderen / Gemeente Lievegem",
            "legal_basis": "Decreet lokaal bestuur / BBC; Bestuursdecreet openbaarheid",
            "decision_date": "2026-06-25",
            "start_year": "2025",
            "end_year": "2031",
            "total_envelope_eur": "",
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "unknown",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE residual map VL JR2025 Lievegem — PDF listed, TLS blocks download",
            "cut_option": "Publish working BBC JR2025 PDF + documentatie + GR/RMW vaststelling",
            "source_id": SRC,
            "confidence": "medium",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": "tick1315; no sourced euros; official page lists JR2025; TLS EOF; FOI ready not sent",
        }
    ],
)
print("commitments", n)

n = append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": "lb_lvgm_jr2025_tls",
            "name": "Stad+OCMW Lievegem JR2025 listed on official page, TLS blocks PDF",
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": HIER + ">jr2025_L5",
            "annual_cost_eur": "",
            "total_cost_eur": "",
            "tco_notes": "No primary JR2025 euros; do not use Belscope/Companyweb; page lists GR 25.06.2026",
            "confidence": "medium",
            "source_id": SRC,
            "beneficiaries": "Lokale besturen Oost-Vlaanderen / Gemeente Lievegem",
            "stated_goal": "Local GE residual map VL JR2025 Lievegem — PDF listed, TLS blocks download",
            "measured_outcome": "JR2025 listed on lievegem.be 2026-08-17; HTTPS TLS unexpected EOF; no PDF bytes",
            "absurdity_score": "6.0",
            "cost_score": "2.0",
            "difficulty": "3.0",
            "priority_index": "5.0",
            "cut_proposal": "Publish working BBC JR2025 PDF + documentatie + GR/RMW",
            "status": "active",
            "struck_reason": "",
            "notes": "tick1315; no invented euros; FOI ready not sent; leftover unmapped city GE; not TE-additive of 348bn",
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
                "Working downloadable BBC jaarrekening 2025 Stad+OCMW Lievegem "
                "(JR2025_beleidsrapport + JR2025_documentatie listed GR 25.06.2026 / "
                "published 26.06.2026) + J1-J7 / T-tables / BBR / AFM / fin debt / new loans / "
                "GE-OCMW tussenkomst / toelagen / pers VTE + GR/RMW vaststelling. Official page "
                "lists the files; HTTPS from this box TLS unexpected EOF; echo 403; no PDF bytes "
                "on 2026-08-17."
            ),
            "why_it_matters": (
                "First leftover unmapped city GE where official site now lists JR2025 after "
                "honest residual dual hunt. KBO 0697.609.152 / 0697.663.986 active fusion "
                "Lovendegem+Waarschoot+Zomergem. PDF does not download (TLS unexpected EOF). "
                "Sister leftovers Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Ranst/"
                "Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE still no fetchable JR2025 PDF. "
                "Do not invent euros."
            ),
            "priority": "8",
            "recipient_body": "Gemeente Lievegem / College van burgemeester en schepenen",
            "recipient_email": FOI_EMAIL,
            "recipient_postal": FOI_POSTAL,
            "draft_letter_path": DRAFT,
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_lvgm_jr2025_tls",
            "linked_leaderboard_id": "lb_lvgm_jr2025_tls",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; no sourced euros; not every-10",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1315",
    "title": "Stad+OCMW Lievegem JR2025 dual residual TLS FOI",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Lievegem JR2025 listed on official page after honest hunt; "
        "KBO 0697.609.152 / 0697.663.986; GR 25.06.2026 pub 26.06.2026; TLS unexpected EOF "
        "blocks PDF; no sourced euros; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T17:10:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1315 Stad+OCMW Lievegem JR2025 leftover city GE residual; KBO 0697.609.152/0697.663.986; "
        "official page lists JR2025; TLS EOF no PDF; FOI ready not sent; next rq_1316 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1316",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1315 done including Stad+OCMW Lievegem 1315 FOI-TLS / AGB Sport Hulshout 1314 "
        "FOI-unpublished / AGB Merchtem 1313 FOI-unpublished / AGBIM Maaseik 1312 / AGB Maaseik 1311 / "
        "APB VERA 1310 / EVA Hoeve Holleken 1309 / Stad+OCMW Beerse 1308 / AGB Beerse 1307); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML "
        "(AGB Bornem / AGB De Kluize only if a PDF actually downloads); "
        "leftover Maarkedal/Londerzeel/Holsbeek/Merchtem city GE/Zwalm/Wortegem-Petegem still unmined — take only if PDF fetches; "
        "leftover city Linkebeek GE still JR2024-only; leftover Ranst official still JR2024; "
        "leftover Kapellen city GE not published; leftover Drogenbos/Boutersem/Schelle city GE JR2024-only; "
        "leftover Oosterzele no BBC PDF; leftover Stad+OCMW Maaseik GE unmined; leftover AGB Blankenberge JR2019-only; "
        "skip already-mined Stad+OCMW Lievegem 1315 (FOI TLS) / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / "
        "AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 / EVA Hoeve Holleken 1309 / Stad+OCMW Beerse 1308 / "
        "AGB Beerse 1307 / AGB Herne 1122 / AGB Gooik 1121 / AGB Bocholt 1135 / AGB Bree 1166 / AGB Lanaken 1120 / "
        "city Hulshout 1050 / Ternat 1073/1124 / Oostkamp 909/1131 / Wetteren 1011/1231; "
        "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
        "skip AGB Kapellen / AGB Lokeren 1200 / EVA Gezinswelzijn 1253 / AGB Genk / ZOG Genk 1242; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF + "
        "vlaamsbrabant.be TLS unexpected-EOF + lievegem.be TLS unexpected-EOF (page lists JR2025); not every-10"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1315 after Stad+OCMW Lievegem JR2025 TLS FOI; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1315", rq_new, rq_spawn)
print("research_queue 1315", found, "spawned_1316", spawned)

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
            "last_unit_id": "rq_1315",
            "ticks_completed": "1315",
            "paused": "no",
            "notes": (
                "tick1315 Stad+OCMW Lievegem JR2025 leftover residual; KBO 0697.609.152/0697.663.986; "
                "official page lists JR2025 GR 25.06.2026; TLS unexpected EOF no PDF; no sourced euros; "
                "FOI ready; next rq_1316 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log_entry = """
### Tick 1315 - 2026-08-17 - rq_1315 Stad+OCMW Lievegem dual residual TLS FOI
- Unit: Gemeente + OCMW Lievegem JR2025 leftover city GE after residual dual hunt (KBO **0697.609.152** / **0697.663.986**; official jaarrekeningen page + KBO). Official page **lists** JR2025_beleidsrapport + JR2025_documentatie (GR **25.06.2026**, published **26.06.2026**). Direct HTTPS download from this box **TLS unexpected EOF** (http 301 then OpenSSL UNEXPECTED_EOF_WHILE_READING; echo portal 403). **No JR2025 PDF bytes / no sourced euros.** Fusion 01.01.2019 Lovendegem+Waarschoot+Zomergem; zetel Centrumstraat 42 9920 since 26.03.2026; AD Kenneth Pauwels since 01.06.2024; 40+18 VE; financieel directeur Bart Kerkhof financien@lievegem.be. FOI post Kasteeldreef 72 9920. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Hunt leftover cities: Londerzeel `/jaarrekeningen` 200 only JR2022 PDF; Holsbeek JR2024-only; Zwalm HLN 23.06.2026 no official PDF echo 403; Wortegem-Petegem no JR2025; Maarkedal official JR2020-2024 only; Ranst official JR2024; Linkebeek JR2024; Kapellen no JR PDF; Drogenbos/Boutersem 404; Maaseik city GE JR2024-only; Bierbeek JR2024; Moerbeke→Lokeren / Wachtebeke→Lochristi already mined. AGB Bornem JR2024-only; AGB De Kluize unpublished. Skip already-mined Ternat/Oostkamp/Wetteren/Poperinge/Haacht/Bilzen/Geel/Zwevegem + AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM/AGB Maaseik 1311-1312. Not an every-10 tick.
- EUR: **none sourced**. Do not invent euros. FOI-ready after honest hunt (page lists JR2025; PDF does not download).
- CSVs: sources+4/entities+1/commitments+1/leaderboard+1 + FOI ready `gap_lvgm_jr2025_tls_nodownload_l5` (not sent); no budget rows (no euros); rq_1315=done; spawn rq_1316; ticks=1315. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (Lievegem leftover city GE TLS). Does not move L5 near-complete of 347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1316 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Ranst/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE / AGB Bornem / AGB De Kluize only if a PDF now downloads; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 unless a fetchable JR appears).
"""
log = ROOT / "loop_log.md"
with log.open("a", encoding="utf-8") as f:
    f.write(log_entry)
print("loop_log ok")
print("tick1315 write done")

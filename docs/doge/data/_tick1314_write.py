# -*- coding: utf-8 -*-
"""Tick 1314 — surgical append/patch only. AGB Sport Hulshout JR2025 unpublished FOI-ready."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1314"
UTC = "2026-08-17T17:10:00Z"
ENT = "agb_sport_hulshout"
CITY = "city_hulshout"
HIER = "Vlaanderen>Gemeenten>Hulshout>AGB_Sport"
GAP = "gap_agbsph_jr2025_unpublished_l5"
SRC = "src_agbsph_portal"
SRC2 = "src_agbsph_jr_page"
SRC3 = "src_kbo_agbsph_0809823801"
SRC4 = "src_agbsph_meetingburger_jr2024"
SRC_URL = "https://www.hulshout.be/nl/bestuur/bestuur-gemeente/agb-sport-hulshout"
SRC2_URL = "https://www.hulshout.be/nl/bestuur/jaarrekening-agb-sport-hulshout"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0809823801"
SRC4_URL = "https://hulshout.meetingburger.net/GR/86f2bc72-e285-4598-846f-e2ab79bb1bce"
FOI_EMAIL = "sport@hulshout.be"
FOI_POSTAL = "Prof. Dr. Vital Celenplein 2 2235 Hulshout"
DRAFT = "docs/doge/foi/drafts/gap_agbsph_jr2025_unpublished_l5.md"


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
            "title": "AGB Sport Hulshout official portal page",
            "url": SRC_URL,
            "publisher": "Gemeente Hulshout / AGB Sport Hulshout",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1314; AGB founded GR 01.09.2008; exploits Sportpark Joris Verhaegen "
                "(sporthal/zwembad/velden/wielerpiste/atletiekpiste); RVB + directiecomite; "
                "contact Industriepark 3 2235 / sport@hulshout.be; no JR2025 PDF on this page"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Hulshout jaarrekening AGB Sport page (2018-2019 only; no JR2025)",
            "url": SRC2_URL,
            "publisher": "Gemeente Hulshout",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1314; HTTP 200; official AGB jaarrekening page lists 2018-2019 only; "
                "no BBC/NBB JR2025 PDF"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO AGB Sport Hulshout 0809.823.801",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1314; KBO 0809.823.801; AGB since 01.09.2008; 2 VE; seat Prof. Dr. Vital "
                "Celenplein 2 2235; NACE 93.110; aanbestedende overheid; BTW since 01.12.2009; "
                "bestuurder Joost Verhaegen since 21.01.2025; no KBO finance"
            ),
        },
        {
            "source_id": SRC4,
            "title": "Hulshout meeting.burger GR — AGB Sport JR2024 approval (no JR2025 PDF)",
            "url": SRC4_URL,
            "publisher": "Gemeente Hulshout / meeting.burger",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1314; GR OZ 5 JR2024 AGB Sport: RVB 02.06.2025 / GR 23.06.2025; "
                "MJP 2026-2031 AGB RVB 08.12.2025; no JR2025 attachment"
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
            "name_nl": "Autonoom Gemeentebedrijf Sport Hulshout (AGB Sport Hulshout)",
            "name_fr": "Regie communale autonome Sport Hulshout (AGB Sport Hulshout)",
            "name_en": "Hulshout autonomous municipal sports company (AGB Sport Hulshout)",
            "level": "agb",
            "parent_id": CITY,
            "community_language": "nl",
            "website": SRC_URL,
            "foi_email": FOI_EMAIL,
            "foi_postal": FOI_POSTAL,
            "notes": (
                "tick1314 JR2025 unpublished Entity II residual; KBO 0809.823.801; "
                "JR2024 live on meeting.burger; official jaarrekening page 2018-2019 only; "
                "MJP 2026-2031 live; no BBC/NBB JR2025 PDF; no sourced euros; FOI ready"
            ),
        },
    ],
)
print("entities", n)

n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": "comm_agbsph_jr2025_unpublished",
            "title": "AGB Sport Hulshout JR2025 BBC/NBB unpublished (FOI-ready)",
            "entity_id": ENT,
            "beneficiary": "Lokale besturen Antwerpen / Gemeente Hulshout",
            "legal_basis": "Decreet lokaal bestuur art. 242-243 / BBC; Bestuursdecreet openbaarheid",
            "decision_date": "",
            "start_year": "2025",
            "end_year": "2031",
            "total_envelope_eur": "",
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "unknown",
            "evaluation_url": SRC2_URL,
            "stated_goal": "Local AGB residual map VL JR2025 Hulshout Sport — PDF missing",
            "cut_option": "Publish BBC JR2025 + NBB filing + RVB vaststelling + city dual lines",
            "source_id": SRC2,
            "confidence": "medium",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": "tick1314; no sourced euros; official portal JR2024-only; FOI ready not sent",
        }
    ],
)
print("commitments", n)

n = append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": "lb_agbsph_jr2025_unpublished",
            "name": "AGB Sport Hulshout JR2025 unpublished (JR2024 live, no BBC 2025 PDF)",
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": HIER + ">jr2025_L5",
            "annual_cost_eur": "",
            "total_cost_eur": "",
            "tco_notes": "No primary JR2025 euros; do not use Belscope/Companyweb; JR2024 + MJP 2026-2031 live",
            "confidence": "medium",
            "source_id": SRC2,
            "beneficiaries": "Lokale besturen Antwerpen / Gemeente Hulshout",
            "stated_goal": "Local AGB residual map VL JR2025 Hulshout Sport — PDF missing",
            "measured_outcome": "JR2025 BBC/NBB not on hulshout.be jaarrekening-AGB page 2026-08-17; JR2024 + MJP 2026-2031 live",
            "absurdity_score": "6.0",
            "cost_score": "2.0",
            "difficulty": "2.0",
            "priority_index": "5.0",
            "cut_proposal": "Publish BBC JR2025 + NBB + RVB + city dual AGB lines",
            "status": "active",
            "struck_reason": "",
            "notes": "tick1314; no invented euros; FOI ready not sent; leftover AGB of mined city Hulshout 1050; not TE-additive of 348bn",
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
                "BBC jaarrekening 2025 AGB Sport Hulshout (J1-J5 / T2-T5 / BBR / AFM / fin debt / "
                "new loans / city inject / prijssub / werksub / pers VTE) + WVV/NBB filing if any "
                "+ RVB vaststelling besluit + dual Gemeente+OCMW Hulshout GE JR2025 lines covering "
                "AGB transfers. Official jaarrekening-AGB page has 2018-2019 only; meeting.burger "
                "has JR2024 (RVB 02.06.2025 / GR 23.06.2025) + MJP 2026-2031; no JR2025 PDF on 2026-08-17."
            ),
            "why_it_matters": (
                "First named leftover unmapped AGB after honest residual dual hunt. "
                "KBO 0809.823.801 active since 01.09.2008; exploits Sportpark Joris Verhaegen. "
                "City Hulshout GE already mined tick1050. No primary JR2025 PDF after portal+KBO "
                "search. Sister leftovers Bornem/De Kluize/Londerzeel/Holsbeek/Zwalm/Wortegem/"
                "Maarkedal/Ranst/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE still no PDF. "
                "Do not invent euros."
            ),
            "priority": "8",
            "recipient_body": "AGB Sport Hulshout / Gemeente Hulshout",
            "recipient_email": FOI_EMAIL,
            "recipient_postal": FOI_POSTAL,
            "draft_letter_path": DRAFT,
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_agbsph_jr2025_unpublished",
            "linked_leaderboard_id": "lb_agbsph_jr2025_unpublished",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; no sourced euros; not every-10",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1314",
    "title": "AGB Sport Hulshout JR2025 dual residual unpublished FOI",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AGB Sport Hulshout JR2025 unpublished after honest hunt; KBO 0809.823.801; "
        "JR2024 + MJP 2026-2031 live; no BBC/NBB JR2025 PDF; no sourced euros; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T16:55:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1314 AGB Sport Hulshout JR2025 unpublished Entity II residual; KBO 0809.823.801; "
        "JR2024 live; no JR2025 PDF; leftover AGB of mined city Hulshout 1050; FOI ready not sent; "
        "next rq_1315 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1315",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1314 done including AGB Sport Hulshout 1314 FOI-unpublished / AGB Merchtem 1313 "
        "FOI-unpublished / AGBIM Maaseik 1312 / AGB Maaseik 1311 / APB VERA 1310 / EVA Hoeve Holleken 1309 / "
        "Stad+OCMW Beerse 1308 / AGB Beerse 1307); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML "
        "(AGB Bornem / AGB De Kluize only if a PDF actually downloads); "
        "leftover Maarkedal/Londerzeel/Holsbeek/Merchtem city GE/Zwalm/Wortegem-Petegem still unmined — take only if PDF fetches; "
        "leftover city Linkebeek GE still JR2024-only; leftover Ranst official still JR2024; "
        "leftover Kapellen city GE not published; leftover Drogenbos/Boutersem/Schelle city GE JR2024-only; "
        "leftover Oosterzele no BBC PDF; leftover Stad+OCMW Maaseik GE unmined; leftover AGB Blankenberge JR2019-only; "
        "skip already-mined AGB Sport Hulshout 1314 (FOI unpublished) / AGB Merchtem 1313 / AGBIM 1312 / "
        "AGB Maaseik 1311 / APB VERA 1310 / EVA Hoeve Holleken 1309 / Stad+OCMW Beerse 1308 / AGB Beerse 1307 / "
        "AGB Herne 1122 / AGB Gooik 1121 / AGB Bocholt 1135 / AGB Bree 1166 / AGB Lanaken 1120 / city Hulshout 1050; "
        "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
        "skip AGB Kapellen / AGB Lokeren 1200 / EVA Gezinswelzijn 1253 / AGB Genk / ZOG Genk 1242; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF + "
        "vlaamsbrabant.be TLS unexpected-EOF (vera.be OK); not every-10"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1314 after AGB Sport Hulshout JR2025 unpublished FOI; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1314", rq_new, rq_spawn)
print("research_queue 1314", found, "spawned_1315", spawned)

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
            "last_unit_id": "rq_1314",
            "ticks_completed": "1314",
            "paused": "no",
            "notes": (
                "tick1314 AGB Sport Hulshout JR2025 unpublished residual; KBO 0809.823.801; "
                "JR2024 + MJP 2026-2031 live; no JR2025 PDF; no sourced euros; FOI ready; "
                "next rq_1315 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log_entry = """
### Tick 1314 - 2026-08-17 - rq_1314 AGB Sport Hulshout dual residual unpublished FOI
- Unit: Autonoom Gemeentebedrijf Sport Hulshout (AGB Sport Hulshout) JR2025 Entity II after residual dual hunt (KBO **0809.823.801**; official portal + KBO; **no JR2025 BBC/NBB PDF**). PREFER FIRST named leftover unmapped AGB (city Hulshout GE already mined tick 1050). Founded GR **01.09.2008**; exploits Sportpark Joris Verhaegen; 2 VE; NACE 93.110; aanbestedende overheid; bestuurder Joost Verhaegen since 21.01.2025; KBO seat Prof. Dr. Vital Celenplein 2 2235 / contact Industriepark 3. Moeder Gemeente Hulshout KBO **0207.502.497**. Official jaarrekening-AGB page HTTP 200: 2018–2019 only. Meeting.burger: JR2024 RVB **02.06.2025** / GR **23.06.2025**; MJP 2026-2031 RVB **08.12.2025**. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Hunt skipped already-mined AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 / AGB Herne 1122 / AGB Gooik 1121 / AGB Bocholt 1135 / AGB Bree 1166 / AGB Lanaken 1120; AGB Bornem still JR2024-only; AGB De Kluize still unpublished; Pajottegem city already 1126. Leftover city GE Londerzeel / Holsbeek / Merchtem / Zwalm / Wortegem-Petegem / Maarkedal TLS / Ranst official JR2024 / Linkebeek / Kapellen / Drogenbos / Boutersem / Stad+OCMW Maaseik still no fetchable JR2025 PDF. Not an every-10 tick.
- EUR: **none sourced**. Do not invent euros. FOI-ready after honest search.
- CSVs: sources+4/entities+1/commitments+1/leaderboard+1 + FOI ready `gap_agbsph_jr2025_unpublished_l5` (not sent); no budget rows (no euros); rq_1314=done; spawn rq_1315; ticks=1314. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (AGB Sport Hulshout unpublished). Does not move L5 near-complete of 347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1315 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; leftover Londerzeel/Holsbeek/Merchtem city GE/Zwalm/Wortegem-Petegem / city Linkebeek GE / Stad+OCMW Maaseik GE / AGB Bornem / AGB De Kluize only if a PDF now downloads; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 unless a fetchable JR appears).
"""
log = ROOT / "loop_log.md"
with log.open("a", encoding="utf-8") as f:
    f.write(log_entry)
print("loop_log ok")
print("tick1314 write done")

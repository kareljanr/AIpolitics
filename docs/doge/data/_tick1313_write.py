# -*- coding: utf-8 -*-
"""Tick 1313 — surgical append/patch only. AGB Merchtem JR2025 unpublished FOI-ready."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1313"
UTC = "2026-08-17T16:55:00Z"
ENT = "agb_merchtem"
CITY = "city_merchtem"
HIER = "Vlaanderen>Gemeenten>Merchtem>AGB"
GAP = "gap_agbmct_jr2025_unpublished_l5"
SRC = "src_agbmct_portal_agb"
SRC2 = "src_agbmct_beleidsrapporten"
SRC3 = "src_kbo_agbmct_0824869093"
SRC4 = "src_kbo_city_merchtem_0207511110"
SRC_URL = "https://www.merchtem.be/AGB"
SRC2_URL = "https://www.merchtem.be/bekendmakingen/detail/44/beleidsrapporten"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0824869093"
SRC4_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207511110"
FOI_EMAIL = "financies@merchtem.be"
FOI_POSTAL = "Nieuwstraat 1 1785 Merchtem"
DRAFT = "docs/doge/foi/drafts/gap_agbmct_jr2025_unpublished_l5.md"


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
            "title": "AGB Merchtem official portal page",
            "url": SRC_URL,
            "publisher": "Gemeente Merchtem / AGB Merchtem",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1313; AGB founded GR 26.10.2009; exploits vrijetijdsinfrastructuur; "
                "directiecomite + RVB; no JR2025 PDF on this page"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Merchtem beleidsrapporten (MJP 2026-2031 AGB + GE/OCMW; no JR2025)",
            "url": SRC2_URL,
            "publisher": "Gemeente Merchtem",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1313; HTTP 200; live MJP 2026-2031 AGB Merchtem + MJP GE+OCMW; "
                "jaarrekening 2025 string count 0; no BBC/NBB JR2025 PDF"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO AGB Merchtem 0824.869.093",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1313; KBO 0824.869.093; AGB since 26.10.2009; 0 VE; seat Nieuwstraat 1 1785; "
                "NACE 93.110; aanbestedende overheid; BTW since 13.04.2010; "
                "bestuurders David De Valck + Brigitte Van Gucht since 25.03.2019; no KBO finance"
            ),
        },
        {
            "source_id": SRC4,
            "title": "KBO Gemeente Merchtem 0207.511.110",
            "url": SRC4_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1313; KBO 0207.511.110; stad/gemeente since 01.01.1968; 11 VE; "
                "burgemeester Maarten Mast since 01.01.2019; AD Chris Van den Bossche since 27.04.2018; "
                "city+OCMW GE JR2025 still unpublished on beleidsrapporten"
            ),
        },
    ],
)
print("sources", n)

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": CITY,
            "name_nl": "Gemeente Merchtem",
            "name_fr": "Commune de Merchtem",
            "name_en": "Municipality of Merchtem",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.merchtem.be/",
            "foi_email": FOI_EMAIL,
            "foi_postal": FOI_POSTAL,
            "notes": (
                "tick1313 stub; KBO 0207.511.110; city+OCMW GE JR2025 unpublished on beleidsrapporten "
                "(MJP 2026-2031 live); AGB Merchtem FOI-ready this tick; leftover GE"
            ),
        },
        {
            "entity_id": ENT,
            "name_nl": "Autonoom Gemeentebedrijf Merchtem (AGB Merchtem)",
            "name_fr": "Regie communale autonome Merchtem (AGB Merchtem)",
            "name_en": "Merchtem autonomous municipal company (AGB Merchtem)",
            "level": "agb",
            "parent_id": CITY,
            "community_language": "nl",
            "website": SRC_URL,
            "foi_email": FOI_EMAIL,
            "foi_postal": FOI_POSTAL,
            "notes": (
                "tick1313 JR2025 unpublished Entity II residual; KBO 0824.869.093; "
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
            "commitment_id": "comm_agbmct_jr2025_unpublished",
            "title": "AGB Merchtem JR2025 BBC/NBB unpublished (FOI-ready)",
            "entity_id": ENT,
            "beneficiary": "Lokale besturen Vlaams-Brabant / Gemeente Merchtem",
            "legal_basis": "Decreet lokaal bestuur art. 242-243 / BBC; Bestuursdecreet openbaarheid",
            "decision_date": "",
            "start_year": "2025",
            "end_year": "2031",
            "total_envelope_eur": "",
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "unknown",
            "evaluation_url": SRC2_URL,
            "stated_goal": "Local AGB residual map VL JR2025 Merchtem — PDF missing",
            "cut_option": "Publish BBC JR2025 + NBB filing + RVB vaststelling + city dual GE",
            "source_id": SRC2,
            "confidence": "medium",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": "tick1313; no sourced euros; official portal MJP-only; FOI ready not sent",
        }
    ],
)
print("commitments", n)

n = append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": "lb_agbmct_jr2025_unpublished",
            "name": "AGB Merchtem JR2025 unpublished (MJP live, no BBC PDF)",
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": HIER + ">jr2025_L5",
            "annual_cost_eur": "",
            "total_cost_eur": "",
            "tco_notes": "No primary JR2025 euros; do not use Belscope/Companyweb; MJP 2026-2031 AGB is live",
            "confidence": "medium",
            "source_id": SRC2,
            "beneficiaries": "Lokale besturen Vlaams-Brabant / Gemeente Merchtem",
            "stated_goal": "Local AGB residual map VL JR2025 Merchtem — PDF missing",
            "measured_outcome": "JR2025 BBC/NBB not on merchtem.be beleidsrapporten 2026-08-17; MJP 2026-2031 AGB live",
            "absurdity_score": "6.0",
            "cost_score": "2.0",
            "difficulty": "2.0",
            "priority_index": "5.0",
            "cut_proposal": "Publish BBC JR2025 + NBB + RVB + city dual GE",
            "status": "active",
            "struck_reason": "",
            "notes": "tick1313; no invented euros; FOI ready not sent; leftover city GE also unpublished; not TE-additive of 348bn",
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
                "BBC jaarrekening 2025 AGB Merchtem (J1-J5 / T2-T5 / BBR / AFM / fin debt / "
                "new loans / city inject / prijssub / werksub / pers VTE) + WVV/NBB filing if any "
                "+ RVB vaststelling besluit + dual Gemeente+OCMW Merchtem GE JR2025 lines covering "
                "AGB transfers. Official beleidsrapporten has MJP 2026-2031 AGB + GE/OCMW only; "
                "JR2025 string count 0 on 2026-08-17."
            ),
            "why_it_matters": (
                "First named unmapped AGB in residual dual hunt. KBO 0824.869.093 active since "
                "26.10.2009; exploits vrijetijdsinfrastructuur. No primary JR2025 PDF after honest "
                "portal+KBO search. City+OCMW Merchtem GE also unpublished. Sister leftovers "
                "Londerzeel/Holsbeek/Zwalm/Wortegem/Maarkedal/Ranst/Linkebeek/Kapellen/Drogenbos/"
                "Boutersem/Maaseik GE still no PDF. Do not invent euros."
            ),
            "priority": "8",
            "recipient_body": "AGB Merchtem / Gemeente Merchtem",
            "recipient_email": FOI_EMAIL,
            "recipient_postal": FOI_POSTAL,
            "draft_letter_path": DRAFT,
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_agbmct_jr2025_unpublished",
            "linked_leaderboard_id": "lb_agbmct_jr2025_unpublished",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; no sourced euros; not every-10",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1313",
    "title": "AGB Merchtem JR2025 dual residual unpublished FOI",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AGB Merchtem JR2025 unpublished after honest hunt; KBO 0824.869.093; "
        "MJP 2026-2031 live; no BBC/NBB JR2025 PDF; no sourced euros; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T18:45:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1313 AGB Merchtem JR2025 unpublished Entity II residual; KBO 0824.869.093; "
        "MJP 2026-2031 live; no JR2025 PDF; city GE also unpublished; FOI ready not sent; "
        "next rq_1314 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1314",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1313 done including AGB Merchtem 1313 FOI-unpublished / AGBIM Maaseik 1312 / "
        "AGB Maaseik 1311 / APB VERA 1310 / EVA Hoeve Holleken 1309 / Stad+OCMW Beerse 1308 / "
        "AGB Beerse 1307 / Stad+OCMW Vleteren 1306 / Stad+OCMW Pepingen 1305 / AGB Pepingen 1304); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML "
        "(AGB Sport Hulshout / AGB Galmaarden fused Pajottegem only if a PDF actually downloads); "
        "leftover Maarkedal/Londerzeel/Holsbeek/Merchtem city GE/Zwalm/Wortegem-Petegem still unmined — take only if PDF fetches; "
        "leftover city Linkebeek GE still JR2024-only; leftover Ranst official still JR2024; "
        "leftover Kapellen city GE not published; leftover Drogenbos/Boutersem/Schelle city GE JR2024-only; "
        "leftover Oosterzele no BBC PDF; leftover Stad+OCMW Maaseik GE unmined; "
        "skip already-mined AGB Merchtem 1313 (FOI unpublished) / AGBIM 1312 / AGB Maaseik 1311 / "
        "APB VERA 1310 / EVA Hoeve Holleken 1309 / Stad+OCMW Beerse 1308 / AGB Beerse 1307 / "
        "city Vleteren 1306 / city Pepingen 1305 / AGB Pepingen 1304 / city Edegem 1303 / "
        "AGB Edegem 1239 / city Wommelgem 1302 / city Zonhoven 1301 / city Kortenaken 1300 / "
        "AGB Kortenaken 1299 / AGB Herne 1122 / AGB Gooik 1121 / AGB Bocholt 1135 / AGB Bree 1166 / "
        "AGB Lanaken 1120; "
        "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
        "skip AGB Kapellen / AGB Lokeren 1200 / EVA Gezinswelzijn 1253 / AGB Genk / ZOG Genk 1242; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF + "
        "vlaamsbrabant.be TLS unexpected-EOF (vera.be OK); not every-10"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1313 after AGB Merchtem JR2025 unpublished FOI; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1313", rq_new, rq_spawn)
print("research_queue 1313", found, "spawned_1314", spawned)

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
            "last_unit_id": "rq_1313",
            "ticks_completed": "1313",
            "paused": "no",
            "notes": (
                "tick1313 AGB Merchtem JR2025 unpublished residual; KBO 0824.869.093; "
                "MJP 2026-2031 live; no JR2025 PDF; no sourced euros; FOI ready; "
                "next rq_1314 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log_entry = """
### Tick 1313 - 2026-08-17 - rq_1313 AGB Merchtem dual residual unpublished FOI
- Unit: Autonoom Gemeentebedrijf Merchtem (AGB Merchtem) JR2025 Entity II after residual dual hunt (KBO **0824.869.093**; official portal + KBO; **no JR2025 BBC/NBB PDF**). PREFER FIRST named unmapped AGB. Founded GR **26.10.2009**; exploits vrijetijdsinfrastructuur; 0 VE; NACE 93.110; aanbestedende overheid; bestuurders David De Valck + Brigitte Van Gucht since 25.03.2019; seat Nieuwstraat 1 1785 Merchtem. Moeder Gemeente Merchtem KBO **0207.511.110** (burgemeester Maarten Mast; AD Chris Van den Bossche). Official beleidsrapporten HTTP 200: live **MJP 2026-2031 AGB** + **MJP GE+OCMW**; jaarrekening-2025 string count **0**. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Hunt skipped already-mined AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 / AGB Herne 1122 (PDF live but mined) / AGB Gooik 1121 / AGB Bocholt 1135 / AGB Bree 1166 / AGB Lanaken 1120; AGB Galmaarden fused Pajottegem; AGB Sport Hulshout MJP-only. Leftover city GE Londerzeel / Holsbeek / Merchtem / Zwalm / Wortegem-Petegem / Maarkedal / Ranst / Linkebeek / Kapellen / Drogenbos / Boutersem / Stad+OCMW Maaseik still no fetchable JR2025 PDF. Not an every-10 tick.
- EUR: **none sourced**. Do not invent euros. FOI-ready after honest search.
- CSVs: sources+4/entities+2/commitments+1/leaderboard+1 + FOI ready `gap_agbmct_jr2025_unpublished_l5` (not sent); no budget rows (no euros); rq_1313=done; spawn rq_1314; ticks=1313. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (AGB Merchtem unpublished). Does not move L5 near-complete of 347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1314 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; leftover Londerzeel/Holsbeek/Merchtem city GE/Zwalm/Wortegem-Petegem / city Linkebeek GE / Stad+OCMW Maaseik GE only if a PDF now downloads; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 unless a fetchable JR appears).
"""
log = ROOT / "loop_log.md"
with log.open("a", encoding="utf-8") as f:
    f.write(log_entry)
print("loop_log ok")
print("tick1313 write done")

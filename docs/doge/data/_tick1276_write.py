# -*- coding: utf-8 -*-
"""Tick 1276 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 Motena Roeselare JR2025 dual residual (PDF opaque)."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T09:32:00Z"
TICK = 1276
SRC = "src_motena_av_20260602_dagorde"
SRC2 = "src_motena_bestuur_av"
SRC3 = "src_kbo_motena_0537951706"
SRC4 = "src_nbb_motena_0537951706"
SRC5 = "src_roeselare_samenwerkingen_motena"
ENT = "motena_roeselare"
CITY = "city_roeselare"
SRC_URL = "https://www.motena.be/sites/motena/files/uploads/verslagen_vergaderings/files/AV_20260602_dagorde.pdf"
SRC2_URL = "https://www.motena.be/de-leden-van-onze-raad-van-bestuur-algemene-vergadering"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0537951706"
SRC4_URL = "https://consult.cbso.nbb.be/consult-enterprise/0537951706"
SRC5_URL = "https://www.roeselare.be/nl/beleid-en-bestuur/bestuur-van-de-stad/samenwerking-met-andere-steden-en-organisaties"
GAP = "gap_motena_jr2025_pdf_opaque_city_dual_unknown_l5"
HIER = "Vlaanderen>Gemeenten>Roeselare>Motena"


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


def patch_rq_target_and_append(path, target_id, new_target, spawn_row):
    text = path.read_text(encoding="utf-8")
    ends_nl = text.endswith("\n")
    lines = text.splitlines()
    header = lines[0]
    fields = next(csv.reader([header]))
    out = [header]
    found = False
    has_spawn = False
    spawn_id = spawn_row.get("task_id")
    for line in lines[1:]:
        if not line:
            continue
        rid = next(csv.reader([line]))[0]
        if rid == spawn_id:
            has_spawn = True
        if rid == target_id:
            found = True
            out.append(csv_line(fields, new_target))
        else:
            out.append(line)
    if not has_spawn:
        out.append(csv_line(fields, spawn_row))
    path.write_text("\n".join(out) + ("\n" if ends_nl else ""), encoding="utf-8")
    return found, not has_spawn


n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Motena AV 2 juni 2026 dagorde — vaststelling JR2025",
            "url": SRC_URL,
            "publisher": "Motena",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1276; primary AV PDF; punt 2 VASTSTELLING Jaarrekening 2025 "
                "+ waarderingsregels; raadzaal Isala 19u30; no euro tables in this file"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Motena bestuur / AV pagina (dagordes)",
            "url": SRC2_URL,
            "publisher": "Motena",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1276; AV dagordes public; JR PDF not on org site; "
                "AD Verdoolaege / voorzitter Wenes; Vereniging van OCMW's"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Motena 0537.951.706",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1276; Vereniging van OCMW's since 25.06.2013; renamed Motena "
                "25.09.2019 (was Zorgbedrijf Roeselare); seat Rolariusplein 8.201 "
                "8800 since 27.11.2024; 27 VE; NACE 84.115 / RSZ 87.101; "
                "replaces 0597.748.345; no KBO financials"
            ),
        },
        {
            "source_id": SRC4,
            "title": "NBB Consult Motena 0537951706 JR filings",
            "url": SRC4_URL,
            "publisher": "NBB Central Balance Sheet Office",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1276; consult/API 403/SPA this box; KBO links NBB publications; "
                "do not invent internals; do not use Belscope/Companyweb"
            ),
        },
        {
            "source_id": SRC5,
            "title": "Stad Roeselare samenwerkingen — Motena JR + commissaris",
            "url": SRC5_URL,
            "publisher": "Stad Roeselare",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1276; page lists Besluit AV 2 juni 2026 + Jaarrekening Motena "
                "+ Verslag commissaris; Cloudflare 403 this box so PDF not fetched; "
                "WebFetch HTML confirms the named downloads exist"
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
            "name_nl": "Stad Roeselare",
            "name_fr": "Ville de Roulers",
            "name_en": "City of Roeselare",
            "level": "municipality",
            "parent_id": "sec_local",
            "community_language": "nl",
            "website": "https://www.roeselare.be/",
            "foi_email": "bestuurszaken@roeselare.be",
            "foi_postal": "Grote Markt 1 8800 Roeselare",
            "notes": (
                "tick1276 stub; Motena dual residual (KBO 0537.951.706; JR2025 AV "
                "2.6.2026; BBC/NBB PDF + city dual unknown this box); city GE JR "
                "not mined this tick; Cloudflare on city site"
            ),
        },
        {
            "entity_id": ENT,
            "name_nl": "Motena (Welzijnsvereniging / ex-Zorgbedrijf Roeselare)",
            "name_fr": "Motena (association de CPAS / ex-entreprise de soins Roulers)",
            "name_en": "Motena (OCMW association / ex Roeselare care company)",
            "level": "parastatal",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://www.motena.be/",
            "foi_email": "info@motena.be",
            "foi_postal": "Rolariusplein 8 bus 201 8800 Roeselare",
            "notes": (
                "tick1276 JR2025 dual residual; KBO 0537.951.706 Vereniging van "
                "OCMW's since 25.06.2013 renamed 25.09.2019; AV 2.6.2026 "
                "vaststelling JR2025; BBC/NBB PDF + city dual unknown (org site "
                "agendas only; city Cloudflare; NBB 403); FOI "
                "gap_motena_jr2025_pdf_opaque_city_dual_unknown_l5; distinct from "
                "Mintus Brugge"
            ),
        },
    ],
)
print("entities", n)

n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": "comm_motena_jr2025_pdf_opaque_2025",
            "title": "Motena JR2025 BBC+NBB PDF + city dual (opaque this box)",
            "entity_id": ENT,
            "beneficiary": "Motena / Stad+OCMW Roeselare / WZC+thuiszorg clients",
            "legal_basis": "Decreet Lokaal Bestuur + Bestuursdecreet; AV 2.6.2026 vaststelling JR2025",
            "decision_date": "2026-06-02",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "",
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Publish fetchable JR2025 BBC+NBB + nominative city/OCMW dual",
            "cut_option": "FOI BBC J2 + NBB VenB + city dual 2025-2031; no invented euros",
            "source_id": SRC,
            "confidence": "high",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": (
                "tick1276; AV agenda confirms JR2025 vaststelling; PDF not fetched "
                "(city Cloudflare + NBB 403 + org site agendas only); envelope Unknown"
            ),
        }
    ],
)
print("commitments", n)

n = append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": HIER + ">jr2025_L5",
            "entity_id": ENT,
            "what_is_missing": (
                "BBC J1-J5 AFM/gecorr AFM/BBR/avail BBR + NBB VenB internals "
                "(assets/fin debt/PnL/personeel/VTE) + city/OCMW dual 2025 lock "
                "and 2026-2031 nominative + AV 2.6.2026 besluit + commissarisverslag "
                "direct PDF URL + NBB Consult working filing number "
                "(org site agendas only; city Cloudflare 403; NBB 403/SPA this box)"
            ),
            "why_it_matters": (
                "Unmined Roeselare Entity II zorg EVA (~27 VE; successor of "
                "Zorgbedrijf Roeselare). AV 2.6.2026 established JR2025 but the "
                "PDF is not fetchable from this box. Distinct from Mintus Brugge. "
                "No invented euros."
            ),
            "priority": "8",
            "recipient_body": "Motena / Stad + OCMW Roeselare",
            "recipient_email": "info@motena.be",
            "recipient_postal": "Rolariusplein 8 bus 201 8800 Roeselare",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_motena_jr2025_pdf_opaque_2025",
            "linked_leaderboard_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; no invented euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1276",
    "title": "Motena Roeselare JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Motena (ex-Zorgbedrijf Roeselare) JR2025 AV+KBO; "
        "KBO 0537.951.706; AV 2.6.2026 vaststelling; BBC/NBB PDF + city dual "
        "unknown this box; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T09:25:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1276 Motena Roeselare JR2025 dual residual; KBO 0537.951.706; "
        "AV 2.6.2026 JR2025 vaststelling; 27 VE; PDF opaque (city Cloudflare + "
        "NBB 403 + org agendas only); no invented euros; FOI ready not sent; "
        "next rq_1277 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1277",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(Gent dual AGB cluster 1255-1259 + Antwerp AG 1260-1265 + Atlas 1266 + Amal 1267 "
        "+ Fietsambassade 1268 + Mintus 1269 + MAC 1270 + AGB Kruibeke/BKZ sport 1271 "
        "+ AGB Tienen 1272 + AG Museum Leuven 1273 + Stad+OCMW Tienen 1274 "
        "+ AGB IBOGEM 1275 + Motena Roeselare 1276 done; prefer other unmined "
        "AGB/zorg/EVA with direct PDF/NBB/city HTML; skip Motena unless a "
        "fetchable JR2025 PDF appears; skip AGSO Knokke-Heist already 1217; "
        "skip AGB Lokeren 1200; WAGSO already mined tick1199; skip Mobil-O/AG EOS "
        "inactive; skip Woonzorgnetwerk Edegem / Zorgbedrijf Sint-Truiden / "
        "Zorgbedrijf Brasschaat unpublished; ebesluit TLS + Leuven besluitvorming "
        "TLS + Roeselare.be Cloudflare — prefer org sites / NBB / city HTML; "
        "Brugge SAS / Blauwe Lelie / SPOOR / WOK only if they have a separate "
        "downloadable JR)."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1276 after Motena Roeselare JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1276", rq_new, rq_spawn)
print("research_queue 1276", found, "spawned_1277", spawned)

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
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": "rq_1276",
            "ticks_completed": "1276",
            "paused": "no",
            "notes": (
                "tick1276 Motena Roeselare JR2025 dual residual; KBO 0537.951.706; "
                "AV 2.6.2026 vaststelling; BBC/NBB PDF + city dual unknown "
                "(Cloudflare/NBB 403); FOI ready; next rq_1277 residual dual L5 VL "
                "(prefer unmined AGB/zorg/EVA JR2025); continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1276 - 2026-08-17 - rq_1276 Motena Roeselare dual residual
- Unit: Motena (Welzijnsvereniging / ex-Zorgbedrijf Roeselare) JR2025 Entity II after Mintus Brugge tick1269 + Zorg/WV cluster 1246–1251 (KBO **0537.951.706**; Vereniging van OCMW's since 25.06.2013; renamed Motena 25.09.2019; AV 2.06.2026 vaststelling JR2025). **Distinct from** Mintus (0682.844.465). Seat Rolariusplein 8.201 8800. AD Steven Verdoolaege / voorzitter Bart Wenes. 27 VE (KBO). WZC De Waterdam / De Zilverberg / Ter Berken / Sint-Henricus + Kotee + KIDZ (org narrative). City Roeselare GE not mined this tick.
- EUR: **none invented**. Primary AV PDF confirms JR2025 is on the 2.06.2026 agenda (punt 2 vaststelling + waarderingsregels). City page names downloads (Jaarrekening Motena + commissaris + AV besluit) but **roeselare.be Cloudflare 403** this box. Org site publishes AV dagordes only — no JR PDF. NBB consult/API **403/SPA**. Raadpleeg-roeselare is a SPA without a fetchable attachment. Do not use Belscope/Companyweb.
- CSVs: sources+5/entities(new Motena + city_roeselare stub)/commitments+1 (envelope Unknown) + FOI ready `gap_motena_jr2025_pdf_opaque_city_dual_unknown_l5` (not sent); no budgets/leaderboard without primary euros; rq_1276=done; spawn rq_1277; ticks=1276. Not a *0 tick — no progress refresh.
- Next: rq_1277 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; skip Motena unless a fetchable JR appears).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")

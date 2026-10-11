# -*- coding: utf-8 -*-
"""Tick 1353 — leftover IGS Limburg.net JR2025 glossy-only FOI residual.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10 (next every-10 is 1360).
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1353"
UTC = "2026-08-19T00:05:00Z"
ENT = "igs_lnet"
HIER = "Vlaanderen>Limburg>IGS>LimburgNet>Afval"
GAP = "gap_lnet_jr2025_glossy_not_wvv_l5"
SRC = "src_lnet_jr2025_pdf"
SRC2 = "src_lnet_site"
SRC3 = "src_kbo_lnet_0214533712"
SRC4 = "src_lnet_foi_contact"
SRC_URL = "https://limburg.net/sites/default/files/generated/components/attachments/jaarverslag_2025.pdf"
SRC2_URL = "https://limburg.net/jaarverslag"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0214533712"
SRC4_URL = "https://limburg.net/over-limburgnet"
FOI_EMAIL = "info@limburg.net"
FOI_POSTAL = "Herkenrodesingel 14 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_lnet_jr2025_glossy_not_wvv_l5.md"


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
                "title": "Limburg.net Schoonste Jaarverslag 2025 (official glossy 17p InDesign 11.06.2026; no embedded WVV)",
                "url": SRC_URL,
                "publisher": "Limburg.net opdrachthoudende vereniging",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1353; official PDF 6.72MB 17p InDesign 11.06.2026 versie mei 2026; leftover IGS waste "
                    "of mined Limburg cities; glossy mix shares only; NOT statutory WVV/BBC J1-J5 euros"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Limburg.net official jaarverslag page (jaarverslag_2025.pdf listed)",
                "url": SRC2_URL,
                "publisher": "Limburg.net",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1353; leftover IGS waste of mined Limburg cities; lists jaarverslag_2025.pdf "
                    "(was 2024 last ticks)"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO LIMBURG.NET 0214.533.712",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1353; KBO 0214.533.712 Actief / normale toestand since 24.06.1974; "
                    "statutaire naam LIMBURG.NET since 19.12.2007; Opdrachthoudende vereniging "
                    "(Vlaams Gewest) since 15.10.1993; zetel Herkenrodesingel 14 3500 Hasselt "
                    "since 01.01.2025; 35 VE; aanbestedende overheid since 24.06.1974; btw since "
                    "01.05.1980; RSZ since 01.01.2022; jaarvergadering mei; boekjaar 31 december; "
                    "KBO kapitaal 250000 (register capital, not JR2025); 18 bestuurders; "
                    "databank 17.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Limburg.net FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "Limburg.net",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1353; FOI info@limburg.net; Herkenrodesingel 14 3500 Hasselt; "
                    "T 011 28 89 89; 39 gemeenten / 921638 inwoners / 399470 gezinnen; "
                    "voorzitter Thomas Vints (bestuurder since 26.03.2025)"
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
                "name_nl": "Limburg.net (leftover IGS afval Limburg en Diest)",
                "name_fr": "Limburg.net (association de mission / IGS residuel / dechets Limbourg et Diest)",
                "name_en": "Limburg.net Limburg+Diest waste intermunicipal (leftover IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://limburg.net",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1353 leftover IGS residual waste of mined Limburg cities "
                    "(Hasselt/Genk/Tongeren-Borgloon/Houthalen-Helchteren/Bilzen-Hoeselt/"
                    "Leopoldsburg/Nieuwerkerken/Gingelom; Maaseik AGB already mined); "
                    "KBO 0214.533.712 Actief since 24.06.1974; official JR2025 glossy PDF downloads "
                    "but no statutory WVV/BBC euros; FOI ready statutory/NBB"
                ),
            },
        ],
    )
    print("entities", n)

    n = append_rows(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": HIER + ">JR2025_L5",
                "entity_id": ENT,
                "what_is_missing": (
                    "Statutory WVV/BBC/NBB jaarrekening 2025 (assets / omzet / pers / expl / pnl / VTE) "
                    "— official JR2025 is glossy 17p InDesign 11.06.2026 with mix shares only "
                    "(inkomsten 46.66pct kohier / 15.02pct gemeentelijke werkingsbijdragen / "
                    "13.58pct sector / 12pct klanten / 8.55pct grondstoffen; uitgaven 53.37pct "
                    "Optimo verwerking / 13.55pct bezoldigingen) plus per-vennoot 2025-2026 dual "
                    "lines for the about-15pct municipal cost cover of 39 vennoten "
                    "(38 Limburg cities + Diest) + Bionerga/Biostoom verwerkingskosten + AV mei "
                    "minutes + NBB filing"
                ),
                "why_it_matters": (
                    "Leftover IGS waste shell of mined Limburg cities "
                    "(Hasselt/Genk/Tongeren-Borgloon/Houthalen-Helchteren/Bilzen-Hoeselt/"
                    "Leopoldsburg/Nieuwerkerken/Gingelom; Maaseik AGB already mined): glossy "
                    "17p mix shares vs unpublished statutory omzet/assets/pers/PnL is a dual "
                    "opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Limburg.net / 39 vennoten (38 Limburg + Diest)",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-19",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "",
                "linked_leaderboard_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "tick1353 leftover IGS waste of mined Limburg cities after honest hunt; "
                    "live JR2025 official glossy PDF now extracted (6.72MB 17p InDesign 11.06.2026) "
                    "but no statutory euros — FOI statutory/NBB. "
                    "Westtoer APB BBC 2025 already mined — skipped. "
                    "IOK/IMOG/Haviland still 2024. Interleuven still 2024 balans. "
                    "EcoWerf/Veneco/Leiedal glossy. IVAGO SSL EOF. MIWA flipbook. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1353",
        "title": "Limburg.net JR2025 leftover IGS dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Limburg.net leftover IGS waste of mined Limburg cities "
            "after honest hunt; KBO 0214.533.712 Actief; live JR2025 official glossy PDF "
            "(6.72MB 17p InDesign 11.06.2026) mix shares only / no statutory WVV euros; "
            "FOI ready statutory/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T23:20:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1353 Limburg.net leftover IGS residual; KBO 0214.533.712; "
            "live JR2025 glossy PDF no statutory euros; FOI ready not sent; next rq_1354 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1354",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1353 done including Limburg.net 1353 leftover IGS glossy-only FOI / "
            "IVBO 1352 leftover IGS live WVV / "
            "SOLVA 1351 leftover IGS live JR / "
            "Interwaas 1350 leftover IGS live WVV + every-10 / "
            "Aquaduin / IWVA ov 1349 leftover IGS live WVV / "
            "Creat Services dv 1348 leftover IGS live WVV / "
            "IVIO Izegem-Ommeland 1347 leftover IGS live JR operational / "
            "WVI West-Vlaanderen 1346 leftover IGS live WVV / "
            "IVVO Veurne-Ommeland 1345 leftover IGS live WVV / "
            "ILvA Land van Aalst 1344 leftover IGS live WVV / "
            "IVM Meetjesland 1343 leftover IGS live WVV / "
            "IDM Durme-Moervaart 1342 leftover IGS live WVV / "
            "IGEAN dienstverlening 1341 leftover IGS live WVV / "
            "EVA Limburg Sterk Merk 1340 leftover EVA live WVV + every-10); "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "Veneco glossy jaarverslag 2025 websingle — take only if a WVV/BBC PDF now downloads; "
            "EcoWerf 2025 jaarverslag glossy / 2024 statutory still unpublished — take only if a WVV/BBC PDF now downloads; "
            "Leiedal 2025 InDesign glossy-only — take only if a WVV/BBC PDF now downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland still 2024 — take only if a 2025 JR PDF now downloads; "
            "IVOO no public 2025 JR PDF — take only if a 2025 JR PDF now downloads; "
            "MIROM 403 — take only if a 2025 JR PDF now downloads; "
            "INCOVO still 2024 — take only if a 2025 JR PDF now downloads; "
            "IVAGO activiteitenverslag 2025 listed but SSL EOF / ebesluit Gent TLS — take only if a statutory WVV/BBC PDF now downloads; "
            "MIWA 2025 aflip flipbook only — take only if a WVV/BBC PDF now downloads; "
            "IVAREM still 2024 / activiteitenverslag 2025 glossy — take only if a 2025 JR PDF now downloads; "
            "IGEMO activiteitenverslag 2025 only — take only if a WVV/BBC PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
            "WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / "
            "WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330; "
            "skip Westtoer APB already mined; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403; not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1353 after Limburg.net leftover IGS glossy FOI; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1353", rq_new, rq_spawn)
    print("research_queue 1353", found, "spawned_1354", spawned)

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
                "last_unit_id": "rq_1353",
                "ticks_completed": "1353",
                "paused": "no",
                "notes": (
                    "tick1353 Limburg.net leftover IGS residual; KBO 0214.533.712; "
                    "live JR2025 glossy PDF no statutory euros; "
                    "FOI ready statutory/NBB; next rq_1354 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1353 - 2026-08-19 - rq_1353 Limburg.net dual residual leftover IGS
- Unit: Limburg.net (opdrachthoudende vereniging / leftover IGS waste; statutaire naam LIMBURG.NET) of already-mined Limburg cities (Hasselt / Genk / Tongeren-Borgloon / Houthalen-Helchteren / Bilzen-Hoeselt / Leopoldsburg / Nieuwerkerken / Gingelom; Maaseik AGB already mined; leftover Stad+OCMW Maaseik GE still unmined) after residual dual hunt (KBO **0214.533.712**; official limburg.net + live jaarverslag 2025 PDF 6.72MB / 17p; InDesign **11.06.2026**; versie mei 2026). Leftover IGS whose official page now yields a downloadable JR2025 PDF — glossy mix shares only, **no** statutory WVV/BBC euros. Distinct from already-mined IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341. KBO Actief / normale toestand since **24.06.1974**; Opdrachthoudende vereniging (Vlaams Gewest) since 15.10.1993; zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; **35 VE**; aanbestedende overheid since 24.06.1974; btw since 01.05.1980; RSZ since 01.01.2022; jaarvergadering mei; boekjaar 31 december; KBO kapitaal **250.000** (register capital, not JR2025); 18 bestuurders; voorzitter Thomas Vints since 26.03.2025; e-mail info@limburg.net; tel 011 28 89 89; NACE 38.330 / 38.110. 39 gemeenten / 921.638 inwoners / 399.470 gezinnen. Hunt leftover AGB/zorg/EVA first: Westtoer APB BBC jaarrekening 2025 already mined earlier — skipped; IOK/IMOG/Haviland still 2024; Interleuven still 2024 balans; EcoWerf 2025 glossy / 2024 statutory unpublished; IVAREM activiteitenverslag 2025 glossy; IGEMO activiteitenverslag only; IVOO login only; Veneco/Leiedal glossy-only; IVAGO SSL EOF; MIWA flipbook; MIROM Cloudflare; De Schorre provincieantwerpen.be 403; APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas no fetchable PDF; Dommelhof leftover Limburg EVA KBO 0777.495.085 no JR2025 PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek no fetchable 2025 JR this tick. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345. Not every-10 (next 1360).
- EUR: **no statutory WVV/BBC euros invented**. Official glossy mix shares only (inkomsten 46,66% kohier / 15,02% gemeentelijke werkingsbijdragen / 13,58% sector / 12% klanten / 8,55% grondstoffen; uitgaven 53,37% Optimo verwerking / 13,55% bezoldigingen). Gemeenten still covered **about 15%** of costs. Operational kg/inw huis-aan-huis restafval **87,60** (was 85,10); parks **82,40** (was 71,00). KBO kapitaal 250.000 is register capital, not JR2025 executed. FOI statutory assets/omzet/pers/PnL/VTE + per-vennoot dual + Bionerga + NBB.
- CSVs: sources+4/entities+1 + FOI ready `gap_lnet_jr2025_glossy_not_wvv_l5` (not sent); no invented budget/leaderboard euros; rq_1353=done; spawn rq_1354; ticks=1353.
- Coverage: residual dual L5 (Limburg.net leftover IGS glossy FOI). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1354 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; EcoWerf only if a statutory WVV/BBC PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; MIROM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer already mined unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1353 write done")


if __name__ == "__main__":
    main()

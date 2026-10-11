# -*- coding: utf-8 -*-
"""Tick 1347 — leftover IGS IVIO Izegem-Ommeland JR2025 official PDF euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10 (next every-10 is 1350).
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1347"
UTC = "2026-08-18T21:15:00Z"
ENT = "igs_ivio"
HIER = "Vlaanderen>WestVlaanderen>IGS>IVIO>IzegemOmmeland"
GAP = "gap_ivio_cityfee_10_04m_statutory_wvv_l5"
SRC = "src_ivio_jr2025_pdf"
SRC2 = "src_ivio_site"
SRC3 = "src_kbo_ivio_0213897173"
SRC4 = "src_ivio_foi_contact"
SRC_URL = "https://www.ivio.be/sites/default/files/2026-05/JaarverslagIVIO2025-web.pdf"
SRC2_URL = "https://www.ivio.be/jaarverslagen"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0213897173"
SRC4_URL = "https://www.ivio.be/"
FOI_EMAIL = "info@ivio.be"
FOI_POSTAL = "Lodewijk de Raetlaan 12 8870 Izegem"
DRAFT = "docs/doge/foi/drafts/gap_ivio_cityfee_10_04m_statutory_wvv_l5.md"
COMM = "comm_ivio_jr2025_cityfee"
LB = "lb_ivio_cityfee_10_04m_rc_3_08m"


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
                "title": "IVIO jaarverslag boekjaar 2025 (official PDF operational tables; InDesign 20.05.2026; no embedded WVV)",
                "url": SRC_URL,
                "publisher": "IVIO Intergemeentelijke vereniging voor duurzaam milieubeleid in Izegem en Ommeland",
                "accessed_date": "2026-08-18",
                "source_class": "budget",
                "notes": (
                    "tick1347; official PDF 3.70MB 64p InDesign 20.05.2026; leftover IGS of mined Midwest West-Flanders cities; "
                    "operational cityfee/BT tables; NOT statutory WVV/BBC J1-J5"
                ),
            },
            {
                "source_id": SRC2,
                "title": "IVIO official jaarverslagen page (Jaarverslag 2025 3.7 MB listed)",
                "url": SRC2_URL,
                "publisher": "IVIO",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1347; HTTP 200 lists JaarverslagIVIO2025-web.pdf 3.70MB; leftover IGS of mined Izegem/Tielt/Ardooie/Dentergem/"
                    "Ingelmunster/Ledegem/Lendelede/Oostrozebeke/Pittem/Ruiselede cities"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO IVIO Intergemeentelijke vereniging Izegem en Ommeland 0213.897.173",
                "url": SRC3_URL,
                "publisher": "KBO Besloten vennootschap Public Search FOD Economie",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1347; KBO 0213.897.173 Actief / normale toestand since 17.12.1973; "
                    "statutaire naam Intergemeentelijke vereniging voor duurzaam milieubeleid in Izegem en Ommeland since 14.05.2003; "
                    "afkorting I.V.I.O. since 17.12.1973; Opdrachthoudende vereniging (Vlaams Gewest) since 10.12.2003; "
                    "zetel Lodewijk de Raetlaan 12 8870 Izegem since 09.12.2013; 11 VE; RSZ since 01.01.2022; "
                    "btw since 01.04.1996; aanbestedende overheid since 17.12.1973; "
                    "jaarvergadering april; boekjaar 31 december; NACE 38.330 / 38.110"
                ),
            },
            {
                "source_id": SRC4,
                "title": "IVIO homepage / FOI channel",
                "url": SRC4_URL,
                "publisher": "IVIO",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1347; FOI info@ivio.be from official PDF; Lodewijk de Raetlaan 12 8870 Izegem; "
                    "T 051 31 17 96; voorzitter Jurgen Olivier; ondervoorzitter Nico Parmentier"
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
                "name_nl": "IVIO Intergemeentelijke vereniging voor duurzaam milieubeleid in Izegem en Ommeland (leftover IGS)",
                "name_fr": "IVIO intercommunale Izegem et environs (association missionnee / IGS residuel)",
                "name_en": "IVIO Izegem-Ommeland waste intermunicipal (leftover IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.ivio.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1347 leftover IGS residual of mined Midwest West-Flanders cities Izegem/Tielt/Ardooie/Dentergem/"
                    "Ingelmunster/Ledegem/Lendelede/Oostrozebeke/Pittem/Ruiselede-exit; "
                    "KBO 0213.897.173 Actief since 17.12.1973; official JR2025 PDF downloads (glossy operational tables); "
                    "sourced euros cityfee 10.040m / BT1 5.649m / parks 2.274m / BT3 2.485m / RC 3.083m; "
                    "FOI ready statutory WVV/NBB"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_ivio_cityfee_2025", ENT, "2025", "10040036", "2025 gemeentelijke bijdrage 10040036 was 9671746 budget 10738248; tick1347; primary official PDF eindafrekening; NOT WVV"),
        ("bud_ivio_budget_2025", ENT, "2025", "10738248", "2025 jaarbudget 10738248 (header also 10738243); 7pct under; tick1347; primary official PDF"),
        ("bud_ivio_bt1_2025", ENT, "2025", "5649253", "2025 bedrijfstak 1 ophaling/overslag 5649253 was 5643056 budget 5020112; tick1347; primary official PDF"),
        ("bud_ivio_parks_2025", ENT, "2025", "2274114", "2025 bedrijfstak 2 recyclageparken 2274114 was 2125398 budget 2521032; tick1347; primary official PDF"),
        ("bud_ivio_parks_budget_2025", ENT, "2025", "2521032", "2025 parks budget 2521032 vs executed 2274114 overschot 10pct; tick1347; primary official PDF"),
        ("bud_ivio_bt3_2025", ENT, "2025", "2485441", "2025 bedrijfstak 3 afzet 2485441 was 2155826 budget 3117040; tick1347; primary official PDF"),
        ("bud_ivio_bt3_budget_2025", ENT, "2025", "3117040", "2025 BT3 budget 3117040 vs executed 2485441; tick1347; primary official PDF"),
        ("bud_ivio_retributie_2025", ENT, "2025", "3303540", "2025 retributies 3303540.25 (HV 3043132 + PMD 260408.25) voorschot 3397488 saldo -93947.75; tick1347; primary official PDF"),
        ("bud_ivio_rc_2025", ENT, "2025", "3082966", "2025 RC schuld IVIO aan gemeenten 3082966 (beginsaldo 2486574.54); tick1347; primary official PDF AR 489"),
        ("bud_ivio_extra_2025", ENT, "2025", "102670", "2025 extra niet-gesolidariseerde gemeentelijke diensten 102670; tick1347; primary official PDF"),
        ("bud_ivio_izegem_fee_2025", ENT, "2025", "2317651", "2025 Izegem cityfee 2317651 was 2281138 budget 2423256; tick1347; primary official PDF per-vennoot"),
        ("bud_ivio_tielt_fee_2025", ENT, "2025", "2542169", "2025 Tielt cityfee 2542169 was 2399352 budget 2730612 (Meulebeke fusion); tick1347; primary official PDF"),
        ("bud_ivio_ingelmunster_fee_2025", ENT, "2025", "888691", "2025 Ingelmunster cityfee 888691 was 876466 budget 958728; tick1347; primary official PDF"),
        ("bud_ivio_izegem_groen_2025", ENT, "2025", "38164", "2025 Izegem groen via composteerbare zakken 38164 extra; tick1347; primary official PDF"),
        ("bud_ivio_park_depr_2025", ENT, "2025", "229923", "2025 park afschrijvingen 229923 was 179435; tick1347; primary official PDF"),
        ("bud_ivio_recupel_2025", ENT, "2025", "91738", "2025 Recupel AEEA 91738 +22pct vs 2024; tick1347; primary official PDF"),
        ("bud_ivio_valumat_2025", ENT, "2025", "156000", "2025 Valumat matrassen 156000 vs budget 85000; tick1347; primary official PDF"),
        ("bud_ivio_park_citizen_2025", ENT, "2025", "228127", "2025 burger-parkontvangsten 228127 vs budget 190000; tick1347; primary official PDF"),
        ("bud_ivio_textiel_2025", ENT, "2025", "93000", "2025 textiel ontvangst VICT/BELCOTEX 93000 DROP vs 431375; tick1347; primary official PDF"),
        ("bud_ivio_park_uitzend_drop_2025", ENT, "2025", "107682", "2025 parks uitzend DROP 107682 / 47pct; tick1347; primary official PDF (delta not org-wide pers)"),
        ("bud_ivio_ledeg_fee_2025", ENT, "2025", "754173", "2025 Ledegem cityfee 754173 was 736822 budget 810744; tick1347; primary official PDF"),
        ("bud_ivio_ardooie_fee_2025", ENT, "2025", "751458", "2025 Ardooie cityfee 751458 was 736819 budget 791856; tick1347; primary official PDF"),
        ("bud_ivio_dentergem_fee_2025", ENT, "2025", "685077", "2025 Dentergem cityfee 685077 was 672388 budget 749556; tick1347; primary official PDF"),
        ("bud_ivio_oostrozebeke_fee_2025", ENT, "2025", "641339", "2025 Oostrozebeke cityfee 641339 was 611660 budget 674424; tick1347; primary official PDF"),
        ("bud_ivio_pittem_fee_2025", ENT, "2025", "534054", "2025 Pittem cityfee 534054 was 505708 budget 629232; tick1347; primary official PDF"),
        ("bud_ivio_lendelede_fee_2025", ENT, "2025", "476873", "2025 Lendelede cityfee 476873 was 446589 budget 488724; tick1347; primary official PDF"),
        ("bud_ivio_ruiselede_fee_2025", ENT, "2025", "448551", "2025 Ruiselede cityfee 448551 was 404804 budget 481116; exit 31.12.2025 to Wingene/Mirom; tick1347; primary official PDF"),
    ]
    n = append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": bid,
                "entity_id": eid,
                "year": year,
                "amount_eur": amt,
                "amount_min_eur": "",
                "amount_max_eur": "",
                "basis": "executed",
                "source_id": SRC,
                "confidence": "strong",
                "notes": notes,
            }
            for bid, eid, year, amt, notes in budget_rows
        ],
    )
    print("budgets", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": "IVIO Izegem-Ommeland JR2025 leftover IGS dual (cityfee 10.04m / RC 3.08m / statutory WVV missing)",
                "entity_id": ENT,
                "beneficiary": "IVIO / 10 West-Vlaamse gemeentevennoten Izegem Tielt Ardooie Dentergem Ingelmunster Ledegem Lendelede Oostrozebeke Pittem Ruiselede-exit",
                "legal_basis": "Decreet lokaal bestuur IGS; opdrachthoudende vereniging; Bestuursdecreet openbaarheid; WVV neerlegging",
                "decision_date": "2026-05-20",
                "start_year": "1973",
                "end_year": "2025",
                "total_envelope_eur": "10040036",
                "cash_by_year": "",
                "remaining_eur": "3082966",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL Midwest West-Flanders — per-vennoot cityfee / RC 3.08m / statutory WVV missing",
                "cut_option": "Publish statutory WVV/NBB 2025 + per-vennoot 10.04m cityfee dual city lines + RC 3.08m; do not recreate parallel waste-IGS shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1347; cityfee 10040036 BT1 5649253 parks 2274114 BT3 2485441 RC 3082966; statutory WVV unpublished; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "IVIO Izegem-Ommeland JR2025 leftover IGS: cityfee 10.04m / RC 3.08m / statutory WVV missing",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "10040036",
                "total_cost_eur": "10040036",
                "tco_notes": "Leftover dual IGS of mined Midwest West-Flanders cities: cityfee 10.04m / BT1 5.65m / parks 2.27m / BT3 2.49m / retributies 3.30m / RC debt to cities 3.08m; official PDF is glossy operational tables not WVV; do not treat 10.04m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "IVIO / 10 West-Vlaamse gemeenten / Ruiselede exited 31.12.2025",
                "stated_goal": "Local leftover IGS map VL Midwest West-Flanders — JR2025 PDF live; dual cityfee/WVV/NBB FOI",
                "measured_outcome": "Official PDF 2026-08-18: cityfee 10.04m / BT1 5.65m / parks 2.27m / BT3 2.49m / RC 3.08m; statutory WVV unpublished",
                "absurdity_score": "5.8",
                "cost_score": "5.9",
                "difficulty": "3.0",
                "priority_index": "5.9",
                "cut_proposal": "Publish statutory WVV/NBB 2025 + per-vennoot 10.04m cityfee dual city lines + RC 3.08m; do not recreate parallel waste-IGS shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1347; leftover IGS of mined Midwest West-Flanders cities; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "Statutory WVV/BBC/NBB jaarrekening 2025 (assets / omzet / pers / expl / PnL / VTE) — official JR2025 is glossy "
                    "activiteitenverslag with operational tables only + per-vennoot 2025-2026 dual lines for cityfee 10040036 "
                    "(budget 10738248 / 2024 9671746; Tielt 2542169 + Izegem 2317651 + 8 others) + composition of RC debt "
                    "3082966 vs beginsaldo 2486574.54 + extra unsocialised services 102670 + org-wide pers "
                    "(only parks brutolonen +159000 / uitzend DROP 107682 published) + commissarisverslag + AV minutes "
                    "(KBO jaarvergadering april)"
                ),
                "why_it_matters": (
                    "Leftover IGS shell of mined Midwest West-Flanders cities Izegem/Tielt/Ardooie/Dentergem/"
                    "Ingelmunster/Ledegem/Lendelede/Oostrozebeke/Pittem/Ruiselede-exit: 10.04m cityfee / 5.65m BT1 / "
                    "2.27m parks / 2.49m BT3 vs unpublished statutory WVV and 3.08m RC debt to the same cities is a dual "
                    "opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "IVIO Intergemeentelijke vereniging voor duurzaam milieubeleid in Izegem en Ommeland / 10 West-Vlaamse gemeentevennoten",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-18",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM,
                "linked_leaderboard_id": LB,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "tick1347 leftover IGS of mined Midwest West-Flanders cities after honest hunt; "
                    "live JR2025 official PDF now downloads (3.70MB 64p InDesign 20.05.2026) but no embedded WVV. "
                    "Leiedal 2025 InDesign 22MB glossy-only — not taken. "
                    "EcoWerf 2025 glossy / 2024 statutory still unpublished. Interleuven still 2024 balans. "
                    "IOK/IMOG/Haviland/IVBO/Limburg.net still 2024. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1347",
        "title": "IVIO Izegem-Ommeland JR2025 leftover IGS dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: IVIO leftover IGS of mined Midwest West-Flanders cities after honest hunt; "
            "KBO 0213.897.173 Actief; live JR2025 official PDF (3.70MB 64p InDesign 20.05.2026 operational tables; no WVV); "
            "sourced euros cityfee 10.040m / BT1 5.649m / parks 2.274m / BT3 2.485m / RC 3.083m; "
            "FOI ready statutory WVV/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T20:45:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1347 IVIO leftover IGS residual; KBO 0213.897.173; live JR2025 official PDF; "
            "sourced euros; FOI ready not sent; next rq_1348 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1348",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1347 done including IVIO Izegem-Ommeland 1347 leftover IGS live JR operational / "
            "WVI West-Vlaanderen 1346 leftover IGS live WVV / "
            "IVVO Veurne-Ommeland 1345 leftover IGS live WVV / "
            "ILvA Land van Aalst 1344 leftover IGS live WVV / "
            "IVM Meetjesland 1343 leftover IGS live WVV / "
            "IDM Durme-Moervaart 1342 leftover IGS live WVV / "
            "IGEAN dienstverlening 1341 leftover IGS live WVV / "
            "EVA Limburg Sterk Merk 1340 leftover EVA live WVV + every-10 / "
            "WV Zorgbedrijf Brasschaat 1339 leftover zorg live BBC / "
            "WV Zorgband 1338 leftover zorg live BBC / WV Sleutelzorg 1337 leftover zorg FOI-unpublished / "
            "WV Weldenderend 1336 leftover zorg live BBC / WV BVK 1335 leftover zorg live BBC / "
            "WV OPcura 1334 leftover zorg live BBC / WV Het Dak 1333 leftover zorg live BBC / "
            "EVA Inagro 1332 FOI-unpublished / APB Vormingscentrum Malle 1331 FOI-glossy-not-BBC / "
            "EVA Kinderopvang Dilbeek 1330 FOI-unpublished + every-10); "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "Welzijnskoepel West-Brabant jaarverslag 2025 glossy-only — take only if a BBC PDF now downloads; "
            "Ter Nethe official still unpublished/DNS — take only if a PDF now downloads; "
            "Veneco glossy 25MB jaarverslag 2025 InDesign — take only if a WVV/BBC PDF now downloads; "
            "EcoWerf 2025 jaarverslag listed ~16MB glossy / 2024 statutory still unpublished — take only if a WVV/BBC PDF now downloads; "
            "Leiedal 2025 InDesign 22MB 118p downloaded tick1347 — glossy-only no WVV — take only if a WVV/BBC PDF now downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland / IVBO / Limburg.net still 2024 — take only if a 2025 JR PDF now downloads; "
            "IVOO no public 2025 JR PDF — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
            "WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / "
            "WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / "
            "Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / "
            "APB Vonk 1325 / APB Campus Vesta 1324 / AGB Blankenberge 1323 / AGB Aarschot / AGB Arendonk / AGB Lokeren; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403; not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1347 after IVIO leftover IGS live JR operational; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1347", rq_new, rq_spawn)
    print("research_queue 1347", found, "spawned_1348", spawned)

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
                "last_unit_id": "rq_1347",
                "ticks_completed": "1347",
                "paused": "no",
                "notes": (
                    "tick1347 IVIO leftover IGS residual; KBO 0213.897.173; "
                    "live JR2025 official PDF; sourced euros cityfee 10.040m BT1 5.649m parks 2.274m BT3 2.485m RC 3.083m; "
                    "FOI ready statutory WVV; next rq_1348 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log_entry = """
### Tick 1347 - 2026-08-18 - rq_1347 IVIO Izegem-Ommeland dual residual leftover IGS
- Unit: IVIO Intergemeentelijke vereniging voor duurzaam milieubeleid in Izegem en Ommeland (opdrachthoudende vereniging / leftover IGS) of already-mined Midwest West-Flanders cities (Izegem / Tielt / Ardooie / Dentergem / Ingelmunster / Ledegem / Lendelede / Oostrozebeke / Pittem / Ruiselede-exit) after residual dual hunt (KBO **0213.897.173**; official ivio.be + live jaarverslag 2025 PDF 3.70MB / 64p; InDesign **20.05.2026**; operational contribution tables — **no** embedded WVV). Prefer live PDF over another unpublished FOI. Distinct from already-mined WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340. KBO Actief / normale toestand since **17.12.1973**; statutaire naam Intergemeentelijke vereniging voor duurzaam milieubeleid in Izegem en Ommeland since 14.05.2003; afkorting I.V.I.O. since 17.12.1973; Opdrachthoudende vereniging (Vlaams Gewest) since 10.12.2003; zetel Lodewijk de Raetlaan 12 8870 Izegem since 09.12.2013; **11 VE**; RSZ-werkgever since 01.01.2022; btw since 01.04.1996; aanbestedende overheid since 17.12.1973; jaarvergadering april; boekjaar 31 december; voorzitter Jurgen Olivier (Ingelmunster) since 31.03.2025; ondervoorzitter Nico Parmentier (Lendelede); onafhankelijke bestuurder Katelijne Vancleemput; permanent deskundige Rudi Neirynck; e-mail info@ivio.be on official PDF; tel 051 31 17 96; NACE 38.330 / 38.110. Hunt leftover AGB/zorg/EVA first: Leiedal 2025 InDesign 22.24MB / 118p downloaded — glossy-only, no jaarrekening/WVV codes — not taken once live IVIO JR downloaded; EcoWerf 2025 glossy / 2024 statutory still "wordt weldra gepubliceerd" — not taken; Interleuven publications still only jaarrekening 2024 PDF; IOK/IMOG/Haviland/IVBO/Limburg.net still 2024; IVOO no public 2025 JR PDF; MIWA still 2024; Dommelhof leftover Limburg EVA KBO 0777.495.085 not taken once live IVIO PDF downloaded. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek not taken once live IVIO PDF downloaded. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331. Not every-10 (next 1350).
- EUR strong (primary official PDF operational tables; NOT statutory WVV/BBC): cityfee **10.040.036** (was 9.671.746; budget **10.738.248**; 7% under / +4% vs 2024); BT1 ophaling **5.649.253** (was 5.643.056; budget 5.020.112); parks **2.274.114** (was 2.125.398; budget 2.521.032); BT3 afzet **2.485.441** (was 2.155.826; budget 3.117.040); retributies **3.303.540** (HV 3.043.132 + PMD 260.408; voorschot 3.397.488 / saldo **−93.948**); RC schuld aan gemeenten **3.082.966**; extra diensten **102.670**; Izegem groen zakken **38.164**; park afschrijvingen **229.923** (was 179.435); Recupel **91.738**; Valumat **156.000**; burger-parkontvangsten **228.127**; textiel DROP **93.000** vs 431.375. Per-vennoot cityfee 2025: Tielt **2.542.169** / Izegem **2.317.651** / Ingelmunster **888.691** / Ledegem **754.173** / Ardooie **751.458** / Dentergem **685.077** / Oostrozebeke **641.339** / Pittem **534.054** / Lendelede **476.873** / Ruiselede **448.551** (exit 31.12.2025). Org-wide pers / VTE / assets / omzet / expl / PnL unpublished.
- CSVs: sources+4/entities+1/budgets+27/commitments+1/leaderboard+1 + FOI ready `gap_ivio_cityfee_10_04m_statutory_wvv_l5` (not sent); rq_1347=done; spawn rq_1348; ticks=1347.
- Coverage: residual dual L5 (IVIO leftover IGS live JR operational). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1348 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland/IVBO/Limburg.net only if a 2025 JR PDF now downloads; EcoWerf only if a statutory WVV/BBC PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 unless a fetchable JR appears).
"""
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1347 write done")


if __name__ == "__main__":
    main()

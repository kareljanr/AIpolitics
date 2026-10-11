# -*- coding: utf-8 -*-
"""Tick 1387 — leftover Fluvius Halle-Vilvoorde JR2025 official NBB WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10 (next 1390).
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1387"
UTC = "2026-08-19T04:55:00Z"
ENT = "igs_flhv"
HIER = "Vlaanderen>VlaamsBrabant>IGS>FluviusHalleVilvoorde"
GAP = "gap_flhv_omzet_238_16m_diensten_76_14m_debt_1_01bn_l5"
SRC = "src_flhv_jr2025_nbb"
SRC2 = "src_flhv_site"
SRC3 = "src_kbo_flhv_0229921078"
SRC4 = "src_flhv_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00227458.pdf"
SRC2_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-halle-vilvoorde/activiteitenverslagen"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0229921078"
SRC4_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-halle-vilvoorde"
FOI_EMAIL = ""
FOI_POSTAL = "Grote Markt z/n 1800 Vilvoorde"
DRAFT = "docs/doge/foi/drafts/gap_flhv_omzet_238_16m_diensten_76_14m_debt_1_01bn_l5.md"
COMM = "comm_flhv_jr2025_pnl"
LB = "lb_flhv_omzet_238_16m_diensten_76_14m_debt_1_01bn"


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

VENNOTEN = (
    "Affligem + Asse + Beersel + Dilbeek + Drogenbos + Grimbergen + Halle + "
    "Kapelle-op-den-Bos + Kraainem + Lennik + Liedekerke + Linkebeek + "
    "Londerzeel + Machelen + Meise + Merchtem + Opwijk + Pajottegem + "
    "Pepingen + Roosdaal + Sint-Genesius-Rode + Sint-Pieters-Leeuw + "
    "Steenokkerzeel + Ternat + Vilvoorde + Wemmel + Wezembeek-Oppem + "
    "Zaventem + Zemst"
)


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "Fluvius Halle-Vilvoorde (voorheen Sibelgas) jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00227458; AV 16.06.2026)",
                "url": SRC_URL,
                "publisher": "Fluvius Halle-Vilvoorde / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1387; official NBB VOL-inb PDF 1.41MB 91p deposit 2026-00227458 header 26.06.2026; "
                    "leftover IGS energy DSO of 29 Halle-Vilvoorde municipalities after Sibelgas+deel Iverlek/PBE 01.01.2025; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / "
                    "Paul Eelen + Line Vyvey oordeel zonder voorbehoud assets 1355438683 / te bestemmen 15197948 + benadrukking 6.19 regulatoire saldi; "
                    "VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.8/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62 empty"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Fluvius Halle-Vilvoorde official governance + jaarverslag 2025 (leftover IGS energy DSO; voorheen Sibelgas; 29 vennoten)",
                "url": SRC2_URL,
                "publisher": "Fluvius / Fluvius Halle-Vilvoorde",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1387; leftover IGS of 29 Halle-Vilvoorde municipalities; "
                    "over.fluvius.be lists activiteitenverslagen + JR2025; statutory 2025 balans is the NBB CDN deposit; fusie Sibelgas+deel Iverlek/PBE januari 2025"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Fluvius Halle-Vilvoorde 0229.921.078",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1387; KBO 0229.921.078 Actief / normale toestand since 19.12.1986; "
                    "statutaire naam Fluvius Halle-Vilvoorde since 01.01.2025; "
                    "Opdrachthoudende vereniging (Vlaams Gewest) since 01.07.2015; "
                    "zetel Grote Markt z/n 1800 Vilvoorde since 26.06.2018; 0 VE; "
                    "no KBO email/web/tel; btw since 01.01.1987; "
                    "boekjaar 31 december; NACE 35.220/35.140; vervangt 0869.605.691 (08.04.2016)"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Fluvius Halle-Vilvoorde FOI channel / official governance + secretariaat (KBO no email)",
                "url": SRC4_URL,
                "publisher": "Fluvius Halle-Vilvoorde",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1387; KBO no email/web/tel; zetel Grote Markt z/n 1800 Vilvoorde; "
                    "secretariaat Brusselsesteenweg 199 9090 Merelbeke-Melle; "
                    "no dedicated openbaarheid mailbox found on official pages this tick"
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
                "name_nl": "Fluvius Halle-Vilvoorde (voorheen Sibelgas; leftover IGS energy DSO Halle-Vilvoorde)",
                "name_fr": "Fluvius Hal-Vilvorde (ex-Sibelgas; IGS residuel DSO energie Hal-Vilvorde)",
                "name_en": "Fluvius Halle-Vilvoorde leftover IGS energy DSO (formerly Sibelgas)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1387 leftover residual IGS energy DSO of 29 Halle-Vilvoorde municipalities; "
                    "KBO 0229.921.078 Actief since 19.12.1986; naam Fluvius Halle-Vilvoorde since 01.01.2025; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 1355438683 omzet 238155358 diensten 76141115 debt 1011846980 pnl 15189063 equity 343177460 dividend 4356632; "
                    "FOI ready omzet geo empty / 36.8m 74 empty 740 / 76.1m 61 / 1.01bn debt / 4.36m dividend; "
                    "distinct from already-mined Fluvius EG group entity fluvius and Antwerpen 1386 / West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382"
                ),
            },
        ],
    )
    print("entities", n)
    budget_rows = []
    with open("/tmp/doge1387/budgets.tsv", encoding="utf-8") as bf:
        for line in bf:
            line = line.rstrip("\n")
            if not line:
                continue
            bid, year, amt, notes = line.split("\t", 3)
            budget_rows.append((bid, ENT, year, amt, notes))
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
                "title": "Fluvius Halle-Vilvoorde JR2025 leftover IGS dual (assets 1.36bn / omzet 238.16m / diensten 76.14m / debt 1.01bn / dividend 4.36m)",
                "entity_id": ENT,
                "beneficiary": "Fluvius Halle-Vilvoorde / " + VENNOTEN,
                "legal_basis": "WVV OV; Decreet Lokaal Bestuur; Energiedecreet; NBB neerlegging",
                "decision_date": "2026-06-16",
                "start_year": "1986",
                "end_year": "",
                "total_envelope_eur": "1355438683",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL energy DSO — 238.16m omzet (geo empty) / 76.14m diensten / 1.01bn debt / 4.36m dividend",
                "cut_option": "Publish unpublished omzet geo + 36.8m 74 + 76.1m 61 FSO pass-through + 1.01bn debt counterparties + 4.36m dividend per vennoot; do not keep DSO IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1387; assets 1355438683 omzet 238155358 diensten 76141115 debt 1011846980 pnl 15189063 equity 343177460 dividend 4356632; FOI ready not sent; not TE-additive of 348bn; double_count vs Fluvius EG possible",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Fluvius Halle-Vilvoorde JR2025 leftover IGS: assets 1.36bn / omzet 238.16m / diensten 76.14m / debt 1.01bn / dividend 4.36m / 0 VTE",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "76141115",
                "total_cost_eur": "1355438683",
                "tco_notes": (
                    "Leftover dual IGS energy DSO of 29 Halle-Vilvoorde municipalities (voorheen Sibelgas): "
                    "assets 1.36bn / equity 343.18m / pnl +15.19m / omzet 238.16m (geo empty) / "
                    "diensten 76.14m / 0 VTE / debt 1.01bn (related 261.75m) / dividend 4.36m / cash 1357; "
                    "official NBB WVV live; do not treat 1.36bn as TE-additive of 348bn; double_count vs Fluvius EG possible"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Fluvius Halle-Vilvoorde / " + VENNOTEN,
                "stated_goal": "Local leftover IGS map VL energy DSO — JR2025 live; dual omzet-geo/diensten/debt/dividend FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 1.36bn / omzet 238.16m / diensten 76.14m / debt 1.01bn / dividend 4.36m / pnl +15.19m / 0 VTE",
                "absurdity_score": "7.1",
                "cost_score": "8.3",
                "difficulty": "3.0",
                "priority_index": "7.2",
                "cut_proposal": "Publish unpublished omzet geo + 36.8m 74 + 76.1m 61 FSO pass-through + 1.01bn debt counterparties + 4.36m dividend per vennoot; do not keep DSO IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1387; leftover IGS of 29 Halle-Vilvoorde municipalities; FOI ready not sent; not TE-additive of 348bn; distinct from Fluvius EG and Antwerpen 1386 / West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382",
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
                    "omzet 238155358 JUMP vs 47051256 (WVV 70; 6.10 category elek 187129541 / gas 47431873 / other 3593943; geo empty) per vennoot/tariefstroom unpublished "
                    "+ andere bedrijfsopbrengsten 36778722 (WVV 74; 740 empty) "
                    "+ diensten 76141115 vs 18425605 (WVV 61; no split) + goods 96237287 + FSO pass-through (pers 62/9087 empty / 0 VTE) "
                    "+ schulden 1011846980 (LT bank 270662356; LT other 577795926; related-party 261746783) counterparties/rente unpublished "
                    "+ FVA other shares 33322350 unpublished "
                    "+ dividend 4356632 vs 1531181 per vennoot unpublished "
                    "+ cash 1357 vs debt 1.01bn + prepaid 34491680 (regulatoire gas 13539209) + VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.8/6.18/9 not filed"
                ),
                "why_it_matters": (
                    "Leftover IGS OV energy DSO of 29 mined Halle-Vilvoorde municipalities "
                    "(same leftover-IGS energy seam as Fluvius Antwerpen 1386 / West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382; distinct from Fluvius EG): "
                    "1.36bn assets / 238.16m omzet / 76.14m diensten / 1.01bn debt / 4.36m dividend / "
                    "0 VTE / FSO shell "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Fluvius Halle-Vilvoorde / Raad van Bestuur / Jan Desmeth / Bjorn Verdoodt / 29 Halle-Vilvoorde vennoten",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-19",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM,
                "linked_leaderboard_id": LB,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "tick1387 leftover IGS OV energy DSO of 29 Halle-Vilvoorde municipalities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (1.41MB 91p deposit 2026-00227458). "
                    "Fluvius Antwerpen already mined 1386 — skipped. Fluvius West already mined 1385 — skipped. Fluvius Kempen already mined 1384 — skipped. "
                    "Imewo already mined 1383 — skipped. INTERGEM already mined 1382 — skipped. "
                    "Other Fluvius DNB holdings (Limburg CDN 2026-00218151 live / Zenne-Dijle) leftover next. "
                    "Dommelhof leftover Limburg EVA 0777.495.085 not re-probed once live Halle-Vilvoorde extracted. "
                    "Otary RS Nuhma-adjacent fallback not taken. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)
    rq_new = {
        "task_id": "rq_1387",
        "title": "Fluvius Halle-Vilvoorde / Sibelgas JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Fluvius Halle-Vilvoorde leftover IGS energy DSO of 29 Halle-Vilvoorde municipalities after honest hunt; "
            "KBO 0229.921.078 Actief; live JR2025 official NBB WVV VOL-inb PDF (1.41MB 91p deposit 2026-00227458; commissaris EY); "
            "sourced euros assets 1355438683 / omzet 238155358 / diensten 76141115 / debt 1011846980 / pnl 15189063 / dividend 4356632; "
            "FOI ready omzet geo empty / 36.8m 74 / 76.1m 61 / 1.01bn debt / 4.36m dividend"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T04:20:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1387 Fluvius Halle-Vilvoorde leftover IGS energy residual; KBO 0229.921.078; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1388 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1388",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1387 done including Fluvius Halle-Vilvoorde 1387 leftover energy IGS live NBB WVV / "
            "Fluvius Antwerpen 1386 leftover energy IGS live NBB WVV / "
            "Fluvius West 1385 leftover energy IGS live NBB WVV / "
            "Fluvius Kempen 1384 leftover energy IGS live NBB WVV / "
            "Fluvius Imewo 1383 leftover energy IGS live NBB WVV / "
            "INTERGEM / Fluvius Midden-Vlaanderen 1382 leftover energy IGS live NBB WVV); "
            "other Fluvius DNB holdings leftover energy IGS (Limburg CDN 2026-00218151 live / Zenne-Dijle) — take if a 2025 CDN/JR PDF still live and unmined; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
            "skip already-mined Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1387 after Fluvius Halle-Vilvoorde leftover energy IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1387", rq_new, rq_spawn)
    print("research_queue 1387", found, "spawned_1388", spawned)

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
                "last_unit_id": "rq_1387",
                "ticks_completed": "1387",
                "paused": "no",
                "notes": (
                    "tick1387 Fluvius Halle-Vilvoorde leftover IGS energy residual; KBO 0229.921.078; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 1355438683 omzet 238155358 diensten 76141115 debt 1011846980 pnl 15189063 equity 343177460 dividend 4356632; "
                    "FOI ready omzet geo empty/36.8m 74/76.1m 61/1.01bn debt/4.36m div; next rq_1388 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")
    log = ROOT / "loop_log.md"
    entry = (
        "### Tick 1387 - 2026-08-19 - rq_1387 Fluvius Halle-Vilvoorde / Sibelgas dual residual leftover\\n"
        "- Unit: Fluvius Halle-Vilvoorde (voorheen Sibelgas; leftover IGS opdrachthoudende vereniging / energy DSO elektriciteit + aardgas of 29 mined Halle-Vilvoorde municipalities after 01.01.2025 fusie Sibelgas + deel Iverlek/PBE; werkmaatschappij Fluvius System Operator) after residual dual hunt (KBO **0229.921.078**; official over.fluvius.be has activiteitenverslagen/governance + jaarverslag 2025; live NBB WVV VOL-inb deposit **2026-00227458** PDF 1.41MB / 91p; AV **16.06.2026**; header **26.06.2026**; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / Paul Eelen A02213 + Line Vyvey A02501 signed 26.03.2026 oordeel zonder voorbehoud assets 1.355.438.683 / te bestemmen +15.197.948 + benadrukking VOL-inb 6.19 regulatoire saldi 2025-2028). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; preferred leftover Fluvius DNB holding this tick). Distinct from already-mined Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / Fluvius EG group-level (entity fluvius). First confirmed not already mined: no Fluvius Halle-Vilvoorde / Sibelgas / 0229.921.078 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **19.12.1986**; statutaire naam Fluvius Halle-Vilvoorde since 01.01.2025; Opdrachthoudende vereniging (Vlaams Gewest) since 01.07.2015; zetel Grote Markt z/n 1800 Vilvoorde since 26.06.2018; **0 VE**; KBO no email/web/tel; official site https://over.fluvius.be/; btw since 01.01.1987; boekjaar 31 december; NACE 35.220/35.140. Vervangt 0869.605.691 (08.04.2016). Voorzitter Jan Desmeth; secretaris Bjorn Verdoodt; commissaris EY since 23.06.2025 tot 23.06.2028. Hunt leftover Fluvius DNB first: Halle-Vilvoorde statutory CDN live this tick (HTTP 200 / 1408540 / 91p) — taken. Fluvius Antwerpen already mined 1386 — skipped. Fluvius West already mined 1385 — skipped. Fluvius Kempen already mined 1384 — skipped. Imewo already mined 1383 — skipped. INTERGEM already mined 1382 — skipped. Limburg CDN 2026-00218151 live leftover next. Zenne-Dijle leftover after Limburg. Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live Halle-Vilvoorde extracted. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Not every-10 (next 1390).\\n"
        "- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud assets 1.355.438.683 / te bestemmen +15.197.948 + benadrukking 6.19; VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.8/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62/9087 empty): assets **1.355.438.683** (was 284.464.478 JUMP na fusie); fixed **1.173.663.587** / MVA **1.123.655.974** (gebouwen **7.989.142**; machines **978.008.596**; meubilair **5.021.297**; leasing **8.042.236**; overige **640.258**; CIP **123.954.446** aanschaf **198.701.230**); IVA 8.981.337; FVA **41.026.276** (deelnemingen **7.703.925** FSO 6,39% / 7,26% K-SYN + Transco 11,11%; andere aandelen **33.322.350**); current **181.775.096**; cash **1.357**; prepaid **34.491.680** (regulatoire gas 13.539.209); equity **343.177.460** (inbreng 168.452.281; reval 51.345.743; reserves 96.463.971; overgedragen 26.085.863; capsub 829.602); voorzieningen **414.243**; schulden **1.011.846.980** (LT **856.337.100** waarvan bank **270.662.356** + lease 7.878.818 + other 577.795.926; ST **105.925.518** waarvan leveranciers **42.454.133 JUMP**; related-party FSO-seam **261.746.783**); omzet **238.155.358 JUMP** vs 47.051.256 (elek **187.129.541** / gas **47.431.873** / other **3.593.943**; geo empty); othops **36.778.722** (740 empty); goods **96.237.287**; diensten **76.141.115** vs 18.425.605; pers **empty / 0 VTE**; afschr 47.090.782; expl **+40.417.136** vs +4.209.346; fin opbr 5.887.614; fin kosten 26.263.851; tax 4.872.862; PnL **+15.189.063** vs -306.424; dividend **4.356.632** vs 1.531.181; commissaris 11.719 + extra 35.329; bestuurders 31.580.\\n"
        "- CSVs: sources+4/entities+1/budgets+76/commitments+1/leaderboard+1 + FOI ready \`gap_flhv_omzet_238_16m_diensten_76_14m_debt_1_01bn_l5\` (not sent); rq_1387=done; spawn rq_1388; ticks=1387.\\n"
        "- Coverage: residual dual L5 (Fluvius Halle-Vilvoorde leftover energy IGS live WVV). Does **not** move L5 near-complete of EUR 347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs Fluvius EG possible. No progress refresh (not every-10; next 1390).\\n"
        "- Next: rq_1388 residual dual L5 VL JR2025 hole_fill (prefer leftover Fluvius Limburg CDN 2026-00218151 live / Zenne-Dijle if a 2025 CDN/JR PDF still live and unmined; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS only after leftover IGS/EVA/AGB; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382).\\n"
    )
    entry = entry.replace(chr(92)+"n", chr(10))
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1387 write done")


if __name__ == "__main__":
    main()

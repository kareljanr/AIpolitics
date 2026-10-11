# -*- coding: utf-8 -*-
"""Tick 1352 — leftover IGS IVBO JR2025 official euros.
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

TICK = "1352"
UTC = "2026-08-18T23:20:00Z"
ENT = "igs_ivbo"
HIER = "Vlaanderen>WestVlaanderen>IGS>IVBO>BruggeOmmeland"
GAP = "gap_ivbo_omzet_55_56m_assets_79_79m_pers_19_85m_l5"
SRC = "src_ivbo_jr2025_pdf"
SRC2 = "src_ivbo_site"
SRC3 = "src_kbo_ivbo_0214015751"
SRC4 = "src_ivbo_foi_contact"
SRC_URL = "https://www.ivbo.be/sites/default/files/2026-06/Jaarverslag%202025_kl.pdf"
SRC2_URL = "https://www.ivbo.be/over-ivbo/publicaties/beleidspublicaties/jaarverslag"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0214015751"
SRC4_URL = "https://www.ivbo.be/over-ivbo"
FOI_EMAIL = "info@ivbo.be"
FOI_POSTAL = "Pathoekeweg 41 8000 Brugge"
DRAFT = "docs/doge/foi/drafts/gap_ivbo_omzet_55_56m_assets_79_79m_pers_19_85m_l5.md"
COMM = "comm_ivbo_jr2025_omzet"
LB = "lb_ivbo_omzet_55_56m_assets_79_79m_pers_19_85m"


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
                "title": "IVBO jaarverslag boekjaar 2025 (official JR + commissarisverslag WVV VOL-inb; InDesign 25.06.2026)",
                "url": SRC_URL,
                "publisher": "IVBO opdrachthoudende vereniging",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1352; official PDF 19.8MB 106p InDesign 25.06.2026; leftover IGS waste "
                    "of mined Brugge-ommeland cities; embedded WVV VOL-inb image pages 51-89 + "
                    "commissaris Auditas oordeel zonder voorbehoud assets 79787842 PnL 565857"
                ),
            },
            {
                "source_id": SRC2,
                "title": "IVBO official jaarverslag page (KBO 0214.015.751)",
                "url": SRC2_URL,
                "publisher": "IVBO",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1352; leftover IGS waste of mined Brugge-ommeland cities; "
                    "lists Jaarverslag 2025_kl.pdf (was 2024 last ticks)"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO IVBO 0214.015.751",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1352; KBO 0214.015.751 Actief / normale toestand since 07.01.1974; "
                    "statutaire naam Intergemeentelijk Samenwerkingsverband voor Vuilverwijdering "
                    "en- Verwerking in Brugge en Ommeland since 16.07.2004; afkorting I.V.B.O. "
                    "since 07.01.1974; Opdrachthoudende vereniging (Vlaams Gewest) since 28.11.2003; "
                    "zetel Pathoekeweg 41 8000 Brugge since 23.11.1993; 10 VE; aanbestedende overheid "
                    "since 07.01.1974; btw since 01.01.1982; RSZ since 01.01.2022; jaarvergadering juni; "
                    "boekjaar 31 december; databank 17.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "IVBO FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "IVBO",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1352; FOI info@ivbo.be; Pathoekeweg 41 8000 Brugge; T 050 45 63 11; "
                    "voorzitter Pieter Marechal since 28.03.2025"
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
                "name_nl": "IVBO (leftover IGS afval Brugge en Ommeland)",
                "name_fr": "IVBO (association de mission / IGS residuel / dechets Bruges et hinterland)",
                "name_en": "IVBO Bruges hinterland waste intermunicipal (leftover IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.ivbo.be",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1352 leftover IGS residual waste of mined Brugge-ommeland cities "
                    "(Brugge/Beernem/Blankenberge/Damme/De Haan/Jabbeke/Oostkamp/Zedelgem/"
                    "Zuienkerke; Damme JR already books IVBO toelage 0.91m); "
                    "KBO 0214.015.751 Actief since 07.01.1974; official JR2025 PDF downloads; "
                    "sourced euros omzet 55.564m / assets 79.788m / pers 19.848m / PnL 0.566m; "
                    "FOI ready per-vennoot/debt/NBB"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_ivbo_assets_2025", ENT, "2025", "79787842", "2025 assets 79787842.04 commissaris; tick1352; primary official JR WVV"),
        ("bud_ivbo_assets_2024", ENT, "2024", "72373546", "2024 assets 72373545.78 comparative; tick1352; primary official JR WVV"),
        ("bud_ivbo_pnl_2025", ENT, "2025", "565857", "2025 PnL 565857.29; tick1352; primary official JR + commissaris"),
        ("bud_ivbo_pnl_2024", ENT, "2024", "4157073", "2024 PnL 4157072.91 comparative; tick1352; primary official JR WVV"),
        ("bud_ivbo_fixed_2025", ENT, "2025", "59870560", "2025 vaste activa 59870559.55; tick1352; primary official JR WVV 21/28"),
        ("bud_ivbo_current_2025", ENT, "2025", "19917282", "2025 vlottende activa 19917282.49; tick1352; primary official JR WVV 29/58"),
        ("bud_ivbo_equity_2025", ENT, "2025", "47041659", "2025 eigen vermogen 47041659.36; tick1352; primary official JR WVV 10/15"),
        ("bud_ivbo_omzet_2025", ENT, "2025", "55563611", "2025 omzet 55563611.27; tick1352; primary official JR WVV 70"),
        ("bud_ivbo_omzet_2024", ENT, "2024", "55986935", "2024 omzet 55986934.74 comparative; tick1352; primary official JR WVV 70"),
        ("bud_ivbo_opsrev_2025", ENT, "2025", "56727155", "2025 bedrijfsopbrengsten 56727155.06; tick1352; primary official JR WVV 70/76A"),
        ("bud_ivbo_pers_2025", ENT, "2025", "19848202", "2025 bezoldigingen 19848201.64; tick1352; primary official JR WVV 62"),
        ("bud_ivbo_diensten_2025", ENT, "2025", "20927494", "2025 diensten 20927494.49; tick1352; primary official JR WVV 61"),
        ("bud_ivbo_goods_2025", ENT, "2025", "6242211", "2025 handelsgoederen 6242211.35; tick1352; primary official JR WVV 60"),
        ("bud_ivbo_afschr_2025", ENT, "2025", "6082679", "2025 afschrijvingen 6082679.37; tick1352; primary official JR WVV 630"),
        ("bud_ivbo_expl_2025", ENT, "2025", "1016371", "2025 bedrijfswinst 1016370.66; tick1352; primary official JR WVV 9901"),
        ("bud_ivbo_cash_2025", ENT, "2025", "4224002", "2025 liquide middelen 4224002.30; tick1352; primary official JR WVV 54/58"),
        ("bud_ivbo_invest_2025", ENT, "2025", "3400000", "2025 geldbeleggingen 3400000 DROP vs 5200000; tick1352; primary official JR WVV 50/53"),
        ("bud_ivbo_invest_2024", ENT, "2024", "5200000", "2024 geldbeleggingen 5200000 comparative; tick1352; primary official JR WVV 50/53"),
        ("bud_ivbo_strecv_2025", ENT, "2025", "8014686", "2025 ST vorderingen 8014685.83; tick1352; primary official JR WVV 40/41"),
        ("bud_ivbo_stock_2025", ENT, "2025", "3228807", "2025 voorraden 3228807.14; tick1352; primary official JR WVV 30/36"),
        ("bud_ivbo_buildings_2025", ENT, "2025", "25248946", "2025 terreinen/gebouwen 25248946.35 JUMP vs 11970908.07; tick1352; primary official JR WVV 22"),
        ("bud_ivbo_buildings_2024", ENT, "2024", "11970908", "2024 terreinen/gebouwen 11970908.07 comparative; tick1352; primary official JR WVV 22"),
        ("bud_ivbo_prov_2025", ENT, "2025", "3994400", "2025 voorzieningen 3994400; tick1352; primary official JR WVV 16"),
        ("bud_ivbo_kapsu_2025", ENT, "2025", "874009", "2025 kapitaalsubsidies 874008.77 DROP vs 2930135.90; tick1352; primary official JR WVV 15"),
        ("bud_ivbo_cityinc_2025", ENT, "2025", "3105551", "2025 inkomsten verwerkte hoeveelheden gemeente-vennoten 3105551; tick1352; primary official JR table"),
        ("bud_ivbo_thirdinc_2025", ENT, "2025", "14839827", "2025 inkomsten derden+vennoten C 14839827; tick1352; primary official JR table"),
        ("bud_ivbo_cityinc_brugge_2025", ENT, "2025", "1487736", "2025 Brugge incineration income 1487736; tick1352; primary official JR table"),
        ("bud_ivbo_cityinc_blankenberge_2025", ENT, "2025", "384867", "2025 Blankenberge incineration income 384867; tick1352; primary official JR table"),
        ("bud_ivbo_fincost_2025", ENT, "2025", "556846", "2025 financiele kosten 556845.67; tick1352; primary official JR WVV 65"),
        ("bud_ivbo_fininc_2025", ENT, "2025", "129828", "2025 financiele opbrengsten 129828.19; tick1352; primary official JR WVV 75"),
        ("bud_ivbo_inbreng_2025", ENT, "2025", "5924200", "2025 inbreng 5924200; tick1352; primary official JR WVV 10/11"),
        ("bud_ivbo_mva_2025", ENT, "2025", "57763519", "2025 materiele VA 57763519.40; tick1352; primary official JR WVV 22/27"),
        ("bud_ivbo_iva_2025", ENT, "2025", "1990720", "2025 immateriele VA 1990720.38; tick1352; primary official JR WVV 21"),
        ("bud_ivbo_otherops_2025", ENT, "2025", "1019170", "2025 andere bedrijfsopbrengsten 1019170.36; tick1352; primary official JR WVV 74"),
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
                "title": "IVBO JR2025 leftover IGS dual (omzet 55.56m / assets 79.79m / pers 19.85m)",
                "entity_id": ENT,
                "beneficiary": "IVBO / 9 Brugge-ommeland vennoten A",
                "legal_basis": "Decreet lokaal bestuur IGS; opdrachthoudende vereniging; Bestuursdecreet openbaarheid; WVV neerlegging",
                "decision_date": "2026-06-25",
                "start_year": "1974",
                "end_year": "2025",
                "total_envelope_eur": "79787842",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL waste — per-vennoot 55.56m omzet / 3.11m city incineration / NBB",
                "cut_option": "Publish per-vennoot 55.56m omzet / 3.11m city incineration dual city lines + ST/LT debt split + full statutory NBB; do not recreate parallel Brugge-ommeland waste IGS shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1352; omzet 55563611 assets 79787842 pers 19848202 PnL 565857; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "IVBO JR2025 leftover IGS: omzet 55.56m / assets 79.79m / pers 19.85m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "55563611",
                "total_cost_eur": "79787842",
                "tco_notes": "Leftover dual IGS waste of mined Brugge-ommeland cities: omzet 55.56m / pers 19.85m / city incineration 3.11m / assets 79.79m / PnL 0.57m DROP vs 4.16m; official JR live; do not treat 79.79m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "IVBO / 9 Brugge-ommeland vennoten A",
                "stated_goal": "Local leftover IGS map VL waste — JR2025 live; dual omzet/city incineration/NBB FOI",
                "measured_outcome": "Official JR 2026-08-19: omzet 55.56m / assets 79.79m / pers 19.85m / PnL 0.57m; commissaris zonder voorbehoud",
                "absurdity_score": "6.2",
                "cost_score": "6.8",
                "difficulty": "3.0",
                "priority_index": "6.2",
                "cut_proposal": "Publish per-vennoot 55.56m omzet / 3.11m city incineration dual city lines + ST/LT debt + full statutory NBB; do not recreate parallel Brugge-ommeland waste IGS shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1352; leftover IGS waste of mined Brugge-ommeland cities; FOI ready not sent; not TE-additive of 348bn",
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
                    "Per-vennoot 2025-2026 dual lines for omzet 55563611.27 + city incineration "
                    "income 3105551 (Brugge 1487736 / Blankenberge 384867 / Oostkamp 269020 / "
                    "Zedelgem 268825 / De Haan 209309 / Beernem 175699 / Jabbeke 175733 / Damme "
                    "103317 / Zuienkerke 31045) + derden/vennoten C 14839827 + exact WVV ST/LT "
                    "debt split of residual ~28751783 (assets 79787842.04 - EV 47041659.36 - "
                    "voorzieningen 3994400) + bezoldigingen 19848201.64 recon vs 237 koppen / "
                    "232.77 VTE + commissaris ereloon + geldbeleggingen DROP 5200000 to 3400000 "
                    "vs cash 4224002.30 + full statutory jaarrekening machine-readable (WVV is "
                    "image pages) + AV 25.06.2026 minutes + NBB filing"
                ),
                "why_it_matters": (
                    "Leftover IGS waste shell of mined Brugge-ommeland cities "
                    "(Brugge/Beernem/Blankenberge/Damme/De Haan/Jabbeke/Oostkamp/Zedelgem/"
                    "Zuienkerke; Damme JR already books IVBO toelage 0.91m): 55.56m omzet vs "
                    "19.85m pers / 3.11m city incineration / 79.79m assets / PnL 0.57m DROP vs "
                    "4.16m is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "IVBO / 9 Brugge-ommeland vennoten A",
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
                    "tick1352 leftover IGS waste of mined Brugge-ommeland cities after honest hunt; "
                    "live JR2025 official PDF now extracted (19.8MB 106p InDesign 25.06.2026). "
                    "Limburg.net 2025 JR now downloads 17p InDesign — not taken once live IVBO WVV. "
                    "Westtoer APB BBC 2025 now downloads — leftover APB later. "
                    "IOK/IMOG/Haviland still 2024. Interleuven still 2024 balans. "
                    "EcoWerf/Veneco/Leiedal glossy. IVAGO SSL EOF. MIWA flipbook. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1352",
        "title": "IVBO JR2025 leftover IGS dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: IVBO leftover IGS waste of mined Brugge-ommeland cities "
            "after honest hunt; KBO 0214.015.751 Actief; live JR2025 official WVV PDF "
            "(19.8MB 106p InDesign 25.06.2026 + commissaris Auditas); "
            "sourced euros omzet 55.564m / assets 79.788m / pers 19.848m / PnL 0.566m; "
            "FOI ready per-vennoot/debt/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T22:50:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1352 IVBO leftover IGS residual; KBO 0214.015.751; "
            "live JR2025 WVV PDF; sourced euros; FOI ready not sent; next rq_1353 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1353",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1352 done including IVBO 1352 leftover IGS live WVV / "
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
            "Westtoer APB BBC jaarrekening 2025 now downloads (124p 26.03.2026) — take if still unmined; "
            "Limburg.net jaarverslag_2025.pdf now downloads (17p InDesign 11.06.2026) — take only if WVV/BBC euros; "
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
            "skip already-mined IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
            "WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / "
            "WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403; not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1352 after IVBO leftover IGS live WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1352", rq_new, rq_spawn)
    print("research_queue 1352", found, "spawned_1353", spawned)

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
                "last_unit_id": "rq_1352",
                "ticks_completed": "1352",
                "paused": "no",
                "notes": (
                    "tick1352 IVBO leftover IGS residual; KBO 0214.015.751; "
                    "live JR2025 WVV PDF; sourced euros omzet 55.564m assets 79.788m pers 19.848m PnL 0.566m; "
                    "FOI ready per-vennoot/debt/NBB; next rq_1353 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1352 - 2026-08-19 - rq_1352 IVBO dual residual leftover IGS
- Unit: IVBO (opdrachthoudende vereniging / leftover IGS waste; statutaire naam Intergemeentelijk Samenwerkingsverband voor Vuilverwijdering en- Verwerking in Brugge en Ommeland) of already-mined Brugge-ommeland cities (Brugge / Beernem / Blankenberge / Damme / De Haan / Jabbeke / Oostkamp / Zedelgem / Zuienkerke; Damme JR already books IVBO toelage 0.91m) after residual dual hunt (KBO **0214.015.751**; official ivbo.be + live jaarverslag 2025 PDF 19.8MB / 106p; InDesign **25.06.2026**; AV **25.06.2026**; embedded WVV VOL-inb image pages 51-89 + commissaris Auditas). Leftover IGS whose official page now yields a downloadable JR2025 PDF with euros (prefer live PDF over another unpublished FOI). Distinct from already-mined SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341. KBO Actief / normale toestand since **07.01.1974**; Opdrachthoudende vereniging (Vlaams Gewest) since 28.11.2003; zetel Pathoekeweg 41 8000 Brugge since 23.11.1993; **10 VE**; aanbestedende overheid since 07.01.1974; btw since 01.01.1982; RSZ since 01.01.2022; jaarvergadering juni; boekjaar 31 december; voorzitter Pieter Marechal since 28.03.2025; e-mail info@ivbo.be; tel 050 45 63 11; NACE 38.330 / 36.000. 9 vennoten A. Hunt leftover AGB/zorg/EVA first: Limburg.net jaarverslag_2025.pdf now downloads (17p InDesign 11.06.2026) — not taken once live IVBO WVV extracted; Westtoer APB BBC jaarrekening 2025 now downloads (124p 26.03.2026) — leftover APB later; IOK/IMOG/Haviland still 2024; Interleuven still 2024 balans; EcoWerf 2025 glossy / 2024 statutory unpublished; IVAREM activiteitenverslag 2025 glossy; IGEMO activiteitenverslag only; IVOO AV 15.06.2026 overzichtslijst only; Veneco/Leiedal glossy-only; IVAGO SSL EOF; MIWA flipbook; MIROM Cloudflare; De Schorre provincieantwerpen.be 403; APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas no fetchable PDF; Dommelhof leftover Limburg EVA KBO 0777.495.085 not taken once live IVBO extracted. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345. Not every-10 (next 1360).
- EUR strong (primary official WVV + commissaris Auditas assets 79.787.842,04 / PnL 565.857,29): assets **79.787.842** (was 72.373.546); fixed **59.870.560**; MVA **57.763.519** (gebouwen **25.248.946** JUMP vs 11.970.908 + installaties **25.131.760** + rollend **5.189.627** + lease **888.486** + CIP **1.304.700**); IVA **1.990.720**; FVA **116.320**; current **19.917.282**; voorraden **3.228.807**; ST recv **8.014.686** (trade **7.695.944**); beleggingen **3.400.000** DROP vs 5.200.000; cash **4.224.002**; equity **47.041.659** (inbreng **5.924.200**; reserves **40.243.451**; kapitaalsubsidies **874.009** DROP vs 2.930.136); voorzieningen **3.994.400**; ops rev **56.727.155**; omzet **55.563.611**; andere **1.019.170**; pers **19.848.202**; 237 koppen / VTE **232,77**; diensten **20.927.494**; goods **6.242.211**; afschr **6.082.679**; expl **+1.016.371**; fin opbr **129.828**; fin kosten **556.846**; PnL **+565.857** DROP vs 4.157.073. City incineration income **3.105.551** (Brugge 1.487.736 / Blankenberge 384.867 / Oostkamp 269.020 / Zedelgem 268.825 / De Haan 209.309 / Beernem 175.699 / Jabbeke 175.733 / Damme 103.317 / Zuienkerke 31.045) + derden/vennoten C **14.839.827**. Commissaris oordeel zonder voorbehoud.
- CSVs: sources+4/entities+1/budgets+34/commitments+1/leaderboard+1 + FOI ready `gap_ivbo_omzet_55_56m_assets_79_79m_pers_19_85m_l5` (not sent); rq_1352=done; spawn rq_1353; ticks=1352.
- Coverage: residual dual L5 (IVBO leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1353 residual dual L5 VL JR2025 hole_fill (prefer Westtoer APB BBC 2025 PDF already downloaded this tick if still unmined; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; Limburg.net 2025 JR 17p InDesign only if WVV/BBC euros; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; EcoWerf only if a statutory WVV/BBC PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; MIROM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1352 write done")


if __name__ == "__main__":
    main()

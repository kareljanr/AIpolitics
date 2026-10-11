# -*- coding: utf-8 -*-
"""Tick 1342 — leftover IGS IDM Durme-Moervaart JR2025 WVV euros.
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

TICK = "1342"
UTC = "2026-08-18T04:05:00Z"
ENT = "igs_idm"
HIER = "Vlaanderen>OostVlaanderen>IGS>IDM>DurmeMoervaart"
GAP = "gap_idm_otherops_11_98m_pers_8_36m_strecv_jump_l5"
SRC = "src_idm_jr2025_pdf"
SRC2 = "src_idm_site"
SRC3 = "src_kbo_idm_0214014167"
SRC4 = "src_idm_foi_contact"
SRC_URL = "https://www.idm.be/sites/default/files/2026-06/IDM-Jaarrekening-BJ-2025-definitief.pdf"
SRC2_URL = "https://www.idm.be/idm-jaarverslag-2025"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0214014167"
SRC4_URL = "https://www.idm.be/contact"
FOI_EMAIL = "info@idm.be"
FOI_POSTAL = "Zelebaan 42 9160 Lokeren"
DRAFT = "docs/doge/foi/drafts/gap_idm_otherops_11_98m_pers_8_36m_strecv_jump_l5.md"
COMM = "comm_idm_jr2025_otherops"
LB = "lb_idm_otherops_11_98m_pers_8_36m"


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
                "title": "IDM jaarrekening boekjaar 2025 (official WVV VOL-kap PDF; AV 19.06.2026)",
                "url": SRC_URL,
                "publisher": "IDM Intercommunale Durme-Moervaart",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1342; official PDF 1.03MB 39p; AV 19.06.2026; "
                    "WVV VOL-kap IDM 0214.014.167; leftover IGS of mined Lokeren/Lochristi/Zele/Zelzate/Moerbeke/Wachtebeke; not BBC J1-J5"
                ),
            },
            {
                "source_id": SRC2,
                "title": "IDM official jaarverslag 2025 page (Jaarrekening BJ 2025 listed)",
                "url": SRC2_URL,
                "publisher": "IDM",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1342; HTTP 200 lists IDM-Jaarrekening-BJ-2025-definitief.pdf 1.03MB + RvB verslag 2025; "
                    "leftover IGS of mined East-Flanders Durme-Moervaart cities"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO IDM Durme-Moervaart 0214.014.167",
                "url": SRC3_URL,
                "publisher": "KBO Besloten vennootschap Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1342; KBO 0214.014.167 Actief / normale toestand since 22.12.1973; "
                    "statutaire naam Intercommunale voor Huisvuilverwerking en Milieuzorg DURME - MOERVAART since 24.11.1993; "
                    "afkorting I.D.M.; Opdrachthoudende vereniging (Vlaams Gewest) since 19.12.2018; "
                    "zetel Zelebaan 42 9160 Lokeren since 01.01.2025; 6 VE; RSZ since 01.01.2022; "
                    "btw since 01.10.2001; aanbestedende overheid since 22.12.1973; "
                    "jaarvergadering mei; boekjaar 31 december; e-mail danny.verbrugge@idm.be; "
                    "tel 09 348 43 97; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "IDM contact / hoofdzetel (FOI channel)",
                "url": SRC4_URL,
                "publisher": "IDM",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1342; FOI info@idm.be from official contact page; "
                    "Zelebaan 42 9160 Lokeren; T 09 348 43 97; ophaaldienst@idm.be Moortelstraat 16"
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
                "name_nl": "IDM Intercommunale voor Huisvuilverwerking en Milieuzorg Durme-Moervaart (opdrachthoudende vereniging / leftover IGS)",
                "name_fr": "IDM intercommunale Durme-Moervaart (association missionnee / IGS residuel)",
                "name_en": "IDM Durme-Moervaart waste intermunicipal (leftover IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.idm.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1342 leftover IGS residual of mined Lokeren AGB + Lochristi Zorgband + Zele/Zelzate/Moerbeke/Wachtebeke; "
                    "KBO 0214.014.167 Actief since 22.12.1973; official JR2025 WVV PDF downloads; "
                    "assets 9.527m other-ops 11.979m pers 8.360m PnL +428.893 VTE 112.8; "
                    "FOI ready other-ops/dual-city/pension/NBB"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_idm_assets_2025", ENT, "2025", "9527457", "2025 assets 9527457.23 was 9608727.08; tick1342; primary WVV in official PDF"),
        ("bud_idm_fixed_2025", ENT, "2025", "5579480", "2025 vaste activa 5579479.82 was 5881544.86; tick1342; primary WVV"),
        ("bud_idm_mva_2025", ENT, "2025", "5535203", "2025 MVA 5535202.86 (gebouwen 2368978.59 + rollend 2881438.46 + lease 36694.61 + CIP 69864.87); tick1342; primary WVV"),
        ("bud_idm_fva_2025", ENT, "2025", "44277", "2025 FVA aandelen 44276.96 unchanged; tick1342; primary WVV"),
        ("bud_idm_current_2025", ENT, "2025", "3947977", "2025 vlottende activa 3947977.41 was 3727182.22; tick1342; primary WVV"),
        ("bud_idm_lt_recv_2025", ENT, "2025", "26240", "2025 LT overige vorderingen 26239.68 was 34986.24; tick1342; primary WVV"),
        ("bud_idm_st_recv_2025", ENT, "2025", "1614322", "2025 ST recv 1614322.49 (trade 1195985.40 + other 418337.09 JUMP vs 106986.07); tick1342; primary WVV"),
        ("bud_idm_cash_2025", ENT, "2025", "2307415", "2025 cash 2307415.24 DROP vs 2489298.18; tick1342; primary WVV"),
        ("bud_idm_equity_2025", ENT, "2025", "6328791", "2025 equity 6328791.08 was 5899897.73; tick1342; primary WVV"),
        ("bud_idm_capital_2025", ENT, "2025", "538350", "2025 geplaatst kapitaal 538350.00; tick1342; primary WVV"),
        ("bud_idm_reserves_2025", ENT, "2025", "3815352", "2025 onbeschikbare reserves 3815351.64; tick1342; primary WVV"),
        ("bud_idm_retained_2025", ENT, "2025", "1975089", "2025 overgedragen winst 1975089.44 was 1546196.09; tick1342; primary WVV"),
        ("bud_idm_prov_2025", ENT, "2025", "101005", "2025 voorzieningen grote herstellingen 101004.67 JUMP vs 13712.64; tick1342; primary WVV"),
        ("bud_idm_debt_2025", ENT, "2025", "3097661", "2025 schulden 3097661.48 was 3695116.71; tick1342; primary WVV"),
        ("bud_idm_lt_fin_2025", ENT, "2025", "468576", "2025 LT financial 468576.17 (banken 461437.04 + lease 7139.13); tick1342; primary WVV"),
        ("bud_idm_st_debt_2025", ENT, "2025", "2628096", "2025 ST schulden 2628096.25 was 2837069.75; tick1342; primary WVV"),
        ("bud_idm_st_ltcurr_2025", ENT, "2025", "386779", "2025 LT-within-year 386778.88 was 383718.55; tick1342; primary WVV"),
        ("bud_idm_trade_pay_2025", ENT, "2025", "1025336", "2025 leveranciers 1025336.27 was 849482.12; tick1342; primary WVV"),
        ("bud_idm_taxsoc_2025", ENT, "2025", "1146400", "2025 tax/soc 1146399.80 (tax 306284.14 + wages 840115.66); tick1342; primary WVV"),
        ("bud_idm_ops_rev_2025", ENT, "2025", "16937420", "2025 bedrijfsopbrengsten 16937419.64 was 16618000.04; tick1342; primary WVV"),
        ("bud_idm_turnover_2025", ENT, "2025", "4922177", "2025 omzet 4922177.47 was 5021428.99; tick1342; primary WVV"),
        ("bud_idm_otherops_2025", ENT, "2025", "11978748", "2025 andere bedrijfsopbrengsten 11978748.13 was 11580654.06; tick1342; primary WVV code 74"),
        ("bud_idm_ops_cost_2025", ENT, "2025", "16487364", "2025 bedrijfskosten 16487364.17 was 16523171.28; tick1342; primary WVV"),
        ("bud_idm_goods_2025", ENT, "2025", "4432837", "2025 handelsgoederen 4432836.92 was 4176602.35; tick1342; primary WVV"),
        ("bud_idm_services_2025", ENT, "2025", "2348583", "2025 diensten 2348582.65 was 2028952.47; tick1342; primary WVV"),
        ("bud_idm_pers_2025", ENT, "2025", "8360345", "2025 bezoldigingen 8360345.02 was 9147190.41; tick1342; primary WVV; VTE 112.8 / 118 koppen"),
        ("bud_idm_ops_2025", ENT, "2025", "450055", "2025 bedrijfswinst 450055.47 was 94828.76; tick1342; primary WVV 9901"),
        ("bud_idm_fin_cost_2025", ENT, "2025", "36578", "2025 fin kosten 36577.61 (schulden 26722.79); tick1342; primary WVV"),
        ("bud_idm_pnl_2025", ENT, "2025", "428893", "2025 PnL +428893.35 was +87960.97; tick1342; primary WVV 9904"),
        ("bud_idm_contrib2026_2025", ENT, "2026", "11479071", "2026 werkingsbijdrage 11479071 = 2025 +414810 (implied 2025 11064261); tick1342; primary WVV narrative waarderingsregels"),
        ("bud_idm_pensionfund_2025", ENT, "2025", "2598719", "2025 off-balance collectief pensioenfonds 2598718.59 was 2655544.88; tick1342; primary WVV narrative"),
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
                "basis": "executed" if year == "2025" else "budgeted",
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
                "title": "IDM Durme-Moervaart JR2025 leftover IGS dual (other ops 11.98m / pers 8.36m / ST recv jump)",
                "entity_id": ENT,
                "beneficiary": "IDM / vennoten Lochristi Lokeren Moerbeke Wachtebeke Zele Zelzate / IVM",
                "legal_basis": "Decreet lokaal bestuur IGS; opdrachthoudende vereniging; Bestuursdecreet openbaarheid; WVV neerlegging",
                "decision_date": "2026-06-19",
                "start_year": "1973",
                "end_year": "2025",
                "total_envelope_eur": "16937420",
                "cash_by_year": "",
                "remaining_eur": "6328791",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL Durme-Moervaart — werkingsbijdrage / dual city lines; other-ops roster/NBB missing",
                "cut_option": "Publish per-vennoot 11.98m other-ops + dual city lines + off-balance pension 2.60m; do not recreate parallel waste-IGS shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1342; assets 9527457 otherops 11978748 pers 8360345 PnL +428893 VTE 112.8; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "IDM Durme-Moervaart JR2025 leftover IGS: other ops 11.98m / pers 8.36m / ST recv jump",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "8360345",
                "total_cost_eur": "16937420",
                "tco_notes": "Leftover dual IGS of mined Lokeren/Lochristi/Zele/Zelzate/Moerbeke/Wachtebeke: ops rev 16.94m / other ops 11.98m / pers 8.36m VTE 112.8 / assets 9.53m / off-balance pension 2.60m / PnL +0.43m; do not treat 16.94m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "IDM / 6 Durme-Moervaart gemeenten / IVM / waste-IGS",
                "stated_goal": "Local leftover IGS map VL Durme-Moervaart — JR2025 PDF live; dual other-ops/pension/NBB FOI",
                "measured_outcome": "Official PDF 2026-08-17: assets 9.53m / other ops 11.98m / pers 8.36m / PnL +428.9k / VTE 112.8",
                "absurdity_score": "6.4",
                "cost_score": "6.6",
                "difficulty": "3.2",
                "priority_index": "6.3",
                "cut_proposal": "Publish per-vennoot 11.98m other-ops + dual city lines + off-balance pension 2.60m; do not recreate parallel waste-IGS shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1342; leftover IGS of mined Durme-Moervaart cities; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "Per-vennoot 2025-2026 dual lines for andere bedrijfsopbrengsten 11978748.13 "
                    "(code 74; no 6.10 split) vs narrative werkingsbijdrage 2025 implied 11064261 "
                    "(2026 11479071 = +414810) + omzet 4922177.47 + counterparties/age of ST recv "
                    "1614322.49 (trade 1195985.40 + other 418337.09 JUMP vs 106986.07) + off-balance "
                    "collectief pensioenfonds 2598718.59 (was 2655544.88; stort 220000; RSZ 315667.33) "
                    "vs voorzieningen 101004.67 JUMP vs 13712.64 + RSZ employer DROP 2225213.64 to "
                    "1174756.09 + FVA aandelen 44276.96 + IVM 10 shares + NBB filing proof "
                    "(ref 2026-00206794 / 25.06.2026) + commissarisverslag KPMG Wim Heyndrickx / AV 19.06.2026"
                ),
                "why_it_matters": (
                    "Leftover IGS shell of mined Lokeren AGB + Lochristi Zorgband + Zele/Zelzate/"
                    "Moerbeke/Wachtebeke: 16.94m ops / 11.98m other-ops vs 8.36m personnel and "
                    "2.60m off-balance pension is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "IDM Intercommunale Durme-Moervaart / vennoten Lochristi Lokeren Moerbeke Wachtebeke Zele Zelzate",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM,
                "linked_leaderboard_id": LB,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "tick1342 leftover IGS of mined Durme-Moervaart cities after honest hunt; "
                    "live JR2025 official WVV PDF now downloads (1.03MB 39p VOL-kap). "
                    "Dommelhof leftover Limburg EVA KBO 0777.495.085 no JR2025 PDF — not taken. "
                    "De Schorre 403 / Ter Nethe DNS / Welzijnskoepel glossy / leftover cities no JR2025. "
                    "Veneco glossy 25MB not mined as BBC. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1342",
        "title": "IDM Durme-Moervaart JR2025 leftover IGS dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: IDM leftover IGS of mined Lokeren/Lochristi/Zele/Zelzate/Moerbeke/Wachtebeke after honest hunt; "
            "KBO 0214.014.167 Actief; live JR2025 official WVV PDF (1.03MB 39p VOL-kap AV 19.06.2026); "
            "sourced euros assets 9.527m / other-ops 11.979m / pers 8.360m / PnL +428.893 / VTE 112.8; "
            "FOI ready other-ops/dual-city/pension/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T03:15:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1342 IDM leftover IGS residual; KBO 0214.014.167; live JR2025 WVV PDF; "
            "sourced euros; FOI ready not sent; next rq_1343 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1343",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1342 done including IDM Durme-Moervaart 1342 leftover IGS live WVV / "
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
            "Interleuven 2025 jaarverslag pending AV — take only if a 2025 balans PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
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
        "notes": "spawned tick1342 after IDM leftover IGS live WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1342", rq_new, rq_spawn)
    print("research_queue 1342", found, "spawned_1343", spawned)

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
                "last_unit_id": "rq_1342",
                "ticks_completed": "1342",
                "paused": "no",
                "notes": (
                    "tick1342 IDM leftover IGS residual; KBO 0214.014.167; "
                    "live JR2025 WVV PDF; sourced euros assets 9.527m other-ops 11.979m pers 8.360m PnL +428.893; "
                    "FOI ready; next rq_1343 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = f"""
### Tick 1342 - 2026-08-18 - rq_1342 IDM Durme-Moervaart dual residual leftover IGS
- Unit: IDM Intercommunale voor Huisvuilverwerking en Milieuzorg Durme-Moervaart (opdrachthoudende vereniging / leftover IGS) of already-mined Lokeren (AGB Lokeren) + Lochristi (Zorgband 1338) + Zele / Zelzate / Moerbeke / Wachtebeke after residual dual hunt (KBO **0214.014.167**; official idm.be + live jaarrekening BJ 2025 PDF 1.03MB / 39p; AV **19.06.2026**; WVV VOL-kap). Prefer live PDF over another unpublished FOI. Distinct from already-mined IGEAN 1341 / AGB Lokeren / Zorgband 1338 / EVA LSM 1340. KBO Actief / normale toestand since **22.12.1973**; statutaire naam Intercommunale voor Huisvuilverwerking en Milieuzorg DURME - MOERVAART since 24.11.1993; afkorting I.D.M.; Opdrachthoudende vereniging (Vlaams Gewest) since 19.12.2018; zetel Zelebaan 42 9160 Lokeren since 01.01.2025; **6 VE**; RSZ-werkgever since 01.01.2022; btw since 01.10.2001; aanbestedende overheid since 22.12.1973; jaarvergadering mei; boekjaar 31 december; voorzitter Piet Penneman; commissaris KPMG / Wim Heyndrickx since 25.06.2025; e-mail danny.verbrugge@idm.be / tel 09 348 43 97 on KBO; NACE 38.330 / 38.110. Hunt leftover AGB/zorg/EVA first: Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 Actief — homepage 200 / no JR2025 PDF (statutes-only last tick) so not taken; Ter Nethe DNS fail; Welzijnskoepel West-Brabant homepage no BBC; AGB Lebbeke ontbonden; AGB Bornem `/agb` 404 / still JR2024-only; AGB De Kluize unpublished. Leftover cities Londerzeel 404 / Wortegem-Petegem official JR2020–2024 only / Zwalm `/jaarrekening` 404 / Holsbeek 404 / Maarkedal TLS / Linkebeek 404 / Kapellen city GE 404 / Drogenbos 404 / Boutersem archive-only / Maaseik city GE 404 / Bierbeek 404 still no fetchable JR2025. APB POA/TPA/De Schorre/Warande/De Nekker: provincieantwerpen.be 403 / venue homepages 200 no JR2025 BBC PDF — not taken. Veneco glossy 25MB InDesign jaarverslag 2025 — not mined as BBC. Interleuven 2025 jaarverslag "klaar" but AV 17.06.2026 pending / only 2024 balans PDF. IOK still 2024; ISVAG no 2025 JR PDF; Haviland 2024; IVAREM activiteitenverslag 2025 glossy. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331. Not every-10 (next 1350).
- EUR strong (primary WVV VOL-kap in official PDF): assets **9.527.457** (was 9.608.727); fixed **5.579.480**; MVA **5.535.203** (gebouwen **2.368.979** + rollend **2.881.438** + lease **36.695** + CIP **69.865**); FVA **44.277** aandelen unchanged; current **3.947.977**; LT recv **26.240**; ST recv **1.614.322** (trade **1.195.985** + other **418.337** JUMP vs 106.986); cash **2.307.415** DROP vs 2.489.298; equity **6.328.791**; kapitaal **538.350**; reserves **3.815.352**; overgedragen **1.975.089**; voorzieningen **101.005** JUMP vs 13.713; schulden **3.097.661**; LT fin **468.576** (banken **461.437** + lease **7.139**); ST **2.628.096** (LT-within-year **386.779** + trade **1.025.336** + tax/soc **1.146.400**); ops rev **16.937.420**; omzet **4.922.177**; andere bedrijfsopbrengsten **11.978.748**; pers **8.360.345**; VTE **112,8** / 118 koppen; expl **+450.055**; fin kosten **36.578**; PnL **+428.893**. Narrative same PDF: 2026 werkingsbijdrage **11.479.071** = 2025 + **414.810** (implied 2025 **11.064.261**); off-balance collectief pensioenfonds **2.598.719** (was 2.655.545; stort 220.000; RSZ 315.667).
- CSVs: sources+4/entities+1/budgets+31/commitments+1/leaderboard+1 + FOI ready `{GAP}` (not sent); rq_1342=done; spawn rq_1343; ticks=1342.
- Coverage: residual dual L5 (IDM leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1343 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1342 write done")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Tick 1348 — leftover IGS Creat Services dv JR2025 official WVV euros.
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

TICK = "1348"
UTC = "2026-08-18T21:50:00Z"
ENT = "igs_creat"
HIER = "Vlaanderen>OostVlaanderen>IGS>CreatServices>Aankoopcentrale"
GAP = "gap_creat_omzet_89_38m_strecv_16_39m_vatunit_3_76m_l5"
SRC = "src_creat_jr2025_pdf"
SRC2 = "src_creat_site"
SRC3 = "src_kbo_creat_0692624441"
SRC4 = "src_creat_foi_contact"
SRC_URL = "https://www.farys.be/nl/file-download/download/public/6080276"
SRC2_URL = "https://www.farys.be/nl/wie-farys"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0692624441"
SRC4_URL = "https://creat.be"
FOI_EMAIL = "creat@creat.be"
FOI_POSTAL = "Stropstraat 1 9000 Gent"
DRAFT = "docs/doge/foi/drafts/gap_creat_omzet_89_38m_strecv_16_39m_vatunit_3_76m_l5.md"
COMM = "comm_creat_jr2025_omzet"
LB = "lb_creat_omzet_89_38m_strecv_16_39m"


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
                "title": "Creat Services dv jaarverslag boekjaar 2025 (official WVV VOL; InDesign 05.06.2026; AV 16.06.2026)",
                "url": SRC_URL,
                "publisher": "Creat Services dv dienstverlenende vereniging",
                "accessed_date": "2026-08-18",
                "source_class": "budget",
                "notes": (
                    "tick1348; official PDF 1.64MB 73p InDesign 05.06.2026; leftover IGS aankoopcentrale of mined Farys ov + 606 deelnemers; "
                    "embedded WVV VOL balans/resultatenrekening; commissaris Figurad 16751601 / 369478"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Farys / Creat official identity page (Creat Services dv KBO 0692.624.441)",
                "url": SRC2_URL,
                "publisher": "Farys ov / Creat",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1348; leftover IGS of mined Farys ov tick576; Creat Services dv ex-TMVS dienstverlenende vereniging; "
                    "Creat CV 0554.887.312 sister"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Creat Services 0692.624.441",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1348; KBO 0692.624.441 Actief / normale toestand since 22.12.2017; "
                    "statutaire naam Creat Services since 12.12.2023; Dienstverlenende vereniging (Vlaams Gewest) since 22.12.2017; "
                    "zetel Botermarkt 1 9000 Gent since 22.12.2017; 0 VE; aanbestedende overheid since 18.01.2003; "
                    "btw since 01.03.2018; jaarvergadering juni; boekjaar 31 december; NACE 82.100 / 46.190"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Creat Services FOI channel / official PDF contact",
                "url": SRC4_URL,
                "publisher": "Creat Services dv",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1348; FOI creat@creat.be from official PDF; Stropstraat 1 9000 Gent; "
                    "T 09 240 05 72; voorzitter Joris Vandenbroucke; AD Marleen Porto-Carrero"
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
                "name_nl": "Creat Services dv (leftover IGS aankoopcentrale; ex-TMVS)",
                "name_fr": "Creat Services dv (association de services / centrale d'achat / IGS residuel)",
                "name_en": "Creat Services dv purchasing intermunicipal (leftover IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://creat.be",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1348 leftover IGS residual of mined Farys ov tick576 + 606 deelnemers; "
                    "KBO 0692.624.441 Actief since 22.12.2017; official JR2025 WVV PDF downloads; "
                    "sourced euros omzet 89.383m / assets 16.752m / ST recv 16.391m / VAT-unit 3.758m / PnL 0.369m; "
                    "FOI ready per-deelnemer/VAT-unit/uncalled/NBB"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_creat_assets_2025", ENT, "2025", "16751601", "2025 assets 16751600.57 commissaris 16751601; tick1348; primary official WVV"),
        ("bud_creat_assets_2024", ENT, "2024", "13784276", "2024 assets 13784275.76 comparative; tick1348; primary official WVV"),
        ("bud_creat_current_2025", ENT, "2025", "16548303", "2025 vlottende activa 16548302.57; tick1348; primary official WVV"),
        ("bud_creat_strecv_2025", ENT, "2025", "16420054", "2025 ST recv 16420054.43 JUMP vs 13463137.04; tick1348; primary official WVV"),
        ("bud_creat_trade_recv_2025", ENT, "2025", "16391304", "2025 handelsvorderingen 16391304.43 JUMP vs 13463137.04; tick1348; primary official WVV"),
        ("bud_creat_cash_2025", ENT, "2025", "128248", "2025 liquide middelen 128248.14 was 117840.72; tick1348; primary official WVV"),
        ("bud_creat_fva_2025", ENT, "2025", "203298", "2025 FVA 203298 all Creat CV deelneming unchanged; tick1348; primary official WVV"),
        ("bud_creat_equity_2025", ENT, "2025", "2567755", "2025 equity 2567755.21 thin 15pct vs 16752k; tick1348; primary official WVV"),
        ("bud_creat_inbreng_2025", ENT, "2025", "884500", "2025 inbreng 884500 was 707000; Farys 177750 + others 706750; tick1348; primary official WVV"),
        ("bud_creat_inbreng_farys_2025", ENT, "2025", "177750", "2025 Farys ov inbreng 177750 of 884500; tick1348; primary official WVV commentaar"),
        ("bud_creat_uncalled_2025", ENT, "2025", "2473500", "2025 niet-opgevraagde inbreng 2473500 (606 deelnemers toel 6.19); tick1348; primary official WVV"),
        ("bud_creat_called_unpaid_2025", ENT, "2025", "24250", "2025 opgevraagd-niet-gestort 24250; tick1348; primary official WVV toel 6.19"),
        ("bud_creat_reserves_2025", ENT, "2025", "1683255", "2025 beschikbare reserves 1683255.21 was 1313777.57; tick1348; primary official WVV"),
        ("bud_creat_debt_2025", ENT, "2025", "14183845", "2025 schulden 14183845.36 all ST was 11763498.19; tick1348; primary official WVV"),
        ("bud_creat_trade_pay_2025", ENT, "2025", "10371185", "2025 leveranciers 10371185.15 was 8534128.33; tick1348; primary official WVV"),
        ("bud_creat_other_debt_2025", ENT, "2025", "3799512", "2025 overige schulden 3799511.93 was 3187197.38; tick1348; primary official WVV"),
        ("bud_creat_vatunit_2025", ENT, "2025", "3757517", "2025 schuld btw-eenheid BE 0630.730.325 3757516.73; tick1348; primary official WVV commentaar"),
        ("bud_creat_omzet_2025", ENT, "2025", "89383335", "2025 omzet 89383335.41 JUMP vs 70522995.83; tick1348; primary official WVV"),
        ("bud_creat_omzet_2024", ENT, "2024", "70522996", "2024 omzet 70522995.83 comparative; tick1348; primary official WVV"),
        ("bud_creat_ops_cost_2025", ENT, "2025", "88835954", "2025 bedrijfskosten 88835954.23 was 69978947.70; tick1348; primary official WVV"),
        ("bud_creat_goods_2025", ENT, "2025", "85516809", "2025 handelsgoederen 85516808.92 was 67318451.75; tick1348; primary official WVV"),
        ("bud_creat_diensten_2025", ENT, "2025", "3184343", "2025 diensten 3184342.60 was 2559400.23; tick1348; primary official WVV"),
        ("bud_creat_recv_impair_2025", ENT, "2025", "134803", "2025 waardeverm ST recv 134802.71 was 101095.72; tick1348; primary official WVV"),
        ("bud_creat_expl_2025", ENT, "2025", "547381", "2025 bedrijfswinst 547381.18 was 544048.13; tick1348; primary official WVV"),
        ("bud_creat_tax_2025", ENT, "2025", "175502", "2025 belasting 175502.35 was 166753.34; tick1348; primary official WVV"),
        ("bud_creat_pnl_2025", ENT, "2025", "369478", "2025 PnL 369477.64 commissaris 369478; tick1348; primary official WVV"),
        ("bud_creat_pnl_before_tax_2025", ENT, "2025", "544980", "2025 winst voor belasting 544979.99; tick1348; primary official WVV"),
        ("bud_creat_fin_cost_2025", ENT, "2025", "2410", "2025 financiele kosten 2410.09; tick1348; primary official WVV"),
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
                "title": "Creat Services dv JR2025 leftover IGS dual (omzet 89.38m / ST recv 16.39m / VAT-unit 3.76m)",
                "entity_id": ENT,
                "beneficiary": "Creat Services dv / 606 deelnemers + Farys ov aankoopcentrale CREAT",
                "legal_basis": "Decreet lokaal bestuur IGS; dienstverlenende vereniging; Bestuursdecreet openbaarheid; WVV neerlegging",
                "decision_date": "2026-06-16",
                "start_year": "2017",
                "end_year": "2025",
                "total_envelope_eur": "89383335",
                "cash_by_year": "",
                "remaining_eur": "3757517",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL aankoopcentrale — per-deelnemer 89.38m omzet / VAT-unit 3.76m / uncalled 2.47m",
                "cut_option": "Publish per-deelnemer 89.38m afroep dual city lines + VAT-unit 3.76m + uncalled 2.47m + NBB; do not recreate parallel aankoop-IGS shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1348; omzet 89383335 assets 16751601 ST recv 16391304 VAT-unit 3757517 PnL 369478; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Creat Services dv JR2025 leftover IGS: omzet 89.38m / ST recv 16.39m / VAT-unit 3.76m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "89383335",
                "total_cost_eur": "89383335",
                "tco_notes": "Leftover dual IGS aankoopcentrale of mined Farys ov + 606 deelnemers: omzet 89.38m pass-through / ST recv 16.39m / VAT-unit debt 3.76m / uncalled 2.47m / thin equity 2.57m vs 16.75m assets; official WVV live; do not treat 89.38m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Creat Services dv / 606 deelnemers / Farys ov",
                "stated_goal": "Local leftover IGS map VL aankoopcentrale — JR2025 WVV live; dual omzet/VAT-unit/NBB FOI",
                "measured_outcome": "Official WVV 2026-08-18: omzet 89.38m / assets 16.75m / ST recv 16.39m / VAT-unit 3.76m / PnL 0.37m; pers 0",
                "absurdity_score": "6.2",
                "cost_score": "7.1",
                "difficulty": "3.0",
                "priority_index": "6.6",
                "cut_proposal": "Publish per-deelnemer 89.38m afroep dual city lines + VAT-unit 3.76m + uncalled 2.47m + NBB; do not recreate parallel aankoop-IGS shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1348; leftover IGS of mined Farys ov + 606 deelnemers; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "Per-deelnemer 2025-2026 dual lines for omzet 89383335.41 (JUMP vs 70522995.83; pass-through aankoopcentrale; "
                    "no 6.10 split) + counterparties/age of trade recv 16391304.43 JUMP vs 13463137.04 + composition of other debt "
                    "3799511.93 of which VAT-unit BE 0630.730.325 3757516.73 + Farys ov recharge (pers 0 / ops via Farys) + "
                    "uncalled inbreng 2473500 / called-not-paid 24250 (toel 6.19) + Creat CV 203298 intra-group + commissaris "
                    "ereloon Figurad/Meganck + AV 16.06.2026 minutes + NBB filing"
                ),
                "why_it_matters": (
                    "Leftover IGS shell of mined Farys ov tick576 + 606 deelnemers (cities/OCMW/AGB/zorg/IGS including already-mined "
                    "Het Dak/OPcura/Sleutelzorg/Weldenderend/Zorgband/WVI): 89.38m omzet pass-through vs 16.39m trade recv / "
                    "3.76m VAT-unit debt / 2.47m uncalled capital is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Creat Services dv / 606 deelnemers / Farys ov",
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
                    "tick1348 leftover IGS of mined Farys ov + 606 deelnemers after honest hunt; "
                    "live JR2025 official WVV PDF now downloads (1.64MB 73p InDesign 05.06.2026). "
                    "EcoWerf 2025 glossy / 2024 statutory still unpublished. Interleuven still 2024 balans. "
                    "IOK/IMOG/Haviland/IVBO/Limburg.net still 2024. Veneco glossy-only. MIROM 403. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1348",
        "title": "Creat Services dv JR2025 leftover IGS dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Creat Services dv leftover IGS aankoopcentrale of mined Farys ov + 606 deelnemers after honest hunt; "
            "KBO 0692.624.441 Actief; live JR2025 official WVV PDF (1.64MB 73p InDesign 05.06.2026 AV 16.06.2026); "
            "sourced euros omzet 89.383m / assets 16.752m / ST recv 16.391m / VAT-unit 3.758m / PnL 0.369m; "
            "FOI ready per-deelnemer/VAT-unit/uncalled/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T21:15:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1348 Creat leftover IGS residual; KBO 0692.624.441; live JR2025 WVV PDF; "
            "sourced euros; FOI ready not sent; next rq_1349 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1349",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1348 done including Creat Services dv 1348 leftover IGS live WVV / "
            "IVIO Izegem-Ommeland 1347 leftover IGS live JR operational / "
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
            "Veneco glossy jaarverslag 2025 websingle — take only if a WVV/BBC PDF now downloads; "
            "EcoWerf 2025 jaarverslag listed ~16MB glossy / 2024 statutory still unpublished — take only if a WVV/BBC PDF now downloads; "
            "Leiedal 2025 InDesign 22MB 118p downloaded tick1347 — glossy-only no WVV — take only if a WVV/BBC PDF now downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland / IVBO / Limburg.net still 2024 — take only if a 2025 JR PDF now downloads; "
            "IVOO no public 2025 JR PDF — take only if a 2025 JR PDF now downloads; "
            "MIROM 403 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
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
        "notes": "spawned tick1348 after Creat leftover IGS live WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1348", rq_new, rq_spawn)
    print("research_queue 1348", found, "spawned_1349", spawned)

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
                "last_unit_id": "rq_1348",
                "ticks_completed": "1348",
                "paused": "no",
                "notes": (
                    "tick1348 Creat leftover IGS residual; KBO 0692.624.441; "
                    "live JR2025 WVV PDF; sourced euros omzet 89.383m assets 16.752m ST recv 16.391m VAT-unit 3.758m PnL 0.369m; "
                    "FOI ready per-deelnemer/VAT-unit; next rq_1349 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log_entry = """
### Tick 1348 - 2026-08-18 - rq_1348 Creat Services dv dual residual leftover IGS
- Unit: Creat Services dv (dienstverlenende vereniging / leftover IGS aankoopcentrale; ex-TMVS) of already-mined Farys ov (tick576) + 606 deelnemers (steden / gemeenten / OCMW / AGB / zorg / IGS including already-mined Het Dak / OPcura / Sleutelzorg / Weldenderend / Zorgband / WVI) after residual dual hunt (KBO **0692.624.441**; official farys.be + live jaarverslag 2025 PDF 1.64MB / 73p; InDesign **05.06.2026**; AV **16.06.2026**; embedded WVV VOL). Prefer live PDF over another unpublished FOI. Distinct from already-mined Farys ov 576 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340. KBO Actief / normale toestand since **22.12.2017**; statutaire naam Creat Services since 12.12.2023 (ex-TMVS); Dienstverlenende vereniging (Vlaams Gewest) since 22.12.2017; zetel Botermarkt 1 9000 Gent since 22.12.2017; admin Stropstraat 1 9000 Gent; **0 VE**; aanbestedende overheid since 18.01.2003; btw since 01.03.2018 (btw-eenheid BE 0630.730.325 with Farys ov / Creat CV / Farys Solar); jaarvergadering juni; boekjaar 31 december; voorzitter Joris Vandenbroucke since 25.03.2025; ondervoorzitter Michèle Esquenet; AD Marleen Porto-Carrero (Farys); secretaris Pascale Aerts; commissaris Figurad / Bart Meganck (AV 17.06.2025 tot boekjaar 2027); e-mail creat@creat.be on official PDF; tel 09 240 05 72; NACE 82.100 / 46.190. 606 deelnemers / 4.721 deelnames / 72 productrubrieken. Geen eigen personeel — ops via Farys ov recharge. Hunt leftover AGB/zorg/EVA first: EcoWerf 2025 glossy 16MB / 2024 statutory still "wordt weldra gepubliceerd" — not taken; Interleuven publications still only jaarrekening 2024 PDF; IOK/IMOG/Haviland/IVBO/Limburg.net still 2024; IVOO no public 2025 JR PDF; MIWA still 2024; MIROM 403; IVAGO activiteitenverslag glossy; ISVAG still 2023; IVAREM still 2024; SOLVA no 2025 JR; IGEMO activiteitenverslag only; Veneco 2025 websingle glossy — no WVV — not taken; Leiedal 2025 InDesign glossy-only; Pidpa/DWG/Farys ov already mined. Dommelhof leftover Limburg EVA KBO 0777.495.085 not taken once live Creat WVV downloaded. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek not taken once live Creat PDF downloaded. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331. Not every-10 (next 1350).
- EUR strong (primary official WVV VOL + commissaris Figurad assets 16.751.601 / PnL 369.478): assets **16.751.601** (was 13.784.276); fixed **203.298** all FVA Creat CV; current **16.548.303**; ST recv **16.420.054** JUMP vs 13.463.137 (trade **16.391.304** + other **28.750**); cash **128.248**; equity **2.567.755** thin 15% (inbreng **884.500** of which Farys **177.750** + others **706.750**; uncalled **2.473.500**; called-not-paid **24.250**; reserves **1.683.255**); schulden **14.183.845** all ST (trade **10.371.185** + tax/soc **13.148** + other **3.799.512** of which VAT-unit **3.757.517**); omzet **89.383.335** JUMP vs 70.522.996; ops cost **88.835.954** (goods **85.516.809** + diensten **3.184.343** + recv impair **134.803**); expl **+547.381**; fin opbr **9**; fin kosten **2.410**; tax **175.502**; PnL **+369.478**. Pers **0**. Commissaris oordeel zonder voorbehoud 02.04.2026.
- CSVs: sources+4/entities+1/budgets+28/commitments+1/leaderboard+1 + FOI ready `gap_creat_omzet_89_38m_strecv_16_39m_vatunit_3_76m_l5` (not sent); rq_1348=done; spawn rq_1349; ticks=1348.
- Coverage: residual dual L5 (Creat leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1349 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland/IVBO/Limburg.net only if a 2025 JR PDF now downloads; EcoWerf only if a statutory WVV/BBC PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; MIROM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 unless a fetchable JR appears).
"""
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1348 write done")


if __name__ == "__main__":
    main()

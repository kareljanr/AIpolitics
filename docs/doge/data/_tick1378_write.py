# -*- coding: utf-8 -*-
"""Tick 1378 — leftover De Nekker VZW JR2025 official NBB WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10 (next every-10 is 1380).
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1378"
UTC = "2026-08-19T05:20:00Z"
ENT = "eva_nekk"
HIER = "Vlaanderen>Antwerpen>Provincie>EVA>DeNekker"
GAP = "gap_nekk_omzet_empty_ops_3_67m_equity_neg_l5"
SRC = "src_nekk_jr2025_nbb"
SRC2 = "src_nekk_site"
SRC3 = "src_kbo_nekk_0450062281"
SRC4 = "src_nekk_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00147494.pdf"
SRC2_URL = "https://www.denekker.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0450062281"
SRC4_URL = "https://www.provincieantwerpen.be/nl/locaties/de-nekker"
FOI_EMAIL = "reservatie@denekker.be"
FOI_POSTAL = "Nekkerspoel-Borcht 19 2800 Mechelen"
DRAFT = "docs/doge/foi/drafts/gap_nekk_omzet_empty_ops_3_67m_equity_neg_l5.md"
COMM = "comm_nekk_jr2025_pnl"
LB = "lb_nekk_omzet_empty_ops_3_67m_equity_neg"


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
                "title": "De Nekker vzw jaarrekening boekjaar 2025 (official NBB WVV VKT-VZW deposit 2026-00147494; AV 26.05.2026)",
                "url": SRC_URL,
                "publisher": "De Nekker vzw / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1378; official NBB VKT-VZW PDF 437kB 19p deposit 2026-00147494 created 09.06.2026 header 07.06.2026 neerlegging 10.06.2026; "
                    "leftover provincial EVA-vzw of mined Provincie Antwerpen; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Callens Vandelanotte Theunissen BV 0427.897.088 / Ken Snoeks 6725.80 excl btw; "
                    "oordeel zonder voorbehoud assets 753425 / PnL 81612; "
                    "VKT-VZW 6.1.1/6.1.3/6.3/6.5/7 not filed; omzet 70 empty; lidgeld/subsidies 73 empty; "
                    "terreinen/gebouwen 22 empty; 8349 empty; not every-10"
                ),
            },
            {
                "source_id": SRC2,
                "title": "De Nekker official site (provincial sport/recreation EVA Mechelen)",
                "url": SRC2_URL,
                "publisher": "De Nekker vzw / Provincie Antwerpen",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1378; leftover provincial EVA of Provincie Antwerpen; 65 ha domein; "
                    "statutory 2025 balans is the NBB CDN deposit; "
                    "contact reservatie@denekker.be / 015 55 70 05; directie@denekker.be in HHR"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO De Nekker vzw 0450.062.281",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1378; KBO 0450.062.281 Actief / normale toestand since 04.05.1993; "
                    "statutaire naam Provinciaal Sport- en Recreatiecentrum De Nekker since 04.05.1993; "
                    "afkorting EVAP PSRN since 03.12.2025; VZW since 04.05.1993; "
                    "zetel Nekkerspoel-Borcht 19 2800 Mechelen since 31.03.1995; 1 VE; "
                    "btw since 01.06.1993; RSZ since 01.06.1993; aanbestedende overheid since 04.05.1993; "
                    "boekjaar 31 december; NACE 93.110/56.301; "
                    "bestuurders Provincie Antwerpen 0207.725.597 + Netwerk Lokaal Sportbeleid 0417.039.919 + Colson Mireille + Mielants Philip; "
                    "dagelijks bestuur De Wit Danny since 01.11.2002"
                ),
            },
            {
                "source_id": SRC4,
                "title": "De Nekker FOI channel / official contact + provincie locatiepagina",
                "url": SRC4_URL,
                "publisher": "De Nekker vzw / Provincie Antwerpen",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1378; FOI reservatie@denekker.be / directie@denekker.be / 015 55 70 05; "
                    "Nekkerspoel-Borcht 19 2800 Mechelen; "
                    "moederbestuur Provincie Antwerpen Kon. Elisabethlei 22 2018 Antwerpen; "
                    "provincieantwerpen.be 403 this box for JR PDF; locatiepagina lists EVA + NBB doorverwijzing"
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
                "name_nl": "De Nekker vzw (leftover provinciaal EVA sport- en recreatiedomein Mechelen / EVAP PSRN)",
                "name_fr": "De Nekker ASBL (agence autonomisee provinciale residuelle / domaine sportif Malines)",
                "name_en": "De Nekker leftover provincial EVA-vzw sport/recreation domain Mechelen",
                "level": "province",
                "parent_id": "prov_antwerpen",
                "community_language": "nl",
                "website": "https://www.denekker.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1378 leftover residual provincial EVA-vzw of mined Provincie Antwerpen; "
                    "KBO 0450.062.281 Actief since 04.05.1993; official NBB WVV VKT-VZW PDF downloads; "
                    "sourced euros assets 753425 brutomarge 2960922 goods_diensten 3666352 pers 2566125 pnl 81612 equity -26184; "
                    "FOI ready omzet empty / 3.67m 60-61 / equity neg"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_nekk_assets_2025", ENT, "2025", "753425", "2025 assets 753425 VOL VKT-VZW 20/58; tick1378; primary official NBB WVV; commissaris 753425"),
        ("bud_nekk_assets_2024", ENT, "2024", "911019", "2024 assets 911019 comparative; tick1378; primary official NBB WVV 20/58"),
        ("bud_nekk_fixed_2025", ENT, "2025", "425742", "2025 vaste activa 425742 vs 614712; tick1378; primary official NBB WVV 21/28"),
        ("bud_nekk_mva_2025", ENT, "2025", "425742", "2025 MVA 425742 vs 614712; terreinen/gebouwen 22 empty; tick1378; primary official NBB WVV 22/27"),
        ("bud_nekk_machines_2025", ENT, "2025", "206104", "2025 installaties/machines 206104 vs 307090; tick1378; primary official NBB WVV 23"),
        ("bud_nekk_furniture_2025", ENT, "2025", "7622", "2025 meubilair/rollend 7622 vs 15244; tick1378; primary official NBB WVV 24"),
        ("bud_nekk_othmva_2025", ENT, "2025", "212016", "2025 overige MVA 212016 vs 292378; tick1378; primary official NBB WVV 26"),
        ("bud_nekk_mva_aanschaf_ye_2025", ENT, "2025", "2845461", "2025 MVA aanschaf YE 2845461 vs 2799612; tick1378; primary official NBB WVV 8199"),
        ("bud_nekk_mva_aanschaf_year_2025", ENT, "2025", "45849", "2025 MVA aanschaffingen 45849; tick1378; primary official NBB WVV 8169"),
        ("bud_nekk_mva_afschr_ye_2025", ENT, "2025", "2419720", "2025 MVA afschr YE 2419720 vs 2184900; tick1378; primary official NBB WVV 8329"),
        ("bud_nekk_current_2025", ENT, "2025", "327683", "2025 vlottende activa 327683 vs 296307; tick1378; primary official NBB WVV 29/58"),
        ("bud_nekk_inv_2025", ENT, "2025", "14141", "2025 voorraden 14141 vs 13814 (horeca FIFO); tick1378; primary official NBB WVV 3"),
        ("bud_nekk_strecv_2025", ENT, "2025", "83024", "2025 ST vorderingen 83024 vs 224646 (trade 83024; other 0 DROP vs 77981); tick1378; primary official NBB WVV 40/41"),
        ("bud_nekk_trade_2025", ENT, "2025", "83024", "2025 handelsvorderingen 83024 vs 146665; tick1378; primary official NBB WVV 40"),
        ("bud_nekk_cash_2025", ENT, "2025", "186206", "2025 liquide middelen 186206 JUMP vs 11136; tick1378; primary official NBB WVV 54/58"),
        ("bud_nekk_cash_2024", ENT, "2024", "11136", "2024 liquide middelen 11136 comparative; tick1378; primary official NBB WVV 54/58"),
        ("bud_nekk_prepaid_2025", ENT, "2025", "44312", "2025 overlopend actief 44312 vs 46711; tick1378; primary official NBB WVV 490/1"),
        ("bud_nekk_equity_2025", ENT, "2025", "-26184", "2025 eigen vermogen -26184 vs -107796 (art. 3:48§2 6° going concern; provincie support); tick1378; primary official NBB WVV 10/15"),
        ("bud_nekk_equity_2024", ENT, "2024", "-107796", "2024 eigen vermogen -107796 comparative; tick1378; primary official NBB WVV 10/15"),
        ("bud_nekk_funds_2025", ENT, "2025", "100000", "2025 bestemde fondsen 100000; tick1378; primary official NBB WVV 13"),
        ("bud_nekk_retained_2025", ENT, "2025", "-126184", "2025 overgedragen verlies -126184 vs -207796; tick1378; primary official NBB WVV 14"),
        ("bud_nekk_debt_2025", ENT, "2025", "779609", "2025 schulden 779609 vs 1018814; LT 17 empty; tick1378; primary official NBB WVV 17/49"),
        ("bud_nekk_debt_2024", ENT, "2024", "1018814", "2024 schulden 1018814 comparative; tick1378; primary official NBB WVV 17/49"),
        ("bud_nekk_st_2025", ENT, "2025", "554044", "2025 ST schulden 554044 vs 754140; tick1378; primary official NBB WVV 42/48"),
        ("bud_nekk_stbank_2025", ENT, "2025", "168834", "2025 ST bank 168834 vs 288322; tick1378; primary official NBB WVV 430/8"),
        ("bud_nekk_sttrade_2025", ENT, "2025", "168225", "2025 leveranciers 168225 vs 248213; tick1378; primary official NBB WVV 440/4"),
        ("bud_nekk_stsoc_2025", ENT, "2025", "193881", "2025 bezoldigingen/sociale lasten 193881 vs 201059 (tax 450/3 empty); tick1378; primary official NBB WVV 454/9"),
        ("bud_nekk_othdebt_2025", ENT, "2025", "23105", "2025 overige ST schulden 23105 vs 16546; tick1378; primary official NBB WVV 48"),
        ("bud_nekk_accrued_2025", ENT, "2025", "225565", "2025 overlopend passief 225565 vs 264674; tick1378; primary official NBB WVV 492/3"),
        ("bud_nekk_brutomarge_2025", ENT, "2025", "2960922", "2025 brutomarge 2960922 vs 2810029; omzet 70 empty; subsidies 73 empty; tick1378; primary official NBB WVV 9900"),
        ("bud_nekk_brutomarge_2024", ENT, "2024", "2810029", "2024 brutomarge 2810029 comparative; tick1378; primary official NBB WVV 9900"),
        ("bud_nekk_goods_diensten_2025", ENT, "2025", "3666352", "2025 handelsgoederen+diensten 3666352 vs 3630150 (60/61 combined; no split); tick1378; primary official NBB WVV 60/61"),
        ("bud_nekk_goods_diensten_2024", ENT, "2024", "3630150", "2024 handelsgoederen+diensten 3630150 comparative; tick1378; primary official NBB WVV 60/61"),
        ("bud_nekk_pers_2025", ENT, "2025", "2566125", "2025 bezoldigingen 2566125 / 49.4 VTE / 69868 uur / YE 47.5 VTE; tick1378; primary official NBB WVV 62 9087"),
        ("bud_nekk_pers_2024", ENT, "2024", "2387985", "2024 bezoldigingen 2387985 / 48.8 VTE comparative; tick1378; primary official NBB WVV 62"),
        ("bud_nekk_deprec_2025", ENT, "2025", "234819", "2025 afschrijvingen 234819 vs 225495; tick1378; primary official NBB WVV 630"),
        ("bud_nekk_wv_2025", ENT, "2025", "154", "2025 waardeverminderingen 154; tick1378; primary official NBB WVV 631/4"),
        ("bud_nekk_othcost_2025", ENT, "2025", "30551", "2025 andere bedrijfskosten 30551 vs 50287; tick1378; primary official NBB WVV 640/8"),
        ("bud_nekk_expl_2025", ENT, "2025", "129273", "2025 bedrijfswinst 129273 vs 146262; tick1378; primary official NBB WVV 9901"),
        ("bud_nekk_expl_2024", ENT, "2024", "146262", "2024 bedrijfswinst 146262 comparative; tick1378; primary official NBB WVV 9901"),
        ("bud_nekk_fininc_2025", ENT, "2025", "3977", "2025 financiele opbrengsten 3977 vs 2914; tick1378; primary official NBB WVV 75"),
        ("bud_nekk_fincost_2025", ENT, "2025", "51638", "2025 financiele kosten 51638 vs 53690; tick1378; primary official NBB WVV 65"),
        ("bud_nekk_pnl_2025", ENT, "2025", "81612", "2025 PnL 9904 81612 vs 95486 overgedragen; commissaris 81612; tick1378; primary official NBB WVV"),
        ("bud_nekk_pnl_2024", ENT, "2024", "95486", "2024 PnL 95486 comparative; tick1378; primary official NBB WVV 9904"),
        ("bud_nekk_comm_2025", ENT, "2025", "6726", "2025 commissaris Callens Vandelanotte / Ken Snoeks 6725.80 excl btw; tick1378; primary official NBB WVV 6.6"),
        ("bud_nekk_train_2025", ENT, "2025", "5738", "2025 formele opleiding mannen 5738 (3 koppen / 159 uur); tick1378; primary official NBB WVV 5803"),
        ("bud_nekk_in_vte_2025", ENT, "2025", "88", "2025 ingetreden 88.1 VTE / 87+2 koppen (seizoen); tick1378; primary official NBB WVV 205"),
        ("bud_nekk_out_vte_2025", ENT, "2025", "87", "2025 uitgetreden 87 VTE / 85+3 koppen (seizoen); tick1378; primary official NBB WVV 305"),
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
                "title": "De Nekker vzw JR2025 leftover EVA dual (assets 0.75m / goods+diensten 3.67m / omzet empty / equity -26k / PnL 82k)",
                "entity_id": ENT,
                "beneficiary": "De Nekker vzw / Provincie Antwerpen",
                "legal_basis": "WVV VZW; Bestuursdecreet EVA; provinciaal EVA-statuut; NBB neerlegging",
                "decision_date": "2026-05-26",
                "start_year": "1993",
                "end_year": "",
                "total_envelope_eur": "753425",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover provincial EVA map VL sport — 2.96m brutomarge (omzet 70 empty / subsidies 73 empty) / 3.67m 60-61 / equity -26k going concern",
                "cut_option": "Publish unpublished omzet 70 + subsidies 73 + 3.67m 60/61 split + provincie continuity amount; do not keep 65ha provincial sport EVA as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1378; assets 753425 brutomarge 2960922 goods_diensten 3666352 pnl 81612 equity -26184; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "De Nekker vzw JR2025 leftover EVA: assets 0.75m / goods+diensten 3.67m / omzet empty / equity -26k / PnL 82k",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "3666352",
                "total_cost_eur": "753425",
                "tco_notes": (
                    "Leftover dual provincial EVA-vzw of mined Provincie Antwerpen: "
                    "assets 0.75m / equity -26k / pnl 82k / brutomarge 2.96m (omzet 70 empty) / "
                    "goods+diensten 3.67m combined / 49.4 VTE / cash JUMP 11k to 186k / "
                    "official NBB WVV live; do not treat 0.75m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "De Nekker vzw / Provincie Antwerpen",
                "stated_goal": "Local leftover provincial EVA map VL sport — JR2025 live; dual omzet-empty/60-61/equity-neg FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 0.75m / goods+diensten 3.67m / omzet empty / equity -26k / pnl 82k",
                "absurdity_score": "7.2",
                "cost_score": "6.4",
                "difficulty": "2.4",
                "priority_index": "6.6",
                "cut_proposal": "Publish unpublished omzet 70 + subsidies 73 + 3.67m 60/61 split + provincie continuity amount; do not keep 65ha provincial sport EVA as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1378; leftover provincial EVA of mined Provincie Antwerpen; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "omzet WVV 70 empty + lidgeld/subsidies WVV 73 empty on VKT-VZW (brutomarge 2960922; 60/61 3666352 implies operating volume but omzet unpublished) "
                    "+ handelsgoederen/diensten 3666352 vs 3630150 (60/61 combined; no split) top-20 leveranciers "
                    "+ eigen vermogen -26184 vs -107796 + overgedragen -126184 + art. 3:48§2 6° provincie continuity support amount/form/besluit "
                    "+ terreinen/gebouwen 22 empty + 8349 empty (65ha provincial domain) "
                    "+ seizoen in 88.1 / uit 87 VTE vs avg 49.4 VTE "
                    "+ VKT-VZW 6.1.1/6.1.3/6.3/6.5/7 not filed + art. 9:14 §1 termijnen + ST bank 168834 path"
                ),
                "why_it_matters": (
                    "Leftover provincial EVA-vzw of mined Provincie Antwerpen "
                    "(same leftover dual seam as EVA LSM 1340 / Inagro 1332 / leftover APB POA-TPA-Schorre-Warande): "
                    "0.75m assets / 2.96m brutomarge / 3.67m goods+diensten / omzet unpublished / "
                    "equity -26k going-concern provincie guarantee / 49.4 VTE / 65ha domain "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "De Nekker vzw / Raad van Bestuur / Danny De Wit / Mireille Colson / Provincie Antwerpen",
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
                    "tick1378 leftover provincial EVA-vzw of mined Provincie Antwerpen after honest hunt; "
                    "live JR2025 official NBB WVV VKT-VZW PDF now extracted (437kB 19p deposit 2026-00147494). "
                    "MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. "
                    "IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. "
                    "IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. "
                    "Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. "
                    "Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 skipped. "
                    "Dommelhof leftover Limburg EVA not re-probed once live De Nekker extracted. "
                    "Otary RS Nuhma-adjacent fallback not taken. "
                    "IVAREM still 2024. leftover AGB 404/403 as of 1375. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1378",
        "title": "De Nekker vzw EVA JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: De Nekker vzw leftover provincial EVA of mined Provincie Antwerpen after honest hunt; KBO 0450.062.281 Actief; "
            "live JR2025 official NBB WVV VKT-VZW PDF (437kB 19p deposit 2026-00147494; commissaris Callens Vandelanotte); "
            "sourced euros assets 753425 / brutomarge 2960922 / goods_diensten 3666352 / pers 2566125 / pnl 81612 / equity -26184; "
            "FOI ready omzet empty / 3.67m 60-61 / equity neg"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T05:00:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1378 De Nekker leftover provincial EVA residual; KBO 0450.062.281; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1379 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1379",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1378 done including De Nekker 1378 leftover provincial EVA live NBB WVV / "
            "MIROM Menen 1377 leftover IGS live NBB WVV / "
            "MIROM Roeselare 1376 leftover IGS live NBB WVV / "
            "IVAGO 1375 leftover IGS live NBB WVV / "
            "MIWA 1374 leftover IGS live NBB WVV / "
            "IVOO 1373 leftover IGS live NBB WVV / "
            "IGEMO 1372 leftover IGS live NBB WVV / "
            "Veneco 1371 leftover IGS live NBB WVV / "
            "Haviland 1370 leftover IGS live NBB WVV + every-10 / "
            "IMOG 1369 leftover IGS live NBB WVV / "
            "IOK 1368 leftover IGS live NBB WVV / "
            "Leiedal 1367 leftover IGS live NBB WVV / "
            "Interleuven 1366 leftover IGS live NBB WVV / "
            "s-Lim DV 1365 leftover IGS live NBB WVV / "
            "Herkenrode RE NV 1364 leftover vastgoed live NBB WVV / "
            "MyCSN NV 1363 leftover smart-city live NBB WVV / "
            "s-Lim CV 1362 leftover smart-city live NBB WVV / "
            "Nuhmeris NV 1361 leftover klimaat-holding live NBB WVV / "
            "ECO2050 cv 1360 leftover klimaat-coop live NBB WVV + every-10); "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if a new live 2025 WVV PDF downloads (prefer leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; Otary CDN 2026-00254280 live prior tick, not taken); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB PIH / APB Inovant / APB Atlas listed or leftover but provincieantwerpen.be 403 — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1378 after De Nekker leftover provincial EVA live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1378", rq_new, rq_spawn)
    print("research_queue 1378", found, "spawned_1379", spawned)

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
                "last_unit_id": "rq_1378",
                "ticks_completed": "1378",
                "paused": "no",
                "notes": (
                    "tick1378 De Nekker leftover provincial EVA residual; KBO 0450.062.281; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 753425 brutomarge 2960922 goods_diensten 3666352 pers 2566125 pnl 81612 equity -26184; "
                    "FOI ready omzet empty/3.67m 60-61/equity neg; next rq_1379 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    entry = """### Tick 1378 - 2026-08-19 - rq_1378 De Nekker dual residual leftover
- Unit: Provinciaal Sport- en Recreatiecentrum De Nekker vzw (leftover provincial EVA / EVAP PSRN of mined Provincie Antwerpen; 65 ha sport- en recreatiedomein Mechelen: Nekkerpool / zwemvijver / sportverblijf / kampeerhutten / horeca) after residual dual hunt (KBO **0450.062.281**; official denekker.be / provincieantwerpen.be have privacy/HHR/statuten but no isolated statutory 2025 balans — provincie page 403 for JR and points to NBB; live NBB WVV VKT-VZW deposit **2026-00147494** PDF 437kB / 19p; AV **26.05.2026**; PDF created **09.06.2026**; header **07.06.2026**; neerlegging SBM **10.06.2026**; commissaris Callens, Vandelanotte & Theunissen BV 0427.897.088 / Ken Snoeks 6.725,80 excl. btw signed 26.05.2026 17:24 +02 oordeel zonder voorbehoud assets 753.425 / PnL 81.612 + vermelding art. 9:14 §1 termijnen; 9e opeenvolgend boekjaar; mandaat AV 21.11.2023 tot AV YE 2025). Leftover provincial EVA-vzw whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last ticks listed De Nekker CDN 2026-00147494 as leftover next after MIROM Menen 1377). Distinct from already-mined MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **04.05.1993**; statutaire naam Provinciaal Sport- en Recreatiecentrum De Nekker since 04.05.1993; afkorting EVAP PSRN since 03.12.2025; Vereniging zonder winstoogmerk since 04.05.1993; zetel Nekkerspoel-Borcht 19 2800 Mechelen since 31.03.1995; **1 VE**; tel 015 55 70 05; e-mail reservatie@denekker.be; web https://www.denekker.be/; btw since 01.06.1993; RSZ since 01.06.1993; aanbestedende overheid since 04.05.1993; boekjaar 31 december; NACE 93.110/56.301. Statutory bestuur: Provincie Antwerpen 0207.725.597 (Francois Catherine / Reydams Daan / Opdenbergh Els / Palinckx Koen / De Cleene Lenn / Stevens Lili / Colson Mireille / Cuylaerts Nathalie / Sohier Rudy / De Keyser Stef) + KBO extra Netwerk Lokaal Sportbeleid 0417.039.919 / Colson Mireille / Mielants Philip; dagelijks bestuur De Wit Danny since 01.11.2002. Hunt leftover AGB/zorg/EVA first: leftover AGB Mechelen/Kortrijk/Brugge/Roeselare/Oostende 404/403 as of 1375 — not re-probed once live De Nekker extracted; Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live De Nekker extracted; IVAREM still 2024 as of 1375; leftover APB provincieantwerpen.be 403. De Nekker statutory CDN live this tick (HTTP 200 / 436756 / 19p) — taken (preferred leftover provincial EVA of mined Provincie Antwerpen outside Nuhma). MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 already mined — skipped. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. NBB consult skipped (403/SPA); euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366. Not every-10 (next 1380).
- EUR strong (primary official WVV VKT-VZW + commissaris oordeel zonder voorbehoud; VKT-VZW 6.1.1/6.1.3/6.3/6.5/7 not filed; omzet 70 empty; lidgeld/subsidies 73 empty; terreinen/gebouwen 22 empty; 8349 empty): assets **753.425** (was 911.019); fixed **425.742** / MVA **425.742** (machines **206.104** vs 307.090; overige **212.016** vs 292.378; meubilair 7.622; gebouwen empty; aanschaf year **45.849** / YE aanschaf **2.845.461** / afschr cum **2.419.720**); current **327.683**; inventory 14.141; ST recv **83.024** (trade 83.024; other **0 DROP** vs 77.981); beleggingen empty; cash **186.206 JUMP** vs 11.136; prepaid 44.312; equity **−26.184** (was −107.796; bestemde fondsen 100.000; overgedragen **−126.184**); voorzieningen empty; schulden **779.609** (LT empty; ST **554.044** waarvan bank **168.834** + leveranciers 168.225 + soc 193.881 + overige 23.105; accruals 225.565); brutomarge **2.960.922** vs 2.810.029 (omzet 70 unpublished); goods+diensten **3.666.352** (60/61 combined); pers **2.566.125** / **49,4 VTE** / 69.868 uur / YE 47,5 VTE (43+7 onbepaalde tijd; bedienden 23 / arbeiders 24,5; PC 302+329) + seizoen in **88,1 VTE** / uit **87 VTE**; afschr 234.819; andere kosten 30.551; expl **+129.273** vs 146.262; fin opbr 3.977; fin kosten 51.638; PnL **81.612** vs 95.486 overgedragen; commissaris 6.726. Continuity art. 3:48§2 6°: Provincie Antwerpen financial support guarantee (amount unpublished). Commissaris: art. 9:14 §1 WVV termijnen niet gerespecteerd.
- CSVs: sources+4/entities+1/budgets+48/commitments+1/leaderboard+1 + FOI ready `gap_nekk_omzet_empty_ops_3_67m_equity_neg_l5` (not sent); rq_1378=done; spawn rq_1379; ticks=1378.
- Coverage: residual dual L5 (De Nekker leftover provincial EVA live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1380).
- Next: rq_1379 residual dual L5 VL JR2025 hole_fill (prefer leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS CDN 2026-00254280 / Rematics / Sunfin only if taken after leftover IGS/EVA/AGB; leftover APB POA / TPA / De Schorre / Warande / PIH / Inovant / Atlas only if a real PDF downloads; IVAREM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1378 write done")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Tick 1395 — leftover IGS Hofheide JR2025 official NBB WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1395"
UTC = "2026-08-19T04:40:00Z"
ENT = "igs_hofh"
HIER = "Vlaanderen>VlaamsBrabant>IGS>Hofheide"
GAP = "gap_hofh_omzet_empty_debt_5_59m_machines_1_06m_l5"
SRC = "src_hofh_jr2025_nbb"
SRC2 = "src_hofh_site"
SRC3 = "src_kbo_hofh_0872310211"
SRC4 = "src_hofh_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00343763.pdf"
SRC2_URL = "https://www.hofheide.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0872310211"
SRC4_URL = "https://www.hofheide.be/contact/contacteer-hofheide"
FOI_EMAIL = "info@hofheide.be"
FOI_POSTAL = "Jennekensstraat 5 3221 Nieuwrode (Holsbeek)"
DRAFT = "docs/doge/foi/drafts/gap_hofh_omzet_empty_debt_5_59m_machines_1_06m_l5.md"
COMM = "comm_hofh_jr2025_pnl"
LB = "lb_hofh_omzet_empty_debt_5_59m_machines_1_06m"

VENNOTEN = (
    "28 gemeenten van het arrondissement Leuven + provincie Vlaams-Brabant "
    "(hofheide.be; named list unpublished this extract; founded 28.01.2005; "
    "verlengd 18 jaar; inbreng 2620746 onbeschikbaar)"
)


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


BUDGETS = [
    ("bud_hofh_assets_2025", "2025", "10925977", "2025 assets 10925977 VKT-inb 20/58; tick1395; primary official NBB WVV"),
    ("bud_hofh_assets_2024", "2024", "11086189", "2024 assets 11086189 comparative; tick1395; primary official NBB WVV 20/58"),
    ("bud_hofh_fixed_2025", "2025", "9696556", "2025 vaste activa 9696556 vs 9393224; tick1395; primary official NBB WVV 21/28"),
    ("bud_hofh_iva_2025", "2025", "22128", "2025 IVA 22128 vs 689; tick1395; primary official NBB WVV 21"),
    ("bud_hofh_mva_2025", "2025", "9673103", "2025 MVA 9673103 vs 9391210; tick1395; primary official NBB WVV 22/27"),
    ("bud_hofh_buildings_2025", "2025", "8404007", "2025 terreinen/gebouwen 8404007 vs 8871925; tick1395; primary official NBB WVV 22"),
    ("bud_hofh_machines_2025", "2025", "1063705", "2025 machines 1063705 JUMP vs 347437; tick1395; primary official NBB WVV 23"),
    ("bud_hofh_machines_2024", "2024", "347437", "2024 machines 347437 comparative; tick1395; primary official NBB WVV 23"),
    ("bud_hofh_furniture_2025", "2025", "108174", "2025 meubilair 108174 vs 74631; tick1395; primary official NBB WVV 24"),
    ("bud_hofh_othmva_2025", "2025", "97217", "2025 overige MVA 97217 unchanged; tick1395; primary official NBB WVV 26"),
    ("bud_hofh_fva_2025", "2025", "1324", "2025 FVA 1324 vs 1324; aanschaf 5074 minus niet-opgevraagd 3750; tick1395; primary official NBB WVV 28"),
    ("bud_hofh_current_2025", "2025", "1229421", "2025 vlottend 1229421 vs 1692965; tick1395; primary official NBB WVV 29/58"),
    ("bud_hofh_stocks_2025", "2025", "19412", "2025 voorraden 19412 vs 26093; tick1395; primary official NBB WVV 30/36"),
    ("bud_hofh_strecv_2025", "2025", "340967", "2025 ST vorderingen 340967 vs 294258; tick1395; primary official NBB WVV 40/41"),
    ("bud_hofh_trade_2025", "2025", "336153", "2025 handelsvorderingen 336153 vs 289340; tick1395; primary official NBB WVV 40"),
    ("bud_hofh_invest_2025", "2025", "550000", "2025 geldbeleggingen 550000 DROP vs 1050000; tick1395; primary official NBB WVV 50/53"),
    ("bud_hofh_invest_2024", "2024", "1050000", "2024 geldbeleggingen 1050000 comparative; tick1395; primary official NBB WVV 50/53"),
    ("bud_hofh_cash_2025", "2025", "305842", "2025 liquide middelen 305842 vs 299373; tick1395; primary official NBB WVV 54/58"),
    ("bud_hofh_cash_2024", "2024", "299373", "2024 liquide middelen 299373 comparative; tick1395; primary official NBB WVV 54/58"),
    ("bud_hofh_prepaid_2025", "2025", "13200", "2025 overlopend actief 13200 vs 23241; tick1395; primary official NBB WVV 490/1"),
    ("bud_hofh_equity_2025", "2025", "5334842", "2025 EV 5334842 vs 5408284; tick1395; primary official NBB WVV 10/15"),
    ("bud_hofh_inbreng_2025", "2025", "2620746", "2025 inbreng 2620746 onbeschikbaar; tick1395; primary official NBB WVV 10/11"),
    ("bud_hofh_reserves_2025", "2025", "987246", "2025 reserves 987246 vs 959114 beschikbaar; tick1395; primary official NBB WVV 13"),
    ("bud_hofh_capsub_2025", "2025", "1726850", "2025 kapitaalsubsidies 1726850 vs 1828423; tick1395; primary official NBB WVV 15"),
    ("bud_hofh_debt_2025", "2025", "5591135", "2025 schulden 5591135 vs 5677905; tick1395; primary official NBB WVV 17/49"),
    ("bud_hofh_debt_2024", "2024", "5677905", "2024 schulden 5677905 comparative; tick1395; primary official NBB WVV 17/49"),
    ("bud_hofh_lt_2025", "2025", "4393056", "2025 LT bank 4393056 vs 4904594; tick1395; primary official NBB WVV 17"),
    ("bud_hofh_st_2025", "2025", "1132454", "2025 ST schulden 1132454 vs 690702; tick1395; primary official NBB WVV 42/48"),
    ("bud_hofh_ltdue_2025", "2025", "511538", "2025 LT-due binnen jaar 511538 vs 489244; tick1395; primary official NBB WVV 42"),
    ("bud_hofh_stfin_2025", "2025", "22561", "2025 ST overige leningen 22561 vs 24681; tick1395; primary official NBB WVV 439"),
    ("bud_hofh_sttrade_2025", "2025", "487485", "2025 leveranciers 487485 JUMP vs 97671; tick1395; primary official NBB WVV 440/4"),
    ("bud_hofh_sttax_2025", "2025", "19244", "2025 belastingschulden 19244 vs 3339; tick1395; primary official NBB WVV 450/3"),
    ("bud_hofh_stsoc_2025", "2025", "91626", "2025 bezoldigingen/sociale lasten 91626 vs 75767; tick1395; primary official NBB WVV 454/9"),
    ("bud_hofh_accrued_2025", "2025", "65625", "2025 overlopend passief 65625 vs 82610; tick1395; primary official NBB WVV 492/3"),
    ("bud_hofh_govguar_2025", "2025", "4904594", "2025 overheidswaarborg 4904594 (LT+due); tick1395; primary official NBB WVV 9061"),
    ("bud_hofh_debt15_2025", "2025", "2291295", "2025 schuld 1-5y 2291295; tick1395; primary official NBB WVV 8912"),
    ("bud_hofh_debt5y_2025", "2025", "2101761", "2025 schuld >5y 2101761; tick1395; primary official NBB WVV 8913"),
    ("bud_hofh_provguar_2025", "2025", "9000000", "2025 provincie Vlaams-Brabant waarborg 9000000 off-balance; tick1395; primary official NBB WVV 6.5"),
    ("bud_hofh_brutomarge_2025", "2025", "1750457", "2025 brutomarge 1750457 vs 1947496; omzet 70 empty; tick1395; primary official NBB WVV 9900"),
    ("bud_hofh_brutomarge_2024", "2024", "1947496", "2024 brutomarge 1947496 comparative; tick1395; primary official NBB WVV 9900"),
    ("bud_hofh_pers_2025", "2025", "1006636", "2025 pers 1006636 vs 908018 / 12 VTE; tick1395; primary official NBB WVV 62"),
    ("bud_hofh_pers_2024", "2024", "908018", "2024 pers 908018 / 11 VTE comparative; tick1395; primary official NBB WVV 62"),
    ("bud_hofh_afschr_2025", "2025", "590538", "2025 afschr 590538 vs 570103; tick1395; primary official NBB WVV 630"),
    ("bud_hofh_othcost_2025", "2025", "14954", "2025 andere bedrijfskosten 14954 vs 49869; tick1395; primary official NBB WVV 640/8"),
    ("bud_hofh_expl_2025", "2025", "144115", "2025 expl +144115 vs +447058; tick1395; primary official NBB WVV 9901"),
    ("bud_hofh_expl_2024", "2024", "447058", "2024 expl +447058 comparative; tick1395; primary official NBB WVV 9901"),
    ("bud_hofh_fininc_2025", "2025", "125237", "2025 financiele opbrengsten 125237 vs 90127 (capsub 101573); tick1395; primary official NBB WVV 75"),
    ("bud_hofh_capsub_inc_2025", "2025", "101573", "2025 kapitaal- en interestsubsidies 101573 vs 59129; tick1395; primary official NBB WVV 753/9078"),
    ("bud_hofh_fincost_2025", "2025", "241220", "2025 financiele kosten 241220 vs 261879; tick1395; primary official NBB WVV 65"),
    ("bud_hofh_pnl_2025", "2025", "28132", "2025 PnL +28132 vs +275305 all to reserves; tick1395; primary official NBB WVV 9904"),
    ("bud_hofh_pnl_2024", "2024", "275305", "2024 PnL +275305 comparative; tick1395; primary official NBB WVV 9904"),
    ("bud_hofh_div_2025", "2025", "0", "2025 dividend 694 empty; tick1395; primary official NBB WVV 694"),
    ("bud_hofh_capex_mva_2025", "2025", "871895", "2025 MVA aanschaf 871895 (8169); tick1395; primary official NBB WVV 6.1.2"),
    ("bud_hofh_capex_iva_2025", "2025", "21974", "2025 IVA aanschaf 21974 (8029); tick1395; primary official NBB WVV 6.1.1"),
    ("bud_hofh_comm_2025", "2025", "6988", "2025 commissaris CVT 6988 excl btw; tick1395; primary official NBB WVV 6.6"),
    ("bud_hofh_board_2025", "2025", "42019", "2025 bestuurders presentiegeld 42019.20; tick1395; primary official NBB WVV remuneratieverslag"),
]


def main() -> None:
    step = sys.argv[1] if len(sys.argv) > 1 else "all"

    if step in ("all", "sources"):
        n = append_rows(
            DATA / "sources.csv",
            [
                {
                    "source_id": SRC,
                    "title": "IGS Hofheide jaarrekening boekjaar 2025 (official NBB WVV VKT-inb deposit 2026-00343763; AV 24.06.2026)",
                    "url": SRC_URL,
                    "publisher": "IGS Hofheide / NBB WVV deposit",
                    "accessed_date": "2026-08-19",
                    "source_class": "budget",
                    "notes": (
                        "tick1395; official NBB VKT-inb PDF 2.92MB 34p deposit 2026-00343763 header 23.07.2026; "
                        "leftover IGS crematorium arrondissement Leuven Holsbeek; "
                        "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                        "Belscope/Companyweb extracted tables not used; Staatsbladmonitor table euros not used; "
                        "commissaris Callens Vandelanotte Theunissen BV B00003 / 0427.897.088 / Marc Maris A01728 fee 6988; "
                        "omzet 70 empty; 60/61 empty; only brutomarge published; 6.6 related empty except commissaris"
                    ),
                },
                {
                    "source_id": SRC2,
                    "title": "IGS Hofheide official site (leftover crematorium IGS arrondissement Leuven; 28 gemeenten + provincie)",
                    "url": SRC2_URL,
                    "publisher": "IGS Hofheide",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1395; leftover crematorium IGS of 28 arrondissement-Leuven municipalities + provincie Vlaams-Brabant; "
                        "site quote opgericht door 28 gemeenten; statutory 2025 balans is the NBB CDN deposit"
                    ),
                },
                {
                    "source_id": SRC3,
                    "title": "KBO IGS Hofheide 0872.310.211",
                    "url": SRC3_URL,
                    "publisher": "KBO Public Search FOD Economie",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1395; KBO 0872.310.211 Actief / normale toestand since 15.02.2005; "
                        "statutaire naam OPDRACHTHOUDENDE VERENIGING VOOR CREMATORIUMBEHEER IN HET ARRONDISSEMENT LEUVEN / IGS Hofheide since 15.02.2005; "
                        "Opdrachthoudende vereniging (Vlaams Gewest) since 15.02.2005; "
                        "zetel Jennekensstraat 5 3221 Holsbeek since 23.05.2017; 1 VE; "
                        "KBO tel 016/44 29 50; KBO email directie@hofheide.be since 17.11.2025; web http://www.hofheide.be; "
                        "btw since 01.02.2006; RSZ since 01.01.2022; NACE 96.302; aanbestedende overheid since 15.02.2005; "
                        "KBO bestuurder Ann Schevenels since 26.03.2019"
                    ),
                },
                {
                    "source_id": SRC4,
                    "title": "IGS Hofheide FOI channel / official contact (info@hofheide.be; 016/44 29 50)",
                    "url": SRC4_URL,
                    "publisher": "IGS Hofheide",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1395; site contact info@hofheide.be; KBO directie@hofheide.be; tel 016/44 29 50; "
                        "voorzitter Ann Schevenels ann.schevenels@vlaamsbrabant.be; directeur Ann Van Staey ann.van.staey@hofheide.be"
                    ),
                },
            ],
        )
        print("sources", n)

    if step in ("all", "entities"):
        n = append_rows(
            DATA / "entities.csv",
            [
                {
                    "entity_id": ENT,
                    "name_nl": "IGS Hofheide (Opdrachthoudende Vereniging voor Crematoriumbeheer in het Arrondissement Leuven; leftover IGS crematorium Holsbeek)",
                    "name_fr": "IGS Hofheide (association missionnee crematorium arrondissement Louvain; IGS residuel)",
                    "name_en": "IGS Hofheide leftover IGS crematorium arrondissement Leuven Holsbeek",
                    "level": "other",
                    "parent_id": "sec_flanders",
                    "community_language": "nl",
                    "website": "https://www.hofheide.be/",
                    "foi_email": FOI_EMAIL,
                    "foi_postal": FOI_POSTAL,
                    "notes": (
                        "tick1395 leftover residual IGS Hofheide crematorium IGS; "
                        "KBO 0872.310.211 Actief since 15.02.2005; official NBB WVV VKT-inb PDF downloads; "
                        "sourced euros assets 10925977 omzet empty diensten empty pers 1006636 debt 5591135 pnl 28132 equity 5334842 capex 871895 machines 1063705; "
                        "FOI ready omzet empty / 60-61 empty / 5.59m debt / 9.00m provincie waarborg / 872k machines capex; "
                        "distinct from already-mined IGS Westlede 1394 prefix wstl and HAVICREM 1393 prefix hvic and IVLA 1392 / Fluvius stack 1382-1391"
                    ),
                },
            ],
        )
        print("entities", n)

    if step in ("all", "budgets"):
        n = append_rows(
            DATA / "budgets.csv",
            [
                {
                    "budget_id": bid,
                    "entity_id": ENT,
                    "year": year,
                    "amount_eur": amt,
                    "amount_min_eur": "",
                    "amount_max_eur": "",
                    "basis": "executed",
                    "source_id": SRC,
                    "confidence": "strong",
                    "notes": notes,
                }
                for bid, year, amt, notes in BUDGETS
            ],
        )
        print("budgets", n)

    if step in ("all", "commitments"):
        n = append_rows(
            DATA / "commitments.csv",
            [
                {
                    "commitment_id": COMM,
                    "title": "IGS Hofheide JR2025 leftover IGS dual (assets 10.93m / omzet empty / debt 5.59m / machines 1.06m / PnL +28k)",
                    "entity_id": ENT,
                    "beneficiary": "IGS Hofheide / " + VENNOTEN,
                    "legal_basis": "WVV OV; Decreet Lokaal Bestuur; NBB neerlegging",
                    "decision_date": "2026-06-24",
                    "start_year": "2005",
                    "end_year": "",
                    "total_envelope_eur": "5591135",
                    "cash_by_year": "",
                    "remaining_eur": "",
                    "status": "active",
                    "evaluation_url": SRC_URL,
                    "stated_goal": "Local leftover IGS map VL crematorium Leuven — omzet unpublished / 5.59m bank / 9.00m provincie waarborg / 872k machines capex / PnL +28k",
                    "cut_option": "Publish omzet + 60/61 split + 5.59m bank counterparties/terms + 9.00m provincie waarborg + 872k machines tender; do not keep crematorium IGS as dual unpublished vehicle",
                    "source_id": SRC,
                    "confidence": "strong",
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "notes": "tick1395; assets 10925977 omzet empty diensten empty pers 1006636 debt 5591135 pnl 28132 equity 5334842 capex 871895 machines 1063705; FOI ready not sent; not TE-additive of 348bn",
                }
            ],
        )
        print("commitments", n)

    if step in ("all", "leaderboard"):
        n = append_rows(
            DATA / "leaderboard.csv",
            [
                {
                    "item_id": LB,
                    "name": "IGS Hofheide JR2025 leftover IGS: assets 10.93m / omzet empty / debt 5.59m / machines 1.06m / 12 VTE",
                    "level": "L5",
                    "type": "local_budget_line",
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "annual_cost_eur": "1006636",
                    "total_cost_eur": "5591135",
                    "tco_notes": (
                        "Leftover dual IGS crematorium Leuven (28 arrondissement-Leuven municipalities + provincie): "
                        "assets 10.93m / equity 5.33m / pnl +28k / omzet unpublished / 60-61 unpublished / "
                        "diensten unpublished / pers 1.01m / 12 VTE / "
                        "debt 5.59m (LT bank 4.39m; gov-guaranteed 4.90m; provincie 9.00m) / cash 306k / capex 872k machines JUMP 1.06m; "
                        "official NBB WVV live; do not treat 5.59m as TE-additive of 348bn"
                    ),
                    "confidence": "strong",
                    "source_id": SRC,
                    "beneficiaries": "IGS Hofheide / " + VENNOTEN,
                    "stated_goal": "Local leftover IGS map VL crematorium Leuven — JR2025 live; dual omzet/debt/machines FOI",
                    "measured_outcome": "Official NBB WVV 2026-08-19: assets 10.93m / omzet empty / debt 5.59m / machines 1.06m / pnl +28k / 12 VTE",
                    "absurdity_score": "6.5",
                    "cost_score": "6.0",
                    "difficulty": "3.0",
                    "priority_index": "5.9",
                    "cut_proposal": "Publish omzet + 60/61 split + 5.59m bank counterparties/terms + 9.00m provincie waarborg + 872k machines tender; do not keep crematorium IGS as dual unpublished vehicle",
                    "status": "active",
                    "struck_reason": "",
                    "notes": "tick1395; leftover IGS Hofheide crematorium IGS; FOI ready not sent; not TE-additive of 348bn; distinct from IGS Westlede 1394 and HAVICREM 1393 and IVLA 1392 / Fluvius stack 1382-1391",
                }
            ],
        )
        print("leaderboard", n)

    if step in ("all", "foi"):
        n = append_rows(
            DATA / "foi_queue.csv",
            [
                {
                    "gap_id": GAP,
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "entity_id": ENT,
                    "what_is_missing": (
                        "omzet WVV 70 empty + 60/61 empty (abbreviated VKT; only brutomarge 1750457 vs 1947496 published) per stroom/vennoot unpublished "
                        "+ schulden 5591135 vs 5677905 (LT bank 4393056 + ST due 511538; gov-guaranteed 4904594; provincie waarborg 9000000) counterparties/terms unpublished "
                        "+ machines 1063705 JUMP vs 347437 / MVA aanschaf 871895 tender/unit price unpublished "
                        "+ geldbeleggingen 550000 DROP vs 1050000 nature unpublished "
                        "+ pers 1006636 / 12 VTE / 20397 uur split unpublished "
                        "+ 6.6 related empty + dividend 694 empty + commissarisverslag p24-28 image-only"
                    ),
                    "why_it_matters": (
                        "Leftover IGS crematorium Leuven of 28 mined arrondissement-Leuven municipalities + provincie Vlaams-Brabant "
                        "(distinct from IGS Westlede 1394 and HAVICREM 1393 and from IVLA 1392 / Fluvius 1382-1391): "
                        "10.93m assets / omzet unpublished / 60-61 unpublished / 5.59m bank / 9.00m provincie waarborg / 872k machines capex / "
                        "abbreviated VKT hides omzet and diensten "
                        "is a dual opacity residual, not TE-additive of 348bn."
                    ),
                    "priority": "8",
                    "recipient_body": "IGS Hofheide / Raad van Bestuur / Ann Schevenels / Boudewijn Herbots / Ann Van Staey / 28 vennoten + provincie Vlaams-Brabant",
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
                        "tick1395 leftover IGS crematorium Leuven of 28 arrondissement-Leuven municipalities + provincie after honest hunt; "
                        "live JR2025 official NBB WVV VKT-inb PDF now extracted (2.92MB 34p deposit 2026-00343763). "
                        "IGS Westlede already mined 1394 — skipped. HAVICREM already mined 1393 — skipped. IVLA already mined 1392 — skipped. Fluvius stack already mined 1382-1391 — skipped. "
                        "Pontes leftover next if a 2025 PDF downloads. Dommelhof leftover next if a JR2025 PDF now downloads. "
                        "Otary RS Nuhma-adjacent fallback not taken. "
                        "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                    ),
                }
            ],
        )
        print("foi", n)

    if step in ("all", "rq"):
        rq_new = {
            "task_id": "rq_1395",
            "title": "IGS Hofheide JR2025 leftover dual residual",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "done",
            "hierarchy_target": "L5",
            "entity_id": ENT,
            "instructions": (
                "Completed: IGS Hofheide leftover IGS crematorium Leuven of 28 arrondissement-Leuven municipalities + provincie Vlaams-Brabant after honest hunt; "
                "KBO 0872.310.211 Actief; live JR2025 official NBB WVV VKT-inb PDF (2.92MB 34p deposit 2026-00343763; commissaris CVT); "
                "sourced euros assets 10925977 / omzet empty / diensten empty / pers 1006636 / debt 5591135 / pnl 28132 / capex 871895 / machines 1063705; "
                "FOI ready omzet empty / 60-61 empty / 5.59m debt / 9.00m provincie waarborg / 872k machines capex"
            ),
            "blocked_gap_id": GAP,
            "created_utc": "2026-08-19T04:25:00Z",
            "updated_utc": UTC,
            "notes": (
                "tick1395 IGS Hofheide leftover IGS crematorium residual; KBO 0872.310.211; "
                "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1396 residual dual L5 VL"
            ),
        }
        rq_spawn = {
            "task_id": "rq_1396",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
                "(prior 1255-1395 done including IGS Hofheide 1395 leftover crematorium IGS live NBB WVV / "
                "IGS Westlede 1394 leftover crematorium IGS live NBB WVV / "
                "HAVICREM 1393 leftover crematorium IGS live NBB WVV / "
                "IVLA 1392 leftover waste IGS live NBB WVV / "
                "Fluvius OV 1391 leftover personnel OV live NBB WVV); "
                "leftover IGS Pontes (Wilrijk/Turnhout/Lommel) — take if a 2025 statutory PDF downloads; "
                "leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; "
                "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
                "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
                "skip already-mined IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / ILvA 1344; "
                "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
                "ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick1395 after IGS Hofheide leftover crematorium IGS live NBB WVV; next residual dual L5 VL",
        }
        found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1395", rq_new, rq_spawn)
        print("research_queue 1395", found, "spawned_1396", spawned)

    if step in ("all", "state"):
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
                    "last_unit_id": "rq_1395",
                    "ticks_completed": "1395",
                    "paused": "no",
                    "notes": (
                        "tick1395 IGS Hofheide leftover IGS crematorium residual; KBO 0872.310.211; "
                        "live JR2025 NBB WVV PDF; sourced euros assets 10925977 omzet empty diensten empty pers 1006636 debt 5591135 pnl 28132 equity 5334842 capex 871895 machines 1063705; "
                        "FOI ready omzet-empty/5.59m debt/9.00m provincie/872k machines; next rq_1396 residual dual L5 VL; continuous hole_fill"
                    ),
                }
            )
        print("loop_state ok")

    if step in ("all", "log"):
        log = ROOT / "loop_log.md"
        entry = (
            "### Tick 1395 - 2026-08-19 - rq_1395 IGS Hofheide dual residual leftover\n"
            "- Unit: IGS Hofheide / Opdrachthoudende Vereniging voor Crematoriumbeheer in het Arrondissement Leuven (leftover IGS opdrachthoudende vereniging / crematorium of 28 mined arrondissement-Leuven municipalities + provincie Vlaams-Brabant; vestiging Holsbeek Nieuwrode) after residual dual hunt (KBO **0872.310.211**; official hofheide.be has contact + 28 gemeenten quote; live NBB WVV VKT-inb deposit **2026-00343763** PDF 2.92MB / 34p; AV **24.06.2026**; header **23.07.2026**; commissaris Callens, Vandelanotte, Theunissen BV B00003 / 0427.897.088 / Marc Maris A01728 fee 6.988 excl. btw). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; preferred leftover Hofheide with live CDN this tick). Distinct from already-mined IGS Westlede 1394 (prefix `wstl`) and HAVICREM 1393 (prefix `hvic`) and from IVLA 1392 / Fluvius stack 1382-1391. First confirmed not already mined: no Hofheide / 0872.310.211 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **15.02.2005**; statutaire naam OPDRACHTHOUDENDE VERENIGING VOOR CREMATORIUMBEHEER IN HET ARRONDISSEMENT LEUVEN / IGS Hofheide since 15.02.2005; Opdrachthoudende vereniging (Vlaams Gewest) since 15.02.2005; zetel Jennekensstraat 5 3221 Holsbeek since 23.05.2017; **1 VE**; KBO tel 016/44 29 50; KBO e-mail directie@hofheide.be since 17.11.2025; official site https://www.hofheide.be/; btw since 01.02.2006; RSZ since 01.01.2022; NACE 96.302. Voorzitter Ann Schevenels since 26.03.2019; ondervoorzitter Boudewijn Herbots since 26.03.2025; directeur Ann Van Staey (site). Contact info@hofheide.be; tel 016/44 29 50. Hunt leftover Hofheide first: statutory CDN live this tick (HTTP 200 / 2921444 / 34p) — taken. IGS Westlede already mined 1394 — skipped. HAVICREM already mined 1393 — skipped. IVLA already mined 1392 — skipped. Fluvius stack already mined 1382-1391 — skipped. Leftover IGS Pontes / AGB/zorg/EVA/APB not taken once live Hofheide extracted. Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live Hofheide extracted. Otary RS Nuhma-adjacent fallback not taken. NBB consult skipped (403/SPA); euros extracted from the official VKT-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used. Not every-10 (next 1400).\n"
            "- EUR strong (primary official WVV VKT-inb; **omzet 70 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; 6.2/6.7/6.9/7/8/10/14-16 not filed; 6.6 related empty except commissaris): assets **10.925.977** (was 11.086.189); fixed **9.696.556** / MVA **9.673.103** (gebouwen **8.404.007**; machines **1.063.705 JUMP** vs 347.437; meubilair **108.174**; overige **97.217**); IVA 22.128; FVA **1.324**; current **1.229.421**; voorraden **19.412**; ST recv **340.967** (trade 336.153); geldbeleggingen **550.000 DROP** vs 1.050.000; cash **305.842**; prepaid 13.200; equity **5.334.842** (inbreng 2.620.746 onbeschikbaar; reserves 987.246; capsub **1.726.850**); voorzieningen empty; schulden **5.591.135** (LT bank **4.393.056**; ST **1.132.454** waarvan LT-due **511.538** + overige leningen 22.561 + leveranciers **487.485 JUMP** vs 97.671 + tax 19.244 + soc 91.626; gov-guaranteed **4.904.594**; debt 1-5y 2.291.295 / >5y 2.101.761; provincie waarborg **9.000.000** off-balance); brutomarge **1.750.457** vs 1.947.496; omzet 70 empty; 60/61 empty; pers **1.006.636** / **12 VTE** / 20.397 uur / YE 12 (8 VT + 5 DT; 10 onbepaald + 2 bepaald); afschr 590.538; expl **+144.115** vs +447.058; fin opbr 125.237 (capsub 101.573); fin kosten 241.220; tax empty; PnL **+28.132** vs +275.305 all to reserves; dividend **0** (694 empty); capex MVA aanschaf **871.895** + IVA 21.974; commissaris 6.988; bestuurders presentiegeld **42.019,20**. Vennoten: 28 gemeenten arrondissement Leuven + provincie Vlaams-Brabant (hofheide.be; named list unpublished).\n"
            "- CSVs: sources+4/entities+1/budgets+56/commitments+1/leaderboard+1 + FOI ready `gap_hofh_omzet_empty_debt_5_59m_machines_1_06m_l5` (not sent); rq_1395=done; spawn rq_1396; ticks=1395.\n"
            "- Coverage: residual dual L5 (IGS Hofheide leftover crematorium IGS live WVV). Does **not** move L5 near-complete of EUR 347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs gemeente funeral fees possible. No progress refresh (not every-10; next 1400).\n"
            "- Next: rq_1396 residual dual L5 VL JR2025 hole_fill (prefer leftover IGS Pontes Wilrijk/Turnhout/Lommel if a 2025 PDF downloads; leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover Nuhma daughters Otary RS only after leftover IGS/EVA/AGB; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / ILvA 1344 / Haviland 1370).\n"
        )
        with log.open("a", encoding="utf-8") as f:
            f.write(entry)
        print("loop_log ok")
    print("tick1395 write", step, "done")


if __name__ == "__main__":
    main()

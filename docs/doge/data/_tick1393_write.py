# -*- coding: utf-8 -*-
"""Tick 1393 — leftover HAVICREM JR2025 official NBB WVV euros.
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

TICK = "1393"
UTC = "2026-08-19T04:10:00Z"
ENT = "igs_havicrem"
HIER = "Vlaanderen>VlaamsBrabant>IGS>HAVICREM"
GAP = "gap_hvic_diensten_empty_debt_6_00m_invest_3_66m_l5"
SRC = "src_hvic_jr2025_nbb"
SRC2 = "src_hvic_site"
SRC3 = "src_kbo_hvic_0860572419"
SRC4 = "src_hvic_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00363711.pdf"
SRC2_URL = "https://www.havicrem.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0860572419"
SRC4_URL = "https://www.havicrem.be/contact"
FOI_EMAIL = "info@havicrem.be"
FOI_POSTAL = "Erasmuslaan 50 1804 Cargovil-Eppegem (Zemst)"
DRAFT = "docs/doge/foi/drafts/gap_hvic_diensten_empty_debt_6_00m_invest_3_66m_l5.md"
COMM = "comm_hvic_jr2025_pnl"
LB = "lb_hvic_diensten_empty_debt_6_00m_invest_3_66m"

VENNOTEN = (
    "Affligem + Asse + Beersel + Dilbeek + Grimbergen + Hoeilaart + "
    "Kampenhout + Kapelle-op-den-Bos + Lennik + Liedekerke + Londerzeel + "
    "Machelen + Meise + Merchtem + Opwijk + Pajottegem + Pepingen + "
    "Roosdaal + Sint-Pieters-Leeuw + Steenokkerzeel + Ternat + Vilvoorde + "
    "Wemmel + Zaventem + Zemst (25 gemeenten; founded 10.06.2003 + provincie Vlaams-Brabant)"
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
    ("bud_hvic_assets_2025", "2025", "12748564", "2025 assets 12748564 VKT-inb 20/58; tick1393; primary official NBB WVV"),
    ("bud_hvic_assets_2024", "2024", "12545697", "2024 assets 12545697 comparative; tick1393; primary official NBB WVV 20/58"),
    ("bud_hvic_fixed_2025", "2025", "8238201", "2025 vaste activa 8238201 vs 8062760; tick1393; primary official NBB WVV 21/28"),
    ("bud_hvic_iva_2025", "2025", "17354", "2025 IVA 17354 vs 24237; tick1393; primary official NBB WVV 21"),
    ("bud_hvic_mva_2025", "2025", "8220290", "2025 MVA 8220290 vs 8037965; tick1393; primary official NBB WVV 22/27"),
    ("bud_hvic_buildings_2025", "2025", "7820353", "2025 terreinen/gebouwen 7820353 vs 7629623; tick1393; primary official NBB WVV 22"),
    ("bud_hvic_machines_2025", "2025", "338870", "2025 machines 338870 vs 267573; tick1393; primary official NBB WVV 23"),
    ("bud_hvic_furniture_2025", "2025", "13806", "2025 meubilair 13806 vs 17037; tick1393; primary official NBB WVV 24"),
    ("bud_hvic_othmva_2025", "2025", "37895", "2025 overige MVA 37895 vs 37997; tick1393; primary official NBB WVV 26"),
    ("bud_hvic_cip_2025", "2025", "9366", "2025 CIP 9366 vs 85736; tick1393; primary official NBB WVV 27"),
    ("bud_hvic_fva_2025", "2025", "558", "2025 FVA 558 vs 558; tick1393; primary official NBB WVV 28"),
    ("bud_hvic_current_2025", "2025", "4510363", "2025 vlottend 4510363 vs 4482937; tick1393; primary official NBB WVV 29/58"),
    ("bud_hvic_stocks_2025", "2025", "45199", "2025 voorraden 45199 vs 52428; tick1393; primary official NBB WVV 30/36"),
    ("bud_hvic_strecv_2025", "2025", "337603", "2025 ST vorderingen 337603 vs 262299; tick1393; primary official NBB WVV 40/41"),
    ("bud_hvic_trade_2025", "2025", "335679", "2025 handelsvorderingen 335679 vs 259262; tick1393; primary official NBB WVV 40"),
    ("bud_hvic_invest_2025", "2025", "3657007", "2025 geldbeleggingen 3657007 unchanged vs 3657007; tick1393; primary official NBB WVV 50/53"),
    ("bud_hvic_invest_2024", "2024", "3657007", "2024 geldbeleggingen 3657007 comparative; tick1393; primary official NBB WVV 50/53"),
    ("bud_hvic_cash_2025", "2025", "293656", "2025 liquide middelen 293656 DROP vs 380864; tick1393; primary official NBB WVV 54/58"),
    ("bud_hvic_cash_2024", "2024", "380864", "2024 liquide middelen 380864 comparative; tick1393; primary official NBB WVV 54/58"),
    ("bud_hvic_prepaid_2025", "2025", "176898", "2025 overlopend actief 176898 vs 130338; tick1393; primary official NBB WVV 490/1"),
    ("bud_hvic_equity_2025", "2025", "6748935", "2025 EV 6748935 vs 5934509; tick1393; primary official NBB WVV 10/15"),
    ("bud_hvic_inbreng_2025", "2025", "220570", "2025 inbreng 220570 onbeschikbaar; tick1393; primary official NBB WVV 10/11"),
    ("bud_hvic_reserves_2025", "2025", "5419396", "2025 beschikbare reserves 5419396 vs 4534960; tick1393; primary official NBB WVV 133"),
    ("bud_hvic_capsub_2025", "2025", "1108970", "2025 kapitaalsubsidies 1108970 vs 1178979; tick1393; primary official NBB WVV 15"),
    ("bud_hvic_debt_2025", "2025", "5999629", "2025 schulden 5999629 vs 6611187; tick1393; primary official NBB WVV 17/49"),
    ("bud_hvic_debt_2024", "2024", "6611187", "2024 schulden 6611187 comparative; tick1393; primary official NBB WVV 17/49"),
    ("bud_hvic_lt_2025", "2025", "4886178", "2025 LT bank 4886178 vs 5410691; tick1393; primary official NBB WVV 17"),
    ("bud_hvic_st_2025", "2025", "1049657", "2025 ST schulden 1049657 vs 1130336; tick1393; primary official NBB WVV 42/48"),
    ("bud_hvic_ltdue_2025", "2025", "524512", "2025 LT-due binnen jaar 524512 vs 505442; tick1393; primary official NBB WVV 42"),
    ("bud_hvic_sttrade_2025", "2025", "282010", "2025 leveranciers 282010 vs 235718; tick1393; primary official NBB WVV 440/4"),
    ("bud_hvic_sttax_2025", "2025", "64798", "2025 belastingschulden 64798 vs 54806; tick1393; primary official NBB WVV 450/3"),
    ("bud_hvic_stsoc_2025", "2025", "177203", "2025 bezoldigingen/sociale lasten 177203 vs 301583; tick1393; primary official NBB WVV 454/9"),
    ("bud_hvic_guaranteed_2025", "2025", "5410691", "2025 overheidswaarborg bank 5410691; tick1393; primary official NBB WVV 6.3 9061"),
    ("bud_hvic_brutomarge_2025", "2025", "2986517", "2025 brutomarge 2986517 vs 2370163; tick1393; primary official NBB WVV 9900"),
    ("bud_hvic_omzet_2025", "2025", "3947173", "2025 omzet 3947173 vs 3415199; category unpublished; tick1393; primary official NBB WVV 70"),
    ("bud_hvic_omzet_2024", "2024", "3415199", "2024 omzet 3415199 comparative; tick1393; primary official NBB WVV 70"),
    ("bud_hvic_goods_diensten_2025", "2025", "1045780", "2025 60/61 combined 1045780 vs 1118382; diensten unpublished as split; tick1393; primary official NBB WVV 60/61"),
    ("bud_hvic_goods_diensten_2024", "2024", "1118382", "2024 60/61 combined 1118382 comparative; tick1393; primary official NBB WVV 60/61"),
    ("bud_hvic_pers_2025", "2025", "1504276", "2025 pers 1504276 vs 1671339 / 18.8 VTE; tick1393; primary official NBB WVV 62"),
    ("bud_hvic_pers_2024", "2024", "1671339", "2024 pers 1671339 / 16.7 VTE comparative; tick1393; primary official NBB WVV 62"),
    ("bud_hvic_afschr_2025", "2025", "453696", "2025 afschr 453696 vs 870522; tick1393; primary official NBB WVV 630"),
    ("bud_hvic_othcost_2025", "2025", "18679", "2025 andere bedrijfskosten 18679 vs 18219; tick1393; primary official NBB WVV 640/8"),
    ("bud_hvic_nrec_2025", "2025", "18621", "2025 niet-recurrente bedrijfskosten 18621 vs 514; tick1393; primary official NBB WVV 66A"),
    ("bud_hvic_expl_2025", "2025", "991244", "2025 expl +991244 vs +712004; tick1393; primary official NBB WVV 9901"),
    ("bud_hvic_expl_2024", "2024", "712004", "2024 expl +712004 comparative; tick1393; primary official NBB WVV 9901"),
    ("bud_hvic_fininc_2025", "2025", "115248", "2025 financiele opbrengsten 115248 vs 254057 (capsub 70010); tick1393; primary official NBB WVV 75"),
    ("bud_hvic_fincost_2025", "2025", "222057", "2025 financiele kosten 222057 vs 249023; tick1393; primary official NBB WVV 65"),
    ("bud_hvic_pnl_2025", "2025", "884436", "2025 PnL +884436 vs +717038 all to reserves; tick1393; primary official NBB WVV 9904"),
    ("bud_hvic_pnl_2024", "2024", "717038", "2024 PnL +717038 comparative; tick1393; primary official NBB WVV 9904"),
    ("bud_hvic_div_2025", "2025", "0", "2025 dividend 694 empty; tick1393; primary official NBB WVV 694"),
    ("bud_hvic_capex_2025", "2025", "733495", "2025 MVA aanschaf 733495; tick1393; primary official NBB WVV 8169"),
    ("bud_hvic_comm_2025", "2025", "11435", "2025 commissaris Moore Audit 11435; tick1393; primary official NBB WVV 6.6"),
    ("bud_hvic_board_2025", "2025", "32211", "2025 bestuurders presentiegeld 32211 + KM 2354; tick1393; primary official NBB WVV p37"),
]


def main() -> None:
    step = sys.argv[1] if len(sys.argv) > 1 else "all"

    if step in ("all", "sources"):
        n = append_rows(
            DATA / "sources.csv",
            [
                {
                    "source_id": SRC,
                    "title": "HAVICREM jaarrekening boekjaar 2025 (official NBB WVV VKT-inb deposit 2026-00363711; AV 24.06.2026)",
                    "url": SRC_URL,
                    "publisher": "HAVICREM / NBB WVV deposit",
                    "accessed_date": "2026-08-19",
                    "source_class": "budget",
                    "notes": (
                        "tick1393; official NBB VKT-inb PDF 788KB 37p deposit 2026-00363711 header 31.07.2026; "
                        "leftover IGS crematorium Halle-Vilvoorde Daelhof; "
                        "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                        "Belscope/Companyweb extracted tables not used; Staatsbladmonitor table euros not used; "
                        "commissaris Moore Audit BV B00212 / 0453.925.059 / Carmen Van Camp A02365 fee 11435; "
                        "omzet 70 published; 60/61 combined; 6.6 related empty; jaarverslag p23-26 + commissarisverslag p28-33 image-only this extract"
                    ),
                },
                {
                    "source_id": SRC2,
                    "title": "HAVICREM official site (leftover crematorium IGS Halle-Vilvoorde; Daelhof Zemst; 25 vennoten)",
                    "url": SRC2_URL,
                    "publisher": "HAVICREM",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1393; leftover crematorium IGS of 25 Halle-Vilvoorde municipalities; "
                        "founded 10.06.2003 Vilvoorde by 26 gemeenten + provincie Vlaams-Brabant; "
                        "baat crematorium Daelhof Eppegem (Zemst); statutory 2025 balans is the NBB CDN deposit"
                    ),
                },
                {
                    "source_id": SRC3,
                    "title": "KBO HAVICREM 0860.572.419",
                    "url": SRC3_URL,
                    "publisher": "KBO Public Search FOD Economie",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1393; KBO 0860.572.419 Actief / normale toestand since 18.09.2003; "
                        "statutaire naam INTERGEMEENTELIJKE VERENIGING VOOR CREMATORIUMBEHEER IN HET ARRONDISSEMENT HALLE-VILVOORDE since 18.09.2003; "
                        "Opdrachthoudende vereniging (Vlaams Gewest) since 19.09.2003; "
                        "zetel Erasmuslaan 50 1804 Zemst since 01.01.2018; 1 VE; "
                        "no KBO email/web/tel; btw since 01.11.2003; RSZ since 01.01.2022; NACE 96.302; "
                        "aanbestedende overheid since 18.09.2003; KBO kapitaal 50000; dagelijks bestuur Bert Carleer"
                    ),
                },
                {
                    "source_id": SRC4,
                    "title": "HAVICREM FOI channel / official contact (info@havicrem.be; 02/251.30.30)",
                    "url": SRC4_URL,
                    "publisher": "HAVICREM",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1393; KBO no email/web/tel; site contact info@havicrem.be; "
                        "operational Erasmuslaan 50 1804 Cargovil (Zemst); tel 02/251.30.30"
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
                    "name_nl": "HAVICREM (Intergemeentelijke Vereniging voor Crematoriumbeheer in het Arrondissement Halle-Vilvoorde; leftover IGS crematorium Daelhof)",
                    "name_fr": "HAVICREM (association missionnee crematorium Halle-Vilvoorde; IGS residuel)",
                    "name_en": "HAVICREM leftover IGS crematorium Halle-Vilvoorde Daelhof",
                    "level": "other",
                    "parent_id": "sec_flanders",
                    "community_language": "nl",
                    "website": "https://www.havicrem.be/",
                    "foi_email": FOI_EMAIL,
                    "foi_postal": FOI_POSTAL,
                    "notes": (
                        "tick1393 leftover residual HAVICREM crematorium IGS; "
                        "KBO 0860.572.419 Actief since 18.09.2003; official NBB WVV VKT-inb PDF downloads; "
                        "sourced euros assets 12748564 omzet 3947173 60/61 combined 1045780 pers 1504276 debt 5999629 pnl 884436 equity 6748935 capex 733495 invest 3657007; "
                        "FOI ready 60-61 empty-split / 6.00m debt / 3.66m invest; "
                        "distinct from already-mined Haviland 1370 prefix havi and IVLA 1392 / Fluvius stack 1382-1391"
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
                    "title": "HAVICREM JR2025 leftover IGS dual (assets 12.75m / omzet 3.95m / 60-61 combined / debt 6.00m / invest 3.66m / PnL +884k)",
                    "entity_id": ENT,
                    "beneficiary": "HAVICREM / " + VENNOTEN,
                    "legal_basis": "WVV OV; Decreet Lokaal Bestuur; NBB neerlegging",
                    "decision_date": "2026-06-24",
                    "start_year": "2003",
                    "end_year": "",
                    "total_envelope_eur": "5999629",
                    "cash_by_year": "",
                    "remaining_eur": "",
                    "status": "active",
                    "evaluation_url": SRC_URL,
                    "stated_goal": "Local leftover IGS map VL crematorium HV — 60/61 combined (diensten unpublished) / 6.00m gov-guaranteed bank / 3.66m investments / PnL +884k",
                    "cut_option": "Publish 60/61 split + 6.00m bank counterparties/terms + 3.66m investment nature + 733k capex tender; do not keep crematorium IGS as dual unpublished vehicle",
                    "source_id": SRC,
                    "confidence": "strong",
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "notes": "tick1393; assets 12748564 omzet 3947173 60/61 1045780 pers 1504276 debt 5999629 pnl 884436 equity 6748935 capex 733495 invest 3657007; FOI ready not sent; not TE-additive of 348bn",
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
                    "name": "HAVICREM JR2025 leftover IGS: assets 12.75m / omzet 3.95m / 60-61 combined / debt 6.00m gov-guaranteed / invest 3.66m / 18.8 VTE",
                    "level": "L5",
                    "type": "local_budget_line",
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "annual_cost_eur": "1504276",
                    "total_cost_eur": "5999629",
                    "tco_notes": (
                        "Leftover dual IGS crematorium HV (25 Halle-Vilvoorde municipalities): "
                        "assets 12.75m / equity 6.75m / pnl +884k / omzet 3.95m / "
                        "60/61 combined 1.05m (diensten unpublished) / pers 1.50m / 18.8 VTE / "
                        "debt 6.00m gov-guaranteed / invest 3.66m unchanged / cash 0.29m DROP / capex 0.73m; "
                        "official NBB WVV live; do not treat 6.00m as TE-additive of 348bn"
                    ),
                    "confidence": "strong",
                    "source_id": SRC,
                    "beneficiaries": "HAVICREM / " + VENNOTEN,
                    "stated_goal": "Local leftover IGS map VL crematorium HV — JR2025 live; dual 60-61/debt/invest FOI",
                    "measured_outcome": "Official NBB WVV 2026-08-19: assets 12.75m / omzet 3.95m / 60-61 combined / debt 6.00m / invest 3.66m / pnl +884k / 18.8 VTE",
                    "absurdity_score": "6.5",
                    "cost_score": "5.0",
                    "difficulty": "3.0",
                    "priority_index": "5.7",
                    "cut_proposal": "Publish 60/61 split + 6.00m bank counterparties/terms + 3.66m investment nature + 733k capex tender; do not keep crematorium IGS as dual unpublished vehicle",
                    "status": "active",
                    "struck_reason": "",
                    "notes": "tick1393; leftover HAVICREM crematorium IGS; FOI ready not sent; not TE-additive of 348bn; distinct from Haviland 1370 and IVLA 1392 / Fluvius stack 1382-1391",
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
                        "60/61 combined 1045780 (abbreviated VKT; diensten unpublished as a split; omzet 70 published 3947173) per stroom/vennoot unpublished "
                        "+ schulden 5999629 vs 6611187 (LT bank 4886178 + ST due 524512; gov-guaranteed 5410691) counterparties/terms unpublished "
                        "+ geldbeleggingen 3657007 unchanged vs 2024 nature unpublished "
                        "+ MVA aanschaf 733495 (8169; machines 338870 vs 267573) tender/unit price unpublished "
                        "+ omzet category/geo unpublished (crematie/aula/catering/asverstrooiing) "
                        "+ pers 1504276 / 18.8 VTE / 26150 uur (cost DROP vs VTE JUMP) "
                        "+ 6.6 related empty + jaarverslag p23-26 image-only + commissarisverslag p28-33 image-only + dividend 694 empty"
                    ),
                    "why_it_matters": (
                        "Leftover IGS crematorium HV of 25 mined Halle-Vilvoorde municipalities "
                        "(distinct from Haviland 1370 and from IVLA 1392 / Fluvius 1382-1391): "
                        "12.75m assets / 3.95m omzet / 60-61 combined / 6.00m gov-guaranteed debt / 3.66m investments / "
                        "abbreviated VKT hides 60 vs 61 "
                        "is a dual opacity residual, not TE-additive of 348bn."
                    ),
                    "priority": "8",
                    "recipient_body": "HAVICREM / Raad van Bestuur / Kirsten Hoefs / Jan Anciaux / Bert Carleer / 25 vennoten",
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
                        "tick1393 leftover IGS crematorium HV of 25 Halle-Vilvoorde municipalities after honest hunt; "
                        "live JR2025 official NBB WVV VKT-inb PDF now extracted (788KB 37p deposit 2026-00363711). "
                        "IVLA already mined 1392 — skipped. Fluvius OV already mined 1391 — skipped. Nine DNB holdings already mined 1382-1390 — skipped. "
                        "Haviland already mined 1370 — skipped. Dommelhof leftover next if a JR2025 PDF now downloads. "
                        "Otary RS Nuhma-adjacent fallback not taken. "
                        "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                    ),
                }
            ],
        )
        print("foi", n)

    if step in ("all", "rq"):
        rq_new = {
            "task_id": "rq_1393",
            "title": "HAVICREM JR2025 leftover dual residual",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "done",
            "hierarchy_target": "L5",
            "entity_id": ENT,
            "instructions": (
                "Completed: HAVICREM leftover IGS crematorium HV of 25 Halle-Vilvoorde municipalities after honest hunt; "
                "KBO 0860.572.419 Actief; live JR2025 official NBB WVV VKT-inb PDF (788KB 37p deposit 2026-00363711; commissaris Moore Audit); "
                "sourced euros assets 12748564 / omzet 3947173 / 60-61 combined 1045780 / pers 1504276 / debt 5999629 / pnl 884436 / capex 733495 / invest 3657007; "
                "FOI ready 60-61 empty-split / 6.00m debt / 3.66m invest"
            ),
            "blocked_gap_id": GAP,
            "created_utc": "2026-08-19T03:50:00Z",
            "updated_utc": UTC,
            "notes": (
                "tick1393 HAVICREM leftover IGS crematorium residual; KBO 0860.572.419; "
                "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1394 residual dual L5 VL"
            ),
        }
        rq_spawn = {
            "task_id": "rq_1394",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
                "(prior 1255-1393 done including HAVICREM 1393 leftover crematorium IGS live NBB WVV / "
                "IVLA 1392 leftover waste IGS live NBB WVV / "
                "Fluvius OV 1391 leftover personnel OV live NBB WVV / "
                "Fluvius Riobra 1390 leftover sewerage IGS live NBB WVV + every-10 / "
                "Fluvius Zenne-Dijle 1389 leftover energy IGS live NBB WVV / "
                "Fluvius Limburg 1388 leftover energy IGS live NBB WVV / "
                "Fluvius Halle-Vilvoorde 1387 leftover energy IGS live NBB WVV / "
                "Fluvius Antwerpen 1386 leftover energy IGS live NBB WVV / "
                "Fluvius West 1385 leftover energy IGS live NBB WVV / "
                "Fluvius Kempen 1384 leftover energy IGS live NBB WVV / "
                "Fluvius Imewo 1383 leftover energy IGS live NBB WVV / "
                "INTERGEM / Fluvius Midden-Vlaanderen 1382 leftover energy IGS live NBB WVV); "
                "leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; "
                "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
                "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
                "skip already-mined HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / ILvA 1344; "
                "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
                "ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick1393 after HAVICREM leftover crematorium IGS live NBB WVV; next residual dual L5 VL",
        }
        found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1393", rq_new, rq_spawn)
        print("research_queue 1393", found, "spawned_1394", spawned)

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
                    "last_unit_id": "rq_1393",
                    "ticks_completed": "1393",
                    "paused": "no",
                    "notes": (
                        "tick1393 HAVICREM leftover IGS crematorium residual; KBO 0860.572.419; "
                        "live JR2025 NBB WVV PDF; sourced euros assets 12748564 omzet 3947173 60/61 1045780 pers 1504276 debt 5999629 pnl 884436 equity 6748935 capex 733495 invest 3657007; "
                        "FOI ready 60-61 empty-split/6.00m debt/3.66m invest; next rq_1394 residual dual L5 VL; continuous hole_fill"
                    ),
                }
            )
        print("loop_state ok")

    if step in ("all", "log"):
        log = ROOT / "loop_log.md"
        entry = (
            "### Tick 1393 - 2026-08-19 - rq_1393 HAVICREM dual residual leftover\n"
            "- Unit: HAVICREM / Intergemeentelijke Vereniging voor Crematoriumbeheer in het Arrondissement Halle-Vilvoorde (leftover IGS opdrachthoudende vereniging / crematorium Daelhof of 25 mined Halle-Vilvoorde municipalities) after residual dual hunt (KBO **0860.572.419**; official havicrem.be has opdracht/werkingsgebied + contact; live NBB WVV VKT-inb deposit **2026-00363711** PDF 788KB / 37p; AV **24.06.2026**; header **31.07.2026**; commissaris Moore Audit BV B00212 / 0453.925.059 / Carmen Van Camp A02365 mandate 25.06.2025-28.06.2028 fee 11.435). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; preferred leftover IGS with live CDN this tick). Distinct from already-mined Haviland 1370 (prefix `havi`) and from IVLA 1392 / Fluvius stack 1382-1391. First confirmed not already mined: no HAVICREM / 0860.572.419 JR2025 extract in entities/sources/leaderboard (only leftover-next mentions in queues). KBO Actief / normale toestand since **18.09.2003**; statutaire naam INTERGEMEENTELIJKE VERENIGING VOOR CREMATORIUMBEHEER IN HET ARRONDISSEMENT HALLE-VILVOORDE since 18.09.2003; Opdrachthoudende vereniging (Vlaams Gewest) since 19.09.2003; zetel Erasmuslaan 50 1804 Zemst since 01.01.2018; **1 VE**; KBO no email/web/tel; official site https://www.havicrem.be/; btw since 01.11.2003; RSZ since 01.01.2022; NACE 96.302; KBO kapitaal 50.000. Voorzitter Kirsten Hoefs since 18.03.2025; ondervoorzitter Jan Anciaux since 18.03.2025; directeur/dagelijks bestuur Bert Carleer. Contact info@havicrem.be; tel 02/251.30.30. Hunt leftover IGS with live CDN first: HAVICREM statutory CDN live this tick (HTTP 200 / 788141 / 37p) — taken. IVLA already mined 1392 — skipped. Fluvius OV already mined 1391 — skipped. Nine Fluvius DNB holdings already mined 1382-1390 — skipped. Haviland already mined 1370 — skipped. Leftover AGB/zorg/EVA/APB not taken once live HAVICREM extracted. Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live HAVICREM extracted. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. NBB consult skipped (403/SPA); euros extracted from the official VKT-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used. Jaarverslag p23-26 + commissarisverslag p28-33 image-only this extract. Not every-10 (next 1400).\n"
            "- EUR strong (primary official WVV VKT-inb; omzet 70 published; 60/61 combined so diensten unpublished as a split; 6.2/6.5/6.7/7/8/9/13-16 not filed; 6.6 related empty): assets **12.748.564** (was 12.545.697); fixed **8.238.201** / MVA **8.220.290** (gebouwen **7.820.353**; machines **338.870**; meubilair **13.806**; overige **37.895**; CIP **9.366**); IVA 17.354; FVA **558**; current **4.510.363**; voorraden **45.199**; ST recv **337.603** (trade 335.679); geldbeleggingen **3.657.007** unchanged; cash **293.656 DROP** vs 380.864; prepaid 176.898; equity **6.748.935** (inbreng 220.570; reserves 5.419.396; capsub **1.108.970**; lifetime capsub received 2.799.494 / 2025 in resultaat 70.010); voorzieningen empty; schulden **5.999.629** (LT bank **4.886.178**; ST **1.049.657** waarvan LT-due **524.512** + leveranciers **282.010** + tax 64.798 + soc 177.203; gov-guaranteed **5.410.691**; debt 1-5y 2.304.279 / >5y 2.581.900); brutomarge **2.986.517** vs 2.370.163; omzet **3.947.173** vs 3.415.199 (category unpublished); 60/61 **1.045.780** combined vs 1.118.382; pers **1.504.276** / **18,8 VTE** / 26.150 uur / YE 21,6 (19 VT + 4 DT; 10,8 in / 5 uit); afschr 453.696; expl **+991.244** vs +712.004; fin opbr 115.248; fin kosten 222.057; tax empty; PnL **+884.436** vs +717.038 all to reserves; dividend **0** (694 empty); capex aanschaf **733.495**; commissaris 11.435; bestuurders presentiegeld **32.211** + KM **2.354**. Vennoten: 25 Halle-Vilvoorde municipalities (site).\n"
            "- CSVs: sources+4/entities+1/budgets+53/commitments+1/leaderboard+1 + FOI ready `gap_hvic_diensten_empty_debt_6_00m_invest_3_66m_l5` (not sent); rq_1393=done; spawn rq_1394; ticks=1393.\n"
            "- Coverage: residual dual L5 (HAVICREM leftover crematorium IGS live WVV). Does **not** move L5 near-complete of EUR 347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs gemeente funeral fees possible. No progress refresh (not every-10; next 1400).\n"
            "- Next: rq_1394 residual dual L5 VL JR2025 hole_fill (prefer leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover Nuhma daughters Otary RS only after leftover IGS/EVA/AGB; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / ILvA 1344 / Haviland 1370).\n"
        )
        with log.open("a", encoding="utf-8") as f:
            f.write(entry)
        print("loop_log ok")
    print("tick1393 write", step, "done")


if __name__ == "__main__":
    main()

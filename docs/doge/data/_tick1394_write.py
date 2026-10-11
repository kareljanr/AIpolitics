# -*- coding: utf-8 -*-
"""Tick 1394 — leftover IGS Westlede JR2025 official NBB WVV euros.
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

TICK = "1394"
UTC = "2026-08-19T04:25:00Z"
ENT = "igs_wstl"
HIER = "Vlaanderen>OostVlaanderen>IGS>Westlede"
GAP = "gap_wstl_omzet_cat_empty_debt_5_72m_pens_3_60m_l5"
SRC = "src_wstl_jr2025_nbb"
SRC2 = "src_wstl_site"
SRC3 = "src_kbo_wstl_0219805958"
SRC4 = "src_wstl_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00190076.pdf"
SRC2_URL = "https://westlede.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0219805958"
SRC4_URL = "https://westlede.be/contact/"
FOI_EMAIL = "crematoriumwestlede@westlede.be"
FOI_POSTAL = "Smalle Heerweg 60 9080 Lochristi"
DRAFT = "docs/doge/foi/drafts/gap_wstl_omzet_cat_empty_debt_5_72m_pens_3_60m_l5.md"
COMM = "comm_wstl_jr2025_pnl"
LB = "lb_wstl_omzet_9_75m_diensten_1_54m_debt_5_72m_pens_3_60m"

VENNOTEN = (
    "Aalst + Aalter + Assenede + Beveren-Kruibeke-Zwijndrecht + Brakel + "
    "Deinze + Denderleeuw + Dendermonde + Destelbergen + Eeklo + Erpe-Mere + "
    "Evergem + Gavere + Gent + Geraardsbergen + Haaltert + Hamme + Herzele + "
    "Kaprijke + Kluisbergen + Kruisem + Laarne + Lede + Lierde + Lievegem + "
    "Lochristi + Lokeren + Maarkedal + Merelbeke-Melle + Nazareth-De Pinte + "
    "Ninove + Oosterzele + Oudenaarde + Ronse + Sint-Gillis-Waas + Sint-Laureins + "
    "Sint-Martens-Latem + Sint-Niklaas + Stekene + Temse + Waasmunster + Wetteren + "
    "Wichelen + Zelzate + Zottegem + Zulte + Zwalm "
    "(47 van 55 Oost-Vlaamse gemeenten; 1240 aandelen / inbreng 3073017)"
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
    ("bud_wstl_assets_2025", "2025", "27806916", "2025 assets 27806916 VOL-inb 20/58; tick1394; primary official NBB WVV"),
    ("bud_wstl_assets_2024", "2024", "25511956", "2024 assets 25511956 comparative; tick1394; primary official NBB WVV 20/58"),
    ("bud_wstl_fixed_2025", "2025", "23357476", "2025 vaste activa 23357476 vs 21779464; tick1394; primary official NBB WVV 21/28"),
    ("bud_wstl_mva_2025", "2025", "23243632", "2025 MVA 23243632 vs 21665620; tick1394; primary official NBB WVV 22/27"),
    ("bud_wstl_buildings_2025", "2025", "16075598", "2025 terreinen/gebouwen 16075598 vs 16349711; tick1394; primary official NBB WVV 22"),
    ("bud_wstl_machines_2025", "2025", "5509744", "2025 machines 5509744 JUMP vs 3248284; tick1394; primary official NBB WVV 23"),
    ("bud_wstl_furniture_2025", "2025", "1077135", "2025 meubilair 1077135 vs 719977; tick1394; primary official NBB WVV 24"),
    ("bud_wstl_othmva_2025", "2025", "431751", "2025 overige MVA 431751 vs 402037; tick1394; primary official NBB WVV 26"),
    ("bud_wstl_cip_2025", "2025", "149405", "2025 CIP 149405 vs 945612; tick1394; primary official NBB WVV 27"),
    ("bud_wstl_fva_2025", "2025", "113844", "2025 FVA 113844 vs 113844; deelnemingen 103170 counterpart unpublished; tick1394; primary official NBB WVV 28"),
    ("bud_wstl_current_2025", "2025", "4449440", "2025 vlottend 4449440 vs 3732493; tick1394; primary official NBB WVV 29/58"),
    ("bud_wstl_stocks_2025", "2025", "238622", "2025 voorraden 238622 vs 239121; tick1394; primary official NBB WVV 30/36"),
    ("bud_wstl_strecv_2025", "2025", "527964", "2025 ST vorderingen 527964 vs 493031; tick1394; primary official NBB WVV 40/41"),
    ("bud_wstl_trade_2025", "2025", "491049", "2025 handelsvorderingen 491049 vs 462653; tick1394; primary official NBB WVV 40"),
    ("bud_wstl_invest_2025", "2025", "7412", "2025 geldbeleggingen 7412 vs 7301 termijnrekening; tick1394; primary official NBB WVV 50/53"),
    ("bud_wstl_cash_2025", "2025", "3534945", "2025 liquide middelen 3534945 vs 2818359; tick1394; primary official NBB WVV 54/58"),
    ("bud_wstl_cash_2024", "2024", "2818359", "2024 liquide middelen 2818359 comparative; tick1394; primary official NBB WVV 54/58"),
    ("bud_wstl_prepaid_2025", "2025", "140497", "2025 overlopend actief 140497 vs 174680; tick1394; primary official NBB WVV 490/1"),
    ("bud_wstl_equity_2025", "2025", "18485561", "2025 EV 18485561 vs 18196573; tick1394; primary official NBB WVV 10/15"),
    ("bud_wstl_inbreng_2025", "2025", "3073017", "2025 inbreng 3073017 beschikbaar / 1240 aandelen; tick1394; primary official NBB WVV 10/11"),
    ("bud_wstl_reserves_2025", "2025", "12199146", "2025 reserves 12199146 vs 11699259; tick1394; primary official NBB WVV 13"),
    ("bud_wstl_capsub_2025", "2025", "3213398", "2025 kapitaalsubsidies 3213398 vs 3424297; tick1394; primary official NBB WVV 15"),
    ("bud_wstl_pens_prov_2025", "2025", "3600000", "2025 voorziening pensioenen 3600000 unchanged; tick1394; primary official NBB WVV 160"),
    ("bud_wstl_debt_2025", "2025", "5721355", "2025 schulden 5721355 vs 3715383; tick1394; primary official NBB WVV 17/49"),
    ("bud_wstl_debt_2024", "2024", "3715383", "2024 schulden 3715383 comparative; tick1394; primary official NBB WVV 17/49"),
    ("bud_wstl_lt_2025", "2025", "3732750", "2025 LT 3732750 vs 2604889 (bank 3600000 + overige 132750); tick1394; primary official NBB WVV 17"),
    ("bud_wstl_st_2025", "2025", "1973321", "2025 ST schulden 1973321 vs 1102137; tick1394; primary official NBB WVV 42/48"),
    ("bud_wstl_ltdue_2025", "2025", "444250", "2025 LT-due binnen jaar 444250 (bank 400000 + overige 44250); tick1394; primary official NBB WVV 42"),
    ("bud_wstl_sttrade_2025", "2025", "598377", "2025 leveranciers 598377 vs 211011; tick1394; primary official NBB WVV 440/4"),
    ("bud_wstl_sttax_2025", "2025", "95644", "2025 belastingschulden 95644 vs 92940; tick1394; primary official NBB WVV 450/3"),
    ("bud_wstl_stsoc_2025", "2025", "627066", "2025 bezoldigingen/sociale lasten 627066 vs 614358; tick1394; primary official NBB WVV 454/9"),
    ("bud_wstl_opbr_2025", "2025", "10024896", "2025 bedrijfsopbrengsten 10024896 vs 9520524; tick1394; primary official NBB WVV 70/76A"),
    ("bud_wstl_omzet_2025", "2025", "9745034", "2025 omzet 9745034 vs 9339054; category unpublished 6.10; tick1394; primary official NBB WVV 70"),
    ("bud_wstl_omzet_2024", "2024", "9339054", "2024 omzet 9339054 comparative; tick1394; primary official NBB WVV 70"),
    ("bud_wstl_goods_2025", "2025", "1092430", "2025 handelsgoederen 1092430 vs 1036913; tick1394; primary official NBB WVV 60"),
    ("bud_wstl_diensten_2025", "2025", "1542035", "2025 diensten 1542035 vs 1620918; tick1394; primary official NBB WVV 61"),
    ("bud_wstl_diensten_2024", "2024", "1620918", "2024 diensten 1620918 comparative; tick1394; primary official NBB WVV 61"),
    ("bud_wstl_pers_2025", "2025", "5188837", "2025 pers 5188837 vs 4967582 / 64.2 VTE; tick1394; primary official NBB WVV 62"),
    ("bud_wstl_pers_2024", "2024", "4967582", "2024 pers 4967582 / 63.1 VTE comparative; tick1394; primary official NBB WVV 62"),
    ("bud_wstl_afschr_2025", "2025", "1628102", "2025 afschr 1628102 vs 1323989; tick1394; primary official NBB WVV 630"),
    ("bud_wstl_othcost_2025", "2025", "12975", "2025 andere bedrijfskosten 12975 vs 24304; tick1394; primary official NBB WVV 640/8"),
    ("bud_wstl_nrec_2025", "2025", "202374", "2025 niet-recurrente bedrijfskosten 202374 vs 239392; tick1394; primary official NBB WVV 66A"),
    ("bud_wstl_expl_2025", "2025", "358143", "2025 expl +358143 vs -392574; tick1394; primary official NBB WVV 9901"),
    ("bud_wstl_expl_2024", "2024", "-392574", "2024 expl -392574 comparative; tick1394; primary official NBB WVV 9901"),
    ("bud_wstl_fininc_2025", "2025", "244454", "2025 financiele opbrengsten 244454 vs 265147 (capsub 210899); tick1394; primary official NBB WVV 75"),
    ("bud_wstl_fincost_2025", "2025", "102710", "2025 financiele kosten 102710 vs 62695; tick1394; primary official NBB WVV 65"),
    ("bud_wstl_pnl_2025", "2025", "499887", "2025 PnL +499887 vs -190121 all to reserves; tick1394; primary official NBB WVV 9904"),
    ("bud_wstl_pnl_2024", "2024", "-190121", "2024 PnL -190121 comparative; tick1394; primary official NBB WVV 9904"),
    ("bud_wstl_div_2025", "2025", "0", "2025 dividend 694 empty; tick1394; primary official NBB WVV 694"),
    ("bud_wstl_capex_2025", "2025", "3226690", "2025 MVA aanschaf 3226690 (8161+8162+8163+8165+8166); tick1394; primary official NBB WVV"),
    ("bud_wstl_comm_2025", "2025", "15000", "2025 commissaris KPMG 15000 + tax 7830; tick1394; primary official NBB WVV 6.16"),
    ("bud_wstl_board_2025", "2025", "38017", "2025 bestuurders 38017 / presentiegeld table 31295; tick1394; primary official NBB WVV 9503"),
    ("bud_wstl_uitzend_2025", "2025", "202007", "2025 uitzend 202007 / 3.7 VTE; tick1394; primary official NBB WVV 617"),
    ("bud_wstl_pens_cost_2025", "2025", "510658", "2025 ouderdoms/overlevingspensioenen 510658; tick1394; primary official NBB WVV 624"),
]


def main() -> None:
    step = sys.argv[1] if len(sys.argv) > 1 else "all"

    if step in ("all", "sources"):
        n = append_rows(
            DATA / "sources.csv",
            [
                {
                    "source_id": SRC,
                    "title": "IGS Westlede jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00190076; AV 16.06.2026)",
                    "url": SRC_URL,
                    "publisher": "IGS Westlede / NBB WVV deposit",
                    "accessed_date": "2026-08-19",
                    "source_class": "budget",
                    "notes": (
                        "tick1394; official NBB VOL-inb PDF 1.75MB 80p deposit 2026-00190076 header 22.06.2026; "
                        "leftover IGS crematorium Oost-Vlaanderen 3 vestigingen Lochristi/Aalst/Sint-Niklaas; "
                        "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                        "Belscope/Companyweb extracted tables not used; Staatsbladmonitor table euros not used; "
                        "commissaris KPMG Bedrijfsrevisoren BV B00001 / 0419.122.548 / Joachim Hoebeeck A02262 fee 15000; "
                        "omzet 70 published; 61 published; 6.10 category/geo empty; 6.15/6.16 related empty except 9503"
                    ),
                },
                {
                    "source_id": SRC2,
                    "title": "IGS Westlede official site (leftover crematorium IGS Oost-Vlaanderen; 3 vestigingen; 47 vennoten)",
                    "url": SRC2_URL,
                    "publisher": "IGS Westlede",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1394; leftover crematorium IGS of 47 Oost-Vlaanderen municipalities; "
                        "3 crematoria Lochristi / Aalst Siesegem / Sint-Niklaas Heimolen; "
                        "statutory 2025 balans is the NBB CDN deposit"
                    ),
                },
                {
                    "source_id": SRC3,
                    "title": "KBO IGS Westlede 0219.805.958",
                    "url": SRC3_URL,
                    "publisher": "KBO Public Search FOD Economie",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1394; KBO 0219.805.958 Actief / normale toestand since 17.09.1979; "
                        "statutaire naam INTERGEMEENTELIJKE SAMENWERKING WESTLEDE since 17.06.2014; "
                        "Opdrachthoudende vereniging (Vlaams Gewest) since 11.12.2002; "
                        "zetel Smalle Heerweg 60 9080 Lochristi since 01.01.2025; 3 VE; "
                        "no KBO email/web/tel; btw since 01.05.1985; RSZ since 01.01.2022; NACE 96.302; "
                        "aanbestedende overheid since 17.09.1979; KBO kapitaal 100000000 BEF; dagelijks bestuur Sven De Backer"
                    ),
                },
                {
                    "source_id": SRC4,
                    "title": "IGS Westlede FOI channel / official contact (crematoriumwestlede@westlede.be; 09 239 43 15)",
                    "url": SRC4_URL,
                    "publisher": "IGS Westlede",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1394; KBO no email/web/tel; site contact crematoriumwestlede@westlede.be; "
                        "deposit header sven.debacker@westlede.be; tel 09 239 43 15"
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
                    "name_nl": "IGS Westlede (Intergemeentelijke Samenwerking Westlede; leftover IGS crematorium Lochristi/Aalst/Sint-Niklaas)",
                    "name_fr": "IGS Westlede (association missionnee crematorium Flandre orientale; IGS residuel)",
                    "name_en": "IGS Westlede leftover IGS crematorium East Flanders 3 sites",
                    "level": "other",
                    "parent_id": "sec_flanders",
                    "community_language": "nl",
                    "website": "https://westlede.be/",
                    "foi_email": FOI_EMAIL,
                    "foi_postal": FOI_POSTAL,
                    "notes": (
                        "tick1394 leftover residual IGS Westlede crematorium IGS; "
                        "KBO 0219.805.958 Actief since 17.09.1979; official NBB WVV VOL-inb PDF downloads; "
                        "sourced euros assets 27806916 omzet 9745034 diensten 1542035 pers 5188837 debt 5721355 pnl 499887 equity 18485561 capex 3226690 pens 3600000; "
                        "FOI ready omzet-category empty / 5.72m debt / 3.60m pens / 3.23m capex; "
                        "distinct from already-mined HAVICREM 1393 prefix hvic and IVLA 1392 / Fluvius stack 1382-1391"
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
                    "title": "IGS Westlede JR2025 leftover IGS dual (assets 27.81m / omzet 9.75m / diensten 1.54m / debt 5.72m / pens 3.60m / PnL +500k)",
                    "entity_id": ENT,
                    "beneficiary": "IGS Westlede / " + VENNOTEN,
                    "legal_basis": "WVV OV; Decreet Lokaal Bestuur; NBB neerlegging",
                    "decision_date": "2026-06-16",
                    "start_year": "1979",
                    "end_year": "",
                    "total_envelope_eur": "5721355",
                    "cash_by_year": "",
                    "remaining_eur": "",
                    "status": "active",
                    "evaluation_url": SRC_URL,
                    "stated_goal": "Local leftover IGS map VL crematorium OVL — omzet category unpublished / 5.72m bank / 3.60m pension / 3.23m capex / PnL +500k",
                    "cut_option": "Publish omzet category + 5.72m bank counterparties/terms + 3.60m pension nature + 3.23m capex tender; do not keep crematorium IGS as dual unpublished vehicle",
                    "source_id": SRC,
                    "confidence": "strong",
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "notes": "tick1394; assets 27806916 omzet 9745034 diensten 1542035 pers 5188837 debt 5721355 pnl 499887 equity 18485561 capex 3226690 pens 3600000; FOI ready not sent; not TE-additive of 348bn",
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
                    "name": "IGS Westlede JR2025 leftover IGS: assets 27.81m / omzet 9.75m / diensten 1.54m / debt 5.72m / pens 3.60m / 64.2 VTE",
                    "level": "L5",
                    "type": "local_budget_line",
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "annual_cost_eur": "5188837",
                    "total_cost_eur": "5721355",
                    "tco_notes": (
                        "Leftover dual IGS crematorium OVL (47 Oost-Vlaanderen municipalities; 3 sites): "
                        "assets 27.81m / equity 18.49m / pnl +500k / omzet 9.75m category unpublished / "
                        "diensten 1.54m / pers 5.19m / 64.2 VTE / "
                        "debt 5.72m (LT bank 3.60m >5y) / pens 3.60m / cash 3.53m / capex 3.23m; "
                        "official NBB WVV live; do not treat 5.72m as TE-additive of 348bn"
                    ),
                    "confidence": "strong",
                    "source_id": SRC,
                    "beneficiaries": "IGS Westlede / " + VENNOTEN,
                    "stated_goal": "Local leftover IGS map VL crematorium OVL — JR2025 live; dual omzet-cat/debt/pens FOI",
                    "measured_outcome": "Official NBB WVV 2026-08-19: assets 27.81m / omzet 9.75m / diensten 1.54m / debt 5.72m / pens 3.60m / pnl +500k / 64.2 VTE / 12852 crematies",
                    "absurdity_score": "6.5",
                    "cost_score": "6.0",
                    "difficulty": "3.0",
                    "priority_index": "5.9",
                    "cut_proposal": "Publish omzet category + 5.72m bank counterparties/terms + 3.60m pension nature + 3.23m capex tender; do not keep crematorium IGS as dual unpublished vehicle",
                    "status": "active",
                    "struck_reason": "",
                    "notes": "tick1394; leftover IGS Westlede crematorium IGS; FOI ready not sent; not TE-additive of 348bn; distinct from HAVICREM 1393 and IVLA 1392 / Fluvius stack 1382-1391",
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
                        "omzet 9745034 published but 6.10 category/geo empty (crematie/aula/catering/asbestemming per vestiging/vennoot unpublished) "
                        "+ diensten 1542035 / goederen 1092430 top-20 suppliers unpublished "
                        "+ schulden 5721355 vs 3715383 (LT bank 3600000 >5y + ST due 444250; gov-guaranteed 9061 empty) counterparties/terms unpublished "
                        "+ voorziening pensioenen 3600000 + WVV 624 510658 nature unpublished "
                        "+ MVA aanschaf 3226690 (machines 2137946) tender/unit price unpublished "
                        "+ FVA deelnemingen 103170 counterpart unpublished "
                        "+ pers 5188837 / 64.2 VTE / 101250 uur (623 DROP 251086 vs 726222) "
                        "+ 6.15/6.16 related empty + dividend 694 empty"
                    ),
                    "why_it_matters": (
                        "Leftover IGS crematorium OVL of 47 mined Oost-Vlaanderen municipalities "
                        "(distinct from HAVICREM 1393 and from IVLA 1392 / Fluvius 1382-1391): "
                        "27.81m assets / 9.75m omzet / 1.54m diensten / 5.72m bank / 3.60m pension / 3.23m capex / "
                        "6.10 hides omzet category "
                        "is a dual opacity residual, not TE-additive of 348bn."
                    ),
                    "priority": "8",
                    "recipient_body": "IGS Westlede / Raad van Bestuur / Yves Deswaene / Burak Nalli / Sven De Backer / 47 vennoten",
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
                        "tick1394 leftover IGS crematorium OVL of 47 Oost-Vlaanderen municipalities after honest hunt; "
                        "live JR2025 official NBB WVV VOL-inb PDF now extracted (1.75MB 80p deposit 2026-00190076). "
                        "HAVICREM already mined 1393 — skipped. IVLA already mined 1392 — skipped. Fluvius stack already mined 1382-1391 — skipped. "
                        "Hofheide leftover next if still live. Dommelhof leftover next if a JR2025 PDF now downloads. "
                        "Otary RS Nuhma-adjacent fallback not taken. "
                        "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                    ),
                }
            ],
        )
        print("foi", n)

    if step in ("all", "rq"):
        rq_new = {
            "task_id": "rq_1394",
            "title": "IGS Westlede JR2025 leftover dual residual",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "done",
            "hierarchy_target": "L5",
            "entity_id": ENT,
            "instructions": (
                "Completed: IGS Westlede leftover IGS crematorium OVL of 47 Oost-Vlaanderen municipalities after honest hunt; "
                "KBO 0219.805.958 Actief; live JR2025 official NBB WVV VOL-inb PDF (1.75MB 80p deposit 2026-00190076; commissaris KPMG); "
                "sourced euros assets 27806916 / omzet 9745034 / diensten 1542035 / pers 5188837 / debt 5721355 / pnl 499887 / capex 3226690 / pens 3600000; "
                "FOI ready omzet-category empty / 5.72m debt / 3.60m pens / 3.23m capex"
            ),
            "blocked_gap_id": GAP,
            "created_utc": "2026-08-19T04:10:00Z",
            "updated_utc": UTC,
            "notes": (
                "tick1394 IGS Westlede leftover IGS crematorium residual; KBO 0219.805.958; "
                "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1395 residual dual L5 VL"
            ),
        }
        rq_spawn = {
            "task_id": "rq_1395",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
                "(prior 1255-1394 done including IGS Westlede 1394 leftover crematorium IGS live NBB WVV / "
                "HAVICREM 1393 leftover crematorium IGS live NBB WVV / "
                "IVLA 1392 leftover waste IGS live NBB WVV / "
                "Fluvius OV 1391 leftover personnel OV live NBB WVV / "
                "Fluvius Riobra 1390 leftover sewerage IGS live NBB WVV + every-10); "
                "leftover Hofheide KBO 0872.310.211 CDN 2026-00343763 live — take if still downloadable; "
                "leftover IGS Pontes (Wilrijk/Turnhout/Lommel) — take if a 2025 statutory PDF downloads; "
                "leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; "
                "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
                "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
                "skip already-mined IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / ILvA 1344; "
                "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
                "ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick1394 after IGS Westlede leftover crematorium IGS live NBB WVV; next residual dual L5 VL",
        }
        found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1394", rq_new, rq_spawn)
        print("research_queue 1394", found, "spawned_1395", spawned)

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
                    "last_unit_id": "rq_1394",
                    "ticks_completed": "1394",
                    "paused": "no",
                    "notes": (
                        "tick1394 IGS Westlede leftover IGS crematorium residual; KBO 0219.805.958; "
                        "live JR2025 NBB WVV PDF; sourced euros assets 27806916 omzet 9745034 diensten 1542035 pers 5188837 debt 5721355 pnl 499887 equity 18485561 capex 3226690 pens 3600000; "
                        "FOI ready omzet-category empty/5.72m debt/3.60m pens/3.23m capex; next rq_1395 residual dual L5 VL; continuous hole_fill"
                    ),
                }
            )
        print("loop_state ok")

    if step in ("all", "log"):
        log = ROOT / "loop_log.md"
        entry = (
            "### Tick 1394 - 2026-08-19 - rq_1394 IGS Westlede dual residual leftover\n"
            "- Unit: IGS Westlede / Intergemeentelijke Samenwerking Westlede (leftover IGS opdrachthoudende vereniging / crematorium of 47 mined Oost-Vlaanderen municipalities; 3 vestigingen Lochristi + Aalst Siesegem + Sint-Niklaas Heimolen) after residual dual hunt (KBO **0219.805.958**; official westlede.be has 3 locaties + contact; live NBB WVV VOL-inb deposit **2026-00190076** PDF 1.75MB / 80p; AV **16.06.2026**; header **22.06.2026**; commissaris KPMG Bedrijfsrevisoren BV B00001 / 0419.122.548 / Joachim Hoebeeck A02262 mandate 24.06.2025-30.06.2028 fee 15.000 + tax 7.830). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; preferred leftover IGS with live CDN this tick). Distinct from already-mined HAVICREM 1393 (prefix `hvic`) and from IVLA 1392 / Fluvius stack 1382-1391. First confirmed not already mined: no Westlede / 0219.805.958 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **17.09.1979**; statutaire naam INTERGEMEENTELIJKE SAMENWERKING WESTLEDE since 17.06.2014; Opdrachthoudende vereniging (Vlaams Gewest) since 11.12.2002; zetel Smalle Heerweg 60 9080 Lochristi since 01.01.2025; **3 VE**; KBO no email/web/tel; official site https://westlede.be/; btw since 01.05.1985; RSZ since 01.01.2022; NACE 96.302. Voorzitter Yves Deswaene since 18.03.2025; 1e ondervoorzitter Burak Nalli since 18.03.2025; dagelijks bestuur Sven De Backer since 01.04.2022. Contact crematoriumwestlede@westlede.be; deposit sven.debacker@westlede.be; tel 09 239 43 15. Hunt leftover IGS with live CDN first: Westlede statutory CDN live this tick (HTTP 200 / 1748785 / 80p) — taken. Hofheide leftover Leuven crematorium IGS KBO 0872.310.211 CDN 2026-00343763 also live — leftover next. HAVICREM already mined 1393 — skipped. IVLA already mined 1392 — skipped. Fluvius stack already mined 1382-1391 — skipped. Leftover AGB/zorg/EVA/APB not taken once live Westlede extracted. Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live Westlede extracted. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used. Not every-10 (next 1400).\n"
            "- EUR strong (primary official WVV VOL-inb; omzet 70 published; diensten 61 published; **6.10 omzet category/geo empty**; 6.1/6.2/6.8/6.14/9/12-14 not filed; 6.15/6.16 related empty except 9503): assets **27.806.916** (was 25.511.956); fixed **23.357.476** / MVA **23.243.632** (gebouwen **16.075.598**; machines **5.509.744 JUMP** vs 3.248.284; meubilair **1.077.135**; overige **431.751**; CIP **149.405**); FVA **113.844** (deelnemingen 103.170 counterpart unpublished); current **4.449.440**; voorraden **238.622**; ST recv **527.964** (trade 491.049); geldbeleggingen **7.412**; cash **3.534.945**; prepaid 140.497; equity **18.485.561** (inbreng 3.073.017 / 1.240 aandelen; reserves 12.199.146; capsub **3.213.398**; 2025 in resultaat 210.899; provincie ovensubsidie 723.166); voorzieningen pensioen **3.600.000** unchanged; schulden **5.721.355** (LT bank **3.600.000** >5y + overige 132.750; ST **1.973.321** waarvan LT-due **444.250** + leveranciers **598.377** + tax 95.644 + soc 627.066; gov-guaranteed empty); bedrijfsopbrengsten 10.024.896; omzet **9.745.034** vs 9.339.054 (category unpublished); 60 **1.092.430**; 61 **1.542.035**; pers **5.188.837** / **64,2 VTE** / 101.250 uur / YE 70 (lonen 3.525.128 / RSZ 884.396 / pensioen 510.658) + uitzend 3,7 VTE / 202.007; afschr 1.628.102; expl **+358.143** vs −392.574; fin opbr 244.454; fin kosten 102.710; tax empty; PnL **+499.887** vs −190.121 all to reserves; dividend **0** (694 empty); capex aanschaf **3.226.690**; commissaris 15.000; bestuurders 38.017 / presentiegeld table 31.295. 12.852 crematies 2025 (Lochristi 5.425 / Sint-Niklaas 3.675 / Aalst 3.752). Vennoten: 47 Oost-Vlaanderen municipalities (jaarverslag p40).\n"
            "- CSVs: sources+4/entities+1/budgets+54/commitments+1/leaderboard+1 + FOI ready `gap_wstl_omzet_cat_empty_debt_5_72m_pens_3_60m_l5` (not sent); rq_1394=done; spawn rq_1395; ticks=1394.\n"
            "- Coverage: residual dual L5 (IGS Westlede leftover crematorium IGS live WVV). Does **not** move L5 near-complete of EUR 347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs gemeente funeral fees possible. No progress refresh (not every-10; next 1400).\n"
            "- Next: rq_1395 residual dual L5 VL JR2025 hole_fill (prefer leftover Hofheide KBO 0872.310.211 CDN 2026-00343763 if still live; leftover IGS Pontes Wilrijk/Turnhout/Lommel if a 2025 PDF downloads; leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover Nuhma daughters Otary RS only after leftover IGS/EVA/AGB; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / ILvA 1344 / Haviland 1370).\n"
        )
        with log.open("a", encoding="utf-8") as f:
            f.write(entry)
        print("loop_log ok")
    print("tick1394 write", step, "done")


if __name__ == "__main__":
    main()

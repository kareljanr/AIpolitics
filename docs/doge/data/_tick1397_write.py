# -*- coding: utf-8 -*-
"""Tick 1397 — leftover IGS IVEBICA JR2025 official NBB WVV euros.
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

TICK = "1397"
UTC = "2026-08-19T05:15:00Z"
ENT = "igs_ivbc"
HIER = "Vlaanderen>Antwerpen>IGS>IVEBICA"
GAP = "gap_ivbc_omzet_empty_toelagen_1_38m_pers_1_02m_l5"
SRC = "src_ivbc_jr2025_nbb"
SRC2 = "src_ivbc_site"
SRC3 = "src_kbo_ivbc_0280300997"
SRC4 = "src_ivbc_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00160301.pdf"
SRC2_URL = "https://www.ivebica.be/over-ivebica"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0280300997"
SRC4_URL = "https://www.ivebica.be/klachtenprocedure"
FOI_EMAIL = "cultuur@ivebica.be"
FOI_POSTAL = "Heuvelstraat 111-117 2620 Hemiksem"
DRAFT = "docs/doge/foi/drafts/gap_ivbc_omzet_empty_toelagen_1_38m_pers_1_02m_l5.md"
COMM = "comm_ivbc_jr2025_pnl"
LB = "lb_ivbc_omzet_empty_toelagen_1_38m_pers_1_02m"

VENNOTEN = "Hemiksem + Schelle + Niel (ivebica.be/over-ivebica; 7 VE; leftover IGS library/culture/academy Rupel)"


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
    ("bud_ivbc_assets_2025", "2025", "919753", "2025 assets 919753 VKT-inb 20/58; commissaris 919752.75; tick1397; primary official NBB WVV"),
    ("bud_ivbc_assets_2024", "2024", "780057", "2024 assets 780057 comparative; tick1397; primary official NBB WVV 20/58"),
    ("bud_ivbc_fixed_2025", "2025", "148430", "2025 vaste activa 148430 vs 121195; tick1397; primary official NBB WVV 21/28"),
    ("bud_ivbc_iva_2025", "2025", "15053", "2025 IVA 15053 vs empty; tick1397; primary official NBB WVV 21"),
    ("bud_ivbc_mva_2025", "2025", "133377", "2025 MVA 133377 vs 121195; tick1397; primary official NBB WVV 22/27"),
    ("bud_ivbc_buildings_2025", "2025", "4938", "2025 terreinen/gebouwen 4938 vs 5318; tick1397; primary official NBB WVV 22"),
    ("bud_ivbc_machines_2025", "2025", "90169", "2025 machines 90169 vs 102109; tick1397; primary official NBB WVV 23"),
    ("bud_ivbc_furniture_2025", "2025", "12549", "2025 meubilair 12549 vs 13769; tick1397; primary official NBB WVV 24"),
    ("bud_ivbc_othmva_2025", "2025", "25721", "2025 overige MVA 25721 vs empty; tick1397; primary official NBB WVV 26"),
    ("bud_ivbc_current_2025", "2025", "771323", "2025 vlottend 771323 vs 658862; tick1397; primary official NBB WVV 29/58"),
    ("bud_ivbc_stocks_2025", "2025", "137079", "2025 voorraden 137079 vs 136543 uitleenmateriaal; tick1397; primary official NBB WVV 30/36"),
    ("bud_ivbc_strecv_2025", "2025", "140032", "2025 ST vorderingen 140032 vs 59157; tick1397; primary official NBB WVV 40/41"),
    ("bud_ivbc_trade_2025", "2025", "105397", "2025 handelsvorderingen 105397 vs 45520; tick1397; primary official NBB WVV 40"),
    ("bud_ivbc_othrecv_2025", "2025", "34636", "2025 overige vorderingen 34636 JUMP vs 13636; tick1397; primary official NBB WVV 41"),
    ("bud_ivbc_invest_2025", "2025", "8728", "2025 geldbeleggingen 8728 unchanged; tick1397; primary official NBB WVV 50/53"),
    ("bud_ivbc_cash_2025", "2025", "455342", "2025 liquide middelen 455342 vs 420551; tick1397; primary official NBB WVV 54/58"),
    ("bud_ivbc_cash_2024", "2024", "420551", "2024 liquide middelen 420551 comparative; tick1397; primary official NBB WVV 54/58"),
    ("bud_ivbc_prepaid_2025", "2025", "30142", "2025 overlopend actief 30142 vs 33884; tick1397; primary official NBB WVV 490/1"),
    ("bud_ivbc_equity_2025", "2025", "581329", "2025 EV 581329 vs 520485; tick1397; primary official NBB WVV 10/15"),
    ("bud_ivbc_inbreng_2025", "2025", "449877", "2025 inbreng 449877 (beschikbaar 68875 / onbeschikbaar 381002); tick1397; primary official NBB WVV 10/11"),
    ("bud_ivbc_reserves_2025", "2025", "57058", "2025 reserves 57058 (onbeschikbaar 13557 / beschikbaar 43501); tick1397; primary official NBB WVV 13"),
    ("bud_ivbc_re_2025", "2025", "74394", "2025 overgedragen winst 74394 vs 28761; tick1397; primary official NBB WVV 14"),
    ("bud_ivbc_debt_2025", "2025", "338424", "2025 schulden 338424 vs 259572; tick1397; primary official NBB WVV 17/49"),
    ("bud_ivbc_debt_2024", "2024", "259572", "2024 schulden 259572 comparative; tick1397; primary official NBB WVV 17/49"),
    ("bud_ivbc_st_2025", "2025", "249943", "2025 ST schulden 249943 vs 195240; no LT; tick1397; primary official NBB WVV 42/48"),
    ("bud_ivbc_sttrade_2025", "2025", "86237", "2025 leveranciers 86237 vs 56191; tick1397; primary official NBB WVV 440/4"),
    ("bud_ivbc_stsoc_2025", "2025", "131780", "2025 bezoldigingen/sociale lasten 131780 vs 131377; tick1397; primary official NBB WVV 454/9"),
    ("bud_ivbc_deferred_2025", "2025", "88480", "2025 overlopend passief 88480 vs 64332; tick1397; primary official NBB WVV 492/3"),
    ("bud_ivbc_brutomarge_2025", "2025", "1211667", "2025 brutomarge 1211667 vs 1176709; omzet 70 empty; tick1397; primary official NBB WVV 9900"),
    ("bud_ivbc_brutomarge_2024", "2024", "1176709", "2024 brutomarge 1176709 comparative; tick1397; primary official NBB WVV 9900"),
    ("bud_ivbc_omzet_jv_2025", "2025", "207858", "2025 omzet 207858.25 jaarverslag (WVV 70 empty); tick1397; primary official NBB WVV jaarverslag"),
    ("bud_ivbc_othinc_jv_2025", "2025", "1382095", "2025 andere bedrijfsopbrengsten 1382095.14 jaarverslag; tick1397; primary official NBB WVV jaarverslag"),
    ("bud_ivbc_diensten_jv_2025", "2025", "370466", "2025 diverse goederen en diensten 370465.83 jaarverslag (60/61 empty); tick1397; primary official NBB WVV jaarverslag"),
    ("bud_ivbc_subs_2025", "2025", "148220", "2025 publieke subsidies listed 148220.28 (Maribel/VIA/Kunstkuur/academie); tick1397; primary official NBB WVV 6.8"),
    ("bud_ivbc_pers_2025", "2025", "1023843", "2025 pers 1023843 vs 1038305 / 12.2 VTE; tick1397; primary official NBB WVV 62"),
    ("bud_ivbc_pers_2024", "2024", "1038305", "2024 pers 1038305 / 12.8 VTE comparative; tick1397; primary official NBB WVV 62"),
    ("bud_ivbc_afschr_2025", "2025", "31356", "2025 afschr 31356 vs 30376; tick1397; primary official NBB WVV 630"),
    ("bud_ivbc_wv_2025", "2025", "69937", "2025 WV voorraden/collecties 69937 vs 71751; tick1397; primary official NBB WVV 631/4"),
    ("bud_ivbc_othcost_2025", "2025", "25780", "2025 andere bedrijfskosten 25780 vs empty; tick1397; primary official NBB WVV 640/8"),
    ("bud_ivbc_expl_2025", "2025", "60751", "2025 expl +60751 vs +36277; tick1397; primary official NBB WVV 9901"),
    ("bud_ivbc_expl_2024", "2024", "36277", "2024 expl +36277 comparative; tick1397; primary official NBB WVV 9901"),
    ("bud_ivbc_pnl_2025", "2025", "60844", "2025 PnL +60844 vs +38348; commissaris 60843.93; tick1397; primary official NBB WVV 9904"),
    ("bud_ivbc_pnl_2024", "2024", "38348", "2024 PnL +38348 comparative; tick1397; primary official NBB WVV 9904"),
    ("bud_ivbc_div_2025", "2025", "0", "2025 dividend 694 empty; tick1397; primary official NBB WVV 694"),
    ("bud_ivbc_capex_mva_2025", "2025", "42867", "2025 MVA aanschaf 42867 (8169); tick1397; primary official NBB WVV 6.1.2"),
    ("bud_ivbc_capex_iva_2025", "2025", "16928", "2025 IVA aanschaf 16928 (8029); tick1397; primary official NBB WVV 6.1.1"),
    ("bud_ivbc_comm_2025", "2025", "3751", "2025 commissaris Clybouw 3751 excl btw 3100; tick1397; primary official NBB WVV 6.6"),
]


def main() -> None:
    step = sys.argv[1] if len(sys.argv) > 1 else "all"

    if step in ("all", "sources"):
        n = append_rows(
            DATA / "sources.csv",
            [
                {
                    "source_id": SRC,
                    "title": "IGS IVEBICA jaarrekening boekjaar 2025 (official NBB WVV VKT-inb deposit 2026-00160301; AV 10.06.2026)",
                    "url": SRC_URL,
                    "publisher": "IGS IVEBICA / NBB WVV deposit",
                    "accessed_date": "2026-08-19",
                    "source_class": "budget",
                    "notes": (
                        "tick1397; official NBB VKT-inb PDF 1.55MB 35p deposit 2026-00160301 created 15.06.2026; "
                        "leftover IGS library/culture/academy Hemiksem+Schelle+Niel; "
                        "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                        "Belscope/Companyweb extracted tables not used; Staatsbladmonitor table euros not used; "
                        "commissaris Clybouw Bedrijfsrevisoren BV B00162 / 0446.129.922 / Arnaud Clybouw A02273 oordeel getrouw beeld assets 919752.75 / PnL 60843.93; "
                        "omzet 70 empty; 60/61 empty; only brutomarge published on form; jaarverslag publishes omzet 207858 / andere 1382095; 6.6 related empty except commissaris"
                    ),
                },
                {
                    "source_id": SRC2,
                    "title": "IGS IVEBICA official site (leftover library/culture/academy IGS Hemiksem Schelle Niel)",
                    "url": SRC2_URL,
                    "publisher": "IGS IVEBICA",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1397; leftover IGS of 3 Rupel municipalities Hemiksem+Schelle+Niel; "
                        "site quote intergemeentelijke vereniging bibliotheek cultuurdienst academie; statutory 2025 balans is the NBB CDN deposit"
                    ),
                },
                {
                    "source_id": SRC3,
                    "title": "KBO IGS IVEBICA 0280.300.997",
                    "url": SRC3_URL,
                    "publisher": "KBO Public Search FOD Economie",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1397; KBO 0280.300.997 Actief / normale toestand since 11.04.2003; "
                        "statutaire naam Intergemeentelijke Vereniging voor Bibliotheekwerking, Cultuur en Academie voor Deeltijds Kunstonderwijs since 31.08.2017; "
                        "afkorting IVEBICA since 31.08.2017; Opdrachthoudende vereniging (Vlaams Gewest) since 11.04.2003; "
                        "zetel Heuvelstraat 111-117 2620 Hemiksem since 05.06.2023; 7 VE; "
                        "KBO no email/web/tel; official site https://www.ivebica.be/; "
                        "btw since 01.01.2026; RSZ since 01.01.2022; NACE 91.110/85.520; aanbestedende overheid since 11.04.2003; "
                        "6 bestuurders; KBO stand 18.08.2026"
                    ),
                },
                {
                    "source_id": SRC4,
                    "title": "IGS IVEBICA FOI channel / klachtenprocedure (cultuur@ivebica.be; directeur Inge Cornelis)",
                    "url": SRC4_URL,
                    "publisher": "IGS IVEBICA",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1397; site contact cultuur@ivebica.be; privacy HQ 03/218.72.09 privacy@ivebica.be; "
                        "directeur Inge Cornelis (klachten 2e niveau); bibhemiksem@ivebica.be; bibniel@ivebica.be"
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
                    "name_nl": "IGS IVEBICA (Opdrachthoudende Vereniging voor Bibliotheekwerking, Cultuur en Academie; leftover IGS Hemiksem/Schelle/Niel)",
                    "name_fr": "IGS IVEBICA (association missionnee bibliotheque/culture/academie Hemiksem/Schelle/Niel; IGS residuel)",
                    "name_en": "IGS IVEBICA leftover IGS library culture academy Hemiksem Schelle Niel",
                    "level": "other",
                    "parent_id": "sec_flanders",
                    "community_language": "nl",
                    "website": "https://www.ivebica.be/",
                    "foi_email": FOI_EMAIL,
                    "foi_postal": FOI_POSTAL,
                    "notes": (
                        "tick1397 leftover residual IGS IVEBICA library/culture/academy IGS; "
                        "KBO 0280.300.997 Actief since 11.04.2003; official NBB WVV VKT-inb PDF downloads; "
                        "sourced euros assets 919753 omzet empty-form/207858-jv diensten empty-form/370466-jv pers 1023843 debt 338424 pnl 60844 equity 581329 capex 42867 othinc 1382095; "
                        "FOI ready omzet empty / 1.38m toelagen / 1.02m pers / 137k collectie; "
                        "distinct from already-mined IGS Pontes 1396 prefix pnts and IGS Hofheide 1395 prefix hofh and IGS Westlede 1394 prefix wstl and HAVICREM 1393 prefix hvic and IVLA 1392 / Fluvius stack 1382-1391"
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
                    "title": "IGS IVEBICA JR2025 leftover IGS dual (assets 0.92m / omzet empty-form / toelagen 1.38m / pers 1.02m / PnL +61k)",
                    "entity_id": ENT,
                    "beneficiary": "IGS IVEBICA / " + VENNOTEN,
                    "legal_basis": "WVV OV; Decreet Lokaal Bestuur; NBB neerlegging",
                    "decision_date": "2026-06-10",
                    "start_year": "2003",
                    "end_year": "",
                    "total_envelope_eur": "1382095",
                    "cash_by_year": "",
                    "remaining_eur": "",
                    "status": "active",
                    "evaluation_url": SRC_URL,
                    "stated_goal": "Local leftover IGS map VL library/culture/academy Hemiksem/Schelle/Niel — omzet unpublished on form / 1.38m andere opbr / 1.02m pers / PnL +61k",
                    "cut_option": "Publish omzet + 60/61 split + 1.38m vennoot-toelagen per gemeente + 1.02m pers split; do not keep library IGS as dual unpublished vehicle",
                    "source_id": SRC,
                    "confidence": "strong",
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "notes": "tick1397; assets 919753 omzet empty-form/207858-jv diensten empty-form pers 1023843 debt 338424 pnl 60844 equity 581329 capex 42867 othinc 1382095; FOI ready not sent; not TE-additive of 348bn",
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
                    "name": "IGS IVEBICA JR2025 leftover IGS: assets 0.92m / omzet empty-form / toelagen 1.38m / pers 1.02m / 12.2 VTE",
                    "level": "L5",
                    "type": "local_budget_line",
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "annual_cost_eur": "1023843",
                    "total_cost_eur": "1382095",
                    "tco_notes": (
                        "Leftover dual IGS library/culture/academy 3 municipalities (Hemiksem/Schelle/Niel): "
                        "assets 0.92m / equity 0.58m / pnl +61k / omzet unpublished on form (jaarverslag 208k) / 60-61 unpublished / "
                        "diensten unpublished on form / pers 1.02m / 12.2 VTE / "
                        "andere bedrijfsopbrengsten 1.38m / debt 0.34m (no LT) / cash 455k / capex 43k / "
                        "voorraad uitleenmateriaal 137k (qualified emphasis); "
                        "official NBB WVV live; do not treat 1.38m as TE-additive of 348bn"
                    ),
                    "confidence": "strong",
                    "source_id": SRC,
                    "beneficiaries": "IGS IVEBICA / " + VENNOTEN,
                    "stated_goal": "Local leftover IGS map VL library/culture/academy Hemiksem/Schelle/Niel — JR2025 live; dual omzet/toelagen FOI",
                    "measured_outcome": "Official NBB WVV 2026-08-19: assets 0.92m / omzet empty-form / toelagen 1.38m / pers 1.02m / pnl +61k / 12.2 VTE",
                    "absurdity_score": "6.5",
                    "cost_score": "5.5",
                    "difficulty": "3.0",
                    "priority_index": "5.6",
                    "cut_proposal": "Publish omzet + 60/61 split + 1.38m vennoot-toelagen per gemeente + 1.02m pers split; do not keep library IGS as dual unpublished vehicle",
                    "status": "active",
                    "struck_reason": "",
                    "notes": "tick1397; leftover IGS IVEBICA library/culture/academy IGS; FOI ready not sent; not TE-additive of 348bn; distinct from IGS Pontes 1396 and IGS Hofheide 1395 and IGS Westlede 1394 and HAVICREM 1393 and IVLA 1392 / Fluvius stack 1382-1391",
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
                        "omzet WVV 70 empty + 60/61 empty (abbreviated VKT; only brutomarge 1211667 vs 1176709 published; jaarverslag omzet 207858 / diensten 370466) per stroom/gemeente unpublished "
                        "+ andere bedrijfsopbrengsten 1382095 (jaarverslag; subsidies listed 148220) vennoot-toelage per gemeente unpublished "
                        "+ pers 1023843 / 12.2 VTE / split unpublished "
                        "+ voorraden 137079 uitleenmateriaal (commissaris emphasis; WV 69937) unpublished "
                        "+ MVA aanschaf 42867 / IVA 16928 tender unpublished "
                        "+ 6.6 related empty + dividend 694 empty + voorzitter unpublished"
                    ),
                    "why_it_matters": (
                        "Leftover IGS library/culture/academy of 3 mined Rupel municipalities Hemiksem/Schelle/Niel "
                        "(distinct from IGS Pontes 1396 and IGS Hofheide 1395 and IGS Westlede 1394 and HAVICREM 1393 and from IVLA 1392 / Fluvius 1382-1391): "
                        "0.92m assets / omzet unpublished on form / 60-61 unpublished / 1.38m andere opbr / 1.02m pers / 137k collectie / "
                        "abbreviated VKT hides omzet and diensten "
                        "is a dual opacity residual, not TE-additive of 348bn."
                    ),
                    "priority": "8",
                    "recipient_body": "IGS IVEBICA / Raad van Bestuur / Inge Cornelis / Hemiksem+Schelle+Niel vennoten",
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
                        "tick1397 leftover IGS library/culture/academy 3 gemeenten after honest hunt; "
                        "live JR2025 official NBB WVV VKT-inb PDF now extracted (1.55MB 35p deposit 2026-00160301). "
                        "IGS Pontes already mined 1396 — skipped. IGS Hofheide already mined 1395 — skipped. IGS Westlede already mined 1394 — skipped. HAVICREM already mined 1393 — skipped. IVLA already mined 1392 — skipped. Fluvius stack already mined 1382-1391 — skipped. "
                        "Leftover AGB Duffel/Zoersel/Diepenbeek already mined — skipped. IVAREM still 2024 — skipped. "
                        "Dommelhof leftover next if a JR2025 PDF now downloads. "
                        "Otary RS Nuhma-adjacent fallback not taken. "
                        "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                    ),
                }
            ],
        )
        print("foi", n)

    if step in ("all", "rq"):
        rq_new = {
            "task_id": "rq_1397",
            "title": "IGS IVEBICA JR2025 leftover dual residual",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "done",
            "hierarchy_target": "L5",
            "entity_id": ENT,
            "instructions": (
                "Completed: IGS IVEBICA leftover IGS library/culture/academy of Hemiksem+Schelle+Niel after honest hunt; "
                "KBO 0280.300.997 Actief; live JR2025 official NBB WVV VKT-inb PDF (1.55MB 35p deposit 2026-00160301; commissaris Clybouw getrouw beeld); "
                "sourced euros assets 919753 / omzet empty-form/207858-jv / diensten empty-form / pers 1023843 / debt 338424 / pnl 60844 / capex 42867 / othinc 1382095; "
                "FOI ready omzet empty / 1.38m toelagen / 1.02m pers / 137k collectie"
            ),
            "blocked_gap_id": GAP,
            "created_utc": "2026-08-19T04:55:00Z",
            "updated_utc": UTC,
            "notes": (
                "tick1397 IGS IVEBICA leftover IGS library/culture/academy residual; KBO 0280.300.997; "
                "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1398 residual dual L5 VL"
            ),
        }
        rq_spawn = {
            "task_id": "rq_1398",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
                "(prior 1255-1397 done including IGS IVEBICA 1397 leftover library/culture/academy IGS live NBB WVV / "
                "IGS Pontes 1396 leftover crematorium IGS live NBB WVV / "
                "IGS Hofheide 1395 leftover crematorium IGS live NBB WVV / "
                "IGS Westlede 1394 leftover crematorium IGS live NBB WVV / "
                "HAVICREM 1393 leftover crematorium IGS live NBB WVV / "
                "IVLA 1392 leftover waste IGS live NBB WVV); "
                "leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; "
                "other leftover IGS only if a DISTINCT unmined entity has a live 2025 PDF; "
                "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
                "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
                "skip already-mined IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / ILvA 1344; "
                "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
                "ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick1397 after IGS IVEBICA leftover library/culture/academy IGS live NBB WVV; next residual dual L5 VL",
        }
        found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1397", rq_new, rq_spawn)
        print("research_queue 1397", found, "spawned_1398", spawned)

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
                    "last_unit_id": "rq_1397",
                    "ticks_completed": "1397",
                    "paused": "no",
                    "notes": (
                        "tick1397 IGS IVEBICA leftover IGS library/culture/academy residual; KBO 0280.300.997; "
                        "live JR2025 NBB WVV PDF; sourced euros assets 919753 omzet empty-form/207858-jv diensten empty-form pers 1023843 debt 338424 pnl 60844 equity 581329 capex 42867 othinc 1382095; "
                        "FOI ready omzet-empty/1.38m toelagen/1.02m pers/137k collectie; next rq_1398 residual dual L5 VL; continuous hole_fill"
                    ),
                }
            )
        print("loop_state ok")

    if step in ("all", "log"):
        log = ROOT / "loop_log.md"
        entry = (
            "### Tick 1397 - 2026-08-19 - rq_1397 IGS IVEBICA dual residual leftover\n"
            "- Unit: IGS IVEBICA / Intergemeentelijke Vereniging voor Bibliotheekwerking, Cultuur en Academie voor Deeltijds Kunstonderwijs (leftover IGS opdrachthoudende vereniging / library + cultuur + academie of 3 mined Rupel municipalities Hemiksem + Schelle + Niel; 7 VE) after residual dual hunt (KBO **0280.300.997**; official ivebica.be has 3 gemeenten + klachtenprocedure; live NBB WVV VKT-inb deposit **2026-00160301** PDF 1.55MB / 35p; AV **10.06.2026**; created **15.06.2026**; commissaris Achiel Clybouw, André Clybouw & Co B00162 / 0446.129.922 / Arnaud Clybouw A02273 oordeel getrouw beeld assets 919.752,75 / PnL +60.843,93; fee 3.751 excl. btw 3.100; emphasis of matter uitleenmateriaal as voorraad). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; leftover AGB first: Duffel/Zoersel/Diepenbeek already mined, Zwevegem extract-only — then leftover IVEBICA with live CDN this tick). Distinct from already-mined IGS Pontes 1396 (prefix `pnts`) and IGS Hofheide 1395 (prefix `hofh`) and IGS Westlede 1394 (prefix `wstl`) and HAVICREM 1393 (prefix `hvic`) and from IVLA 1392 / Fluvius stack 1382-1391. First confirmed not already mined: no IVEBICA / 0280.300.997 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **11.04.2003**; statutaire naam Intergemeentelijke Vereniging voor Bibliotheekwerking, Cultuur en Academie voor Deeltijds Kunstonderwijs since 31.08.2017; afkorting IVEBICA since 31.08.2017; Opdrachthoudende vereniging (Vlaams Gewest) since 11.04.2003; zetel Heuvelstraat 111-117 2620 Hemiksem since 05.06.2023; **7 VE**; KBO no email/web/tel; official site https://www.ivebica.be/; btw since 01.01.2026; RSZ since 01.01.2022; NACE 91.110/85.520. Directeur Inge Cornelis (klachtenprocedure). Contact cultuur@ivebica.be; tel 03/218.72.09. Hunt leftover AGB first: Duffel/Zoersel/Diepenbeek already mined — skipped; Zwevegem extract-only — skipped. Leftover IGS IVEBICA statutory CDN live this tick (HTTP 200 / 1552185 / 35p) — taken. IGS Pontes already mined 1396 — skipped. IGS Hofheide already mined 1395 — skipped. IGS Westlede already mined 1394 — skipped. HAVICREM already mined 1393 — skipped. IVLA already mined 1392 — skipped. Fluvius stack already mined 1382-1391 — skipped. IVAREM still JR2024 — skipped. IGL last JR2024 — skipped. Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live IVEBICA extracted. Otary RS Nuhma-adjacent fallback not taken. NBB consult skipped (403/SPA); euros extracted from the official VKT-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used. Not every-10 (next 1400).\n"
            "- EUR strong (primary official WVV VKT-inb; **omzet 70 empty** on form; **60/61 empty** so diensten unpublished as a split on form; only brutomarge published on form; jaarverslag 30.04.2026 publishes omzet 207.858,25 / andere bedrijfsopbrengsten 1.382.095,14 / diverse goederen en diensten 370.465,83; 6.1.3/6.2/6.3/6.7/6.9/7/8/9/14-17 not filed; 6.6 related empty except commissaris): assets **919.753** (was 780.057; commissaris 919.752,75); fixed **148.430** / MVA **133.377** (gebouwen **4.938**; machines **90.169**; meubilair **12.549**; overige **25.721**); IVA **15.053**; FVA empty; current **771.323**; voorraden **137.079** (uitleenmateriaal; commissaris emphasis); ST recv **140.032** (trade 105.397 / other **34.636 JUMP** vs 13.636); geldbeleggingen **8.728**; cash **455.342**; prepaid 30.142; equity **581.329** (inbreng 449.877; reserves 57.058; overgedragen 74.394); voorzieningen empty; schulden **338.424** (no LT; ST **249.943** waarvan leveranciers **86.237** + soc **131.780** + other 31.844; deferred 88.480); brutomarge **1.211.667** vs 1.176.709; omzet 70 empty (jaarverslag 207.858); 60/61 empty; pers **1.023.843** / **12,2 VTE** (was 1.038.305 / 12,8); afschr 31.356; WV collecties 69.937; andere bedrijfskosten 25.780; expl **+60.751** vs +36.277; fin opbr 767; fin kosten 580; tax 93; PnL **+60.844** vs +38.348 (15.211 to reserves / 74.394 overgedragen); dividend **0** (694 empty); capex MVA aanschaf **42.867** + IVA 16.928; publieke subsidies listed **148.220**; andere bedrijfsopbrengsten **1.382.095**; commissaris 3.751. Vennoten: Hemiksem + Schelle + Niel (ivebica.be).\n"
            "- CSVs: sources+4/entities+1/budgets+47/commitments+1/leaderboard+1 + FOI ready `gap_ivbc_omzet_empty_toelagen_1_38m_pers_1_02m_l5` (not sent); rq_1397=done; spawn rq_1398; ticks=1397.\n"
            "- Coverage: residual dual L5 (IGS IVEBICA leftover library/culture/academy IGS live WVV). Does **not** move L5 near-complete of EUR 347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs gemeente cultuur/bib toelagen possible. No progress refresh (not every-10; next 1400).\n"
            "- Next: rq_1398 residual dual L5 VL JR2025 hole_fill (prefer leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover Nuhma daughters Otary RS only after leftover IGS/EVA/AGB; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / ILvA 1344 / Haviland 1370).\n"
        )
        with log.open("a", encoding="utf-8") as f:
            f.write(entry)
        print("loop_log ok")
    print("tick1397 write", step, "done")


if __name__ == "__main__":
    main()

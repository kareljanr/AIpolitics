# -*- coding: utf-8 -*-
"""Tick 1392 — leftover IVLA / I.VL.A. JR2025 official NBB WVV euros.
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

TICK = "1392"
UTC = "2026-08-19T03:50:00Z"
ENT = "igs_ivla"
HIER = "Vlaanderen>OostVlaanderen>IGS>IVLA"
GAP = "gap_ivla_omzet_empty_debt_2_25m_gft_1_06m_l5"
SRC = "src_ivla_jr2025_nbb"
SRC2 = "src_ivla_site"
SRC3 = "src_kbo_ivla_0228618706"
SRC4 = "src_ivla_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00281193.pdf"
SRC2_URL = "https://www.ivla.be/bestuur/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0228618706"
SRC4_URL = "https://www.ivla.be/contact/"
FOI_EMAIL = "info@ivla.be"
FOI_POSTAL = "Meersbloem-Melden 46A 9700 Oudenaarde"
DRAFT = "docs/doge/foi/drafts/gap_ivla_omzet_empty_debt_2_25m_gft_1_06m_l5.md"
COMM = "comm_ivla_jr2025_pnl"
LB = "lb_ivla_omzet_empty_debt_2_25m_gft_1_06m"

VENNOTEN = (
    "Brakel 13.773% + Horebeke 1.879% + Lierde 6.166% + Maarkedal 6.339% + "
    "Oudenaarde 27.375% + Ronse 24.184% + Wortegem-Petegem 5.802% + "
    "Kruisem 6.527% + Zwalm 7.953% + ILVA 1 C-share + IMOG 1 C-share "
    "(99.573 aandelen)"
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
    ("bud_ivla_assets_2025", "2025", "4169634", "2025 assets 4169634 VKT-inb 20/58; tick1392; primary official NBB WVV"),
    ("bud_ivla_assets_2024", "2024", "3803070", "2024 assets 3803070 comparative; tick1392; primary official NBB WVV 20/58"),
    ("bud_ivla_fixed_2025", "2025", "1401284", "2025 vaste activa 1401284 vs 402010; tick1392; primary official NBB WVV 21/28"),
    ("bud_ivla_mva_2025", "2025", "1400432", "2025 MVA 1400432 vs 401159; tick1392; primary official NBB WVV 22/27"),
    ("bud_ivla_buildings_2025", "2025", "51032", "2025 terreinen/gebouwen 51032 vs 51981; tick1392; primary official NBB WVV 22"),
    ("bud_ivla_machines_2025", "2025", "1269295", "2025 machines 1269295 JUMP vs 284589; tick1392; primary official NBB WVV 23"),
    ("bud_ivla_furniture_2025", "2025", "29724", "2025 meubilair 29724 vs 656; tick1392; primary official NBB WVV 24"),
    ("bud_ivla_othmva_2025", "2025", "50382", "2025 overige MVA 50382 vs 63933; tick1392; primary official NBB WVV 26"),
    ("bud_ivla_fva_2025", "2025", "851", "2025 FVA 851 vs 851; tick1392; primary official NBB WVV 28"),
    ("bud_ivla_current_2025", "2025", "2768350", "2025 vlottend 2768350 vs 3401059; tick1392; primary official NBB WVV 29/58"),
    ("bud_ivla_stocks_2025", "2025", "41890", "2025 voorraden 41890 vs 8971; tick1392; primary official NBB WVV 30/36"),
    ("bud_ivla_strecv_2025", "2025", "1461428", "2025 ST vorderingen 1461428 vs 930507; tick1392; primary official NBB WVV 40/41"),
    ("bud_ivla_trade_2025", "2025", "980319", "2025 handelsvorderingen 980319 vs 857740; tick1392; primary official NBB WVV 40"),
    ("bud_ivla_othrecv_2025", "2025", "481109", "2025 overige ST vorderingen 481109 JUMP vs 72767; tick1392; primary official NBB WVV 41"),
    ("bud_ivla_cash_2025", "2025", "1224728", "2025 liquide middelen 1224728 DROP vs 2418359; tick1392; primary official NBB WVV 54/58"),
    ("bud_ivla_cash_2024", "2024", "2418359", "2024 liquide middelen 2418359 comparative; tick1392; primary official NBB WVV 54/58"),
    ("bud_ivla_prepaid_2025", "2025", "40305", "2025 overlopend actief 40305 vs 43222; tick1392; primary official NBB WVV 490/1"),
    ("bud_ivla_equity_2025", "2025", "1915772", "2025 EV 1915772 vs 2383224; tick1392; primary official NBB WVV 10/15"),
    ("bud_ivla_inbreng_2025", "2025", "1893040", "2025 inbreng 1893040 / 99573 aandelen; tick1392; primary official NBB WVV 10/11"),
    ("bud_ivla_reserves_2025", "2025", "189354", "2025 reserves 189354 vs 246880; tick1392; primary official NBB WVV 13"),
    ("bud_ivla_retained_2025", "2025", "-166622", "2025 overgedragen -166622 vs 243303; tick1392; primary official NBB WVV 14"),
    ("bud_ivla_debt_2025", "2025", "2253862", "2025 schulden 2253862 vs 1419846; tick1392; primary official NBB WVV 17/49"),
    ("bud_ivla_debt_2024", "2024", "1419846", "2024 schulden 1419846 comparative; tick1392; primary official NBB WVV 17/49"),
    ("bud_ivla_st_2025", "2025", "1769733", "2025 ST schulden 1769733 (no LT); tick1392; primary official NBB WVV 42/48"),
    ("bud_ivla_sttrade_2025", "2025", "1467246", "2025 leveranciers 1467246 vs 1122217; tick1392; primary official NBB WVV 440/4"),
    ("bud_ivla_sttax_2025", "2025", "66909", "2025 belastingschulden 66909 vs 48826; tick1392; primary official NBB WVV 450/3"),
    ("bud_ivla_stsoc_2025", "2025", "17119", "2025 bezoldigingen/sociale lasten 17119 vs 29317; tick1392; primary official NBB WVV 454/9"),
    ("bud_ivla_stother_2025", "2025", "218221", "2025 overige ST schulden 218221 vs 146717; tick1392; primary official NBB WVV 47/48"),
    ("bud_ivla_deferred_2025", "2025", "484129", "2025 overlopend passief 484129 JUMP vs 72769; tick1392; primary official NBB WVV 492/3"),
    ("bud_ivla_brutomarge_2025", "2025", "7353", "2025 brutomarge 7353 DROP vs 555793; omzet 70 empty; tick1392; primary official NBB WVV 9900"),
    ("bud_ivla_brutomarge_2024", "2024", "555793", "2024 brutomarge 555793 comparative; tick1392; primary official NBB WVV 9900"),
    ("bud_ivla_pers_2025", "2025", "399515", "2025 pers 399515 vs 397745 / 4 VTE; tick1392; primary official NBB WVV 62"),
    ("bud_ivla_pers_2024", "2024", "397745", "2024 pers 397745 / 4.1 VTE comparative; tick1392; primary official NBB WVV 62"),
    ("bud_ivla_afschr_2025", "2025", "63215", "2025 afschr 63215 vs 52908; tick1392; primary official NBB WVV 630"),
    ("bud_ivla_othcost_2025", "2025", "5940", "2025 andere bedrijfskosten 5940 vs 5759; tick1392; primary official NBB WVV 640/8"),
    ("bud_ivla_expl_2025", "2025", "-461317", "2025 expl -461317 vs +99381; tick1392; primary official NBB WVV 9901"),
    ("bud_ivla_expl_2024", "2024", "99381", "2024 expl +99381 comparative; tick1392; primary official NBB WVV 9901"),
    ("bud_ivla_fininc_2025", "2025", "13922", "2025 financiele opbrengsten 13922 vs 16040; tick1392; primary official NBB WVV 75"),
    ("bud_ivla_fincost_2025", "2025", "1126", "2025 financiele kosten 1126 vs 1612; tick1392; primary official NBB WVV 65"),
    ("bud_ivla_pretax_2025", "2025", "-448521", "2025 verlies voor belasting -448521 vs +113810; tick1392; primary official NBB WVV 9903"),
    ("bud_ivla_tax_2025", "2025", "18931", "2025 belasting 18931 vs 4407; tick1392; primary official NBB WVV 67/77"),
    ("bud_ivla_pnl_2025", "2025", "-467452", "2025 PnL -467452 vs +109402; tick1392; primary official NBB WVV 9904"),
    ("bud_ivla_pnl_2024", "2024", "109402", "2024 PnL +109402 comparative; tick1392; primary official NBB WVV 9904"),
    ("bud_ivla_div_2025", "2025", "0", "2025 dividend 694 empty; tick1392; primary official NBB WVV 694"),
    ("bud_ivla_capex_2025", "2025", "1062489", "2025 MVA aanschaf 1062489 GFT-containers; tick1392; primary official NBB WVV 8169"),
    ("bud_ivla_comm_2025", "2025", "6250", "2025 commissaris A&C 6250; tick1392; primary official NBB WVV 6.6"),
    ("bud_ivla_board_2025", "2025", "29897", "2025 bestuurders presentiegeld+KM 29897; tick1392; primary official NBB WVV remun"),
]


def main() -> None:
    step = sys.argv[1] if len(sys.argv) > 1 else "all"

    if step in ("all", "sources"):
        n = append_rows(
            DATA / "sources.csv",
            [
                {
                    "source_id": SRC,
                    "title": "IVLA / I.VL.A. jaarrekening boekjaar 2025 (official NBB WVV VKT-inb deposit 2026-00281193; AV 29.06.2026)",
                    "url": SRC_URL,
                    "publisher": "IVLA / NBB WVV deposit",
                    "accessed_date": "2026-08-19",
                    "source_class": "budget",
                    "notes": (
                        "tick1392; official NBB VKT-inb PDF 2.05MB 31p deposit 2026-00281193 header 09.07.2026; "
                        "leftover IGS waste OV Vlaamse Ardennen; "
                        "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                        "Belscope/Companyweb extracted tables not used; Staatsbladmonitor table euros not used; "
                        "commissaris A & C Bedrijfsrevisor BV B00348 / 0461.238.562 / Mohammed Boumalek A02265 fee 6250; "
                        "omzet 70 empty; 60/61 empty; 6.6 related empty; commissarisverslag p23-27 image-only this extract"
                    ),
                },
                {
                    "source_id": SRC2,
                    "title": "IVLA official bestuur (leftover waste IGS Vlaamse Ardennen; voorzitter Patrice Dutranoit)",
                    "url": SRC2_URL,
                    "publisher": "IVLA",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1392; leftover waste IGS of 9 Vlaamse Ardennen municipalities; "
                        "ivla.be/bestuur lists voorzitter Dutranoit / Bogaert / Vandekerkhove; "
                        "operational address Meersbloem-Melden 46A 9700 Oudenaarde; "
                        "statutory 2025 balans is the NBB CDN deposit"
                    ),
                },
                {
                    "source_id": SRC3,
                    "title": "KBO IVLA / I.VL.A. 0228.618.706",
                    "url": SRC3_URL,
                    "publisher": "KBO Public Search FOD Economie",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1392; KBO 0228.618.706 Actief / normale toestand since 01.04.1986; "
                        "statutaire naam Intergemeentelijke Vereniging voor Beheer van Afvalstoffen Vlaamse Ardennen since 28.12.2004; "
                        "afkorting I.VL.A. since 01.04.1986; "
                        "Opdrachthoudende vereniging (Vlaams Gewest) since 22.01.2007; "
                        "zetel Markt 1 9700 Oudenaarde Stadhuis since 01.04.1986; 1 VE; "
                        "no KBO email/web/tel; btw since 01.04.1986; RSZ since 01.01.2022; NACE 81.230/38.110; "
                        "aanbestedende overheid since 01.04.1986"
                    ),
                },
                {
                    "source_id": SRC4,
                    "title": "IVLA FOI channel / official contact (info@ivla.be; infolijn 0800 90 270)",
                    "url": SRC4_URL,
                    "publisher": "IVLA",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1392; KBO no email/web/tel; site contact info@ivla.be; "
                        "operational Meersbloem-Melden 46A 9700 Oudenaarde; "
                        "KBO zetel Markt 1 Stadhuis 9700 Oudenaarde"
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
                    "name_nl": "IVLA / I.VL.A. (Intergemeentelijke Vereniging voor Beheer van Afvalstoffen Vlaamse Ardennen; leftover IGS waste)",
                    "name_fr": "IVLA (association missionnee dechets Ardennes flamandes; IGS residuel)",
                    "name_en": "IVLA leftover IGS waste OV Flemish Ardennes",
                    "level": "other",
                    "parent_id": "sec_flanders",
                    "community_language": "nl",
                    "website": "https://www.ivla.be/",
                    "foi_email": FOI_EMAIL,
                    "foi_postal": FOI_POSTAL,
                    "notes": (
                        "tick1392 leftover residual IVLA waste IGS; "
                        "KBO 0228.618.706 Actief since 01.04.1986; official NBB WVV VKT-inb PDF downloads; "
                        "sourced euros assets 4169634 brutomarge 7353 omzet unpublished pers 399515 debt 2253862 pnl -467452 equity 1915772 capex 1062489; "
                        "FOI ready omzet 70 empty / 60-61 empty / 1.06m GFT / 2.25m debt; "
                        "distinct from already-mined ILvA 1344 prefix ilva and Fluvius OV 1391 / Riobra 1390 / DNB stack 1382-1389"
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
                    "title": "IVLA JR2025 leftover IGS dual (assets 4.17m / omzet unpublished / GFT capex 1.06m / debt 2.25m / PnL -467k)",
                    "entity_id": ENT,
                    "beneficiary": "IVLA / " + VENNOTEN,
                    "legal_basis": "WVV OV; Decreet Lokaal Bestuur; NBB neerlegging",
                    "decision_date": "2026-06-29",
                    "start_year": "1986",
                    "end_year": "",
                    "total_envelope_eur": "1062489",
                    "cash_by_year": "",
                    "remaining_eur": "",
                    "status": "active",
                    "evaluation_url": SRC_URL,
                    "stated_goal": "Local leftover IGS map VL waste OV — omzet unpublished (VKT 70 empty) / GFT capex 1.06m / debt 2.25m / PnL -467k",
                    "cut_option": "Publish unpublished omzet 70 + 60/61 + 1.06m GFT tender/unit price + 2.25m debt counterparties; do not keep waste IGS as dual unpublished vehicle",
                    "source_id": SRC,
                    "confidence": "strong",
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "notes": "tick1392; assets 4169634 brutomarge 7353 omzet unpublished pers 399515 debt 2253862 pnl -467452 equity 1915772 capex 1062489; FOI ready not sent; not TE-additive of 348bn",
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
                    "name": "IVLA JR2025 leftover IGS: assets 4.17m / omzet unpublished / GFT capex 1.06m / debt 2.25m / PnL -467k / 4 VTE",
                    "level": "L5",
                    "type": "local_budget_line",
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "annual_cost_eur": "399515",
                    "total_cost_eur": "1062489",
                    "tco_notes": (
                        "Leftover dual IGS waste OV (9 Vlaamse Ardennen municipalities): "
                        "assets 4.17m / equity 1.92m / pnl -467k / omzet unpublished (VKT 70 empty) / "
                        "brutomarge 7.4k DROP / pers 0.40m / 4 VTE / debt 2.25m / GFT capex 1.06m / cash 1.22m DROP; "
                        "official NBB WVV live; do not treat 1.06m as TE-additive of 348bn"
                    ),
                    "confidence": "strong",
                    "source_id": SRC,
                    "beneficiaries": "IVLA / " + VENNOTEN,
                    "stated_goal": "Local leftover IGS map VL waste OV — JR2025 live; dual omzet-empty/GFT/debt FOI",
                    "measured_outcome": "Official NBB WVV 2026-08-19: assets 4.17m / omzet unpublished / GFT capex 1.06m / debt 2.25m / pnl -467k / 4 VTE",
                    "absurdity_score": "6.5",
                    "cost_score": "4.0",
                    "difficulty": "3.0",
                    "priority_index": "5.5",
                    "cut_proposal": "Publish unpublished omzet 70 + 60/61 + 1.06m GFT tender/unit price + 2.25m debt counterparties; do not keep waste IGS as dual unpublished vehicle",
                    "status": "active",
                    "struck_reason": "",
                    "notes": "tick1392; leftover IVLA waste IGS; FOI ready not sent; not TE-additive of 348bn; distinct from ILvA 1344 and Fluvius OV 1391 / DNB stack 1382-1390",
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
                        "omzet WVV 70 empty + 60/61 empty (abbreviated VKT; only brutomarge 7353 vs 555793 published) per stroom/vennoot unpublished "
                        "+ GFT-container aanschaf 1062489 (8169; machines JUMP 1269295 vs 284589) tender/unit price unpublished "
                        "+ schulden 2253862 vs 1419846 (no LT; leveranciers 1467246 + deferred 484129 JUMP) counterparties unpublished "
                        "+ pers 399515 / 4 VTE / 7642 uur (inzameling uitbesteed?) "
                        "+ overige ST vorderingen 481109 JUMP vs 72767 unpublished "
                        "+ cash DROP 1224728 vs 2418359 unpublished "
                        "+ 6.6 related empty + commissarisverslag p23-27 image-only + dividend 694 empty"
                    ),
                    "why_it_matters": (
                        "Leftover IGS waste OV of 9 mined Vlaamse Ardennen municipalities "
                        "(distinct from ILvA 1344 and from Fluvius 1382-1391): "
                        "4.17m assets / omzet unpublished / 1.06m GFT capex / 2.25m debt / -467k PnL / "
                        "abbreviated VKT hides 70 and 60/61 "
                        "is a dual opacity residual, not TE-additive of 348bn."
                    ),
                    "priority": "8",
                    "recipient_body": "IVLA / Raad van Bestuur / Patrice Dutranoit / Delphine Bogaert / David Vandekerkhove / 9 vennoten",
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
                        "tick1392 leftover IGS waste OV of 9 Vlaamse Ardennen municipalities after honest hunt; "
                        "live JR2025 official NBB WVV VKT-inb PDF now extracted (2.05MB 31p deposit 2026-00281193). "
                        "Fluvius OV already mined 1391 — skipped. Nine DNB holdings already mined 1382-1390 — skipped. "
                        "ILvA already mined 1344 — skipped. HAVICREM leftover next. "
                        "Dommelhof leftover Limburg EVA 0777.495.085 not re-probed once live IVLA extracted. "
                        "Otary RS Nuhma-adjacent fallback not taken. "
                        "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                    ),
                }
            ],
        )
        print("foi", n)

    if step in ("all", "rq"):
        rq_new = {
            "task_id": "rq_1392",
            "title": "IVLA JR2025 leftover dual residual",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "done",
            "hierarchy_target": "L5",
            "entity_id": ENT,
            "instructions": (
                "Completed: IVLA leftover IGS waste OV of 9 Vlaamse Ardennen municipalities after honest hunt; "
                "KBO 0228.618.706 Actief; live JR2025 official NBB WVV VKT-inb PDF (2.05MB 31p deposit 2026-00281193; commissaris A&C); "
                "sourced euros assets 4169634 / brutomarge 7353 / omzet unpublished / pers 399515 / debt 2253862 / pnl -467452 / capex 1062489; "
                "FOI ready omzet 70 empty / 60-61 empty / 1.06m GFT / 2.25m debt"
            ),
            "blocked_gap_id": GAP,
            "created_utc": "2026-08-19T03:35:00Z",
            "updated_utc": UTC,
            "notes": (
                "tick1392 IVLA leftover IGS waste residual; KBO 0228.618.706; "
                "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1393 residual dual L5 VL"
            ),
        }
        rq_spawn = {
            "task_id": "rq_1393",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
                "(prior 1255-1392 done including IVLA 1392 leftover waste IGS live NBB WVV / "
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
                "leftover IGS HAVICREM 0860.572.419 CDN 2026-00363711 now live — leftover next; "
                "leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; "
                "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
                "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
                "skip already-mined IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / ILvA 1344; "
                "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
                "ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick1392 after IVLA leftover waste IGS live NBB WVV; next residual dual L5 VL",
        }
        found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1392", rq_new, rq_spawn)
        print("research_queue 1392", found, "spawned_1393", spawned)

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
                    "last_unit_id": "rq_1392",
                    "ticks_completed": "1392",
                    "paused": "no",
                    "notes": (
                        "tick1392 IVLA leftover IGS waste residual; KBO 0228.618.706; "
                        "live JR2025 NBB WVV PDF; sourced euros assets 4169634 brutomarge 7353 omzet unpublished pers 399515 debt 2253862 pnl -467452 equity 1915772 capex 1062489; "
                        "FOI ready omzet 70 empty/1.06m GFT/2.25m debt; next rq_1393 residual dual L5 VL; continuous hole_fill"
                    ),
                }
            )
        print("loop_state ok")

    if step in ("all", "log"):
        log = ROOT / "loop_log.md"
        entry = (
            "### Tick 1392 - 2026-08-19 - rq_1392 IVLA / I.VL.A. dual residual leftover\n"
            "- Unit: IVLA / I.VL.A. / Intergemeentelijke Vereniging voor Beheer van Afvalstoffen Vlaamse Ardennen (leftover IGS opdrachthoudende vereniging / waste inzameling + recyclageparken of 9 mined Vlaamse Ardennen municipalities) after residual dual hunt (KBO **0228.618.706**; official ivla.be has bestuur/contact + GFT portal; live NBB WVV VKT-inb deposit **2026-00281193** PDF 2.05MB / 31p; AV **29.06.2026**; header **09.07.2026**; commissaris A & C Bedrijfsrevisor BV B00348 / 0461.238.562 / Mohammed Boumalek A02265 fee 6.250; Fiscovan NV 0449.881.446 boekhouding+jaarrekening). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; preferred leftover IGS with live CDN this tick). Distinct from already-mined ILvA 1344 (KBO 0862.014.551; prefix `ilva`) and from Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / Fluvius EG group-level (entity fluvius). First confirmed not already mined: no IVLA / I.VL.A. / 0228.618.706 JR2025 extract in entities/sources (Ronse IGS FVA row only mentions IVLA reclass 1.40m — not a statutory extract). KBO Actief / normale toestand since **01.04.1986**; statutaire naam Intergemeentelijke Vereniging voor Beheer van Afvalstoffen Vlaamse Ardennen since 28.12.2004; afkorting I.VL.A. since 01.04.1986; Opdrachthoudende vereniging (Vlaams Gewest) since 22.01.2007; zetel Markt 1 9700 Oudenaarde (Stadhuis) since 01.04.1986; **1 VE**; KBO no email/web/tel; official site https://www.ivla.be/; btw since 01.04.1986; RSZ since 01.01.2022; NACE 81.230/38.110. Voorzitter Patrice Dutranoit; 1e ondervoorzitter Delphine Bogaert; 2e ondervoorzitter David Vandekerkhove (ivla.be/bestuur). Operational address Meersbloem-Melden 46A 9700 Oudenaarde; info@ivla.be; infolijn 0800 90 270. Hunt leftover IGS with live CDN first: IVLA statutory CDN live this tick (HTTP 200 / 2052117 / 31p) — taken. HAVICREM CDN 2026-00363711 also live — leftover next. Fluvius OV already mined 1391 — skipped. Nine Fluvius DNB holdings already mined 1382-1390 — skipped. ILvA already mined 1344 — skipped. IMOG already mined 1369 — skipped. Leftover AGB/zorg/EVA/APB not taken once live IVLA extracted. Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live IVLA extracted. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. NBB consult skipped (403/SPA); euros extracted from the official VKT-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used. Commissarisverslag p23-27 image-only this extract. Not every-10 (next 1400).\n"
            "- EUR strong (primary official WVV VKT-inb; omzet 70 empty / 60/61 empty — abbreviated model only publishes brutomarge 9900; 6.2/6.3/6.5/6.7/7/9/10/14-17 not filed; 6.6 related empty): assets **4.169.634** (was 3.803.070); fixed **1.401.284** / MVA **1.400.432** (gebouwen **51.032**; machines **1.269.295 JUMP** vs 284.589; meubilair **29.724**; overige **50.382**); IVA fully depreciated 5.865; FVA **851**; current **2.768.350**; voorraden **41.890**; ST recv **1.461.428** (trade 980.319 / other **481.109 JUMP** vs 72.767); cash **1.224.728 DROP** vs 2.418.359; prepaid 40.305; equity **1.915.772** (inbreng 1.893.040 / 99.573 aandelen; reserves 189.354; overgedragen **−166.622**); voorzieningen empty; schulden **2.253.862** (no LT; ST **1.769.733** waarvan leveranciers **1.467.246** + tax 66.909 + soc 17.119 + other 218.221; deferred **484.129 JUMP** vs 72.769); brutomarge **7.353 DROP** vs 555.793; omzet **unpublished**; diensten **unpublished**; pers **399.515** / **4 VTE** / 7.642 uur / YE 4 (3 VT + 2 DT); afschr 63.215; expl **−461.317** vs +99.381; fin opbr 13.922; fin kosten 1.126; tax 18.931; PnL **−467.452** vs +109.402; dividend **0** (694 empty); onttrekking EV 57.527; capex aanschaf **1.062.489** (GFT-containers; continuity note 6.9); commissaris 6.250; bestuurders presentiegeld+KM **29.897**. Vennoten: Oudenaarde 27.375% / Ronse 24.184% / Brakel 13.773% / Zwalm 7.953% / Kruisem 6.527% / Maarkedal 6.339% / Lierde 6.166% / Wortegem-Petegem 5.802% / Horebeke 1.879% + ILVA 1 C + IMOG 1 C.\n"
            "- CSVs: sources+4/entities+1/budgets+47/commitments+1/leaderboard+1 + FOI ready `gap_ivla_omzet_empty_debt_2_25m_gft_1_06m_l5` (not sent); rq_1392=done; spawn rq_1393; ticks=1392.\n"
            "- Coverage: residual dual L5 (IVLA leftover waste IGS live WVV). Does **not** move L5 near-complete of EUR 347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs gemeente waste fees possible. No progress refresh (not every-10; next 1400).\n"
            "- Next: rq_1393 residual dual L5 VL JR2025 hole_fill (prefer leftover IGS HAVICREM 0860.572.419 CDN 2026-00363711 now live; leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover Nuhma daughters Otary RS only after leftover IGS/EVA/AGB; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / ILvA 1344).\n"
        )
        with log.open("a", encoding="utf-8") as f:
            f.write(entry)
        print("loop_log ok")
    print("tick1392 write", step, "done")


if __name__ == "__main__":
    main()

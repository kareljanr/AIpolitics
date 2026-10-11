# -*- coding: utf-8 -*-
"""Tick 1369 — leftover IMOG JR2025 official NBB WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10 (next every-10 is 1370).
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1369"
UTC = "2026-08-19T03:10:00Z"
ENT = "igs_imog"
HIER = "Vlaanderen>West-Vlaanderen>IGS>IMOG>ZuidWestVlaanderen"
GAP = "gap_imog_omzet_50_30m_diensten_34_11m_vooruit_6_60m_l5"
SRC = "src_imog_jr2025_nbb"
SRC2 = "src_imog_site"
SRC3 = "src_kbo_imog_0206848639"
SRC4 = "src_imog_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00123049.pdf"
SRC2_URL = "https://imog.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0206848639"
SRC4_URL = "https://imog.be/contact/"
FOI_EMAIL = "info@imog.be"
FOI_POSTAL = "Kortrijksesteenweg 264 8530 Harelbeke"
DRAFT = "docs/doge/foi/drafts/gap_imog_omzet_50_30m_diensten_34_11m_vooruit_6_60m_l5.md"
COMM = "comm_imog_jr2025_pnl"
LB = "lb_imog_omzet_50_30m_diensten_34_11m_vooruit_6_60m"


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
                "title": "IMOG jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00123049; AV 19.05.2026)",
                "url": SRC_URL,
                "publisher": "IMOG / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1369; official NBB VOL-inb PDF 471kB 49p deposit 2026-00123049 created 28.05.2026 neerlegging 28.05.2026; "
                    "leftover IGS OV of mined Zuid-West-Vlaanderen / Leiedal cities; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Callens Vandelanotte Theunissen BV B00003 / Inge Nuyttens A02514 18480 oordeel zonder voorbehoud; "
                    "6.4.1/6.5.1/6.15/6.17/6.18/6.20 not filed; 6.10 category empty; jaarverslag Cfr. website"
                ),
            },
            {
                "source_id": SRC2,
                "title": "IMOG official site (opdrachthoudende vereniging 11 Zuid-West-Vlaanderen gemeenten)",
                "url": SRC2_URL,
                "publisher": "Intergemeentelijke Maatschappij voor Openbare Gezondheid in Zuid-West-Vlaanderen",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1369; leftover IGS waste of mined Leiedal cities; "
                    "imog.be has no statutory JR2025 (VOL-inb 7 Cfr. website Imog); statutory 2025 balans is the NBB CDN deposit"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO IMOG 0206.848.639",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1369; KBO 0206.848.639 Actief / normale toestand since 09.09.1969; "
                    "statutaire naam Intergemeentelijke Maatschappij voor Openbare Gezondheid in Zuid-West-Vlaanderen since 18.12.2007; "
                    "afkorting I.M.O.G. since 09.09.1969; Opdrachthoudende vereniging (Vlaams Gewest) since 21.03.2003; "
                    "zetel Kortrijksesteenweg 264 8530 Harelbeke since 20.05.2025; 2 VE; "
                    "btw since 01.02.1978; RSZ since 01.01.2022; aanbestedende overheid since 09.09.1969; "
                    "jaarvergadering mei; boekjaar 31 december; "
                    "17 KBO-bestuurders; voorzitter Isabelle Degezelle; "
                    "no KBO email/web/tel; NACE 38.330/35.110/52.100/38.220/38.210"
                ),
            },
            {
                "source_id": SRC4,
                "title": "IMOG FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "IMOG",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1369; FOI info@imog.be / 0800 99 827 / fax 056 71 09 85; "
                    "Kortrijksesteenweg 264 8530 Harelbeke; no own KBO email/web/tel"
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
                "name_nl": "IMOG Intergemeentelijke Maatschappij voor Openbare Gezondheid in Zuid-West-Vlaanderen (leftover opdrachthoudende vereniging / IGS afval Zuid-West-Vlaanderen)",
                "name_fr": "IMOG Societe intercommunale de sante publique en Flandre occidentale du Sud (association chargee de mission residuelle / IGS dechets)",
                "name_en": "IMOG leftover South-West Flanders waste IGS (mission association)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://imog.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1369 leftover residual IGS OV of mined Leiedal / Zuid-West-Vlaanderen cities; "
                    "KBO 0206.848.639 Actief since 09.09.1969; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 71874597 omzet 50303598 diensten 34105306 pnl 4638; "
                    "FOI ready omzet 50.30m/diensten 34.11m/vooruit 6.60m"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_imog_assets_2025", ENT, "2025", "71874597", "2025 assets 71874597 VOL-inb 20/58; tick1369; primary official NBB WVV"),
        ("bud_imog_assets_2024", ENT, "2024", "64510281", "2024 assets 64510281 comparative; tick1369; primary official NBB WVV 20/58"),
        ("bud_imog_fixed_2025", ENT, "2025", "37866130", "2025 vaste activa 37866130 JUMP vs 29503844; tick1369; primary official NBB WVV 21/28"),
        ("bud_imog_immat_2025", ENT, "2025", "81430", "2025 immateriele VA 81430 vs 97372; tick1369; primary official NBB WVV 21"),
        ("bud_imog_mva_2025", ENT, "2025", "37771942", "2025 MVA 37771942 (gebouwen 8825391 + machines 20758748 + rollend 8183227 + leasing 4576); tick1369; primary official NBB WVV 22/27"),
        ("bud_imog_buildings_2025", ENT, "2025", "8825391", "2025 terreinen en gebouwen 8825391 aanschaf 1384419; tick1369; primary official NBB WVV 22"),
        ("bud_imog_machines_2025", ENT, "2025", "20758748", "2025 installaties/machines 20758748 aanschaf 4959342; tick1369; primary official NBB WVV 23"),
        ("bud_imog_rollend_2025", ENT, "2025", "8183227", "2025 meubilair/rollend 8183227 JUMP vs 3081872 after aanschaf 6138151; tick1369; primary official NBB WVV 24"),
        ("bud_imog_rollend_acq_2025", ENT, "2025", "6138151", "2025 aanschaf meubilair/rollend 6138151; tick1369; primary official NBB WVV 6.3.3 8163"),
        ("bud_imog_mach_acq_2025", ENT, "2025", "4959342", "2025 aanschaf machines 4959342; tick1369; primary official NBB WVV 6.3.2 8162"),
        ("bud_imog_leasing_2025", ENT, "2025", "4576", "2025 leasing MVA 4576 vs 10067; tick1369; primary official NBB WVV 25"),
        ("bud_imog_fva_2025", ENT, "2025", "12758", "2025 FVA 12758 (aandelen 4526 + borg 8231; 6.4.1/6.5.1 not filed); tick1369; primary official NBB WVV 28"),
        ("bud_imog_current_2025", ENT, "2025", "34008468", "2025 vlottende activa 34008468 vs 35006438; tick1369; primary official NBB WVV 29/58"),
        ("bud_imog_ltrecv_2025", ENT, "2025", "2190050", "2025 LT overige vorderingen 2190050; tick1369; primary official NBB WVV 291"),
        ("bud_imog_inv_2025", ENT, "2025", "2662737", "2025 voorraden grond-hulp 2662737; tick1369; primary official NBB WVV 30/31"),
        ("bud_imog_strecv_2025", ENT, "2025", "7375876", "2025 ST vorderingen 7375876 (trade 6628444 + other 747432); tick1369; primary official NBB WVV 40/41"),
        ("bud_imog_invest_2025", ENT, "2025", "0", "2025 geldbeleggingen 0 DROP vs 4940053 (6.6 8689); tick1369; primary official NBB WVV 50/53"),
        ("bud_imog_invest_2024", ENT, "2024", "4940053", "2024 geldbeleggingen 4940053 comparative; tick1369; primary official NBB WVV 50/53"),
        ("bud_imog_cash_2025", ENT, "2025", "20581515", "2025 liquide middelen 20581515 JUMP vs 17885018; tick1369; primary official NBB WVV 54/58"),
        ("bud_imog_cash_2024", ENT, "2024", "17885018", "2024 cash 17885018 comparative; tick1369; primary official NBB WVV 54/58"),
        ("bud_imog_prepaid_2025", ENT, "2025", "1198289", "2025 overlopend actief 1198289 (kosten 44761 + opbr 1153528); tick1369; primary official NBB WVV 490/1"),
        ("bud_imog_equity_2025", ENT, "2025", "20973508", "2025 eigen vermogen 20973508 vs 20397807; tick1369; primary official NBB WVV 10/15"),
        ("bud_imog_inbreng_2025", ENT, "2025", "10143151", "2025 inbreng 10143151 (beschikbaar 9893497 + onbeschikbaar 249654) / 409163 aandelen; tick1369; primary official NBB WVV 10/11"),
        ("bud_imog_reserves_2025", ENT, "2025", "5818907", "2025 reserves 5818907 (onbeschikbaar 4576556 + beschikbaar 1242351); tick1369; primary official NBB WVV 13"),
        ("bud_imog_capsub_2025", ENT, "2025", "3320837", "2025 kapitaalsubsidies 3320837 vs 2781753; tick1369; primary official NBB WVV 15"),
        ("bud_imog_prov_2025", ENT, "2025", "11851310", "2025 voorzieningen 11851310 (herstelling 2201500 + overige 9649810); tick1369; primary official NBB WVV 16"),
        ("bud_imog_repair_2025", ENT, "2025", "2201500", "2025 grote herstellingen 2201500 vs 2251500; tick1369; primary official NBB WVV 162"),
        ("bud_imog_othprov_2025", ENT, "2025", "9649810", "2025 overige risico's 9649810 (Moen 6798786 + responsabilisering 2776024 + overige 75000); tick1369; primary official NBB WVV 164/5 6.8"),
        ("bud_imog_moen_2025", ENT, "2025", "6798786", "2025 Masterplan Moen + afwerking stortplaats 6798786; tick1369; primary official NBB WVV 6.8"),
        ("bud_imog_pension_2025", ENT, "2025", "2776024", "2025 responsabiliseringsbijdragen 2776024 verdisconteerd tot 2052 Belfius; tick1369; primary official NBB WVV 6.8 6.14"),
        ("bud_imog_debt_2025", ENT, "2025", "39049779", "2025 schulden 39049779 JUMP vs 31761273; tick1369; primary official NBB WVV 17/49"),
        ("bud_imog_lt_2025", ENT, "2025", "15610642", "2025 LT schulden 15610642 (bank 14863272 + overige 747370); tick1369; primary official NBB WVV 17"),
        ("bud_imog_ltbank_2025", ENT, "2025", "14863272", "2025 LT kredietinstellingen 14863272; tick1369; primary official NBB WVV 173"),
        ("bud_imog_st_2025", ENT, "2025", "23217880", "2025 ST schulden 23217880 JUMP vs 12666098; tick1369; primary official NBB WVV 42/48"),
        ("bud_imog_stbank_2025", ENT, "2025", "1138569", "2025 ST financieel kredietinstellingen 1138569; tick1369; primary official NBB WVV 43"),
        ("bud_imog_sttrade_2025", ENT, "2025", "9893440", "2025 leveranciers 9893440 JUMP vs 5523241; tick1369; primary official NBB WVV 440/4"),
        ("bud_imog_vooruit_2025", ENT, "2025", "6604624", "2025 vooruitbetalingen 6604624 JUMP vs 629740; tick1369; primary official NBB WVV 46"),
        ("bud_imog_vooruit_2024", ENT, "2024", "629740", "2024 vooruitbetalingen 629740 comparative; tick1369; primary official NBB WVV 46"),
        ("bud_imog_govg_2025", ENT, "2025", "5578751", "2025 door Belgische overheden gewaarborgde schulden 5578751; tick1369; primary official NBB WVV 6.9 9061"),
        ("bud_imog_offg_2025", ENT, "2025", "19957275", "2025 buitenbalans leningen gewaarborgd door deelnemende lokale besturen 19957275; tick1369; primary official NBB WVV 6.14"),
        ("bud_imog_bankw_2025", ENT, "2025", "2283223", "2025 bankwaarborgen 2283223 (OVAM Moen 980739+1295597); tick1369; primary official NBB WVV 6.14 6.19"),
        ("bud_imog_ops_2025", ENT, "2025", "53945954", "2025 bedrijfsopbrengsten 53945954; tick1369; primary official NBB WVV 70/76A"),
        ("bud_imog_omzet_2025", ENT, "2025", "50303598", "2025 omzet 50303598; 6.10 geo only BE 50248530 / EU 55068; category empty; tick1369; primary official NBB WVV 70"),
        ("bud_imog_omzet_2024", ENT, "2024", "46173743", "2024 omzet 46173743 comparative; tick1369; primary official NBB WVV 70"),
        ("bud_imog_othops_2025", ENT, "2025", "2641749", "2025 andere bedrijfsopbrengsten 2641749 waarvan subsidies 662261 only (~1979488 unnamed); tick1369; primary official NBB WVV 74"),
        ("bud_imog_sub_2025", ENT, "2025", "662261", "2025 exploitatiesubsidies/overheidscompensatie 662261 vs 385214; tick1369; primary official NBB WVV 740"),
        ("bud_imog_nrops_2025", ENT, "2025", "1000607", "2025 niet-recurrente bedrijfsopbrengsten 1000607 (meerwaarde MVA 669333 + andere 331273); tick1369; primary official NBB WVV 76A 6.12"),
        ("bud_imog_diensten_2025", ENT, "2025", "34105306", "2025 diensten 34105306 (67.8pct of omzet); tick1369; primary official NBB WVV 61"),
        ("bud_imog_goods_2025", ENT, "2025", "963073", "2025 handelsgoederen/grond-hulp 963073; tick1369; primary official NBB WVV 60"),
        ("bud_imog_pers_2025", ENT, "2025", "13117675", "2025 bezoldigingen 13117675 / 170 VTE / 181 koppen vs sociale balans 11275446; tick1369; primary official NBB WVV 62 9087"),
        ("bud_imog_uitzend_2025", ENT, "2025", "440856", "2025 uitzend 440856 / 6.8 VTE; tick1369; primary official NBB WVV 617 9097"),
        ("bud_imog_deprec_2025", ENT, "2025", "4123188", "2025 afschrijvingen 4123188; tick1369; primary official NBB WVV 630"),
        ("bud_imog_expl_2025", ENT, "2025", "123588", "2025 bedrijfswinst 123588 vs -1661424; tick1369; primary official NBB WVV 9901"),
        ("bud_imog_expl_2024", ENT, "2024", "-1661424", "2024 bedrijfsverlies 1661424 comparative; tick1369; primary official NBB WVV 9901"),
        ("bud_imog_fininc_2025", ENT, "2025", "433189", "2025 financiele opbrengsten 433189 (vlottende 87913 + andere 345268 waarvan capsub 110916); tick1369; primary official NBB WVV 75"),
        ("bud_imog_fincost_2025", ENT, "2025", "541907", "2025 financiele kosten 541907 (schulden 543058); tick1369; primary official NBB WVV 65"),
        ("bud_imog_pnl_2025", ENT, "2025", "4638", "2025 PnL 9904 4638 vs -1575501; added to overgedragen; tick1369; primary official NBB WVV"),
        ("bud_imog_pnl_2024", ENT, "2024", "-1575501", "2024 PnL -1575501 comparative; tick1369; primary official NBB WVV 9904"),
        ("bud_imog_comm_2025", ENT, "2025", "18480", "2025 commissaris Callens Vandelanotte Nuyttens 18480; tick1369; primary official NBB WVV 9505"),
        ("bud_imog_board_2025", ENT, "2025", "61638", "2025 bestuurders presentiegeld 61638 + km 2465 = 64103 (9503 empty); tick1369; primary official remunatieverslag p48-49"),
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
                "title": "IMOG JR2025 leftover IGS dual (assets 71.87m / omzet 50.30m / diensten 34.11m / vooruit 6.60m / PnL 4.6k)",
                "entity_id": ENT,
                "beneficiary": "IMOG / 11 Zuid-West-Vlaanderen municipalities / OVAM Moen",
                "legal_basis": "WVV OV; decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-05-19",
                "start_year": "1969",
                "end_year": "2026",
                "total_envelope_eur": "71874597",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL waste — 50.30m omzet / 34.11m diensten / 6.60m vooruit / 6.80m Moen",
                "cut_option": "Publish 34.11m diensten counterparties + 6.60m vooruit project list + 6.10 category + Masterplan Moen 6.80m + 19.96m gemeentegarantie + site-JR; do not keep 71.87m municipal waste IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1369; assets 71874597 omzet 50303598 diensten 34105306 pnl 4638; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "IMOG JR2025 leftover IGS: assets 71.87m / omzet 50.30m / diensten 34.11m / vooruit 6.60m / PnL 4.6k",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "34105306",
                "total_cost_eur": "71874597",
                "tco_notes": (
                    "Leftover dual IGS OV of mined Leiedal / Zuid-West-Vlaanderen municipalities: "
                    "assets 71.87m / equity 20.97m / pnl 4.6k / omzet 50.30m / 170 VTE / "
                    "diensten 34.11m (67.8pct of omzet) / vooruit 6.60m JUMP / "
                    "Masterplan Moen 6.80m / official NBB WVV live; "
                    "do not treat 71.87m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "IMOG / 11 Zuid-West-Vlaanderen municipalities",
                "stated_goal": "Local leftover IGS map VL waste — JR2025 live; dual diensten/vooruit/Moen FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 71.87m / omzet 50.30m / diensten 34.11m / pnl 4.6k; vooruit 6.60m JUMP; Moen 6.80m",
                "absurdity_score": "7.3",
                "cost_score": "7.5",
                "difficulty": "2.5",
                "priority_index": "6.9",
                "cut_proposal": "Publish 34.11m diensten counterparties + 6.60m vooruit project list + 6.10 category + Masterplan Moen 6.80m + 19.96m gemeentegarantie + site-JR; do not keep 71.87m municipal waste IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1369; leftover IGS OV of mined Leiedal cities; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "6.10 omzet 50303598 category split empty (geo only BE 50248530 / EU 55068) + per-gemeente/verbranding/recyclagepark counterparties "
                    "+ diensten 34105306 (67.8pct of omzet) top-tegenpartijen "
                    "+ vooruitbetalingen 6604624 JUMP vs 629740 project list "
                    "+ leveranciers 9893440 JUMP vs 5523241 "
                    "+ andere bedrijfsopbrengsten 2641749 of which subsidies 662261 only (~1979488 unnamed) "
                    "+ niet-recurrente 1000607 (meerwaarde MVA 669333 + andere 331273 unnamed) "
                    "+ Masterplan Moen stortplaats 6798786 + responsabilisering 2776024 tot 2052 Belfius "
                    "+ buitenbalans gemeentegaranties 19957275 vs 6.9 overheidsgarantie 5578751 "
                    "+ pers 13117675 vs sociale balans 11275446 "
                    "+ 6.4.1/6.5.1/6.15/6.18 not filed "
                    "+ 409163 aandelen / per-vennoot inleg/stem empty "
                    "+ official-site JR (VOL-inb 7 Cfr. website Imog; site has none) "
                    "+ 9503 bestuurders empty vs remunatieverslag 61638"
                ),
                "why_it_matters": (
                    "Leftover IGS OV of mined Zuid-West-Vlaanderen / Leiedal cities "
                    "(same leftover-IGS seam as Leiedal 1367 / Interleuven 1366 / IOK 1368 / Interwaas 1350 / SOLVA 1351 / IGEAN 1341 / EcoWerf 1357 / IVBO 1352): "
                    "71.87m assets / 50.30m omzet / 34.11m diensten / 4.6k pnl / 170 VTE / "
                    "6.60m vooruit JUMP / 6.80m Masterplan Moen / 19.96m gemeentegarantie / site-JR missing "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "IMOG / Isabelle Degezelle / 11 Zuid-West-Vlaanderen municipalities",
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
                    "tick1369 leftover IGS OV of mined Leiedal / Zuid-West-Vlaanderen cities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (471kB 49p deposit 2026-00123049). "
                    "IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Interleuven already mined 1366 — skipped. "
                    "Nuhma-group seam 1353-1365 skipped. "
                    "Dommelhof leftover Limburg EVA still no 2025/2026 PDF. "
                    "Otary RS Nuhma-adjacent fallback not taken. "
                    "Haviland 2026-00188817 / Veneco 2026-00188751 / IGEMO 2026-00235028 / IVOO 2026-00271895 / MIWA 2026-00209388 2025 CDN now live — leftover next. "
                    "IVAREM still 2024. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1369",
        "title": "IMOG OV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: IMOG leftover IGS OV of mined Leiedal / Zuid-West-Vlaanderen cities "
            "after honest hunt; KBO 0206.848.639 Actief; "
            "live JR2025 official NBB WVV VOL-inb PDF (471kB 49p deposit 2026-00123049; commissaris Callens Vandelanotte Nuyttens); "
            "sourced euros assets 71874597 / omzet 50303598 / diensten 34105306 / pnl 4638; "
            "FOI ready omzet 50.30m/diensten 34.11m/vooruit 6.60m"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T02:20:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1369 IMOG leftover IGS residual; KBO 0206.848.639; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1370 every-10 then residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1370",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "EVERY-10 FIRST (ticks_completed will be 1370): refresh progress_every_10_ticks.md + doge_waste_top10_current.md from on-disk CSVs, then ONE residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1369 done including IMOG 1369 leftover IGS live NBB WVV / "
            "IOK 1368 leftover IGS live NBB WVV / "
            "Leiedal 1367 leftover IGS live NBB WVV / "
            "Interleuven 1366 leftover IGS live NBB WVV / "
            "s-Lim DV 1365 leftover IGS live NBB WVV / "
            "Herkenrode RE NV 1364 leftover vastgoed live NBB WVV / "
            "MyCSN NV 1363 leftover smart-city live NBB WVV / "
            "s-Lim CV 1362 leftover smart-city live NBB WVV / "
            "Nuhmeris NV 1361 leftover klimaat-holding live NBB WVV / "
            "ECO2050 cv 1360 leftover klimaat-coop live NBB WVV + every-10 / "
            "Nubema NV 1359 leftover klimaat-holding live NBB WVV / "
            "NUHMA DC BV 1358 leftover klimaat-holding live NBB WVV / "
            "EcoWerf 1357 leftover IGS live NBB WVV / "
            "Nuhma cv 1356 leftover klimaat-holding live NBB WVV / "
            "NUHMA AC NV 1355 leftover klimaat-holding live NBB WVV / "
            "Bionerga NV 1354 leftover waste-processing live NBB WVV / "
            "Limburg.net 1353 leftover IGS glossy-only FOI / IVBO 1352 leftover IGS live WVV / "
            "SOLVA 1351 leftover IGS live JR / Interwaas 1350 leftover IGS live WVV + every-10); "
            "Haviland leftover IGS KBO 0200.881.951 — take if JR2025 CDN 2026-00188817 still live (1.73MB HEAD this tick, not taken once IMOG extracted); "
            "Veneco leftover IGS KBO 0200.065.765 CDN 2026-00188751 (24.1MB) / IGEMO KBO 0213.349.124 CDN 2026-00235028 (944kB) / IVOO KBO 0214.753.050 CDN 2026-00271895 (1.56MB) / MIWA KBO 0218.239.409 CDN 2026-00209388 (480kB) — take only if still live; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if a new live 2025 WVV PDF downloads (prefer leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; Otary CDN 2026-00254280 live this tick, not taken); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1369 after IMOG leftover IGS live NBB WVV; next every-10 is 1370 then residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1369", rq_new, rq_spawn)
    print("research_queue 1369", found, "spawned_1370", spawned)

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
                "last_unit_id": "rq_1369",
                "ticks_completed": "1369",
                "paused": "no",
                "notes": (
                    "tick1369 IMOG leftover IGS residual; KBO 0206.848.639; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 71874597 omzet 50303598 diensten 34105306 pnl 4638; "
                    "FOI ready omzet 50.30m/diensten 34.11m/vooruit 6.60m; next rq_1370 every-10 then residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1369 - 2026-08-19 - rq_1369 IMOG dual residual leftover
- Unit: Intergemeentelijke Maatschappij voor Openbare Gezondheid in Zuid-West-Vlaanderen / IMOG (leftover opdrachthoudende vereniging / IGS waste of mined Zuid-West-Vlaanderen municipalities: Anzegem / Avelgem / Deerlijk / Harelbeke / Kortrijk / Kruisem / Kuurne / Spiere-Helkijn / Waregem / Wielsbeke / Zwevegem; 409.163 aandelen op naam) after residual dual hunt (KBO **0206.848.639**; official imog.be has no statutory JR — VOL-inb 7 **Cfr. website Imog**; live NBB WVV VOL-inb deposit **2026-00123049** PDF 471kB / 49p; AV **19.05.2026**; PDF created **28.05.2026**; neerlegging SBM **28.05.2026**; commissaris Callens, Vandelanotte & Theunissen BV B00003 / Inge Nuyttens IBR A02514 18.480 oordeel zonder voorbehoud; 4e opeenvolgend boekjaar; mandaat tot YE 2027). Leftover IGS OV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; previous ticks listed IMOG as still 2024 as of 1367). Distinct from already-mined IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **09.09.1969**; statutaire naam Intergemeentelijke Maatschappij voor Openbare Gezondheid in Zuid-West-Vlaanderen since 18.12.2007; afkorting I.M.O.G. since 09.09.1969; Opdrachthoudende vereniging (Vlaams Gewest) since 21.03.2003; zetel Kortrijksesteenweg 264 8530 Harelbeke since 20.05.2025; **2 VE**; btw since 01.02.1978; RSZ since 01.01.2022; aanbestedende overheid since 09.09.1969; jaarvergadering mei; 17 KBO-bestuurders / voorzitter Isabelle Degezelle / ondervoorzitters Thomas Guillemyn + Wouter Allijns; e-mail info@imog.be; tel 0800 99 827; NACE 38.330/35.110/52.100/38.220/38.210. Hunt leftover AGB/zorg/EVA first: IMOG statutory CDN live this tick (HTTP 200 / 471076 / 49p) — taken (preferred leftover IGS outside Nuhma). IOK already mined 1368 — skipped; Leiedal already mined 1367 — skipped; Interleuven already mined 1366 — skipped; Nuhma-group seam 1353-1365 already mined — skipped; Dommelhof leftover Limburg EVA KBO 0777.495.085 still no 2025/2026 jaarrekening on Staatsbladmonitor — skipped. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. Haviland 2026-00188817 (1.73MB) / Veneco 2026-00188751 (24.1MB) / IGEMO 2026-00235028 (944kB) / IVOO 2026-00271895 (1.56MB) / MIWA 2026-00209388 (480kB) 2025 CDN now live — leftover next, not taken once live IMOG extracted. IVAREM still 2024. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350. Not every-10 (next 1370).
- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud assets 71.874.597 / PnL 4.638; 6.4.1/6.5.1/6.15/6.17/6.18/6.20 not filed; 6.10 category empty; 9503 empty): assets **71.874.597** (was 64.510.281); fixed **37.866.130** JUMP vs 29.503.844 / MVA **37.771.942** (gebouwen **8.825.391** aanschaf 1.384.419 + machines **20.758.748** aanschaf **4.959.342** + rollend **8.183.227 JUMP** vs 3.081.872 after aanschaf **6.138.151** + leasing 4.576); immaterieel 81.430; FVA **12.758**; current **34.008.468**; LT recv 2.190.050; inventory grond-hulp **2.662.737**; ST recv **7.375.876** (trade 6.628.444); beleggingen **0 DROP** vs 4.940.053; cash **20.581.515 JUMP** vs 17.885.018; prepaid 1.198.289 (opbr 1.153.528); equity **20.973.508** (inbreng 10.143.151 / 409.163 aandelen; actualisering 31.979; reserves 5.818.907; kapitaalsubsidies **3.320.837**); voorzieningen **11.851.310** (herstelling 2.201.500 + overige **9.649.810**: Masterplan Moen **6.798.786** + responsabilisering **2.776.024** tot 2052 Belfius + 75.000); schulden **39.049.779 JUMP** vs 31.761.273 (LT bank **14.863.272**; ST **23.217.880** waarvan bank 1.138.569 + leveranciers **9.893.440 JUMP** vs 5.523.241 + vooruit **6.604.624 JUMP** vs 629.740); 6.9 overheidsgarantie **5.578.751** vs buitenbalans gemeentegaranties **19.957.275** + bankwaarborgen 2.283.223 (OVAM Moen); omzet **50.303.598** (6.10 geo BE 50.248.530 / EU 55.068; category empty; comparative 46.173.743); andere opbr **2.641.749** (subsidies 662.261 only; ~1.979.488 unnamed); nr-opbr **1.000.607** (meerwaarde MVA 669.333 + andere 331.273); goods 963.073; diensten **34.105.306** (67,8% of omzet); pers **13.117.675** / **170 VTE** / 181 koppen vs sociale balans 11.275.446 / avg 160,3 VTE; uitzend 440.856 / 6,8 VTE; afschr 4.123.188; expl **123.588** vs −1.661.424; fin opbr 433.189; fin kosten 541.907; PnL **4.638** vs −1.575.501 toegevoegd aan overgedragen; bestuurders presentiegeld **61.638** + km 2.465 = 64.103 (9503 empty); commissaris 18.480.
- CSVs: sources+4/entities+1/budgets+61/commitments+1/leaderboard+1 + FOI ready `gap_imog_omzet_50_30m_diensten_34_11m_vooruit_6_60m_l5` (not sent); rq_1369=done; spawn rq_1370; ticks=1369.
- Coverage: residual dual L5 (IMOG leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1370).
- Next: rq_1370 **every-10 progress first** then residual dual L5 VL JR2025 hole_fill (prefer leftover Haviland KBO 0200.881.951 CDN 2026-00188817 if still live; leftover Veneco 0200.065.765 CDN 2026-00188751 / IGEMO 0213.349.124 CDN 2026-00235028 / IVOO 0214.753.050 CDN 2026-00271895 / MIWA 0218.239.409 CDN 2026-00209388 only if still live; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS CDN 2026-00254280 / Rematics / Sunfin only if taken after leftover IGS; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; IVAREM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1369 write done")


if __name__ == "__main__":
    main()

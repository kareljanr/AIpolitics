# -*- coding: utf-8 -*-
"""Tick 1379 — leftover ISVAG JR2025 official NBB WVV euros.
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

TICK = "1379"
UTC = "2026-08-19T05:40:00Z"
ENT = "igs_isvg"
HIER = "Vlaanderen>Antwerpen>IGS>ISVAG"
GAP = "gap_isvg_omzet_29_44m_diensten_14_73m_permit_l5"
SRC = "src_isvg_jr2025_nbb"
SRC2 = "src_isvg_site"
SRC3 = "src_kbo_isvg_0214981001"
SRC4 = "src_isvg_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00182993.pdf"
SRC2_URL = "https://isvag.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0214981001"
SRC4_URL = "https://isvag.be/informatie/"
FOI_EMAIL = "info@isvag.be"
FOI_POSTAL = "Boomsesteenweg 1000 2610 Wilrijk"
DRAFT = "docs/doge/foi/drafts/gap_isvg_omzet_29_44m_diensten_14_73m_permit_l5.md"
COMM = "comm_isvg_jr2025_pnl"
LB = "lb_isvg_omzet_29_44m_diensten_14_73m_permit"


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
                "title": "ISVAG jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00182993; AV 18.06.2026)",
                "url": SRC_URL,
                "publisher": "ISVAG / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1379; official NBB VOL-inb PDF 308kB 48p deposit 2026-00182993 created 22.06.2026 header 19.06.2026 neerlegging 23.06.2026; "
                    "leftover IGS waste incinerator of mined Antwerp-region municipalities; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Grant Thornton 0439.814.826 / Stefaan De Coninck 25675; "
                    "oordeel zonder voorbehoud assets 42718614 / PnL -1492829 + benadrukking VOL-inb 6.19 permit beroep; "
                    "VOL-inb 6.1/6.2/6.8/6.15/6.17/6.18/6.20/9 not filed; omzet 6.10 category/geo empty; subsidies 740 empty; not every-10"
                ),
            },
            {
                "source_id": SRC2,
                "title": "ISVAG official site (leftover IGS afvalenergiecentrale Wilrijk / 29 gemeenten)",
                "url": SRC2_URL,
                "publisher": "ISVAG",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1379; leftover IGS of mined Antwerp-region municipalities; 29 steden en gemeenten; "
                    "statutory 2025 balans is the NBB CDN deposit; contact info@isvag.be / +32 3 877 28 55"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO ISVAG 0214.981.001",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1379; KBO 0214.981.001 Actief / normale toestand since 17.01.1975; "
                    "statutaire naam Intercommunale voor Slib- en Vuilverwijdering van Antwerpse Gemeenten since 17.01.1975; "
                    "afkorting I.S.V.A.G. since 17.01.1975; Opdrachthoudende vereniging since 11.12.2003; "
                    "zetel Boomsesteenweg 1000 2610 Antwerpen since 28.12.1995; 1 VE; "
                    "btw since 01.09.1997; RSZ since 01.01.2022; aanbestedende overheid since 17.01.1975; "
                    "KBO kapitaal 25000; jaarvergadering mei; boekjaar 31 december; NACE 38.330/38.210"
                ),
            },
            {
                "source_id": SRC4,
                "title": "ISVAG FOI channel / official contact + informatiepagina",
                "url": SRC4_URL,
                "publisher": "ISVAG",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1379; FOI info@isvag.be / communicatie@isvag.be / +32 3 877 28 55; "
                    "Boomsesteenweg 1000 2610 Wilrijk; official site lists jaarverslagen but statutory 2025 is the NBB CDN"
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
                "name_nl": "ISVAG (leftover IGS afvalenergiecentrale Antwerpse gemeenten / I.S.V.A.G.)",
                "name_fr": "ISVAG (intercommunale residuelle d'incineration Anvers)",
                "name_en": "ISVAG leftover IGS waste-to-energy Antwerp municipalities",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://isvag.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1379 leftover residual IGS of mined Antwerp-region municipalities; "
                    "KBO 0214.981.001 Actief since 17.01.1975; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 42718614 omzet 29439548 diensten 14728199 pers 7056785 pnl -1492829 equity 32073522; "
                    "FOI ready omzet 6.10 empty / 14.73m 61 / permit beroep"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_isvg_assets_2025", ENT, "2025", "42718614", "2025 assets 42718614 VOL-inb 20/58; tick1379; primary official NBB WVV; commissaris 42718614"),
        ("bud_isvg_assets_2024", ENT, "2024", "46749415", "2024 assets 46749415 comparative; tick1379; primary official NBB WVV 20/58"),
        ("bud_isvg_fixed_2025", ENT, "2025", "12309395", "2025 vaste activa 12309395 vs 12822030; tick1379; primary official NBB WVV 21/28"),
        ("bud_isvg_mva_2025", ENT, "2025", "12308949", "2025 MVA 12308949 vs 12821852; tick1379; primary official NBB WVV 22/27"),
        ("bud_isvg_buildings_2025", ENT, "2025", "2757772", "2025 terreinen/gebouwen 2757772 vs 2765205; tick1379; primary official NBB WVV 22"),
        ("bud_isvg_machines_2025", ENT, "2025", "9251115", "2025 installaties/machines 9251115 vs 9743799; aanschaf year 1095443; tick1379; primary official NBB WVV 23"),
        ("bud_isvg_furniture_2025", ENT, "2025", "300062", "2025 meubilair/rollend 300062 vs 312848; tick1379; primary official NBB WVV 24"),
        ("bud_isvg_fva_2025", ENT, "2025", "446", "2025 FVA 446 vs 178 (aandelen 284); tick1379; primary official NBB WVV 28"),
        ("bud_isvg_current_2025", ENT, "2025", "30409219", "2025 vlottende activa 30409219 vs 33927385; tick1379; primary official NBB WVV 29/58"),
        ("bud_isvg_ltrecv_2025", ENT, "2025", "21600", "2025 LT overige vorderingen 21600 vs 0; tick1379; primary official NBB WVV 291"),
        ("bud_isvg_inv_2025", ENT, "2025", "1178211", "2025 voorraden 1178211 vs 957624 (grond/hulp 10pct traag-roterend); tick1379; primary official NBB WVV 3"),
        ("bud_isvg_strecv_2025", ENT, "2025", "2908233", "2025 ST vorderingen 2908233 vs 2519673; tick1379; primary official NBB WVV 40/41"),
        ("bud_isvg_trade_2025", ENT, "2025", "2905146", "2025 handelsvorderingen 2905146 vs 2500139; tick1379; primary official NBB WVV 40"),
        ("bud_isvg_invest_2025", ENT, "2025", "21865510", "2025 geldbeleggingen 21865510 vs 19007457 (vastrentende effecten 52); tick1379; primary official NBB WVV 50/53"),
        ("bud_isvg_cash_2025", ENT, "2025", "4145068", "2025 liquide middelen 4145068 DROP vs 11137685; tick1379; primary official NBB WVV 54/58"),
        ("bud_isvg_cash_2024", ENT, "2024", "11137685", "2024 liquide middelen 11137685 comparative; tick1379; primary official NBB WVV 54/58"),
        ("bud_isvg_prepaid_2025", ENT, "2025", "290597", "2025 overlopend actief 290597 (over te dragen 246593 + verworven 44004); tick1379; primary official NBB WVV 490/1"),
        ("bud_isvg_equity_2025", ENT, "2025", "32073522", "2025 eigen vermogen 32073522 vs 33630737; tick1379; primary official NBB WVV 10/15"),
        ("bud_isvg_equity_2024", ENT, "2024", "33630737", "2024 eigen vermogen 33630737 comparative; tick1379; primary official NBB WVV 10/15"),
        ("bud_isvg_inbreng_2025", ENT, "2025", "4909965", "2025 inbreng 4909965 (beschikbaar 2269140 + onbeschikbaar 2640825); tick1379; primary official NBB WVV 10/11"),
        ("bud_isvg_reserves_2025", ENT, "2025", "39640412", "2025 reserves 39640412 (beschikbaar 39376329); tick1379; primary official NBB WVV 13"),
        ("bud_isvg_retained_2025", ENT, "2025", "-14449352", "2025 overgedragen verlies -14449352 vs -12956523; tick1379; primary official NBB WVV 14"),
        ("bud_isvg_capsib_2025", ENT, "2025", "1684288", "2025 kapitaalsubsidies 1684288 vs 1748674; tick1379; primary official NBB WVV 15"),
        ("bud_isvg_prov_2025", ENT, "2025", "6025192", "2025 voorzieningen 6025192 JUMP vs 4675192 (all 164/5 overige; pens 160 empty); tick1379; primary official NBB WVV 16"),
        ("bud_isvg_prov_2024", ENT, "2024", "4675192", "2024 voorzieningen 4675192 comparative; tick1379; primary official NBB WVV 16"),
        ("bud_isvg_debt_2025", ENT, "2025", "4619900", "2025 schulden 4619900 vs 8443486; LT 17 empty; tick1379; primary official NBB WVV 17/49"),
        ("bud_isvg_debt_2024", ENT, "2024", "8443486", "2024 schulden 8443486 comparative; tick1379; primary official NBB WVV 17/49"),
        ("bud_isvg_st_2025", ENT, "2025", "4351886", "2025 ST schulden 4351886 vs 8188353; tick1379; primary official NBB WVV 42/48"),
        ("bud_isvg_sttrade_2025", ENT, "2025", "3430158", "2025 leveranciers 3430158 vs 7085709; tick1379; primary official NBB WVV 440/4"),
        ("bud_isvg_sttax_2025", ENT, "2025", "257748", "2025 belastingen 257748 vs 382111; tick1379; primary official NBB WVV 450/3"),
        ("bud_isvg_stsoc_2025", ENT, "2025", "663480", "2025 bezoldigingen/sociale lasten 663480 vs 720533; tick1379; primary official NBB WVV 454/9"),
        ("bud_isvg_accrued_2025", ENT, "2025", "268014", "2025 overlopend passief 268014 vs 255133; tick1379; primary official NBB WVV 492/3"),
        ("bud_isvg_opsinc_2025", ENT, "2025", "29583006", "2025 bedrijfsopbrengsten 29583006 vs 26342664; tick1379; primary official NBB WVV 70/76A"),
        ("bud_isvg_omzet_2025", ENT, "2025", "29439548", "2025 omzet 29439548 JUMP vs 25215937; 6.10 category/geo empty; tick1379; primary official NBB WVV 70"),
        ("bud_isvg_omzet_2024", ENT, "2024", "25215937", "2024 omzet 25215937 comparative (partial year closure); tick1379; primary official NBB WVV 70"),
        ("bud_isvg_othops_2025", ENT, "2025", "136188", "2025 andere bedrijfsopbrengsten 136188 DROP vs 961884; subsidies 740 empty; tick1379; primary official NBB WVV 74"),
        ("bud_isvg_nrec_2025", ENT, "2025", "7270", "2025 niet-recurrente bedrijfsopbrengsten 7270 vs 164843; tick1379; primary official NBB WVV 76A"),
        ("bud_isvg_opscost_2025", ENT, "2025", "31375348", "2025 bedrijfskosten 31375348 vs 34520486; tick1379; primary official NBB WVV 60/66A"),
        ("bud_isvg_goods_2025", ENT, "2025", "836393", "2025 handelsgoederen 836393 vs 771108 (aankopen 1076342); tick1379; primary official NBB WVV 60"),
        ("bud_isvg_diensten_2025", ENT, "2025", "14728199", "2025 diensten 14728199 vs 20056349; no split; tick1379; primary official NBB WVV 61"),
        ("bud_isvg_diensten_2024", ENT, "2024", "20056349", "2024 diensten 20056349 comparative (closure/conservering); tick1379; primary official NBB WVV 61"),
        ("bud_isvg_pers_2025", ENT, "2025", "7056785", "2025 bezoldigingen 7056785 / 53.7 VTE / 77191 uur / YE 53; tick1379; primary official NBB WVV 62 9087"),
        ("bud_isvg_pers_2024", ENT, "2024", "6869911", "2024 bezoldigingen 6869911 / 55.8 VTE comparative; tick1379; primary official NBB WVV 62"),
        ("bud_isvg_deprec_2025", ENT, "2025", "1747355", "2025 afschrijvingen 1747355 vs 1595115; tick1379; primary official NBB WVV 630"),
        ("bud_isvg_wv_2025", ENT, "2025", "19362", "2025 waardeverminderingen voorraden 19362 vs 106403; tick1379; primary official NBB WVV 631/4"),
        ("bud_isvg_prov_pnl_2025", ENT, "2025", "1350000", "2025 voorzieningen PnL +1350000 vs -987596 (add 1500000 / use 150000); tick1379; primary official NBB WVV 635/8"),
        ("bud_isvg_othcost_2025", ENT, "2025", "5637254", "2025 andere bedrijfskosten 5637254 vs 6109196 (640 bedrijfsbelastingen 5636284); tick1379; primary official NBB WVV 640/8"),
        ("bud_isvg_tax640_2025", ENT, "2025", "5636284", "2025 bedrijfsbelastingen 5636284 vs 6108547 (RPB booked in 64); tick1379; primary official NBB WVV 640"),
        ("bud_isvg_expl_2025", ENT, "2025", "-1792342", "2025 bedrijfsverlies -1792342 vs -8177822; tick1379; primary official NBB WVV 9901"),
        ("bud_isvg_expl_2024", ENT, "2024", "-8177822", "2024 bedrijfsverlies -8177822 comparative; tick1379; primary official NBB WVV 9901"),
        ("bud_isvg_fininc_2025", ENT, "2025", "406040", "2025 financiele opbrengsten 406040 vs 545382; tick1379; primary official NBB WVV 75"),
        ("bud_isvg_fincost_2025", ENT, "2025", "106527", "2025 financiele kosten 106527 vs 800255 (impair 0 vs 717088); tick1379; primary official NBB WVV 65"),
        ("bud_isvg_pnl_2025", ENT, "2025", "-1492829", "2025 PnL 9904 -1492829 vs -8432695; commissaris -1492829; tick1379; primary official NBB WVV"),
        ("bud_isvg_pnl_2024", ENT, "2024", "-8432695", "2024 PnL -8432695 comparative (closure year); tick1379; primary official NBB WVV 9904"),
        ("bud_isvg_comm_2025", ENT, "2025", "25675", "2025 commissaris Grant Thornton / Stefaan De Coninck 25675; tick1379; primary official NBB WVV 9505"),
        ("bud_isvg_steam_2025", ENT, "2025", "3000000", "2025 stoominkomsten 3 Mio (jaarverslag same official PDF; not a WVV 70 split line); tick1379; primary official NBB WVV jaarverslag"),
        ("bud_isvg_heat_2025", ENT, "2025", "133964", "2025 warmte-inkomsten 133964 (jaarverslag same official PDF); tick1379; primary official NBB WVV jaarverslag"),
        ("bud_isvg_ton_2025", ENT, "2025", "169303", "2025 vennoten 169303.19 ton (77pct restafval / 23pct grofvuil); tick1379; primary official NBB WVV jaarverslag"),
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
                "title": "ISVAG JR2025 leftover IGS dual (assets 42.72m / omzet 29.44m / diensten 14.73m / permit beroep / PnL -1.49m)",
                "entity_id": ENT,
                "beneficiary": "ISVAG / 29 Antwerp-region municipalities + IGEAN",
                "legal_basis": "WVV OV; Decreet Lokaal Bestuur; NBB neerlegging; omgevingsvergunning 26.12.2024",
                "decision_date": "2026-06-18",
                "start_year": "1975",
                "end_year": "",
                "total_envelope_eur": "42718614",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL waste — 29.44m omzet (6.10 empty) / 14.73m diensten / hangend vergunningsberoep",
                "cut_option": "Publish unpublished omzet 6.10 + 14.73m 61 split + 5.64m 640 + 6.03m voorzieningen + permit-path; do not keep incinerator IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1379; assets 42718614 omzet 29439548 diensten 14728199 pnl -1492829 equity 32073522; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "ISVAG JR2025 leftover IGS: assets 42.72m / omzet 29.44m / diensten 14.73m / permit beroep / PnL -1.49m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "14728199",
                "total_cost_eur": "42718614",
                "tco_notes": (
                    "Leftover dual IGS waste incinerator of mined Antwerp-region municipalities: "
                    "assets 42.72m / equity 32.07m / pnl -1.49m / omzet 29.44m (6.10 empty) / "
                    "diensten 14.73m / 53.7 VTE / cash DROP 11.14m to 4.15m / provisions 6.03m JUMP / "
                    "hangend vergunningsberoep; official NBB WVV live; do not treat 42.72m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "ISVAG / 29 Antwerp-region municipalities + IGEAN",
                "stated_goal": "Local leftover IGS map VL waste — JR2025 live; dual omzet-empty/diensten/permit FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 42.72m / omzet 29.44m / diensten 14.73m / permit beroep / pnl -1.49m",
                "absurdity_score": "7.3",
                "cost_score": "7.0",
                "difficulty": "2.5",
                "priority_index": "6.8",
                "cut_proposal": "Publish unpublished omzet 6.10 + 14.73m 61 split + 5.64m 640 + 6.03m voorzieningen + permit-path; do not keep incinerator IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1379; leftover IGS of mined Antwerp-region municipalities; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "omzet 29439548 vs 25215937 (WVV 70; 6.10 category empty / geo empty) per stroom/tegenpartij + voorschot per ton unpublished "
                    "+ diensten 14728199 vs 20056349 (WVV 61; no split) top-20 leveranciers "
                    "+ bedrijfsbelastingen 5636284 vs 6108547 (WVV 640; RPB booked in 64) "
                    "+ voorzieningen 6025192 JUMP vs 4675192 (164/5 overige; pens 160 empty; add 1500000 / use 150000) "
                    "+ hangend beroep 17.02.2025 tegen omgevingsvergunning 26.12.2024 (commissaris benadrukking 6.19; significante impact 2026+) "
                    "+ cash DROP 11137685 to 4145068 + beleggingen 21865510 "
                    "+ overgedragen -14449352 after two loss years + VOL-inb 6.1/6.2/6.8/6.15/6.17/6.18/6.20/9 not filed + subsidies 740 empty"
                ),
                "why_it_matters": (
                    "Leftover IGS OV of mined Antwerp-region municipalities "
                    "(same leftover-IGS waste seam as IVAGO 1375 / MIWA 1374 / IVOO 1373 / IMOG 1369 / IVBO 1352 / IVIO 1347 / IVVO 1345): "
                    "42.72m assets / 29.44m omzet / 14.73m diensten / 6.03m provisions JUMP / "
                    "hangend vergunningsberoep after 2024 forced closure / 53.7 VTE / cash DROP "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "ISVAG / Raad van Bestuur / Kristof Bossuyt / 29 Antwerp-region municipalities + IGEAN",
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
                    "tick1379 leftover IGS OV of mined Antwerp-region municipalities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (308kB 48p deposit 2026-00182993). "
                    "De Nekker already mined 1378 — skipped. MIROM Menen already mined 1377 — skipped. "
                    "MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. "
                    "MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. "
                    "Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. "
                    "IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 skipped. "
                    "Dommelhof leftover Limburg EVA 0777.495.085 still no JR2025 PDF. "
                    "IVAREM still 2024. Otary RS Nuhma-adjacent fallback not taken. "
                    "INCOVO/INTERZA 2026 CDN now live — leftover later. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1379",
        "title": "ISVAG JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: ISVAG leftover IGS of mined Antwerp-region municipalities after honest hunt; KBO 0214.981.001 Actief; "
            "live JR2025 official NBB WVV VOL-inb PDF (308kB 48p deposit 2026-00182993; commissaris Grant Thornton); "
            "sourced euros assets 42718614 / omzet 29439548 / diensten 14728199 / pers 7056785 / pnl -1492829 / equity 32073522; "
            "FOI ready omzet 6.10 empty / 14.73m 61 / permit beroep"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T05:20:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1379 ISVAG leftover IGS residual; KBO 0214.981.001; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1380 residual dual L5 VL + every-10"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1380",
        "title": "Continuous FOI-adjacent public hole-fill batch + every-10",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "EVERY-10 FIRST (tick 1380): refresh docs/doge/data/progress_every_10_ticks.md + doge_waste_top10_current.md then one residual unit. "
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1379 done including ISVAG 1379 leftover IGS live NBB WVV / "
            "De Nekker 1378 leftover provincial EVA live NBB WVV / "
            "MIROM Menen 1377 leftover IGS live NBB WVV / "
            "MIROM Roeselare 1376 leftover IGS live NBB WVV / "
            "IVAGO 1375 leftover IGS live NBB WVV / "
            "MIWA 1374 leftover IGS live NBB WVV / "
            "IVOO 1373 leftover IGS live NBB WVV / "
            "IGEMO 1372 leftover IGS live NBB WVV / "
            "Veneco 1371 leftover IGS live NBB WVV / "
            "Haviland 1370 leftover IGS live NBB WVV + every-10); "
            "INCOVO leftover IGS KBO 0218.993.039 CDN 2026-00239674 now live — take if still unmined; "
            "INTERZA leftover IGS KBO 0219.324.522 CDN 2026-00246462 now live — take if still unmined; "
            "Fluvius Midden-Vlaanderen / INTERGEM 0220.764.971 CDN 2026-00227859 live — leftover energy IGS later; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads "
            "(old VZW 0443.049.478 CDN 2026-00325874 is a different Tielt-Winge entity); "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB PIH / APB Inovant / APB Atlas listed or leftover but provincieantwerpen.be 403 — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1379 after ISVAG leftover IGS live NBB WVV; next residual dual L5 VL + every-10",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1379", rq_new, rq_spawn)
    print("research_queue 1379", found, "spawned_1380", spawned)

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
                "last_unit_id": "rq_1379",
                "ticks_completed": "1379",
                "paused": "no",
                "notes": (
                    "tick1379 ISVAG leftover IGS residual; KBO 0214.981.001; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 42718614 omzet 29439548 diensten 14728199 pers 7056785 pnl -1492829 equity 32073522; "
                    "FOI ready omzet 6.10 empty/14.73m 61/permit beroep; next rq_1380 residual dual L5 VL + every-10; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    entry = """### Tick 1379 - 2026-08-19 - rq_1379 ISVAG dual residual leftover
- Unit: Intercommunale voor Slib- en Vuilverwijdering van Antwerpse Gemeenten / ISVAG / I.S.V.A.G. (leftover IGS opdrachthoudende vereniging / afvalenergiecentrale + warmtenet Wilrijk of mined Antwerp-region municipalities; 29 steden en gemeenten + IGEAN) after residual dual hunt (KBO **0214.981.001**; official isvag.be has informatie/jaarverslagen but no isolated statutory 2025 balans — live NBB WVV VOL-inb deposit **2026-00182993** PDF 308kB / 48p; AV **18.06.2026**; PDF created **22.06.2026**; header **19.06.2026**; neerlegging SBM **23.06.2026**; commissaris Grant Thornton Bedrijfsrevisoren BV 0439.814.826 / Stefaan De Coninck A002461 25.675 signed 26.03.2026 oordeel zonder voorbehoud assets 42.718.614 / PnL −1.492.829 + benadrukking VOL-inb 6.19 omgevingsvergunning-beroep; 2e opeenvolgend boekjaar; mandaat AV 16.04.2024 tot AV YE 2026). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; prior ticks listed ISVAG as still-2023/no-2025-JR). Distinct from already-mined De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **17.01.1975**; statutaire naam Intercommunale voor Slib- en Vuilverwijdering van Antwerpse Gemeenten since 17.01.1975; afkorting I.S.V.A.G. since 17.01.1975; Opdrachthoudende vereniging (Vlaams Gewest) since 11.12.2003; zetel Boomsesteenweg 1000 2610 Antwerpen since 28.12.1995; **1 VE**; tel +32 3 877 28 55; e-mail info@isvag.be; web https://isvag.be/; btw since 01.09.1997; RSZ since 01.01.2022; aanbestedende overheid since 17.01.1975; KBO kapitaal 25.000; jaarvergadering mei; boekjaar 31 december; NACE 38.330/38.210. Voorzitter Kristof Bossuyt since 27.03.2025; commissaris Grant Thornton / Stefaan De Coninck. Hunt leftover AGB/zorg/EVA first: leftover AGB Mechelen/Kortrijk/Brugge/Roeselare/Oostende 404/403 as of 1375 — not re-probed once live ISVAG extracted; Dommelhof leftover Limburg EVA KBO 0777.495.085 still no JR2025 PDF (old VZW 0443.049.478 has CDN 2026-00325874 but is a different Tielt-Winge entity) — not taken; IVAREM still 2024 (SBM last JR 2024 / neerlegging 2025-09-18); leftover APB provincieantwerpen.be 403. ISVAG statutory CDN live this tick (HTTP 200 / 308464 / 48p) — taken (preferred leftover IGS of mined Antwerp-region municipalities outside Nuhma). De Nekker already mined 1378 — skipped. MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 already mined — skipped. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. INCOVO 0218.993.039 CDN 2026-00239674 + INTERZA 0219.324.522 CDN 2026-00246462 now live — leftover later. Fluvius Midden-Vlaanderen / INTERGEM 0220.764.971 CDN 2026-00227859 live — leftover energy IGS later. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366. Not every-10 (next 1380).
- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud + benadrukking 6.19; VOL-inb 6.1/6.2/6.8/6.15/6.17/6.18/6.20/9 not filed; omzet 6.10 category/geo empty; subsidies 740 empty): assets **42.718.614** (was 46.749.415); fixed **12.309.395** / MVA **12.308.949** (gebouwen **2.757.772**; machines **9.251.115** vs 9.743.799 aanschaf year **1.095.443**; meubilair 300.062); FVA 446; current **30.409.219**; LT recv 21.600; inventory 1.178.211; ST recv **2.908.233** (trade 2.905.146); beleggingen **21.865.510** vs 19.007.457 (vastrentende effecten); cash **4.145.068 DROP** vs 11.137.685; prepaid 290.597; equity **32.073.522** (was 33.630.737; inbreng 4.909.965; reserves 39.640.412; overgedragen **−14.449.352**; kapitaalsubsidies 1.684.288); voorzieningen **6.025.192 JUMP** vs 4.675.192 (all 164/5 overige; pens 160 empty; add 1.500.000 / use 150.000); schulden **4.619.900** (LT empty; ST **4.351.886** waarvan leveranciers 3.430.158 + tax 257.748 + soc 663.480; accruals 268.014); omzet **29.439.548 JUMP** vs 25.215.937 (6.10 unpublished); othops 136.188 DROP vs 961.884; goods 836.393; diensten **14.728.199** vs 20.056.349; pers **7.056.785** / **53,7 VTE** / 77.191 uur / YE 53 (49,3+5,8; 46,7M/7V); afschr 1.747.355; andere kosten **5.637.254** waarvan bedrijfsbelastingen **5.636.284**; expl **−1.792.342** vs −8.177.822; fin opbr 406.040; fin kosten 106.527; PnL **−1.492.829** vs −8.432.695 overgedragen; commissaris 25.675. Jaarverslag same PDF: 169.303,19 ton (77% restafval / 23% grofvuil); stoom **3 Mio**; warmte **133.964**; 2024 gedwongen sluiting na vernietiging vergunning; herstart lijn 1 **09.01.2025** / lijn 2 **16.01.2025**; nieuwe vergunning 10 jaar **26.12.2024**; beroep **17.02.2025** hangende — commissaris benadrukking significante impact 2026+. Continuity: voldoende eigen middelen (board).
- CSVs: sources+4/entities+1/budgets+58/commitments+1/leaderboard+1 + FOI ready `gap_isvg_omzet_29_44m_diensten_14_73m_permit_l5` (not sent); rq_1379=done; spawn rq_1380; ticks=1379.
- Coverage: residual dual L5 (ISVAG leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1380).
- Next: rq_1380 residual dual L5 VL JR2025 hole_fill + **every-10 first** (prefer leftover INCOVO KBO 0218.993.039 CDN 2026-00239674 / INTERZA KBO 0219.324.522 CDN 2026-00246462 now live; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS CDN 2026-00254280 / Rematics / Sunfin only if taken after leftover IGS/EVA/AGB; leftover APB POA / TPA / De Schorre / Warande / PIH / Inovant / Atlas only if a real PDF downloads; IVAREM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1379 write done")


if __name__ == "__main__":
    main()

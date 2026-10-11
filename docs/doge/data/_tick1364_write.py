# -*- coding: utf-8 -*-
"""Tick 1364 — leftover Herkenrode Real Estate NV JR2025 official NBB WVV euros.
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

TICK = "1364"
UTC = "2026-08-19T00:25:00Z"
ENT = "nv_herk"
HIER = "Vlaanderen>Limburg>NV>HerkenrodeRE>Vastgoed"
GAP = "gap_herk_omzet_2_62m_pnl_neg_0_39m_debt_27_45m_l5"
SRC = "src_herk_jr2025_nbb"
SRC2 = "src_herk_site"
SRC3 = "src_kbo_herk_0724557633"
SRC4 = "src_herk_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00124490.pdf"
SRC2_URL = "https://nuhma.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0724557633"
SRC4_URL = "https://nuhma.be/contact"
FOI_EMAIL = "info@nuhma.be"
FOI_POSTAL = "Herkenrodesingel 14 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_herk_omzet_2_62m_pnl_neg_0_39m_debt_27_45m_l5.md"
COMM = "comm_herk_jr2025_pnl"
LB = "lb_herk_omzet_2_62m_pnl_neg_0_39m_debt"


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
                "title": "Herkenrode Real Estate NV jaarrekening boekjaar 2025 (official NBB WVV VOL-kap deposit 2026-00124490; AV 26.05.2026)",
                "url": SRC_URL,
                "publisher": "Herkenrode Real Estate NV / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1364; official NBB VOL-kap PDF 439kB 38p deposit 2026-00124490 neerlegging 28.05.2026 created 28.05.2026; "
                    "leftover vastgoed NV of NUHMA DC 1358 / Nuhma cv 1356 / MyCSN 1363 / s-Lim 1362 / Nuhmeris 1361 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Moore Audit / Jimmy Depré 5500 oordeel zonder voorbehoud 05.05.2026; "
                    "parent DC 6.5.1 EV 131842 / PnL -386604 MATCHES"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Nuhma official site (parent cv; statutory Herkenrode RE JR unpublished on site; nuhma.be still 2020-only)",
                "url": SRC2_URL,
                "publisher": "Nuhma cv",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1364; leftover NV of mined Limburg + Nuhma cv/DC/AC/Nubema/ECO2050/Nuhmeris/s-Lim/MyCSN/Bionerga/Limburg.net; "
                    "nuhma.be has no 2025 JR PDF (jaarverslag still 2020-only); this NV has no own site; "
                    "owns HQ campus Herkenrodesingel 14+16 + magazijnen Oude Spoorbaan 100.14+100.15"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Herkenrode Real Estate 0724.557.633",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1364; KBO 0724.557.633 Actief / normale toestand since 04.04.2019; "
                    "statutaire naam HERKENRODE REAL ESTATE since 04.04.2019; NV since 04.04.2019; "
                    "zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; 1 VE 2287840119; "
                    "btw since 01.06.2019; jaarvergadering april; boekjaar 31 december; KBO kapitaal 1200000; "
                    "bestuurders Nuhma cv 0472325068 / Nubema 0834086964; no KBO email/web/tel; "
                    "NACE 68.201 / 64.210 / 68.203 / 68.204"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Herkenrode RE FOI channel / parent Nuhma official contact",
                "url": SRC4_URL,
                "publisher": "Nuhma cv",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1364; FOI info@nuhma.be; tel 011 49 56 10; "
                    "Herkenrodesingel 14 3500 Hasselt (this NV owns the zetel campus); "
                    "no own KBO email/web"
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
                "name_nl": "Herkenrode Real Estate (leftover vastgoed NV Limburg / 100pct Nuhma DC / HQ-campus)",
                "name_fr": "Herkenrode Real Estate (SA immobiliere residuelle Limbourg / participation Nuhma DC 100pct / campus siege)",
                "name_en": "Herkenrode Real Estate leftover Limburg property NV (100pct Nuhma DC / HQ campus)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://nuhma.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1364 leftover residual vastgoed NV of NUHMA DC 1358 "
                    "+ Nuhma cv 1356 + MyCSN 1363 + s-Lim 1362 + Nuhmeris 1361 + Nubema 1359 + ECO2050 1360 + NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353 "
                    "(owns zetel Herkenrodesingel 14+16 + Oude Spoorbaan 100.14+100.15); "
                    "KBO 0724.557.633 Actief since 04.04.2019; official NBB WVV VOL-kap PDF downloads; "
                    "sourced euros assets 27578356 omzet 2622876 pnl -386604; "
                    "FOI ready 6.10/tenants/parent-loan 7.91m/ING 19.08m/alarmbel"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_herk_assets_2025", ENT, "2025", "27578356", "2025 assets 27578356 VOL-kap 20/58; tick1364; primary official NBB WVV"),
        ("bud_herk_assets_2024", ENT, "2024", "29840745", "2024 assets 29840745 comparative; tick1364; primary official NBB WVV 20/58"),
        ("bud_herk_fixed_2025", ENT, "2025", "26809718", "2025 vaste activa / MVA 26809718 DROP vs 29003388; tick1364; primary official NBB WVV 21/28 22/27"),
        ("bud_herk_mva_2025", ENT, "2025", "26809718", "2025 terreinen/gebouwen 26809718; tick1364; primary official NBB WVV 22"),
        ("bud_herk_mvaacq_2025", ENT, "2025", "34162894", "2025 MVA aanschaf 34162894 unchanged; tick1364; primary official NBB WVV 8191"),
        ("bud_herk_reval_2025", ENT, "2025", "1880718", "2025 MVA meerwaarde 1880718 after afboek 168782; tick1364; primary official NBB WVV 8251"),
        ("bud_herk_revaloff_2025", ENT, "2025", "168782", "2025 herwaardering afgeboekt 168782; tick1364; primary official NBB WVV 8231"),
        ("bud_herk_deprcum_2025", ENT, "2025", "9233894", "2025 MVA afschr cum 9233894; tick1364; primary official NBB WVV 8321"),
        ("bud_herk_current_2025", ENT, "2025", "768639", "2025 vlottende activa 768639 DROP vs 837356; tick1364; primary official NBB WVV 29/58"),
        ("bud_herk_strecv_2025", ENT, "2025", "3228", "2025 ST overige vorderingen 3228; tick1364; primary official NBB WVV 41"),
        ("bud_herk_cash_2025", ENT, "2025", "764024", "2025 liquide middelen 764024 DROP vs 834010; tick1364; primary official NBB WVV 54/58"),
        ("bud_herk_cash_2024", ENT, "2024", "834010", "2024 liquide middelen 834010 comparative; tick1364; primary official NBB WVV 54/58"),
        ("bud_herk_prepaid_2025", ENT, "2025", "1386", "2025 overlopend actief 1386 (verkregen opbrengsten); tick1364; primary official NBB WVV 490/1"),
        ("bud_herk_equity_2025", ENT, "2025", "131842", "2025 eigen vermogen 131842 DROP vs 518446; matches parent DC 6.5.1; tick1364; primary official NBB WVV 10/15"),
        ("bud_herk_equity_2024", ENT, "2024", "518446", "2024 eigen vermogen 518446 comparative; tick1364; primary official NBB WVV 10/15"),
        ("bud_herk_capital_2025", ENT, "2025", "1200000", "2025 geplaatst kapitaal 1200000 / 100 aandelen op naam 100pct Nuhma DC; tick1364; primary official NBB WVV 100"),
        ("bud_herk_revaleq_2025", ENT, "2025", "1880718", "2025 herwaarderingsmeerwaarden EV 1880718 DROP vs 2025388; tick1364; primary official NBB WVV 12"),
        ("bud_herk_reserve_2025", ENT, "2025", "120000", "2025 wettelijke reserve 120000; tick1364; primary official NBB WVV 130"),
        ("bud_herk_re_2025", ENT, "2025", "-3068876", "2025 overgedragen verlies -3068876; tick1364; primary official NBB WVV 14"),
        ("bud_herk_debt_2025", ENT, "2025", "27446514", "2025 schulden 27446514 DROP vs 29322299; tick1364; primary official NBB WVV 17/49"),
        ("bud_herk_lt_2025", ENT, "2025", "25475421", "2025 LT financieel 25475421; tick1364; primary official NBB WVV 17"),
        ("bud_herk_ltbank_2025", ENT, "2025", "17568388", "2025 LT kredietinstellingen 17568388; tick1364; primary official NBB WVV 173"),
        ("bud_herk_ltother_2025", ENT, "2025", "7907034", "2025 LT overige leningen 7907034 related; tick1364; primary official NBB WVV 174"),
        ("bud_herk_st_2025", ENT, "2025", "1508641", "2025 ST schulden 1508641; tick1364; primary official NBB WVV 42/48"),
        ("bud_herk_stwithin_2025", ENT, "2025", "1507599", "2025 LT binnen jaar 1507599 all bank; tick1364; primary official NBB WVV 42"),
        ("bud_herk_trade_2025", ENT, "2025", "1042", "2025 leveranciers 1042 related; tick1364; primary official NBB WVV 440/4"),
        ("bud_herk_accrued_2025", ENT, "2025", "462452", "2025 overlopend passief 462452 (kosten 215615 + opbr 246837); tick1364; primary official NBB WVV 492/3"),
        ("bud_herk_accruedcost_2025", ENT, "2025", "215615", "2025 toe te rekenen kosten 215615; tick1364; primary official NBB WVV 6.9"),
        ("bud_herk_defrev_2025", ENT, "2025", "246837", "2025 over te dragen opbrengsten 246837; tick1364; primary official NBB WVV 6.9"),
        ("bud_herk_banksec_2025", ENT, "2025", "19075986", "2025 zakelijk gewaarborgd 19075986 all bank; tick1364; primary official NBB WVV 9062"),
        ("bud_herk_hypbook_2025", ENT, "2025", "26809717", "2025 hypotheek boekwaarde 26809717; tick1364; primary official NBB WVV 91611"),
        ("bud_herk_hypins_2025", ENT, "2025", "8121577", "2025 hypotheek inschrijving 8121577; tick1364; primary official NBB WVV 91621"),
        ("bud_herk_hypmand_2025", ENT, "2025", "15000000", "2025 hypotheekmandaat 15000000; tick1364; primary official NBB WVV 91631"),
        ("bud_herk_ops_2025", ENT, "2025", "2849284", "2025 bedrijfsopbrengsten 2849284; tick1364; primary official NBB WVV 70/76A"),
        ("bud_herk_omzet_2025", ENT, "2025", "2622876", "2025 omzet 2622876 JUMP vs 2533891; 6.10 category/geo empty; tick1364; primary official NBB WVV 70"),
        ("bud_herk_omzet_2024", ENT, "2024", "2533891", "2024 omzet 2533891 comparative; tick1364; primary official NBB WVV 70"),
        ("bud_herk_andere_2025", ENT, "2025", "226409", "2025 andere bedrijfsopbrengsten 226409 DROP vs 674227; tick1364; primary official NBB WVV 74"),
        ("bud_herk_opscost_2025", ENT, "2025", "2433782", "2025 bedrijfskosten 2433782; tick1364; primary official NBB WVV 60/66A"),
        ("bud_herk_diensten_2025", ENT, "2025", "13421", "2025 diensten 13421; tick1364; primary official NBB WVV 61"),
        ("bud_herk_afschr_2025", ENT, "2025", "2193671", "2025 afschrijvingen 2193671; tick1364; primary official NBB WVV 630"),
        ("bud_herk_taxcost_2025", ENT, "2025", "226691", "2025 bedrijfsbelastingen 226691; tick1364; primary official NBB WVV 640"),
        ("bud_herk_expl_2025", ENT, "2025", "415502", "2025 bedrijfswinst 415502 DROP vs 824585; tick1364; primary official NBB WVV 9901"),
        ("bud_herk_fininc_2025", ENT, "2025", "7633", "2025 financiele opbrengsten 7633 (vlottende); tick1364; primary official NBB WVV 75"),
        ("bud_herk_fincost_2025", ENT, "2025", "809738", "2025 financiele kosten 809738 (schulden 809121); tick1364; primary official NBB WVV 65"),
        ("bud_herk_debint_2025", ENT, "2025", "809121", "2025 kosten van schulden 809121; tick1364; primary official NBB WVV 650"),
        ("bud_herk_pnl_2025", ENT, "2025", "-386604", "2025 PnL 9904 -386604 (was -120980); tick1364; primary official NBB WVV; matches parent DC 6.5.1"),
        ("bud_herk_pnl_2024", ENT, "2024", "-120980", "2024 PnL -120980 comparative; tick1364; primary official NBB WVV 9904"),
        ("bud_herk_comm_2025", ENT, "2025", "5500", "2025 commissaris Moore Audit 5500; tick1364; primary official NBB WVV 9505"),
        ("bud_herk_reldebt_2025", ENT, "2025", "7908076", "2025 verbonden schulden 7908076 (LT 7907034 + ST 1042); tick1364; primary official NBB WVV 9351"),
        ("bud_herk_reldcost_2025", ENT, "2025", "268683", "2025 verbonden kosten schulden 268683 JUMP vs 181938; tick1364; primary official NBB WVV 9461"),
        ("bud_herk_taxlat_2025", ENT, "2025", "509060", "2025 actieve latenties fiscale verliezen 509060; tick1364; primary official NBB WVV 9142; not TE-additive"),
        ("bud_herk_vat_2025", ENT, "2025", "370254", "2025 BTW door vennootschap 370254; tick1364; primary official NBB WVV 9146"),
        ("bud_herk_lt1to5_2025", ENT, "2025", "16475421", "2025 resterend 1-5j 16475421 (bank 8568388 + overige 7907034); tick1364; primary official NBB WVV 8912"),
        ("bud_herk_lt5y_2025", ENT, "2025", "9000000", "2025 resterend >5j 9000000 all bank; tick1364; primary official NBB WVV 8913"),
        ("bud_herk_cdc_2025", ENT, "2025", "15000000", "2025 Nuhma cv cash-deficiency clause ING 15000000 27.06.2024; tick1364; primary official NBB WVV 6.19"),
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
                "title": "Herkenrode RE NV JR2025 leftover NV dual (assets 27.58m / omzet 2.62m / PnL -0.39m / debt 27.45m / alarmbel)",
                "entity_id": ENT,
                "beneficiary": "Herkenrode Real Estate / NUHMA DC / Nuhma cv / ING / Limburg municipalities",
                "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; NBB neerlegging; alarmbel art. 7:228",
                "decision_date": "2026-05-26",
                "start_year": "2019",
                "end_year": "2026",
                "total_envelope_eur": "27578356",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover NV map VL vastgoed HQ-campus — 6.10 empty / parent loan 7.91m / ING 19.08m / alarmbel EV 0.13m",
                "cut_option": "Publish 6.10 tenants of HQ+warehouses + put 7.91m parent loan and 19.08m ING + 15m Nuhma cv cash-deficiency on the record + why alarmbel EV 0.13m on 1.20m capital after buying own zetel 04.07.2024; do not keep 27.6m municipal HQ campus as unpublished dual vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1364; assets 27578356 omzet 2622876 pnl -386604; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Herkenrode RE NV JR2025 leftover NV: assets 27.58m / omzet 2.62m / PnL -0.39m / debt 27.45m / alarmbel",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "386604",
                "total_cost_eur": "27578356",
                "tco_notes": (
                    "Leftover dual vastgoed NV of NUHMA DC of mined Limburg cities: "
                    "assets 27.58m / equity 0.13m / pnl -0.39m / omzet 2.62m / pers 0 / 0 VTE / "
                    "Nuhma DC 100pct / parent DC 6.5.1 MATCHES / "
                    "related loan 7.91m / ING 19.08m / cash-deficiency 15m / alarmbel since Jun 2025 / official NBB WVV live; "
                    "do not treat 27.58m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Herkenrode Real Estate / NUHMA DC / Nuhma cv / ING / Limburg municipalities",
                "stated_goal": "Local leftover NV map VL vastgoed HQ-campus — JR2025 live; dual 6.10/loan/alarmbel FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 27.58m / omzet 2.62m / pnl -0.39m; 0 VTE; parent DC 6.5.1 matches; alarmbel EV 0.13m",
                "absurdity_score": "7.2",
                "cost_score": "6.8",
                "difficulty": "2.5",
                "priority_index": "6.6",
                "cut_proposal": "Publish 6.10 tenants of HQ+warehouses + put 7.91m parent loan and 19.08m ING + 15m Nuhma cv cash-deficiency on the record + why alarmbel EV 0.13m on 1.20m capital after buying own zetel 04.07.2024; do not keep 27.6m municipal HQ campus as unpublished dual vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1364; leftover NV of mined Limburg + NUHMA DC 1358 / Nuhma cv 1356 / MyCSN 1363 / s-Lim 1362 / Nuhmeris 1361 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "6.10 omzet 2622876 category/geo split empty + per-gebouw tenants Herkenrodesingel 14+16 / Oude Spoorbaan 100.14+100.15 "
                    "(Nuhma cv/DC/AC/Nubema/Nuhmeris/ECO2050/MyCSN/s-Lim/Bionerga/Limburg.net/derden) "
                    "+ andere bedrijfsopbrengsten 226409 DROP vs 674227 unnamed "
                    "+ Nuhma DC 100pct book/votes (tick1358 6.5.1 MATCHES EV 131842 / PnL -386604) "
                    "+ overname 04.07.2024 Monument Immo Management / Monument Real Estate Fund "
                    "+ related overige lening 7907034 (was 8253351; 1-5y) + related ST 1042 / debt cost 268683 "
                    "+ ING 19075986 (LT 17568388 + within-year 1507599) + hypotheek book 26809717 / inschrijving 8121577 / mandaat 15000000 "
                    "+ Nuhma cv cash-deficiency clause ING 15000000 27.06.2024 "
                    "+ 6.15 related-party refusal "
                    "+ alarmbel since Jun 2025 EV 131842 = 11pct of capital 1200000 "
                    "+ herwaardering 2024 / afboek 168782 / transfer 144670 to RE "
                    "+ tax losses 509060 "
                    "+ continuity art.3:6 6deg two consecutive losses / aandeelhouderssteun unquantified "
                    "+ official-site JR (nuhma.be 2020-only; no own site)"
                ),
                "why_it_matters": (
                    "Leftover vastgoed NV of NUHMA DC of mined Limburg cities + Nuhma cv 1356 "
                    "+ MyCSN 1363 + s-Lim 1362 + Nuhmeris 1361 + Nubema 1359 + ECO2050 1360 + NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353 "
                    "(owns zetel campus Herkenrodesingel 14+16): "
                    "27.58m assets / 2.62m omzet / -0.39m pnl / 0 VTE / 100pct Nuhma DC / "
                    "7.91m parent loan / 19.08m ING / 15m cash-deficiency / alarmbel EV 0.13m on 1.20m capital "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "Herkenrode Real Estate NV / NUHMA DC BV / Nuhma cv / Limburg municipalities",
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
                    "tick1364 leftover NV of mined Limburg cities + NUHMA DC 1358 / Nuhma cv 1356 / MyCSN 1363 / s-Lim 1362 / Nuhmeris 1361 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 after honest hunt; "
                    "live JR2025 official NBB WVV VOL-kap PDF now extracted (439kB 38p deposit 2026-00124490). "
                    "AGB MAC already mined 1270 — skipped. Westtoer already mined — skipped. "
                    "MyCSN already mined 1363 — skipped. s-Lim already mined 1362 — skipped. Nuhmeris already mined 1361 — skipped. ECO2050 already mined 1360 — skipped. Nubema already mined 1359 — skipped. NUHMA DC already mined 1358 — skipped. EcoWerf already mined 1357 — skipped. "
                    "s-Lim DV 0805138503 leftover IGS later. "
                    "Dommelhof leftover Limburg EVA KBO 0777.495.085 still no 2026 PDF. "
                    "IOK/IMOG/Haviland still 2024. Interleuven still 2024 balans. "
                    "POM Limburg glossy-only. Veneco/Leiedal glossy. NBB consult skipped. "
                    "Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1364",
        "title": "Herkenrode RE NV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Herkenrode Real Estate leftover vastgoed NV of NUHMA DC of mined Limburg cities "
            "+ Nuhma cv/MyCSN/s-Lim/Nuhmeris/Nubema/ECO2050/AC/Bionerga/Limburg.net after honest hunt; KBO 0724.557.633 Actief; "
            "live JR2025 official NBB WVV VOL-kap PDF (439kB 38p deposit 2026-00124490; commissaris Moore); "
            "sourced euros assets 27578356 / omzet 2622876 / pnl -386604; "
            "FOI ready 6.10/tenants/parent-loan 7.91m/ING 19.08m/alarmbel"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T01:45:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1364 Herkenrode leftover NV residual; KBO 0724.557.633; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1365 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1365",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1364 done including Herkenrode RE NV 1364 leftover vastgoed live NBB WVV / "
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
            "s-Lim DV 0805.138.503 leftover IGS (67.13pct+16.44pct of s-Lim CV votes) — take only if a statutory 2025 WVV/BBC PDF now downloads; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland still 2024 — take only if a 2025 JR PDF now downloads; "
            "Veneco / Leiedal / IVOO / MIROM / INCOVO / IVAGO / MIWA / IVAREM / IGEMO — take only if a statutory 2025 WVV/BBC PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined Herkenrode RE 1364 / MyCSN 1363 / s-Lim 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1364 after Herkenrode leftover NV live NBB WVV; next residual dual L5 VL; next every-10 is 1370",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1364", rq_new, rq_spawn)
    print("research_queue 1364", found, "spawned_1365", spawned)

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
                "last_unit_id": "rq_1364",
                "ticks_completed": "1364",
                "paused": "no",
                "notes": (
                    "tick1364 Herkenrode leftover NV residual; KBO 0724.557.633; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 27578356 omzet 2622876 pnl -386604; "
                    "FOI ready 6.10/tenants/parent-loan/ING/alarmbel; next rq_1365 residual dual L5 VL; continuous hole_fill; next every-10 is 1370"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1364 - 2026-08-19 - rq_1364 Herkenrode RE NV dual residual leftover
- Unit: Herkenrode Real Estate NV (leftover vastgoed naamloze vennootschap / 100% NUHMA DC BV since 04.07.2024; owns the Nuhma HQ campus) of already-mined Limburg cities via Nuhma cv tick1356 (Hasselt / Genk / Tongeren-Borgloon / Houthalen-Helchteren / Bilzen-Hoeselt / Leopoldsburg / Nieuwerkerken / Gingelom / Pelt / Maasmechelen) + leftover BV NUHMA DC tick1358 + leftover NV MyCSN tick1363 + leftover CV s-Lim tick1362 + leftover NV Nuhmeris tick1361 + leftover NV Nubema tick1359 + leftover cv ECO2050 tick1360 + leftover NV NUHMA AC tick1355 + leftover NV Bionerga tick1354 + leftover IGS Limburg.net tick1353 after residual dual hunt (KBO **0724.557.633**; official nuhma.be still 2020-only / this NV has no own site; live NBB WVV VOL-kap deposit **2026-00124490** PDF 439kB / 38p; AV **26.05.2026**; neerlegging **28.05.2026**; PDF created **28.05.2026**; commissaris Moore Audit / Jimmy Depré 5.500 oordeel zonder voorbehoud 05.05.2026; jaarverslag RvB 05.05.2026 text-extractable). Leftover NV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last tick listed leftover Herkenrode RE CDN 2026-00124490 if still live). Distinct from already-mined MyCSN 1363 / s-Lim 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **04.04.2019**; statutaire naam HERKENRODE REAL ESTATE since 04.04.2019; Naamloze vennootschap since 04.04.2019; zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; **1 VE** 2.287.840.119; btw since 01.06.2019; jaarvergadering april; KBO kapitaal 1.200.000; bestuurders Nuhma cv / Nubema NV; e-mail via parent info@nuhma.be; NACE 68.201 / 64.210 / 68.203 / 68.204. Hunt leftover AGB/zorg/EVA first: AGB MAC Mechelen 2025 BBC already mined tick1270 — skipped; SportAG Aalst / AGB Deinze / AGB Genk already mined — skipped; Westtoer APB already mined — skipped; MyCSN already mined 1363 — skipped; s-Lim already mined 1362 — skipped; Nuhmeris already mined 1361 — skipped; ECO2050 already mined 1360 — skipped; Nubema already mined 1359 — skipped; NUHMA DC already mined 1358 — skipped; EcoWerf already mined 1357 — skipped; Herkenrode statutory CDN live this tick (HTTP 200 / 438714 / 38p) — taken. s-Lim DV 0805.138.503 leftover IGS later. IOK/IMOG/Haviland still 2024; Interleuven 2025 jaarverslag InDesign embed only / balans still 2024; POM Limburg glossy-only — not taken; Veneco/Leiedal glossy-only; IVAREM activiteitenverslag glossy; IGEMO activiteitenverslag only; IVOO no public 2025 JR; IVAGO SSL EOF; MIWA flipbook; MIROM Cloudflare; De Schorre provincieantwerpen.be 403; APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas not taken (Herkenrode WVV live); Dommelhof leftover Limburg EVA KBO 0777.495.085 still no 2026 PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE no fetchable 2025 JR this tick. NBB consult skipped (403/SPA); euros extracted from the official VOL-kap deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined MyCSN 1363 / s-Lim 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345. Not every-10 (next 1370).
- EUR strong (primary official WVV VOL-kap; parent DC 6.5.1 EV 131.842 / PnL −386.604 **matches**; commissaris Moore oordeel zonder voorbehoud 05.05.2026): assets **27.578.356** (was 29.840.745; RvB 27.578.356,33); fixed/MVA **26.809.718** DROP vs 29.003.388 (terreinen/gebouwen; aanschaf **34.162.894**; herwaard **1.880.718** after afboek **168.782**; afschr cum **9.233.894** after geboekt **2.193.671**); current **768.639**; ST recv **3.228**; cash **764.024 DROP** vs 834.010; prepaid **1.386**; equity **131.842** DROP vs 518.446 (kapitaal 1.200.000 / 100 aandelen op naam **100% Nuhma DC**; herwaard 1.880.718 DROP vs 2.025.388; wettelijk 120.000; overgedragen verlies **−3.068.876**); schulden **27.446.514** (LT **25.475.421** waarvan bank **17.568.388** + related overige **7.907.034**; ST **1.508.641** waarvan binnen jaar **1.507.599** bank + leveranciers **1.042**; resterend 1–5j **16.475.421** / >5j **9.000.000**; zakelijk gewaarborgd **19.075.986**; hypotheek boek **26.809.717** / inschrijving **8.121.577** / mandaat **15.000.000**); omzet **2.622.876 JUMP** vs 2.533.891 / andere **226.409 DROP** vs 674.227 / pers **0** / VTE **0**; diensten **13.421**; afschr **2.193.671**; bedrijfsbelastingen **226.691**; expl **+415.502** DROP vs 824.585; fin opbr **7.633**; fin kosten **809.738** (schulden 809.121 waarvan related **268.683**); PnL **−386.604** (was −120.980; RvB −386.603,71); dividend **0**. Related schulden **7.908.076**. Tax losses **509.060**. Alarmbel since juni 2025 (EV 11% of kapitaal). Continuity art. 3:6, 6° (aandeelhouderssteun). Nuhma cv cash-deficiency clause ING **15.000.000** 27.06.2024. Overname 04.07.2024 van Monument Immo Management / Monument Real Estate Fund; gebouwen Herkenrodesingel 14+16 + magazijnen Oude Spoorbaan 100.14+100.15. Commissaris Moore **5.500**. 6.10 category/geo empty. 6.15 related-party refusal.
- CSVs: sources+4/entities+1/budgets+55/commitments+1/leaderboard+1 + FOI ready `gap_herk_omzet_2_62m_pnl_neg_0_39m_debt_27_45m_l5` (not sent); rq_1364=done; spawn rq_1365; ticks=1364.
- Coverage: residual dual L5 (Herkenrode leftover NV live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1370).
- Next: rq_1365 residual dual L5 VL JR2025 hole_fill (prefer leftover s-Lim DV 0805.138.503 only if a statutory 2025 WVV/BBC PDF now downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Herkenrode RE 1364 / MyCSN 1363 / s-Lim 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1364 write done")


if __name__ == "__main__":
    main()

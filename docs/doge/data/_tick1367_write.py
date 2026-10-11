# -*- coding: utf-8 -*-
"""Tick 1367 — leftover Leiedal JR2025 official NBB WVV euros.
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

TICK = "1367"
UTC = "2026-08-19T01:35:00Z"
ENT = "igs_leid"
HIER = "Vlaanderen>West-Vlaanderen>IGS>Leiedal>Streek"
GAP = "gap_leid_omzet_10_37m_inv_106_16m_pnl_neg_4_93m_l5"
SRC = "src_leid_jr2025_nbb"
SRC2 = "src_leid_site"
SRC3 = "src_kbo_leid_0205350681"
SRC4 = "src_leid_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00126956.pdf"
SRC2_URL = "https://www.leiedal.be/jaarverslagen"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0205350681"
SRC4_URL = "https://www.leiedal.be/contact"
FOI_EMAIL = "info@leiedal.be"
FOI_POSTAL = "President Kennedypark 10 8500 Kortrijk"
DRAFT = "docs/doge/foi/drafts/gap_leid_omzet_10_37m_inv_106_16m_pnl_neg_4_93m_l5.md"
COMM = "comm_leid_jr2025_pnl"
LB = "lb_leid_omzet_10_37m_inv_106_16m_debt"


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
                "title": "Intercommunale Leiedal jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00126956; AV 27.05.2026)",
                "url": SRC_URL,
                "publisher": "Intercommunale Leiedal / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1367; official NBB VOL-inb PDF 1.25MB 54p deposit 2026-00126956 created 30.05.2026 neerlegging 30.05.2026; "
                    "leftover IGS DV of mined Zuid-West-Vlaanderen cities; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Callens Vandelanotte B00003 / Frank Vandelanotte A01476 9099 + andere controle 23677; "
                    "site still jaarverslag 2024 + jaarrekening 2023 only"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Leiedal official publications (jaarverslag 2024; statutory balans still 2023 on site)",
                "url": SRC2_URL,
                "publisher": "Intercommunale Leiedal",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1367; leftover IGS of mined Zuid-West-Vlaanderen cities; "
                    "leiedal.be/jaarverslagen still jaarverslag 2024; jaarrekening PDF still 2023; "
                    "statutory 2025 balans is the NBB CDN deposit not the site"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Intercommunale Leiedal 0205.350.681",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1367; KBO 0205.350.681 Actief / normale toestand since 01.03.1966; "
                    "statutaire naam INTERCOMMUNALE LEIEDAL since 07.11.2003; "
                    "Dienstverlenende vereniging (Vlaams Gewest) since 17.11.2003; "
                    "zetel President Kennedypark 10 8500 Kortrijk since 07.11.2003; 1 VE; "
                    "btw since 01.01.1998; RSZ since 01.01.2022; aanbestedende overheid since 01.03.1966; "
                    "jaarvergadering mei; boekjaar 31 december; "
                    "KBO-bestuurders Wout Maddens since 26.04.2019 + Filip Vanhaverbeke since 01.06.2013; "
                    "no KBO email/web/tel; NACE 68.310/82.100/84.130"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Leiedal FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "Intercommunale Leiedal",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1367; FOI info@leiedal.be / 056 24 16 16; "
                    "President Kennedypark 10 8500 Kortrijk; no own KBO email/web/tel"
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
                "name_nl": "Intercommunale Leiedal (leftover dienstverlenende vereniging Zuid-West-Vlaanderen / IGS streek- en projectontwikkeling)",
                "name_fr": "Intercommunale Leiedal (association prestataire de services residuelle Flandre occidentale du Sud / IGS developpement regional)",
                "name_en": "Leiedal leftover South-West Flanders service association (regional development IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.leiedal.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1367 leftover residual IGS DV of mined Zuid-West-Vlaanderen cities; "
                    "KBO 0205.350.681 Actief since 01.03.1966; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 125577074 omzet 10372520 pnl -4932541; "
                    "FOI ready 6.10-geo/inv 106.16m/bank 75.10m/continuity/streekfonds/site-JR"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_leid_assets_2025", ENT, "2025", "125577074", "2025 assets 125577074 VOL-inb 20/58; commissaris 125577073.92; tick1367; primary official NBB WVV"),
        ("bud_leid_assets_2024", ENT, "2024", "130585618", "2024 assets 130585618 comparative; tick1367; primary official NBB WVV 20/58"),
        ("bud_leid_fixed_2025", ENT, "2025", "12294515", "2025 vaste activa 12294515; tick1367; primary official NBB WVV 21/28"),
        ("bud_leid_mva_2025", ENT, "2025", "11605634", "2025 MVA 11605634 (gebouwen 7245520 + machines 213932 + meubilair 105119 + overige 210979 + CIP 3830085); tick1367; primary official NBB WVV 22/27"),
        ("bud_leid_buildings_2025", ENT, "2025", "7245520", "2025 terreinen en gebouwen 7245520 JUMP vs 5359191; tick1367; primary official NBB WVV 22"),
        ("bud_leid_cip_2025", ENT, "2025", "3830085", "2025 activa in aanbouw 3830085 vs 4539073; tick1367; primary official NBB WVV 27"),
        ("bud_leid_fva_2025", ENT, "2025", "688880", "2025 FVA 688880 (deelnemingsverhouding 247894 + andere 440987); tick1367; primary official NBB WVV 28"),
        ("bud_leid_kanaal_2025", ENT, "2025", "247894", "2025 Kanaal 127 cv 0460937169 30.41pct / 1000 aandelen book 247894 EV 302188 PnL -28777 (2024); tick1367; primary official NBB WVV 282 6.5.1"),
        ("bud_leid_current_2025", ENT, "2025", "113282559", "2025 vlottende activa 113282559 vs 119506566; tick1367; primary official NBB WVV 29/58"),
        ("bud_leid_ltrecv_2025", ENT, "2025", "1323222", "2025 LT handelsvorderingen 1323222; tick1367; primary official NBB WVV 290"),
        ("bud_leid_inv_2025", ENT, "2025", "106156450", "2025 voorraden 106156450 all onroerend bestemd voor verkoop; tick1367; primary official NBB WVV 30/36 35"),
        ("bud_leid_inv_2024", ENT, "2024", "106932100", "2024 voorraden RE-for-sale 106932100 comparative; tick1367; primary official NBB WVV 35"),
        ("bud_leid_strecv_2025", ENT, "2025", "1810854", "2025 ST vorderingen 1810854 (trade 863671 + other 947183); tick1367; primary official NBB WVV 40/41"),
        ("bud_leid_invest_2025", ENT, "2025", "2614842", "2025 geldbeleggingen 2614842 DROP vs 4164842 (vastrentend 2000000); tick1367; primary official NBB WVV 50/53"),
        ("bud_leid_cash_2025", ENT, "2025", "1231988", "2025 liquide middelen 1231988 DROP vs 3560558 THIN vs bank 75.10m; tick1367; primary official NBB WVV 54/58"),
        ("bud_leid_cash_2024", ENT, "2024", "3560558", "2024 cash 3560558 comparative; tick1367; primary official NBB WVV 54/58"),
        ("bud_leid_equity_2025", ENT, "2025", "39393918", "2025 eigen vermogen 39393918 DROP vs 44514510; tick1367; primary official NBB WVV 10/15"),
        ("bud_leid_inbreng_2025", ENT, "2025", "2565483", "2025 onbeschikbare inbreng 2565483 / 60880 aandelen op naam; tick1367; primary official NBB WVV 111 8702"),
        ("bud_leid_reserves_2025", ENT, "2025", "34204174", "2025 reserves 34204174 (onbeschikbaar 256548 + beschikbaar 33947626); tick1367; primary official NBB WVV 13"),
        ("bud_leid_capsub_2025", ENT, "2025", "2624261", "2025 kapitaalsubsidies 2624261 vs 2812311; tick1367; primary official NBB WVV 15"),
        ("bud_leid_prov_2025", ENT, "2025", "4305724", "2025 voorzieningen 4305724 (pensioen 357842 + bedrijventerreinen 3947883); tick1367; primary official NBB WVV 16 6.8"),
        ("bud_leid_debt_2025", ENT, "2025", "81877432", "2025 schulden 81877432 vs 81721949; tick1367; primary official NBB WVV 17/49"),
        ("bud_leid_lt_2025", ENT, "2025", "62386717", "2025 LT schulden 62386717 (fin banks 60000000 + other 2386717); tick1367; primary official NBB WVV 17"),
        ("bud_leid_ltbank_2025", ENT, "2025", "60000000", "2025 LT kredietinstellingen 60000000 JUMP vs 54325000; tick1367; primary official NBB WVV 173"),
        ("bud_leid_st_2025", ENT, "2025", "19473123", "2025 ST schulden 19473123 DROP vs 24847819; tick1367; primary official NBB WVV 42/48"),
        ("bud_leid_stcurr_2025", ENT, "2025", "13100000", "2025 ST vervallend LT bank 13100000; tick1367; primary official NBB WVV 42 8841"),
        ("bud_leid_stbank_2025", ENT, "2025", "2000000", "2025 ST financieel kredietinstellingen 2000000 vs 0; tick1367; primary official NBB WVV 43 430/8"),
        ("bud_leid_sttrade_2025", ENT, "2025", "2293558", "2025 leveranciers 2293558 JUMP vs 866383; tick1367; primary official NBB WVV 440/4"),
        ("bud_leid_govg_2025", ENT, "2025", "73100000", "2025 door Belgische overheidsinstellingen gewaarborgde bankschuld 73100000; tick1367; primary official NBB WVV 9061"),
        ("bud_leid_ops_2025", ENT, "2025", "15459343", "2025 bedrijfsopbrengsten 15459343; tick1367; primary official NBB WVV 70/76A"),
        ("bud_leid_omzet_2025", ENT, "2025", "10372520", "2025 omzet 10372520; 6.10 category filed geo empty; tick1367; primary official NBB WVV 70"),
        ("bud_leid_omzet_2024", ENT, "2024", "10178018", "2024 omzet 10178018 comparative; tick1367; primary official NBB WVV 70"),
        ("bud_leid_othops_2025", ENT, "2025", "4924538", "2025 andere bedrijfsopbrengsten 4924538 waarvan subsidies 3660363; tick1367; primary official NBB WVV 74"),
        ("bud_leid_sub_2025", ENT, "2025", "3660363", "2025 exploitatiesubsidies/overheidscompensatie 3660363 vs 3416107; tick1367; primary official NBB WVV 740"),
        ("bud_leid_opscost_2025", ENT, "2025", "19732993", "2025 bedrijfskosten 19732993 vs 18001854; tick1367; primary official NBB WVV 60/66A"),
        ("bud_leid_goods_2025", ENT, "2025", "7888563", "2025 handelsgoederen/grond-hulp 7888563; tick1367; primary official NBB WVV 60"),
        ("bud_leid_diensten_2025", ENT, "2025", "2938783", "2025 diensten 2938783; tick1367; primary official NBB WVV 61"),
        ("bud_leid_pers_2025", ENT, "2025", "7950014", "2025 bezoldigingen 7950014 / 76.2 VTE / 83 koppen; tick1367; primary official NBB WVV 62 9087"),
        ("bud_leid_deprec_2025", ENT, "2025", "395345", "2025 afschrijvingen 395345; tick1367; primary official NBB WVV 630"),
        ("bud_leid_wvinv_2025", ENT, "2025", "542207", "2025 WV voorraden/vorderingen 542207 JUMP vs 1354; tick1367; primary official NBB WVV 631/4"),
        ("bud_leid_expl_2025", ENT, "2025", "-4273651", "2025 bedrijfsverlies 4273651 DROP vs -2300327; tick1367; primary official NBB WVV 9901"),
        ("bud_leid_expl_2024", ENT, "2024", "-2300327", "2024 bedrijfsverlies 2300327 comparative; tick1367; primary official NBB WVV 9901"),
        ("bud_leid_fincost_2025", ENT, "2025", "631840", "2025 financiele kosten 631840 (schulden 627232); tick1367; primary official NBB WVV 65"),
        ("bud_leid_intcap_2025", ENT, "2025", "1128910", "2025 geactiveerde interesten 1128910 vs 889910; tick1367; primary official NBB WVV 6502"),
        ("bud_leid_tax_2025", ENT, "2025", "123424", "2025 belastingen 123424 vs 184200; tick1367; primary official NBB WVV 67/77"),
        ("bud_leid_pnl_2025", ENT, "2025", "-4932541", "2025 PnL 9904 -4932541 DROP vs -2758808; commissaris -4932540.64; tick1367; primary official NBB WVV"),
        ("bud_leid_pnl_2024", ENT, "2024", "-2758808", "2024 PnL -2758808 comparative; tick1367; primary official NBB WVV 9904"),
        ("bud_leid_board_2025", ENT, "2025", "75309", "2025 bestuurdersbezoldiging 75309; tick1367; primary official NBB WVV 9503"),
        ("bud_leid_comm_2025", ENT, "2025", "9099", "2025 commissaris Callens Vandelanotte 9099 + andere controle 23677; tick1367; primary official NBB WVV 9505"),
        ("bud_leid_cat_bt_2025", ENT, "2025", "6188647", "2025 6.10 verkopen BT en WZ 6188647; tick1367; primary official NBB WVV 6.10"),
        ("bud_leid_cat_diensten_2025", ENT, "2025", "3550660", "2025 6.10 dienstprestaties 3550660; tick1367; primary official NBB WVV 6.10"),
        ("bud_leid_cat_huur_2025", ENT, "2025", "633213", "2025 6.10 verhuur en concessies 633213; tick1367; primary official NBB WVV 6.10"),
        ("bud_leid_streekfonds_2025", ENT, "2025", "2680000", "2025 6.20 streekfonds engagement tot 2030 geraamd 2680000; tick1367; primary official NBB WVV 6.20"),
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
                "title": "Leiedal JR2025 leftover IGS dual (assets 125.58m / omzet 10.37m / inventory 106.16m / PnL -4.93m)",
                "entity_id": ENT,
                "beneficiary": "Intercommunale Leiedal / Zuid-West-Vlaanderen municipalities / Kanaal 127 / streekfonds",
                "legal_basis": "WVV DV; decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-05-27",
                "start_year": "1966",
                "end_year": "2026",
                "total_envelope_eur": "125577074",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL streek/project — 106.16m RE inventory / 75.10m bank vs 1.23m cash / continuity herschikking",
                "cut_option": "Publish 6.10 geo + 106.16m project list + put 75.10m bank vs 1.23m cash and 73.10m gov-guarantee on the record + disclose 2026 bank herschikkingen + streekfonds 2.68m + site statutory JR; do not keep 125.58m municipal streek IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1367; assets 125577074 omzet 10372520 pnl -4932541; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Leiedal JR2025 leftover IGS: assets 125.58m / omzet 10.37m / inventory 106.16m / PnL -4.93m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "81877432",
                "total_cost_eur": "125577074",
                "tco_notes": (
                    "Leftover dual IGS DV of mined Zuid-West-Vlaanderen municipalities: "
                    "assets 125.58m / equity 39.39m / pnl -4.93m DROP vs -2.76m / omzet 10.37m / 76.2 VTE / "
                    "inventory RE 106.16m (84.5pct of assets) / bank 75.10m vs cash 1.23m / "
                    "gov-guarantee 73.10m / continuity herschikking 2026 / official NBB WVV live; "
                    "do not treat 125.58m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Intercommunale Leiedal / Zuid-West-Vlaanderen municipalities / Kanaal 127 / streekfonds",
                "stated_goal": "Local leftover IGS map VL streek/project — JR2025 live; dual inventory/bank/continuity FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 125.58m / omzet 10.37m / pnl -4.93m; inventory 106.16m; bank 75.10m vs cash 1.23m",
                "absurdity_score": "7.6",
                "cost_score": "7.4",
                "difficulty": "2.5",
                "priority_index": "7.1",
                "cut_proposal": "Publish 6.10 geo + 106.16m project list + put 75.10m bank vs 1.23m cash and 73.10m gov-guarantee on the record + disclose 2026 bank herschikkingen + streekfonds 2.68m + site statutory JR; do not keep 125.58m municipal streek IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1367; leftover IGS DV of mined Zuid-West-Vlaanderen; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "6.10 omzet 10372520 geo split empty (category filed: BT/WZ 6188647 / dienstprestaties 3550660 / verhuur 633213) "
                    "+ per-gemeente/afsprakennota counterparties "
                    "+ andere bedrijfsopbrengsten 4924538 of which subsidies 3660363 only (~1264175 unnamed) "
                    "+ inventory RE for sale 106156450 (84.5pct of assets) + WV voorraden 542716 + intercalaire interesten 1128910 project list "
                    "+ bank 75100000 (LT 60000000 + ST current 13100000 + ST 2000000) vs cash 1231988 DROP vs 3560558 "
                    "+ gov-guaranteed bank 73100000 unnamed grantor municipalities "
                    "+ continuity 2026 bank herschikkingen (jaarverslag VOL-inb 7) "
                    "+ streekfonds engagement 2680000 tot 2030 "
                    "+ Kanaal 127 cv 0460937169 30.41pct book 247894 + other FVA (luchthaven 3pct / BITLAR 8.62pct / Takeoff 4.8pct / XOM 1.98pct / XPO 0.25pct) + 6.18 consolidation sections not filed "
                    "+ 60880 aandelen / per-vennoot inleg/stem "
                    "+ official-site JR (leiedal.be still jaarverslag 2024 / jaarrekening 2023)"
                ),
                "why_it_matters": (
                    "Leftover IGS DV of mined Zuid-West-Vlaanderen cities "
                    "(same leftover-IGS seam as Interleuven 1366 / Interwaas 1350 / SOLVA 1351 / IGEAN 1341): "
                    "125.58m assets / 10.37m omzet / -4.93m pnl DROP vs -2.76m / 76.2 VTE / "
                    "106.16m RE inventory (84.5pct of assets) / 75.10m bank vs 1.23m cash / "
                    "73.10m gov-guarantee / 2026 bank herschikkingen / site still 2024 glossy "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "Intercommunale Leiedal / Wout Maddens / Zuid-West-Vlaanderen municipalities",
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
                    "tick1367 leftover IGS DV of mined Zuid-West-Vlaanderen cities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (1.25MB 54p deposit 2026-00126956). "
                    "Dommelhof leftover Limburg EVA KBO 0777.495.085 still no 2025/2026 PDF — skipped. "
                    "Interleuven already mined 1366 — skipped. Nuhma-group seam 1353-1365 skipped. "
                    "IOK DV 0204.212.714 now lists JR2025 CDN 2026-00307549 — leftover next, not taken. "
                    "Otary RS Nuhma-adjacent fallback not taken. IMOG/Haviland still 2024. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1367",
        "title": "Leiedal JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Intercommunale Leiedal leftover IGS DV of mined Zuid-West-Vlaanderen cities "
            "after honest hunt; KBO 0205.350.681 Actief; "
            "live JR2025 official NBB WVV VOL-inb PDF (1.25MB 54p deposit 2026-00126956; commissaris Callens Vandelanotte); "
            "sourced euros assets 125577074 / omzet 10372520 / pnl -4932541; "
            "FOI ready 6.10-geo/inv 106.16m/bank 75.10m/continuity/streekfonds/site-JR"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T01:05:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1367 Leiedal leftover IGS residual; KBO 0205.350.681; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1368 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1368",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1367 done including Leiedal 1367 leftover IGS live NBB WVV / "
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
            "IOK DV leftover Kempen IGS KBO 0204.212.714 — take if JR2025 CDN 2026-00307549 still live (listed this tick, not taken once Leiedal extracted); "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if a new live 2025 WVV PDF downloads (prefer leftover AGB/zorg/EVA/IGS/APB outside Nuhma first); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "IMOG / Haviland still 2024 — take only if a 2025 JR PDF now downloads; "
            "Veneco / IVOO / MIROM / INCOVO / IVAGO / MIWA / IVAREM / IGEMO — take only if a statutory 2025 WVV/BBC PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1367 after Leiedal leftover IGS live NBB WVV; next residual dual L5 VL; next every-10 is 1370",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1367", rq_new, rq_spawn)
    print("research_queue 1367", found, "spawned_1368", spawned)

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
                "last_unit_id": "rq_1367",
                "ticks_completed": "1367",
                "paused": "no",
                "notes": (
                    "tick1367 Leiedal leftover IGS residual; KBO 0205.350.681; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 125577074 omzet 10372520 pnl -4932541; "
                    "FOI ready 6.10-geo/inv 106.16m/bank 75.10m/continuity/streekfonds; next rq_1368 residual dual L5 VL; continuous hole_fill; next every-10 is 1370"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1367 - 2026-08-19 - rq_1367 Leiedal dual residual leftover
- Unit: Intercommunale Leiedal (leftover dienstverlenende vereniging / IGS streek- en projectontwikkeling of mined Zuid-West-Vlaanderen municipalities: Kortrijk / Waregem / Harelbeke / Izegem / Wevelgem / Menen / Zwevegem / Kuurne / Lendelede / Anzegem / Avelgem / Deerlijk / Wervik / Spiere-Helkijn) after residual dual hunt (KBO **0205.350.681**; official leiedal.be still jaarverslag 2024 + jaarrekening 2023 only; live NBB WVV VOL-inb deposit **2026-00126956** PDF 1.25MB / 54p; AV **27.05.2026**; PDF created **30.05.2026**; neerlegging **30.05.2026**; commissaris Callens, Vandelanotte & Theunissen BV B00003 / Frank Vandelanotte A01476 9.099 + andere controle 23.677). Leftover IGS DV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; previous ticks listed Leiedal as glossy-only). Distinct from already-mined Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **01.03.1966**; statutaire naam INTERCOMMUNALE LEIEDAL since 07.11.2003; Dienstverlenende vereniging (Vlaams Gewest) since 17.11.2003; zetel President Kennedypark 10 8500 Kortrijk since 07.11.2003; **1 VE**; btw since 01.01.1998; RSZ since 01.01.2022; aanbestedende overheid since 01.03.1966; jaarvergadering mei; KBO-bestuurders Wout Maddens since 26.04.2019 + Filip Vanhaverbeke since 01.06.2013; e-mail info@leiedal.be; tel 056 24 16 16; NACE 68.310/82.100/84.130. Hunt leftover AGB/zorg/EVA first: Dommelhof leftover Limburg EVA KBO 0777.495.085 still no 2025/2026 jaarrekening on Staatsbladmonitor — skipped; AGB MAC Mechelen 2025 BBC already mined tick1270 — skipped; Westtoer APB already mined — skipped; Nuhma-group seam 1353-1365 already mined — skipped; Interleuven already mined 1366 — skipped; Leiedal statutory CDN live this tick (HTTP 200 / 1252067 / 54p) — taken. IOK DV 0204.212.714 now lists JR2025 CDN 2026-00307549 — leftover next, not taken once live Leiedal extracted. IMOG/Haviland still 2024; POM Limburg glossy-only; Veneco glossy; IVAREM/IGEMO activiteitenverslag only; IVOO no public 2025 JR. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE no fetchable 2025 JR this tick. Otary RS Nuhma-adjacent fallback not taken. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350. Not every-10 (next 1370).
- EUR strong (primary official WVV VOL-inb; commissaris Callens Vandelanotte oordeel zonder voorbehoud assets 125.577.073,92 / PnL −4.932.540,64): assets **125.577.074** (was 130.585.618); fixed **12.294.515** / MVA **11.605.634** (gebouwen **7.245.520** JUMP vs 5.359.191 + machines 213.932 + meubilair 105.119 + overige 210.979 + CIP **3.830.085**); FVA **688.880** (Kanaal 127 cv 0460.937.169 **30,41%** / 1.000 aandelen book **247.894** EV 302.188 / PnL −28.777 boekjaar 2024; andere FVA 440.987: luchthaven Kortrijk-Wevelgem 3% / BITLAR 8,62% / Takeoff 4,8% / XOM 1,98% / XPO 0,25%); current **113.282.559**; LT recv **1.323.222**; inventory **106.156.450** all onroerend bestemd voor verkoop (84,5% of assets; was 106.932.100); ST recv **1.810.854**; beleggingen **2.614.842** DROP vs 4.164.842; cash **1.231.988 DROP** vs 3.560.558 THIN vs bank 75.10m; equity **39.393.918** (inbreng 2.565.483 onbeschikbaar / 60.880 aandelen; reserves 34.204.174; kapitaalsubsidies **2.624.261**); voorzieningen **4.305.724** (pensioen 357.842 + bedrijventerreinen **3.947.883**); schulden **81.877.432** (LT fin **60.000.000 JUMP** vs 54.325.000 + other 2.386.717; ST **19.473.123** waarvan ST current **13.100.000** + ST bank **2.000.000** + leveranciers 2.293.558); gov-guarantee **73.100.000**; omzet **10.372.520** (6.10 category: BT/WZ 6.188.647 / diensten 3.550.660 / verhuur 633.213; geo empty; comparative 10.178.018); andere opbr **4.924.538** (subsidies 3.660.363); goods 7.888.563; diensten 2.938.783; pers **7.950.014** / **76,2 VTE** / 83 koppen; afschr 395.345; WV inv **542.207** JUMP vs 1.354; expl **−4.273.651 DROP** vs −2.300.327; fin kosten **631.840**; geactiveerde interesten **1.128.910**; belasting 123.424; PnL **−4.932.541 DROP** vs −2.758.808; te bestemmen −4.932.541 onttrokken aan reserves; bestuurders 75.309. Continuity: 2026 kredieten vervallen / herschikkingsbesprekingen banken / streekfonds 2.680.000 tot 2030. 6.18 consolidatie-secties niet neergelegd. 6.15 related-party empty (gebrek wettelijke criteria).
- CSVs: sources+4/entities+1/budgets+53/commitments+1/leaderboard+1 + FOI ready `gap_leid_omzet_10_37m_inv_106_16m_pnl_neg_4_93m_l5` (not sent); rq_1367=done; spawn rq_1368; ticks=1367.
- Coverage: residual dual L5 (Leiedal leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1370).
- Next: rq_1368 residual dual L5 VL JR2025 hole_fill (prefer leftover IOK DV KBO 0204.212.714 CDN 2026-00307549 if still live; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS / Rematics / Sunfin only if a new live 2025 WVV PDF downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; IMOG/Haviland only if a 2025 JR PDF now downloads; Veneco/IVOO/MIWA/IVAREM/IGEMO only if a WVV/BBC PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1367 write done")


if __name__ == "__main__":
    main()

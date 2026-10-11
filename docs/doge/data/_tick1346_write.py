# -*- coding: utf-8 -*-
"""Tick 1346 — leftover IGS WVI West-Vlaamse Intercommunale JR2025 WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10 (next every-10 is 1350).
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1346"
UTC = "2026-08-18T20:45:00Z"
ENT = "igs_wvi"
HIER = "Vlaanderen>WestVlaanderen>IGS>WVI"
GAP = "gap_wvi_omzet_34_23m_stock_181_88m_pers_13_76m_l5"
SRC = "src_wvi_jr2025_pdf"
SRC2 = "src_wvi_site"
SRC3 = "src_kbo_wvi_0205157869"
SRC4 = "src_wvi_foi_contact"
SRC_URL = "https://www.wvi.be/sites/wvi/files/uploads/medias/publication/JV_2025_spreads.pdf"
SRC2_URL = "https://www.wvi.be/lokaal-bestuur/publicaties"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0205157869"
SRC4_URL = "https://www.wvi.be/"
FOI_EMAIL = "info@wvi.be"
FOI_POSTAL = "Koning Albert I-laan 122 bus 301 8200 Brugge"
DRAFT = "docs/doge/foi/drafts/gap_wvi_omzet_34_23m_stock_181_88m_pers_13_76m_l5.md"
COMM = "comm_wvi_jr2025_omzet"
LB = "lb_wvi_omzet_34_23m_stock_181_88m"


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
                "title": "WVI jaarverslag boekjaar 2025 (official PDF + embedded WVV VOL-kap; AV 10.06.2026 Tielt)",
                "url": SRC_URL,
                "publisher": "West-Vlaamse Intercommunale WVI",
                "accessed_date": "2026-08-18",
                "source_class": "budget",
                "notes": (
                    "tick1346; official PDF 47.20MB 140p spreads InDesign 04.06.2026; AV 10.06.2026 Tielt; "
                    "WVV VOL-kap WVI 0205.157.869 embedded; leftover IGS of mined West-Flanders cities; not BBC J1-J5"
                ),
            },
            {
                "source_id": SRC2,
                "title": "WVI official publicaties page (Jaarverslag 2025 listed)",
                "url": SRC2_URL,
                "publisher": "WVI",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1346; HTTP 200 lists JV_2025_spreads.pdf 47.20MB + short DIG folder; "
                    "leftover IGS of mined West-Flanders Brugge/Middenkust/Westhoek/Midwest cities"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO WVI West-Vlaamse Intercommunale 0205.157.869",
                "url": SRC3_URL,
                "publisher": "KBO Besloten vennootschap Public Search FOD Economie",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1346; KBO 0205.157.869 Actief / normale toestand since 30.05.1964; "
                    "statutaire naam West-Vlaamse Intercommunale since 21.10.2003; "
                    "afkorting WVI since 10.12.1999; Dienstverlenende vereniging (Vlaams Gewest) since 24.03.2004; "
                    "zetel Koning Albert I-laan 122 bus 301 8200 Brugge since 27.11.2024; 2 VE; RSZ since 01.01.2022; "
                    "btw since 01.01.1971; aanbestedende overheid since 30.05.1964; "
                    "jaarvergadering mei; boekjaar 31 december; NACE 71.121 / 84.120"
                ),
            },
            {
                "source_id": SRC4,
                "title": "WVI homepage / FOI channel",
                "url": SRC4_URL,
                "publisher": "WVI",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1346; FOI info@wvi.be from official PDF + short jaarverslag; "
                    "Koning Albert I-laan 122 bus 301 8200 Brugge; T +32 50 36 71 71; "
                    "codirectie Ann Tack / Johan Proot; voorzitter Dirk De fauw"
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
                "name_nl": "WVI West-Vlaamse Intercommunale (leftover IGS)",
                "name_fr": "WVI intercommunale Flandre occidentale (association de services / IGS residuel)",
                "name_en": "WVI West Flanders intermunicipal (leftover IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.wvi.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1346 leftover IGS residual of mined West-Flanders cities 52 vennoten Brugge/Middenkust/Westhoek/Midwest; "
                    "KBO 0205.157.869 Actief since 30.05.1964; official JR2025 WVV PDF downloads; "
                    "assets 240.992m omzet 34.226m stock 181.883m pers 13.761m expl 1.335m PnL 1.278m; "
                    "FOI ready omzet/stock/loans/NBB"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_wvi_assets_2025", ENT, "2025", "240991792", "2025 assets 240991792.06 was 239604133.02; tick1346; primary WVV in official PDF; commissaris confirms"),
        ("bud_wvi_fixed_2025", ENT, "2025", "22732658", "2025 vaste activa 22732657.60 was 19108656.75; tick1346; primary WVV 21/28"),
        ("bud_wvi_mva_2025", ENT, "2025", "22432564", "2025 MVA 22432563.68 (gebouwen 18712877 + installaties 76192.51 + rollend 253452.33 + overige 2016382.61 + CIP 1373659.23); tick1346; primary WVV"),
        ("bud_wvi_buildings_2025", ENT, "2025", "18712877", "2025 terreinen/gebouwen 18712877.00 was 16287153.02; tick1346; primary WVV"),
        ("bud_wvi_plant_2025", ENT, "2025", "76193", "2025 installaties 76192.51; tick1346; primary WVV"),
        ("bud_wvi_rolling_2025", ENT, "2025", "253452", "2025 meubilair/rollend 253452.33; tick1346; primary WVV"),
        ("bud_wvi_other_mva_2025", ENT, "2025", "2016383", "2025 overige MVA 2016382.61; tick1346; primary WVV"),
        ("bud_wvi_cip_2025", ENT, "2025", "1373659", "2025 CIP 1373659.23 JUMP vs 339464.21; tick1346; primary WVV"),
        ("bud_wvi_fva_2025", ENT, "2025", "300042", "2025 FVA 300042.34 (aandelen 300042.34) JUMP vs 180042.34; tick1346; primary WVV"),
        ("bud_wvi_current_2025", ENT, "2025", "218259134", "2025 vlottende activa 218259134.46 was 220495476.27; tick1346; primary WVV"),
        ("bud_wvi_lt_recv_2025", ENT, "2025", "127604", "2025 LT trade recv 127603.70 was 160377.31; tick1346; primary WVV"),
        ("bud_wvi_stock_2025", ENT, "2025", "181883498", "2025 voorraden onroerend voor verkoop 181883497.84 was 181702595.71; tick1346; primary WVV"),
        ("bud_wvi_st_recv_2025", ENT, "2025", "10061915", "2025 ST recv 10061914.62 JUMP vs 3205950.97 (trade 8298069.18 JUMP vs 1587511.69 + other 1763845.44); tick1346; primary WVV"),
        ("bud_wvi_invest_2025", ENT, "2025", "21898456", "2025 geldbeleggingen 21898456.31 DROP vs 29402029.68; tick1346; primary WVV"),
        ("bud_wvi_cash_2025", ENT, "2025", "4004506", "2025 cash 4004505.51 DROP vs 5730609.54; tick1346; primary WVV"),
        ("bud_wvi_accr_asset_2025", ENT, "2025", "283156", "2025 overlopende activa 283156.48; tick1346; primary WVV"),
        ("bud_wvi_equity_2025", ENT, "2025", "133457384", "2025 equity 133457384.42 was 132299827.72; tick1346; primary WVV 10/15"),
        ("bud_wvi_capital_2025", ENT, "2025", "13336600", "2025 geplaatst kapitaal 13336600 DROP vs 13449100 (Fluvius uittreding 112500); tick1346; primary WVV"),
        ("bud_wvi_reserves_2025", ENT, "2025", "119796644", "2025 reserves 119796643.80 (onbeschikbaar 5827064.80 + beschikbaar 113969579.00); tick1346; primary WVV"),
        ("bud_wvi_capsu_2025", ENT, "2025", "324141", "2025 kapitaalsubsidies 324140.62 was 332578.12; tick1346; primary WVV"),
        ("bud_wvi_prov_2025", ENT, "2025", "75360974", "2025 voorzieningen 75360974.21 (pensioen 11102822.38 + overige 64150104.96 + uitgesteld 108046.87); tick1346; primary WVV"),
        ("bud_wvi_debt_2025", ENT, "2025", "32173433", "2025 schulden 32173433.43 was 31106664.30; tick1346; primary WVV 17/49"),
        ("bud_wvi_lt_fin_2025", ENT, "2025", "19000000", "2025 LT financial banken 19000000 new; plus LT trade 375000; tick1346; primary WVV 6.9"),
        ("bud_wvi_st_debt_2025", ENT, "2025", "12018729", "2025 ST schulden 12018729.02 was 11164067.65; tick1346; primary WVV"),
        ("bud_wvi_trade_pay_2025", ENT, "2025", "3924379", "2025 leveranciers ST 3924379.20 JUMP vs 2781907.99; tick1346; primary WVV"),
        ("bud_wvi_taxsoc_2025", ENT, "2025", "2209382", "2025 tax/soc 2209382.38 (tax 446981.98 + wages 1762400.40); tick1346; primary WVV"),
        ("bud_wvi_ops_rev_2025", ENT, "2025", "39150195", "2025 bedrijfsopbrengsten 39150195.00 was 32901605.29; tick1346; primary WVV 70/76A"),
        ("bud_wvi_turnover_2025", ENT, "2025", "34225614", "2025 omzet 34225614.21 JUMP vs 18394219.39; narrative ondernemen 25.7m / wonen 4.2m / GO 0.1m / dienst 4.2m; tick1346; primary WVV 70"),
        ("bud_wvi_stockchange_2025", ENT, "2025", "180902", "2025 voorraadwijziging 180902.13 DROP vs 10402571.75; tick1346; primary WVV 71"),
        ("bud_wvi_otherops_2025", ENT, "2025", "4743679", "2025 andere bedrijfsopbrengsten 4743678.66 was 4104814.15; tick1346; primary WVV 74"),
        ("bud_wvi_ops_cost_2025", ENT, "2025", "37815032", "2025 bedrijfskosten 37815031.79 was 35697951.47; tick1346; primary WVV"),
        ("bud_wvi_goods_2025", ENT, "2025", "22616082", "2025 handelsgoederen 22616082.45; tick1346; primary WVV"),
        ("bud_wvi_services_2025", ENT, "2025", "1801397", "2025 diensten 1801396.79 JUMP vs 1467339.49; tick1346; primary WVV"),
        ("bud_wvi_pers_2025", ENT, "2025", "13761416", "2025 bezoldigingen 13761415.84 was 13818386.64; tick1346; primary WVV; avg VTE 103.6 / YE 101.2 / 110 koppen"),
        ("bud_wvi_uitzend_2025", ENT, "2025", "10367", "2025 uitzend 10367.20 VTE 0.3; tick1346; primary WVV sociale balans 152"),
        ("bud_wvi_ops_2025", ENT, "2025", "1335163", "2025 bedrijfswinst 1335163.21 was -2796346.18; tick1346; primary WVV 9901"),
        ("bud_wvi_fin_inc_2025", ENT, "2025", "607546", "2025 fin opbr 607545.64 (vlottend 584140.26); tick1346; primary WVV"),
        ("bud_wvi_fin_cost_2025", ENT, "2025", "667027", "2025 fin kosten 667027.15 JUMP vs 15137.20 (schulden 519203.66 + non-rec 154999); tick1346; primary WVV"),
        ("bud_wvi_pnl_2025", ENT, "2025", "1278494", "2025 PnL 1278494.20 was -2104801.58; added to beschikbare reserves; tick1346; primary WVV 9904 + commissaris"),
        ("bud_wvi_comm_fee_2025", ENT, "2025", "8016", "2025 commissaris Kantoor Hosten Walter Hosten 8015.65; tick1346; primary WVV 6.16"),
        ("bud_wvi_cash_invest_drop_2025", ENT, "2025", "9229677", "2025 beleggingen+cash DROP 9229677.40 (35132639.22 to 25902961.82) vs new 19m bank loans; tick1346; primary WVV"),
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
                "title": "WVI West-Vlaanderen JR2025 leftover IGS dual (omzet 34.23m / stock 181.88m / pers 13.76m / loans 19m)",
                "entity_id": ENT,
                "beneficiary": "WVI / 52 West-Vlaamse gemeentevennoten Brugge Middenkust Westhoek Midwest / Fluvius exited 2025",
                "legal_basis": "Decreet lokaal bestuur IGS; dienstverlenende vereniging; Bestuursdecreet openbaarheid; WVV neerlegging",
                "decision_date": "2026-06-10",
                "start_year": "1964",
                "end_year": "2025",
                "total_envelope_eur": "39150195",
                "cash_by_year": "",
                "remaining_eur": "133457384",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL West-Flanders — per-vennoot omzet / 181.88m land stock / 19m loans / NBB missing",
                "cut_option": "Publish per-vennoot 34.23m omzet + dual city lines + 181.88m land stock sites + 19m new loans vs cash DROP 9.23m; do not recreate parallel development-IGS shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1346; assets 240991792 omzet 34225614 stock 181883498 pers 13761416 expl 1335163 PnL 1278494 VTE 103.6; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "WVI West-Vlaanderen JR2025 leftover IGS: omzet 34.23m / stock 181.88m / pers 13.76m / loans 19m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "13761416",
                "total_cost_eur": "39150195",
                "tco_notes": "Leftover dual IGS of mined West-Flanders cities: ops rev 39.15m / omzet 34.23m JUMP / pers 13.76m VTE 103.6 / assets 240.99m / land stock 181.88m / new bank loans 19m vs cash+beleg DROP 9.23m / expl +1.34m / PnL +1.28m; do not treat 39.15m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "WVI / 52 West-Vlaamse gemeenten / Fluvius exited",
                "stated_goal": "Local leftover IGS map VL West-Flanders — JR2025 PDF live; dual omzet/stock/loans/NBB FOI",
                "measured_outcome": "Official PDF 2026-08-18: assets 240.99m / omzet 34.23m / stock 181.88m / pers 13.76m / expl +1.335m / PnL +1.278m / VTE 103.6",
                "absurdity_score": "6.4",
                "cost_score": "6.6",
                "difficulty": "3.0",
                "priority_index": "6.5",
                "cut_proposal": "Publish per-vennoot 34.23m omzet + dual city lines + 181.88m land stock sites + 19m new loans vs cash DROP 9.23m; do not recreate parallel development-IGS shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1346; leftover IGS of mined West-Flanders cities; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "Per-vennoot 2025-2026 dual lines for omzet 34225614.21 JUMP vs 18394219.39 "
                    "(narrative ondernemen 25.7m / wonen 4.2m / GO 0.1m / dienst 4.2m) + counterparties/age of "
                    "ST recv 10061914.62 JUMP vs 3205950.97 (trade 8298069.18) + composition/location of "
                    "voorraden onroerend voor verkoop 181883497.84 vs grondinvesteringen 6.3m / infra 13m "
                    "(Tielt Noord 3.7m) + destination of beleggingen+cash DROP 9229677.40 "
                    "(35132639.22 to 25902961.82) vs new LT bank loans 19000000 + fin kosten 667027.15 "
                    "JUMP vs 15137.20 + voorzieningen 75360974.21 vs equity 133457384.42 + Fluvius "
                    "kapitaalexit 112500 + pers 13761415.84 VTE 103.6 / YE 101.2 / 110 koppen "
                    "+ uitzend 10367.20 VTE 0.3 + NBB filing proof + commissarisverslag Kantoor Hosten "
                    "Walter Hosten / AV 10.06.2026 Tielt"
                ),
                "why_it_matters": (
                    "Leftover IGS shell of mined West-Flanders cities 52 vennoten "
                    "Brugge/Middenkust/Westhoek/Midwest: 39.15m ops / 34.23m omzet JUMP vs "
                    "13.76m personnel and 181.88m land inventory plus 19m new bank loans "
                    "while cash+beleg drop 9.23m is a dual opacity residual, "
                    "not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "WVI West-Vlaamse Intercommunale / 52 West-Vlaamse gemeentevennoten Brugge Middenkust Westhoek Midwest",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-18",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM,
                "linked_leaderboard_id": LB,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "tick1346 leftover IGS of mined West-Flanders cities after honest hunt; "
                    "live JR2025 official WVV PDF now downloads (47.20MB 140p VOL-kap AV 10.06.2026). "
                    "EcoWerf 2025 glossy 16MB / 2024 statutory still unpublished — not taken. "
                    "Interleuven still 2024 balans. IOK/IMOG/Haviland/IVBO/IVIO/Limburg.net still 2024. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1346",
        "title": "WVI West-Vlaanderen JR2025 leftover IGS dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: WVI leftover IGS of mined West-Flanders cities after honest hunt; "
            "KBO 0205.157.869 Actief; live JR2025 official WVV PDF (47.20MB 140p VOL-kap AV 10.06.2026); "
            "sourced euros assets 240.992m / omzet 34.226m / stock 181.883m / pers 13.761m / expl 1.335m / PnL 1.278m / VTE 103.6; "
            "FOI ready omzet/stock/loans/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T20:15:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1346 WVI leftover IGS residual; KBO 0205.157.869; live JR2025 WVV PDF; "
            "sourced euros; FOI ready not sent; next rq_1347 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1347",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1346 done including WVI West-Vlaanderen 1346 leftover IGS live WVV / "
            "IVVO Veurne-Ommeland 1345 leftover IGS live WVV / "
            "ILvA Land van Aalst 1344 leftover IGS live WVV / "
            "IVM Meetjesland 1343 leftover IGS live WVV / "
            "IDM Durme-Moervaart 1342 leftover IGS live WVV / "
            "IGEAN dienstverlening 1341 leftover IGS live WVV / "
            "EVA Limburg Sterk Merk 1340 leftover EVA live WVV + every-10 / "
            "WV Zorgbedrijf Brasschaat 1339 leftover zorg live BBC / "
            "WV Zorgband 1338 leftover zorg live BBC / WV Sleutelzorg 1337 leftover zorg FOI-unpublished / "
            "WV Weldenderend 1336 leftover zorg live BBC / WV BVK 1335 leftover zorg live BBC / "
            "WV OPcura 1334 leftover zorg live BBC / WV Het Dak 1333 leftover zorg live BBC / "
            "EVA Inagro 1332 FOI-unpublished / APB Vormingscentrum Malle 1331 FOI-glossy-not-BBC / "
            "EVA Kinderopvang Dilbeek 1330 FOI-unpublished + every-10); "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "Welzijnskoepel West-Brabant jaarverslag 2025 glossy-only — take only if a BBC PDF now downloads; "
            "Ter Nethe official still unpublished/DNS — take only if a PDF now downloads; "
            "Veneco glossy 25MB jaarverslag 2025 InDesign — take only if a WVV/BBC PDF now downloads; "
            "EcoWerf 2025 jaarverslag listed ~16MB glossy / 2024 statutory still unpublished — take only if a WVV/BBC PDF now downloads; "
            "Leiedal 2025 InDesign 22MB listed — take only if a WVV/BBC PDF now downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland / IVBO / IVIO / Limburg.net still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
            "WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / "
            "WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / "
            "Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / "
            "APB Vonk 1325 / APB Campus Vesta 1324 / AGB Blankenberge 1323 / AGB Aarschot / AGB Arendonk / AGB Lokeren; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403; not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1346 after WVI leftover IGS live WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1346", rq_new, rq_spawn)
    print("research_queue 1346", found, "spawned_1347", spawned)

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
                "last_unit_id": "rq_1346",
                "ticks_completed": "1346",
                "paused": "no",
                "notes": (
                    "tick1346 WVI leftover IGS residual; KBO 0205.157.869; "
                    "live JR2025 WVV PDF; sourced euros assets 240.992m omzet 34.226m stock 181.883m pers 13.761m expl 1.335m PnL 1.278m; "
                    "FOI ready; next rq_1347 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log_entry = """
### Tick 1346 - 2026-08-18 - rq_1346 WVI West-Vlaanderen dual residual leftover IGS
- Unit: WVI West-Vlaamse Intercommunale (dienstverlenende vereniging / leftover IGS) of already-mined West-Flanders cities (52 vennoten Brugge / Middenkust / Westhoek / Midwest) after residual dual hunt (KBO **0205.157.869**; official wvi.be + live jaarverslag 2025 PDF 47.20MB / 140p spreads; InDesign **04.06.2026**; AV **10.06.2026** Tielt; WVV VOL-kap embedded). Prefer live PDF over another unpublished FOI. Distinct from already-mined IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340. KBO Actief / normale toestand since **30.05.1964**; statutaire naam West-Vlaamse Intercommunale since 21.10.2003; afkorting WVI since 10.12.1999; Dienstverlenende vereniging (Vlaams Gewest) since 24.03.2004; zetel Koning Albert I-laan 122 bus 301 8200 Brugge since 27.11.2024; **2 VE**; RSZ-werkgever since 01.01.2022; btw since 01.01.1971; aanbestedende overheid since 30.05.1964; jaarvergadering mei; boekjaar 31 december; voorzitter Dirk De fauw; codirectie Ann Tack / Johan Proot since 09.2025; commissaris Kantoor Hosten / Walter Hosten (IBR A01441; BE 0450.010.318; mandaat AV 13.12.2023 tot boekjaar 2026); e-mail info@wvi.be on official PDF; tel +32 50 36 71 71; NACE 71.121 / 84.120. Hunt leftover AGB/zorg/EVA first: EcoWerf 2025 glossy 16.38MB downloaded — narrative 54.25m opbr / 54.28m kosten / VTE 351.38 — 2024 statutory still "wordt weldra gepubliceerd" — not taken once live WVI WVV downloaded; Interleuven publications still only jaarrekening 2024 PDF; IOK/IMOG/Haviland/IVBO/IVIO/Limburg.net still 2024; MIWA lists Jaarverslag 2025 heading but PDFs only to 2024; IVAGO SSL / activiteitenverslag glossy; ISVAG jaarverslag still 2023; IVAREM still 2024; Leiedal 2025 InDesign 22MB listed — not taken once live WVI WVV downloaded; Dommelhof leftover Limburg EVA KBO 0777.495.085 not taken once live WVI PDF downloaded. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek not taken once live WVI PDF downloaded. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331. Not every-10 (next 1350).
- EUR strong (primary WVV VOL-kap in official PDF; commissaris confirms assets 240.991.792,06 / PnL 1.278.494,20): assets **240.991.792** (was 239.604.133); fixed **22.732.658**; IVA **52**; MVA **22.432.564** (gebouwen **18.712.877** + installaties **76.193** + rollend **253.452** + overige **2.016.383** + CIP **1.373.659**); FVA **300.042**; current **218.259.134**; LT recv **127.604**; voorraden **181.883.498** (onroerend voor verkoop); ST recv **10.061.915** JUMP vs 3.205.951 (trade **8.298.069** JUMP vs 1.587.512); beleggingen **21.898.456** DROP vs 29.402.030; cash **4.004.506** DROP vs 5.730.610; equity **133.457.384**; kapitaal **13.336.600** DROP vs 13.449.100 (Fluvius uittreding **112.500**); reserves **119.796.644** (beschikbaar **113.969.579**); kapitaalsubsidies **324.141**; voorzieningen **75.360.974** (pensioen **11.102.822** + overige **64.150.105**); schulden **32.173.433**; LT fin **19.000.000** new banken; ST **12.018.729** (trade **3.924.379** + vooruit **1.434.362** + tax/soc **2.209.382** + other **4.450.605**); ops rev **39.150.195**; omzet **34.225.614** JUMP vs 18.394.219 (narrative ondernemen **25,7m** / wonen **4,2m** / GO **0,1m** / dienst **4,2m**); voorraadwijziging **180.902**; andere **4.743.679**; pers **13.761.416**; avg VTE **103,6** / YE **101,2** / 110 koppen; uitzend **10.367** VTE 0,3; diensten **1.801.397**; goods **22.616.082**; expl **1.335.163**; fin opbr **607.546**; fin kosten **667.027** JUMP vs 15.137; PnL **1.278.494**. Commissaris Hosten **8.016**. Oordeel zonder voorbehoud.
- CSVs: sources+4/entities+1/budgets+41/commitments+1/leaderboard+1 + FOI ready `gap_wvi_omzet_34_23m_stock_181_88m_pers_13_76m_l5` (not sent); rq_1346=done; spawn rq_1347; ticks=1346.
- Coverage: residual dual L5 (WVI leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1347 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland/IVBO/IVIO/Limburg.net only if a 2025 JR PDF now downloads; EcoWerf only if a statutory WVV/BBC PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 unless a fetchable JR appears).
"""
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1346 write done")


if __name__ == "__main__":
    main()

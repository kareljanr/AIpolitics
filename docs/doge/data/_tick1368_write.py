# -*- coding: utf-8 -*-
"""Tick 1368 — leftover IOK DV JR2025 official NBB WVV euros.
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

TICK = "1368"
UTC = "2026-08-19T02:20:00Z"
ENT = "igs_iokd"
HIER = "Vlaanderen>Antwerpen>IGS>IOK>Kempen"
GAP = "gap_iokd_othops_18_03m_inv_62_18m_invest_52_87m_l5"
SRC = "src_iokd_jr2025_nbb"
SRC2 = "src_iokd_site"
SRC3 = "src_kbo_iokd_0204212714"
SRC4 = "src_iokd_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00307549.pdf"
SRC2_URL = "https://www.iok.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0204212714"
SRC4_URL = "https://www.iok.be/contact"
FOI_EMAIL = "info@iok.be"
FOI_POSTAL = "Antwerpseweg 1 2440 Geel"
DRAFT = "docs/doge/foi/drafts/gap_iokd_othops_18_03m_inv_62_18m_invest_52_87m_l5.md"
COMM = "comm_iokd_jr2025_pnl"
LB = "lb_iokd_othops_18_03m_inv_62_18m_invest_52_87m"


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
                "title": "IOK jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00307549; AV 19.06.2026)",
                "url": SRC_URL,
                "publisher": "IOK / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1368; official NBB VOL-inb PDF 6.04MB 130p deposit 2026-00307549 created 18.07.2026 neerlegging 15.07.2026; "
                    "leftover IGS DV of mined Kempen cities; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris EY Bedrijfsrevisoren BV B160 / Christoph Oris A02341 17424; "
                    "6.4.1/6.5.1/6.8/6.20 not filed; commissarisverslag image-only p118-121"
                ),
            },
            {
                "source_id": SRC2,
                "title": "IOK official site (dienstverlenende vereniging 29 Kempense gemeenten)",
                "url": SRC2_URL,
                "publisher": "Interkommunale Ontwikkelingsmaatschappij voor de Kempen",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1368; leftover IGS of mined Kempen cities; "
                    "iok.be TLS failed from this box; statutory 2025 balans is the NBB CDN deposit not the site"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO IOK 0204.212.714",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1368; KBO 0204.212.714 Actief / normale toestand since 13.11.1968; "
                    "statutaire naam Interkommunale Ontwikkelingsmaatschappij voor de Kempen / I.O.K. since 01.01.1969; "
                    "Dienstverlenende vereniging (Vlaams Gewest) since 11.05.1993; "
                    "zetel Antwerpseweg 1 2440 Geel since 31.12.1985; 5 VE; "
                    "btw since 01.10.1977; RSZ since 01.01.2022; aanbestedende overheid since 13.11.1968; "
                    "jaarvergadering mei; boekjaar 31 december; "
                    "15 KBO-bestuurders incl. voorzitter Ward Kennes; "
                    "no KBO email/web/tel; NACE 84.130/68.203/84.119/68.110"
                ),
            },
            {
                "source_id": SRC4,
                "title": "IOK FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "IOK",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1368; FOI info@iok.be / 014 53 53 00; "
                    "Antwerpseweg 1 2440 Geel; no own KBO email/web/tel"
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
                "name_nl": "IOK Interkommunale Ontwikkelingsmaatschappij voor de Kempen (leftover dienstverlenende vereniging Kempen / IGS streek- en projectontwikkeling)",
                "name_fr": "IOK Intercommunale de developpement de la Campine (association prestataire de services residuelle / IGS developpement regional)",
                "name_en": "IOK leftover Kempen service association (regional development IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.iok.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1368 leftover residual IGS DV of mined Kempen cities; "
                    "KBO 0204.212.714 Actief since 13.11.1968; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 163272484 omzet 4999438 pnl 1466438; "
                    "FOI ready othops 18.03m/inv 62.18m/invest 52.87m/pension 10.33m"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_iokd_assets_2025", ENT, "2025", "163272484", "2025 assets 163272484 VOL-inb 20/58; tick1368; primary official NBB WVV"),
        ("bud_iokd_assets_2024", ENT, "2024", "160249951", "2024 assets 160249951 comparative; tick1368; primary official NBB WVV 20/58"),
        ("bud_iokd_fixed_2025", ENT, "2025", "39467439", "2025 vaste activa 39467439; tick1368; primary official NBB WVV 21/28"),
        ("bud_iokd_immat_2025", ENT, "2025", "226922", "2025 immateriele VA 226922 vs 45113; tick1368; primary official NBB WVV 21"),
        ("bud_iokd_mva_2025", ENT, "2025", "39174192", "2025 MVA 39174192 (gebouwen 21487838 + machines 419017 + meubilair 14846 + overige 17252491); tick1368; primary official NBB WVV 22/27"),
        ("bud_iokd_buildings_2025", ENT, "2025", "21487838", "2025 terreinen en gebouwen 21487838 DROP vs 23097128; tick1368; primary official NBB WVV 22"),
        ("bud_iokd_othermva_2025", ENT, "2025", "17252491", "2025 overige MVA 17252491 JUMP vs 15195693; tick1368; primary official NBB WVV 26"),
        ("bud_iokd_fva_2025", ENT, "2025", "66325", "2025 FVA 66325 (deelnemingsverhouding 31000 + andere 35325); 6.4.1/6.5.1 not filed; tick1368; primary official NBB WVV 28"),
        ("bud_iokd_current_2025", ENT, "2025", "123805044", "2025 vlottende activa 123805044 vs 121445379; tick1368; primary official NBB WVV 29/58"),
        ("bud_iokd_inv_2025", ENT, "2025", "62335305", "2025 voorraden+bestellingen 62335305 (RE-for-sale 62175899 + vooruit 6532 + WIP 152873); tick1368; primary official NBB WVV 3"),
        ("bud_iokd_invre_2025", ENT, "2025", "62175899", "2025 onroerend bestemd voor verkoop 62175899 (38.1pct of assets); tick1368; primary official NBB WVV 35"),
        ("bud_iokd_invre_2024", ENT, "2024", "61957732", "2024 voorraden RE-for-sale 61957732 comparative; tick1368; primary official NBB WVV 35"),
        ("bud_iokd_strecv_2025", ENT, "2025", "6187816", "2025 ST vorderingen 6187816 (trade 4008092 + other 2179724); tick1368; primary official NBB WVV 40/41"),
        ("bud_iokd_invest_2025", ENT, "2025", "52871636", "2025 geldbeleggingen 52871636 (aandelen 52867325 + termijn 4311); issuer list empty 6.6; tick1368; primary official NBB WVV 50/53"),
        ("bud_iokd_invest_2024", ENT, "2024", "53902916", "2024 geldbeleggingen 53902916 comparative; tick1368; primary official NBB WVV 50/53"),
        ("bud_iokd_shares_2025", ENT, "2025", "52867325", "2025 aandelen-beleggingen 52867325 (8681); tick1368; primary official NBB WVV 51"),
        ("bud_iokd_cash_2025", ENT, "2025", "2006742", "2025 liquide middelen 2006742 JUMP vs 1066533 THIN vs 52.87m aandelen; tick1368; primary official NBB WVV 54/58"),
        ("bud_iokd_cash_2024", ENT, "2024", "1066533", "2024 cash 1066533 comparative; tick1368; primary official NBB WVV 54/58"),
        ("bud_iokd_equity_2025", ENT, "2025", "137104637", "2025 eigen vermogen 137104637 vs 135920201; tick1368; primary official NBB WVV 10/15"),
        ("bud_iokd_inbreng_2025", ENT, "2025", "15642075", "2025 onbeschikbare inbreng 15642075 / 625723 aandelen (A 625093 gemeenten / B 200 WZK / C 430); tick1368; primary official NBB WVV 111"),
        ("bud_iokd_reserves_2025", ENT, "2025", "119425973", "2025 reserves 119425973 (onbeschikbaar 1950055 + beschikbaar 117475918); tick1368; primary official NBB WVV 13"),
        ("bud_iokd_capsub_2025", ENT, "2025", "2015592", "2025 kapitaalsubsidies 2015592 vs 2297594; tick1368; primary official NBB WVV 15"),
        ("bud_iokd_prov_2025", ENT, "2025", "12484741", "2025 voorzieningen 12484741 (pensioen 10333741 + overige 2151000 JUMP vs 200000); tick1368; primary official NBB WVV 16"),
        ("bud_iokd_pension_2025", ENT, "2025", "10333741", "2025 responsabiliseringsbijdrage vastbenoemden 10333740.91 geen verdiscontering; tick1368; primary official NBB WVV 160 6.14"),
        ("bud_iokd_othprov_2025", ENT, "2025", "2151000", "2025 overige risico's 2151000 JUMP vs 200000 (toevoegingen 2175101); 6.8 not filed; tick1368; primary official NBB WVV 164/5"),
        ("bud_iokd_debt_2025", ENT, "2025", "13683106", "2025 schulden 13683106 vs 13596149; LT empty; tick1368; primary official NBB WVV 17/49"),
        ("bud_iokd_st_2025", ENT, "2025", "10745565", "2025 ST schulden 10745565; tick1368; primary official NBB WVV 42/48"),
        ("bud_iokd_stbank_2025", ENT, "2025", "31", "2025 ST financieel kredietinstellingen 31; tick1368; primary official NBB WVV 43"),
        ("bud_iokd_sttrade_2025", ENT, "2025", "3509905", "2025 leveranciers 3509905; tick1368; primary official NBB WVV 440/4"),
        ("bud_iokd_stoth_2025", ENT, "2025", "4774297", "2025 overige schulden 4774297; tick1368; primary official NBB WVV 47/48"),
        ("bud_iokd_accr_2025", ENT, "2025", "2937541", "2025 overlopend passief 2937541 (te betalen 2070055 + over te dragen 867486); tick1368; primary official NBB WVV 492/3"),
        ("bud_iokd_ops_2025", ENT, "2025", "23365447", "2025 bedrijfsopbrengsten 23365447; tick1368; primary official NBB WVV 70/76A"),
        ("bud_iokd_omzet_2025", ENT, "2025", "4999438", "2025 omzet 4999438; 6.10 category+geo filed; tick1368; primary official NBB WVV 70"),
        ("bud_iokd_omzet_2024", ENT, "2024", "4626164", "2024 omzet 4626164 comparative; tick1368; primary official NBB WVV 70"),
        ("bud_iokd_othops_2025", ENT, "2025", "18029791", "2025 andere bedrijfsopbrengsten 18029791 waarvan subsidies 2576328 only (~15453463 unnamed); tick1368; primary official NBB WVV 74"),
        ("bud_iokd_sub_2025", ENT, "2025", "2576328", "2025 exploitatiesubsidies/overheidscompensatie 2576328 vs 2424313; tick1368; primary official NBB WVV 740"),
        ("bud_iokd_opscost_2025", ENT, "2025", "23122364", "2025 bedrijfskosten 23122364 vs 22722888; tick1368; primary official NBB WVV 60/66A"),
        ("bud_iokd_goods_2025", ENT, "2025", "3060301", "2025 handelsgoederen/grond-hulp 3060301; tick1368; primary official NBB WVV 60"),
        ("bud_iokd_diensten_2025", ENT, "2025", "4508164", "2025 diensten 4508164; tick1368; primary official NBB WVV 61"),
        ("bud_iokd_pers_2025", ENT, "2025", "11111594", "2025 bezoldigingen 11111594 / 109.4 VTE / 149 koppen; tick1368; primary official NBB WVV 62 9087"),
        ("bud_iokd_deprec_2025", ENT, "2025", "1653493", "2025 afschrijvingen 1653493; tick1368; primary official NBB WVV 630"),
        ("bud_iokd_expl_2025", ENT, "2025", "243083", "2025 bedrijfswinst 243083 vs -58782; tick1368; primary official NBB WVV 9901"),
        ("bud_iokd_expl_2024", ENT, "2024", "-58782", "2024 bedrijfsverlies 58782 comparative; tick1368; primary official NBB WVV 9901"),
        ("bud_iokd_fininc_2025", ENT, "2025", "1152569", "2025 financiele opbrengsten 1152569 (meerwaarde vlottende 858528 + capsub 282002); tick1368; primary official NBB WVV 75"),
        ("bud_iokd_gain_2025", ENT, "2025", "858528", "2025 meerwaarde realisatie vlottende activa 858528; tick1368; primary official NBB WVV 6.11"),
        ("bud_iokd_fincost_2025", ENT, "2025", "-70787", "2025 financiele kosten -70787 (schulden 111658 + WV-terugname); tick1368; primary official NBB WVV 65"),
        ("bud_iokd_pnl_2025", ENT, "2025", "1466438", "2025 PnL 9904 1466438 vs 1157878; added to overige reserves; tick1368; primary official NBB WVV"),
        ("bud_iokd_pnl_2024", ENT, "2024", "1157878", "2024 PnL 1157878 comparative; tick1368; primary official NBB WVV 9904"),
        ("bud_iokd_board_2025", ENT, "2025", "49107", "2025 bestuurdersbezoldiging 49107; tick1368; primary official NBB WVV 9503"),
        ("bud_iokd_comm_2025", ENT, "2025", "17424", "2025 commissaris EY 17424; tick1368; primary official NBB WVV 9505"),
        ("bud_iokd_cat_ind_2025", ENT, "2025", "1162672", "2025 6.10 industrie- en ambachtszones 1162672; tick1368; primary official NBB WVV 6.10"),
        ("bud_iokd_cat_woon_2025", ENT, "2025", "629925", "2025 6.10 woonzones 629925; tick1368; primary official NBB WVV 6.10"),
        ("bud_iokd_cat_studio_2025", ENT, "2025", "3206841", "2025 6.10 studiebureau-opdrachten 3206841; tick1368; primary official NBB WVV 6.10"),
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
                "title": "IOK JR2025 leftover IGS dual (assets 163.27m / othops 18.03m / inventory 62.18m / invest 52.87m / PnL 1.47m)",
                "entity_id": ENT,
                "beneficiary": "IOK / 29 Kempen municipalities / Welzijnszorg Kempen / OCMW+PZ+HVZ",
                "legal_basis": "WVV DV; decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-06-19",
                "start_year": "1968",
                "end_year": "2026",
                "total_envelope_eur": "163272484",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL streek/project — 18.03m other opbr / 62.18m RE inventory / 52.87m share investments",
                "cut_option": "Publish 15.45m unnamed other-opbr counterparties + 52.87m aandelen issuer list + 62.18m project list + pension 10.33m actuarial note + other-prov JUMP 2.15m; do not keep 163.27m municipal Kempen IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1368; assets 163272484 omzet 4999438 othops 18029791 pnl 1466438; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "IOK JR2025 leftover IGS: assets 163.27m / othops 18.03m / inv 62.18m / invest 52.87m / PnL 1.47m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "18029791",
                "total_cost_eur": "163272484",
                "tco_notes": (
                    "Leftover dual IGS DV of mined Kempen municipalities: "
                    "assets 163.27m / equity 137.10m / pnl 1.47m / omzet 5.00m / 109.4 VTE / "
                    "other opbr 18.03m of which subsidies 2.58m only / inventory RE 62.18m / "
                    "share investments 52.87m vs cash 2.01m / pension 10.33m / official NBB WVV live; "
                    "do not treat 163.27m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "IOK / 29 Kempen municipalities / Welzijnszorg Kempen",
                "stated_goal": "Local leftover IGS map VL streek/project — JR2025 live; dual othops/invest/inventory FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 163.27m / omzet 5.00m / othops 18.03m / pnl 1.47m; inv 62.18m; invest 52.87m vs cash 2.01m",
                "absurdity_score": "7.4",
                "cost_score": "7.6",
                "difficulty": "2.5",
                "priority_index": "7.0",
                "cut_proposal": "Publish 15.45m unnamed other-opbr counterparties + 52.87m aandelen issuer list + 62.18m project list + pension 10.33m actuarial note + other-prov JUMP 2.15m; do not keep 163.27m municipal Kempen IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1368; leftover IGS DV of mined Kempen; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "andere bedrijfsopbrengsten 18029791 of which subsidies 2576328 only (~15453463 unnamed grantor/tegenpartij) "
                    "+ 6.10 omzet 4999438 studiebureau 3206841 per-gemeente counterparties "
                    "+ inventory RE for sale 62175899 (38.1pct of assets) project list "
                    "+ geldbeleggingen aandelen 52867325 issuer list empty (6.6) vs cash 2006742 "
                    "+ meerwaarde vlottende 858528 "
                    "+ pension responsabilisering 10333741 no discount + other-prov JUMP 2151000 vs 200000 (6.8 not filed) "
                    "+ overige schulden 4774297 + accruals 2937541 "
                    "+ 6.4.1/6.5.1/6.8/6.20 not filed "
                    "+ 625723 aandelen / per-vennoot inleg/stem "
                    "+ official-site JR (iok.be TLS failed this box) + readable commissarisverslag (p118-121 image-only)"
                ),
                "why_it_matters": (
                    "Leftover IGS DV of mined Kempen cities "
                    "(same leftover-IGS seam as Leiedal 1367 / Interleuven 1366 / Interwaas 1350 / SOLVA 1351 / IGEAN 1341): "
                    "163.27m assets / 5.00m omzet / 18.03m other opbr / 1.47m pnl / 109.4 VTE / "
                    "62.18m RE inventory / 52.87m share investments vs 2.01m cash / "
                    "10.33m pension / site TLS "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "IOK / Ward Kennes / 29 Kempen municipalities",
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
                    "tick1368 leftover IGS DV of mined Kempen cities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (6.04MB 130p deposit 2026-00307549). "
                    "Leiedal already mined 1367 — skipped. Interleuven already mined 1366 — skipped. "
                    "Nuhma-group seam 1353-1365 skipped. "
                    "Dommelhof leftover Limburg EVA not re-probed once live IOK extracted. "
                    "Otary RS Nuhma-adjacent fallback not taken. IMOG/Haviland still 2024 as of 1367. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1368",
        "title": "IOK DV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: IOK leftover IGS DV of mined Kempen cities "
            "after honest hunt; KBO 0204.212.714 Actief; "
            "live JR2025 official NBB WVV VOL-inb PDF (6.04MB 130p deposit 2026-00307549; commissaris EY Oris); "
            "sourced euros assets 163272484 / omzet 4999438 / othops 18029791 / pnl 1466438; "
            "FOI ready othops 18.03m/inv 62.18m/invest 52.87m/pension 10.33m"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T01:35:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1368 IOK leftover IGS residual; KBO 0204.212.714; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1369 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1369",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1368 done including IOK 1368 leftover IGS live NBB WVV / "
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
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if a new live 2025 WVV PDF downloads (prefer leftover AGB/zorg/EVA/IGS/APB outside Nuhma first); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "IMOG / Haviland still 2024 — take only if a 2025 JR PDF now downloads; "
            "Veneco / IVOO / MIROM / INCOVO / IVAGO / MIWA / IVAREM / IGEMO — take only if a statutory 2025 WVV/BBC PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1368 after IOK leftover IGS live NBB WVV; next residual dual L5 VL; next every-10 is 1370",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1368", rq_new, rq_spawn)
    print("research_queue 1368", found, "spawned_1369", spawned)

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
                "last_unit_id": "rq_1368",
                "ticks_completed": "1368",
                "paused": "no",
                "notes": (
                    "tick1368 IOK leftover IGS residual; KBO 0204.212.714; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 163272484 omzet 4999438 othops 18029791 pnl 1466438; "
                    "FOI ready othops 18.03m/inv 62.18m/invest 52.87m; next rq_1369 residual dual L5 VL; continuous hole_fill; next every-10 is 1370"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1368 - 2026-08-19 - rq_1368 IOK dual residual leftover
- Unit: Interkommunale Ontwikkelingsmaatschappij voor de Kempen / IOK (leftover dienstverlenende vereniging / IGS streek- en projectontwikkeling of mined Kempen municipalities: 29 A-aandeelhouders Turnhout 53.877 / Heist-op-den-Berg 50.581 / Geel 46.100 / Mol 42.910 / Herentals 34.801 / Westerlo 29.302 / Nijlen 27.757 / Balen 26.410 / Kasterlee 23.538 / Hoogstraten 22.617 / Beerse / Laakdal / Lille / Herselt / Oud-Turnhout / Ravels / Arendonk / Olen / Grobbendonk / Rijkevorsel / Vosselaar / Retie / Meerhout / Dessel / Herenthout / Hulshout / Merksplas / Vorselaar / Baarle-Hertog; plus B Welzijnszorg Kempen 200; C OCMW+8 PZ+2 HVZ+4 WV 430; totaal 625.723 aandelen) after residual dual hunt (KBO **0204.212.714**; official iok.be TLS failed this box; live NBB WVV VOL-inb deposit **2026-00307549** PDF 6.04MB / 130p; AV **19.06.2026**; PDF created **18.07.2026**; neerlegging **15.07.2026**; commissaris EY Bedrijfsrevisoren BV B160 / Christoph Oris IBR A02341 17.424). Leftover IGS DV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; tick 1367 listed this CDN as leftover next). Distinct from already-mined Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 / Welzijnszorg Kempen WV. KBO Actief / normale toestand since **13.11.1968**; statutaire naam Interkommunale Ontwikkelingsmaatschappij voor de Kempen / I.O.K. since 01.01.1969; Dienstverlenende vereniging (Vlaams Gewest) since 11.05.1993; zetel Antwerpseweg 1 2440 Geel since 31.12.1985; **5 VE**; btw since 01.10.1977; RSZ since 01.01.2022; aanbestedende overheid since 13.11.1968; jaarvergadering mei; 15 KBO-bestuurders / voorzitter Ward Kennes; e-mail info@iok.be; tel 014 53 53 00; NACE 84.130/68.203/84.119/68.110. Hunt leftover AGB/zorg/EVA first: IOK statutory CDN live this tick (HTTP 200 / 6041287 / 130p) — taken (preferred unit). Leiedal already mined 1367 — skipped; Interleuven already mined 1366 — skipped; Nuhma-group seam 1353-1365 already mined — skipped; Dommelhof leftover Limburg EVA not re-probed once live IOK extracted. Otary RS Nuhma-adjacent fallback not taken. IMOG/Haviland still 2024 as of 1367; POM Limburg glossy-only; Veneco glossy; IVAREM/IGEMO activiteitenverslag only; IVOO no public 2025 JR. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350. Not every-10 (next 1370).
- EUR strong (primary official WVV VOL-inb; 6.4.1/6.5.1/6.8/6.20 not filed; commissarisverslag image-only p118-121): assets **163.272.484** (was 160.249.951); fixed **39.467.439** / MVA **39.174.192** (gebouwen **21.487.838** DROP vs 23.097.128 + machines 419.017 + meubilair 14.846 + overige **17.252.491** JUMP vs 15.195.693); immaterieel 226.922; FVA **66.325** (deelneming 31.000 + andere 35.325; 6.4.1 not filed); current **123.805.044**; inventory **62.335.305** waarvan onroerend bestemd voor verkoop **62.175.899** (38,1% of assets; was 61.957.732) + WIP 152.873; ST recv **6.187.816**; beleggingen **52.871.636** waarvan aandelen **52.867.325** (issuer list empty) + termijn 4.311; cash **2.006.742 JUMP** vs 1.066.533 THIN vs 52,87m aandelen; equity **137.104.637** (inbreng 15.642.075 onbeschikbaar / 625.723 aandelen; reserves 119.425.973; kapitaalsubsidies **2.015.592**); voorzieningen **12.484.741** (pensioen responsabilisering **10.333.741** geen verdiscontering + overige **2.151.000 JUMP** vs 200.000); schulden **13.683.106** (LT empty; ST **10.745.565** waarvan bank **31** + leveranciers 3.509.905 + overige 4.774.297 + accruals 2.937.541); omzet **4.999.438** (6.10 category: industrie/ambacht 1.162.672 / woonzones 629.925 / studiebureau 3.206.841; geo BE 4.999.438 / NL 0; comparative 4.626.164); andere opbr **18.029.791** (subsidies 2.576.328 only; ~15.453.463 unnamed); goods 3.060.301; diensten 4.508.164; pers **11.111.594** / **109,4 VTE** / 149 koppen; afschr 1.653.493; expl **243.083** vs −58.782; fin opbr 1.152.569 (meerwaarde vlottende 858.528 + capsub 282.002); fin kosten −70.787; PnL **1.466.438** vs 1.157.878 toegevoegd aan overige reserves; bestuurders 49.107. 6.18 vrijgesteld (1:26 criteria). 6.15 related-party nihil.
- CSVs: sources+4/entities+1/budgets+53/commitments+1/leaderboard+1 + FOI ready `gap_iokd_othops_18_03m_inv_62_18m_invest_52_87m_l5` (not sent); rq_1368=done; spawn rq_1369; ticks=1368.
- Coverage: residual dual L5 (IOK leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1370).
- Next: rq_1369 residual dual L5 VL JR2025 hole_fill (prefer leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS / Rematics / Sunfin only if a new live 2025 WVV PDF downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; IMOG/Haviland only if a 2025 JR PDF now downloads; Veneco/IVOO/MIWA/IVAREM/IGEMO only if a WVV/BBC PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1368 write done")


if __name__ == "__main__":
    main()

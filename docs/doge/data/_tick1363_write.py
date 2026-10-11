# -*- coding: utf-8 -*-
"""Tick 1363 — leftover MyCSN NV JR2025 official NBB WVV euros.
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

TICK = "1363"
UTC = "2026-08-19T01:45:00Z"
ENT = "nv_mycs"
HIER = "Vlaanderen>Limburg>NV>MyCSN>SmartCity"
GAP = "gap_mycs_omzet_1_85m_pnl_neg_0_46m_sub_l5"
SRC = "src_mycs_jr2025_nbb"
SRC2 = "src_mycs_site"
SRC3 = "src_kbo_mycs_0724946623"
SRC4 = "src_mycs_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00126775.pdf"
SRC2_URL = "https://www.mycsn.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0724946623"
SRC4_URL = "https://www.mycsn.be/contact/"
FOI_EMAIL = "info@mycsn.be"
FOI_POSTAL = "Herkenrodesingel 14 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_mycs_omzet_1_85m_pnl_neg_0_46m_sub_l5.md"
COMM = "comm_mycs_jr2025_pnl"
LB = "lb_mycs_omzet_1_85m_pnl_neg_0_46m_sub"


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
                "title": "MyCSN NV jaarrekening boekjaar 2025 (official NBB WVV VOL-kap deposit 2026-00126775; AV 26.05.2026)",
                "url": SRC_URL,
                "publisher": "MyCSN NV / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1363; official NBB VOL-kap PDF 1.52MB 47p deposit 2026-00126775 neerlegging 28.05.2026 created 30.05.2026; "
                    "leftover smart-city NV of NUHMA DC 1358 / Nuhma cv 1356 / s-Lim 1362 / Nuhmeris 1361 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Moore Audit / Jimmy Depré 8125; "
                    "parent DC 6.5.1 EV 1855808 / PnL -455887 MATCHES"
                ),
            },
            {
                "source_id": SRC2,
                "title": "MyCSN official site (smart-city NV; statutory JR unpublished on site)",
                "url": SRC2_URL,
                "publisher": "MyCSN NV",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1363; leftover NV of mined Limburg + Nuhma cv/DC/AC/Nubema/ECO2050/Nuhmeris/s-Lim/Bionerga/Limburg.net; "
                    "mycsn.be has no JR PDF (only 2021 magazine); daughter of Cipal + Nuhma; "
                    "cloud smart-city platform / PaaS / GEO-spatial"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO MyCSN 0724.946.623",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1363; KBO 0724.946.623 Actief / normale toestand since 15.04.2019; "
                    "statutaire naam MyCSN since 15.04.2019; NV since 15.04.2019; "
                    "zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; 1 VE; "
                    "btw since 01.06.2019; RSZ since 06.01.2020; "
                    "jaarvergadering mei; boekjaar 31 december; KBO kapitaal 2325000; 6 functiehouders; "
                    "bestuurders Cipal 0442802030 / Nuhma cv 0472325068 / Nubema 0834086964; no KBO email/web/tel"
                ),
            },
            {
                "source_id": SRC4,
                "title": "MyCSN FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "MyCSN NV",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1363; FOI info@mycsn.be; tel +32 14 39 70 70; "
                    "Herkenrodesingel 14 3500 Hasselt (same zetel as Nuhma cv / Nubema / NUHMA DC / NUHMA AC / ECO2050 / Nuhmeris / s-Lim / Bionerga / Limburg.net); "
                    "PEPPOL MyCSN NV 0208:0724946623"
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
                "name_nl": "MyCSN (leftover smart-city NV Limburg / Nuhma DC 90pct + Cipal 10pct)",
                "name_fr": "MyCSN (SA smart city residuelle Limbourg / participation Nuhma DC 90pct + Cipal 10pct)",
                "name_en": "MyCSN leftover Limburg smart-city NV (Nuhma DC 90pct + Cipal 10pct)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.mycsn.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1363 leftover residual smart-city NV of NUHMA DC 1358 "
                    "+ Nuhma cv 1356 + s-Lim 1362 + Nuhmeris 1361 + Nubema 1359 + ECO2050 1360 + NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353 "
                    "(same zetel Herkenrodesingel 14); "
                    "KBO 0724.946.623 Actief since 15.04.2019; official NBB WVV VOL-kap PDF downloads; "
                    "sourced euros assets 4360871 omzet 1847195 pnl -455887; "
                    "FOI ready 6.10/subsidies 283k+291k/parent-loan 2.02m/Rematics/taxlat 5.38m"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_mycs_assets_2025", ENT, "2025", "4360871", "2025 assets 4360871 VOL-kap 20/58; tick1363; primary official NBB WVV"),
        ("bud_mycs_assets_2024", ENT, "2024", "3612356", "2024 assets 3612356 comparative; tick1363; primary official NBB WVV 20/58"),
        ("bud_mycs_startup_2025", ENT, "2025", "725", "2025 oprichtingskosten 725; tick1363; primary official NBB WVV 20"),
        ("bud_mycs_fixed_2025", ENT, "2025", "2778153", "2025 vaste activa 2778153 JUMP vs 2298250; tick1363; primary official NBB WVV 21/28"),
        ("bud_mycs_iva_2025", ENT, "2025", "2256412", "2025 IVA 2256412 JUMP vs 2118290 (GEO-spatial platform); tick1363; primary official NBB WVV 21"),
        ("bud_mycs_ivaacq_2025", ENT, "2025", "700889", "2025 IVA aanschaf 700889 (JV 700888.84 GEO-spatial); tick1363; primary official NBB WVV 8021"),
        ("bud_mycs_mva_2025", ENT, "2025", "7501", "2025 MVA 7501 (meubilair 24); tick1363; primary official NBB WVV 22/27"),
        ("bud_mycs_fva_2025", ENT, "2025", "514240", "2025 FVA 514240 JUMP vs 178356 (Rematics 47.85pct); tick1363; primary official NBB WVV 28"),
        ("bud_mycs_partic_2025", ENT, "2025", "343319", "2025 deelnemingen 343319 Rematics 6703 sh / 47.85pct; tick1363; primary official NBB WVV 282"),
        ("bud_mycs_fvarecv_2025", ENT, "2025", "170921", "2025 FVA vorderingen deelneming 170921; tick1363; primary official NBB WVV 283"),
        ("bud_mycs_current_2025", ENT, "2025", "1581993", "2025 vlottende activa 1581993 JUMP vs 1312649; tick1363; primary official NBB WVV 29/58"),
        ("bud_mycs_strecv_2025", ENT, "2025", "265891", "2025 ST vorderingen 265891 (trade 168958 + other 96933); tick1363; primary official NBB WVV 40/41"),
        ("bud_mycs_cash_2025", ENT, "2025", "461475", "2025 liquide middelen 461475 DROP vs 507108; tick1363; primary official NBB WVV 54/58"),
        ("bud_mycs_cash_2024", ENT, "2024", "507108", "2024 liquide middelen 507108 comparative; tick1363; primary official NBB WVV 54/58"),
        ("bud_mycs_prepaid_2025", ENT, "2025", "854627", "2025 overlopend actief 854627 (kosten 5269 + opbrengsten 849357); tick1363; primary official NBB WVV 490/1"),
        ("bud_mycs_accruedinc_2025", ENT, "2025", "849357", "2025 verkregen opbrengsten 849357 unnamed; tick1363; primary official NBB WVV 6.6"),
        ("bud_mycs_equity_2025", ENT, "2025", "1855808", "2025 eigen vermogen 1855808 DROP vs 2021008; matches parent DC 6.5.1; tick1363; primary official NBB WVV 10/15"),
        ("bud_mycs_equity_2024", ENT, "2024", "2021008", "2024 eigen vermogen 2021008 comparative; tick1363; primary official NBB WVV 10/15"),
        ("bud_mycs_capital_2025", ENT, "2025", "2325000", "2025 geplaatst kapitaal 2325000 / 2000 aandelen; tick1363; primary official NBB WVV 100"),
        ("bud_mycs_re_2025", ENT, "2025", "-759879", "2025 overgedragen verlies -759879; tick1363; primary official NBB WVV 14"),
        ("bud_mycs_capsid_2025", ENT, "2025", "290687", "2025 kapitaalsubsidies 290687 new unnamed public; tick1363; primary official NBB WVV 15"),
        ("bud_mycs_defertax_2025", ENT, "2025", "96896", "2025 uitgestelde belastingen 96896 on kapitaalsubsidie; tick1363; primary official NBB WVV 168"),
        ("bud_mycs_debt_2025", ENT, "2025", "2408167", "2025 schulden 2408167 JUMP vs 1591348; tick1363; primary official NBB WVV 17/49"),
        ("bud_mycs_lt_2025", ENT, "2025", "2023674", "2025 LT achtergesteld 2023674 JUMP vs 1251273 (all 1-5y; related); tick1363; primary official NBB WVV 170"),
        ("bud_mycs_st_2025", ENT, "2025", "344648", "2025 ST schulden 344648; tick1363; primary official NBB WVV 42/48"),
        ("bud_mycs_trade_2025", ENT, "2025", "307078", "2025 leveranciers 307078; tick1363; primary official NBB WVV 440/4"),
        ("bud_mycs_soc_2025", ENT, "2025", "37429", "2025 bezoldigingen/sociale lasten 37429; tick1363; primary official NBB WVV 454/9"),
        ("bud_mycs_accrued_2025", ENT, "2025", "39846", "2025 overlopend passief 39846 (opbr 25579 + kosten 14267); tick1363; primary official NBB WVV 492/3"),
        ("bud_mycs_ops_2025", ENT, "2025", "2349075", "2025 bedrijfsopbrengsten 2349075; tick1363; primary official NBB WVV 70/76A"),
        ("bud_mycs_omzet_2025", ENT, "2025", "1847195", "2025 omzet 1847195 JUMP vs 1380974; 6.10 category/geo empty; tick1363; primary official NBB WVV 70"),
        ("bud_mycs_omzet_2024", ENT, "2024", "1380974", "2024 omzet 1380974 comparative; tick1363; primary official NBB WVV 70"),
        ("bud_mycs_ownprod_2025", ENT, "2025", "183133", "2025 geproduceerde vaste activa 183133; tick1363; primary official NBB WVV 72"),
        ("bud_mycs_andere_2025", ENT, "2025", "318747", "2025 andere bedrijfsopbrengsten 318747; tick1363; primary official NBB WVV 74"),
        ("bud_mycs_opssub_2025", ENT, "2025", "283405", "2025 exploitatiesubsidies 283405 DROP vs 592836 unnamed public; tick1363; primary official NBB WVV 740"),
        ("bud_mycs_opscost_2025", ENT, "2025", "2817609", "2025 bedrijfskosten 2817609; tick1363; primary official NBB WVV 60/66A"),
        ("bud_mycs_goods_2025", ENT, "2025", "336774", "2025 handelsgoederen 336774; tick1363; primary official NBB WVV 60"),
        ("bud_mycs_diensten_2025", ENT, "2025", "1518164", "2025 diensten 1518164; tick1363; primary official NBB WVV 61"),
        ("bud_mycs_pers_2025", ENT, "2025", "331868", "2025 pers 331868 / avg VTE 4.2 / YE 5 koppen 4.7 VTE; tick1363; primary official NBB WVV 62/6.10"),
        ("bud_mycs_afschr_2025", ENT, "2025", "565683", "2025 afschrijvingen 565683; tick1363; primary official NBB WVV 630"),
        ("bud_mycs_expl_2025", ENT, "2025", "-468533", "2025 bedrijfsverlies -468533 (was -487475); tick1363; primary official NBB WVV 9901"),
        ("bud_mycs_fininc_2025", ENT, "2025", "79819", "2025 financiele opbrengsten 79819 (capsid 44276 + nonrec 19684); tick1363; primary official NBB WVV 75/76B"),
        ("bud_mycs_capsid_pl_2025", ENT, "2025", "44276", "2025 kapitaalsubsidies in resultaat 44276; tick1363; primary official NBB WVV 9125"),
        ("bud_mycs_fincost_2025", ENT, "2025", "81164", "2025 financiele kosten 81164 (schulden 80774); tick1363; primary official NBB WVV 65/66B"),
        ("bud_mycs_pnl_2025", ENT, "2025", "-455887", "2025 PnL 9904 -455887 (was -535912); tick1363; primary official NBB WVV; matches parent DC 6.5.1"),
        ("bud_mycs_pnl_2024", ENT, "2024", "-535912", "2024 PnL -535912 comparative; tick1363; primary official NBB WVV 9904"),
        ("bud_mycs_comm_2025", ENT, "2025", "8125", "2025 commissaris Moore Audit 8125; tick1363; primary official NBB WVV 9505"),
        ("bud_mycs_relrecv_2025", ENT, "2025", "90523", "2025 verbonden ST vorderingen 90523; tick1363; primary official NBB WVV 9291"),
        ("bud_mycs_reldebt_2025", ENT, "2025", "2050622", "2025 verbonden schulden 2050622 (LT 2023674 + ST 26948); tick1363; primary official NBB WVV 9351"),
        ("bud_mycs_reldcost_2025", ENT, "2025", "80401", "2025 verbonden kosten schulden 80401; tick1363; primary official NBB WVV 9461"),
        ("bud_mycs_taxlat_2025", ENT, "2025", "5383264", "2025 actieve latenties fiscale verliezen 5383264; tick1363; primary official NBB WVV 9142; not TE-additive"),
        ("bud_mycs_rematics_ev_2025", ENT, "2025", "490947", "2025 Rematics BV 47.85pct EV 490947 / PnL -195783 (6.5.1); tick1363; primary official NBB WVV"),
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
                "title": "MyCSN NV JR2025 leftover NV dual (assets 4.36m / omzet 1.85m / PnL -0.46m / 4.2 VTE)",
                "entity_id": ENT,
                "beneficiary": "MyCSN / NUHMA DC / Nuhma cv / Cipal / Rematics / Limburg municipalities",
                "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-05-26",
                "start_year": "2019",
                "end_year": "2026",
                "total_envelope_eur": "4360871",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover NV map VL smart-city — 6.10 empty / unnamed subsidies 283k+291k / parent loan 2.02m",
                "cut_option": "Publish 6.10 municipal counterparties + name subsidy grantors 283405/290687 + put 2.02m achtergesteld parent loan terms on the record + why 5.38m tax losses sit on 4.36m assets after 7 development years; do not keep 4.4m municipal smart-city NV as unpublished dual vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1363; assets 4360871 omzet 1847195 pnl -455887; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "MyCSN NV JR2025 leftover NV: assets 4.36m / omzet 1.85m / PnL -0.46m / subsidies+loan",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "455887",
                "total_cost_eur": "4360871",
                "tco_notes": (
                    "Leftover dual smart-city NV of NUHMA DC of mined Limburg cities + Cipal: "
                    "assets 4.36m / equity 1.86m / pnl -0.46m / omzet 1.85m / pers 0.33m / 4.2 VTE / "
                    "Nuhma DC 90pct votes / Cipal 10pct / parent DC 6.5.1 MATCHES / "
                    "achtergesteld 2.02m related / unnamed subsidies 283k+291k / tax losses 5.38m / official NBB WVV live; "
                    "do not treat 4.36m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "MyCSN / NUHMA DC / Nuhma cv / Cipal / Rematics / Limburg municipalities",
                "stated_goal": "Local leftover NV map VL smart-city — JR2025 live; dual 6.10/subsidy/loan FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 4.36m / omzet 1.85m / pnl -0.46m; 4.2 VTE; parent DC 6.5.1 matches",
                "absurdity_score": "6.6",
                "cost_score": "5.2",
                "difficulty": "2.5",
                "priority_index": "6.0",
                "cut_proposal": "Publish 6.10 municipal counterparties + name subsidy grantors 283405/290687 + put 2.02m achtergesteld parent loan terms on the record + why 5.38m tax losses sit on 4.36m assets after 7 development years; do not keep 4.4m municipal smart-city NV as unpublished dual vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1363; leftover NV of mined Limburg + NUHMA DC 1358 / Nuhma cv 1356 / s-Lim 1362 / Nuhmeris 1361 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "6.10 omzet 1847195 category/geo split empty + per-gemeente/s-Lim/Nuhma/Cipal/Fluvius/Rematics counterparties "
                    "+ exploitatiesubsidies 283405 DROP vs 592836 unnamed grantor "
                    "+ kapitaalsubsidie 290687 new + in-resultaat 44276 (WVV 9125) unnamed grantor "
                    "+ Nuhma DC 90pct book/votes (tick1358 6.5.1 MATCHES EV 1855808 / PnL -455887) / Cipal 10pct "
                    "+ intra-group transfer from Nuhmeris (tick1361 FVA sale) "
                    "+ achtergesteld related loan 2023674 (was 1251273; 1-5y) + related ST recv 90523 / ST debt 26948 / debt cost 80401 "
                    "+ 6.15 related-party refusal "
                    "+ prepaid verkregen opbrengsten 849357 unnamed "
                    "+ Rematics 47.85pct extra 335884 / aanschaf 339415 / 6.5.1 EV 490947 PnL -195783 "
                    "+ tax losses 5383264 on assets 4360871 "
                    "+ continuity art.3:6 6deg still ontwikkeling after 7y / IVA 2256412 not deducted "
                    "+ image-only commissaris Moore 8125 + official-site JR"
                ),
                "why_it_matters": (
                    "Leftover smart-city NV of NUHMA DC of mined Limburg cities + Nuhma cv 1356 "
                    "+ s-Lim 1362 + Nuhmeris 1361 + Nubema 1359 + ECO2050 1360 + NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353 "
                    "(same zetel Herkenrodesingel 14) + Cipal 10pct: "
                    "4.36m assets / 1.85m omzet / -0.46m pnl / 4.2 VTE / 90pct Nuhma DC / "
                    "2.02m achtergesteld parent loan / unnamed subsidies 283k+291k / tax losses 5.38m / 7y still development "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "MyCSN NV / NUHMA DC BV / Nuhma cv / Cipal NV / Limburg municipalities",
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
                    "tick1363 leftover NV of mined Limburg cities + NUHMA DC 1358 / Nuhma cv 1356 / s-Lim 1362 / Nuhmeris 1361 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 after honest hunt; "
                    "live JR2025 official NBB WVV VOL-kap PDF now extracted (1.52MB 47p deposit 2026-00126775). "
                    "AGB MAC already mined 1270 — skipped. Westtoer already mined — skipped. "
                    "s-Lim already mined 1362 — skipped. Nuhmeris already mined 1361 — skipped. ECO2050 already mined 1360 — skipped. Nubema already mined 1359 — skipped. NUHMA DC already mined 1358 — skipped. EcoWerf already mined 1357 — skipped. "
                    "Herkenrode RE 0724557633 CDN 2026-00124490 listed — leftover next. "
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
        "task_id": "rq_1363",
        "title": "MyCSN NV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: MyCSN leftover smart-city NV of NUHMA DC of mined Limburg cities "
            "+ Nuhma cv/s-Lim/Nuhmeris/Nubema/ECO2050/AC/Bionerga/Limburg.net after honest hunt; KBO 0724.946.623 Actief; "
            "live JR2025 official NBB WVV VOL-kap PDF (1.52MB 47p deposit 2026-00126775; commissaris Moore); "
            "sourced euros assets 4360871 / omzet 1847195 / pnl -455887; "
            "FOI ready 6.10/subsidies 283k+291k/parent-loan 2.02m/Rematics/taxlat 5.38m"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T01:20:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1363 MyCSN leftover NV residual; KBO 0724.946.623; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1364 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1364",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1363 done including MyCSN NV 1363 leftover smart-city live NBB WVV / "
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
            "Herkenrode RE 0724.557.633 leftover Nuhma-family CDN 2026-00124490 — take only if a statutory 2025 WVV PDF now downloads; "
            "s-Lim DV 0805.138.503 leftover IGS (67.13pct+16.44pct of s-Lim CV votes) — take only if a statutory 2025 WVV/BBC PDF now downloads; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland still 2024 — take only if a 2025 JR PDF now downloads; "
            "Veneco / Leiedal / IVOO / MIROM / INCOVO / IVAGO / MIWA / IVAREM / IGEMO — take only if a statutory 2025 WVV/BBC PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined MyCSN 1363 / s-Lim 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1363 after MyCSN leftover NV live NBB WVV; next residual dual L5 VL; next every-10 is 1370",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1363", rq_new, rq_spawn)
    print("research_queue 1363", found, "spawned_1364", spawned)

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
                "last_unit_id": "rq_1363",
                "ticks_completed": "1363",
                "paused": "no",
                "notes": (
                    "tick1363 MyCSN leftover NV residual; KBO 0724.946.623; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 4360871 omzet 1847195 pnl -455887; "
                    "FOI ready 6.10/subsidies/parent-loan; next rq_1364 residual dual L5 VL; continuous hole_fill; next every-10 is 1370"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1363 - 2026-08-19 - rq_1363 MyCSN NV dual residual leftover
- Unit: MyCSN NV (leftover smart-city naamloze vennootschap / sold this year from Nuhmeris NV to NUHMA DC BV) of already-mined Limburg cities via Nuhma cv tick1356 (Hasselt / Genk / Tongeren-Borgloon / Houthalen-Helchteren / Bilzen-Hoeselt / Leopoldsburg / Nieuwerkerken / Gingelom / Pelt / Maasmechelen) + leftover BV NUHMA DC tick1358 + leftover CV s-Lim tick1362 + leftover NV Nuhmeris tick1361 + leftover NV Nubema tick1359 + leftover cv ECO2050 tick1360 + leftover NV NUHMA AC tick1355 + leftover NV Bionerga tick1354 + leftover IGS Limburg.net tick1353 after residual dual hunt (KBO **0724.946.623**; official mycsn.be has no JR PDF; live NBB WVV VOL-kap deposit **2026-00126775** PDF 1.52MB / 47p; AV **26.05.2026**; neerlegging **28.05.2026**; PDF created **30.05.2026**; commissaris Moore Audit / Jimmy Depré 8.125; jaarverslag RvB 02.03.2026 text-extractable; commissarisverslag image-embedded). Leftover NV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last tick listed leftover MyCSN / Herkenrode / s-Lim DV / Dommelhof only if a statutory 2025 WVV now downloads). Distinct from already-mined s-Lim 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **15.04.2019**; statutaire naam MyCSN since 15.04.2019; Naamloze vennootschap since 15.04.2019; zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; **1 VE**; btw since 01.06.2019; RSZ since 06.01.2020; jaarvergadering mei; KBO kapitaal 2.325.000; 6 functiehouders; bestuurders Cipal NV / Nuhma cv / Nubema NV; e-mail info@mycsn.be; NACE 62.900 / 63.100 / 62.200 / 63.910 / 62.100. Hunt leftover AGB/zorg/EVA first: AGB MAC Mechelen 2025 BBC already mined tick1270 — skipped; SportAG Aalst / AGB Deinze / AGB Genk already mined — skipped; Westtoer APB already mined — skipped; s-Lim already mined 1362 — skipped; Nuhmeris already mined 1361 — skipped; ECO2050 already mined 1360 — skipped; Nubema already mined 1359 — skipped; NUHMA DC already mined 1358 — skipped; EcoWerf already mined 1357 — skipped; MyCSN statutory CDN live this tick (HTTP 200 / 1515022 / 47p) — taken. Herkenrode RE 0724.557.633 CDN 2026-00124490 listed — leftover next. s-Lim DV 0805.138.503 leftover IGS later. IOK/IMOG/Haviland still 2024; Interleuven 2025 jaarverslag InDesign embed only / balans still 2024; POM Limburg glossy-only — not taken; Veneco/Leiedal glossy-only; IVAREM activiteitenverslag glossy; IGEMO activiteitenverslag only; IVOO no public 2025 JR; IVAGO SSL EOF; MIWA flipbook; MIROM Cloudflare; De Schorre provincieantwerpen.be 403; APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas not taken (MyCSN WVV live); Dommelhof leftover Limburg EVA KBO 0777.495.085 still no 2026 PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE no fetchable 2025 JR this tick. NBB consult skipped (403/SPA); euros extracted from the official VOL-kap deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined s-Lim 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345. Not every-10 (next 1370).
- EUR strong (primary official WVV VOL-kap; parent DC 6.5.1 EV 1.855.808 / PnL −455.887 **matches**): assets **4.360.871** (was 3.612.356); fixed **2.778.153** JUMP vs 2.298.250; IVA **2.256.412** JUMP vs 2.118.290 after aanschaf **700.889** GEO-spatial PaaS; MVA **7.501**; FVA **514.240** JUMP vs 178.356 (Rematics 47,85% 6.703 sh EV 490.947 / PnL −195.783; extra middelen 335.884); current **1.581.993**; ST recv **265.891**; cash **461.475 DROP** vs 507.108; prepaid **854.627** (verkregen opbrengsten **849.357** unnamed); equity **1.855.808** DROP vs 2.021.008 (kapitaal 2.325.000 / 2.000 aandelen; overgedragen verlies −759.879; kapitaalsubsidies **290.687** new; reserves 231.920 onttrokken); schulden **2.408.167** (LT achtergesteld **2.023.674 JUMP** vs 1.251.273 all 1–5y related; ST **344.648** waarvan leveranciers **307.078**); omzet **1.847.195 JUMP** vs 1.380.974 / exploitatiesubsidies **283.405 DROP** vs 592.836 / pers **331.868** / avg VTE **4,2** / YE **5** koppen (4,7 VTE; 4 voltijds + 1 deeltijds bedienden); diensten **1.518.164**; goods **336.774**; afschr **565.683**; expl **−468.533**; fin opbr **79.819** (capsid in resultaat 44.276 + nonrec FVA 19.684); fin kosten **81.164**; PnL **−455.887** (was −535.912); dividend **0**. Stemrechten: Nuhma DC **90%** (1.800) / Cipal NV **10%** (200). Related ST recv **90.523** / schulden **2.050.622**. Tax losses **5.383.264**. Continuity art. 3:6, 6° (still ontwikkeling after 7y; existing financing + 12-month cash-flow; alarmbel waived by not deducting IVA 2.256.412). Commissaris Moore **8.125**. 6.10 category/geo empty. 6.15 related-party refusal.
- CSVs: sources+4/entities+1/budgets+51/commitments+1/leaderboard+1 + FOI ready `gap_mycs_omzet_1_85m_pnl_neg_0_46m_sub_l5` (not sent); rq_1363=done; spawn rq_1364; ticks=1363.
- Coverage: residual dual L5 (MyCSN leftover NV live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1370).
- Next: rq_1364 residual dual L5 VL JR2025 hole_fill (prefer leftover Herkenrode RE 0724.557.633 CDN 2026-00124490 if still live; leftover s-Lim DV 0805.138.503 only if a statutory 2025 WVV/BBC PDF now downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined MyCSN 1363 / s-Lim 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1363 write done")


if __name__ == "__main__":
    main()

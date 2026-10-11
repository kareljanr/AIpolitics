# -*- coding: utf-8 -*-
"""Tick 1361 — leftover Nuhmeris NV JR2025 official NBB WVV euros.
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

TICK = "1361"
UTC = "2026-08-19T00:50:00Z"
ENT = "nv_nuhm"
HIER = "Vlaanderen>Limburg>NV>Nuhmeris>KlimaatHolding"
GAP = "gap_nuhm_fva_sale_6_05m_cash_7_96m_re_11_26m_l5"
SRC = "src_nuhm_jr2025_nbb"
SRC2 = "src_nuhm_site"
SRC3 = "src_kbo_nuhm_0560976140"
SRC4 = "src_nuhm_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00124698.pdf"
SRC2_URL = "https://nuhma.be/jaarverslag/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0560976140"
SRC4_URL = "https://nuhma.be/contact/"
FOI_EMAIL = "info@nuhma.be"
FOI_POSTAL = "Herkenrodesingel 14 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_nuhm_fva_sale_6_05m_cash_7_96m_re_11_26m_l5.md"
COMM = "comm_nuhm_jr2025_pnl"
LB = "lb_nuhm_fva_sale_6_05m_cash_7_96m_re_11_26m"


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
                "title": "Nuhmeris NV jaarrekening boekjaar 2025 (official NBB WVV VOL-kap deposit 2026-00124698; AV 26.05.2026)",
                "url": SRC_URL,
                "publisher": "Nuhmeris NV / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1361; official NBB VOL-kap PDF 460kB 45p deposit 2026-00124698 neerlegging header 27.05.2026 created 29.05.2026; "
                    "leftover klimaat-holding NV 100pct of NUHMA DC 1358 / Nuhma cv 1356 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Moore Audit / Jimmy Depré oordeel zonder voorbehoud; "
                    "parent DC 6.5.1 EV 13531710 / PnL -510182 MATCHES"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Nuhma official site jaarverslag page (parent cv; Nuhmeris statutory not published separately)",
                "url": SRC2_URL,
                "publisher": "Nuhma cv / Nuhmeris NV",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1361; leftover NV of mined Limburg + Nuhma cv/DC/AC/Nubema/ECO2050/Bionerga/Limburg.net; "
                    "nuhma.be is Nuhma cv KBO 0472.325.068; jaarverslag page still 2020 PDF only; "
                    "Nuhmeris statutory unpublished on official site"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO NUHMERIS 0560.976.140",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1361; KBO 0560.976.140 Actief / normale toestand since 04.09.2014; "
                    "statutaire naam NUHMERIS since 04.09.2014; NV since 04.09.2014; "
                    "zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; 1 VE; "
                    "btw since 01.11.2014; aanbestedende overheid since 04.09.2014; "
                    "jaarvergadering mei; boekjaar 31 december; KBO-kapitaal still 24500000 "
                    "(statutory reduced to 21259185); bestuurders Nuhma cv 0472.325.068 + Nubema NV 0834.086.964; "
                    "no KBO email/web/tel"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Nuhmeris FOI channel / official contact (parent Nuhma email/tel)",
                "url": SRC4_URL,
                "publisher": "Nuhma cv / Nuhmeris NV",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1361; FOI info@nuhma.be 011 49 56 10; "
                    "Herkenrodesingel 14 3500 Hasselt (same zetel as Nuhma cv / Nubema / NUHMA DC / NUHMA AC / ECO2050 / Bionerga / Limburg.net)"
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
                "name_nl": "Nuhmeris (leftover klimaat-holding NV / smart-city / 100pct dochter NUHMA DC)",
                "name_fr": "Nuhmeris (holding climat residuelle / smart city / filiale 100pct NUHMA DC)",
                "name_en": "Nuhmeris leftover climate-holding NV (smart-city 100pct daughter of NUHMA DC)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://nuhma.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1361 leftover residual klimaat-holding NV 100pct of NUHMA DC 1358 "
                    "+ Nuhma cv 1356 + Nubema 1359 + ECO2050 1360 + NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353 "
                    "(same zetel Herkenrodesingel 14); "
                    "KBO 0560.976.140 Actief since 04.09.2014; official NBB WVV VOL-kap PDF downloads; "
                    "sourced euros assets 19350925 cash 7959717 fva_sale 6049188 pnl -510182; "
                    "FOI ready MyCSN/s-Lim sale / RE 11.26m / ING 15m lastgeving / cash 7.96m / ECO2050 book"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_nuhm_assets_2025", ENT, "2025", "19350925", "2025 assets 19350925 VOL-kap 20/58; tick1361; primary official NBB WVV; RvB 19350924.85"),
        ("bud_nuhm_assets_2024", ENT, "2024", "23548570", "2024 assets 23548570 comparative; tick1361; primary official NBB WVV 20/58"),
        ("bud_nuhm_fixed_2025", ENT, "2025", "6000250", "2025 vaste activa 6000250 DROP vs 9832825; tick1361; primary official NBB WVV 21/28"),
        ("bud_nuhm_mva_2025", ENT, "2025", "6000000", "2025 MVA 6000000 (terreinen/gebouwen 6000000; machines 0 after disposal); tick1361; primary official NBB WVV 22/27"),
        ("bud_nuhm_land_2025", ENT, "2025", "6000000", "2025 terreinen en gebouwen 6000000 no depreciation; tick1361; primary official NBB WVV 22"),
        ("bud_nuhm_fva_2025", ENT, "2025", "250", "2025 FVA 250 DROP vs 3796061 (sold MyCSN + s-Lim to Nuhma DC); tick1361; primary official NBB WVV 28"),
        ("bud_nuhm_fva_2024", ENT, "2024", "3796061", "2024 FVA 3796061 comparative (verbonden 1818907 + deelneming 1977154); tick1361; primary official NBB WVV 28"),
        ("bud_nuhm_fva_deel_2025", ENT, "2025", "250", "2025 deelnemingsverhouding 250 leftover ECO2050 1 Cat B 0.01pct; tick1361; primary official NBB WVV 282"),
        ("bud_nuhm_current_2025", ENT, "2025", "13350675", "2025 vlottende activa 13350675 DROP vs 13715745; tick1361; primary official NBB WVV 29/58"),
        ("bud_nuhm_stock_2025", ENT, "2025", "5260860", "2025 onroerende goederen bestemd voor verkoop 5260860 unchanged vs 2024; tick1361; primary official NBB WVV 35"),
        ("bud_nuhm_strecv_2025", ENT, "2025", "91151", "2025 ST vorderingen 91151 (trade 44390 + other 46761); tick1361; primary official NBB WVV 40/41"),
        ("bud_nuhm_cash_2025", ENT, "2025", "7959717", "2025 liquide middelen 7959717 JUMP vs 412592 (2024 termijn 7750000 converted); tick1361; primary official NBB WVV 54/58"),
        ("bud_nuhm_cash_2024", ENT, "2024", "412592", "2024 liquide middelen 412592 comparative; tick1361; primary official NBB WVV 54/58"),
        ("bud_nuhm_term_2024", ENT, "2024", "7750000", "2024 termijnrekeningen 7750000 (7m <1m + 750k 1m-1y) gone 2025; tick1361; primary official NBB WVV 53"),
        ("bud_nuhm_prepaid_2025", ENT, "2025", "38947", "2025 overlopend actief 38947 (kosten 1489 + opbrengsten 37458); tick1361; primary official NBB WVV 490/1"),
        ("bud_nuhm_equity_2025", ENT, "2025", "13531710", "2025 eigen vermogen 13531710 DROP vs 17282707; matches parent DC 6.5.1; tick1361; primary official NBB WVV 10/15"),
        ("bud_nuhm_equity_2024", ENT, "2024", "17282707", "2024 eigen vermogen 17282707 comparative; tick1361; primary official NBB WVV 10/15"),
        ("bud_nuhm_kapitaal_2025", ENT, "2025", "21259185", "2025 geplaatst kapitaal 21259185 / 1000 aandelen 100pct Nuhma DC; tick1361; primary official NBB WVV 100"),
        ("bud_nuhm_capred_2025", ENT, "2025", "3240815", "2025 kapitaalvermindering 3240815 per 01.01.2025 (BAV dec 2024); tick1361; primary official NBB WVV 6.7.1"),
        ("bud_nuhm_accumloss_2025", ENT, "2025", "-7727475", "2025 overgedragen verlies -7727475 (was -7217293); tick1361; primary official NBB WVV 14"),
        ("bud_nuhm_debt_2025", ENT, "2025", "5819215", "2025 schulden 5819215 DROP vs 6265863; tick1361; primary official NBB WVV 17/49"),
        ("bud_nuhm_lt_2025", ENT, "2025", "5200000", "2025 LT kredietinstellingen 5200000 DROP vs 5600000; tick1361; primary official NBB WVV 173"),
        ("bud_nuhm_bank_2025", ENT, "2025", "5600000", "2025 ING hypothecair total 5600000 (LT 5200000 + within-year 400000; 04.07.2024-31.07.2039); tick1361; primary official NBB WVV 6.9/6.19"),
        ("bud_nuhm_st_2025", ENT, "2025", "438288", "2025 ST schulden 438288 (current portion 400000 + trade 36141 + tax 259 + other 1888); tick1361; primary official NBB WVV 42/48"),
        ("bud_nuhm_accrued_2025", ENT, "2025", "180926", "2025 overlopend passief 180926 (kosten 111372 + opbrengsten 69554); tick1361; primary official NBB WVV 492/3"),
        ("bud_nuhm_omzet_2025", ENT, "2025", "195582", "2025 omzet 195582 DROP vs 242238; tick1361; primary official NBB WVV 70"),
        ("bud_nuhm_omzet_2024", ENT, "2024", "242238", "2024 omzet 242238 comparative; tick1361; primary official NBB WVV 70"),
        ("bud_nuhm_opscost_2025", ENT, "2025", "109120", "2025 bedrijfskosten 109120 (goods 15558 + diensten 18606 + taksen 38191 + nr 36764); tick1361; primary official NBB WVV 60/66A"),
        ("bud_nuhm_diensten_2025", ENT, "2025", "18606", "2025 diensten 18606 DROP vs 37850; tick1361; primary official NBB WVV 61"),
        ("bud_nuhm_expl_2025", ENT, "2025", "86462", "2025 bedrijfswinst 86462 (was 88229); tick1361; primary official NBB WVV 9901"),
        ("bud_nuhm_fininc_2025", ENT, "2025", "5649659", "2025 financiele opbrengsten 5649659 (rec 155870 + nr FVA reversal 5493789); tick1361; primary official NBB WVV 75/76B"),
        ("bud_nuhm_fincost_2025", ENT, "2025", "6246304", "2025 financiele kosten 6246304 (rec 197115 waarvan schulden 196989 + nr FVA sale 6049188); tick1361; primary official NBB WVV 65/66B"),
        ("bud_nuhm_fva_sale_2025", ENT, "2025", "6049188", "2025 minderwaarden realisatie FVA 6049188 (MyCSN + s-Lim to Nuhma DC); tick1361; primary official NBB WVV 6631"),
        ("bud_nuhm_fva_rev_2025", ENT, "2025", "5493789", "2025 terugname WV FVA 5493789; tick1361; primary official NBB WVV 761"),
        ("bud_nuhm_pnl_2025", ENT, "2025", "-510182", "2025 PnL 9904 -510182 DROP vs -249210; tick1361; primary official NBB WVV + RvB -510181.70; matches parent DC 6.5.1"),
        ("bud_nuhm_pnl_2024", ENT, "2024", "-249210", "2024 PnL -249210 comparative; tick1361; primary official NBB WVV 9904"),
        ("bud_nuhm_pers_2025", ENT, "2025", "0", "2025 pers/VTE 0 (9086/9087/62 empty); tick1361; primary official NBB WVV 6.10"),
        ("bud_nuhm_comm_2025", ENT, "2025", "3601", "2025 commissaris Moore Audit 3601; tick1361; primary official NBB WVV 9505"),
        ("bud_nuhm_relrecv_2025", ENT, "2025", "7944", "2025 verbonden ST vorderingen 7944; tick1361; primary official NBB WVV 9291"),
        ("bud_nuhm_reldebt_2025", ENT, "2025", "7413", "2025 verbonden ST schulden 7413 DROP vs 49949; tick1361; primary official NBB WVV 9351"),
        ("bud_nuhm_mortgage_book_2025", ENT, "2025", "6000000", "2025 hypotheek boekwaarde bezwaarde activa 6000000; tick1361; primary official NBB WVV 91611"),
        ("bud_nuhm_lastgeving_2025", ENT, "2025", "15000000", "2025 hypothecaire lastgeving ING 15000000 (inschrijving 25000 + volmacht 5975000); tick1361; primary official NBB WVV 6.19; not TE-additive"),
        ("bud_nuhm_taxlat_2025", ENT, "2025", "1461353", "2025 actieve latenties fiscale verliezen 1461353; tick1361; primary official NBB WVV 9142; not TE-additive"),
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
                "title": "Nuhmeris NV JR2025 leftover NV dual (assets 19.35m / cash 7.96m / FVA sale 6.05m / RE 11.26m / 0-VTE)",
                "entity_id": ENT,
                "beneficiary": "Nuhmeris / NUHMA DC / MyCSN / s-Lim / ING / ECO2050",
                "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; NBB neerlegging; aanbestedende overheid",
                "decision_date": "2026-05-26",
                "start_year": "2014",
                "end_year": "2039",
                "total_envelope_eur": "19350925",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover NV map VL klimaat-holding — MyCSN/s-Lim intra-group sale / RE 11.26m / ING 15m lastgeving",
                "cut_option": "Publish MyCSN/s-Lim sale price vs 6.05m loss + RE 11.26m addresses + why ING lastgeving 15m on 6m asset + why 0-VTE NV holds 7.96m cash after 3.24m capital reduction; do not keep 19m municipal-holding shell as unpublished smart-city RE/cash vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1361; assets 19350925 cash 7959717 fva_sale 6049188 pnl -510182; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Nuhmeris NV JR2025 leftover NV: assets 19.35m / cash 7.96m / FVA sale 6.05m / RE 11.26m / 0-VTE",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "510182",
                "total_cost_eur": "19350925",
                "tco_notes": (
                    "Leftover dual klimaat-holding NV 100pct of NUHMA DC of mined Limburg cities: "
                    "assets 19.35m / equity 13.53m / pnl -0.51m / omzet 0.20m / pers 0 / "
                    "cash jump 7.96m / FVA sale loss 6.05m (MyCSN + s-Lim to parent DC) / "
                    "RE 11.26m (land 6.00m + inventory 5.26m) / ING lastgeving 15m / capred 3.24m / "
                    "ECO2050 1 Cat B book 250 vs 1360 5 Cat A; official NBB WVV live; "
                    "do not treat 19.35m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Nuhmeris / NUHMA DC / MyCSN / s-Lim / ING / ECO2050",
                "stated_goal": "Local leftover NV map VL klimaat-holding — JR2025 live; dual FVA-sale/RE/ING/cash FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 19.35m / cash 7.96m / FVA sale 6.05m / pnl -0.51m; 0 VTE; parent DC 6.5.1 matches",
                "absurdity_score": "7.0",
                "cost_score": "6.2",
                "difficulty": "2.5",
                "priority_index": "6.5",
                "cut_proposal": "Publish MyCSN/s-Lim sale price vs 6.05m loss + RE 11.26m addresses + why ING lastgeving 15m on 6m asset + why 0-VTE NV holds 7.96m cash after 3.24m capital reduction; do not keep 19m municipal-holding shell as unpublished smart-city RE/cash vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1361; leftover NV of mined Limburg + NUHMA DC 1358 / Nuhma cv 1356 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "MyCSN NV + s-Lim cv intra-group sale to Nuhma DC (RvB 05.05.2026) price/date/SPA "
                    "+ FVA realization loss 6049188 (WVV 6631) vs impairment reversal 5493789 (WVV 761) "
                    "+ RE land/buildings 6000000 (no depreciation) + inventory for sale 5260860 unchanged "
                    "+ ING hypothecair 5600000 04.07.2024-31.07.2039 lastgeving 15000000 "
                    "+ capital reduction 3240815 01.01.2025 cash to Nuhma DC / KBO still 24500000 "
                    "+ cash 7959717 JUMP vs 412592 (term deposits 7750000 gone) / omzet 195582 counterparties "
                    "+ ECO2050 1 Cat B 0.01pct book 250 / 2024 EV 9023080 vs ECO2050 1360 5 Cat A "
                    "+ 6.15 related-party refusal (no wettelijk kader) / related ST recv 7944 + debt 7413 "
                    "+ AV 26.05.2026 minutes + RvB 05.05.2026 + official-site JR"
                ),
                "why_it_matters": (
                    "Leftover klimaat-holding NV 100pct of NUHMA DC of mined Limburg cities + Nuhma cv 1356 "
                    "+ Nubema 1359 + ECO2050 1360 + NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353 "
                    "(same zetel Herkenrodesingel 14): "
                    "19.35m assets / 7.96m cash / 11.26m RE / 0 VTE / 196k omzet / intra-group FVA sale 6.05m "
                    "loss / capred 3.24m / ING lastgeving 15m / two consecutive losses "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "Nuhmeris NV / NUHMA DC BV / Nuhma cv / Limburg municipalities",
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
                    "tick1361 leftover NV of mined Limburg cities + NUHMA DC 1358 / Nuhma cv 1356 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 after honest hunt; "
                    "live JR2025 official NBB WVV VOL-kap PDF now extracted (460kB 45p deposit 2026-00124698). "
                    "AGB MAC already mined 1270 — skipped. Westtoer already mined — skipped. "
                    "ECO2050 already mined 1360 — skipped. Nubema already mined 1359 — skipped. NUHMA DC already mined 1358 — skipped. EcoWerf already mined 1357 — skipped. "
                    "IOK/IMOG/Haviland still 2024. Interleuven still 2024 balans. "
                    "POM Limburg glossy-only. Veneco/Leiedal glossy. NBB consult skipped. "
                    "Dommelhof leftover Limburg EVA KBO 0777.495.085 — leftover next if JR2025 PDF. "
                    "Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1361",
        "title": "Nuhmeris NV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Nuhmeris leftover klimaat-holding NV 100pct of NUHMA DC of mined Limburg cities "
            "+ Nuhma cv/Nubema/ECO2050/AC/Bionerga/Limburg.net after honest hunt; KBO 0560.976.140 Actief; "
            "live JR2025 official NBB WVV VOL-kap PDF (460kB 45p deposit 2026-00124698; commissaris Moore); "
            "sourced euros assets 19350925 / cash 7959717 / fva_sale 6049188 / pnl -510182; "
            "FOI ready MyCSN/s-Lim sale/RE 11.26m/ING 15m/cash 7.96m/ECO2050 book"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T00:15:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1361 Nuhmeris leftover NV residual; KBO 0560.976.140; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1362 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1362",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1361 done including Nuhmeris NV 1361 leftover klimaat-holding live NBB WVV / "
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
            "MyCSN NV / S-lim cv / Herkenrode RE leftover Nuhma-family — take only if a statutory 2025 WVV PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland still 2024 — take only if a 2025 JR PDF now downloads; "
            "Veneco / Leiedal / IVOO / MIROM / INCOVO / IVAGO / MIWA / IVAREM / IGEMO — take only if a statutory 2025 WVV/BBC PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1361 after Nuhmeris leftover NV live NBB WVV; next residual dual L5 VL; next every-10 is 1370",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1361", rq_new, rq_spawn)
    print("research_queue 1361", found, "spawned_1362", spawned)

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
                "last_unit_id": "rq_1361",
                "ticks_completed": "1361",
                "paused": "no",
                "notes": (
                    "tick1361 Nuhmeris leftover NV residual; KBO 0560.976.140; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 19350925 cash 7959717 fva_sale 6049188 pnl -510182; "
                    "FOI ready MyCSN/s-Lim/RE/ING/cash; next rq_1362 residual dual L5 VL; continuous hole_fill; next every-10 is 1370"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1361 - 2026-08-19 - rq_1361 Nuhmeris NV dual residual leftover
- Unit: Nuhmeris NV (leftover klimaat-holding NV / smart-city / 100% dochter NUHMA DC BV) of already-mined Limburg cities via Nuhma cv tick1356 (Hasselt / Genk / Tongeren-Borgloon / Houthalen-Helchteren / Bilzen-Hoeselt / Leopoldsburg / Nieuwerkerken / Gingelom / Pelt / Maasmechelen) + leftover BV NUHMA DC tick1358 + leftover NV Nubema tick1359 + leftover cv ECO2050 tick1360 + leftover NV NUHMA AC tick1355 + leftover NV Bionerga tick1354 + leftover IGS Limburg.net tick1353 after residual dual hunt (KBO **0560.976.140**; official nuhma.be is the parent cv — Nuhmeris statutory unpublished on site; live NBB WVV VOL-kap deposit **2026-00124698** PDF 460kB / 45p; AV **26.05.2026**; neerlegging header **27.05.2026**; PDF created **29.05.2026**; commissaris Moore Audit / Jimmy Depré oordeel zonder voorbehoud). Leftover NV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last tick listed Nuhmeris NV 0560.976.140 CDN 2026-00124698 live — leftover next). Distinct from already-mined ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **04.09.2014**; statutaire naam NUHMERIS since 04.09.2014; Naamloze vennootschap since 04.09.2014; zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; **1 VE**; btw since 01.11.2014; **aanbestedende overheid** since 04.09.2014; jaarvergadering mei; KBO-kapitaal still **24.500.000** (statutory 21.259.185); bestuurders Nuhma cv (Ludo Kelchtermans) + Nubema NV (Peter Jans); e-mail via parent info@nuhma.be; tel 011 49 56 10; NACE 62.100 / 62.900 / 62.200. Hunt leftover AGB/zorg/EVA first: AGB MAC Mechelen 2025 BBC already mined tick1270 — skipped; SportAG Aalst / AGB Deinze / AGB Genk already mined — skipped; Westtoer APB already mined — skipped; ECO2050 already mined 1360 — skipped; Nubema already mined 1359 — skipped; NUHMA DC already mined 1358 — skipped; EcoWerf already mined 1357 — skipped; Nuhmeris statutory CDN still live this tick (HTTP 200 / 460490 / 45p) — taken. IOK/IMOG/Haviland still 2024; Interleuven 2025 jaarverslag InDesign embed only / balans still 2024; POM Limburg glossy-only — not taken; Veneco/Leiedal glossy-only; IVAREM activiteitenverslag glossy; IGEMO activiteitenverslag only; IVOO no public 2025 JR; IVAGO SSL EOF; MIWA flipbook; MIROM Cloudflare; De Schorre provincieantwerpen.be 403; APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas not taken (Nuhmeris WVV live); Dommelhof leftover Limburg EVA KBO 0777.495.085 not taken. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE no fetchable 2025 JR this tick. NBB consult skipped (403/SPA); euros extracted from the official VOL-kap deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345. Not every-10 (next 1370).
- EUR strong (primary official WVV VOL-kap + RvB 05.05.2026; commissaris Moore oordeel zonder voorbehoud): assets **19.350.925** (was 23.548.570; RvB 19.350.924,85); fixed **6.000.250** DROP vs 9.832.825; MVA **6.000.000** (terreinen/gebouwen **6.000.000** geen afschrijving; machines 0 after disposal 36.764); FVA **250 DROP** vs 3.796.061 (sold MyCSN NV + s-Lim cv to Nuhma DC; leftover ECO2050 1 Cat B 0,01% book 250 / 2024 EV 9.023.080 — ECO2050 1360 lists Nuhmeris 5 Cat A, **does not match**); current **13.350.675**; voorraden RE for sale **5.260.860** unchanged; ST recv **91.151**; cash **7.959.717 JUMP** vs 412.592 (2024 termijn 7.750.000 converted); prepaid **38.947**; equity **13.531.710** DROP vs 17.282.707 (kapitaal **21.259.185** after reduction **3.240.815** 01.01.2025; accum loss **−7.727.475**); schulden **5.819.215** (ING hypothecair **5.600.000** 04.07.2024–31.07.2039; LT 5.200.000 + within-year 400.000; lastgeving **15.000.000**); omzet **195.582** DROP vs 242.238 / pers **0** / VTE **0**; diensten **18.606**; expl **+86.462**; fin opbr **5.649.659** (rec 155.870 + nr FVA reversal **5.493.789**); fin kosten **6.246.304** (rec 197.115 + nr FVA sale **6.049.188**); PnL **−510.182** (was −249.210; RvB −510.181,70); dividend **0**. Commissaris Moore **3.601**. Parent DC 6.5.1 EV 13.531.710 / PnL −510.182 **matches**. Continuity art. 3:6, 6° (two consecutive losses; aandeelhouderssteun).
- CSVs: sources+4/entities+1/budgets+43/commitments+1/leaderboard+1 + FOI ready `gap_nuhm_fva_sale_6_05m_cash_7_96m_re_11_26m_l5` (not sent); rq_1361=done; spawn rq_1362; ticks=1361.
- Coverage: residual dual L5 (Nuhmeris leftover NV live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1370).
- Next: rq_1362 residual dual L5 VL JR2025 hole_fill (prefer leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover MyCSN NV / S-lim cv / Herkenrode RE only if a statutory 2025 WVV PDF now downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1361 write done")


if __name__ == "__main__":
    main()

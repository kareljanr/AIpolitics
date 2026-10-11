# -*- coding: utf-8 -*-
"""Tick 1359 — leftover Nubema NV JR2025 official NBB WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10 (next every-10 is 1360).
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1359"
UTC = "2026-08-19T03:05:00Z"
ENT = "nv_nubm"
HIER = "Vlaanderen>Limburg>NV>Nubema>KlimaatHolding"
GAP = "gap_nubm_omzet_12_25k_uncalled_375k_eco2050_l5"
SRC = "src_nubm_jr2025_nbb"
SRC2 = "src_nubm_site"
SRC3 = "src_kbo_nubm_0834086964"
SRC4 = "src_nubm_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00124675.pdf"
SRC2_URL = "https://nuhma.be/jaarverslag/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0834086964"
SRC4_URL = "https://nuhma.be/contact/"
FOI_EMAIL = "info@nuhma.be"
FOI_POSTAL = "Herkenrodesingel 14 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_nubm_omzet_12_25k_uncalled_375k_eco2050_l5.md"
COMM = "comm_nubm_jr2025_pnl"
LB = "lb_nubm_omzet_12_25k_uncalled_375k_eco2050"


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
                "title": "Nubema NV jaarrekening boekjaar 2025 (official NBB WVV VOL-kap deposit 2026-00124675; AV 26.05.2026)",
                "url": SRC_URL,
                "publisher": "Nubema NV / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1359; official NBB VOL-kap PDF 175kB 29p deposit 2026-00124675 neerlegging header 27.05.2026 created 29.05.2026; "
                    "leftover klimaat-holding NV 100pct of Nuhma cv 1356 / NUHMA DC 1358 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; parent cv deelnemingstabel EV 187044 / PnL 9438 MATCHES; geen commissaris"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Nuhma official site jaarverslag page (parent cv; Nubema statutory not published separately)",
                "url": SRC2_URL,
                "publisher": "Nuhma cv / Nubema NV",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1359; leftover NV of mined Limburg + Nuhma cv/DC/AC/Bionerga/Limburg.net; "
                    "nuhma.be is Nuhma cv KBO 0472.325.068; jaarverslag page still 2020 PDF only; "
                    "Nubema 0834.086.964 statutory only via NBB deposit"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO NUBEMA 0834.086.964",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1359; KBO 0834.086.964 Actief / normale toestand since 22.02.2011; "
                    "statutaire naam NUBEMA since 25.04.2014; NV since 22.02.2011; "
                    "zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; 1 VE; "
                    "btw since 01.04.2011; aanbestedende overheid since 22.02.2011; "
                    "jaarvergadering mei; kapitaal 500000; bestuurders Nuhma cv + Nuhmeris NV; NACE 70.200/63.920"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Nuhma FOI channel / official contact (parent; Nubema has no KBO email)",
                "url": SRC4_URL,
                "publisher": "Nubema NV / Nuhma cv",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1359; FOI info@nuhma.be; 011 49 56 10; Herkenrodesingel 14 3500 Hasselt "
                    "(same zetel as Nuhma cv / NUHMA DC / NUHMA AC / Bionerga / Limburg.net); geen commissaris"
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
                "name_nl": "Nubema (leftover klimaat-holding NV Limburg / 100pct dochter Nuhma cv / bestuurder NUHMA DC)",
                "name_fr": "Nubema (holding climat residuel Limbourg / filiale 100pct Nuhma sc / administrateur NUHMA DC)",
                "name_en": "Nubema leftover Limburg climate-holding NV (100pct daughter of Nuhma cv; director of NUHMA DC)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://nuhma.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1359 leftover residual klimaat-holding NV 100pct of Nuhma cv 1356 "
                    "+ NUHMA DC 1358 + NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353 (same zetel Herkenrodesingel 14); "
                    "KBO 0834.086.964 Actief since 22.02.2011; official NBB WVV VOL-kap PDF downloads; "
                    "sourced euros assets 188.491 equity 187.044 pnl 9438 omzet 12247 uncalled 375000; "
                    "FOI ready ECO2050/uncalled/omzet/no-commissaris/site-JR"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_nubm_assets_2025", ENT, "2025", "188491", "2025 assets 188491 VOL-kap 20/58; tick1359; primary official NBB WVV; RvB 188491.15"),
        ("bud_nubm_assets_2024", ENT, "2024", "178817", "2024 assets 178817 comparative; tick1359; primary official NBB WVV 20/58"),
        ("bud_nubm_pnl_2025", ENT, "2025", "9438", "2025 PnL 9904 9438; tick1359; primary official NBB WVV + RvB 9437.65"),
        ("bud_nubm_pnl_2024", ENT, "2024", "10413", "2024 PnL 9904 10413 comparative; tick1359; primary official NBB WVV"),
        ("bud_nubm_fixed_2025", ENT, "2025", "1000", "2025 vaste activa/FVA 1000; tick1359; primary official NBB WVV 21/28"),
        ("bud_nubm_current_2025", ENT, "2025", "187491", "2025 vlottende activa 187491 JUMP vs 177817; tick1359; primary official NBB WVV 29/58"),
        ("bud_nubm_equity_2025", ENT, "2025", "187044", "2025 eigen vermogen 187044 JUMP vs 177606; matches parent cv 6.5.1; tick1359; primary official NBB WVV 10/15"),
        ("bud_nubm_equity_2024", ENT, "2024", "177606", "2024 eigen vermogen 177606 comparative; tick1359; primary official NBB WVV 10/15"),
        ("bud_nubm_inbreng_2025", ENT, "2025", "125000", "2025 inbreng/kapitaal 125000 (geplaatst 500000 minus niet-opgevraagd 375000; 1000 aandelen 100pct Nuhma cv); tick1359; primary official NBB WVV 10/11"),
        ("bud_nubm_kap_placed_2025", ENT, "2025", "500000", "2025 geplaatst kapitaal 500000 / 1000 aandelen op naam; tick1359; primary official NBB WVV 100"),
        ("bud_nubm_kap_uncalled_2025", ENT, "2025", "375000", "2025 niet-opgevraagd kapitaal 375000 (Nuhma cv still to pay); tick1359; primary official NBB WVV 101"),
        ("bud_nubm_reserves_2025", ENT, "2025", "62044", "2025 reserves 62044 JUMP vs 52606; tick1359; primary official NBB WVV 13"),
        ("bud_nubm_wettres_2025", ENT, "2025", "10129", "2025 wettelijke reserve 10129 (toevoeging 472); tick1359; primary official NBB WVV 130/6920"),
        ("bud_nubm_availres_2025", ENT, "2025", "51915", "2025 beschikbare reserves 51915 (toevoeging 8966); tick1359; primary official NBB WVV 133/6921"),
        ("bud_nubm_fva_2025", ENT, "2025", "1000", "2025 FVA verbonden deelnemingen 1000 (ECO2050 5pct); tick1359; primary official NBB WVV 280"),
        ("bud_nubm_strecv_2025", ENT, "2025", "860", "2025 ST overige vorderingen 860 DROP vs 1110; tick1359; primary official NBB WVV 41"),
        ("bud_nubm_deposits_2025", ENT, "2025", "160000", "2025 termijnrekeningen 160000 (1m-1y); tick1359; primary official NBB WVV 53/8687"),
        ("bud_nubm_deposits_2024", ENT, "2024", "150000", "2024 termijnrekeningen 150000 comparative; tick1359; primary official NBB WVV 53"),
        ("bud_nubm_cash_2025", ENT, "2025", "24991", "2025 liquide middelen 24991 JUMP vs 24444; tick1359; primary official NBB WVV 54/58"),
        ("bud_nubm_cash_2024", ENT, "2024", "24444", "2024 liquide middelen 24444 comparative; tick1359; primary official NBB WVV 54/58"),
        ("bud_nubm_prepaid_2025", ENT, "2025", "1640", "2025 overlopende activa 1640 (kosten 464 + opbrengsten 1176); tick1359; primary official NBB WVV 490/1"),
        ("bud_nubm_debt_2025", ENT, "2025", "1447", "2025 schulden 1447 JUMP vs 1210; tick1359; primary official NBB WVV 17/49"),
        ("bud_nubm_debt_2024", ENT, "2024", "1210", "2024 schulden 1210 comparative; tick1359; primary official NBB WVV 17/49"),
        ("bud_nubm_st_2025", ENT, "2025", "1094", "2025 ST handelsschulden leveranciers 1094 JUMP vs 532; tick1359; primary official NBB WVV 42/48 440/4"),
        ("bud_nubm_accrued_2025", ENT, "2025", "353", "2025 overlopende passiva 353 DROP vs 679; tick1359; primary official NBB WVV 492/3"),
        ("bud_nubm_reldebt_2025", ENT, "2025", "630", "2025 schulden verbonden ST 630 JUMP vs 532; tick1359; primary official NBB WVV 9351/9371"),
        ("bud_nubm_omzet_2025", ENT, "2025", "12247", "2025 omzet 12247 JUMP vs 11872; tick1359; primary official NBB WVV 70"),
        ("bud_nubm_omzet_2024", ENT, "2024", "11872", "2024 omzet 11872 comparative; tick1359; primary official NBB WVV 70"),
        ("bud_nubm_opscost_2025", ENT, "2025", "2580", "2025 bedrijfskosten 2580 (diensten 1746 + andere 834); tick1359; primary official NBB WVV 60/66A"),
        ("bud_nubm_diensten_2025", ENT, "2025", "1746", "2025 diensten 1746 DROP vs 1854; tick1359; primary official NBB WVV 61"),
        ("bud_nubm_expl_2025", ENT, "2025", "9667", "2025 bedrijfswinst 9667 JUMP vs 9045; tick1359; primary official NBB WVV 9901"),
        ("bud_nubm_fininc_2025", ENT, "2025", "3342", "2025 financiele opbrengsten 3342 DROP vs 5264 (vlottende 751); tick1359; primary official NBB WVV 75/76B"),
        ("bud_nubm_fincost_2025", ENT, "2025", "425", "2025 financiele kosten 425 bankkosten; tick1359; primary official NBB WVV 65/66B"),
        ("bud_nubm_tax_2025", ENT, "2025", "3146", "2025 belastingen 3146 (betaald 4003 minus overschot 857); tick1359; primary official NBB WVV 67/77"),
        ("bud_nubm_div_2025", ENT, "2025", "0", "2025 dividend 0 (694 empty; resultaat naar wettelijke 472 + overige 8966); tick1359; primary official NBB WVV 694"),
        ("bud_nubm_eco2050_ev_2023", ENT, "2023", "8772472", "2023 ECO2050 cv 0699503028 5pct EV 8772472 / PnL 267823 (deelnemingstabel; not Nubema statutory); tick1359; primary official NBB WVV 6.5.1; not TE-additive"),
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
                "title": "Nubema NV JR2025 leftover NV dual (assets 188.5k / omzet 12.25k / uncalled 375k / ECO2050 5pct book 1k)",
                "entity_id": ENT,
                "beneficiary": "Nubema / Nuhma cv / Limburg municipalities / ECO2050",
                "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; NBB neerlegging; aanbestedende overheid",
                "decision_date": "2026-05-26",
                "start_year": "2011",
                "end_year": "2025",
                "total_envelope_eur": "188491",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover NV map VL klimaat-holding — ECO2050 5pct book-vs-EV / 375k uncalled / 12.25k omzet counterparties",
                "cut_option": "Publish ECO2050 2024/2025 EV + uncalled-375k call schedule + omzet/deposit counterparties + official-site JR + why no commissaris; do not keep a parallel 0-VTE public NV shell for 12k omzet",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1359; assets 188491 pnl 9438 omzet 12247 uncalled 375000 eco2050 book 1000; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Nubema NV JR2025 leftover NV: assets 188.5k / omzet 12.25k / uncalled 375k / ECO2050 5pct book 1k",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "12247",
                "total_cost_eur": "188491",
                "tco_notes": (
                    "Leftover dual klimaat-holding NV 100pct of Nuhma cv of mined Limburg cities + DC/AC/Bionerga/Limburg.net: "
                    "assets 188.5k / equity 187.0k / pnl +9.4k / omzet 12.25k / pers 0 / "
                    "termijnrekeningen 160k / uncalled capital 375k from parent / ECO2050 5pct booked 1k vs EV 8.77m (2023); "
                    "geen commissaris; parent cv 6.5.1 MATCHES Nubema statutory; "
                    "official NBB WVV live / site statutory unpublished; do not treat 188.5k as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Nubema / Nuhma cv / Limburg municipalities / ECO2050",
                "stated_goal": "Local leftover NV map VL klimaat-holding — JR2025 live; dual ECO2050/uncalled/omzet FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 188.5k / omzet 12.25k / pnl +9.4k / uncalled 375k; geen commissaris",
                "absurdity_score": "6.8",
                "cost_score": "3.5",
                "difficulty": "2.5",
                "priority_index": "4.8",
                "cut_proposal": "Publish ECO2050 2024/2025 EV + uncalled-375k call schedule + omzet/deposit counterparties + official-site JR + why no commissaris; do not keep a parallel 0-VTE public NV shell for 12k omzet",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1359; leftover NV of mined Limburg + Nuhma cv 1356 / NUHMA DC 1358 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; FOI ready not sent; not TE-additive of 348bn",
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
                    "ECO2050 cv 0699503028 5pct 1 aandeel Cat A book 1000 vs EV 8772472 / PnL 267823 (WVV 6.5.1 still 2023-12-31) "
                    "+ 2024/2025 ECO2050 JR or internal EV/PnL + why 5pct still held at 1k book "
                    "+ uncalled capital 375000 (WVV 101; Nuhma cv 100pct / 1000 aandelen; geplaatst 500000) call schedule and purpose "
                    "+ omzet 12247 counterparties (intra-group management fees?) "
                    "+ termijnrekeningen 160000 bank/term (WVV 53/8687) "
                    "+ related-party ST debt 630 counterparties (WVV 9351/9371) "
                    "+ 6.15 related-party refusal (no wettelijk kader) "
                    "+ why no commissaris despite aanbestedende overheid / 100pct public via Nuhma "
                    "+ AV 26.05.2026 minutes + RvB 05.05.2026 + official-site statutory JR PDF of Nubema "
                    "+ dual role as KBO bestuurder of NUHMA DC since 26.05.2025"
                ),
                "why_it_matters": (
                    "Leftover klimaat-holding NV shell 100pct of Nuhma cv of mined Limburg cities + NUHMA DC 1358 "
                    "+ NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353 (same zetel Herkenrodesingel 14): "
                    "188.5k assets / 12.25k omzet / 0 VTE / 160k term deposits / 375k uncalled / "
                    "ECO2050 5pct booked 1k vs 8.77m EV (2023) / no commissaris is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "Nubema NV / Nuhma cv / Limburg municipalities",
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
                    "tick1359 leftover NV of mined Limburg cities + Nuhma cv 1356 / NUHMA DC 1358 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 after honest hunt; "
                    "live JR2025 official NBB WVV VOL-kap PDF now extracted (175kB 29p deposit 2026-00124675). "
                    "AGB MAC already mined 1270 — skipped. Westtoer already mined — skipped. "
                    "NUHMA DC already mined 1358 — skipped. EcoWerf already mined 1357 — skipped. "
                    "IOK/IMOG/Haviland still 2024. Interleuven still 2024 balans. "
                    "POM Limburg glossy-only. Veneco/Leiedal glossy. NBB consult skipped. "
                    "Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1359",
        "title": "Nubema NV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Nubema leftover klimaat-holding NV 100pct of Nuhma cv of mined Limburg cities + DC/AC/Bionerga/Limburg.net "
            "after honest hunt; KBO 0834.086.964 Actief; live JR2025 official NBB WVV VOL-kap PDF "
            "(175kB 29p deposit 2026-00124675; geen commissaris); "
            "sourced euros assets 188.491 / equity 187.044 / pnl 9438 / omzet 12247 / uncalled 375000; "
            "FOI ready ECO2050/uncalled/omzet/no-commissaris/site-JR"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T02:40:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1359 Nubema leftover NV residual; KBO 0834.086.964; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1360 every-10 + residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1360",
        "title": "Continuous FOI-adjacent public hole-fill batch + every-10 progress",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "EVERY-10 first: refresh docs/doge/data/progress_every_10_ticks.md (layers A-E percent of 347.956 bn TE) "
            "and docs/doge/data/doge_waste_top10_current.md (top 10 by priority_index + short high-absurdity); "
            "then residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1359 done including Nubema NV 1359 leftover klimaat-holding live NBB WVV / "
            "NUHMA DC BV 1358 leftover klimaat-holding live NBB WVV / "
            "EcoWerf 1357 leftover IGS live NBB WVV / "
            "Nuhma cv 1356 leftover klimaat-holding live NBB WVV / "
            "NUHMA AC NV 1355 leftover klimaat-holding live NBB WVV / "
            "Bionerga NV 1354 leftover waste-processing live NBB WVV / "
            "Limburg.net 1353 leftover IGS glossy-only FOI / IVBO 1352 leftover IGS live WVV / "
            "SOLVA 1351 leftover IGS live JR / Interwaas 1350 leftover IGS live WVV + every-10 / "
            "Aquaduin / IWVA ov 1349 leftover IGS live WVV / Creat Services dv 1348 leftover IGS live WVV / "
            "IVIO Izegem-Ommeland 1347 leftover IGS live JR operational / WVI West-Vlaanderen 1346 leftover IGS live WVV / "
            "IVVO Veurne-Ommeland 1345 leftover IGS live WVV / ILvA Land van Aalst 1344 leftover IGS live WVV / "
            "IVM Meetjesland 1343 leftover IGS live WVV / IDM Durme-Moervaart 1342 leftover IGS live WVV / "
            "IGEAN dienstverlening 1341 leftover IGS live WVV / EVA Limburg Sterk Merk 1340 leftover EVA live WVV + every-10); "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "Veneco glossy jaarverslag 2025 websingle — take only if a WVV/BBC PDF now downloads; "
            "Leiedal 2025 InDesign glossy-only — take only if a WVV/BBC PDF now downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland still 2024 — take only if a 2025 JR PDF now downloads; "
            "IVOO no public 2025 JR PDF — take only if a 2025 JR PDF now downloads; "
            "MIROM 403 — take only if a 2025 JR PDF now downloads; "
            "INCOVO still 2024 — take only if a 2025 JR PDF now downloads; "
            "IVAGO activiteitenverslag 2025 listed but SSL EOF / ebesluit Gent TLS — take only if a statutory WVV/BBC PDF now downloads; "
            "MIWA 2025 aflip flipbook only — take only if a WVV/BBC PDF now downloads; "
            "IVAREM still 2024 / activiteitenverslag 2025 glossy — take only if a 2025 JR PDF now downloads; "
            "IGEMO activiteitenverslag 2025 only — take only if a WVV/BBC PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
            "WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / "
            "WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403; every-10 first"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1359 after Nubema leftover NV live NBB WVV; next every-10 progress + residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1359", rq_new, rq_spawn)
    print("research_queue 1359", found, "spawned_1360", spawned)

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
                "last_unit_id": "rq_1359",
                "ticks_completed": "1359",
                "paused": "no",
                "notes": (
                    "tick1359 Nubema leftover NV residual; KBO 0834.086.964; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 188.491 equity 187.044 pnl 9438 omzet 12247 uncalled 375000; "
                    "FOI ready ECO2050/uncalled/omzet/no-commissaris; next rq_1360 every-10 + residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1359 - 2026-08-19 - rq_1359 Nubema NV dual residual leftover
- Unit: Nubema NV (leftover klimaat-holding NV / 100% dochter Nuhma cv / KBO-bestuurder NUHMA DC) of already-mined Limburg cities via Nuhma cv tick1356 (Hasselt / Genk / Tongeren-Borgloon / Houthalen-Helchteren / Bilzen-Hoeselt / Leopoldsburg / Nieuwerkerken / Gingelom / Pelt / Maasmechelen) + leftover BV NUHMA DC tick1358 + leftover NV NUHMA AC tick1355 + leftover NV Bionerga tick1354 + leftover IGS Limburg.net tick1353 after residual dual hunt (KBO **0834.086.964**; official nuhma.be is the parent cv — Nubema statutory unpublished on site; live NBB WVV VOL-kap deposit **2026-00124675** PDF 175kB / 29p; AV **26.05.2026**; neerlegging header **27.05.2026**; PDF created **29.05.2026**; **geen commissaris**). Leftover NV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last ticks listed Nubema as leftover later pending statutory WVV). Distinct from already-mined NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **22.02.2011**; statutaire naam NUBEMA since 25.04.2014; Naamloze vennootschap since 22.02.2011; zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; **1 VE**; btw since 01.04.2011; **aanbestedende overheid** since 22.02.2011; jaarvergadering mei; kapitaal 500.000; bestuurders Nuhma cv (Ludo Kelchtermans) + Nuhmeris NV (Peter Jans); e-mail via parent info@nuhma.be; tel 011 49 56 10; NACE 70.200 / 63.920. Hunt leftover AGB/zorg/EVA first: AGB MAC Mechelen 2025 BBC already mined tick1270 — skipped; SportAG Aalst / AGB Deinze / AGB Genk already mined — skipped; Westtoer APB already mined — skipped; NUHMA DC already mined 1358 — skipped; EcoWerf already mined 1357 — skipped; Nubema statutory CDN now live this tick (HTTP 200 / 175114 / 29p) — taken. IOK/IMOG/Haviland still 2024; Interleuven 2025 jaarverslag InDesign embed only / balans still 2024; POM Limburg glossy-only — not taken; Veneco/Leiedal glossy-only; IVAREM activiteitenverslag glossy; IGEMO activiteitenverslag only; IVOO no public 2025 JR; IVAGO SSL EOF; MIWA flipbook; MIROM Cloudflare; De Schorre provincieantwerpen.be 403; APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas not taken (Nubema WVV live); Dommelhof leftover Limburg EVA KBO 0777.495.085 not taken. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE no fetchable 2025 JR this tick. NBB consult skipped (403/SPA); euros extracted from the official VOL-kap deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345. Not every-10 (next 1360).
- EUR strong (primary official WVV VOL-kap + RvB 05.05.2026; geen commissaris): assets **188.491** (was 178.817; RvB 188.491,15); fixed/FVA **1.000** (verbonden deelneming ECO2050 cv 0699.503.028 5% / 1 aandeel Cat A; EV **8.772.472** / PnL **267.823** boekjaar **2023**); current **187.491**; ST recv **860**; termijnrekeningen **160.000** JUMP vs 150.000 (1m–1j); cash **24.991** JUMP vs 24.444; overlopend actief **1.640** (kosten 464 + opbrengsten 1.176); equity **187.044** JUMP vs 177.606 (geplaatst **500.000** / 1.000 aandelen 100% Nuhma cv; niet-opgevraagd **375.000** Nuhma cv; inbreng **125.000**; reserves **62.044** waarvan wettelijk **10.129** + beschikbaar **51.915**); schulden **1.447** JUMP vs 1.210 (ST leveranciers **1.094**; overlopend **353**; verbonden ST **630**); omzet **12.247** JUMP vs 11.872 / pers **0** / VTE **0**; diensten **1.746**; expl **+9.667**; fin opbr **3.342** DROP vs 5.264 (vlottende); fin kosten **425** bankkosten; belasting **3.146**; PnL **+9.438** (was +10.413; RvB 9.437,65); dividend **0** (wettelijk 472 + overige 8.966). Parent cv 6.5.1 EV 187.044 / PnL 9.438 **matches** Nubema statutory.
- CSVs: sources+4/entities+1/budgets+36/commitments+1/leaderboard+1 + FOI ready `gap_nubm_omzet_12_25k_uncalled_375k_eco2050_l5` (not sent); rq_1359=done; spawn rq_1360; ticks=1359.
- Coverage: residual dual L5 (Nubema leftover NV live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1360).
- Next: rq_1360 **every-10 progress first** then residual dual L5 VL JR2025 hole_fill (prefer leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; MIROM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1359 write done")


if __name__ == "__main__":
    main()

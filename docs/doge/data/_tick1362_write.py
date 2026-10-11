# -*- coding: utf-8 -*-
"""Tick 1362 — leftover s-Lim CV JR2025 official NBB WVV euros.
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

TICK = "1362"
UTC = "2026-08-19T01:20:00Z"
ENT = "cv_slim"
HIER = "Vlaanderen>Limburg>CV>s-Lim>SmartCity"
GAP = "gap_slim_omzet_2_39m_pnl_neg_1_36m_votes_l5"
SRC = "src_slim_jr2025_nbb"
SRC2 = "src_slim_site"
SRC3 = "src_kbo_slim_0679631191"
SRC4 = "src_slim_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00118633.pdf"
SRC2_URL = "https://s-lim.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0679631191"
SRC4_URL = "https://s-lim.be/contact/"
FOI_EMAIL = "info@s-lim.be"
FOI_POSTAL = "Herkenrodesingel 14 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_slim_omzet_2_39m_pnl_neg_1_36m_votes_l5.md"
COMM = "comm_slim_jr2025_pnl"
LB = "lb_slim_omzet_2_39m_pnl_neg_1_36m_votes"


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
                "title": "s-Lim CV jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00118633; AV 04.05.2026)",
                "url": SRC_URL,
                "publisher": "s-Lim CV / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1362; official NBB VOL-inb PDF 5.38MB 48p deposit 2026-00118633 neerlegging 19.05.2026 created 23.05.2026; "
                    "leftover smart-city CV of NUHMA DC 1358 / Nuhma cv 1356 / Nuhmeris 1361 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris EY / Christophe Beckers signed 15.04.2026 (verslag image-embedded); "
                    "parent DC 6.5.1 EV 2599382 / PnL -1355216 MATCHES"
                ),
            },
            {
                "source_id": SRC2,
                "title": "s-Lim official site (smart-city CV; statutory JR unpublished on site)",
                "url": SRC2_URL,
                "publisher": "s-Lim CV",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1362; leftover CV of mined Limburg + Nuhma cv/DC/AC/Nubema/ECO2050/Nuhmeris/Bionerga/Limburg.net; "
                    "s-lim.be has no JR PDF; partner MyCSN + Nuhma; "
                    "s-Lim DV described as intergemeentelijke samenwerking Limburg + Laakdal"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO s-Lim 0679.631.191",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1362; KBO 0679.631.191 Actief / normale toestand since 07.08.2017; "
                    "statutaire naam s-Lim since 07.08.2017; CV since 23.12.2019; "
                    "zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; 1 VE; "
                    "btw since 07.08.2017; RSZ since 06.08.2018; "
                    "jaarvergadering mei; boekjaar 31 december; 19 functiehouders; "
                    "voorzitter Yilmaz Kurtal since 25.03.2025; no KBO email/web/tel"
                ),
            },
            {
                "source_id": SRC4,
                "title": "s-Lim FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "s-Lim CV",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1362; FOI info@s-lim.be; "
                    "Herkenrodesingel 14 3500 Hasselt (same zetel as Nuhma cv / Nubema / NUHMA DC / NUHMA AC / ECO2050 / Nuhmeris / Bionerga / Limburg.net); "
                    "PEPPOL s-Lim CV 0208:1001753840 / s-Lim DV 0208:0805138503"
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
                "name_nl": "s-Lim (leftover smart-city CV Limburg / Nuhma DC deelneming)",
                "name_fr": "s-Lim (cooperative smart city residuelle Limbourg / participation Nuhma DC)",
                "name_en": "s-Lim leftover Limburg smart-city CV (Nuhma DC participation)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://s-lim.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1362 leftover residual smart-city CV of NUHMA DC 1358 "
                    "+ Nuhma cv 1356 + Nuhmeris 1361 + Nubema 1359 + ECO2050 1360 + NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353 "
                    "(same zetel Herkenrodesingel 14); "
                    "KBO 0679.631.191 Actief since 07.08.2017; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 4282111 omzet 2393079 pnl -1355216; "
                    "FOI ready 6.10/votes vs 49.99pct/DV-loan 2m/related/taxlat 11.28m"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_slim_assets_2025", ENT, "2025", "4282111", "2025 assets 4282111 VOL-inb 20/58; tick1362; primary official NBB WVV"),
        ("bud_slim_assets_2024", ENT, "2024", "5334436", "2024 assets 5334436 comparative; tick1362; primary official NBB WVV 20/58"),
        ("bud_slim_fixed_2025", ENT, "2025", "2142965", "2025 vaste activa 2142965 JUMP vs 1305682; tick1362; primary official NBB WVV 21/28"),
        ("bud_slim_iva_2025", ENT, "2025", "489620", "2025 IVA 489620 DROP vs 734480 (licences/software); tick1362; primary official NBB WVV 21"),
        ("bud_slim_mva_2025", ENT, "2025", "1653345", "2025 MVA 1653345 JUMP vs 571202; tick1362; primary official NBB WVV 22/27"),
        ("bud_slim_machines_2025", ENT, "2025", "1645271", "2025 installaties/machines 1645271 JUMP vs 565445; tick1362; primary official NBB WVV 23"),
        ("bud_slim_machacq_2025", ENT, "2025", "1179694", "2025 machines aanschaf 1179694; tick1362; primary official NBB WVV 6.3.2 8162"),
        ("bud_slim_current_2025", ENT, "2025", "2139146", "2025 vlottende activa 2139146 DROP vs 4028754; tick1362; primary official NBB WVV 29/58"),
        ("bud_slim_current_2024", ENT, "2024", "4028754", "2024 vlottende activa 4028754 comparative; tick1362; primary official NBB WVV 29/58"),
        ("bud_slim_wip_2025", ENT, "2025", "65734", "2025 bestellingen in uitvoering 65734; tick1362; primary official NBB WVV 37"),
        ("bud_slim_strecv_2025", ENT, "2025", "699831", "2025 ST vorderingen 699831 (trade 511274 + other 188557); tick1362; primary official NBB WVV 40/41"),
        ("bud_slim_cash_2025", ENT, "2025", "1030902", "2025 liquide middelen 1030902 JUMP vs 810663; tick1362; primary official NBB WVV 54/58"),
        ("bud_slim_cash_2024", ENT, "2024", "810663", "2024 liquide middelen 810663 comparative; tick1362; primary official NBB WVV 54/58"),
        ("bud_slim_term_2024", ENT, "2024", "2000000", "2024 termijnrekeningen 2000000 (1.5m <1m + 0.5m 1m-1y) gone 2025; tick1362; primary official NBB WVV 53"),
        ("bud_slim_prepaid_2025", ENT, "2025", "342678", "2025 overlopend actief 342678 (kosten 331015 + opbrengsten 11663); tick1362; primary official NBB WVV 490/1"),
        ("bud_slim_equity_2025", ENT, "2025", "2599382", "2025 eigen vermogen 2599382 DROP vs 3954599; matches parent DC 6.5.1; tick1362; primary official NBB WVV 10/15"),
        ("bud_slim_equity_2024", ENT, "2024", "3954599", "2024 eigen vermogen 3954599 comparative; tick1362; primary official NBB WVV 10/15"),
        ("bud_slim_inbreng_2025", ENT, "2025", "2599382", "2025 onbeschikbare inbreng 2599382 (all equity; loss absorbed); tick1362; primary official NBB WVV 111"),
        ("bud_slim_debt_2025", ENT, "2025", "1682728", "2025 schulden 1682728 JUMP vs 1379837; tick1362; primary official NBB WVV 17/49"),
        ("bud_slim_st_2025", ENT, "2025", "1474417", "2025 ST schulden 1474417 JUMP vs 832833 (no LT debt); tick1362; primary official NBB WVV 42/48"),
        ("bud_slim_trade_2025", ENT, "2025", "1394096", "2025 leveranciers 1394096 JUMP vs 728308; tick1362; primary official NBB WVV 440/4"),
        ("bud_slim_soc_2025", ENT, "2025", "80322", "2025 bezoldigingen/sociale lasten 80322; tick1362; primary official NBB WVV 454/9"),
        ("bud_slim_accrued_2025", ENT, "2025", "208311", "2025 overlopend passief 208311 (kosten 185124 + opbrengsten 23187); tick1362; primary official NBB WVV 492/3"),
        ("bud_slim_ops_2025", ENT, "2025", "2567574", "2025 bedrijfsopbrengsten 2567574; tick1362; primary official NBB WVV 70/76A"),
        ("bud_slim_omzet_2025", ENT, "2025", "2393079", "2025 omzet 2393079 DROP vs 2723349; 6.10 category/geo empty; tick1362; primary official NBB WVV 70"),
        ("bud_slim_omzet_2024", ENT, "2024", "2723349", "2024 omzet 2723349 comparative; tick1362; primary official NBB WVV 70"),
        ("bud_slim_andere_2025", ENT, "2025", "126150", "2025 andere bedrijfsopbrengsten 126150; tick1362; primary official NBB WVV 74"),
        ("bud_slim_opscost_2025", ENT, "2025", "3952610", "2025 bedrijfskosten 3952610; tick1362; primary official NBB WVV 60/66A"),
        ("bud_slim_goods_2025", ENT, "2025", "1432077", "2025 handelsgoederen 1432077; tick1362; primary official NBB WVV 60"),
        ("bud_slim_diensten_2025", ENT, "2025", "1471861", "2025 diensten 1471861 JUMP vs 1137140; tick1362; primary official NBB WVV 61"),
        ("bud_slim_pers_2025", ENT, "2025", "698849", "2025 pers 698849 / avg VTE 4.8 / YE 5 koppen; tick1362; primary official NBB WVV 62/6.10"),
        ("bud_slim_afschr_2025", ENT, "2025", "348764", "2025 afschrijvingen 348764; tick1362; primary official NBB WVV 630"),
        ("bud_slim_expl_2025", ENT, "2025", "-1385036", "2025 bedrijfsverlies -1385036 (was -1240478); tick1362; primary official NBB WVV 9901"),
        ("bud_slim_fininc_2025", ENT, "2025", "34634", "2025 financiele opbrengsten 34634 (vlottende); tick1362; primary official NBB WVV 75"),
        ("bud_slim_fincost_2025", ENT, "2025", "3176", "2025 financiele kosten 3176; tick1362; primary official NBB WVV 65"),
        ("bud_slim_pnl_2025", ENT, "2025", "-1355216", "2025 PnL 9904 -1355216 DROP vs -1137032; tick1362; primary official NBB WVV; matches parent DC 6.5.1"),
        ("bud_slim_pnl_2024", ENT, "2024", "-1137032", "2024 PnL -1137032 comparative; tick1362; primary official NBB WVV 9904"),
        ("bud_slim_comm_2025", ENT, "2025", "10430", "2025 commissaris EY 10430; tick1362; primary official NBB WVV 9505"),
        ("bud_slim_relrecv_2025", ENT, "2025", "194550", "2025 verbonden ST vorderingen 194550 DROP vs 589770; tick1362; primary official NBB WVV 9291"),
        ("bud_slim_reldebt_2025", ENT, "2025", "322279", "2025 verbonden ST schulden 322279 DROP vs 460923; tick1362; primary official NBB WVV 9351"),
        ("bud_slim_taxlat_2025", ENT, "2025", "11279467", "2025 actieve latenties fiscale verliezen 11279467; tick1362; primary official NBB WVV 9142; not TE-additive"),
        ("bud_slim_inbreng_onttrek_2025", ENT, "2025", "1355216", "2025 onttrekking aan inbreng 1355216 (absorbs year loss); tick1362; primary official NBB WVV 791"),
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
                "title": "s-Lim CV JR2025 leftover CV dual (assets 4.28m / omzet 2.39m / PnL -1.36m / 4.8 VTE)",
                "entity_id": ENT,
                "beneficiary": "s-Lim / s-Lim DV / NUHMA DC / Nuhma cv / Limburg municipalities / MyCSN",
                "legal_basis": "WVV CV; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-05-04",
                "start_year": "2017",
                "end_year": "2026",
                "total_envelope_eur": "4282111",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover CV map VL smart-city — 6.10 empty / votes vs 49.99pct / DV-loan 2m off-balance",
                "cut_option": "Publish 6.10 municipal counterparties + reconcile Nuhma DC 49.99pct book vs 16.43pct votes + put s-Lim DV 2m estimated loan on balance + why 11.28m tax losses sit on 4.28m assets; do not keep 4.3m municipal smart-city CV as unpublished dual vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1362; assets 4282111 omzet 2393079 pnl -1355216; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "s-Lim CV JR2025 leftover CV: assets 4.28m / omzet 2.39m / PnL -1.36m / votes vs 49.99pct",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "1355216",
                "total_cost_eur": "4282111",
                "tco_notes": (
                    "Leftover dual smart-city CV of NUHMA DC of mined Limburg cities: "
                    "assets 4.28m / equity 2.60m / pnl -1.36m / omzet 2.39m / pers 0.70m / 4.8 VTE / "
                    "s-Lim DV 83.57pct votes vs Nuhma DC 16.43pct votes / 49.99pct book / "
                    "DV-loan 2m estimated off-balance / tax losses 11.28m / official NBB WVV live; "
                    "do not treat 4.28m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "s-Lim / s-Lim DV / NUHMA DC / Nuhma cv / Limburg municipalities / MyCSN",
                "stated_goal": "Local leftover CV map VL smart-city — JR2025 live; dual 6.10/votes/DV-loan FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 4.28m / omzet 2.39m / pnl -1.36m; 4.8 VTE; parent DC 6.5.1 matches",
                "absurdity_score": "6.8",
                "cost_score": "5.4",
                "difficulty": "2.5",
                "priority_index": "6.2",
                "cut_proposal": "Publish 6.10 municipal counterparties + reconcile Nuhma DC 49.99pct book vs 16.43pct votes + put s-Lim DV 2m estimated loan on balance + why 11.28m tax losses sit on 4.28m assets; do not keep 4.3m municipal smart-city CV as unpublished dual vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1362; leftover CV of mined Limburg + NUHMA DC 1358 / Nuhma cv 1356 / Nuhmeris 1361 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "6.10 omzet 2393079 category/geo split empty + per-gemeente/MyCSN/Nuhma/Fluvius/s-Lim DV counterparties "
                    "+ Nuhma DC 49.99pct book (tick1358 6.5.1) vs 16.43pct votes (4.999 Cat A) / s-Lim DV 0805138503 67.13pct+16.44pct "
                    "+ intra-group transfer from Nuhmeris (tick1361 FVA sale) "
                    "+ continuity art.3:6 6deg s-Lim DV loan estimated 2mEUR + 1.9m product development through 2026 (NOT on LT debt; WVV 17 empty) "
                    "+ related ST recv 194550 + ST debt 322279 unnamed / 6.15 related-party refusal "
                    "+ machines aanschaf 1179694 vs termijn 2000000 gone "
                    "+ tax losses 11279467 on assets 4282111 "
                    "+ image-only jaarverslag/commissaris EY 10430 + official-site JR"
                ),
                "why_it_matters": (
                    "Leftover smart-city CV of NUHMA DC of mined Limburg cities + Nuhma cv 1356 "
                    "+ Nuhmeris 1361 + Nubema 1359 + ECO2050 1360 + NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353 "
                    "(same zetel Herkenrodesingel 14): "
                    "4.28m assets / 2.39m omzet / -1.36m pnl / 4.8 VTE / DV 83.57pct votes vs DC 49.99pct book / "
                    "off-balance DV-loan 2m / tax losses 11.28m / two consecutive losses "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "s-Lim CV / s-Lim DV / NUHMA DC BV / Nuhma cv / Limburg municipalities",
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
                    "tick1362 leftover CV of mined Limburg cities + NUHMA DC 1358 / Nuhma cv 1356 / Nuhmeris 1361 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (5.38MB 48p deposit 2026-00118633). "
                    "AGB MAC already mined 1270 — skipped. Westtoer already mined — skipped. "
                    "Nuhmeris already mined 1361 — skipped. ECO2050 already mined 1360 — skipped. Nubema already mined 1359 — skipped. NUHMA DC already mined 1358 — skipped. EcoWerf already mined 1357 — skipped. "
                    "MyCSN NV 0724946623 CDN 2026-00126775 listed — leftover next. "
                    "Herkenrode RE 0724557633 CDN 2026-00124490 listed — leftover later. "
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
        "task_id": "rq_1362",
        "title": "s-Lim CV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: s-Lim leftover smart-city CV of NUHMA DC of mined Limburg cities "
            "+ Nuhma cv/Nuhmeris/Nubema/ECO2050/AC/Bionerga/Limburg.net after honest hunt; KBO 0679.631.191 Actief; "
            "live JR2025 official NBB WVV VOL-inb PDF (5.38MB 48p deposit 2026-00118633; commissaris EY); "
            "sourced euros assets 4282111 / omzet 2393079 / pnl -1355216; "
            "FOI ready 6.10/votes vs 49.99pct/DV-loan 2m/related/taxlat 11.28m"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T00:50:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1362 s-Lim leftover CV residual; KBO 0679.631.191; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1363 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1363",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1362 done including s-Lim CV 1362 leftover smart-city live NBB WVV / "
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
            "MyCSN NV 0724.946.623 leftover Nuhma-family CDN 2026-00126775 — take only if a statutory 2025 WVV PDF now downloads; "
            "Herkenrode RE 0724.557.633 leftover Nuhma-family CDN 2026-00124490 — take only if a statutory 2025 WVV PDF now downloads; "
            "s-Lim DV 0805.138.503 leftover IGS (67.13pct+16.44pct of s-Lim CV votes) — take only if a statutory 2025 WVV/BBC PDF now downloads; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland still 2024 — take only if a 2025 JR PDF now downloads; "
            "Veneco / Leiedal / IVOO / MIROM / INCOVO / IVAGO / MIWA / IVAREM / IGEMO — take only if a statutory 2025 WVV/BBC PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined s-Lim 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1362 after s-Lim leftover CV live NBB WVV; next residual dual L5 VL; next every-10 is 1370",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1362", rq_new, rq_spawn)
    print("research_queue 1362", found, "spawned_1363", spawned)

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
                "last_unit_id": "rq_1362",
                "ticks_completed": "1362",
                "paused": "no",
                "notes": (
                    "tick1362 s-Lim leftover CV residual; KBO 0679.631.191; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 4282111 omzet 2393079 pnl -1355216; "
                    "FOI ready 6.10/votes/DV-loan; next rq_1363 residual dual L5 VL; continuous hole_fill; next every-10 is 1370"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1362 - 2026-08-19 - rq_1362 s-Lim CV dual residual leftover
- Unit: s-Lim CV (leftover smart-city cooperatie / sold this year from Nuhmeris NV to NUHMA DC BV) of already-mined Limburg cities via Nuhma cv tick1356 (Hasselt / Genk / Tongeren-Borgloon / Houthalen-Helchteren / Bilzen-Hoeselt / Leopoldsburg / Nieuwerkerken / Gingelom / Pelt / Maasmechelen) + leftover BV NUHMA DC tick1358 + leftover NV Nuhmeris tick1361 + leftover NV Nubema tick1359 + leftover cv ECO2050 tick1360 + leftover NV NUHMA AC tick1355 + leftover NV Bionerga tick1354 + leftover IGS Limburg.net tick1353 after residual dual hunt (KBO **0679.631.191**; official s-lim.be has no JR PDF; live NBB WVV VOL-inb deposit **2026-00118633** PDF 5.38MB / 48p; AV **04.05.2026**; neerlegging **19.05.2026**; PDF created **23.05.2026**; commissaris EY / Christophe Beckers signed 15.04.2026; jaarverslag + commissarisverslag image-embedded). Leftover CV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last tick listed leftover MyCSN / S-lim / Herkenrode only if a statutory 2025 WVV now downloads). Distinct from already-mined Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **07.08.2017**; statutaire naam s-Lim since 07.08.2017; Cooperatieve vennootschap since 23.12.2019; zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; **1 VE**; btw since 07.08.2017; RSZ since 06.08.2018; jaarvergadering mei; 19 functiehouders; voorzitter Yilmaz Kurtal since 25.03.2025; e-mail info@s-lim.be; NACE 63.100 / 62.200 / 62.100. Hunt leftover AGB/zorg/EVA first: AGB MAC Mechelen 2025 BBC already mined tick1270 — skipped; SportAG Aalst / AGB Deinze / AGB Genk already mined — skipped; Westtoer APB already mined — skipped; Nuhmeris already mined 1361 — skipped; ECO2050 already mined 1360 — skipped; Nubema already mined 1359 — skipped; NUHMA DC already mined 1358 — skipped; EcoWerf already mined 1357 — skipped; s-Lim statutory CDN live this tick (HTTP 200 / 5381213 / 48p) — taken. MyCSN NV 0724.946.623 CDN 2026-00126775 listed — leftover next. Herkenrode RE 0724.557.633 CDN 2026-00124490 listed — leftover later. s-Lim DV 0805.138.503 leftover IGS later. IOK/IMOG/Haviland still 2024; Interleuven 2025 jaarverslag InDesign embed only / balans still 2024; POM Limburg glossy-only — not taken; Veneco/Leiedal glossy-only; IVAREM activiteitenverslag glossy; IGEMO activiteitenverslag only; IVOO no public 2025 JR; IVAGO SSL EOF; MIWA flipbook; MIROM Cloudflare; De Schorre provincieantwerpen.be 403; APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas not taken (s-Lim WVV live); Dommelhof leftover Limburg EVA KBO 0777.495.085 still no 2026 PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE no fetchable 2025 JR this tick. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345. Not every-10 (next 1370).
- EUR strong (primary official WVV VOL-inb; parent DC 6.5.1 EV 2.599.382 / PnL −1.355.216 **matches**): assets **4.282.111** (was 5.334.436); fixed **2.142.965** JUMP vs 1.305.682; IVA **489.620** DROP vs 734.480; MVA **1.653.345** (machines **1.645.271** JUMP vs 565.445 after aanschaf **1.179.694** + meubilair 8.074); FVA empty; current **2.139.146** DROP vs 4.028.754 (termijn **2.000.000** gone); ST recv **699.831**; cash **1.030.902 JUMP** vs 810.663; prepaid **342.678**; equity **2.599.382** DROP vs 3.954.599 (all onbeschikbare inbreng; loss **1.355.216** onttrokken aan inbreng); schulden **1.682.728** (no LT; ST **1.474.417** waarvan leveranciers **1.394.096 JUMP** vs 728.308); omzet **2.393.079** DROP vs 2.723.349 / pers **698.849** / avg VTE **4,8** / YE **5** koppen (all men, bedienden); diensten **1.471.861** JUMP vs 1.137.140; goods **1.432.077**; afschr **348.764**; expl **−1.385.036**; fin opbr **34.634**; fin kosten **3.176**; PnL **−1.355.216** (was −1.137.032); dividend **0**. Stemrechten: s-Lim DV 0805.138.503 Cat C 20.422 / **67,13%** + Cat B 5.000 / **16,44%**; Nuhma DC 4.999 Cat A / **16,43%** vs parent 49,99% book; Nuhma cv 1 Cat A. Related ST recv **194.550** / ST debt **322.279**. Tax losses **11.279.467**. Continuity art. 3:6, 6° (s-Lim DV-lening geraamd 2m + 1,9m productontwikkeling tot 2026 — **not** on LT debt). Commissaris EY **10.430**. 6.10 category/geo empty. 6.15 related-party refusal.
- CSVs: sources+4/entities+1/budgets+42/commitments+1/leaderboard+1 + FOI ready `gap_slim_omzet_2_39m_pnl_neg_1_36m_votes_l5` (not sent); rq_1362=done; spawn rq_1363; ticks=1362.
- Coverage: residual dual L5 (s-Lim leftover CV live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1370).
- Next: rq_1363 residual dual L5 VL JR2025 hole_fill (prefer leftover MyCSN NV 0724.946.623 CDN 2026-00126775 if still live; leftover Herkenrode RE 0724.557.633 CDN 2026-00124490 only if a statutory 2025 WVV PDF now downloads; leftover s-Lim DV 0805.138.503 only if a statutory 2025 WVV/BBC PDF now downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined s-Lim 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1362 write done")


if __name__ == "__main__":
    main()

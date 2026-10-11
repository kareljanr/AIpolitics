# -*- coding: utf-8 -*-
"""Tick 1339 — WV Zorgbedrijf Brasschaat leftover zorg residual, JR2025 BBC euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10 (next every-10 is 1340).
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1339"
UTC = "2026-08-18T01:20:00Z"
ENT = "zorg_zbb"
HIER = "Vlaanderen>Antwerpen>Brasschaat>Zorg>ZorgbedrijfBrasschaat"
GAP = "gap_zbb_bbr_neg_5_39m_cash_drop_5_68m_ltrecv_17_90m_l5"
SRC = "src_zbb_jr2025_pdf"
SRC2 = "src_zbb_docs"
SRC3 = "src_kbo_zbb_0647949706"
SRC4 = "src_zbb_foi_contact"
SRC_URL = "https://www.brasschaat.be/sites/brasschaat/files/documenten/ZBB_Jaarrekening_2025_v20260602.pdf"
SRC2_URL = "https://www.brasschaat.be/besturen-en-samenwerken/beleidsdocumenten/meerjarenplan-en-jaarrekening-zorgbedrijf-brasschaat"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0647949706"
SRC4_URL = "https://www.brasschaat.be/besturen-en-samenwerken/openbaarheid-van-bestuur"
FOI_EMAIL = "info@brasschaat.be"
FOI_POSTAL = "Prins Kavellei 75 2930 Brasschaat"
DRAFT = "docs/doge/foi/drafts/gap_zbb_bbr_neg_5_39m_cash_drop_5_68m_ltrecv_17_90m_l5.md"


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
                "title": "WV Zorgbedrijf Brasschaat jaarrekening 2025 BBC (official PDF; J1-J5 / T2-T5)",
                "url": SRC_URL,
                "publisher": "Zorgbedrijf Brasschaat / Gemeente Brasschaat",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1339; official BBC PDF 1.13MB 36p; publicatie 30.06.2026; "
                    "print schemas J1-J5 T2-T5; leftover zorg of mined Brasschaat city+AGB"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Brasschaat beleidsdocumenten Zorgbedrijf (JR2025 listed 30.06.2026)",
                "url": SRC2_URL,
                "publisher": "Gemeente Brasschaat",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1339; HTTP 200 now lists Jaarrekening 2025 (pub 30.06.2026) + JR2024 + MJP; "
                    "prior tick still JR2024-only; leftover zorg of mined Brasschaat"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Zorgbedrijf Brasschaat 0647.949.706",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1339; KBO 0647.949.706 Actief / normale toestand since 01.04.2016; "
                    "statutaire naam Zorgbedrijf Brasschaat; Vereniging van OCMW's; "
                    "zetel Prins Kavellei 75 2930 Brasschaat since 01.04.2016; "
                    "1 VE; RSZ-werkgever since 01.01.2022; btw since 01.07.2016; "
                    "bestuurder Erwin Callens since 01.04.2016; dagelijks bestuur Dirk Bervoets since 17.02.2024; "
                    "tel 03/650 25 87; no KBO e-mail/web; "
                    "NACE BTW2025 87.101/56.220; RSZ2025 87.101; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Brasschaat openbaarheid van bestuur (FOI channel)",
                "url": SRC4_URL,
                "publisher": "Gemeente Brasschaat",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1339; official FOI info@brasschaat.be / secretariaat@brasschaat.be; "
                    "gemeentehuis Verhoevenlei 11 2930 Brasschaat; ZBB zetel Prins Kavellei 75; "
                    "KBO 0647.949.706; tel ZBB 03/650 25 87 / gemeente 03 650 29 30"
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
                "name_nl": "Zorgbedrijf Brasschaat (vereniging van OCMW's)",
                "name_fr": "Zorgbedrijf Brasschaat (association de CPAS)",
                "name_en": "Zorgbedrijf Brasschaat (OCMW association)",
                "level": "ocmw_association",
                "parent_id": "city_brasschaat",
                "community_language": "nl",
                "website": "https://www.brasschaat.be/besturen-en-samenwerken/beleidsdocumenten/meerjarenplan-en-jaarrekening-zorgbedrijf-brasschaat",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1339 leftover zorg residual of mined Brasschaat city stub + AGB tick1179; "
                    "KBO 0647.949.706 Actief since 01.04.2016; official BBC JR2025 PDF downloads; "
                    "assets 28.938m cash 2.655m DROP BBR -5.388m LT-recv-due 17.900m VTE 102.04; "
                    "FOI ready BBR/cash/LT-recv/dual-OCMW/NBB; not every-10"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_zbb_assets_2025", "2025", "28937874", "2025 assets 28937874 was 29738266; tick1339; primary BBC J4"),
        ("bud_zbb_cash_2025", "2025", "2654671", "2025 cash 2654671 DROP vs 8332781; tick1339; primary BBC J4"),
        ("bud_zbb_st_recv_2025", "2025", "1865034", "2025 ST recv 1865034 (ruil 1547667 + niet-ruil 317367); tick1339; primary BBC J4"),
        ("bud_zbb_st_recv_ruil_2025", "2025", "1547667", "2025 ST recv ruil 1547667 vs 1631395; FOI counterparties; tick1339; primary BBC J4"),
        ("bud_zbb_lt_recv_due_2025", "2025", "17900000", "2025 LT recv due within year 17900000 JUMP vs 5012000; Vesalius/AZ Klina FOI; tick1339; primary BBC J4"),
        ("bud_zbb_fixed_2025", "2025", "6517864", "2025 fixed 6517864 (FVA 17206 + MVA 6500658 + IVA 0); tick1339; primary BBC J4"),
        ("bud_zbb_fva_2025", "2025", "17206", "2025 FVA 17206 other (EVA 0 + IGS 0); tick1339; primary BBC J4"),
        ("bud_zbb_mva_2025", "2025", "6500658", "2025 MVA 6500658 JUMP vs 750276; buildings 6274384; tick1339; primary BBC J4"),
        ("bud_zbb_lease_2025", "2025", "0", "2025 MVA leasing 0; tick1339; primary BBC J4"),
        ("bud_zbb_debt_2025", "2025", "3274749", "2025 schulden 3274749 (ST 3271599 + LT 3150); tick1339; primary BBC J4"),
        ("bud_zbb_st_debt_2025", "2025", "3271599", "2025 ST 3271599 (voorz 803319 + non-fin ruil 2400108 + niet-ruil 68173); tick1339; primary BBC J4"),
        ("bud_zbb_fin_debt_2025", "2025", "0", "2025 fin debt T4 0 (early repay 28310 + periodic 4055); tick1339; primary BBC T4"),
        ("bud_zbb_equity_2025", "2025", "25663125", "2025 nettoactief 25663125 was 25179000; tick1339; primary BBC J4"),
        ("bud_zbb_cum_surplus_2025", "2025", "16351401", "2025 cum surplus 16351401 was 15867276; tick1339; primary BBC J4"),
        ("bud_zbb_other_equity_2025", "2025", "9311724", "2025 overig nettoactief 9311724 unchanged; tick1339; primary BBC J4"),
        ("bud_zbb_expl_in_2025", "2025", "12152635", "2025 expl ontv 12152635; tick1339; primary BBC J2"),
        ("bud_zbb_expl_out_2025", "2025", "11698454", "2025 expl uitg 11698454; tick1339; primary BBC J2"),
        ("bud_zbb_expl_2025", "2025", "454181", "2025 expl saldo +454181; tick1339; primary BBC J2"),
        ("bud_zbb_invest_2025", "2025", "-5809618", "2025 invest saldo -5809618 (uitg 5809618 / ontv 0; Sint-Jozef); tick1339; primary BBC J2"),
        ("bud_zbb_fin_2025", "2025", "-32160", "2025 fin saldo -32160 (uitg 32365 / ontv 205); tick1339; primary BBC J2"),
        ("bud_zbb_bbr_2025", "2025", "-5387598", "2025 BBR year -5387598; tick1339; primary BBC J2"),
        ("bud_zbb_cum_bbr_2025", "2025", "2121453", "YE2025 cum/beschikbaar BBR 2121453 was 7509051; tick1339; primary BBC J2"),
        ("bud_zbb_afm_2025", "2025", "450126", "2025 AFM +450126; tick1339; primary BBC J2"),
        ("bud_zbb_gecorr_afm_2025", "2025", "451592", "2025 gecorr AFM +451592; tick1339; primary BBC J2"),
        ("bud_zbb_pnl_2025", "2025", "484125", "2025 PnL +484125 (ops +346625 / fin +137500); tick1339; primary BBC J5"),
        ("bud_zbb_pers_2025", "2025", "8913182", "2025 J5 pers 8913182 (T2 8837949); VTE 102.04; tick1339; primary BBC"),
        ("bud_zbb_vte_2025", "2025", "102.04", "2025 VTE 102.04 (contr 79.99 + stat 22.05; was 98.23); tick1339; primary BBC T personnel"),
        ("bud_zbb_goods_2025", "2025", "2793814", "2025 J5 goederen/diensten 2793814 (T2 2792944); tick1339; primary BBC J5/T2"),
        ("bud_zbb_werksub_j5_2025", "2025", "1840352", "2025 J5 werksub ontv 1840352 all spec; granted 0; tick1339; primary BBC J5"),
        ("bud_zbb_werksub_t2_2025", "2025", "2778380", "2025 T2 spec werksub 2778380 (VL 2041385 + OCMW 736995); J5-T2 gap 938028 FOI; tick1339; primary BBC T2"),
        ("bud_zbb_werksub_vl_2025", "2025", "2041385", "2025 T2 spec werksub VL 2041385; tick1339; primary BBC T2"),
        ("bud_zbb_werksub_ocmw_2025", "2025", "736995", "2025 T2 spec werksub OCMW 736995 (meerkost 315393 + resp 421602); tick1339; primary BBC T2/narrative"),
        ("bud_zbb_ocmw_beleid_2025", "2025", "1104752", "2025 OCMW beleidskosten 1104752 (meerkost 315393 + resp 421602 + korting 367757 ten laste ZBB); tick1339; primary BBC narrative"),
        ("bud_zbb_ops_rev_2025", "2025", "9176475", "2025 J5 opbrengsten uit de werking 9176475; tick1339; primary BBC J5"),
        ("bud_zbb_other_ops_2025", "2025", "67113", "2025 J5 andere operationele opbrengsten 67113; tick1339; primary BBC J5"),
        ("bud_zbb_early_repay_2025", "2025", "28310", "2025 T2/T4 niet-periodieke aflossing 28310; tick1339; primary BBC T2/T4"),
    ]
    n = append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": bid,
                "entity_id": ENT,
                "year": year,
                "amount_eur": amt,
                "amount_min_eur": "",
                "amount_max_eur": "",
                "basis": "executed",
                "source_id": SRC,
                "confidence": "strong",
                "notes": notes,
            }
            for bid, year, amt, notes in budget_rows
        ],
    )
    print("budgets", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_zbb_jr2025_bbr_cash",
                "title": "WV Zorgbedrijf Brasschaat JR2025 leftover zorg dual (BBR -5.39m / cash drop 5.68m / LT-recv 17.90m / OCMW dual)",
                "entity_id": ENT,
                "beneficiary": "Zorgbedrijf Brasschaat / WZC+dagzorg / OCMW Brasschaat-cliënten",
                "legal_basis": "Decreet lokaal bestuur welzijnsvereniging; BBC; Bestuursdecreet openbaarheid",
                "decision_date": "2016-04-01",
                "start_year": "2016",
                "end_year": "2025",
                "total_envelope_eur": "28937874",
                "cash_by_year": "",
                "remaining_eur": "2121453",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover zorg map VL Brasschaat — WZC/dagzorg; dual OCMW/Vesalius/NBB missing",
                "cut_option": "Publish BBR/cash/17.9m recv recon + J5-T2 werksub gap + per-OCMW dotatie + NBB; do not recreate parallel zorg-shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1339; assets 28937874 cash 2654671 BBR -5387598 AFM +450126 LT-recv-due 17900000 VTE 102.04; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_zbb_bbr_neg_5_39m_cash_drop_5_68m_ltrecv_17_90m",
                "name": "WV Zorgbedrijf Brasschaat JR2025 leftover zorg: BBR -5.39m / cash drop 5.68m / LT-recv-due 17.90m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "11698454",
                "total_cost_eur": "28937874",
                "tco_notes": "Leftover dual zorg of mined Brasschaat: assets 28.9m / cash drop 5.68m / BBR -5.39m vs AFM +0.45m / LT-recv-due 17.90m Vesalius / pers 8.91m VTE 102; do not treat 28.9m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Zorgbedrijf Brasschaat / WZC+dagzorg / OCMW Brasschaat-cliënten",
                "stated_goal": "Local leftover zorg map VL Brasschaat — BBC PDF live; dual OCMW/Vesalius/NBB FOI",
                "measured_outcome": "Official BBC PDF 2026-08-17: BBR -5.39m / AFM +0.45m / PnL +0.48m; cash 2.65m DROP; fin debt 0; LT-recv-due 17.90m; VTE 102.04",
                "absurdity_score": "6.2",
                "cost_score": "6.8",
                "difficulty": "3.0",
                "priority_index": "6.4",
                "cut_proposal": "Publish BBR/cash recon + 17.9m Vesalius qualify + J5-T2 werksub gap 0.94m + OCMW dual 0.74m/1.10m + NBB; do not recreate parallel zorg-shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1339; leftover zorg of mined Brasschaat; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "Recon PnL +484125 vs AFM +450126 vs gecorr AFM +451592 vs BBR -5387598 "
                    "(invest -5809618 / fin -32160) + destination of cash drop 5678110 "
                    "(8332781 to 2654671) vs invest 5809618 Sint-Jozef + cum BBR 2121453 + "
                    "counterparties/age of LT recv due 17900000 (was ST-due 5012000 + LT "
                    "13912675 = 18924675) vs Vesalius sale AZ Klina 26.04.2022 jointly "
                    "managed with OCMW/city + J5 werksub 1840352 vs T2 2778380 (gap 938028; "
                    "VL 2041385 + OCMW 736995) vs narrative beleidskosten 1104752 "
                    "(meerkost 315393 + resp 421602 + korting 367757 ten laste ZBB) + "
                    "VTE 102.04 behind pers J5 8913182 / T2 8837949 + T5 2025 MVA mutatiestaat "
                    "to 6500658 (published T5 still closes 750276) + externe exploitant "
                    "action + NBB WVV filing PDF or non-filing rechtsgrond + AV 29.06.2026."
                ),
                "why_it_matters": (
                    "Named leftover unmined zorg of already-mined Brasschaat city stub + "
                    "AGB tick1179 after honest residual dual hunt. KBO 0647.949.706 Actief. "
                    "Official BBC PDF now downloads (1.13MB 36p; last tick still JR2024-only). "
                    "28.9m leftover WZC/dagzorg shell with BBR -5.39m vs AFM +0.45m, cash "
                    "drop 5.68m and 17.90m LT-recv-due (Vesalius). APB POA/TPA/De Schorre/"
                    "Warande/De Nekker/PIH/Inovant/Atlas 403 / Foleon leftover slugs 404 or "
                    "redirect Hooibeekhoeve — not taken. Leftover cities still no fetchable "
                    "JR2025. Welzijnskoepel jaarverslag 2025 glossy-only — not mined as BBC. "
                    "Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "Zorgbedrijf Brasschaat / Lokaal bestuur Brasschaat",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_zbb_jr2025_bbr_cash",
                "linked_leaderboard_id": "lb_zbb_bbr_neg_5_39m_cash_drop_5_68m_ltrecv_17_90m",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; sourced euros from primary BBC; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1339",
        "title": "WV Zorgbedrijf Brasschaat JR2025 leftover zorg dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: WV Zorgbedrijf Brasschaat leftover zorg of mined Brasschaat "
            "after honest hunt; KBO 0647.949.706 Actief; live JR2025 BBC PDF "
            "(official 1.13MB 36p J1-J5/T2-T5; last tick still JR2024-only); "
            "sourced euros assets 28.938m / cash 2.655m DROP / BBR -5.388m / "
            "LT-recv-due 17.900m / VTE 102.04; FOI ready BBR/cash/LT-recv/dual-OCMW/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T00:45:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1339 WV Zorgbedrijf Brasschaat leftover zorg residual; KBO 0647.949.706; "
            "live BBC PDF; sourced euros; FOI ready not sent; next rq_1340 every-10 + residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1340",
        "title": "Continuous FOI-adjacent public hole-fill batch + every-10 progress",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "EVERY-10 first: refresh progress_every_10_ticks.md + doge_waste_top10_current.md. "
            "THEN residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1339 done including WV Zorgbedrijf Brasschaat 1339 leftover zorg live BBC / "
            "WV Zorgband 1338 leftover zorg live BBC / "
            "WV Sleutelzorg 1337 leftover zorg FOI-unpublished / "
            "WV Weldenderend 1336 leftover zorg live BBC / "
            "WV BVK 1335 leftover zorg live BBC / "
            "WV OPcura 1334 leftover zorg live BBC / "
            "WV Het Dak 1333 leftover zorg live BBC / EVA Inagro 1332 FOI-unpublished / "
            "APB Vormingscentrum Malle 1331 FOI-glossy-not-BBC / "
            "EVA Kinderopvang Dilbeek 1330 FOI-unpublished + every-10 / "
            "Zorg Houthalen 1329 FOI-unpublished / APB Zilvermeer 1328 FOI-unpublished / "
            "APB Vlabinvest 1327 FOI-unpublished / APB Monumentenwacht WVL 1326 FOI-unpublished / "
            "APB Vonk 1325 leftover other-province APB / APB Campus Vesta 1324 FOI-glossy-not-BBC / "
            "AGB Blankenberge 1323 FOI-liquidated JR2019-only / EVA Proefbedrijf Pluimveehouderij 1322 leftover sister EVA / "
            "APB Hooibeekhoeve 1321 leftover sister APB / APB KampC 1320 leftover sister APB + every-10); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "Welzijnskoepel West-Brabant jaarverslag 2025 glossy-only — take only if a BBC PDF now downloads; "
            "Ter Nethe official still JR2024-only — take only if a PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / "
            "APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / APB Campus Vesta 1324 / AGB Blankenberge 1323 / "
            "EVA Proefbedrijf Pluimveehouderij 1322 / APB Hooibeekhoeve 1321 / APB KampC 1320 / "
            "APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 / "
            "AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 / Westtoer; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 (Foleon leftover slugs 404/redirect Hooibeekhoeve); every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1339 after WV Zorgbedrijf Brasschaat leftover zorg live BBC; next every-10 + residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1339", rq_new, rq_spawn)
    print("research_queue 1339", found, "spawned_1340", spawned)

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
                "last_unit_id": "rq_1339",
                "ticks_completed": "1339",
                "paused": "no",
                "notes": (
                    "tick1339 WV Zorgbedrijf Brasschaat leftover zorg residual; KBO 0647.949.706; "
                    "live JR2025 BBC PDF; sourced euros assets 28.938m cash 2.655m BBR -5.388m LT-recv 17.900m; "
                    "FOI ready; next rq_1340 every-10 + residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1339 - 2026-08-18 - rq_1339 WV Zorgbedrijf Brasschaat dual residual leftover zorg
- Unit: Zorgbedrijf Brasschaat (Vereniging van OCMW's) leftover zorg of already-mined Brasschaat (city stub + AGB tick1179) after residual dual hunt (KBO **0647.949.706**; official beleidsdocumenten + live BBC PDF 1.13MB 36p / J1–J5 T2–T5; publicatie **30.06.2026**; AV vaststelling **29.06.2026**). PREFER leftover AGB/zorg/EVA/IGS/other-province APB with a live JR2025 BBC/NBB PDF: first leftover zorg whose official page now yields a downloadable BBC PDF (last tick still listed Zorgbedrijf Brasschaat as JR2024-only; same city-portal pattern as Het Dak/BVK knokke-heist.be, OPcura opwijk.be, Weldenderend berlare.be, Zorgband zorgband.be). Distinct from already-mined AGB Brasschaat 1179 / city Brasschaat stub / Zorgbedrijf Antwerpen 1246 / WV Zorgband 1338 / Sleutelzorg 1337 / Weldenderend 1336 / BVK 1335 / OPcura 1334 / Het Dak 1333 / Zorg Houthalen 1329 / Klein-Brabant 1143. KBO Actief / normale toestand since **01.04.2016**; statutaire naam Zorgbedrijf Brasschaat; zetel Prins Kavellei 75 2930 Brasschaat; **1 VE**; RSZ-werkgever since 01.01.2022; btw since 01.07.2016; bestuurder/voorzitter Erwin Callens since 01.04.2016; dagelijks bestuur Dirk Bervoets since 17.02.2024; FD Carl Oorts; tel 03/650 25 87; no KBO e-mail; NACE 87.101 / 56.220. Hunt leftover AGB first: AGB Bornem official still JR2024-only; AGB De Kluize unpublished; AGB Lebbeke ontbonden 01.01.2023 / last JR2022. Ter Nethe official still JR2024-only; Welzijnskoepel West-Brabant jaarverslag 2025 glossy 3.27MB / 15p (uitgaven 9.76m / deelgenoot-bijdragen 1.59m) **not** BBC J1–J5 — not mined as BBC. Leftover cities Londerzeel official still JR2022–2024 only / Wortegem-Petegem official JR2020–2024 only / Zwalm `/jaarrekening` 404 / Holsbeek 404 / Maarkedal TLS / Linkebeek 404 / Kapellen city GE 404 / Drogenbos 404 / Boutersem archive-only / Maaseik city GE 404 / Bierbeek 404 still no fetchable JR2025. APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas official pages 403 / Foleon leftover slugs 404 or redirect already-mined Hooibeekhoeve — not taken. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / Vlabinvest 1327 / Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320. Not an every-10 tick.
- EUR strong (primary BBC J2/J4/J5/T2/T4): assets **28.937.874** (was 29.738.266); cash **2.654.671** DROP vs 8.332.781; ST recv **1.865.034** (ruil **1.547.667** + niet-ruil **317.367**); LT recv due **17.900.000** JUMP vs 5.012.000 (LT recv **0** was 13.912.675); voorraden **0**; fixed **6.517.864**; FVA **17.206** other (EVA **0** + IGS **0**); MVA **6.500.658** JUMP vs 750.276 (gebouwen **6.274.384**); leasing **0**; IVA **0**; schulden **3.274.749**; ST **3.271.599** (voorzieningen **803.319** + non-fin ruil **2.400.108** + niet-ruil **68.173**); LT **3.150**; fin debt T4 **0** (early repay **28.310** + periodic **4.055**); equity **25.663.125**; cum surplus **16.351.401**; cap-subs **0**; overig nettoactief **9.311.724**; expl **+454.181** (ontv **12.152.635** / uitg **11.698.454**); invest **−5.809.618** (Sint-Jozef nieuwbouw + WZC-uitrusting); fin **−32.160**; BBR year **−5.387.598**; cum BBR **2.121.453** (was 7.509.051); AFM **+450.126**; gecorr AFM **+451.592**; PnL **+484.125** (ops **+346.625** / fin **+137.500**); pers J5 **8.913.182** / T2 **8.837.949**; VTE **102,04** (contr **79,99** + stat **22,05**; was 98,23); werksub granted **0**; werksub received J5 **1.840.352** vs T2 **2.778.380** (gap **938.028**; VL **2.041.385** + OCMW **736.995**); OCMW beleidskosten **1.104.752** (meerkost **315.393** + responsabilisering **421.602** + korting **367.757** ten laste ZBB); ops rev **9.176.475**; other ops **67.113**; goederen J5 **2.793.814**.
- CSVs: sources+4/entities+1/budgets+36/commitments+1/leaderboard+1 + FOI ready `gap_zbb_bbr_neg_5_39m_cash_drop_5_68m_ltrecv_17_90m_l5` (not sent); rq_1339=done; spawn rq_1340; ticks=1339. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (WV Zorgbedrijf Brasschaat leftover zorg live BBC). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1340 EVERY-10 + residual dual L5 VL JR2025 hole_fill (refresh progress_every_10_ticks.md + doge_waste_top10_current.md first; then prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1339 write done")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Tick 1338 — WV Zorgband Leie en Schelde leftover zorg residual, JR2025 BBC euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10.
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1338"
UTC = "2026-08-18T00:45:00Z"
ENT = "zorg_zbls"
HIER = "Vlaanderen>OostVlaanderen>MerelbekeMelle>Zorg>Zorgband"
GAP = "gap_zbls_pnl_neg_5_83m_afm_neg_0_36m_lease_43_75m_l5"
SRC = "src_zbls_jr2025_pdf"
SRC2 = "src_zbls_docs"
SRC3 = "src_kbo_zbls_0698817989"
SRC4 = "src_zbls_foi_contact"
SRC_URL = "https://www.zorgband.be/sites/default/files/2026-06/DEF_JR%202025%20-%20bundel.pdf"
SRC2_URL = "https://www.zorgband.be/over-ons/beleidsdocumenten"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0698817989"
SRC4_URL = "https://www.zorgband.be/contact"
FOI_EMAIL = "info@zorgband.be"
FOI_POSTAL = "Salisburylaan 100 9820 Merelbeke-Melle"
DRAFT = "docs/doge/foi/drafts/gap_zbls_pnl_neg_5_83m_afm_neg_0_36m_lease_43_75m_l5.md"


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
                "title": "WV Zorgband Leie en Schelde jaarrekening 2025 BBC (official PDF; J1-J5 / T2-T5)",
                "url": SRC_URL,
                "publisher": "Zorgband Leie en Schelde",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1338; official BBC PDF 9.13MB 375p; publicatie 12.06.2026; "
                    "print schemas J1-J5 T2-T5; leftover zorg of mined Merelbeke-Melle"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Zorgband beleidsdocumenten (JR2025 listed 12.06.2026)",
                "url": SRC2_URL,
                "publisher": "Zorgband Leie en Schelde",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1338; HTTP 200 now lists Jaarrekening 2025 (pub 12.06.2026) + JR2024 + MJP 2026-2031; "
                    "prior tick still JR2024-only; leftover zorg of mined Merelbeke-Melle"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Zorgband Leie en Schelde 0698.817.989",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1338; KBO 0698.817.989 Actief / normale toestand since 27.11.2017; "
                    "statutaire naam Zorgband Leie en Schelde, OCMW-vereniging van publiekrecht; "
                    "Vereniging van OCMW's; zetel Salisburylaan 100 9820 Merelbeke-Melle since 01.01.2025; "
                    "23 VE; RSZ-werkgever since 01.01.2022; btw since 01.01.2025; "
                    "aanbestedende overheid since 26.06.2018; algemeen lasthebber Githa Praet since 16.02.2024; "
                    "bestuurder Luc Van Huffel since 24.02.2025; tel 09/272 20 00; no KBO e-mail; "
                    "NACE BTW2025 88.102/87.101/86.103/88.101/87.302/84.120; RSZ2025 87.101; databank 17.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Zorgband contact (FOI channel)",
                "url": SRC4_URL,
                "publisher": "Zorgband Leie en Schelde",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1338; official contact info@zorgband.be; tel +32 9 272 20 00; "
                    "zetel Salisburylaan 100 9820 Merelbeke-Melle; KBO 0698.817.989; "
                    "FOI via info@zorgband.be / info@merelbeke-melle.be"
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
                "name_nl": "Zorgband Leie en Schelde (OCMW-vereniging van publiekrecht)",
                "name_fr": "Zorgband Leie et Escaut (association de CPAS de droit public)",
                "name_en": "Zorgband Leie and Scheldt (public-law OCMW association)",
                "level": "ocmw_association",
                "parent_id": "city_merelbeke_melle",
                "community_language": "nl",
                "website": "https://www.zorgband.be",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1338 leftover zorg residual of mined Merelbeke-Melle city GE + AGB; "
                    "KBO 0698.817.989 Actief since 27.11.2017; official BBC JR2025 PDF downloads; "
                    "assets 61.865m cash 1.690m PnL -5.829m AFM -0.356m lease MVA 43.752m VTE 770.30; "
                    "FOI ready PnL/AFM/lease/dual-OCMW/NBB; not every-10"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_zbls_assets_2025", "2025", "61864567", "2025 assets 61864567 was 63217370; tick1338; primary BBC J4"),
        ("bud_zbls_cash_2025", "2025", "1689510", "2025 cash 1689510 DROP vs 2615177; tick1338; primary BBC J4"),
        ("bud_zbls_st_recv_2025", "2025", "7884494", "2025 ST recv 7884494 (ruil 6193417 + niet-ruil 1691077); tick1338; primary BBC J4"),
        ("bud_zbls_st_recv_ruil_2025", "2025", "6193417", "2025 ST recv ruil 6193417 JUMP vs 4489710; FOI counterparties; tick1338; primary BBC J4"),
        ("bud_zbls_fixed_2025", "2025", "52290564", "2025 fixed 52290564 (FVA 8750 + MVA 52193238 + IVA 88576); tick1338; primary BBC J4"),
        ("bud_zbls_fva_2025", "2025", "8750", "2025 FVA 8750 all IGS (EVA 0); tick1338; primary BBC J4"),
        ("bud_zbls_mva_2025", "2025", "52193238", "2025 MVA 52193238 was 53420583; tick1338; primary BBC J4"),
        ("bud_zbls_lease_2025", "2025", "43751520", "2025 MVA leasing 43751520 vs T4 fin debt 2879677; FOI qualify; tick1338; primary BBC J4"),
        ("bud_zbls_iva_2025", "2025", "88576", "2025 IVA 88576 was 78239; tick1338; primary BBC J4"),
        ("bud_zbls_debt_2025", "2025", "16098339", "2025 schulden 16098339 (ST 11729645 + LT 4368694); tick1338; primary BBC J4"),
        ("bud_zbls_st_debt_2025", "2025", "11729645", "2025 ST 11729645 (voorz 3276040 + non-fin ruil 7137310 + niet-ruil 853183 + ST due 463113); tick1338; primary BBC J4"),
        ("bud_zbls_fin_debt_2025", "2025", "2879677", "2025 fin debt T4 2879677 (LT 2416565 + ST due 463113); new loans 187735; tick1338; primary BBC T4"),
        ("bud_zbls_equity_2025", "2025", "45766228", "2025 nettoactief 45766228 was 48373463; tick1338; primary BBC J4"),
        ("bud_zbls_cum_surplus_2025", "2025", "-18054961", "2025 cum surplus -18054961 was -14697672; tick1338; primary BBC J4"),
        ("bud_zbls_capsub_2025", "2025", "5335657", "2025 kapitaalssubsidies 5335657 was 5317094; tick1338; primary BBC J4"),
        ("bud_zbls_other_equity_2025", "2025", "58485531", "2025 overig nettoactief 58485531 was 57754041; tick1338; primary BBC J4"),
        ("bud_zbls_expl_in_2025", "2025", "75908057", "2025 expl ontv 75908057; tick1338; primary BBC J2"),
        ("bud_zbls_expl_out_2025", "2025", "75813812", "2025 expl uitg 75813812; tick1338; primary BBC J2"),
        ("bud_zbls_expl_2025", "2025", "94244", "2025 expl saldo +94244; tick1338; primary BBC J2"),
        ("bud_zbls_invest_2025", "2025", "-776427", "2025 invest saldo -776427 (uitg 1563790 / ontv 787363); tick1338; primary BBC J2"),
        ("bud_zbls_fin_2025", "2025", "-310027", "2025 fin saldo -310027 (uitg 449892 / ontv 139865); tick1338; primary BBC J2"),
        ("bud_zbls_bbr_2025", "2025", "-992210", "2025 BBR year -992210; tick1338; primary BBC J2"),
        ("bud_zbls_cum_bbr_2025", "2025", "1583511", "YE2025 cum/beschikbaar BBR 1583511 was 2575721; tick1338; primary BBC J2"),
        ("bud_zbls_afm_2025", "2025", "-355648", "2025 AFM -355648; tick1338; primary BBC J2"),
        ("bud_zbls_gecorr_afm_2025", "2025", "-157102", "2025 gecorr AFM -157102; tick1338; primary BBC J2"),
        ("bud_zbls_pnl_2025", "2025", "-5829218", "2025 PnL -5829218 (ops -6570844 / fin +741627); tick1338; primary BBC J5"),
        ("bud_zbls_pers_2025", "2025", "53163724", "2025 J5/T2 pers 53163724 (niet-vast 50973879 + andere 2189844); VTE 770.30; tick1338; primary BBC"),
        ("bud_zbls_vte_2025", "2025", "770.30", "2025 VTE 770.30 / 1265 koppen (was 641.42 / 1070); Lochristi instap; tick1338; primary BBC narrative"),
        ("bud_zbls_goods_2025", "2025", "20765510", "2025 J5=T2 goederen/diensten 20765510; tick1338; primary BBC J5/T2"),
        ("bud_zbls_werksub_in_2025", "2025", "17336409", "2025 J5=T2 werksub ontv 17336409 all spec; granted 0; tick1338; primary BBC J5/T2"),
        ("bud_zbls_werksub_vl_2025", "2025", "13584576", "2025 T2 spec werksub VL 13584576; tick1338; primary BBC T2"),
        ("bud_zbls_werksub_fed_2025", "2025", "3636645", "2025 T2 spec werksub fed 3636645; tick1338; primary BBC T2"),
        ("bud_zbls_tussenkomst_2025", "2025", "4271257", "2025 J5/T2 tussenkomst derden 4271257 vs narrative 4053126; dual OCMW FOI; tick1338; primary BBC J5/T2"),
        ("bud_zbls_ops_rev_2025", "2025", "53164768", "2025 J5 opbrengsten uit de werking 53164768; tick1338; primary BBC J5"),
        ("bud_zbls_other_ops_2025", "2025", "1107037", "2025 J5 andere operationele opbrengsten 1107037; tick1338; primary BBC J5"),
        ("bud_zbls_new_loans_2025", "2025", "187735", "2025 T4 nieuwe leningen 187735; tick1338; primary BBC T4"),
        ("bud_zbls_members_2025", "2025", "6", "2025 deelgenoten 6 (Merelbeke-Melle Destelbergen Laarne Nazareth-De Pinte Lochristi Oosterzele); tick1338; primary BBC/bestuur"),
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
                "commitment_id": "comm_zbls_jr2025_pnl_lease",
                "title": "WV Zorgband Leie en Schelde JR2025 leftover zorg dual (PnL -5.83m / AFM -0.36m / lease 43.75m / 6 OCMW)",
                "entity_id": ENT,
                "beneficiary": "Zorgband / WZC+thuiszorg+revalidatie / OCMW-cliënten 6 gemeenten",
                "legal_basis": "Decreet lokaal bestuur welzijnsvereniging; BBC; Bestuursdecreet openbaarheid",
                "decision_date": "2017-11-27",
                "start_year": "2017",
                "end_year": "2025",
                "total_envelope_eur": "61864567",
                "cash_by_year": "",
                "remaining_eur": "1583511",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover zorg map VL Merelbeke-Melle — WZC/thuiszorg/revalidatie; dual OCMW/lease/NBB missing",
                "cut_option": "Publish PnL/AFM recon + lease vs T4 + per-OCMW tussenkomst + NBB; do not recreate parallel zorg-shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1338; assets 61864567 cash 1689510 PnL -5829218 AFM -355648 lease 43751520 VTE 770.30; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_zbls_pnl_neg_5_83m_lease_43_75m_afm_neg_0_36m",
                "name": "WV Zorgband JR2025 leftover zorg: PnL -5.83m / AFM -0.36m / lease MVA 43.75m vs T4 debt 2.88m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "75813812",
                "total_cost_eur": "61864567",
                "tco_notes": "Leftover dual zorg of mined Merelbeke-Melle: assets 61.9m / cash drop 0.93m / PnL -5.83m vs AFM -0.36m / lease MVA 43.75m vs T4 2.88m / pers 53.2m VTE 770; do not treat 61.9m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Zorgband / WZC+thuiszorg+revalidatie / OCMW-cliënten 6 gemeenten",
                "stated_goal": "Local leftover zorg map VL Merelbeke-Melle — BBC PDF live; dual OCMW/lease/NBB FOI",
                "measured_outcome": "Official BBC PDF 2026-08-17: BBR -0.99m / AFM -0.36m / PnL -5.83m; cash 1.69m DROP; fin debt 2.88m; lease MVA 43.75m; VTE 770.30",
                "absurdity_score": "6.4",
                "cost_score": "7.2",
                "difficulty": "3.2",
                "priority_index": "6.6",
                "cut_proposal": "Publish PnL/AFM recon + lease vs T4 qualify + per-OCMW tussenkomst 4.27m + NBB; do not recreate parallel 6-OCMW zorg-shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1338; leftover zorg of mined Merelbeke-Melle; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "Recon PnL -5829218 vs AFM -355648 vs gecorr AFM -157102 vs BBR -992210 + "
                    "tussenkomst derden J5/T2 4271257 vs narrative 4053126 + per-OCMW 2025-2026 "
                    "dual lines (Merelbeke-Melle/Destelbergen/Laarne/Nazareth-De Pinte/Lochristi/"
                    "Oosterzele) for spec werksub 17336409 (fed 3636645 + VL 13584576 + prov 31186 "
                    "+ gem 26000 + other 58003) + lease MVA 43751520 vs T4 fin debt 2879677 "
                    "(new loans 187735) + destination of cash drop 925667 (2615177 to 1689510) "
                    "vs cum BBR 1583511 + counterparties/age of ST recv 7884494 (ruil 6193417 "
                    "JUMP) + VTE 770.30 / 1265 koppen (Lochristi instap) behind pers 53163724 + "
                    "NBB WVV filing PDF or non-filing rechtsgrond + AV vaststelling JR2025."
                ),
                "why_it_matters": (
                    "Named leftover unmined zorg of already-mined Merelbeke-Melle city GE + AGB "
                    "tick1171 after honest residual dual hunt. KBO 0698.817.989 Actief. "
                    "Official BBC PDF now downloads (9.13MB 375p; last tick still JR2024-only). "
                    "61.9m leftover 6-OCMW WZC/thuiszorg/revalidatie shell with PnL -5.83m vs "
                    "AFM -0.36m and lease MVA 43.75m vs T4 2.88m. APB POA/TPA/De Schorre/"
                    "Warande/De Nekker/PIH/Inovant/Atlas 403 / Foleon leftover slugs redirect "
                    "Hooibeekhoeve — not taken. Leftover cities still no fetchable JR2025. "
                    "Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "Zorgband Leie en Schelde / Lokaal bestuur Merelbeke-Melle",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_zbls_jr2025_pnl_lease",
                "linked_leaderboard_id": "lb_zbls_pnl_neg_5_83m_lease_43_75m_afm_neg_0_36m",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; sourced euros from primary BBC; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1338",
        "title": "WV Zorgband Leie en Schelde JR2025 leftover zorg dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: WV Zorgband Leie en Schelde leftover zorg of mined Merelbeke-Melle "
            "after honest hunt; KBO 0698.817.989 Actief; live JR2025 BBC PDF "
            "(official 9.13MB 375p J1-J5/T2-T5; last tick still JR2024-only); "
            "sourced euros assets 61.865m / cash 1.690m / PnL -5.829m / AFM -0.356m / "
            "lease 43.752m / VTE 770.30; FOI ready PnL/AFM/lease/dual-OCMW/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T00:10:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1338 WV Zorgband leftover zorg residual; KBO 0698.817.989; "
            "live BBC PDF; sourced euros; FOI ready not sent; next rq_1339 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1339",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1338 done including WV Zorgband 1338 leftover zorg live BBC / "
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
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / "
            "APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / APB Campus Vesta 1324 / AGB Blankenberge 1323 / "
            "EVA Proefbedrijf Pluimveehouderij 1322 / APB Hooibeekhoeve 1321 / APB KampC 1320 / "
            "APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 / "
            "AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 / Westtoer; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 (Foleon leftover slugs redirect Hooibeekhoeve); not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1338 after WV Zorgband leftover zorg live BBC; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1338", rq_new, rq_spawn)
    print("research_queue 1338", found, "spawned_1339", spawned)

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
                "last_unit_id": "rq_1338",
                "ticks_completed": "1338",
                "paused": "no",
                "notes": (
                    "tick1338 WV Zorgband leftover zorg residual; KBO 0698.817.989; "
                    "live JR2025 BBC PDF; sourced euros assets 61.865m cash 1.690m PnL -5.829m AFM -0.356m; "
                    "FOI ready; next rq_1339 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1338 - 2026-08-18 - rq_1338 WV Zorgband Leie en Schelde dual residual leftover zorg
- Unit: Zorgband Leie en Schelde (OCMW-vereniging van publiekrecht) leftover zorg of already-mined Merelbeke-Melle (city GE + AGB tick1171) + Destelbergen / Laarne / Nazareth-De Pinte / Lochristi / Oosterzele after residual dual hunt (KBO **0698.817.989**; official beleidsdocumenten + live BBC PDF 9.13MB 375p / J1–J5 T2–T5; publicatie **12.06.2026**). PREFER leftover AGB/zorg/EVA/IGS/other-province APB with a live JR2025 BBC/NBB PDF: first leftover zorg whose official page now yields a downloadable BBC PDF (last tick still listed Zorgband as JR2024-only). Distinct from already-mined city Merelbeke-Melle / AGB Merelbeke-Melle / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / Zorg Houthalen 1329 / Zorg Leuven 1241 / Dodoens 1245 / Zorgbedrijf Antwerpen 1246 / Klein-Brabant 1143. KBO Actief / normale toestand since **27.11.2017**; statutaire naam Zorgband Leie en Schelde, OCMW-vereniging van publiekrecht; zetel Salisburylaan 100 9820 Merelbeke-Melle since 01.01.2025; **23 VE**; RSZ-werkgever since 01.01.2022; btw since 01.01.2025; aanbestedende overheid since 26.06.2018; algemeen lasthebber Githa Praet since 16.02.2024; bestuurder Luc Van Huffel since 24.02.2025; tel 09/272 20 00; no KBO e-mail; NACE 88.102 / 87.101 / 86.103. 6 OCMW-deelgenoten (Merelbeke-Melle, Destelbergen, Laarne, Nazareth-De Pinte, Lochristi, Oosterzele). Hunt leftover AGB first: AGB Bornem official still JR2024-only; AGB De Kluize unpublished; AGB Lebbeke no JR2025. Ter Nethe official still JR2024-only; Zorgbedrijf Brasschaat official still JR2024-only; Welzijnskoepel West-Brabant no JR2025 BBC. Leftover cities Londerzeel official still JR2022–2024 only / Wortegem-Petegem official JR2020–2024 only / Zwalm `/jaarrekening` 404 / Holsbeek 404 / Maarkedal TLS / Linkebeek 404 / Kapellen city GE 404 / Drogenbos 404 / Boutersem archive-only / Maaseik city GE 404 / Bierbeek 404 still no fetchable JR2025. APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas official pages 403 / Foleon leftover slugs redirect already-mined Hooibeekhoeve — not taken. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / Vlabinvest 1327 / Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320. Not an every-10 tick.
- EUR strong (primary BBC J2/J4/J5/T2/T4): assets **61.864.567** (was 63.217.370); cash **1.689.510** DROP vs 2.615.177; ST recv **7.884.494** (ruil **6.193.417** JUMP + niet-ruil **1.691.077**); voorraden **0**; fixed **52.290.564**; FVA **8.750** all IGS (EVA **0**); MVA **52.193.238** leasing **43.751.520**; IVA **88.576**; schulden **16.098.339**; ST **11.729.645** (voorzieningen **3.276.040** + non-fin ruil **7.137.310** + niet-ruil **853.183** + ST due **463.113**); LT **4.368.694** (fin **2.416.565** + niet-ruil **1.952.129**); fin debt T4 **2.879.677**; new loans **187.735**; equity **45.766.228**; cum surplus **−18.054.961**; cap-subs **5.335.657**; overig nettoactief **58.485.531**; expl **+94.244** (ontv **75.908.057** / uitg **75.813.812**); invest **−776.427**; fin **−310.027**; BBR year **−992.210**; cum BBR **1.583.511**; AFM **−355.648**; gecorr AFM **−157.102**; PnL **−5.829.218** (ops **−6.570.844** / fin **+741.627**); pers J5/T2 **53.163.724**; VTE **770,30** / 1.265 koppen (was 641,42 / 1.070; Lochristi instap); werksub granted **0**; werksub received J5=T2 **17.336.409** (all spec: fed **3.636.645** + VL **13.584.576** + prov **31.186** + gem **26.000** + other **58.003**); tussenkomst derden J5/T2 **4.271.257**; ops rev **53.164.768**; other ops **1.107.037**; goederen J5=T2 **20.765.510**; fin costs **49.259**.
- CSVs: sources+4/entities+1/budgets+37/commitments+1/leaderboard+1 + FOI ready `gap_zbls_pnl_neg_5_83m_afm_neg_0_36m_lease_43_75m_l5` (not sent); rq_1338=done; spawn rq_1339; ticks=1338. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (WV Zorgband leftover zorg live BBC). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1339 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1338 write done")


if __name__ == "__main__":
    main()

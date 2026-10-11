# -*- coding: utf-8 -*-
"""Tick 1336 — WV Weldenderend leftover zorg residual, JR2025 BBC euros.
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

TICK = "1336"
UTC = "2026-08-17T23:40:00Z"
ENT = "zorg_weldenderend"
HIER = "Vlaanderen>OostVlaanderen>Berlare>Zorg>Weldenderend"
GAP = "gap_weld_ocmwsub_0_19m_strecv_8k_art60_l5"
SRC = "src_weld_jr2025_pdf"
SRC2 = "src_weld_docs"
SRC3 = "src_kbo_weld_0677764437"
SRC4 = "src_weld_foi_contact"
SRC_URL = "https://berlare.be/sites/berlare/files/documenten/bestuur_en_beleid_beleidsdocumenten_weldenderend_jaarrekening2025.pdf"
SRC2_URL = "https://berlare.be/bestuur-beleid/welzijnsvereniging-weldenderend"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0677764437"
SRC4_URL = "https://www.slaatjepraatje.be"
FOI_EMAIL = "info@slaatjepraatje.be"
FOI_POSTAL = "Baron Tibbautstraat 29A 9290 Berlare"
DRAFT = "docs/doge/foi/drafts/gap_weld_ocmwsub_0_19m_strecv_8k_art60_l5.md"


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
                "title": "WV Weldenderend jaarrekening 2025 BBC (official PDF; J1-J5 / T2-T5)",
                "url": SRC_URL,
                "publisher": "WV Weldenderend / Gemeente Berlare",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1336; official BBC PDF 1.26MB 41p; goedkeuring AV 17.06.2026; "
                    "print schemas J1-J5 T2-T5; leftover zorg of mined Berlare"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Berlare welzijnsvereniging Weldenderend (JR2025 listed)",
                "url": SRC2_URL,
                "publisher": "Gemeente Berlare",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1336; HTTP 200 lists JR2025 + AV 17.06.2026 besluitenlijst + MJP 2026-2031; "
                    "leftover zorg of already-mined Berlare city GE tick1006"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Vereniging Weldenderend 0677.764.437",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1336; KBO 0677.764.437 Actief / normale toestand since 12.04.2017; "
                    "statutaire naam Vereniging Weldenderend; Vereniging van OCMW's; "
                    "zetel Baron Tibbautstraat 29 bus a 9290 Berlare; 2 VE; "
                    "RSZ-werkgever since 01.01.2022; btw since 02.01.2018; "
                    "algemeen lasthebber Mathieu Renneboog since 01.10.2025; "
                    "bestuurder Marie-Rose Locquet since 01.04.2025; "
                    "KBO e-mail voorzitterBCSD@berlare.be; tel 09/326 97 10; "
                    "NACE BTW2025 47.110 / RSZ2025 88.994; databank 17.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "WV Weldenderend / Slaatje Praatje contact (FOI channel)",
                "url": SRC4_URL,
                "publisher": "WV Weldenderend",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1336; BBC header e-mail info@slaatjepraatje.be; tel 09 337 50 36; "
                    "GSM 0477 53 24 37; zetel Baron Tibbautstraat 29A 9290 Berlare; "
                    "FOI via info@slaatjepraatje.be / voorzitterBCSD@berlare.be / info@berlare.be"
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
                "name_nl": "Welzijnsvereniging Weldenderend (vereniging van OCMW's / Slaatje Praatje)",
                "name_fr": "Association de CPAS Weldenderend (epicerie sociale Slaatje Praatje)",
                "name_en": "Public welfare association Weldenderend (social grocery Slaatje Praatje)",
                "level": "ocmw_association",
                "parent_id": "city_berlare",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1336 leftover zorg residual of mined Berlare city GE; "
                    "KBO 0677.764.437 Actief since 12.04.2017; official BBC JR2025 PDF downloads; "
                    "assets 0.142m cash 0.055m OCMW werksub 0.186m pers 0.167m VTE 2.6; "
                    "FOI ready dual-OCMW/ST-recv/art60/NBB; not every-10"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_weld_assets_2025", "2025", "142356", "2025 assets 142356 was 151482; tick1336; primary BBC J4"),
        ("bud_weld_cash_2025", "2025", "55272", "2025 cash 55272 was 54596; tick1336; primary BBC J4"),
        ("bud_weld_st_recv_2025", "2025", "10657", "2025 ST recv 10657 (ruil 2640 + niet-ruil 8017); tick1336; primary BBC J4"),
        ("bud_weld_st_recv_nietruil_2025", "2025", "8017", "2025 ST recv niet-ruil 8017 unchanged vs 2024; FOI counterparties; tick1336; primary BBC J4"),
        ("bud_weld_stock_2025", "2025", "3000", "2025 voorraden 3000 unchanged; tick1336; primary BBC J4"),
        ("bud_weld_fixed_2025", "2025", "73426", "2025 fixed 73426 (FVA 1250 + MVA 72176 + IVA 0); tick1336; primary BBC J4"),
        ("bud_weld_fva_2025", "2025", "1250", "2025 FVA 1250 all IGS (EVA 0); 5 aandelen Creat-TMVS 25pct; tick1336; primary BBC J4/T5"),
        ("bud_weld_mva_2025", "2025", "72176", "2025 MVA 72176 was 81923 (install 2578 + rollend 69599); tick1336; primary BBC J4"),
        ("bud_weld_debt_2025", "2025", "20370", "2025 schulden 20370 all ST non-fin ruil was 32096; tick1336; primary BBC J4"),
        ("bud_weld_fin_debt_2025", "2025", "0", "2025 fin debt T4 0 (LT 0 + ST 0; no loans); tick1336; primary BBC T4"),
        ("bud_weld_equity_2025", "2025", "121986", "2025 nettoactief 121986 was 119386; tick1336; primary BBC J4"),
        ("bud_weld_cum_surplus_2025", "2025", "69256", "2025 cum surplus 69256 was 66656; tick1336; primary BBC J4"),
        ("bud_weld_other_equity_2025", "2025", "52729", "2025 overig nettoactief 52729 unchanged (kapitaal+inbreng); tick1336; primary BBC J4"),
        ("bud_weld_capital_2025", "2025", "42000", "2025 maatschappelijk kapitaal 42000 (7x6000); tick1336; primary BBC narrative"),
        ("bud_weld_expl_in_2025", "2025", "262217", "2025 expl ontv 262217; tick1336; primary BBC J2"),
        ("bud_weld_expl_out_2025", "2025", "249871", "2025 expl uitg 249871; tick1336; primary BBC J2"),
        ("bud_weld_expl_2025", "2025", "12346", "2025 expl saldo +12346; tick1336; primary BBC J2"),
        ("bud_weld_invest_2025", "2025", "0", "2025 invest saldo 0 (no capex); tick1336; primary BBC J2/T3"),
        ("bud_weld_bbr_2025", "2025", "12346", "2025 BBR year +12346; tick1336; primary BBC J2"),
        ("bud_weld_cum_bbr_2025", "2025", "45559", "YE2025 cum BBR 45559 was 33213; tick1336; primary BBC J2"),
        ("bud_weld_afm_2025", "2025", "12346", "2025 AFM +12346; tick1336; primary BBC J2"),
        ("bud_weld_gecorr_afm_2025", "2025", "12346", "2025 gecorr AFM +12346; tick1336; primary BBC J2"),
        ("bud_weld_pnl_2025", "2025", "2600", "2025 PnL +2600 (ops +2600 / fin 0); tick1336; primary BBC J5"),
        ("bud_weld_pers_2025", "2025", "166936", "2025 J5/T2 pers 166936 (niet-vast 162126 + andere 4810); VTE 2.6; tick1336; primary BBC"),
        ("bud_weld_vte_2025", "2025", "2.6", "2025 VTE 2.6 all contractueel (B 1.1 + C 0.5 + D 1.0); art.60 extra FOI; tick1336; primary BBC personnel table"),
        ("bud_weld_goods_2025", "2025", "82643", "2025 J5=T2 goederen/diensten 82643; tick1336; primary BBC J5/T2"),
        ("bud_weld_werksub_in_2025", "2025", "211554", "2025 J5=T2 werksub ontv 211554 (alg 185500 + spec 26054); tick1336; primary BBC J5/T2"),
        ("bud_weld_werksub_ocmw_2025", "2025", "185500", "2025 T2 alg werksub van het OCMW 185500; dual 7-OCMW FOI; tick1336; primary BBC T2"),
        ("bud_weld_werksub_spec_2025", "2025", "26054", "2025 T2 spec werksub 26054 (fed 17879 + VL 8174); tick1336; primary BBC T2"),
        ("bud_weld_ops_rev_2025", "2025", "49678", "2025 J5 opbrengsten uit de werking 49678; tick1336; primary BBC J5"),
        ("bud_weld_other_ops_2025", "2025", "985", "2025 J5 andere operationele opbrengsten 985; tick1336; primary BBC J5"),
        ("bud_weld_members_2025", "2025", "7", "2025 deelgenoten 7 (Berlare Buggenhout Laarne Waasmunster Wichelen Lebbeke SG-Waas); tick1336; primary BBC narrative"),
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
                "commitment_id": "comm_weld_jr2025_ocmwsub",
                "title": "WV Weldenderend JR2025 leftover zorg dual (OCMW werksub 0.19m / pers 0.17m / 7 OCMW social grocery)",
                "entity_id": ENT,
                "beneficiary": "Weldenderend / Slaatje Praatje / OCMW-cliënten 7 gemeenten",
                "legal_basis": "Decreet lokaal bestuur welzijnsvereniging; BBC; Bestuursdecreet openbaarheid",
                "decision_date": "2017-04-12",
                "start_year": "2017",
                "end_year": "2025",
                "total_envelope_eur": "142356",
                "cash_by_year": "",
                "remaining_eur": "45559",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover zorg map VL Berlare — sociale kruidenier; dual OCMW/art.60/NBB missing",
                "cut_option": "Publish per-OCMW 2025-2026 werksub path + art.60 dual + NBB; do not recreate parallel grocery-shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1336; assets 142356 cash 55272 OCMW werksub 185500 pers 166936 VTE 2.6; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_weld_ocmwsub_0_19m_pers_0_17m",
                "name": "WV Weldenderend JR2025 leftover zorg: OCMW werksub 0.19m / pers 0.17m / 7-OCMW social grocery shell",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "249871",
                "total_cost_eur": "142356",
                "tco_notes": "Leftover dual zorg of mined Berlare: assets 0.14m / cash 0.055m / OCMW werksub 0.19m / pers 0.17m VTE 2.6 + art.60 off-books; BBC itself notes extra WV admin cost vs keeping Slaatje Praatje inside OCMW Berlare; do not treat 0.14m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Weldenderend / Slaatje Praatje / OCMW-cliënten 7 gemeenten",
                "stated_goal": "Local leftover zorg map VL Berlare — BBC PDF live; dual OCMW/art.60/NBB FOI",
                "measured_outcome": "Official BBC PDF 2026-08-17: BBR +0.012m / AFM +0.012m / PnL +0.003m; cash 0.055m; fin debt 0; VTE 2.6; 7 OCMW members",
                "absurdity_score": "5.1",
                "cost_score": "4.2",
                "difficulty": "3.0",
                "priority_index": "4.9",
                "cut_proposal": "Publish per-OCMW dual werksub 0.19m + art.60 path + NBB; do not recreate parallel grocery-shell; BBC itself flags extra WV admin vs OCMW item",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1336; leftover zorg of mined Berlare; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "Per-OCMW 2025-2026 dual lines for alg werksub 185500 (all van het OCMW; "
                    "7 deelgenoten Berlare/Buggenhout/Laarne/Waasmunster/Wichelen/Lebbeke/"
                    "Sint-Gillis-Waas) + spec werksub 26054 (fed 17879 + VL 8174) + "
                    "counterparties/age of ST recv 10657 (niet-ruil 8017 unchanged) + "
                    "ST debt drop 32096 to 20370 + art.60§7 VTE/cost path via OCMW "
                    "Berlare/Laarne/Wichelen behind pers 166936 / VTE 2.6 + "
                    "Creat-TMVS FVA 1250 + Goudberg 20 rent 2024-2026 + NBB WVV "
                    "filing PDF or non-filing rechtsgrond + AV 17.06.2026."
                ),
                "why_it_matters": (
                    "Named leftover unmined zorg of already-mined Berlare city GE tick1006 "
                    "after honest residual dual hunt. KBO 0677.764.437 Actief. "
                    "Official BBC PDF now downloads (1.26MB 41p). 0.14m leftover "
                    "7-OCMW social-grocery shell with OCMW werksub 0.19m. APB "
                    "POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas 403 / "
                    "Foleon leftover slugs redirect Hooibeekhoeve — not taken. "
                    "Leftover cities still no fetchable JR2025. Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "WV Weldenderend / Gemeente Berlare",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_weld_jr2025_ocmwsub",
                "linked_leaderboard_id": "lb_weld_ocmwsub_0_19m_pers_0_17m",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; sourced euros from primary BBC; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1336",
        "title": "WV Weldenderend JR2025 leftover zorg dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: WV Weldenderend leftover zorg of mined Berlare city GE after honest hunt; "
            "KBO 0677.764.437 Actief; live JR2025 BBC PDF (official 1.26MB 41p J1-J5/T2-T5); "
            "sourced euros assets 0.142m / cash 0.055m / OCMW werksub 0.186m / "
            "pers 0.167m VTE 2.6; FOI ready dual-OCMW/ST-recv/art60/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T23:10:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1336 WV Weldenderend leftover zorg residual; KBO 0677.764.437; "
            "live BBC PDF; sourced euros; FOI ready not sent; next rq_1337 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1337",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1336 done including WV Weldenderend 1336 leftover zorg live BBC / "
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
            "skip already-mined WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / "
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
        "notes": "spawned tick1336 after WV Weldenderend leftover zorg live BBC; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1336", rq_new, rq_spawn)
    print("research_queue 1336", found, "spawned_1337", spawned)

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
                "last_unit_id": "rq_1336",
                "ticks_completed": "1336",
                "paused": "no",
                "notes": (
                    "tick1336 WV Weldenderend leftover zorg residual; KBO 0677.764.437; "
                    "live JR2025 BBC PDF; sourced euros assets 0.142m cash 0.055m OCMW werksub 0.186m; "
                    "FOI ready; next rq_1337 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1336 - 2026-08-17 - rq_1336 WV Weldenderend dual residual leftover zorg
- Unit: Welzijnsvereniging Weldenderend (Slaatje Praatje) leftover zorg of already-mined Berlare (city GE tick1006) after residual dual hunt (KBO **0677.764.437**; official Weldenderend page + live BBC PDF 1.26MB 41p / J1–J5 T2–T5; goedkeuring AV **17.06.2026**). PREFER leftover AGB/zorg/EVA/IGS/other-province APB with a live JR2025 BBC/NBB PDF: first leftover zorg whose official page now yields a downloadable BBC PDF (same city-portal pattern as Het Dak/BVK knokke-heist.be and OPcura opwijk.be). Distinct from already-mined city Berlare / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / Zorg Houthalen 1329 / Zilveren Zwaan Heist. KBO Actief / normale toestand since **12.04.2017**; statutaire naam Vereniging Weldenderend; zetel Baron Tibbautstraat 29A 9290 Berlare; **2 VE**; RSZ-werkgever since 01.01.2022; btw since 02.01.2018; algemeen lasthebber Mathieu Renneboog since 01.10.2025; bestuurder/voorzitter Marie-Rose Locquet since 01.04.2025; NACE 47.110 / 88.994. 7 OCMW-deelgenoten (Berlare, Buggenhout, Laarne, Waasmunster, Wichelen, Lebbeke, Sint-Gillis-Waas; Dendermonde left YE2023). Hunt leftover AGB first: AGB Bornem official still JR2024-only; AGB De Kluize unpublished; AGB Pelt already mined. Leftover cities Londerzeel official still JR2022–2024 only / Wortegem-Petegem official JR2020–2024 only / Zwalm `/jaarrekening` 404 / Holsbeek 404 / Maarkedal TLS / Linkebeek 404 / Kapellen city GE 404 / Drogenbos 404 / Boutersem archive-only / Maaseik city GE 404 / Bierbeek 404 still no fetchable JR2025. APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas official pages 403 / Foleon leftover slugs redirect already-mined Hooibeekhoeve — not taken. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / Vlabinvest 1327 / Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320. Not an every-10 tick.
- EUR strong (primary BBC J2/J4/J5/T2/T4/T5): assets **142.356** (was 151.482); cash **55.272** (was 54.596); ST recv **10.657** (ruil **2.640** + niet-ruil **8.017** unchanged); voorraden **3.000**; fixed **73.426**; FVA **1.250** all IGS (Creat-TMVS 5×1.000 25% volstort); MVA **72.176** (was 81.923); IVA **0**; schulden **20.370** all ST non-fin ruil (was 32.096); LT **0**; fin debt T4 **0**; equity **121.986**; cum surplus **69.256**; cap-subs **0**; overig nettoactief **52.729**; kapitaal **42.000** (7×6.000); expl **+12.346** (ontv **262.217** / uitg **249.871**); invest **0**; fin **0**; BBR year **+12.346**; cum BBR **45.559**; AFM/gecorr **+12.346**; PnL **+2.600**; pers J5/T2 **166.936**; VTE **2,6** all contractueel (B **1,1** / C **0,5** / D **1,0**); art.60§7 extra via OCMW Berlare/Laarne/Wichelen; werksub granted **0**; werksub received J5=T2 **211.554** (alg **185.500** all OCMW; spec **26.054** of which fed **17.879** + VL **8.174**); ops rev **49.678**; other ops **985**; goederen J5=T2 **82.643**.
- CSVs: sources+4/entities+1/budgets+32/commitments+1/leaderboard+1 + FOI ready `gap_weld_ocmwsub_0_19m_strecv_8k_art60_l5` (not sent); rq_1336=done; spawn rq_1337; ticks=1336. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (WV Weldenderend leftover zorg live BBC). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1337 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1336 write done")


if __name__ == "__main__":
    main()

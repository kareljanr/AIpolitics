# -*- coding: utf-8 -*-
"""Tick 1333 — WV Het Dak leftover zorg residual, JR2025 BBC euros.
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

TICK = "1333"
UTC = "2026-08-17T22:25:00Z"
ENT = "zorg_het_dak"
HIER = "Vlaanderen>WestVlaanderen>KnokkeHeist>Zorg>HetDak"
GAP = "gap_hetdak_lease_32_29m_findebt_26_37m_cash_14_44m_vte_l5"
SRC = "src_hetdak_jr2025_pdf"
SRC2 = "src_hetdak_docs"
SRC3 = "src_kbo_hetdak_0863329989"
SRC4 = "src_hetdak_foi_contact"
SRC_URL = "https://www.knokke-heist.be/sites/default/files/inline-files/Jaarrekening_Het_Dak_2025%20AV.pdf"
SRC2_URL = "https://www.knokke-heist.be/gemeente-en-bestuur/beleidsrapporten/welzijnsverenigingen"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0863329989"
SRC4_URL = "https://wvhetdak.be/"
FOI_EMAIL = "info@knokke-heist.be"
FOI_POSTAL = "Westkapellestraat 460 8300 Knokke-Heist"
DRAFT = "docs/doge/foi/drafts/gap_hetdak_lease_32_29m_findebt_26_37m_cash_14_44m_vte_l5.md"


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
                "title": "WV Het Dak jaarrekening 2025 BBC (official PDF; J1-J5 / T2-T5)",
                "url": SRC_URL,
                "publisher": "Welzijnsvereniging Het Dak / Gemeente Knokke-Heist",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1333; official BBC PDF 2.64MB; goedkeuring AV 01.06.2026 / "
                    "publicatie 04.06.2026; print schemas J1-J5 T2-T5; leftover zorg of mined Knokke-Heist"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Knokke-Heist welzijnsverenigingen (Het Dak JR2025 listed)",
                "url": SRC2_URL,
                "publisher": "Gemeente Knokke-Heist",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1333; HTTP 200 lists Jaarrekening 2025 Het Dak + MJP 2026-2031; "
                    "FOI channel info@knokke-heist.be"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Welzijnsvereniging 'Het Dak' 0863.329.989",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1333; KBO 0863.329.989 Actief / normale toestand since 01.01.2002; "
                    "statutaire naam Welzijnsvereniging 'Het Dak' since 27.11.2018; "
                    "Vereniging van OCMW's; zetel Westkapellestraat 460 8300 Knokke-Heist "
                    "since 12.12.2023; 3 VE; RSZ-werkgever since 01.01.2022; "
                    "aanbestedende overheid; bestuurder Fabienne Maes since 27.01.2025; "
                    "NACE RSZ2025 87.101; replaces 0267.390.002 closed 18.06.2019; "
                    "no KBO e-mail/finance; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "WV Het Dak site (campuses / FOI channel)",
                "url": SRC4_URL,
                "publisher": "Welzijnsvereniging Het Dak",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1333; HTTP 200; WZC Polderparel / WZC De Noordhinder / "
                    "assistentiewoningen De Mardyck; contact form only; FOI via "
                    "info@knokke-heist.be / Westkapellestraat 460 8300 Knokke-Heist"
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
                "name_nl": "Welzijnsvereniging 'Het Dak' (vereniging van OCMW's)",
                "name_fr": "Association de CPAS 'Het Dak'",
                "name_en": "Public welfare association 'Het Dak' (OCMW association)",
                "level": "ocmw_association",
                "parent_id": "city_knokke_heist",
                "community_language": "nl",
                "website": SRC4_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1333 leftover zorg residual of mined Knokke-Heist city+AGSO; "
                    "KBO 0863.329.989 Actief since 01.01.2002; official BBC JR2025 PDF downloads; "
                    "assets 52.803m cash 14.437m leasing 32.291m fin debt 26.367m pers 16.242m; "
                    "FOI ready VTE/lease/dual; not every-10"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_hetdak_assets_2025", "2025", "52802561", "2025 assets 52802561.13 was 53162485.81; tick1333; primary BBC J4"),
        ("bud_hetdak_cash_2025", "2025", "14436967", "2025 cash 14436966.55 vs 14019335.11; tick1333; primary BBC J4"),
        ("bud_hetdak_st_recv_2025", "2025", "2145912", "2025 ST recv 2145911.72 (ruil 2085399.32 + niet-ruil 60512.40); tick1333; primary BBC J4"),
        ("bud_hetdak_fixed_2025", "2025", "35668905", "2025 fixed 35668904.63 (FVA 61470 IGS + MVA 33955100.63 + IVA 0); tick1333; primary BBC J4/T5"),
        ("bud_hetdak_mva_lease_2025", "2025", "32291209", "2025 MVA leasing 32291208.86 of MVA 33955100.63; tick1333; primary BBC J4/T5"),
        ("bud_hetdak_fva_igs_2025", "2025", "61470", "2025 FVA IGS 61470 EVA 0; tick1333; primary BBC J4/T5"),
        ("bud_hetdak_debt_2025", "2025", "29738409", "2025 schulden 29738408.59 (ST 5297410.00 + LT 24440998.59); tick1333; primary BBC J4"),
        ("bud_hetdak_fin_debt_2025", "2025", "26367082", "2025 fin debt T4 26367081.82 (LT 24440998.80 + ST due 1926083.02); tick1333; primary BBC T4"),
        ("bud_hetdak_equity_2025", "2025", "23064153", "2025 nettoactief 23064152.54 was 21542118.73; tick1333; primary BBC J4"),
        ("bud_hetdak_cum_surplus_2025", "2025", "9844156", "2025 cum surplus 9844155.69 was 7966335.13; tick1333; primary BBC J4"),
        ("bud_hetdak_cap_subs_2025", "2025", "6104051", "2025 kapitaalsubsidies 6104050.85 was 6459837.60; tick1333; primary BBC J4/T5"),
        ("bud_hetdak_expl_in_2025", "2025", "25474555", "2025 expl ontv 25474554.60; tick1333; primary BBC J2"),
        ("bud_hetdak_expl_out_2025", "2025", "21447174", "2025 expl uitg 21447173.91; tick1333; primary BBC J2"),
        ("bud_hetdak_expl_2025", "2025", "4027381", "2025 expl saldo +4027380.69; tick1333; primary BBC J2"),
        ("bud_hetdak_invest_2025", "2025", "1686080", "2025 invest saldo -1686079.90 (uitg 2246834.75 / ontv 560754.85); tick1333; primary BBC J2"),
        ("bud_hetdak_bbr_2025", "2025", "169307", "2025 BBR year +169306.85; tick1333; primary BBC J2"),
        ("bud_hetdak_cum_bbr_2025", "2025", "14334947", "YE2025 cum BBR 14334946.59 was 14165639.74; tick1333; primary BBC J2"),
        ("bud_hetdak_afm_2025", "2025", "2406165", "2025 AFM +2406164.86; tick1333; primary BBC J2"),
        ("bud_hetdak_gecorr_afm_2025", "2025", "2295033", "2025 gecorr AFM +2295032.64; tick1333; primary BBC J2"),
        ("bud_hetdak_pnl_2025", "2025", "1877821", "2025 PnL +1877820.56 (ops 1765864.13 / fin 111956.43); tick1333; primary BBC J5"),
        ("bud_hetdak_pers_2025", "2025", "16242301", "2025 J5/T2 pers 16242301.41 (niet-vast 14763360.07 + vast 970838.11 + andere 508103.23); VTE unpublished FOI; tick1333; primary BBC"),
        ("bud_hetdak_goods_2025", "2025", "4489342", "2025 J5/T2 goederen/diensten 4489342.31; tick1333; primary BBC J5/T2"),
        ("bud_hetdak_werksub_in_2025", "2025", "3908787", "2025 J5=T2 werksub ontv 3908787.07 (alg 745093.00 + spec 3163694.07); tick1333; primary BBC J5/T2"),
        ("bud_hetdak_werksub_city_2025", "2025", "469189", "2025 T2 alg werksub van de gemeente 469189.00; dual city line FOI; tick1333; primary BBC T2"),
        ("bud_hetdak_werksub_vl_2025", "2025", "2615787", "2025 T2 VL werksub alg 275904.00 + spec 2339883.00 = 2615787.00; tick1333; primary BBC T2"),
        ("bud_hetdak_werksub_fed_2025", "2025", "823811", "2025 T2 spec werksub federale overheid 823811.00; tick1333; primary BBC T2"),
        ("bud_hetdak_ops_rev_2025", "2025", "21165739", "2025 J5 opbrengsten uit de werking 21165739.22; tick1333; primary BBC J5"),
        ("bud_hetdak_other_ops_2025", "2025", "121828", "2025 J5 andere operationele opbrengsten 121827.71; tick1333; primary BBC J5"),
        ("bud_hetdak_fin_cost_2025", "2025", "532008", "2025 J5/T2 fin costs 532008.18; tick1333; primary BBC J5/T2"),
        ("bud_hetdak_st_prov_2025", "2025", "1123395", "2025 ST voorzieningen 1123395.00; tick1333; primary BBC J4"),
        ("bud_hetdak_westkapelle_inv_2025", "2025", "1458128", "2025 invest nieuwbouw WZC Westkapelle/Polderparel 1458128.00 (actieplan 2020001); tick1333; primary BBC J1"),
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
                "commitment_id": "comm_hetdak_jr2025_lease_cash",
                "title": "WV Het Dak JR2025 leftover zorg dual (leasing 32.29m / fin debt 26.37m / cash 14.44m / pers 16.24m)",
                "entity_id": ENT,
                "beneficiary": "WZC Polderparel / WZC De Noordhinder / assistentiewoningen De Mardyck residents",
                "legal_basis": "Decreet lokaal bestuur welzijnsvereniging; BBC; Bestuursdecreet openbaarheid",
                "decision_date": "2002-01-01",
                "start_year": "2002",
                "end_year": "2025",
                "total_envelope_eur": "52802561",
                "cash_by_year": "",
                "remaining_eur": "14334947",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover zorg map VL Knokke-Heist — residentiele ouderenzorg; VTE/lease/dual missing",
                "cut_option": "Publish VTE + lease/debt counterparties + dual stad/AGSO/OCMW 2025 lines",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1333; assets 52802561 cash 14436967 leasing 32291209 fin debt 26367082 pers 16242301; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_hetdak_lease_32_29m_findebt_26_37m_cash_14_44m",
                "name": "WV Het Dak JR2025 leftover zorg: 52.80m assets / 32.29m leasing / 26.37m fin debt / 14.44m cash",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "21447174",
                "total_cost_eur": "52802561",
                "tco_notes": "Leftover dual zorg of mined Knokke-Heist: assets 52.80m / leasing MVA 32.29m / fin debt 26.37m / cash 14.44m / pers 16.24m; do not treat 52.80m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "WZC Polderparel / WZC De Noordhinder / De Mardyck residents",
                "stated_goal": "Local leftover zorg map VL Knokke-Heist — BBC PDF live; VTE/lease/dual FOI",
                "measured_outcome": "Official BBC PDF 2026-08-17: BBR +0.169m / AFM +2.406m / PnL +1.878m; cash 14.437m; fin debt 26.367m; VTE unpublished",
                "absurdity_score": "6.2",
                "cost_score": "7.4",
                "difficulty": "3.0",
                "priority_index": "6.6",
                "cut_proposal": "Publish VTE + lease counterparties vs 26.37m debt + dual stad/AGSO lines; do not recreate parallel zorg shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1333; leftover zorg of mined Knokke-Heist; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "VTE behind pers 16242301.41 + lease counterparties for MVA leasing "
                    "32291208.86 vs fin debt T4 26367081.82 + destination of cash 14436966.55 "
                    "vs cum BBR 14334946.59 + dual stad/OCMW/AGSO Knokke-Heist 2025 lines "
                    "(gemeente alg werksub 469189.00 / VL+fed werksub / Polderparel dading "
                    "1.458m 2025) + NBB WVV filing PDF or non-filing rechtsgrond + AV 01.06.2026."
                ),
                "why_it_matters": (
                    "Named leftover unmined zorg of already-mined Knokke-Heist city+AGSO "
                    "after honest residual dual hunt. KBO 0863.329.989 Actief. Official BBC "
                    "PDF now downloads (2.64MB). 52.80m leftover zorg shell with leasing 32.29m "
                    "and cash 14.44m. APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas "
                    "403 / Foleon leftover slugs redirect Hooibeekhoeve — not taken. Leftover "
                    "cities still no fetchable JR2025. Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "Welzijnsvereniging Het Dak / Gemeente Knokke-Heist",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_hetdak_jr2025_lease_cash",
                "linked_leaderboard_id": "lb_hetdak_lease_32_29m_findebt_26_37m_cash_14_44m",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; sourced euros from primary BBC; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1333",
        "title": "WV Het Dak JR2025 leftover zorg dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: WV Het Dak leftover zorg of mined Knokke-Heist city+AGSO after honest hunt; "
            "KBO 0863.329.989 Actief; live JR2025 BBC PDF (official 2.64MB J1-J5/T2-T5); "
            "sourced euros assets 52.803m / leasing 32.291m / fin debt 26.367m / cash 14.437m / "
            "pers 16.242m; FOI ready VTE/lease/dual"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T22:10:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1333 WV Het Dak leftover zorg residual; KBO 0863.329.989; "
            "live BBC PDF; sourced euros; FOI ready not sent; next rq_1334 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1334",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1333 done including WV Het Dak 1333 leftover zorg live BBC / "
            "EVA Inagro 1332 FOI-unpublished / "
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
            "skip already-mined WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / "
            "APB Monumentenwacht WVL 1326 / APB Vonk 1325 / APB Campus Vesta 1324 / AGB Blankenberge 1323 / "
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
        "notes": "spawned tick1333 after WV Het Dak leftover zorg live BBC; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1333", rq_new, rq_spawn)
    print("research_queue 1333", found, "spawned_1334", spawned)

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
                "last_unit_id": "rq_1333",
                "ticks_completed": "1333",
                "paused": "no",
                "notes": (
                    "tick1333 WV Het Dak leftover zorg residual; KBO 0863.329.989; "
                    "live JR2025 BBC PDF; sourced euros assets 52.803m leasing 32.291m fin debt 26.367m; "
                    "FOI ready; next rq_1334 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1333 - 2026-08-17 - rq_1333 WV Het Dak dual residual leftover zorg
- Unit: Welzijnsvereniging 'Het Dak' leftover zorg of already-mined Knokke-Heist (city GE + AGSO) after residual dual hunt (KBO **0863.329.989**; official welzijnsverenigingen + live BBC PDF 2.64MB / J1–J5 T2–T5; goedkeuring AV **01.06.2026**; publicatie **04.06.2026**). PREFER leftover AGB/zorg/EVA/IGS/other-province APB with a live JR2025 BBC/NBB PDF: first leftover zorg whose official page now yields a downloadable BBC PDF. Distinct from already-mined AGSO Knokke-Heist / city Knokke-Heist / Zorg Houthalen 1329 / Zilveren Zwaan Heist. KBO Actief / normale toestand since **01.01.2002**; zetel Westkapellestraat 460 8300 Knokke-Heist since 12.12.2023; **3 VE**; RSZ-werkgever since 01.01.2022; aanbestedende overheid; bestuurder Fabienne Maes since 27.01.2025; AD Franck Libeer; FD Lucrèce Leeman; NACE 87.101; replaces 0267.390.002 closed 18.06.2019. WZC Polderparel / WZC De Noordhinder / assistentiewoningen De Mardyck. Hunt leftover AGB first: AGB Bornem official still JR2024-only; AGB De Kluize unpublished; AGB Pelt already mined. Leftover cities Londerzeel official still JR2022–2024 only / Wortegem-Petegem official JR2020–2024 only / Zwalm `/jaarrekening` 404 / Holsbeek 404 / Maarkedal TLS / Linkebeek 404 / Kapellen city GE 404 / Drogenbos 404 / Boutersem archive-only / Maaseik city GE 404 / Bierbeek 404 still no fetchable JR2025. APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas official pages 403 / Foleon leftover slugs redirect already-mined Hooibeekhoeve — not taken. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / Vlabinvest 1327 / Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320. Not an every-10 tick.
- EUR strong (primary BBC J2/J4/J5/T2/T4/T5): assets **52.802.561** (was 53.162.486); cash **14.436.967** vs 14.019.335; ST recv **2.145.912** (ruil **2.085.399** + niet-ruil **60.512**); LT recv due **550.778**; fixed **35.668.905**; FVA **61.470** (EVA **0** + IGS **61.470**); MVA **33.955.101** leasing **32.291.209**; IVA **0**; schulden **29.738.409**; ST **5.297.410** (voorzieningen **1.123.395** + non-fin ruil **2.218.285** + ST due **1.926.083**); LT fin debt **24.440.999**; fin debt T4 **26.367.082**; equity **23.064.153**; cum surplus **9.844.156**; cap-subs **6.104.051**; expl **+4.027.381** (ontv **25.474.555** / uitg **21.447.174**); invest **−1.686.080**; fin **−2.171.994**; BBR year **+169.307**; cum BBR **14.334.947**; AFM **+2.406.165**; gecorr AFM **+2.295.033**; PnL **+1.877.821**; pers J5/T2 **16.242.301**; werksub granted **0**; werksub received J5=T2 **3.908.787** (alg **745.093** of which gemeente **469.189** + VL **275.904**; spec **3.163.694** of which VL **2.339.883** + fed **823.811**); ops rev **21.165.739**; other ops **121.828**; goederen **4.489.342**; fin costs **532.008**. VTE unpublished.
- CSVs: sources+4/entities+1/budgets+31/commitments+1/leaderboard+1 + FOI ready `gap_hetdak_lease_32_29m_findebt_26_37m_cash_14_44m_vte_l5` (not sent); rq_1333=done; spawn rq_1334; ticks=1333. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (WV Het Dak leftover zorg live BBC). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1334 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1333 write done")


if __name__ == "__main__":
    main()

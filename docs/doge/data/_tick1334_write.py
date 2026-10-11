# -*- coding: utf-8 -*-
"""Tick 1334 — WV OPcura leftover zorg residual, JR2025 BBC euros.
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

TICK = "1334"
UTC = "2026-08-17T22:45:00Z"
ENT = "zorg_opcura"
HIER = "Vlaanderen>VlaamsBrabant>Opwijk>Zorg>OPcura"
GAP = "gap_opcura_afm_neg_0_38m_cash_drop_0_91m_citysub_1_24m_l5"
SRC = "src_opcura_jr2025_pdf"
SRC2 = "src_opcura_docs"
SRC3 = "src_kbo_opcura_0684493762"
SRC4 = "src_opcura_foi_contact"
SRC_URL = "https://opcura.be/sites/default/files/2026-06/Jaarrekening-2025-OPcura-Publicatie.pdf"
SRC2_URL = "https://opcura.be/over-opcura/beleidsdocumenten"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0684493762"
SRC4_URL = "https://opcura.be/"
FOI_EMAIL = "geert.geeroms@opcura.be"
FOI_POSTAL = "Kloosterstraat 75 1745 Opwijk"
DRAFT = "docs/doge/foi/drafts/gap_opcura_afm_neg_0_38m_cash_drop_0_91m_citysub_1_24m_l5.md"


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
                "title": "WV OPcura jaarrekening 2025 BBC (official PDF; J1-J5 / T2-T5)",
                "url": SRC_URL,
                "publisher": "Zorgvereniging OPcura / Gemeente Opwijk",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1334; official BBC PDF 12.21MB; goedkeuring AV 16.06.2026 / "
                    "publicatie 22.06.2026; print schemas J1-J5 T2-T5; leftover zorg of mined Opwijk"
                ),
            },
            {
                "source_id": SRC2,
                "title": "OPcura beleidsdocumenten (JR2025 listed)",
                "url": SRC2_URL,
                "publisher": "Zorgvereniging OPcura",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1334; HTTP 200 lists Jaarrekening 2025 11.65MB pub 22.06.2026 + MJP 2026-2031; "
                    "FOI channel geert.geeroms@opcura.be"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Zorgvereniging OPcura 0684.493.762",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1334; KBO 0684.493.762 Actief / normale toestand since 08.11.2017; "
                    "statutaire naam Zorgvereniging OPcura / afkorting ZV OPcura; "
                    "Vereniging van OCMW's; zetel Kloosterstraat 75 1745 Opwijk; "
                    "1 VE; RSZ-werkgever since 01.01.2022; "
                    "bestuurder Patrick De Smedt since 08.11.2017 + Maaike Deleu since 11.03.2025; "
                    "e-mail geert.geeroms@opcura.be since 22.04.2025; tel 052/36 59 41; "
                    "NACE RSZ2025 87.101; no KBO finance/web; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "WV OPcura site (zorgcampus / FOI channel)",
                "url": SRC4_URL,
                "publisher": "Zorgvereniging OPcura",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1334; HTTP 200; zorgcampus Kloosterstraat 75 1745 Opwijk; "
                    "publiekrechtelijke welzijnsvereniging since 01.01.2018; "
                    "~115 medewerkers; FOI via geert.geeroms@opcura.be / info@opwijk.be"
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
                "name_nl": "Zorgvereniging OPcura (vereniging van OCMW's)",
                "name_fr": "Association de CPAS OPcura",
                "name_en": "Public welfare association OPcura (OCMW association)",
                "level": "ocmw_association",
                "parent_id": "city_opwijk",
                "community_language": "nl",
                "website": SRC4_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1334 leftover zorg residual of mined Opwijk city GE; "
                    "KBO 0684.493.762 Actief since 08.11.2017; official BBC JR2025 PDF downloads; "
                    "assets 2.504m cash 0.493m DROP AFM -0.382m city werksub 1.236m VTE 93.00; "
                    "FOI ready AFM/cash/dual; not every-10"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_opcura_assets_2025", "2025", "2504005", "2025 assets 2504005 was 3212361; tick1334; primary BBC J4"),
        ("bud_opcura_cash_2025", "2025", "492912", "2025 cash 492912 DROP vs 1404044; tick1334; primary BBC J4"),
        ("bud_opcura_st_recv_2025", "2025", "693339", "2025 ST recv 693339 (ruil 516162 + niet-ruil 177177); tick1334; primary BBC J4"),
        ("bud_opcura_fixed_2025", "2025", "1285457", "2025 fixed 1285457 (FVA 1250 IGS + MVA 1181795 + IVA 102413); tick1334; primary BBC J4/T5"),
        ("bud_opcura_mva_2025", "2025", "1181795", "2025 MVA 1181795 leasing 0 of MVA bedrijfsmatig 1175767; tick1334; primary BBC J4"),
        ("bud_opcura_fva_igs_2025", "2025", "1250", "2025 FVA IGS 1250 EVA 0 (new vs 0 in 2024); tick1334; primary BBC J4/T2"),
        ("bud_opcura_iva_2025", "2025", "102413", "2025 IVA 102413 was 104854; tick1334; primary BBC J4"),
        ("bud_opcura_debt_2025", "2025", "1285424", "2025 schulden 1285424 all ST (voorzieningen 330584 + non-fin ruil 948936); tick1334; primary BBC J4"),
        ("bud_opcura_fin_debt_2025", "2025", "0", "2025 fin debt T4 0 (LT 0 + ST 0; no new loans 2020-2025); tick1334; primary BBC T4"),
        ("bud_opcura_equity_2025", "2025", "1218581", "2025 nettoactief 1218581 was 1873702; tick1334; primary BBC J4"),
        ("bud_opcura_cum_surplus_2025", "2025", "-432918", "2025 cum surplus -432918 was +214423; tick1334; primary BBC J4"),
        ("bud_opcura_cap_subs_2025", "2025", "85580", "2025 kapitaalsubsidies 85580 was 93360; tick1334; primary BBC J4"),
        ("bud_opcura_expl_in_2025", "2025", "8888479", "2025 expl ontv 8888479; tick1334; primary BBC J2"),
        ("bud_opcura_expl_out_2025", "2025", "9270285", "2025 expl uitg 9270285; tick1334; primary BBC J2"),
        ("bud_opcura_expl_2025", "2025", "-381806", "2025 expl saldo -381806; tick1334; primary BBC J2"),
        ("bud_opcura_invest_2025", "2025", "-500681", "2025 invest saldo -500681 (uitg 500681 / ontv 0); tick1334; primary BBC J2"),
        ("bud_opcura_bbr_2025", "2025", "-882487", "2025 BBR year -882487; tick1334; primary BBC J2"),
        ("bud_opcura_cum_bbr_2025", "2025", "237315", "YE2025 cum BBR 237315 was 1119802; tick1334; primary BBC J2"),
        ("bud_opcura_afm_2025", "2025", "-381806", "2025 AFM -381806; tick1334; primary BBC J2"),
        ("bud_opcura_gecorr_afm_2025", "2025", "-381806", "2025 gecorr AFM -381806; tick1334; primary BBC J2"),
        ("bud_opcura_pnl_2025", "2025", "-647340", "2025 PnL -647340 (ops -658170 / fin +10830); tick1334; primary BBC J5"),
        ("bud_opcura_pers_2025", "2025", "6353535", "2025 J5/T2 pers 6353535 (niet-vast 6145393 + andere 208142); VTE 93.00 / 120 koppen; tick1334; primary BBC"),
        ("bud_opcura_vte_2025", "2025", "93", "2025 VTE 93.00 (120 koppen; statutair 4.00 / contractueel 89.00); tick1334; primary BBC personeelsinzet"),
        ("bud_opcura_goods_2025", "2025", "2919930", "2025 J5 goederen/diensten 2919930 (T2 2913190); tick1334; primary BBC J5"),
        ("bud_opcura_werksub_in_2025", "2025", "2428751", "2025 J5=T2 werksub ontv 2428751 (alg 1236287 + spec 1192464); tick1334; primary BBC J5/T2"),
        ("bud_opcura_werksub_city_2025", "2025", "1236287", "2025 T2 alg werksub van de gemeente 1236287; MJP 2026 drops to 700000; dual city line FOI; tick1334; primary BBC T2"),
        ("bud_opcura_werksub_vl_2025", "2025", "806190", "2025 T2 spec werksub VL 806190 (alg VL 0); tick1334; primary BBC T2"),
        ("bud_opcura_werksub_fed_2025", "2025", "386274", "2025 T2 spec werksub federale overheid 386274; tick1334; primary BBC T2"),
        ("bud_opcura_ops_rev_2025", "2025", "6412492", "2025 J5 opbrengsten uit de werking 6412492; tick1334; primary BBC J5"),
        ("bud_opcura_other_ops_2025", "2025", "43902", "2025 J5 andere operationele opbrengsten 43902; tick1334; primary BBC J5"),
        ("bud_opcura_st_prov_2025", "2025", "330584", "2025 ST voorzieningen 330584; tick1334; primary BBC J4"),
        ("bud_opcura_cash_drop_2025", "2025", "911132", "2025 cash drop 1404044-492912=911132; FOI destination; tick1334; primary BBC J4"),
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
                "commitment_id": "comm_opcura_jr2025_afm_cash",
                "title": "WV OPcura JR2025 leftover zorg dual (AFM -0.38m / cash drop 0.91m / city werksub 1.24m / pers 6.35m)",
                "entity_id": ENT,
                "beneficiary": "OPcura zorgcampus / WZC / assistentiewoningen / thuiszorg Opwijk residents",
                "legal_basis": "Decreet lokaal bestuur welzijnsvereniging; BBC; Bestuursdecreet openbaarheid",
                "decision_date": "2017-11-08",
                "start_year": "2018",
                "end_year": "2025",
                "total_envelope_eur": "2504005",
                "cash_by_year": "",
                "remaining_eur": "237315",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover zorg map VL Opwijk — residentiele ouderenzorg; AFM/cash/dual missing",
                "cut_option": "Publish AFM/cash-drop drivers + dual stad/OCMW 2025-2026 werksub path",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1334; assets 2504005 cash 492912 AFM -381806 city werksub 1236287 pers 6353535 VTE 93; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_opcura_afm_neg_0_38m_cash_drop_0_91m",
                "name": "WV OPcura JR2025 leftover zorg: AFM -0.38m / cash drop 0.91m / city werksub 1.24m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "9270285",
                "total_cost_eur": "2504005",
                "tco_notes": "Leftover dual zorg of mined Opwijk: assets 2.50m / cash 0.49m DROP 0.91m / AFM -0.38m / city werksub 1.24m / pers 6.35m VTE 93; do not treat 2.50m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "OPcura zorgcampus / WZC / assistentiewoningen / thuiszorg residents",
                "stated_goal": "Local leftover zorg map VL Opwijk — BBC PDF live; AFM/cash/dual FOI",
                "measured_outcome": "Official BBC PDF 2026-08-17: BBR -0.882m / AFM -0.382m / PnL -0.647m; cash 0.493m DROP; fin debt 0; VTE 93.00",
                "absurdity_score": "5.8",
                "cost_score": "5.4",
                "difficulty": "3.0",
                "priority_index": "5.6",
                "cut_proposal": "Publish AFM/cash-drop drivers + dual stad werksub path (1.24m to 0.70m in MJP 2026); do not recreate parallel zorg shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1334; leftover zorg of mined Opwijk; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "AFM drivers behind -381806 + destination of cash drop 911132 "
                    "(1404044 to 492912) vs cum BBR 237315 + dual stad/OCMW Opwijk 2025-2026 "
                    "lines (gemeente alg werksub 1236287 dropping to 700000 in MJP 2026) + "
                    "IGS FVA 1250 counterpart + NBB WVV filing PDF or non-filing rechtsgrond + "
                    "AV 16.06.2026 + vacant FD in BBC."
                ),
                "why_it_matters": (
                    "Named leftover unmined zorg of already-mined Opwijk city GE "
                    "after honest residual dual hunt. KBO 0684.493.762 Actief. Official BBC "
                    "PDF now downloads (12.21MB). 2.50m leftover zorg shell with AFM -0.38m "
                    "and cash drop 0.91m. APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas "
                    "403 / Foleon leftover slugs redirect Hooibeekhoeve — not taken. Leftover "
                    "cities still no fetchable JR2025. Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "Zorgvereniging OPcura / Gemeente Opwijk",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_opcura_jr2025_afm_cash",
                "linked_leaderboard_id": "lb_opcura_afm_neg_0_38m_cash_drop_0_91m",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; sourced euros from primary BBC; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1334",
        "title": "WV OPcura JR2025 leftover zorg dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: WV OPcura leftover zorg of mined Opwijk city GE after honest hunt; "
            "KBO 0684.493.762 Actief; live JR2025 BBC PDF (official 12.21MB J1-J5/T2-T5); "
            "sourced euros assets 2.504m / cash 0.493m DROP / AFM -0.382m / city werksub 1.236m / "
            "pers 6.354m VTE 93.00; FOI ready AFM/cash/dual"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T22:25:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1334 WV OPcura leftover zorg residual; KBO 0684.493.762; "
            "live BBC PDF; sourced euros; FOI ready not sent; next rq_1335 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1335",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1334 done including WV OPcura 1334 leftover zorg live BBC / "
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
            "skip already-mined WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / "
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
        "notes": "spawned tick1334 after WV OPcura leftover zorg live BBC; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1334", rq_new, rq_spawn)
    print("research_queue 1334", found, "spawned_1335", spawned)

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
                "last_unit_id": "rq_1334",
                "ticks_completed": "1334",
                "paused": "no",
                "notes": (
                    "tick1334 WV OPcura leftover zorg residual; KBO 0684.493.762; "
                    "live JR2025 BBC PDF; sourced euros assets 2.504m cash 0.493m AFM -0.382m; "
                    "FOI ready; next rq_1335 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1334 - 2026-08-17 - rq_1334 WV OPcura dual residual leftover zorg
- Unit: Zorgvereniging OPcura leftover zorg of already-mined Opwijk (city GE) after residual dual hunt (KBO **0684.493.762**; official beleidsdocumenten + live BBC PDF 12.21MB / J1–J5 T2–T5; goedkeuring AV **16.06.2026**; publicatie **22.06.2026**). PREFER leftover AGB/zorg/EVA/IGS/other-province APB with a live JR2025 BBC/NBB PDF: first leftover zorg whose official page now yields a downloadable BBC PDF. Distinct from already-mined city Opwijk GE / WV Het Dak 1333 / Zorg Houthalen 1329 / Zilveren Zwaan Heist / Motena. KBO Actief / normale toestand since **08.11.2017**; zetel Kloosterstraat 75 1745 Opwijk; **1 VE**; RSZ-werkgever since 01.01.2022; bestuurder Patrick De Smedt since 08.11.2017 + Maaike Deleu since 11.03.2025; AD Christel Ringoot; FD vacant in BBC; e-mail geert.geeroms@opcura.be; NACE 87.101. Publiekrechtelijke welzijnsvereniging since 01.01.2018 (ex-OCMW zorgcampus). Hunt leftover AGB first: AGB Bornem official still JR2024-only; AGB De Kluize unpublished; AGB Pelt already mined. Leftover cities Londerzeel official still JR2022–2024 only / Wortegem-Petegem official JR2020–2024 only / Zwalm `/jaarrekening` 404 / Holsbeek 404 / Maarkedal TLS / Linkebeek 404 / Kapellen city GE 404 / Drogenbos 404 / Boutersem archive-only / Maaseik city GE 404 / Bierbeek 404 still no fetchable JR2025. APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas official pages 403 / Foleon leftover slugs redirect already-mined Hooibeekhoeve — not taken. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / Vlabinvest 1327 / Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320. Not an every-10 tick.
- EUR strong (primary BBC J2/J4/J5/T2/T4/T5): assets **2.504.005** (was 3.212.361); cash **492.912** DROP vs 1.404.044; ST recv **693.339** (ruil **516.162** + niet-ruil **177.177**); voorraden **14.593**; fixed **1.285.457**; FVA **1.250** (EVA **0** + IGS **1.250** new); MVA **1.181.795** leasing **0**; IVA **102.413**; schulden **1.285.424** all ST (voorzieningen **330.584** + non-fin ruil **948.936**); LT **0**; fin debt T4 **0**; equity **1.218.581**; cum surplus **−432.918**; cap-subs **85.580**; expl **−381.806** (ontv **8.888.479** / uitg **9.270.285**); invest **−500.681**; fin **0**; BBR year **−882.487**; cum BBR **237.315**; AFM/gecorr **−381.806**; PnL **−647.340**; pers J5/T2 **6.353.535**; VTE **93,00** / 120 koppen (statutair **4,00** / contractueel **89,00**); werksub granted **0**; werksub received J5=T2 **2.428.751** (alg **1.236.287** all gemeente; spec **1.192.464** of which VL **806.190** + fed **386.274**); ops rev **6.412.492**; other ops **43.902**; goederen J5 **2.919.930**.
- CSVs: sources+4/entities+1/budgets+32/commitments+1/leaderboard+1 + FOI ready `gap_opcura_afm_neg_0_38m_cash_drop_0_91m_citysub_1_24m_l5` (not sent); rq_1334=done; spawn rq_1335; ticks=1334. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (WV OPcura leftover zorg live BBC). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1335 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1334 write done")


if __name__ == "__main__":
    main()

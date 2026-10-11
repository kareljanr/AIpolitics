# -*- coding: utf-8 -*-
"""Tick 1335 — WV BVK Knokke-Heist leftover zorg residual, JR2025 BBC euros.
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

TICK = "1335"
UTC = "2026-08-17T23:10:00Z"
ENT = "zorg_bvk"
HIER = "Vlaanderen>WestVlaanderen>KnokkeHeist>Zorg>BVK"
GAP = "gap_bvk_cash_drop_0_10m_strecv_0_35m_citysub_0_27m_vte_l5"
SRC = "src_bvk_jr2025_pdf"
SRC2 = "src_bvk_docs"
SRC3 = "src_kbo_bvk_0865506155"
SRC4 = "src_bvk_foi_contact"
SRC_URL = "https://www.knokke-heist.be/sites/default/files/inline-files/JAARREKENING%202025%20-%20na%20COMMISSIE.pdf"
SRC2_URL = "https://www.knokke-heist.be/gemeente-en-bestuur/beleidsrapporten/welzijnsverenigingen"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0865506155"
SRC4_URL = "https://www.knokke-heist.be/wonen/huren-en-verhuren/betaalbaar-verhuurkantoor-bvk/betaalbaar-verhuren"
FOI_EMAIL = "woonloket@knokke-heist.be"
FOI_POSTAL = "Kraaiennestplein 1 bus 3 8301 Knokke-Heist"
DRAFT = "docs/doge/foi/drafts/gap_bvk_cash_drop_0_10m_strecv_0_35m_citysub_0_27m_vte_l5.md"


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
                "title": "WV BVK Knokke-Heist jaarrekening 2025 BBC (official PDF; J1-J5 / T2-T5)",
                "url": SRC_URL,
                "publisher": "WV BVK Knokke-Heist / Gemeente Knokke-Heist",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1335; official BBC PDF 1.44MB 29p; goedkeuring AV 05.06.2026 / "
                    "publicatie 10.06.2026; print schemas J1-J5 T2-T5; leftover zorg of mined Knokke-Heist"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Knokke-Heist welzijnsverenigingen (JR2025 BVK listed)",
                "url": SRC2_URL,
                "publisher": "Gemeente Knokke-Heist",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1335; HTTP 200 lists WV BVK Jaarrekening 2025 AV 05.06.2026 / bekendmaking 10.06.2026 "
                    "+ MJP 2026-2031; leftover sister of already-mined WV Het Dak 1333"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO BVK Knokke-Heist 0865.506.155",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1335; KBO 0865.506.155 Actief / normale toestand since 02.06.2004; "
                    "statutaire naam BVK Knokke-Heist since 05.03.2024 (ex-Woonwinkel); "
                    "Vereniging van OCMW's; zetel Kraaiennestplein 1 bus 3 8301 Knokke-Heist; "
                    "1 VE; RSZ-werkgever since 01.01.2022; aanbestedende overheid since 02.06.2004; "
                    "algemeen lasthebber Stefaan Keirse since 18.03.2024; "
                    "NACE RSZ2025 68.202; no KBO e-mail/tel/web; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "WV BVK Knokke-Heist city page (betaalbaar verhuren / FOI channel)",
                "url": SRC4_URL,
                "publisher": "Gemeente Knokke-Heist",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1335; HTTP 200; zetel Kraaiennestplein 1 bus 3 8301 Knokke-Heist; "
                    "29 panden YE2025; FOI via woonloket@knokke-heist.be / info@knokke-heist.be; "
                    "tel 050 53 09 89"
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
                "name_nl": "BVK Knokke-Heist (vereniging van OCMW's / ex-Woonwinkel)",
                "name_fr": "Association de CPAS BVK Knokke-Heist",
                "name_en": "Public welfare association BVK Knokke-Heist (affordable rental office)",
                "level": "ocmw_association",
                "parent_id": "city_knokke_heist",
                "community_language": "nl",
                "website": SRC4_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1335 leftover zorg residual of mined Knokke-Heist city+AGSO+Het Dak; "
                    "KBO 0865.506.155 Actief since 02.06.2004; official BBC JR2025 PDF downloads; "
                    "assets 0.372m cash 0.023m DROP ST recv 0.346m city werksub 0.273m VTE unpublished; "
                    "FOI ready cash/ST-recv/dual/VTE; not every-10"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_bvk_assets_2025", "2025", "371940", "2025 assets 371940 was 272775; tick1335; primary BBC J4"),
        ("bud_bvk_cash_2025", "2025", "22726", "2025 cash 22726 DROP vs 125237; tick1335; primary BBC J4"),
        ("bud_bvk_st_recv_2025", "2025", "346124", "2025 ST recv 346124 all ruil (niet-ruil 0) JUMP vs 145188; tick1335; primary BBC J4"),
        ("bud_bvk_fixed_2025", "2025", "3090", "2025 fixed 3090 (FVA 3090 + MVA 0 + IVA 0); tick1335; primary BBC J4/T5"),
        ("bud_bvk_fva_2025", "2025", "3090", "2025 FVA 3090 (IGS 1250 new + other 1840); tick1335; primary BBC J4/T5"),
        ("bud_bvk_fva_igs_2025", "2025", "1250", "2025 FVA IGS 1250 EVA 0 (new vs 0 in 2024); tick1335; primary BBC J4/T2/T5"),
        ("bud_bvk_mva_2025", "2025", "0", "2025 MVA 0 was 510 (fully depreciated furniture/office); tick1335; primary BBC J4/T5"),
        ("bud_bvk_debt_2025", "2025", "46571", "2025 schulden 46571 all ST (voorzieningen 22572 + non-fin ruil 23999); tick1335; primary BBC J4"),
        ("bud_bvk_fin_debt_2025", "2025", "0", "2025 fin debt T4 0 (LT 0 + ST 0; no loans); tick1335; primary BBC T4"),
        ("bud_bvk_equity_2025", "2025", "325369", "2025 nettoactief 325369 was 237337; tick1335; primary BBC J4"),
        ("bud_bvk_cum_surplus_2025", "2025", "278004", "2025 cum surplus 278004 was 189972; tick1335; primary BBC J4/T5"),
        ("bud_bvk_other_equity_2025", "2025", "47365", "2025 overig nettoactief 47365 unchanged; tick1335; primary BBC J4"),
        ("bud_bvk_expl_in_2025", "2025", "896089", "2025 expl ontv 896089; tick1335; primary BBC J2"),
        ("bud_bvk_expl_out_2025", "2025", "806329", "2025 expl uitg 806329; tick1335; primary BBC J2"),
        ("bud_bvk_expl_2025", "2025", "89760", "2025 expl saldo +89760; tick1335; primary BBC J2"),
        ("bud_bvk_invest_2025", "2025", "-1250", "2025 invest saldo -1250 (IGS FVA aankoop 1250 / ontv 0); tick1335; primary BBC J2/T2"),
        ("bud_bvk_bbr_2025", "2025", "88510", "2025 BBR year +88510; tick1335; primary BBC J2"),
        ("bud_bvk_cum_bbr_2025", "2025", "344851", "YE2025 cum BBR 344851 was 256341; tick1335; primary BBC J2"),
        ("bud_bvk_afm_2025", "2025", "89760", "2025 AFM +89760; tick1335; primary BBC J2"),
        ("bud_bvk_gecorr_afm_2025", "2025", "89760", "2025 gecorr AFM +89760; tick1335; primary BBC J2"),
        ("bud_bvk_pnl_2025", "2025", "88032", "2025 PnL +88032 (ops +88044 / fin -12); tick1335; primary BBC J5"),
        ("bud_bvk_pers_2025", "2025", "397252", "2025 J5/T2 pers 397252 (niet-vast 386658 + andere 10594); VTE unpublished; tick1335; primary BBC"),
        ("bud_bvk_goods_2025", "2025", "390747", "2025 J5=T2 goederen/diensten 390747; tick1335; primary BBC J5/T2"),
        ("bud_bvk_werksub_in_2025", "2025", "273451", "2025 J5=T2 werksub ontv 273451 all spec van de gemeente (alg 0); tick1335; primary BBC J5/T2"),
        ("bud_bvk_werksub_city_2025", "2025", "273451", "2025 T2 spec werksub van de gemeente 273451 was 173451; dual city line FOI; tick1335; primary BBC T2"),
        ("bud_bvk_ops_rev_2025", "2025", "288474", "2025 J5 opbrengsten uit de werking 288474; tick1335; primary BBC J5"),
        ("bud_bvk_other_ops_2025", "2025", "334164", "2025 J5 andere operationele opbrengsten 334164 was 214619; dual FOI; tick1335; primary BBC J5"),
        ("bud_bvk_st_prov_2025", "2025", "22572", "2025 ST voorzieningen 22572; tick1335; primary BBC J4"),
        ("bud_bvk_cash_drop_2025", "2025", "102511", "2025 cash drop 125237-22726=102511; FOI destination; tick1335; primary BBC J4"),
        ("bud_bvk_st_recv_jump_2025", "2025", "200936", "2025 ST recv jump 346124-145188=200936; FOI counterparties; tick1335; primary BBC J4"),
        ("bud_bvk_panden_2025", "2025", "29", "2025 YE panden 29 (BBC beleidsevaluatie); tick1335; primary BBC narrative"),
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
                "commitment_id": "comm_bvk_jr2025_cash_strecv",
                "title": "WV BVK Knokke-Heist JR2025 leftover zorg dual (cash drop 0.10m / ST recv 0.35m / city werksub 0.27m / pers 0.40m)",
                "entity_id": ENT,
                "beneficiary": "BVK Knokke-Heist / 29 betaalbare huurpanden / private eigenaars / middeninkomens",
                "legal_basis": "Decreet lokaal bestuur welzijnsvereniging; BBC; Bestuursdecreet openbaarheid",
                "decision_date": "2004-06-02",
                "start_year": "2004",
                "end_year": "2025",
                "total_envelope_eur": "371940",
                "cash_by_year": "",
                "remaining_eur": "344851",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover zorg map VL Knokke-Heist — betaalbaar verhuren; cash/ST-recv/dual/VTE missing",
                "cut_option": "Publish cash-drop + ST-recv counterparties + dual stad/OCMW 2025-2026 werksub path + VTE",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1335; assets 371940 cash 22726 ST recv 346124 city werksub 273451 pers 397252 VTE unpublished; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_bvk_cash_drop_0_10m_strecv_0_35m",
                "name": "WV BVK Knokke-Heist JR2025 leftover zorg: cash drop 0.10m / ST recv 0.35m / city werksub 0.27m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "806329",
                "total_cost_eur": "371940",
                "tco_notes": "Leftover dual zorg of mined Knokke-Heist: assets 0.37m / cash 0.023m DROP 0.10m / ST recv 0.35m JUMP / city werksub 0.27m / pers 0.40m VTE unpublished; do not treat 0.37m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "BVK Knokke-Heist / 29 betaalbare huurpanden / middeninkomens",
                "stated_goal": "Local leftover zorg map VL Knokke-Heist — BBC PDF live; cash/ST-recv/dual/VTE FOI",
                "measured_outcome": "Official BBC PDF 2026-08-17: BBR +0.089m / AFM +0.090m / PnL +0.088m; cash 0.023m DROP; ST recv 0.346m; fin debt 0; VTE unpublished",
                "absurdity_score": "5.2",
                "cost_score": "4.4",
                "difficulty": "3.0",
                "priority_index": "5.0",
                "cut_proposal": "Publish cash-drop destination + ST-recv counterparties + dual stad werksub 0.27m + other ops 0.33m + VTE; do not recreate parallel woon-shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1335; leftover zorg of mined Knokke-Heist; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "Destination of cash drop 102511 (125237 to 22726) vs cum BBR 344851 + "
                    "counterparties/age of ST recv JUMP 200936 (145188 to 346124 all ruil) + "
                    "dual stad/OCMW Knokke-Heist 2025-2026 lines (specifieke gemeente werksub "
                    "273451 was 173451; andere operationele opbrengsten 334164) + IGS FVA 1250 "
                    "counterpart + VTE/koppen behind pers 397252 + NBB WVV filing PDF or "
                    "non-filing rechtsgrond + AV 05.06.2026."
                ),
                "why_it_matters": (
                    "Named leftover unmined zorg of already-mined Knokke-Heist city GE + AGSO "
                    "+ WV Het Dak 1333 after honest residual dual hunt. KBO 0865.506.155 Actief. "
                    "Official BBC PDF now downloads (1.44MB 29p). 0.37m leftover woon-shell with "
                    "cash drop 0.10m and ST recv 0.35m. APB POA/TPA/De Schorre/Warande/De Nekker/"
                    "PIH/Inovant/Atlas 403 / Foleon leftover slugs redirect Hooibeekhoeve — not "
                    "taken. Leftover cities still no fetchable JR2025. Do not invent euros."
                ),
                "priority": "8",
                "recipient_body": "WV BVK Knokke-Heist / Gemeente Knokke-Heist",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_bvk_jr2025_cash_strecv",
                "linked_leaderboard_id": "lb_bvk_cash_drop_0_10m_strecv_0_35m",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; sourced euros from primary BBC; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1335",
        "title": "WV BVK Knokke-Heist JR2025 leftover zorg dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: WV BVK Knokke-Heist leftover zorg of mined Knokke-Heist city+AGSO+Het Dak after honest hunt; "
            "KBO 0865.506.155 Actief; live JR2025 BBC PDF (official 1.44MB 29p J1-J5/T2-T5); "
            "sourced euros assets 0.372m / cash 0.023m DROP / ST recv 0.346m / city werksub 0.273m / "
            "pers 0.397m VTE unpublished; FOI ready cash/ST-recv/dual/VTE"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T22:45:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1335 WV BVK leftover zorg residual; KBO 0865.506.155; "
            "live BBC PDF; sourced euros; FOI ready not sent; next rq_1336 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1336",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1335 done including WV BVK 1335 leftover zorg live BBC / "
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
            "skip already-mined WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / "
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
        "notes": "spawned tick1335 after WV BVK leftover zorg live BBC; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1335", rq_new, rq_spawn)
    print("research_queue 1335", found, "spawned_1336", spawned)

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
                "last_unit_id": "rq_1335",
                "ticks_completed": "1335",
                "paused": "no",
                "notes": (
                    "tick1335 WV BVK leftover zorg residual; KBO 0865.506.155; "
                    "live JR2025 BBC PDF; sourced euros assets 0.372m cash 0.023m ST recv 0.346m; "
                    "FOI ready; next rq_1336 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1335 - 2026-08-17 - rq_1335 WV BVK Knokke-Heist dual residual leftover zorg
- Unit: Welzijnsvereniging BVK Knokke-Heist (ex-Woonwinkel) leftover zorg of already-mined Knokke-Heist (city GE + AGSO + WV Het Dak 1333) after residual dual hunt (KBO **0865.506.155**; official welzijnsverenigingen + live BBC PDF 1.44MB 29p / J1–J5 T2–T5; goedkeuring AV **05.06.2026**; publicatie **10.06.2026**). PREFER leftover AGB/zorg/EVA/IGS/other-province APB with a live JR2025 BBC/NBB PDF: first leftover zorg whose official page now yields a downloadable BBC PDF (same knokke-heist.be portal as Het Dak 1333). Distinct from already-mined AGSO Knokke-Heist / city Knokke-Heist / WV Het Dak 1333 / Zilveren Zwaan Heist / WV OPcura 1334. KBO Actief / normale toestand since **02.06.2004**; statutaire naam BVK Knokke-Heist since 05.03.2024; zetel Kraaiennestplein 1 bus 3 8301 Knokke-Heist; **1 VE**; RSZ-werkgever since 01.01.2022; aanbestedende overheid; algemeen lasthebber Stefaan Keirse since 18.03.2024; voorzitter Cathy Coudyser; NACE 68.202. Hunt leftover AGB first: AGB Bornem official still JR2024-only; AGB De Kluize unpublished; AGB Pelt already mined. Leftover cities Londerzeel official still JR2022–2024 only / Wortegem-Petegem official JR2020–2024 only / Zwalm `/jaarrekening` 404 / Holsbeek 404 / Maarkedal TLS / Linkebeek 404 / Kapellen city GE 404 / Drogenbos 404 / Boutersem archive-only / Maaseik city GE 404 / Bierbeek 404 still no fetchable JR2025. APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas official pages 403 / Foleon leftover slugs redirect already-mined Hooibeekhoeve — not taken. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / Vlabinvest 1327 / Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320. Not an every-10 tick.
- EUR strong (primary BBC J2/J4/J5/T2/T4/T5): assets **371.940** (was 272.775); cash **22.726** DROP vs 125.237; ST recv **346.124** all ruil JUMP vs 145.188; voorraden **0**; fixed **3.090**; FVA **3.090** (EVA **0** + IGS **1.250** new + other **1.840**); MVA **0** (was 510); IVA **0**; schulden **46.571** all ST (voorzieningen **22.572** + non-fin ruil **23.999**); LT **0**; fin debt T4 **0**; equity **325.369**; cum surplus **278.004**; cap-subs **0**; overig nettoactief **47.365**; expl **+89.760** (ontv **896.089** / uitg **806.329**); invest **−1.250**; fin **0**; BBR year **+88.510**; cum BBR **344.851**; AFM/gecorr **+89.760**; PnL **+88.032**; pers J5/T2 **397.252**; VTE unpublished; werksub granted **0**; werksub received J5=T2 **273.451** (alg **0**; spec **273.451** all gemeente); ops rev **288.474**; other ops **334.164**; goederen J5=T2 **390.747**; 29 panden YE2025.
- CSVs: sources+4/entities+1/budgets+31/commitments+1/leaderboard+1 + FOI ready `gap_bvk_cash_drop_0_10m_strecv_0_35m_citysub_0_27m_vte_l5` (not sent); rq_1335=done; spawn rq_1336; ticks=1335. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (WV BVK leftover zorg live BBC). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1336 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1335 write done")


if __name__ == "__main__":
    main()

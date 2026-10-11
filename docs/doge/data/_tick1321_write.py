# -*- coding: utf-8 -*-
"""Tick 1321 — APB Hooibeekhoeve JR2025 leftover sister APB residual.
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

TICK = "1321"
UTC = "2026-08-17T18:50:00Z"
ENT = "apb_hbh"
HIER = "Vlaanderen>Provincies>Antwerpen>APB>Hooibeekhoeve"
GAP = "gap_hbh_st_recv_2_82m_werksub_j5t2_1_02m_l5"
SRC = "src_hbh_jr2025_pdf"
SRC2 = "src_hbh_jaarverslag_2025"
SRC3 = "src_kbo_hbh_0541414606"
SRC4 = "src_hbh_foi_page"
SRC_URL = "https://assets.foleon.com/eu-central-1/de-uploads-7e3kk3/20500/2025-apb_hh.88dc4701a19a.pdf"
SRC2_URL = "https://publicaties.provincieantwerpen.be/hooibeekhoeve-jaarverslag-2025/in-cijfers"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0541414606"
SRC4_URL = "https://www.provincieantwerpen.be/nl/provinciebestuur/werking-provincie/provinciegriffier/inzagerecht"
FOI_EMAIL = "openbaarheid@provincieantwerpen.be"
FOI_POSTAL = "Koningin Elisabethlei 22 2018 Antwerpen"
DRAFT = "docs/doge/foi/drafts/gap_hbh_st_recv_2_82m_werksub_j5t2_1_02m_l5.md"


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
                "title": "APB Hooibeekhoeve jaarrekening 2025 (official BBC text PDF)",
                "url": SRC_URL,
                "publisher": "APB Hooibeekhoeve / Provincie Antwerpen",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1321; Foleon BBC text PDF 0.79MB 27p print 31.03.2026 volgnr 1493199; "
                    "KBO 0541.414.606; assets 5927071.31 cash 2645838.46 ST recv 2815550.26 "
                    "ST pay 2486460.61 BBR +1304472.17 AFM +1338745.36 PnL +114855.68; primary BBC text"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Hooibeekhoeve jaarverslag 2025 in cijfers (official Foleon link)",
                "url": SRC2_URL,
                "publisher": "Provincie Antwerpen",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1321; publicaties.provincieantwerpen.be/hooibeekhoeve-jaarverslag-2025/in-cijfers "
                    "links the same BBC PDF; leftover sister APB of mined provincie Antwerpen"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO APB Hooibeekhoeve 0541.414.606",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1321; KBO 0541.414.606 actief APB since 26.09.2013; "
                    "zetel Hooibeeksedijk 1 2440 Geel since 26.09.2013; 1 VE; "
                    "bestuurder Jinnih Beels since 05.12.2024; NACE 72.109; "
                    "RSZ-werkgever since 01.01.2022; aanbestedende overheid; no KBO e-mail/finance"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Provincie Antwerpen openbaarheid van bestuur (FOI channel)",
                "url": SRC4_URL,
                "publisher": "Provincie Antwerpen",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1321; FOI openbaarheid@provincieantwerpen.be / provinciegriffier; "
                    "Koningin Elisabethlei 22 2018"
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
                "name_nl": "APB Hooibeekhoeve",
                "name_fr": "APB Hooibeekhoeve (centre provincial recherche lait/fourrage)",
                "name_en": "APB Hooibeekhoeve (provincial dairy/fodder research centre)",
                "level": "apb",
                "parent_id": "prov_antwerpen",
                "community_language": "nl",
                "website": "https://www.provincieantwerpen.be/index.php/nl/locaties/hooibeekhoeve",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1321 JR2025 leftover sister APB residual; KBO 0541.414.606; assets 5927071 "
                    "fin debt 0 ST recv 2815550 ST pay 2486460 BBR +1304472 AFM +1338745 "
                    "PnL +114856 cash 2645838 equity 3290611; FOI ready"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_hbh_assets_2025", "2025", "5927071", "YE2025 assets 5927071.31 was 4780837.64; tick1321; primary BBC J4"),
        ("bud_hbh_assets_2024", "2024", "4780838", "YE2024 assets 4780837.64; tick1321; primary BBC J4"),
        ("bud_hbh_cash_2025", "2025", "2645838", "YE2025 cash 2645838.46 was 2327970.37; tick1321; primary BBC J4"),
        ("bud_hbh_cash_2024", "2024", "2327970", "YE2024 cash 2327970.37; tick1321; primary BBC J4"),
        ("bud_hbh_current_2025", "2025", "5630302", "YE2025 vlottende activa 5630301.74; tick1321; primary BBC J4"),
        ("bud_hbh_recv_st_2025", "2025", "2815550", "YE2025 ST recv 2815550.26 (ruil 78922.20 + niet-ruil 2736628.06) was 1968619.19 JUMP; tick1321; primary BBC J4"),
        ("bud_hbh_recv_nietruil_2025", "2025", "2736628", "YE2025 ST niet-ruil recv 2736628.06; tick1321; primary BBC J4"),
        ("bud_hbh_recv_ruil_2025", "2025", "78922", "YE2025 ST ruil recv 78922.20; tick1321; primary BBC J4"),
        ("bud_hbh_inventories_2025", "2025", "159911", "YE2025 voorraden 159910.75; tick1321; primary BBC J4"),
        ("bud_hbh_accruals_act_2025", "2025", "9002", "YE2025 overlopend actief 9002.27; tick1321; primary BBC J4"),
        ("bud_hbh_fixed_2025", "2025", "296770", "YE2025 vaste activa 296769.57 was 322956.62; tick1321; primary BBC J4/T5"),
        ("bud_hbh_fva_2025", "2025", "60610", "YE2025 FVA 60610.00 andere (EVA 0 IGS 0) was 40607.50; tick1321; primary BBC J4/T5"),
        ("bud_hbh_mva_2025", "2025", "236160", "YE2025 MVA 236159.57 leasing 0; tick1321; primary BBC J4"),
        ("bud_hbh_machines_2025", "2025", "210299", "YE2025 machines/uitrusting 210298.71; tick1321; primary BBC J4/T5"),
        ("bud_hbh_schulden_2025", "2025", "2636461", "YE2025 schulden 2636460.61 (ST 2486460.61 + LT voorziening 150000) was 1605082.62; tick1321; primary BBC J4"),
        ("bud_hbh_pay_ruil_2025", "2025", "346696", "YE2025 non-fin ST ruil pay 346696.27 was 486369.28; tick1321; primary BBC J4"),
        ("bud_hbh_accruals_2025", "2025", "2139764", "YE2025 overlopend passief 2139764.34 was 1118713.34 JUMP; tick1321; primary BBC J4"),
        ("bud_hbh_provision_lt_2025", "2025", "150000", "YE2025 LT voorziening andere risico's 150000.00 (niet pensioen / niet fin debt); tick1321; primary BBC J4"),
        ("bud_hbh_fin_debt_2025", "2025", "0", "YE2025 T4 fin debt 0 all years; J4 empty financiële schulden; T2 financing empty; tick1321; primary BBC T4/J4/T2"),
        ("bud_hbh_equity_2025", "2025", "3290611", "YE2025 nettoactief 3290610.70 was 3175755.02; tick1321; primary BBC J4/T5"),
        ("bud_hbh_cum_pnl_2025", "2025", "3129269", "YE2025 gecumuleerd overschot 3129268.95 was 3014413.27; tick1321; primary BBC J4/T5"),
        ("bud_hbh_pnl_2025", "2025", "114856", "2025 J5 PnL +114855.68 (ops +100396.81 / fin +14458.87); tick1321; primary BBC J5"),
        ("bud_hbh_expl_saldo_2025", "2025", "1338745", "2025 expl saldo +1338745.36 (ontv 4147084.84 / uitg 2808339.48); tick1321; primary BBC J2"),
        ("bud_hbh_expl_ontv_2025", "2025", "4147085", "2025 expl ontv 4147084.84; tick1321; primary BBC J2"),
        ("bud_hbh_expl_uitg_2025", "2025", "2808339", "2025 expl uitg 2808339.48; tick1321; primary BBC J2"),
        ("bud_hbh_invest_2025", "2025", "34273", "2025 invest saldo -34273.19 (uitg 14270.69 / ontv -20002.50 FVA); tick1321; primary BBC J2/T2"),
        ("bud_hbh_bbr_2025", "2025", "1304472", "2025 BBR year +1304472.17; tick1321; primary BBC J2"),
        ("bud_hbh_cum_bbr_2025", "2025", "5114692", "YE2025 cum BBR 5114692.45 was 3810220.28; tick1321; primary BBC J2"),
        ("bud_hbh_afm_2025", "2025", "1338745", "2025 AFM +1338745.36 = gecorr AFM; no afl; tick1321; primary BBC J2"),
        ("bud_hbh_pers_2025", "2025", "1718049", "2025 J5/T2 pers 1718049.32; VTE unpublished FOI; tick1321; primary BBC"),
        ("bud_hbh_goods_2025", "2025", "1080616", "2025 J5 goederen/diensten 1080615.69 / T2 1090141.37; tick1321; primary BBC"),
        ("bud_hbh_werksub_in_2025", "2025", "2291212", "2025 J5 werksub ontv 2291211.99 (alg 1000524.00 + spec 1290687.99); tick1321; primary BBC J5"),
        ("bud_hbh_werksub_t2_2025", "2025", "3312704", "2025 T2 werksub kas 3312703.55 (alg provincie 1000524.00 + spec VL 2312179.55); J5/T2 gap 1021491.56 FOI; tick1321; primary BBC T2"),
        ("bud_hbh_werksub_prov_2025", "2025", "1000524", "2025 T2/J5 alg werksub van de provincie 1000524.00; tick1321; primary BBC T2/J5"),
        ("bud_hbh_werksub_spec_vl_2025", "2025", "2312180", "2025 T2 spec werksub Vlaamse overheid 2312179.55 vs J5 spec 1290687.99; tick1321; primary BBC T2/J5"),
        ("bud_hbh_other_ops_2025", "2025", "216794", "2025 J5 andere operationele opbrengsten 216793.58; tick1321; primary BBC J5"),
        ("bud_hbh_ops_rev_2025", "2025", "638864", "2025 J5 opbrengsten uit de werking 638864.49; tick1321; primary BBC J5"),
        ("bud_hbh_costs_2025", "2025", "3046617", "2025 J5 costs 3046616.70; tick1321; primary BBC J5"),
        ("bud_hbh_rev_2025", "2025", "3161472", "2025 J5 opbrengsten 3161472.38; tick1321; primary BBC J5"),
        ("bud_hbh_deprec_2025", "2025", "247808", "2025 J5 afschrijvingen/waardeverminderingen/voorzieningen 247808.24; tick1321; primary BBC J5/T5"),
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
                "commitment_id": "comm_hbh_jr2025_dual",
                "title": "APB Hooibeekhoeve JR2025 leftover APB dual (cash 2.65m / ST recv 2.82m / J5-T2 werksub gap 1.02m)",
                "entity_id": ENT,
                "beneficiary": "VLAIO/PAS dairy-fodder research + provincie Antwerpen dual",
                "legal_basis": "Provinciedecreet APB; BBC; Bestuursdecreet openbaarheid",
                "decision_date": "",
                "start_year": "2025",
                "end_year": "2027",
                "total_envelope_eur": "5927071",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Praktijkonderzoek melkvee/voedergewassen (VLAIO/PAS; Beemdenhoeve afbraak; proefveldoogstmachine 2026; transitietraject)",
                "cut_option": "Publish named ST recv ledger + J5/T2 werksub 1.02m recon + VLAIO/PAS envelopes + VTE; shrink leftover APB if intra-group",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">jr2025_L5",
                "notes": "tick1321; assets 5927071 ST recv 2815550 ST pay 2486460 BBR +1304472 AFM +1338745 PnL +114856; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_hbh_cash_2_65m_recv_2_82m_bbr_1_30m",
                "name": "APB Hooibeekhoeve JR2025 leftover APB: 5.93m assets / 2.65m cash / 2.82m ST recv / BBR +1.30m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">jr2025_L5",
                "annual_cost_eur": "2808339",
                "total_cost_eur": "5927071",
                "tco_notes": "Leftover dual APB shell: assets 5.93m / cash 2.65m / equity 3.29m; expl uitg 2.81m; J5/T2 werksub gap 1.02m; do not treat 5.93m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "VLAIO/PAS dairy-fodder research + provincie Antwerpen dual",
                "stated_goal": "Praktijkonderzoek melkvee/voedergewassen (transitietraject / Beemdenhoeve)",
                "measured_outcome": "Official BBC PDF 2026-08-17: BBR +1.304m / AFM +1.339m / PnL +0.115m; cash 2.65m; ST recv 2.82m JUMP; J5 werksub 2.291m vs T2 3.313m; VTE unpublished",
                "absurdity_score": "5.8",
                "cost_score": "4.4",
                "difficulty": "3.0",
                "priority_index": "5.1",
                "cut_proposal": "Publish named ST recv + J5/T2 werksub recon + VLAIO/PAS envelopes; shrink leftover APB if intra-group",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1321; leftover sister APB of mined provincie Antwerpen; FOI ready not sent; not TE-additive of 348bn",
            }
        ],
    )
    print("leaderboard", n)

    n = append_rows(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": HIER + ">jr2025_L5",
                "entity_id": ENT,
                "what_is_missing": (
                    "Named counterparties behind ST recv 2815550.26 (ruil 78922.20 + niet-ruil 2736628.06) "
                    "and ST non-fin ruil pay 346696.27 + accruals 2139764.34 + recon J5 werksub 2291211.99 "
                    "vs T2 3312703.55 (gap 1021491.56) and named VLAIO/PAS / VL-spec 2312179.55 envelopes "
                    "+ VTE behind pers 1718049.32 + LT voorziening andere risico's 150000 + FVA mut +20002.50 "
                    "+ provincieraad vaststelling JR2025 + NBB non-filing legal basis"
                ),
                "why_it_matters": (
                    "Leftover unmapped sister APB of already-mined provincie Antwerpen after honest residual "
                    "dual hunt (KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 done). KBO 0541.414.606 active. "
                    "Official BBC PDF now downloads (Foleon). 5.93m leftover APB shell with cash 2.65m, "
                    "ST recv JUMP to 2.82m, and J5/T2 werksub gap 1.02m. Sister leftover APBs PSES/GKC/HC/KampC now mined. "
                    "Do not invent euros."
                ),
                "priority": "7",
                "recipient_body": "APB Hooibeekhoeve / Provincie Antwerpen / provinciegriffier",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_hbh_jr2025_dual",
                "linked_leaderboard_id": "lb_hbh_cash_2_65m_recv_2_82m_bbr_1_30m",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; sourced euros from primary BBC",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1321",
        "title": "APB Hooibeekhoeve JR2025 dual residual leftover APB",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: APB Hooibeekhoeve JR2025 leftover sister APB after honest hunt; "
            "KBO 0541.414.606; official BBC PDF downloads; assets 5.93m / cash 2.65m / ST recv 2.82m / "
            "BBR +1.30m / AFM +1.34m / PnL +0.11m; FOI ready"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T18:35:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1321 APB Hooibeekhoeve JR2025 leftover sister APB residual; KBO 0541.414.606; "
            "assets 5927071 ST recv 2815550 ST pay 2486460 BBR +1304472 AFM +1338745 "
            "PnL +114856; FOI ready not sent; next rq_1322 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1322",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1321 done including APB Hooibeekhoeve 1321 leftover sister APB / "
            "APB KampC 1320 leftover sister APB + every-10 / APB Havencentrum 1319 leftover sister APB / "
            "APB GKC 1318 leftover sister APB / APB PSES 1317 leftover APB / Stad+OCMW Ranst 1316 FOI-unpublished / "
            "Stad+OCMW Lievegem 1315 FOI-TLS / AGB Sport Hulshout 1314 FOI-unpublished / AGB Merchtem 1313 FOI-unpublished / "
            "AGBIM Maaseik 1312 / AGB Maaseik 1311 / APB VERA 1310); prefer other unmined AGB/zorg/EVA with direct "
            "PDF (provincie Antwerpen leftover sister APBs PSES/GKC/HC/KampC/Hooibeekhoeve now mined; "
            "APB POA listed on provincieantwerpen.be JR2025 28.05.2026 but site 403 — take only if a Foleon/direct PDF downloads; "
            "AGB Blankenberge only if a PDF actually downloads); "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined APB Hooibeekhoeve 1321 / APB KampC 1320 / APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / "
            "Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 "
            "(FOI TLS) / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / "
            "APB VERA 1310 / EVA Hoeve Holleken 1309 / Stad+OCMW Beerse 1308 / AGB Beerse 1307 / "
            "Ternat / Oostkamp / Wetteren / Poperinge / Haacht / Bilzen-Hoeselt / AGB Sport Geel / Zwevegem; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 (Foleon OK); not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1321 after APB Hooibeekhoeve JR2025 leftover sister APB; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1321", rq_new, rq_spawn)
    print("research_queue 1321", found, "spawned_1322", spawned)

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
                "last_unit_id": "rq_1321",
                "ticks_completed": "1321",
                "paused": "no",
                "notes": (
                    "tick1321 APB Hooibeekhoeve JR2025 leftover sister APB residual; KBO 0541.414.606; "
                    "assets 5.93m cash 2.65m ST recv 2.82m ST pay 2.49m BBR +1.30m AFM +1.34m PnL +0.11m; "
                    "FOI ready; next rq_1322 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = f"""
### Tick 1321 - 2026-08-17 - rq_1321 APB Hooibeekhoeve dual residual leftover sister APB
- Unit: APB Hooibeekhoeve JR2025 leftover sister APB/EVA of already-mined provincie Antwerpen after residual dual hunt (KBO **0541.414.606**; official BBC text PDF on Foleon 27p / 0.79MB; print **31.03.2026**; volgnr **1493199**; Jnl. via CSrapportaal). PREFER leftover AGB/zorg/EVA/IGS/other-province APB: first leftover Foleon APB still unmined after PSES/GKC/HC/KampC. Distinct from already-mined APB KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 / APB VERA 1310 / Westtoer / APB Mercator. KBO zetel Hooibeeksedijk 1 2440 Geel since 26.09.2013. Bestuurder Jinnih Beels since 05.12.2024. NACE 72.109; RSZ-werkgever since 01.01.2022; aanbestedende overheid; 1 VE; no KBO e-mail. APB states not an onderneming — no NBB filing. Praktijkonderzoek melkvee/voedergewassen; 3 nieuwe VLAIO-projecten eind 2025; afbraak Beemdenhoeve; proefveldoogstmachine gunning 2025 / aankoop 2026; transitietraject. Hunt leftover AGB first: AGB Blankenberge official still **JR2019-only** (unmined, no JR2025 PDF); AGB Bornem / AGB De Kluize already FOI — no new PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek still no fetchable JR2025. APB POA listed on provincieantwerpen.be (JR2025 28.05.2026) but site 403 from this box — left for later if a Foleon/direct PDF downloads. provincieantwerpen.be 403 (Foleon OK). Skip already-mined KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 / Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313. Not an every-10 tick.
- EUR strong (primary BBC J2/J4/J5/T2/T4/T5): assets **5.927.071,31** (was 4.780.837,64); cash **2.645.838,46** vs 2.327.970,37; ST recv **2.815.550,26** (ruil **78.922,20** + niet-ruil **2.736.628,06**) JUMP vs 1.968.619,19; voorraden **159.910,75**; fixed **296.769,57**; FVA **60.610,00** (EVA **0** + IGS **0**); MVA **236.159,57** leasing **0**; IVA **0**; schulden **2.636.460,61**; ST **2.486.460,61** (non-fin ruil **346.696,27** + accruals **2.139.764,34** JUMP); LT voorziening andere risico's **150.000,00** (niet pensioen / niet fin debt); fin debt T4 **0**; equity **3.290.610,70**; cum surplus **3.129.268,95**; expl **+1.338.745,36** (ontv **4.147.084,84** / uitg **2.808.339,48**); invest **−34.273,19**; fin **0**; BBR year **+1.304.472,17**; cum BBR **5.114.692,45**; AFM/gecorr **+1.338.745,36**; PnL **+114.855,68**; pers J5/T2 **1.718.049,32**; werksub granted **0**; werksub received J5 **2.291.211,99** vs T2 **3.312.703,55** (gap **1.021.491,56**; T2 spec VL **2.312.179,55**); other ops **216.793,58**. VTE unpublished.
- CSVs: sources+4/entities+1/budgets+40/commitments+1/leaderboard+1 + FOI ready `{GAP}` (not sent); rq_1321=done; spawn rq_1322; ticks=1321. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (APB Hooibeekhoeve leftover sister APB). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1322 residual dual L5 VL JR2025 hole_fill (provincie Antwerpen leftover sister APBs PSES/GKC/HC/KampC/Hooibeekhoeve now mined; APB POA listed but provincieantwerpen.be 403 — take only if a Foleon/direct PDF downloads; leftover AGB Blankenberge only if a PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 / Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1321 write done")


if __name__ == "__main__":
    main()

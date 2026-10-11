# -*- coding: utf-8 -*-
"""Tick 1322 — EVA Proefbedrijf Pluimveehouderij JR2025 leftover EVA residual.
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

TICK = "1322"
UTC = "2026-08-17T18:15:00Z"
ENT = "eva_pv"
HIER = "Vlaanderen>Provincies>Antwerpen>EVA>ProefbedrijfPluimveehouderij"
GAP = "gap_evapv_st_recv_4_46m_cash_4_08m_werksub_2_78m_l5"
SRC = "src_evapv_jr2025_pdf"
SRC2 = "src_evapv_jaarverslag_2025"
SRC3 = "src_kbo_evapv_0841556855"
SRC4 = "src_evapv_foi_page"
SRC_URL = "https://assets.foleon.com/eu-central-1/de-uploads-7e3kk3/20500/2025-eva_pv.d4006ac9491e.pdf"
SRC2_URL = "https://publicaties.provincieantwerpen.be/proefbedrijf-pluimveehouderij-jaarverslag-2025/in-cijfers"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0841556855"
SRC4_URL = "https://www.provincieantwerpen.be/nl/provinciebestuur/werking-provincie/provinciegriffier/inzagerecht"
FOI_EMAIL = "openbaarheid@provincieantwerpen.be"
FOI_POSTAL = "Koningin Elisabethlei 22 2018 Antwerpen"
DRAFT = "docs/doge/foi/drafts/gap_evapv_st_recv_4_46m_cash_4_08m_werksub_2_78m_l5.md"


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
                "title": "EVA Proefbedrijf Pluimveehouderij jaarrekening 2025 (official BBC text PDF)",
                "url": SRC_URL,
                "publisher": "EVA Proefbedrijf Pluimveehouderij / Provincie Antwerpen",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1322; Foleon BBC text PDF 0.24MB 4p print 01.04.2026 volgnr 884942 J1/J2/J4/J5; "
                    "KBO 0841.556.855; assets 8632319.20 cash 4080815.16 ST recv 4459398.65 "
                    "ST pay 4665561.28 BBR +1170804.00 AFM +1183000.15 PnL +1052154.66; primary BBC text"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Proefbedrijf Pluimveehouderij jaarverslag 2025 in cijfers (official Foleon link)",
                "url": SRC2_URL,
                "publisher": "Provincie Antwerpen",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1322; publicaties.provincieantwerpen.be/proefbedrijf-pluimveehouderij-jaarverslag-2025/in-cijfers "
                    "links the same BBC PDF; leftover sister EVA of mined provincie Antwerpen"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO EVA-vzw Proefbedrijf Pluimveehouderij 0841.556.855",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1322; KBO 0841.556.855 actief VZW since 25.11.2011 afkorting PV; "
                    "zetel Poiel 77 2440 Geel since 25.11.2011; 1 VE; "
                    "bestuurder provincie Antwerpen 0207.725.597 since 25.11.2011; NACE 72.109; "
                    "RSZ-werkgever since 01.01.2012; BTW since 01.06.2012; aanbestedende overheid; no KBO e-mail/finance"
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
                    "tick1322; FOI openbaarheid@provincieantwerpen.be / provinciegriffier Maarten Puls; "
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
                "name_nl": "EVA Proefbedrijf Pluimveehouderij (vzw PV)",
                "name_fr": "EVA Proefbedrijf Pluimveehouderij (centre provincial recherche volaille)",
                "name_en": "EVA Proefbedrijf Pluimveehouderij (provincial poultry research centre)",
                "level": "eva",
                "parent_id": "prov_antwerpen",
                "community_language": "nl",
                "website": "https://provincieantwerpen.be/nl/locaties/proefbedrijf-pluimveehouderij",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1322 JR2025 leftover sister EVA residual; KBO 0841.556.855; assets 8632319 "
                    "fin debt 0 ST recv 4459398 ST pay 4665561 BBR +1170804 AFM +1183000 "
                    "PnL +1052155 cash 4080815 equity 3937491; FOI ready"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_evapv_assets_2025", "2025", "8632319", "YE2025 assets 8632319.20 was 7848965.54; tick1322; primary BBC J4"),
        ("bud_evapv_assets_2024", "2024", "7848966", "YE2024 assets 7848965.54; tick1322; primary BBC J4"),
        ("bud_evapv_cash_2025", "2025", "4080815", "YE2025 cash 4080815.16 was 2883307.11 JUMP; tick1322; primary BBC J4"),
        ("bud_evapv_cash_2024", "2024", "2883307", "YE2024 cash 2883307.11; tick1322; primary BBC J4"),
        ("bud_evapv_current_2025", "2025", "8587753", "YE2025 vlottende activa 8587753.31; tick1322; primary BBC J4"),
        ("bud_evapv_recv_st_2025", "2025", "4459399", "YE2025 ST recv 4459398.65 (ruil 417633.02 + niet-ruil 4041765.63) was 4788369.09; tick1322; primary BBC J4"),
        ("bud_evapv_recv_nietruil_2025", "2025", "4041766", "YE2025 ST niet-ruil recv 4041765.63; tick1322; primary BBC J4"),
        ("bud_evapv_recv_ruil_2025", "2025", "417633", "YE2025 ST ruil recv 417633.02 JUMP vs 157981.63; tick1322; primary BBC J4"),
        ("bud_evapv_inventories_2025", "2025", "35590", "YE2025 voorraden 35589.93; tick1322; primary BBC J4"),
        ("bud_evapv_accruals_act_2025", "2025", "11950", "YE2025 overlopend actief 11949.57; tick1322; primary BBC J4"),
        ("bud_evapv_fixed_2025", "2025", "44566", "YE2025 vaste activa 44565.89 was 68609.89; tick1322; primary BBC J4"),
        ("bud_evapv_fva_2025", "2025", "149", "YE2025 FVA 148.74 andere (EVA 0 IGS 0); tick1322; primary BBC J4"),
        ("bud_evapv_mva_2025", "2025", "44417", "YE2025 MVA 44417.15 leasing 0; tick1322; primary BBC J4"),
        ("bud_evapv_machines_2025", "2025", "44417", "YE2025 machines/uitrusting 44417.15; tick1322; primary BBC J4"),
        ("bud_evapv_schulden_2025", "2025", "4694828", "YE2025 schulden 4694828.13 (ST 4665561.28 + LT voorziening 29266.85) was 4963629.13; tick1322; primary BBC J4"),
        ("bud_evapv_pay_ruil_2025", "2025", "2332871", "YE2025 non-fin ST ruil pay 2332871.21 was 3082693.74; tick1322; primary BBC J4"),
        ("bud_evapv_accruals_2025", "2025", "2315346", "YE2025 overlopend passief 2315346.46 was 1875117.48 JUMP; tick1322; primary BBC J4"),
        ("bud_evapv_provision_lt_2025", "2025", "29267", "YE2025 LT voorziening andere risico's 29266.85 (niet pensioen / J4 fin debt empty); tick1322; primary BBC J4"),
        ("bud_evapv_fin_debt_2025", "2025", "0", "YE2025 J4 financiële schulden empty ST+LT; T4 unpublished; tick1322; primary BBC J4"),
        ("bud_evapv_equity_2025", "2025", "3937491", "YE2025 nettoactief 3937491.07 was 2885336.41; tick1322; primary BBC J4"),
        ("bud_evapv_cum_pnl_2025", "2025", "3812491", "YE2025 gecumuleerd overschot 3812491.07 was 2760336.41; tick1322; primary BBC J4"),
        ("bud_evapv_pnl_2025", "2025", "1052155", "2025 J5 PnL +1052154.66 (ops +1026139.04 / fin +26015.62); tick1322; primary BBC J5"),
        ("bud_evapv_expl_saldo_2025", "2025", "1183000", "2025 expl saldo +1183000.15 (ontv 5270494.68 / uitg 4087494.53); tick1322; primary BBC J2"),
        ("bud_evapv_expl_ontv_2025", "2025", "5270495", "2025 expl ontv 5270494.68; tick1322; primary BBC J2"),
        ("bud_evapv_expl_uitg_2025", "2025", "4087495", "2025 expl uitg 4087494.53; tick1322; primary BBC J2"),
        ("bud_evapv_invest_2025", "2025", "12196", "2025 invest saldo -12196.15 (uitg 12196.15); tick1322; primary BBC J2"),
        ("bud_evapv_bbr_2025", "2025", "1170804", "2025 BBR year +1170804.00; tick1322; primary BBC J2"),
        ("bud_evapv_cum_bbr_2025", "2025", "4350240", "YE2025 cum BBR 4350239.94 was 3179435.94; tick1322; primary BBC J2"),
        ("bud_evapv_afm_2025", "2025", "1183000", "2025 AFM +1183000.15 = gecorr AFM; no afl; tick1322; primary BBC J2"),
        ("bud_evapv_pers_2025", "2025", "1807841", "2025 J5 pers 1807841.37; VTE unpublished FOI; tick1322; primary BBC J5"),
        ("bud_evapv_goods_2025", "2025", "2344430", "2025 J5 goederen/diensten 2344429.56; tick1322; primary BBC J5"),
        ("bud_evapv_werksub_in_2025", "2025", "2776247", "2025 J5 werksub ontv 2776246.71 (all algemene; spec empty); T2 unpublished FOI; tick1322; primary BBC J5"),
        ("bud_evapv_other_ops_2025", "2025", "154854", "2025 J5 andere operationele opbrengsten 154854.46; tick1322; primary BBC J5"),
        ("bud_evapv_ops_rev_2025", "2025", "2313019", "2025 J5 opbrengsten uit de werking 2313019.35; tick1322; primary BBC J5"),
        ("bud_evapv_costs_2025", "2025", "4218340", "2025 J5 costs 4218340.02; tick1322; primary BBC J5"),
        ("bud_evapv_rev_2025", "2025", "5270495", "2025 J5 opbrengsten 5270494.68; tick1322; primary BBC J5"),
        ("bud_evapv_deprec_2025", "2025", "65507", "2025 J5 afschrijvingen/waardeverminderingen/voorzieningen 65507.00; tick1322; primary BBC J5"),
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
                "commitment_id": "comm_evapv_jr2025_dual",
                "title": "EVA Proefbedrijf Pluimveehouderij JR2025 leftover EVA dual (cash 4.08m / ST recv 4.46m / werksub 2.78m)",
                "entity_id": ENT,
                "beneficiary": "VLAIO/Interreg/LEADER poultry research + provincie Antwerpen dual",
                "legal_basis": "Bestuursdecreet openbaarheid; vzw-wetboek; BBC provincial EVA",
                "decision_date": "",
                "start_year": "2025",
                "end_year": "2027",
                "total_envelope_eur": "8632319",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Praktijkonderzoek legkippen/vleeskuikens (RAMBO Interreg; athletic chicks VLAIO; LEADER; RAMMONIA; 2026 MICROHEN/Chickwell/Broilermap)",
                "cut_option": "Publish named ST recv ledger + werksub 2.78m envelopes + T2/T4/T5 + VTE; shrink leftover EVA if intra-group with Hooibeekhoeve",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">jr2025_L5",
                "notes": "tick1322; assets 8632319 ST recv 4459399 ST pay 4665561 BBR +1170804 AFM +1183000 PnL +1052155; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_evapv_cash_4_08m_recv_4_46m_bbr_1_17m",
                "name": "EVA Proefbedrijf Pluimveehouderij JR2025 leftover EVA: 8.63m assets / 4.08m cash / 4.46m ST recv / BBR +1.17m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">jr2025_L5",
                "annual_cost_eur": "4087495",
                "total_cost_eur": "8632319",
                "tco_notes": "Leftover dual EVA shell: assets 8.63m / cash 4.08m JUMP / equity 3.94m; expl uitg 4.09m; werksub 2.78m; sister of mined Hooibeekhoeve BD30; do not treat 8.63m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "VLAIO/Interreg/LEADER poultry research + provincie Antwerpen dual",
                "stated_goal": "Praktijkonderzoek legkippen/vleeskuikens (RAMBO / athletic chicks / LEADER)",
                "measured_outcome": "Official BBC PDF 2026-08-17: BBR +1.171m / AFM +1.183m / PnL +1.052m; cash 4.08m JUMP; ST recv 4.46m; J5 werksub 2.776m all algemene; T2/T4/T5 unpublished; VTE unpublished",
                "absurdity_score": "6.0",
                "cost_score": "4.8",
                "difficulty": "3.0",
                "priority_index": "5.4",
                "cut_proposal": "Publish named ST recv + werksub envelopes + T2/T4/T5; shrink leftover EVA if intra-group with Hooibeekhoeve",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1322; leftover sister EVA of mined provincie Antwerpen; FOI ready not sent; not TE-additive of 348bn",
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
                    "Named counterparties behind ST recv 4459398.65 (ruil 417633.02 + niet-ruil 4041765.63) "
                    "and ST non-fin ruil pay 2332871.21 + accruals 2315346.46 + named J5 algemene werksub 2776246.71 "
                    "(provincie / VLAIO / Interreg / LEADER envelopes) + unpublished T2/T4/T5 BBC schemas "
                    "+ VTE behind pers 1807841.37 + LT voorziening andere risico's 29266.85 "
                    "+ AV/provincieraad vaststelling JR2025 + NBB deposit or VZW non-filing legal basis"
                ),
                "why_it_matters": (
                    "Leftover unmapped sister EVA of already-mined provincie Antwerpen after honest residual "
                    "dual hunt (Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 done). "
                    "KBO 0841.556.855 active VZW. Official BBC PDF now downloads (Foleon 4p). 8.63m leftover EVA shell "
                    "with cash JUMP to 4.08m, ST recv 4.46m, and werksub 2.78m. Same BD30 family as Hooibeekhoeve. "
                    "Do not invent euros."
                ),
                "priority": "7",
                "recipient_body": "EVA Proefbedrijf Pluimveehouderij / Provincie Antwerpen / provinciegriffier",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_evapv_jr2025_dual",
                "linked_leaderboard_id": "lb_evapv_cash_4_08m_recv_4_46m_bbr_1_17m",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; sourced euros from primary BBC",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1322",
        "title": "EVA Proefbedrijf Pluimveehouderij JR2025 dual residual leftover EVA",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: EVA Proefbedrijf Pluimveehouderij JR2025 leftover sister EVA after honest hunt; "
            "KBO 0841.556.855; official BBC PDF downloads; assets 8.63m / cash 4.08m / ST recv 4.46m / "
            "BBR +1.17m / AFM +1.18m / PnL +1.05m; FOI ready"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T18:50:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1322 EVA Proefbedrijf Pluimveehouderij JR2025 leftover sister EVA residual; KBO 0841.556.855; "
            "assets 8632319 ST recv 4459399 ST pay 4665561 BBR +1170804 AFM +1183000 "
            "PnL +1052155; FOI ready not sent; next rq_1323 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1323",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1322 done including EVA Proefbedrijf Pluimveehouderij 1322 leftover sister EVA / "
            "APB Hooibeekhoeve 1321 leftover sister APB / APB KampC 1320 leftover sister APB + every-10 / "
            "APB Havencentrum 1319 leftover sister APB / APB GKC 1318 leftover sister APB / APB PSES 1317 leftover APB / "
            "Stad+OCMW Ranst 1316 FOI-unpublished / Stad+OCMW Lievegem 1315 FOI-TLS / AGB Sport Hulshout 1314 FOI-unpublished / "
            "AGB Merchtem 1313 FOI-unpublished / AGBIM Maaseik 1312 / AGB Maaseik 1311 / APB VERA 1310); prefer other unmined "
            "AGB/zorg/EVA with direct PDF (provincie Antwerpen leftover sister APBs PSES/GKC/HC/KampC/Hooibeekhoeve "
            "and leftover EVA Pluimveehouderij now mined; "
            "APB POA listed on provincieantwerpen.be JR2025 28.05.2026 but site 403 — take only if a Foleon/direct PDF downloads; "
            "AGB Blankenberge only if a PDF actually downloads); "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined EVA Proefbedrijf Pluimveehouderij 1322 / APB Hooibeekhoeve 1321 / APB KampC 1320 / "
            "APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / "
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
        "notes": "spawned tick1322 after EVA Proefbedrijf Pluimveehouderij JR2025 leftover sister EVA; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1322", rq_new, rq_spawn)
    print("research_queue 1322", found, "spawned_1323", spawned)

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
                "last_unit_id": "rq_1322",
                "ticks_completed": "1322",
                "paused": "no",
                "notes": (
                    "tick1322 EVA Proefbedrijf Pluimveehouderij JR2025 leftover sister EVA residual; KBO 0841.556.855; "
                    "assets 8.63m cash 4.08m ST recv 4.46m ST pay 4.67m BBR +1.17m AFM +1.18m PnL +1.05m; "
                    "FOI ready; next rq_1323 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = f"""
### Tick 1322 - 2026-08-17 - rq_1322 EVA Proefbedrijf Pluimveehouderij dual residual leftover sister EVA
- Unit: EVA Proefbedrijf Pluimveehouderij JR2025 leftover sister EVA of already-mined provincie Antwerpen after residual dual hunt (KBO **0841.556.855**; official BBC text PDF on Foleon 4p / 0.24MB; print **01.04.2026**; volgnr **884942**; schemas J1/J2/J4/J5 only). PREFER leftover AGB/zorg/EVA/IGS/other-province APB: first leftover Foleon EVA still unmined after PSES/GKC/HC/KampC/Hooibeekhoeve. Distinct from already-mined APB Hooibeekhoeve 1321 (same BD30 family, different KBO/zetel) / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 / APB VERA 1310 / Westtoer / APB Mercator. KBO zetel Poiel 77 2440 Geel since 25.11.2011. VZW afkorting PV. Bestuurder provincie Antwerpen 0207.725.597 since 25.11.2011. NACE 72.109; RSZ-werkgever since 01.01.2012; aanbestedende overheid; 1 VE; no KBO e-mail. Praktijkonderzoek legkippen/vleeskuikens; RAMBO Interreg / athletic chicks VLAIO / LEADER / RAMMONIA; 2026 pipeline MICROHEN/Chickwell/Broilermap. Hunt leftover AGB first: AGB Blankenberge official still **JR2019-only** (city JR2025 listed 25.06.2026 as lokaal bestuur, not AGB); AGB Bornem / AGB De Kluize already FOI — no new PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek still no fetchable JR2025. APB POA listed on provincieantwerpen.be (JR2025 28.05.2026) but no Foleon/direct PDF downloaded — listing only, internals not invented. provincieantwerpen.be 403 (Foleon OK). Skip already-mined Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 / Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313. Not an every-10 tick.
- EUR strong (primary BBC J2/J4/J5): assets **8.632.319,20** (was 7.848.965,54); cash **4.080.815,16** JUMP vs 2.883.307,11; ST recv **4.459.398,65** (ruil **417.633,02** JUMP + niet-ruil **4.041.765,63**); voorraden **35.589,93**; fixed **44.565,89**; FVA **148,74** (EVA **0** + IGS **0**); MVA **44.417,15** leasing **0**; IVA **0**; schulden **4.694.828,13**; ST **4.665.561,28** (non-fin ruil **2.332.871,21** + accruals **2.315.346,46** JUMP); LT voorziening andere risico's **29.266,85** (niet pensioen / J4 fin debt empty); fin debt J4 **0**; equity **3.937.491,07**; cum surplus **3.812.491,07**; expl **+1.183.000,15** (ontv **5.270.494,68** / uitg **4.087.494,53**); invest **−12.196,15**; fin **0**; BBR year **+1.170.804,00**; cum BBR **4.350.239,94**; AFM/gecorr **+1.183.000,15**; PnL **+1.052.154,66**; pers J5 **1.807.841,37**; werksub granted **0**; werksub received J5 **2.776.246,71** (all algemene; T2 unpublished); other ops **154.854,46**; werking **2.313.019,35**. VTE unpublished. T2/T4/T5 unpublished.
- CSVs: sources+4/entities+1/budgets+37/commitments+1/leaderboard+1 + FOI ready `{{GAP}}` (not sent); rq_1322=done; spawn rq_1323; ticks=1322. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (EVA Proefbedrijf Pluimveehouderij leftover sister EVA). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1323 residual dual L5 VL JR2025 hole_fill (provincie Antwerpen leftover sister APBs PSES/GKC/HC/KampC/Hooibeekhoeve and leftover EVA Pluimveehouderij now mined; APB POA listed but no Foleon/direct PDF — take only if a PDF downloads; leftover AGB Blankenberge only if a PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 / Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313 unless a fetchable JR appears).
""".replace("{GAP}", GAP)
    # fix the accidental double-brace if any
    log_entry = log_entry.replace("{{GAP}}", GAP)
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1322 write done")


if __name__ == "__main__":
    main()

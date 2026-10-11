# -*- coding: utf-8 -*-
"""Tick 1325 — APB Vonk leftover other-province APB residual, JR2025 BBC euros.
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

TICK = "1325"
UTC = "2026-08-17T18:55:00Z"
ENT = "apb_vonk"
HIER = "Vlaanderen>Provincies>WestVlaanderen>APB>Vonk"
GAP = "gap_vonk_liq_cash_0_96m_bbr_0_97m_vte_l5"
SRC = "src_vonk_jr2025_pdf"
SRC2 = "src_vonk_kenniswest"
SRC3 = "src_kbo_vonk_0666654175"
SRC4 = "src_vonk_foi_page"
SRC_URL = "https://www.west-vlaanderen.be/sites/default/files/2026-04/JaarrekeningBBC2025.pdf"
SRC2_URL = "https://www.kenniswest.be/organisatie/vonk-apb-brugge/20494"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0666654175"
SRC4_URL = "https://www.west-vlaanderen.be/over-west-vlaanderen/contact/openbaarheid-van-bestuur"
FOI_EMAIL = "griffie@west-vlaanderen.be"
FOI_POSTAL = "Koning Leopold III-laan 41 8200 Sint-Andries"
DRAFT = "docs/doge/foi/drafts/gap_vonk_liq_cash_0_96m_bbr_0_97m_vte_l5.md"


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
                "title": "APB Vonk jaarrekening 2025 BBC (official west-vlaanderen.be PDF)",
                "url": SRC_URL,
                "publisher": "APB Vonk / Provincie West-Vlaanderen",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1325; HTTP 200 PDF 2.21 MB; Jnl Budg 7318 Alg 2025085128; "
                    "9de werkjaar; vaststelling vereffenaar 31.03.2026; PR 14.04.2026; "
                    "primary J1-J5/T2-T5 euros; T5 print 17.02.2026"
                ),
            },
            {
                "source_id": SRC2,
                "title": "KennisWest organisation page APB Vonk (absorbed as Kennisdelen 01.01.2026)",
                "url": SRC2_URL,
                "publisher": "Provincie West-Vlaanderen / KennisWest",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1325; HTTP 200; Gestopt / overgenomen door Kennisdelen Kennishub "
                    "01.01.2026; KBO 0666.654.175; zetel Koning Leopold III-laan 41 8200 Brugge"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Autonoom provinciebedrijf Vonk 0666.654.175",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1325; KBO 0666.654.175 Actief / normale toestand since 22.09.2016; "
                    "zetel Koning Leopold III-laan 41 8200 Brugge; 0 VE; APB; "
                    "e-mail info@apbvonk.be; tel 050/40 34 50; bestuurder Kelly Detavernier "
                    "since 23.01.2025; no KBO finance/NACE; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Provincie West-Vlaanderen openbaarheid van bestuur / griffie",
                "url": SRC4_URL,
                "publisher": "Provincie West-Vlaanderen",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1325; FOI griffie@west-vlaanderen.be + info@apbvonk.be; "
                    "postal Koning Leopold III-laan 41 8200 Sint-Andries; "
                    "vereffenaar Regis De Brulle (BBC toelichting punt 14)"
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
                "name_nl": "Autonoom provinciebedrijf Vonk (APB Vonk)",
                "name_fr": "Régie provinciale autonome Vonk (APB Vonk)",
                "name_en": "Vonk autonomous provincial company (APB Vonk)",
                "level": "apb",
                "parent_id": "prov_west_vlaanderen",
                "community_language": "nl",
                "website": SRC_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1325 leftover other-province APB residual; KBO 0666.654.175 Actief since 22.09.2016; "
                    "official BBC JR2025 PDF downloads; liquidated 31.12.2025 into provincie Kennisdelen; "
                    "assets 1.024m cash 0.963m BBR +0.164m PnL +0.193m; FOI ready; BD Kelly Detavernier"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_vonk_assets_2025", "2025", "1023918", "2025 assets 1023917.92 was 898278.66; tick1325; primary BBC J4"),
        ("bud_vonk_cash_2025", "2025", "962753", "2025 cash 962752.89 JUMP vs 675448.32; tick1325; primary BBC J4"),
        ("bud_vonk_st_recv_2025", "2025", "60440", "2025 ST recv 60439.57 all ruil; niet-ruil 0; tick1325; primary BBC J4"),
        ("bud_vonk_fixed_2025", "2025", "725", "2025 fixed 725.46 MVA gemeenschapsgoederen; FVA 0 IVA 0 leasing 0; tick1325; primary BBC J4/T5"),
        ("bud_vonk_debt_2025", "2025", "49240", "2025 schulden 49240.10 all ST (ruil 45146.54 + niet-ruil 4093.56); tick1325; primary BBC J4"),
        ("bud_vonk_fin_debt_2025", "2025", "0", "2025 fin debt T4 empty schema = 0; tick1325; primary BBC T4"),
        ("bud_vonk_equity_2025", "2025", "974678", "2025 nettoactief 974677.82 was 782037.41; tick1325; primary BBC J4"),
        ("bud_vonk_cum_surplus_2025", "2025", "-969618", "2025 cum surplus -969618.13 was -1162258.54; tick1325; primary BBC J4"),
        ("bud_vonk_expl_in_2025", "2025", "1234943", "2025 expl ontv 1234943.07; tick1325; primary BBC J2"),
        ("bud_vonk_expl_out_2025", "2025", "1071432", "2025 expl uitg 1071431.55; tick1325; primary BBC J2"),
        ("bud_vonk_expl_2025", "2025", "163512", "2025 expl saldo +163511.52; tick1325; primary BBC J2"),
        ("bud_vonk_invest_2025", "2025", "0", "2025 invest saldo 0 (uitg 0 / ontv 0); tick1325; primary BBC J2/T2"),
        ("bud_vonk_bbr_2025", "2025", "163512", "2025 BBR year +163511.52; tick1325; primary BBC J2"),
        ("bud_vonk_cum_bbr_2025", "2025", "973952", "YE2025 cum BBR 973951.90 was 810440.38; tick1325; primary BBC J2"),
        ("bud_vonk_afm_2025", "2025", "163512", "2025 AFM +163511.52 = gecorr AFM; no afl; tick1325; primary BBC J2"),
        ("bud_vonk_pnl_2025", "2025", "192640", "2025 PnL +192640.41 (ops 189684.71 / fin 2955.70); tick1325; primary BBC J5"),
        ("bud_vonk_pers_2025", "2025", "546230", "2025 J5/T2 pers 546230.37 (niet-vast 526248.06 + andere 19982.31); VTE unpublished FOI; tick1325; primary BBC"),
        ("bud_vonk_goods_t2_2025", "2025", "522402", "2025 T2 goederen/diensten 522401.90; tick1325; primary BBC T2"),
        ("bud_vonk_goods_j5_2025", "2025", "512837", "2025 J5 goederen/diensten 512837.26; tick1325; primary BBC J5"),
        ("bud_vonk_werksub_in_2025", "2025", "297908", "2025 J5=T2 werksub ontv 297907.79 (alg provincie 270533.98 + spec fed 27373.81); tick1325; primary BBC J5/T2"),
        ("bud_vonk_werksub_prov_2025", "2025", "270534", "2025 T2/J5 alg werksub van de provincie 270533.98; tick1325; primary BBC T2/J5"),
        ("bud_vonk_werksub_fed_2025", "2025", "27374", "2025 T2/J5 spec werksub federale overheid 27373.81; tick1325; primary BBC T2/J5"),
        ("bud_vonk_ops_rev_2025", "2025", "929161", "2025 J5 opbrengsten uit de werking 929161.41; tick1325; primary BBC J5"),
        ("bud_vonk_other_ops_2025", "2025", "3420", "2025 J5 andere operationele opbrengsten 3420.23; tick1325; primary BBC J5"),
        ("bud_vonk_costs_2025", "2025", "1041114", "2025 J5 costs 1041114.20; tick1325; primary BBC J5"),
        ("bud_vonk_rev_2025", "2025", "1233755", "2025 J5 opbrengsten 1233754.61; tick1325; primary BBC J5"),
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
                "commitment_id": "comm_vonk_jr2025_liq",
                "title": "APB Vonk JR2025 leftover APB dual (cash 0.96m / BBR 0.97m / liquidated 31.12.2025 into Kennisdelen)",
                "entity_id": ENT,
                "beneficiary": "Provincie West-Vlaanderen / lokale besturen opleidingen (Kennisdelen)",
                "legal_basis": "Provinciedecreet APB; BBC; Bestuursdecreet openbaarheid",
                "decision_date": "2016-09-22",
                "start_year": "2016",
                "end_year": "2025",
                "total_envelope_eur": "1023918",
                "cash_by_year": "",
                "remaining_eur": "973952",
                "status": "ended",
                "evaluation_url": SRC_URL,
                "stated_goal": "Kennispartner lokale besturen WVL — opleidingen/netwerk; absorbed into provincie Kennishub 01.01.2026",
                "cut_option": "Publish vereffeningsrekening + destination of 0.96m cash / 0.97m BBR + VTE + dual provincie absorption lines",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1325; assets 1023918 cash 962753 BBR +163512 PnL +192640; liquidated 31.12.2025; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_vonk_liq_cash_0_96m_bbr_0_97m",
                "name": "APB Vonk JR2025 leftover APB: 1.02m assets / 0.96m cash / BBR +0.16m / liquidated into provincie",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "1071432",
                "total_cost_eur": "1023918",
                "tco_notes": "Leftover dual APB shell liquidated 31.12.2025: assets 1.02m / cash 0.96m / equity 0.97m; expl uitg 1.07m; do not treat 1.02m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Provincie West-Vlaanderen / lokale besturen opleidingen",
                "stated_goal": "Kennispartner lokale besturen WVL — absorbed as Kennisdelen 01.01.2026",
                "measured_outcome": "Official BBC PDF 2026-08-17: BBR +0.164m / AFM +0.164m / PnL +0.193m; cash 0.963m JUMP; fin debt 0; VTE unpublished; vereffenaar Regis De Brulle",
                "absurdity_score": "5.4",
                "cost_score": "3.2",
                "difficulty": "2.5",
                "priority_index": "4.8",
                "cut_proposal": "Publish vereffeningsrekening + cash/BBR destination + VTE + dual provincie absorption; do not recreate APB shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1325; leftover other-province APB of mined provincie West-Vlaanderen; FOI ready not sent; not TE-additive of 348bn",
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
                    "Vereffeningsrekening / destination of cash 962752.89 and cum BBR 973951.90 "
                    "after 31.12.2025 liquidation into provincie Kennisdelen + dual provincie JR2025 "
                    "absorption lines + VTE behind pers 546230.37 + named ST recv 60439.57 + "
                    "NBB filings (consult listings year-end 30.12.2025 / 29.04.2026; consult 403) + "
                    "PR 14.04.2026 goedkeuring and December 2025 ontbinding decision."
                ),
                "why_it_matters": (
                    "Named leftover unmined other-province APB of already-mined provincie West-Vlaanderen "
                    "after honest residual dual hunt. KBO 0666.654.175 Actief. Official BBC PDF now "
                    "downloads. 1.02m leftover APB shell with cash 0.96m JUMP and BBR 0.97m parked "
                    "at liquidation into provincie. APB POA/TPA listed but no PDF bytes; leftover "
                    "cities still no fetchable JR2025. Do not invent euros."
                ),
                "priority": "7",
                "recipient_body": "APB Vonk / vereffenaar / Provincie West-Vlaanderen",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_vonk_jr2025_liq",
                "linked_leaderboard_id": "lb_vonk_liq_cash_0_96m_bbr_0_97m",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; sourced euros from primary BBC; not every-10",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1325",
        "title": "APB Vonk JR2025 dual residual leftover other-province APB",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: APB Vonk leftover other-province APB after honest hunt; KBO 0666.654.175 "
            "Actief; official BBC JR2025 PDF downloads; assets 1.02m / cash 0.96m / BBR +0.16m / "
            "PnL +0.19m; liquidated 31.12.2025 into Kennisdelen; FOI ready"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T18:40:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1325 APB Vonk leftover other-province APB residual; KBO 0666.654.175; "
            "assets 1023918 cash 962753 BBR +163512 PnL +192640; FOI ready not sent; "
            "next rq_1326 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1326",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1325 done including APB Vonk 1325 leftover other-province APB / "
            "APB Campus Vesta 1324 FOI-glossy-not-BBC / AGB Blankenberge 1323 FOI-liquidated JR2019-only / "
            "EVA Proefbedrijf Pluimveehouderij 1322 leftover sister EVA / APB Hooibeekhoeve 1321 leftover sister APB / "
            "APB KampC 1320 leftover sister APB + every-10 / APB Havencentrum 1319 leftover sister APB / "
            "APB GKC 1318 leftover sister APB / APB PSES 1317 leftover APB); "
            "prefer leftover APB Monumentenwacht West-Vlaanderen (also dissolved Dec 2025) only if a BBC/NBB PDF downloads; "
            "APB POA / APB TPA listed on provincieantwerpen.be but no PDF bytes — take only if a real PDF downloads; "
            "APB De Schorre leftover APB — take only if a JR2025 BBC PDF now downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined APB Vonk 1325 / APB Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Proefbedrijf Pluimveehouderij 1322 / "
            "APB Hooibeekhoeve 1321 / APB KampC 1320 / APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / "
            "Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / "
            "AGBIM 1312 / AGB Maaseik 1311 / APB VERA 1310 / Westtoer; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 (Foleon OK); not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1325 after APB Vonk leftover other-province APB; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1325", rq_new, rq_spawn)
    print("research_queue 1325", found, "spawned_1326", spawned)

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
                "last_unit_id": "rq_1325",
                "ticks_completed": "1325",
                "paused": "no",
                "notes": (
                    "tick1325 APB Vonk leftover other-province APB residual; KBO 0666.654.175; "
                    "official BBC JR2025 PDF; assets 1.02m cash 0.96m BBR +0.16m; liquidated 31.12.2025; "
                    "FOI ready; next rq_1326 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1325 - 2026-08-17 - rq_1325 APB Vonk dual residual leftover other-province APB
- Unit: Autonoom provinciebedrijf Vonk leftover other-province APB of already-mined provincie West-Vlaanderen after residual dual hunt (KBO **0666.654.175**; official west-vlaanderen.be BBC PDF 2.21 MB / Jnl Budg **7318** Alg **2025085128**; 9de werkjaar; vaststelling vereffenaar **31.03.2026**; provincieraad **14.04.2026**). PREFER leftover AGB/zorg/EVA/IGS/other-province APB: first leftover other-province APB with a live JR2025 BBC PDF after Antwerpen sister APBs were mined. Distinct from already-mined Westtoer / APB VERA 1310 / APB Mercator / Campus Vesta 1324 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317. KBO zetel Koning Leopold III-laan 41 8200 Brugge since 22.09.2016. Bestuurder Kelly Detavernier since 23.01.2025. 0 VE; e-mail info@apbvonk.be. Absorbed into provincie as sectie **Kennisdelen** (Kennishub) from **01.01.2026**; vereffening 31.12.2025; vereffenaar **Regis De Brulle**. Hunt leftover AGB first: AGB Bornem / AGB De Kluize already FOI — no new PDF. Leftover cities Londerzeel official still JR2022–2024 only / Holsbeek / Zwalm / Wortegem-Petegem / Maarkedal / Linkebeek / Kapellen / Drogenbos / Boutersem / Maaseik GE / Bierbeek still no fetchable JR2025. APB POA listed provincieantwerpen.be JR2025 28.05.2026 but **no PDF bytes**. APB TPA `jaarrekening 25 tpa.pdf` 25.06.2026 — same. APB De Schorre leftover — no JR2025 PDF. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317. Not an every-10 tick.
- EUR strong (primary BBC J2/J4/J5/T2/T4/T5): assets **1.023.917,92** (was 898.278,66); cash **962.752,89** JUMP vs 675.448,32; ST recv **60.439,57** (all ruil); fixed **725,46**; FVA **0** (EVA **0** + IGS **0**); MVA **725,46** leasing **0**; IVA **0**; schulden **49.240,10** all ST; fin debt T4 **0**; equity **974.677,82**; cum surplus **−969.618,13**; overig **1.944.295,95**; expl **+163.511,52** (ontv **1.234.943,07** / uitg **1.071.431,55**); invest **0**; fin **0**; BBR year **+163.511,52**; cum BBR **973.951,90**; AFM/gecorr **+163.511,52**; PnL **+192.640,41**; pers J5/T2 **546.230,37**; werksub granted **0**; werksub received J5=T2 **297.907,79** (alg provincie **270.533,98** + spec fed **27.373,81**); ops rev **929.161,41**; other ops **3.420,23**; goederen T2 **522.401,90** / J5 **512.837,26**. VTE unpublished.
- CSVs: sources+4/entities+1/budgets+26/commitments+1/leaderboard+1 + FOI ready `gap_vonk_liq_cash_0_96m_bbr_0_97m_vte_l5` (not sent); rq_1325=done; spawn rq_1326; ticks=1325. Not a *0 tick — no progress refresh.
- Coverage: residual dual L5 (APB Vonk leftover other-province APB). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1326 residual dual L5 VL JR2025 hole_fill (prefer leftover APB Monumentenwacht West-Vlaanderen only if a BBC/NBB PDF downloads; APB POA / APB TPA / APB De Schorre only if a real PDF downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB Vonk 1325 / Campus Vesta 1324 / AGB Blankenberge 1323 / EVA Pluimveehouderij 1322 / Hooibeekhoeve 1321 / KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1325 write done")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Tick 1374 — leftover MIWA JR2025 official NBB WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10 (next every-10 is 1380).
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1374"
UTC = "2026-08-19T03:40:00Z"
ENT = "igs_miwa"
HIER = "Vlaanderen>OostVlaanderen>IGS>MIWA>MiddenWaasland"
GAP = "gap_miwa_othops_13_95m_diensten_10_57m_fire_l5"
SRC = "src_miwa_jr2025_nbb"
SRC2 = "src_miwa_site"
SRC3 = "src_kbo_miwa_0218239409"
SRC4 = "src_miwa_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00209388.pdf"
SRC2_URL = "https://miwa.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0218239409"
SRC4_URL = "https://miwa.be/contact"
FOI_EMAIL = "info@miwa.be"
FOI_POSTAL = "Vlyminckshoek 12 9100 Sint-Niklaas"
DRAFT = "docs/doge/foi/drafts/gap_miwa_othops_13_95m_diensten_10_57m_fire_l5.md"
COMM = "comm_miwa_jr2025_pnl"
LB = "lb_miwa_othops_13_95m_diensten_10_57m_fire"


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
                "title": "MIWA jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00209388; AV 03.06.2026)",
                "url": SRC_URL,
                "publisher": "MIWA / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1374; official NBB VOL-inb PDF 480kB 50p deposit 2026-00209388 created 29.06.2026 header 25.06.2026; "
                    "leftover IGS OV of Midden-Waasland municipalities; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Callens Vandelanotte NV B00083 / Erik Thuysbaert A01792 7678 signed 11.05.2026; "
                    "oordeel zonder voorbehoud assets 19597553.04 / PnL 32304.94 + vermelding 6.20 brand; "
                    "6.1/6.2.1-6.2.2/6.2.4-6.2.5/6.4.1-6.4.2/6.5.1-6.5.2/6.8/6.15/6.17/6.18.1-6.18.2 not filed; "
                    "6.10 category/geo empty; 740 subsidies 182583 only of othops 13954081; not every-10"
                ),
            },
            {
                "source_id": SRC2,
                "title": "MIWA official site (waste IGS Midden-Waasland)",
                "url": SRC2_URL,
                "publisher": "MIWA Intercommunale",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1374; leftover IGS waste of Sint-Niklaas/Temse/Sint-Gillis-Waas/Stekene/Waasmunster; "
                    "miwa.be has no isolated statutory 2025 balans PDF (citizen flipbook only); statutory 2025 balans is the NBB CDN deposit"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO MIWA 0218.239.409",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1374; KBO 0218.239.409 Actief / normale toestand since 17.04.1978; vervangt 0218.521.501 afgesloten 11.05.2011; "
                    "statutaire naam Opdrachthoudende Vereniging voor Huisvuilverwerking Midden-Waasland since 26.11.2002; "
                    "afkorting MIWA since 19.09.2017; Opdrachthoudende vereniging (Vlaams Gewest) since 17.12.2002; "
                    "zetel Vlyminckshoek 12 9100 Sint-Niklaas since 08.04.2003; 6 VE; "
                    "btw since 01.06.1978; RSZ since 01.01.2022; aanbestedende overheid since 17.04.1978; "
                    "jaarvergadering mei; boekjaar 31 december; "
                    "10 KBO-bestuurders; NACE 38.330/38.110"
                ),
            },
            {
                "source_id": SRC4,
                "title": "MIWA FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "MIWA",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1374; FOI info@miwa.be / 0800 98 003 / 03 776 72 50; "
                    "Vlyminckshoek 12 9100 Sint-Niklaas; maandag-vrijdag 8.30-17.00"
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
                "name_nl": "MIWA (leftover opdrachthoudende vereniging / IGS afval Midden-Waasland)",
                "name_fr": "MIWA (association chargee de mission residuelle / IGS dechets Midden-Waasland)",
                "name_en": "MIWA leftover Midden-Waasland waste IGS (mission association)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://miwa.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1374 leftover residual IGS OV of Midden-Waasland; "
                    "KBO 0218.239.409 Actief since 17.04.1978; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 19597553 othops 13954081 diensten 10572385 pnl 32305; "
                    "FOI ready othops 13.95m/diensten 10.57m/brand"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_miwa_assets_2025", ENT, "2025", "19597553", "2025 assets 19597553 VOL-inb 20/58 (commissaris 19597553.04); tick1374; primary official NBB WVV"),
        ("bud_miwa_assets_2024", ENT, "2024", "17621021", "2024 assets 17621021 comparative; tick1374; primary official NBB WVV 20/58"),
        ("bud_miwa_fixed_2025", ENT, "2025", "8542542", "2025 vaste activa 8542542 vs 7370059; tick1374; primary official NBB WVV 21/28"),
        ("bud_miwa_iva_2025", ENT, "2025", "118991", "2025 IVA 118991 vs 108844 after aanschaf 49024; tick1374; primary official NBB WVV 21"),
        ("bud_miwa_mva_2025", ENT, "2025", "8421439", "2025 MVA 8421439 vs 7258359; tick1374; primary official NBB WVV 22/27"),
        ("bud_miwa_buildings_2025", ENT, "2025", "550382", "2025 terreinen en gebouwen 550382 vs 638734 after uitboek aanschaf 576782; tick1374; primary official NBB WVV 22"),
        ("bud_miwa_machines_2025", ENT, "2025", "547558", "2025 installaties/machines 547558 vs 692406 (aanschaf 3329632 / afschr cum 2782073); tick1374; primary official NBB WVV 23"),
        ("bud_miwa_rollend_2025", ENT, "2025", "619690", "2025 meubilair/rollend 619690 vs 735461; tick1374; primary official NBB WVV 24"),
        ("bud_miwa_othmva_2025", ENT, "2025", "6093402", "2025 overige MVA/recyclageparken 6093402 vs 5017356 (aanschaf 10462803 / overboek 1428378); tick1374; primary official NBB WVV 26"),
        ("bud_miwa_cip_2025", ENT, "2025", "610407", "2025 activa in aanbouw 610407 vs 174403 after aanschaf 1864382 + overboek -1428378; tick1374; primary official NBB WVV 27"),
        ("bud_miwa_fva_2025", ENT, "2025", "2113", "2025 FVA 2113 (aandelen 771 after verkoop 669 + borg 1342; 6.4.1/6.5.1 not filed); tick1374; primary official NBB WVV 28"),
        ("bud_miwa_current_2025", ENT, "2025", "11055011", "2025 vlottende activa 11055011 vs 10250963; tick1374; primary official NBB WVV 29/58"),
        ("bud_miwa_inv_2025", ENT, "2025", "191471", "2025 voorraden 191471 (grond-hulp 4411 + handels 187060); tick1374; primary official NBB WVV 3"),
        ("bud_miwa_strecv_2025", ENT, "2025", "988305", "2025 ST vorderingen 988305 (trade 817388 + other 170918); tick1374; primary official NBB WVV 40/41"),
        ("bud_miwa_invest_2025", ENT, "2025", "4675030", "2025 geldbeleggingen 4675030 DROP vs 6695869 (vastrentend 3730920 waarvan bank 3250000 + termijn >1y 944109); tick1374; primary official NBB WVV 50/53"),
        ("bud_miwa_invest_2024", ENT, "2024", "6695869", "2024 geldbeleggingen 6695869 comparative; tick1374; primary official NBB WVV 50/53"),
        ("bud_miwa_cash_2025", ENT, "2025", "5115569", "2025 liquide middelen 5115569 JUMP vs 2313450; no bank debt; tick1374; primary official NBB WVV 54/58"),
        ("bud_miwa_cash_2024", ENT, "2024", "2313450", "2024 liquide middelen 2313450 comparative; tick1374; primary official NBB WVV 54/58"),
        ("bud_miwa_prepaid_2025", ENT, "2025", "84635", "2025 overlopend actief 84635 (OVAM asbest 79140 + intresten 4733 + accijnzen 762); tick1374; primary official NBB WVV 490/1"),
        ("bud_miwa_equity_2025", ENT, "2025", "11888794", "2025 eigen vermogen 11888794 vs 12012050 (RvB 11888794.08); tick1374; primary official NBB WVV 10/15"),
        ("bud_miwa_inbreng_2025", ENT, "2025", "44155", "2025 inbreng onbeschikbaar 44155 / 44155 aandelen (SN 21813 49.4pct / Temse 8469 / SGW 5572 / Stekene 5188 / Waasmunster 3113); tick1374; primary official NBB WVV 10/11"),
        ("bud_miwa_reserves_2025", ENT, "2025", "7163624", "2025 reserves 7163624 (statutair onbeschikbaar 7120317 + beschikbaar 43307); tick1374; primary official NBB WVV 13"),
        ("bud_miwa_retained_2025", ENT, "2025", "3622603", "2025 overgedragen winst 3622603 vs 3590298 after PnL 32305; tick1374; primary official NBB WVV 14"),
        ("bud_miwa_capsub_2025", ENT, "2025", "1058412", "2025 kapitaalsubsidies 1058412 vs 1213973; tick1374; primary official NBB WVV 15"),
        ("bud_miwa_prov_2025", ENT, "2025", "4129494", "2025 voorzieningen 4129494 vs 3901074 (pensioen 4101074 + overige 28420; 6.8 not filed); tick1374; primary official NBB WVV 16"),
        ("bud_miwa_prov_pens_2025", ENT, "2025", "4101074", "2025 voorziening responsabilisering 4101074 2025-2044 disconto 2pct opbouw tot 2035; tick1374; primary official NBB WVV 160 + 6.19"),
        ("bud_miwa_debt_2025", ENT, "2025", "3579264", "2025 schulden 3579264 JUMP vs 1707897; no LT/bank; tick1374; primary official NBB WVV 17/49"),
        ("bud_miwa_st_2025", ENT, "2025", "3484031", "2025 ST schulden 3484031 vs 1599248; tick1374; primary official NBB WVV 42/48"),
        ("bud_miwa_sttrade_2025", ENT, "2025", "1335838", "2025 leveranciers 1335838 vs 1100716; tick1374; primary official NBB WVV 440/4"),
        ("bud_miwa_sttaxsoc_2025", ENT, "2025", "331956", "2025 tax/soc 331956 (tax 41696 + wages 290260); tick1374; primary official NBB WVV 45"),
        ("bud_miwa_stoth_2025", ENT, "2025", "1816236", "2025 overige ST schulden 1816236 JUMP vs 182963; no 6.9 split; tick1374; primary official NBB WVV 47/48"),
        ("bud_miwa_stoth_2024", ENT, "2024", "182963", "2024 overige ST schulden 182963 comparative; tick1374; primary official NBB WVV 47/48"),
        ("bud_miwa_accrued_2025", ENT, "2025", "95234", "2025 overlopend passief 95234 (OVAM heffing 49564 + asbest 4838 + asbestattest 40000); tick1374; primary official NBB WVV 492/3"),
        ("bud_miwa_ops_2025", ENT, "2025", "16785392", "2025 bedrijfsopbrengsten 16785392 vs 16556957; tick1374; primary official NBB WVV 70/76A"),
        ("bud_miwa_omzet_2025", ENT, "2025", "2620372", "2025 omzet 2620372 vs 2679055; 6.10 category/geo empty; tick1374; primary official NBB WVV 70"),
        ("bud_miwa_omzet_2024", ENT, "2024", "2679055", "2024 omzet 2679055 comparative; tick1374; primary official NBB WVV 70"),
        ("bud_miwa_othops_2025", ENT, "2025", "13954081", "2025 andere bedrijfsopbrengsten 13954081 vs 13877241 (740 subsidies 182583 only; ~13771498 unnamed); tick1374; primary official NBB WVV 74"),
        ("bud_miwa_othops_2024", ENT, "2024", "13877241", "2024 andere bedrijfsopbrengsten 13877241 comparative; tick1374; primary official NBB WVV 74"),
        ("bud_miwa_subs_2025", ENT, "2025", "182583", "2025 exploitatiesubsidies 182583 vs 267901; tick1374; primary official NBB WVV 740"),
        ("bud_miwa_nrop_2025", ENT, "2025", "210939", "2025 niet-recurrente bedrijfsopbrengsten 210939 (terugneming afschr 112987 + meerwaarde MVA 97952); tick1374; primary official NBB WVV 76A"),
        ("bud_miwa_goods_2025", ENT, "2025", "657227", "2025 handelsgoederen/grond-hulp 657227 vs 577989 (aankopen 666688 / voorraad -9460); tick1374; primary official NBB WVV 60"),
        ("bud_miwa_diensten_2025", ENT, "2025", "10572385", "2025 diensten 10572385 vs 10128425 (63.0pct of ops 16.79m; 403pct of omzet); tick1374; primary official NBB WVV 61"),
        ("bud_miwa_diensten_2024", ENT, "2024", "10128425", "2024 diensten 10128425 comparative; tick1374; primary official NBB WVV 61"),
        ("bud_miwa_pers_2025", ENT, "2025", "4110749", "2025 bezoldigingen 4110749 / 48.5 VTE / 50 koppen / YE 48.3 VTE; tick1374; primary official NBB WVV 62 9087"),
        ("bud_miwa_deprec_2025", ENT, "2025", "1005046", "2025 afschrijvingen 1005046; tick1374; primary official NBB WVV 630"),
        ("bud_miwa_provchg_2025", ENT, "2025", "228420", "2025 voorzieningen toevoeging 228420 (pensioen 200000 + overige 28420); tick1374; primary official NBB WVV 635/8"),
        ("bud_miwa_othcost_2025", ENT, "2025", "288160", "2025 andere bedrijfskosten 288160 (tax 285825 + other 2336); tick1374; primary official NBB WVV 640/8"),
        ("bud_miwa_nrcost_2025", ENT, "2025", "125071", "2025 niet-recurrente bedrijfskosten 125071 all minderwaarde MVA 6630; tick1374; primary official NBB WVV 66A"),
        ("bud_miwa_expl_2025", ENT, "2025", "-201667", "2025 bedrijfsverlies 201667 vs winst 415820; tick1374; primary official NBB WVV 9901"),
        ("bud_miwa_expl_2024", ENT, "2024", "415820", "2024 bedrijfswinst 415820 comparative; tick1374; primary official NBB WVV 9901"),
        ("bud_miwa_fininc_2025", ENT, "2025", "290827", "2025 financiele opbrengsten 290827 (FVA 8479 + vlottend 125998 + other 156350 waarvan capsub 154621); tick1374; primary official NBB WVV 75"),
        ("bud_miwa_fincost_2025", ENT, "2025", "18874", "2025 financiele kosten 18874 (schulden 1458 + WV -15117 + other 32534); tick1374; primary official NBB WVV 65"),
        ("bud_miwa_tax_2025", ENT, "2025", "37980", "2025 belasting 37980; tick1374; primary official NBB WVV 67/77"),
        ("bud_miwa_pnl_2025", ENT, "2025", "32305", "2025 PnL 9904 32305 vs 661566 (commissaris 32304.94); overgedragen; tick1374; primary official NBB WVV"),
        ("bud_miwa_pnl_2024", ENT, "2024", "661566", "2024 PnL 661566 comparative; tick1374; primary official NBB WVV 9904"),
        ("bud_miwa_comm_2025", ENT, "2025", "7678", "2025 commissaris Callens Vandelanotte / Erik Thuysbaert 7678; tick1374; primary official NBB WVV 9505"),
        ("bud_miwa_board_2025", ENT, "2025", "39127", "2025 bestuurders 39127; tick1374; primary official NBB WVV 9503"),
        ("bud_miwa_vat_out_2025", ENT, "2025", "227561", "2025 BTW door de vennootschap 227561 vs 247474; tick1374; primary official NBB WVV 6.13 9146"),
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
                "title": "MIWA JR2025 leftover IGS dual (assets 19.60m / othops 13.95m / diensten 10.57m / brand 2025 / PnL +32k DROP)",
                "entity_id": ENT,
                "beneficiary": "MIWA / Midden-Waasland municipalities / Sint-Niklaas Temse Sint-Gillis-Waas Stekene Waasmunster",
                "legal_basis": "WVV OV; decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-06-03",
                "start_year": "1978",
                "end_year": "2044",
                "total_envelope_eur": "19597553",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL waste — 13.95m othops (740 only 183k) / 10.57m diensten / brand 2025 insurance open",
                "cut_option": "Publish 13.95m othops split + 10.57m diensten/top-20 + brand/insurance file + 1.82m ST-other JUMP + 4.10m pension; do not keep 19.60m municipal waste IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1374; assets 19597553 othops 13954081 diensten 10572385 pnl 32305; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "MIWA JR2025 leftover IGS: assets 19.60m / othops 13.95m / diensten 10.57m / brand 2025 / PnL +32k DROP",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "13954081",
                "total_cost_eur": "19597553",
                "tco_notes": (
                    "Leftover dual IGS OV of Midden-Waasland: "
                    "assets 19.60m / equity 11.89m / pnl +32k DROP vs 662k / othops 13.95m (740 only 183k) / "
                    "diensten 10.57m (63pct of ops) / 48.5 VTE / brand 2025 insurance open / pensioen 4.10m / "
                    "official NBB WVV live; "
                    "do not treat 19.60m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "MIWA / Midden-Waasland municipalities",
                "stated_goal": "Local leftover IGS map VL waste — JR2025 live; dual othops/diensten/brand FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 19.60m / othops 13.95m / diensten 10.57m / brand 2025 / pnl +32k DROP",
                "absurdity_score": "7.5",
                "cost_score": "6.5",
                "difficulty": "2.5",
                "priority_index": "6.8",
                "cut_proposal": "Publish 13.95m othops split + 10.57m diensten/top-20 + brand/insurance file + 1.82m ST-other JUMP + 4.10m pension; do not keep 19.60m municipal waste IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1374; leftover IGS OV of Midden-Waasland; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "andere bedrijfsopbrengsten 13954081 (WVV 74; 740 subsidies 182583 only; ~13771498 unnamed) per stroom/tegenpartij "
                    "+ omzet 2620372 (WVV 70; 6.10 category/geo empty) waarom bijna alle opbrengsten buiten omzet "
                    "+ diensten 10572385 (63.0pct of ops; 403pct of omzet; WVV 61) top-20 leveranciers "
                    "+ bedrijfsbrand 2025 (6.20 + commissaris; verzekering open; nr-opbr 210939 / nr-kost 125071) "
                    "+ ST overige schulden 1816236 JUMP vs 182963 + voorziening pensioen 4101074 2025-2044 "
                    "+ recyclageparken overige MVA 6093402 / CIP 610407 / 25y opstal "
                    "+ 6.4.1/6.5.1/6.8/6.15/6.18 not filed + FVA aandelen 771"
                ),
                "why_it_matters": (
                    "Leftover IGS OV of Midden-Waasland municipalities "
                    "(same leftover-IGS waste seam as IVOO 1373 / IMOG 1369 / IVBO 1352 / IVIO 1347 / IVVO 1345): "
                    "19.60m assets / 13.95m othops (740 only 183k) / 10.57m diensten / "
                    "brand 2025 insurance open / 48.5 VTE / 6.10 empty "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "MIWA / Raad van Bestuur / Sint-Niklaas / Temse / Sint-Gillis-Waas / Stekene / Waasmunster",
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
                    "tick1374 leftover IGS OV of Midden-Waasland after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (480kB 50p deposit 2026-00209388). "
                    "IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. "
                    "IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 skipped. "
                    "Dommelhof leftover Limburg EVA not re-probed once live MIWA extracted. "
                    "Otary RS Nuhma-adjacent fallback not taken. "
                    "IVAREM still 2024. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1374",
        "title": "MIWA OV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: MIWA leftover IGS OV of Midden-Waasland after honest hunt; KBO 0218.239.409 Actief; "
            "live JR2025 official NBB WVV VOL-inb PDF (480kB 50p deposit 2026-00209388; commissaris Callens Vandelanotte); "
            "sourced euros assets 19597553 / othops 13954081 / diensten 10572385 / pnl 32305; "
            "FOI ready othops 13.95m/diensten 10.57m/brand"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T03:25:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1374 MIWA leftover IGS residual; KBO 0218.239.409; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1375 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1375",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1374 done including MIWA 1374 leftover IGS live NBB WVV / "
            "IVOO 1373 leftover IGS live NBB WVV / "
            "IGEMO 1372 leftover IGS live NBB WVV / "
            "Veneco 1371 leftover IGS live NBB WVV / "
            "Haviland 1370 leftover IGS live NBB WVV + every-10 / "
            "IMOG 1369 leftover IGS live NBB WVV / "
            "IOK 1368 leftover IGS live NBB WVV / "
            "Leiedal 1367 leftover IGS live NBB WVV / "
            "Interleuven 1366 leftover IGS live NBB WVV / "
            "s-Lim DV 1365 leftover IGS live NBB WVV / "
            "Herkenrode RE NV 1364 leftover vastgoed live NBB WVV / "
            "MyCSN NV 1363 leftover smart-city live NBB WVV / "
            "s-Lim CV 1362 leftover smart-city live NBB WVV / "
            "Nuhmeris NV 1361 leftover klimaat-holding live NBB WVV / "
            "ECO2050 cv 1360 leftover klimaat-coop live NBB WVV + every-10); "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if a new live 2025 WVV PDF downloads (prefer leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; Otary CDN 2026-00254280 live prior tick, not taken); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1374 after MIWA leftover IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1374", rq_new, rq_spawn)
    print("research_queue 1374", found, "spawned_1375", spawned)

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
                "last_unit_id": "rq_1374",
                "ticks_completed": "1374",
                "paused": "no",
                "notes": (
                    "tick1374 MIWA leftover IGS residual; KBO 0218.239.409; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 19597553 othops 13954081 diensten 10572385 pnl 32305; "
                    "FOI ready othops 13.95m/diensten 10.57m/brand; next rq_1375 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")
    print("tick1374 write done")


if __name__ == "__main__":
    main()

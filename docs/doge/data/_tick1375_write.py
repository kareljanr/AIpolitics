# -*- coding: utf-8 -*-
"""Tick 1375 — leftover IVAGO JR2025 official NBB WVV euros.
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

TICK = "1375"
UTC = "2026-08-19T04:00:00Z"
ENT = "igs_ivag"
HIER = "Vlaanderen>OostVlaanderen>IGS>IVAGO>GentDestelbergen"
GAP = "gap_ivag_omzet_81_14m_diensten_38_04m_ecov_l5"
SRC = "src_ivag_jr2025_nbb"
SRC2 = "src_ivag_site"
SRC3 = "src_kbo_ivag_0252828916"
SRC4 = "src_ivag_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00236431.pdf"
SRC2_URL = "https://www.ivago.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0252828916"
SRC4_URL = "https://stad.gent/nl/opening-hours-addresses/ivago-intercommunale-vereniging-voor-afvalbeheer-gent-en-omstreken"
FOI_EMAIL = "info@ivago.be"
FOI_POSTAL = "Proeftuinstraat 43 9000 Gent"
DRAFT = "docs/doge/foi/drafts/gap_ivag_omzet_81_14m_diensten_38_04m_ecov_l5.md"
COMM = "comm_ivag_jr2025_pnl"
LB = "lb_ivag_omzet_81_14m_diensten_38_04m_ecov"


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
                "title": "IVAGO jaarrekening boekjaar 2025 (official NBB WVV VOL-kap deposit 2026-00236431; AV 24.06.2026)",
                "url": SRC_URL,
                "publisher": "IVAGO / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1375; official NBB VOL-kap PDF 691kB 58p deposit 2026-00236431 created 02.07.2026; "
                    "leftover IGS OV of mined Gent+Destelbergen; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Baker Tilly BV B00190 / Christel De Blander A02258 23572; "
                    "oordeel zonder voorbehoud + emphasis 6.19 AEC onderhoud / 6.14 pensioen; "
                    "6.1/6.2.1-6.2.2/6.2.4-6.2.5/6.3.5/6.4.2/6.5.1-6.5.2/6.7.2/6.8/6.17/6.18.1-6.18.2/6.20 not filed; "
                    "6.10 category/geo empty; 740 empty; not every-10"
                ),
            },
            {
                "source_id": SRC2,
                "title": "IVAGO official site (waste IGS Gent-Destelbergen)",
                "url": SRC2_URL,
                "publisher": "IVAGO Intercommunale",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1375; leftover IGS waste of Gent/Destelbergen; "
                    "ivago.be TLS unexpected EOF this box; statutory 2025 balans is the NBB CDN deposit; "
                    "activiteitenverslag 2025 glossy exists (not used for euros)"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO IVAGO 0252.828.916",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1375; KBO 0252.828.916 Actief / normale toestand since 06.06.1994; "
                    "statutaire naam Intergemeentelijke Vereniging voor Afvalbeheer in Gent en Omstreken since 15.10.2003; "
                    "afkorting IVAGO since 06.06.1994; Opdrachthoudende vereniging (Vlaams Gewest) since 06.06.1994; "
                    "zetel Proeftuinstraat 43 9000 Gent since 20.12.2023; 6 VE; "
                    "btw since 01.11.1994; RSZ since 01.01.2022; aanbestedende overheid since 06.06.1994; "
                    "jaarvergadering juni; boekjaar 31 december; "
                    "13 KBO-bestuurders; NACE 38.330/38.210"
                ),
            },
            {
                "source_id": SRC4,
                "title": "IVAGO FOI channel / official contact (Stad Gent listing)",
                "url": SRC4_URL,
                "publisher": "Stad Gent / IVAGO",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1375; FOI info@ivago.be / 09 240 81 11; "
                    "Proeftuinstraat 43 9000 Gent; ivago.be TLS failed this box so Stad Gent listing used"
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
                "name_nl": "IVAGO (leftover opdrachthoudende vereniging / IGS afval Gent-Destelbergen)",
                "name_fr": "IVAGO (association chargee de mission residuelle / IGS dechets Gand-Destelbergen)",
                "name_en": "IVAGO leftover Gent-Destelbergen waste IGS (mission association)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.ivago.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1375 leftover residual IGS OV of mined Gent+Destelbergen; "
                    "KBO 0252.828.916 Actief since 06.06.1994; official NBB WVV VOL-kap PDF downloads; "
                    "sourced euros assets 78394662 omzet 81142751 diensten 38044488 pnl 2216561; "
                    "FOI ready omzet 81.14m/diensten 38.04m/ECOV"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_ivag_assets_2025", ENT, "2025", "78394662", "2025 assets 78394662 VOL-kap 20/58; tick1375; primary official NBB WVV"),
        ("bud_ivag_assets_2024", ENT, "2024", "68282738", "2024 assets 68282738 comparative; tick1375; primary official NBB WVV 20/58"),
        ("bud_ivag_fixed_2025", ENT, "2025", "42377128", "2025 vaste activa 42377128 vs 41537715; tick1375; primary official NBB WVV 21/28"),
        ("bud_ivag_iva_2025", ENT, "2025", "9806562", "2025 IVA 9806562 vs 9745113 after aanschaf 1666489 / YE aanschaf 21525050; tick1375; primary official NBB WVV 21"),
        ("bud_ivag_mva_2025", ENT, "2025", "32155095", "2025 MVA 32155095 vs 31529466; tick1375; primary official NBB WVV 22/27"),
        ("bud_ivag_buildings_2025", ENT, "2025", "10401643", "2025 terreinen en gebouwen 10401643 vs 10937780; tick1375; primary official NBB WVV 22"),
        ("bud_ivag_machines_2025", ENT, "2025", "9270400", "2025 installaties/machines 9270400 vs 10061594 (aanschaf year 1079530); tick1375; primary official NBB WVV 23"),
        ("bud_ivag_rollend_2025", ENT, "2025", "11674141", "2025 meubilair/rollend 11674141 vs 9764107 (aanschaf year 4382620); tick1375; primary official NBB WVV 24"),
        ("bud_ivag_cip_2025", ENT, "2025", "808911", "2025 activa in aanbouw 808911 vs 765985 after aanschaf 775848; tick1375; primary official NBB WVV 27"),
        ("bud_ivag_fva_2025", ENT, "2025", "415471", "2025 FVA 415471 (verbonden vordering 165494 + aandelen 235067 + borg 14910); tick1375; primary official NBB WVV 28"),
        ("bud_ivag_current_2025", ENT, "2025", "36017534", "2025 vlottende activa 36017534 vs 26745023; tick1375; primary official NBB WVV 29/58"),
        ("bud_ivag_inv_2025", ENT, "2025", "1778402", "2025 voorraden 1778402 (grond-hulp 180456 + handels 1597946; WV 506549); tick1375; primary official NBB WVV 3"),
        ("bud_ivag_strecv_2025", ENT, "2025", "6809787", "2025 ST vorderingen 6809787 (trade 6453083 + other 356704); tick1375; primary official NBB WVV 40/41"),
        ("bud_ivag_cash_2025", ENT, "2025", "26990182", "2025 liquide middelen 26990182 JUMP vs 17430362 (notes: delayed capex); tick1375; primary official NBB WVV 54/58"),
        ("bud_ivag_cash_2024", ENT, "2024", "17430362", "2024 liquide middelen 17430362 comparative; tick1375; primary official NBB WVV 54/58"),
        ("bud_ivag_prepaid_2025", ENT, "2025", "439163", "2025 overlopend actief 439163; tick1375; primary official NBB WVV 490/1"),
        ("bud_ivag_equity_2025", ENT, "2025", "51188968", "2025 eigen vermogen 51188968 vs 36354631; tick1375; primary official NBB WVV 10/15"),
        ("bud_ivag_capital_2025", ENT, "2025", "10946224", "2025 geplaatst kapitaal 10946224 / 44138 aandelen (I 18428 / V 11041 / O 14669); ECOV terug 4975624/20063 + toetreding 4977112/20069; tick1375; primary official NBB WVV 10"),
        ("bud_ivag_reserves_2025", ENT, "2025", "4822867", "2025 reserves 4822867 (wettelijk 414312 + overige onbeschikbaar 4408555); tick1375; primary official NBB WVV 13"),
        ("bud_ivag_retained_2025", ENT, "2025", "1210604", "2025 overgedragen winst 1210604 vs -895129 after PnL 2216561 / wettelijk 110828; tick1375; primary official NBB WVV 14"),
        ("bud_ivag_capsub_2025", ENT, "2025", "34209194", "2025 kapitaalsubsidies 34209194 JUMP vs 21339933 (+12.9m Stad Gent investeringstoelage); tick1375; primary official NBB WVV 15"),
        ("bud_ivag_capsub_2024", ENT, "2024", "21339933", "2024 kapitaalsubsidies 21339933 comparative; tick1375; primary official NBB WVV 15"),
        ("bud_ivag_prov_2025", ENT, "2025", "5823296", "2025 voorzieningen 5823296 vs 6345259 (AEC groot onderhoud 5823296; 6.8 empty); tick1375; primary official NBB WVV 16"),
        ("bud_ivag_debt_2025", ENT, "2025", "21382398", "2025 schulden 21382398 vs 25582848; LT 0 vs 1001351; resterende bank 1001350 tot juni 2026; tick1375; primary official NBB WVV 17/49"),
        ("bud_ivag_st_2025", ENT, "2025", "20375567", "2025 ST schulden 20375567 vs 23483882; tick1375; primary official NBB WVV 42/48"),
        ("bud_ivag_stbank_2025", ENT, "2025", "1001350", "2025 ST bank current portion 1001350 (last repayment juni 2026); tick1375; primary official NBB WVV 42"),
        ("bud_ivag_sttrade_2025", ENT, "2025", "9378981", "2025 leveranciers 9378981 vs 8908120; tick1375; primary official NBB WVV 440/4"),
        ("bud_ivag_sttaxsoc_2025", ENT, "2025", "6329688", "2025 tax/soc 6329688 (tax 597547 + wages 5732141); tick1375; primary official NBB WVV 45"),
        ("bud_ivag_stoth_2025", ENT, "2025", "3665548", "2025 overige ST schulden 3665548 vs 3852160; tick1375; primary official NBB WVV 47/48"),
        ("bud_ivag_accrued_2025", ENT, "2025", "1006831", "2025 overlopend passief 1006831; tick1375; primary official NBB WVV 492/3"),
        ("bud_ivag_ops_2025", ENT, "2025", "82950889", "2025 bedrijfsopbrengsten 82950889 vs 86405052; tick1375; primary official NBB WVV 70/76A"),
        ("bud_ivag_omzet_2025", ENT, "2025", "81142751", "2025 omzet 81142751 DROP vs 83374612; 6.10 category/geo empty; elektriciteit 0.8m geelimineerd; tick1375; primary official NBB WVV 70"),
        ("bud_ivag_omzet_2024", ENT, "2024", "83374612", "2024 omzet 83374612 comparative; tick1375; primary official NBB WVV 70"),
        ("bud_ivag_othops_2025", ENT, "2025", "1416601", "2025 andere bedrijfsopbrengsten 1416601 vs 2739451 (740 empty; textiel 0.2m + BTW-verhouding 0.3m); tick1375; primary official NBB WVV 74"),
        ("bud_ivag_goods_2025", ENT, "2025", "3533919", "2025 handelsgoederen/grond-hulp 3533919 (aankopen 3956410 / voorraad -422491); tick1375; primary official NBB WVV 60"),
        ("bud_ivag_diensten_2025", ENT, "2025", "38044488", "2025 diensten 38044488 vs 38210993 (46.9pct of omzet); tick1375; primary official NBB WVV 61"),
        ("bud_ivag_diensten_2024", ENT, "2024", "38210993", "2024 diensten 38210993 comparative; tick1375; primary official NBB WVV 61"),
        ("bud_ivag_pers_2025", ENT, "2025", "32837525", "2025 bezoldigingen 32837525 / 399 VTE / 405 koppen / YE 398 VTE; tick1375; primary official NBB WVV 62 9087"),
        ("bud_ivag_uitzend_2025", ENT, "2025", "4342883", "2025 uitzend 4342883 / 57.8 VTE / 114115 uur; tick1375; primary official NBB WVV 617"),
        ("bud_ivag_deprec_2025", ENT, "2025", "7313982", "2025 afschrijvingen 7313982 vs 8843747 (leasing aflopen -1.5m); tick1375; primary official NBB WVV 630"),
        ("bud_ivag_wv_2025", ENT, "2025", "549827", "2025 WV 549827 (voorraad 506549 + trade 43278); tick1375; primary official NBB WVV 631/4"),
        ("bud_ivag_provchg_2025", ENT, "2025", "-521963", "2025 voorzieningen netto terugname 521963 (toevoeg 630674 / besteding 1152637); tick1375; primary official NBB WVV 635/8"),
        ("bud_ivag_othcost_2025", ENT, "2025", "1089279", "2025 andere bedrijfskosten 1089279 (tax 1010046 + other 79233); tick1375; primary official NBB WVV 640/8"),
        ("bud_ivag_nrcost_2025", ENT, "2025", "17224", "2025 niet-recurrente bedrijfskosten 17224; tick1375; primary official NBB WVV 66A"),
        ("bud_ivag_expl_2025", ENT, "2025", "86608", "2025 bedrijfswinst 86608 vs verlies 829792; tick1375; primary official NBB WVV 9901"),
        ("bud_ivag_expl_2024", ENT, "2024", "-829792", "2024 bedrijfsverlies 829792 comparative; tick1375; primary official NBB WVV 9901"),
        ("bud_ivag_fininc_2025", ENT, "2025", "2199632", "2025 financiele opbrengsten 2199632 (capsub 2108789 + intrest 17181 + divers 69289); tick1375; primary official NBB WVV 75"),
        ("bud_ivag_capsub_pl_2025", ENT, "2025", "2108789", "2025 kapitaalsubsidies in PnL 2108789 vs 1397603; tick1375; primary official NBB WVV 9125"),
        ("bud_ivag_fincost_2025", ENT, "2025", "72596", "2025 financiele kosten 72596 (schulden 3221 + other 52781 + nr 16594); tick1375; primary official NBB WVV 65/66B"),
        ("bud_ivag_tax_2025", ENT, "2025", "-2917", "2025 belasting credit 2917; tick1375; primary official NBB WVV 67/77"),
        ("bud_ivag_pnl_2025", ENT, "2025", "2216561", "2025 PnL 9904 2216561 vs 1404485 (9905 2216561 vs 574693); tick1375; primary official NBB WVV"),
        ("bud_ivag_pnl_2024", ENT, "2024", "1404485", "2024 PnL 1404485 comparative (9905 574693); tick1375; primary official NBB WVV 9904"),
        ("bud_ivag_comm_2025", ENT, "2025", "23572", "2025 commissaris Baker Tilly / Christel De Blander 23572; tick1375; primary official NBB WVV 9505"),
        ("bud_ivag_vat_out_2025", ENT, "2025", "3662399", "2025 BTW door de vennootschap 3662399 vs 4285437; tick1375; primary official NBB WVV 6.13 9146"),
        ("bud_ivag_invest_2025", ENT, "2025", "8000000", "2025 investeringen notes 8.0m (SAP 2.1m + rollend 4.1m + IT 0.277m); tick1375; primary official NBB WVV jaarverslag"),
        ("bud_ivag_aec_ton_2025", ENT, "2025", "96602", "2025 AEC 96602 ton brandbaar afval (tonnage not euros); recorded as sourced activity count; tick1375; primary official NBB WVV jaarverslag"),
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
                "title": "IVAGO JR2025 leftover IGS dual (assets 78.39m / omzet 81.14m / diensten 38.04m / ECOV exit / capsub 34.21m / PnL +2.22m)",
                "entity_id": ENT,
                "beneficiary": "IVAGO / Gent Destelbergen OCMW Gent / former ECOV transition",
                "legal_basis": "WVV OV; decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-06-24",
                "start_year": "1994",
                "end_year": "2030",
                "total_envelope_eur": "78394662",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL waste — 81.14m omzet (6.10 empty) / 38.04m diensten / ECOV-exit + Gent capsub 34.21m / AEC to 2030 open",
                "cut_option": "Publish 81.14m omzet split + 38.04m diensten/top-20 + ECOV-exit file + 34.21m Gent capsub + AEC-to-2030 plan; do not keep 78.39m municipal waste IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1375; assets 78394662 omzet 81142751 diensten 38044488 pnl 2216561; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "IVAGO JR2025 leftover IGS: assets 78.39m / omzet 81.14m / diensten 38.04m / ECOV exit / capsub 34.21m / PnL +2.22m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "38044488",
                "total_cost_eur": "78394662",
                "tco_notes": (
                    "Leftover dual IGS OV of mined Gent+Destelbergen after ECOV private-partner exit 25.06.2025: "
                    "assets 78.39m / equity 51.19m / pnl +2.22m / omzet 81.14m (6.10 empty) / "
                    "diensten 38.04m (47pct of omzet) / 399 VTE + 57.8 uitzend / capsub 34.21m JUMP / "
                    "AEC permit to 30.06.2030 / official NBB WVV live; "
                    "do not treat 78.39m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "IVAGO / Gent Destelbergen OCMW Gent",
                "stated_goal": "Local leftover IGS map VL waste — JR2025 live; dual omzet/diensten/ECOV FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 78.39m / omzet 81.14m / diensten 38.04m / ECOV exit / pnl +2.22m",
                "absurdity_score": "7.4",
                "cost_score": "7.8",
                "difficulty": "2.5",
                "priority_index": "7.1",
                "cut_proposal": "Publish 81.14m omzet split + 38.04m diensten/top-20 + ECOV-exit file + 34.21m Gent capsub + AEC-to-2030 plan; do not keep 78.39m municipal waste IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1375; leftover IGS OV of mined Gent+Destelbergen; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "omzet 81142751 DROP vs 83374612 (WVV 70; 6.10 category/geo empty; notes elektriciteit 0.8m geelimineerd / AEC 96602 t partners) per stroom/tegenpartij "
                    "+ diensten 38044488 (46.9pct of omzet; WVV 61; comparative 38210993) top-20 leveranciers "
                    "+ uitzend 4342883 / 57.8 VTE (WVV 617) "
                    "+ ECOV-exit 25/26.06.2025 (terugbetaling 4975624 / 20063 aandelen; Stad Gent toetreding 4977112 / 20069; OCMW dec 2025; overgang tot juni 2026) "
                    "+ kapitaalsubsidies 34209194 JUMP vs 21339933 (+12.9m Stad Gent) + 5.0m kapitaalstorting + cash 26990182 JUMP vs 17430362 "
                    "+ AEC vergunning tot 30.06.2030 / voorziening 5823296 (6.19) "
                    "+ 740 empty + 6.8/6.15/6.20 not filed + FVA 415471"
                ),
                "why_it_matters": (
                    "Leftover IGS OV of mined Gent+Destelbergen "
                    "(same leftover-IGS waste seam as MIWA 1374 / IVOO 1373 / IMOG 1369 / IVBO 1352 / IVIO 1347 / IVVO 1345; "
                    "NOT in the 1366-1374 CDN seam): "
                    "78.39m assets / 81.14m omzet / 38.04m diensten / "
                    "ECOV private-partner exit + Gent capsub 34.21m / AEC to 2030 / 399 VTE / 6.10 empty "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "IVAGO / Raad van Bestuur / Sofie Bracke / Stad Gent / Destelbergen / OCMW Gent",
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
                    "tick1375 leftover IGS OV of mined Gent+Destelbergen after honest hunt; "
                    "live JR2025 official NBB WVV VOL-kap PDF now extracted (691kB 58p deposit 2026-00236431). "
                    "MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. "
                    "Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. "
                    "IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 skipped. "
                    "Dommelhof leftover Limburg EVA still no 2025/2026 PDF. "
                    "Otary RS Nuhma-adjacent fallback not taken. "
                    "IVAREM still 2024. leftover AGB 404/403. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1375",
        "title": "IVAGO OV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: IVAGO leftover IGS OV of mined Gent+Destelbergen after honest hunt; KBO 0252.828.916 Actief; "
            "live JR2025 official NBB WVV VOL-kap PDF (691kB 58p deposit 2026-00236431; commissaris Baker Tilly); "
            "sourced euros assets 78394662 / omzet 81142751 / diensten 38044488 / pnl 2216561; "
            "FOI ready omzet 81.14m/diensten 38.04m/ECOV"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T03:40:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1375 IVAGO leftover IGS residual; KBO 0252.828.916; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1376 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1376",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1375 done including IVAGO 1375 leftover IGS live NBB WVV / "
            "MIWA 1374 leftover IGS live NBB WVV / "
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
            "prefer leftover MIROM Roeselare KBO 0213.894.205 CDN 2026-00128720 if still live; "
            "leftover MIROM Menen 0213.809.081 CDN 2026-00228376 / De Nekker VZW 0450.062.281 CDN 2026-00147494 only if still live; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if a new live 2025 WVV PDF downloads (prefer leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; Otary CDN 2026-00254280 live prior tick, not taken); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but provincieantwerpen.be 403 — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1375 after IVAGO leftover IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1375", rq_new, rq_spawn)
    print("research_queue 1375", found, "spawned_1376", spawned)

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
                "last_unit_id": "rq_1375",
                "ticks_completed": "1375",
                "paused": "no",
                "notes": (
                    "tick1375 IVAGO leftover IGS residual; KBO 0252.828.916; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 78394662 omzet 81142751 diensten 38044488 pnl 2216561; "
                    "FOI ready omzet 81.14m/diensten 38.04m/ECOV; next rq_1376 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    entry = """### Tick 1375 - 2026-08-19 - rq_1375 IVAGO dual residual leftover
- Unit: IVAGO / Intergemeentelijke Vereniging voor Afvalbeheer in Gent en Omstreken (leftover opdrachthoudende vereniging / IGS waste of mined Gent+Destelbergen; OCMW Gent joined Dec 2025; ECOV private partner exited 25/26.06.2025; 44.138 aandelen I 18.428 / V 11.041 / O 14.669) after residual dual hunt (KBO **0252.828.916**; ivago.be TLS unexpected EOF this box; live NBB WVV VOL-kap deposit **2026-00236431** PDF 691kB / 58p; AV **24.06.2026**; PDF created **02.07.2026**; commissaris Baker Tilly Bedrijfsrevisoren BV B00190 0449.065.260 / Christel De Blander A02258 23.572 oordeel zonder voorbehoud + emphasis 6.19 AEC-onderhoud / 6.14 pensioen). Leftover IGS OV of a mined city whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; **not** in the 1366–1374 leftover IGS CDN seam). Distinct from already-mined MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **06.06.1994**; statutaire naam since 15.10.2003; afkorting IVAGO since 06.06.1994; Opdrachthoudende vereniging (Vlaams Gewest) since 06.06.1994; zetel Proeftuinstraat 43 9000 Gent since 20.12.2023; **6 VE**; tel 09 240 81 11; e-mail info@ivago.be; web https://www.ivago.be/; btw since 01.11.1994; RSZ since 01.01.2022; aanbestedende overheid since 06.06.1994; jaarvergadering juni; 13 KBO-bestuurders; NACE 38.330/38.210. Hunt leftover AGB/zorg/EVA first: leftover AGB Mechelen/Kortrijk/Brugge/Roeselare/Oostende 404/403; Dommelhof leftover Limburg EVA KBO 0777.495.085 SBM page has **no 2025/2026 PDF** — skipped; IVAREM still 2024 (2025-00188050 / 2025-00494826) — skipped; leftover APB provincieantwerpen.be 403. IVAGO statutory CDN live this tick (HTTP 200 / 691273 / 58p) — taken (preferred leftover IGS of mined Gent outside the 1366–1374 CDN seam and outside Nuhma). MIROM Roeselare 2026-00128720 / MIROM Menen 2026-00228376 / De Nekker VZW 2026-00147494 2025 CDN now live — leftover next, not taken once live IVAGO extracted. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. NBB consult skipped (403/SPA); euros extracted from the official VOL-kap deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366. Not every-10 (next 1380).
- EUR strong (primary official WVV VOL-kap + commissaris oordeel zonder voorbehoud; 6.1/6.2.1-6.2.2/6.2.4-6.2.5/6.3.5/6.4.2/6.5.1-6.5.2/6.7.2/6.8/6.17/6.18.1-6.18.2/6.20 not filed; 6.10 category/geo empty; 740 empty): assets **78.394.662** (was 68.282.738); fixed **42.377.128** / IVA **9.806.562** (aanschaf 1.666.489) / MVA **32.155.095** (gebouwen **10.401.643**; machines **9.270.400**; rollend **11.674.141** aanschaf 4.382.620; CIP **808.911**); FVA **415.471**; current **36.017.534**; inventory **1.778.402**; ST recv **6.809.787**; cash **26.990.182 JUMP** vs 17.430.362; equity **51.188.968** (kapitaal 10.946.224 / 44.138 aandelen; reserves 4.822.867; overgedragen 1.210.604; capsub **34.209.194 JUMP** vs 21.339.933); voorzieningen **5.823.296** (AEC groot onderhoud; besteding 724k / dotatie 317k); schulden **21.382.398** (LT 0 vs 1.001.351; resterende bank **1.001.350** tot juni 2026; leveranciers 9.378.981); omzet **81.142.751 DROP** vs 83.374.612 (6.10 empty; elektriciteit 0,8m geëlimineerd); andere opbr **1.416.601** (740 empty; textiel 0,2m + BTW-verhouding 0,3m); diensten **38.044.488** (46,9% of omzet); pers **32.837.525** / **399 VTE** / 405 koppen / YE 398 VTE + uitzend **57,8 VTE / 4.342.883**; afschr 7.313.982; expl **+86.608** vs −829.792; fin opbr 2.199.632 (capsub 2.108.789); fin kosten 72.596; PnL **2.216.561** vs 1.404.485; commissaris 23.572. ECOV-exit 25/26.06.2025 (terug 4.975.624 / 20.063 aandelen; Stad Gent +5,0m kapitaal + +12,9m capsub); AEC 96.602 t / vergunning tot 30.06.2030; investeringen 8,0m (SAP 2,1m / rollend 4,1m).
- CSVs: sources+4/entities+1/budgets+56/commitments+1/leaderboard+1 + FOI ready `gap_ivag_omzet_81_14m_diensten_38_04m_ecov_l5` (not sent); rq_1375=done; spawn rq_1376; ticks=1375.
- Coverage: residual dual L5 (IVAGO leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1380).
- Next: rq_1376 residual dual L5 VL JR2025 hole_fill (prefer leftover MIROM Roeselare KBO 0213.894.205 CDN 2026-00128720 if still live; leftover MIROM Menen 0213.809.081 CDN 2026-00228376 / De Nekker VZW 0450.062.281 CDN 2026-00147494 only if still live; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS CDN 2026-00254280 / Rematics / Sunfin only if taken after leftover IGS; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; IVAREM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1375 write done")


if __name__ == "__main__":
    main()

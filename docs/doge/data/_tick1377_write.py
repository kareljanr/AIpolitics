# -*- coding: utf-8 -*-
"""Tick 1377 — leftover MIROM Menen JR2025 official NBB WVV euros.
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

TICK = "1377"
UTC = "2026-08-19T05:00:00Z"
ENT = "igs_miromn"
HIER = "Vlaanderen>WestVlaanderen>IGS>MIROM>Menen3"
GAP = "gap_miromn_othops_4_37m_diensten_4_77m_pens_2_64m_l5"
SRC = "src_miromn_jr2025_nbb"
SRC2 = "src_miromn_site"
SRC3 = "src_kbo_miromn_0213809081"
SRC4 = "src_miromn_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00228376.pdf"
SRC2_URL = "https://www.mirom-menen.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0213809081"
SRC4_URL = "https://publicaties.mirom.org/"
FOI_EMAIL = "info@mirom-menen.be"
FOI_POSTAL = "Industrielaan 30 8930 Menen"
DRAFT = "docs/doge/foi/drafts/gap_miromn_othops_4_37m_diensten_4_77m_pens_2_64m_l5.md"
COMM = "comm_miromn_jr2025_pnl"
LB = "lb_miromn_othops_4_37m_diensten_4_77m_pens"


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
                "title": "MIROM Menen jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00228376; AV 15.06.2026)",
                "url": SRC_URL,
                "publisher": "MIROM Menen / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1377; official NBB VOL-inb PDF 7.5MB 164p deposit 2026-00228376 created 01.07.2026 header 26.06.2026; "
                    "leftover IGS OV of 3 mined Menen-region municipalities; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Auditas BV B00364 / Sven Vansteelant A02050 6975; "
                    "oordeel zonder voorbehoud assets 11706411.28 / PnL 747276.85; "
                    "6.1/6.2.2/6.2.4-6.2.5/6.3.4-6.3.6/6.4.1-6.4.2/6.5.1-6.5.2/6.7.2/6.8/6.14/6.15/6.17/6.18.1-6.18.2/6.20 not filed; "
                    "6.10 category empty geo BE only; 8761/8762 empty; not every-10"
                ),
            },
            {
                "source_id": SRC2,
                "title": "MIROM Menen official site (waste IGS Menen/Wevelgem/Wervik)",
                "url": SRC2_URL,
                "publisher": "MIROM Menen Intercommunale",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1377; leftover IGS waste of Menen-region 3 municipalities; "
                    "statutory 2025 balans is the NBB CDN deposit; "
                    "publicaties.mirom.org lists beknopte verslagen/AV/jaarverslagen (not used for euros)"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO MIROM Menen 0213.809.081",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1377; KBO 0213.809.081 Actief / normale toestand since 03.12.1973; "
                    "statutaire naam Milieuzorg Roeselaere en Menen, Menen / afkorting MIROM Menen since 15.10.2004; "
                    "Opdrachthoudende vereniging (Vlaams Gewest) since 10.11.1993; "
                    "zetel Industrielaan 30 8930 Menen since 01.10.1990; 7 VE; "
                    "btw since 01.05.1982; RSZ since 01.01.2022; aanbestedende overheid since 03.12.1973; "
                    "jaarvergadering april; boekjaar 31 december; "
                    "KBO lists 1 bestuurder Zeno Verschaeve (statutory 10); NACE 38.330"
                ),
            },
            {
                "source_id": SRC4,
                "title": "MIROM Menen FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "MIROM Menen",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1377; FOI info@mirom-menen.be / 056 52 81 30; "
                    "Industrielaan 30 8930 Menen; "
                    "voorzitter Zeno Verschaeve / ondervoorzitters Kristof Vandamme + Stijn Tant"
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
                "name_nl": "MIROM Menen (leftover opdrachthoudende vereniging / IGS afval Menen Wevelgem Wervik)",
                "name_fr": "MIROM Menin (association chargee de mission residuelle / IGS dechets Menin Wevelgem Wervik)",
                "name_en": "MIROM Menen leftover 3-municipality waste IGS (mission association)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.mirom-menen.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1377 leftover residual IGS OV of 3 mined Menen-region municipalities; "
                    "KBO 0213.809.081 Actief since 03.12.1973; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 11706411 omzet 5510522 othops 4366684 diensten 4769777 pnl 747277; "
                    "FOI ready othops 4.37m/diensten 4.77m/pens 2.64m"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_miromn_assets_2025", ENT, "2025", "11706411", "2025 assets 11706411 VOL-inb 20/58; tick1377; primary official NBB WVV; commissaris 11706411.28"),
        ("bud_miromn_assets_2024", ENT, "2024", "12881099", "2024 assets 12881099 comparative; tick1377; primary official NBB WVV 20/58"),
        ("bud_miromn_fixed_2025", ENT, "2025", "3901408", "2025 vaste activa 3901408 vs 3841199; tick1377; primary official NBB WVV 21/28"),
        ("bud_miromn_mva_2025", ENT, "2025", "3894819", "2025 MVA 3894819 vs 3833061; tick1377; primary official NBB WVV 22/27"),
        ("bud_miromn_buildings_2025", ENT, "2025", "1290259", "2025 terreinen en gebouwen 1290259 vs 1468569 (aanschaf year 24513 / YE aanschaf 5362227 / afschr cum 4102497); tick1377; primary official NBB WVV 22"),
        ("bud_miromn_machines_2025", ENT, "2025", "2083295", "2025 installaties/machines 2083295 JUMP vs 1808362 (aanschaf year 636719 / YE aanschaf 4893877); tick1377; primary official NBB WVV 23"),
        ("bud_miromn_rollend_2025", ENT, "2025", "521266", "2025 meubilair/rollend 521266 vs 556130 (aanschaf year 150507); tick1377; primary official NBB WVV 24"),
        ("bud_miromn_fva_2025", ENT, "2025", "6589", "2025 FVA 6589 (aandelen 1425 + borg 5164); tick1377; primary official NBB WVV 28"),
        ("bud_miromn_current_2025", ENT, "2025", "7805003", "2025 vlottende activa 7805003 vs 9039900; tick1377; primary official NBB WVV 29/58"),
        ("bud_miromn_ltrecv_2024", ENT, "2024", "2640000", "2024 LT overige vorderingen 2640000 matching pensioenvoorziening; 2025 0; tick1377; primary official NBB WVV 291"),
        ("bud_miromn_inv_2025", ENT, "2025", "350589", "2025 voorraden 350589 (grond-hulp 259906 + handels 90683); tick1377; primary official NBB WVV 3"),
        ("bud_miromn_strecv_2025", ENT, "2025", "2461225", "2025 ST vorderingen 2461225 (trade 1600318 + other 860907 JUMP vs 376331); tick1377; primary official NBB WVV 40/41"),
        ("bud_miromn_beleg_2025", ENT, "2025", "3432201", "2025 geldbeleggingen 3432201 JUMP vs 2707015 (8689 unnamed; 51/52/53 looptijden empty); tick1377; primary official NBB WVV 50/53"),
        ("bud_miromn_beleg_2024", ENT, "2024", "2707015", "2024 geldbeleggingen 2707015 comparative; tick1377; primary official NBB WVV 50/53"),
        ("bud_miromn_cash_2025", ENT, "2025", "1447446", "2025 liquide middelen 1447446 DROP vs 1629275; tick1377; primary official NBB WVV 54/58"),
        ("bud_miromn_cash_2024", ENT, "2024", "1629275", "2024 liquide middelen 1629275 comparative; tick1377; primary official NBB WVV 54/58"),
        ("bud_miromn_prepaid_2025", ENT, "2025", "113542", "2025 overlopend actief 113542 (verzekeringen 36485 + abonnementen 6000 + ophaalkalender 29007 + gft 42051); tick1377; primary official NBB WVV 490/1"),
        ("bud_miromn_equity_2025", ENT, "2025", "8626785", "2025 eigen vermogen 8626785 vs 7725530; tick1377; primary official NBB WVV 10/15"),
        ("bud_miromn_inbreng_2025", ENT, "2025", "2652670", "2025 inbreng 2652670 onbeschikbaar / 85570 aandelen op naam; niet volgestort 13485; 8761/8762 empty; tick1377; primary official NBB WVV 10/11"),
        ("bud_miromn_capinc_2025", ENT, "2025", "29233", "2025 inbrengverhoging 29233 / 943 aandelen (Menen 13485 / Wevelgem 9889 / Wervik 5859); tick1377; primary official NBB WVV 6.7.1 + JV 5.2"),
        ("bud_miromn_reserves_2025", ENT, "2025", "1167505", "2025 reserves 1167505 (statutair 265267 + overige 14775 + beschikbaar 887464); tick1377; primary official NBB WVV 13"),
        ("bud_miromn_overgedragen_2025", ENT, "2025", "3942241", "2025 overgedragen winst 3942241 vs 3197888; tick1377; primary official NBB WVV 14"),
        ("bud_miromn_capsub_2025", ENT, "2025", "830155", "2025 kapitaalsubsidies 830155 vs 705409; tick1377; primary official NBB WVV 15"),
        ("bud_miromn_prov_2025", ENT, "2025", "0", "2025 voorzieningen 0 DROP vs 2640000; tick1377; primary official NBB WVV 16"),
        ("bud_miromn_pens_2024", ENT, "2024", "2640000", "2024 pensioenvoorziening 2640000 (2025 teruggenomen + 664/7 2640000); tick1377; primary official NBB WVV 160"),
        ("bud_miromn_debt_2025", ENT, "2025", "3079626", "2025 schulden 3079626 vs 2515569; tick1377; primary official NBB WVV 17/49"),
        ("bud_miromn_ltbank_2025", ENT, "2025", "215000", "2025 LT bank 215000 (1-5j) vs 435000; tick1377; primary official NBB WVV 173"),
        ("bud_miromn_st_2025", ENT, "2025", "1852916", "2025 ST schulden 1852916 vs 1465580; tick1377; primary official NBB WVV 42/48"),
        ("bud_miromn_stbank_2025", ENT, "2025", "220000", "2025 ST current bank 220000; tick1377; primary official NBB WVV 42/8841"),
        ("bud_miromn_sttrade_2025", ENT, "2025", "1254857", "2025 leveranciers 1254857 JUMP vs 877082; tick1377; primary official NBB WVV 440/4"),
        ("bud_miromn_sttaxsoc_2025", ENT, "2025", "377145", "2025 tax/soc 377145 (tax 30083 + wages 347062); tick1377; primary official NBB WVV 45"),
        ("bud_miromn_accrued_2025", ENT, "2025", "1011710", "2025 overlopend passief 1011710 (GFT 26 682975 + zakken 288375 + Fost Plus 15443); tick1377; primary official NBB WVV 492/3"),
        ("bud_miromn_ops_2025", ENT, "2025", "12582513", "2025 bedrijfsopbrengsten 12582513 vs 9195870; tick1377; primary official NBB WVV 70/76A"),
        ("bud_miromn_omzet_2025", ENT, "2025", "5510522", "2025 omzet 5510522 vs 5496006; 6.10 category empty / geo BE only; tick1377; primary official NBB WVV 70"),
        ("bud_miromn_omzet_2024", ENT, "2024", "5496006", "2024 omzet 5496006 comparative; tick1377; primary official NBB WVV 70"),
        ("bud_miromn_othops_2025", ENT, "2025", "4366684", "2025 andere bedrijfsopbrengsten 4366684 vs 3685232 (740 subsidies 515641; ~3851043 unnamed); tick1377; primary official NBB WVV 74"),
        ("bud_miromn_subs_2025", ENT, "2025", "515641", "2025 exploitatiesubsidies 515641 JUMP vs 270321; tick1377; primary official NBB WVV 740"),
        ("bud_miromn_nrops_2025", ENT, "2025", "2705306", "2025 niet-recurrente bedrijfsopbrengsten 2705306 (terugneming voorziening 2640000 + meerwaarde 65306); tick1377; primary official NBB WVV 76A"),
        ("bud_miromn_pensrev_2025", ENT, "2025", "2640000", "2025 terugneming pensioenvoorziening 2640000 (WVV 7620); tick1377; primary official NBB WVV"),
        ("bud_miromn_goods_2025", ENT, "2025", "550888", "2025 handelsgoederen/grond-hulp 550888 (aankopen 486801 / voorraad 64088); tick1377; primary official NBB WVV 60"),
        ("bud_miromn_diensten_2025", ENT, "2025", "4769777", "2025 diensten 4769777 vs 4632369 (86.6pct of omzet); tick1377; primary official NBB WVV 61"),
        ("bud_miromn_diensten_2024", ENT, "2024", "4632369", "2024 diensten 4632369 comparative; tick1377; primary official NBB WVV 61"),
        ("bud_miromn_pers_2025", ENT, "2025", "2712524", "2025 bezoldigingen 2712524 / 36.5 VTE / 41 koppen / 54125 uur; tick1377; primary official NBB WVV 62 9087"),
        ("bud_miromn_uitzend_2025", ENT, "2025", "49466", "2025 uitzend 49466 / 0.7 VTE / 1335 uur; tick1377; primary official NBB WVV 617"),
        ("bud_miromn_deprec_2025", ENT, "2025", "749980", "2025 afschrijvingen 749980 vs 698787; tick1377; primary official NBB WVV 630"),
        ("bud_miromn_othcost_2025", ENT, "2025", "544339", "2025 andere bedrijfskosten 544339 (tax 48813 + other 495526 JUMP vs 158410); tick1377; primary official NBB WVV 640/8"),
        ("bud_miromn_nrcost_2025", ENT, "2025", "2641549", "2025 niet-recurrente bedrijfskosten 2641549 (664/7 2640000 + minderwaarde 1549); tick1377; primary official NBB WVV 66A"),
        ("bud_miromn_expl_2025", ENT, "2025", "613455", "2025 bedrijfswinst 613455 vs 510453; tick1377; primary official NBB WVV 9901"),
        ("bud_miromn_expl_2024", ENT, "2024", "510453", "2024 bedrijfswinst 510453 comparative; tick1377; primary official NBB WVV 9901"),
        ("bud_miromn_fininc_2025", ENT, "2025", "155853", "2025 financiele opbrengsten 155853 (capsub 120254 + vlottende 30777); tick1377; primary official NBB WVV 75"),
        ("bud_miromn_capsub_pl_2025", ENT, "2025", "120254", "2025 kapitaalsubsidies in PnL 120254 vs 103921; tick1377; primary official NBB WVV 9125"),
        ("bud_miromn_fincost_2025", ENT, "2025", "12799", "2025 financiele kosten 12799 (schulden 12104 + other 694); tick1377; primary official NBB WVV 65"),
        ("bud_miromn_tax_2025", ENT, "2025", "9233", "2025 belasting 9233; tick1377; primary official NBB WVV 67/77"),
        ("bud_miromn_pnl_2025", ENT, "2025", "747277", "2025 PnL 9904 747277 vs 631416 overgedragen; commissaris 747276.85; tick1377; primary official NBB WVV"),
        ("bud_miromn_pnl_2024", ENT, "2024", "631416", "2024 PnL 631416 comparative; tick1377; primary official NBB WVV 9904"),
        ("bud_miromn_comm_2025", ENT, "2025", "6975", "2025 commissaris Auditas / Sven Vansteelant 6975; tick1377; primary official NBB WVV 9505"),
        ("bud_miromn_bestuur_2025", ENT, "2025", "33904", "2025 bestuurders 33904; tick1377; primary official NBB WVV 9503"),
        ("bud_miromn_machines_aanschaf_2025", ENT, "2025", "636719", "2025 machines aanschaf 636719; tick1377; primary official NBB WVV 8162"),
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
                "title": "MIROM Menen JR2025 leftover IGS dual (assets 11.71m / othops 4.37m / diensten 4.77m / pens 2.64m / PnL 0.75m)",
                "entity_id": ENT,
                "beneficiary": "MIROM Menen / Menen Wevelgem Wervik",
                "legal_basis": "WVV OV; decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-06-15",
                "start_year": "1973",
                "end_year": "2040",
                "total_envelope_eur": "11706411",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL waste — 5.51m omzet (6.10 category empty) / 4.37m othops / 4.77m diensten / pensioen 2.64m DROP",
                "cut_option": "Publish 4.37m othops split + 4.77m diensten/top-20 + 2.64m pensioen path + 3.43m unnamed beleggingen; do not keep 11.71m municipal waste IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1377; assets 11706411 othops 4366684 diensten 4769777 pnl 747277; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "MIROM Menen JR2025 leftover IGS: assets 11.71m / othops 4.37m / diensten 4.77m / pens 2.64m / PnL 0.75m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "4769777",
                "total_cost_eur": "11706411",
                "tco_notes": (
                    "Leftover dual IGS OV of 3 mined Menen-region municipalities: "
                    "assets 11.71m / equity 8.63m / pnl 0.75m / omzet 5.51m (6.10 category empty) / "
                    "othops 4.37m (740 subsidies 0.52m only) / diensten 4.77m (87pct of omzet) / "
                    "36.5 VTE / pensioenvoorziening 2.64m DROP / official NBB WVV live; "
                    "do not treat 11.71m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "MIROM Menen / Menen Wevelgem Wervik",
                "stated_goal": "Local leftover IGS map VL waste — JR2025 live; dual othops/diensten/pens FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 11.71m / othops 4.37m / diensten 4.77m / pens 2.64m DROP / pnl 0.75m",
                "absurdity_score": "7.1",
                "cost_score": "6.8",
                "difficulty": "2.5",
                "priority_index": "6.6",
                "cut_proposal": "Publish 4.37m othops split + 4.77m diensten/top-20 + 2.64m pensioen path + 3.43m unnamed beleggingen; do not keep 11.71m municipal waste IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1377; leftover IGS OV of mined Menen-region; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "omzet 5510522 vs 5496006 (WVV 70; 6.10 category empty / geo BE only) per stroom/tegenpartij "
                    "+ andere bedrijfsopbrengsten 4366684 vs 3685232 (740 subsidies 515641 only; ~3851043 unnamed) "
                    "+ diensten 4769777 (86.6pct of omzet; WVV 61; comparative 4632369) top-20 leveranciers "
                    "+ pensioenvoorziening 2640000 DROP naar 0 + LT vordering 2640000 DROP + nr-opbr 7620 2640000 + nr-kosten 664/7 2640000 path "
                    "+ beleggingen 3432201 JUMP vs 2707015 (8689 unnamed) + overlopend passief GFT 682975 / zakken 288375 "
                    "+ inbrengverhoging 29233 / 85570 aandelen / 8761/8762 empty + 6.15/6.17/6.18/6.20 not filed"
                ),
                "why_it_matters": (
                    "Leftover IGS OV of 3 mined Menen-region municipalities "
                    "(same leftover-IGS waste seam as MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IMOG 1369 / IVBO 1352 / IVIO 1347 / IVVO 1345): "
                    "11.71m assets / 5.51m omzet / 4.37m othops / 4.77m diensten / "
                    "pensioen 2.64m DROP / 36.5 VTE / 6.10 category empty "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "MIROM Menen / Raad van Bestuur / Zeno Verschaeve / Kristof Vandamme / Stijn Tant / Menen Wevelgem Wervik",
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
                    "tick1377 leftover IGS OV of 3 mined Menen-region municipalities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (7.5MB 164p deposit 2026-00228376). "
                    "MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. "
                    "IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. "
                    "Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. "
                    "Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 skipped. "
                    "Dommelhof leftover Limburg EVA not re-probed once live MIROM Menen extracted. "
                    "Otary RS Nuhma-adjacent fallback not taken. De Nekker VZW leftover next. "
                    "IVAREM still 2024. leftover AGB 404/403 as of 1375. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1377",
        "title": "MIROM Menen OV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: MIROM Menen leftover IGS OV of 3 mined Menen-region municipalities after honest hunt; KBO 0213.809.081 Actief; "
            "live JR2025 official NBB WVV VOL-inb PDF (7.5MB 164p deposit 2026-00228376; commissaris Auditas); "
            "sourced euros assets 11706411 / omzet 5510522 / othops 4366684 / diensten 4769777 / pnl 747277; "
            "FOI ready othops 4.37m/diensten 4.77m/pens 2.64m"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T04:20:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1377 MIROM Menen leftover IGS residual; KBO 0213.809.081; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1378 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1378",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1377 done including MIROM Menen 1377 leftover IGS live NBB WVV / "
            "MIROM Roeselare 1376 leftover IGS live NBB WVV / "
            "IVAGO 1375 leftover IGS live NBB WVV / "
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
            "prefer leftover De Nekker VZW 0450.062.281 CDN 2026-00147494 if still live; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if a new live 2025 WVV PDF downloads (prefer leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; Otary CDN 2026-00254280 live prior tick, not taken); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but provincieantwerpen.be 403 — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1377 after MIROM Menen leftover IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1377", rq_new, rq_spawn)
    print("research_queue 1377", found, "spawned_1378", spawned)

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
                "last_unit_id": "rq_1377",
                "ticks_completed": "1377",
                "paused": "no",
                "notes": (
                    "tick1377 MIROM Menen leftover IGS residual; KBO 0213.809.081; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 11706411 omzet 5510522 othops 4366684 diensten 4769777 pnl 747277; "
                    "FOI ready othops 4.37m/diensten 4.77m/pens 2.64m; next rq_1378 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    entry = """### Tick 1377 - 2026-08-19 - rq_1377 MIROM Menen dual residual leftover
- Unit: MIROM Menen (leftover opdrachthoudende vereniging / IGS waste of 3 mined Menen-region municipalities: Menen 34.417 / 1.066.927; Wevelgem 31.884 / 988.404; Wervik 19.209 / 595.479 + B IVVO/MIROM Roeselare/IMOG/IVIO/IVOO/IVBO 10/310 each; 85.570 aandelen / inbreng 2.652.670; duur tot 31.12.2040) after residual dual hunt (KBO **0213.809.081**; official mirom-menen.be / publicaties.mirom.org have beknopte verslagen/AV but no isolated statutory 2025 balans; live NBB WVV VOL-inb deposit **2026-00228376** PDF 7.5MB / 164p of which ~34 statutory; AV **15.06.2026**; PDF created **01.07.2026**; header **26.06.2026**; commissaris Auditas Bedrijfsrevisoren BV B00364 0464.594.366 / Sven Vansteelant A02050 6.975 oordeel zonder voorbehoud assets 11.706.411,28 / PnL 747.276,85). Leftover IGS OV of mined cities whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last ticks listed MIROM Menen CDN 2026-00228376 as leftover next after MIROM Roeselare 1376). Distinct from already-mined MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **03.12.1973**; statutaire naam Milieuzorg Roeselaere en Menen, Menen / afkorting MIROM Menen since 15.10.2004; Opdrachthoudende vereniging (Vlaams Gewest) since 10.11.1993; zetel Industrielaan 30 8930 Menen since 01.10.1990; **7 VE**; tel 056 52 81 30; e-mail info@mirom-menen.be; web https://www.mirom-menen.be/; btw since 01.05.1982; RSZ since 01.01.2022; aanbestedende overheid since 03.12.1973; jaarvergadering april; 10 statutory bestuurders / voorzitter Zeno Verschaeve / ondervoorzitters Kristof Vandamme + Stijn Tant; NACE 38.330. Hunt leftover AGB/zorg/EVA first: leftover AGB Mechelen/Kortrijk/Brugge/Roeselare/Oostende 404/403 as of 1375 — not re-probed once live MIROM Menen extracted; Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live MIROM Menen extracted; IVAREM still 2024 as of 1375; leftover APB provincieantwerpen.be 403. MIROM Menen statutory CDN live this tick (HTTP 200 / 7857251 / 164p) — taken (preferred leftover IGS of mined Menen/Wevelgem/Wervik outside Nuhma). MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 already mined — skipped. De Nekker VZW 2026-00147494 2025 CDN still live — leftover next, not taken once live MIROM Menen extracted. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366. Not every-10 (next 1380).
- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud; 6.1/6.2.2/6.2.4-6.2.5/6.3.4-6.3.6/6.4.1-6.4.2/6.5.1-6.5.2/6.7.2/6.8/6.14/6.15/6.17/6.18.1-6.18.2/6.20 not filed; 6.10 category empty / geo BE only; 8761/8762 empty): assets **11.706.411** (was 12.881.099); fixed **3.901.408** / MVA **3.894.819** (gebouwen **1.290.259**; machines **2.083.295 JUMP** vs 1.808.362 after aanschaf **636.719**; rollend **521.266** aanschaf 150.507; CIP empty); FVA 6.589; current **7.805.003**; LT recv **0 DROP** vs 2.640.000; inventory **350.589**; ST recv **2.461.225** (trade 1.600.318 + other **860.907 JUMP** vs 376.331); beleggingen **3.432.201 JUMP** vs 2.707.015 (8689 unnamed); cash **1.447.446 DROP** vs 1.629.275; equity **8.626.785** (inbreng 2.652.670 / +29.233 / 85.570 aandelen; reserves 1.167.505; overgedragen 3.942.241; capsub 830.155); voorzieningen **0 DROP** vs 2.640.000 pensioen (terugneming 2.640.000 + nr-kosten 664/7 2.640.000); schulden **3.079.626** (LT bank **215.000** 1–5j; ST **1.852.916** waarvan current bank 220.000 + leveranciers **1.254.857 JUMP** vs 877.082); omzet **5.510.522** vs 5.496.006 (6.10 category empty); andere opbr **4.366.684** (740 subsidies 515.641; ~3.851.043 unnamed); nr-opbr **2.705.306**; diensten **4.769.777** (86,6% of omzet); pers **2.712.524** / **36,5 VTE** / 41 koppen + uitzend **0,7 VTE / 49.466**; afschr 749.980; andere kosten 544.339; nr-kosten **2.641.549**; expl **+613.455** vs 510.453; fin opbr 155.853 (capsub 120.254); fin kosten 12.799; PnL **747.277** vs 631.416 overgedragen; bestuurders 33.904; commissaris 6.975. Responsabilisering future jan.26 **71.804** rising to jan.32 **287.745** (Menen 41,5% / Wevelgem 35,9% / Wervik 22,6%).
- CSVs: sources+4/entities+1/budgets+58/commitments+1/leaderboard+1 + FOI ready `gap_miromn_othops_4_37m_diensten_4_77m_pens_2_64m_l5` (not sent); rq_1377=done; spawn rq_1378; ticks=1377.
- Coverage: residual dual L5 (MIROM Menen leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1380).
- Next: rq_1378 residual dual L5 VL JR2025 hole_fill (prefer leftover De Nekker VZW 0450.062.281 CDN 2026-00147494 if still live; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS CDN 2026-00254280 / Rematics / Sunfin only if taken after leftover IGS; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; IVAREM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1377 write done")


if __name__ == "__main__":
    main()

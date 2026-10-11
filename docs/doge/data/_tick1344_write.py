# -*- coding: utf-8 -*-
"""Tick 1344 — leftover IGS ILvA Land van Aalst JR2025 WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10 (next every-10 is 1350).
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1344"
UTC = "2026-08-18T06:15:00Z"
ENT = "igs_ilva"
HIER = "Vlaanderen>OostVlaanderen>IGS>ILvA>LandVanAalst"
GAP = "gap_ilva_cityfee_31_81m_pers_19_65m_expl_neg_l5"
SRC = "src_ilva_jr2025_pdf"
SRC2 = "src_ilva_site"
SRC3 = "src_kbo_ilva_0862014551"
SRC4 = "src_ilva_foi_contact"
SRC_URL = "https://www.ilva.be/volumes/general/Jaarverslagen/2025-jaarverslag_LR.pdf"
SRC2_URL = "https://www.ilva.be/over-ilva/publicaties"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0862014551"
SRC4_URL = "https://www.ilva.be/over-ilva/contact"
FOI_EMAIL = "info@ilva.be"
FOI_POSTAL = "Industrielaan 18 9320 Aalst (Erembodegem)"
DRAFT = "docs/doge/foi/drafts/gap_ilva_cityfee_31_81m_pers_19_65m_expl_neg_l5.md"
COMM = "comm_ilva_jr2025_cityfee"
LB = "lb_ilva_cityfee_31_81m_pers_19_65m"


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
                "title": "ILvA jaarverslag boekjaar 2025 (official PDF + embedded WVV VOL-inb; AV 23.06.2026)",
                "url": SRC_URL,
                "publisher": "ILvA Opdrachthoudend samenwerkingsverband Land van Aalst voor Milieu",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1344; official PDF 7.15MB 90p InDesign 22.06.2026; AV 23.06.2026; "
                    "WVV VOL-inb ILvA 0862.014.551 39p embedded; leftover IGS of mined Aalst-region cities; not BBC J1-J5"
                ),
            },
            {
                "source_id": SRC2,
                "title": "ILvA official publicaties page (Jaarverslag 2025 listed)",
                "url": SRC2_URL,
                "publisher": "ILvA",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1344; HTTP 200 lists 2025-jaarverslag_LR.pdf 7.15MB last-modified 24.06.2026; "
                    "leftover IGS of mined East-Flanders Aalst-region cities"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO ILvA Land van Aalst 0862.014.551",
                "url": SRC3_URL,
                "publisher": "KBO Besloten vennootschap Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1344; KBO 0862.014.551 Actief / normale toestand since 04.12.2003; "
                    "statutaire naam Opdrachthoudend samenwerkingsverband Land van Aalst voor Milieu since 31.10.2003; "
                    "afkorting ILvA since 31.10.2003; Opdrachthoudende vereniging (Vlaams Gewest) since 31.10.2003; "
                    "zetel Industrielaan 18 9320 Aalst since 06.10.2010; 20 VE; RSZ since 01.01.2022; "
                    "btw since 01.12.2003; aanbestedende overheid since 31.10.2003; kapitaal 747450; "
                    "boekjaar 31 december; NACE 38.110"
                ),
            },
            {
                "source_id": SRC4,
                "title": "ILvA contact / hoofdzetel (FOI channel)",
                "url": SRC4_URL,
                "publisher": "ILvA",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1344; FOI info@ilva.be from official contact page; "
                    "Industrielaan 18 9320 Aalst (Erembodegem); T 053 83 88 48"
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
                "name_nl": "ILvA Opdrachthoudend samenwerkingsverband Land van Aalst voor Milieu (leftover IGS)",
                "name_fr": "ILvA intercommunale Land van Aalst (association missionnee / IGS residuel)",
                "name_en": "ILvA Land van Aalst waste intermunicipal (leftover IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.ilva.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1344 leftover IGS residual of mined Aalst-region cities Aalst/Geraardsbergen/Zottegem/Ninove/Herzele/Lede/Liedekerke/Affligem/Haaltert/Sint-Lievens-Houtem/Kluisbergen/Denderleeuw/Erpe-Mere/Oosterzele/Pajottegem; "
                    "KBO 0862.014.551 Actief since 04.12.2003; official JR2025 WVV PDF downloads; "
                    "assets 47.881m city-fee 31.813m pers 19.653m expl -177.039 PnL 0; "
                    "FOI ready city-fee/dual-city/WIPS/NBB"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_ilva_assets_2025", ENT, "2025", "47881079", "2025 assets 47881078.62 was 49112733.16; tick1344; primary WVV in official PDF"),
        ("bud_ilva_fixed_2025", ENT, "2025", "30284912", "2025 vaste activa 30284912.34 was 30477086.18; tick1344; primary WVV"),
        ("bud_ilva_iva_2025", ENT, "2025", "99377", "2025 IVA 99376.68 was 165684.13; tick1344; primary WVV"),
        ("bud_ilva_mva_2025", ENT, "2025", "30169626", "2025 MVA 30169625.89 (gebouwen 13986341.55 + installaties 6065266.05 + rollend 7492948.83 + overige 2094446.52 + CIP 530622.94); tick1344; primary WVV"),
        ("bud_ilva_fva_2025", ENT, "2025", "15910", "2025 FVA 15909.77 (aandelen 2635.15 + borg 13274.62); tick1344; primary WVV"),
        ("bud_ilva_current_2025", ENT, "2025", "17596166", "2025 vlottende activa 17596166.28 was 18635646.98; tick1344; primary WVV"),
        ("bud_ilva_lt_recv_2025", ENT, "2025", "5058919", "2025 LT other recv 5058918.61 WIPS GFT-installatie was 5166724.93; tick1344; primary WVV"),
        ("bud_ilva_stock_2025", ENT, "2025", "73466", "2025 voorraden 73466.19 was 107344.52; tick1344; primary WVV"),
        ("bud_ilva_st_recv_2025", ENT, "2025", "3528208", "2025 ST recv 3528208.29 JUMP vs 1879314.05 (trade 3128971.33); tick1344; primary WVV"),
        ("bud_ilva_invest_2025", ENT, "2025", "6700000", "2025 geldbeleggingen 6700000.00 DROP vs 9000000.00; tick1344; primary WVV"),
        ("bud_ilva_cash_2025", ENT, "2025", "1960567", "2025 cash 1960566.90 DROP vs 2071419.35; tick1344; primary WVV"),
        ("bud_ilva_accr_asset_2025", ENT, "2025", "275006", "2025 overlopende activa 275006.29 was 410844.13; tick1344; primary WVV"),
        ("bud_ilva_equity_2025", ENT, "2025", "16416740", "2025 equity 16416739.67 was 16503719.66; tick1344; primary WVV"),
        ("bud_ilva_inbreng_2025", ENT, "2025", "1088227", "2025 inbreng 1088227.37 was 1083727.37 (+4500 / 180 aandelen); tick1344; primary WVV"),
        ("bud_ilva_reserves_2025", ENT, "2025", "12912314", "2025 reserves 12912313.62 all onbeschikbaar; tick1344; primary WVV"),
        ("bud_ilva_capsu_2025", ENT, "2025", "2042076", "2025 kapitaalsubsidies 2042075.57 was 2133555.56; tick1344; primary WVV"),
        ("bud_ilva_prov_2025", ENT, "2025", "6561296", "2025 voorzieningen 6561295.74 other risks (deponie nazorg) was 6840846.09; tick1344; primary WVV"),
        ("bud_ilva_debt_2025", ENT, "2025", "24903043", "2025 schulden 24903043.21 was 25768167.41; tick1344; primary WVV 17/49"),
        ("bud_ilva_lt_fin_2025", ENT, "2025", "11881946", "2025 LT financial banken 11881945.65 was 9989419.68; tick1344; primary WVV"),
        ("bud_ilva_st_debt_2025", ENT, "2025", "12683707", "2025 ST schulden 12683706.61 was 15416883.63; tick1344; primary WVV"),
        ("bud_ilva_st_ltcurr_2025", ENT, "2025", "2923627", "2025 LT-within-year 2923626.92; tick1344; primary WVV"),
        ("bud_ilva_trade_pay_2025", ENT, "2025", "1512227", "2025 leveranciers 1512226.56 DROP vs 3946432.52; tick1344; primary WVV"),
        ("bud_ilva_taxsoc_2025", ENT, "2025", "2835919", "2025 tax/soc 2835918.79 (tax 537502.63 + wages 2298416.16); tick1344; primary WVV"),
        ("bud_ilva_other_st_2025", ENT, "2025", "5411934", "2025 overige ST schulden 5411934.34 (diftar + provincie project); tick1344; primary WVV"),
        ("bud_ilva_ops_rev_2025", ENT, "2025", "42428356", "2025 bedrijfsopbrengsten 42428356.05 was 39975379.22; tick1344; primary WVV"),
        ("bud_ilva_turnover_2025", ENT, "2025", "40616039", "2025 omzet 40616039.33 was 38498386.62; tick1344; primary WVV; no 6.10 split"),
        ("bud_ilva_cityfee_2025", ENT, "2025", "31812747", "2025 narrative city voorschotten 31095000 + afrekening 717747 so result zero; tick1344; primary WVV commentary not 6.10"),
        ("bud_ilva_otherops_2025", ENT, "2025", "1338607", "2025 andere bedrijfsopbrengsten 1338606.99 was 1476992.60; tick1344; primary WVV code 74"),
        ("bud_ilva_subsidy_2025", ENT, "2025", "252806", "2025 exploitatiesubsidies code 740 252806.10 was 184778.00; tick1344; primary WVV 6.10"),
        ("bud_ilva_nonrec_2025", ENT, "2025", "473710", "2025 niet-recurrente bedrijfsopbrengsten 473709.73 Ninove recyclagepark sale; tick1344; primary WVV 76A"),
        ("bud_ilva_ops_cost_2025", ENT, "2025", "42605395", "2025 bedrijfskosten 42605395.11 was 40555563.34; tick1344; primary WVV"),
        ("bud_ilva_goods_2025", ENT, "2025", "536126", "2025 handelsgoederen 536125.76; tick1344; primary WVV"),
        ("bud_ilva_services_2025", ENT, "2025", "17478059", "2025 diensten 17478059.14 was 16455244.84; tick1344; primary WVV"),
        ("bud_ilva_pers_2025", ENT, "2025", "19652919", "2025 bezoldigingen 19652918.77 was 17710979.25; tick1344; primary WVV; VTE 290.2 / 298 koppen"),
        ("bud_ilva_uitzend_2025", ENT, "2025", "425952", "2025 uitzend 425952.39 VTE 7.5; tick1344; primary WVV 6.10"),
        ("bud_ilva_ops_2025", ENT, "2025", "-177039", "2025 bedrijfsverlies -177039.06 was -580184.12; tick1344; primary WVV 9901"),
        ("bud_ilva_fin_inc_2025", ENT, "2025", "499336", "2025 fin opbr 499336.37 (vlottend 214120.09 + andere 278988.61 capsu); tick1344; primary WVV"),
        ("bud_ilva_fin_cost_2025", ENT, "2025", "240438", "2025 fin kosten 240437.60 (schulden 217204.14); tick1344; primary WVV"),
        ("bud_ilva_pnl_pretax_2025", ENT, "2025", "81860", "2025 PnL before tax 81859.71; tick1344; primary WVV 9903"),
        ("bud_ilva_tax_2025", ENT, "2025", "81860", "2025 belasting 81859.71; tick1344; primary WVV 67/77"),
        ("bud_ilva_pnl_2025", ENT, "2025", "0", "2025 PnL 0.00 nulresultaat after tax + municipal settlement; tick1344; primary WVV 9904 blank"),
        ("bud_ilva_comm_fee_2025", ENT, "2025", "17877", "2025 commissaris KPMG 17877.00; tick1344; primary WVV 6.16"),
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
                "title": "ILvA Land van Aalst JR2025 leftover IGS dual (city fee 31.81m / pers 19.65m / expl NEG / WIPS 5.06m)",
                "entity_id": ENT,
                "beneficiary": "ILvA / vennoten Aalst Affligem Denderleeuw Erpe-Mere Pajottegem Geraardsbergen Haaltert Herzele Kluisbergen Lede Liedekerke Ninove Oosterzele Sint-Lievens-Houtem Zottegem",
                "legal_basis": "Decreet lokaal bestuur IGS; opdrachthoudende vereniging; Bestuursdecreet openbaarheid; WVV neerlegging",
                "decision_date": "2026-06-23",
                "start_year": "2003",
                "end_year": "2025",
                "total_envelope_eur": "42428356",
                "cash_by_year": "",
                "remaining_eur": "16416740",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL Land van Aalst — city fee / dual city lines; WIPS/NBB missing",
                "cut_option": "Publish per-vennoot 31.81m city-fee + dual city lines + WIPS 5.06m + deponie 6.56m; do not recreate parallel waste-IGS shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1344; assets 47881079 cityfee 31812747 pers 19652919 expl -177039 PnL 0 VTE 290.2; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "ILvA Land van Aalst JR2025 leftover IGS: city fee 31.81m / pers 19.65m / expl NEG / WIPS 5.06m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "19652919",
                "total_cost_eur": "42428356",
                "tco_notes": "Leftover dual IGS of mined Aalst-region cities: ops rev 42.43m / city fee 31.81m / pers 19.65m VTE 290.2 / assets 47.88m / WIPS 5.06m / expl -0.18m / PnL 0; do not treat 42.43m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "ILvA / 15 Aalst-region gemeenten / waste-IGS",
                "stated_goal": "Local leftover IGS map VL Land van Aalst — JR2025 PDF live; dual city-fee/WIPS/NBB FOI",
                "measured_outcome": "Official PDF 2026-08-17: assets 47.88m / city fee 31.81m / pers 19.65m / expl -177.0k / PnL 0 / VTE 290.2",
                "absurdity_score": "6.5",
                "cost_score": "7.4",
                "difficulty": "3.1",
                "priority_index": "6.8",
                "cut_proposal": "Publish per-vennoot 31.81m city-fee + dual city lines + WIPS 5.06m + deponie 6.56m; do not recreate parallel waste-IGS shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1344; leftover IGS of mined Aalst-region cities; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "Per-vennoot 2025-2026 dual lines for municipal inzameling/verwerking fee "
                    "(narrative voorschotten 31095000 + afrekening 717747) vs omzet 40616039.33 "
                    "(no 6.10 split) + counterparties/age of ST recv 3528208.29 JUMP vs 1879314.05 "
                    "(trade 3128971.33) + LT recv WIPS GFT 5058918.61 + diensten 17478059.14 vs "
                    "pers 19652918.77 VTE 290.2 / 298 koppen + uitzend 425952.39 VTE 7.5 + "
                    "voorzieningen deponie 6561295.74 (terugname 279550.35) + NBB filing proof "
                    "+ commissarisverslag KPMG Wim Heyndrickx / AV 23.06.2026"
                ),
                "why_it_matters": (
                    "Leftover IGS shell of mined Aalst-region cities Aalst/Geraardsbergen/"
                    "Zottegem/Ninove/Herzele/Lede/Liedekerke/Affligem/Haaltert/"
                    "Sint-Lievens-Houtem/Kluisbergen/Denderleeuw/Erpe-Mere/Oosterzele/"
                    "Pajottegem: 42.43m ops / 31.81m city-fee vs 19.65m personnel and "
                    "5.06m WIPS LT recv is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "ILvA Opdrachthoudend samenwerkingsverband Land van Aalst voor Milieu / vennoten Aalst Affligem Denderleeuw Erpe-Mere Pajottegem Geraardsbergen Haaltert Herzele Kluisbergen Lede Liedekerke Ninove Oosterzele Sint-Lievens-Houtem Zottegem",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM,
                "linked_leaderboard_id": LB,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "tick1344 leftover IGS of mined Aalst-region cities after honest hunt; "
                    "live JR2025 official WVV PDF now downloads (7.15MB 90p VOL-inb AV 23.06.2026). "
                    "Interleuven 2025 jaarverslag klaar but still no 2025 balans PDF — not taken. "
                    "IOK/IMOG/Haviland still 2024. EcoWerf glossy 16MB statutory still unpublished. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1344",
        "title": "ILvA Land van Aalst JR2025 leftover IGS dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: ILvA leftover IGS of mined Aalst-region cities after honest hunt; "
            "KBO 0862.014.551 Actief; live JR2025 official WVV PDF (7.15MB 90p VOL-inb AV 23.06.2026); "
            "sourced euros assets 47.881m / city-fee 31.813m / pers 19.653m / expl -177.039 / PnL 0 / VTE 290.2; "
            "FOI ready city-fee/dual-city/WIPS/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T05:20:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1344 ILvA leftover IGS residual; KBO 0862.014.551; live JR2025 WVV PDF; "
            "sourced euros; FOI ready not sent; next rq_1345 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1345",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1344 done including ILvA Land van Aalst 1344 leftover IGS live WVV / "
            "IVM Meetjesland 1343 leftover IGS live WVV / "
            "IDM Durme-Moervaart 1342 leftover IGS live WVV / "
            "IGEAN dienstverlening 1341 leftover IGS live WVV / "
            "EVA Limburg Sterk Merk 1340 leftover EVA live WVV + every-10 / "
            "WV Zorgbedrijf Brasschaat 1339 leftover zorg live BBC / "
            "WV Zorgband 1338 leftover zorg live BBC / WV Sleutelzorg 1337 leftover zorg FOI-unpublished / "
            "WV Weldenderend 1336 leftover zorg live BBC / WV BVK 1335 leftover zorg live BBC / "
            "WV OPcura 1334 leftover zorg live BBC / WV Het Dak 1333 leftover zorg live BBC / "
            "EVA Inagro 1332 FOI-unpublished / APB Vormingscentrum Malle 1331 FOI-glossy-not-BBC / "
            "EVA Kinderopvang Dilbeek 1330 FOI-unpublished + every-10); "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "Welzijnskoepel West-Brabant jaarverslag 2025 glossy-only — take only if a BBC PDF now downloads; "
            "Ter Nethe official still unpublished/DNS — take only if a PDF now downloads; "
            "Veneco glossy 25MB jaarverslag 2025 InDesign — take only if a WVV/BBC PDF now downloads; "
            "EcoWerf glossy 16MB jaarverslag 2025 / statutory jaarrekening still unpublished — take only if a WVV/BBC PDF now downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland / IVBO / IVIO / Limburg.net still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
            "WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / "
            "WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / "
            "Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / "
            "APB Vonk 1325 / APB Campus Vesta 1324 / AGB Blankenberge 1323 / AGB Aarschot / AGB Arendonk / AGB Lokeren; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403; not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1344 after ILvA leftover IGS live WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1344", rq_new, rq_spawn)
    print("research_queue 1344", found, "spawned_1345", spawned)

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
                "last_unit_id": "rq_1344",
                "ticks_completed": "1344",
                "paused": "no",
                "notes": (
                    "tick1344 ILvA leftover IGS residual; KBO 0862.014.551; "
                    "live JR2025 WVV PDF; sourced euros assets 47.881m city-fee 31.813m pers 19.653m expl -177.039 PnL 0; "
                    "FOI ready; next rq_1345 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log_entry = """
### Tick 1344 - 2026-08-18 - rq_1344 ILvA Land van Aalst dual residual leftover IGS
- Unit: ILvA Opdrachthoudend samenwerkingsverband Land van Aalst voor Milieu (leftover IGS) of already-mined Aalst-region cities (Aalst + SportAG/AGSA / Geraardsbergen + AGB / Zottegem + AGB / Ninove + AGB / Herzele + AGB / Lede / Liedekerke / Affligem / Haaltert / Sint-Lievens-Houtem / Kluisbergen / Denderleeuw / Erpe-Mere / Oosterzele + AGB De Kluize / Pajottegem) after residual dual hunt (KBO **0862.014.551**; official ilva.be + live jaarverslag 2025 PDF 7.15MB / 90p; AV **23.06.2026**; WVV VOL-inb 39p embedded). Prefer live PDF over another unpublished FOI. Distinct from already-mined IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340. KBO Actief / normale toestand since **04.12.2003**; statutaire naam Opdrachthoudend samenwerkingsverband Land van Aalst voor Milieu since 31.10.2003; afkorting ILvA since 31.10.2003; Opdrachthoudende vereniging (Vlaams Gewest) since 31.10.2003; zetel Industrielaan 18 9320 Aalst since 06.10.2010; **20 VE**; RSZ-werkgever since 01.01.2022; btw since 01.12.2003; aanbestedende overheid since 31.10.2003; kapitaal KBO 747.450; boekjaar 31 december; voorzitter Frederik Meulewaeter; AD Bart Rooms; commissaris KPMG / Wim Heyndrickx since 18.06.2024; e-mail info@ilva.be on contact page; tel 053 83 88 48; NACE 38.110. Hunt leftover AGB/zorg/EVA first: Interleuven 2025 jaarverslag "klaar" + LinkedIn AV 17.06.2026 approved, but publications page still only jaarrekening 2024 PDF — not taken; IOK/IMOG/Haviland still 2024; EcoWerf glossy 16MB jaarverslag 2025 listed but statutory jaarrekening "wordt weldra gepubliceerd" — not taken once live ILvA WVV downloaded; IVBO/IVIO/Limburg.net still 2024; IVAREM activiteitenverslag glossy; Veneco glossy 25MB InDesign — not mined as BBC; Dommelhof leftover Limburg EVA KBO 0777.495.085 not taken once live ILvA PDF downloaded. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek not taken once live ILvA PDF downloaded. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331. Not every-10 (next 1350).
- EUR strong (primary WVV VOL-inb in official PDF): assets **47.881.079** (was 49.112.733); fixed **30.284.912**; IVA **99.377**; MVA **30.169.626** (gebouwen **13.986.342** + installaties **6.065.266** + rollend **7.492.949** + overige **2.094.447** + CIP **530.623**); FVA **15.910**; current **17.596.166**; LT recv **5.058.919** (WIPS GFT); voorraden **73.466**; ST recv **3.528.208** JUMP vs 1.879.314 (trade **3.128.971**); beleggingen **6.700.000** DROP vs 9.000.000; cash **1.960.567** DROP vs 2.071.419; equity **16.416.740**; inbreng **1.088.227**; reserves **12.912.314**; kapitaalsubsidies **2.042.076**; voorzieningen **6.561.296**; schulden **24.903.043**; LT fin **11.881.946**; ST **12.683.707** (LT-within-year **2.923.627** + trade **1.512.227** + tax/soc **2.835.919** + other **5.411.934**); ops rev **42.428.356**; omzet **40.616.039** (no 6.10 split; narrative city voorschotten **31.095.000** + afrekening **717.747**); andere bedrijfsopbrengsten **1.338.607** (subsidies 740 **252.806**); non-recurrent **473.710** (Ninove park); pers **19.652.919**; VTE **290,2** / 298 koppen; uitzend **425.952** VTE 7,5; diensten **17.478.059**; expl **−177.039**; fin opbr **499.336**; fin kosten **240.438**; PnL vóór belasting **81.860**; belasting **81.860**; PnL **0,00**. Commissaris KPMG **17.877**.
- CSVs: sources+4/entities+1/budgets+42/commitments+1/leaderboard+1 + FOI ready `gap_ilva_cityfee_31_81m_pers_19_65m_expl_neg_l5` (not sent); rq_1344=done; spawn rq_1345; ticks=1344.
- Coverage: residual dual L5 (ILvA leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1345 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland/IVBO/IVIO/Limburg.net only if a 2025 JR PDF now downloads; EcoWerf only if a statutory WVV/BBC PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 unless a fetchable JR appears).
"""
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1344 write done")


if __name__ == "__main__":
    main()

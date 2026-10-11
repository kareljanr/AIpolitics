# -*- coding: utf-8 -*-
"""Tick 1373 — leftover IVOO JR2025 official NBB WVV euros.
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

TICK = "1373"
UTC = "2026-08-19T03:25:00Z"
ENT = "igs_ivoo"
HIER = "Vlaanderen>WestVlaanderen>IGS>IVOO>OostendeOmmeland"
GAP = "gap_ivoo_omzet_16_55m_diensten_12_39m_aec_l5"
SRC = "src_ivoo_jr2025_nbb"
SRC2 = "src_ivoo_site"
SRC3 = "src_kbo_ivoo_0214753050"
SRC4 = "src_ivoo_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00271895.pdf"
SRC2_URL = "https://www.ivoo.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0214753050"
SRC4_URL = "https://www.ivoo.be/nl/contact"
FOI_EMAIL = "info@ivoo.be"
FOI_POSTAL = "Klokhofstraat 2 8400 Oostende"
DRAFT = "docs/doge/foi/drafts/gap_ivoo_omzet_16_55m_diensten_12_39m_aec_l5.md"
COMM = "comm_ivoo_jr2025_pnl"
LB = "lb_ivoo_omzet_16_55m_diensten_12_39m_aec"


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
                "title": "IVOO jaarrekening boekjaar 2025 (official NBB WVV VOL-kap deposit 2026-00271895; AV 15.06.2026)",
                "url": SRC_URL,
                "publisher": "IVOO / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1373; official NBB VOL-kap PDF 1.56MB 91p deposit 2026-00271895 created 09.07.2026; "
                    "leftover IGS OV of Oostende-Ommeland municipalities; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Walter HOSTEN BV B00196 / Walter Hosten A01441 11500 signed 24.04.2026; "
                    "oordeel zonder voorbehoud assets 10739335.61 / PnL -882826.75 + emphasis 6.20 no new AEC permit after 2033; "
                    "6.1/6.2.1-6.2.5/6.3.4-6.3.5/6.4.1-6.4.2/6.5.1-6.5.2/6.7.2/6.8/6.15/6.17/6.18 not filed; "
                    "6.10 category/geo empty; 740 empty; not every-10"
                ),
            },
            {
                "source_id": SRC2,
                "title": "IVOO official site (waste IGS Oostende en Ommeland)",
                "url": SRC2_URL,
                "publisher": "IVOO Intercommunale",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1373; leftover IGS waste of Bredene/Gistel/Ichtegem/Middelkerke/Oostende/Oudenburg + B-zuster IGS; "
                    "ivoo.be has no isolated statutory 2025 balans PDF; statutory 2025 balans is the NBB CDN deposit"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO IVOO 0214.753.050",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1373; KBO 0214.753.050 Actief / normale toestand since 04.11.1974; "
                    "statutaire naam Intergemeentelijke Vereniging voor het afvalbeheer voor Oostende en Ommeland since 16.12.2003; "
                    "afkorting I.V.O.O. since 04.11.1974; Opdrachthoudende vereniging (Vlaams Gewest) since 25.05.1993; "
                    "zetel Klokhofstraat 2 8400 Oostende since 21.01.1998; 1 VE; "
                    "btw since 01.05.1980; RSZ since 01.01.2022; aanbestedende overheid since 04.11.1974; "
                    "jaarvergadering mei; boekjaar 31 december; "
                    "17 KBO-bestuurders; NACE 38.330/35.110"
                ),
            },
            {
                "source_id": SRC4,
                "title": "IVOO FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "IVOO",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1373; FOI info@ivoo.be / 059 55 27 30; "
                    "Klokhofstraat 2 8400 Oostende; statutory deposit also lists boekhouding@ivoo.be"
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
                "name_nl": "IVOO (leftover opdrachthoudende vereniging / IGS afval Oostende-Ommeland)",
                "name_fr": "IVOO (association chargee de mission residuelle / IGS dechets Ostende-Ommeland)",
                "name_en": "IVOO leftover Ostend-region waste IGS (mission association)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.ivoo.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1373 leftover residual IGS OV of Oostende-Ommeland; "
                    "KBO 0214.753.050 Actief since 04.11.1974; official NBB WVV VOL-kap PDF downloads; "
                    "sourced euros assets 10739336 omzet 16545262 diensten 12388023 pnl -882827; "
                    "FOI ready omzet 16.55m/diensten 12.39m/AEC"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_ivoo_assets_2025", ENT, "2025", "10739336", "2025 assets 10739336 VOL-kap 20/58 (commissaris 10739335.61); tick1373; primary official NBB WVV"),
        ("bud_ivoo_assets_2024", ENT, "2024", "12310972", "2024 assets 12310972 comparative; tick1373; primary official NBB WVV 20/58"),
        ("bud_ivoo_fixed_2025", ENT, "2025", "2321635", "2025 vaste activa 2321635 vs 2548336; tick1373; primary official NBB WVV 21/28"),
        ("bud_ivoo_mva_2025", ENT, "2025", "2280717", "2025 MVA 2280717 vs 2508669; tick1373; primary official NBB WVV 22/27"),
        ("bud_ivoo_buildings_2025", ENT, "2025", "678141", "2025 terreinen en gebouwen 678141 vs 673856 after aanschaf 25968 + afschr 21683; tick1373; primary official NBB WVV 22"),
        ("bud_ivoo_machines_2025", ENT, "2025", "1575822", "2025 installaties/machines 1575822 vs 1834813 (aanschaf 30520136 / afschr cum 30374125 after 258991); tick1373; primary official NBB WVV 23"),
        ("bud_ivoo_machines_acq_2025", ENT, "2025", "30520136", "2025 machines aanschafwaarde 30520136 almost fully depreciated; tick1373; primary official NBB WVV 6.3.2 8192"),
        ("bud_ivoo_rollend_2025", ENT, "2025", "0", "2025 meubilair/rollend 0 (aanschaf 301240 / afschr 302383); tick1373; primary official NBB WVV 24"),
        ("bud_ivoo_cip_2025", ENT, "2025", "26754", "2025 activa in aanbouw 26754 new; tick1373; primary official NBB WVV 27"),
        ("bud_ivoo_fva_2025", ENT, "2025", "40917", "2025 FVA 40917 (aandelen 37149 after aankoop 1250 + borg 3768; 6.4.1/6.5.1 not filed); tick1373; primary official NBB WVV 28"),
        ("bud_ivoo_current_2025", ENT, "2025", "8417701", "2025 vlottende activa 8417701 vs 9762635; tick1373; primary official NBB WVV 29/58"),
        ("bud_ivoo_inv_2025", ENT, "2025", "447998", "2025 voorraden 447998 (grond-hulp 415040 + handels 32958); tick1373; primary official NBB WVV 3"),
        ("bud_ivoo_strecv_2025", ENT, "2025", "5023983", "2025 ST vorderingen 5023983 (trade 5008252 + other 15732); tick1373; primary official NBB WVV 40/41"),
        ("bud_ivoo_cash_2025", ENT, "2025", "2772205", "2025 liquide middelen 2772205 JUMP vs 1303878; no bank debt; tick1373; primary official NBB WVV 54/58"),
        ("bud_ivoo_cash_2024", ENT, "2024", "1303878", "2024 liquide middelen 1303878 comparative; tick1373; primary official NBB WVV 54/58"),
        ("bud_ivoo_prepaid_2025", ENT, "2025", "173515", "2025 overlopend actief 173515 all over te dragen kosten; tick1373; primary official NBB WVV 490/1"),
        ("bud_ivoo_equity_2025", ENT, "2025", "4431321", "2025 eigen vermogen 4431321 vs 5321130; tick1373; primary official NBB WVV 10/15"),
        ("bud_ivoo_inbreng_2025", ENT, "2025", "3373725", "2025 kapitaal 3373725 (A 3372225 / 134889 + B 1500 / 60; 134949 aandelen op naam); tick1373; primary official NBB WVV 10"),
        ("bud_ivoo_reserves_2025", ENT, "2025", "963165", "2025 reserves 963165 (wettelijk 337373 + beschikbaar 625793; belastingvrij 0 vs 697636); tick1373; primary official NBB WVV 13"),
        ("bud_ivoo_capsub_2025", ENT, "2025", "91633", "2025 kapitaalsubsidies 91633 vs 98616; tick1373; primary official NBB WVV 15"),
        ("bud_ivoo_prov_2025", ENT, "2025", "2341455", "2025 voorzieningen 2341455 DROP vs 3499117 (pensioen 78585 + grote herstelling 2262870); tick1373; primary official NBB WVV 16"),
        ("bud_ivoo_prov_repair_2025", ENT, "2025", "2262870", "2025 voorziening grote herstelling 2262870 vs 3387478; tick1373; primary official NBB WVV 162"),
        ("bud_ivoo_prov_used_2025", ENT, "2025", "1157662", "2025 voorziening besteding/terugneming 1157662 / toevoeging 0 / netto 635/8 -1157662; tick1373; primary official NBB WVV 6.10 9116"),
        ("bud_ivoo_debt_2025", ENT, "2025", "3966560", "2025 schulden 3966560 vs 3490724; no LT; tick1373; primary official NBB WVV 17/49"),
        ("bud_ivoo_st_2025", ENT, "2025", "3936579", "2025 ST schulden 3936579 vs 3465858; tick1373; primary official NBB WVV 42/48"),
        ("bud_ivoo_sttrade_2025", ENT, "2025", "3104174", "2025 leveranciers 3104174 vs 2689400; tick1373; primary official NBB WVV 440/4"),
        ("bud_ivoo_sttaxsoc_2025", ENT, "2025", "768741", "2025 tax/soc 768741 (tax 498571 + wages 270170); tick1373; primary official NBB WVV 45"),
        ("bud_ivoo_stadv_2025", ENT, "2025", "59315", "2025 vooruitbetalingen 59315 vs 40279; tick1373; primary official NBB WVV 46"),
        ("bud_ivoo_accrued_2025", ENT, "2025", "29981", "2025 overlopend passief 29981 (kosten 5053 + opbr 24928); tick1373; primary official NBB WVV 492/3"),
        ("bud_ivoo_ops_2025", ENT, "2025", "16599504", "2025 bedrijfsopbrengsten 16599504 vs 18310640; tick1373; primary official NBB WVV 70/76A"),
        ("bud_ivoo_omzet_2025", ENT, "2025", "16545262", "2025 omzet 16545262 DROP vs 18253807; 6.10 category/geo empty; notes restafval 57481t / 6385540 + elektriciteit 1105810; tick1373; primary official NBB WVV 70"),
        ("bud_ivoo_omzet_2024", ENT, "2024", "18253807", "2024 omzet 18253807 comparative; tick1373; primary official NBB WVV 70"),
        ("bud_ivoo_restwaste_2025", ENT, "2025", "6385540", "2025 omzet restafval 6385540 / 57481 ton vs 72186 ton 2024; tick1373; primary jaarverslag in NBB PDF"),
        ("bud_ivoo_electric_2025", ENT, "2025", "1105810", "2025 omzet elektriciteit 1105810 / 13470 MWh DROP vs 20873; tick1373; primary jaarverslag in NBB PDF"),
        ("bud_ivoo_othops_2025", ENT, "2025", "54242", "2025 andere bedrijfsopbrengsten 54242 vs 56833; 740 subsidies empty; tick1373; primary official NBB WVV 74"),
        ("bud_ivoo_goods_2025", ENT, "2025", "1459596", "2025 handelsgoederen/grond-hulp 1459596 vs 2049685 (aankopen 1541318 / voorraad +81722); tick1373; primary official NBB WVV 60"),
        ("bud_ivoo_diensten_2025", ENT, "2025", "12388023", "2025 diensten 12388023 vs 12098327 (74.9pct of omzet; onderhoud AEC ca 2834020); tick1373; primary official NBB WVV 61"),
        ("bud_ivoo_diensten_2024", ENT, "2024", "12098327", "2024 diensten 12098327 comparative; tick1373; primary official NBB WVV 61"),
        ("bud_ivoo_aec_maint_2025", ENT, "2025", "2834020", "2025 onderhoud installatie ca 2834020 waarvan ovens 1171865; tick1373; primary jaarverslag in NBB PDF"),
        ("bud_ivoo_pers_2025", ENT, "2025", "3082731", "2025 bezoldigingen 3082731 / 34.1 VTE / 32 koppen / YE 31.5 VTE; tick1373; primary official NBB WVV 62 9087"),
        ("bud_ivoo_deprec_2025", ENT, "2025", "280674", "2025 afschrijvingen 280674; tick1373; primary official NBB WVV 630"),
        ("bud_ivoo_othcost_2025", ENT, "2025", "1294995", "2025 andere bedrijfskosten 1294995 (tax 400620 JUMP vs 5189 + other 894375); tick1373; primary official NBB WVV 640/8"),
        ("bud_ivoo_nrcost_2025", ENT, "2025", "90784", "2025 niet-recurrente bedrijfskosten 90784 all 664/7; tick1373; primary official NBB WVV 66A"),
        ("bud_ivoo_expl_2025", ENT, "2025", "-898763", "2025 bedrijfsverlies 898763 vs 519604; tick1373; primary official NBB WVV 9901"),
        ("bud_ivoo_expl_2024", ENT, "2024", "-519604", "2024 bedrijfsverlies 519604 comparative; tick1373; primary official NBB WVV 9901"),
        ("bud_ivoo_fininc_2025", ENT, "2025", "19528", "2025 financiele opbrengsten 19528 (vlottend 5393 + other 14135 waarvan capsub 6983); tick1373; primary official NBB WVV 75"),
        ("bud_ivoo_fincost_2025", ENT, "2025", "2104", "2025 financiele kosten 2104 (schulden 1581 + other 524); tick1373; primary official NBB WVV 65"),
        ("bud_ivoo_pnl_2025", ENT, "2025", "-882827", "2025 PnL 9904 -882827 vs -489969 (commissaris -882826.75); onttrokken aan reserves 882827; tick1373; primary official NBB WVV"),
        ("bud_ivoo_pnl_2024", ENT, "2024", "-489969", "2024 PnL -489969 comparative; tick1373; primary official NBB WVV 9904"),
        ("bud_ivoo_comm_2025", ENT, "2025", "11500", "2025 commissaris Walter HOSTEN 11500; tick1373; primary official NBB WVV 9505"),
        ("bud_ivoo_board_2025", ENT, "2025", "38036", "2025 bestuurders 38036; tick1373; primary official NBB WVV 9503"),
        ("bud_ivoo_vat_out_2025", ENT, "2025", "1834844", "2025 BTW door de vennootschap 1834844 vs 2483920; tick1373; primary official NBB WVV 6.13 9146"),
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
                "title": "IVOO JR2025 leftover IGS dual (assets 10.74m / omzet 16.55m DROP / diensten 12.39m / AEC wind-down / PnL -0.88m)",
                "entity_id": ENT,
                "beneficiary": "IVOO / Oostende-Ommeland municipalities / B-zuster IGS",
                "legal_basis": "WVV OV; decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-06-15",
                "start_year": "1974",
                "end_year": "2035",
                "total_envelope_eur": "10739336",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL waste — 16.55m omzet DROP vs 18.25m / 12.39m diensten / AEC no new permit after 2033",
                "cut_option": "Publish 16.55m omzet split + 12.39m diensten/top-20 + AEC wind-down study/scenarios + 2.26m repair provision + 30.52m machine gross; do not keep 10.74m municipal waste IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1373; assets 10739336 omzet 16545262 diensten 12388023 pnl -882827; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "IVOO JR2025 leftover IGS: assets 10.74m / omzet 16.55m DROP / diensten 12.39m / AEC wind-down / PnL -0.88m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "12388023",
                "total_cost_eur": "10739336",
                "tco_notes": (
                    "Leftover dual IGS OV of Oostende-Ommeland: "
                    "assets 10.74m / equity 4.43m / pnl -0.88m / omzet 16.55m DROP vs 18.25m / 34.1 VTE / "
                    "diensten 12.39m (74.9pct of omzet) / AEC no new permit after 2033 / machines gross 30.52m / "
                    "official NBB WVV live; "
                    "do not treat 10.74m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "IVOO / Oostende-Ommeland municipalities",
                "stated_goal": "Local leftover IGS map VL waste — JR2025 live; dual omzet-DROP/diensten/AEC FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 10.74m / omzet 16.55m DROP / diensten 12.39m / AEC wind-down / pnl -0.88m",
                "absurdity_score": "7.5",
                "cost_score": "6.5",
                "difficulty": "2.5",
                "priority_index": "6.8",
                "cut_proposal": "Publish 16.55m omzet split + 12.39m diensten/top-20 + AEC wind-down study/scenarios + 2.26m repair provision + 30.52m machine gross; do not keep 10.74m municipal waste IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1373; leftover IGS OV of Oostende-Ommeland; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "omzet 16545262 DROP vs 18253807 (WVV 70; 6.10 category/geo empty; notes restafval 57481t / 6385540 + elektriciteit 1105810) per stroom/tegenpartij "
                    "+ diensten 12388023 (74.9pct of omzet; WVV 61; onderhoud AEC ca 2834020 / ovens 1171865) top-20 leveranciers "
                    "+ AEC-afwikkeling 16.02.2026 geen nieuwe milieuvergunning na 07.02.2033 (6.20 + commissaris-emphasis) "
                    "+ voorziening grote herstelling 2262870 / besteding 1157662 + machines aanschaf 30520136 / net 1575822 "
                    "+ andere kosten 1294995 (tax 400620 JUMP vs 5189) + nr-kosten 90784 "
                    "+ 6.4.1/6.5.1/6.8/6.15/6.18 not filed + FVA aandelen 37149 + Creat Services / IVBO samenwerking"
                ),
                "why_it_matters": (
                    "Leftover IGS OV of Oostende-Ommeland municipalities "
                    "(same leftover-IGS waste seam as IMOG 1369 / IVBO 1352 / IVIO 1347 / IVVO 1345): "
                    "10.74m assets / 16.55m omzet DROP vs 18.25m / 12.39m diensten / "
                    "AEC wind-down after 2033 / 34.1 VTE / 6.10 empty "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "IVOO / Raad van Bestuur / Bredene / Gistel / Ichtegem / Middelkerke / Oostende / Oudenburg",
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
                    "tick1373 leftover IGS OV of Oostende-Ommeland after honest hunt; "
                    "live JR2025 official NBB WVV VOL-kap PDF now extracted (1.56MB 91p deposit 2026-00271895). "
                    "IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. "
                    "IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 skipped. "
                    "Dommelhof leftover Limburg EVA not re-probed once live IVOO extracted. "
                    "Otary RS Nuhma-adjacent fallback not taken. "
                    "MIWA 2026-00209388 2025 CDN still live — leftover next. "
                    "IVAREM still 2024. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1373",
        "title": "IVOO OV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: IVOO leftover IGS OV of Oostende-Ommeland after honest hunt; KBO 0214.753.050 Actief; "
            "live JR2025 official NBB WVV VOL-kap PDF (1.56MB 91p deposit 2026-00271895; commissaris Walter HOSTEN); "
            "sourced euros assets 10739336 / omzet 16545262 / diensten 12388023 / pnl -882827; "
            "FOI ready omzet 16.55m/diensten 12.39m/AEC"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T03:15:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1373 IVOO leftover IGS residual; KBO 0214.753.050; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1374 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1374",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1373 done including IVOO 1373 leftover IGS live NBB WVV / "
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
            "MIWA leftover IGS KBO 0218.239.409 — take if JR2025 CDN 2026-00209388 still live; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if a new live 2025 WVV PDF downloads (prefer leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; Otary CDN 2026-00254280 live prior tick, not taken); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1373 after IVOO leftover IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1373", rq_new, rq_spawn)
    print("research_queue 1373", found, "spawned_1374", spawned)

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
                "last_unit_id": "rq_1373",
                "ticks_completed": "1373",
                "paused": "no",
                "notes": (
                    "tick1373 IVOO leftover IGS residual; KBO 0214.753.050; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 10739336 omzet 16545262 diensten 12388023 pnl -882827; "
                    "FOI ready omzet 16.55m/diensten 12.39m/AEC; next rq_1374 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")
    print("tick1373 write done")


if __name__ == "__main__":
    main()

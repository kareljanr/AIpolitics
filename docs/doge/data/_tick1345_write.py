# -*- coding: utf-8 -*-
"""Tick 1345 — leftover IGS IVVO Veurne-Ommeland JR2025 WVV euros.
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

TICK = "1345"
UTC = "2026-08-18T20:15:00Z"
ENT = "igs_ivvo"
HIER = "Vlaanderen>WestVlaanderen>IGS>IVVO>VeurneOmmeland"
GAP = "gap_ivvo_omzet_17_57m_pers_3_27m_termijn_1_1m_l5"
SRC = "src_ivvo_jr2025_pdf"
SRC2 = "src_ivvo_site"
SRC3 = "src_kbo_ivvo_0213877575"
SRC4 = "src_ivvo_foi_contact"
SRC_URL = "https://www.ivvo.be/sites/default/files/2026-04/NIEUW-JV-2025.pdf"
SRC2_URL = "https://www.ivvo.be/over-ivvo/verslagen-en-documenten"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0213877575"
SRC4_URL = "https://www.ivvo.be/over-ivvo/wie-zijn-we"
FOI_EMAIL = "info@ivvo.be"
FOI_POSTAL = "Bargiestraat 6 8900 Ieper"
DRAFT = "docs/doge/foi/drafts/gap_ivvo_omzet_17_57m_pers_3_27m_termijn_1_1m_l5.md"
COMM = "comm_ivvo_jr2025_omzet"
LB = "lb_ivvo_omzet_17_57m_pers_3_27m"


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
                "title": "IVVO jaarverslag boekjaar 2025 (official PDF + embedded WVV VOL-inb; AV 16.06.2026)",
                "url": SRC_URL,
                "publisher": "IVVO Intercommunale Vereniging voor Vuilverwijdering en -verwerking voor de Veurne en Ommeland",
                "accessed_date": "2026-08-18",
                "source_class": "budget",
                "notes": (
                    "tick1345; official PDF 16.19MB 110p InDesign 11.06.2026; AV 16.06.2026; "
                    "WVV VOL-inb IVVO 0213.877.575 embedded p55-96; leftover IGS of mined Westhoek cities; not BBC J1-J5"
                ),
            },
            {
                "source_id": SRC2,
                "title": "IVVO official verslagen-en-documenten page (Jaarverslag 2025 listed)",
                "url": SRC2_URL,
                "publisher": "IVVO",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1345; HTTP 200 lists NIEUW-JV-2025.pdf 16.19MB path 2026-04; "
                    "leftover IGS of mined West-Flanders Westhoek/Ieper-Veurne-Kust cities"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO IVVO Veurne-Ommeland 0213.877.575",
                "url": SRC3_URL,
                "publisher": "KBO Besloten vennootschap Public Search FOD Economie",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1345; KBO 0213.877.575 Actief / normale toestand since 14.12.1973; "
                    "statutaire naam Intercommunale Vereniging voor Vuilverwijdering en -verwerking voor de Veurne en Ommeland since 14.12.1973; "
                    "afkorting I.V.V.O. since 14.12.1973; Opdrachthoudende vereniging (Vlaams Gewest) since 25.05.1993; "
                    "zetel Bargiestraat 6 8900 Ieper since 17.06.2014; 6 VE; RSZ since 01.01.2022; "
                    "btw since 01.04.1988; aanbestedende overheid since 14.12.1973; kapitaal 250000; "
                    "jaarvergadering mei; boekjaar 31 december; NACE 38.330"
                ),
            },
            {
                "source_id": SRC4,
                "title": "IVVO wie-zijn-we / hoofdzetel (FOI channel)",
                "url": SRC4_URL,
                "publisher": "IVVO",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1345; FOI info@ivvo.be from official PDF + KBO webadres field; "
                    "Bargiestraat 6 8900 Ieper; T 057 23 08 80; finance jan.masselin@ivvo.be on WVV ID"
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
                "name_nl": "IVVO Intercommunale Vereniging voor Vuilverwijdering en -verwerking voor de Veurne en Ommeland (leftover IGS)",
                "name_fr": "IVVO intercommunale Veurne et environs (association missionnee / IGS residuel)",
                "name_en": "IVVO Veurne-Ommeland waste intermunicipal (leftover IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.ivvo.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1345 leftover IGS residual of mined Westhoek cities Ieper/Veurne/Diksmuide/Poperinge/Koksijde/De Panne/Nieuwpoort/Heuvelland/Alveringem/Lo-Reninge/Mesen/Vleteren; "
                    "KBO 0213.877.575 Actief since 14.12.1973; official JR2025 WVV PDF downloads; "
                    "assets 24.422m omzet 17.566m pers 3.265m expl 789k PnL 903k; "
                    "FOI ready omzet/termijn/OVAM/NBB"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_ivvo_assets_2025", ENT, "2025", "24421533", "2025 assets 24421533.34 was 22459716.18; tick1345; primary WVV in official PDF; commissaris confirms"),
        ("bud_ivvo_fixed_2025", ENT, "2025", "14897732", "2025 vaste activa 14897731.86 was 12204362.43; tick1345; primary WVV"),
        ("bud_ivvo_mva_2025", ENT, "2025", "14874384", "2025 MVA 14874384.44 (gebouwen 12195474.55 + installaties 1976006.03 + rollend 701170.79 + CIP 1733.07); tick1345; primary WVV"),
        ("bud_ivvo_buildings_2025", ENT, "2025", "12195475", "2025 terreinen/gebouwen 12195474.55 after CIP transfer 4822869.57; tick1345; primary WVV 6.3"),
        ("bud_ivvo_plant_2025", ENT, "2025", "1976006", "2025 installaties 1976006.03; tick1345; primary WVV"),
        ("bud_ivvo_rolling_2025", ENT, "2025", "701171", "2025 meubilair/rollend 701170.79; tick1345; primary WVV"),
        ("bud_ivvo_cip_2025", ENT, "2025", "1733", "2025 CIP 1733.07 was 1696916 after 4822869.57 transfer to buildings; tick1345; primary WVV"),
        ("bud_ivvo_fva_2025", ENT, "2025", "23347", "2025 FVA 23347.42 (aandelen 20255.13 + borg 3092.29); tick1345; primary WVV"),
        ("bud_ivvo_current_2025", ENT, "2025", "9523801", "2025 vlottende activa 9523801.48 was 10255353.75; tick1345; primary WVV"),
        ("bud_ivvo_lt_recv_2025", ENT, "2025", "1500000", "2025 LT other recv 1500000.00 OVAM GFT kapitaalsubsidie booked 09.12.2024; tick1345; primary WVV + RVB"),
        ("bud_ivvo_stock_2025", ENT, "2025", "37518", "2025 voorraden 37518.37 was 54385.30; tick1345; primary WVV"),
        ("bud_ivvo_st_recv_2025", ENT, "2025", "3764224", "2025 ST recv 3764223.59 (trade 3489990.80 + other 274232.79); tick1345; primary WVV"),
        ("bud_ivvo_invest_2025", ENT, "2025", "1600000", "2025 termijnrekeningen 1600000.00 DROP vs 2700000.00 (looptijd hoogstens 1 maand); tick1345; primary WVV 6.6"),
        ("bud_ivvo_cash_2025", ENT, "2025", "2397548", "2025 cash 2397547.87 was 2133543.34; tick1345; primary WVV"),
        ("bud_ivvo_accr_asset_2025", ENT, "2025", "224512", "2025 overlopende activa 224511.65 (Fost Plus 96308.67 + asbest opleg 51645.22 + OVAM asbest 67370); tick1345; primary WVV 6.6"),
        ("bud_ivvo_equity_2025", ENT, "2025", "15633767", "2025 equity 15633766.54 was 14934536.69; tick1345; primary WVV"),
        ("bud_ivvo_inbreng_2025", ENT, "2025", "7280075", "2025 inbreng 7280075.00 (291203 aandelen x 25; beschikbaar 7031375 + onbeschikbaar 248700); tick1345; primary WVV"),
        ("bud_ivvo_reserves_2025", ENT, "2025", "5964598", "2025 reserves 5964597.96 (onbeschikbaar 359593 + beschikbaar 5605004.96); tick1345; primary WVV"),
        ("bud_ivvo_capsu_2025", ENT, "2025", "2389094", "2025 kapitaalsubsidies 2389093.58 was 2592498.35; tick1345; primary WVV"),
        ("bud_ivvo_prov_2025", ENT, "2025", "1864532", "2025 voorzieningen 1864531.68 (pensioen 777651 + herstel 1086880.68); tick1345; primary WVV"),
        ("bud_ivvo_debt_2025", ENT, "2025", "6923235", "2025 schulden 6923235.12 was 5867057.81; tick1345; primary WVV 17/49"),
        ("bud_ivvo_lt_fin_2025", ENT, "2025", "3750000", "2025 LT financial banken 3750000 (1-5j 1200000 + >5j 2550000); tick1345; primary WVV 6.9"),
        ("bud_ivvo_st_debt_2025", ENT, "2025", "3092066", "2025 ST schulden 3092066.22 was 3165704.82; tick1345; primary WVV"),
        ("bud_ivvo_st_ltcurr_2025", ENT, "2025", "300000", "2025 LT-within-year 300000; tick1345; primary WVV"),
        ("bud_ivvo_trade_pay_2025", ENT, "2025", "1690639", "2025 leveranciers 1690639.19 DROP vs 1844205.61; tick1345; primary WVV"),
        ("bud_ivvo_taxsoc_2025", ENT, "2025", "372573", "2025 tax/soc 372572.63 (tax 131670.60 + wages 240902.03); tick1345; primary WVV"),
        ("bud_ivvo_ops_rev_2025", ENT, "2025", "18152051", "2025 bedrijfsopbrengsten 18152050.70 was 20037322.39; tick1345; primary WVV"),
        ("bud_ivvo_turnover_2025", ENT, "2025", "17566199", "2025 omzet 17566198.64 was 17730009.71; tick1345; primary WVV 6.10 BT1 13114711.89 + BT2 4451486.75"),
        ("bud_ivvo_bt1_2025", ENT, "2025", "13114712", "2025 omzet bedrijfstak 1 afvalinzameling 13114711.89 was 12600174.68; tick1345; primary WVV 6.10"),
        ("bud_ivvo_bt2_2025", ENT, "2025", "4451487", "2025 omzet bedrijfstak 2 GFT 4451486.75 was 5277584.34; tick1345; primary WVV 6.10"),
        ("bud_ivvo_cityfee_cut_2025", ENT, "2025", "396130", "2025 narrative bijdragevermindering vennoten 396130 (was 431656) on tonnages+beheersvergoeding; tick1345; primary RVB not 6.10"),
        ("bud_ivvo_otherops_2025", ENT, "2025", "572062", "2025 andere bedrijfsopbrengsten 572061.56 was 2298664.18; tick1345; primary WVV code 74"),
        ("bud_ivvo_subsidy_2025", ENT, "2025", "275736", "2025 exploitatiesubsidies code 740 275735.76 was 232587.94; tick1345; primary WVV 6.10"),
        ("bud_ivvo_ops_cost_2025", ENT, "2025", "17362996", "2025 bedrijfskosten 17362996.37 was 19115455.20; tick1345; primary WVV"),
        ("bud_ivvo_goods_2025", ENT, "2025", "8516945", "2025 handelsgoederen 8516945.37; tick1345; primary WVV"),
        ("bud_ivvo_services_2025", ENT, "2025", "3243346", "2025 diensten 3243346.24 JUMP vs 2980826.28; tick1345; primary WVV"),
        ("bud_ivvo_pers_2025", ENT, "2025", "3265078", "2025 bezoldigingen 3265078.47 was 3179664.58; tick1345; primary WVV; 47 koppen / avg VTE 45 / year-end 44.69 VTE"),
        ("bud_ivvo_uitzend_2025", ENT, "2025", "34566", "2025 uitzend 34566.21 VTE 0.3; tick1345; primary WVV 6.10"),
        ("bud_ivvo_ops_2025", ENT, "2025", "789054", "2025 bedrijfswinst 789054.33 was 921867.19; tick1345; primary WVV 9901"),
        ("bud_ivvo_fin_inc_2025", ENT, "2025", "247119", "2025 fin opbr 247118.52 (vlottend 30933.44 + andere 215749.14 wv kapsu 215724.77); tick1345; primary WVV"),
        ("bud_ivvo_fin_cost_2025", ENT, "2025", "133538", "2025 fin kosten 133538.23 (schulden 129368.05); tick1345; primary WVV"),
        ("bud_ivvo_pnl_2025", ENT, "2025", "902635", "2025 PnL 902634.62 was 1039128.80; added to beschikbare reserves; tick1345; primary WVV 9904 + commissaris"),
        ("bud_ivvo_comm_fee_2025", ENT, "2025", "10263", "2025 commissaris Auditas Sven Vansteelant 10262.78; tick1345; primary WVV 6.16"),
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
                "title": "IVVO Veurne-Ommeland JR2025 leftover IGS dual (omzet 17.57m / pers 3.27m / termijn DROP 1.1m / OVAM 1.5m)",
                "entity_id": ENT,
                "beneficiary": "IVVO / vennoten Alveringem De Panne Diksmuide Heuvelland Ieper Koksijde Lo-Reninge Mesen Nieuwpoort Poperinge Veurne Vleteren / IGS IVBO IVOO IVIO IMOG IVM MIROM-Menen MIROM-Roeselare",
                "legal_basis": "Decreet lokaal bestuur IGS; opdrachthoudende vereniging; Bestuursdecreet openbaarheid; WVV neerlegging",
                "decision_date": "2026-06-16",
                "start_year": "1973",
                "end_year": "2025",
                "total_envelope_eur": "18152051",
                "cash_by_year": "",
                "remaining_eur": "15633767",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL Westhoek — per-vennoot omzet / OVAM 1.5m / NBB missing",
                "cut_option": "Publish per-vennoot 17.57m omzet + dual city lines + OVAM 1.5m vs 7.5m plan + termijn DROP 1.1m; do not recreate parallel waste-IGS shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1345; assets 24421533 omzet 17566199 pers 3265078 expl 789054 PnL 902635 VTE 44.69; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "IVVO Veurne-Ommeland JR2025 leftover IGS: omzet 17.57m / pers 3.27m / termijn DROP 1.1m / OVAM 1.5m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "3265078",
                "total_cost_eur": "18152051",
                "tco_notes": "Leftover dual IGS of mined Westhoek cities: ops rev 18.15m / omzet 17.57m / pers 3.27m VTE 44.69 / assets 24.42m / termijn DROP 1.1m / OVAM LT recv 1.5m / expl +0.79m / PnL +0.90m; do not treat 18.15m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "IVVO / 12 Westhoek gemeenten / waste-IGS",
                "stated_goal": "Local leftover IGS map VL Westhoek — JR2025 PDF live; dual omzet/OVAM/NBB FOI",
                "measured_outcome": "Official PDF 2026-08-18: assets 24.42m / omzet 17.57m / pers 3.27m / expl +789.1k / PnL +902.6k / VTE 44.69",
                "absurdity_score": "6.2",
                "cost_score": "5.8",
                "difficulty": "3.0",
                "priority_index": "6.1",
                "cut_proposal": "Publish per-vennoot 17.57m omzet + dual city lines + OVAM 1.5m vs 7.5m plan + termijn DROP 1.1m; do not recreate parallel waste-IGS shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1345; leftover IGS of mined Westhoek cities; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "Per-vennoot 2025-2026 dual lines for omzet 17566198.64 "
                    "(BT1 inzameling 13114711.89 + BT2 GFT 4451486.75) vs narrative "
                    "bijdragevermindering 396130 + counterparties/age of ST recv 3764223.59 "
                    "(trade 3489990.80) + LT recv OVAM GFT 1500000.00 vs 7.5m investment plan "
                    "/ derde reactor 2026 + destination of termijnrekeningen DROP 1100000 "
                    "(2700000 to 1600000) vs cash 2397547.87 vs CIP-to-buildings transfer "
                    "4822869.57 + diensten 3243346.24 vs pers 3265078.47 VTE 44.69 / 47 koppen "
                    "+ uitzend 34566.21 VTE 0.3 + NBB filing proof + commissarisverslag Auditas "
                    "Sven Vansteelant / AV 16.06.2026"
                ),
                "why_it_matters": (
                    "Leftover IGS shell of mined Westhoek cities Ieper/Veurne/Diksmuide/"
                    "Poperinge/Koksijde/De Panne/Nieuwpoort/Heuvelland/Alveringem/"
                    "Lo-Reninge/Mesen/Vleteren: 18.15m ops / 17.57m omzet vs 3.27m "
                    "personnel and 1.5m OVAM LT recv is a dual opacity residual, "
                    "not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "IVVO Intercommunale Vereniging voor Vuilverwijdering en -verwerking voor de Veurne en Ommeland / vennoten Alveringem De Panne Diksmuide Heuvelland Ieper Koksijde Lo-Reninge Mesen Nieuwpoort Poperinge Veurne Vleteren",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-18",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM,
                "linked_leaderboard_id": LB,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "tick1345 leftover IGS of mined Westhoek cities after honest hunt; "
                    "live JR2025 official WVV PDF now downloads (16.19MB 110p VOL-inb AV 16.06.2026). "
                    "Interleuven 2025 jaarverslag klaar but still no 2025 balans PDF — not taken. "
                    "IOK/IMOG/Haviland/IVBO/IVIO/Limburg.net still 2024. EcoWerf 2025 glossy listed / 2024 statutory still unpublished. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1345",
        "title": "IVVO Veurne-Ommeland JR2025 leftover IGS dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: IVVO leftover IGS of mined Westhoek cities after honest hunt; "
            "KBO 0213.877.575 Actief; live JR2025 official WVV PDF (16.19MB 110p VOL-inb AV 16.06.2026); "
            "sourced euros assets 24.422m / omzet 17.566m / pers 3.265m / expl 789.054 / PnL 902.635 / VTE 44.69; "
            "FOI ready omzet/termijn/OVAM/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T06:15:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1345 IVVO leftover IGS residual; KBO 0213.877.575; live JR2025 WVV PDF; "
            "sourced euros; FOI ready not sent; next rq_1346 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1346",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1345 done including IVVO Veurne-Ommeland 1345 leftover IGS live WVV / "
            "ILvA Land van Aalst 1344 leftover IGS live WVV / "
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
            "EcoWerf 2025 jaarverslag listed ~16MB / 2024 statutory still unpublished — take only if a WVV/BBC PDF now downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland / IVBO / IVIO / Limburg.net still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
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
        "notes": "spawned tick1345 after IVVO leftover IGS live WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1345", rq_new, rq_spawn)
    print("research_queue 1345", found, "spawned_1346", spawned)

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
                "last_unit_id": "rq_1345",
                "ticks_completed": "1345",
                "paused": "no",
                "notes": (
                    "tick1345 IVVO leftover IGS residual; KBO 0213.877.575; "
                    "live JR2025 WVV PDF; sourced euros assets 24.422m omzet 17.566m pers 3.265m expl 789.054 PnL 902.635; "
                    "FOI ready; next rq_1346 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log_entry = """
### Tick 1345 - 2026-08-18 - rq_1345 IVVO Veurne-Ommeland dual residual leftover IGS
- Unit: IVVO Intercommunale Vereniging voor Vuilverwijdering en -verwerking voor de Veurne en Ommeland (leftover IGS) of already-mined Westhoek / Ieper-Veurne-Kust cities (Ieper / Veurne / Diksmuide / Poperinge / Koksijde / De Panne / Nieuwpoort / Heuvelland / Alveringem / Lo-Reninge / Mesen / Vleteren) after residual dual hunt (KBO **0213.877.575**; official ivvo.be + live jaarverslag 2025 PDF 16.19MB / 110p; AV **16.06.2026**; WVV VOL-inb embedded p55-96). Prefer live PDF over another unpublished FOI. Distinct from already-mined ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340. KBO Actief / normale toestand since **14.12.1973**; statutaire naam Intercommunale Vereniging voor Vuilverwijdering en -verwerking voor de Veurne en Ommeland since 14.12.1973; afkorting I.V.V.O. since 14.12.1973; Opdrachthoudende vereniging (Vlaams Gewest) since 25.05.1993; zetel Bargiestraat 6 8900 Ieper since 17.06.2014; **6 VE**; RSZ-werkgever since 01.01.2022; btw since 01.04.1988; aanbestedende overheid since 14.12.1973; kapitaal KBO 250.000; jaarvergadering mei; boekjaar 31 december; voorzitter Bart Vanacker; ondervoorzitters Elise Sticker / Jeroen Thieren; FD Jan Masselin; commissaris Auditas / Sven Vansteelant since AV 20.06.2023; e-mail info@ivvo.be on official PDF; tel 057 23 08 80; NACE 38.330. Hunt leftover AGB/zorg/EVA first: Interleuven 2025 jaarverslag "klaar" + AV 17.06.2026, publications page still only jaarrekening 2024 PDF — not taken; IOK/IMOG/Haviland still 2024; EcoWerf now lists jaarverslag 2025 (~16MB) but 2024 statutory jaarrekening still "wordt weldra gepubliceerd" — not taken once live IVVO WVV downloaded; IVBO/IVIO/Limburg.net still 2024; IVAREM jaarverslag still 2024; Veneco glossy 25MB InDesign — not mined as BBC; Dommelhof leftover Limburg EVA KBO 0777.495.085 not taken once live IVVO PDF downloaded. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek not taken once live IVVO PDF downloaded. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331. Not every-10 (next 1350).
- EUR strong (primary WVV VOL-inb in official PDF; commissaris confirms assets 24.421.533,34 / PnL 902.634,62): assets **24.421.533** (was 22.459.716); fixed **14.897.732**; MVA **14.874.384** (gebouwen **12.195.475** + installaties **1.976.006** + rollend **701.171** + CIP **1.733** after 4.822.870 transfer); FVA **23.347**; current **9.523.801**; LT recv **1.500.000** (OVAM GFT); voorraden **37.518**; ST recv **3.764.224** (trade **3.489.991**); termijn **1.600.000** DROP vs 2.700.000; cash **2.397.548**; equity **15.633.767**; inbreng **7.280.075**; reserves **5.964.598** (beschikbaar **5.605.005**); kapitaalsubsidies **2.389.094**; voorzieningen **1.864.532** (pensioen **777.651** + herstel **1.086.881**); schulden **6.923.235**; LT fin **3.750.000**; ST **3.092.066** (LT-within-year **300.000** + trade **1.690.639** + tax/soc **372.573**); ops rev **18.152.051**; omzet **17.566.199** (BT1 **13.114.712** + BT2 **4.451.487**); andere **572.062** (subsidies 740 **275.736**); pers **3.265.078**; 47 koppen / VTE **44,69** / avg **45**; uitzend **34.566** VTE 0,3; diensten **3.243.346**; expl **789.054**; fin opbr **247.119**; fin kosten **133.538**; PnL **902.635**. Narrative bijdragevermindering **396.130**. Commissaris Auditas **10.263**. Oordeel zonder voorbehoud.
- CSVs: sources+4/entities+1/budgets+43/commitments+1/leaderboard+1 + FOI ready `gap_ivvo_omzet_17_57m_pers_3_27m_termijn_1_1m_l5` (not sent); rq_1345=done; spawn rq_1346; ticks=1345.
- Coverage: residual dual L5 (IVVO leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1346 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland/IVBO/IVIO/Limburg.net only if a 2025 JR PDF now downloads; EcoWerf only if a statutory WVV/BBC PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 unless a fetchable JR appears).
"""
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1345 write done")


if __name__ == "__main__":
    main()

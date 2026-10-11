# -*- coding: utf-8 -*-
"""Tick 1349 — leftover IGS Aquaduin / IWVA ov JR2025 official WVV euros.
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

TICK = "1349"
UTC = "2026-08-18T21:55:00Z"
ENT = "igs_aquaduin"
HIER = "Vlaanderen>WestVlaanderen>IGS>Aquaduin>IWVA"
GAP = "gap_aqd_omzet_26_50m_accrual_31_68m_l5"
SRC = "src_aqd_jr2025_pdf"
SRC2 = "src_aqd_site"
SRC3 = "src_kbo_aqd_0205264668"
SRC4 = "src_aqd_foi_contact"
SRC_URL = "https://www.aquaduin.be/volumes/general/Paginas/Over-ons/Publicaties/Jaarverslagen/Aquaduin-Jaarverslag-2025.pdf?v=1785911536"
SRC2_URL = "https://www.aquaduin.be/bedrijfsinfo/jaarverslagen"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0205264668"
SRC4_URL = "https://www.aquaduin.be/contact"
FOI_EMAIL = "info@aquaduin.be"
FOI_POSTAL = "Doornpannestraat 1 8670 Koksijde"
DRAFT = "docs/doge/foi/drafts/gap_aqd_omzet_26_50m_accrual_31_68m_l5.md"
COMM = "comm_aqd_jr2025_omzet"
LB = "lb_aqd_omzet_26_50m_accrual_31_68m"


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
                "title": "Aquaduin / IWVA ov jaarverslag boekjaar 2025 (official WVV balans; InDesign 10.06.2026; AV 21.05.2026)",
                "url": SRC_URL,
                "publisher": "Aquaduin / IWVA ov opdrachthoudende vereniging",
                "accessed_date": "2026-08-18",
                "source_class": "budget",
                "notes": (
                    "tick1349; official PDF 9.77MB 64p InDesign 10.06.2026; leftover IGS water of mined Westhoek cities; "
                    "embedded WVV balans/resultatenrekening; RvB 04.03.2026 AV 21.05.2026; commissaris VRC / Vander Donckt"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Aquaduin official jaarverslagen page (IWVA ov KBO 0205.264.668)",
                "url": SRC2_URL,
                "publisher": "Aquaduin / IWVA ov",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1349; leftover IGS water of mined Westhoek / IVVO 1345 waste IGS same cities; "
                    "handelsnaam Aquaduin; statutaire naam IWVA"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Aquaduin / IWVA 0205.264.668",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1349; KBO 0205.264.668 Actief / normale toestand since 24.12.1924; "
                    "statutaire naam Intercommunale Waterleidingsmaatschappij van Veurne Ambacht since 24.12.1924; "
                    "Opdrachthoudende vereniging (Vlaams Gewest) since 23.05.2003; zetel Doornpannestraat 1 8670 Koksijde since 20.06.1991; "
                    "2 VE; aanbestedende overheid since 24.12.1924; btw since 01.10.1977; RSZ since 01.01.2022; "
                    "jaarvergadering mei; boekjaar 31 december; NACE 36.000"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Aquaduin / IWVA FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "Aquaduin / IWVA ov",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1349; FOI info@aquaduin.be; Doornpannestraat 1 8670 Koksijde; "
                    "T 058 53 38 33; voorzitter Wim Janssens; AD Johan Verbauwhede"
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
                "name_nl": "Aquaduin / IWVA ov (leftover IGS water Veurne-Ambacht)",
                "name_fr": "Aquaduin / IWVA ov (association chargee de mission / eau / IGS residuel)",
                "name_en": "Aquaduin / IWVA ov Westhoek water intermunicipal (leftover IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.aquaduin.be",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1349 leftover IGS residual water of mined Westhoek cities (Koksijde/De Panne/Nieuwpoort/Veurne/Alveringem/Diksmuide); "
                    "KBO 0205.264.668 Actief since 24.12.1924; official JR2025 WVV PDF downloads; "
                    "sourced euros omzet 26.499m / assets 99.094m / sanering accrual 31.332m / PnL 2.597m; "
                    "FOI ready per-vennoot/sanering/kapsu/NBB"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_aqd_assets_2025", ENT, "2025", "99094393", "2025 assets 99094393.07; tick1349; primary official WVV"),
        ("bud_aqd_assets_2024", ENT, "2024", "89349170", "2024 assets 89349170.31 comparative; tick1349; primary official WVV"),
        ("bud_aqd_fixed_2025", ENT, "2025", "74706710", "2025 vaste activa 74706709.82; tick1349; primary official WVV"),
        ("bud_aqd_mva_2025", ENT, "2025", "74513245", "2025 MVA 74513244.58; tick1349; primary official WVV"),
        ("bud_aqd_current_2025", ENT, "2025", "24387683", "2025 vlottende activa 24387683.25; tick1349; primary official WVV"),
        ("bud_aqd_ltrecv_2025", ENT, "2025", "4205000", "2025 LT recv 4205000 new vs 0; tick1349; primary official WVV"),
        ("bud_aqd_stock_2025", ENT, "2025", "1316792", "2025 voorraden 1316792.15; tick1349; primary official WVV"),
        ("bud_aqd_strecv_2025", ENT, "2025", "5100085", "2025 ST recv 5100085.22; tick1349; primary official WVV"),
        ("bud_aqd_trade_recv_2025", ENT, "2025", "5036714", "2025 handelsvorderingen 5036714.04; tick1349; primary official WVV"),
        ("bud_aqd_invest_2025", ENT, "2025", "13415919", "2025 geldbeleggingen 13415919.13; tick1349; primary official WVV"),
        ("bud_aqd_cash_2025", ENT, "2025", "164458", "2025 liquide middelen 164457.68; tick1349; primary official WVV"),
        ("bud_aqd_equity_2025", ENT, "2025", "52908396", "2025 equity 52908395.62; tick1349; primary official WVV"),
        ("bud_aqd_capital_2025", ENT, "2025", "2049750", "2025 geplaatst kapitaal 2049750 / 8199 aandelen; tick1349; primary official WVV"),
        ("bud_aqd_reserves_2025", ENT, "2025", "24018601", "2025 reserves 24018601.46; tick1349; primary official WVV"),
        ("bud_aqd_kapsu_2025", ENT, "2025", "26819983", "2025 kapitaalsubsidies 26819982.98 was 23199955.02; tick1349; primary official WVV"),
        ("bud_aqd_prov_2025", ENT, "2025", "4335477", "2025 voorzieningen 4335476.73; tick1349; primary official WVV"),
        ("bud_aqd_debt_2025", ENT, "2025", "41850521", "2025 schulden 41850520.72; tick1349; primary official WVV"),
        ("bud_aqd_ltdebt_2025", ENT, "2025", "3255235", "2025 LT fin achtergesteld 3255235.02; tick1349; primary official WVV"),
        ("bud_aqd_stdebt_2025", ENT, "2025", "6911672", "2025 ST schulden 6911672.27; tick1349; primary official WVV"),
        ("bud_aqd_trade_pay_2025", ENT, "2025", "4603876", "2025 leveranciers 4603876.06; tick1349; primary official WVV"),
        ("bud_aqd_accrual_2025", ENT, "2025", "31683613", "2025 overlopend 31683613.43; tick1349; primary official WVV"),
        ("bud_aqd_sanering_2025", ENT, "2025", "31332405", "2025 aanrekeningen gemeentelijke sanering 31332405.27; tick1349; primary official WVV toel"),
        ("bud_aqd_opsrev_2025", ENT, "2025", "30697805", "2025 bedrijfsopbrengsten 30697804.89; tick1349; primary official WVV"),
        ("bud_aqd_omzet_2025", ENT, "2025", "26499270", "2025 omzet 26499269.80 JUMP vs 22910441.64; tick1349; primary official WVV"),
        ("bud_aqd_omzet_2024", ENT, "2024", "22910442", "2024 omzet 22910441.64 comparative; tick1349; primary official WVV"),
        ("bud_aqd_otherops_2025", ENT, "2025", "3436323", "2025 andere bedrijfsopbrengsten 3436322.83; tick1349; primary official WVV"),
        ("bud_aqd_ops_cost_2025", ENT, "2025", "28823323", "2025 bedrijfskosten 28823323.44; tick1349; primary official WVV"),
        ("bud_aqd_goods_2025", ENT, "2025", "15281985", "2025 handelsgoederen 15281985.26; tick1349; primary official WVV"),
        ("bud_aqd_diensten_2025", ENT, "2025", "4903752", "2025 diensten 4903752.08; tick1349; primary official WVV"),
        ("bud_aqd_pers_2025", ENT, "2025", "4987994", "2025 personeel 4987994.28; 45 koppen / 43.12 VTE; tick1349; primary official WVV"),
        ("bud_aqd_depr_2025", ENT, "2025", "3030680", "2025 afschrijvingen 3030679.61; tick1349; primary official WVV"),
        ("bud_aqd_expl_2025", ENT, "2025", "1874481", "2025 bedrijfswinst 1874481.45 commentaar = 30697804.89-28823323.44; tick1349; primary official WVV"),
        ("bud_aqd_fin_opbr_2025", ENT, "2025", "782382", "2025 financiele opbrengsten 782381.67; tick1349; primary official WVV"),
        ("bud_aqd_fin_cost_2025", ENT, "2025", "59757", "2025 financiele kosten 59757.42; tick1349; primary official WVV"),
        ("bud_aqd_pnl_2025", ENT, "2025", "2597106", "2025 PnL 2597105.70 all to reserves; tick1349; primary official WVV"),
        ("bud_aqd_capex_2025", ENT, "2025", "7599263", "2025 geinvesteerd in vast actief 7599263.41 commentaar; tick1349; primary official WVV"),
        ("bud_aqd_kapsu_recv_2025", ENT, "2025", "4095522", "2025 ontvangen kapitaalsubsidies 4095522.43 commentaar; tick1349; primary official WVV"),
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
                "title": "Aquaduin / IWVA ov JR2025 leftover IGS dual (omzet 26.50m / sanering accrual 31.33m / kapsu 26.82m)",
                "entity_id": ENT,
                "beneficiary": "Aquaduin / IWVA ov / 6 Westhoek vennoten (Koksijde De Panne Nieuwpoort Veurne Alveringem Diksmuide)",
                "legal_basis": "Decreet lokaal bestuur IGS; opdrachthoudende vereniging; Bestuursdecreet openbaarheid; WVV neerlegging",
                "decision_date": "2026-05-21",
                "start_year": "1924",
                "end_year": "2025",
                "total_envelope_eur": "26499270",
                "cash_by_year": "",
                "remaining_eur": "31683613",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL water — per-vennoot 26.50m omzet / sanering 31.33m / kapsu 26.82m",
                "cut_option": "Publish per-vennoot 26.50m omzet dual city lines + sanering accrual 31.33m + kapsu 26.82m + NBB; do not recreate parallel Westhoek water-IGS shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1349; omzet 26499270 assets 99094393 sanering 31332405 kapsu 26819983 PnL 2597106; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Aquaduin / IWVA ov JR2025 leftover IGS: omzet 26.50m / sanering accrual 31.33m / kapsu 26.82m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "26499270",
                "total_cost_eur": "26499270",
                "tco_notes": "Leftover dual IGS water of mined Westhoek cities: omzet 26.50m / sanering accrual 31.33m of 31.68m overlopend / kapsu 26.82m / assets 99.09m; official WVV live; do not treat 26.50m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Aquaduin / IWVA ov / 6 Westhoek vennoten",
                "stated_goal": "Local leftover IGS map VL water — JR2025 WVV live; dual omzet/sanering/NBB FOI",
                "measured_outcome": "Official WVV 2026-08-18: omzet 26.50m / assets 99.09m / sanering accrual 31.33m / kapsu 26.82m / PnL 2.60m; pers 45 / 43.12 VTE",
                "absurdity_score": "5.8",
                "cost_score": "6.4",
                "difficulty": "3.0",
                "priority_index": "5.9",
                "cut_proposal": "Publish per-vennoot 26.50m omzet dual city lines + sanering 31.33m + kapsu 26.82m + NBB; do not recreate parallel Westhoek water-IGS shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1349; leftover IGS water of mined Westhoek cities; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "Per-vennoot 2025-2026 dual lines for omzet 26499269.80 (JUMP vs 22910441.64; drinkwater + sanering; "
                    "no 6.10 split) + composition of overlopend 31683613.43 of which gemeentelijke sanering 31332405.27 "
                    "+ bovengemeentelijke 51989.74 + milieuheffing 254327.25 + new LT recv 4205000 (was 0) + "
                    "kapitaalsubsidies 26819982.98 vs received 4095522.43 + off-balance capex Groenendijk 1680465.34 / "
                    "De Panne 3844197.95 / Veurne 3197395.10 / Nieuwpoort 382353.19 / Alveringem 29228.79 / Westhoek 1876558.75 "
                    "+ commissaris ereloon VRC/Vander Donckt + AV 21.05.2026 minutes + NBB filing"
                ),
                "why_it_matters": (
                    "Leftover IGS water shell of mined Westhoek cities (Koksijde/De Panne/Nieuwpoort/Veurne/Alveringem/Diksmuide; "
                    "IVVO waste IGS same region tick1345; Pidpa/DWG/Farys ov already mined): 26.50m omzet vs 31.33m "
                    "sanering accrual / 26.82m kapitaalsubsidies is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Aquaduin / IWVA ov / 6 Westhoek vennoten",
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
                    "tick1349 leftover IGS water of mined Westhoek cities after honest hunt; "
                    "live JR2025 official WVV PDF now downloads (9.77MB 64p InDesign 10.06.2026). "
                    "Interwaas 2025 PDF 19.3MB 65p downloaded this tick (has WVV codes) leftover for next. "
                    "EcoWerf 2025 glossy / 2024 statutory still unpublished. Interleuven still 2024 balans. "
                    "IOK/IMOG/Haviland/IVBO/Limburg.net still 2024. Veneco/Leiedal glossy-only. MIROM 403. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1349",
        "title": "Aquaduin IWVA ov JR2025 leftover IGS dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Aquaduin / IWVA ov leftover IGS water of mined Westhoek cities after honest hunt; "
            "KBO 0205.264.668 Actief; live JR2025 official WVV PDF (9.77MB 64p InDesign 10.06.2026 AV 21.05.2026); "
            "sourced euros omzet 26.499m / assets 99.094m / sanering accrual 31.332m / kapsu 26.820m / PnL 2.597m; "
            "FOI ready per-vennoot/sanering/kapsu/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T21:50:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1349 Aquaduin leftover IGS residual; KBO 0205.264.668; live JR2025 WVV PDF; "
            "sourced euros; FOI ready not sent; next rq_1350 residual dual L5 VL + every-10"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1350",
        "title": "Continuous FOI-adjacent public hole-fill batch + every-10 progress",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill + every-10 progress (ticks_completed will be 1350); "
            "next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1349 done including Aquaduin / IWVA ov 1349 leftover IGS live WVV / "
            "Creat Services dv 1348 leftover IGS live WVV / "
            "IVIO Izegem-Ommeland 1347 leftover IGS live JR operational / "
            "WVI West-Vlaanderen 1346 leftover IGS live WVV / "
            "IVVO Veurne-Ommeland 1345 leftover IGS live WVV / "
            "ILvA Land van Aalst 1344 leftover IGS live WVV / "
            "IVM Meetjesland 1343 leftover IGS live WVV / "
            "IDM Durme-Moervaart 1342 leftover IGS live WVV / "
            "IGEAN dienstverlening 1341 leftover IGS live WVV / "
            "EVA Limburg Sterk Merk 1340 leftover EVA live WVV + every-10); "
            "Interwaas 2025 PDF 19.3MB 65p InDesign 21.05.2026 downloaded tick1349 — HAS jaarrekening WVV codes — take if still unmined; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "AGB Bornem / AGB De Kluize already FOI — skip unless a PDF now downloads; "
            "Welzijnskoepel West-Brabant jaarverslag 2025 glossy-only — take only if a BBC PDF now downloads; "
            "Ter Nethe official still unpublished/DNS — take only if a PDF now downloads; "
            "Veneco glossy jaarverslag 2025 websingle — take only if a WVV/BBC PDF now downloads; "
            "EcoWerf 2025 jaarverslag listed ~16MB glossy / 2024 statutory still unpublished — take only if a WVV/BBC PDF now downloads; "
            "Leiedal 2025 InDesign 22MB 118p downloaded tick1347 — glossy-only no WVV — take only if a WVV/BBC PDF now downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland / IVBO / Limburg.net still 2024 — take only if a 2025 JR PDF now downloads; "
            "IVOO no public 2025 JR PDF — take only if a 2025 JR PDF now downloads; "
            "MIROM 403 — take only if a 2025 JR PDF now downloads; "
            "INCOVO still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
            "WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / "
            "WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403; IS every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1349 after Aquaduin leftover IGS live WVV; next residual dual L5 VL + every-10",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1349", rq_new, rq_spawn)
    print("research_queue 1349", found, "spawned_1350", spawned)

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
                "last_unit_id": "rq_1349",
                "ticks_completed": "1349",
                "paused": "no",
                "notes": (
                    "tick1349 Aquaduin leftover IGS residual; KBO 0205.264.668; "
                    "live JR2025 WVV PDF; sourced euros omzet 26.499m assets 99.094m sanering 31.332m kapsu 26.820m PnL 2.597m; "
                    "FOI ready per-vennoot/sanering; next rq_1350 residual dual L5 VL + every-10; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log_entry = """
### Tick 1349 - 2026-08-18 - rq_1349 Aquaduin / IWVA ov dual residual leftover IGS
- Unit: Aquaduin / IWVA ov (opdrachthoudende vereniging / leftover IGS water; statutaire naam Intercommunale Waterleidingsmaatschappij van Veurne Ambacht) of already-mined Westhoek cities (Koksijde / De Panne / Nieuwpoort / Veurne / Alveringem / Diksmuide) after residual dual hunt (KBO **0205.264.668**; official aquaduin.be + live jaarverslag 2025 PDF 9.77MB / 64p; InDesign **10.06.2026**; RvB **04.03.2026**; AV **21.05.2026**; embedded WVV balans). Prefer live PDF over another unpublished FOI. Distinct from already-mined Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 (waste IGS same Westhoek) / ILvA 1344. Pidpa / DWG / Farys ov already mined. KBO Actief / normale toestand since **24.12.1924**; Opdrachthoudende vereniging (Vlaams Gewest) since 23.05.2003; zetel Doornpannestraat 1 8670 Koksijde since 20.06.1991; **2 VE**; aanbestedende overheid since 24.12.1924; btw since 01.10.1977; RSZ since 01.01.2022; jaarvergadering mei; boekjaar 31 december; voorzitter Wim Janssens (De Panne) since 11.12.2025; ondervoorzitter Ben Peperstraete; AD Johan Verbauwhede; commissaris VRC Bedrijfsrevisoren / Frederik Vander Donckt; e-mail info@aquaduin.be; tel 058 53 38 33; NACE 36.000. 6 vennoten / 8.199 aandelen (Koksijde 2.916 / Veurne 1.661 / De Panne 1.617 / Nieuwpoort 1.488 / Alveringem 332 / Diksmuide 185). Hunt leftover AGB/zorg/EVA first: Interwaas 2025 PDF 19.3MB / 65p InDesign 21.05.2026 downloaded this tick (has jaarrekening WVV codes) — leftover for next; EcoWerf 2025 glossy / 2024 statutory still unpublished; Interleuven still 2024 balans; IOK/IMOG/Haviland/IVBO/Limburg.net still 2024; IVOO no public 2025 JR; MIWA still 2024; MIROM 403; Veneco/Leiedal glossy-only; IVAGO activiteitenverslag; ISVAG 2023; IVAREM 2024; SOLVA/IGEMO no 2025 JR; INCOVO still 2024; Pidpa/DWG/Farys ov already mined. Dommelhof leftover Limburg EVA KBO 0777.495.085 not taken once live Aquaduin WVV downloaded. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek not taken once live Aquaduin PDF downloaded. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339. Not every-10 (next 1350).
- EUR strong (primary official WVV): assets **99.094.393** (was 89.349.170); fixed **74.706.710**; MVA **74.513.245**; current **24.387.683**; LT recv **4.205.000** (new vs 0); voorraden **1.316.792**; ST recv **5.100.085** (trade **5.036.714**); beleggingen **13.415.919**; cash **164.458**; equity **52.908.396** (kapitaal **2.049.750**; reserves **24.018.601**; kapitaalsubsidies **26.819.983**); voorzieningen **4.335.477**; schulden **41.850.521** (LT achtergesteld **3.255.235** + ST **6.911.672** trade **4.603.876** + overlopend **31.683.613** waarvan gemeentelijke sanering **31.332.405**); ops rev **30.697.805**; omzet **26.499.270** JUMP vs 22.910.442; andere bedrijfsopbrengsten **3.436.323**; ops cost **28.823.323** (goederen **15.281.985** + diensten **4.903.752** + pers **4.987.994** + afschr **3.030.680**); expl **+1.874.481**; fin opbr **782.382**; fin kosten **59.757**; PnL **+2.597.106** (all to reserves). Pers **45** / 43,12 VTE. Off-balance capex Groenendijk 1.680.465 + De Panne 3.844.198 + Veurne 3.197.395 + Nieuwpoort 382.353 + Alveringem 29.229 + Westhoek 1.876.559. Investeringen **7.599.263**; ontvangen kapsu **4.095.522**. Bestuurders **22.717**; commissaris **11.200** + 3.200.
- CSVs: sources+4/entities+1/budgets+37/commitments+1/leaderboard+1 + FOI ready `gap_aqd_omzet_26_50m_accrual_31_68m_l5` (not sent); rq_1349=done; spawn rq_1350; ticks=1349.
- Coverage: residual dual L5 (Aquaduin leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1350 residual dual L5 VL JR2025 hole_fill + every-10 (prefer Interwaas 2025 PDF already downloaded tick1349 if still unmined and WVV tables extract; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland/IVBO/Limburg.net only if a 2025 JR PDF now downloads; EcoWerf only if a statutory WVV/BBC PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; MIROM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 unless a fetchable JR appears).
"""
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1349 write done")


if __name__ == "__main__":
    main()

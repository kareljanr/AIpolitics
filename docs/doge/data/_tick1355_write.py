# -*- coding: utf-8 -*-
"""Tick 1355 — leftover NUHMA AC NV JR2025 official NBB WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10 (next every-10 is 1360).
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1355"
UTC = "2026-08-19T01:25:00Z"
ENT = "nv_nuhma"
HIER = "Vlaanderen>Limburg>NV>NUHMA_AC>KlimaatHolding"
GAP = "gap_nuhma_pnl_8_77m_div_8_33m_fva_drop_l5"
SRC = "src_nuhma_jr2025_nbb"
SRC2 = "src_nuhma_site"
SRC3 = "src_kbo_nuhma_0697972507"
SRC4 = "src_nuhma_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00124430.pdf"
SRC2_URL = "https://nuhma.be/duurzaam-rendement-in-2025/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0697972507"
SRC4_URL = "https://nuhma.be/contact/"
FOI_EMAIL = "info@nuhma.be"
FOI_POSTAL = "Herkenrodesingel 14 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_nuhma_pnl_8_77m_div_8_33m_fva_drop_l5.md"
COMM = "comm_nuhma_jr2025_pnl"
LB = "lb_nuhma_pnl_8_77m_div_8_33m_fva_drop"


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
                "title": "NUHMA AC NV jaarrekening boekjaar 2025 (official NBB WVV VOL-kap deposit 2026-00124430; AV 26.05.2026)",
                "url": SRC_URL,
                "publisher": "NUHMA AC NV / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1355; official NBB VOL-kap PDF 484kB 47p deposit 2026-00124430 neerlegging 27.05.2026; "
                    "leftover klimaat-holding NV of mined Limburg cities + Bionerga 1354 / Limburg.net 1353; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Nuhma official site 2025 kerncijfers (Nuhma cv microsite; no statutory AC PDF)",
                "url": SRC2_URL,
                "publisher": "Nuhma cv",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1355; leftover NV of mined Limburg + Bionerga/Limburg.net; "
                    "nuhma.be is Nuhma cv KBO 0472.325.068; narrative EV 662.8m / winst 26.3m; "
                    "jaarverslag page still 2020 PDF only; narrative euros NOT used as AC statutory"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO NUHMA AC 0697.972.507",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1355; KBO 0697.972.507 Actief / normale toestand since 15.06.2018; "
                    "statutaire naam NUHMA AC since 15.06.2018; NV since 15.06.2018; "
                    "zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; 1 VE; "
                    "btw since 01.10.2018; KBO kapitaal 470197930; jaarvergadering mei; "
                    "12 functiehouders; gedelegeerd bestuurder Nuhma cv 0472.325.068; NACE 64.210"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Nuhma FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "Nuhma cv",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1355; FOI info@nuhma.be; 011 49 56 10; Herkenrodesingel 14 3500 Hasselt "
                    "(same zetel as Bionerga / Limburg.net); commissaris Moore Audit / Jimmy Depré"
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
                "name_nl": "NUHMA AC NV (leftover klimaat-holding Limburg / Bionerga / Limburg.net)",
                "name_fr": "NUHMA AC SA (holding climat residuel Limbourg / Bionerga / Limburg.net)",
                "name_en": "NUHMA AC NV leftover Limburg climate holding (Bionerga/Limburg.net dual)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://nuhma.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1355 leftover residual klimaat-holding NV of mined Limburg cities + Bionerga 1354 "
                    "+ Limburg.net 1353 (same zetel Herkenrodesingel 14; Nuhma cv 0472.325.068 is gedelegeerd bestuurder); "
                    "KBO 0697.972.507 Actief since 15.06.2018; official NBB WVV VOL-kap PDF downloads; "
                    "sourced euros assets 630.631m / equity 607.097m / pnl 8.773m / div 8.325m / fva drop 37.121m; "
                    "FOI ready per-shareholder/impairment/cv-recon/Bionerga dual"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_nuhma_assets_2025", ENT, "2025", "630630603", "2025 assets 630630603 VOL-kap 20/58; tick1355; primary official NBB WVV"),
        ("bud_nuhma_assets_2024", ENT, "2024", "679344341", "2024 assets 679344341 comparative; tick1355; primary official NBB WVV 20/58"),
        ("bud_nuhma_pnl_2025", ENT, "2025", "8772737", "2025 PnL 9904 8772737; tick1355; primary official NBB WVV + commissaris Moore"),
        ("bud_nuhma_pnl_2024", ENT, "2024", "22963457", "2024 PnL 9904 22963457 comparative; tick1355; primary official NBB WVV"),
        ("bud_nuhma_fixed_2025", ENT, "2025", "617947424", "2025 vaste activa 617947424 all FVA; tick1355; primary official NBB WVV 21/28"),
        ("bud_nuhma_current_2025", ENT, "2025", "12666460", "2025 vlottende activa 12666460 DROP vs 24254768; tick1355; primary official NBB WVV 29/58"),
        ("bud_nuhma_equity_2025", ENT, "2025", "607097228", "2025 eigen vermogen 607097228 DROP vs 657461926; tick1355; primary official NBB WVV 10/15"),
        ("bud_nuhma_equity_2024", ENT, "2024", "657461926", "2024 eigen vermogen 657461926 comparative; tick1355; primary official NBB WVV 10/15"),
        ("bud_nuhma_kapitaal_2025", ENT, "2025", "470197930", "2025 geplaatst kapitaal 470197930; tick1355; primary official NBB WVV 100"),
        ("bud_nuhma_herw_2025", ENT, "2025", "131972345", "2025 herwaardering 131972345 DROP vs 182784780; tick1355; primary official NBB WVV 12"),
        ("bud_nuhma_herw_2024", ENT, "2024", "182784780", "2024 herwaardering 182784780 comparative; tick1355; primary official NBB WVV 12"),
        ("bud_nuhma_reserves_2025", ENT, "2025", "4926953", "2025 reserves 4926953 (wettelijk 4755405 + beschikbaar 171548); tick1355; primary official NBB WVV 13"),
        ("bud_nuhma_setup_2025", ENT, "2025", "16719", "2025 oprichtingskosten 16719; tick1355; primary official NBB WVV 20"),
        ("bud_nuhma_fva_2025", ENT, "2025", "617947424", "2025 FVA 617947424 DROP vs 655068418; tick1355; primary official NBB WVV 28"),
        ("bud_nuhma_fva_2024", ENT, "2024", "655068418", "2024 FVA 655068418 comparative; tick1355; primary official NBB WVV 28"),
        ("bud_nuhma_fva_verb_2025", ENT, "2025", "164104968", "2025 FVA verbonden 164104968 (deeln 156529351 + vord 7575616); tick1355; primary official NBB WVV 280/1"),
        ("bud_nuhma_fva_deel_2025", ENT, "2025", "447544171", "2025 FVA deelnemingsverhouding 447544171 (deeln 435950902 + vord 11593269); tick1355; primary official NBB WVV 282/3"),
        ("bud_nuhma_fva_other_2025", ENT, "2025", "6298286", "2025 andere FVA 6298286 (aandelen 5189381 + vord 1108904); tick1355; primary official NBB WVV 284/8"),
        ("bud_nuhma_strecv_2025", ENT, "2025", "9445622", "2025 ST vorderingen 9445622 all overige; tick1355; primary official NBB WVV 40/41"),
        ("bud_nuhma_invest_2025", ENT, "2025", "128800", "2025 geldbeleggingen 128800 DROP vs 7528800; tick1355; primary official NBB WVV 50/53"),
        ("bud_nuhma_invest_2024", ENT, "2024", "7528800", "2024 geldbeleggingen 7528800 comparative; tick1355; primary official NBB WVV 50/53"),
        ("bud_nuhma_cash_2025", ENT, "2025", "3089512", "2025 liquide middelen 3089512 DROP vs 6823778; tick1355; primary official NBB WVV 54/58"),
        ("bud_nuhma_cash_2024", ENT, "2024", "6823778", "2024 liquide middelen 6823778 comparative; tick1355; primary official NBB WVV 54/58"),
        ("bud_nuhma_debt_2025", ENT, "2025", "23533375", "2025 schulden 23533375; tick1355; primary official NBB WVV 17/49"),
        ("bud_nuhma_lt_2025", ENT, "2025", "15169577", "2025 LT schulden 15169577 all overige leningen; tick1355; primary official NBB WVV 17"),
        ("bud_nuhma_st_2025", ENT, "2025", "8360620", "2025 ST schulden 8360620 (trade 1152 + tax 34468 + other/div 8325000); tick1355; primary official NBB WVV 42/48"),
        ("bud_nuhma_div_2025", ENT, "2025", "8325000", "2025 uit te keren winst/dividend 8325000 DROP vs 21800000; tick1355; primary official NBB WVV 694"),
        ("bud_nuhma_div_2024", ENT, "2024", "21800000", "2024 dividend 21800000 comparative; tick1355; primary official NBB WVV 694"),
        ("bud_nuhma_opscost_2025", ENT, "2025", "163323", "2025 bedrijfskosten 163323; tick1355; primary official NBB WVV 60/66A"),
        ("bud_nuhma_diensten_2025", ENT, "2025", "156845", "2025 diensten 156845; tick1355; primary official NBB WVV 61"),
        ("bud_nuhma_expl_2025", ENT, "2025", "-163323", "2025 bedrijfsverlies -163323; tick1355; primary official NBB WVV 9901"),
        ("bud_nuhma_fininc_2025", ENT, "2025", "28584984", "2025 financiele opbrengsten 28584984 (rec 28551701 FVA 27407926 + vlottend 1143775; nr 33283); tick1355; primary official NBB WVV 75/76B"),
        ("bud_nuhma_fincost_2025", ENT, "2025", "19410816", "2025 financiele kosten 19410816 (rec 349144 + nr 19061672); tick1355; primary official NBB WVV 65/66B"),
        ("bud_nuhma_nrfin_2025", ENT, "2025", "19061672", "2025 niet-recurrente fin kosten 19061672 WVV 66B; tick1355; primary official NBB WVV"),
        ("bud_nuhma_tax_2025", ENT, "2025", "238108", "2025 belastingen 238108; tick1355; primary official NBB WVV 67/77"),
        ("bud_nuhma_comm_2025", ENT, "2025", "4650", "2025 commissaris ereloon Moore 4650; tick1355; primary official NBB WVV 9505"),
        ("bud_nuhma_cons_assets_2025", ENT, "2025", "1091188656", "2025 geconsolideerde activa 1091188656.35 deposit 2026-00124161; tick1355; primary official NBB CONSO; not TE-additive"),
        ("bud_nuhma_cons_pnl_2025", ENT, "2025", "15387829", "2025 geconsolideerde PnL 15387829.22; tick1355; primary official NBB CONSO"),
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
                "title": "NUHMA AC JR2025 leftover NV dual (assets 630.63m / pnl 8.77m / div 8.33m)",
                "entity_id": ENT,
                "beneficiary": "NUHMA AC NV / Nuhma cv / Limburg municipalities / Bionerga",
                "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-05-26",
                "start_year": "2018",
                "end_year": "2025",
                "total_envelope_eur": "630630603",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover NV map VL klimaat-holding — per-shareholder 8.33m dividend / 19.06m impairment / cv+Bionerga dual",
                "cut_option": "Publish per-shareholder 8.33m dividend dual + composition of 19.06m non-recurrent fin cost / 37.12m FVA drop + Nuhma cv recon + official-site JR; do not recreate parallel Limburg climate-holding NV shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1355; assets 630630603 pnl 8772737 div 8325000 fva drop 37120994; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "NUHMA AC JR2025 leftover NV: assets 630.63m / pnl 8.77m / div 8.33m / FVA drop 37.12m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "8325000",
                "total_cost_eur": "630630603",
                "tco_notes": "Leftover dual klimaat-holding NV of mined Limburg cities + Bionerga/Limburg.net: assets 630.63m DROP vs 679.34m / equity 607.10m DROP / pnl 8.77m DROP vs 22.96m / dividend 8.33m DROP vs 21.80m / FVA drop 37.12m / non-recurrent fin 19.06m; nuhma.be cv narrative 662.8m/26.3m does not match AC statutory; official NBB WVV live; do not treat 630.63m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "NUHMA AC NV / Nuhma cv / Limburg municipalities / Bionerga",
                "stated_goal": "Local leftover NV map VL klimaat-holding — JR2025 live; dual dividend/impairment/cv/Bionerga FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 630.63m / pnl 8.77m / div 8.33m / FVA drop 37.12m; commissaris Moore",
                "absurdity_score": "7.2",
                "cost_score": "7.4",
                "difficulty": "3.0",
                "priority_index": "6.9",
                "cut_proposal": "Publish per-shareholder 8.33m dividend dual + 19.06m impairment composition + Nuhma cv recon + official-site JR; do not recreate parallel Limburg climate-holding NV shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1355; leftover NV of mined Limburg + Bionerga 1354 / Limburg.net 1353; FOI ready not sent; not TE-additive of 348bn",
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
                    "Per-shareholder 2025-2026 dual lines for geplaatst kapitaal 470197930 "
                    "(38 Limburg cities + Laakdal / other public) + composition of non-recurrent "
                    "fin cost 19061672 (WVV 66B) and FVA drop 655068418 to 617947424 (verbonden "
                    "164104968 + deelnemingsverhouding 447544171; which participation Bionerga/"
                    "Aspiravi/Biostoom) + recon of AC statutory EV 607097228 / pnl 8772737 / "
                    "div 8325000 vs nuhma.be Nuhma cv 0472.325.068 narrative EV 662.8m / winst "
                    "26.3m + statutory JR of Nuhma cv itself + cons deposit 2026-00124161 "
                    "(assets 1091188656.35 / pnl 15387829.22) machine-readable + AV 26.05.2026 "
                    "minutes + commissaris Moore 4650 + official-site statutory JR PDF "
                    "(nuhma.be jaarverslag still 2020 PDF only)"
                ),
                "why_it_matters": (
                    "Leftover klimaat-holding NV shell of mined Limburg cities + Bionerga 1354 "
                    "+ Limburg.net 1353 (same zetel Herkenrodesingel 14; Nuhma cv is gedelegeerd "
                    "bestuurder): 630.63m assets / 8.33m dividend / 19.06m non-recurrent / "
                    "37.12m FVA drop vs website 662.8m-26.3m is a dual opacity residual, "
                    "not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "NUHMA AC NV / Nuhma cv / Limburg municipalities",
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
                    "tick1355 leftover NV of mined Limburg cities + Bionerga 1354 / Limburg.net 1353 after honest hunt; "
                    "live JR2025 official NBB WVV VOL-kap PDF now extracted (484kB 47p deposit 2026-00124430). "
                    "AGB MAC already mined 1270 — skipped. Westtoer already mined — skipped. "
                    "IOK/IMOG/Haviland still 2024. Interleuven still 2024 balans. "
                    "EcoWerf 2025 glossy / statutory unpublished on site. POM Limburg glossy-only. "
                    "Veneco/Leiedal glossy. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1355",
        "title": "NUHMA AC NV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: NUHMA AC leftover klimaat-holding NV of mined Limburg cities + Bionerga/Limburg.net "
            "after honest hunt; KBO 0697.972.507 Actief; live JR2025 official NBB WVV VOL-kap PDF "
            "(484kB 47p deposit 2026-00124430 + commissaris Moore); "
            "sourced euros assets 630.631m / equity 607.097m / pnl 8.773m / div 8.325m / fva drop 37.121m; "
            "FOI ready per-shareholder/impairment/cv-recon/Bionerga dual"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T00:40:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1355 NUHMA AC leftover NV residual; KBO 0697.972.507; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1356 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1356",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1355 done including NUHMA AC NV 1355 leftover klimaat-holding live NBB WVV / "
            "Bionerga NV 1354 leftover waste-processing live NBB WVV / "
            "Limburg.net 1353 leftover IGS glossy-only FOI / IVBO 1352 leftover IGS live WVV / "
            "SOLVA 1351 leftover IGS live JR / Interwaas 1350 leftover IGS live WVV + every-10 / "
            "Aquaduin / IWVA ov 1349 leftover IGS live WVV / Creat Services dv 1348 leftover IGS live WVV / "
            "IVIO Izegem-Ommeland 1347 leftover IGS live JR operational / WVI West-Vlaanderen 1346 leftover IGS live WVV / "
            "IVVO Veurne-Ommeland 1345 leftover IGS live WVV / ILvA Land van Aalst 1344 leftover IGS live WVV / "
            "IVM Meetjesland 1343 leftover IGS live WVV / IDM Durme-Moervaart 1342 leftover IGS live WVV / "
            "IGEAN dienstverlening 1341 leftover IGS live WVV / EVA Limburg Sterk Merk 1340 leftover EVA live WVV + every-10); "
            "Nuhma cv KBO 0472.325.068 2025 statutory still unpublished on nuhma.be (narrative EV 662.8m / winst 26.3m) — take only if a statutory WVV/BBC PDF now downloads; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "Veneco glossy jaarverslag 2025 websingle — take only if a WVV/BBC PDF now downloads; "
            "EcoWerf 2025 jaarverslag glossy / NBB deposit 2026-00256489 exists but official statutory still unpublished on site — take only if a WVV/BBC PDF now downloads from official site or staatsbladmonitor CDN; "
            "Leiedal 2025 InDesign glossy-only — take only if a WVV/BBC PDF now downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland still 2024 — take only if a 2025 JR PDF now downloads; "
            "IVOO no public 2025 JR PDF — take only if a 2025 JR PDF now downloads; "
            "MIROM 403 — take only if a 2025 JR PDF now downloads; "
            "INCOVO still 2024 — take only if a 2025 JR PDF now downloads; "
            "IVAGO activiteitenverslag 2025 listed but SSL EOF / ebesluit Gent TLS — take only if a statutory WVV/BBC PDF now downloads; "
            "MIWA 2025 aflip flipbook only — take only if a WVV/BBC PDF now downloads; "
            "IVAREM still 2024 / activiteitenverslag 2025 glossy — take only if a 2025 JR PDF now downloads; "
            "IGEMO activiteitenverslag 2025 only — take only if a WVV/BBC PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
            "WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / "
            "WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403; not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1355 after NUHMA AC leftover NV live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1355", rq_new, rq_spawn)
    print("research_queue 1355", found, "spawned_1356", spawned)

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
                "last_unit_id": "rq_1355",
                "ticks_completed": "1355",
                "paused": "no",
                "notes": (
                    "tick1355 NUHMA AC leftover NV residual; KBO 0697.972.507; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 630.631m equity 607.097m pnl 8.773m div 8.325m fva drop 37.121m; "
                    "FOI ready per-shareholder/impairment/cv-recon; next rq_1356 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1355 - 2026-08-19 - rq_1355 NUHMA AC NV dual residual leftover
- Unit: NUHMA AC NV (leftover klimaat-holding NV / 38 Limburg municipalities + Laakdal) of already-mined Limburg cities (Hasselt / Genk / Tongeren-Borgloon / Houthalen-Helchteren / Bilzen-Hoeselt / Leopoldsburg / Nieuwerkerken / Gingelom / Pelt / Maasmechelen; Maaseik AGB already mined) + leftover NV Bionerga tick1354 + leftover IGS Limburg.net tick1353 (same zetel Herkenrodesingel 14; Nuhma cv 0472.325.068 is gedelegeerd bestuurder of NUHMA AC) after residual dual hunt (KBO **0697.972.507**; official nuhma.be is Nuhma cv microsite — no statutory AC PDF; live NBB WVV VOL-kap deposit **2026-00124430** PDF 484kB / 47p; AV **26.05.2026**; neerlegging **27.05.2026**; commissaris Moore Audit / Jimmy Depré 05.05.2026 oordeel zonder voorbehoud). Leftover NV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last tick listed NUHMA as leftover later pending statutory WVV). Distinct from already-mined Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **15.06.2018**; statutaire naam NUHMA AC since 15.06.2018; Naamloze vennootschap since 15.06.2018; zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; **1 VE**; btw since 01.10.2018; KBO kapitaal **470.197.930**; jaarvergadering mei; 12 functiehouders; e-mail info@nuhma.be (cv page); tel 011 49 56 10; NACE 64.210. Hunt leftover AGB/zorg/EVA first: AGB MAC Mechelen 2025 BBC already mined tick1270 — skipped; SportAG Aalst / AGB Deinze / AGB Genk already mined — skipped; Westtoer APB already mined — skipped; IOK/IMOG/Haviland still 2024; Interleuven 2025 jaarverslag InDesign embed only / balans still 2024; EcoWerf 2025 glossy / NBB deposit 2026-00256489 listed but official statutory still unpublished on site — not taken once live NUHMA AC WVV extracted; POM Limburg glossy-only — not taken; Veneco/Leiedal glossy-only; IVAREM activiteitenverslag glossy; IGEMO activiteitenverslag only; IVOO no public 2025 JR; IVAGO SSL EOF; MIWA flipbook; MIROM Cloudflare; De Schorre provincieantwerpen.be 403; APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas no fetchable PDF; Dommelhof leftover Limburg EVA KBO 0777.495.085 no JR2025 PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE no fetchable 2025 JR this tick. Nuhma cv KBO 0472.325.068 leftover later (website narrative only). NBB consult skipped (403/SPA); euros extracted from the official VOL-kap deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345. Not every-10 (next 1360).
- EUR strong (primary official WVV VOL-kap + commissaris Moore oordeel zonder voorbehoud 05.05.2026): assets **630.630.603** (was 679.344.341); oprichting **16.719**; fixed/FVA **617.947.424** DROP vs 655.068.418 (verbonden **164.104.968** waarvan deeln **156.529.351** + vord **7.575.616**; deelnemingsverhouding **447.544.171** waarvan deeln **435.950.902** + vord **11.593.269**; andere **6.298.286**); current **12.666.460** DROP vs 24.254.768; ST recv **9.445.622** all overige; beleggingen **128.800** DROP vs 7.528.800; cash **3.089.512** DROP vs 6.823.778; equity **607.097.228** DROP vs 657.461.926 (kapitaal **470.197.930**; herwaardering **131.972.345** DROP vs 182.784.780; reserves **4.926.953**); schulden **23.533.375** (LT **15.169.577** all overige leningen; ST **8.360.620** waarvan dividend **8.325.000**); omzet unpublished; ops cost **163.323** (diensten **156.845** + afschr **4.436** + andere **2.042**); expl **−163.323**; fin opbr **28.584.984** (FVA **27.407.926**); fin kosten **19.410.816** waarvan niet-recurrent **19.061.672**; PnL **+8.772.737** DROP vs 22.963.457; dividend **8.325.000** DROP vs 21.800.000; belasting **238.108**. Pers **0** / VTE unpublished. Commissaris Moore **4.650**. Cons (deposit 2026-00124161): assets **1.091.188.656** / PnL **15.387.829**. Website cv narrative EV 662,8m / winst 26,3m does **not** match AC statutory — FOI recon.
- CSVs: sources+4/entities+1/budgets+38/commitments+1/leaderboard+1 + FOI ready `gap_nuhma_pnl_8_77m_div_8_33m_fva_drop_l5` (not sent); rq_1355=done; spawn rq_1356; ticks=1355.
- Coverage: residual dual L5 (NUHMA AC leftover NV live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1356 residual dual L5 VL JR2025 hole_fill (prefer Nuhma cv 0472.325.068 only if a statutory WVV/BBC PDF now downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; EcoWerf only if a statutory WVV/BBC PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; MIROM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1355 write done")


if __name__ == "__main__":
    main()

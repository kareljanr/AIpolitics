# -*- coding: utf-8 -*-
"""Tick 1354 — leftover Bionerga NV JR2025 official NBB WVV euros.
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

TICK = "1354"
UTC = "2026-08-19T00:40:00Z"
ENT = "nv_bionerga"
HIER = "Vlaanderen>Limburg>NV>Bionerga>AfvalVerwerking"
GAP = "gap_bng_omzet_22_56m_pnl_neg_33_80m_fva_drop_l5"
SRC = "src_bng_jr2025_nbb"
SRC2 = "src_bng_site"
SRC3 = "src_kbo_bng_0882280227"
SRC4 = "src_bng_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00156177.pdf"
SRC2_URL = "https://bionerga.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0882280227"
SRC4_URL = "https://bionerga.be/downloads/"
FOI_EMAIL = "info@bionerga.be"
FOI_POSTAL = "Herkenrodesingel 14 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_bng_omzet_22_56m_pnl_neg_33_80m_fva_drop_l5.md"
COMM = "comm_bng_jr2025_omzet"
LB = "lb_bng_omzet_22_56m_pnl_neg_33_80m_fva_drop"


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
                "title": "Bionerga NV jaarrekening boekjaar 2025 (official NBB WVV VOL-kap deposit 2026-00156177; AV 23.04.2026)",
                "url": SRC_URL,
                "publisher": "Bionerga NV / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1354; official NBB VOL-kap PDF 2.32MB 113p deposit 2026-00156177 neerlegging 12.06.2026; "
                    "leftover waste-processing NV of mined Limburg cities + Limburg.net IGS; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Bionerga official site (no JR2025 PDF on downloads)",
                "url": SRC2_URL,
                "publisher": "Bionerga NV",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1354; leftover NV of mined Limburg + Limburg.net; "
                    "downloads page compost/Biostoom milieu only; no statutory JR PDF"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Bionerga 0882.280.227",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1354; KBO 0882.280.227 Actief / normale toestand since 04.07.2006; "
                    "statutaire naam BIONERGA since 30.06.2006; NV since 30.06.2006; "
                    "zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; 7 VE; "
                    "aanbestedende overheid since 30.06.2006; btw since 01.08.2006; "
                    "RSZ since 01.07.2006; 15 bestuurders; NACE 38.210; databank 18.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Bionerga FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "Bionerga NV",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1354; FOI info@bionerga.be; Herkenrodesingel 14 3500 Hasselt "
                    "(same zetel as Limburg.net); commissaris BDO / Gert Maris"
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
                "name_nl": "Bionerga NV (leftover afvalverwerking Limburg / Limburg.net)",
                "name_fr": "Bionerga SA (traitement dechets residuel Limbourg / Limburg.net)",
                "name_en": "Bionerga NV leftover Limburg waste-processing (Limburg.net dual)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://bionerga.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1354 leftover residual waste-processing NV of mined Limburg cities + Limburg.net 1353 "
                    "(same zetel Herkenrodesingel 14; Thomas Vints on both boards); "
                    "KBO 0882.280.227 Actief since 04.07.2006; official NBB WVV VOL-kap PDF downloads; "
                    "sourced euros omzet 22.560m / assets 82.918m / pnl -33.798m / fva drop 24.631m / pers 5.491m; "
                    "FOI ready per-shareholder/impairment/Limburg.net dual"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_bng_assets_2025", ENT, "2025", "82918422", "2025 assets 82918422.46 commissaris; tick1354; primary official NBB WVV 20/58"),
        ("bud_bng_assets_2024", ENT, "2024", "117477776", "2024 assets 117477776.25 comparative; tick1354; primary official NBB WVV 20/58"),
        ("bud_bng_pnl_2025", ENT, "2025", "-33797727", "2025 PnL 9904 -33797727.39; tick1354; primary official NBB WVV + commissaris"),
        ("bud_bng_pnl_2024", ENT, "2024", "-24672272", "2024 PnL 9904 -24672271.66 comparative; tick1354; primary official NBB WVV"),
        ("bud_bng_fixed_2025", ENT, "2025", "54229996", "2025 vaste activa 54229996.29; tick1354; primary official NBB WVV 21/28"),
        ("bud_bng_current_2025", ENT, "2025", "28688426", "2025 vlottende activa 28688426.17; tick1354; primary official NBB WVV 29/58"),
        ("bud_bng_equity_2025", ENT, "2025", "39707904", "2025 eigen vermogen 39707904.27 DROP vs 73521905; tick1354; primary official NBB WVV 10/15"),
        ("bud_bng_equity_2024", ENT, "2024", "73521905", "2024 eigen vermogen 73521905 comparative; tick1354; primary official NBB WVV 10/15"),
        ("bud_bng_omzet_2025", ENT, "2025", "22559843", "2025 omzet 22559842.87; tick1354; primary official NBB WVV 70"),
        ("bud_bng_omzet_2024", ENT, "2024", "19363324", "2024 omzet 19363324.21 comparative; tick1354; primary official NBB WVV 70"),
        ("bud_bng_opsrev_2025", ENT, "2025", "30051914", "2025 bedrijfsopbrengsten 30051914.05; tick1354; primary official NBB WVV 70/76A"),
        ("bud_bng_pers_2025", ENT, "2025", "5491207", "2025 bezoldigingen 5491207; tick1354; primary official NBB WVV 62"),
        ("bud_bng_diensten_2025", ENT, "2025", "5347032", "2025 diensten 5347032; tick1354; primary official NBB WVV 61"),
        ("bud_bng_goods_2025", ENT, "2025", "14714182", "2025 handelsgoederen 14714182 (aankopen 14774295.26); tick1354; primary official NBB WVV 60"),
        ("bud_bng_afschr_2025", ENT, "2025", "1419285", "2025 afschrijvingen 1419285; tick1354; primary official NBB WVV 630"),
        ("bud_bng_expl_2025", ENT, "2025", "2730058", "2025 bedrijfswinst 2730057.56; tick1354; primary official NBB WVV 9901"),
        ("bud_bng_cash_2025", ENT, "2025", "7492359", "2025 liquide middelen 7492359 DROP vs 12182222; tick1354; primary official NBB WVV 54/58"),
        ("bud_bng_cash_2024", ENT, "2024", "12182222", "2024 liquide middelen 12182222 comparative; tick1354; primary official NBB WVV 54/58"),
        ("bud_bng_invest_2025", ENT, "2025", "10204923", "2025 geldbeleggingen 10204923; tick1354; primary official NBB WVV 50/53"),
        ("bud_bng_strecv_2025", ENT, "2025", "10632524", "2025 ST vorderingen 10632524 (trade 6656084 + other 3976440); tick1354; primary official NBB WVV 40/41"),
        ("bud_bng_fva_2025", ENT, "2025", "44240798", "2025 FVA 44240798 DROP vs 68872142 (verbonden 44094203); tick1354; primary official NBB WVV 28"),
        ("bud_bng_fva_2024", ENT, "2024", "68872142", "2024 FVA 68872142 comparative; tick1354; primary official NBB WVV 28"),
        ("bud_bng_mva_2025", ENT, "2025", "9989199", "2025 MVA 9989198.77 (gebouwen 7776781.42 + machines 792565.67 + rollend 1419851.68); tick1354; primary official NBB WVV 22/27"),
        ("bud_bng_debt_2025", ENT, "2025", "43037527", "2025 schulden 43037526.98; tick1354; primary official NBB WVV 17/49"),
        ("bud_bng_lt_2025", ENT, "2025", "32500000", "2025 LT schulden 32500000 (achtergesteld 6500000 + overige 26000000); tick1354; primary official NBB WVV 17"),
        ("bud_bng_st_2025", ENT, "2025", "10391335", "2025 ST schulden 10391335 (LT-within-year 2000000 + fin 5000000 + trade 2423870 + tax/soc 967466); tick1354; primary official NBB WVV 42/48"),
        ("bud_bng_nrfin_2025", ENT, "2025", "35809797", "2025 niet-recurrente fin kosten 35809797 WVV 66B; tick1354; primary official NBB WVV"),
        ("bud_bng_fincost_2025", ENT, "2025", "37332947", "2025 financiele kosten 37332946.75; tick1354; primary official NBB WVV 65/66B"),
        ("bud_bng_fininc_2025", ENT, "2025", "1430516", "2025 financiele opbrengsten 1430516.48; tick1354; primary official NBB WVV 75/76B"),
        ("bud_bng_otherops_2025", ENT, "2025", "6609865", "2025 andere bedrijfsopbrengsten 6609865.12; tick1354; primary official NBB WVV 74"),
        ("bud_bng_inbreng_2025", ENT, "2025", "37199735", "2025 inbreng/kapitaal 37199735.24; tick1354; primary official NBB WVV 10/11"),
        ("bud_bng_overgedragen_2025", ENT, "2025", "-3272758", "2025 overgedragen verlies -3272758.05; tick1354; primary official NBB WVV 14"),
        ("bud_bng_reserve_draw_2025", ENT, "2025", "31043943", "2025 onttrekking reserves 31043943; tick1354; primary official NBB WVV 792"),
        ("bud_bng_pledge_2025", ENT, "2025", "20110000", "2025 off-balance pand andere activa 20110000; tick1354; primary official NBB WVV 91812/91822"),
        ("bud_bng_comm_2025", ENT, "2025", "13795", "2025 commissaris ereloon BDO 13795 (groep 56655); tick1354; primary official NBB WVV 9505"),
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
                "title": "Bionerga JR2025 leftover NV dual (omzet 22.56m / assets 82.92m / pnl -33.80m)",
                "entity_id": ENT,
                "beneficiary": "Bionerga NV / Limburg municipalities / Limburg.net",
                "legal_basis": "WVV NV; aanbestedende overheid; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-04-23",
                "start_year": "2006",
                "end_year": "2025",
                "total_envelope_eur": "82918422",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover NV map VL waste-processing — per-shareholder 22.56m omzet / 35.81m impairment / Limburg.net dual",
                "cut_option": "Publish per-shareholder 22.56m omzet dual + composition of 35.81m non-recurrent fin cost / 24.63m FVA drop + official-site JR; do not recreate parallel Limburg waste-processing NV shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1354; omzet 22559843 assets 82918422 pnl -33797727 fva drop 24631344; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Bionerga JR2025 leftover NV: omzet 22.56m / pnl -33.80m / FVA drop 24.63m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "22559843",
                "total_cost_eur": "82918422",
                "tco_notes": "Leftover dual waste-processing NV of mined Limburg cities + Limburg.net: omzet 22.56m / expl +2.73m / non-recurrent fin 35.81m / PnL -33.80m / FVA drop 24.63m / assets 82.92m DROP vs 117.48m; official NBB WVV live; do not treat 82.92m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Bionerga NV / Limburg municipalities / Limburg.net",
                "stated_goal": "Local leftover NV map VL waste-processing — JR2025 live; dual omzet/impairment/Limburg.net FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: omzet 22.56m / assets 82.92m / pnl -33.80m / FVA drop 24.63m; commissaris BDO",
                "absurdity_score": "7.1",
                "cost_score": "6.4",
                "difficulty": "3.0",
                "priority_index": "6.6",
                "cut_proposal": "Publish per-shareholder 22.56m omzet dual + 35.81m impairment composition + official-site JR; do not recreate parallel Limburg waste-processing NV shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1354; leftover NV of mined Limburg + Limburg.net 1353; FOI ready not sent; not TE-additive of 348bn",
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
                    "Per-shareholder 2025-2026 dual lines for geplaatst kapitaal 37199735.24 "
                    "(Limburg cities / Limburg.net / other public) + composition of non-recurrent "
                    "fin cost 35809797 (WVV 66B) and FVA drop 68872142 to 44240798 (verbonden "
                    "deelnemingen 27156801 + vorderingen 16937401; which subsidiary Biostoom "
                    "Beringen/Oostende) + per-contract dual for omzet 22559842.87 vs Limburg.net "
                    "Optimo/verwerking fees (tick1353 glossy) + AV 23.04.2026 minutes + "
                    "commissaris BDO 13795 / group 56655 machine-readable + official-site JR PDF "
                    "(bionerga.be downloads has none)"
                ),
                "why_it_matters": (
                    "Leftover waste-processing NV shell of mined Limburg cities + Limburg.net "
                    "(same zetel Herkenrodesingel 14; Thomas Vints on both boards): 22.56m omzet "
                    "vs +2.73m expl / 35.81m non-recurrent fin / 33.80m loss / 24.63m FVA drop / "
                    "82.92m assets DROP vs 117.48m is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Bionerga NV / Limburg municipalities / Limburg.net",
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
                    "tick1354 leftover NV of mined Limburg cities + Limburg.net 1353 after honest hunt; "
                    "live JR2025 official NBB WVV VOL-kap PDF now extracted (2.32MB 113p deposit 2026-00156177). "
                    "AGB MAC already mined 1270 — skipped. Westtoer already mined — skipped. "
                    "IOK/IMOG/Haviland still 2024. Interleuven still 2024 balans. "
                    "EcoWerf 2025 glossy / statutory unpublished. POM Limburg glossy-only. "
                    "NUHMA 2025 microsite leftover later. Veneco/Leiedal glossy. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1354",
        "title": "Bionerga NV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Bionerga leftover waste-processing NV of mined Limburg cities + Limburg.net "
            "after honest hunt; KBO 0882.280.227 Actief; live JR2025 official NBB WVV VOL-kap PDF "
            "(2.32MB 113p deposit 2026-00156177 + commissaris BDO); "
            "sourced euros omzet 22.560m / assets 82.918m / pnl -33.798m / fva drop 24.631m; "
            "FOI ready per-shareholder/impairment/Limburg.net dual"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T00:05:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1354 Bionerga leftover NV residual; KBO 0882.280.227; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1355 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1355",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1354 done including Bionerga NV 1354 leftover waste-processing live NBB WVV / "
            "Limburg.net 1353 leftover IGS glossy-only FOI / IVBO 1352 leftover IGS live WVV / "
            "SOLVA 1351 leftover IGS live JR / Interwaas 1350 leftover IGS live WVV + every-10 / "
            "Aquaduin / IWVA ov 1349 leftover IGS live WVV / Creat Services dv 1348 leftover IGS live WVV / "
            "IVIO Izegem-Ommeland 1347 leftover IGS live JR operational / WVI West-Vlaanderen 1346 leftover IGS live WVV / "
            "IVVO Veurne-Ommeland 1345 leftover IGS live WVV / ILvA Land van Aalst 1344 leftover IGS live WVV / "
            "IVM Meetjesland 1343 leftover IGS live WVV / IDM Durme-Moervaart 1342 leftover IGS live WVV / "
            "IGEAN dienstverlening 1341 leftover IGS live WVV / EVA Limburg Sterk Merk 1340 leftover EVA live WVV + every-10); "
            "NUHMA 2025 jaarverslag microsite listed (EV 662.8m / winst 26.3m narrative) — take only if a statutory WVV/BBC PDF now downloads; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "Veneco glossy jaarverslag 2025 websingle — take only if a WVV/BBC PDF now downloads; "
            "EcoWerf 2025 jaarverslag glossy / statutory still unpublished — take only if a WVV/BBC PDF now downloads; "
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
            "skip already-mined Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
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
        "notes": "spawned tick1354 after Bionerga leftover NV live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1354", rq_new, rq_spawn)
    print("research_queue 1354", found, "spawned_1355", spawned)

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
                "last_unit_id": "rq_1354",
                "ticks_completed": "1354",
                "paused": "no",
                "notes": (
                    "tick1354 Bionerga leftover NV residual; KBO 0882.280.227; "
                    "live JR2025 NBB WVV PDF; sourced euros omzet 22.560m assets 82.918m pnl -33.798m fva drop 24.631m; "
                    "FOI ready per-shareholder/impairment; next rq_1355 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1354 - 2026-08-19 - rq_1354 Bionerga NV dual residual leftover
- Unit: Bionerga NV (leftover waste-processing NV / aanbestedende overheid) of already-mined Limburg cities (Hasselt / Genk / Tongeren-Borgloon / Houthalen-Helchteren / Bilzen-Hoeselt / Leopoldsburg / Nieuwerkerken / Gingelom; Maaseik AGB already mined) + leftover IGS Limburg.net tick1353 (same zetel Herkenrodesingel 14; Thomas Vints on both boards; tick1353 FOI already named Bionerga) after residual dual hunt (KBO **0882.280.227**; official bionerga.be has no JR PDF; live NBB WVV VOL-kap deposit **2026-00156177** PDF 2.32MB / 113p; AV **23.04.2026**; neerlegging **12.06.2026**; commissaris BDO / Gert Maris). Leftover NV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI). Distinct from already-mined Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **04.07.2006**; statutaire naam BIONERGA since 30.06.2006; Naamloze vennootschap since 30.06.2006; zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; **7 VE**; aanbestedende overheid since 30.06.2006; btw since 01.08.2006; RSZ since 01.07.2006; 15 bestuurders; e-mail info@bionerga.be; NACE 38.210. Hunt leftover AGB/zorg/EVA first: AGB MAC Mechelen 2025 BBC already mined tick1270 — skipped; SportAG Aalst / AGB Deinze / AGB Genk already mined — skipped; Westtoer APB already mined — skipped; IOK/IMOG/Haviland still 2024; Interleuven 2025 jaarverslag InDesign embed only / balans still 2024; EcoWerf 2025 glossy 16.38MB now downloads (narrative omzet 52.004m / 420 staff) but statutory jaarrekening still "wordt weldra gepubliceerd" — not taken once live Bionerga WVV extracted; POM Limburg 2025 JR 7.92MB 32p glossy-only no WVV — not taken; NUHMA 2025 jaarverslag microsite listed (EV 662.8m / winst 26.3m narrative) — leftover later; Veneco/Leiedal glossy-only; IVAREM activiteitenverslag glossy; IGEMO activiteitenverslag only; IVOO no public 2025 JR; IVAGO SSL EOF; MIWA flipbook; MIROM Cloudflare; De Schorre provincieantwerpen.be 403; APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas no fetchable PDF; Dommelhof leftover Limburg EVA KBO 0777.495.085 no JR2025 PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE no fetchable 2025 JR this tick. NBB consult skipped (403/SPA); euros extracted from the official VOL-kap deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345. Not every-10 (next 1360).
- EUR strong (primary official WVV VOL-kap + commissaris BDO assets 82.918.422,46 / PnL −33.797.727,39): assets **82.918.422** (was 117.477.776); fixed **54.229.996**; MVA **9.989.199** (gebouwen **7.776.781** + machines **792.566** + rollend **1.419.852**); FVA **44.240.798** DROP vs 68.872.142 (verbonden **44.094.203** waarvan deelnemingen **27.156.801** + vorderingen **16.937.401**); current **28.688.426**; voorraden **136.289**; ST recv **10.632.524** (trade **6.656.084** + other **3.976.440**); beleggingen **10.204.923**; cash **7.492.359** DROP vs 12.182.222; equity **39.707.904** DROP vs 73.521.905 (kapitaal **37.199.735**; reserves **4.196.739**; overgedragen **−3.272.758**); schulden **43.037.527** (LT **32.500.000** achtergesteld **6.500.000** + overige **26.000.000**; ST **10.391.335**); ops rev **30.051.914**; omzet **22.559.843** JUMP vs 19.363.324; andere **6.609.865**; pers **5.491.207**; VTE **47,9** / YE 49 koppen 47,5 VTE; diensten **5.347.032**; goods **14.714.182**; afschr **1.419.285**; expl **+2.730.058**; fin opbr **1.430.516**; fin kosten **37.332.947** waarvan niet-recurrent **35.809.797**; PnL **−33.797.727** (was −24.672.272). Off-balance pand **20.110.000**. Reserve onttrekking **31.043.943**. Commissaris BDO **13.795** + groep **56.655**.
- CSVs: sources+4/entities+1/budgets+35/commitments+1/leaderboard+1 + FOI ready `gap_bng_omzet_22_56m_pnl_neg_33_80m_fva_drop_l5` (not sent); rq_1354=done; spawn rq_1355; ticks=1354.
- Coverage: residual dual L5 (Bionerga leftover NV live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1355 residual dual L5 VL JR2025 hole_fill (prefer NUHMA 2025 only if a statutory WVV/BBC PDF now downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; EcoWerf only if a statutory WVV/BBC PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; MIROM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1354 write done")


if __name__ == "__main__":
    main()

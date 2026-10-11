# -*- coding: utf-8 -*-
"""Tick 1351 — leftover IGS SOLVA JR2025 official euros.
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

TICK = "1351"
UTC = "2026-08-18T22:50:00Z"
ENT = "igs_solva"
HIER = "Vlaanderen>OostVlaanderen>IGS>SOLVA>VlaamseArdennenDender"
GAP = "gap_solva_omzet_25_52m_stock_47_2m_pnl_neg_0_20m_l5"
SRC = "src_solva_jr2025_pdf"
SRC2 = "src_solva_site"
SRC3 = "src_kbo_solva_0200305493"
SRC4 = "src_solva_foi_contact"
SRC5 = "src_solva_av_20260617"
SRC_URL = "https://www.so-lva.be/wp-content/uploads/2026/06/Jaarverslag-2025.pdf"
SRC2_URL = "https://www.so-lva.be/over-solva/publicaties/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0200305493"
SRC4_URL = "https://www.so-lva.be/contact/"
SRC5_URL = "https://www.so-lva.be/wp-content/uploads/2026/07/Notulen-AV-SOLVA-17-juni-2026-signed.pdf"
FOI_EMAIL = "info@so-lva.be"
FOI_POSTAL = "Gentsesteenweg 1B 9520 Sint-Lievens-Houtem"
DRAFT = "docs/doge/foi/drafts/gap_solva_omzet_25_52m_stock_47_2m_pnl_neg_0_20m_l5.md"
COMM = "comm_solva_jr2025_omzet"
LB = "lb_solva_omzet_25_52m_stock_47_2m_pnl_neg"


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
                "title": "SOLVA jaarverslag boekjaar 2025 (official JR + commissarisverslag WVV; Ghostscript 18.06.2026)",
                "url": SRC_URL,
                "publisher": "SOLVA dienstverlenende vereniging",
                "accessed_date": "2026-08-18",
                "source_class": "budget",
                "notes": (
                    "tick1351; official PDF 8.34MB 102p Ghostscript 18.06.2026; leftover IGS streek/project "
                    "of mined Vlaamse Ardennen+Dender cities; embedded financial commentaar + commissaris "
                    "Vyvey 20.04.2026 oordeel zonder voorbehoud assets 64235491 PnL -197137"
                ),
            },
            {
                "source_id": SRC2,
                "title": "SOLVA official publicaties page (KBO 0200.305.493)",
                "url": SRC2_URL,
                "publisher": "SOLVA",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1351; leftover IGS streek/project of mined Vlaamse Ardennen+Dender cities; "
                    "lists Jaarverslag-2025.pdf plus AV 17.06.2026 notulen"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO SOLVA 0200.305.493",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1351; KBO 0200.305.493 Actief / normale toestand since 19.03.1962; "
                    "statutaire naam Intergemeentelijk Samenwerkingsverband voor ruimtelijke ordening "
                    "en socio-economische expansie since 01.11.2003; afkorting SOLVA since 01.11.2003; "
                    "Dienstverlenende vereniging (Vlaams Gewest) since 25.02.2005; zetel Gentsesteenweg 1B "
                    "9520 Sint-Lievens-Houtem since 01.12.2017; 2 VE; aanbestedende overheid since 01.01.1922; "
                    "btw since 01.01.1971; RSZ since 01.01.2022; jaarvergadering mei; boekjaar 31 december; "
                    "KBO kapitaal 125000; databank 17.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "SOLVA FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "SOLVA",
                "accessed_date": "2026-08-18",
                "source_class": "official_register",
                "notes": (
                    "tick1351; FOI info@so-lva.be / contact form so-lva.be/contact/; "
                    "Gentsesteenweg 1B 9520 Sint-Lievens-Houtem; T 053 64 65 20; "
                    "voorzitter Martine De Maght; directeur Bart Wallays"
                ),
            },
            {
                "source_id": SRC5,
                "title": "SOLVA AV 17.06.2026 notulen (goedkeuring jaarrekening 2025)",
                "url": SRC5_URL,
                "publisher": "SOLVA",
                "accessed_date": "2026-08-18",
                "source_class": "budget",
                "notes": (
                    "tick1351; official signed AV minutes 11p; 30160/44725 aandelen 67pct; "
                    "approved jaarverslag + jaarrekening 2025; quotes verlies 197137 / "
                    "vaste activa 8481461 / cash 2989696"
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
                "name_nl": "SOLVA (leftover IGS streek/project Vlaamse Ardennen en Dender)",
                "name_fr": "SOLVA (association de services / IGS residuel / amenagement et expansion socio-economique)",
                "name_en": "SOLVA Flemish Ardennes/Dender intermunicipal development (leftover IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.so-lva.be",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1351 leftover IGS residual streek/project of mined Vlaamse Ardennen+Dender cities "
                    "(Aalst/Geraardsbergen/Zottegem/Ninove/Ronse/Oudenaarde + leftover Zwalm/"
                    "Wortegem-Petegem/Maarkedal; AGB De Kluize already FOI); "
                    "KBO 0200.305.493 Actief since 19.03.1962; official JR2025 PDF downloads; "
                    "sourced euros omzet 25.519m / assets 64.235m / cash JUMP 2.825m / PnL -0.197m; "
                    "FOI ready per-vennoot/stock/NBB"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_solva_assets_2025", ENT, "2025", "64235491", "2025 assets 64235491 commissaris; tick1351; primary official JR"),
        ("bud_solva_pnl_2025", ENT, "2025", "-197137", "2025 PnL -197137; tick1351; primary official JR + commissaris + AV"),
        ("bud_solva_fixed_2025", ENT, "2025", "8481461", "2025 vaste activa 8481461; tick1351; primary official JR"),
        ("bud_solva_fixed_2024", ENT, "2024", "8473135", "2024 vaste activa 8473135 comparative; tick1351; primary official JR"),
        ("bud_solva_cash_2025", ENT, "2025", "2989696", "2025 liquide middelen 2989696 JUMP vs 164719; tick1351; primary official JR"),
        ("bud_solva_cash_2024", ENT, "2024", "164719", "2024 liquide middelen 164719 comparative; tick1351; primary official JR"),
        ("bud_solva_accrual_2025", ENT, "2025", "725349", "2025 overlopende rekeningen 725349; tick1351; primary official JR"),
        ("bud_solva_accrual_2024", ENT, "2024", "1346260", "2024 overlopende rekeningen 1346260 comparative; tick1351; primary official JR"),
        ("bud_solva_ltdebt_2025", ENT, "2025", "259650", "2025 LT schulden 259650; tick1351; primary official JR"),
        ("bud_solva_ltdebt_2024", ENT, "2024", "281288", "2024 LT schulden 281288 comparative; tick1351; primary official JR"),
        ("bud_solva_diensten_2025", ENT, "2025", "1312460", "2025 diensten 1312460; tick1351; primary official JR"),
        ("bud_solva_diensten_2024", ENT, "2024", "1124490", "2024 diensten 1124490 comparative; tick1351; primary official JR"),
        ("bud_solva_afschr_2025", ENT, "2025", "237881", "2025 afschrijvingen 237881; tick1351; primary official JR"),
        ("bud_solva_afschr_2024", ENT, "2024", "351085", "2024 afschrijvingen 351085 comparative; tick1351; primary official JR"),
        ("bud_solva_fincost_2025", ENT, "2025", "429332", "2025 financiele kosten 429332; tick1351; primary official JR"),
        ("bud_solva_fincost_2024", ENT, "2024", "448390", "2024 financiele kosten 448390 comparative; tick1351; primary official JR"),
        ("bud_solva_severance_2025", ENT, "2025", "155500", "2025 niet-recurrente ontslagvergoeding 155500 RvB dec 2025; tick1351; primary official JR"),
        ("bud_solva_omzet_2025", ENT, "2025", "25518838", "2025 omzet 25518837.60 sum official 70-tabel JUMP vs 15307519.24; tick1351; primary official JR"),
        ("bud_solva_omzet_2024", ENT, "2024", "15307519", "2024 omzet 15307519.24 sum official 70-tabel comparative; tick1351; primary official JR"),
        ("bud_solva_omzet_infra_2025", ENT, "2025", "13258535", "2025 verkoop gemeentelijke infra 13258534.73; tick1351; primary official JR 709300"),
        ("bud_solva_omzet_infra_2024", ENT, "2024", "6462314", "2024 verkoop gemeentelijke infra 6462314.19 comparative; tick1351; primary official JR 709300"),
        ("bud_solva_omzet_arch_2025", ENT, "2025", "3227014", "2025 archeologie 3227014.14; tick1351; primary official JR 700001"),
        ("bud_solva_omzet_studie_2025", ENT, "2025", "2714125", "2025 studie- en begeleiding 2714124.52; tick1351; primary official JR 700004"),
        ("bud_solva_omzet_bt_2025", ENT, "2025", "3769505", "2025 verkoop bedrijventerreinen 3769504.57; tick1351; primary official JR 709200"),
        ("bud_solva_omzet_wonen_2025", ENT, "2025", "863885", "2025 verkoop projectontwikkeling wonen 863884.85; tick1351; primary official JR 709314"),
        ("bud_solva_omzet_huur_2025", ENT, "2025", "658555", "2025 huurinkomsten 658554.97; tick1351; primary official JR 709400"),
        ("bud_solva_omzet_prev_2025", ENT, "2025", "551996", "2025 preventiedienst GIP PBW 551996.20; tick1351; primary official JR 700350"),
        ("bud_solva_omzet_regio_2025", ENT, "2025", "130009", "2025 bijdrage regiowerking 130008.89; tick1351; primary official JR 700400"),
        ("bud_solva_omzet_klimaat_2025", ENT, "2025", "104641", "2025 bijdrage klimaatwerking 104640.61; tick1351; primary official JR 700450"),
        ("bud_solva_omzet_energ_2025", ENT, "2025", "171527", "2025 energieleningen 171526.77; tick1351; primary official JR 709100"),
        ("bud_solva_omzet_vme_2025", ENT, "2025", "69047", "2025 beheersvergoeding VME 69047.35; tick1351; primary official JR 709105"),
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
                "title": "SOLVA JR2025 leftover IGS dual (omzet 25.52m / stock ~47.2m / PnL -0.20m)",
                "entity_id": ENT,
                "beneficiary": "SOLVA / 21 Vlaamse Ardennen+Dender vennoten",
                "legal_basis": "Decreet lokaal bestuur IGS; dienstverlenende vereniging; Bestuursdecreet openbaarheid; WVV neerlegging",
                "decision_date": "2026-06-17",
                "start_year": "1962",
                "end_year": "2025",
                "total_envelope_eur": "64235491",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL streek/project — per-vennoot 25.52m omzet / stock 47.2m / NBB",
                "cut_option": "Publish per-vennoot 25.52m omzet / 13.26m city infra dual city lines + stock 47.2m recon + full statutory NBB; do not recreate parallel Vlaamse Ardennen/Dender IGS project shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1351; omzet 25518838 assets 64235491 cash JUMP 2989696 vs 164719 PnL -197137; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "SOLVA JR2025 leftover IGS: omzet 25.52m / stock ~47.2m / PnL -0.20m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "25518838",
                "total_cost_eur": "64235491",
                "tco_notes": "Leftover dual IGS streek/project of mined Vlaamse Ardennen+Dender cities: omzet 25.52m JUMP / city infra 13.26m / cash JUMP 2.83m / stock ~47.2m narrative / assets 64.24m / PnL -0.20m; official JR live; do not treat 64.24m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "SOLVA / 21 Vlaamse Ardennen+Dender vennoten",
                "stated_goal": "Local leftover IGS map VL streek/project — JR2025 live; dual omzet/stock/NBB FOI",
                "measured_outcome": "Official JR 2026-08-18: omzet 25.52m / assets 64.24m / cash 2.99m JUMP vs 0.16m / PnL -0.20m; commissaris zonder voorbehoud",
                "absurdity_score": "6.1",
                "cost_score": "6.5",
                "difficulty": "3.0",
                "priority_index": "6.1",
                "cut_proposal": "Publish per-vennoot 25.52m omzet / 13.26m city infra dual city lines + stock 47.2m recon + full statutory NBB; do not recreate parallel Vlaamse Ardennen/Dender IGS project shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1351; leftover IGS streek/project of mined Vlaamse Ardennen+Dender cities; FOI ready not sent; not TE-additive of 348bn",
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
                    "Per-vennoot 2025-2026 dual lines for omzet 25518837.60 (JUMP vs 15307519.24; "
                    "city infra 13258534.73 vs 6462314.19) + exact WVV (not rounded commentaar) for "
                    "stock ~47.2m vs ~45m / ST recv ~4.7m vs ~5.2m / inbreng ~26.94m vs ~26.91m / "
                    "voorzieningen ~2.78m vs ~2.91m / ST debt ~25.4m vs ~21m + R/C aandeelhouders ~3m / "
                    "bezoldigingen ~9m vs severance 155500 + handelsgoederen ~17.6m + recon cash 2989696 "
                    "JUMP vs 164719 vs kredietlijn + full statutory jaarrekening (jaarverslag is commentaar "
                    "+ commissaris, no full WVV schema) + commissarisverslag ereloon + AV 17.06.2026 "
                    "minutes already public + NBB filing"
                ),
                "why_it_matters": (
                    "Leftover IGS streek/project shell of mined Vlaamse Ardennen+Dender cities "
                    "(Aalst/Geraardsbergen/Zottegem/Ninove/Ronse/Oudenaarde + leftover Zwalm/"
                    "Wortegem-Petegem/Maarkedal; AGB De Kluize already FOI): 25.52m omzet vs "
                    "~47.2m stock / 2.83m cash JUMP / ~25.4m ST debt / PnL -0.20m is a dual "
                    "opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "SOLVA / 21 Vlaamse Ardennen+Dender vennoten",
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
                    "tick1351 leftover IGS streek/project of mined Vlaamse Ardennen+Dender cities after honest hunt; "
                    "live JR2025 official PDF now extracted (8.34MB 102p Ghostscript 18.06.2026). "
                    "EcoWerf 2025 glossy / 2024 statutory still unpublished. Interleuven still 2024 balans. "
                    "IOK/IMOG/Haviland/IVBO/Limburg.net still 2024. Veneco/Leiedal glossy-only. MIROM 403. "
                    "IVAGO SSL EOF / ebesluit Gent TLS. MIWA 2025 flipbook. NBB consult skipped. "
                    "Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1351",
        "title": "SOLVA JR2025 leftover IGS dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: SOLVA leftover IGS streek/project of mined Vlaamse Ardennen+Dender cities "
            "after honest hunt; KBO 0200.305.493 Actief; live JR2025 official PDF "
            "(8.34MB 102p Ghostscript 18.06.2026 + AV 17.06.2026 + commissaris 20.04.2026); "
            "sourced euros omzet 25.519m / assets 64.235m / cash JUMP 2.825m / PnL -0.197m; "
            "FOI ready per-vennoot/stock/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T22:20:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1351 SOLVA leftover IGS residual; KBO 0200.305.493; "
            "live JR2025 PDF; sourced euros; FOI ready not sent; next rq_1352 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1352",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1351 done including SOLVA 1351 leftover IGS live JR / "
            "Interwaas 1350 leftover IGS live WVV + every-10 / "
            "Aquaduin / IWVA ov 1349 leftover IGS live WVV / "
            "Creat Services dv 1348 leftover IGS live WVV / "
            "IVIO Izegem-Ommeland 1347 leftover IGS live JR operational / "
            "WVI West-Vlaanderen 1346 leftover IGS live WVV / "
            "IVVO Veurne-Ommeland 1345 leftover IGS live WVV / "
            "ILvA Land van Aalst 1344 leftover IGS live WVV / "
            "IVM Meetjesland 1343 leftover IGS live WVV / "
            "IDM Durme-Moervaart 1342 leftover IGS live WVV / "
            "IGEAN dienstverlening 1341 leftover IGS live WVV / "
            "EVA Limburg Sterk Merk 1340 leftover EVA live WVV + every-10); "
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
            "IVAGO activiteitenverslag 2025 listed but SSL EOF / ebesluit Gent TLS — take only if a statutory WVV/BBC PDF now downloads; "
            "MIWA 2025 aflip flipbook only — take only if a WVV/BBC PDF now downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "IGEMO activiteitenverslag 2025 only — take only if a WVV/BBC PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
            "WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / "
            "WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403; not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1351 after SOLVA leftover IGS live JR; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1351", rq_new, rq_spawn)
    print("research_queue 1351", found, "spawned_1352", spawned)

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
                "last_unit_id": "rq_1351",
                "ticks_completed": "1351",
                "paused": "no",
                "notes": (
                    "tick1351 SOLVA leftover IGS residual; KBO 0200.305.493; "
                    "live JR2025 PDF; sourced euros omzet 25.519m assets 64.235m cash JUMP 2.825m PnL -0.197m; "
                    "FOI ready per-vennoot/stock/NBB; next rq_1352 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1351 - 2026-08-18 - rq_1351 SOLVA dual residual leftover IGS
- Unit: SOLVA (dienstverlenende vereniging / leftover IGS streek/project; statutaire naam Intergemeentelijk Samenwerkingsverband voor ruimtelijke ordening en socio-economische expansie) of already-mined Vlaamse Ardennen + Dender cities (Aalst / Geraardsbergen / Zottegem / Ninove / Ronse / Oudenaarde + leftover Zwalm / Wortegem-Petegem / Maarkedal; AGB De Kluize already FOI) after residual dual hunt (KBO **0200.305.493**; official so-lva.be + live jaarverslag 2025 PDF 8.34MB / 102p; Ghostscript **18.06.2026**; AV **17.06.2026** approved jaarrekening; commissaris Vyvey **20.04.2026** oordeel zonder voorbehoud). Leftover IGS whose official page now yields a downloadable JR2025 PDF with euros (prefer live PDF over another unpublished FOI). Distinct from already-mined Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341. KBO Actief / normale toestand since **19.03.1962**; Dienstverlenende vereniging (Vlaams Gewest) since 25.02.2005; zetel Gentsesteenweg 1B 9520 Sint-Lievens-Houtem since 01.12.2017; **2 VE**; aanbestedende overheid since 01.01.1922; btw since 01.01.1971; RSZ since 01.01.2022; jaarvergadering mei; boekjaar 31 december; KBO kapitaal 125.000; voorzitter Martine De Maght; directeur Bart Wallays since 01.05.2016; tel 053 64 65 20; NACE 82.990 / 68.122 / 94.999 / 71.122 / 41.003 / RSZ 84.130. Hunt leftover AGB/zorg/EVA first: IVAGO activiteitenverslag 2025 listed but SSL EOF / ebesluit Gent TLS skip; MIWA 2025 aflip flipbook not statutory; EcoWerf 2025 glossy / 2024 statutory still unpublished; Interleuven still 2024 balans; IOK/IMOG/Haviland/IVBO/Limburg.net still 2024; IVOO no public 2025 JR; IVAREM still 2024; IGEMO activiteitenverslag only; INCOVO still 2024; MIROM 403; Veneco/Leiedal glossy-only; Dommelhof leftover Limburg EVA KBO 0777.495.085 not taken once live SOLVA extracted. De Schorre JR2025 listed on provincieantwerpen.be 403 — not taken. APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas official pages no fetchable PDF — not taken. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340. Not every-10 (next 1360).
- EUR strong (primary official JR + commissaris): assets **64.235.491**; PnL **−197.137**; vaste activa **8.481.461** (was 8.473.135); cash **2.989.696** JUMP vs 164.719; overlopend **725.349** (was 1.346.260); LT schulden **259.650** (was 281.288); diensten **1.312.460** (was 1.124.490); afschr **237.881** (was 351.085); fin cost **429.332** (was 448.390); ontslagvergoeding **155.500**. Omzet-tabel 70 exact sum **25.518.838** JUMP vs **15.307.519** waarvan gemeentelijke infra **13.258.535** (was 6.462.314) + archeologie **3.227.014** + studie **2.714.125** + bedrijventerreinen **3.769.505** + wonen **863.885** + huur **658.555** + preventie **551.996** + regio **130.009** + klimaat **104.641** + energieleningen **171.527** + VME **69.047**. Narrative rounded only (FOI exact): stock ~47,2m (was ~45m); ST recv ~4,7m (was ~5,2m); inbreng ~26,94m (was ~26,91m); voorzieningen ~2,78m (was ~2,91m); ST schulden ~25,4m (was ~21m) + R/C aandeelhouders ~3m; andere ops ~3,2m; handelsgoederen ~17,6m; bezoldigingen ~9m. Commissaris oordeel zonder voorbehoud.
- CSVs: sources+5/entities+1/budgets+31/commitments+1/leaderboard+1 + FOI ready `gap_solva_omzet_25_52m_stock_47_2m_pnl_neg_0_20m_l5` (not sent); rq_1351=done; spawn rq_1352; ticks=1351.
- Next: rq_1352 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland/IVBO/Limburg.net only if a 2025 JR PDF now downloads; EcoWerf only if a statutory WVV/BBC PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; MIROM only if a 2025 JR PDF now downloads; IVAGO only if a statutory WVV/BBC PDF now downloads; MIWA only if a WVV/BBC PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1351 write done")


if __name__ == "__main__":
    main()

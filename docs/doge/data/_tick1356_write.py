# -*- coding: utf-8 -*-
"""Tick 1356 — leftover Nuhma cv JR2025 official NBB WVV euros.
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

TICK = "1356"
UTC = "2026-08-19T01:50:00Z"
ENT = "cv_nuhc"
HIER = "Vlaanderen>Limburg>CV>Nuhma>KlimaatHolding"
GAP = "gap_nuhc_pnl_26_27m_div_33_50m_fva_drop_l5"
SRC = "src_nuhc_jr2025_nbb"
SRC2 = "src_nuhc_site"
SRC3 = "src_kbo_nuhc_0472325068"
SRC4 = "src_nuhc_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00154816.pdf"
SRC2_URL = "https://nuhma.be/duurzaam-rendement-in-2025/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0472325068"
SRC4_URL = "https://nuhma.be/contact/"
FOI_EMAIL = "info@nuhma.be"
FOI_POSTAL = "Herkenrodesingel 14 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_nuhc_pnl_26_27m_div_33_50m_fva_drop_l5.md"
COMM = "comm_nuhc_jr2025_pnl"
LB = "lb_nuhc_pnl_26_27m_div_33_50m_fva_drop"


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
                "title": "Nuhma cv jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00154816; AV 01.06.2026)",
                "url": SRC_URL,
                "publisher": "Nuhma cv / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1356; official NBB VOL-inb PDF 3.17MB 65p deposit 2026-00154816 neerlegging 08.06.2026; "
                    "leftover klimaat-holding cv of mined Limburg cities + NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; cons deposit 2026-00153822 3.32MB 64p"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Nuhma official site 2025 kerncijfers (Nuhma cv; now matches statutory EV 662.8m / winst 26.3m)",
                "url": SRC2_URL,
                "publisher": "Nuhma cv",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1356; leftover cv of mined Limburg + NUHMA AC/Bionerga/Limburg.net; "
                    "nuhma.be is Nuhma cv KBO 0472.325.068; narrative EV 662.8m / winst 26.3m "
                    "MATCHES cv statutory 662794232 / 26272333 (does not match AC 607.10m / 8.77m); "
                    "jaarverslag page still 2020 PDF only"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Nuhma cv 0472.325.068",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1356; KBO 0472.325.068 Actief / normale toestand since 07.07.2000; "
                    "statutaire naam NUTSBEDRIJVEN HOUDSTERMAATSCHAPPIJ / NUHMA since 28.06.2000; "
                    "CV since 08.10.2024; zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; 1 VE; "
                    "aanbestedende overheid since 28.06.2000; btw since 01.01.2008; RSZ since 04.02.2008; "
                    "jaarvergadering juni; 9 bestuurders; NACE 64.210"
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
                    "tick1356; FOI info@nuhma.be; 011 49 56 10; Herkenrodesingel 14 3500 Hasselt "
                    "(same zetel as NUHMA AC / Bionerga / Limburg.net); commissaris Moore Audit / Jimmy Depré"
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
                "name_nl": "Nuhma cv (leftover klimaat-holding coop Limburg / NUHMA AC / Bionerga)",
                "name_fr": "Nuhma sc (holding climat residuel Limbourg / NUHMA AC / Bionerga)",
                "name_en": "Nuhma cv leftover Limburg climate-holding cooperative (NUHMA AC/Bionerga dual)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://nuhma.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1356 leftover residual klimaat-holding cv of mined Limburg cities + NUHMA AC 1355 "
                    "+ Bionerga 1354 + Limburg.net 1353 (same zetel Herkenrodesingel 14; 100pct of NUHMA AC); "
                    "KBO 0472.325.068 Actief since 07.07.2000; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 693.833m / equity 662.794m / pnl 26.272m / div 33.501m / fva drop 58.533m; "
                    "FOI ready per-vennoot/impairment/AC-recon/cons"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_nuhc_assets_2025", ENT, "2025", "693832591", "2025 assets 693832591 VOL-inb 20/58; tick1356; primary official NBB WVV"),
        ("bud_nuhc_assets_2024", ENT, "2024", "755820904", "2024 assets 755820904 comparative; tick1356; primary official NBB WVV 20/58"),
        ("bud_nuhc_pnl_2025", ENT, "2025", "26272333", "2025 PnL 9904 26272333; tick1356; primary official NBB WVV + commissaris Moore"),
        ("bud_nuhc_pnl_2024", ENT, "2024", "10315591", "2024 PnL 9904 10315591 comparative; tick1356; primary official NBB WVV"),
        ("bud_nuhc_fixed_2025", ENT, "2025", "688809513", "2025 vaste activa 688809513; tick1356; primary official NBB WVV 21/28"),
        ("bud_nuhc_current_2025", ENT, "2025", "5006364", "2025 vlottende activa 5006364 DROP vs 9237260; tick1356; primary official NBB WVV 29/58"),
        ("bud_nuhc_equity_2025", ENT, "2025", "662794232", "2025 eigen vermogen 662794232 DROP vs 730495885; tick1356; primary official NBB WVV 10/15; matches website 662.8m"),
        ("bud_nuhc_equity_2024", ENT, "2024", "730495885", "2024 eigen vermogen 730495885 comparative; tick1356; primary official NBB WVV 10/15"),
        ("bud_nuhc_inbreng_2025", ENT, "2025", "303515270", "2025 inbreng 303515270 (beschikbaar 26597620 + onbeschikbaar 276917650); tick1356; primary official NBB WVV 10/11"),
        ("bud_nuhc_herw_2025", ENT, "2025", "148643187", "2025 herwaardering 148643187 DROP vs 209116567; tick1356; primary official NBB WVV 12"),
        ("bud_nuhc_herw_2024", ENT, "2024", "209116567", "2024 herwaardering 209116567 comparative; tick1356; primary official NBB WVV 12"),
        ("bud_nuhc_reserves_2025", ENT, "2025", "210635775", "2025 reserves 210635775 (statutair 124948075 + beschikbaar 85687700); tick1356; primary official NBB WVV 13"),
        ("bud_nuhc_setup_2025", ENT, "2025", "16714", "2025 oprichtingskosten 16714; tick1356; primary official NBB WVV 20"),
        ("bud_nuhc_fva_2025", ENT, "2025", "686781779", "2025 FVA 686781779 DROP vs 745315000; tick1356; primary official NBB WVV 28"),
        ("bud_nuhc_fva_2024", ENT, "2024", "745315000", "2024 FVA 745315000 comparative; tick1356; primary official NBB WVV 28"),
        ("bud_nuhc_fva_verb_2025", ENT, "2025", "686144385", "2025 FVA verbonden 686144385 (deeln 650466151 + vord 35678233); tick1356; primary official NBB WVV 280/1"),
        ("bud_nuhc_fva_deel_2025", ENT, "2025", "637394", "2025 FVA deelnemingsverhouding 637394 (deeln 319388 + vord 318006); tick1356; primary official NBB WVV 282/3"),
        ("bud_nuhc_mva_2025", ENT, "2025", "2027735", "2025 MVA 2027735 (machines 60707 + rollend 924876 + overige 1042152); tick1356; primary official NBB WVV 22/27"),
        ("bud_nuhc_strecv_2025", ENT, "2025", "660311", "2025 ST vorderingen 660311 (trade 486283 + other 174028); tick1356; primary official NBB WVV 40/41"),
        ("bud_nuhc_invest_2025", ENT, "2025", "0", "2025 geldbeleggingen 0 DROP vs 7000000; tick1356; primary official NBB WVV 50/53"),
        ("bud_nuhc_invest_2024", ENT, "2024", "7000000", "2024 geldbeleggingen 7000000 comparative; tick1356; primary official NBB WVV 50/53"),
        ("bud_nuhc_cash_2025", ENT, "2025", "3949440", "2025 liquide middelen 3949440 JUMP vs 945349; tick1356; primary official NBB WVV 54/58"),
        ("bud_nuhc_cash_2024", ENT, "2024", "945349", "2024 liquide middelen 945349 comparative; tick1356; primary official NBB WVV 54/58"),
        ("bud_nuhc_debt_2025", ENT, "2025", "31038359", "2025 schulden 31038359; tick1356; primary official NBB WVV 17/49"),
        ("bud_nuhc_st_2025", ENT, "2025", "27046058", "2025 ST schulden 27046058 (trade 278544 + tax/soc 1265131 + other 25502384); tick1356; primary official NBB WVV 42/48"),
        ("bud_nuhc_div_2025", ENT, "2025", "33500606", "2025 uit te keren winst/dividend 33500606 JUMP vs 17000000; tick1356; primary official NBB WVV 694"),
        ("bud_nuhc_div_2024", ENT, "2024", "17000000", "2024 dividend 17000000 comparative; tick1356; primary official NBB WVV 694"),
        ("bud_nuhc_omzet_2025", ENT, "2025", "2098031", "2025 omzet 2098031 (no 6.10 split); tick1356; primary official NBB WVV 70"),
        ("bud_nuhc_opsrev_2025", ENT, "2025", "2882711", "2025 bedrijfsopbrengsten 2882711 (omzet 2098031 + andere 305330 + nr 479350); tick1356; primary official NBB WVV 70/76A"),
        ("bud_nuhc_opscost_2025", ENT, "2025", "5646427", "2025 bedrijfskosten 5646427; tick1356; primary official NBB WVV 60/66A"),
        ("bud_nuhc_diensten_2025", ENT, "2025", "4038618", "2025 diensten 4038618; tick1356; primary official NBB WVV 61"),
        ("bud_nuhc_pers_2025", ENT, "2025", "1266380", "2025 personeelskosten 1266380 / avg VTE 9 / YE 11 koppen 10.3 VTE; tick1356; primary official NBB WVV 62 / 1023"),
        ("bud_nuhc_expl_2025", ENT, "2025", "-2763716", "2025 bedrijfsverlies -2763716; tick1356; primary official NBB WVV 9901"),
        ("bud_nuhc_fininc_2025", ENT, "2025", "29061372", "2025 financiele opbrengsten 29061372 (rec 23825735 FVA 21814747 + vlottend 2010988; nr 5235638); tick1356; primary official NBB WVV 75/76B"),
        ("bud_nuhc_fincost_2025", ENT, "2025", "23852", "2025 financiele kosten 23852 (rec 23852; nr 66B empty vs 1319912 prior); tick1356; primary official NBB WVV 65/66B"),
        ("bud_nuhc_nrfininc_2025", ENT, "2025", "5235638", "2025 niet-recurrente fin opbrengsten 5235638 WVV 76B (terugname WV FVA); tick1356; primary official NBB WVV"),
        ("bud_nuhc_tax_2025", ENT, "2025", "1471", "2025 belastingen 1471; tick1356; primary official NBB WVV 67/77"),
        ("bud_nuhc_comm_2025", ENT, "2025", "17739", "2025 commissaris ereloon Moore 17739 + andere controle 9028; tick1356; primary official NBB WVV 9505/95061"),
        ("bud_nuhc_bestuur_2025", ENT, "2025", "120149", "2025 bestuurdersbezoldiging 120149; tick1356; primary official NBB WVV 9503"),
        ("bud_nuhc_cons_assets_2025", ENT, "2025", "1180633427", "2025 geconsolideerde activa 1180633427.42 deposit 2026-00153822; tick1356; primary official NBB CONSO; not TE-additive"),
        ("bud_nuhc_cons_omzet_2025", ENT, "2025", "171643806", "2025 geconsolideerde omzet 171643805.98; tick1356; primary official NBB CONSO"),
        ("bud_nuhc_cons_pnl_2025", ENT, "2025", "17638162", "2025 geconsolideerde PnL 17638162.11 (cons winst 14925129.42); tick1356; primary official NBB CONSO"),
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
                "title": "Nuhma cv JR2025 leftover CV dual (assets 693.83m / pnl 26.27m / div 33.50m)",
                "entity_id": ENT,
                "beneficiary": "Nuhma cv / NUHMA AC / Limburg municipalities / Bionerga",
                "legal_basis": "WVV CV; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-06-01",
                "start_year": "2000",
                "end_year": "2025",
                "total_envelope_eur": "693832591",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover CV map VL klimaat-holding — per-vennoot 33.50m dividend / 58.53m FVA drop / AC dual",
                "cut_option": "Publish per-vennoot 33.50m dividend dual + composition of 58.53m FVA drop / 63.84m herwaardering-afboeking + AC/DC recon + official-site JR; do not recreate parallel Limburg climate-holding CV+NV shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1356; assets 693832591 pnl 26272333 div 33500606 fva drop 58533221; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Nuhma cv JR2025 leftover CV: assets 693.83m / pnl 26.27m / div 33.50m / FVA drop 58.53m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "33500606",
                "total_cost_eur": "693832591",
                "tco_notes": (
                    "Leftover dual klimaat-holding cv of mined Limburg cities + NUHMA AC/Bionerga/Limburg.net: "
                    "assets 693.83m DROP vs 755.82m / equity 662.79m DROP / pnl 26.27m JUMP vs 10.32m / "
                    "dividend 33.50m JUMP vs 17.00m / FVA drop 58.53m / herwaardering-afboeking 63.84m; "
                    "nuhma.be narrative 662.8m/26.3m MATCHES cv statutory not AC 607.10m/8.77m; "
                    "official NBB WVV live; do not treat 693.83m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Nuhma cv / NUHMA AC / Limburg municipalities / Bionerga",
                "stated_goal": "Local leftover CV map VL klimaat-holding — JR2025 live; dual dividend/FVA/AC FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 693.83m / pnl 26.27m / div 33.50m / FVA drop 58.53m; commissaris Moore",
                "absurdity_score": "7.4",
                "cost_score": "7.8",
                "difficulty": "3.0",
                "priority_index": "7.1",
                "cut_proposal": "Publish per-vennoot 33.50m dividend dual + 58.53m FVA drop composition + AC/DC recon + official-site JR; do not recreate parallel Limburg climate-holding CV+NV shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1356; leftover cv of mined Limburg + NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; FOI ready not sent; not TE-additive of 348bn",
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
                    "Per-vennoot 2025-2026 dual lines for inbreng 303515270 (18.195.138 aandelen op naam; "
                    "only Stad Hasselt 12.75pct / 2185631 Cat A+B disclosed) + composition of FVA drop "
                    "745315000 to 686781779 (verbonden 686144385 waarvan deeln 650466151 + vord 35678233; "
                    "herwaardering afgeboekt 63839699 / terugname WV 5235638 WVV 76B; which participation "
                    "NUHMA AC/DC/Nubema) + recon of cv statutory EV 662794232 / pnl 26272333 / div 33500606 "
                    "vs AC statutory EV 607097228 / pnl 8772737 / div 8325000 and deelnemingstabel AC "
                    "netto 5132062 vs AC statutory 8772737 + NUHMA DC BV 0697972606 (EV 31807278 / pnl "
                    "-1207764) + Nubema NV 0834086964 statutory + cons deposit 2026-00153822 "
                    "(assets 1180633427.42 / omzet 171643805.98 / pnl 17638162.11) machine-readable + "
                    "overige schulden 25502384 vs dividend 33500606 + 6.10 omzet split empty + AV "
                    "01.06.2026 minutes + commissaris Moore 17739 + official-site statutory JR PDF"
                ),
                "why_it_matters": (
                    "Leftover klimaat-holding CV shell of mined Limburg cities + NUHMA AC 1355 "
                    "+ Bionerga 1354 + Limburg.net 1353 (same zetel Herkenrodesingel 14; 100pct of AC): "
                    "693.83m assets / 33.50m dividend / 58.53m FVA drop vs AC 8.33m dividend / website "
                    "now matches cv not AC is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Nuhma cv / NUHMA AC NV / Limburg municipalities",
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
                    "tick1356 leftover CV of mined Limburg cities + NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (3.17MB 65p deposit 2026-00154816). "
                    "AGB MAC already mined 1270 — skipped. Westtoer already mined — skipped. "
                    "EcoWerf statutory CDN 2026-00256489 now downloads (928kB 64p) — leftover later. "
                    "IOK/IMOG/Haviland still 2024. Interleuven still 2024 balans. "
                    "POM Limburg glossy-only. Veneco/Leiedal glossy. NBB consult skipped. "
                    "Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1356",
        "title": "Nuhma cv JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Nuhma cv leftover klimaat-holding cooperative of mined Limburg cities + NUHMA AC/Bionerga/Limburg.net "
            "after honest hunt; KBO 0472.325.068 Actief; live JR2025 official NBB WVV VOL-inb PDF "
            "(3.17MB 65p deposit 2026-00154816 + commissaris Moore); "
            "sourced euros assets 693.833m / equity 662.794m / pnl 26.272m / div 33.501m / fva drop 58.533m; "
            "FOI ready per-vennoot/impairment/AC-recon/cons"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T01:25:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1356 Nuhma cv leftover CV residual; KBO 0472.325.068; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1357 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1357",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1356 done including Nuhma cv 1356 leftover klimaat-holding live NBB WVV / "
            "NUHMA AC NV 1355 leftover klimaat-holding live NBB WVV / "
            "Bionerga NV 1354 leftover waste-processing live NBB WVV / "
            "Limburg.net 1353 leftover IGS glossy-only FOI / IVBO 1352 leftover IGS live WVV / "
            "SOLVA 1351 leftover IGS live JR / Interwaas 1350 leftover IGS live WVV + every-10 / "
            "Aquaduin / IWVA ov 1349 leftover IGS live WVV / Creat Services dv 1348 leftover IGS live WVV / "
            "IVIO Izegem-Ommeland 1347 leftover IGS live JR operational / WVI West-Vlaanderen 1346 leftover IGS live WVV / "
            "IVVO Veurne-Ommeland 1345 leftover IGS live WVV / ILvA Land van Aalst 1344 leftover IGS live WVV / "
            "IVM Meetjesland 1343 leftover IGS live WVV / IDM Durme-Moervaart 1342 leftover IGS live WVV / "
            "IGEAN dienstverlening 1341 leftover IGS live WVV / EVA Limburg Sterk Merk 1340 leftover EVA live WVV + every-10); "
            "EcoWerf KBO 0862.492.920 leftover IGS Oost-Brabant — statutory NBB VOL-inb deposit 2026-00256489 now downloads (928kB 64p AV 24.06.2026) — TAKE if still unmined; "
            "NUHMA DC BV KBO 0697.972.606 leftover Nuhma dochter — take only if a statutory WVV PDF now downloads; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "Veneco glossy jaarverslag 2025 websingle — take only if a WVV/BBC PDF now downloads; "
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
            "skip already-mined Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
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
        "notes": "spawned tick1356 after Nuhma cv leftover CV live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1356", rq_new, rq_spawn)
    print("research_queue 1356", found, "spawned_1357", spawned)

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
                "last_unit_id": "rq_1356",
                "ticks_completed": "1356",
                "paused": "no",
                "notes": (
                    "tick1356 Nuhma cv leftover CV residual; KBO 0472.325.068; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 693.833m equity 662.794m pnl 26.272m div 33.501m fva drop 58.533m; "
                    "FOI ready per-vennoot/impairment/AC-recon; next rq_1357 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1356 - 2026-08-19 - rq_1356 Nuhma cv dual residual leftover
- Unit: Nuhma cv (Nutsbedrijven Houdstermaatschappij / leftover klimaat-holding cooperative / Limburg municipalities) of already-mined Limburg cities (Hasselt 12,75% / 2.185.631 Cat A+B disclosed; Genk / Tongeren-Borgloon / Houthalen-Helchteren / Bilzen-Hoeselt / Leopoldsburg / Nieuwerkerken / Gingelom / Pelt / Maasmechelen; Maaseik AGB already mined) + leftover NV NUHMA AC tick1355 (100% dochter; zelfde zetel; Nuhma cv is gedelegeerd bestuurder) + leftover NV Bionerga tick1354 + leftover IGS Limburg.net tick1353 after residual dual hunt (KBO **0472.325.068**; official nuhma.be is this cv; live NBB WVV VOL-inb deposit **2026-00154816** PDF 3.17MB / 65p; AV **01.06.2026**; neerlegging **08.06.2026**; commissaris Moore Audit / Jimmy Depré 05.05.2026 oordeel zonder voorbehoud). Leftover CV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last tick listed Nuhma cv as leftover later pending statutory WVV). Distinct from already-mined NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **07.07.2000**; statutaire naam NUTSBEDRIJVEN HOUDSTERMAATSCHAPPIJ / NUHMA since 28.06.2000; Coöperatieve vennootschap since 08.10.2024; zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; **1 VE**; aanbestedende overheid since 28.06.2000; btw since 01.01.2008; RSZ since 04.02.2008; jaarvergadering juni; 9 bestuurders; e-mail info@nuhma.be; tel 011 49 56 10; NACE 64.210. Hunt leftover AGB/zorg/EVA first: AGB MAC Mechelen 2025 BBC already mined tick1270 — skipped; SportAG Aalst / AGB Deinze / AGB Genk already mined — skipped; Westtoer APB already mined — skipped; EcoWerf leftover IGS statutory NBB VOL-inb deposit **2026-00256489** now downloads (928kB / 64p / AV 24.06.2026) — not taken once live Nuhma cv WVV extracted (leftover later); IOK/IMOG/Haviland still 2024; Interleuven 2025 jaarverslag InDesign embed only / balans still 2024; POM Limburg glossy-only — not taken; Veneco/Leiedal glossy-only; IVAREM activiteitenverslag glossy; IGEMO activiteitenverslag only; IVOO no public 2025 JR; IVAGO SSL EOF; MIWA flipbook; MIROM Cloudflare; De Schorre provincieantwerpen.be 403; APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas no fetchable PDF; Dommelhof leftover Limburg EVA KBO 0777.495.085 no JR2025 PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE no fetchable 2025 JR this tick. NUHMA DC BV 0697.972.606 leftover later. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345. Not every-10 (next 1360).
- EUR strong (primary official WVV VOL-inb + commissaris Moore oordeel zonder voorbehoud 05.05.2026): assets **693.832.591** (was 755.820.904); oprichting **16.714**; fixed **688.809.513**; MVA **2.027.735** (machines **60.707** + rollend **924.876** + overige **1.042.152**); FVA **686.781.779** DROP vs 745.315.000 (verbonden **686.144.385** waarvan deeln **650.466.151** + vord **35.678.233**; deelnemingsverhouding **637.394**); current **5.006.364** DROP vs 9.237.260; ST recv **660.311**; beleggingen **0** DROP vs 7.000.000; cash **3.949.440** JUMP vs 945.349; equity **662.794.232** DROP vs 730.495.885 (inbreng **303.515.270**; herwaardering **148.643.187** DROP vs 209.116.567; reserves **210.635.775**); schulden **31.038.359** (ST **27.046.058** waarvan overige **25.502.384**); ops rev **2.882.711**; omzet **2.098.031** (no 6.10 split); diensten **4.038.618**; pers **1.266.380**; avg VTE **9** / YE 11 koppen 10,3 VTE; expl **−2.763.716**; fin opbr **29.061.372** (FVA **21.814.747** + nr **5.235.638**); fin kosten **23.852**; PnL **+26.272.333** JUMP vs 10.315.591; dividend **33.500.606** JUMP vs 17.000.000; belasting **1.471**. Commissaris Moore **17.739** + andere controle **9.028**. Bestuurders **120.149**. Cons (deposit 2026-00153822): assets **1.180.633.427** / omzet **171.643.806** / PnL **17.638.162** / cons winst **14.925.129**. Website cv narrative EV 662,8m / winst 26,3m **matches** cv statutory — does **not** match AC 607,10m / 8,77m. Deelnemingen: NUHMA AC 100% EV 607.097.227 / netto 5.132.062 (vs AC statutory PnL 8.772.737); NUHMA DC BV 100% EV 31.807.278 / PnL −1.207.764; Nubema NV 100% EV 187.044 / PnL 9.438.
- CSVs: sources+4/entities+1/budgets+42/commitments+1/leaderboard+1 + FOI ready `gap_nuhc_pnl_26_27m_div_33_50m_fva_drop_l5` (not sent); rq_1356=done; spawn rq_1357; ticks=1356.
- Coverage: residual dual L5 (Nuhma cv leftover CV live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1357 residual dual L5 VL JR2025 hole_fill (prefer EcoWerf leftover IGS statutory NBB VOL-inb 2026-00256489 already downloaded this tick if still unmined; leftover NUHMA DC BV 0697.972.606 only if a statutory WVV PDF now downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; MIROM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1356 write done")


if __name__ == "__main__":
    main()

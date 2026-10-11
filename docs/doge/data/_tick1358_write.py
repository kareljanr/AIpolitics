# -*- coding: utf-8 -*-
"""Tick 1358 — leftover NUHMA DC BV JR2025 official NBB WVV euros.
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

TICK = "1358"
UTC = "2026-08-19T02:40:00Z"
ENT = "bv_nuhd"
HIER = "Vlaanderen>Limburg>BV>NUHMA_DC>KlimaatHolding"
GAP = "gap_nuhd_pnl_neg_1_21m_debt_20_51m_fva_impair_l5"
SRC = "src_nuhd_jr2025_nbb"
SRC2 = "src_nuhd_site"
SRC3 = "src_kbo_nuhd_0697972606"
SRC4 = "src_nuhd_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00124744.pdf"
SRC2_URL = "https://nuhma.be/duurzaam-rendement-in-2025/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0697972606"
SRC4_URL = "https://nuhma.be/contact/"
FOI_EMAIL = "info@nuhma.be"
FOI_POSTAL = "Herkenrodesingel 14 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_nuhd_pnl_neg_1_21m_debt_20_51m_fva_impair_l5.md"
COMM = "comm_nuhd_jr2025_pnl"
LB = "lb_nuhd_pnl_neg_1_21m_debt_20_51m_fva_impair"


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
                "title": "NUHMA DC BV jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00124744; AV 26.05.2026)",
                "url": SRC_URL,
                "publisher": "NUHMA DC BV / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1358; official NBB VOL-inb PDF 471kB 45p deposit 2026-00124744 neerlegging 27.05.2026; "
                    "leftover klimaat-holding BV 100pct of Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; parent cv deelnemingstabel EV 31807278 / PnL -1207764 MATCHES"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Nuhma official site 2025 kerncijfers (parent cv; NUHMA DC statutory not published separately)",
                "url": SRC2_URL,
                "publisher": "Nuhma cv / NUHMA DC",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1358; leftover BV of mined Limburg + Nuhma cv/AC/Bionerga/Limburg.net; "
                    "nuhma.be is Nuhma cv KBO 0472.325.068; narrative EV 662.8m / winst 26.3m is cv not DC; "
                    "jaarverslag page still 2020 PDF only; DC 0697.972.606 statutory only via NBB deposit"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO NUHMA DC 0697.972.606",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1358; KBO 0697.972.606 Actief / normale toestand since 15.06.2018; "
                    "statutaire naam NUHMA DC since 15.06.2018; BV since 27.07.2023; "
                    "zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; 1 VE; "
                    "btw since 01.10.2018; jaarvergadering mei; 14 functiehouders; NACE 64.210/70.200"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Nuhma FOI channel / official contact (parent; DC has no KBO email)",
                "url": SRC4_URL,
                "publisher": "NUHMA DC / Nuhma cv",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1358; FOI info@nuhma.be; 011 49 56 10; Herkenrodesingel 14 3500 Hasselt "
                    "(same zetel as Nuhma cv / NUHMA AC / Bionerga / Limburg.net); commissaris Moore Audit / Jimmy Depré"
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
                "name_nl": "NUHMA DC (leftover klimaat-holding BV Limburg / slimme diensten / Nuhma cv dochter)",
                "name_fr": "NUHMA DC (holding climat residuel Limbourg / services intelligents / filiale Nuhma sc)",
                "name_en": "NUHMA DC leftover Limburg climate-holding BV (smart-services daughter of Nuhma cv)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://nuhma.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1358 leftover residual klimaat-holding BV 100pct of Nuhma cv 1356 "
                    "+ NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353 (same zetel Herkenrodesingel 14); "
                    "KBO 0697.972.606 Actief since 15.06.2018; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 52.319m / equity 31.807m / pnl -1.208m / debt 20.512m / impair 6.018m; "
                    "FOI ready per-deelneming/intra-group-debt/FVA-mutation/site-JR"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_nuhd_assets_2025", ENT, "2025", "52319175", "2025 assets 52319175 VOL-inb 20/58; tick1358; primary official NBB WVV; commissaris 52319175"),
        ("bud_nuhd_assets_2024", ENT, "2024", "65080177", "2024 assets 65080177 comparative; tick1358; primary official NBB WVV 20/58"),
        ("bud_nuhd_pnl_2025", ENT, "2025", "-1207764", "2025 PnL 9904 -1207764; tick1358; primary official NBB WVV + commissaris Moore"),
        ("bud_nuhd_pnl_2024", ENT, "2024", "-1476276", "2024 PnL 9904 -1476276 comparative; tick1358; primary official NBB WVV"),
        ("bud_nuhd_fixed_2025", ENT, "2025", "50652986", "2025 vaste activa/FVA 50652986 DROP vs 63044651; tick1358; primary official NBB WVV 21/28"),
        ("bud_nuhd_current_2025", ENT, "2025", "1666189", "2025 vlottende activa 1666189 DROP vs 2035526; tick1358; primary official NBB WVV 29/58"),
        ("bud_nuhd_equity_2025", ENT, "2025", "31807278", "2025 eigen vermogen 31807278 JUMP vs 26264361; matches parent cv 6.5.1; tick1358; primary official NBB WVV 10/15"),
        ("bud_nuhd_equity_2024", ENT, "2024", "26264361", "2024 eigen vermogen 26264361 comparative; tick1358; primary official NBB WVV 10/15"),
        ("bud_nuhd_inbreng_2025", ENT, "2025", "31500000", "2025 inbreng beschikbaar 31500000 (3150000 aandelen op naam; 100pct Nuhma cv); tick1358; primary official NBB WVV 10/11"),
        ("bud_nuhd_herw_2025", ENT, "2025", "7004192", "2025 herwaardering 7004192 JUMP vs 253511 (andere FVA meerwaarden geboekt 6633965); tick1358; primary official NBB WVV 12"),
        ("bud_nuhd_herw_2024", ENT, "2024", "253511", "2024 herwaardering 253511 comparative; tick1358; primary official NBB WVV 12"),
        ("bud_nuhd_lossfwd_2025", ENT, "2025", "-6696914", "2025 overgedragen verlies -6696914 (was -5489151); tick1358; primary official NBB WVV 14"),
        ("bud_nuhd_fva_2025", ENT, "2025", "50652986", "2025 FVA 50652986 DROP vs 63044651; tick1358; primary official NBB WVV 28"),
        ("bud_nuhd_fva_2024", ENT, "2024", "63044651", "2024 FVA 63044651 comparative; tick1358; primary official NBB WVV 28"),
        ("bud_nuhd_fva_verb_2025", ENT, "2025", "26563918", "2025 FVA verbonden 26563918 (deeln 16633211 + vord 9930708); tick1358; primary official NBB WVV 280/1"),
        ("bud_nuhd_fva_deel_2025", ENT, "2025", "10562828", "2025 FVA deelnemingsverhouding 10562828 (deeln 5323307 + vord 5239521); tick1358; primary official NBB WVV 282/3"),
        ("bud_nuhd_fva_other_2025", ENT, "2025", "13526240", "2025 andere FVA 13526240 (aandelen 12781826 + vord 744413 DROP vs 20414825); tick1358; primary official NBB WVV 284/8"),
        ("bud_nuhd_ltrecv_2025", ENT, "2025", "1578109", "2025 LT overige vorderingen 1578109; tick1358; primary official NBB WVV 291"),
        ("bud_nuhd_strecv_2025", ENT, "2025", "420", "2025 ST overige vorderingen 420 DROP vs 176281; tick1358; primary official NBB WVV 41"),
        ("bud_nuhd_cash_2025", ENT, "2025", "87660", "2025 liquide middelen 87660 JUMP vs 20976; tick1358; primary official NBB WVV 54/58"),
        ("bud_nuhd_cash_2024", ENT, "2024", "20976", "2024 liquide middelen 20976 comparative; tick1358; primary official NBB WVV 54/58"),
        ("bud_nuhd_debt_2025", ENT, "2025", "20511898", "2025 schulden 20511898 DROP vs 38815817; tick1358; primary official NBB WVV 17/49"),
        ("bud_nuhd_debt_2024", ENT, "2024", "38815817", "2024 schulden 38815817 comparative; tick1358; primary official NBB WVV 17/49"),
        ("bud_nuhd_lt_2025", ENT, "2025", "19378846", "2025 LT schulden 19378846 all overige leningen 1-5y; tick1358; primary official NBB WVV 17/174/8852"),
        ("bud_nuhd_st_2025", ENT, "2025", "1133051", "2025 ST schulden 1133051 (trade 2829 + tax 412 + other 1129810); tick1358; primary official NBB WVV 42/48"),
        ("bud_nuhd_reldebt_2025", ENT, "2025", "20508656", "2025 schulden verbonden 20508656 (LT 19378846 + ST 1129810); tick1358; primary official NBB WVV 9351"),
        ("bud_nuhd_opscost_2025", ENT, "2025", "11796", "2025 bedrijfskosten 11796 (diensten 10195 + andere 1601); tick1358; primary official NBB WVV 60/66A"),
        ("bud_nuhd_diensten_2025", ENT, "2025", "10195", "2025 diensten 10195; tick1358; primary official NBB WVV 61"),
        ("bud_nuhd_expl_2025", ENT, "2025", "-11796", "2025 bedrijfsverlies -11796 (was -17307); tick1358; primary official NBB WVV 9901"),
        ("bud_nuhd_fininc_2025", ENT, "2025", "6472480", "2025 financiele opbrengsten 6472480 (rec FVA 1078331 + nr 5394149); tick1358; primary official NBB WVV 75/76B"),
        ("bud_nuhd_fincost_2025", ENT, "2025", "7668448", "2025 financiele kosten 7668448 (rec 1650848 waarvan schulden 1650723 + nr impair 6017599); tick1358; primary official NBB WVV 65/66B"),
        ("bud_nuhd_nrfininc_2025", ENT, "2025", "5394149", "2025 niet-recurrente fin opbrengsten 5394149 (terugname WV 4945594 + meerwaarde 448555); tick1358; primary official NBB WVV 76B"),
        ("bud_nuhd_nrimpair_2025", ENT, "2025", "6017599", "2025 niet-recurrente FVA waardeverminderingen 6017599 WVV 661; tick1358; primary official NBB WVV"),
        ("bud_nuhd_div_2025", ENT, "2025", "0", "2025 dividend 0 (694 empty; resultaat naar overgedragen verlies); tick1358; primary official NBB WVV 694"),
        ("bud_nuhd_comm_2025", ENT, "2025", "4100", "2025 commissaris ereloon Moore 4100; tick1358; primary official NBB WVV 9505"),
        ("bud_nuhd_patron_2025", ENT, "2025", "1400000", "2025 patronagebrief dochter 1400000 (waarderingsregels); tick1358; primary official NBB WVV 6.19"),
        ("bud_nuhd_subloan_2025", ENT, "2025", "1555000", "2025 achtergestelde leningen dochter 1555000 (waarderingsregels); tick1358; primary official NBB WVV 6.19"),
        ("bud_nuhd_cipal_pnl_2025", ENT, "2025", "101449266", "2025 Cipal NV 0442802030 10pct PnL 101449266 / EV 62689280 (deelnemingstabel; not DC statutory); tick1358; primary official NBB WVV 6.5.1; not TE-additive"),
        ("bud_nuhd_nuhmeris_ev_2025", ENT, "2025", "13531710", "2025 Nuhmeris NV 0560976140 100pct EV 13531710 / PnL -510182; tick1358; primary official NBB WVV 6.5.1; not TE-additive"),
        ("bud_nuhd_slim_pnl_2025", ENT, "2025", "-1355216", "2025 S-lim CV 0679631191 49.99pct PnL -1355216 / EV 2599382; tick1358; primary official NBB WVV 6.5.1; not TE-additive"),
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
                "title": "NUHMA DC BV JR2025 leftover BV dual (assets 52.32m / pnl -1.21m / debt 20.51m / impair 6.02m)",
                "entity_id": ENT,
                "beneficiary": "NUHMA DC / Nuhma cv / Limburg municipalities / slimme-diensten participaties",
                "legal_basis": "WVV BV; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-05-26",
                "start_year": "2018",
                "end_year": "2025",
                "total_envelope_eur": "52319175",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover BV map VL klimaat-holding slimme diensten — per-deelneming 6.02m impair / 20.51m intra-group debt",
                "cut_option": "Publish per-deelneming book-vs-EV + intra-group 20.51m debt counterparties + -22.08m other-FVA mutation + official-site JR; do not recreate parallel Limburg climate-holding CV+NV+BV shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1358; assets 52319175 pnl -1207764 debt 20511898 impair 6017599; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "NUHMA DC BV JR2025 leftover BV: assets 52.32m / pnl -1.21m / debt 20.51m / FVA impair 6.02m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "6017599",
                "total_cost_eur": "52319175",
                "tco_notes": (
                    "Leftover dual klimaat-holding BV 100pct of Nuhma cv of mined Limburg cities + AC/Bionerga/Limburg.net: "
                    "assets 52.32m DROP vs 65.08m / equity 31.81m JUMP / pnl -1.21m / "
                    "debt 20.51m DROP vs 38.82m (almost all related-party) / FVA impair 6.02m vs reverse 4.95m; "
                    "omzet empty / pers 0; parent cv 6.5.1 MATCHES DC statutory; "
                    "official NBB WVV live / site statutory unpublished; do not treat 52.32m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "NUHMA DC / Nuhma cv / Limburg municipalities / slimme-diensten participaties",
                "stated_goal": "Local leftover BV map VL klimaat-holding — JR2025 live; dual impair/debt/deelneming FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 52.32m / pnl -1.21m / debt 20.51m / impair 6.02m; commissaris Moore",
                "absurdity_score": "7.3",
                "cost_score": "6.8",
                "difficulty": "3.0",
                "priority_index": "6.7",
                "cut_proposal": "Publish per-deelneming book-vs-EV + 20.51m intra-group debt counterparties + -22.08m other-FVA mutation + official-site JR; do not recreate parallel Limburg climate-holding CV+NV+BV shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1358; leftover BV of mined Limburg + Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; FOI ready not sent; not TE-additive of 348bn",
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
                    "Per-deelneming 2025-2026 book-vs-EV for the 9 WVV 6.5.1 names (Campus Energyville 21.83pct / "
                    "Cipal 10pct PnL 101449266 / Fairville 33.33pct / Herkenrode RE 100pct / Immo Soltech 33.33pct 2024 / "
                    "MyCSN 90pct / Nuhmeris 100pct EV 13531710 / S-lim 49.99pct PnL -1355216 / Soltech 16.67pct 2024) "
                    "+ split of FVA verbonden 26563918 / deelnemingsverhouding 10562828 / andere 13526240 "
                    "+ intra-group debt counterparties for 20508656 (LT 19378846 + ST 1129810) of total debt 20511898 "
                    "and interest 1650723 + other-FVA vorderingen mutation 20414825 to 744413 (overige -22077913) "
                    "+ impair 6017599 vs reverse 4945594 / herwaardering geboekt 6633965 composition "
                    "+ patronage 1400000 + achtergesteld 1555000 which daughter + continuity at lossfwd -6696914 "
                    "+ AV 26.05.2026 minutes + commissaris Moore 4100 + official-site statutory JR PDF of DC "
                    "+ 6.15 related-party refusal (no wettelijk kader)"
                ),
                "why_it_matters": (
                    "Leftover klimaat-holding BV shell 100pct of Nuhma cv of mined Limburg cities + NUHMA AC 1355 "
                    "+ Bionerga 1354 + Limburg.net 1353 (same zetel Herkenrodesingel 14): "
                    "52.32m assets / 0 omzet / 0 VTE / 20.51m intra-group debt / 6.02m FVA impair / third-year "
                    "loss -1.21m next to Cipal 10pct +101.45m is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "NUHMA DC BV / Nuhma cv / Limburg municipalities",
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
                    "tick1358 leftover BV of mined Limburg cities + Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (471kB 45p deposit 2026-00124744). "
                    "AGB MAC already mined 1270 — skipped. Westtoer already mined — skipped. "
                    "EcoWerf already mined 1357 — skipped. "
                    "IOK/IMOG/Haviland still 2024. Interleuven still 2024 balans. "
                    "POM Limburg glossy-only. Veneco/Leiedal glossy. NBB consult skipped. "
                    "Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1358",
        "title": "NUHMA DC BV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: NUHMA DC leftover klimaat-holding BV 100pct of Nuhma cv of mined Limburg cities + AC/Bionerga/Limburg.net "
            "after honest hunt; KBO 0697.972.606 Actief; live JR2025 official NBB WVV VOL-inb PDF "
            "(471kB 45p deposit 2026-00124744 + commissaris Moore); "
            "sourced euros assets 52.319m / equity 31.807m / pnl -1.208m / debt 20.512m / impair 6.018m; "
            "FOI ready per-deelneming/intra-group-debt/FVA-mutation/site-JR"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T02:15:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1358 NUHMA DC leftover BV residual; KBO 0697.972.606; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1359 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1359",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1358 done including NUHMA DC BV 1358 leftover klimaat-holding live NBB WVV / "
            "EcoWerf 1357 leftover IGS live NBB WVV / "
            "Nuhma cv 1356 leftover klimaat-holding live NBB WVV / "
            "NUHMA AC NV 1355 leftover klimaat-holding live NBB WVV / "
            "Bionerga NV 1354 leftover waste-processing live NBB WVV / "
            "Limburg.net 1353 leftover IGS glossy-only FOI / IVBO 1352 leftover IGS live WVV / "
            "SOLVA 1351 leftover IGS live JR / Interwaas 1350 leftover IGS live WVV + every-10 / "
            "Aquaduin / IWVA ov 1349 leftover IGS live WVV / Creat Services dv 1348 leftover IGS live WVV / "
            "IVIO Izegem-Ommeland 1347 leftover IGS live JR operational / WVI West-Vlaanderen 1346 leftover IGS live WVV / "
            "IVVO Veurne-Ommeland 1345 leftover IGS live WVV / ILvA Land van Aalst 1344 leftover IGS live WVV / "
            "IVM Meetjesland 1343 leftover IGS live WVV / IDM Durme-Moervaart 1342 leftover IGS live WVV / "
            "IGEAN dienstverlening 1341 leftover IGS live WVV / EVA Limburg Sterk Merk 1340 leftover EVA live WVV + every-10); "
            "Nubema NV KBO 0834.086.964 leftover Nuhma dochter — take only if a statutory WVV PDF now downloads; "
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
            "skip already-mined NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
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
        "notes": "spawned tick1358 after NUHMA DC leftover BV live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1358", rq_new, rq_spawn)
    print("research_queue 1358", found, "spawned_1359", spawned)

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
                "last_unit_id": "rq_1358",
                "ticks_completed": "1358",
                "paused": "no",
                "notes": (
                    "tick1358 NUHMA DC leftover BV residual; KBO 0697.972.606; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 52.319m equity 31.807m pnl -1.208m debt 20.512m impair 6.018m; "
                    "FOI ready per-deelneming/intra-group-debt/FVA-mutation; next rq_1359 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1358 - 2026-08-19 - rq_1358 NUHMA DC dual residual leftover
- Unit: NUHMA DC BV (leftover klimaat-holding BV / slimme diensten / 100% dochter Nuhma cv) of already-mined Limburg cities via Nuhma cv tick1356 (Hasselt / Genk / Tongeren-Borgloon / Houthalen-Helchteren / Bilzen-Hoeselt / Leopoldsburg / Nieuwerkerken / Gingelom / Pelt / Maasmechelen) + leftover NV NUHMA AC tick1355 + leftover NV Bionerga tick1354 + leftover IGS Limburg.net tick1353 after residual dual hunt (KBO **0697.972.606**; official nuhma.be is the parent cv — DC statutory unpublished on site; live NBB WVV VOL-inb deposit **2026-00124744** PDF 471kB / 45p; AV **26.05.2026**; neerlegging header **27.05.2026**; commissaris Moore Audit / Jimmy Depré oordeel zonder voorbehoud). Leftover BV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last ticks listed NUHMA DC as leftover later pending statutory WVV). Distinct from already-mined EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **15.06.2018**; statutaire naam NUHMA DC since 15.06.2018; Besloten Vennootschap since 27.07.2023; zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; **1 VE**; btw since 01.10.2018; jaarvergadering mei; 14 functiehouders; Nuhma cv + Nubema NV bestuurders / Nuhma cv gedelegeerd bestuurder since 26.11.2025; e-mail via parent info@nuhma.be; tel 011 49 56 10; NACE 64.210 / 70.200. Hunt leftover AGB/zorg/EVA first: AGB MAC Mechelen 2025 BBC already mined tick1270 — skipped; SportAG Aalst / AGB Deinze / AGB Genk already mined — skipped; Westtoer APB already mined — skipped; EcoWerf already mined 1357 — skipped; NUHMA DC statutory CDN still live this tick (HTTP 200 / 471480 / 45p) — taken. IOK/IMOG/Haviland still 2024; Interleuven 2025 jaarverslag InDesign embed only / balans still 2024; POM Limburg glossy-only — not taken; Veneco/Leiedal glossy-only; IVAREM activiteitenverslag glossy; IGEMO activiteitenverslag only; IVOO no public 2025 JR; IVAGO SSL EOF; MIWA flipbook; MIROM Cloudflare; De Schorre provincieantwerpen.be 403; APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas no fetchable PDF; Dommelhof leftover Limburg EVA KBO 0777.495.085 no JR2025 PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE no fetchable 2025 JR this tick. Nubema NV 0834.086.964 leftover later. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345. Not every-10 (next 1360).
- EUR strong (primary official WVV VOL-inb + commissaris Moore oordeel zonder voorbehoud): assets **52.319.175** (was 65.080.177); fixed/FVA **50.652.986** DROP vs 63.044.651 (verbonden **26.563.918** waarvan deeln **16.633.211** + vord **9.930.708**; deelnemingsverhouding **10.562.828** waarvan deeln **5.323.307** + vord **5.239.521**; andere **13.526.240** waarvan aandelen **12.781.826** + vord **744.413** DROP vs 20.414.825 via overige mutaties **−22.077.913**); current **1.666.189**; LT recv **1.578.109**; ST recv **420**; cash **87.660** JUMP vs 20.976; equity **31.807.278** JUMP vs 26.264.361 (inbreng **31.500.000** / 3.150.000 aandelen 100% Nuhma cv; herwaardering **7.004.192** JUMP vs 253.511; overgedragen verlies **−6.696.914**); schulden **20.511.898** DROP vs 38.815.817 (LT **19.378.846** overige leningen 1–5j; ST **1.133.051**); verbonden schulden **20.508.656**; omzet **empty** / pers **0** / VTE **0**; diensten **10.195**; expl **−11.796**; fin opbr **6.472.480** (rec FVA **1.078.331** + nr **5.394.149** waarvan terugname WV **4.945.594** + meerwaarde **448.555**); fin kosten **7.668.448** (rec schulden **1.650.723** + nr impair **6.017.599**); PnL **−1.207.764** (was −1.476.276); dividend **0**. Commissaris Moore **4.100**. Patronage dochter **1.400.000**; achtergesteld dochter **1.555.000**. Parent cv 6.5.1 EV 31.807.278 / PnL −1.207.764 **matches** DC statutory. Deelnemingen: Campus Energyville 21,83% EV 23.054.534 / PnL −238.266; Cipal 10% EV 62.689.280 / PnL **+101.449.266**; Fairville 33,33% EV −77.614 / PnL −157.754; Herkenrode RE 100% EV 131.842 / PnL −386.604; Immo Soltech 33,33% (2024) EV 14.766 / PnL −181.485; MyCSN 90% EV 1.855.808 / PnL −455.887; Nuhmeris 100% EV 13.531.710 / PnL −510.182; S-lim 49,99% EV 2.599.382 / PnL −1.355.216; Soltech 16,67% (2024) EV 1.390.078 / PnL −1.845.317.
- CSVs: sources+4/entities+1/budgets+40/commitments+1/leaderboard+1 + FOI ready `gap_nuhd_pnl_neg_1_21m_debt_20_51m_fva_impair_l5` (not sent); rq_1358=done; spawn rq_1359; ticks=1358.
- Coverage: residual dual L5 (NUHMA DC leftover BV live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1359 residual dual L5 VL JR2025 hole_fill (prefer leftover Nubema NV 0834.086.964 only if a statutory WVV PDF now downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; MIROM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1358 write done")


if __name__ == "__main__":
    main()

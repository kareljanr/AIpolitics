# -*- coding: utf-8 -*-
"""Tick 1391 — leftover Fluvius OV JR2025 official NBB WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1391"
UTC = "2026-08-19T03:35:00Z"
ENT = "igs_flov"
HIER = "Vlaanderen>Limburg>IGS>FluviusOV"
GAP = "gap_flov_omzet_97_35m_pers_97_58m_pens_151_26m_l5"
SRC = "src_flov_jr2025_nbb"
SRC2 = "src_flov_site"
SRC3 = "src_kbo_flov_0201311226"
SRC4 = "src_flov_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00165875.pdf"
SRC2_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0201311226"
SRC4_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders"
FOI_EMAIL = ""
FOI_POSTAL = "Trichterheideweg 8 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_flov_omzet_97_35m_pers_97_58m_pens_151_26m_l5.md"
COMM = "comm_flov_jr2025_pnl"
LB = "lb_flov_omzet_97_35m_pers_97_58m_pens_151_26m"

VENNOTEN = (
    "Fluvius Antwerpen + Fluvius Halle-Vilvoorde + Fluvius Imewo + "
    "Fluvius Kempen + Fluvius Limburg + Fluvius Midden-Vlaanderen + "
    "Fluvius West + Fluvius Zenne-Dijle (ex-Infrax/ex-Integan statutair personeel; "
    "secondment naar Fluvius System Operator)"
)


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


BUDGETS = [
    ("bud_flov_assets_2025", "2025", "27892216", "2025 assets 27892216 VOL-inb 20/58; tick1391; primary official NBB WVV"),
    ("bud_flov_assets_2024", "2024", "30297051", "2024 assets 30297051 comparative; tick1391; primary official NBB WVV 20/58"),
    ("bud_flov_fixed_2025", "2025", "491180", "2025 vaste activa 491180 vs 491180; tick1391; primary official NBB WVV 21/28"),
    ("bud_flov_mva_2025", "2025", "235499", "2025 MVA 235499 terreinen/gebouwen (0 aanschaf); tick1391; primary official NBB WVV 22/27"),
    ("bud_flov_buildings_2025", "2025", "235499", "2025 terreinen/gebouwen 235499; tick1391; primary official NBB WVV 22"),
    ("bud_flov_fva_2025", "2025", "255681", "2025 FVA 255681 andere aandelen 284; tick1391; primary official NBB WVV 28"),
    ("bud_flov_fva_oth_2025", "2025", "255681", "2025 FVA andere aandelen 255681 Ethias+Poolstok; tick1391; primary official NBB WVV 284"),
    ("bud_flov_current_2025", "2025", "27401036", "2025 vlottend 27401036 vs 29805871; tick1391; primary official NBB WVV 29/58"),
    ("bud_flov_strecv_2025", "2025", "24254648", "2025 ST vorderingen 24254648 vs 26501931; tick1391; primary official NBB WVV 40/41"),
    ("bud_flov_trade_2025", "2025", "11118804", "2025 handelsvorderingen 11118804 JUMP vs 398233; tick1391; primary official NBB WVV 40"),
    ("bud_flov_othrecv_2025", "2025", "13135845", "2025 overige ST vorderingen 13135845 vs 26103698; tick1391; primary official NBB WVV 41"),
    ("bud_flov_relrecv_2025", "2025", "23547194", "2025 related-party ST vorderingen 23547194 vs 25946161; tick1391; primary official NBB WVV 6.15 9292"),
    ("bud_flov_cash_2025", "2025", "242", "2025 liquide middelen 242 vs 448; tick1391; primary official NBB WVV 54/58"),
    ("bud_flov_prepaid_2025", "2025", "3146145", "2025 overlopend actief 3146145 (pers 2749732 + diensten 396414); tick1391; primary official NBB WVV 490/1"),
    ("bud_flov_equity_2025", "2025", "26642", "2025 EV 26642 vs 26642; tick1391; primary official NBB WVV 10/15"),
    ("bud_flov_inbreng_2025", "2025", "24393", "2025 inbreng beschikbaar 24393 / 984 aandelen; tick1391; primary official NBB WVV 10/11"),
    ("bud_flov_reserves_2025", "2025", "2248", "2025 beschikbare reserves 2248; tick1391; primary official NBB WVV 13"),
    ("bud_flov_debt_2025", "2025", "27865574", "2025 schulden 27865574 vs 30270409; tick1391; primary official NBB WVV 17/49"),
    ("bud_flov_debt_2024", "2024", "30270409", "2024 schulden 30270409 comparative; tick1391; primary official NBB WVV 17/49"),
    ("bud_flov_st_2025", "2025", "27865574", "2025 ST schulden 27865574 (no LT); tick1391; primary official NBB WVV 42/48"),
    ("bud_flov_sttrade_2025", "2025", "958474", "2025 leveranciers 958474 vs 925530; tick1391; primary official NBB WVV 440/4"),
    ("bud_flov_sttax_2025", "2025", "5180158", "2025 belastingschulden 5180158 vs 5478962; tick1391; primary official NBB WVV 450/3"),
    ("bud_flov_stsoc_2025", "2025", "19877282", "2025 bezoldigingen/sociale lasten 19877282 vs 21882356; tick1391; primary official NBB WVV 454/9"),
    ("bud_flov_stother_2025", "2025", "1849659", "2025 overige ST schulden 1849659 vs 1983561; tick1391; primary official NBB WVV 47/48"),
    ("bud_flov_opsinc_2025", "2025", "122078961", "2025 bedrijfsopbrengsten 122078961 vs 126440657; tick1391; primary official NBB WVV 70/76A"),
    ("bud_flov_omzet_2025", "2025", "97349085", "2025 omzet 97349085 vs 102061287; 6.10 category/geo unpublished; tick1391; primary official NBB WVV 70"),
    ("bud_flov_omzet_2024", "2024", "102061287", "2024 omzet 102061287 comparative; tick1391; primary official NBB WVV 70"),
    ("bud_flov_othops_2025", "2025", "1900470", "2025 andere bedrijfsopbrengsten 1900470 vs 1549962; 740 empty; tick1391; primary official NBB WVV 74"),
    ("bud_flov_nonrec_2025", "2025", "22829407", "2025 niet-recurrent 76A=66A 22829407 both years; tick1391; primary official NBB WVV 76A"),
    ("bud_flov_opscost_2025", "2025", "121572751", "2025 bedrijfskosten 121572751 vs 125353929; tick1391; primary official NBB WVV 60/66A"),
    ("bud_flov_diensten_2025", "2025", "1156794", "2025 diensten 1156794 vs 874386; tick1391; primary official NBB WVV 61"),
    ("bud_flov_diensten_2024", "2024", "874386", "2024 diensten 874386 comparative; tick1391; primary official NBB WVV 61"),
    ("bud_flov_pers_2025", "2025", "97583389", "2025 pers 97583389 vs 101646653 / 573.6 VTE; tick1391; primary official NBB WVV 62"),
    ("bud_flov_pers_2024", "2024", "101646653", "2024 pers 101646653 / 615.4 VTE comparative; tick1391; primary official NBB WVV 62"),
    ("bud_flov_othcost_2025", "2025", "3161", "2025 andere bedrijfskosten 3161 vs 3483; tick1391; primary official NBB WVV 640/8"),
    ("bud_flov_expl_2025", "2025", "506211", "2025 expl +506211 vs +1086728; tick1391; primary official NBB WVV 9901"),
    ("bud_flov_expl_2024", "2024", "1086728", "2024 expl +1086728 comparative; tick1391; primary official NBB WVV 9901"),
    ("bud_flov_fininc_2025", "2025", "189852", "2025 financiele opbrengsten 189852 vs 178152; tick1391; primary official NBB WVV 75/76B"),
    ("bud_flov_fincost_2025", "2025", "36950", "2025 financiele kosten 36950 vs 34802; tick1391; primary official NBB WVV 65/66B"),
    ("bud_flov_pretax_2025", "2025", "659112", "2025 winst voor belasting 659112 vs 1230078; tick1391; primary official NBB WVV 9903"),
    ("bud_flov_tax_2025", "2025", "659112", "2025 belasting 659112 (670/3 1056359 - 77 397247); tick1391; primary official NBB WVV 67/77"),
    ("bud_flov_pnl_2025", "2025", "0", "2025 PnL 0 vs 0 (full tax wipe); tick1391; primary official NBB WVV 9904"),
    ("bud_flov_pnl_2024", "2024", "0", "2024 PnL 0 comparative; tick1391; primary official NBB WVV 9904"),
    ("bud_flov_div_2025", "2025", "0", "2025 dividend 694 empty; tick1391; primary official NBB WVV 694"),
    ("bud_flov_pens_off_2025", "2025", "151260000", "2025 off-balance IAS19 pensioen/personeel 151.26m (6.20); tick1391; primary official NBB WVV 6.20"),
    ("bud_flov_comm_2025", "2025", "16634", "2025 commissaris 9505 16634; tick1391; primary official NBB WVV 9505"),
    ("bud_flov_board_2025", "2025", "17439", "2025 bestuurders 9503 17439; tick1391; primary official NBB WVV 9503"),
    ("bud_flov_train_2025", "2025", "443935", "2025 formele opleiding 443935 (357048M+86887V); tick1391; primary official NBB WVV 5803/5813"),
]


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "Fluvius OV (Fluvius Opdrachthoudende Vereniging) jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00165875; AV 03.06.2026)",
                "url": SRC_URL,
                "publisher": "Fluvius OV / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1391; official NBB VOL-inb PDF 4.17MB 40p deposit 2026-00165875 header 08.06.2026 created 08.06.2026; "
                    "leftover Fluvius personnel OV / statutair personeel ex-Infrax/ex-Integan; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; Staatsbladmonitor table euros not used (2025 row empty); "
                    "commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / "
                    "Paul Eelen + Line Vyvey oordeel zonder voorbehoud signed 26.03.2026; "
                    "omzet 6.10 category/geo unpublished; 740 empty; 694 empty; 6.15 verbonden empty"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Fluvius OV official governance (leftover personnel OV; aandeelhouders 9 DNB; AV 03.06.2026)",
                "url": SRC2_URL,
                "publisher": "Fluvius / Fluvius OV",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1391; leftover personnel OV of ex-Infrax/ex-Integan statutory staff; "
                    "over.fluvius.be lists Fluvius OV as the secondment vehicle; "
                    "AV presentatie https://over.fluvius.be/sites/fluvius/files/2026-06/2026-06-03-presentatie-av-fluvius-ov.pdf; "
                    "statutory 2025 balans is the NBB CDN deposit"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Fluvius / Fluvius OV 0201.311.226",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1391; KBO 0201.311.226 Actief / normale toestand since 01.01.1968; "
                    "statutaire naam FLUVIUS since 20.06.2018; "
                    "Opdrachthoudende vereniging (Vlaams Gewest) since 02.06.2003; "
                    "zetel Trichterheideweg 8 3500 Hasselt since 01.01.2025; 1 VE; "
                    "no KBO email/web/tel; btw since 01.01.1971; RSZ since 01.01.2022; NACE 35.140/35.220; "
                    "aanbestedende overheid since 01.01.1968"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Fluvius OV FOI channel / official governance + secretariaat (KBO no email)",
                "url": SRC4_URL,
                "publisher": "Fluvius OV",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1391; KBO no email/web/tel; zetel Trichterheideweg 8 3500 Hasselt; "
                    "secretariaat Brusselsesteenweg 199 9090 Merelbeke-Melle; "
                    "no dedicated openbaarheid mailbox found on official pages this tick"
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
                "name_nl": "Fluvius OV (Fluvius Opdrachthoudende Vereniging; leftover IGS statutair personeel)",
                "name_fr": "Fluvius OV (association missionnee; IGS residuel personnel statutaire)",
                "name_en": "Fluvius OV leftover IGS statutory-staff secondment vehicle",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1391 leftover residual Fluvius personnel OV; "
                    "KBO 0201.311.226 Actief since 01.01.1968; naam FLUVIUS since 20.06.2018; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 27892216 omzet 97349085 pers 97583389 diensten 1156794 debt 27865574 pnl 0 equity 26642 pens 151260000; "
                    "FOI ready omzet geo empty / 97.58m 62 / 151.26m off-balance pens / 23.55m related recv / 1.16m 61; "
                    "distinct from already-mined Fluvius EG group entity fluvius and Riobra 1390 / Zenne-Dijle 1389 / Limburg 1388 / Halle-Vilvoorde 1387 / Antwerpen 1386 / West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382"
                ),
            },
        ],
    )
    print("entities", n)

    n = append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": bid,
                "entity_id": ENT,
                "year": year,
                "amount_eur": amt,
                "amount_min_eur": "",
                "amount_max_eur": "",
                "basis": "executed",
                "source_id": SRC,
                "confidence": "strong",
                "notes": notes,
            }
            for bid, year, amt, notes in BUDGETS
        ],
    )
    print("budgets", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": "Fluvius OV JR2025 leftover IGS dual (assets 27.89m / omzet 97.35m / pers 97.58m / off-balance pens 151.26m / dividend 0)",
                "entity_id": ENT,
                "beneficiary": "Fluvius OV / " + VENNOTEN,
                "legal_basis": "WVV OV; Decreet Lokaal Bestuur; NBB neerlegging",
                "decision_date": "2026-06-03",
                "start_year": "1968",
                "end_year": "",
                "total_envelope_eur": "151260000",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL personnel OV — 97.35m omzet (geo empty) / 97.58m pers / 151.26m off-balance pens / 0 dividend",
                "cut_option": "Publish unpublished omzet geo + 22.83m non-recurrent + 97.58m 62 FSO pass-through + 151.26m off-balance pens + 23.55m related ST vorderingen; do not keep personnel OV as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1391; assets 27892216 omzet 97349085 pers 97583389 diensten 1156794 debt 27865574 pnl 0 equity 26642 pens 151260000; FOI ready not sent; not TE-additive of 348bn; double_count vs Fluvius EG possible",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Fluvius OV JR2025 leftover IGS: assets 27.89m / omzet 97.35m / pers 97.58m / 573.6 VTE / off-balance pens 151.26m / PnL 0",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "97583389",
                "total_cost_eur": "151260000",
                "tco_notes": (
                    "Leftover dual IGS personnel OV (statutair ex-Infrax/ex-Integan): "
                    "assets 27.89m / equity 26.6k / pnl 0 / omzet 97.35m (geo empty) / "
                    "pers 97.58m / 573.6 VTE / diensten 1.16m / debt 27.87m / off-balance pens 151.26m / cash 242; "
                    "official NBB WVV live; do not treat 151.26m as TE-additive of 348bn; double_count vs Fluvius EG / DNB possible"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Fluvius OV / " + VENNOTEN,
                "stated_goal": "Local leftover IGS map VL personnel OV — JR2025 live; dual omzet-geo/pers/pens FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 27.89m / omzet 97.35m / pers 97.58m / 573.6 VTE / off-balance pens 151.26m / pnl 0",
                "absurdity_score": "7.0",
                "cost_score": "5.5",
                "difficulty": "3.0",
                "priority_index": "6.2",
                "cut_proposal": "Publish unpublished omzet geo + 22.83m non-recurrent + 97.58m 62 FSO pass-through + 151.26m off-balance pens + 23.55m related ST vorderingen; do not keep personnel OV as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1391; leftover Fluvius personnel OV; FOI ready not sent; not TE-additive of 348bn; distinct from Fluvius EG and Riobra 1390 / Zenne-Dijle 1389 / Limburg 1388 / Halle-Vilvoorde 1387 / Antwerpen 1386 / West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382",
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
                    "omzet 97349085 vs 102061287 (WVV 70; 6.10 category/geo unpublished) per FSO/DNB unpublished "
                    "+ andere bedrijfsopbrengsten 1900470 (WVV 74; 740 empty) "
                    "+ niet-recurrent 22829407 (76A=66A both years) unpublished "
                    "+ diensten 1156794 vs 874386 (WVV 61; no split) "
                    "+ pers 97583389 / 573.6 VTE / YE 582 / 0 in / 36 FTE out "
                    "+ off-balance IAS19 pensioen 151260000 (6.20; 8 DNB alloc) cash-out unpublished "
                    "+ related-party ST vorderingen 23547194 vs 25946161 unpublished "
                    "+ schulden 27865574 (all ST; soc 19877282) counterparties unpublished "
                    "+ dividend 694 empty + VOL-inb 6.10 omzet split not filed"
                ),
                "why_it_matters": (
                    "Leftover Fluvius personnel OV of ex-Infrax/ex-Integan statutory staff "
                    "(distinct from Fluvius EG and from the 9 DNB holdings mined 1382-1390): "
                    "27.89m assets / 97.35m omzet / 97.58m pers / 151.26m off-balance pens / 0 PnL / "
                    "FSO secondment shell "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Fluvius OV / Raad van Bestuur / Wim Dries / Mieke Bailleul-Vanrobaeys",
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
                    "tick1391 leftover Fluvius personnel OV after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (4.17MB 40p deposit 2026-00165875). "
                    "Nine DNB holdings already mined 1382-1390 — skipped. "
                    "Leftover AGB/zorg/EVA/APB of mined cities next if a 2025 PDF downloads. "
                    "Dommelhof leftover Limburg EVA 0777.495.085 not re-probed once live Fluvius OV extracted. "
                    "Otary RS Nuhma-adjacent fallback not taken. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1391",
        "title": "Fluvius OV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Fluvius OV leftover IGS personnel OV after honest hunt; "
            "KBO 0201.311.226 Actief; live JR2025 official NBB WVV VOL-inb PDF (4.17MB 40p deposit 2026-00165875; commissaris EY); "
            "sourced euros assets 27892216 / omzet 97349085 / pers 97583389 / diensten 1156794 / debt 27865574 / pnl 0 / pens 151260000; "
            "FOI ready omzet geo empty / 97.58m 62 / 151.26m off-balance pens / 23.55m related recv / 1.16m 61"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T05:50:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1391 Fluvius OV leftover IGS personnel residual; KBO 0201.311.226; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1392 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1392",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1391 done including Fluvius OV 1391 leftover personnel OV live NBB WVV / "
            "Fluvius Riobra 1390 leftover sewerage IGS live NBB WVV + every-10 / "
            "Fluvius Zenne-Dijle 1389 leftover energy IGS live NBB WVV / "
            "Fluvius Limburg 1388 leftover energy IGS live NBB WVV / "
            "Fluvius Halle-Vilvoorde 1387 leftover energy IGS live NBB WVV / "
            "Fluvius Antwerpen 1386 leftover energy IGS live NBB WVV / "
            "Fluvius West 1385 leftover energy IGS live NBB WVV / "
            "Fluvius Kempen 1384 leftover energy IGS live NBB WVV / "
            "Fluvius Imewo 1383 leftover energy IGS live NBB WVV / "
            "INTERGEM / Fluvius Midden-Vlaanderen 1382 leftover energy IGS live NBB WVV); "
            "leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; "
            "leftover IGS IVLA 0228.618.706 CDN 2026-00281193 / HAVICREM 0860.572.419 CDN 2026-00363711 now live — leftover next; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
            "skip already-mined Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1391 after Fluvius OV leftover personnel OV live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1391", rq_new, rq_spawn)
    print("research_queue 1391", found, "spawned_1392", spawned)

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
                "last_unit_id": "rq_1391",
                "ticks_completed": "1391",
                "paused": "no",
                "notes": (
                    "tick1391 Fluvius OV leftover IGS personnel residual; KBO 0201.311.226; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 27892216 omzet 97349085 pers 97583389 diensten 1156794 debt 27865574 pnl 0 equity 26642 pens 151260000; "
                    "FOI ready omzet geo empty/97.58m 62/151.26m off-balance pens/23.55m related recv; next rq_1392 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    entry = (
        "### Tick 1391 - 2026-08-19 - rq_1391 Fluvius OV dual residual leftover\n"
        "- Unit: Fluvius OV / Fluvius Opdrachthoudende Vereniging (leftover IGS opdrachthoudende vereniging / statutair personeel ex-Infrax + ex-Integan seconded to Fluvius System Operator) after residual dual hunt (KBO **0201.311.226**; official over.fluvius.be has governance + AV 03.06.2026; live NBB WVV VOL-inb deposit **2026-00165875** PDF 4.17MB / 40p; AV **03.06.2026**; header **08.06.2026**; created **08.06.2026**; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / Paul Eelen A02213 + Line Vyvey A02501 signed Gent 26.03.2026 oordeel zonder voorbehoud assets 27.892.216 / PnL 0). Leftover Fluvius personnel OV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; preferred leftover DISTINCT Fluvius holding this tick after the 9 DNB stack closed). Distinct from already-mined Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / Fluvius EG group-level (entity fluvius / FSO 0477.445.084). First confirmed not already mined: no Fluvius OV / 0201.311.226 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **01.01.1968**; statutaire naam FLUVIUS since 20.06.2018; Opdrachthoudende vereniging (Vlaams Gewest) since 02.06.2003; zetel Trichterheideweg 8 3500 Hasselt since 01.01.2025; **1 VE**; KBO no email/web/tel; official site https://over.fluvius.be/; btw since 01.01.1971; RSZ since 01.01.2022; NACE 35.140/35.220. Voorzitter Wim Dries since 29.03.2019; ondervoorzitter Mieke Bailleul-Vanrobaeys since 26.03.2025; commissaris EY 04.06.2025-07.06.2028. Hunt leftover Fluvius DNB first: the 9 DNB stack is closed (Riobra 1390 last). Fluvius OV statutory CDN live this tick (HTTP 200 / 4174612 / 40p) — taken as DISTINCT unmined Fluvius holding. Fluvius Riobra already mined 1390 — skipped. Fluvius Zenne-Dijle already mined 1389 — skipped. Fluvius Limburg already mined 1388 — skipped. Fluvius Halle-Vilvoorde already mined 1387 — skipped. Fluvius Antwerpen already mined 1386 — skipped. Fluvius West already mined 1385 — skipped. Fluvius Kempen already mined 1384 — skipped. Imewo already mined 1383 — skipped. INTERGEM already mined 1382 — skipped. Leftover AGB/zorg/EVA/APB not taken once live Fluvius OV extracted. Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live Fluvius OV extracted. Leftover IGS IVLA 0228.618.706 CDN 2026-00281193 + HAVICREM 0860.572.419 CDN 2026-00363711 now live — leftover next. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used (2025 SBM row empty). Not every-10 (next 1400).\n"
        "- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud; 6.10 omzet category/geo unpublished; 740 empty; 694 empty; 6.15 verbonden empty): assets **27.892.216** (was 30.297.051); fixed **491.180** / MVA **235.499** (gebouwen; 0 aanschaf); FVA **255.681** (andere aandelen 284; Ethias+Poolstok); current **27.401.036**; cash **242**; ST recv **24.254.648** (trade 11.118.804 JUMP / other 13.135.845); related-party ST recv **23.547.194**; prepaid **3.146.145** (pers 2.749.732); equity **26.642** (inbreng 24.393 / 984 aandelen; reserves 2.248); schulden **27.865.574** (no LT; ST leveranciers 958.474 + tax 5.180.158 + soc 19.877.282 + other 1.849.659); omzet **97.349.085** vs 102.061.287 (6.10 category/geo unpublished); othops **1.900.470** (740 empty); niet-recurrent 76A=66A **22.829.407** both years; diensten **1.156.794** vs 874.386; pers **97.583.389** / **573,6 VTE** / 746.467 uur / YE 582 (559,3 FTE; 0 in / 36,0 FTE out waarvan 35,0 pensioen); expl **+506.211** vs +1.086.728; fin opbr 189.852; fin kosten 36.950; tax 659.112 (1.056.359 - 397.247); PnL **0** vs 0; dividend **0** (694 empty); off-balance IAS19 pensioen **151,26m** (Limburg 106.13m / Antwerpen 15.65m / Zenne-Dijle 12.89m / West 11.84m / Halle-Vilvoorde 3.37m / Kempen 0.78m / Imewo 0.60m); commissaris 16.634; bestuurders 17.439; opleiding 443.935. Jaarverslag 25.03.2026: geen R&D / geen bijkantoren / geen bijzondere risico's; resultaat 0 doorgerekend aan FSO.\n"
        "- CSVs: sources+4/entities+1/budgets+48/commitments+1/leaderboard+1 + FOI ready `gap_flov_omzet_97_35m_pers_97_58m_pens_151_26m_l5` (not sent); rq_1391=done; spawn rq_1392; ticks=1391.\n"
        "- Coverage: residual dual L5 (Fluvius OV leftover personnel OV live WVV). Does **not** move L5 near-complete of EUR 347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs Fluvius EG / DNB possible. No progress refresh (not every-10; next 1400).\n"
        "- Next: rq_1392 residual dual L5 VL JR2025 hole_fill (prefer leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads; leftover IGS IVLA 0228.618.706 CDN 2026-00281193 / HAVICREM 0860.572.419 CDN 2026-00363711 now live; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover Nuhma daughters Otary RS only after leftover IGS/EVA/AGB; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / INTERZA 1381).\n"
    )
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1391 write done")


if __name__ == "__main__":
    main()

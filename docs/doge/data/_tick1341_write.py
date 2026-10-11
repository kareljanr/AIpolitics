# -*- coding: utf-8 -*-
"""Tick 1341 — leftover IGS IGEAN dienstverlening JR2025 WVV euros.
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

TICK = "1341"
UTC = "2026-08-18T03:15:00Z"
ENT = "igean_dv"
ENT2 = "igean_mv"
HIER = "Vlaanderen>Antwerpen>IGS>IGEAN>Dienstverlening"
GAP = "gap_igeandv_inv_68_19m_debt_85_39m_equity_thin_4_83m_l5"
SRC = "src_igean_jv2025_pdf"
SRC2 = "src_igean_site"
SRC3 = "src_kbo_igeandv_0206767574"
SRC4 = "src_kbo_igeanmv_0863137573"
SRC5 = "src_igean_foi_contact"
SRC_URL = "https://www.igean.be/sites/default/files/2026-06/IGEAN-jaarverslag-2025.pdf"
SRC2_URL = "https://www.igean.be/over-igean/bestuur/publicaties/jaarverslag"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0206767574"
SRC4_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0863137573"
SRC5_URL = "https://www.igean.be/over-igean/bestuur"
FOI_EMAIL = "financien@igean.be"
FOI_POSTAL = "Doornaardstraat 60 2160 Wommelgem"
DRAFT = "docs/doge/foi/drafts/gap_igeandv_inv_68_19m_debt_85_39m_equity_thin_4_83m_l5.md"
COMM = "comm_igean_dv_jr2025_inventory"
LB = "lb_igean_dv_inv_68_19m_debt_85_39m_equity_thin"


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
                "title": "IGEAN jaarverslag 2025 (official PDF; two WVV VOL-inb jaarrekeningen AV 25.06.2026)",
                "url": SRC_URL,
                "publisher": "IGEAN dienstverlening / IGEAN-milieu en veiligheid",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1341; official PDF 4.25MB 89p; AV 25.06.2026; "
                    "embeds WVV VOL-inb IGEAN dienstverlening 0206.767.574 + "
                    "IGEAN-milieu en veiligheid 0863.137.573; leftover IGS of mined Antwerp-region cities; not BBC J1-J5"
                ),
            },
            {
                "source_id": SRC2,
                "title": "IGEAN official jaarverslag page (Jaarverslag 2025 listed)",
                "url": SRC2_URL,
                "publisher": "IGEAN",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1341; HTTP 200 lists IGEAN jaarverslag 2025 PDF 4.25MB; "
                    "leftover IGS of mined Antwerp-region cities"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO IGEAN dienstverlening 0206.767.574",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1341; KBO 0206.767.574 Actief / normale toestand since 19.06.1969; "
                    "statutaire naam IGEAN dienstverlening since 17.06.2016; "
                    "Dienstverlenende vereniging (Vlaams Gewest) since 08.11.2003; "
                    "zetel Doornaardstraat 60 2160 Wommelgem since 16.07.1996; "
                    "1 VE; aanbestedende overheid since 19.06.1969; kapitaal 958635; "
                    "jaarvergadering mei; boekjaar 31 december; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "KBO IGEAN-milieu en veiligheid 0863.137.573",
                "url": SRC4_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1341; KBO 0863.137.573 Actief / normale toestand since 08.11.2003; "
                    "Opdrachthoudende vereniging (Vlaams Gewest); 28 VE; limited duration 18y on KBO; "
                    "aanbestedende overheid; same zetel Wommelgem; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC5,
                "title": "IGEAN bestuur / AV / RvB (FOI channel)",
                "url": SRC5_URL,
                "publisher": "IGEAN",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1341; FOI financien@igean.be from official JR PDF; "
                    "Doornaardstraat 60 2160 Wommelgem; AD Jo Bridts; voorzitter Maarten De Veuster"
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
                "name_nl": "IGEAN dienstverlening (dienstverlenende vereniging / leftover IGS)",
                "name_fr": "IGEAN dienstverlening (association de services / IGS residuel)",
                "name_en": "IGEAN service association (leftover intermunicipal IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.igean.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1341 leftover IGS residual of mined Antwerp-region cities; "
                    "KBO 0206.767.574 Actief since 19.06.1969; official JR2025 PDF downloads; "
                    "assets 103.920m inv 68.186m debt 85.394m equity thin 4.833m PnL +54.898; "
                    "FOI ready inventory/debt/dual-IGS/NBB"
                ),
            },
            {
                "entity_id": ENT2,
                "name_nl": "IGEAN-milieu en veiligheid (opdrachthoudende vereniging / leftover IGS sister)",
                "name_fr": "IGEAN-milieu en veiligheid (association missionnee / IGS soeur)",
                "name_en": "IGEAN environment and safety (leftover IGS sister)",
                "level": "other",
                "parent_id": ENT,
                "community_language": "nl",
                "website": "https://www.igean.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1341 leftover IGS sister in same official JR2025 PDF; "
                    "KBO 0863.137.573 Actief since 08.11.2003; 28 VE; "
                    "assets 38.168m debt JUMP 28.807m omzet 57.621m pers 19.663m PnL 0"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_igeandv_assets_2025", ENT, "2025", "103920441", "2025 assets 103920441.47 was 108957794.47; tick1341; primary WVV in official PDF"),
        ("bud_igeandv_fixed_2025", ENT, "2025", "369182", "2025 vaste activa 369182.44 was 421996.46; tick1341; primary WVV"),
        ("bud_igeandv_current_2025", ENT, "2025", "103551259", "2025 vlottende activa 103551259.03 was 108535798.01; tick1341; primary WVV"),
        ("bud_igeandv_inv_re_2025", ENT, "2025", "68186223", "2025 onroerende goederen bestemd voor verkoop 68186223.11 was 67022776.97; tick1341; primary WVV code 35"),
        ("bud_igeandv_lt_recv_2025", ENT, "2025", "23487789", "2025 LT overige vorderingen 23487789.09 DROP vs 31494163.53; tick1341; primary WVV"),
        ("bud_igeandv_st_recv_2025", ENT, "2025", "10125477", "2025 ST recv 10125477.41 (trade 3399977.29 + other 6725500.12); tick1341; primary WVV"),
        ("bud_igeandv_cash_2025", ENT, "2025", "1645795", "2025 cash 1645794.74 DROP vs 1930570.05; tick1341; primary WVV"),
        ("bud_igeandv_equity_2025", ENT, "2025", "4832798", "2025 equity 4832798.30 was 4808612.44 thin vs 103.92m assets; tick1341; primary WVV"),
        ("bud_igeandv_prov_2025", ENT, "2025", "13693936", "2025 voorzieningen overige risico's 13693936.03 was 13208745.97; tick1341; primary WVV"),
        ("bud_igeandv_debt_2025", ENT, "2025", "85393707", "2025 schulden 85393707.14 was 90940436.06; tick1341; primary WVV"),
        ("bud_igeandv_lt_fin_2025", ENT, "2025", "17406207", "2025 LT financial 17406206.96 (krediet 17185906.96 + achtergesteld 220300); tick1341; primary WVV"),
        ("bud_igeandv_st_debt_2025", ENT, "2025", "65591635", "2025 ST schulden 65591635.22 was 69334281.16; tick1341; primary WVV"),
        ("bud_igeandv_st_ltcurr_2025", ENT, "2025", "42998519", "2025 LT-within-year 42998519.00 was 43250276.87; tick1341; primary WVV"),
        ("bud_igeandv_st_fin_2025", ENT, "2025", "10338139", "2025 ST financial kredietinstellingen 10338138.95 was 18327510.22; tick1341; primary WVV"),
        ("bud_igeandv_prepay_2025", ENT, "2025", "11153539", "2025 ST vooruitbetalingen 11153538.90 was 6596659.72; tick1341; primary WVV"),
        ("bud_igeandv_turnover_2025", ENT, "2025", "5134809", "2025 omzet 5134808.64 was 4156543.81; tick1341; primary WVV"),
        ("bud_igeandv_ops_rev_2025", ENT, "2025", "9193942", "2025 bedrijfsopbrengsten 9193942.17 was 11471572.20; tick1341; primary WVV"),
        ("bud_igeandv_ops_cost_2025", ENT, "2025", "6743333", "2025 bedrijfskosten 6743332.64 was 7876195.03; tick1341; primary WVV"),
        ("bud_igeandv_ops_2025", ENT, "2025", "2450610", "2025 bedrijfswinst 2450609.53 was 3595377.17; tick1341; primary WVV 9901"),
        ("bud_igeandv_pers_2025", ENT, "2025", "4129543", "2025 bezoldigingen 4129542.51 was 3908613.25; tick1341; primary WVV"),
        ("bud_igeandv_fin_cost_2025", ENT, "2025", "2362953", "2025 fin kosten 2362952.85 (schulden 2359176.45); tick1341; primary WVV"),
        ("bud_igeandv_pnl_2025", ENT, "2025", "54898", "2025 PnL +54898.36 was +53259.29; tick1341; primary WVV 9904"),
        ("bud_igeanmv_assets_2025", ENT2, "2025", "38167808", "2025 assets 38167808.17 JUMP vs 33564769.31; tick1341; primary WVV sister"),
        ("bud_igeanmv_fixed_2025", ENT2, "2025", "26642129", "2025 vaste activa 26642129.03 JUMP vs 19340126.18; tick1341; primary WVV sister"),
        ("bud_igeanmv_mva_2025", ENT2, "2025", "21124431", "2025 MVA 21124430.79 (CIP 6631529.82); tick1341; primary WVV sister"),
        ("bud_igeanmv_cash_2025", ENT2, "2025", "2706083", "2025 cash 2706083.31 DROP vs 3261011.76; tick1341; primary WVV sister"),
        ("bud_igeanmv_equity_2025", ENT2, "2025", "4075700", "2025 equity 4075700.02 DROP vs 4239710.35; tick1341; primary WVV sister"),
        ("bud_igeanmv_debt_2025", ENT2, "2025", "28807341", "2025 schulden 28807340.80 JUMP vs 21895927.54; tick1341; primary WVV sister"),
        ("bud_igeanmv_lt_fin_2025", ENT2, "2025", "5225411", "2025 LT financial 5225410.65 (krediet 4437146.72 + overige 788263.93); tick1341; primary WVV sister"),
        ("bud_igeanmv_turnover_2025", ENT2, "2025", "57621266", "2025 omzet 57621265.80 was 57051316.19; tick1341; primary WVV sister"),
        ("bud_igeanmv_pers_2025", ENT2, "2025", "19663281", "2025 bezoldigingen 19663281.17 was 18783025.67; tick1341; primary WVV sister"),
        ("bud_igeanmv_ops_2025", ENT2, "2025", "261007", "2025 bedrijfswinst 261006.99 was 248563.15; tick1341; primary WVV sister 9901"),
        ("bud_igeanmv_pnl_2025", ENT2, "2025", "0", "2025 PnL 0 (9904 empty; auditor winst 0; tax 52660.04 = pretax 52660.04); tick1341; primary WVV sister"),
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
                "title": "IGEAN dienstverlening JR2025 leftover IGS dual (inventory 68.19m / debt 85.39m / thin equity 4.83m)",
                "entity_id": ENT,
                "beneficiary": "IGEAN dienstverlening / IGEAN-milieu en veiligheid / aangesloten Antwerpse gemeenten",
                "legal_basis": "Decreet lokaal bestuur IGS; dienstverlenende + opdrachthoudende vereniging; Bestuursdecreet openbaarheid; WVV neerlegging",
                "decision_date": "2026-06-25",
                "start_year": "1969",
                "end_year": "2025",
                "total_envelope_eur": "103920441",
                "cash_by_year": "",
                "remaining_eur": "4832798",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL Antwerp-region — vastgoedvoorraad / dual IGS debt; inventory/debt roster/NBB missing",
                "cut_option": "Publish parcel list of 68.19m inventory + debt roster 85.39m + dual IGS consolidation; do not recreate parallel IGS-shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1341; assets 103920441 inv 68186223 debt 85393707 equity 4832798 PnL +54898; sister MV assets 38167808 debt 28807341 PnL 0; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "IGEAN dienstverlening JR2025 leftover IGS: inventory 68.19m / debt 85.39m / thin equity 4.83m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "2362953",
                "total_cost_eur": "103920441",
                "tco_notes": "Leftover dual IGS of mined Antwerp-region cities: assets 103.92m / inventory RE-for-sale 68.19m / debt 85.39m / equity only 4.83m / interest 2.36m / sister MV assets 38.17m debt JUMP 28.81m omzet 57.62m PnL 0; do not treat 103.92m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "IGEAN / aangesloten Antwerpse gemeenten / vastgoed- en afval-IGS",
                "stated_goal": "Local leftover IGS map VL Antwerp-region — JR2025 PDF live; dual inventory/debt/NBB FOI",
                "measured_outcome": "Official PDF 2026-08-17: DV assets 103.92m / inv 68.19m / debt 85.39m / equity 4.83m / PnL +54.9k; MV assets 38.17m / debt 28.81m / PnL 0",
                "absurdity_score": "7.0",
                "cost_score": "7.2",
                "difficulty": "3.5",
                "priority_index": "6.9",
                "cut_proposal": "Publish parcel list of 68.19m inventory + debt roster 85.39m + dual IGS consolidation; do not recreate parallel IGS-shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1341; leftover IGS of mined Antwerp-region cities; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "Parcel list / book vs market of inventory onroerend bestemd voor verkoop "
                    "68186223.11 vs 67022776.97 + counterparties/looptijd of LT recv 23487789.09 "
                    "DROP vs 31494163.53 + ST other recv 6725500.12 + debt roster of schulden "
                    "85393707.14 (LT fin 17406206.96 + ST 65591635.22 of which LT-within-year "
                    "42998519.00 + ST fin 10338138.95 + vooruitbetalingen 11153538.90) + nature of "
                    "voorzieningen 13693936.03 + dual IGS consolidation IGEAN-milieu 0863.137.573 "
                    "(assets 38167808.17 debt JUMP 21895927.54 to 28807340.80 CIP 6631529.82 "
                    "omzet 57621265.80 pers 19663281.17 PnL 0) + NBB filing proof "
                    "(ref 2026-00257698 / 02.07.2026) + commissarisverslag HLB / AV 25.06.2026"
                ),
                "why_it_matters": (
                    "Leftover IGS shell of mined Antwerp-region cities: 103.92m assets vs thin "
                    "equity 4.83m and 68.19m real-estate inventory plus 85.39m debt is a dual "
                    "opacity/leverage residual, not TE-additive of 348bn. Sister waste IGS adds "
                    "38.17m assets / 57.62m turnover / 19.66m personnel."
                ),
                "priority": "8",
                "recipient_body": "IGEAN dienstverlening / IGEAN-milieu en veiligheid",
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
                    "tick1341 leftover IGS of mined Antwerp-region cities after honest hunt; "
                    "live JR2025 official PDF now downloads (4.25MB 89p two WVV). "
                    "Dommelhof leftover Limburg EVA KBO 0777.495.085 no JR2025 PDF — not taken. "
                    "De Schorre 403 / Ter Nethe JR2024 / Welzijnskoepel glossy / leftover cities no JR2025. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1341",
        "title": "IGEAN dienstverlening JR2025 leftover IGS dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: IGEAN dienstverlening leftover IGS of mined Antwerp-region cities after honest hunt; "
            "KBO 0206.767.574 Actief; live JR2025 official PDF (4.25MB 89p two WVV AV 25.06.2026); "
            "sourced euros assets 103.920m / inv 68.186m / debt 85.394m / equity 4.833m / PnL +54.898; "
            "sister MV 0863.137.573 assets 38.168m debt 28.807m omzet 57.621m PnL 0; "
            "FOI ready inventory/debt/dual-IGS/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T02:10:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1341 IGEAN leftover IGS residual; KBO 0206.767.574; live JR2025 PDF; "
            "sourced euros; FOI ready not sent; next rq_1342 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1342",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1341 done including IGEAN dienstverlening 1341 leftover IGS live WVV / "
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
            "Ter Nethe official still JR2024-only — take only if a PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
            "WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / "
            "WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 / EVA Kinderopvang Dilbeek 1330 / "
            "Zorg Houthalen 1329 / APB Zilvermeer 1328 / APB Vlabinvest 1327 / APB Monumentenwacht WVL 1326 / "
            "APB Vonk 1325 / APB Campus Vesta 1324 / AGB Blankenberge 1323 / AGB Aarschot / AGB Arendonk; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403; not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1341 after IGEAN leftover IGS live WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1341", rq_new, rq_spawn)
    print("research_queue 1341", found, "spawned_1342", spawned)

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
                "last_unit_id": "rq_1341",
                "ticks_completed": "1341",
                "paused": "no",
                "notes": (
                    "tick1341 IGEAN leftover IGS residual; KBO 0206.767.574; "
                    "live JR2025 PDF; sourced euros assets 103.920m inv 68.186m debt 85.394m equity 4.833m PnL +54.898; "
                    "FOI ready; next rq_1342 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = f"""
### Tick 1341 - 2026-08-18 - rq_1341 IGEAN dienstverlening dual residual leftover IGS
- Unit: IGEAN dienstverlening (dienstverlenende vereniging / leftover IGS) of already-mined Antwerp-region cities after residual dual hunt (KBO **0206.767.574**; official igean.be + live jaarverslag 2025 PDF 4.25MB / 89p; AV **25.06.2026**; two embedded WVV VOL-inb jaarrekeningen). Prefer live PDF over another unpublished FOI. Distinct from already-mined AGB Aarschot 1168 / AGB Arendonk 1150 / AGB Ibogem / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339. KBO Actief / normale toestand since **19.06.1969**; statutaire naam IGEAN dienstverlening since 17.06.2016; Dienstverlenende vereniging (Vlaams Gewest) since 08.11.2003; zetel Doornaardstraat 60 2160 Wommelgem since 16.07.1996; **1 VE**; aanbestedende overheid; kapitaal 958.635; jaarvergadering mei; boekjaar 31 december. Sister IGEAN-milieu en veiligheid KBO **0863.137.573** Actief since 08.11.2003; Opdrachthoudende vereniging; **28 VE**; limited duration 18y on KBO. Hunt leftover AGB/zorg/EVA first: Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 Actief private stichting — c-takt/dommelhof/limburg no JR2025 PDF (statutes only) so not taken; Ter Nethe official still JR2024-only; Welzijnskoepel West-Brabant jaarverslag 2025 glossy-only — not BBC; AGB Lebbeke ontbonden; AGB Bornem official still JR2024-only; AGB De Kluize unpublished. Leftover cities Londerzeel official still JR2022–2024 only / Wortegem-Petegem official JR2020–2024 only / Zwalm `/jaarrekening` 301/Cloudflare / Holsbeek 404 / Maarkedal TLS / Linkebeek 404 / Kapellen city GE 404 / Drogenbos 404 / Boutersem archive-only / Maaseik city GE 404 / Bierbeek 404 still no fetchable JR2025. APB POA/TPA/De Schorre/Warande/De Nekker/PIH/Inovant/Atlas official pages 403 — not taken. AGB Aarschot / AGB Arendonk already mined. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331. Not every-10 (next 1350).
- EUR strong (primary WVV in official PDF, IGEAN dienstverlening): assets **103.920.441** (was 108.957.794); inventory RE-for-sale **68.186.223** (was 67.022.777); LT recv **23.487.789** DROP vs 31.494.164; ST recv **10.125.477**; cash **1.645.795** DROP vs 1.930.570; equity **4.832.798** thin vs 103.92m; voorzieningen **13.693.936**; schulden **85.393.707**; LT fin **17.406.207**; ST debt **65.591.635** (LT-within-year **42.998.519** + ST fin **10.338.139** + vooruitbetalingen **11.153.539**); omzet **5.134.809**; expl **+2.450.610**; pers **4.129.543**; fin kosten **2.362.953**; PnL **+54.898**. Sister IGEAN-milieu: assets **38.167.808** JUMP vs 33.564.769; MVA **21.124.431** (CIP **6.631.530**); cash **2.706.083** DROP; equity **4.075.700** DROP; schulden **28.807.341** JUMP vs 21.895.928; LT fin **5.225.411**; omzet **57.621.266**; pers **19.663.281**; expl **+261.007**; PnL **0** (auditor balanstotaal 38.167.808 / winst 0).
- CSVs: sources+5/entities+2/budgets+33/commitments+1/leaderboard+1 + FOI ready `{GAP}` (not sent); rq_1341=done; spawn rq_1342; ticks=1341.
- Coverage: residual dual L5 (IGEAN leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1342 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1341 write done")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Tick 1343 — leftover IGS IVM Meetjesland JR2025 WVV euros.
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

TICK = "1343"
UTC = "2026-08-18T05:20:00Z"
ENT = "igs_ivm"
HIER = "Vlaanderen>OostVlaanderen>IGS>IVM>Meetjesland"
GAP = "gap_ivm_otherops_12_27m_pers_9_48m_expl_neg_l5"
SRC = "src_ivm_jr2025_pdf"
SRC2 = "src_ivm_site"
SRC3 = "src_kbo_ivm_0220574436"
SRC4 = "src_ivm_foi_contact"
SRC_URL = "https://ivm.paddlecms.net/sites/default/files/2026-06/Jaarrekening-2025.pdf"
SRC2_URL = "https://www.ivmmilieubeheer.be/jaarverslagen"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0220574436"
SRC4_URL = "https://www.ivmmilieubeheer.be/contact"
FOI_EMAIL = "boekhouding@ivmmilieubeheer.be"
FOI_POSTAL = "Sint-Laureinsesteenweg 29 9900 Eeklo"
DRAFT = "docs/doge/foi/drafts/gap_ivm_otherops_12_27m_pers_9_48m_expl_neg_l5.md"
COMM = "comm_ivm_jr2025_otherops"
LB = "lb_ivm_otherops_12_27m_pers_9_48m"


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
                "title": "IVM jaarrekening boekjaar 2025 (official WVV VOL-inb PDF; AV 10.06.2026)",
                "url": SRC_URL,
                "publisher": "IVM Intergemeentelijke opdrachthoudende Vereniging voor huisvuilverwerking Meetjesland",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1343; official PDF 1.24MB 48p; AV 10.06.2026; "
                    "WVV VOL-inb IVM 0220.574.436; leftover IGS of mined Meetjesland cities; not BBC J1-J5"
                ),
            },
            {
                "source_id": SRC2,
                "title": "IVM official jaarverslagen page (Jaarrekening 2025 listed)",
                "url": SRC2_URL,
                "publisher": "IVM",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1343; HTTP 200 lists Jaarrekening-2025.pdf 1.24MB + RvB verslag + commissarisverslag VGD; "
                    "leftover IGS of mined East-Flanders Meetjesland cities"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO IVM Meetjesland 0220.574.436",
                "url": SRC3_URL,
                "publisher": "KBO Besloten vennootschap Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1343; KBO 0220.574.436 Actief / normale toestand since 18.02.1980; "
                    "statutaire naam Intergemeentelijke opdrachthoudende Vereniging voor huisvuilverwerking Meetjesland since 19.12.2003; "
                    "afkorting IVM since 08.12.2021; Opdrachthoudende vereniging (Vlaams Gewest) since 06.01.2004; "
                    "zetel Sint-Laureinsesteenweg 29 9900 Eeklo since 01.01.2010; 14 VE; RSZ since 01.01.2022; "
                    "btw since 01.12.1982; aanbestedende overheid since 18.02.1980; kapitaal 500000; "
                    "jaarvergadering mei; boekjaar 31 december; databank 16.08.2026"
                ),
            },
            {
                "source_id": SRC4,
                "title": "IVM contact / hoofdzetel (FOI channel)",
                "url": SRC4_URL,
                "publisher": "IVM",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1343; FOI boekhouding@ivmmilieubeheer.be from official WVV PDF; "
                    "Sint-Laureinsesteenweg 29 9900 Eeklo; T 09 377 82 11 on contact page"
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
                "name_nl": "IVM Intergemeentelijke opdrachthoudende Vereniging voor huisvuilverwerking Meetjesland (leftover IGS)",
                "name_fr": "IVM intercommunale Meetjesland (association missionnee / IGS residuel)",
                "name_en": "IVM Meetjesland waste intermunicipal (leftover IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.ivmmilieubeheer.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1343 leftover IGS residual of mined Meetjesland AGB Aalter/Assenede/Deinze/Evergem/Kaprijke/Maldegem/Merelbeke-Melle/Nazareth-De Pinte + Zorgbedrijf Meetjesland; "
                    "KBO 0220.574.436 Actief since 18.02.1980; official JR2025 WVV PDF downloads; "
                    "assets 53.701m other-ops 12.269m pers 9.478m PnL -519.529; "
                    "FOI ready other-ops/dual-city/IRS/NBB"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_ivm_assets_2025", ENT, "2025", "53700580", "2025 assets 53700580.28 was 55251239.49; tick1343; primary WVV in official PDF"),
        ("bud_ivm_fixed_2025", ENT, "2025", "41381097", "2025 vaste activa 41381097.09 was 43133979.61; tick1343; primary WVV"),
        ("bud_ivm_iva_2025", ENT, "2025", "35016", "2025 IVA 35015.50; tick1343; primary WVV"),
        ("bud_ivm_mva_2025", ENT, "2025", "41344000", "2025 MVA 41343999.80 (gebouwen 3100198.03 + installaties 36027858.43 + rollend 546384.20 + CIP 1669559.14); tick1343; primary WVV"),
        ("bud_ivm_fva_2025", ENT, "2025", "2082", "2025 FVA 2081.79 (aandelen 995.79 + borg 1086.00); tick1343; primary WVV"),
        ("bud_ivm_current_2025", ENT, "2025", "12319483", "2025 vlottende activa 12319483.19 was 12117259.88; tick1343; primary WVV"),
        ("bud_ivm_stock_2025", ENT, "2025", "3031386", "2025 voorraden 3031386.43 was 2927031.26; tick1343; primary WVV"),
        ("bud_ivm_st_recv_2025", ENT, "2025", "5762491", "2025 ST recv trade 5762490.94 DROP vs 6287152.32; tick1343; primary WVV"),
        ("bud_ivm_invest_2025", ENT, "2025", "2875370", "2025 geldbeleggingen 2875370.43 was 2525791.44; tick1343; primary WVV"),
        ("bud_ivm_cash_2025", ENT, "2025", "245218", "2025 cash 245218.19 DROP vs 314661.93; tick1343; primary WVV"),
        ("bud_ivm_accr_asset_2025", ENT, "2025", "405017", "2025 overlopende activa 405017.20 JUMP vs 62622.93; tick1343; primary WVV"),
        ("bud_ivm_equity_2025", ENT, "2025", "27104096", "2025 equity 27104095.68 was 27558624.20; tick1343; primary WVV"),
        ("bud_ivm_inbreng_2025", ENT, "2025", "20107775", "2025 inbreng 20107775.00 was 20042775.00 (+304250 / 12170 aandelen); tick1343; primary WVV"),
        ("bud_ivm_reserves_2025", ENT, "2025", "6919870", "2025 reserves 6919870.33 (onbeschikbaar 1379461.71 + beschikbaar 5540408.62); tick1343; primary WVV"),
        ("bud_ivm_capsu_2025", ENT, "2025", "76450", "2025 kapitaalsubsidies 76450.35; tick1343; primary WVV"),
        ("bud_ivm_prov_2025", ENT, "2025", "873063", "2025 voorzieningen 873063.27 (pensioen 347113.27 + herstellingen 525950.00); tick1343; primary WVV"),
        ("bud_ivm_debt_2025", ENT, "2025", "25723421", "2025 schulden 25723421.33 was 26508294.90; tick1343; primary WVV"),
        ("bud_ivm_lt_fin_2025", ENT, "2025", "16625000", "2025 LT financial banken 16625000.00 was 18375000.00; tick1343; primary WVV"),
        ("bud_ivm_st_debt_2025", ENT, "2025", "8854431", "2025 ST schulden 8854430.65 was 7986021.38; tick1343; primary WVV"),
        ("bud_ivm_st_ltcurr_2025", ENT, "2025", "1750000", "2025 LT-within-year 1750000.00; tick1343; primary WVV"),
        ("bud_ivm_trade_pay_2025", ENT, "2025", "4713585", "2025 leveranciers 4713585.31 JUMP vs 3795907.01; tick1343; primary WVV"),
        ("bud_ivm_taxsoc_2025", ENT, "2025", "2360348", "2025 tax/soc 2360347.90 (tax 417386.93 + wages 1942960.97); tick1343; primary WVV"),
        ("bud_ivm_ops_rev_2025", ENT, "2025", "37251663", "2025 bedrijfsopbrengsten 37251662.99 was 36438878.50; tick1343; primary WVV"),
        ("bud_ivm_turnover_2025", ENT, "2025", "24964838", "2025 omzet 24964837.80 DROP vs 27476804.67; tick1343; primary WVV; no 6.10 split"),
        ("bud_ivm_otherops_2025", ENT, "2025", "12268825", "2025 andere bedrijfsopbrengsten 12268825.19 JUMP vs 8947941.60; tick1343; primary WVV code 74; subsidies 740 only 442307.19"),
        ("bud_ivm_subsidy_2025", ENT, "2025", "442307", "2025 exploitatiesubsidies code 740 442307.19 was 469497.68; tick1343; primary WVV 6.10"),
        ("bud_ivm_ops_cost_2025", ENT, "2025", "37484036", "2025 bedrijfskosten 37484035.59 was 35766581.79; tick1343; primary WVV"),
        ("bud_ivm_goods_2025", ENT, "2025", "2497517", "2025 handelsgoederen 2497516.70 was 1115947.15; tick1343; primary WVV"),
        ("bud_ivm_services_2025", ENT, "2025", "21039362", "2025 diensten 21039362.14 was 20340972.22; tick1343; primary WVV"),
        ("bud_ivm_pers_2025", ENT, "2025", "9477984", "2025 bezoldigingen 9477984.47 was 9411362.11; tick1343; primary WVV; VTE 105.1 / 109 koppen"),
        ("bud_ivm_uitzend_2025", ENT, "2025", "401918", "2025 uitzend 401917.99 VTE 5.4; tick1343; primary WVV 6.10"),
        ("bud_ivm_ops_2025", ENT, "2025", "-232373", "2025 bedrijfsverlies -232372.60 was +672296.71; tick1343; primary WVV 9901"),
        ("bud_ivm_fin_cost_2025", ENT, "2025", "306628", "2025 fin kosten 306628.19 (schulden 305146.99); tick1343; primary WVV"),
        ("bud_ivm_pnl_2025", ENT, "2025", "-519529", "2025 PnL -519528.52 was +376544.11; tick1343; primary WVV 9904"),
        ("bud_ivm_irs_notional_2025", ENT, "2025", "27125000", "2025 off-balance IRS notioneel 27125000 marktwaarde 1390494.79 was 1262885.48; tick1343; primary WVV 6.17"),
        ("bud_ivm_ovam_garant_2025", ENT, "2025", "1293027", "2025 off-balance OVAM waarborgen Burkel 1253027 + bodemassen 40000; tick1343; primary WVV 6.14"),
        ("bud_ivm_comm_fee_2025", ENT, "2025", "16206", "2025 commissaris VGD 16205.68 + andere 682.00; tick1343; primary WVV 6.16"),
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
                "title": "IVM Meetjesland JR2025 leftover IGS dual (other ops 12.27m / pers 9.48m / expl NEG / IRS 27.13m)",
                "entity_id": ENT,
                "beneficiary": "IVM / vennoten Aalter Assenede Deinze Eeklo Evergem Gavere Kaprijke Lievegem Maldegem Merelbeke-Melle Nazareth-De Pinte Sint-Laureins Sint-Martens-Latem Zulte",
                "legal_basis": "Decreet lokaal bestuur IGS; opdrachthoudende vereniging; Bestuursdecreet openbaarheid; WVV neerlegging",
                "decision_date": "2026-06-10",
                "start_year": "1980",
                "end_year": "2025",
                "total_envelope_eur": "37251663",
                "cash_by_year": "",
                "remaining_eur": "27104096",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL Meetjesland — werkingsbijdrage / dual city lines; other-ops roster/IRS/NBB missing",
                "cut_option": "Publish per-vennoot 12.27m other-ops + dual city lines + IRS 27.13m + OVAM 1.29m; do not recreate parallel waste-IGS shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1343; assets 53700580 otherops 12268825 pers 9477984 PnL -519529 VTE 105.1; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "IVM Meetjesland JR2025 leftover IGS: other ops 12.27m / pers 9.48m / expl NEG / IRS 27.13m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "9477984",
                "total_cost_eur": "37251663",
                "tco_notes": "Leftover dual IGS of mined Meetjesland cities: ops rev 37.25m / other ops 12.27m / pers 9.48m VTE 105.1 / assets 53.70m / IRS notional 27.13m / PnL -0.52m; do not treat 37.25m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "IVM / 14 Meetjesland gemeenten / waste-IGS",
                "stated_goal": "Local leftover IGS map VL Meetjesland — JR2025 PDF live; dual other-ops/IRS/NBB FOI",
                "measured_outcome": "Official PDF 2026-08-17: assets 53.70m / other ops 12.27m / pers 9.48m / PnL -519.5k / VTE 105.1",
                "absurdity_score": "6.6",
                "cost_score": "7.2",
                "difficulty": "3.2",
                "priority_index": "6.7",
                "cut_proposal": "Publish per-vennoot 12.27m other-ops + dual city lines + IRS 27.13m + OVAM 1.29m; do not recreate parallel waste-IGS shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1343; leftover IGS of mined Meetjesland cities; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "Per-vennoot 2025-2026 dual lines for andere bedrijfsopbrengsten 12268825.19 "
                    "(code 74; 6.10 subsidies 740 only 442307.19; no omzet split) vs omzet 24964837.80 "
                    "DROP vs 27476804.67 + counterparties/age of ST recv 5762490.94 DROP vs 6287152.32 "
                    "+ trade pay 4713585.31 JUMP vs 3795907.01 + diensten 21039362.14 vs pers 9477984.47 "
                    "VTE 105.1 / 109 koppen + uitzend 401917.99 VTE 5.4 + off-balance IRS notioneel "
                    "27125000 marktwaarde 1390494.79 (was 1262885.48) + OVAM waarborgen 1293027 "
                    "(Burkel 1253027 + bodemassen 40000) vs voorzieningen 873063.27 + NBB filing proof "
                    "+ commissarisverslag VGD Tina Burm / AV 10.06.2026"
                ),
                "why_it_matters": (
                    "Leftover IGS shell of mined Meetjesland AGB Aalter/Assenede/Deinze/Evergem/"
                    "Kaprijke/Maldegem/Merelbeke-Melle/Nazareth-De Pinte + Zorgbedrijf Meetjesland: "
                    "37.25m ops / 12.27m other-ops vs 9.48m personnel and 27.13m off-balance IRS "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "IVM Intergemeentelijke opdrachthoudende Vereniging voor huisvuilverwerking Meetjesland / vennoten Aalter Assenede Deinze Eeklo Evergem Gavere Kaprijke Lievegem Maldegem Merelbeke-Melle Nazareth-De Pinte Sint-Laureins Sint-Martens-Latem Zulte",
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
                    "tick1343 leftover IGS of mined Meetjesland cities after honest hunt; "
                    "live JR2025 official WVV PDF now downloads (1.24MB 48p VOL-inb). "
                    "Interleuven 2025 jaarverslag klaar but still no 2025 balans PDF — not taken. "
                    "IOK/IMOG/Haviland still 2024. De Schorre provincieantwerpen.be 403. "
                    "Veneco glossy 25MB not mined as BBC. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1343",
        "title": "IVM Meetjesland JR2025 leftover IGS dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: IVM leftover IGS of mined Meetjesland cities after honest hunt; "
            "KBO 0220.574.436 Actief; live JR2025 official WVV PDF (1.24MB 48p VOL-inb AV 10.06.2026); "
            "sourced euros assets 53.701m / other-ops 12.269m / pers 9.478m / PnL -519.529 / VTE 105.1; "
            "FOI ready other-ops/dual-city/IRS/NBB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-18T04:05:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1343 IVM leftover IGS residual; KBO 0220.574.436; live JR2025 WVV PDF; "
            "sourced euros; FOI ready not sent; next rq_1344 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1344",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1343 done including IVM Meetjesland 1343 leftover IGS live WVV / "
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
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
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
        "notes": "spawned tick1343 after IVM leftover IGS live WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1343", rq_new, rq_spawn)
    print("research_queue 1343", found, "spawned_1344", spawned)

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
                "last_unit_id": "rq_1343",
                "ticks_completed": "1343",
                "paused": "no",
                "notes": (
                    "tick1343 IVM leftover IGS residual; KBO 0220.574.436; "
                    "live JR2025 WVV PDF; sourced euros assets 53.701m other-ops 12.269m pers 9.478m PnL -519.529; "
                    "FOI ready; next rq_1344 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = f"""
### Tick 1343 - 2026-08-18 - rq_1343 IVM Meetjesland dual residual leftover IGS
- Unit: IVM Intergemeentelijke opdrachthoudende Vereniging voor huisvuilverwerking Meetjesland (leftover IGS) of already-mined Meetjesland AGB Aalter / Assenede / Deinze / Evergem / Kaprijke / Maldegem / Merelbeke-Melle / Nazareth-De Pinte + Zorgbedrijf Meetjesland / Welzijnsband Meetjesland after residual dual hunt (KBO **0220.574.436**; official ivmmilieubeheer.be + live jaarrekening 2025 PDF 1.24MB / 48p; AV **10.06.2026**; WVV VOL-inb). Prefer live PDF over another unpublished FOI. Distinct from already-mined IDM 1342 / IGEAN 1341 / EVA LSM 1340. KBO Actief / normale toestand since **18.02.1980**; statutaire naam Intergemeentelijke opdrachthoudende Vereniging voor huisvuilverwerking Meetjesland since 19.12.2003; afkorting IVM since 08.12.2021; Opdrachthoudende vereniging (Vlaams Gewest) since 06.01.2004; zetel Sint-Laureinsesteenweg 29 9900 Eeklo since 01.01.2010; **14 VE**; RSZ-werkgever since 01.01.2022; btw since 01.12.1982; aanbestedende overheid since 18.02.1980; kapitaal KBO 500.000; jaarvergadering mei; boekjaar 31 december; voorzitter Kim Martens; commissaris VGD / Tina Burm; e-mail boekhouding@ivmmilieubeheer.be on official WVV; tel 09 377 82 11 on contact page; NACE 38.330 / 38.210. Hunt leftover AGB/zorg/EVA first: Interleuven 2025 jaarverslag "klaar" + LinkedIn AV 17.06.2026 approved, but publications page still only jaarrekening 2024 PDF — not taken; IOK jaarverslagen still 2024; IMOG beleidsdocumenten still 2024; Haviland no 2025 JR PDF; De Schorre listed on provincieantwerpen.be but site 403 — not taken without bytes; Veneco glossy 25MB InDesign — not mined as BBC; Dommelhof leftover Limburg EVA KBO 0777.495.085 not taken once live IVM PDF downloaded. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek not taken once live IVM PDF downloaded. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331. Not every-10 (next 1350).
- EUR strong (primary WVV VOL-inb in official PDF): assets **53.700.580** (was 55.251.239); fixed **41.381.097**; MVA **41.344.000** (gebouwen **3.100.198** + installaties **36.027.858** + rollend **546.384** + CIP **1.669.559**); FVA **2.082**; current **12.319.483**; voorraden **3.031.386**; ST recv **5.762.491** DROP vs 6.287.152; beleggingen **2.875.370**; cash **245.218** DROP vs 314.662; equity **27.104.096**; inbreng **20.107.775**; reserves **6.919.870**; kapitaalsubsidies **76.450**; voorzieningen **873.063** (pensioen **347.113** + herstellingen **525.950**); schulden **25.723.421**; LT fin **16.625.000**; ST **8.854.431** (LT-within-year **1.750.000** + trade **4.713.585** JUMP vs 3.795.907 + tax/soc **2.360.348**); ops rev **37.251.663**; omzet **24.964.838** DROP vs 27.476.805; andere bedrijfsopbrengsten **12.268.825** JUMP vs 8.947.942 (waarvan subsidies 740 slechts **442.307**); pers **9.477.984**; VTE **105,1** / 109 koppen; diensten **21.039.362**; expl **-232.373**; fin kosten **306.628**; PnL **-519.529**. Off-balance same PDF: IRS notioneel **27.125.000** marktwaarde **1.390.495** (was 1.262.885); OVAM-waarborgen **1.293.027** (Burkel 1.253.027 + bodemassen 40.000).
- CSVs: sources+4/entities+1/budgets+37/commitments+1/leaderboard+1 + FOI ready `{{GAP}}` (not sent); rq_1343=done; spawn rq_1344; ticks=1343.
- Coverage: residual dual L5 (IVM leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1344 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 unless a fetchable JR appears).
""".replace("{GAP}", GAP)
    # fix the f-string GAP - I used {{GAP}} then replace. Actually I already have GAP in the f-string via the replace after. Wait I used f""" and {{GAP}} which becomes {GAP} then replace. Simpler: just embed GAP.
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    # rewrite log_entry cleanly without the replace hack
    log_entry = """
### Tick 1343 - 2026-08-18 - rq_1343 IVM Meetjesland dual residual leftover IGS
- Unit: IVM Intergemeentelijke opdrachthoudende Vereniging voor huisvuilverwerking Meetjesland (leftover IGS) of already-mined Meetjesland AGB Aalter / Assenede / Deinze / Evergem / Kaprijke / Maldegem / Merelbeke-Melle / Nazareth-De Pinte + Zorgbedrijf Meetjesland / Welzijnsband Meetjesland after residual dual hunt (KBO **0220.574.436**; official ivmmilieubeheer.be + live jaarrekening 2025 PDF 1.24MB / 48p; AV **10.06.2026**; WVV VOL-inb). Prefer live PDF over another unpublished FOI. Distinct from already-mined IDM 1342 / IGEAN 1341 / EVA LSM 1340. KBO Actief / normale toestand since **18.02.1980**; statutaire naam Intergemeentelijke opdrachthoudende Vereniging voor huisvuilverwerking Meetjesland since 19.12.2003; afkorting IVM since 08.12.2021; Opdrachthoudende vereniging (Vlaams Gewest) since 06.01.2004; zetel Sint-Laureinsesteenweg 29 9900 Eeklo since 01.01.2010; **14 VE**; RSZ-werkgever since 01.01.2022; btw since 01.12.1982; aanbestedende overheid since 18.02.1980; kapitaal KBO 500.000; jaarvergadering mei; boekjaar 31 december; voorzitter Kim Martens; commissaris VGD / Tina Burm; e-mail boekhouding@ivmmilieubeheer.be on official WVV; tel 09 377 82 11 on contact page; NACE 38.330 / 38.210. Hunt leftover AGB/zorg/EVA first: Interleuven 2025 jaarverslag "klaar" + LinkedIn AV 17.06.2026 approved, but publications page still only jaarrekening 2024 PDF — not taken; IOK jaarverslagen still 2024; IMOG beleidsdocumenten still 2024; Haviland no 2025 JR PDF; De Schorre listed on provincieantwerpen.be but site 403 — not taken without bytes; Veneco glossy 25MB InDesign — not mined as BBC; Dommelhof leftover Limburg EVA KBO 0777.495.085 not taken once live IVM PDF downloaded. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek not taken once live IVM PDF downloaded. NBB consult skipped (403/SPA). Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331. Not every-10 (next 1350).
- EUR strong (primary WVV VOL-inb in official PDF): assets **53.700.580** (was 55.251.239); fixed **41.381.097**; MVA **41.344.000** (gebouwen **3.100.198** + installaties **36.027.858** + rollend **546.384** + CIP **1.669.559**); FVA **2.082**; current **12.319.483**; voorraden **3.031.386**; ST recv **5.762.491** DROP vs 6.287.152; beleggingen **2.875.370**; cash **245.218** DROP vs 314.662; equity **27.104.096**; inbreng **20.107.775**; reserves **6.919.870**; kapitaalsubsidies **76.450**; voorzieningen **873.063** (pensioen **347.113** + herstellingen **525.950**); schulden **25.723.421**; LT fin **16.625.000**; ST **8.854.431** (LT-within-year **1.750.000** + trade **4.713.585** JUMP vs 3.795.907 + tax/soc **2.360.348**); ops rev **37.251.663**; omzet **24.964.838** DROP vs 27.476.805; andere bedrijfsopbrengsten **12.268.825** JUMP vs 8.947.942 (waarvan subsidies 740 slechts **442.307**); pers **9.477.984**; VTE **105,1** / 109 koppen; diensten **21.039.362**; expl **-232.373**; fin kosten **306.628**; PnL **-519.529**. Off-balance same PDF: IRS notioneel **27.125.000** marktwaarde **1.390.495** (was 1.262.885); OVAM-waarborgen **1.293.027** (Burkel 1.253.027 + bodemassen 40.000).
- CSVs: sources+4/entities+1/budgets+37/commitments+1/leaderboard+1 + FOI ready `gap_ivm_otherops_12_27m_pers_9_48m_expl_neg_l5` (not sent); rq_1343=done; spawn rq_1344; ticks=1343.
- Coverage: residual dual L5 (IVM leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1344 residual dual L5 VL JR2025 hole_fill (prefer leftover APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / WV Zorgbedrijf Brasschaat 1339 / WV Zorgband 1338 / WV Sleutelzorg 1337 / WV Weldenderend 1336 / WV BVK 1335 / WV OPcura 1334 / WV Het Dak 1333 / EVA Inagro 1332 / APB Vormingscentrum Malle 1331 unless a fetchable JR appears).
"""
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1343 write done")


if __name__ == "__main__":
    main()

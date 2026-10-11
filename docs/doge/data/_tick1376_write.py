# -*- coding: utf-8 -*-
"""Tick 1376 — leftover MIROM Roeselare JR2025 official NBB WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10 (next every-10 is 1380).
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1376"
UTC = "2026-08-19T04:20:00Z"
ENT = "igs_mirom"
HIER = "Vlaanderen>WestVlaanderen>IGS>MIROM>Roeselare12"
GAP = "gap_mirom_omzet_21_18m_diensten_12_64m_cip_l5"
SRC = "src_mirom_jr2025_nbb"
SRC2 = "src_mirom_site"
SRC3 = "src_kbo_mirom_0213894205"
SRC4 = "src_mirom_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00128720.pdf"
SRC2_URL = "https://www.mirom.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0213894205"
SRC4_URL = "https://www.mirom.be/werking-mirom-roeselare"
FOI_EMAIL = "info@mirom.be"
FOI_POSTAL = "Oostnieuwkerksesteenweg 121 8800 Roeselare"
DRAFT = "docs/doge/foi/drafts/gap_mirom_omzet_21_18m_diensten_12_64m_cip_l5.md"
COMM = "comm_mirom_jr2025_pnl"
LB = "lb_mirom_omzet_21_18m_diensten_12_64m_cip"


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
                "title": "MIROM Roeselare jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00128720; AV 26.05.2026)",
                "url": SRC_URL,
                "publisher": "MIROM Roeselare / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1376; official NBB VOL-inb PDF 429kB 47p deposit 2026-00128720 created 01.06.2026; "
                    "leftover IGS OV of 12 mined Roeselare-region municipalities; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Auditas BV B00364 / Sven Vansteelant A02050 9424; "
                    "oordeel zonder voorbehoud assets 37444580.98 / PnL -377780.19 signed 13.04.2026; "
                    "6.1/6.2.1-6.2.2/6.2.4-6.2.5/6.3.4-6.3.5/6.4.1-6.4.2/6.5.1-6.5.2/6.7.2/6.15/6.17/6.18.2/6.20 not filed; "
                    "6.10 category empty geo BE only; 6.18.1 exemption unmotivated; 8761/8762 empty; 9503 empty; not every-10"
                ),
            },
            {
                "source_id": SRC2,
                "title": "MIROM Roeselare official site (waste IGS 12 West-Vlaanderen municipalities)",
                "url": SRC2_URL,
                "publisher": "MIROM Roeselare Intercommunale",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1376; leftover IGS waste of Roeselare-region 12 municipalities; "
                    "VOL-inb 7 refers to website jaarverslagen; statutory 2025 balans is the NBB CDN deposit; "
                    "site lists publicaties/bestuursverslagen/jaarverslagen (not used for euros)"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO MIROM Roeselare 0213.894.205",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1376; KBO 0213.894.205 Actief / normale toestand since 21.12.1973; "
                    "statutaire naam MIROM Roeselare since 02.08.2024; "
                    "Opdrachthoudende vereniging (Vlaams Gewest) since 26.11.2004; "
                    "zetel Oostnieuwkerksesteenweg 121 8800 Roeselare since 21.12.1973; 1 VE; "
                    "btw since 01.05.1976; RSZ since 01.01.2022; aanbestedende overheid since 21.12.1973; "
                    "jaarvergadering april; boekjaar 31 december; "
                    "KBO lists 3 bestuurders (statutory 14); NACE 38.330"
                ),
            },
            {
                "source_id": SRC4,
                "title": "MIROM Roeselare FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "MIROM Roeselare",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1376; FOI info@mirom.be / 051 26 03 50; "
                    "Oostnieuwkerksesteenweg 121 8800 Roeselare; "
                    "voorzitter Stefaan Van Coillie / ondervoorzitter Elsie Desmet"
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
                "name_nl": "MIROM Roeselare (leftover opdrachthoudende vereniging / IGS afval 12 West-Vlaanderen gemeenten)",
                "name_fr": "MIROM Roulers (association chargee de mission residuelle / IGS dechets 12 communes Flandre-Occidentale)",
                "name_en": "MIROM Roeselare leftover 12-municipality waste IGS (mission association)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.mirom.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1376 leftover residual IGS OV of 12 mined Roeselare-region municipalities; "
                    "KBO 0213.894.205 Actief since 21.12.1973; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 37444581 omzet 21181609 diensten 12640771 pnl -377780; "
                    "FOI ready omzet 21.18m/diensten 12.64m/CIP 4.13m"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_mirom_assets_2025", ENT, "2025", "37444581", "2025 assets 37444581 VOL-inb 20/58; tick1376; primary official NBB WVV"),
        ("bud_mirom_assets_2024", ENT, "2024", "35595716", "2024 assets 35595716 comparative; tick1376; primary official NBB WVV 20/58"),
        ("bud_mirom_fixed_2025", ENT, "2025", "24810752", "2025 vaste activa 24810752 vs 22347251; tick1376; primary official NBB WVV 21/28"),
        ("bud_mirom_mva_2025", ENT, "2025", "24807516", "2025 MVA 24807516 vs 22345266; tick1376; primary official NBB WVV 22/27"),
        ("bud_mirom_buildings_2025", ENT, "2025", "11183507", "2025 terreinen en gebouwen 11183507 vs 11548214 (aanschaf year 131706 / YE aanschaf 17012556); tick1376; primary official NBB WVV 22"),
        ("bud_mirom_machines_2025", ENT, "2025", "7134317", "2025 installaties/machines 7134317 vs 7074409 (aanschaf year 676852 / YE aanschaf 29021134 / afschr cum 21917237); tick1376; primary official NBB WVV 23"),
        ("bud_mirom_rollend_2025", ENT, "2025", "2360323", "2025 meubilair/rollend 2360323 JUMP vs 1674378 (aanschaf year 1026880); tick1376; primary official NBB WVV 24"),
        ("bud_mirom_cip_2025", ENT, "2025", "4129369", "2025 activa in aanbouw 4129369 JUMP vs 2048264 after aanschaf 2081105; tick1376; primary official NBB WVV 27"),
        ("bud_mirom_cip_2024", ENT, "2024", "2048264", "2024 activa in aanbouw 2048264 comparative; tick1376; primary official NBB WVV 27"),
        ("bud_mirom_fva_2025", ENT, "2025", "3235", "2025 FVA 3235 (aandelen 3099 + borg 136); tick1376; primary official NBB WVV 28"),
        ("bud_mirom_current_2025", ENT, "2025", "12633829", "2025 vlottende activa 12633829 vs 13248465; tick1376; primary official NBB WVV 29/58"),
        ("bud_mirom_inv_2025", ENT, "2025", "1515406", "2025 voorraden 1515406 (grond-hulp 1290270 + handels 225135; WV 88756); tick1376; primary official NBB WVV 3"),
        ("bud_mirom_strecv_2025", ENT, "2025", "5905331", "2025 ST vorderingen 5905331 (trade 4364786 + other 1540545 JUMP vs 725165); tick1376; primary official NBB WVV 40/41"),
        ("bud_mirom_beleg_2025", ENT, "2025", "800000", "2025 geldbeleggingen 800000 (termijn 700000 1m-1y + other 100000); tick1376; primary official NBB WVV 50/53"),
        ("bud_mirom_cash_2025", ENT, "2025", "3829027", "2025 liquide middelen 3829027 DROP vs 6003034; tick1376; primary official NBB WVV 54/58"),
        ("bud_mirom_cash_2024", ENT, "2024", "6003034", "2024 liquide middelen 6003034 comparative; tick1376; primary official NBB WVV 54/58"),
        ("bud_mirom_prepaid_2025", ENT, "2025", "584065", "2025 overlopend actief 584065 (over te dragen 541365 + lonen 35168 + opbr 7532); tick1376; primary official NBB WVV 490/1"),
        ("bud_mirom_equity_2025", ENT, "2025", "28729064", "2025 eigen vermogen 28729064 vs 27624476; tick1376; primary official NBB WVV 10/15"),
        ("bud_mirom_inbreng_2025", ENT, "2025", "8212561", "2025 inbreng 8212561 (beschikbaar 4838675 + onbeschikbaar 3373886; 203487 aandelen op naam; 8761/8762 empty); tick1376; primary official NBB WVV 10/11"),
        ("bud_mirom_capinc_2025", ENT, "2025", "1672947", "2025 kapitaalverhoging 1672947 (6.7.1); tick1376; primary official NBB WVV"),
        ("bud_mirom_reserves_2025", ENT, "2025", "18813739", "2025 reserves 18813739 (statutair onbeschikbaar 9114416 + beschikbaar 9699324 after onttrekking 377780); tick1376; primary official NBB WVV 13"),
        ("bud_mirom_capsub_2025", ENT, "2025", "1573447", "2025 kapitaalsubsidies 1573447 vs 1764026; tick1376; primary official NBB WVV 15"),
        ("bud_mirom_prov_2025", ENT, "2025", "1450000", "2025 voorzieningen 1450000 vs 1270000 (pensioen 1440000 + Ivroponie 10000); tick1376; primary official NBB WVV 16"),
        ("bud_mirom_pens_2025", ENT, "2025", "1440000", "2025 pensioen/responsabilisering 1440000 vs 1260000 (Belfius tabellen; toevoeg 180000); tick1376; primary official NBB WVV 160"),
        ("bud_mirom_debt_2025", ENT, "2025", "7265517", "2025 schulden 7265517 vs 6701240; LT 0 / no bank; tick1376; primary official NBB WVV 17/49"),
        ("bud_mirom_st_2025", ENT, "2025", "5675587", "2025 ST schulden 5675587 vs 5398381; tick1376; primary official NBB WVV 42/48"),
        ("bud_mirom_sttrade_2025", ENT, "2025", "4041918", "2025 leveranciers 4041918 vs 3849664; tick1376; primary official NBB WVV 440/4"),
        ("bud_mirom_sttaxsoc_2025", ENT, "2025", "1316162", "2025 tax/soc 1316162 (tax 631287 + wages 684874); tick1376; primary official NBB WVV 45"),
        ("bud_mirom_stoth_2025", ENT, "2025", "317508", "2025 overige ST schulden 317508 vs 625636; tick1376; primary official NBB WVV 47/48"),
        ("bud_mirom_accrued_2025", ENT, "2025", "1589930", "2025 overlopend passief 1589930 (over te dragen opbrengsten); tick1376; primary official NBB WVV 492/3"),
        ("bud_mirom_ops_2025", ENT, "2025", "22552135", "2025 bedrijfsopbrengsten 22552135 vs 22139590; tick1376; primary official NBB WVV 70/76A"),
        ("bud_mirom_omzet_2025", ENT, "2025", "21181609", "2025 omzet 21181609 vs 21190661; 6.10 category empty / geo BE only; tick1376; primary official NBB WVV 70"),
        ("bud_mirom_omzet_2024", ENT, "2024", "21190661", "2024 omzet 21190661 comparative; tick1376; primary official NBB WVV 70"),
        ("bud_mirom_othops_2025", ENT, "2025", "1370526", "2025 andere bedrijfsopbrengsten 1370526 JUMP vs 622934 (740 subsidies 257791; ~1112735 unnamed); tick1376; primary official NBB WVV 74"),
        ("bud_mirom_subs_2025", ENT, "2025", "257791", "2025 exploitatiesubsidies 257791 vs 287458; tick1376; primary official NBB WVV 740"),
        ("bud_mirom_goods_2025", ENT, "2025", "2144300", "2025 handelsgoederen/grond-hulp 2144300 (aankopen 2154653 / voorraad -10353); tick1376; primary official NBB WVV 60"),
        ("bud_mirom_diensten_2025", ENT, "2025", "12640771", "2025 diensten 12640771 vs 12972307 (59.7pct of omzet); tick1376; primary official NBB WVV 61"),
        ("bud_mirom_diensten_2024", ENT, "2024", "12972307", "2024 diensten 12972307 comparative; tick1376; primary official NBB WVV 61"),
        ("bud_mirom_pers_2025", ENT, "2025", "5785312", "2025 bezoldigingen 5785312 / 58.1 VTE / 62 koppen / YE 59.8 VTE; tick1376; primary official NBB WVV 62 9087"),
        ("bud_mirom_uitzend_2025", ENT, "2025", "72248", "2025 uitzend 72248 / 7 VTE (6.10 617; sociale balans uitzend 12206/6 + ter beschikking 60041/1); tick1376; primary official NBB WVV 617"),
        ("bud_mirom_deprec_2025", ENT, "2025", "1454294", "2025 afschrijvingen 1454294 vs 1447380; tick1376; primary official NBB WVV 630"),
        ("bud_mirom_wv_2025", ENT, "2025", "88756", "2025 WV voorraden 88756; tick1376; primary official NBB WVV 631/4"),
        ("bud_mirom_provchg_2025", ENT, "2025", "180000", "2025 voorzieningen toevoeg 180000 (pensioen); tick1376; primary official NBB WVV 635/8"),
        ("bud_mirom_othcost_2025", ENT, "2025", "807742", "2025 andere bedrijfskosten 807742 (tax 767694 + other 40048); tick1376; primary official NBB WVV 640/8"),
        ("bud_mirom_expl_2025", ENT, "2025", "-549040", "2025 bedrijfsverlies 549040 vs 462127; tick1376; primary official NBB WVV 9901"),
        ("bud_mirom_expl_2024", ENT, "2024", "-462127", "2024 bedrijfsverlies 462127 comparative; tick1376; primary official NBB WVV 9901"),
        ("bud_mirom_fininc_2025", ENT, "2025", "205884", "2025 financiele opbrengsten 205884 (capsub 150133 + intrest 49307 + vord 6421); tick1376; primary official NBB WVV 75"),
        ("bud_mirom_capsub_pl_2025", ENT, "2025", "150133", "2025 kapitaalsubsidies in PnL 150133 vs 152829; tick1376; primary official NBB WVV 9125"),
        ("bud_mirom_fincost_2025", ENT, "2025", "19832", "2025 financiele kosten 19832 (schulden 17048 + bank 2749); tick1376; primary official NBB WVV 65"),
        ("bud_mirom_tax_2025", ENT, "2025", "14792", "2025 belasting 14792; tick1376; primary official NBB WVV 67/77"),
        ("bud_mirom_pnl_2025", ENT, "2025", "-377780", "2025 PnL 9904 -377780 vs -251738 onttrokken aan reserves; tick1376; primary official NBB WVV"),
        ("bud_mirom_pnl_2024", ENT, "2024", "-251738", "2024 PnL -251738 comparative; tick1376; primary official NBB WVV 9904"),
        ("bud_mirom_comm_2025", ENT, "2025", "9424", "2025 commissaris Auditas / Sven Vansteelant 9424; tick1376; primary official NBB WVV 9505"),
        ("bud_mirom_vat_out_2025", ENT, "2025", "1511979", "2025 BTW door de vennootschap 1511979 vs 1011692; tick1376; primary official NBB WVV 6.13 9146"),
        ("bud_mirom_cip_aanschaf_2025", ENT, "2025", "2081105", "2025 CIP aanschaf 2081105; tick1376; primary official NBB WVV 8166"),
        ("bud_mirom_rollend_aanschaf_2025", ENT, "2025", "1026880", "2025 rollend aanschaf 1026880; tick1376; primary official NBB WVV 8163"),
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
                "title": "MIROM Roeselare JR2025 leftover IGS dual (assets 37.44m / omzet 21.18m / diensten 12.64m / CIP 4.13m / PnL -0.38m)",
                "entity_id": ENT,
                "beneficiary": "MIROM Roeselare / 12 West-Vlaanderen municipalities",
                "legal_basis": "WVV OV; decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-05-26",
                "start_year": "1973",
                "end_year": "",
                "total_envelope_eur": "37444581",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL waste — 21.18m omzet (6.10 category empty) / 12.64m diensten / CIP 4.13m JUMP / kapitaalverhoging 1.67m",
                "cut_option": "Publish 21.18m omzet split + 12.64m diensten/top-20 + CIP 4.13m project list + 1.67m per-gemeente capital increase; do not keep 37.44m municipal waste IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1376; assets 37444581 omzet 21181609 diensten 12640771 pnl -377780; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "MIROM Roeselare JR2025 leftover IGS: assets 37.44m / omzet 21.18m / diensten 12.64m / CIP 4.13m / PnL -0.38m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "12640771",
                "total_cost_eur": "37444581",
                "tco_notes": (
                    "Leftover dual IGS OV of 12 mined Roeselare-region municipalities: "
                    "assets 37.44m / equity 28.73m / pnl -0.38m / omzet 21.18m (6.10 category empty) / "
                    "diensten 12.64m (60pct of omzet) / 58.1 VTE / CIP 4.13m JUMP / "
                    "kapitaalverhoging 1.67m / official NBB WVV live; "
                    "do not treat 37.44m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "MIROM Roeselare / 12 West-Vlaanderen municipalities",
                "stated_goal": "Local leftover IGS map VL waste — JR2025 live; dual omzet/diensten/CIP FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 37.44m / omzet 21.18m / diensten 12.64m / CIP 4.13m / pnl -0.38m",
                "absurdity_score": "7.2",
                "cost_score": "7.3",
                "difficulty": "2.5",
                "priority_index": "6.8",
                "cut_proposal": "Publish 21.18m omzet split + 12.64m diensten/top-20 + CIP 4.13m project list + 1.67m per-gemeente capital increase; do not keep 37.44m municipal waste IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1376; leftover IGS OV of mined Roeselare-region; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "omzet 21181609 vs 21190661 (WVV 70; 6.10 category empty / geo BE only) per stroom/tegenpartij "
                    "+ diensten 12640771 (59.7pct of omzet; WVV 61; comparative 12972307) top-20 leveranciers "
                    "+ andere bedrijfsopbrengsten 1370526 JUMP vs 622934 (740 subsidies 257791 only; ~1112735 unnamed) "
                    "+ CIP 4129369 JUMP vs 2048264 / aanschaf 2081105 project list "
                    "+ kapitaalverhoging 1672947 / 203487 aandelen / 8761/8762 empty + cash DROP 3829027 vs 6003034 "
                    "+ pensioen 1440000 Belfius + 6.18.1 exemption unmotivated + VOL-inb 7 website-only + 6.20/6.15/9503 not filed"
                ),
                "why_it_matters": (
                    "Leftover IGS OV of 12 mined Roeselare-region municipalities "
                    "(same leftover-IGS waste seam as IVAGO 1375 / MIWA 1374 / IVOO 1373 / IMOG 1369 / IVBO 1352 / IVIO 1347 / IVVO 1345): "
                    "37.44m assets / 21.18m omzet / 12.64m diensten / "
                    "CIP 4.13m JUMP / kapitaalverhoging 1.67m / 58.1 VTE / 6.10 category empty "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "MIROM Roeselare / Raad van Bestuur / Stefaan Van Coillie / Elsie Desmet / 12 West-Vlaanderen municipalities",
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
                    "tick1376 leftover IGS OV of 12 mined Roeselare-region municipalities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (429kB 47p deposit 2026-00128720). "
                    "IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. "
                    "IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. "
                    "IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. "
                    "Nuhma-group seam 1353-1365 skipped. Dommelhof leftover Limburg EVA not re-probed once live MIROM extracted. "
                    "Otary RS Nuhma-adjacent fallback not taken. "
                    "IVAREM still 2024. leftover AGB 404/403 as of 1375. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1376",
        "title": "MIROM Roeselare OV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: MIROM Roeselare leftover IGS OV of 12 mined Roeselare-region municipalities after honest hunt; KBO 0213.894.205 Actief; "
            "live JR2025 official NBB WVV VOL-inb PDF (429kB 47p deposit 2026-00128720; commissaris Auditas); "
            "sourced euros assets 37444581 / omzet 21181609 / diensten 12640771 / pnl -377780; "
            "FOI ready omzet 21.18m/diensten 12.64m/CIP 4.13m"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T04:00:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1376 MIROM Roeselare leftover IGS residual; KBO 0213.894.205; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1377 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1377",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1376 done including MIROM Roeselare 1376 leftover IGS live NBB WVV / "
            "IVAGO 1375 leftover IGS live NBB WVV / "
            "MIWA 1374 leftover IGS live NBB WVV / "
            "IVOO 1373 leftover IGS live NBB WVV / "
            "IGEMO 1372 leftover IGS live NBB WVV / "
            "Veneco 1371 leftover IGS live NBB WVV / "
            "Haviland 1370 leftover IGS live NBB WVV + every-10 / "
            "IMOG 1369 leftover IGS live NBB WVV / "
            "IOK 1368 leftover IGS live NBB WVV / "
            "Leiedal 1367 leftover IGS live NBB WVV / "
            "Interleuven 1366 leftover IGS live NBB WVV / "
            "s-Lim DV 1365 leftover IGS live NBB WVV / "
            "Herkenrode RE NV 1364 leftover vastgoed live NBB WVV / "
            "MyCSN NV 1363 leftover smart-city live NBB WVV / "
            "s-Lim CV 1362 leftover smart-city live NBB WVV / "
            "Nuhmeris NV 1361 leftover klimaat-holding live NBB WVV / "
            "ECO2050 cv 1360 leftover klimaat-coop live NBB WVV + every-10); "
            "prefer leftover MIROM Menen KBO 0213.809.081 CDN 2026-00228376 if still live; "
            "leftover De Nekker VZW 0450.062.281 CDN 2026-00147494 only if still live; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if a new live 2025 WVV PDF downloads (prefer leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; Otary CDN 2026-00254280 live prior tick, not taken); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but provincieantwerpen.be 403 — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1376 after MIROM Roeselare leftover IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1376", rq_new, rq_spawn)
    print("research_queue 1376", found, "spawned_1377", spawned)

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
                "last_unit_id": "rq_1376",
                "ticks_completed": "1376",
                "paused": "no",
                "notes": (
                    "tick1376 MIROM Roeselare leftover IGS residual; KBO 0213.894.205; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 37444581 omzet 21181609 diensten 12640771 pnl -377780; "
                    "FOI ready omzet 21.18m/diensten 12.64m/CIP 4.13m; next rq_1377 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    entry = """### Tick 1376 - 2026-08-19 - rq_1376 MIROM Roeselare dual residual leftover
- Unit: MIROM Roeselare (leftover opdrachthoudende vereniging / IGS waste of 12 mined Roeselare-region municipalities: Hooglede / Houthulst / Koekelare / Kortemark / Langemark-Poelkapelle / Lichtervelde / Moorslede / Roeselare / Staden / Torhout / Wingene / Zonnebeke; 203.487 aandelen op naam; eigen AEC + 19 km warmtenet) after residual dual hunt (KBO **0213.894.205**; official mirom.be has publicaties/jaarverslagen but no isolated statutory 2025 balans; live NBB WVV VOL-inb deposit **2026-00128720** PDF 429kB / 47p; AV **26.05.2026**; PDF created **01.06.2026**; header **28.05.2026**; commissaris Auditas Bedrijfsrevisoren BV B00364 0464.594.366 / Sven Vansteelant A02050 9.424 signed 13.04.2026 oordeel zonder voorbehoud assets 37.444.580,98 / PnL −377.780,19). Leftover IGS OV of mined cities whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last ticks listed MIROM Roeselare CDN 2026-00128720 as leftover next after IVAGO 1375). Distinct from already-mined IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **21.12.1973**; statutaire naam MIROM Roeselare since 02.08.2024; Opdrachthoudende vereniging (Vlaams Gewest) since 26.11.2004; zetel Oostnieuwkerksesteenweg 121 8800 Roeselare since 21.12.1973; **1 VE**; tel 051 26 03 50; e-mail info@mirom.be; web https://www.mirom.be/; btw since 01.05.1976; RSZ since 01.01.2022; aanbestedende overheid since 21.12.1973; jaarvergadering april; 14 statutory bestuurders / voorzitter Stefaan Van Coillie / ondervoorzitter Elsie Desmet; NACE 38.330. Hunt leftover AGB/zorg/EVA first: leftover AGB Mechelen/Kortrijk/Brugge/Roeselare/Oostende 404/403 as of 1375 — not re-probed once live MIROM extracted; Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live MIROM extracted; IVAREM still 2024 as of 1375; leftover APB provincieantwerpen.be 403. MIROM Roeselare statutory CDN live this tick (HTTP 200 / 429256 / 47p) — taken (preferred leftover IGS of mined Roeselare-region outside Nuhma). IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 already mined — skipped. MIROM Menen 2026-00228376 / De Nekker VZW 2026-00147494 2025 CDN still live — leftover next, not taken once live MIROM Roeselare extracted. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366. Not every-10 (next 1380).
- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud; 6.1/6.2.1-6.2.2/6.2.4-6.2.5/6.3.4-6.3.5/6.4.1-6.4.2/6.5.1-6.5.2/6.7.2/6.15/6.17/6.18.2/6.20 not filed; 6.10 category empty / geo BE only; 6.18.1 exemption unmotivated; 8761/8762 empty; 9503 empty; VOL-inb 7 website-only): assets **37.444.581** (was 35.595.716); fixed **24.810.752** / MVA **24.807.516** (gebouwen **11.183.507**; machines **7.134.317** aanschaf YE **29.021.134** / afschr cum 21.917.237; rollend **2.360.323 JUMP** vs 1.674.378 after aanschaf **1.026.880**; CIP **4.129.369 JUMP** vs 2.048.264 after aanschaf **2.081.105**); FVA 3.235; current **12.633.829**; inventory **1.515.406**; ST recv **5.905.331** (trade 4.364.786 + other **1.540.545 JUMP** vs 725.165); beleggingen **800.000** (termijn 700.000); cash **3.829.027 DROP** vs 6.003.034; equity **28.729.064** (inbreng 8.212.561 / kapitaalverhoging **1.672.947** / 203.487 aandelen; reserves 18.813.739; capsub 1.573.447); voorzieningen **1.450.000** (pensioen **1.440.000** Belfius + Ivroponie 10.000; toevoeg 180.000); schulden **7.265.517** (LT 0 / no bank; leveranciers 4.041.918); omzet **21.181.609** vs 21.190.661 (6.10 category empty); andere opbr **1.370.526 JUMP** vs 622.934 (740 subsidies 257.791; ~1.112.735 unnamed); diensten **12.640.771** (59,7% of omzet); pers **5.785.312** / **58,1 VTE** / 62 koppen / YE 59,8 VTE + uitzend **7 VTE / 72.248**; afschr 1.454.294; expl **−549.040** vs −462.127; fin opbr 205.884 (capsub 150.133); fin kosten 19.832; PnL **−377.780** vs −251.738 onttrokken aan reserves; commissaris 9.424.
- CSVs: sources+4/entities+1/budgets+56/commitments+1/leaderboard+1 + FOI ready `gap_mirom_omzet_21_18m_diensten_12_64m_cip_l5` (not sent); rq_1376=done; spawn rq_1377; ticks=1376.
- Coverage: residual dual L5 (MIROM Roeselare leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1380).
- Next: rq_1377 residual dual L5 VL JR2025 hole_fill (prefer leftover MIROM Menen KBO 0213.809.081 CDN 2026-00228376 if still live; leftover De Nekker VZW 0450.062.281 CDN 2026-00147494 only if still live; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS CDN 2026-00254280 / Rematics / Sunfin only if taken after leftover IGS; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; IVAREM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1376 write done")


if __name__ == "__main__":
    main()

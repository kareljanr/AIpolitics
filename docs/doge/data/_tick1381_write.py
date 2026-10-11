# -*- coding: utf-8 -*-
"""Tick 1381 — leftover INTERZA JR2025 official NBB WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10 (next 1390).
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1381"
UTC = "2026-08-19T02:15:00Z"
ENT = "igs_inza"
HIER = "Vlaanderen>VlaamsBrabant>IGS>INTERZA"
GAP = "gap_inza_omzet_4_54m_subs_5_72m_diensten_4_92m_l5"
SRC = "src_inza_jr2025_nbb"
SRC2 = "src_inza_site"
SRC3 = "src_kbo_inza_0219324522"
SRC4 = "src_inza_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00246462.pdf"
SRC2_URL = "https://www.incovo-interza.be/nl/over-interza-en-incovo"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0219324522"
SRC4_URL = "https://www.incovo-interza.be/nl"
FOI_EMAIL = "financien@incovo-interza.be"
FOI_POSTAL = "Hoogstraat 185 1930 Zaventem"
DRAFT = "docs/doge/foi/drafts/gap_inza_omzet_4_54m_subs_5_72m_diensten_4_92m_l5.md"
COMM = "comm_inza_jr2025_pnl"
LB = "lb_inza_omzet_4_54m_subs_5_72m_diensten_4_92m"


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
                "title": "INTERZA jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00246462; AV 24.06.2026)",
                "url": SRC_URL,
                "publisher": "INTERZA / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1381; official NBB VOL-inb PDF 2.50MB 53p deposit 2026-00246462 created 02.07.2026; "
                    "leftover IGS waste of Kampenhout+Kraainem+Steenokkerzeel+Wezembeek-Oppem+Zaventem; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Moore Audit BV B00212 / 0453.925.059 / "
                    "Carmen Van Camp A02365 + Jan De Bom Van Driessche A00909 11790 oordeel zonder voorbehoud assets 7439948 / PnL 592225; "
                    "VOL-inb 6.1/6.2/6.3.4-6.3.6/6.4.1/6.5/6.7.2/6.8/6.14/6.15/6.17/6.20/9 not filed; omzet 6.10 category/geo empty"
                ),
            },
            {
                "source_id": SRC2,
                "title": "INTERZA official site (leftover IGS afval Kampenhout/Kraainem/Steenokkerzeel/Wezembeek-Oppem/Zaventem; shared Interza-Incovo)",
                "url": SRC2_URL,
                "publisher": "INTERZA / Incovo",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1381; leftover IGS of 5 Vlaams-Brabant municipalities; "
                    "incovo-interza.be is shared with INCOVO; statutory 2025 balans is the NBB CDN deposit"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO INTERZA 0219.324.522",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1381; KBO 0219.324.522 Actief / normale toestand since 13.11.1978; "
                    "statutaire naam INTERCOMMUNALE VOOR AFVALBEHEER INTERZA since 02.07.2008; "
                    "afkorting INTERZA since 13.11.1978; Opdrachthoudende vereniging (Vlaams Gewest) since 17.08.2002; "
                    "zetel Hoogstraat 185 1930 Zaventem since 13.11.1978; 5 VE; "
                    "no KBO email/web/tel; btw since 01.01.1981; RSZ since 01.01.2022; aanbestedende overheid since 13.11.1978; "
                    "jaarvergadering mei; boekjaar 31 december; NACE 38.330/38.110"
                ),
            },
            {
                "source_id": SRC4,
                "title": "INTERZA FOI channel / official contact + shared Interza-Incovo site",
                "url": SRC4_URL,
                "publisher": "INTERZA",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1381; FOI financien@incovo-interza.be (shared mailbox documented on sibling INCOVO deposit); "
                    "Hoogstraat 185 1930 Zaventem; no own KBO email/web/tel"
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
                "name_nl": "INTERZA (leftover IGS afval Zaventem en omliggende / Intercommunale voor Afvalbeheer)",
                "name_fr": "INTERZA (intercommunale residuelle de dechets Zaventem et environs)",
                "name_en": "INTERZA leftover IGS waste Zaventem and surrounding municipalities",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.incovo-interza.be/nl",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1381 leftover residual IGS of Kampenhout+Kraainem+Steenokkerzeel+Wezembeek-Oppem+Zaventem; "
                    "KBO 0219.324.522 Actief since 13.11.1978; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 7439948 omzet 4541212 subs 5720694 diensten 4916314 pers 3881316 pnl 592225; "
                    "FOI ready omzet 6.10 empty / 5.72m 740 / 4.92m 61"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_inza_assets_2025", ENT, "2025", "7439948", "2025 assets 7439948 VOL-inb 20/58; tick1381; primary official NBB WVV; commissaris 7439948"),
        ("bud_inza_assets_2024", ENT, "2024", "7247774", "2024 assets 7247774 comparative; tick1381; primary official NBB WVV 20/58"),
        ("bud_inza_fixed_2025", ENT, "2025", "1160005", "2025 vaste activa 1160005 vs 1474212; tick1381; primary official NBB WVV 21/28"),
        ("bud_inza_mva_2025", ENT, "2025", "1156527", "2025 MVA 1156527 vs 1471569; tick1381; primary official NBB WVV 22/27"),
        ("bud_inza_buildings_2025", ENT, "2025", "158459", "2025 terreinen/gebouwen 158459 vs 146256; tick1381; primary official NBB WVV 22"),
        ("bud_inza_machines_2025", ENT, "2025", "73128", "2025 installaties/machines 73128 vs 91602; tick1381; primary official NBB WVV 23"),
        ("bud_inza_furniture_2025", ENT, "2025", "924941", "2025 meubilair/rollend 924941 vs 1233710; tick1381; primary official NBB WVV 24"),
        ("bud_inza_fva_2025", ENT, "2025", "3478", "2025 FVA 3478 vs 2644 (aandelen 508 + borg 2970); tick1381; primary official NBB WVV 28"),
        ("bud_inza_current_2025", ENT, "2025", "6279943", "2025 vlottende activa 6279943 vs 5773562; tick1381; primary official NBB WVV 29/58"),
        ("bud_inza_inv_2025", ENT, "2025", "97331", "2025 voorraden 97331 vs 116766; tick1381; primary official NBB WVV 3"),
        ("bud_inza_strecv_2025", ENT, "2025", "1101018", "2025 ST vorderingen 1101018 vs 1002412; tick1381; primary official NBB WVV 40/41"),
        ("bud_inza_trade_2025", ENT, "2025", "1071383", "2025 handelsvorderingen 1071383 vs 1002412; tick1381; primary official NBB WVV 40"),
        ("bud_inza_invest_2025", ENT, "2025", "0", "2025 geldbeleggingen 0 empty 50/53; tick1381; primary official NBB WVV 50/53"),
        ("bud_inza_cash_2025", ENT, "2025", "4543480", "2025 liquide middelen 4543480 JUMP vs 4060475 (61% of assets); tick1381; primary official NBB WVV 54/58"),
        ("bud_inza_cash_2024", ENT, "2024", "4060475", "2024 liquide middelen 4060475 comparative; tick1381; primary official NBB WVV 54/58"),
        ("bud_inza_prepaid_2025", ENT, "2025", "538113", "2025 overlopend actief 538113 (kosten 209155 + opbr 328958); tick1381; primary official NBB WVV 490/1"),
        ("bud_inza_equity_2025", ENT, "2025", "4002165", "2025 eigen vermogen 4002165 vs 3383797; tick1381; primary official NBB WVV 10/15"),
        ("bud_inza_equity_2024", ENT, "2024", "3383797", "2024 eigen vermogen 3383797 comparative; tick1381; primary official NBB WVV 10/15"),
        ("bud_inza_inbreng_2025", ENT, "2025", "834116", "2025 inbreng onbeschikbaar 834116 vs 807972 (geplaatst 2263050; niet-opgevraagd 1428934; 90507 aandelen); tick1381; primary official NBB WVV 10/11"),
        ("bud_inza_reval_2025", ENT, "2025", "48733", "2025 herwaarderingsmeerwaarden 48733; tick1381; primary official NBB WVV 12"),
        ("bud_inza_reserves_2025", ENT, "2025", "3119316", "2025 reserves 3119316 (onbeschikbaar 789628 + beschikbaar 2329688); tick1381; primary official NBB WVV 13"),
        ("bud_inza_prov_2025", ENT, "2025", "2036349", "2025 voorzieningen 2036349 vs 2066386 (pens 1204962 + herstelling 801387 + overige 30000); tick1381; primary official NBB WVV 16"),
        ("bud_inza_prov_2024", ENT, "2024", "2066386", "2024 voorzieningen 2066386 comparative; tick1381; primary official NBB WVV 16"),
        ("bud_inza_pens_2025", ENT, "2025", "1204962", "2025 pensioenvoorziening 1204962 vs 1264999 (160; responsabilisering -60036); tick1381; primary official NBB WVV 160"),
        ("bud_inza_repair_2025", ENT, "2025", "801387", "2025 grote herstelling 801387 (gebouwen 301387 + wagenpark 500000); tick1381; primary official NBB WVV 162"),
        ("bud_inza_debt_2025", ENT, "2025", "1401433", "2025 schulden 1401433 vs 1797591; no LT; tick1381; primary official NBB WVV 17/49"),
        ("bud_inza_st_2025", ENT, "2025", "1401187", "2025 ST schulden 1401187 vs 1744401; tick1381; primary official NBB WVV 42/48"),
        ("bud_inza_sttrade_2025", ENT, "2025", "992592", "2025 leveranciers 992592 vs 643742; tick1381; primary official NBB WVV 440/4"),
        ("bud_inza_sttaxsoc_2025", ENT, "2025", "265938", "2025 tax+soc 265938 (tax 54094 + soc 211844); tick1381; primary official NBB WVV 45"),
        ("bud_inza_stother_2025", ENT, "2025", "142657", "2025 overige ST 142657 vs 855007; tick1381; primary official NBB WVV 47/48"),
        ("bud_inza_accrued_2025", ENT, "2025", "246", "2025 overlopend passief 246 vs 53190; tick1381; primary official NBB WVV 492/3"),
        ("bud_inza_opsinc_2025", ENT, "2025", "10458650", "2025 bedrijfsopbrengsten 10458650 vs 10041940; tick1381; primary official NBB WVV 70/76A"),
        ("bud_inza_omzet_2025", ENT, "2025", "4541212", "2025 omzet 4541212 vs 4729340; 6.10 category/geo empty; tick1381; primary official NBB WVV 70"),
        ("bud_inza_omzet_2024", ENT, "2024", "4729340", "2024 omzet 4729340 comparative; tick1381; primary official NBB WVV 70"),
        ("bud_inza_othops_2025", ENT, "2025", "5907438", "2025 andere bedrijfsopbrengsten 5907438 vs 5312350; tick1381; primary official NBB WVV 74"),
        ("bud_inza_subs_2025", ENT, "2025", "5720694", "2025 exploitatiesubsidies 5720694 JUMP vs 4801697 (740); tick1381; primary official NBB WVV 6.10 740"),
        ("bud_inza_subs_2024", ENT, "2024", "4801697", "2024 exploitatiesubsidies 4801697 comparative; tick1381; primary official NBB WVV 6.10 740"),
        ("bud_inza_cityfee_2025", ENT, "2025", "5198259", "2025 bijdragen gemeentevennoten 5198259 (jaarverslag split of 74); tick1381; primary official NBB WVV jaarverslag"),
        ("bud_inza_nrec_2025", ENT, "2025", "10000", "2025 niet-recurrente bedrijfsopbrengsten 10000 vs 250; tick1381; primary official NBB WVV 76A"),
        ("bud_inza_opscost_2025", ENT, "2025", "9891766", "2025 bedrijfskosten 9891766 vs 10018054; tick1381; primary official NBB WVV 60/66A"),
        ("bud_inza_goods_2025", ENT, "2025", "757794", "2025 handelsgoederen 757794 vs 704382 (aankopen 738360); tick1381; primary official NBB WVV 60"),
        ("bud_inza_diensten_2025", ENT, "2025", "4916314", "2025 diensten 4916314 vs 4385311; no split; tick1381; primary official NBB WVV 61"),
        ("bud_inza_diensten_2024", ENT, "2024", "4385311", "2024 diensten 4385311 comparative; tick1381; primary official NBB WVV 61"),
        ("bud_inza_pers_2025", ENT, "2025", "3881316", "2025 bezoldigingen 3881316 / 56.7 VTE / 81027 uur / YE 60; tick1381; primary official NBB WVV 62 9087"),
        ("bud_inza_pers_2024", ENT, "2024", "4115562", "2024 bezoldigingen 4115562 / 61.6 VTE comparative; tick1381; primary official NBB WVV 62"),
        ("bud_inza_pens624_2025", ENT, "2025", "434062", "2025 ouderdoms/overlevingspensioenen 434062 vs 520881; tick1381; primary official NBB WVV 6.10 624"),
        ("bud_inza_uitzend_2025", ENT, "2025", "715688", "2025 uitzendkosten 715688 / 15 VTE / 23049 uur; tick1381; primary official NBB WVV 6.10 617"),
        ("bud_inza_deprec_2025", ENT, "2025", "360459", "2025 afschrijvingen 360459 vs 398377; tick1381; primary official NBB WVV 630"),
        ("bud_inza_prov_pnl_2025", ENT, "2025", "-60036", "2025 voorzieningen PnL -60036 vs 408717 (all pens 635); tick1381; primary official NBB WVV 635/8"),
        ("bud_inza_othcost_2025", ENT, "2025", "4477", "2025 andere bedrijfskosten 4477 vs 4884 (all 640 bedrijfsbelastingen); tick1381; primary official NBB WVV 640/8"),
        ("bud_inza_expl_2025", ENT, "2025", "566884", "2025 bedrijfswinst 566884 vs 23886; tick1381; primary official NBB WVV 9901"),
        ("bud_inza_expl_2024", ENT, "2024", "23886", "2024 bedrijfswinst 23886 comparative; tick1381; primary official NBB WVV 9901"),
        ("bud_inza_fininc_2025", ENT, "2025", "46821", "2025 financiele opbrengsten 46821 vs 71314 (vlottende 45512); tick1381; primary official NBB WVV 75"),
        ("bud_inza_fincost_2025", ENT, "2025", "7826", "2025 financiele kosten 7826 vs 3679 (all bankkosten); tick1381; primary official NBB WVV 65"),
        ("bud_inza_tax_2025", ENT, "2025", "13654", "2025 belastingen 13654 vs 20207; tick1381; primary official NBB WVV 67/77"),
        ("bud_inza_pnl_2025", ENT, "2025", "592225", "2025 PnL 9904 592225 vs 71314; commissaris 592225; tick1381; primary official NBB WVV"),
        ("bud_inza_pnl_2024", ENT, "2024", "71314", "2024 PnL 71314 comparative; tick1381; primary official NBB WVV 9904"),
        ("bud_inza_comm_2025", ENT, "2025", "11790", "2025 commissaris Moore Audit BV / Van Camp + De Bom Van Driessche 11790; tick1381; primary official NBB WVV 9505"),
        ("bud_inza_board_2025", ENT, "2025", "36985", "2025 bestuurders zitpenningen 36325.8 + km 659.37 (9503 empty); tick1381; primary official NBB WVV remuneratieverslag"),
        ("bud_inza_inbreng_call_2025", ENT, "2025", "26144", "2025 volstorting inbreng 26143.75 (AV dec 2025 pop 90507); tick1381; primary official NBB WVV jaarverslag"),
        ("bud_inza_pop_2025", ENT, "2025", "90507", "2025 vennoten bevolking 90507 (Kampenhout 12523 / Kraainem 13906 / Steenokkerzeel 12673 / Wezembeek-Oppem 14735 / Zaventem 36670); tick1381; primary official NBB WVV jaarverslag"),
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
                "title": "INTERZA JR2025 leftover IGS dual (assets 7.44m / omzet 4.54m / subs 5.72m / diensten 4.92m / pens 1.20m / PnL +592k)",
                "entity_id": ENT,
                "beneficiary": "INTERZA / Kampenhout + Kraainem + Steenokkerzeel + Wezembeek-Oppem + Zaventem",
                "legal_basis": "WVV OV; Decreet Lokaal Bestuur; NBB neerlegging",
                "decision_date": "2026-06-24",
                "start_year": "1978",
                "end_year": "",
                "total_envelope_eur": "7439948",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL waste — 4.54m omzet (6.10 empty) / 5.72m subsidies / 4.92m diensten",
                "cut_option": "Publish unpublished omzet 6.10 + 5.72m 740 + 4.92m 61 + 1.20m pens + INCOVO pass-through; do not keep waste IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1381; assets 7439948 omzet 4541212 subs 5720694 diensten 4916314 pnl 592225 equity 4002165; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "INTERZA JR2025 leftover IGS: assets 7.44m / omzet 4.54m / subs 5.72m / diensten 4.92m / pens 1.20m / cash 4.54m / PnL +592k",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "4916314",
                "total_cost_eur": "7439948",
                "tco_notes": (
                    "Leftover dual IGS waste of 5 Vlaams-Brabant municipalities: "
                    "assets 7.44m / equity 4.00m / pnl +592k / omzet 4.54m (6.10 empty) / "
                    "subsidies 5.72m JUMP / diensten 4.92m / 56.7 VTE + 15 uitzend / pens 1.20m / cash 4.54m; "
                    "official NBB WVV live; do not treat 7.44m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "INTERZA / Kampenhout + Kraainem + Steenokkerzeel + Wezembeek-Oppem + Zaventem",
                "stated_goal": "Local leftover IGS map VL waste — JR2025 live; dual omzet-empty/subs/diensten FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 7.44m / omzet 4.54m / subs 5.72m / diensten 4.92m / pens 1.20m / cash 4.54m / pnl +592k",
                "absurdity_score": "7.0",
                "cost_score": "5.4",
                "difficulty": "2.5",
                "priority_index": "6.1",
                "cut_proposal": "Publish unpublished omzet 6.10 + 5.72m 740 + 4.92m 61 + 1.20m pens + INCOVO pass-through; do not keep waste IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1381; leftover IGS of 5 Vlaams-Brabant municipalities; FOI ready not sent; not TE-additive of 348bn",
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
                    "omzet 4541212 vs 4729340 (WVV 70; 6.10 category empty / geo empty) per stroom/tegenpartij/vennoot unpublished "
                    "+ exploitatiesubsidies 5720694 JUMP vs 4801697 (WVV 740; othops 5907438; jaarverslag bijdragen 5198259) per toekennende overheid "
                    "+ diensten 4916314 vs 4385311 (WVV 61; no split) top-20 leveranciers + INCOVO pass-through "
                    "+ pensioenvoorziening 1204962 (160; 624 434062) + uitzend 715688 / 15 VTE "
                    "+ cash 4543480 (61% of assets; 50/53 empty) treasury unpublished "
                    "+ inbreng niet-opgevraagd 1428934 / AV dec 2025 pop 90507 + VOL-inb 6.1/6.2/6.8/6.14/6.15/6.17/6.20/9 not filed + 9503 empty"
                ),
                "why_it_matters": (
                    "Leftover IGS OV of 5 mined Vlaams-Brabant municipalities "
                    "(same leftover-IGS waste seam as INCOVO 1380 / ISVAG 1379 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IMOG 1369 / IVBO 1352): "
                    "7.44m assets / 4.54m omzet / 5.72m subsidies / 4.92m diensten / 1.20m pension / "
                    "56.7 VTE + 15 uitzend / 4.54m cash / shared INCOVO shell "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "INTERZA / Raad van Bestuur / Wim Driesen / Peter De Bruyne / Kampenhout + Kraainem + Steenokkerzeel + Wezembeek-Oppem + Zaventem",
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
                    "tick1381 leftover IGS OV of 5 Vlaams-Brabant municipalities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (2.50MB 53p deposit 2026-00246462). "
                    "INCOVO already mined 1380 — skipped. ISVAG already mined 1379 — skipped. De Nekker already mined 1378 — skipped. "
                    "MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. "
                    "IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. "
                    "IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. "
                    "IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. "
                    "Nuhma-group seam 1353-1365 skipped. "
                    "Fluvius Midden-Vlaanderen / INTERGEM leftover energy IGS 0220.764.971 CDN 2026-00227859 live — leftover next. "
                    "Dommelhof leftover Limburg EVA 0777.495.085 not re-probed once live INTERZA extracted. "
                    "IVAREM still 2024. Otary RS Nuhma-adjacent fallback not taken. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1381",
        "title": "INTERZA JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: INTERZA leftover IGS of 5 Vlaams-Brabant municipalities after honest hunt; "
            "KBO 0219.324.522 Actief; live JR2025 official NBB WVV VOL-inb PDF (2.50MB 53p deposit 2026-00246462; commissaris Moore Audit); "
            "sourced euros assets 7439948 / omzet 4541212 / subs 5720694 / diensten 4916314 / pers 3881316 / pnl 592225; "
            "FOI ready omzet 6.10 empty / 5.72m 740 / 4.92m 61"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T02:00:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1381 INTERZA leftover IGS residual; KBO 0219.324.522; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1382 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1382",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1381 done including INTERZA 1381 leftover IGS live NBB WVV / "
            "INCOVO 1380 leftover IGS live NBB WVV + every-10 / "
            "ISVAG 1379 leftover IGS live NBB WVV / "
            "De Nekker 1378 leftover provincial EVA live NBB WVV / "
            "MIROM Menen 1377 leftover IGS live NBB WVV / "
            "MIROM Roeselare 1376 leftover IGS live NBB WVV / "
            "IVAGO 1375 leftover IGS live NBB WVV / "
            "MIWA 1374 leftover IGS live NBB WVV / "
            "IVOO 1373 leftover IGS live NBB WVV / "
            "IGEMO 1372 leftover IGS live NBB WVV / "
            "Veneco 1371 leftover IGS live NBB WVV / "
            "Haviland 1370 leftover IGS live NBB WVV + every-10); "
            "Fluvius Midden-Vlaanderen / INTERGEM leftover energy IGS KBO 0220.764.971 CDN 2026-00227859 now live — take if still unmined; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads "
            "(old VZW 0443.049.478 CDN 2026-00325874 is a different Tielt-Winge entity); "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB PIH / APB Inovant / APB Atlas listed or leftover but provincieantwerpen.be 403 — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1381 after INTERZA leftover IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1381", rq_new, rq_spawn)
    print("research_queue 1381", found, "spawned_1382", spawned)

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
                "last_unit_id": "rq_1381",
                "ticks_completed": "1381",
                "paused": "no",
                "notes": (
                    "tick1381 INTERZA leftover IGS residual; KBO 0219.324.522; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 7439948 omzet 4541212 subs 5720694 diensten 4916314 pers 3881316 pnl 592225 equity 4002165 cash 4543480; "
                    "FOI ready omzet 6.10 empty/5.72m 740/4.92m 61; next rq_1382 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    entry = """### Tick 1381 - 2026-08-19 - rq_1381 INTERZA dual residual leftover
- Unit: Intercommunale voor Afvalbeheer INTERZA (leftover IGS opdrachthoudende vereniging / afvalbeleid + preventie + inzameling of Kampenhout + Kraainem + Steenokkerzeel + Wezembeek-Oppem + Zaventem; verwerking fully outsourced; shared Interza-Incovo site) after residual dual hunt (KBO **0219.324.522**; official incovo-interza.be has missie/bestuur/publicaties but no isolated statutory 2025 balans — live NBB WVV VOL-inb deposit **2026-00246462** PDF 2.50MB / 53p; AV **24.06.2026**; PDF created **02.07.2026**; commissaris Moore Audit BV B00212 / 0453.925.059 / Carmen Van Camp A02365 + Jan De Bom Van Driessche A00909 11.790 signed 10.06.2026 oordeel zonder voorbehoud assets 7.439.948 / PnL +592.225; 15e opeenvolgend boekjaar; mandaat AV 21.06.2023 tot AV 24.06.2026). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; prior ticks listed INTERZA CDN 2026-00246462 as leftover next after INCOVO 1380). Distinct from already-mined INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 / AGB Zaventem. KBO Actief / normale toestand since **13.11.1978**; statutaire naam INTERCOMMUNALE VOOR AFVALBEHEER INTERZA since 02.07.2008; afkorting INTERZA since 13.11.1978; Opdrachthoudende vereniging (Vlaams Gewest) since 17.08.2002; zetel Hoogstraat 185 1930 Zaventem since 13.11.1978; **5 VE**; KBO no email/web/tel; official site https://www.incovo-interza.be/; e-mail financien@incovo-interza.be (shared); btw since 01.01.1981; RSZ since 01.01.2022; aanbestedende overheid since 13.11.1978; jaarvergadering mei; boekjaar 31 december; NACE 38.330/38.110. Voorzitter Wim Driesen since 13.03.2025; ondervoorzitter Ronald Probst; algemeen directeur Peter De Bruyne; commissaris Moore Audit BV. Hunt leftover AGB/zorg/EVA first: leftover AGB Mechelen/Kortrijk/Brugge/Roeselare/Oostende 404/403 as of 1375 — not re-probed once live INTERZA extracted; Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live INTERZA extracted; IVAREM still 2024; leftover APB provincieantwerpen.be 403. INTERZA statutory CDN live this tick (HTTP 200 / 2496272 / 53p) — taken (preferred leftover IGS of mined Zaventem-ommeland municipalities outside Nuhma). INCOVO already mined 1380 — skipped. ISVAG already mined 1379 — skipped. De Nekker already mined 1378 — skipped. MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 already mined — skipped. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. Fluvius Midden-Vlaanderen / INTERGEM 0220.764.971 CDN 2026-00227859 live (2.01MB) — leftover next. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366. Not every-10 (next 1390).
- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud assets 7.439.948 / PnL +592.225; VOL-inb 6.1/6.2/6.3.4-6.3.6/6.4.1/6.5/6.7.2/6.8/6.14/6.15/6.17/6.20/9 not filed; omzet 6.10 category/geo empty): assets **7.439.948** (was 7.247.774); fixed **1.160.005** / MVA **1.156.527** (gebouwen **158.459**; machines **73.128**; meubilair/rollend **924.941**); FVA 3.478; current **6.279.943**; inventory 97.331; ST recv **1.101.018** (trade 1.071.383); beleggingen **0**; cash **4.543.480 JUMP** vs 4.060.475 (61% of assets); prepaid 538.113; equity **4.002.165** (was 3.383.797; inbreng 834.116 onbeschikbaar / geplaatst 2.263.050 / niet-opgevraagd 1.428.934 / 90.507 aandelen; reserves 3.119.316); voorzieningen **2.036.349** (pens 1.204.962 + herstelling 801.387 + overige 30.000); schulden **1.401.433** (no LT/bank; ST **1.401.187** waarvan leveranciers 992.592 + tax/soc 265.938; accruals 246); omzet **4.541.212** vs 4.729.340 (6.10 unpublished); othops **5.907.438** vs 5.312.350 waarvan exploitatiesubsidies **5.720.694 JUMP** vs 4.801.697 (jaarverslag bijdragen vennoten **5.198.259** + andere 709.179); goods 757.794; diensten **4.916.314** vs 4.385.311; pers **3.881.316** / **56,7 VTE** / 81.027 uur / YE 60 + uitzend **15 VTE / 715.688**; pensioenkost 624 **434.062**; afschr 360.459; expl **+566.884** vs +23.886; fin opbr 46.821; fin kosten 7.826; tax 13.654; PnL **+592.225** vs +71.314 naar beschikbare reserve; commissaris 11.790. Jaarverslag same PDF: 5 vennoten pop **90.507** (Zaventem 36.670 / Wezembeek-Oppem 14.735 / Kraainem 13.906 / Steenokkerzeel 12.673 / Kampenhout 12.523); AV dec 2025 inbreng-aanpassing volstorting **26.143,75**; bestuurders zitpenningen 36.325,8 + km 659,37 (9503 empty).
- CSVs: sources+4/entities+1/budgets+61/commitments+1/leaderboard+1 + FOI ready `gap_inza_omzet_4_54m_subs_5_72m_diensten_4_92m_l5` (not sent); rq_1381=done; spawn rq_1382; ticks=1381.
- Coverage: residual dual L5 (INTERZA leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1390).
- Next: rq_1382 residual dual L5 VL JR2025 hole_fill (prefer leftover Fluvius Midden-Vlaanderen / INTERGEM KBO 0220.764.971 CDN 2026-00227859 now live; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS CDN 2026-00254280 / Rematics / Sunfin only if taken after leftover IGS/EVA/AGB; leftover APB POA / TPA / De Schorre / Warande / PIH / Inovant / Atlas only if a real PDF downloads; IVAREM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1381 write done")


if __name__ == "__main__":
    main()

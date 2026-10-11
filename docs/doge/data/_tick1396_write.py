# -*- coding: utf-8 -*-
"""Tick 1396 — leftover IGS Pontes JR2025 official NBB WVV euros.
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

TICK = "1396"
UTC = "2026-08-19T04:55:00Z"
ENT = "igs_pnts"
HIER = "Vlaanderen>Antwerpen>IGS>Pontes"
GAP = "gap_pnts_omzet_empty_debt_9_44m_pens_13_43m_l5"
SRC = "src_pnts_jr2025_nbb"
SRC2 = "src_pnts_site"
SRC3 = "src_kbo_pnts_0219473683"
SRC4 = "src_pnts_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00294244.pdf"
SRC2_URL = "https://www.pontes.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0219473683"
SRC4_URL = "https://www.pontes.be/nl/over/publicaties"
FOI_EMAIL = "info@pontes.be"
FOI_POSTAL = "Jules Moretuslei 2 2610 Wilrijk (Antwerpen)"
DRAFT = "docs/doge/foi/drafts/gap_pnts_omzet_empty_debt_9_44m_pens_13_43m_l5.md"
COMM = "comm_pnts_jr2025_pnl"
LB = "lb_pnts_omzet_empty_debt_9_44m_pens_13_43m"

VENNOTEN = (
    "57 gemeenten (stichtende Antwerpen+Mechelen+Turnhout; "
    "arr. Antwerpen 20 / Mechelen 4 / Turnhout 24 / Maaseik 6; "
    "pontes.be/nl/over/bestuursorganen; 3 vestigingen Wilrijk+Turnhout+Lommel)"
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
    ("bud_pnts_assets_2025", "2025", "21976605", "2025 assets 21976605 VKT-kap 20/58; commissaris 21976604.96; tick1396; primary official NBB WVV"),
    ("bud_pnts_assets_2024", "2024", "22229095", "2024 assets 22229095 comparative; tick1396; primary official NBB WVV 20/58"),
    ("bud_pnts_fixed_2025", "2025", "17289894", "2025 vaste activa 17289894 vs 17246428; tick1396; primary official NBB WVV 21/28"),
    ("bud_pnts_iva_2025", "2025", "67545", "2025 IVA 67545 vs 69558; tick1396; primary official NBB WVV 21"),
    ("bud_pnts_mva_2025", "2025", "17216395", "2025 MVA 17216395 vs 17170915; tick1396; primary official NBB WVV 22/27"),
    ("bud_pnts_buildings_2025", "2025", "11625602", "2025 terreinen/gebouwen 11625602 vs 12630820; tick1396; primary official NBB WVV 22"),
    ("bud_pnts_machines_2025", "2025", "3086186", "2025 machines 3086186 JUMP vs 2473408; tick1396; primary official NBB WVV 23"),
    ("bud_pnts_machines_2024", "2024", "2473408", "2024 machines 2473408 comparative; tick1396; primary official NBB WVV 23"),
    ("bud_pnts_furniture_2025", "2025", "196102", "2025 meubilair 196102 vs 274246; tick1396; primary official NBB WVV 24"),
    ("bud_pnts_othmva_2025", "2025", "208480", "2025 overige MVA 208480 unchanged; tick1396; primary official NBB WVV 26"),
    ("bud_pnts_cip_2025", "2025", "2100024", "2025 activa in aanbouw 2100024 vs 1583962; tick1396; primary official NBB WVV 27"),
    ("bud_pnts_cip_2024", "2024", "1583962", "2024 activa in aanbouw 1583962 comparative; tick1396; primary official NBB WVV 27"),
    ("bud_pnts_fva_2025", "2025", "5955", "2025 FVA 5955 vs 5955; tick1396; primary official NBB WVV 28"),
    ("bud_pnts_current_2025", "2025", "4686711", "2025 vlottend 4686711 vs 4982668; tick1396; primary official NBB WVV 29/58"),
    ("bud_pnts_stocks_2025", "2025", "31159", "2025 voorraden 31159 vs 20473; tick1396; primary official NBB WVV 30/36"),
    ("bud_pnts_strecv_2025", "2025", "1542329", "2025 ST vorderingen 1542329 vs 1046261; tick1396; primary official NBB WVV 40/41"),
    ("bud_pnts_trade_2025", "2025", "1257538", "2025 handelsvorderingen 1257538 vs 1042155; tick1396; primary official NBB WVV 40"),
    ("bud_pnts_othrecv_2025", "2025", "284791", "2025 overige vorderingen 284791 JUMP vs 4106; tick1396; primary official NBB WVV 41"),
    ("bud_pnts_invest_2025", "2025", "2500000", "2025 geldbeleggingen 2500000 unchanged; tick1396; primary official NBB WVV 50/53"),
    ("bud_pnts_cash_2025", "2025", "570825", "2025 liquide middelen 570825 DROP vs 1263658; tick1396; primary official NBB WVV 54/58"),
    ("bud_pnts_cash_2024", "2024", "1263658", "2024 liquide middelen 1263658 comparative; tick1396; primary official NBB WVV 54/58"),
    ("bud_pnts_prepaid_2025", "2025", "42398", "2025 overlopend actief 42398 vs 152275; tick1396; primary official NBB WVV 490/1"),
    ("bud_pnts_equity_2025", "2025", "12532417", "2025 EV 12532417 vs 12534432; tick1396; primary official NBB WVV 10/15"),
    ("bud_pnts_capital_2025", "2025", "4840960", "2025 geplaatst kapitaal 4840960; KBO kapitaal 5287360; tick1396; primary official NBB WVV 100"),
    ("bud_pnts_reval_2025", "2025", "838917", "2025 herwaarderingsmeerwaarden 838917 unchanged; tick1396; primary official NBB WVV 12"),
    ("bud_pnts_reserves_2025", "2025", "1874148", "2025 reserves 1874148 (wettelijk 214020 / andere onbesch 226161 / beschikbaar 1433967); tick1396; primary official NBB WVV 13"),
    ("bud_pnts_re_2025", "2025", "3314288", "2025 overgedragen winst 3314288 vs 3228376; tick1396; primary official NBB WVV 14"),
    ("bud_pnts_capsub_2025", "2025", "1664103", "2025 kapitaalsubsidies 1664103 vs 1752031; tick1396; primary official NBB WVV 15"),
    ("bud_pnts_debt_2025", "2025", "9444188", "2025 schulden 9444188 vs 9694663; tick1396; primary official NBB WVV 17/49"),
    ("bud_pnts_debt_2024", "2024", "9694663", "2024 schulden 9694663 comparative; tick1396; primary official NBB WVV 17/49"),
    ("bud_pnts_lt_2025", "2025", "6249222", "2025 LT bank 6249222 vs 7155098; tick1396; primary official NBB WVV 17"),
    ("bud_pnts_st_2025", "2025", "3194966", "2025 ST schulden 3194966 vs 2520037; tick1396; primary official NBB WVV 42/48"),
    ("bud_pnts_ltdue_2025", "2025", "936819", "2025 LT-due binnen jaar 936819 vs 931456; tick1396; primary official NBB WVV 42"),
    ("bud_pnts_sttrade_2025", "2025", "1524037", "2025 leveranciers 1524037 JUMP vs 922327; tick1396; primary official NBB WVV 440/4"),
    ("bud_pnts_sttax_2025", "2025", "162695", "2025 belastingschulden 162695 vs 128637; tick1396; primary official NBB WVV 450/3"),
    ("bud_pnts_stsoc_2025", "2025", "571414", "2025 bezoldigingen/sociale lasten 571414 vs 537617; tick1396; primary official NBB WVV 454/9"),
    ("bud_pnts_govguar_2025", "2025", "7083689", "2025 overheidswaarborg 7083689 (LT+due); tick1396; primary official NBB WVV 9061"),
    ("bud_pnts_debt15_2025", "2025", "2959656", "2025 schuld 1-5y 2959656; tick1396; primary official NBB WVV 8912"),
    ("bud_pnts_debt5y_2025", "2025", "3289567", "2025 schuld >5y 3289567; tick1396; primary official NBB WVV 8913"),
    ("bud_pnts_pens_off_2025", "2025", "13430000", "2025 off-balance pensioen 13.43m (responsabilisering 10.33m + post-2049 3.10m); commissaris voorbehoud EV overstated 13.4m; tick1396; primary official NBB WVV 6.5"),
    ("bud_pnts_pens_resp_2025", "2025", "10330000", "2025 responsabiliseringsbijdrage remaining 10.33m off-balance; tick1396; primary official NBB WVV 6.5"),
    ("bud_pnts_pens_post_2025", "2025", "3100000", "2025 statutaire pensioenlast na 2049 3.10m off-balance; tick1396; primary official NBB WVV 6.5"),
    ("bud_pnts_sw_contract_2025", "2025", "1195000", "2025 software/hardware contract 1195000 / 35 months; tick1396; primary official NBB WVV 6.5"),
    ("bud_pnts_brutomarge_2025", "2025", "6811317", "2025 brutomarge 6811317 vs 6572228; omzet 70 empty; tick1396; primary official NBB WVV 9900"),
    ("bud_pnts_brutomarge_2024", "2024", "6572228", "2024 brutomarge 6572228 comparative; tick1396; primary official NBB WVV 9900"),
    ("bud_pnts_pers_2025", "2025", "4855276", "2025 pers 4855276 vs 4490340 / 43.3 VTE; tick1396; primary official NBB WVV 62"),
    ("bud_pnts_pers_2024", "2024", "4490340", "2024 pers 4490340 / 37.4 VTE comparative; tick1396; primary official NBB WVV 62"),
    ("bud_pnts_afschr_2025", "2025", "1229264", "2025 afschr 1229264 vs 1467676; tick1396; primary official NBB WVV 630"),
    ("bud_pnts_wv_2025", "2025", "256567", "2025 WV voorraden/vorderingen 256567 vs 48556; tick1396; primary official NBB WVV 631/4"),
    ("bud_pnts_othcost_2025", "2025", "8923", "2025 andere bedrijfskosten 8923 vs 4669; tick1396; primary official NBB WVV 640/8"),
    ("bud_pnts_nrec_2025", "2025", "287301", "2025 niet-recurrente bedrijfskosten 287301 vs 5442; tick1396; primary official NBB WVV 66A"),
    ("bud_pnts_expl_2025", "2025", "173986", "2025 expl +173986 vs +555544; tick1396; primary official NBB WVV 9901"),
    ("bud_pnts_expl_2024", "2024", "555544", "2024 expl +555544 comparative; tick1396; primary official NBB WVV 9901"),
    ("bud_pnts_fininc_2025", "2025", "100124", "2025 financiele opbrengsten 100124 vs 133516 (capsub 87928); tick1396; primary official NBB WVV 75"),
    ("bud_pnts_capsub_inc_2025", "2025", "87928", "2025 kapitaal- en interestsubsidies 87928 vs 123995; tick1396; primary official NBB WVV 753"),
    ("bud_pnts_fincost_2025", "2025", "184328", "2025 financiele kosten 184328 vs 203718; tick1396; primary official NBB WVV 65"),
    ("bud_pnts_tax_2025", "2025", "3869", "2025 belastingen 3869 vs 2547; tick1396; primary official NBB WVV 67/77"),
    ("bud_pnts_pnl_2025", "2025", "85913", "2025 PnL +85913 vs +482795 all overgedragen; commissaris 85912.59; tick1396; primary official NBB WVV 9904"),
    ("bud_pnts_pnl_2024", "2024", "482795", "2024 PnL +482795 comparative; tick1396; primary official NBB WVV 9904"),
    ("bud_pnts_div_2025", "2025", "0", "2025 dividend 694 empty; tick1396; primary official NBB WVV 694"),
    ("bud_pnts_capex_mva_2025", "2025", "1544513", "2025 MVA aanschaf 1544513 (8169); tick1396; primary official NBB WVV 6.1.2"),
    ("bud_pnts_capex_iva_2025", "2025", "15519", "2025 IVA aanschaf 15519 (8029); tick1396; primary official NBB WVV 6.1.1"),
    ("bud_pnts_comm_2025", "2025", "14526", "2025 commissaris CVT 14526 excl btw + extra 2250 + 1126; tick1396; primary official NBB WVV 6.6"),
    ("bud_pnts_board_2025", "2025", "31201", "2025 bestuurders presentiegeld table sum 31200.70; tick1396; primary official NBB WVV remuneratieverslag"),
    ("bud_pnts_resp_cash_2025", "2025", "366000", "2025 responsabiliseringsbijdrage circa 366000 in 62; commissaris; tick1396; primary official NBB WVV commissarisverslag"),
]


def main() -> None:
    step = sys.argv[1] if len(sys.argv) > 1 else "all"

    if step in ("all", "sources"):
        n = append_rows(
            DATA / "sources.csv",
            [
                {
                    "source_id": SRC,
                    "title": "IGS Pontes jaarrekening boekjaar 2025 (official NBB WVV VKT-kap deposit 2026-00294244; AV 25.06.2026)",
                    "url": SRC_URL,
                    "publisher": "IGS Pontes / NBB WVV deposit",
                    "accessed_date": "2026-08-19",
                    "source_class": "budget",
                    "notes": (
                        "tick1396; official NBB VKT-kap PDF 1.15MB 43p deposit 2026-00294244 header 15.07.2026 created 15.07.2026; "
                        "leftover IGS crematorium 57 gemeenten Wilrijk/Turnhout/Lommel; "
                        "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                        "Belscope/Companyweb extracted tables not used; Staatsbladmonitor table euros not used; "
                        "commissaris Callens Vandelanotte Theunissen BV B00003 / 0427.897.088 / Yvan Willems A02616 signed 28.04.2026 oordeel met voorbehoud assets 21976604.96 / PnL 85912.59; "
                        "omzet 70 empty; 60/61 empty; only brutomarge published; 6.6 related empty except commissaris"
                    ),
                },
                {
                    "source_id": SRC2,
                    "title": "IGS Pontes official site (leftover crematorium IGS 57 gemeenten; vestigingen Wilrijk Turnhout Lommel)",
                    "url": SRC2_URL,
                    "publisher": "IGS Pontes",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1396; leftover crematorium IGS of 57 Antwerpen/Mechelen/Turnhout/Maaseik municipalities; "
                        "site quote IGS bestaande uit 57 aangesloten steden en gemeenten; statutory 2025 balans is the NBB CDN deposit"
                    ),
                },
                {
                    "source_id": SRC3,
                    "title": "KBO IGS Pontes 0219.473.683",
                    "url": SRC3_URL,
                    "publisher": "KBO Public Search FOD Economie",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1396; KBO 0219.473.683 Actief / normale toestand since 14.02.1979; "
                        "statutaire naam Pontes since 16.10.2013; "
                        "Opdrachthoudende vereniging (Vlaams Gewest) since 08.08.1998; "
                        "zetel Jules Moretuslei 2 2610 Antwerpen since 08.08.1998; 3 VE; "
                        "KBO no email/web/tel; official site https://www.pontes.be/; "
                        "btw since 01.07.1979; RSZ since 01.01.2022; NACE 96.302; aanbestedende overheid since 14.02.1979; "
                        "KBO kapitaal 5287360; 15 bestuurders; KBO stand 18.08.2026"
                    ),
                },
                {
                    "source_id": SRC4,
                    "title": "IGS Pontes FOI channel / official publicaties (info@pontes.be; +32 3 828 95 60)",
                    "url": SRC4_URL,
                    "publisher": "IGS Pontes",
                    "accessed_date": "2026-08-19",
                    "source_class": "official_register",
                    "notes": (
                        "tick1396; site contact info@pontes.be; tel +32 3 828 95 60; "
                        "voorzitter Carine Leys; algemeen directeur Tom Wustenberghs; "
                        "inzage besluiten binnen 15 dagen via info@pontes.be"
                    ),
                },
            ],
        )
        print("sources", n)

    if step in ("all", "entities"):
        n = append_rows(
            DATA / "entities.csv",
            [
                {
                    "entity_id": ENT,
                    "name_nl": "IGS Pontes (Opdrachthoudende Vereniging Pontes; leftover IGS crematorium Wilrijk/Turnhout/Lommel; 57 gemeenten)",
                    "name_fr": "IGS Pontes (association missionnee crematorium Wilrijk/Turnhout/Lommel; IGS residuel)",
                    "name_en": "IGS Pontes leftover IGS crematorium Wilrijk Turnhout Lommel 57 municipalities",
                    "level": "other",
                    "parent_id": "sec_flanders",
                    "community_language": "nl",
                    "website": "https://www.pontes.be/",
                    "foi_email": FOI_EMAIL,
                    "foi_postal": FOI_POSTAL,
                    "notes": (
                        "tick1396 leftover residual IGS Pontes crematorium IGS; "
                        "KBO 0219.473.683 Actief since 14.02.1979; official NBB WVV VKT-kap PDF downloads; "
                        "sourced euros assets 21976605 omzet empty diensten empty pers 4855276 debt 9444188 pnl 85913 equity 12532417 capex 1544513 pens 13430000; "
                        "FOI ready omzet empty / 60-61 empty / 9.44m debt / 13.43m pens / 1.54m capex; "
                        "distinct from already-mined IGS Hofheide 1395 prefix hofh and IGS Westlede 1394 prefix wstl and HAVICREM 1393 prefix hvic and IVLA 1392 / Fluvius stack 1382-1391"
                    ),
                },
            ],
        )
        print("entities", n)

    if step in ("all", "budgets"):
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

    if step in ("all", "commitments"):
        n = append_rows(
            DATA / "commitments.csv",
            [
                {
                    "commitment_id": COMM,
                    "title": "IGS Pontes JR2025 leftover IGS dual (assets 21.98m / omzet empty / debt 9.44m / pens 13.43m / PnL +86k)",
                    "entity_id": ENT,
                    "beneficiary": "IGS Pontes / " + VENNOTEN,
                    "legal_basis": "WVV OV; Decreet Lokaal Bestuur; NBB neerlegging",
                    "decision_date": "2026-06-25",
                    "start_year": "1979",
                    "end_year": "",
                    "total_envelope_eur": "9444188",
                    "cash_by_year": "",
                    "remaining_eur": "",
                    "status": "active",
                    "evaluation_url": SRC_URL,
                    "stated_goal": "Local leftover IGS map VL crematorium Antwerpen/Turnhout/Lommel — omzet unpublished / 9.44m bank / 13.43m pens off-balance / 1.54m capex / PnL +86k",
                    "cut_option": "Publish omzet + 60/61 split + 9.44m bank counterparties/terms + 13.43m pensioen voorziening + 1.54m capex tender; do not keep crematorium IGS as dual unpublished vehicle",
                    "source_id": SRC,
                    "confidence": "strong",
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "notes": "tick1396; assets 21976605 omzet empty diensten empty pers 4855276 debt 9444188 pnl 85913 equity 12532417 capex 1544513 pens 13430000; FOI ready not sent; not TE-additive of 348bn",
                }
            ],
        )
        print("commitments", n)

    if step in ("all", "leaderboard"):
        n = append_rows(
            DATA / "leaderboard.csv",
            [
                {
                    "item_id": LB,
                    "name": "IGS Pontes JR2025 leftover IGS: assets 21.98m / omzet empty / debt 9.44m / pens 13.43m / 43.3 VTE",
                    "level": "L5",
                    "type": "local_budget_line",
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "annual_cost_eur": "4855276",
                    "total_cost_eur": "9444188",
                    "tco_notes": (
                        "Leftover dual IGS crematorium 57 municipalities (Wilrijk/Turnhout/Lommel): "
                        "assets 21.98m / equity 12.53m / pnl +86k / omzet unpublished / 60-61 unpublished / "
                        "diensten unpublished / pers 4.86m / 43.3 VTE / "
                        "debt 9.44m (LT bank 6.25m; gov-guaranteed 7.08m) / cash 571k DROP / capex 1.54m / "
                        "off-balance pens 13.43m (qualified audit EV overstated 13.4m); "
                        "official NBB WVV live; do not treat 9.44m as TE-additive of 348bn"
                    ),
                    "confidence": "strong",
                    "source_id": SRC,
                    "beneficiaries": "IGS Pontes / " + VENNOTEN,
                    "stated_goal": "Local leftover IGS map VL crematorium Antwerpen/Turnhout/Lommel — JR2025 live; dual omzet/debt/pens FOI",
                    "measured_outcome": "Official NBB WVV 2026-08-19: assets 21.98m / omzet empty / debt 9.44m / pens 13.43m / pnl +86k / 43.3 VTE / qualified audit",
                    "absurdity_score": "7.0",
                    "cost_score": "6.5",
                    "difficulty": "3.0",
                    "priority_index": "6.3",
                    "cut_proposal": "Publish omzet + 60/61 split + 9.44m bank counterparties/terms + 13.43m pensioen voorziening + 1.54m capex tender; do not keep crematorium IGS as dual unpublished vehicle",
                    "status": "active",
                    "struck_reason": "",
                    "notes": "tick1396; leftover IGS Pontes crematorium IGS; FOI ready not sent; not TE-additive of 348bn; distinct from IGS Hofheide 1395 and IGS Westlede 1394 and HAVICREM 1393 and IVLA 1392 / Fluvius stack 1382-1391",
                }
            ],
        )
        print("leaderboard", n)

    if step in ("all", "foi"):
        n = append_rows(
            DATA / "foi_queue.csv",
            [
                {
                    "gap_id": GAP,
                    "hierarchy_path": HIER + ">JR2025_L5",
                    "entity_id": ENT,
                    "what_is_missing": (
                        "omzet WVV 70 empty + 60/61 empty (abbreviated VKT; only brutomarge 6811317 vs 6572228 published) per stroom/vestiging/vennoot unpublished "
                        "+ schulden 9444188 vs 9694663 (LT bank 6249222 + ST due 936819; gov-guaranteed 7083689; 4 IRS ING) counterparties/terms unpublished "
                        "+ off-balance pensioen 13430000 (responsabilisering 10330000 + post-2049 3100000; commissaris voorbehoud EV overstated 13.4m) "
                        "+ machines 3086186 JUMP vs 2473408 / MVA aanschaf 1544513 / CIP 2100024 tender/unit price unpublished "
                        "+ niet-recurrent 287301 nature unpublished "
                        "+ software/hardware contract 1195000 / 35m opdrachtnemer unpublished "
                        "+ pers 4855276 / 43.3 VTE / 71238 uur split unpublished "
                        "+ 6.6 related empty + dividend 694 empty"
                    ),
                    "why_it_matters": (
                        "Leftover IGS crematorium of 57 mined Antwerpen/Mechelen/Turnhout/Maaseik municipalities "
                        "(distinct from IGS Hofheide 1395 and IGS Westlede 1394 and HAVICREM 1393 and from IVLA 1392 / Fluvius 1382-1391): "
                        "21.98m assets / omzet unpublished / 60-61 unpublished / 9.44m bank / 13.43m pens off-balance / qualified audit / 1.54m capex / "
                        "abbreviated VKT hides omzet and diensten "
                        "is a dual opacity residual, not TE-additive of 348bn."
                    ),
                    "priority": "8",
                    "recipient_body": "IGS Pontes / Raad van Bestuur / Carine Leys / Tom Wustenberghs / 57 vennoten",
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
                        "tick1396 leftover IGS crematorium 57 gemeenten after honest hunt; "
                        "live JR2025 official NBB WVV VKT-kap PDF now extracted (1.15MB 43p deposit 2026-00294244). "
                        "IGS Hofheide already mined 1395 — skipped. IGS Westlede already mined 1394 — skipped. HAVICREM already mined 1393 — skipped. IVLA already mined 1392 — skipped. Fluvius stack already mined 1382-1391 — skipped. "
                        "Leftover AGB/zorg/EVA/APB next if a 2025 PDF downloads. Dommelhof leftover next if a JR2025 PDF now downloads. "
                        "Otary RS Nuhma-adjacent fallback not taken. "
                        "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                    ),
                }
            ],
        )
        print("foi", n)

    if step in ("all", "rq"):
        rq_new = {
            "task_id": "rq_1396",
            "title": "IGS Pontes JR2025 leftover dual residual",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "done",
            "hierarchy_target": "L5",
            "entity_id": ENT,
            "instructions": (
                "Completed: IGS Pontes leftover IGS crematorium of 57 Antwerpen/Mechelen/Turnhout/Maaseik municipalities after honest hunt; "
                "KBO 0219.473.683 Actief; live JR2025 official NBB WVV VKT-kap PDF (1.15MB 43p deposit 2026-00294244; commissaris CVT oordeel met voorbehoud); "
                "sourced euros assets 21976605 / omzet empty / diensten empty / pers 4855276 / debt 9444188 / pnl 85913 / capex 1544513 / pens 13430000; "
                "FOI ready omzet empty / 60-61 empty / 9.44m debt / 13.43m pens / 1.54m capex"
            ),
            "blocked_gap_id": GAP,
            "created_utc": "2026-08-19T04:40:00Z",
            "updated_utc": UTC,
            "notes": (
                "tick1396 IGS Pontes leftover IGS crematorium residual; KBO 0219.473.683; "
                "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1397 residual dual L5 VL"
            ),
        }
        rq_spawn = {
            "task_id": "rq_1397",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
                "(prior 1255-1396 done including IGS Pontes 1396 leftover crematorium IGS live NBB WVV / "
                "IGS Hofheide 1395 leftover crematorium IGS live NBB WVV / "
                "IGS Westlede 1394 leftover crematorium IGS live NBB WVV / "
                "HAVICREM 1393 leftover crematorium IGS live NBB WVV / "
                "IVLA 1392 leftover waste IGS live NBB WVV / "
                "Fluvius OV 1391 leftover personnel OV live NBB WVV); "
                "leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; "
                "other leftover IGS/crematoria only if a DISTINCT unmined entity has a live 2025 PDF; "
                "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
                "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
                "skip already-mined IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / ILvA 1344; "
                "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
                "ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick1396 after IGS Pontes leftover crematorium IGS live NBB WVV; next residual dual L5 VL",
        }
        found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1396", rq_new, rq_spawn)
        print("research_queue 1396", found, "spawned_1397", spawned)

    if step in ("all", "state"):
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
                    "last_unit_id": "rq_1396",
                    "ticks_completed": "1396",
                    "paused": "no",
                    "notes": (
                        "tick1396 IGS Pontes leftover IGS crematorium residual; KBO 0219.473.683; "
                        "live JR2025 NBB WVV PDF; sourced euros assets 21976605 omzet empty diensten empty pers 4855276 debt 9444188 pnl 85913 equity 12532417 capex 1544513 pens 13430000; "
                        "FOI ready omzet-empty/9.44m debt/13.43m pens/1.54m capex; next rq_1397 residual dual L5 VL; continuous hole_fill"
                    ),
                }
            )
        print("loop_state ok")

    if step in ("all", "log"):
        log = ROOT / "loop_log.md"
        entry = (
            "### Tick 1396 - 2026-08-19 - rq_1396 IGS Pontes dual residual leftover\n"
            "- Unit: IGS Pontes / Opdrachthoudende Vereniging Pontes (leftover IGS opdrachthoudende vereniging / crematorium of 57 mined Antwerpen/Mechelen/Turnhout/Maaseik municipalities; vestigingen Wilrijk + Turnhout + Lommel) after residual dual hunt (KBO **0219.473.683**; official pontes.be has 57 gemeenten + 3 vestigingen + publicaties; live NBB WVV VKT-kap deposit **2026-00294244** PDF 1.15MB / 43p; AV **25.06.2026**; header **15.07.2026**; created **15.07.2026**; commissaris Callens, Vandelanotte & Theunissen BV B00003 / 0427.897.088 / Yvan Willems A02616 signed 28.04.2026 **oordeel met voorbehoud** assets 21.976.604,96 / PnL +85.912,59; fee 14.526 + extra 2.250 + 1.126). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; preferred leftover Pontes with live CDN this tick). Distinct from already-mined IGS Hofheide 1395 (prefix `hofh`) and IGS Westlede 1394 (prefix `wstl`) and HAVICREM 1393 (prefix `hvic`) and from IVLA 1392 / Fluvius stack 1382-1391. First confirmed not already mined: no Pontes / 0219.473.683 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **14.02.1979**; statutaire naam Pontes since 16.10.2013; Opdrachthoudende vereniging (Vlaams Gewest) since 08.08.1998; zetel Jules Moretuslei 2 2610 Antwerpen since 08.08.1998; **3 VE**; KBO no email/web/tel; official site https://www.pontes.be/; btw since 01.07.1979; RSZ since 01.01.2022; NACE 96.302; KBO kapitaal 5.287.360. Voorzitter Carine Leys since 06.2014 / herkozen 26.03.2025-03.2031; algemeen directeur Tom Wustenberghs (remuneratieverslag). Contact info@pontes.be; tel +32 3 828 95 60. Hunt leftover Pontes first: statutory CDN live this tick (HTTP 200 / 1153968 / 43p) — taken. IGS Hofheide already mined 1395 — skipped. IGS Westlede already mined 1394 — skipped. HAVICREM already mined 1393 — skipped. IVLA already mined 1392 — skipped. Fluvius stack already mined 1382-1391 — skipped. Leftover AGB/zorg/EVA/APB not taken once live Pontes extracted. Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live Pontes extracted. Otary RS Nuhma-adjacent fallback not taken. NBB consult skipped (403/SPA); euros extracted from the official VKT-kap deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used (1 euro rounding vs form). Not every-10 (next 1400).\n"
            "- EUR strong (primary official WVV VKT-kap; **omzet 70 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; 6.2/6.7/6.9/7/8/9/10/14-17 not filed; 6.6 related empty except commissaris; commissaris **oordeel met voorbehoud**): assets **21.976.605** (was 22.229.095; commissaris 21.976.604,96); fixed **17.289.894** / MVA **17.216.395** (gebouwen **11.625.602**; machines **3.086.186 JUMP** vs 2.473.408; meubilair **196.102**; overige **208.480**; CIP **2.100.024**); IVA 67.545; FVA **5.955**; current **4.686.711**; voorraden **31.159**; ST recv **1.542.329** (trade 1.257.538 / other **284.791 JUMP** vs 4.106); geldbeleggingen **2.500.000**; cash **570.825 DROP** vs 1.263.658; prepaid 42.398; equity **12.532.417** (kapitaal 4.840.960; herwaardering 838.917; reserves 1.874.148; overgedragen 3.314.288; capsub **1.664.103**); voorzieningen empty; schulden **9.444.188** (LT bank **6.249.222**; ST **3.194.966** waarvan LT-due **936.819** + leveranciers **1.524.037 JUMP** vs 922.327 + tax 162.695 + soc 571.414; gov-guaranteed **7.083.689**; debt 1-5y 2.959.656 / >5y 3.289.567); brutomarge **6.811.317** vs 6.572.228; omzet 70 empty; 60/61 empty; pers **4.855.276** / **43,3 VTE** / 71.238 uur / YE 47,9 (36 VT + 16 DT; all onbepaald; in 13,9 / uit 4,8); afschr 1.229.264; WV 256.567; niet-recurrent 66A **287.301**; expl **+173.986** vs +555.544; fin opbr 100.124 (capsub 87.928); fin kosten 184.328; tax 3.869; PnL **+85.913** vs +482.795 all overgedragen; dividend **0** (694 empty); capex MVA aanschaf **1.544.513** + IVA 15.519; off-balance pensioen **13,43m** (responsabilisering 10,33m + post-2049 3,10m; commissaris EV overstated 13,4m; 2025 responsabilisering ~366.000 in 62); software/hardware **1.195.000** / 35m; 4 IRS ING; commissaris 14.526; bestuurders presentiegeld **31.200,70**. Vennoten: 57 gemeenten (pontes.be/nl/over/bestuursorganen).\n"
            "- CSVs: sources+4/entities+1/budgets+65/commitments+1/leaderboard+1 + FOI ready `gap_pnts_omzet_empty_debt_9_44m_pens_13_43m_l5` (not sent); rq_1396=done; spawn rq_1397; ticks=1396.\n"
            "- Coverage: residual dual L5 (IGS Pontes leftover crematorium IGS live WVV). Does **not** move L5 near-complete of EUR 347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs gemeente funeral fees possible. No progress refresh (not every-10; next 1400).\n"
            "- Next: rq_1397 residual dual L5 VL JR2025 hole_fill (prefer leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover Nuhma daughters Otary RS only after leftover IGS/EVA/AGB; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius OV 1391 / Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / ILvA 1344 / Haviland 1370).\n"
        )
        with log.open("a", encoding="utf-8") as f:
            f.write(entry)
        print("loop_log ok")
    print("tick1396 write", step, "done")


if __name__ == "__main__":
    main()

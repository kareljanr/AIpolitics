# -*- coding: utf-8 -*-
"""Tick 1357 — leftover IGS EcoWerf JR2025 official NBB WVV euros.
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

TICK = "1357"
UTC = "2026-08-19T02:15:00Z"
ENT = "igs_ecow"
HIER = "Vlaanderen>VlaamsBrabant>IGS>EcoWerf>Afval"
GAP = "gap_ecow_omzet_53_57m_pers_25_80m_pnl_neg_l5"
SRC = "src_ecow_jr2025_nbb"
SRC2 = "src_ecow_site"
SRC3 = "src_kbo_ecow_0862492920"
SRC4 = "src_ecow_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00256489.pdf"
SRC2_URL = "https://www.ecowerf.be/jaarverslagen"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0862492920"
SRC4_URL = "https://www.ecowerf.be/contact"
FOI_EMAIL = "info@ecowerf.be"
FOI_POSTAL = "Aarschotsesteenweg 210 3012 Leuven (Wilsele)"
DRAFT = "docs/doge/foi/drafts/gap_ecow_omzet_53_57m_pers_25_80m_pnl_neg_l5.md"
COMM = "comm_ecow_jr2025_omzet"
LB = "lb_ecow_omzet_53_57m_pers_25_80m_pnl_neg"


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
                "title": "EcoWerf jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00256489; AV 24.06.2026)",
                "url": SRC_URL,
                "publisher": "EcoWerf / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1357; official NBB VOL-inb PDF 928kB 64p deposit 2026-00256489 neerlegging SBM 07.07.2026 header 25.06.2026; "
                    "leftover IGS waste of mined Oost-Brabant cities + leftover Holsbeek/Boutersem/Bierbeek; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; official site statutory still unpublished"
                ),
            },
            {
                "source_id": SRC2,
                "title": "EcoWerf official jaarverslagen page (glossy 2025 live; statutory jaarrekening still unpublished)",
                "url": SRC2_URL,
                "publisher": "EcoWerf",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1357; leftover IGS of mined Oost-Brabant; "
                    "jaarverslag 2025 glossy 16MB listed; jaarrekening+commissaris 'wordt weldra gepubliceerd'; "
                    "glossy narrative omzet 52.004m / 420 staff does NOT match statutory 53571356 / 439 YE"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO EcoWerf 0862.492.920",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1357; KBO 0862.492.920 Actief / normale toestand since 07.01.2004; "
                    "statutaire naam EcoWerf Intergemeentelijk Milieubedrijf Oost-Brabant since 15.12.2003; "
                    "OV since 07.01.2004; zetel Aarschotsesteenweg 210 3012 Leuven since 15.12.2003; 29 VE; "
                    "aanbestedende overheid since 15.12.2003; btw since 01.01.2004; RSZ since 01.01.2022; "
                    "jaarvergadering juni; 17 functiehouders; NACE 38.330/38.110"
                ),
            },
            {
                "source_id": SRC4,
                "title": "EcoWerf FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "EcoWerf",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1357; FOI info@ecowerf.be; 016 28 43 00 / 0800 97 0 97; "
                    "Aarschotsesteenweg 210 3012 Leuven (Wilsele); commissaris RSM Inter Audit / Van Heghe Sara"
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
                "name_nl": "EcoWerf (leftover IGS Oost-Brabant / Intergemeentelijk Milieubedrijf)",
                "name_fr": "EcoWerf (IGS residuel Brabant flamand oriental / dechets)",
                "name_en": "EcoWerf leftover Oost-Brabant intermunicipal waste IGS",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.ecowerf.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1357 leftover residual IGS waste of mined Oost-Brabant cities + leftover Holsbeek/Boutersem/Bierbeek; "
                    "KBO 0862.492.920 Actief since 07.01.2004; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 46.228m / omzet 53.571m / pers 25.796m / pnl -0.030m; "
                    "FOI ready per-vennoot/6.10/glossy-recon/site-JR"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_ecow_assets_2025", ENT, "2025", "46228354", "2025 assets 46228354 VOL-inb 20/58; tick1357; primary official NBB WVV"),
        ("bud_ecow_assets_2024", ENT, "2024", "45283091", "2024 assets 45283091 comparative; tick1357; primary official NBB WVV 20/58"),
        ("bud_ecow_pnl_2025", ENT, "2025", "-30175", "2025 PnL 9904 -30175; tick1357; primary official NBB WVV + commissaris RSM"),
        ("bud_ecow_pnl_2024", ENT, "2024", "485129", "2024 PnL 9904 485129 comparative; tick1357; primary official NBB WVV"),
        ("bud_ecow_fixed_2025", ENT, "2025", "33407479", "2025 vaste activa 33407479; tick1357; primary official NBB WVV 21/28"),
        ("bud_ecow_current_2025", ENT, "2025", "12820875", "2025 vlottende activa 12820875 DROP vs 13179837; tick1357; primary official NBB WVV 29/58"),
        ("bud_ecow_equity_2025", ENT, "2025", "13831009", "2025 eigen vermogen 13831009; tick1357; primary official NBB WVV 10/15"),
        ("bud_ecow_equity_2024", ENT, "2024", "13642361", "2024 eigen vermogen 13642361 comparative; tick1357; primary official NBB WVV 10/15"),
        ("bud_ecow_inbreng_2025", ENT, "2025", "4197034", "2025 inbreng 4197034 JUMP vs 3714644 (kapitaalsverhoging 482390 = 1 EUR/inwoner); tick1357; primary official NBB WVV 10/11"),
        ("bud_ecow_reserves_2025", ENT, "2025", "6112794", "2025 reserves 6112794; tick1357; primary official NBB WVV 13"),
        ("bud_ecow_subsidy_2025", ENT, "2025", "2577404", "2025 kapitaalsubsidies 2577404; tick1357; primary official NBB WVV 15"),
        ("bud_ecow_mva_2025", ENT, "2025", "32901026", "2025 MVA 32901026 (gebouwen 14821277 + machines 7700746 + rollend 7925097 + CIP 2453908); tick1357; primary official NBB WVV 22/27"),
        ("bud_ecow_cip_2025", ENT, "2025", "2453908", "2025 activa in aanbouw 2453908 JUMP vs 619420; tick1357; primary official NBB WVV 27"),
        ("bud_ecow_fva_2025", ENT, "2025", "506453", "2025 FVA 506453 (verbonden EcoWerf Energie 500000); tick1357; primary official NBB WVV 28"),
        ("bud_ecow_stock_2025", ENT, "2025", "1074627", "2025 voorraden 1074627; tick1357; primary official NBB WVV 30/36"),
        ("bud_ecow_strecv_2025", ENT, "2025", "7061111", "2025 ST vorderingen 7061111 (trade 4817780 + other 2243331); tick1357; primary official NBB WVV 40/41"),
        ("bud_ecow_cash_2025", ENT, "2025", "3473097", "2025 liquide middelen 3473097 JUMP vs 2774496; tick1357; primary official NBB WVV 54/58"),
        ("bud_ecow_cash_2024", ENT, "2024", "2774496", "2024 liquide middelen 2774496 comparative; tick1357; primary official NBB WVV 54/58"),
        ("bud_ecow_prov_2025", ENT, "2025", "3587359", "2025 voorzieningen 3587359 (pensioen 848797 + herstelling 2661330 + overige 77232); tick1357; primary official NBB WVV 16"),
        ("bud_ecow_debt_2025", ENT, "2025", "28809986", "2025 schulden 28809986; tick1357; primary official NBB WVV 17/49"),
        ("bud_ecow_lt_2025", ENT, "2025", "12177345", "2025 LT schulden 12177345 all kredietinstellingen; tick1357; primary official NBB WVV 17"),
        ("bud_ecow_st_2025", ENT, "2025", "16628906", "2025 ST schulden 16628906 (LT-within-year 2383549 + fin 800000 + trade 8693597 + tax/soc 4501290 + other 249360); tick1357; primary official NBB WVV 42/48"),
        ("bud_ecow_omzet_2025", ENT, "2025", "53571356", "2025 omzet 53571356 JUMP vs 48514571 (no 6.10 split; glossy 52.004m mismatch); tick1357; primary official NBB WVV 70"),
        ("bud_ecow_omzet_2024", ENT, "2024", "48514571", "2024 omzet 48514571 comparative; tick1357; primary official NBB WVV 70"),
        ("bud_ecow_opsrev_2025", ENT, "2025", "55422064", "2025 bedrijfsopbrengsten 55422064 (omzet 53571356 + andere 1701018 + nr 149690); tick1357; primary official NBB WVV 70/76A"),
        ("bud_ecow_opscost_2025", ENT, "2025", "55443914", "2025 bedrijfskosten 55443914; tick1357; primary official NBB WVV 60/66A"),
        ("bud_ecow_diensten_2025", ENT, "2025", "19306658", "2025 diensten 19306658 JUMP vs 17528291; tick1357; primary official NBB WVV 61"),
        ("bud_ecow_goods_2025", ENT, "2025", "4560174", "2025 handelsgoederen/grondstoffen 4560174; tick1357; primary official NBB WVV 60"),
        ("bud_ecow_pers_2025", ENT, "2025", "25796282", "2025 personeelskosten 25796282 / avg VTE 403.6 / YE 439 koppen 402.7 VTE; tick1357; primary official NBB WVV 62 / 1023"),
        ("bud_ecow_pers_2024", ENT, "2024", "23202558", "2024 personeelskosten 23202558 / avg VTE 382.5 comparative; tick1357; primary official NBB WVV 62"),
        ("bud_ecow_expl_2025", ENT, "2025", "-21850", "2025 bedrijfsverlies -21850 DROP vs +415408; tick1357; primary official NBB WVV 9901"),
        ("bud_ecow_expl_2024", ENT, "2024", "415408", "2024 bedrijfswinst 415408 comparative; tick1357; primary official NBB WVV 9901"),
        ("bud_ecow_fininc_2025", ENT, "2025", "399153", "2025 financiele opbrengsten 399153 (kapitaalsubsidies 372237); tick1357; primary official NBB WVV 75/76B"),
        ("bud_ecow_fincost_2025", ENT, "2025", "407477", "2025 financiele kosten 407477 (schulden 378360); tick1357; primary official NBB WVV 65/66B"),
        ("bud_ecow_afschr_2025", ENT, "2025", "5472570", "2025 afschrijvingen 5472570; tick1357; primary official NBB WVV 630"),
        ("bud_ecow_invest_2025", ENT, "2025", "6784088", "2025 MVA investeringen 6784087.93 (bestuursverslag); tick1357; primary official NBB WVV 6.3"),
        ("bud_ecow_uitzend_2025", ENT, "2025", "436116", "2025 uitzend 436116 / 5.1 VTE; tick1357; primary official NBB WVV 617"),
        ("bud_ecow_subs740_2025", ENT, "2025", "591633", "2025 exploitatiesubsidies 740 591633; tick1357; primary official NBB WVV 6.10"),
        ("bud_ecow_comm_2025", ENT, "2025", "29500", "2025 commissaris ereloon RSM 29500; tick1357; primary official NBB WVV 9505"),
        ("bud_ecow_zitpen_2025", ENT, "2025", "55744", "2025 bestuurders bruto zitpenning 55744.15 / totaal 59218.10; tick1357; primary official NBB WVV 11 remun"),
        ("bud_ecow_energy_ev_2025", ENT, "2025", "1355641", "2025 EcoWerf Energie NV 0755795294 100pct EV 1355641 / PnL -53585 book 500000; tick1357; primary official NBB WVV 6.5.1; not TE-additive"),
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
                "title": "EcoWerf JR2025 leftover IGS dual (omzet 53.57m / pers 25.80m / expl -21.9k)",
                "entity_id": ENT,
                "beneficiary": "EcoWerf / 28 Oost-Brabant municipalities / EcoWerf Energie",
                "legal_basis": "WVV OV; Bestuursdecreet openbaarheid; decreet lokaal bestuur IGS; NBB neerlegging",
                "decision_date": "2026-06-24",
                "start_year": "2004",
                "end_year": "2025",
                "total_envelope_eur": "53571356",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL waste — per-vennoot 53.57m omzet / 25.80m pers / glossy recon",
                "cut_option": "Publish per-vennoot 53.57m omzet dual + 6.10 split + glossy 52.004m recon + official-site statutory JR; do not recreate parallel Oost-Brabant waste IGS shell",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1357; assets 46228354 omzet 53571356 pers 25796282 pnl -30175; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "EcoWerf JR2025 leftover IGS: omzet 53.57m / pers 25.80m / expl -21.9k / glossy mismatch",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "53571356",
                "total_cost_eur": "46228354",
                "tco_notes": (
                    "Leftover dual IGS waste of mined Oost-Brabant cities + leftover Holsbeek/Boutersem/Bierbeek: "
                    "omzet 53.57m JUMP vs 48.51m / pers 25.80m / expl -21.9k DROP vs +415k / pnl -30.2k / "
                    "assets 46.23m; glossy 52.004m/420 staff does NOT match statutory 53.57m/439 YE; "
                    "official NBB WVV live / site statutory unpublished; do not treat 53.57m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "EcoWerf / 28 Oost-Brabant municipalities / EcoWerf Energie",
                "stated_goal": "Local leftover IGS map VL waste — JR2025 live; dual omzet/pers/glossy FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: omzet 53.57m / pers 25.80m / expl -21.9k / pnl -30.2k; commissaris RSM",
                "absurdity_score": "7.2",
                "cost_score": "7.5",
                "difficulty": "3.0",
                "priority_index": "6.9",
                "cut_proposal": "Publish per-vennoot 53.57m omzet dual + 6.10 split + glossy 52.004m recon + official-site JR; do not recreate parallel Oost-Brabant waste IGS shell",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1357; leftover IGS of mined Oost-Brabant + Holsbeek/Boutersem/Bierbeek; FOI ready not sent; not TE-additive of 348bn",
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
                    "Per-vennoot 2025-2026 dual lines for omzet 53571356 (6.10 category/geo split empty; "
                    "28 gemeenten Aarschot/Begijnendijk/Bekkevoort/Bertem/Bierbeek/Boortmeerbeek/Boutersem/"
                    "Geetbets/Glabbeek/Haacht/Herent/Hoegaarden/Holsbeek/Huldenberg/Keerbergen/Kortenaken/"
                    "Kortenberg/Landen/Leuven/Linter/Lubbeek/Oud-Heverlee/Rotselaar/Scherpenheuvel-Zichem/"
                    "Tielt-Winge/Tienen/Tremelo/Zoutleeuw + Interrand/Interza/Intradura/IOK/Limburg.net/Ivarem) "
                    "+ recon of glossy omzet 52.004m / 420 staff vs statutory 53571356 / 439 YE 403.6 VTE "
                    "+ kapitaalsverhoging 482390 (1 EUR/inwoner; 482390 inwoners) + pers 25796282 vs "
                    "uitzend 436116 / zitpenning 55744 + diensten 19306658 + ST fin 800000 new + CIP jump "
                    "619420 to 2453908 + bestuursverslag mislabel omzet-as-opsrev / 2024 fincost copied as 2025 "
                    "(statutory 407477) + EcoWerf Energie NV 0755795294 (EV 1355641 / pnl -53585 / book 500000) "
                    "+ official-site statutory JR still 'wordt weldra gepubliceerd' + AV 24.06.2026 minutes "
                    "+ commissaris RSM 29500 machine-readable"
                ),
                "why_it_matters": (
                    "Leftover IGS waste shell of mined Oost-Brabant cities + leftover Holsbeek/Boutersem/Bierbeek: "
                    "53.57m omzet / 25.80m pers / expl -21.9k vs glossy 52.004m/420 and unpublished site JR "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "EcoWerf / 28 Oost-Brabant municipalities",
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
                    "tick1357 leftover IGS of mined Oost-Brabant cities + leftover Holsbeek/Boutersem/Bierbeek after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (928kB 64p deposit 2026-00256489). "
                    "AGB MAC already mined 1270 — skipped. Westtoer already mined — skipped. "
                    "Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 skipped. "
                    "NUHMA DC leftover later. IOK/IMOG/Haviland still 2024. Interleuven still 2024 balans. "
                    "POM Limburg glossy-only. Veneco/Leiedal glossy. NBB consult skipped. "
                    "Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1357",
        "title": "EcoWerf JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: EcoWerf leftover IGS waste of mined Oost-Brabant cities + leftover Holsbeek/Boutersem/Bierbeek "
            "after honest hunt; KBO 0862.492.920 Actief; live JR2025 official NBB WVV VOL-inb PDF "
            "(928kB 64p deposit 2026-00256489 + commissaris RSM); "
            "sourced euros assets 46.228m / omzet 53.571m / pers 25.796m / pnl -0.030m; "
            "FOI ready per-vennoot/6.10/glossy-recon/site-JR"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T01:50:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1357 EcoWerf leftover IGS residual; KBO 0862.492.920; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1358 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1358",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1357 done including EcoWerf 1357 leftover IGS live NBB WVV / "
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
            "leftover Londerzeel/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Stad+OCMW Maaseik GE/Brasschaat GE still unmined — take only if PDF fetches "
            "(Holsbeek/Boutersem/Bierbeek now covered as EcoWerf 1357 vennoten); "
            "skip already-mined EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340 / WV Zorgbedrijf Brasschaat 1339 / "
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
        "notes": "spawned tick1357 after EcoWerf leftover IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1357", rq_new, rq_spawn)
    print("research_queue 1357", found, "spawned_1358", spawned)

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
                "last_unit_id": "rq_1357",
                "ticks_completed": "1357",
                "paused": "no",
                "notes": (
                    "tick1357 EcoWerf leftover IGS residual; KBO 0862.492.920; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 46.228m omzet 53.571m pers 25.796m pnl -0.030m; "
                    "FOI ready per-vennoot/6.10/glossy-recon; next rq_1358 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1357 - 2026-08-19 - rq_1357 EcoWerf dual residual leftover
- Unit: EcoWerf (Intergemeentelijk Milieubedrijf Oost-Brabant / leftover IGS waste / opdrachthoudende vereniging) of already-mined Oost-Brabant cities (Leuven / Tienen / Aarschot / Landen / Tielt-Winge / Rotselaar / Herent / Haacht / Tremelo / Kortenberg) + leftover city vennoten Holsbeek / Boutersem / Bierbeek after residual dual hunt (KBO **0862.492.920**; official ecowerf.be jaarverslagen still **Jaarrekening en verslag van de commissaris (wordt weldra gepubliceerd)**; live NBB WVV VOL-inb deposit **2026-00256489** PDF 928kB / 64p; AV **24.06.2026**; neerlegging SBM **07.07.2026**; commissaris RSM Inter Audit BV / Van Heghe Sara oordeel zonder voorbehoud). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last tick confirmed this deposit 928kB/64p and downloaded but not taken). Distinct from already-mined Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **07.01.2004**; statutaire naam EcoWerf, Intergemeentelijk Milieubedrijf Oost-Brabant since 15.12.2003; Opdrachthoudende vereniging since 07.01.2004; zetel Aarschotsesteenweg 210 3012 Leuven since 15.12.2003; **29 VE**; aanbestedende overheid since 15.12.2003; btw since 01.01.2004; RSZ since 01.01.2022; jaarvergadering juni; 17 functiehouders; voorzitter Johan Vanhulst since 26.03.2025; e-mail info@ecowerf.be; tel 016 28 43 00; NACE 38.330 / 38.110. Hunt leftover AGB/zorg/EVA first: AGB MAC Mechelen 2025 BBC already mined tick1270 — skipped; SportAG Aalst / AGB Deinze / AGB Genk already mined — skipped; Westtoer APB already mined — skipped; EcoWerf statutory CDN still live this tick (HTTP 200 / 928518 / 64p) — taken; official site statutory still unpublished. IOK/IMOG/Haviland still 2024; Interleuven 2025 jaarverslag InDesign embed only / balans still 2024; POM Limburg glossy-only — not taken; Veneco/Leiedal glossy-only; IVAREM activiteitenverslag glossy; IGEMO activiteitenverslag only; IVOO no public 2025 JR; IVAGO SSL EOF; MIWA flipbook; MIROM Cloudflare; De Schorre provincieantwerpen.be 403; APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas no fetchable PDF; Dommelhof leftover Limburg EVA KBO 0777.495.085 no JR2025 PDF. Leftover cities Londerzeel/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Stad+OCMW Maaseik GE/Brasschaat GE no fetchable 2025 JR this tick (Holsbeek/Boutersem/Bierbeek now EcoWerf vennoten). NUHMA DC BV 0697.972.606 leftover later. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345. Not every-10 (next 1360).
- EUR strong (primary official WVV VOL-inb + commissaris RSM oordeel zonder voorbehoud): assets **46.228.354** (was 45.283.091); fixed **33.407.479**; MVA **32.901.026** (gebouwen **14.821.277** + machines **7.700.746** + rollend **7.925.097** + CIP **2.453.908** JUMP vs 619.420); FVA **506.453** (EcoWerf Energie NV 0755.795.294 100% book **500.000** / EV 1.355.641 / PnL −53.585); current **12.820.875**; voorraden **1.074.627**; ST recv **7.061.111** (trade **4.817.780** + other **2.243.331**); cash **3.473.097** JUMP vs 2.774.496; equity **13.831.009** (inbreng **4.197.034** JUMP vs 3.714.644 via 1 EUR/inwoner **482.390**; reserves **6.112.794**; kapitaalsubsidies **2.577.404**); voorzieningen **3.587.359**; schulden **28.809.986** (LT **12.177.345** + ST **16.628.906** waarvan nieuw ST-krediet **800.000**); ops rev **55.422.064**; omzet **53.571.356** JUMP vs 48.514.571 (no 6.10 split; glossy **52,004m** mismatch); andere **1.701.018** (subsidies 740 **591.633**); diensten **19.306.658**; goods **4.560.174**; pers **25.796.282** / avg VTE **403,6** / YE **439** koppen **402,7** VTE (glossy 420); uitzend **436.116** / 5,1 VTE; afschr **5.472.570**; expl **−21.850** DROP vs +415.408; fin opbr **399.153**; fin kosten **407.477**; PnL **−30.175** DROP vs +485.129; dividend **0**. Commissaris RSM **29.500**. Zitpenning bruto **55.744**. Bestuursverslag mislabels omzet as bedrijfsopbrengsten and copies 2024 fin kosten 307.247 as 2025.
- CSVs: sources+4/entities+1/budgets+41/commitments+1/leaderboard+1 + FOI ready `gap_ecow_omzet_53_57m_pers_25_80m_pnl_neg_l5` (not sent); rq_1357=done; spawn rq_1358; ticks=1357.
- Coverage: residual dual L5 (EcoWerf leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10).
- Next: rq_1358 residual dual L5 VL JR2025 hole_fill (prefer leftover NUHMA DC BV 0697.972.606 only if a statutory WVV PDF now downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; MIROM only if a 2025 JR PDF now downloads; leftover Londerzeel/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Stad+OCMW Maaseik GE/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1357 write done")


if __name__ == "__main__":
    main()

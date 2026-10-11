# -*- coding: utf-8 -*-
"""Tick 1365 — leftover s-Lim DV JR2025 official NBB WVV euros.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
Not every-10 (next every-10 is 1370).
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1365"
UTC = "2026-08-19T00:45:00Z"
ENT = "dv_sldv"
HIER = "Vlaanderen>Limburg>DV>s-Lim>SmartCity"
GAP = "gap_sldv_omzet_2_56m_pnl_neg_0_62m_adv_10_69m_l5"
SRC = "src_sldv_jr2025_nbb"
SRC2 = "src_sldv_site"
SRC3 = "src_kbo_sldv_0805138503"
SRC4 = "src_sldv_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00173036.pdf"
SRC2_URL = "https://s-lim.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0805138503"
SRC4_URL = "https://s-lim.be/contact/"
FOI_EMAIL = "info@s-lim.be"
FOI_POSTAL = "Herkenrodesingel 14 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_sldv_omzet_2_56m_pnl_neg_0_62m_adv_10_69m_l5.md"
COMM = "comm_sldv_jr2025_pnl"
LB = "lb_sldv_omzet_2_56m_pnl_neg_0_62m_adv"


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
                "title": "s-Lim DV jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00173036; AV 02.06.2026)",
                "url": SRC_URL,
                "publisher": "s-Lim DV / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1365; official NBB VOL-inb PDF 466kB 38p deposit 2026-00173036 neerlegging 16.06.2026 created 18.06.2026; "
                    "leftover IGS DV of 39 Limburg+Laakdal municipalities + s-Lim CV 1362 / MyCSN 1363 / Herkenrode 1364 / NUHMA DC 1358 / Nuhma cv 1356 / Nuhmeris 1361 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Moore Audit / Jimmy Depré 7700 oordeel zonder voorbehoud 18.05.2026; "
                    "s-Lim CV 1362 EV 2599382 / PnL -1355216 MATCHES 50pct book 1299691 / impair 677608"
                ),
            },
            {
                "source_id": SRC2,
                "title": "s-Lim official site (DV+CV; statutory JR unpublished on site; AV 02.06.2026 news without euros)",
                "url": SRC2_URL,
                "publisher": "s-Lim DV",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1365; leftover DV of mined Limburg + Laakdal + Nuhma group; "
                    "s-lim.be has no 2025 JR PDF; AV news 02.06.2026 mentions 2025 cijfers without amounts; "
                    "site key figures 39 lokale besturen / 925186 burgers / 7 mensen / 450 cameras / 339 schermen; "
                    "PEPPOL s-Lim DV 0208:0805138503 / CV 0208:1001753840"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO s-Lim DV 0805.138.503",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1365; KBO 0805.138.503 Actief / normale toestand since 11.09.2023; "
                    "statutaire naam s-Lim since 11.09.2023; Dienstverlenende vereniging (Vlaams Gewest) since 11.09.2023; "
                    "zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; 0 VE; "
                    "btw since 11.09.2023; jaarvergadering juni; boekjaar 31 december; "
                    "uitzonderlijk eerste boekjaar 11.09.2023-31.12.2024; duur 18 jaar; "
                    "15 functiehouders; voorzitter Yilmaz Kurtal / ondervoorzitter Dennis Fransen since 25.03.2025; "
                    "no KBO email/web/tel; NACE 84.130"
                ),
            },
            {
                "source_id": SRC4,
                "title": "s-Lim DV FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "s-Lim DV",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1365; FOI info@s-lim.be (also on NBB deposit header); "
                    "Herkenrodesingel 14 3500 Hasselt; PEPPOL 0208:0805138503; "
                    "no own KBO email/web/tel"
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
                "name_nl": "s-Lim DV (leftover dienstverlenende vereniging Limburg+Laakdal / 39 lokale besturen / smart-city IGS)",
                "name_fr": "s-Lim DV (association prestataire de services residuelle Limbourg+Laakdal / 39 communes / smart city)",
                "name_en": "s-Lim DV leftover Limburg+Laakdal service association (39 municipalities / smart-city IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://s-lim.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1365 leftover residual IGS DV of 39 Limburg+Laakdal municipalities "
                    "+ s-Lim CV 1362 + MyCSN 1363 + Herkenrode 1364 + NUHMA DC 1358 + Nuhma cv 1356 "
                    "+ Nuhmeris 1361 + Nubema 1359 + ECO2050 1360 + NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353; "
                    "KBO 0805.138.503 Actief since 11.09.2023; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 12511069 omzet 2557330 pnl -622829; "
                    "FOI ready 6.10/voorschotten 10.69m/50pct-vs-83.57pct/post-YE 2m/0 VTE"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_sldv_assets_2025", ENT, "2025", "12511069", "2025 assets 12511069 VOL-inb 20/58; tick1365; primary official NBB WVV"),
        ("bud_sldv_assets_2024", ENT, "2024", "15273205", "2024 assets 15273205 comparative 18m first year 30.06.2023-31.12.2024; tick1365; primary official NBB WVV 20/58"),
        ("bud_sldv_fixed_2025", ENT, "2025", "1299691", "2025 vaste activa / FVA 1299691 DROP vs 1977299; all s-Lim CV deelneming; tick1365; primary official NBB WVV 21/28 28"),
        ("bud_sldv_fva_2025", ENT, "2025", "1299691", "2025 verbonden deelnemingen 1299691 = 50pct of s-Lim CV EV 2599382; tick1365; primary official NBB WVV 280"),
        ("bud_sldv_fva_2024", ENT, "2024", "1977299", "2024 FVA 1977299 comparative; tick1365; primary official NBB WVV 280"),
        ("bud_sldv_fvaacq_2025", ENT, "2025", "3810283", "2025 FVA aanschaf 3810283 unchanged; tick1365; primary official NBB WVV 8391"),
        ("bud_sldv_fvaimp_2025", ENT, "2025", "677608", "2025 FVA waardevermindering geboekt 677608 = 50pct of CV PnL -1355216; tick1365; primary official NBB WVV 8471 661"),
        ("bud_sldv_fvaimpcum_2025", ENT, "2025", "2510592", "2025 FVA impair cum 2510592 (was 1832984); tick1365; primary official NBB WVV 8521"),
        ("bud_sldv_current_2025", ENT, "2025", "11211378", "2025 vlottende activa 11211378 vs 13295906; tick1365; primary official NBB WVV 29/58"),
        ("bud_sldv_strecv_2025", ENT, "2025", "492826", "2025 ST vorderingen 492826 (trade 335020 + other 157807); tick1365; primary official NBB WVV 40/41"),
        ("bud_sldv_trade_2025", ENT, "2025", "335020", "2025 handelsvorderingen 335020 vs 506223; tick1365; primary official NBB WVV 40"),
        ("bud_sldv_othrecv_2025", ENT, "2025", "157807", "2025 overige ST vorderingen 157807 vs 144953; tick1365; primary official NBB WVV 41"),
        ("bud_sldv_deposits_2025", ENT, "2025", "10000000", "2025 termijnrekeningen 10000000 (1m-1j); tick1365; primary official NBB WVV 53 8687"),
        ("bud_sldv_deposits_2024", ENT, "2024", "12300000", "2024 termijnrekeningen 12300000 comparative (1m 1000000 + 1m-1j 11300000); tick1365; primary official NBB WVV 53"),
        ("bud_sldv_cash_2025", ENT, "2025", "636145", "2025 liquide middelen 636145 vs 248417; tick1365; primary official NBB WVV 54/58"),
        ("bud_sldv_cash_2024", ENT, "2024", "248417", "2024 liquide middelen 248417 comparative; tick1365; primary official NBB WVV 54/58"),
        ("bud_sldv_prepaid_2025", ENT, "2025", "82407", "2025 overlopend actief 82407 (kosten 35113 + opbr 47293); tick1365; primary official NBB WVV 490/1"),
        ("bud_sldv_equity_2025", ENT, "2025", "1360204", "2025 eigen vermogen 1360204 vs 1983034; tick1365; primary official NBB WVV 10/15"),
        ("bud_sldv_equity_2024", ENT, "2024", "1983034", "2024 eigen vermogen 1983034 comparative; tick1365; primary official NBB WVV 10/15"),
        ("bud_sldv_inbreng_2025", ENT, "2025", "2000000", "2025 onbeschikbare inbreng 2000000 / 80000 aandelen 80000 stemrechten; tick1365; primary official NBB WVV 111 8761"),
        ("bud_sldv_re_2025", ENT, "2025", "-639796", "2025 overgedragen verlies -639796 (RvB -639795.70); tick1365; primary official NBB WVV 14"),
        ("bud_sldv_debt_2025", ENT, "2025", "11150865", "2025 schulden 11150865 vs 13290172; tick1365; primary official NBB WVV 17/49"),
        ("bud_sldv_lt_2025", ENT, "2025", "8496089", "2025 LT overige schulden 8496089 (1-5j voorschotten/verrekeningsrechten); tick1365; primary official NBB WVV 17 178/9 8902"),
        ("bud_sldv_st_2025", ENT, "2025", "2612652", "2025 ST schulden 2612652 vs 3773036; tick1365; primary official NBB WVV 42/48"),
        ("bud_sldv_sttrade_2025", ENT, "2025", "328846", "2025 leveranciers 328846 vs 816317; tick1365; primary official NBB WVV 440/4"),
        ("bud_sldv_stprepay_2025", ENT, "2025", "88529", "2025 vooruitbetalingen op bestellingen 88529; tick1365; primary official NBB WVV 46"),
        ("bud_sldv_stother_2025", ENT, "2025", "2190982", "2025 ST overige schulden 2190982 voorschotten/verrekeningsrechten; tick1365; primary official NBB WVV 47/48"),
        ("bud_sldv_adv_2025", ENT, "2025", "10687071", "2025 voorschotten LT+ST 8496089+2190982=10687071 vs termijn 10000000; tick1365; primary official NBB WVV 6.19"),
        ("bud_sldv_accrued_2025", ENT, "2025", "42123", "2025 overlopend passief 42123 (kosten 19201 + opbr 22923); tick1365; primary official NBB WVV 492/3"),
        ("bud_sldv_sttax_2025", ENT, "2025", "4295", "2025 niet-vervallen belastingschulden 4295; tick1365; primary official NBB WVV 450/3 9073"),
        ("bud_sldv_ops_2025", ENT, "2025", "2557330", "2025 bedrijfsopbrengsten 2557330 all omzet; tick1365; primary official NBB WVV 70/76A"),
        ("bud_sldv_omzet_2025", ENT, "2025", "2557330", "2025 omzet 2557330; 6.10 not filed; tick1365; primary official NBB WVV 70"),
        ("bud_sldv_omzet_2024", ENT, "2024", "3258622", "2024 omzet 3258622 comparative 18m first year; tick1365; primary official NBB WVV 70"),
        ("bud_sldv_opscost_2025", ENT, "2025", "2717716", "2025 bedrijfskosten 2717716 all diensten; pers empty; tick1365; primary official NBB WVV 60/66A 61"),
        ("bud_sldv_diensten_2025", ENT, "2025", "2717716", "2025 diensten 2717716 vs 3616251 (18m comparative); tick1365; primary official NBB WVV 61"),
        ("bud_sldv_expl_2025", ENT, "2025", "-160387", "2025 bedrijfsverlies -160387 vs -357590; tick1365; primary official NBB WVV 9901"),
        ("bud_sldv_fininc_2025", ENT, "2025", "235000", "2025 financiele opbrengsten 235000 (vlottende/termijn); tick1365; primary official NBB WVV 75 751"),
        ("bud_sldv_fincost_2025", ENT, "2025", "677915", "2025 financiele kosten 677915 (rec 307 bank + nr FVA 677608); tick1365; primary official NBB WVV 65/66B"),
        ("bud_sldv_tax_2025", ENT, "2025", "19528", "2025 belastingen 19528 (betaald 70500 / geactiveerd 50972); tick1365; primary official NBB WVV 67/77"),
        ("bud_sldv_pnl_2025", ENT, "2025", "-622829", "2025 PnL 9904 -622829 (RvB -622829.29; commissaris 622829); tick1365; primary official NBB WVV"),
        ("bud_sldv_pnl_2024", ENT, "2024", "-1827249", "2024 PnL -1827249 comparative 18m; tick1365; primary official NBB WVV 9904"),
        ("bud_sldv_comm_2025", ENT, "2025", "7700", "2025 commissaris Moore Audit 7700; tick1365; primary official NBB WVV 9505"),
        ("bud_sldv_board_2025", ENT, "2025", "36861", "2025 bestuurdersbezoldiging 36861; tick1365; primary official NBB WVV 9503"),
        ("bud_sldv_relrecv_2025", ENT, "2025", "284666", "2025 verbonden ST vorderingen 284666 vs 383681; tick1365; primary official NBB WVV 9291 9311"),
        ("bud_sldv_reldebt_2025", ENT, "2025", "194146", "2025 verbonden ST schulden 194146 vs 572984; tick1365; primary official NBB WVV 9351 9371"),
        ("bud_sldv_vat_2025", ENT, "2025", "551925", "2025 BTW door vennootschap 551925; tick1365; primary official NBB WVV 9146"),
        ("bud_sldv_wh_2025", ENT, "2025", "11829", "2025 bedrijfsvoorheffing 11829; tick1365; primary official NBB WVV 9147"),
        ("bud_sldv_loanest_2026", ENT, "2026", "2000000", "2026 post-YE 20.02.2026 lening s-Lim CV schuilhuisjes Genk/Hasselt geraamd 2m; tick1365; primary official NBB WVV jaarverslag"),
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
                "basis": "estimate" if bid == "bud_sldv_loanest_2026" else "executed",
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
                "title": "s-Lim DV JR2025 leftover IGS dual (assets 12.51m / omzet 2.56m / PnL -0.62m / voorschotten 10.69m)",
                "entity_id": ENT,
                "beneficiary": "s-Lim DV / s-Lim CV / NUHMA DC / Nuhma cv / 39 Limburg+Laakdal municipalities / MyCSN",
                "legal_basis": "WVV DV; decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-06-02",
                "start_year": "2023",
                "end_year": "2026",
                "total_envelope_eur": "12511069",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL smart-city DV — 6.10 empty / 10.69m voorschotten / 50pct book vs 83.57pct votes / 0 VTE",
                "cut_option": "Publish 6.10 municipal counterparties + put 10.69m voorschotten vs 10.00m termijn on the record + reconcile 50pct book vs 83.57pct votes + 2m post-YE CV loan + why 0 VTE on the 39-municipality DV; do not keep 12.5m municipal smart-city IGS as unpublished dual vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1365; assets 12511069 omzet 2557330 pnl -622829; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "s-Lim DV JR2025 leftover IGS: assets 12.51m / omzet 2.56m / PnL -0.62m / voorschotten 10.69m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "622829",
                "total_cost_eur": "12511069",
                "tco_notes": (
                    "Leftover dual IGS DV of 39 Limburg+Laakdal municipalities: "
                    "assets 12.51m / equity 1.36m / pnl -0.62m / omzet 2.56m / pers 0 / 0 VTE / "
                    "83.57pct votes in s-Lim CV vs 50pct book 1.30m / "
                    "voorschotten 10.69m vs termijn 10.00m / no consolidation / official NBB WVV live; "
                    "do not treat 12.51m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "s-Lim DV / s-Lim CV / NUHMA DC / Nuhma cv / 39 Limburg+Laakdal municipalities / MyCSN",
                "stated_goal": "Local leftover IGS map VL smart-city DV — JR2025 live; dual 6.10/voorschotten/votes FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 12.51m / omzet 2.56m / pnl -0.62m; 0 VTE; CV 50pct book MATCHES; voorschotten 10.69m",
                "absurdity_score": "7.4",
                "cost_score": "6.3",
                "difficulty": "2.5",
                "priority_index": "6.6",
                "cut_proposal": "Publish 6.10 municipal counterparties + put 10.69m voorschotten vs 10.00m termijn on the record + reconcile 50pct book vs 83.57pct votes + 2m post-YE CV loan + why 0 VTE on the 39-municipality DV; do not keep 12.5m municipal smart-city IGS as unpublished dual vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1365; leftover IGS DV of mined Limburg+Laakdal + s-Lim CV 1362 / MyCSN 1363 / Herkenrode 1364 / NUHMA DC 1358 / Nuhma cv 1356 / Nuhmeris 1361 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "6.10 omzet 2557330 category/geo split not filed + per-gemeente/MyCSN/Nuhma/s-Lim CV/Fluvius/Limburg.net counterparties "
                    "+ voorschotten/verrekeningsrechten 10687071 (LT 8496089 + ST 2190982) vs termijnrekeningen 10000000 + cash 636145 "
                    "+ 50pct FVA book 1299691 vs 83.57pct stemrechten in s-Lim CV 0679631191 (Cat C 20422 / 67.13pct + Cat B 5000 / 16.44pct; tick1362 MATCH) "
                    "+ no consolidation 6.18.1 exemption unmotivated "
                    "+ post-YE 20.02.2026 lening s-Lim CV geraamd 2m schuilhuisjes Genk/Hasselt "
                    "+ related ST recv 284666 / ST debt 194146 + 6.15 related-party refusal "
                    "+ pers 0 / 0 VTE vs site 7 mensen / CV 4.8 VTE 698849 "
                    "+ bestuurders 36861 + commissaris Moore 7700 "
                    "+ FVA impair 677608 / cum 2510592 on aanschaf 3810283 + equity-method switch 31.12.2025 "
                    "+ 39 municipalities (Voeren 39th) inleg/stem/voorschot "
                    "+ official-site JR (s-lim.be no JR PDF)"
                ),
                "why_it_matters": (
                    "Leftover IGS DV of 39 Limburg+Laakdal municipalities + s-Lim CV 1362 "
                    "+ MyCSN 1363 + Herkenrode 1364 + NUHMA DC 1358 + Nuhma cv 1356 "
                    "+ Nuhmeris 1361 + Nubema 1359 + ECO2050 1360 + NUHMA AC 1355 + Bionerga 1354 + Limburg.net 1353 "
                    "(same zetel Herkenrodesingel 14): "
                    "12.51m assets / 2.56m omzet / -0.62m pnl / 0 VTE / 10.69m municipal advances vs 10.00m term deposits / "
                    "83.57pct CV votes vs 50pct book / no consolidation / post-YE 2m loan "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "s-Lim DV / s-Lim CV / NUHMA DC BV / Nuhma cv / Limburg municipalities",
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
                    "tick1365 leftover IGS DV of 39 Limburg+Laakdal municipalities + s-Lim CV 1362 / MyCSN 1363 / Herkenrode 1364 / NUHMA DC 1358 / Nuhma cv 1356 / Nuhmeris 1361 / Nubema 1359 / ECO2050 1360 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (466kB 38p deposit 2026-00173036). "
                    "AGB MAC already mined 1270 — skipped. Westtoer already mined — skipped. "
                    "Herkenrode already mined 1364 — skipped. MyCSN already mined 1363 — skipped. s-Lim CV already mined 1362 — skipped. Nuhmeris already mined 1361 — skipped. ECO2050 already mined 1360 — skipped. Nubema already mined 1359 — skipped. NUHMA DC already mined 1358 — skipped. EcoWerf already mined 1357 — skipped. "
                    "Dommelhof leftover Limburg EVA KBO 0777.495.085 still no 2026 PDF. "
                    "IOK/IMOG/Haviland still 2024. Interleuven still 2024 balans. "
                    "POM Limburg glossy-only. Veneco/Leiedal glossy. NBB consult skipped. "
                    "Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1365",
        "title": "s-Lim DV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: s-Lim leftover IGS DV of 39 Limburg+Laakdal municipalities "
            "+ s-Lim CV/MyCSN/Herkenrode/NUHMA DC/Nuhma cv/Nuhmeris/Nubema/ECO2050/AC/Bionerga/Limburg.net after honest hunt; KBO 0805.138.503 Actief; "
            "live JR2025 official NBB WVV VOL-inb PDF (466kB 38p deposit 2026-00173036; commissaris Moore); "
            "sourced euros assets 12511069 / omzet 2557330 / pnl -622829; "
            "FOI ready 6.10/voorschotten 10.69m/50pct-vs-83.57pct/post-YE 2m/0 VTE"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T00:25:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1365 s-Lim DV leftover IGS residual; KBO 0805.138.503; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1366 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1366",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1365 done including s-Lim DV 1365 leftover IGS live NBB WVV / "
            "Herkenrode RE NV 1364 leftover vastgoed live NBB WVV / "
            "MyCSN NV 1363 leftover smart-city live NBB WVV / "
            "s-Lim CV 1362 leftover smart-city live NBB WVV / "
            "Nuhmeris NV 1361 leftover klimaat-holding live NBB WVV / "
            "ECO2050 cv 1360 leftover klimaat-coop live NBB WVV + every-10 / "
            "Nubema NV 1359 leftover klimaat-holding live NBB WVV / "
            "NUHMA DC BV 1358 leftover klimaat-holding live NBB WVV / "
            "EcoWerf 1357 leftover IGS live NBB WVV / "
            "Nuhma cv 1356 leftover klimaat-holding live NBB WVV / "
            "NUHMA AC NV 1355 leftover klimaat-holding live NBB WVV / "
            "Bionerga NV 1354 leftover waste-processing live NBB WVV / "
            "Limburg.net 1353 leftover IGS glossy-only FOI / IVBO 1352 leftover IGS live WVV / "
            "SOLVA 1351 leftover IGS live JR / Interwaas 1350 leftover IGS live WVV + every-10); "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "Interleuven 2025 jaarverslag klaar / AV 17.06.2026 but still no 2025 balans PDF — take only if a 2025 balans PDF now downloads; "
            "IOK / IMOG / Haviland still 2024 — take only if a 2025 JR PDF now downloads; "
            "Veneco / Leiedal / IVOO / MIROM / INCOVO / IVAGO / MIWA / IVAREM / IGEMO — take only if a statutory 2025 WVV/BBC PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1365 after s-Lim DV leftover IGS live NBB WVV; next residual dual L5 VL; next every-10 is 1370",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1365", rq_new, rq_spawn)
    print("research_queue 1365", found, "spawned_1366", spawned)

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
                "last_unit_id": "rq_1365",
                "ticks_completed": "1365",
                "paused": "no",
                "notes": (
                    "tick1365 s-Lim DV leftover IGS residual; KBO 0805.138.503; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 12511069 omzet 2557330 pnl -622829; "
                    "FOI ready 6.10/voorschotten 10.69m/50pct-vs-83.57pct/post-YE 2m; next rq_1366 residual dual L5 VL; continuous hole_fill; next every-10 is 1370"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1365 - 2026-08-19 - rq_1365 s-Lim DV dual residual leftover
- Unit: s-Lim DV (leftover dienstverlenende vereniging / smart-city IGS of 39 Limburg + Laakdal municipalities; Voeren 39ste eind 2025) of already-mined Limburg cities via Nuhma cv tick1356 (Hasselt / Genk / Tongeren-Borgloon / Houthalen-Helchteren / Bilzen-Hoeselt / Leopoldsburg / Nieuwerkerken / Gingelom / Pelt / Maasmechelen) + leftover CV s-Lim tick1362 + leftover NV MyCSN tick1363 + leftover NV Herkenrode RE tick1364 + leftover BV NUHMA DC tick1358 + leftover NV Nuhmeris tick1361 + leftover NV Nubema tick1359 + leftover cv ECO2050 tick1360 + leftover NV NUHMA AC tick1355 + leftover NV Bionerga tick1354 + leftover IGS Limburg.net tick1353 after residual dual hunt (KBO **0805.138.503**; official s-lim.be has no JR PDF / AV-nieuws 02.06.2026 noemt cijfers zonder bedragen; live NBB WVV VOL-inb deposit **2026-00173036** PDF 466kB / 38p; AV **02.06.2026**; neerlegging **16.06.2026**; PDF created **18.06.2026**; commissaris Moore Audit / Jimmy Depré 7.700 oordeel zonder voorbehoud 18.05.2026; jaarverslag RvB 11.03.2026 text-extractable). Leftover IGS DV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last tick listed leftover s-Lim DV 0805.138.503 only if a statutory 2025 WVV/BBC PDF now downloads). Distinct from already-mined Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **11.09.2023**; statutaire naam s-Lim since 11.09.2023; Dienstverlenende vereniging (Vlaams Gewest) since 11.09.2023; zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025; **0 VE**; btw since 11.09.2023; jaarvergadering juni; uitzonderlijk eerste boekjaar 11.09.2023–31.12.2024 (18m comparative); duur 18 jaar; 15 functiehouders; voorzitter Yilmaz Kurtal / ondervoorzitter Dennis Fransen since 25.03.2025; e-mail info@s-lim.be; NACE 84.130. Hunt leftover AGB/zorg/EVA first: AGB MAC Mechelen 2025 BBC already mined tick1270 — skipped; SportAG Aalst / AGB Deinze / AGB Genk already mined — skipped; Westtoer APB already mined — skipped; Herkenrode already mined 1364 — skipped; MyCSN already mined 1363 — skipped; s-Lim CV already mined 1362 — skipped; Nuhmeris already mined 1361 — skipped; ECO2050 already mined 1360 — skipped; Nubema already mined 1359 — skipped; NUHMA DC already mined 1358 — skipped; EcoWerf already mined 1357 — skipped; s-Lim DV statutory CDN live this tick (HTTP 200 / 465607 / 38p) — taken. IOK/IMOG/Haviland still 2024; Interleuven 2025 jaarverslag InDesign embed only / balans still 2024; POM Limburg glossy-only — not taken; Veneco/Leiedal glossy-only; IVAREM activiteitenverslag glossy; IGEMO activiteitenverslag only; IVOO no public 2025 JR; IVAGO SSL EOF; MIWA flipbook; MIROM Cloudflare; De Schorre provincieantwerpen.be 403; APB POA/TPA/Warande/Nekker/PIH/Inovant/Atlas not taken (s-Lim DV WVV live); Dommelhof leftover Limburg EVA KBO 0777.495.085 still no 2026 PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE no fetchable 2025 JR this tick. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345. Not every-10 (next 1370).
- EUR strong (primary official WVV VOL-inb; s-Lim CV 1362 EV 2.599.382 / PnL −1.355.216 **matches** 50% book 1.299.691 / impair 677.608; commissaris Moore oordeel zonder voorbehoud 18.05.2026): assets **12.511.069** (was 15.273.205 18m comparative; RvB 12.511.068,84); fixed/FVA **1.299.691** DROP vs 1.977.299 (s-Lim CV 0679.631.191 Cat C 20.422 / **67,13%** + Cat B 5.000 / **16,44%** = **83,57%** stemrechten; aanschaf **3.810.283**; impair cum **2.510.592** after 2025 **677.608** = 50% of CV PnL; equity-method since 31.12.2025 CBN 2011/14 + 2016/23); current **11.211.378**; ST recv **492.826** (trade 335.020 + other 157.807); termijn **10.000.000** DROP vs 12.300.000 (all 1m–1j); cash **636.145 JUMP** vs 248.417; prepaid **82.407** (kosten 35.113 + opbr 47.293); equity **1.360.204** DROP vs 1.983.034 (inbreng 2.000.000 onbeschikbaar / 80.000 aandelen; overgedragen −639.796); schulden **11.150.865** (LT overige **8.496.089** 1–5j voorschotten; ST **2.612.652** waarvan leveranciers 328.846 + vooruit 88.529 + tax 4.295 + overige **2.190.982**; 6.19 verrekeningsrechten); omzet **2.557.330** (6.10 niet neergelegd; 18m comparative 3.258.622) / pers **0** / VTE **0**; diensten **2.717.716**; expl **−160.387**; fin opbr **235.000**; fin kosten **677.915** (bank 307 + nr FVA 677.608); belasting **19.528**; PnL **−622.829** (was −1.827.249 18m; RvB −622.829,29); dividend **0**. Related ST recv **284.666** / ST debt **194.146**. Bestuurders **36.861**. Commissaris Moore **7.700**. Geen consolidatie (6.18.1 vrijgesteld). Post-YE 20.02.2026 lening s-Lim CV **geraamd 2m** schuilhuisjes Genk/Hasselt (tick 1362 continuity). Continuity art. 3:6, 6° (voldoende liquide). 6.15 related-party refusal.
- CSVs: sources+4/entities+1/budgets+48/commitments+1/leaderboard+1 + FOI ready `gap_sldv_omzet_2_56m_pnl_neg_0_62m_adv_10_69m_l5` (not sent); rq_1365=done; spawn rq_1366; ticks=1365.
- Coverage: residual dual L5 (s-Lim leftover DV live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1370).
- Next: rq_1366 residual dual L5 VL JR2025 hole_fill (prefer leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; Interleuven only if a 2025 balans PDF now downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; Leiedal only if a WVV/BBC PDF now downloads; IVOO only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1365 write done")


if __name__ == "__main__":
    main()

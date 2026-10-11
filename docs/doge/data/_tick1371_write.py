# -*- coding: utf-8 -*-
"""Tick 1371 — leftover Veneco JR2025 official NBB WVV euros.
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

TICK = "1371"
UTC = "2026-08-19T02:10:00Z"
ENT = "igs_vene"
HIER = "Vlaanderen>OostVlaanderen>IGS>Veneco>MeetjeslandGent"
GAP = "gap_vene_omzet_1_18m_othops_5_27m_inv_23_12m_l5"
SRC = "src_vene_jr2025_nbb"
SRC2 = "src_vene_site"
SRC3 = "src_kbo_vene_0200065765"
SRC4 = "src_vene_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00188751.pdf"
SRC2_URL = "https://veneco.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0200065765"
SRC4_URL = "https://veneco.be/publicaties"
FOI_EMAIL = "info@veneco.be"
FOI_POSTAL = "Panhuisstraat 1 9070 Destelbergen"
DRAFT = "docs/doge/foi/drafts/gap_vene_omzet_1_18m_othops_5_27m_inv_23_12m_l5.md"
COMM = "comm_vene_jr2025_pnl"
LB = "lb_vene_omzet_1_18m_othops_5_27m_inv_23_12m"


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
                "title": "Veneco jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00188751; AV 10.06.2026)",
                "url": SRC_URL,
                "publisher": "Veneco / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1371; official NBB VOL-inb PDF 24.1MB 282p (41 statutory + glossy) deposit 2026-00188751 created 18.06.2026 header 22.06.2026; "
                    "leftover IGS DV of Gent-Meetjesland municipalities; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Figurad BV 0423.109.644 / Bart Meganck A01675 14417; "
                    "6.1/6.4.1/6.5.1/6.15/6.18 not filed; 6.10 category/geo empty; 8761/8762/9503 empty; not every-10"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Veneco official site (intercommunale streekontwikkeling regio Gent / Meetjesland)",
                "url": SRC2_URL,
                "publisher": "Veneco Intergemeentelijke Vereniging",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1371; leftover IGS streek of 20 A-vennoten Gent-Meetjesland; "
                    "veneco.be has glossy jaarverslag 2025 + AV 10.06.2026 presentatie; statutory 2025 balans is the NBB CDN deposit"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Veneco 0200.065.765",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1371; KBO 0200.065.765 Actief / normale toestand since 09.08.1960; "
                    "statutaire naam Intergemeentelijke Vereniging Veneco since 13.12.2016; "
                    "afkorting Veneco since 21.06.1997; Dienstverlenende vereniging (Vlaams Gewest) since 09.08.1960; "
                    "zetel Panhuisstraat 1 9070 Destelbergen since 13.12.2016; 1 VE; "
                    "btw since 01.03.2007; RSZ since 01.01.2022; aanbestedende overheid since 09.08.1960; "
                    "jaarvergadering mei; boekjaar 31 december; "
                    "15 KBO-bestuurders; voorzitter Koenraad De Ceuninck; "
                    "no KBO email/web/tel; NACE 84.130/82.990/68.121"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Veneco FOI channel / official contact + publicaties",
                "url": SRC4_URL,
                "publisher": "Veneco",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1371; FOI info@veneco.be / 09 251 22 22; "
                    "Panhuisstraat 1 9070 Destelbergen; no own KBO email/web/tel"
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
                "name_nl": "Veneco (leftover dienstverlenende vereniging / IGS streek Gent-Meetjesland)",
                "name_fr": "Veneco (association de services residuelle / IGS regionale Gand-Meetjesland)",
                "name_en": "Veneco leftover Gent-Meetjesland regional IGS (service association)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://veneco.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1371 leftover residual IGS DV of 20 A-vennoten Gent-Meetjesland; "
                    "KBO 0200.065.765 Actief since 09.08.1960; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 51983427 omzet 1184113 othops 5270686 inv 23116144 pnl 3231312; "
                    "FOI ready omzet 1.18m/othops 5.27m/inv 23.12m"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_vene_assets_2025", ENT, "2025", "51983427", "2025 assets 51983427 VOL-inb 20/58; tick1371; primary official NBB WVV"),
        ("bud_vene_assets_2024", ENT, "2024", "53729614", "2024 assets 53729614 comparative; tick1371; primary official NBB WVV 20/58"),
        ("bud_vene_fixed_2025", ENT, "2025", "1849887", "2025 vaste activa 1849887 vs 1924170; tick1371; primary official NBB WVV 21/28"),
        ("bud_vene_iva_2025", ENT, "2025", "49048", "2025 immateriele VA 49048 vs 11840 after aanschaf 52177; tick1371; primary official NBB WVV 21"),
        ("bud_vene_mva_2025", ENT, "2025", "1788517", "2025 MVA 1788517 vs 1900008; tick1371; primary official NBB WVV 22/27"),
        ("bud_vene_buildings_2025", ENT, "2025", "1651207", "2025 terreinen en gebouwen 1651207 vs 1729391; tick1371; primary official NBB WVV 22"),
        ("bud_vene_machines_2025", ENT, "2025", "110767", "2025 installaties/machines 110767 vs 135607; tick1371; primary official NBB WVV 23"),
        ("bud_vene_rollend_2025", ENT, "2025", "26543", "2025 meubilair/rollend 26543 vs 35010; tick1371; primary official NBB WVV 24"),
        ("bud_vene_fva_2025", ENT, "2025", "12322", "2025 FVA 12322 (aandelen 322 + borg 12000; 6.4.1/6.5.1 not filed); tick1371; primary official NBB WVV 28"),
        ("bud_vene_current_2025", ENT, "2025", "50133540", "2025 vlottende activa 50133540 vs 51805444; tick1371; primary official NBB WVV 29/58"),
        ("bud_vene_inv_2025", ENT, "2025", "23116144", "2025 voorraden 23116144 all onroerend bestemd voor verkoop; tick1371; primary official NBB WVV 3/35"),
        ("bud_vene_inv_2024", ENT, "2024", "21529677", "2024 RE inventory 21529677 comparative; tick1371; primary official NBB WVV 35"),
        ("bud_vene_strecv_2025", ENT, "2025", "1031861", "2025 ST vorderingen 1031861 (trade 773215 + other 258646); tick1371; primary official NBB WVV 40/41"),
        ("bud_vene_invest_2025", ENT, "2025", "24148004", "2025 geldbeleggingen 24148004 vs 24988899; tick1371; primary official NBB WVV 50/53"),
        ("bud_vene_invest_2024", ENT, "2024", "24988899", "2024 geldbeleggingen 24988899 comparative; tick1371; primary official NBB WVV 50/53"),
        ("bud_vene_shares_2025", ENT, "2025", "499523", "2025 aandelen beleggingen 499523 vs 1054146; tick1371; primary official NBB WVV 6.6 51"),
        ("bud_vene_fixedinc_2025", ENT, "2025", "8542462", "2025 vastrentende effecten kredietinstellingen 8542462 vs 11371991; tick1371; primary official NBB WVV 6.6 52"),
        ("bud_vene_term_2025", ENT, "2025", "9100000", "2025 termijnrekeningen 9100000 all 1m-1j vs 7515000; tick1371; primary official NBB WVV 6.6 53"),
        ("bud_vene_othinv_2025", ENT, "2025", "6006019", "2025 hierboven niet-opgenomen overige geldbeleggingen 6006019 vs 5047762; tick1371; primary official NBB WVV 6.6 8689"),
        ("bud_vene_cash_2025", ENT, "2025", "1747622", "2025 liquide middelen 1747622 vs 1644887; tick1371; primary official NBB WVV 54/58"),
        ("bud_vene_prepaid_2025", ENT, "2025", "89909", "2025 overlopend actief 89909 (intrest 36857 + opbr 52346); tick1371; primary official NBB WVV 490/1"),
        ("bud_vene_equity_2025", ENT, "2025", "23063251", "2025 eigen vermogen 23063251 vs 19724600; tick1371; primary official NBB WVV 10/15"),
        ("bud_vene_inbreng_2025", ENT, "2025", "2408388", "2025 inbreng onbeschikbaar 2408388 / toetreding Laarne 31500 + SML 20000 + OCMW 50; 8761 empty; tick1371; primary official NBB WVV 10/11"),
        ("bud_vene_reserves_2025", ENT, "2025", "3786019", "2025 reserves 3786019 (statutair 291300 + belastingvrij 2075530 + beschikbaar 1419189); tick1371; primary official NBB WVV 13"),
        ("bud_vene_retained_2025", ENT, "2025", "16868844", "2025 overgedragen winst 16868844 vs 14344812; tick1371; primary official NBB WVV 14"),
        ("bud_vene_prov_2025", ENT, "2025", "15250091", "2025 voorzieningen 15250091 DROP vs 19749909; tick1371; primary official NBB WVV 16"),
        ("bud_vene_pension_2025", ENT, "2025", "2355002", "2025 pensioenen 2355002 vs 2367655; tick1371; primary official NBB WVV 160"),
        ("bud_vene_othprov_2025", ENT, "2025", "12895089", "2025 overige risico's 12895089 DROP vs 17382254 (Innovatiefonds 3956211 / Campagne 3680284 / Prijkels 3312188 / park 613011 / Groenling 258599 / diverse 837922 / SOM 236874); tick1371; primary official NBB WVV 164/5 6.8"),
        ("bud_vene_prov_used_2025", ENT, "2025", "5098819", "2025 voorziening aanwending 5098819 / dotatie 599001 / netto 635/8 -4499818; tick1371; primary official NBB WVV 6.10 9116"),
        ("bud_vene_innov_2025", ENT, "2025", "3956211", "2025 voorziening Innovatiefonds 3956211; tick1371; primary official NBB WVV 6.8"),
        ("bud_vene_campagne_2025", ENT, "2025", "3680284", "2025 voorziening BT De Campagne Maldegem 3680284; tick1371; primary official NBB WVV 6.8"),
        ("bud_vene_prijkels_2025", ENT, "2025", "3312188", "2025 voorziening BT De Prijkels 3312188; tick1371; primary official NBB WVV 6.8"),
        ("bud_vene_debt_2025", ENT, "2025", "13670085", "2025 schulden 13670085 vs 14255105; tick1371; primary official NBB WVV 17/49"),
        ("bud_vene_lt_2025", ENT, "2025", "10562893", "2025 LT schulden 10562893 (achtergesteld 10337943 + bank 224950); tick1371; primary official NBB WVV 17"),
        ("bud_vene_subord_2025", ENT, "2025", "10337943", "2025 achtergestelde lening 10337943 (vennoten 8233278 tot 2035 + provincie 3666290 + scheiding 279958); tick1371; primary official NBB WVV 170 + jaarverslag"),
        ("bud_vene_ltbank_2025", ENT, "2025", "224950", "2025 LT bank panloos huis 224950; tick1371; primary official NBB WVV 173"),
        ("bud_vene_st_2025", ENT, "2025", "2888845", "2025 ST schulden 2888845 vs 3225432; tick1371; primary official NBB WVV 42/48"),
        ("bud_vene_sttrade_2025", ENT, "2025", "875335", "2025 leveranciers 875335 vs 1218367; tick1371; primary official NBB WVV 440/4"),
        ("bud_vene_othdebt_2025", ENT, "2025", "1178055", "2025 overige ST schulden 1178055 (groenwaarborgen + tax shelter 115000); tick1371; primary official NBB WVV 47/48"),
        ("bud_vene_govg_2025", ENT, "2025", "10601026", "2025 door Belgische overheden gewaarborgde schulden 10601026 all achtergesteld; tick1371; primary official NBB WVV 6.9 9061"),
        ("bud_vene_hyp_2025", ENT, "2025", "1347707", "2025 hypotheek boekwaarde 1347707 + mandaat 700000; tick1371; primary official NBB WVV 6.14 91611"),
        ("bud_vene_ops_2025", ENT, "2025", "8569220", "2025 bedrijfsopbrengsten 8569220 vs 13222298; tick1371; primary official NBB WVV 70/76A"),
        ("bud_vene_omzet_2025", ENT, "2025", "1184113", "2025 omzet 1184113 DROP vs 9984485; 6.10 category/geo empty; glossy gronden IZ 1173378 + woon 10735; tick1371; primary official NBB WVV 70"),
        ("bud_vene_omzet_2024", ENT, "2024", "9984485", "2024 omzet 9984485 comparative; tick1371; primary official NBB WVV 70"),
        ("bud_vene_invchg_2025", ENT, "2025", "2114421", "2025 voorraadwijziging +2114421 (IZ 1955046 + woon 159375); tick1371; primary official NBB WVV 71"),
        ("bud_vene_othops_2025", ENT, "2025", "5270686", "2025 andere bedrijfsopbrengsten 5270686 vs 5607424; 740 subsidies 1577066 only; tick1371; primary official NBB WVV 74"),
        ("bud_vene_othops_2024", ENT, "2024", "5607424", "2024 andere bedrijfsopbrengsten 5607424 comparative; tick1371; primary official NBB WVV 74"),
        ("bud_vene_subs_2025", ENT, "2025", "1577066", "2025 exploitatiesubsidies 1577066 vs 1721704 (toelagen Vlaamse Gemeenschap); tick1371; primary official NBB WVV 6.10 740"),
        ("bud_vene_goods_2025", ENT, "2025", "1755030", "2025 handelsgoederen/grond-hulp 1755030 vs 3543484; tick1371; primary official NBB WVV 60"),
        ("bud_vene_diensten_2025", ENT, "2025", "2100124", "2025 diensten 2100124 vs 1696238; tick1371; primary official NBB WVV 61"),
        ("bud_vene_pers_2025", ENT, "2025", "4512526", "2025 bezoldigingen 4512526 / 42.6 VTE / 51 koppen / YE 45.5 VTE; tick1371; primary official NBB WVV 62 9087"),
        ("bud_vene_deprec_2025", ENT, "2025", "167369", "2025 afschrijvingen 167369; tick1371; primary official NBB WVV 630"),
        ("bud_vene_wvinv_2025", ENT, "2025", "527954", "2025 WV voorraden netto 527954 (geboekt 700000 / terug 172046); tick1371; primary official NBB WVV 631/4"),
        ("bud_vene_expl_2025", ENT, "2025", "3997215", "2025 bedrijfswinst 3997215 vs 1750433; tick1371; primary official NBB WVV 9901"),
        ("bud_vene_expl_2024", ENT, "2024", "1750433", "2024 bedrijfswinst 1750433 comparative; tick1371; primary official NBB WVV 9901"),
        ("bud_vene_fininc_2025", ENT, "2025", "364800", "2025 financiele opbrengsten 364800 (vlottende 364738 waarvan beleg 326011 + taxshelter 38727); tick1371; primary official NBB WVV 75"),
        ("bud_vene_fincost_2025", ENT, "2025", "114050", "2025 financiele kosten 114050 (schulden 121659 waarvan achtergesteld 108641); tick1371; primary official NBB WVV 65"),
        ("bud_vene_tax_2025", ENT, "2025", "1016653", "2025 belastingen 1016653 vs 498962; tick1371; primary official NBB WVV 67/77"),
        ("bud_vene_pnl_2025", ENT, "2025", "3231312", "2025 PnL 9904 3231312 vs 1404833; te bestemmen 2524032 overgedragen; tick1371; primary official NBB WVV"),
        ("bud_vene_pnl_2024", ENT, "2024", "1404833", "2024 PnL 1404833 comparative; tick1371; primary official NBB WVV 9904"),
        ("bud_vene_comm_2025", ENT, "2025", "14417", "2025 commissaris Figurad / Bart Meganck 14417; tick1371; primary official NBB WVV 9505"),
        ("bud_vene_board_2025", ENT, "2025", "", "2025 bestuurders 9503 empty (zitpenningen in diensten); tick1371; primary official NBB WVV 9503"),
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
                "title": "Veneco JR2025 leftover IGS dual (assets 51.98m / omzet 1.18m DROP / othops 5.27m / RE inv 23.12m / subord 10.34m)",
                "entity_id": ENT,
                "beneficiary": "Veneco / Gent-Meetjesland municipalities / provincie Oost-Vlaanderen (scheiding)",
                "legal_basis": "WVV DV; decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-06-10",
                "start_year": "1960",
                "end_year": "2034",
                "total_envelope_eur": "51983427",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL streek — 1.18m omzet DROP vs 9.98m / 5.27m othops / 23.12m RE / 10.34m achtergesteld tot 2035",
                "cut_option": "Publish 1.18m land-sale list + 23.12m remaining RE + 5.27m othops counterparties + 5.10m voorziening-vrijgave + 6.01m unnamed beleggingen + achtergesteld per vennoot; do not keep 51.98m municipal streek IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1371; assets 51983427 omzet 1184113 othops 5270686 inv 23116144 pnl 3231312; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Veneco JR2025 leftover IGS: assets 51.98m / omzet 1.18m DROP / othops 5.27m / RE inv 23.12m / subord 10.34m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "5270686",
                "total_cost_eur": "51983427",
                "tco_notes": (
                    "Leftover dual IGS DV of 20 A-vennoten Gent-Meetjesland: "
                    "assets 51.98m / equity 23.06m / pnl +3.23m / omzet 1.18m DROP vs 9.98m / 42.6 VTE / "
                    "othops 5.27m (740 subsidies 1.58m only) / RE inv 23.12m / "
                    "voorziening vrijgave 5.10m / achtergesteld 10.34m tot 2035 / invest 24.15m / "
                    "official NBB WVV live; "
                    "do not treat 51.98m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Veneco / Gent-Meetjesland municipalities",
                "stated_goal": "Local leftover IGS map VL streek — JR2025 live; dual omzet-DROP/othops/RE FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 51.98m / omzet 1.18m DROP / othops 5.27m / RE 23.12m / pnl +3.23m; invest 24.15m",
                "absurdity_score": "7.0",
                "cost_score": "5.6",
                "difficulty": "2.5",
                "priority_index": "6.3",
                "cut_proposal": "Publish 1.18m land-sale list + 23.12m remaining RE + 5.27m othops counterparties + 5.10m voorziening-vrijgave + 6.01m unnamed beleggingen + achtergesteld per vennoot; do not keep 51.98m municipal streek IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1371; leftover IGS DV of Gent-Meetjesland; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "omzet 1184113 DROP vs 9984485 (WVV 70; 6.10 category/geo empty; glossy verkopen gronden IZ 1173378 + woon 10735) per perceel "
                    "+ RE inventory 23116144 JUMP vs 21529677 (code 71 +2114421; WV voorraden netto 527954) completed-contract list "
                    "+ andere bedrijfsopbrengsten 5270686 (WVV 74; 740 subsidies 1577066 only; rest ~3.69m diensten/parkmgmt/lidgelden) "
                    "+ voorzieningen overige 12895089 / aanwending 5098819 (Innovatiefonds 3956211 / Campagne 3680284 / Prijkels 3312188) "
                    "+ geldbeleggingen 24148004 (termijn 9100000 + vastrentend 8542462 + other unnamed 6006019 + aandelen 499523) "
                    "+ achtergesteld 10337943 tot 2035 / 6.9 overheidsgarantie 10601026 / provincie scheidingsaandeel 279958 "
                    "+ 8761/8762 empty vs 6190 A + 20 B / toetreding Laarne 31500 + SML 20000 "
                    "+ 9503 bestuurders empty + 6.4.1/6.5.1/6.15/6.18 not filed + commissarisverslag image-only"
                ),
                "why_it_matters": (
                    "Leftover IGS DV of 20 A-vennoten Gent-Meetjesland "
                    "(same leftover-IGS seam as Haviland 1370 / Leiedal 1367 / Interleuven 1366 / IOK 1368 / SOLVA 1351): "
                    "51.98m assets / 1.18m omzet DROP vs 9.98m / 5.27m othops / 23.12m RE / "
                    "5.10m voorziening-vrijgave / 10.34m achtergesteld tot 2035 / 42.6 VTE / 6.10 empty "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "Veneco / Koenraad De Ceuninck / Elsie Sierens / Thomas Van Ongeval / Sofie Vandelannoote / Gent-Meetjesland municipalities",
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
                    "tick1371 leftover IGS DV of Gent-Meetjesland after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (24.1MB 282p deposit 2026-00188751). "
                    "Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. "
                    "Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 skipped. "
                    "Dommelhof leftover Limburg EVA not re-probed once live Veneco extracted. "
                    "Otary RS Nuhma-adjacent fallback not taken. "
                    "IGEMO 2026-00235028 / IVOO 2026-00271895 / MIWA 2026-00209388 2025 CDN still live — leftover next. "
                    "IVAREM still 2024. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1371",
        "title": "Veneco DV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Veneco leftover IGS DV of Gent-Meetjesland after honest hunt; KBO 0200.065.765 Actief; "
            "live JR2025 official NBB WVV VOL-inb PDF (24.1MB 282p deposit 2026-00188751; commissaris Figurad Meganck); "
            "sourced euros assets 51983427 / omzet 1184113 / othops 5270686 / inv 23116144 / pnl 3231312; "
            "FOI ready omzet 1.18m/othops 5.27m/inv 23.12m"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T01:15:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1371 Veneco leftover IGS residual; KBO 0200.065.765; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1372 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1372",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1371 done including Veneco 1371 leftover IGS live NBB WVV / "
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
            "IGEMO leftover IGS KBO 0213.349.124 — take if JR2025 CDN 2026-00235028 still live; "
            "IVOO KBO 0214.753.050 CDN 2026-00271895 / MIWA KBO 0218.239.409 CDN 2026-00209388 — take only if still live; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if a new live 2025 WVV PDF downloads (prefer leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; Otary CDN 2026-00254280 live prior tick, not taken); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1371 after Veneco leftover IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1371", rq_new, rq_spawn)
    print("research_queue 1371", found, "spawned_1372", spawned)

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
                "last_unit_id": "rq_1371",
                "ticks_completed": "1371",
                "paused": "no",
                "notes": (
                    "tick1371 Veneco leftover IGS residual; KBO 0200.065.765; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 51983427 omzet 1184113 othops 5270686 inv 23116144 pnl 3231312; "
                    "FOI ready omzet 1.18m/othops 5.27m/inv 23.12m; next rq_1372 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")
    print("tick1371 write done")


if __name__ == "__main__":
    main()

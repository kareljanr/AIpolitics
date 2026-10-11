# -*- coding: utf-8 -*-
"""Tick 1372 — leftover IGEMO JR2025 official NBB WVV euros.
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

TICK = "1372"
UTC = "2026-08-19T03:15:00Z"
ENT = "igs_igem"
HIER = "Vlaanderen>Antwerpen>IGS>IGEMO>MechelenRivierenland"
GAP = "gap_igem_omzet_5_98m_othops_3_00m_inv_19_61m_l5"
SRC = "src_igem_jr2025_nbb"
SRC2 = "src_igem_site"
SRC3 = "src_kbo_igem_0213349124"
SRC4 = "src_igem_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00235028.pdf"
SRC2_URL = "https://igemo.be/"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0213349124"
SRC4_URL = "https://igemo.be/contact/"
FOI_EMAIL = "info@igemo.be"
FOI_POSTAL = "Schoutetstraat 2 2800 Mechelen"
DRAFT = "docs/doge/foi/drafts/gap_igem_omzet_5_98m_othops_3_00m_inv_19_61m_l5.md"
COMM = "comm_igem_jr2025_pnl"
LB = "lb_igem_omzet_5_98m_othops_3_00m_inv_19_61m"


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
                "title": "IGEMO jaarrekening boekjaar 2025 (official NBB WVV VOL-kap deposit 2026-00235028; AV 12.06.2026)",
                "url": SRC_URL,
                "publisher": "IGEMO / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1372; official NBB VOL-kap PDF 944kB 52p deposit 2026-00235028 created 02.07.2026 header 29.06.2026; "
                    "leftover IGS DV of arrondissement Mechelen / Rivierenland municipalities; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Clybouw BV B00162 / Arnaud Clybouw A02273 6904 signed 27.05.2026; "
                    "6.1/6.4.1/6.5.1/6.11/6.14/6.17/6.18 not filed; 6.10 category/geo empty; not every-10"
                ),
            },
            {
                "source_id": SRC2,
                "title": "IGEMO official site (streekintercommunale arrondissement Mechelen / Rivierenland)",
                "url": SRC2_URL,
                "publisher": "IGEMO Intercommunale",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1372; leftover IGS streek of Mechelen-region municipalities + IVAREM + OCMW; "
                    "igemo.be has no isolated statutory 2025 balans PDF; statutory 2025 balans is the NBB CDN deposit"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO IGEMO 0213.349.124",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1372; KBO 0213.349.124 Actief / normale toestand since 02.06.1973; "
                    "statutaire naam Intercommunale voor Ontwikkeling van het Gewest Mechelen en Omgeving since 02.06.1973; "
                    "afkorting I.G.E.M.O. since 02.06.1973; Dienstverlenende vereniging (Vlaams Gewest) since 30.11.1993; "
                    "zetel Schoutetstraat 2 2800 Mechelen since 20.01.1999; 1 VE; "
                    "tel +3215285050; email info@igemo.be; web https://igemo.be/ since 05.05.2023; "
                    "btw since 01.03.1995; RSZ since 01.01.2022; aanbestedende overheid since 02.06.1973; "
                    "jaarvergadering mei; boekjaar 31 december; "
                    "16 KBO-bestuurders; algemeen directeur Peter De Bruyne; "
                    "NACE 70.100/68.122/68.121/68.203/84.119 + RSZ 38.110"
                ),
            },
            {
                "source_id": SRC4,
                "title": "IGEMO FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "IGEMO",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1372; FOI info@igemo.be / +32 15 28 50 50; "
                    "Schoutetstraat 2 2800 Mechelen; KBO also lists email/web/tel"
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
                "name_nl": "IGEMO (leftover dienstverlenende vereniging / IGS streek Mechelen-Rivierenland)",
                "name_fr": "IGEMO (association de services residuelle / IGS regionale Malines-Rivierenland)",
                "name_en": "IGEMO leftover Mechelen-Rivierenland regional IGS (service association)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://igemo.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1372 leftover residual IGS DV of arrondissement Mechelen / Rivierenland; "
                    "KBO 0213.349.124 Actief since 02.06.1973; official NBB WVV VOL-kap PDF downloads; "
                    "sourced euros assets 25436788 omzet 5983847 othops 3002243 inv 19614912 pnl 2729; "
                    "FOI ready omzet 5.98m/othops 3.00m/inv 19.61m"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_igem_assets_2025", ENT, "2025", "25436788", "2025 assets 25436788 VOL-kap 20/58; tick1372; primary official NBB WVV"),
        ("bud_igem_assets_2024", ENT, "2024", "25246628", "2024 assets 25246628 comparative; tick1372; primary official NBB WVV 20/58"),
        ("bud_igem_fixed_2025", ENT, "2025", "2773796", "2025 vaste activa 2773796 vs 3044542; tick1372; primary official NBB WVV 21/28"),
        ("bud_igem_iva_2025", ENT, "2025", "0", "2025 immateriele VA 0 vs 4951 after afschr 4951; tick1372; primary official NBB WVV 21"),
        ("bud_igem_mva_2025", ENT, "2025", "2768962", "2025 MVA 2768962 vs 3034757; tick1372; primary official NBB WVV 22/27"),
        ("bud_igem_buildings_2025", ENT, "2025", "2642621", "2025 terreinen en gebouwen 2642621 vs 2866165 after afschr 223544; tick1372; primary official NBB WVV 22"),
        ("bud_igem_machines_2025", ENT, "2025", "40576", "2025 installaties/machines 40576 vs 55335; tick1372; primary official NBB WVV 23"),
        ("bud_igem_rollend_2025", ENT, "2025", "85766", "2025 meubilair/rollend 85766 vs 113257; tick1372; primary official NBB WVV 24"),
        ("bud_igem_fva_2025", ENT, "2025", "4834", "2025 FVA 4834 (36 CIPAL + 15 POOLSTOK; 6.4.1/6.5.1 not filed); tick1372; primary official NBB WVV 28"),
        ("bud_igem_current_2025", ENT, "2025", "22662992", "2025 vlottende activa 22662992 vs 22202086; tick1372; primary official NBB WVV 29/58"),
        ("bud_igem_inv_2025", ENT, "2025", "19614912", "2025 voorraden 19614912 all onroerend bestemd voor verkoop; tick1372; primary official NBB WVV 3/35"),
        ("bud_igem_inv_2024", ENT, "2024", "18448128", "2024 RE inventory 18448128 comparative; tick1372; primary official NBB WVV 35"),
        ("bud_igem_strecv_2025", ENT, "2025", "2820384", "2025 ST vorderingen 2820384 (trade 2049965 waarvan op te stellen 846952 + other 770419); tick1372; primary official NBB WVV 40/41"),
        ("bud_igem_relrecv_2025", ENT, "2025", "598856", "2025 related-party ST recv 598856 vs 1068003; tick1372; primary official NBB WVV 6.15 9311"),
        ("bud_igem_cash_2025", ENT, "2025", "185705", "2025 liquide middelen 185705 vs 267189 THIN vs ST bank 13.91m; tick1372; primary official NBB WVV 54/58"),
        ("bud_igem_prepaid_2025", ENT, "2025", "41991", "2025 overlopend actief 41991 all over te dragen kosten; tick1372; primary official NBB WVV 490/1"),
        ("bud_igem_equity_2025", ENT, "2025", "5860763", "2025 eigen vermogen 5860763 vs 5858034; tick1372; primary official NBB WVV 10/15"),
        ("bud_igem_inbreng_2025", ENT, "2025", "714920", "2025 inbreng 714920 (kapitaal 648760 + premie 66160); geplaatst 793270 / niet-opgevraagd 144510; tick1372; primary official NBB WVV 10/11"),
        ("bud_igem_reserves_2025", ENT, "2025", "6405323", "2025 reserves 6405323 (onbeschikbaar 5668650 waarvan statutair 5571351 + wettelijk 97299; beschikbaar 736673); tick1372; primary official NBB WVV 13"),
        ("bud_igem_retained_2025", ENT, "2025", "-1259480", "2025 overgedragen verlies 1259480 continuity art 3:6 6 WVV; tick1372; primary official NBB WVV 14"),
        ("bud_igem_prov_2025", ENT, "2025", "989476", "2025 voorzieningen 989476 DROP vs 1482329 all overige 164/5; tick1372; primary official NBB WVV 16"),
        ("bud_igem_kavelprov_2025", ENT, "2025", "518968", "2025 voorziening toekomstige kosten verkochte kavels 518968; tick1372; primary official NBB WVV 6.8"),
        ("bud_igem_beheerprov_2025", ENT, "2025", "470507", "2025 provisie beheersfonds ontwikkelingsprojecten 470507; tick1372; primary official NBB WVV 6.8"),
        ("bud_igem_prov_used_2025", ENT, "2025", "527178", "2025 voorziening besteding/terugneming 527178 / toevoeging 34325 / netto 635/8 -492853; tick1372; primary official NBB WVV 6.10 9116"),
        ("bud_igem_debt_2025", ENT, "2025", "18586550", "2025 schulden 18586550 vs 17906265; tick1372; primary official NBB WVV 17/49"),
        ("bud_igem_lt_2025", ENT, "2025", "1795592", "2025 LT schulden 1795592 DROP vs 6941099 (bank 1592879 + borg 202713); tick1372; primary official NBB WVV 17"),
        ("bud_igem_ltbank_2025", ENT, "2025", "1592879", "2025 LT bank 1592879 (1-5y 546539 + >5y 1046340); tick1372; primary official NBB WVV 173"),
        ("bud_igem_st_2025", ENT, "2025", "16464406", "2025 ST schulden 16464406 JUMP vs 10362121; tick1372; primary official NBB WVV 42/48"),
        ("bud_igem_stbank_2025", ENT, "2025", "13905575", "2025 ST bank 13905575 JUMP vs 8072920; tick1372; primary official NBB WVV 430/8"),
        ("bud_igem_sttrade_2025", ENT, "2025", "1182180", "2025 leveranciers 1182180 vs 961331; tick1372; primary official NBB WVV 440/4"),
        ("bud_igem_sttaxsoc_2025", ENT, "2025", "944085", "2025 tax/soc 944085 (tax 152434 + wages 791650); tick1372; primary official NBB WVV 45"),
        ("bud_igem_othdebt_2025", ENT, "2025", "301398", "2025 overige ST schulden 301398 vs 277609; tick1372; primary official NBB WVV 47/48"),
        ("bud_igem_govg_2025", ENT, "2025", "13905575", "2025 door Belgische overheden gewaarborgde schulden 13905575 all ST bank; tick1372; primary official NBB WVV 6.9 9061"),
        ("bud_igem_accrued_2025", ENT, "2025", "326551", "2025 overlopend passief 326551 (opbr 11700 + startvergoedingen 50000 + subsidies 264851); tick1372; primary official NBB WVV 492/3"),
        ("bud_igem_ops_2025", ENT, "2025", "8986090", "2025 bedrijfsopbrengsten 8986090 vs 11786570; tick1372; primary official NBB WVV 70/76A"),
        ("bud_igem_omzet_2025", ENT, "2025", "5983847", "2025 omzet 5983847 DROP vs 8583564; 6.10 category/geo empty; tick1372; primary official NBB WVV 70"),
        ("bud_igem_omzet_2024", ENT, "2024", "8583564", "2024 omzet 8583564 comparative; tick1372; primary official NBB WVV 70"),
        ("bud_igem_othops_2025", ENT, "2025", "3002243", "2025 andere bedrijfsopbrengsten 3002243 vs 3203006; 740 subsidies 2881184 only; tick1372; primary official NBB WVV 74"),
        ("bud_igem_othops_2024", ENT, "2024", "3203006", "2024 andere bedrijfsopbrengsten 3203006 comparative; tick1372; primary official NBB WVV 74"),
        ("bud_igem_subs_2025", ENT, "2025", "2881184", "2025 exploitatiesubsidies 2881184 vs 2881394; notes granted 2722136 of which pass-through 644525 + deferred 264851; tick1372; primary official NBB WVV 6.10 740"),
        ("bud_igem_goods_2025", ENT, "2025", "2497799", "2025 handelsgoederen/grond-hulp 2497799 vs 4693646 (aankopen 3664584 / voorraad +1166784); tick1372; primary official NBB WVV 60"),
        ("bud_igem_diensten_2025", ENT, "2025", "718135", "2025 diensten 718135 vs 903805; tick1372; primary official NBB WVV 61"),
        ("bud_igem_pers_2025", ENT, "2025", "4909768", "2025 bezoldigingen 4909768 / 57.3 VTE / 82 koppen / YE 63.2 VTE; tick1372; primary official NBB WVV 62 9087"),
        ("bud_igem_deprec_2025", ENT, "2025", "285379", "2025 afschrijvingen 285379 (MVA 280428 + IVA 4951); tick1372; primary official NBB WVV 630"),
        ("bud_igem_othcost_2025", ENT, "2025", "652005", "2025 andere bedrijfskosten 652005 JUMP vs 61086 (tax 5962 + other 646043 JUMP vs 11423); tick1372; primary official NBB WVV 640/8"),
        ("bud_igem_expl_2025", ENT, "2025", "416397", "2025 bedrijfswinst 416397 vs 555738; tick1372; primary official NBB WVV 9901"),
        ("bud_igem_expl_2024", ENT, "2024", "555738", "2024 bedrijfswinst 555738 comparative; tick1372; primary official NBB WVV 9901"),
        ("bud_igem_fininc_2025", ENT, "2025", "874", "2025 financiele opbrengsten 874 vs 25781; tick1372; primary official NBB WVV 75/76B"),
        ("bud_igem_fincost_2025", ENT, "2025", "414542", "2025 financiele kosten 414542 (schulden 407749 + other 6793); tick1372; primary official NBB WVV 65"),
        ("bud_igem_pnl_2025", ENT, "2025", "2729", "2025 PnL 9904 2729 vs -38047; te bestemmen 2729 overgedragen; tick1372; primary official NBB WVV"),
        ("bud_igem_pnl_2024", ENT, "2024", "-38047", "2024 PnL -38047 comparative; tick1372; primary official NBB WVV 9904"),
        ("bud_igem_comm_2025", ENT, "2025", "6904", "2025 commissaris Clybouw / Arnaud Clybouw 6904; tick1372; primary official NBB WVV 9505"),
        ("bud_igem_board_2025", ENT, "2025", "60853", "2025 bestuurders 60853; tick1372; primary official NBB WVV 9503"),
        ("bud_igem_taxloss_2025", ENT, "2025", "3143949", "2025 actieve latenties fiscale verliezen 3143949; tick1372; primary official NBB WVV 6.13 9142"),
        ("bud_igem_claims_2025", ENT, "2025", "791000", "2025 unprovisioned social claims 75000+156000+560000; tick1372; primary official NBB WVV 6.20"),
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
                "title": "IGEMO JR2025 leftover IGS dual (assets 25.44m / omzet 5.98m DROP / othops 3.00m / RE inv 19.61m / ST bank 13.91m)",
                "entity_id": ENT,
                "beneficiary": "IGEMO / Mechelen-Rivierenland municipalities / IVAREM / OCMW",
                "legal_basis": "WVV DV; decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-06-12",
                "start_year": "1973",
                "end_year": "",
                "total_envelope_eur": "25436788",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL streek — 5.98m omzet DROP vs 8.58m / 3.00m othops / 19.61m RE / 13.91m ST-bank JUMP",
                "cut_option": "Publish 5.98m omzet split + 19.61m remaining RE + 3.00m othops/subsidy counterparties + 13.91m ST-bank/gemeentegarantie + 646k andere kosten + 791k social claims; do not keep 25.44m municipal streek IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1372; assets 25436788 omzet 5983847 othops 3002243 inv 19614912 pnl 2729; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "IGEMO JR2025 leftover IGS: assets 25.44m / omzet 5.98m DROP / othops 3.00m / RE inv 19.61m / ST bank 13.91m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "3002243",
                "total_cost_eur": "25436788",
                "tco_notes": (
                    "Leftover dual IGS DV of arrondissement Mechelen / Rivierenland: "
                    "assets 25.44m / equity 5.86m / pnl +2.7k / omzet 5.98m DROP vs 8.58m / 57.3 VTE / "
                    "othops 3.00m (740 subsidies 2.88m only) / RE inv 19.61m (77pct assets) / "
                    "ST bank 13.91m JUMP vs 8.07m / cash 0.19m / retained loss 1.26m continuity / "
                    "official NBB WVV live; "
                    "do not treat 25.44m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "IGEMO / Mechelen-Rivierenland municipalities",
                "stated_goal": "Local leftover IGS map VL streek — JR2025 live; dual omzet-DROP/othops/RE/ST-bank FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 25.44m / omzet 5.98m DROP / othops 3.00m / RE 19.61m / ST bank 13.91m / pnl +2.7k",
                "absurdity_score": "7.0",
                "cost_score": "5.0",
                "difficulty": "2.5",
                "priority_index": "6.1",
                "cut_proposal": "Publish 5.98m omzet split + 19.61m remaining RE + 3.00m othops/subsidy counterparties + 13.91m ST-bank/gemeentegarantie + 646k andere kosten + 791k social claims; do not keep 25.44m municipal streek IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1372; leftover IGS DV of Mechelen-Rivierenland; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "omzet 5983847 DROP vs 8583564 (WVV 70; 6.10 category/geo empty) per dienst/project "
                    "+ RE inventory 19614912 JUMP vs 18448128 (77.1pct of assets; code 609 -1166784) completed-contract list "
                    "+ andere bedrijfsopbrengsten 3002243 (WVV 74; 740 subsidies 2881184 only; notes granted 2722136 / pass-through 644525 / deferred 264851) "
                    "+ voorzieningen overige 989476 / besteding 527178 (kavels 518968 / beheersfonds 470507) "
                    "+ ST bank 13905575 JUMP vs 8072920 / LT bank 1592879 DROP vs 6724047 / 6.9 overheidsgarantie 13905575 vs cash 185705 "
                    "+ andere kosten 646043 JUMP vs 11423 + related-party ST recv 598856 "
                    "+ unprovisioned social claims 75000+156000+560000 + retained loss 1259480 continuity "
                    "+ 6.4.1/6.5.1/6.18 not filed + CIPAL 36 / POOLSTOK 15"
                ),
                "why_it_matters": (
                    "Leftover IGS DV of arrondissement Mechelen / Rivierenland municipalities "
                    "(same leftover-IGS seam as Veneco 1371 / Haviland 1370 / Leiedal 1367 / Interleuven 1366 / IOK 1368): "
                    "25.44m assets / 5.98m omzet DROP vs 8.58m / 3.00m othops / 19.61m RE / "
                    "13.91m ST-bank JUMP / 0.19m cash / 57.3 VTE / 6.10 empty "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "IGEMO / Raad van Bestuur / Peter De Bruyne / Mechelen-Rivierenland municipalities / IVAREM / OCMW",
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
                    "tick1372 leftover IGS DV of Mechelen-Rivierenland after honest hunt; "
                    "live JR2025 official NBB WVV VOL-kap PDF now extracted (944kB 52p deposit 2026-00235028). "
                    "Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. "
                    "IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 skipped. "
                    "Dommelhof leftover Limburg EVA not re-probed once live IGEMO extracted. "
                    "Otary RS Nuhma-adjacent fallback not taken. "
                    "IVOO 2026-00271895 / MIWA 2026-00209388 2025 CDN still live — leftover next. "
                    "IVAREM still 2024 (and is an IGEMO C-shareholder). NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1372",
        "title": "IGEMO DV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: IGEMO leftover IGS DV of Mechelen-Rivierenland after honest hunt; KBO 0213.349.124 Actief; "
            "live JR2025 official NBB WVV VOL-kap PDF (944kB 52p deposit 2026-00235028; commissaris Clybouw Arnaud); "
            "sourced euros assets 25436788 / omzet 5983847 / othops 3002243 / inv 19614912 / pnl 2729; "
            "FOI ready omzet 5.98m/othops 3.00m/inv 19.61m"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T02:10:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1372 IGEMO leftover IGS residual; KBO 0213.349.124; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1373 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1373",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1372 done including IGEMO 1372 leftover IGS live NBB WVV / "
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
            "IVOO leftover IGS KBO 0214.753.050 — take if JR2025 CDN 2026-00271895 still live; "
            "MIWA leftover IGS KBO 0218.239.409 CDN 2026-00209388 — take only if still live; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if a new live 2025 WVV PDF downloads (prefer leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; Otary CDN 2026-00254280 live prior tick, not taken); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1372 after IGEMO leftover IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1372", rq_new, rq_spawn)
    print("research_queue 1372", found, "spawned_1373", spawned)

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
                "last_unit_id": "rq_1372",
                "ticks_completed": "1372",
                "paused": "no",
                "notes": (
                    "tick1372 IGEMO leftover IGS residual; KBO 0213.349.124; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 25436788 omzet 5983847 othops 3002243 inv 19614912 pnl 2729; "
                    "FOI ready omzet 5.98m/othops 3.00m/inv 19.61m; next rq_1373 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")
    print("tick1372 write done")


if __name__ == "__main__":
    main()

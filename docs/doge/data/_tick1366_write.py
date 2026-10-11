# -*- coding: utf-8 -*-
"""Tick 1366 — leftover Interleuven JR2025 official NBB WVV euros.
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

TICK = "1366"
UTC = "2026-08-19T01:05:00Z"
ENT = "igs_ileu"
HIER = "Vlaanderen>Vlaams-Brabant>IGS>Interleuven>Streek"
GAP = "gap_ileu_omzet_11_68m_inv_36_05m_stbank_24_32m_l5"
SRC = "src_ileu_jr2025_nbb"
SRC2 = "src_ileu_site"
SRC3 = "src_kbo_ileu_0205774810"
SRC4 = "src_ileu_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00244206.pdf"
SRC2_URL = "https://www.interleuven.be/over-ons/publicaties"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0205774810"
SRC4_URL = "https://www.interleuven.be/contact"
FOI_EMAIL = "info@interleuven.be"
FOI_POSTAL = "Brouwersstraat 6 3000 Leuven"
DRAFT = "docs/doge/foi/drafts/gap_ileu_omzet_11_68m_inv_36_05m_stbank_24_32m_l5.md"
COMM = "comm_ileu_jr2025_pnl"
LB = "lb_ileu_omzet_11_68m_inv_36_05m_stbank"


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
                "title": "Interleuven jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00244206; AV 17.06.2026)",
                "url": SRC_URL,
                "publisher": "Interleuven / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1366; official NBB VOL-inb PDF 969kB 59p deposit 2026-00244206 created 29.06.2026 neerlegging 03.07.2026; "
                    "leftover IGS DV of mined Leuven-region / Oost-Brabant cities + EcoWerf 1357; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris Vyvey & C° B00523 / Steven Vyvey A01917 15750; "
                    "site still InDesign jaarverslag 2025 + jaarrekening 2024 only"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Interleuven official publications (2025 jaarverslag InDesign embed; statutory balans still 2024 on site)",
                "url": SRC2_URL,
                "publisher": "Interleuven",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1366; leftover IGS of mined Leuven-region cities; "
                    "interleuven.be/over-ons/publicaties has InDesign jaarverslag 2025 (AV 17.06.2026) but jaarrekening PDF still 2024 (2.47 MB); "
                    "statutory 2025 balans is the NBB CDN deposit not the site"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Interleuven 0205.774.810",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1366; KBO 0205.774.810 Actief / normale toestand since 08.07.1965; "
                    "statutaire naam Intercommunale Maatschappij voor de Ruimtelijke Ordening en de Economische Sociale Expansie van het Arrondissement Leuven / INTERLEUVEN; "
                    "Dienstverlenende vereniging (Vlaams Gewest) since 14.01.2004; "
                    "zetel Brouwersstraat 6 3000 Leuven since 21.10.1988; 1 VE; "
                    "btw since 01.04.1976; RSZ since 01.01.2022; aanbestedende overheid; "
                    "jaarvergadering mei; boekjaar 31 december; 16 functiehouders; "
                    "voorzitter Geert Cluckers / ondervoorzitter An Wouters since 19.03.2025; "
                    "dagelijks bestuur Jessica Vandebroek since 04.09.2024; no KBO email/web/tel; NACE 41.001/42.110/84.120/84.130"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Interleuven FOI channel / official contact",
                "url": SRC4_URL,
                "publisher": "Interleuven",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1366; FOI info@interleuven.be / 016 28 42 00; "
                    "Brouwersstraat 6 3000 Leuven; algemeen directeur Jessica Vandebroek jessica.vandebroek@interleuven.be; "
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
                "name_nl": "Interleuven (leftover dienstverlenende vereniging arrondissement Leuven / IGS streek- en projectontwikkeling Oost-Brabant)",
                "name_fr": "Interleuven (association prestataire de services residuelle arrondissement Louvain / IGS developpement regional)",
                "name_en": "Interleuven leftover Leuven-arrondissement service association (regional development IGS)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://www.interleuven.be/",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1366 leftover residual IGS DV of mined Leuven-region / Oost-Brabant cities "
                    "+ EcoWerf 1357 leftover waste IGS; "
                    "KBO 0205.774.810 Actief since 08.07.1965; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 95248547 omzet 11677203 pnl 417314; "
                    "FOI ready 6.10-geo/inv 36.05m/ST-bank 24.32m/leasing-mismatch/Loco 91.86pct/site-JR"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_ileu_assets_2025", ENT, "2025", "95248547", "2025 assets 95248547 VOL-inb 20/58; tick1366; primary official NBB WVV"),
        ("bud_ileu_assets_2024", ENT, "2024", "85713581", "2024 assets 85713581 comparative; tick1366; primary official NBB WVV 20/58"),
        ("bud_ileu_fixed_2025", ENT, "2025", "47533282", "2025 vaste activa 47533282; tick1366; primary official NBB WVV 21/28"),
        ("bud_ileu_mva_2025", ENT, "2025", "47326149", "2025 MVA 47326149 (machines 245766 + meubilair 372296 + leasing 23814256 + overige 22893831); tick1366; primary official NBB WVV 22/27"),
        ("bud_ileu_lease_2025", ENT, "2025", "23814256", "2025 leasing en soortgelijke rechten 23814256 vs 24627401; leasing-schulden empty; tick1366; primary official NBB WVV 25"),
        ("bud_ileu_othmva_2025", ENT, "2025", "22893831", "2025 overige MVA 22893831 vs 20251926; tick1366; primary official NBB WVV 26"),
        ("bud_ileu_fva_2025", ENT, "2025", "207133", "2025 FVA 207133 (Loco Tervuren 11685 + andere 195448); tick1366; primary official NBB WVV 28"),
        ("bud_ileu_loco_2025", ENT, "2025", "11685", "2025 Loco Tervuren cv 1033031192 91.86pct / 2337 aandelen book 11685 EV/PnL empty; tick1366; primary official NBB WVV 280 6.5.1"),
        ("bud_ileu_current_2025", ENT, "2025", "47715265", "2025 vlottende activa 47715265 vs 39999358; tick1366; primary official NBB WVV 29/58"),
        ("bud_ileu_ltrecv_2025", ENT, "2025", "4817118", "2025 LT overige vorderingen 4817118 vs 4143047; tick1366; primary official NBB WVV 291"),
        ("bud_ileu_inv_2025", ENT, "2025", "36144799", "2025 voorraden 36144799 vs 30213269; tick1366; primary official NBB WVV 30/36"),
        ("bud_ileu_reinv_2025", ENT, "2025", "36049928", "2025 onroerende goederen bestemd voor verkoop 36049928 JUMP vs 30140703; tick1366; primary official NBB WVV 35"),
        ("bud_ileu_strecv_2025", ENT, "2025", "6443875", "2025 ST vorderingen 6443875 (trade 2996967 + other 3446908); tick1366; primary official NBB WVV 40/41"),
        ("bud_ileu_cash_2025", ENT, "2025", "288638", "2025 liquide middelen 288638 vs 311361 THIN vs ST bank 24.32m; tick1366; primary official NBB WVV 54/58"),
        ("bud_ileu_equity_2025", ENT, "2025", "23387441", "2025 eigen vermogen 23387441 vs 22442333; tick1366; primary official NBB WVV 10/15"),
        ("bud_ileu_inbreng_2025", ENT, "2025", "2662088", "2025 onbeschikbare inbreng 2662088 / 156917 aandelen op naam; tick1366; primary official NBB WVV 111 8702"),
        ("bud_ileu_reserves_2025", ENT, "2025", "18777651", "2025 reserves 18777651 (onbeschikbaar 12567678 + belastingvrij 6209973); tick1366; primary official NBB WVV 13"),
        ("bud_ileu_capsub_2025", ENT, "2025", "1328119", "2025 kapitaalsubsidies 1328119 vs 800325 unnamed grantor; tick1366; primary official NBB WVV 15"),
        ("bud_ileu_prov_2025", ENT, "2025", "6880084", "2025 voorzieningen+uitgesteld 6880084 (risks 4810093 + deferred tax 2069991); tick1366; primary official NBB WVV 16"),
        ("bud_ileu_dispute_2025", ENT, "2025", "1062767", "2025 voorziening hangende geschillen 1062767; tick1366; primary official NBB WVV 6.8"),
        ("bud_ileu_env_2025", ENT, "2025", "443960", "2025 voorziening milieuproblematiek 443960; tick1366; primary official NBB WVV 6.8"),
        ("bud_ileu_debt_2025", ENT, "2025", "64981022", "2025 schulden 64981022 JUMP vs 55740882; tick1366; primary official NBB WVV 17/49"),
        ("bud_ileu_lt_2025", ENT, "2025", "32973092", "2025 LT schulden 32973092 (fin 32028796 banks 27511355 + other loans 4517441 + other 944296); tick1366; primary official NBB WVV 17"),
        ("bud_ileu_st_2025", ENT, "2025", "31388263", "2025 ST schulden 31388263 JUMP vs 21217611; tick1366; primary official NBB WVV 42/48"),
        ("bud_ileu_stbank_2025", ENT, "2025", "24322614", "2025 ST financieel kredietinstellingen 24322614 JUMP vs 14822614; tick1366; primary official NBB WVV 43 430/8"),
        ("bud_ileu_stbank_2024", ENT, "2024", "14822614", "2024 ST financieel 14822614 comparative; tick1366; primary official NBB WVV 43"),
        ("bud_ileu_sttrade_2025", ENT, "2025", "1174198", "2025 leveranciers 1174198; tick1366; primary official NBB WVV 440/4"),
        ("bud_ileu_stadv_2025", ENT, "2025", "536870", "2025 vooruitbetalingen op bestellingen 536870; tick1366; primary official NBB WVV 46"),
        ("bud_ileu_govg_2025", ENT, "2025", "14610761", "2025 door Belgische overheidsinstellingen gewaarborgde bankschuld 14610761; tick1366; primary official NBB WVV 9061"),
        ("bud_ileu_coll_2025", ENT, "2025", "14880007", "2025 zakelijke zekerheden op eigen activa 14880007; tick1366; primary official NBB WVV 8922"),
        ("bud_ileu_ops_2025", ENT, "2025", "24491518", "2025 bedrijfsopbrengsten 24491518; tick1366; primary official NBB WVV 70/76A"),
        ("bud_ileu_omzet_2025", ENT, "2025", "11677203", "2025 omzet 11677203; 6.10 category filed geo empty; tick1366; primary official NBB WVV 70"),
        ("bud_ileu_omzet_2024", ENT, "2024", "8653453", "2024 omzet 8653453 comparative; tick1366; primary official NBB WVV 70"),
        ("bud_ileu_invinc_2025", ENT, "2025", "5909224", "2025 voorraadtoename 5909224 vs 1380494; tick1366; primary official NBB WVV 71"),
        ("bud_ileu_othops_2025", ENT, "2025", "6895584", "2025 andere bedrijfsopbrengsten 6895584 DROP vs 14359399; subsidies 913054 only; tick1366; primary official NBB WVV 74"),
        ("bud_ileu_othops_2024", ENT, "2024", "14359399", "2024 andere bedrijfsopbrengsten 14359399 comparative; tick1366; primary official NBB WVV 74"),
        ("bud_ileu_sub_2025", ENT, "2025", "913054", "2025 exploitatiesubsidies/overheidscompensatie 913054 vs 235291; tick1366; primary official NBB WVV 740"),
        ("bud_ileu_opscost_2025", ENT, "2025", "22161751", "2025 bedrijfskosten 22161751 vs 14340170; tick1366; primary official NBB WVV 60/66A"),
        ("bud_ileu_goods_2025", ENT, "2025", "7839057", "2025 handelsgoederen/grond-hulp 7839057 JUMP vs 1979295; tick1366; primary official NBB WVV 60"),
        ("bud_ileu_diensten_2025", ENT, "2025", "4262119", "2025 diensten 4262119; tick1366; primary official NBB WVV 61"),
        ("bud_ileu_pers_2025", ENT, "2025", "6641468", "2025 bezoldigingen 6641468 / 70 VTE / 78 koppen; tick1366; primary official NBB WVV 62 9087"),
        ("bud_ileu_deprec_2025", ENT, "2025", "2464158", "2025 afschrijvingen 2464158; tick1366; primary official NBB WVV 630"),
        ("bud_ileu_nrcost_2025", ENT, "2025", "1169259", "2025 niet-recurrente bedrijfskosten 1169259 JUMP vs 21299; tick1366; primary official NBB WVV 66A 664/7"),
        ("bud_ileu_expl_2025", ENT, "2025", "2329767", "2025 bedrijfswinst 2329767 DROP vs 10119732; tick1366; primary official NBB WVV 9901"),
        ("bud_ileu_fincost_2025", ENT, "2025", "1810380", "2025 financiele kosten 1810380 (schulden 1783136); tick1366; primary official NBB WVV 65"),
        ("bud_ileu_tax_2025", ENT, "2025", "279169", "2025 belastingen 279169 vs 54848; tick1366; primary official NBB WVV 67/77"),
        ("bud_ileu_pnl_2025", ENT, "2025", "417314", "2025 PnL 9904 417314 DROP vs 5975250; te bestemmen 603852; tick1366; primary official NBB WVV"),
        ("bud_ileu_pnl_2024", ENT, "2024", "5975250", "2024 PnL 5975250 comparative; tick1366; primary official NBB WVV 9904"),
        ("bud_ileu_board_2025", ENT, "2025", "60676", "2025 bestuurdersbezoldiging 60676; tick1366; primary official NBB WVV 9503"),
        ("bud_ileu_comm_2025", ENT, "2025", "15750", "2025 commissaris Vyvey 15750; tick1366; primary official NBB WVV 9505"),
        ("bud_ileu_cat_re_2025", ENT, "2025", "5525970", "2025 6.10 grondbeleid/vastgoedbeheer 5525970; tick1366; primary official NBB WVV 6.10"),
        ("bud_ileu_cat_gem_2025", ENT, "2025", "2469134", "2025 6.10 werken voor gemeenten 2469134; tick1366; primary official NBB WVV 6.10"),
        ("bud_ileu_cat_mil_2025", ENT, "2025", "1803792", "2025 6.10 milieudienst 1803792; tick1366; primary official NBB WVV 6.10"),
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
                "title": "Interleuven JR2025 leftover IGS dual (assets 95.25m / omzet 11.68m / inventory 36.05m / ST bank 24.32m)",
                "entity_id": ENT,
                "beneficiary": "Interleuven / Loco Tervuren cv / Leuven-region municipalities / EcoWerf",
                "legal_basis": "WVV DV; decreet lokaal bestuur; Bestuursdecreet openbaarheid; NBB neerlegging",
                "decision_date": "2026-06-17",
                "start_year": "1965",
                "end_year": "2026",
                "total_envelope_eur": "95248547",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL streek/project — 36.05m RE inventory / 24.32m ST bank vs 0.29m cash / 91.86pct Loco no consolidation",
                "cut_option": "Publish 6.10 geo + 36.05m project list + put 24.32m ST bank vs 0.29m cash on the record + reconcile 23.81m leasing-MVA vs empty leasing-debt + 91.86pct Loco Tervuren consolidation + site statutory JR; do not keep 95.25m municipal streek IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1366; assets 95248547 omzet 11677203 pnl 417314; FOI ready not sent; not every-10",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Interleuven JR2025 leftover IGS: assets 95.25m / omzet 11.68m / inventory 36.05m / ST bank 24.32m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "24322614",
                "total_cost_eur": "95248547",
                "tco_notes": (
                    "Leftover dual IGS DV of mined Leuven-region municipalities: "
                    "assets 95.25m / equity 23.39m / pnl 0.42m DROP vs 5.98m / omzet 11.68m / 70 VTE / "
                    "inventory RE 36.05m / ST bank 24.32m JUMP vs cash 0.29m / "
                    "leasing-MVA 23.81m vs leasing-debt 0 / 91.86pct Loco Tervuren no consolidation / official NBB WVV live; "
                    "do not treat 95.25m as TE-additive of 348bn"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Interleuven / Loco Tervuren cv / Leuven-region municipalities / EcoWerf",
                "stated_goal": "Local leftover IGS map VL streek/project — JR2025 live; dual inventory/ST-bank/Loco FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 95.25m / omzet 11.68m / pnl 0.42m; inventory 36.05m; ST bank 24.32m vs cash 0.29m",
                "absurdity_score": "7.3",
                "cost_score": "7.1",
                "difficulty": "2.5",
                "priority_index": "6.8",
                "cut_proposal": "Publish 6.10 geo + 36.05m project list + put 24.32m ST bank vs 0.29m cash on the record + reconcile 23.81m leasing-MVA vs empty leasing-debt + 91.86pct Loco Tervuren consolidation + site statutory JR; do not keep 95.25m municipal streek IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1366; leftover IGS DV of mined Leuven-region + EcoWerf 1357; FOI ready not sent; not TE-additive of 348bn; not every-10",
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
                    "6.10 omzet 11677203 geo split empty (category filed: grondbeleid 5525970 / werken gemeenten 2469134 / milieu 1803792 / training 746867 / veiligheid 1059912 / digiloket 71527) "
                    "+ per-gemeente/Loco Tervuren/EcoWerf counterparties "
                    "+ andere bedrijfsopbrengsten 6895584 DROP vs 14359399 of which subsidies 913054 only (~5982530 unnamed) "
                    "+ inventory RE for sale 36049928 JUMP vs 30140703 + voorraadtoename 5909224 + aankopen 7861362 project list "
                    "+ ST bank 24322614 JUMP vs 14822614 vs cash 288638 "
                    "+ leasing-MVA 23814256 vs leasing-schulden 172/8831 empty "
                    "+ niet-recurrente kosten 1169259 JUMP vs 21299 + geschillen 1062767 + milieu 443960 "
                    "+ Loco Tervuren cv 1033031192 91.86pct book 11685 EV/PnL empty + no consolidation 6.18.1 exemption unmotivated + 6.15 related-party empty "
                    "+ gov-guaranteed bank 14610761 + zakelijke zekerheden 14880007 + kapitaalsubsidies 1328119 unnamed grantor "
                    "+ 156917 aandelen / per-vennoot inleg/stem "
                    "+ official-site JR (interleuven.be still 2024 balans / InDesign 2025 glossy)"
                ),
                "why_it_matters": (
                    "Leftover IGS DV of mined Leuven-region / Oost-Brabant cities + EcoWerf 1357 "
                    "(same leftover-IGS seam as Interwaas 1350 / SOLVA 1351 / IGEAN 1341): "
                    "95.25m assets / 11.68m omzet / 0.42m pnl DROP vs 5.98m / 70 VTE / "
                    "36.05m RE inventory / 24.32m ST bank vs 0.29m cash / "
                    "23.81m leasing-MVA vs empty leasing-debt / 91.86pct Loco Tervuren no consolidation / site still 2024 balans "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "7",
                "recipient_body": "Interleuven / Jessica Vandebroek / Leuven-region municipalities",
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
                    "tick1366 leftover IGS DV of mined Leuven-region / Oost-Brabant cities + EcoWerf 1357 after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (969kB 59p deposit 2026-00244206). "
                    "Dommelhof leftover Limburg EVA KBO 0777.495.085 still no 2025/2026 PDF — skipped. "
                    "s-Lim DV already mined 1365 — skipped. Herkenrode already mined 1364 — skipped. "
                    "Nuhma-group seam 1353-1365 skipped. AGB MAC already mined 1270 — skipped. Westtoer already mined — skipped. "
                    "IOK/IMOG/Haviland still 2024. POM Limburg glossy-only. Veneco/Leiedal glossy. NBB consult skipped. "
                    "Belscope/Companyweb euros not used. ready not sent; not every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1366",
        "title": "Interleuven JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Interleuven leftover IGS DV of mined Leuven-region / Oost-Brabant cities "
            "+ EcoWerf 1357 after honest hunt; KBO 0205.774.810 Actief; "
            "live JR2025 official NBB WVV VOL-inb PDF (969kB 59p deposit 2026-00244206; commissaris Vyvey); "
            "sourced euros assets 95248547 / omzet 11677203 / pnl 417314; "
            "FOI ready 6.10-geo/inv 36.05m/ST-bank 24.32m/leasing-mismatch/Loco 91.86pct/site-JR"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T00:45:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1366 Interleuven leftover IGS residual; KBO 0205.774.810; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1367 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1367",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1366 done including Interleuven 1366 leftover IGS live NBB WVV / "
            "s-Lim DV 1365 leftover IGS live NBB WVV / "
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
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if a new live 2025 WVV PDF downloads (Otary RS Staatsbladmonitor 2025 live as of 1366 but prefer leftover AGB/zorg/EVA/IGS/APB outside Nuhma first); "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB De Nekker / APB PIH / APB Inovant / APB Atlas listed or leftover but no PDF bytes — take only if a real PDF downloads; "
            "IOK / IMOG / Haviland still 2024 — take only if a 2025 JR PDF now downloads; "
            "Veneco / Leiedal / IVOO / MIROM / INCOVO / IVAGO / MIWA / IVAREM / IGEMO — take only if a statutory 2025 WVV/BBC PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1366 after Interleuven leftover IGS live NBB WVV; next residual dual L5 VL; next every-10 is 1370",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1366", rq_new, rq_spawn)
    print("research_queue 1366", found, "spawned_1367", spawned)

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
                "last_unit_id": "rq_1366",
                "ticks_completed": "1366",
                "paused": "no",
                "notes": (
                    "tick1366 Interleuven leftover IGS residual; KBO 0205.774.810; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 95248547 omzet 11677203 pnl 417314; "
                    "FOI ready 6.10-geo/inv 36.05m/ST-bank 24.32m/leasing-mismatch/Loco 91.86pct; next rq_1367 residual dual L5 VL; continuous hole_fill; next every-10 is 1370"
                ),
            }
        )
    print("loop_state ok")

    log_entry = """
### Tick 1366 - 2026-08-19 - rq_1366 Interleuven dual residual leftover
- Unit: Interleuven (leftover dienstverlenende vereniging / IGS streek- en projectontwikkeling of mined Leuven-region / Oost-Brabant municipalities: Leuven / Tremelo / Diest / Landen / Tienen / Begijnendijk / Holsbeek / Boutersem / Tervuren / Hoegaarden / Zoutleeuw / Bekkevoort) + leftover IGS EcoWerf tick1357 after residual dual hunt (KBO **0205.774.810**; official interleuven.be still InDesign jaarverslag 2025 embed + jaarrekening 2024 only; live NBB WVV VOL-inb deposit **2026-00244206** PDF 969kB / 59p; AV **17.06.2026**; PDF created **29.06.2026**; neerlegging **03.07.2026**; commissaris Vyvey & C° Bedrijfsrevisoren BV B00523 / Steven Vyvey A01917 15.750). Leftover IGS DV whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; last tick listed leftover Interleuven only if a 2025 balans PDF now downloads). Distinct from already-mined s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270. KBO Actief / normale toestand since **08.07.1965**; statutaire naam INTERLEUVEN; Dienstverlenende vereniging (Vlaams Gewest) since 14.01.2004; zetel Brouwersstraat 6 3000 Leuven since 21.10.1988; **1 VE**; btw since 01.04.1976; jaarvergadering mei; 16 functiehouders; voorzitter Geert Cluckers / ondervoorzitter An Wouters since 19.03.2025; dagelijks bestuur Jessica Vandebroek since 04.09.2024; e-mail info@interleuven.be; NACE 41.001/42.110/84.120/84.130. Hunt leftover AGB/zorg/EVA first: Dommelhof leftover Limburg EVA KBO 0777.495.085 still no 2025/2026 jaarrekening on Staatsbladmonitor (only 2021-2023 Staatsblad akten) — skipped; AGB MAC Mechelen 2025 BBC already mined tick1270 — skipped; AGB Genk / AGB Mortsel / ZOG Genk already mined — skipped; Westtoer APB already mined — skipped; Nuhma-group seam 1353-1365 already mined — skipped; Interleuven statutory CDN live this tick (HTTP 200 / 969099 / 59p) — taken. IOK/IMOG/Haviland still 2024; POM Limburg glossy-only — not taken; Veneco/Leiedal glossy-only; IVAREM/IGEMO activiteitenverslag only; IVOO no public 2025 JR. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE no fetchable 2025 JR this tick. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350. Not every-10 (next 1370).
- EUR strong (primary official WVV VOL-inb; commissaris Vyvey 15.750): assets **95.248.547** (was 85.713.581); fixed **47.533.282** / MVA **47.326.149** (leasing **23.814.256** + overige MVA **22.893.831**; machines 245.766 + meubilair 372.296); FVA **207.133** (Loco Tervuren cv 1033.031.192 **91,86%** / 2.337 aandelen book **11.685** — EV/PnL empty in 6.5.1; andere FVA 195.448); current **47.715.265**; LT recv **4.817.118**; inventory **36.144.799** waarvan onroerend bestemd voor verkoop **36.049.928 JUMP** vs 30.140.703; ST recv **6.443.875** (trade 2.996.967 + other 3.446.908); cash **288.638** vs 311.361 THIN vs ST bank 24.32m; equity **23.387.441** (inbreng 2.662.088 onbeschikbaar / 156.917 aandelen; herwaard 619.583; reserves 18.777.651; kapitaalsubsidies **1.328.119** vs 800.325); voorzieningen **6.880.084** (risks 4.810.093 waarvan geschillen **1.062.767** + milieu **443.960**; deferred tax 2.069.991); schulden **64.981.022 JUMP** vs 55.740.882 (LT fin **32.028.796** banks 27.511.355 + other loans 4.517.441; ST **31.388.263** waarvan ST bank **24.322.614 JUMP** vs 14.822.614 + leveranciers 1.174.198 + vooruit 536.870); gov-guarantee **14.610.761** / zakelijke zekerheden **14.880.007**; omzet **11.677.203** (6.10 category: grondbeleid 5.525.970 / werken gemeenten 2.469.134 / milieu 1.803.792 / training 746.867 / veiligheid 1.059.912 / digiloket 71.527; geo empty; comparative 8.653.453); andere opbr **6.895.584 DROP** vs 14.359.399 (subsidies 913.054 only); voorraadtoename **5.909.224**; goods **7.839.057 JUMP** vs 1.979.295; diensten 4.262.119; pers **6.641.468** / **70 VTE** / 78 koppen; afschr 2.464.158; nr-kosten **1.169.259 JUMP** vs 21.299; expl **2.329.767 DROP** vs 10.119.732; fin kosten **1.810.380**; belasting 279.169; PnL **417.314 DROP** vs 5.975.250; te bestemmen 603.852; bestuurders 60.676. Geen consolidatie (6.18.1 vrijgesteld, reden leeg) ondanks 91,86% Loco Tervuren. 6.15 related-party empty. Leasing-MVA 23,81m vs leasing-schulden empty.
- CSVs: sources+4/entities+1/budgets+53/commitments+1/leaderboard+1 + FOI ready `gap_ileu_omzet_11_68m_inv_36_05m_stbank_24_32m_l5` (not sent); rq_1366=done; spawn rq_1367; ticks=1366.
- Coverage: residual dual L5 (Interleuven leftover IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. No progress refresh (not every-10; next 1370).
- Next: rq_1367 residual dual L5 VL JR2025 hole_fill (prefer leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS / Rematics / Sunfin only if a new live 2025 WVV PDF downloads; leftover APB POA / TPA / De Schorre / Warande / De Nekker / PIH / Inovant / Atlas only if a real PDF downloads; IOK/IMOG/Haviland only if a 2025 JR PDF now downloads; Leiedal/Veneco/IVOO/MIWA/IVAREM/IGEMO only if a WVV/BBC PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1366 write done")


if __name__ == "__main__":
    main()

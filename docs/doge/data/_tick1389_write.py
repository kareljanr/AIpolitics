# -*- coding: utf-8 -*-
"""Tick 1389 — leftover Fluvius Zenne-Dijle JR2025 official NBB WVV euros.
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

TICK = "1389"
UTC = "2026-08-19T05:30:00Z"
ENT = "igs_flzd"
HIER = "Vlaanderen>VlaamsBrabant>IGS>FluviusZenneDijle"
GAP = "gap_flzd_omzet_354_23m_diensten_124_68m_debt_1_97bn_l5"
SRC = "src_flzd_jr2025_nbb"
SRC2 = "src_flzd_site"
SRC3 = "src_kbo_flzd_0222343301"
SRC4 = "src_flzd_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00206993.pdf"
SRC2_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-zenne-dijle/activiteitenverslagen"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0222343301"
SRC4_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-zenne-dijle"
FOI_EMAIL = ""
FOI_POSTAL = "Diestsesteenweg 126 3210 Lubbeek"
DRAFT = "docs/doge/foi/drafts/gap_flzd_omzet_354_23m_diensten_124_68m_debt_1_97bn_l5.md"
COMM = "comm_flzd_jr2025_pnl"
LB = "lb_flzd_omzet_354_23m_diensten_124_68m_debt_1_97bn"

VENNOTEN = (
    "Aarschot + Begijnendijk + Bekkevoort + Berlaar + Bertem + "
    "Bierbeek + Bonheiden + Boortmeerbeek + Bornem + Boutersem + "
    "Diest + Geetbets + Glabbeek + Haacht + Heist-op-den-Berg + "
    "Herent + Herselt + Hoegaarden + Hoeilaart + Holsbeek + "
    "Huldenberg + Hulshout + Kampenhout + Keerbergen + Kortenaken + "
    "Kortenberg + Landen + Leuven + Linter + Lubbeek + Mechelen + "
    "Oud-Heverlee + Overijse + Putte + Puurs-Sint-Amands + Rotselaar + "
    "Scherpenheuvel-Zichem + Sint-Katelijne-Waver + Tervuren + "
    "Tielt-Winge + Tienen + Tremelo + Willebroek + Zoutleeuw"
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
    ("bud_flzd_assets_2025", "2025", "2521878483", "2025 assets 2521878483 VOL-inb 20/58; tick1389; primary official NBB WVV"),
    ("bud_flzd_assets_2024", "2024", "2310551331", "2024 assets 2310551331 comparative (ex-Iverlek); tick1389; primary official NBB WVV 20/58"),
    ("bud_flzd_fixed_2025", "2025", "1696031777", "2025 vaste activa 1696031777 vs 2064960567; tick1389; primary official NBB WVV 21/28"),
    ("bud_flzd_iva_2025", "2025", "13232548", "2025 IVA 13232548 vs 16829444; tick1389; primary official NBB WVV 21"),
    ("bud_flzd_iva_acq_2025", "2025", "11031160", "2025 IVA aanschaf 11031160 (8021); tick1389; primary official NBB WVV 6.2.1"),
    ("bud_flzd_mva_2025", "2025", "1590822866", "2025 MVA 1590822866 vs 1948158658; tick1389; primary official NBB WVV 22/27"),
    ("bud_flzd_buildings_2025", "2025", "36396750", "2025 terreinen/gebouwen 36396750 vs 30393740; tick1389; primary official NBB WVV 22"),
    ("bud_flzd_buildings_acq_2025", "2025", "22082588", "2025 gebouwen aanschaf 22082588 (8161); tick1389; primary official NBB WVV 6.3.1"),
    ("bud_flzd_machines_2025", "2025", "1398735216", "2025 machines 1398735216 vs 1735260932; tick1389; primary official NBB WVV 23"),
    ("bud_flzd_machines_acq_2025", "2025", "386448825", "2025 machines aanschaf 386448825 (8162; merger/transfer inflated); tick1389; primary official NBB WVV 6.3.2"),
    ("bud_flzd_furniture_2025", "2025", "8570911", "2025 meubilair 8570911 vs 9688979; tick1389; primary official NBB WVV 24"),
    ("bud_flzd_lease_mva_2025", "2025", "9610720", "2025 leasing MVA 9610720 vs 12755637; tick1389; primary official NBB WVV 25"),
    ("bud_flzd_other_mva_2025", "2025", "558797", "2025 overige MVA 558797 vs 129928; tick1389; primary official NBB WVV 26"),
    ("bud_flzd_cip_2025", "2025", "136950472", "2025 CIP 136950472 vs 159929442; tick1389; primary official NBB WVV 27"),
    ("bud_flzd_cip_acq_2025", "2025", "188063051", "2025 CIP aanschaf 188063051 (8166); tick1389; primary official NBB WVV 6.3.6"),
    ("bud_flzd_fva_2025", "2025", "91976363", "2025 FVA 91976363 vs 99972465; tick1389; primary official NBB WVV 28"),
    ("bud_flzd_fva_part_2025", "2025", "39298047", "2025 FVA deelnemingen 39298047 FSO 7.09pct K-SYN / 10.75pct A / Transco 11.11pct; tick1389; primary official NBB WVV 282"),
    ("bud_flzd_fva_shares_2025", "2025", "52678316", "2025 andere FVA aandelen 52678316 vs 84863978; tick1389; primary official NBB WVV 284"),
    ("bud_flzd_current_2025", "2025", "825846706", "2025 vlottend 825846706 JUMP vs 245590764; tick1389; primary official NBB WVV 29/58"),
    ("bud_flzd_ltrecv_2025", "2025", "578103637", "2025 LT vorderingen 578103637 JUMP vs 17395268; tick1389; primary official NBB WVV 29"),
    ("bud_flzd_wip_2025", "2025", "5364112", "2025 bestellingen in uitvoering 5364112 vs 4473767; tick1389; primary official NBB WVV 37"),
    ("bud_flzd_strecv_2025", "2025", "171400464", "2025 ST vorderingen 171400464 vs 145832840; tick1389; primary official NBB WVV 40/41"),
    ("bud_flzd_trade_2025", "2025", "59003055", "2025 handelsvorderingen 59003055 vs 45149056; tick1389; primary official NBB WVV 40"),
    ("bud_flzd_othrecv_2025", "2025", "112397409", "2025 overige ST vorderingen 112397409 vs 100683784; tick1389; primary official NBB WVV 41"),
    ("bud_flzd_cash_2025", "2025", "1239", "2025 liquide middelen 1239 vs 1115; tick1389; primary official NBB WVV 54/58"),
    ("bud_flzd_prepaid_2025", "2025", "70977254", "2025 overlopend actief 70977254 vs 77887773; tick1389; primary official NBB WVV 490/1"),
    ("bud_flzd_prepaid_reg_2025", "2025", "18717862", "2025 prepaid regulatoire VNR-gas 18717862; tick1389; primary official NBB WVV 6.6"),
    ("bud_flzd_equity_2025", "2025", "554585848", "2025 EV 554585848 vs 638770889; tick1389; primary official NBB WVV 10/15"),
    ("bud_flzd_equity_2024", "2024", "638770889", "2024 EV 638770889 comparative; tick1389; primary official NBB WVV 10/15"),
    ("bud_flzd_inbreng_2025", "2025", "179859315", "2025 inbreng 179859315 vs 281706031; tick1389; primary official NBB WVV 10/11"),
    ("bud_flzd_reval_2025", "2025", "101585074", "2025 herwaarderingsmeerwaarden 101585074 vs 125854102; tick1389; primary official NBB WVV 12"),
    ("bud_flzd_reserves_2025", "2025", "226455748", "2025 reserves 226455748 vs 192589040; tick1389; primary official NBB WVV 13"),
    ("bud_flzd_retained_2025", "2025", "46441215", "2025 overgedragen 46441215 vs 37568498; tick1389; primary official NBB WVV 14"),
    ("bud_flzd_capsub_2025", "2025", "244496", "2025 kapitaalsubsidies 244496 vs 1053218; tick1389; primary official NBB WVV 15"),
    ("bud_flzd_prov_2025", "2025", "1636228", "2025 voorzieningen+uitgesteld 1636228 vs 669549; tick1389; primary official NBB WVV 16"),
    ("bud_flzd_debt_2025", "2025", "1965656407", "2025 schulden 1965656407 vs 1671110893; tick1389; primary official NBB WVV 17/49"),
    ("bud_flzd_debt_2024", "2024", "1671110893", "2024 schulden 1671110893 comparative; tick1389; primary official NBB WVV 17/49"),
    ("bud_flzd_lt_2025", "2025", "1679231766", "2025 LT schulden 1679231766 vs 1482272752; tick1389; primary official NBB WVV 17"),
    ("bud_flzd_ltbank_2025", "2025", "1619373978", "2025 LT bank 1619373978 vs 1458184093; tick1389; primary official NBB WVV 173"),
    ("bud_flzd_ltlease_2025", "2025", "9397765", "2025 LT lease 9397765 vs 12447206; tick1389; primary official NBB WVV 172"),
    ("bud_flzd_ltother_2025", "2025", "50460022", "2025 LT overige leningen 50460022 JUMP vs 11641453; tick1389; primary official NBB WVV 174"),
    ("bud_flzd_st_2025", "2025", "242283533", "2025 ST schulden 242283533 vs 151370369; tick1389; primary official NBB WVV 42/48"),
    ("bud_flzd_st_due_2025", "2025", "138580537", "2025 LT-due binnen jaar 138580537 vs 94601356; tick1389; primary official NBB WVV 42"),
    ("bud_flzd_sttrade_2025", "2025", "50882110", "2025 leveranciers 50882110 JUMP vs 17639237; tick1389; primary official NBB WVV 440/4"),
    ("bud_flzd_stadv_2025", "2025", "14626631", "2025 vooruitbetalingen 14626631 vs 14157233; tick1389; primary official NBB WVV 46"),
    ("bud_flzd_sttax_2025", "2025", "8506591", "2025 belastingschulden 8506591 vs 7436095; tick1389; primary official NBB WVV 450/3"),
    ("bud_flzd_stother_2025", "2025", "29687664", "2025 overige ST schulden 29687664 vs 17536448; tick1389; primary official NBB WVV 47/48"),
    ("bud_flzd_accrued_2025", "2025", "44141108", "2025 overlopend passief 44141108 vs 37467772; tick1389; primary official NBB WVV 492/3"),
    ("bud_flzd_reldebt_2025", "2025", "1444425810", "2025 related-party schulden 1444425810 (LT 1306192018 / ST 138233792); tick1389; primary official NBB WVV 6.15 9352"),
    ("bud_flzd_relrecv_2025", "2025", "9931752", "2025 related-party vorderingen 9931752 vs 379848; tick1389; primary official NBB WVV 6.15 9292"),
    ("bud_flzd_opsinc_2025", "2025", "424479306", "2025 bedrijfsopbrengsten 424479306 vs 451884789; tick1389; primary official NBB WVV 70/76A"),
    ("bud_flzd_omzet_2025", "2025", "354226189", "2025 omzet 354226189 vs 369051837; tick1389; primary official NBB WVV 70"),
    ("bud_flzd_omzet_2024", "2024", "369051837", "2024 omzet 369051837 comparative; tick1389; primary official NBB WVV 70"),
    ("bud_flzd_omzet_elec_2025", "2025", "285235467", "2025 omzet elek 285235467 vs 268655665; tick1389; primary official NBB WVV 6.10"),
    ("bud_flzd_omzet_gas_2025", "2025", "65489646", "2025 omzet gas 65489646 vs 96634498; tick1389; primary official NBB WVV 6.10"),
    ("bud_flzd_omzet_other_2025", "2025", "3501076", "2025 omzet overige 3501076 vs 3761675; tick1389; primary official NBB WVV 6.10"),
    ("bud_flzd_othops_2025", "2025", "69706519", "2025 andere bedrijfsopbrengsten 69706519 vs 82101678; 740 empty; tick1389; primary official NBB WVV 74"),
    ("bud_flzd_opscost_2025", "2025", "359772130", "2025 bedrijfskosten 359772130 vs 411649863; tick1389; primary official NBB WVV 60/66A"),
    ("bud_flzd_goods_2025", "2025", "145806339", "2025 handelsgoederen 145806339 vs 147264921; tick1389; primary official NBB WVV 60"),
    ("bud_flzd_diensten_2025", "2025", "124676940", "2025 diensten 124676940 vs 156561080; tick1389; primary official NBB WVV 61"),
    ("bud_flzd_diensten_2024", "2024", "156561080", "2024 diensten 156561080 comparative; tick1389; primary official NBB WVV 61"),
    ("bud_flzd_deprec_2025", "2025", "71797716", "2025 afschrijvingen 71797716 vs 86542385; tick1389; primary official NBB WVV 630"),
    ("bud_flzd_othcost_2025", "2025", "15548934", "2025 andere bedrijfskosten 15548934 vs 21872781; tick1389; primary official NBB WVV 640/8"),
    ("bud_flzd_nr_opscost_2025", "2025", "1819084", "2025 niet-recurrente bedrijfskosten 1819084; tick1389; primary official NBB WVV 66A"),
    ("bud_flzd_expl_2025", "2025", "64707176", "2025 expl +64707176 vs +40234927; tick1389; primary official NBB WVV 9901"),
    ("bud_flzd_expl_2024", "2024", "40234927", "2024 expl +40234927 comparative; tick1389; primary official NBB WVV 9901"),
    ("bud_flzd_fininc_2025", "2025", "25701730", "2025 financiele opbrengsten 25701730 vs 11732174; tick1389; primary official NBB WVV 75/76B"),
    ("bud_flzd_fincost_2025", "2025", "48981931", "2025 financiele kosten 48981931 vs 39323392; tick1389; primary official NBB WVV 65/66B"),
    ("bud_flzd_tax_2025", "2025", "9705291", "2025 belastingen 9705291; tick1389; primary official NBB WVV 67/77"),
    ("bud_flzd_pnl_2025", "2025", "31728232", "2025 PnL +31728232 vs +10791915; tick1389; primary official NBB WVV 9904"),
    ("bud_flzd_pnl_2024", "2024", "10791915", "2024 PnL +10791915 comparative; tick1389; primary official NBB WVV 9904"),
    ("bud_flzd_alloc_2025", "2025", "62533575", "2025 te bestemmen 62533575; tick1389; primary official NBB WVV 9906"),
    ("bud_flzd_div_2025", "2025", "20014296", "2025 dividend 20014296 vs 21915024; tick1389; primary official NBB WVV 694"),
    ("bud_flzd_div_2024", "2024", "21915024", "2024 dividend 21915024 comparative; tick1389; primary official NBB WVV 694"),
    ("bud_flzd_capex_2025", "2025", "184060000", "2025 bruto capex jaarverslag 184060000 (kerncijfers); WVV aanschaf 628449886 merger-inflated; tick1389"),
    ("bud_flzd_capex_wvv_2025", "2025", "628449886", "2025 WVV bruto aanschaf IVA+MVA 628449886 (8021+8161-8166; merger/transfer inflated); tick1389; primary official NBB WVV 6.2/6.3"),
    ("bud_flzd_comm_2025", "2025", "17532", "2025 commissaris 9505 17532; tick1389; primary official NBB WVV 9505"),
    ("bud_flzd_comm_extra_2025", "2025", "43993", "2025 commissaris extra controle 95061 43993 + tax 9682; tick1389; primary official NBB WVV 95061"),
    ("bud_flzd_board_2025", "2025", "29108", "2025 bestuurders 9503 29108; tick1389; primary official NBB WVV 9503"),
]


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "Fluvius Zenne-Dijle (voorheen Iverlek + fusie PBE) jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00206993; AV 18.06.2026)",
                "url": SRC_URL,
                "publisher": "Fluvius Zenne-Dijle / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1389; official NBB VOL-inb PDF 1.67MB 90p deposit 2026-00206993 header 23.06.2026 created 27.06.2026; "
                    "leftover IGS energy DSO of 44 Vlaams-Brabant/Mechelen-area municipalities after Iverlek+PBE 01.01.2025; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; Staatsbladmonitor table euros not used (rounded scrape); "
                    "commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / "
                    "Paul Eelen + Line Vyvey oordeel zonder voorbehoud + benadrukking 6.19 regulatoire saldi signed 20.03.2026; "
                    "VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62 empty"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Fluvius Zenne-Dijle official governance + jaarverslag 2025 (leftover IGS energy DSO; voorheen Iverlek + PBE; 44 vennoten)",
                "url": SRC2_URL,
                "publisher": "Fluvius / Fluvius Zenne-Dijle",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1389; leftover IGS of 44 Vlaams-Brabant/Mechelen-area municipalities; "
                    "over.fluvius.be lists activiteitenverslagen + JR2025 https://over.fluvius.be/sites/fluvius/files/2026-06/fluvius-zenne-dijle-jaarverslag-2025.pdf; "
                    "statutory 2025 balans is the NBB CDN deposit; fusie Iverlek+PBE 01.01.2025; 25 gemeenten afgesplitst naar Halle-Vilvoorde"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Fluvius Zenne-Dijle 0222.343.301",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1389; KBO 0222.343.301 Actief / normale toestand since 29.03.1982; "
                    "statutaire naam FLUVIUS ZENNE-DIJLE since 01.01.2025; "
                    "Opdrachthoudende vereniging (Vlaams Gewest) since 05.11.2003; "
                    "zetel Diestsesteenweg 126 3210 Lubbeek since 01.01.2025; 0 VE; "
                    "no KBO email/web/tel; btw since 01.05.1982; jaarvergadering mei; "
                    "boekjaar 31 december; NACE 35.140/35.220/35.110/42.220/43.211/71.111; "
                    "absorbed 0257.942.992 FINILEK (01.04.2018) + 0203.563.111 PBE (01.01.2025)"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Fluvius Zenne-Dijle FOI channel / official governance + secretariaat (KBO no email)",
                "url": SRC4_URL,
                "publisher": "Fluvius Zenne-Dijle",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1389; KBO no email/web/tel; zetel Diestsesteenweg 126 3210 Lubbeek; "
                    "secretariaat Brusselsesteenweg 199 9090 Merelbeke-Melle; "
                    "no dedicated openbaarheid mailbox found on official pages this tick"
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
                "name_nl": "Fluvius Zenne-Dijle (voorheen Iverlek + fusie PBE; leftover IGS energy DSO Vlaams-Brabant)",
                "name_fr": "Fluvius Zenne-Dijle (ex-Iverlek + fusion PBE; IGS residuel DSO energie Brabant flamand)",
                "name_en": "Fluvius Zenne-Dijle leftover IGS energy DSO (formerly Iverlek + PBE merger)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1389 leftover residual IGS energy DSO of 44 Vlaams-Brabant/Mechelen-area municipalities; "
                    "KBO 0222.343.301 Actief since 29.03.1982; naam FLUVIUS ZENNE-DIJLE since 01.01.2025; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 2521878483 omzet 354226189 diensten 124676940 debt 1965656407 pnl 31728232 equity 554585848 dividend 20014296; "
                    "FOI ready omzet geo empty / 69.7m 74 empty 740 / 124.7m 61 / 1.97bn debt / 20.01m dividend; "
                    "distinct from already-mined Fluvius EG group entity fluvius and Limburg 1388 / Halle-Vilvoorde 1387 / Antwerpen 1386 / West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382"
                ),
            },
        ],
    )
    print("entities", n)

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

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": "Fluvius Zenne-Dijle JR2025 leftover IGS dual (assets 2.52bn / omzet 354.23m / diensten 124.68m / debt 1.97bn / dividend 20.01m)",
                "entity_id": ENT,
                "beneficiary": "Fluvius Zenne-Dijle / " + VENNOTEN,
                "legal_basis": "WVV OV; Decreet Lokaal Bestuur; Energiedecreet; NBB neerlegging",
                "decision_date": "2026-06-18",
                "start_year": "1982",
                "end_year": "",
                "total_envelope_eur": "2521878483",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL energy DSO — 354.23m omzet (geo empty) / 124.68m diensten / 1.97bn debt / 20.01m dividend",
                "cut_option": "Publish unpublished omzet geo + 69.7m 74 + 124.7m 61 FSO pass-through + 1.97bn debt counterparties + 20.01m dividend per vennoot + 578.1m LT vorderingen; do not keep DSO IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1389; assets 2521878483 omzet 354226189 diensten 124676940 debt 1965656407 pnl 31728232 equity 554585848 dividend 20014296; FOI ready not sent; not TE-additive of 348bn; double_count vs Fluvius EG possible",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Fluvius Zenne-Dijle JR2025 leftover IGS: assets 2.52bn / omzet 354.23m / diensten 124.68m / debt 1.97bn / dividend 20.01m / 0 VTE",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "124676940",
                "total_cost_eur": "2521878483",
                "tco_notes": (
                    "Leftover dual IGS energy DSO of 44 Vlaams-Brabant/Mechelen-area municipalities (voorheen Iverlek + PBE): "
                    "assets 2.52bn / equity 554.59m / pnl +31.73m / omzet 354.23m (geo empty) / "
                    "diensten 124.68m / 0 VTE / debt 1.97bn (related 1.44bn) / dividend 20.01m / cash 1239; "
                    "official NBB WVV live; do not treat 2.52bn as TE-additive of 348bn; double_count vs Fluvius EG possible"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Fluvius Zenne-Dijle / " + VENNOTEN,
                "stated_goal": "Local leftover IGS map VL energy DSO — JR2025 live; dual omzet-geo/diensten/debt/dividend FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 2.52bn / omzet 354.23m / diensten 124.68m / debt 1.97bn / dividend 20.01m / pnl +31.73m / 0 VTE",
                "absurdity_score": "7.2",
                "cost_score": "8.4",
                "difficulty": "3.0",
                "priority_index": "7.3",
                "cut_proposal": "Publish unpublished omzet geo + 69.7m 74 + 124.7m 61 FSO pass-through + 1.97bn debt counterparties + 20.01m dividend per vennoot + 578.1m LT vorderingen; do not keep DSO IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1389; leftover IGS of 44 Vlaams-Brabant/Mechelen-area municipalities; FOI ready not sent; not TE-additive of 348bn; distinct from Fluvius EG and Limburg 1388 / Halle-Vilvoorde 1387 / Antwerpen 1386 / West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382",
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
                    "omzet 354226189 vs 369051837 (WVV 70; 6.10 category elek 285235467 / gas 65489646 / other 3501076; geo empty) per vennoot/tariefstroom unpublished "
                    "+ andere bedrijfsopbrengsten 69706519 (WVV 74; 740 empty) "
                    "+ diensten 124676940 vs 156561080 (WVV 61; no split) + goods 145806339 + FSO pass-through (pers 62/9087 empty / 0 VTE) "
                    "+ schulden 1965656407 (LT bank 1619373978; related-party 1444425810) counterparties/rente unpublished "
                    "+ LT vorderingen 578103637 JUMP vs 17395268 unpublished "
                    "+ FVA deelnemingen 39298047 unpublished "
                    "+ dividend 20014296 vs 21915024 per vennoot unpublished "
                    "+ cash 1239 vs debt 1.97bn + prepaid 70977254 (regulatoire gas 18717862) + VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.18/9 not filed"
                ),
                "why_it_matters": (
                    "Leftover IGS OV energy DSO of 44 mined Vlaams-Brabant/Mechelen-area municipalities "
                    "(same leftover-IGS energy seam as Fluvius Limburg 1388 / Halle-Vilvoorde 1387 / Antwerpen 1386 / West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382; distinct from Fluvius EG): "
                    "2.52bn assets / 354.23m omzet / 124.68m diensten / 1.97bn debt / 20.01m dividend / "
                    "0 VTE / FSO shell "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Fluvius Zenne-Dijle / Raad van Bestuur / Dirk Vansina / Mohamed Ridouani / 44 vennoten",
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
                    "tick1389 leftover IGS OV energy DSO of 44 Vlaams-Brabant/Mechelen-area municipalities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (1.67MB 90p deposit 2026-00206993). "
                    "Fluvius Limburg already mined 1388 — skipped. Fluvius Halle-Vilvoorde already mined 1387 — skipped. "
                    "Fluvius Antwerpen already mined 1386 — skipped. Fluvius West already mined 1385 — skipped. "
                    "Fluvius Kempen already mined 1384 — skipped. Imewo already mined 1383 — skipped. INTERGEM already mined 1382 — skipped. "
                    "Other Fluvius DNB holdings (Riobra) leftover next. "
                    "Dommelhof leftover Limburg EVA 0777.495.085 not re-probed once live Zenne-Dijle extracted. "
                    "Otary RS Nuhma-adjacent fallback not taken. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1389",
        "title": "Fluvius Zenne-Dijle / Iverlek+PBE JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Fluvius Zenne-Dijle leftover IGS energy DSO of 44 Vlaams-Brabant/Mechelen-area municipalities after honest hunt; "
            "KBO 0222.343.301 Actief; live JR2025 official NBB WVV VOL-inb PDF (1.67MB 90p deposit 2026-00206993; commissaris EY); "
            "sourced euros assets 2521878483 / omzet 354226189 / diensten 124676940 / debt 1965656407 / pnl 31728232 / dividend 20014296; "
            "FOI ready omzet geo empty / 69.7m 74 / 124.7m 61 / 1.97bn debt / 20.01m dividend"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T05:15:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1389 Fluvius Zenne-Dijle leftover IGS energy residual; KBO 0222.343.301; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1390 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1390",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1389 done including Fluvius Zenne-Dijle 1389 leftover energy IGS live NBB WVV / "
            "Fluvius Limburg 1388 leftover energy IGS live NBB WVV / "
            "Fluvius Halle-Vilvoorde 1387 leftover energy IGS live NBB WVV / "
            "Fluvius Antwerpen 1386 leftover energy IGS live NBB WVV / "
            "Fluvius West 1385 leftover energy IGS live NBB WVV / "
            "Fluvius Kempen 1384 leftover energy IGS live NBB WVV / "
            "Fluvius Imewo 1383 leftover energy IGS live NBB WVV / "
            "INTERGEM / Fluvius Midden-Vlaanderen 1382 leftover energy IGS live NBB WVV); "
            "other Fluvius DNB holdings leftover energy IGS (Riobra / Fluvius Riobra from 01.01.2026) — take if a 2025 CDN/JR PDF still live and unmined; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
            "skip already-mined Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1389 after Fluvius Zenne-Dijle leftover energy IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1389", rq_new, rq_spawn)
    print("research_queue 1389", found, "spawned_1390", spawned)

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
                "last_unit_id": "rq_1389",
                "ticks_completed": "1389",
                "paused": "no",
                "notes": (
                    "tick1389 Fluvius Zenne-Dijle leftover IGS energy residual; KBO 0222.343.301; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 2521878483 omzet 354226189 diensten 124676940 debt 1965656407 pnl 31728232 equity 554585848 dividend 20014296; "
                    "FOI ready omzet geo empty/69.7m 74/124.7m 61/1.97bn debt/20.01m div; next rq_1390 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    entry = (
        "### Tick 1389 - 2026-08-19 - rq_1389 Fluvius Zenne-Dijle / Iverlek+PBE dual residual leftover\\n"
        "- Unit: Fluvius Zenne-Dijle (voorheen Iverlek + fusie PBE 01.01.2025; leftover IGS opdrachthoudende vereniging / energy DSO elektriciteit + aardgas + leftover kabel/neven + openbare verlichting + warmte of 44 mined Vlaams-Brabant / Mechelen-area municipalities; werkmaatschappij Fluvius System Operator) after residual dual hunt (KBO **0222.343.301**; official over.fluvius.be has activiteitenverslagen/governance + jaarverslag 2025; live NBB WVV VOL-inb deposit **2026-00206993** PDF 1.67MB / 90p; AV **18.06.2026**; header **23.06.2026**; created **27.06.2026**; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / Paul Eelen A02213 + Line Vyvey A02501 signed 20.03.2026 oordeel zonder voorbehoud assets 2.521.878.483 / PnL +31.728.232 + benadrukking VOL-inb 6.19 regulatoire saldi). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; preferred leftover Fluvius DNB holding this tick). Distinct from already-mined Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / Fluvius EG group-level (entity fluvius). First confirmed not already mined: no Fluvius Zenne-Dijle / Iverlek / 0222.343.301 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **29.03.1982**; statutaire naam FLUVIUS ZENNE-DIJLE since 01.01.2025; Opdrachthoudende vereniging (Vlaams Gewest) since 05.11.2003; zetel Diestsesteenweg 126 3210 Lubbeek since 01.01.2025; **0 VE**; KBO no email/web/tel; official site https://over.fluvius.be/; btw since 01.05.1982; jaarvergadering mei; boekjaar 31 december; NACE 35.140/35.220. Absorbed FINILEK 0257.942.992 (01.04.2018) and PBE 0203.563.111 (01.01.2025). Voorzitter Dirk Vansina since 01.01.2025; ondervoorzitter Mohamed Ridouani since 24.03.2025; commissaris EY 26.06.2024-26.06.2027 (benoemd 19.06.2025). Hunt leftover Fluvius DNB first: Zenne-Dijle statutory CDN live this tick (HTTP 200 / 1669481 / 90p) — taken. Fluvius Limburg already mined 1388 — skipped. Fluvius Halle-Vilvoorde already mined 1387 — skipped. Fluvius Antwerpen already mined 1386 — skipped. Fluvius West already mined 1385 — skipped. Fluvius Kempen already mined 1384 — skipped. Imewo already mined 1383 — skipped. INTERGEM already mined 1382 — skipped. Fluvius Riobra leftover next. Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live Zenne-Dijle extracted. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used (rounded scrape). Not every-10 (next 1390).\\n"
        "- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud + benadrukking 6.19; VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62/9087 empty): assets **2.521.878.483** (was 2.310.551.331; 2024 comparative is ex-Iverlek); fixed **1.696.031.777** / MVA **1.590.822.866** (gebouwen **36.396.750**; machines **1.398.735.216**; meubilair **8.570.911**; leasing **9.610.720**; overige **558.797**; CIP **136.950.472** aanschaf **188.063.051**); IVA 13.232.548; FVA **91.976.363** (deelnemingen **39.298.047** FSO 7,09% K-SYN / 10,75% A / Transco 11,11%; andere aandelen **52.678.316**); current **825.846.706 JUMP** vs 245.590.764 (LT recv **578.103.637 JUMP** vs 17.395.268); cash **1.239**; prepaid **70.977.254** (regulatoire VNR-gas 18.717.862 / REG 11.154.861); equity **554.585.848**; voorzieningen **1.636.228**; schulden **1.965.656.407** (LT **1.679.231.766** waarvan bank **1.619.373.978**; ST **242.283.533** waarvan leveranciers **50.882.110 JUMP**; related-party FSO-seam **1.444.425.810**); omzet **354.226.189** vs 369.051.837 (elek **285.235.467** / gas **65.489.646** / other **3.501.076**; geo empty); othops **69.706.519** (740 empty); goods **145.806.339**; diensten **124.676.940** vs 156.561.080; pers **empty / 0 VTE**; afschr 71.797.716; expl **+64.707.176** vs +40.234.927; fin opbr 25.701.730; fin kosten 48.981.931; tax 9.705.291; PnL **+31.728.232** vs +10.791.915; dividend **20.014.296** vs 21.915.024; bruto capex jaarverslag **184.060.000**; WVV aanschaf 628.449.886 merger-inflated; commissaris 17.532 + extra 43.993; bestuurders 29.108. Jaarverslag same deposit: 44 vennoten; WACC/kapitaalkost 5,2% vs 3,5%; nettarief gezin elek **495** vs 353 Iverlek / 420 PBE / gas **269** vs 241; 25 gemeenten afgesplitst naar Fluvius Halle-Vilvoorde 01.01.2025; Kampenhout kabel from Fluvius West 01.01.2026.\\n"
        "- CSVs: sources+4/entities+1/budgets+79/commitments+1/leaderboard+1 + FOI ready `gap_flzd_omzet_354_23m_diensten_124_68m_debt_1_97bn_l5` (not sent); rq_1389=done; spawn rq_1390; ticks=1389.\\n"
        "- Coverage: residual dual L5 (Fluvius Zenne-Dijle leftover energy IGS live WVV). Does **not** move L5 near-complete of EUR 347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs Fluvius EG possible. No progress refresh (not every-10; next 1390).\\n"
        "- Next: rq_1390 residual dual L5 VL JR2025 hole_fill (prefer leftover Fluvius Riobra if a 2025 CDN/JR PDF still live and unmined; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS only after leftover IGS/EVA/AGB; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382).\\n"
    )
    entry = entry.replace(chr(92) + "n", chr(10))
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1389 write done")


if __name__ == "__main__":
    main()

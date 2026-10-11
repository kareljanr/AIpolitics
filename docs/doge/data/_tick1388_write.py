# -*- coding: utf-8 -*-
"""Tick 1388 — leftover Fluvius Limburg JR2025 official NBB WVV euros.
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

TICK = "1388"
UTC = "2026-08-19T05:15:00Z"
ENT = "igs_flli"
HIER = "Vlaanderen>Limburg>IGS>FluviusLimburg"
GAP = "gap_flli_omzet_434_32m_diensten_163_67m_debt_1_55bn_l5"
SRC = "src_flli_jr2025_nbb"
SRC2 = "src_flli_site"
SRC3 = "src_kbo_flli_0207165769"
SRC4 = "src_flli_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00218151.pdf"
SRC2_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-limburg/activiteitenverslagen"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0207165769"
SRC4_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-limburg"
FOI_EMAIL = ""
FOI_POSTAL = "Trichterheideweg 8 3500 Hasselt"
DRAFT = "docs/doge/foi/drafts/gap_flli_omzet_434_32m_diensten_163_67m_debt_1_55bn_l5.md"
COMM = "comm_flli_jr2025_pnl"
LB = "lb_flli_omzet_434_32m_diensten_163_67m_debt_1_55bn"

VENNOTEN = (
    "Alken + As + Beringen + Bilzen-Hoeselt + Bocholt + Bree + "
    "Diepenbeek + Dilsen-Stokkem + Genk + Gingelom + Halen + "
    "Hamont-Achel + Hasselt + Hechtel-Eksel + Heers + Herk-de-Stad + "
    "Herstappe + Heusden-Zolder + Houthalen-Helchteren + Kinrooi + "
    "Kortessem + Laakdal + Lanaken + Leopoldsburg + Lommel + Lummen + "
    "Maaseik + Maasmechelen + Nieuwerkerken + Oudsbergen + Peer + "
    "Pelt + Riemst + Sint-Truiden + Tessenderlo-Ham + Tongeren-Borgloon + "
    "Voeren + Wellen + Zonhoven + Zutendaal"
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
    ("bud_flli_assets_2025", "2025", "3255341179", "2025 assets 3255341179 VOL-inb 20/58; tick1388; primary official NBB WVV"),
    ("bud_flli_assets_2024", "2024", "2997199476", "2024 assets 2997199476 comparative; tick1388; primary official NBB WVV 20/58"),
    ("bud_flli_fixed_2025", "2025", "2872298964", "2025 vaste activa 2872298964 vs 2728024649; tick1388; primary official NBB WVV 21/28"),
    ("bud_flli_iva_2025", "2025", "18971349", "2025 IVA 18971349 vs 18591969; tick1388; primary official NBB WVV 21"),
    ("bud_flli_iva_acq_2025", "2025", "7593586", "2025 IVA aanschaf 7593586 (8021); tick1388; primary official NBB WVV 6.2.1"),
    ("bud_flli_mva_2025", "2025", "2668421302", "2025 MVA 2668421302 vs 2524521498; tick1388; primary official NBB WVV 22/27"),
    ("bud_flli_buildings_2025", "2025", "28934712", "2025 terreinen/gebouwen 28934712 vs 27353788; tick1388; primary official NBB WVV 22"),
    ("bud_flli_buildings_acq_2025", "2025", "2514424", "2025 gebouwen aanschaf 2514424 (8161); tick1388; primary official NBB WVV 6.3.1"),
    ("bud_flli_machines_2025", "2025", "2255932045", "2025 machines 2255932045 vs 2118782887; tick1388; primary official NBB WVV 23"),
    ("bud_flli_machines_acq_2025", "2025", "33747582", "2025 machines aanschaf 33747582 (8162); tick1388; primary official NBB WVV 6.3.2"),
    ("bud_flli_furniture_2025", "2025", "10723138", "2025 meubilair 10723138 vs 9120790; tick1388; primary official NBB WVV 24"),
    ("bud_flli_lease_mva_2025", "2025", "4095684", "2025 leasing MVA 4095684 vs 4068511; tick1388; primary official NBB WVV 25"),
    ("bud_flli_other_mva_2025", "2025", "1198766", "2025 overige MVA 1198766 vs 212741; tick1388; primary official NBB WVV 26"),
    ("bud_flli_cip_2025", "2025", "367536958", "2025 CIP 367536958 vs 364982781; tick1388; primary official NBB WVV 27"),
    ("bud_flli_cip_acq_2025", "2025", "286934860", "2025 CIP aanschaf 286934860 (8166); tick1388; primary official NBB WVV 6.3.6"),
    ("bud_flli_fva_2025", "2025", "184906313", "2025 FVA 184906313 vs 184911182; tick1388; primary official NBB WVV 28"),
    ("bud_flli_fva_part_2025", "2025", "184901850", "2025 FVA deelnemingen 184901850 FSO 16.35pct / 41.38pct K-SYN; tick1388; primary official NBB WVV 282"),
    ("bud_flli_fva_shares_2025", "2025", "4462", "2025 andere FVA aandelen 4462; tick1388; primary official NBB WVV 284"),
    ("bud_flli_current_2025", "2025", "383042215", "2025 vlottend 383042215 vs 269174827; tick1388; primary official NBB WVV 29/58"),
    ("bud_flli_ltrecv_2025", "2025", "91655339", "2025 LT vorderingen 91655339 vs 56265787; tick1388; primary official NBB WVV 29"),
    ("bud_flli_wip_2025", "2025", "30667364", "2025 bestellingen in uitvoering 30667364 vs 30131154; tick1388; primary official NBB WVV 37"),
    ("bud_flli_strecv_2025", "2025", "195728512", "2025 ST vorderingen 195728512 vs 128423859; tick1388; primary official NBB WVV 40/41"),
    ("bud_flli_trade_2025", "2025", "85495964", "2025 handelsvorderingen 85495964 vs 53798055; tick1388; primary official NBB WVV 40"),
    ("bud_flli_othrecv_2025", "2025", "110232548", "2025 overige ST vorderingen 110232548 vs 74625804; tick1388; primary official NBB WVV 41"),
    ("bud_flli_cash_2025", "2025", "905", "2025 liquide middelen 905 vs 1865; tick1388; primary official NBB WVV 54/58"),
    ("bud_flli_prepaid_2025", "2025", "64990095", "2025 overlopend actief 64990095 vs 54352162; tick1388; primary official NBB WVV 490/1"),
    ("bud_flli_prepaid_reg_2025", "2025", "12189209", "2025 prepaid regulatoire elek+gas 12189209; tick1388; primary official NBB WVV 6.6"),
    ("bud_flli_equity_2025", "2025", "1658770893", "2025 EV 1658770893 vs 1673729341; tick1388; primary official NBB WVV 10/15"),
    ("bud_flli_equity_2024", "2024", "1673729341", "2024 EV 1673729341 comparative; tick1388; primary official NBB WVV 10/15"),
    ("bud_flli_inbreng_2025", "2025", "713688993", "2025 inbreng 713688993 vs 719507426; tick1388; primary official NBB WVV 10/11"),
    ("bud_flli_reval_2025", "2025", "258043057", "2025 herwaarderingsmeerwaarden 258043057 vs 274791218; tick1388; primary official NBB WVV 12"),
    ("bud_flli_reserves_2025", "2025", "369190363", "2025 reserves 369190363 vs 406895469; tick1388; primary official NBB WVV 13"),
    ("bud_flli_retained_2025", "2025", "67737233", "2025 overgedragen 67737233 vs 44359742; tick1388; primary official NBB WVV 14"),
    ("bud_flli_capsub_2025", "2025", "250111247", "2025 kapitaalsubsidies 250111247 vs 228175485; tick1388; primary official NBB WVV 15"),
    ("bud_flli_prov_2025", "2025", "50981558", "2025 voorzieningen+uitgesteld 50981558 vs 42605336; tick1388; primary official NBB WVV 16"),
    ("bud_flli_debt_2025", "2025", "1545588729", "2025 schulden 1545588729 vs 1280864799; tick1388; primary official NBB WVV 17/49"),
    ("bud_flli_debt_2024", "2024", "1280864799", "2024 schulden 1280864799 comparative; tick1388; primary official NBB WVV 17/49"),
    ("bud_flli_lt_2025", "2025", "1324182291", "2025 LT schulden 1324182291 vs 1150309979; tick1388; primary official NBB WVV 17"),
    ("bud_flli_ltbank_2025", "2025", "1301995163", "2025 LT bank 1301995163 vs 1135364415; tick1388; primary official NBB WVV 173"),
    ("bud_flli_ltlease_2025", "2025", "4000596", "2025 LT lease 4000596 vs 4215564; tick1388; primary official NBB WVV 172"),
    ("bud_flli_ltother_2025", "2025", "18186532", "2025 LT overige leningen 18186532 vs 10730000; tick1388; primary official NBB WVV 174"),
    ("bud_flli_st_2025", "2025", "186410935", "2025 ST schulden 186410935 vs 112074605; tick1388; primary official NBB WVV 42/48"),
    ("bud_flli_st_due_2025", "2025", "28003370", "2025 LT-due binnen jaar 28003370 vs 20786925; tick1388; primary official NBB WVV 42"),
    ("bud_flli_sttrade_2025", "2025", "81490417", "2025 leveranciers 81490417 JUMP vs 17974451; tick1388; primary official NBB WVV 440/4"),
    ("bud_flli_stadv_2025", "2025", "37244477", "2025 vooruitbetalingen 37244477 vs 31295744; tick1388; primary official NBB WVV 46"),
    ("bud_flli_sttax_2025", "2025", "10667111", "2025 belastingschulden 10667111 vs 9978184; tick1388; primary official NBB WVV 450/3"),
    ("bud_flli_stother_2025", "2025", "29005560", "2025 overige ST schulden 29005560 vs 32039302; tick1388; primary official NBB WVV 47/48"),
    ("bud_flli_accrued_2025", "2025", "34995502", "2025 overlopend passief 34995502 vs 18480215; tick1388; primary official NBB WVV 492/3"),
    ("bud_flli_reldebt_2025", "2025", "1158223306", "2025 related-party schulden 1158223306 (LT 1099782707 / ST 58440599); tick1388; primary official NBB WVV 6.15 9352"),
    ("bud_flli_relrecv_2025", "2025", "78904120", "2025 related-party ST vorderingen 78904120 vs 28836340; tick1388; primary official NBB WVV 6.15 9292"),
    ("bud_flli_opsinc_2025", "2025", "503115377", "2025 bedrijfsopbrengsten 503115377 vs 444491611; tick1388; primary official NBB WVV 70/76A"),
    ("bud_flli_omzet_2025", "2025", "434321317", "2025 omzet 434321317 JUMP vs 351808989; tick1388; primary official NBB WVV 70"),
    ("bud_flli_omzet_2024", "2024", "351808989", "2024 omzet 351808989 comparative; tick1388; primary official NBB WVV 70"),
    ("bud_flli_omzet_elec_2025", "2025", "301900661", "2025 omzet elek 301900661 vs 222275707; tick1388; primary official NBB WVV 6.10"),
    ("bud_flli_omzet_gas_2025", "2025", "63657909", "2025 omzet gas 63657909 vs 73627764; tick1388; primary official NBB WVV 6.10"),
    ("bud_flli_omzet_cable_2025", "2025", "5482751", "2025 omzet kabel 5482751 vs 241273; tick1388; primary official NBB WVV 6.10"),
    ("bud_flli_omzet_sewer_2025", "2025", "61997817", "2025 omzet riolering 61997817 vs 55029728; tick1388; primary official NBB WVV 6.10"),
    ("bud_flli_omzet_other_2025", "2025", "1282179", "2025 omzet overige 1282179 vs 634516; tick1388; primary official NBB WVV 6.10"),
    ("bud_flli_othops_2025", "2025", "68257849", "2025 andere bedrijfsopbrengsten 68257849 vs 73219865; 740 empty; tick1388; primary official NBB WVV 74"),
    ("bud_flli_opscost_2025", "2025", "467273964", "2025 bedrijfskosten 467273964 vs 437884932; tick1388; primary official NBB WVV 60/66A"),
    ("bud_flli_goods_2025", "2025", "169982709", "2025 handelsgoederen 169982709 vs 129987223; tick1388; primary official NBB WVV 60"),
    ("bud_flli_diensten_2025", "2025", "163666440", "2025 diensten 163666440 vs 177958629; tick1388; primary official NBB WVV 61"),
    ("bud_flli_diensten_2024", "2024", "177958629", "2024 diensten 177958629 comparative; tick1388; primary official NBB WVV 61"),
    ("bud_flli_deprec_2025", "2025", "100336808", "2025 afschrijvingen 100336808 vs 95886896; tick1388; primary official NBB WVV 630"),
    ("bud_flli_othcost_2025", "2025", "17644949", "2025 andere bedrijfskosten 17644949 vs 15508700; tick1388; primary official NBB WVV 640/8"),
    ("bud_flli_nr_opscost_2025", "2025", "14543625", "2025 niet-recurrente bedrijfskosten 14543625 vs 15100000; tick1388; primary official NBB WVV 66A"),
    ("bud_flli_expl_2025", "2025", "35841413", "2025 expl +35841413 vs +6606679; tick1388; primary official NBB WVV 9901"),
    ("bud_flli_expl_2024", "2024", "6606679", "2024 expl +6606679 comparative; tick1388; primary official NBB WVV 9901"),
    ("bud_flli_fininc_2025", "2025", "8418018", "2025 financiele opbrengsten 8418018 vs 176937908; tick1388; primary official NBB WVV 75/76B"),
    ("bud_flli_fincost_2025", "2025", "30961708", "2025 financiele kosten 30961708 vs 24666046; tick1388; primary official NBB WVV 65/66B"),
    ("bud_flli_tax_2025", "2025", "1320742", "2025 belastingen 1320742; tick1388; primary official NBB WVV 67/77"),
    ("bud_flli_pnl_2025", "2025", "12635360", "2025 PnL +12635360 vs +159358483; tick1388; primary official NBB WVV 9904"),
    ("bud_flli_pnl_2024", "2024", "159358483", "2024 PnL +159358483 (incl 170255488 FVA meerwaarde); tick1388; primary official NBB WVV 9904"),
    ("bud_flli_alloc_2025", "2025", "55037440", "2025 te bestemmen 55037440; tick1388; primary official NBB WVV 9906"),
    ("bud_flli_div_2025", "2025", "28540639", "2025 dividend 28540639 DROP vs 207761485; tick1388; primary official NBB WVV 694"),
    ("bud_flli_div_2024", "2024", "207761485", "2024 dividend 207761485 after FVA meerwaarde; tick1388; primary official NBB WVV 694"),
    ("bud_flli_capex_2025", "2025", "338207466", "2025 bruto capex IVA+MVA aanschaf 338207466 (8021+8161-8166); tick1388; primary official NBB WVV 6.2/6.3"),
    ("bud_flli_comm_2025", "2025", "42558", "2025 commissaris 9505 42558; tick1388; primary official NBB WVV 9505"),
    ("bud_flli_comm_extra_2025", "2025", "56212", "2025 commissaris extra controle 95061 56212 + tax 12127; tick1388; primary official NBB WVV 95061"),
    ("bud_flli_board_2025", "2025", "29288", "2025 bestuurders 9503 29288; tick1388; primary official NBB WVV 9503"),
]


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "Fluvius Limburg (voorheen Inter-energa) jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00218151; AV 11.06.2026)",
                "url": SRC_URL,
                "publisher": "Fluvius Limburg / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1388; official NBB VOL-inb PDF 2.31MB 98p deposit 2026-00218151 header 23.06.2026; "
                    "leftover IGS energy DSO of 43 Limburg municipalities after Inter-energa+Inter-aqua+Inter-media 01.04.2019; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris EY Bedrijfsrevisoren BV A01753 / 0446.334.711 / "
                    "Paul Eelen + Line Vyvey oordeel zonder voorbehoud + benadrukking 6.19 regulatoire saldi; "
                    "VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62 empty"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Fluvius Limburg official governance + jaarverslag 2025 (leftover IGS energy DSO; voorheen Inter-energa; 43 vennoten)",
                "url": SRC2_URL,
                "publisher": "Fluvius / Fluvius Limburg",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1388; leftover IGS of 43 Limburg municipalities; "
                    "over.fluvius.be lists activiteitenverslagen + JR2025; statutory 2025 balans is the NBB CDN deposit; fusie Inter-energa+Inter-aqua+Inter-media april 2019"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Fluvius Limburg 0207.165.769",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1388; KBO 0207.165.769 Actief / normale toestand since 15.06.1970; "
                    "statutaire naam Fluvius Limburg since 01.04.2019; "
                    "Opdrachthoudende vereniging (Vlaams Gewest) since 21.05.2003; "
                    "zetel Trichterheideweg 8 3500 Hasselt since 01.01.2025; 0 VE; "
                    "no KBO email/web/tel; btw since 01.01.1971; "
                    "boekjaar 31 december; NACE 35.140/35.220; absorbed 0872.183.022 + 0872.183.121 (01.04.2019)"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Fluvius Limburg FOI channel / official governance + secretariaat (KBO no email)",
                "url": SRC4_URL,
                "publisher": "Fluvius Limburg",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1388; KBO no email/web/tel; zetel Trichterheideweg 8 3500 Hasselt; "
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
                "name_nl": "Fluvius Limburg (voorheen Inter-energa; leftover IGS energy DSO Limburg)",
                "name_fr": "Fluvius Limbourg (ex-Inter-energa; IGS residuel DSO energie Limbourg)",
                "name_en": "Fluvius Limburg leftover IGS energy DSO (formerly Inter-energa)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1388 leftover residual IGS energy DSO of 43 Limburg municipalities; "
                    "KBO 0207.165.769 Actief since 15.06.1970; naam Fluvius Limburg since 01.04.2019; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 3255341179 omzet 434321317 diensten 163666440 debt 1545588729 pnl 12635360 equity 1658770893 dividend 28540639; "
                    "FOI ready omzet geo empty / 68.3m 74 empty 740 / 163.7m 61 / 1.55bn debt / 28.54m dividend; "
                    "distinct from already-mined Fluvius EG group entity fluvius and Halle-Vilvoorde 1387 / Antwerpen 1386 / West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382"
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
                "title": "Fluvius Limburg JR2025 leftover IGS dual (assets 3.26bn / omzet 434.32m / diensten 163.67m / debt 1.55bn / dividend 28.54m)",
                "entity_id": ENT,
                "beneficiary": "Fluvius Limburg / " + VENNOTEN,
                "legal_basis": "WVV OV; Decreet Lokaal Bestuur; Energiedecreet; NBB neerlegging",
                "decision_date": "2026-06-11",
                "start_year": "1970",
                "end_year": "",
                "total_envelope_eur": "3255341179",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL energy DSO — 434.32m omzet (geo empty) / 163.67m diensten / 1.55bn debt / 28.54m dividend",
                "cut_option": "Publish unpublished omzet geo + 68.3m 74 + 163.7m 61 FSO pass-through + 1.55bn debt counterparties + 28.54m dividend per vennoot; do not keep DSO IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1388; assets 3255341179 omzet 434321317 diensten 163666440 debt 1545588729 pnl 12635360 equity 1658770893 dividend 28540639; FOI ready not sent; not TE-additive of 348bn; double_count vs Fluvius EG possible",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Fluvius Limburg JR2025 leftover IGS: assets 3.26bn / omzet 434.32m / diensten 163.67m / debt 1.55bn / dividend 28.54m / 0 VTE",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "163666440",
                "total_cost_eur": "3255341179",
                "tco_notes": (
                    "Leftover dual IGS energy DSO of 43 Limburg municipalities (voorheen Inter-energa): "
                    "assets 3.26bn / equity 1.66bn / pnl +12.64m / omzet 434.32m (geo empty) / "
                    "diensten 163.67m / 0 VTE / debt 1.55bn (related 1.16bn) / dividend 28.54m / cash 905; "
                    "official NBB WVV live; do not treat 3.26bn as TE-additive of 348bn; double_count vs Fluvius EG possible"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Fluvius Limburg / " + VENNOTEN,
                "stated_goal": "Local leftover IGS map VL energy DSO — JR2025 live; dual omzet-geo/diensten/debt/dividend FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 3.26bn / omzet 434.32m / diensten 163.67m / debt 1.55bn / dividend 28.54m / pnl +12.64m / 0 VTE",
                "absurdity_score": "7.2",
                "cost_score": "8.6",
                "difficulty": "3.0",
                "priority_index": "7.4",
                "cut_proposal": "Publish unpublished omzet geo + 68.3m 74 + 163.7m 61 FSO pass-through + 1.55bn debt counterparties + 28.54m dividend per vennoot; do not keep DSO IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1388; leftover IGS of 43 Limburg municipalities; FOI ready not sent; not TE-additive of 348bn; distinct from Fluvius EG and Halle-Vilvoorde 1387 / Antwerpen 1386 / West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382",
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
                    "omzet 434321317 JUMP vs 351808989 (WVV 70; 6.10 category elek 301900661 / gas 63657909 / kabel 5482751 / riolering 61997817 / other 1282179; geo empty) per vennoot/tariefstroom unpublished "
                    "+ andere bedrijfsopbrengsten 68257849 (WVV 74; 740 empty) "
                    "+ diensten 163666440 vs 177958629 (WVV 61; no split) + goods 169982709 + FSO pass-through (pers 62/9087 empty / 0 VTE) "
                    "+ schulden 1545588729 (LT bank 1301995163; related-party 1158223306) counterparties/rente unpublished "
                    "+ FVA deelnemingen 184901850 unpublished "
                    "+ dividend 28540639 vs 207761485 per vennoot unpublished "
                    "+ cash 905 vs debt 1.55bn + prepaid 64990095 (regulatoire 12189209) + VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.18/9 not filed"
                ),
                "why_it_matters": (
                    "Leftover IGS OV energy DSO of 43 mined Limburg municipalities "
                    "(same leftover-IGS energy seam as Fluvius Halle-Vilvoorde 1387 / Antwerpen 1386 / West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382; distinct from Fluvius EG): "
                    "3.26bn assets / 434.32m omzet / 163.67m diensten / 1.55bn debt / 28.54m dividend / "
                    "0 VTE / FSO shell "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Fluvius Limburg / Raad van Bestuur / Mark Vos / Jasmine Neven / 43 Limburg vennoten",
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
                    "tick1388 leftover IGS OV energy DSO of 43 Limburg municipalities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (2.31MB 98p deposit 2026-00218151). "
                    "Fluvius Halle-Vilvoorde already mined 1387 — skipped. Fluvius Antwerpen already mined 1386 — skipped. "
                    "Fluvius West already mined 1385 — skipped. Fluvius Kempen already mined 1384 — skipped. "
                    "Imewo already mined 1383 — skipped. INTERGEM already mined 1382 — skipped. "
                    "Other Fluvius DNB holdings (Zenne-Dijle) leftover next. "
                    "Dommelhof leftover Limburg EVA 0777.495.085 not re-probed once live Limburg extracted. "
                    "Otary RS Nuhma-adjacent fallback not taken. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1388",
        "title": "Fluvius Limburg / Inter-energa JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Fluvius Limburg leftover IGS energy DSO of 43 Limburg municipalities after honest hunt; "
            "KBO 0207.165.769 Actief; live JR2025 official NBB WVV VOL-inb PDF (2.31MB 98p deposit 2026-00218151; commissaris EY); "
            "sourced euros assets 3255341179 / omzet 434321317 / diensten 163666440 / debt 1545588729 / pnl 12635360 / dividend 28540639; "
            "FOI ready omzet geo empty / 68.3m 74 / 163.7m 61 / 1.55bn debt / 28.54m dividend"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T04:50:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1388 Fluvius Limburg leftover IGS energy residual; KBO 0207.165.769; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1389 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1389",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1388 done including Fluvius Limburg 1388 leftover energy IGS live NBB WVV / "
            "Fluvius Halle-Vilvoorde 1387 leftover energy IGS live NBB WVV / "
            "Fluvius Antwerpen 1386 leftover energy IGS live NBB WVV / "
            "Fluvius West 1385 leftover energy IGS live NBB WVV / "
            "Fluvius Kempen 1384 leftover energy IGS live NBB WVV / "
            "Fluvius Imewo 1383 leftover energy IGS live NBB WVV / "
            "INTERGEM / Fluvius Midden-Vlaanderen 1382 leftover energy IGS live NBB WVV); "
            "other Fluvius DNB holdings leftover energy IGS (Zenne-Dijle) — take if a 2025 CDN/JR PDF still live and unmined; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
            "skip already-mined Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1388 after Fluvius Limburg leftover energy IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1388", rq_new, rq_spawn)
    print("research_queue 1388", found, "spawned_1389", spawned)

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
                "last_unit_id": "rq_1388",
                "ticks_completed": "1388",
                "paused": "no",
                "notes": (
                    "tick1388 Fluvius Limburg leftover IGS energy residual; KBO 0207.165.769; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 3255341179 omzet 434321317 diensten 163666440 debt 1545588729 pnl 12635360 equity 1658770893 dividend 28540639; "
                    "FOI ready omzet geo empty/68.3m 74/163.7m 61/1.55bn debt/28.54m div; next rq_1389 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    entry = (
        "### Tick 1388 - 2026-08-19 - rq_1388 Fluvius Limburg / Inter-energa dual residual leftover\\n"
        "- Unit: Fluvius Limburg (voorheen Inter-energa + Inter-aqua + Inter-media fusie 01.04.2019; leftover IGS opdrachthoudende vereniging / energy DSO elektriciteit + aardgas + riolering + kabel of 43 mined Limburg municipalities; werkmaatschappij Fluvius System Operator) after residual dual hunt (KBO **0207.165.769**; official over.fluvius.be has activiteitenverslagen/governance + jaarverslag 2025; live NBB WVV VOL-inb deposit **2026-00218151** PDF 2.31MB / 98p; AV **11.06.2026**; header **23.06.2026**; commissaris EY Bedrijfsrevisoren BV A01753 / 0446.334.711 / Paul Eelen A02213 + Line Vyvey A02501 signed Gent 26.03.2026 oordeel zonder voorbehoud + benadrukking VOL-inb 6.19 regulatoire saldi). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; preferred leftover Fluvius DNB holding this tick). Distinct from already-mined Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / Fluvius EG group-level (entity fluvius). First confirmed not already mined: no Fluvius Limburg / Inter-energa / 0207.165.769 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **15.06.1970**; statutaire naam Fluvius Limburg since 01.04.2019; Opdrachthoudende vereniging (Vlaams Gewest) since 21.05.2003; zetel Trichterheideweg 8 3500 Hasselt since 01.01.2025; **0 VE**; KBO no email/web/tel; official site https://over.fluvius.be/; btw since 01.01.1971; boekjaar 31 december; NACE 35.140/35.220. Absorbed INTER-MEDIA 0872.183.022 and INTER-AQUA 0872.183.121 (01.04.2019). Voorzitter Mark Vos since 11.03.2025; ondervoorzitter Jasmine Neven; commissaris EY since 16.06.2025 tot 16.06.2028. Hunt leftover Fluvius DNB first: Limburg statutory CDN live this tick (HTTP 200 / 2313339 / 98p) — taken. Fluvius Halle-Vilvoorde already mined 1387 — skipped. Fluvius Antwerpen already mined 1386 — skipped. Fluvius West already mined 1385 — skipped. Fluvius Kempen already mined 1384 — skipped. Imewo already mined 1383 — skipped. INTERGEM already mined 1382 — skipped. Zenne-Dijle leftover next. Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live Limburg extracted. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Not every-10 (next 1390).\\n"
        "- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud + benadrukking 6.19; VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62/9087 empty): assets **3.255.341.179** (was 2.997.199.476); fixed **2.872.298.964** / MVA **2.668.421.302** (gebouwen **28.934.712**; machines **2.255.932.045**; meubilair **10.723.138**; leasing **4.095.684**; overige **1.198.766**; CIP **367.536.958** aanschaf **286.934.860**); IVA 18.971.349; FVA **184.906.313** (deelnemingen **184.901.850** FSO 16,35% / 41,38% K-SYN); current **383.042.215**; cash **905**; prepaid **64.990.095** (GSC 34.069.700 / regulatoire 12.189.209); equity **1.658.770.893**; voorzieningen **50.981.558**; schulden **1.545.588.729** (LT **1.324.182.291** waarvan bank **1.301.995.163**; ST **186.410.935** waarvan leveranciers **81.490.417 JUMP**; related-party FSO-seam **1.158.223.306**); omzet **434.321.317 JUMP** vs 351.808.989 (elek **301.900.661** / gas **63.657.909** / riolering **61.997.817** / kabel **5.482.751** / other **1.282.179**; geo empty); othops **68.257.849** (740 empty); goods **169.982.709**; diensten **163.666.440** vs 177.958.629; pers **empty / 0 VTE**; afschr 100.336.808; expl **+35.841.413** vs +6.606.679; fin opbr 8.418.018; fin kosten 30.961.708; tax 1.320.742; PnL **+12.635.360** vs +159.358.483; dividend **28.540.639** vs 207.761.485; bruto capex **338.207.466**; commissaris 42.558 + extra 56.212; bestuurders 29.288.\\n"
        "- CSVs: sources+4/entities+1/budgets+80/commitments+1/leaderboard+1 + FOI ready `gap_flli_omzet_434_32m_diensten_163_67m_debt_1_55bn_l5` (not sent); rq_1388=done; spawn rq_1389; ticks=1388.\\n"
        "- Coverage: residual dual L5 (Fluvius Limburg leftover energy IGS live WVV). Does **not** move L5 near-complete of EUR 347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs Fluvius EG possible. No progress refresh (not every-10; next 1390).\\n"
        "- Next: rq_1389 residual dual L5 VL JR2025 hole_fill (prefer leftover Fluvius Zenne-Dijle if a 2025 CDN/JR PDF still live and unmined; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS only after leftover IGS/EVA/AGB; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382).\\n"
    )
    entry = entry.replace(chr(92) + "n", chr(10))
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1388 write done")


if __name__ == "__main__":
    main()

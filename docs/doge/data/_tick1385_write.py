# -*- coding: utf-8 -*-
"""Tick 1385 — leftover Fluvius West JR2025 official NBB WVV euros.
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

TICK = "1385"
UTC = "2026-08-19T03:45:00Z"
ENT = "igs_flww"
HIER = "Vlaanderen>WestVlaanderen>IGS>FluviusWest"
GAP = "gap_flww_omzet_541_75m_diensten_173_84m_debt_2_05bn_l5"
SRC = "src_flww_jr2025_nbb"
SRC2 = "src_flww_site"
SRC3 = "src_kbo_flww_0215266160"
SRC4 = "src_flww_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00227938.pdf"
SRC2_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-west/overzichtslijst-besluiten"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0215266160"
SRC4_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-west/overzichtslijst-besluiten"
FOI_EMAIL = ""
FOI_POSTAL = "President Kennedypark 12 8500 Kortrijk"
DRAFT = "docs/doge/foi/drafts/gap_flww_omzet_541_75m_diensten_173_84m_debt_2_05bn_l5.md"
COMM = "comm_flww_jr2025_pnl"
LB = "lb_flww_omzet_541_75m_diensten_173_84m_debt_2_05bn"
VENNOTEN = (
    "Alveringem + Anzegem + Ardooie + Avelgem + De Panne + Deerlijk + "
    "Dentergem + Diksmuide + Gavere + Gistel + Harelbeke + Heuvelland + "
    "Hooglede + Horebeke + Houthulst + Ichtegem + Ieper + Ingelmunster + "
    "Izegem + Kluisbergen + Koekelare + Koksijde + Kortemark + Kortrijk + "
    "Kruisem + Kuurne + Langemark-Poelkapelle + Ledegem + Lendelede + "
    "Lo-Reninge + Maarkedal + Menen + Mesen + Middelkerke + Moorslede + "
    "Nieuwpoort + Oostrozebeke + Oudenaarde + Oudenburg + Pittem + "
    "Poperinge + Roeselare + Ronse + Spiere-Helkijn + Staden + Tielt + "
    "Torhout + Veurne + Vleteren + Waregem + Wervik + Wevelgem + "
    "Wielsbeke + Wingene + Wortegem-Petegem + Zonnebeke + Zulte + Zwalm + Zwevegem"
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


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "Fluvius West (voorheen Gaselwest + Infrax West) jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00227938; AV 09.06.2026)",
                "url": SRC_URL,
                "publisher": "Fluvius West / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1385; official NBB VOL-inb PDF 3.93MB 104p deposit 2026-00227938 header 26.06.2026; "
                    "leftover IGS energy DSO of 59 West- + Oost-Vlaanderen energy municipalities after Gaselwest+Infrax West fusie 01.01.2025; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / "
                    "Paul Eelen + Line Vyvey oordeel zonder voorbehoud assets 3378067279 / PnL 50249954 + benadrukking 6.19 inbreng riolering voorlopig + regulatoire saldi; "
                    "VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62 empty"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Fluvius West official governance page (leftover IGS energy DSO; voorheen Gaselwest + Infrax West; 59 energy vennoten)",
                "url": SRC2_URL,
                "publisher": "Fluvius / Fluvius West",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1385; leftover IGS of 59 West- + Oost-Vlaanderen energy municipalities; "
                    "over.fluvius.be lists besluiten + AV 09.06.2026; statutory 2025 balans is the NBB CDN deposit; "
                    "naamswijziging Gaselwest -> Fluvius West 01.01.2025; fusie met Infrax West / Fluvius West 0205.157.176 01.01.2025"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Fluvius West 0215.266.160",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1385; KBO 0215.266.160 Actief / normale toestand since 17.02.1975; "
                    "statutaire naam FLUVIUS WEST since 01.01.2025; "
                    "Opdrachthoudende vereniging (Vlaams Gewest) since 10.12.2014; "
                    "zetel President Kennedypark 12 8500 Kortrijk since 01.10.2008; 0 VE; "
                    "no KBO email/web/tel; btw since 01.09.1975; "
                    "boekjaar 31 december; NACE 35.140/35.220/35.110/42.220/43.211/71.111/25.210; "
                    "absorbed Fluvius West 0205.157.176 (01.01.2025) and Financieringsvereniging gemeenten Gaselwest 0252.774.080 (01.04.2018)"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Fluvius West FOI channel / official governance + secretariaat (KBO no email)",
                "url": SRC4_URL,
                "publisher": "Fluvius West",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1385; KBO no email/web/tel; zetel/secretariaat President Kennedypark 12 8500 Kortrijk; "
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
                "name_nl": "Fluvius West (voorheen Gaselwest + Infrax West; leftover IGS energy DSO West- + Oost-Vlaanderen)",
                "name_fr": "Fluvius West (ex-Gaselwest + Infrax West; IGS residuel DSO energie Flandre occidentale et orientale)",
                "name_en": "Fluvius West leftover IGS energy DSO (formerly Gaselwest + Infrax West)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1385 leftover residual IGS energy DSO of 59 West- + Oost-Vlaanderen energy municipalities; "
                    "KBO 0215.266.160 Actief since 17.02.1975; naam Gaselwest until 01.01.2025; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 3378067279 omzet 541745938 diensten 173839503 debt 2048270787 pnl 50249954 equity 1295033064 dividend 26125009; "
                    "FOI ready omzet geo empty / 101.3m 74 empty 740 / 173.8m 61 / 2.05bn debt / 26.13m dividend; "
                    "distinct from already-mined Fluvius EG group entity fluvius and Kempen 1384 / Imewo 1383 / INTERGEM 1382"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_flww_assets_2025", ENT, "2025", "3378067279", "2025 assets 3378067279 VOL-inb 20/58; tick1385; primary official NBB WVV; commissaris 3378067279"),
        ("bud_flww_assets_2024", ENT, "2024", "2212213444", "2024 assets 2212213444 comparative (pre-merger Gaselwest surviving); tick1385; primary official NBB WVV 20/58"),
        ("bud_flww_fixed_2025", ENT, "2025", "2964163087", "2025 vaste activa 2964163087 vs 2007208192; tick1385; primary official NBB WVV 21/28"),
        ("bud_flww_iva_2025", ENT, "2025", "19954862", "2025 IVA 19954862 vs 14581211; tick1385; primary official NBB WVV 21"),
        ("bud_flww_iva_acq_2025", ENT, "2025", "22223990", "2025 IVA aanschaf 22223990 (8021); tick1385; primary official NBB WVV 6.2.1"),
        ("bud_flww_mva_2025", ENT, "2025", "2728913242", "2025 MVA 2728913242 vs 1878081870; tick1385; primary official NBB WVV 22/27"),
        ("bud_flww_buildings_2025", ENT, "2025", "79689401", "2025 terreinen/gebouwen 79689401 vs 48421366; tick1385; primary official NBB WVV 22"),
        ("bud_flww_machines_2025", ENT, "2025", "2375613277", "2025 installaties/machines 2375613277 vs 1681538338; tick1385; primary official NBB WVV 23"),
        ("bud_flww_machines_acq_2025", ENT, "2025", "892688226", "2025 machines aanschaf 892688226 (8162; includes merger inflow); tick1385; primary official NBB WVV 6.3"),
        ("bud_flww_furniture_2025", ENT, "2025", "11478447", "2025 meubilair/rollend 11478447 vs 8587170; tick1385; primary official NBB WVV 24"),
        ("bud_flww_lease_mva_2025", ENT, "2025", "15466026", "2025 leasing MVA 15466026 vs 12221570; tick1385; primary official NBB WVV 25"),
        ("bud_flww_other_mva_2025", ENT, "2025", "791864", "2025 overige MVA 791864 vs 199696; tick1385; primary official NBB WVV 26"),
        ("bud_flww_cip_2025", ENT, "2025", "245874227", "2025 CIP 245874227 vs 127113730; aanschaf 398616774 incl merger; tick1385; primary official NBB WVV 27"),
        ("bud_flww_cip_acq_2025", ENT, "2025", "398616774", "2025 CIP aanschaf 398616774 (8166; includes merger inflow); tick1385; primary official NBB WVV 6.3.6"),
        ("bud_flww_fva_2025", ENT, "2025", "215294983", "2025 FVA 215294983 vs 114545112; tick1385; primary official NBB WVV 28"),
        ("bud_flww_fva_part_2025", ENT, "2025", "122371550", "2025 deelnemingen 122371550 (FSO 16.23pct stem); tick1385; primary official NBB WVV 282"),
        ("bud_flww_fva_shares_2025", ENT, "2025", "92923433", "2025 andere aandelen 92923433 vs 95652468; tick1385; primary official NBB WVV 284"),
        ("bud_flww_current_2025", ENT, "2025", "413904192", "2025 vlottende activa 413904192 vs 205005252; tick1385; primary official NBB WVV 29/58"),
        ("bud_flww_ltrecv_2025", ENT, "2025", "107268094", "2025 LT vorderingen 107268094 vs 16334102 (all other 291); tick1385; primary official NBB WVV 29"),
        ("bud_flww_wip_2025", ENT, "2025", "17048603", "2025 bestellingen in uitvoering 17048603 vs 2562318; tick1385; primary official NBB WVV 37"),
        ("bud_flww_strecv_2025", ENT, "2025", "220501148", "2025 ST vorderingen 220501148 vs 123157281; tick1385; primary official NBB WVV 40/41"),
        ("bud_flww_trade_2025", ENT, "2025", "97371111", "2025 handelsvorderingen 97371111 vs 41103951; tick1385; primary official NBB WVV 40"),
        ("bud_flww_othrecv_2025", ENT, "2025", "123130038", "2025 overige ST vorderingen 123130038 vs 82053330; tick1385; primary official NBB WVV 41"),
        ("bud_flww_cash_2025", ENT, "2025", "1337", "2025 liquide middelen 1337 vs 835 (near-zero vs 2.05bn debt); tick1385; primary official NBB WVV 54/58"),
        ("bud_flww_prepaid_2025", ENT, "2025", "69085010", "2025 overlopend actief 69085010 vs 62950716; tick1385; primary official NBB WVV 490/1"),
        ("bud_flww_prepaid_reg_2025", ENT, "2025", "25503107", "2025 regulatoire saldi in prepaid 25503107; tick1385; primary official NBB WVV 6.6"),
        ("bud_flww_equity_2025", ENT, "2025", "1295033064", "2025 eigen vermogen 1295033064 vs 738174516; tick1385; primary official NBB WVV 10/15"),
        ("bud_flww_equity_2024", ENT, "2024", "738174516", "2024 eigen vermogen 738174516 comparative; tick1385; primary official NBB WVV 10/15"),
        ("bud_flww_inbreng_2025", ENT, "2025", "572952588", "2025 inbreng beschikbaar 572952588 vs 347706251; tick1385; primary official NBB WVV 10/11"),
        ("bud_flww_reval_2025", ENT, "2025", "192155112", "2025 herwaarderingsmeerwaarden 192155112 vs 146166249; tick1385; primary official NBB WVV 12"),
        ("bud_flww_reserves_2025", ENT, "2025", "371095351", "2025 reserves 371095351 (onbeschikbaar 102459870 + belastingvrij 979100 + beschikbaar 267656381); tick1385; primary official NBB WVV 13"),
        ("bud_flww_retained_2025", ENT, "2025", "83901633", "2025 overgedragen winst 83901633 vs 41278680; tick1385; primary official NBB WVV 14"),
        ("bud_flww_capsub_2025", ENT, "2025", "74928380", "2025 kapitaalsubsidies 74928380 JUMP vs 2954346; tick1385; primary official NBB WVV 15"),
        ("bud_flww_prov_2025", ENT, "2025", "34763427", "2025 voorzieningen+latenties 34763427 (milieu 4463318 + overige 5000000 + uitgesteld 25300109); pens 160 empty; tick1385; primary official NBB WVV 16"),
        ("bud_flww_env_2025", ENT, "2025", "4463318", "2025 milieuvoorziening 4463318; tick1385; primary official NBB WVV 163"),
        ("bud_flww_debt_2025", ENT, "2025", "2048270787", "2025 schulden 2048270787 vs 1468361815; tick1385; primary official NBB WVV 17/49"),
        ("bud_flww_debt_2024", ENT, "2024", "1468361815", "2024 schulden 1468361815 comparative; tick1385; primary official NBB WVV 17/49"),
        ("bud_flww_lt_2025", ENT, "2025", "1723746813", "2025 LT schulden 1723746813 vs 1310671997 (all financial); tick1385; primary official NBB WVV 17"),
        ("bud_flww_ltbank_2025", ENT, "2025", "1696065512", "2025 LT kredietinstellingen 1696065512 vs 1288657864; tick1385; primary official NBB WVV 173"),
        ("bud_flww_ltlease_2025", ENT, "2025", "15153991", "2025 LT leasing 15153991 vs 11932389; tick1385; primary official NBB WVV 172"),
        ("bud_flww_ltother_2025", ENT, "2025", "12527310", "2025 LT overige leningen 12527310 vs 10081743; tick1385; primary official NBB WVV 174"),
        ("bud_flww_st_2025", ENT, "2025", "281300595", "2025 ST schulden 281300595 vs 131645800; tick1385; primary official NBB WVV 42/48"),
        ("bud_flww_st_due_2025", ENT, "2025", "145623581", "2025 LT-due within year 145623581 vs 77830367; tick1385; primary official NBB WVV 42"),
        ("bud_flww_sttrade_2025", ENT, "2025", "86529313", "2025 leveranciers 86529313 JUMP vs 17701998; tick1385; primary official NBB WVV 440/4"),
        ("bud_flww_stadv_2025", ENT, "2025", "14381842", "2025 vooruitbetalingen 14381842 vs 11372425; tick1385; primary official NBB WVV 46"),
        ("bud_flww_sttax_2025", ENT, "2025", "14002410", "2025 tax ST 14002410 vs 7014884 (soc empty); tick1385; primary official NBB WVV 45"),
        ("bud_flww_stother_2025", ENT, "2025", "20763448", "2025 overige ST 20763448 vs 17726126; tick1385; primary official NBB WVV 47/48"),
        ("bud_flww_accrued_2025", ENT, "2025", "43223380", "2025 overlopend passief 43223380 vs 26044018; tick1385; primary official NBB WVV 492/3"),
        ("bud_flww_reldebt_2025", ENT, "2025", "1504341907", "2025 related-party debt 1504341907 (LT 1357874617 / ST 146467290; FSO-seam 6.15); tick1385; primary official NBB WVV 6.15 9352"),
        ("bud_flww_opsinc_2025", ENT, "2025", "642355755", "2025 bedrijfsopbrengsten 642355755 vs 437668136; tick1385; primary official NBB WVV 70/76A"),
        ("bud_flww_omzet_2025", ENT, "2025", "541745938", "2025 omzet 541745938 JUMP vs 360191712; 6.10 geo empty; tick1385; primary official NBB WVV 70"),
        ("bud_flww_omzet_2024", ENT, "2024", "360191712", "2024 omzet 360191712 comparative; tick1385; primary official NBB WVV 70"),
        ("bud_flww_omzet_elec_2025", ENT, "2025", "431449091", "2025 omzet elektriciteit 431449091 vs 273736238; tick1385; primary official NBB WVV 6.10"),
        ("bud_flww_omzet_gas_2025", ENT, "2025", "84076490", "2025 omzet gas 84076490 vs 83768255; tick1385; primary official NBB WVV 6.10"),
        ("bud_flww_omzet_rio_2025", ENT, "2025", "17181857", "2025 omzet riolering 17181857 vs 2687219; tick1385; primary official NBB WVV 6.10"),
        ("bud_flww_omzet_other_2025", ENT, "2025", "9038499", "2025 omzet overige 9038499 (2024 empty); tick1385; primary official NBB WVV 6.10"),
        ("bud_flww_othops_2025", ENT, "2025", "101341587", "2025 andere bedrijfsopbrengsten 101341587 vs 77176004; 740 empty; tick1385; primary official NBB WVV 74"),
        ("bud_flww_opscost_2025", ENT, "2025", "543639570", "2025 bedrijfskosten 543639570 vs 389028233; tick1385; primary official NBB WVV 60/66A"),
        ("bud_flww_goods_2025", ENT, "2025", "234333671", "2025 handelsgoederen 234333671 vs 160918073; tick1385; primary official NBB WVV 60"),
        ("bud_flww_diensten_2025", ENT, "2025", "173839503", "2025 diensten 173839503 vs 127269686; no split; FSO pass-through; tick1385; primary official NBB WVV 61"),
        ("bud_flww_diensten_2024", ENT, "2024", "127269686", "2024 diensten 127269686 comparative; tick1385; primary official NBB WVV 61"),
        ("bud_flww_pers_2025", ENT, "2025", "0", "2025 bezoldigingen 62 empty / 9087 empty / 0 VTE (werkmaatschappij FSO); tick1385; primary official NBB WVV 62"),
        ("bud_flww_deprec_2025", ENT, "2025", "112867143", "2025 afschrijvingen 112867143 vs 82235357; tick1385; primary official NBB WVV 630"),
        ("bud_flww_othcost_2025", ENT, "2025", "20855363", "2025 andere bedrijfskosten 20855363 (tax 416247 + other 20439116); tick1385; primary official NBB WVV 640/8"),
        ("bud_flww_expl_2025", ENT, "2025", "98716185", "2025 bedrijfswinst 98716185 vs 48639904; tick1385; primary official NBB WVV 9901"),
        ("bud_flww_expl_2024", ENT, "2024", "48639904", "2024 bedrijfswinst 48639904 comparative; tick1385; primary official NBB WVV 9901"),
        ("bud_flww_fininc_2025", ENT, "2025", "16882576", "2025 financiele opbrengsten 16882576 vs 13134206 (FVA 11150705 + vlottende 4389388); tick1385; primary official NBB WVV 75"),
        ("bud_flww_fincost_2025", ENT, "2025", "48899006", "2025 financiele kosten 48899006 vs 35361018 (schulden 48895891); tick1385; primary official NBB WVV 65"),
        ("bud_flww_tax_2025", ENT, "2025", "16905051", "2025 belastingen 16905051 vs 6031789; tick1385; primary official NBB WVV 67/77"),
        ("bud_flww_pnl_2025", ENT, "2025", "50249954", "2025 PnL 9904 50249954 vs 20398636; commissaris 50249954; tick1385; primary official NBB WVV"),
        ("bud_flww_pnl_2024", ENT, "2024", "20398636", "2024 PnL 20398636 comparative; tick1385; primary official NBB WVV 9904"),
        ("bud_flww_alloc_2025", ENT, "2025", "50273721", "2025 te bestemmen 9905 50273721 vs 20412677; tick1385; primary official NBB WVV 9905"),
        ("bud_flww_div_2025", ENT, "2025", "26125009", "2025 dividend/vergoeding inbreng 26125009 DROP vs 29921894; tick1385; primary official NBB WVV 694"),
        ("bud_flww_div_2024", ENT, "2024", "29921894", "2024 dividend 29921894 comparative; tick1385; primary official NBB WVV 694"),
        ("bud_flww_capex_2025", ENT, "2025", "354681000", "2025 gerealiseerd bruto investeringsbudget 354681000 (jaarverslag duizenden); tick1385; primary official NBB WVV jaarverslag"),
        ("bud_flww_comm_2025", ENT, "2025", "34297", "2025 commissaris EY 34297 + extra controle 95445 + taxadvies verbonden 12290; tick1385; primary official NBB WVV 9505"),
        ("bud_flww_comm_extra_2025", ENT, "2025", "95445", "2025 commissaris andere controleopdrachten 95445; tick1385; primary official NBB WVV 95061"),
        ("bud_flww_board_2025", ENT, "2025", "38193", "2025 bestuurders 9503 38193; tick1385; primary official NBB WVV 9503"),
        ("bud_flww_tariff_elec_2025", ENT, "2025", "537", "2025 nettarief elek gezin digitale meter 537 EUR incl btw vs 371 old West / 410 Gaselwest; tick1385; primary official NBB WVV jaarverslag"),
        ("bud_flww_tariff_gas_2025", ENT, "2025", "280", "2025 nettarief gas gezin 280 EUR incl btw vs 305 old West / 269 Gaselwest; tick1385; primary official NBB WVV jaarverslag"),
        ("bud_flww_pens_fso_2025", ENT, "2025", "17275797", "2025 off-balance FSO contractueel pensioen aandeel 17275797.24 + statutair Fluvius OV 11842000; tick1385; primary official NBB WVV 6.20"),
        ("bud_flww_shares_nb_2025", ENT, "2025", "43330734", "2025 aandelen netbeheer+neven 43330734 + Aov 1454103; tick1385; primary official NBB WVV jaarverslag"),
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
                "title": "Fluvius West JR2025 leftover IGS dual (assets 3.38bn / omzet 541.75m / diensten 173.84m / debt 2.05bn / dividend 26.13m)",
                "entity_id": ENT,
                "beneficiary": "Fluvius West / " + VENNOTEN,
                "legal_basis": "WVV OV; Decreet Lokaal Bestuur; Energiedecreet; NBB neerlegging",
                "decision_date": "2026-06-09",
                "start_year": "1975",
                "end_year": "",
                "total_envelope_eur": "3378067279",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL energy DSO — 541.75m omzet (geo empty) / 173.84m diensten / 2.05bn debt / 26.13m dividend",
                "cut_option": "Publish unpublished omzet geo + 101.3m 74 + 173.8m 61 FSO pass-through + 2.05bn debt counterparties + 26.13m dividend per vennoot; do not keep DSO IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1385; assets 3378067279 omzet 541745938 diensten 173839503 debt 2048270787 pnl 50249954 equity 1295033064 dividend 26125009; FOI ready not sent; not TE-additive of 348bn; double_count vs Fluvius EG possible",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Fluvius West JR2025 leftover IGS: assets 3.38bn / omzet 541.75m / diensten 173.84m / debt 2.05bn / dividend 26.13m / 0 VTE",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "173839503",
                "total_cost_eur": "3378067279",
                "tco_notes": (
                    "Leftover dual IGS energy DSO of 59 West- + Oost-Vlaanderen energy municipalities (voorheen Gaselwest + Infrax West): "
                    "assets 3.38bn / equity 1.30bn / pnl +50.25m / omzet 541.75m (geo empty) / "
                    "diensten 173.84m / 0 VTE / debt 2.05bn (related 1.50bn) / dividend 26.13m / cash 1337; "
                    "official NBB WVV live; do not treat 3.38bn as TE-additive of 348bn; double_count vs Fluvius EG possible"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Fluvius West / " + VENNOTEN,
                "stated_goal": "Local leftover IGS map VL energy DSO — JR2025 live; dual omzet-geo/diensten/debt/dividend FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 3.38bn / omzet 541.75m / diensten 173.84m / debt 2.05bn / dividend 26.13m / pnl +50.25m / 0 VTE",
                "absurdity_score": "7.3",
                "cost_score": "8.9",
                "difficulty": "3.0",
                "priority_index": "7.6",
                "cut_proposal": "Publish unpublished omzet geo + 101.3m 74 + 173.8m 61 FSO pass-through + 2.05bn debt counterparties + 26.13m dividend per vennoot; do not keep DSO IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1385; leftover IGS of 59 West- + Oost-Vlaanderen energy municipalities; FOI ready not sent; not TE-additive of 348bn; distinct from Fluvius EG and Kempen 1384 / Imewo 1383 / INTERGEM 1382",
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
                    "omzet 541745938 JUMP vs 360191712 (WVV 70; 6.10 category elek 431449091 / gas 84076490 / riolering 17181857 / other 9038499; geo empty) per vennoot/tariefstroom unpublished "
                    "+ andere bedrijfsopbrengsten 101341587 (WVV 74; 740 empty) "
                    "+ diensten 173839503 vs 127269686 (WVV 61; no split) + goods 234333671 + FSO pass-through (pers 62/9087 empty / 0 VTE) "
                    "+ schulden 2048270787 (LT bank 1696065512; related-party 1504341907) counterparties/rente unpublished "
                    "+ FVA other shares 92923433 unpublished "
                    "+ dividend 26125009 DROP vs 29921894 per vennoot unpublished "
                    "+ cash 1337 vs debt 2.05bn + prepaid 69085010 (regulatoire 25503107) + VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.18/9 not filed"
                ),
                "why_it_matters": (
                    "Leftover IGS OV energy DSO of 59 mined West- + Oost-Vlaanderen energy municipalities "
                    "(same leftover-IGS energy seam as Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382; distinct from Fluvius EG): "
                    "3.38bn assets / 541.75m omzet / 173.84m diensten / 2.05bn debt / 26.13m dividend / "
                    "0 VTE / FSO shell "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Fluvius West / Raad van Bestuur / Christof Dejaegher / Véronique Buyck / 59 West- + Oost-Vlaanderen energy vennoten",
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
                    "tick1385 leftover IGS OV energy DSO of 59 West- + Oost-Vlaanderen energy municipalities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (3.93MB 104p deposit 2026-00227938). "
                    "Fluvius Kempen already mined 1384 — skipped. Imewo already mined 1383 — skipped. INTERGEM already mined 1382 — skipped. "
                    "INTERZA already mined 1381 — skipped. INCOVO already mined 1380 — skipped. ISVAG already mined 1379 — skipped. De Nekker already mined 1378 — skipped. "
                    "MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. "
                    "Nuhma-group seam 1353-1365 skipped. Fluvius EG group already mined — this is a different legal person. "
                    "Other Fluvius DNB holdings (Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle) leftover next if CDN live. "
                    "Dommelhof leftover Limburg EVA 0777.495.085 not re-probed once live West extracted. "
                    "IVAREM still 2024. Otary RS Nuhma-adjacent fallback not taken. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1385",
        "title": "Fluvius West / Gaselwest JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Fluvius West leftover IGS energy DSO of 59 West- + Oost-Vlaanderen energy municipalities after honest hunt; "
            "KBO 0215.266.160 Actief; live JR2025 official NBB WVV VOL-inb PDF (3.93MB 104p deposit 2026-00227938; commissaris EY); "
            "sourced euros assets 3378067279 / omzet 541745938 / diensten 173839503 / debt 2048270787 / pnl 50249954 / dividend 26125009; "
            "FOI ready omzet geo empty / 101.3m 74 / 173.8m 61 / 2.05bn debt / 26.13m dividend"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T03:10:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1385 Fluvius West leftover IGS energy residual; KBO 0215.266.160; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1386 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1386",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1385 done including Fluvius West 1385 leftover energy IGS live NBB WVV / "
            "Fluvius Kempen 1384 leftover energy IGS live NBB WVV / "
            "Fluvius Imewo 1383 leftover energy IGS live NBB WVV / "
            "INTERGEM / Fluvius Midden-Vlaanderen 1382 leftover energy IGS live NBB WVV / "
            "INTERZA 1381 leftover IGS live NBB WVV / "
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
            "other Fluvius DNB holdings leftover energy IGS (Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle) — take if a 2025 CDN/JR PDF still live and unmined; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads "
            "(old VZW 0443.049.478 CDN 2026-00325874 is a different Tielt-Winge entity); "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB PIH / APB Inovant / APB Atlas listed or leftover but provincieantwerpen.be 403 — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1385 after Fluvius West leftover energy IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1385", rq_new, rq_spawn)
    print("research_queue 1385", found, "spawned_1386", spawned)

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
                "last_unit_id": "rq_1385",
                "ticks_completed": "1385",
                "paused": "no",
                "notes": (
                    "tick1385 Fluvius West leftover IGS energy residual; KBO 0215.266.160; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 3378067279 omzet 541745938 diensten 173839503 debt 2048270787 pnl 50249954 equity 1295033064 dividend 26125009; "
                    "FOI ready omzet geo empty/101.3m 74/173.8m 61/2.05bn debt/26.13m div; next rq_1386 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    entry = """### Tick 1385 - 2026-08-19 - rq_1385 Fluvius West / Gaselwest dual residual leftover
- Unit: Fluvius West (voorheen Gaselwest / Intercommunale Maatschappij Voor GAS en Elektriciteit Van HET Westen + fusie Infrax West 0205.157.176 01.01.2025; leftover IGS opdrachthoudende vereniging / energy DSO elektriciteit + aardgas + riolering + openbare verlichting + warmte of 59 mined West- + Oost-Vlaanderen energy municipalities; werkmaatschappij Fluvius System Operator) after residual dual hunt (KBO **0215.266.160**; official over.fluvius.be has besluiten/governance; live NBB WVV VOL-inb deposit **2026-00227938** PDF 3.93MB / 104p; AV **09.06.2026**; header **26.06.2026**; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / Paul Eelen + Line Vyvey signed oordeel zonder voorbehoud assets 3.378.067.279 / PnL +50.249.954 + benadrukking VOL-inb 6.19 inbreng riolering voorlopige waarde + regulatoire saldi). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; preferred leftover other Fluvius DNB holdings this tick). Distinct from already-mined Fluvius Kempen 1384 / Imewo 1383 / INTERGEM / Fluvius Midden-Vlaanderen 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 / Fluvius EG group-level (entity `fluvius`). First confirmed not already mined: no Fluvius West / Gaselwest / 0215.266.160 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **17.02.1975**; statutaire naam FLUVIUS WEST since 01.01.2025; Opdrachthoudende vereniging (Vlaams Gewest) since 10.12.2014; zetel President Kennedypark 12 8500 Kortrijk since 01.10.2008; **0 VE**; KBO no email/web/tel; official site https://over.fluvius.be/; btw since 01.09.1975; boekjaar 31 december; NACE 35.140/35.220/35.110/42.220/43.211/71.111/25.210. Absorbed Fluvius West / Infrax West 0205.157.176 (01.01.2025) and Financieringsvereniging gemeenten Gaselwest 0252.774.080 (01.04.2018). Voorzitter Christof Dejaegher; commissaris EY since 09.06.2025 tot 09.06.2028. Hunt leftover AGB/zorg/EVA first: leftover AGB Mechelen/Kortrijk/Brugge/Roeselare/Oostende 404/403 as of 1375 — not re-probed once live West extracted; Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live West extracted; IVAREM still 2024; leftover APB provincieantwerpen.be 403. Fluvius West statutory CDN live this tick (HTTP 200 / 3926873 / 104p) — taken (preferred leftover energy IGS of mined West municipalities outside Nuhma; listed leftover-next after Kempen 1384). Fluvius Kempen already mined 1384 — skipped. Imewo already mined 1383 — skipped. INTERGEM already mined 1382 — skipped. INTERZA already mined 1381 — skipped. INCOVO already mined 1380 — skipped. ISVAG already mined 1379 — skipped. De Nekker already mined 1378 — skipped. MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 already mined — skipped. Fluvius EG group already mined — this is a different legal person (DSO holding). Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. Other Fluvius DNB holdings (Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle) leftover next. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366. Not every-10 (next 1390).
- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud assets 3.378.067.279 / PnL +50.249.954 + benadrukking 6.19; VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62/9087 empty): assets **3.378.067.279** (was 2.212.213.444; JUMP via Gaselwest+Infrax West fusie); fixed **2.964.163.087** / MVA **2.728.913.242** (gebouwen **79.689.401**; machines **2.375.613.277**; meubilair **11.478.447**; leasing **15.466.026**; overige **791.864**; CIP **245.874.227** aanschaf **398.616.774** incl merger); IVA 19.954.862; FVA **215.294.983** (deelnemingen **122.371.550** FSO 16,23%; andere aandelen **92.923.433**); current **413.904.192**; LT recv 107.268.094; WIP 17.048.603; ST recv **220.501.148** (trade 97.371.111 + other 123.130.038); beleggingen empty; cash **1.337** vs 835; prepaid **69.085.010** (regulatoire 25.503.107); equity **1.295.033.064** (inbreng 572.952.588; reval 192.155.112; reserves 371.095.351; overgedragen 83.901.633; capsub 74.928.380 JUMP); voorzieningen **34.763.427** (milieu 4.463.318; pens 160 empty); schulden **2.048.270.787** (LT **1.723.746.813** waarvan bank **1.696.065.512** + lease 15.153.991 + other 12.527.310; ST **281.300.595** waarvan LT-due 145.623.581 + leveranciers **86.529.313 JUMP** vs 17.701.998; related-party FSO-seam **1.504.341.907**); omzet **541.745.938 JUMP** vs 360.191.712 (elek **431.449.091** / gas **84.076.490** / riolering **17.181.857** / other **9.038.499**; geo empty); othops **101.341.587** (740 empty); goods **234.333.671**; diensten **173.839.503** vs 127.269.686; pers **empty / 0 VTE**; afschr 112.867.143; expl **+98.716.185** vs +48.639.904; fin opbr 16.882.576; fin kosten 48.899.006; tax 16.905.051; PnL **+50.249.954** vs +20.398.636; dividend **26.125.009 DROP** vs 29.921.894; bruto capex jaarverslag **354.681.000**; commissaris 34.297 + extra 95.445; bestuurders 38.193. Jaarverslag same deposit: 59 energy vennoten + leftover cable/riolering deelnemers; nettarief gezin elek **537** vs 371 old West / 410 Gaselwest / gas **280** vs 305 old West / 269 Gaselwest; naamswijziging Gaselwest -> Fluvius West 01.01.2025; FSO stemaandeel 16,23%.
- CSVs: sources+4/entities+1/budgets+81/commitments+1/leaderboard+1 + FOI ready `gap_flww_omzet_541_75m_diensten_173_84m_debt_2_05bn_l5` (not sent); rq_1385=done; spawn rq_1386; ticks=1385.
- Coverage: residual dual L5 (Fluvius West leftover energy IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs Fluvius EG possible. No progress refresh (not every-10; next 1390).
- Next: rq_1386 residual dual L5 VL JR2025 hole_fill (prefer leftover other Fluvius DNB holdings Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle if a 2025 CDN/JR PDF still live and unmined; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS CDN 2026-00254280 / Rematics / Sunfin only if taken after leftover IGS/EVA/AGB; leftover APB POA / TPA / De Schorre / Warande / PIH / Inovant / Atlas only if a real PDF downloads; IVAREM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1385 write done")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Tick 1383 — leftover Fluvius Imewo JR2025 official NBB WVV euros.
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

TICK = "1383"
UTC = "2026-08-19T02:45:00Z"
ENT = "igs_imew"
HIER = "Vlaanderen>OostWestVlaanderen>IGS>FluviusImewo"
GAP = "gap_imew_omzet_544_91m_diensten_185_22m_debt_2_29bn_l5"
SRC = "src_imew_jr2025_nbb"
SRC2 = "src_imew_site"
SRC3 = "src_kbo_imew_0215362368"
SRC4 = "src_imew_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00225268.pdf"
SRC2_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-imewo/overzichtslijst-besluiten"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0215362368"
SRC4_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-imewo/overzichtslijst-besluiten"
FOI_EMAIL = ""
FOI_POSTAL = "Brusselsesteenweg 199 9090 Merelbeke-Melle"
DRAFT = "docs/doge/foi/drafts/gap_imew_omzet_544_91m_diensten_185_22m_debt_2_29bn_l5.md"
COMM = "comm_imew_jr2025_pnl"
LB = "lb_imew_omzet_544_91m_diensten_185_22m_debt_2_29bn"
VENNOTEN = (
    "Aalter + Assenede + Beernem + Berlare + Blankenberge + Bredene + "
    "Brugge + Damme + De Haan + Deinze + Destelbergen + Eeklo + Evergem + "
    "Gent + Jabbeke + Kaprijke + Knokke-Heist + Laarne + Lede + "
    "Lichtervelde + Lievegem + Lochristi + Lokeren + Maldegem + "
    "Merelbeke-Melle + Nazareth-De Pinte + Oostende + Oosterzele + "
    "Oostkamp + Sint-Laureins + Sint-Lievens-Houtem + Sint-Martens-Latem + "
    "Wetteren + Wichelen + Zedelgem + Zele + Zelzate + Zuienkerke"
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
                "title": "Fluvius Imewo (voorheen Imewo) jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00225268; AV 08.06.2026)",
                "url": SRC_URL,
                "publisher": "Fluvius Imewo / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1383; official NBB VOL-inb PDF 1.61MB 92p deposit 2026-00225268 created 30.06.2026 header 26.06.2026; "
                    "leftover IGS energy DSO of 38 Oost- + West-Vlaanderen municipalities (voorheen Imewo); "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / "
                    "Paul Eelen A02213 + Line Vyvey A02501 oordeel zonder voorbehoud assets 3069003579 / PnL 42031854 + benadrukking 6.19 regulatoire saldi; "
                    "VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.8/6.12/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62 empty"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Fluvius Imewo official governance page (leftover IGS energy DSO; voorheen Imewo; 38 Oost- + West-Vlaanderen vennoten)",
                "url": SRC2_URL,
                "publisher": "Fluvius / Fluvius Imewo",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1383; leftover IGS of 38 Oost- + West-Vlaanderen municipalities; "
                    "over.fluvius.be lists besluiten; statutory 2025 balans is the NBB CDN deposit; "
                    "naamswijziging Imewo -> Fluvius Imewo 01.01.2025; AV 08.06.2026 published 18.06.2026"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Fluvius Imewo 0215.362.368",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1383; KBO 0215.362.368 Actief / normale toestand since 10.03.1975; "
                    "statutaire naam FLUVIUS IMEWO since 01.01.2025; "
                    "Opdrachthoudende vereniging (Vlaams Gewest) since 07.11.2003; "
                    "zetel Brusselsesteenweg 199 9090 Merelbeke-Melle since 01.01.2025; 0 VE; "
                    "no KBO email/web/tel; btw since 01.10.1975; "
                    "jaarvergadering mei; boekjaar 31 december; NACE 35.140/35.220/42.220/43.211/71.111/35.110/25.210; "
                    "absorbed Financieringsintercommunale West- en Oost-Vlaanderen 0252.903.744 (01.04.2018)"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Fluvius Imewo FOI channel / official governance + secretariaat (KBO no email)",
                "url": SRC4_URL,
                "publisher": "Fluvius Imewo",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1383; KBO no email/web/tel; zetel/secretariaat Brusselsesteenweg 199 9090 Merelbeke-Melle; "
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
                "name_nl": "Fluvius Imewo (voorheen Imewo; leftover IGS energy DSO Oost- + West-Vlaanderen)",
                "name_fr": "Fluvius Imewo (ex-Imewo; IGS residuel DSO energie Flandre orientale et occidentale)",
                "name_en": "Fluvius Imewo leftover IGS energy DSO (formerly Imewo)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1383 leftover residual IGS energy DSO of 38 Oost- + West-Vlaanderen municipalities; "
                    "KBO 0215.362.368 Actief since 10.03.1975; naam Imewo until 01.01.2025; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 3069003579 omzet 544911033 diensten 185219326 debt 2293851040 pnl 42031854 equity 772545254 dividend 17418700; "
                    "FOI ready omzet geo empty / 94.2m 74 empty 740 / 185.2m 61 / 2.29bn debt / 17.42m dividend; "
                    "distinct from already-mined Fluvius EG group entity fluvius and INTERGEM / Fluvius Midden-Vlaanderen 1382"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_imew_assets_2025", ENT, "2025", "3069003579", "2025 assets 3069003579 VOL-inb 20/58; tick1383; primary official NBB WVV; commissaris 3069003579"),
        ("bud_imew_assets_2024", ENT, "2024", "2719289174", "2024 assets 2719289174 comparative; tick1383; primary official NBB WVV 20/58"),
        ("bud_imew_fixed_2025", ENT, "2025", "2802706299", "2025 vaste activa 2802706299 vs 2510111089; tick1383; primary official NBB WVV 21/28"),
        ("bud_imew_iva_2025", ENT, "2025", "21028817", "2025 IVA 21028817 vs 19620069; tick1383; primary official NBB WVV 21"),
        ("bud_imew_iva_acq_2025", ENT, "2025", "12500255", "2025 IVA aanschaf 12500255 (8021); tick1383; primary official NBB WVV 6.2.1"),
        ("bud_imew_mva_2025", ENT, "2025", "2643277966", "2025 MVA 2643277966 vs 2357512049; tick1383; primary official NBB WVV 22/27"),
        ("bud_imew_buildings_2025", ENT, "2025", "64688429", "2025 terreinen/gebouwen 64688429 vs 61977706; tick1383; primary official NBB WVV 22"),
        ("bud_imew_machines_2025", ENT, "2025", "2248143242", "2025 installaties/machines 2248143242 vs 2043619129; tick1383; primary official NBB WVV 23"),
        ("bud_imew_machines_acq_2025", ENT, "2025", "164578834", "2025 machines aanschaf 164578834 (8162); tick1383; primary official NBB WVV 6.3"),
        ("bud_imew_furniture_2025", ENT, "2025", "15015356", "2025 meubilair/rollend 15015356 vs 13172166; tick1383; primary official NBB WVV 24"),
        ("bud_imew_lease_mva_2025", ENT, "2025", "12160746", "2025 leasing MVA 12160746 vs 11484253; tick1383; primary official NBB WVV 25"),
        ("bud_imew_other_mva_2025", ENT, "2025", "716673", "2025 overige MVA 716673 vs 110157; tick1383; primary official NBB WVV 26"),
        ("bud_imew_cip_2025", ENT, "2025", "302553520", "2025 CIP 302553520 vs 227148638; aanschaf 307690209; tick1383; primary official NBB WVV 27"),
        ("bud_imew_cip_acq_2025", ENT, "2025", "307690209", "2025 CIP aanschaf 307690209 (8166); tick1383; primary official NBB WVV 6.3.6"),
        ("bud_imew_fva_2025", ENT, "2025", "138399516", "2025 FVA 138399516 vs 132978970; tick1383; primary official NBB WVV 28"),
        ("bud_imew_fva_part_2025", ENT, "2025", "32872626", "2025 deelnemingen 32872626 (FSO 18.57pct); tick1383; primary official NBB WVV 282"),
        ("bud_imew_fva_shares_2025", ENT, "2025", "105526891", "2025 andere aandelen 105526891 vs 101982644 after aanschaf 3544247; tick1383; primary official NBB WVV 284"),
        ("bud_imew_fva_acq_2025", ENT, "2025", "3544247", "2025 FVA andere aandelen aanschaf 3544247; tick1383; primary official NBB WVV 6.4.3 8363"),
        ("bud_imew_current_2025", ENT, "2025", "266297280", "2025 vlottende activa 266297280 vs 209178085; tick1383; primary official NBB WVV 29/58"),
        ("bud_imew_ltrecv_2025", ENT, "2025", "7252565", "2025 LT vorderingen 7252565 vs 8921966 (all other 291); tick1383; primary official NBB WVV 29"),
        ("bud_imew_wip_2025", ENT, "2025", "10613583", "2025 bestellingen in uitvoering 10613583 vs 8935386; tick1383; primary official NBB WVV 37"),
        ("bud_imew_strecv_2025", ENT, "2025", "176069219", "2025 ST vorderingen 176069219 vs 119820714; tick1383; primary official NBB WVV 40/41"),
        ("bud_imew_trade_2025", ENT, "2025", "87251277", "2025 handelsvorderingen 87251277 vs 63412728; tick1383; primary official NBB WVV 40"),
        ("bud_imew_othrecv_2025", ENT, "2025", "88817942", "2025 overige ST vorderingen 88817942 vs 56407986; tick1383; primary official NBB WVV 41"),
        ("bud_imew_cash_2025", ENT, "2025", "993", "2025 liquide middelen 993 vs 1503 (near-zero vs 2.29bn debt); tick1383; primary official NBB WVV 54/58"),
        ("bud_imew_prepaid_2025", ENT, "2025", "72360920", "2025 overlopend actief 72360920 (VNR 28405832 / REG 14833223 / pens 14430250 / verbruiken 13560300); tick1383; primary official NBB WVV 490/1"),
        ("bud_imew_equity_2025", ENT, "2025", "772545254", "2025 eigen vermogen 772545254 vs 715140711; tick1383; primary official NBB WVV 10/15"),
        ("bud_imew_equity_2024", ENT, "2024", "715140711", "2024 eigen vermogen 715140711 comparative; tick1383; primary official NBB WVV 10/15"),
        ("bud_imew_inbreng_2025", ENT, "2025", "359573487", "2025 inbreng beschikbaar 359573487 vs 347514810; tick1383; primary official NBB WVV 10/11"),
        ("bud_imew_reval_2025", ENT, "2025", "154851529", "2025 herwaarderingsmeerwaarden 154851529 vs 155442545; tick1383; primary official NBB WVV 12"),
        ("bud_imew_reserves_2025", ENT, "2025", "190084800", "2025 reserves 190084800 (onbeschikbaar 57496749 + belastingvrij 2620885 + beschikbaar 129967166); tick1383; primary official NBB WVV 13"),
        ("bud_imew_retained_2025", ENT, "2025", "67496612", "2025 overgedragen winst 67496612 vs 39684291; tick1383; primary official NBB WVV 14"),
        ("bud_imew_capsub_2025", ENT, "2025", "538826", "2025 kapitaalsubsidies 538826 vs 451328; tick1383; primary official NBB WVV 15"),
        ("bud_imew_prov_2025", ENT, "2025", "2607285", "2025 voorzieningen+latenties 2607285 (milieu 2114765 + uitgesteld 492520); pens 160 empty; tick1383; primary official NBB WVV 16"),
        ("bud_imew_env_2025", ENT, "2025", "2114765", "2025 milieuvoorziening 2114765; tick1383; primary official NBB WVV 163"),
        ("bud_imew_debt_2025", ENT, "2025", "2293851040", "2025 schulden 2293851040 vs 2001584542; tick1383; primary official NBB WVV 17/49"),
        ("bud_imew_debt_2024", ENT, "2024", "2001584542", "2024 schulden 2001584542 comparative; tick1383; primary official NBB WVV 17/49"),
        ("bud_imew_lt_2025", ENT, "2025", "1925545654", "2025 LT schulden 1925545654 vs 1766906236 (all financial); tick1383; primary official NBB WVV 17"),
        ("bud_imew_ltbank_2025", ENT, "2025", "1823111037", "2025 LT kredietinstellingen 1823111037 vs 1724822410; tick1383; primary official NBB WVV 173"),
        ("bud_imew_ltlease_2025", ENT, "2025", "11907348", "2025 LT leasing 11907348 vs 11202831; tick1383; primary official NBB WVV 172"),
        ("bud_imew_ltother_2025", ENT, "2025", "90527269", "2025 LT overige leningen 90527269 JUMP vs 30880995; tick1383; primary official NBB WVV 174"),
        ("bud_imew_st_2025", ENT, "2025", "299480941", "2025 ST schulden 299480941 vs 194431172; tick1383; primary official NBB WVV 42/48"),
        ("bud_imew_st_due_2025", ENT, "2025", "161070183", "2025 LT-due within year 161070183 vs 104992656; tick1383; primary official NBB WVV 42"),
        ("bud_imew_sttrade_2025", ENT, "2025", "87060409", "2025 leveranciers 87060409 JUMP vs 18255146; tick1383; primary official NBB WVV 440/4"),
        ("bud_imew_stadv_2025", ENT, "2025", "24238465", "2025 vooruitbetalingen 24238465 vs 22201375; tick1383; primary official NBB WVV 46"),
        ("bud_imew_sttax_2025", ENT, "2025", "13552085", "2025 tax ST 13552085 vs 11563905 (soc empty); tick1383; primary official NBB WVV 45"),
        ("bud_imew_stother_2025", ENT, "2025", "13559800", "2025 overige ST 13559800 vs 37418090; tick1383; primary official NBB WVV 47/48"),
        ("bud_imew_accrued_2025", ENT, "2025", "68824445", "2025 overlopend passief 68824445 (intrest 27164523 + VNR 25028489 + GSC 11736500); tick1383; primary official NBB WVV 492/3"),
        ("bud_imew_reldebt_2025", ENT, "2025", "1604090869", "2025 related-party debt 1604090869 (LT 1448048967 / ST 156041902; FSO-seam 6.15); tick1383; primary official NBB WVV 6.15 9352"),
        ("bud_imew_opsinc_2025", ENT, "2025", "640720641", "2025 bedrijfsopbrengsten 640720641 vs 522063969; tick1383; primary official NBB WVV 70/76A"),
        ("bud_imew_omzet_2025", ENT, "2025", "544911033", "2025 omzet 544911033 JUMP vs 426186254; 6.10 geo empty; tick1383; primary official NBB WVV 70"),
        ("bud_imew_omzet_2024", ENT, "2024", "426186254", "2024 omzet 426186254 comparative; tick1383; primary official NBB WVV 70"),
        ("bud_imew_omzet_elec_2025", ENT, "2025", "432036280", "2025 omzet elektriciteit 432036280 vs 308854356; tick1383; primary official NBB WVV 6.10"),
        ("bud_imew_omzet_gas_2025", ENT, "2025", "107256781", "2025 omzet gas 107256781 vs 110838155; tick1383; primary official NBB WVV 6.10"),
        ("bud_imew_omzet_other_2025", ENT, "2025", "5617972", "2025 omzet overige 5617972 vs 6493743; tick1383; primary official NBB WVV 6.10"),
        ("bud_imew_othops_2025", ENT, "2025", "94181775", "2025 andere bedrijfsopbrengsten 94181775 vs 94949466; 740 empty; tick1383; primary official NBB WVV 74"),
        ("bud_imew_opscost_2025", ENT, "2025", "543674883", "2025 bedrijfskosten 543674883 vs 462270038; tick1383; primary official NBB WVV 60/66A"),
        ("bud_imew_goods_2025", ENT, "2025", "217679821", "2025 handelsgoederen 217679821 vs 160725556; tick1383; primary official NBB WVV 60"),
        ("bud_imew_diensten_2025", ENT, "2025", "185219326", "2025 diensten 185219326 vs 179219682; no split; FSO pass-through; tick1383; primary official NBB WVV 61"),
        ("bud_imew_diensten_2024", ENT, "2024", "179219682", "2024 diensten 179219682 comparative; tick1383; primary official NBB WVV 61"),
        ("bud_imew_pers_2025", ENT, "2025", "0", "2025 bezoldigingen 62 empty / 9087 empty / 0 VTE (werkmaatschappij FSO); tick1383; primary official NBB WVV 62"),
        ("bud_imew_deprec_2025", ENT, "2025", "113031011", "2025 afschrijvingen 113031011 vs 101846589; tick1383; primary official NBB WVV 630"),
        ("bud_imew_othcost_2025", ENT, "2025", "28646542", "2025 andere bedrijfskosten 28646542 (tax 284039 + other 28362503); tick1383; primary official NBB WVV 640/8"),
        ("bud_imew_expl_2025", ENT, "2025", "97045759", "2025 bedrijfswinst 97045759 vs 59793931; tick1383; primary official NBB WVV 9901"),
        ("bud_imew_expl_2024", ENT, "2024", "59793931", "2024 bedrijfswinst 59793931 comparative; tick1383; primary official NBB WVV 9901"),
        ("bud_imew_fininc_2025", ENT, "2025", "13458279", "2025 financiele opbrengsten 13458279 vs 12612233 (FVA 12563583 + vlottende 849787); tick1383; primary official NBB WVV 75"),
        ("bud_imew_fincost_2025", ENT, "2025", "55747090", "2025 financiele kosten 55747090 vs 47993837 (schulden 55745702); tick1383; primary official NBB WVV 65"),
        ("bud_imew_tax_2025", ENT, "2025", "12746249", "2025 belastingen 12746249 vs 4799646; tick1383; primary official NBB WVV 67/77"),
        ("bud_imew_pnl_2025", ENT, "2025", "42031854", "2025 PnL 9904 42031854 vs 19630098; commissaris 42031854; tick1383; primary official NBB WVV"),
        ("bud_imew_pnl_2024", ENT, "2024", "19630098", "2024 PnL 19630098 comparative; tick1383; primary official NBB WVV 9904"),
        ("bud_imew_alloc_2025", ENT, "2025", "42050450", "2025 te bestemmen 9905 42050450 vs 19647526; tick1383; primary official NBB WVV 9905"),
        ("bud_imew_div_2025", ENT, "2025", "17418700", "2025 dividend/vergoeding inbreng 17418700 DROP vs 28332698; tick1383; primary official NBB WVV 694"),
        ("bud_imew_div_2024", ENT, "2024", "28332698", "2024 dividend 28332698 comparative; tick1383; primary official NBB WVV 694"),
        ("bud_imew_capex_2025", ENT, "2025", "184060000", "2025 gerealiseerd bruto investeringsbudget 184060000 (jaarverslag duizenden); tick1383; primary official NBB WVV jaarverslag"),
        ("bud_imew_comm_2025", ENT, "2025", "12378", "2025 commissaris EY 12378 + extra controle 62485 + taxadvies verbonden 12532; tick1383; primary official NBB WVV 9505"),
        ("bud_imew_comm_extra_2025", ENT, "2025", "62485", "2025 commissaris andere controleopdrachten 62485; tick1383; primary official NBB WVV 95061"),
        ("bud_imew_board_2025", ENT, "2025", "31867", "2025 bestuurders 9503 31867; tick1383; primary official NBB WVV 9503"),
        ("bud_imew_tariff_elec_2025", ENT, "2025", "478", "2025 nettarief elek gezin digitale meter 478 EUR incl btw vs 357; tick1383; primary official NBB WVV jaarverslag"),
        ("bud_imew_tariff_gas_2025", ENT, "2025", "277", "2025 nettarief gas gezin 277 EUR incl btw vs 260; tick1383; primary official NBB WVV jaarverslag"),
        ("bud_imew_shares_nb_2025", ENT, "2025", "28882938", "2025 aandelen netbeheer+neven 28882938 + Aov 1558680; tick1383; primary official NBB WVV jaarverslag"),
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
                "title": "Fluvius Imewo JR2025 leftover IGS dual (assets 3.07bn / omzet 544.91m / diensten 185.22m / debt 2.29bn / dividend 17.42m)",
                "entity_id": ENT,
                "beneficiary": "Fluvius Imewo / " + VENNOTEN,
                "legal_basis": "WVV OV; Decreet Lokaal Bestuur; Energiedecreet; NBB neerlegging",
                "decision_date": "2026-06-08",
                "start_year": "1975",
                "end_year": "",
                "total_envelope_eur": "3069003579",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL energy DSO — 544.91m omzet (geo empty) / 185.22m diensten / 2.29bn debt / 17.42m dividend",
                "cut_option": "Publish unpublished omzet geo + 94.2m 74 + 185.2m 61 FSO pass-through + 2.29bn debt counterparties + 17.42m dividend per vennoot; do not keep DSO IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1383; assets 3069003579 omzet 544911033 diensten 185219326 debt 2293851040 pnl 42031854 equity 772545254 dividend 17418700; FOI ready not sent; not TE-additive of 348bn; double_count vs Fluvius EG possible",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Fluvius Imewo JR2025 leftover IGS: assets 3.07bn / omzet 544.91m / diensten 185.22m / debt 2.29bn / dividend 17.42m / 0 VTE",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "185219326",
                "total_cost_eur": "3069003579",
                "tco_notes": (
                    "Leftover dual IGS energy DSO of 38 Oost- + West-Vlaanderen municipalities (voorheen Imewo): "
                    "assets 3.07bn / equity 772.5m / pnl +42.03m / omzet 544.91m (geo empty) / "
                    "diensten 185.22m / 0 VTE / debt 2.29bn (related 1.60bn) / dividend 17.42m / cash 993; "
                    "official NBB WVV live; do not treat 3.07bn as TE-additive of 348bn; double_count vs Fluvius EG possible"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Fluvius Imewo / " + VENNOTEN,
                "stated_goal": "Local leftover IGS map VL energy DSO — JR2025 live; dual omzet-geo/diensten/debt/dividend FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 3.07bn / omzet 544.91m / diensten 185.22m / debt 2.29bn / dividend 17.42m / pnl +42.03m / 0 VTE",
                "absurdity_score": "7.5",
                "cost_score": "9.2",
                "difficulty": "3.0",
                "priority_index": "7.9",
                "cut_proposal": "Publish unpublished omzet geo + 94.2m 74 + 185.2m 61 FSO pass-through + 2.29bn debt counterparties + 17.42m dividend per vennoot; do not keep DSO IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1383; leftover IGS of 38 Oost- + West-Vlaanderen municipalities; FOI ready not sent; not TE-additive of 348bn; distinct from Fluvius EG and INTERGEM 1382",
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
                    "omzet 544911033 JUMP vs 426186254 (WVV 70; 6.10 category elek 432036280 / gas 107256781 / other 5617972; geo empty) per vennoot/tariefstroom unpublished "
                    "+ andere bedrijfsopbrengsten 94181775 (WVV 74; 740 empty) "
                    "+ diensten 185219326 vs 179219682 (WVV 61; no split) + goods 217679821 + FSO pass-through (pers 62/9087 empty / 0 VTE) "
                    "+ schulden 2293851040 (LT bank 1823111037; related-party 1604090869) counterparties/rente unpublished "
                    "+ FVA other shares 105526891 after aanschaf 3544247 unpublished "
                    "+ dividend 17418700 DROP vs 28332698 per vennoot unpublished "
                    "+ cash 993 vs debt 2.29bn + prepaid VNR/REG/pens 72360920 + VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.8/6.12/6.18/9 not filed"
                ),
                "why_it_matters": (
                    "Leftover IGS OV energy DSO of 38 mined Oost- + West-Vlaanderen municipalities "
                    "(same leftover-IGS energy seam as INTERGEM 1382; distinct from Fluvius EG): "
                    "3.07bn assets / 544.91m omzet / 185.22m diensten / 2.29bn debt / 17.42m dividend / "
                    "0 VTE / FSO shell "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Fluvius Imewo / Raad van Bestuur / Joris Vandenbroucke / Rutger De Reu / 38 Oost- + West-Vlaanderen vennoten",
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
                    "tick1383 leftover IGS OV energy DSO of 38 Oost- + West-Vlaanderen municipalities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (1.61MB 92p deposit 2026-00225268). "
                    "INTERGEM already mined 1382 — skipped. INTERZA already mined 1381 — skipped. INCOVO already mined 1380 — skipped. "
                    "ISVAG already mined 1379 — skipped. De Nekker already mined 1378 — skipped. MIROM Menen already mined 1377 — skipped. "
                    "MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. "
                    "Nuhma-group seam 1353-1365 skipped. Fluvius EG group already mined — this is a different legal person. "
                    "Other Fluvius DNB holdings (Kempen / West / Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle) leftover next if CDN live. "
                    "Dommelhof leftover Limburg EVA 0777.495.085 not re-probed once live Imewo extracted. "
                    "IVAREM still 2024. Otary RS Nuhma-adjacent fallback not taken. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1383",
        "title": "Imewo / Fluvius Imewo JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Fluvius Imewo leftover IGS energy DSO of 38 Oost- + West-Vlaanderen municipalities after honest hunt; "
            "KBO 0215.362.368 Actief; live JR2025 official NBB WVV VOL-inb PDF (1.61MB 92p deposit 2026-00225268; commissaris EY); "
            "sourced euros assets 3069003579 / omzet 544911033 / diensten 185219326 / debt 2293851040 / pnl 42031854 / dividend 17418700; "
            "FOI ready omzet geo empty / 94.2m 74 / 185.2m 61 / 2.29bn debt / 17.42m dividend"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T02:25:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1383 Imewo leftover IGS energy residual; KBO 0215.362.368; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1384 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1384",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1383 done including Fluvius Imewo 1383 leftover energy IGS live NBB WVV / "
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
            "other Fluvius DNB holdings leftover energy IGS (Kempen-Iveka / West-Gaselwest / Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle) — take if a 2025 CDN/JR PDF still live and unmined; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads "
            "(old VZW 0443.049.478 CDN 2026-00325874 is a different Tielt-Winge entity); "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB PIH / APB Inovant / APB Atlas listed or leftover but provincieantwerpen.be 403 — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1383 after Imewo leftover energy IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1383", rq_new, rq_spawn)
    print("research_queue 1383", found, "spawned_1384", spawned)

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
                "last_unit_id": "rq_1383",
                "ticks_completed": "1383",
                "paused": "no",
                "notes": (
                    "tick1383 Imewo leftover IGS energy residual; KBO 0215.362.368; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 3069003579 omzet 544911033 diensten 185219326 debt 2293851040 pnl 42031854 equity 772545254 dividend 17418700; "
                    "FOI ready omzet geo empty/94.2m 74/185.2m 61/2.29bn debt/17.42m div; next rq_1384 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    entry = """### Tick 1383 - 2026-08-19 - rq_1383 Imewo / Fluvius Imewo dual residual leftover
- Unit: Fluvius Imewo (voorheen Imewo / Intercommunale Maatschappij voor Energievoorziening in West- en Oost-Vlaanderen; leftover IGS opdrachthoudende vereniging / energy DSO elektriciteit + aardgas + openbare verlichting of 38 mined Oost- + West-Vlaanderen municipalities; werkmaatschappij Fluvius System Operator) after residual dual hunt (KBO **0215.362.368**; official over.fluvius.be has besluiten/governance + activiteitenverslag 2025 but no isolated statutory 2025 balans — live NBB WVV VOL-inb deposit **2026-00225268** PDF 1.61MB / 92p; AV **08.06.2026**; header **26.06.2026**; PDF created **30.06.2026**; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / Paul Eelen A02213 + Line Vyvey A02501 signed 26.03.2026 oordeel zonder voorbehoud assets 3.069.003.579 / PnL +42.031.854 + benadrukking VOL-inb 6.19 regulatoire saldi 2025-2028). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; preferred leftover other Fluvius DNB holdings this tick). Distinct from already-mined INTERGEM / Fluvius Midden-Vlaanderen 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 / Fluvius EG group-level (entity `fluvius`). First confirmed not already mined: no IMEWO / IMEA / IVEKA / GASELWEST / IVEG / imew JR2025 extract in entities/sources/leaderboard (only Kaprijke leasing-counterparty mention). KBO Actief / normale toestand since **10.03.1975**; statutaire naam FLUVIUS IMEWO since 01.01.2025; Opdrachthoudende vereniging (Vlaams Gewest) since 07.11.2003; zetel Brusselsesteenweg 199 9090 Merelbeke-Melle since 01.01.2025; **0 VE**; KBO no email/web/tel; official site https://over.fluvius.be/; btw since 01.10.1975; jaarvergadering mei; boekjaar 31 december; NACE 35.140/35.220/42.220/43.211/71.111/35.110/25.210. Absorbed Financieringsintercommunale West- en Oost-Vlaanderen 0252.903.744 (01.04.2018). Voorzitter Joris Vandenbroucke since 17.03.2025; ondervoorzitter Rutger De Reu; commissaris EY since 25.06.2025 tot 25.06.2028. Hunt leftover AGB/zorg/EVA first: leftover AGB Mechelen/Kortrijk/Brugge/Roeselare/Oostende 404/403 as of 1375 — not re-probed once live Imewo extracted; Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live Imewo extracted; IVAREM still 2024; leftover APB provincieantwerpen.be 403. Imewo statutory CDN live this tick (HTTP 200 / 1609492 / 92p) — taken (preferred leftover energy IGS of mined Oost- + West-Vlaanderen municipalities outside Nuhma; listed leftover-next after INTERGEM 1382). INTERGEM already mined 1382 — skipped. INTERZA already mined 1381 — skipped. INCOVO already mined 1380 — skipped. ISVAG already mined 1379 — skipped. De Nekker already mined 1378 — skipped. MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 already mined — skipped. Fluvius EG group already mined — this is a different legal person (DSO holding). Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. Other Fluvius DNB holdings (Kempen / West / Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle) leftover next. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366. Not every-10 (next 1390).
- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud assets 3.069.003.579 / PnL +42.031.854 + benadrukking 6.19; VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.8/6.12/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62/9087 empty): assets **3.069.003.579** (was 2.719.289.174); fixed **2.802.706.299** / MVA **2.643.277.966** (gebouwen **64.688.429**; machines **2.248.143.242**; meubilair **15.015.356**; leasing **12.160.746**; overige **716.673**; CIP **302.553.520** aanschaf **307.690.209**); IVA 21.028.817; FVA **138.399.516** (deelnemingen **32.872.626** FSO 18,57%; andere aandelen **105.526.891** aanschaf **3.544.247**); current **266.297.280**; LT recv 7.252.565; WIP 10.613.583; ST recv **176.069.219** (trade 87.251.277 + other 88.817.942); beleggingen empty; cash **993** vs 1.503; prepaid **72.360.920** (VNR 28.405.832 / REG 14.833.223 / pens 14.430.250 / verbruiken 13.560.300); equity **772.545.254** (inbreng 359.573.487; reval 154.851.529; reserves 190.084.800; overgedragen 67.496.612; capsub 538.826); voorzieningen **2.607.285** (milieu 2.114.765; pens 160 empty); schulden **2.293.851.040** (LT **1.925.545.654** waarvan bank **1.823.111.037** + lease 11.907.348 + other 90.527.269 JUMP; ST **299.480.941** waarvan LT-due 161.070.183 + leveranciers **87.060.409 JUMP** vs 18.255.146; related-party FSO-seam **1.604.090.869**); omzet **544.911.033 JUMP** vs 426.186.254 (elek **432.036.280** / gas **107.256.781** / other **5.617.972**; geo empty); othops **94.181.775** (740 empty); goods **217.679.821**; diensten **185.219.326** vs 179.219.682; pers **empty / 0 VTE**; afschr 113.031.011; expl **+97.045.759** vs +59.793.931; fin opbr 13.458.279; fin kosten 55.747.090; tax 12.746.249; PnL **+42.031.854** vs +19.630.098; dividend **17.418.700 DROP** vs 28.332.698; bruto capex jaarverslag **184.060.000**; commissaris 12.378 + extra 62.485; bestuurders 31.867. Jaarverslag same PDF: 38 vennoten; WACC/kapitaalkost 5,2% vs 3,5%; nettarief gezin elek **478** vs 357 / gas **277** vs 260; structuurwijzigingen 01.01.2025 add Zelzate (van Fluvius Antwerpen) / Jabbeke (van Fluvius West) / De Haan + Nazareth (van Gaselwest).
- CSVs: sources+4/entities+1/budgets+80/commitments+1/leaderboard+1 + FOI ready `gap_imew_omzet_544_91m_diensten_185_22m_debt_2_29bn_l5` (not sent); rq_1383=done; spawn rq_1384; ticks=1383.
- Coverage: residual dual L5 (Imewo leftover energy IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs Fluvius EG possible. No progress refresh (not every-10; next 1390).
- Next: rq_1384 residual dual L5 VL JR2025 hole_fill (prefer leftover other Fluvius DNB holdings Kempen-Iveka / West-Gaselwest / Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle if a 2025 CDN/JR PDF still live and unmined; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS CDN 2026-00254280 / Rematics / Sunfin only if taken after leftover IGS/EVA/AGB; leftover APB POA / TPA / De Schorre / Warande / PIH / Inovant / Atlas only if a real PDF downloads; IVAREM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1383 write done")


if __name__ == "__main__":
    main()

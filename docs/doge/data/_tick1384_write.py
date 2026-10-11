# -*- coding: utf-8 -*-
"""Tick 1384 — leftover Fluvius Kempen JR2025 official NBB WVV euros.
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

TICK = "1384"
UTC = "2026-08-19T03:10:00Z"
ENT = "igs_flkp"
HIER = "Vlaanderen>AntwerpenKempen>IGS>FluviusKempen"
GAP = "gap_flkp_omzet_221_58m_diensten_63_61m_debt_858_89m_l5"
SRC = "src_flkp_jr2025_nbb"
SRC2 = "src_flkp_site"
SRC3 = "src_kbo_flkp_0222030426"
SRC4 = "src_flkp_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00228440.pdf"
SRC2_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-kempen/overzichtslijst-besluiten"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0222030426"
SRC4_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-kempen/overzichtslijst-besluiten"
FOI_EMAIL = ""
FOI_POSTAL = "Koningin Elisabethlei 38 2300 Turnhout"
DRAFT = "docs/doge/foi/drafts/gap_flkp_omzet_221_58m_diensten_63_61m_debt_858_89m_l5.md"
COMM = "comm_flkp_jr2025_pnl"
LB = "lb_flkp_omzet_221_58m_diensten_63_61m_debt_858_89m"
VENNOTEN = (
    "Arendonk + Baarle-Hertog + Balen + Beerse + Dessel + Essen + Geel + "
    "Herentals + Herenthout + Hoogstraten + Kalmthout + Kasterlee + Lille + "
    "Meerhout + Merksplas + Mol + Olen + Oud-Turnhout + Ravels + Retie + "
    "Rijkevorsel + Turnhout + Vorselaar + Vosselaar + Westerlo + Wuustwezel + "
    "Zandhoven"
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
                "title": "Fluvius Kempen (voorheen Iveka) jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00228440; AV 22.06.2026)",
                "url": SRC_URL,
                "publisher": "Fluvius Kempen / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1384; official NBB VOL-inb PDF 1.87MB 91p deposit 2026-00228440 header 26.06.2026; "
                    "leftover IGS energy DSO of 27 Kempen + noord-Antwerpen municipalities (voorheen Iveka); "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / "
                    "Paul Eelen A02213 + Line Vyvey A02501 oordeel zonder voorbehoud assets 1158693922 / PnL 9895346 + benadrukking 6.19 regulatoire saldi; "
                    "VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.8/6.12/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62 empty"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Fluvius Kempen official governance page (leftover IGS energy DSO; voorheen Iveka; 27 Kempen + noord-Antwerpen vennoten)",
                "url": SRC2_URL,
                "publisher": "Fluvius / Fluvius Kempen",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1384; leftover IGS of 27 Kempen + noord-Antwerpen municipalities; "
                    "over.fluvius.be lists besluiten + jaarverslag 2025 PDF; statutory 2025 balans is the NBB CDN deposit; "
                    "naamswijziging Iveka -> Fluvius Kempen 01.01.2025; AV 22.06.2026"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Fluvius Kempen 0222.030.426",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1384; KBO 0222.030.426 Actief / normale toestand since 24.11.1981; "
                    "statutaire naam FLUVIUS KEMPEN since 01.01.2025; "
                    "Opdrachthoudende vereniging (Vlaams Gewest) since 05.11.2003; "
                    "zetel Koningin Elisabethlei 38 2300 Turnhout since 17.12.2007; 0 VE; "
                    "no KBO email/web/tel; btw since 01.01.1982; "
                    "boekjaar 31 december; NACE 35.140/35.220/43.211/71.111/25.210; "
                    "absorbed Intercommunale Gasvoorziening van Antwerpen en Omgeving 0204.889.734 (01.01.2009)"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Fluvius Kempen FOI channel / official governance + secretariaat (KBO no email)",
                "url": SRC4_URL,
                "publisher": "Fluvius Kempen",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1384; KBO no email/web/tel; zetel/secretariaat Koningin Elisabethlei 38 2300 Turnhout; "
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
                "name_nl": "Fluvius Kempen (voorheen Iveka; leftover IGS energy DSO Kempen + noord-Antwerpen)",
                "name_fr": "Fluvius Kempen (ex-Iveka; IGS residuel DSO energie Campine et nord d'Anvers)",
                "name_en": "Fluvius Kempen leftover IGS energy DSO (formerly Iveka)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1384 leftover residual IGS energy DSO of 27 Kempen + noord-Antwerpen municipalities; "
                    "KBO 0222.030.426 Actief since 24.11.1981; naam Iveka until 01.01.2025; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 1158693922 omzet 221584650 diensten 63605834 debt 858885051 pnl 9895346 equity 298568709 dividend 4096381; "
                    "FOI ready omzet geo empty / 31.4m 74 empty 740 / 63.6m 61 / 858.89m debt / 4.10m dividend; "
                    "distinct from already-mined Fluvius EG group entity fluvius and Imewo 1383 / INTERGEM 1382"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_flkp_assets_2025", ENT, "2025", "1158693922", "2025 assets 1158693922 VOL-inb 20/58; tick1384; primary official NBB WVV; commissaris 1158693922"),
        ("bud_flkp_assets_2024", ENT, "2024", "1018212750", "2024 assets 1018212750 comparative; tick1384; primary official NBB WVV 20/58"),
        ("bud_flkp_fixed_2025", ENT, "2025", "891071207", "2025 vaste activa 891071207 vs 804681117; tick1384; primary official NBB WVV 21/28"),
        ("bud_flkp_iva_2025", ENT, "2025", "7831912", "2025 IVA 7831912 vs 7358648; tick1384; primary official NBB WVV 21"),
        ("bud_flkp_iva_acq_2025", ENT, "2025", "4877698", "2025 IVA aanschaf 4877698 (8021); tick1384; primary official NBB WVV 6.2.1"),
        ("bud_flkp_mva_2025", ENT, "2025", "871318367", "2025 MVA 871318367 vs 788369698; tick1384; primary official NBB WVV 22/27"),
        ("bud_flkp_buildings_2025", ENT, "2025", "17270751", "2025 terreinen/gebouwen 17270751 vs 16231560; tick1384; primary official NBB WVV 22"),
        ("bud_flkp_machines_2025", ENT, "2025", "781420189", "2025 installaties/machines 781420189 vs 697718419; tick1384; primary official NBB WVV 23"),
        ("bud_flkp_machines_acq_2025", ENT, "2025", "82489346", "2025 machines aanschaf 82489346 (8162); tick1384; primary official NBB WVV 6.3"),
        ("bud_flkp_furniture_2025", ENT, "2025", "4443593", "2025 meubilair/rollend 4443593 vs 3761882; tick1384; primary official NBB WVV 24"),
        ("bud_flkp_lease_mva_2025", ENT, "2025", "6308109", "2025 leasing MVA 6308109 vs 5215176; tick1384; primary official NBB WVV 25"),
        ("bud_flkp_other_mva_2025", ENT, "2025", "1309607", "2025 overige MVA 1309607 vs 66625; tick1384; primary official NBB WVV 26"),
        ("bud_flkp_cip_2025", ENT, "2025", "60566118", "2025 CIP 60566118 vs 65376036; aanschaf 93235956; tick1384; primary official NBB WVV 27"),
        ("bud_flkp_cip_acq_2025", ENT, "2025", "93235956", "2025 CIP aanschaf 93235956 (8166); tick1384; primary official NBB WVV 6.3.6"),
        ("bud_flkp_fva_2025", ENT, "2025", "11920929", "2025 FVA 11920929 vs 8952772; tick1384; primary official NBB WVV 28"),
        ("bud_flkp_fva_part_2025", ENT, "2025", "9158569", "2025 deelnemingen 9158569 (FSO ~6.15-6.26pct); tick1384; primary official NBB WVV 282"),
        ("bud_flkp_fva_shares_2025", ENT, "2025", "2762360", "2025 andere aandelen 2762360 vs 471977 after aanschaf 2290383; tick1384; primary official NBB WVV 284"),
        ("bud_flkp_fva_acq_2025", ENT, "2025", "2290383", "2025 FVA andere aandelen aanschaf 2290383; tick1384; primary official NBB WVV 6.4.3 8363"),
        ("bud_flkp_current_2025", ENT, "2025", "267622715", "2025 vlottende activa 267622715 vs 213531633; tick1384; primary official NBB WVV 29/58"),
        ("bud_flkp_ltrecv_2025", ENT, "2025", "20013635", "2025 LT vorderingen 20013635 vs 20875949 (all other 291); tick1384; primary official NBB WVV 29"),
        ("bud_flkp_wip_2025", ENT, "2025", "1206037", "2025 bestellingen in uitvoering 1206037 vs 1899475; tick1384; primary official NBB WVV 37"),
        ("bud_flkp_strecv_2025", ENT, "2025", "212306698", "2025 ST vorderingen 212306698 vs 161913412; tick1384; primary official NBB WVV 40/41"),
        ("bud_flkp_trade_2025", ENT, "2025", "34210140", "2025 handelsvorderingen 34210140 vs 24966292; tick1384; primary official NBB WVV 40"),
        ("bud_flkp_othrecv_2025", ENT, "2025", "178096558", "2025 overige ST vorderingen 178096558 vs 136947120; tick1384; primary official NBB WVV 41"),
        ("bud_flkp_cash_2025", ENT, "2025", "993", "2025 liquide middelen 993 vs 1442 (near-zero vs 858.89m debt); tick1384; primary official NBB WVV 54/58"),
        ("bud_flkp_prepaid_2025", ENT, "2025", "34095353", "2025 overlopend actief 34095353 vs 28841355; tick1384; primary official NBB WVV 490/1"),
        ("bud_flkp_equity_2025", ENT, "2025", "298568709", "2025 eigen vermogen 298568709 vs 265586351; tick1384; primary official NBB WVV 10/15"),
        ("bud_flkp_equity_2024", ENT, "2024", "265586351", "2024 eigen vermogen 265586351 comparative; tick1384; primary official NBB WVV 10/15"),
        ("bud_flkp_inbreng_2025", ENT, "2025", "141536617", "2025 inbreng beschikbaar 141536617 vs 127294717; tick1384; primary official NBB WVV 10/11"),
        ("bud_flkp_reval_2025", ENT, "2025", "53337817", "2025 herwaarderingsmeerwaarden 53337817 vs 51008882; tick1384; primary official NBB WVV 12"),
        ("bud_flkp_reserves_2025", ENT, "2025", "80970389", "2025 reserves 80970389 (onbeschikbaar 30354419 + belastingvrij 2495999 + beschikbaar 48119971); tick1384; primary official NBB WVV 13"),
        ("bud_flkp_retained_2025", ENT, "2025", "22158857", "2025 overgedragen winst 22158857 vs 14575134; tick1384; primary official NBB WVV 14"),
        ("bud_flkp_capsub_2025", ENT, "2025", "565029", "2025 kapitaalsubsidies 565029 vs 594661; tick1384; primary official NBB WVV 15"),
        ("bud_flkp_prov_2025", ENT, "2025", "1240163", "2025 voorzieningen+latenties 1240163 (milieu 775738 + uitgesteld 464425); pens 160 empty; tick1384; primary official NBB WVV 16"),
        ("bud_flkp_env_2025", ENT, "2025", "775738", "2025 milieuvoorziening 775738; tick1384; primary official NBB WVV 163"),
        ("bud_flkp_debt_2025", ENT, "2025", "858885051", "2025 schulden 858885051 vs 751550754; tick1384; primary official NBB WVV 17/49"),
        ("bud_flkp_debt_2024", ENT, "2024", "751550754", "2024 schulden 751550754 comparative; tick1384; primary official NBB WVV 17/49"),
        ("bud_flkp_lt_2025", ENT, "2025", "702318476", "2025 LT schulden 702318476 vs 649791693 (all financial); tick1384; primary official NBB WVV 17"),
        ("bud_flkp_ltbank_2025", ENT, "2025", "660956601", "2025 LT kredietinstellingen 660956601 vs 640540963; tick1384; primary official NBB WVV 173"),
        ("bud_flkp_ltlease_2025", ENT, "2025", "6154489", "2025 LT leasing 6154489 vs 5080730; tick1384; primary official NBB WVV 172"),
        ("bud_flkp_ltother_2025", ENT, "2025", "35207386", "2025 LT overige leningen 35207386 JUMP vs 4170000; tick1384; primary official NBB WVV 174"),
        ("bud_flkp_st_2025", ENT, "2025", "142047835", "2025 ST schulden 142047835 vs 90803340; tick1384; primary official NBB WVV 42/48"),
        ("bud_flkp_st_due_2025", ENT, "2025", "68911555", "2025 LT-due within year 68911555 vs 38692317; tick1384; primary official NBB WVV 42"),
        ("bud_flkp_sttrade_2025", ENT, "2025", "37360612", "2025 leveranciers 37360612 JUMP vs 9258827; tick1384; primary official NBB WVV 440/4"),
        ("bud_flkp_stadv_2025", ENT, "2025", "7723280", "2025 vooruitbetalingen 7723280 vs 7179719; tick1384; primary official NBB WVV 46"),
        ("bud_flkp_sttax_2025", ENT, "2025", "4073749", "2025 tax ST 4073749 vs 3248772 (soc empty); tick1384; primary official NBB WVV 45"),
        ("bud_flkp_stother_2025", ENT, "2025", "23978639", "2025 overige ST 23978639 vs 32423705; tick1384; primary official NBB WVV 47/48"),
        ("bud_flkp_accrued_2025", ENT, "2025", "14518740", "2025 overlopend passief 14518740 vs 10955721; tick1384; primary official NBB WVV 492/3"),
        ("bud_flkp_reldebt_2025", ENT, "2025", "616255953", "2025 related-party debt 616255953 (LT 527561762 / ST 88694191; FSO-seam 6.15); tick1384; primary official NBB WVV 6.15 9352"),
        ("bud_flkp_opsinc_2025", ENT, "2025", "252255596", "2025 bedrijfsopbrengsten 252255596 vs 215633984; tick1384; primary official NBB WVV 70/76A"),
        ("bud_flkp_omzet_2025", ENT, "2025", "221584650", "2025 omzet 221584650 JUMP vs 176218575; 6.10 geo empty; tick1384; primary official NBB WVV 70"),
        ("bud_flkp_omzet_2024", ENT, "2024", "176218575", "2024 omzet 176218575 comparative; tick1384; primary official NBB WVV 70"),
        ("bud_flkp_omzet_elec_2025", ENT, "2025", "181922166", "2025 omzet elektriciteit 181922166 vs 135331632; tick1384; primary official NBB WVV 6.10"),
        ("bud_flkp_omzet_gas_2025", ENT, "2025", "37495810", "2025 omzet gas 37495810 vs 39653864; tick1384; primary official NBB WVV 6.10"),
        ("bud_flkp_omzet_other_2025", ENT, "2025", "2166674", "2025 omzet overige 2166674 vs 1233079; tick1384; primary official NBB WVV 6.10"),
        ("bud_flkp_othops_2025", ENT, "2025", "31369554", "2025 andere bedrijfsopbrengsten 31369554 vs 38033324; 740 empty; tick1384; primary official NBB WVV 74"),
        ("bud_flkp_opscost_2025", ENT, "2025", "219209763", "2025 bedrijfskosten 219209763 vs 195432565; tick1384; primary official NBB WVV 60/66A"),
        ("bud_flkp_goods_2025", ENT, "2025", "105274030", "2025 handelsgoederen 105274030 vs 87095597; tick1384; primary official NBB WVV 60"),
        ("bud_flkp_diensten_2025", ENT, "2025", "63605834", "2025 diensten 63605834 vs 64209027; no split; FSO pass-through; tick1384; primary official NBB WVV 61"),
        ("bud_flkp_diensten_2024", ENT, "2024", "64209027", "2024 diensten 64209027 comparative; tick1384; primary official NBB WVV 61"),
        ("bud_flkp_pers_2025", ENT, "2025", "0", "2025 bezoldigingen 62 empty / 9087 empty / 0 VTE (werkmaatschappij FSO); tick1384; primary official NBB WVV 62"),
        ("bud_flkp_deprec_2025", ENT, "2025", "41646213", "2025 afschrijvingen 41646213 vs 37444372; tick1384; primary official NBB WVV 630"),
        ("bud_flkp_othcost_2025", ENT, "2025", "9053288", "2025 andere bedrijfskosten 9053288 (tax 183564 + other 8869724); tick1384; primary official NBB WVV 640/8"),
        ("bud_flkp_expl_2025", ENT, "2025", "33045833", "2025 bedrijfswinst 33045833 vs 20201419; tick1384; primary official NBB WVV 9901"),
        ("bud_flkp_expl_2024", ENT, "2024", "20201419", "2024 bedrijfswinst 20201419 comparative; tick1384; primary official NBB WVV 9901"),
        ("bud_flkp_fininc_2025", ENT, "2025", "1364299", "2025 financiele opbrengsten 1364299 vs 1174690 (FVA 163904 + vlottende 1188254); tick1384; primary official NBB WVV 75"),
        ("bud_flkp_fincost_2025", ENT, "2025", "20202168", "2025 financiele kosten 20202168 vs 17459462 (schulden 20201067); tick1384; primary official NBB WVV 65"),
        ("bud_flkp_tax_2025", ENT, "2025", "4318938", "2025 belastingen 4318938 vs 1403701; tick1384; primary official NBB WVV 67/77"),
        ("bud_flkp_pnl_2025", ENT, "2025", "9895346", "2025 PnL 9904 9895346 vs 2518556; commissaris 9895346; tick1384; primary official NBB WVV"),
        ("bud_flkp_pnl_2024", ENT, "2024", "2518556", "2024 PnL 2518556 comparative; tick1384; primary official NBB WVV 9904"),
        ("bud_flkp_alloc_2025", ENT, "2025", "9902222", "2025 te bestemmen 9905 9902222 vs 2525047; tick1384; primary official NBB WVV 9905"),
        ("bud_flkp_div_2025", ENT, "2025", "4096381", "2025 dividend/vergoeding inbreng 4096381 DROP vs 9288892; tick1384; primary official NBB WVV 694"),
        ("bud_flkp_div_2024", ENT, "2024", "9288892", "2024 dividend 9288892 comparative; tick1384; primary official NBB WVV 694"),
        ("bud_flkp_capex_2025", ENT, "2025", "110737000", "2025 gerealiseerd bruto investeringsbudget 110737000 (jaarverslag duizenden); tick1384; primary official NBB WVV jaarverslag"),
        ("bud_flkp_comm_2025", ENT, "2025", "12378", "2025 commissaris EY 12378 + extra controle 24596 + taxadvies verbonden 4904; tick1384; primary official NBB WVV 9505"),
        ("bud_flkp_comm_extra_2025", ENT, "2025", "24596", "2025 commissaris andere controleopdrachten 24596; tick1384; primary official NBB WVV 95061"),
        ("bud_flkp_board_2025", ENT, "2025", "31767", "2025 bestuurders 9503 31767; tick1384; primary official NBB WVV 9503"),
        ("bud_flkp_tariff_elec_2025", ENT, "2025", "484", "2025 nettarief elek gezin digitale meter 484 EUR incl btw vs 364; tick1384; primary official NBB WVV jaarverslag"),
        ("bud_flkp_tariff_gas_2025", ENT, "2025", "242", "2025 nettarief gas gezin 242 EUR incl btw vs 224; tick1384; primary official NBB WVV jaarverslag"),
        ("bud_flkp_pens_fso_2025", ENT, "2025", "5898739", "2025 off-balance FSO contractueel pensioen aandeel 5898738.93 + statutair Fluvius OV 781000; tick1384; primary official NBB WVV 6.20"),
        ("bud_flkp_shares_nb_2025", ENT, "2025", "11220266", "2025 aandelen netbeheer+neven 11220266 + Aov 853942; tick1384; primary official NBB WVV jaarverslag"),
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
                "title": "Fluvius Kempen JR2025 leftover IGS dual (assets 1.16bn / omzet 221.58m / diensten 63.61m / debt 858.89m / dividend 4.10m)",
                "entity_id": ENT,
                "beneficiary": "Fluvius Kempen / " + VENNOTEN,
                "legal_basis": "WVV OV; Decreet Lokaal Bestuur; Energiedecreet; NBB neerlegging",
                "decision_date": "2026-06-22",
                "start_year": "1981",
                "end_year": "",
                "total_envelope_eur": "1158693922",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL energy DSO — 221.58m omzet (geo empty) / 63.61m diensten / 858.89m debt / 4.10m dividend",
                "cut_option": "Publish unpublished omzet geo + 31.4m 74 + 63.6m 61 FSO pass-through + 858.89m debt counterparties + 4.10m dividend per vennoot; do not keep DSO IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1384; assets 1158693922 omzet 221584650 diensten 63605834 debt 858885051 pnl 9895346 equity 298568709 dividend 4096381; FOI ready not sent; not TE-additive of 348bn; double_count vs Fluvius EG possible",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Fluvius Kempen JR2025 leftover IGS: assets 1.16bn / omzet 221.58m / diensten 63.61m / debt 858.89m / dividend 4.10m / 0 VTE",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "63605834",
                "total_cost_eur": "1158693922",
                "tco_notes": (
                    "Leftover dual IGS energy DSO of 27 Kempen + noord-Antwerpen municipalities (voorheen Iveka): "
                    "assets 1.16bn / equity 298.6m / pnl +9.90m / omzet 221.58m (geo empty) / "
                    "diensten 63.61m / 0 VTE / debt 858.89m (related 616.26m) / dividend 4.10m / cash 993; "
                    "official NBB WVV live; do not treat 1.16bn as TE-additive of 348bn; double_count vs Fluvius EG possible"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Fluvius Kempen / " + VENNOTEN,
                "stated_goal": "Local leftover IGS map VL energy DSO — JR2025 live; dual omzet-geo/diensten/debt/dividend FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 1.16bn / omzet 221.58m / diensten 63.61m / debt 858.89m / dividend 4.10m / pnl +9.90m / 0 VTE",
                "absurdity_score": "7.2",
                "cost_score": "8.6",
                "difficulty": "3.0",
                "priority_index": "7.5",
                "cut_proposal": "Publish unpublished omzet geo + 31.4m 74 + 63.6m 61 FSO pass-through + 858.89m debt counterparties + 4.10m dividend per vennoot; do not keep DSO IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1384; leftover IGS of 27 Kempen + noord-Antwerpen municipalities; FOI ready not sent; not TE-additive of 348bn; distinct from Fluvius EG and Imewo 1383 / INTERGEM 1382",
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
                    "omzet 221584650 JUMP vs 176218575 (WVV 70; 6.10 category elek 181922166 / gas 37495810 / other 2166674; geo empty) per vennoot/tariefstroom unpublished "
                    "+ andere bedrijfsopbrengsten 31369554 (WVV 74; 740 empty) "
                    "+ diensten 63605834 vs 64209027 (WVV 61; no split) + goods 105274030 + FSO pass-through (pers 62/9087 empty / 0 VTE) "
                    "+ schulden 858885051 (LT bank 660956601; related-party 616255953) counterparties/rente unpublished "
                    "+ FVA other shares 2762360 after aanschaf 2290383 unpublished "
                    "+ dividend 4096381 DROP vs 9288892 per vennoot unpublished "
                    "+ cash 993 vs debt 858.89m + prepaid 34095353 + VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.8/6.12/6.18/9 not filed"
                ),
                "why_it_matters": (
                    "Leftover IGS OV energy DSO of 27 mined Kempen + noord-Antwerpen municipalities "
                    "(same leftover-IGS energy seam as Imewo 1383 / INTERGEM 1382; distinct from Fluvius EG): "
                    "1.16bn assets / 221.58m omzet / 63.61m diensten / 858.89m debt / 4.10m dividend / "
                    "0 VTE / FSO shell "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Fluvius Kempen / Raad van Bestuur / Guy Van de Perre / Nathalie Cuylaerts / 27 Kempen + noord-Antwerpen vennoten",
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
                    "tick1384 leftover IGS OV energy DSO of 27 Kempen + noord-Antwerpen municipalities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (1.87MB 91p deposit 2026-00228440). "
                    "Imewo already mined 1383 — skipped. INTERGEM already mined 1382 — skipped. INTERZA already mined 1381 — skipped. "
                    "INCOVO already mined 1380 — skipped. ISVAG already mined 1379 — skipped. De Nekker already mined 1378 — skipped. "
                    "MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. "
                    "Nuhma-group seam 1353-1365 skipped. Fluvius EG group already mined — this is a different legal person. "
                    "Other Fluvius DNB holdings (West / Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle) leftover next if CDN live. "
                    "Dommelhof leftover Limburg EVA 0777.495.085 not re-probed once live Kempen extracted. "
                    "IVAREM still 2024. Otary RS Nuhma-adjacent fallback not taken. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1384",
        "title": "Fluvius Kempen / Iveka JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Fluvius Kempen leftover IGS energy DSO of 27 Kempen + noord-Antwerpen municipalities after honest hunt; "
            "KBO 0222.030.426 Actief; live JR2025 official NBB WVV VOL-inb PDF (1.87MB 91p deposit 2026-00228440; commissaris EY); "
            "sourced euros assets 1158693922 / omzet 221584650 / diensten 63605834 / debt 858885051 / pnl 9895346 / dividend 4096381; "
            "FOI ready omzet geo empty / 31.4m 74 / 63.6m 61 / 858.89m debt / 4.10m dividend"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T02:45:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1384 Fluvius Kempen leftover IGS energy residual; KBO 0222.030.426; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1385 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1385",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1384 done including Fluvius Kempen 1384 leftover energy IGS live NBB WVV / "
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
            "other Fluvius DNB holdings leftover energy IGS (West-Gaselwest / Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle) — take if a 2025 CDN/JR PDF still live and unmined; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads "
            "(old VZW 0443.049.478 CDN 2026-00325874 is a different Tielt-Winge entity); "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB PIH / APB Inovant / APB Atlas listed or leftover but provincieantwerpen.be 403 — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1384 after Fluvius Kempen leftover energy IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1384", rq_new, rq_spawn)
    print("research_queue 1384", found, "spawned_1385", spawned)

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
                "last_unit_id": "rq_1384",
                "ticks_completed": "1384",
                "paused": "no",
                "notes": (
                    "tick1384 Fluvius Kempen leftover IGS energy residual; KBO 0222.030.426; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 1158693922 omzet 221584650 diensten 63605834 debt 858885051 pnl 9895346 equity 298568709 dividend 4096381; "
                    "FOI ready omzet geo empty/31.4m 74/63.6m 61/858.89m debt/4.10m div; next rq_1385 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    entry = """### Tick 1384 - 2026-08-19 - rq_1384 Fluvius Kempen / Iveka dual residual leftover
- Unit: Fluvius Kempen (voorheen Iveka / Intercommunale Vereniging Voor de Energiedistributie in de Kempen en het Antwerpse; leftover IGS opdrachthoudende vereniging / energy DSO elektriciteit + aardgas + openbare verlichting + warmte of 27 mined Kempen + noord-Antwerpen municipalities; werkmaatschappij Fluvius System Operator) after residual dual hunt (KBO **0222.030.426**; official over.fluvius.be has besluiten/governance + jaarverslag 2025 PDF; live NBB WVV VOL-inb deposit **2026-00228440** PDF 1.87MB / 91p; AV **22.06.2026**; header **26.06.2026**; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / Paul Eelen A02213 + Line Vyvey A02501 signed 26.03.2026 oordeel zonder voorbehoud assets 1.158.693.922 / PnL +9.895.346 + benadrukking VOL-inb 6.19 regulatoire saldi 2025-2028). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; preferred leftover other Fluvius DNB holdings this tick). Distinct from already-mined Fluvius Imewo 1383 / INTERGEM / Fluvius Midden-Vlaanderen 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 / Fluvius EG group-level (entity `fluvius`). First confirmed not already mined: no Fluvius Kempen / IVEKA / 0222.030.426 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **24.11.1981**; statutaire naam FLUVIUS KEMPEN since 01.01.2025; Opdrachthoudende vereniging (Vlaams Gewest) since 05.11.2003; zetel Koningin Elisabethlei 38 2300 Turnhout since 17.12.2007; **0 VE**; KBO no email/web/tel; official site https://over.fluvius.be/; btw since 01.01.1982; boekjaar 31 december; NACE 35.140/35.220/43.211/71.111/25.210. Absorbed Intercommunale Gasvoorziening van Antwerpen en Omgeving 0204.889.734 (01.01.2009). Voorzitter Guy Van de Perre; ondervoorzitter Nathalie Cuylaerts; commissaris EY since 17.06.2025 tot 17.06.2028. Hunt leftover AGB/zorg/EVA first: leftover AGB Mechelen/Kortrijk/Brugge/Roeselare/Oostende 404/403 as of 1375 — not re-probed once live Kempen extracted; Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live Kempen extracted; IVAREM still 2024; leftover APB provincieantwerpen.be 403. Fluvius Kempen statutory CDN live this tick (HTTP 200 / 1866952 / 91p) — taken (preferred leftover energy IGS of mined Kempen municipalities outside Nuhma; listed leftover-next after Imewo 1383). Imewo already mined 1383 — skipped. INTERGEM already mined 1382 — skipped. INTERZA already mined 1381 — skipped. INCOVO already mined 1380 — skipped. ISVAG already mined 1379 — skipped. De Nekker already mined 1378 — skipped. MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 already mined — skipped. Fluvius EG group already mined — this is a different legal person (DSO holding). Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. Other Fluvius DNB holdings (West / Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle) leftover next. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366. Not every-10 (next 1390).
- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud assets 1.158.693.922 / PnL +9.895.346 + benadrukking 6.19; VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.8/6.12/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62/9087 empty): assets **1.158.693.922** (was 1.018.212.750); fixed **891.071.207** / MVA **871.318.367** (gebouwen **17.270.751**; machines **781.420.189**; meubilair **4.443.593**; leasing **6.308.109**; overige **1.309.607**; CIP **60.566.118** aanschaf **93.235.956**); IVA 7.831.912; FVA **11.920.929** (deelnemingen **9.158.569** FSO ~6,15-6,26%; andere aandelen **2.762.360** aanschaf **2.290.383**); current **267.622.715**; LT recv 20.013.635; WIP 1.206.037; ST recv **212.306.698** (trade 34.210.140 + other 178.096.558); beleggingen empty; cash **993** vs 1.442; prepaid **34.095.353**; equity **298.568.709** (inbreng 141.536.617; reval 53.337.817; reserves 80.970.389; overgedragen 22.158.857; capsub 565.029); voorzieningen **1.240.163** (milieu 775.738; pens 160 empty); schulden **858.885.051** (LT **702.318.476** waarvan bank **660.956.601** + lease 6.154.489 + other 35.207.386 JUMP; ST **142.047.835** waarvan LT-due 68.911.555 + leveranciers **37.360.612 JUMP** vs 9.258.827; related-party FSO-seam **616.255.953**); omzet **221.584.650 JUMP** vs 176.218.575 (elek **181.922.166** / gas **37.495.810** / other **2.166.674**; geo empty); othops **31.369.554** (740 empty); goods **105.274.030**; diensten **63.605.834** vs 64.209.027; pers **empty / 0 VTE**; afschr 41.646.213; expl **+33.045.833** vs +20.201.419; fin opbr 1.364.299; fin kosten 20.202.168; tax 4.318.938; PnL **+9.895.346** vs +2.518.556; dividend **4.096.381 DROP** vs 9.288.892; bruto capex jaarverslag **110.737.000**; commissaris 12.378 + extra 24.596; bestuurders 31.767. Jaarverslag same deposit + over.fluvius.be PDF: 27 vennoten; WACC/kapitaalkost 5,2% vs 3,5%; nettarief gezin elek **484** vs 364 / gas **242** vs 224; naamswijziging Iveka -> Fluvius Kempen 01.01.2025; FSO stemaandeel 6,08%.
- CSVs: sources+4/entities+1/budgets+81/commitments+1/leaderboard+1 + FOI ready `gap_flkp_omzet_221_58m_diensten_63_61m_debt_858_89m_l5` (not sent); rq_1384=done; spawn rq_1385; ticks=1384.
- Coverage: residual dual L5 (Fluvius Kempen leftover energy IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs Fluvius EG possible. No progress refresh (not every-10; next 1390).
- Next: rq_1385 residual dual L5 VL JR2025 hole_fill (prefer leftover other Fluvius DNB holdings West-Gaselwest / Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle if a 2025 CDN/JR PDF still live and unmined; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS CDN 2026-00254280 / Rematics / Sunfin only if taken after leftover IGS/EVA/AGB; leftover APB POA / TPA / De Schorre / Warande / PIH / Inovant / Atlas only if a real PDF downloads; IVAREM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1384 write done")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Tick 1386 — leftover Fluvius Antwerpen JR2025 official NBB WVV euros.
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

TICK = "1386"
UTC = "2026-08-19T04:20:00Z"
ENT = "igs_flan"
HIER = "Vlaanderen>Antwerpen>IGS>FluviusAntwerpen"
GAP = "gap_flan_omzet_430_93m_diensten_165_12m_debt_1_69bn_l5"
SRC = "src_flan_jr2025_nbb"
SRC2 = "src_flan_site"
SRC3 = "src_kbo_flan_0212704370"
SRC4 = "src_flan_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00228192.pdf"
SRC2_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-antwerpen/activiteitenverslagen"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0212704370"
SRC4_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-antwerpen"
FOI_EMAIL = ""
FOI_POSTAL = "Merksemsesteenweg 233 2100 Deurne (Antwerpen)"
DRAFT = "docs/doge/foi/drafts/gap_flan_omzet_430_93m_diensten_165_12m_debt_1_69bn_l5.md"
COMM = "comm_flan_jr2025_pnl"
LB = "lb_flan_omzet_430_93m_diensten_165_12m_debt_1_69bn"
VENNOTEN = (
    "Aartselaar + Antwerpen + Beveren-Kruibeke-Zwijndrecht + Boechout + "
    "Boom + Brasschaat + Brecht + Duffel + Edegem + Essen + Grobbendonk + "
    "Hemiksem + Hove + Kapellen + Kontich + Lier + Lille + Lint + Malle + "
    "Mortsel + Niel + Nijlen + Ranst + Rumst + Schelle + Schilde + Schoten + "
    "Stabroek + Wijnegem + Willebroek + Wommelgem + Zoersel"
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
                "title": "Fluvius Antwerpen (voorheen IMEA + Iveg + Integan) jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00228192; AV 17.06.2026)",
                "url": SRC_URL,
                "publisher": "Fluvius Antwerpen / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1386; official NBB VOL-inb PDF 1.94MB 97p deposit 2026-00228192 header 26.06.2026; "
                    "leftover IGS energy DSO of 32 Antwerp-area municipalities after IMEA+Iveg+Integan fusie 01.04.2019; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / "
                    "Paul Eelen + Line Vyvey oordeel zonder voorbehoud assets 2456270811 / te bestemmen 28526039 + benadrukking 6.19 regulatoire saldi; "
                    "VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62 empty"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Fluvius Antwerpen official governance + jaarverslag 2025 (leftover IGS energy DSO; voorheen IMEA + Iveg + Integan; 32 vennoten)",
                "url": SRC2_URL,
                "publisher": "Fluvius / Fluvius Antwerpen",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1386; leftover IGS of 32 Antwerp-area municipalities; "
                    "over.fluvius.be lists activiteitenverslagen + JR2025 PDF sites/fluvius/files/2026-06/fluvius-antwerpen-jaarverslag-2025.pdf; "
                    "statutory 2025 balans is the NBB CDN deposit; fusie IMEA+Iveg+Integan april 2019"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Fluvius Antwerpen 0212.704.370",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1386; KBO 0212.704.370 Actief / normale toestand since 24.11.1972; "
                    "statutaire naam FLUVIUS Antwerpen since 01.04.2019; "
                    "Opdrachthoudende vereniging (Vlaams Gewest) since 08.12.2003; "
                    "zetel Merksemsesteenweg 233 2100 Antwerpen since 01.01.2023; 0 VE; "
                    "no KBO email/web/tel; btw since 01.01.1973; "
                    "boekjaar 31 december; NACE 35.220/35.110/37.000; "
                    "absorbed VET 0219.943.441 (17.12.2003), IMEA 0204.647.234 (01.04.2019), Integan 0212.586.683 (01.04.2019)"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Fluvius Antwerpen FOI channel / official governance + secretariaat (KBO no email)",
                "url": SRC4_URL,
                "publisher": "Fluvius Antwerpen",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1386; KBO no email/web/tel; zetel Merksemsesteenweg 233 2100 Deurne; "
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
                "name_nl": "Fluvius Antwerpen (voorheen IMEA + Iveg + Integan; leftover IGS energy DSO Antwerpen)",
                "name_fr": "Fluvius Anvers (ex-IMEA + Iveg + Integan; IGS residuel DSO energie Anvers)",
                "name_en": "Fluvius Antwerpen leftover IGS energy DSO (formerly IMEA + Iveg + Integan)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1386 leftover residual IGS energy DSO of 32 Antwerp-area municipalities; "
                    "KBO 0212.704.370 Actief since 24.11.1972; naam Fluvius Antwerpen since 01.04.2019; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 2456270811 omzet 430933126 diensten 165123722 debt 1690066932 pnl 28512602 equity 755426317 dividend 20422377; "
                    "FOI ready omzet geo empty / 81.3m 74 empty 740 / 165.1m 61 / 1.69bn debt / 20.42m dividend; "
                    "distinct from already-mined Fluvius EG group entity fluvius and West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_flan_assets_2025", ENT, "2025", "2456270811", "2025 assets 2456270811 VOL-inb 20/58; tick1386; primary official NBB WVV; commissaris 2456270811"),
        ("bud_flan_assets_2024", ENT, "2024", "2295213508", "2024 assets 2295213508 comparative; tick1386; primary official NBB WVV 20/58"),
        ("bud_flan_fixed_2025", ENT, "2025", "2060199199", "2025 vaste activa 2060199199 vs 1993475353; tick1386; primary official NBB WVV 21/28"),
        ("bud_flan_iva_2025", ENT, "2025", "18422050", "2025 IVA 18422050 vs 18970011; tick1386; primary official NBB WVV 21"),
        ("bud_flan_iva_acq_2025", ENT, "2025", "8018986", "2025 IVA aanschaf 8018986 (8021); tick1386; primary official NBB WVV 6.2.1"),
        ("bud_flan_mva_2025", ENT, "2025", "1881193332", "2025 MVA 1881193332 vs 1810850758; tick1386; primary official NBB WVV 22/27"),
        ("bud_flan_buildings_2025", ENT, "2025", "43846411", "2025 terreinen/gebouwen 43846411 vs 43286882; tick1386; primary official NBB WVV 22"),
        ("bud_flan_machines_2025", ENT, "2025", "1557190339", "2025 installaties/machines 1557190339 vs 1518291582; tick1386; primary official NBB WVV 23"),
        ("bud_flan_machines_acq_2025", ENT, "2025", "29110606", "2025 machines aanschaf 29110606 (8162) + overboeking 180673212 from CIP; tick1386; primary official NBB WVV 6.3.2"),
        ("bud_flan_furniture_2025", ENT, "2025", "8354243", "2025 meubilair/rollend 8354243 vs 9081604; tick1386; primary official NBB WVV 24"),
        ("bud_flan_lease_mva_2025", ENT, "2025", "10451205", "2025 leasing MVA 10451205 vs 9792319; tick1386; primary official NBB WVV 25"),
        ("bud_flan_other_mva_2025", ENT, "2025", "1557466", "2025 overige MVA 1557466 vs 182505; tick1386; primary official NBB WVV 26"),
        ("bud_flan_cip_2025", ENT, "2025", "259793668", "2025 CIP 259793668 vs 230215867; aanschaf 218093174; tick1386; primary official NBB WVV 27"),
        ("bud_flan_cip_acq_2025", ENT, "2025", "218093174", "2025 CIP aanschaf 218093174 (8166); tick1386; primary official NBB WVV 6.3.6"),
        ("bud_flan_fva_2025", ENT, "2025", "160583817", "2025 FVA 160583817 vs 163654584; tick1386; primary official NBB WVV 28"),
        ("bud_flan_fva_part_2025", ENT, "2025", "100246306", "2025 deelnemingen 100246306 (FSO 15.7pct A / 26.23pct K-SYN / 12.91pct SYN); tick1386; primary official NBB WVV 282"),
        ("bud_flan_fva_shares_2025", ENT, "2025", "60212510", "2025 andere aandelen 60212510 vs 63077539; tick1386; primary official NBB WVV 284"),
        ("bud_flan_current_2025", ENT, "2025", "396071612", "2025 vlottende activa 396071612 vs 301738155; tick1386; primary official NBB WVV 29/58"),
        ("bud_flan_ltrecv_2025", ENT, "2025", "60885783", "2025 LT vorderingen 60885783 vs 2235044 (other 291 60651753); tick1386; primary official NBB WVV 29"),
        ("bud_flan_wip_2025", ENT, "2025", "14838054", "2025 bestellingen in uitvoering 14838054 vs 18103283; tick1386; primary official NBB WVV 37"),
        ("bud_flan_strecv_2025", ENT, "2025", "248927944", "2025 ST vorderingen 248927944 vs 209146948; tick1386; primary official NBB WVV 40/41"),
        ("bud_flan_trade_2025", ENT, "2025", "69882449", "2025 handelsvorderingen 69882449 vs 55513239; tick1386; primary official NBB WVV 40"),
        ("bud_flan_othrecv_2025", ENT, "2025", "179045495", "2025 overige ST vorderingen 179045495 vs 153633709; tick1386; primary official NBB WVV 41"),
        ("bud_flan_cash_2025", ENT, "2025", "1480", "2025 liquide middelen 1480 vs 2840 (near-zero vs 1.69bn debt); tick1386; primary official NBB WVV 54/58"),
        ("bud_flan_prepaid_2025", ENT, "2025", "71418351", "2025 overlopend actief 71418351 vs 72250041; tick1386; primary official NBB WVV 490/1"),
        ("bud_flan_prepaid_reg_2025", ENT, "2025", "25238887", "2025 regulatoire saldi gas in prepaid 25238887; tick1386; primary official NBB WVV 6.6"),
        ("bud_flan_equity_2025", ENT, "2025", "755426317", "2025 eigen vermogen 755426317 vs 777094458; tick1386; primary official NBB WVV 10/15"),
        ("bud_flan_equity_2024", ENT, "2024", "777094458", "2024 eigen vermogen 777094458 comparative; tick1386; primary official NBB WVV 10/15"),
        ("bud_flan_inbreng_2025", ENT, "2025", "404513783", "2025 inbreng beschikbaar 404513783 vs 426142075; tick1386; primary official NBB WVV 10/11"),
        ("bud_flan_reval_2025", ENT, "2025", "112617787", "2025 herwaarderingsmeerwaarden 112617787 vs 124783937; tick1386; primary official NBB WVV 12"),
        ("bud_flan_reserves_2025", ENT, "2025", "159221603", "2025 reserves 159221603 (onbeschikbaar 56511664 + belastingvrij 1540025 + beschikbaar 101169914); tick1386; primary official NBB WVV 13"),
        ("bud_flan_retained_2025", ENT, "2025", "64637195", "2025 overgedragen winst 64637195 vs 47900795; tick1386; primary official NBB WVV 14"),
        ("bud_flan_capsub_2025", ENT, "2025", "14435949", "2025 kapitaalsubsidies 14435949 vs 13437132; tick1386; primary official NBB WVV 15"),
        ("bud_flan_prov_2025", ENT, "2025", "10777562", "2025 voorzieningen+latenties 10777562 (milieu 420731 + overige 5530509 + uitgesteld 4826321); pens 160 empty; tick1386; primary official NBB WVV 16"),
        ("bud_flan_env_2025", ENT, "2025", "420731", "2025 milieuvoorziening 420731; tick1386; primary official NBB WVV 163"),
        ("bud_flan_debt_2025", ENT, "2025", "1690066932", "2025 schulden 1690066932 vs 1507480162; tick1386; primary official NBB WVV 17/49"),
        ("bud_flan_debt_2024", ENT, "2024", "1507480162", "2024 schulden 1507480162 comparative; tick1386; primary official NBB WVV 17/49"),
        ("bud_flan_lt_2025", ENT, "2025", "1399475389", "2025 LT schulden 1399475389 vs 1322907494 (all financial); tick1386; primary official NBB WVV 17"),
        ("bud_flan_ltbank_2025", ENT, "2025", "1357665997", "2025 LT kredietinstellingen 1357665997 vs 1280162548; tick1386; primary official NBB WVV 173"),
        ("bud_flan_ltlease_2025", ENT, "2025", "10228288", "2025 LT leasing 10228288 vs 9622892; tick1386; primary official NBB WVV 172"),
        ("bud_flan_ltother_2025", ENT, "2025", "31581103", "2025 LT overige leningen 31581103 vs 33122054; tick1386; primary official NBB WVV 174"),
        ("bud_flan_st_2025", ENT, "2025", "226589414", "2025 ST schulden 226589414 vs 146298202; tick1386; primary official NBB WVV 42/48"),
        ("bud_flan_st_due_2025", ENT, "2025", "103284536", "2025 LT-due within year 103284536 vs 70960569; tick1386; primary official NBB WVV 42"),
        ("bud_flan_sttrade_2025", ENT, "2025", "73040004", "2025 leveranciers 73040004 JUMP vs 21216849; tick1386; primary official NBB WVV 440/4"),
        ("bud_flan_stadv_2025", ENT, "2025", "16525557", "2025 vooruitbetalingen 16525557 vs 18275402; tick1386; primary official NBB WVV 46"),
        ("bud_flan_sttax_2025", ENT, "2025", "9032919", "2025 tax ST 9032919 vs 8804580 (soc empty); tick1386; primary official NBB WVV 45"),
        ("bud_flan_stother_2025", ENT, "2025", "24706398", "2025 overige ST 24706398 vs 27040801; tick1386; primary official NBB WVV 47/48"),
        ("bud_flan_accrued_2025", ENT, "2025", "64002129", "2025 overlopend passief 64002129 vs 38274466; tick1386; primary official NBB WVV 492/3"),
        ("bud_flan_reldebt_2025", ENT, "2025", "1184715297", "2025 related-party debt 1184715297 (LT 1084406622 / ST 100308675; FSO-seam 6.15); tick1386; primary official NBB WVV 6.15 9352"),
        ("bud_flan_opsinc_2025", ENT, "2025", "508743746", "2025 bedrijfsopbrengsten 508743746 vs 457374249; tick1386; primary official NBB WVV 70/76A"),
        ("bud_flan_omzet_2025", ENT, "2025", "430933126", "2025 omzet 430933126 JUMP vs 364038942; 6.10 geo empty; tick1386; primary official NBB WVV 70"),
        ("bud_flan_omzet_2024", ENT, "2024", "364038942", "2024 omzet 364038942 comparative; tick1386; primary official NBB WVV 70"),
        ("bud_flan_omzet_elec_2025", ENT, "2025", "325913485", "2025 omzet elektriciteit 325913485 vs 256520764; tick1386; primary official NBB WVV 6.10"),
        ("bud_flan_omzet_gas_2025", ENT, "2025", "92718616", "2025 omzet gas 92718616 vs 98562206; tick1386; primary official NBB WVV 6.10"),
        ("bud_flan_omzet_rio_2025", ENT, "2025", "3886574", "2025 omzet riolering 3886574 vs 3487837; tick1386; primary official NBB WVV 6.10"),
        ("bud_flan_omzet_heat_2025", ENT, "2025", "2364769", "2025 omzet warmte 2364769 vs 2632835; tick1386; primary official NBB WVV 6.10"),
        ("bud_flan_omzet_cable_2025", ENT, "2025", "230056", "2025 omzet kabeltelevisie 230056 vs 41358; tick1386; primary official NBB WVV 6.10"),
        ("bud_flan_omzet_other_2025", ENT, "2025", "5819627", "2025 omzet overige 5819627 vs 2793942; tick1386; primary official NBB WVV 6.10"),
        ("bud_flan_othops_2025", ENT, "2025", "81309426", "2025 andere bedrijfsopbrengsten 81309426 vs 79794888; 740 empty; tick1386; primary official NBB WVV 74"),
        ("bud_flan_opscost_2025", ENT, "2025", "445474075", "2025 bedrijfskosten 445474075 vs 427979579; tick1386; primary official NBB WVV 60/66A"),
        ("bud_flan_goods_2025", ENT, "2025", "172844254", "2025 handelsgoederen 172844254 vs 143037052; tick1386; primary official NBB WVV 60"),
        ("bud_flan_diensten_2025", ENT, "2025", "165123722", "2025 diensten 165123722 vs 177723856; no split; FSO pass-through; tick1386; primary official NBB WVV 61"),
        ("bud_flan_diensten_2024", ENT, "2024", "177723856", "2024 diensten 177723856 comparative; tick1386; primary official NBB WVV 61"),
        ("bud_flan_pers_2025", ENT, "2025", "0", "2025 bezoldigingen 62 empty / 9087 empty / 0 VTE (werkmaatschappij FSO); tick1386; primary official NBB WVV 62"),
        ("bud_flan_deprec_2025", ENT, "2025", "79818145", "2025 afschrijvingen 79818145 vs 78496059; tick1386; primary official NBB WVV 630"),
        ("bud_flan_othcost_2025", ENT, "2025", "24327298", "2025 andere bedrijfskosten 24327298 (tax 203852 + other 24123446); tick1386; primary official NBB WVV 640/8"),
        ("bud_flan_expl_2025", ENT, "2025", "63269671", "2025 bedrijfswinst 63269671 vs 29394670; tick1386; primary official NBB WVV 9901"),
        ("bud_flan_expl_2024", ENT, "2024", "29394670", "2024 bedrijfswinst 29394670 comparative; tick1386; primary official NBB WVV 9901"),
        ("bud_flan_fininc_2025", ENT, "2025", "13464943", "2025 financiele opbrengsten 13464943 vs 11840427 (FVA 9521197 + vlottende 3847544); tick1386; primary official NBB WVV 75"),
        ("bud_flan_fincost_2025", ENT, "2025", "39712360", "2025 financiele kosten 39712360 vs 34734458 (schulden 39592801); tick1386; primary official NBB WVV 65"),
        ("bud_flan_tax_2025", ENT, "2025", "8546124", "2025 belastingen 8546124 vs 1067515; tick1386; primary official NBB WVV 67/77"),
        ("bud_flan_pnl_2025", ENT, "2025", "28512602", "2025 PnL 9904 28512602 vs 5467394; commissaris quotes 9905 28526039; tick1386; primary official NBB WVV"),
        ("bud_flan_pnl_2024", ENT, "2024", "5467394", "2024 PnL 5467394 comparative; tick1386; primary official NBB WVV 9904"),
        ("bud_flan_alloc_2025", ENT, "2025", "28526039", "2025 te bestemmen 9905 28526039 vs 5480876; commissaris 28526039; tick1386; primary official NBB WVV 9905"),
        ("bud_flan_div_2025", ENT, "2025", "20422377", "2025 dividend/vergoeding inbreng 20422377 DROP vs 26522655; tick1386; primary official NBB WVV 694"),
        ("bud_flan_div_2024", ENT, "2024", "26522655", "2024 dividend 26522655 comparative; tick1386; primary official NBB WVV 694"),
        ("bud_flan_capex_2025", ENT, "2025", "253124000", "2025 gerealiseerd bruto investeringsbudget 253124000 (jaarverslag duizenden); tick1386; primary official NBB WVV jaarverslag"),
        ("bud_flan_comm_2025", ENT, "2025", "42558", "2025 commissaris EY 42558 + extra controle 28272 + taxadvies verbonden 13305; tick1386; primary official NBB WVV 9505"),
        ("bud_flan_comm_extra_2025", ENT, "2025", "28272", "2025 commissaris andere controleopdrachten 28272; tick1386; primary official NBB WVV 95061"),
        ("bud_flan_board_2025", ENT, "2025", "29237", "2025 bestuurders 9503 29237; tick1386; primary official NBB WVV 9503"),
        ("bud_flan_tariff_elec_2025", ENT, "2025", "455", "2025 nettarief elek gezin digitale meter 455 EUR incl btw vs 346; tick1386; primary official Fluvius JR2025 jaarverslag"),
        ("bud_flan_tariff_gas_2025", ENT, "2025", "242", "2025 nettarief gas gezin 242 EUR incl btw vs 225; tick1386; primary official Fluvius JR2025 jaarverslag"),
        ("bud_flan_pens_fso_2025", ENT, "2025", "14923505", "2025 off-balance FSO contractueel pensioen aandeel 14923505 + statutair Fluvius OV 15652000; tick1386; primary official NBB WVV 6.20"),
        ("bud_flan_shares_nb_2025", ENT, "2025", "28932166", "2025 aandelen netbeheer+neven 28932166 + Aov 1214561; tick1386; primary official Fluvius JR2025 jaarverslag"),
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
                "title": "Fluvius Antwerpen JR2025 leftover IGS dual (assets 2.46bn / omzet 430.93m / diensten 165.12m / debt 1.69bn / dividend 20.42m)",
                "entity_id": ENT,
                "beneficiary": "Fluvius Antwerpen / " + VENNOTEN,
                "legal_basis": "WVV OV; Decreet Lokaal Bestuur; Energiedecreet; NBB neerlegging",
                "decision_date": "2026-06-17",
                "start_year": "1972",
                "end_year": "",
                "total_envelope_eur": "2456270811",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL energy DSO — 430.93m omzet (geo empty) / 165.12m diensten / 1.69bn debt / 20.42m dividend",
                "cut_option": "Publish unpublished omzet geo + 81.3m 74 + 165.1m 61 FSO pass-through + 1.69bn debt counterparties + 20.42m dividend per vennoot; do not keep DSO IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1386; assets 2456270811 omzet 430933126 diensten 165123722 debt 1690066932 pnl 28512602 equity 755426317 dividend 20422377; FOI ready not sent; not TE-additive of 348bn; double_count vs Fluvius EG possible",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Fluvius Antwerpen JR2025 leftover IGS: assets 2.46bn / omzet 430.93m / diensten 165.12m / debt 1.69bn / dividend 20.42m / 0 VTE",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "165123722",
                "total_cost_eur": "2456270811",
                "tco_notes": (
                    "Leftover dual IGS energy DSO of 32 Antwerp-area municipalities (voorheen IMEA + Iveg + Integan): "
                    "assets 2.46bn / equity 755.43m / pnl +28.51m / omzet 430.93m (geo empty) / "
                    "diensten 165.12m / 0 VTE / debt 1.69bn (related 1.18bn) / dividend 20.42m / cash 1480; "
                    "official NBB WVV live; do not treat 2.46bn as TE-additive of 348bn; double_count vs Fluvius EG possible"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Fluvius Antwerpen / " + VENNOTEN,
                "stated_goal": "Local leftover IGS map VL energy DSO — JR2025 live; dual omzet-geo/diensten/debt/dividend FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 2.46bn / omzet 430.93m / diensten 165.12m / debt 1.69bn / dividend 20.42m / pnl +28.51m / 0 VTE",
                "absurdity_score": "7.2",
                "cost_score": "8.6",
                "difficulty": "3.0",
                "priority_index": "7.4",
                "cut_proposal": "Publish unpublished omzet geo + 81.3m 74 + 165.1m 61 FSO pass-through + 1.69bn debt counterparties + 20.42m dividend per vennoot; do not keep DSO IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1386; leftover IGS of 32 Antwerp-area municipalities; FOI ready not sent; not TE-additive of 348bn; distinct from Fluvius EG and West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382",
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
                    "omzet 430933126 JUMP vs 364038942 (WVV 70; 6.10 category elek 325913485 / gas 92718616 / riolering 3886574 / warmte 2364769 / kabel 230056 / other 5819627; geo empty) per vennoot/tariefstroom unpublished "
                    "+ andere bedrijfsopbrengsten 81309426 (WVV 74; 740 empty) "
                    "+ diensten 165123722 vs 177723856 (WVV 61; no split) + goods 172844254 + FSO pass-through (pers 62/9087 empty / 0 VTE) "
                    "+ schulden 1690066932 (LT bank 1357665997; related-party 1184715297) counterparties/rente unpublished "
                    "+ FVA other shares 60212510 unpublished "
                    "+ dividend 20422377 DROP vs 26522655 per vennoot unpublished "
                    "+ cash 1480 vs debt 1.69bn + prepaid 71418351 (regulatoire gas 25238887) + VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.18/9 not filed"
                ),
                "why_it_matters": (
                    "Leftover IGS OV energy DSO of 32 mined Antwerp-area municipalities "
                    "(same leftover-IGS energy seam as Fluvius West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382; distinct from Fluvius EG): "
                    "2.46bn assets / 430.93m omzet / 165.12m diensten / 1.69bn debt / 20.42m dividend / "
                    "0 VTE / FSO shell "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Fluvius Antwerpen / Raad van Bestuur / Koen Kennis / Patrick Janssens / 32 Antwerp-area vennoten",
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
                    "tick1386 leftover IGS OV energy DSO of 32 Antwerp-area municipalities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (1.94MB 97p deposit 2026-00228192). "
                    "Fluvius West already mined 1385 — skipped. Fluvius Kempen already mined 1384 — skipped. Imewo already mined 1383 — skipped. "
                    "INTERGEM already mined 1382 — skipped. INTERZA already mined 1381 — skipped. INCOVO already mined 1380 — skipped. "
                    "ISVAG already mined 1379 — skipped. De Nekker already mined 1378 — skipped. "
                    "MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. "
                    "Nuhma-group seam 1353-1365 skipped. Fluvius EG group already mined — this is a different legal person. "
                    "Other Fluvius DNB holdings (Halle-Vilvoorde / Limburg / Zenne-Dijle) leftover next if CDN live. "
                    "Dommelhof leftover Limburg EVA 0777.495.085 not re-probed once live Antwerpen extracted. "
                    "IVAREM still 2024. Otary RS Nuhma-adjacent fallback not taken. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1386",
        "title": "Fluvius Antwerpen / IMEA+Iveg JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Fluvius Antwerpen leftover IGS energy DSO of 32 Antwerp-area municipalities after honest hunt; "
            "KBO 0212.704.370 Actief; live JR2025 official NBB WVV VOL-inb PDF (1.94MB 97p deposit 2026-00228192; commissaris EY); "
            "sourced euros assets 2456270811 / omzet 430933126 / diensten 165123722 / debt 1690066932 / pnl 28512602 / dividend 20422377; "
            "FOI ready omzet geo empty / 81.3m 74 / 165.1m 61 / 1.69bn debt / 20.42m dividend"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T03:45:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1386 Fluvius Antwerpen leftover IGS energy residual; KBO 0212.704.370; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1387 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1387",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1386 done including Fluvius Antwerpen 1386 leftover energy IGS live NBB WVV / "
            "Fluvius West 1385 leftover energy IGS live NBB WVV / "
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
            "other Fluvius DNB holdings leftover energy IGS (Halle-Vilvoorde / Limburg / Zenne-Dijle) — take if a 2025 CDN/JR PDF still live and unmined; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads "
            "(old VZW 0443.049.478 CDN 2026-00325874 is a different Tielt-Winge entity); "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB PIH / APB Inovant / APB Atlas listed or leftover but provincieantwerpen.be 403 — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1386 after Fluvius Antwerpen leftover energy IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1386", rq_new, rq_spawn)
    print("research_queue 1386", found, "spawned_1387", spawned)

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
                "last_unit_id": "rq_1386",
                "ticks_completed": "1386",
                "paused": "no",
                "notes": (
                    "tick1386 Fluvius Antwerpen leftover IGS energy residual; KBO 0212.704.370; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 2456270811 omzet 430933126 diensten 165123722 debt 1690066932 pnl 28512602 equity 755426317 dividend 20422377; "
                    "FOI ready omzet geo empty/81.3m 74/165.1m 61/1.69bn debt/20.42m div; next rq_1387 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    entry = """### Tick 1386 - 2026-08-19 - rq_1386 Fluvius Antwerpen / IMEA+Iveg dual residual leftover
- Unit: Fluvius Antwerpen (voorheen IMEA / Intercommunale Maatschappij Voor Energievoorziening Antwerpen + Iveg + Integan fusie 01.04.2019; leftover IGS opdrachthoudende vereniging / energy DSO elektriciteit + aardgas + riolering + openbare verlichting + warmte + leftover kabel of 32 mined Antwerp-area municipalities; werkmaatschappij Fluvius System Operator) after residual dual hunt (KBO **0212.704.370**; official over.fluvius.be has activiteitenverslagen/governance + jaarverslag 2025 PDF; live NBB WVV VOL-inb deposit **2026-00228192** PDF 1.94MB / 97p; AV **17.06.2026**; header **26.06.2026**; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / Paul Eelen A02213 + Line Vyvey A02501 signed 26.03.2026 oordeel zonder voorbehoud assets 2.456.270.811 / te bestemmen +28.526.039 + benadrukking VOL-inb 6.19 regulatoire saldi 2025-2028). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; preferred leftover other Fluvius DNB holdings this tick). Distinct from already-mined Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM / Fluvius Midden-Vlaanderen 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 / Fluvius EG group-level (entity `fluvius`). First confirmed not already mined: no Fluvius Antwerpen / IMEA / IVEG / 0212.704.370 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **24.11.1972**; statutaire naam FLUVIUS Antwerpen since 01.04.2019; Opdrachthoudende vereniging (Vlaams Gewest) since 08.12.2003; zetel Merksemsesteenweg 233 2100 Antwerpen since 01.01.2023; **0 VE**; KBO no email/web/tel; official site https://over.fluvius.be/; btw since 01.01.1973; boekjaar 31 december; NACE 35.220/35.110/37.000. Absorbed VET 0219.943.441 (17.12.2003), IMEA 0204.647.234 (01.04.2019), Integan 0212.586.683 (01.04.2019). Voorzitter Koen Kennis; ondervoorzitter Patrick Janssens; commissaris EY since 18.06.2025 tot 18.06.2028. Hunt leftover AGB/zorg/EVA first: leftover AGB Mechelen/Kortrijk/Brugge/Roeselare/Oostende 404/403 as of 1375 — not re-probed once live Antwerpen extracted; Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live Antwerpen extracted; IVAREM still 2024; leftover APB provincieantwerpen.be 403. Fluvius Antwerpen statutory CDN live this tick (HTTP 200 / 1940681 / 97p) — taken (preferred leftover energy IGS of mined Antwerp municipalities outside Nuhma; listed leftover-next after West 1385). Fluvius West already mined 1385 — skipped. Fluvius Kempen already mined 1384 — skipped. Imewo already mined 1383 — skipped. INTERGEM already mined 1382 — skipped. INTERZA already mined 1381 — skipped. INCOVO already mined 1380 — skipped. ISVAG already mined 1379 — skipped. De Nekker already mined 1378 — skipped. MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 already mined — skipped. Fluvius EG group already mined — this is a different legal person (DSO holding). Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. Other Fluvius DNB holdings (Halle-Vilvoorde / Limburg / Zenne-Dijle) leftover next. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366. Not every-10 (next 1390).
- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud assets 2.456.270.811 / te bestemmen +28.526.039 + benadrukking 6.19; VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62/9087 empty): assets **2.456.270.811** (was 2.295.213.508); fixed **2.060.199.199** / MVA **1.881.193.332** (gebouwen **43.846.411**; machines **1.557.190.339**; meubilair **8.354.243**; leasing **10.451.205**; overige **1.557.466**; CIP **259.793.668** aanschaf **218.093.174**); IVA 18.422.050; FVA **160.583.817** (deelnemingen **100.246.306** FSO 15,7% A / 26,23% K-SYN; andere aandelen **60.212.510**); current **396.071.612**; LT recv 60.885.783; WIP 14.838.054; ST recv **248.927.944** (trade 69.882.449 + other 179.045.495); beleggingen empty; cash **1.480** vs 2.840; prepaid **71.418.351** (regulatoire gas 25.238.887); equity **755.426.317** (inbreng 404.513.783; reval 112.617.787; reserves 159.221.603; overgedragen 64.637.195; capsub 14.435.949); voorzieningen **10.777.562** (milieu 420.731; pens 160 empty); schulden **1.690.066.932** (LT **1.399.475.389** waarvan bank **1.357.665.997** + lease 10.228.288 + other 31.581.103; ST **226.589.414** waarvan LT-due 103.284.536 + leveranciers **73.040.004 JUMP** vs 21.216.849; related-party FSO-seam **1.184.715.297**); omzet **430.933.126 JUMP** vs 364.038.942 (elek **325.913.485** / gas **92.718.616** / riolering **3.886.574** / warmte **2.364.769** / kabel **230.056** / other **5.819.627**; geo empty); othops **81.309.426** (740 empty); goods **172.844.254**; diensten **165.123.722** vs 177.723.856; pers **empty / 0 VTE**; afschr 79.818.145; expl **+63.269.671** vs +29.394.670; fin opbr 13.464.943; fin kosten 39.712.360; tax 8.546.124; PnL **+28.512.602** vs +5.467.394; dividend **20.422.377 DROP** vs 26.522.655; bruto capex jaarverslag **253.124.000**; commissaris 42.558 + extra 28.272; bestuurders 29.237. Jaarverslag same tick: 32 vennoten; WACC/kapitaalkost 5,2% vs 3,5%; nettarief gezin elek **455** vs 346 / gas **242** vs 225; FSO stemaandeel 15,7% A; Zwijndrecht partiële splitsing naar Fluvius MV 01.01.2026.
- CSVs: sources+4/entities+1/budgets+84/commitments+1/leaderboard+1 + FOI ready `gap_flan_omzet_430_93m_diensten_165_12m_debt_1_69bn_l5` (not sent); rq_1386=done; spawn rq_1387; ticks=1386.
- Coverage: residual dual L5 (Fluvius Antwerpen leftover energy IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs Fluvius EG possible. No progress refresh (not every-10; next 1390).
- Next: rq_1387 residual dual L5 VL JR2025 hole_fill (prefer leftover other Fluvius DNB holdings Halle-Vilvoorde / Limburg / Zenne-Dijle if a 2025 CDN/JR PDF still live and unmined; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS CDN 2026-00254280 / Rematics / Sunfin only if taken after leftover IGS/EVA/AGB; leftover APB POA / TPA / De Schorre / Warande / PIH / Inovant / Atlas only if a real PDF downloads; IVAREM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1386 write done")


if __name__ == "__main__":
    main()

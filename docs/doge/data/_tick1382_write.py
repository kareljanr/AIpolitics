# -*- coding: utf-8 -*-
"""Tick 1382 — leftover Fluvius Midden-Vlaanderen / INTERGEM JR2025 official NBB WVV euros.
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

TICK = "1382"
UTC = "2026-08-19T02:25:00Z"
ENT = "igs_intg"
HIER = "Vlaanderen>OostVlaanderen>IGS>FluviusMiddenVlaanderen"
GAP = "gap_intg_omzet_242_74m_diensten_88_70m_debt_946_63m_l5"
SRC = "src_intg_jr2025_nbb"
SRC2 = "src_intg_site"
SRC3 = "src_kbo_intg_0220764971"
SRC4 = "src_intg_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00227859.pdf"
SRC2_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-midden-vlaanderen/overzichtslijst-besluiten"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0220764971"
SRC4_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-midden-vlaanderen/overzichtslijst-besluiten"
FOI_EMAIL = ""
FOI_POSTAL = "Franz Courtensstraat 11 9200 Dendermonde / p/a Brusselsesteenweg 199 9090 Merelbeke-Melle"
DRAFT = "docs/doge/foi/drafts/gap_intg_omzet_242_74m_diensten_88_70m_debt_946_63m_l5.md"
COMM = "comm_intg_jr2025_pnl"
LB = "lb_intg_omzet_242_74m_diensten_88_70m_debt_946_63m"
VENNOTEN = (
    "Aalst + Bever + Beveren-Kruibeke-Zwijndrecht + Brakel + Buggenhout + "
    "Denderleeuw + Dendermonde + Erpe-Mere + Geraardsbergen + Haaltert + "
    "Hamme + Herzele + Lebbeke + Lierde + Ninove + Sint-Gillis-Waas + "
    "Sint-Niklaas + Stekene + Temse + Waasmunster + Zottegem"
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
                "title": "Fluvius Midden-Vlaanderen (voorheen INTERGEM) jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00227859; AV 15.06.2026)",
                "url": SRC_URL,
                "publisher": "Fluvius Midden-Vlaanderen / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1382; official NBB VOL-inb PDF 2.01MB 90p deposit 2026-00227859 created 01.07.2026 header 26.06.2026; "
                    "leftover IGS energy DSO of 21 Oost-Vlaanderen municipalities (voorheen INTERGEM); "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / "
                    "Line Vyvey A02501 + Paul Eelen A02213 oordeel zonder voorbehoud assets 1294735894 / PnL 17698095 + benadrukking 6.19 regulatoire saldi; "
                    "VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.8/6.12/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62 empty"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Fluvius Midden-Vlaanderen official governance page (leftover IGS energy DSO; voorheen INTERGEM; 21 Oost-Vlaanderen vennoten)",
                "url": SRC2_URL,
                "publisher": "Fluvius / Fluvius Midden-Vlaanderen",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1382; leftover IGS of 21 Oost-Vlaanderen municipalities; "
                    "over.fluvius.be lists besluiten; statutory 2025 balans is the NBB CDN deposit; "
                    "naamswijziging INTERGEM -> Fluvius Midden-Vlaanderen 01.01.2025"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Fluvius Midden-Vlaanderen / INTERGEM 0220.764.971",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1382; KBO 0220.764.971 Actief / normale toestand since 15.09.1980; "
                    "statutaire naam FLUVIUS MIDDEN-VLAANDEREN since 01.01.2025; "
                    "Opdrachthoudende vereniging (Vlaams Gewest) since 06.11.2003; "
                    "zetel Franz Courtensstraat 11 9200 Dendermonde since 28.01.2008; 0 VE; "
                    "no KBO email/web/tel; KBO kapitaal 201116418; btw since 01.10.1980; "
                    "jaarvergadering mei; boekjaar 31 december; NACE 35.140/35.220/42.220/43.211/71.111; "
                    "absorbed IGA 0204.889.734 (01.01.2009) + FINGEM 0219.768.346 (01.04.2018)"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Fluvius Midden-Vlaanderen FOI channel / official governance + secretariaat (KBO no email)",
                "url": SRC4_URL,
                "publisher": "Fluvius Midden-Vlaanderen",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1382; KBO no email/web/tel; secretariaat Brusselsesteenweg 199 9090 Merelbeke-Melle; "
                    "zetel Franz Courtensstraat 11 9200 Dendermonde; "
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
                "name_nl": "Fluvius Midden-Vlaanderen (voorheen INTERGEM; leftover IGS energy DSO Midden-Vlaanderen)",
                "name_fr": "Fluvius Flandre-Centrale (ex-INTERGEM; IGS residuel DSO energie)",
                "name_en": "Fluvius Midden-Vlaanderen leftover IGS energy DSO (formerly INTERGEM)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-midden-vlaanderen/overzichtslijst-besluiten",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1382 leftover residual IGS energy DSO of 21 Oost-Vlaanderen municipalities; "
                    "KBO 0220.764.971 Actief since 15.09.1980; naam INTERGEM until 01.01.2025; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 1294735894 omzet 242736979 diensten 88697404 debt 946626642 pnl 17698095 equity 346065423 dividend 9036900; "
                    "FOI ready omzet geo empty / 48.3m 74 empty 740 / 88.7m 61 / 946.6m debt / 9.04m dividend; "
                    "distinct from already-mined Fluvius EG group entity fluvius"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_intg_assets_2025", ENT, "2025", "1294735894", "2025 assets 1294735894 VOL-inb 20/58; tick1382; primary official NBB WVV; commissaris 1294735894"),
        ("bud_intg_assets_2024", ENT, "2024", "1236766390", "2024 assets 1236766390 comparative; tick1382; primary official NBB WVV 20/58"),
        ("bud_intg_fixed_2025", ENT, "2025", "1147687334", "2025 vaste activa 1147687334 vs 1091248799; tick1382; primary official NBB WVV 21/28"),
        ("bud_intg_iva_2025", ENT, "2025", "9563402", "2025 IVA 9563402 vs 9555706; tick1382; primary official NBB WVV 21"),
        ("bud_intg_mva_2025", ENT, "2025", "1066587791", "2025 MVA 1066587791 vs 1023642822; tick1382; primary official NBB WVV 22/27"),
        ("bud_intg_buildings_2025", ENT, "2025", "23189194", "2025 terreinen/gebouwen 23189194 vs 22831071; tick1382; primary official NBB WVV 22"),
        ("bud_intg_machines_2025", ENT, "2025", "934212228", "2025 installaties/machines 934212228 vs 901663768; tick1382; primary official NBB WVV 23"),
        ("bud_intg_furniture_2025", ENT, "2025", "5971674", "2025 meubilair/rollend 5971674 vs 5914170; tick1382; primary official NBB WVV 24"),
        ("bud_intg_lease_mva_2025", ENT, "2025", "7320407", "2025 leasing MVA 7320407 vs 7684700; tick1382; primary official NBB WVV 25"),
        ("bud_intg_other_mva_2025", ENT, "2025", "414255", "2025 overige MVA 414255 vs 103272; tick1382; primary official NBB WVV 26"),
        ("bud_intg_cip_2025", ENT, "2025", "95480033", "2025 CIP 95480033 vs 85445841; aanschaf 113816058; tick1382; primary official NBB WVV 27"),
        ("bud_intg_cip_acq_2025", ENT, "2025", "113816058", "2025 CIP aanschaf 113816058 (8166); tick1382; primary official NBB WVV 6.3.6"),
        ("bud_intg_fva_2025", ENT, "2025", "71536142", "2025 FVA 71536142 vs 58050271; tick1382; primary official NBB WVV 28"),
        ("bud_intg_fva_part_2025", ENT, "2025", "9707603", "2025 deelnemingen 9707603 (FSO 7.12pct + K-SYN 8.04pct + Transco 11.11pct); tick1382; primary official NBB WVV 282"),
        ("bud_intg_fva_shares_2025", ENT, "2025", "61828539", "2025 andere aandelen 61828539 vs 48160496 after aanschaf 14421971; tick1382; primary official NBB WVV 284"),
        ("bud_intg_fva_acq_2025", ENT, "2025", "14421971", "2025 FVA andere aandelen aanschaf 14421971; tick1382; primary official NBB WVV 6.4.3 8363"),
        ("bud_intg_current_2025", ENT, "2025", "147048560", "2025 vlottende activa 147048560 vs 145517591; tick1382; primary official NBB WVV 29/58"),
        ("bud_intg_ltrecv_2025", ENT, "2025", "21628033", "2025 LT vorderingen 21628033 JUMP vs 8340291 (all other 291); tick1382; primary official NBB WVV 29"),
        ("bud_intg_wip_2025", ENT, "2025", "2687192", "2025 bestellingen in uitvoering 2687192 vs 4269673; tick1382; primary official NBB WVV 37"),
        ("bud_intg_strecv_2025", ENT, "2025", "85553248", "2025 ST vorderingen 85553248 vs 75846556; tick1382; primary official NBB WVV 40/41"),
        ("bud_intg_trade_2025", ENT, "2025", "35643258", "2025 handelsvorderingen 35643258 vs 28396119; tick1382; primary official NBB WVV 40"),
        ("bud_intg_othrecv_2025", ENT, "2025", "49909991", "2025 overige ST vorderingen 49909991 vs 47450437; tick1382; primary official NBB WVV 41"),
        ("bud_intg_invest_2025", ENT, "2025", "0", "2025 geldbeleggingen 0 vs 14670143; tick1382; primary official NBB WVV 50/53"),
        ("bud_intg_invest_2024", ENT, "2024", "14670143", "2024 geldbeleggingen 14670143 comparative; tick1382; primary official NBB WVV 50/53"),
        ("bud_intg_cash_2025", ENT, "2025", "993", "2025 liquide middelen 993 vs 1442 (near-zero vs 946.6m debt); tick1382; primary official NBB WVV 54/58"),
        ("bud_intg_prepaid_2025", ENT, "2025", "37179094", "2025 overlopend actief 37179094 (VNR-gas 12761545 / verbruiken 8958900 / REG 7270761 / pens 5284753); tick1382; primary official NBB WVV 490/1"),
        ("bud_intg_equity_2025", ENT, "2025", "346065423", "2025 eigen vermogen 346065423 vs 345660142; tick1382; primary official NBB WVV 10/15"),
        ("bud_intg_equity_2024", ENT, "2024", "345660142", "2024 eigen vermogen 345660142 comparative; tick1382; primary official NBB WVV 10/15"),
        ("bud_intg_inbreng_2025", ENT, "2025", "130575272", "2025 inbreng beschikbaar 130575272 vs 135117124; tick1382; primary official NBB WVV 10/11"),
        ("bud_intg_reval_2025", ENT, "2025", "74689796", "2025 herwaarderingsmeerwaarden 74689796 vs 80576725; tick1382; primary official NBB WVV 12"),
        ("bud_intg_reserves_2025", ENT, "2025", "109613364", "2025 reserves 109613364 (onbeschikbaar 27360350 + belastingvrij 426150 + beschikbaar 81826865); tick1382; primary official NBB WVV 13"),
        ("bud_intg_retained_2025", ENT, "2025", "30856406", "2025 overgedragen winst 30856406 vs 21258306; tick1382; primary official NBB WVV 14"),
        ("bud_intg_capsub_2025", ENT, "2025", "330584", "2025 kapitaalsubsidies 330584 vs 324987; tick1382; primary official NBB WVV 15"),
        ("bud_intg_prov_2025", ENT, "2025", "2043828", "2025 voorzieningen+latenties 2043828 (milieu 1819824 + uitgesteld 224004); pens 160 empty; tick1382; primary official NBB WVV 16"),
        ("bud_intg_env_2025", ENT, "2025", "1819824", "2025 milieuvoorziening 1819824; tick1382; primary official NBB WVV 163"),
        ("bud_intg_debt_2025", ENT, "2025", "946626642", "2025 schulden 946626642 vs 889058033; tick1382; primary official NBB WVV 17/49"),
        ("bud_intg_debt_2024", ENT, "2024", "889058033", "2024 schulden 889058033 comparative; tick1382; primary official NBB WVV 17/49"),
        ("bud_intg_lt_2025", ENT, "2025", "804040494", "2025 LT schulden 804040494 vs 764632318 (all financial); tick1382; primary official NBB WVV 17"),
        ("bud_intg_ltbank_2025", ENT, "2025", "791081244", "2025 LT kredietinstellingen 791081244 vs 750851725; tick1382; primary official NBB WVV 173"),
        ("bud_intg_ltlease_2025", ENT, "2025", "7188944", "2025 LT leasing 7188944 vs 7504927; tick1382; primary official NBB WVV 172"),
        ("bud_intg_ltother_2025", ENT, "2025", "5770307", "2025 LT overige leningen 5770307 vs 6275666; tick1382; primary official NBB WVV 174"),
        ("bud_intg_st_2025", ENT, "2025", "123907544", "2025 ST schulden 123907544 vs 107952072; tick1382; primary official NBB WVV 42/48"),
        ("bud_intg_st_due_2025", ENT, "2025", "64892087", "2025 LT-due within year 64892087 vs 44770584; tick1382; primary official NBB WVV 42"),
        ("bud_intg_sttrade_2025", ENT, "2025", "40578108", "2025 leveranciers 40578108 JUMP vs 10435829; tick1382; primary official NBB WVV 440/4"),
        ("bud_intg_stadv_2025", ENT, "2025", "11480267", "2025 vooruitbetalingen 11480267 vs 11588916; tick1382; primary official NBB WVV 46"),
        ("bud_intg_sttax_2025", ENT, "2025", "5152185", "2025 tax ST 5152185 vs 4669020 (soc empty); tick1382; primary official NBB WVV 45"),
        ("bud_intg_stother_2025", ENT, "2025", "1804897", "2025 overige ST 1804897 vs 36487724; tick1382; primary official NBB WVV 47/48"),
        ("bud_intg_accrued_2025", ENT, "2025", "18678605", "2025 overlopend passief 18678605 (intrest 10647841 + VNR-elek 4973994 + energie 2665700); tick1382; primary official NBB WVV 492/3"),
        ("bud_intg_reldebt_2025", ENT, "2025", "692009832", "2025 related-party debt 692009832 (LT 627847198 / ST 64162634; FSO-seam 6.15); tick1382; primary official NBB WVV 6.15 9352"),
        ("bud_intg_opsinc_2025", ENT, "2025", "289786955", "2025 bedrijfsopbrengsten 289786955 vs 248937455; tick1382; primary official NBB WVV 70/76A"),
        ("bud_intg_omzet_2025", ENT, "2025", "242736979", "2025 omzet 242736979 JUMP vs 199983337; 6.10 geo empty; tick1382; primary official NBB WVV 70"),
        ("bud_intg_omzet_2024", ENT, "2024", "199983337", "2024 omzet 199983337 comparative; tick1382; primary official NBB WVV 70"),
        ("bud_intg_omzet_elec_2025", ENT, "2025", "192454099", "2025 omzet elektriciteit 192454099 vs 147308574; tick1382; primary official NBB WVV 6.10"),
        ("bud_intg_omzet_gas_2025", ENT, "2025", "46691078", "2025 omzet gas 46691078 vs 49525956; tick1382; primary official NBB WVV 6.10"),
        ("bud_intg_omzet_other_2025", ENT, "2025", "3591802", "2025 omzet overige 3591802 vs 3148807; tick1382; primary official NBB WVV 6.10"),
        ("bud_intg_othops_2025", ENT, "2025", "48348893", "2025 andere bedrijfsopbrengsten 48348893 vs 48494358; 740 empty; tick1382; primary official NBB WVV 74"),
        ("bud_intg_opscost_2025", ENT, "2025", "252782254", "2025 bedrijfskosten 252782254 vs 227622420; tick1382; primary official NBB WVV 60/66A"),
        ("bud_intg_goods_2025", ENT, "2025", "103810208", "2025 handelsgoederen 103810208 vs 81252709; tick1382; primary official NBB WVV 60"),
        ("bud_intg_diensten_2025", ENT, "2025", "88697404", "2025 diensten 88697404 vs 90114995; no split; FSO pass-through; tick1382; primary official NBB WVV 61"),
        ("bud_intg_diensten_2024", ENT, "2024", "90114995", "2024 diensten 90114995 comparative; tick1382; primary official NBB WVV 61"),
        ("bud_intg_pers_2025", ENT, "2025", "0", "2025 bezoldigingen 62 empty / 9087 empty / 0 VTE (werkmaatschappij FSO); tick1382; primary official NBB WVV 62"),
        ("bud_intg_deprec_2025", ENT, "2025", "48433249", "2025 afschrijvingen 48433249 vs 46473187; tick1382; primary official NBB WVV 630"),
        ("bud_intg_othcost_2025", ENT, "2025", "12145118", "2025 andere bedrijfskosten 12145118 (tax 244788 + other 11900330); tick1382; primary official NBB WVV 640/8"),
        ("bud_intg_expl_2025", ENT, "2025", "37004700", "2025 bedrijfswinst 37004700 vs 21315034; tick1382; primary official NBB WVV 9901"),
        ("bud_intg_expl_2024", ENT, "2024", "21315034", "2024 bedrijfswinst 21315034 comparative; tick1382; primary official NBB WVV 9901"),
        ("bud_intg_fininc_2025", ENT, "2025", "9190325", "2025 financiele opbrengsten 9190325 vs 6642485 (FVA 5427511 + vlottende 3751668); tick1382; primary official NBB WVV 75"),
        ("bud_intg_fincost_2025", ENT, "2025", "23121533", "2025 financiele kosten 23121533 vs 21006778 (schulden 23118621); tick1382; primary official NBB WVV 65"),
        ("bud_intg_tax_2025", ENT, "2025", "5381478", "2025 belastingen 5381478 vs 1222174; tick1382; primary official NBB WVV 67/77"),
        ("bud_intg_pnl_2025", ENT, "2025", "17698095", "2025 PnL 9904 17698095 vs 5734582; commissaris 17698095; tick1382; primary official NBB WVV"),
        ("bud_intg_pnl_2024", ENT, "2024", "5734582", "2024 PnL 5734582 comparative; tick1382; primary official NBB WVV 9904"),
        ("bud_intg_alloc_2025", ENT, "2025", "17705614", "2025 te bestemmen 9905 17705614 vs 5742245; tick1382; primary official NBB WVV 9905"),
        ("bud_intg_div_2025", ENT, "2025", "9036900", "2025 dividend/vergoeding inbreng 9036900 DROP vs 14260886; tick1382; primary official NBB WVV 694"),
        ("bud_intg_div_2024", ENT, "2024", "14260886", "2024 dividend 14260886 comparative; tick1382; primary official NBB WVV 694"),
        ("bud_intg_capex_2025", ENT, "2025", "133322000", "2025 gerealiseerd bruto investeringsbudget 133322000 (jaarverslag duizenden); tick1382; primary official NBB WVV jaarverslag"),
        ("bud_intg_comm_2025", ENT, "2025", "12378", "2025 commissaris EY 12378 + extra controle 41899 + taxadvies verbonden 6024; tick1382; primary official NBB WVV 9505"),
        ("bud_intg_comm_extra_2025", ENT, "2025", "41899", "2025 commissaris andere controleopdrachten 41899; tick1382; primary official NBB WVV 95061"),
        ("bud_intg_board_2025", ENT, "2025", "15305", "2025 bestuurders 9503 15305; tick1382; primary official NBB WVV 9503"),
        ("bud_intg_tariff_elec_2025", ENT, "2025", "436", "2025 nettarief elek gezin digitale meter 436 EUR incl btw vs 314; tick1382; primary official NBB WVV jaarverslag"),
        ("bud_intg_tariff_gas_2025", ENT, "2025", "244", "2025 nettarief gas gezin 244 EUR incl btw vs 229; tick1382; primary official NBB WVV jaarverslag"),
        ("bud_intg_shares_nb_2025", ENT, "2025", "13203185", "2025 aandelen netbeheer+neven 13203185 + Aov 704877; tick1382; primary official NBB WVV jaarverslag"),
        ("bud_intg_kbo_cap_2025", ENT, "2025", "201116418", "2025 KBO kapitaal 201116418 (register; vs inbreng 130575272); tick1382; primary official KBO"),
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
                "title": "Fluvius Midden-Vlaanderen / INTERGEM JR2025 leftover IGS dual (assets 1.29bn / omzet 242.74m / diensten 88.70m / debt 946.63m / dividend 9.04m)",
                "entity_id": ENT,
                "beneficiary": "Fluvius Midden-Vlaanderen / " + VENNOTEN,
                "legal_basis": "WVV OV; Decreet Lokaal Bestuur; Energiedecreet; NBB neerlegging",
                "decision_date": "2026-06-15",
                "start_year": "1980",
                "end_year": "",
                "total_envelope_eur": "1294735894",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL energy DSO — 242.74m omzet (geo empty) / 88.70m diensten / 946.63m debt / 9.04m dividend",
                "cut_option": "Publish unpublished omzet geo + 48.3m 74 + 88.7m 61 FSO pass-through + 946.6m debt counterparties + 9.04m dividend per vennoot; do not keep DSO IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1382; assets 1294735894 omzet 242736979 diensten 88697404 debt 946626642 pnl 17698095 equity 346065423 dividend 9036900; FOI ready not sent; not TE-additive of 348bn; double_count vs Fluvius EG possible",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Fluvius Midden-Vlaanderen / INTERGEM JR2025 leftover IGS: assets 1.29bn / omzet 242.74m / diensten 88.70m / debt 946.63m / dividend 9.04m / 0 VTE",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "88697404",
                "total_cost_eur": "1294735894",
                "tco_notes": (
                    "Leftover dual IGS energy DSO of 21 Oost-Vlaanderen municipalities (voorheen INTERGEM): "
                    "assets 1.29bn / equity 346.1m / pnl +17.70m / omzet 242.74m (geo empty) / "
                    "diensten 88.70m / 0 VTE / debt 946.63m (related 692.01m) / dividend 9.04m / cash 993; "
                    "official NBB WVV live; do not treat 1.29bn as TE-additive of 348bn; double_count vs Fluvius EG possible"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Fluvius Midden-Vlaanderen / " + VENNOTEN,
                "stated_goal": "Local leftover IGS map VL energy DSO — JR2025 live; dual omzet-geo/diensten/debt/dividend FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 1.29bn / omzet 242.74m / diensten 88.70m / debt 946.63m / dividend 9.04m / pnl +17.70m / 0 VTE",
                "absurdity_score": "7.5",
                "cost_score": "9.0",
                "difficulty": "3.0",
                "priority_index": "7.8",
                "cut_proposal": "Publish unpublished omzet geo + 48.3m 74 + 88.7m 61 FSO pass-through + 946.6m debt counterparties + 9.04m dividend per vennoot; do not keep DSO IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1382; leftover IGS of 21 Oost-Vlaanderen municipalities; FOI ready not sent; not TE-additive of 348bn; distinct from Fluvius EG",
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
                    "omzet 242736979 JUMP vs 199983337 (WVV 70; 6.10 category elek 192454099 / gas 46691078 / other 3591802; geo empty) per vennoot/tariefstroom unpublished "
                    "+ andere bedrijfsopbrengsten 48348893 (WVV 74; 740 empty) "
                    "+ diensten 88697404 vs 90114995 (WVV 61; no split) + goods 103810208 + FSO pass-through (pers 62/9087 empty / 0 VTE) "
                    "+ schulden 946626642 (LT bank 791081244; related-party 692009832) counterparties/rente unpublished "
                    "+ FVA other shares 61828539 after aanschaf 14421971 unpublished "
                    "+ dividend 9036900 DROP vs 14260886 per vennoot unpublished "
                    "+ cash 993 vs debt 946.6m + prepaid VNR/REG/pens 37179094 + VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.8/6.12/6.18/9 not filed"
                ),
                "why_it_matters": (
                    "Leftover IGS OV energy DSO of 21 mined Oost-Vlaanderen municipalities "
                    "(same leftover-IGS seam as INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / IVAGO 1375; distinct from Fluvius EG): "
                    "1.29bn assets / 242.74m omzet / 88.70m diensten / 946.63m debt / 9.04m dividend / "
                    "0 VTE / FSO shell "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Fluvius Midden-Vlaanderen / Raad van Bestuur / Carl Hanssens / Dirk Abbeloos / 21 Oost-Vlaanderen vennoten",
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
                    "tick1382 leftover IGS OV energy DSO of 21 Oost-Vlaanderen municipalities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (2.01MB 90p deposit 2026-00227859). "
                    "INTERZA already mined 1381 — skipped. INCOVO already mined 1380 — skipped. ISVAG already mined 1379 — skipped. "
                    "De Nekker already mined 1378 — skipped. MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. "
                    "IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. "
                    "IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. "
                    "IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. "
                    "Nuhma-group seam 1353-1365 skipped. Fluvius EG group already mined — this is a different legal person. "
                    "Other Fluvius DNB holdings (Imewo / Kempen / West / Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle) leftover next if CDN live. "
                    "Dommelhof leftover Limburg EVA 0777.495.085 not re-probed once live INTERGEM extracted. "
                    "IVAREM still 2024. Otary RS Nuhma-adjacent fallback not taken. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1382",
        "title": "INTERGEM / Fluvius MV JR2025 leftover dual residual",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: Fluvius Midden-Vlaanderen / INTERGEM leftover IGS energy DSO of 21 Oost-Vlaanderen municipalities after honest hunt; "
            "KBO 0220.764.971 Actief; live JR2025 official NBB WVV VOL-inb PDF (2.01MB 90p deposit 2026-00227859; commissaris EY); "
            "sourced euros assets 1294735894 / omzet 242736979 / diensten 88697404 / debt 946626642 / pnl 17698095 / dividend 9036900; "
            "FOI ready omzet geo empty / 48.3m 74 / 88.7m 61 / 946.6m debt / 9.04m dividend"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T02:15:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1382 INTERGEM leftover IGS energy residual; KBO 0220.764.971; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1383 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1383",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1382 done including INTERGEM / Fluvius Midden-Vlaanderen 1382 leftover energy IGS live NBB WVV / "
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
            "other Fluvius DNB holdings leftover energy IGS (Imewo / Kempen-Iveka / West-Gaselwest / Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle) — take if a 2025 CDN/JR PDF still live and unmined; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads "
            "(old VZW 0443.049.478 CDN 2026-00325874 is a different Tielt-Winge entity); "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
            "APB POA / APB TPA / APB De Schorre / APB Warande / APB PIH / APB Inovant / APB Atlas listed or leftover but provincieantwerpen.be 403 — take only if a real PDF downloads; "
            "IVAREM still 2024 — take only if a 2025 JR PDF now downloads; "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE still unmined — take only if PDF fetches; "
            "skip already-mined INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat Services 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA Limburg Sterk Merk 1340; "
            "skip Westtoer APB already mined; skip AGB MAC if 1270 already extracted JR2025; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1382 after INTERGEM leftover energy IGS live NBB WVV; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1382", rq_new, rq_spawn)
    print("research_queue 1382", found, "spawned_1383", spawned)

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
                "last_unit_id": "rq_1382",
                "ticks_completed": "1382",
                "paused": "no",
                "notes": (
                    "tick1382 INTERGEM leftover IGS energy residual; KBO 0220.764.971; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 1294735894 omzet 242736979 diensten 88697404 debt 946626642 pnl 17698095 equity 346065423 dividend 9036900; "
                    "FOI ready omzet geo empty/48.3m 74/88.7m 61/946.6m debt/9.04m div; next rq_1383 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    log = ROOT / "loop_log.md"
    entry = """### Tick 1382 - 2026-08-19 - rq_1382 INTERGEM / Fluvius Midden-Vlaanderen dual residual leftover
- Unit: Fluvius Midden-Vlaanderen (voorheen INTERGEM / Intercommunale Vereniging voor Energieleveringen in Midden-Vlaanderen; leftover IGS opdrachthoudende vereniging / energy DSO elektriciteit + aardgas + openbare verlichting of 21 mined Oost-Vlaanderen municipalities; werkmaatschappij Fluvius System Operator) after residual dual hunt (KBO **0220.764.971**; official over.fluvius.be has besluiten/governance but no isolated statutory 2025 balans — live NBB WVV VOL-inb deposit **2026-00227859** PDF 2.01MB / 90p; AV **15.06.2026**; header **26.06.2026**; PDF created **01.07.2026**; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / Line Vyvey A02501 + Paul Eelen A02213 signed 26.03.2026 oordeel zonder voorbehoud assets 1.294.735.894 / PnL +17.698.095 + benadrukking VOL-inb 6.19 regulatoire saldi 2025-2028). Leftover IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; prior ticks listed INTERGEM CDN 2026-00227859 as leftover next after INTERZA 1381). Distinct from already-mined INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 / Fluvius EG group-level (entity `fluvius`). First confirmed not already mined: no INTERGEM / IMEA / IVEKA / GASELWEST / IMEWO / IVEG / intg / flmv JR2025 extract in entities/sources. KBO Actief / normale toestand since **15.09.1980**; statutaire naam FLUVIUS MIDDEN-VLAANDEREN since 01.01.2025; Opdrachthoudende vereniging (Vlaams Gewest) since 06.11.2003; zetel Franz Courtensstraat 11 9200 Dendermonde since 28.01.2008; **0 VE**; KBO no email/web/tel; KBO kapitaal 201.116.418; official site https://over.fluvius.be/; secretariaat Brusselsesteenweg 199 9090 Merelbeke-Melle; btw since 01.10.1980; jaarvergadering mei; boekjaar 31 december; NACE 35.140/35.220/42.220/43.211/71.111. Absorbed IGA 0204.889.734 (01.01.2009) + FINGEM 0219.768.346 (01.04.2018). Voorzitter Carl Hanssens since 13.03.2025; ondervoorzitter Dirk Abbeloos; commissaris EY since 12.06.2025 tot 12.06.2028. Hunt leftover AGB/zorg/EVA first: leftover AGB Mechelen/Kortrijk/Brugge/Roeselare/Oostende 404/403 as of 1375 — not re-probed once live INTERGEM extracted; Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live INTERGEM extracted; IVAREM still 2024; leftover APB provincieantwerpen.be 403. INTERGEM statutory CDN live this tick (HTTP 200 / 2011372 / 90p) — taken (preferred leftover energy IGS of mined Midden-Vlaanderen municipalities outside Nuhma). INTERZA already mined 1381 — skipped. INCOVO already mined 1380 — skipped. ISVAG already mined 1379 — skipped. De Nekker already mined 1378 — skipped. MIROM Menen already mined 1377 — skipped. MIROM Roeselare already mined 1376 — skipped. IVAGO already mined 1375 — skipped. MIWA already mined 1374 — skipped. IVOO already mined 1373 — skipped. IGEMO already mined 1372 — skipped. Veneco already mined 1371 — skipped. Haviland already mined 1370 — skipped. IMOG already mined 1369 — skipped. IOK already mined 1368 — skipped. Leiedal already mined 1367 — skipped. Nuhma-group seam 1353-1365 already mined — skipped. Fluvius EG group already mined — this is a different legal person (DSO holding). Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. Other Fluvius DNB holdings (Imewo / Kempen / West / Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle) leftover next. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366. Not every-10 (next 1390).
- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud assets 1.294.735.894 / PnL +17.698.095 + benadrukking 6.19; VOL-inb 6.1/6.2.2-6.2.5/6.4.1/6.5.2/6.7.2/6.8/6.12/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62/9087 empty): assets **1.294.735.894** (was 1.236.766.390); fixed **1.147.687.334** / MVA **1.066.587.791** (gebouwen **23.189.194**; machines **934.212.228**; meubilair **5.971.674**; leasing **7.320.407**; overige **414.255**; CIP **95.480.033** aanschaf **113.816.058**); IVA 9.563.402; FVA **71.536.142** (deelnemingen **9.707.603** FSO 7,12% + K-SYN 8,04% + Transco 11,11%; andere aandelen **61.828.539** aanschaf **14.421.971**); current **147.048.560**; LT recv **21.628.033 JUMP** vs 8.340.291; WIP 2.687.192; ST recv **85.553.248** (trade 35.643.258 + other 49.909.991); beleggingen **0** vs 14.670.143; cash **993** vs 1.442; prepaid **37.179.094** (VNR-gas 12.761.545 / verbruiken 8.958.900 / REG 7.270.761 / pens 5.284.753); equity **346.065.423** (inbreng 130.575.272; reval 74.689.796; reserves 109.613.364; overgedragen 30.856.406; capsub 330.584); voorzieningen **2.043.828** (milieu 1.819.824; pens 160 empty); schulden **946.626.642** (LT **804.040.494** waarvan bank **791.081.244** + lease 7.188.944 + other 5.770.307; ST **123.907.544** waarvan LT-due 64.892.087 + leveranciers **40.578.108 JUMP** vs 10.435.829; related-party FSO-seam **692.009.832**); omzet **242.736.979 JUMP** vs 199.983.337 (elek **192.454.099** / gas **46.691.078** / other **3.591.802**; geo empty); othops **48.348.893** (740 empty); goods **103.810.208**; diensten **88.697.404** vs 90.114.995; pers **empty / 0 VTE**; afschr 48.433.249; expl **+37.004.700** vs +21.315.034; fin opbr 9.190.325; fin kosten 23.121.533; tax 5.381.478; PnL **+17.698.095** vs +5.734.582; dividend **9.036.900 DROP** vs 14.260.886; bruto capex jaarverslag **133.322.000**; commissaris 12.378 + extra 41.899; bestuurders 15.305. Jaarverslag same PDF: 21 vennoten; WACC/kapitaalkost 5,2% vs 3,5%; nettarief gezin elek **436** vs 314 / gas **244** vs 229; Affligem exited to Fluvius Halle-Vilvoorde 01.01.2025; 8 DNB left in Vlaanderen.
- CSVs: sources+4/entities+1/budgets+81/commitments+1/leaderboard+1 + FOI ready `gap_intg_omzet_242_74m_diensten_88_70m_debt_946_63m_l5` (not sent); rq_1382=done; spawn rq_1383; ticks=1382.
- Coverage: residual dual L5 (INTERGEM leftover energy IGS live WVV). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs Fluvius EG possible. No progress refresh (not every-10; next 1390).
- Next: rq_1383 residual dual L5 VL JR2025 hole_fill (prefer leftover other Fluvius DNB holdings Imewo / Kempen-Iveka / West-Gaselwest / Antwerpen / Halle-Vilvoorde / Limburg / Zenne-Dijle if a 2025 CDN/JR PDF still live and unmined; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; leftover Nuhma daughters Otary RS CDN 2026-00254280 / Rematics / Sunfin only if taken after leftover IGS/EVA/AGB; leftover APB POA / TPA / De Schorre / Warande / PIH / Inovant / Atlas only if a real PDF downloads; IVAREM only if a 2025 JR PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek/Brasschaat GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353 / IVBO 1352 / SOLVA 1351 / Interwaas 1350 / Aquaduin 1349 / Creat 1348 / IVIO 1347 / WVI 1346 / IVVO 1345 / ILvA 1344 / IVM 1343 / IDM 1342 / IGEAN 1341 / EVA LSM 1340 / Westtoer / AGB MAC 1270 unless a fetchable JR appears).
"""
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1382 write done")


if __name__ == "__main__":
    main()

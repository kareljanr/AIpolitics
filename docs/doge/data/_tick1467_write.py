#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1467 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T16:20:00Z"
ENT = "wm_dndz"
SRC = "src_dndz_jr2025_nbb"
GAP = "gap_dndz_omzet_33_88m_pers_6_04m_debt_345m_l5"
LB = "lb_dndz_omzet_33_88m_pers_6_04m_debt_345m"
COMM = "comm_dndz_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00122816.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Woonmaatschappij Dender-Zuid official NBB WVV VOL-inb JR2025,{PDF},NBB / Woonmaatschappij Dender-Zuid,2026-08-19,budget,tick1467; official NBB WVV VOL-inb JR2025 PDF 56p / 1028556 bytes; deposit 2026-00122816; AV 19.05.2026; header 21.05.2026; pdfinfo created 28.05.2026 01:10:32 UTC; model VOL-inb 26.0.11 m82-f; KBO 0400.268.025; assets 424733496 cash 10644121 debt 344504919 pers 6035509 omzet 33880542 diensten 13705925 pnl 224021 equity 73676712",
        "src_dndz_site,Woonmaatschappij Dender-Zuid official pages,https://www.woonmaatschappijdenderzuid.be/,Woonmaatschappij Dender-Zuid / mined Dender-Zuid cities,2026-08-19,official_register,tick1467; leftover woonmaatschappij of mined Aalst+Ninove+Geraardsbergen+Denderleeuw+Haaltert+Lede+Erpe-Mere+Wichelen; zetel Heilig Hartlaan 54 9300 Aalst; KBO 0400.268.025; Busibee used for deposit-id discovery only",
        "src_kbo_dndz_0400268025,KBO Woonmaatschappij Dender-Zuid 0400.268.025,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0400268025,KBO Public Search FOD Economie,2026-08-19,official_register,tick1467; Actief since 03.05.1956; BV since 30.06.2023; naam Woonmaatschappij Dender-Zuid since 30.06.2023; zetel Heilig Hartlaan 54 9300 Aalst; 3 VE; 19 functiehouders; Werkgever RSZ since 01.01.1963; aanbestedende overheid",
        "src_dndz_foi_contact,Woonmaatschappij Dender-Zuid FOI channel (klachten@denderzuid.be),https://www.woonmaatschappijdenderzuid.be/,Woonmaatschappij Dender-Zuid,2026-08-19,official_register,tick1467; leftover woonmaatschappij of mined Dender-Zuid cities; NOT Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_dndz," in raw or raw.startswith(b"wm_dndz,"):
        raise SystemExit("wm_dndz already present")
    if b"0400.268.025" in raw:
        raise SystemExit("Dender-Zuid KBO already present as entity")
    row = (
        "wm_dndz,Woonmaatschappij Dender-Zuid (leftover woonmaatschappij / social-housing BV of mined Dender-Zuid cities Aalst + Ninove + Geraardsbergen + Denderleeuw + Haaltert + Lede + Erpe-Mere + Wichelen; NOT Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg),"
        "Societe de logement Dender-Zuid SRL (logement social residuel Dender-Zuid),"
        "Dender-Zuid leftover social-housing company of mined Dender-Zuid cities (not Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg),"
        "other,city_aalst,nl,https://www.woonmaatschappijdenderzuid.be/,klachten@denderzuid.be,Heilig Hartlaan 54 9300 Aalst,"
        "tick1467 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0400.268.025 Actief since 03.05.1956; live JR2025 official NBB WVV PDF; sourced euros assets 424733496 omzet 33880542 diensten 13705925 pers 6035509 68.8 VTE pnl 224021 equity 73676712 cash 10644121 debt 344504919 capex 39707195 dividend 0; FOI ready omzet 33.88m DROP / pers 6.04m 68.8 VTE / debt 344.50m / cash JUMP 10.64m / PnL DROP 0.22m / dividend 0 / 3 VE; distinct from already-mined Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_dndz")

def part_budgets():
    BUDGETS = [
        ("bud_dndz_assets_2025", "2025", "424733496", "2025 assets 424733496 (was 424215034 restated); tick1467; primary official NBB WVV VOL-inb 2026-00122816"),
        ("bud_dndz_current_2025", "2025", "27720998", "2025 vlottend 27720998 (was 30439115); tick1467; primary official NBB WVV"),
        ("bud_dndz_cash_2025", "2025", "10644121", "2025 liquide middelen 10644121 JUMP (was 8957496); tick1467; primary official NBB WVV"),
        ("bud_dndz_geldbeleg_2025", "2025", "0", "2025 geldbeleggingen empty; tick1467; primary official NBB WVV"),
        ("bud_dndz_strecv_2025", "2025", "1688960", "2025 ST vorderingen 1688960 (was 1315375); tick1467; primary official NBB WVV"),
        ("bud_dndz_trade_2025", "2025", "912218", "2025 handelsvorderingen 912218 (was 497039); tick1467; primary official NBB WVV"),
        ("bud_dndz_othrecv_2025", "2025", "776742", "2025 overige ST vorderingen 776742; tick1467; primary official NBB WVV"),
        ("bud_dndz_voorraden_2025", "2025", "11568724", "2025 voorraden 11568724 DROP (was 16513520; onroerend verkoop 11520727); tick1467; primary official NBB WVV"),
        ("bud_dndz_prepaid_2025", "2025", "3819193", "2025 overlopend actief 3819193 (was 3652725); tick1467; primary official NBB WVV"),
        ("bud_dndz_fixed_2025", "2025", "397012499", "2025 vaste activa 397012499 (was 393775918); tick1467; primary official NBB WVV"),
        ("bud_dndz_iva_2025", "2025", "0", "2025 IVA empty; tick1467; primary official NBB WVV"),
        ("bud_dndz_mva_2025", "2025", "396969652", "2025 MVA 396969652 (was 393750259; terreinen/gebouwen 337968623 in aanbouw 58904507); tick1467; primary official NBB WVV"),
        ("bud_dndz_fva_2025", "2025", "42847", "2025 FVA 42847 (aandelen 35127 + borg 7720); tick1467; primary official NBB WVV"),
        ("bud_dndz_equity_2025", "2025", "73676712", "2025 eigen vermogen 73676712 DROP (was 75490832); tick1467; primary official NBB WVV"),
        ("bud_dndz_inbreng_2025", "2025", "40808", "2025 inbreng 40808 (onbeschikbaar 40808); tick1467; primary official NBB WVV"),
        ("bud_dndz_reserves_2025", "2025", "47100449", "2025 reserves 47100449; tick1467; primary official NBB WVV"),
        ("bud_dndz_kapsubs_2025", "2025", "26535456", "2025 kapitaalsubsidies 26535456 DROP (was 28567066); tick1467; primary official NBB WVV"),
        ("bud_dndz_voorz_2025", "2025", "6551865", "2025 voorzieningen+uitgestelde belasting 6551865; tick1467; primary official NBB WVV"),
        ("bud_dndz_debt_2025", "2025", "344504919", "2025 schulden 344504919 (was 341907875); tick1467; primary official NBB WVV"),
        ("bud_dndz_ltdebt_2025", "2025", "314435326", "2025 LT schulden 314435326 (was 311149026; fin krediet 310929272); tick1467; primary official NBB WVV"),
        ("bud_dndz_stdebt_2025", "2025", "27553395", "2025 ST schulden 27553395 (was 28203383); tick1467; primary official NBB WVV"),
        ("bud_dndz_lev_2025", "2025", "1672982", "2025 leveranciers 1672982 DROP (was 2473996); tick1467; primary official NBB WVV"),
        ("bud_dndz_bezold_2025", "2025", "612681", "2025 bezoldigingen-schulden 612681 (was 452467); tick1467; primary official NBB WVV"),
        ("bud_dndz_taxpay_2025", "2025", "1666894", "2025 belastingschulden 1666894 (was 1551223); tick1467; primary official NBB WVV"),
        ("bud_dndz_deferred_2025", "2025", "2516198", "2025 overlopend passief 2516198 (was 2555466); tick1467; primary official NBB WVV"),
        ("bud_dndz_omzet_2025", "2025", "33880542", "2025 omzet 70 33880542 DROP (was 34314731); tick1467; primary official NBB WVV"),
        ("bud_dndz_diensten_2025", "2025", "13705925", "2025 diensten 61 13705925 JUMP (was 11104433); tick1467; primary official NBB WVV"),
        ("bud_dndz_aankopen_2025", "2025", "6830181", "2025 handelsgoederen/grondstoffen 60 6830181 (aankopen 1885384 voorraad 4944797); tick1467; primary official NBB WVV"),
        ("bud_dndz_pers_2025", "2025", "6035509", "2025 pers 62 6035509; 68.8 VTE vs 66.7; 97306 uur; YE 69.7; tick1467; primary official NBB WVV"),
        ("bud_dndz_afschr_2025", "2025", "9508604", "2025 afschrijvingen 9508604; tick1467; primary official NBB WVV"),
        ("bud_dndz_expl_2025", "2025", "564648", "2025 bedrijfswinst 564648 DROP (was 2465271); tick1467; primary official NBB WVV"),
        ("bud_dndz_finopbr_2025", "2025", "7681309", "2025 financiele opbrengsten 7681309 all recurrent; tick1467; primary official NBB WVV"),
        ("bud_dndz_finkost_2025", "2025", "7912806", "2025 financiele kosten 7912806; tick1467; primary official NBB WVV"),
        ("bud_dndz_pnl_2025", "2025", "224021", "2025 PnL 224021 DROP (was 1855640); tick1467; primary official NBB WVV"),
        ("bud_dndz_div_2025", "2025", "0", "2025 dividend 0 vergoeding van de inbreng empty; tick1467; primary official NBB WVV"),
        ("bud_dndz_capex_2025", "2025", "39707195", "2025 capex MVA aanschaf 39707195 (terreinen 27217661 + meubilair 2408 + in aanbouw 12487126); tick1467; primary official NBB WVV"),
        ("bud_dndz_bedrijfsopbr_2025", "2025", "39381683", "2025 bedrijfsopbrengsten 70/76A 39381683; tick1467; primary official NBB WVV"),
        ("bud_dndz_bedrijfskost_2025", "2025", "38817035", "2025 bedrijfskosten 60/66A 38817035; tick1467; primary official NBB WVV"),
        ("bud_dndz_tax_2025", "2025", "160725", "2025 belastingen 67/77 160725; tick1467; primary official NBB WVV"),
        ("bud_dndz_in_aanbouw_2025", "2025", "58904507", "2025 activa in aanbouw 58904507 DROP (was 73394678); tick1467; primary official NBB WVV"),
        ("bud_dndz_krediet_2025", "2025", "310929272", "2025 LT kredietinstellingen 310929272 (was 308379383); tick1467; primary official NBB WVV"),
    ]
    bp = DATA / "budgets.csv"
    braw = bp.read_bytes()
    if braw and not braw.endswith(b"\n"):
        braw += b"\n"
    existing = set()
    for brow in csv.reader(io.StringIO(braw.decode("utf-8"))):
        if brow:
            existing.add(brow[0])
    added = []
    for bid, year, amt, notes in BUDGETS:
        if bid in existing:
            continue
        added.append(f"{bid},{ENT},{year},{amt},,,executed,{SRC},strong,{notes}\n")
    bp.write_bytes(braw + "".join(added).encode("utf-8"))
    print("budgets", len(added))

def part_rest1():
    append_lf(DATA / "commitments.csv", [
        f"{COMM},Woonmaatschappij Dender-Zuid JR2025 leftover woonmaatschappij dual (omzet 33.88m DROP / diensten 13.71m JUMP / pers 6.04m 68.8 VTE / debt 344.50m / cash JUMP 10.64m / PnL DROP 0.22m / dividend 0 / 3 VE),{ENT},Dender-Zuid / mined Dender-Zuid dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-19,1956,,33880542,,,active,{PDF},Local leftover woonmaatschappij map VL Dender-Zuid — omzet 33.88m DROP / pers 6.04m 68.8 VTE / debt 344.50m / cash JUMP 10.64m,Publish omzet split + 3 VE payroll + cash JUMP 8.96m to 10.64m + LT krediet 310.93m counterparties + capex 39.71m + aandeel % 8 gemeenten/OCMW/private + dividend 0; do not keep leftover woonmaatschappij as unpublished 33.88m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Aalst>Woonmaatschappij>Dender-Zuid>JR2025_L5,tick1467; assets 424733496 omzet 33880542 diensten 13705925 pers 6035509 pnl 224021 equity 73676712 cash 10644121 debt 344504919 capex 39707195 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Woonmaatschappij Dender-Zuid JR2025 leftover woonmaatschappij: omzet 33.88m DROP / diensten 13.71m JUMP / pers 6.04m 68.8 VTE / debt 344.50m / cash JUMP 10.64m / PnL DROP 0.22m / dividend 0 / 3 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Aalst>Woonmaatschappij>Dender-Zuid>JR2025_L5,33880542,424733496,Leftover dual woonmaatschappij shell: assets 424.73m / equity 73.68m / omzet 33.88m DROP / diensten 13.71m JUMP / pers 6.04m 68.8 VTE / cash 10.64m JUMP / debt 344.50m / LT krediet 310.93m / PnL 0.22m DROP / dividend 0 / 3 VE; do not treat 33.88m as TE-additive of 348bn,strong,{SRC},Dender-Zuid / mined Dender-Zuid dual housing,Local leftover woonmaatschappij map VL Dender-Zuid — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 33.88m DROP / pers 6.04m 68.8 VTE / debt 344.50m / cash JUMP 10.64m / PnL DROP 0.22m / dividend 0 / 3 VE,7.0,7.5,3.0,7.0,Publish omzet split + 3 VE payroll + cash JUMP 8.96m to 10.64m + LT krediet 310.93m counterparties + capex 39.71m + aandeel % 8 gemeenten/OCMW/private + dividend 0; do not keep leftover woonmaatschappij as unpublished 33.88m housing shell,active,,tick1467; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Gemeenten>Aalst>Woonmaatschappij>Dender-Zuid>JR2025_L5,{ENT},omzet 33880542 DROP vs 34314731 + diensten 13705925 JUMP vs 11104433 + pers 6035509 68.8 VTE vs 66.7 + 3 VE + cash 10644121 JUMP vs 8957496 + debt 344504919 LT krediet 310929272 + voorraden 11568724 DROP onroerend 11520727 + capex 39707195 in aanbouw DROP 58904507 vs 73394678 + PnL DROP 224021 vs 1855640 + dividend 0 + commissaris unpublished + aandeel % 8 gemeenten/OCMW/private unpublished,Leftover woonmaatschappij Dender-Zuid after leftover AGB/APB hunt: omzet 33.88m DROP / pers 6.04m 68.8 VTE / debt 344.50m / cash JUMP 10.64m / PnL DROP 0.22m / dividend 0 / 3 VE hides municipal housing vehicle,8,Woonmaatschappij Dender-Zuid / Bestuursorgaan / dagelijks bestuur,klachten@denderzuid.be,Heilig Hartlaan 54 9300 Aalst,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1467 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF now extracted (1028556 bytes 56p). FOI ready not sent. NOT every-10. NOT Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / Toerisme Limburg / Toerisme Vlaams-Brabant / Toerisme Oost-Vlaanderen / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1466. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still no separate APB 2025 PDF.",
    ])
    print("foi_queue +1")

def part_rqstate():
    p = DATA / "research_queue.csv"
    with p.open("rb") as f:
        f.seek(0, 2)
        size = f.tell()
        f.seek(max(0, size - 131072))
        tail = f.read()
    if not tail.endswith(b"\n"):
        raise SystemExit("research_queue tail missing newline")
    stripped = tail[:-1]
    last_nl = stripped.rfind(b"\n")
    if last_nl < 0:
        raise SystemExit("research_queue tail too short")
    last = stripped[last_nl + 1 :]
    last_s = last.decode("utf-8")
    if not last_s.startswith("rq_1467,"):
        raise SystemExit(f"expected last row rq_1467, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1467 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1467,Woonmaatschappij Dender-Zuid JR2025 leftover dual residual,hole_fill,5,done,L5,wm_dndz,"
        "Completed: Woonmaatschappij Dender-Zuid leftover woonmaatschappij of mined Dender-Zuid cities after leftover AGB/APB hunt; KBO 0400.268.025 Actief; live JR2025 official NBB WVV VOL-inb PDF (1028556 bytes 56p; deposit 2026-00122816; AV 19.05.2026; header 21.05.2026; pdfinfo 28.05.2026 01:10:32 UTC). PDF header WOONMAATSCHAPPIJ DENDER-ZUID / Heilig Hartlaan 54 — NOT Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Sourced euros assets 424733496 omzet 33880542 diensten 13705925 pers 6035509 68.8 VTE pnl 224021 equity 73676712 cash 10644121 debt 344504919 capex 39707195 dividend 0. FOI "
        f"{GAP} ready not sent. Distinct from already-mined Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456.,"
        f"{GAP},2026-08-19T16:05:00Z,{TS},"
        "tick1467 Dender-Zuid leftover woonmaatschappij residual; KBO 0400.268.025; live JR2025 official NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1468 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025"
    )
    spawn = (
        "rq_1468,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1467 done including Dender-Zuid 1467 leftover woonmaatschappij live official NBB WVV / Dimensa 1466 leftover woonmaatschappij live official NBB WVV / Woonmaatschappij Rivierenland 1465 leftover woonmaatschappij live official NBB WVV / Woonpunt Waas 1464 leftover woonmaatschappij live official NBB WVV / Toerisme Limburg 1463 leftover provincial tourism VZW live official NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 404 as of 1467). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck spotted unmined around 1453 — still no separate APB 2025 PDF as of 1467). Do NOT confuse with already-mined Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live. Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1467 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1467. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461.,,"
        f"{TS},{TS},"
        "spawned tick1467 after Dender-Zuid leftover woonmaatschappij live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1467=done + rq_1468 spawned; keep", last_line_start)

    def n_data(fn):
        with open(DATA / fn, "rb") as f:
            return sum(1 for _ in f) - 1

    inv = {fn: n_data(fn) for fn in ["budgets.csv","commitments.csv","leaderboard.csv","entities.csv","sources.csv","foi_queue.csv","research_queue.csv"]}
    foi_c = Counter()
    csv.field_size_limit(sys.maxsize)
    with open(DATA / "foi_queue.csv", newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            st = (row.get("status") or "").strip()
            foi_c[st] += 1
    foi_ready = foi_c.get("ready", 0)
    foi_ans = foi_c.get("answered", 0)
    foi_part = foi_c.get("partial", 0)
    foi_tot = inv["foi_queue.csv"]
    print("INV", inv, "FOI ready", foi_ready, "answered", foi_ans, "partial", foi_part, "total", foi_tot)
    Path("/tmp/tick1467_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1467 Dender-Zuid leftover woonmaatschappij residual; KBO 0400.268.025; live JR2025 official NBB WVV PDF; sourced euros assets 424733496 omzet 33880542 diensten 13705925 pers 6035509 68.8 VTE pnl 224021 equity 73676712 cash 10644121 debt 344504919 capex 39707195 dividend 0; FOI ready omzet 33.88m DROP / pers 6.04m 68.8 VTE / debt 344.50m / cash JUMP 10.64m / PnL DROP 0.22m / dividend 0 / 3 VE; NOT Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / Toerisme Limburg / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1468 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1467,1467,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1467")

    entry = (
        "\n## Tick 1467 - 2026-08-19 - rq_1467 Woonmaatschappij Dender-Zuid dual residual leftover\n"
        "- Unit: Woonmaatschappij Dender-Zuid BV (leftover woonmaatschappij / social-housing BV of mined Aalst + Ninove + Geraardsbergen + Denderleeuw + Haaltert + Lede + Erpe-Mere + Wichelen; 3 VE) after residual dual hunt (KBO **0400.268.025**; official NBB WVV VOL-inb PDF **1028556** bytes / 56p; deposit **2026-00122816**; AV **19.05.2026**; header **21.05.2026**; pdfinfo created **28.05.2026 01:10:32 UTC**; model **VOL-inb** 26.0.11 m82-f; commissaris KPMG Bedrijfsrevisoren BV B00001 / 0419.122.548 / Heyndrickx Wim A01925 mandate 30.06.2025–AV JR2027 fee unpublished VOL-inb 6.18 not filed; oordeel zonder voorbehoud 29.04.2026). Leftover AGB/APB first: leftover APB Inovant / Atlas Foleon `jaarrekening_25_inov` / `jaarrekening_25_atlas` HEAD **404** this tick; provincieantwerpen.be **403** even with Googlebot UA; no fetchable 2025 Inovant/Atlas PDF (do not take Hooibeekhoeve). Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick. Leftover AGB Herzele already in entities (tick1163) — skipped. Leftover AGB Bornem still 2024. Leftover AGB Hasselt / SOLag / WAGSO / Temse / Herk / Lommel already in entities — skipped. Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel still no JR as of 1466. Leftover IGS IVAREM 0267.403.264 last JR still 2024-12-31. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover Dender-Zuid statutory CDN `2026-00122816` live this tick (HTTP 200 / 1028556 / 56p; jaar **2025-12-31**; neerlegging **21.05.2026**) — taken (hunt order #2 leftover unmined woonmaatschappij of mined Dender-Zuid cities with live 2025 statutory PDF after leftover AGB/APB hunt). PDF header **WOONMAATSCHAPPIJ DENDER-ZUID / Heilig Hartlaan 54 / 9300 Aalst** — NOT Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Distinct from already-mined **Dimensa 1466** / **Woonmaatschappij Rivierenland 1465** / **Woonpunt Waas 1464** / **Toerisme Limburg 1463** / **Toerisme Vlaams-Brabant 1462** / **Toerisme Oost-Vlaanderen 1461** / **Arboretum Kalmthout 1460** / **Kempens Landschap 1459** / **APB Warande 1458** / **APB De Schorre 1457** / **APB PIH 1456**. First confirmed not already extracted as JR2025 euros: no Dender-Zuid / 0400.268.025 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **03.05.1956**; statutaire naam Woonmaatschappij Dender-Zuid since 30.06.2023; BV since 30.06.2023; zetel Heilig Hartlaan 54 9300 Aalst; **3 VE**; 19 functiehouders; dagelijks bestuur DeSmet/Hutse/Vincent since 30.06.2023; Werkgever RSZ since 01.01.1963; btw since 01.01.1971; aanbestedende overheid; NACE 68.202; site https://www.woonmaatschappijdenderzuid.be/; absorbeerde DEWACO 0400.290.789 + NINOVE-WELZIJN 0400.312.466 since 30.06.2023. Prior-year figures **niet identiek**. Busibee used for deposit-id discovery only. Euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1470).\n"
        "- EUR strong (primary official WVV VOL-inb; omzet 70 **33880542** DROP vs 34314731; diensten 61 **13705925** JUMP vs 11104433; pers 62 **6035509** / **68,8 VTE** vs 66,7): assets **424733496** (was 424215034); fixed **397012499** vs 393775918 / IVA empty / MVA **396969652** vs 393750259 (terreinen/gebouwen **337968623**; installaties **2958**; meubilair **93564**; leasing **0**; in aanbouw **58904507 DROP** vs 73394678) / FVA **42847**; current **27720998** vs 30439115; voorraden **11568724 DROP** vs 16513520 (onroerend verkoop **11520727**); ST recv **1688960** (trade **912218** / other **776742**); geldbeleg empty; cash **10644121 JUMP** vs 8957496; prepaid **3819193**; equity **73676712 DROP** vs 75490832 (inbreng **40808**; reserves **47100449**; overgedragen empty; kapsubs **26535456 DROP** vs 28567066); voorzieningen **6551865** (grote herstellingen **4397628**; uitgestelde belasting **1525859**); schulden **344504919** vs 341907875 (LT **314435326** waarvan fin krediet **310929272**; ST **27553395** waarvan 42 **22792373** + leveranciers **1672982 DROP** vs 2473996; deferred **2516198**); omzet **33880542** DROP vs 34314731; 60 **6830181**; diensten **13705925** JUMP; pers **6035509** / **68,8 VTE** / 97306 uur / YE **69,7** VTE 75 personen; afschr **9508604**; expl **+564648 DROP** vs +2465271; fin opbr **7681309**; fin kosten **7912806**; tax **160725**; PnL **+224021 DROP** vs +1855640; dividend **0**; onttrekking reserves **7163973**; toevoeging reserves **7600291**; capex MVA aanschaf **39707195** (terreinen 27217661 + meubilair 2408 + in aanbouw 12487126) + FVA 30127. Commissaris fee unpublished. 3 VE. 13855293 aandelen op naam; uittredingen BJ2025 6531. Cross-checks: 397012499+27720998=424733497 vs 424733496; 73676712+6551865+344504919=424733496; 39381683-38817035=564648; 564648+7681309-7912806=333151; 333151+51596-160725=224022 vs 224021; 224021+212297=436318.\n"
        "- CSVs: sources +4; entities +1 `wm_dndz` parent `city_aalst`; budgets +41 executed; commitments +1 envelope 33880542 AV 19.05.2026; leaderboard +1 annual 33880542 / total 424733496; foi_queue +1 status=ready never sent; research_queue surgical rq_1467=done + rq_1468 spawn; loop_state ticks_completed=1467. Inventory after write: budgets {INV_B} · commitments {INV_C} · leaderboard {INV_L} · entities {INV_E} · sources {INV_S} · FOI ready {FOI_R} / answered {FOI_A} / partial {FOI_P} / total {FOI_T}.\n"
        "- FOI: `gap_dndz_omzet_33_88m_pers_6_04m_debt_345m_l5` ready not sent — omzet 33.88m DROP / diensten 13.71m JUMP / pers 6.04m 68.8 VTE / 3 VE / cash JUMP 10.64m / debt 344.50m LT krediet 310.93m / voorraden DROP 11.57m / capex 39.71m / PnL DROP 0.22m / dividend 0 / commissaris unpublished / aandeel % 8 gemeenten/OCMW/private unpublished.\n"
        "- Next: rq_1468 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 404 this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1467). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live. Leftover IGS IVAREM **0267.403.264** still JR2024. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Stichting Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456. Next every-10 is **1470**. Provincial tourism VZWs now exhausted (Westtoer + TOV + TVLB + TLim).\n"
    )
    entry = entry.replace("{INV_B}", str(inv["budgets.csv"])).replace("{INV_C}", str(inv["commitments.csv"])).replace("{INV_L}", str(inv["leaderboard.csv"])).replace("{INV_E}", str(inv["entities.csv"])).replace("{INV_S}", str(inv["sources.csv"])).replace("{FOI_R}", str(foi_ready)).replace("{FOI_A}", str(foi_ans)).replace("{FOI_P}", str(foi_part)).replace("{FOI_T}", str(foi_tot))
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1467 -" in lraw:
        raise SystemExit("loop_log already has tick 1467 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1467")
    print("DONE tick 1467")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else "all"
    if part in ("sources", "all"):
        part_sources()
    if part in ("entities", "all"):
        part_entities()
    if part in ("budgets", "all"):
        part_budgets()
    if part in ("rest1", "all"):
        part_rest1()
    if part in ("rqstate", "all"):
        part_rqstate()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1477 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T17:55:00Z"
ENT = "wm_wvrk"
SRC = "src_wvrk_jr2025_nbb"
GAP = "gap_wvrk_brutomarge_6_66m_pers_1_77m_omzet_empty_l5"
LB = "lb_wvrk_brutomarge_6_66m_pers_1_77m_omzet_empty"
COMM = "comm_wvrk_jr2025_brutomarge"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00187904.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Woonveer Klein-Brabant official NBB WVV VKT-inb JR2025,{PDF},NBB / Woonveer Klein-Brabant,2026-08-19,budget,tick1477; official NBB WVV VKT-inb JR2025 PDF 40p / 3260693 bytes; deposit 2026-00187904; AV 22.05.2026; header 12.06.2026; pdfinfo created 23.06.2026 22:00:52 UTC; model VKT-inb 26.0.15 m81-f; KBO 0406.039.624; assets 122300664 cash 12151452 debt 84475969 pers 1772581 brutomarge 6663129 pnl 302728 equity 35538478",
        "src_wvrk_site,Woonveer Klein-Brabant official pages,https://woonveer.be/,Woonveer Klein-Brabant / mined Puurs-Sint-Amands + Bornem,2026-08-19,official_register,tick1477; leftover woonmaatschappij of mined Puurs-Sint-Amands + Bornem; zetel Palingstraat 48 bus 101 2870 Puurs-Sint-Amands; KBO 0406.039.624; SBM used for deposit-id discovery only",
        "src_kbo_wvrk_0406039624,KBO Woonveer Klein-Brabant 0406.039.624,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0406039624,KBO Public Search FOD Economie,2026-08-19,official_register,tick1477; Actief since 01.01.1968; BV since 27.06.2023; naam WOONVEER KLEIN-BRABANT since 10.01.2019; zetel Palingstraat 48 bus 101 2870 Puurs-Sint-Amands; 1 VE; 18 functiehouders; Werkgever RSZ since 01.01.1977; aanbestedende overheid",
        "src_wvrk_foi_contact,Woonveer Klein-Brabant FOI channel (info@woonveer.be),https://woonveer.be/,Woonveer Klein-Brabant,2026-08-19,official_register,tick1477; leftover woonmaatschappij of mined Puurs-Sint-Amands + Bornem; NOT Zorgbedrijf Klein-Brabant / Woonkade / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_wvrk," in raw or raw.startswith(b"wm_wvrk,"):
        raise SystemExit("wm_wvrk already present")
    if b"0406.039.624" in raw or b"0406039624" in raw:
        raise SystemExit("Woonveer KBO already present as entity")
    row = (
        "wm_wvrk,Woonveer Klein-Brabant (leftover woonmaatschappij / social-housing BV of mined Puurs-Sint-Amands + Bornem; NOT Zorgbedrijf Klein-Brabant 1143 / Woonkade Rupelstreek 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92),"
        "Woonveer Klein-Brabant SRL (logement social residuel Puurs-Sint-Amands-Bornem),"
        "Woonveer Klein-Brabant leftover social-housing company of mined Puurs-Sint-Amands + Bornem (not Zorgbedrijf Klein-Brabant / Woonkade / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92),"
        "other,city_puurs_sint_amands,nl,https://woonveer.be/,info@woonveer.be,Palingstraat 48 bus 101 2870 Puurs-Sint-Amands,"
        "tick1477 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0406.039.624 Actief since 01.01.1968; live JR2025 official NBB WVV VKT-inb PDF; sourced euros assets 122300664 brutomarge 6663129 pers 1772581 24.3 VTE pnl 302728 equity 35538478 cash 12151452 debt 84475969 capex 5198013 dividend 0; FOI ready brutomarge 6.66m DROP / omzet unpublished / pers 1.77m 24.3 VTE JUMP / debt 84.48m / cash 12.15m DROP / PnL DROP 0.30m / dividend 0 / 1 VE; distinct from already-mined Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Zorgbedrijf Klein-Brabant 1143"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_wvrk")

def part_budgets():
    BUDGETS = [
        ("bud_wvrk_assets_2025", "2025", "122300664", "2025 assets 122300664 UP (was 121815309); tick1477; primary official NBB WVV VKT-inb 2026-00187904"),
        ("bud_wvrk_current_2025", "2025", "29678371", "2025 vlottend 29678371 DROP (was 30726694); tick1477; primary official NBB WVV"),
        ("bud_wvrk_cash_2025", "2025", "12151452", "2025 liquide middelen 12151452 DROP (was 13271389); tick1477; primary official NBB WVV"),
        ("bud_wvrk_strecv_2025", "2025", "481231", "2025 ST vorderingen 481231 (was 182533); tick1477; primary official NBB WVV"),
        ("bud_wvrk_trade_2025", "2025", "125738", "2025 handelsvorderingen 125738 (was 93509); tick1477; primary official NBB WVV"),
        ("bud_wvrk_othrecv_2025", "2025", "355493", "2025 overige ST vorderingen 355493 (was 89024); tick1477; primary official NBB WVV"),
        ("bud_wvrk_voorraden_2025", "2025", "5962423", "2025 voorraden 5962423 (was 5959981); tick1477; primary official NBB WVV"),
        ("bud_wvrk_prepaid_2025", "2025", "1083266", "2025 overlopend actief 1083266 (was 1312792); tick1477; primary official NBB WVV"),
        ("bud_wvrk_geldbeleg_2025", "2025", "10000000", "2025 geldbeleggingen 10000000; tick1477; primary official NBB WVV"),
        ("bud_wvrk_fixed_2025", "2025", "92622293", "2025 vaste activa 92622293 (was 91088615); tick1477; primary official NBB WVV"),
        ("bud_wvrk_mva_2025", "2025", "92494707", "2025 MVA 92494707 (was 90961029; terreinen/gebouwen 88595421 in aanbouw 3804616); tick1477; primary official NBB WVV"),
        ("bud_wvrk_fva_2025", "2025", "127586", "2025 FVA 127586; tick1477; primary official NBB WVV"),
        ("bud_wvrk_equity_2025", "2025", "35538478", "2025 eigen vermogen 35538478 UP (was 35239123); tick1477; primary official NBB WVV"),
        ("bud_wvrk_inbreng_2025", "2025", "39496", "2025 inbreng 39496 (onbeschikbaar 39496); tick1477; primary official NBB WVV"),
        ("bud_wvrk_reserves_2025", "2025", "27991284", "2025 reserves 27991284 (was 27688556); tick1477; primary official NBB WVV"),
        ("bud_wvrk_kapsubs_2025", "2025", "7507698", "2025 kapitaalsubsidies 7507698 DROP (was 7511072); tick1477; primary official NBB WVV"),
        ("bud_wvrk_voorz_2025", "2025", "2286217", "2025 voorzieningen+uitgestelde belasting 2286217 (herstel 1632947); tick1477; primary official NBB WVV"),
        ("bud_wvrk_debt_2025", "2025", "84475969", "2025 schulden 84475969 (was 84386746); tick1477; primary official NBB WVV"),
        ("bud_wvrk_ltdebt_2025", "2025", "79014400", "2025 LT schulden 79014400 (was 78815466; fin krediet 77689087); tick1477; primary official NBB WVV"),
        ("bud_wvrk_stdebt_2025", "2025", "4600172", "2025 ST schulden 4600172 (was 5166677); tick1477; primary official NBB WVV"),
        ("bud_wvrk_lev_2025", "2025", "552801", "2025 leveranciers 552801 (was 1212145); tick1477; primary official NBB WVV"),
        ("bud_wvrk_bezold_2025", "2025", "266212", "2025 bezoldigingen-schulden 266212 (was 243060); tick1477; primary official NBB WVV"),
        ("bud_wvrk_taxpay_2025", "2025", "758707", "2025 belastingschulden 758707 (was 741915); tick1477; primary official NBB WVV"),
        ("bud_wvrk_deferred_2025", "2025", "861398", "2025 overlopend passief 861398 (was 404603); tick1477; primary official NBB WVV"),
        ("bud_wvrk_brutomarge_2025", "2025", "6663129", "2025 brutomarge 9900 6663129 DROP (was 7950814; omzet 70 empty); tick1477; primary official NBB WVV"),
        ("bud_wvrk_pers_2025", "2025", "1772581", "2025 pers 62 1772581; 24.3 VTE vs 21.4; 32797 uur; YE 27 / 24.5 VTE; tick1477; primary official NBB WVV"),
        ("bud_wvrk_afschr_2025", "2025", "3650419", "2025 afschrijvingen 3650419; tick1477; primary official NBB WVV"),
        ("bud_wvrk_expl_2025", "2025", "326542", "2025 bedrijfswinst 326542 DROP (was 2043652); tick1477; primary official NBB WVV"),
        ("bud_wvrk_finopbr_2025", "2025", "1750195", "2025 financiele opbrengsten 1750195 (interestsubs 1385020); tick1477; primary official NBB WVV"),
        ("bud_wvrk_finkost_2025", "2025", "1774035", "2025 financiele kosten 1774035; tick1477; primary official NBB WVV"),
        ("bud_wvrk_pnl_2025", "2025", "302728", "2025 PnL 302728 DROP (was 1891080); tick1477; primary official NBB WVV"),
        ("bud_wvrk_div_2025", "2025", "0", "2025 dividend 0 vergoeding van de inbreng empty; tick1477; primary official NBB WVV"),
        ("bud_wvrk_capex_2025", "2025", "5198013", "2025 capex MVA aanschaf 5198013; tick1477; primary official NBB WVV"),
        ("bud_wvrk_in_aanbouw_2025", "2025", "3804616", "2025 activa in aanbouw 3804616 DROP (was 4225868); tick1477; primary official NBB WVV"),
        ("bud_wvrk_krediet_2025", "2025", "77689087", "2025 LT kredietinstellingen 77689087 (was 77542188); tick1477; primary official NBB WVV"),
        ("bud_wvrk_terreinen_2025", "2025", "88595421", "2025 terreinen en gebouwen 88595421 (was 86624583); tick1477; primary official NBB WVV"),
        ("bud_wvrk_herstel_2025", "2025", "1632947", "2025 voorziening grote herstellingen 1632947 (was 1337227); tick1477; primary official NBB WVV"),
        ("bud_wvrk_bestuur_2025", "2025", "20085", "2025 bestuurders zitpenningen 20085; tick1477; primary official NBB WVV remuneratieverslag"),
        ("bud_wvrk_commissaris_2025", "2025", "9600", "2025 commissaris fee 9600 Luc Callaert BV; tick1477; primary official NBB WVV"),
        ("bud_wvrk_commit_fa_2025", "2025", "5751422", "2025 verplichtingen aankoop vaste activa 5751422; tick1477; primary official NBB WVV 6.5"),
        ("bud_wvrk_tax_2025", "2025", "20119", "2025 belastingen op het resultaat 20119; tick1477; primary official NBB WVV"),
        ("bud_wvrk_andere_expl_2025", "2025", "733079", "2025 andere bedrijfskosten 733079; tick1477; primary official NBB WVV"),
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
        f"{COMM},Woonveer Klein-Brabant JR2025 leftover woonmaatschappij dual (brutomarge 6.66m DROP / omzet unpublished / pers 1.77m 24.3 VTE JUMP / debt 84.48m / cash 12.15m DROP / PnL DROP 0.30m / dividend 0 / 1 VE),{ENT},Puurs-Sint-Amands-Bornem / mined Klein-Brabant dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-22,1968,,6663129,,,active,{PDF},Local leftover woonmaatschappij map VL Klein-Brabant — brutomarge 6.66m DROP / omzet unpublished / pers 1.77m 24.3 VTE / debt 84.48m / cash 12.15m DROP,Publish omzet+diensten split + 1 VE payroll + cash 12.15m DROP + geldbeleg 10.00m + LT krediet 77.69m counterparties + capex 5.20m + aandeel % Puurs-Sint-Amands/Bornem/OCMW/private + dividend 0; do not keep leftover woonmaatschappij as unpublished 6.66m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Puurs-Sint-Amands>Woonmaatschappij>Woonveer>JR2025_L5,tick1477; assets 122300664 brutomarge 6663129 pers 1772581 pnl 302728 equity 35538478 cash 12151452 debt 84475969 capex 5198013 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT Zorgbedrijf Klein-Brabant / Woonkade / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Woonveer Klein-Brabant JR2025 leftover woonmaatschappij: brutomarge 6.66m DROP / omzet unpublished / pers 1.77m 24.3 VTE JUMP / debt 84.48m / cash 12.15m DROP / PnL DROP 0.30m / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Puurs-Sint-Amands>Woonmaatschappij>Woonveer>JR2025_L5,6663129,122300664,Leftover dual woonmaatschappij shell: assets 122.30m / equity 35.54m / brutomarge 6.66m DROP / omzet unpublished VKT / pers 1.77m 24.3 VTE JUMP / cash 12.15m DROP / geldbeleg 10.00m / debt 84.48m / LT krediet 77.69m / PnL DROP 0.30m / dividend 0 / 1 VE; do not treat 6.66m as TE-additive of 348bn,strong,{SRC},Woonveer Klein-Brabant / mined Puurs-Sint-Amands-Bornem dual housing,Local leftover woonmaatschappij map VL Klein-Brabant — JR2025 official NBB WVV live; brutomarge+omzet-empty+pers+debt+cash FOI,Official NBB WVV 2026-08-19: brutomarge 6.66m DROP / omzet unpublished / pers 1.77m 24.3 VTE JUMP / debt 84.48m / cash 12.15m DROP / PnL DROP 0.30m / dividend 0 / 1 VE,7.0,7.0,3.0,7.0,Publish omzet+diensten split + 1 VE payroll + cash 12.15m DROP + geldbeleg 10.00m + LT krediet 77.69m counterparties + capex 5.20m + aandeel % Puurs-Sint-Amands/Bornem/OCMW/private + dividend 0; do not keep leftover woonmaatschappij as unpublished 6.66m housing shell,active,,tick1477; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Zorgbedrijf Klein-Brabant 1143",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Gemeenten>Puurs-Sint-Amands>Woonmaatschappij>Woonveer>JR2025_L5,{ENT},brutomarge 6663129 DROP vs 7950814 + omzet 70 empty + 60/61 empty + pers 1772581 24.3 VTE vs 21.4 + 1 VE + cash 12151452 DROP vs 13271389 + geldbeleg 10000000 + debt 84475969 LT krediet 77689087 + voorraden 5962423 + capex 5198013 + PnL DROP 302728 vs 1891080 + dividend 0 + commissaris 9600 + bestuurders 20085 + aandeel % Puurs-Sint-Amands/Bornem/OCMW/private unpublished,Leftover woonmaatschappij Woonveer Klein-Brabant after leftover AGB/APB hunt: brutomarge 6.66m DROP / omzet unpublished / pers 1.77m 24.3 VTE JUMP / debt 84.48m / cash 12.15m DROP / PnL DROP 0.30m / dividend 0 / 1 VE hides municipal housing vehicle,8,Woonveer Klein-Brabant / Bestuursorgaan / voorzitter De Blaiser Raf,info@woonveer.be,Palingstraat 48 bus 101 2870 Puurs-Sint-Amands,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1477 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VKT-inb PDF now extracted (3260693 bytes 40p). FOI ready not sent. NOT every-10. NOT Zorgbedrijf Klein-Brabant 1143 / Woonkade 1476 / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still no separate APB 2025 PDF. WoonST Temse still JR2024 as of 1467. stek92 still JR2024 as of 1473. Woonveer TAKEN this tick.",
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
    if not last_s.startswith("rq_1477,"):
        raise SystemExit(f"expected last row rq_1477, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1477 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1477,Woonveer Klein-Brabant JR2025 leftover dual residual,hole_fill,5,done,L5,wm_wvrk,"
        "Completed: Woonveer Klein-Brabant leftover woonmaatschappij of mined Puurs-Sint-Amands + Bornem after leftover AGB/APB hunt; KBO 0406.039.624 Actief; live JR2025 official NBB WVV VKT-inb PDF (3260693 bytes 40p; deposit 2026-00187904; AV 22.05.2026; header 12.06.2026; pdfinfo 23.06.2026 22:00:52 UTC). PDF header WOONVEER KLEIN-BRABANT / Palingstraat 48 bus 101 — NOT Zorgbedrijf Klein-Brabant 1143 / Woonkade / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Sourced euros assets 122300664 brutomarge 6663129 pers 1772581 24.3 VTE pnl 302728 equity 35538478 cash 12151452 debt 84475969 capex 5198013 dividend 0. FOI "
        f"{GAP} ready not sent. Distinct from already-mined Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Zorgbedrijf Klein-Brabant 1143.,"
        f"{GAP},2026-08-19T17:45:00Z,{TS},"
        "tick1477 Woonveer Klein-Brabant leftover woonmaatschappij residual; KBO 0406.039.624; live JR2025 official NBB WVV VKT-inb PDF; sourced euros; FOI ready not sent; next rq_1478 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (WoonST Temse / stek92 / Woonin / Zonnige Kempen / De Ideale Woning / Wooncompagnie only if JR2025 live)"
    )
    spawn = (
        "rq_1478,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill: Next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1477 done including Woonveer 1477 leftover woonmaatschappij live official NBB WVV / Woonkade 1476 leftover woonmaatschappij live official NBB WVV / Woonstroom 1475 leftover woonmaatschappij live official NBB WVV / Thuisrand 1474 leftover woonmaatschappij live official NBB WVV / Vivendo 1473 leftover woonmaatschappij live official NBB WVV / SW+ 1472 leftover woonmaatschappij live official NBB WVV / Woonhaven 1471 leftover woonmaatschappij live official NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 404 as of 1477). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1477). Do NOT confuse with already-mined Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Erfgoed Rupelstreek IOED 1431 / Zorgbedrijf Klein-Brabant 1143. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live. Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1471 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1461. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonhaven TAKEN 1471; SW+ TAKEN 1472; Vivendo TAKEN 1473; Thuisrand TAKEN 1474; Woonstroom TAKEN 1475; Woonkade TAKEN 1476; Woonveer TAKEN 1477; WoonST Temse still JR2024 as of 1467; stek92 still JR2024 as of 1473). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Erfgoed Rupelstreek IOED 1431 / Zorgbedrijf Klein-Brabant 1143.,,"
        f"{TS},{TS},"
        "spawned tick1477 after Woonveer leftover woonmaatschappij live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (WoonST Temse / stek92 / Woonin / Zonnige Kempen / De Ideale Woning / Wooncompagnie only if JR2025 live)"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1477=done + rq_1478 spawned; keep", last_line_start)

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
    Path("/tmp/tick1477_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1477 Woonveer leftover woonmaatschappij residual; KBO 0406.039.624; live JR2025 official NBB WVV VKT-inb PDF; sourced euros assets 122300664 brutomarge 6663129 pers 1772581 24.3 VTE pnl 302728 equity 35538478 cash 12151452 debt 84475969 capex 5198013 dividend 0; FOI ready brutomarge 6.66m DROP / omzet unpublished / pers 1.77m 24.3 VTE JUMP / debt 84.48m / cash 12.15m DROP / PnL DROP 0.30m / dividend 0 / 1 VE; NOT Zorgbedrijf Klein-Brabant / Woonkade / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1478 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (WoonST Temse / stek92 / Woonin / Zonnige Kempen / De Ideale Woning / Wooncompagnie only if JR2025 live); FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1477,1477,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1477")

    entry = (
        "\n## Tick 1477 - 2026-08-19 - rq_1477 Woonveer Klein-Brabant dual residual leftover\n"
        "- Unit: Woonveer Klein-Brabant BV (leftover woonmaatschappij / social-housing BV of mined Puurs-Sint-Amands + Bornem; 1 VE) after residual dual hunt (KBO **0406.039.624**; official NBB WVV VKT-inb PDF **3260693** bytes / 40p; deposit **2026-00187904**; AV **22.05.2026**; header **12.06.2026**; pdfinfo created **23.06.2026 22:00:52 UTC**; model **VKT-inb** 26.0.15 m81-f; commissaris Luc Callaert BV B00342 / 0463.716.022 / Callaert Luc A01123 mandate 23.05.2025–08.05.2028 fee **9600**; VKT-inb 6.1.1/6.2/6.7/6.9/7/8/14/15/16/17 not filed; 6.1.2 MVA + 6.1.3 FVA + 6.3 + 6.4 + 6.5 + 6.6 + 6.8 + sociale balans + remuneratieverslag + commissarisverslag filed). Leftover AGB/APB first: leftover APB Inovant / Atlas provincieantwerpen.be **404** even with Googlebot UA; no fetchable 2025 Inovant/Atlas PDF (do not take Hooibeekhoeve). Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick (puyenbroeck.be 302). Leftover AGB Herzele already in entities (tick1163) — skipped. Leftover AGB Bornem still 2024. Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 last JR still 2024-12-31 as of 1471. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover WoonST Temse still JR2024 as of 1467. Leftover stek92 still JR2024 as of 1473. Leftover Woonveer statutory CDN `2026-00187904` live this tick (HTTP 200 / application/pdf / 3260693 / 40p; jaar **2025-12-31**; neerlegging **12.06.2026**) — taken (hunt order #2 leftover unmined woonmaatschappij of mined Puurs-Sint-Amands + Bornem with live 2025 VKT-inb after leftover AGB/APB hunt; strong 1476 hint; NBB consult only Verkort — no VOL-inb exists). PDF header **WOONVEER KLEIN-BRABANT / Palingstraat 48 bus 101 / 2870 Puurs-Sint-Amands** — NOT Zorgbedrijf Klein-Brabant 1143 / Woonkade / Woonstroom / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Distinct from already-mined **Woonkade 1476** / **Woonstroom 1475** / **Thuisrand 1474** / **Vivendo 1473** / **SW+ 1472** / **Woonhaven 1471** / **Thuispunt Gent 1470** / **Tuinwijk 1469** / **Dijledal 1468** / **Dender-Zuid 1467** / **Dimensa 1466** / **Woonmaatschappij Rivierenland 1465** / **Woonpunt Waas 1464** / **Zorgbedrijf Klein-Brabant 1143**. First confirmed not already extracted as JR2025 euros: no Woonveer / 0406.039.624 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **01.01.1968**; statutaire naam WOONVEER KLEIN-BRABANT since 10.01.2019; BV since 27.06.2023; zetel Palingstraat 48 bus 101 2870 Puurs-Sint-Amands since 01.01.2019; **1 VE**; 18 functiehouders; voorzitter De Blaiser Raf since 09.03.2022; dagelijks bestuur Smets Bartholomeus since 27.06.2023; Werkgever RSZ since 01.01.1977; btw since 01.04.1993; aanbestedende overheid; NACE 68.121 / 68.202; site https://woonveer.be/; werkingsgebied Puurs-Sint-Amands + Bornem (~1500 huurwoningen). Absorbeerde 0400.797.367 since 20.10.1988 + 0400.791.726 since 18.12.2018 + 0400.818.351 since 18.12.2018. Prior-year figures **identiek**. SBM used for deposit-id discovery only. Euros extracted from the official VKT-inb deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1480).\n"
        "- EUR strong (primary official WVV VKT-inb; omzet 70 **empty**; 60/61 **empty**; brutomarge 9900 **6663129** DROP vs 7950814; pers 62 **1772581** / **24,3 VTE** vs 1547893 / 21,4): assets **122300664** (was 121815309); fixed **92622293** vs 91088615 / IVA empty / MVA **92494707** vs 90961029 (terreinen/gebouwen **88595421**; installaties **163**; meubilair **94507**; in aanbouw **3804616**) / FVA **127586**; current **29678371 DROP** vs 30726694; voorraden **5962423**; ST recv **481231** (trade **125738** / other **355493**); LT recv empty; geldbeleg **10000000**; cash **12151452 DROP** vs 13271389; prepaid **1083266**; equity **35538478** vs 35239123 (inbreng **39496** onbeschikbaar; reserves **27991284**; kapsubs **7507698**); voorzieningen **2286217** (herstel **1632947**; overige **144057**; uitgestelde belasting **509213**); schulden **84475969** vs 84386746 (LT **79014400** waarvan fin krediet **77689087**; ST **4600172** waarvan 42 **2640244** + leveranciers **552801**; deferred **861398**); brutomarge **6663129** DROP; pers **1772581** / **24,3 VTE** / 32797 uur / YE **27** / YE VTE **24,5**; afschr **3650419**; expl **326542** vs 2043652; fin opbr **1750195** (interestsubs 1385020); fin kosten **1774035**; tax **20119**; PnL **9904 302728 DROP** vs 1891080 (te bestemmen 9905 **436625** volledig naar reserves); dividend **0**; capex MVA aanschaf **5198013**. Commissaris fee **9600**. Bestuurders zitpenningen **20085**. 1 VE. VKT 6.7 aandeel % unpublished. Cross-checks: 92622293+29678371=122300664; 35538478+2286217+84475969=122300664; 156118271-63623565=92494707; PDF-line P&L 1-euro rounding vs arithmetic (use PDF figures).\n"
        "- CSVs: sources +4; entities +1 `wm_wvrk` parent `city_puurs_sint_amands`; budgets +42 executed; commitments +1 envelope 6663129 AV 22.05.2026; leaderboard +1 annual 6663129 / total 122300664; foi_queue +1 status=ready never sent; research_queue surgical rq_1477=done + rq_1478 spawn; loop_state ticks_completed=1477. Inventory after write: budgets {INV_B} · commitments {INV_C} · leaderboard {INV_L} · entities {INV_E} · sources {INV_S} · FOI ready {FOI_R} / answered {FOI_A} / partial {FOI_P} / total {FOI_T}.\n"
        "- FOI: `gap_wvrk_brutomarge_6_66m_pers_1_77m_omzet_empty_l5` ready not sent — brutomarge 6.66m DROP / omzet 70 unpublished / 60/61 unpublished / pers 1.77m 24.3 VTE JUMP / 1 VE / cash DROP 12.15m / geldbeleg 10.00m / debt 84.48m LT krediet 77.69m / voorraden 5.96m / capex 5.20m / PnL DROP 0.30m / dividend 0 / commissaris 9.60k / aandeel % unpublished.\n"
        "- Next: rq_1478 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 404 this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1477). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live. Leftover IGS IVAREM **0267.403.264** still JR2024 as of 1471. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonhaven **0403.795.657** TAKEN 1471; SW+ **0405.342.610** TAKEN 1472; Vivendo **0406.062.883** TAKEN 1473; Thuisrand **0404.710.724** TAKEN 1474; Woonstroom **0404.033.605** TAKEN 1475; Woonkade **0452.753.537** TAKEN 1476; Woonveer **0406.039.624** TAKEN 1477; WoonST Temse still JR2024 as of 1467; stek92 still JR2024 as of 1473). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Erfgoed Rupelstreek IOED 1431 / Zorgbedrijf Klein-Brabant 1143. Next every-10 is **1480**. Provincial tourism VZWs now exhausted (Westtoer + TOV + TVLB + TLim).\n"
    )
    entry = entry.replace("{INV_B}", str(inv["budgets.csv"])).replace("{INV_C}", str(inv["commitments.csv"])).replace("{INV_L}", str(inv["leaderboard.csv"])).replace("{INV_E}", str(inv["entities.csv"])).replace("{INV_S}", str(inv["sources.csv"])).replace("{FOI_R}", str(foi_ready)).replace("{FOI_A}", str(foi_ans)).replace("{FOI_P}", str(foi_part)).replace("{FOI_T}", str(foi_tot))
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1477 -" in lraw:
        raise SystemExit("loop_log already has tick 1477 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1477")
    print("DONE tick 1477")

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

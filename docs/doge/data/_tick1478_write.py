#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1478 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T18:10:00Z"
ENT = "wm_wbog"
SRC = "src_wbog_jr2025_nbb"
GAP = "gap_wbog_omzet_38_56m_pers_5_37m_debt_481m_l5"
LB = "lb_wbog_omzet_38_56m_pers_5_37m_debt_481m"
COMM = "comm_wbog_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00145590.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Woonboog official NBB WVV VOL-inb JR2025,{PDF},NBB / Woonboog,2026-08-19,budget,tick1478; official NBB WVV VOL-inb JR2025 PDF 58p / 1200129 bytes; deposit 2026-00145590; AV 19.05.2026; header 09.06.2026; pdfinfo created 09.06.2026 07:55:00 UTC; model VOL-inb 25.0.12 m82-f; KBO 0403.773.287; assets 520063407 cash 11886333 debt 480967612 pers 5372953 omzet 38558400 pnl 2114753 equity 37466380",
        "src_wbog_site,Woonboog official pages,https://www.woonboog.be/,Woonboog / mined Turnhout + Beerse + Mol + Balen + Oud-Turnhout,2026-08-19,official_register,tick1478; leftover woonmaatschappij of mined Kempen-Midden; zetel Campus Blairon 599 2300 Turnhout; KBO 0403.773.287; SBM used for deposit-id discovery only",
        "src_kbo_wbog_0403773287,KBO Woonboog 0403.773.287,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0403773287,KBO Public Search FOD Economie,2026-08-19,official_register,tick1478; Actief since 01.01.1921; BV since 15.12.2022; naam WOONBOOG since 01.01.2023; zetel Campus Blairon 599 2300 Turnhout; 1 VE; 15 functiehouders; Werkgever RSZ since 01.07.1963; aanbestedende overheid",
        "src_wbog_foi_contact,Woonboog FOI channel (info@woonboog.be),https://www.woonboog.be/,Woonboog,2026-08-19,official_register,tick1478; leftover woonmaatschappij of mined Turnhout + Beerse + Mol + Balen + Oud-Turnhout; NOT Woonveer / Woonkade / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92 / leftover LeefGoed",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_wbog," in raw or raw.startswith(b"wm_wbog,"):
        raise SystemExit("wm_wbog already present")
    if b"0403.773.287" in raw or b"0403773287" in raw:
        raise SystemExit("Woonboog KBO already present as entity")
    row = (
        "wm_wbog,Woonboog (leftover woonmaatschappij / social-housing BV of mined Turnhout + Beerse + Mol + Balen + Oud-Turnhout / Kempen-Midden; NOT Woonveer 1477 / Woonkade Rupelstreek 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92 / leftover LeefGoed-Zonnige Kempen),"
        "Woonboog SRL (logement social residuel Kempen-Midden),"
        "Woonboog leftover social-housing company of mined Turnhout + Beerse + Mol + Balen + Oud-Turnhout (not Woonveer / Woonkade / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92 / leftover LeefGoed),"
        "other,city_turnhout,nl,https://www.woonboog.be/,info@woonboog.be,Campus Blairon 599 2300 Turnhout,"
        "tick1478 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0403.773.287 Actief since 01.01.1921; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 520063407 omzet 38558400 pers 5372953 65.4 VTE pnl 2114753 equity 37466380 cash 11886333 debt 480967612 capex 60407693 dividend 0; FOI ready omzet 38.56m JUMP / pers 5.37m 65.4 VTE / debt 480.97m / cash 11.89m DROP / PnL DROP 2.11m / dividend 0 / 1 VE; distinct from already-mined Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_wbog")

def part_budgets():
    BUDGETS = [
        ("bud_wbog_assets_2025", "2025", "520063407", "2025 assets 520063407 UP (was 516599675); tick1478; primary official NBB WVV VOL-inb 2026-00145590"),
        ("bud_wbog_current_2025", "2025", "50309563", "2025 vlottend 50309563 DROP (was 59195936); tick1478; primary official NBB WVV"),
        ("bud_wbog_cash_2025", "2025", "11886333", "2025 liquide middelen 11886333 DROP (was 12319316); tick1478; primary official NBB WVV"),
        ("bud_wbog_strecv_2025", "2025", "12121365", "2025 ST vorderingen 12121365 (was 9752689); tick1478; primary official NBB WVV"),
        ("bud_wbog_trade_2025", "2025", "850350", "2025 handelsvorderingen 850350 (was 606254); tick1478; primary official NBB WVV"),
        ("bud_wbog_othrecv_2025", "2025", "11271015", "2025 overige ST vorderingen 11271015 (was 9146435); tick1478; primary official NBB WVV"),
        ("bud_wbog_voorraden_2025", "2025", "18632938", "2025 voorraden 18632938 DROP (was 31020753); tick1478; primary official NBB WVV"),
        ("bud_wbog_prepaid_2025", "2025", "4427856", "2025 overlopend actief 4427856 (was 3895387); tick1478; primary official NBB WVV"),
        ("bud_wbog_geldbeleg_2025", "2025", "3231405", "2025 geldbeleggingen 3231405 (was 2198126); tick1478; primary official NBB WVV"),
        ("bud_wbog_fixed_2025", "2025", "469753844", "2025 vaste activa 469753844 (was 457403739); tick1478; primary official NBB WVV"),
        ("bud_wbog_iva_2025", "2025", "30291", "2025 IVA 30291 (was 118126); tick1478; primary official NBB WVV"),
        ("bud_wbog_mva_2025", "2025", "469690522", "2025 MVA 469690522 (was 457252257; terreinen/gebouwen 391097306 leasing 18559908 in aanbouw 59965794); tick1478; primary official NBB WVV"),
        ("bud_wbog_fva_2025", "2025", "33031", "2025 FVA 33031 (was 33356); tick1478; primary official NBB WVV"),
        ("bud_wbog_equity_2025", "2025", "37466380", "2025 eigen vermogen 37466380 UP (was 31939419); tick1478; primary official NBB WVV"),
        ("bud_wbog_inbreng_2025", "2025", "1141672", "2025 inbreng 1141672 (onbeschikbaar 1141672); tick1478; primary official NBB WVV"),
        ("bud_wbog_reserves_2025", "2025", "10168692", "2025 reserves 10168692 (was 9653150); tick1478; primary official NBB WVV"),
        ("bud_wbog_kapsubs_2025", "2025", "26156016", "2025 kapitaalsubsidies 26156016 UP (was 21834652); tick1478; primary official NBB WVV"),
        ("bud_wbog_voorz_2025", "2025", "1629415", "2025 voorzieningen+uitgestelde belasting 1629415 (herstel 200010); tick1478; primary official NBB WVV"),
        ("bud_wbog_debt_2025", "2025", "480967612", "2025 schulden 480967612 DROP (was 483231376); tick1478; primary official NBB WVV"),
        ("bud_wbog_ltdebt_2025", "2025", "452720025", "2025 LT schulden 452720025 (was 444782171; fin krediet 448816497); tick1478; primary official NBB WVV"),
        ("bud_wbog_stdebt_2025", "2025", "24857004", "2025 ST schulden 24857004 (42 17787156 + leveranciers 4603208); tick1478; primary official NBB WVV"),
        ("bud_wbog_lev_2025", "2025", "4603208", "2025 leveranciers 4603208 (was 8350297); tick1478; primary official NBB WVV"),
        ("bud_wbog_bezold_2025", "2025", "360489", "2025 bezoldigingen-schulden 360489 (was 379462); tick1478; primary official NBB WVV"),
        ("bud_wbog_taxpay_2025", "2025", "998688", "2025 belastingschulden 998688 (was 2395084); tick1478; primary official NBB WVV"),
        ("bud_wbog_deferred_2025", "2025", "3390583", "2025 overlopend passief 3390583 (was 4109656); tick1478; primary official NBB WVV"),
        ("bud_wbog_omzet_2025", "2025", "38558400", "2025 omzet 70 38558400 JUMP (was 32677715; verhuur 25836767 verkoop 12721634); tick1478; primary official NBB WVV"),
        ("bud_wbog_diensten_2025", "2025", "8366332", "2025 diensten 61 8366332 JUMP (was 7857051); tick1478; primary official NBB WVV"),
        ("bud_wbog_pers_2025", "2025", "5372953", "2025 pers 62 5372953; 65.4 VTE vs 65.2; 99844 uur; YE 71 / 64.3 VTE; tick1478; primary official NBB WVV"),
        ("bud_wbog_afschr_2025", "2025", "12618993", "2025 afschrijvingen 12618993; tick1478; primary official NBB WVV"),
        ("bud_wbog_expl_2025", "2025", "2258418", "2025 bedrijfswinst 2258418 DROP (was 5268240); tick1478; primary official NBB WVV"),
        ("bud_wbog_finopbr_2025", "2025", "10650659", "2025 financiele opbrengsten 10650659 (interestsubs 9651434); tick1478; primary official NBB WVV"),
        ("bud_wbog_finkost_2025", "2025", "10805429", "2025 financiele kosten 10805429; tick1478; primary official NBB WVV"),
        ("bud_wbog_pnl_2025", "2025", "2114753", "2025 PnL 2114753 DROP (was 3864483); tick1478; primary official NBB WVV"),
        ("bud_wbog_div_2025", "2025", "0", "2025 dividend 0 vergoeding van de inbreng empty; tick1478; primary official NBB WVV"),
        ("bud_wbog_capex_2025", "2025", "60407693", "2025 capex MVA aanschaf 60407693 (terreinen 41249962 meubilair 54798 in aanbouw 19102933); tick1478; primary official NBB WVV"),
        ("bud_wbog_in_aanbouw_2025", "2025", "59965794", "2025 activa in aanbouw 59965794 DROP (was 89943039); tick1478; primary official NBB WVV"),
        ("bud_wbog_krediet_2025", "2025", "448816497", "2025 LT kredietinstellingen 448816497 (was 441325938); tick1478; primary official NBB WVV"),
        ("bud_wbog_terreinen_2025", "2025", "391097306", "2025 terreinen en gebouwen 391097306 (was 347971086); tick1478; primary official NBB WVV"),
        ("bud_wbog_herstel_2025", "2025", "200010", "2025 voorziening grote herstellingen 200010 (was 225010); tick1478; primary official NBB WVV"),
        ("bud_wbog_bestuur_2025", "2025", "37143", "2025 bestuurders 37143; tick1478; primary official NBB WVV 6.16"),
        ("bud_wbog_commissaris_2025", "2025", "11500", "2025 commissaris fee 11500 Compass audit BV + extra controle 2625; tick1478; primary official NBB WVV"),
        ("bud_wbog_tax_2025", "2025", "30477", "2025 belastingen op het resultaat 30477; tick1478; primary official NBB WVV"),
        ("bud_wbog_andere_expl_2025", "2025", "1493707", "2025 andere bedrijfskosten 1493707; tick1478; primary official NBB WVV"),
        ("bud_wbog_interestsubs_2025", "2025", "9651434", "2025 interestsubsidies 9651434 (was 8043378); tick1478; primary official NBB WVV 6.11"),
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
        f"{COMM},Woonboog JR2025 leftover woonmaatschappij dual (omzet 38.56m JUMP / pers 5.37m 65.4 VTE / debt 480.97m / cash 11.89m DROP / PnL DROP 2.11m / dividend 0 / 1 VE),{ENT},Turnhout-Beerse-Mol-Balen / mined Kempen-Midden dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-19,1921,,38558400,,,active,{PDF},Local leftover woonmaatschappij map VL Kempen-Midden — omzet 38.56m JUMP / pers 5.37m 65.4 VTE / debt 480.97m / cash 11.89m DROP,Publish omzet+diensten+verhuur/verkoop split + 1 VE payroll + cash 11.89m DROP + LT krediet 448.82m counterparties + capex 60.41m + aandeel % Turnhout/Beerse/Mol/Balen/Oud-Turnhout/OCMW/private + dividend 0; do not keep leftover woonmaatschappij as unpublished 38.56m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Turnhout>Woonmaatschappij>Woonboog>JR2025_L5,tick1478; assets 520063407 omzet 38558400 pers 5372953 pnl 2114753 equity 37466380 cash 11886333 debt 480967612 capex 60407693 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT Woonveer / Woonkade / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92 / leftover LeefGoed",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Woonboog JR2025 leftover woonmaatschappij: omzet 38.56m JUMP / pers 5.37m 65.4 VTE / debt 480.97m / cash 11.89m DROP / PnL DROP 2.11m / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Turnhout>Woonmaatschappij>Woonboog>JR2025_L5,38558400,520063407,Leftover dual woonmaatschappij shell: assets 520.06m / equity 37.47m / omzet 38.56m JUMP / pers 5.37m 65.4 VTE / cash 11.89m DROP / debt 480.97m / LT krediet 448.82m / PnL DROP 2.11m / dividend 0 / 1 VE; do not treat 38.56m as TE-additive of 348bn,strong,{SRC},Woonboog / mined Turnhout-Beerse-Mol-Balen dual housing,Local leftover woonmaatschappij map VL Kempen-Midden — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 38.56m JUMP / pers 5.37m 65.4 VTE / debt 480.97m / cash 11.89m DROP / PnL DROP 2.11m / dividend 0 / 1 VE,7.0,8.0,3.0,7.0,Publish omzet+diensten+verhuur/verkoop split + 1 VE payroll + cash 11.89m DROP + LT krediet 448.82m counterparties + capex 60.41m + aandeel % Turnhout/Beerse/Mol/Balen/Oud-Turnhout/OCMW/private + dividend 0; do not keep leftover woonmaatschappij as unpublished 38.56m housing shell,active,,tick1478; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Gemeenten>Turnhout>Woonmaatschappij>Woonboog>JR2025_L5,{ENT},omzet 38558400 JUMP vs 32677715 + diensten 8366332 JUMP vs 7857051 + pers 5372953 65.4 VTE vs 65.2 + 1 VE + cash 11886333 DROP vs 12319316 + geldbeleg 3231405 + debt 480967612 LT krediet 448816497 + voorraden 18632938 DROP + capex 60407693 + PnL DROP 2114753 vs 3864483 + dividend 0 + commissaris 11500 + extra 2625 + bestuurders 37143 + aandeel % Turnhout/Beerse/Mol/Balen/Oud-Turnhout/OCMW/private unpublished,Leftover woonmaatschappij Woonboog after leftover AGB/APB hunt: omzet 38.56m JUMP / pers 5.37m 65.4 VTE / debt 480.97m / cash 11.89m DROP / PnL DROP 2.11m / dividend 0 / 1 VE hides municipal housing vehicle,8,Woonboog / Bestuursorgaan / voorzitter Kenis Bert,info@woonboog.be,Campus Blairon 599 2300 Turnhout,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1478 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (1200129 bytes 58p). FOI ready not sent. NOT every-10. NOT Woonveer 1477 / Woonkade 1476 / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still no separate APB 2025 PDF. WoonST Temse still JR2024 as of 1467. stek92 still JR2024 as of 1473. Leftover LeefGoed Zonnige Kempen still JR2024 as of this tick. Leftover Woonmaatschappij Vlaamse Ardennen 2026-00215629 live this tick unused. Woonboog TAKEN this tick.",
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
    if not last_s.startswith("rq_1478,"):
        raise SystemExit(f"expected last row rq_1478, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1478 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1478,Woonboog JR2025 leftover dual residual,hole_fill,5,done,L5,wm_wbog,"
        "Completed: Woonboog leftover woonmaatschappij of mined Turnhout + Beerse + Mol + Balen + Oud-Turnhout after leftover AGB/APB hunt; KBO 0403.773.287 Actief; live JR2025 official NBB WVV VOL-inb PDF (1200129 bytes 58p; deposit 2026-00145590; AV 19.05.2026; header 09.06.2026; pdfinfo 09.06.2026 07:55:00 UTC). PDF header WOONBOOG / Campus Blairon 599 — NOT Woonveer 1477 / Woonkade / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck / leftover LeefGoed. Sourced euros assets 520063407 omzet 38558400 pers 5372953 65.4 VTE pnl 2114753 equity 37466380 cash 11886333 debt 480967612 capex 60407693 dividend 0. FOI "
        f"{GAP} ready not sent. Distinct from already-mined Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464.,"
        f"{GAP},2026-08-19T17:55:00Z,{TS},"
        "tick1478 Woonboog leftover woonmaatschappij residual; KBO 0403.773.287; live JR2025 official NBB WVV VOL-inb PDF; sourced euros; FOI ready not sent; next rq_1479 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (WoonST Temse / stek92 / Woonin / Zonnige Kempen-LeefGoed / De Ideale Woning / Wooncompagnie / Kanvaz / Woonmaatschappij Vlaamse Ardennen 2026-00215629 live unused only if JR2025 live)"
    )
    spawn = (
        "rq_1479,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill: Next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1478 done including Woonboog 1478 leftover woonmaatschappij live official NBB WVV / Woonveer 1477 leftover woonmaatschappij live official NBB WVV / Woonkade 1476 leftover woonmaatschappij live official NBB WVV / Woonstroom 1475 leftover woonmaatschappij live official NBB WVV / Thuisrand 1474 leftover woonmaatschappij live official NBB WVV / Vivendo 1473 leftover woonmaatschappij live official NBB WVV / SW+ 1472 leftover woonmaatschappij live official NBB WVV / Woonhaven 1471 leftover woonmaatschappij live official NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 404 as of 1478). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1478). Do NOT confuse with already-mined Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Erfgoed Rupelstreek IOED 1431 / Zorgbedrijf Klein-Brabant 1143. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live. Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1471 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1461. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonhaven TAKEN 1471; SW+ TAKEN 1472; Vivendo TAKEN 1473; Thuisrand TAKEN 1474; Woonstroom TAKEN 1475; Woonkade TAKEN 1476; Woonveer TAKEN 1477; Woonboog TAKEN 1478; WoonST Temse still JR2024 as of 1467; stek92 still JR2024 as of 1473; LeefGoed-Zonnige Kempen still JR2024 as of 1478; Woonmaatschappij Vlaamse Ardennen 2026-00215629 live unused as of 1478). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Erfgoed Rupelstreek IOED 1431 / Zorgbedrijf Klein-Brabant 1143.,,"
        f"{TS},{TS},"
        "spawned tick1478 after Woonboog leftover woonmaatschappij live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (WoonST Temse / stek92 / Woonin / Zonnige Kempen-LeefGoed / De Ideale Woning / Wooncompagnie / Kanvaz / Woonmaatschappij Vlaamse Ardennen 2026-00215629 live unused only if JR2025 live)"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1478=done + rq_1479 spawned; keep", last_line_start)

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
    Path("/tmp/tick1478_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1478 Woonboog leftover woonmaatschappij residual; KBO 0403.773.287; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 520063407 omzet 38558400 pers 5372953 65.4 VTE pnl 2114753 equity 37466380 cash 11886333 debt 480967612 capex 60407693 dividend 0; FOI ready omzet 38.56m JUMP / pers 5.37m 65.4 VTE / debt 480.97m / cash 11.89m DROP / PnL DROP 2.11m / dividend 0 / 1 VE; NOT Woonveer / Woonkade / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1479 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (WoonST Temse / stek92 / Woonin / Zonnige Kempen-LeefGoed / De Ideale Woning / Wooncompagnie / Kanvaz / Woonmaatschappij Vlaamse Ardennen 2026-00215629 live unused only if JR2025 live); FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1478,1478,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1478")

    entry = (
        "\n## Tick 1478 - 2026-08-19 - rq_1478 Woonboog dual residual leftover\n"
        "- Unit: Woonboog BV (leftover woonmaatschappij / social-housing BV of mined Turnhout + Beerse + Mol + Balen + Oud-Turnhout / Kempen-Midden; 1 VE) after residual dual hunt (KBO **0403.773.287**; official NBB WVV VOL-inb PDF **1200129** bytes / 58p; deposit **2026-00145590**; AV **19.05.2026**; header **09.06.2026**; pdfinfo created **09.06.2026 07:55:00 UTC**; model **VOL-inb** 25.0.12 m82-f; commissaris Compass audit BV B00974 / 0680.780.741 / Camps Wim A02596 mandate 21.05.2024–18.05.2027 fee **11500** + extra controle **2625**; VOL-inb 6.1/6.2.1/6.2.2/6.2.4/6.2.5/6.4.1/6.4.2/6.5.1/6.5.2/6.7.2/6.8/6.15/6.18/6.20/9/12/13/14/15 not filed; 6.3 MVA + 6.4.3 FVA + 6.7.1 + 6.9 + 6.10 + 6.11 + 6.12 + 6.14 + 6.16 + 6.17 + 6.19 + sociale balans filed). Leftover AGB/APB first: leftover APB Inovant / Atlas provincieantwerpen.be **404** even with Googlebot UA; Foleon leftover slugs **403**; no fetchable 2025 Inovant/Atlas PDF (do not take Hooibeekhoeve). Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick (puyenbroeck.be 302). Leftover AGB Herzele already in entities (tick1163) — skipped. Leftover AGB Bornem still 2024. Leftover AGB Turnhout / AGB Beerse already in entities — skipped. Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 last JR still 2024-12-31 as of 1471. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover WoonST Temse still JR2024 as of 1467. Leftover stek92 still JR2024 as of 1473. Leftover LeefGoed (Zonnige Kempen successor 0404.144.065) Companyweb/SBM last JR still 2024 as of this tick — unused. Leftover Woonmaatschappij Vlaamse Ardennen CDN `2026-00215629` live this tick unused. Leftover Woonboog statutory CDN `2026-00145590` live this tick (HTTP 200 / application/pdf / 1200129 / 58p; jaar **2025-12-31**; neerlegging **09.06.2026**) — taken (hunt order #2 leftover unmined woonmaatschappij of mined Turnhout + Beerse + Mol + Balen + Oud-Turnhout with live 2025 VOL-inb after leftover AGB/APB hunt). PDF header **WOONBOOG / Campus Blairon 599 / 2300 Turnhout** — NOT Woonveer 1477 / Woonkade / Woonstroom / leftover IVAREM / Hooibeekhoeve / Puyenbroeck / leftover LeefGoed. Distinct from already-mined **Woonveer 1477** / **Woonkade 1476** / **Woonstroom 1475** / **Thuisrand 1474** / **Vivendo 1473** / **SW+ 1472** / **Woonhaven 1471** / **Thuispunt Gent 1470** / **Tuinwijk 1469** / **Dijledal 1468** / **Dender-Zuid 1467** / **Dimensa 1466** / **Woonmaatschappij Rivierenland 1465** / **Woonpunt Waas 1464**. First confirmed not already extracted as JR2025 euros: no Woonboog / 0403.773.287 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **01.01.1921**; statutaire naam WOONBOOG since 01.01.2023; BV since 15.12.2022; zetel Campus Blairon 599 2300 Turnhout since 11.05.2010; **1 VE**; 15 functiehouders; voorzitter Kenis Bert; algemeen directeur Teunkens Sanne since 01.01.2026; Werkgever RSZ since 01.07.1963; btw since 01.01.1971; aanbestedende overheid; NACE 68.121 / 68.202; site https://www.woonboog.be/; werkingsgebied Kempen-Midden 11 gemeenten (~4800 huurwoningen). Absorbeerde 0404.166.336 since 12.05.2009 + 0404.176.135 since 01.01.2023. Prior-year figures **identiek**. SBM used for deposit-id discovery only. Euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1480).\n"
        "- EUR strong (primary official WVV VOL-inb; omzet 70 **38558400** JUMP vs 32677715; diensten 61 **8366332** JUMP vs 7857051; pers 62 **5372953** / **65,4 VTE** vs 5186207 / 65,2): assets **520063407** (was 516599675); fixed **469753844** vs 457403739 / IVA **30291** / MVA **469690522** vs 457252257 (terreinen/gebouwen **391097306**; installaties **15863**; meubilair **51652**; leasing **18559908**; in aanbouw **59965794**) / FVA **33031**; current **50309563 DROP** vs 59195936; voorraden **18632938 DROP** vs 31020753; ST recv **12121365** (trade **850350** / other **11271015**); LT recv **9665**; geldbeleg **3231405**; cash **11886333 DROP** vs 12319316; prepaid **4427856**; equity **37466380** vs 31939419 (inbreng **1141672** onbeschikbaar; reserves **10168692**; kapsubs **26156016**); voorzieningen **1629415** (herstel **200010**; uitgestelde belasting **1429405**); schulden **480967612** vs 483231376 (LT **452720025** waarvan fin krediet **448816497**; ST **24857004** waarvan 42 **17787156** + leveranciers **4603208**; deferred **3390583**); omzet **38558400** JUMP (verhuur **25836767** / verkoop **12721634**); diensten **8366332**; pers **5372953** / **65,4 VTE** / 99844 uur / YE **71** / YE VTE **64,3**; afschr **12618993**; expl **2258418** vs 5268240; fin opbr **10650659** (interestsubs 9651434); fin kosten **10805429**; tax **30477**; PnL **9904 2114753 DROP** vs 3864483 (te bestemmen 9905 **2123688** waarvan 1434677 naar reserves); dividend **0**; capex MVA aanschaf **60407693**. Commissaris fee **11500** + extra **2625**. Bestuurders **37143**. 1 VE. VOL 6.7 aandeel % unpublished. Cross-checks: 469753844+50309563=520063407; 37466380+1629415+480967612=520063407; 38558400+376003+2497255+1401697=42833355; PDF-line P&L 1-euro rounding vs arithmetic (use PDF figures).\n"
        "- CSVs: sources +4; entities +1 `wm_wbog` parent `city_turnhout`; budgets +44 executed; commitments +1 envelope 38558400 AV 19.05.2026; leaderboard +1 annual 38558400 / total 520063407; foi_queue +1 status=ready never sent; research_queue surgical rq_1478=done + rq_1479 spawn; loop_state ticks_completed=1478. Inventory after write: budgets {INV_B} · commitments {INV_C} · leaderboard {INV_L} · entities {INV_E} · sources {INV_S} · FOI ready {FOI_R} / answered {FOI_A} / partial {FOI_P} / total {FOI_T}.\n"
        "- FOI: `gap_wbog_omzet_38_56m_pers_5_37m_debt_481m_l5` ready not sent — omzet 38.56m JUMP / diensten 8.37m JUMP / pers 5.37m 65.4 VTE / 1 VE / cash DROP 11.89m / geldbeleg 3.23m / debt 480.97m LT krediet 448.82m / voorraden DROP 18.63m / capex 60.41m / PnL DROP 2.11m / dividend 0 / commissaris 11.50k + extra 2.63k / aandeel % unpublished.\n"
        "- Next: rq_1479 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 404 this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1478). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live. Leftover IGS IVAREM **0267.403.264** still JR2024 as of 1471. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonhaven **0403.795.657** TAKEN 1471; SW+ **0405.342.610** TAKEN 1472; Vivendo **0406.062.883** TAKEN 1473; Thuisrand **0404.710.724** TAKEN 1474; Woonstroom **0404.033.605** TAKEN 1475; Woonkade **0452.753.537** TAKEN 1476; Woonveer **0406.039.624** TAKEN 1477; Woonboog **0403.773.287** TAKEN 1478; WoonST Temse still JR2024 as of 1467; stek92 still JR2024 as of 1473; LeefGoed-Zonnige Kempen still JR2024 as of 1478; Woonmaatschappij Vlaamse Ardennen **0466.370.951** CDN `2026-00215629` live unused as of 1478). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Erfgoed Rupelstreek IOED 1431. Next every-10 is **1480**. Provincial tourism VZWs now exhausted (Westtoer + TOV + TVLB + TLim).\n"
    )
    entry = entry.replace("{INV_B}", str(inv["budgets.csv"])).replace("{INV_C}", str(inv["commitments.csv"])).replace("{INV_L}", str(inv["leaderboard.csv"])).replace("{INV_E}", str(inv["entities.csv"])).replace("{INV_S}", str(inv["sources.csv"])).replace("{FOI_R}", str(foi_ready)).replace("{FOI_A}", str(foi_ans)).replace("{FOI_P}", str(foi_part)).replace("{FOI_T}", str(foi_tot))
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1478 -" in lraw:
        raise SystemExit("loop_log already has tick 1478 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1478")
    print("DONE tick 1478")

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

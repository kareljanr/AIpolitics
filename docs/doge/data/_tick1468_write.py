#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1468 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T16:35:00Z"
ENT = "wm_djld"
SRC = "src_djld_jr2025_nbb"
GAP = "gap_djld_omzet_23_69m_pers_5_27m_debt_318m_l5"
LB = "lb_djld_omzet_23_69m_pers_5_27m_debt_318m"
COMM = "comm_djld_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00115640.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Dijledal official NBB WVV VOL-inb JR2025,{PDF},NBB / Dijledal,2026-08-19,budget,tick1468; official NBB WVV VOL-inb JR2025 PDF 61p / 1923680 bytes; deposit 2026-00115640; AV 13.05.2026; header 20.05.2026; pdfinfo created 20.05.2026 22:50:40 UTC; model VOL-inb 25.0.12 m82-f; KBO 0400.634.447; assets 352693973 cash 9950972 debt 318395099 pers 5274246 omzet 23688493 diensten 9130062 pnl -2643149 equity 29029222",
        "src_djld_site,Dijledal official pages,https://www.dijledal.be/,Dijledal / mined Leuven,2026-08-19,official_register,tick1468; leftover woonmaatschappij of mined Leuven+Bierbeek+Boutersem+Oud-Heverlee; zetel Vaartkom 1B 3000 Leuven; KBO 0400.634.447; NBB consult used for deposit-id discovery only",
        "src_kbo_djld_0400634447,KBO Dijledal 0400.634.447,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0400634447,KBO Public Search FOD Economie,2026-08-19,official_register,tick1468; Actief since 08.07.1938; BV since 20.06.2023; naam DIJLEDAL Sociale Huisvesting Leuven since 16.07.1997; zetel Vaartkom 1B 3000 Leuven; 1 VE; 16 functiehouders; Werkgever RSZ since 01.01.1945; aanbestedende overheid",
        "src_djld_foi_contact,Dijledal FOI channel (info@dijledal.be),https://www.dijledal.be/,Dijledal,2026-08-19,official_register,tick1468; leftover woonmaatschappij of mined Leuven; NOT Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover Tuinwijk",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_djld," in raw or raw.startswith(b"wm_djld,"):
        raise SystemExit("wm_djld already present")
    if b"0400.634.447" in raw:
        raise SystemExit("Dijledal KBO already present as entity")
    row = (
        "wm_djld,Dijledal Sociale Huisvesting Leuven (leftover woonmaatschappij / social-housing BV of mined Leuven + Bierbeek + Boutersem + Oud-Heverlee; NOT Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover Tuinwijk / leftover Thuispunt Gent / leftover Woonhaven),"
        "Societe de logement Dijledal Louvain SRL (logement social residuel Louvain),"
        "Dijledal leftover social-housing company of mined Leuven (not Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover Tuinwijk),"
        "other,city_leuven,nl,https://www.dijledal.be/,info@dijledal.be,Vaartkom 1B 3000 Leuven,"
        "tick1468 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0400.634.447 Actief since 08.07.1938; live JR2025 official NBB WVV PDF; sourced euros assets 352693973 omzet 23688493 diensten 9130062 pers 5274246 70.2 VTE pnl -2643149 equity 29029222 cash 9950972 debt 318395099 capex 16818275 dividend 0; FOI ready omzet 23.69m DROP / pers 5.27m 70.2 VTE / debt 318.40m / cash DROP 9.95m / PnL -2.64m / dividend 0 / 1 VE / VMSW going-concern; distinct from already-mined Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_djld")

def part_budgets():
    BUDGETS = [
        ("bud_djld_assets_2025", "2025", "352693973", "2025 assets 352693973 (was 347248092); tick1468; primary official NBB WVV VOL-inb 2026-00115640"),
        ("bud_djld_current_2025", "2025", "16357483", "2025 vlottend 16357483 (was 16914623); tick1468; primary official NBB WVV"),
        ("bud_djld_cash_2025", "2025", "9950972", "2025 liquide middelen 9950972 DROP (was 11185626); tick1468; primary official NBB WVV"),
        ("bud_djld_geldbeleg_2025", "2025", "0", "2025 geldbeleggingen empty; tick1468; primary official NBB WVV"),
        ("bud_djld_strecv_2025", "2025", "2671472", "2025 ST vorderingen 2671472 (was 1780917); tick1468; primary official NBB WVV"),
        ("bud_djld_trade_2025", "2025", "301775", "2025 handelsvorderingen 301775 (was 619137); tick1468; primary official NBB WVV"),
        ("bud_djld_othrecv_2025", "2025", "2369697", "2025 overige ST vorderingen 2369697 JUMP (was 1161780); tick1468; primary official NBB WVV"),
        ("bud_djld_voorraden_2025", "2025", "310910", "2025 voorraden 310910 DROP (was 1091773; onroerend verkoop 0 vs 793007); tick1468; primary official NBB WVV"),
        ("bud_djld_prepaid_2025", "2025", "3424130", "2025 overlopend actief 3424130 (was 2856307); tick1468; primary official NBB WVV"),
        ("bud_djld_fixed_2025", "2025", "336336489", "2025 vaste activa 336336489 (was 330333469); tick1468; primary official NBB WVV"),
        ("bud_djld_iva_2025", "2025", "159385", "2025 IVA 159385 (was 163794); tick1468; primary official NBB WVV"),
        ("bud_djld_mva_2025", "2025", "335886894", "2025 MVA 335886894 (was 329889034; terreinen/gebouwen 319519434 in aanbouw 15993623); tick1468; primary official NBB WVV"),
        ("bud_djld_fva_2025", "2025", "290210", "2025 FVA 290210 (aandelen 289634 + borg 576); tick1468; primary official NBB WVV"),
        ("bud_djld_equity_2025", "2025", "29029222", "2025 eigen vermogen 29029222 DROP (was 29951787); tick1468; primary official NBB WVV"),
        ("bud_djld_inbreng_2025", "2025", "145342", "2025 inbreng 145342 (onbeschikbaar 145342); tick1468; primary official NBB WVV"),
        ("bud_djld_reserves_2025", "2025", "9655579", "2025 reserves 9655579; tick1468; primary official NBB WVV"),
        ("bud_djld_overgedr_2025", "2025", "-15941613", "2025 overgedragen verlies -15941613 (was -13298465); tick1468; primary official NBB WVV"),
        ("bud_djld_kapsubs_2025", "2025", "35169914", "2025 kapitaalsubsidies 35169914 JUMP (was 33449330); tick1468; primary official NBB WVV"),
        ("bud_djld_voorz_2025", "2025", "5269653", "2025 voorzieningen+uitgestelde belasting 5269653; tick1468; primary official NBB WVV"),
        ("bud_djld_debt_2025", "2025", "318395099", "2025 schulden 318395099 (was 312114861); tick1468; primary official NBB WVV"),
        ("bud_djld_ltdebt_2025", "2025", "298037099", "2025 LT schulden 298037099 (was 293002089; fin krediet 290115366); tick1468; primary official NBB WVV"),
        ("bud_djld_stdebt_2025", "2025", "17574839", "2025 ST schulden 17574839 (was 16505904); tick1468; primary official NBB WVV"),
        ("bud_djld_lev_2025", "2025", "3132024", "2025 leveranciers 3132024 JUMP (was 1760427); tick1468; primary official NBB WVV"),
        ("bud_djld_bezold_2025", "2025", "515504", "2025 bezoldigingen-schulden 515504 (was 594880); tick1468; primary official NBB WVV"),
        ("bud_djld_taxpay_2025", "2025", "2316587", "2025 belastingschulden 2316587 (was 2155391); tick1468; primary official NBB WVV"),
        ("bud_djld_deferred_2025", "2025", "2783161", "2025 overlopend passief 2783161 (was 2606868); tick1468; primary official NBB WVV"),
        ("bud_djld_omzet_2025", "2025", "23688493", "2025 omzet 70 23688493 DROP (was 25187830; 6.10 verhuring 24168355 gap 479862); tick1468; primary official NBB WVV"),
        ("bud_djld_diensten_2025", "2025", "9130062", "2025 diensten 61 9130062 JUMP (was 8205642); tick1468; primary official NBB WVV"),
        ("bud_djld_aankopen_2025", "2025", "1210647", "2025 handelsgoederen/grondstoffen 60 1210647 (aankopen 429784 voorraad 780863); tick1468; primary official NBB WVV"),
        ("bud_djld_pers_2025", "2025", "5274246", "2025 pers 62 5274246; 70.2 VTE vs 69.7; 105409 uur; YE 68 VTE 73 personen; tick1468; primary official NBB WVV"),
        ("bud_djld_afschr_2025", "2025", "10836111", "2025 afschrijvingen 10836111; tick1468; primary official NBB WVV"),
        ("bud_djld_expl_2025", "2025", "-2004468", "2025 bedrijfsverlies -2004468 (was -2380106); tick1468; primary official NBB WVV"),
        ("bud_djld_finopbr_2025", "2025", "5800290", "2025 financiele opbrengsten 5800290 all recurrent; tick1468; primary official NBB WVV"),
        ("bud_djld_finkost_2025", "2025", "6522659", "2025 financiele kosten 6522659; tick1468; primary official NBB WVV"),
        ("bud_djld_pnl_2025", "2025", "-2643149", "2025 PnL -2643149 (was -3034399); tick1468; primary official NBB WVV"),
        ("bud_djld_div_2025", "2025", "0", "2025 dividend 0 vergoeding van de inbreng empty; tick1468; primary official NBB WVV"),
        ("bud_djld_capex_2025", "2025", "16818275", "2025 capex MVA aanschaf 16818275 (terreinen 1902393 + install 45347 + in aanbouw 14870535); tick1468; primary official NBB WVV"),
        ("bud_djld_bedrijfsopbr_2025", "2025", "27508408", "2025 bedrijfsopbrengsten 70/76A 27508408; tick1468; primary official NBB WVV"),
        ("bud_djld_bedrijfskost_2025", "2025", "29512876", "2025 bedrijfskosten 60/66A 29512876; tick1468; primary official NBB WVV"),
        ("bud_djld_tax_2025", "2025", "35", "2025 belastingen 67/77 35; tick1468; primary official NBB WVV"),
        ("bud_djld_in_aanbouw_2025", "2025", "15993623", "2025 activa in aanbouw 15993623 JUMP (was 12894072); tick1468; primary official NBB WVV"),
        ("bud_djld_krediet_2025", "2025", "290115366", "2025 LT kredietinstellingen 290115366 (was 285290221); tick1468; primary official NBB WVV"),
        ("bud_djld_comm_2025", "2025", "12300", "2025 commissaris Auditas fee 9505 12300; tick1468; primary official NBB WVV"),
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
        f"{COMM},Dijledal JR2025 leftover woonmaatschappij dual (omzet 23.69m DROP / diensten 9.13m JUMP / pers 5.27m 70.2 VTE / debt 318.40m / cash DROP 9.95m / PnL -2.64m / dividend 0 / 1 VE / VMSW going-concern),{ENT},Leuven / mined Leuven dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-13,1938,,23688493,,,active,{PDF},Local leftover woonmaatschappij map VL Leuven — omzet 23.69m DROP / pers 5.27m 70.2 VTE / debt 318.40m / cash DROP 9.95m,Publish omzet split + 6.10 gap 0.48m + 1 VE payroll + cash DROP 11.19m to 9.95m + LT krediet 290.12m counterparties + capex 16.82m + aandeel % Leuven/OCMW/Bierbeek/Boutersem/Oud-Heverlee/VL/provincie/Voka + VMSW going-concern + dividend 0; do not keep leftover woonmaatschappij as unpublished 23.69m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Leuven>Woonmaatschappij>Dijledal>JR2025_L5,tick1468; assets 352693973 omzet 23688493 diensten 9130062 pers 5274246 pnl -2643149 equity 29029222 cash 9950972 debt 318395099 capex 16818275 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover Tuinwijk",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Dijledal JR2025 leftover woonmaatschappij: omzet 23.69m DROP / diensten 9.13m JUMP / pers 5.27m 70.2 VTE / debt 318.40m / cash DROP 9.95m / PnL -2.64m / dividend 0 / 1 VE / VMSW going-concern,L5,local_budget_line,Vlaanderen>Gemeenten>Leuven>Woonmaatschappij>Dijledal>JR2025_L5,23688493,352693973,Leftover dual woonmaatschappij shell: assets 352.69m / equity 29.03m / omzet 23.69m DROP / diensten 9.13m JUMP / pers 5.27m 70.2 VTE / cash 9.95m DROP / debt 318.40m / LT krediet 290.12m / PnL -2.64m / dividend 0 / 1 VE / VMSW going-concern; do not treat 23.69m as TE-additive of 348bn,strong,{SRC},Leuven / mined Leuven dual housing,Local leftover woonmaatschappij map VL Leuven — JR2025 official NBB WVV live; omzet+pers+debt+cash+VMSW FOI,Official NBB WVV 2026-08-19: omzet 23.69m DROP / pers 5.27m 70.2 VTE / debt 318.40m / cash DROP 9.95m / PnL -2.64m / dividend 0 / 1 VE / VMSW going-concern,7.0,7.5,3.0,7.0,Publish omzet split + 6.10 gap 0.48m + 1 VE payroll + cash DROP 11.19m to 9.95m + LT krediet 290.12m counterparties + capex 16.82m + aandeel % Leuven/OCMW/Bierbeek/Boutersem/Oud-Heverlee/VL/provincie/Voka + VMSW going-concern + dividend 0; do not keep leftover woonmaatschappij as unpublished 23.69m housing shell,active,,tick1468; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Gemeenten>Leuven>Woonmaatschappij>Dijledal>JR2025_L5,{ENT},omzet 23688493 DROP vs 25187830 + 6.10 verhuring 24168355 gap 479862 + diensten 9130062 JUMP vs 8205642 + pers 5274246 70.2 VTE vs 69.7 + 1 VE + cash 9950972 DROP vs 11185626 + debt 318395099 LT krediet 290115366 + voorraden 310910 DROP onroerend 0 vs 793007 + capex 16818275 in aanbouw JUMP 15993623 vs 12894072 + PnL -2643149 vs -3034399 + dividend 0 + commissaris 12300 + VMSW going-concern + aandeel % Leuven/OCMW/Bierbeek/Boutersem/Oud-Heverlee/VL/provincie/Voka unpublished,Leftover woonmaatschappij Dijledal after leftover AGB/APB hunt: omzet 23.69m DROP / pers 5.27m 70.2 VTE / debt 318.40m / cash DROP 9.95m / PnL -2.64m / dividend 0 / 1 VE / VMSW going-concern hides municipal housing vehicle,8,Dijledal / Bestuursorgaan / directeur,info@dijledal.be,Vaartkom 1B 3000 Leuven,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1468 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF now extracted (1923680 bytes 61p). FOI ready not sent. NOT every-10. NOT Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / Toerisme Limburg / Toerisme Vlaams-Brabant / Toerisme Oost-Vlaanderen / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1467. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still no separate APB 2025 PDF. Leftover Tuinwijk 0400.180.131 JR2025 spotted on SBM this tick — not taken.",
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
    if not last_s.startswith("rq_1468,"):
        raise SystemExit(f"expected last row rq_1468, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1468 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1468,Dijledal Sociale Huisvesting Leuven JR2025 leftover dual residual,hole_fill,5,done,L5,wm_djld,"
        "Completed: Dijledal leftover woonmaatschappij of mined Leuven after leftover AGB/APB hunt; KBO 0400.634.447 Actief; live JR2025 official NBB WVV VOL-inb PDF (1923680 bytes 61p; deposit 2026-00115640; AV 13.05.2026; header 20.05.2026; pdfinfo 20.05.2026 22:50:40 UTC). PDF header Dijledal / Vaartkom 1B — NOT Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Sourced euros assets 352693973 omzet 23688493 diensten 9130062 pers 5274246 70.2 VTE pnl -2643149 equity 29029222 cash 9950972 debt 318395099 capex 16818275 dividend 0. FOI "
        f"{GAP} ready not sent. Distinct from already-mined Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456.,"
        f"{GAP},2026-08-19T16:20:00Z,{TS},"
        "tick1468 Dijledal leftover woonmaatschappij residual; KBO 0400.634.447; live JR2025 official NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1469 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (Tuinwijk 0400.180.131 JR2025 spotted on SBM)"
    )
    spawn = (
        "rq_1469,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1468 done including Dijledal 1468 leftover woonmaatschappij live official NBB WVV / Dender-Zuid 1467 leftover woonmaatschappij live official NBB WVV / Dimensa 1466 leftover woonmaatschappij live official NBB WVV / Woonmaatschappij Rivierenland 1465 leftover woonmaatschappij live official NBB WVV / Woonpunt Waas 1464 leftover woonmaatschappij live official NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 404 as of 1468). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck spotted unmined around 1453 — still no separate APB 2025 PDF as of 1468). Do NOT confuse with already-mined Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live. Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1468 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1468. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Tuinwijk 0400.180.131 JR2025 spotted on SBM this tick). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463.,,"
        f"{TS},{TS},"
        "spawned tick1468 after Dijledal leftover woonmaatschappij live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (Tuinwijk 0400.180.131 JR2025 spotted)"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1468=done + rq_1469 spawned; keep", last_line_start)

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
    Path("/tmp/tick1468_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1468 Dijledal leftover woonmaatschappij residual; KBO 0400.634.447; live JR2025 official NBB WVV PDF; sourced euros assets 352693973 omzet 23688493 diensten 9130062 pers 5274246 70.2 VTE pnl -2643149 equity 29029222 cash 9950972 debt 318395099 capex 16818275 dividend 0; FOI ready omzet 23.69m DROP / pers 5.27m 70.2 VTE / debt 318.40m / cash DROP 9.95m / PnL -2.64m / dividend 0 / 1 VE / VMSW going-concern; NOT Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1469 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (Tuinwijk 0400.180.131 JR2025 spotted); FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1468,1468,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1468")

    entry = (
        "\n## Tick 1468 - 2026-08-19 - rq_1468 Dijledal Sociale Huisvesting Leuven dual residual leftover\n"
        "- Unit: Dijledal Sociale Huisvesting Leuven BV (leftover woonmaatschappij / social-housing BV of mined Leuven + Bierbeek + Boutersem + Oud-Heverlee; 1 VE) after residual dual hunt (KBO **0400.634.447**; official NBB WVV VOL-inb PDF **1923680** bytes / 61p; deposit **2026-00115640**; AV **13.05.2026**; header **20.05.2026**; pdfinfo created **20.05.2026 22:50:40 UTC**; model **VOL-inb** 25.0.12 m82-f; commissaris Auditas Bedrijfsrevisoren BV B00364 / 0464.594.366 / Vansteelant Sven A02050 mandate 08.05.2024–13.05.2027 fee **12300**; oordeel zonder voorbehoud + benadrukking continuïteit / VMSW-steun). Leftover AGB/APB first: leftover APB Inovant / Atlas Foleon `jaarrekening_25_inov` / `jaarrekening_25_atlas` HEAD **404** this tick; provincieantwerpen.be **403** even with Googlebot UA; no fetchable 2025 Inovant/Atlas PDF (do not take Hooibeekhoeve). Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick. Leftover AGB Herzele already in entities (tick1163) — skipped. Leftover AGB Bornem still 2024 (2026-00553588 HEAD 403). Leftover AGB Hasselt / SOLag / WAGSO / Temse / Herk / Lommel already in entities — skipped. Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel still no JR as of 1467. Leftover IGS IVAREM 0267.403.264 last JR still 2024-12-31. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover Dijledal statutory CDN `2026-00115640` live this tick (HTTP 200 / 1923680 / 61p; jaar **2025-12-31**; neerlegging **20.05.2026**) — taken (hunt order #2 leftover unmined woonmaatschappij of mined Leuven with live 2025 statutory PDF after leftover AGB/APB hunt). PDF header **Dijledal / Vaartkom 1B / 3000 Leuven** — NOT Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Distinct from already-mined **Dender-Zuid 1467** / **Dimensa 1466** / **Woonmaatschappij Rivierenland 1465** / **Woonpunt Waas 1464** / **Toerisme Limburg 1463** / **Toerisme Vlaams-Brabant 1462** / **Toerisme Oost-Vlaanderen 1461** / **Arboretum Kalmthout 1460** / **Kempens Landschap 1459** / **APB Warande 1458** / **APB De Schorre 1457** / **APB PIH 1456**. First confirmed not already extracted as JR2025 euros: no Dijledal / 0400.634.447 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **08.07.1938**; statutaire naam DIJLEDAL Sociale Huisvesting Leuven since 16.07.1997; BV since 20.06.2023; zetel Vaartkom 1B 3000 Leuven; **1 VE**; 16 functiehouders; directeur Thora Erik since 10.05.2007; Werkgever RSZ since 01.01.1945; btw since 01.03.1983; aanbestedende overheid; NACE 68.202 / 41.001; site https://www.dijledal.be/; werkingsgebied Leuven+Bierbeek+Boutersem+Oud-Heverlee. Prior-year figures **identiek**. NBB consult used for deposit-id discovery only. Euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1470).\n"
        "- EUR strong (primary official WVV VOL-inb; omzet 70 **23688493** DROP vs 25187830; 6.10 verhuring **24168355** gap **479862**; diensten 61 **9130062** JUMP vs 8205642; pers 62 **5274246** / **70,2 VTE** vs 69,7): assets **352693973** (was 347248092); fixed **336336489** vs 330333469 / IVA **159385** vs 163794 / MVA **335886894** vs 329889034 (terreinen/gebouwen **319519434**; installaties **54804**; meubilair **73179**; leasing **0**; overige **245854**; in aanbouw **15993623 JUMP** vs 12894072) / FVA **290210**; current **16357483** vs 16914623; voorraden **310910 DROP** vs 1091773 (onroerend verkoop **0** vs 793007); ST recv **2671472** (trade **301775** / other **2369697 JUMP**); geldbeleg empty; cash **9950972 DROP** vs 11185626; prepaid **3424130**; equity **29029222 DROP** vs 29951787 (inbreng **145342**; reserves **9655579**; overgedragen **-15941613**; kapsubs **35169914 JUMP** vs 33449330); voorzieningen **5269653** (grote herstellingen **893801**; overige **2500000**; uitgestelde belasting **1875852**); schulden **318395099** vs 312114861 (LT **298037099** waarvan fin krediet **290115366**; ST **17574839** waarvan 42 **11309405** + leveranciers **3132024 JUMP** vs 1760427; deferred **2783161**); omzet **23688493** DROP; 60 **1210647**; diensten **9130062** JUMP; pers **5274246** / **70,2 VTE** / 105409 uur / YE **68 VTE** 73 personen vs 74; interim **1,1 VTE** 118491; afschr **10836111**; expl **-2004468** vs -2380106; fin opbr **5800290**; fin kosten **6522659**; tax **35**; PnL **-2643149** vs -3034399; dividend **0**; capex MVA aanschaf **16818275** (terreinen 1902393 + install 45347 + in aanbouw 14870535) + IVA 11287 + FVA 10394. Commissaris fee **12300**. Bestuurders 9503 **56739**. 1 VE. 38561 aandelen op naam. Cross-checks: 336336489+16357483=352693972 vs 352693973; 29029222+5269653+318395099=352693974 vs 352693973; 27508408-29512876=-2004468; -2004468+5800290-6522659=-2726837 vs -2726836; -2726836+83722-35=-2643149. Commissaris cents 352693972.81 / -2643148.72.\n"
        "- CSVs: sources +4; entities +1 `wm_djld` parent `city_leuven`; budgets +43 executed; commitments +1 envelope 23688493 AV 13.05.2026; leaderboard +1 annual 23688493 / total 352693973; foi_queue +1 status=ready never sent; research_queue surgical rq_1468=done + rq_1469 spawn; loop_state ticks_completed=1468. Inventory after write: budgets {INV_B} · commitments {INV_C} · leaderboard {INV_L} · entities {INV_E} · sources {INV_S} · FOI ready {FOI_R} / answered {FOI_A} / partial {FOI_P} / total {FOI_T}.\n"
        "- FOI: `gap_djld_omzet_23_69m_pers_5_27m_debt_318m_l5` ready not sent — omzet 23.69m DROP / 6.10 gap 0.48m / diensten 9.13m JUMP / pers 5.27m 70.2 VTE / 1 VE / cash DROP 9.95m / debt 318.40m LT krediet 290.12m / voorraden DROP 0.31m / capex 16.82m / PnL -2.64m / dividend 0 / commissaris 12.3k / VMSW going-concern / aandeel pct Leuven/OCMW/Bierbeek/Boutersem/Oud-Heverlee/VL/provincie/Voka unpublished.\n"
        "- Next: rq_1469 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 404 this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1468). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live. Leftover IGS IVAREM **0267.403.264** still JR2024. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Tuinwijk **0400.180.131** JR2025 spotted on SBM this tick; Thuispunt Gent **0400.032.156** / Woonhaven **0403.795.657** also JR2025-spotted). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Stichting Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456. Next every-10 is **1470**. Provincial tourism VZWs now exhausted (Westtoer + TOV + TVLB + TLim).\n"
    )
    entry = entry.replace("{INV_B}", str(inv["budgets.csv"])).replace("{INV_C}", str(inv["commitments.csv"])).replace("{INV_L}", str(inv["leaderboard.csv"])).replace("{INV_E}", str(inv["entities.csv"])).replace("{INV_S}", str(inv["sources.csv"])).replace("{FOI_R}", str(foi_ready)).replace("{FOI_A}", str(foi_ans)).replace("{FOI_P}", str(foi_part)).replace("{FOI_T}", str(foi_tot))
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1468 -" in lraw:
        raise SystemExit("loop_log already has tick 1468 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1468")
    print("DONE tick 1468")

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

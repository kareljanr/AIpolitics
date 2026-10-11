#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1475 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T17:55:00Z"
ENT = "wm_wstr"
SRC = "src_wstr_jr2025_nbb"
GAP = "gap_wstr_omzet_16_00m_pers_2_89m_debt_164m_l5"
LB = "lb_wstr_omzet_16_00m_pers_2_89m_debt_164m"
COMM = "comm_wstr_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00178253.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Woonstroom official NBB WVV VOL-inb JR2025,{PDF},NBB / Woonstroom,2026-08-19,budget,tick1475; official NBB WVV VOL-inb JR2025 PDF 66p / 3332034 bytes; deposit 2026-00178253; AV 27.05.2026; header 12.06.2026; pdfinfo created 20.06.2026 03:32:20 UTC; model VOL-inb 26.0.15 m82-f; KBO 0404.033.605; assets 203977089 cash 3750757 debt 164155257 pers 2885619 omzet 16002569 diensten 6853374 pnl 24748 equity 35164736",
        "src_wstr_site,Woonstroom official pages,https://woonstroom.be/,Woonstroom / mined Duffel-Lier-Bonheiden,2026-08-19,official_register,tick1475; leftover woonmaatschappij of mined Duffel + Lier + Bonheiden + Sint-Katelijne-Waver; zetel Nieuwstraat 3 2570 Duffel; KBO 0404.033.605; SBM used for deposit-id discovery only",
        "src_kbo_wstr_0404033605,KBO Woonstroom 0404.033.605,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0404033605,KBO Public Search FOD Economie,2026-08-19,official_register,tick1475; Actief since 01.01.1968; BV since 19.06.2023; naam Woonstroom since 19.06.2023; zetel Nieuwstraat 3 2570 Duffel; 3 VE; 14 functiehouders; Werkgever RSZ since 01.01.1945; aanbestedende overheid",
        "src_wstr_foi_contact,Woonstroom FOI channel (info@woonstroom.be),https://woonstroom.be/,Woonstroom,2026-08-19,official_register,tick1475; leftover woonmaatschappij of mined Duffel-Lier-Bonheiden; NOT Thuisrand / Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92 / leftover Woonkade / leftover Woonveer",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_wstr," in raw or raw.startswith(b"wm_wstr,"):
        raise SystemExit("wm_wstr already present")
    if b"0404.033.605" in raw or b"0404033605" in raw:
        raise SystemExit("Woonstroom KBO already present as entity")
    row = (
        "wm_wstr,Woonstroom (leftover woonmaatschappij / social-housing BV of mined Duffel + Lier + Bonheiden + Sint-Katelijne-Waver; NOT Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92 / leftover Woonkade / leftover Woonveer),"
        "Woonstroom SRL (logement social residuel Duffel-Lier-Bonheiden),"
        "Woonstroom leftover social-housing company of mined Duffel-Lier-Bonheiden (not Thuisrand / Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92 / leftover Woonkade / leftover Woonveer),"
        "other,city_duffel,nl,https://woonstroom.be/,info@woonstroom.be,Nieuwstraat 3 2570 Duffel,"
        "tick1475 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0404.033.605 Actief since 01.01.1968; live JR2025 official NBB WVV PDF; sourced euros assets 203977089 omzet 16002569 diensten 6853374 pers 2885619 30.3 VTE pnl 24748 equity 35164736 cash 3750757 debt 164155257 capex 13967360 dividend 0; FOI ready omzet 16.00m DROP / pers 2.89m 30.3 VTE JUMP / debt 164.16m / cash 3.75m DROP / PnL DROP 0.02m / dividend 0 / 3 VE; distinct from already-mined Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_wstr")

def part_budgets():
    BUDGETS = [
        ("bud_wstr_assets_2025", "2025", "203977089", "2025 assets 203977089 UP (was 198313389); tick1475; primary official NBB WVV VOL-inb 2026-00178253"),
        ("bud_wstr_current_2025", "2025", "17782819", "2025 vlottend 17782819 (was 19311653); tick1475; primary official NBB WVV"),
        ("bud_wstr_cash_2025", "2025", "3750757", "2025 liquide middelen 3750757 DROP (was 6201122); tick1475; primary official NBB WVV"),
        ("bud_wstr_strecv_2025", "2025", "1770431", "2025 ST vorderingen 1770431 (was 1153824); tick1475; primary official NBB WVV"),
        ("bud_wstr_trade_2025", "2025", "1509571", "2025 handelsvorderingen 1509571 (was 937602); tick1475; primary official NBB WVV"),
        ("bud_wstr_othrecv_2025", "2025", "260860", "2025 overige ST vorderingen 260860 (was 216222); tick1475; primary official NBB WVV"),
        ("bud_wstr_voorraden_2025", "2025", "304633", "2025 voorraden 304633 JUMP (was 7110; onroerend verkoop 300016); tick1475; primary official NBB WVV"),
        ("bud_wstr_prepaid_2025", "2025", "1425831", "2025 overlopend actief 1425831 (was 1420660); tick1475; primary official NBB WVV"),
        ("bud_wstr_geldbeleg_2025", "2025", "10531167", "2025 geldbeleggingen 10531167 (termijnrekeningen); tick1475; primary official NBB WVV"),
        ("bud_wstr_fixed_2025", "2025", "186194270", "2025 vaste activa 186194270 (was 179001736); tick1475; primary official NBB WVV"),
        ("bud_wstr_iva_2025", "2025", "0", "2025 IVA 0 (6.2.3 fully depreciated 26509); tick1475; primary official NBB WVV"),
        ("bud_wstr_mva_2025", "2025", "186133760", "2025 MVA 186133760 (was 178933856; terreinen/gebouwen 175545176 in aanbouw 10185723); tick1475; primary official NBB WVV"),
        ("bud_wstr_fva_2025", "2025", "60510", "2025 FVA 60510 (aandelen 41933 borg 18577); tick1475; primary official NBB WVV"),
        ("bud_wstr_equity_2025", "2025", "35164736", "2025 eigen vermogen 35164736 DROP (was 35447882); tick1475; primary official NBB WVV"),
        ("bud_wstr_inbreng_2025", "2025", "399594", "2025 inbreng 399594 (onbeschikbaar 399594); tick1475; primary official NBB WVV"),
        ("bud_wstr_reserves_2025", "2025", "20530169", "2025 reserves 20530169 (was 20505423); tick1475; primary official NBB WVV"),
        ("bud_wstr_kapsubs_2025", "2025", "14234973", "2025 kapitaalsubsidies 14234973 DROP (was 14542865); tick1475; primary official NBB WVV"),
        ("bud_wstr_voorz_2025", "2025", "4657096", "2025 voorzieningen+uitgestelde belasting 4657096; tick1475; primary official NBB WVV"),
        ("bud_wstr_debt_2025", "2025", "164155257", "2025 schulden 164155257 JUMP (was 157593155); tick1475; primary official NBB WVV"),
        ("bud_wstr_ltdebt_2025", "2025", "152671550", "2025 LT schulden 152671550 (was 146809151; fin krediet 150407102); tick1475; primary official NBB WVV"),
        ("bud_wstr_stdebt_2025", "2025", "10479762", "2025 ST schulden 10479762 (was 9775635); tick1475; primary official NBB WVV"),
        ("bud_wstr_lev_2025", "2025", "2245769", "2025 leveranciers 2245769 (was 1973246); tick1475; primary official NBB WVV"),
        ("bud_wstr_bezold_2025", "2025", "436748", "2025 bezoldigingen-schulden 436748 (was 317260); tick1475; primary official NBB WVV"),
        ("bud_wstr_taxpay_2025", "2025", "979123", "2025 belastingschulden 979123 (was 1000953); tick1475; primary official NBB WVV"),
        ("bud_wstr_deferred_2025", "2025", "1003945", "2025 overlopend passief 1003945 (was 1008369); tick1475; primary official NBB WVV"),
        ("bud_wstr_omzet_2025", "2025", "16002569", "2025 omzet 70 16002569 DROP (was 16143565); tick1475; primary official NBB WVV"),
        ("bud_wstr_diensten_2025", "2025", "6853374", "2025 diensten 61 6853374 JUMP (was 5500162); tick1475; primary official NBB WVV"),
        ("bud_wstr_aankopen_2025", "2025", "12022", "2025 handelsgoederen/grondstoffen 60 12022 (aankopen 309545 voorraad -297523); tick1475; primary official NBB WVV"),
        ("bud_wstr_pers_2025", "2025", "2885619", "2025 pers 62 2885619; 30.3 VTE vs 23.2; 43851 uur; YE 34; tick1475; primary official NBB WVV"),
        ("bud_wstr_afschr_2025", "2025", "6540248", "2025 afschrijvingen 6540248; tick1475; primary official NBB WVV"),
        ("bud_wstr_expl_2025", "2025", "-235927", "2025 bedrijfsverlies -235927 (was +620079); tick1475; primary official NBB WVV"),
        ("bud_wstr_finopbr_2025", "2025", "3803141", "2025 financiele opbrengsten 3803141 (interestsubs 3158306); tick1475; primary official NBB WVV"),
        ("bud_wstr_finkost_2025", "2025", "3575071", "2025 financiele kosten 3575071; tick1475; primary official NBB WVV"),
        ("bud_wstr_pnl_2025", "2025", "24748", "2025 PnL 24748 DROP (was 1073669); tick1475; primary official NBB WVV"),
        ("bud_wstr_div_2025", "2025", "0", "2025 dividend 0 vergoeding van de inbreng empty; tick1475; primary official NBB WVV"),
        ("bud_wstr_capex_2025", "2025", "13967360", "2025 capex MVA aanschaf 13967360 (terreinen 2667723 + meubilair 85572 + in aanbouw 11214065); tick1475; primary official NBB WVV"),
        ("bud_wstr_bedrijfsopbr_2025", "2025", "17152216", "2025 bedrijfsopbrengsten 70/76A 17152216; tick1475; primary official NBB WVV"),
        ("bud_wstr_bedrijfskost_2025", "2025", "17388143", "2025 bedrijfskosten 60/66A 17388143; tick1475; primary official NBB WVV"),
        ("bud_wstr_in_aanbouw_2025", "2025", "10185723", "2025 activa in aanbouw 10185723 DROP (was 11955319); tick1475; primary official NBB WVV"),
        ("bud_wstr_krediet_2025", "2025", "150407102", "2025 LT kredietinstellingen 150407102 JUMP (was 144612091); tick1475; primary official NBB WVV"),
        ("bud_wstr_terreinen_2025", "2025", "175545176", "2025 terreinen en gebouwen 175545176 (was 166526690); tick1475; primary official NBB WVV"),
        ("bud_wstr_interim_2025", "2025", "403256", "2025 interim 2.5 VTE kosten 403256; tick1475; primary official NBB WVV"),
        ("bud_wstr_huur_2025", "2025", "14414216", "2025 6.10 opbrengsten uit verhuur 14414216; tick1475; primary official NBB WVV"),
        ("bud_wstr_doorverhuur_2025", "2025", "1588353", "2025 6.10 opbrengsten doorverhuur 1588353; tick1475; primary official NBB WVV"),
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
        f"{COMM},Woonstroom JR2025 leftover woonmaatschappij dual (omzet 16.00m DROP / diensten 6.85m JUMP / pers 2.89m 30.3 VTE JUMP / debt 164.16m / cash 3.75m DROP / PnL DROP 0.02m / dividend 0 / 3 VE),{ENT},Duffel-Lier-Bonheiden / mined Duffel dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-27,1968,,16002569,,,active,{PDF},Local leftover woonmaatschappij map VL Duffel-Lier-Bonheiden — omzet 16.00m DROP / pers 2.89m 30.3 VTE JUMP / debt 164.16m / cash 3.75m DROP,Publish omzet split + 3 VE payroll + cash 3.75m DROP + LT krediet 150.41m counterparties + capex 13.97m + aandeel % Duffel/Lier/Bonheiden/SKW/OCMW/private + dividend 0; do not keep leftover woonmaatschappij as unpublished 16.00m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Duffel>Woonmaatschappij>Woonstroom>JR2025_L5,tick1475; assets 203977089 omzet 16002569 diensten 6853374 pers 2885619 pnl 24748 equity 35164736 cash 3750757 debt 164155257 capex 13967360 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT Thuisrand / Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92 / leftover Woonkade / leftover Woonveer",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Woonstroom JR2025 leftover woonmaatschappij: omzet 16.00m DROP / diensten 6.85m JUMP / pers 2.89m 30.3 VTE JUMP / debt 164.16m / cash 3.75m DROP / PnL DROP 0.02m / dividend 0 / 3 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Duffel>Woonmaatschappij>Woonstroom>JR2025_L5,16002569,203977089,Leftover dual woonmaatschappij shell: assets 203.98m / equity 35.16m / omzet 16.00m DROP / diensten 6.85m JUMP / pers 2.89m 30.3 VTE JUMP / cash 3.75m DROP / debt 164.16m / LT krediet 150.41m / PnL DROP 0.02m / dividend 0 / 3 VE; do not treat 16.00m as TE-additive of 348bn,strong,{SRC},Woonstroom / mined Duffel-Lier-Bonheiden dual housing,Local leftover woonmaatschappij map VL Duffel-Lier-Bonheiden — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 16.00m DROP / pers 2.89m 30.3 VTE JUMP / debt 164.16m / cash 3.75m DROP / PnL DROP 0.02m / dividend 0 / 3 VE,7.0,7.0,3.0,7.0,Publish omzet split + 3 VE payroll + cash 3.75m DROP + LT krediet 150.41m counterparties + capex 13.97m + aandeel % Duffel/Lier/Bonheiden/SKW/OCMW/private + dividend 0; do not keep leftover woonmaatschappij as unpublished 16.00m housing shell,active,,tick1475; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Gemeenten>Duffel>Woonmaatschappij>Woonstroom>JR2025_L5,{ENT},omzet 16002569 DROP vs 16143565 + diensten 6853374 JUMP vs 5500162 + pers 2885619 30.3 VTE JUMP vs 23.2 + 3 VE + cash 3750757 DROP vs 6201122 + debt 164155257 LT krediet 150407102 + voorraden 304633 JUMP + capex 13967360 in aanbouw aanschaf 11214065 + PnL DROP 24748 vs 1073669 + dividend 0 + commissaris 18150 + bestuurders 37170 + aandeel % Duffel/Lier/Bonheiden/SKW/OCMW/private unpublished,Leftover woonmaatschappij Woonstroom after leftover AGB/APB hunt: omzet 16.00m DROP / pers 2.89m 30.3 VTE JUMP / debt 164.16m / cash 3.75m DROP / PnL DROP 0.02m / dividend 0 / 3 VE hides municipal housing vehicle,8,Woonstroom / Bestuursorgaan / voorzitter Franquet Marc,info@woonstroom.be,Nieuwstraat 3 2570 Duffel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1475 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF now extracted (3332034 bytes 66p). FOI ready not sent. NOT every-10. NOT Thuisrand / Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / Toerisme Limburg / Toerisme Vlaams-Brabant / Toerisme Oost-Vlaanderen / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 403 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still no separate APB 2025 PDF. WoonST Temse still JR2024 as of 1467. stek92 still JR2024 as of 1473. Leftover Woonkade 2026-00140460 live this tick unused.",
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
    if not last_s.startswith("rq_1475,"):
        raise SystemExit(f"expected last row rq_1475, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1475 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1475,Woonstroom JR2025 leftover dual residual,hole_fill,5,done,L5,wm_wstr,"
        "Completed: Woonstroom leftover woonmaatschappij of mined Duffel + Lier + Bonheiden + Sint-Katelijne-Waver after leftover AGB/APB hunt; KBO 0404.033.605 Actief; live JR2025 official NBB WVV VOL-inb PDF (3332034 bytes 66p; deposit 2026-00178253; AV 27.05.2026; header 12.06.2026; pdfinfo 20.06.2026 03:32:20 UTC). PDF header Woonstroom / Nieuwstraat 3 — NOT Thuisrand / Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Sourced euros assets 203977089 omzet 16002569 diensten 6853374 pers 2885619 30.3 VTE pnl 24748 equity 35164736 cash 3750757 debt 164155257 capex 13967360 dividend 0. FOI "
        f"{GAP} ready not sent. Distinct from already-mined Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461.,"
        f"{GAP},2026-08-19T17:23:00Z,{TS},"
        "tick1475 Woonstroom leftover woonmaatschappij residual; KBO 0404.033.605; live JR2025 official NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1476 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (Woonkade 2026-00140460 live unused)"
    )
    spawn = (
        "rq_1476,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill: Next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1475 done including Woonstroom 1475 leftover woonmaatschappij live official NBB WVV / Thuisrand 1474 leftover woonmaatschappij live official NBB WVV / Vivendo 1473 leftover woonmaatschappij live official NBB WVV / SW+ 1472 leftover woonmaatschappij live official NBB WVV / Woonhaven 1471 leftover woonmaatschappij live official NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 403/404 as of 1475). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1475). Do NOT confuse with already-mined Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live. Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1471 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1461. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonhaven TAKEN 1471; SW+ TAKEN 1472; Vivendo TAKEN 1473; Thuisrand TAKEN 1474; Woonstroom TAKEN 1475; leftover Woonkade Rupelstreek 0452.753.537 deposit 2026-00140460 live unused this tick; leftover Woonveer 0406.039.624 2026-00187904 live VERKORT unused; WoonST Temse still JR2024 as of 1467; stek92 still JR2024 as of 1473). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461.,,"
        f"{TS},{TS},"
        "spawned tick1475 after Woonstroom leftover woonmaatschappij live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (Woonkade 2026-00140460 live unused)"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1475=done + rq_1476 spawned; keep", last_line_start)

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
    Path("/tmp/tick1475_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1475 Woonstroom leftover woonmaatschappij residual; KBO 0404.033.605; live JR2025 official NBB WVV PDF; sourced euros assets 203977089 omzet 16002569 diensten 6853374 pers 2885619 30.3 VTE pnl 24748 equity 35164736 cash 3750757 debt 164155257 capex 13967360 dividend 0; FOI ready omzet 16.00m DROP / pers 2.89m 30.3 VTE JUMP / debt 164.16m / cash 3.75m DROP / PnL DROP 0.02m / dividend 0 / 3 VE; NOT Thuisrand / Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1476 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (Woonkade 2026-00140460 live unused); FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1475,1475,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1475")

    entry = (
        "\n## Tick 1475 - 2026-08-19 - rq_1475 Woonstroom Duffel dual residual leftover\n"
        "- Unit: Woonstroom BV (leftover woonmaatschappij / social-housing BV of mined Duffel + Lier + Bonheiden + Sint-Katelijne-Waver; 3 VE) after residual dual hunt (KBO **0404.033.605**; official NBB WVV VOL-inb PDF **3332034** bytes / 66p; deposit **2026-00178253**; AV **27.05.2026**; header **12.06.2026**; pdfinfo created **20.06.2026 03:32:20 UTC**; model **VOL-inb** 26.0.15 m82-f; commissaris Luc Callaert BV B00342 / 0463.716.022 / Callaert Luc A01123 mandate 22.05.2024–26.05.2027 fee **18150**; VOL-inb 6.1/6.2.1/6.2.2/6.2.4/6.2.5/6.3.4/6.4.1/6.4.2/6.5.1/6.5.2/6.7.2/6.15/6.17/6.18.2/6.20/9/12/13/14/15 not filed; 6.2.3 IVA + 6.3 MVA + 6.4.3 FVA + 6.6 + 6.7.1 + 6.8 + 6.9 + 6.10 + 6.11 + 6.12 + 6.13 + 6.14 + 6.16 + 6.18.1 + 6.19 + sociale balans + commissarisverslag + remuneratieverslag filed). Leftover AGB/APB first: leftover APB Inovant / Atlas koepel slugs empty / provincieantwerpen.be **403** even with Googlebot UA; no fetchable 2025 Inovant/Atlas PDF (do not take Hooibeekhoeve). Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick (puyenbroeck.be redirects). Leftover AGB Herzele already in entities (tick1163) — skipped. Leftover AGB Bornem still 2024 (2026-00553588 HEAD 403). Leftover AGB Duffel already in entities — skipped. Leftover SOLag Lier already in entities — skipped. Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 last JR still 2024-12-31 as of 1471. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover WoonST Temse still JR2024 as of 1467. Leftover stek92 still JR2024 as of 1473. Leftover Woonstroom statutory CDN `2026-00178253` live this tick (HTTP 200 / application/pdf / 3332034 / 66p; jaar **2025-12-31**; neerlegging **12.06.2026**) — taken (hunt order #2 leftover unmined woonmaatschappij of mined Duffel+Lier+Bonheiden with live 2025 statutory PDF after leftover AGB/APB hunt). PDF header **Woonstroom / Nieuwstraat 3 / 2570 Duffel** — NOT Thuisrand / Vivendo / SW+ / Woonhaven / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Distinct from already-mined **Thuisrand 1474** / **Vivendo 1473** / **SW+ 1472** / **Woonhaven 1471** / **Thuispunt Gent 1470** / **Tuinwijk 1469** / **Dijledal 1468** / **Dender-Zuid 1467** / **Dimensa 1466** / **Woonmaatschappij Rivierenland 1465** / **Woonpunt Waas 1464**. First confirmed not already extracted as JR2025 euros: no Woonstroom / 0404.033.605 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **01.01.1968**; statutaire naam Woonstroom since 19.06.2023; BV since 19.06.2023; zetel Nieuwstraat 3 2570 Duffel since 17.05.2023; **3 VE**; 14 functiehouders; voorzitter Franquet Marc since 26.03.2025; ondervoorzitter Wuyts Luc; dagelijks bestuur Vanden Eynde Marc + Verhoye Kristina; Werkgever RSZ since 01.01.1945; btw since 01.01.2006; aanbestedende overheid; NACE 68.121 / 68.203 / 68.202; site https://woonstroom.be/; werkingsgebied Duffel + Lier + Bonheiden + Sint-Katelijne-Waver. Absorbeerde 0404.067.356 since 19.06.2023. Prior-year figures **identiek**. SBM used for deposit-id discovery only (SBM table 1-euro-off vs PDF). Euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1480).\n"
        "- EUR strong (primary official WVV VOL-inb; omzet 70 **16002569** DROP vs 16143565; 6.10 split huur **14414216** / doorverhuur **1588353** / verkoop 0; diensten 61 **6853374** JUMP vs 5500162; pers 62 **2885619** / **30,3 VTE** JUMP vs 2199069 / 23,2): assets **203977089** (was 198313389); fixed **186194270** vs 179001736 / IVA empty / MVA **186133760** vs 178933856 (terreinen/gebouwen **175545176**; installaties **211**; meubilair **163380**; overige **239270**; in aanbouw **10185723 DROP** vs 11955319) / FVA **60510**; current **17782819** vs 19311653; voorraden **304633 JUMP** vs 7110 (onroerend verkoop **300016**); ST recv **1770431** (trade **1509571** / other **260860**); LT recv empty; geldbeleg **10531167**; cash **3750757 DROP** vs 6201122; prepaid **1425831**; equity **35164736 DROP** vs 35447882 (inbreng **399594**; reserves **20530169**; overgedragen empty; kapsubs **14234973 DROP** vs 14542865); voorzieningen **4657096** (grote herstellingen **3928173**; overige **63505**; uitgestelde belasting **665418**); schulden **164155257 JUMP** vs 157593155 (LT **152671550** waarvan fin krediet **150407102 JUMP** vs 144612091; ST **10479762** waarvan 42 **6246001** + leveranciers **2245769**; deferred **1003945**); omzet **16002569** DROP; 60 **12022**; diensten **6853374** JUMP; pers **2885619** / **30,3 VTE** / 43851 uur / YE **34** vs 28 / YE VTE **32,6**; interim **2,5 VTE** 403256; afschr **6540248**; expl **-235927** vs +620079; fin opbr **3803141** (interestsubs 3158306); fin kosten **3575071**; tax **-8643**; PnL **9904 +24748 DROP** vs +1073669 (te bestemmen 9905 **24748**); dividend **0**; capex MVA aanschaf **13967360** (terreinen 2667723 + meubilair 85572 + in aanbouw 11214065). Commissaris fee **18150**. Bestuurders 9503 **37170**. 3 VE. 6.7.2 aandeel % unpublished. Cross-checks: 186194270+17782819=203977089; 35164736+4657096+164155257=203977089; 17152216-17388143=-235927; -235927+3803141-3575071=-7857; -7857+23962-(-8643)=24748; 14414216+1588353=16002569; 2667723+85572+11214065=13967360. SBM table 1-euro-off vs PDF.\n"
        "- CSVs: sources +4; entities +1 `wm_wstr` parent `city_duffel`; budgets +44 executed; commitments +1 envelope 16002569 AV 27.05.2026; leaderboard +1 annual 16002569 / total 203977089; foi_queue +1 status=ready never sent; research_queue surgical rq_1475=done + rq_1476 spawn; loop_state ticks_completed=1475. Inventory after write: budgets {INV_B} · commitments {INV_C} · leaderboard {INV_L} · entities {INV_E} · sources {INV_S} · FOI ready {FOI_R} / answered {FOI_A} / partial {FOI_P} / total {FOI_T}.\n"
        "- FOI: `gap_wstr_omzet_16_00m_pers_2_89m_debt_164m_l5` ready not sent — omzet 16.00m DROP / 6.10 split huur 14.41m doorverhuur 1.59m / diensten 6.85m JUMP / pers 2.89m 30.3 VTE JUMP / 3 VE / cash DROP 3.75m / debt 164.16m LT krediet 150.41m / voorraden JUMP 0.30m / capex 13.97m / PnL DROP 0.02m / dividend 0 / commissaris 18.15k / aandeel % unpublished.\n"
        "- Next: rq_1476 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 403 this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1475). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live. Leftover IGS IVAREM **0267.403.264** still JR2024 as of 1471. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonhaven **0403.795.657** TAKEN 1471; SW+ **0405.342.610** TAKEN 1472; Vivendo **0406.062.883** TAKEN 1473; Thuisrand **0404.710.724** TAKEN 1474; Woonstroom **0404.033.605** TAKEN 1475; leftover Woonkade Rupelstreek **0452.753.537** deposit **2026-00140460** live unused this tick; leftover Woonveer Klein-Brabant **0406.039.624** 2026-00187904 live VERKORT unused; WoonST Temse still JR2024 as of 1467; stek92 still JR2024 as of 1473). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460. Next every-10 is **1480**. Provincial tourism VZWs now exhausted (Westtoer + TOV + TVLB + TLim).\n"
    )
    entry = entry.replace("{INV_B}", str(inv["budgets.csv"])).replace("{INV_C}", str(inv["commitments.csv"])).replace("{INV_L}", str(inv["leaderboard.csv"])).replace("{INV_E}", str(inv["entities.csv"])).replace("{INV_S}", str(inv["sources.csv"])).replace("{FOI_R}", str(foi_ready)).replace("{FOI_A}", str(foi_ans)).replace("{FOI_P}", str(foi_part)).replace("{FOI_T}", str(foi_tot))
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1475 -" in lraw:
        raise SystemExit("loop_log already has tick 1475 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1475")
    print("DONE tick 1475")

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

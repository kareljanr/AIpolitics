#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1474 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T17:45:00Z"
ENT = "wm_thrn"
SRC = "src_thrn_jr2025_nbb"
GAP = "gap_thrn_omzet_11_16m_pers_2_66m_loss_1_66m_l5"
LB = "lb_thrn_omzet_11_16m_pers_2_66m_loss_1_66m"
COMM = "comm_thrn_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00140988.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Thuisrand official NBB WVV VOL-inb JR2025,{PDF},NBB / Thuisrand,2026-08-19,budget,tick1474; official NBB WVV VOL-inb JR2025 PDF 59p / 732363 bytes; deposit 2026-00140988; AV 28.05.2026; header 04.06.2026; pdfinfo created 06.06.2026 02:07:46 UTC; model VOL-inb 25.0.12 m82-f; KBO 0404.710.724; assets 143365723 cash 2273845 debt 121507096 pers 2659320 omzet 11157176 diensten 7086182 pnl -1661853 equity 19686816",
        "src_thrn_site,Thuisrand official pages,https://thuisrand.be/,Thuisrand / mined Mortsel-Zuidrand,2026-08-19,official_register,tick1474; leftover woonmaatschappij of mined Stad Mortsel + Aartselaar + Boechout + Edegem + Hove + Kontich + Lint; zetel Diksmuidelaan 276 2600 Berchem; KBO 0404.710.724; SBM used for deposit-id discovery only",
        "src_thrn_jaarverslag,Thuisrand official JR2025 jaarverslag,https://thuisrand.be/assets/files/Jaarverslag-boekjaar-2025.pdf,Thuisrand,2026-08-19,official_register,tick1474; official jaarverslag 11923268 bytes last-modified 27.05.2026; used for header/werkingsgebied only; euros from NBB VOL-inb PDF",
        "src_kbo_thrn_0404710724,KBO Thuisrand 0404.710.724,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0404710724,KBO Public Search FOD Economie,2026-08-19,official_register,tick1474; Actief since 01.01.1968; BV since 01.07.2023; naam Thuisrand since 01.07.2023; zetel Diksmuidelaan 276 2600 Antwerpen; 1 VE; 11 functiehouders; Werkgever RSZ since 01.01.1945; aanbestedende overheid",
        "src_thrn_foi_contact,Thuisrand FOI channel (info@thuisrand.be),https://thuisrand.be/,Thuisrand,2026-08-19,official_register,tick1474; leftover woonmaatschappij of mined Mortsel-Zuidrand; NOT Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92",
    ])
    print("sources +5")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_thrn," in raw or raw.startswith(b"wm_thrn,"):
        raise SystemExit("wm_thrn already present")
    if b"0404.710.724" in raw or b"0404710724" in raw:
        raise SystemExit("Thuisrand KBO already present as entity")
    row = (
        "wm_thrn,Thuisrand (leftover woonmaatschappij / social-housing BV of mined Stad Mortsel + Aartselaar + Boechout + Edegem + Hove + Kontich + Lint; NOT Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92),"
        "Thuisrand SRL (logement social residuel Mortsel-Zuidrand),"
        "Thuisrand leftover social-housing company of mined Mortsel-Zuidrand (not Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92),"
        "other,city_mortsel,nl,https://thuisrand.be/,info@thuisrand.be,Diksmuidelaan 276 2600 Berchem (Antwerpen),"
        "tick1474 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0404.710.724 Actief since 01.01.1968; live JR2025 official NBB WVV PDF; sourced euros assets 143365723 omzet 11157176 diensten 7086182 pers 2659320 25.1 VTE pnl -1661853 equity 19686816 cash 2273845 debt 121507096 capex 13191657 dividend 0; FOI ready omzet 11.16m UP / pers 2.66m 25.1 VTE DROP / debt 121.51m / cash 2.27m DROP 50% / PnL LOSS 1.66m / dividend 0 / 1 VE; distinct from already-mined Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_thrn")

def part_budgets():
    BUDGETS = [
        ("bud_thrn_assets_2025", "2025", "143365723", "2025 assets 143365723 DROP (was 148955903); tick1474; primary official NBB WVV VOL-inb 2026-00140988"),
        ("bud_thrn_current_2025", "2025", "9419278", "2025 vlottend 9419278 (was 10655631); tick1474; primary official NBB WVV"),
        ("bud_thrn_cash_2025", "2025", "2273845", "2025 liquide middelen 2273845 DROP (was 4517512); tick1474; primary official NBB WVV"),
        ("bud_thrn_strecv_2025", "2025", "3006731", "2025 ST vorderingen 3006731 JUMP (was 980775); tick1474; primary official NBB WVV"),
        ("bud_thrn_trade_2025", "2025", "593853", "2025 handelsvorderingen 593853 (was 396353); tick1474; primary official NBB WVV"),
        ("bud_thrn_othrecv_2025", "2025", "2412878", "2025 overige ST vorderingen 2412878 JUMP (was 584422); tick1474; primary official NBB WVV"),
        ("bud_thrn_voorraden_2025", "2025", "2355470", "2025 voorraden 2355470 (was 2945598; onroerend verkoop 2344839); tick1474; primary official NBB WVV"),
        ("bud_thrn_prepaid_2025", "2025", "691191", "2025 overlopend actief 691191 (was 1198513); tick1474; primary official NBB WVV"),
        ("bud_thrn_geldbeleg_2025", "2025", "1092041", "2025 geldbeleggingen 1092041 (eigen aandelen 85041 overige 1007000); tick1474; primary official NBB WVV"),
        ("bud_thrn_fixed_2025", "2025", "133946445", "2025 vaste activa 133946445 (was 138300271); tick1474; primary official NBB WVV"),
        ("bud_thrn_iva_2025", "2025", "5310", "2025 IVA 5310 (was 484); tick1474; primary official NBB WVV"),
        ("bud_thrn_mva_2025", "2025", "133886627", "2025 MVA 133886627 (was 138245503; terreinen/gebouwen 118076319 in aanbouw 15732383); tick1474; primary official NBB WVV"),
        ("bud_thrn_fva_2025", "2025", "54507", "2025 FVA 54507 (aandelen 51223 borg 3284); tick1474; primary official NBB WVV"),
        ("bud_thrn_equity_2025", "2025", "19686816", "2025 eigen vermogen 19686816 DROP (was 22026068); tick1474; primary official NBB WVV"),
        ("bud_thrn_inbreng_2025", "2025", "107283", "2025 inbreng 107283 (onbeschikbaar 107283; Borsbeek split -3524); tick1474; primary official NBB WVV"),
        ("bud_thrn_reserves_2025", "2025", "17073577", "2025 reserves 17073577 (was 19432317); tick1474; primary official NBB WVV"),
        ("bud_thrn_kapsubs_2025", "2025", "2505956", "2025 kapitaalsubsidies 2505956 (was 2482944); tick1474; primary official NBB WVV"),
        ("bud_thrn_voorz_2025", "2025", "2171811", "2025 voorzieningen+uitgestelde belasting 2171811; tick1474; primary official NBB WVV"),
        ("bud_thrn_debt_2025", "2025", "121507096", "2025 schulden 121507096 DROP (was 124449616); tick1474; primary official NBB WVV"),
        ("bud_thrn_ltdebt_2025", "2025", "111655684", "2025 LT schulden 111655684 (was 111475369; fin krediet 110154029); tick1474; primary official NBB WVV"),
        ("bud_thrn_stdebt_2025", "2025", "9036246", "2025 ST schulden 9036246 (was 11688670); tick1474; primary official NBB WVV"),
        ("bud_thrn_lev_2025", "2025", "1666140", "2025 leveranciers 1666140 (was 2254467); tick1474; primary official NBB WVV"),
        ("bud_thrn_bezold_2025", "2025", "563442", "2025 bezoldigingen-schulden 563442 (was 247159); tick1474; primary official NBB WVV"),
        ("bud_thrn_taxpay_2025", "2025", "596177", "2025 belastingschulden 596177 (was 657941); tick1474; primary official NBB WVV"),
        ("bud_thrn_deferred_2025", "2025", "815166", "2025 overlopend passief 815166 (was 1285577); tick1474; primary official NBB WVV"),
        ("bud_thrn_omzet_2025", "2025", "11157176", "2025 omzet 70 11157176 UP (was 10992179); tick1474; primary official NBB WVV"),
        ("bud_thrn_diensten_2025", "2025", "7086182", "2025 diensten 61 7086182 JUMP (was 6878738); tick1474; primary official NBB WVV"),
        ("bud_thrn_aankopen_2025", "2025", "1162505", "2025 handelsgoederen/grondstoffen 60 1162505 (aankopen 572377 voorraad 590128); tick1474; primary official NBB WVV"),
        ("bud_thrn_pers_2025", "2025", "2659320", "2025 pers 62 2659320; 25.1 VTE vs 28.2; 37858 uur; YE 28; tick1474; primary official NBB WVV"),
        ("bud_thrn_afschr_2025", "2025", "2949583", "2025 afschrijvingen 2949583; tick1474; primary official NBB WVV"),
        ("bud_thrn_expl_2025", "2025", "-1364190", "2025 bedrijfsverlies -1364190 (was +401689); tick1474; primary official NBB WVV"),
        ("bud_thrn_finopbr_2025", "2025", "1816138", "2025 financiele opbrengsten 1816138 (interestsubs 1727810); tick1474; primary official NBB WVV"),
        ("bud_thrn_finkost_2025", "2025", "2097391", "2025 financiele kosten 2097391; tick1474; primary official NBB WVV"),
        ("bud_thrn_pnl_2025", "2025", "-1661853", "2025 PnL -1661853 LOSS (was -7194); tick1474; primary official NBB WVV"),
        ("bud_thrn_div_2025", "2025", "0", "2025 dividend 0 vergoeding van de inbreng empty; tick1474; primary official NBB WVV"),
        ("bud_thrn_capex_2025", "2025", "13191657", "2025 capex MVA aanschaf 13191657 (terreinen 1091493 + overige 29714 + in aanbouw 12070450); tick1474; primary official NBB WVV"),
        ("bud_thrn_bedrijfsopbr_2025", "2025", "12832176", "2025 bedrijfsopbrengsten 70/76A 12832176; tick1474; primary official NBB WVV"),
        ("bud_thrn_bedrijfskost_2025", "2025", "14196367", "2025 bedrijfskosten 60/66A 14196367; tick1474; primary official NBB WVV"),
        ("bud_thrn_in_aanbouw_2025", "2025", "15732383", "2025 activa in aanbouw 15732383 JUMP (was 11125490); tick1474; primary official NBB WVV"),
        ("bud_thrn_krediet_2025", "2025", "110154029", "2025 LT kredietinstellingen 110154029 (was 109974803); tick1474; primary official NBB WVV"),
        ("bud_thrn_terreinen_2025", "2025", "118076319", "2025 terreinen en gebouwen 118076319 (was 127057390); tick1474; primary official NBB WVV"),
        ("bud_thrn_interim_2025", "2025", "344271", "2025 interim 1.1 VTE kosten 344271; tick1474; primary official NBB WVV"),
        ("bud_thrn_huur_2025", "2025", "6929526", "2025 6.10 sociale huurwoningen 6929526; tick1474; primary official NBB WVV"),
        ("bud_thrn_doorverhuur_2025", "2025", "2148942", "2025 6.10 sociale doorverhuur 2148942; tick1474; primary official NBB WVV"),
        ("bud_thrn_koop_2025", "2025", "1020566", "2025 6.10 sociale koopwoningen 1020566; tick1474; primary official NBB WVV"),
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
        f"{COMM},Thuisrand JR2025 leftover woonmaatschappij dual (omzet 11.16m UP / diensten 7.09m JUMP / pers 2.66m 25.1 VTE DROP / debt 121.51m / cash 2.27m DROP 50% / PnL LOSS 1.66m / dividend 0 / 1 VE),{ENT},Mortsel-Zuidrand / mined Mortsel dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-28,1968,,11157176,,,active,{PDF},Local leftover woonmaatschappij map VL Mortsel-Zuidrand — omzet 11.16m UP / pers 2.66m 25.1 VTE DROP / debt 121.51m / cash 2.27m DROP,Publish omzet split + 1 VE payroll + cash 2.27m DROP + LT krediet 110.15m counterparties + capex 13.19m + aandeel % Mortsel/Aartselaar/Boechout/Edegem/Hove/Kontich/Lint/OCMW/private + Borsbeek split + dividend 0; do not keep leftover woonmaatschappij as unpublished 11.16m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Mortsel>Woonmaatschappij>Thuisrand>JR2025_L5,tick1474; assets 143365723 omzet 11157176 diensten 7086182 pers 2659320 pnl -1661853 equity 19686816 cash 2273845 debt 121507096 capex 13191657 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Thuisrand JR2025 leftover woonmaatschappij: omzet 11.16m UP / diensten 7.09m JUMP / pers 2.66m 25.1 VTE DROP / debt 121.51m / cash 2.27m DROP 50% / PnL LOSS 1.66m / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Mortsel>Woonmaatschappij>Thuisrand>JR2025_L5,11157176,143365723,Leftover dual woonmaatschappij shell: assets 143.37m / equity 19.69m / omzet 11.16m UP / diensten 7.09m JUMP / pers 2.66m 25.1 VTE DROP / cash 2.27m DROP 50% / debt 121.51m / LT krediet 110.15m / PnL LOSS 1.66m / dividend 0 / 1 VE; do not treat 11.16m as TE-additive of 348bn,strong,{SRC},Thuisrand / mined Mortsel-Zuidrand dual housing,Local leftover woonmaatschappij map VL Mortsel-Zuidrand — JR2025 official NBB WVV live; omzet+pers+debt+cash+loss FOI,Official NBB WVV 2026-08-19: omzet 11.16m UP / pers 2.66m 25.1 VTE DROP / debt 121.51m / cash 2.27m DROP 50% / PnL LOSS 1.66m / dividend 0 / 1 VE,7.0,7.0,3.0,7.0,Publish omzet split + 1 VE payroll + cash 2.27m DROP + LT krediet 110.15m counterparties + capex 13.19m + aandeel % Mortsel/Aartselaar/Boechout/Edegem/Hove/Kontich/Lint/OCMW/private + Borsbeek split + dividend 0; do not keep leftover woonmaatschappij as unpublished 11.16m housing shell,active,,tick1474; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Gemeenten>Mortsel>Woonmaatschappij>Thuisrand>JR2025_L5,{ENT},omzet 11157176 UP vs 10992179 + diensten 7086182 JUMP vs 6878738 + pers 2659320 25.1 VTE vs 28.2 + 1 VE + cash 2273845 DROP vs 4517512 + debt 121507096 LT krediet 110154029 + voorraden 2355470 onroerend 2344839 + capex 13191657 in aanbouw JUMP 15732383 vs 11125490 + PnL LOSS -1661853 vs -7194 + dividend 0 + commissaris 9500 + extra 2500 + aandeel % Mortsel/Aartselaar/Boechout/Edegem/Hove/Kontich/Lint/OCMW/private unpublished + Borsbeek split to Woonhaven,Leftover woonmaatschappij Thuisrand after leftover AGB/APB hunt: omzet 11.16m UP / pers 2.66m 25.1 VTE DROP / debt 121.51m / cash 2.27m DROP 50% / PnL LOSS 1.66m / dividend 0 / 1 VE hides municipal housing vehicle,8,Thuisrand / Bestuursorgaan / voorzitter Vanbaeden Cindy,info@thuisrand.be,Diksmuidelaan 276 2600 Berchem (Antwerpen),docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1474 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF now extracted (732363 bytes 59p). FOI ready not sent. NOT every-10. NOT Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / Toerisme Limburg / Toerisme Vlaams-Brabant / Toerisme Oost-Vlaanderen / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still no separate APB 2025 PDF. WoonST Temse still JR2024 as of 1467. stek92 still JR2024 as of 1473.",
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
    if not last_s.startswith("rq_1474,"):
        raise SystemExit(f"expected last row rq_1474, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1474 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1474,Thuisrand JR2025 leftover dual residual,hole_fill,5,done,L5,wm_thrn,"
        "Completed: Thuisrand leftover woonmaatschappij of mined Stad Mortsel + Aartselaar + Boechout + Edegem + Hove + Kontich + Lint after leftover AGB/APB hunt; KBO 0404.710.724 Actief; live JR2025 official NBB WVV VOL-inb PDF (732363 bytes 59p; deposit 2026-00140988; AV 28.05.2026; header 04.06.2026; pdfinfo 06.06.2026 02:07:46 UTC). PDF header Thuisrand BV / Diksmuidelaan 276 — NOT Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Sourced euros assets 143365723 omzet 11157176 diensten 7086182 pers 2659320 25.1 VTE pnl -1661853 equity 19686816 cash 2273845 debt 121507096 capex 13191657 dividend 0. FOI "
        f"{GAP} ready not sent. Distinct from already-mined Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461.,"
        f"{GAP},2026-08-19T17:20:00Z,{TS},"
        "tick1474 Thuisrand leftover woonmaatschappij residual; KBO 0404.710.724; live JR2025 official NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1475 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025"
    )
    spawn = (
        "rq_1475,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill: Next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1474 done including Thuisrand 1474 leftover woonmaatschappij live official NBB WVV / Vivendo 1473 leftover woonmaatschappij live official NBB WVV / SW+ 1472 leftover woonmaatschappij live official NBB WVV / Woonhaven 1471 leftover woonmaatschappij live official NBB WVV / Thuispunt Gent 1470 leftover woonmaatschappij live official NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 404 as of 1474). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1473). Do NOT confuse with already-mined Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live. Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1471 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1461. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonhaven TAKEN 1471; SW+ TAKEN 1472; Vivendo TAKEN 1473; Thuisrand TAKEN 1474; WoonST Temse still JR2024 as of 1467; stek92 still JR2024 as of 1473). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461.,,"
        f"{TS},{TS},"
        "spawned tick1474 after Thuisrand leftover woonmaatschappij live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1474=done + rq_1475 spawned; keep", last_line_start)

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
    Path("/tmp/tick1474_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1474 Thuisrand leftover woonmaatschappij residual; KBO 0404.710.724; live JR2025 official NBB WVV PDF; sourced euros assets 143365723 omzet 11157176 diensten 7086182 pers 2659320 25.1 VTE pnl -1661853 equity 19686816 cash 2273845 debt 121507096 capex 13191657 dividend 0; FOI ready omzet 11.16m UP / pers 2.66m 25.1 VTE DROP / debt 121.51m / cash 2.27m DROP 50% / PnL LOSS 1.66m / dividend 0 / 1 VE; NOT Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1475 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1474,1474,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1474")

    entry = (
        "\n## Tick 1474 - 2026-08-19 - rq_1474 Thuisrand Mortsel dual residual leftover\n"
        "- Unit: Thuisrand BV (leftover woonmaatschappij / social-housing BV of mined Stad Mortsel + Aartselaar + Boechout + Edegem + Hove + Kontich + Lint; 1 VE) after residual dual hunt (KBO **0404.710.724**; official NBB WVV VOL-inb PDF **732363** bytes / 59p; deposit **2026-00140988**; AV **28.05.2026**; header **04.06.2026**; pdfinfo created **06.06.2026 02:07:46 UTC**; model **VOL-inb** 25.0.12 m82-f; commissaris Groupe Audit Belgium BV B00096 / 0434.720.148 / Augustinus David A02755 mandate 14.05.2024–14.05.2027 fee **9500** + extra controle 2500; VOL-inb 6.1/6.2.1/6.2.2/6.2.4/6.2.5/6.4.2/6.5.1/6.5.2/6.7.2/6.15/6.17/6.18.1/6.18.2/6.20/9/12/13/14/15 not filed; 6.2.3 IVA + 6.3 MVA + 6.6 + 6.7.1 + 6.8 + 6.9 + 6.10 + 6.11 + 6.16 + 6.19 + sociale balans + commissarisverslag + remuneratieverslag filed). Leftover AGB/APB first: leftover APB Inovant / Atlas Foleon `jaarrekening_25_inov` / `jaarrekening_25_atlas` HEAD **404** this tick; provincieantwerpen.be locaties/inovant / locaties/atlas **404**; Foleon leftover slugs **403**; no fetchable 2025 Inovant/Atlas PDF (do not take Hooibeekhoeve). Leftover Puyenbroeck still no separate APB 2025 statutory PDF as of 1473. Leftover AGB Herzele already in entities (tick1163) — skipped. Leftover AGB Bornem still 2024. Leftover AGB Mortsel / Kontich / Boechout / Hove / Edegem already in entities — skipped. Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 last JR still 2024-12-31 as of 1471. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover WoonST Temse still JR2024 as of 1467. Leftover stek92 still JR2024 as of 1473. Leftover Thuisrand statutory CDN `2026-00140988` live this tick (HTTP 200 / application/pdf / 732363 / 59p; jaar **2025-12-31**; neerlegging **04.06.2026**) — taken (hunt order #2 leftover unmined woonmaatschappij of mined Mortsel-Zuidrand with live 2025 statutory PDF after leftover AGB/APB hunt). PDF header **Thuisrand BV / Diksmuidelaan 276 / 2600 Berchem (Antwerpen)** — NOT Vivendo / SW+ / Woonhaven / Thuispunt Gent / Dimensa / Tuinwijk / Dijledal / Dender-Zuid / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck / Integratie Atlas 1266. Distinct from already-mined **Vivendo 1473** / **SW+ 1472** / **Woonhaven 1471** / **Thuispunt Gent 1470** / **Tuinwijk 1469** / **Dijledal 1468** / **Dender-Zuid 1467** / **Dimensa 1466** / **Woonmaatschappij Rivierenland 1465** / **Woonpunt Waas 1464** / **Toerisme Limburg 1463** / **Toerisme Vlaams-Brabant 1462** / **Toerisme Oost-Vlaanderen 1461**. First confirmed not already extracted as JR2025 euros: no Thuisrand / 0404.710.724 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **01.01.1968**; statutaire naam Thuisrand since 01.07.2023; BV since 01.07.2023; zetel Diksmuidelaan 276 2600 Antwerpen since 01.01.1983; **1 VE**; 11 functiehouders; voorzitter Vanbaeden Cindy since 01.07.2023; ondervoorzitter Peeters Jos; bestuurder-zaakvoerder Janssen Daan since 01.05.2023; Werkgever RSZ since 01.01.1945; btw since 01.09.1995; aanbestedende overheid; NACE 68.202 / 68.203; site https://thuisrand.be/; werkingsgebied Stad Mortsel + Aartselaar + Boechout + Edegem + Hove + Kontich + Lint. Borsbeek transferred to Woonhaven (6.7.1 inbreng **-3524**). Prior-year figures **identiek**. SBM used for deposit-id discovery only. Euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1480).\n"
        "- EUR strong (primary official WVV VOL-inb; omzet 70 **11157176** UP vs 10992179; 6.10 split huur **6929526** / doorverhuur **2148942** / koop **1020566** / huurlasten **1058141**; diensten 61 **7086182** JUMP vs 6878738; pers 62 **2659320** / **25,1 VTE** vs 2454106 / 28,2): assets **143365723** (was 148955903); fixed **133946445** vs 138300271 / IVA **5310** vs 484 / MVA **133886627** vs 138245503 (terreinen/gebouwen **118076319**; installaties **200**; meubilair **9217**; leasing **40223**; overige **28286**; in aanbouw **15732383 JUMP** vs 11125490) / FVA **54507**; current **9419278** vs 10655631; voorraden **2355470** (onroerend verkoop **2344839**); ST recv **3006731 JUMP** (trade **593853** / other **2412878**); LT recv empty; geldbeleg **1092041**; cash **2273845 DROP** vs 4517512; prepaid **691191**; equity **19686816 DROP** vs 22026068 (inbreng **107283**; reserves **17073577**; overgedragen empty; kapsubs **2505956**); voorzieningen **2171811** (grote herstellingen **1287886**; pensioen **36789 DROP** vs 760684; overige **110250**; uitgestelde belasting **736886**); schulden **121507096 DROP** vs 124449616 (LT **111655684** waarvan fin krediet **110154029**; ST **9036246** waarvan 42 **4353441** + leveranciers **1666140**; deferred **815166**); omzet **11157176** UP; 60 **1162505**; diensten **7086182** JUMP; pers **2659320** / **25,1 VTE** / 37858 uur / YE **28** personen vs 30; interim **1,1 VTE** 344271; afschr **2949583**; expl **-1364190** vs +401689; fin opbr **1816138**; fin kosten **2097391**; tax empty; PnL **9904 -1661853 LOSS** vs -7194 (te bestemmen 9905 **-2028335**); dividend **0**; capex MVA aanschaf **13191657** (terreinen 1091493 + overige 29714 + in aanbouw 12070450) + IVA 6251. Commissaris fee **9500**. 1 VE. 6.7.2 aandeel % unpublished. Cross-checks: 133946445+9419278=143365723; 19686816+2171811+121507096=143365723; 12832176-14196367=-1364191 vs -1364190; -1364190+1816138-2097391=-1645443 vs -1645444; -1645444+17124-33534=-1661854 vs -1661853. 1-euro rounding on expl/PnL.\n"
        "- CSVs: sources +5; entities +1 `wm_thrn` parent `city_mortsel`; budgets +45 executed; commitments +1 envelope 11157176 AV 28.05.2026; leaderboard +1 annual 11157176 / total 143365723; foi_queue +1 status=ready never sent; research_queue surgical rq_1474=done + rq_1475 spawn; loop_state ticks_completed=1474. Inventory after write: budgets {INV_B} · commitments {INV_C} · leaderboard {INV_L} · entities {INV_E} · sources {INV_S} · FOI ready {FOI_R} / answered {FOI_A} / partial {FOI_P} / total {FOI_T}.\n"
        "- FOI: `gap_thrn_omzet_11_16m_pers_2_66m_loss_1_66m_l5` ready not sent — omzet 11.16m UP / 6.10 split huur 6.93m doorverhuur 2.15m koop 1.02m huurlasten 1.06m / diensten 7.09m JUMP / pers 2.66m 25.1 VTE DROP / 1 VE / cash DROP 2.27m / debt 121.51m LT krediet 110.15m / in aanbouw JUMP 15.73m / capex 13.19m / PnL LOSS 1.66m / dividend 0 / commissaris 9.50k / aandeel % unpublished / Borsbeek split.\n"
        "- Next: rq_1475 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 404 this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1473). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live. Leftover IGS IVAREM **0267.403.264** still JR2024 as of 1471. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonhaven **0403.795.657** TAKEN 1471; SW+ **0405.342.610** TAKEN 1472; Vivendo **0406.062.883** TAKEN 1473; Thuisrand **0404.710.724** TAKEN 1474; WoonST Temse still JR2024 as of 1467; stek92 still JR2024 as of 1473). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460. Next every-10 is **1480**. Provincial tourism VZWs now exhausted (Westtoer + TOV + TVLB + TLim).\n"
    )
    entry = entry.replace("{INV_B}", str(inv["budgets.csv"])).replace("{INV_C}", str(inv["commitments.csv"])).replace("{INV_L}", str(inv["leaderboard.csv"])).replace("{INV_E}", str(inv["entities.csv"])).replace("{INV_S}", str(inv["sources.csv"])).replace("{FOI_R}", str(foi_ready)).replace("{FOI_A}", str(foi_ans)).replace("{FOI_P}", str(foi_part)).replace("{FOI_T}", str(foi_tot))
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1474 -" in lraw:
        raise SystemExit("loop_log already has tick 1474 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1474")
    print("DONE tick 1474")

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

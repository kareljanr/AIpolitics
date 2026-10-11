#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1465 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T15:50:00Z"
ENT = "wm_wriv"
SRC = "src_wriv_jr2025_nbb"
GAP = "gap_wriv_omzet_29_13m_pers_5_44m_debt_454m_l5"
LB = "lb_wriv_omzet_29_13m_pers_5_44m_debt_454m"
COMM = "comm_wriv_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00137594.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Woonmaatschappij Rivierenland official NBB WVV VOL-inb JR2025,{PDF},NBB / Woonmaatschappij Rivierenland,2026-08-19,budget,tick1465; official NBB WVV VOL-inb JR2025 PDF 66p / 5523641 bytes; deposit 2026-00137594; AV 27.05.2026; header 02.06.2026; pdfinfo created 04.06.2026 21:45:27 UTC; model VOL-inb 26.0.12 m82-f; KBO 0403.698.162; assets 523681710 cash 27666290 debt 453954887 pers 5435789 omzet 29125693 diensten 9454816 pnl -591785 equity 64764590",
        "src_wriv_site,Woonmaatschappij Rivierenland official Woonland pages,https://wmwoonland.be/wie-zijn-we/,Woonmaatschappij Rivierenland / mined Mechelen+Willebroek,2026-08-19,official_register,tick1465; leftover woonmaatschappij of mined Mechelen + Willebroek; zetel Lijsterstraat 6 2800 Mechelen; KBO 0403.698.162; NBB/SBM consult for deposit id",
        "src_kbo_wriv_0403698162,KBO Woonmaatschappij Rivierenland 0403.698.162,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0403698162,KBO Public Search FOD Economie,2026-08-19,official_register,tick1465; Actief since 01.01.1968; BV since 21.06.2023; naam Woonmaatschappij Rivierenland since 21.06.2023; zetel Lijsterstraat 6 2800 Mechelen; 2 VE 2230711572+2348316847; 16 functiehouders; Werkgever RSZ since 01.07.1953; aanbestedende overheid",
        "src_wriv_foi_contact,Woonmaatschappij Rivierenland FOI channel (info@wmwoonland.be),https://wmwoonland.be/,Woonmaatschappij Rivierenland,2026-08-19,official_register,tick1465; leftover woonmaatschappij of mined Mechelen + Willebroek; NOT Zorgbedrijf Rivierenland / RL Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_wriv," in raw or raw.startswith(b"wm_wriv,"):
        raise SystemExit("wm_wriv already present")
    if b"0403.698.162" in raw:
        raise SystemExit("Woonmaatschappij Rivierenland KBO already present as entity")
    row = (
        "wm_wriv,Woonmaatschappij Rivierenland / Woonland (leftover woonmaatschappij / social-housing BV of mined Mechelen + Willebroek; NOT Zorgbedrijf Rivierenland 0680.439.360 / RL Rivierenland / Woonpunt Waas 1464 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg),"
        "Societe de logement Woonmaatschappij Rivierenland SRL (logement social residuel Mechelen-Willebroek),"
        "Woonmaatschappij Rivierenland leftover social-housing company of mined Mechelen + Willebroek (not Zorgbedrijf Rivierenland / RL Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg),"
        "other,city_mechelen,nl,https://wmwoonland.be/,info@wmwoonland.be,Lijsterstraat 6 2800 Mechelen,"
        "tick1465 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0403.698.162 Actief since 01.01.1968; live JR2025 official NBB WVV PDF; sourced euros assets 523681710 omzet 29125693 diensten 9454816 pers 5435789 63.8 VTE pnl -591785 equity 64764590 cash 27666290 debt 453954887 capex 30517061 dividend 0; FOI ready omzet 29.13m / pers 5.44m 63.8 VTE DROP vs 94.3 / debt 453.95m / cash JUMP 27.67m / PnL DROP -0.59m / 2 VE; distinct from already-mined Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / Zorgbedrijf Rivierenland / RL Rivierenland"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_wriv")

def part_budgets():
    BUDGETS = [
        ("bud_wriv_assets_2025", "2025", "523681710", "2025 assets 523681710 (was 508395351); tick1465; primary official NBB WVV VOL-inb 2026-00137594"),
        ("bud_wriv_current_2025", "2025", "55223232", "2025 vlottend 55223232 (was 54909144); tick1465; primary official NBB WVV"),
        ("bud_wriv_cash_2025", "2025", "27666290", "2025 liquide middelen 27666290 JUMP (was 23794658); tick1465; primary official NBB WVV"),
        ("bud_wriv_geldbeleg_2025", "2025", "0", "2025 geldbeleggingen empty; tick1465; primary official NBB WVV"),
        ("bud_wriv_strecv_2025", "2025", "8562849", "2025 ST vorderingen 8562849 (was 7080367); tick1465; primary official NBB WVV"),
        ("bud_wriv_trade_2025", "2025", "413239", "2025 handelsvorderingen 413239 (was 536298); tick1465; primary official NBB WVV"),
        ("bud_wriv_othrecv_2025", "2025", "8149609", "2025 overige ST vorderingen 8149609 (was 6544069); tick1465; primary official NBB WVV"),
        ("bud_wriv_voorraden_2025", "2025", "16220849", "2025 voorraden 16220849 DROP (was 21606830; onroerend verkoop 16000185); tick1465; primary official NBB WVV"),
        ("bud_wriv_prepaid_2025", "2025", "2773244", "2025 overlopend actief 2773244 (was 2427290; FS3 2717376); tick1465; primary official NBB WVV"),
        ("bud_wriv_fixed_2025", "2025", "468458479", "2025 vaste activa 468458479 (was 453486207); tick1465; primary official NBB WVV"),
        ("bud_wriv_iva_2025", "2025", "54274", "2025 IVA 54274 (was 88445); tick1465; primary official NBB WVV"),
        ("bud_wriv_mva_2025", "2025", "468392634", "2025 MVA 468392634 (was 453386191; terreinen/gebouwen 449045846 in aanbouw 19242270); tick1465; primary official NBB WVV"),
        ("bud_wriv_fva_2025", "2025", "11571", "2025 FVA 11571 (aandelen 1000 + borg 10571); tick1465; primary official NBB WVV"),
        ("bud_wriv_equity_2025", "2025", "64764590", "2025 eigen vermogen 64764590 (was 56925590); tick1465; primary official NBB WVV"),
        ("bud_wriv_inbreng_2025", "2025", "84344", "2025 inbreng 84344 onbeschikbaar; tick1465; primary official NBB WVV"),
        ("bud_wriv_reserves_2025", "2025", "26803031", "2025 reserves 26803031 (was 27394816); tick1465; primary official NBB WVV"),
        ("bud_wriv_kapsubs_2025", "2025", "33772290", "2025 kapitaalsubsidies 33772290 JUMP (was 25425850); tick1465; primary official NBB WVV"),
        ("bud_wriv_voorz_2025", "2025", "4962234", "2025 voorzieningen+uitgestelde belasting 4962234 (was 4595592); tick1465; primary official NBB WVV"),
        ("bud_wriv_debt_2025", "2025", "453954887", "2025 schulden 453954887 (was 446789819); tick1465; primary official NBB WVV"),
        ("bud_wriv_ltdebt_2025", "2025", "426543908", "2025 LT schulden 426543908 (was 417058834; fin krediet 422715442); tick1465; primary official NBB WVV"),
        ("bud_wriv_stdebt_2025", "2025", "24323575", "2025 ST schulden 24323575 (was 26355983); tick1465; primary official NBB WVV"),
        ("bud_wriv_lev_2025", "2025", "5008298", "2025 leveranciers 5008298 DROP (was 9378501); tick1465; primary official NBB WVV"),
        ("bud_wriv_bezold_2025", "2025", "504240", "2025 bezoldigingen-schulden 504240 (was 479248); tick1465; primary official NBB WVV"),
        ("bud_wriv_taxpay_2025", "2025", "2869479", "2025 belastingschulden 2869479 (was 2335274); tick1465; primary official NBB WVV"),
        ("bud_wriv_deferred_2025", "2025", "3087405", "2025 overlopend passief 3087405 (was 3375002); tick1465; primary official NBB WVV"),
        ("bud_wriv_omzet_2025", "2025", "29125693", "2025 omzet 70 29125693 (was 28151265; huur 27375806 koop 1749887); tick1465; primary official NBB WVV"),
        ("bud_wriv_diensten_2025", "2025", "9454816", "2025 diensten 61 9454816 (was 8665842); tick1465; primary official NBB WVV"),
        ("bud_wriv_aankopen_2025", "2025", "7839160", "2025 handelsgoederen/grondstoffen 60 7839160 (was 2877241); tick1465; primary official NBB WVV"),
        ("bud_wriv_pers_2025", "2025", "5435789", "2025 pers 62 5435789 (was 5460096); 63.8 VTE DROP vs 94.3; 98186 uur; YE 72; tick1465; primary official NBB WVV"),
        ("bud_wriv_afschr_2025", "2025", "14135283", "2025 afschrijvingen 14135283 (was 13085487); tick1465; primary official NBB WVV"),
        ("bud_wriv_expl_2025", "2025", "482724", "2025 bedrijfswinst 482724 DROP (was 1243168); tick1465; primary official NBB WVV"),
        ("bud_wriv_finopbr_2025", "2025", "7261156", "2025 financiele opbrengsten 7261156 all recurrent; tick1465; primary official NBB WVV"),
        ("bud_wriv_finkost_2025", "2025", "8372086", "2025 financiele kosten 8372086 (was 7431385); tick1465; primary official NBB WVV"),
        ("bud_wriv_pnl_2025", "2025", "-591785", "2025 PnL -591785 DROP (was +377796); tick1465; primary official NBB WVV"),
        ("bud_wriv_div_2025", "2025", "0", "2025 dividend 0 uit te keren empty; tick1465; primary official NBB WVV"),
        ("bud_wriv_capex_2025", "2025", "30517061", "2025 capex MVA aanschaf 30517061 (terreinen 2216557 + meubilair 4294 + in aanbouw 28296210); tick1465; primary official NBB WVV"),
        ("bud_wriv_bedrijfsopbr_2025", "2025", "42646784", "2025 bedrijfsopbrengsten 70/76A 42646784 (was 34964630); tick1465; primary official NBB WVV"),
        ("bud_wriv_bedrijfskost_2025", "2025", "42164059", "2025 bedrijfskosten 60/66A 42164059 (was 33721462); tick1465; primary official NBB WVV"),
        ("bud_wriv_tax_2025", "2025", "10361", "2025 belastingen 67/77 10361 (was 122133); tick1465; primary official NBB WVV"),
        ("bud_wriv_in_aanbouw_2025", "2025", "19242270", "2025 activa in aanbouw 19242270 DROP (was 60945922); tick1465; primary official NBB WVV"),
        ("bud_wriv_krediet_2025", "2025", "422715442", "2025 LT kredietinstellingen 422715442 (was 413442617); tick1465; primary official NBB WVV"),
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
        f"{COMM},Woonmaatschappij Rivierenland JR2025 leftover woonmaatschappij dual (omzet 29.13m / diensten 9.45m / pers 5.44m 63.8 VTE DROP vs 94.3 / debt 453.95m / cash JUMP 27.67m / PnL DROP -0.59m / 2 VE),{ENT},Woonmaatschappij Rivierenland / mined Mechelen+Willebroek dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-27,1968,,29125693,,,active,{PDF},Local leftover woonmaatschappij map VL Mechelen-Willebroek — omzet 29.13m / pers 5.44m 63.8 VTE DROP / debt 453.95m / cash JUMP 27.67m,Publish omzet split + 2 VE payroll + VTE DROP 94.3 to 63.8 + LT krediet 422.7m counterparties + capex 30.52m + aandeel % Mechelen/Willebroek/OCMW/private; do not keep leftover woonmaatschappij as unpublished 29.13m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Mechelen>Woonmaatschappij>Rivierenland>JR2025_L5,tick1465; assets 523681710 omzet 29125693 diensten 9454816 pers 5435789 pnl -591785 equity 64764590 cash 27666290 debt 453954887 capex 30517061 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT Zorgbedrijf Rivierenland / RL Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Woonmaatschappij Rivierenland JR2025 leftover woonmaatschappij: omzet 29.13m / diensten 9.45m / pers 5.44m 63.8 VTE DROP vs 94.3 / debt 453.95m / cash JUMP 27.67m / PnL DROP -0.59m / 2 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Mechelen>Woonmaatschappij>Rivierenland>JR2025_L5,29125693,523681710,Leftover dual woonmaatschappij shell: assets 523.68m / equity 64.76m / omzet 29.13m / diensten 9.45m / pers 5.44m 63.8 VTE DROP vs 94.3 / cash 27.67m JUMP / debt 453.95m / LT krediet 422.7m / PnL -0.59m DROP / 2 VE; do not treat 29.13m as TE-additive of 348bn,strong,{SRC},Woonmaatschappij Rivierenland / mined Mechelen+Willebroek dual housing,Local leftover woonmaatschappij map VL Mechelen-Willebroek — JR2025 official NBB WVV live; omzet+pers+debt+cash+VTE FOI,Official NBB WVV 2026-08-19: omzet 29.13m / pers 5.44m 63.8 VTE DROP / debt 453.95m / cash JUMP 27.67m / PnL -0.59m / 2 VE,7.0,7.6,3.0,7.1,Publish omzet split + 2 VE payroll + VTE DROP 94.3 to 63.8 + LT krediet 422.7m counterparties + capex 30.52m + aandeel % Mechelen/Willebroek/OCMW/private; do not keep leftover woonmaatschappij as unpublished 29.13m housing shell,active,,tick1465; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / Zorgbedrijf Rivierenland / RL Rivierenland",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Gemeenten>Mechelen>Woonmaatschappij>Rivierenland>JR2025_L5,{ENT},omzet 29125693 vs 28151265 + diensten 9454816 + pers 5435789 63.8 VTE DROP vs 94.3 + 2 VE 2230711572/2348316847 + cash 27666290 JUMP vs 23794658 + debt 453954887 LT krediet 422715442 + voorraden DROP 16220849 vs 21606830 + capex 30517061 in aanbouw DROP 19242270 vs 60945922 + PnL DROP -591785 vs +377796 + kapsubs JUMP 33772290 vs 25425850 + commissaris 18150 + aandeel % Mechelen/Willebroek/OCMW/private unpublished,Leftover woonmaatschappij Mechelen-Willebroek after leftover AGB/APB hunt: omzet 29.13m / pers 5.44m 63.8 VTE DROP vs 94.3 / debt 453.95m / cash JUMP 27.67m / PnL DROP -0.59m / 2 VE hides municipal housing vehicle,8,Woonmaatschappij Rivierenland / Bestuursorgaan / algemeen directeur,info@wmwoonland.be,Lijsterstraat 6 2800 Mechelen,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1465 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF now extracted (5523641 bytes 66p). FOI ready not sent. NOT every-10. NOT Woonpunt Waas / Toerisme Limburg / Toerisme Vlaams-Brabant / Toerisme Oost-Vlaanderen / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / Zorgbedrijf Rivierenland / RL Rivierenland / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1464. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still no separate APB 2025 PDF.",
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
    if not last_s.startswith("rq_1465,"):
        raise SystemExit(f"expected last row rq_1465, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1465 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1465,Woonmaatschappij Rivierenland JR2025 leftover dual residual,hole_fill,5,done,L5,wm_wriv,"
        "Completed: Woonmaatschappij Rivierenland leftover woonmaatschappij of mined Mechelen + Willebroek after leftover AGB/APB hunt; KBO 0403.698.162 Actief; live JR2025 official NBB WVV VOL-inb PDF (5523641 bytes 66p; deposit 2026-00137594; AV 27.05.2026; header 02.06.2026; pdfinfo 04.06.2026 21:45:27 UTC). PDF header Woonmaatschappij Rivierenland / Lijsterstraat 6 — NOT Zorgbedrijf Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Sourced euros assets 523681710 omzet 29125693 diensten 9454816 pers 5435789 63.8 VTE pnl -591785 equity 64764590 cash 27666290 debt 453954887 capex 30517061 dividend 0. FOI "
        f"{GAP} ready not sent. Distinct from already-mined Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / Zorgbedrijf Rivierenland / RL Rivierenland.,"
        f"{GAP},2026-08-19T15:42:00Z,{TS},"
        "tick1465 Woonmaatschappij Rivierenland leftover woonmaatschappij residual; KBO 0403.698.162; live JR2025 official NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1466 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij (Dimensa 0400.067.887 deposit 2026-00138353 live) if JR2025"
    )
    spawn = (
        "rq_1466,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1465 done including Woonmaatschappij Rivierenland 1465 leftover woonmaatschappij live official NBB WVV / Woonpunt Waas 1464 leftover woonmaatschappij live official NBB WVV / Toerisme Limburg 1463 leftover provincial tourism VZW live official NBB WVV / Toerisme Vlaams-Brabant 1462 leftover provincial tourism VZW live official NBB WVV / Toerisme Oost-Vlaanderen 1461 leftover provincial tourism VZW live official NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 404 as of 1465). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck spotted unmined around 1453 — still no separate APB 2025 PDF as of 1465). Do NOT confuse with already-mined Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / Zorgbedrijf Rivierenland. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live. Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1465 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1465. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Dimensa 0400.067.887 deposit 2026-00138353 live 15MB as of 1465). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461.,,"
        f"{TS},{TS},"
        "spawned tick1465 after Woonmaatschappij Rivierenland leftover woonmaatschappij live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij (Dimensa) if JR2025"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1465=done + rq_1466 spawned; keep", last_line_start)

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
    Path("/tmp/tick1465_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1465 Woonmaatschappij Rivierenland leftover woonmaatschappij residual; KBO 0403.698.162; live JR2025 official NBB WVV PDF; sourced euros assets 523681710 omzet 29125693 diensten 9454816 pers 5435789 63.8 VTE pnl -591785 equity 64764590 cash 27666290 debt 453954887 capex 30517061 dividend 0; FOI ready omzet 29.13m / pers 5.44m 63.8 VTE DROP vs 94.3 / debt 453.95m / cash JUMP 27.67m / PnL DROP -0.59m / 2 VE; NOT Woonpunt Waas / Toerisme Limburg / Toerisme Vlaams-Brabant / Toerisme Oost-Vlaanderen / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / Zorgbedrijf Rivierenland / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1466 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij (Dimensa) if JR2025; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1465,1465,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1465")

    entry = (
        "\n## Tick 1465 - 2026-08-19 - rq_1465 Woonmaatschappij Rivierenland dual residual leftover\n"
        "- Unit: Woonmaatschappij Rivierenland BV / Woonland (leftover woonmaatschappij / social-housing BV of mined Mechelen + Willebroek; 2 VE 2.230.711.572 + 2.348.316.847) after residual dual hunt (KBO **0403.698.162**; official NBB WVV VOL-inb PDF **5523641** bytes / 66p; deposit **2026-00137594**; AV **27.05.2026**; header **02.06.2026**; pdfinfo created **04.06.2026 21:45:27 UTC**; model **VOL-inb** 26.0.12 m82-f; commissaris Luc Callaert BV B00342 / 0463.716.022 / Callaert Luc N01123 mandate 21.05.2024–26.05.2027 fee **18150** incl. 21% BTW; VOL-inb 6.1/6.2.2/6.2.4/6.2.5/6.3.4/6.3.5/6.4.1/6.4.2/6.5.1/6.5.2/6.7.2/6.15/6.18.2/6.20/9/12/13/14/15 not filed; 6.2.1/6.2.3 IVA + 6.3 MVA + 6.4.3 FVA + 6.6 + 6.7.1 + 6.8 + 6.9 + 6.10 + 6.11 + 6.12 + 6.13 + 6.14 + 6.16 + 6.17 + 6.18.1 + 6.19 + sociale balans + remuneratieverslag + commissarisverslag filed). Leftover AGB/APB first: leftover APB Inovant / Atlas koepelsite `jaarrekening_25_inov` / `jaarrekening_25_atlas` HEAD **404** on 2026-05-28 and 2026-06-25 with Googlebot UA this tick (Foleon leftover slugs have redirected to Hooibeekhoeve — no fetchable 2025 Inovant/Atlas PDF). Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick. Leftover AGB Herzele already in entities (tick1163) — skipped. Leftover AGB Bornem 0877.556.624 last JR still 2024. Leftover AGB Hasselt / SOLag / WAGSO / Temse / Herk / Lommel / Puurs already in entities — skipped. Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel still no JR as of 1464. Leftover IGS IVAREM 0267.403.264 last JR still 2024-12-31. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover Woonmaatschappij Rivierenland statutory CDN `2026-00137594` live this tick (HTTP 200 / 5523641 / 66p; jaar **2025-12-31**; neerlegging **04.06.2026**) — taken (hunt order #2 leftover unmined woonmaatschappij of mined Mechelen + Willebroek with live 2025 statutory PDF after leftover AGB/APB hunt). PDF header **Woonmaatschappij Rivierenland / Lijsterstraat 6 / 2800 Mechelen** — NOT Zorgbedrijf Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Distinct from already-mined **Woonpunt Waas 1464** / **Toerisme Limburg 1463** / **Toerisme Vlaams-Brabant 1462** / **Toerisme Oost-Vlaanderen 1461** / **Arboretum Kalmthout 1460** / **Kempens Landschap 1459** / **APB Warande 1458** / **APB De Schorre 1457** / **APB PIH 1456** / **Zorgbedrijf Rivierenland** / **RL Rivierenland**. First confirmed not already extracted as JR2025 euros: no Woonmaatschappij Rivierenland / 0403.698.162 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **01.01.1968**; statutaire naam Woonmaatschappij Rivierenland since 21.06.2023; BV since 21.06.2023; zetel Lijsterstraat 6 2800 Mechelen since 21.06.2023; **2 VE**; 16 functiehouders; dagelijks bestuur Dierckx Yvette since 21.06.2023; Werkgever RSZ since 01.07.1953; btw since 01.01.2004; aanbestedende overheid; NACE 68.203 / 68.121 / 68.202; site https://wmwoonland.be/; absorbeerde Woonpunt Mechelen 0403.607.397 since 21.06.2023. Prior-year figures **identiek**. SBM HTML used for deposit-id discovery only (SBM table 1-euro-off vs PDF). Euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1470).\n"
        "- EUR strong (primary official WVV VOL-inb; omzet 70 **29125693**; diensten 61 **9454816**; pers 62 **5435789** / **63,8 VTE** vs 5460096 / 94,3): assets **523681710** (was 508395351); fixed **468458479** vs 453486207 / IVA **54274** vs 88445 / MVA **468392634** vs 453386191 (terreinen/gebouwen **449045846**; installaties **9005**; meubilair **95513**; in aanbouw **19242270 DROP** vs 60945922) / FVA **11571**; current **55223232** vs 54909144; voorraden **16220849 DROP** vs 21606830 (onroerend verkoop **16000185**); ST recv **8562849** vs 7080367 (trade **413239** / other **8149609**); geldbeleg empty; cash **27666290 JUMP** vs 23794658; prepaid **2773244**; equity **64764590** vs 56925590 (inbreng **84344**; herw **4104924**; reserves **26803031**; overgedragen empty; kapsubs **33772290 JUMP** vs 25425850); voorzieningen **4962234** vs 4595592 (grote herstellingen **1401396**; hangende geschillen **1415000**; uitgestelde belasting **2066450**); schulden **453954887** vs 446789819 (LT **426543908** vs 417058834 waarvan fin krediet **422715442**; ST **24323575** vs 26355983 waarvan 42 **15193640** + leveranciers **5008298 DROP** vs 9378501 + tax **2869479** + bezold **504240**; deferred **3087405**); omzet **29125693** vs 28151265 (huur **27375806** / koop **1749887**); 60 **7839160**; diensten **9454816** vs 8665842; pers **5435789** / **63,8 VTE DROP** vs 94,3 / 98186 uur / YE **72** / YE VTE **62,2**; afschr **14135283**; expl **+482724 DROP** vs +1243168; fin opbr **7261156**; fin kosten **8372086**; tax **10361**; PnL **-591785 DROP** vs +377796; dividend **0**; onttrekking reserves **373107**; capex MVA aanschaf **30517061** (terreinen 2216557 + meubilair 4294 + in aanbouw 28296210) + IVA 10285. Commissaris fee **18150**. 2 VE. Cross-checks: 468458479+55223232=523681711 vs 523681710; 64764590+4962234+453954887=523681711 vs 523681710; 42646784-42164059=482725 vs 482724; 482724+7261156-8372086=-628206 vs -628205; -628205+46781-10361=-591785; -591785+218678=-373107. 1-euro rounding on assets/PnL.\n"
        "- CSVs: sources +4; entities +1 `wm_wriv` parent `city_mechelen`; budgets +41 executed; commitments +1 envelope 29125693 AV 27.05.2026; leaderboard +1 annual 29125693 / total 523681710; foi_queue +1 status=ready never sent; research_queue surgical rq_1465=done + rq_1466 spawn; loop_state ticks_completed=1465. Inventory after write: budgets {INV_B} · commitments {INV_C} · leaderboard {INV_L} · entities {INV_E} · sources {INV_S} · FOI ready {FOI_R} / answered {FOI_A} / partial {FOI_P} / total {FOI_T}.\n"
        "- FOI: `gap_wriv_omzet_29_13m_pers_5_44m_debt_454m_l5` ready not sent — omzet 29.13m / diensten 9.45m / pers 5.44m 63.8 VTE DROP vs 94.3 / 2 VE / cash JUMP 27.67m / debt 453.95m LT krediet 422.7m / voorraden DROP 16.22m / capex 30.52m / PnL DROP -0.59m / kapsubs JUMP 33.77m / commissaris 18.15k / aandeel % Mechelen/Willebroek/OCMW/private unpublished.\n"
        "- Next: rq_1466 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 404 this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1465). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live. Leftover IGS IVAREM **0267.403.264** still JR2024. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Dimensa 0400.067.887 deposit **2026-00138353** live 15MB this tick — take next if still unmined). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Stichting Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456. Next every-10 is **1470**. Provincial tourism VZWs now exhausted (Westtoer + TOV + TVLB + TLim).\n"
    )
    entry = entry.replace("{INV_B}", str(inv["budgets.csv"])).replace("{INV_C}", str(inv["commitments.csv"])).replace("{INV_L}", str(inv["leaderboard.csv"])).replace("{INV_E}", str(inv["entities.csv"])).replace("{INV_S}", str(inv["sources.csv"])).replace("{FOI_R}", str(foi_ready)).replace("{FOI_A}", str(foi_ans)).replace("{FOI_P}", str(foi_part)).replace("{FOI_T}", str(foi_tot))
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1465 -" in lraw:
        raise SystemExit("loop_log already has tick 1465 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1465")
    print("DONE tick 1465")

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

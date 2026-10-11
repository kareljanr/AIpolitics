#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1463 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T15:28:00Z"
ENT = "vzw_tlim"
SRC = "src_tlim_jr2025_nbb"
GAP = "gap_tlim_omzet_empty_bruto_3_66m_pers_2_79m_l5"
LB = "lb_tlim_omzet_empty_bruto_3_66m_pers_2_79m"
COMM = "comm_tlim_jr2025_bruto"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00229240.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Toerisme Limburg vzw official NBB WVV VKT-VZW JR2025,{PDF},NBB / Toerisme Limburg vzw,2026-08-19,budget,tick1463; official NBB WVV VKT-VZW JR2025 PDF 27p / 450763 bytes; deposit 2026-00229240; AV 22.06.2026; header 23.06.2026; pdfinfo created 01.07.2026 01:38:20 UTC; model VKT-VZW 23.0.10 m04-f; KBO 0420.092.944; assets 4361033 cash 3172365 debt 2739144 pers 2792619 omzet empty diensten empty pnl 519317 equity 1621889",
        "src_tlim_site,Toerisme Limburg vzw / Visit Limburg official sector + provincie tourism pages,https://visitlimburg.be/,Provincie Limburg / TL vzw,2026-08-19,official_register,tick1463; leftover provincial tourism VZW/EVA of mined provincie Limburg; zetel Universiteitslaan 3 3500 Hasselt; KBO 0420.092.944; SBM HTTP bedrijfsfiche for deposit id; provincie page https://www.limburg.be/toerisme-limburg-vzw",
        "src_kbo_tlim_0420092944,KBO Toerisme Limburg vzw 0420.092.944,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0420092944,KBO Public Search FOD Economie,2026-08-19,official_register,tick1463; Actief since 21.09.1979; VZW; naam Toerisme Limburg since 25.07.1996; afkorting P.V.T.L.; zetel Universiteitslaan 3 3500 Hasselt; 1 VE 2154332782 Toerisme Limburg; 15 functiehouders; Werkgever RSZ since 21.09.1979",
        "src_tlim_foi_contact,Toerisme Limburg FOI channel (info@limburg.be / provincie contactformulier),https://www.limburg.be/toerisme-limburg-vzw,TL vzw / Provincie Limburg,2026-08-19,official_register,tick1463; leftover provincial tourism VZW; NOT Westtoer / Toerisme Oost-Vlaanderen / Toerisme Vlaams-Brabant / leftover APB Inovant / Atlas / leftover APB Puyenbroeck / leftover Bosgroep Limburg / CoLimBo / leftover Dommelhof",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nvzw_tlim," in raw or raw.startswith(b"vzw_tlim,"):
        raise SystemExit("vzw_tlim already present")
    if b"0420.092.944" in raw:
        raise SystemExit("Toerisme Limburg KBO already present as entity")
    row = (
        "vzw_tlim,Toerisme Limburg vzw / Visit Limburg (leftover provincial tourism VZW/EVA of mined provincie Limburg; NOT Westtoer / Toerisme Oost-Vlaanderen / Toerisme Vlaams-Brabant / leftover APB Inovant / Atlas / leftover APB Puyenbroeck / leftover Bosgroep Limburg / CoLimBo / leftover Dommelhof),"
        "Tourisme Limbourg ASBL (EVA provincial residuel tourisme / Visit Limburg),"
        "Toerisme Limburg leftover provincial tourism VZW/EVA of mined province of Limburg (not Westtoer / Toerisme Oost-Vlaanderen / Toerisme Vlaams-Brabant / leftover APB Inovant / Atlas / leftover APB Puyenbroeck / leftover Bosgroep Limburg / CoLimBo / leftover Dommelhof),"
        "eva,prov_limburg,nl,https://visitlimburg.be/,info@limburg.be,Universiteitslaan 3 3500 Hasselt,"
        "tick1463 leftover residual tourism VZW/EVA after leftover AGB/APB hunt; KBO 0420.092.944 Actief since 21.09.1979; live JR2025 official NBB WVV PDF; sourced euros assets 4361033 omzet empty diensten empty pers 2792619 30.4 VTE pnl 519317 equity 1621889 cash 3172365 debt 2739144 capex 6062 dividend 0; FOI ready empty 70 / empty 73 / empty 60-61 / pers 2.79m 30.4 VTE / cash JUMP 3.17m / geldbeleg DROP 1.76m / vooruitbet 1.53m / 1 VE; distinct from already-mined Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / Westtoer / Vlabinvest"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 vzw_tlim")

def part_budgets():
    BUDGETS = [
        ("bud_tlim_assets_2025", "2025", "4361033", "2025 assets 4361033 (was 4323651); tick1463; primary official NBB WVV VKT-VZW 2026-00229240"),
        ("bud_tlim_current_2025", "2025", "4354661", "2025 vlottend 4354661 (was 4317551); tick1463; primary official NBB WVV"),
        ("bud_tlim_cash_2025", "2025", "3172365", "2025 liquide middelen 3172365 JUMP (was 1182333); tick1463; primary official NBB WVV"),
        ("bud_tlim_geldbeleg_2025", "2025", "0", "2025 geldbeleggingen 0 DROP (was 1759446); tick1463; primary official NBB WVV"),
        ("bud_tlim_strecv_2025", "2025", "317073", "2025 ST vorderingen 317073 (was 325900); tick1463; primary official NBB WVV"),
        ("bud_tlim_trade_2025", "2025", "113850", "2025 handelsvorderingen 113850 (was 157915); tick1463; primary official NBB WVV"),
        ("bud_tlim_othrecv_2025", "2025", "203223", "2025 overige ST vorderingen 203223 (was 167985); tick1463; primary official NBB WVV"),
        ("bud_tlim_voorraden_2025", "2025", "841698", "2025 voorraden/bestellingen 841698 DROP (was 942122; all bestellingen in uitvoering); tick1463; primary official NBB WVV"),
        ("bud_tlim_prepaid_2025", "2025", "23526", "2025 overlopend actief 23526 (was 32750); tick1463; primary official NBB WVV"),
        ("bud_tlim_ltrecv_2025", "2025", "0", "2025 LT vorderingen 0 DROP (was 74999); tick1463; primary official NBB WVV"),
        ("bud_tlim_fixed_2025", "2025", "6372", "2025 vaste activa 6372 (was 6100); tick1463; primary official NBB WVV"),
        ("bud_tlim_iva_2025", "2025", "0", "2025 IVA net 0 (aanschaf 185319 fully depreciated); tick1463; primary official NBB WVV"),
        ("bud_tlim_mva_2025", "2025", "6372", "2025 MVA net 6372 all meubilair (aanschaf 215178 afschr 208806); tick1463; primary official NBB WVV"),
        ("bud_tlim_fva_2025", "2025", "0", "2025 FVA empty; 6.1.3 not filed; tick1463; primary official NBB WVV"),
        ("bud_tlim_equity_2025", "2025", "1621889", "2025 eigen vermogen 1621889 JUMP (was 1102572); tick1463; primary official NBB WVV"),
        ("bud_tlim_fondsen_2025", "2025", "0", "2025 fondsen beginvermogen empty; tick1463; primary official NBB WVV"),
        ("bud_tlim_bestemde_2025", "2025", "226172", "2025 bestemde fondsen 226172 DROP (was 292171); tick1463; primary official NBB WVV"),
        ("bud_tlim_overgedragen_2025", "2025", "1395717", "2025 overgedragen winst 1395717 JUMP (was 810401); tick1463; primary official NBB WVV"),
        ("bud_tlim_voorz_2025", "2025", "0", "2025 voorzieningen empty; tick1463; primary official NBB WVV"),
        ("bud_tlim_debt_2025", "2025", "2739144", "2025 schulden 2739144 DROP (was 3221079; LT empty); tick1463; primary official NBB WVV"),
        ("bud_tlim_stdebt_2025", "2025", "2682924", "2025 ST schulden 2682924 (was 3055362); tick1463; primary official NBB WVV"),
        ("bud_tlim_lev_2025", "2025", "623855", "2025 leveranciers 623855 DROP (was 717490); tick1463; primary official NBB WVV"),
        ("bud_tlim_vooruit_2025", "2025", "1534306", "2025 vooruitbetalingen 1534306 DROP (was 1803096); tick1463; primary official NBB WVV"),
        ("bud_tlim_bezold_2025", "2025", "366946", "2025 bezoldigingen-schulden 366946 (was 400678); tick1463; primary official NBB WVV"),
        ("bud_tlim_taxpay_2025", "2025", "135493", "2025 belastingschulden 135493 (was 90965); tick1463; primary official NBB WVV"),
        ("bud_tlim_deferred_2025", "2025", "56220", "2025 overlopend passief 56220 DROP (was 165717); tick1463; primary official NBB WVV"),
        ("bud_tlim_bruto_2025", "2025", "3660709", "2025 brutomarge 3660709 JUMP (was 1353683); tick1463; primary official NBB WVV"),
        ("bud_tlim_omzet_2025", "2025", "0", "2025 omzet 70 empty unpublished; tick1463; primary official NBB WVV"),
        ("bud_tlim_lidgeld_2025", "2025", "0", "2025 lidgeld/subsidies 73 empty unpublished; tick1463; primary official NBB WVV"),
        ("bud_tlim_diensten_2025", "2025", "0", "2025 60/61 empty unpublished so diensten unpublished as a split; tick1463; primary official NBB WVV"),
        ("bud_tlim_pers_2025", "2025", "2792619", "2025 pers 62 2792619 (was 2966696); 30.4 VTE vs 32.6; 42457 uur; YE 30.9; tick1463; primary official NBB WVV"),
        ("bud_tlim_afschr_2025", "2025", "5790", "2025 afschrijvingen 5790 (was 12159); tick1463; primary official NBB WVV"),
        ("bud_tlim_andere_2025", "2025", "204689", "2025 andere bedrijfskosten 204689 (was 199705); tick1463; primary official NBB WVV"),
        ("bud_tlim_expl_2025", "2025", "655636", "2025 bedrijfswinst 655636 JUMP (was -1825243); tick1463; primary official NBB WVV"),
        ("bud_tlim_finopbr_2025", "2025", "2642", "2025 financiele opbrengsten 2642 all recurrent; tick1463; primary official NBB WVV"),
        ("bud_tlim_finkost_2025", "2025", "138961", "2025 financiele kosten 138961 JUMP (was 21737); tick1463; primary official NBB WVV"),
        ("bud_tlim_pnl_2025", "2025", "519317", "2025 PnL 519317 JUMP (was -1851957); tick1463; primary official NBB WVV"),
        ("bud_tlim_div_2025", "2025", "0", "2025 dividend 0 VZW; tick1463; primary official NBB WVV"),
        ("bud_tlim_capex_2025", "2025", "6062", "2025 capex MVA aanschaf 6062; tick1463; primary official NBB WVV"),
        ("bud_tlim_commissaris_2025", "2025", "7300", "2025 commissaris fee 7300 CARLO DEWITTE BEDRIJFSREVISOR BV; tick1463; primary official NBB WVV"),
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
        f"{COMM},Toerisme Limburg vzw JR2025 leftover provincial tourism dual (empty 70/73/60-61 / bruto 3.66m / pers 2.79m 30.4 VTE / cash JUMP 3.17m / geldbeleg DROP 1.76m / vooruitbet 1.53m / 1 VE),{ENT},TL vzw / provincie Limburg dual tourism,WVV VZW; Provinciedecreet; Bestuursdecreet openbaarheid,2026-06-22,1979,,3660709,,,active,{PDF},Local leftover tourism VZW map VL Limburg — empty 70/73/60-61 / bruto 3.66m / pers 2.79m 30.4 VTE / cash JUMP 3.17m,Publish omzet+73+60/61 split + 1 VE payroll + cash 3.17m counterparties + geldbeleg DROP + vooruitbet 1.53m + provincie subsidy share; do not keep leftover tourism VZW as unpublished 3.66m tourism shell,{SRC},strong,Vlaanderen>Provincies>Limburg>EVA>ToerismeLimburg>JR2025_L5,tick1463; assets 4361033 omzet empty diensten empty pers 2792619 pnl 519317 equity 1621889 cash 3172365 debt 2739144 capex 6062 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT Westtoer / Toerisme Oost-Vlaanderen / Toerisme Vlaams-Brabant / leftover APB Inovant / Atlas / leftover APB Puyenbroeck / leftover Bosgroep Limburg / CoLimBo / leftover Dommelhof",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Toerisme Limburg vzw JR2025 leftover provincial tourism: empty 70/73/60-61 / bruto 3.66m / pers 2.79m 30.4 VTE / cash JUMP 3.17m / geldbeleg DROP 1.76m / vooruitbet 1.53m / 1 VE,L5,local_budget_line,Vlaanderen>Provincies>Limburg>EVA>ToerismeLimburg>JR2025_L5,2792619,4361033,Leftover dual tourism VZW shell: assets 4.36m / equity 1.62m / bruto 3.66m JUMP / omzet empty / 73 empty / 60-61 empty / pers 2.79m 30.4 VTE / cash 3.17m JUMP / geldbeleg DROP 1.76m / vooruitbet 1.53m / debt 2.74m / PnL +0.52m JUMP / 1 VE; do not treat 3.66m as TE-additive of 348bn,strong,{SRC},TL vzw / provincie Limburg dual tourism,Local leftover tourism VZW map VL Limburg — JR2025 official NBB WVV live; empty 70/73/60-61 + pers/cash/vooruitbet FOI,Official NBB WVV 2026-08-19: bruto 3.66m / pers 2.79m 30.4 VTE / cash JUMP 3.17m / PnL +0.52m / 1 VE / omzet empty,6.5,5.5,3.0,6.2,Publish omzet+73+60/61 split + 1 VE payroll + cash 3.17m counterparties + geldbeleg DROP + vooruitbet 1.53m + provincie subsidy share; do not keep leftover tourism VZW as unpublished 3.66m tourism shell,active,,tick1463; leftover tourism VZW/EVA after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / Westtoer / Vlabinvest",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Provincies>Limburg>EVA>ToerismeLimburg>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto 3660709 vs 1353683 + pers 2792619 30.4 VTE + 1 VE 2154332782 + cash 3172365 JUMP vs 1182333 + geldbeleg 0 DROP vs 1759446 + vooruitbetalingen 1534306 vs 1803096 + fin kosten 138961 JUMP vs 21737 + equity JUMP 1621889 vs 1102572 + PnL JUMP 519317 vs -1851957 + MVA 6372 / capex 6062 + commissaris 7300 + provincie subsidy share unpublished,Leftover tourism VZW Limburg after leftover AGB/APB hunt: empty 70/73/60-61 / bruto 3.66m / pers 2.79m 30.4 VTE / cash JUMP 3.17m / geldbeleg DROP 1.76m / vooruitbet 1.53m / 1 VE hides provincial tourism vehicle,8,Toerisme Limburg vzw / provinciegriffier / Bestuursorgaan,info@limburg.be,Universiteitslaan 3 3500 Hasselt,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1463 leftover tourism VZW/EVA after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF now extracted (450763 bytes 27p). FOI ready not sent. NOT every-10. NOT Toerisme Vlaams-Brabant / Toerisme Oost-Vlaanderen / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / TPA / POA / Westtoer / Vlabinvest / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep IJzer en Leie 0816.706.346 still no JR. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening as of 1462. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. Puyenbroeck still no separate APB 2025 PDF.",
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
    if not last_s.startswith("rq_1463,"):
        raise SystemExit(f"expected last row rq_1463, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1463 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1463,Toerisme Limburg JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_tlim,"
        "Completed: Toerisme Limburg vzw leftover provincial tourism VZW/EVA of mined provincie Limburg after leftover AGB/APB hunt; KBO 0420.092.944 Actief; live JR2025 official NBB WVV VKT-VZW PDF (450763 bytes 27p; deposit 2026-00229240; AV 22.06.2026; header 23.06.2026; pdfinfo 01.07.2026 01:38:20 UTC). PDF header Toerisme Limburg / Universiteitslaan 3 — NOT Westtoer / Toerisme Oost-Vlaanderen / Toerisme Vlaams-Brabant / Hooibeekhoeve / Puyenbroeck. Sourced euros assets 4361033 omzet empty diensten empty pers 2792619 30.4 VTE pnl 519317 equity 1621889 cash 3172365 debt 2739144 capex 6062 dividend 0. FOI "
        f"{GAP} ready not sent. Distinct from already-mined Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / Westtoer / Vlabinvest.,"
        f"{GAP},2026-08-19T15:22:00Z,{TS},"
        "tick1463 Toerisme Limburg leftover tourism VZW residual; KBO 0420.092.944; live JR2025 official NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1464 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
    )
    spawn = (
        "rq_1464,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1463 done including Toerisme Limburg 1463 leftover provincial tourism VZW live official NBB WVV / Toerisme Vlaams-Brabant 1462 leftover provincial tourism VZW live official NBB WVV / Toerisme Oost-Vlaanderen 1461 leftover provincial tourism VZW live official NBB WVV / Arboretum Kalmthout 1460 leftover EVAP live official NBB WVV + every-10 / Stichting Kempens Landschap 1459 leftover IGS/SON live official NBB WVV / APB Warande 1458 leftover APB live official BBC / APB De Schorre 1457 leftover APB live official BBC / APB PIH 1456 leftover APB live official BBC / APB TPA 1455 leftover APB live official BBC / APB POA 1454 leftover APB live official BBC). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 404 as of 1463). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck spotted unmined around 1453 — still no separate APB 2025 PDF as of 1463). Do NOT confuse with already-mined Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live (IJzer en Leie still no JR as of 1463). Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1463 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1463. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456.,,"
        f"{TS},{TS},"
        "spawned tick1463 after Toerisme Limburg leftover tourism VZW live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1463=done + rq_1464 spawned; keep", last_line_start)

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
    Path("/tmp/tick1463_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1463 Toerisme Limburg leftover tourism VZW residual; KBO 0420.092.944; live JR2025 official NBB WVV PDF; sourced euros assets 4361033 omzet empty diensten empty pers 2792619 30.4 VTE pnl 519317 equity 1621889 cash 3172365 debt 2739144 capex 6062 dividend 0; FOI ready empty 70 / empty 73 / empty 60-61 / pers 2.79m 30.4 VTE / cash JUMP 3.17m / geldbeleg DROP 1.76m / vooruitbet 1.53m / 1 VE; NOT Toerisme Vlaams-Brabant / Toerisme Oost-Vlaanderen / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / TPA / POA / Westtoer / Vlabinvest / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1464 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1463,1463,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1463")

    entry = (
        "\n## Tick 1463 - 2026-08-19 - rq_1463 Toerisme Limburg dual residual leftover\n"
        "- Unit: Toerisme Limburg vzw / Visit Limburg (leftover provincial tourism VZW/EVA of mined provincie Limburg; 1 VE 2.154.332.782) after residual dual hunt (KBO **0420.092.944**; official NBB WVV VKT-VZW PDF **450763** bytes / 27p; deposit **2026-00229240**; AV **22.06.2026**; header **23.06.2026**; pdfinfo created **01.07.2026 01:38:20 UTC**; model **VKT-VZW** 23.0.10 m04-f; commissaris CARLO DEWITTE BEDRIJFSREVISOR BV B-00883 / 0565.941.451 / Dewitte Carlo A-02466 mandate 19.06.2025–19.06.2028 fee **7300**; VKT-VZW 6.1.3/6.3/7 not filed; 6.1.1 IVA + 6.1.2 MVA + 6.2 fondsen + 6.4 + 6.5 + 6.6 + 6.7 sociale balans + 6.8 waarderingsregels filed). Leftover AGB/APB first: leftover APB Inovant / Atlas koepelsite `jaarrekening_25_inov` / `jaarrekening_25_atlas` HEAD **404** on 2026-05-28 and 2026-06-25 with Googlebot UA this tick (Foleon leftover slugs have redirected to Hooibeekhoeve — no fetchable 2025 Inovant/Atlas PDF). Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick. Leftover AGB Bornem 0877.556.624 last JR still 2024 (2026pdf 2026-00553588 HEAD 403 this tick). Leftover AGB Hasselt / SOLag / WAGSO / Temse / Herk-de-Stad already in entities — skipped. Leftover Bosgroep IJzer en Leie 0816.706.346 still no jaarrekening (SBM jaarrekeninganalyse niet beschikbaar this tick). Leftover IGS IVAREM 0267.403.264 last JR still 2024-12-31 (neerlegging 2025-09-18). Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening as of 1462. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover Toerisme Limburg statutory CDN `2026-00229240` live this tick (HTTP 200 / 450763 / 27p; jaar **2025-12-31**; neerlegging **01.07.2026**) — taken (hunt order #1 leftover EVA of mined provincie with live 2025 statutory PDF after leftover AGB/APB hunt). PDF header **Toerisme Limburg / Universiteitslaan 3 / 3500 Hasselt** — NOT Westtoer / Toerisme Oost-Vlaanderen / Toerisme Vlaams-Brabant / Hooibeekhoeve / Puyenbroeck. Distinct from already-mined **Toerisme Vlaams-Brabant 1462** / **Toerisme Oost-Vlaanderen 1461** / **Arboretum Kalmthout 1460** / **Kempens Landschap 1459** / **APB Warande 1458** / **APB De Schorre 1457** / **APB PIH 1456** / **APB TPA 1455** / **APB POA 1454** / **Westtoer** / **Vlabinvest**. First confirmed not already extracted as JR2025 euros: no Toerisme Limburg / 0420.092.944 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **21.09.1979**; statutaire naam Toerisme Limburg since 25.07.1996; afkorting P.V.T.L. since 21.09.1979; VZW since 21.09.1979; zetel Universiteitslaan 3 3500 Hasselt; **1 VE**; 15 functiehouders; dagelijks bestuur Luys Jeroen since 23.04.2018; Werkgever RSZ since 21.09.1979; btw since 01.10.1985; aanbestedende overheid; NACE RSZ 79.901; site https://visitlimburg.be/. Prior-year figures **identiek**. NBB consult SPA timeout; SBM HTML via WebFetch HTTP yielded deposit id. Euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1470).\n"
        "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 **2792619** / **30,4 VTE** vs 2966696 / 32,6): assets **4361033** (was 4323651); fixed **6372** vs 6100 / IVA **0** (aanschaf **185319** fully depreciated) / MVA **6372** (all meubilair; aanschaf **215178**; afschr **208806**) / FVA empty; current **4354661** vs 4317551; LT recv **0** vs 74999; voorraden/bestellingen **841698** vs 942122 (all bestellingen in uitvoering); ST recv **317073** vs 325900 (trade **113850** / other **203223**); geldbeleg **0 DROP** vs 1759446; cash **3172365 JUMP** vs 1182333; prepaid **23526** vs 32750; equity **1621889 JUMP** vs 1102572 (fondsen empty; bestemde **226172** vs 292171; overgedragen **1395717**; kapsubs empty); voorzieningen empty; schulden **2739144 DROP** vs 3221079 (LT empty; ST **2682924** vs 3055362 waarvan leveranciers **623855** vs 717490 + vooruitbetalingen **1534306** vs 1803096 + tax **135493** + bezold **366946**; deferred **56220** vs 165717); brutomarge **3660709 JUMP** vs 1353683 (nrec 76A **9000**); omzet empty; 73 empty; 60/61 empty; pers **2792619** / **30,4 VTE** / 42457 uur / YE **30,9**; afschr **5790**; waardeverm **1975**; andere **204689**; expl **+655636 JUMP** vs -1825243; fin opbr **2642**; fin kosten **138961 JUMP** vs 21737; tax empty vs 6823; PnL **+519317 JUMP** vs -1851957; dividend **0**; onttrekking bestemde **292171**; toevoeging bestemde **226172**; over te dragen **1395717**; capex **6062**. Commissaris fee **7300**. Huur personenwagens buitenbalans **37060**/jaar. Cross-checks: 6372+4354661=4361033; 1621889+2739144=4361033; 226172+1395717=1621889; 2682924+56220=2739144; 623855+1534306+502438+22325=2682924; 3660709-2792619-5790-1975-204689=655636; 655636+2642-138961=519317; 810401+519317+292171-226172=1395717; 263040+6062-53924=215178; 256940+5790-53924=208806; 215178-208806=6372. 1-euro rounding: 841698+317073+3172365+23526=4354662 vs current 4354661; 135493+366946=502439 vs 502438.\n"
        f"- CSVs: sources +4; entities +1 `vzw_tlim` parent `prov_limburg`; budgets +40 executed; commitments +1 envelope 3660709 AV 22.06.2026; leaderboard +1 annual 2792619 / total 4361033; foi_queue +1 status=ready never sent; research_queue surgical rq_1463=done + rq_1464 spawn; loop_state ticks_completed=1463. Inventory after write: budgets {{INV_B}} · commitments {{INV_C}} · leaderboard {{INV_L}} · entities {{INV_E}} · sources {{INV_S}} · FOI ready {{FOI_R}} / answered {{FOI_A}} / partial {{FOI_P}} / total {{FOI_T}}.\n"
        "- FOI: `gap_tlim_omzet_empty_bruto_3_66m_pers_2_79m_l5` ready not sent — empty 70 / empty 73 / empty 60-61 / pers 2.79m 30.4 VTE / 1 VE / cash JUMP 3.17m / geldbeleg DROP 1.76m / vooruitbet 1.53m / fin kosten JUMP 0.14m / PnL JUMP +0.52m / MVA 6.4k / capex 6.1k / commissaris 7.3k / provincie subsidy share unpublished.\n"
        "- Next: rq_1464 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 404 this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1463). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live (IJzer en Leie still no JR this tick). Leftover IGS IVAREM **0267.403.264** still JR2024. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Stichting Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456. Next every-10 is **1470**.\n"
    )
    entry = entry.replace("{INV_B}", str(inv["budgets.csv"])).replace("{INV_C}", str(inv["commitments.csv"])).replace("{INV_L}", str(inv["leaderboard.csv"])).replace("{INV_E}", str(inv["entities.csv"])).replace("{INV_S}", str(inv["sources.csv"])).replace("{FOI_R}", str(foi_ready)).replace("{FOI_A}", str(foi_ans)).replace("{FOI_P}", str(foi_part)).replace("{FOI_T}", str(foi_tot))
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1463 -" in lraw:
        raise SystemExit("loop_log already has tick 1463 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1463")
    print("DONE tick 1463")

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

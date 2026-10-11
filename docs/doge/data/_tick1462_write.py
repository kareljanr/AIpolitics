#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1462 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T15:22:00Z"
ENT = "vzw_tvlb"
SRC = "src_tvlb_jr2025_nbb"
GAP = "gap_tvlb_omzet_empty_bruto_0_55m_pers_0_36m_l5"
LB = "lb_tvlb_omzet_empty_bruto_0_55m_pers_0_36m"
COMM = "comm_tvlb_jr2025_bruto"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00131325.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Toerisme Vlaams-Brabant vzw official NBB WVV VKT-VZW JR2025,{PDF},NBB / Toerisme Vlaams-Brabant vzw,2026-08-19,budget,tick1462; official NBB WVV VKT-VZW JR2025 PDF 12p / 47307 bytes; deposit 2026-00131325; AV 12.05.2026; header 02.06.2026; pdfinfo created 02.06.2026 08:37:57 UTC; model VKT-VZW 26.0.11 m04-f; KBO 0422.667.404; assets 1667400 cash 1597663 debt 470434 pers 364012 omzet empty diensten empty pnl -35880 equity 494894",
        "src_tvlb_site,Toerisme Vlaams-Brabant vzw / VISIT Vlaams-Brabant official sector + provincie tourism pages,https://www.visitvlaamsbrabant.be/contact,Provincie Vlaams-Brabant / TVB vzw,2026-08-19,official_register,tick1462; leftover provincial tourism VZW/EVA of mined provincie Vlaams-Brabant; zetel Provincieplein 1 3010 Leuven; KBO 0422.667.404; SBM HTTP bedrijfsfiche for deposit id",
        "src_kbo_tvlb_0422667404,KBO Toerisme Vlaams-Brabant vzw 0422.667.404,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0422667404,KBO Public Search FOD Economie,2026-08-19,official_register,tick1462; Actief since 15.12.1981; VZW; naam Toerisme Vlaams-Brabant since 23.06.1999; zetel Provincieplein 1 3010 Leuven; 1 VE 2178926638 VISIT Vlaams-Brabant; 19 functiehouders; Werkgever RSZ since 15.06.2009",
        "src_tvlb_foi_contact,Toerisme Vlaams-Brabant FOI channel (toerisme@vlaamsbrabant.be),https://www.vlaamsbrabant.be/nl/over-de-provincie/administratie/provinciale-diensten-en-organisaties/toerisme-vlaams-brabant-vzw,TVB vzw / Provincie Vlaams-Brabant,2026-08-19,official_register,tick1462; leftover provincial tourism VZW; NOT Vlabinvest / Westtoer / Toerisme Oost-Vlaanderen / leftover Toerisme Limburg / leftover APB Inovant / Atlas / leftover APB Puyenbroeck / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / TPA / POA",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nvzw_tvlb," in raw or raw.startswith(b"vzw_tvlb,"):
        raise SystemExit("vzw_tvlb already present")
    if b"0422.667.404" in raw:
        raise SystemExit("Toerisme Vlaams-Brabant KBO already present as entity")
    row = (
        "vzw_tvlb,Toerisme Vlaams-Brabant vzw / VISIT Vlaams-Brabant (leftover provincial tourism VZW/EVA of mined provincie Vlaams-Brabant; NOT Vlabinvest / Westtoer / Toerisme Oost-Vlaanderen / leftover Toerisme Limburg / leftover APB Inovant / Atlas / leftover APB Puyenbroeck / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / TPA / POA),"
        "Tourisme Brabant flamand ASBL (EVA provincial residuel tourisme / VISIT Vlaams-Brabant),"
        "Toerisme Vlaams-Brabant leftover provincial tourism VZW/EVA of mined province of Flemish Brabant (not Vlabinvest / Westtoer / Toerisme Oost-Vlaanderen / leftover Toerisme Limburg / leftover APB Inovant / Atlas / leftover APB Puyenbroeck / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / TPA / POA),"
        "eva,prov_vlaams_brabant,nl,https://www.visitvlaamsbrabant.be/,toerisme@vlaamsbrabant.be,Provincieplein 1 3010 Leuven,"
        "tick1462 leftover residual tourism VZW/EVA after leftover AGB/APB hunt; KBO 0422.667.404 Actief since 15.12.1981; live JR2025 official NBB WVV PDF; sourced euros assets 1667400 omzet empty diensten empty pers 364012 4.7 VTE pnl -35880 equity 494894 cash 1597663 debt 470434 capex 0 dividend 0; FOI ready empty 70 / empty 73 / empty 60-61 / pers 0.36m 4.7 VTE / cash JUMP 1.60m / prepaid DROP / voorzieningen DROP 0.70m / 1 VE; distinct from already-mined Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / Westtoer / Vlabinvest"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 vzw_tvlb")

def part_budgets():
    BUDGETS = [
        ("bud_tvlb_assets_2025", "2025", "1667400", "2025 assets 1667400 (was 1715196); tick1462; primary official NBB WVV VKT-VZW 2026-00131325"),
        ("bud_tvlb_current_2025", "2025", "1667400", "2025 vlottend 1667400 (was 1715196); tick1462; primary official NBB WVV"),
        ("bud_tvlb_cash_2025", "2025", "1597663", "2025 liquide middelen 1597663 JUMP (was 1526483); tick1462; primary official NBB WVV"),
        ("bud_tvlb_geldbeleg_2025", "2025", "0", "2025 geldbeleggingen empty; tick1462; primary official NBB WVV"),
        ("bud_tvlb_strecv_2025", "2025", "2029", "2025 ST vorderingen 2029 (was 2933); tick1462; primary official NBB WVV"),
        ("bud_tvlb_trade_2025", "2025", "1320", "2025 handelsvorderingen 1320 (was 2224); tick1462; primary official NBB WVV"),
        ("bud_tvlb_othrecv_2025", "2025", "709", "2025 overige ST vorderingen 709 unchanged; tick1462; primary official NBB WVV"),
        ("bud_tvlb_voorraden_2025", "2025", "67708", "2025 voorraden 67708 DROP (was 84649); tick1462; primary official NBB WVV"),
        ("bud_tvlb_prepaid_2025", "2025", "0", "2025 overlopend actief 0 DROP (was 101131); tick1462; primary official NBB WVV"),
        ("bud_tvlb_ltrecv_2025", "2025", "0", "2025 LT vorderingen empty; tick1462; primary official NBB WVV"),
        ("bud_tvlb_fixed_2025", "2025", "0", "2025 vaste activa empty (MVA net 0); tick1462; primary official NBB WVV"),
        ("bud_tvlb_iva_2025", "2025", "0", "2025 IVA empty; 6.1.1 not filed; tick1462; primary official NBB WVV"),
        ("bud_tvlb_mva_2025", "2025", "0", "2025 MVA net 0 (aanschaf 608439 fully depreciated); tick1462; primary official NBB WVV"),
        ("bud_tvlb_fva_2025", "2025", "0", "2025 FVA empty; 6.1.3 not filed; tick1462; primary official NBB WVV"),
        ("bud_tvlb_equity_2025", "2025", "494894", "2025 eigen vermogen 494894 JUMP (was 385051; all bestemde fondsen); tick1462; primary official NBB WVV"),
        ("bud_tvlb_fondsen_2025", "2025", "0", "2025 fondsen beginvermogen empty; tick1462; primary official NBB WVV"),
        ("bud_tvlb_bestemde_2025", "2025", "494894", "2025 bestemde fondsen 494894 (was 385051); tick1462; primary official NBB WVV"),
        ("bud_tvlb_overgedragen_2025", "2025", "0", "2025 overgedragen winst empty; tick1462; primary official NBB WVV"),
        ("bud_tvlb_voorz_2025", "2025", "702073", "2025 voorzieningen 702073 DROP (was 926880; all grote herstellingen); tick1462; primary official NBB WVV"),
        ("bud_tvlb_debt_2025", "2025", "470434", "2025 schulden 470434 (was 403265; LT empty); tick1462; primary official NBB WVV"),
        ("bud_tvlb_stdebt_2025", "2025", "159820", "2025 ST schulden 159820 (was 175352); tick1462; primary official NBB WVV"),
        ("bud_tvlb_lev_2025", "2025", "100014", "2025 leveranciers 100014 DROP (was 138096); tick1462; primary official NBB WVV"),
        ("bud_tvlb_bezold_2025", "2025", "31493", "2025 bezoldigingen-schulden 31493 (was 34200); tick1462; primary official NBB WVV"),
        ("bud_tvlb_taxpay_2025", "2025", "28314", "2025 belastingschulden 28314 (was 3056); tick1462; primary official NBB WVV"),
        ("bud_tvlb_deferred_2025", "2025", "310614", "2025 overlopend passief 310614 JUMP (was 227912); tick1462; primary official NBB WVV"),
        ("bud_tvlb_bruto_2025", "2025", "550846", "2025 brutomarge 550846 DROP (was 618885); tick1462; primary official NBB WVV"),
        ("bud_tvlb_omzet_2025", "2025", "0", "2025 omzet 70 empty unpublished; tick1462; primary official NBB WVV"),
        ("bud_tvlb_lidgeld_2025", "2025", "0", "2025 lidgeld/subsidies 73 empty unpublished; tick1462; primary official NBB WVV"),
        ("bud_tvlb_diensten_2025", "2025", "0", "2025 60/61 empty unpublished so diensten unpublished as a split; tick1462; primary official NBB WVV"),
        ("bud_tvlb_pers_2025", "2025", "364012", "2025 pers 62 364012 (was 419363); 4.7 VTE vs 5.6; 7171 uur; YE 4.8; tick1462; primary official NBB WVV"),
        ("bud_tvlb_afschr_2025", "2025", "0", "2025 afschrijvingen empty; tick1462; primary official NBB WVV"),
        ("bud_tvlb_andere_2025", "2025", "311551", "2025 andere bedrijfskosten 311551 (was 363372); tick1462; primary official NBB WVV"),
        ("bud_tvlb_expl_2025", "2025", "-45632", "2025 bedrijfsverlies -45632 (was -11209); tick1462; primary official NBB WVV"),
        ("bud_tvlb_finopbr_2025", "2025", "9015", "2025 financiele opbrengsten 9015 all recurrent; tick1462; primary official NBB WVV"),
        ("bud_tvlb_finkost_2025", "2025", "-737", "2025 financiele kosten -737 credit (was 484); tick1462; primary official NBB WVV"),
        ("bud_tvlb_pnl_2025", "2025", "-35880", "2025 PnL -35880 (was 0); tick1462; primary official NBB WVV"),
        ("bud_tvlb_div_2025", "2025", "0", "2025 dividend 0 VZW; tick1462; primary official NBB WVV"),
        ("bud_tvlb_capex_2025", "2025", "0", "2025 capex MVA aanschaf empty; tick1462; primary official NBB WVV"),
        ("bud_tvlb_onttrekking_2025", "2025", "35880", "2025 onttrekking EV 35880 to cover loss; tick1462; primary official NBB WVV"),
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
        f"{COMM},Toerisme Vlaams-Brabant vzw JR2025 leftover provincial tourism dual (empty 70/73/60-61 / bruto 0.55m / pers 0.36m 4.7 VTE / cash JUMP 1.60m / voorzieningen DROP 0.70m / 1 VE),{ENT},TVB vzw / provincie Vlaams-Brabant dual tourism,WVV VZW; Provinciedecreet; Bestuursdecreet openbaarheid,2026-05-12,1981,,550846,,,active,{PDF},Local leftover tourism VZW map VL Vlaams-Brabant — empty 70/73/60-61 / bruto 0.55m / pers 0.36m 4.7 VTE / cash JUMP 1.60m,Publish omzet+73+60/61 split + 1 VE payroll + cash 1.60m counterparties + provincie subsidy share + voorzieningen herclassificatie; do not keep leftover tourism VZW as unpublished 0.55m tourism shell,{SRC},strong,Vlaanderen>Provincies>VlaamsBrabant>EVA>ToerismeVB>JR2025_L5,tick1462; assets 1667400 omzet empty diensten empty pers 364012 pnl -35880 equity 494894 cash 1597663 debt 470434 capex 0 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT Vlabinvest / Westtoer / Toerisme Oost-Vlaanderen / leftover Toerisme Limburg / leftover APB Inovant / Atlas / leftover APB Puyenbroeck / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / TPA / POA",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Toerisme Vlaams-Brabant vzw JR2025 leftover provincial tourism: empty 70/73/60-61 / bruto 0.55m / pers 0.36m 4.7 VTE / cash JUMP 1.60m / voorzieningen DROP 0.70m / 1 VE,L5,local_budget_line,Vlaanderen>Provincies>VlaamsBrabant>EVA>ToerismeVB>JR2025_L5,364012,1667400,Leftover dual tourism VZW shell: assets 1.67m / equity 0.49m / bruto 0.55m / omzet empty / 73 empty / 60-61 empty / pers 0.36m 4.7 VTE / cash 1.60m JUMP / prepaid DROP / voorzieningen 0.70m DROP / debt 0.47m / PnL -36k / 1 VE; do not treat 0.55m as TE-additive of 348bn,strong,{SRC},TVB vzw / provincie Vlaams-Brabant dual tourism,Local leftover tourism VZW map VL Vlaams-Brabant — JR2025 official NBB WVV live; empty 70/73/60-61 + pers/cash/voorzieningen FOI,Official NBB WVV 2026-08-19: bruto 0.55m / pers 0.36m 4.7 VTE / cash JUMP 1.60m / PnL -36k / 1 VE / omzet empty,6.5,5.5,3.0,6.2,Publish omzet+73+60/61 split + 1 VE payroll + cash 1.60m counterparties + provincie subsidy share + voorzieningen herclassificatie; do not keep leftover tourism VZW as unpublished 0.55m tourism shell,active,,tick1462; leftover tourism VZW/EVA after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / Westtoer / Vlabinvest",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Provincies>VlaamsBrabant>EVA>ToerismeVB>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto 550846 vs 618885 + pers 364012 4.7 VTE + 1 VE 2178926638 + cash 1597663 JUMP vs 1526483 + prepaid 0 DROP vs 101131 + voorzieningen 702073 DROP vs 926880 vs P&L -79085 + equity JUMP 494894 vs 385051 despite PnL -35880 + deferred 310614 JUMP + MVA net 0 / capex 0 + commissaris unpublished (6.6 not filed) + provincie subsidy share unpublished,Leftover tourism VZW Vlaams-Brabant after leftover AGB/APB hunt: empty 70/73/60-61 / bruto 0.55m / pers 0.36m 4.7 VTE / cash JUMP 1.60m / voorzieningen DROP 0.70m / 1 VE hides provincial tourism vehicle,8,Toerisme Vlaams-Brabant vzw / provinciegriffier / Bestuursorgaan,toerisme@vlaamsbrabant.be,Provincieplein 1 3010 Leuven,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1462 leftover tourism VZW/EVA after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF now extracted (47307 bytes 12p). FOI ready not sent. NOT every-10. NOT Toerisme Oost-Vlaanderen / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / TPA / POA / De Gavers / Westtoer / Vlabinvest / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs redirect to Hooibeekhoeve this tick. Leftover Bosgroep WVL Houtland 0866.482.291 still no JR. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. Puyenbroeck still no separate APB 2025 PDF. Leftover Toerisme Limburg not taken this tick.",
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
    if not last_s.startswith("rq_1462,"):
        raise SystemExit(f"expected last row rq_1462, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1462 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1462,Toerisme Vlaams-Brabant JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_tvlb,"
        "Completed: Toerisme Vlaams-Brabant vzw leftover provincial tourism VZW/EVA of mined provincie Vlaams-Brabant after leftover AGB/APB hunt; KBO 0422.667.404 Actief; live JR2025 official NBB WVV VKT-VZW PDF (47307 bytes 12p; deposit 2026-00131325; AV 12.05.2026; header 02.06.2026; pdfinfo 02.06.2026 08:37:57 UTC). PDF header Toerisme Vlaams-Brabant / Provincieplein 1 — NOT Hooibeekhoeve / Puyenbroeck / De Gavers / Westtoer. Sourced euros assets 1667400 omzet empty diensten empty pers 364012 4.7 VTE pnl -35880 equity 494894 cash 1597663 debt 470434 capex 0 dividend 0. FOI "
        f"{GAP} ready not sent. Distinct from already-mined Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / Westtoer / Vlabinvest.,"
        f"{GAP},2026-08-19T15:19:00Z,{TS},"
        "tick1462 Toerisme Vlaams-Brabant leftover tourism VZW residual; KBO 0422.667.404; live JR2025 official NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1463 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Toerisme Limburg if CDN live else leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
    )
    spawn = (
        "rq_1463,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1462 done including Toerisme Vlaams-Brabant 1462 leftover provincial tourism VZW live official NBB WVV / Toerisme Oost-Vlaanderen 1461 leftover provincial tourism VZW live official NBB WVV / Arboretum Kalmthout 1460 leftover EVAP live official NBB WVV + every-10 / Stichting Kempens Landschap 1459 leftover IGS/SON live official NBB WVV / APB Warande 1458 leftover APB live official BBC / APB De Schorre 1457 leftover APB live official BBC / APB PIH 1456 leftover APB live official BBC / APB TPA 1455 leftover APB live official BBC / APB POA 1454 leftover APB live official BBC). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 302 to Hooibeekhoeve as of 1462). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck spotted unmined around 1453 — still no separate APB 2025 PDF as of 1462). Leftover provincial tourism: leftover Toerisme Limburg 0420.092.944 only if a 2025 CDN now downloads. Do NOT confuse with already-mined Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live (still no JR as of 1462). Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1462 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1462. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456.,,"
        f"{TS},{TS},"
        "spawned tick1462 after Toerisme Vlaams-Brabant leftover tourism VZW live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Toerisme Limburg if CDN live else leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1462=done + rq_1463 spawned; keep", last_line_start)

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
    Path("/tmp/tick1462_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1462 Toerisme Vlaams-Brabant leftover tourism VZW residual; KBO 0422.667.404; live JR2025 official NBB WVV PDF; sourced euros assets 1667400 omzet empty diensten empty pers 364012 4.7 VTE pnl -35880 equity 494894 cash 1597663 debt 470434 capex 0 dividend 0; FOI ready empty 70 / empty 73 / empty 60-61 / pers 0.36m 4.7 VTE / cash JUMP 1.60m / prepaid DROP / voorzieningen DROP 0.70m / 1 VE; NOT Toerisme Oost-Vlaanderen / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / TPA / POA / De Gavers / Westtoer / Vlabinvest / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1463 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Toerisme Limburg if CDN live else leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1462,1462,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1462")

    entry = (
        "\n## Tick 1462 - 2026-08-19 - rq_1462 Toerisme Vlaams-Brabant dual residual leftover\n"
        "- Unit: Toerisme Vlaams-Brabant vzw / VISIT Vlaams-Brabant (leftover provincial tourism VZW/EVA of mined provincie Vlaams-Brabant; 1 VE 2.178.926.638) after residual dual hunt (KBO **0422.667.404**; official NBB WVV VKT-VZW PDF **47307** bytes / 12p; deposit **2026-00131325**; AV **12.05.2026**; header **02.06.2026**; pdfinfo created **02.06.2026 08:37:57 UTC**; model **VKT-VZW** 26.0.11 m04-f; commissaris **not filed** (6.6 not neergelegd); VKT-VZW 6.1.1/6.1.3/6.2/6.3/6.5/6.6/7/8 not filed; 6.1.2 MVA + 6.4 + 6.7 sociale balans + 6.8 waarderingsregels filed). Leftover AGB/APB first: leftover APB Inovant / Atlas koepelsite `jaarrekening_25_inov` / `jaarrekening_25_atlas` HEAD **302 redirect to Hooibeekhoeve-jaarverslag-2025-webversie** with Googlebot UA this tick (Foleon leftover slugs have redirected to Hooibeekhoeve — no fetchable 2025 Inovant/Atlas PDF). Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick. Leftover AGB Hasselt / SOLag / WAGSO / Temse / Herk-de-Stad already in entities — skipped. Leftover Bosgroep WVL Houtland 0866.482.291 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover Toerisme Vlaams-Brabant statutory CDN `2026-00131325` live this tick (HTTP 200 / 47307 / 12p; jaar **2025-12-31**; neerlegging **02.06.2026**) — taken (hunt order #1 leftover EVA of mined provincie with live 2025 statutory PDF after leftover AGB/APB hunt). PDF header **Toerisme Vlaams-Brabant / Provincieplein 1 / 3010 Kessel-lo** — NOT Hooibeekhoeve / Puyenbroeck / De Gavers / Westtoer. Distinct from already-mined **Toerisme Oost-Vlaanderen 1461** / **Arboretum Kalmthout 1460** / **Kempens Landschap 1459** / **APB Warande 1458** / **APB De Schorre 1457** / **APB PIH 1456** / **APB TPA 1455** / **APB POA 1454** / **Westtoer** / **Vlabinvest**. First confirmed not already extracted as JR2025 euros: no Toerisme Vlaams-Brabant / 0422.667.404 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **15.12.1981**; statutaire naam Toerisme Vlaams-Brabant since 23.06.1999; VZW since 15.12.1981; zetel Provincieplein 1 3010 Leuven; **1 VE**; 19 functiehouders; Werkgever RSZ since 15.06.2009; btw since 01.06.1982; aanbestedende overheid; NACE 79.901; site https://www.visitvlaamsbrabant.be/. Prior-year figures **identiek**. NBB consult SPA timeout; SBM HTML via WebFetch HTTP yielded deposit id. Euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1470).\n"
        "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 **364012** / **4,7 VTE** vs 419363 / 5,6): assets **1667400** (was 1715196); fixed empty / IVA empty / MVA **0** net (aanschaf **608439** fully depreciated) / FVA empty; current **1667400** vs 1715196; LT recv empty; voorraden **67708** vs 84649; ST recv **2029** vs 2933 (trade **1320** / other **709**); geldbeleg empty; cash **1597663 JUMP** vs 1526483; prepaid **0 DROP** vs 101131; equity **494894 JUMP** vs 385051 (fondsen empty; bestemde **494894**; overgedragen empty; kapsubs empty); voorzieningen **702073 DROP** vs 926880 (all grote herstellingen); schulden **470434** vs 403265 (LT empty; ST **159820** vs 175352 waarvan leveranciers **100014 DROP** vs 138096 + tax **28314** + bezold **31493**; deferred **310614 JUMP** vs 227912); brutomarge **550846 DROP** vs 618885; omzet empty; 73 empty; 60/61 empty; pers **364012** / **4,7 VTE** / 7171 uur / YE **4,8**; afschr empty; voorzieningen P&L **-79085**; andere **311551**; expl **-45632** vs -11209; fin opbr **9015**; fin kosten **-737** (credit); tax empty; PnL **-35880** vs 0; dividend **0**; onttrekking EV **35880**; capex **0**. Commissaris unpublished (6.6 not filed). Cross-checks: 67708+2029+1597663=1667400; 159820+310614=470434; 28314+31493=59807; 550846-364012+79085-311551=-45632; -45632+9015-(-737)=-35880. 1-euro rounding: 494894+702073+470434=1667401 vs assets 1667400; 100014+59807=159821 vs ST 159820.\n"
        f"- CSVs: sources +4; entities +1 `vzw_tvlb` parent `prov_vlaams_brabant`; budgets +39 executed; commitments +1 envelope 550846 AV 12.05.2026; leaderboard +1 annual 364012 / total 1667400; foi_queue +1 status=ready never sent; research_queue surgical rq_1462=done + rq_1463 spawn; loop_state ticks_completed=1462. Inventory after write: budgets {inv['budgets.csv']} · commitments {inv['commitments.csv']} · leaderboard {inv['leaderboard.csv']} · entities {inv['entities.csv']} · sources {inv['sources.csv']} · FOI ready {foi_ready} / answered {foi_ans} / partial {foi_part} / total {foi_tot}.\n"
        "- FOI: `gap_tvlb_omzet_empty_bruto_0_55m_pers_0_36m_l5` ready not sent — empty 70 / empty 73 / empty 60-61 / pers 0.36m 4.7 VTE / 1 VE / cash JUMP 1.60m / prepaid DROP / voorzieningen DROP 0.70m / equity JUMP 0.49m / deferred JUMP 0.31m / MVA net 0 / capex 0 / commissaris unpublished / provincie subsidy share unpublished.\n"
        "- Next: rq_1463 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs redirect to Hooibeekhoeve this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1462). Leftover provincial tourism: leftover **Toerisme Limburg** 0420.092.944 only if a 2025 CDN now downloads. Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live. Leftover IGS IVAREM **0267.403.264** still JR2024. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Stichting Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456. Next every-10 is **1470**.\n"
    )
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1462 -" in lraw:
        raise SystemExit("loop_log already has tick 1462 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1462")
    print("DONE tick 1462")

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

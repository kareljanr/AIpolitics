#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1461 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T15:15:00Z"
ENT = "vzw_tov"
SRC = "src_tov_jr2025_nbb"
GAP = "gap_tov_omzet_empty_bruto_4_12m_pers_3_19m_l5"
LB = "lb_tov_omzet_empty_bruto_4_12m_pers_3_19m"
COMM = "comm_tov_jr2025_bruto"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00206793.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Toerisme Oost-Vlaanderen vzw official NBB WVV VKT-VZW JR2025,{PDF},NBB / Toerisme Oost-Vlaanderen vzw,2026-08-19,budget,tick1461; official NBB WVV VKT-VZW JR2025 PDF 21p / 310229 bytes; deposit 2026-00206793; AV 24.06.2026; header 25.06.2026; pdfinfo created 27.06.2026 UTC; model VKT-VZW 23.0.10 m04-f; KBO 0407.710.695; assets 3400882 cash 2519862 debt 806233 pers 3188667 omzet empty diensten empty pnl 234588 equity 2409808",
        "src_tov_site,Toerisme Oost-Vlaanderen vzw official sector + provincie tourism pages,https://toerismeoostvlaanderen.be/over-ons/wie-zijn-we/toerisme-oost-vlaanderen-vzw,Provincie Oost-Vlaanderen / TOV vzw,2026-08-19,official_register,tick1461; leftover provincial tourism VZW/EVA of mined provincie Oost-Vlaanderen; zetel Charles de Kerchovelaan 189 9000 Gent; site https://www.tov.be/; NBB consult page for deposit id",
        "src_kbo_tov_0407710695,KBO Toerisme Oost-Vlaanderen vzw 0407.710.695,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407710695,KBO Public Search FOD Economie,2026-08-19,official_register,tick1461; Actief since 25.02.1948; VZW; naam Toerisme Oost-Vlaanderen since 01.02.1996; zetel Charles de Kerchovelaan 189 9000 Gent; 2 VE 2143364755 + 2143365349; 26 functiehouders; Werkgever RSZ since 01.10.1957",
        "src_tov_foi_contact,Toerisme Oost-Vlaanderen FOI channel (toerisme@oost-vlaanderen.be),https://toerismeoostvlaanderen.be/,TOV vzw / Provincie Oost-Vlaanderen,2026-08-19,official_register,tick1461; leftover provincial tourism VZW; NOT APB De Gavers / leftover APB Puyenbroeck / leftover APB Inovant / Atlas / Westtoer / Toerisme Limburg / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / TPA / POA",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nvzw_tov," in raw or raw.startswith(b"vzw_tov,"):
        raise SystemExit("vzw_tov already present")
    if b"0407.710.695" in raw:
        raise SystemExit("Toerisme Oost-Vlaanderen KBO already present as entity")
    row = (
        "vzw_tov,Toerisme Oost-Vlaanderen vzw (leftover provincial tourism VZW/EVA of mined provincie Oost-Vlaanderen; NOT APB De Gavers / leftover APB Puyenbroeck / leftover APB Inovant / Atlas / Westtoer / Toerisme Limburg / Toerisme Vlaams-Brabant / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / TPA / POA),"
        "Tourisme Flandre orientale ASBL (EVA provincial residuel tourisme),"
        "Toerisme Oost-Vlaanderen leftover provincial tourism VZW/EVA of mined province of East Flanders (not APB De Gavers / leftover APB Puyenbroeck / leftover APB Inovant / Atlas / Westtoer / Toerisme Limburg / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / TPA / POA),"
        "eva,prov_oost_vlaanderen,nl,https://toerismeoostvlaanderen.be/,toerisme@oost-vlaanderen.be,Charles de Kerchovelaan 189 9000 Gent,"
        "tick1461 leftover residual tourism VZW/EVA after leftover AGB/APB hunt; KBO 0407.710.695 Actief since 25.02.1948; live JR2025 official NBB WVV PDF; sourced euros assets 3400882 omzet empty diensten empty pers 3188667 34.9 VTE pnl 234588 equity 2409808 cash 2519862 debt 806233 capex 46247 dividend 0; FOI ready empty 70 / empty 73 / empty 60-61 / pers 3.19m 34.9 VTE / cash JUMP 2.52m / geldbeleg DROP 0.62m / 2 VE; distinct from already-mined Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / APB De Gavers / Westtoer"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 vzw_tov")

def part_budgets():
    BUDGETS = [
        ("bud_tov_assets_2025", "2025", "3400882", "2025 assets 3400882 (was 3362549); tick1461; primary official NBB WVV VKT-VZW 2026-00206793"),
        ("bud_tov_current_2025", "2025", "3356694", "2025 vlottend 3356694 (was 3343485); tick1461; primary official NBB WVV"),
        ("bud_tov_cash_2025", "2025", "2519862", "2025 liquide middelen 2519862 JUMP (was 2150554); tick1461; primary official NBB WVV"),
        ("bud_tov_geldbeleg_2025", "2025", "615861", "2025 geldbeleggingen 615861 DROP (was 913057); tick1461; primary official NBB WVV"),
        ("bud_tov_strecv_2025", "2025", "118158", "2025 ST vorderingen 118158 (was 126018); tick1461; primary official NBB WVV"),
        ("bud_tov_trade_2025", "2025", "11792", "2025 handelsvorderingen 11792 (was 28253); tick1461; primary official NBB WVV"),
        ("bud_tov_othrecv_2025", "2025", "106365", "2025 overige ST vorderingen 106365 (was 97765); tick1461; primary official NBB WVV"),
        ("bud_tov_voorraden_2025", "2025", "17985", "2025 voorraden 17985 DROP (was 33420); tick1461; primary official NBB WVV"),
        ("bud_tov_prepaid_2025", "2025", "84828", "2025 overlopend actief 84828 (was 65639); tick1461; primary official NBB WVV"),
        ("bud_tov_ltrecv_2025", "2025", "0", "2025 LT vorderingen empty (was 54796); tick1461; primary official NBB WVV"),
        ("bud_tov_fixed_2025", "2025", "44188", "2025 vaste activa 44188 (was 19063); tick1461; primary official NBB WVV"),
        ("bud_tov_iva_2025", "2025", "0", "2025 IVA empty; tick1461; primary official NBB WVV"),
        ("bud_tov_mva_2025", "2025", "42465", "2025 MVA 42465 (was 17347; all meubilair); tick1461; primary official NBB WVV"),
        ("bud_tov_fva_2025", "2025", "1723", "2025 FVA 1723 (was 1717); tick1461; primary official NBB WVV"),
        ("bud_tov_equity_2025", "2025", "2409808", "2025 eigen vermogen 2409808 (was 2175220); tick1461; primary official NBB WVV"),
        ("bud_tov_fondsen_2025", "2025", "94870", "2025 fondsen beginvermogen 94870 unchanged; tick1461; primary official NBB WVV"),
        ("bud_tov_bestemde_2025", "2025", "760000", "2025 bestemde fondsen 760000 (was 634000; dotatie 126000); tick1461; primary official NBB WVV"),
        ("bud_tov_overgedragen_2025", "2025", "1554938", "2025 overgedragen winst 1554938 (was 1446350); tick1461; primary official NBB WVV"),
        ("bud_tov_voorz_2025", "2025", "184841", "2025 voorzieningen 184841 (was 172081); tick1461; primary official NBB WVV"),
        ("bud_tov_debt_2025", "2025", "806233", "2025 schulden 806233 DROP (was 1015248; LT empty); tick1461; primary official NBB WVV"),
        ("bud_tov_stdebt_2025", "2025", "638831", "2025 ST schulden 638831 (was 717694); tick1461; primary official NBB WVV"),
        ("bud_tov_lev_2025", "2025", "303619", "2025 leveranciers 303619 DROP (was 405415); tick1461; primary official NBB WVV"),
        ("bud_tov_bezold_2025", "2025", "311705", "2025 bezoldigingen-schulden 311705 (was 295776); tick1461; primary official NBB WVV"),
        ("bud_tov_taxpay_2025", "2025", "23506", "2025 belastingschulden 23506 (was 16503); tick1461; primary official NBB WVV"),
        ("bud_tov_deferred_2025", "2025", "167402", "2025 overlopend passief 167402 DROP (was 297554); tick1461; primary official NBB WVV"),
        ("bud_tov_bruto_2025", "2025", "4121686", "2025 brutomarge 4121686 (was 4038182); tick1461; primary official NBB WVV"),
        ("bud_tov_omzet_2025", "2025", "0", "2025 omzet 70 empty unpublished; tick1461; primary official NBB WVV"),
        ("bud_tov_lidgeld_2025", "2025", "0", "2025 lidgeld/subsidies 73 empty unpublished; tick1461; primary official NBB WVV"),
        ("bud_tov_diensten_2025", "2025", "0", "2025 60/61 empty unpublished so diensten unpublished as a split; tick1461; primary official NBB WVV"),
        ("bud_tov_pers_2025", "2025", "3188667", "2025 pers 62 3188667 (was 3011246); 34.9 VTE vs 34.8; 48742 uur; YE 35.5; tick1461; primary official NBB WVV"),
        ("bud_tov_afschr_2025", "2025", "21129", "2025 afschrijvingen 21129 (was 14740); tick1461; primary official NBB WVV"),
        ("bud_tov_andere_2025", "2025", "674685", "2025 andere bedrijfskosten 674685 (was 832580); tick1461; primary official NBB WVV"),
        ("bud_tov_expl_2025", "2025", "224701", "2025 bedrijfswinst 224701 (was 180341); tick1461; primary official NBB WVV"),
        ("bud_tov_finopbr_2025", "2025", "9887", "2025 financiele opbrengsten 9887 all recurrent; tick1461; primary official NBB WVV"),
        ("bud_tov_finkost_2025", "2025", "0", "2025 financiele kosten empty; tick1461; primary official NBB WVV"),
        ("bud_tov_pnl_2025", "2025", "234588", "2025 PnL 234588 (was 193818); tick1461; primary official NBB WVV"),
        ("bud_tov_div_2025", "2025", "0", "2025 dividend 0 VZW; tick1461; primary official NBB WVV"),
        ("bud_tov_capex_2025", "2025", "46247", "2025 capex MVA aanschaf 46247; tick1461; primary official NBB WVV"),
        ("bud_tov_commissaris_2025", "2025", "6500", "2025 commissaris fee 6500 FIGURAD / Loontjens Geoffrey; tick1461; primary official NBB WVV"),
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
        f"{COMM},Toerisme Oost-Vlaanderen vzw JR2025 leftover provincial tourism dual (empty 70/73/60-61 / bruto 4.12m / pers 3.19m 34.9 VTE / cash JUMP 2.52m / 2 VE),{ENT},TOV vzw / provincie Oost-Vlaanderen dual tourism,WVV VZW; Provinciedecreet; Bestuursdecreet openbaarheid,2026-06-24,1948,,4121686,,,active,{PDF},Local leftover tourism VZW map VL Oost-Vlaanderen — empty 70/73/60-61 / bruto 4.12m / pers 3.19m 34.9 VTE / cash JUMP 2.52m,Publish omzet+73+60/61 split + 2 VE payroll + cash 2.52m counterparties + provincie subsidy share; do not keep leftover tourism VZW as unpublished 4.12m tourism shell,{SRC},strong,Vlaanderen>Provincies>OostVlaanderen>EVA>ToerismeOV>JR2025_L5,tick1461; assets 3400882 omzet empty diensten empty pers 3188667 pnl 234588 equity 2409808 cash 2519862 debt 806233 capex 46247 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT De Gavers / Puyenbroeck / Inovant / Atlas / Westtoer / Toerisme Limburg / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / TPA / POA",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Toerisme Oost-Vlaanderen vzw JR2025 leftover provincial tourism: empty 70/73/60-61 / bruto 4.12m / pers 3.19m 34.9 VTE / cash JUMP 2.52m / 2 VE,L5,local_budget_line,Vlaanderen>Provincies>OostVlaanderen>EVA>ToerismeOV>JR2025_L5,3188667,3400882,Leftover dual tourism VZW shell: assets 3.40m / equity 2.41m / bruto 4.12m / omzet empty / 73 empty / 60-61 empty / pers 3.19m 34.9 VTE / cash 2.52m JUMP / geldbeleg 0.62m DROP / debt 0.81m DROP / PnL +235k / 2 VE; do not treat 4.12m as TE-additive of 348bn,strong,{SRC},TOV vzw / provincie Oost-Vlaanderen dual tourism,Local leftover tourism VZW map VL Oost-Vlaanderen — JR2025 official NBB WVV live; empty 70/73/60-61 + pers/cash FOI,Official NBB WVV 2026-08-19: bruto 4.12m / pers 3.19m 34.9 VTE / cash JUMP 2.52m / PnL +235k / 2 VE / omzet empty,6.5,6.2,3.0,6.5,Publish omzet+73+60/61 split + 2 VE payroll + cash 2.52m counterparties + provincie subsidy share; do not keep leftover tourism VZW as unpublished 4.12m tourism shell,active,,tick1461; leftover tourism VZW/EVA after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / APB De Gavers / Westtoer",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Provincies>OostVlaanderen>EVA>ToerismeOV>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto 4121686 vs 4038182 + pers 3188667 34.9 VTE + 2 VE 2143364755/2143365349 + cash 2519862 JUMP vs 2150554 + geldbeleg 615861 DROP vs 913057 + debt 806233 DROP vs 1015248 + leveranciers 303619 DROP + MVA 42465 + capex 46247 + commissaris 6500 + provincie subsidy share unpublished,Leftover tourism VZW Oost-Vlaanderen after leftover AGB/APB hunt: empty 70/73/60-61 / bruto 4.12m / pers 3.19m 34.9 VTE / cash JUMP 2.52m / 2 VE hides provincial tourism vehicle,8,Toerisme Oost-Vlaanderen vzw / provinciegriffier / Bestuursorgaan,toerisme@oost-vlaanderen.be,Charles de Kerchovelaan 189 9000 Gent,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1461 leftover tourism VZW/EVA after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF now extracted (310229 bytes 21p). FOI ready not sent. NOT every-10. NOT Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / TPA / POA / De Gavers / Westtoer / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep WVL Houtland 0866.482.291 still no JR. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. Puyenbroeck still no separate APB 2025 PDF.",
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
    if not last_s.startswith("rq_1461,"):
        raise SystemExit(f"expected last row rq_1461, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1461 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1461,Toerisme Oost-Vlaanderen JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_tov,"
        "Completed: Toerisme Oost-Vlaanderen vzw leftover provincial tourism VZW/EVA of mined provincie Oost-Vlaanderen after leftover AGB/APB hunt; KBO 0407.710.695 Actief; live JR2025 official NBB WVV VKT-VZW PDF (310229 bytes 21p; deposit 2026-00206793; AV 24.06.2026; header 25.06.2026; pdfinfo 27.06.2026 UTC). PDF header TOERISME OOST-VLAANDEREN / Charles de Kerchovelaan 189 — NOT De Gavers / Puyenbroeck / Hooibeekhoeve. Sourced euros assets 3400882 omzet empty diensten empty pers 3188667 34.9 VTE pnl 234588 equity 2409808 cash 2519862 debt 806233 capex 46247 dividend 0. FOI "
        f"{GAP} ready not sent. Distinct from already-mined Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / APB De Gavers / Westtoer.,"
        f"{GAP},2026-08-19T15:10:00Z,{TS},"
        "tick1461 Toerisme Oost-Vlaanderen leftover tourism VZW residual; KBO 0407.710.695; live JR2025 official NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1462 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
    )
    spawn = (
        "rq_1462,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1461 done including Toerisme Oost-Vlaanderen 1461 leftover provincial tourism VZW live official NBB WVV / Arboretum Kalmthout 1460 leftover EVAP live official NBB WVV + every-10 / Stichting Kempens Landschap 1459 leftover IGS/SON live official NBB WVV / APB Warande 1458 leftover APB live official BBC / APB De Schorre 1457 leftover APB live official BBC / APB PIH 1456 leftover APB live official BBC / APB TPA 1455 leftover APB live official BBC / APB POA 1454 leftover APB live official BBC). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 404 as of 1461). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck spotted unmined around 1453 — still no separate APB 2025 PDF as of 1461). Do NOT confuse with already-mined Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live (still no JR as of 1461). Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1461 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1461. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456.,,"
        f"{TS},{TS},"
        "spawned tick1461 after Toerisme Oost-Vlaanderen leftover tourism VZW live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1461=done + rq_1462 spawned; keep", last_line_start)

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
    Path("/tmp/tick1461_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1461 Toerisme Oost-Vlaanderen leftover tourism VZW residual; KBO 0407.710.695; live JR2025 official NBB WVV PDF; sourced euros assets 3400882 omzet empty diensten empty pers 3188667 34.9 VTE pnl 234588 equity 2409808 cash 2519862 debt 806233 capex 46247 dividend 0; FOI ready empty 70 / empty 73 / empty 60-61 / pers 3.19m 34.9 VTE / cash JUMP 2.52m / geldbeleg DROP 0.62m / 2 VE; NOT Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / TPA / POA / De Gavers / Westtoer / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1462 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1461,1461,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1461")

    entry = (
        "\\n## Tick 1461 - 2026-08-19 - rq_1461 Toerisme Oost-Vlaanderen dual residual leftover\\n"
        "- Unit: Toerisme Oost-Vlaanderen vzw (leftover provincial tourism VZW/EVA of mined provincie Oost-Vlaanderen; 2 VE 2.143.364.755 + 2.143.365.349) after residual dual hunt (KBO **0407.710.695**; official NBB WVV VKT-VZW PDF **310229** bytes / 21p; deposit **2026-00206793**; AV **24.06.2026**; header **25.06.2026**; pdfinfo created **27.06.2026 UTC**; model **VKT-VZW** 23.0.10 m04-f; commissaris FIGURAD BEDRIJFSREVISOREN BV B00027 / 0423.109.644 / Loontjens Geoffrey A02712 fee **6500**; VKT-VZW 6.1.1/6.3/6.5/7 not filed; 6.1.2 MVA + 6.1.3 FVA + 6.2 fondsen + 6.4 + 6.6 + 6.7 sociale balans + 6.8 waarderingsregels filed). Leftover AGB/APB first: leftover APB Inovant / Atlas koepelsite `jaarrekening_25_inov` / `jaarrekening_25_atlas` HEAD **404** on 2026-05-28 and 2026-06-25 with Googlebot UA this tick (Foleon leftover slugs have redirected to Hooibeekhoeve — no fetchable 2025 PDF). Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick. Leftover AGB Hasselt / SOLag / WAGSO / Temse / Herk-de-Stad already in entities — skipped. Leftover Bosgroep WVL Houtland 0866.482.291 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover Toerisme Oost-Vlaanderen statutory CDN `2026-00206793` live this tick (HTTP 200 / application/pdf / 310229 / 21p; jaar **2025-12-31**; neerlegging **25.06.2026**) — taken (hunt order #1 leftover EVA of mined provincie with live 2025 statutory PDF after leftover AGB/APB hunt). PDF header **TOERISME OOST-VLAANDEREN / Provinciehuis - Charles de Kerchovelaan 189 / 9000 Gent** — NOT De Gavers / Puyenbroeck / Hooibeekhoeve. Distinct from already-mined **Arboretum Kalmthout 1460** / **Kempens Landschap 1459** / **APB Warande 1458** / **APB De Schorre 1457** / **APB PIH 1456** / **APB TPA 1455** / **APB POA 1454** / **APB De Gavers** / **Westtoer**. First confirmed not already extracted as JR2025 euros: no Toerisme Oost-Vlaanderen / 0407.710.695 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **25.02.1948**; statutaire naam Toerisme Oost-Vlaanderen since 01.02.1996; VZW since 25.02.1948; zetel Charles de Kerchovelaan 189 9000 Gent; **2 VE**; 26 functiehouders; Werkgever RSZ since 01.10.1957; btw since 01.02.1989; aanbestedende overheid; NACE 79.901; site https://toerismeoostvlaanderen.be/. Prior-year figures **identiek**. NBB consult SPA; SBM HTML IP-blacklisted from box curl; WebFetch NBB consult yielded deposit id. Euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1470).\\n"
        "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 **3188667** / **34,9 VTE** vs 3011246 / 34,8): assets **3400882** (was 3362549); fixed **44188** vs 19063 / IVA empty / MVA **42465** vs 17347 (all meubilair) / FVA **1723**; current **3356694** vs 3343485; LT recv empty vs 54796; voorraden **17985** vs 33420; ST recv **118158** vs 126018 (trade **11792** / other **106365**); geldbeleg **615861 DROP** vs 913057; cash **2519862 JUMP** vs 2150554; prepaid **84828** vs 65639; equity **2409808** vs 2175220 (fondsen **94870**; bestemde **760000** vs 634000; overgedragen **1554938**; kapsubs empty); voorzieningen **184841** vs 172081; schulden **806233 DROP** vs 1015248 (LT empty; ST **638831** vs 717694 waarvan leveranciers **303619 DROP** vs 405415 + tax **23506** + bezold **311705**; deferred **167402** vs 297554); brutomarge **4121686** vs 4038182; omzet empty; 73 empty; 60/61 empty; pers **3188667** / **34,9 VTE** / 48742 uur / YE **35,5**; afschr **21129**; waardeverm **-255**; voorzieningen P&L **+12760**; andere **674685**; expl **+224701** vs +180341; fin opbr **9887**; fin kosten empty; tax empty; PnL **+234588** vs +193818; dividend **0**; toevoeging bestemde **126000**; over te dragen **1554938**; capex **46247**. Commissaris fee **6500**. Cross-checks: 44188+3356694=3400882; 2409808+184841+806233=3400882; 42465+1723=44188; 17985+118158+615861+2519862+84828=3356694; 94870+760000+1554938=2409808; 638831+167402=806233; 224701+9887=234588.\\n"
        f"- CSVs: sources +4; entities +1 `vzw_tov` parent `prov_oost_vlaanderen`; budgets +39 executed; commitments +1 envelope 4121686 AV 24.06.2026; leaderboard +1 annual 3188667 / total 3400882; foi_queue +1 status=ready never sent; research_queue surgical rq_1461=done + rq_1462 spawn; loop_state ticks_completed=1461. Inventory after write: budgets {{inv['budgets.csv']}} · commitments {{inv['commitments.csv']}} · leaderboard {{inv['leaderboard.csv']}} · entities {{inv['entities.csv']}} · sources {{inv['sources.csv']}} · FOI ready {{foi_ready}} / answered {{foi_ans}} / partial {{foi_part}} / total {{foi_tot}}.\\n"
        "- FOI: `gap_tov_omzet_empty_bruto_4_12m_pers_3_19m_l5` ready not sent — empty 70 / empty 73 / empty 60-61 / pers 3.19m 34.9 VTE / 2 VE / cash JUMP 2.52m / geldbeleg DROP 0.62m / debt DROP 0.81m / MVA 42k / capex 46k / commissaris 6.5k / provincie subsidy share unpublished.\\n"
        "- Next: rq_1462 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 404 this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1461). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live. Leftover IGS IVAREM **0267.403.264** still JR2024. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Stichting Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456. Next every-10 is **1470**.\\n"
    )
    # fix the f-string braces that were escaped
    entry = entry.replace("{inv['budgets.csv']}", str(inv['budgets.csv']))
    entry = entry.replace("{inv['commitments.csv']}", str(inv['commitments.csv']))
    entry = entry.replace("{inv['leaderboard.csv']}", str(inv['leaderboard.csv']))
    entry = entry.replace("{inv['entities.csv']}", str(inv['entities.csv']))
    entry = entry.replace("{inv['sources.csv']}", str(inv['sources.csv']))
    entry = entry.replace("{foi_ready}", str(foi_ready))
    entry = entry.replace("{foi_ans}", str(foi_ans))
    entry = entry.replace("{foi_part}", str(foi_part))
    entry = entry.replace("{foi_tot}", str(foi_tot))
    entry = entry.replace("\\n", "\n")
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1461 -" in lraw:
        raise SystemExit("loop_log already has tick 1461 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1461")
    print("DONE tick 1461")

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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1460 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T15:10:00Z"
ENT = "evap_arbk"
SRC = "src_arbk_jr2025_nbb"
GAP = "gap_arbk_omzet_empty_bruto_1_55m_pers_1_40m_l5"
LB = "lb_arbk_omzet_empty_bruto_1_55m_pers_1_40m"
COMM = "comm_arbk_jr2025_bruto"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00103572.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Arboretum Kalmthout vzw official NBB WVV VKT-VZW JR2025,{PDF},NBB / Arboretum Kalmthout vzw / EVAP AK,2026-08-19,budget,tick1460; official NBB WVV VKT-VZW JR2025 PDF 20p / 2831768 bytes; deposit 2026-00103572; AV 21.04.2026; header 05.05.2026; pdfinfo created 06.05.2026 UTC; model VKT-VZW 25.0.11 m04-f; KBO 0418.558.364; assets 1321730 cash 971509 debt 331977 pers 1397239 omzet empty diensten empty pnl 80699 equity 989753",
        "src_arbk_site,Arboretum Kalmthout vzw official EVAP locatie + besluiten-statuten pages,https://www.provincieantwerpen.be/nl/locaties/arboretum-kalmthout/besluiten-statuten,Provincie Antwerpen / EVAP AK,2026-08-19,official_register,tick1460; leftover EVAP of mined provincie Antwerpen + leftover of mined city Kalmthout; zetel Heuvel 8 2920 Kalmthout; site https://www.arboretumkalmthout.be/; NBB consult page for deposit id",
        "src_kbo_arbk_0418558364,KBO Arboretum Kalmthout vzw / EVAP AK 0418.558.364,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418558364,KBO Public Search FOD Economie,2026-08-19,official_register,tick1460; Actief since 06.06.1978; VZW; naam Arboretum Kalmthout vzw since 23.05.2023; afkorting EVAP AK since 18.12.2012; zetel Heuvel (Dp) 8 2920 Kalmthout; 1 VE 2155696524 since 23.08.2006; 13 functiehouders; bestuurder provincie 0207.725.597 since 28.12.2012; Werkgever RSZ since 01.10.1978",
        "src_arbk_foi_contact,Arboretum Kalmthout FOI channel (openbaarheid@provincieantwerpen.be),https://www.arboretumkalmthout.be/,EVAP AK / Provincie Antwerpen,2026-08-19,official_register,tick1460; leftover provincial EVAP botanic garden; NOT AGB Kalmthout / city Kalmthout / EVA Pluimveehouderij / leftover APB Inovant / Atlas / Warande / De Schorre / PIH / TPA / POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / Zilvermeer / De Nekker / Kempens Landschap",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nevap_arbk," in raw or raw.startswith(b"evap_arbk,"):
        raise SystemExit("evap_arbk already present")
    if b"0418.558.364" in raw:
        raise SystemExit("Arboretum Kalmthout KBO already present as entity")
    row = (
        "evap_arbk,Arboretum Kalmthout vzw (EVAP AK leftover provincial EVAP of mined provincie Antwerpen + leftover of mined city Kalmthout; NOT AGB Kalmthout / city Kalmthout / EVA Pluimveehouderij / leftover APB Inovant / Atlas / Warande / De Schorre / PIH / TPA / POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / Zilvermeer / De Nekker / Kempens Landschap),"
        "Arboretum de Kalmthout ASBL (EVAP provincial residuel jardin botanique),"
        "Arboretum Kalmthout leftover provincial EVAP botanic garden of mined province of Antwerp + leftover of mined city Kalmthout (not AGB Kalmthout / city Kalmthout / EVA Pluimveehouderij / leftover APB Inovant / Atlas / Warande / De Schorre / PIH / TPA / POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / Zilvermeer / De Nekker / Kempens Landschap),"
        "eva,prov_antwerpen,nl,https://www.arboretumkalmthout.be/,openbaarheid@provincieantwerpen.be,Heuvel 8 2920 Kalmthout,"
        "tick1460 leftover residual EVAP after leftover AGB/APB hunt; KBO 0418.558.364 Actief since 06.06.1978; live JR2025 official NBB WVV PDF; sourced euros assets 1321730 omzet empty diensten empty pers 1397239 19.5 VTE pnl 80699 equity 989753 cash 971509 debt 331977 capex 78207 dividend 0; FOI ready empty 70 / empty 73 / empty 60-61 / pers 1.40m 19.5 VTE / cash JUMP 0.97m / geldbeleg DROP 0.09m / 1 VE; distinct from already-mined Stichting Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 evap_arbk")

def part_budgets():
    BUDGETS = [
        ("bud_arbk_assets_2025", "2025", "1321730", "2025 assets 1321730 (was 1302867); tick1460; primary official NBB WVV VKT-VZW 2026-00103572"),
        ("bud_arbk_current_2025", "2025", "1145716", "2025 vlottend 1145716 (was 1141028); tick1460; primary official NBB WVV"),
        ("bud_arbk_cash_2025", "2025", "971509", "2025 liquide middelen 971509 JUMP (was 760222); tick1460; primary official NBB WVV"),
        ("bud_arbk_geldbeleg_2025", "2025", "86994", "2025 geldbeleggingen 86994 DROP (was 286994); tick1460; primary official NBB WVV"),
        ("bud_arbk_strecv_2025", "2025", "34441", "2025 ST vorderingen 34441 (was 33022); tick1460; primary official NBB WVV"),
        ("bud_arbk_trade_2025", "2025", "27110", "2025 handelsvorderingen 27110 (was 20026); tick1460; primary official NBB WVV"),
        ("bud_arbk_othrecv_2025", "2025", "7331", "2025 overige ST vorderingen 7331 (was 12996); tick1460; primary official NBB WVV"),
        ("bud_arbk_voorraden_2025", "2025", "41027", "2025 voorraden 41027 DROP (was 53605); tick1460; primary official NBB WVV"),
        ("bud_arbk_prepaid_2025", "2025", "11745", "2025 overlopend actief 11745 (was 7185); tick1460; primary official NBB WVV"),
        ("bud_arbk_fixed_2025", "2025", "176014", "2025 vaste activa 176014 (was 161839); tick1460; primary official NBB WVV"),
        ("bud_arbk_iva_2025", "2025", "0", "2025 IVA empty; tick1460; primary official NBB WVV"),
        ("bud_arbk_mva_2025", "2025", "175764", "2025 MVA 175764 (was 161589); tick1460; primary official NBB WVV"),
        ("bud_arbk_terreinen_2025", "2025", "68513", "2025 terreinen/gebouwen 68513 (was 66276); tick1460; primary official NBB WVV"),
        ("bud_arbk_install_2025", "2025", "105806", "2025 installaties 105806 (was 91797); tick1460; primary official NBB WVV"),
        ("bud_arbk_meubilair_2025", "2025", "1445", "2025 meubilair 1445 (was 3516); tick1460; primary official NBB WVV"),
        ("bud_arbk_fva_2025", "2025", "250", "2025 FVA 250 unchanged; tick1460; primary official NBB WVV"),
        ("bud_arbk_equity_2025", "2025", "989753", "2025 eigen vermogen 989753 (was 909054); tick1460; primary official NBB WVV"),
        ("bud_arbk_fondsen_2025", "2025", "346238", "2025 fondsen beginvermogen 346238 unchanged; tick1460; primary official NBB WVV"),
        ("bud_arbk_bestemde_2025", "2025", "562816", "2025 bestemde fondsen 562816 unchanged; tick1460; primary official NBB WVV"),
        ("bud_arbk_overgedragen_2025", "2025", "80699", "2025 overgedragen winst 80699; tick1460; primary official NBB WVV"),
        ("bud_arbk_debt_2025", "2025", "331977", "2025 schulden 331977 DROP (was 393813; LT empty); tick1460; primary official NBB WVV"),
        ("bud_arbk_stdebt_2025", "2025", "268325", "2025 ST schulden 268325 (was 332867); tick1460; primary official NBB WVV"),
        ("bud_arbk_lev_2025", "2025", "74904", "2025 leveranciers 74904 DROP (was 106011); tick1460; primary official NBB WVV"),
        ("bud_arbk_bezold_2025", "2025", "150950", "2025 bezoldigingen-schulden 150950 (was 172994); tick1460; primary official NBB WVV"),
        ("bud_arbk_taxpay_2025", "2025", "42471", "2025 belastingschulden 42471 (was 53862); tick1460; primary official NBB WVV"),
        ("bud_arbk_deferred_2025", "2025", "63652", "2025 overlopend passief 63652 (was 60946); tick1460; primary official NBB WVV"),
        ("bud_arbk_bruto_2025", "2025", "1550751", "2025 brutomarge 1550751 (was 1450728); tick1460; primary official NBB WVV"),
        ("bud_arbk_omzet_2025", "2025", "0", "2025 omzet 70 empty unpublished; tick1460; primary official NBB WVV"),
        ("bud_arbk_lidgeld_2025", "2025", "0", "2025 lidgeld/subsidies 73 empty unpublished; tick1460; primary official NBB WVV"),
        ("bud_arbk_diensten_2025", "2025", "0", "2025 60/61 empty unpublished so diensten unpublished as a split; tick1460; primary official NBB WVV"),
        ("bud_arbk_pers_2025", "2025", "1397239", "2025 pers 62 1397239 JUMP (was 1300962); 19.5 VTE vs 19.7; 31194 uur; YE 19.6; tick1460; primary official NBB WVV"),
        ("bud_arbk_afschr_2025", "2025", "64032", "2025 afschrijvingen 64032 (was 56935); tick1460; primary official NBB WVV"),
        ("bud_arbk_andere_2025", "2025", "5111", "2025 andere bedrijfskosten 5111 (was 6834); tick1460; primary official NBB WVV"),
        ("bud_arbk_expl_2025", "2025", "84369", "2025 bedrijfswinst 84369 (was 85997); tick1460; primary official NBB WVV"),
        ("bud_arbk_finopbr_2025", "2025", "5255", "2025 financiele opbrengsten 5255 (rec 5254 + nrec 1); tick1460; primary official NBB WVV"),
        ("bud_arbk_finkost_2025", "2025", "8925", "2025 financiele kosten 8925 all recurrent; tick1460; primary official NBB WVV"),
        ("bud_arbk_pnl_2025", "2025", "80699", "2025 PnL 80699 (was 83009); tick1460; primary official NBB WVV"),
        ("bud_arbk_div_2025", "2025", "0", "2025 dividend 0 VZW; tick1460; primary official NBB WVV"),
        ("bud_arbk_capex_2025", "2025", "78207", "2025 capex MVA aanschaf 78207 (overdrachten 30680); tick1460; primary official NBB WVV"),
        ("bud_arbk_commissaris_2025", "2025", "7210", "2025 commissaris fee 7210 Callens Vandelanotte / Snoeks Ken; tick1460; primary official NBB WVV"),
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
        f"{COMM},Arboretum Kalmthout vzw JR2025 leftover provincial EVAP dual (empty 70/73/60-61 / bruto 1.55m / pers 1.40m 19.5 VTE / cash JUMP 0.97m / 1 VE),{ENT},EVAP AK / provincie Antwerpen dual botanic garden,WVV VZW EVAP; Provinciedecreet EVA; Bestuursdecreet openbaarheid,2026-04-21,1978,,1550751,,,active,{PDF},Local leftover EVAP map VL Arboretum — empty 70/73/60-61 / bruto 1.55m / pers 1.40m 19.5 VTE / cash JUMP 0.97m,Publish omzet+73+60/61 split + 1 VE payroll + cash 0.97m counterparties + provincie/gemeente subsidy share; do not keep leftover EVAP Arboretum as unpublished 1.55m botanic-garden shell,{SRC},strong,Vlaanderen>Provincies>Antwerpen>EVAP>ArboretumKalmthout>JR2025_L5,tick1460; assets 1321730 omzet empty diensten empty pers 1397239 pnl 80699 equity 989753 cash 971509 debt 331977 capex 78207 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT Kempens Landschap / Warande / De Schorre / PIH / TPA / POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / Zilvermeer / De Nekker / AGB Kalmthout / city Kalmthout",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Arboretum Kalmthout vzw JR2025 leftover provincial EVAP: empty 70/73/60-61 / bruto 1.55m / pers 1.40m 19.5 VTE / cash JUMP 0.97m / 1 VE,L5,local_budget_line,Vlaanderen>Provincies>Antwerpen>EVAP>ArboretumKalmthout>JR2025_L5,1397239,1321730,Leftover dual EVAP botanic-garden shell: assets 1.32m / equity 0.99m / bruto 1.55m / omzet empty / 73 empty / 60-61 empty / pers 1.40m 19.5 VTE / cash 0.97m JUMP / geldbeleg 0.09m DROP / debt 0.33m DROP / PnL +81k / 1 VE; do not treat 1.55m as TE-additive of 348bn,strong,{SRC},EVAP AK / provincie Antwerpen dual botanic garden,Local leftover EVAP map VL Arboretum — JR2025 official NBB WVV live; empty 70/73/60-61 + pers/cash FOI,Official NBB WVV 2026-08-19: bruto 1.55m / pers 1.40m 19.5 VTE / cash JUMP 0.97m / PnL +81k / 1 VE / omzet empty,6.4,5.5,3.0,6.2,Publish omzet+73+60/61 split + 1 VE payroll + cash 0.97m counterparties + provincie/gemeente subsidy share; do not keep leftover EVAP Arboretum as unpublished 1.55m botanic-garden shell,active,,tick1460; leftover EVAP after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Provincies>Antwerpen>EVAP>ArboretumKalmthout>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto 1550751 vs 1450728 + pers 1397239 19.5 VTE + 1 VE 2155696524 + cash 971509 JUMP vs 760222 + geldbeleg 86994 DROP vs 286994 + debt 331977 DROP vs 393813 + leveranciers 74904 DROP + MVA 175764 + capex 78207 + commissaris 7210 + provincie/gemeente subsidy share unpublished,Leftover EVAP Arboretum after leftover AGB/APB hunt: empty 70/73/60-61 / bruto 1.55m / pers 1.40m 19.5 VTE / cash JUMP 0.97m / 1 VE hides provincial botanic-garden vehicle,8,Arboretum Kalmthout vzw / provinciegriffier / Bestuursorgaan,openbaarheid@provincieantwerpen.be,Heuvel 8 2920 Kalmthout,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1460 leftover EVAP after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF now extracted (2831768 bytes 20p). FOI ready not sent. EVERY-10. NOT Kempens Landschap / Warande / De Schorre / PIH / TPA / POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / Zilvermeer / De Nekker / AGB Kalmthout / city Kalmthout. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep WVL Houtland 0866.482.291 still no JR. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024 HEAD 403. Puyenbroeck still no separate APB 2025 PDF.",
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
    if not last_s.startswith("rq_1460,"):
        raise SystemExit(f"expected last row rq_1460, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1460 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1460,Arboretum Kalmthout JR2025 leftover dual residual + progress,hole_fill,5,done,L5,evap_arbk,"
        "Completed: Arboretum Kalmthout vzw leftover EVAP of mined provincie Antwerpen + leftover of mined city Kalmthout after leftover AGB/APB hunt; KBO 0418.558.364 Actief; live JR2025 official NBB WVV VKT-VZW PDF (2831768 bytes 20p; deposit 2026-00103572; AV 21.04.2026; header 05.05.2026; pdfinfo 06.05.2026 UTC). PDF header Arboretum Kalmthout vzw / Heuvel 8 — NOT Hooibeekhoeve. Sourced euros assets 1321730 omzet empty diensten empty pers 1397239 19.5 VTE pnl 80699 equity 989753 cash 971509 debt 331977 capex 78207 dividend 0. FOI "
        f"{GAP} ready not sent. EVERY-10 progress refresh. Distinct from already-mined Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve.,"
        f"{GAP},2026-08-19T15:25:00Z,{TS},"
        "tick1460 Arboretum Kalmthout leftover EVAP residual + every-10; KBO 0418.558.364; live JR2025 official NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1461 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
    )
    spawn = (
        "rq_1461,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1460 done including Arboretum Kalmthout 1460 leftover EVAP live official NBB WVV + every-10 / Stichting Kempens Landschap 1459 leftover IGS/SON live official NBB WVV / APB Warande 1458 leftover APB live official BBC / APB De Schorre 1457 leftover APB live official BBC / APB PIH 1456 leftover APB live official BBC / APB TPA 1455 leftover APB live official BBC / APB POA 1454 leftover APB live official BBC / Crematorium Hasselt 1453 leftover 100pct Stad Hasselt daughter live NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 404 as of 1460). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck spotted unmined around 1453 — still no separate APB 2025 PDF as of 1460). Do NOT confuse with already-mined Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live (still no JR as of 1460). Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1460 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1460. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456.,,"
        f"{TS},{TS},"
        "spawned tick1460 after Arboretum Kalmthout leftover EVAP live official NBB WVV JR2025 + every-10; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1460=done + rq_1461 spawned; keep", last_line_start)

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
    Path("/tmp/tick1460_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1460 Arboretum Kalmthout leftover EVAP residual + every-10; KBO 0418.558.364; live JR2025 official NBB WVV PDF; sourced euros assets 1321730 omzet empty diensten empty pers 1397239 19.5 VTE pnl 80699 equity 989753 cash 971509 debt 331977 capex 78207 dividend 0; FOI ready empty 70 / empty 73 / empty 60-61 / pers 1.40m 19.5 VTE / cash JUMP 0.97m / geldbeleg DROP 0.09m / 1 VE; NOT Kempens Landschap / Warande / De Schorre / PIH / TPA / POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / Zilvermeer / De Nekker / AGB Kalmthout / city Kalmthout; next rq_1461 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1460,1460,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1460")

    entry = (
        "\n## Tick 1460 - 2026-08-19 - rq_1460 Arboretum Kalmthout dual residual leftover + every-10\n"
        "- Unit: Arboretum Kalmthout vzw / EVAP AK (leftover provincial EVAP of mined provincie Antwerpen + leftover of mined city Kalmthout; 1 VE 2.155.696.524) after residual dual hunt (KBO **0418.558.364**; official NBB WVV VKT-VZW PDF **2831768** bytes / 20p; deposit **2026-00103572**; AV **21.04.2026**; header **05.05.2026**; pdfinfo created **06.05.2026 UTC**; model **VKT-VZW** 25.0.11 m04-f; commissaris Callens Vandelanotte B00003 / 0427.897.088 / Snoeks Ken A02189 fee **7210**; VKT-VZW 6.1.1/6.3/6.5/8 not filed; 6.1.2 MVA + 6.1.3 FVA + 6.2 fondsen + 6.4 + 6.6 + 6.7 sociale balans + 6.8 waarderingsregels + 7 jaarverslag image filed). Leftover AGB/APB first: leftover APB Inovant / Atlas koepelsite `jaarrekening_25_inov` / `jaarrekening_25_atlas` HEAD **404** on 2026-05-28 and 2026-06-25 with Googlebot UA this tick (Foleon leftover slugs have redirected to Hooibeekhoeve — no fetchable 2025 PDF; PDF header would have to be Inovant/Atlas not Hooibeekhoeve). AGB Bornem 0877.556.624 last JR still 2024 (2026pdf 2026-00553588 HEAD 403 this tick); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; Zwevegem/Rotselaar/Oudsbergen/MAC already mined. Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick. Leftover Bosgroep WVL Houtland 0866.482.291 still no jaarrekening (SBM jaarrekeninganalyse niet beschikbaar). Leftover IGS IVAREM 0267.403.264 last JR still 2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover EVAP Arboretum Kalmthout statutory CDN `2026-00103572` live this tick (HTTP 200 / application/pdf / 2831768 / 20p; jaar **2025-12-31**; neerlegging **05.05.2026**) — taken (hunt order #1 leftover EVA of mined provincie / mined city with live 2025 statutory PDF after leftover AGB/APB hunt). PDF header **Arboretum Kalmthout vzw / Heuvel (Dp) 8 / 2920 Kalmthout** — NOT a Foleon leftover-slug redirect to Hooibeekhoeve. Distinct from already-mined **Stichting Kempens Landschap 1459** / **APB Warande 1458** / **APB De Schorre 1457** / **APB PIH 1456** / **APB TPA 1455** / **APB POA 1454** / **APB PSES** / **GKC** / **Havencentrum** / **Kamp C** / **Hooibeekhoeve** / **Zilvermeer** / **De Nekker** / **AGB Kalmthout** / **city Kalmthout** / **EVA Pluimveehouderij**. First confirmed not already extracted as JR2025 euros: no Arboretum Kalmthout / 0418.558.364 JR2025 extract in entities/sources/leaderboard (0 KBO hits; city_kalmthout and agb_kalmthout are different entities). KBO Actief / normale toestand since **06.06.1978**; statutaire naam Arboretum Kalmthout vzw since 23.05.2023; afkorting EVAP AK since 18.12.2012; VZW since 06.06.1978; zetel Heuvel (Dp) 8 2920 Kalmthout; **1 VE 2.155.696.524** since 23.08.2006; 13 functiehouders; bestuurder provincie Antwerpen 0207.725.597 since 28.12.2012; Werkgever RSZ since 01.10.1978; btw since 01.03.2003; aanbestedende overheid; NACE RSZ 91.420; site https://www.arboretumkalmthout.be/. Waarderingsregels: EVAP follows provincie Antwerpen except specified. Prior-year figures **identiek**. NBB consult skipped (403/SPA); SBM HTML IP-blacklisted from box curl; WebFetch NBB consult yielded deposit id only. Euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb/Busibee euros not used. **EVERY-10 this tick** (progress_every_10_ticks.md + doge_waste_top10_current.md).\n"
        "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 **1397239** / **19,5 VTE** vs 1300962 / 19,7): assets **1321730** (was 1302867); fixed **176014** vs 161839 / IVA empty / MVA **175764** vs 161589 (terreinen/gebouwen **68513**; installaties **105806**; meubilair **1445**) / FVA **250**; current **1145716** vs 1141028; voorraden **41027** vs 53605; ST recv **34441** vs 33022 (trade **27110** / other **7331**); geldbeleg **86994 DROP** vs 286994; cash **971509 JUMP** vs 760222; prepaid **11745** vs 7185; equity **989753** vs 909054 (fondsen **346238**; bestemde **562816**; overgedragen **80699**; kapsubs empty); voorzieningen empty; schulden **331977 DROP** vs 393813 (LT empty; ST **268325** vs 332867 waarvan leveranciers **74904 DROP** vs 106011 + tax **42471** + bezold **150950**; deferred **63652** vs 60946); brutomarge **1550751** vs 1450728; omzet empty; 73 empty; 60/61 empty; pers **1397239** / **19,5 VTE** / 31194 uur / YE **19,6**; afschr **64032**; andere **5111**; expl **+84369** vs +85997; fin opbr **5255**; fin kosten **8925**; tax empty; PnL **+80699** vs +83009; dividend **0**; over te dragen **80699**; capex **78207** (MVA aanschaf; overdrachten 30680). Commissaris fee **7210**. Cross-checks: 176014+1145716=1321730; 989753+331977=1321730; 175764+250=176014; 41027+34441+86994+971509+11745=1145716; 346238+562816+80699=989753; 268325+63652=331977; 1550751-1397239-64032-5111=84369; 84369+5255-8925=80699; 1068276-892512=175764.\n"
        f"- CSVs: sources +4; entities +1 `evap_arbk` parent `prov_antwerpen`; budgets +40 executed; commitments +1 envelope 1550751 AV 21.04.2026; leaderboard +1 annual 1397239 / total 1321730; foi_queue +1 status=ready never sent; research_queue surgical rq_1460=done + rq_1461 spawn; loop_state ticks_completed=1460. Inventory after write: budgets {inv['budgets.csv']} · commitments {inv['commitments.csv']} · leaderboard {inv['leaderboard.csv']} · entities {inv['entities.csv']} · sources {inv['sources.csv']} · FOI ready {foi_ready} / answered {foi_ans} / partial {foi_part} / total {foi_tot}.\n"
        "- FOI: `gap_arbk_omzet_empty_bruto_1_55m_pers_1_40m_l5` ready not sent — empty 70 / empty 73 / empty 60-61 / pers 1.40m 19.5 VTE / 1 VE / cash JUMP 0.97m / geldbeleg DROP 0.09m / debt DROP 0.33m / MVA 0.18m / capex 78k / commissaris 7.2k / provincie-gemeente subsidy share unpublished.\n"
        "- EVERY-10: refreshed progress_every_10_ticks.md + doge_waste_top10_current.md from on-disk CSVs. Dual NEW since 1450: RL Houtland 1.21m · CoLimBo 0.91m · Crematorium Hasselt 1.86m · APB POA 27.38m · APB TPA 2.04m · APB PIH 3.88m · APB De Schorre 2.88m · APB Warande 4.60m · Kempens Landschap 82.17m · **Arboretum Kalmthout 1.32m**. Waste top10 stable (GIP #1; fossil/cars/cheque/reporté #2–10). TE denom €347.956 bn. Not TE-additive of ~348bn. Double-count vs Fluvius EG possible on DSO holdings.\n"
        "- Next: rq_1461 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 404 this tick (Foleon leftover slugs have redirected to Hooibeekhoeve) — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck spotted unmined around 1453 — still no separate APB 2025 PDF as of 1460). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live (still no JR as of 1460). Leftover IGS IVAREM **0267.403.264** still JR2024. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Arboretum Kalmthout 1460 / Stichting Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456.\n"
    )
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1460 -" in lraw:
        raise SystemExit("loop_log already has tick 1460 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1460")
    print("DONE tick 1460")

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

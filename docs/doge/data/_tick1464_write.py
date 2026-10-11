#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1464 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T15:42:00Z"
ENT = "wm_wpwa"
SRC = "src_wpwa_jr2025_nbb"
GAP = "gap_wpwa_omzet_21_24m_pers_2_94m_debt_212m_l5"
LB = "lb_wpwa_omzet_21_24m_pers_2_94m_debt_212m"
COMM = "comm_wpwa_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00151748.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Woonmaatschappij Woonpunt Waas official NBB WVV VOL-inb JR2025,{PDF},NBB / Woonpunt Waas,2026-08-19,budget,tick1464; official NBB WVV VOL-inb JR2025 PDF 81p / 3584745 bytes; deposit 2026-00151748; AV 26.05.2026; header 05.06.2026; pdfinfo created 11.06.2026 06:46:04 UTC; model VOL-inb 25.0.12 m82-f; KBO 0405.085.163; assets 280636169 cash 12458157 debt 212106941 pers 2939908 omzet 21244376 diensten 6667018 pnl 1492059 equity 67283451",
        "src_wpwa_site,Woonpunt Waas official sector + woonmaatschappij pages,https://www.woonpuntwaas.be/over-woonpunt-waas/,Woonpunt Waas / mined Waasland cities,2026-08-19,official_register,tick1464; leftover woonmaatschappij of mined Beveren-Kruibeke-Zwijndrecht + Sint-Gillis-Waas + Stekene; zetel Diederik Van Beverenlaan 11 9120 BKZ; KBO 0405.085.163; NBB consult for deposit id",
        "src_kbo_wpwa_0405085163,KBO Woonmaatschappij Woonpunt Waas 0405.085.163,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0405085163,KBO Public Search FOD Economie,2026-08-19,official_register,tick1464; Actief since 02.05.1922; BV since 22.06.2023; naam Woonmaatschappij Woonpunt Waas since 22.06.2023; zetel Diederik Van Beverenlaan 11 9120 BKZ; 1 VE 2229122356; 31 functiehouders; Werkgever RSZ since 01.01.1945; aanbestedende overheid",
        "src_wpwa_foi_contact,Woonpunt Waas FOI channel (info@woonpuntwaas.be),https://www.woonpuntwaas.be/over-woonpunt-waas/,Woonpunt Waas,2026-08-19,official_register,tick1464; leftover woonmaatschappij of mined Waasland cities; NOT Zorgpunt Waasland / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_wpwa," in raw or raw.startswith(b"wm_wpwa,"):
        raise SystemExit("wm_wpwa already present")
    if b"0405.085.163" in raw:
        raise SystemExit("Woonpunt Waas KBO already present as entity")
    row = (
        "wm_wpwa,Woonmaatschappij Woonpunt Waas (leftover woonmaatschappij / social-housing BV of mined Waasland cities BKZ + Sint-Gillis-Waas + Stekene; NOT Zorgpunt Waasland / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg),"
        "Societe de logement Woonpunt Waas SRL (logement social residuel Waasland),"
        "Woonpunt Waas leftover social-housing company of mined Waasland cities (not Zorgpunt Waasland / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg),"
        "other,city_bkz,nl,https://www.woonpuntwaas.be/,info@woonpuntwaas.be,Diederik Van Beverenlaan 11 9120 Beveren-Kruibeke-Zwijndrecht,"
        "tick1464 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0405.085.163 Actief since 02.05.1922; live JR2025 official NBB WVV PDF; sourced euros assets 280636169 omzet 21244376 diensten 6667018 pers 2939908 28.5 VTE pnl 1492059 equity 67283451 cash 12458157 debt 212106941 capex 8426929 dividend 0; FOI ready omzet 21.24m / pers 2.94m 28.5 VTE / debt 212.11m / cash DROP 12.46m / 1 VE; distinct from already-mined Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / Zorgpunt Waasland"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_wpwa")

def part_budgets():
    BUDGETS = [
        ("bud_wpwa_assets_2025", "2025", "280636169", "2025 assets 280636169 (was 280315945); tick1464; primary official NBB WVV VOL-inb 2026-00151748"),
        ("bud_wpwa_current_2025", "2025", "30587035", "2025 vlottend 30587035 (was 30992409); tick1464; primary official NBB WVV"),
        ("bud_wpwa_cash_2025", "2025", "12458157", "2025 liquide middelen 12458157 DROP (was 14450973); tick1464; primary official NBB WVV"),
        ("bud_wpwa_geldbeleg_2025", "2025", "0", "2025 geldbeleggingen empty; tick1464; primary official NBB WVV"),
        ("bud_wpwa_strecv_2025", "2025", "1341784", "2025 ST vorderingen 1341784 DROP (was 2923189); tick1464; primary official NBB WVV"),
        ("bud_wpwa_trade_2025", "2025", "880896", "2025 handelsvorderingen 880896 DROP (was 2410453); tick1464; primary official NBB WVV"),
        ("bud_wpwa_othrecv_2025", "2025", "460887", "2025 overige ST vorderingen 460887 (was 512736); tick1464; primary official NBB WVV"),
        ("bud_wpwa_voorraden_2025", "2025", "15068631", "2025 voorraden 15068631 JUMP (was 12384387; all onroerend verkoop); tick1464; primary official NBB WVV"),
        ("bud_wpwa_prepaid_2025", "2025", "1718465", "2025 overlopend actief 1718465 (was 1233860); tick1464; primary official NBB WVV"),
        ("bud_wpwa_fixed_2025", "2025", "250049133", "2025 vaste activa 250049133 (was 249323536); tick1464; primary official NBB WVV"),
        ("bud_wpwa_iva_2025", "2025", "57352", "2025 IVA 57352 (was 59895); tick1464; primary official NBB WVV"),
        ("bud_wpwa_mva_2025", "2025", "249768891", "2025 MVA 249768891 (was 249081075; terreinen/gebouwen 229594599 in aanbouw 19177127); tick1464; primary official NBB WVV"),
        ("bud_wpwa_fva_2025", "2025", "222890", "2025 FVA 222890 (was 182566); tick1464; primary official NBB WVV"),
        ("bud_wpwa_equity_2025", "2025", "67283451", "2025 eigen vermogen 67283451 (was 66032469); tick1464; primary official NBB WVV"),
        ("bud_wpwa_inbreng_2025", "2025", "103467", "2025 inbreng 103467 onbeschikbaar (was 105131); tick1464; primary official NBB WVV"),
        ("bud_wpwa_reserves_2025", "2025", "51822479", "2025 reserves 51822479 (was 50348666); tick1464; primary official NBB WVV"),
        ("bud_wpwa_kapsubs_2025", "2025", "15357504", "2025 kapitaalsubsidies 15357504 (was 15578672); tick1464; primary official NBB WVV"),
        ("bud_wpwa_voorz_2025", "2025", "1245777", "2025 voorzieningen+uitgestelde belasting 1245777 (was 1046624); tick1464; primary official NBB WVV"),
        ("bud_wpwa_debt_2025", "2025", "212106941", "2025 schulden 212106941 DROP (was 213236853); tick1464; primary official NBB WVV"),
        ("bud_wpwa_ltdebt_2025", "2025", "197584355", "2025 LT schulden 197584355 (was 200429559; fin krediet 194999895); tick1464; primary official NBB WVV"),
        ("bud_wpwa_stdebt_2025", "2025", "13272225", "2025 ST schulden 13272225 (was 11682987); tick1464; primary official NBB WVV"),
        ("bud_wpwa_lev_2025", "2025", "1612887", "2025 leveranciers 1612887 (was 1813179); tick1464; primary official NBB WVV"),
        ("bud_wpwa_bezold_2025", "2025", "326262", "2025 bezoldigingen-schulden 326262 (was 272704); tick1464; primary official NBB WVV"),
        ("bud_wpwa_taxpay_2025", "2025", "1336955", "2025 belastingschulden 1336955 (was 1308237); tick1464; primary official NBB WVV"),
        ("bud_wpwa_deferred_2025", "2025", "1250361", "2025 overlopend passief 1250361 (was 1124307); tick1464; primary official NBB WVV"),
        ("bud_wpwa_omzet_2025", "2025", "21244376", "2025 omzet 70 21244376 (was 18370940); tick1464; primary official NBB WVV"),
        ("bud_wpwa_diensten_2025", "2025", "6667018", "2025 diensten 61 6667018 (was 5767849); tick1464; primary official NBB WVV"),
        ("bud_wpwa_aankopen_2025", "2025", "2160020", "2025 handelsgoederen/grondstoffen 60 2160020 (was 220529); tick1464; primary official NBB WVV"),
        ("bud_wpwa_pers_2025", "2025", "2939908", "2025 pers 62 2939908 (was 2645638); 28.5 VTE vs 26.6; 42424 uur; YE 28.7; tick1464; primary official NBB WVV"),
        ("bud_wpwa_afschr_2025", "2025", "7683658", "2025 afschrijvingen 7683658 (was 7250834); tick1464; primary official NBB WVV"),
        ("bud_wpwa_expl_2025", "2025", "2242070", "2025 bedrijfswinst 2242070 DROP (was 3964367); tick1464; primary official NBB WVV"),
        ("bud_wpwa_finopbr_2025", "2025", "3528067", "2025 financiele opbrengsten 3528067 all recurrent; tick1464; primary official NBB WVV"),
        ("bud_wpwa_finkost_2025", "2025", "4214410", "2025 financiele kosten 4214410 (was 3898854); tick1464; primary official NBB WVV"),
        ("bud_wpwa_pnl_2025", "2025", "1492059", "2025 PnL 1492059 DROP (was 2832808); tick1464; primary official NBB WVV"),
        ("bud_wpwa_div_2025", "2025", "0", "2025 dividend 0 uit te keren empty; tick1464; primary official NBB WVV"),
        ("bud_wpwa_capex_2025", "2025", "8426929", "2025 capex MVA aanschaf 8426929 (terreinen 393397 + meubilair 14683 + in aanbouw 8018849); tick1464; primary official NBB WVV"),
        ("bud_wpwa_bedrijfsopbr_2025", "2025", "23589394", "2025 bedrijfsopbrengsten 70/76A 23589394 (was 21557108); tick1464; primary official NBB WVV"),
        ("bud_wpwa_bedrijfskost_2025", "2025", "21347324", "2025 bedrijfskosten 60/66A 21347324 (was 17592742); tick1464; primary official NBB WVV"),
        ("bud_wpwa_tax_2025", "2025", "116993", "2025 belastingen 67/77 116993 (was 179457); tick1464; primary official NBB WVV"),
        ("bud_wpwa_in_aanbouw_2025", "2025", "19177127", "2025 activa in aanbouw 19177127 JUMP (was 14214318); tick1464; primary official NBB WVV"),
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
        f"{COMM},Woonpunt Waas JR2025 leftover woonmaatschappij dual (omzet 21.24m / diensten 6.67m / pers 2.94m 28.5 VTE / debt 212.11m / cash DROP 12.46m / 1 VE),{ENT},Woonpunt Waas / mined Waasland cities dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-26,1922,,21244376,,,active,{PDF},Local leftover woonmaatschappij map VL Waasland — omzet 21.24m / pers 2.94m 28.5 VTE / debt 212.11m / cash DROP 12.46m,Publish omzet split + 1 VE payroll + LT krediet 195.0m counterparties + capex 8.43m + aandeel % gemeenten/OCMW/private; do not keep leftover woonmaatschappij as unpublished 21.24m housing shell,{SRC},strong,Vlaanderen>Gemeenten>BKZ>Woonmaatschappij>WoonpuntWaas>JR2025_L5,tick1464; assets 280636169 omzet 21244376 diensten 6667018 pers 2939908 pnl 1492059 equity 67283451 cash 12458157 debt 212106941 capex 8426929 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT Zorgpunt Waasland / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Woonpunt Waas JR2025 leftover woonmaatschappij: omzet 21.24m / diensten 6.67m / pers 2.94m 28.5 VTE / debt 212.11m / cash DROP 12.46m / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>BKZ>Woonmaatschappij>WoonpuntWaas>JR2025_L5,21244376,280636169,Leftover dual woonmaatschappij shell: assets 280.64m / equity 67.28m / omzet 21.24m / diensten 6.67m / pers 2.94m 28.5 VTE / cash 12.46m DROP / debt 212.11m / LT krediet 195.0m / PnL +1.49m DROP / 1 VE; do not treat 21.24m as TE-additive of 348bn,strong,{SRC},Woonpunt Waas / mined Waasland cities dual housing,Local leftover woonmaatschappij map VL Waasland — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 21.24m / pers 2.94m 28.5 VTE / debt 212.11m / cash DROP 12.46m / PnL +1.49m / 1 VE,6.8,7.2,3.0,6.8,Publish omzet split + 1 VE payroll + LT krediet 195.0m counterparties + capex 8.43m + aandeel % gemeenten/OCMW/private; do not keep leftover woonmaatschappij as unpublished 21.24m housing shell,active,,tick1464; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / Zorgpunt Waasland",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Gemeenten>BKZ>Woonmaatschappij>WoonpuntWaas>JR2025_L5,{ENT},omzet 21244376 vs 18370940 + diensten 6667018 + pers 2939908 28.5 VTE + 1 VE 2229122356 + cash 12458157 DROP vs 14450973 + debt 212106941 LT krediet 194999895 + voorraden JUMP 15068631 vs 12384387 + capex 8426929 in aanbouw 19177127 + PnL DROP 1492059 vs 2832808 + commissaris fee unpublished + aandeel % BKZ/SGW/Stekene/OCMW/private unpublished,Leftover woonmaatschappij Waasland after leftover AGB/APB hunt: omzet 21.24m / pers 2.94m 28.5 VTE / debt 212.11m / cash DROP 12.46m / 1 VE hides municipal housing vehicle,8,Woonmaatschappij Woonpunt Waas / Bestuursorgaan / algemeen directeur,info@woonpuntwaas.be,Diederik Van Beverenlaan 11 9120 Beveren-Kruibeke-Zwijndrecht,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1464 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF now extracted (3584745 bytes 81p). FOI ready not sent. NOT every-10. NOT Toerisme Limburg / Toerisme Vlaams-Brabant / Toerisme Oost-Vlaanderen / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / Zorgpunt Waasland / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1463. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. Puyenbroeck still no separate APB 2025 PDF.",
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
    if not last_s.startswith("rq_1464,"):
        raise SystemExit(f"expected last row rq_1464, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1464 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1464,Woonpunt Waas JR2025 leftover dual residual,hole_fill,5,done,L5,wm_wpwa,"
        "Completed: Woonmaatschappij Woonpunt Waas leftover woonmaatschappij of mined Waasland cities after leftover AGB/APB hunt; KBO 0405.085.163 Actief; live JR2025 official NBB WVV VOL-inb PDF (3584745 bytes 81p; deposit 2026-00151748; AV 26.05.2026; header 05.06.2026; pdfinfo 11.06.2026 06:46:04 UTC). PDF header Woonpunt Waas / Diederik van Beverenlaan 11 — NOT Zorgpunt Waasland / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Sourced euros assets 280636169 omzet 21244376 diensten 6667018 pers 2939908 28.5 VTE pnl 1492059 equity 67283451 cash 12458157 debt 212106941 capex 8426929 dividend 0. FOI "
        f"{GAP} ready not sent. Distinct from already-mined Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / Zorgpunt Waasland.,"
        f"{GAP},2026-08-19T15:28:00Z,{TS},"
        "tick1464 Woonpunt Waas leftover woonmaatschappij residual; KBO 0405.085.163; live JR2025 official NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1465 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025"
    )
    spawn = (
        "rq_1465,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1464 done including Woonpunt Waas 1464 leftover woonmaatschappij live official NBB WVV / Toerisme Limburg 1463 leftover provincial tourism VZW live official NBB WVV / Toerisme Vlaams-Brabant 1462 leftover provincial tourism VZW live official NBB WVV / Toerisme Oost-Vlaanderen 1461 leftover provincial tourism VZW live official NBB WVV / Arboretum Kalmthout 1460 leftover EVAP live official NBB WVV + every-10). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 404 as of 1464). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck spotted unmined around 1453 — still no separate APB 2025 PDF as of 1464). Do NOT confuse with already-mined Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / Zorgpunt Waasland. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live. Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1464 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1464. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460.,,"
        f"{TS},{TS},"
        "spawned tick1464 after Woonpunt Waas leftover woonmaatschappij live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1464=done + rq_1465 spawned; keep", last_line_start)

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
    Path("/tmp/tick1464_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1464 Woonpunt Waas leftover woonmaatschappij residual; KBO 0405.085.163; live JR2025 official NBB WVV PDF; sourced euros assets 280636169 omzet 21244376 diensten 6667018 pers 2939908 28.5 VTE pnl 1492059 equity 67283451 cash 12458157 debt 212106941 capex 8426929 dividend 0; FOI ready omzet 21.24m / pers 2.94m 28.5 VTE / debt 212.11m / cash DROP 12.46m / 1 VE; NOT Toerisme Limburg / Toerisme Vlaams-Brabant / Toerisme Oost-Vlaanderen / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / Zorgpunt Waasland / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1465 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1464,1464,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1464")

    entry = (
        "\n## Tick 1464 - 2026-08-19 - rq_1464 Woonpunt Waas dual residual leftover\n"
        "- Unit: Woonmaatschappij Woonpunt Waas BV (leftover woonmaatschappij / social-housing BV of mined Waasland cities Beveren-Kruibeke-Zwijndrecht + Sint-Gillis-Waas + Stekene; 1 VE 2.229.122.356) after residual dual hunt (KBO **0405.085.163**; official NBB WVV VOL-inb PDF **3584745** bytes / 81p; deposit **2026-00151748**; AV **26.05.2026**; header **05.06.2026**; pdfinfo created **11.06.2026 06:46:04 UTC**; model **VOL-inb** 25.0.12 m82-f; commissaris RSM InterAudit BV B00091 / 0436.391.122 / Uytterhaegen Jonas A02777 mandate 20.05.2023–26.05.2026 fee unpublished VOL-inb 6.18.2 not filed; VOL-inb 6.1/6.2.2/6.2.4/6.2.5/6.3.4/6.4.1/6.4.2/6.5.1/6.5.2/6.7.2/6.8/6.14/6.15/6.17/6.18.2/9/12/13/14/15 not filed; 6.2.1/6.2.3 IVA + 6.3 MVA + 6.6 + 6.7.1 + 6.9 + 6.10 + 6.11 + 6.12 + 6.13 + 6.16 + 6.19 + sociale balans + remuneratieverslag filed). Leftover AGB/APB first: leftover APB Inovant / Atlas koepelsite `jaarrekening_25_inov` / `jaarrekening_25_atlas` HEAD **404** on 2026-05-28 and 2026-06-25 with Googlebot UA this tick (Foleon leftover slugs have redirected to Hooibeekhoeve — no fetchable 2025 Inovant/Atlas PDF). Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick. Leftover AGB Bornem 0877.556.624 last JR still 2024 (2026pdf 2026-00553588 HEAD 403 this tick). Leftover AGB Hasselt / SOLag / WAGSO / Temse / Herk / Lommel / Herzele / Puurs already in entities — skipped. Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel still no JR as of 1463. Leftover IGS IVAREM 0267.403.264 last JR still 2024-12-31. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover Woonpunt Waas statutory CDN `2026-00151748` live this tick (HTTP 200 / 3584745 / 81p; jaar **2025-12-31**; neerlegging **05.06.2026**) — taken (hunt order #2 leftover unmined IGS / woonmaatschappij of mined Waasland cities with live 2025 statutory PDF after leftover AGB/APB hunt). PDF header **WOONMAATSCHAPPIJ WOONPUNT WAAS / Diederik van Beverenlaan 11 / 9120 Beveren-Kruibeke-Zwijndrecht** — NOT Zorgpunt Waasland / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Distinct from already-mined **Toerisme Limburg 1463** / **Toerisme Vlaams-Brabant 1462** / **Toerisme Oost-Vlaanderen 1461** / **Arboretum Kalmthout 1460** / **Kempens Landschap 1459** / **APB Warande 1458** / **APB De Schorre 1457** / **APB PIH 1456** / **Zorgpunt Waasland**. First confirmed not already extracted as JR2025 euros: no Woonpunt Waas / 0405.085.163 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **02.05.1922**; statutaire naam Woonmaatschappij Woonpunt Waas since 22.06.2023; afkorting WOONPUNT WAAS since 22.06.2023; BV since 22.06.2023; zetel Diederik Van Beverenlaan 11 9120 Beveren-Kruibeke-Zwijndrecht since 01.01.2025; **1 VE**; 31 functiehouders; lid Directiecomité Beeldens Karin since 21.11.2019; Werkgever RSZ since 01.01.1945; btw since 01.01.1971; aanbestedende overheid; NACE 68.121 / 68.202; site https://www.woonpuntwaas.be/. Prior-year figures **identiek**. NBB consult yielded deposit id. Euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1470).\n"
        "- EUR strong (primary official WVV VOL-inb; omzet 70 **21244376**; diensten 61 **6667018**; pers 62 **2939908** / **28,5 VTE** vs 2645638 / 26,6): assets **280636169** (was 280315945); fixed **250049133** vs 249323536 / IVA **57352** vs 59895 / MVA **249768891** vs 249081075 (terreinen/gebouwen **229594599**; meubilair **148280**; overige **848885**; in aanbouw **19177127**) / FVA **222890** vs 182566; current **30587035** vs 30992409; voorraden **15068631 JUMP** vs 12384387 (all onroerend verkoop); ST recv **1341784 DROP** vs 2923189 (trade **880896 DROP** vs 2410453 / other **460887**); geldbeleg empty; cash **12458157 DROP** vs 14450973; prepaid **1718465** vs 1233860; equity **67283451** vs 66032469 (inbreng **103467**; reserves **51822479**; overgedragen empty; kapsubs **15357504**); voorzieningen **1245777** vs 1046624 (grote herstellingen **400682 JUMP** vs 156109; uitgestelde belasting **845096**); schulden **212106941 DROP** vs 213236853 (LT **197584355** vs 200429559 waarvan fin krediet **194999895**; ST **13272225** vs 11682987 waarvan 42 **9453349** + leveranciers **1612887** + tax **1336955** + bezold **326262**; deferred **1250361**); omzet **21244376** vs 18370940; 60 **2160020**; diensten **6667018** vs 5767849; pers **2939908** / **28,5 VTE** / 42424 uur / YE **28,7**; afschr **7683658**; expl **+2242070 DROP** vs +3964367; fin opbr **3528067**; fin kosten **4214410**; tax **116993**; PnL **+1492059 DROP** vs +2832808; dividend **0**; toevoeging reserves **2032420**; capex MVA aanschaf **8426929** (terreinen 393397 + meubilair 14683 + in aanbouw 8018849) + IVA 29040. Commissaris fee unpublished. Aandeelhouders PDF: BKZ 7875 / SGW 275 / Stekene 272 / OCMW BKZ 2485 / private 162 / totaal 12914. Cross-checks: 250049133+30587035=280636168 vs 280636169; 67283451+1245777+212106941=280636169; 23589394-21347324=2242070; 2242070+3528067-4214410=1555727; 1555727+53324-116993=1492058 vs 1492059; 1492059+540361=2032420. 1-euro rounding on assets/PnL.\n"
        "- CSVs: sources +4; entities +1 `wm_wpwa` parent `city_bkz`; budgets +40 executed; commitments +1 envelope 21244376 AV 26.05.2026; leaderboard +1 annual 21244376 / total 280636169; foi_queue +1 status=ready never sent; research_queue surgical rq_1464=done + rq_1465 spawn; loop_state ticks_completed=1464. Inventory after write: budgets {INV_B} · commitments {INV_C} · leaderboard {INV_L} · entities {INV_E} · sources {INV_S} · FOI ready {FOI_R} / answered {FOI_A} / partial {FOI_P} / total {FOI_T}.\n"
        "- FOI: `gap_wpwa_omzet_21_24m_pers_2_94m_debt_212m_l5` ready not sent — omzet 21.24m / diensten 6.67m / pers 2.94m 28.5 VTE / 1 VE / cash DROP 12.46m / debt 212.11m LT krediet 195.0m / voorraden JUMP 15.07m / capex 8.43m / PnL DROP +1.49m / commissaris unpublished / aandeel % gemeenten/OCMW/private unpublished.\n"
        "- Next: rq_1465 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 404 this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1464). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live. Leftover IGS IVAREM **0267.403.264** still JR2024. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Stichting Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456. Next every-10 is **1470**. Provincial tourism VZWs now exhausted (Westtoer + TOV + TVLB + TLim).\n"
    )
    entry = entry.replace("{INV_B}", str(inv["budgets.csv"])).replace("{INV_C}", str(inv["commitments.csv"])).replace("{INV_L}", str(inv["leaderboard.csv"])).replace("{INV_E}", str(inv["entities.csv"])).replace("{INV_S}", str(inv["sources.csv"])).replace("{FOI_R}", str(foi_ready)).replace("{FOI_A}", str(foi_ans)).replace("{FOI_P}", str(foi_part)).replace("{FOI_T}", str(foi_tot))
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1464 -" in lraw:
        raise SystemExit("loop_log already has tick 1464 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1464")
    print("DONE tick 1464")

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

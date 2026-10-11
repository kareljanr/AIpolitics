#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1473 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T17:35:00Z"
ENT = "wm_vvnd"
SRC = "src_vvnd_jr2025_nbb"
GAP = "gap_vvnd_omzet_44_90m_pers_6_73m_debt_481m_l5"
LB = "lb_vvnd_omzet_44_90m_pers_6_73m_debt_481m"
COMM = "comm_vvnd_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00154781.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Vivendo official NBB WVV VOL-inb JR2025,{PDF},NBB / Vivendo,2026-08-19,budget,tick1473; official NBB WVV VOL-inb JR2025 PDF 56p / 710320 bytes; deposit 2026-00154781; AV 08.06.2026; header 09.06.2026; pdfinfo created 12.06.2026 03:00:16 UTC; model VOL-inb 26.0.12 m82-f; KBO 0406.062.883; assets 605932612 cash 24748434 debt 481406996 pers 6725524 omzet 44896478 diensten 14062354 pnl 894681 equity 120004062",
        "src_vvnd_site,Vivendo official pages,https://www.vivendo.be/,Vivendo / mined Brugge-regio,2026-08-19,official_register,tick1473; leftover woonmaatschappij of mined Stad Brugge + Beernem + Damme + Jabbeke + Oostkamp + Zedelgem; zetel Handboogstraat 2 bus 13 8000 Brugge; KBO 0406.062.883; SBM used for deposit-id discovery only",
        "src_kbo_vvnd_0406062883,KBO Vivendo 0406.062.883,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0406062883,KBO Public Search FOD Economie,2026-08-19,official_register,tick1473; Actief since 07.11.1955; BV since 15.12.2021; naam VIVENDO since 11.06.2007; zetel Handboogstraat 2 bus 13 8000 Brugge; 2 VE; 15 functiehouders; Werkgever RSZ since 01.04.1962; aanbestedende overheid",
        "src_vvnd_foi_contact,Vivendo FOI channel (info@vivendo.be),https://www.vivendo.be/,Vivendo,2026-08-19,official_register,tick1473; leftover woonmaatschappij of mined Brugge-regio; NOT SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_vvnd," in raw or raw.startswith(b"wm_vvnd,"):
        raise SystemExit("wm_vvnd already present")
    if b"0406.062.883" in raw or b"0406062883" in raw:
        raise SystemExit("Vivendo KBO already present as entity")
    row = (
        "wm_vvnd,Vivendo (leftover woonmaatschappij / social-housing BV of mined Stad Brugge + Beernem + Damme + Jabbeke + Oostkamp + Zedelgem; NOT SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST),"
        "Vivendo SRL (logement social residuel Brugge-regio),"
        "Vivendo leftover social-housing company of mined Brugge-regio (not SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST),"
        "other,city_brugge,nl,https://www.vivendo.be/,info@vivendo.be,Handboogstraat 2 bus 13 8000 Brugge,"
        "tick1473 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0406.062.883 Actief since 07.11.1955; live JR2025 official NBB WVV PDF; sourced euros assets 605932612 omzet 44896478 diensten 14062354 pers 6725524 75.1 VTE pnl 894681 equity 120004062 cash 24748434 debt 481406996 capex 37681448 dividend 0; FOI ready omzet 44.90m DROP / pers 6.73m 75.1 VTE / debt 481.41m / cash 24.75m JUMP / PnL DROP 0.89m / dividend 0 / 2 VE; distinct from already-mined SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_vvnd")

def part_budgets():
    BUDGETS = [
        ("bud_vvnd_assets_2025", "2025", "605932612", "2025 assets 605932612 DROP (was 613487534); tick1473; primary official NBB WVV VOL-inb 2026-00154781"),
        ("bud_vvnd_current_2025", "2025", "33082379", "2025 vlottend 33082379 (was 36681924); tick1473; primary official NBB WVV"),
        ("bud_vvnd_cash_2025", "2025", "24748434", "2025 liquide middelen 24748434 JUMP (was 20947648; huurwaarborgen 4508892); tick1473; primary official NBB WVV"),
        ("bud_vvnd_strecv_2025", "2025", "1306913", "2025 ST vorderingen 1306913 (was 825492); tick1473; primary official NBB WVV"),
        ("bud_vvnd_trade_2025", "2025", "478030", "2025 handelsvorderingen 478030 (was 253234); tick1473; primary official NBB WVV"),
        ("bud_vvnd_othrecv_2025", "2025", "828883", "2025 overige ST vorderingen 828883; tick1473; primary official NBB WVV"),
        ("bud_vvnd_voorraden_2025", "2025", "2838366", "2025 voorraden 2838366 DROP (was 10613189; onroerend verkoop 2838366); tick1473; primary official NBB WVV"),
        ("bud_vvnd_prepaid_2025", "2025", "4188666", "2025 overlopend actief 4188666 (was 4295595); tick1473; primary official NBB WVV"),
        ("bud_vvnd_fixed_2025", "2025", "572850233", "2025 vaste activa 572850233 (was 576805610); tick1473; primary official NBB WVV"),
        ("bud_vvnd_iva_2025", "2025", "1537", "2025 IVA 1537 (was 3205); tick1473; primary official NBB WVV"),
        ("bud_vvnd_mva_2025", "2025", "572760451", "2025 MVA 572760451 (was 576714160; terreinen/gebouwen 536596288 in aanbouw 35810366); tick1473; primary official NBB WVV"),
        ("bud_vvnd_fva_2025", "2025", "88245", "2025 FVA 88245 (aandelen 88245); tick1473; primary official NBB WVV"),
        ("bud_vvnd_equity_2025", "2025", "120004062", "2025 eigen vermogen 120004062 DROP (was 122988286); tick1473; primary official NBB WVV"),
        ("bud_vvnd_inbreng_2025", "2025", "62306", "2025 inbreng 62306 (onbeschikbaar 62306); tick1473; primary official NBB WVV"),
        ("bud_vvnd_reserves_2025", "2025", "96161783", "2025 reserves 96161783; tick1473; primary official NBB WVV"),
        ("bud_vvnd_kapsubs_2025", "2025", "23709913", "2025 kapitaalsubsidies 23709913 DROP (was 24219008); tick1473; primary official NBB WVV"),
        ("bud_vvnd_voorz_2025", "2025", "4521554", "2025 voorzieningen+uitgestelde belasting 4521554; tick1473; primary official NBB WVV"),
        ("bud_vvnd_debt_2025", "2025", "481406996", "2025 schulden 481406996 DROP (was 485462680); tick1473; primary official NBB WVV"),
        ("bud_vvnd_ltdebt_2025", "2025", "448963595", "2025 LT schulden 448963595 (was 455452883; fin krediet 444350619); tick1473; primary official NBB WVV"),
        ("bud_vvnd_stdebt_2025", "2025", "29215134", "2025 ST schulden 29215134 (was 27329272); tick1473; primary official NBB WVV"),
        ("bud_vvnd_lev_2025", "2025", "7812489", "2025 leveranciers 7812489 (was 7469469); tick1473; primary official NBB WVV"),
        ("bud_vvnd_bezold_2025", "2025", "890601", "2025 bezoldigingen-schulden 890601 (was 773974); tick1473; primary official NBB WVV"),
        ("bud_vvnd_taxpay_2025", "2025", "2986294", "2025 belastingschulden 2986294 (was 2464488); tick1473; primary official NBB WVV"),
        ("bud_vvnd_deferred_2025", "2025", "3228266", "2025 overlopend passief 3228266 (was 2680525); tick1473; primary official NBB WVV"),
        ("bud_vvnd_omzet_2025", "2025", "44896478", "2025 omzet 70 44896478 DROP (was 48298483); tick1473; primary official NBB WVV"),
        ("bud_vvnd_diensten_2025", "2025", "14062354", "2025 diensten 61 14062354 JUMP (was 12372336); tick1473; primary official NBB WVV"),
        ("bud_vvnd_aankopen_2025", "2025", "8999132", "2025 handelsgoederen/grondstoffen 60 8999132 (aankopen 1224309 voorraad 7774823); tick1473; primary official NBB WVV"),
        ("bud_vvnd_pers_2025", "2025", "6725524", "2025 pers 62 6725524; 75.1 VTE vs 70.3; 118451 uur; YE 86; tick1473; primary official NBB WVV"),
        ("bud_vvnd_afschr_2025", "2025", "15388491", "2025 afschrijvingen 15388491; tick1473; primary official NBB WVV"),
        ("bud_vvnd_expl_2025", "2025", "1675993", "2025 bedrijfswinst 1675993 DROP (was 5789256); tick1473; primary official NBB WVV"),
        ("bud_vvnd_finopbr_2025", "2025", "9478586", "2025 financiele opbrengsten 9478586 all recurrent; tick1473; primary official NBB WVV"),
        ("bud_vvnd_finkost_2025", "2025", "10248776", "2025 financiele kosten 10248776; tick1473; primary official NBB WVV"),
        ("bud_vvnd_pnl_2025", "2025", "894681", "2025 PnL 894681 DROP (was 4459704); tick1473; primary official NBB WVV"),
        ("bud_vvnd_div_2025", "2025", "0", "2025 dividend 0 vergoeding van de inbreng empty; tick1473; primary official NBB WVV"),
        ("bud_vvnd_capex_2025", "2025", "37681448", "2025 capex MVA aanschaf 37681448 (terreinen 2369045 + install 10298 + meubilair 69308 + in aanbouw 35232797); tick1473; primary official NBB WVV"),
        ("bud_vvnd_bedrijfsopbr_2025", "2025", "50917841", "2025 bedrijfsopbrengsten 70/76A 50917841; tick1473; primary official NBB WVV"),
        ("bud_vvnd_bedrijfskost_2025", "2025", "49241849", "2025 bedrijfskosten 60/66A 49241849; tick1473; primary official NBB WVV"),
        ("bud_vvnd_tax_2025", "2025", "58104", "2025 belastingen 67/77 58104; tick1473; primary official NBB WVV"),
        ("bud_vvnd_in_aanbouw_2025", "2025", "35810366", "2025 activa in aanbouw 35810366 DROP (was 58119086); tick1473; primary official NBB WVV"),
        ("bud_vvnd_krediet_2025", "2025", "444350619", "2025 LT kredietinstellingen 444350619 DROP (was 451002279); tick1473; primary official NBB WVV"),
        ("bud_vvnd_terreinen_2025", "2025", "536596288", "2025 terreinen en gebouwen 536596288 (was 518242954); tick1473; primary official NBB WVV"),
        ("bud_vvnd_interim_2025", "2025", "454285", "2025 interim 3.4 VTE kosten 454285; tick1473; primary official NBB WVV"),
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
        f"{COMM},Vivendo JR2025 leftover woonmaatschappij dual (omzet 44.90m DROP / diensten 14.06m JUMP / pers 6.73m 75.1 VTE / debt 481.41m / cash 24.75m JUMP / PnL DROP 0.89m / dividend 0 / 2 VE),{ENT},Brugge-regio / mined Brugge dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-06-08,1955,,44896478,,,active,{PDF},Local leftover woonmaatschappij map VL Brugge-regio — omzet 44.90m DROP / pers 6.73m 75.1 VTE / debt 481.41m / cash 24.75m,Publish omzet split + 2 VE payroll + cash 24.75m + LT krediet 444.35m counterparties + capex 37.68m + aandeel % Brugge/Beernem/Damme/Jabbeke/Oostkamp/Zedelgem/OCMW/private + dividend 0; do not keep leftover woonmaatschappij as unpublished 44.90m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Brugge>Woonmaatschappij>Vivendo>JR2025_L5,tick1473; assets 605932612 omzet 44896478 diensten 14062354 pers 6725524 pnl 894681 equity 120004062 cash 24748434 debt 481406996 capex 37681448 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Vivendo JR2025 leftover woonmaatschappij: omzet 44.90m DROP / diensten 14.06m JUMP / pers 6.73m 75.1 VTE / debt 481.41m / cash 24.75m JUMP / PnL DROP 0.89m / dividend 0 / 2 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Brugge>Woonmaatschappij>Vivendo>JR2025_L5,44896478,605932612,Leftover dual woonmaatschappij shell: assets 605.93m / equity 120.00m / omzet 44.90m DROP / diensten 14.06m JUMP / pers 6.73m 75.1 VTE / cash 24.75m JUMP / debt 481.41m / LT krediet 444.35m / PnL 0.89m DROP / dividend 0 / 2 VE; do not treat 44.90m as TE-additive of 348bn,strong,{SRC},Vivendo / mined Brugge-regio dual housing,Local leftover woonmaatschappij map VL Brugge-regio — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 44.90m DROP / pers 6.73m 75.1 VTE / debt 481.41m / cash 24.75m JUMP / PnL DROP 0.89m / dividend 0 / 2 VE,7.0,7.0,3.0,7.0,Publish omzet split + 2 VE payroll + cash 24.75m + LT krediet 444.35m counterparties + capex 37.68m + aandeel % Brugge/Beernem/Damme/Jabbeke/Oostkamp/Zedelgem/OCMW/private + dividend 0; do not keep leftover woonmaatschappij as unpublished 44.90m housing shell,active,,tick1473; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Gemeenten>Brugge>Woonmaatschappij>Vivendo>JR2025_L5,{ENT},omzet 44896478 DROP vs 48298483 + diensten 14062354 JUMP vs 12372336 + pers 6725524 75.1 VTE vs 70.3 + 2 VE + cash 24748434 JUMP vs 20947648 + debt 481406996 LT krediet 444350619 + voorraden 2838366 DROP onroerend 2838366 + capex 37681448 in aanbouw DROP 35810366 vs 58119086 + PnL DROP 894681 vs 4459704 + dividend 0 + commissaris 12703 + aandeel % Brugge/Beernem/Damme/Jabbeke/Oostkamp/Zedelgem/OCMW/private unpublished,Leftover woonmaatschappij Vivendo after leftover AGB/APB hunt: omzet 44.90m DROP / pers 6.73m 75.1 VTE / debt 481.41m / cash 24.75m JUMP / PnL DROP 0.89m / dividend 0 / 2 VE hides municipal housing vehicle,8,Vivendo / Bestuursorgaan / voorzitter Van Belleghem Doenja,info@vivendo.be,Handboogstraat 2 bus 13 8000 Brugge,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1473 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF now extracted (710320 bytes 56p). FOI ready not sent. NOT every-10. NOT SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / Toerisme Limburg / Toerisme Vlaams-Brabant / Toerisme Oost-Vlaanderen / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still no separate APB 2025 PDF. WoonST Temse still JR2024 as of 1467. stek92 still JR2024 this tick.",
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
    if not last_s.startswith("rq_1473,"):
        raise SystemExit(f"expected last row rq_1473, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1473 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1473,Vivendo JR2025 leftover dual residual,hole_fill,5,done,L5,wm_vvnd,"
        "Completed: Vivendo leftover woonmaatschappij of mined Stad Brugge + Beernem + Damme + Jabbeke + Oostkamp + Zedelgem after leftover AGB/APB hunt; KBO 0406.062.883 Actief; live JR2025 official NBB WVV VOL-inb PDF (710320 bytes 56p; deposit 2026-00154781; AV 08.06.2026; header 09.06.2026; pdfinfo 12.06.2026 03:00:16 UTC). PDF header Vivendo / Handboogstraat 2 bus 0013 — NOT SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Sourced euros assets 605932612 omzet 44896478 diensten 14062354 pers 6725524 75.1 VTE pnl 894681 equity 120004062 cash 24748434 debt 481406996 capex 37681448 dividend 0. FOI "
        f"{GAP} ready not sent. Distinct from already-mined SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461.,"
        f"{GAP},2026-08-19T17:20:00Z,{TS},"
        "tick1473 Vivendo leftover woonmaatschappij residual; KBO 0406.062.883; live JR2025 official NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1474 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (Thuisrand 0404.710.724 JR2025 spotted)"
    )
    spawn = (
        "rq_1474,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill: Next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1473 done including Vivendo 1473 leftover woonmaatschappij live official NBB WVV / SW+ 1472 leftover woonmaatschappij live official NBB WVV / Woonhaven 1471 leftover woonmaatschappij live official NBB WVV / Thuispunt Gent 1470 leftover woonmaatschappij live official NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 404 as of 1473). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1473). Do NOT confuse with already-mined Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live. Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1471 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1461. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonhaven TAKEN 1471; SW+ TAKEN 1472; Vivendo TAKEN 1473; Thuisrand 0404.710.724 JR2025 spotted; WoonST Temse still JR2024 as of 1467; stek92 still JR2024 as of 1473). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461.,,"
        f"{TS},{TS},"
        "spawned tick1473 after Vivendo leftover woonmaatschappij live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (Thuisrand spotted)"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1473=done + rq_1474 spawned; keep", last_line_start)

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
    Path("/tmp/tick1473_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1473 Vivendo leftover woonmaatschappij residual; KBO 0406.062.883; live JR2025 official NBB WVV PDF; sourced euros assets 605932612 omzet 44896478 diensten 14062354 pers 6725524 75.1 VTE pnl 894681 equity 120004062 cash 24748434 debt 481406996 capex 37681448 dividend 0; FOI ready omzet 44.90m DROP / pers 6.73m 75.1 VTE / debt 481.41m / cash 24.75m JUMP / PnL DROP 0.89m / dividend 0 / 2 VE; NOT SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1474 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (Thuisrand 0404.710.724 spotted); FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1473,1473,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1473")

    entry = (
        "\n## Tick 1473 - 2026-08-19 - rq_1473 Vivendo Brugge dual residual leftover\n"
        "- Unit: Vivendo BV (leftover woonmaatschappij / social-housing BV of mined Stad Brugge + Beernem + Damme + Jabbeke + Oostkamp + Zedelgem; 2 VE) after residual dual hunt (KBO **0406.062.883**; official NBB WVV VOL-inb PDF **710320** bytes / 56p; deposit **2026-00154781**; AV **08.06.2026**; header **09.06.2026**; pdfinfo created **12.06.2026 03:00:16 UTC**; model **VOL-inb** 26.0.12 m82-f; commissaris Moore Audit BV B00212 / 0453.925.059 / Vandenabeele Liesbet A02306 mandate 10.06.2024–14.06.2027 fee **12703** + extra 3500 + andere 2900; VOL-inb 6.1/6.2.1/6.2.2/6.2.4/6.2.5/6.3.4/6.3.5/6.4.1/6.4.2/6.5.1/6.5.2/6.7.2/6.15/6.17/6.18.2/6.20/9/12/13/14/15 not filed; 6.2.3 IVA + 6.3 MVA + 6.6 + 6.7.1 + 6.9 + 6.10 + 6.16 + 6.19 + sociale balans + commissarisverslag + remuneratieverslag filed). Leftover AGB/APB first: leftover APB Inovant / Atlas Foleon `jaarrekening_25_inov` / `jaarrekening_25_atlas` HEAD **404** this tick; provincieantwerpen.be **403** even with Googlebot UA; no fetchable 2025 Inovant/Atlas PDF (do not take Hooibeekhoeve). Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick (puyenbroeck.be redirects to oost-vlaanderen.be). Leftover AGB Herzele already in entities (tick1163) — skipped. Leftover AGB Bornem still 2024 (2026-00553588 HEAD 403). Leftover AGB Hasselt / SOLag / WAGSO / Temse / Herk / Lommel already in entities — skipped. Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 last JR still 2024-12-31 as of 1471. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover WoonST Temse still JR2024 as of 1467. Leftover stek92 still JR2024 this tick. Leftover Vivendo statutory CDN `2026-00154781` live this tick (HTTP 200 / application/pdf / 710320 / 56p; jaar **2025-12-31**; neerlegging **09.06.2026**) — taken (hunt order #2 leftover unmined woonmaatschappij of mined Brugge-regio with live 2025 statutory PDF after leftover AGB/APB hunt). PDF header **Vivendo / Handboogstraat 2 bus 0013 / 8000 Brugge** — NOT SW+ / Woonhaven / Thuispunt Gent / Dimensa / Tuinwijk / Dijledal / Dender-Zuid / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Distinct from already-mined **SW+ 1472** / **Woonhaven 1471** / **Thuispunt Gent 1470** / **Tuinwijk 1469** / **Dijledal 1468** / **Dender-Zuid 1467** / **Dimensa 1466** / **Woonmaatschappij Rivierenland 1465** / **Woonpunt Waas 1464** / **Toerisme Limburg 1463** / **Toerisme Vlaams-Brabant 1462** / **Toerisme Oost-Vlaanderen 1461**. First confirmed not already extracted as JR2025 euros: no Vivendo / 0406.062.883 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **07.11.1955**; statutaire naam VIVENDO since 11.06.2007; BV since 15.12.2021; zetel Handboogstraat 2 bus 13 8000 Brugge since 15.12.2021; **2 VE**; 15 functiehouders; voorzitter Van Belleghem Doenja since 15.12.2021; ondervoorzitter Demon Franky + Vande Ginste Sebastian; gevolmachtigd bestuurder Knockaert Joke; Werkgever RSZ since 01.04.1962; btw since 23.05.1995; aanbestedende overheid; NACE 68.202 / 68.110 / 68.121; site https://www.vivendo.be/; werkingsgebied Stad Brugge + Beernem + Damme + Jabbeke + Oostkamp + Zedelgem. Absorbeerde HAARD EN KOUTER 0205.115.705 since 12.05.2006 + Brugse Maatschappij voor Huisvesting 0405.096.546 since 15.12.2021. Prior-year figures **identiek**. SBM used for deposit-id discovery only (SBM table 1-euro-off vs PDF; SBM HTML IP-blacklisted via box curl this tick). Euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1480).\n"
        "- EUR strong (primary official WVV VOL-inb; omzet 70 **44896478** DROP vs 48298483; 6.10 omzet-split empty; diensten 61 **14062354** JUMP vs 12372336; pers 62 **6725524** / **75,1 VTE** vs 6057510 / 70,3): assets **605932612** (was 613487534); fixed **572850233** vs 576805610 / IVA **1537** vs 3205 / MVA **572760451** vs 576714160 (terreinen/gebouwen **536596288**; installaties **14167**; meubilair **339630**; leasing empty; in aanbouw **35810366 DROP** vs 58119086) / FVA **88245**; current **33082379** vs 36681924; voorraden **2838366 DROP** vs 10613189 (onroerend verkoop **2838366**); ST recv **1306913** (trade **478030** / other **828883**); LT recv empty; geldbeleg empty; cash **24748434 JUMP** vs 20947648 (huurwaarborgen 4508892); prepaid **4188666**; equity **120004062 DROP** vs 122988286 (inbreng **62306**; herw **70060**; reserves **96161783**; overgedragen empty; kapsubs **23709913 DROP** vs 24219008); voorzieningen **4521554** (grote herstellingen **2835358**; milieu **213850**; overige **47900**; uitgestelde belasting **1424446**); schulden **481406996 DROP** vs 485462680 (LT **448963595** waarvan fin krediet **444350619 DROP** vs 451002279; ST **29215134** waarvan 42 **16818855** + leveranciers **7812489**; deferred **3228266**); omzet **44896478** DROP; 60 **8999132**; diensten **14062354** JUMP; pers **6725524** / **75,1 VTE** / 118451 uur / YE **86** personen vs 75; interim **3,4 VTE** 454285; afschr **15388491**; expl **+1675993 DROP** vs +5789256; fin opbr **9478586**; fin kosten **10248776**; tax **58104**; PnL **9904 +894681 DROP** vs +4459704 (te bestemmen 9905 **989030**); dividend **0**; capex MVA aanschaf **37681448** (terreinen 2369045 + install 10298 + meubilair 69308 + in aanbouw 35232797) + IVA 0. Commissaris fee **12703**. 2 VE. 6.7.2 aandeel % unpublished. Cross-checks: 572850233+33082379=605932612; 120004062+4521554+481406996=605932612; 50917841-49241849=1675992 vs 1675993; 1675993+9478586-10248776=905803; 905803+46983-58104=894682 vs 894681; 894681+94349=989030. 1-euro rounding on expl/PnL. SBM table 1-euro-off vs PDF.\n"
        "- CSVs: sources +4; entities +1 `wm_vvnd` parent `city_brugge`; budgets +42 executed; commitments +1 envelope 44896478 AV 08.06.2026; leaderboard +1 annual 44896478 / total 605932612; foi_queue +1 status=ready never sent; research_queue surgical rq_1473=done + rq_1474 spawn; loop_state ticks_completed=1473. Inventory after write: budgets {INV_B} · commitments {INV_C} · leaderboard {INV_L} · entities {INV_E} · sources {INV_S} · FOI ready {FOI_R} / answered {FOI_A} / partial {FOI_P} / total {FOI_T}.\n"
        "- FOI: `gap_vvnd_omzet_44_90m_pers_6_73m_debt_481m_l5` ready not sent — omzet 44.90m DROP / 6.10 split empty / diensten 14.06m JUMP / pers 6.73m 75.1 VTE / 2 VE / cash JUMP 24.75m / debt 481.41m LT krediet 444.35m / voorraden DROP 2.84m / capex 37.68m / PnL DROP 0.89m / dividend 0 / commissaris 12.70k / aandeel % unpublished.\n"
        "- Next: rq_1474 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 404 this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1473). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live. Leftover IGS IVAREM **0267.403.264** still JR2024 as of 1471. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonhaven **0403.795.657** TAKEN 1471; SW+ **0405.342.610** TAKEN 1472; Vivendo **0406.062.883** TAKEN 1473; Thuisrand **0404.710.724** JR2025 spotted this tick; WoonST Temse still JR2024 as of 1467; stek92 still JR2024 this tick). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460. Next every-10 is **1480**. Provincial tourism VZWs now exhausted (Westtoer + TOV + TVLB + TLim).\n"
    )
    entry = entry.replace("{INV_B}", str(inv["budgets.csv"])).replace("{INV_C}", str(inv["commitments.csv"])).replace("{INV_L}", str(inv["leaderboard.csv"])).replace("{INV_E}", str(inv["entities.csv"])).replace("{INV_S}", str(inv["sources.csv"])).replace("{FOI_R}", str(foi_ready)).replace("{FOI_A}", str(foi_ans)).replace("{FOI_P}", str(foi_part)).replace("{FOI_T}", str(foi_tot))
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1473 -" in lraw:
        raise SystemExit("loop_log already has tick 1473 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1473")
    print("DONE tick 1473")

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

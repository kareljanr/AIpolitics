#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1472 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T17:20:00Z"
ENT = "wm_swpl"
SRC = "src_swpl_jr2025_nbb"
GAP = "gap_swpl_omzet_24_19m_pers_4_49m_debt_332m_l5"
LB = "lb_swpl_omzet_24_19m_pers_4_49m_debt_332m"
COMM = "comm_swpl_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00128816.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},SW+ official NBB WVV VOL-inb JR2025,{PDF},NBB / SW+,2026-08-19,budget,tick1472; official NBB WVV VOL-inb JR2025 PDF 64p / 628838 bytes; deposit 2026-00128816; AV 19.05.2026; header 29.05.2026; pdfinfo created 01.06.2026 11:08:05 UTC; model VOL-inb 26.0.11 m82-f; KBO 0405.342.610; assets 401693637 cash 6631278 debt 331973788 pers 4487149 omzet 24188277 diensten 9773856 pnl 3617392 equity 66956394",
        "src_swpl_site,SW+ official pages,https://swplus.be/,SW+ / mined Kortrijk+Wevelgem,2026-08-19,official_register,tick1472; leftover woonmaatschappij of mined Stad Kortrijk + Wevelgem; zetel Damastweversstraat 3 8500 Kortrijk; KBO 0405.342.610; NBB consult used for deposit-id discovery only",
        "src_kbo_swpl_0405342610,KBO SW+ 0405.342.610,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0405342610,KBO Public Search FOD Economie,2026-08-19,official_register,tick1472; Actief since 17.05.1923; BV since 09.06.2023; naam SW+ since 09.06.2023; zetel Damastweversstraat(Kor) 3 8500 Kortrijk; 3 VE; 16 functiehouders; Werkgever RSZ since 01.01.1956; aanbestedende overheid",
        "src_swpl_foi_contact,SW+ FOI channel (klachten@swplus.be / info@swplus.be),https://swplus.be/over-ons/klachtenprocedure/,SW+,2026-08-19,official_register,tick1472; leftover woonmaatschappij of mined Kortrijk+Wevelgem; NOT Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_swpl," in raw or raw.startswith(b"wm_swpl,"):
        raise SystemExit("wm_swpl already present")
    if b"0405.342.610" in raw or b"0405342610" in raw:
        raise SystemExit("SW+ KBO already present as entity")
    row = (
        "wm_swpl,SW+ (leftover woonmaatschappij / social-housing BV of mined Stad Kortrijk + Wevelgem; NOT Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST),"
        "SW+ SRL (logement social residuel Kortrijk-Wevelgem),"
        "SW+ leftover social-housing company of mined Kortrijk+Wevelgem (not Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST),"
        "other,city_kortrijk,nl,https://swplus.be/,klachten@swplus.be,Damastweversstraat 3 8500 Kortrijk,"
        "tick1472 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0405.342.610 Actief since 17.05.1923; live JR2025 official NBB WVV PDF; sourced euros assets 401693637 omzet 24188277 diensten 9773856 pers 4487149 56.5 VTE pnl 3617392 equity 66956394 cash 6631278 debt 331973788 capex 27140667 dividend 0; FOI ready omzet 24.19m JUMP / pers 4.49m 56.5 VTE / debt 331.97m / cash 6.63m / PnL JUMP 3.62m / dividend 0 / 3 VE; distinct from already-mined Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_swpl")

def part_budgets():
    BUDGETS = [
        ("bud_swpl_assets_2025", "2025", "401693637", "2025 assets 401693637 (was 392252146); tick1472; primary official NBB WVV VOL-inb 2026-00128816"),
        ("bud_swpl_current_2025", "2025", "16127712", "2025 vlottend 16127712 (was 23467812); tick1472; primary official NBB WVV"),
        ("bud_swpl_cash_2025", "2025", "6631278", "2025 liquide middelen 6631278 DROP (was 6763793); tick1472; primary official NBB WVV"),
        ("bud_swpl_geldbeleg_2025", "2025", "643", "2025 geldbeleggingen 643; tick1472; primary official NBB WVV"),
        ("bud_swpl_strecv_2025", "2025", "2796790", "2025 ST vorderingen 2796790 (was 4584215); tick1472; primary official NBB WVV"),
        ("bud_swpl_trade_2025", "2025", "682813", "2025 handelsvorderingen 682813 (was 863270); tick1472; primary official NBB WVV"),
        ("bud_swpl_othrecv_2025", "2025", "2113977", "2025 overige ST vorderingen 2113977; tick1472; primary official NBB WVV"),
        ("bud_swpl_voorraden_2025", "2025", "3711133", "2025 voorraden 3711133 DROP (was 9604940; onroerend verkoop 3711133); tick1472; primary official NBB WVV"),
        ("bud_swpl_prepaid_2025", "2025", "2987868", "2025 overlopend actief 2987868 (was 2514221); tick1472; primary official NBB WVV"),
        ("bud_swpl_fixed_2025", "2025", "385565925", "2025 vaste activa 385565925 (was 368784334); tick1472; primary official NBB WVV"),
        ("bud_swpl_iva_2025", "2025", "95526", "2025 IVA 95526 (was 9477); tick1472; primary official NBB WVV"),
        ("bud_swpl_mva_2025", "2025", "385147896", "2025 MVA 385147896 (was 368472086; terreinen/gebouwen 353650824 in aanbouw 31159960); tick1472; primary official NBB WVV"),
        ("bud_swpl_fva_2025", "2025", "322503", "2025 FVA 322503 (aandelen 273609 + borg 48894); tick1472; primary official NBB WVV"),
        ("bud_swpl_equity_2025", "2025", "66956394", "2025 eigen vermogen 66956394 (was 64117354); tick1472; primary official NBB WVV"),
        ("bud_swpl_inbreng_2025", "2025", "108592", "2025 inbreng 108592 (onbeschikbaar 108592); tick1472; primary official NBB WVV"),
        ("bud_swpl_reserves_2025", "2025", "36304489", "2025 reserves 36304489; tick1472; primary official NBB WVV"),
        ("bud_swpl_kapsubs_2025", "2025", "30543313", "2025 kapitaalsubsidies 30543313 DROP (was 31291228); tick1472; primary official NBB WVV"),
        ("bud_swpl_voorz_2025", "2025", "2763455", "2025 voorzieningen+uitgestelde belasting 2763455; tick1472; primary official NBB WVV"),
        ("bud_swpl_debt_2025", "2025", "331973788", "2025 schulden 331973788 JUMP (was 324943877); tick1472; primary official NBB WVV"),
        ("bud_swpl_ltdebt_2025", "2025", "310893800", "2025 LT schulden 310893800 (was 301533379; fin krediet 307957377); tick1472; primary official NBB WVV"),
        ("bud_swpl_stdebt_2025", "2025", "18821397", "2025 ST schulden 18821397 (was 21637862); tick1472; primary official NBB WVV"),
        ("bud_swpl_lev_2025", "2025", "3813259", "2025 leveranciers 3813259 DROP (was 6313918); tick1472; primary official NBB WVV"),
        ("bud_swpl_bezold_2025", "2025", "689545", "2025 bezoldigingen-schulden 689545 (was 455610); tick1472; primary official NBB WVV"),
        ("bud_swpl_taxpay_2025", "2025", "1624415", "2025 belastingschulden 1624415 (was 1374652); tick1472; primary official NBB WVV"),
        ("bud_swpl_deferred_2025", "2025", "2258591", "2025 overlopend passief 2258591 (was 1772636); tick1472; primary official NBB WVV"),
        ("bud_swpl_omzet_2025", "2025", "24188277", "2025 omzet 70 24188277 JUMP (was 22903074); tick1472; primary official NBB WVV"),
        ("bud_swpl_diensten_2025", "2025", "9773856", "2025 diensten 61 9773856 (was 9190036); tick1472; primary official NBB WVV"),
        ("bud_swpl_aankopen_2025", "2025", "849750", "2025 handelsgoederen/grondstoffen 60 849750 (aankopen 667555 voorraad 182195); tick1472; primary official NBB WVV"),
        ("bud_swpl_pers_2025", "2025", "4487149", "2025 pers 62 4487149; 56.5 VTE vs 57.2; 84172 uur; YE 58.2; tick1472; primary official NBB WVV"),
        ("bud_swpl_afschr_2025", "2025", "9111934", "2025 afschrijvingen 9111934; tick1472; primary official NBB WVV"),
        ("bud_swpl_expl_2025", "2025", "4228672", "2025 bedrijfswinst 4228672 JUMP (was 998496); tick1472; primary official NBB WVV"),
        ("bud_swpl_finopbr_2025", "2025", "7470693", "2025 financiele opbrengsten 7470693 all recurrent; tick1472; primary official NBB WVV"),
        ("bud_swpl_finkost_2025", "2025", "8010628", "2025 financiele kosten 8010628; tick1472; primary official NBB WVV"),
        ("bud_swpl_pnl_2025", "2025", "3617392", "2025 PnL 3617392 JUMP (was 380047); tick1472; primary official NBB WVV"),
        ("bud_swpl_div_2025", "2025", "0", "2025 dividend 0 vergoeding van de inbreng empty; tick1472; primary official NBB WVV"),
        ("bud_swpl_capex_2025", "2025", "27140667", "2025 capex MVA aanschaf 27140667 (terreinen 3390177 + install 27585 + in aanbouw 23722905); tick1472; primary official NBB WVV"),
        ("bud_swpl_bedrijfsopbr_2025", "2025", "30991770", "2025 bedrijfsopbrengsten 70/76A 30991770; tick1472; primary official NBB WVV"),
        ("bud_swpl_bedrijfskost_2025", "2025", "26763098", "2025 bedrijfskosten 60/66A 26763098; tick1472; primary official NBB WVV"),
        ("bud_swpl_tax_2025", "2025", "34131", "2025 belastingen 67/77 34131; tick1472; primary official NBB WVV"),
        ("bud_swpl_in_aanbouw_2025", "2025", "31159960", "2025 activa in aanbouw 31159960 DROP (was 35373236); tick1472; primary official NBB WVV"),
        ("bud_swpl_krediet_2025", "2025", "307957377", "2025 LT kredietinstellingen 307957377 JUMP (was 298795574); tick1472; primary official NBB WVV"),
        ("bud_swpl_terreinen_2025", "2025", "353650824", "2025 terreinen en gebouwen 353650824 (was 332581483); tick1472; primary official NBB WVV"),
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
        f"{COMM},SW+ JR2025 leftover woonmaatschappij dual (omzet 24.19m JUMP / diensten 9.77m / pers 4.49m 56.5 VTE / debt 331.97m / cash 6.63m / PnL JUMP 3.62m / dividend 0 / 3 VE),{ENT},Kortrijk+Wevelgem / mined Kortrijk dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-19,1923,,24188277,,,active,{PDF},Local leftover woonmaatschappij map VL Kortrijk-Wevelgem — omzet 24.19m JUMP / pers 4.49m 56.5 VTE / debt 331.97m / cash 6.63m,Publish omzet split + 3 VE payroll + cash 6.63m + LT krediet 307.96m counterparties + capex 27.14m + aandeel % Kortrijk/Wevelgem/OCMW/private + dividend 0; do not keep leftover woonmaatschappij as unpublished 24.19m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Kortrijk>Woonmaatschappij>SW+>JR2025_L5,tick1472; assets 401693637 omzet 24188277 diensten 9773856 pers 4487149 pnl 3617392 equity 66956394 cash 6631278 debt 331973788 capex 27140667 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},SW+ JR2025 leftover woonmaatschappij: omzet 24.19m JUMP / diensten 9.77m / pers 4.49m 56.5 VTE / debt 331.97m / cash 6.63m / PnL JUMP 3.62m / dividend 0 / 3 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Kortrijk>Woonmaatschappij>SW+>JR2025_L5,24188277,401693637,Leftover dual woonmaatschappij shell: assets 401.69m / equity 66.96m / omzet 24.19m JUMP / diensten 9.77m / pers 4.49m 56.5 VTE / cash 6.63m / debt 331.97m / LT krediet 307.96m / PnL 3.62m JUMP / dividend 0 / 3 VE; do not treat 24.19m as TE-additive of 348bn,strong,{SRC},SW+ / mined Kortrijk+Wevelgem dual housing,Local leftover woonmaatschappij map VL Kortrijk-Wevelgem — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 24.19m JUMP / pers 4.49m 56.5 VTE / debt 331.97m / cash 6.63m / PnL JUMP 3.62m / dividend 0 / 3 VE,7.0,7.0,3.0,7.0,Publish omzet split + 3 VE payroll + cash 6.63m + LT krediet 307.96m counterparties + capex 27.14m + aandeel % Kortrijk/Wevelgem/OCMW/private + dividend 0; do not keep leftover woonmaatschappij as unpublished 24.19m housing shell,active,,tick1472; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Gemeenten>Kortrijk>Woonmaatschappij>SW+>JR2025_L5,{ENT},omzet 24188277 JUMP vs 22903074 + diensten 9773856 vs 9190036 + pers 4487149 56.5 VTE vs 57.2 + 3 VE + cash 6631278 DROP vs 6763793 + debt 331973788 LT krediet 307957377 + voorraden 3711133 DROP onroerend 3711133 + capex 27140667 in aanbouw DROP 31159960 vs 35373236 + PnL JUMP 3617392 vs 380047 + dividend 0 + commissaris 12356 + aandeel % Kortrijk/Wevelgem/OCMW/private unpublished,Leftover woonmaatschappij SW+ after leftover AGB/APB hunt: omzet 24.19m JUMP / pers 4.49m 56.5 VTE / debt 331.97m / cash 6.63m / PnL JUMP 3.62m / dividend 0 / 3 VE hides municipal housing vehicle,8,SW+ / Bestuursorgaan / voorzitter,klachten@swplus.be,Damastweversstraat 3 8500 Kortrijk,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1472 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF now extracted (628838 bytes 64p). FOI ready not sent. NOT every-10. NOT Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / Toerisme Limburg / Toerisme Vlaams-Brabant / Toerisme Oost-Vlaanderen / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still no separate APB 2025 PDF. WoonST Temse still JR2024 as of 1467.",
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
    if not last_s.startswith("rq_1472,"):
        raise SystemExit(f"expected last row rq_1472, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1472 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1472,SW+ JR2025 leftover dual residual,hole_fill,5,done,L5,wm_swpl,"
        "Completed: SW+ leftover woonmaatschappij of mined Stad Kortrijk + Wevelgem after leftover AGB/APB hunt; KBO 0405.342.610 Actief; live JR2025 official NBB WVV VOL-inb PDF (628838 bytes 64p; deposit 2026-00128816; AV 19.05.2026; header 29.05.2026; pdfinfo 01.06.2026 11:08:05 UTC). PDF header SW+ / Damastweversstraat(Kor) 3 — NOT Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Sourced euros assets 401693637 omzet 24188277 diensten 9773856 pers 4487149 56.5 VTE pnl 3617392 equity 66956394 cash 6631278 debt 331973788 capex 27140667 dividend 0. FOI "
        f"{GAP} ready not sent. Distinct from already-mined Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461.,"
        f"{GAP},2026-08-19T17:10:00Z,{TS},"
        "tick1472 SW+ leftover woonmaatschappij residual; KBO 0405.342.610; live JR2025 official NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1473 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025"
    )
    spawn = (
        "rq_1473,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill: Next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1472 done including SW+ 1472 leftover woonmaatschappij live official NBB WVV / Woonhaven 1471 leftover woonmaatschappij live official NBB WVV / Thuispunt Gent 1470 leftover woonmaatschappij live official NBB WVV / Tuinwijk 1469 leftover woonmaatschappij live official NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 404 as of 1472). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1472). Do NOT confuse with already-mined SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live. Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1471 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1461. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonhaven TAKEN 1471; SW+ TAKEN 1472; WoonST Temse still JR2024 as of 1467). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461.,,"
        f"{TS},{TS},"
        "spawned tick1472 after SW+ leftover woonmaatschappij live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1472=done + rq_1473 spawned; keep", last_line_start)

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
    Path("/tmp/tick1472_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1472 SW+ leftover woonmaatschappij residual; KBO 0405.342.610; live JR2025 official NBB WVV PDF; sourced euros assets 401693637 omzet 24188277 diensten 9773856 pers 4487149 56.5 VTE pnl 3617392 equity 66956394 cash 6631278 debt 331973788 capex 27140667 dividend 0; FOI ready omzet 24.19m JUMP / pers 4.49m 56.5 VTE / debt 331.97m / cash 6.63m / PnL JUMP 3.62m / dividend 0 / 3 VE; NOT Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1473 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1472,1472,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1472")

    entry = (
        "\n## Tick 1472 - 2026-08-19 - rq_1472 SW+ Kortrijk dual residual leftover\n"
        "- Unit: SW+ BV (leftover woonmaatschappij / social-housing BV of mined Stad Kortrijk + Wevelgem; 3 VE) after residual dual hunt (KBO **0405.342.610**; official NBB WVV VOL-inb PDF **628838** bytes / 64p; deposit **2026-00128816**; AV **19.05.2026**; header **29.05.2026**; pdfinfo created **01.06.2026 11:08:05 UTC**; model **VOL-inb** 26.0.11 m82-f; commissaris Callens Vandelanotte NV B-00083 / 0433.608.707 / Vandelanotte Frank A01476 mandate 30.05.2023–19.05.2026 fee **12356** + extra 3200 + verbonden 9375+535; VOL-inb 6.1/6.2.1/6.2.2/6.2.4/6.2.5/6.4.1/6.4.2/6.5.1/6.5.2/6.7.2/6.8/6.15/6.17/6.18.2/6.20/9/12/13/14/15 not filed; 6.2.3 IVA + 6.3 MVA + 6.4 FVA + 6.6 + 6.7.1 + 6.9 + 6.10 + 6.16 + 6.19 + sociale balans + commissarisverslag filed). Leftover AGB/APB first: leftover APB Inovant / Atlas Foleon `jaarrekening_25_inov` / `jaarrekening_25_atlas` HEAD **404** this tick; provincieantwerpen.be **403** even with Googlebot UA; no fetchable 2025 Inovant/Atlas PDF (do not take Hooibeekhoeve). Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick. Leftover AGB Herzele already in entities (tick1163) — skipped. Leftover AGB Bornem still 2024. Leftover AGB Hasselt / SOLag / WAGSO / Temse / Herk / Lommel already in entities — skipped. Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 last JR still 2024-12-31 as of 1471. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover WoonST Temse still JR2024 as of 1467. Leftover SW+ statutory CDN `2026-00128816` live this tick (HTTP 200 / application/pdf / 628838 / 64p; jaar **2025-12-31**; neerlegging **29.05.2026**) — taken (hunt order #2 leftover unmined woonmaatschappij of mined Kortrijk+Wevelgem with live 2025 statutory PDF after leftover AGB/APB hunt). PDF header **SW+ / Damastweversstraat(Kor) 3 / 8500 Kortrijk** — NOT Woonhaven / Thuispunt Gent / Dimensa / Tuinwijk / Dijledal / Dender-Zuid / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Distinct from already-mined **Woonhaven 1471** / **Thuispunt Gent 1470** / **Tuinwijk 1469** / **Dijledal 1468** / **Dender-Zuid 1467** / **Dimensa 1466** / **Woonmaatschappij Rivierenland 1465** / **Woonpunt Waas 1464** / **Toerisme Limburg 1463** / **Toerisme Vlaams-Brabant 1462** / **Toerisme Oost-Vlaanderen 1461**. First confirmed not already extracted as JR2025 euros: no SW+ / 0405.342.610 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **17.05.1923**; statutaire naam SW+ since 09.06.2023; BV since 09.06.2023; zetel Damastweversstraat(Kor) 3 8500 Kortrijk since 19.03.2024; **3 VE**; 16 functiehouders; voorzitter Decaluwe Veronique; ondervoorzitter Loosvelt Christiane; Lid Directiecomité Raes Thomas since 17.06.2025; Werkgever RSZ since 01.01.1956; btw since 01.07.2017; aanbestedende overheid; NACE 68.202; site https://swplus.be/; werkingsgebied Stad Kortrijk + Wevelgem. Absorbeerde De Vlashaard 0453.559.231 since 09.06.2023. Prior-year figures **identiek**. NBB consult used for deposit-id discovery only. Euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1480).\n"
        "- EUR strong (primary official WVV VOL-inb; omzet 70 **24188277** JUMP vs 22903074; 6.10 omzet-split empty; diensten 61 **9773856** vs 9190036; pers 62 **4487149** / **56,5 VTE** vs 5038706 / 57,2): assets **401693637** (was 392252146); fixed **385565925** vs 368784334 / IVA **95526** vs 9477 / MVA **385147896** vs 368472086 (terreinen/gebouwen **353650824**; installaties **107832**; meubilair **225192**; leasing **778**; overige **3310**; in aanbouw **31159960 DROP** vs 35373236) / FVA **322503**; current **16127712** vs 23467812; voorraden **3711133 DROP** vs 9604940 (onroerend verkoop **3711133**); ST recv **2796790** (trade **682813** / other **2113977**); LT recv empty; geldbeleg **643**; cash **6631278 DROP** vs 6763793; prepaid **2987868**; equity **66956394** vs 64117354 (inbreng **108592**; reserves **36304489**; overgedragen empty; kapsubs **30543313 DROP** vs 31291228); voorzieningen **2763455** (grote herstellingen **899927**; uitgestelde belasting **1863528**); schulden **331973788 JUMP** vs 324943877 (LT **310893800** waarvan fin krediet **307957377 JUMP** vs 298795574; ST **18821397** waarvan 42 **12016392** + leveranciers **3813259 DROP** vs 6313918; deferred **2258591**); omzet **24188277** JUMP; 60 **849750**; diensten **9773856**; pers **4487149** / **56,5 VTE** / 84172 uur / YE **58,2 VTE** 61 personen vs 57; afschr **9111934**; expl **+4228672 JUMP** vs +998496; fin opbr **7470693** (interestsubs 6828079); fin kosten **8010628**; tax **34131**; PnL **9904 +3617392 JUMP** vs +380047 (te bestemmen 9905 **2321946**); dividend **0**; capex MVA aanschaf **27140667** (terreinen 3390177 + install 27585 + in aanbouw 23722905) + IVA 56402 + FVA 19615. Commissaris fee **12356**. 3 VE. 6.7.2 aandeel % unpublished. Cross-checks: 385565925+16127712=401693637; 66956394+2763455+331973788=401693637; 30991770-26763098=4228672; 4228672+7470693-8010628=3688737; 3688737+35551-72765-34131=3617392; 3617392+87091-1382537=2321946. Prior-year passiva 392252147 vs assets 392252146 (1-euro).\n"
        "- CSVs: sources +4; entities +1 `wm_swpl` parent `city_kortrijk`; budgets +42 executed; commitments +1 envelope 24188277 AV 19.05.2026; leaderboard +1 annual 24188277 / total 401693637; foi_queue +1 status=ready never sent; research_queue surgical rq_1472=done + rq_1473 spawn; loop_state ticks_completed=1472. Inventory after write: budgets {INV_B} · commitments {INV_C} · leaderboard {INV_L} · entities {INV_E} · sources {INV_S} · FOI ready {FOI_R} / answered {FOI_A} / partial {FOI_P} / total {FOI_T}.\n"
        "- FOI: `gap_swpl_omzet_24_19m_pers_4_49m_debt_332m_l5` ready not sent — omzet 24.19m JUMP / 6.10 split empty / diensten 9.77m / pers 4.49m 56.5 VTE / 3 VE / cash 6.63m / debt 331.97m LT krediet 307.96m / voorraden DROP 3.71m / capex 27.14m / PnL JUMP 3.62m / dividend 0 / commissaris 12.36k / aandeel % unpublished.\n"
        "- Next: rq_1473 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 404 this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1472). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live. Leftover IGS IVAREM **0267.403.264** still JR2024 as of 1471. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonhaven **0403.795.657** TAKEN 1471; SW+ **0405.342.610** TAKEN 1472; WoonST Temse still JR2024 as of 1467). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460. Next every-10 is **1480**. Provincial tourism VZWs now exhausted (Westtoer + TOV + TVLB + TLim).\n"
    )
    entry = entry.replace("{INV_B}", str(inv["budgets.csv"])).replace("{INV_C}", str(inv["commitments.csv"])).replace("{INV_L}", str(inv["leaderboard.csv"])).replace("{INV_E}", str(inv["entities.csv"])).replace("{INV_S}", str(inv["sources.csv"])).replace("{FOI_R}", str(foi_ready)).replace("{FOI_A}", str(foi_ans)).replace("{FOI_P}", str(foi_part)).replace("{FOI_T}", str(foi_tot))
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1472 -" in lraw:
        raise SystemExit("loop_log already has tick 1472 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1472")
    print("DONE tick 1472")

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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1466 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T16:05:00Z"
ENT = "wm_dmsa"
SRC = "src_dmsa_jr2025_nbb"
GAP = "gap_dmsa_omzet_39_36m_pers_7_87m_debt_443m_l5"
LB = "lb_dmsa_omzet_39_36m_pers_7_87m_debt_443m"
COMM = "comm_dmsa_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00138353.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Dimensa Woonmaatschappij official NBB WVV VOL-kap JR2025,{PDF},NBB / Dimensa Woonmaatschappij,2026-08-19,budget,tick1466; official NBB WVV VOL-kap JR2025 PDF 47p / 15439739 bytes; deposit 2026-00138353; AV 26.05.2026; header 02.06.2026; pdfinfo created 02.06.2026 13:08:57 UTC; model VOL-kap 26.0.12 m02-f-p; KBO 0400.067.887; assets 633527939 cash 40819167 debt 443380246 pers 7872133 omzet 39356346 diensten 14318019 pnl 2181013 equity 183607951",
        "src_dmsa_site,Dimensa Woonmaatschappij official pages,https://www.dimensa.be/,Dimensa / mined Gent-Zuid cities,2026-08-19,official_register,tick1466; leftover woonmaatschappij of mined Aalter+Deinze+Destelbergen+Gavere+Lievegem+Merelbeke-Melle+Nazareth-De Pinte+Sint-Martens-Latem+Zulte; zetel Ravensteinstraat 12 9000 Gent; KBO 0400.067.887; NBB consult for deposit id",
        "src_kbo_dmsa_0400067887,KBO Dimensa Woonmaatschappij 0400.067.887,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0400067887,KBO Public Search FOD Economie,2026-08-19,official_register,tick1466; Actief since 03.01.1928; BV since 30.06.2022; naam Dimensa Woonmaatschappij since 30.05.2023; zetel Ravensteinstraat 12 9000 Gent; 1 VE; 19 functiehouders; Werkgever RSZ since 01.01.1945; aanbestedende overheid",
        "src_dmsa_foi_contact,Dimensa Woonmaatschappij FOI channel (info@dimensa.be),https://www.dimensa.be/nl/contact,Dimensa Woonmaatschappij,2026-08-19,official_register,tick1466; leftover woonmaatschappij of mined Gent-Zuid cities; NOT Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_dmsa," in raw or raw.startswith(b"wm_dmsa,"):
        raise SystemExit("wm_dmsa already present")
    if b"0400.067.887" in raw:
        raise SystemExit("Dimensa KBO already present as entity")
    row = (
        "wm_dmsa,Dimensa Woonmaatschappij (leftover woonmaatschappij / social-housing BV of mined Gent-Zuid cities Aalter + Deinze + Destelbergen + Gavere + Lievegem + Merelbeke-Melle + Nazareth-De Pinte + Sint-Martens-Latem + Zulte; NOT Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg),"
        "Societe de logement Dimensa SRL (logement social residuel Gent-Zuid),"
        "Dimensa leftover social-housing company of mined Gent-Zuid cities (not Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg),"
        "other,city_deinze,nl,https://www.dimensa.be/,info@dimensa.be,Ravensteinstraat 12 9000 Gent,"
        "tick1466 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0400.067.887 Actief since 03.01.1928; live JR2025 official NBB WVV PDF; sourced euros assets 633527939 omzet 39356346 diensten 14318019 pers 7872133 102.5 VTE pnl 2181013 equity 183607951 cash 40819167 debt 443380246 capex 11428045 dividend 6304; FOI ready omzet 39.36m DROP / pers 7.87m 102.5 VTE / debt 443.38m / cash DROP 40.82m / PnL DROP 2.18m / dividend 6304 / 1 VE; distinct from already-mined Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_dmsa")

def part_budgets():
    BUDGETS = [
        ("bud_dmsa_assets_2025", "2025", "633527939", "2025 assets 633527939 DROP (was 645505336); tick1466; primary official NBB WVV VOL-kap 2026-00138353"),
        ("bud_dmsa_current_2025", "2025", "75735670", "2025 vlottend 75735670 (was 82166136); tick1466; primary official NBB WVV"),
        ("bud_dmsa_cash_2025", "2025", "40819167", "2025 liquide middelen 40819167 DROP (was 54369441); tick1466; primary official NBB WVV"),
        ("bud_dmsa_geldbeleg_2025", "2025", "0", "2025 geldbeleggingen empty; tick1466; primary official NBB WVV"),
        ("bud_dmsa_strecv_2025", "2025", "2675513", "2025 ST vorderingen 2675513; tick1466; primary official NBB WVV"),
        ("bud_dmsa_trade_2025", "2025", "838861", "2025 handelsvorderingen 838861; tick1466; primary official NBB WVV"),
        ("bud_dmsa_othrecv_2025", "2025", "1836652", "2025 overige ST vorderingen 1836652; tick1466; primary official NBB WVV"),
        ("bud_dmsa_ltrecv_2025", "2025", "1194720", "2025 LT vorderingen 1194720; tick1466; primary official NBB WVV"),
        ("bud_dmsa_voorraden_2025", "2025", "26986164", "2025 voorraden 26986164 (onroerend verkoop 26761981 + grond 224183); tick1466; primary official NBB WVV"),
        ("bud_dmsa_prepaid_2025", "2025", "4060106", "2025 overlopend actief 4060106 (verkregen 3793933 + over te dragen 266173); tick1466; primary official NBB WVV"),
        ("bud_dmsa_fixed_2025", "2025", "557792269", "2025 vaste activa 557792269 (was 563339200); tick1466; primary official NBB WVV"),
        ("bud_dmsa_iva_2025", "2025", "303077", "2025 IVA 303077 (was 223860); tick1466; primary official NBB WVV"),
        ("bud_dmsa_mva_2025", "2025", "557456115", "2025 MVA 557456115 (was 563082263; terreinen/gebouwen 513023752 in aanbouw 42801441); tick1466; primary official NBB WVV"),
        ("bud_dmsa_fva_2025", "2025", "33077", "2025 FVA 33077 (aandelen 1744 + borg 31333); tick1466; primary official NBB WVV"),
        ("bud_dmsa_equity_2025", "2025", "183607951", "2025 eigen vermogen 183607951 (was 182717464); tick1466; primary official NBB WVV"),
        ("bud_dmsa_inbreng_2025", "2025", "158056", "2025 inbreng 158056 (geplaatst 254211 - niet-opgevraagd 96155); tick1466; primary official NBB WVV"),
        ("bud_dmsa_reserves_2025", "2025", "140111372", "2025 reserves 140111372; tick1466; primary official NBB WVV"),
        ("bud_dmsa_kapsubs_2025", "2025", "43338523", "2025 kapitaalsubsidies 43338523; tick1466; primary official NBB WVV"),
        ("bud_dmsa_voorz_2025", "2025", "6539742", "2025 voorzieningen+uitgestelde belasting 6539742; tick1466; primary official NBB WVV"),
        ("bud_dmsa_debt_2025", "2025", "443380246", "2025 schulden 443380246 (was 455387570); tick1466; primary official NBB WVV"),
        ("bud_dmsa_ltdebt_2025", "2025", "415590032", "2025 LT schulden 415590032 (was 420358517; fin krediet 410460664); tick1466; primary official NBB WVV"),
        ("bud_dmsa_stdebt_2025", "2025", "23677378", "2025 ST schulden 23677378 (was 31250172); tick1466; primary official NBB WVV"),
        ("bud_dmsa_lev_2025", "2025", "557723", "2025 leveranciers 557723 DROP (was 2299242); tick1466; primary official NBB WVV"),
        ("bud_dmsa_bezold_2025", "2025", "828843", "2025 bezoldigingen-schulden 828843 (was 701621); tick1466; primary official NBB WVV"),
        ("bud_dmsa_taxpay_2025", "2025", "2208542", "2025 belastingschulden 2208542 (was 2128575); tick1466; primary official NBB WVV"),
        ("bud_dmsa_deferred_2025", "2025", "4112836", "2025 overlopend passief 4112836 (was 3778881); tick1466; primary official NBB WVV"),
        ("bud_dmsa_omzet_2025", "2025", "39356346", "2025 omzet 70 39356346 DROP (was 43540751); tick1466; primary official NBB WVV"),
        ("bud_dmsa_diensten_2025", "2025", "14318019", "2025 diensten 61 14318019; tick1466; primary official NBB WVV"),
        ("bud_dmsa_aankopen_2025", "2025", "2030307", "2025 handelsgoederen/grondstoffen 60 2030307 (aankopen 8283849 voorraad -6253542); tick1466; primary official NBB WVV"),
        ("bud_dmsa_pers_2025", "2025", "7872133", "2025 pers 62 7872133; 102.5 VTE vs 103.6; 133033 uur; YE 111; tick1466; primary official NBB WVV"),
        ("bud_dmsa_afschr_2025", "2025", "16301111", "2025 afschrijvingen 16301111; tick1466; primary official NBB WVV"),
        ("bud_dmsa_expl_2025", "2025", "1537108", "2025 bedrijfswinst 1537108 DROP (was 2393124); tick1466; primary official NBB WVV"),
        ("bud_dmsa_finopbr_2025", "2025", "9566997", "2025 financiele opbrengsten 9566997 all recurrent; tick1466; primary official NBB WVV"),
        ("bud_dmsa_finkost_2025", "2025", "8893328", "2025 financiele kosten 8893328; tick1466; primary official NBB WVV"),
        ("bud_dmsa_pnl_2025", "2025", "2181013", "2025 PnL 2181013 DROP (was 2725742); tick1466; primary official NBB WVV"),
        ("bud_dmsa_div_2025", "2025", "6304", "2025 dividend 6304 vergoeding van de inbreng; tick1466; primary official NBB WVV"),
        ("bud_dmsa_capex_2025", "2025", "11428045", "2025 capex MVA aanschaf 11428045 (terreinen 8102152 + install 40524 + meubilair 116338 + in aanbouw 3169031); tick1466; primary official NBB WVV"),
        ("bud_dmsa_bedrijfsopbr_2025", "2025", "44514981", "2025 bedrijfsopbrengsten 70/76A 44514981; tick1466; primary official NBB WVV"),
        ("bud_dmsa_bedrijfskost_2025", "2025", "42977873", "2025 bedrijfskosten 60/66A 42977873; tick1466; primary official NBB WVV"),
        ("bud_dmsa_tax_2025", "2025", "99492", "2025 belastingen 67/77 99492; tick1466; primary official NBB WVV"),
        ("bud_dmsa_in_aanbouw_2025", "2025", "42801441", "2025 activa in aanbouw 42801441 DROP (was 76013335); tick1466; primary official NBB WVV"),
        ("bud_dmsa_krediet_2025", "2025", "410460664", "2025 LT kredietinstellingen 410460664 (was 415407740); tick1466; primary official NBB WVV"),
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
        f"{COMM},Dimensa Woonmaatschappij JR2025 leftover woonmaatschappij dual (omzet 39.36m DROP / diensten 14.32m / pers 7.87m 102.5 VTE / debt 443.38m / cash DROP 40.82m / PnL DROP 2.18m / dividend 6304 / 1 VE),{ENT},Dimensa / mined Gent-Zuid dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-26,1928,,39356346,,,active,{PDF},Local leftover woonmaatschappij map VL Gent-Zuid — omzet 39.36m DROP / pers 7.87m 102.5 VTE / debt 443.38m / cash DROP 40.82m,Publish omzet split + 1 VE payroll + cash DROP 54.37m to 40.82m + LT krediet 410.5m counterparties + capex 11.43m + aandeel % 9 gemeenten/OCMW/provincie/VL/private + dividend 6304; do not keep leftover woonmaatschappij as unpublished 39.36m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Deinze>Woonmaatschappij>Dimensa>JR2025_L5,tick1466; assets 633527939 omzet 39356346 diensten 14318019 pers 7872133 pnl 2181013 equity 183607951 cash 40819167 debt 443380246 capex 11428045 dividend 6304; FOI ready not sent; not TE-additive of 348bn; NOT Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / Toerisme Limburg",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Dimensa Woonmaatschappij JR2025 leftover woonmaatschappij: omzet 39.36m DROP / diensten 14.32m / pers 7.87m 102.5 VTE / debt 443.38m / cash DROP 40.82m / PnL DROP 2.18m / dividend 6304 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Deinze>Woonmaatschappij>Dimensa>JR2025_L5,39356346,633527939,Leftover dual woonmaatschappij shell: assets 633.53m / equity 183.61m / omzet 39.36m DROP / diensten 14.32m / pers 7.87m 102.5 VTE / cash 40.82m DROP / debt 443.38m / LT krediet 410.5m / PnL 2.18m DROP / dividend 6304 / 1 VE; do not treat 39.36m as TE-additive of 348bn,strong,{SRC},Dimensa / mined Gent-Zuid dual housing,Local leftover woonmaatschappij map VL Gent-Zuid — JR2025 official NBB WVV live; omzet+pers+debt+cash+dividend FOI,Official NBB WVV 2026-08-19: omzet 39.36m DROP / pers 7.87m 102.5 VTE / debt 443.38m / cash DROP 40.82m / PnL DROP 2.18m / dividend 6304 / 1 VE,7.0,7.6,3.0,7.1,Publish omzet split + 1 VE payroll + cash DROP 54.37m to 40.82m + LT krediet 410.5m counterparties + capex 11.43m + aandeel % 9 gemeenten/OCMW/provincie/VL/private + dividend 6304; do not keep leftover woonmaatschappij as unpublished 39.36m housing shell,active,,tick1466; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Gemeenten>Deinze>Woonmaatschappij>Dimensa>JR2025_L5,{ENT},omzet 39356346 DROP vs 43540751 + diensten 14318019 + pers 7872133 102.5 VTE vs 103.6 + 1 VE + cash 40819167 DROP vs 54369441 + debt 443380246 LT krediet 410460664 + voorraden 26986164 onroerend 26761981 + capex 11428045 in aanbouw DROP 42801441 vs 76013335 + PnL DROP 2181013 vs 2725742 + dividend 6304 + commissaris 32000+1000 + aandeel % 9 gemeenten/OCMW/provincie/VL/private unpublished,Leftover woonmaatschappij Gent-Zuid after leftover AGB/APB hunt: omzet 39.36m DROP / pers 7.87m 102.5 VTE / debt 443.38m / cash DROP 40.82m / PnL DROP 2.18m / dividend 6304 / 1 VE hides municipal housing vehicle,8,Dimensa Woonmaatschappij / Bestuursorgaan / dagelijks bestuur,info@dimensa.be,Ravensteinstraat 12 9000 Gent,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1466 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF now extracted (15439739 bytes 47p). FOI ready not sent. NOT every-10. NOT Woonmaatschappij Rivierenland / Woonpunt Waas / Toerisme Limburg / Toerisme Vlaams-Brabant / Toerisme Oost-Vlaanderen / Arboretum Kalmthout / Kempens Landschap / Warande / De Schorre / PIH / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1465. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still no separate APB 2025 PDF.",
    ])
    print("foi_queue +1")

def part_rqstate():
    p = DATA / "research_queue.csv"
    with p.open("rb") as f:
        f.seek(0, 2)
        size = f.tell()
        f.seek(max(0, size - 131072))
        tail = f.read()
    if not tail.endswith(b"\\n"):
        raise SystemExit("research_queue tail missing newline")
    stripped = tail[:-1]
    last_nl = stripped.rfind(b"\\n")
    if last_nl < 0:
        raise SystemExit("research_queue tail too short")
    last = stripped[last_nl + 1 :]
    last_s = last.decode("utf-8")
    if not last_s.startswith("rq_1466,"):
        raise SystemExit(f"expected last row rq_1466, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1466 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1466,Dimensa Woonmaatschappij JR2025 leftover dual residual,hole_fill,5,done,L5,wm_dmsa,"
        "Completed: Dimensa Woonmaatschappij leftover woonmaatschappij of mined Gent-Zuid cities after leftover AGB/APB hunt; KBO 0400.067.887 Actief; live JR2025 official NBB WVV VOL-kap PDF (15439739 bytes 47p; deposit 2026-00138353; AV 26.05.2026; header 02.06.2026; pdfinfo 02.06.2026 13:08:57 UTC). PDF header Dimensa Woonmaatschappij / Ravensteinstraat 12 — NOT Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Sourced euros assets 633527939 omzet 39356346 diensten 14318019 pers 7872133 102.5 VTE pnl 2181013 equity 183607951 cash 40819167 debt 443380246 capex 11428045 dividend 6304. FOI "
        f"{GAP} ready not sent. Distinct from already-mined Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456.,"
        f"{GAP},2026-08-19T15:50:00Z,{TS},"
        "tick1466 Dimensa leftover woonmaatschappij residual; KBO 0400.067.887; live JR2025 official NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1467 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025"
    )
    spawn = (
        "rq_1467,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1466 done including Dimensa 1466 leftover woonmaatschappij live official NBB WVV / Woonmaatschappij Rivierenland 1465 leftover woonmaatschappij live official NBB WVV / Woonpunt Waas 1464 leftover woonmaatschappij live official NBB WVV / Toerisme Limburg 1463 leftover provincial tourism VZW live official NBB WVV / Toerisme Vlaams-Brabant 1462 leftover provincial tourism VZW live official NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 404 as of 1466). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck spotted unmined around 1453 — still no separate APB 2025 PDF as of 1466). Do NOT confuse with already-mined Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live. Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1466 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1466. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461.,,"
        f"{TS},{TS},"
        "spawned tick1466 after Dimensa leftover woonmaatschappij live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\\n" + spawn.encode("utf-8") + b"\\n")
    print("research_queue patched: rq_1466=done + rq_1467 spawned; keep", last_line_start)

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
    Path("/tmp/tick1466_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\\ncommitments={inv['commitments.csv']}\\nleaderboard={inv['leaderboard.csv']}\\nentities={inv['entities.csv']}\\nsources={inv['sources.csv']}\\nfoi_ready={foi_ready}\\nfoi_answered={foi_ans}\\nfoi_partial={foi_part}\\nfoi_total={foi_tot}\\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1466 Dimensa leftover woonmaatschappij residual; KBO 0400.067.887; live JR2025 official NBB WVV PDF; sourced euros assets 633527939 omzet 39356346 diensten 14318019 pers 7872133 102.5 VTE pnl 2181013 equity 183607951 cash 40819167 debt 443380246 capex 11428045 dividend 6304; FOI ready omzet 39.36m DROP / pers 7.87m 102.5 VTE / debt 443.38m / cash DROP 40.82m / PnL DROP 2.18m / dividend 6304 / 1 VE; NOT Woonmaatschappij Rivierenland / Woonpunt Waas / Toerisme Limburg / Toerisme Vlaams-Brabant / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1467 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\\n"
        f"main,continuous,hole_fill,{TS},rq_1466,1466,no,{notes}\\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1466")

    entry = (
        "\\n## Tick 1466 - 2026-08-19 - rq_1466 Dimensa Woonmaatschappij dual residual leftover\\n"
        "- Unit: Dimensa Woonmaatschappij BV (leftover woonmaatschappij / social-housing BV of mined Gent-Zuid cities Aalter + Deinze + Destelbergen + Gavere + Lievegem + Merelbeke-Melle + Nazareth-De Pinte + Sint-Martens-Latem + Zulte; 1 VE) after residual dual hunt (KBO **0400.067.887**; official NBB WVV VOL-kap PDF **15439739** bytes / 47p; deposit **2026-00138353**; AV **26.05.2026**; header **02.06.2026**; pdfinfo created **02.06.2026 13:08:57 UTC**; model **VOL-kap** 26.0.12 m02-f-p; commissaris EY bedrijfsrevisoren BV B00160 / 0446.334.711 mandate 27.05.2025–31.05.2028 fee **32000** + andere controle **1000**; voorzitter Mario Pauwels). Leftover AGB/APB first: leftover APB Inovant / Atlas Foleon `jaarrekening_25_inov` / `jaarrekening_25_atlas` HEAD **404** this tick; provincieantwerpen.be **403** even with Googlebot UA; no fetchable 2025 Inovant/Atlas PDF (do not take Hooibeekhoeve). Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick. Leftover AGB Herzele already in entities (tick1163) — skipped. Leftover AGB Bornem still 2024. Leftover AGB Hasselt / SOLag / WAGSO / Temse / Herk / Lommel already in entities — skipped. Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel still no JR as of 1465. Leftover IGS IVAREM 0267.403.264 last JR still 2024-12-31. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover Dimensa statutory CDN `2026-00138353` live this tick (HTTP 200 / 15439739 / 47p; jaar **2025-12-31**; neerlegging **02.06.2026**) — taken (hunt order #2 leftover unmined woonmaatschappij of mined Gent-Zuid cities with live 2025 statutory PDF after leftover AGB/APB hunt). PDF header **Dimensa Woonmaatschappij / Ravensteinstraat 12 / 9000 Gent** — NOT Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Distinct from already-mined **Woonmaatschappij Rivierenland 1465** / **Woonpunt Waas 1464** / **Toerisme Limburg 1463** / **Toerisme Vlaams-Brabant 1462** / **Toerisme Oost-Vlaanderen 1461** / **Arboretum Kalmthout 1460** / **Kempens Landschap 1459** / **APB Warande 1458** / **APB De Schorre 1457** / **APB PIH 1456**. First confirmed not already extracted as JR2025 euros: no Dimensa / 0400.067.887 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **03.01.1928**; statutaire naam Dimensa Woonmaatschappij since 30.05.2023; BV since 30.06.2022; zetel Ravensteinstraat 12 9000 Gent; **1 VE**; 19 functiehouders; dagelijks bestuur Adams/Rousseaux/Vercruyssen since 27.05.2025; Werkgever RSZ since 01.01.1945; btw since 01.03.1995; aanbestedende overheid; NACE 41.001 / 68.203 / 68.202; site https://www.dimensa.be/; absorbeerde GMKL Het Volk 0400.067.590 + HABITARE+ 0400.189.831 since 30.06.2022. Prior-year figures **identiek**. NBB consult used for deposit-id discovery only. Euros extracted from the official VOL-kap deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1470).\\n"
        "- EUR strong (primary official WVV VOL-kap; omzet 70 **39356346** DROP vs 43540751; diensten 61 **14318019**; pers 62 **7872133** / **102,5 VTE** vs 103,6): assets **633527939** (was 645505336); fixed **557792269** vs 563339200 / IVA **303077** vs 223860 / MVA **557456115** vs 563082263 (terreinen/gebouwen **513023752**; installaties **121045**; meubilair **367987**; leasing **1132600**; overige **9290**; in aanbouw **42801441 DROP** vs 76013335) / FVA **33077**; current **75735670** vs 82166136; voorraden **26986164** (onroerend verkoop **26761981**); ST recv **2675513** (trade **838861** / other **1836652**); LT recv **1194720**; geldbeleg empty; cash **40819167 DROP** vs 54369441; prepaid **4060106**; equity **183607951** vs 182717464 (inbreng **158056**; reserves **140111372**; overgedragen empty; kapsubs **43338523**); voorzieningen **6539742** (grote herstellingen **3377181**; uitgestelde belasting **2313569**); schulden **443380246** vs 455387570 (LT **415590032** waarvan fin krediet **410460664**; ST **23677378** waarvan 42 **17866003** + leveranciers **557723 DROP** vs 2299242; deferred **4112836**); omzet **39356346** DROP vs 43540751; 60 **2030307**; diensten **14318019**; pers **7872133** / **102,5 VTE** / 133033 uur / YE **111** vs 114 / interim **2,0 VTE** 112423; afschr **16301111**; expl **+1537108 DROP** vs +2393124; fin opbr **9566997**; fin kosten **8893328**; tax **99492**; PnL **+2181013 DROP** vs +2725742; dividend **6304**; toevoeging reserves **2174709**; capex MVA aanschaf **11428045** (terreinen 8102152 + install 40524 + meubilair 116338 + in aanbouw 3169031) + IVA 152626. Commissaris fee **32000** + 1000. 1 VE. 17628 aandelen; niet-opgevraagd 96155 (gemeenten 71449 / private 8879 / provincie OV 8105 / VL 7722). Cross-checks: 557792269+75735670=633527939; 183607951+6539742+443380246=633527939; 44514981-42977873=1537108; 1537108+9566997-8893328=2210777; 2210777+69728-99492=2181013; 2181013-6304=2174709.\\n"
        "- CSVs: sources +4; entities +1 `wm_dmsa` parent `city_deinze`; budgets +42 executed; commitments +1 envelope 39356346 AV 26.05.2026; leaderboard +1 annual 39356346 / total 633527939; foi_queue +1 status=ready never sent; research_queue surgical rq_1466=done + rq_1467 spawn; loop_state ticks_completed=1466. Inventory after write: budgets {INV_B} · commitments {INV_C} · leaderboard {INV_L} · entities {INV_E} · sources {INV_S} · FOI ready {FOI_R} / answered {FOI_A} / partial {FOI_P} / total {FOI_T}.\\n"
        "- FOI: `gap_dmsa_omzet_39_36m_pers_7_87m_debt_443m_l5` ready not sent — omzet 39.36m DROP / diensten 14.32m / pers 7.87m 102.5 VTE / 1 VE / cash DROP 40.82m / debt 443.38m LT krediet 410.5m / voorraden 26.99m / capex 11.43m / PnL DROP 2.18m / dividend 6304 / commissaris 33k / aandeel % 9 gemeenten/OCMW/provincie/VL/private unpublished.\\n"
        "- Next: rq_1467 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 404 this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1466). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live. Leftover IGS IVAREM **0267.403.264** still JR2024. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Stichting Kempens Landschap 1459 / APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456. Next every-10 is **1470**. Provincial tourism VZWs now exhausted (Westtoer + TOV + TVLB + TLim).\\n"
    )
    entry = entry.replace("{INV_B}", str(inv["budgets.csv"])).replace("{INV_C}", str(inv["commitments.csv"])).replace("{INV_L}", str(inv["leaderboard.csv"])).replace("{INV_E}", str(inv["entities.csv"])).replace("{INV_S}", str(inv["sources.csv"])).replace("{FOI_R}", str(foi_ready)).replace("{FOI_A}", str(foi_ans)).replace("{FOI_P}", str(foi_part)).replace("{FOI_T}", str(foi_tot))
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\\n"):
        lraw += b"\\n"
    if b"## Tick 1466 -" in lraw:
        raise SystemExit("loop_log already has tick 1466 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1466")
    print("DONE tick 1466")

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

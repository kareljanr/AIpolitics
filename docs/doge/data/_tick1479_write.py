#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1479 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T18:25:00Z"
ENT = "wm_wmva"
SRC = "src_wmva_jr2025_nbb"
GAP = "gap_wmva_omzet_18_31m_pers_3_26m_debt_288m_l5"
LB = "lb_wmva_omzet_18_31m_pers_3_26m_debt_288m"
COMM = "comm_wmva_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00215629.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Woonmaatschappij Vlaamse Ardennen official NBB WVV VOL-inb JR2025,{PDF},NBB / Woonmaatschappij Vlaamse Ardennen,2026-08-19,budget,tick1479; official NBB WVV VOL-inb JR2025 PDF 61p / 2275223 bytes; deposit 2026-00215629; AV 02.06.2026; header 29.06.2026; pdfinfo created 29.06.2026 22:54:18 UTC; model VOL-inb 23.0.10 m82-f; KBO 0466.370.951; assets 350865381 cash 13566516 debt 288205501 pers 3257566 omzet 18305499 pnl 193992 equity 56746168",
        "src_wmva_site,Woonmaatschappij Vlaamse Ardennen official pages,https://wmvla.be/,Woonmaatschappij Vlaamse Ardennen / mined Oudenaarde + Ronse + Zottegem + Herzele + Brakel + Kluisbergen + Kruisem + Lierde + Sint-Lievens-Houtem + Horebeke,2026-08-19,official_register,tick1479; leftover woonmaatschappij of mined Vlaamse Ardennen; zetel Sint-Jozefsplein 18 9700 Oudenaarde; KBO 0466.370.951; SBM used for deposit-id discovery only",
        "src_kbo_wmva_0466370951,KBO Woonmaatschappij Vlaamse Ardennen 0466.370.951,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0466370951,KBO Public Search FOD Economie,2026-08-19,official_register,tick1479; Actief since 01.07.1999; BV since 30.09.2021; naam Woonmaatschappij Vlaamse Ardennen since 06.12.2022; zetel Sint-Jozefsplein 18 9700 Oudenaarde; 1 VE; 31 functiehouders; Werkgever RSZ since 01.07.1999; aanbestedende overheid",
        "src_wmva_foi_contact,Woonmaatschappij Vlaamse Ardennen FOI channel (info@wmvla.be),https://wmvla.be/,Woonmaatschappij Vlaamse Ardennen,2026-08-19,official_register,tick1479; leftover woonmaatschappij of mined Oudenaarde + Ronse + Zottegem + Herzele + Brakel + Kluisbergen + Kruisem + Lierde + Sint-Lievens-Houtem + Horebeke; NOT RL Vlaamse Ardennen 1437 / SOLVA / Woonboog / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92 / leftover LeefGoed",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_wmva," in raw or raw.startswith(b"wm_wmva,"):
        raise SystemExit("wm_wmva already present")
    if b"0466.370.951" in raw or b"0466370951" in raw:
        raise SystemExit("Woonmaatschappij Vlaamse Ardennen KBO already present as entity")
    row = (
        "wm_wmva,Woonmaatschappij Vlaamse Ardennen (leftover woonmaatschappij / social-housing BV of mined Oudenaarde + Ronse + Zottegem + Herzele + Brakel + Kluisbergen + Kruisem + Lierde + Sint-Lievens-Houtem + Horebeke / Vlaamse Ardennen; NOT RL Vlaamse Ardennen 1437 / SOLVA / Woonboog 1478 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92 / leftover LeefGoed-Zonnige Kempen),"
        "Woonmaatschappij Vlaamse Ardennen SRL (logement social residuel Ardennes flamandes),"
        "Woonmaatschappij Vlaamse Ardennen leftover social-housing company of mined Oudenaarde + Ronse + Zottegem + Herzele + Brakel + Kluisbergen + Kruisem + Lierde + Sint-Lievens-Houtem + Horebeke (not RL Vlaamse Ardennen / SOLVA / Woonboog / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92 / leftover LeefGoed),"
        "other,city_oudenaarde,nl,https://wmvla.be/,info@wmvla.be,Sint-Jozefsplein 18 9700 Oudenaarde,"
        "tick1479 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0466.370.951 Actief since 01.07.1999; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 350865381 omzet 18305499 pers 3257566 37.7 VTE pnl 193992 equity 56746168 cash 13566516 debt 288205501 capex 30109817 dividend 2990; FOI ready omzet 18.31m DROP / pers 3.26m 37.7 VTE / debt 288.21m / cash 13.57m JUMP / PnL DROP 0.19m / dividend 2990 / 1 VE; distinct from already-mined Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / RL Vlaamse Ardennen 1437 / SOLVA"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_wmva")

def part_budgets():
    BUDGETS = [
        ("bud_wmva_assets_2025", "2025", "350865381", "2025 assets 350865381 UP (was 327644239); tick1479; primary official NBB WVV VOL-inb 2026-00215629"),
        ("bud_wmva_current_2025", "2025", "27791402", "2025 vlottend 27791402 UP (was 24587400); tick1479; primary official NBB WVV"),
        ("bud_wmva_cash_2025", "2025", "13566516", "2025 liquide middelen 13566516 JUMP (was 10084417); tick1479; primary official NBB WVV"),
        ("bud_wmva_strecv_2025", "2025", "2536419", "2025 ST vorderingen 2536419 (was 3536560); tick1479; primary official NBB WVV"),
        ("bud_wmva_trade_2025", "2025", "565469", "2025 handelsvorderingen 565469 (was 500118); tick1479; primary official NBB WVV"),
        ("bud_wmva_othrecv_2025", "2025", "1970949", "2025 overige ST vorderingen 1970949 (was 3036442); tick1479; primary official NBB WVV"),
        ("bud_wmva_voorraden_2025", "2025", "9546609", "2025 voorraden 9546609 (was 9002999); tick1479; primary official NBB WVV"),
        ("bud_wmva_prepaid_2025", "2025", "2141858", "2025 overlopend actief 2141858 (was 1963424); tick1479; primary official NBB WVV"),
        ("bud_wmva_fixed_2025", "2025", "323073979", "2025 vaste activa 323073979 (was 303056839); tick1479; primary official NBB WVV"),
        ("bud_wmva_iva_2025", "2025", "7516", "2025 IVA 7516 (was 10185); tick1479; primary official NBB WVV"),
        ("bud_wmva_mva_2025", "2025", "322985940", "2025 MVA 322985940 (was 302966427; terreinen/gebouwen 283158011 meubilair 232352 overige 677174 in aanbouw 38918403); tick1479; primary official NBB WVV"),
        ("bud_wmva_fva_2025", "2025", "80524", "2025 FVA 80524 (was 80226); tick1479; primary official NBB WVV"),
        ("bud_wmva_equity_2025", "2025", "56746168", "2025 eigen vermogen 56746168 UP (was 54500174); tick1479; primary official NBB WVV"),
        ("bud_wmva_inbreng_2025", "2025", "74749", "2025 inbreng 74749 (onbeschikbaar 74749); tick1479; primary official NBB WVV"),
        ("bud_wmva_reserves_2025", "2025", "31919850", "2025 reserves 31919850 (was 31728848); tick1479; primary official NBB WVV"),
        ("bud_wmva_kapsubs_2025", "2025", "24751570", "2025 kapitaalsubsidies 24751570 UP (was 22696290); tick1479; primary official NBB WVV"),
        ("bud_wmva_voorz_2025", "2025", "5913712", "2025 voorzieningen+uitgestelde belasting 5913712 (herstel 4559482); tick1479; primary official NBB WVV"),
        ("bud_wmva_debt_2025", "2025", "288205501", "2025 schulden 288205501 JUMP (was 266677708); tick1479; primary official NBB WVV"),
        ("bud_wmva_ltdebt_2025", "2025", "263780342", "2025 LT schulden 263780342 (was 247389917; fin krediet 261344634); tick1479; primary official NBB WVV"),
        ("bud_wmva_stdebt_2025", "2025", "22335753", "2025 ST schulden 22335753 (42 16891787 + leveranciers 3420617); tick1479; primary official NBB WVV"),
        ("bud_wmva_lev_2025", "2025", "3420617", "2025 leveranciers 3420617 (was 2707611); tick1479; primary official NBB WVV"),
        ("bud_wmva_bezold_2025", "2025", "431471", "2025 bezoldigingen-schulden 431471 (was 286198); tick1479; primary official NBB WVV"),
        ("bud_wmva_taxpay_2025", "2025", "1138414", "2025 belastingschulden 1138414 (was 719053); tick1479; primary official NBB WVV"),
        ("bud_wmva_deferred_2025", "2025", "2089406", "2025 overlopend passief 2089406 (was 1602807); tick1479; primary official NBB WVV"),
        ("bud_wmva_omzet_2025", "2025", "18305499", "2025 omzet 70 18305499 DROP (was 21922765; verhuur/verkoop split unpublished); tick1479; primary official NBB WVV"),
        ("bud_wmva_diensten_2025", "2025", "6633062", "2025 diensten 61 6633062 JUMP (was 5722207); tick1479; primary official NBB WVV"),
        ("bud_wmva_pers_2025", "2025", "3257566", "2025 pers 62 3257566; 37.7 VTE vs 34.9; 52746 uur; YE 44 / 41.5 VTE; tick1479; primary official NBB WVV"),
        ("bud_wmva_afschr_2025", "2025", "7664923", "2025 afschrijvingen 7664923; tick1479; primary official NBB WVV"),
        ("bud_wmva_expl_2025", "2025", "3680701", "2025 bedrijfswinst 3680701 DROP (was 3757245); tick1479; primary official NBB WVV"),
        ("bud_wmva_finopbr_2025", "2025", "2334467", "2025 financiele opbrengsten 2334467 (interestsubs 1503428); tick1479; primary official NBB WVV"),
        ("bud_wmva_finkost_2025", "2025", "5859550", "2025 financiele kosten 5859550; tick1479; primary official NBB WVV"),
        ("bud_wmva_pnl_2025", "2025", "193992", "2025 PnL 193992 DROP (was 266925); tick1479; primary official NBB WVV"),
        ("bud_wmva_div_2025", "2025", "2990", "2025 dividend 2990 vergoeding van de inbreng; tick1479; primary official NBB WVV"),
        ("bud_wmva_capex_2025", "2025", "30109817", "2025 capex MVA aanschaf 30109817 (terreinen 3359132 meubilair 144219 overige 4038 in aanbouw 26602428); tick1479; primary official NBB WVV"),
        ("bud_wmva_in_aanbouw_2025", "2025", "38918403", "2025 activa in aanbouw 38918403 DROP (was 39097068); tick1479; primary official NBB WVV"),
        ("bud_wmva_krediet_2025", "2025", "261344634", "2025 LT kredietinstellingen 261344634 (was 245138504); tick1479; primary official NBB WVV"),
        ("bud_wmva_terreinen_2025", "2025", "283158011", "2025 terreinen en gebouwen 283158011 (was 262076536); tick1479; primary official NBB WVV"),
        ("bud_wmva_herstel_2025", "2025", "4559482", "2025 voorziening grote herstellingen 4559482 (was 5216070); tick1479; primary official NBB WVV"),
        ("bud_wmva_commissaris_2025", "2025", "9749", "2025 commissaris fee 9749 Debrabandere - Van Brabandt BV + extra controle 5253; tick1479; primary official NBB WVV"),
        ("bud_wmva_tax_2025", "2025", "308", "2025 belastingen op het resultaat 308; tick1479; primary official NBB WVV"),
        ("bud_wmva_andere_expl_2025", "2025", "1299048", "2025 andere bedrijfskosten 1299048; tick1479; primary official NBB WVV"),
        ("bud_wmva_interestsubs_2025", "2025", "1503428", "2025 interestsubsidies 1503428 (was 1261302); tick1479; primary official NBB WVV 6.11"),
        ("bud_wmva_explsubs_2025", "2025", "3828960", "2025 exploitatiesubsidies 3828960 (was 3920480); tick1479; primary official NBB WVV 6.10"),
        ("bud_wmva_herstel_drop_2025", "2025", "4559482", "2025 herstelvoorziening 4559482 DROP vs 5216070; tick1479; primary official NBB WVV"),
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
        f"{COMM},Woonmaatschappij Vlaamse Ardennen JR2025 leftover woonmaatschappij dual (omzet 18.31m DROP / pers 3.26m 37.7 VTE / debt 288.21m / cash 13.57m JUMP / PnL DROP 0.19m / dividend 2990 / 1 VE),{ENT},Oudenaarde-Ronse-Zottegem / mined Vlaamse Ardennen dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-06-02,1999,,18305499,,,active,{PDF},Local leftover woonmaatschappij map VL Vlaamse Ardennen — omzet 18.31m DROP / pers 3.26m 37.7 VTE / debt 288.21m / cash 13.57m JUMP,Publish omzet+diensten+verhuur/verkoop split + 1 VE payroll + cash 13.57m JUMP + LT krediet 261.34m counterparties + capex 30.11m + aandeel % Oudenaarde/Ronse/Zottegem/Herzele/Brakel + dividend 2990; do not keep leftover woonmaatschappij as unpublished 18.31m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Oudenaarde>Woonmaatschappij>Woonmaatschappij_Vlaamse_Ardennen>JR2025_L5,tick1479; assets 350865381 omzet 18305499 pers 3257566 pnl 193992 equity 56746168 cash 13566516 debt 288205501 capex 30109817 dividend 2990; FOI ready not sent; not TE-additive of 348bn; NOT RL Vlaamse Ardennen / SOLVA / Woonboog / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92 / leftover LeefGoed",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Woonmaatschappij Vlaamse Ardennen JR2025 leftover woonmaatschappij: omzet 18.31m DROP / pers 3.26m 37.7 VTE / debt 288.21m / cash 13.57m JUMP / PnL DROP 0.19m / dividend 2990 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Oudenaarde>Woonmaatschappij>Woonmaatschappij_Vlaamse_Ardennen>JR2025_L5,18305499,350865381,Leftover dual woonmaatschappij shell: assets 350.87m / equity 56.75m / omzet 18.31m DROP / pers 3.26m 37.7 VTE / cash 13.57m JUMP / debt 288.21m / LT krediet 261.34m / PnL DROP 0.19m / dividend 2990 / 1 VE; do not treat 18.31m as TE-additive of 348bn,strong,{SRC},Woonmaatschappij Vlaamse Ardennen / mined Oudenaarde-Ronse-Zottegem dual housing,Local leftover woonmaatschappij map VL Vlaamse Ardennen — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 18.31m DROP / pers 3.26m 37.7 VTE / debt 288.21m / cash 13.57m JUMP / PnL DROP 0.19m / dividend 2990 / 1 VE,7.0,8.0,3.0,7.0,Publish omzet+diensten+verhuur/verkoop split + 1 VE payroll + cash 13.57m JUMP + LT krediet 261.34m counterparties + capex 30.11m + aandeel % Oudenaarde/Ronse/Zottegem/Herzele/Brakel + dividend 2990; do not keep leftover woonmaatschappij as unpublished 18.31m housing shell,active,,tick1479; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / RL Vlaamse Ardennen 1437 / SOLVA",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Gemeenten>Oudenaarde>Woonmaatschappij>Woonmaatschappij_Vlaamse_Ardennen>JR2025_L5,{ENT},omzet 18305499 DROP vs 21922765 + diensten 6633062 JUMP vs 5722207 + pers 3257566 37.7 VTE vs 34.9 + 1 VE + cash 13566516 JUMP vs 10084417 + debt 288205501 LT krediet 261344634 + voorraden 9546609 + capex 30109817 + PnL DROP 193992 vs 266925 + dividend 2990 + commissaris 9749 + extra 5253 + 6.16 bestuurders empty + aandeel % Oudenaarde/Ronse/Zottegem/Herzele/Brakel unpublished,Leftover woonmaatschappij Woonmaatschappij Vlaamse Ardennen after leftover AGB/APB hunt: omzet 18.31m DROP / pers 3.26m 37.7 VTE / debt 288.21m / cash 13.57m JUMP / PnL DROP 0.19m / dividend 2990 / 1 VE hides municipal housing vehicle,8,Woonmaatschappij Vlaamse Ardennen / Bestuursorgaan / voorzitter Vercamer Stefaan,info@wmvla.be,Sint-Jozefsplein 18 9700 Oudenaarde,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1479 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (2275223 bytes 61p). FOI ready not sent. NOT every-10. NOT RL Vlaamse Ardennen 1437 / SOLVA / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404/403 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still no separate APB 2025 PDF. WoonST Temse still JR2024 as of 1467. stek92 still JR2024 as of 1473. Leftover LeefGoed Zonnige Kempen still JR2024 as of 1478. Woonmaatschappij Vlaamse Ardennen TAKEN this tick.",
    ])
    print("foi_queue +1")

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

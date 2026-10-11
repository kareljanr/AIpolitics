#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1476 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T17:45:00Z"
ENT = "wm_wkdr"
SRC = "src_wkdr_jr2025_nbb"
GAP = "gap_wkdr_omzet_10_29m_pers_3_03m_loss_2_37m_l5"
LB = "lb_wkdr_omzet_10_29m_pers_3_03m_loss_2_37m"
COMM = "comm_wkdr_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00140460.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Woonkade Rupelstreek official NBB WVV VOL-inb JR2025,{PDF},NBB / Woonkade Rupelstreek,2026-08-19,budget,tick1476; official NBB WVV VOL-inb JR2025 PDF 61p / 2176655 bytes; deposit 2026-00140460; AV 02.06.2026; header 03.06.2026; pdfinfo created 06.06.2026 01:02:43 UTC; model VOL-inb 26.0.12 m82-f; KBO 0452.753.537; assets 159099064 cash 1837328 debt 139739427 pers 3032421 omzet 10288580 diensten 4211680 pnl -2373789 equity 18271109",
        "src_wkdr_site,Woonkade Rupelstreek official pages,https://woonkade.be/,Woonkade Rupelstreek / mined Boom-Rupelstreek,2026-08-19,official_register,tick1476; leftover woonmaatschappij of mined Boom + Hemiksem + Niel + Rumst + Schelle; zetel Uitbreidingsstraat 39 2850 Boom; KBO 0452.753.537; SBM used for deposit-id discovery only",
        "src_kbo_wkdr_0452753537,KBO Woonkade Rupelstreek 0452.753.537,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0452753537,KBO Public Search FOD Economie,2026-08-19,official_register,tick1476; Actief since 25.05.1994; BV since 22.06.2023; naam WOONKADE RUPELSTREEK since 22.06.2023; zetel Uitbreidingsstraat 39 2850 Boom; 1 VE; 16 functiehouders; Werkgever RSZ since 25.05.1994; aanbestedende overheid",
        "src_wkdr_foi_contact,Woonkade Rupelstreek FOI channel (jan@woonkade.be),https://woonkade.be/,Woonkade Rupelstreek,2026-08-19,official_register,tick1476; leftover woonmaatschappij of mined Boom-Rupelstreek; NOT Erfgoed Rupelstreek IOED 1431 / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / leftover Woonveer / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_wkdr," in raw or raw.startswith(b"wm_wkdr,"):
        raise SystemExit("wm_wkdr already present")
    if b"0452.753.537" in raw or b"0452753537" in raw:
        raise SystemExit("Woonkade KBO already present as entity")
    row = (
        "wm_wkdr,Woonkade Rupelstreek (leftover woonmaatschappij / social-housing BV of mined Boom + Hemiksem + Niel + Rumst + Schelle; NOT Erfgoed Rupelstreek IOED 1431 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / leftover Woonveer / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92),"
        "Woonkade Rupelstreek SRL (logement social residuel Boom-Rupelstreek),"
        "Woonkade Rupelstreek leftover social-housing company of mined Boom-Rupelstreek (not Erfgoed Rupelstreek IOED / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / leftover Woonveer / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92),"
        "other,city_boom,nl,https://woonkade.be/,jan@woonkade.be,Uitbreidingsstraat 39 2850 Boom,"
        "tick1476 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0452.753.537 Actief since 25.05.1994; live JR2025 official NBB WVV PDF; sourced euros assets 159099064 omzet 10288580 diensten 4211680 pers 3032421 36.9 VTE pnl -2373789 equity 18271109 cash 1837328 debt 139739427 capex 13308629 dividend 0; FOI ready omzet 10.29m DROP / pers 3.03m 36.9 VTE / debt 139.74m / cash 1.84m DROP / PnL LOSS 2.37m / dividend 0 / 1 VE; distinct from already-mined Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Erfgoed Rupelstreek IOED 1431"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_wkdr")

def part_budgets():
    BUDGETS = [
        ("bud_wkdr_assets_2025", "2025", "159099064", "2025 assets 159099064 UP (was 153904629); tick1476; primary official NBB WVV VOL-inb 2026-00140460"),
        ("bud_wkdr_current_2025", "2025", "4857804", "2025 vlottend 4857804 DROP (was 8360808); tick1476; primary official NBB WVV"),
        ("bud_wkdr_cash_2025", "2025", "1837328", "2025 liquide middelen 1837328 DROP (was 5145025); tick1476; primary official NBB WVV"),
        ("bud_wkdr_strecv_2025", "2025", "296836", "2025 ST vorderingen 296836 (was 507634); tick1476; primary official NBB WVV"),
        ("bud_wkdr_trade_2025", "2025", "281970", "2025 handelsvorderingen 281970 (was 451911); tick1476; primary official NBB WVV"),
        ("bud_wkdr_othrecv_2025", "2025", "14866", "2025 overige ST vorderingen 14866 (was 55723); tick1476; primary official NBB WVV"),
        ("bud_wkdr_voorraden_2025", "2025", "1408274", "2025 voorraden 1408274 (onroerend verkoop 1369922); tick1476; primary official NBB WVV"),
        ("bud_wkdr_prepaid_2025", "2025", "1311367", "2025 overlopend actief 1311367 (was 1200578); tick1476; primary official NBB WVV"),
        ("bud_wkdr_geldbeleg_2025", "2025", "4000", "2025 geldbeleggingen 4000; tick1476; primary official NBB WVV"),
        ("bud_wkdr_fixed_2025", "2025", "154241260", "2025 vaste activa 154241260 (was 145543820); tick1476; primary official NBB WVV"),
        ("bud_wkdr_iva_2025", "2025", "8450", "2025 IVA 8450 (was 13458); tick1476; primary official NBB WVV"),
        ("bud_wkdr_mva_2025", "2025", "154120562", "2025 MVA 154120562 (was 145435952; terreinen/gebouwen 129126383 in aanbouw 24592909); tick1476; primary official NBB WVV"),
        ("bud_wkdr_fva_2025", "2025", "112247", "2025 FVA 112247 (aandelen 100766 borg 11482); tick1476; primary official NBB WVV"),
        ("bud_wkdr_equity_2025", "2025", "18271109", "2025 eigen vermogen 18271109 DROP (was 20944487); tick1476; primary official NBB WVV"),
        ("bud_wkdr_inbreng_2025", "2025", "54906", "2025 inbreng 54906 (beschikbaar 54906); tick1476; primary official NBB WVV"),
        ("bud_wkdr_reserves_2025", "2025", "11304327", "2025 reserves 11304327 (was 11486608); tick1476; primary official NBB WVV"),
        ("bud_wkdr_kapsubs_2025", "2025", "8798185", "2025 kapitaalsubsidies 8798185 DROP (was 9097077); tick1476; primary official NBB WVV"),
        ("bud_wkdr_voorz_2025", "2025", "1088528", "2025 voorzieningen+uitgestelde belasting 1088528 (claim 310000); tick1476; primary official NBB WVV"),
        ("bud_wkdr_debt_2025", "2025", "139739427", "2025 schulden 139739427 JUMP (was 132155590); tick1476; primary official NBB WVV"),
        ("bud_wkdr_ltdebt_2025", "2025", "130918132", "2025 LT schulden 130918132 (was 121745770; fin krediet 129372104); tick1476; primary official NBB WVV"),
        ("bud_wkdr_stdebt_2025", "2025", "7916437", "2025 ST schulden 7916437 (was 9078190); tick1476; primary official NBB WVV"),
        ("bud_wkdr_lev_2025", "2025", "901554", "2025 leveranciers 901554 (was 864582); tick1476; primary official NBB WVV"),
        ("bud_wkdr_bezold_2025", "2025", "389065", "2025 bezoldigingen-schulden 389065 (was 418748); tick1476; primary official NBB WVV"),
        ("bud_wkdr_taxpay_2025", "2025", "841599", "2025 belastingschulden 841599 (was 781909); tick1476; primary official NBB WVV"),
        ("bud_wkdr_deferred_2025", "2025", "904858", "2025 overlopend passief 904858 (was 1331631); tick1476; primary official NBB WVV"),
        ("bud_wkdr_omzet_2025", "2025", "10288580", "2025 omzet 70 10288580 DROP (was 10500673); tick1476; primary official NBB WVV"),
        ("bud_wkdr_diensten_2025", "2025", "4211680", "2025 diensten 61 4211680 JUMP (was 3931696); tick1476; primary official NBB WVV"),
        ("bud_wkdr_aankopen_2025", "2025", "151838", "2025 handelsgoederen/grondstoffen 60 151838; tick1476; primary official NBB WVV"),
        ("bud_wkdr_pers_2025", "2025", "3032421", "2025 pers 62 3032421; 36.9 VTE vs 36.2; 51082 uur; YE 36 / 34.7 VTE; tick1476; primary official NBB WVV"),
        ("bud_wkdr_afschr_2025", "2025", "4645450", "2025 afschrijvingen 4645450; tick1476; primary official NBB WVV"),
        ("bud_wkdr_expl_2025", "2025", "-1828674", "2025 bedrijfsverlies -1828674 (was -354357); tick1476; primary official NBB WVV"),
        ("bud_wkdr_finopbr_2025", "2025", "2645598", "2025 financiele opbrengsten 2645598 (interestsubs 2312426); tick1476; primary official NBB WVV"),
        ("bud_wkdr_finkost_2025", "2025", "3216737", "2025 financiele kosten 3216737; tick1476; primary official NBB WVV"),
        ("bud_wkdr_pnl_2025", "2025", "-2373789", "2025 PnL -2373789 LOSS (was -880277); tick1476; primary official NBB WVV"),
        ("bud_wkdr_div_2025", "2025", "0", "2025 dividend 0 vergoeding van de inbreng empty; tick1476; primary official NBB WVV"),
        ("bud_wkdr_capex_2025", "2025", "13308629", "2025 capex MVA aanschaf 13308629 (meubilair 27267 + in aanbouw 13281362); tick1476; primary official NBB WVV"),
        ("bud_wkdr_bedrijfsopbr_2025", "2025", "11637610", "2025 bedrijfsopbrengsten 70/76A 11637610; tick1476; primary official NBB WVV"),
        ("bud_wkdr_bedrijfskost_2025", "2025", "13466284", "2025 bedrijfskosten 60/66A 13466284; tick1476; primary official NBB WVV"),
        ("bud_wkdr_in_aanbouw_2025", "2025", "24592909", "2025 activa in aanbouw 24592909 JUMP (was 16733281); tick1476; primary official NBB WVV"),
        ("bud_wkdr_krediet_2025", "2025", "129372104", "2025 LT kredietinstellingen 129372104 JUMP (was 120225235); tick1476; primary official NBB WVV"),
        ("bud_wkdr_terreinen_2025", "2025", "129126383", "2025 terreinen en gebouwen 129126383 (was 128235850); tick1476; primary official NBB WVV"),
        ("bud_wkdr_interim_2025", "2025", "144200", "2025 interim 1.5 VTE kosten 144200; tick1476; primary official NBB WVV"),
        ("bud_wkdr_explsubs_2025", "2025", "814615", "2025 6.10 exploitatiesubsidies 814615 (was 1122448); tick1476; primary official NBB WVV"),
        ("bud_wkdr_claim_2025", "2025", "310000", "2025 voorziening claim 310000; tick1476; primary official NBB WVV"),
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
        f"{COMM},Woonkade Rupelstreek JR2025 leftover woonmaatschappij dual (omzet 10.29m DROP / diensten 4.21m JUMP / pers 3.03m 36.9 VTE / debt 139.74m / cash 1.84m DROP / PnL LOSS 2.37m / dividend 0 / 1 VE),{ENT},Boom-Rupelstreek / mined Boom dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-06-02,1994,,10288580,,,active,{PDF},Local leftover woonmaatschappij map VL Boom-Rupelstreek — omzet 10.29m DROP / pers 3.03m 36.9 VTE / debt 139.74m / cash 1.84m DROP,Publish omzet split + 1 VE payroll + cash 1.84m DROP + LT krediet 129.37m counterparties + capex 13.31m + aandeel % Boom/Hemiksem/Niel/Rumst/Schelle/OCMW/private + dividend 0; do not keep leftover woonmaatschappij as unpublished 10.29m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Boom>Woonmaatschappij>Woonkade>JR2025_L5,tick1476; assets 159099064 omzet 10288580 diensten 4211680 pers 3032421 pnl -2373789 equity 18271109 cash 1837328 debt 139739427 capex 13308629 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT Erfgoed Rupelstreek IOED / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / leftover Woonveer / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof / leftover WoonST / leftover stek92",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},Woonkade Rupelstreek JR2025 leftover woonmaatschappij: omzet 10.29m DROP / diensten 4.21m JUMP / pers 3.03m 36.9 VTE / debt 139.74m / cash 1.84m DROP / PnL LOSS 2.37m / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Boom>Woonmaatschappij>Woonkade>JR2025_L5,10288580,159099064,Leftover dual woonmaatschappij shell: assets 159.10m / equity 18.27m / omzet 10.29m DROP / diensten 4.21m JUMP / pers 3.03m 36.9 VTE / cash 1.84m DROP / debt 139.74m / LT krediet 129.37m / PnL LOSS 2.37m / dividend 0 / 1 VE; do not treat 10.29m as TE-additive of 348bn,strong,{SRC},Woonkade Rupelstreek / mined Boom-Rupelstreek dual housing,Local leftover woonmaatschappij map VL Boom-Rupelstreek — JR2025 official NBB WVV live; omzet+pers+debt+cash+loss FOI,Official NBB WVV 2026-08-19: omzet 10.29m DROP / pers 3.03m 36.9 VTE / debt 139.74m / cash 1.84m DROP / PnL LOSS 2.37m / dividend 0 / 1 VE,7.0,7.0,3.0,7.0,Publish omzet split + 1 VE payroll + cash 1.84m DROP + LT krediet 129.37m counterparties + capex 13.31m + aandeel % Boom/Hemiksem/Niel/Rumst/Schelle/OCMW/private + dividend 0; do not keep leftover woonmaatschappij as unpublished 10.29m housing shell,active,,tick1476; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Erfgoed Rupelstreek IOED 1431",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Gemeenten>Boom>Woonmaatschappij>Woonkade>JR2025_L5,{ENT},omzet 10288580 DROP vs 10500673 + diensten 4211680 JUMP vs 3931696 + pers 3032421 36.9 VTE vs 36.2 + 1 VE + cash 1837328 DROP vs 5145025 + debt 139739427 LT krediet 129372104 + voorraden 1408274 + capex 13308629 in aanbouw aanschaf 13281362 + PnL LOSS -2373789 vs -880277 + dividend 0 + commissaris 15000 + bestuurders unpublished + aandeel % Boom/Hemiksem/Niel/Rumst/Schelle/OCMW/private unpublished,Leftover woonmaatschappij Woonkade Rupelstreek after leftover AGB/APB hunt: omzet 10.29m DROP / pers 3.03m 36.9 VTE / debt 139.74m / cash 1.84m DROP / PnL LOSS 2.37m / dividend 0 / 1 VE hides municipal housing vehicle,8,Woonkade Rupelstreek / Bestuursorgaan / voorzitter Cools Sven,jan@woonkade.be,Uitbreidingsstraat 39 2850 Boom,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1476 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF now extracted (2176655 bytes 61p). FOI ready not sent. NOT every-10. NOT Erfgoed Rupelstreek IOED 1431 / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 403 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still no separate APB 2025 PDF. WoonST Temse still JR2024 as of 1467. stek92 still JR2024 as of 1473. Leftover Woonveer 2026-00187904 live this tick unused.",
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
    if not last_s.startswith("rq_1476,"):
        raise SystemExit(f"expected last row rq_1476, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1476 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1476,Woonkade Rupelstreek JR2025 leftover dual residual,hole_fill,5,done,L5,wm_wkdr,"
        "Completed: Woonkade Rupelstreek leftover woonmaatschappij of mined Boom + Hemiksem + Niel + Rumst + Schelle after leftover AGB/APB hunt; KBO 0452.753.537 Actief; live JR2025 official NBB WVV VOL-inb PDF (2176655 bytes 61p; deposit 2026-00140460; AV 02.06.2026; header 03.06.2026; pdfinfo 06.06.2026 01:02:43 UTC). PDF header Woonkade Rupelstreek / Uitbreidingsstraat 39 — NOT Erfgoed Rupelstreek IOED 1431 / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / Thuispunt Gent / Tuinwijk / Dijledal / Dender-Zuid / Dimensa / Woonmaatschappij Rivierenland / Woonpunt Waas / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Sourced euros assets 159099064 omzet 10288580 diensten 4211680 pers 3032421 36.9 VTE pnl -2373789 equity 18271109 cash 1837328 debt 139739427 capex 13308629 dividend 0. FOI "
        f"{GAP} ready not sent. Distinct from already-mined Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Erfgoed Rupelstreek IOED 1431.,"
        f"{GAP},2026-08-19T17:28:00Z,{TS},"
        "tick1476 Woonkade Rupelstreek leftover woonmaatschappij residual; KBO 0452.753.537; live JR2025 official NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1477 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (Woonveer 2026-00187904 live unused)"
    )
    spawn = (
        "rq_1477,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill: Next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1476 done including Woonkade 1476 leftover woonmaatschappij live official NBB WVV / Woonstroom 1475 leftover woonmaatschappij live official NBB WVV / Thuisrand 1474 leftover woonmaatschappij live official NBB WVV / Vivendo 1473 leftover woonmaatschappij live official NBB WVV / SW+ 1472 leftover woonmaatschappij live official NBB WVV / Woonhaven 1471 leftover woonmaatschappij live official NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 403 as of 1476). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1476). Do NOT confuse with already-mined Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Erfgoed Rupelstreek IOED 1431. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live. Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1471 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1461. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonhaven TAKEN 1471; SW+ TAKEN 1472; Vivendo TAKEN 1473; Thuisrand TAKEN 1474; Woonstroom TAKEN 1475; Woonkade TAKEN 1476; leftover Woonveer 0406.039.624 2026-00187904 live unused; WoonST Temse still JR2024 as of 1467; stek92 still JR2024 as of 1473). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Erfgoed Rupelstreek IOED 1431.,,"
        f"{TS},{TS},"
        "spawned tick1476 after Woonkade leftover woonmaatschappij live official NBB WVV JR2025; leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (Woonveer 2026-00187904 live unused)"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1476=done + rq_1477 spawned; keep", last_line_start)

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
    Path("/tmp/tick1476_inv.txt").write_text(
        f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\n",
        encoding="utf-8",
    )

    notes = (
        f"tick1476 Woonkade leftover woonmaatschappij residual; KBO 0452.753.537; live JR2025 official NBB WVV PDF; sourced euros assets 159099064 omzet 10288580 diensten 4211680 pers 3032421 36.9 VTE pnl -2373789 equity 18271109 cash 1837328 debt 139739427 capex 13308629 dividend 0; FOI ready omzet 10.29m DROP / pers 3.03m 36.9 VTE / debt 139.74m / cash 1.84m DROP / PnL LOSS 2.37m / dividend 0 / 1 VE; NOT Erfgoed Rupelstreek IOED / Woonstroom / Thuisrand / Vivendo / SW+ / Woonhaven / leftover Woonveer / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1477 leftover APB Inovant/Atlas if PDF live else leftover other provincial APBs (Puyenbroeck) / leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM/other woonmaatschappij if JR2025 (Woonveer 2026-00187904 live unused); FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1476,1476,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1476")

    entry = (
        "\n## Tick 1476 - 2026-08-19 - rq_1476 Woonkade Boom dual residual leftover\n"
        "- Unit: Woonkade Rupelstreek BV (leftover woonmaatschappij / social-housing BV of mined Boom + Hemiksem + Niel + Rumst + Schelle; 1 VE) after residual dual hunt (KBO **0452.753.537**; official NBB WVV VOL-inb PDF **2176655** bytes / 61p; deposit **2026-00140460**; AV **02.06.2026**; header **03.06.2026**; pdfinfo created **06.06.2026 01:02:43 UTC**; model **VOL-inb** 26.0.12 m82-f; commissaris Moore Audit BV B00212 / 0453.925.059 / Boeykens Pieterjan A02594 mandate 22.09.2022–06.06.2028 fee **15000** + extra 3170; VOL-inb 6.1/6.2.1/6.2.2/6.2.4/6.2.5/6.3.5/6.4.1/6.4.2/6.5.1/6.5.2/6.7.2/6.15/6.17/6.18.2/6.20/9/12/13/14/15 not filed; 6.2.3 IVA + 6.3 MVA + 6.4.3 FVA + 6.6 + 6.7.1 + 6.8 + 6.9 + 6.10 + 6.11 + 6.12 + 6.16 + 6.18.1 + 6.19 + sociale balans + commissarisverslag filed). Leftover AGB/APB first: leftover APB Inovant / Atlas provincieantwerpen.be **403** even with Googlebot UA; Foleon leftover slugs redirect to foleon.com; no fetchable 2025 Inovant/Atlas PDF (do not take Hooibeekhoeve). Leftover Puyenbroeck still no separate APB 2025 statutory PDF this tick. Leftover AGB Herzele already in entities (tick1163) — skipped. Leftover AGB Bornem still 2024. Leftover AGB Boom Plus + AGB Rumst already in entities — skipped. Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel still no JR as of 1471. Leftover IGS IVAREM 0267.403.264 last JR still 2024-12-31 as of 1471. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. Leftover WoonST Temse still JR2024 as of 1467. Leftover stek92 still JR2024 as of 1473. Leftover Woonkade statutory CDN `2026-00140460` live this tick (HTTP 200 / application/pdf / 2176655 / 61p; jaar **2025-12-31**; neerlegging **03.06.2026**) — taken (hunt order #2 leftover unmined woonmaatschappij of mined Boom-Rupelstreek with live 2025 VOL-inb after leftover AGB/APB hunt; strong 1475 hint). PDF header **Woonkade Rupelstreek / Uitbreidingsstraat 39 / 2850 Boom** — NOT Erfgoed Rupelstreek IOED 1431 / Woonstroom / Thuisrand / leftover IVAREM / Hooibeekhoeve / Puyenbroeck. Distinct from already-mined **Woonstroom 1475** / **Thuisrand 1474** / **Vivendo 1473** / **SW+ 1472** / **Woonhaven 1471** / **Thuispunt Gent 1470** / **Tuinwijk 1469** / **Dijledal 1468** / **Dender-Zuid 1467** / **Dimensa 1466** / **Woonmaatschappij Rivierenland 1465** / **Woonpunt Waas 1464** / **Erfgoed Rupelstreek IOED 1431**. First confirmed not already extracted as JR2025 euros: no Woonkade / 0452.753.537 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **25.05.1994**; statutaire naam WOONKADE RUPELSTREEK since 22.06.2023; BV since 22.06.2023; zetel Uitbreidingsstraat 39 2850 Boom since 22.06.2023; **1 VE**; 16 functiehouders; voorzitter Cools Sven since 25.02.2025; dagelijks bestuur Maeremans Frank since 22.06.2023; Werkgever RSZ since 25.05.1994; btw since 01.08.1995; aanbestedende overheid; NACE 68.202 / 68.203; site https://woonkade.be/; werkingsgebied Boom + Hemiksem + Niel + Rumst + Schelle. Absorbeerde 0403.675.396 since 05.06.2018 + 0400.813.304 since 22.06.2023. Prior-year figures **identiek**. SBM used for deposit-id discovery only. Euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb/Busibee euros not used. NOT every-10 (next 1480).\n"
        "- EUR strong (primary official WVV VOL-inb; omzet 70 **10288580** DROP vs 10500673; 6.10 omzet-split empty; diensten 61 **4211680** JUMP vs 3931696; pers 62 **3032421** / **36,9 VTE** vs 2958536 / 36,2): assets **159099064** (was 153904629); fixed **154241260** vs 145543820 / IVA **8450** / MVA **154120562** vs 145435952 (terreinen/gebouwen **129126383**; installaties **178232**; meubilair **222856**; leasing **181**; in aanbouw **24592909 JUMP** vs 16733281) / FVA **112247**; current **4857804 DROP** vs 8360808; voorraden **1408274** (onroerend verkoop **1369922**); ST recv **296836** (trade **281970** / other **14866**); LT recv empty; geldbeleg **4000**; cash **1837328 DROP** vs 5145025; prepaid **1311367**; equity **18271109 DROP** vs 20944487 (inbreng **54906**; herw **2055962**; reserves **11304327**; overgedragen **-3942272**; kapsubs **8798185**); voorzieningen **1088528** (claim **310000**; uitgestelde belasting **778528**); schulden **139739427 JUMP** vs 132155590 (LT **130918132** waarvan fin krediet **129372104 JUMP** vs 120225235; ST **7916437** waarvan 42 **5506854** + leveranciers **901554**; deferred **904858**); omzet **10288580** DROP; 60 **151838**; diensten **4211680** JUMP; pers **3032421** / **36,9 VTE** / 51082 uur / YE **36** / YE VTE **34,7**; interim **1,5 VTE** 144200; afschr **4645450**; expl **-1828674** vs -354357; fin opbr **2645598** (interestsubs 2312426); fin kosten **3216737**; tax empty; PnL **9904 -2373789 LOSS** vs -880277 (te bestemmen 9905 **-2191508**); dividend **0**; capex MVA aanschaf **13308629** (meubilair 27267 + in aanbouw 13281362). Commissaris fee **15000**. Bestuurders 9503 unpublished. 1 VE. 6.7.2 aandeel % unpublished. 3365174 aandelen op naam. Cross-checks: 154241260+4857804=159099064; 18271109+1088528+139739427=159099064; 11637610-13466284=-1828674; -1828674+2645598-3216737=-2399813; -2399813+26024=-2373789; 27267+13281362=13308629.\n"
        "- CSVs: sources +4; entities +1 `wm_wkdr` parent `city_boom`; budgets +44 executed; commitments +1 envelope 10288580 AV 02.06.2026; leaderboard +1 annual 10288580 / total 159099064; foi_queue +1 status=ready never sent; research_queue surgical rq_1476=done + rq_1477 spawn; loop_state ticks_completed=1476. Inventory after write: budgets {INV_B} · commitments {INV_C} · leaderboard {INV_L} · entities {INV_E} · sources {INV_S} · FOI ready {FOI_R} / answered {FOI_A} / partial {FOI_P} / total {FOI_T}.\n"
        "- FOI: `gap_wkdr_omzet_10_29m_pers_3_03m_loss_2_37m_l5` ready not sent — omzet 10.29m DROP / 6.10 split empty / diensten 4.21m JUMP / pers 3.03m 36.9 VTE / 1 VE / cash DROP 1.84m / debt 139.74m LT krediet 129.37m / voorraden 1.41m / capex 13.31m / PnL LOSS 2.37m / dividend 0 / commissaris 15.00k / aandeel % unpublished.\n"
        "- Next: rq_1477 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 403 this tick — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck still no separate APB 2025 PDF as of 1476). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live. Leftover IGS IVAREM **0267.403.264** still JR2024 as of 1471. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonhaven **0403.795.657** TAKEN 1471; SW+ **0405.342.610** TAKEN 1472; Vivendo **0406.062.883** TAKEN 1473; Thuisrand **0404.710.724** TAKEN 1474; Woonstroom **0404.033.605** TAKEN 1475; Woonkade **0452.753.537** TAKEN 1476; leftover Woonveer Klein-Brabant **0406.039.624** 2026-00187904 live unused this tick; WoonST Temse still JR2024 as of 1467; stek92 still JR2024 as of 1473). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / Toerisme Limburg 1463 / Toerisme Vlaams-Brabant 1462 / Toerisme Oost-Vlaanderen 1461 / Arboretum Kalmthout 1460 / Erfgoed Rupelstreek IOED 1431. Next every-10 is **1480**. Provincial tourism VZWs now exhausted (Westtoer + TOV + TVLB + TLim).\n"
    )
    entry = entry.replace("{INV_B}", str(inv["budgets.csv"])).replace("{INV_C}", str(inv["commitments.csv"])).replace("{INV_L}", str(inv["leaderboard.csv"])).replace("{INV_E}", str(inv["entities.csv"])).replace("{INV_S}", str(inv["sources.csv"])).replace("{FOI_R}", str(foi_ready)).replace("{FOI_A}", str(foi_ans)).replace("{FOI_P}", str(foi_part)).replace("{FOI_T}", str(foi_tot))
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1476 -" in lraw:
        raise SystemExit("loop_log already has tick 1476 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1476")
    print("DONE tick 1476")

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

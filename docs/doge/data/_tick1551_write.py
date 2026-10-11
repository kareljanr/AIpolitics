#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1551 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, io, sys, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "eva_inagro"
SRC = "src_inagro_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00069903.pdf"
GAP = "gap_inagro_opbr_26_28m_pers_15_60m_beleg_jump_l5"
LB = "lb_inagro_opbr_26_28m_pers_15_60m_beleg_jump"
COMM = "comm_inagro_jr2025_opbr"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def check(row, n, label):
    fields = next(csv.reader(io.StringIO(row)))
    got = len(fields)
    if got != n:
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:180]}")
    if any("," in f for f in fields):
        raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")

def part_sources():
    rows = [
        f"{SRC},Inagro official NBB VOL-VZW JR2025 deposit 2026-00069903,{PDF},Nationale Bank van Belgie / Inagro vzw,2026-08-20,budget,tick1551; official NBB WVV VOL-VZW PDF 44p / 396186 bytes; deposit 2026-00069903 Initial; model VOL-VZW 25.0.9 m05-f; AV 24.03.2026; year-end 31.12.2025; pdfinfo created 02.04.2026 03:27:57 UTC OpenPDF 1.3.26; euros PDF only; envelope bedrijfsopbrengsten 70/76A 26282403 (leftover EVA VZW; omzet 70 present but commercial-only 4836725; not CREMABRU omzet-envelope)",
        "src_inagro_nbb_consult,NBB consult Inagro 0417474241 published deposit 2026-00069903,https://consult.cbso.nbb.be/consult-enterprise/0417474241,Nationale Bank van Belgie,2026-08-20,official_register,tick1551; leftover EVA of mined provincie West-Vlaanderen; official NBB consult lists JR2025 deposit 2026-00069903 filing 30.03.2026 year-end 31.12.2025 Volledig model vereniging; official CDN 396186 bytes",
        "src_inagro_kbo_0417474241_1551,KBO Inagro provinciaal EVAP vzw 0417.474.241 (reconfirm tick1551),https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0417474241,FPS Economy KBO,2026-08-20,official_register,tick1551; leftover EVA of mined provincie West-Vlaanderen; KBO 0417.474.241 Actief official kbo-bce.fgov.be; zetel Ieperseweg 87 8800 Roeselare; entity eva_inagro already mapped tick1332 FOI-only",
        "src_inagro_foi_contact_1551,Inagro FOI channel (info@inagro.be),https://inagro.be/contact,Inagro vzw / Provincie West-Vlaanderen,2026-08-20,official_web,tick1551; leftover EVA of mined provincie West-Vlaanderen; FOI ready not sent; Ieperseweg 87 8800 Roeselare; official e-mail info@inagro.be; NOT leftover Westtoer / leftover TUA West / leftover CREMABRU 1550 / leftover INTRADURA 1549",
    ]
    for r in rows:
        check(r, 7, "sources")
    append_lf(DATA / "sources.csv", rows)
    print("sources +4")

def part_entities():
    """Surgical one-line notes patch. Do not rewrite whole entities.csv."""
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    lines = raw.split(b"\n")
    found = False
    notes = (
        "tick1551 leftover EVA residual of mined provincie West-Vlaanderen after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover EVA with live official NBB JR2025 euros taken (tick1332 FOI-only / no fetchable PDF); KBO 0417.474.241 Actief official kbo-bce.fgov.be; zetel Ieperseweg 87 8800 Roeselare; live official NBB VOL-VZW deposit 2026-00069903 44p 396186; sourced euros assets 57442295 opbr 26282403 omzet 4836725 subsid 21223307 pers 15598848 vte 204.2 expl 849611 PROFIT pnl 1073542 PROFIT cash 4503752 DROP beleg 18330475 JUMP kapsubs 22290803 JUMP; FOI ready not sent; parent prov_west_vlaanderen; entity eva_inagro already mapped; NOT leftover Westtoer / leftover TUA West / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand"
    )
    if "," in notes:
        raise SystemExit("entity notes contain comma")
    out = []
    for line in lines:
        if line.startswith(b"eva_inagro,"):
            found = True
            # keep first 10 fields (quoted names intact); replace notes (last unquoted field)
            prefix, sep, _old = line.rpartition(b",")
            if not prefix.startswith(b"eva_inagro,"):
                raise SystemExit("eva_inagro rpartition failed")
            line = prefix + b"," + notes.encode("utf-8")
        out.append(line)
    if not found:
        raise SystemExit("eva_inagro missing")
    text = b"\n".join(out)
    if not text.endswith(b"\n"):
        text += b"\n"
    before = pth.stat().st_size
    pth.write_bytes(text)
    after = pth.stat().st_size
    print("entities surgical eva_inagro notes", before, "->", after)

def part_budgets():
    rows = [
        f"bud_inagro_opbr_2025,{ENT},2025,26282403,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 26282403 envelope (leftover EVA VZW; omzet 70 present but commercial-only); tick1551; primary official NBB VOL-VZW AV 24.03.2026",
        f"bud_inagro_omzet_2025,{ENT},2025,4836725,,,executed,{SRC},strong,2025 omzet 70 4836725 DROP was 4842545; commercial-only; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_subsid_2025,{ENT},2025,21223307,,,executed,{SRC},strong,2025 lidgeld/schenkingen/legaten/subsidies 73 21223307 JUMP was 19456592; 733 subsidies 21223307 (730/731/732 empty); tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_74_2025,{ENT},2025,202680,,,executed,{SRC},strong,2025 andere bedrijfsopbrengsten 74 202680 UP was 197735; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_76a_2025,{ENT},2025,19691,,,executed,{SRC},strong,2025 niet-recurrente bedrijfsopbrengsten 76A 19691; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_assets_2025,{ENT},2025,57442295,,,executed,{SRC},strong,2025 balanstotaal 20/58 57442295 UP was 50678618; VA+vlottend holds; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_va_2025,{ENT},2025,18308447,,,executed,{SRC},strong,2025 vaste activa 21/28 18308447 DROP was 19226075; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_iva_2025,{ENT},2025,140454,,,executed,{SRC},strong,2025 IVA 21 140454 DROP was 263657; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_mva_2025,{ENT},2025,18154673,,,executed,{SRC},strong,2025 MVA 22/27 18154673 DROP was 18949098; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_gebouwen_2025,{ENT},2025,13910198,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 13910198 DROP was 15064571; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_install_2025,{ENT},2025,3614393,,,executed,{SRC},strong,2025 installaties 23 3614393 JUMP was 2602804; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_meubilair_2025,{ENT},2025,422817,,,executed,{SRC},strong,2025 meubilair 24 422817 DROP was 508452; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_inaanbouw_2025,{ENT},2025,207266,,,executed,{SRC},strong,2025 in aanbouw 27 207266 DROP was 773271; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_fva_2025,{ENT},2025,13320,,,executed,{SRC},strong,2025 FVA 28 13320 (verbonden 1412 + deelneming 11350 + andere 558); tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_vlottend_2025,{ENT},2025,39133848,,,executed,{SRC},strong,2025 vlottende 29/58 39133848 JUMP was 31452543; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_stocks_2025,{ENT},2025,3600,,,executed,{SRC},strong,2025 voorraden 3 3600 UP was 1780; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_handelsrecv_2025,{ENT},2025,1737471,,,executed,{SRC},strong,2025 handelsvorderingen 40 1737471 UP was 1443105; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_otherrecv_2025,{ENT},2025,14286718,,,executed,{SRC},strong,2025 overige vorderingen 41 14286718 UP was 13712779; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_beleg_2025,{ENT},2025,18330475,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 18330475 JUMP was 3805475; termijn 53 18325000 JUMP was 3800000; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_cash_2025,{ENT},2025,4503752,,,executed,{SRC},strong,2025 liquide middelen 54/58 4503752 DROP was 12311686; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_prepaid_2025,{ENT},2025,271833,,,executed,{SRC},strong,2025 overlopend actief 490/1 271833 (over te dragen 191247 + verkregen 80532); tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_equity_2025,{ENT},2025,33535933,,,executed,{SRC},strong,2025 eigen vermogen 10/15 33535933 UP was 29264242; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_fondsen_2025,{ENT},2025,1468018,,,executed,{SRC},strong,2025 fondsen 10 1468018 (beginvermogen 1466902 + permanente 1115); tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_reserves_2025,{ENT},2025,4532513,,,executed,{SRC},strong,2025 bestemde fondsen 13 4532513 identiek; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_overgedragen_2025,{ENT},2025,5244599,,,executed,{SRC},strong,2025 overgedragen winst 14 5244599 UP was 4171057; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_kapsubs_2025,{ENT},2025,22290803,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 22290803 JUMP was 19092654; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_debt_2025,{ENT},2025,23906362,,,executed,{SRC},strong,2025 schulden 17/49 23906362 UP was 21414376; EV+debt holds 57442295; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_lt_2025,{ENT},2025,9525000,,,executed,{SRC},strong,2025 LT 17 9525000 DROP was 10125000; bank 173 9525000; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_st_2025,{ENT},2025,11014696,,,executed,{SRC},strong,2025 ST 42/48 11014696 JUMP was 8339529; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_lt_current_2025,{ENT},2025,600000,,,executed,{SRC},strong,2025 LT binnen jaar 42 600000; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_lev_2025,{ENT},2025,894149,,,executed,{SRC},strong,2025 handelsschulden 44 894149 UP was 669196; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_taxsoc_2025,{ENT},2025,3225904,,,executed,{SRC},strong,2025 belastingen/bezoldigingen 45 3225904; bezold 2659794; tax 566110; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_otherdebt_2025,{ENT},2025,6294643,,,executed,{SRC},strong,2025 overige schulden 48 6294643 JUMP was 4064203; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_accrued_2025,{ENT},2025,3366666,,,executed,{SRC},strong,2025 overlopend passief 492/3 3366666 over te dragen opbrengsten; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_costs_2025,{ENT},2025,25432792,,,executed,{SRC},strong,2025 bedrijfskosten 60/66A 25432792; official 1-euro vs 60+61+62+630+640/8; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_60_2025,{ENT},2025,1278137,,,executed,{SRC},strong,2025 handelsgoederen 60 1278137 (aankopen 1279957 stock -1820); tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_61_2025,{ENT},2025,5323432,,,executed,{SRC},strong,2025 diensten 61 5323432 UP was 5112921; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_pers_2025,{ENT},2025,15598848,,,executed,{SRC},strong,2025 bezoldigingen 62 15598848 / 204.2 VTE UP was 14459916 / 198.4; YE 216 / 201.5 VTE; hours 312578; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_afschr_2025,{ENT},2025,3070633,,,executed,{SRC},strong,2025 afschrijvingen 630 3070633 UP was 2820449; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_expl_2025,{ENT},2025,849611,,,executed,{SRC},strong,2025 bedrijfswinst 9901 849611 PROFIT was 675109; opbr-costs holds; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_fin_2025,{ENT},2025,604627,,,executed,{SRC},strong,2025 financiele opbrengsten 75 604627 (750 312883 + 752/9 291744 incl provincie intrest 282060); tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_fincost_2025,{ENT},2025,380695,,,executed,{SRC},strong,2025 financiele kosten 65 380695 (schulden 282060 + andere 98635); tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_pnl_2025,{ENT},2025,1073542,,,executed,{SRC},strong,2025 resultaat 9904/9905 1073542 PROFIT was 928811; tax empty; official 1-euro vs expl+fin 1073543; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_commissaris_2025,{ENT},2025,13727,,,executed,{SRC},strong,2025 commissaris 9505 13727 (Callens Vandelanotte); extra 95061 11100 + 95063 558; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_uitzend_2025,{ENT},2025,41675,,,executed,{SRC},strong,2025 uitzend 617 41675 / 0.7 VTE DROP was 61771 / 0.9; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_capex_2025,{ENT},2025,2153005,,,executed,{SRC},strong,2025 MVA aanschaffingen 8161 253698 + 8162 1589669 + 8163 222339 + 8166 78997 + IVA 8022 8302 = 2153005; tick1551; primary official NBB VOL-VZW",
        f"bud_inagro_gewaarborgd_2025,{ENT},2025,10125000,,,executed,{SRC},strong,2025 door Belgische overheidsinstellingen gewaarborgde schulden 9061 10125000; tick1551; primary official NBB VOL-VZW",
    ]
    for r in rows:
        check(r, 10, "budgets")
    append_lf(DATA / "budgets.csv", rows)
    print(f"budgets +{len(rows)}")

def part_rest():
    comm = (
        f"{COMM},Inagro JR2025 leftover EVA dual (opbr 26.28m / subsid 21.22m / pers 15.60m 204.2 VTE / expl PROFIT 0.85m / PnL PROFIT 1.07m / assets 57.44m),{ENT},Inagro / dual mined provincie West-Vlaanderen / land- en tuinbouwonderzoek,Provinciedecreet EVAP; VZW-wet; Bestuursdecreet openbaarheid,2026-03-24,2025,2025,26282403,,,active,{PDF},Local leftover EVA map VL West-Vlaanderen Inagro — opbr 26.28m / subsid 21.22m / pers 15.60m / beleg JUMP 18.33m / kapsubs JUMP 22.29m,Publish full AV notulen 24.03.2026 + 73 subsidy split provincie/Vlaanderen/EU + toelichting beleg JUMP / cash DROP / kapsubs JUMP / other recv / other ST debt / commissaris extra 11.7k; do not keep leftover Inagro unpublished,{SRC},strong,Vlaanderen>Provincies>WestVlaanderen>EVA>Inagro>JR2025_L5,tick1551; opbr 26282403 omzet 4836725 subsid 21223307 pers 15598848 vte 204.2 expl 849611 pnl 1073542 assets 57442295 beleg 18330475 JUMP kapsubs 22290803 JUMP cash 4503752 DROP commissaris 13727 extra 11658; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished"
    )
    check(comm, 19, "commitments")
    append_lf(DATA / "commitments.csv", [comm])
    print("commitments +1")

    lb = (
        f"{LB},Inagro JR2025 leftover EVA: opbr 26.28m / subsid 21.22m / pers 15.60m 204.2 VTE / expl PROFIT 0.85m / PnL PROFIT 1.07m / assets 57.44m,L5,local_budget_line,Vlaanderen>Provincies>WestVlaanderen>EVA>Inagro>JR2025_L5,26282403,57442295,Leftover dual EVA shell: opbr 26.28m / omzet 4.84m / subsid 21.22m / pers 15.60m 204.2 VTE / expl PROFIT 0.85m / PnL PROFIT 1.07m / assets 57.44m / beleg JUMP 18.33m / kapsubs JUMP 22.29m / cash DROP 4.50m / commissaris 13727 + extra 11658 / dividend n.a.,strong,{SRC},West-Vlaamse land- en tuinbouwers + Agrotopia / provinciale R&D,Local leftover EVA map VL West-Vlaanderen Inagro — official NBB VOL-VZW JR2025 live; 73 subsidy split FOI,Official NBB 2026-08-20: opbr 26.28m / pers 15.60m / subsid 21.22m / assets 57.44m,6.5,4.2,3.0,5.0,Publish full AV notulen 24.03.2026 + 73 subsidy split + toelichting beleg JUMP / cash DROP / kapsubs JUMP / other recv / other ST debt / commissaris extra 11.7k; do not keep leftover Inagro unpublished,active,,tick1551; leftover EVA of mined provincie West-Vlaanderen after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover Westtoer / leftover TUA West / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand"
    )
    check(lb, 21, "leaderboard")
    append_lf(DATA / "leaderboard.csv", [lb])
    print("leaderboard +1")

    foi = (
        f"{GAP},Vlaanderen>Provincies>WestVlaanderen>EVA>Inagro>JR2025_L5,{ENT},Official NBB VOL-VZW publishes opbr 26282403 / omzet 4836725 / subsid 21223307 / pers 15598848 204.2 VTE / expl PROFIT 849611 / PnL PROFIT 1073542 / assets 57442295 / beleg JUMP 18330475 / kapsubs JUMP 22290803 / cash DROP 4503752; 73 subsidy split provincie/Vlaanderen/EU unpublished; toelichting beleg JUMP / cash DROP / kapsubs JUMP / other recv 14.29m / other ST 6.29m unpublished; commissaris extra 11658 unpublished detail; AV notulen 24.03.2026 unpublished,Leftover EVA of mined provincie West-Vlaanderen with live official NBB JR2025 euros; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick; opbr 26.28m / pers 15.60m / subsid 21.22m,8,Inagro vzw / dienst openbaarheid,info@inagro.be,Ieperseweg 87 8800 Roeselare,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1551 leftover EVA after honest leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished so leftover EVA with live official NBB JR2025 euros taken (tick1332 FOI-only now filled); official CDN PDF. FOI ready not sent. NOT leftover Westtoer / leftover TUA West / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand"
    )
    check(foi, 21, "foi_queue")
    foi_path = DATA / "foi_queue.csv"
    before = foi_path.stat().st_size
    append_lf(foi_path, [foi])
    after = foi_path.stat().st_size
    if after < before:
        raise SystemExit(f"foi_queue shrank {before} -> {after}")
    print("foi_queue +1 append-only", before, "->", after)
    print("TS", TS)

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    elif part == "budgets":
        part_budgets()
    elif part == "rest":
        part_rest()
    else:
        raise SystemExit("use sources|entities|budgets|rest")

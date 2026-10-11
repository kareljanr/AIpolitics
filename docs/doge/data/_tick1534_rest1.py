#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
import subprocess
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "caw_cwzw"
SRC = "src_cwzw_jr2025_nbb"
GAP = "gap_cwzw_opbr_12_01m_pers_9_30m_expl_profit_l5"
LB = "lb_cwzw_opbr_12_01m_pers_9_30m_expl_profit"
COMM = "comm_cwzw_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00069501.pdf"

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
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:160]}")
    if any("," in f for f in fields):
        raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")

comm = (
    f"{COMM},CAW Zuid-West-Vlaanderen JR2025 leftover zorg EVA dual (opbr 12.01m / 73 10.63m / pers 9.30m 125 VTE / expl PROFIT 0.40m / cash JUMP 2.07m / beleg DROP 0.57m / other recv JUMP 1.63m),{ENT},CAW Zuid-West-Vlaanderen / dual mined Kortrijk + remaining Zuid-West-Vlaanderen municipalities / Departement Zorg subsidies,WVV vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid,2026-03-30,1970,,12009580,,,active,{PDF},Local leftover zorg EVA map VL Kortrijk CAW — opbr 12.01m / pers 9.30m 125 VTE / expl PROFIT 0.40m / cash JUMP 2.07m / beleg DROP 0.57m / other recv JUMP 1.63m,Publish 73 split (731 16694 + 733 10612561) + city vs Departement Zorg + beleg DROP + cash JUMP + other recv JUMP + in-aanbouw DROP + 76A JUMP + commissaris fee; do not keep leftover CAW ZWVL unpublished,{SRC},strong,Vlaanderen>Gemeenten>Kortrijk>CAW>CAW_Zuid_West_Vlaanderen>JR2025_L5,tick1534; assets 14138245 omzet 626259 73 10629255 opbr 12009580 pers 9302213 125 VTE pnl 401314 equity 11169738 cash 2068876 debt 2588507 capex 478865 dividend 0 nrec 76A 476789; FOI ready not sent; not TE-additive of 348bn; next every-10 1540"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CAW Zuid-West-Vlaanderen JR2025 leftover zorg EVA: opbr 12.01m / 73 10.63m / pers 9.30m 125 VTE / expl PROFIT 0.40m / cash JUMP 2.07m / beleg DROP 0.57m / other recv JUMP 1.63m,L5,local_budget_line,Vlaanderen>Gemeenten>Kortrijk>CAW>CAW_Zuid_West_Vlaanderen>JR2025_L5,12009580,14138245,Leftover dual zorg EVA shell: assets 14.14m / equity 11.17m / opbr 12.01m / 73 10.63m / pers 9.30m 125 VTE / cash 2.07m JUMP / beleg 0.57m DROP / in-aanbouw 0.09m DROP / expl PROFIT 0.40m / debt 2.59m / PnL PROFIT 0.40m,strong,{SRC},CAW Zuid-West-Vlaanderen / dual mined Kortrijk + remaining Zuid-West-Vlaanderen municipalities / Departement Zorg subsidies,Local leftover zorg EVA map VL Kortrijk CAW — JR2025 official NBB WVV live; 73 split + beleg DROP + cash JUMP + other recv JUMP + in-aanbouw DROP FOI,Official NBB WVV 2026-08-20: opbr 12.01m / pers 9.30m 125 VTE / cash JUMP 2.07m / beleg DROP 0.57m / expl PROFIT 0.40m,6.6,6.3,3.0,6.2,Publish 73 split (731 16694 + 733 10612561) + city vs Departement Zorg + beleg DROP 565797 was 1400404 + cash JUMP 2068876 + other recv JUMP 1628894 + in-aanbouw DROP 90797 was 2271648 + 76A JUMP 476789 + commissaris 6655; do not keep leftover CAW ZWVL unpublished,active,,tick1534; leftover recognized CAW of mined Kortrijk after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant/CAW-Limburg/CAW-Oost-Vlaanderen/CAW-CWVL hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG Mandel en Leie 1522 / leftover AGB Kortrijk / leftover SW+ 1472 / leftover !Mpuls 1484 / leftover Vivus 1500 / leftover CAW CWVL 1533 / leftover CAW Oost-Vlaanderen 1532 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Kortrijk>CAW>CAW_Zuid_West_Vlaanderen>JR2025_L5,{ENT},VOL-VZW publishes opbr 12009580 / omzet 626259 (6.9 category empty) / 73 10629255 (731 16694 + 733 10612561; 730 empty 732 empty); city vs Departement Zorg split unpublished; beleg DROP 565797 was 1400404 (51/52/53 empty; 8689 overige 565797); cash JUMP 2068876 was 1110751; other recv JUMP 1628894 was 541187; in-aanbouw DROP 90797 was 2271648; kapsubs UP 7123357 was 6458427; 76A JUMP 476789 (7630 meerwaarden); 66A 170345; expl PROFIT 401199; pers 9302213 / 125 VTE; capex 478865; dual city/Departement Zorg split unpublished; related leftover Steunfonds 0860553415 unpublished,Leftover recognized Flemish CAW / leftover zorg EVA of mined Kortrijk with live JR2025; tenth per-CAW L5 after CAW Antwerpen 1525 CAW De Kempen 1526 CAW Brussel 1527 CAW Rivierenland 1528 CAW Halle-Vilvoorde 1529 CAW Oost-Brabant 1530 CAW Limburg 1531 CAW Oost-Vlaanderen 1532 and CAW CWVL 1533; annual envelope 12.01m opbr / pers 9.30m 125 VTE / expl PROFIT 0.40m / cash JUMP 2.07m / assets 14.14m,8,CAW Zuid-West-Vlaanderen / dienst openbaarheid,carine.verhaeghe@cawzuidwestvlaanderen.be,Voorstraat 51 8500 Kortrijk,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1534 leftover recognized CAW after honest leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant/CAW-Limburg/CAW-Oost-Vlaanderen/CAW-CWVL hunt; official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1540). NOT leftover CGG Mandel en Leie 1522 / leftover AGB Kortrijk / leftover SW+ 1472 / leftover !Mpuls 1484 / leftover Vivus 1500 / leftover CAW CWVL 1533 / leftover CAW Oost-Vlaanderen 1532 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

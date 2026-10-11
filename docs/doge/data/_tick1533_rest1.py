#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
import subprocess
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "caw_cwcw"
SRC = "src_cwcw_jr2025_nbb"
GAP = "gap_cwcw_opbr_9_19m_pers_7_32m_expl_loss_l5"
LB = "lb_cwcw_opbr_9_19m_pers_7_32m_expl_loss"
COMM = "comm_cwcw_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00088320.pdf"

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
    f"{COMM},CAW Centraal-West-Vlaanderen JR2025 leftover zorg EVA dual (opbr 9.19m / 73 8.74m / pers 7.32m 108.9 VTE / expl LOSS 0.15m / beleg DROP 1.17m / in-aanbouw JUMP 2.37m / lev JUMP 1.23m),{ENT},CAW Centraal-West-Vlaanderen / dual mined Izegem + remaining Centraal-West-Vlaanderen municipalities / Departement Zorg subsidies,WVV vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid,2026-04-22,1970,,9188129,,,active,{PDF},Local leftover zorg EVA map VL Izegem CAW — opbr 9.19m / pers 7.32m 108.9 VTE / expl LOSS 0.15m / beleg DROP 1.17m / in-aanbouw JUMP 2.37m,Publish 73 split (731 19764 + 733 8719910) + city vs Departement Zorg + termijn DROP + in-aanbouw JUMP + lev JUMP + expl LOSS + commissaris fee; do not keep leftover CAW CWVL unpublished,{SRC},strong,Vlaanderen>Gemeenten>Izegem>CAW>CAW_Centraal_West_Vlaanderen>JR2025_L5,tick1533; assets 8483960 omzet 187872 73 8739673 opbr 9188129 pers 7318691 108.9 VTE pnl -99538 equity 5379782 cash 901859 debt 3002354 capex 2099971 dividend 0 nrec 76A 156513; FOI ready not sent; not TE-additive of 348bn; next every-10 1540"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CAW Centraal-West-Vlaanderen JR2025 leftover zorg EVA: opbr 9.19m / 73 8.74m / pers 7.32m 108.9 VTE / expl LOSS 0.15m / beleg DROP 1.17m / in-aanbouw JUMP 2.37m / lev JUMP 1.23m,L5,local_budget_line,Vlaanderen>Gemeenten>Izegem>CAW>CAW_Centraal_West_Vlaanderen>JR2025_L5,9188129,8483960,Leftover dual zorg EVA shell: assets 8.48m / equity 5.38m / opbr 9.19m / 73 8.74m / pers 7.32m 108.9 VTE / cash 0.90m / beleg 1.17m DROP / in-aanbouw 2.37m JUMP / expl LOSS 0.15m / debt 3.00m / PnL LOSS 0.10m,strong,{SRC},CAW Centraal-West-Vlaanderen / dual mined Izegem + remaining Centraal-West-Vlaanderen municipalities / Departement Zorg subsidies,Local leftover zorg EVA map VL Izegem CAW — JR2025 official NBB WVV live; 73 split + termijn DROP + in-aanbouw JUMP + expl LOSS FOI,Official NBB WVV 2026-08-20: opbr 9.19m / pers 7.32m 108.9 VTE / beleg DROP 1.17m / expl LOSS 0.15m,6.6,6.3,3.0,6.2,Publish 73 split (731 19764 + 733 8719910) + city vs Departement Zorg + termijn DROP 0 was 1165000 + in-aanbouw JUMP 2369201 + lev JUMP 1233306 + 74 DROP 104071 + kapsubs JUMP 2087596 + commissaris 6732; do not keep leftover CAW CWVL unpublished,active,,tick1533; leftover recognized CAW of mined Izegem after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant/CAW-Limburg/CAW-Oost-Vlaanderen hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG Largo 1518 / leftover Motena Roeselare / leftover Thuiswest 1493 / leftover CAW Oost-Vlaanderen 1532 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Izegem>CAW>CAW_Centraal_West_Vlaanderen>JR2025_L5,{ENT},VOL-VZW publishes opbr 9188129 / omzet 187872 (6.9 category empty) / 73 8739673 (731 19764 + 733 8719910; 730 empty 732 empty); city vs Departement Zorg split unpublished; termijn DROP 0 was 1165000; beleg DROP 1173271 was 2336418; in-aanbouw JUMP 2369201 was 290209; lev JUMP 1233306 was 431918; 74 DROP 104071 was 633721; kapsubs JUMP 2087596 was 964102; accrued DROP 232020 was 826571; expl LOSS 151354; pers 7318691 / 108.9 VTE; capex 2099971; dual city/Departement Zorg split unpublished,Leftover recognized Flemish CAW / leftover zorg EVA of mined Izegem with live JR2025; ninth per-CAW L5 after CAW Antwerpen 1525 CAW De Kempen 1526 CAW Brussel 1527 CAW Rivierenland 1528 CAW Halle-Vilvoorde 1529 CAW Oost-Brabant 1530 CAW Limburg 1531 and CAW Oost-Vlaanderen 1532; annual envelope 9.19m opbr / pers 7.32m 108.9 VTE / expl LOSS 0.15m / beleg DROP 1.17m / assets 8.48m,8,CAW Centraal-West-Vlaanderen / dienst openbaarheid,administratie@cawcentraalwestvlaanderen.be,Krekelstraat 56 8870 Izegem,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1533 leftover recognized CAW after honest leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant/CAW-Limburg/CAW-Oost-Vlaanderen hunt; official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1540). NOT leftover CGG Largo 1518 / leftover Motena Roeselare / leftover Thuiswest 1493 / leftover CAW Oost-Vlaanderen 1532 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

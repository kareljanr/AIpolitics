#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
import subprocess
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "caw_cwnw"
SRC = "src_cwnw_jr2025_nbb"
GAP = "gap_cwnw_opbr_17_99m_pers_14_78m_expl_loss_l5"
LB = "lb_cwnw_opbr_17_99m_pers_14_78m_expl_loss"
COMM = "comm_cwnw_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00103625.pdf"

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
    f"{COMM},CAW Noord-West-Vlaanderen JR2025 leftover zorg EVA dual (opbr 17.99m / 73 16.12m / pers 14.78m 206.2 VTE / expl LOSS 1.89m / cash DROP 0.43m / beleg JUMP 1.02m / voorzieningen JUMP 1.31m),{ENT},CAW Noord-West-Vlaanderen / dual mined Brugge + remaining Noord-West-Vlaanderen municipalities / Departement Zorg subsidies,WVV vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid,2026-04-22,1970,,17987315,,,active,{PDF},Local leftover zorg EVA map VL Brugge CAW — opbr 17.99m / pers 14.78m 206.2 VTE / expl LOSS 1.89m / cash DROP 0.43m / beleg JUMP 1.02m / voorzieningen JUMP 1.31m,Publish 73 split (731 40823 + 733 16078297) + city vs Departement Zorg + cash DROP + beleg JUMP + LT recv JUMP + voorzieningen JUMP + 66A JUMP + commissaris fee; do not keep leftover CAW NWVL unpublished,{SRC},strong,Vlaanderen>Gemeenten>Brugge>CAW>CAW_Noord_West_Vlaanderen>JR2025_L5,tick1535; assets 15981042 omzet 431305 73 16119120 opbr 17987315 pers 14781014 206.2 VTE pnl -1892028 equity 8328831 cash 430376 debt 6344185 capex 1427657 dividend 0 nrec 76A 600928; FOI ready not sent; not TE-additive of 348bn; last official 11-CAW; next every-10 1540"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CAW Noord-West-Vlaanderen JR2025 leftover zorg EVA: opbr 17.99m / 73 16.12m / pers 14.78m 206.2 VTE / expl LOSS 1.89m / cash DROP 0.43m / beleg JUMP 1.02m / voorzieningen JUMP 1.31m,L5,local_budget_line,Vlaanderen>Gemeenten>Brugge>CAW>CAW_Noord_West_Vlaanderen>JR2025_L5,17987315,15981042,Leftover dual zorg EVA shell: assets 15.98m / equity 8.33m / opbr 17.99m / 73 16.12m / pers 14.78m 206.2 VTE / cash 0.43m DROP / beleg 1.02m JUMP / voorzieningen 1.31m JUMP / expl LOSS 1.89m / debt 6.34m / PnL LOSS 1.89m,strong,{SRC},CAW Noord-West-Vlaanderen / dual mined Brugge + remaining Noord-West-Vlaanderen municipalities / Departement Zorg subsidies,Local leftover zorg EVA map VL Brugge CAW — JR2025 official NBB WVV live; 73 split + cash DROP + beleg JUMP + LT recv JUMP + voorzieningen JUMP FOI,Official NBB WVV 2026-08-20: opbr 17.99m / pers 14.78m 206.2 VTE / cash DROP 0.43m / beleg JUMP 1.02m / expl LOSS 1.89m,6.8,6.7,3.0,6.5,Publish 73 split (731 40823 + 733 16078297) + city vs Departement Zorg + cash DROP 430376 was 1924544 + beleg JUMP 1022346 + LT recv JUMP 860158 + voorzieningen JUMP 1308026 + 66A JUMP 1680781 + 76A JUMP 600928 + commissaris 7657; do not keep leftover CAW NWVL unpublished,active,,tick1535; leftover recognized CAW of mined Brugge after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant/CAW-Limburg/CAW-Oost-Vlaanderen/CAW-CWVL/CAW-ZWVL hunt; last official 11-CAW unit; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG NWVL 1507 / leftover Mintus Brugge / leftover AGB Brugge / leftover CGG Prisma 1513 / leftover CAW ZWVL 1534 / leftover CAW CWVL 1533 / leftover CAW Oost-Vlaanderen 1532 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Brugge>CAW>CAW_Noord_West_Vlaanderen>JR2025_L5,{ENT},VOL-VZW publishes opbr 17987315 / omzet 431305 (6.9 category empty) / 73 16119120 (731 40823 + 733 16078297; 730 empty 732 empty); city vs Departement Zorg split unpublished; cash DROP 430376 was 1924544; beleg JUMP 1022346 was 348292 (51/52/53 empty; 8689 overige 1022346); LT recv JUMP 860158 was 55000; other recv JUMP 1007414 was 565021; voorzieningen JUMP 1308026 (was empty; 6620 nrec); 66A JUMP 1680781; 76A JUMP 600928 (7630 524540 + 764/8 76388); accrued JUMP 1240278; expl LOSS 1890904; pers 14781014 / 206.2 VTE; YE 9086 192 vs social 105 216; capex 1427657; dual city/Departement Zorg split unpublished,Leftover recognized Flemish CAW / leftover zorg EVA of mined Brugge with live JR2025; eleventh and last official per-CAW L5 after CAW Antwerpen 1525 CAW De Kempen 1526 CAW Brussel 1527 CAW Rivierenland 1528 CAW Halle-Vilvoorde 1529 CAW Oost-Brabant 1530 CAW Limburg 1531 CAW Oost-Vlaanderen 1532 CAW CWVL 1533 and CAW ZWVL 1534; annual envelope 17.99m opbr / pers 14.78m 206.2 VTE / expl LOSS 1.89m / cash DROP 0.43m / assets 15.98m,8,CAW Noord-West-Vlaanderen / dienst openbaarheid,nele.haers@cawnoordwestvlaanderen.be,Ruddershove 8 8000 Brugge,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1535 leftover recognized CAW after honest leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant/CAW-Limburg/CAW-Oost-Vlaanderen/CAW-CWVL/CAW-ZWVL hunt; official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1540). Last official 11-CAW. NOT leftover CGG NWVL 1507 / leftover Mintus Brugge / leftover AGB Brugge / leftover CGG Prisma 1513 / leftover CAW ZWVL 1534 / leftover CAW CWVL 1533 / leftover CAW Oost-Vlaanderen 1532 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T04:00:00Z"
ENT = "cgg_cgvb"
SRC = "src_cgvb_jr2025_nbb"
GAP = "gap_cgvb_opbr_9_34m_pers_6_66m_debt_2_33m_l5"
LB = "lb_cgvb_opbr_9_34m_pers_6_66m_debt_2_33m"
COMM = "comm_cgvb_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00227270.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def check(row, n, label):
    got = len(next(csv.reader(io.StringIO(row))))
    if got != n:
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:160]}")

comm = (
    f"{COMM},CGG Vlaams-Brabant Oost VZW JR2025 leftover recognized CGG dual (opbr 9.34m / 73 6.72m / pers 6.66m 69.5 VTE / cash DROP 2.48m / other ST debt DROP 0.09m / debt 2.33m),{ENT},CGG VBO / dual city Leuven-Tienen / Departement Zorg CGG-dotatie,WVV VZW; Decreet geestelijke gezondheidszorg; Bestuursdecreet openbaarheid,2026-06-24,2000,,9335733,,,active,{PDF},Local leftover CGG map VL Leuven — opbr 9.34m / 73 6.72m / pers 6.66m 69.5 VTE / cash DROP 2.48m,Publish 73 CGG-dotatie / city share + andere 74 JUMP 1.46m + diensten JUMP 2.31m + cash DROP + other ST DROP 92203 + 69.5 VTE payroll; do not keep leftover CGG unpublished,{SRC},strong,Vlaanderen>Gemeenten>Leuven>EVA>CGG_VBO>JR2025_L5,tick1509; assets 9329271 omzet 1083816 73 6717617 pers 6655129 69.5 VTE pnl 34423 equity 6996922 cash 2477705 debt 2332348 capex 65717 dividend 0 nrec 74763; FOI ready not sent; not TE-additive of 348bn; next every-10 is 1510"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CGG Vlaams-Brabant Oost VZW JR2025 leftover recognized CGG: opbr 9.34m / 73 6.72m / pers 6.66m 69.5 VTE / cash DROP 2.48m / andere 74 JUMP 1.46m / debt 2.33m,L5,local_budget_line,Vlaanderen>Gemeenten>Leuven>EVA>CGG_VBO>JR2025_L5,9335733,9329271,Leftover dual CGG VZW shell: assets 9.33m / equity 7.00m / opbr 9.34m / omzet 1.08m / 73 6.72m / pers 6.66m 69.5 VTE / cash DROP 2.48m / andere 74 JUMP 1.46m / diensten JUMP 2.31m / PnL +0.03m,strong,{SRC},CGG VBO / dual city Leuven-Tienen / Departement Zorg CGG-dotatie,Local leftover CGG map VL Leuven — JR2025 official NBB WVV live; 73 + andere-74/cash DROP FOI,Official NBB WVV 2026-08-20: opbr 9.34m / pers 6.66m 69.5 VTE / cash DROP 2.48m / PnL +0.03m / 1 VE / 73 6.72m,6.5,6.5,3.0,6.4,Publish 73 CGG-dotatie / city share + andere 74 JUMP 1459538 + diensten JUMP 2312175 + cash DROP + other ST DROP 92203 + 69.5 VTE payroll; do not keep leftover CGG unpublished,active,,tick1509; leftover recognized Flemish CGG after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG NWVL 1507 / leftover CGG SDW 1508 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Leuven>EVA>CGG_VBO>JR2025_L5,{ENT},VOL-VZW publishes 73 6717617 but CGG-dotatie / city share unpublished as a split; andere 74 JUMP 1459538; diensten 61 JUMP 2312175; cash DROP 2477705; other ST 48 DROP 92203; dual city/Flanders envelope unpublished,Leftover recognized Flemish CGG of mined Leuven + leftover Tienen with live JR2025; annual envelope 9.34m opbr / pers 6.66m 69.5 VTE / debt 2.33m / assets 9.33m,8,CGG Vlaams-Brabant Oost VZW / Departement Zorg Team Openbaarheid,openbaarheid@vlaanderen.be,Kapucijnenvoer 16 3000 Leuven,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1509 leftover recognized Flemish CGG after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1510 MUST do every-10 refresh). NOT leftover CGG NWVL 1507 / leftover CGG SDW 1508 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

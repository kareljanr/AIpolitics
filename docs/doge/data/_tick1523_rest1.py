#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T00:40:35Z"
ENT = "cgg_cgkh"
SRC = "src_cgkh_jr2025_nbb"
GAP = "gap_cgkh_opbr_8_79m_pers_6_25m_pnl_loss_l5"
LB = "lb_cgkh_opbr_8_79m_pers_6_25m_pnl_loss"
COMM = "comm_cgkh_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00242985.pdf"

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
    f"{COMM},CGG Kohesi VZW JR2025 leftover recognized CGG dual (opbr 8.79m / 73 7.94m / pers 6.25m 73.4 VTE / cash JUMP 1.98m / beleg DROP 0.50m / PnL LOSS 5.0k / expl DROP 10.4k / diensten JUMP 2.31m),{ENT},CGG Kohesi / dual city Hasselt / Departement Zorg CGG-dotatie,WVV VZW; Decreet geestelijke gezondheidszorg; Bestuursdecreet openbaarheid,2026-06-25,2000,,8794445,,,active,{PDF},Local leftover CGG map VL Hasselt — opbr 8.79m / 73 7.94m / pers 6.25m 73.4 VTE / cash JUMP 1.98m / PnL LOSS 5.0k,Publish 73 split + CGG-dotatie / city share + cash JUMP + beleg DROP + PnL LOSS + 73.4 VTE payroll; do not keep leftover CGG unpublished,{SRC},strong,Vlaanderen>Gemeenten>Hasselt>EVA>CGG_Kohesi>JR2025_L5,tick1523; assets 7706860 omzet 717138 73 7941612 opbr 8794445 pers 6248426 73.4 VTE pnl -5036 equity 4764907 cash 1981073 debt 2941952 capex 59387 dividend 0 nrec 76A 1 nrec 66A 95; FOI ready not sent; not TE-additive of 348bn; next every-10 1530"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CGG Kohesi VZW JR2025 leftover recognized CGG: opbr 8.79m / 73 7.94m / pers 6.25m 73.4 VTE / cash JUMP 1.98m / beleg DROP 0.50m / PnL LOSS 5.0k / expl DROP 10.4k / diensten JUMP 2.31m,L5,local_budget_line,Vlaanderen>Gemeenten>Hasselt>EVA>CGG_Kohesi>JR2025_L5,8794445,7706860,Leftover dual CGG VZW shell: assets 7.71m / equity 4.76m / opbr 8.79m / omzet 0.72m / 73 7.94m / pers 6.25m 73.4 VTE / cash JUMP 1.98m / beleg DROP 0.50m / PnL LOSS 5.0k,strong,{SRC},CGG Kohesi / dual city Hasselt / Departement Zorg CGG-dotatie,Local leftover CGG map VL Hasselt — JR2025 official NBB WVV live; 73 split + cash JUMP FOI,Official NBB WVV 2026-08-20: opbr 8.79m / pers 6.25m 73.4 VTE / cash JUMP 1.98m / beleg DROP 0.50m / PnL LOSS 5.0k,6.6,6.3,3.0,6.2,Publish 73 split + CGG-dotatie / city share + cash JUMP 1981073 + beleg DROP 500000 + PnL LOSS -5036 + 73.4 VTE payroll; do not keep leftover CGG unpublished,active,,tick1523; leftover recognized Flemish CGG after leftover AGB/APB hunt; NEW unused recognized CGG not in 1507-1522 list; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG Integra 1515 / leftover CGG Mandel en Leie 1522 / leftover CGG Brussel 1521 / leftover CGG PassAnt 1520 / leftover CGG Andante 1519 / leftover CGG Largo 1518 / leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG DAGG STOPPED / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Hasselt>EVA>CGG_Kohesi>JR2025_L5,{ENT},VOL-VZW publishes opbr 8794445 / 73 7941612 / omzet 717138; cash JUMP 1981073; beleg DROP 500000; other ST JUMP 699485; LT recv JUMP 518960; diensten JUMP 2307277; expl DROP 10440; PnL LOSS -5036; pers UP 6248426 / 73.4 VTE; dual city/Flanders envelope unpublished,Leftover recognized Flemish CGG of mined Hasselt with live JR2025; NEW unused recognized CGG not in 1507-1522 list; annual envelope 8.79m opbr / pers 6.25m 73.4 VTE / debt 2.94m / assets 7.71m,8,CGG Kohesi VZW / Departement Zorg Team Openbaarheid,openbaarheid@vlaanderen.be,Ilgatlaan 11 bus 3 3500 Hasselt,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1523 leftover recognized Flemish CGG after honest leftover AGB/APB hunt; NEW unused recognized CGG not in 1507-1522 list; live JR2025 official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1530). NOT leftover CGG Integra 1515 / leftover CGG Mandel en Leie 1522 / leftover CGG Brussel 1521 / leftover CGG PassAnt 1520 / leftover CGG Andante 1519 / leftover CGG Largo 1518 / leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG DAGG STOPPED / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

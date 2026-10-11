#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:49:00Z"
ENT = "cgg_cgin"
SRC = "src_cgin_jr2025_nbb"
GAP = "gap_cgin_opbr_19_62m_pers_16_53m_inb_jump_l5"
LB = "lb_cgin_opbr_19_62m_pers_16_53m_inb_jump"
COMM = "comm_cgin_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00205082.pdf"

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
    f"{COMM},CGG Integra VZW JR2025 leftover recognized CGG dual (opbr 19.62m / 73 9.25m / pers 16.53m 191.5 VTE / in aanbouw JUMP 1.60m / andere 74 6.20m / cash DROP 3.70m / PnL 0.10m DROP / debt 4.85m UP),{ENT},CGG Integra / dual city Hasselt-Limburg / Departement Zorg CGG-dotatie,WVV VZW; Decreet geestelijke gezondheidszorg; Bestuursdecreet openbaarheid,2026-06-25,2000,,19622796,,,active,{PDF},Local leftover CGG map VL Hasselt — opbr 19.62m / 73 9.25m / pers 16.53m 191.5 VTE / in aanbouw JUMP 1.60m,Publish 73 CGG-dotatie / city share + in aanbouw JUMP + andere 74 6.20m + andere pers 623 JUMP + 191.5 VTE payroll + cash DROP; do not keep leftover CGG unpublished,{SRC},strong,Vlaanderen>Gemeenten>Hasselt>EVA>CGG_Integra>JR2025_L5,tick1515; assets 14975892 omzet 3978611 73 9254873 opbr 19622796 pers 16532661 191.5 VTE pnl 102706 equity 9584897 cash 3698941 debt 4852883 capex 167392 dividend 0 nrec 76A 189157 inb 1596634; FOI ready not sent; not TE-additive of 348bn; next every-10 1520"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CGG Integra VZW JR2025 leftover recognized CGG: opbr 19.62m / 73 9.25m / pers 16.53m 191.5 VTE / in aanbouw JUMP 1.60m / andere 74 6.20m / cash DROP 3.70m / PnL 0.10m DROP / debt 4.85m UP,L5,local_budget_line,Vlaanderen>Gemeenten>Hasselt>EVA>CGG_Integra>JR2025_L5,19622796,14975892,Leftover dual CGG VZW shell: assets 14.98m / equity 9.58m / opbr 19.62m / omzet 3.98m / 73 9.25m / pers 16.53m 191.5 VTE / in aanbouw JUMP 1.60m / andere 74 6.20m / cash DROP 3.70m / PnL 0.10m,strong,{SRC},CGG Integra / dual city Hasselt-Limburg / Departement Zorg CGG-dotatie,Local leftover CGG map VL Hasselt — JR2025 official NBB WVV live; in aanbouw JUMP + andere 74 + andere pers 623 JUMP FOI,Official NBB WVV 2026-08-20: opbr 19.62m / pers 16.53m 191.5 VTE / in aanbouw JUMP 1.60m / andere 74 6.20m / cash DROP 3.70m,6.5,6.4,3.0,6.4,Publish 73 CGG-dotatie / city share + in aanbouw JUMP 1596634 + andere 74 6200155 + andere pers 623 JUMP 1163913 + 191.5 VTE payroll + cash DROP 3698941; do not keep leftover CGG unpublished,active,,tick1515; leftover recognized Flemish CGG after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Hasselt>EVA>CGG_Integra>JR2025_L5,{ENT},VOL-VZW publishes opbr 19622796 / 73 9254873 730-733 empty / pers 16532661 191.5 VTE; in aanbouw JUMP 1596634; andere 74 6200155; andere pers 623 JUMP 1163913; cash DROP 3698941; kapsubs JUMP 2221692; leveranciers JUMP 821474; PnL DROP 102706; dual city/Flanders envelope unpublished,Leftover recognized Flemish CGG of mined Hasselt + leftover Limburg with live JR2025; annual envelope 19.62m opbr / pers 16.53m 191.5 VTE / debt 4.85m / assets 14.98m,8,CGG Integra VZW / Departement Zorg Team Openbaarheid,openbaarheid@vlaanderen.be,Pater Valentinuslaan 32 3500 Hasselt,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1515 leftover recognized Flemish CGG after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1520). NOT leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

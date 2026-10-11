#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T00:08:00Z"
ENT = "cgg_cglr"
SRC = "src_cglr_jr2025_nbb"
GAP = "gap_cglr_opbr_6_76m_pers_5_51m_bestemde_jump_l5"
LB = "lb_cglr_opbr_6_76m_pers_5_51m_bestemde_jump"
COMM = "comm_cglr_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00186340.pdf"

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
    f"{COMM},CGG Largo VZW JR2025 leftover recognized CGG dual (opbr 6.76m / 73 6.39m / pers 5.51m 60.9 VTE / bestemde JUMP 2.04m / kapsubs JUMP 0.93m / other recv JUMP 1.42m / PnL DROP 0.17m / debt 1.29m DROP),{ENT},CGG Largo / dual city Roeselare-Ieper-Veurne / Departement Zorg CGG-dotatie,WVV VZW; Decreet geestelijke gezondheidszorg; Bestuursdecreet openbaarheid,2026-06-22,2000,,6764354,,,active,{PDF},Local leftover CGG map VL Roeselare — opbr 6.76m / 73 6.39m / pers 5.51m 60.9 VTE / bestemde JUMP 2.04m,Publish 73 split + CGG-dotatie / city share + bestemde JUMP + kapsubs JUMP + other recv JUMP + 60.9 VTE payroll; do not keep leftover CGG unpublished,{SRC},strong,Vlaanderen>Gemeenten>Roeselare>EVA>CGG_Largo>JR2025_L5,tick1518; assets 6034498 omzet 251094 73 6391572 opbr 6764354 pers 5512029 60.9 VTE pnl 165138 equity 4730724 cash 1666321 debt 1287831 capex 10507 dividend 0 nrec 76A 0 nrec 66A 15299; FOI ready not sent; not TE-additive of 348bn; next every-10 1520"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CGG Largo VZW JR2025 leftover recognized CGG: opbr 6.76m / 73 6.39m / pers 5.51m 60.9 VTE / bestemde JUMP 2.04m / kapsubs JUMP 0.93m / other recv JUMP 1.42m / PnL DROP 0.17m / debt 1.29m DROP,L5,local_budget_line,Vlaanderen>Gemeenten>Roeselare>EVA>CGG_Largo>JR2025_L5,6764354,6034498,Leftover dual CGG VZW shell: assets 6.03m / equity 4.73m / opbr 6.76m / omzet 0.25m / 73 6.39m / pers 5.51m 60.9 VTE / bestemde JUMP 2.04m / kapsubs JUMP 0.93m / other recv JUMP 1.42m / PnL DROP 0.17m,strong,{SRC},CGG Largo / dual city Roeselare-Ieper-Veurne / Departement Zorg CGG-dotatie,Local leftover CGG map VL Roeselare — JR2025 official NBB WVV live; 73 split + bestemde JUMP FOI,Official NBB WVV 2026-08-20: opbr 6.76m / pers 5.51m 60.9 VTE / bestemde JUMP 2.04m / kapsubs JUMP 0.93m / PnL DROP 0.17m,6.5,6.1,3.0,6.2,Publish 73 split + CGG-dotatie / city share + bestemde JUMP 2043117 + kapsubs JUMP 933642 + other recv JUMP 1417554 + 60.9 VTE payroll; do not keep leftover CGG unpublished,active,,tick1518; leftover recognized Flemish CGG after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover Motena Roeselare / leftover official-41 1464-1505"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Roeselare>EVA>CGG_Largo>JR2025_L5,{ENT},VKT-VZW publishes opbr 6764354 / 73 6391572 / omzet 251094; bestemde JUMP 2043117; kapsubs JUMP 933642; other recv JUMP 1417554; pers UP 5512029 / 60.9 VTE; PnL DROP 165138; dual city/Flanders envelope unpublished,Leftover recognized Flemish CGG of mined Roeselare + leftover Ieper + leftover Veurne with live JR2025; annual envelope 6.76m opbr / pers 5.51m 60.9 VTE / debt 1.29m / assets 6.03m,8,CGG Largo VZW / Departement Zorg Team Openbaarheid,openbaarheid@vlaanderen.be,Jules Lagaelaan 21 8800 Roeselare,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1518 leftover recognized Flemish CGG after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1520). NOT leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover Motena Roeselare / leftover official-41 1464-1505"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

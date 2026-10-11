#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:50:00Z"
ENT = "cgg_cgpt"
SRC = "src_cgpt_jr2025_nbb"
GAP = "gap_cgpt_opbr_10_29m_pers_9_38m_pnl_loss_l5"
LB = "lb_cgpt_opbr_10_29m_pers_9_38m_pnl_loss"
COMM = "comm_cgpt_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00167849.pdf"

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
    f"{COMM},CGG De Pont VZW JR2025 leftover recognized CGG dual (opbr 10.29m / 73 9.49m / pers 9.38m 103.3 VTE / cash JUMP 0.96m / beleg DROP 1.17m / PnL LOSS 61.9k / debt 2.63m DROP),{ENT},CGG De Pont / dual city Mechelen-Lier-Boom / Departement Zorg CGG-dotatie,WVV VZW; Decreet geestelijke gezondheidszorg; Bestuursdecreet openbaarheid,2026-06-03,2000,,10287468,,,active,{PDF},Local leftover CGG map VL Mechelen — opbr 10.29m / 73 9.49m / pers 9.38m 103.3 VTE / cash JUMP 0.96m,Publish 73 CGG-dotatie / city share + cash JUMP + beleg DROP + overgedragen-to-bestemde + 103.3 VTE payroll + PnL LOSS; do not keep leftover CGG unpublished,{SRC},strong,Vlaanderen>Gemeenten>Mechelen>EVA>CGG_DePont>JR2025_L5,tick1514; assets 7371989 omzet 485306 73 9488056 opbr 10287468 pers 9380342 103.3 VTE pnl -61881 equity 4737871 cash 955481 debt 2634118 capex 130253 dividend 0 nrec 76A 133835; FOI ready not sent; not TE-additive of 348bn; next every-10 1520"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CGG De Pont VZW JR2025 leftover recognized CGG: opbr 10.29m / 73 9.49m / pers 9.38m 103.3 VTE / cash JUMP 0.96m / beleg DROP 1.17m / PnL LOSS 61.9k / debt 2.63m DROP,L5,local_budget_line,Vlaanderen>Gemeenten>Mechelen>EVA>CGG_DePont>JR2025_L5,10287468,7371989,Leftover dual CGG VZW shell: assets 7.37m / equity 4.74m / opbr 10.29m / omzet 0.49m / 73 9.49m / pers 9.38m 103.3 VTE / cash JUMP 0.96m / beleg DROP 1.17m / PnL LOSS 61.9k,strong,{SRC},CGG De Pont / dual city Mechelen-Lier-Boom / Departement Zorg CGG-dotatie,Local leftover CGG map VL Mechelen — JR2025 official NBB WVV live; cash JUMP + beleg DROP + PnL LOSS FOI,Official NBB WVV 2026-08-20: opbr 10.29m / pers 9.38m 103.3 VTE / cash JUMP 0.96m / PnL LOSS 61.9k / beleg DROP 1.17m,6.5,6.1,3.0,6.3,Publish 73 CGG-dotatie / city share + cash JUMP 955481 + beleg DROP 1170000 + overgedragen-to-bestemde + 103.3 VTE payroll + PnL LOSS 61881; do not keep leftover CGG unpublished,active,,tick1514; leftover recognized Flemish CGG after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Mechelen>EVA>CGG_DePont>JR2025_L5,{ENT},VOL-VZW publishes opbr 10287468 / 73 9488056 all subsidies / pers 9380342 103.3 VTE; cash JUMP 955481; beleg DROP 1170000; overgedragen 816526 to 0 into bestemde JUMP 2876174; nrec 76A JUMP 133835; PnL LOSS 61881; dual city/Flanders envelope unpublished,Leftover recognized Flemish CGG of mined Mechelen + leftover Lier Boom with live JR2025; annual envelope 10.29m opbr / pers 9.38m 103.3 VTE / debt 2.63m / assets 7.37m,8,CGG De Pont VZW / Departement Zorg Team Openbaarheid,openbaarheid@vlaanderen.be,Lange Ridderstraat 20 2800 Mechelen,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1514 leftover recognized Flemish CGG after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1520). NOT leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

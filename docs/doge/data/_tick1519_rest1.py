#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T00:15:12Z"
ENT = "cgg_cgan"
SRC = "src_cgan_jr2025_nbb"
GAP = "gap_cgan_opbr_10_80m_pers_9_30m_kapsubs_jump_l5"
LB = "lb_cgan_opbr_10_80m_pers_9_30m_kapsubs_jump"
COMM = "comm_cgan_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00103827.pdf"

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
    f"{COMM},CGG Andante VZW JR2025 leftover recognized CGG dual (opbr 10.80m / 73 9.66m / pers 9.30m 108.7 VTE / kapsubs JUMP 4.36m / in aanbouw JUMP 2.27m / other recv JUMP / PnL LOSS 38.8k / debt 2.16m UP),{ENT},CGG Andante / dual city Antwerpen / Departement Zorg CGG-dotatie,WVV VZW; Decreet geestelijke gezondheidszorg; Bestuursdecreet openbaarheid,2026-05-04,2000,,10796084,,,active,{PDF},Local leftover CGG map VL Antwerpen — opbr 10.80m / 73 9.66m / pers 9.30m 108.7 VTE / kapsubs JUMP 4.36m,Publish 73 split + CGG-dotatie / city share + kapsubs JUMP + in aanbouw JUMP + other recv JUMP + 108.7 VTE payroll; do not keep leftover CGG unpublished,{SRC},strong,Vlaanderen>Gemeenten>Antwerpen>EVA>CGG_Andante>JR2025_L5,tick1519; assets 10657318 omzet 802604 73 9664811 opbr 10796084 pers 9295936 108.7 VTE pnl -38833 equity 8493688 cash 1540487 debt 2163630 capex 1280560 dividend 0 nrec 76A 0 nrec 66A 0; FOI ready not sent; not TE-additive of 348bn; next every-10 1520"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CGG Andante VZW JR2025 leftover recognized CGG: opbr 10.80m / 73 9.66m / pers 9.30m 108.7 VTE / kapsubs JUMP 4.36m / in aanbouw JUMP 2.27m / other recv JUMP / PnL LOSS 38.8k / debt 2.16m UP,L5,local_budget_line,Vlaanderen>Gemeenten>Antwerpen>EVA>CGG_Andante>JR2025_L5,10796084,10657318,Leftover dual CGG VZW shell: assets 10.66m / equity 8.49m / opbr 10.80m / omzet 0.80m / 73 9.66m / pers 9.30m 108.7 VTE / kapsubs JUMP 4.36m / in aanbouw JUMP 2.27m / other recv JUMP / PnL LOSS 38.8k,strong,{SRC},CGG Andante / dual city Antwerpen / Departement Zorg CGG-dotatie,Local leftover CGG map VL Antwerpen — JR2025 official NBB WVV live; 73 split + kapsubs JUMP FOI,Official NBB WVV 2026-08-20: opbr 10.80m / pers 9.30m 108.7 VTE / kapsubs JUMP 4.36m / in aanbouw JUMP 2.27m / PnL LOSS 38.8k,6.6,6.4,3.0,6.3,Publish 73 split + CGG-dotatie / city share + kapsubs JUMP 4360723 + in aanbouw JUMP 2266750 + other recv JUMP + 108.7 VTE payroll; do not keep leftover CGG unpublished,active,,tick1519; leftover recognized Flemish CGG after leftover AGB/APB hunt; NEW unused recognized CGG not in 1507-1518 list; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG Largo 1518 / leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Antwerpen>EVA>CGG_Andante>JR2025_L5,{ENT},VOL-VZW publishes opbr 10796084 / 73 9664811 / omzet 802604; kapsubs JUMP 4360723; in aanbouw JUMP 2266750; other LT recv JUMP 1859107; other ST recv JUMP 2089584; bestemde JUMP 1490000; pers UP 9295936 / 108.7 VTE; PnL LOSS -38833; dual city/Flanders envelope unpublished,Leftover recognized Flemish CGG of mined Antwerpen with live JR2025; NEW unused recognized CGG not in 1507-1518 list; annual envelope 10.80m opbr / pers 9.30m 108.7 VTE / debt 2.16m / assets 10.66m,8,CGG Andante VZW / Departement Zorg Team Openbaarheid,openbaarheid@vlaanderen.be,Herculusstraat 17 2600 Berchem (Antwerpen),docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1519 leftover recognized Flemish CGG after honest leftover AGB/APB hunt; NEW unused recognized CGG not in 1507-1518 list; live JR2025 official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1520). NOT leftover CGG Largo 1518 / leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

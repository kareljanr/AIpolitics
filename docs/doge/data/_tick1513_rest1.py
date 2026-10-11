#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:40:00Z"
ENT = "cgg_cgpr"
SRC = "src_cgpr_jr2025_nbb"
GAP = "gap_cgpr_bruto_4_19m_pers_4_14m_inb_jump_l5"
LB = "lb_cgpr_bruto_4_19m_pers_4_14m_inb_jump"
COMM = "comm_cgpr_jr2025_bruto"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00209149.pdf"

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
    f"{COMM},CGG Prisma VZW JR2025 leftover recognized CGG dual (bruto 4.19m / omzet+73 empty / pers 4.14m 47.8 VTE / cash DROP 0.29m / in aanbouw JUMP 2.01m / debt 3.23m UP / PnL LOSS 90.6k),{ENT},CGG Prisma / dual city Blankenberge-Oostende-Torhout-Beernem / Departement Zorg CGG-dotatie,WVV VZW; Decreet geestelijke gezondheidszorg; Bestuursdecreet openbaarheid,2026-06-09,2000,,4186449,,,active,{PDF},Local leftover CGG map VL Blankenberge — bruto 4.19m / omzet+73 empty / pers 4.14m 47.8 VTE / cash DROP 0.29m,Publish omzet+73 split + CGG-dotatie / city share + in aanbouw JUMP + cash DROP + 47.8 VTE payroll; do not keep leftover CGG unpublished,{SRC},strong,Vlaanderen>Gemeenten>Blankenberge>EVA>CGG_Prisma>JR2025_L5,tick1513; assets 8441644 omzet empty 73 empty bruto 4186449 pers 4142732 47.8 VTE pnl -90558 equity 5198486 cash 288830 debt 3234189 capex 1723701 dividend 0 nrec 76A 38650; FOI ready not sent; not TE-additive of 348bn; next every-10 1520"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CGG Prisma VZW JR2025 leftover recognized CGG: bruto 4.19m / omzet+73 empty / pers 4.14m 47.8 VTE / cash DROP 0.29m / in aanbouw JUMP 2.01m / debt 3.23m UP / PnL LOSS 90.6k,L5,local_budget_line,Vlaanderen>Gemeenten>Blankenberge>EVA>CGG_Prisma>JR2025_L5,4186449,8441644,Leftover dual CGG VZW shell: assets 8.44m / equity 5.20m / bruto 4.19m / omzet empty / 73 empty / pers 4.14m 47.8 VTE / cash DROP 0.29m / in aanbouw JUMP 2.01m / capex 1.72m / PnL LOSS 90.6k,strong,{SRC},CGG Prisma / dual city Blankenberge-Oostende-Torhout-Beernem / Departement Zorg CGG-dotatie,Local leftover CGG map VL Blankenberge — JR2025 official NBB WVV live; omzet+73 empty + in aanbouw JUMP FOI,Official NBB WVV 2026-08-20: bruto 4.19m / pers 4.14m 47.8 VTE / cash DROP 0.29m / PnL LOSS 90.6k / in aanbouw JUMP 2.01m,6.5,5.9,3.0,6.2,Publish omzet+73 split + CGG-dotatie / city share + in aanbouw JUMP 2010659 + cash DROP 288830 + capex 1723701 + 47.8 VTE payroll; do not keep leftover CGG unpublished,active,,tick1513; leftover recognized Flemish CGG after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover WV Blankenberge 1506 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Blankenberge>EVA>CGG_Prisma>JR2025_L5,{ENT},VKT-VZW publishes bruto 4186449 but omzet 70 and 73 empty; cash DROP 288830; in aanbouw JUMP 2010659; capex 1723701; nrec 76A JUMP 38650; debt UP 3234189; PnL LOSS 90558; dual city/Flanders envelope unpublished,Leftover recognized Flemish CGG of mined Blankenberge + leftover Oostende Torhout Beernem with live JR2025; annual envelope 4.19m bruto / pers 4.14m 47.8 VTE / debt 3.23m / assets 8.44m,8,CGG Prisma VZW / Departement Zorg Team Openbaarheid,openbaarheid@vlaanderen.be,Astridlaan 35 8370 Blankenberge,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1513 leftover recognized Flemish CGG after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1520). NOT leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover WV Blankenberge 1506 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

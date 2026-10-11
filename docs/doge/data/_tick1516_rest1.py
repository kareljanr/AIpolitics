#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:54:00Z"
ENT = "cgg_cgkp"
SRC = "src_cgkp_jr2025_nbb"
GAP = "gap_cgkp_bruto_10_12m_pers_8_39m_expl_jump_l5"
LB = "lb_cgkp_bruto_10_12m_pers_8_39m_expl_jump"
COMM = "comm_cgkp_jr2025_bruto"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00178615.pdf"

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
    f"{COMM},CGG Kempen VZW JR2025 leftover recognized CGG dual (bruto 10.12m / omzet+73 empty / pers 8.39m 99.5 VTE / cash DROP 1.53m / beleg JUMP 0.30m / expl JUMP 0.75m / PnL JUMP 0.69m / debt 4.06m DROP),{ENT},CGG Kempen / dual city Geel-Kempen / Departement Zorg CGG-dotatie,WVV VZW; Decreet geestelijke gezondheidszorg; Bestuursdecreet openbaarheid,2026-06-10,2000,,10124140,,,active,{PDF},Local leftover CGG map VL Geel — bruto 10.12m / omzet+73 empty / pers 8.39m 99.5 VTE / expl JUMP 0.75m,Publish omzet+73 split + CGG-dotatie / city share + expl JUMP + cash DROP + beleg JUMP + 99.5 VTE payroll; do not keep leftover CGG unpublished,{SRC},strong,Vlaanderen>Gemeenten>Geel>EVA>CGG_Kempen>JR2025_L5,tick1516; assets 10466965 omzet empty 73 empty bruto 10124140 pers 8390551 99.5 VTE pnl 688968 equity 6409473 cash 1534479 debt 4057491 capex 118276 dividend 0 nrec 76A empty; FOI ready not sent; not TE-additive of 348bn; next every-10 1520"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CGG Kempen VZW JR2025 leftover recognized CGG: bruto 10.12m / omzet+73 empty / pers 8.39m 99.5 VTE / cash DROP 1.53m / beleg JUMP 0.30m / expl JUMP 0.75m / PnL JUMP 0.69m / debt 4.06m DROP,L5,local_budget_line,Vlaanderen>Gemeenten>Geel>EVA>CGG_Kempen>JR2025_L5,10124140,10466965,Leftover dual CGG VZW shell: assets 10.47m / equity 6.41m / bruto 10.12m / omzet empty / 73 empty / pers 8.39m 99.5 VTE / cash DROP 1.53m / beleg JUMP 0.30m / expl JUMP 0.75m / PnL JUMP 0.69m,strong,{SRC},CGG Kempen / dual city Geel-Kempen / Departement Zorg CGG-dotatie,Local leftover CGG map VL Geel — JR2025 official NBB WVV live; omzet+73 empty + expl JUMP FOI,Official NBB WVV 2026-08-20: bruto 10.12m / pers 8.39m 99.5 VTE / cash DROP 1.53m / expl JUMP 0.75m / PnL JUMP 0.69m,6.5,6.3,3.0,6.3,Publish omzet+73 split + CGG-dotatie / city share + expl JUMP 750808 + cash DROP 1534479 + beleg JUMP 302335 + lev DROP 215944 + 99.5 VTE payroll; do not keep leftover CGG unpublished,active,,tick1516; leftover recognized Flemish CGG after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Geel>EVA>CGG_Kempen>JR2025_L5,{ENT},VKT-VZW publishes bruto 10124140 but omzet 70 and 73 empty; cash DROP 1534479; beleg JUMP 302335; expl JUMP 750808; PnL JUMP 688968; lev DROP 215944; handelsrecv JUMP 809739; other ST JUMP 199749; dual city/Flanders envelope unpublished,Leftover recognized Flemish CGG of mined Geel + leftover Kempen with live JR2025; annual envelope 10.12m bruto / pers 8.39m 99.5 VTE / debt 4.06m / assets 10.47m,8,CGG Kempen VZW / Departement Zorg Team Openbaarheid,openbaarheid@vlaanderen.be,Antwerpseweg 1 2440 Geel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1516 leftover recognized Flemish CGG after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1520). NOT leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

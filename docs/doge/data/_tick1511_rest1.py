#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T06:00:00Z"
ENT = "cgg_cgad"
SRC = "src_cgad_jr2025_nbb"
GAP = "gap_cgad_opbr_13_80m_pers_11_16m_cash_jump_l5"
LB = "lb_cgad_opbr_13_80m_pers_11_16m_cash_jump"
COMM = "comm_cgad_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00188352.pdf"

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
    f"{COMM},CGG Adentro VZW JR2025 leftover recognized CGG dual (opbr 13.80m / 73 13.17m / pers 11.16m 121.1 VTE / cash JUMP 2.91m / bestemde JUMP 4.36m / debt 2.34m DROP),{ENT},CGG Adentro / dual city Gent-Deinze-Eeklo / Departement Zorg CGG-dotatie,WVV VZW; Decreet geestelijke gezondheidszorg; Bestuursdecreet openbaarheid,2026-06-22,2000,,13798629,,,active,{PDF},Local leftover CGG map VL Gent — opbr 13.80m / 73 13.17m / pers 11.16m 121.1 VTE / cash JUMP 2.91m,Publish 73 CGG-dotatie / city share + cash JUMP + bestemde JUMP + 121.1 VTE payroll; do not keep leftover CGG unpublished,{SRC},strong,Vlaanderen>Gemeenten>Gent>EVA>CGG_Adentro>JR2025_L5,tick1511; assets 9833698 omzet 597815 73 13172501 pers 11157856 121.1 VTE pnl 598359 equity 7390848 cash 2905244 debt 2344595 capex 94989 dividend 0 nrec 76A empty; FOI ready not sent; not TE-additive of 348bn; next every-10 1520"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CGG Adentro VZW JR2025 leftover recognized CGG: opbr 13.80m / 73 13.17m / pers 11.16m 121.1 VTE / cash JUMP 2.91m / bestemde JUMP 4.36m / debt 2.34m DROP,L5,local_budget_line,Vlaanderen>Gemeenten>Gent>EVA>CGG_Adentro>JR2025_L5,13798629,9833698,Leftover dual CGG VZW shell: assets 9.83m / equity 7.39m / opbr 13.80m / omzet 0.60m / 73 13.17m / pers 11.16m 121.1 VTE / cash JUMP 2.91m / bestemde JUMP 4.36m / diensten 1.64m / PnL +0.60m,strong,{SRC},CGG Adentro / dual city Gent-Deinze-Eeklo / Departement Zorg CGG-dotatie,Local leftover CGG map VL Gent — JR2025 official NBB WVV live; 73 + cash/bestemde JUMP FOI,Official NBB WVV 2026-08-20: opbr 13.80m / pers 11.16m 121.1 VTE / cash JUMP 2.91m / PnL +0.60m / 73 13.17m,6.6,6.8,3.0,6.5,Publish 73 CGG-dotatie / city share + cash JUMP 2905244 + bestemde JUMP 4355670 + diensten 1641099 + 121.1 VTE payroll; do not keep leftover CGG unpublished,active,,tick1511; leftover recognized Flemish CGG after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Gent>EVA>CGG_Adentro>JR2025_L5,{ENT},VOL-VZW publishes 73 13172501 but CGG-dotatie / city share unpublished as a split; cash JUMP 2905244; bestemde JUMP 4355670; diensten 61 1641099; trade recv 1295655; dual city/Flanders envelope unpublished,Leftover recognized Flemish CGG of mined Gent + leftover Deinze Eeklo with live JR2025; annual envelope 13.80m opbr / pers 11.16m 121.1 VTE / debt 2.34m / assets 9.83m,8,CGG Adentro VZW / Departement Zorg Team Openbaarheid,openbaarheid@vlaanderen.be,Elyzeese Velden 74 9000 Gent,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1511 leftover recognized Flemish CGG after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1520). NOT leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

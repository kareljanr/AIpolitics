#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T05:00:00Z"
ENT = "cgg_cgzo"
SRC = "src_cgzo_jr2025_nbb"
GAP = "gap_cgzo_opbr_7_62m_pers_6_09m_voorz_jump_l5"
LB = "lb_cgzo_opbr_7_62m_pers_6_09m_voorz_jump"
COMM = "comm_cgzo_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00195156.pdf"

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
    f"{COMM},CGG Zuid-Oost-Vlaanderen VZW JR2025 leftover recognized CGG dual (opbr 7.62m / 73 5.30m / pers 6.09m 65.8 VTE / cash JUMP 0.14m / beleg JUMP 2.38m / voorz JUMP 0.18m / debt 1.42m),{ENT},CGG ZOV / dual city Aalst-Ninove-Geraardsbergen-Oudenaarde / Departement Zorg CGG-dotatie,WVV VZW; Decreet geestelijke gezondheidszorg; Bestuursdecreet openbaarheid,2026-06-04,2000,,7623192,,,active,{PDF},Local leftover CGG map VL Aalst — opbr 7.62m / 73 5.30m / pers 6.09m 65.8 VTE / cash JUMP 0.14m,Publish 73 CGG-dotatie / city share + andere 74 JUMP 2.04m + diensten JUMP 1.02m + voorz JUMP 0.18m + 65.8 VTE payroll; do not keep leftover CGG unpublished,{SRC},strong,Vlaanderen>Gemeenten>Aalst>EVA>CGG_ZOV>JR2025_L5,tick1510; assets 6678603 omzet 112615 73 5295335 pers 6091984 65.8 VTE pnl 140404 equity 5076165 cash 139180 debt 1420686 capex 34836 dividend 0 nrec 171612; FOI ready not sent; not TE-additive of 348bn; EVERY-10 next 1520"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CGG Zuid-Oost-Vlaanderen VZW JR2025 leftover recognized CGG: opbr 7.62m / 73 5.30m / pers 6.09m 65.8 VTE / cash JUMP 0.14m / andere 74 JUMP 2.04m / voorz JUMP 0.18m,L5,local_budget_line,Vlaanderen>Gemeenten>Aalst>EVA>CGG_ZOV>JR2025_L5,7623192,6678603,Leftover dual CGG VZW shell: assets 6.68m / equity 5.08m / opbr 7.62m / omzet 0.11m / 73 5.30m / pers 6.09m 65.8 VTE / cash JUMP 0.14m / andere 74 JUMP 2.04m / diensten JUMP 1.02m / voorz JUMP 0.18m / PnL +0.14m,strong,{SRC},CGG ZOV / dual city Aalst-Ninove-Geraardsbergen-Oudenaarde / Departement Zorg CGG-dotatie,Local leftover CGG map VL Aalst — JR2025 official NBB WVV live; 73 + andere-74/voorz JUMP FOI,Official NBB WVV 2026-08-20: opbr 7.62m / pers 6.09m 65.8 VTE / cash JUMP 0.14m / PnL +0.14m / 73 5.30m,6.5,6.5,3.0,6.4,Publish 73 CGG-dotatie / city share + andere 74 JUMP 2043630 + diensten JUMP 1018389 + voorz JUMP 181752 + cash JUMP + 65.8 VTE payroll; do not keep leftover CGG unpublished,active,,tick1510; leftover recognized Flemish CGG after leftover AGB/APB hunt; FOI ready not sent; EVERY-10; not TE-additive of 348bn; distinct from leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Aalst>EVA>CGG_ZOV>JR2025_L5,{ENT},VOL-VZW publishes 73 5295335 but CGG-dotatie / city share unpublished as a split; andere 74 JUMP 2043630; diensten 61 JUMP 1018389; cash JUMP 139180; beleg JUMP 2375000; voorzieningen JUMP 181752; nrec 76A 171612; dual city/Flanders envelope unpublished,Leftover recognized Flemish CGG of mined Aalst + leftover Ninove Geraardsbergen Oudenaarde with live JR2025; annual envelope 7.62m opbr / pers 6.09m 65.8 VTE / debt 1.42m / assets 6.68m,8,CGG Zuid-Oost-Vlaanderen VZW / Departement Zorg Team Openbaarheid,openbaarheid@vlaanderen.be,Keizersplein 4 9300 Aalst,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1510 leftover recognized Flemish CGG after honest leftover AGB/APB hunt; live JR2025 official NBB WVV PDF. FOI ready not sent. EVERY-10 (next 1520). NOT leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover official-41 1464-1505"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

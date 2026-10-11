#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T00:48:03Z"
ENT = "igs_ivrm"
SRC = "src_ivrm_jr2025_nbb"
GAP = "gap_ivrm_omzet_34_82m_pers_12_43m_debt_jump_l5"
LB = "lb_ivrm_omzet_34_82m_pers_12_43m_debt_jump"
COMM = "comm_ivrm_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00373329.pdf"

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
    f"{COMM},IVAREM JR2025 leftover IGS dual (omzet 34.82m / opbr 35.14m / pers 12.43m 165.8 VTE / debt JUMP 37.24m / cash JUMP 8.11m / PnL LOSS 2.24m / capex 16.37m),{ENT},IVAREM / dual mined Mechelen-region cities / recyclagepark fees,WVV opdrachthoudende vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid,2026-06-19,1970,,34824643,,,active,{PDF},Local leftover IGS map VL Mechelen-region waste — omzet 34.82m / pers 12.43m 165.8 VTE / debt JUMP 37.24m / PnL LOSS 2.24m,Publish 70 split + city vs household vs OVAM + LT-bank JUMP 18.68m + capex 16.37m + commissaris fee; do not keep leftover IVAREM unpublished,{SRC},strong,Vlaanderen>Gemeenten>Mechelen>IGS>IVAREM>JR2025_L5,tick1524; assets 61398227 omzet 34824643 opbr 35143041 pers 12430050 165.8 VTE pnl -2241145 equity 18801904 cash 8106299 debt 37235254 capex 16367406 dividend 0 nrec 76A 0; FOI ready not sent; not TE-additive of 348bn; next every-10 1530"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},IVAREM JR2025 leftover IGS: omzet 34.82m / opbr 35.14m / pers 12.43m 165.8 VTE / debt JUMP 37.24m / cash JUMP 8.11m / PnL LOSS 2.24m / capex 16.37m,L5,local_budget_line,Vlaanderen>Gemeenten>Mechelen>IGS>IVAREM>JR2025_L5,34824643,61398227,Leftover dual IGS shell: assets 61.40m / equity 18.80m / omzet 34.82m / opbr 35.14m / pers 12.43m 165.8 VTE / cash JUMP 8.11m / debt JUMP 37.24m / PnL LOSS 2.24m,strong,{SRC},IVAREM / dual mined Mechelen-region cities / recyclagepark fees,Local leftover IGS map VL Mechelen-region waste — JR2025 official NBB WVV live; 70 split + LT-bank JUMP FOI,Official NBB WVV 2026-08-20: omzet 34.82m / pers 12.43m 165.8 VTE / debt JUMP 37.24m / PnL LOSS 2.24m,6.8,7.4,3.0,6.6,Publish 70 split + city vs household vs OVAM + LT-bank JUMP 18680625 + capex 16367406 + commissaris fee unpublished; do not keep leftover IVAREM unpublished,active,,tick1524; leftover IGS of mined Mechelen after leftover AGB/APB/CGG/Bosgroep hunt; TRUE JR2025 after prior Busibee false-alarm; FOI ready not sent; not TE-additive of 348bn; distinct from leftover IGEMO 1372 / leftover IOK Afvalbeheer / leftover PMBS / leftover CGG 1507-1523 / leftover official-41 1464-1505"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Mechelen>IGS>IVAREM>JR2025_L5,{ENT},VOL-inb publishes omzet 34824643 / opbr 35143041; 73 empty; 740 empty; cash JUMP 8106299; beleg DROP 4023373; debt JUMP 37235254; LT bank JUMP 18680625; other ST JUMP 4653605; handelsrecv JUMP 7332306; diensten JUMP 17687984; expl LOSS -2080142; PnL LOSS -2241145; pers UP 12430050 / 165.8 VTE; capex 16367406; commissaris fee unpublished; dual city/household/OVAM split unpublished,Leftover IGS of mined Mechelen-region cities with live JR2025; prior ticks listed JR2024 / Busibee 2025 false-alarm; annual envelope 34.82m omzet / pers 12.43m 165.8 VTE / debt JUMP 37.24m / assets 61.40m,8,IVAREM / dienst openbaarheid,boekhouding@ivarem.be,Leuvensesteenweg 443 bus D 2812 Muizen (Mechelen),docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1524 leftover IGS after honest leftover AGB/APB/CGG/Bosgroep hunt; TRUE JR2025 official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1530). NOT leftover IGEMO 1372 / leftover IOK Afvalbeheer / leftover PMBS / leftover CGG 1507-1523 / leftover official-41 1464-1505"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T00:54:31Z"
ENT = "caw_cwan"
SRC = "src_cwan_jr2025_nbb"
GAP = "gap_cwan_opbr_52_46m_pers_43_21m_cash_drop_l5"
LB = "lb_cwan_opbr_52_46m_pers_43_21m_cash_drop"
COMM = "comm_cwan_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00112717.pdf"

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
    f"{COMM},CAW Antwerpen JR2025 leftover zorg EVA dual (opbr 52.46m / 73 47.45m / pers 43.21m 596.7 VTE / cash DROP 1.00m / PnL LOSS 76.9k / capex 1.70m),{ENT},CAW Antwerpen / dual mined Antwerp-region cities / Departement Zorg subsidies,WVV vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid,2026-04-28,1970,,52460317,,,active,{PDF},Local leftover zorg EVA map VL Antwerp-region CAW — opbr 52.46m / pers 43.21m 596.7 VTE / cash DROP 1.00m / PnL LOSS 76.9k,Publish 73 split + city vs Departement Zorg + cash DROP + in-aanbouw JUMP + commissaris fee; do not keep leftover CAW Antwerpen unpublished,{SRC},strong,Vlaanderen>Gemeenten>Antwerpen>CAW>CAW_Antwerpen>JR2025_L5,tick1525; assets 16778368 omzet 3691060 73 47451115 opbr 52460317 pers 43212061 596.7 VTE pnl -76893 equity 6183712 cash 1004443 debt 10594656 capex 1704942 dividend 0 nrec 76A 179376; FOI ready not sent; not TE-additive of 348bn; next every-10 1530"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CAW Antwerpen JR2025 leftover zorg EVA: opbr 52.46m / 73 47.45m / pers 43.21m 596.7 VTE / cash DROP 1.00m / PnL LOSS 76.9k / capex 1.70m,L5,local_budget_line,Vlaanderen>Gemeenten>Antwerpen>CAW>CAW_Antwerpen>JR2025_L5,52460317,16778368,Leftover dual zorg EVA shell: assets 16.78m / equity 6.18m / opbr 52.46m / 73 47.45m / pers 43.21m 596.7 VTE / cash DROP 1.00m / debt 10.59m / PnL LOSS 76.9k,strong,{SRC},CAW Antwerpen / dual mined Antwerp-region cities / Departement Zorg subsidies,Local leftover zorg EVA map VL Antwerp-region CAW — JR2025 official NBB WVV live; 73 split + cash DROP FOI,Official NBB WVV 2026-08-20: opbr 52.46m / pers 43.21m 596.7 VTE / cash DROP 1.00m / PnL LOSS 76.9k,6.8,7.4,3.0,6.6,Publish 73 split + city vs Departement Zorg + cash DROP 1004443 + in-aanbouw JUMP 1315042 + commissaris 17768; do not keep leftover CAW Antwerpen unpublished,active,,tick1525; leftover recognized CAW of mined Antwerpen after leftover AGB/APB/CGG/Bosgroep/IVAREM hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG VAGGA 1512 / leftover CGG Andante 1519 / leftover umbrella caw_vl / leftover IVAREM 1524 / leftover CGG 1507-1523 / leftover official-41 1464-1505"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Antwerpen>CAW>CAW_Antwerpen>JR2025_L5,{ENT},VOL-VZW publishes opbr 52460317 / omzet 3691060 / 73 47451115 (733 47054006 + 731 57420); 6.9 70 split empty; cash DROP 1004443; beleg empty; debt 10594656; in aanbouw JUMP 1315042; handelsrecv JUMP 1386339; diensten JUMP 6708907; expl LOSS -209028; PnL LOSS -76893; pers UP 43212061 / 596.7 VTE; capex 1704942; nrec 66A JUMP 133083; dual city/Departement Zorg split unpublished,Leftover recognized Flemish CAW / leftover zorg EVA of mined Antwerpen with live JR2025; first per-CAW L5 after umbrella caw_vl; annual envelope 52.46m opbr / pers 43.21m 596.7 VTE / cash DROP 1.00m / assets 16.78m,8,CAW Antwerpen / dienst openbaarheid,info@cawantwerpen.be,Lange Lozanastraat 200 2018 Antwerpen,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1525 leftover recognized CAW after honest leftover AGB/APB/CGG/Bosgroep/IVAREM hunt; official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1530). NOT leftover CGG VAGGA 1512 / leftover CGG Andante 1519 / leftover umbrella caw_vl / leftover IVAREM 1524 / leftover CGG 1507-1523 / leftover official-41 1464-1505"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

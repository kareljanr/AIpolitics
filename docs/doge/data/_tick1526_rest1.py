#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T01:05:00Z"
ENT = "caw_cwkp"
SRC = "src_cwkp_jr2025_nbb"
GAP = "gap_cwkp_opbr_13_82m_pers_10_85m_73_split_l5"
LB = "lb_cwkp_opbr_13_82m_pers_10_85m_73_split"
COMM = "comm_cwkp_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00128692.pdf"

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
    f"{COMM},CAW De Kempen JR2025 leftover zorg EVA dual (opbr 13.82m / 73 12.80m / pers 10.85m 148 VTE / expl DROP 113k / PnL DROP 109k / capex 126k),{ENT},CAW De Kempen / dual mined Herentals + 27 Turnhout-arrondissement cities / Departement Zorg subsidies,WVV vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid,2026-05-12,1970,,13824525,,,active,{PDF},Local leftover zorg EVA map VL Kempen CAW — opbr 13.82m / pers 10.85m 148 VTE / expl DROP 113k / PnL DROP 109k,Publish 73 split (6.9 only 0.76m of 12.80m) + city vs Departement Zorg + expl DROP + taxsoc JUMP + commissaris fee; do not keep leftover CAW De Kempen unpublished,{SRC},strong,Vlaanderen>Gemeenten>Herentals>CAW>CAW_De_Kempen>JR2025_L5,tick1526; assets 19957060 omzet 595237 73 12796950 opbr 13824525 pers 10852214 148 VTE pnl 109444 equity 12442247 cash 674251 debt 7514813 capex 125774 dividend 0 nrec 76A empty; FOI ready not sent; not TE-additive of 348bn; next every-10 1530"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CAW De Kempen JR2025 leftover zorg EVA: opbr 13.82m / 73 12.80m / pers 10.85m 148 VTE / expl DROP 113k / PnL DROP 109k / 6.9 73 split incomplete,L5,local_budget_line,Vlaanderen>Gemeenten>Herentals>CAW>CAW_De_Kempen>JR2025_L5,13824525,19957060,Leftover dual zorg EVA shell: assets 19.96m / equity 12.44m / opbr 13.82m / 73 12.80m / pers 10.85m 148 VTE / cash 0.67m / debt 7.51m / PnL DROP 109k,strong,{SRC},CAW De Kempen / dual mined Herentals + 27 Turnhout-arrondissement cities / Departement Zorg subsidies,Local leftover zorg EVA map VL Kempen CAW — JR2025 official NBB WVV live; 73 split + expl DROP FOI,Official NBB WVV 2026-08-20: opbr 13.82m / pers 10.85m 148 VTE / expl DROP 113k / PnL DROP 109k,6.5,6.9,3.0,6.3,Publish 73 split (6.9 only 616853+143437 of 12796950) + city vs Departement Zorg + expl DROP 112979 + taxsoc JUMP 1936788 + commissaris 10250; do not keep leftover CAW De Kempen unpublished,active,,tick1526; leftover recognized CAW of mined Herentals after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG Kempen 1516 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover Welzijnszorg Kempen / leftover De Noorderkempen 1504 / leftover Erfgoed Noorderkempen 1426 / leftover CGG 1507-1523 / leftover official-41 1464-1505"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Herentals>CAW>CAW_De_Kempen>JR2025_L5,{ENT},VOL-VZW publishes opbr 13824525 / omzet 595237 / 73 12796950 but 6.9 only 733 616853 + 731 143437 = 760290; 6.9 70 split empty; cash 674251; beleg JUMP 2200000; debt 7514813; taxsoc JUMP 1936788; diensten JUMP 1611119; expl DROP 112979 (was 818514); PnL DROP 109444 (was 818572); pers 10852214 / 148 VTE; capex 125774; dual city/Departement Zorg split unpublished,Leftover recognized Flemish CAW / leftover zorg EVA of mined Herentals with live JR2025; second per-CAW L5 after CAW Antwerpen 1525; annual envelope 13.82m opbr / pers 10.85m 148 VTE / expl DROP 113k / assets 19.96m,8,CAW De Kempen / dienst openbaarheid,onthaal@cawdekempen.be,Hofkwartier 23 2200 Herentals,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1526 leftover recognized CAW after honest leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen hunt; official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1530). NOT leftover CGG Kempen 1516 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover Welzijnszorg Kempen / leftover De Noorderkempen 1504 / leftover Erfgoed Noorderkempen 1426 / leftover CGG 1507-1523 / leftover official-41 1464-1505"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

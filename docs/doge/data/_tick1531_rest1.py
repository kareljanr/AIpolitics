#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
import subprocess
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "caw_cwlm"
SRC = "src_cwlm_jr2025_nbb"
GAP = "gap_cwlm_opbr_25_35m_pers_20_15m_cash_drop_l5"
LB = "lb_cwlm_opbr_25_35m_pers_20_15m_cash_drop"
COMM = "comm_cwlm_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00099651.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def check(row, n, label):
    fields = next(csv.reader(io.StringIO(row)))
    got = len(fields)
    if got != n:
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:160]}")
    if any("," in f for f in fields):
        raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")

comm = (
    f"{COMM},CAW Limburg JR2025 leftover zorg EVA dual (opbr 25.35m / 73 23.04m / pers 20.15m 271.8 VTE / cash DROP 2.74m / handelsrecv JUMP 1.55m / other ST JUMP 2.30m),{ENT},CAW Limburg / dual mined Genk + remaining Limburg municipalities / Departement Zorg subsidies,WVV vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid,2026-04-29,1970,,25346747,,,active,{PDF},Local leftover zorg EVA map VL Genk CAW — opbr 25.35m / pers 20.15m 271.8 VTE / cash DROP 2.74m / other ST JUMP 2.30m,Publish 73 split (730 24162 + 733 23013331) + city vs Departement Zorg + cash DROP + handelsrecv JUMP + other ST JUMP + commissaris fee; do not keep leftover CAW Limburg unpublished,{SRC},strong,Vlaanderen>Gemeenten>Genk>CAW>CAW_Limburg>JR2025_L5,tick1531; assets 17396760 omzet 2047768 73 23037493 opbr 25346747 pers 20148522 271.8 VTE pnl 117423 equity 9082939 cash 2737774 debt 8313821 capex 959014 dividend 0 nrec 66A 30650; FOI ready not sent; not TE-additive of 348bn; next every-10 1540"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CAW Limburg JR2025 leftover zorg EVA: opbr 25.35m / 73 23.04m / pers 20.15m 271.8 VTE / cash DROP 2.74m / handelsrecv JUMP 1.55m / other ST JUMP 2.30m,L5,local_budget_line,Vlaanderen>Gemeenten>Genk>CAW>CAW_Limburg>JR2025_L5,25346747,17396760,Leftover dual zorg EVA shell: assets 17.40m / equity 9.08m / opbr 25.35m / 73 23.04m / pers 20.15m 271.8 VTE / cash 2.74m DROP / handelsrecv 1.55m JUMP / other ST 2.30m JUMP / debt 8.31m / expl 81.0k,strong,{SRC},CAW Limburg / dual mined Genk + remaining Limburg municipalities / Departement Zorg subsidies,Local leftover zorg EVA map VL Genk CAW — JR2025 official NBB WVV live; 73 split + cash DROP + recv JUMP + other ST JUMP FOI,Official NBB WVV 2026-08-20: opbr 25.35m / pers 20.15m 271.8 VTE / cash DROP 2.74m / PnL 117.4k,6.8,6.8,3.0,6.3,Publish 73 split (730 24162 + 733 23013331) + city vs Departement Zorg + cash DROP 2737774 + handelsrecv JUMP 1548222 + other recv JUMP 1626269 + other ST JUMP 2296113 + accrued DROP 370729 + IVA JUMP 189762 + commissaris 13950; do not keep leftover CAW Limburg unpublished,active,,tick1531; leftover recognized CAW of mined Genk after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486 / leftover LeefGoed 1481 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Genk>CAW>CAW_Limburg>JR2025_L5,{ENT},VOL-VZW publishes opbr 25346747 / omzet 2047768 (6.9 category empty) / 73 23037493 (730 24162 + 733 23013331; 731/732 empty); city vs Departement Zorg split unpublished; cash DROP 2737774 was 4502757; handelsrecv JUMP 1548222 was 802449; other recv JUMP 1626269 was 924925; other ST JUMP 2296113 was 1172644; accrued DROP 370729 was 1268941; IVA JUMP 189762; in-aanbouw JUMP 117823; diensten JUMP 3428070; pers 20148522 / 271.8 VTE DROP; capex 959014; dual city/Departement Zorg split unpublished,Leftover recognized Flemish CAW / leftover zorg EVA of mined Genk with live JR2025; seventh per-CAW L5 after CAW Antwerpen 1525 CAW De Kempen 1526 CAW Brussel 1527 CAW Rivierenland 1528 CAW Halle-Vilvoorde 1529 and CAW Oost-Brabant 1530; annual envelope 25.35m opbr / pers 20.15m 271.8 VTE / cash DROP 2.74m / assets 17.40m,8,CAW Limburg / dienst openbaarheid,guy.guisson@cawlimburg.be,Welzijnscampus 19 bus 2 3600 Genk,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1531 leftover recognized CAW after honest leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant hunt; official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1540). NOT leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486 / leftover LeefGoed 1481 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

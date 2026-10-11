#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T01:10:00Z"
ENT = "caw_cwbr"
SRC = "src_cwbr_jr2025_nbb"
GAP = "gap_cwbr_opbr_13_38m_pers_11_59m_pnl_loss_l5"
LB = "lb_cwbr_opbr_13_38m_pers_11_59m_pnl_loss"
COMM = "comm_cwbr_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00101211.pdf"

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
    f"{COMM},CAW Brussel JR2025 leftover zorg EVA dual (opbr 13.38m / 73 12.81m / pers 11.59m 160.2 VTE / expl LOSS 24k / PnL LOSS 25k / cash DROP 0.93m),{ENT},CAW Brussel / dual mined Brussel + 18 other BHG cities / Departement Zorg subsidies,WVV vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid,2026-04-20,1970,,13378953,,,active,{PDF},Local leftover zorg EVA map VL Brussels CAW — opbr 13.38m / pers 11.59m 160.2 VTE / expl LOSS 24k / PnL LOSS 25k,Publish 73 split (733 12.80m of 12.81m) + city vs Departement Zorg + cash DROP + other ST JUMP + commissaris fee; do not keep leftover CAW Brussel unpublished,{SRC},strong,Vlaanderen>Gemeenten>Brussel>CAW>CAW_Brussel>JR2025_L5,tick1527; assets 6760334 omzet 458249 73 12807697 opbr 13378953 pers 11589623 160.2 VTE pnl -24907 equity 3246857 cash 926690 debt 3508957 capex 179775 dividend 0 nrec 76A 10098; FOI ready not sent; not TE-additive of 348bn; next every-10 1530"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CAW Brussel JR2025 leftover zorg EVA: opbr 13.38m / 73 12.81m / pers 11.59m 160.2 VTE / expl LOSS 24k / PnL LOSS 25k / cash DROP 0.93m,L5,local_budget_line,Vlaanderen>Gemeenten>Brussel>CAW>CAW_Brussel>JR2025_L5,13378953,6760334,Leftover dual zorg EVA shell: assets 6.76m / equity 3.25m / opbr 13.38m / 73 12.81m / pers 11.59m 160.2 VTE / cash 0.93m DROP / debt 3.51m / PnL LOSS 25k,strong,{SRC},CAW Brussel / dual mined Brussel + 18 other BHG cities / Departement Zorg subsidies,Local leftover zorg EVA map VL Brussels CAW — JR2025 official NBB WVV live; 73 split + cash DROP + PnL LOSS FOI,Official NBB WVV 2026-08-20: opbr 13.38m / pers 11.59m 160.2 VTE / expl LOSS 24k / PnL LOSS 25k,6.5,6.8,3.0,6.2,Publish 73 split (733 12800465 of 12807697) + city vs Departement Zorg + cash DROP 926690 + other ST JUMP 262908 + prepaid JUMP 132336 + 74 DROP 102909 + commissaris 6516; do not keep leftover CAW Brussel unpublished,active,,tick1527; leftover recognized CAW of mined Brussel after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG Brussel 1521 / leftover CAW Antwerpen 1525 / leftover CAW De Kempen 1526 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Brussel>CAW>CAW_Brussel>JR2025_L5,{ENT},VOL-VZW publishes opbr 13378953 / omzet 458249 / 73 12807697 of which 733 12800465 + 731 7232; 6.9 70 split empty; cash DROP 926690 was 1582721; other ST JUMP 262908 was 109058; prepaid JUMP 132336; accrued DROP 81622 was 728280; 74 DROP 102909 was 406624; expl LOSS -23645; PnL LOSS -24907 was +11067; pers 11589623 / 160.2 VTE; capex 179775; dual city/Departement Zorg split unpublished,Leftover recognized Flemish CAW / leftover zorg EVA of mined Brussel with live JR2025; third per-CAW L5 after CAW Antwerpen 1525 and CAW De Kempen 1526; annual envelope 13.38m opbr / pers 11.59m 160.2 VTE / PnL LOSS 25k / assets 6.76m,8,CAW Brussel / dienst openbaarheid,algmeen@cawbrussel.be,Priemstraat 19A 1000 Brussel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1527 leftover recognized CAW after honest leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen hunt; official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1530). NOT leftover CGG Brussel 1521 / leftover CAW Antwerpen 1525 / leftover CAW De Kempen 1526 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T01:10:00Z"
ENT = "caw_cwrv"
SRC = "src_cwrv_jr2025_nbb"
GAP = "gap_cwrv_opbr_8_43m_pers_7_01m_expl_loss_l5"
LB = "lb_cwrv_opbr_8_43m_pers_7_01m_expl_loss"
COMM = "comm_cwrv_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00090859.pdf"

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
    f"{COMM},CAW Rivierenland JR2025 leftover zorg EVA dual (opbr 8.43m / 73 7.78m / pers 7.01m 95.1 VTE / expl LOSS 9k / PnL DROP 12k / cash DROP 0.31m / beleg DROP 1.50m),{ENT},CAW Rivierenland / dual mined Mechelen + 11 other Rivierenland cities / Departement Zorg subsidies,WVV vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid,2026-04-27,1970,,8432403,,,active,{PDF},Local leftover zorg EVA map VL Mechelen CAW — opbr 8.43m / pers 7.01m 95.1 VTE / expl LOSS 9k / PnL DROP 12k,Publish 73 split (733 7.76m of 7.78m) + city vs Departement Zorg + cash DROP + beleg DROP + expl LOSS + commissaris fee; do not keep leftover CAW Rivierenland unpublished,{SRC},strong,Vlaanderen>Gemeenten>Mechelen>CAW>CAW_Rivierenland>JR2025_L5,tick1528; assets 9362853 omzet 371409 73 7780184 opbr 8432403 pers 7006469 95.1 VTE pnl 11558 equity 5744350 cash 312739 debt 3564445 capex 107925 dividend 0 nrec 76A empty; FOI ready not sent; not TE-additive of 348bn; next every-10 1530"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CAW Rivierenland JR2025 leftover zorg EVA: opbr 8.43m / 73 7.78m / pers 7.01m 95.1 VTE / expl LOSS 9k / PnL DROP 12k / cash DROP 0.31m / beleg DROP 1.50m,L5,local_budget_line,Vlaanderen>Gemeenten>Mechelen>CAW>CAW_Rivierenland>JR2025_L5,8432403,9362853,Leftover dual zorg EVA shell: assets 9.36m / equity 5.74m / opbr 8.43m / 73 7.78m / pers 7.01m 95.1 VTE / cash 0.31m DROP / beleg 1.50m DROP / debt 3.56m / expl LOSS 9k,strong,{SRC},CAW Rivierenland / dual mined Mechelen + 11 other Rivierenland cities / Departement Zorg subsidies,Local leftover zorg EVA map VL Mechelen CAW — JR2025 official NBB WVV live; 73 split + cash DROP + beleg DROP + expl LOSS FOI,Official NBB WVV 2026-08-20: opbr 8.43m / pers 7.01m 95.1 VTE / expl LOSS 9k / PnL DROP 12k,6.5,6.6,3.0,6.1,Publish 73 split (733 7764361 of 7780184) + city vs Departement Zorg + cash DROP 312739 + beleg DROP 1500401 + 74 JUMP 280810 + other recv JUMP 146893 + vooruit JUMP 126267 + commissaris 8627; do not keep leftover CAW Rivierenland unpublished,active,,tick1528; leftover recognized CAW of mined Mechelen after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover Woonmaatschappij Rivierenland 1465 / leftover CGG De Pont 1514 / leftover IVAREM 1524 / leftover CAW Antwerpen 1525 / leftover CAW De Kempen 1526 / leftover CAW Brussel 1527 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Mechelen>CAW>CAW_Rivierenland>JR2025_L5,{ENT},VOL-VZW publishes opbr 8432403 / omzet 371409 / 73 7780184 of which 733 7764361 + 731 15823; 6.9 70 split empty; cash DROP 312739 was 507300; beleg DROP 1500401 was 2000400; other recv JUMP 146893 was 48604; vooruit JUMP 126267 was 23009; 74 JUMP 280810 was 79046; expl LOSS -9004 was +634632; PnL DROP 11558 was 661044; pers 7006469 / 95.1 VTE; capex 107925; dual city/Departement Zorg split unpublished,Leftover recognized Flemish CAW / leftover zorg EVA of mined Mechelen with live JR2025; fourth per-CAW L5 after CAW Antwerpen 1525 CAW De Kempen 1526 and CAW Brussel 1527; annual envelope 8.43m opbr / pers 7.01m 95.1 VTE / expl LOSS 9k / assets 9.36m,8,CAW Rivierenland / dienst openbaarheid,centraal.secretariaat@cawboommechelenlier.be,Maurits Sabbestraat 119 2800 Mechelen,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1528 leftover recognized CAW after honest leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel hunt; official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1530). NOT leftover Woonmaatschappij Rivierenland 1465 / leftover CGG De Pont 1514 / leftover IVAREM 1524 / leftover CAW Antwerpen 1525 / leftover CAW De Kempen 1526 / leftover CAW Brussel 1527 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

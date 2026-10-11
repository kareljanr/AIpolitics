#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
import subprocess
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "caw_cwov"
SRC = "src_cwov_jr2025_nbb"
GAP = "gap_cwov_opbr_43_87m_pers_37_30m_expl_loss_l5"
LB = "lb_cwov_opbr_43_87m_pers_37_30m_expl_loss"
COMM = "comm_cwov_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00117344.pdf"

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
    f"{COMM},CAW Oost-Vlaanderen JR2025 leftover zorg EVA dual (opbr 43.87m / 73 40.33m / pers 37.30m 506.3 VTE / expl LOSS 1.22m / cash DROP 8.41m / handelsrecv JUMP 3.14m),{ENT},CAW Oost-Vlaanderen / dual mined Gent + remaining Oost-Vlaanderen municipalities / Departement Zorg subsidies,WVV vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid,2026-04-23,1970,,43872173,,,active,{PDF},Local leftover zorg EVA map VL Gent CAW — opbr 43.87m / pers 37.30m 506.3 VTE / expl LOSS 1.22m / cash DROP 8.41m / handelsrecv JUMP 3.14m,Publish 73 split (731 76347 + 732 42207 + 733 40214356) + city vs Departement Zorg + cash DROP + handelsrecv JUMP + expl LOSS + commissaris fee; do not keep leftover CAW Oost-Vlaanderen unpublished,{SRC},strong,Vlaanderen>Gemeenten>Gent>CAW>CAW_Oost_Vlaanderen>JR2025_L5,tick1532; assets 32814654 omzet 2041949 73 40332909 opbr 43872173 pers 37299480 506.3 VTE pnl -1021215 equity 21806046 cash 8405654 debt 10810222 capex 885268 dividend 0 nrec 66A 328855; FOI ready not sent; not TE-additive of 348bn; next every-10 1540"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CAW Oost-Vlaanderen JR2025 leftover zorg EVA: opbr 43.87m / 73 40.33m / pers 37.30m 506.3 VTE / expl LOSS 1.22m / cash DROP 8.41m / handelsrecv JUMP 3.14m,L5,local_budget_line,Vlaanderen>Gemeenten>Gent>CAW>CAW_Oost_Vlaanderen>JR2025_L5,43872173,32814654,Leftover dual zorg EVA shell: assets 32.81m / equity 21.81m / opbr 43.87m / 73 40.33m / pers 37.30m 506.3 VTE / cash 8.41m DROP / handelsrecv 3.14m JUMP / expl LOSS 1.22m / debt 10.81m / PnL LOSS 1.02m,strong,{SRC},CAW Oost-Vlaanderen / dual mined Gent + remaining Oost-Vlaanderen municipalities / Departement Zorg subsidies,Local leftover zorg EVA map VL Gent CAW — JR2025 official NBB WVV live; 73 split + cash DROP + recv JUMP + expl LOSS FOI,Official NBB WVV 2026-08-20: opbr 43.87m / pers 37.30m 506.3 VTE / cash DROP 8.41m / expl LOSS 1.22m,6.8,7.1,3.0,6.5,Publish 73 split (731 76347 + 732 42207 + 733 40214356) + city vs Departement Zorg + cash DROP 8405654 + handelsrecv JUMP 3142271 + prepaid JUMP 203304 + accrued DROP 432627 + in-aanbouw JUMP 1544223 + 76A JUMP 533479 + commissaris 14791; do not keep leftover CAW Oost-Vlaanderen unpublished,active,,tick1532; leftover recognized CAW of mined Gent after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant/CAW-Limburg hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG Adentro 1511 / leftover Thuispunt Gent 1470 / leftover Dimensa 1466 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Gent>CAW>CAW_Oost_Vlaanderen>JR2025_L5,{ENT},VOL-VZW publishes opbr 43872173 / omzet 2041949 (6.9 category empty) / 73 40332909 (731 76347 + 732 42207 + 733 40214356; 730 empty); city vs Departement Zorg split unpublished; cash DROP 8405654 was 10210384; handelsrecv JUMP 3142271 was 1326010; other recv DROP 1955741 was 2918425; prepaid JUMP 203304 was 13634; accrued DROP 432627 was 1186514; in-aanbouw JUMP 1544223; 76A JUMP 533479; expl LOSS 1217212; pers 37299480 / 506.3 VTE DROP; capex 885268; dual city/Departement Zorg split unpublished,Leftover recognized Flemish CAW / leftover zorg EVA of mined Gent with live JR2025; eighth per-CAW L5 after CAW Antwerpen 1525 CAW De Kempen 1526 CAW Brussel 1527 CAW Rivierenland 1528 CAW Halle-Vilvoorde 1529 CAW Oost-Brabant 1530 and CAW Limburg 1531; annual envelope 43.87m opbr / pers 37.30m 506.3 VTE / expl LOSS 1.22m / cash DROP 8.41m / assets 32.81m,8,CAW Oost-Vlaanderen / dienst openbaarheid,marleenverhasselt@cawoostvlaanderen.be,Visserij 153 9000 Gent,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1532 leftover recognized CAW after honest leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant/CAW-Limburg hunt; official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1540). NOT leftover CGG Adentro 1511 / leftover Thuispunt Gent 1470 / leftover Dimensa 1466 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

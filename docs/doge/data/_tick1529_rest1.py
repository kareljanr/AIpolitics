#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T01:16:00Z"
ENT = "caw_cwhv"
SRC = "src_cwhv_jr2025_nbb"
GAP = "gap_cwhv_opbr_12_97m_pers_11_73m_expl_loss_l5"
LB = "lb_cwhv_opbr_12_97m_pers_11_73m_expl_loss"
COMM = "comm_cwhv_jr2025_opbr"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00124483.pdf"

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
    f"{COMM},CAW Halle-Vilvoorde JR2025 leftover zorg EVA dual (opbr 12.97m / 73 12.73m / pers 11.73m 159.2 VTE / expl LOSS 1.14m / PnL LOSS 1.05m / cash DROP 3.96m / in-aanbouw JUMP 0.68m),{ENT},CAW Halle-Vilvoorde / dual mined Asse + 35 other Halle-Vilvoorde cities / Departement Zorg subsidies,WVV vereniging; Decreet lokaal bestuur; Bestuursdecreet openbaarheid,2026-05-26,1970,,12971653,,,active,{PDF},Local leftover zorg EVA map VL Asse CAW — opbr 12.97m / pers 11.73m 159.2 VTE / expl LOSS 1.14m / PnL LOSS 1.05m,Publish 73 split (all 733 12.73m) + city vs Departement Zorg + cash DROP + in-aanbouw JUMP + expl LOSS + commissaris fee; do not keep leftover CAW Halle-Vilvoorde unpublished,{SRC},strong,Vlaanderen>Gemeenten>Asse>CAW>CAW_Halle_Vilvoorde>JR2025_L5,tick1529; assets 13485378 omzet 75857 73 12731598 opbr 12971653 pers 11730941 159.2 VTE pnl -1053552 equity 10876596 cash 3955937 debt 2608782 capex 794809 dividend 0 nrec 66A 47816; FOI ready not sent; not TE-additive of 348bn; next every-10 1530"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},CAW Halle-Vilvoorde JR2025 leftover zorg EVA: opbr 12.97m / 73 12.73m / pers 11.73m 159.2 VTE / expl LOSS 1.14m / PnL LOSS 1.05m / cash DROP 3.96m / in-aanbouw JUMP 0.68m,L5,local_budget_line,Vlaanderen>Gemeenten>Asse>CAW>CAW_Halle_Vilvoorde>JR2025_L5,12971653,13485378,Leftover dual zorg EVA shell: assets 13.49m / equity 10.88m / opbr 12.97m / 73 12.73m / pers 11.73m 159.2 VTE / cash 3.96m DROP / in-aanbouw 0.68m JUMP / debt 2.61m / expl LOSS 1.14m,strong,{SRC},CAW Halle-Vilvoorde / dual mined Asse + 35 other Halle-Vilvoorde cities / Departement Zorg subsidies,Local leftover zorg EVA map VL Asse CAW — JR2025 official NBB WVV live; 73 split + cash DROP + in-aanbouw JUMP + expl LOSS FOI,Official NBB WVV 2026-08-20: opbr 12.97m / pers 11.73m 159.2 VTE / expl LOSS 1.14m / PnL LOSS 1.05m,6.8,6.8,3.0,6.3,Publish 73 split (all 733 12731598) + city vs Departement Zorg + cash DROP 3955937 + in-aanbouw JUMP 681722 + 74 DROP 143808 + nrec 66A JUMP 47816 + taxsoc JUMP 1999329 + commissaris 9010; do not keep leftover CAW Halle-Vilvoorde unpublished,active,,tick1529; leftover recognized CAW of mined Asse after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover CGG Ahasverus 1517 / leftover AGA Asse / leftover Providentia 1501 / leftover AGB Vilvoorde / leftover Inter-Vilvoordse 1489 / leftover Woonpunt Zennevallei 1485 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Asse>CAW>CAW_Halle_Vilvoorde>JR2025_L5,{ENT},VOL-VZW publishes opbr 12971653 / omzet 75857 Sociale Winkel / 73 12731598 all 733 (730/731/732 empty); city vs Departement Zorg split unpublished; cash DROP 3955937 was 4591722; in-aanbouw JUMP 681722 was 4978; 74 DROP 143808 was 574501; nrec 66A JUMP 47816; taxsoc JUMP 1999329 was 1617273; expl LOSS -1136898 was +325869; PnL LOSS -1053552 was +466761; pers 11730941 / 159.2 VTE JUMP; capex 794809; dual city/Departement Zorg split unpublished,Leftover recognized Flemish CAW / leftover zorg EVA of mined Asse with live JR2025; fifth per-CAW L5 after CAW Antwerpen 1525 CAW De Kempen 1526 CAW Brussel 1527 and CAW Rivierenland 1528; annual envelope 12.97m opbr / pers 11.73m 159.2 VTE / expl LOSS 1.14m / assets 13.49m,8,CAW Halle-Vilvoorde / dienst openbaarheid,onthaal@cawhallevilvoorde.be,Poverstraat 75 bus 48 1731 Asse,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1529 leftover recognized CAW after honest leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland hunt; official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1530). NOT leftover CGG Ahasverus 1517 / leftover AGA Asse / leftover Providentia 1501 / leftover AGB Vilvoorde / leftover Inter-Vilvoordse 1489 / leftover Woonpunt Zennevallei 1485 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

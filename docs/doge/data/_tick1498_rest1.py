#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T22:00:00Z"
ENT = "wm_wpij"
SRC = "src_wpij_jr2025_nbb"
GAP = "gap_wpij_omzet_7_08m_pers_1_51m_debt_92m_l5"
LB = "lb_wpij_omzet_7_08m_pers_1_51m_debt_92m"
COMM = "comm_wpij_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00297388.pdf"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def check(row, n, label):
    got = len(next(csv.reader(io.StringIO(row))))
    if got != n:
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:160]}")

comm = (
    f"{COMM},Woonpijler JR2025 leftover woonmaatschappij dual (omzet 7.08m UP / pers 1.51m 17.4 VTE / debt 92.44m UP / cash 2.67m DROP / capex 19.33m / in aanbouw 22.96m JUMP / PnL LOSS 0.46m / dividend 0 / 1 VE),{ENT},Wetteren-Laarne-Lochristi / mined Wetteren+Laarne+Lochristi dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-07-03,1922,,7083881,,,active,{PDF},Local leftover woonmaatschappij map VL Wetteren-Laarne-Lochristi — omzet 7.08m / pers 1.51m 17.4 VTE / debt 92.44m / cash 2.67m DROP,Publish omzet+diensten+huur/koop split + 1 VE payroll + cash 2.67m DROP + LT krediet 83.97m counterparties + capex 19.33m + in aanbouw 22.96m JUMP + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 7.08m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Wetteren>Woonmaatschappij>Woonpijler>JR2025_L5,tick1498; assets 105006637 omzet 7083881 pers 1513868 pnl -463096 equity 12170207 cash 2667094 debt 92437291 capex 19327583 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover AGB Wetteren / leftover de Thuisbouwer 1497 / leftover Meetjesland 1496 / leftover Woonstart 1495 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck"
)
check(comm, 19, "commitments")
append_crlf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},Woonpijler JR2025 leftover woonmaatschappij: omzet 7.08m UP / pers 1.51m 17.4 VTE / debt 92.44m UP / cash 2.67m DROP / capex 19.33m / in aanbouw 22.96m JUMP / PnL LOSS 0.46m / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Wetteren>Woonmaatschappij>Woonpijler>JR2025_L5,7083881,105006637,Leftover dual woonmaatschappij shell: assets 105.01m UP / equity 12.17m / omzet 7.08m UP / pers 1.51m 17.4 VTE / cash 2.67m DROP / debt 92.44m UP / LT krediet 83.97m / capex 19.33m / in aanbouw 22.96m JUMP / PnL LOSS 0.46m / dividend 0 / 1 VE; do not treat 7.08m as TE-additive of 348bn,strong,{SRC},Woonpijler / mined Wetteren-Laarne-Lochristi dual housing,Local leftover woonmaatschappij map VL Wetteren-Laarne-Lochristi — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 7.08m UP / pers 1.51m 17.4 VTE / debt 92.44m UP / cash 2.67m DROP / PnL LOSS 0.46m / dividend 0 / 1 VE,7.0,8.0,3.0,6.8,Publish omzet+diensten+huur/koop split + 1 VE payroll + cash 2.67m DROP + LT krediet 83.97m counterparties + capex 19.33m + in aanbouw 22.96m JUMP + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 7.08m housing shell,active,,tick1498; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined de Thuisbouwer 1497 / Meetjesland 1496 / Woonstart 1495 / IJzer en Zee 1494 / Thuiswest 1493 / Woonsprong 1492 / Ons Onderdak 1491 / Zetus 1490 / Inter-Vilvoordse 1489 / Woonschakel 1488 / De Voorkempen 1487 / Wonen in Limburg 1486 / Woonpunt Zennevallei 1485 / leftover AGB Wetteren / leftover AGB HIM Hamme / leftover AGB Zele"
)
check(lb, 21, "leaderboard")
append_crlf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Wetteren>Woonmaatschappij>Woonpijler>JR2025_L5,{ENT},omzet 7083881 UP vs 5652106 + huur/koop split unpublished + diensten 61 2759089 vs 2190916 + pers 1513868 17.4 VTE vs 16.5 + 1 VE + cash 2667094 DROP vs 3462411 + debt 92437291 UP LT krediet 83973820 + capex 19327583 + in aanbouw 22959832 JUMP + PnL -463096 vs 212474 + dividend 0 + aandeel % unpublished,Leftover woonmaatschappij Woonpijler after leftover AGB/APB hunt: omzet 7.08m UP / pers 1.51m 17.4 VTE / debt 92.44m UP / cash 2.67m DROP / capex 19.33m / in aanbouw 22.96m JUMP / PnL LOSS 0.46m / dividend 0 / 1 VE hides municipal housing vehicle,8,Woonpijler / Bestuursorgaan / voorzitter Michael Beeckman,info@woonpijler.be,Felix Beernaertsplein 55/01 9230 Wetteren,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1498 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (4489764 bytes 140p). FOI ready not sent. NOT every-10 (next 1500). NOT leftover AGB Wetteren / leftover de Thuisbouwer 1497 / leftover Meetjesland 1496 / leftover Woonstart 1495 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. Puyenbroeck still 302. de Thuisbouwer 1497 TAKEN. Woonpijler TAKEN this tick."
)
check(foi, 21, "foi_queue")
append_crlf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T21:00:00Z"
ENT = "wm_wstrt"
SRC = "src_wstrt_jr2025_nbb"
GAP = "gap_wstrt_omzet_7_33m_pers_1_54m_debt_82m_l5"
LB = "lb_wstrt_omzet_7_33m_pers_1_54m_debt_82m"
COMM = "comm_wstrt_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00159134.pdf"

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
    f"{COMM},Woonstart JR2025 leftover woonmaatschappij dual (omzet 7.33m UP / pers 1.54m 17.1 VTE / debt 81.70m UP / cash 2.04m UP / capex 31.84m JUMP / PnL -0.84m / dividend 0 / 1 VE),{ENT},Tielt-Midwest-Oost / mined Tielt+Pittem+Wingene dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-06-09,1923,,7325986,,,active,{PDF},Local leftover woonmaatschappij map VL Tielt-Midwest-Oost — omzet 7.33m / pers 1.54m 17.1 VTE / debt 81.70m / cash 2.04m UP,Publish omzet+diensten+huur/koop split + 1 VE payroll + cash 2.04m UP + LT krediet 75.67m counterparties + capex 31.84m JUMP + in aanbouw 1.37m DROP + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 7.33m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Tielt>Woonmaatschappij>Woonstart>JR2025_L5,tick1495; assets 97529158 omzet 7325986 pers 1536245 pnl -835178 equity 15514356 cash 2036624 debt 81699993 capex 31842106 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover AGB Tielt / leftover Woonstroom 1475 / leftover Thuiswest 1493 / leftover IJzer en Zee 1494 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck"
)
check(comm, 19, "commitments")
append_crlf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},Woonstart JR2025 leftover woonmaatschappij: omzet 7.33m UP / pers 1.54m 17.1 VTE / debt 81.70m UP / cash 2.04m UP / capex 31.84m JUMP / PnL -0.84m / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Tielt>Woonmaatschappij>Woonstart>JR2025_L5,7325986,97529158,Leftover dual woonmaatschappij shell: assets 97.53m UP / equity 15.51m / omzet 7.33m UP / pers 1.54m 17.1 VTE / cash 2.04m UP / debt 81.70m UP / LT krediet 75.67m / capex 31.84m JUMP / PnL -0.84m / dividend 0 / 1 VE; do not treat 7.33m as TE-additive of 348bn,strong,{SRC},Woonstart / mined Tielt-Midwest-Oost dual housing,Local leftover woonmaatschappij map VL Tielt-Midwest-Oost — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 7.33m UP / pers 1.54m 17.1 VTE / debt 81.70m UP / cash 2.04m UP / PnL -0.84m / dividend 0 / 1 VE,7.0,8.0,3.0,6.8,Publish omzet+diensten+huur/koop split + 1 VE payroll + cash 2.04m UP + LT krediet 75.67m counterparties + capex 31.84m JUMP + in aanbouw 1.37m DROP + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 7.33m housing shell,active,,tick1495; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined IJzer en Zee 1494 / Thuiswest 1493 / Woonsprong 1492 / Ons Onderdak 1491 / Zetus 1490 / Inter-Vilvoordse 1489 / Woonschakel 1488 / De Voorkempen 1487 / Wonen in Limburg 1486 / Woonpunt Zennevallei 1485 / !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / leftover AGB Tielt"
)
check(lb, 21, "leaderboard")
append_crlf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Tielt>Woonmaatschappij>Woonstart>JR2025_L5,{ENT},omzet 7325986 UP vs 5633706 + huur/koop split unpublished + diensten 60/61 4260712 vs 3003012 + pers 1536245 17.1 VTE vs 17.2 + 1 VE + cash 2036624 UP vs 1573182 + debt 81699993 UP LT krediet 75672267 + capex 31842106 JUMP + in aanbouw 1370567 DROP + PnL -835178 vs -699553 + dividend 0 + interestsubs 1576284 + aandeel % unpublished,Leftover woonmaatschappij Woonstart after leftover AGB/APB hunt: omzet 7.33m UP / pers 1.54m 17.1 VTE / debt 81.70m UP / cash 2.04m UP / capex 31.84m JUMP / PnL -0.84m / dividend 0 / 1 VE hides municipal housing vehicle,8,Woonstart / Bestuursorgaan / voorzitter Luc Vannieuwenhuyze,info@woonstart.be,Sint-Michielstraat 1A 8700 Tielt,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1495 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VKT-inb PDF now extracted (746796 bytes 38p). FOI ready not sent. NOT every-10 (next 1500). NOT leftover AGB Tielt / leftover Woonstroom 1475 / leftover Thuiswest 1493 / leftover IJzer en Zee 1494 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. Puyenbroeck still 302. IJzer en Zee 1494 TAKEN. Woonstart TAKEN this tick."
)
check(foi, 21, "foi_queue")
append_crlf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

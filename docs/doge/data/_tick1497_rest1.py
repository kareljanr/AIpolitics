#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T21:40:00Z"
ENT = "wm_thbw"
SRC = "src_thbw_jr2025_nbb"
GAP = "gap_thbw_omzet_12_47m_pers_1_87m_debt_125m_l5"
LB = "lb_thbw_omzet_12_47m_pers_1_87m_debt_125m"
COMM = "comm_thbw_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00200690.pdf"

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
    f"{COMM},de Thuisbouwer JR2025 leftover woonmaatschappij dual (omzet 12.47m DROP / pers 1.87m 20.1 VTE / debt 125.06m DROP / cash 10.77m DROP / capex 12.12m / PnL 2.05m / dividend 1075 / 2 VE),{ENT},Hamme-Zele / mined Hamme+Zele dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-06-11,1968,,12474312,,,active,{PDF},Local leftover woonmaatschappij map VL Hamme-Zele — omzet 12.47m / pers 1.87m 20.1 VTE / debt 125.06m / cash 10.77m DROP,Publish omzet+diensten+huur/koop split + 2 VE payroll + cash 10.77m DROP + geldbeleg 8.00m JUMP + LT krediet 113.80m counterparties + capex 12.12m + in aanbouw 14.99m DROP + aandeel % unpublished + dividend 1075; do not keep leftover woonmaatschappij as unpublished 12.47m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Hamme>Woonmaatschappij>de Thuisbouwer>JR2025_L5,tick1497; assets 202554297 omzet 12474312 pers 1868369 pnl 2048234 equity 75921924 cash 10773820 debt 125064700 capex 12121406 dividend 1075; FOI ready not sent; not TE-additive of 348bn; NOT leftover AGB HIM Hamme / leftover AGB Zele / leftover stek92 1482 / leftover Dender-Zuid 1467 / leftover Meetjesland 1496 / leftover Woonstart 1495 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck"
)
check(comm, 19, "commitments")
append_crlf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},de Thuisbouwer JR2025 leftover woonmaatschappij: omzet 12.47m DROP / pers 1.87m 20.1 VTE / debt 125.06m DROP / cash 10.77m DROP / capex 12.12m / PnL 2.05m / dividend 1075 / 2 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Hamme>Woonmaatschappij>de Thuisbouwer>JR2025_L5,12474312,202554297,Leftover dual woonmaatschappij shell: assets 202.55m DROP / equity 75.92m / omzet 12.47m DROP / pers 1.87m 20.1 VTE / cash 10.77m DROP / debt 125.06m DROP / LT krediet 113.80m / capex 12.12m / PnL 2.05m / dividend 1075 / 2 VE; do not treat 12.47m as TE-additive of 348bn,strong,{SRC},de Thuisbouwer / mined Hamme-Zele dual housing,Local leftover woonmaatschappij map VL Hamme-Zele — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 12.47m DROP / pers 1.87m 20.1 VTE / debt 125.06m DROP / cash 10.77m DROP / PnL 2.05m / dividend 1075 / 2 VE,7.0,8.0,3.0,6.8,Publish omzet+diensten+huur/koop split + 2 VE payroll + cash 10.77m DROP + geldbeleg 8.00m JUMP + LT krediet 113.80m counterparties + capex 12.12m + in aanbouw 14.99m DROP + aandeel % unpublished + dividend 1075; do not keep leftover woonmaatschappij as unpublished 12.47m housing shell,active,,tick1497; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Meetjesland 1496 / Woonstart 1495 / IJzer en Zee 1494 / Thuiswest 1493 / Woonsprong 1492 / Ons Onderdak 1491 / Zetus 1490 / Inter-Vilvoordse 1489 / Woonschakel 1488 / De Voorkempen 1487 / Wonen in Limburg 1486 / Woonpunt Zennevallei 1485 / leftover stek92 1482 / leftover Dender-Zuid 1467 / leftover AGB HIM Hamme / leftover AGB Zele"
)
check(lb, 21, "leaderboard")
append_crlf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Hamme>Woonmaatschappij>de Thuisbouwer>JR2025_L5,{ENT},omzet 12474312 DROP vs 12782802 + huur/koop split unpublished + diensten 61 4084164 vs 3878691 + pers 1868369 20.1 VTE vs 19.6 + 2 VE + cash 10773820 DROP vs 18259080 + geldbeleg 8000000 JUMP + debt 125064700 DROP LT krediet 113798252 + capex 12121406 + in aanbouw 14985396 DROP + PnL 2048234 vs 1590676 + dividend 1075 + aandeel % unpublished,Leftover woonmaatschappij de Thuisbouwer after leftover AGB/APB hunt: omzet 12.47m DROP / pers 1.87m 20.1 VTE / debt 125.06m DROP / cash 10.77m DROP / capex 12.12m / PnL 2.05m / dividend 1075 / 2 VE hides municipal housing vehicle,8,de Thuisbouwer / Bestuursorgaan / voorzitter Johan Anthuenis,info@dethuisbouwer.be,Rozenhoed 1 9220 Hamme,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1497 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (1108201 bytes 53p). FOI ready not sent. NOT every-10 (next 1500). NOT leftover AGB HIM Hamme / leftover AGB Zele / leftover stek92 1482 / leftover Dender-Zuid 1467 / leftover Meetjesland 1496 / leftover Woonstart 1495 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. Puyenbroeck still 302. Meetjesland 1496 TAKEN. de Thuisbouwer TAKEN this tick."
)
check(foi, 21, "foi_queue")
append_crlf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

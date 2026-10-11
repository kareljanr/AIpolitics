#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T20:40:00Z"
ENT = "wm_ijez"
SRC = "src_ijez_jr2025_nbb"
GAP = "gap_ijez_omzet_17_97m_pers_2_55m_debt_141m_l5"
LB = "lb_ijez_omzet_17_97m_pers_2_55m_debt_141m"
COMM = "comm_ijez_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00171983.pdf"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def check(row, n, label):
    got = len(next(csv.reader(io.StringIO(row))))
    if got != n:
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:120]}")

comm = (
    f"{COMM},IJzer en Zee JR2025 leftover woonmaatschappij dual (omzet 17.97m DROP / pers 2.55m 30.6 VTE / debt 140.52m DROP / cash 13.13m UP / beleggingen 5.00m JUMP / PnL 1.77m / dividend 0 / 2 VE),{ENT},Veurne-westkust-westhoek / mined Veurne+De Panne+Diksmuide+Koksijde+Nieuwpoort dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-06-05,1920,,17969403,,,active,{PDF},Local leftover woonmaatschappij map VL Veurne-westkust-westhoek — omzet 17.97m / pers 2.55m 30.6 VTE / debt 140.52m / cash 13.13m UP,Publish omzet+diensten+huur/koop split + 2 VE payroll + cash 13.13m UP + beleggingen 5.00m JUMP + LT krediet 127.80m counterparties + capex 15.39m + in aanbouw 2.02m DROP + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 17.97m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Veurne>Woonmaatschappij>IJzerEnZee>JR2025_L5,tick1494; assets 182256295 omzet 17969403 pers 2550095 pnl 1773977 equity 39032061 cash 13132132 debt 140520313 capex 15386690 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover AGB Veurne / leftover Thuiswest 1493 / leftover Woonsprong 1492 / leftover Ons Onderdak 1491 / leftover Zetus 1490 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck"
)
check(comm, 19, "commitments")
append_crlf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},IJzer en Zee JR2025 leftover woonmaatschappij: omzet 17.97m DROP / pers 2.55m 30.6 VTE / debt 140.52m DROP / cash 13.13m UP / beleggingen 5.00m JUMP / PnL 1.77m / dividend 0 / 2 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Veurne>Woonmaatschappij>IJzerEnZee>JR2025_L5,17969403,182256295,Leftover dual woonmaatschappij shell: assets 182.26m DROP / equity 39.03m / omzet 17.97m DROP / pers 2.55m 30.6 VTE / cash 13.13m UP / beleggingen 5.00m JUMP / debt 140.52m DROP / LT krediet 127.80m / PnL 1.77m / dividend 0 / 2 VE; do not treat 17.97m as TE-additive of 348bn,strong,{SRC},IJzer en Zee / mined Veurne-westkust-westhoek dual housing,Local leftover woonmaatschappij map VL Veurne-westkust-westhoek — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 17.97m DROP / pers 2.55m 30.6 VTE / debt 140.52m DROP / cash 13.13m UP / PnL 1.77m / dividend 0 / 2 VE,7.0,8.0,3.0,6.8,Publish omzet+diensten+huur/koop split + 2 VE payroll + cash 13.13m UP + beleggingen 5.00m JUMP + LT krediet 127.80m counterparties + capex 15.39m + in aanbouw 2.02m DROP + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 17.97m housing shell,active,,tick1494; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Thuiswest 1493 / Woonsprong 1492 / Ons Onderdak 1491 / Zetus 1490 / Inter-Vilvoordse 1489 / Woonschakel 1488 / De Voorkempen 1487 / Wonen in Limburg 1486 / Woonpunt Zennevallei 1485 / !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / leftover AGB Veurne"
)
check(lb, 21, "leaderboard")
append_crlf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Veurne>Woonmaatschappij>IJzerEnZee>JR2025_L5,{ENT},omzet 17969403 DROP vs 19393837 + 6.10 split unpublished + diensten 5683226 vs 5259072 + explsubs 884446 DROP vs 951390 + pers 2550095 30.6 VTE vs 30.5 + 2 VE + cash 13132132 UP vs 12782367 + beleggingen 5000000 JUMP vs 3500000 + debt 140520313 DROP LT krediet 127800377 + capex 15386690 + in aanbouw 2021643 DROP + PnL 1773977 vs 1734748 + dividend 0 + commissaris 8904 + bestuurders 46610 + aandeel % unpublished,Leftover woonmaatschappij IJzer en Zee after leftover AGB/APB hunt: omzet 17.97m DROP / pers 2.55m 30.6 VTE / debt 140.52m DROP / cash 13.13m UP / beleggingen 5.00m JUMP / PnL 1.77m / dividend 0 / 2 VE hides municipal housing vehicle,8,IJzer en Zee / Bestuursorgaan / voorzitter Jonas Bel,info@ijzerenzee.be,Brugse Steenweg 2 8630 Veurne,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1494 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (970220 bytes 58p). FOI ready not sent. NOT every-10 (next 1500). NOT leftover AGB Veurne / leftover Thuiswest 1493 / leftover Woonsprong 1492 / leftover Ons Onderdak 1491 / leftover Zetus 1490 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still 302. Thuiswest 1493 TAKEN. IJzer en Zee TAKEN this tick."
)
check(foi, 21, "foi_queue")
append_crlf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

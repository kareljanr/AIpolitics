#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T20:20:00Z"
ENT = "wm_thws"
SRC = "src_thws_jr2025_nbb"
GAP = "gap_thws_omzet_40_78m_pers_7_60m_debt_450m_l5"
LB = "lb_thws_omzet_40_78m_pers_7_60m_debt_450m"
COMM = "comm_thws_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00263016.pdf"

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
    f"{COMM},Thuiswest JR2025 leftover woonmaatschappij dual (omzet 40.78m / pers 7.60m 90.9 VTE / debt 450.00m / cash 24.57m UP / beleggingen 15.26m DROP / PnL LOSS 1.88m / dividend 0 / 1 VE),{ENT},Roeselare-Midden-West-Vlaanderen / mined Roeselare+Izegem+Poperinge+Torhout dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-06-09,1920,,40776434,,,active,{PDF},Local leftover woonmaatschappij map VL Roeselare-Midden-West-Vlaanderen — omzet 40.78m / pers 7.60m 90.9 VTE / debt 450.00m / cash 24.57m UP,Publish omzet+diensten+huur/koop split + 1 VE payroll + cash 24.57m UP + beleggingen 15.26m DROP + LT krediet 408.75m counterparties + capex 19.36m + in aanbouw 22.12m + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 40.78m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Roeselare>Woonmaatschappij>Thuiswest>JR2025_L5,tick1493; assets 603044813 omzet 40776434 pers 7596389 pnl -1879750 equity 148379349 cash 24569716 debt 449999751 capex 19362596 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover Motena Roeselare / leftover Woonsprong 1492 / leftover Ons Onderdak 1491 / leftover IJzer en Zee / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck"
)
check(comm, 19, "commitments")
append_crlf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},Thuiswest JR2025 leftover woonmaatschappij: omzet 40.78m / pers 7.60m 90.9 VTE / debt 450.00m / cash 24.57m UP / beleggingen 15.26m DROP / PnL LOSS 1.88m / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Roeselare>Woonmaatschappij>Thuiswest>JR2025_L5,40776434,603044813,Leftover dual woonmaatschappij shell: assets 603.04m / equity 148.38m / omzet 40.78m / pers 7.60m 90.9 VTE / cash 24.57m UP / beleggingen 15.26m DROP / debt 450.00m / LT krediet 408.75m / PnL LOSS 1.88m / dividend 0 / 1 VE; do not treat 40.78m as TE-additive of 348bn,strong,{SRC},Thuiswest / mined Roeselare-Midden-West-Vlaanderen dual housing,Local leftover woonmaatschappij map VL Roeselare-Midden-West-Vlaanderen — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 40.78m / pers 7.60m 90.9 VTE / debt 450.00m / cash 24.57m UP / PnL LOSS 1.88m / dividend 0 / 1 VE,7.0,8.0,3.0,6.8,Publish omzet+diensten+huur/koop split + 1 VE payroll + cash 24.57m UP + beleggingen 15.26m DROP + LT krediet 408.75m counterparties + capex 19.36m + in aanbouw 22.12m + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 40.78m housing shell,active,,tick1493; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Woonsprong 1492 / Ons Onderdak 1491 / Zetus 1490 / Inter-Vilvoordse 1489 / Woonschakel 1488 / De Voorkempen 1487 / Wonen in Limburg 1486 / Woonpunt Zennevallei 1485 / !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Motena Roeselare"
)
check(lb, 21, "leaderboard")
append_crlf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Roeselare>Woonmaatschappij>Thuiswest>JR2025_L5,{ENT},omzet 40776434 vs 36565841 + 6.10 split unpublished + diensten 18193236 vs 16020600 + explsubs 2180609 DROP vs 4367356 + pers 7596389 90.9 VTE vs 88.8 + 1 VE + cash 24569716 UP vs 21998883 + beleggingen 15261099 DROP vs 20260008 + debt 449999751 LT krediet 408746068 + capex 19362596 + in aanbouw 22115489 + PnL LOSS 1879750 vs +222838 + dividend 0 + commissaris 19488 + extra 11638 + bestuurders 43662 + aandeel % unpublished,Leftover woonmaatschappij Thuiswest after leftover AGB/APB hunt: omzet 40.78m / pers 7.60m 90.9 VTE / debt 450.00m / cash 24.57m UP / beleggingen 15.26m DROP / PnL LOSS 1.88m / dividend 0 / 1 VE hides municipal housing vehicle,8,Thuiswest / Bestuursorgaan / voorzitter Bart Wenes,info@thuiswest.be,Groenestraat 224 8800 Roeselare,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1493 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (357403 bytes 52p). FOI ready not sent. NOT every-10 (next 1500). NOT leftover Motena Roeselare / leftover Woonsprong 1492 / leftover Ons Onderdak 1491 / leftover IJzer en Zee / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still 302. Woonsprong 1492 TAKEN. Thuiswest TAKEN this tick."
)
check(foi, 21, "foi_queue")
append_crlf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

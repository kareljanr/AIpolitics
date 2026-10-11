#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T18:55:00Z"
ENT = "wm_wpzn"
SRC = "src_wpzn_jr2025_nbb"
GAP = "gap_wpzn_omzet_15_27m_pers_3_13m_debt_108m_l5"
LB = "lb_wpzn_omzet_15_27m_pers_3_13m_debt_108m"
COMM = "comm_wpzn_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00145529.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

append_lf(DATA / "commitments.csv", [
    f"{COMM},Woonpunt Zennevallei JR2025 leftover woonmaatschappij dual (omzet 15.27m JUMP / pers 3.13m 37.3 VTE / debt 108.04m / cash 4.80m JUMP / PnL JUMP 0.74m / dividend 0 / 1 VE),{ENT},Halle-Zennevallei / mined Halle-Vilvoorde-Zuid dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-06-01,1920,,15271056,,,active,{PDF},Local leftover woonmaatschappij map VL Halle-Zennevallei — omzet 15.27m JUMP / pers 3.13m 37.3 VTE / debt 108.04m / cash 4.80m JUMP,Publish omzet+diensten+verhuur/verkoop split + 1 VE payroll + cash 4.80m JUMP + LT krediet 84.98m counterparties + capex 10.46m + aandeel % Halle/Beersel + dividend 0; do not keep leftover woonmaatschappij as unpublished 15.27m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Halle>Woonmaatschappij>WoonpuntZennevallei>JR2025_L5,tick1485; assets 162911198 omzet 15271056 pers 3128980 pnl 741465 equity 47335265 cash 4801403 debt 108036213 capex 10461618 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover Woonpunt Waas 1464 / leftover !Mpuls 1484 / leftover WoonST 1483 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"{LB},Woonpunt Zennevallei JR2025 leftover woonmaatschappij: omzet 15.27m JUMP / pers 3.13m 37.3 VTE / debt 108.04m / cash 4.80m JUMP / PnL JUMP 0.74m / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Halle>Woonmaatschappij>WoonpuntZennevallei>JR2025_L5,15271056,162911198,Leftover dual woonmaatschappij shell: assets 162.91m / equity 47.34m / omzet 15.27m JUMP / pers 3.13m 37.3 VTE / cash 4.80m JUMP / debt 108.04m / LT krediet 84.98m / PnL JUMP 0.74m / dividend 0 / 1 VE; do not treat 15.27m as TE-additive of 348bn,strong,{SRC},Woonpunt Zennevallei / mined Halle-Beersel dual housing,Local leftover woonmaatschappij map VL Halle-Zennevallei — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 15.27m JUMP / pers 3.13m 37.3 VTE / debt 108.04m / cash 4.80m JUMP / PnL JUMP 0.74m / dividend 0 / 1 VE,7.0,8.0,3.0,7.0,Publish omzet+diensten+verhuur/verkoop split + 1 VE payroll + cash 4.80m JUMP + LT krediet 84.98m counterparties + capex 10.46m + aandeel % Halle/Beersel + dividend 0; do not keep leftover woonmaatschappij as unpublished 15.27m housing shell,active,,tick1485; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Woonpunt Waas 1464",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Gemeenten>Halle>Woonmaatschappij>WoonpuntZennevallei>JR2025_L5,{ENT},omzet 15271056 JUMP vs 11209053 + diensten 6315121 JUMP vs 5633044 + pers 3128980 37.3 VTE vs 35.2 + 1 VE + cash 4801403 JUMP vs 3516094 + debt 108036213 LT krediet 84984146 + voorraden DROP 648189 vs 2657485 + capex 10461618 + PnL JUMP 741465 vs 405723 + dividend 0 + commissaris 19148 + belastingadvies 6779 + bestuurders 9503 92796 + aandeel % Halle/Beersel unpublished,Leftover woonmaatschappij Woonpunt Zennevallei after leftover AGB/APB hunt: omzet 15.27m JUMP / pers 3.13m 37.3 VTE / debt 108.04m / cash 4.80m JUMP / PnL JUMP 0.74m / dividend 0 / 1 VE hides municipal housing vehicle,8,Woonpunt Zennevallei / Bestuursorgaan / voorzitter Hugo Vandaele,info@wpz.be,Molenborre 26 bus 1 1500 Halle,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1485 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (1344945 bytes 64p). FOI ready not sent. NOT every-10. NOT leftover Woonpunt Waas 1464 / leftover !Mpuls 1484 / leftover WoonST 1483 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 403/404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still 302. !Mpuls 1484 TAKEN. WoonST 1483 TAKEN. stek92 1482 TAKEN. LeefGoed 1481 TAKEN. Kanvaz 1480 TAKEN. Woonpunt Zennevallei TAKEN this tick.",
])
print("foi_queue +1")

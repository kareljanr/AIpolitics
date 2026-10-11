#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T19:40:00Z"
ENT = "wm_ivlv"
SRC = "src_ivlv_jr2025_nbb"
GAP = "gap_ivlv_omzet_9_37m_pers_2_00m_debt_136m_l5"
LB = "lb_ivlv_omzet_9_37m_pers_2_00m_debt_136m"
COMM = "comm_ivlv_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00138038.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

append_lf(DATA / "commitments.csv", [
    f"{COMM},Inter-Vilvoordse JR2025 leftover woonmaatschappij dual (omzet 9.37m / pers 2.00m 20.8 VTE / debt 135.88m / cash 22.77m JUMP / PnL DROP 0.96m / dividend 0 / 1 VE),{ENT},Vilvoorde-Machelen / mined Vilvoorde-Machelen dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-27,1920,,9370627,,,active,{PDF},Local leftover woonmaatschappij map VL Vilvoorde-Machelen — omzet 9.37m / pers 2.00m 20.8 VTE / debt 135.88m / cash 22.77m JUMP,Publish omzet+diensten+verhuur/doorverhuur split + 1 VE payroll + cash 22.77m JUMP + LT krediet 125.16m counterparties + capex 12.02m + in aanbouw 31.08m + aandeel % Vilvoorde/Machelen + dividend 0; do not keep leftover woonmaatschappij as unpublished 9.37m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Vilvoorde>Woonmaatschappij>Inter-Vilvoordse>JR2025_L5,tick1489; assets 175606699 omzet 9370627 pers 1996874 pnl 961462 equity 38667098 cash 22766208 debt 135881516 capex 12018842 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover AGB Vilvoorde / leftover Zetus / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"{LB},Inter-Vilvoordse JR2025 leftover woonmaatschappij: omzet 9.37m / pers 2.00m 20.8 VTE / debt 135.88m / cash 22.77m JUMP / PnL DROP 0.96m / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Vilvoorde>Woonmaatschappij>Inter-Vilvoordse>JR2025_L5,9370627,175606699,Leftover dual woonmaatschappij shell: assets 175.61m / equity 38.67m / omzet 9.37m / pers 2.00m 20.8 VTE / cash 22.77m JUMP / debt 135.88m / LT krediet 125.16m / PnL DROP 0.96m / dividend 0 / 1 VE; do not treat 9.37m as TE-additive of 348bn,strong,{SRC},Inter-Vilvoordse / mined Vilvoorde-Machelen dual housing,Local leftover woonmaatschappij map VL Vilvoorde-Machelen — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 9.37m / pers 2.00m 20.8 VTE / debt 135.88m / cash 22.77m JUMP / PnL DROP 0.96m / dividend 0 / 1 VE,7.0,8.0,3.0,6.8,Publish omzet+diensten+verhuur/doorverhuur split + 1 VE payroll + cash 22.77m JUMP + LT krediet 125.16m counterparties + capex 12.02m + in aanbouw 31.08m + aandeel % Vilvoorde/Machelen + dividend 0; do not keep leftover woonmaatschappij as unpublished 9.37m housing shell,active,,tick1489; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Woonschakel 1488 / De Voorkempen 1487 / Wonen in Limburg 1486 / Woonpunt Zennevallei 1485 / !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / AGB Vilvoorde",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Gemeenten>Vilvoorde>Woonmaatschappij>Inter-Vilvoordse>JR2025_L5,{ENT},omzet 9370627 vs 9368788 + diensten 3298243 vs 3309716 + pers 1996874 20.8 VTE vs 20.7 + 1 VE + cash 22766208 JUMP vs 20393831 + debt 135881516 LT krediet 125161194 + capex 12018842 + in aanbouw 31079542 + PnL DROP 961462 vs 1690890 + dividend 0 + commissaris 11616 + bestuurders 9503 13800 + aandeel % Vilvoorde/Machelen published,Leftover woonmaatschappij Inter-Vilvoordse after leftover AGB/APB hunt: omzet 9.37m / pers 2.00m 20.8 VTE / debt 135.88m / cash 22.77m JUMP / PnL DROP 0.96m / dividend 0 / 1 VE hides municipal housing vehicle,8,Inter-Vilvoordse / Bestuursorgaan / voorzitter Steve Van Camp,onthaal@intervilvoordse.be,Parkstraat 115 1800 Vilvoorde,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1489 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (4820480 bytes 57p). FOI ready not sent. NOT every-10. NOT leftover AGB Vilvoorde / leftover Zetus / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404/403 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still 302. Woonschakel 1488 TAKEN. Leftover Zetus 0405.196.516 deposit 2026-00117246 live unused. Inter-Vilvoordse TAKEN this tick.",
])
print("foi_queue +1")

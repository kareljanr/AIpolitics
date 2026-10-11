#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T19:26:00Z"
ENT = "wm_wsbn"
SRC = "src_wsbn_jr2025_nbb"
GAP = "gap_wsbn_omzet_11_00m_pers_1_96m_debt_136m_l5"
LB = "lb_wsbn_omzet_11_00m_pers_1_96m_debt_136m"
COMM = "comm_wsbn_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00131692.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

append_lf(DATA / "commitments.csv", [
    f"{COMM},Woonschakel Berg en Nete JR2025 leftover woonmaatschappij dual (omzet 11.00m JUMP / pers 1.96m 21.7 VTE / debt 136.07m / cash 3.46m JUMP / PnL DROP 0.35m / dividend 0 / 2 VE),{ENT},Rivierenland-Oost / mined Heist-op-den-Berg-Berlaar-Nijlen-Putte dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-04-24,1968,,10995862,,,active,{PDF},Local leftover woonmaatschappij map VL Rivierenland-Oost — omzet 11.00m JUMP / pers 1.96m 21.7 VTE / debt 136.07m / cash 3.46m JUMP,Publish omzet+diensten+huur/andere split + 2 VE payroll + cash 3.46m JUMP + voorraden JUMP 2.43m + LT krediet 123.18m counterparties + capex 13.40m + aandeel % Heist/Berlaar/Nijlen/Putte + dividend 0; do not keep leftover woonmaatschappij as unpublished 11.00m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Heist-op-den-Berg>Woonmaatschappij>Woonschakel>JR2025_L5,tick1488; assets 155658879 omzet 10995862 pers 1957328 pnl 348212 equity 19159867 cash 3462126 debt 136065192 capex 13398259 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover cultuur-IGS Berg en Nete 0671.761.919 / leftover De Voorkempen 1487 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover Inter-Vilvoordse / leftover Zetus / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"{LB},Woonschakel Berg en Nete JR2025 leftover woonmaatschappij: omzet 11.00m JUMP / pers 1.96m 21.7 VTE / debt 136.07m / cash 3.46m JUMP / PnL DROP 0.35m / dividend 0 / 2 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Heist-op-den-Berg>Woonmaatschappij>Woonschakel>JR2025_L5,10995862,155658879,Leftover dual woonmaatschappij shell: assets 155.66m / equity 19.16m / omzet 11.00m JUMP / pers 1.96m 21.7 VTE / cash 3.46m JUMP / voorraden JUMP 2.43m / debt 136.07m / LT krediet 123.18m / PnL DROP 0.35m / dividend 0 / 2 VE; do not treat 11.00m as TE-additive of 348bn,strong,{SRC},Woonschakel / mined Heist-op-den-Berg-Berlaar dual housing,Local leftover woonmaatschappij map VL Rivierenland-Oost — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 11.00m JUMP / pers 1.96m 21.7 VTE / debt 136.07m / cash 3.46m JUMP / PnL DROP 0.35m / dividend 0 / 2 VE,7.0,8.0,3.0,6.8,Publish omzet+diensten+huur/andere split + 2 VE payroll + cash 3.46m JUMP + voorraden JUMP 2.43m + LT krediet 123.18m counterparties + capex 13.40m + aandeel % Heist/Berlaar/Nijlen/Putte + dividend 0; do not keep leftover woonmaatschappij as unpublished 11.00m housing shell,active,,tick1488; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined De Voorkempen 1487 / Wonen in Limburg 1486 / Woonpunt Zennevallei 1485 / !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / leftover cultuur-IGS Berg en Nete",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Gemeenten>Heist-op-den-Berg>Woonmaatschappij>Woonschakel>JR2025_L5,{ENT},omzet 10995862 JUMP vs 9176950 + diensten 4799320 JUMP vs 3348423 + pers 1957328 21.7 VTE vs 17.7 + 2 VE + cash 3462126 JUMP vs 3139025 + voorraden JUMP 2429386 vs 70882 + debt 136065192 LT krediet 123184025 + capex 13398259 + PnL DROP 348212 vs 425988 + dividend 0 + commissaris 8000 + bestuurders 9503 empty + aandeel % Heist/Berlaar/Nijlen/Putte unpublished,Leftover woonmaatschappij Woonschakel Berg en Nete after leftover AGB/APB hunt: omzet 11.00m JUMP / pers 1.96m 21.7 VTE / debt 136.07m / cash 3.46m JUMP / PnL DROP 0.35m / dividend 0 / 2 VE hides municipal housing vehicle,8,Woonschakel Berg en Nete / Bestuursorgaan / voorzitter Kelly Van Tendeloo,info@wsben.vlaanderen,Plantijnlaan 2 2220 Heist-op-den-Berg,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1488 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (2752616 bytes 91p). FOI ready not sent. NOT every-10. NOT leftover cultuur-IGS Berg en Nete 0671.761.919 / leftover De Voorkempen 1487 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 403/404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still 302. De Voorkempen 1487 TAKEN. Leftover Inter-Vilvoordse 0400.676.613 deposit 2026-00138038 live unused. Leftover Zetus 0405.196.516 deposit 2026-00117246 live unused. Woonschakel TAKEN this tick.",
])
print("foi_queue +1")

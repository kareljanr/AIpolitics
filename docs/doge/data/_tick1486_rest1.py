#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T19:12:00Z"
ENT = "wm_wlim"
SRC = "src_wlim_jr2025_nbb"
GAP = "gap_wlim_omzet_149_76m_pers_32_78m_debt_1459m_l5"
LB = "lb_wlim_omzet_149_76m_pers_32_78m_debt_1459m"
COMM = "comm_wlim_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00206025.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

append_lf(DATA / "commitments.csv", [
    f"{COMM},Wonen in Limburg JR2025 leftover woonmaatschappij dual (omzet 149.76m DROP / pers 32.78m 397.5 VTE / debt 1.459bn / cash 96.29m DROP / PnL DROP 5.71m / dividend 0 / 19 VE),{ENT},Limburg / mined Houthalen-Helchteren-Hasselt-Genk-Beringen-Maasmechelen dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-06-15,1953,,149755087,,,active,{PDF},Local leftover woonmaatschappij map VL Limburg — omzet 149.76m DROP / pers 32.78m 397.5 VTE / debt 1.459bn / cash 96.29m DROP,Publish omzet+diensten+verhuur/verkoop split + 19 VE payroll + cash 96.29m DROP + geldbeleg 88.65m JUMP + LT krediet 1.341bn counterparties + capex 106.98m + aandeel % Houthalen-Helchteren/Hasselt/Genk + dividend 0; do not keep leftover woonmaatschappij as unpublished 149.76m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Houthalen-Helchteren>Woonmaatschappij>WonenInLimburg>JR2025_L5,tick1486; assets 2060381293 omzet 149755087 pers 32782938 pnl 5708426 equity 591815458 cash 96287038 debt 1459270191 capex 106984224 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover Dutch Wonen Limburg NL / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover Woonpunt Zennevallei 1485 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"{LB},Wonen in Limburg JR2025 leftover woonmaatschappij: omzet 149.76m DROP / pers 32.78m 397.5 VTE / debt 1.459bn / cash 96.29m DROP / PnL DROP 5.71m / dividend 0 / 19 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Houthalen-Helchteren>Woonmaatschappij>WonenInLimburg>JR2025_L5,149755087,2060381293,Leftover dual woonmaatschappij shell: assets 2.060bn / equity 591.82m / omzet 149.76m DROP / pers 32.78m 397.5 VTE / cash 96.29m DROP / geldbeleg 88.65m JUMP / debt 1.459bn / LT krediet 1.341bn / PnL DROP 5.71m / dividend 0 / 19 VE; do not treat 149.76m as TE-additive of 348bn,strong,{SRC},Wonen in Limburg / mined Houthalen-Helchteren-Hasselt-Genk dual housing,Local leftover woonmaatschappij map VL Limburg — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 149.76m DROP / pers 32.78m 397.5 VTE / debt 1.459bn / cash 96.29m DROP / PnL DROP 5.71m / dividend 0 / 19 VE,7.0,9.0,3.0,7.5,Publish omzet+diensten+verhuur/verkoop split + 19 VE payroll + cash 96.29m DROP + geldbeleg 88.65m JUMP + LT krediet 1.341bn counterparties + capex 106.98m + aandeel % Houthalen-Helchteren/Hasselt/Genk + dividend 0; do not keep leftover woonmaatschappij as unpublished 149.76m housing shell,active,,tick1486; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Woonpunt Zennevallei 1485 / !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Woonpunt Waas 1464",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Gemeenten>Houthalen-Helchteren>Woonmaatschappij>WonenInLimburg>JR2025_L5,{ENT},omzet 149755087 DROP vs 159522539 + diensten 51702656 JUMP vs 50511252 + pers 32782938 397.5 VTE vs 367 + 19 VE + cash 96287038 DROP vs 156033570 + geldbeleg 88647595 JUMP vs 48637647 + debt 1459270191 LT krediet 1340664945 + voorraden JUMP 82007845 vs 67270536 + capex 106984224 + PnL DROP 5708426 vs 10494226 + dividend 0 + commissaris 158695 + bestuurders 63607 + aandeel % Houthalen-Helchteren/Hasselt/Genk unpublished,Leftover woonmaatschappij Wonen in Limburg after leftover AGB/APB hunt: omzet 149.76m DROP / pers 32.78m 397.5 VTE / debt 1.459bn / cash 96.29m DROP / PnL DROP 5.71m / dividend 0 / 19 VE hides municipal housing vehicle,8,Wonen in Limburg / Bestuursorgaan / voorzitter Dries Deferm,info@wil.be,Ringlaan 20 3530 Houthalen-Helchteren,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1486 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (4703685 bytes 72p). FOI ready not sent. NOT every-10. NOT leftover Dutch Wonen Limburg NL / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover Woonpunt Zennevallei 1485 / leftover !Mpuls 1484 / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 403/404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still 302. Woonpunt Zennevallei 1485 TAKEN. !Mpuls 1484 TAKEN. WoonST 1483 TAKEN. stek92 1482 TAKEN. LeefGoed 1481 TAKEN. Kanvaz 1480 TAKEN. Wonen in Limburg TAKEN this tick.",
])
print("foi_queue +1")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T18:50:00Z"
ENT = "wm_zkem"
SRC = "src_zkem_jr2025_nbb"
GAP = "gap_zkem_omzet_35_33m_pers_7_12m_debt_476m_l5"
LB = "lb_zkem_omzet_35_33m_pers_7_12m_debt_476m"
COMM = "comm_zkem_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00157303.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

append_lf(DATA / "commitments.csv", [
    f"{COMM},LeefGoed JR2025 leftover woonmaatschappij dual (omzet 35.33m DROP / pers 7.12m 86.6 VTE / debt 476.31m / cash 16.92m JUMP / PnL JUMP 0.42m / dividend 0 / 5 VE),{ENT},Geel-Herentals-Westerlo / mined Zuiderkempen-Neteland dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-26,1947,,35325415,,,active,{PDF},Local leftover woonmaatschappij map VL Zuiderkempen — omzet 35.33m DROP / pers 7.12m 86.6 VTE / debt 476.31m / cash 16.92m JUMP,Publish omzet+diensten+verhuur/verkoop split + 5 VE payroll + cash 16.92m JUMP + LT krediet 434.79m counterparties + capex 34.83m + aandeel % Geel/Herentals/Westerlo/Herselt/Hulshout + dividend 0; do not keep leftover woonmaatschappij as unpublished 35.33m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Geel>Woonmaatschappij>LeefGoed>JR2025_L5,tick1481; assets 570754360 omzet 35325415 pers 7117830 pnl 417118 equity 92517644 cash 16924292 debt 476306208 capex 34832940 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT Woonboog 1478 / leftover stek92 / leftover Woonin / leftover Wooncompagnie / leftover WoonST / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"{LB},LeefGoed JR2025 leftover woonmaatschappij: omzet 35.33m DROP / pers 7.12m 86.6 VTE / debt 476.31m / cash 16.92m JUMP / PnL JUMP 0.42m / dividend 0 / 5 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Geel>Woonmaatschappij>LeefGoed>JR2025_L5,35325415,570754360,Leftover dual woonmaatschappij shell: assets 570.75m / equity 92.52m / omzet 35.33m DROP / pers 7.12m 86.6 VTE / cash 16.92m JUMP / debt 476.31m / LT krediet 434.79m / PnL JUMP 0.42m / dividend 0 / 5 VE; do not treat 35.33m as TE-additive of 348bn,strong,{SRC},LeefGoed / mined Geel-Herentals-Westerlo dual housing,Local leftover woonmaatschappij map VL Zuiderkempen — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 35.33m DROP / pers 7.12m 86.6 VTE / debt 476.31m / cash 16.92m JUMP / PnL JUMP 0.42m / dividend 0 / 5 VE,7.0,8.0,3.0,7.0,Publish omzet+diensten+verhuur/verkoop split + 5 VE payroll + cash 16.92m JUMP + LT krediet 434.79m counterparties + capex 34.83m + aandeel % Geel/Herentals/Westerlo/Herselt/Hulshout + dividend 0; do not keep leftover woonmaatschappij as unpublished 35.33m housing shell,active,,tick1481; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Gemeenten>Geel>Woonmaatschappij>LeefGoed>JR2025_L5,{ENT},omzet 35325415 DROP vs 42853240 + diensten 10462898 JUMP vs 9490243 + pers 7117830 86.6 VTE vs 85.5 + 5 VE + cash 16924292 JUMP vs 10988951 + debt 476306208 LT krediet 434791212 + voorraden 31583791 + capex 34832940 + PnL JUMP 417118 vs -1143473 + dividend 0 + commissaris 12415 + bestuurders 37276 + aandeel % Geel/Herentals/Westerlo unpublished,Leftover woonmaatschappij LeefGoed after leftover AGB/APB hunt: omzet 35.33m DROP / pers 7.12m 86.6 VTE / debt 476.31m / cash 16.92m JUMP / PnL JUMP 0.42m / dividend 0 / 5 VE hides municipal housing vehicle,8,LeefGoed / Bestuursorgaan / voorzitter Matthias Verhegge,info@leefgoed.be,Kameinestraat 3 2440 Geel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1481 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (1286171 bytes 73p). FOI ready not sent. NOT every-10. NOT Woonboog 1478 / leftover stek92 / leftover Woonin / leftover Wooncompagnie / leftover WoonST / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 403 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still no separate APB 2025 PDF. WoonST Temse still JR2024. leftover stek92 JR2025 live unused this tick. LeefGoed TAKEN this tick.",
])
print("foi_queue +1")

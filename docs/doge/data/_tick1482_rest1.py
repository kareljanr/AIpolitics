#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T19:10:00Z"
ENT = "wm_stk9"
SRC = "src_stk9_jr2025_nbb"
GAP = "gap_stk9_omzet_14_56m_pers_5_21m_debt_169m_l5"
LB = "lb_stk9_omzet_14_56m_pers_5_21m_debt_169m"
COMM = "comm_stk9_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00288124.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

append_lf(DATA / "commitments.csv", [
    f"{COMM},stek92 JR2025 leftover woonmaatschappij dual (omzet 14.56m DROP / pers 5.21m 48.5 VTE / debt 168.79m / cash 18.89m DROP / PnL LOSS 1.55m / dividend 0 / 1 VE),{ENT},Dendermonde-Berlare-Buggenhout-Lebbeke / mined Dender-Waasland dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-06-08,1928,,14564880,,,active,{PDF},Local leftover woonmaatschappij map VL Dender-Waasland — omzet 14.56m DROP / pers 5.21m 48.5 VTE / debt 168.79m / cash 18.89m DROP,Publish omzet+diensten+verhuur/verkoop split + 1 VE payroll + cash 18.89m DROP + LT krediet 153.33m counterparties + capex 9.16m + aandeel % Dendermonde/Berlare/Buggenhout/Lebbeke + dividend 0; do not keep leftover woonmaatschappij as unpublished 14.56m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Dendermonde>Woonmaatschappij>stek92>JR2025_L5,tick1482; assets 228254549 omzet 14564880 pers 5207321 pnl -1546368 equity 58118603 cash 18887511 debt 168788912 capex 9157319 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover WoonST Temse / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"{LB},stek92 JR2025 leftover woonmaatschappij: omzet 14.56m DROP / pers 5.21m 48.5 VTE / debt 168.79m / cash 18.89m DROP / PnL LOSS 1.55m / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Dendermonde>Woonmaatschappij>stek92>JR2025_L5,14564880,228254549,Leftover dual woonmaatschappij shell: assets 228.25m / equity 58.12m / omzet 14.56m DROP / pers 5.21m 48.5 VTE / cash 18.89m DROP / debt 168.79m / LT krediet 153.33m / PnL LOSS 1.55m / dividend 0 / 1 VE; do not treat 14.56m as TE-additive of 348bn,strong,{SRC},stek92 / mined Dendermonde-Berlare-Buggenhout-Lebbeke dual housing,Local leftover woonmaatschappij map VL Dender-Waasland — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 14.56m DROP / pers 5.21m 48.5 VTE / debt 168.79m / cash 18.89m DROP / PnL LOSS 1.55m / dividend 0 / 1 VE,7.0,8.0,3.0,7.0,Publish omzet+diensten+verhuur/verkoop split + 1 VE payroll + cash 18.89m DROP + LT krediet 153.33m counterparties + capex 9.16m + aandeel % Dendermonde/Berlare/Buggenhout/Lebbeke + dividend 0; do not keep leftover woonmaatschappij as unpublished 14.56m housing shell,active,,tick1482; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Gemeenten>Dendermonde>Woonmaatschappij>stek92>JR2025_L5,{ENT},omzet 14564880 DROP vs 14586153 + diensten 6016120 DROP vs 6973553 + pers 5207321 48.5 VTE vs 48.1 + 1 VE + cash 18887511 DROP vs 25075051 + debt 168788912 LT krediet 153334678 + voorraden 9813656 + capex 9157319 + PnL LOSS -1546368 vs -1223605 + dividend 0 + commissaris 7000 + bestuurders 61077 + aandeel % Dendermonde/Berlare/Buggenhout/Lebbeke unpublished,Leftover woonmaatschappij stek92 after leftover AGB/APB hunt: omzet 14.56m DROP / pers 5.21m 48.5 VTE / debt 168.79m / cash 18.89m DROP / PnL LOSS 1.55m / dividend 0 / 1 VE hides municipal housing vehicle,8,stek92 / Bestuursorgaan / voorzitter Tom Bogman,info@stek92.be,Pijnderslaan 2 9200 Dendermonde,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1482 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (1181166 bytes 57p). FOI ready not sent. NOT every-10. NOT leftover WoonST Temse / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still 302. WoonST Temse still JR2024. LeefGoed 1481 TAKEN. Kanvaz 1480 TAKEN. stek92 TAKEN this tick.",
])
print("foi_queue +1")

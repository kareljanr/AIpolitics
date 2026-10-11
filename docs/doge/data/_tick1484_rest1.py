#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T18:50:00Z"
ENT = "wm_mpls"
SRC = "src_mpls_jr2025_nbb"
GAP = "gap_mpls_omzet_13_19m_pers_2_68m_debt_149m_l5"
LB = "lb_mpls_omzet_13_19m_pers_2_68m_debt_149m"
COMM = "comm_mpls_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00117115.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

append_lf(DATA / "commitments.csv", [
    f"{COMM},!Mpuls Menen-Wervik JR2025 leftover woonmaatschappij dual (omzet 13.19m UP / pers 2.68m 33.4 VTE / debt 149.31m / cash 9.23m DROP / PnL JUMP 1.23m / dividend 0 / 1 VE),{ENT},Menen-Wervik / mined Leie-Westhoek dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-12,1968,,13185888,,,active,{PDF},Local leftover woonmaatschappij map VL Menen-Wervik — omzet 13.19m UP / pers 2.68m 33.4 VTE / debt 149.31m / cash 9.23m DROP,Publish omzet+diensten+verhuur/verkoop split + 1 VE payroll + cash 9.23m DROP + LT krediet 135.36m counterparties + capex 22.39m + aandeel % Menen/Wervik + dividend 0; do not keep leftover woonmaatschappij as unpublished 13.19m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Menen>Woonmaatschappij>!Mpuls>JR2025_L5,tick1484; assets 213864560 omzet 13185888 pers 2677490 pnl 1225909 equity 62364982 cash 9225512 debt 149309010 capex 22387387 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover WoonST 1483 / leftover SW+ 1472 / leftover AGB Menen / leftover WZBW Wervik / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"{LB},!Mpuls Menen-Wervik JR2025 leftover woonmaatschappij: omzet 13.19m UP / pers 2.68m 33.4 VTE / debt 149.31m / cash 9.23m DROP / PnL JUMP 1.23m / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Menen>Woonmaatschappij>!Mpuls>JR2025_L5,13185888,213864560,Leftover dual woonmaatschappij shell: assets 213.86m / equity 62.36m / omzet 13.19m UP / pers 2.68m 33.4 VTE / cash 9.23m DROP / debt 149.31m / LT krediet 135.36m / PnL JUMP 1.23m / dividend 0 / 1 VE; do not treat 13.19m as TE-additive of 348bn,strong,{SRC},!Mpuls / mined Menen-Wervik dual housing,Local leftover woonmaatschappij map VL Menen-Wervik — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 13.19m UP / pers 2.68m 33.4 VTE / debt 149.31m / cash 9.23m DROP / PnL JUMP 1.23m / dividend 0 / 1 VE,7.0,8.0,3.0,7.0,Publish omzet+diensten+verhuur/verkoop split + 1 VE payroll + cash 9.23m DROP + LT krediet 135.36m counterparties + capex 22.39m + aandeel % Menen/Wervik + dividend 0; do not keep leftover woonmaatschappij as unpublished 13.19m housing shell,active,,tick1484; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Gemeenten>Menen>Woonmaatschappij>!Mpuls>JR2025_L5,{ENT},omzet 13185888 UP vs 12760808 + diensten 5317564 vs 5282951 + pers 2677490 33.4 VTE vs 31.7 + 1 VE + cash 9225512 DROP vs 14391203 + debt 149309010 LT krediet 135359108 + voorraden 88528 + capex 22387387 + PnL JUMP 1225909 vs 267829 + dividend 0 + commissaris 10876 + bestuurders 9503 empty remuneratie 37983.50 + aandeel % Menen/Wervik unpublished,Leftover woonmaatschappij !Mpuls after leftover AGB/APB hunt: omzet 13.19m UP / pers 2.68m 33.4 VTE / debt 149.31m / cash 9.23m DROP / PnL JUMP 1.23m / dividend 0 / 1 VE hides municipal housing vehicle,8,!Mpuls Menen-Wervik / Bestuursorgaan / voorzitter Willy Ugille,info@wm-impuls.be,Volkslaan 302 bus 0201 8930 Menen,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1484 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-kap PDF now extracted (3536251 bytes 66p). FOI ready not sent. NOT every-10. NOT leftover WoonST 1483 / leftover SW+ 1472 / leftover AGB Menen / leftover WZBW Wervik / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 403/404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still 302. WoonST 1483 TAKEN. stek92 1482 TAKEN. LeefGoed 1481 TAKEN. Kanvaz 1480 TAKEN. !Mpuls TAKEN this tick.",
])
print("foi_queue +1")

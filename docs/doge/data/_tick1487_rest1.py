#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T19:20:00Z"
ENT = "wm_dvpk"
SRC = "src_dvpk_jr2025_nbb"
GAP = "gap_dvpk_omzet_19_57m_pers_4_72m_debt_307m_l5"
LB = "lb_dvpk_omzet_19_57m_pers_4_72m_debt_307m"
COMM = "comm_dvpk_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00192551.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

append_lf(DATA / "commitments.csv", [
    f"{COMM},De Voorkempen JR2025 leftover woonmaatschappij dual (omzet 19.57m DROP / pers 4.72m 58.5 VTE / debt 306.99m / cash 5.09m JUMP / PnL JUMP 4.67k / dividend 0 / 1 VE),{ENT},Voorkempen / mined Brecht-Kalmthout-Kapellen-Zoersel-Brasschaat-Schoten-Malle dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-06-15,1985,,19566170,,,active,{PDF},Local leftover woonmaatschappij map VL Voorkempen — omzet 19.57m DROP / pers 4.72m 58.5 VTE / debt 306.99m / cash 5.09m JUMP,Publish omzet+diensten+verhuur/koop split + 1 VE payroll + cash 5.09m JUMP + geldbeleg 0 DROP + LT krediet 281.48m counterparties + capex 32.27m + aandeel % Brecht/Kalmthout/Kapellen + dividend 0; do not keep leftover woonmaatschappij as unpublished 19.57m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Brecht>Woonmaatschappij>DeVoorkempen>JR2025_L5,tick1487; assets 352377695 omzet 19566170 pers 4716427 pnl 4666 equity 42644547 cash 5091590 debt 306985521 capex 32271841 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover RL de Voorkempen 1441 / leftover Erfgoed Voorkempen IOED 1425 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover Wonen in Limburg 1486 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"{LB},De Voorkempen JR2025 leftover woonmaatschappij: omzet 19.57m DROP / pers 4.72m 58.5 VTE / debt 306.99m / cash 5.09m JUMP / PnL JUMP 4.67k / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Brecht>Woonmaatschappij>DeVoorkempen>JR2025_L5,19566170,352377695,Leftover dual woonmaatschappij shell: assets 352.38m / equity 42.64m / omzet 19.57m DROP / pers 4.72m 58.5 VTE / cash 5.09m JUMP / geldbeleg 0 DROP / debt 306.99m / LT krediet 281.48m / PnL JUMP 4.67k / dividend 0 / 1 VE; do not treat 19.57m as TE-additive of 348bn,strong,{SRC},De Voorkempen / mined Brecht-Kalmthout-Kapellen dual housing,Local leftover woonmaatschappij map VL Voorkempen — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 19.57m DROP / pers 4.72m 58.5 VTE / debt 306.99m / cash 5.09m JUMP / PnL JUMP 4.67k / dividend 0 / 1 VE,7.0,8.5,3.0,7.0,Publish omzet+diensten+verhuur/koop split + 1 VE payroll + cash 5.09m JUMP + geldbeleg 0 DROP + LT krediet 281.48m counterparties + capex 32.27m + aandeel % Brecht/Kalmthout/Kapellen + dividend 0; do not keep leftover woonmaatschappij as unpublished 19.57m housing shell,active,,tick1487; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Wonen in Limburg 1486 / Woonpunt Zennevallei 1485 / !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Woonpunt Waas 1464 / RL de Voorkempen 1441 / Erfgoed Voorkempen IOED 1425",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Gemeenten>Brecht>Woonmaatschappij>DeVoorkempen>JR2025_L5,{ENT},omzet 19566170 DROP vs 20993841 + diensten 8811074 JUMP vs 8713442 + pers 4716427 58.5 VTE vs 51.7 + 1 VE + cash 5091590 JUMP vs 4853096 + geldbeleg DROP 0 vs 696417 + debt 306985521 LT krediet 281475127 + voorraden DROP 2723969 vs 2889011 + capex 32271841 + PnL JUMP 4666 vs -1266832 + dividend 0 + commissaris 15698 + bestuurders 9503 empty + aandeel % Brecht/Kalmthout/Kapellen unpublished,Leftover woonmaatschappij De Voorkempen after leftover AGB/APB hunt: omzet 19.57m DROP / pers 4.72m 58.5 VTE / debt 306.99m / cash 5.09m JUMP / PnL JUMP 4.67k / dividend 0 / 1 VE hides municipal housing vehicle,8,De Voorkempen - H.E. / Bestuursorgaan / voorzitter Erwin Callens,info@devoorkempen-he.be,Nijverheidsstraat 3 2960 Brecht,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1487 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (2156809 bytes 66p). FOI ready not sent. NOT every-10. NOT leftover RL de Voorkempen 1441 / leftover Erfgoed Voorkempen IOED 1425 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover Wonen in Limburg 1486 / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 403/404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still 302. Wonen in Limburg 1486 TAKEN. Woonpunt Zennevallei 1485 TAKEN. !Mpuls 1484 TAKEN. WoonST 1483 TAKEN. stek92 1482 TAKEN. LeefGoed 1481 TAKEN. Kanvaz 1480 TAKEN. De Voorkempen TAKEN this tick.",
])
print("foi_queue +1")

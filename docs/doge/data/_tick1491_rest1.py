#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T19:55:00Z"
ENT = "wm_onod"
SRC = "src_onod_jr2025_nbb"
GAP = "gap_onod_omzet_11_51m_pers_1_92m_debt_102m_l5"
LB = "lb_onod_omzet_11_51m_pers_1_92m_debt_102m"
COMM = "comm_onod_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00189814.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

append_lf(DATA / "commitments.csv", [
    f"{COMM},Ons Onderdak JR2025 leftover woonmaatschappij dual (omzet 11.51m / pers 1.92m 23.3 VTE / debt 101.59m / cash 5.01m DROP / PnL DROP 0.32m / dividend 0 / 1 VE),{ENT},Ieper-Heuvelland-Mesen / mined Ieper-Heuvelland-Poperinge dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-06-12,1929,,11511389,,,active,{PDF},Local leftover woonmaatschappij map VL Ieper-Heuvelland-Mesen — omzet 11.51m / pers 1.92m 23.3 VTE / debt 101.59m / cash 5.01m DROP,Publish omzet+diensten+huur/koop split + 1 VE payroll + cash 5.01m DROP + LT krediet 91.99m counterparties + capex 11.19m + in aanbouw 10.41m + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 11.51m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Ieper>Woonmaatschappij>Ons Onderdak>JR2025_L5,tick1491; assets 136782795 omzet 11511389 pers 1919909 pnl 321927 equity 34735657 cash 5008962 debt 101590448 capex 11194008 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover AGB Vauban Ieper / leftover AGB Musea Ieper / leftover Zetus 1490 / leftover IJzer en Zee / leftover Thuiswest / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"{LB},Ons Onderdak JR2025 leftover woonmaatschappij: omzet 11.51m / pers 1.92m 23.3 VTE / debt 101.59m / cash 5.01m DROP / PnL DROP 0.32m / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Ieper>Woonmaatschappij>Ons Onderdak>JR2025_L5,11511389,136782795,Leftover dual woonmaatschappij shell: assets 136.78m / equity 34.74m / omzet 11.51m / pers 1.92m 23.3 VTE / cash 5.01m DROP / debt 101.59m / LT krediet 91.99m / PnL DROP 0.32m / dividend 0 / 1 VE; do not treat 11.51m as TE-additive of 348bn,strong,{SRC},Ons Onderdak / mined Ieper-Heuvelland-Poperinge dual housing,Local leftover woonmaatschappij map VL Ieper-Heuvelland-Mesen — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 11.51m / pers 1.92m 23.3 VTE / debt 101.59m / cash 5.01m DROP / PnL DROP 0.32m / dividend 0 / 1 VE,7.0,8.0,3.0,6.8,Publish omzet+diensten+huur/koop split + 1 VE payroll + cash 5.01m DROP + LT krediet 91.99m counterparties + capex 11.19m + in aanbouw 10.41m + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 11.51m housing shell,active,,tick1491; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Zetus 1490 / Inter-Vilvoordse 1489 / Woonschakel 1488 / De Voorkempen 1487 / Wonen in Limburg 1486 / Woonpunt Zennevallei 1485 / !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / AGB Vauban Ieper / AGB Musea Ieper",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Gemeenten>Ieper>Woonmaatschappij>Ons Onderdak>JR2025_L5,{ENT},omzet 11511389 vs 10809659 + 6.10 huur 9044302 koop 2467087 + diensten 3444762 vs 3439777 + pers 1919909 23.3 VTE vs 23.4 + 1 VE + cash 5008962 DROP vs 5485677 + debt 101590448 LT krediet 91993798 + capex 11194008 + in aanbouw 10413545 JUMP + PnL DROP 321927 vs 946143 + dividend 0 + commissaris 7800 + bestuurders 9503 26515 + aandeel % unpublished,Leftover woonmaatschappij Ons Onderdak after leftover AGB/APB hunt: omzet 11.51m / pers 1.92m 23.3 VTE / debt 101.59m / cash 5.01m DROP / PnL DROP 0.32m / dividend 0 / 1 VE hides municipal housing vehicle,8,Ons Onderdak / Bestuursorgaan / voorzitter Thijs Descamps,info@onsonderdak.be,Ter Waarde 65 8900 Ieper,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1491 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (1423605 bytes 62p). FOI ready not sent. NOT every-10 (next 1500). NOT leftover AGB Vauban Ieper / leftover AGB Musea Ieper / leftover Zetus 1490 / leftover IJzer en Zee / leftover Thuiswest / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 403/404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. AGB Herzele already mined. Puyenbroeck still 302. Zetus 1490 TAKEN. Ons Onderdak TAKEN this tick.",
])
print("foi_queue +1")

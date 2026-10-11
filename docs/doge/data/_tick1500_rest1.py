#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T22:40:00Z"
ENT = "wm_vivs"
SRC = "src_vivs_jr2025_nbb"
GAP = "gap_vivs_omzet_19_55m_pers_3_21m_debt_238m_l5"
LB = "lb_vivs_omzet_19_55m_pers_3_21m_debt_238m"
COMM = "comm_vivs_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00122331.pdf"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def check(row, n, label):
    got = len(next(csv.reader(io.StringIO(row))))
    if got != n:
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:160]}")

comm = (
    f"{COMM},Woonmaatschappij Vivus JR2025 leftover woonmaatschappij dual (omzet 19.55m UP / pers 3.21m 34.8 VTE / debt 237.73m UP / cash 10.77m DROP / beleggingen 2.00m stable / capex 18.58m / in aanbouw 3.42m DROP / PnL 1.02m / dividend 0 / 1 VE),{ENT},Harelbeke-Waregem-Deerlijk-Anzegem-Wielsbeke-Dentergem-Oostrozebeke-Lendelede / mined Harelbeke+Waregem+Deerlijk+Anzegem+Wielsbeke+Dentergem+Oostrozebeke+Lendelede dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-26,1968,,19547175,,,active,{PDF},Local leftover woonmaatschappij map VL Harelbeke-Waregem-Deerlijk-Anzegem-Wielsbeke-Dentergem-Oostrozebeke-Lendelede — omzet 19.55m / pers 3.21m 34.8 VTE / debt 237.73m / cash 10.77m DROP,Publish omzet+diensten+huur/koop split + 1 VE payroll + cash 10.77m DROP + beleggingen 2.00m + LT krediet 221.59m counterparties + capex 18.58m + in aanbouw 3.42m DROP + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 19.55m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Harelbeke>Woonmaatschappij>Vivus>JR2025_L5,tick1500; assets 303989219 omzet 19547175 pers 3214483 pnl 1023260 equity 63760761 cash 10772582 debt 237728579 capex 18581782 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover WM Elan 1499 / leftover SW+ 1472 / leftover !Mpuls 1484 / leftover WAGSO Waregem / leftover AGB Wielsbeke / leftover AGL Lendelede / leftover zorg Harelbeke / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck"
)
check(comm, 19, "commitments")
append_crlf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},Woonmaatschappij Vivus JR2025 leftover woonmaatschappij: omzet 19.55m UP / pers 3.21m 34.8 VTE / debt 237.73m UP / cash 10.77m DROP / beleggingen 2.00m stable / capex 18.58m / in aanbouw 3.42m DROP / PnL 1.02m / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Harelbeke>Woonmaatschappij>Vivus>JR2025_L5,19547175,303989219,Leftover dual woonmaatschappij shell: assets 303.99m UP / equity 63.76m / omzet 19.55m UP / pers 3.21m 34.8 VTE / cash 10.77m DROP / beleggingen 2.00m / debt 237.73m UP / LT krediet 221.59m / capex 18.58m / in aanbouw 3.42m DROP / PnL 1.02m / dividend 0 / 1 VE; do not treat 19.55m as TE-additive of 348bn,strong,{SRC},Woonmaatschappij Vivus / mined Harelbeke-Waregem-Deerlijk-Anzegem-Wielsbeke-Dentergem-Oostrozebeke-Lendelede dual housing,Local leftover woonmaatschappij map VL Harelbeke-Waregem-Deerlijk-Anzegem-Wielsbeke-Dentergem-Oostrozebeke-Lendelede — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 19.55m UP / pers 3.21m 34.8 VTE / debt 237.73m UP / cash 10.77m DROP / beleggingen 2.00m / PnL 1.02m / dividend 0 / 1 VE,7.0,8.0,3.0,6.8,Publish omzet+diensten+huur/koop split + 1 VE payroll + cash 10.77m DROP + beleggingen 2.00m + LT krediet 221.59m counterparties + capex 18.58m + in aanbouw 3.42m DROP + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 19.55m housing shell,active,,tick1500; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined WM Elan 1499 / Woonpijler 1498 / de Thuisbouwer 1497 / Meetjesland 1496 / Woonstart 1495 / IJzer en Zee 1494 / Thuiswest 1493 / leftover SW+ 1472 / leftover !Mpuls 1484 / leftover WAGSO Waregem / leftover AGB Wielsbeke / leftover AGL Lendelede / leftover zorg Harelbeke"
)
check(lb, 21, "leaderboard")
append_crlf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Harelbeke>Woonmaatschappij>Vivus>JR2025_L5,{ENT},omzet 19547175 UP vs 18767838 + huur/koop split unpublished + diensten 61 8278094 vs 7488449 + pers 3214483 34.8 VTE vs 34.9 + 1 VE + cash 10772582 DROP vs 11076675 + beleggingen 2000000 + debt 237728579 UP LT krediet 221592918 + capex 18581782 + in aanbouw 3421563 DROP + PnL 1023260 vs 1022275 + dividend 0 + aandeel % unpublished,Leftover woonmaatschappij Vivus after leftover AGB/APB hunt: omzet 19.55m UP / pers 3.21m 34.8 VTE / debt 237.73m UP / cash 10.77m DROP / beleggingen 2.00m / capex 18.58m / in aanbouw 3.42m DROP / PnL 1.02m / dividend 0 / 1 VE hides municipal housing vehicle,8,Woonmaatschappij Vivus / Bestuursorgaan / voorzitter Rik Soens,info@vivus.be,Marktstraat 80 8530 Harelbeke,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1500 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (1038131 bytes 58p). FOI ready not sent. EVERY-10 this tick (next 1510). NOT leftover WM Elan 1499 / leftover SW+ 1472 / leftover !Mpuls 1484 / leftover WAGSO Waregem / leftover AGB Wielsbeke / leftover AGL Lendelede / leftover zorg Harelbeke / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. Puyenbroeck still 302. WM Elan 1499 TAKEN. Vivus TAKEN this tick. Leftover Providentia 2026-00121288 LIVE unused."
)
check(foi, 21, "foi_queue")
append_crlf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

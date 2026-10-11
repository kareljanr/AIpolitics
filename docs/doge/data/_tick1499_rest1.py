#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T22:20:00Z"
ENT = "wm_elan"
SRC = "src_elan_jr2025_nbb"
GAP = "gap_elan_omzet_10_96m_pers_2_24m_debt_137m_l5"
LB = "lb_elan_omzet_10_96m_pers_2_24m_debt_137m"
COMM = "comm_elan_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00144589.pdf"

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
    f"{COMM},WM Elan JR2025 leftover woonmaatschappij dual (omzet 10.96m UP / pers 2.24m 26.8 VTE / debt 136.94m UP / cash 9.89m DROP / beleggingen 15.00m JUMP / capex 16.41m / in aanbouw 18.38m / PnL 1.66m / dividend 0 / 2 VE),{ENT},Zwevegem-Kuurne-Avelgem-Spiere-Helkijn / mined Zwevegem+Kuurne+Avelgem+Spiere-Helkijn dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-06-02,1923,,10963582,,,active,{PDF},Local leftover woonmaatschappij map VL Zwevegem-Kuurne-Avelgem-Spiere-Helkijn — omzet 10.96m / pers 2.24m 26.8 VTE / debt 136.94m / cash 9.89m DROP,Publish omzet+diensten+huur/koop split + 2 VE payroll + cash 9.89m DROP + beleggingen 15.00m JUMP + LT krediet 121.85m counterparties + capex 16.41m + in aanbouw 18.38m + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 10.96m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Zwevegem>Woonmaatschappij>WM Elan>JR2025_L5,tick1499; assets 179416827 omzet 10963582 pers 2241828 pnl 1657825 equity 40289353 cash 9893916 debt 136938057 capex 16411769 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover AGB Zwevegem / leftover SW+ 1472 / leftover !Mpuls 1484 / leftover Vivus / leftover Woonpijler 1498 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck"
)
check(comm, 19, "commitments")
append_crlf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},WM Elan JR2025 leftover woonmaatschappij: omzet 10.96m UP / pers 2.24m 26.8 VTE / debt 136.94m UP / cash 9.89m DROP / beleggingen 15.00m JUMP / capex 16.41m / in aanbouw 18.38m / PnL 1.66m / dividend 0 / 2 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Zwevegem>Woonmaatschappij>WM Elan>JR2025_L5,10963582,179416827,Leftover dual woonmaatschappij shell: assets 179.42m UP / equity 40.29m / omzet 10.96m UP / pers 2.24m 26.8 VTE / cash 9.89m DROP / beleggingen 15.00m JUMP / debt 136.94m UP / LT krediet 121.85m / capex 16.41m / in aanbouw 18.38m / PnL 1.66m / dividend 0 / 2 VE; do not treat 10.96m as TE-additive of 348bn,strong,{SRC},WM Elan / mined Zwevegem-Kuurne-Avelgem-Spiere-Helkijn dual housing,Local leftover woonmaatschappij map VL Zwevegem-Kuurne-Avelgem-Spiere-Helkijn — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 10.96m UP / pers 2.24m 26.8 VTE / debt 136.94m UP / cash 9.89m DROP / beleggingen 15.00m JUMP / PnL 1.66m / dividend 0 / 2 VE,7.0,8.0,3.0,6.8,Publish omzet+diensten+huur/koop split + 2 VE payroll + cash 9.89m DROP + beleggingen 15.00m JUMP + LT krediet 121.85m counterparties + capex 16.41m + in aanbouw 18.38m + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 10.96m housing shell,active,,tick1499; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Woonpijler 1498 / de Thuisbouwer 1497 / Meetjesland 1496 / Woonstart 1495 / IJzer en Zee 1494 / Thuiswest 1493 / Woonsprong 1492 / Ons Onderdak 1491 / Zetus 1490 / leftover SW+ 1472 / leftover !Mpuls 1484 / leftover AGB Zwevegem"
)
check(lb, 21, "leaderboard")
append_crlf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Zwevegem>Woonmaatschappij>WM Elan>JR2025_L5,{ENT},omzet 10963582 UP vs 9886881 + huur/koop split unpublished + diensten 61 3874175 vs 3094399 + pers 2241828 26.8 VTE vs 22.5 + 2 VE + cash 9893916 DROP vs 25619244 + beleggingen 15000000 JUMP + debt 136938057 UP LT krediet 121852403 + capex 16411769 + in aanbouw 18379907 + PnL 1657825 vs 499290 + dividend 0 + aandeel % unpublished,Leftover woonmaatschappij WM Elan after leftover AGB/APB hunt: omzet 10.96m UP / pers 2.24m 26.8 VTE / debt 136.94m UP / cash 9.89m DROP / beleggingen 15.00m JUMP / capex 16.41m / in aanbouw 18.38m / PnL 1.66m / dividend 0 / 2 VE hides municipal housing vehicle,8,WM Elan / Bestuursorgaan / voorzitter Erwin Bossuyt,info@wmelan.be,Kortrijkstraat 117 8550 Zwevegem,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1499 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (992461 bytes 72p). FOI ready not sent. NOT every-10 (next 1500 MUST do the every-10 refresh). NOT leftover AGB Zwevegem / leftover SW+ 1472 / leftover !Mpuls 1484 / leftover Vivus / leftover Woonpijler 1498 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. Puyenbroeck still 302. Woonpijler 1498 TAKEN. WM Elan TAKEN this tick. Leftover Vivus 2026-00122331 LIVE unused. Leftover Providentia 2026-00121288 LIVE unused."
)
check(foi, 21, "foi_queue")
append_crlf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T01:10:00Z"
ENT = "wm_vitr"
SRC = "src_vitr_jr2025_nbb"
GAP = "gap_vitr_omzet_15_7k_nrec_2_31m_debt_41m_l5"
LB = "lb_vitr_omzet_15_7k_nrec_2_31m_debt_41m"
COMM = "comm_vitr_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00332427.pdf"

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
    f"{COMM},Vitare in vereffening JR2025 leftover former SHM dual (omzet 15.7k DROP / pers 0 0 VTE / debt 41.30m UP / cash 39.1k UP / nrec WV 2.31m / equity -24.32m / PnL 1.96m reval-driven / capex 0 / dividend 0),{ENT},Deinze / mined Deinze leftover former SHM liquidation,WVV NV in vereffening; BVR 03.02.2023 vereffenaars; Bestuursdecreet openbaarheid,2026-07-15,2008,,15730,,,active,{PDF},Local leftover former SHM map VL Deinze — omzet 15.7k / pers 0 / debt 41.30m / cash 39.1k / nrec 2.31m / equity -24.32m,Publish omzet residual + 2.31m terugneming WV Matexi-takeback + LT krediet 32.65m counterparties + ST fin 8.59m + deficitair liquidation close + aandeel Abacus/Matexi unpublished + dividend 0; do not keep leftover former SHM as unpublished 17.06m land shell,{SRC},strong,Vlaanderen>Gemeenten>Deinze>Vitare>JR2025_L5,tick1505; assets 17056698 omzet 15730 pers 0 pnl 1964420 equity -24315400 cash 39058 debt 41297098 capex 0 dividend 0 nrec 2305848; FOI ready not sent; not TE-additive of 348bn; NOT leftover Dimensa 1466 / leftover AGB Deinze / leftover Meetjesland 1496 / leftover De Noorderkempen 1504 / leftover Woontrots 1503 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck"
)
check(comm, 19, "commitments")
append_crlf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},Vitare in vereffening JR2025 leftover former SHM: omzet 15.7k DROP / pers 0 0 VTE / debt 41.30m UP / cash 39.1k UP / nrec WV 2.31m / equity -24.32m / PnL 1.96m reval-driven / capex 0 / dividend 0,L5,local_budget_line,Vlaanderen>Gemeenten>Deinze>Vitare>JR2025_L5,15730,17056698,Leftover dual former SHM liquidation shell: assets 17.06m UP / equity -24.32m / omzet 15.7k DROP / pers 0 / cash 39.1k UP / debt 41.30m UP / LT krediet 32.65m / nrec WV 2.31m Matexi-takeback / PnL 1.96m reval-driven / capex 0 / dividend 0; do not treat 15.7k as TE-additive of 348bn,strong,{SRC},Vitare / mined Deinze leftover former SHM liquidation,Local leftover former SHM map VL Deinze — JR2025 official NBB WVV live; omzet+nrec+debt+liquidation FOI,Official NBB WVV 2026-08-20: omzet 15.7k DROP / pers 0 / debt 41.30m UP / cash 39.1k UP / nrec 2.31m / PnL 1.96m / dividend 0,7.5,7.5,3.0,6.9,Publish omzet residual + 2.31m terugneming WV Matexi-takeback + LT krediet 32.65m counterparties + ST fin 8.59m + deficitair liquidation close + aandeel Abacus/Matexi unpublished + dividend 0; do not keep leftover former SHM as unpublished 17.06m land shell,active,,tick1505; leftover former SHM after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined De Noorderkempen 1504 / Woontrots 1503 / Dimensa 1466 / leftover AGB Deinze / leftover Meetjesland 1496"
)
check(lb, 21, "leaderboard")
append_crlf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Deinze>Vitare>JR2025_L5,{ENT},omzet 15730 DROP vs 22555 + nrec 76A 2305848 terugneming WV + pers 0 0 VTE + cash 39058 UP vs 29859 + debt 41297098 UP LT krediet 32652441 + ST fin 8590265 + equity -24315400 + PnL 1964420 vs -57123 + capex 0 + dividend 0 + Matexi-takeback + aandeel Abacus unpublished + liquidation close unpublished,Leftover former SHM Vitare after leftover AGB/APB hunt: omzet 15.7k DROP / pers 0 / debt 41.30m UP / cash 39.1k UP / nrec WV 2.31m Matexi-takeback / equity -24.32m / PnL 1.96m reval-driven / capex 0 / dividend 0 hides deficitair liquidation land shell,8,Vitare vereffenaars / Paul Van Der Putten / Pieter Wouters,,Loksumstraat 25 1000 Brussel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1505 leftover former SHM after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-kap PDF now extracted (652219 bytes 36p). FOI ready not sent. NOT every-10 (next 1510). NOT leftover Dimensa 1466 / leftover AGB Deinze / leftover Meetjesland 1496 / leftover De Noorderkempen 1504 / leftover Woontrots 1503 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover AGB Hoogstraten/Ravels/Rijkevorsel unused no AGB JR2025 PDF. Leftover Bosgroep still no JR. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Named leftover official-41 vein from 1464 now fully exhausted (Vitare JR2025 TAKEN this tick)."
)
check(foi, 21, "foi_queue")
append_crlf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

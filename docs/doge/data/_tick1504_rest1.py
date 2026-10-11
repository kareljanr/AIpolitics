#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T00:35:00Z"
ENT = "wm_dnkm"
SRC = "src_dnkm_jr2025_nbb"
GAP = "gap_dnkm_omzet_7_79m_pers_1_37m_debt_109m_l5"
LB = "lb_dnkm_omzet_7_79m_pers_1_37m_debt_109m"
COMM = "comm_dnkm_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00131989.pdf"

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
    f"{COMM},Woonmaatschappij De Noorderkempen JR2025 leftover woonmaatschappij dual (omzet 7.79m DROP / pers 1.37m 18.3 VTE / debt 109.23m DROP / cash 2.72m UP / capex 42.45m transfer-driven / in aanbouw 2.55m DROP / PnL 0.85m UP / dividend 0 / 1 VE),{ENT},Merksplas-Hoogstraten-Arendonk-Ravels-Rijkevorsel / mined Merksplas+Hoogstraten+Arendonk+Ravels+Rijkevorsel dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-12,1984,,7793810,,,active,{PDF},Local leftover woonmaatschappij map VL Merksplas-Hoogstraten-Arendonk-Ravels-Rijkevorsel — omzet 7.79m / pers 1.37m 18.3 VTE / debt 109.23m / cash 2.72m UP,Publish omzet+diensten+huur/andere split + 1 VE payroll + cash 2.72m UP + LT krediet 95.71m counterparties + capex 42.45m transfer-driven + in aanbouw 2.55m + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 7.79m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Merksplas>Woonmaatschappij>DeNoorderkempen>JR2025_L5,tick1504; assets 129317196 omzet 7793810 pers 1372325 pnl 853059 equity 19508599 cash 2718970 debt 109233846 capex 42448162 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover Erfgoed Noorderkempen 1426 / leftover Bosgroep Kempen Noord 1450 / leftover Woonboog 1478 / leftover De Voorkempen 1487 / leftover AGB Arendonk / leftover AGB Merksplas / leftover Woontrots 1503 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck"
)
check(comm, 19, "commitments")
append_crlf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},Woonmaatschappij De Noorderkempen JR2025 leftover woonmaatschappij: omzet 7.79m DROP / pers 1.37m 18.3 VTE / debt 109.23m DROP / cash 2.72m UP / capex 42.45m transfer-driven / in aanbouw 2.55m DROP / PnL 0.85m UP / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Merksplas>Woonmaatschappij>DeNoorderkempen>JR2025_L5,7793810,129317196,Leftover dual woonmaatschappij shell: assets 129.32m DROP / equity 19.51m / omzet 7.79m DROP / pers 1.37m 18.3 VTE / cash 2.72m UP / debt 109.23m DROP / LT krediet 95.71m / capex 42.45m transfer-driven / in aanbouw 2.55m DROP / PnL 0.85m UP / dividend 0 / 1 VE; do not treat 7.79m as TE-additive of 348bn,strong,{SRC},Woonmaatschappij De Noorderkempen / mined Merksplas-Hoogstraten-Arendonk-Ravels-Rijkevorsel dual housing,Local leftover woonmaatschappij map VL Merksplas-Hoogstraten-Arendonk-Ravels-Rijkevorsel — JR2025 official NBB WVV live; omzet+pers+debt+cash+split FOI,Official NBB WVV 2026-08-20: omzet 7.79m DROP / pers 1.37m 18.3 VTE / debt 109.23m DROP / cash 2.72m UP / capex 42.45m / PnL 0.85m UP / dividend 0 / 1 VE,7.0,8.0,3.0,6.8,Publish omzet+diensten+huur/andere split + 1 VE payroll + cash 2.72m UP + LT krediet 95.71m counterparties + capex 42.45m transfer-driven + in aanbouw 2.55m + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 7.79m housing shell,active,,tick1504; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Woontrots 1503 / Het Vlaamse Woonanker 1502 / Providentia 1501 / Vivus 1500 / leftover Erfgoed Noorderkempen 1426 / leftover Bosgroep Kempen Noord 1450 / leftover Woonboog 1478 / leftover De Voorkempen 1487 / leftover AGB Arendonk / leftover AGB Merksplas"
)
check(lb, 21, "leaderboard")
append_crlf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Merksplas>Woonmaatschappij>DeNoorderkempen>JR2025_L5,{ENT},omzet 7793810 DROP vs 9603459 + huur 7450744 andere 343065 + diensten 61 2117459 vs 2078129 + pers 1372325 18.3 VTE vs 17.6 + 1 VE + cash 2718970 UP vs 1275234 + debt 109233846 DROP LT krediet 95707198 + capex 42448162 transfer-driven + in aanbouw 2545818 DROP + PnL 853059 vs 445678 + dividend 0 + aandeel % unpublished,Leftover woonmaatschappij De Noorderkempen after leftover AGB/APB hunt: omzet 7.79m DROP / pers 1.37m 18.3 VTE / debt 109.23m DROP / cash 2.72m UP / capex 42.45m transfer-driven / in aanbouw 2.55m DROP / PnL 0.85m UP / dividend 0 / 1 VE hides municipal housing vehicle,8,Woonmaatschappij De Noorderkempen / Bestuursorgaan / voorzitter Hans Heylen,info@denoorderkempen.be,Kweekstraat 4 bus b 2330 Merksplas,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1504 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (842176 bytes 70p). FOI ready not sent. NOT every-10 (next 1510). NOT leftover Erfgoed Noorderkempen 1426 / leftover Bosgroep Kempen Noord 1450 / leftover Woonboog 1478 / leftover De Voorkempen 1487 / leftover AGB Arendonk / leftover AGB Merksplas / leftover Woontrots 1503 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. Puyenbroeck still 302. Woontrots 1503 TAKEN. De Noorderkempen TAKEN this tick. Named leftover official-41 vein from 1464 now exhausted except unpublished Vitare 0808.101.060 (in liquidation; last JR 2024)."
)
check(foi, 21, "foi_queue")
append_crlf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

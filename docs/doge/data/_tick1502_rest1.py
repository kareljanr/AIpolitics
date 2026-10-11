#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:40:00Z"
ENT = "wm_wvwa"
SRC = "src_wvwa_jr2025_nbb"
GAP = "gap_wvwa_omzet_11_80m_pers_1_92m_debt_98m_l5"
LB = "lb_wvwa_omzet_11_80m_pers_1_92m_debt_98m"
COMM = "comm_wvwa_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00145176.pdf"

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
    f"{COMM},Het Vlaamse Woonanker JR2025 leftover woonmaatschappij dual (omzet 11.80m UP / pers 1.92m 22.7 VTE / debt 98.32m DROP / cash 2.89m DROP / capex 1.29m / in aanbouw 1.02m DROP / PnL LOSS 0.96m / dividend 0 / 1 VE),{ENT},Grimbergen-Kampenhout-Kapelle-Meise-Steenokkerzeel-Zemst-Sint-Pieters-Leeuw-Londerzeel-Drogenbos / mined Grimbergen+Kampenhout+Kapelle-op-den-Bos+Meise+Steenokkerzeel+Zemst+Sint-Pieters-Leeuw dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-27,1922,,11795988,,,active,{PDF},Local leftover woonmaatschappij map VL Grimbergen-Kampenhout-Kapelle-Meise-Steenokkerzeel-Zemst-Sint-Pieters-Leeuw-Londerzeel-Drogenbos — omzet 11.80m / pers 1.92m 22.7 VTE / debt 98.32m / cash 2.89m DROP,Publish omzet+diensten+huur/koop split + 1 VE payroll + cash 2.89m DROP + LT krediet 87.07m counterparties + patrimonial split + capex 1.29m + in aanbouw 1.02m + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 11.80m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Sint-Pieters-Leeuw>Woonmaatschappij>HetVlaamseWoonanker>JR2025_L5,tick1502; assets 116281420 omzet 11795988 pers 1918960 pnl -960306 equity 16952289 cash 2894405 debt 98315832 capex 1292536 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover Providentia 1501 / leftover Woonpunt Zennevallei 1485 / leftover Inter-Vilvoordse 1489 / leftover Fluvius Halle-Vilvoorde / leftover AGB Grimbergen / leftover Erfgoed Brabantse Kouters 1428 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck"
)
check(comm, 19, "commitments")
append_crlf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},Het Vlaamse Woonanker JR2025 leftover woonmaatschappij: omzet 11.80m UP / pers 1.92m 22.7 VTE / debt 98.32m DROP / cash 2.89m DROP / capex 1.29m / in aanbouw 1.02m DROP / PnL LOSS 0.96m / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Sint-Pieters-Leeuw>Woonmaatschappij>HetVlaamseWoonanker>JR2025_L5,11795988,116281420,Leftover dual woonmaatschappij shell: assets 116.28m DROP / equity 16.95m / omzet 11.80m UP / pers 1.92m 22.7 VTE / cash 2.89m DROP / debt 98.32m DROP / LT krediet 87.07m / capex 1.29m / in aanbouw 1.02m DROP / PnL LOSS 0.96m / dividend 0 / 1 VE; patrimonial split; do not treat 11.80m as TE-additive of 348bn,strong,{SRC},Het Vlaamse Woonanker / mined Grimbergen-Kampenhout-Kapelle-Meise-Steenokkerzeel-Zemst-Sint-Pieters-Leeuw dual housing,Local leftover woonmaatschappij map VL Grimbergen-Kampenhout-Kapelle-Meise-Steenokkerzeel-Zemst-Sint-Pieters-Leeuw-Londerzeel-Drogenbos — JR2025 official NBB WVV live; omzet+pers+debt+cash+split FOI,Official NBB WVV 2026-08-19: omzet 11.80m UP / pers 1.92m 22.7 VTE / debt 98.32m DROP / cash 2.89m DROP / capex 1.29m / PnL LOSS 0.96m / dividend 0 / 1 VE,7.0,8.0,3.0,6.8,Publish omzet+diensten+huur/koop split + 1 VE payroll + cash 2.89m DROP + LT krediet 87.07m counterparties + patrimonial split + capex 1.29m + in aanbouw 1.02m + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 11.80m housing shell,active,,tick1502; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Providentia 1501 / Vivus 1500 / WM Elan 1499 / Woonpijler 1498 / leftover Woonpunt Zennevallei 1485 / leftover Inter-Vilvoordse 1489 / leftover AGB Grimbergen / leftover AGB Steenokkerzeel / leftover AGB Sint-Pieters-Leeuw / leftover AGB Zemst / leftover Erfgoed Brabantse Kouters 1428"
)
check(lb, 21, "leaderboard")
append_crlf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Sint-Pieters-Leeuw>Woonmaatschappij>HetVlaamseWoonanker>JR2025_L5,{ENT},omzet 11795988 UP vs 11766080 + huur/koop split unpublished + diensten 61 7038929 vs 5686000 + pers 1918960 22.7 VTE vs 22.2 + 1 VE + cash 2894405 DROP vs 5636147 + debt 98315832 DROP LT krediet 87065225 + capex 1292536 + in aanbouw 1018203 DROP + PnL -960306 vs -1919997 + patrimonial split assets 178981322 to 116281420 + dividend 0 + aandeel % unpublished,Leftover woonmaatschappij Het Vlaamse Woonanker after leftover AGB/APB hunt: omzet 11.80m UP / pers 1.92m 22.7 VTE / debt 98.32m DROP / cash 2.89m DROP / capex 1.29m / in aanbouw 1.02m DROP / PnL LOSS 0.96m / patrimonial split / dividend 0 / 1 VE hides municipal housing vehicle,8,Het Vlaamse Woonanker / Bestuursorgaan / voorzitter Bart Laeremans,Ann@hvw.vlaanderen,Bezemstraat 83 bus A 1600 Sint-Pieters-Leeuw,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1502 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (998995 bytes 61p). FOI ready not sent. NOT every-10 (next 1510). NOT leftover Providentia 1501 / leftover Woonpunt Zennevallei 1485 / leftover Inter-Vilvoordse 1489 / leftover Fluvius Halle-Vilvoorde / leftover AGB Grimbergen / leftover AGB Steenokkerzeel / leftover AGB Sint-Pieters-Leeuw / leftover AGB Zemst / leftover Erfgoed Brabantse Kouters 1428 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. Puyenbroeck still 302. Providentia 1501 TAKEN. Het Vlaamse Woonanker TAKEN this tick. Leftover Woontrots 0400.629.794 deposit 2026-00170888 LIVE unused / leftover De Noorderkempen 0427.003.106 deposit 2026-00131989 LIVE unused / leftover Vitare 0808.101.060 unused."
)
check(foi, 21, "foi_queue")
append_crlf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

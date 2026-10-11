#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:15:00Z"
ENT = "wm_prvd"
SRC = "src_prvd_jr2025_nbb"
GAP = "gap_prvd_omzet_20_81m_pers_3_57m_debt_196m_l5"
LB = "lb_prvd_omzet_20_81m_pers_3_57m_debt_196m"
COMM = "comm_prvd_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00121288.pdf"

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
    f"{COMM},Providentia JR2025 leftover woonmaatschappij dual (omzet 20.81m DROP / pers 3.57m 39.1 VTE / debt 195.93m UP / cash 5.32m UP / capex 92.69m / in aanbouw 6.17m / PnL 1.63m DROP / dividend 0 / 1 VE),{ENT},Asse-Dilbeek-Affligem-Bever-Lennik-Liedekerke-Merchtem-Opwijk-Roosdaal-Ternat-Wemmel-Pajottegem / mined Asse+Dilbeek+Affligem+Bever+Lennik+Liedekerke+Merchtem+Opwijk+Roosdaal+Ternat+Wemmel+Pajottegem dual housing,WVV BV; Vlaamse Codex Wonen; Bestuursdecreet openbaarheid,2026-05-07,1968,,20807498,,,active,{PDF},Local leftover woonmaatschappij map VL Asse-Dilbeek-Affligem-Bever-Lennik-Liedekerke-Merchtem-Opwijk-Roosdaal-Ternat-Wemmel-Pajottegem — omzet 20.81m / pers 3.57m 39.1 VTE / debt 195.93m / cash 5.32m UP,Publish omzet+diensten+huur/koop split + 1 VE payroll + cash 5.32m UP + LT krediet 172.76m counterparties + capex 92.69m + in aanbouw 6.17m + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 20.81m housing shell,{SRC},strong,Vlaanderen>Gemeenten>Asse>Woonmaatschappij>Providentia>JR2025_L5,tick1501; assets 228332050 omzet 20807498 pers 3571584 pnl 1625580 equity 29021932 cash 5321913 debt 195927025 capex 92686585 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT leftover Woonpunt Zennevallei 1485 / leftover Inter-Vilvoordse 1489 / leftover Fluvius Halle-Vilvoorde / leftover AGA Asse / leftover Vivus 1500 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck"
)
check(comm, 19, "commitments")
append_crlf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},Providentia JR2025 leftover woonmaatschappij: omzet 20.81m DROP / pers 3.57m 39.1 VTE / debt 195.93m UP / cash 5.32m UP / capex 92.69m / in aanbouw 6.17m / PnL 1.63m DROP / dividend 0 / 1 VE,L5,local_budget_line,Vlaanderen>Gemeenten>Asse>Woonmaatschappij>Providentia>JR2025_L5,20807498,228332050,Leftover dual woonmaatschappij shell: assets 228.33m UP / equity 29.02m / omzet 20.81m DROP / pers 3.57m 39.1 VTE / cash 5.32m UP / debt 195.93m UP / LT krediet 172.76m / capex 92.69m / in aanbouw 6.17m / PnL 1.63m DROP / dividend 0 / 1 VE; do not treat 20.81m as TE-additive of 348bn,strong,{SRC},Providentia / mined Asse-Dilbeek-Affligem-Bever-Lennik-Liedekerke-Merchtem-Opwijk-Roosdaal-Ternat-Wemmel-Pajottegem dual housing,Local leftover woonmaatschappij map VL Asse-Dilbeek-Affligem-Bever-Lennik-Liedekerke-Merchtem-Opwijk-Roosdaal-Ternat-Wemmel-Pajottegem — JR2025 official NBB WVV live; omzet+pers+debt+cash FOI,Official NBB WVV 2026-08-19: omzet 20.81m DROP / pers 3.57m 39.1 VTE / debt 195.93m UP / cash 5.32m UP / capex 92.69m / PnL 1.63m DROP / dividend 0 / 1 VE,7.0,8.0,3.0,6.8,Publish omzet+diensten+huur/koop split + 1 VE payroll + cash 5.32m UP + LT krediet 172.76m counterparties + capex 92.69m + in aanbouw 6.17m + aandeel % unpublished + dividend 0; do not keep leftover woonmaatschappij as unpublished 20.81m housing shell,active,,tick1501; leftover woonmaatschappij after leftover AGB/APB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Vivus 1500 / WM Elan 1499 / Woonpijler 1498 / de Thuisbouwer 1497 / Meetjesland 1496 / Woonstart 1495 / IJzer en Zee 1494 / Thuiswest 1493 / leftover Woonpunt Zennevallei 1485 / leftover Inter-Vilvoordse 1489 / leftover AGA Asse / leftover AGB Ternat / leftover AGB Roosdaal / leftover AGB Merchtem"
)
check(lb, 21, "leaderboard")
append_crlf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Asse>Woonmaatschappij>Providentia>JR2025_L5,{ENT},omzet 20807498 DROP vs 20921943 + huur/koop split unpublished + diensten 61 9020541 vs 9492446 + pers 3571584 39.1 VTE vs 38.6 + 1 VE + cash 5321913 UP vs 4421330 + debt 195927025 UP LT krediet 172755477 + capex 92686585 + in aanbouw 6171593 + PnL 1625580 vs 2449202 + dividend 0 + aandeel % unpublished,Leftover woonmaatschappij Providentia after leftover AGB/APB hunt: omzet 20.81m DROP / pers 3.57m 39.1 VTE / debt 195.93m UP / cash 5.32m UP / capex 92.69m / in aanbouw 6.17m / PnL 1.63m DROP / dividend 0 / 1 VE hides municipal housing vehicle,8,Providentia / Bestuursorgaan / algemeen directeur Leen Deraedt,info@providentia.be,Brusselsesteenweg 191 1730 Asse,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1501 leftover woonmaatschappij after honest leftover AGB/APB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (1196609 bytes 80p). FOI ready not sent. NOT every-10 (next 1510). NOT leftover Woonpunt Zennevallei 1485 / leftover Inter-Vilvoordse 1489 / leftover Fluvius Halle-Vilvoorde / leftover AGA Asse / leftover Vivus 1500 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck. Leftover APB Inovant/Atlas slugs 404 this tick. Leftover Bosgroep still no JR as of 1471. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Zender/Zuidrand/Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. AGB Bornem still 2024. Puyenbroeck still 302. Vivus 1500 TAKEN. Providentia TAKEN this tick. Leftover Het Vlaamse Woonanker 0403.304.026 / leftover Woontrots 0400.629.794 / leftover De Noorderkempen 0427.003.106 / leftover Vitare 0808.101.060 unused."
)
check(foi, 21, "foi_queue")
append_crlf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

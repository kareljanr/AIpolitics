#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
TS = "2026-08-19T10:30:00Z"
ENT = "nv_bnlg"
SRC = "src_bnlg_jr2025_nbb"
GAP = "gap_bnlg_omzet_1_72m_diensten_1_29m_l5"
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
append_lf(DATA / "commitments.csv", [
    f"comm_bnlg_jr2025_omzet,BIONERGA LOGISTICS JR2025 leftover daughter dual (assets 3.51m / omzet 1.72m / diensten 1.29m / cash 0.96m / debt 1.85m / PnL +0.14m),{ENT},BIONERGA LOGISTICS / Bionerga NV / Limburg.net Optimo,WVV NV; NBB neerlegging; 100pct dochter Bionerga NV 0882.280.227,2026-04-20,2014,,1717525,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00119950.pdf,Local leftover daughter map VL Limburg Optimo truck fleet — 1.72m omzet / 1.29m diensten / 0.96m cash / 1.85m debt / PnL +0.14m,Publish 6.10 omzet category+geo + diensten 61 split + related-party recv/debt counterparts + leveranciers JUMP + pers empty explanation; do not keep leftover Logistics as dual unpublished vehicle,{SRC},strong,Vlaanderen>Limburg>Bionerga>BIONERGA LOGISTICS>JR2025_L5,tick1423; assets 3510439 omzet 1717525 diensten 1289949 pers empty pnl 142458 equity 1664756 cash 956680 debt 1845683 capex 355000 dividend 0; FOI ready not sent; not TE-additive of 348bn",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"lb_bnlg_omzet_1_72m_diensten_1_29m_cash_0_96m,BIONERGA LOGISTICS JR2025 leftover daughter: assets 3.51m / omzet 1.72m / diensten 1.29m / cash 0.96m,L5,local_budget_line,Vlaanderen>Limburg>Bionerga>BIONERGA LOGISTICS>JR2025_L5,1717525,3510439,Leftover dual daughter: assets 3.51m / equity 1.66m / pnl +0.14m / omzet 1.72m 6.10 empty / diensten 1.29m unpublished split / pers empty / cash 0.96m JUMP / debt 1.85m (LT bank 1.13m) / leveranciers JUMP 0.33m / dividend 0,strong,{SRC},BIONERGA LOGISTICS / Bionerga NV / Limburg.net,Local leftover daughter map VL Limburg Optimo — JR2025 live; dual omzet/diensten/related-party FOI,Official NBB WVV 2026-08-19: assets 3.51m / omzet 1.72m / diensten 1.29m / cash 0.96m,6.6,4.5,2.0,5.1,Publish 6.10 omzet category+geo + diensten 61 split + related-party recv/debt counterparts + leveranciers JUMP + pers empty explanation; do not keep leftover Logistics as dual unpublished vehicle,active,,tick1423; leftover daughter after leftover AGB/IGS hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Bionerga NV 1354 / Limburg.net 1353 / Nuhma seam 1355-1365 / Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Limburg>Bionerga>BIONERGA LOGISTICS>JR2025_L5,{ENT},omzet 70 filled 1717525 but 6.10 category+geo empty + diensten 61 filled 1289949 unpublished as a split + pers 62 empty / VTE unpublished + related-party verbonden debt 153046 / assoc recv 338386 counterparts unpublished + leveranciers 331702 JUMP vs 100702 + other ST 29289 DROP vs 250057 + CIP 355000 counterpart unpublished,Leftover 100pct Bionerga daughter after leftover AGB/IGS hunt: 3.51m assets / 1.72m omzet hides public-perimeter Optimo truck vehicle,8,BIONERGA LOGISTICS NV / Raad van Bestuur / Bionerga NV,info@bionerga.be,Herkenrodesingel 14 3500 Hasselt,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_bnlg_jr2025_omzet,lb_bnlg_omzet_1_72m_diensten_1_29m_cash_0_96m,{TS},{TS},tick1423 leftover daughter after honest leftover AGB/IGS hunt; live JR2025 official NBB WVV VOL-kap PDF now extracted (2003913 bytes 90p deposit 2026-00119950). FOI ready not sent. IVAREM still JR2024. Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. Cultuur Noordrand still no jaarrekening.",
])
print("foi_queue +1")

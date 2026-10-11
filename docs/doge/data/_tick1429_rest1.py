#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
TS = "2026-08-19T11:15:00Z"
ENT = "igs_kstf"
SRC = "src_kstf_jr2025_nbb"
GAP = "gap_kstf_omzet_empty_pers_0_26m_bruto_0_25m_l5"
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
append_lf(DATA / "commitments.csv", [
    f"comm_kstf_jr2025_bruto,Kusterfgoed JR2025 leftover IGS dual (brutomarge 0.25m / pers 0.26m / cash 0.15m / empty 70-73-60/61),{ENT},Kusterfgoed / 5 Middenkust cities,WVV projectvereniging; NBB neerlegging; 5 Middenkust gemeenten + Knokke-Heist 2026,2026-03-25,2012,,248766,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00241009.pdf,Local leftover IGS map VL Middenkust erfgoed — 0.25m brutomarge / 0.26m pers / empty 70/73/60/61 / PnL -0.02m,Publish empty 70/73/60/61 split + pers 0.26m deelwerking + cash drop + vennoten share-pct; do not keep leftover Kusterfgoed as dual unpublished vehicle,{SRC},strong,Vlaanderen>WestVlaanderen>Middenkust>Kusterfgoed>JR2025_L5,tick1429; assets 162729 omzet empty diensten empty lidgeld empty pers 263807 pnl -16180 equity 100647 cash 153074 debt 62082 capex 0 dividend 0; FOI ready not sent; not TE-additive of 348bn",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"lb_kstf_omzet_empty_pers_0_26m_bruto_0_25m,Kusterfgoed JR2025 leftover IGS: brutomarge 0.25m / pers 0.26m / empty 70-73-60/61 / cash 0.15m,L5,local_budget_line,Vlaanderen>WestVlaanderen>Middenkust>Kusterfgoed>JR2025_L5,248766,162729,Leftover dual IGS: assets 0.16m / equity 0.10m / pnl -0.02m / omzet empty / 73 empty / diensten empty / pers 0.26m / cash 0.15m / debt 0.06m / dividend 0,strong,{SRC},Kusterfgoed / 5 Middenkust cities,Local leftover IGS map VL Middenkust erfgoed — JR2025 live; dual empty 70/73/60/61 / pers FOI,Official NBB WVV 2026-08-19: brutomarge 0.25m / pers 0.26m / cash 0.15m / PnL -0.02m,6.8,5.2,2.0,5.4,Publish empty 70/73/60/61 split + pers 0.26m deelwerking + cash drop + vennoten share-pct; do not keep leftover Kusterfgoed as dual unpublished vehicle,active,,tick1429; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>WestVlaanderen>Middenkust>Kusterfgoed>JR2025_L5,{ENT},omzet 70 empty + lidgeld/subsidies 73 empty + 60/61 empty + pers 263807 / 3.4 VTE deelwerking unpublished + cash DROP 153074 vs 165432 + leveranciers 9714 JUMP counterpart unpublished + EV DROP 100647 vs 116827 + continuity WVV 3:6 §1 6° + IVA/MVA disposal + vennoten share-pct unpublished + Knokke-Heist 2026 contribution unpublished + commissaris unpublished,Leftover Kusterfgoed IGS after leftover AGB hunt: 0.25m brutomarge / 0.26m pers / empty 70/73/60/61 hides public-perimeter erfgoed vehicle,8,Kusterfgoed / Raad van Bestuur,info@kusterfgoed.be,InnovOcean Campus Jacobsenstraat 1 8400 Oostende,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_kstf_jr2025_bruto,lb_kstf_omzet_empty_pers_0_26m_bruto_0_25m,{TS},{TS},tick1429 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV MIC-VZW PDF now extracted (45818 bytes 11p deposit 2026-00241009). FOI ready not sent. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. RL Lage Kempen 0677.597.755 JR2025 CDN live leftover for next.",
])
print("foi_queue +1")

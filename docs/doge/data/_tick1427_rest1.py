#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
TS = "2026-08-19T10:50:00Z"
ENT = "igs_eddl"
SRC = "src_eddl_jr2025_nbb"
GAP = "gap_eddl_subs_0_50m_diensten_0_57m_recv_0_10m_l5"
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
append_lf(DATA / "commitments.csv", [
    f"comm_eddl_jr2025_subs,Erfgoed Denderland JR2025 leftover IGS dual (assets 0.45m / subsidies 0.50m / diensten 0.57m / cash 0.32m / PnL -77k),{ENT},Erfgoed Denderland / 6 Denderland cities,WVV projectvereniging; NBB neerlegging; 6 Denderland gemeenten,2026-03-20,2013,,498745,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00110901.pdf,Local leftover IGS map VL Denderland erfgoed — 0.50m subsidies / 0.57m diensten / 0.10m other recv / 0.32m cash / PnL -77k,Publish 73 subsidy split + diensten 60/61 split + other recv 0.10m counterpart + pers/VTE + vennoten share-pct; do not keep leftover Denderland as dual unpublished vehicle,{SRC},strong,Vlaanderen>OostVlaanderen>Denderland>ErfgoedDenderland>JR2025_L5,tick1427; assets 454221 lidgeld 498745 omzet 100 diensten 573634 pers empty pnl -76695 equity 73209 cash 320049 debt 381012 capex 0 dividend 0; FOI ready not sent; not TE-additive of 348bn",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"lb_eddl_subs_0_50m_diensten_0_57m_recv_0_10m,Erfgoed Denderland JR2025 leftover IGS: assets 0.45m / subsidies 0.50m / diensten 0.57m / other recv 0.10m,L5,local_budget_line,Vlaanderen>OostVlaanderen>Denderland>ErfgoedDenderland>JR2025_L5,498745,454221,Leftover dual IGS: assets 0.45m / equity 0.07m / pnl -77k / omzet token 100 / diensten 0.57m unpublished / pers empty / cash 0.32m DROP / debt 0.38m / other recv 0.10m / dividend 0,strong,{SRC},Erfgoed Denderland / 6 Denderland cities,Local leftover IGS map VL Denderland erfgoed — JR2025 live; dual omzet/diensten/recv/pers FOI,Official NBB WVV 2026-08-19: assets 0.45m / subsidies 0.50m / diensten 0.57m / cash 0.32m,6.8,5.3,2.0,5.3,Publish 73 subsidy split + diensten 60/61 split + other recv 0.10m counterpart + pers/VTE + vennoten share-pct; do not keep leftover Denderland as dual unpublished vehicle,active,,tick1427; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>OostVlaanderen>Denderland>ErfgoedDenderland>JR2025_L5,{ENT},omzet 70 token 100 + lidgeld/subsidies 498745 unpublished as a split + 60/61 573634 unpublished as a split + pers 62 empty / VTE unpublished + overige vorderingen 95969 JUMP counterpart unpublished + cash 320049 DROP vs 402847 + leveranciers 361155 counterpart unpublished + vennoten share-pct unpublished + commissaris unpublished,Leftover Denderland IGS after leftover AGB hunt: 0.45m assets / 0.50m subsidies / 0.57m diensten hides public-perimeter erfgoed vehicle,8,Erfgoed Denderland / Raad van Bestuur,erfgoedcel@aalst.be,Onderwijsstraat 1 9300 Aalst,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_eddl_jr2025_subs,lb_eddl_subs_0_50m_diensten_0_57m_recv_0_10m,{TS},{TS},tick1427 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV MIC-VZW PDF now extracted (40314 bytes 10p deposit 2026-00110901). FOI ready not sent. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. Dommelhof leftover EVA no jaarrekening.",
])
print("foi_queue +1")

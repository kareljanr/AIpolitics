#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
TS = "2026-08-19T11:00:00Z"
ENT = "igs_ebk"
SRC = "src_ebk_jr2025_nbb"
GAP = "gap_ebk_assets_0_20m_lev_0_15m_empty_pnl_l5"
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
append_lf(DATA / "commitments.csv", [
    f"comm_ebk_jr2025_assets,Erfgoed Brabantse Kouters JR2025 leftover IGS dual (assets 0.20m / cash 0.17m / leveranciers 0.15m / empty P&L),{ENT},Erfgoed Brabantse Kouters / 12 Brabantse Kouters cities,WVV projectvereniging; NBB neerlegging; 12 Brabantse Kouters gemeenten,2026-03-25,2020,,200838,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00321349.pdf,Local leftover IGS map VL Brabantse Kouters erfgoed — 0.20m assets / 0.17m cash / 0.15m leveranciers / empty 70/73/60/61 / PnL 0,Publish empty 70/73/60/61 split + leveranciers 0.15m counterpart + empty EV + vennoten share-pct; do not keep leftover Brabantse Kouters as dual unpublished vehicle,{SRC},strong,Vlaanderen>VlaamsBrabant>BrabantseKouters>ErfgoedBrabantseKouters>JR2025_L5,tick1428; assets 200838 omzet empty diensten empty lidgeld empty pers empty pnl 0 equity empty cash 172470 debt 200838 capex 0 dividend 0; FOI ready not sent; not TE-additive of 348bn",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"lb_ebk_assets_0_20m_lev_0_15m_cash_0_17m,Erfgoed Brabantse Kouters JR2025 leftover IGS: assets 0.20m / leveranciers 0.15m / cash 0.17m / empty P&L,L5,local_budget_line,Vlaanderen>VlaamsBrabant>BrabantseKouters>ErfgoedBrabantseKouters>JR2025_L5,200838,200838,Leftover dual IGS: assets 0.20m / equity empty / pnl 0 / omzet empty / 73 empty / diensten empty / pers empty / cash 0.17m / debt 0.20m / leveranciers 0.15m / dividend 0,strong,{SRC},Erfgoed Brabantse Kouters / 12 Brabantse Kouters cities,Local leftover IGS map VL Brabantse Kouters erfgoed — JR2025 live; dual empty P&L / leveranciers FOI,Official NBB WVV 2026-08-19: assets 0.20m / cash 0.17m / leveranciers 0.15m / PnL 0,6.6,4.8,2.0,5.0,Publish empty 70/73/60/61 split + leveranciers 0.15m counterpart + empty EV + vennoten share-pct; do not keep leftover Brabantse Kouters as dual unpublished vehicle,active,,tick1428; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>VlaamsBrabant>BrabantseKouters>ErfgoedBrabantseKouters>JR2025_L5,{ENT},omzet 70 empty + lidgeld/subsidies 73 empty + 60/61 empty + pers 62 empty / VTE unpublished + EV 10/15 empty + leveranciers 153718 counterpart unpublished + deferred 47119 JUMP vs 30062 + prepaid 28368 + vennoten share-pct unpublished + commissaris unpublished + Vlaamse IOED-subsidie 2025 unpublished,Leftover Brabantse Kouters IGS after leftover AGB hunt: 0.20m assets / 0.15m leveranciers / empty P&L hides public-perimeter erfgoed vehicle,8,Erfgoed Brabantse Kouters / Raad van Bestuur,info@brabantsekouters.be,Houtemsesteenweg 23 1800 Vilvoorde,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_ebk_jr2025_assets,lb_ebk_assets_0_20m_lev_0_15m_cash_0_17m,{TS},{TS},tick1428 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV MIC-VZW PDF now extracted (34843 bytes 7p deposit 2026-00321349). FOI ready not sent. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Kusterfgoed 0552.559.411 JR2025 CDN live leftover for next.",
])
print("foi_queue +1")

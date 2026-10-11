#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
TS = "2026-08-19T10:25:00Z"
ENT = "igs_evpk"
SRC = "src_evpk_jr2025_nbb"
GAP = "gap_evpk_omzet_empty_recv_0_11m_trade_0_45m_l5"
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
append_lf(DATA / "commitments.csv", [
    f"comm_evpk_jr2025_brutomarge,Erfgoed Voorkempen JR2025 leftover IGS dual (assets 0.62m / brutomarge 0.05m / cash 0.50m / leveranciers 0.45m / PnL +48k),{ENT},Erfgoed Voorkempen / 14 Voorkempen cities,WVV projectvereniging; NBB neerlegging; 14 Voorkempen gemeenten,2026-03-27,2016,,49498,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00151989.pdf,Local leftover IGS map VL Voorkempen erfgoed — 0.05m brutomarge / 0.12m other recv / 0.45m leveranciers / 0.50m cash / PnL +48k,Publish omzet 70 + diensten 60/61 split + other recv 0.11m counterpart + leveranciers 0.45m counterpart + pers/VTE + vennoten share-pct; do not keep leftover Voorkempen as dual unpublished vehicle,{SRC},strong,Vlaanderen>Antwerpen>Voorkempen>ErfgoedVoorkempen>JR2025_L5,tick1425; assets 623422 brutomarge 49498 omzet empty diensten empty pers empty pnl 48253 equity 125438 cash 499042 debt 497984 capex 0 dividend 0; FOI ready not sent; not TE-additive of 348bn",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"lb_evpk_brutomarge_0_05m_recv_0_11m_trade_0_45m,Erfgoed Voorkempen JR2025 leftover IGS: assets 0.62m / brutomarge 0.05m / other recv 0.11m / leveranciers 0.45m,L5,local_budget_line,Vlaanderen>Antwerpen>Voorkempen>ErfgoedVoorkempen>JR2025_L5,49498,623422,Leftover dual IGS: assets 0.62m / equity 0.13m / pnl +48k / omzet empty / diensten unpublished / pers empty / cash 0.50m DROP / debt 0.50m (leveranciers 0.45m) / other recv 0.11m / dividend 0,strong,{SRC},Erfgoed Voorkempen / 14 Voorkempen cities,Local leftover IGS map VL Voorkempen erfgoed — JR2025 live; dual omzet/diensten/recv/leveranciers FOI,Official NBB WVV 2026-08-19: assets 0.62m / brutomarge 0.05m / cash 0.50m,6.4,3.8,2.0,4.8,Publish omzet 70 + diensten 60/61 split + other recv 0.11m counterpart + leveranciers 0.45m counterpart + pers/VTE + vennoten share-pct; do not keep leftover Voorkempen as dual unpublished vehicle,active,,tick1425; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / AGB Zoersel / AGB Kapellen / IGEAN",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Antwerpen>Voorkempen>ErfgoedVoorkempen>JR2025_L5,{ENT},omzet 70 empty + 60/61 empty so diensten unpublished as a split + pers 62 empty / VTE unpublished + overige vorderingen 114279 counterpart unpublished + leveranciers 453765 counterpart unpublished + cash 499042 DROP vs 555586 + deferred 44219 DROP vs 203120 + vennoten share-pct unpublished + commissaris unpublished,Leftover Voorkempen IGS after leftover AGB hunt: 0.62m assets / 0.05m brutomarge hides public-perimeter erfgoed vehicle,8,Erfgoed Voorkempen / Raad van Bestuur,info@rldevoorkempen.be,Schildesteenweg 99 2520 Ranst,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_evpk_jr2025_brutomarge,lb_evpk_brutomarge_0_05m_recv_0_11m_trade_0_45m,{TS},{TS},tick1425 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV MIC-inb PDF now extracted (44523 bytes 12p deposit 2026-00151989). FOI ready not sent. Erfgoed Noorderkempen leftover-next live CDN 2026-00061596. IVAREM still JR2024. Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening. Cultuur Noordrand still no jaarrekening.",
])
print("foi_queue +1")

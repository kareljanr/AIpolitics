#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
TS = "2026-08-19T10:35:00Z"
ENT = "igs_enpk"
SRC = "src_enpk_jr2025_nbb"
GAP = "gap_enpk_omzet_empty_pers_0_77m_recv_0_07m_l5"
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
append_lf(DATA / "commitments.csv", [
    f"comm_enpk_jr2025_brutomarge,Erfgoed Noorderkempen JR2025 leftover IGS dual (assets 0.48m / brutomarge 0.83m / pers 0.77m / cash 0.38m / PnL +57k),{ENT},Erfgoed Noorderkempen / 11 Noorderkempen cities,WVV projectvereniging; NBB neerlegging; 11 Noorderkempen gemeenten,2026-03-24,2004,,831915,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00061596.pdf,Local leftover IGS map VL Noorderkempen erfgoed — 0.83m brutomarge / 0.77m pers / 0.07m other recv / 0.38m cash / PnL +57k,Publish omzet 70 + diensten 60/61 split + other recv 0.07m counterpart + pers/deelwerking split + vennoten share-pct; do not keep leftover Noorderkempen as dual unpublished vehicle,{SRC},strong,Vlaanderen>Antwerpen>Noorderkempen>ErfgoedNoorderkempen>JR2025_L5,tick1426; assets 480193 brutomarge 831915 omzet empty diensten empty pers 767960 pnl 56632 equity 401292 cash 376948 debt 78901 capex 4084 dividend 0; FOI ready not sent; not TE-additive of 348bn",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"lb_enpk_brutomarge_0_83m_pers_0_77m_recv_0_07m,Erfgoed Noorderkempen JR2025 leftover IGS: assets 0.48m / brutomarge 0.83m / pers 0.77m / other recv 0.07m,L5,local_budget_line,Vlaanderen>Antwerpen>Noorderkempen>ErfgoedNoorderkempen>JR2025_L5,831915,480193,Leftover dual IGS: assets 0.48m / equity 0.40m / pnl +57k / omzet empty / diensten unpublished / pers 0.77m VTE 9.2 / cash 0.38m UP / debt 0.08m / other recv 0.07m / dividend 0,strong,{SRC},Erfgoed Noorderkempen / 11 Noorderkempen cities,Local leftover IGS map VL Noorderkempen erfgoed — JR2025 live; dual omzet/diensten/recv/pers FOI,Official NBB WVV 2026-08-19: assets 0.48m / brutomarge 0.83m / pers 0.77m / cash 0.38m,6.6,5.4,2.0,5.2,Publish omzet 70 + diensten 60/61 split + other recv 0.07m counterpart + pers/deelwerking split + vennoten share-pct; do not keep leftover Noorderkempen as dual unpublished vehicle,active,,tick1426; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Druivenstreek 1422",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Antwerpen>Noorderkempen>ErfgoedNoorderkempen>JR2025_L5,{ENT},omzet 70 empty + 60/61 empty so diensten unpublished as a split + pers 767960 / VTE 9.2 deelwerking unpublished + overige vorderingen 71602 counterpart unpublished + cash 376948 UP vs 325115 + vennoten share-pct unpublished + commissaris unpublished,Leftover Noorderkempen IGS after leftover AGB hunt: 0.48m assets / 0.83m brutomarge / 0.77m pers hides public-perimeter erfgoed vehicle,8,Erfgoed Noorderkempen / Raad van Bestuur,info@erfgoednoorderkempen.be,Grote Markt 1 2300 Turnhout,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_enpk_jr2025_brutomarge,lb_enpk_brutomarge_0_83m_pers_0_77m_recv_0_07m,{TS},{TS},tick1426 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV VKT-inb PDF now extracted (56875 bytes 17p deposit 2026-00061596). FOI ready not sent. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. Dommelhof leftover EVA no jaarrekening.",
])
print("foi_queue +1")

#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
TS = "2026-08-19T11:45:00Z"
ENT = "igs_rpsk"
SRC = "src_rpsk_jr2025_nbb"
GAP = "gap_rpsk_omzet_empty_bruto_neg_cash_drop_l5"
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
append_lf(DATA / "commitments.csv", [
    f"comm_rpsk_jr2025_bruto,Erfgoed Rupelstreek JR2025 leftover IGS dual (negative brutomarge 0.01m / cash 0.03m / empty 70-60/61-62),{ENT},Erfgoed Rupelstreek / 5 Rupelstreek cities,WVV projectvereniging; NBB neerlegging; 5 Rupelstreek gemeenten,2026-03-23,2009,,10959,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00079897.pdf,Local leftover IGS map VL Rupelstreek erfgoed — 0.01m negative brutomarge / empty 70/60/61/62 / PnL -0.01m,Publish empty 70/60/61/62 split + cash drop + vennoten share-pct; do not keep leftover Rupelstreek as dual unpublished vehicle,{SRC},strong,Vlaanderen>Antwerpen>Rupelstreek>ErfgoedRupelstreek>JR2025_L5,tick1431; assets 58035 omzet empty diensten empty pers empty pnl -10998 equity 58035 cash 31653 debt 0 capex 0 dividend 0; FOI ready not sent; not TE-additive of 348bn",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"lb_rpsk_omzet_empty_bruto_neg_cash_drop,Erfgoed Rupelstreek JR2025 leftover IGS: negative brutomarge 0.01m / empty 70-60/61-62 / cash 0.03m,L5,local_budget_line,Vlaanderen>Antwerpen>Rupelstreek>ErfgoedRupelstreek>JR2025_L5,10959,58035,Leftover dual IGS: assets 0.06m / equity 0.06m / pnl -0.01m / omzet empty / diensten empty / pers empty / cash 0.03m DROP / debt 0 / dividend 0,strong,{SRC},Erfgoed Rupelstreek / 5 Rupelstreek cities,Local leftover IGS map VL Rupelstreek erfgoed — JR2025 live; dual empty 70/60/61/62 FOI,Official NBB WVV 2026-08-19: brutomarge -0.01m / cash 0.03m / PnL -0.01m,6.6,3.2,2.0,4.8,Publish empty 70/60/61/62 split + cash drop + vennoten share-pct; do not keep leftover Rupelstreek as dual unpublished vehicle,active,,tick1431; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Antwerpen>Rupelstreek>ErfgoedRupelstreek>JR2025_L5,{ENT},omzet 70 empty + 60/61 empty + pers 62 empty / VTE unpublished + cash DROP 31653 vs 38681 + EV DROP 58035 vs 69033 + continuity two loss years + vennoten share-pct unpublished + commissaris unpublished,Leftover Rupelstreek IGS after leftover AGB hunt: 0.01m negative brutomarge / empty 70/60/61/62 hides public-perimeter IOED vehicle,8,Erfgoed Rupelstreek / Raad van Bestuur,info@erfgoedrupelstreek.be,Hoogstraat 27 2850 Boom / zetel Schommelei 1 Provinciaal Domein De Schorre,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_rpsk_jr2025_bruto,lb_rpsk_omzet_empty_bruto_neg_cash_drop,{TS},{TS},tick1431 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV MIC-inb PDF now extracted (40153 bytes 10p deposit 2026-00079897). FOI ready not sent. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. RL Schelde-Durme VZW 0889.859.093 JR2025 CDN 2026-00106166 LIVE leftover for next.",
])
print("foi_queue +1")

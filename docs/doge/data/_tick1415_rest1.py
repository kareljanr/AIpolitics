#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
TS = "2026-08-19T10:50:00Z"
ENT = "igs_westhoek_dv"
SRC = "src_whdv_jr2025_nbb"
GAP = "gap_whdv_omzet_empty_pers_2_65m_recv_0_54m_l5"
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
append_lf(DATA / "commitments.csv", [
    f"comm_whdv_jr2025_pnl,DVV Westhoek JR2025 leftover IGS dual (assets 3.15m / brutomarge 2.86m / pers 2.65m / cash 1.86m / debt 1.16m / PnL 0.10m),{ENT},DVV Westhoek / 17 Westhoek gemeenten + WVI,WVV IGS; NBB neerlegging; Bestuursdecreet via 17 gemeenten + WVI,2026-06-23,2017,,2859900,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00300232.pdf,Local leftover IGS map VL Westhoek — 2.86m brutomarge / 2.65m pers / 1.86m cash / 1.16m debt / PnL 0.10m,Publish omzet 70 + diensten 60/61 split + other recv 0.54m counterpart + other ST 0.22m counterpart; do not keep leftover DVV Westhoek as dual unpublished vehicle,{SRC},strong,Vlaanderen>West-Vlaanderen>Westhoek>DVV_Westhoek>JR2025_L5,tick1415; assets 3145801 brutomarge 2859900 omzet empty pnl 101860 equity 1987351 cash 1859774 debt 1158449 pers 2648974 capex 17881 dividend 0; FOI ready not sent; not TE-additive of 348bn",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"lb_whdv_omzet_empty_pers_2_65m_cash_1_86m,DVV Westhoek JR2025 leftover IGS: assets 3.15m / brutomarge 2.86m / pers 2.65m / cash 1.86m,L5,local_budget_line,Vlaanderen>West-Vlaanderen>Westhoek>DVV_Westhoek>JR2025_L5,2859900,3145801,Leftover dual IGS: assets 3.15m / equity 1.99m / pnl 0.10m / omzet empty / pers 2.65m / cash 1.86m / debt 1.16m / expl drop vs 0.92m / dividend 0,strong,{SRC},DVV Westhoek / 17 Westhoek gemeenten + WVI,Local leftover IGS map VL Westhoek — JR2025 live; dual omzet/pers/recv FOI,Official NBB WVV 2026-08-19: assets 3.15m / brutomarge 2.86m / pers 2.65m / cash 1.86m,6.4,4.2,2.0,5.3,Publish omzet 70 + diensten 60/61 split + other recv 0.54m counterpart + other ST 0.22m counterpart; do not keep leftover DVV Westhoek as dual unpublished vehicle,active,,tick1415; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined IVVO 1345 / WVI 1346 / Aquaduin 1349 / AGB De Kluize 1414",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>West-Vlaanderen>Westhoek>DVV_Westhoek>JR2025_L5,{ENT},omzet 70 empty + 60/61 diensten empty + overige vorderingen 539225 JUMP counterpart unpublished + geldbeleggingen 500000 counterpart unpublished + overige ST 223780 counterpart unpublished + deferred 370952 JUMP counterpart unpublished + expl drop 81814 vs 917226 unpublished,Leftover IGS after leftover AGB hunt: 3.15m assets / 2.86m brutomarge hides public-perimeter regional-staff / project vehicle,8,DVV Westhoek / Raad van Bestuur,info@dvvwesthoek.be,Grote Markt 6 8600 Diksmuide,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_whdv_jr2025_pnl,lb_whdv_omzet_empty_pers_2_65m_cash_1_86m,{TS},{TS},tick1415 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV VKT-inb PDF now extracted (786056 bytes 27p deposit 2026-00300232). FOI ready not sent. IVAREM still JR2024. Dommelhof leftover EVA no jaarrekening.",
])
print("foi_queue +1")

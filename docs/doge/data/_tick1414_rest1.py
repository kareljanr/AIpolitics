#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
TS = "2026-08-19T09:10:00Z"
ENT = "agb_de_kluize_oosterzele"
SRC = "src_kluz_jr2025_nbb"
GAP = "gap_kluz_omzet_empty_lease_4_48m_debt_5_76m_l5"
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
append_lf(DATA / "commitments.csv", [
    f"comm_kluz_jr2025_pnl,AGB De Kluize JR2025 leftover AGB dual (assets 5.83m / brutomarge 0.34m / lease 4.48m / debt 5.76m / PnL 0.07m),{ENT},AGB De Kluize / Gemeente Oosterzele,WVV AGB; NBB neerlegging; Bestuursdecreet via gemeente 100pct,2026-05-11,2011,,342519,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00286795.pdf,Local leftover AGB map VL Oosterzele sport/GC/erfgoed/jeugd — 0.34m brutomarge / 4.48m lease / 5.76m debt / PnL 0.07m,Publish omzet 70 + diensten 60/61 split + pers + lease/loan counterparts + commissaris fee; do not keep leftover AGB De Kluize as dual unpublished vehicle,{SRC},strong,Vlaanderen>Oost-Vlaanderen>Oosterzele>AGB_De_Kluize>JR2025_L5,tick1414; assets 5831290 brutomarge 342519 omzet empty pnl 73538 equity 69529 cash 724091 debt 5761761 lease 4483958 capex 87700 dividend 50000; FOI ready not sent; not TE-additive of 348bn",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"lb_kluz_omzet_empty_lease_4_48m_debt_5_76m,AGB De Kluize JR2025 leftover AGB: assets 5.83m / brutomarge 0.34m / lease 4.48m / debt 5.76m,L5,local_budget_line,Vlaanderen>Oost-Vlaanderen>Oosterzele>AGB_De_Kluize>JR2025_L5,342519,5831290,Leftover dual AGB: assets 5.83m / equity 0.07m thin / pnl 0.07m / omzet empty / lease 4.48m / cash 0.72m JUMP / debt 5.76m / fin cost 0 / dividend 0.05m,strong,{SRC},AGB De Kluize / Gemeente Oosterzele,Local leftover AGB map VL Oosterzele — JR2025 live; dual omzet/lease/debt FOI,Official NBB WVV 2026-08-19: assets 5.83m / brutomarge 0.34m / lease 4.48m / debt 5.76m,6.6,4.4,2.0,5.5,Publish omzet 70 + diensten 60/61 split + pers + lease/loan counterparts + commissaris fee; do not keep leftover AGB De Kluize as dual unpublished vehicle,active,,tick1414; leftover AGB after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Oost-Vlaanderen>Oosterzele>AGB_De_Kluize>JR2025_L5,{ENT},omzet 70 empty + 60/61 diensten empty + pers 62 empty + leasing 4483958 / LT lease 4932885 counterpart unpublished + overige leningen 384447 counterpart unpublished + overige ST 64512 JUMP counterpart unpublished + commissaris fee unpublished (6.6 not filed) + fin kosten 0 bij 5.32m LT,Leftover AGB after leftover AGB hunt: 5.83m assets / 0.34m brutomarge hides public-perimeter sport/GC/erfgoed vehicle,8,AGB De Kluize / Raad van Bestuur / voorzitter Mia Waterloos,david.delandsheere@oosterzele.be,Sportstraat 3 9860 Oosterzele,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_kluz_jr2025_pnl,lb_kluz_omzet_empty_lease_4_48m_debt_5_76m,{TS},{TS},tick1414 leftover AGB after honest leftover AGB hunt; live JR2025 official NBB WVV VKT-kap PDF now extracted (260838 bytes 17p deposit 2026-00286795). FOI ready not sent. IVAREM still JR2024. Dommelhof leftover EVA no jaarrekening. Bornem still 2024. Hulshout still 2022.",
])
print("foi_queue +1")

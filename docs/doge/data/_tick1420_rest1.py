#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
TS = "2026-08-19T09:55:00Z"
ENT = "igs_co7"
SRC = "src_co7_jr2025_nbb"
GAP = "gap_co7_omzet_0_90m_diensten_0_90m_prepaid_0_12m_l5"
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
append_lf(DATA / "commitments.csv", [
    f"comm_co7_jr2025_pnl,CultuurOverleg Zeven / CO7 JR2025 leftover IGS dual (assets 0.69m / omzet 0.90m / diensten 0.90m / cash 0.55m / debt 0.30m / PnL -7.1k),{ENT},CO7 / 7 Zuidelijke Westhoek gemeenten,WVV IGS; NBB neerlegging; Bestuursdecreet via 7 gemeenten,2026-03-26,2005,,899440,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00080644.pdf,Local leftover IGS map VL Zuidelijke Westhoek — 0.90m omzet / 0.90m diensten / 0.55m cash / 0.30m debt / PnL -7.1k,Publish 6.10 omzet category + diensten 60/61 split + prepaid 0.12m counterpart + leveranciers 0.28m counterpart; do not keep leftover CO7 as dual unpublished vehicle,{SRC},strong,Vlaanderen>West-Vlaanderen>Westhoek>CO7>JR2025_L5,tick1420; assets 691225 omzet 899440 diensten 900356 pers empty pnl -7140 equity 393922 cash 552517 debt 297303 capex 17712 dividend 0; FOI ready not sent; not TE-additive of 348bn; EVERY-10",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"lb_co7_omzet_0_90m_diensten_0_90m_cash_0_55m,CO7 JR2025 leftover IGS: assets 0.69m / omzet 0.90m / diensten 0.90m / cash 0.55m,L5,local_budget_line,Vlaanderen>West-Vlaanderen>Westhoek>CO7>JR2025_L5,899440,691225,Leftover dual IGS: assets 0.69m / equity 0.39m / pnl -7.1k / omzet 0.90m / diensten 0.90m unpublished split / pers empty / cash 0.55m / debt 0.30m / prepaid 0.12m / brutomarge NEG / dividend 0,strong,{SRC},CO7 / 7 Zuidelijke Westhoek gemeenten,Local leftover IGS map VL Zuidelijke Westhoek — JR2025 live; dual omzet/diensten/prepaid FOI,Official NBB WVV 2026-08-19: assets 0.69m / omzet 0.90m / diensten 0.90m / cash 0.55m,6.6,3.5,2.0,5.0,Publish 6.10 omzet category + diensten 60/61 split + prepaid 0.12m counterpart + leveranciers 0.28m counterpart; do not keep leftover CO7 as dual unpublished vehicle,active,,tick1420; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined DVV Westhoek 1415 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>West-Vlaanderen>Westhoek>CO7>JR2025_L5,{ENT},omzet 70 filled 899440 but 6.10 category/geo not filed + 60/61 diensten 900356 unpublished as a split + pers 62 empty / VTE unpublished + prepaid 119499 JUMP counterpart unpublished + leveranciers 284516 counterpart unpublished + brutomarge NEG -917 / expl -8979 unpublished,Leftover IGS after leftover AGB hunt: 0.69m assets / 0.90m omzet hides public-perimeter cultuur/erfgoed vehicle,8,CultuurOverleg Zeven / Raad van Bestuur,info@co7.be,Grote Markt 1 8970 Poperinge,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_co7_jr2025_pnl,lb_co7_omzet_0_90m_diensten_0_90m_cash_0_55m,{TS},{TS},tick1420 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV MIC-inb PDF now extracted (43209 bytes 11p deposit 2026-00080644). FOI ready not sent. EVERY-10. IVAREM still JR2024. Dommelhof leftover EVA no jaarrekening.",
])
print("foi_queue +1")

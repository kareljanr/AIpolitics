#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
TS = "2026-08-19T10:05:00Z"
ENT = "igs_vtrt"
SRC = "src_vtrt_jr2025_nbb"
GAP = "gap_vtrt_omzet_empty_pers_0_08m_cash_0_19m_l5"
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
append_lf(DATA / "commitments.csv", [
    f"comm_vtrt_jr2025_pnl,Viertoren JR2025 leftover IGS dual (assets 0.21m / brutomarge 0.11m / pers 0.08m / cash 0.19m / debt 8.8k / PnL +30.7k),{ENT},Viertoren / 4 Westhoek kust gemeenten,WVV IGS; NBB neerlegging; Bestuursdecreet via 4 gemeenten,2026-03-31,2019,,110397,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00070101.pdf,Local leftover IGS map VL Westhoek kust — 0.11m brutomarge / 0.08m pers / 0.19m cash / 8.8k debt / PnL +30.7k,Publish omzet 70 + diensten 60/61 split + pers VTE + other recv 0.02m counterpart + cash drop; do not keep leftover Viertoren as dual unpublished vehicle,{SRC},strong,Vlaanderen>West-Vlaanderen>Westhoek>Viertoren>JR2025_L5,tick1421; assets 211378 brutomarge 110397 omzet empty diensten empty pers 79534 pnl 30657 equity 202586 cash 189139 debt 8791 capex 0 dividend 0; FOI ready not sent; not TE-additive of 348bn",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"lb_vtrt_brutomarge_0_11m_cash_0_19m,Viertoren JR2025 leftover IGS: assets 0.21m / brutomarge 0.11m / pers 0.08m / cash 0.19m,L5,local_budget_line,Vlaanderen>West-Vlaanderen>Westhoek>Viertoren>JR2025_L5,110397,211378,Leftover dual IGS: assets 0.21m / equity 0.20m / pnl +30.7k / omzet empty / diensten unpublished split / pers 0.08m VTE unpublished / cash 0.19m DROP / debt 8.8k / other recv 0.02m / dividend 0,strong,{SRC},Viertoren / 4 Westhoek kust gemeenten,Local leftover IGS map VL Westhoek kust — JR2025 live; dual omzet/diensten/VTE FOI,Official NBB WVV 2026-08-19: assets 0.21m / brutomarge 0.11m / pers 0.08m / cash 0.19m,6.4,3.2,2.0,4.8,Publish omzet 70 + diensten 60/61 split + pers VTE + other recv 0.02m counterpart + cash drop; do not keep leftover Viertoren as dual unpublished vehicle,active,,tick1421; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined CO7 1420 / DVV Westhoek 1415 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>West-Vlaanderen>Westhoek>Viertoren>JR2025_L5,{ENT},omzet 70 empty + 60/61 diensten empty unpublished as a split + pers 62 filed 79534 / VTE unpublished MIC-inb 6.2 not filed + overige vorderingen 22238 counterpart unpublished + cash 189139 DROP vs 229857 unpublished + leveranciers 47 / soc 8744 split unpublished,Leftover IGS after leftover AGB hunt: 0.21m assets / 0.11m brutomarge hides public-perimeter cultuur/bibliotheek vehicle,8,Viertoren / Raad van Bestuur,info@viertoren.be,Zeelaan 303 8670 Koksijde,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_vtrt_jr2025_pnl,lb_vtrt_brutomarge_0_11m_cash_0_19m,{TS},{TS},tick1421 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV MIC-inb PDF now extracted (41364 bytes 10p deposit 2026-00070101). FOI ready not sent. IVAREM still JR2024. Dijk92 still JR2024. Dommelhof leftover EVA no jaarrekening.",
])
print("foi_queue +1")

#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
TS = "2026-08-19T08:45:00Z"
ENT = "nv_pmbs"
SRC = "src_pmbs_jr2025_nbb"
GAP = "gap_pmbs_omzet_0_11m_diensten_0_11m_vrucht_l5"
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
append_lf(DATA / "commitments.csv", [
    f"comm_pmbs_jr2025_pnl,PATRIMONIUM MBS JR2025 leftover IOK-daughter dual (assets 1.60m / omzet 0.11m / diensten 0.11m / PnL 0.001m),{ENT},PATRIMONIUM MBS / IOK Afvalbeheer 60pct / IVAREM 40pct,WVV NV; NBB neerlegging; Bestuursdecreet via IOK/IVAREM public-perimeter share,2026-05-08,2007,,107101,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00136170.pdf,Local leftover IOK daughter map VL Kempen MBS patrimonium — 0.11m omzet / 0.11m diensten / vruchtgebruik Maatschap MBS / PnL 0.001m,Publish 6.10 omzet category/geo + diensten 0.11m split + vruchtgebruik counterpart + other recv/debt counterparts + searchable commissaris; do not keep leftover MBS patrimonium NV as dual unpublished vehicle,{SRC},strong,Vlaanderen>Antwerpen>Kempen>PATRIMONIUM_MBS>JR2025_L5,tick1413; assets 1600122 omzet 107101 diensten 112337 pnl 1072 equity 1599050 cash 528367 debt 1072 capex 0 dividend 1072; FOI ready not sent; not TE-additive of 348bn",
])
print("commitments +1")
append_lf(DATA / "leaderboard.csv", [
    f"lb_pmbs_omzet_0_11m_diensten_0_11m_vrucht,PATRIMONIUM MBS JR2025 leftover IOK daughter: assets 1.60m / omzet 0.11m / diensten 0.11m / vruchtgebruik,L5,local_budget_line,Vlaanderen>Antwerpen>Kempen>PATRIMONIUM_MBS>JR2025_L5,107101,1600122,Leftover dual IOK daughter NV: assets 1.60m / equity 1.60m / pnl 0.001m / omzet 0.11m 6.10 empty / diensten 0.11m / cash 0.53m / debt 0.001m / MVA naakt 1.06m of 42.33m aanschaf,strong,{SRC},PATRIMONIUM MBS / IOK Afvalbeheer / IVAREM,Local leftover IOK daughter map VL Kempen MBS — JR2025 live; dual omzet/diensten/vrucht FOI,Official NBB WVV 2026-08-19: assets 1.60m / omzet 0.11m / diensten 0.11m / pnl 0.001m,6.4,4.2,2.0,5.4,Publish 6.10 omzet category/geo + diensten 0.11m split + vruchtgebruik Maatschap MBS counterpart + other recv/debt counterparts + searchable commissaris; do not keep leftover MBS patrimonium NV as dual unpublished vehicle,active,,tick1413; leftover IOK daughter after leftover AGB/IGS hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined IOK Afvalbeheer 1412 / IOK DV 1368 / AGB Merchtem 1411",
])
print("leaderboard +1")
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Antwerpen>Kempen>PATRIMONIUM_MBS>JR2025_L5,{ENT},omzet 70 filled 107101 but 6.10 category/geo empty + diensten 112337 split unpublished + overige vorderingen 9143 counterpart unpublished + overige schulden 750 counterpart unpublished + vruchtgebruik Maatschap MBS omzet counterpart unpublished + commissarisverslag VOL-kap 8 image-only,Leftover IOK daughter after leftover AGB/IGS hunt: 1.60m assets / 0.11m omzet / 0.11m diensten hides public-perimeter MBS patrimonium vehicle,8,PATRIMONIUM MBS / Raad van Bestuur / voorzitters Eduardus Ward Kennes + Ivan Blauwhoff,info@iok.be,Antwerpseweg 1 2440 Geel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_pmbs_jr2025_pnl,lb_pmbs_omzet_0_11m_diensten_0_11m_vrucht,{TS},{TS},tick1413 leftover IOK daughter after honest leftover AGB/IGS hunt; live JR2025 official NBB WVV VOL-kap PDF now extracted (1814120 bytes 41p deposit 2026-00136170). FOI ready not sent. IVAREM still JR2024. Dommelhof leftover EVA no jaarrekening. Leftover AGB already mined or still 2024.",
])
print("foi_queue +1")

#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
TS = "2026-08-19T08:10:00Z"
GAP = "gap_mrch_omzet_empty_recv_1_33m_debt_3_38m_l5"
LB = "lb_mrch_omzet_empty_recv_1_33m_debt_3_38m"
COMM = "comm_mrch_jr2025_pnl"
SRC = "src_mrch_jr2025_nbb"

def append_lf(path: Path, rows: list[str]) -> None:
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

append_lf(DATA / "commitments.csv", [
    f"{COMM},AGB Merchtem JR2025 leftover AGB dual (assets 4.93m / brutomarge 0.31m / recv 1.33m / debt 3.38m / PnL 0.05m),agb_merchtem,AGB Merchtem / Gemeente Merchtem,WVV autonoom gemeentebedrijf; NBB neerlegging; Bestuursdecreet,2026-06-29,2009,,313807,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00317853.pdf,Local leftover AGB map VL Merchtem — 0.31m brutomarge / 1.33m recv / 3.38m debt / PnL 0.05m,Publish omzet 70 + diensten 60/61 split + recv 1.33m counterpart + LT loans 2.73m + pers + jaarverslag; do not keep leftover AGB as dual unpublished vehicle,{SRC},strong,Vlaanderen>Vlaams-Brabant>Merchtem>AGB>JR2025_L5,tick1411; assets 4925278 brutomarge 313807 omzet empty diensten empty pers empty pnl 46516 equity 1413160 cash 57860 debt 3382104 recv 1328425 capex 48876 dividend 25000; FOI ready not sent; not TE-additive of 348bn",
])
append_lf(DATA / "leaderboard.csv", [
    f"{LB},AGB Merchtem JR2025 leftover AGB: assets 4.93m / brutomarge 0.31m / recv 1.33m / debt 3.38m,L5,local_budget_line,Vlaanderen>Vlaams-Brabant>Merchtem>AGB>JR2025_L5,313807,4925278,Leftover dual AGB: assets 4.93m / equity 1.41m / pnl 0.05m / omzet empty / brutomarge 0.31m / recv 1.33m / debt 3.38m / cash 0.06m / dividend 0.03m,strong,{SRC},AGB Merchtem / Gemeente Merchtem,Local leftover AGB map VL Merchtem — JR2025 live; dual omzet/recv/debt FOI,Official NBB WVV 2026-08-19: assets 4.93m / brutomarge 0.31m / recv 1.33m / debt 3.38m / pnl 0.05m,6.2,5.2,2.0,5.7,Publish omzet 70 + diensten 60/61 split + recv 1.33m counterpart + LT loans 2.73m + pers + jaarverslag not filed; do not keep leftover AGB as dual unpublished vehicle,active,,tick1411; leftover AGB after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined AGB Tielt 1405 / AGB Patri 1407 / Sunfin 1410",
])
append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Vlaams-Brabant>Merchtem>AGB>JR2025_L5,agb_merchtem,omzet 70 empty + 60/61 empty so diensten unpublished as a split (only brutomarge 313807 published) + pers 62 empty / VTE unpublished + ST overige vorderingen 1328425 counterpart unpublished + LT overige leningen 2734894 counterpart unpublished + jaarverslag VKT-inb 7 not filed + commissarisverslag image-only,Leftover AGB of mined city Merchtem after leftover AGB hunt: 4.93m assets / omzet empty / 0.31m brutomarge / 1.33m recv / 3.38m debt hides sport-AGB turnover and city counterpart,8,AGB Merchtem / Raad van Bestuur / voorzitter David De Valck,financies@merchtem.be,Nieuwstraat 1 1785 Merchtem,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,{COMM},{LB},{TS},{TS},tick1411 leftover AGB after honest leftover AGB hunt; live JR2025 official NBB WVV VKT-inb PDF now extracted (264500 bytes 22p deposit 2026-00317853). FOI ready not sent. Tick 1313 unpublished gap superseded by sourced euros. IVAREM still JR2024. Dommelhof leftover EVA no jaarrekening. IOK Afvalbeheer CDN live leftover-next.",
])
print("commitments +1 leaderboard +1 foi_queue +1")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "igs_hvva"
SRC = "src_hvva_jr2025_bbc"
GAP = "gap_hvva_spend_11_00m_pers_7_24m_rekening_l5"
LB = "lb_hvva_spend_11_00m_pers_7_24m"
COMM = "comm_hvva_jr2025_spend"
PDF = "https://bvlar.be/wp-content/uploads/2026/03/BVLAR-Activiteitenverslag-2025.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def check(row, n, label):
    fields = next(csv.reader(io.StringIO(row)))
    got = len(fields)
    if got != n:
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:160]}")
    if any("," in f for f in fields):
        raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")

comm = (
    f"{COMM},BVLAR JR2025 leftover IGS dual (spend 11.00m / pers 7.24m / werking 3.34m / inkomsten 9.39m / invest 3.57m),{ENT},BVLAR / dual mined Oudenaarde + remaining Vlaamse Ardennen municipalities / municipal + federal civiele-veiligheid,Wet 15.05.2007 civiele veiligheid; KB boekhouding hulpverleningszones; Bestuursdecreet openbaarheid,2026-03-11,2025,2025,10999722,,,active,{PDF},Local leftover IGS fire-rescue map VL Oudenaarde BVLAR — spend 11.00m / pers 7.24m / unpublished full rekening balans,Publish full rekening 2025 verslag + balans + expl/PnL + VTE + gemeentelijke bijdragen split + cash/debt/equity + full BBC; do not keep leftover BVLAR unpublished,{SRC},strong,Vlaanderen>Gemeenten>Oudenaarde>IGS>HVZ_Vlaamse_Ardennen>JR2025_L5,tick1542; uitgaven_gewone 10999722 pers 7238089 werking 3339750 overdrachten 222609 schuld_uitg 199274 inkomsten 9390635 toelagen_gem 5751118 invest 3565917; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},BVLAR JR2025 leftover IGS: spend 11.00m / pers 7.24m / werking 3.34m / inkomsten 9.39m / unpublished full rekening balans,L5,local_budget_line,Vlaanderen>Gemeenten>Oudenaarde>IGS>HVZ_Vlaamse_Ardennen>JR2025_L5,10999722,10999722,Leftover dual IGS fire-rescue shell: spend 11.00m / pers 7.24m / werking 3.34m / overdrachten 0.22m / inkomsten 9.39m / toelagen gemeenten 5.75m / invest 3.57m / balans expl PnL VTE cash debt equity unpublished,strong,{SRC},BVLAR / dual mined Oudenaarde + remaining Vlaamse Ardennen municipalities / municipal + federal civiele-veiligheid,Local leftover IGS fire-rescue map VL Oudenaarde BVLAR — JR2025 official activiteitenverslag live; full rekening balans + pers/VTE + city-share FOI,Official AV2025 2026-08-20: spend 11.00m / pers 7.24m / inkomsten 9.39m / unpublished full rekening,7.0,7.0,3.0,6.2,Publish full rekening 2025 verslag + balans + expl/PnL + VTE + gemeentelijke bijdragen split 13 gemeenten + cash/debt/equity + full BBC; do not keep leftover BVLAR unpublished,active,,tick1542; leftover IGS hulpverleningszone of mined Oudenaarde after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Kempen / leftover HVZ Waasland / leftover HVZ Fluvia / leftover Brandweerzone Centrum / leftover CAW Oost-Vlaanderen 1532 / leftover CGG Adentro 1511 / leftover Thuispunt Gent 1470 / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Oudenaarde>IGS>HVZ_Vlaamse_Ardennen>JR2025_L5,{ENT},Official AV2025 publishes uitgaven gewone 10999722 / pers 7238089 / werking 3339750 / overdrachten 222609 / schuld 199274 / inkomsten 9390635 / toelagen gem 5751118 / invest 3565917; full rekening 2025 verslag + balans + expl/PnL unpublished; VTE unpublished; gemeentelijke bijdragen split unpublished; cash/debt/equity unpublished; dual municipal + federal civiele-veiligheid split unpublished,Leftover IGS hulpverleningszone of mined Oudenaarde with live official AV2025; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; spend 11.00m / pers 7.24m / unpublished full rekening,8,Brandweerzone Vlaamse Ardennen / dienst openbaarheid,administratie@bvlar.be,Bedrijvenpark Coupure 21 9700 Oudenaarde,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1542 leftover IGS hulpverleningszone after honest leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished so leftover IGS with live official AV2025 taken; official AV PDF. FOI ready not sent. NOT leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Kempen / leftover HVZ Waasland / leftover HVZ Fluvia / leftover Brandweerzone Centrum / leftover CAW Oost-Vlaanderen 1532 / leftover CGG Adentro 1511 / leftover Thuispunt Gent 1470 / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
foi_path = DATA / "foi_queue.csv"
before = foi_path.stat().st_size
append_lf(foi_path, [foi])
after = foi_path.stat().st_size
if after < before:
    raise SystemExit(f"foi_queue shrank {before} -> {after}")
print("foi_queue +1 append-only", before, "->", after)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "igs_hvzm"
SRC = "src_hvzm_jr2025_bbc"
GAP = "gap_hvzm_assets_4_11m_expl_258k_rekening_l5"
LB = "lb_hvzm_assets_4_11m_expl_258k_pnl_285k"
COMM = "comm_hvzm_jr2025_assets"
PDF = "https://www.maldegem.be/file/download/80b29791-d19b-4e15-8040-df30f6b2a3de/3GyCecLpP8KnwZad0NCw3WW9QL04GEbFvqjxhQ9RJqI3d.pdf"

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
    f"{COMM},HVZ Meetjesland JR2025 leftover IGS dual (assets 4.11m / expl 0.26m / PnL PROFIT 0.28m / uitz 27k / equity 3.16m / debt 0.96m / vastgelegd gewone 6.33m),{ENT},HVZ Meetjesland / dual mined Eeklo + remaining Meetjesland municipalities / municipal + federal civiele-veiligheid,Wet 15.05.2007 civiele veiligheid; KB 19.04.2014 boekhouding hulpverleningszones (as printed); Bestuursdecreet openbaarheid,2026-03-18,1970,,4113934,,,active,{PDF},Local leftover IGS fire-rescue map VL Eeklo HVZ Meetjesland — assets 4.11m / expl 0.26m / PnL PROFIT 0.28m / unpublished full rekening bijlage,Publish full rekening 2025 bijlage + pers/VTE + gemeentelijke bijdragen split + cash/omzet + full BBC; do not keep leftover HVZ Meetjesland unpublished,{SRC},strong,Vlaanderen>Gemeenten>Eeklo>IGS>HVZ_Meetjesland>JR2025_L5,tick1540; assets 4113934 expl 258096 pnl 284889 uitz 26793 equity 3158074 debt 955860 vastgelegd_gewone 6332064; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED still unpublished; EVERY-10"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},HVZ Meetjesland JR2025 leftover IGS: assets 4.11m / expl 0.26m / PnL PROFIT 0.28m / equity 3.16m / debt 0.96m / unpublished full rekening bijlage,L5,local_budget_line,Vlaanderen>Gemeenten>Eeklo>IGS>HVZ_Meetjesland>JR2025_L5,4113934,4113934,Leftover dual IGS fire-rescue shell: assets 4.11m / expl 0.26m / PnL PROFIT 0.28m / uitz 27k / equity 3.16m / debt 0.96m / vastgelegd gewone 6.33m / pers VTE cash omzet unpublished,strong,{SRC},HVZ Meetjesland / dual mined Eeklo + remaining Meetjesland municipalities / municipal + federal civiele-veiligheid,Local leftover IGS fire-rescue map VL Eeklo HVZ Meetjesland — JR2025 official zoneraad live; full rekening bijlage + pers/VTE + city-share FOI,Official zoneraad 2026-08-20: assets 4.11m / expl 0.26m / PnL PROFIT 0.28m / equity 3.16m / unpublished full rekening,7.0,6.8,3.0,6.2,Publish full rekening 2025 bijlage + pers/VTE + gemeentelijke bijdragen split Meetjesland municipalities + cash/omzet + full BBC; do not keep leftover HVZ Meetjesland unpublished,active,,tick1540; leftover IGS hulpverleningszone of mined Eeklo after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Kempen / leftover WM Meetjesland 1496 / leftover RL Meetjesland 1443 / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Eeklo>IGS>HVZ_Meetjesland>JR2025_L5,{ENT},Zoneraad uittreksel publish assets 4113934 / expl 258096 / PnL PROFIT 284889 / uitz 26793 / equity 3158074 / debt 955860; full rekening 2025 bijlage unpublished; pers/VTE unpublished; gemeentelijke bijdragen split unpublished; cash/omzet/uitgaven gewone unpublished; dual municipal + federal civiele-veiligheid split unpublished,Leftover IGS hulpverleningszone of mined Eeklo with live official JR2025 uittreksel; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; assets 4.11m / expl 0.26m / PnL PROFIT 0.28m / unpublished full rekening,8,Hulpverleningszone Meetjesland / dienst openbaarheid,communicatie@zonemeetjesland.be,Gentsesteenweg 2 9900 Eeklo,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1540 leftover IGS hulpverleningszone after honest leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished so leftover IGS with live official JR2025 uittreksel taken; official zoneraad PDF. FOI ready not sent. EVERY-10. NOT leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Kempen / leftover WM Meetjesland 1496 / leftover RL Meetjesland 1443 / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
# APPEND ONLY — never rewrite foi_queue
foi_path = DATA / "foi_queue.csv"
before = foi_path.stat().st_size
append_lf(foi_path, [foi])
after = foi_path.stat().st_size
if after < before:
    raise SystemExit(f"foi_queue shrank {before} -> {after}")
print("foi_queue +1 append-only", before, "->", after)

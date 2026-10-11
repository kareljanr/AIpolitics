#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "igs_hvzk"
SRC = "src_hvzk_jr2025_bbc"
GAP = "gap_hvzk_spend_16_75m_pers_13_74m_rekening_l5"
LB = "lb_hvzk_spend_16_75m_pers_13_74m"
COMM = "comm_hvzk_jr2025_spend"
PDF = "https://kempen.hulpverleningszone.be/storage/JZ16ya31sYaCcDTQxcDSHeoq5zcxR3VW7GlychOl.pdf"

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
    f"{COMM},HVZ Kempen JR2025 leftover IGS dual (spend 16.75m / pers 13.74m / werking 3.01m / beschikbaar 18.99m / gem 9.71m / invest 2.51m),{ENT},HVZ Kempen / dual mined Geel + remaining Kempen municipalities / municipal + federal civiele-veiligheid,Wet 15.05.2007 civiele veiligheid; KB boekhouding hulpverleningszones; Bestuursdecreet openbaarheid,2026-05-05,2025,2025,16747636,,,active,{PDF},Local leftover IGS fire-rescue map VL Geel HVZ Kempen — spend 16.75m / pers 13.74m / unpublished full rekening balans,Publish full rekening 2025 verslag + balans + expl/PnL + VTE + bijkomende federal exact + andere-remainder + cash/debt/equity + full BBC; do not keep leftover HVZ Kempen unpublished,{SRC},strong,Vlaanderen>Gemeenten>Geel>IGS>HVZ_Kempen>JR2025_L5,tick1543; uitgaven_gewone 16747636 pers 13742087 werking 3005549 beschikbaar 18986967 gem_totaal 9713805 fed 4394794 invest 2506646; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},HVZ Kempen JR2025 leftover IGS: spend 16.75m / pers 13.74m / werking 3.01m / beschikbaar 18.99m / unpublished full rekening balans,L5,local_budget_line,Vlaanderen>Gemeenten>Geel>IGS>HVZ_Kempen>JR2025_L5,16747636,16747636,Leftover dual IGS fire-rescue shell: spend 16.75m / pers 13.74m / werking 3.01m / beschikbaar 18.99m / gem 9.71m / fed 4.39m / DGH 2.42m / invest 2.51m / balans expl PnL VTE cash debt equity unpublished,strong,{SRC},HVZ Kempen / dual mined Geel + remaining Kempen municipalities / municipal + federal civiele-veiligheid,Local leftover IGS fire-rescue map VL Geel HVZ Kempen — JR2025 official activiteitenrapport live; full rekening balans + pers/VTE FOI,Official AV2025 2026-08-20: spend 16.75m / pers 13.74m / beschikbaar 18.99m / unpublished full rekening,7.2,7.5,3.0,6.4,Publish full rekening 2025 verslag + balans + expl/PnL + VTE + bijkomende federal exact + andere-remainder + cash/debt/equity + full BBC; do not keep leftover HVZ Kempen unpublished,active,,tick1543; leftover IGS hulpverleningszone of mined Geel after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover HVZ Taxandria 1538 / leftover CAW De Kempen 1526 / leftover CGG Kempen 1516 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover HVZ Fluvia / leftover Brandweerzone Centrum / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Geel>IGS>HVZ_Kempen>JR2025_L5,{ENT},Official AV2025 publishes uitgaven gewone 16747636 / pers 13742087 / werking 3005549 / beschikbaar 18986967 / gem 9713805 / fed 4394794 / DGH 2421103 / invest 2506646; full rekening 2025 verslag + balans + expl/PnL unpublished; VTE unpublished; bijkomende federal text OCR-garbled; andere remainder unpublished; cash/debt/equity unpublished; dual municipal + federal civiele-veiligheid split unpublished,Leftover IGS hulpverleningszone of mined Geel with live official AV2025; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; spend 16.75m / pers 13.74m / unpublished full rekening,8,Brandweer Zone Kempen / dienst openbaarheid,info@brandweerzonekempen.be,Stelenseweg 92 2440 Geel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1543 leftover IGS hulpverleningszone after honest leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished so leftover IGS with live official AV2025 taken; official AV PDF. FOI ready not sent. NOT leftover HVZ Taxandria 1538 / leftover CAW De Kempen 1526 / leftover CGG Kempen 1516 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover HVZ Fluvia / leftover Brandweerzone Centrum / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
foi_path = DATA / "foi_queue.csv"
before = foi_path.stat().st_size
append_lf(foi_path, [foi])
after = foi_path.stat().st_size
if after < before:
    raise SystemExit(f"foi_queue shrank {before} -> {after}")
print("foi_queue +1 append-only", before, "->", after)

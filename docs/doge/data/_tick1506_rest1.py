#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T02:20:00Z"
ENT = "zorg_wvbl"
SRC = "src_wvbl_kbo_1013719482"
GAP = "gap_wvbl_jr2025_unpublished_l5"
LB = "lb_wvbl_jr2025_unpublished"
COMM = "comm_wvbl_jr2025_unpublished"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = [r.rstrip("\r\n") + "\r\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def check(row, n, label):
    got = len(next(csv.reader(io.StringIO(row))))
    if got != n:
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:160]}")

comm = (
    f"{COMM},Welzijnsvereniging Blankenberge JR2025 unpublished (FOI-ready),{ENT},Ouderen / dagverzorging / LDC De Bollaard / mogelijke kribbe Blankenberge,Decreet lokaal bestuur welzijnsvereniging; BBC; Bestuursdecreet openbaarheid,2024-06-25,2024,2028,,,,unknown,https://www.motena.be/blog/welzijnsvereniging-blankenberge-officieel-van-start,Local leftover zorg map VL Blankenberge — BBC/NBB extract missing,Publish BBC J1-J5/T2-T5 + RVB/GR/AV + NBB or non-filing + dual city/OCMW / VTE + zorgsite envelope,{SRC},medium,Vlaanderen>Gemeenten>Blankenberge>WV_Blankenberge>JR2025_L5,tick1506; no sourced euros; no fetchable BBC/NBB PDF; FOI ready not sent; not TE-additive of 348bn"
)
check(comm, 19, "commitments")
append_crlf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},Welzijnsvereniging Blankenberge JR2025 unpublished (no official 2025 PDF),L5,local_budget_line,Vlaanderen>Gemeenten>Blankenberge>WV_Blankenberge>JR2025_L5,,,No primary JR2025 BBC/NBB euros; KBO 1013.719.482 Actief no financials; do not use Belscope/Companyweb/Busibee or KW press 34m,medium,{SRC},Ouderen / dagverzorging / LDC De Bollaard / mogelijke kribbe Blankenberge,Local leftover zorg map VL Blankenberge — BBC PDF unpublished,KBO 1013.719.482 active; 2026-08-20 no fetchable JR2025 PDF bytes; TSV 24139864 image-only; Motena start page no euros,6.0,2.0,2.0,5.0,Publish BBC J1-J5/T2-T5 + RVB/GR/AV + NBB or non-filing + dual city/OCMW / VTE + zorgsite envelope,active,,tick1506; no invented euros; FOI ready not sent; leftover zorg of mined Blankenberge; not TE-additive of 348bn"
)
check(lb, 21, "leaderboard")
append_crlf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Blankenberge>WV_Blankenberge>JR2025_L5,{ENT},BBC jaarrekening 2025 welzijnsvereniging Blankenberge (J1-J5 / T2-T5 / BBR / AFM / fin debt / city-OCMW dotaties / zorgsite envelope / pers VTE) + WVV/NBB filing if any or gemotiveerde non-filing + RVB/GR/AV vaststelling,Leftover zorg of mined Blankenberge after leftover AGB/APB hunt: KBO 1013.719.482 Actief since 25.06.2024; no fetchable JR2025 BBC/NBB PDF; Motena+Stad zorgsite WZC 120 / dagverzorging 20-30 / target ~2028; press 34m not sourced,8,Welzijnsvereniging Blankenberge / Stad + OCMW Blankenberge,info@blankenberge.be,Frans Masereellaan 9 8370 Blankenberge,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1506 leftover zorg after honest leftover AGB/APB hunt; no live JR2025 official PDF. FOI ready not sent. NOT every-10 (next 1510). NOT leftover AGB Blankenberge 1323 / leftover Zetus 1490 / leftover Motena / leftover Vitare 1505 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck. Leftover APB Inovant/Atlas still 404. Leftover AGB Hoogstraten/Ravels/Rijkevorsel unused no AGB JR2025 PDF. Leftover Bosgroep still no JR. Leftover IGS IVAREM still JR2024. Leftover RL West-Vlaamse Hart still no jaarrekening. Leftover cultuur-IGS/IOED still no JR. Named leftover official-41 vein from 1464 fully exhausted."
)
check(foi, 21, "foi_queue")
append_crlf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

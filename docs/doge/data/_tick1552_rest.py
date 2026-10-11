#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1552 commitments / leaderboard / foi_queue. Surgical append only."""
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_vvsg"
SRC = "src_vvsg_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00217075.pdf"
GAP = "gap_vvsg_opbr_31_27m_pers_23_00m_accrued_jump_l5"
LB = "lb_vvsg_opbr_31_27m_pers_23_00m_accrued_jump"
COMM = "comm_vvsg_jr2025_opbr"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()

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
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:180]}")
    if any("," in f for f in fields):
        raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")

comm = (
    f"{COMM},VVSG JR2025 leftover public koepel dual (opbr 31.27m / subsid 27.76m / pers 23.00m 208.5 VTE / expl PROFIT 0.10m / PnL PROFIT 0.05m / assets 43.33m),{ENT},VVSG / dual mined Flemish cities / lokale besturen koepel,VZW-wet; Bestuursdecreet openbaarheid,2026-06-24,2025,2025,31266193,,,active,{PDF},Local leftover public koepel map VL cities VVSG — opbr 31.27m / subsid 27.76m / pers 23.00m / handelsrecv JUMP 9.69m / accrued JUMP 28.63m,Publish full AV notulen 24.06.2026 + 73 lidgeld/subsidy split + toelichting handelsrecv JUMP / accrued JUMP / cash DROP / other recv / commissaris extra 2.9k; do not keep leftover VVSG unpublished,{SRC},strong,Vlaanderen>Koepel>VVSG>JR2025_L5,tick1552; opbr 31266193 omzet 2672153 subsid 27759906 pers 22996957 vte 208.5 expl 103938 pnl 45220 assets 43332320 handelsrecv 9690908 JUMP accrued 28627254 JUMP cash 1857566 DROP commissaris 10204 extra 2863; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},VVSG JR2025 leftover public koepel: opbr 31.27m / subsid 27.76m / pers 23.00m 208.5 VTE / expl PROFIT 0.10m / PnL PROFIT 0.05m / assets 43.33m,L5,local_budget_line,Vlaanderen>Koepel>VVSG>JR2025_L5,31266193,43332320,Leftover dual public koepel shell: opbr 31.27m / omzet 2.67m / subsid 27.76m / pers 23.00m 208.5 VTE / expl PROFIT 0.10m / PnL PROFIT 0.05m / assets 43.33m / handelsrecv JUMP 9.69m / accrued JUMP 28.63m / cash DROP 1.86m / commissaris 10204 + extra 2863 / dividend n.a.,strong,{SRC},Vlaamse steden en gemeenten / lokale besturen,Local leftover public koepel map VL cities VVSG — official NBB VOL-VZW JR2025 live; 73 lidgeld/subsidy split FOI,Official NBB 2026-08-20: opbr 31.27m / pers 23.00m / subsid 27.76m / assets 43.33m,6.5,4.2,3.0,5.0,Publish full AV notulen 24.06.2026 + 73 lidgeld/subsidy split + toelichting handelsrecv JUMP / accrued JUMP / cash DROP / other recv / commissaris extra 2.9k; do not keep leftover VVSG unpublished,active,,tick1552; leftover public koepel VZW of mined Flemish cities after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover VVP / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Koepel>VVSG>JR2025_L5,{ENT},Official NBB VOL-VZW publishes opbr 31266193 / omzet 2672153 / subsid 27759906 / pers 22996957 208.5 VTE / expl PROFIT 103938 / PnL PROFIT 45220 / assets 43332320 / handelsrecv JUMP 9690908 / accrued JUMP 28627254 / cash DROP 1857566; 73 lidgeld 11067493 / subsidy 16692413 split unpublished; toelichting handelsrecv JUMP / accrued JUMP / cash DROP / other recv 16.89m unpublished; commissaris extra 2863 unpublished detail; AV notulen 24.06.2026 unpublished,Leftover public koepel VZW of mined Flemish cities with live official NBB JR2025 euros; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick; opbr 31.27m / pers 23.00m / subsid 27.76m,8,VVSG vzw / dienst openbaarheid,info@vvsg.be,Bischoffsheimlaan 1-8 1000 Brussel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1552 leftover public koepel after honest leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished so leftover public koepel with live official NBB JR2025 euros taken; official CDN PDF. FOI ready not sent. NOT leftover VVP / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand"
)
check(foi, 21, "foi_queue")
foi_path = DATA / "foi_queue.csv"
before = foi_path.stat().st_size
append_lf(foi_path, [foi])
after = foi_path.stat().st_size
if after < before:
    raise SystemExit(f"foi_queue shrank {before} -> {after}")
print("foi_queue +1 append-only", before, "->", after)
print("TS", TS)

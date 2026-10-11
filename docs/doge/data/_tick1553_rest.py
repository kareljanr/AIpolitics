#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1553 commitments / leaderboard / foi_queue. Surgical append only."""
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_vvp"
SRC = "src_vvp_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00138938.pdf"
GAP = "gap_vvp_bruto_0_59m_pers_0_56m_mva_jump_l5"
LB = "lb_vvp_bruto_0_59m_pers_0_56m_mva_jump"
COMM = "comm_vvp_jr2025_bruto"
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
    f"{COMM},VVP JR2025 leftover public koepel dual (bruto 0.59m / pers 0.56m 6.8 VTE / expl LOSS 6.2k / PnL LOSS 10.6k / assets 3.41m / MVA JUMP 0.58m),{ENT},VVP / dual mined Flemish provinces / provinciale besturen koepel,VZW-wet; Bestuursdecreet openbaarheid,2026-05-08,2025,2025,589640,,,active,{PDF},Local leftover public koepel map VL provinces VVP — bruto 0.59m / pers 0.56m / MVA JUMP 0.58m / cash DROP 2.26m,Publish full AV notulen 08.05.2026 + 73 lidgeld/subsidy split (VKT empty) + toelichting MVA JUMP / cash DROP / lev JUMP / 66A / zetel Groendreef 1; do not keep leftover VVP unpublished,{SRC},strong,Vlaanderen>Koepel>VVP>JR2025_L5,tick1553; bruto 589640 omzet empty 73 empty pers 558980 vte 6.8 expl -6198 pnl -10588 assets 3412677 mva 582447 JUMP cash 2256569 DROP lev 95590 JUMP commissaris 6888; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},VVP JR2025 leftover public koepel: bruto 0.59m / pers 0.56m 6.8 VTE / expl LOSS 6.2k / PnL LOSS 10.6k / assets 3.41m / MVA JUMP 0.58m,L5,local_budget_line,Vlaanderen>Koepel>VVP>JR2025_L5,589640,3412677,Leftover dual public koepel shell: bruto 0.59m / omzet empty / 73 empty / pers 0.56m 6.8 VTE / expl LOSS 6.2k / PnL LOSS 10.6k / assets 3.41m / MVA JUMP 0.58m / cash DROP 2.26m / lev JUMP 95.6k / commissaris 6888 / dividend n.a.,strong,{SRC},Vlaamse provincies / provinciale besturen,Local leftover public koepel map VL provinces VVP — official NBB VKT-VZW JR2025 live; 73/70/60/61 FOI,Official NBB 2026-08-20: bruto 0.59m / pers 0.56m / assets 3.41m / MVA JUMP 0.58m,6.2,3.4,3.0,4.6,Publish full AV notulen 08.05.2026 + 73 lidgeld/subsidy split (VKT empty) + toelichting MVA JUMP / cash DROP / lev JUMP / 66A / zetel Groendreef 1; do not keep leftover VVP unpublished,active,,tick1553; leftover public koepel VZW of mined Flemish provinces after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Koepel>VVP>JR2025_L5,{ENT},Official NBB VKT-VZW publishes bruto 589640 / omzet 70 empty / 73 empty / pers 558980 6.8 VTE / expl LOSS -6198 / PnL LOSS -10588 / assets 3412677 / MVA JUMP 582447 / cash DROP 2256569 / lev JUMP 95590; 73 lidgeld/subsidy unpublished (VKT); 60/61 unpublished; toelichting MVA JUMP gebouwen 142500 + in aanbouw 432014 unpublished; cash DROP / lev JUMP / LT DROP / fin DROP / 66A 17913 unpublished; commissaris 6888 no extra split; AV notulen 08.05.2026 unpublished; zetelwijziging Groendreef 1 unpublished,Leftover public koepel VZW of mined Flemish provinces with live official NBB JR2025 euros; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick; bruto 0.59m / pers 0.56m / MVA JUMP 0.58m,8,VVP vzw / dienst openbaarheid,info@vlaamseprovincies.be,Groendreef 1 1000 Brussel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1553 leftover public koepel after honest leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished so leftover public koepel with live official NBB JR2025 euros taken; official CDN PDF. FOI ready not sent. NOT leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand"
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

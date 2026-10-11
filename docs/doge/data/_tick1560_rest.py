#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1560 commitments / leaderboard / foi_queue. Surgical append only."""
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_soci"
SRC = "src_socius_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00065726.pdf"
GAP = "gap_socius_bruto_1_38m_pers_1_27m_beleg_1_04m_l5"
LB = "lb_socius_bruto_1_38m_pers_1_27m_beleg_1_04m"
COMM = "comm_socius_jr2025_bruto"
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
    f"{COMM},Socius JR2025 leftover public koepel dual (bruto 1.38m / pers 1.27m 12.2 VTE / expl PROFIT 91.2k / PnL PROFIT 103.7k / assets 1.36m / beleg 1.04m / cash 74.2k / MVA JUMP 39.0k / lev DROP 71.0k),{ENT},Socius / dual mined Flanders / socius,VZW-wet; Bestuursdecreet openbaarheid; erkenning steunpunt sociaal-cultureel werk,2026-03-25,2025,2025,1380002,,,active,{PDF},Local leftover public koepel map VL socio-cultural support point — bruto 1.38m / pers 1.27m / beleg 1.04m / MVA JUMP 39.0k / lev DROP 71.0k,Publish full AV notulen 25.03.2026 + 73 lidgeld/subsidy split (VKT empty) + toelichting beleg 1.04m / MVA JUMP / lev DROP / other ST JUMP / commissaris unpublished; do not keep leftover Socius unpublished,{SRC},strong,Vlaanderen>Koepel>Socius>JR2025_L5,tick1560; bruto 1380002 omzet empty 73 empty pers 1265278 vte 12.2 expl 91179 pnl 103727 assets 1356462 beleg 1044949 cash 74193 mva JUMP 39032 lev DROP 70980; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},Socius JR2025 leftover public koepel: bruto 1.38m / pers 1.27m 12.2 VTE / expl PROFIT 91.2k / PnL PROFIT 103.7k / assets 1.36m / beleg 1.04m / cash 74.2k / MVA JUMP 39.0k / lev DROP 71.0k,L5,local_budget_line,Vlaanderen>Koepel>Socius>JR2025_L5,1380002,1356462,Leftover dual public koepel shell: bruto 1.38m / omzet empty / 73 empty / pers 1.27m 12.2 VTE / expl PROFIT 91.2k / PnL PROFIT 103.7k / assets 1.36m / beleg 1.04m / cash 74.2k / MVA JUMP 39.0k / lev DROP 71.0k / other ST JUMP 9.6k / commissaris unpublished VKT sectie 8 / dividend n.a.,strong,{SRC},Vlaams sociaal-cultureel werk / Vlaamse overheid,Local leftover public koepel map Socius — official NBB VKT-VZW JR2025 live; 73/70/60/61 FOI,Official NBB 2026-08-20: bruto 1.38m / pers 1.27m / assets 1.36m / beleg 1.04m / MVA JUMP 39.0k,3.5,5.6,3.0,4.6,Publish full AV notulen 25.03.2026 + 73 lidgeld/subsidy split (VKT empty) + toelichting beleg 1.04m / MVA JUMP / lev DROP / other ST JUMP / commissaris unpublished; do not keep leftover Socius unpublished,active,,tick1560; leftover public koepel VZW of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick; leftover FARO still JR2024 so leftover Socius with live official CDN taken; leftover publiq unused live deferred; FOI ready not sent; not TE-additive of 348bn; distinct from leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Koepel>Socius>JR2025_L5,{ENT},Official NBB VKT-VZW publishes bruto 1380002 / omzet 70 empty / 73 empty / pers 1265278 12.2 VTE / expl PROFIT 91179 / PnL PROFIT 103727 / assets 1356462 / beleg 1044949 / cash 74193 / MVA JUMP 39032 / lev DROP 70980 / other ST JUMP 9576; 73/70/60/61 unpublished VKT; sectie 8 commissaris unpublished; toelichting beleg 1.04m / MVA JUMP / lev DROP / other ST JUMP unpublished; AV notulen 25.03.2026 unpublished; beheersovereenkomst Vlaamse Regering unpublished,Leftover public koepel VZW of mined Flanders with live official NBB JR2025 euros; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick; leftover FARO still JR2024; bruto 1.38m / pers 1.27m / beleg 1.04m,8,Socius VZW / dienst openbaarheid,debbie.bevers@socius.be,Sainctelettesquare 19 1000 Brussel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1560 leftover public koepel after honest leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished so leftover public koepel with live official NBB JR2025 euros taken; leftover FARO still JR2024 so leftover Socius taken; leftover publiq unused live deferred; official CDN PDF. FOI ready not sent. NOT leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
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

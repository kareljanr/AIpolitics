#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1561 commitments / leaderboard / foi_queue. Surgical append only."""
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_pubq"
SRC = "src_publiq_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00086529.pdf"
GAP = "gap_publiq_bruto_7_29m_pers_6_49m_recv_jump_l5"
LB = "lb_publiq_bruto_7_29m_pers_6_49m_recv_jump"
COMM = "comm_publiq_jr2025_bruto"
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
    f"{COMM},publiq JR2025 leftover public koepel dual (bruto 7.29m / pers 6.49m 81.2 VTE / expl PROFIT 151.9k / PnL PROFIT 150.7k / assets 4.20m / recv JUMP 2.33m / beleg JUMP 267k / cash 862k / accrued JUMP 834k / onttrekking 828k),{ENT},publiq / dual mined Flanders / publiq,VZW-wet; Bestuursdecreet openbaarheid; digital kernspeler Vlaamse overheid,2026-03-23,2025,2025,7291932,,,active,{PDF},Local leftover public koepel map VL digital culture leisure platform — bruto 7.29m / pers 6.49m / recv JUMP 2.33m / beleg JUMP 267k / accrued JUMP 834k / onttrekking 828k,Publish full AV notulen 23.03.2026 + 73 lidgeld/subsidy split (VKT empty) + toelichting recv JUMP 2.33m / beleg JUMP 267k / accrued JUMP 834k / onttrekking 828k / commissaris unpublished / zetel KBO vs JR; do not keep leftover publiq unpublished,{SRC},strong,Vlaanderen>Koepel>publiq>JR2025_L5,tick1561; bruto 7291932 omzet empty 73 empty pers 6493450 vte 81.2 expl 151937 pnl 150686 assets 4196794 recv JUMP 2328518 beleg JUMP 267028 cash 862453 accrued JUMP 833654 onttrekking 827535; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},publiq JR2025 leftover public koepel: bruto 7.29m / pers 6.49m 81.2 VTE / expl PROFIT 151.9k / PnL PROFIT 150.7k / assets 4.20m / recv JUMP 2.33m / beleg JUMP 267k / cash 862k / accrued JUMP 834k / onttrekking 828k,L5,local_budget_line,Vlaanderen>Koepel>publiq>JR2025_L5,7291932,4196794,Leftover dual public koepel shell: bruto 7.29m / omzet empty / 73 empty / pers 6.49m 81.2 VTE / expl PROFIT 151.9k / PnL PROFIT 150.7k / assets 4.20m / recv JUMP 2.33m / beleg JUMP 267k / cash 862k / accrued JUMP 834k / onttrekking 828k / commissaris unpublished VKT sectie 8 / zetel KBO vs JR / dividend n.a.,strong,{SRC},Vlaams cultuur- en vrijetijdspubliek / Vlaamse overheid,Local leftover public koepel map publiq — official NBB VKT-VZW JR2025 live; 73/70/60/61 FOI,Official NBB 2026-08-20: bruto 7.29m / pers 6.49m / assets 4.20m / recv JUMP 2.33m / beleg JUMP 267k / accrued JUMP 834k,3.8,6.4,3.0,5.1,Publish full AV notulen 23.03.2026 + 73 lidgeld/subsidy split (VKT empty) + toelichting recv JUMP 2.33m / beleg JUMP 267k / accrued JUMP 834k / onttrekking 828k / commissaris unpublished / zetel KBO vs JR; do not keep leftover publiq unpublished,active,,tick1561; leftover public koepel VZW of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick; leftover FARO still no confirmed JR2025 so leftover publiq with live official CDN taken; leftover Socius 1560 TAKEN; FOI ready not sent; not TE-additive of 348bn; distinct from leftover Socius 1560 / leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Koepel>publiq>JR2025_L5,{ENT},Official NBB VKT-VZW publishes bruto 7291932 / omzet 70 empty / 73 empty / pers 6493450 81.2 VTE / expl PROFIT 151937 / PnL PROFIT 150686 / assets 4196794 / recv JUMP 2328518 / beleg JUMP 267028 / cash 862453 / accrued JUMP 833654 / onttrekking 791 827535; 73/70/60/61 unpublished VKT; sectie 8 commissaris unpublished; toelichting recv JUMP / beleg JUMP / accrued JUMP / onttrekking / equity JUMP unpublished; AV notulen 23.03.2026 unpublished; beheersovereenkomst Vlaamse Regering unpublished; zetel KBO vs JR unpublished,Leftover public koepel VZW of mined Flanders with live official NBB JR2025 euros; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick; leftover FARO still no confirmed JR2025; bruto 7.29m / pers 6.49m / recv JUMP 2.33m,8,publiq VZW / dienst openbaarheid,info@publiq.be,Henegouwenkaai 41-43 1080 Sint-Jans-Molenbeek,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1561 leftover public koepel after honest leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished so leftover public koepel with live official NBB JR2025 euros taken; leftover FARO still no confirmed JR2025 so leftover publiq taken; leftover Socius 1560 TAKEN; official CDN PDF. FOI ready not sent. NOT leftover Socius 1560 / leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
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

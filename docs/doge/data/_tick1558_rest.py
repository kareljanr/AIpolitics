#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1558 commitments / leaderboard / foi_queue. Surgical append only."""
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_meem"
SRC = "src_meemoo_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00090751.pdf"
GAP = "gap_meemoo_bruto_5_41m_pers_4_93m_cash_drop_l5"
LB = "lb_meemoo_bruto_5_41m_pers_4_93m_cash_drop"
COMM = "comm_meemoo_jr2025_bruto"
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
    f"{COMM},meemoo JR2025 leftover public koepel dual (bruto 5.41m / pers 4.93m 64.9 VTE / expl LOSS 4.5k / PnL PROFIT 11.6k / assets 3.44m / cash DROP 0.99m / lev JUMP 1.08m / accrued DROP 0.97m),{ENT},meemoo / dual mined Flanders / Vlaams instituut voor het archief,VZW-wet; Bestuursdecreet openbaarheid; aanbestedende overheid,2026-04-23,2025,2025,5412745,,,active,{PDF},Local leftover public koepel map VL archive institute — bruto 5.41m / pers 4.93m / cash DROP 0.99m / lev JUMP 1.08m / accrued DROP 0.97m,Publish full AV notulen 23.04.2026 + 73 lidgeld/subsidy split (VKT empty) + toelichting cash DROP / lev JUMP / accrued DROP / other recv 1.21m; do not keep leftover meemoo unpublished,{SRC},strong,Vlaanderen>Koepel>meemoo>JR2025_L5,tick1558; bruto 5412745 omzet empty 73 empty pers 4927717 vte 64.9 expl -4546 pnl 11551 assets 3435584 cash DROP 994688 lev JUMP 1076339 accrued DROP 970841 otherrecv 1209119 commissaris 8600 extra 2500; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},meemoo JR2025 leftover public koepel: bruto 5.41m / pers 4.93m 64.9 VTE / expl LOSS 4.5k / PnL PROFIT 11.6k / assets 3.44m / cash DROP 0.99m / lev JUMP 1.08m / accrued DROP 0.97m,L5,local_budget_line,Vlaanderen>Koepel>meemoo>JR2025_L5,5412745,3435584,Leftover dual public koepel shell: bruto 5.41m / omzet empty / 73 empty / pers 4.93m 64.9 VTE / expl LOSS 4.5k / PnL PROFIT 11.6k / assets 3.44m / cash DROP 0.99m / lev JUMP 1.08m / accrued DROP 0.97m / other recv 1.21m / commissaris 8600 extra 2500 / dividend n.a.,strong,{SRC},Vlaams archief / Vlaamse overheid,Local leftover public koepel map meemoo — official NBB VKT-VZW JR2025 live; 73/70/60/61 FOI,Official NBB 2026-08-20: bruto 5.41m / pers 4.93m / assets 3.44m / cash DROP 0.99m / lev JUMP 1.08m,6.7,6.2,3.0,5.3,Publish full AV notulen 23.04.2026 + 73 lidgeld/subsidy split (VKT empty) + toelichting cash DROP / lev JUMP / accrued DROP / other recv; do not keep leftover meemoo unpublished,active,,tick1558; leftover public koepel VZW of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Koepel>meemoo>JR2025_L5,{ENT},Official NBB VKT-VZW publishes bruto 5412745 / omzet 70 empty / 73 empty / pers 4927717 64.9 VTE / expl LOSS -4546 / PnL PROFIT 11551 / assets 3435584 / cash DROP 994688 / lev JUMP 1076339 / accrued DROP 970841 / other recv 1209119; 73/70/60/61 unpublished VKT; toelichting cash DROP / lev JUMP / accrued DROP / other recv unpublished; commissaris 8600 extra 2500; AV notulen 23.04.2026 unpublished; beheersovereenkomst Vlaamse Regering unpublished; reserves +100k still named VIAA unpublished,Leftover public koepel VZW of mined Flanders with live official NBB JR2025 euros; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick; bruto 5.41m / pers 4.93m / cash DROP 0.99m / lev JUMP 1.08m,8,meemoo VZW / dienst openbaarheid,info@meemoo.be,Ham 175 9000 Gent,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1558 leftover public koepel after honest leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished so leftover public koepel with live official NBB JR2025 euros taken; official CDN PDF. FOI ready not sent. NOT leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
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

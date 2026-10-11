#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1554 commitments / leaderboard / foi_queue. Surgical append only."""
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_vleva"
SRC = "src_vleva_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00075254.pdf"
GAP = "gap_vleva_bruto_1_08m_pers_1_02m_expl_loss_l5"
LB = "lb_vleva_bruto_1_08m_pers_1_02m_expl_loss"
COMM = "comm_vleva_jr2025_bruto"
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
    f"{COMM},VLEVA JR2025 leftover public koepel dual (bruto 1.08m / pers 1.02m 8.8 VTE / expl LOSS 54.8k / PnL LOSS 56.3k / assets 0.43m / cash DROP / LT DROP),{ENT},VLEVA / dual mined Flanders / Vlaamse lokale besturen en middenveld koepel EU,VZW-wet; Bestuursdecreet openbaarheid,2026-03-26,2025,2025,1077899,,,active,{PDF},Local leftover public koepel map VL-EU VLEVA — bruto 1.08m / pers 1.02m / expl LOSS 54.8k / cash DROP 0.10m,Publish full AV notulen 26.03.2026 + 73 lidgeld/subsidy split (VKT empty) + toelichting expl LOSS / cash DROP / VA DROP / LT DROP / continuity; do not keep leftover VLEVA unpublished,{SRC},strong,Vlaanderen>Koepel>VLEVA>JR2025_L5,tick1554; bruto 1077899 omzet empty 73 empty pers 1021920 vte 8.8 expl -54822 pnl -56289 assets 433039 cash 104066 DROP va 262987 DROP lev 20596 JUMP commissaris 4160; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},VLEVA JR2025 leftover public koepel: bruto 1.08m / pers 1.02m 8.8 VTE / expl LOSS 54.8k / PnL LOSS 56.3k / assets 0.43m / cash DROP / LT DROP,L5,local_budget_line,Vlaanderen>Koepel>VLEVA>JR2025_L5,1077899,433039,Leftover dual public koepel shell: bruto 1.08m / omzet empty / 73 empty / pers 1.02m 8.8 VTE / expl LOSS 54.8k / PnL LOSS 56.3k / assets 0.43m / cash DROP 0.10m / VA DROP 0.26m / LT DROP 6.0k / lev JUMP 20.6k / commissaris 4160 / dividend n.a.,strong,{SRC},Vlaamse lokale besturen / middenveld / Vlaamse overheid,Local leftover public koepel map VL-EU VLEVA — official NBB VKT-VZW JR2025 live; 73/70/60/61 FOI,Official NBB 2026-08-20: bruto 1.08m / pers 1.02m / assets 0.43m / expl LOSS 54.8k,6.4,3.6,3.0,4.6,Publish full AV notulen 26.03.2026 + 73 lidgeld/subsidy split (VKT empty) + toelichting expl LOSS / cash DROP / VA DROP / LT DROP / continuity; do not keep leftover VLEVA unpublished,active,,tick1554; leftover public koepel VZW of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand / leftover Zuidrand"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Koepel>VLEVA>JR2025_L5,{ENT},Official NBB VKT-VZW publishes bruto 1077899 / omzet 70 empty / 73 empty / pers 1021920 8.8 VTE / expl LOSS -54822 / PnL LOSS -56289 / assets 433039 / cash DROP 104066 / VA DROP 262987 / LT DROP 6016 / lev JUMP 20596; 73 lidgeld/subsidy unpublished (VKT); 60/61 unpublished; toelichting expl LOSS / cash DROP / VA DROP / LT DROP / continuity unpublished; commissaris 4160 no extra split; AV notulen 26.03.2026 unpublished; ledenlijst/lidgeld unpublished,Leftover public koepel VZW of mined Flanders with live official NBB JR2025 euros; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick; bruto 1.08m / pers 1.02m / expl LOSS 54.8k,8,VLEVA vzw / dienst openbaarheid,info@vleva.eu,Aarlenstraat 80 1000 Brussel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1554 leftover public koepel after honest leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished so leftover public koepel with live official NBB JR2025 euros taken; official CDN PDF. FOI ready not sent. NOT leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand / leftover Zuidrand"
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

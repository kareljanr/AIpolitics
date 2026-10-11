#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1559 commitments / leaderboard / foi_queue. Surgical append only."""
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_knst"
SRC = "src_kunstenpunt_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00065820.pdf"
GAP = "gap_kunstenpunt_bruto_1_71m_pers_1_74m_expl_loss_l5"
LB = "lb_kunstenpunt_bruto_1_71m_pers_1_74m_expl_loss"
COMM = "comm_kunstenpunt_jr2025_bruto"
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
    f"{COMM},Kunstensteunpunt JR2025 leftover public koepel dual (bruto 1.71m / pers 1.74m 20 VTE exceeds bruto / expl LOSS 57.1k / PnL LOSS 57.3k / assets 0.68m / cash DROP 0.32m / lev JUMP 70.5k / accrued JUMP 57.2k),{ENT},Kunstenpunt / dual mined Flanders / kunstensteunpunt,VZW-wet; Bestuursdecreet openbaarheid; erkenning kunstensteunpunt,2026-03-23,2025,2025,1713627,,,active,{PDF},Local leftover public koepel map VL arts support point — bruto 1.71m / pers 1.74m exceeds bruto / cash DROP 0.32m / lev JUMP 70.5k / accrued JUMP 57.2k,Publish full AV notulen 23.03.2026 + 73 lidgeld/subsidy split (VKT empty) + toelichting pers>bruto / expl LOSS / cash DROP / lev JUMP / accrued JUMP / prepaid JUMP / VTI-fusie fonds; do not keep leftover Kunstensteunpunt unpublished,{SRC},strong,Vlaanderen>Koepel>Kunstenpunt>JR2025_L5,tick1559; bruto 1713627 omzet empty 73 empty pers 1742627 vte 20 expl -57096 pnl -57334 assets 677951 cash DROP 324544 lev JUMP 70453 accrued JUMP 57176 prepaid JUMP 42818 otherrecv 234542; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},Kunstensteunpunt JR2025 leftover public koepel: bruto 1.71m / pers 1.74m 20 VTE exceeds bruto / expl LOSS 57.1k / PnL LOSS 57.3k / assets 0.68m / cash DROP 0.32m / lev JUMP 70.5k / accrued JUMP 57.2k,L5,local_budget_line,Vlaanderen>Koepel>Kunstenpunt>JR2025_L5,1713627,677951,Leftover dual public koepel shell: bruto 1.71m / omzet empty / 73 empty / pers 1.74m 20 VTE exceeds bruto / expl LOSS 57.1k / PnL LOSS 57.3k / assets 0.68m / cash DROP 0.32m / lev JUMP 70.5k / accrued JUMP 57.2k / prepaid JUMP 42.8k / other recv 0.23m / commissaris unpublished VKT sectie 8 / dividend n.a.,strong,{SRC},Vlaamse kunsten / Vlaamse overheid,Local leftover public koepel map Kunstenpunt — official NBB VKT-VZW JR2025 live; 73/70/60/61 FOI,Official NBB 2026-08-20: bruto 1.71m / pers 1.74m exceeds bruto / assets 0.68m / expl LOSS 57.1k / cash DROP 0.32m,6.8,5.6,3.0,5.2,Publish full AV notulen 23.03.2026 + 73 lidgeld/subsidy split (VKT empty) + toelichting pers>bruto / expl LOSS / cash DROP / lev JUMP / accrued JUMP / prepaid JUMP / VTI-fusie fonds; do not keep leftover Kunstensteunpunt unpublished,active,,tick1559; leftover public koepel VZW of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick; leftover FARO still JR2024 so leftover Kunstensteunpunt with live official CDN taken; FOI ready not sent; not TE-additive of 348bn; distinct from leftover meemoo 1558 / leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Koepel>Kunstenpunt>JR2025_L5,{ENT},Official NBB VKT-VZW publishes bruto 1713627 / omzet 70 empty / 73 empty / pers 1742627 20 VTE exceeds bruto / expl LOSS -57096 / PnL LOSS -57334 / assets 677951 / cash DROP 324544 / lev JUMP 70453 / accrued JUMP 57176 / prepaid JUMP 42818 / other recv 234542; 73/70/60/61 unpublished VKT; sectie 8 commissaris unpublished; toelichting pers>bruto / expl LOSS / cash DROP / lev JUMP / accrued JUMP / prepaid JUMP / VTI-fusie fonds unpublished; AV notulen 23.03.2026 unpublished; beheersovereenkomst Vlaamse Regering unpublished,Leftover public koepel VZW of mined Flanders with live official NBB JR2025 euros; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick; leftover FARO still JR2024; bruto 1.71m / pers 1.74m exceeds bruto / expl LOSS 57.1k,8,Kunstensteunpunt VZW / dienst openbaarheid,info@kunsten.be,Ravensteingalerij 38 1000 Brussel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1559 leftover public koepel after honest leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished so leftover public koepel with live official NBB JR2025 euros taken; leftover FARO still JR2024 so leftover Kunstensteunpunt taken; official CDN PDF. FOI ready not sent. NOT leftover meemoo 1558 / leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
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

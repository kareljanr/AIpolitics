#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1557 commitments / leaderboard / foi_queue. Surgical append only."""
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "son_vlho"
SRC = "src_vlhora_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00079599.pdf"
GAP = "gap_vlhora_bruto_1_20m_pers_1_05m_recv_jump_l5"
LB = "lb_vlhora_bruto_1_20m_pers_1_05m_recv_jump"
COMM = "comm_vlhora_jr2025_bruto"
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
    f"{COMM},VLHORA JR2025 leftover public koepel dual (bruto 1.20m / pers 1.05m 13.2 VTE / expl PROFIT 144k / PnL PROFIT 143k / assets 11.93m / recv JUMP 7.67m / vooruit JUMP 9.37m / cash DROP),{ENT},VLHORA / dual mined Flanders / Vlaamse hogescholen koepel,SON-wet; Bestuursdecreet openbaarheid,2026-03-27,2025,2025,1200770,,,active,{PDF},Local leftover public koepel map VL hogescholen — bruto 1.20m / pers 1.05m / recv JUMP 7.67m / vooruit JUMP 9.37m / cash DROP 2.97m,Publish full AV notulen 27.03.2026 + 73 lidgeld/subsidy split (VKT empty) + toelichting handelsrecv JUMP / vooruit JUMP / cash DROP / lev DROP; do not keep leftover VLHORA unpublished,{SRC},strong,Vlaanderen>Koepel>VLHORA>JR2025_L5,tick1557; bruto 1200770 omzet empty 73 empty pers 1052307 vte 13.2 expl 144241 pnl 143093 assets 11929249 handelsrecv JUMP 7665740 vooruit JUMP 9370719 cash DROP 2972417 lev DROP 439394 commissaris 4958; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},VLHORA JR2025 leftover public koepel: bruto 1.20m / pers 1.05m 13.2 VTE / expl PROFIT 144k / PnL PROFIT 143k / assets 11.93m / recv JUMP 7.67m / vooruit JUMP 9.37m / cash DROP,L5,local_budget_line,Vlaanderen>Koepel>VLHORA>JR2025_L5,1200770,11929249,Leftover dual public koepel shell: bruto 1.20m / omzet empty / 73 empty / pers 1.05m 13.2 VTE / expl PROFIT 144k / PnL PROFIT 143k / assets 11.93m / handelsrecv JUMP 7.67m / vooruit JUMP 9.37m / cash DROP 2.97m / lev DROP 0.44m / commissaris 4958 / dividend n.a.,strong,{SRC},Vlaamse hogescholen / Vlaamse overheid,Local leftover public koepel map VLHORA — official NBB VKT-VZW JR2025 live; 73/70/60/61 FOI,Official NBB 2026-08-20: bruto 1.20m / pers 1.05m / assets 11.93m / recv JUMP 7.67m / vooruit JUMP 9.37m,6.6,5.2,3.0,5.0,Publish full AV notulen 27.03.2026 + 73 lidgeld/subsidy split (VKT empty) + toelichting handelsrecv JUMP / vooruit JUMP / cash DROP / lev DROP; do not keep leftover VLHORA unpublished,active,,tick1557; leftover public koepel SON of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Koepel>VLHORA>JR2025_L5,{ENT},Official NBB VKT-VZW publishes bruto 1200770 / omzet 70 empty / 73 empty / pers 1052307 13.2 VTE / expl PROFIT 144241 / PnL PROFIT 143093 / assets 11929249 / handelsrecv JUMP 7665740 / vooruit JUMP 9370719 / cash DROP 2972417 / lev DROP 439394; 73/70/60/61 unpublished VKT; toelichting handelsrecv JUMP / vooruit JUMP / cash DROP / lev DROP unpublished; commissaris 4958 extra 0; AV notulen 27.03.2026 unpublished; ledenlijst/hogeschoolssleutel unpublished; KBO zetel Ravensteingalerij vs JR PDF Sinter-Goedeleplein unpublished,Leftover public koepel SON of mined Flanders with live official NBB JR2025 euros; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick; bruto 1.20m / pers 1.05m / recv JUMP 7.67m / vooruit JUMP 9.37m,8,VLHORA SON / dienst openbaarheid,info@vlhora.be,Sinter-Goedeleplein 14 1000 Brussel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1557 leftover public koepel after honest leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished so leftover public koepel with live official NBB JR2025 euros taken; official CDN PDF. FOI ready not sent. NOT leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
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

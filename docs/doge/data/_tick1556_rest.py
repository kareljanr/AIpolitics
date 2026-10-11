#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1556 commitments / leaderboard / foi_queue. Surgical append only."""
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "son_vlir"
SRC = "src_vlir_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00072863.pdf"
GAP = "gap_vlir_opbr_36_81m_pers_4_01m_uos_passthru_l5"
LB = "lb_vlir_opbr_36_81m_pers_4_01m_uos_passthru"
COMM = "comm_vlir_jr2025_opbr"
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
    f"{COMM},VLIR JR2025 leftover public koepel dual (opbr 36.81m / pers 4.01m 37.9 VTE / 73 34.10m / othercosts JUMP 30.01m / assets 20.06m / cash JUMP / beleg DROP),{ENT},VLIR / dual mined Flanders / Vlaamse universiteiten + federale VLIR-UOS,SON-wet; Bestuursdecreet openbaarheid,2026-03-27,2025,2025,36809788,,,active,{PDF},Local leftover public koepel map VL universities + VLIR-UOS — opbr 36.81m / pers 4.01m / 73 34.10m / othercosts JUMP 30.01m / cash JUMP 4.93m,Publish full AV notulen 27.03.2026 + 73/VLIR-UOS split + toelichting othercosts JUMP / beleg DROP / cash JUMP / vooruit 16.00m; do not keep leftover VLIR unpublished,{SRC},strong,Vlaanderen>Koepel>VLIR>JR2025_L5,tick1556; opbr 36809788 omzet 1742031 73 34095480 pers 4013097 vte 37.9 expl 60746 pnl 312676 assets 20061015 cash 4929904 JUMP beleg 9092658 DROP vooruit 15996948 othercosts 30005208 JUMP commissaris 14128 extra 19500; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},VLIR JR2025 leftover public koepel: opbr 36.81m / pers 4.01m 37.9 VTE / 73 34.10m / othercosts JUMP 30.01m / assets 20.06m / cash JUMP / beleg DROP,L5,local_budget_line,Vlaanderen>Koepel>VLIR>JR2025_L5,36809788,20061015,Leftover dual public koepel shell: opbr 36.81m / omzet 1.74m commercial-only / 73 34.10m / pers 4.01m 37.9 VTE / expl PROFIT 60.7k / PnL PROFIT 0.31m / assets 20.06m / cash JUMP 4.93m / beleg DROP 9.09m / vooruit 16.00m / othercosts JUMP 30.01m VLIR-UOS pass-through / commissaris 14.1k + extra 19.5k / dividend n.a.,strong,{SRC},Vlaamse universiteiten / federale DGD VLIR-UOS / Vlaamse overheid,Local leftover public koepel map VLIR — official NBB VOL-VZW JR2025 live; 73/VLIR-UOS/othercosts FOI,Official NBB 2026-08-20: opbr 36.81m / pers 4.01m / assets 20.06m / othercosts JUMP 30.01m,6.8,6.2,3.0,5.4,Publish full AV notulen 27.03.2026 + 73/VLIR-UOS split + toelichting othercosts JUMP / beleg DROP / cash JUMP / vooruit 16.00m; do not keep leftover VLIR unpublished,active,,tick1556; leftover public koepel SON of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover VLUHR 1555 / leftover VLHORA / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Koepel>VLIR>JR2025_L5,{ENT},Official NBB VOL-VZW publishes opbr 36809788 / omzet 1742031 commercial-only / 73 34095480 (733 only 730 empty) / pers 4013097 37.9 VTE / expl PROFIT 60746 / PnL PROFIT 312676 / assets 20061015 / cash JUMP 4929904 / beleg DROP 9092658 / vooruit 15996948 / othercosts 640 JUMP 30005208; 73/VLIR-UOS split unpublished beyond toelichting 1204939+32890541; toelichting othercosts JUMP / beleg DROP / cash JUMP / vooruit / 71 swing unpublished; commissaris 14128 + extra 19500; AV notulen 27.03.2026 unpublished; ledenlijst/universiteitssleutel unpublished,Leftover public koepel SON of mined Flanders with live official NBB JR2025 euros; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick; opbr 36.81m / pers 4.01m / othercosts JUMP 30.01m,8,VLIR SON / dienst openbaarheid,administratie@vlir.be,Sinter-Goedeleplein 14 1000 Brussel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1556 leftover public koepel after honest leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished so leftover public koepel with live official NBB JR2025 euros taken; official CDN PDF. FOI ready not sent. NOT leftover VLUHR 1555 / leftover VLHORA / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
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

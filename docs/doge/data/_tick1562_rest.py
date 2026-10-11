#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1562 commitments / leaderboard / foi_queue. Surgical append only."""
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_cult"
SRC = "src_cultuurconnect_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00072195.pdf"
GAP = "gap_cultuurconnect_opbr_12_75m_pers_5_18m_expl_loss_l5"
LB = "lb_cultuurconnect_opbr_12_75m_pers_5_18m_expl_loss"
COMM = "comm_cultuurconnect_jr2025_opbr"
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
    f"{COMM},Cultuurconnect JR2025 leftover public koepel dual (opbr 12.75m / omzet 5.03m commercial-only / 73 7.72m / pers 5.18m 51 VTE / expl LOSS 1.09m / PnL LOSS 1.05m / assets 6.48m / cash DROP 5.10m / 60 8.13m / onttrekking 2.81m),{ENT},Cultuurconnect / dual mined Flanders / Cultuurconnect,VZW-wet; Bestuursdecreet openbaarheid; digital culture steunpunt Vlaamse overheid,2026-03-26,2025,2025,12751502,,,active,{PDF},Local leftover public koepel map VL digital culture libraries theatres platform — opbr 12.75m / pers 5.18m / expl LOSS 1.09m / cash DROP 5.10m / 60 8.13m / onttrekking 2.81m,Publish full AV notulen 26.03.2026 + 73 Flanders/other subsidy split + toelichting 60 8.13m pass-through vs omzet 5.03m + cash DROP 5.10m + onttrekking 2.81m / toevoeging 2.28m / two-year LOSS continuity / beheersovereenkomst; do not keep leftover Cultuurconnect unpublished,{SRC},strong,Vlaanderen>Koepel>Cultuurconnect>JR2025_L5,tick1562; opbr 12751502 omzet 5026615 73 7718118 pers 5184352 vte 51 expl LOSS 1090651 pnl LOSS 1049404 assets 6483521 cash DROP 5103622 60 8128810 onttrekking 2814680; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},Cultuurconnect JR2025 leftover public koepel: opbr 12.75m / omzet 5.03m commercial-only / 73 7.72m / pers 5.18m 51 VTE / expl LOSS 1.09m / PnL LOSS 1.05m / assets 6.48m / cash DROP 5.10m / 60 8.13m / onttrekking 2.81m,L5,local_budget_line,Vlaanderen>Koepel>Cultuurconnect>JR2025_L5,12751502,6483521,Leftover dual public koepel shell: opbr 12.75m / omzet 5.03m commercial-only / 73 7.72m / pers 5.18m 51 VTE / expl LOSS 1.09m two consecutive years / PnL LOSS 1.05m / assets 6.48m / cash DROP 5.10m / 60 handelsgoederen 8.13m exceeds omzet / onttrekking 2.81m / toevoeging 2.28m / commissaris 7.9k / dividend n.a.,strong,{SRC},Vlaams cultuur- en bibliotheekpubliek / Vlaamse overheid,Local leftover public koepel map Cultuurconnect — official NBB VOL-VZW JR2025 live; 73 split / 60 pass-through / cash DROP / two-year LOSS FOI,Official NBB 2026-08-20: opbr 12.75m / pers 5.18m / assets 6.48m / expl LOSS 1.09m / cash DROP 5.10m / 60 8.13m / onttrekking 2.81m,4.1,6.6,3.0,5.4,Publish full AV notulen 26.03.2026 + 73 Flanders/other subsidy split + toelichting 60 8.13m pass-through vs omzet 5.03m + cash DROP 5.10m + onttrekking 2.81m / toevoeging 2.28m / two-year LOSS continuity / beheersovereenkomst; do not keep leftover Cultuurconnect unpublished,active,,tick1562; leftover public koepel VZW of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick; leftover FARO still JR2024 so leftover Cultuurconnect with live official CDN taken; leftover publiq 1561 TAKEN; leftover VI.BE CDN live unused deferred; leftover OP-TIL unused not confirmed JR2025; FOI ready not sent; not TE-additive of 348bn; distinct from leftover publiq 1561 / leftover Socius 1560 / leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland / leftover OP-TIL / leftover VI.BE"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Koepel>Cultuurconnect>JR2025_L5,{ENT},Official NBB VOL-VZW publishes opbr 12751502 / omzet 70 5026615 commercial-only / 73 7718118 733 only / pers 5184352 51 VTE / expl LOSS 1090651 / PnL LOSS 1049404 / assets 6483521 / cash DROP 5103622 / 60 8128810 / onttrekking 791 2814680 / toevoeging 691 2280119; 73 Flanders/other split unpublished; 60 pass-through vs omzet unpublished; cash DROP toelichting unpublished; two consecutive years budgeted LOSS continuity unpublished; AV notulen 26.03.2026 unpublished; beheersovereenkomst Vlaamse Regering unpublished,Leftover public koepel VZW of mined Flanders with live official NBB JR2025 euros; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick; leftover FARO still JR2024; opbr 12.75m / pers 5.18m / expl LOSS 1.09m,8,Cultuurconnect VZW / dienst openbaarheid,servicedesk@cultuurconnect.be,Miriam Makebaplein 1 9000 Gent,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1562 leftover public koepel after honest leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished so leftover public koepel with live official NBB JR2025 euros taken; leftover FARO still JR2024 so leftover Cultuurconnect taken; leftover publiq 1561 TAKEN; leftover VI.BE CDN live unused deferred; leftover OP-TIL unused not confirmed JR2025; official CDN PDF. FOI ready not sent. NOT leftover publiq 1561 / leftover Socius 1560 / leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland / leftover OP-TIL / leftover VI.BE"
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

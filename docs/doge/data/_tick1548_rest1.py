#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "igs_hvoo"
SRC = "src_hvoo_jr2025_bbc"
GAP = "gap_hvoo_assets_13_59m_result_gewone_2_01m_rekening_l5"
LB = "lb_hvoo_assets_13_59m_result_gewone_2_01m"
COMM = "comm_hvoo_jr2025_assets"
PDF = "https://oost.hulpverleningszone.be/storage/i3rR7xKSixoE9claxCf2XSYVEfzV1myOsvvwfhGq.pdf"

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
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:160]}")
    if any("," in f for f in fields):
        raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")

comm = (
    f"{COMM},HVZ Oost OVL JR2025 leftover IGS dual (assets 13.59m / resultaat gewone 2.01m / boek gewone 2.48m / buitengewoon -2.90m / pnl -25k),{ENT},HVZ Oost OVL / dual mined Dendermonde + remaining Oost-Vlaanderen Oost municipalities / municipal + federal civiele-veiligheid,Wet 15.05.2007 civiele veiligheid; KB boekhouding hulpverleningszones; Bestuursdecreet openbaarheid,2026-05-22,2025,2025,13589234,,,active,{PDF},Local leftover IGS fire-rescue map VL Dendermonde HVZ Oost OVL — assets 13.59m / resultaat gewone 2.01m / unpublished uitgaven gewone pers werking,Publish full rekening 2025 verslag + uitgaven/ontvangsten gewone + pers/werking + VTE + per-gemeente split + cash/debt/equity + full BBC M2; do not keep leftover HVZ Oost OVL unpublished,{SRC},strong,Vlaanderen>Gemeenten>Dendermonde>IGS>HVZ_Oost_OVL>JR2025_L5,tick1548; balans 13589234 resultaat_gewone_begroting 2011808 resultaat_gewone_boek 2481692 resultaat_buit_begroting -2897489 resultaat_buit_boek 703832 pnl_nadelig 25226; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},HVZ Oost OVL JR2025 leftover IGS: assets 13.59m / resultaat gewone 2.01m / unpublished uitgaven gewone pers werking,L5,local_budget_line,Vlaanderen>Gemeenten>Dendermonde>IGS>HVZ_Oost_OVL>JR2025_L5,13589234,13589234,Leftover dual IGS fire-rescue shell: balans 13.59m / resultaat gewone begroting 2.01m / boek gewone 2.48m / buitengewoon begroting -2.90m / boek buit 0.70m / pnl nadelig 25k / uitgaven gewone pers werking VTE cash debt equity unpublished,strong,{SRC},HVZ Oost OVL / dual mined Dendermonde + remaining Oost-Vlaanderen Oost municipalities / municipal + federal civiele-veiligheid,Local leftover IGS fire-rescue map VL Dendermonde HVZ Oost OVL — zoneraad 22.05.2026 rekening 2025 live; uitgaven gewone + pers/VTE FOI,Official zoneraad 2026-08-20: assets 13.59m / resultaat gewone 2.01m / unpublished uitgaven gewone,6.8,6.8,3.0,6.0,Publish full rekening 2025 verslag + uitgaven/ontvangsten gewone + pers/werking + VTE + per-gemeente split + cash/debt/equity + full BBC M2; do not keep leftover HVZ Oost OVL unpublished,active,,tick1548; leftover IGS hulpverleningszone of mined Dendermonde after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover HVZ Oost VB 1537 / leftover HVZ Fluvia 1547 / leftover HVZ ZWL 1546 / leftover HVZ Noord-Limburg 1545 / leftover HVZ Westhoek 1544 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover HVZ Zuid-Oost / leftover Dijk92 / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Dendermonde>IGS>HVZ_Oost_OVL>JR2025_L5,{ENT},Official zoneraad 22.05.2026 publishes balans 13589234 / resultaat gewone begroting 2011808 / boek gewone 2481692 / buitengewoon begroting -2897489 / boek buit 703832 / pnl nadelig 25226; full rekening 2025 verslag + uitgaven/ontvangsten gewone + pers/werking unpublished; operational VTE unpublished; per-gemeente municipal split unpublished; cash/debt/equity unpublished; BBC M2 unpublished,Leftover IGS hulpverleningszone of mined Dendermonde with live official zoneraad rekening 2025 euros; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; assets 13.59m / resultaat gewone 2.01m / unpublished uitgaven gewone,8,Brandweerzone Oost OVL / dienst openbaarheid,administratie@zoneoost.be,Oude Vest 150 9200 Dendermonde,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1548 leftover IGS hulpverleningszone after honest leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished so leftover IGS with live official zoneraad rekening 2025 euros taken; official besluit PDF. FOI ready not sent. NOT leftover HVZ Oost VB 1537 / leftover HVZ Fluvia 1547 / leftover HVZ ZWL 1546 / leftover HVZ Noord-Limburg 1545 / leftover HVZ Westhoek 1544 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover HVZ Zuid-Oost / leftover Dijk92 / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
foi_path = DATA / "foi_queue.csv"
before = foi_path.stat().st_size
append_lf(foi_path, [foi])
after = foi_path.stat().st_size
if after < before:
    raise SystemExit(f"foi_queue shrank {before} -> {after}")
print("foi_queue +1 append-only", before, "->", after)

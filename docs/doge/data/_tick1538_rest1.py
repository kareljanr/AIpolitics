#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "igs_hvzt"
SRC = "src_hvzt_jr2025_bbc"
GAP = "gap_hvzt_assets_15_68m_expl_470k_rekening_l5"
LB = "lb_hvzt_assets_15_68m_expl_470k_pnl_759k"
COMM = "comm_hvzt_jr2025_assets"
PDF = "https://www.hvztaxandria.be/storage/files/notulen-open-zitting-zr-25-maart-2026-1777898549.pdf"

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
    f"{COMM},HVZ Taxandria JR2025 leftover IGS dual (assets 15.68m / expl 0.47m / PnL PROFIT 0.76m / uitz 0.29m / equity 14.87m / debt 0.81m / begroting gewone 0.62m),{ENT},HVZ Taxandria / dual mined Turnhout + 11 other Taxandria municipalities / municipal + federal civiele-veiligheid,Wet 15.05.2007 civiele veiligheid; KB 19.04.2017 boekhouding hulpverleningszones (as printed in notulen); Bestuursdecreet openbaarheid,2026-03-25,1970,,15684701,,,active,{PDF},Local leftover IGS fire-rescue map VL Turnhout HVZ Taxandria — assets 15.68m / expl 0.47m / PnL PROFIT 0.76m / unpublished full rekening bijlagen,Publish full rekening 2025 bijlagen + pers/VTE + gemeentelijke bijdragen split + cash/omzet + full BBC; do not keep leftover HVZ Taxandria unpublished,{SRC},strong,Vlaanderen>Gemeenten>Turnhout>IGS>HVZ_Taxandria>JR2025_L5,tick1538; assets 15684701 expl 470131 pnl 758780 uitz 288649 equity 14871076 debt 813625 begroting_gewone 622750; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED still unpublished; next every-10 1540"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},HVZ Taxandria JR2025 leftover IGS: assets 15.68m / expl 0.47m / PnL PROFIT 0.76m / equity 14.87m / debt 0.81m / unpublished full rekening bijlagen,L5,local_budget_line,Vlaanderen>Gemeenten>Turnhout>IGS>HVZ_Taxandria>JR2025_L5,15684701,15684701,Leftover dual IGS fire-rescue shell: assets 15.68m / expl 0.47m / PnL PROFIT 0.76m / uitz 0.29m / equity 14.87m / debt 0.81m / begroting gewone 0.62m / pers VTE cash omzet unpublished,strong,{SRC},HVZ Taxandria / dual mined Turnhout + 11 other Taxandria municipalities / municipal + federal civiele-veiligheid,Local leftover IGS fire-rescue map VL Turnhout HVZ Taxandria — JR2025 official zoneraad live; full rekening bijlagen + pers/VTE + city-share FOI,Official zoneraad 2026-08-20: assets 15.68m / expl 0.47m / PnL PROFIT 0.76m / equity 14.87m / unpublished full rekening,7.0,6.8,3.0,6.2,Publish full rekening 2025 bijlagen + pers/VTE + gemeentelijke bijdragen split 12 municipalities + cash/omzet + full BBC; do not keep leftover HVZ Taxandria unpublished,active,,tick1538; leftover IGS hulpverleningszone of mined Turnhout after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Kempen / leftover CAW De Kempen 1526 / leftover CGG Kempen 1516 / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Turnhout>IGS>HVZ_Taxandria>JR2025_L5,{ENT},Zoneraad notulen publish assets 15684701 / expl 470131 / PnL PROFIT 758780 / uitz 288649 / equity 14871076 / debt 813625; full rekening 2025 bijlagen unpublished; pers/VTE unpublished; gemeentelijke bijdragen split 12 municipalities unpublished; cash/omzet/spend unpublished; dual municipal + federal civiele-veiligheid split unpublished,Leftover IGS hulpverleningszone of mined Turnhout with live official JR2025 notulen; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; assets 15.68m / expl 0.47m / PnL PROFIT 0.76m / unpublished full rekening,8,Hulpverleningszone Taxandria / dienst openbaarheid,info@hvztaxandria.be,Noord-Brabantlaan 68 2300 Turnhout,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1538 leftover IGS hulpverleningszone after honest leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished so leftover IGS with live official JR2025 notulen taken; official zoneraad PDF. FOI ready not sent. NOT every-10 (next 1540). NOT leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Kempen / leftover CAW De Kempen 1526 / leftover CGG Kempen 1516 / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

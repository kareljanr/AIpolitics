#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "igs_hvzo"
SRC = "src_hvzo_jr2025_bbc"
GAP = "gap_hvzo_assets_48_14m_expl_4_28m_rekening_l5"
LB = "lb_hvzo_assets_48_14m_expl_4_28m_pnl_3_56m"
COMM = "comm_hvzo_jr2025_assets"
PDF = "https://oost-vlaams-brabant.hulpverleningszone.be/storage/AKwBj1sHddY6KSHKufRCMX9Td2EuKSU8mdaMqknP.pdf"

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
    f"{COMM},HVZ Oost Vlaams-Brabant JR2025 leftover IGS dual (assets 48.14m / expl 4.28m / PnL PROFIT 3.56m / uitz kosten 6.89m / uitz opbr 6.17m / begroting gewone 6.38m),{ENT},HVZ Oost Vlaams-Brabant / dual mined Herent + 31 other Oost-VB municipalities / municipal + federal civiele-veiligheid,Wet 15.05.2007 civiele veiligheid; KB 19.04.2014 boekhouding hulpverleningszones; Bestuursdecreet openbaarheid,2026-04-22,1970,,48137974,,,active,{PDF},Local leftover IGS fire-rescue map VL Herent HVZ Oost — assets 48.14m / expl 4.28m / PnL PROFIT 3.56m / unpublished Rekening_2025_deel_1/2/3,Publish Rekening_2025_deel_1/2/3 + pers/VTE + gemeentelijke bijdragen split + cash/debt + full BBC; do not keep leftover HVZ Oost unpublished,{SRC},strong,Vlaanderen>Gemeenten>Herent>IGS>HVZ_Oost_VB>JR2025_L5,tick1537; assets 48137974 expl 4279776 pnl 3557913 uitz_kosten 6887696 uitz_opbr 6165833 begroting_gewone 6378403 begroting_buitengewoon 1705020; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED still unpublished; next every-10 1540"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},HVZ Oost Vlaams-Brabant JR2025 leftover IGS: assets 48.14m / expl 4.28m / PnL PROFIT 3.56m / uitz kosten 6.89m / unpublished Rekening_2025_deel_1/2/3,L5,local_budget_line,Vlaanderen>Gemeenten>Herent>IGS>HVZ_Oost_VB>JR2025_L5,48137974,48137974,Leftover dual IGS fire-rescue shell: assets 48.14m / expl 4.28m / PnL PROFIT 3.56m / uitz kosten 6.89m / uitz opbr 6.17m / begroting gewone 6.38m / pers VTE cash debt unpublished,strong,{SRC},HVZ Oost Vlaams-Brabant / dual mined Herent + 31 other Oost-VB municipalities / municipal + federal civiele-veiligheid,Local leftover IGS fire-rescue map VL Herent HVZ Oost — JR2025 official zoneraad live; Rekening_2025_deel_1/2/3 + pers/VTE + city-share FOI,Official zoneraad 2026-08-20: assets 48.14m / expl 4.28m / PnL PROFIT 3.56m / uitz kosten 6.89m / unpublished full rekening,7.0,7.2,3.0,6.4,Publish Rekening_2025_deel_1/2/3 + pers/VTE + gemeentelijke bijdragen split 32 municipalities + cash/debt + full BBC; do not keep leftover HVZ Oost unpublished,active,,tick1537; leftover IGS hulpverleningszone of mined Herent after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover Brandweerzone Antwerpen / leftover CAW Oost-Brabant 1530 / leftover CGG VBO 1509 / leftover Kanvaz / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Herent>IGS>HVZ_Oost_VB>JR2025_L5,{ENT},Zoneraad besluit publishes assets 48137974 / expl 4279776 / PnL PROFIT 3557913 / uitz kosten 6887696 / uitz opbr 6165833; Rekening_2025_deel_1/2/3 listed as bijlagen but unpublished (inzage zetel only); pers/VTE unpublished; gemeentelijke bijdragen split 32 municipalities unpublished; cash/debt/equity unpublished; dual municipal + federal civiele-veiligheid split unpublished,Leftover IGS hulpverleningszone of mined Herent with live official JR2025 besluit; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; assets 48.14m / expl 4.28m / PnL PROFIT 3.56m / unpublished full rekening,8,Hulpverleningszone Oost Vlaams-Brabant / dienst openbaarheid,info@hvzoost.be,Spoorwegstraat 6 3020 Herent,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1537 leftover IGS hulpverleningszone after honest leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished so leftover IGS with live official JR2025 besluit taken; official zoneraad PDF. FOI ready not sent. NOT every-10 (next 1540). NOT leftover Brandweerzone Antwerpen / leftover CAW Oost-Brabant 1530 / leftover CGG VBO 1509 / leftover Kanvaz / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

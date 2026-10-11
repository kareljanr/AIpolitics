#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "igs_hvnl"
SRC = "src_hvnl_jr2025_bbc"
GAP = "gap_hvnl_spend_13_88m_pers_10_57m_rekening_l5"
LB = "lb_hvnl_spend_13_88m_pers_10_57m"
COMM = "comm_hvnl_jr2025_spend"
PDF = "https://noord-limburg.hulpverleningszone.be/storage/hq2aZiMeCuVVjDBHkPdi4Ej61GUHrlw84ZTwjDeo.pdf"

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
    f"{COMM},HVZ Noord-Limburg JR2025 leftover IGS dual (spend 13.88m / pers 10.57m / werking 2.83m / toelagen 14.31m / prestaties 0.83m / invest 3.78m),{ENT},HVZ Noord-Limburg / dual mined Lommel + remaining Noord-Limburg municipalities / municipal + federal civiele-veiligheid,Wet 15.05.2007 civiele veiligheid; KB boekhouding hulpverleningszones; Bestuursdecreet openbaarheid,2026-03-18,2025,2025,13883486,,,active,{PDF},Local leftover IGS fire-rescue map VL Lommel HVZ Noord-Limburg — spend 13.88m / pers 10.57m / unpublished full rekening balans,Publish full rekening 2025 verslag + balans + expl/PnL + VTE + per-gemeente toelagen split + cash/debt/equity + full BBC + clarify 450k werking summary vs detail; do not keep leftover HVZ Noord-Limburg unpublished,{SRC},strong,Vlaanderen>Gemeenten>Lommel>IGS>HVZ_NoordLimburg>JR2025_L5,tick1545; uitgaven_gewone 13883486 pers 10572316 werking 2834534 prestaties 834402 werkingstoelagen 14309007 gemeente 8057000 federaal 6252007 invest 3784028; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},HVZ Noord-Limburg JR2025 leftover IGS: spend 13.88m / pers 10.57m / werking 2.83m / toelagen 14.31m / unpublished full rekening balans,L5,local_budget_line,Vlaanderen>Gemeenten>Lommel>IGS>HVZ_NoordLimburg>JR2025_L5,13883486,13883486,Leftover dual IGS fire-rescue shell: spend 13.88m / pers 10.57m / werking 2.83m / toelagen 14.31m gemeente 8.06m federal 6.25m / prestaties 0.83m / invest 3.78m / balans expl PnL VTE cash debt equity unpublished,strong,{SRC},HVZ Noord-Limburg / dual mined Lommel + remaining Noord-Limburg municipalities / municipal + federal civiele-veiligheid,Local leftover IGS fire-rescue map VL Lommel HVZ Noord-Limburg — JR2025 official jaarverslag live; full rekening balans + pers/VTE FOI,Official JV2025 2026-08-20: spend 13.88m / pers 10.57m / toelagen 14.31m / unpublished full rekening,7.2,7.4,3.0,6.3,Publish full rekening 2025 verslag + balans + expl/PnL + VTE + per-gemeente toelagen split + cash/debt/equity + full BBC + clarify 450k werking summary vs detail; do not keep leftover HVZ Noord-Limburg unpublished,active,,tick1545; leftover IGS hulpverleningszone of mined Lommel after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover HVZ Oost-Limburg / leftover CAW Limburg 1531 / leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486 / leftover HVZ Westhoek 1544 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost VB 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Lommel>IGS>HVZ_NoordLimburg>JR2025_L5,{ENT},Official JV2025 publishes uitgaven gewone 13883486 / pers 10572316 / werking detail 2834534 (summary 2384534) / prestaties 834402 / werkingstoelagen 14309007 gemeente 8057000 federaal 6252007 / invest 3784028; full rekening 2025 verslag + balans + expl/PnL unpublished; operational VTE unpublished (admin VTE 19.7 published); per-gemeente split of 8057000 unpublished; cash/debt/equity unpublished; 450k werking summary vs detail unpublished,Leftover IGS hulpverleningszone of mined Lommel with live official JV2025; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; spend 13.88m / pers 10.57m / unpublished full rekening,8,HVZ Noord-Limburg / dienst openbaarheid,info@hvznl.be,Norbert Neeckxlaan 52 bus Z 3920 Lommel,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1545 leftover IGS hulpverleningszone after honest leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished so leftover IGS with live official JV2025 taken; official JV PDF. FOI ready not sent. NOT leftover HVZ Oost-Limburg / leftover CAW Limburg 1531 / leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486 / leftover HVZ Westhoek 1544 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost VB 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
foi_path = DATA / "foi_queue.csv"
before = foi_path.stat().st_size
append_lf(foi_path, [foi])
after = foi_path.stat().st_size
if after < before:
    raise SystemExit(f"foi_queue shrank {before} -> {after}")
print("foi_queue +1 append-only", before, "->", after)

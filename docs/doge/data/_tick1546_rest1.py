#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "igs_hvzwl"
SRC = "src_hvzwl_jr2025_bbc"
GAP = "gap_hvzwl_spend_29_12m_pers_20_93m_rekening_l5"
LB = "lb_hvzwl_spend_29_12m_pers_20_93m"
COMM = "comm_hvzwl_jr2025_spend"
PDF = "https://www.zuidwestlimburg.be/content/documents/01-jaarverslag-2025-hvzzwl.pdf"

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
    f"{COMM},HVZ Zuid-West-Limburg AV2025 leftover IGS dual (spend 29.12m / pers 20.93m / werking 5.78m / gemeente 20.91m / volksgezondheid 4.48m / prestaties 2.29m / invest 4.39m),{ENT},HVZ Zuid-West-Limburg / dual mined Hasselt + remaining ZWL municipalities / municipal + federal civiele-veiligheid,Wet 15.05.2007 civiele veiligheid; KB boekhouding hulpverleningszones; Bestuursdecreet openbaarheid,2026-03-16,2025,2025,29117176,,,active,{PDF},Local leftover IGS fire-rescue map VL Hasselt HVZ ZWL — spend 29.12m / pers 20.93m / unpublished full rekening balans,Publish full rekening 2025 verslag + balans + expl/PnL + VTE + remainder of 32.63m overdrachten/subsidies after gemeente 20.91m and Volksgezondheid 4.48m + cash/debt/equity + full BBC; do not keep leftover HVZ Zuid-West-Limburg unpublished,{SRC},strong,Vlaanderen>Gemeenten>Hasselt>IGS>HVZ_ZuidWestLimburg>JR2025_L5,tick1546; uitgaven_gewone 29117176 pers 20930221 werking 5782142 overdrachten 676531 schuld 1728282 gemeente 20908513 volksgezondheid 4478255 prestaties 2291333 invest 4393168 ontvangsten 35360400; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},HVZ Zuid-West-Limburg AV2025 leftover IGS: spend 29.12m / pers 20.93m / werking 5.78m / gemeente 20.91m / unpublished full rekening balans,L5,local_budget_line,Vlaanderen>Gemeenten>Hasselt>IGS>HVZ_ZuidWestLimburg>JR2025_L5,29117176,29117176,Leftover dual IGS fire-rescue shell: spend 29.12m / pers 20.93m / werking 5.78m / gemeente 20.91m (Hasselt 5.47m) / Volksgezondheid 4.48m / prestaties 2.29m / invest 4.39m / balans expl PnL VTE cash debt equity unpublished,strong,{SRC},HVZ Zuid-West-Limburg / dual mined Hasselt + remaining ZWL municipalities / municipal + federal civiele-veiligheid,Local leftover IGS fire-rescue map VL Hasselt HVZ ZWL — AV2025 official activiteitenrapport live; full rekening balans + pers/VTE FOI,Official AV2025 2026-08-20: spend 29.12m / pers 20.93m / gemeente 20.91m / unpublished full rekening,7.2,7.6,3.0,6.4,Publish full rekening 2025 verslag + balans + expl/PnL + VTE + remainder of 32.63m overdrachten/subsidies after gemeente 20.91m and Volksgezondheid 4.48m + cash/debt/equity + full BBC; do not keep leftover HVZ Zuid-West-Limburg unpublished,active,,tick1546; leftover IGS hulpverleningszone of mined Hasselt after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover HVZ Noord-Limburg 1545 / leftover HVZ Oost-Limburg / leftover CAW Limburg 1531 / leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486 / leftover LeefGoed 1481 / leftover HVZ Westhoek 1544 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost VB 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Hasselt>IGS>HVZ_ZuidWestLimburg>JR2025_L5,{ENT},Official AV2025 publishes uitgaven gewone 29117176 / pers 20930221 / werking 5782142 / overdrachten 676531 / schuld 1728282 / gemeente 20908513 / Volksgezondheid 4478255 / prestaties 2291333 / invest 4393168 / ontvangsten 35360400; full rekening 2025 verslag + balans + expl/PnL unpublished (zoneraad 16.03.2026 named Goedkeuring rekening 2025 only); operational VTE unpublished (640 medewerkers published); remainder of 32626534 overdrachten/subsidies after gemeente and Volksgezondheid unpublished; cash/debt/equity unpublished,Leftover IGS hulpverleningszone of mined Hasselt with live official AV2025; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; spend 29.12m / pers 20.93m / unpublished full rekening,8,HVZ Zuid-West Limburg / dienst openbaarheid,brandweer@zuidwestlimburg.be,Zwarte-Brugstraat 1 3500 Hasselt,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1546 leftover IGS hulpverleningszone after honest leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished so leftover IGS with live official AV2025 taken; official AV PDF. FOI ready not sent. NOT leftover HVZ Noord-Limburg 1545 / leftover HVZ Oost-Limburg / leftover CAW Limburg 1531 / leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486 / leftover LeefGoed 1481 / leftover HVZ Westhoek 1544 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost VB 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
foi_path = DATA / "foi_queue.csv"
before = foi_path.stat().st_size
append_lf(foi_path, [foi])
after = foi_path.stat().st_size
if after < before:
    raise SystemExit(f"foi_queue shrank {before} -> {after}")
print("foi_queue +1 append-only", before, "->", after)

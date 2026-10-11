#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "igs_hvzf"
SRC = "src_hvzf_jr2025_bbc"
GAP = "gap_hvzf_spend_20_24m_pers_15_46m_rekening_l5"
LB = "lb_hvzf_spend_20_24m_pers_15_46m"
COMM = "comm_hvzf_jr2025_spend"
PDF = "https://www.brandweerfluvia.be/media/597/download?attachment"

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
    f"{COMM},HVZ Fluvia AV2025 leftover IGS dual (spend 20.24m / pers 15.46m / werking 4.65m / gemeente 11.65m / fed 7.78m / prestaties 1.84m / invest 1.60m / buitengewoon 3.87m),{ENT},HVZ Fluvia / dual mined Kortrijk + remaining Fluvia municipalities / municipal + federal civiele-veiligheid,Wet 15.05.2007 civiele veiligheid; KB boekhouding hulpverleningszones; Bestuursdecreet openbaarheid,2026-04-02,2025,2025,20237541,,,active,{PDF},Local leftover IGS fire-rescue map VL Kortrijk HVZ Fluvia — spend 20.24m / pers 15.46m / unpublished full rekening balans,Publish full rekening 2025 verslag + balans + expl/PnL + VTE + per-gemeente split of 11.65m gemeente + cash/debt/equity + full BBC M2; do not keep leftover HVZ Fluvia unpublished,{SRC},strong,Vlaanderen>Gemeenten>Kortrijk>IGS>HVZ_Fluvia>JR2025_L5,tick1547; uitgaven_gewone 20237541 pers 15462341 werking 4652717 overdrachten 122484 ontvangsten 21496867 gemeente 11650000 fed_bw 4684000 fed_dgh 3091000 prestaties 1837568 invest 1598798 buitengewoon 3872440; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},HVZ Fluvia AV2025 leftover IGS: spend 20.24m / pers 15.46m / werking 4.65m / gemeente 11.65m / unpublished full rekening balans,L5,local_budget_line,Vlaanderen>Gemeenten>Kortrijk>IGS>HVZ_Fluvia>JR2025_L5,20237541,20237541,Leftover dual IGS fire-rescue shell: spend 20.24m / pers 15.46m / werking 4.65m / gemeente 11.65m / fed BW 4.68m / fed DGH 3.09m / prestaties 1.84m / invest 1.60m / buitengewoon 3.87m / balans expl PnL VTE cash debt equity unpublished,strong,{SRC},HVZ Fluvia / dual mined Kortrijk + remaining Fluvia municipalities / municipal + federal civiele-veiligheid,Local leftover IGS fire-rescue map VL Kortrijk HVZ Fluvia — AV2025 official activiteitenverslag live; full rekening balans + pers/VTE FOI,Official AV2025 2026-08-20: spend 20.24m / pers 15.46m / gemeente 11.65m / unpublished full rekening,7.2,7.5,3.0,6.3,Publish full rekening 2025 verslag + balans + expl/PnL + VTE + per-gemeente split of 11.65m gemeente + cash/debt/equity + full BBC M2; do not keep leftover HVZ Fluvia unpublished,active,,tick1547; leftover IGS hulpverleningszone of mined Kortrijk after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover HVZ Westhoek 1544 / leftover HVZ1 1539 / leftover HVZ Midwest 1541 / leftover CAW ZWVL 1534 / leftover CGG Mandel en Leie 1522 / leftover HVZ ZWL 1546 / leftover HVZ Noord-Limburg 1545 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Meetjesland 1540 / leftover HVZ Taxandria 1538 / leftover HVZ Oost VB 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Kortrijk>IGS>HVZ_Fluvia>JR2025_L5,{ENT},Official AV2025 publishes uitgaven gewone 20237541 / pers 15462341 / werking 4652717 / overdrachten 122484 / ontvangsten 21496867 / gemeente 11650000 / fed BW 4684000 / fed DGH 3091000 / prestaties 1837568 / invest 1598798 / buitengewoon 3872440 / resultaat gewone 5368924; full rekening 2025 verslag + balans + expl/PnL unpublished; operational VTE unpublished (771 medewerkers published); per-gemeente split of 11.65m gemeente unpublished; cash/debt/equity unpublished; BBC M2 schema image-only,Leftover IGS hulpverleningszone of mined Kortrijk with live official AV2025; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; spend 20.24m / pers 15.46m / unpublished full rekening,8,Brandweer Fluvia / dienst openbaarheid,info@hvzfluvia.be,Doorniksesteenweg 214 bus A 8500 Kortrijk,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1547 leftover IGS hulpverleningszone after honest leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished so leftover IGS with live official AV2025 taken; official AV PDF. FOI ready not sent. NOT leftover HVZ Westhoek 1544 / leftover HVZ1 1539 / leftover HVZ Midwest 1541 / leftover CAW ZWVL 1534 / leftover CGG Mandel en Leie 1522 / leftover HVZ ZWL 1546 / leftover HVZ Noord-Limburg 1545 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Meetjesland 1540 / leftover HVZ Taxandria 1538 / leftover HVZ Oost VB 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
foi_path = DATA / "foi_queue.csv"
before = foi_path.stat().st_size
append_lf(foi_path, [foi])
after = foi_path.stat().st_size
if after < before:
    raise SystemExit(f"foi_queue shrank {before} -> {after}")
print("foi_queue +1 append-only", before, "->", after)

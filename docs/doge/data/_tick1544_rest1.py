#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "igs_hvwh"
SRC = "src_hvwh_jr2025_bbc"
GAP = "gap_hvwh_spend_17_51m_pers_13_08m_rekening_l5"
LB = "lb_hvwh_spend_17_51m_pers_13_08m"
COMM = "comm_hvwh_jr2025_spend"
PDF = "https://brandweerwesthoek.be/wp-content/uploads/2026/06/2025-Activiteitenverslag-Brandweer-Westhoek_LR.pdf"

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
    f"{COMM},HVZ Westhoek JR2025 leftover IGS dual (spend 17.51m / pers 13.08m / werking 4.43m / toelagen 18.49m / prestaties 1.49m / invest 2.78m),{ENT},HVZ Westhoek / dual mined Koksijde + remaining Westhoek municipalities / municipal + federal civiele-veiligheid,Wet 15.05.2007 civiele veiligheid; KB boekhouding hulpverleningszones; Bestuursdecreet openbaarheid,2026-05-05,2025,2025,17511626,,,active,{PDF},Local leftover IGS fire-rescue map VL Koksijde HVZ Westhoek — spend 17.51m / pers 13.08m / unpublished full rekening balans,Publish full rekening 2025 verslag + balans + expl/PnL + VTE + gemeentelijk vs federal toelagen split + cash/debt/equity + full BBC; do not keep leftover HVZ Westhoek unpublished,{SRC},strong,Vlaanderen>Gemeenten>Koksijde>IGS>HVZ_Westhoek>JR2025_L5,tick1544; uitgaven_gewone 17511626 pers 13083164 werking 4428462 prestaties 1493651 werkingstoelagen 18487764 invest 2782545; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},HVZ Westhoek JR2025 leftover IGS: spend 17.51m / pers 13.08m / werking 4.43m / toelagen 18.49m / unpublished full rekening balans,L5,local_budget_line,Vlaanderen>Gemeenten>Koksijde>IGS>HVZ_Westhoek>JR2025_L5,17511626,17511626,Leftover dual IGS fire-rescue shell: spend 17.51m / pers 13.08m / werking 4.43m / toelagen 18.49m / prestaties 1.49m / invest 2.78m / balans expl PnL VTE cash debt equity unpublished,strong,{SRC},HVZ Westhoek / dual mined Koksijde + remaining Westhoek municipalities / municipal + federal civiele-veiligheid,Local leftover IGS fire-rescue map VL Koksijde HVZ Westhoek — JR2025 official activiteitenverslag live; full rekening balans + pers/VTE FOI,Official AV2025 2026-08-20: spend 17.51m / pers 13.08m / toelagen 18.49m / unpublished full rekening,7.2,7.5,3.0,6.4,Publish full rekening 2025 verslag + balans + expl/PnL + VTE + gemeentelijk vs federal toelagen split + cash/debt/equity + full BBC; do not keep leftover HVZ Westhoek unpublished,active,,tick1544; leftover IGS hulpverleningszone of mined Koksijde after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover HVZ Fluvia / leftover HVZ1 1539 / leftover CAW NWVL 1535 / leftover DVV Westhoek / leftover RL Westhoek / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Koksijde>IGS>HVZ_Westhoek>JR2025_L5,{ENT},Official AV2025 publishes uitgaven gewone 17511626 / pers 13083164 / werking 4428462 / prestaties 1493651 / werkingstoelagen 18487764 / invest 2782545; full rekening 2025 verslag + balans + expl/PnL unpublished; VTE unpublished; gemeentelijk vs federal toelagen split unpublished; cash/debt/equity unpublished; dual municipal + federal civiele-veiligheid split unpublished,Leftover IGS hulpverleningszone of mined Koksijde with live official AV2025; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; spend 17.51m / pers 13.08m / unpublished full rekening,8,Brandweer Westhoek / dienst openbaarheid,info@brandweerwesthoek.be,Zeelaan 37 8670 Koksijde,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1544 leftover IGS hulpverleningszone after honest leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished so leftover IGS with live official AV2025 taken; official AV PDF. FOI ready not sent. NOT leftover HVZ Fluvia / leftover HVZ1 1539 / leftover CAW NWVL 1535 / leftover DVV Westhoek / leftover RL Westhoek / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
foi_path = DATA / "foi_queue.csv"
before = foi_path.stat().st_size
append_lf(foi_path, [foi])
after = foi_path.stat().st_size
if after < before:
    raise SystemExit(f"foi_queue shrank {before} -> {after}")
print("foi_queue +1 append-only", before, "->", after)

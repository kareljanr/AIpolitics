#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "igs_hvmw"
SRC = "src_hvmw_jr2025_bbc"
GAP = "gap_hvmw_assets_20_27m_expl_795k_pnl_loss_l5"
LB = "lb_hvmw_assets_20_27m_expl_795k_pnl_loss"
COMM = "comm_hvmw_jr2025_assets"
PDF = "https://zonemidwest.be/uploads/files/Zoneraad/Verslagen/2026/Zoneraad-op-vrijdag-27-maart-2026-Overzicht-beslissingen-website.pdf"

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
    f"{COMM},HVZ Midwest JR2025 leftover IGS dual (assets 20.27m / expl 0.79m / PnL LOSS 0.26m / uitz LOSS 1.05m / equity 18.80m / debt 1.46m / vastgelegd gewone 14.80m),{ENT},HVZ Midwest / dual mined Roeselare + remaining Midwest municipalities / municipal + federal civiele-veiligheid,Wet 15.05.2007 civiele veiligheid; KB 19.04.2014 boekhouding hulpverleningszones (as printed); Bestuursdecreet openbaarheid,2026-03-27,1970,,20266035,,,active,{PDF},Local leftover IGS fire-rescue map VL Roeselare HVZ Midwest — assets 20.27m / expl 0.79m / PnL LOSS 0.26m / unpublished full rekening verslag,Publish full rekening 2025 verslag + pers/VTE + gemeentelijke bijdragen split + cash/omzet + full BBC; do not keep leftover HVZ Midwest unpublished,{SRC},strong,Vlaanderen>Gemeenten>Roeselare>IGS>HVZ_Midwest>JR2025_L5,tick1541; assets 20266035 expl 794672 pnl -257322 uitz -1051994 equity 18804221 debt 1461814 vastgelegd_gewone 14801789; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep/Dijk92/IOED still unpublished"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},HVZ Midwest JR2025 leftover IGS: assets 20.27m / expl 0.79m / PnL LOSS 0.26m / equity 18.80m / debt 1.46m / unpublished full rekening verslag,L5,local_budget_line,Vlaanderen>Gemeenten>Roeselare>IGS>HVZ_Midwest>JR2025_L5,20266035,20266035,Leftover dual IGS fire-rescue shell: assets 20.27m / expl 0.79m / PnL LOSS 0.26m / uitz LOSS 1.05m / equity 18.80m / debt 1.46m / vastgelegd gewone 14.80m / pers VTE cash omzet unpublished,strong,{SRC},HVZ Midwest / dual mined Roeselare + remaining Midwest municipalities / municipal + federal civiele-veiligheid,Local leftover IGS fire-rescue map VL Roeselare HVZ Midwest — JR2025 official zoneraad live; full rekening verslag + pers/VTE + city-share FOI,Official zoneraad 2026-08-20: assets 20.27m / expl 0.79m / PnL LOSS 0.26m / equity 18.80m / unpublished full rekening,7.0,7.2,3.0,6.3,Publish full rekening 2025 verslag + pers/VTE + gemeentelijke bijdragen split Midwest municipalities + cash/omzet + full BBC; do not keep leftover HVZ Midwest unpublished,active,,tick1541; leftover IGS hulpverleningszone of mined Roeselare after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Kempen / leftover HVZ Fluvia / leftover DVV Midwest / leftover Thuiswest 1493 / leftover Motena Roeselare / leftover CGG Largo 1518 / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Roeselare>IGS>HVZ_Midwest>JR2025_L5,{ENT},Zoneraad overzicht publish assets 20266035 / expl 794672 / PnL LOSS 257322 / uitz LOSS 1051994 / equity 18804221 / debt 1461814; full rekening 2025 verslag + begrotingsrekening presentatie unpublished; pers/VTE unpublished; gemeentelijke bijdragen split unpublished; cash/omzet/uitgaven gewone unpublished; dual municipal + federal civiele-veiligheid split unpublished,Leftover IGS hulpverleningszone of mined Roeselare with live official JR2025 zoneraad overzicht; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick; assets 20.27m / expl 0.79m / PnL LOSS 0.26m / unpublished full rekening,8,Hulpverleningszone Midwest / dienst openbaarheid,info@zonemidwest.be,Kwadestraat 159 8800 Roeselare,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1541 leftover IGS hulpverleningszone after honest leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished so leftover IGS with live official JR2025 zoneraad overzicht taken; official zoneraad PDF. FOI ready not sent. NOT leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Kempen / leftover HVZ Fluvia / leftover DVV Midwest / leftover Thuiswest 1493 / leftover Motena Roeselare / leftover CGG Largo 1518 / leftover Erfpunt 1536 / leftover IVAREM 1524 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
foi_path = DATA / "foi_queue.csv"
before = foi_path.stat().st_size
append_lf(foi_path, [foi])
after = foi_path.stat().st_size
if after < before:
    raise SystemExit(f"foi_queue shrank {before} -> {after}")
print("foi_queue +1 append-only", before, "->", after)

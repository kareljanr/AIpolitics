#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()
ENT = "igs_erfp"
SRC = "src_erfp_jr2025_nbb"
GAP = "gap_erfp_bruto_701k_pers_678k_pnl_loss_l5"
LB = "lb_erfp_bruto_701k_pers_678k_pnl_loss"
COMM = "comm_erfp_jr2025_bruto"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00165556.pdf"

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
    f"{COMM},Erfpunt JR2025 leftover IOED dual (bruto 701k / pers 678k 7.8 VTE / expl PROFIT 8.7k / PnL LOSS 929 / cash DROP 61k / handelsrecv JUMP 192k / lev JUMP 105k),{ENT},Erfpunt / dual mined Sint-Niklaas + remaining Waasland municipalities / Onroerend Erfgoed subsidies,WVV projectvereniging; Decreet intergemeentelijke samenwerking; Bestuursdecreet openbaarheid,2026-06-11,1970,,700561,,,active,{PDF},Local leftover IOED map VL Sint-Niklaas Erfpunt — bruto 701k / pers 678k 7.8 VTE / PnL LOSS 929 / cash DROP 61k / handelsrecv JUMP 192k / lev JUMP 105k,Publish omzet 70 empty + 60/61 empty + city vs Onroerend Erfgoed split + handelsrecv JUMP + lev JUMP + cash DROP + beleg DROP + prepaid JUMP + pers 62 vs social 102; do not keep leftover Erfpunt unpublished,{SRC},strong,Vlaanderen>Gemeenten>Sint-Niklaas>IOED>Erfpunt>JR2025_L5,tick1536; assets 438711 omzet empty bruto 700561 pers 677959 7.8 VTE pnl -929 equity 140814 cash 61449 debt 297897 capex 29009 dividend 0 commissaris none; FOI ready not sent; not TE-additive of 348bn; leftover AGB/Bosgroep still unpublished; next every-10 1540"
)
check(comm, 19, "commitments")
append_lf(DATA / "commitments.csv", [comm])
print("commitments +1")

lb = (
    f"{LB},Erfpunt JR2025 leftover IOED: bruto 701k / pers 678k 7.8 VTE / expl PROFIT 8.7k / PnL LOSS 929 / cash DROP 61k / handelsrecv JUMP 192k / lev JUMP 105k,L5,local_budget_line,Vlaanderen>Gemeenten>Sint-Niklaas>IOED>Erfpunt>JR2025_L5,700561,438711,Leftover dual IOED shell: assets 0.44m / equity 0.14m / bruto 0.70m / pers 0.68m 7.8 VTE / cash 61k DROP / handelsrecv 192k JUMP / lev 105k JUMP / expl PROFIT 8.7k / debt 0.30m / PnL LOSS 929,strong,{SRC},Erfpunt / dual mined Sint-Niklaas + remaining Waasland municipalities / Onroerend Erfgoed subsidies,Local leftover IOED map VL Sint-Niklaas Erfpunt — JR2025 official NBB WVV live; omzet empty + handelsrecv JUMP + lev JUMP + cash DROP FOI,Official NBB WVV 2026-08-20: bruto 701k / pers 678k 7.8 VTE / cash DROP 61k / handelsrecv JUMP 192k / PnL LOSS 929,6.6,5.2,2.0,5.1,Publish omzet 70 empty + 60/61 empty + city vs Onroerend Erfgoed split + handelsrecv JUMP 191912 was 52934 + lev JUMP 105313 was 13892 + cash DROP 61449 was 110060 + beleg DROP 117476 + prepaid JUMP 11350 + pers 62 677959 vs social 102 653291; do not keep leftover Erfpunt unpublished,active,,tick1536; leftover recognized IOED of mined Sint-Niklaas after leftover AGB/APB/Bosgroep/CAW hunt; leftover AGB/Bosgroep still unpublished this tick; FOI ready not sent; not TE-additive of 348bn; distinct from leftover Erfgoed Denderland / leftover Erfgoed Voorkempen / leftover Erfgoed Noorderkempen / leftover Woonpunt Waas / leftover WoonST Temse / leftover Dimensa / leftover IVAREM / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(lb, 21, "leaderboard")
append_lf(DATA / "leaderboard.csv", [lb])
print("leaderboard +1")

foi = (
    f"{GAP},Vlaanderen>Gemeenten>Sint-Niklaas>IOED>Erfpunt>JR2025_L5,{ENT},VKT-kap publishes bruto 700561 (omzet 70 empty; 60/61 empty); city vs Onroerend Erfgoed / gemeentelijke bijdragen split unpublished; handelsrecv JUMP 191912 was 52934; lev JUMP 105313 was 13892; cash DROP 61449 was 110060; beleg DROP 117476 was 140641; prepaid JUMP 11350 was empty; pers 62 677959 vs social 102 653291; no commissaris; dual city/Onroerend Erfgoed split unpublished,Leftover recognized IOED / leftover IGS projectvereniging of mined Sint-Niklaas with live JR2025; leftover AGB/Bosgroep still unpublished this tick; annual envelope 701k bruto / pers 678k 7.8 VTE / PnL LOSS 929 / cash DROP 61k / assets 439k,8,Erfpunt / dienst openbaarheid,admin@erfpunt.be,Regentiestraat 63 9100 Sint-Niklaas,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-20,,,,,{COMM},{LB},{TS},{TS},tick1536 leftover recognized IOED after honest leftover AGB/APB/Bosgroep/CAW hunt; leftover AGB/Bosgroep still unpublished so leftover IOED with live JR2025 taken; official NBB WVV PDF. FOI ready not sent. NOT every-10 (next 1540). NOT leftover Erfgoed Denderland / leftover Erfgoed Voorkempen / leftover Erfgoed Noorderkempen / leftover Woonpunt Waas / leftover WoonST Temse / leftover Dimensa / leftover IVAREM / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
)
check(foi, 21, "foi_queue")
append_lf(DATA / "foi_queue.csv", [foi])
print("foi_queue +1")

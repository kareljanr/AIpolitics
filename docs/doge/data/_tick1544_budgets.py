#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvwh"
SRC = "src_hvwh_jr2025_bbc"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_hvwh_uitgaven_gewone_2025,{ENT},2025,17511626,,,executed,{SRC},strong,2025 uitgaven gewone 17511626 envelope (pers 13083164 + werking 4428462; PDF 13083163.73 / 4428462.23 rounded); tick1544; primary official AV2025 05.05.2026; 1539/1542/1543 spend pattern",
    f"bud_hvwh_pers_2025,{ENT},2025,13083164,,,executed,{SRC},strong,2025 personeelskosten 13083164 (PDF 13083163.73 rounded); tick1544; primary official AV2025 05.05.2026",
    f"bud_hvwh_werking_2025,{ENT},2025,4428462,,,executed,{SRC},strong,2025 werkingskosten 4428462 (PDF 4428462.23 rounded); tick1544; primary official AV2025 05.05.2026",
    f"bud_hvwh_prestaties_2025,{ENT},2025,1493651,,,executed,{SRC},strong,2025 ontvangsten prestaties 1493651 (PDF 1493651.00); tick1544; primary official AV2025 05.05.2026",
    f"bud_hvwh_werkingstoelagen_2025,{ENT},2025,18487764,,,executed,{SRC},strong,2025 werkingstoelagen 18487764 (PDF 18487763.90 rounded; gemeentelijk + federal split unpublished FOI); tick1544; primary official AV2025 05.05.2026",
    f"bud_hvwh_invest_2025,{ENT},2025,2782545,,,executed,{SRC},strong,2025 investeringen uitrusting en voertuigen 2782545 (PDF 2782544.98 rounded); tick1544; primary official AV2025 05.05.2026",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

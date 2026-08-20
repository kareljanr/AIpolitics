#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvzo"
SRC = "src_hvzo_jr2025_bbc"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_hvzo_assets_2025,{ENT},2025,48137974,,,executed,{SRC},strong,2025 balanstotaal actief=passief 48137974; tick1537; primary official zoneraad JR2025 besluit 2026_ZR_00026",
    f"bud_hvzo_expl_2025,{ENT},2025,4279776,,,executed,{SRC},strong,2025 batig exploitatieresultaat 4279776; tick1537; primary official zoneraad JR2025 besluit 2026_ZR_00026",
    f"bud_hvzo_uitzkost_2025,{ENT},2025,6887696,,,executed,{SRC},strong,2025 uitzonderlijke kosten en toevoeging aan reserves 6887696; tick1537; primary official zoneraad JR2025 besluit 2026_ZR_00026",
    f"bud_hvzo_uitzopbr_2025,{ENT},2025,6165833,,,executed,{SRC},strong,2025 uitzonderlijke opbrengsten en afname van reserves 6165833; tick1537; primary official zoneraad JR2025 besluit 2026_ZR_00026",
    f"bud_hvzo_pnl_2025,{ENT},2025,3557913,,,executed,{SRC},strong,2025 batig resultaat 3557913 PROFIT (4279776 - 6887696 + 6165833); tick1537; primary official zoneraad JR2025 besluit 2026_ZR_00026",
    f"bud_hvzo_begroting_gewone_2025,{ENT},2025,6378403,,,executed,{SRC},strong,2025 begrotingsresultaat gewone dienst 6378403 (PDF 6378403.26 rounded); tick1537; primary official zoneraad JR2025 besluit 2026_ZR_00026",
    f"bud_hvzo_begroting_buitengewoon_2025,{ENT},2025,1705020,,,executed,{SRC},strong,2025 begrotingsresultaat buitengewone dienst 1705020 (PDF 1705019.56 rounded); tick1537; primary official zoneraad JR2025 besluit 2026_ZR_00026",
    f"bud_hvzo_boek_gewone_2025,{ENT},2025,8274796,,,executed,{SRC},strong,2025 boekhoudkundig resultaat gewone dienst 8274796 (PDF 8274796.34 rounded); tick1537; primary official zoneraad JR2025 besluit 2026_ZR_00026",
    f"bud_hvzo_boek_buitengewoon_2025,{ENT},2025,7935784,,,executed,{SRC},strong,2025 boekhoudkundig resultaat buitengewone dienst 7935784 (PDF 7935783.99 rounded); tick1537; primary official zoneraad JR2025 besluit 2026_ZR_00026",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

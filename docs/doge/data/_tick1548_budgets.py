#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvoo"
SRC = "src_hvoo_jr2025_bbc"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_hvoo_assets_2025,{ENT},2025,13589234,,,executed,{SRC},strong,2025 balanstotaal actief=passief 13589234 envelope (PDF 13589234.41 rounded); tick1548; primary official zoneraad 22.05.2026; 1537/1538/1540/1541 balanstotaal pattern (uitgaven gewone unpublished)",
    f"bud_hvoo_begroting_gewone_2025,{ENT},2025,2011808,,,executed,{SRC},strong,2025 begrotingsresultaat gewone dienst 2011808 PROFIT (PDF 2011808.33 rounded); tick1548; primary official zoneraad 22.05.2026",
    f"bud_hvoo_boek_gewone_2025,{ENT},2025,2481692,,,executed,{SRC},strong,2025 boekhoudkundig resultaat gewone dienst 2481692 PROFIT (PDF 2481692.46 rounded); tick1548; primary official zoneraad 22.05.2026",
    f"bud_hvoo_begroting_buitengewoon_2025,{ENT},2025,-2897489,,,executed,{SRC},strong,2025 begrotingsresultaat buitengewone dienst -2897489 LOSS (PDF -2897488.75 rounded); tick1548; primary official zoneraad 22.05.2026",
    f"bud_hvoo_boek_buitengewoon_2025,{ENT},2025,703832,,,executed,{SRC},strong,2025 boekhoudkundig resultaat buitengewone dienst 703832 PROFIT (PDF 703832.42 rounded); tick1548; primary official zoneraad 22.05.2026",
    f"bud_hvoo_pnl_2025,{ENT},2025,-25226,,,executed,{SRC},strong,2025 resultatenrekening nadelig resultaat -25226 LOSS (PDF 25226.13 nadelig); tick1548; primary official zoneraad 22.05.2026",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

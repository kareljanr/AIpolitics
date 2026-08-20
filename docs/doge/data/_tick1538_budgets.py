#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvzt"
SRC = "src_hvzt_jr2025_bbc"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_hvzt_assets_2025,{ENT},2025,15684701,,,executed,{SRC},strong,2025 balanstotaal actief=passief 15684701 (PDF 15684701.04 rounded); tick1538; primary official zoneraad JR2025 notulen 2026_ZR_00053",
    f"bud_hvzt_vlottend_2025,{ENT},2025,3934714,,,executed,{SRC},strong,2025 vlottende activa 3934714 (PDF 3934714.42 rounded); tick1538; primary official zoneraad JR2025 notulen 2026_ZR_00053",
    f"bud_hvzt_vast_2025,{ENT},2025,11749987,,,executed,{SRC},strong,2025 vaste activa 11749987 (PDF 11749986.62 rounded); tick1538; primary official zoneraad JR2025 notulen 2026_ZR_00053",
    f"bud_hvzt_debt_2025,{ENT},2025,813625,,,executed,{SRC},strong,2025 schulden 813625 (PDF 813624.60 rounded); tick1538; primary official zoneraad JR2025 notulen 2026_ZR_00053",
    f"bud_hvzt_equity_2025,{ENT},2025,14871076,,,executed,{SRC},strong,2025 eigen vermogen 14871076 (PDF 14871076.44 rounded); tick1538; primary official zoneraad JR2025 notulen 2026_ZR_00053",
    f"bud_hvzt_expl_2025,{ENT},2025,470131,,,executed,{SRC},strong,2025 batig exploitatieresultaat 470131 PROFIT (PDF 470131.11 rounded); tick1538; primary official zoneraad JR2025 notulen 2026_ZR_00053",
    f"bud_hvzt_uitz_2025,{ENT},2025,288649,,,executed,{SRC},strong,2025 batig uitzonderlijk resultaat 288649 (PDF 288648.51 rounded); tick1538; primary official zoneraad JR2025 notulen 2026_ZR_00053",
    f"bud_hvzt_pnl_2025,{ENT},2025,758780,,,executed,{SRC},strong,2025 batig resultaat boekjaar 758780 PROFIT (470131 + 288649); tick1538; primary official zoneraad JR2025 notulen 2026_ZR_00053",
    f"bud_hvzt_begroting_gewone_2025,{ENT},2025,622750,,,executed,{SRC},strong,2025 begrotingsresultaat gewone dienst 622750 (PDF 622750.26 rounded); tick1538; primary official zoneraad JR2025 notulen 2026_ZR_00053",
    f"bud_hvzt_begroting_buitengewoon_2025,{ENT},2025,388498,,,executed,{SRC},strong,2025 begrotingsresultaat buitengewone dienst 388498 (PDF 388498.41 rounded); tick1538; primary official zoneraad JR2025 notulen 2026_ZR_00053",
    f"bud_hvzt_boek_gewone_2025,{ENT},2025,856437,,,executed,{SRC},strong,2025 boekhoudkundig resultaat gewone dienst 856437 (PDF 856437.40 rounded); tick1538; primary official zoneraad JR2025 notulen 2026_ZR_00053",
    f"bud_hvzt_boek_buitengewoon_2025,{ENT},2025,2264652,,,executed,{SRC},strong,2025 boekhoudkundig resultaat buitengewone dienst 2264652 (PDF 2264652.42 rounded); tick1538; primary official zoneraad JR2025 notulen 2026_ZR_00053",
    f"bud_hvzt_vastleggingen_gewone_2025,{ENT},2025,233687,,,executed,{SRC},strong,2025 over te dragen vastleggingen gewone dienst 233687 (PDF 233687.14 rounded); tick1538; primary official zoneraad JR2025 notulen 2026_ZR_00053",
    f"bud_hvzt_vastleggingen_buitengewoon_2025,{ENT},2025,1876154,,,executed,{SRC},strong,2025 over te dragen vastleggingen buitengewone dienst 1876154 (PDF 1876154.01 rounded); tick1538; primary official zoneraad JR2025 notulen 2026_ZR_00053",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

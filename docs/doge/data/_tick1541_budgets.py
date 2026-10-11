#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvmw"
SRC = "src_hvmw_jr2025_bbc"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_hvmw_assets_2025,{ENT},2025,20266035,,,executed,{SRC},strong,2025 balanstotaal actief=passief 20266035 (PDF 20266035.14 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_vast_2025,{ENT},2025,9609770,,,executed,{SRC},strong,2025 vaste activa 9609770 (PDF 9609769.85 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_vlottend_2025,{ENT},2025,10656265,,,executed,{SRC},strong,2025 vlottende activa 10656265 (PDF 10656265.29 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_equity_2025,{ENT},2025,18804221,,,executed,{SRC},strong,2025 eigen vermogen 18804221 (PDF 18804220.79 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_debt_2025,{ENT},2025,1461814,,,executed,{SRC},strong,2025 schulden 1461814 (PDF 1461814.35 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_expl_2025,{ENT},2025,794672,,,executed,{SRC},strong,2025 exploitatieresultaat 794672 PROFIT (PDF 794672.48 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_uitz_2025,{ENT},2025,-1051994,,,executed,{SRC},strong,2025 uitzonderlijk resultaat -1051994 LOSS (PDF -1051994.07 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_pnl_2025,{ENT},2025,-257322,,,executed,{SRC},strong,2025 resultaat dienstjaar -257322 LOSS (PDF -257321.59 rounded; 794672 + -1051994); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_rechten_gewone_2025,{ENT},2025,20387479,,,executed,{SRC},strong,2025 netto vastgestelde rechten gewone dienst 20387479 (PDF 20387479.37 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_vastgelegd_gewone_2025,{ENT},2025,14801789,,,executed,{SRC},strong,2025 vastgelegde uitgaven gewone dienst 14801789 (PDF 14801789.23 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_begroting_gewone_2025,{ENT},2025,5585690,,,executed,{SRC},strong,2025 begrotingsresultaat gewone dienst 5585690 (PDF 5585690.14 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_carry_gewone_2025,{ENT},2025,162647,,,executed,{SRC},strong,2025 over te dragen vastgelegde uitgaven gewone dienst 162647 (PDF 162646.68 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_boek_gewone_2025,{ENT},2025,5748337,,,executed,{SRC},strong,2025 boekhoudkundig resultaat gewone dienst 5748337 (PDF 5748336.82 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_rechten_buitengewoon_2025,{ENT},2025,4933915,,,executed,{SRC},strong,2025 netto vastgestelde rechten buitengewone dienst 4933915 (PDF 4933914.96 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_vastgelegd_buitengewoon_2025,{ENT},2025,4822390,,,executed,{SRC},strong,2025 vastgelegde uitgaven buitengewone dienst 4822390 (PDF 4822390.00); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_begroting_buitengewoon_2025,{ENT},2025,111525,,,executed,{SRC},strong,2025 begrotingsresultaat buitengewone dienst 111525 (PDF 111524.96 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_carry_buitengewoon_2025,{ENT},2025,1584589,,,executed,{SRC},strong,2025 over te dragen vastgelegde uitgaven buitengewone dienst 1584589 (PDF 1584589.16 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
    f"bud_hvmw_boek_buitengewoon_2025,{ENT},2025,1696114,,,executed,{SRC},strong,2025 boekhoudkundig resultaat buitengewone dienst 1696114 (PDF 1696114.12 rounded); tick1541; primary official zoneraad JR2025 27.03.2026",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvzm"
SRC = "src_hvzm_jr2025_bbc"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_hvzm_assets_2025,{ENT},2025,4113934,,,executed,{SRC},strong,2025 balanstotaal actief=passief 4113934 (PDF 4113934.10 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_vast_2025,{ENT},2025,1789645,,,executed,{SRC},strong,2025 vaste activa 1789645 (PDF 1789644.77 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_vlottend_2025,{ENT},2025,2324289,,,executed,{SRC},strong,2025 vlottende activa 2324289 (PDF 2324289.33 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_equity_2025,{ENT},2025,3158074,,,executed,{SRC},strong,2025 eigen vermogen 3158074 (PDF 3158074.39 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_debt_2025,{ENT},2025,955860,,,executed,{SRC},strong,2025 schulden 955860 (PDF 955859.71 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_expl_2025,{ENT},2025,258096,,,executed,{SRC},strong,2025 exploitatieresultaat 258096 PROFIT (PDF 258096.19 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_uitz_2025,{ENT},2025,26793,,,executed,{SRC},strong,2025 uitzonderlijk resultaat 26793 (PDF 26793.00); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_pnl_2025,{ENT},2025,284889,,,executed,{SRC},strong,2025 resultaat boekjaar 284889 PROFIT computed (258096 + 26793); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_rechten_gewone_2025,{ENT},2025,7559144,,,executed,{SRC},strong,2025 netto vastgestelde rechten gewone dienst 7559144 (PDF 7559143.84 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_vastgelegd_gewone_2025,{ENT},2025,6332064,,,executed,{SRC},strong,2025 vastgelegde uitgaven gewone dienst 6332064 (PDF 6332064.21 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_begroting_gewone_2025,{ENT},2025,1227080,,,executed,{SRC},strong,2025 algemeen begrotingsresultaat gewone dienst 1227080 (PDF 1227079.63 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_aanrekeningen_gewone_2025,{ENT},2025,6285130,,,executed,{SRC},strong,2025 aanrekeningen gewone dienst 6285130 (PDF 6285129.70 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_boek_gewone_2025,{ENT},2025,1274014,,,executed,{SRC},strong,2025 algemeen boekhoudkundig resultaat gewone dienst 1274014 (PDF 1274014.14 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_carry_gewone_2025,{ENT},2025,46935,,,executed,{SRC},strong,2025 over te dragen vastleggingen gewone dienst 46935 (PDF 46934.51 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_rechten_buitengewoon_2025,{ENT},2025,617111,,,executed,{SRC},strong,2025 netto vastgestelde rechten buitengewone dienst 617111 (PDF 617111.27 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_vastgelegd_buitengewoon_2025,{ENT},2025,581280,,,executed,{SRC},strong,2025 vastgelegde uitgaven buitengewone dienst 581280 (PDF 581280.40 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_begroting_buitengewoon_2025,{ENT},2025,35831,,,executed,{SRC},strong,2025 algemeen begrotingsresultaat buitengewone dienst 35831 (PDF 35830.87 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_aanrekeningen_buitengewoon_2025,{ENT},2025,522696,,,executed,{SRC},strong,2025 aanrekeningen buitengewone dienst 522696 (PDF 522695.79 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_boek_buitengewoon_2025,{ENT},2025,94415,,,executed,{SRC},strong,2025 algemeen boekhoudkundig resultaat buitengewone dienst 94415 (PDF 94415.48 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
    f"bud_hvzm_carry_buitengewoon_2025,{ENT},2025,58585,,,executed,{SRC},strong,2025 over te dragen vastleggingen buitengewone dienst 58585 (PDF 58584.61 rounded); tick1540; primary official zoneraad JR2025 uittreksel 18.03.2026",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

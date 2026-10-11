#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvva"
SRC = "src_hvva_jr2025_bbc"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_hvva_uitgaven_gewone_2025,{ENT},2025,10999722,,,executed,{SRC},strong,2025 uitgaven gewone 10999722 envelope (pers 7238089 + werking 3339750 + overdrachten 222609 + schuld 199274; PDF 7238088.65 / 3339750.33 / 222608.84 / 199274.43 rounded); tick1542; primary official AV2025 11.03.2026; 1539 spend pattern",
    f"bud_hvva_pers_2025,{ENT},2025,7238089,,,executed,{SRC},strong,2025 personeelskosten gewone 7238089 (PDF 7238088.65 rounded); tick1542; primary official AV2025 11.03.2026",
    f"bud_hvva_werking_2025,{ENT},2025,3339750,,,executed,{SRC},strong,2025 werkingskosten gewone 3339750 (PDF 3339750.33 rounded); tick1542; primary official AV2025 11.03.2026",
    f"bud_hvva_overdrachten_2025,{ENT},2025,222609,,,executed,{SRC},strong,2025 overdrachten gewone 222609 (PDF 222608.84 rounded); tick1542; primary official AV2025 11.03.2026",
    f"bud_hvva_schuld_uitg_2025,{ENT},2025,199274,,,executed,{SRC},strong,2025 schuld-uitgaven gewone 199274 (PDF 199274.43 rounded); tick1542; primary official AV2025 11.03.2026",
    f"bud_hvva_inkomsten_gewone_2025,{ENT},2025,9390635,,,executed,{SRC},strong,2025 inkomsten gewone 9390635 (retributie 926305 + fed 2698944 + gemeenten 5751118 + schuld 14268; PDF 926305.10 / 2698944.02 / 5751118.00 / 14267.60 rounded); tick1542; primary official AV2025 11.03.2026",
    f"bud_hvva_retributie_2025,{ENT},2025,926305,,,executed,{SRC},strong,2025 retributie gewone 926305 (PDF 926305.10 rounded); tick1542; primary official AV2025 11.03.2026",
    f"bud_hvva_toelagen_fed_2025,{ENT},2025,2698944,,,executed,{SRC},strong,2025 toelagen federaal 2698944 (PDF 2698944.02 rounded); tick1542; primary official AV2025 11.03.2026",
    f"bud_hvva_toelagen_gem_2025,{ENT},2025,5751118,,,executed,{SRC},strong,2025 toelagen gemeenten 5751118 (PDF 5751118.00); tick1542; primary official AV2025 11.03.2026; city-share unpublished",
    f"bud_hvva_schuld_ink_2025,{ENT},2025,14268,,,executed,{SRC},strong,2025 schuld-inkomsten gewone 14268 (PDF 14267.60 rounded); tick1542; primary official AV2025 11.03.2026",
    f"bud_hvva_invest_2025,{ENT},2025,3565917,,,executed,{SRC},strong,2025 investeringen buitengewoon 3565917 (PDF 3565917.15 rounded); tick1542; primary official AV2025 11.03.2026",
    f"bud_hvva_dotaties_buitengewoon_2025,{ENT},2025,3460697,,,executed,{SRC},strong,2025 dotaties buitengewoon 3460697 (PDF 3460697.00); tick1542; primary official AV2025 11.03.2026",
    f"bud_hvva_voertuigen_2025,{ENT},2025,848700,,,executed,{SRC},strong,2025 in dienst gestelde voertuigen 848700 (2x ambulance 202500 + 5x logistiek 76500 + personeelswagen 61200); tick1542; primary official AV2025 11.03.2026",
    f"bud_hvva_nietrollend_2025,{ENT},2025,211500,,,executed,{SRC},strong,2025 belangrijkste aankopen niet-rollend 211500 (ademlucht 20000 + pakken 85000 + helmen 26500 + interventie 55000 + vesten 10000 + machines 15000); tick1542; primary official AV2025 11.03.2026",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

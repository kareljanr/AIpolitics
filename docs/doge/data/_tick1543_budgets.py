#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvzk"
SRC = "src_hvzk_jr2025_bbc"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_hvzk_uitgaven_gewone_2025,{ENT},2025,16747636,,,executed,{SRC},strong,2025 uitgaven gewone 16747636 envelope (pers 13742087 + werking 3005549; PDF 13742086.51 / 3005549.03 rounded); tick1543; primary official AV2025 05.05.2026; 1539/1542 spend pattern",
    f"bud_hvzk_pers_2025,{ENT},2025,13742087,,,executed,{SRC},strong,2025 personeelskosten 13742087 (PDF 13742086.51 rounded); tick1543; primary official AV2025 05.05.2026",
    f"bud_hvzk_werking_2025,{ENT},2025,3005549,,,executed,{SRC},strong,2025 werkingskosten 3005549 (PDF 3005549.03 rounded); tick1543; primary official AV2025 05.05.2026",
    f"bud_hvzk_invest_2025,{ENT},2025,2506646,,,executed,{SRC},strong,2025 investeringen 2506646 (PDF 2506645.96 rounded; gebouwen 662672 + voertuigen 1080849 + materieel 763126); tick1543; primary official AV2025 05.05.2026",
    f"bud_hvzk_invest_gebouwen_2025,{ENT},2025,662672,,,executed,{SRC},strong,2025 investeringen gebouwen 662672 (PDF 662671.68 rounded); tick1543; primary official AV2025 05.05.2026",
    f"bud_hvzk_invest_voertuigen_2025,{ENT},2025,1080849,,,executed,{SRC},strong,2025 investeringen voertuigen 1080849 (PDF 1080848.68 rounded); tick1543; primary official AV2025 05.05.2026",
    f"bud_hvzk_invest_materieel_2025,{ENT},2025,763126,,,executed,{SRC},strong,2025 investeringen materieel 763126 (PDF 763125.60 rounded); tick1543; primary official AV2025 05.05.2026",
    f"bud_hvzk_beschikbaar_2025,{ENT},2025,18986967,,,executed,{SRC},strong,2025 ter beschikking 18986967 (PDF 18986966.85 rounded; invest-subsidy 1942761 + ordinary inkomsten); tick1543; primary official AV2025 05.05.2026",
    f"bud_hvzk_invest_subsidy_2025,{ENT},2025,1942761,,,executed,{SRC},strong,2025 investeringssubsidie 1942761 (PDF 1942761.25 rounded); tick1543; primary official AV2025 05.05.2026",
    f"bud_hvzk_gem_werking_2025,{ENT},2025,7771044,,,executed,{SRC},strong,2025 gemeentelijke werkingsbijdrage 7771044 (PDF 7771044.03 rounded); tick1543; primary official AV2025 05.05.2026",
    f"bud_hvzk_gem_totaal_2025,{ENT},2025,9713805,,,executed,{SRC},strong,2025 gemeentelijk totaal 9713805 (PDF 9713805.28 rounded; expl 7771044 + invest 1942761); tick1543; primary official AV2025 05.05.2026",
    f"bud_hvzk_fed_2025,{ENT},2025,4394794,,,executed,{SRC},strong,2025 federale dotatie 4394794 (PDF table 4394794.18 rounded; basis 922619.10 sourced; bijkomende text OCR-garbled FOI); tick1543; primary official AV2025 05.05.2026",
    f"bud_hvzk_dgh_2025,{ENT},2025,2421103,,,executed,{SRC},strong,2025 dotatie DGH 2421103 (PDF 2421103.20 rounded; FOD VG 2337785.20 + PIT Mol 83318.00); tick1543; primary official AV2025 05.05.2026",
    f"bud_hvzk_facturatie_2025,{ENT},2025,1307948,,,executed,{SRC},strong,2025 facturatie prestaties 1307948 (PDF 1307947.58 rounded; ambulance 752829 + preventie 273465 + interventie 281654); tick1543; primary official AV2025 05.05.2026",
    f"bud_hvzk_seveso_2025,{ENT},2025,496057,,,executed,{SRC},strong,2025 Sevesofonds 496057 (PDF 496057.48 rounded; extra 246000); tick1543; primary official AV2025 05.05.2026",
    f"bud_hvzk_andere_2025,{ENT},2025,570289,,,executed,{SRC},strong,2025 andere werkingsontvangsten 570289 (PDF 570289.13 rounded; vlottende 218236 + fiets/cheques 95334 + verzek 91156 + unpublished remainder); tick1543; primary official AV2025 05.05.2026",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

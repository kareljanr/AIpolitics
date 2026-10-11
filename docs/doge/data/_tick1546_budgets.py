#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvzwl"
SRC = "src_hvzwl_jr2025_bbc"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_hvzwl_uitgaven_gewone_2025,{ENT},2025,29117176,,,executed,{SRC},strong,2025 uitgaven gewone 29117176 envelope (pers 20930221 + werking 5782142 + overdrachten 676531 + schuld 1728282); tick1546; primary official AV2025 09.07.2026; 1539/1542-1545 spend pattern",
    f"bud_hvzwl_pers_2025,{ENT},2025,20930221,,,executed,{SRC},strong,2025 personeelskosten 20930221 (PDF 20930221.17 rounded); tick1546; primary official AV2025 09.07.2026",
    f"bud_hvzwl_werking_2025,{ENT},2025,5782142,,,executed,{SRC},strong,2025 werkingskosten 5782142 (PDF 5782142.28 rounded); tick1546; primary official AV2025 09.07.2026",
    f"bud_hvzwl_overdrachten_2025,{ENT},2025,676531,,,executed,{SRC},strong,2025 uitgaven overdrachten 676531 (PDF 676530.79 rounded); tick1546; primary official AV2025 09.07.2026",
    f"bud_hvzwl_schuld_2025,{ENT},2025,1728282,,,executed,{SRC},strong,2025 uitgaven schuld 1728282 (PDF 1728281.99 rounded); tick1546; primary official AV2025 09.07.2026",
    f"bud_hvzwl_invest_2025,{ENT},2025,4393168,,,executed,{SRC},strong,2025 investeringen 4393168 (PDF 4393168.32 rounded; hoogwerkers 622000 + blusrobot 150000 named); tick1546; primary official AV2025 09.07.2026",
    f"bud_hvzwl_dot_gemeente_2025,{ENT},2025,20908513,,,executed,{SRC},strong,2025 gemeentelijke dotaties 20908513 over 17 gemeenten (PDF 20908512.76; Hasselt 5465558); tick1546; primary official AV2025 09.07.2026",
    f"bud_hvzwl_dot_hasselt_2025,{ENT},2025,5465558,,,executed,{SRC},strong,2025 Hasselt gemeentelijke dotatie 5465558 (PDF 5465557.73; 26.17 pct of 20908513); tick1546; primary official AV2025 09.07.2026",
    f"bud_hvzwl_volksgezondheid_2025,{ENT},2025,4478255,,,executed,{SRC},strong,2025 subsidies Volksgezondheid 4478255 (PDF 4478254.91); tick1546; primary official AV2025 09.07.2026",
    f"bud_hvzwl_prestaties_2025,{ENT},2025,2291333,,,executed,{SRC},strong,2025 ontvangsten prestaties 2291333 (PDF 2291332.89); tick1546; primary official AV2025 09.07.2026",
    f"bud_hvzwl_ontvangsten_2025,{ENT},2025,35360400,,,executed,{SRC},strong,2025 werkingsbudget / totaal ontvangsten 35360400 (PDF 35360400.19; receipts not spend); tick1546; primary official AV2025 09.07.2026",
    f"bud_hvzwl_hoogwerkers_2025,{ENT},2025,622000,,,executed,{SRC},strong,2025 aankoop 3 lichte hoogwerkers 622000 (part of invest 4393168); tick1546; primary official AV2025 09.07.2026",
    f"bud_hvzwl_blusrobot_2025,{ENT},2025,150000,,,executed,{SRC},strong,2025 aankoop blusrobot 150000 (part of invest 4393168); tick1546; primary official AV2025 09.07.2026",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

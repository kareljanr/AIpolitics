#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvnl"
SRC = "src_hvnl_jr2025_bbc"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_hvnl_uitgaven_gewone_2025,{ENT},2025,13883486,,,executed,{SRC},strong,2025 uitgaven gewone GD 13883486 envelope (pers 10572316 + werking detail 2834534 + divers 136386 + schuld 340250); PDF summary werking 2384534 is 450k short of GD — FOI; tick1545; primary official JV2025 18.03.2026; 1539/1542/1543/1544 spend pattern",
    f"bud_hvnl_pers_2025,{ENT},2025,10572316,,,executed,{SRC},strong,2025 personeelskosten 10572316 (PDF Totaal Loonkost / Personeel both 10572316); tick1545; primary official JV2025 18.03.2026",
    f"bud_hvnl_werking_2025,{ENT},2025,2834534,,,executed,{SRC},strong,2025 werkingskosten 2834534 (PDF detail Totaal werkingskost; summary line 2384534 does not reconcile — FOI); tick1545; primary official JV2025 18.03.2026",
    f"bud_hvnl_prestaties_2025,{ENT},2025,834402,,,executed,{SRC},strong,2025 ontvangsten prestaties 834402 (brandweer 222821 + D100 611581); tick1545; primary official JV2025 18.03.2026",
    f"bud_hvnl_werkingstoelagen_2025,{ENT},2025,14309007,,,executed,{SRC},strong,2025 totaal dotaties 14309007 (gemeente 8057000 + federaal 6252007); tick1545; primary official JV2025 18.03.2026",
    f"bud_hvnl_dot_gemeente_2025,{ENT},2025,8057000,,,executed,{SRC},strong,2025 gemeentelijke dotaties 8057000 (PDF Gemeentelijke dotaties / Dotaties Gemeenten); per-gemeente split unpublished FOI; tick1545; primary official JV2025 18.03.2026",
    f"bud_hvnl_dot_federaal_2025,{ENT},2025,6252007,,,executed,{SRC},strong,2025 federale overheid 6252007 (PDF Federale overheid; brandweer 2708361 + D100 2888866 + overige 654780); tick1545; primary official JV2025 18.03.2026",
    f"bud_hvnl_invest_2025,{ENT},2025,3784028,,,executed,{SRC},strong,2025 investeringen 3784028 (PDF Totaal Investeringen; BD uitgaven 3748028); tick1545; primary official JV2025 18.03.2026",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

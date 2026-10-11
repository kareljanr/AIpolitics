#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvzf"
SRC = "src_hvzf_jr2025_bbc"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_hvzf_uitgaven_gewone_2025,{ENT},2025,20237541,,,executed,{SRC},strong,2025 uitgaven gewone 20237541 envelope (PDF 20237540.93; pers 15462341 + werking 4652717 + overdrachten 122484; 1-euro official rounding); tick1547; primary official AV2025 02.04.2026; 1539/1542-1546 spend pattern",
    f"bud_hvzf_pers_2025,{ENT},2025,15462341,,,executed,{SRC},strong,2025 personeelskosten 15462341 (PDF 15462340.54 rounded); tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_werking_2025,{ENT},2025,4652717,,,executed,{SRC},strong,2025 werkingskosten 4652717 (PDF 4652716.84 rounded; ICT 1011920 + materieel BW 958006 + gebouwen 661074 + voertuigen BW 613358); tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_overdrachten_2025,{ENT},2025,122484,,,executed,{SRC},strong,2025 uitgaven overdrachten 122484 (PDF 122483.55 rounded); tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_ontvangsten_2025,{ENT},2025,21496867,,,executed,{SRC},strong,2025 ontvangsten gewone 21496867 (PDF 21496867.16; prestaties 1837568 + overdrachten 19477333 + schuld 181967); tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_prestaties_2025,{ENT},2025,1837568,,,executed,{SRC},strong,2025 ontvangsten prestaties 1837568 (PDF 1837567.90; retributies BW 469k + DGH 1000k); tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_overdr_ontv_2025,{ENT},2025,19477333,,,executed,{SRC},strong,2025 ontvangsten overdrachten 19477333 (PDF 19477332.61; gemeente 11650k + fed BW 4684k + fed DGH 3091k); tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_dot_gemeente_2025,{ENT},2025,11650000,,,executed,{SRC},strong,2025 gemeentelijke exploitatiedotaties 11650000 (PDF 11.650k; 14 gemeenten unpublished split); tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_fed_brandweer_2025,{ENT},2025,4684000,,,executed,{SRC},strong,2025 federale toelagen brandweer 4684000 (PDF 4.684k); tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_fed_dgh_2025,{ENT},2025,3091000,,,executed,{SRC},strong,2025 federale toelagen DGH 3091000 (PDF 3.091k incl 299k correctie 2024); tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_invest_2025,{ENT},2025,1598798,,,executed,{SRC},strong,2025 investeringen buitengewoon 1598798 (PDF 1598798.37; 41.29 pct of buitengewoon 3872440); tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_buitengewoon_2025,{ENT},2025,3872440,,,executed,{SRC},strong,2025 uitgaven buitengewoon 3872440 (PDF 3872440.35; invest 1598798 + schuld 2253247 + overdrachten 20395); tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_schuld_buit_2025,{ENT},2025,2253247,,,executed,{SRC},strong,2025 schulduitgaven buitengewoon 2253247 (PDF 2253246.83; laatste schijven kazernes Menen Belgiek Waregem); tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_ict_2025,{ENT},2025,1011920,,,executed,{SRC},strong,2025 werkingskosten ICT 1011920 (PDF 1011920.27; 21.75 pct of werking); tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_resultaat_gewone_2025,{ENT},2025,5368924,,,executed,{SRC},strong,2025 algemeen budgettair resultaat gewone dienst 5368924 (PDF 5368923.85; eigen dienstjaar 1162424); tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_reserve_gewoon_2025,{ENT},2025,500000,,,executed,{SRC},strong,2025 gewoon reservefonds 500000; tick1547; primary official AV2025 02.04.2026",
    f"bud_hvzf_reserve_buit_2025,{ENT},2025,516905,,,executed,{SRC},strong,2025 buitengewoon reservefonds 516905 (PDF 516905.31; kazernering); tick1547; primary official AV2025 02.04.2026",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")

#!/usr/bin/env python3
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nigs_kstf," in raw or raw.startswith(b"igs_kstf,"):
    raise SystemExit("igs_kstf already present")
if b"0552.559.411" in raw or b"0552559411" in raw:
    raise SystemExit("Kusterfgoed KBO already present")
row = (
    "igs_kstf,Projectvereniging Kusterfgoed (leftover IGS projectvereniging / IOED / erfgoedcel of 5 mined Middenkust cities),"
    "Kusterfgoed (IGS residuel / association de projet cote),"
    "Kusterfgoed leftover IGS / IOED / heritage cell of 5 Mid-Coast municipalities,"
    "other,sec_flanders,nl,https://www.kusterfgoed.be/,info@kusterfgoed.be,Vindictivelaan 1 8400 Oostende / InnovOcean Campus Jacobsenstraat 1,"
    "tick1429 leftover residual IGS / IOED of mined Middenkust cities after leftover AGB hunt; KBO 0552.559.411 Actief since 09.05.2012; official NBB WVV MIC-VZW PDF downloads; sourced euros assets 162729 omzet empty diensten empty lidgeld empty pers 263807 pnl -16180 equity 100647 cash 153074 debt 62082 capex 0 dividend 0; FOI ready empty 70/73/60/61 / pers 0.26m / cash drop / continuity 3:6; distinct from already-mined Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / IVBO / IVOO"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 igs_kstf")

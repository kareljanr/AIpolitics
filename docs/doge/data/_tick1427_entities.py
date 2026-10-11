#!/usr/bin/env python3
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nigs_eddl," in raw or raw.startswith(b"igs_eddl,"):
    raise SystemExit("igs_eddl already present")
if b"0544.953.225" in raw or b"0544953225" in raw:
    raise SystemExit("Erfgoed Denderland KBO already present")
row = (
    "igs_eddl,Intergemeentelijke Projectvereniging Erfgoed Denderland / PV Erfgoed Denderland (leftover IGS projectvereniging / IOED of 6 mined Denderland cities),"
    "Erfgoed Denderland (IGS residuel / association de projet Denderland),"
    "Erfgoed Denderland leftover IGS / IOED of 6 Denderland municipalities,"
    "other,sec_flanders,nl,https://www.erfgoedceldenderland.be/,erfgoedcel@aalst.be,Onderwijsstraat 1 9300 Aalst,"
    "tick1427 leftover residual IGS / IOED of mined Denderland cities after leftover AGB hunt; KBO 0544.953.225 Actief since 27.11.2013; official NBB WVV MIC-VZW PDF downloads; sourced euros assets 454221 lidgeld 498745 omzet 100 diensten 573634 pers empty pnl -76695 equity 73209 cash 320049 debt 381012 capex 0 dividend 0; FOI ready omzet token / diensten unpublished / pers empty / other recv 0.10m / cash drop; distinct from already-mined Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 igs_eddl")

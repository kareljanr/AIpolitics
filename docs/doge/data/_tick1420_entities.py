#!/usr/bin/env python3
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nigs_co7," in raw or raw.startswith(b"igs_co7,"):
    raise SystemExit("igs_co7 already present")
row = (
    "igs_co7,CultuurOverleg Zeven / CO7 (leftover IGS projectvereniging of 7 mined Zuidelijke Westhoek cities),"
    "CultuurOverleg Zeven (IGS residuel / association de projet Westhoek sud),"
    "CultuurOverleg Zeven leftover IGS of 7 southern Westhoek municipalities,"
    "other,sec_flanders,nl,https://www.co7.be/,info@co7.be,Grote Markt 1 8970 Poperinge,"
    "tick1420 leftover residual IGS of mined Zuidelijke Westhoek cities after leftover AGB hunt; KBO 0877.372.225 Actief since 17.11.2005; official NBB WVV MIC-inb PDF downloads; sourced euros assets 691225 omzet 899440 diensten 900356 pers empty pnl -7140 equity 393922 cash 552517 debt 297303 capex 17712 dividend 0; FOI ready omzet 6.10 empty / diensten unpublished split / prepaid 0.12m / pers empty; distinct from already-mined DVV Westhoek 1415 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 igs_co7")

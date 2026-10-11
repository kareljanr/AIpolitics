#!/usr/bin/env python3
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nigs_ebk," in raw or raw.startswith(b"igs_ebk,"):
    raise SystemExit("igs_ebk already present")
if b"0741.478.094" in raw or b"0741478094" in raw:
    raise SystemExit("Erfgoed Brabantse Kouters KBO already present")
row = (
    "igs_ebk,Projectvereniging Erfgoed Brabantse Kouters (leftover IGS projectvereniging / IOED of 12 mined Brabantse Kouters cities),"
    "Erfgoed Brabantse Kouters (IGS residuel / association de projet Brabantse Kouters),"
    "Erfgoed Brabantse Kouters leftover IGS / IOED of 12 Brabantse Kouters municipalities,"
    "other,sec_flanders,nl,https://www.brabantsekouters.be/projecten/erfgoed-brabantse-kouters,info@brabantsekouters.be,Houtemsesteenweg 23 1800 Vilvoorde,"
    "tick1428 leftover residual IGS / IOED of mined Brabantse Kouters cities after leftover AGB hunt; KBO 0741.478.094 Actief since 06.01.2020; official NBB WVV MIC-VZW PDF downloads; sourced euros assets 200838 omzet empty diensten empty lidgeld empty pers empty pnl 0 equity empty cash 172470 debt 200838 capex 0 dividend 0; FOI ready empty 70/73/60/61 / empty EV / leveranciers 0.15m / deferred 0.05m; distinct from already-mined Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 igs_ebk")

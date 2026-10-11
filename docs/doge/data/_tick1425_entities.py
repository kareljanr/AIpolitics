#!/usr/bin/env python3
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nigs_evpk," in raw or raw.startswith(b"igs_evpk,"):
    raise SystemExit("igs_evpk already present")
if b"0650.649.076" in raw or b"0650649076" in raw:
    raise SystemExit("Erfgoed Voorkempen KBO already present")
row = (
    "igs_evpk,Erfgoed Voorkempen / Projectvereniging erfgoed Voorkempen (leftover IGS projectvereniging of 14 mined Voorkempen cities),"
    "Erfgoed Voorkempen (IGS residuel / association de projet Voorkempen),"
    "Erfgoed Voorkempen leftover IGS of 14 Voorkempen municipalities,"
    "other,sec_flanders,nl,https://www.rldv.be/erfgoed-voorkempen/,info@rldevoorkempen.be,Schildesteenweg 99 2520 Ranst,"
    "tick1425 leftover residual IGS of mined Voorkempen cities after leftover AGB hunt; KBO 0650.649.076 Actief since 01.01.2016; official NBB WVV MIC-inb PDF downloads; sourced euros assets 623422 brutomarge 49498 omzet empty diensten empty pers empty pnl 48253 equity 125438 cash 499042 debt 497984 capex 0 dividend 0; FOI ready omzet empty / diensten unpublished / other recv 0.11m / leveranciers 0.45m / cash drop / pers empty; distinct from already-mined Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / AGB Zoersel / AGB Kapellen / IGEAN"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 igs_evpk")

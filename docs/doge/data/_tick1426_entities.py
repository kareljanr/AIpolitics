#!/usr/bin/env python3
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nigs_enpk," in raw or raw.startswith(b"igs_enpk,"):
    raise SystemExit("igs_enpk already present")
if b"0863.327.714" in raw or b"0863327714" in raw:
    raise SystemExit("Erfgoed Noorderkempen KBO already present")
row = (
    "igs_enpk,Erfgoed Noorderkempen / Projectvereniging Erfgoed Noorderkempen (leftover IGS projectvereniging of 11 mined Noorderkempen cities),"
    "Erfgoed Noorderkempen (IGS residuel / association de projet Noorderkempen),"
    "Erfgoed Noorderkempen leftover IGS of 11 Noorderkempen municipalities,"
    "other,sec_flanders,nl,https://erfgoednoorderkempen.be/,info@erfgoednoorderkempen.be,Grote Markt 1 2300 Turnhout,"
    "tick1426 leftover residual IGS of mined Noorderkempen cities after leftover AGB hunt; KBO 0863.327.714 Actief since 10.02.2004; official NBB WVV VKT-inb PDF downloads; sourced euros assets 480193 brutomarge 831915 omzet empty diensten empty pers 767960 pnl 56632 equity 401292 cash 376948 debt 78901 capex 4084 dividend 0; FOI ready omzet empty / diensten unpublished / pers 0.77m / other recv 0.07m / cash jump; distinct from already-mined Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Druivenstreek 1422"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 igs_enpk")

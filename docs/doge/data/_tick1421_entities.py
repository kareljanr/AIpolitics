#!/usr/bin/env python3
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nigs_vtrt," in raw or raw.startswith(b"igs_vtrt,"):
    raise SystemExit("igs_vtrt already present")
if b"0744.514.689" in raw or b"0744514689" in raw:
    raise SystemExit("Viertoren KBO already present")
row = (
    "igs_vtrt,Viertoren (leftover IGS projectvereniging of 4 mined Westhoek kust cities),"
    "Viertoren (IGS residuel / association de projet cote Westhoek),"
    "Viertoren leftover IGS of 4 coastal Westhoek municipalities,"
    "other,sec_flanders,nl,https://viertoren.be/,info@viertoren.be,Zeelaan 303 8670 Koksijde,"
    "tick1421 leftover residual IGS of mined De Panne/Koksijde/Nieuwpoort/Veurne after leftover AGB hunt; KBO 0744.514.689 Actief since 01.10.2019; official NBB WVV MIC-inb PDF downloads; sourced euros assets 211378 brutomarge 110397 omzet empty diensten empty pers 79534 pnl 30657 equity 202586 cash 189139 debt 8791 capex 0 dividend 0; FOI ready omzet empty / diensten unpublished / pers 0.08m VTE unpublished / other recv 0.02m / cash drop unpublished; distinct from already-mined CO7 1420 / DVV Westhoek 1415 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 igs_vtrt")

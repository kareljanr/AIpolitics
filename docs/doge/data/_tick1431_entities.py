#!/usr/bin/env python3
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nigs_rpsk," in raw or raw.startswith(b"igs_rpsk,"):
    raise SystemExit("igs_rpsk already present")
if b"0822.286.618" in raw or b"0822286618" in raw:
    raise SystemExit("Erfgoed Rupelstreek KBO already present")
row = (
    "igs_rpsk,Erfgoed Rupelstreek (leftover IGS projectvereniging / IOED of 5 mined Rupelstreek cities),"
    "Erfgoed Rupelstreek (IGS residuel / association de projet / IOED Rupel),"
    "Erfgoed Rupelstreek leftover IGS / IOED / project association of 5 Rupelstreek municipalities,"
    "other,sec_flanders,nl,https://erfgoedrupelstreek.be/,info@erfgoedrupelstreek.be,Hoogstraat 27 2850 Boom / zetel Schommelei 1 Provinciaal Domein De Schorre,"
    "tick1431 leftover residual IGS / IOED of mined Rupelstreek cities after leftover AGB hunt; KBO 0822.286.618 Actief since 13.11.2009; official NBB WVV MIC-inb PDF downloads; sourced euros assets 58035 omzet empty diensten empty pers empty pnl -10998 equity 58035 cash 31653 debt 0 capex 0 dividend 0; FOI ready empty 70/60/61/62 / negative bruto / cash drop / continuity; distinct from already-mined RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / IVBO"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 igs_rpsk")

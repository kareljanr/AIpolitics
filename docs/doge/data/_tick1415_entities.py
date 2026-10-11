#!/usr/bin/env python3
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nigs_westhoek_dv," in raw or raw.startswith(b"igs_westhoek_dv,"):
    raise SystemExit("igs_westhoek_dv already present")
row = (
    "igs_westhoek_dv,Dienstverlenende Vereniging Westhoek / DVV Westhoek (leftover IGS dienstverlenende vereniging of 17 mined Westhoek cities + WVI),"
    "DVV Westhoek (association de services / IGS residuel Westhoek),"
    "DVV Westhoek leftover IGS of 17 Westhoek municipalities + WVI,"
    "other,sec_flanders,nl,https://dvvwesthoek.be/,info@dvvwesthoek.be,Grote Markt 6 8600 Diksmuide,"
    "tick1415 leftover residual IGS of mined Westhoek cities after leftover AGB hunt; KBO 0695.496.928 Actief since 22.12.2017; official NBB WVV VKT-inb PDF downloads; sourced euros assets 3145801 brutomarge 2859900 omzet empty diensten empty pers 2648974 pnl 101860 equity 1987351 cash 1859774 debt 1158449 capex 17881 dividend 0; FOI ready omzet empty / diensten unpublished / other recv 0.54m / other ST 0.22m; distinct from already-mined IVVO 1345 / WVI 1346 / Aquaduin 1349 / AGB De Kluize 1414"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 igs_westhoek_dv")

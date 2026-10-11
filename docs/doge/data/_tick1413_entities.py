#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
rows = [
    "nv_pmbs,PATRIMONIUM MBS NV (leftover IOK Afvalbeheer 60pct / IVAREM 40pct daughter NV / MBS patrimonium Geel),PATRIMONIUM MBS SA (filiale residuelle IOK Afvalbeheer / IVAREM),PATRIMONIUM MBS leftover IOK/IVAREM daughter NV,other,igs_ioka,nl,https://www.iok.be,info@iok.be,Antwerpseweg 1 2440 Geel,tick1413 leftover residual IOK Afvalbeheer 60pct daughter after leftover AGB/IGS hunt; KBO 0886.391.839 Actief since 15.01.2007; official NBB WVV VOL-kap PDF downloads; sourced euros assets 1600122 omzet 107101 diensten 112337 pnl 1072 equity 1599050 cash 528367 debt 1072 capex 0 dividend 1072; FOI ready omzet 6.10 empty / diensten split / vruchtgebruik Maatschap MBS / commissaris image-only",
]
append_lf(DATA / "entities.csv", rows)
print("entities +1")

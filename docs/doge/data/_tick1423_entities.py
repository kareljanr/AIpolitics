#!/usr/bin/env python3
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nnv_bnlg," in raw or raw.startswith(b"nv_bnlg,"):
    raise SystemExit("nv_bnlg already present")
if b"0553.855.647" in raw or b"0553855647" in raw:
    raise SystemExit("BIONERGA LOGISTICS KBO already present")
row = (
    "nv_bnlg,BIONERGA LOGISTICS NV (leftover Bionerga NV 100pct daughter / Optimo truck fleet Limburg.net),"
    "BIONERGA LOGISTICS SA (filiale residuelle 100pct Bionerga / flotte camions Optimo Limburg.net),"
    "BIONERGA LOGISTICS leftover 100pct Bionerga NV daughter (Limburg.net Optimo collection trucks),"
    "other,nv_bionerga,nl,https://bionerga.be/,info@bionerga.be,Herkenrodesingel 14 3500 Hasselt,"
    "tick1423 leftover residual daughter after leftover AGB/IGS hunt; KBO 0553.855.647 Actief since 13.06.2014; official NBB WVV VOL-kap PDF downloads; sourced euros assets 3510439 omzet 1717525 diensten 1289949 pers empty pnl 142458 equity 1664756 cash 956680 debt 1845683 capex 355000 dividend 0; FOI ready 6.10 omzet category/geo empty / diensten 1.29m split / related-party recv+debt / leveranciers JUMP / pers empty; distinct from already-mined Bionerga NV 1354 / Limburg.net 1353 / Nuhma seam 1355-1365 / Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 nv_bnlg")

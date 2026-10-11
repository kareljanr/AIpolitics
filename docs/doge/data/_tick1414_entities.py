#!/usr/bin/env python3
from pathlib import Path
p = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
raw = p.read_bytes()
if not raw.endswith(b"\n"):
    raw += b"\n"
lines = raw.splitlines(keepends=True)
out = []
found = 0
new_notes = (
    "tick1414 leftover residual AGB of mined city Oosterzele after leftover AGB hunt; "
    "KBO 0844.272.162 Actief since 28.09.2011; official NBB WVV VKT-kap PDF downloads; "
    "sourced euros assets 5831290 brutomarge 342519 omzet empty diensten empty pers empty "
    "pnl 73538 equity 69529 cash 724091 debt 5761761 lease 4483958 capex 87700 dividend 50000; "
    "FOI ready omzet empty / diensten unpublished / pers empty / lease 4.48m / LT debt 5.32m / "
    "commissaris fee unpublished; distinct from already-mined PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411"
)
for line in lines:
    if line.startswith(b"agb_de_kluize_oosterzele,"):
        s = line.decode("utf-8").rstrip("\r\n")
        parts = s.split(",", 10)
        if len(parts) != 11:
            raise SystemExit(f"unexpected kluize cols {len(parts)}")
        parts[10] = new_notes
        line = (",".join(parts) + "\n").encode("utf-8")
        found += 1
    out.append(line)
if found != 1:
    raise SystemExit(f"expected 1 agb_de_kluize_oosterzele row, got {found}")
p.write_bytes(b"".join(out))
print("entities patched agb_de_kluize_oosterzele notes only")

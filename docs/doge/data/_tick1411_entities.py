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
    "tick1411 leftover residual AGB of mined city Merchtem after leftover AGB hunt; "
    "KBO 0824.869.093 Actief since 26.10.2009; official NBB WVV VKT-inb PDF downloads; "
    "sourced euros assets 4925278 brutomarge 313807 omzet empty diensten empty pers empty "
    "pnl 46516 equity 1413160 cash 57860 debt 3382104 recv 1328425 capex 48876 dividend 25000; "
    "FOI ready omzet empty / diensten unpublished / pers empty / ST recv 1.33m / LT loans 2.73m / "
    "jaarverslag not filed; distinct from already-mined AGB Tielt 1405 / AGB Patri 1407 / Sunfin 1410"
)
for line in lines:
    if line.startswith(b"agb_merchtem,"):
        s = line.decode("utf-8").rstrip("\r\n")
        parts = s.split(",", 10)
        if len(parts) != 11:
            raise SystemExit(f"unexpected merchtem cols {len(parts)}")
        parts[10] = new_notes
        line = (",".join(parts) + "\n").encode("utf-8")
        found += 1
    out.append(line)
if found != 1:
    raise SystemExit(f"expected 1 agb_merchtem row, got {found}")
p.write_bytes(b"".join(out))
print("entities patched agb_merchtem notes only")

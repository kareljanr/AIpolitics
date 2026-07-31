# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\research_queue.csv")
raw = p.read_bytes()
for enc in ("utf-8", "cp1252", "latin-1"):
    try:
        text = raw.decode(enc)
        break
    except UnicodeDecodeError:
        pass
if not text.endswith("\n"):
    text += "\n"
row = (
    "rq_158,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    '"Prefer public primary fills (De Lijn 2025-26 full perimeter Antwerp register univ '
    "per-institution VIPA Mons BI2026 bpost USO HR Rail) if new PDFs appear; else next open rq; "
    'do not idle while public work remains.",'
    ",2026-07-28T04:05:00Z,,"
    '"Spawned tick162 after FOREM L5; rq_116 SWA deferred Oct-Dec 2026"\n'
)
# Fix CSV: field 8 description is quoted; field 9 empty gap; etc.
# Actual well-formed row:
row = (
    'rq_158,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,'
    '"Prefer public primary fills (De Lijn 2025-26 full perimeter Antwerp register univ '
    "per-institution VIPA Mons BI2026 bpost USO HR Rail) if new PDFs appear; else next open rq; "
    'do not idle while public work remains.",'
    ',2026-07-28T04:05:00Z,,'
    '"Spawned tick162 after FOREM L5; rq_116 SWA deferred Oct-Dec 2026"\n'
)
if not any(L.startswith("rq_158,") for L in text.splitlines()):
    text += row
    p.write_bytes(text.encode("utf-8"))
    print("appended rq_158")
else:
    print("already present")
print("lines", sum(1 for L in text.splitlines() if L.startswith("rq_158,")))

# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
q = Path("/workspace/AIpolitics/docs/doge/data/research_queue.csv")
with q.open("rb") as f:
    f.seek(0, 2)
    size = f.tell()
    f.seek(max(0, size - 600))
    tail = f.read().decode("utf-8", "replace")
print("QUEUE_SIZE", size)
print("QUEUE_TAIL")
print(tail[-400:])
e = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
with e.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    ids = [row["entity_id"] for row in r]
print("N_ENTITIES", len(ids))
print("LAST5", ids[-5:])
print("OTAR_HITS", [i for i in ids if "otar" in i.lower()])
print("NV_OTAR", "nv_otar" in ids)

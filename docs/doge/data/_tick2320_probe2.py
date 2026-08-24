# -*- coding: utf-8 -*-
import csv
csv.field_size_limit(10**7)
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
hvz = [r.get("entity_id") for r in rows if "hvz" in (r.get("entity_id") or "").lower()]
print("hvz count", len(hvz))
print("\n".join(hvz))
print("---")
for n in [
    "de_max",
    "mpi",
    "vzw_de_",
    "wzc_den_akker",
    "huize_vincent",
    "hof_ter_lande",
    "werkplus",
]:
    hits = [r.get("entity_id") for r in rows if n in (r.get("entity_id") or "").lower()]
    print(n, "->", hits[:8] if hits else "MISSING")

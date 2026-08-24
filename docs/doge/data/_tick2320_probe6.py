# -*- coding: utf-8 -*-
import csv
csv.field_size_limit(10**7)
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
for n in [
    "pidpa",
    "farys",
    "watergroep",
    "hydrobru",
    "iwva",
    "fluvia",
    "westhoek",
    "midwest",
    "zuid_west_limburg",
    "zwl",
    "hvzzwl",
    "brandweerzone",
    "aiee",
    "ores",
    "sibelga",
]:
    hits = [r.get("entity_id") for r in rows if n in (r.get("entity_id") or "").lower() or n in (r.get("name_nl") or "").lower()]
    print(n, "->", hits[:6] if hits else "MISSING")

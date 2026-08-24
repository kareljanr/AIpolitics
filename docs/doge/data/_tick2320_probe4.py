# -*- coding: utf-8 -*-
import csv
csv.field_size_limit(10**7)
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
for n in ["psychogeriatr", "0435.357", "0435357675", "sint-agatha", "berchem"]:
    hits = []
    for r in rows:
        blob = " ".join([(r.get("entity_id") or ""), (r.get("name") or ""), (r.get("kbo") or ""), (r.get("notes") or "")]).lower()
        if n.lower() in blob:
            hits.append(r.get("entity_id"))
    print(n, hits[:6] if hits else "MISSING")

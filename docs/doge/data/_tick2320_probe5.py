# -*- coding: utf-8 -*-
import csv
csv.field_size_limit(10**7)
eid = "nv_psychogeriatrisch_centrum"
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        if r.get("entity_id") == eid:
            for k, v in r.items():
                if v:
                    print(f"{k}: {(v[:220] if isinstance(v, str) else v)}")
with open("docs/doge/data/budgets.csv", encoding="utf-8-sig", newline="") as f:
    b = [x for x in csv.DictReader(f) if x.get("entity_id") == eid]
print("budget rows", len(b))
for x in b:
    print(x.get("year"), x.get("amount_eur"), (x.get("metric") or x.get("line_item") or x.get("notes") or "")[:90])
with open("docs/doge/data/leaderboard.csv", encoding="utf-8-sig", newline="") as f:
    lb = [x for x in csv.DictReader(f) if eid in (x.get("entity_id") or "") or "psychogeriatr" in (x.get("item_id") or "").lower()]
print("lb", len(lb))
for x in lb[:3]:
    print(x.get("item_id"), x.get("amount_eur_low"), x.get("priority_index"))

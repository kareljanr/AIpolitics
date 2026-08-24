# -*- coding: utf-8 -*-
import csv
csv.field_size_limit(10_000_000)
needles = ["pieds", "0407884307", "atelier_namur", "l'atelier", "latelier"]
with open("docs/doge/data/budgets.csv", encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f):
        s = str(r).lower()
        if any(n in s for n in needles):
            print(r.get("budget_id"), r.get("entity_id"), (r.get("notes") or "")[:100])
print("---entities---")
with open("docs/doge/data/entities.csv", encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f):
        s = str(r).lower()
        if any(n in s for n in needles):
            print(r.get("entity_id"), (r.get("notes") or "")[:100])

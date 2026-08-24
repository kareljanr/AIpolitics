import csv
csv.field_size_limit(10**7)
with open("docs/doge/data/budgets.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
hits = [r for r in rows if "kindervriend" in r.get("budget_id", "").lower() or r.get("entity_id") == "vzw_mpi_de_kindervriend_kortrijk"]
for h in hits:
    print(h)
with open("docs/doge/data/sources.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
hits = [r for r in rows if "kindervriend" in r.get("source_id", "").lower()]
for h in hits:
    print(h)

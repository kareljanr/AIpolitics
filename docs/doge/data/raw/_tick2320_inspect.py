import csv
csv.field_size_limit(10**7)
for name in ["leaderboard", "budgets", "entities", "sources", "commitments", "foi_queue"]:
    with open(f"docs/doge/data/{name}.csv", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    print("===", name, "n=", len(rows), "cols=", list(rows[0].keys()) if rows else None)
    hits = [row for row in rows if "kindervriend" in str(row).lower()]
    if hits:
        for k, v in hits[-1].items():
            s = v if isinstance(v, str) else str(v)
            print(f"  {k}={s[:200]}")

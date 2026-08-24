import csv, re
csv.field_size_limit(10**7)
with open("docs/doge/data/entities.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
for r in rows:
    notes = r.get("notes") or ""
    eid = r.get("entity_id") or ""
    blob = (notes + " " + eid).lower()
    if any(x in blob for x in ["eta", "maatwerk", "88.993", "aviq"]):
        m = re.search(r"tick(\d+)", notes)
        t = int(m.group(1)) if m else 0
        if t >= 2220:
            name = (r.get("name_en") or r.get("name_nl") or "")[:55]
            kbo = re.search(r"KBO\s*([0-9.]+)", notes)
            kb = kbo.group(1) if kbo else "?"
            print(f"tick{t} {eid} {kb} {name}")

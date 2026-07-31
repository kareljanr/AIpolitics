import json
import collections
from pathlib import Path

meta = json.load(open("docs/doge/data/raw/brugge_subs_meta.json", encoding="utf-8"))
ds = meta.get("dataset", meta)
print("title", ds.get("metas", {}).get("default", {}).get("title"))
print(
    "records",
    ds.get("metas", {}).get("default", {}).get("records_count") or ds.get("records_count"),
)
fields = ds.get("fields", [])
print("FIELDS:")
for f in fields:
    print(" ", f.get("name"), f.get("type"), (f.get("label") or "")[:60])

data = json.load(open("docs/doge/data/raw/brugge_subs_full.json", encoding="utf-8"))
print("rows", len(data))
print("sample", data[0] if data else None)

# discover year/amount field names
keys = set()
for r in data[:50]:
    keys.update(r.keys())
print("keys", sorted(keys))

# guess amount fields
amount_keys = [k for k in keys if any(x in k.lower() for x in ("bedrag", "amount", "euro", "subsidie", "totaal"))]
year_keys = [k for k in keys if any(x in k.lower() for x in ("jaar", "year", "annee", "periode", "boek"))]
name_keys = [k for k in keys if any(x in k.lower() for x in ("naam", "name", "organisatie", "begunstigde", "ontvanger", "derde"))]
print("amount_keys", amount_keys)
print("year_keys", year_keys)
print("name_keys", name_keys)

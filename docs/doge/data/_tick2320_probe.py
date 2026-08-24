# -*- coding: utf-8 -*-
import csv
csv.field_size_limit(10**7)
needles = [
    "heilig_hart_grimbergen",
    "groep_intro",
    "groep_maatwerk",
    "annuntiaten",
    "zorg_en_welzijn",
    "ocura",
    "ter_burg",
    "vincentius",
    "groep_zorg_h_familie",
    "de_ploeg",
    "vlotter",
]
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
for n in needles:
    hits = [r.get("entity_id") for r in rows if n in (r.get("entity_id") or "").lower()]
    print(n, hits[:4] if hits else "MISSING")

with open("docs/doge/data/budgets.csv", encoding="utf-8-sig", newline="") as f:
    b = [x for x in csv.DictReader(f) if "heilig_hart_grimbergen" in (x.get("entity_id") or "")]
print("grimbergen budget rows", len(b))
for x in b[:5]:
    print(x.get("year"), x.get("amount_eur"), (x.get("line_item") or "")[:90])

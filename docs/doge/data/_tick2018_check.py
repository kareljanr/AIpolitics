import csv
import sys

csv.field_size_limit(sys.maxsize)
keys = [
    "sint-barbara",
    "sint barbara",
    "vincentius",
    "maria s rustoord",
    "sint-carolus",
    "zilverbos",
    "kanunnik triest",
    "de foyer",
    "0422152314",
    "0418016550",
    "0411600692",
]
with open("docs/doge/data/entities.csv", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
for k in keys:
    hits = [
        x.get("entity_id")
        for x in rows
        if k in " ".join(str(v) for v in x.values()).lower()
    ]
    print(k, hits[:3] if hits else "UNUSED")

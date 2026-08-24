# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
needles = [
    "0411600692",
    "0411.600.692",
    "maria's rustoord",
    "marias rustoord",
    "0413055989",
    "0413.055.989",
    "0446222962",
    "0446.222.962",
    "maagd der armen",
    "0410142031",
    "0410.142.031",
    "0461563315",
    "0461.563.315",
    "0418016550",
    "0418.016.550",
    "vincentius",
    "0409724238",
    "0409.724.238",
    "heilig hart",
    "grimbergen",
    "0480566704",
    "0480.566.704",
    "hof ter lande",
    "haagwinde",
]
blobs = {}
for name in ["entities.csv", "leaderboard.csv", "research_queue.csv", "foi_queue.csv"]:
    with open(Path("docs/doge/data") / name, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    blobs[name] = "\n".join(" | ".join(r.values()) for r in rows).lower()

for n in needles:
    hits = [k for k, b in blobs.items() if n.lower() in b]
    print(("HIT " + ",".join(hits) if hits else "FREE"), n)

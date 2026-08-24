# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
needles = [
    "0449.507.205",
    "0449507205",
    "veilige have",
    "0810.616.132",
    "0810616132",
    "molenheide",
    "0436.595.020",
    "0436595020",
    "seniorencentrum onze lieve vrouw",
    "olv ten rozen",
    "0446.222.962",
    "0446222962",
    "maagd der armen",
    "0409.942.289",
    "0409942289",
    "huize sint",
]
blobs = {}
for name in ["entities.csv", "leaderboard.csv", "research_queue.csv", "foi_queue.csv"]:
    with open(Path("docs/doge/data") / name, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    blobs[name] = "\n".join(" | ".join(r.values()) for r in rows).lower()

for n in needles:
    hits = [k for k, b in blobs.items() if n.lower() in b]
    print(("HIT " + ",".join(hits) if hits else "FREE"), n)

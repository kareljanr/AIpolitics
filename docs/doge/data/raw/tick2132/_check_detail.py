# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
needles = [
    "0411.600.692",
    "maria",
    "0409.724.238",
    "heilig hart",
    "0446.222.962",
    "maagd",
    "0480.566.704",
    "hof ter lande",
    "0413.055.989",
    "0410.142.031",
    "0461.563.315",
    "0418.016.550",
]
for name in ["entities.csv", "leaderboard.csv", "research_queue.csv"]:
    print("====", name)
    with open(Path("docs/doge/data") / name, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        blob = " | ".join(r.values()).lower()
        if any(n.lower() in blob for n in needles):
            # print short
            keys = list(r.keys())
            tid = r.get("task_id") or r.get("entity_id") or r.get("item_id") or r.get("lb_id") or ""
            title = (
                r.get("title")
                or r.get("name_nl")
                or r.get("name")
                or r.get("notes")
                or ""
            )
            print(tid[:40], "|", title[:140])

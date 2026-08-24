import csv
import re

csv.field_size_limit(10**7)
base = r"C:\Users\karel\dev\AIpolitics\docs\doge\data"
needles = [
    "0422152314",
    "sint-barbara",
    "sint barbara",
    "herselt",
    "0413055989",
    "0416337262",
    "vrijzicht",
    "0421031171",
    "onze-lieve-vrouw",
    "roosdaal",
    "0639973732",
    "den akker",
    "0409724238",
    "heilig hart",
    "grimbergen",
    "0467355403",  # de linde lievegem
    "de linde",
    "lievegem",
    "0893863017",  # faro
    "0201712587",  # aiesh
    "0644638937",  # rew
]

files = [
    "entities.csv",
    "commitments.csv",
    "leaderboard.csv",
    "budgets.csv",
    "research_queue.csv",
]
for needle in needles:
    hits = []
    for fn in files:
        with open(f"{base}\\{fn}", encoding="utf-8", newline="") as f:
            for i, row in enumerate(csv.DictReader(f), 1):
                blob = " ".join((v or "") for v in row.values()).lower()
                if needle.lower() in blob:
                    tid = list(row.values())[0]
                    hits.append(f"{fn}:{tid}")
                    if len(hits) >= 3:
                        break
        if len(hits) >= 3:
            break
    print(f"{needle!r}: {hits[:3] if hits else 'UNUSED'}")

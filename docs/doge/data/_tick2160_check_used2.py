import csv

csv.field_size_limit(10**7)
base = r"C:\Users\karel\dev\AIpolitics\docs\doge\data"
needles = [
    "0411600692",
    "maria",
    "moorslede",
    "0461563315",
    "sint-michiels",
    "0480566704",
    "hof ter lande",
    "vorselaar",
    "0433419259",
    "wezembeek",
    "0479401318",
    "ter burg",
    "0428471856",
    "ocura",
    "0845895824",  # hertog already
    "0454543856",
]
files = ["entities.csv", "commitments.csv", "leaderboard.csv", "research_queue.csv"]
for needle in needles:
    hits = []
    for fn in files:
        with open(f"{base}\\{fn}", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                blob = " ".join((v or "") for v in row.values()).lower()
                if needle.lower() in blob:
                    hits.append(f"{fn}:{list(row.values())[0]}")
                    if len(hits) >= 2:
                        break
        if len(hits) >= 2:
            break
    print(f"{needle!r}: {hits[:2] if hits else 'UNUSED'}")

import re
import csv

csv.field_size_limit(10**7)

html = open(
    "docs/doge/data/raw/tick2072/mater_amabilis_en.html",
    encoding="utf-8",
    errors="replace",
).read()
print("turnover FAQ:", re.search(r"recorded a total turnover of ([^.<]+)", html).group(1))
print("filed:", re.search(r"were filed on ([0-9-]+)", html).group(1))
print("FTE:", re.search(r'amountOfEmployees = "([^"]+)"', html).group(1))
for y in ["2025", "2024"]:
    block = re.search(y + r"\s*:\s*\{[^}]+\}", html)
    print(block.group(0) if block else y + " missing")

# percent changes from CW table cells
for label in ["Profit/Loss", "Turnover", "Equity", "Gross margin"]:
    m = re.search(
        label + r".{0,500}?€\s*([0-9][0-9.,]*)\s*</td>\s*<td[^>]*>\s*([^<]+)",
        html,
        re.S,
    )
    if m:
        print(label, m.group(1), m.group(2).strip()[:40])

print("--- last CSV ids ---")
for f in ["sources", "budgets", "commitments", "leaderboard", "entities", "foi_queue"]:
    with open(f"docs/doge/data/{f}.csv", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    last = rows[-1]
    first_key = list(last.keys())[0]
    print(f, first_key, "=", last[first_key])

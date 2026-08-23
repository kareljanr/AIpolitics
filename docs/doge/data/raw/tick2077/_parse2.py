# Deeper parse of De Zwaluw CW tables
import re
from pathlib import Path
from html.parser import HTMLParser

RAW = Path(__file__).parent
t = (RAW / "zwaluw_en.html").read_text(encoding="utf-8", errors="replace")

# Find FTE value near year 2025 header
idx = t.find(">                             2025")
print("2025 header idx", idx)
print(t[idx - 200 : idx + 800].replace("\n", " ")[:900])

# Extract all rows that look like financial metric rows with multiple euro spans
# Pattern: label ... then several € amounts
# Find section "Key figures" or similar
for needle in [
    "Key figures",
    "Kerncijfers",
    "Turnover",
    "Profit/Loss",
    "Equity",
    "Gross margin",
    "Total assets",
    "Workforce",
    "FTE",
    "Debts",
    "Employees",
]:
    positions = [m.start() for m in re.finditer(re.escape(needle), t)]
    print(f"\n{needle} positions: {positions[:5]}")

# Pull table after Turnover label - get surrounding HTML
m = re.search(
    r"Turnover</i>.*?€\s*</span>\s*<span>\s*([0-9,\.]+)</span>",
    t,
    re.S,
)
print("\nTurnover latest:", m.group(1) if m else None)

# Better: find all metric rows with yoy %
# Structure from earlier extract: Turnover 5,443 -0.42%
rows = re.findall(
    r"(Turnover|Profit/Loss|Equity|Gross margin|Total assets|Debts|Workforce|FTE|Employees|Added value|Staff costs)"
    r".{0,600}?"
    r"€\s*</span>\s*<span>\s*([0-9,\.\-]+)</span>"
    r".{0,400}?"
    r">\s*([+\-]?[0-9,\.]+)\s*%",
    t,
    re.S | re.I,
)
print("\nmetric rows with yoy:")
for r in rows:
    print(r)

# Multi-year: look for chart config with years
# Sometimes in script tags as years: [2022,2023,2024,2025]
for m in re.finditer(r"\[(?:\s*20\d{2}\s*,){2,5}\s*20\d{2}\s*\]", t):
    print("year array", m.group(0), "at", m.start())

# Find all script type application/json
jsons = re.findall(r"<script[^>]*type=\"application/json\"[^>]*>(.*?)</script>", t, re.S)
print("json scripts", len(jsons), [len(j) for j in jsons[:5]])

# Look for vue/nuxt payload
for pat in [r"__NUXT__", r"window\.__", r"financialYears", r"key_figures", r"omzet"]:
    if re.search(pat, t, re.I):
        print("found pat", pat)

# Extract 4-year history from comparison table - often years as headers then cells
# Print a chunk around first Turnover euro
idx2 = t.find("5,443,008")
print("\nAROUND TURNOVER VALUE:")
print(t[idx2 - 500 : idx2 + 1500])

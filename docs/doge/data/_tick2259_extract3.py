# -*- coding: utf-8 -*-
import re
from pathlib import Path

t = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2259\erables_en.html").read_text(
    encoding="utf-8", errors="replace"
)

# Find Gross margin section and dump nearby text
for label in ["Gross margin", "Equity", "Employees", "Profit/Loss", "Turnover", "Balance sheet"]:
    i = t.find(label)
    print("====", label, "idx", i)
    if i < 0:
        continue
    chunk = t[i : i + 2500]
    chunk = re.sub(r"<script[\s\S]*?</script>", " ", chunk, flags=re.I)
    text = re.sub(r"<[^>]+>", " | ", chunk)
    text = re.sub(r"\s+", " ", text)
    print(text[:1200])
    print()

# Also look for euro amounts after 2025 header in financial table
m = re.search(r"Financial data from[\s\S]{0,8000}", t, re.I)
if m:
    chunk = re.sub(r"<[^>]+>", " | ", m.group(0))
    chunk = re.sub(r"\s+", " ", chunk)
    print("FINDATA", chunk[:2500])

# Try northdata / pappers style
# Look for data-year attributes
for m in re.finditer(r'data-[a-z-]*year[^=]*=["\']?(202[45])["\']?', t, re.I):
    print("data-year", m.group(0)[:80])

# Find all € amounts with context
amounts = []
for m in re.finditer(r"€\s*([0-9][0-9\s\u00a0,.]*)", t):
    ctx = re.sub(r"\s+", " ", t[max(0, m.start() - 60) : m.end() + 20])
    amounts.append(ctx)
print("euro contexts", len(amounts))
for a in amounts[:40]:
    print("€", a)

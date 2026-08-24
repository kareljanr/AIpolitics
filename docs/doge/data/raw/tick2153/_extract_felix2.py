# -*- coding: utf-8 -*-
import re
from pathlib import Path

t = Path(__file__).resolve().parent.joinpath("sint_felix_en.html").read_text(
    encoding="utf-8", errors="ignore"
)
# year blocks
for y in ["2025", "2024", "2023", "2022"]:
    m = re.search(y + r"\s*:\s*\{([^}]+)\}", t)
    print(y, m.group(1).replace("\n", " ").strip()[:220] if m else "-")

# FTE / employees
for pat in [
    r"Employees</[^>]*>[\s\S]{0,200}?>([0-9.,]+)",
    r"werknemers:\s*\"([^\"]+)\"",
    r"Employees\s*</tooltip>[\s\S]{0,400}?([0-9]+[.,]?[0-9]*)",
    r"Big ([0-9.,]+) FTE",
    r"Medium-sized ([0-9.,]+) FTE",
    r"Groot ([0-9.,]+) FTE",
    r"Middelgroot ([0-9.,]+) FTE",
]:
    m = re.search(pat, t, re.I)
    if m:
        print("FTE_PAT", pat[:40], m.group(1))

# company size line
m = re.search(r"Company size[\s\S]{0,200}?([A-Za-z\-]+ [0-9.,]+ FTE)", t)
print("size", m.group(1) if m else "-")

# activity
m = re.search(r"Principal activity[\s\S]{0,120}?>([^<]{5,80})", t)
print("activity", m.group(1).strip() if m else "-")

# table rows with percentages
rows = re.findall(
    r"(Profit/Loss|Turnover|Equity|Gross margin|Employees)[\s\S]{0,40}?</t[dh]>[\s\S]{0,800}?</tr>",
    t,
    re.I,
)
print("rowcount", len(rows))

# simpler: extract markdown-like table from page text
text = re.sub(r"<[^>]+>", "\n", t)
text = re.sub(r"\n+", "\n", text)
# find financial table section
idx = text.find("Financial data from")
print(text[idx : idx + 1200] if idx >= 0 else "no fin section")

kbo = Path(__file__).resolve().parent.joinpath("sint_felix_kbo.html").read_text(
    encoding="utf-8", errors="ignore"
)
kbo_text = re.sub(r"<[^>]+>", "\n", kbo)
kbo_text = re.sub(r"\n+", "\n", kbo_text)
print("---KBO---")
print(kbo_text[:2500])

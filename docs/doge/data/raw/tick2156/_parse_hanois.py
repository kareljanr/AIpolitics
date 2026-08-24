import re
from pathlib import Path

t = Path(__file__).with_name("hanois_en.html").read_text(encoding="utf-8", errors="replace")
# Extract table-like sequences of euros near financial labels
labels = [
    "Profit/Loss",
    "Turnover",
    "Equity",
    "Gross margin",
    "Employees",
    "Winst/Verlies",
    "Omzet",
    "Eigen vermogen",
    "Brutomarge",
    "Personeel",
]
for lab in labels:
    m = re.search(re.escape(lab) + r"[\s\S]{0,800}", t, re.I)
    if not m:
        continue
    chunk = m.group(0)
    euros = re.findall(r"€\s*([\d\.\s]+(?:,\d+)?)", chunk)
    pcts = re.findall(r"([+\-]?\d+(?:[.,]\d+)?)\s*%", chunk)
    print(lab, "euros", euros[:8], "pcts", pcts[:8])

# FAQ snippets
for pat in [
    r"filed on ([0-9\-]+)",
    r"did not publish any turnover[^.]{0,80}",
    r"gross margin of €([\d,\.]+)",
    r"There are ([\d,\.]+) FTEs",
    r"Last balance sheet year\s*</div>\s*<div[^>]*>\s*(\d{4})",
]:
    m = re.search(pat, t, re.I)
    print("FAQ", pat[:40], "->", m.group(0)[:120] if m else None)

# NL mirror for consistency
tn = Path(__file__).with_name("hanois_nl.html").read_text(encoding="utf-8", errors="replace")
for lab in ["Winst/Verlies", "Omzet", "Eigen vermogen", "Brutomarge", "Personeel"]:
    m = re.search(re.escape(lab) + r"[\s\S]{0,800}", tn, re.I)
    if not m:
        continue
    chunk = m.group(0)
    euros = re.findall(r"€\s*([\d\.\s]+(?:,\d+)?)", chunk)
    pcts = re.findall(r"([+\-]?\d+(?:[.,]\d+)?)\s*%", chunk)
    print("NL", lab, "euros", euros[:8], "pcts", pcts[:8])

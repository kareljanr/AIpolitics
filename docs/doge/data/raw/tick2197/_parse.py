from pathlib import Path
import re

text = Path("docs/doge/data/raw/tick2197/schakel_en.html").read_text(encoding="utf-8", errors="replace")
nl = Path("docs/doge/data/raw/tick2197/schakel_nl.html").read_text(encoding="utf-8", errors="replace")

m = re.search(r"total turnover of .([0-9.,]+)", text)
print("faq_turnover", m.group(1) if m else None)
m = re.search(r"filed on ([0-9-]+)", text)
print("filed", m.group(1) if m else None)
m = re.search(r"There are ([0-9.,]+) FTEs", text)
print("fte_faq", m.group(1) if m else None)
m = re.search(r'window\.cw\.amountOfEmployees\s*=\s*"([^"]+)"', text)
print("emp", m.group(1) if m else None)

# Find financial table block via years header
i = text.find("Profit/Loss")
print("---EN chunk---")
print(text[i : i + 3500])

i = nl.find("Winst/Verlies")
print("---NL chunk---")
print(nl[i : i + 3500])

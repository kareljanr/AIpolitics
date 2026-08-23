from pathlib import Path
import re

t = Path("docs/doge/data/raw/tick2010/zorgkas_en.html").read_text(encoding="utf-8", errors="replace")
m = re.search(r'itemprop="description">\s*<span>([^<]+)</span>', t)
print("desc", m.group(1) if m else None)
for pat in [r'companySize\s*=\s*"([^"]+)"', r'amountOfEmployees\s*=\s*"([^"]+)"', r'startDate\s*=\s*"([^"]+)"']:
    m = re.search(pat, t)
    print(pat, m.group(1) if m else None)

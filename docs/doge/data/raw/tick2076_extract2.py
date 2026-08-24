import re
from pathlib import Path
t = Path(r"docs/doge/data/raw/tick2075/kuurne_en.html").read_text(encoding="utf-8", errors="replace")
# find year labels near omzet block
idx = t.find('omzet: "16,399,438"')
print("idx", idx)
print(t[idx-500:idx+1200])
print("---FTE SEARCH---")
for m in re.finditer(r'.{0,80}FTE.{0,120}', t, re.I):
    s = re.sub(r"\s+", " ", m.group(0))
    if any(ch.isdigit() for ch in s):
        print(s[:200])
print("---EMAIL---")
emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t))
print(sorted(emails)[:30])
print("---YEARS near financial---")
# look for years: array
for pat in [r'years?\s*[:=]\s*\[[^\]]+\]', r'jaren\s*[:=]\s*\[[^\]]+\]', r'labels\s*[:=]\s*\[[^\]]+\]', r'2025[^\n]{0,40}2024', r'boekjaren']:
    ms = re.findall(pat, t, re.I)
    print(pat, ms[:3])
# search personnel
for key in ["Personnel", "staff", "employees", "workforce", "tewerkstelling", "personeel", "Gemiddeld"]:
    i = t.lower().find(key.lower())
    if i>=0:
        print(key, ":", re.sub(r"\s+"," ", t[i:i+250])[:250])

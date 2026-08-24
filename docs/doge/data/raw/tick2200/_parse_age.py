from pathlib import Path
import re

text = Path("docs/doge/data/raw/tick2200/age_en.html").read_text(encoding="utf-8", errors="replace")
print("filed", re.search(r"filed on ([0-9-]+)", text).group(1))
print("empty_omzet", bool(re.search(r"did not publish any turnover|geen omzet", text, re.I)))
parts = re.split(r'title="Section [^"]+"', text)
for p in parts[1:8]:
    lab = re.search(r">\s*([A-Za-z /]+)<", p[:500])
    euros = re.findall(r"<span>€\s*</span>\s*<span>\s*([0-9.,\s-]+)</span>", p)
    plain = re.findall(r"<span>([0-9]+(?:[.,][0-9]+)?)</span>", p)
    pct = re.findall(r"<span>([+-]?[0-9]+,[0-9]+%)</span>", p)
    print(lab.group(1).strip() if lab else "?", euros[:4], plain[:4], pct[:3])

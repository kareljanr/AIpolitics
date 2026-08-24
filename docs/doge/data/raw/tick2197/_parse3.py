from pathlib import Path
import re

text = Path("docs/doge/data/raw/tick2197/schakel_en.html").read_text(encoding="utf-8", errors="replace")

# Split by tooltip title sections
parts = re.split(r'title="Section [^"]+"', text)
print("parts", len(parts))
for p in parts[1:8]:
    # first text label after
    lab = re.search(r">\s*([A-Za-z /]+)<", p[:500])
    # euros
    euros = re.findall(r"<span>€\s*</span>\s*<span>\s*([0-9.,\s-]+)</span>", p)
    plain = re.findall(r"<span>([0-9]+(?:[.,][0-9]+)?)</span>", p)
    pct = re.findall(r"<span>([+-]?[0-9]+,[0-9]+%)</span>", p)
    print("---", lab.group(1).strip() if lab else "?", "euros", euros[:4], "plain", plain[:6], "pct", pct[:4])

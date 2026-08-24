from pathlib import Path
import re

text = Path("docs/doge/data/raw/tick2203/kromme_en.html").read_text(encoding="utf-8", errors="replace")
print("filed", re.search(r"filed on ([0-9-]+)", text).group(1))
print("faq", re.search(r"total turnover of .([0-9.,]+)", text))
m = re.search(r"total turnover of .([0-9.,]+)", text)
print("faq_to", m.group(1) if m else None)
print("empty", bool(re.search(r"did not publish any turnover", text, re.I)))
parts = re.split(r'title="Section [^"]+"', text)
for part in parts[1:8]:
    lab = re.search(r">\s*([A-Za-z /]+)<", part[:500])
    euros = re.findall(r"<span>€\s*</span>\s*<span>\s*([0-9.,\s-]+)</span>", part)
    plain = re.findall(r"<span>([-0-9]+(?:[.,][0-9]+)?)</span>", part)
    pct = re.findall(r"<span>([+-]?[0-9]+,[0-9]+%)</span>", part)
    print(lab.group(1).strip() if lab else "?", "euros", euros[:4], "plain", plain[:6], "pct", pct[:3])

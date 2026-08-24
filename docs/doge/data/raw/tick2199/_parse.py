from pathlib import Path
import re

def parse(path):
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    print("====", path)
    m = re.search(r"filed on ([0-9-]+)", text)
    print("filed", m.group(1) if m else None)
    m = re.search(r"total turnover of .([0-9.,]+)", text)
    print("faq_to", m.group(1) if m else None)
    m = re.search(r'did not publish any turnover|geen omzetcijfers|no turnover', text, re.I)
    print("empty_omzet_hint", bool(m))
    m = re.search(r'window\.cw\.amountOfEmployees\s*=\s*"([^"]+)"', text)
    print("emp", m.group(1) if m else None)
    m = re.search(r"Last balance sheet year[^0-9]*([0-9]{4})", text)
    print("year", m.group(1) if m else None)
    parts = re.split(r'title="Section [^"]+"', text)
    for p in parts[1:8]:
        lab = re.search(r">\s*([A-Za-z /]+)<", p[:500])
        euros = re.findall(r"<span>€\s*</span>\s*<span>\s*([0-9.,\s-]+)</span>", p)
        plain = re.findall(r"<span>([0-9]+(?:[.,][0-9]+)?)</span>", p)
        pct = re.findall(r"<span>([+-]?[0-9]+,[0-9]+%)</span>", p)
        print(lab.group(1).strip() if lab else "?", "euros", euros[:4], "plain", plain[:6], "pct", pct[:3])

parse("docs/doge/data/raw/tick2199/age_en.html")
parse("docs/doge/data/raw/tick2199/talent_en.html")

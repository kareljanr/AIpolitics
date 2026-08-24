from pathlib import Path
import re

text = Path("docs/doge/data/raw/tick2197/schakel_en.html").read_text(encoding="utf-8", errors="replace")


def grab(label):
    # find label then next four money/employee cells
    i = text.find(f">{label}<")
    if i < 0:
        i = text.find(f">{label}<i")
    if i < 0:
        print(label, "NOT FOUND")
        return
    chunk = text[i : i + 4000]
    nums = re.findall(
        r'<span(?: class="[^"]*")?>\s*(?:€\s*)?</span>\s*<span>\s*([0-9.,\s-]+)</span>|<span>\s*([0-9.,]+)\s*</span>',
        chunk,
    )
    flat = []
    for a, b in nums:
        v = (a or b).strip().replace(" ", "")
        if v:
            flat.append(v)
    # also employee plain numbers without euro
    if label == "Employees":
        flat = re.findall(r"<span>([0-9.,]+)</span>", chunk)
    print(label, flat[:12])


for lab in ["Profit/Loss", "Turnover", "Equity", "Gross margin", "Employees"]:
    grab(lab)

# year headers
years = re.findall(r"<span>(202[0-9])</span>", text[text.find("Financial data") : text.find("Financial data") + 3000])
print("years", years[:8])

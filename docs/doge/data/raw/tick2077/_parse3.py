# Extract multi-year CW financial table for De Zwaluw
import re
from pathlib import Path

RAW = Path(__file__).parent
t = (RAW / "zwaluw_en.html").read_text(encoding="utf-8", errors="replace")

# Year headers in the financial comparison table
# Find block containing years 2022-2025 near Turnover
# Extract year order from header row near key figures
year_headers = re.findall(
    r'<div class="font-medium\s*">\s*(202[0-9])\s*</div>', t
)
print("year headers sequence:", year_headers[:20])

# FTE near top
fte_block = t[t.find("FTE") : t.find("FTE") + 2500]
fte_nums = re.findall(r">\s*([0-9]+(?:[,\.][0-9]+)?)\s*<", fte_block)
print("FTE nearby nums:", fte_nums[:30])
print("FTE block snippet:", fte_block[:800].replace("\n", " "))


def row_values(label):
    """Find table row starting with label; collect successive € amounts and %."""
    # Find the tooltip/label cell then following td v-financial spans
    pat = re.compile(
        re.escape(label)
        + r".{0,200}?</td>\s*((?:<td[^>]*>.*?</td>\s*){1,12})",
        re.S | re.I,
    )
    m = pat.search(t)
    if not m:
        return None
    cells = m.group(1)
    euros = re.findall(
        r"€\s*</span>\s*<span>\s*([0-9,\.\-]+)</span>", cells
    )
    pcts = re.findall(r">\s*([+\-]?[0-9,\.]+)\s*%\s*<", cells)
    plain = re.findall(
        r'whitespace-nowrap"[^>]*>\s*<span>\s*([0-9,\.\-]+)\s*</span>', cells
    )
    return {"euros": euros, "pcts": pcts, "plain": plain, "raw_len": len(cells)}


for lab in [
    "Turnover",
    "Profit/Loss",
    "Equity",
    "Gross margin",
    "Employees",
    "FTE",
    "Total assets",
    "Added value",
    "Staff costs",
    "Operating income",
    "Debts",
    "Current assets",
    "Fixed assets",
]:
    r = row_values(lab)
    print(f"\n{lab}:", r)

# Also dump year header context at top of key figures table
idx = t.find("Key figures")
print("\n\nKEY FIGURES SECTION (2k):")
print(t[idx : idx + 2500])

# Check KBO page
kbo = (RAW / "kbo.html").read_text(encoding="utf-8", errors="replace")
print("\n\nKBO title/entity:")
for line in kbo.splitlines():
    if any(
        x in line.lower()
        for x in ["zwaluw", "0431", "naam", "adres", "status", "rechtstoestand"]
    ):
        print(line.strip()[:200])

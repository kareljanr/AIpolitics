# Parse Ten Anker CW EN multi-year table
import re
from pathlib import Path

RAW = Path(__file__).parent
t = (RAW / "tenanker_en.html").read_text(encoding="utf-8", errors="replace")


def row_values(label):
    pat = re.compile(
        re.escape(label) + r".{0,200}?</td>\s*((?:<td[^>]*>.*?</td>\s*){1,12})",
        re.S | re.I,
    )
    m = pat.search(t)
    if not m:
        return None
    cells = m.group(1)
    euros = re.findall(r"€\s*</span>\s*<span>\s*([0-9,\.\-]+)</span>", cells)
    pcts = re.findall(r">\s*([+\-]?[0-9,\.]+)\s*%\s*<", cells)
    plain = re.findall(
        r'whitespace-nowrap"[^>]*>\s*<span>\s*([0-9,\.\-]+)\s*</span>', cells
    )
    # also bare number spans for employees
    if not plain:
        plain = re.findall(r">\s*([0-9]+(?:[,\.][0-9]+)?)\s*<", cells)
    return {"euros": euros, "pcts": pcts, "plain": plain[:8]}


for lab in [
    "Turnover",
    "Profit/Loss",
    "Equity",
    "Gross margin",
    "Employees",
    "FTE",
    "Total assets",
    "Debts",
    "Staff costs",
    "Added value",
]:
    print(lab, row_values(lab))

# meta
for needle in [
    "nursing",
    "Principal activity",
    "filed on",
    "mailto:",
    "8620",
    "Albert",
]:
    idx = t.lower().find(needle.lower())
    if idx >= 0:
        print(needle, "=>", t[idx : idx + 180].replace("\n", " ")[:180])

# KBO
kbo = (RAW / "tenanker_kbo.html").read_text(encoding="utf-8", errors="replace")
for pat in [
    r"Ondernemingsnummer:</td><td[^>]*><strong>([^<]+)",
    r"Naam:</td><td[^>]*>(.*?)</td>",
    r"Adres van de zetel:</td><td[^>]*>(.*?)</td>",
    r"Rechtsvorm:</td><td[^>]*>(.*?)</td>",
    r'mailto:([^"]+)',
    r'Webadres:</td><td[^>]*>.*?href="([^"]+)"',
]:
    m = re.search(pat, kbo, re.S | re.I)
    if m:
        print("KBO", pat[:30], "=>", re.sub(r"<[^>]+>", " ", m.group(1)).strip()[:120])

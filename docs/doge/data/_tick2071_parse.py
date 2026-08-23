# ephemeral parse tick2071 — MSW NZVL details from raw HTML
import re
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2071")
en = (outdir / "msw_en.html").read_text(encoding="utf-8")
nl = (outdir / "msw_nl.html").read_text(encoding="utf-8")
kbo = (outdir / "msw_kbo.html").read_text(encoding="utf-8")

# strip tags helper for KBO
text = re.sub(r"<script[\s\S]*?</script>", " ", kbo, flags=re.I)
text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
text = re.sub(r"<[^>]+>", " ", text)
text = re.sub(r"&nbsp;", " ", text)
text = re.sub(r"\s+", " ", text)
print("KBO_TEXT_SNIP:", text[:2500])
print("---")

# NACE / activities from CW
for lab in [
    "NACE",
    "Activity",
    "Activiteit",
    "Company number",
    "Ondernemingsnummer",
    "Establishments",
    "Vestigingseenheden",
    "Legal form",
    "Rechtsvorm",
    "Address",
    "Adres",
    "Last balance",
    "filed on",
    "neergelegd",
]:
    i = en.find(lab)
    if i < 0:
        i = nl.find(lab)
    if i >= 0:
        sn = re.sub(r"\s+", " ", (en if lab in en else nl)[i : i + 180])
        print(lab, "->", sn[:160])

# employees / social
for pat in [
    r'Employees\s*=\s*"([^"]+)"',
    r"Average number of employees[^0-9]*([0-9,\.]+)",
    r"Gemiddeld aantal werknemers[^0-9]*([0-9,\.]+)",
    r"code\s*1003[^0-9]*([0-9,\.]+)",
]:
    m = re.search(pat, en, re.I) or re.search(pat, nl, re.I)
    print("PAT", pat[:40], "->", m.group(1) if m else None)

# look for year-over-year % in page
for pat in [
    r"Turnover[^%]{0,80}?([+\-−]?[0-9,\.]+)\s*%",
    r"Profit[^%]{0,80}?([+\-−]?[0-9,\.]+)\s*%",
    r"Equity[^%]{0,80}?([+\-−]?[0-9,\.]+)\s*%",
    r"Gross margin[^%]{0,80}?([+\-−]?[0-9,\.]+)\s*%",
    r"Omzet[^%]{0,80}?([+\-−]?[0-9,\.]+)\s*%",
    r"Winst[^%]{0,80}?([+\-−]?[0-9,\.]+)\s*%",
]:
    m = re.search(pat, en, re.I) or re.search(pat, nl, re.I)
    print("PCT", pat[:30], "->", m.group(1) if m else None)

# aanbestedende in KBO
print("AANBEST", "aanbestedende" in kbo.lower())
print("VE count hints:")
for m in re.finditer(r"vestiging|eenheid|establishment", kbo, re.I):
    print(" ", re.sub(r"\s+", " ", kbo[m.start() : m.start() + 120])[:100])

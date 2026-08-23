import re
import csv

csv.field_size_limit(10**7)

for name in ["faro_en", "aiesh_en", "rew_en", "mater_en", "mater_nl"]:
    html = open(f"docs/doge/data/raw/tick2073/{name}.html", encoding="utf-8", errors="replace").read()
    y = re.search(r"Last balance sheet year[^0-9]{0,80}([0-9]{4})", html, re.S)
    y2 = re.search(r"Laatste balansjaar[^0-9]{0,80}([0-9]{4})", html, re.S)
    print(name, "EN-year", y.group(1) if y else None, "NL-year", y2.group(1) if y2 else None)

# KBO + site email
kbo = open("docs/doge/data/raw/tick2073/mater_kbo.html", encoding="utf-8", errors="replace").read()
site = open("docs/doge/data/raw/tick2073/mater_site.html", encoding="utf-8", errors="replace").read()
emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", kbo + site)))
print("emails:", emails)
print("KBO status Actief?", "Actief" in kbo)
print("VE:", re.search(r"Aantal vestigingseenheden[^0-9]*([0-9]+)", kbo, re.S))
ve = re.search(r"Aantal vestigingseenheden \(VE\):.*?<[^>]+>\s*<[^>]+>\s*\*?\*?([0-9]+)", kbo, re.S)
print("VE match2:", ve.group(1) if ve else None)
# aanbestedende
print("aanbestedende:", "Aanbestedende overheid" in kbo)

# percents from NL page
nl = open("docs/doge/data/raw/tick2073/mater_nl.html", encoding="utf-8", errors="replace").read()
for label in ["Winst/Verlies", "Omzet", "Eigen vermogen", "Brutomarge", "Personeel"]:
    m = re.search(
        label + r".{0,600}?€\s*([0-9][0-9.\s]*)\s*</td>\s*<td[^>]*>\s*([^<]+)",
        nl,
        re.S,
    )
    if m:
        print("NL", label, m.group(1).strip(), m.group(2).strip()[:50])

en = open("docs/doge/data/raw/tick2073/mater_en.html", encoding="utf-8", errors="replace").read()
for label in ["Profit/Loss", "Turnover", "Equity", "Gross margin"]:
    m = re.search(
        label + r".{0,600}?€\s*([0-9][0-9.,]*)\s*</td>\s*<td[^>]*>\s*([^<]+)",
        en,
        re.S,
    )
    if m:
        print("EN", label, m.group(1).strip(), m.group(2).strip()[:50])
print("filed:", re.search(r"were filed on ([0-9-]+)", en).group(1))
print("turnover FAQ:", re.search(r"recorded a total turnover of ([^.<]+)", en).group(1))

# last leaderboard for pi pattern
with open("docs/doge/data/leaderboard.csv", encoding="utf-8", newline="") as fh:
    rows = list(csv.DictReader(fh))
last = rows[-1]
for k in [
    "item_id",
    "name",
    "annual_cost_eur",
    "absurdity_score",
    "cost_score",
    "difficulty",
    "priority_index",
    "confidence",
    "cut_proposal",
]:
    print("LB", k, "=", (last.get(k) or "")[:120])

# last sources pattern
with open("docs/doge/data/sources.csv", encoding="utf-8", newline="") as fh:
    rows = list(csv.DictReader(fh))
for r in rows[-5:]:
    print("SRC", r["source_id"], r["url"][:80])

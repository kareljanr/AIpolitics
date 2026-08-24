import re
from pathlib import Path

text = Path("docs/doge/raw/tick2221/manus_nbb.txt").read_text(encoding="utf-8")
# normalize
t = re.sub(r"[ \t]+", " ", text)
print("len", len(t))

# look for key codes
codes = [
    "20/58",
    "10/15",
    "17/49",
    "70",
    "9900",
    "9904",
    "62",
    "9087",
    "54/58",
    "29",
]
for c in codes:
    for m in re.finditer(rf"\b{re.escape(c)}\b.{{0,80}}", t):
        chunk = m.group(0).replace("\n", " ")
        if any(ch.isdigit() for ch in chunk):
            print(c, ":", chunk[:120])

# broader money near labels
for lab in [
    "Omzet",
    "Brutomarge",
    "Bedrijfsopbrengsten",
    "Winst",
    "Verlies",
    "Eigen vermogen",
    "Schulden",
    "Totaal der activa",
    "Personeelskosten",
    "Gemiddeld aantal",
]:
    for m in re.finditer(lab, t):
        print("LAB", lab, "->", repr(t[m.start() : m.start() + 160].replace("\n", "|")[:160]))
        break

# extract tables of numbers after VOL-VZW balance pages
# print section around results
idx = t.find("RESULTATENREKENING")
if idx < 0:
    idx = t.lower().find("resultatenrekening")
print("RESULT idx", idx)
if idx >= 0:
    print(t[idx : idx + 2500])

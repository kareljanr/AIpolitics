# -*- coding: utf-8 -*-
import re
import html as H
from pathlib import Path

raw = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2206")


def to_text(path):
    t = path.read_text(encoding="utf-8", errors="replace")
    t = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
    t = re.sub(r"<style[\s\S]*?</style>", " ", t, flags=re.I)
    text = re.sub(r"<[^>]+>", "\n", t)
    text = H.unescape(text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n+", "\n", text)
    return text


def sniff(name, labels):
    text = to_text(raw / name)
    print("====", name)
    # Laatste balansjaar / Last balance
    for pat in [
        r"Laatste balansjaar\s*\n?\s*(20\d{2})",
        r"Last balance sheet year\s*\n?\s*(20\d{2})",
        r"Dernier bilan\s*\n?\s*(20\d{2})",
        r"Bedrijfsgrootte\s*\n?\s*([^\n]+)",
        r"Company size\s*\n?\s*([^\n]+)",
        r"neergelegd op\s*([0-9.\-/]+)",
        r"filed on\s*([0-9.\-/]+)",
        r"Filing date\s*\n?\s*([0-9.\-/]+)",
    ]:
        m = re.search(pat, text, re.I)
        if m:
            print(" ", pat[:40], "->", m.group(1).strip())
    for label in labels:
        m = re.search(re.escape(label) + r"[\s\|]*([^\n]{0,200})", text)
        if m:
            print(" ", label, ":", m.group(0).replace("\n", " | ")[:220])
    # dump finance-ish window
    for key in ["Omzet", "Turnover", "Brutomarge", "Gross margin", "Winst/Verlies", "Profit/Loss", "Eigen vermogen", "Equity"]:
        idx = text.find(key)
        if idx >= 0:
            print(" WIN", key, ":", repr(text[idx : idx + 250]))
    print()


sniff(
    "entiris_en.html",
    [
        "Last balance sheet year",
        "Company size",
        "Turnover",
        "Gross margin",
        "Profit/Loss",
        "Equity",
        "Workforce",
        "Principal activity",
    ],
)
sniff(
    "entiris_nl.html",
    [
        "Laatste balansjaar",
        "Bedrijfsgrootte",
        "Omzet",
        "Brutomarge",
        "Winst/Verlies",
        "Eigen vermogen",
        "Personeel",
        "Hoofdactiviteit",
    ],
)

# Extract year columns from finance tables via HTML structure
html = (raw / "entiris_nl.html").read_text(encoding="utf-8", errors="replace")
# find blocks with € amounts
amounts = re.findall(
    r"(Omzet|Brutomarge|Winst/Verlies|Eigen vermogen|Personeel)[\s\S]{0,120}?€?\s*([-\d.]+(?:\.\d{3})*(?:,\d+)?|\-)",
    html,
)
print("amount-ish pairs", amounts[:20])

# Better: look near table headers 2025 2024
# Companyweb often embeds data in vue/json. Search for 18927215 etc
for needle in ["18927215", "18.927.215", "18,927,215", "3265873", "3.265.873", "92293922", "1448"]:
    print(needle, html.count(needle))

# Extract surrounding for 18.927.215
for m in re.finditer(r"18\.927\.215", html):
    sn = re.sub(r"<[^>]+>", " ", html[max(0, m.start() - 200) : m.end() + 400])
    sn = re.sub(r"\s+", " ", sn)
    print("CTX omzet:", sn[:500])
    break

for m in re.finditer(r"Brutomarge[\s\S]{0,800}?€\s*([\d.]+)", html):
    sn = re.sub(r"<[^>]+>", " ", m.group(0))
    sn = re.sub(r"\s+", " ", sn)
    print("CTX bruto:", sn[:500])
    break

# Prior year values - look for percentage spans near figures
# Grab all € X.XXX.XXX with nearby %
pairs = re.findall(
    r"€\s*([-]?\d{1,3}(?:\.\d{3})+)\s*(?:<[^>]+>\s*)*(?:<[^>]+>[^<]*</[^>]+>\s*)*([+\-]\s*\d+\s*%|)",
    html,
)
print("euro pairs sample", pairs[:30])

# AGB bornem check
agb = to_text(raw / "agb_bornem.html")
print("==== AGB Bornem snippets")
for line in agb.split("\n"):
    if re.search(r"202[45]|AGB|jaarrekening|PDF", line, re.I) and len(line.strip()) > 5:
        print(" ", line.strip()[:160])

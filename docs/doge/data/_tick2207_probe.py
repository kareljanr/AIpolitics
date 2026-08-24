# -*- coding: utf-8 -*-
import re
import html as H
from pathlib import Path

raw = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2207")


def to_text(path):
    t = path.read_text(encoding="utf-8", errors="replace")
    t = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
    t = re.sub(r"<style[\s\S]*?</style>", " ", t, flags=re.I)
    text = H.unescape(re.sub(r"<[^>]+>", "\n", t))
    return re.sub(r"\n+", "\n", text)


def sniff(name):
    text = to_text(raw / name)
    print("====", name)
    for pat in [
        r"Last balance sheet year\s*\n?\s*(20\d{2})",
        r"Laatste balansjaar\s*\n?\s*(20\d{2})",
        r"Company size\s*\n?\s*([^\n]+)",
        r"filed on\s*([0-9.\-/]+)",
        r"neergelegd op\s*([0-9.\-/]+)",
    ]:
        m = re.search(pat, text, re.I)
        if m:
            print(" ", pat[:35], "->", m.group(1).strip())
    for key in [
        "Turnover",
        "Gross margin",
        "Profit/Loss",
        "Equity",
        "Employees",
        "Omzet",
        "Brutomarge",
        "Winst/Verlies",
        "Eigen vermogen",
        "Personeel",
    ]:
        idx = text.find(key)
        if idx >= 0:
            print(" ", key, ":", repr(text[idx : idx + 280]))
    print()


for n in [
    "kemphaan_en.html",
    "kemphaan_nl.html",
    "arcor_en.html",
    "noordheuvel_en.html",
    "agb_bornem.html",
]:
    if (raw / n).exists():
        sniff(n)

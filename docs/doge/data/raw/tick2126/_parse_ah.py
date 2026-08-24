# -*- coding: utf-8 -*-
import re
from pathlib import Path

OUT = Path(__file__).resolve().parent

for fname in ["ah_en.html", "ah_nl.html", "ah_fr.html", "armonea_at_home.html"]:
    p = OUT / fname
    if not p.exists():
        print(fname, "missing")
        continue
    html = p.read_text(encoding="utf-8", errors="ignore")
    print("====", fname, "len", len(html))
    euros = re.findall(r"€\s*([-\d][\d,]*)", html)
    print("euro unique", list(dict.fromkeys(euros))[:50])
    print("Last balance snippet:")
    idx = html.find("Last balance sheet year")
    if idx < 0:
        idx = html.find("Laatste")
    if idx >= 0:
        text = re.sub(r"<[^>]+>", " ", html[idx : idx + 800])
        print(re.sub(r"\s+", " ", text)[:500])
    # Table Graph block
    idx = html.find("Table Graph")
    print("Table Graph", idx)
    if idx > 0:
        text = re.sub(r"<[^>]+>", " ", html[idx : idx + 6000])
        print(re.sub(r"\s+", " ", text)[:1200])
    # FAQ templates filled?
    for pat in [
        r"recorded a total turnover of ([^.]+)\.",
        r"reported a gross margin of ([^.]+)\.",
        r"profit/loss of ([^.]+)\.",
        r"filed on ([0-9-]{10})",
        r"neergelegd op ([0-9./]{8,})",
        r"déposées le ([0-9-]{10})",
        r"([0-9]+(?:[.,]\d+)?)\s*FTE",
    ]:
        ms = re.findall(pat, html, re.I)
        if ms:
            print(pat, ms[:6])
    # look for vue/json numbers near financial keys
    for key in ["omzet", "brutomarge", "eigenVermogen", "winst", "turnover", "grossMargin"]:
        for m in re.finditer(key, html, re.I):
            snippet = html[m.start() : m.start() + 120]
            if any(ch.isdigit() for ch in snippet):
                print("near", key, re.sub(r"\s+", " ", snippet)[:120])
                break
    # FTE context
    for token in ["43,5", "43.5", "Medium-sized"]:
        idx = html.find(token)
        if idx >= 0:
            text = re.sub(r"<[^>]+>", " ", html[max(0, idx - 150) : idx + 200])
            print("ctx", token, re.sub(r"\s+", " ", text)[:300])
            break
    print()

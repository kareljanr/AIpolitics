# -*- coding: utf-8 -*-
import re
from pathlib import Path

raw = Path(__file__).resolve().parent
t = (raw / "annuntiaten_en.html").read_text(encoding="utf-8", errors="ignore")
tn = (raw / "annuntiaten_nl.html").read_text(encoding="utf-8", errors="ignore")
tk = (raw / "annuntiaten_kbo.html").read_text(encoding="utf-8", errors="ignore")

for label, html in [("EN", t), ("NL", tn)]:
    tbodys = re.findall(r"<tbody>(.*?)</tbody>", html, re.S)
    print("====", label, "tbodys", len(tbodys))
    for ti, body in enumerate(tbodys[:2]):
        rows = re.findall(r"<tr>(.*?)</tr>", body, re.S)
        print(" tbody", ti, "rows", len(rows))
        for row in rows[:10]:
            cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)
            clean = []
            for c in cells:
                c = re.sub(r"<[^>]+>", " ", c)
                c = re.sub(r"&nbsp;", " ", c)
                c = re.sub(r"\s+", " ", c).strip()
                if c:
                    clean.append(c[:100])
            if clean:
                print("  ", clean)

# Prefer probes YE
for name in ["faro_en.html", "aiesh_en.html", "rew_en.html", "bornem_en.html"]:
    ht = (raw / name).read_text(encoding="utf-8", errors="ignore")
    m = re.search(
        r"Last balance sheet year</[^>]+>\s*</[^>]+>\s*<[^>]+>\s*(\d{4})",
        ht,
        re.S | re.I,
    )
    if not m:
        m = re.search(r"Last balance sheet year.{0,200}?>(20\d{2})<", ht, re.S | re.I)
    print(name, "YE", m.group(1) if m else "?")

# KBO basics
for pat in [
    r"Ondernemingsnummer:</td><td[^>]*>([^<]+)",
    r"Status:</td><td[^>]*>.*?<strong><span[^>]*>([^<]+)",
    r"Rechtsvorm:</td><td[^>]*>([^<]+)",
    r"Adres van de zetel:</td><td[^>]*>(.*?)</td>",
    r"aanbestedende overheid",
    r"NACE",
]:
    m = re.search(pat, tk, re.S | re.I)
    print("KBO", pat[:40], "->", (m.group(1)[:120] if m and m.lastindex else bool(m)))

# NACE codes from KBO
for m in re.finditer(r"(\d{2}\.\d{3})[^<]{0,80}", tk):
    print("NACE-ish", m.group(0)[:100])

# filing / FAQ from EN
for pat in [
    r"filed on ([0-9\-]+)",
    r"There are ([0-9,\.]+) FTEs",
    r"turnover of €([0-9,\.]+)",
    r"registered office[^.]{0,120}",
]:
    m = re.search(pat, t, re.I)
    print("FAQ", pat[:50], "->", m.group(0)[:140] if m else None)

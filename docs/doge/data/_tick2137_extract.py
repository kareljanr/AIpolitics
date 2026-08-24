# -*- coding: utf-8 -*-
import re
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2137")
en = (base / "corolles_en.html").read_text(encoding="utf-8", errors="replace")
nl = (base / "corolles_nl.html").read_text(encoding="utf-8", errors="replace")
kbo = (base / "corolles_kbo.html").read_text(encoding="utf-8", errors="replace")

# financials
for y in ["2025", "2024", "2023"]:
    mm = re.search(rf"{y}\s*:\s*\{{([^}}]+)}}", en)
    print(y, re.sub(r"\s+", " ", mm.group(1)) if mm else None)

# FTE series
fte = re.findall(r"(202[0-9]).{0,40}(?:fte|Employees).{0,40}|Employees\s*=\s*\"([^\"]+)\"", en, re.I)
print("fte_raw", fte[:10])
# chart data employees
for pat in [
    r"personeel[^\n]{0,200}",
    r"employees\s*:\s*\{[^}]+\}",
    r"2025\s*:\s*\{[^}]*fte[^}]*\}",
    r"averageNumberOfEmployees[^\n]{0,120}",
    r"window\.cw\.[a-zA-Z]*[Ee]mploy",
]:
    m = re.search(pat, en, re.I)
    if m:
        print("pat", pat[:40], re.sub(r"\s+", " ", m.group(0))[:200])

# Extract JS financial year blocks more carefully including fte if present
blocks = re.findall(r"(202[0-9])\s*:\s*\{([^}]+)\}", en)
for y, body in blocks:
    if "winst" in body or "omzet" in body or "fte" in body.lower() or "personeel" in body:
        print("block", y, re.sub(r"\s+", " ", body)[:350])

# Address / activity
for pat in [
    r"Principal activity</[^>]+>\s*<[^>]+>([^<]+)",
    r"Head office[^<]{0,200}",
    r"Registered office[^<]{0,200}",
    r"Establishments[^<]{0,200}",
    r"Number of establishments[^<]{0,80}",
    r"Legal form[^<]{0,80}",
    r"Company number[^<]{0,80}",
    r"VAT[^<]{0,80}",
    r"Start date[^<]{0,80}",
    r"filed on ([0-9\-]+)",
    r"Last balance sheet year[^<]{0,40}",
    r"email[^\"']{0,5}[\"']([^\"']+@[^\"']+)",
    r"info@[a-z0-9\.\-]+",
]:
    m = re.search(pat, en, re.I | re.S)
    if m:
        print("EN", pat[:50], "=>", re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(0)))[:200])

# NL snippets for activity / adres
for pat in [
    r"Hoofdactiviteit.{0,200}",
    r"Maatschappelijke zetel.{0,200}",
    r"Vestigingen.{0,120}",
    r"Rechtsvorm.{0,80}",
    r"neergelegd op ([0-9\.\-]+)",
    r"omzet van € ([0-9\.,]+)",
    r"brutomarge van € ([0-9\.,]+)",
    r"winst van € ([0-9\.,]+)",
    r"eigen vermogen van € ([0-9\.,]+)",
]:
    m = re.search(pat, nl, re.I | re.S)
    if m:
        print("NL", pat[:40], "=>", re.sub(r"<[^>]+>", " ", re.sub(r"\s+", " ", m.group(0)))[:220])

# KBO extract
text = re.sub(r"<script[\s\S]*?</script>", " ", kbo)
text = re.sub(r"<[^>]+>", "\n", text)
text = re.sub(r"\n+", "\n", text)
lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
for i, ln in enumerate(lines):
    if any(
        k in ln.lower()
        for k in [
            "status",
            "actief",
            "adres",
            "tournai",
            "doornik",
            "nace",
            "87.",
            "88.",
            "entiteit",
            "naam",
            "corolles",
            "zetel",
            "start",
            "functie",
        ]
    ):
        ctx = " | ".join(lines[i : i + 3])
        if len(ctx) < 300:
            print("KBO", ctx)

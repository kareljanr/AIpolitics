# -*- coding: utf-8 -*-
import re
from pathlib import Path

out = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2218")
t = (out / "veerkracht4_en.html").read_text(encoding="utf-8", errors="ignore")
tn = (out / "veerkracht4_nl.html").read_text(encoding="utf-8", errors="ignore")
k = (out / "kbo.html").read_text(encoding="utf-8", errors="ignore")

print("amountOfEmployees", re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', t))
print("FTE lines", re.findall(r"([\d,]+)\s*FTE", t)[:10])
print("estabs EN", re.findall(r"Number of establishments.{0,120}?(\d+)", t, re.S | re.I)[:5])
print("NL VTE", re.findall(r"([\d,]+)\s*VTE", tn)[:10])
print("NL vestigingen", re.findall(r"(\d+)\s*[Vv]estiging", tn)[:8])
print("NL bruto faq", re.search(r"brutomarge van Veerkracht 4 is € ([0-9\.,]+)", tn))
print("NL nace", re.findall(r"(88\.\d{3}|81\.\d{3}|43\.\d{3}|94\.\d{3}|41\.\d{3}|39\.\d{3})", tn)[:15])
print("EN nace", re.findall(r"(88\.\d{3}|81\.\d{3}|43\.\d{3}|94\.\d{3}|41\.\d{3}|39\.\d{3})", t)[:15])

# prior year FTE from social balance if present
for y in ["2025", "2024"]:
    m = re.search(rf"{y}.{{0,400}}?(?:fte|employees|werknemers).{{0,40}}?([\d]+[,\.]\d+)", t, re.I | re.S)
    print("fte near", y, m.group(1) if m else None)

# KBO stripped snippets
text = re.sub(r"<[^>]+>", " ", k)
text = re.sub(r"\s+", " ", text)
for needle in [
    "Status van de entiteit",
    "Adres van de zetel",
    "Rechtsvorm",
    "Start datum",
    "Nace code",
    "Aantal vestiging",
    "E-mail",
    "Telefoon",
    "Yv",
    "Serruys",
    "Menen",
]:
    i = text.find(needle)
    if i >= 0:
        print("KBO", needle, "->", text[i : i + 160])

for f in ["site_www.veerkracht4.be.html", "site_contact.html", "site_over.html"]:
    s = (out / f).read_text(encoding="utf-8", errors="ignore")
    emails = sorted(set(re.findall(r"[\w.\-]+@[\w.\-]+\.\w+", s)))
    print(f, "emails", [e for e in emails if "veerkracht" in e.lower() or "info@" in e][:10])
    print(" all emails", emails[:12])

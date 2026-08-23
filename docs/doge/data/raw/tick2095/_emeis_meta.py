# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request
from pathlib import Path

RAW = Path(__file__).resolve().parent
CTX = ssl.create_default_context()
UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

kbo = (RAW / "emeis_kbo.html").read_text(encoding="utf-8", errors="replace")
# NACE links
for m in re.finditer(r"nace\.code=(\d+)[^>]*>\s*([\d.]+)", kbo):
    print("NACE code", m.group(1), m.group(2))
for m in re.finditer(r"87\.\d{3}[^<]{0,80}", kbo):
    print("NACE ctx", re.sub(r"\s+", " ", m.group(0))[:100])

# FTE prior year from EN page if any
en = (RAW / "emeis_en.html").read_text(encoding="utf-8")
# look for employee history - often only current
print("FTE en", re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', en))

# contact pages
for url, name in [
    ("https://www.emeis.be/contact", "emeis_contact.html"),
    ("https://www.emeis.be/nl/contact", "emeis_contact_nl.html"),
    ("https://www.emeis.be/fr/contact", "emeis_contact_fr.html"),
    ("https://www.emeis.be/contactez-nous", "emeis_contact2.html"),
]:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
            html = r.read().decode("utf-8", errors="replace")
        (RAW / name).write_text(html, encoding="utf-8")
        emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)))
        emails = [e for e in emails if "sentry" not in e.lower() and "example" not in e.lower()]
        print("CONTACT", url, emails[:10], "len", len(html))
    except Exception as e:
        print("CONTACT FAIL", url, e)

# check race on rq_2095
import csv

csv.field_size_limit(10**7)
for r in csv.DictReader(open("docs/doge/data/research_queue.csv", encoding="utf-8-sig", newline="")):
    if r["task_id"] in ("rq_2095", "rq_2096"):
        print("RQ", r["task_id"], r.get("status"), (r.get("title") or "")[:80])
print(open("docs/doge/data/loop_state.csv", encoding="utf-8").read())

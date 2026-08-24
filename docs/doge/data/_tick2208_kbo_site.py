# -*- coding: utf-8 -*-
import re
import html as H
from pathlib import Path
from urllib.request import Request, urlopen

RAW = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2208")
UA = "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0; research)"


def fetch(url, name):
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=45) as r:
        data = r.read()
    (RAW / name).write_bytes(data)
    print("OK", name, len(data))


def to_text(path):
    t = path.read_text(encoding="utf-8", errors="replace")
    t = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
    t = re.sub(r"<style[\s\S]*?</style>", " ", t, flags=re.I)
    text = H.unescape(re.sub(r"<[^>]+>", "\n", t))
    return re.sub(r"\n+", "\n", text)


fetch("https://arcor.be/", "site_arcor.html")
fetch("https://arcor.be/contact", "site_arcor_contact.html")

# denser KBO parse
kbo = to_text(RAW / "kbo_arcor.html")
print("===== KBO snippets =====")
# Find VE count nearby
for pat in [
    r"Aantal vestigingseenheden \(VE\):\s*\n?\s*(\d+)",
    r"Rechtsvorm\s*\n\s*([^\n]+)",
    r"Status van de entiteit\s*\n\s*([^\n]+)",
    r"Begindatum\s*\n\s*([^\n]+)",
    r"Afkorting[^\n]*\n\s*([^\n]+)",
    r"88\.993[^\n]*",
    r"85\.322[^\n]*",
    r"Ninovestraat[^\n]*",
    r"info@[^\s]+",
    r"\+32[^\n]*",
]:
    for m in re.finditer(pat, kbo, re.I):
        print(pat[:50], "->", m.group(0)[:120] if m.lastindex is None else m.group(1)[:120])

# Print lines around vestiging / NACE / email
lines = kbo.splitlines()
for i, line in enumerate(lines):
    low = line.lower()
    if any(
        x in low
        for x in [
            "vestigingseenheid",
            "rechtsvorm",
            "status van",
            "begindatum",
            "afkorting",
            "88.993",
            "ninove",
            "e-mail",
            "telefoon",
            "actief",
            "vereniging",
        ]
    ):
        ctx = " | ".join(lines[j].strip() for j in range(max(0, i - 1), min(len(lines), i + 3)) if lines[j].strip())
        print("CTX:", ctx[:200])

site = to_text(RAW / "site_arcor.html")
print("\n===== SITE =====")
for pat in [r"info@[a-z0-9.-]+", r"\+32[^\n]{0,30}", r"Ninovestraat[^\n]*", r"9600[^\n]*"]:
    m = re.search(pat, site, re.I)
    if m:
        print(m.group(0))

# AGB Bornem — look for 2025
agb = to_text(RAW / "agb_bornem_probe.html")
print("\n===== AGB Bornem =====")
for m in re.finditer(r"20(2[4-6])[^\n]{0,80}", agb):
    print(m.group(0)[:100])
print("jr2025 pdf?", bool(re.search(r"2025.*\.(pdf|xlsx)|jaarrekening.?2025", agb, re.I)))

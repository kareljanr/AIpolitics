# -*- coding: utf-8 -*-
import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
OUT = ROOT / "docs" / "doge" / "data" / "raw" / "tick2254"
t = (OUT / "leseta_annuaire.html").read_text(encoding="utf-8", errors="replace")
slugs = re.findall(r"annuaire-eta/([a-z0-9-]+)/?", t)
c = Counter(slugs)
print("slugs", len(c))
for s, n in sorted(c.items()):
    print(f"{n:3} {s}")

# already taken / skip markers from recent queue notes
SKIP = {
    "gaillettes",
    "les-gaillettes",
    "atelier-les-gaillettes",
    "hunelle",
    "moulin-de-la-hunelle",
    "le-moulin-de-la-hunelle",
    "dauphins",
    "les-dauphins",
    "saupont",
    "le-saupont",
    "serviplast",
    "jean-delcour",
    "jean-del-cour",
    "travco",
    "pilifs",
    "ferme-nos-pilifs",
    "nos-pilifs",
    "jeunes-jardiniers",
    "la-lumiere",
    "apam",
    "jean-gielen",
    "le-perron",
    "latelier",
    "l-atelier",
    "axedis",
    "eta-123",
    "beauraing",
    "manufast",
    "metalgroup",
    "entranam",
    "enghien",
    "entra",
    "ateliers-de-tertre",
    "le-rucher",
    "ate-ensival",
    "ensival",
    "relais-de-la-haute-sambre",
    "relais-haute-sambre",
}

print("\nCANDIDATES (not obviously skipped):")
for s in sorted(c):
    if any(k in s for k in SKIP):
        continue
    print(" ", s)

# check entities.csv for prior ETA coverage
ent_path = ROOT / "docs" / "doge" / "data" / "entities.csv"
csv.field_size_limit(10_000_000)
with ent_path.open(encoding="utf-8", newline="") as f:
    ents = list(csv.DictReader(f))
eta_ents = [
    e
    for e in ents
    if "eta" in (e.get("notes") or "").lower()
    or "88.993" in (e.get("notes") or "")
    or "ETA" in (e.get("name") or "")
    or "eta" in (e.get("entity_id") or "").lower()
]
print("\neta-ish entities", len(eta_ents))
for e in eta_ents[-40:]:
    print(e.get("entity_id"), "|", (e.get("name") or "")[:60], "|", (e.get("kbo") or e.get("enterprise_number") or "")[:20])

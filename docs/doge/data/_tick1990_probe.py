import csv, re, urllib.request
from pathlib import Path

csv.field_size_limit(10**7)
with open("docs/doge/data/entities.csv", newline="", encoding="utf-8") as f:
    hits = [
        row
        for row in csv.DictReader(f)
        if "chba" in ((row.get("entity_id") or "") + (row.get("name_nl") or "")).lower()
        or "bois de l" in ((row.get("name_nl") or "") + (row.get("name_fr") or "")).lower()
        or "0203.980" in (row.get("notes") or "")
        or "humani" in ((row.get("entity_id") or "") + (row.get("name_nl") or "")).lower()
    ]
for h in hits:
    print("HIT", h.get("entity_id"), (h.get("notes") or "")[:100])
print("hits", len(hits))

ua = {"User-Agent": "Mozilla/5.0 DOGEresearch"}
Path("docs/doge/data/raw/tick1990").mkdir(parents=True, exist_ok=True)
for name, url in [
    ("chba_cw_nl.html", "https://www.companyweb.be/nl/0203980409/centre-hospitalier-bois-de-l-abbaye"),
    ("chba_cw_en.html", "https://www.companyweb.be/en/0203980409/centre-hospitalier-bois-de-l-abbaye"),
]:
    data = urllib.request.urlopen(urllib.request.Request(url, headers=ua), timeout=30).read()
    Path("docs/doge/data/raw/tick1990", name).write_bytes(data)
    print(name, len(data))

html = urllib.request.urlopen(
    urllib.request.Request(
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0203980409",
        headers=ua,
    ),
    timeout=30,
).read().decode("utf-8", "ignore")
m = re.search(r"mailto:([^\"']+)", html)
print("email", m.group(1) if m else "NONE")

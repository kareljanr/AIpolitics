import json
import collections
from pathlib import Path

data = json.load(open("docs/doge/data/raw/brugge_subs_full.json", encoding="utf-8"))

years = collections.Counter(r.get("jaar") for r in data)
print("years", sorted(years.items()))

summary = {
    "source": "https://data.brugge.be/explore/dataset/subsidieregister/",
    "dataset": "subsidieregister",
    "tick": 102,
    "rows": len(data),
    "years": {},
    "top20_by_year": {},
    "top_beleidsveld_latest": [],
}

for year in sorted(set(r.get("jaar") for r in data if r.get("jaar"))):
    rows = [r for r in data if r.get("jaar") == year]
    total = sum(float(r.get("bedrag") or 0) for r in rows)
    # aggregate by recipient
    by_rec = collections.defaultdict(float)
    for r in rows:
        name = r.get("ontvangertoelage_beschrijving") or "?"
        by_rec[name] += float(r.get("bedrag") or 0)
    ranked = sorted(by_rec.items(), key=lambda x: -x[1])[:20]
    by_field = collections.defaultdict(float)
    for r in rows:
        by_field[r.get("beleidsveld_beschrijvig") or "?"] += float(r.get("bedrag") or 0)
    summary["years"][str(year)] = {
        "n_rows": len(rows),
        "unique_recipients": len(by_rec),
        "sum_eur": round(total, 2),
    }
    summary["top20_by_year"][str(year)] = [
        {"name": n, "eur": round(a, 2)} for n, a in ranked
    ]
    print(f"\n=== {year} sum={total:,.2f} rows={len(rows)} orgs={len(by_rec)} ===")
    for i, (n, a) in enumerate(ranked[:15], 1):
        print(f"  {i:2}. {a:12,.2f}  {n[:70]}")

# latest year detail by field
latest = max(summary["years"].keys())
rows = [r for r in data if r.get("jaar") == latest]
by_field = collections.defaultdict(float)
for r in rows:
    by_field[r.get("beleidsveld_beschrijvig") or "?"] += float(r.get("bedrag") or 0)
summary["top_beleidsveld_latest"] = [
    {"field": f, "eur": round(a, 2)}
    for f, a in sorted(by_field.items(), key=lambda x: -x[1])[:15]
]
summary["latest_year"] = latest
print(f"\n=== {latest} top fields ===")
for f, a in sorted(by_field.items(), key=lambda x: -x[1])[:12]:
    print(f"  {a:12,.2f}  {f}")

# culture / sport keywords in latest
cult = collections.defaultdict(float)
for r in rows:
    blob = " ".join(
        [
            r.get("beleidsveld_beschrijvig") or "",
            r.get("beleidsitem_beschrijving") or "",
            r.get("actie_beschrijving") or "",
        ]
    ).lower()
    if any(k in blob for k in ("cultuur", "kunst", "museum", "theater", "erfgoed", "bibliotheek")):
        cult[r.get("ontvangertoelage_beschrijving") or "?"] += float(r.get("bedrag") or 0)
print(f"\n=== culture-ish {latest} total {sum(cult.values()):,.2f} orgs {len(cult)} ===")
for i, (n, a) in enumerate(sorted(cult.items(), key=lambda x: -x[1])[:15], 1):
    print(f"  {i:2}. {a:12,.2f}  {n[:70]}")

# known from prior Brugge sample: Concertgebouw, Brugge Plus
for key in ("Concertgebouw", "Brugge Plus", "Entrepot", "Musea", "Cultuurcentrum", "CC Brugge", "Toneel"):
    hits = [
        (r.get("jaar"), r.get("ontvangertoelage_beschrijving"), r.get("bedrag"))
        for r in data
        if r.get("ontvangertoelage_beschrijving")
        and key.lower() in r.get("ontvangertoelage_beschrijving", "").lower()
    ]
    if hits:
        by_y = collections.defaultdict(float)
        for y, n, b in hits:
            by_y[y] += float(b or 0)
        print(key, dict(by_y), "rows", len(hits))

Path("docs/doge/data/raw/brugge_subs_top_tick102.json").write_text(
    json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
)
print("\nwrote raw/brugge_subs_top_tick102.json latest", latest)

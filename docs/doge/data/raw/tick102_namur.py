import json
import collections
from pathlib import Path

meta = json.load(open("docs/doge/data/raw/namur_subsides_meta.json", encoding="utf-8"))
ds = meta.get("dataset", meta)
print("title", ds.get("metas", {}).get("default", {}).get("title"))
print("records", ds.get("metas", {}).get("default", {}).get("records_count") or ds.get("records_count"))
fields = ds.get("fields", [])
print("FIELDS:")
for f in fields:
    print(" ", f.get("name"), f.get("type"), (f.get("label") or "")[:50])

data = json.load(open("docs/doge/data/raw/namur_subsides_full.json", encoding="utf-8"))
print("rows", len(data))
print("sample", data[0] if data else None)

years = collections.Counter(r.get("annee") for r in data)
print("years", sorted(years.items()))

summary = {
    "source": "https://data.namur.be/explore/assets/subsides-attribues/",
    "dataset": "subsides-attribues",
    "tick": 102,
    "rows": len(data),
    "years": {},
    "top15_by_year": {},
}

for year in sorted(set(r.get("annee") for r in data if r.get("annee") is not None)):
    rows = [r for r in data if r.get("annee") == year]
    total_bf = sum(float(r.get("budget_final") or 0) for r in rows)
    total_eng = sum(float(r.get("engagements") or 0) for r in rows)
    by_budget = collections.Counter(r.get("budget") for r in rows)
    summary["years"][str(year)] = {
        "n": len(rows),
        "budget_final_sum": round(total_bf, 2),
        "engagements_sum": round(total_eng, 2),
        "by_budget_type": dict(by_budget),
    }
    ranked = sorted(rows, key=lambda r: -float(r.get("budget_final") or 0))[:15]
    summary["top15_by_year"][str(year)] = [
        {
            "libelle": r.get("libelle"),
            "budget_final": float(r.get("budget_final") or 0),
            "engagements": float(r.get("engagements") or 0),
            "budget": r.get("budget"),
            "article": r.get("article"),
        }
        for r in ranked
    ]
    print(f"\n=== {year} n={len(rows)} budget_final={total_bf:,.2f} engagements={total_eng:,.2f} types={dict(by_budget)} ===")
    for i, r in enumerate(ranked, 1):
        print(f"  {i:2}. {float(r.get('budget_final') or 0):10,.2f}  {(r.get('libelle') or '')[:75]}")

# latest year with meaningful data
latest = max(int(y) for y in summary["years"])
summary["latest_year"] = latest
Path("docs/doge/data/raw/namur_subsides_top_tick102.json").write_text(
    json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
)
print("\nwrote raw/namur_subsides_top_tick102.json latest", latest)

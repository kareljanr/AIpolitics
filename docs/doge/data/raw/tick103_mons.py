import fitz
import re
import json
from pathlib import Path

def parse_amount(s: str) -> float:
    return float(s.replace(".", "").replace(",", "."))

doc = fitz.open("docs/doge/data/raw/mons_budget_ord_2025.pdf")
# page 1 totals
p0 = doc[0].get_text()
print("PAGE1 snippet:\n", p0[:800])

# Collect lines with SUBSIDES / ASBL / Associations and extract article + amounts
entries = []
for pi, page in enumerate(doc):
    text = page.get_text()
    # Match article code then label then 63212 or other then amounts
    # Pattern: ARTICLE  LABEL  CODE  amt amt amt amt
    lines = [l.strip() for l in text.splitlines()]
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^(\d{5}/\d{3}-\d{2}(?:/\S+)?)\s*$", line)
        if m:
            article = m.group(1)
            label_parts = []
            j = i + 1
            while j < len(lines) and not re.match(r"^\d{5}/", lines[j]) and not re.match(r"^\d{3}/\d{3}/", lines[j]):
                if re.match(r"^\d{5}$", lines[j]) or lines[j] in ("63212", "63121", "63122", "63617", "67111", "61319", "61311", "65104"):
                    break
                if re.match(r"^\d{1,3}(?:\.\d{3})*,\d{2}$", lines[j]):
                    break
                label_parts.append(lines[j])
                j += 1
            # skip econ code
            while j < len(lines) and re.match(r"^\d{5}$", lines[j]):
                j += 1
            amts = []
            while j < len(lines) and re.match(r"^\d{1,3}(?:\.\d{3})*,\d{2}$", lines[j]):
                amts.append(parse_amount(lines[j]))
                j += 1
            label = " ".join(label_parts)
            if amts and re.search(
                r"SUBSIDE|ASBL|Association|FONDATION MONS|MARS |OFFICE DU TOURISME|MAISON DU TOURISME|CHARTE|FORUM ASSOCIATIF|INFOR JEUNES|JEUNESSE|MUSEE|CULTURE|TOURISME|REGIE DES QUARTIERS|PRO VELO|COMMERCANTS|PORT DE PLAISANCE|SAINT GEORGES|FIBBC|AIDES ALIMENTAIRES",
                label,
                re.I,
            ):
                entries.append(
                    {
                        "page": pi + 1,
                        "article": article,
                        "label": label,
                        "amounts": amts,
                        "y2025": amts[-1] if amts else None,
                        "y2023": amts[0] if len(amts) > 0 else None,
                        "y2024_compte_or_budget": amts[1] if len(amts) > 1 else None,
                    }
                )
            i = j
            continue
        i += 1

# sort by 2025 amount
entries_sorted = sorted(entries, key=lambda e: -(e["y2025"] or 0))
print(f"\nFound {len(entries)} subsidy-like lines\n")
for e in entries_sorted[:40]:
    print(f"{e['y2025']:12,.2f} | {e['article']} | {e['label'][:70]} | p{e['page']} amts={e['amounts']}")

# key culture package sum (filter)
culture_keys = re.compile(
    r"MARS |FONDATION MONS|FESTIVAL|PLAZA|CHARTE|ASSOCIATIONS CULTURE|MUSEE|THEATRE|FILM|SAINT GEORGES|ART\.27|PROCESSION|BEATLES|JUMELAGES|ASSOCIATIONS FESTIVES|PROMOTION DES ACTIVITES|FEUX DE|VOLET MUSICAL",
    re.I,
)
cult = [e for e in entries if culture_keys.search(e["label"] or "")]
print("\nCulture-ish sum 2025", sum(e["y2025"] or 0 for e in cult), "n", len(cult))
for e in sorted(cult, key=lambda x: -(x["y2025"] or 0))[:25]:
    print(f"  {e['y2025']:10,.2f}  {e['label'][:65]}")

summary = {
    "source": "https://www.mons.be/fr/ma-commune/vie-politique/budgets",
    "file": "mons_budget_ord_2025.pdf",
    "tick": 103,
    "budget_2025_recettes": 246241165.81,
    "budget_2025_depenses": 244180817.50,
    "result_presumed_2026_start": 2060348.31,
    "column_note": "Amounts columns typically: Compte 2023, Compte/Budget 2024 variants, Prévision Conseil 2025 (last filled used as y2025)",
    "top_subsidy_lines_2025": [
        {
            "article": e["article"],
            "label": e["label"],
            "eur_2025": e["y2025"],
            "amounts": e["amounts"],
            "page": e["page"],
        }
        for e in entries_sorted[:50]
    ],
    "culture_ish_sum_2025": round(sum(e["y2025"] or 0 for e in cult), 2),
    "culture_ish_lines": [
        {"label": e["label"], "eur_2025": e["y2025"], "article": e["article"]}
        for e in sorted(cult, key=lambda x: -(x["y2025"] or 0))
    ],
}
Path("docs/doge/data/raw/mons_l5_top_tick103.json").write_text(
    json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
)
print("\nwrote mons_l5_top_tick103.json")

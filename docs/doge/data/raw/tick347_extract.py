import re
from pathlib import Path

raw = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw")

for name in ["fwo_jv_2024.txt", "fwo_jv_2025.txt", "fnrs_ra_2024.txt"]:
    t = (raw / name).read_text(encoding="utf-8", errors="replace")
    print("=" * 60, name)
    # pages mentioning budget totals
    pages = t.split("---PAGE")
    for p in pages:
        # score for financial overview pages
        keys = [
            "inkomsten",
            "uitgaven",
            "begroting",
            "toelage",
            "subsidie",
            "totaal",
            "budget",
            "dotation",
            "recettes",
            "dépenses",
            "charges",
            "produits",
            "millions",
            "miljoen",
            "805",
            "resultaat",
            "bilan",
            "compte",
        ]
        low = p.lower()
        score = sum(1 for k in keys if k in low)
        has_eur = bool(re.search(r"\d{1,3}[\s.]\d{3}[\s.]\d{3}|\d{2,3}\s*miljoen|\d{2,3}\s*million", p))
        if score >= 4 and has_eur and len(p) > 200:
            # print first 2500 chars of promising pages
            head = p[:40].replace("\n", " ")
            # only print if looks like summary finance
            if any(
                x in low
                for x in [
                    "inkomsten",
                    "uitgaven",
                    "dotation",
                    "recettes",
                    "dépenses",
                    "charges d",
                    "totales",
                    "totaal",
                    "budget alloué",
                    "vl.a. middelen",
                    "vlaamse",
                ]
            ):
                print("---", head)
                # extract money lines
                for line in p.splitlines():
                    l = line.strip()
                    if re.search(
                        r"(\d[\d\s.,]{4,}|miljoen|million|€|EUR|toelage|dotation|subsid|inkomst|uitgave|budget|recette|dépense|charge)",
                        l,
                        re.I,
                    ):
                        if 5 < len(l) < 160:
                            print(l)
                print()

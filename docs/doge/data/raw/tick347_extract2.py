import re
from pathlib import Path

raw = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw")

# FWO 2024 pages 8-20 (finance overview often early)
for name in ["fwo_jv_2024.txt", "fwo_jv_2025.txt"]:
    t = (raw / name).read_text(encoding="utf-8", errors="replace")
    pages = t.split("---PAGE")
    print("=" * 50, name, "pages", len(pages) - 1)
    for i, p in enumerate(pages[1:25], 1):
        if any(
            x in p
            for x in [
                "Algemeen totaal",
                "inkomsten",
                "Inkomsten",
                "Vlaamse middelen",
                "toelage",
                "Tabel 1",
                "Tabel 2",
                "Tabel 3",
                "436.",
                "begroting",
            ]
        ):
            print(f"\n##### PAGE {i} #####")
            print(p[:4000])

print("\n\n==== FNRS search ====")
t = (raw / "fnrs_ra_2024.txt").read_text(encoding="utf-8", errors="replace")
# find totals
for pat in [
    r".{0,40}(dotation|budget total|total des|millions d|M€|MEUR|recettes|charges).{0,80}",
    r".{0,20}\d{1,3}[\s.]\d{3}[\s.]\d{3}.{0,40}",
]:
    hits = re.findall(pat, t, re.I)
    print("pattern hits", len(hits))
    for h in hits[:40]:
        if isinstance(h, tuple):
            h = "".join(h)
        h = " ".join(h.split())
        if len(h) > 20:
            print(h[:180])

# print pages with "CHIFFRES" or budget chapter
pages = t.split("---PAGE")
for i, p in enumerate(pages[1:], 1):
    if any(
        x in p
        for x in [
            "CHIFFRES-CLÉS",
            "Chiffres-clés",
            "BUDGET",
            "Dotation",
            "dotation de la",
            "TOTAL GÉNÉRAL",
            "Total des engagements",
            "Recettes",
            "180",
            "200 million",
        ]
    ) and (
        "dotation" in p.lower()
        or "budget" in p.lower()
        or "chiffres" in p.lower()
        or "recettes" in p.lower()
    ):
        if i < 30 or "dotation" in p.lower()[:500] or "CHIFFRES" in p[:200]:
            print(f"\n##### FNRS PAGE {i} #####")
            print(p[:3500])

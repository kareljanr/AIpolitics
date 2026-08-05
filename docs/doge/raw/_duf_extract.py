import fitz
from pathlib import Path

doc = fitz.open(r"docs/doge/raw/duffel_jr2025.pdf")
pages = list(range(126, 135)) + list(range(142, 152)) + list(range(185, 190))
out = []
for i in pages:
    out.append(f"\n======== PAGE {i+1} ========\n" + doc[i].get_text())
Path(r"docs/doge/raw/_duf_extract.txt").write_text("\n".join(out), encoding="utf-8")
print("wrote", len(pages), "pages chars", sum(len(x) for x in out))
# also cover/KBO search first 20 pages of financial section
for i in range(120, 128):
    t = doc[i].get_text()
    if "020" in t or "KBO" in t or "Algemeen directeur" in t or "Financieel" in t:
        print("---", i + 1, "---")
        print(t[:1500])

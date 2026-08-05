import fitz
from pathlib import Path

doc = fitz.open(r"docs/doge/raw/bonheiden_jr2025.pdf")
pages = list(range(55, 62)) + list(range(66, 74)) + [142, 143, 144, 145, 146]
out = []
for i in pages:
    if i < len(doc):
        out.append(f"\n======== PAGE {i+1} ========\n" + doc[i].get_text())
Path(r"docs/doge/raw/_bon_extract.txt").write_text("\n".join(out), encoding="utf-8")
print("wrote", len(out), "chars", sum(len(x) for x in out))

import fitz
from pathlib import Path
doc = fitz.open("docs/doge/raw/kampenhout_jr2025.pdf")
parts = []
for p in [1,38,39,40,41,42,43,54,55,56,57,58,91,92]:
    parts.append(f"\n======== PAGE {p} ========\n" + doc[p-1].get_text())
for i in range(92, 110):
    t = doc[i].get_text()
    if "Gecumuleerd overschot" in t and "Tussenkomst" in t:
        parts.append(f"\n======== PAGE {i+1} EQUITY ========\n" + t)
        break
Path("docs/doge/raw/_kam_extract.txt").write_text("".join(parts), encoding="utf-8")
print(Path("docs/doge/raw/_kam_extract.txt").read_text(encoding="utf-8")[:16000])

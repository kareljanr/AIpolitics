import pypdf, re
from pathlib import Path
r=pypdf.PdfReader(r"docs/doge/raw/tick1725/go_jr2024.pdf")
out=[]
for i in range(78,94):
    t=r.pages[i].extract_text() or ""
    out.append(f"===== PAGE {i+1} =====\n{t}")
Path(r"docs/doge/raw/tick1725/go_jr2024_finance_extract.txt").write_text("\n\n".join(out), encoding="utf-8")
print("wrote", sum(len(x) for x in out))
# print key pages fully
for i in [84,85,87,88,89,90,91,92]:
    print(f"\n######## PAGE {i+1} ########")
    print(r.pages[i].extract_text() or "")

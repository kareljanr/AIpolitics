import pypdf
from pathlib import Path
r=pypdf.PdfReader(r"docs/doge/raw/tick1726/erfpunt_nbb_2026-00165556.pdf")
parts=[]
for i,p in enumerate(r.pages):
    t=p.extract_text() or ""
    parts.append(f"===== PAGE {i+1} =====\n{t}")
    print(f"--- page {i+1} chars {len(t)}")
    if i>=4:  # print finance pages
        print(t[:2000])
        print("====")
Path(r"docs/doge/raw/tick1726/erfpunt_extract.txt").write_text("\n\n".join(parts), encoding="utf-8")
print("saved extract")

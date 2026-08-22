import pypdf, re
r=pypdf.PdfReader(r"docs/doge/raw/tick1724/natuurpunt_jr2025_official.pdf")
for i in [0,1,13,14,15]:
    t=r.pages[i].extract_text() or ""
    print("===== PAGE", i+1, "chars", len(t), "=====")
    print(t)
    print()

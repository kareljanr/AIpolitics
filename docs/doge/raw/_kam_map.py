import fitz
doc = fitz.open("docs/doge/raw/kampenhout_jr2025.pdf")
print(doc[1].get_text()[:2500])
print("---")
print(doc[2].get_text()[:1500])
print("---")
print(doc[3].get_text()[:1500])
print("---")
print(doc[4].get_text()[:1500])
for i in range(doc.page_count):
    t = doc[i].get_text()
    if any(k in t for k in ["J2:", "J4:", "J5:", "T2:", "T4:", "KENGETALLEN", "financieel evenwicht", "Mutatiestaat van het nettoactief"]):
        lines = [x.strip() for x in t.strip().splitlines() if x.strip()][:3]
        print(f"p{i+1}: {lines}")

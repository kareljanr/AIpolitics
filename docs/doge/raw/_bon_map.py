import fitz
from pathlib import Path

for name in ["bonheiden_jr2025.pdf", "bonheiden_jr2025_doc.pdf"]:
    path = Path("docs/doge/raw") / name
    doc = fitz.open(path)
    print("===", name, "pages", len(doc), "===")
    print(doc[0].get_text()[:800].replace("\n", " | "))
    keys = ["J2", "J3", "J4", "J5", "T2", "T4", "evenwicht", "Balans", "economische", "financiële schulden", "Mutatiestaat", "tussenkomst"]
    for i in range(len(doc)):
        t = doc[i].get_text()
        head = t[:350]
        for k in keys:
            if k in head:
                print(f"p{i+1}: {head.replace(chr(10),' ')[:160]}")
                break

import fitz
from pathlib import Path

doc = fitz.open(r"docs/doge/raw/duffel_jr2025.pdf")
print("pages", len(doc))
keys = [
    "J2:",
    "J3:",
    "J4:",
    "J5:",
    "T2:",
    "T4:",
    "Mutatiestaat",
    "tussenkomst",
    "financieel evenwicht",
    "Balans",
    "economische aard",
    "financiële schulden",
]
for i in range(len(doc)):
    t = doc[i].get_text()
    head = t[:400]
    for k in keys:
        if k in head or k.lower() in head.lower():
            snip = head.replace("\n", " ")[:180]
            print(f"p{i+1}: {snip}")
            break
print("---P1---")
print(doc[0].get_text()[:600])

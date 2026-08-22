from pypdf import PdfReader
from pathlib import Path

r = PdfReader("docs/doge/raw/tick1752/rand_motivatienota.pdf")
print("pages", len(r.pages))
for i, p in enumerate(r.pages):
    t = p.extract_text() or ""
    # print pages with tables / euros near end
    if i >= 5 or any(k in t.lower() for k in ["overzicht", "18.185", "personeel", "gemeentelijke", "resultaat", "dotatie", "uitgaven"]):
        print(f"\n======== PAGE {i+1} ========")
        print(t)

import re
from pathlib import Path
from pypdf import PdfReader

OUT = Path("docs/doge/raw/tick2223")
pdf = OUT / "manus_bxl_nbb.pdf"
reader = PdfReader(str(pdf))
text = "\n".join((p.extract_text() or "") for p in reader.pages)
(OUT / "manus_bxl_nbb.txt").write_text(text, encoding="utf-8")
print("pages", len(reader.pages), "text", len(text))
print(text[:2500])

# key codes for abbreviated schema
for c in ["20/58", "10/15", "17/49", "70", "9900", "9904", "62", "9087", "73", "70/76"]:
    for m in re.finditer(rf"\b{re.escape(c)}\b.{{0,60}}", text):
        chunk = m.group(0).replace("\n", " ")
        if any(ch.isdigit() for ch in chunk):
            print(c, ":", chunk[:100])

idx = text.lower().find("resultatenrekening")
if idx < 0:
    idx = text.find("RESULTATEN")
print("--- RESULTS ---")
print(text[idx : idx + 2000] if idx >= 0 else "no results")

# CW kern
html = (OUT / "manus_bxl_en.html").read_text(encoding="utf-8")
m = re.search(r"window\.cw\.kernCijfers\s*=\s*\{(.*?)\};", html, re.S)
print("CW kern", m.group(1)[:900] if m else None)
m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
print("emp", m.group(1) if m else None)
m = re.search(r"filed on ([0-9-]+)", html)
print("filed", m.group(1) if m else None)

# KBO
kbo = (OUT / "manus_bxl_kbo.html").read_text(encoding="utf-8")
kt = re.sub(r"<[^>]+>", " ", kbo)
kt = re.sub(r"\s+", " ", kt)
m = re.search(r"Aantal vestigingseenheden \(VE\):\s*(\d+)", kt)
print("VE", m.group(1) if m else None)
m = re.search(r"Adres van de zetel:.{0,120}", kt)
print("addr", m.group(0)[:140] if m else None)
m = re.search(r"Status:\s*(\w+)", kt)
print("status", m.group(1) if m else None)
print("naces", re.findall(r"88\.\d{3}", kt)[:5])
m = re.search(r"Begindatum:.{0,50}", kt)
print("begin", m.group(0) if m else None)
# email from pdf header
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
print("pdf emails", emails[:5])

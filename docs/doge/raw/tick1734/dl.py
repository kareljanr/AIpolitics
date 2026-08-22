import urllib.request, ssl, os, pypdf, re

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
dep = "2026-00272845"
u = f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
out = rf"docs/doge/raw/tick1734/wzc_sintjozef_nbb_{dep}.pdf"
req = urllib.request.Request(u, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=120) as resp:
    data = resp.read()
print("len", len(data), "status", resp.status)
open(out, "wb").write(data)
r = pypdf.PdfReader(out)
print("pages", len(r.pages))
parts = []
for i, p in enumerate(r.pages):
    t = p.extract_text() or ""
    parts.append(f"===== PAGE {i+1} =====\n{t}")
    if i < 15 or re.search(
        r"9900|9904|9901|9087|RESULTAT|ACTIVA|Omzet|Codes Boekjaar|Sint-Jozef|VOL-VZW|VKT|Personeel|9910",
        t,
    ):
        print(f"--- {i+1} chars {len(t)}")
        print(t[:2000])
        print("====")
open(r"docs/doge/raw/tick1734/wzc_sintjozef_extract.txt", "w", encoding="utf-8").write(
    "\n\n".join(parts)
)
print("saved")

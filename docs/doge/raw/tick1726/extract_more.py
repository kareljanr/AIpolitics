import urllib.request, ssl, os, re, pypdf
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
# finish Dommelhof extract - page 4 remainder
r=pypdf.PdfReader(r"docs/doge/raw/tick1726/dommelhof_vzw_nbb_2026-00325874.pdf")
print("P4 FULL:\n", r.pages[3].extract_text())
print("\nP5 FULL:\n", r.pages[4].extract_text())

# Erfpunt deposit
dep="2026-00165556"
u=f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
out=rf"docs/doge/raw/tick1726/erfpunt_nbb_{dep}.pdf"
req=urllib.request.Request(u, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
    data=resp.read()
open(out,"wb").write(data)
print("\nErfpunt len", len(data))
r2=pypdf.PdfReader(out)
print("pages", len(r2.pages))
t0=r2.pages[0].extract_text() or ""
print(t0[:1200])
# identify entity
for i in range(min(5,len(r2.pages))):
    t=r2.pages[i].extract_text() or ""
    if len(t)>80:
        print("---", i+1, t[:800])

import urllib.request, ssl, os, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
# download real JR
u="https://www.natuurpunt.be/system/files/2026-04/Jaarverslag%20Natuurpunt%202025.pdf"
out=r"docs/doge/raw/tick1724/natuurpunt_jr2025_official.pdf"
req=urllib.request.Request(u, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=120) as resp:
    data=resp.read()
    print("JR status", resp.status, "len", len(data), "ctype", resp.getheader("Content-Type"))
open(out,"wb").write(data)
print("saved", os.path.getsize(out))
# extract text pages looking for finance
import pypdf
r=pypdf.PdfReader(out)
print("pages", len(r.pages))
# scan for euro/financ keywords
for i,p in enumerate(r.pages):
    t=p.extract_text() or ""
    if re.search(r"(miljoen|budget|subsid|omzet|kosten|resultaat|balans|€|EUR|financ)", t, re.I):
        print("--- page", i+1, "chars", len(t))
        print(t[:1500])
        print("====")

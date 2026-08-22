import urllib.request, ssl, os
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
# Amnesty VL
dep="2026-00115926"
u=f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
out=rf"docs/doge/raw/tick1725/amnesty_nbb_{dep}.pdf"
req=urllib.request.Request(u, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=90) as resp:
    data=resp.read()
print("amnesty len", len(data))
open(out,"wb").write(data)
import pypdf, re
r=pypdf.PdfReader(out)
print("pages", len(r.pages))
t0=r.pages[0].extract_text() or ""
print("p1", repr(t0[:200]), "chars", len(t0))
# count text pages
text_pages=0
for i,p in enumerate(r.pages):
    t=p.extract_text() or ""
    if len(t)>100:
        text_pages+=1
        if text_pages<=3:
            print("---", i+1, t[:500])
print("text_pages", text_pages)

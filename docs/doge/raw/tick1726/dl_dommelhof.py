import urllib.request, ssl, os, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
# download Dommelhof VZW YE2025
dep="2026-00325874"
u=f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
out=rf"docs/doge/raw/tick1726/dommelhof_vzw_nbb_{dep}.pdf"
req=urllib.request.Request(u, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
    data=resp.read()
print("status", resp.status, "len", len(data))
open(out,"wb").write(data)
import pypdf
r=pypdf.PdfReader(out)
print("pages", len(r.pages))
for i,p in enumerate(r.pages):
    t=p.extract_text() or ""
    print("--- page", i+1, "chars", len(t))
    print(t[:1500] if t else "(empty/image)")
    print("====")

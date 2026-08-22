import urllib.request, ssl, pypdf, os
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
dep="2026-00238663"
u=f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
out=rf"docs/doge/raw/tick1726/dommelhof_nv_nbb_{dep}.pdf"
req=urllib.request.Request(u, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
    data=resp.read()
open(out,"wb").write(data)
print("len", len(data))
r=pypdf.PdfReader(out)
print("pages", len(r.pages))
print(r.pages[0].extract_text() or ""[:1500])

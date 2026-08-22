import urllib.request, ssl, os
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
dep="2026-00394221"
u=f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
out=rf"docs/doge/raw/tick1725/nsz_nbb_{dep}.pdf"
req=urllib.request.Request(u, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=120) as resp:
    data=resp.read()
    print("status", resp.status, "len", len(data), "ctype", resp.getheader("Content-Type"))
open(out,"wb").write(data)
print("saved", os.path.getsize(out))
import pypdf
r=pypdf.PdfReader(out)
print("pages", len(r.pages))
# header page
for i in range(min(3,len(r.pages))):
    t=r.pages[i].extract_text() or ""
    print("--- page", i+1, "chars", len(t))
    print(t[:1200])
# scan all for money codes
import re
for i,p in enumerate(r.pages):
    t=p.extract_text() or ""
    if re.search(r"(9900|9901|9904|20/58|10/15|9087|bruto|personeel|VTE|omzet|Code)", t, re.I) or len(t)>200:
        if i<3: continue
        print("=== page", i+1, "chars", len(t))
        print(t[:2000])
        print("====")

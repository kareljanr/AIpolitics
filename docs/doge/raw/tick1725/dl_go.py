import urllib.request, ssl, os, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
# download GO! JR2024
u="https://publicaties.vlaanderen.be/view-file/77989"
out=r"docs/doge/raw/tick1725/go_jr2024.pdf"
req=urllib.request.Request(u, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=90) as resp:
    data=resp.read()
    print("status", resp.status, "len", len(data), "ctype", resp.getheader("Content-Type"))
open(out,"wb").write(data)
import pypdf
r=pypdf.PdfReader(out)
print("pages", len(r.pages))
# scan for finance
for i,p in enumerate(r.pages):
    t=p.extract_text() or ""
    if re.search(r"(miljoen|€|EUR|begroting|uitgaven|werkingsmiddelen|personeel|financ|budget|balans)", t, re.I):
        print("---", i+1, "chars", len(t))
        print(t[:900])
        print("====")

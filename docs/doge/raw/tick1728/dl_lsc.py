import urllib.request, ssl, os, pypdf, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
dep="2026-00117935"
u=f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
out=rf"docs/doge/raw/tick1728/lsc_oostbrabant_nbb_{dep}.pdf"
req=urllib.request.Request(u, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
    data=resp.read()
print("len", len(data))
open(out,"wb").write(data)
r=pypdf.PdfReader(out)
print("pages", len(r.pages))
parts=[]
for i,p in enumerate(r.pages):
    t=p.extract_text() or ""
    parts.append(f"===== PAGE {i+1} =====\n{t}")
    print("---", i+1, "chars", len(t))
    print(t[:1600] if t else "(empty)")
    print("====")
open(r"docs/doge/raw/tick1728/lsc_oostbrabant_extract.txt","w",encoding="utf-8").write("\n\n".join(parts))

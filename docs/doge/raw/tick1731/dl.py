import urllib.request, ssl, os, pypdf, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}

def cdn_head(dep, year="2026"):
    u=f"http://cdn.staatsbladmonitor.be/{year}pdf/{dep}.pdf"
    try:
        req=urllib.request.Request(u, method="HEAD", headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
            return resp.status, int(resp.getheader("Content-Length") or 0)
    except Exception as e:
        return getattr(e,"code",None), type(e).__name__

for dep,label in [("2026-00394221","NSZ"),("2026-00377886","Dijk92"),("2026-00375176","APEFE"),("2026-00322588","TerEngelen"),("2026-00123787","WitteMeren")]:
    print(label, cdn_head(dep))

# download Ter Engelen (was text before)
dep="2026-00322588"
u=f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
out=rf"docs/doge/raw/tick1731/wzc_terengelen_nbb_{dep}.pdf"
req=urllib.request.Request(u, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=90) as resp:
    data=resp.read()
open(out,"wb").write(data)
print("downloaded", len(data))
r=pypdf.PdfReader(out)
print("pages", len(r.pages))
parts=[]
for i,p in enumerate(r.pages):
    t=p.extract_text() or ""
    parts.append(f"===== PAGE {i+1} =====\n{t}")
    if i < 8 or re.search(r"9900|9904|9087|RESULTAT|ACTIVA|Codes", t):
        print(f"--- {i+1} chars {len(t)}")
        print(t[:1500])
        print("====")
open(r"docs/doge/raw/tick1731/wzc_terengelen_extract.txt","w",encoding="utf-8").write("\n\n".join(parts))
print("saved extract")

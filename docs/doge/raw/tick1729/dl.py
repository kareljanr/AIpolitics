import urllib.request, ssl, os, pypdf, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}

def cdn_get(dep, out):
    u=f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
    req=urllib.request.Request(u, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=90) as resp:
        data=resp.read()
    open(out,"wb").write(data)
    return len(data)

# LSC Noord-Brabant - was 7.8MB
dep="2026-00109506"
out=rf"docs/doge/raw/tick1729/lsc_noordbrabant_nbb_{dep}.pdf"
try:
    n=cdn_get(dep, out)
    print("LSC_NB len", n)
    r=pypdf.PdfReader(out)
    print("pages", len(r.pages))
    t0=r.pages[0].extract_text() or ""
    print("p1 chars", len(t0))
    print(t0[:500])
    text_pages=sum(1 for p in r.pages if len(p.extract_text() or "")>100)
    print("text_pages", text_pages)
except Exception as e:
    print("LSC_NB FAIL", type(e).__name__, getattr(e,"code",None), e)

# if image, try Ter Engelen WZC (812KB)
dep2="2026-00322588"
out2=rf"docs/doge/raw/tick1729/wzc_terengelen_nbb_{dep2}.pdf"
try:
    n2=cdn_get(dep2, out2)
    print("TerEngelen len", n2)
    r2=pypdf.PdfReader(out2)
    print("TE pages", len(r2.pages))
    t0=r2.pages[0].extract_text() or ""
    print("TE p1 chars", len(t0))
    print(t0[:600])
    text_pages=sum(1 for p in r2.pages if len(p.extract_text() or "")>100)
    print("TE text_pages", text_pages)
except Exception as e:
    print("TE FAIL", type(e).__name__, getattr(e,"code",None))

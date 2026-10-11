import urllib.request, ssl, http.cookiejar, json, re
from pathlib import Path
ctx=ssl.create_default_context()
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2473")
REF="2026-00295237"
UID="3f52c368-8055-11f1-8445-8fc15c279710"
RAW="0417400205"

def fetch(url, name, extra=None, method="GET"):
    req=urllib.request.Request(url, method=method)
    req.add_header("User-Agent", UA)
    req.add_header("Accept","*/*")
    if extra:
        for k,v in extra.items():
            req.add_header(k,v)
    try:
        with opener.open(req, timeout=40) as r:
            b=r.read()
            print(method, r.status, name, "len", len(b), "ct", r.headers.get("content-type"), "lm", r.headers.get("last-modified"))
            if name and b:
                (OUT/name).write_bytes(b)
            return r.status, b, dict(r.headers)
    except urllib.error.HTTPError as e:
        print(method, "HTTP", e.code, name, e.read()[:180])
        return e.code, b"", {}
    except Exception as e:
        print(method, "ERR", name, type(e).__name__, e)
        return 0, b"", {}

# CDN
fetch(f"http://cdn.staatsbladmonitor.be/2026pdf/{REF}.pdf", "pardoes-cdn.pdf")
# HTTPS CDN variants
fetch(f"https://cdn.staatsbladmonitor.be/2026pdf/{REF}.pdf", "pardoes-cdn2.pdf")
fetch(f"http://www.staatsbladmonitor.be/2026pdf/{REF}.pdf", "pardoes-sbm.pdf")

# KBO
fetch(f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={RAW}", "pardoes_kbo.html", extra={"Accept":"text/html"})
fetch(f"https://kbopub.economie.fgov.be/kbopub/toonvestigingps.html?ondernemingsnummer={RAW}", "pardoes_kbo_ve.html", extra={"Accept":"text/html"})

# warm NBB
req=urllib.request.Request("https://consult.cbso.nbb.be/")
req.add_header("User-Agent", UA)
try:
    opener.open(req, timeout=15).read(40)
    print("NBB home ok")
except Exception as e:
    print("NBB home", e)

# official NBB download attempts
for url,name in [
    (f"https://consult.cbso.nbb.be/api/external/broker/public/deposits/{UID}/download","pardoes-nbb-broker.pdf"),
    (f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/{UID}/pdf","pardoes-nbb-pdf.pdf"),
    (f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/{UID}/file","pardoes-nbb-file.bin"),
    (f"https://consult.cbso.nbb.be/consult-deposit/{UID}","pardoes-nbb-page.html"),
]:
    fetch(url, name, extra={"Origin":"https://consult.cbso.nbb.be","Referer":"https://consult.cbso.nbb.be/"})

# Companyweb
fetch(f"https://www.companyweb.be/nl/{RAW}", "pardoes_cw.html")

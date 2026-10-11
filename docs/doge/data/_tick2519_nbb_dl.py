import json, urllib.request, ssl, http.cookiejar, hashlib
from pathlib import Path
ctx=ssl.create_default_context()
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx), urllib.request.HTTPHandler())
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
UUID="a853cf1d-747b-11f1-846f-959060aeeb11"
REF="2026-00251692"
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2519")
TMP=Path("/tmp/tick2519")
OUT.mkdir(parents=True, exist_ok=True)
TMP.mkdir(parents=True, exist_ok=True)

def fetch(url, dest, extra=None):
    req=urllib.request.Request(url)
    req.add_header("User-Agent", UA)
    req.add_header("Accept", "application/pdf,application/octet-stream,*/*")
    if extra:
        for k,v in extra.items():
            req.add_header(k,v)
    try:
        with opener.open(req, timeout=45) as r:
            body=r.read()
            dest.write_bytes(body)
            print("OK", r.status, len(body), r.headers.get("Content-Type"), dest.name, body[:5], hashlib.md5(body).hexdigest())
            return body
    except Exception as e:
        print("FAIL", url[:90], type(e).__name__, e)
        return None

# warm NBB
req=urllib.request.Request("https://consult.cbso.nbb.be/")
req.add_header("User-Agent", UA)
try:
    opener.open(req, timeout=20).read(80)
    print("NBB home OK")
except Exception as e:
    print("NBB home", type(e).__name__, e)

urls = [
    (f"http://cdn.staatsbladmonitor.be/2026pdf/{REF}.pdf", TMP/"terkempen_cdn.pdf", None),
    (f"https://cdn.staatsbladmonitor.be/2026pdf/{REF}.pdf", TMP/"terkempen_cdn_https.pdf", None),
    (f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/{UUID}/pdf", TMP/"terkempen_nbb_pdf.pdf", {"Origin":"https://consult.cbso.nbb.be","Referer":"https://consult.cbso.nbb.be/"}),
    (f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/{UUID}/download", TMP/"terkempen_nbb_dl.pdf", {"Origin":"https://consult.cbso.nbb.be","Referer":"https://consult.cbso.nbb.be/"}),
    (f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/{UUID}/file", TMP/"terkempen_nbb_file.pdf", {"Origin":"https://consult.cbso.nbb.be","Referer":"https://consult.cbso.nbb.be/"}),
    (f"https://consult.cbso.nbb.be/api/rs-consult/deposits/{UUID}/pdf", TMP/"terkempen_nbb_dep.pdf", {"Origin":"https://consult.cbso.nbb.be","Referer":"https://consult.cbso.nbb.be/"}),
]
for url, dest, extra in urls:
    fetch(url, dest, extra)

# also try broker pattern used in prior ticks
try:
    st_req=urllib.request.Request(f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/{UUID}")
    st_req.add_header("User-Agent", UA)
    st_req.add_header("Accept", "application/json")
    st_req.add_header("Origin","https://consult.cbso.nbb.be")
    st_req.add_header("Referer","https://consult.cbso.nbb.be/")
    with opener.open(st_req, timeout=30) as r:
        body=r.read()
        (TMP/"terkempen_depmeta.json").write_bytes(body)
        print("META", r.status, body[:400])
except Exception as e:
    print("META FAIL", type(e).__name__, e)

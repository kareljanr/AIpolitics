import urllib.request, ssl, http.cookiejar
from pathlib import Path
ctx=ssl.create_default_context()
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2474")
UID="98e94f9d-8ccc-11f1-9362-5fa85de4714b"

def fetch(url, name, extra=None):
    req=urllib.request.Request(url)
    req.add_header("User-Agent", UA)
    req.add_header("Accept","*/*")
    if extra:
        for k,v in extra.items():
            req.add_header(k,v)
    try:
        with opener.open(req, timeout=45) as r:
            b=r.read()
            print("OK", r.status, name, "len", len(b), "ct", r.headers.get("content-type"), "cd", r.headers.get("content-disposition"))
            print("  magic", b[:8])
            if name and b:
                (OUT/name).write_bytes(b)
            return r.status, b
    except urllib.error.HTTPError as e:
        body=e.read()
        print("HTTP", e.code, name, body[:220])
        return e.code, body
    except Exception as e:
        print("ERR", name, type(e).__name__, e)
        return 0, b""

# warm SPA
req=urllib.request.Request("https://consult.cbso.nbb.be/")
req.add_header("User-Agent", UA)
opener.open(req, timeout=15).read(80)
print("cookies", [(c.name,c.value[:20]) for c in cj])

extra={"Origin":"https://consult.cbso.nbb.be","Referer":"https://consult.cbso.nbb.be/consult-deposit/"+UID}
for url,name in [
    (f"https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/{UID}","hupskadee-nbb-pdf2.pdf"),
    (f"https://consult.cbso.nbb.be/api/external/broker/public/deposits/xbrl/{UID}","hupskadee-nbb.xbrl"),
    (f"https://consult.cbso.nbb.be/api/external/broker/public/deposits/consult/csv/{UID}","hupskadee-nbb.csv"),
    (f"https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf.zip/published?depositIds={UID}","hupskadee-nbb-zip.bin"),
]:
    fetch(url, name, extra=extra)
print("DONE")

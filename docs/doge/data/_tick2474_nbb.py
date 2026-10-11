import urllib.request, ssl, http.cookiejar, json
from pathlib import Path
ctx=ssl.create_default_context()
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2474")
UID="98e94f9d-8ccc-11f1-9362-5fa85de4714b"
RAW="0863886651"

def fetch(url, name, extra=None, method="GET"):
    req=urllib.request.Request(url, method=method)
    req.add_header("User-Agent", UA)
    req.add_header("Accept","*/*")
    if extra:
        for k,v in extra.items():
            req.add_header(k,v)
    try:
        with opener.open(req, timeout=45) as r:
            b=r.read()
            print(method, r.status, name, "len", len(b), "ct", r.headers.get("content-type"), "cd", r.headers.get("content-disposition"), "lm", r.headers.get("last-modified"))
            if name and b:
                (OUT/name).write_bytes(b)
            return r.status, b
    except urllib.error.HTTPError as e:
        body=e.read()
        print(method, "HTTP", e.code, name, body[:220])
        return e.code, body
    except Exception as e:
        print(method, "ERR", name, type(e).__name__, e)
        return 0, b""

# warm
req=urllib.request.Request("https://consult.cbso.nbb.be/")
req.add_header("User-Agent", UA)
try:
    opener.open(req, timeout=15).read(80)
    print("home ok cookies", len(cj))
except Exception as e:
    print("home", e)

# consult enterprise page (SPA)
fetch(f"https://consult.cbso.nbb.be/consult-enterprise/{RAW}", "nbb_enterprise.html", extra={"Referer":"https://consult.cbso.nbb.be/"})
fetch(f"https://consult.cbso.nbb.be/consult-deposit/{UID}", "nbb_deposit.html", extra={"Referer":"https://consult.cbso.nbb.be/"})

extra={"Origin":"https://consult.cbso.nbb.be","Referer":"https://consult.cbso.nbb.be/"}
urls=[
    (f"https://consult.cbso.nbb.be/api/external/broker/public/deposits/{UID}/download","hupskadee-nbb-broker.pdf"),
    (f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/{UID}/pdf","hupskadee-nbb-pdf.pdf"),
    (f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/{UID}/file","hupskadee-nbb-file.bin"),
    (f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/{UID}","hupskadee-dep-meta.json"),
    (f"https://consult.cbso.nbb.be/api/external/broker/public/deposits/{UID}","hupskadee-broker-meta.json"),
    (f"https://consult.cbso.nbb.be/api/external/broker/public/deposits/{UID}/download?language=nl","hupskadee-nbb-broker-nl.pdf"),
]
for url,name in urls:
    fetch(url, name, extra=extra)

# also try HEAD
fetch(f"https://consult.cbso.nbb.be/api/external/broker/public/deposits/{UID}/download", None, extra=extra, method="HEAD")

# parse deps for more download hints
deps=json.loads((OUT/"hupskadee_deps.json").read_text())
c=deps["content"][0]
print("LATEST KEYS", list(c.keys()))
print(json.dumps({k:c.get(k) for k in c}, indent=2)[:2000])
print("DONE")

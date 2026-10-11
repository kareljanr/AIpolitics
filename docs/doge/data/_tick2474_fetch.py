import urllib.request, ssl, http.cookiejar, json
from pathlib import Path
ctx=ssl.create_default_context()
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2474")
OUT.mkdir(parents=True, exist_ok=True)
REF="2026-00374083"
RAW="0863886651"

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
        body=e.read()
        print(method, "HTTP", e.code, name, body[:180])
        return e.code, body, {}
    except Exception as e:
        print(method, "ERR", name, type(e).__name__, e)
        return 0, b"", {}

# CDN
fetch(f"http://cdn.staatsbladmonitor.be/2026pdf/{REF}.pdf", "hupskadee-cdn.pdf")
fetch(f"https://cdn.staatsbladmonitor.be/2026pdf/{REF}.pdf", "hupskadee-cdn2.pdf")
fetch(f"http://www.staatsbladmonitor.be/2026pdf/{REF}.pdf", "hupskadee-sbm.pdf")

# KBO
fetch(f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={RAW}", "hupskadee_kbo.html", extra={"Accept":"text/html"})
fetch(f"https://kbopub.economie.fgov.be/kbopub/toonvestigingps.html?ondernemingsnummer={RAW}", "hupskadee_kbo_ve.html", extra={"Accept":"text/html"})

# warm NBB
req=urllib.request.Request("https://consult.cbso.nbb.be/")
req.add_header("User-Agent", UA)
try:
    opener.open(req, timeout=15).read(40)
    print("NBB home ok")
except Exception as e:
    print("NBB home", e)

# NBB deposits API
st,body,_=fetch(f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/ids?enterpriseNumber={RAW}", "hupskadee_dep_ids.json", extra={"Origin":"https://consult.cbso.nbb.be","Referer":"https://consult.cbso.nbb.be/","Accept":"application/json"})
print("ids", body[:400])
st,body,_=fetch(f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits?page=0&size=8&enterpriseNumber={RAW}&sort=depositDate,desc", "hupskadee_deps.json", extra={"Origin":"https://consult.cbso.nbb.be","Referer":"https://consult.cbso.nbb.be/","Accept":"application/json"})
if st==200:
    d=json.loads(body)
    for c in d.get("content",[])[:6]:
        print("DEP", c.get("reference"), c.get("periodStartDate"), c.get("periodEndDate"), c.get("depositDate"), c.get("modelName"), c.get("id"))

st,body,_=fetch(f"https://consult.cbso.nbb.be/api/rs-consult/companies/{RAW}/NL", "hupskadee_company.json", extra={"Origin":"https://consult.cbso.nbb.be","Referer":"https://consult.cbso.nbb.be/","Accept":"application/json"})
if st==200:
    d=json.loads(body)
    print("CO", d.get("name"), d.get("postalCode"), d.get("town"), d.get("streetName"), d.get("streetNumber"), d.get("legalForm"), d.get("email"), d.get("website"))

# Companyweb last-balansjaar
fetch(f"https://www.companyweb.be/nl/{RAW}", "hupskadee_cw.html")
print("DONE")

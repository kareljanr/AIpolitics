import json, urllib.request, ssl, http.cookiejar, re
from pathlib import Path
ctx=ssl.create_default_context()
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
RAW="0448731106"
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2473")
OUT.mkdir(parents=True, exist_ok=True)

def get(url, accept="application/json, text/plain, */*"):
    req=urllib.request.Request(url)
    req.add_header("User-Agent", UA)
    req.add_header("Accept", accept)
    req.add_header("Origin","https://consult.cbso.nbb.be")
    req.add_header("Referer","https://consult.cbso.nbb.be/")
    with opener.open(req, timeout=30) as r:
        return r.status, r.geturl(), r.headers, r.read()

# warm cookies
req=urllib.request.Request("https://consult.cbso.nbb.be/")
req.add_header("User-Agent", UA)
try:
    opener.open(req, timeout=20).read(80)
    print("NBB home OK")
except Exception as e:
    print("NBB home", type(e).__name__, e)

# company
try:
    st, url, hdr, body = get(f"https://consult.cbso.nbb.be/api/rs-consult/companies/{RAW}/NL")
    (OUT/"tsas_company.json").write_bytes(body)
    d=json.loads(body)
    print("CO", d.get("name"), d.get("postalCode"), d.get("town"), d.get("legalForm"), d.get("streetName"), d.get("streetNumber"), d.get("enterpriseNumber"))
    print("CO keys", list(d.keys())[:30])
except Exception as e:
    print("CO FAIL", type(e).__name__, e)

# deposit ids
try:
    st, url, hdr, body = get(f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/ids?enterpriseNumber={RAW}")
    (OUT/"tsas_ids.json").write_bytes(body)
    ids=json.loads(body)
    print("IDS n", len(ids) if isinstance(ids,list) else type(ids))
    if isinstance(ids, list):
        for x in ids[:8]:
            print(" ID", x)
except Exception as e:
    print("IDS FAIL", type(e).__name__, e)

# deposits page
try:
    st, url, hdr, body = get(f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits?page=0&size=8&enterpriseNumber={RAW}")
    (OUT/"tsas_deps.json").write_bytes(body)
    d=json.loads(body)
    content=d.get("content") or d
    if isinstance(content, list):
        for c in content[:8]:
            print("DEP", c.get("reference"), "YE", c.get("periodEndDate"), "filed", c.get("depositDate"), c.get("modelName"), c.get("importFileType"), "uuid", c.get("id") or c.get("depositId") or c.get("uuid"))
            print("  keys", list(c.keys()))
    else:
        print("DEP raw", str(d)[:400])
except Exception as e:
    print("DEP FAIL", type(e).__name__, e)

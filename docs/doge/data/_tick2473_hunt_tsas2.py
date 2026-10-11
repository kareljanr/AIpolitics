import json, urllib.request, ssl, http.cookiejar, re
from pathlib import Path
ctx=ssl.create_default_context()
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
RAW="0448731106"
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2473")

def get(url, accept="application/json, text/plain, */*", extra=None):
    req=urllib.request.Request(url)
    req.add_header("User-Agent", UA)
    req.add_header("Accept", accept)
    req.add_header("Origin","https://consult.cbso.nbb.be")
    req.add_header("Referer","https://consult.cbso.nbb.be/")
    if extra:
        for k,v in extra.items():
            req.add_header(k,v)
    try:
        with opener.open(req, timeout=30) as r:
            return r.status, r.geturl(), dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, url, dict(e.headers), e.read()

req=urllib.request.Request("https://consult.cbso.nbb.be/")
req.add_header("User-Agent", UA)
opener.open(req, timeout=20).read(80)

ids=json.loads((OUT/"tsas_ids.json").read_text())
print("ALL IDS", len(ids))
non_mig=[x for x in ids if not x.get("migration")]
print("non-migration", len(non_mig))
for x in ids:
    print(x.get("id"), x.get("importFileType"), "mig", x.get("migration"))

# try per-deposit endpoints for non-migration first then first few
cands = non_mig + [x for x in ids if x.get("migration")][:4]
for x in cands:
    uid=x["id"]
    for url in [
        f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/{uid}",
        f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/{uid}/NL",
        f"https://consult.cbso.nbb.be/api/external/broker/public/deposits/{uid}",
        f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/{uid}/download",
    ]:
        st, u, hdr, body = get(url)
        print(st, url.split("/")[-2:], "len", len(body), body[:120])
        if st==200 and len(body)>200:
            (OUT/f"dep_{uid[:8]}.bin").write_bytes(body[:200000])

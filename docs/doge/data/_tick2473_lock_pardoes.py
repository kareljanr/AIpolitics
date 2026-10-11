import csv, sys, json, urllib.request, ssl, http.cookiejar, re
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA=Path("/workspace/AIpolitics/docs/doge/data")
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2473")
OUT.mkdir(parents=True, exist_ok=True)

needles=["0417.400.205","0417400205","417400205","pardoes"]
hits=[]
with open(DATA/"entities.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        blob=" ".join((row.get(k) or "") for k in row).lower()
        if any(n.lower() in blob for n in needles):
            # exclude mere skip-mentions in notes of other entities? still print
            hits.append((row["entity_id"], row.get("name_nl"), row.get("parent_id"), (row.get("notes") or "")[:100]))
print("PARDOES ENTITY HITS", len(hits))
for h in hits:
    print(h)

# Hupskadee unused check too
needles2=["0863.886.651","0863886651","hupskadee"]
hits2=[]
with open(DATA/"entities.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        blob=" ".join((row.get(k) or "") for k in row).lower()
        if any(n.lower() in blob for n in needles2):
            hits2.append((row["entity_id"], row.get("name_nl"), row.get("parent_id")))
print("HUPSKADEE ENTITY HITS", len(hits2))
for h in hits2:
    print(h)

ctx=ssl.create_default_context()
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def get(url, accept="application/json"):
    req=urllib.request.Request(url)
    req.add_header("User-Agent", UA)
    req.add_header("Accept", accept)
    req.add_header("Origin","https://consult.cbso.nbb.be")
    req.add_header("Referer","https://consult.cbso.nbb.be/")
    try:
        with opener.open(req, timeout=30) as r:
            return r.status, r.read(), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, e.read(), dict(e.headers)

req=urllib.request.Request("https://consult.cbso.nbb.be/")
req.add_header("User-Agent", UA)
opener.open(req, timeout=15).read(40)

# company + full latest deposit
for raw,label in [("0417400205","pardoes"),("0863886651","hupskadee")]:
    st,body,hdr=get(f"https://consult.cbso.nbb.be/api/rs-consult/companies/{raw}/NL")
    print("\nCO", label, st)
    if st==200:
        d=json.loads(body)
        (OUT/f"{label}_company.json").write_bytes(body)
        print(d.get("name"), d.get("postalCode"), d.get("town"), d.get("streetName"), d.get("streetNumber"), d.get("legalForm"), d.get("email"), d.get("website"))
    st,body,hdr=get(f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits?page=0&size=5&enterpriseNumber={raw}&sort=depositDate,desc")
    if st==200:
        d=json.loads(body)
        (OUT/f"{label}_deps.json").write_text(json.dumps(d, indent=2)[:200000])
        c=d["content"][0]
        print("LATEST", label, c.get("reference"), c.get("periodEndDateYear"), c.get("periodStartDate"), c.get("periodEndDate"), c.get("depositDate"), c.get("modelName"), c.get("id"))
        print(" keys", list(c.keys()))
        print(" extra", {k:c.get(k) for k in c if k in ("reference","depositNumber","fileType","importFileType","language","modelType","modelName","periodEndDateYear")})

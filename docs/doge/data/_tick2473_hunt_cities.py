import csv, sys, json, urllib.request, ssl, http.cookiejar
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA=Path("/workspace/AIpolitics/docs/doge/data")
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2473")

want=["city_mechelen","city_herentals","city_schoten","city_vilvoorde","city_geel","city_mol","city_denderleeuw","city_begijnendijk"]
with open(DATA/"entities.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row["entity_id"] in want:
            print("CITY", row["entity_id"], row.get("name_nl"), (row.get("notes") or "")[:80])

# leftover CIK already in those cities?
print("\n==== existing leftover entities parented to those cities ====")
with open(DATA/"entities.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row.get("parent_id") in want:
            print(row["parent_id"], "->", row["entity_id"], row.get("name_nl"), (row.get("notes") or "")[:90])

# save t Sas deposits that worked
ctx=ssl.create_default_context()
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
req=urllib.request.Request("https://consult.cbso.nbb.be/")
req.add_header("User-Agent", UA)
opener.open(req, timeout=15).read(40)

def nbb_deps(raw):
    url=f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits?page=0&size=8&enterpriseNumber={raw}&sort=depositDate,desc"
    req=urllib.request.Request(url)
    req.add_header("User-Agent", UA)
    req.add_header("Accept","application/json")
    req.add_header("Origin","https://consult.cbso.nbb.be")
    req.add_header("Referer","https://consult.cbso.nbb.be/")
    with opener.open(req, timeout=25) as r:
        return json.loads(r.read())

d=nbb_deps("0448731106")
(OUT/"tsas_deps.json").write_text(json.dumps(d, indent=2)[:200000])
print("\n==== t Sas latest deps ====")
for c in (d.get("content") or [])[:5]:
    print(c.get("reference"), "YEy", c.get("periodEndDateYear"), c.get("periodEndDate"), "filed", c.get("depositDate"), c.get("modelName"), c.get("id"))

# HEAD-only known near-misses in target cities
known=[
    ("0448186520","Molleke mol"),
    ("0417400205","Pardoes mechelen"),
    ("0882468881","KIOS schoten"),
    ("0863886651","Hupskadee begijnendijk"),
    ("0439731880","Dol-Fijn turnhout"),
]
print("\n==== known near-miss last year ====")
for raw,label in known:
    try:
        d=nbb_deps(raw)
        c=(d.get("content") or [None])[0]
        if c:
            print(label, raw, "ref", c.get("reference"), "YEy", c.get("periodEndDateYear"), "end", c.get("periodEndDate"), "model", c.get("modelName"))
        else:
            print(label, raw, "NO CONTENT", str(d)[:160])
    except Exception as e:
        print(label, "FAIL", type(e).__name__, e)

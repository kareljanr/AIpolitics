import urllib.request, ssl, re, json
from pathlib import Path
ctx=ssl.create_default_context()
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2473")
RAW="0448731106"

def fetch(url, name=None):
    req=urllib.request.Request(url)
    req.add_header("User-Agent", UA)
    req.add_header("Accept","text/html,application/json,*/*")
    try:
        with urllib.request.urlopen(req, timeout=22, context=ctx) as r:
            b=r.read()
            print("OK", r.status, url[:90], "len", len(b), r.headers.get("content-type"))
            if name:
                (OUT/name).write_bytes(b)
            return b
    except urllib.error.HTTPError as e:
        print("HTTP", e.code, url[:90], e.read()[:160])
        return b""
    except Exception as e:
        print("ERR", type(e).__name__, url[:90], e)
        return b""

# Companyweb jaarrekening / financieel
for url,name in [
    (f"https://www.companyweb.be/nl/{RAW}/kinderdagverblijf-t-sas/jaarrekening","tsas_cw_jr.html"),
    (f"https://www.companyweb.be/nl/{RAW}/kinderdagverblijf-t-sas","tsas_cw2.html"),
    (f"https://www.staatsbladmonitor.be/europese-jaarrekening.html?ondernemingsnummer={RAW}","tsas_sbm_eu.html"),
    (f"https://www.staatsbladmonitor.be/financiele-analyse.html?ondernemingsnummer={RAW}","tsas_sbm_fin.html"),
]:
    b=fetch(url,name)
    if not b: continue
    t=b.decode("utf-8","replace")
    print("  refs", re.findall(r"20[12][0-9]-[0-9]{8}", t)[:12])
    print("  2026pdf", re.findall(r"2026pdf/[^\"']+", t)[:8])
    print("  balans", re.findall(r"Laatste balansjaar.{0,40}", t, re.I)[:3])
    print("  years", re.findall(r"boekjaar.{0,40}20[12][0-9]", t, re.I)[:5])

# KBO VE page
kbo= (OUT/"tsas_kbo.html").read_text(encoding="utf-8", errors="replace")
for m in re.finditer(r'href="([^"]*vestig[^"]*)"', kbo, re.I):
    print("KBO HREF", m.group(1))
for m in re.finditer(r'href="([^"]*toonvestiging[^"]*)"', kbo, re.I):
    print("KBO VE", m.group(1))

# try NBB consult page API variants that returned 500 before with different sizes
import http.cookiejar
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))
req=urllib.request.Request("https://consult.cbso.nbb.be/")
req.add_header("User-Agent", UA)
opener.open(req, timeout=15).read(40)

urls=[
    f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits?page=0&size=20&enterpriseNumber={RAW}&sort=depositDate,desc",
    f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits?enterpriseNumber={RAW}&page=0&size=3",
    f"https://consult.cbso.nbb.be/api/rs-consult/companies/{RAW}/published-deposits",
    f"https://consult.cbso.nbb.be/api/rs-consult/published-deposits/search?enterpriseNumber={RAW}",
    f"https://consult.cbso.nbb.be/api/rs-consult/deposits?enterpriseNumber={RAW}",
]
for url in urls:
    req=urllib.request.Request(url)
    req.add_header("User-Agent", UA)
    req.add_header("Accept","application/json")
    req.add_header("Origin","https://consult.cbso.nbb.be")
    req.add_header("Referer","https://consult.cbso.nbb.be/")
    try:
        with opener.open(req, timeout=20) as r:
            b=r.read()
            print("API", r.status, url.split("nbb.be")[-1][:80], b[:180])
    except urllib.error.HTTPError as e:
        print("API HTTP", e.code, url.split("nbb.be")[-1][:80], e.read()[:120])
    except Exception as e:
        print("API ERR", type(e).__name__, e)

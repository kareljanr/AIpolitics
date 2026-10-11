import urllib.request, ssl, re
from pathlib import Path
ctx=ssl.create_default_context()
RAW="0448731106"
OUT=Path("/workspace/AIpolitics/docs/doge/raw/tick2473")
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def fetch(url, name):
    req=urllib.request.Request(url)
    req.add_header("User-Agent", UA)
    req.add_header("Accept","text/html,application/xhtml+xml,application/json,*/*")
    try:
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            body=r.read()
            print("====", name, r.status, r.geturl(), "len", len(body), "ct", r.headers.get("content-type"))
            (OUT/f"{name}").write_bytes(body)
            return body
    except urllib.error.HTTPError as e:
        print("====", name, "HTTP", e.code, url, e.read()[:200])
        return b""
    except Exception as e:
        print("====", name, type(e).__name__, e)
        return b""

# Companyweb
cw=fetch(f"https://www.companyweb.be/nl/{RAW}", "tsas_cw.html")
if cw:
    text=cw.decode("utf-8","replace")
    print(" title", (re.search(r"<title>([^<]+)</title>", text) or type("x",(object,),{"group":lambda s,i: "?"})()).group(1)[:120])
    for pat in ["laatste balansjaar","Laatste jaarrekening","Stopgezet","Actief","2025","2026-","neerlegg"]:
        print("  has", pat, pat.lower() in text.lower())
    refs=re.findall(r"20[12][0-9]-[0-9]{8}", text)
    print("  refs", refs[:15])
    idx=text.lower().find("laatste balansjaar")
    if idx>=0:
        chunk=re.sub(r"<[^>]+>"," ", text[idx:idx+400])
        print("  balans chunk", re.sub(r"\s+"," ", chunk)[:250])
    idx=text.lower().find("jaarrekening")
    if idx>=0:
        chunk=re.sub(r"<[^>]+>"," ", text[idx:idx+400])
        print("  jr chunk", re.sub(r"\s+"," ", chunk)[:250])

# SBM
for url,name in [
    (f"https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer={RAW}","tsas_sbm.html"),
    (f"https://www.staatsbladmonitor.be/jaarrekening.html?ondernemingsnummer={RAW}","tsas_sbm_jr.html"),
    (f"https://consult.cbso.nbb.be/consult-enterprise/{RAW}","tsas_nbb_html.html"),
    (f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={RAW}","tsas_kbo.html"),
]:
    b=fetch(url, name)
    if not b: continue
    text=b.decode("utf-8","replace")
    refs=re.findall(r"20[12][0-9]-[0-9]{8}", text)
    pdfs=re.findall(r"2026pdf/[^\"']+", text)
    print("  refs", refs[:20], "pdfs", pdfs[:8], "2025?", "2025" in text, "title", (re.search(r"<title>([^<]+)</title>", text) or type("x",(object,),{"group":lambda s,i:"?"})()).group(1)[:80])

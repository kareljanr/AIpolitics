import urllib.request, ssl, re
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}

# Probe NBB consult enterprise page + known search endpoints
urls = [
    "https://consult.cbso.nbb.be/api/enterprise/0448190181",
    "https://consult.cbso.nbb.be/api/filings?enterpriseNumber=0448190181",
    "https://consult.cbso.nbb.be/consult-enterprise/0448190181",
]
for u in urls:
    try:
        req = urllib.request.Request(u, headers={**ua, "Accept": "application/json,text/html"})
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            data = r.read()
            ct = r.headers.get("content-type", "")
            print(u, r.status, ct, len(data))
            text = data.decode("utf-8", "replace")
            deps = sorted(set(re.findall(r"2026-00\d{5}", text)))
            print("  deps", deps[:20])
            Path("docs/doge/raw/tick1734/probe_" + u.split("/")[-1].replace("?", "_")[:40] + ".txt").write_text(text[:5000], encoding="utf-8")
    except Exception as e:
        print(u, type(e).__name__, e)

# companyweb page
try:
    u = "https://www.companyweb.be/nl/0448190181/woon-en-zorgcentrum-sint-jozef-vzw"
    req = urllib.request.Request(u, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        text = r.read().decode("utf-8", "replace")
    print("companyweb", len(text))
    deps = sorted(set(re.findall(r"2026-00\d{5}", text)))
    print("cw deps", deps)
    for m in re.findall(r".{0,40}neerlegging.{0,80}", text, re.I)[:10]:
        print("  ", m)
except Exception as e:
    print("cw", type(e).__name__, e)

# staatsbladmonitor bedrijfsfiche
try:
    u = "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0448190181"
    req = urllib.request.Request(u, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        text = r.read().decode("utf-8", "replace")
    print("sbm", len(text))
    deps = sorted(set(re.findall(r"2026-00\d{5}", text)))
    print("sbm deps", deps)
    for m in re.findall(r".{0,60}jaarrekening.{0,120}", text, re.I)[:15]:
        print("  ", m.replace("\n", " ")[:180])
    Path("docs/doge/raw/tick1734/sbm_sintjozef.html").write_text(text, encoding="utf-8")
except Exception as e:
    print("sbm", type(e).__name__, e)

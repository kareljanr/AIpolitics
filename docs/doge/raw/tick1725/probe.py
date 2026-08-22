import urllib.request, ssl, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}

def head(url):
    try:
        req=urllib.request.Request(url, method="HEAD", headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            return resp.status, resp.getheader("Content-Length"), resp.getheader("Content-Type")
    except Exception as e:
        return type(e).__name__, getattr(e,"code",None), str(e)[:120]

# probe known blocked + NSZ
probes=[
 ("dijk92","http://cdn.staatsbladmonitor.be/2026pdf/2026-00377886.pdf"),
 ("faro_jr2024ish","http://cdn.staatsbladmonitor.be/2025pdf/2025-00569658.pdf"),
]
for name,u in probes:
    print(name, head(u))

# NSZ staatsbladmonitor / companyweb for deposit id
for url in [
 "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0410357609",
 "https://northdata.com/Neutraal%20Syndicaat%20voor%20Zelfstandigen%20VZW,%20Brussel/KBO%200410.357.609",
 "https://www.companyweb.be/nl/0410357609/neutraal-syndicaat-voor-zelfstandigen",
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            html=resp.read().decode("utf-8","replace")
        print("\nURL", url, "len", len(html), "status", resp.status)
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        print("deps", deps[-20:])
        pdfs=re.findall(r"cdn\.staatsbladmonitor[^\"' ]+\.pdf|2026pdf/[^\"' ]+", html)
        print("pdfs", pdfs[:15])
        for pat in ["2025","2026","neerlegging","bruto","Gross","jaarrekening"]:
            pass
        # print snippets with 2026-
        for m in re.finditer(r".{0,50}2026-\d{8}.{0,80}", html):
            print("CTX", re.sub(r"\s+"," ", m.group(0))[:200])
    except Exception as e:
        print("FAIL", url, type(e).__name__, getattr(e,"code",None), e)

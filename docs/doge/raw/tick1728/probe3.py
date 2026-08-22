import urllib.request, ssl, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}

def cdn(dep, year="2026"):
    u=f"http://cdn.staatsbladmonitor.be/{year}pdf/{dep}.pdf"
    try:
        req=urllib.request.Request(u, method="HEAD", headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
            return resp.status, int(resp.getheader("Content-Length") or 0)
    except Exception as e:
        return getattr(e,"code",None), type(e).__name__

# companyweb for IOED candidates
for name,url in [
 ("Viersprong","https://www.companyweb.be/nl/0809450251/projectvereniging-viersprong"),
 ("VARIANT","https://www.companyweb.be/nl/0738732697/variant"),
 ("Noordrand","https://www.companyweb.be/nl/0740822256/intergemeentelijk-samenwerkingsverband-voor-cultuur-noordrand"),
 ("Haspengouw","https://www.companyweb.be/nl/0548989217/projectvereniging-erfgoed-haspengouw"),
 ("BosgroepLim","https://www.companyweb.be/nl/0668619317/bosgroep-limburg"),
 ("AGBHulshout","https://www.companyweb.be/nl/0809823801/agb-hulshout"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            html=resp.read().decode("utf-8","replace")
        print(name, "len", len(html))
        for pat in [r"Laatste balansjaar.{0,80}", r"neergelegd op.{0,50}", r"geen jaarrekening", r"Brutomarge.{0,60}", r"2025.{0,40}"]:
            m=re.search(pat, html, re.I|re.S)
            if m:
                print(" ", re.sub(r"\s+"," ", m.group(0))[:130])
    except Exception as e:
        print(name, "FAIL", type(e).__name__, getattr(e,"code",None))

# try official JR for leftover orgs - e.g. POV budget, or VBO/FEB, or ACV
# also probe known deferred KBOs with northdata
for name,url in [
 ("BosgroepLimND","https://www.northdata.com/?query=0668.619.317"),
 ("AGBHulshoutND","https://www.northdata.com/?query=0809.823.801"),
 ("WinArKBO","https://www.northdata.com/?query=0811.517.440"),
 ("BruggeOmmelandKBO","https://www.northdata.com/?query=0554.701.428"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        links=re.findall(r'href="(/[^"]*KBO%20[0-9.]+[^"]*)"', html)[:2]
        print(name, "deps", deps[-8:], "links", links)
        for d in deps[::-1]:
            if d.startswith("2026-"):
                print(" ", d, cdn(d))
                break
    except Exception as e:
        print(name, "FAIL", type(e).__name__)

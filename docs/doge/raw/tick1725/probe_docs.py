import urllib.request, ssl, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}

def cdn(dep):
    u=f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf"
    try:
        req=urllib.request.Request(u, method="HEAD", headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            return resp.status, int(resp.getheader("Content-Length") or 0)
    except Exception as e:
        return getattr(e,"code",None), type(e).__name__

print("scwitch", cdn("2026-00232537"))

# northdata for promising unused orgs
for name,url in [
 ("Scwitch","https://www.northdata.com/?query=Scwitch+VZW"),
 ("VVT","https://www.northdata.com/?query=Vlaamse+Vereniging+voor+Tandheelkunde"),
 ("ASGB","https://www.northdata.com/?query=Algemeen+Syndicaat+van+Geneeskundigen"),
 ("GBO","https://www.northdata.com/?query=GBO+huisartsen"),
 ("BVAS","https://www.northdata.com/?query=Belgische+Vereniging+van+Artsensyndicaten"),
 ("Orde","https://www.northdata.com/?query=Orde+der+Artsen+Belgi%C3%AB"),
 ("FARO","https://www.northdata.com/?query=FARO+Vlaams+steunpunt+cultureel+erfgoed"),
 ("APEFE","https://www.northdata.com/?query=APEFE"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        # company links
        links=re.findall(r'href="(/[^"]+KBO%20[0-9.]+[^"]*)"', html)[:5]
        print(name, "deps", deps[-8:], "links", links[:3], "len", len(html))
    except Exception as e:
        print(name, "FAIL", type(e).__name__, getattr(e,"code",None))

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

# recheck blocked
for dep,label in [
 ("2026-00394221","NSZ"),
 ("2026-00377886","Dijk92"),
 ("2026-00375176","APEFE"),
]:
    print(label, cdn(dep))

# unused IOED / HVZ / other from prior next lists
cands = [
 ("WinAr","https://www.northdata.com/?query=WinAr+erfgoed+OR+IOED+WinAr"),
 ("PORTIVA","https://www.northdata.com/?query=PORTIVA+OR+Portiva+erfgoed"),
 ("VARIANT","https://www.northdata.com/?query=VARIANT+IOED+OR+Projectvereniging+VARIANT"),
 ("BruggeOmmeland","https://www.northdata.com/?query=Brugge+en+Ommeland+erfgoed"),
 ("LandNeteAa","https://www.northdata.com/?query=Land+van+Nete+en+Aa"),
 ("Viersprong","https://www.northdata.com/?query=Viersprong+erfgoed+IOED"),
 ("Zender","https://www.northdata.com/?query=Zender+cultuur+IGS+OR+Projectvereniging+Zender"),
 ("CultuurNoordrand","https://www.northdata.com/?query=Cultuur+Noordrand"),
 ("IVAREM","https://www.northdata.com/?query=IVAREM+intercommunale"),
 ("KempensKarakter","https://www.northdata.com/?query=Kempens+Karakter"),
]
for name,url in cands:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        links=re.findall(r'href="(/[^"]*KBO%20[0-9.]+[^"]*)"', html)[:3]
        print(name, "deps", deps[-6:], "links", links)
        for d in deps[::-1]:
            if d.startswith("2026-"):
                print(" ", d, cdn(d))
                break
    except Exception as e:
        print(name, "FAIL", type(e).__name__, getattr(e,"code",None))

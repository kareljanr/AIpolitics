import urllib.request, ssl, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}

def cdn(dep, year="2026"):
    u=f"http://cdn.staatsbladmonitor.be/{year}pdf/{dep}.pdf"
    try:
        req=urllib.request.Request(u, method="HEAD", headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            return resp.status, int(resp.getheader("Content-Length") or 0)
    except Exception as e:
        return getattr(e,"code",None), type(e).__name__

# recheck blocked
for dep,label in [
 ("2026-00394221","NSZ"),
 ("2026-00377886","Dijk92"),
 ("2026-00375176","APEFE"),
 ("2025-00569658","FARO_jr2024"),
]:
    y="2025" if dep.startswith("2025") else "2026"
    print(label, dep, cdn(dep,y))

# POV / BVAS / leftover candidates via northdata
for name,url in [
 ("POV","https://www.northdata.com/Provinciaal%20Onderwijs%20Vlaanderen%20VZW,%20Bruxelles/KBO%200445.224.456"),
 ("BVAS","https://www.northdata.com/?query=BVAS+artsensyndicaten"),
 ("Kartel","https://www.northdata.com/?query=Kartel+artsen+syndicaat"),
 ("GBO","https://www.northdata.com/?query=%22GBO-MBO%22+OR+Huisartsenvereniging"),
 ("BosgroepHoutland","https://www.northdata.com/?query=Bosgroep+Houtland"),
 ("BosgroepIJzer","https://www.northdata.com/?query=Bosgroep+IJzer+en+Polder"),
 ("BosgroepLimburgVZW","https://www.northdata.com/Bosgroep%20Limburg%20VZW,%20Hasselt/KBO%200668.619.317"),
 ("IVAREM","https://www.northdata.com/?query=IVAREM"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        links=re.findall(r'href="(/[^"]*KBO%20[0-9.]+[^"]*)"', html)[:4]
        print(name, "deps", deps[-8:], "links", links[:3])
    except Exception as e:
        print(name, "FAIL", type(e).__name__, getattr(e,"code",None))

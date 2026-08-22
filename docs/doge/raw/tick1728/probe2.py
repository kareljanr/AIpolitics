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

for name,url in [
 ("VARIANT","https://www.northdata.com/Variant%20PROJ%20V,%20Zwalm/KBO%200738.732.697"),
 ("Viersprong","https://www.northdata.com/Projectvereniging%20Viersprong,%20Oosterzele/KBO%200809.450.251"),
 ("Haspengouw","https://www.northdata.com/Projectvereniging%20Erfgoed%20Haspengouw,%20Sint-Truiden/KBO%200548.989.217"),
 ("Noordrand","https://www.northdata.com/Intergemeentelijk%20Samenwerkingsverband%20Voor%20Cultuur%20Noordrand%20PROJ%20V,%20Grimbergen/KBO%200740.822.256"),
 ("WinAr2","https://www.companyweb.be/nl/search?q=WinAr+erfgoed"),
 ("IOEDHydra","https://www.northdata.com/?query=0811.517.440+OR+Hydra+projectvereniging"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        print(name, "deps", deps[-10:])
        for d in deps[::-1]:
            if d.startswith("2026-") or d.startswith("2025-"):
                y="2025" if d.startswith("2025") else "2026"
                print(" ", d, cdn(d,y))
                if d.startswith("2026-"):
                    break
    except Exception as e:
        print(name, "FAIL", type(e).__name__, getattr(e,"code",None))

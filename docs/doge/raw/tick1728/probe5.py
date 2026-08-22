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
 ("LSC_Kempen","https://www.northdata.com/Leersteuncentrum%20Kempen%20VZW,%20Geel/KBO%200801.066.976"),
 ("LSC_OostBrabant","https://www.northdata.com/Leersteuncentrum%20Oost-Brabant%20VZW,%20Leuven/KBO%200800.106.082"),
 ("LSC_NoordBrabant","https://www.northdata.com/Leersteuncentrum%20Noord-Brabant%20VZW,%20Mechelen/KBO%200799.959.988"),
 ("LSC_AntPlus","https://www.northdata.com/VZW%20Leersteuncentrum%20Antwerpen%20Plus,%20Mortsel/KBO%200801.621.361"),
 ("WZC_Haagwinde","https://www.northdata.com/Woonzorgcentrum%20Haagwinde%20VZW,%20Maarkedal/KBO%200410.219.433"),
 ("WZC_WitteMeren","https://www.northdata.com/Woonzorgcentrum%20Witte%20Meren%20VZW,%20Mol/KBO%200418.234.997"),
 ("WZC_TerEngelen","https://www.northdata.com/Woonzorgcentrum%20Ter%20Engelen%20VZW,%20Lokeren/KBO%200430.882.809"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        print(name, "deps", deps[-8:])
        for d in deps[::-1]:
            if d.startswith("2026-"):
                print(" ", d, cdn(d))
                break
            if d.startswith("2025-") and not any(x.startswith("2026-") for x in deps):
                print(" ", d, cdn(d,"2025"))
                break
    except Exception as e:
        print(name, "FAIL", type(e).__name__, getattr(e,"code",None))

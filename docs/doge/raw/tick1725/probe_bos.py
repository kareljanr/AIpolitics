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

print("bos 2026-00159428", cdn("2026-00159428"))
print("bos 2025-00147901", cdn("2025-00147901","2025"))

# company pages
for name,url in [
 ("BosgroepOVL","https://www.northdata.com/Bosgroep%20Oost-Vlaanderen%20VZW,%20Gent/KBO%200803.977.372"),
 ("BosgroepMidden","https://www.northdata.com/Bosgroep%20Midden%20Oost-Vlaanderen%20VZW,%20Gent/KBO%200890.587.286"),
 ("BosgroepNoord","https://www.northdata.com/Bosgroep%20Oost-Vlaanderen%20Noord%20VZW,%20Gent/KBO%200865.959.877"),
 ("BosgroepLimCV","https://www.northdata.com/Co%C3%B6peratieve%20Van%20de%20Limburgse%20Bosgroepen%20CV,%20Hasselt/KBO%200890.220.171"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        print(name, "deps", deps[-8:])
        for d in deps[::-1]:
            if d.startswith("2026-") or d.startswith("2025-"):
                y=d[:4]
                print(" ", d, cdn(d, y if y=="2025" else "2026"))
    except Exception as e:
        print(name, "FAIL", type(e).__name__, getattr(e,"code",None))

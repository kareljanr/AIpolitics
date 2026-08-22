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

print("Erfpunt", cdn("2026-00165556"))
print("Erfpunt2025", cdn("2025-00095296","2025"))

for name,url in [
 ("Erfpunt","https://www.northdata.com/?query=Erfpunt+VZW+OR+Intergemeentelijke+Erfgoeddienst+Erfpunt"),
 ("DommelhofVZW","https://www.northdata.com/Dommelhof%20VZW,%20Tielt-Winge/KBO%200443.049.478"),
 ("DommelhofNV","https://www.northdata.com/Dommelhof%20N%C2%B7V%C2%B7,%20Tielt-Winge/KBO%200433.155.577"),
 ("PORTIVA","https://www.northdata.com/?query=PORTIVA+erfgoed"),
 ("VARIANT","https://www.northdata.com/?query=VARIANT+erfgoed+IOED"),
 ("Hydra","https://www.northdata.com/?query=Hydra+erfgoed+IOED"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        links=re.findall(r'href="(/[^"]*KBO%20[0-9.]+[^"]*)"', html)[:4]
        print(name, "deps", deps[-8:], "links", links[:3])
        for d in deps[::-1]:
            if d.startswith("2026-"):
                print(" ", d, cdn(d))
                break
    except Exception as e:
        print(name, "FAIL", type(e).__name__, getattr(e,"code",None))
